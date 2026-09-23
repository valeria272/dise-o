#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · carrusel SAN JUAN — Cemento Especial San Juan (octubre 2026, 20/10).

Uso:  python carrusel_sanjuan.py && bash render.sh sanjuan
"""
from _motor import construir

# ---------------------------------------------------------------- el brief ---
# CARRUSEL — Hormigón que resiste el contacto permanente con agua
# Producto: Cemento Especial San Juan (puzolánico). Mismo ángulo de fondo que
# agosto, aplicado a una estructura distinta (agosto = muro de contención;
# CBB este mes = suelo con sulfatos agrícola).
# Pilar: Proveedores · 20/10/2026
CARRUSEL = {
    "slug": "sanjuan",
    "proveedor_logo": "img/proveedores/logo_san-juan.png",
    "producto": "Cemento Especial San Juan",
    "ancho_caja_des": 780,
    "laminas": [
        # L1 · PORTADA
        # brief: «Un estanque o un pozo exige más que hormigón común.»
        #        Visual: estanque de acumulación de agua o pozo en construcción.
        {"foto": "fotos/sanjuan/01.jpg", "y": 644, "portada": True,
         "sobre": "UN ESTANQUE O UN POZO",
         "caja": "EXIGE MÁS QUE HORMIGÓN COMÚN",
         "capsula": "Cemento Especial San Juan, de formulación puzolánica",
         "pie": ""},

        # L2 · brief: «El contacto permanente con agua desgasta el hormigón común» /
        #      «con el tiempo, pierde resistencia y se agrieta.»
        #      Visual: detalle de hormigón deteriorado por humedad → ESPECIFICACIÓN → zoom
        {"foto": "fotos/sanjuan/02.jpg", "y": 248,
         "sobre": "EL CONTACTO PERMANENTE|CON AGUA DESGASTA", "cuerpo": 56,
         "caja": "EL HORMIGÓN COMÚN",
         "bajada": "Con el tiempo, **pierde resistencia** y se agrieta."},

        # L3 · brief: «Cemento Especial San Juan, formulación puzolánica» / «pensado
        #      para estructuras en contacto directo con agua o suelo húmedo.»
        #      Visual: aplicación o mezcla del cemento → USO → escena
        {"foto": "fotos/sanjuan/03.jpg", "y": 234,
         "sobre": "CEMENTO ESPECIAL SAN JUAN,", "cuerpo": 52,
         "caja": "FORMULACIÓN PUZOLÁNICA",
         "bajada": "Pensado para estructuras en **contacto directo con agua** o suelo húmedo."},

        # L4 · rotulado «(Tip pro)» pero es un beneficio, no una orden de oficio:
        #      registro normal (§4-bis, el caso de cedral).
        #      «Ideal para estanques, pozos y fosas» /
        #      «mayor durabilidad frente a la humedad constante.»
        {"foto": "fotos/sanjuan/04.jpg", "y": 224,
         "sobre": "IDEAL PARA ESTANQUES,",
         "caja": "POZOS Y FOSAS",
         "bajada": "Mayor durabilidad frente a la **humedad constante**."},

        # L5 · CIERRE — brief: «Cemento Especial San Juan, disponible en Ebema.»
        #      Visual: sacos San Juan + logo Ebema. Desenfocados y sin marca legible:
        #      el packshot de marca no se genera con IA (§5).
        {"foto": "fotos/sanjuan/05.jpg", "cierre": True},
    ],
}

if __name__ == "__main__":
    construir(CARRUSEL)
