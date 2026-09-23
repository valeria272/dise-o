#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · carrusel POINTFIX — alambre de púas (octubre 2026, 22/10).

Uso:  python carrusel_pointfix.py && bash render.sh pointfix
"""
from _motor import construir

# ---------------------------------------------------------------- el brief ---
# CARRUSEL — Cercar el campo antes de que entre el ganado
# Producto: Alambre de púas Pointfix — se corrige el rubro: Pointfix (vía Ebema) es
# cercos y fijaciones agrícolas/ganaderas (alambre de púas, malla ganadera, malla
# hexagonal, concertina, clavos, grapas), no sistemas niveladores de cerámica.
# Pilar: Proveedores · 22/10/2026
CARRUSEL = {
    "slug": "pointfix",
    "proveedor_logo": "img/proveedores/logo_pointfix.png",
    "producto": "Alambre de púas Pointfix",
    "ancho_caja_des": 720,
    "laminas": [
        # L1 · PORTADA
        # brief: «Delimitar un campo o parcela no puede esperar.»
        #        Visual: perímetro de campo o parcela sin cercar.
        {"foto": "fotos/pointfix/01.jpg", "y": 640, "portada": True,
         "sobre": "DELIMITAR UN CAMPO O PARCELA",
         "caja": "NO PUEDE ESPERAR",
         "capsula": "Alambre de púas Pointfix, de 4 puntas",
         "pie": ""},

        # L2 · brief: «Antes de que entre el ganado o se pierda el límite» /
        #      «un cerco a tiempo evita problemas mayores.»
        #      Visual: instalación de postes para el cerco → USO → escena
        {"foto": "fotos/pointfix/02.jpg", "y": 246,
         "sobre": "ANTES DE QUE ENTRE EL GANADO", "cuerpo": 50,
         "caja": "O SE PIERDA EL LÍMITE",
         "bajada": "Un cerco a tiempo **evita problemas mayores**."},

        # L3 · brief: «Alambre de púas Pointfix, 4 puntas» / «resistente, pensado
        #      para cercos agrícolas y ganaderos.»
        #      Visual: detalle del alambre de púas tensado → ESPECIFICACIÓN → zoom
        #
        # «4 PUNTAS» solo son 8 letras y la caja se compondría gigante: el corte va
        # antes, dejando el nombre del producto y la cifra juntos dentro del rojo.
        # El 4 sale en Helvetica Bold solo, por la regla de las cifras.
        {"foto": "fotos/pointfix/03.jpg", "y": 232,
         "sobre": "ALAMBRE DE PÚAS",
         "caja": "POINTFIX, 4 PUNTAS",
         "bajada": "Resistente, pensado para **cercos agrícolas y ganaderos**."},

        # L4 · rotulado «(Tip pro)» pero es descriptivo, no una orden de oficio:
        #      registro normal. «Se instala con postes y grapas» /
        #      «tensado parejo a lo largo de todo el cerco.»
        # ⭐ RONDA 1 — Paulina, 23-09-2026, dos comentarios:
        #   sobre el titular: «dejar en dos líneas "se instala con" / "postes y grapas"»
        #   sobre la bajada:  «dejar en una sola línea, disminuir pt si es necesario
        #                      para que se vea estético»
        # El corte del titular se mueve una palabra a la derecha. La bajada tiene 43
        # letras y a 40 px pasaba de los 740 de `max-width`, así que se partía en dos:
        # con 34 entra en una.
        {"foto": "fotos/pointfix/04.jpg", "y": 226,
         "sobre": "SE INSTALA CON",
         "caja": "POSTES Y GRAPAS",
         "bajada": "Tensado **parejo** a lo largo de todo el cerco.", "bajada_cuerpo": 34},

        # L5 · CIERRE — brief: «Alambre de púas Pointfix, disponible en Ebema.»
        #      Visual: rollo de alambre + logo Ebema.
        {"foto": "fotos/pointfix/05.jpg", "cierre": True},
    ],
}

if __name__ == "__main__":
    construir(CARRUSEL)
