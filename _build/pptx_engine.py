#!/usr/bin/env python3
"""Motor de PowerPoint del Curso Gas B (FASE 2) - plantilla exacta v9.
16:9, Montserrat, portada navy 1E2761, contenido blanco con eyebrow + contador,
titulo 27 navy, texto a la izquierda (5,45"), imagen a la derecha en marco
redondeado F3F6FB (x=6,35 y=1,15 3,05x3,75), pie gris. Notas N1/N2 en cada slide.

Un slide se define como dict:
  {"tipo":"portada","tema":..,"titulo":..,"subtitulo":..,"videoxy":.. ,"notas":..}
  {"tipo":"cifras","titulo":..,"tarjetas":[("9","texto"),...],"notas":..}
  {"tipo":"contenido","eyebrow":..,"titulo":..,"vinetas":[..],"img":"ruta.png"|None,
      "img_brief":"texto para foto realista","notas":..}
  {"tipo":"cierre","titulo":..,"mapa":[..],"notas":..}
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

NAVY=RGBColor(0x1E,0x27,0x61); NAVY2=RGBColor(0x2E,0x3A,0x80)
CAD=RGBColor(0xCA,0xDC,0xFC); GRIS=RGBColor(0x64,0x74,0x8B)
FRAME=RGBColor(0xF3,0xF6,0xFB); INK=RGBColor(0x1B,0x23,0x30); WHITE=RGBColor(0xFF,0xFF,0xFF)
FONT="Montserrat"
W,H=Inches(13.333),Inches(7.5)

def _font(run,size,color,bold=False,italic=False):
    run.font.name=FONT; run.font.size=Pt(size); run.font.bold=bold
    run.font.italic=italic; run.font.color.rgb=color

def _box(slide,x,y,w,h):
    tb=slide.shapes.add_textbox(x,y,w,h); tb.text_frame.word_wrap=True
    return tb

def _rect(slide,x,y,w,h,fill,line=None,round_=True):
    sh=slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if round_ else MSO_SHAPE.RECTANGLE,x,y,w,h)
    sh.fill.solid(); sh.fill.fore_color.rgb=fill
    if line: sh.line.color.rgb=line; sh.line.width=Pt(1)
    else: sh.line.fill.background()
    sh.shadow.inherit=False
    return sh

def _notas(slide,texto):
    tf=slide.notes_slide.notes_text_frame; tf.text=texto

def _pie(slide,texto):
    tb=_box(slide,Inches(0.5),Inches(7.02),Inches(9),Inches(0.4))
    p=tb.text_frame.paragraphs[0]; r=p.add_run(); r.text=texto; _font(r,9,GRIS)

def _contador(slide,n,total):
    tb=_box(slide,Inches(11.6),Inches(0.35),Inches(1.5),Inches(0.4))
    p=tb.text_frame.paragraphs[0]; p.alignment=PP_ALIGN.RIGHT
    r=p.add_run(); r.text=f"{n:03d} / {total:03d}"; _font(r,10,GRIS,bold=True)

def _blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])

def _fondo(slide,color):
    r=_rect(slide,0,0,W,H,color,round_=False);
    slide.shapes._spTree.remove(r._element); slide.shapes._spTree.insert(2,r._element)
    return r

def portada(prs,s):
    sl=_blank(prs); _fondo(sl,NAVY)
    tb=_box(sl,Inches(0.9),Inches(0.8),Inches(11.5),Inches(0.6))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s["videoxy"].upper(); _font(r,14,CAD,bold=True)
    tb.text_frame.paragraphs[0].runs[0].font.name=FONT
    tb2=_box(sl,Inches(0.9),Inches(2.4),Inches(11.5),Inches(2.2))
    p=tb2.text_frame.paragraphs[0]; r=p.add_run(); r.text=s["titulo"]; _font(r,40,WHITE,bold=True)
    if s.get("subtitulo"):
        p2=tb2.text_frame.add_paragraph(); r=p2.add_run(); r.text=s["subtitulo"]; _font(r,22,CAD)
    tb3=_box(sl,Inches(0.9),Inches(6.4),Inches(11.5),Inches(0.6))
    r=tb3.text_frame.paragraphs[0].add_run(); r.text=s["tema"]; _font(r,13,CAD)
    _notas(sl,s.get("notas","")); return sl

def cifras(prs,s,n,total,pie):
    sl=_blank(prs); _fondo(sl,WHITE); _contador(sl,n,total); _pie(sl,pie)
    tb=_box(sl,Inches(0.9),Inches(0.55),Inches(10),Inches(1.0))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s["titulo"]; _font(r,27,NAVY,bold=True)
    xs=[Inches(0.9),Inches(5.05),Inches(9.2)]
    for (num,txt),x in zip(s["tarjetas"],xs):
        card=_rect(sl,x,Inches(2.2),Inches(3.3),Inches(3.0),FRAME,line=RGBColor(0xD7,0xDE,0xEA))
        t=_box(sl,x,Inches(2.55),Inches(3.3),Inches(1.6)); t.text_frame.paragraphs[0].alignment=PP_ALIGN.CENTER
        r=t.text_frame.paragraphs[0].add_run(); r.text=num; _font(r,60,NAVY,bold=True)
        t2=_box(sl,x+Inches(0.25),Inches(3.95),Inches(2.8),Inches(1.1))
        p=t2.text_frame.paragraphs[0]; p.alignment=PP_ALIGN.CENTER
        r=p.add_run(); r.text=txt; _font(r,14,INK)
    _notas(sl,s.get("notas","")); return sl

def contenido(prs,s,n,total,pie):
    sl=_blank(prs); _fondo(sl,WHITE); _contador(sl,n,total); _pie(sl,pie)
    if s.get("eyebrow"):
        tb=_box(sl,Inches(0.9),Inches(0.5),Inches(9),Inches(0.4))
        r=tb.text_frame.paragraphs[0].add_run(); r.text=s["eyebrow"].upper(); _font(r,12,GRIS,bold=True)
    tb=_box(sl,Inches(0.9),Inches(0.95),Inches(11.5),Inches(1.0))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s["titulo"]; _font(r,27,NAVY,bold=True)
    # texto izquierda 5.45"
    tb=_box(sl,Inches(0.9),Inches(2.1),Inches(5.45),Inches(4.6))
    tf=tb.text_frame; tf.word_wrap=True; first=True
    for v in s["vinetas"]:
        p=tf.paragraphs[0] if first else tf.add_paragraph(); first=False
        p.space_after=Pt(10)
        rb=p.add_run(); rb.text="•  "; _font(rb,16,NAVY2,bold=True)
        r=p.add_run(); r.text=v; _font(r,16,INK)
    # marco imagen derecha
    fx,fy,fw,fh=Inches(6.35),Inches(1.15),Inches(3.05*1.9),Inches(3.75*1.35)
    if s.get("img"):
        fr=_rect(sl,fx-Inches(0.06),fy-Inches(0.06),fw+Inches(0.12),fh+Inches(0.12),FRAME,line=RGBColor(0xD7,0xDE,0xEA))
        try: sl.shapes.add_picture(s["img"],fx,fy,width=fw)
        except Exception: pass
    else:
        fr=_rect(sl,fx,fy,fw,fh,FRAME,line=RGBColor(0xC7,0xD2,0xE6))
        # etiqueta legible por el script de descarga: descr = "IMGQ:<termino de busqueda>"
        brief=s.get("img_brief","instalacion de gas")
        try:
            cnv=fr._element.xpath('.//p:cNvPr')[0]
            cnv.set('descr','IMGQ:'+brief); cnv.set('name','imgph')
        except Exception: pass
        t=_box(sl,fx+Inches(0.3),fy+fh/2-Inches(0.7),fw-Inches(0.6),Inches(1.4))
        p=t.text_frame.paragraphs[0]; p.alignment=PP_ALIGN.CENTER
        r=p.add_run(); r.text="IMAGEN REALISTA"; _font(r,14,GRIS,bold=True)
        p2=t.text_frame.add_paragraph(); p2.alignment=PP_ALIGN.CENTER
        r=p2.add_run(); r.text=brief; _font(r,11,GRIS,italic=True)
    _notas(sl,s.get("notas","")); return sl

def cierre(prs,s,n,total,pie):
    sl=_blank(prs); _fondo(sl,WHITE); _contador(sl,n,total); _pie(sl,pie)
    tb=_box(sl,Inches(0.9),Inches(0.7),Inches(11),Inches(1.0))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s["titulo"]; _font(r,30,NAVY,bold=True)
    tb=_box(sl,Inches(0.9),Inches(2.2),Inches(11),Inches(4.0)); tf=tb.text_frame; first=True
    for m in s["mapa"]:
        p=tf.paragraphs[0] if first else tf.add_paragraph(); first=False; p.space_after=Pt(14)
        rb=p.add_run(); rb.text="✓  "; _font(rb,20,NAVY2,bold=True)
        r=p.add_run(); r.text=m; _font(r,20,INK)
    _notas(sl,s.get("notas","")); return sl

def construir(slides, pie, salida):
    prs=Presentation(); prs.slide_width=W; prs.slide_height=H
    total=len(slides)
    for i,s in enumerate(slides,1):
        t=s["tipo"]
        if t=="portada": portada(prs,s)
        elif t=="cifras": cifras(prs,s,i,total,pie)
        elif t=="contenido": contenido(prs,s,i,total,pie)
        elif t=="cierre": cierre(prs,s,i,total,pie)
    prs.save(salida); return salida
