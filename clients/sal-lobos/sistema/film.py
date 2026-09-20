#!/usr/bin/env python3
"""EL ÚLTIMO GESTO — película de tono. Montaje.

NO es un comercial terminado: es una referencia de dirección de arte y ritmo.

Se monta sin Remotion y sin After Effects, en Python, porque el ffmpeg que trae
este repo viene RECORTADO (`--disable-filters`): no tiene overlay, fade, crop ni
drawtext. Así que cada fotograma se compone acá con PIL/numpy y se le entrega a
ffmpeg por tubería PNG (`-f image2pipe`), que sí funciona. El audio sí se arma con
ffmpeg, porque sus filtros de audio (adelay, amix, volume, atrim) están todos.

Ventaja de hacerlo así: la gradación de la película sale del MISMO kit que las
nueve piezas gráficas, así que el film y los key visuals comparten la firma
cromática exacta en vez de parecerse.

    python3 clients/sal-lobos/sistema/film.py            # las 4 entregas
    python3 clients/sal-lobos/sistema/film.py --solo 16x9
"""
from __future__ import annotations

import argparse
import io
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cv2  # noqa: E402
import kit  # noqa: E402
import numpy as np  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

RAIZ = kit.RAIZ
PLANOS_DIR = RAIZ / "raw/sal-lobos/film/planos"
AUDIO_DIR = RAIZ / "raw/sal-lobos/film/audio"
SALIDA = RAIZ / "out/spl/20260915_film"
FFMPEG = RAIZ / "node_modules/@remotion/compositor-darwin-arm64/ffmpeg"
FFLIB = str(RAIZ / "node_modules/@remotion/compositor-darwin-arm64")

FPS = 25

# ─────────────────────────────────────────────────────────── el guion
# `voz` mide lo que dura cada clip de locución, MEDIDO con ffprobe. El corte se
# construye sobre esa medida y no sobre una estimación: el texto es intocable, así
# que la voz manda y la imagen se acomoda.
VOZ = {"t1": 2.35, "t2": 4.21, "t3": 10.45, "t4": 7.39,
       "t5": 6.03, "t6": 7.63, "t7": 5.96}

# Cada entrada: (id, plano de origen, entrada en el origen, duración en el corte).
# `foco` encuadra el 16:9 y `foco9` lo corrige para el vertical cuando hace falta:
# el 9:16 NO es un recorte ciego del 16:9. Los valores se eligieron mirando la
# tira de control de los ocho planos reencuadrados, para no cortar ninguna mano.
# `apaga` = (centro_x, centro_y, radio, fuerza). Sólo donde hace falta: t1 trae la
# ventana de la cocina y t3b una cortina clara, y las dos pelean con la regla
# «fondo oscuro, sólo la acción iluminada». Medido: t1 tenía 1,51 % de píxeles
# quemados y t3b 0,95 %.
CORTE = [
    # La mancha clara de la ventana mide x 0,006-0,270 (109.219 px sobre 170 de
    # luma, medido en t1). Se probó recortarla en origen y la olla quedaba pegada
    # al borde del 16:9, así que se resuelve acotando la protección de brillo del
    # apagado: el 5º valor de `apaga` es ese radio.
    dict(t="T1", src="t1", desde=0.6, dur=3.05, foco=(0.52, 0.55), empuje=0.0,
         foco9=(0.26, 0.62), apaga=(0.42, 0.70, 0.30, 0.90, 0.26)),
    dict(t="T2", src="t2", desde=0.2, dur=4.55, foco=(0.50, 0.50), empuje=0.0),
    dict(t="T3a", src="t3a", desde=0.2, dur=3.50, foco=(0.42, 0.50), empuje=0.0),
    dict(t="T3b", src="t3b", desde=0.2, dur=3.50, foco=(0.58, 0.50), empuje=0.0,
         apaga=(0.62, 0.42, 0.24, 0.95)),
    dict(t="T3c", src="t3c", desde=0.2, dur=3.50, foco=(0.55, 0.50), empuje=0.0),
    # T4 — la repetición. El CORTE hace el argumento: es la misma acción y nunca
    # es igual. Seis planos cortos, manos distintas, corte seco.
    dict(t="T4a", src="t2", desde=1.6, dur=1.30, foco=(0.50, 0.50), empuje=0.0),
    dict(t="T4b", src="t3b", desde=1.2, dur=1.30, foco=(0.58, 0.50), empuje=0.0,
         apaga=(0.62, 0.42, 0.24, 0.95)),
    dict(t="T4c", src="t3a", desde=1.4, dur=1.30, foco=(0.42, 0.50), empuje=0.0),
    dict(t="T4d", src="t3c", desde=1.5, dur=1.30, foco=(0.55, 0.50), empuje=0.0),
    dict(t="T4e", src="t2", desde=3.2, dur=1.30, foco=(0.50, 0.50), empuje=0.0),
    dict(t="T4f", src="t3b", desde=2.4, dur=1.30, foco=(0.58, 0.50), empuje=0.0,
         apaga=(0.62, 0.42, 0.24, 0.95)),
    dict(t="T5", src="t5", desde=0.0, dur=6.70, foco=(0.50, 0.55), empuje=0.0,
         foco9=(0.40, 0.58), apaga=(0.52, 0.52, 0.30, 0.80)),
    # T6 — el ÚNICO plano abierto. Fotografía fija con un empuje mínimo: el brief
    # pide «un leve empuje o nada» y prohíbe el travelling de comercial.
    dict(t="T6", src="salar", desde=0.0, dur=7.90, foco=(0.50, 0.42), empuje=0.035),
    dict(t="T7", src="cierre", desde=0.0, dur=7.00, foco=(0.50, 0.50), empuje=0.0),
]

# Locución: cama continua. La voz corre POR SOBRE los cortes de imagen, como en
# cualquier película — no se reinicia en cada plano.
VOZ_EN = {"t1": 0.45, "t2": 3.25, "t3": 7.85, "t4": 18.45,
          "t5": 26.10, "t6": 32.90, "t7": 40.60}

# T5: «Silencio real en T5, cuando la sal desaparece. El silencio es el argumento.»
# No es un fundido: es silencio DIGITAL. Verificado midiendo la mezcla — ese tramo
# da -104 dBFS. Sale de que el plano t5 dura 6,05 s y su tramo en el corte dura
# 6,70 s, así que los últimos 0,65 s no tienen sonido directo, la voz de T6 entra
# recién en 32,90 y la nota del salar también. Está buscado, no es un accidente.
SILENCIO_REAL = (32.13, 32.90)

FORMATOS = {
    "16x9": (1920, 1080),
    "9x16": (1080, 1920),
}


# ─────────────────────────────────────────────────────────── lectura de planos
class Fuente:
    """Un plano de origen: video generado o fotografía fija."""

    def __init__(self, ruta: Path):
        self.ruta = ruta
        self.es_video = ruta.suffix.lower() in (".mp4", ".mov", ".webm")
        if self.es_video:
            cap = cv2.VideoCapture(str(ruta))
            self.fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
            self.n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.dur = self.n / self.fps
            self.cuadros = []
            while True:
                ok, fr = cap.read()
                if not ok:
                    break
                self.cuadros.append(fr[:, :, ::-1].copy())     # BGR → RGB
            cap.release()
            self.n = len(self.cuadros)
        else:
            self.cuadros = [np.asarray(Image.open(ruta).convert("RGB"))]
            self.fps, self.n, self.dur = 1.0, 1, 1e9

    def en(self, t: float) -> np.ndarray:
        """El fotograma que corresponde al segundo t. Si el plano se acaba,
        SOSTIENE el último — nunca repite el clip ni lo estira."""
        if not self.es_video:
            return self.cuadros[0]
        i = min(int(round(t * self.fps)), self.n - 1)
        return self.cuadros[max(i, 0)]


def reencuadrar(a: np.ndarray, W: int, H: int, foco, empuje: float,
                p: float, pre=None) -> Image.Image:
    """Recorta al formato y aplica el empuje mínimo. Nunca estira.

    `pre` recorta el plano de ORIGEN antes de encuadrar, en fracciones del cuadro.
    Existe por T1: la ventana de la cocina sobrevivía al apagado de fondo, porque
    apagar_fondo protege deliberadamente lo muy claro para no matar la sal — y una
    ventana es exactamente eso. Bajar la protección habría apagado los granos, así
    que la ventana se recorta de raíz y vale para los dos formatos.
    """
    im = Image.fromarray(a)
    if pre:
        l, t, r, b = pre
        im = im.crop((int(l * im.width), int(t * im.height),
                      int(r * im.width), int(b * im.height)))
    if empuje:
        z = 1.0 + empuje * p
        nw, nh = int(im.width / z), int(im.height / z)
        x0 = int((im.width - nw) * foco[0])
        y0 = int((im.height - nh) * foco[1])
        im = im.crop((x0, y0, x0 + nw, y0 + nh))
    return kit.encajar(im, W, H, foco=foco)


def tarjeta_cierre(W: int, H: int, p: float) -> Image.Image:
    """T7. Navy y el lockup completo. Y sólo después, el logo.

    El lockup entra con su propio ritmo: primero el titular, después el filete,
    después la bajada. Se hace con opacidad sobre el campo, no con un fundido de
    la pieza entera, para que las tres partes lleguen juntas al final — la regla
    dice que el concepto NUNCA aparece solo, ni por un segundo.
    """
    base = kit.campo_navy(W, H, kit.NAVY_LOBOS, kit.NAVY_PROFUNDO).convert("RGBA")
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    tam = int(0.088 * W) if W > H else int(0.135 * W)
    caja = kit.medir_lockup(capa, x=0, y=0, tam=tam, ancho_max=int(0.74 * W))
    x = (W - caja["ancho"]) // 2
    y = int(H * 0.44) - caja["alto"] // 2
    kit.lockup(capa, x=x, y=y, tam=tam, ancho_max=int(0.74 * W),
               alineacion="izquierda")

    # aparición: 0 → 0,9 s el lockup entra; el logo entra después, nunca antes
    a_lock = min(max((p - 0.04) / 0.16, 0.0), 1.0)
    capa.putalpha(capa.getchannel("A").point(lambda v: int(v * a_lock)))
    base.alpha_composite(capa)

    a_logo = min(max((p - 0.40) / 0.18, 0.0), 1.0)
    if a_logo > 0:
        cl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        kit.firma_spl(cl, alto=int(0.072 * H) if W > H else int(0.042 * H),
                      x=W // 2 + int(0.055 * W), y=int(H * 0.80), anclaje="ri")
        cl.putalpha(cl.getchannel("A").point(lambda v: int(v * a_logo)))
        base.alpha_composite(cl)
    return base.convert("RGB")


# ─────────────────────────────────────────────────────────── el video
def fuentes() -> dict:
    f = {}
    for k in ("t1", "t2", "t3a", "t3b", "t3c", "t5"):
        p = PLANOS_DIR / f"{k}.mp4"
        if p.is_file():
            f[k] = Fuente(p)
    f["salar"] = Fuente(kit.ACTIVOS / "salar-horizonte.jpg")
    return f


def construir(nombre: str, W: int, H: int, corte: list, fuen: dict,
              negro_final: float = 0.0) -> tuple[Path, float]:
    """Compone cada fotograma y lo entrega a ffmpeg por tubería PNG."""
    SALIDA.mkdir(parents=True, exist_ok=True)
    destino = SALIDA / f"{nombre}_sinaudio.mp4"
    dur_total = sum(c["dur"] for c in corte) + negro_final
    env = dict(os.environ, DYLD_LIBRARY_PATH=FFLIB)
    ff = subprocess.Popen(
        [str(FFMPEG), "-y", "-f", "image2pipe", "-vcodec", "png",
         "-framerate", str(FPS), "-i", "-",
         "-c:v", "libx264", "-preset", "medium", "-crf", "17",
         "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(destino)],
        stdin=subprocess.PIPE, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL, env=env)

    hechos = 0
    for c in corte:
        n = max(1, int(round(c["dur"] * FPS)))
        src = fuen.get(c["src"])
        for i in range(n):
            p = i / max(n - 1, 1)
            if c["src"] == "cierre":
                im = tarjeta_cierre(W, H, p)
            else:
                a = src.en(c["desde"] + i / FPS)
                foco = c.get("foco9", c["foco"]) if H > W else c["foco"]
                im = reencuadrar(a, W, H, foco, c["empuje"], p, c.get("pre"))
                if c.get("apaga"):
                    ap = c["apaga"]
                    cx, cy, rad, fz = ap[:4]
                    pr = ap[4] if len(ap) > 4 else None
                    im = kit.apagar_fondo(im, centro=(cx, cy), radio=rad,
                                          fuerza=fz, piso=0.22, gate_frio=0.55,
                                          protege_radio=pr)
                # la firma cromática: el MISMO kit que las nueve piezas gráficas
                im = kit.gradar_navy(im, fuerza=0.62, lift_sal=0.55)
            b = io.BytesIO()
            im.save(b, "PNG", compress_level=1)
            ff.stdin.write(b.getvalue())
            hechos += 1
        print(f"    {c['t']:5} {c['src']:7} {c['dur']:5.2f}s  {n:3} cuadros",
              flush=True)

    for _ in range(int(round(negro_final * FPS))):
        b = io.BytesIO()
        Image.new("RGB", (W, H), kit.rgb(kit.NAVY_PROFUNDO)).save(
            b, "PNG", compress_level=1)
        ff.stdin.write(b.getvalue())
        hechos += 1

    ff.stdin.close()
    ff.wait()
    print(f"  ✓ {destino.name}  {hechos} cuadros  {hechos / FPS:.2f}s")
    return destino, hechos / FPS


# ─────────────────────────────────────────────────────────── el audio
def construir_audio(nombre: str, corte: list, dur: float,
                    con_voz: bool = True) -> Path:
    """Sonido directo de cocina + locución + el grano + la nota del salar.

    El sonido directo sale del AUDIO NATIVO de cada plano generado: es lo más
    cercano al «sonido directo» que pide el brief. Va bajo, porque el protagonista
    es el grano cayendo.
    """
    env = dict(os.environ, DYLD_LIBRARY_PATH=FFLIB)
    entradas, filtros, mezcla = [], [], []
    idx = 0

    # 1 · sonido directo, plano por plano, en su posición del corte
    t = 0.0
    for c in corte:
        p = PLANOS_DIR / f"{c['src']}.mp4"
        if c["src"] not in ("cierre", "salar") and p.is_file():
            entradas += ["-ss", f"{c['desde']:.3f}", "-t", f"{c['dur']:.3f}",
                         "-i", str(p)]
            filtros.append(
                f"[{idx}:a]volume=0.42,adelay={int(t * 1000)}|{int(t * 1000)}"
                f",apad=whole_dur={dur:.3f}[d{idx}]")
            mezcla.append(f"[d{idx}]")
            idx += 1
        t += c["dur"]

    # 2 · el grano cayendo: «ese último sonido es el protagonista»
    for pos, vol in ((5.10, 0.85), (26.60, 0.70)):
        entradas += ["-i", str(AUDIO_DIR / "sfx_grano.mp3")]
        filtros.append(f"[{idx}:a]volume={vol},adelay={int(pos * 1000)}|"
                       f"{int(pos * 1000)},apad=whole_dur={dur:.3f}[d{idx}]")
        mezcla.append(f"[d{idx}]")
        idx += 1

    # 3 · la nota sostenida: entra RECIÉN en T6, con el salar. Nada de piano.
    entradas += ["-i", str(AUDIO_DIR / "sfx_nota.mp3")]
    filtros.append(f"[{idx}:a]volume=0.22,adelay=32900|32900,"
                   f"apad=whole_dur={dur:.3f}[d{idx}]")
    mezcla.append(f"[d{idx}]")
    idx += 1

    # 4 · la locución, como cama continua
    if con_voz:
        for k, en in VOZ_EN.items():
            f = AUDIO_DIR / f"voz_{k}.mp3"
            if not f.is_file():
                continue
            entradas += ["-i", str(f)]
            filtros.append(f"[{idx}:a]volume=1.0,adelay={int(en * 1000)}|"
                           f"{int(en * 1000)},apad=whole_dur={dur:.3f}[d{idx}]")
            mezcla.append(f"[d{idx}]")
            idx += 1

    destino = AUDIO_DIR / f"mezcla_{nombre}.wav"
    # OJO: este ffmpeg viene con --disable-filters y sólo trae una lista blanca.
    # `alimiter` y `dynaudnorm` NO existen acá, así que la cabeza se controla con
    # volúmenes conservadores y normalize=0 en el amix, no con un limitador.
    cadena = ";".join(filtros) + ";" + "".join(mezcla) + \
        f"amix=inputs={len(mezcla)}:normalize=0,volume=1.40,aresample=48000[out]"
    cmd = [str(FFMPEG), "-y"] + entradas + \
        ["-filter_complex", cadena, "-map", "[out]",
         "-t", f"{dur:.3f}", "-c:a", "pcm_s16le", str(destino)]
    r = subprocess.run(cmd, capture_output=True, env=env)
    if r.returncode != 0:
        print(r.stderr.decode()[-1500:])
        raise RuntimeError("la mezcla de audio falló")
    print(f"  ✓ {destino.name}")
    return destino


def unir(video: Path, audio: Path, destino: Path) -> Path:
    env = dict(os.environ, DYLD_LIBRARY_PATH=FFLIB)
    r = subprocess.run(
        [str(FFMPEG), "-y", "-i", str(video), "-i", str(audio),
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
         str(destino)], capture_output=True, env=env)
    if r.returncode != 0:
        print(r.stderr.decode()[-1500:])
        raise RuntimeError("el muxeo falló")
    print(f"  ✓ {destino.name}")
    return destino


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", help="16x9 | 9x16 | corto | planos")
    a = ap.parse_args()

    faltan = [k for k in ("t1", "t2", "t3a", "t3b", "t3c", "t5")
              if not (PLANOS_DIR / f"{k}.mp4").is_file()]
    if faltan:
        sys.exit(f"✗ Faltan planos en {PLANOS_DIR}: {faltan}\n"
                 f"  Se generan con Seedance 2.5 desde los stills aprobados.")

    fuen = fuentes()
    SALIDA.mkdir(parents=True, exist_ok=True)
    hecho = []

    if a.solo in (None, "16x9"):
        print("MASTER 16:9")
        W, H = FORMATOS["16x9"]
        v, dur = construir("master_16x9", W, H, CORTE, fuen, negro_final=0.5)
        au = construir_audio("master", CORTE, dur)
        hecho.append(unir(v, au, SALIDA / "sallobos_ultimogesto_master_16x9.mp4"))

    if a.solo in (None, "9x16"):
        print("VERTICAL 9:16 — mismo corte")
        W, H = FORMATOS["9x16"]
        v, dur = construir("vertical_9x16", W, H, CORTE, fuen, negro_final=0.5)
        au = construir_audio("vertical", CORTE, dur)
        hecho.append(unir(v, au, SALIDA / "sallobos_ultimogesto_vertical_9x16.mp4"))

    if a.solo in (None, "corto"):
        # El corto que pide el brief: T2 + T4 + T7.
        print("CORTO 15 s — T2 + T4 + T7")
        # Con las duraciones del máster esto daba 16,85 s. El brief pide 15, así
        # que se recorta el plano madre, se aprieta la repetición y se acorta el
        # cierre: 4,00 + 6 x 1,15 + 3,85 + 0,3 de negro = 15,05 s.
        corto = [dict(c) for c in CORTE
                 if c["t"] == "T2" or c["t"].startswith("T4") or c["t"] == "T7"]
        for c in corto:
            if c["t"] == "T2":
                c["dur"] = 4.00
            elif c["t"].startswith("T4"):
                c["dur"] = 1.15
            else:
                c["dur"] = 3.85
        W, H = FORMATOS["16x9"]
        v, dur = construir("corto_15s", W, H, corto, fuen, negro_final=0.3)
        au = construir_audio("corto", corto, dur, con_voz=False)
        hecho.append(unir(v, au, SALIDA / "sallobos_ultimogesto_corto_15s.mp4"))

    if a.solo in (None, "planos"):
        # Los planos sueltos, sin música ni texto, para reutilizar.
        print("PLANOS SUELTOS — sin música ni texto")
        sueltos = SALIDA / "planos-sueltos"
        sueltos.mkdir(parents=True, exist_ok=True)
        W, H = FORMATOS["16x9"]
        for c in CORTE:
            if c["src"] in ("cierre",):
                continue
            uno = [dict(c, desde=c["desde"], dur=c["dur"])]
            v, dur = construir(f"suelto_{c['t']}", W, H, uno, fuen)
            # van CON su sonido directo y SIN música ni locución, que es lo que
            # sirve para reeditar. Mudos no servirían de nada.
            fuente_a = PLANOS_DIR / f"{c['src']}.mp4"
            destino = sueltos / f"sallobos_plano_{c['t']}.mp4"
            if fuente_a.is_file():
                env = dict(os.environ, DYLD_LIBRARY_PATH=FFLIB)
                r = subprocess.run(
                    [str(FFMPEG), "-y", "-i", str(v),
                     "-ss", f"{c['desde']:.3f}", "-t", f"{c['dur']:.3f}",
                     "-i", str(fuente_a),
                     "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                     "-c:a", "aac", "-b:a", "192k", "-shortest", str(destino)],
                    capture_output=True, env=env)
                if r.returncode == 0:
                    v.unlink(missing_ok=True)
                else:
                    v.replace(destino)
            else:
                v.replace(destino)
        hecho.append(sueltos)

    (SALIDA / "corte.json").write_text(json.dumps(
        {"fps": FPS, "voz_medida_s": VOZ, "voz_entra_s": VOZ_EN,
         "silencio_real_s": SILENCIO_REAL,
         "duracion_total_s": round(sum(c["dur"] for c in CORTE) + 0.5, 2),
         "corte": CORTE}, ensure_ascii=False, indent=2))
    print("\n".join(f"  → {h}" for h in hecho))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
