#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · carrusel VOLCANITA RH — Volcán (octubre 2026, 13/10).

Uso:  python carrusel_volcanita.py && bash render.sh volcanita
"""
from _motor import construir

# ---------------------------------------------------------------- el brief ---
# CARRUSEL — Volcanita RH para baños y lavanderías
# Producto: Volcanita RH (resistente a la humedad) — único producto Volcán que
# vende Ebema (no Volcopanel ni Siding). Distinta de la Volcanita estándar de agosto.
# Pilar: Proveedores · 13/10/2026
CARRUSEL = {
    "slug": "volcanita",
    "proveedor_logo": "img/proveedores/logo_volcan.png",
    "producto": "Volcanita RH",
    "ancho_caja_des": 745,
    "laminas": [
        # L1 · PORTADA
        # brief: «Remodelar el baño o la lavandería empieza por la placa.»
        #        Visual: baño o lavandería en remodelación.
        #
        # El brief no trae subtexto de portada: la cápsula lleva el descriptor del
        # producto, que es el titular de la L3 del mismo brief.
        {"foto": "fotos/volcanita/01.jpg", "y": 648, "portada": True,
         "sobre": "REMODELAR EL BAÑO O LA LAVANDERÍA",
         "caja": "EMPIEZA POR LA PLACA",
         "capsula": "Volcanita RH, resistente a la humedad",
         "pie": ""},

        # L2 · brief: «No cualquier placa aguanta la humedad constante» / «la
        #      Volcanita estándar no está pensada para esa exposición.»
        #      Visual: detalle de placa dañada por humedad → ESPECIFICACIÓN → zoom
        {"foto": "fotos/volcanita/02.jpg", "y": 244,
         "sobre": "NO CUALQUIER PLACA AGUANTA", "cuerpo": 52,
         "caja": "LA HUMEDAD CONSTANTE",
         "bajada": "La Volcanita estándar **no está pensada** para esa exposición."},

        # L3 · brief: «Volcanita RH, resistente a la humedad» / «núcleo y cara
        #      tratados para instalarse en baños, lavanderías y cocinas.»
        #      Visual: instalación de placa Volcanita RH → USO → escena
        {"foto": "fotos/volcanita/03.jpg", "y": 230,
         "sobre": "VOLCANITA RH,",
         "caja": "RESISTENTE A LA HUMEDAD",
         "bajada": "Núcleo y cara tratados para instalarse en **baños, lavanderías y cocinas**."},

        # L4 · rotulado «(Tip pro)» en el brief pero es un beneficio, no una orden:
        #      registro normal. «Se instala igual que la Volcanita estándar» /
        #      «mismo sistema de tabiquería — atornillado y terminación con cinta y pasta.»
        {"foto": "fotos/volcanita/04.jpg", "y": 222,
         "sobre": "SE INSTALA IGUAL QUE",
         "caja": "LA VOLCANITA ESTÁNDAR",
         "bajada": "Mismo sistema de tabiquería: **atornillado y terminación** con cinta y pasta."},

        # L5 · CIERRE — brief: «Volcanita RH, disponible en Ebema.»
        {"foto": "fotos/volcanita/05.jpg", "cierre": True},
    ],
}

if __name__ == "__main__":
    construir(CARRUSEL)
