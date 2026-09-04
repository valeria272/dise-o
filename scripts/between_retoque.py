#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Retoque fotográfico compartido de BETWEEN — el paso que faltaba.

⭐ RONDA 10 · segunda pasada (04-09-2026). Eli, sobre la primera entrega:

    «no se ve un retoque que se vea apetitosa las imágenes de comida»
    «el color está muy oscuro»
    «tiene que ser realista y no pegoteado»
    «borrar los detalles que se vean rayones o extraño en la mesa»
    «que se vea full real 4K»

La primera pasada resolvió el MATERIAL —producto real en vez de generado— pero
entregó las fotos **crudas**: la sesión del cliente está subexpuesta, la mesa de
listones está llena de marcas negras y el hojaldre sale plano. Una foto de banco
no se entrega tal cual; se revela.

Este módulo es ese revelado, y vive aparte porque las cuatro piezas de la ronda
lo comparten:

    limpia_madera()  quita rayones, grietas y motas de la mesa
    apetitoso()      claridad, calidez y cuerpo sobre la comida
    revela()         exposición, negros y contraste de la escena completa
    nitidez()        el remate, al final y con mano corta
    luz_envolvente() para montajes: funde el canto del recorte con su fondo

⚠️ El ORDEN importa: limpiar → revelar → apetitoso → nitidez. Al revés, la
   nitidez realza los rayones antes de borrarlos y la limpieza se come el grano
   que acabas de subir.
"""
import cv2
import numpy as np
from PIL import Image, ImageFilter


# ─────────────────────────── utilidades ───────────────────────────────────────
def _np(im):
    return np.asarray(im.convert("RGB")).astype(np.float32)


def _im(a):
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def _caja(a, r, eje):
    if r < 1:
        return a
    a = np.moveaxis(a, eje, 0)
    pad = np.concatenate([np.repeat(a[:1], r, 0), a, np.repeat(a[-1:], r, 0)], 0)
    c = np.cumsum(pad, axis=0, dtype=np.float64)
    c = np.concatenate([np.zeros((1,) + c.shape[1:]), c], 0)
    out = (c[2 * r + 1:] - c[:-(2 * r + 1)]) / (2 * r + 1)
    return np.moveaxis(out.astype(np.float32), 0, eje)


def borrosa(a, radio, pasadas=3):
    """Gaussiana aproximada sobre float32 — PIL no desenfoca en modo F."""
    r = max(1, int(round(radio / 2)))
    for _ in range(pasadas):
        a = _caja(_caja(a, r, 0), r, 1)
    return a


# ─────────────────────── 1 · limpiar la madera ────────────────────────────────
def limpia_madera(im, zona=None, umbral=17, nucleo=31, proteger=None):
    """Borra rayones, grietas y motas oscuras de la mesa.

    Cómo: se compara cada píxel contra la MEDIANA local. La veta de la madera es
    de baja frecuencia y sobrevive a la mediana; un rayón o una grieta no, así
    que aparece como un pozo oscuro contra ella. Donde el pozo pasa del umbral,
    manda la mediana.

    Es el «pincel corrector» de toda la vida, y funciona acá porque la mesa es
    lisa: sobre comida o loza haría papilla, de ahí `proteger`.

    zona     · máscara booleana de dónde se puede tocar (la mesa)
    proteger · máscara booleana de lo que NO se toca nunca (producto, loza)
    """
    bgr = cv2.cvtColor(np.asarray(im.convert("RGB")), cv2.COLOR_RGB2BGR)
    mediana = cv2.medianBlur(bgr, nucleo)
    hueco = (mediana.astype(np.int16) - bgr.astype(np.int16)).mean(axis=2)
    marcas = (hueco > umbral).astype(np.uint8) * 255
    marcas = cv2.morphologyEx(marcas, cv2.MORPH_CLOSE,
                              cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    marcas = cv2.dilate(marcas, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)))
    if zona is not None:
        marcas[~zona] = 0
    if proteger is not None:
        marcas[proteger] = 0
    alfa = (cv2.GaussianBlur(marcas, (0, 0), 4.0).astype(np.float32) / 255.0)[:, :, None]
    limpio = cv2.cvtColor(mediana, cv2.COLOR_BGR2RGB).astype(np.float32)
    base = np.asarray(im.convert("RGB")).astype(np.float32)
    return _im(base * (1 - alfa) + limpio * alfa), int((marcas > 0).sum())


# ─────────────────────── 2 · revelar la escena ────────────────────────────────
def revela(im, luces=214.0, negros=0.012, contraste=1.06, calidez_max=21.0,
           medios=None):
    """Exposición, punto negro y contraste. Es el «no se ve tan oscuro».

    · `luces` fija el p95 (el manual pide ~214 cuando el protagonista es comida
      clara: por encima de 215 el hojaldre pierde las capas);
    · `negros` recorta el 1,2 % inferior para que el negro sea negro y la foto
      deje de verse lavada y apagada a la vez;
    · la calidez se contiene como en el perfil `neutro` del mes.
    """
    a = _np(im)
    calidez = float(a[..., 0].mean() - a[..., 2].mean())
    if calidez > calidez_max + 1:
        ajuste = (calidez - calidez_max) * 0.55
        a[..., 0] -= ajuste * 0.62
        a[..., 2] += ajuste * 0.38
    p1 = float(np.percentile(a, negros * 100))
    a = (a - p1) * (255.0 / max(1.0, 255.0 - p1))
    p95 = float(np.percentile(a, 95))
    if p95 > 1:
        a *= min(1.55, max(0.85, luces / p95))
    if medios:
        # gamma para levantar los MEDIOS sin tocar el blanco: una escena de
        # madera oscura y muro verde puede tener el p95 en su sitio y aun así
        # leerse apagada, porque la mediana está abajo. Es el «está muy oscuro».
        mediana = max(1.0, float(np.median(a)))
        gamma = np.log(max(medios, 1.0) / 255.0) / np.log(mediana / 255.0)
        a = np.power(np.clip(a / 255.0, 0, 1), np.clip(gamma, 0.55, 1.6)) * 255.0
    media = float(a.mean())
    a = (a - media) * contraste + media
    return _im(a)


# ─────────────────────── 3 · que dé hambre ────────────────────────────────────
def apetitoso(im, mascara=None, claridad=0.55, cuerpo=1.14, calor=6.0):
    """Claridad, saturación y calidez sobre la comida.

    `claridad` es contraste de MEDIA frecuencia (unsharp de radio grande): es lo
    que separa las capas del hojaldre y hace que el queso se vea fundido en vez
    de plano. `cuerpo` sube la saturación sólo donde ya hay color, así que no
    ensucia los grises de la loza.
    """
    a = _np(im)
    base = borrosa(a, 26)
    a = a + (a - base) * claridad                       # claridad
    gris = a.mean(axis=2, keepdims=True)
    a = gris + (a - gris) * cuerpo                      # cuerpo (saturación)
    a[..., 0] += calor * 0.6                            # calidez de horno
    a[..., 2] -= calor * 0.4
    if mascara is not None:
        m = mascara[:, :, None].astype(np.float32)
        a = _np(im) * (1 - m) + a * m
    return _im(a)


# ─────────────────────── 4 · el remate ────────────────────────────────────────
def nitidez(im, cantidad=0.42, radio=1.5):
    a = _np(im)
    return _im(a + (a - borrosa(a, radio)) * cantidad)


# ─────────────────── 5 · para montajes: fundir el canto ───────────────────────
def luz_envolvente(fondo, figura, radio=26, fuerza=0.55):
    """Mete la luz del fondo en el canto de la figura recortada.

    Es LO que separa un montaje creíble de un sticker: en una foto real, la luz
    del ambiente moja el borde del sujeto. Sin esto el recorte se lee como un
    papel pegado encima, por muy limpio que esté el alfa.
    """
    alfa = np.asarray(figura.getchannel("A")).astype(np.float32) / 255.0
    borde = np.clip(alfa - (np.asarray(
        figura.getchannel("A").filter(ImageFilter.MinFilter(9))
    ).astype(np.float32) / 255.0), 0, 1)
    borde = borrosa(borde[:, :, None], radio)[:, :, 0] * fuerza
    f = _np(fondo)
    halo = borrosa(f, radio * 1.6)
    mezcla = f * (1 - borde[:, :, None]) + halo * borde[:, :, None]
    salida = _im(mezcla).convert("RGBA")
    salida.alpha_composite(figura)
    # y un pelo del color del fondo derramado sobre el canto del sujeto
    derrame = Image.fromarray(
        np.dstack([borrosa(f, radio * 2).astype(np.uint8),
                   (borde * 190).astype(np.uint8)]))
    salida.alpha_composite(derrame)
    return salida
