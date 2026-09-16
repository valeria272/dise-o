#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deja la revisión de la RONDA 4 de PISO18 como DOCUMENTO DE GOOGLE.

    python scripts/p18-s4-r4-doc.py --dry-run
    python scripts/p18-s4-r4-doc.py

Por qué existe: la página local `out/piso18/s4/revision-r4/index.html` sirve en
esta máquina, pero Eli pidió verla «en Google». Drive **no renderiza** un `.html`
—lo ofrece para descargar—, así que la vía que sí se abre en el navegador es
subirlo pidiendo la **conversión a Documento de Google**: Drive importa el HTML y
deja un doc con las imágenes dentro, que se ve en el teléfono, se comparte y
admite comentarios.

⚠️ DOS COSAS CAMBIAN respecto de la página local, y no son capricho:

1. **Tablas en vez de grilla CSS.** El importador de Drive ignora `display:grid`
   y apila todo en una columna — y un antes/después apilado deja de ser una
   comparación. Con `<table>` de dos celdas el par queda lado a lado.
2. **Los videos se reemplazan por fotogramas.** Un Documento de Google no
   reproduce video. Van los dos fotogramas del titular, y el enlace al `.mp4`
   de Drive queda al pie para verlo de verdad.

Y las imágenes viajan **embebidas en base64**: si fueran rutas relativas, el
importador no las encuentra y el documento sale sin una sola foto.
"""
from __future__ import annotations

import argparse
import base64
import io
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google  # noqa: E402

from google.auth.transport.requests import Request  # noqa: E402
from google.oauth2.credentials import Credentials  # noqa: E402
from googleapiclient.discovery import build  # noqa: E402
from googleapiclient.http import MediaFileUpload  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(str(_RAIZ))
IMG = RAIZ / "out/piso18/s4/revision-r4/img"
SALIDA = RAIZ / "out/piso18/s4/revision-r4/para-google.html"

# S4 HILTON SEP 2026 › PISO18
PISO18_S4 = "1xHin8e7Iw4gdGR5x-Z_akFCokOzy4wE3"
TITULO = "PISO18 · S4 ronda 4 · antes y después (16-09)"

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]

# Enlaces a las piezas ya subidas, para que el doc lleve a la pieza de verdad.
EN_DRIVE = {
    "g3": "https://drive.google.com/file/d/1dbMi93lrPETdnAadSaJRmVJ40UdTfGft/view",
    "st3": "https://drive.google.com/file/d/1q8V7ibQtVGYijeAgKK0UPCkCyaYMAyTV/view",
    "st4": "https://drive.google.com/file/d/1zpdMH_NB73bSSz6scy3flPtZkQa7kAp8/view",
    "post": "https://drive.google.com/file/d/1POosvbTfM1s15gOmcxfg7uwz7dT2zUbZ/view",
    "carpeta": "https://drive.google.com/drive/folders/1xHin8e7Iw4gdGR5x-Z_akFCokOzy4wE3",
}


def dato(nombre: str) -> str:
    """La imagen como URI de datos. Sin esto el documento sale sin fotos."""
    crudo = (IMG / nombre).read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(crudo).decode()


def foto(nombre: str, ancho: int) -> str:
    return f'<img src="{dato(nombre)}" width="{ancho}">'


def par(izq: tuple[str, str, str], der: tuple[str, str, str], ancho: int = 300) -> str:
    """Una fila de dos celdas: (rótulo, archivo, pie) a cada lado."""
    celdas = []
    for rotulo, archivo, pie in (izq, der):
        celdas.append(
            f'<td width="50%" valign="top">'
            f'<p><b>{rotulo}</b></p>{foto(archivo, ancho)}'
            f'<p><span style="font-size:9pt;color:#666666">{pie}</span></p></td>')
    return ('<table border="0" cellpadding="8" width="100%"><tr>'
            + "".join(celdas) + "</tr></table>")


def trio(a, b, c, ancho: int = 195) -> str:
    celdas = []
    for rotulo, archivo, pie in (a, b, c):
        celdas.append(
            f'<td width="33%" valign="top">'
            f'<p><b>{rotulo}</b></p>{foto(archivo, ancho)}'
            f'<p><span style="font-size:9pt;color:#666666">{pie}</span></p></td>')
    return ('<table border="0" cellpadding="8" width="100%"><tr>'
            + "".join(celdas) + "</tr></table>")


def documento() -> str:
    p = []
    a = p.append
    a("<h1>PISO18 &middot; S4 ronda 4 &mdash; antes y despu&eacute;s</h1>")
    a("<p><i>16 de septiembre de 2026. Los cuatro cambios que dej&oacute; el cliente en la "
      "grilla de la S4, aplicados y subidos a Drive. La S3 no se toc&oacute;: la hace Eli.</i></p>")
    a("<p><span style='font-size:9pt;color:#666666'>Lo nuevo se detect&oacute; comparando la grilla "
      "viva de hoy contra la copia del 15-09, por conjunto de cadenas. Hizo falta porque ese mismo "
      "d&iacute;a <b>se corrieron las columnas</b>: &laquo;Piso18 de noche&raquo; pas&oacute; del 25-09 al 23-09 y "
      "&laquo;Secci&oacute;n fotos novios&raquo; ocup&oacute; el 25-09.</span></p>")
    a("<hr>")

    # ── 1 · carrusel ──────────────────────────────────────────────────
    a("<h2>1 &middot; 21-09 &middot; Carrusel de feed &mdash; la G3</h2>")
    a("<p><b>Lo que pidi&oacute;:</b> <i>&laquo;Hag&aacute;mosle + zoom a la G3 para que no sea tan "
      "protagonista el mes&oacute;n, el resto OK!&raquo;</i></p>")
    a("<p>El recorte anterior entraba a <b>ancho completo</b> de la foto, y por eso cab&iacute;a el "
      "mes&oacute;n con patas y todo: el tablero ca&iacute;a al <b>63&nbsp;%</b> del alto. El nuevo cierra sobre "
      "el arreglo y el tablero baja al <b>85&nbsp;%</b>. <b>Y el arreglo no se toca</b>: en vez de bajar "
      "el corte de arriba, el recorte sube a y=0, as&iacute; que las pampas siguen enteras.</p>")
    a(par(("ANTES &middot; ronda 3", "a-g3.jpg",
           "El mes&oacute;n entero. Tablero al 63&nbsp;% y las patas hasta el borde."),
          ("AHORA", "g3.jpg",
           "El arreglo manda. Tablero al 85&nbsp;%, las pampas intactas arriba.")))
    a("<p>Las otras tres no se tocaron &mdash; <i>&laquo;el resto OK!&raquo;</i>. El carrusel completo:</p>")
    a('<table border="0" cellpadding="6" width="100%"><tr>'
      + "".join(f'<td width="25%" valign="top">{foto(f"g{n}.jpg", 145)}'
                f'<p><span style="font-size:9pt;color:#666666">G{n}{t}</span></p></td>'
                for n, t in ((1, " portada"), (2, ""), (3, " <b>corregida</b>"), (4, "")))
      + "</tr></table>")
    a(f'<p><span style="font-size:9pt">Pieza en Drive: '
      f'<a href="{EN_DRIVE["g3"]}">C1 S4 N&deg;3.png</a> &mdash; mismo enlace de siempre.</span></p>')
    a("<hr>")

    # ── 2 · encuesta ──────────────────────────────────────────────────
    a("<h2>2 &middot; 25-09 &middot; Historia encuesta &mdash; la opci&oacute;n B</h2>")
    a("<p><b>Lo que pidi&oacute;:</b> <i>&laquo;En la B, pongamos una opci&oacute;n m&aacute;s de mesa para cenar, "
      "ya que las otras 2 propuestas son m&aacute;s de esa onda.&raquo;</i></p>")
    a("<p>El defecto no era la foto: era que <b>no se pod&iacute;an comparar</b>. La A y la C son centros "
      "de mesa <b>puestos</b>, con copas, platos y mantel. La B era el arreglo del <b>mes&oacute;n suelto</b>, "
      "con patas y piso. La B nueva es mantel negro, bajoplato dorado, copas moradas y un centro bajo "
      "de rosas crema y palo rosa con vela.</p>")
    a(trio(("ANTES", "a-tira-b.jpg", "El mes&oacute;n con patas y piso."),
           ("AHORA", "tira-b.jpg", "Mesa puesta, a la misma escala que la A y la C."),
           ("POR QU&Eacute; &Eacute;STA", "g1.jpg",
            "La primera candidata era la mesa de tulipanes&hellip; pero <b>es el mismo montaje de la G1 "
            "del carrusel</b>. Carrusel el 21 y encuesta el 25 con la misma escena es repetir el feed, "
            "as&iacute; que fui a un tercer montaje.")))
    a(par(("ANTES", "a-st4.jpg", "La B romp&iacute;a la serie."),
          ("AHORA", "st4.jpg",
           "Tres mesas puestas y tres estilos florales distintos: pampa seca, rosas cl&aacute;sicas y "
           "blanco con verde."), 240))
    a(f'<p><span style="font-size:9pt">Pieza en Drive: '
      f'<a href="{EN_DRIVE["st4"]}">ST N&deg;4 S4.png</a> &mdash; mismo enlace.</span></p>')
    a("<hr>")

    # ── 3 · animada ───────────────────────────────────────────────────
    a("<h2>3 &middot; 23-09 &middot; Historia animada &mdash; texto nuevo</h2>")
    a("<p>Ac&aacute; <b>no hubo comentario: cambi&oacute; el brief</b>. El montaje, los cinco planos y el "
      "ritmo quedan igual &mdash; s&oacute;lo cambia lo que dice.</p>")
    a('<table border="1" cellpadding="8" width="100%" style="border-collapse:collapse">'
      '<tr><td width="18%"><b></b></td><td width="41%"><b>Antes</b></td><td width="41%"><b>Ahora</b></td></tr>'
      '<tr><td><b>Texto principal</b></td>'
      '<td>As&iacute; se monta un evento en Piso18, paso a paso.</td>'
      '<td>Arreglos florales que le dan vida al matrimonio de tus sue&ntilde;os en Piso18.</td></tr>'
      '<tr><td><b>Bajada</b></td>'
      '<td>Dejando todo listo, para que solo te preocupes de celebrar.</td>'
      '<td><b>La borr&oacute;.</b> El brief pas&oacute; de dos l&iacute;neas a una.</td></tr></table>')
    a("<p><span style='font-size:9pt;color:#666666'>Un Documento de Google no reproduce video: van "
      "los fotogramas. El video completo est&aacute; en Drive, al pie de esta secci&oacute;n.</span></p>")
    a(trio(("ANTES", "a-st3.jpg", "&laquo;As&iacute; se monta un evento&hellip;&raquo;"),
           ("AHORA", "st3.jpg", "El texto nuevo, literal de la grilla. Entra en dos l&iacute;neas y no "
                                "toca la zona segura."),
           ("CIERRE", "st3-cierre.jpg", "Sin la bajada, el cierre queda logotipo + bot&oacute;n. El "
                                        "bot&oacute;n sube a y=1100 para ocupar el sitio.")))
    a("<p><b>Lo decides t&uacute;:</b> el comentario <i>&laquo;Podr&iacute;a ser un texto orientado a "
      "''Dejando todo listo, para que solo te preocupes de celebrar''&raquo;</i> <b>sigue en la celda y "
      "sin tachar</b>, y es el que hab&iacute;a producido la bajada. Como la grilla la borr&oacute;, la quit&eacute;. "
      "Si la quieres de vuelta se repone y el bot&oacute;n baja otra vez.</p>")
    a(f'<p><span style="font-size:9pt">Video en Drive: '
      f'<a href="{EN_DRIVE["st3"]}">ST N&deg;3 S4.mp4</a> &mdash; 1080&times;1920, 13,0 s, mismo enlace.</span></p>')
    a("<hr>")

    # ── 4 · post ──────────────────────────────────────────────────────
    a("<h2>4 &middot; 25-09 &middot; Post de feed &mdash; pieza nueva</h2>")
    a("<p><b>Lo que pidi&oacute;:</b> <i>&laquo;Que sea esta foto, con logo y estamos&raquo;</i> + el enlace.</p>")
    a("<p>Ese enlace es <b>piso_18-128.jpg</b>, de tu sesi&oacute;n del 28/AGO, y ya estaba en el estudio. "
      "Es horizontal y el feed va 4:5, as&iacute; que el recorte abre hacia la <b>izquierda</b>, que es donde "
      "est&aacute; el sal&oacute;n: mesas vestidas, sillas y los ventanales. Eso responde lo que ven&iacute;a pidiendo "
      "en el mismo hilo &mdash; <i>&laquo;planos m&aacute;s amplios&hellip; mostrar el espacio&raquo;</i> y "
      "<i>&laquo;que sean de ambiente, sin caras directas&raquo;</i>: no hay una sola persona en cuadro.</p>")
    a(par(("LA FOTO QUE MAND&Oacute;", "ref-post.jpg",
           "piso_18-128.jpg &middot; 5760&times;3840 &middot; sesi&oacute;n 28/AGO."),
          ("AHORA", "post.jpg",
           "2250&times;2813. Logotipo 568&nbsp;px en y=218, centrado &mdash; el mismo de la G1 aprobada.")))
    a("<p>El recorte izquierdo resuelve de paso el logotipo: la banda donde va queda en "
      "<b>luminancia 20&ndash;35</b> (techo oscuro) contra 88 si el recorte fuera centrado, que cae sobre "
      "las flores claras. Blanco sobre eso no se lee.</p>")
    a(f'<p><span style="font-size:9pt">Pieza en Drive: '
      f'<a href="{EN_DRIVE["post"]}">Post n&deg;2 S4 PISO18 25-09.png</a> &mdash; nueva.</span></p>')
    a("<hr>")

    # ── decisiones ────────────────────────────────────────────────────
    a("<h2>Tres cosas que decides t&uacute;</h2>")
    a("<p><b>1 &middot; El nombre del post.</b> El archivo <b>Post S4 PISO18 25-09.png</b> que ya estaba "
      "en Drive es el de &laquo;Piso18 de noche&raquo;, y la grilla lo movi&oacute; al <b>23-09</b>. El 25-09 ahora "
      "lo ocupa el post nuevo. Para no romper ning&uacute;n enlace no renombr&eacute; nada: sub&iacute; el nuevo como "
      "<b>Post n&deg;2 S4 PISO18 25-09.png</b>. Si prefieres renombrar el viejo a 23-09 y dejar el nuevo "
      "con el nombre limpio, se hace en un minuto.</p>")
    a("<p><b>2 &middot; La foto repetida.</b> piso_18-128 es tambi&eacute;n el <b>tercer plano de la historia "
      "animada del 23-09</b>. El cliente eligi&oacute; esa foto con nombre y apellido, as&iacute; que la us&eacute;; pero "
      "quedar&iacute;a la misma escena el 23 y el 25. Si quieres, cambio el plano de la animada.</p>")
    a("<p><b>3 &middot; La bajada de la animada.</b> La quit&eacute; porque la grilla la borr&oacute;, pero el "
      "comentario que la ped&iacute;a sigue vivo.</p>")

    a("<h2>Lo que no toqu&eacute;, y por qu&eacute;</h2>")
    a("<p><b>Toda la S3.</b> Tuya. Las piezas de la S3 en Drive las subiste t&uacute; desde tus editables, y "
      "el token del estudio no puede reemplazar archivos que subiste a mano. Los cambios que dej&oacute; el "
      "cliente ah&iacute; son: <b>16-09</b> &laquo;Quitemos Sujeto a disponibilidad y OK&raquo;, <b>20-09</b> "
      "&laquo;Quitar ese CTA, que sea foco reacci&oacute;n&raquo;, y en feed el <b>reel del 17-09</b> cambi&oacute; de "
      "texto en el brief: ahora pide &laquo;La atm&oacute;sfera indicada&raquo; en grande y &laquo;puede cambiar por "
      "completo tu celebraci&oacute;n&raquo; en chico.</p>")
    a("<p><b>ST N&deg;2 S4 &middot; 22-09:</b> pas&oacute; a APROBADO, sin comentarios nuevos. "
      "<b>Post &laquo;Piso18 de noche&raquo;:</b> sigue EN REVISI&Oacute;N y sin comentario nuevo; s&oacute;lo se movi&oacute; de "
      "fecha. <b>Carrusel de cumplea&ntilde;os &middot; 22-09:</b> pas&oacute; de CORREGIDO a APROBADO.</p>")

    a("<h2>Estado</h2>")
    a("<p>Las tres piezas corregidas se <b>reemplazaron conservando el enlace</b>; el post subi&oacute; nuevo. "
      "Las tres piezas sin cambios conservan su fecha en Drive, para que se vea de un vistazo qu&eacute; se "
      "toc&oacute; hoy. Las 8 piezas de la S4 pasan el QA de la marca.</p>")
    a(f'<p>Carpeta: <a href="{EN_DRIVE["carpeta"]}">S4 HILTON SEP 2026 &rsaquo; PISO18</a></p>')

    return ("<html><head><meta charset=\"utf-8\"><title>" + TITULO + "</title></head>"
            "<body style=\"font-family:Arial,sans-serif\">" + "".join(p) + "</body></html>")


def credenciales():
    cred = Credentials.from_authorized_user_file(str(_token_google()), SCOPES)
    if cred.expired and cred.refresh_token:
        cred.refresh(Request())
        # ⛔ No se reescribe el token: si Google devolviera menos scopes,
        # guardarlo degradaría los permisos de todo el monorepo.
    return cred


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="arma el HTML y no sube nada")
    a = ap.parse_args()

    html = documento()
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    io.open(SALIDA, "w", encoding="utf-8", newline="\n").write(html)
    print(f"  ✓ {SALIDA.relative_to(RAIZ)}  ({len(html)//1024} KB, imágenes embebidas)")

    if a.dry_run:
        print("\nEnsayo: no se subió nada.")
        return 0

    svc = build("drive", "v3", credentials=credenciales(), cache_discovery=False)
    # Si ya existe un doc con este título en la carpeta, se reemplaza su contenido
    # para no dejar dos versiones dando vueltas y para que el enlace no cambie.
    q = (f"name = '{TITULO}' and '{PISO18_S4}' in parents and trashed = false")
    hay = svc.files().list(q=q, fields="files(id)", pageSize=5).execute().get("files", [])
    media = MediaFileUpload(str(SALIDA), mimetype="text/html", resumable=True)
    if hay:
        f = svc.files().update(fileId=hay[0]["id"], media_body=media,
                               fields="id,webViewLink").execute()
        print(f"\n  ↻ documento actualizado\n     {f['webViewLink']}")
    else:
        meta = {"name": TITULO, "parents": [PISO18_S4],
                # ⭐ Esta línea es la conversión: Drive importa el HTML y deja un
                # Documento de Google que SÍ se abre en el navegador.
                "mimeType": "application/vnd.google-apps.document"}
        f = svc.files().create(body=meta, media_body=media,
                               fields="id,webViewLink").execute()
        print(f"\n  ✓ documento creado\n     {f['webViewLink']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
