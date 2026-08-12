#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Motor PowerPoint del Curso Gas B (FASE 2) v2 - didactico y dinamico.
Plantilla navy 1E2761 + acentos naranja E8801A. 16:9, Montserrat.
Tipos de slide: portada, cifras, indice (auto), contenido (imagen der/izq alterna),
tabla (tabla grande, sin imagen), quiz (pregunta -> respuesta), cierre (gran final).
Transicion de CUBO en todas. Marco de imagen etiquetado IMGQ: para el script/Cowork.
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml import parse_xml
from pptx.oxml.ns import qn

NAVY=RGBColor(0x1E,0x27,0x61); NAVY2=RGBColor(0x2E,0x3A,0x80)
CAD=RGBColor(0xCA,0xDC,0xFC); GRIS=RGBColor(0x64,0x74,0x8B)
FRAME=RGBColor(0xF3,0xF6,0xFB); INK=RGBColor(0x1B,0x23,0x30); WHITE=RGBColor(0xFF,0xFF,0xFF)
ORANGE=RGBColor(0xE8,0x80,0x1A); ORANGEL=RGBColor(0xF4,0xA2,0x4C)
GREEN=RGBColor(0x1E,0x8E,0x4B)
FONT="Montserrat"
W,H=Inches(13.333),Inches(7.5)

def _font(run,size,color,bold=False,italic=False):
    run.font.name=FONT; run.font.size=Pt(size); run.font.bold=bold
    run.font.italic=italic; run.font.color.rgb=color

def _box(slide,x,y,w,h):
    tb=slide.shapes.add_textbox(x,y,w,h); tb.text_frame.word_wrap=True; return tb

def _rect(slide,x,y,w,h,fill,line=None,shape=MSO_SHAPE.ROUNDED_RECTANGLE):
    sh=slide.shapes.add_shape(shape,x,y,w,h)
    sh.fill.solid(); sh.fill.fore_color.rgb=fill
    if line: sh.line.color.rgb=line; sh.line.width=Pt(1)
    else: sh.line.fill.background()
    sh.shadow.inherit=False; return sh

def _notas(slide,texto):
    slide.notes_slide.notes_text_frame.text=texto or ""

def _pie(slide,texto):
    tb=_box(slide,Inches(0.5),Inches(7.02),Inches(9),Inches(0.4))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=texto; _font(r,9,GRIS)

def _contador(slide,n,total):
    tb=_box(slide,Inches(11.6),Inches(0.35),Inches(1.5),Inches(0.4))
    p=tb.text_frame.paragraphs[0]; p.alignment=PP_ALIGN.RIGHT
    r=p.add_run(); r.text=f"{n:03d} / {total:03d}"; _font(r,10,GRIS,bold=True)

def _blank(prs): return prs.slides.add_slide(prs.slide_layouts[6])

def _fondo(slide,color):
    r=_rect(slide,0,0,W,H,color,shape=MSO_SHAPE.RECTANGLE)
    slide.shapes._spTree.remove(r._element); slide.shapes._spTree.insert(2,r._element); return r

def _cubo(slide,direccion='l'):
    """Transicion de cubo (PowerPoint 2010) en la diapositiva."""
    xml=('<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">'
         '<mc:Choice xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" '
         'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" Requires="p14">'
         f'<p:transition spd="med" p14:dur="700"><p14:cube dir="{direccion}"/></p:transition>'
         '</mc:Choice><mc:Fallback>'
         '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med">'
         f'<p:push dir="{direccion}"/></p:transition></mc:Fallback></mc:AlternateContent>')
    node=parse_xml(xml); sld=slide._element
    ref=sld.find(qn('p:clrMapOvr'))
    if ref is None: ref=sld.find(qn('p:cSld'))
    ref.addnext(node)

def _acento(slide,x,y,w=Inches(1.6),h=Inches(0.09),color=ORANGE):
    _rect(slide,x,y,w,h,color,shape=MSO_SHAPE.RECTANGLE)

# ---------- tipos de slide ----------
def portada(prs,s):
    sl=_blank(prs); _fondo(sl,NAVY)
    tb=_box(sl,Inches(0.9),Inches(0.8),Inches(11.5),Inches(0.6))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s["videoxy"].upper(); _font(r,14,ORANGEL,bold=True)
    _acento(sl,Inches(0.95),Inches(2.25))
    tb2=_box(sl,Inches(0.9),Inches(2.5),Inches(11.5),Inches(2.2))
    r=tb2.text_frame.paragraphs[0].add_run(); r.text=s["titulo"]; _font(r,40,WHITE,bold=True)
    if s.get("subtitulo"):
        p2=tb2.text_frame.add_paragraph(); r=p2.add_run(); r.text=s["subtitulo"]; _font(r,22,CAD)
    tb3=_box(sl,Inches(0.9),Inches(6.4),Inches(11.5),Inches(0.6))
    r=tb3.text_frame.paragraphs[0].add_run(); r.text=s["tema"]; _font(r,13,CAD)
    _notas(sl,s.get("notas","")); return sl

def cifras(prs,s,n,total,pie):
    sl=_blank(prs); _fondo(sl,WHITE); _contador(sl,n,total); _pie(sl,pie)
    tb=_box(sl,Inches(0.9),Inches(0.55),Inches(10),Inches(1.0))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s["titulo"]; _font(r,27,ORANGE,bold=True)
    _acento(sl,Inches(0.95),Inches(1.35),Inches(1.6),Inches(0.08),NAVY)
    for (num,txt),x in zip(s["tarjetas"],[Inches(0.9),Inches(5.05),Inches(9.2)]):
        _rect(sl,x,Inches(2.2),Inches(3.3),Inches(3.0),FRAME,line=RGBColor(0xD7,0xDE,0xEA))
        _rect(sl,x,Inches(2.2),Inches(3.3),Inches(0.14),ORANGE,shape=MSO_SHAPE.RECTANGLE)
        t=_box(sl,x,Inches(2.6),Inches(3.3),Inches(1.5)); t.text_frame.paragraphs[0].alignment=PP_ALIGN.CENTER
        r=t.text_frame.paragraphs[0].add_run(); r.text=str(num); _font(r,58,NAVY,bold=True)
        t2=_box(sl,x+Inches(0.25),Inches(4.0),Inches(2.8),Inches(1.1)); p=t2.text_frame.paragraphs[0]; p.alignment=PP_ALIGN.CENTER
        r=p.add_run(); r.text=txt; _font(r,14,INK)
    _notas(sl,s.get("notas","")); return sl

def indice(prs,s,n,total,pie):
    sl=_blank(prs); _fondo(sl,WHITE); _contador(sl,n,total); _pie(sl,pie)
    tb=_box(sl,Inches(0.9),Inches(0.55),Inches(9),Inches(0.4))
    r=tb.text_frame.paragraphs[0].add_run(); r.text="PARTES DE ESTE VÍDEO"; _font(r,13,ORANGE,bold=True)
    tb=_box(sl,Inches(0.9),Inches(1.0),Inches(11.5),Inches(1.0))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s["titulo"]; _font(r,27,NAVY,bold=True)
    _acento(sl,Inches(0.95),Inches(1.83),Inches(2.2),Inches(0.08))
    tb=_box(sl,Inches(0.9),Inches(2.3),Inches(11.5),Inches(4.4)); tf=tb.text_frame; first=True
    for i,it in enumerate(s["items"],1):
        p=tf.paragraphs[0] if first else tf.add_paragraph(); first=False; p.space_after=Pt(9)
        rb=p.add_run(); rb.text=f"{i:02d}   "; _font(rb,18,ORANGE,bold=True)
        r=p.add_run(); r.text=it; _font(r,17,INK)
    _notas(sl,s.get("notas","")); return sl

def contenido(prs,s,n,total,pie,lado='der'):
    sl=_blank(prs); _fondo(sl,WHITE); _contador(sl,n,total); _pie(sl,pie)
    if s.get("eyebrow"):
        tb=_box(sl,Inches(0.9),Inches(0.5),Inches(11),Inches(0.4))
        r=tb.text_frame.paragraphs[0].add_run(); r.text=s["eyebrow"].upper(); _font(r,13,ORANGE,bold=True)
    tb=_box(sl,Inches(0.9),Inches(0.95),Inches(11.5),Inches(1.0))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s["titulo"]; _font(r,28,NAVY,bold=True)
    _acento(sl,Inches(0.95),Inches(1.78),Inches(2.2),Inches(0.08))
    fw,fh=Inches(5.8),Inches(5.0)
    if lado=='izq':
        img_x=Inches(0.9); txt_x=Inches(6.95); txt_w=Inches(5.5)
    else:
        img_x=Inches(6.65); txt_x=Inches(0.9); txt_w=Inches(5.5)
    img_y=Inches(2.15)
    # texto
    tb=_box(sl,txt_x,Inches(2.15),txt_w,Inches(4.6)); tf=tb.text_frame; tf.word_wrap=True; first=True
    for v in s["vinetas"]:
        p=tf.paragraphs[0] if first else tf.add_paragraph(); first=False; p.space_after=Pt(11)
        rb=p.add_run(); rb.text="▸  "; _font(rb,16,ORANGE,bold=True)
        r=p.add_run(); r.text=v; _font(r,16,INK)
    # marco imagen (etiquetado para Cowork/script)
    brief=s.get("img_brief","instalacion de gas")
    fr=_rect(sl,img_x,img_y,fw,fh,FRAME,line=RGBColor(0xC7,0xD2,0xE6))
    try:
        cnv=fr._element.xpath('.//p:cNvPr')[0]; cnv.set('descr','IMGQ:'+brief); cnv.set('name','imgph')
    except Exception: pass
    t=_box(sl,img_x+Inches(0.3),img_y+fh/2-Inches(0.7),fw-Inches(0.6),Inches(1.4))
    p=t.text_frame.paragraphs[0]; p.alignment=PP_ALIGN.CENTER
    r=p.add_run(); r.text="IMAGEN"; _font(r,14,GRIS,bold=True)
    p2=t.text_frame.add_paragraph(); p2.alignment=PP_ALIGN.CENTER
    r=p2.add_run(); r.text=brief; _font(r,11,GRIS,italic=True)
    _notas(sl,s.get("notas","")); return sl

def tabla(prs,s,n,total,pie):
    sl=_blank(prs); _fondo(sl,WHITE); _contador(sl,n,total); _pie(sl,pie)
    if s.get("eyebrow"):
        tb=_box(sl,Inches(0.9),Inches(0.45),Inches(11),Inches(0.4))
        r=tb.text_frame.paragraphs[0].add_run(); r.text=s["eyebrow"].upper(); _font(r,13,ORANGE,bold=True)
    tb=_box(sl,Inches(0.9),Inches(0.85),Inches(11.5),Inches(0.9))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s["titulo"]; _font(r,26,NAVY,bold=True)
    _acento(sl,Inches(0.95),Inches(1.62),Inches(2.2),Inches(0.08))
    headers=s["headers"]; rows=s["rows"]; nc=len(headers); nr=len(rows)+1
    gtab=sl.shapes.add_table(nr,nc,Inches(0.6),Inches(1.95),Inches(12.13),Inches(4.4)).table
    # ancho de columnas: primera un poco mas
    fs=12 if nc<=4 else (11 if nc<=6 else 9)
    for j,h in enumerate(headers):
        c=gtab.cell(0,j); c.fill.solid(); c.fill.fore_color.rgb=NAVY
        c.text=str(h); p=c.text_frame.paragraphs[0]
        for run in p.runs: _font(run,fs,WHITE,bold=True)
        if not p.runs:
            run=p.add_run(); run.text=str(h); _font(run,fs,WHITE,bold=True)
    for i,row in enumerate(rows,1):
        for j in range(nc):
            c=gtab.cell(i,j); val=row[j] if j<len(row) else ""
            c.fill.solid(); c.fill.fore_color.rgb=(RGBColor(0xF6,0xF8,0xFC) if i%2 else WHITE)
            c.text=str(val); p=c.text_frame.paragraphs[0]
            for run in p.runs: _font(run,fs,INK)
            if not p.runs:
                run=p.add_run(); run.text=str(val); _font(run,fs,INK)
    if s.get("nota"):
        band=_rect(sl,Inches(0.6),Inches(6.5),Inches(12.13),Inches(0.42),FRAME,line=RGBColor(0xD7,0xDE,0xEA))
        t=_box(sl,Inches(0.8),Inches(6.52),Inches(11.8),Inches(0.4))
        rb=t.text_frame.paragraphs[0].add_run(); rb.text="Qué significa:  "; _font(rb,11,ORANGE,bold=True)
        r=t.text_frame.paragraphs[0].add_run(); r.text=s["nota"]; _font(r,11,INK)
    _notas(sl,s.get("notas","")); return sl

def quiz_pregunta(prs,s,n,total,pie):
    sl=_blank(prs); _fondo(sl,WHITE); _contador(sl,n,total); _pie(sl,pie)
    _rect(sl,0,0,W,Inches(1.25),ORANGE,shape=MSO_SHAPE.RECTANGLE)
    tb=_box(sl,Inches(0.9),Inches(0.3),Inches(11.5),Inches(0.7))
    r=tb.text_frame.paragraphs[0].add_run(); r.text="⚡  PREGUNTA RÁPIDA"; _font(r,24,WHITE,bold=True)
    tb=_box(sl,Inches(0.9),Inches(1.65),Inches(11.5),Inches(1.5))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s["pregunta"]; _font(r,24,NAVY,bold=True)
    letras="ABCD"; xs=[Inches(0.9),Inches(6.95)]; ys=[Inches(3.6),Inches(5.05)]
    for k,op in enumerate(s["opciones"][:4]):
        x=xs[k%2]; y=ys[k//2]
        _rect(sl,x,y,Inches(5.45),Inches(1.25),FRAME,line=RGBColor(0xC7,0xD2,0xE6))
        _rect(sl,x,y,Inches(0.7),Inches(1.25),NAVY,shape=MSO_SHAPE.RECTANGLE)
        tl=_box(sl,x,y+Inches(0.35),Inches(0.7),Inches(0.6)); tl.text_frame.paragraphs[0].alignment=PP_ALIGN.CENTER
        r=tl.text_frame.paragraphs[0].add_run(); r.text=letras[k]; _font(r,22,WHITE,bold=True)
        to=_box(sl,x+Inches(0.85),y+Inches(0.2),Inches(4.5),Inches(0.95))
        r=to.text_frame.paragraphs[0].add_run(); r.text=op; _font(r,14,INK)
    _notas(sl,s.get("notas_p","")); return sl

def quiz_respuesta(prs,s,n,total,pie):
    sl=_blank(prs); _fondo(sl,WHITE); _contador(sl,n,total); _pie(sl,pie)
    _rect(sl,0,0,W,Inches(1.25),GREEN,shape=MSO_SHAPE.RECTANGLE)
    letras="ABCD"; ci=s.get("correcta",0)
    tb=_box(sl,Inches(0.9),Inches(0.3),Inches(11.5),Inches(0.7))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=f"✔  RESPUESTA:  {letras[ci]}"; _font(r,24,WHITE,bold=True)
    tb=_box(sl,Inches(0.9),Inches(1.55),Inches(11.5),Inches(1.0))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s["pregunta"]; _font(r,18,GRIS,bold=True)
    # opcion correcta destacada
    _rect(sl,Inches(0.9),Inches(2.75),Inches(11.5),Inches(1.0),RGBColor(0xE9,0xF6,0xEE),line=GREEN)
    to=_box(sl,Inches(1.2),Inches(2.95),Inches(11),Inches(0.7))
    rb=to.text_frame.paragraphs[0].add_run(); rb.text=f"{letras[ci]}.  "; _font(rb,18,GREEN,bold=True)
    r=to.text_frame.paragraphs[0].add_run(); r.text=s["opciones"][ci]; _font(r,18,NAVY,bold=True)
    # por que
    tb=_box(sl,Inches(0.9),Inches(4.1),Inches(11.5),Inches(2.4))
    rb=tb.text_frame.paragraphs[0].add_run(); rb.text="Por qué:  "; _font(rb,15,ORANGE,bold=True)
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s.get("porque",""); _font(r,15,INK)
    _notas(sl,s.get("notas_r","")); return sl

# ---------- ensamblado ----------
def _auto_indice(slides):
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

def _expandir(slides):
    """quiz -> pregunta + respuesta."""
    out=[]
    for s in slides:
        if s.get("tipo")=="quiz":
            out.append({"tipo":"_quizP","_q":s}); out.append({"tipo":"_quizR","_q":s})
        else: out.append(s)
    return out

def construir(slides, pie, salida):
    slides=_expandir(_auto_indice(slides))
    prs=Presentation(); prs.slide_width=W; prs.slide_height=H
    total=len(slides); idxc=0; dirs=['l','r']
    for i,s in enumerate(slides,1):
        t=s["tipo"]
        if t=="portada": sl=portada(prs,s)
        elif t=="cifras": sl=cifras(prs,s,i,total,pie)
        elif t=="indice": sl=indice(prs,s,i,total,pie)
        elif t=="tabla": sl=tabla(prs,s,i,total,pie)
        elif t=="_quizP": sl=quiz_pregunta(prs,s["_q"],i,total,pie)
        elif t=="_quizR": sl=quiz_respuesta(prs,s["_q"],i,total,pie)
        elif t=="cierre": sl=cierre(prs,s,i,total,pie)
        elif t=="contenido":
            lado='der' if idxc%2==0 else 'izq'; idxc+=1
            sl=contenido(prs,s,i,total,pie,lado)
        else: continue
        _cubo(sl, dirs[(i-1)%2])
    prs.save(salida); return salida

def cierre(prs,s,n,total,pie):
    sl=_blank(prs); _fondo(sl,NAVY)
    tb=_box(sl,Inches(0.9),Inches(0.7),Inches(11.5),Inches(0.5))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s.get("eyebrow","LO QUE YA DOMINAS").upper(); _font(r,14,ORANGEL,bold=True)
    _acento(sl,Inches(0.95),Inches(1.15))
    tb=_box(sl,Inches(0.9),Inches(1.35),Inches(11.5),Inches(1.2))
    r=tb.text_frame.paragraphs[0].add_run(); r.text=s["titulo"]; _font(r,34,WHITE,bold=True)
    tb=_box(sl,Inches(0.9),Inches(2.85),Inches(11.5),Inches(3.0)); tf=tb.text_frame; first=True
    for m in s["mapa"]:
        p=tf.paragraphs[0] if first else tf.add_paragraph(); first=False; p.space_after=Pt(12)
        rb=p.add_run(); rb.text="✓  "; _font(rb,20,ORANGEL,bold=True)
        r=p.add_run(); r.text=m; _font(r,19,WHITE)
    if s.get("tagline"):
        _rect(sl,Inches(0.9),Inches(6.05),Inches(11.5),Inches(0.9),ORANGE)
        t=_box(sl,Inches(1.15),Inches(6.15),Inches(11.0),Inches(0.7))
        r=t.text_frame.paragraphs[0].add_run(); r.text=s["tagline"]; _font(r,15,NAVY,bold=True,italic=True)
    _notas(sl,s.get("notas","")); return sl
