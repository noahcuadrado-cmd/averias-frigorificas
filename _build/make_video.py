#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera un MP4 de un video del curso: renderiza cada diapositiva (HTML->PNG con
Chromium) y la sincroniza con su audio WAV. Diapositiva sin audio -> 4 s.
Uso: python3 make_video.py <slides.json> "<pie>" <prefijo tXXvN> <wav_dir> <salida.mp4> [tmp_dir]
"""
import sys, os, json, subprocess, wave, contextlib, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import slide_html as SH
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
CHROME = "/opt/pw-browsers/chromium"

def dur_wav(p):
    with contextlib.closing(wave.open(p,'rb')) as w:
        return w.getnframes()/float(w.getframerate())

def render_pngs(slides, pie, tmp):
    from playwright.sync_api import sync_playwright
    paths=[]
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        pg=b.new_page(viewport={'width':1920,'height':1080}, device_scale_factor=1)
        total=len(slides)
        for i,s in enumerate(slides,1):
            html=SH.render(s,i,total,pie)
            pg.set_content(html, wait_until='networkidle')
            out=os.path.join(tmp,f"s{i:03d}.png")
            pg.screenshot(path=out, clip={'x':0,'y':0,'width':1920,'height':1080})
            paths.append(out)
        b.close()
    return paths

def seg(png, wav, out, tmp_idx):
    """Crea un segmento mp4: imagen fija durante (dur audio + 0.7s), con audio."""
    if wav and os.path.exists(wav):
        total=dur_wav(wav)+0.7
        cmd=[FF,'-y','-loglevel','error','-loop','1','-i',png,'-i',wav,
             '-filter_complex','[1:a]apad=pad_dur=0.7,aresample=48000[a]',
             '-map','0:v','-map','[a]','-t',f'{total:.3f}',
             '-r','25','-c:v','libx264','-pix_fmt','yuv420p','-vf','scale=1920:1080',
             '-c:a','aac','-b:a','160k','-ac','2','-ar','48000',out]
    else:
        total=4.0
        cmd=[FF,'-y','-loglevel','error','-loop','1','-i',png,
             '-f','lavfi','-t','4','-i','anullsrc=r=48000:cl=stereo',
             '-map','0:v','-map','1:a','-t','4',
             '-r','25','-c:v','libx264','-pix_fmt','yuv420p','-vf','scale=1920:1080',
             '-c:a','aac','-b:a','160k','-ar','48000',out]
    subprocess.run(cmd,check=True)
    return total

def main():
    sj,pie,pref,wavdir,outmp4 = sys.argv[1:6]
    tmp = sys.argv[6] if len(sys.argv)>6 else tempfile.mkdtemp()
    os.makedirs(tmp,exist_ok=True)
    data=json.load(open(sj,encoding="utf-8"))
    slides=SH.prepare(data["slides"])
    print(f"Diapositivas: {len(slides)}")
    pngs=render_pngs(slides,pie,tmp)
    print("PNGs renderizados.")
    segs=[]; tot=0
    for i,png in enumerate(pngs,1):
        wav=os.path.join(wavdir,f"{pref}_{i:03d}.wav")
        so=os.path.join(tmp,f"seg{i:03d}.mp4")
        d=seg(png, wav if os.path.exists(wav) else None, so, i)
        segs.append(so); tot+=d
        print(f"  seg {i}/{len(pngs)}  {d:.1f}s")
    listf=os.path.join(tmp,"list.txt")
    open(listf,"w").write("\n".join(f"file '{s}'" for s in segs))
    subprocess.run([FF,'-y','-loglevel','error','-f','concat','-safe','0','-i',listf,
                    '-c','copy',outmp4],check=True)
    print(f"MP4: {outmp4}  ({tot/60:.1f} min)")

if __name__=="__main__":
    main()
