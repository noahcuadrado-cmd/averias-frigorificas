#!/usr/bin/env python3
"""Construye un .pptx a partir de un JSON de diapositivas.
Uso: python3 _build/build_deck.py <deck.json> <salida.pptx>
El JSON: {"pie": "texto del pie", "slides": [ {slide}, {slide}, ... ]}
Cada {slide} sigue el formato de pptx_engine (tipo: portada|cifras|contenido|cierre).
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pptx_engine import construir

def main():
    deck=json.load(open(sys.argv[1], encoding="utf-8"))
    salida=sys.argv[2]
    construir(deck["slides"], deck.get("pie","Curso Gas B"), salida)
    print("PPTX:", salida, "|", len(deck["slides"]), "diapositivas")

if __name__=="__main__":
    main()
