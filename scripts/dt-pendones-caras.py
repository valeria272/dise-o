"""Pendones DT 0,8x3 m (28-09-2026): cambia SOLO la cara de las modelos de la sesión feb-2025.
Nano Banana Pro rehace un recorte cuadrado alrededor de la cara; acá se alinea al original,
se le iguala el desenfoque y se pega con una elipse difuminada. Todo lo demás es la foto real."""
import cv2, numpy as np
from PIL import Image

R = "raw/hilton/dt/pendones-2026/"
# foto: (recorte x0,y0,x1,y1 en el original, generada, elipse (cx,cy,rx,ry) en coords del recorte, sigma desenfoque)
CASOS = {
    297: ((426, 200, 1146, 920), "caras/nb-297.png", (360, 395, 150, 200), 0),
    173: ((350, 575, 670, 895), "caras/nb2-173.png", (160, 150, 70, 95), 0),
    80:  ((760, 0, 1460, 700), "caras/nb2-80.png", (370, 130, 250, 210), None),  # None = igualar
}

def nitidez(g):
    return cv2.Laplacian(g.astype(np.float64), cv2.CV_64F).var()

def componer(k):
    (x0, y0, x1, y1), gen_f, (cx, cy, rx, ry), sigma = CASOS[k]
    orig = np.asarray(Image.open(f"{R}originales/sesion_3-{k}.jpg").convert("RGB")).astype(np.float32)
    w, h = x1 - x0, y1 - y0
    crop = orig[y0:y1, x0:x1]
    gen = np.asarray(Image.open(R + gen_f).convert("RGB").resize((w, h), Image.LANCZOS)).astype(np.float32)
    # alinear: el modelo a veces corre el encuadre unos píxeles
    ga = cv2.cvtColor(crop.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
    gb = cv2.cvtColor(gen.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
    (dx, dy), _ = cv2.phaseCorrelate(ga, gb)
    M = np.float32([[1, 0, -dx], [0, 1, -dy]])
    gen = cv2.warpAffine(gen, M, (w, h), borderMode=cv2.BORDER_REFLECT)
    # igualar desenfoque (la galleta tiene la cara fuera de foco)
    if sigma is None:
        ref = nitidez(ga[:int(cy + ry), :]); best = (1e18, 0)
        for s in np.arange(0.5, 12, 0.5):
            b = cv2.GaussianBlur(gb, (0, 0), s)[:int(cy + ry), :]
            best = min(best, (abs(nitidez(b) - ref), s))
        sigma = best[1]
    if sigma:
        gen = cv2.GaussianBlur(gen, (0, 0), sigma)
    # igualar color medio dentro de la elipse contra el original
    m = np.zeros((h, w), np.float32)
    cv2.ellipse(m, (cx, cy), (rx, ry), 0, 0, 360, 1, -1)
    feather = max(rx, ry) * 0.18
    a = cv2.GaussianBlur(m, (0, 0), feather)[..., None]
    out = orig.copy()
    out[y0:y1, x0:x1] = gen * a + crop * (1 - a)
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(f"{R}final-{k}.png")
    print(k, f"desplazamiento ({dx:.1f},{dy:.1f}) px · desenfoque {sigma}")

if __name__ == "__main__":
    for k in CASOS:
        componer(k)


# ── Ronda 2 (Eli 28-09): «se siguen pareciendo» → pelo, piel, cejas y gafas también.
# Nano Banana Pro edita la foto ENTERA (acolchada a 3:4); acá se vuelve a la foto real
# en todo lo que el modelo no cambió, con una máscara por diferencia.
def componer_r2(k, umbral=14, pad=94):
    orig = np.asarray(Image.open(f"{R}final-{k}.png").convert("RGB")).astype(np.float32)
    H, W = orig.shape[:2]
    gen = Image.open(f"{R}caras/r2/nb-{k}.png").convert("RGB").resize((W + 2 * pad, H), Image.LANCZOS)
    gen = np.asarray(gen).astype(np.float32)[:, pad:pad + W]
    ga = cv2.cvtColor(orig.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
    gb = cv2.cvtColor(gen.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
    (dx, dy), _ = cv2.phaseCorrelate(ga, gb)
    gen = cv2.warpAffine(gen, np.float32([[1, 0, -dx], [0, 1, -dy]]), (W, H), borderMode=cv2.BORDER_REFLECT)
    la = cv2.cvtColor(orig.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
    lb = cv2.cvtColor(gen.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
    d = np.sqrt(((cv2.GaussianBlur(la, (0, 0), 3) - cv2.GaussianBlur(lb, (0, 0), 3)) ** 2).sum(2))
    m = (d > umbral).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((31, 31), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    keep = np.zeros_like(m)
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] > 0.002 * H * W:
            keep[lab == i] = 1
    cnts, _ = cv2.findContours(keep, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(keep, cnts, -1, 1, -1)
    keep = cv2.dilate(keep, np.ones((15, 15), np.uint8))
    a = cv2.GaussianBlur(keep.astype(np.float32), (0, 0), 8)[..., None]
    out = gen * a + orig * (1 - a)
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(f"{R}final2-{k}.png")
    Image.fromarray((a[..., 0] * 255).astype(np.uint8)).save(f"{R}caras/r2/mascara-{k}.png")
    print(k, f"desplazamiento ({dx:.1f},{dy:.1f}) · máscara {a.mean()*100:.1f} %")


# ── Ronda 3 (Eli 28-09): «se ve poco natural». Bata: pelo caramelo que le venga a la piel.
# Teléfono: pelirroja a los hombros, chaleco celeste, zapatos celestes. Galleta: todo el pelo rojo.
R3 = {297: "final2-297", "173a": "final-173", "173b": "final2-173", 80: "final2-80"}

def componer_r3(k, umbral=14, pad=94):
    import os
    base = f"{R}{R3[k]}.png"
    tmp = f"{R}caras/r2/_r3-{k}.png"
    # reutiliza componer_r2 cambiando las rutas de entrada y salida
    orig = np.asarray(Image.open(base).convert("RGB")).astype(np.float32)
    H, W = orig.shape[:2]
    gen = Image.open(f"{R}caras/r3/nb-{k}.png").convert("RGB").resize((W + 2 * pad, H), Image.LANCZOS)
    gen = np.asarray(gen).astype(np.float32)[:, pad:pad + W]
    ga = cv2.cvtColor(orig.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
    gb = cv2.cvtColor(gen.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
    (dx, dy), _ = cv2.phaseCorrelate(ga, gb)
    gen = cv2.warpAffine(gen, np.float32([[1, 0, -dx], [0, 1, -dy]]), (W, H), borderMode=cv2.BORDER_REFLECT)
    la = cv2.cvtColor(orig.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
    lb = cv2.cvtColor(gen.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
    d = np.sqrt(((cv2.GaussianBlur(la, (0, 0), 3) - cv2.GaussianBlur(lb, (0, 0), 3)) ** 2).sum(2))
    m = (d > umbral).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((31, 31), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    keep = np.zeros_like(m)
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] > 0.002 * H * W:
            keep[lab == i] = 1
    cnts, _ = cv2.findContours(keep, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(keep, cnts, -1, 1, -1)
    keep = cv2.dilate(keep, np.ones((15, 15), np.uint8))
    a = cv2.GaussianBlur(keep.astype(np.float32), (0, 0), 8)[..., None]
    out = gen * a + orig * (1 - a)
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(f"{R}final3-{k}.png")
    Image.fromarray((a[..., 0] * 255).astype(np.uint8)).save(f"{R}caras/r3/mascara-{k}.png")
    print(k, f"desplazamiento ({dx:.1f},{dy:.1f}) · máscara {a.mean()*100:.1f} %")
