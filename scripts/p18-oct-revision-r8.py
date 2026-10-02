#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — ronda 8 (02-10): los comentarios de Eli sobre la ronda 7.

    python scripts/p18-oct-revision-r8.py
"""
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
R = "out/piso18/oct/r8-respaldo/"
E = "out/piso18/oct/entrega/"
CUADROS = RAIZ / "out/piso18/oct/r8"
CUADROS.mkdir(parents=True, exist_ok=True)


def tira(mp4: Path, clave: str, segundos, alto: int = 960) -> str:
    """Una tira de fotogramas del MP4, lado a lado, para comparar el antes con el ahora."""
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    ims = []
    for i, t in enumerate(segundos):
        tmp = CUADROS / f"_{clave}-{i}.png"
        subprocess.run([ff, "-v", "error", "-y", "-ss", f"{t}", "-i", str(mp4), "-frames:v", "1", str(tmp)], check=True)
        im = Image.open(tmp).convert("RGB")
        ims.append(im.resize((round(im.width * alto / im.height), alto), Image.LANCZOS))
        tmp.unlink()
    hoja = Image.new("RGB", (sum(i.width for i in ims) + 12 * (len(ims) - 1), alto), "white")
    x = 0
    for im in ims:
        hoja.paste(im, (x, 0))
        x += im.width + 12
    dst = CUADROS / f"{clave}.jpg"
    hoja.save(dst, quality=90)
    return str(dst.relative_to(RAIZ)).replace("\\", "/")


p = Pagina(
    "piso18",
    "PISO18 · GRILLA OCTUBRE 2026 · RONDA 8",
    "Tus comentarios de la ronda 7, pieza por pieza",
    "02-10-2026 · 6 piezas corregidas · todo reemplazado en Drive",
    "out/piso18/oct/revision-r8.html",
    origen="scripts/p18-oct-revision-r8.py",
)
p.pedido(
    "El carrusel, la lámina 2, me parece bien. En la ST de cuenta regresiva, me gustaría que el sobre tuviera "
    "un poco de texturita para que se viera más realista. Revisa que realmente esté el botón en brief. La "
    "fiesta de empresa de fin de año, la fotografía se ve un poco extraña, yo ocuparía una real, y que la hoja "
    "se vea un poquitito más texturizada. En la encuesta de estaciones, que sea una sola tipografía, máximo "
    "dos. Para el post animado de cumpleaños, cada beneficio encerrado en cajillas del mismo tamaño, tal vez "
    "algún ícono, y faltan más detalles porque parece más matrimonio. Para la historia animada, que no tape "
    "mucho los rostros. La ST del 30-10 me gusta mucho; trata de utilizar mejores videos",
    "Eli", "02-10-2026",
    que="El carrusel Fechas 2027 queda como está (aprobado). Lo que el cliente había pedido ahí, en la celda "
        "C13 del FEED: «Eliminar temporada alta de la G2».")

p.comparar(
    (R + "P18 ST 13-10 Cuenta regresiva al 2027.png", "sobre liso"),
    (E + "S3/STS/P18 ST 13-10 Cuenta regresiva al 2027.png", "sobre con fibra de papel"),
    titulo="ST 13-10 · Cuenta regresiva al 2027", detalle=(110, 980, 970, 1580), escala=1.0,
    notas=("Qué cambió", [
        "El sobre lleva <b>textura de papel real</b> (fibra y pliegues suaves), atrás y adelante. La tarjeta "
        "blanca queda limpia.",
        "<b>El botón se queda:</b> revisé la grilla y la celda de interacción dice «CTA: Cotiza ya en piso18.cl».",
        "Textos: sin cambios."]))

p.comparar(
    (R + "P18 ST 19-10 Fiesta de empresa fin de ano.png", "foto generada, hoja lisa"),
    (E + "S4/STS/P18 ST 19-10 Fiesta de empresa fin de ano.png", "foto real, hoja con textura"),
    titulo="ST 19-10 · Fiesta de empresa de fin de año", detalle=(170, 380, 930, 1500), escala=0.9,
    notas=("Qué cambió", [
        "La polaroid ahora es una <b>foto real</b> de un evento en Piso18 (sesión «Piso18 julio evento», foto "
        "106): los spritz en la barra iluminada, con los invitados de traje detrás. No se distingue ningún rostro.",
        "La hoja de cuaderno suma la fibra y los pliegues del papel, apenas más marcada que antes.",
        "Textos y botón: sin cambios (el brief trae «CTA: Asegura tu fecha en piso18.cl»)."]))

p.comparar(
    (R + "P18 ST 21-10 Estaciones de comida.png", "cinco voces tipográficas"),
    (E + "S4/STS/P18 ST 21-10 Estaciones de comida.png", "dos voces"),
    titulo="ST 21-10 · Encuesta estaciones de comida", detalle=(120, 520, 960, 1000), escala=1.0,
    notas=("Qué cambió", [
        "«Estación Japonesa» y «Estación New York» van en <b>una sola tipografía</b> y un solo cuerpo (antes "
        "«Estación» iba en fina recta y el nombre en itálica más grande).",
        "La pregunta entera va en esa misma itálica; «menú perfecto» sólo cambia de color.",
        "La pieza queda en <b>dos voces</b>: IvyPresto itálica (rótulos y pregunta) y Raleway (el dato).",
        "Textos: sin cambios. Sin botón, porque el brief trae sticker y no CTA."]))

mp4 = "P18 FEED 20-10 Cumpleanos en Piso18.mp4"
p.comparar(
    (R + "P18 FEED 20-10 Cumpleanos en Piso18 portada.png", "lista suelta, foto sin detalles de cumpleaños"),
    (E + "S4/FEED/P18 FEED 20-10 Cumpleanos en Piso18 portada.png", "cajas iguales con ícono, foto de cumpleaños"),
    titulo="FEED 20-10 · Post animado · Cumpleaños en Piso18", detalle=(200, 400, 880, 800), escala=1.2,
    notas=("Qué cambió", [
        "Cada beneficio va en su <b>caja</b>: las cinco del mismo tamaño, centradas y más cortas que el ancho "
        "de la lámina, con el texto centrado adentro.",
        "En el cuadro fucsia va un <b>ícono</b> por beneficio (globo, parlante, cubiertos, copa, hamburguesa), "
        "del mismo set profesional del carrusel de cumpleaños de la S5.",
        "La foto es la misma, <b>editada para que se lea cumpleaños</b>: globos dorados, fucsia y blancos, "
        "regalos, serpentinas, confeti y velas de colores en la torta.",
        "Las cajas entran una por una; la foto sigue quieta, como pide el brief. Entrega: MP4 + GIF + portada.",
        "Textos: sin cambios."]))
p.opciones(
    [(tira(RAIZ / E / "S4/FEED" / mp4, "f2010-r8", (1.6, 3.2, 7.5), alto=900), "1,6 s · 3,2 s · 7,5 s")],
    titulo="FEED 20-10 · cómo entran las cajas", ancho=900, elige=False)

mp4 = "P18 ST 16-10 Equipo Piso18.mp4"
p.comparar(
    (tira(RAIZ / R / mp4, "s1610-r7", (1.5, 6.5, 10.5)), "el texto sobre los rostros"),
    (tira(RAIZ / E / "S3/STS" / mp4, "s1610-r8", (1.5, 6.5, 10.5)), "el texto abajo, los rostros despejados"),
    titulo="ST 16-10 · Animada · Equipo Piso18", ancho=760,
    notas=("Qué cambió", [
        "El titular bajó al tercio inferior y es algo más chico: <b>ya no pisa ningún rostro</b>.",
        "El oscurecido también se movió: la franja de las caras queda limpia y el velo va detrás del texto.",
        "Los cuatro planos son los mismos de ayer. Textos y botón: sin cambios.",
        "Entrega: MP4 + GIF + portada."]))

mp4 = "P18 ST 30-10 Broche perfecto.mp4"
p.comparar(
    (tira(RAIZ / R / mp4, "s3010-r7", (1.5, 4.5, 7.2, 11.0)), "planos de ayer"),
    (tira(RAIZ / E / "S5/STS" / mp4, "s3010-r8", (1.5, 4.5, 7.2, 11.0)), "planos nuevos"),
    titulo="ST 30-10 · Animada · El broche perfecto para tu historia", ancho=900,
    notas=("Qué cambió", [
        "Los <b>cuatro planos son nuevos</b>, del mismo material real de Piso18, elegidos por nitidez y con la "
        "cámara derecha: el atardecer por el ventanal con la mesa montada, el centro de flores de cerca, el "
        "salón de noche con las guirnaldas, y el letrero de neón.",
        "Salieron los de ayer: uno tenía la cámara chueca y una persona parada en la pista, otro tenía hojas "
        "desenfocadas en primer plano, y el letrero estaba inclinado con una licuadora a la vista.",
        "El <b>letrero ahora va nivelado</b> y sin la licuadora; en ese plano el oscurecido de arriba se "
        "aclara para que el neón brille.",
        "Titular, botón y duración: sin cambios. Entrega: MP4 + GIF + portada."]))

p.notas([
    "<b>Todo está reemplazado en Drive</b> con el mismo nombre (enlaces conservados), en las carpetas de semana "
    "de Piso18 (S3 a S5).",
    "Lo de ayer quedó respaldado en local: <code>out/piso18/oct/r8-respaldo/</code>.",
    "Tu comentario de la historia animada se cortó en «y que los textos…». Bajé el titular y lo achiqué un "
    "poco; si era otra cosa, dímela y la ajusto.",
    "El QA automático sigue sin correr completo en esta máquina: zonas seguras, «sin bodas» y «sin punto en "
    "títulos» se revisaron a mano."],
    titulo="Notas")
p.escribir()
