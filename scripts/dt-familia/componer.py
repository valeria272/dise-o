"""Pega a la familia generada sobre la foto REAL de DT (regla de Eli 25-09: fondo real siempre).
La máscara sale de la diferencia generada vs. real: se queda con las regiones grandes (personas
+ sombras + la ropa de cama que tocan) y el resto de píxeles vuelve a ser la foto original."""
import sys, cv2, numpy as np
from PIL import Image
R = "raw/hilton/dt/familia/r2/"
def componer(k, umbral=30):
    g = cv2.cvtColor(np.asarray(Image.open(f"{R}nb-{k}.png").convert("RGB")), cv2.COLOR_RGB2LAB).astype(float)
    H, W = g.shape[:2]
    real = np.asarray(Image.open(f"{R}fondos/{k}.jpg").convert("RGB").resize((W, H), Image.LANCZOS))
    r = cv2.cvtColor(real, cv2.COLOR_RGB2LAB).astype(float)
    d = np.sqrt(((cv2.GaussianBlur(g,(0,0),3) - cv2.GaussianBlur(r,(0,0),3))**2).sum(2))
    m = (d > umbral).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((9,9),np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((41,41),np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    keep = np.zeros_like(m)
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] > 0.004*H*W: keep[lab == i] = 1
    keep = cv2.dilate(keep, np.ones((31,31),np.uint8))
    # rellenar huecos interiores
    cnts,_ = cv2.findContours(keep, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(keep, cnts, -1, 1, -1)
    a = cv2.GaussianBlur(keep.astype(float), (0,0), 14)[..., None]
    gen = np.asarray(Image.open(f"{R}nb-{k}.png").convert("RGB")).astype(float)
    out = gen*a + real.astype(float)*(1-a)
    Image.fromarray(out.clip(0,255).astype(np.uint8)).save(f"{R}final-{k}.jpg", quality=94)
    Image.fromarray((a[...,0]*255).astype(np.uint8)).save(f"{R}mascara-{k}.png")
    print(k, "máscara cubre", round(a.mean()*100,1), "% del cuadro")
for k in sys.argv[1:]: componer(k)
