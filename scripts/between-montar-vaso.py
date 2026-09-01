#!/usr/bin/env python3
"""
Monta el vaso To Go REAL sobre una escena, haciéndolo pasar por parte de la foto.

Por qué
-------
Ronda 5 (31-08-2026). Primero el cliente rechazó el logotipo estampado sobre un
vaso generado con IA; se resolvió recortando el vaso real de la sesión del
cliente (`togo-vaso-real-nobg.png`, del frame `Double Tree 25 jul 25-255`).
Pero pegar el recorte tal cual **seguía leyéndose como un montaje**:

    «Se ve un montaje muy raro el vaso pegado en la foto»

Medido, las tres causas eran objetivas:

1. **Nitidez.** El recorte marcaba 2095 de varianza del laplaciano y la escena
   13,5: unas **150 veces más nítido**. Un objeto perfectamente enfocado sobre
   un fondo desenfocado se lee como pegatina, siempre.
2. **Dirección de la luz.** En la escena la luz entra por la IZQUIERDA (mesa
   izquierda 230, derecha 184). En el recorte entra por la DERECHA (cartón
   izquierdo 145, derecho 170). El vaso venía iluminado al revés que su fondo.
3. **Sin sombra de contacto.** Sin sombra, un objeto flota aunque todo lo demás
   esté bien.

⛔ **El vaso NO se puede espejar** para arreglar la luz: invertiría el logotipo,
que es justo lo que costó la ronda 4. Se re-ilumina con un degradado lateral.

Qué hace
--------
  1. Escala el recorte y le **invierte el degradado lateral** para que la luz
     caiga del mismo lado que en la escena.
  2. Iguala su **nivel y su temperatura** a los de la escena.
  3. Lo **desenfoca hasta la nitidez de la escena**, medida en las dos.
  4. Le dibuja una **sombra de contacto** elíptica, corrida al lado contrario
     de la luz y más densa junto a la base.

Uso:
    python3 scripts/between-montar-vaso.py <escena> <salida> \
        --centro CX --piso Y --ancho W \
        [--luz izquierda|derecha]   # de dónde viene la luz EN LA ESCENA
        [--desenfoque auto|N]
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
VASO = RAIZ / 'public/assets/hilton/between/togo-vaso-real-nobg.png'


def nitidez(gris):
    """Varianza del laplaciano: cuánto detalle fino tiene una zona."""
    g = gris.astype(np.float64)
    lap = g[1:-1, 1:-1]*4 - g[:-2, 1:-1] - g[2:, 1:-1] - g[1:-1, :-2] - g[1:-1, 2:]
    return float(np.var(lap))


def lado_luz(rgb, mascara):
    """Por qué lado entra la luz, mirando el tercio izquierdo contra el derecho."""
    ys, xs = np.where(mascara)
    if not len(xs): return 'izquierda'
    x0, x1 = xs.min(), xs.max(); t = max((x1 - x0)//3, 1)
    col = np.arange(mascara.shape[1])[None, :]
    izq = rgb[mascara & (col < x0 + t)].mean()
    der = rgb[mascara & (col > x1 - t)].mean()
    return 'izquierda' if izq > der else 'derecha'


def montar(escena, salida, cx, piso, ancho, luz, desenfoque, sombra):
    esc = Image.open(escena).convert('RGB')
    E = np.asarray(esc).astype(np.float64)
    vaso = Image.open(VASO).convert('RGBA')

    v = vaso.resize((ancho, int(round(vaso.height * ancho / vaso.width))), Image.LANCZOS)
    a = np.asarray(v).astype(np.float64).copy()
    alfa = a[:, :, 3] / 255.0
    solido = alfa > 0.78
    h, w = a.shape[:2]
    x0, y0 = cx - w // 2, piso - h

    # ── 1. re-iluminar: invertir el degradado lateral si hace falta ──────────
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    kraft = solido & (R > B + 22) & ((.299*R + .587*G + .114*B) > 60)
    luz_vaso = lado_luz(a[..., :3].mean(2), kraft)
    if luz_vaso != luz:
        t = np.linspace(0, 1, w)[None, :]          # 0 izquierda · 1 derecha
        if luz == 'izquierda':
            g = 1.0 + 0.20 - 0.40 * t              # aclara izquierda, oscurece derecha
        else:
            g = 1.0 - 0.20 + 0.40 * t
        a[:, :, :3] *= g[..., None]

    # ── 2. igualar nivel y temperatura a la escena ──────────────────────────
    zona = E[max(y0, 0):y0 + h, max(x0, 0):x0 + w]
    if zona.size:
        objetivo = np.percentile(zona.reshape(-1, 3), 62, axis=0)
        actual = a[..., :3][kraft].mean(0) if kraft.any() else a[..., :3].mean((0, 1))
        a[:, :, :3] += (objetivo - actual) * 0.55

    # ── 3. desenfocar hasta la nitidez de la escena ─────────────────────────
    if desenfoque == 'auto':
        n_esc = nitidez(zona.mean(2)) if zona.size else 20.0
        r = 0.6
        for _ in range(28):
            prueba = np.asarray(Image.fromarray(np.clip(a[:, :, :3], 0, 255).astype(np.uint8))
                                .filter(ImageFilter.GaussianBlur(r))).astype(np.float64)
            if nitidez(prueba[solido].reshape(-1) if False else prueba.mean(2)) <= max(n_esc, 8):
                break
            r += 0.35
        radio = round(r, 2)
    else:
        radio = float(desenfoque)

    rgb = Image.fromarray(np.clip(a[:, :, :3], 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(radio))
    al = Image.fromarray((alfa * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(max(radio * 0.55, 0.8)))
    v2 = Image.merge('RGBA', (*rgb.split(), al))
    print(f'luz escena {luz} · luz recorte {luz_vaso} · desenfoque {radio} px')

    # ── 4. sombra de contacto ───────────────────────────────────────────────
    capa = Image.new('RGBA', esc.size, (0, 0, 0, 0))
    if sombra > 0:
        base_w = int(w * 0.62); base_h = int(h * 0.085)
        desp = int(w * 0.14) * (1 if luz == 'izquierda' else -1)
        s = Image.new('L', esc.size, 0)
        ImageDraw.Draw(s).ellipse(
            (cx - base_w//2 + desp, piso - base_h//2 - int(h*0.012),
             cx + base_w//2 + desp, piso + base_h//2 + int(h*0.012)), fill=255)
        s = s.filter(ImageFilter.GaussianBlur(w * 0.045))
        sombra_col = Image.new('RGBA', esc.size, (26, 16, 8, 255))
        sombra_col.putalpha(s.point(lambda p: int(p * sombra)))
        capa = Image.alpha_composite(capa, sombra_col)

    capa.paste(v2, (x0, y0), v2)
    fuera = Image.alpha_composite(esc.convert('RGBA'), capa).convert('RGB')
    Path(salida).parent.mkdir(parents=True, exist_ok=True)
    fuera.save(salida, quality=95)
    print(f'{salida}  vaso {w}x{h} en ({x0},{y0})')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('escena'); ap.add_argument('salida')
    ap.add_argument('--centro', type=int, required=True)
    ap.add_argument('--piso', type=int, required=True)
    ap.add_argument('--ancho', type=int, required=True)
    ap.add_argument('--luz', choices=('izquierda', 'derecha'), default='izquierda')
    ap.add_argument('--desenfoque', default='auto')
    ap.add_argument('--sombra', type=float, default=0.55)
    g = ap.parse_args()
    montar(g.escena, g.salida, g.centro, g.piso, g.ancho, g.luz, g.desenfoque, g.sombra)


if __name__ == '__main__':
    main()
