#!/usr/bin/env python3
"""Convierte un .md (convencion del curso) en PDF con la plantilla navy.
Uso: python3 _build/build_pdf.py "ruta/al/archivo.md" ["Nombre del curso al pie"]
- Titulos: #, ##, ###
- Tablas markdown, listas, **negrita**
- Notas del instructor: blockquote (> texto). Si empieza por AVISO -> caja ambar.
- Seccion cuyo titulo contenga "Ideas clave" se resalta en caja.
"""
import sys, os, re
import markdown as md
from weasyprint import HTML

CSS_PATH = os.path.join(os.path.dirname(__file__), "estilo_curso.css")

def build(md_path, curso="Curso Gas B"):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    body = md.markdown(text, extensions=[
        "tables", "sane_lists", "attr_list", "def_list", "fenced_code", "md_in_html"])
    body = re.sub(r"<blockquote>\s*<p>(AVISO|CUIDADO|ATENCION|ATENCIÓN)",
                  r'<blockquote class="aviso"><p><strong>\1</strong>', body)
    m = re.search(r'(<h2[^>]*>[^<]*Ideas clave[^<]*</h2>)', body, re.I)
    if m:
        body = body[:m.start()] + '<div class="ideas">' + body[m.start():] + '</div>'
    with open(CSS_PATH, encoding="utf-8") as c:
        css = c.read()
    html = (f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
            f'<style>{css}</style></head><body>'
            f'<span style="string-set: curso \'{curso}\'"></span>'
            f'{body}</body></html>')
    out = os.path.splitext(md_path)[0] + ".pdf"
    HTML(string=html, base_url=os.path.dirname(os.path.abspath(md_path))).write_pdf(out)
    return out

if __name__ == "__main__":
    curso = sys.argv[2] if len(sys.argv) > 2 else "Curso Gas B"
    print("PDF:", build(sys.argv[1], curso))
