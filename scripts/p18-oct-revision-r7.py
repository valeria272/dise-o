#!/usr/bin/env python3
"""PISO18 · OCTUBRE 2026 — ronda 7 (01-10): el cambio del carrusel de la primera semana,
las historias del 13 y 19-10 con el comentario del cliente, y lo que faltaba por diseñar.

    python scripts/p18-oct-revision-r7.py
"""
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _revision import Pagina  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
R = "out/piso18/oct/r7-respaldo/"
E = "out/piso18/oct/entrega/"
REF = "raw/hilton/piso18/oct/refs/"
CUADROS = RAIZ / "out/piso18/oct/r7"
CUADROS.mkdir(parents=True, exist_ok=True)


def cuadros(mp4: str, clave: str, segundos):
    """Saca fotogramas del MP4 entregado para mostrarlos en la página."""
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    out = []
    for i, t in enumerate(segundos):
        dst = CUADROS / f"{clave}-{i}.jpg"
        subprocess.run([ff, "-v", "error", "-y", "-ss", f"{t}", "-i", str(RAIZ / E / mp4), "-frames:v", "1",
                        "-q:v", "3", str(dst)], check=True)
        out.append((str(dst.relative_to(RAIZ)).replace("\\", "/"), f"{t:.1f} s".replace(".", ",")))
    return out


p = Pagina(
    "piso18",
    "PISO18 · GRILLA OCTUBRE 2026 · RONDA 7",
    "El cambio del carrusel, las historias del 13 y 19-10 y lo que faltaba por diseñar",
    "01-10-2026 · 1 lámina corregida + 6 piezas nuevas · todo en Drive",
    "out/piso18/oct/revision-r7.html",
    origen="scripts/p18-oct-revision-r7.py",
)
p.pedido(
    "Sigamos con los diseños de Piso18, toma las stories la del 13 y 19 de octubre, solo que corrige según "
    "comentario de cliente ya que solo ese era el cambio. Lo demás y toma lo que falta por diseñar + el "
    "cambio en el carrusel de la s1 de piso18",
    "Eli", "01-10-2026",
    que="La grilla se leyó en vivo (celdas e hilos) antes de partir. Lo que había: el carrusel Fechas 2027 "
        "EN CAMBIOS con un comentario nuevo; las historias del 13 y 19-10 con el comentario del cliente; y "
        "en OK PARA DISEÑAR sin pieza, el post animado del 20-10 y las historias del 16, 21 y 30-10.")

p.comparar(
    (R + "P18 FEED 09-10 Fechas 2027 2.png", "con «TEMPORADA ALTA 2027»"),
    (E + "S2/FEED/P18 FEED 09-10 Fechas 2027 2.png", "sin el rótulo"),
    titulo="FEED · Carrusel Fechas 2027 · lámina 2", detalle=(140, 150, 940, 520), escala=1.0,
    notas=("Qué cambió", [
        "Cliente (FEED C13): <b>«Eliminar temporada alta de la G2»</b> → salió el rótulo «TEMPORADA ALTA 2027».",
        "Nada más se movió: titular, «Asegura tu fecha 2027» y calendario quedan donde los aprobaste.",
        "Reemplazada en Drive con el mismo nombre (enlace conservado)."]))

p.opciones(
    [(REF + "st-13-10-cuenta-regresiva-0.jpg", "<b>REF</b> — sobre con tarjeta"),
     (E + "S3/STS/P18 ST 13-10 Cuenta regresiva al 2027.png", "<b>ST 13-10</b>")],
    titulo="ST 13-10 · Cuenta regresiva al 2027", elige=False,
    notas=("Cómo se armó", [
        "Cliente: <b>«Digamos Cuenta regresiva al 2027 · No hablemos de temporada alta»</b> → el titular es "
        "«Cuenta regresiva al 2027» y la palabra «temporada» no aparece.",
        "Calcada de la ref: sobre abierto (en el fucsia de Piso18) con la tarjeta asomando sobre una mesa real "
        "de matrimonio. El bloque de precio es el de la promo aprobada «¿Te casas en verano?»: ANTES tachado, "
        "AHORA en caja fucsia.",
        "Bajada sobre el sobre, legal «*Desde 60 invitados» al pie, botón «Cotiza ya en piso18.cl» (el brief trae CTA).",
        "<b>Ojo:</b> el brief pedía «número de días destacado». No lo puse porque no está en los textos y "
        "cambia según el día en que se publique; si lo quieren, es el sticker de cuenta regresiva de Instagram "
        "o me dices la cifra."]))

p.opciones(
    [(REF + "st-19-10-fin-de-ano-0.jpg", "<b>REF</b> — polaroid + hoja de cuaderno"),
     (E + "S4/STS/P18 ST 19-10 Fiesta de empresa fin de ano.png", "<b>ST 19-10</b>")],
    titulo="ST 19-10 · Fiesta de empresa de fin de año", elige=False,
    notas=("Cómo se armó", [
        "Cliente: <b>«Ok pero no digamos diciembre, cerremos en corporativas · Foco fiesta empresa fin de año»</b> "
        "→ la bajada termina en «para fiestas corporativas»; «diciembre» no aparece en ninguna parte.",
        "Calcada de la ref: fondo en blanco y negro (mesas reales del salón de noche), polaroid a color con "
        "cinta fucsia y hoja de cuaderno arrancada con el texto.",
        "La foto de la polaroid es un brindis producido sobre el salón y la barra reales, tomada desde atrás "
        "del grupo (la primera tirada salió de banco de imágenes y la descarté).",
        "Botón «Asegura tu fecha en piso18.cl» (CTA del brief)."]))

p.opciones(
    [(REF + "st-15-10-cumple-0.jpg", "<b>REF</b> — la misma de la 15-10"),
     (E + "S4/STS/P18 ST 21-10 Estaciones de comida.png", "<b>ST 21-10</b>")],
    titulo="ST 21-10 · Encuesta estaciones de comida", elige=False,
    notas=("Cómo se armó", [
        "Brief ya corregido por contenido: «pantalla dividida», Estación Japonesa vs. Estación New York, y "
        "sticker de 3 opciones (Japonesa / New York / ¡Las 2!) que pone el CM.",
        "La ref es la misma de la historia del 15-10. Para que no salgan dos historias iguales en seis días, "
        "de la ref tomé la hoja de papel rasgado con la pregunta y la composición es la del brief: la pantalla "
        "partida en dos, con la hoja cruzando el corte.",
        "El papel bajo el texto queda limpio para el sticker. Sin botón: el brief no trae CTA.",
        "Las dos fotos son producidas sobre el buffet real de Piso18 (no hay fotos de esas estaciones)."]))

p.opciones(
    cuadros("S4/FEED/P18 FEED 20-10 Cumpleanos en Piso18.mp4", "f2010", (0.6, 2.6, 7.5)),
    titulo="FEED 20-10 · Post animado · Cumpleaños en Piso18 (8 s)", elige=False,
    notas=("Cómo se armó", [
        "Cliente: <b>«Que se animen los textos de las cosas que incluye el cumple»</b>; brief: «la imagen debe "
        "mantenerse quieta». La foto no se mueve; entran el título y los cinco textos uno por uno.",
        "Los números van en cuadro fucsia, como la lista de beneficios aprobada del carrusel de cumpleaños de la S5.",
        "Foto producida sobre el salón real de noche, con la torta como protagonista (brief), sin personas.",
        "Entrega: MP4 + GIF + portada."]))

p.opciones(
    cuadros("S3/STS/P18 ST 16-10 Equipo Piso18.mp4", "s1610", (1.5, 4.5, 10.5)),
    titulo="ST 16-10 · Animada · Equipo Piso18 (11,5 s)", elige=False,
    notas=("Cómo se armó", [
        "Cliente: <b>«Solo texto principal»</b> → va sólo «El secreto de una noche inolvidable está en los "
        "detalles», centrado y quieto sobre el video, como las dos refs.",
        "Video <b>real</b> de Piso18 (cápsulas de marzo 2026, disco F:): barman, garzón armando la bandeja de "
        "copas, garzona con bandeja de cóctel y la bandeja de cerca.",
        "Botón «Conoce más en piso18.cl» al final (CTA del brief).",
        "<b>Ojo:</b> se ven caras del equipo real y el uniforme lleva bordado DoubleTree. Es lo que pide el brief "
        "(«garzones sirviendo»), pero mírala con eso en mente; puedo cambiar a planos sin rostro.",
        "Entrega: MP4 + GIF + portada. Medida fotograma a fotograma: sin congelados ni negros."]))

p.opciones(
    cuadros("S5/STS/P18 ST 30-10 Broche perfecto.mp4", "s3010", (1.5, 4.5, 11.0)),
    titulo="ST 30-10 · Animada · El broche perfecto para tu historia (11,6 s)", elige=False,
    notas=("Cómo se armó", [
        "Cliente: <b>«Dejémos El broche perfecto para tu historia»</b> → salió «En Piso18,».",
        "Brief: «recorrido breve por el venue terminando en fachada o logo Piso18». Video <b>real</b>: salón "
        "montado, mesa larga bajo las lámparas, ventanal con la ciudad, y cierra en el letrero de neón PISO18 "
        "de la barra. En ese último plano el logotipo de arriba se apaga para no tener dos.",
        "Botón «Reserva tu fecha en piso18.cl» al final (CTA del brief).",
        "Entrega: MP4 + GIF + portada."]))

p.notas([
    "<b>Todo está en Drive</b>, en las carpetas de semana de Piso18 (S2 a S5), con md5 verificado.",
    "El QA automático no corrió completo en esta máquina (Windows bloquea una librería): las zonas seguras, "
    "«sin bodas» y «sin punto en títulos» se revisaron a mano.",
    "Siguen fuera: ST 08-10 (PENDIENTE POR CLIENTE) y el reel orgánico del Día del Chef (sin estado).",
    "Respaldo de la lámina anterior del carrusel: <code>out/piso18/oct/r7-respaldo/</code>."],
    titulo="Notas")
p.escribir()
