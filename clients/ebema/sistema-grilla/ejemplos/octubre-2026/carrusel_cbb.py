#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · carrusel CBB — Cemento Especial CBB (octubre 2026, 10/10).

Uso:  python carrusel_cbb.py && bash render.sh cbb
"""
from _motor import construir

# ---------------------------------------------------------------- el brief ---
# CARRUSEL — Hormigón que resiste los sulfatos del suelo agrícola
# Producto: Cemento Especial CBB (puzolánico). Mismo perfil que julio, pero con
# situación distinta (julio = ambiente marino/costero).
# Pilar: Proveedores · 10/10/2026
CARRUSEL = {
    "slug": "cbb",
    "proveedor_logo": "img/proveedores/logo_cbb.png",
    "producto": "Cemento Especial CBB",
    "ancho_caja_des": 760,
    "laminas": [
        # L1 · PORTADA
        # brief: «Una fundación en el campo no enfrenta el mismo suelo que una en la ciudad.»
        #        Visual: terreno agrícola o parcela con fundación en construcción.
        #
        # El brief NO trae subtexto para la portada, y la cápsula blanca no es
        # opcional (§4-bis). Se llena con el descriptor del producto tal como lo
        # escribe el copy de esa misma diapositiva: «de base puzolánica».
        {"foto": "fotos/cbb/01.jpg", "y": 636, "portada": True,
         "pre": "UNA FUNDACIÓN EN EL CAMPO",
         "sobre": "NO ENFRENTA EL MISMO SUELO",
         "caja": "QUE UNA EN LA CIUDAD",
         "capsula": "Cemento Especial CBB, de base puzolánica",
         "pie": ""},

        # L2 · brief: «El suelo agrícola tiene sulfatos naturales» / «con el tiempo,
        #      atacan y deterioran el hormigón común.»
        #      Visual: detalle de hormigón dañado → ESPECIFICACIÓN → zoom
        {"foto": "fotos/cbb/02.jpg", "y": 246,
         "sobre": "EL SUELO AGRÍCOLA TIENE", "cuerpo": 56,
         "caja": "SULFATOS NATURALES",
         "bajada": "Con el tiempo, **atacan y deterioran** el hormigón común."},

        # L3 · brief: «Cemento Especial CBB, pensado para esa exposición» /
        #      «formulación puzolánica que resiste el ataque químico del suelo.»
        #      Visual: aplicación o mezcla del cemento → USO → escena
        {"foto": "fotos/cbb/03.jpg", "y": 232,
         "sobre": "CEMENTO ESPECIAL CBB,", "cuerpo": 58,
         "caja": "PENSADO PARA ESA EXPOSICIÓN",
         "bajada": "Formulación puzolánica que resiste el **ataque químico** del suelo."},

        # L4 · el brief lo rotula «(Tip pro)» pero es un beneficio, no una orden de
        #      oficio: va en el registro normal (§4-bis, el caso de cedral).
        #      «Ideal para fundaciones, radieres y estructuras rurales o agrícolas» /
        #      «mayor durabilidad frente a suelos con sulfatos.»
        {"foto": "fotos/cbb/04.jpg", "y": 220,
         "sobre": "IDEAL PARA FUNDACIONES,|RADIERES Y ESTRUCTURAS", "cuerpo": 54,
         "caja": "RURALES O AGRÍCOLAS",
         "bajada": "Mayor durabilidad frente a **suelos con sulfatos**."},

        # L5 · CIERRE — brief: «Cemento Especial CBB, disponible en Ebema.»
        #      Visual: sacos CBB + logo Ebema. Van DESENFOCADOS y sin marca legible:
        #      el packshot de marca no se genera con IA (§5).
        {"foto": "fotos/cbb/05.jpg", "cierre": True},
    ],
}

if __name__ == "__main__":
    construir(CARRUSEL)
