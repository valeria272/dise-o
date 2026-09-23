#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · carrusel ETERSOL — pasto sintético (octubre 2026, 08/10).

La PORTADA es la que Paulina aprobó el 15-09-2026, sin tocar. Las láminas 2 a 5
se arman ahora con el mismo brief de la grilla.

Uso:  python carrusel_etersol.py && bash render.sh etersol
"""
from _motor import construir

# ---------------------------------------------------------------- el brief ---
# CARRUSEL — Pasto sintético para un patio que aguante la primavera
# Producto: Pasto sintético Etersol (distinto de la línea GEOS de cerámicas de julio)
# Pilar: Proveedores · 08/10/2026
CARRUSEL = {
    "slug": "etersol",
    "proveedor_logo": "img/proveedores/logo_etersol.png",
    "producto": "Pasto sintético Etersol",
    "ancho_caja_des": 700,
    "laminas": [
        # L1 · PORTADA — aprobada por Paulina el 15-09-2026, tal cual.
        # brief: «Llega la primavera, ¿tu patio aguanta la temporada?»
        #        Subtexto: Descubre el pasto sintético Etersol.
        #        Visual: patio con pasto natural descuidado o tierra pelada.
        {"foto": "fotos/etersol/01.jpg", "y": 620, "portada": True,
         "pre": "LLEGA LA PRIMAVERA,",
         "sobre": "¿TU PATIO AGUANTA",
         "caja": "LA TEMPORADA?",
         "capsula": "Descubre el pasto sintético Etersol",
         "pie": ""},

        # L2 · brief: «Sin barro ni pasto amarillo» / «a diferencia del pasto natural,
        #      no necesita riego, corte ni fertilizante se mantiene verde todo el año.»
        #      Visual: detalle de textura del pasto sintético → ESPECIFICACIÓN → zoom
        {"foto": "fotos/etersol/02.jpg", "y": 242,
         "sobre": "SIN BARRO",
         "caja": "NI PASTO AMARILLO",
         "bajada": "No necesita riego, corte ni fertilizante: **se mantiene verde todo el año**."},

        # L3 · brief: «Instalación simple» / «se instala sobre tierra compactada o
        #      radier, sin obra mayor.»  Visual: instalación → USO → escena
        #
        # El titular son dos palabras: partirlo entre línea blanca y caja roja deja
        # una caja de 6 letras que se compone gigante y se sale de la banda de alto
        # (70-80). Va entero en el rojo — sigue siendo una sola caja por lámina.
        {"foto": "fotos/etersol/03.jpg", "y": 236,
         "sobre": "",
         "caja": "INSTALACIÓN SIMPLE",
         "bajada": "Se instala sobre **tierra compactada o radier**, sin obra mayor."},

        # L4 · el brief lo rotula «(Tip pro)» pero el texto NO es una orden de oficio,
        #      es un beneficio. §4-bis: cedral tampoco tiene tip pro y su L4 lleva
        #      otro beneficio EN EL REGISTRO NORMAL. Va así, sin invertir la jerarquía.
        #      «Ideal para patios, terrazas y áreas de juego» /
        #      «resiste el tránsito diario y no se decolora con el sol.»
        {"foto": "fotos/etersol/04.jpg", "y": 228,
         "sobre": "IDEAL PARA PATIOS,",
         "caja": "TERRAZAS Y ÁREAS DE JUEGO",
         "bajada": "Resiste el **tránsito diario** y no se decolora con el sol."},

        # L5 · CIERRE — brief: «Pasto sintético Etersol, disponible en Ebema.»
        #      Visual: rollo de pasto sintético + logo Ebema.
        {"foto": "fotos/etersol/05.jpg", "cierre": True},
    ],
}

if __name__ == "__main__":
    construir(CARRUSEL)
