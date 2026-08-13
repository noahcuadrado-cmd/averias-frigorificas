# -*- coding: utf-8 -*-
"""Renderiza una diapositiva (spec JSON del deck) a HTML 1920x1080, replicando
el diseno navy+naranja del PPTX. Incluye la misma expansion que el motor
(indice automatico + quiz -> pregunta/respuesta) para casar con los audios.
"""
import html as _h

NAVY="#1E2761"; NAVY2="#2E3A80"; CAD="#CADCFC"; GRIS="#64748B"
FRAME="#F3F6FB"; INK="#1B2330"; ORANGE="#E8801A"; ORANGEL="#F4A24C"; GREEN="#1E8E4B"
LINE="#D7DEEA"

def esc(s): return _h.escape(str(s))

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Segoe UI','Montserrat',Arial,sans-serif}}
html,body{{width:1920px;height:1080px;overflow:hidden}}
.slide{{position:relative;width:1920px;height:1080px;background:#fff;color:{INK}}}
.navy{{background:{NAVY};color:#fff}}
.pad{{position:absolute;left:130px;right:130px}}
.eyebrow{{position:absolute;left:135px;top:70px;color:{ORANGE};font-size:26px;font-weight:800;letter-spacing:2px}}
.eyebrow.cad{{color:{ORANGEL}}}
.acc{{position:absolute;left:137px;height:13px;background:{ORANGE};border-radius:3px}}
.title{{position:absolute;left:130px;font-weight:800;line-height:1.12}}
.foot{{position:absolute;left:72px;bottom:24px;color:{GRIS};font-size:16px}}
.count{{position:absolute;right:60px;top:48px;color:{GRIS};font-size:18px;font-weight:700}}
.und{{position:absolute;left:137px;height:12px;width:300px;background:{ORANGE};border-radius:3px}}
ul{{list-style:none}}
.bul{{display:flex;gap:14px;margin-bottom:20px;font-size:31px;line-height:1.3}}
.bul .m{{color:{ORANGE};font-weight:800}}
.imgframe{{position:absolute;top:300px;width:760px;height:660px;background:{FRAME};border:2px solid #C7D2E6;border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:{GRIS};text-align:center;padding:20px}}
.imgframe .t{{font-size:26px;font-weight:800;letter-spacing:2px}}
.imgframe .b{{font-size:22px;font-style:italic;margin-top:12px;max-width:600px}}
table{{position:absolute;left:80px;right:80px;top:270px;border-collapse:collapse;width:1760px}}
th{{background:{NAVY};color:#fff;text-align:left;padding:16px 18px;font-size:24px}}
td{{border:1px solid {LINE};padding:13px 18px;font-size:22px;vertical-align:top}}
tr:nth-child(even) td{{background:#F6F8FC}}
.notaband{{position:absolute;left:80px;right:80px;bottom:70px;background:{FRAME};border:1px solid {LINE};border-radius:10px;padding:16px 22px;font-size:22px}}
.notaband b{{color:{ORANGE}}}
.card{{position:absolute;top:300px;width:470px;height:420px;background:{FRAME};border:1px solid {LINE};border-radius:14px;text-align:center;overflow:hidden}}
.card .bar{{height:20px;background:{ORANGE}}}
.card .num{{font-size:120px;font-weight:800;color:{NAVY};margin-top:40px}}
.card .lab{{font-size:28px;color:{INK};padding:0 30px;margin-top:10px}}
.qband{{position:absolute;left:0;top:0;width:1920px;height:150px;display:flex;align-items:center;padding-left:130px;font-size:44px;font-weight:800;color:#fff}}
.opt{{position:absolute;width:770px;height:150px;background:{FRAME};border:1px solid #C7D2E6;border-radius:14px;display:flex;align-items:center;overflow:hidden}}
.opt .l{{width:100px;height:150px;background:{NAVY};color:#fff;font-size:52px;font-weight:800;display:flex;align-items:center;justify-content:center}}
.opt .x{{padding:0 24px;font-size:30px}}
.chk{{display:flex;gap:16px;margin-bottom:22px;font-size:34px;color:#fff}}
.chk .m{{color:{ORANGEL};font-weight:800}}
.tag{{position:absolute;left:130px;right:130px;bottom:70px;background:{ORANGE};border-radius:10px;padding:20px 26px;color:{NAVY};font-weight:800;font-style:italic;font-size:28px}}
"""

def _wrap(inner):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{inner}</body></html>"

def _count(n,total): return f"<div class='count'>{n:03d} / {total:03d}</div>"
def _foot(pie): return f"<div class='foot'>{esc(pie)}</div>"

def render(s, n, total, pie):
    t=s.get("tipo")
    if t=="portada":
        sub=f"<div style='position:absolute;left:130px;top:430px;color:{CAD};font-size:40px'>{esc(s.get('subtitulo',''))}</div>" if s.get("subtitulo") else ""
        return _wrap(f"""<div class='slide navy'>
        <div class='eyebrow cad'>{esc(s['videoxy']).upper()}</div>
        <div class='acc' style='top:300px;width:210px'></div>
        <div class='title' style='top:330px;font-size:88px;color:#fff;right:130px'>{esc(s['titulo'])}</div>
        {sub}
        <div style='position:absolute;left:130px;bottom:70px;color:{CAD};font-size:24px'>{esc(s['tema'])}</div>
        </div>""")
    if t=="cifras":
        cards=""
        for (num,lab),x in zip(s["tarjetas"],[130,725,1320]):
            cards+=f"<div class='card' style='left:{x}px'><div class='bar'></div><div class='num'>{esc(num)}</div><div class='lab'>{esc(lab)}</div></div>"
        return _wrap(f"""<div class='slide'>{_count(n,total)}{_foot(pie)}
        <div class='title' style='top:70px;font-size:52px;color:{ORANGE}'>{esc(s['titulo'])}</div>
        <div class='und' style='top:175px;background:{NAVY}'></div>{cards}</div>""")
    if t=="indice":
        items=""
        for i,it in enumerate(s["items"],1):
            items+=f"<div style='display:flex;gap:22px;margin-bottom:16px;font-size:33px'><span style='color:{ORANGE};font-weight:800'>{i:02d}</span><span>{esc(it)}</span></div>"
        return _wrap(f"""<div class='slide'>{_count(n,total)}{_foot(pie)}
        <div class='eyebrow'>PARTES DE ESTE VÍDEO</div>
        <div class='title' style='top:130px;font-size:52px;color:{NAVY}'>{esc(s['titulo'])}</div>
        <div class='und' style='top:240px'></div>
        <div class='pad' style='top:320px'>{items}</div></div>""")
    if t=="contenido":
        lado=s.get("_lado","der")
        bullets="".join(f"<div class='bul'><span class='m'>▸</span><span>{esc(v)}</span></div>" for v in s["vinetas"])
        brief=esc(s.get("img_brief","imagen"))
        frame=f"<div class='imgframe' style='{'left:130px' if lado=='izq' else 'right:130px'}'><div class='t'>IMAGEN</div><div class='b'>{brief}</div></div>"
        txt_l = "980px" if lado=='izq' else "130px"
        return _wrap(f"""<div class='slide'>{_count(n,total)}{_foot(pie)}
        <div class='eyebrow'>{esc(s.get('eyebrow','')).upper()}</div>
        <div class='title' style='top:130px;font-size:54px;color:{NAVY};right:130px'>{esc(s['titulo'])}</div>
        <div class='und' style='top:245px'></div>
        <div style='position:absolute;left:{txt_l};top:310px;width:760px'>{bullets}</div>
        {frame}</div>""")
    if t=="tabla":
        heads="".join(f"<th>{esc(h)}</th>" for h in s["headers"])
        rows=""
        for row in s["rows"]:
            rows+="<tr>"+"".join(f"<td>{esc(c)}</td>" for c in row)+"</tr>"
        nota=f"<div class='notaband'><b>Qué significa:</b> {esc(s['nota'])}</div>" if s.get("nota") else ""
        return _wrap(f"""<div class='slide'>{_count(n,total)}{_foot(pie)}
        <div class='eyebrow'>{esc(s.get('eyebrow','')).upper()}</div>
        <div class='title' style='top:120px;font-size:48px;color:{NAVY}'>{esc(s['titulo'])}</div>
        <div class='und' style='top:225px'></div>
        <table><thead><tr>{heads}</tr></thead><tbody>{rows}</tbody></table>{nota}</div>""")
    if t=="_quizP":
        q=s["_q"]; letras="ABCD"
        opts=""
        pos=[(130,470),(1020,470),(130,720),(1020,720)]
        for k,op in enumerate(q["opciones"][:4]):
            x,y=pos[k]
            opts+=f"<div class='opt' style='left:{x}px;top:{y}px'><div class='l'>{letras[k]}</div><div class='x'>{esc(op)}</div></div>"
        return _wrap(f"""<div class='slide'>{_count(n,total)}{_foot(pie)}
        <div class='qband' style='background:{ORANGE}'>PREGUNTA RÁPIDA</div>
        <div style='position:absolute;left:130px;top:210px;right:130px;font-size:42px;font-weight:800;color:{NAVY}'>{esc(q['pregunta'])}</div>
        {opts}</div>""")
    if t=="_quizR":
        q=s["_q"]; letras="ABCD"; ci=q.get("correcta",0)
        return _wrap(f"""<div class='slide'>{_count(n,total)}{_foot(pie)}
        <div class='qband' style='background:{GREEN}'>RESPUESTA: {letras[ci]}</div>
        <div style='position:absolute;left:130px;top:200px;right:130px;font-size:30px;color:{GRIS};font-weight:700'>{esc(q['pregunta'])}</div>
        <div style='position:absolute;left:130px;right:130px;top:300px;background:#E9F6EE;border:2px solid {GREEN};border-radius:12px;padding:22px 26px;font-size:34px;color:{NAVY};font-weight:800'>{letras[ci]}. {esc(q['opciones'][ci])}</div>
        <div style='position:absolute;left:130px;right:130px;top:470px;font-size:30px'><b style='color:{ORANGE}'>Por qué:</b> {esc(q.get('porque',''))}</div></div>""")
    if t=="cierre":
        chk="".join(f"<div class='chk'><span class='m'>✓</span><span>{esc(m)}</span></div>" for m in s["mapa"])
        tag=f"<div class='tag'>{esc(s['tagline'])}</div>" if s.get("tagline") else ""
        return _wrap(f"""<div class='slide navy'>{_count(n,total)}
        <div class='eyebrow cad'>{esc(s.get('eyebrow','LO QUE YA DOMINAS')).upper()}</div>
        <div class='acc' style='top:150px;width:210px'></div>
        <div class='title' style='top:180px;font-size:64px;color:#fff;right:130px'>{esc(s['titulo'])}</div>
        <div class='pad' style='top:360px'>{chk}</div>{tag}</div>""")
    return _wrap("<div class='slide'></div>")

# ---- expansion identica al motor ----
def auto_indice(slides):
    partes=[]
    for s in slides:
        if s.get("tipo")=="contenido":
            e=(s.get("eyebrow") or "").strip(); base=e.split("·")[0].strip() if "·" in e else e
            if base and base not in partes: partes.append(base)
    if len(partes)<2: return slides
    if len(partes)>9: partes=partes[:9]
    pos=1
    for i,s in enumerate(slides):
        if s.get("tipo")=="cifras": pos=i+1; break
        if s.get("tipo")=="portada": pos=i+1
    return slides[:pos]+[{"tipo":"indice","titulo":"En este vídeo","items":partes}]+slides[pos:]

def expand(slides):
    out=[]
    for s in slides:
        if s.get("tipo")=="quiz":
            out.append({"tipo":"_quizP","_q":s}); out.append({"tipo":"_quizR","_q":s})
        else: out.append(s)
    return out

def prepare(slides):
    slides=expand(auto_indice(slides))
    idxc=0
    for s in slides:
        if s.get("tipo")=="contenido":
            s["_lado"]='der' if idxc%2==0 else 'izq'; idxc+=1
    return slides
