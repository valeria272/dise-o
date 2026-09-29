"""BETWEEN · FEED 02-10 reel cumpleaños — RONDA 6: fondo nuevo «más Between».

Hilo de Scarlette Muñoz en la grilla (FEED!F15, 29-09 20:52): «el fondo no se ve muy
between». La foto aprobada tenía un interior de cafetería genérico (ampolletas colgantes,
techo oscuro). Se cambia SOLO el entorno por el jardín de invierno real de Between (muro
verde, piedra gris, toldo con guirnaldas), sin tocar la figura aprobada:

  1. `between-oct-generar.py f02-10-fondo --sufijo b` edita la foto aprobada con NB Pro 4K
     (refs: la aprobada + dos fotos reales del jardín de invierno).
  2. Se ALINEA la edición con la aprobada (ECC afín sobre la zona de manos y vaso).
  3. Se recorta a la persona de la edición (imgly) → máscara de primer plano.
  4. Fondo: se borra la llama (inpaint), se DESENFOCA (retrato de iPhone) y se oscurece el
     tercio de arriba para que los textos sigan leyéndose.
  5. Encima va la persona de la edición (su figura calza con la aprobada: diferencia media
     5–6/255 en logo y manos). La apagada toma la vela y los dedos sin brillo de la apagada
     vieja, sólo dentro de la elipse que ya estaba aprobada.
  6. Los recortes del hook `f-cumple-figura*.png` se rehacen desde la foto nueva con su
     mismo alfa.

Uso:  py scripts/bw-fd-02-10-cumple-fondo.py [--gen raw/.../gen-f02-10-fondo-b.png]
"""
import argparse
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

RAIZ = Path(__file__).resolve().parent.parent
OCT = RAIZ / "public/assets/hilton/between/oct"
TMP = RAIZ / "raw/hilton/between/oct/gen/f02-fondo"
W, H = 2160, 3840


def leer(p, flags=cv2.IMREAD_UNCHANGED):
    return cv2.imdecode(np.fromfile(str(p), np.uint8), flags)


def escribir(p, img, params=()):
    ok, buf = cv2.imencode(Path(p).suffix, img, list(params))
    buf.tofile(str(p))


def alfa_figura(nombre):
    """Alfa de la figura aprobada (1080×1920) llevado a 2160×3840, con borde suave."""
    f = leer(OCT / nombre)
    if f.ndim == 2 or f.shape[2] < 4:  # PNG paleta: cv2 la trae sin alfa → vía PIL
        from PIL import Image
        f = np.array(Image.open(OCT / nombre).convert("RGBA"))[:, :, [2, 1, 0, 3]]
    a = cv2.resize(f[:, :, 3], (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255
    a = cv2.GaussianBlur(a, (0, 0), 1.5)
    return np.clip(a, 0, 1)[..., None]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen", default=str(RAIZ / "raw/hilton/between/oct/gen/gen-f02-10-fondo-b.png"))
    ap.add_argument("--desenfoque", type=float, default=22)
    a = ap.parse_args()
    TMP.mkdir(parents=True, exist_ok=True)

    ref = leer(RAIZ / "out/hilton/between/oct-r6-respaldo/f-cumple-reel.jpg", cv2.IMREAD_COLOR)
    apag = leer(RAIZ / "out/hilton/between/oct-r6-respaldo/f-cumple-apagada.jpg", cv2.IMREAD_COLOR)
    gen = leer(a.gen, cv2.IMREAD_COLOR)
    gen = cv2.resize(gen, (W, round(gen.shape[0] * W / gen.shape[1])), interpolation=cv2.INTER_AREA)

    # 2 · alinear: ECC afín sobre manos + vaso (lo que la edición debía conservar)
    g1 = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY).astype(np.float32)
    g2 = cv2.cvtColor(gen, cv2.COLOR_BGR2GRAY).astype(np.float32)
    g2 = cv2.copyMakeBorder(g2, 0, max(0, H - g2.shape[0]), 0, 0, cv2.BORDER_REPLICATE)[:H]
    zona = np.zeros((H, W), np.uint8)
    zona[1400:3700, 300:2000] = 255
    M = np.array([[1, 0, 0], [0, 1, -(gen.shape[0] - H) / 2]], np.float32)
    _, M = cv2.findTransformECC(cv2.GaussianBlur(g1, (0, 0), 3), cv2.GaussianBlur(g2, (0, 0), 3), M,
                                cv2.MOTION_AFFINE,
                                (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 200, 1e-6), zona, 5)
    gen = cv2.warpAffine(gen, M, (W, H), flags=cv2.INTER_CUBIC | cv2.WARP_INVERSE_MAP,
                         borderMode=cv2.BORDER_REFLECT)
    print("afín:", np.round(M, 4).tolist())
    escribir(TMP / "gen-alineada.jpg", gen, (cv2.IMWRITE_JPEG_QUALITY, 95))

    # 3 · persona = recorte imgly (manos, vaso, vela) ∪ sweater por color (imgly lo deja fuera)
    persona = TMP / "gen-alineada-nobg.png"
    if not persona.is_file():
        subprocess.run(["npx", "tsx", "scripts/remove-bg.ts", str(TMP / "gen-alineada.jpg"), str(persona)],
                       cwd=RAIZ, check=True, shell=sys.platform == "win32")
    from PIL import Image
    a_img = np.array(Image.open(persona).convert("RGBA"))[:, :, 3].astype(np.float32) / 255
    lab = cv2.cvtColor(cv2.GaussianBlur(gen, (0, 0), 4), cv2.COLOR_BGR2LAB).astype(int)
    L, A, B = lab[..., 0], lab[..., 1] - 128, lab[..., 2] - 128
    torso = ((A > 8) & (L < 110) & (A > B - 2)).astype(np.uint8) * 255
    torso[:1560] = 0  # sobre los hombros sólo hay muro: corta la fuga hacia la piedra
    torso = cv2.morphologyEx(torso, cv2.MORPH_OPEN, np.ones((41, 41), np.uint8))
    torso = cv2.morphologyEx(torso, cv2.MORPH_CLOSE, np.ones((61, 61), np.uint8))
    n, lbl, st, _ = cv2.connectedComponentsWithStats(torso)
    torso = np.isin(lbl, [k for k in range(1, n) if st[k, 4] > 200000]).astype(np.float32)
    pa = np.maximum(a_img, cv2.GaussianBlur(torso, (0, 0), 6))
    pa = np.clip(cv2.GaussianBlur(pa, (0, 0), 1.5), 0, 1)[..., None]
    escribir(TMP / "persona.png", (pa[..., 0] * 255).astype(np.uint8))

    # 4 · fondo limpio: sin persona ni llama, desenfocado, tercio de arriba más bajo.
    # ⚠️ f-cumple-mascara-llama.png NO es la llama: es el golpe de luz entero (mano y tapa).
    # La llama sale por brillo dentro de su caja, sobre la punta de la vela.
    lum = cv2.cvtColor(gen, cv2.COLOR_BGR2GRAY)
    llama = np.zeros((H, W), np.uint8)
    caja = (slice(1380, 1720), slice(1020, 1200))
    llama[caja] = (lum[caja] > 150).astype(np.uint8) * 255
    llama = cv2.dilate(llama, np.ones((5, 5), np.uint8))
    escribir(TMP / "llama.png", llama)
    hueco = cv2.dilate(np.maximum((pa[..., 0] > 0.05).astype(np.uint8) * 255, llama),
                       np.ones((25, 25), np.uint8))
    # relleno por convolución normalizada: el fondo de alrededor se «derrama» al hueco sin
    # las estrías del inpaint TELEA
    libre = (hueco == 0).astype(np.float32)[..., None]
    sig = 90
    num = cv2.GaussianBlur(gen.astype(np.float32) * libre, (0, 0), sig)
    den = cv2.GaussianBlur(libre, (0, 0), sig)[..., None] + 1e-4
    relleno = num / den
    fondo = gen.astype(np.float32) * libre + relleno * (1 - libre)
    fondo = cv2.GaussianBlur(fondo, (0, 0), a.desenfoque)
    y = np.linspace(0, 1, H, dtype=np.float32)[:, None, None]
    fondo *= 1 - 0.38 * np.clip((0.42 - y) / 0.42, 0, 1) ** 1.2
    fondo[..., 0] *= 0.93  # el jardín de día sale frío al lado de la luz de la vela
    fondo[..., 2] *= 1.03
    fondo = np.clip(fondo, 0, 255)

    # 5 · encendida = persona editada sobre el fondo limpio
    enc = fondo * (1 - pa) + gen.astype(np.float32) * pa
    # apagada: sin llama, y en la elipse que ya estaba aprobada (vela + dedos sin brillo)
    # manda la apagada vieja, sólo donde hay figura
    sin_llama = cv2.dilate(llama, np.ones((31, 31), np.uint8)).astype(np.float32) / 255
    sin_llama = cv2.GaussianBlur(sin_llama, (0, 0), 6)[..., None]
    apa = enc * (1 - sin_llama) + fondo * sin_llama
    elipse = (np.abs(apag.astype(int) - ref.astype(int)).max(2) > 6).astype(np.uint8)
    elipse = cv2.morphologyEx(elipse, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8)).astype(np.float32)
    fig = alfa_figura("f-cumple-figura-apagada.png")[..., 0]
    fig = cv2.erode(fig, np.ones((7, 7), np.uint8)) * (1 - sin_llama[..., 0])
    w = np.clip(cv2.GaussianBlur(elipse * fig, (0, 0), 2), 0, 1)[..., None]
    apa = apa * (1 - w) + apag.astype(np.float32) * w

    for nombre, img in (("f-cumple-reel.jpg", enc), ("f-cumple-apagada.jpg", apa)):
        escribir(OCT / nombre, np.clip(img, 0, 255).astype(np.uint8), (cv2.IMWRITE_JPEG_QUALITY, 94))
        print("✓", nombre)

    # 6 · los recortes del hook salen de la foto NUEVA con el alfa aprobado (sin llama
    # fantasma en la apagada): si no, sobre el titular asoman trozos del fondo viejo
    llama_1080 = cv2.resize(sin_llama[..., 0], (1080, 1920))
    for nombre, img, sacar in (("f-cumple-figura.png", enc, False), ("f-cumple-figura-apagada.png", apa, True)):
        viejo = np.array(Image.open(RAIZ / "out/hilton/between/oct-r6-respaldo" / nombre).convert("RGBA"))
        alfa = viejo[:, :, 3].astype(np.float32)
        if sacar:
            alfa *= 1 - llama_1080
        rgb = cv2.cvtColor(cv2.resize(np.clip(img, 0, 255).astype(np.uint8), (1080, 1920),
                                      interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2RGB)
        Image.fromarray(np.dstack([rgb, alfa.astype(np.uint8)]), "RGBA").save(OCT / nombre)
        print("✓", nombre)

if __name__ == "__main__":
    main()
