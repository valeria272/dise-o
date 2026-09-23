#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · carrusel MASISA — Tablero Estructural (octubre 2026, 03/10).

⚠️ ESTE BRIEF CAMBIÓ. El 15-09 Paulina aprobó un carrusel de «línea melamina y
cantos» de 5 láminas; la grilla del 22-09 lo reemplazó por «Tablero Estructural
Masisa» para un clóset empotrado, con 4 láminas y SIN tip pro. Manda la grilla
(§0-bis: el brief no es nuestro). Se reusan las reglas de composición aprobadas.

Familia A · producto en stock. Los textos van VERBATIM del brief: lo único que
decide diseño es el reparto entre las tres zonas y a qué altura cae el bloque.

Uso:  python carrusel_masisa.py && bash render.sh masisa
"""
from _motor import construir

# ---------------------------------------------------------------- el brief ---
# CARRUSEL — Un clóset que exige un tablero a la altura
# Producto: Tablero Estructural Masisa.
# Pilar: Proveedores · 03/10/2026 · REF ACTUALIZADA (Pinterest, en la grilla)
CARRUSEL = {
    "slug": "masisa",
    "proveedor_logo": "img/proveedores/logo_masisa.png",
    "producto": "Tablero Estructural Masisa",
    # Su L2 aprobada aterrizó en 778 y calza con toro (783,4), la referencia de
    # línea más larga. Se mantiene: es el mismo producto y el mismo registro.
    "ancho_caja_des": 778,
    "laminas": [
        # L1 · PORTADA
        # brief texto:  «Tablero Estructural Masisa para un clóset empotrado bien resuelto.»
        # brief bajada: «Precisión, firmeza y una base adecuada para trabajar muebles a medida.»
        # brief visual: «Maestro tomando medidas dentro del nicho donde irá instalado el
        #                clóset. Debe verse claramente que es un espacio empotrado y que el
        #                mueble se está fabricando a medida.»
        #
        # ⭐ RONDA 1 — Paulina, 23-09-2026, dos comentarios sobre esta portada:
        #   «dejemos este texto en el cuadro blanco»  -> señalando el pre-enunciado
        #   «este texto dejémoslo con el formato que queda sobre la flecha»
        #                                             -> señalando la cápsula
        # O sea se INTERCAMBIAN: el nombre del producto pasa a la cápsula blanca y
        # la bajada del brief baja al pie, sobre la flecha. Ya no hay pre-enunciado
        # acá — el titular queda en dos niveles y el rojo muerde el gancho igual.
        {"foto": "fotos/masisa/01.jpg", "y": 660, "portada": True,
         "sobre": "PARA UN CLÓSET EMPOTRADO",
         "caja": "BIEN RESUELTO",
         "capsula": "Tablero Estructural Masisa",
         "pie": "Precisión, firmeza y una base adecuada para trabajar muebles a medida"},

        # L2 · precisión en el trabajo
        # brief texto:  «Cuando el espacio es exacto, el corte también tiene que serlo.»
        # brief visual: «Detalle del tablero siendo medido y cortado, mostrando canto,
        #                superficie y precisión de la pieza.»  → ESPECIFICACIÓN → zoom
        # ⭐ RONDA 1 — Paulina: «que sean 2 líneas. Primero "cuando el espacio es
        # exacto,", segundo "el corte también tiene que serlo". Disminuir o aumentar
        # pt para que se vea estético.» El corte del brief cambia de sitio: la coma
        # cierra la línea blanca y el rojo se lleva la frase entera. Con 32 letras
        # dentro del rojo, 778 lo dejaba muy chico: esta lámina declara su propio
        # ancho de caja, 860, y el `cuerpo` baja para que la blanca no se desborde.
        {"foto": "fotos/masisa/02.jpg", "y": 250, "ancho_caja": 860,
         "sobre": "CUANDO EL ESPACIO ES EXACTO,", "cuerpo": 46,
         "caja": "EL CORTE TAMBIÉN TIENE QUE SERLO",
         "bajada": "Superficie pareja para trabajar piezas a medida, con **cortes limpios** y buen ajuste en obra."},

        # L3 · estructura y espesor
        # brief texto:  «La estructura parte por elegir bien el tablero.»
        # brief visual: «Estructura interior del clóset en proceso, mostrando repisas,
        #                divisiones y diferentes puntos de apoyo.»  → USO → escena
        {"foto": "fotos/masisa/03.jpg", "y": 226,
         "sobre": "LA ESTRUCTURA PARTE",
         "caja": "POR ELEGIR BIEN EL TABLERO",
         "bajada": "Considera dimensiones, distribución y carga antes de definir el **espesor**."},

        # L4 · CIERRE — plantilla dura de §4-bis: anillo + botón + «en el link de la bio!»
        # brief texto:  «Tablero Estructural Masisa: una base firme para trabajos a medida.»
        # brief visual: «Clóset empotrado terminado, integrado de muro a muro.»
        {"foto": "fotos/masisa/04.jpg", "cierre": True},
    ],
}

if __name__ == "__main__":
    construir(CARRUSEL)
