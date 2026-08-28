#!/usr/bin/env python3
"""Magnific / Freepik desde la línea de comandos — generar, escalar, reiluminar.

    python3 scripts/magnific.py generar   "<prompt>" --out ruta.png [--aspecto reel|feed|story|wide]
    python3 scripts/magnific.py pro       "<prompt>" --out ruta.png [--resolucion 4K] [--refs a.png b.png]
                                          ↑ Nano Banana Pro: el único que escribe TEXTO legible
    python3 scripts/magnific.py escalar   entrada.png --out salida.png [--precision] [--escala 2x|4x]
    python3 scripts/magnific.py reiluminar entrada.png --out salida.png --prompt "<luz que quieres>"
    python3 scripts/magnific.py estilo    entrada.png --ref referencia.png --out salida.png
    python3 scripts/magnific.py loras                          ← estilos entrenados de la cuenta
    python3 scripts/magnific.py tareas                         ← qué se generó últimamente

Magnific es Freepik: Freepik lo compró y todo pasa por `api.freepik.com`. No hay un
endpoint "magnific.com" aparte. La clave sale de `~/.magnific_key` o de
`FREEPIK_API_KEY` en el .env compartido — las dos sirven.

⚠️ Lo que esta API NO hace: leer tus PROYECTOS del sitio web de Magnific
(ABAKOS, BETWEEN, Copywriters, QB…). Eso vive en tu cuenta del navegador. Lo que
generes ahí se baja a mano y se guarda en `raw/<marca>/` o `public/assets/<marca>/`.
Lo que generes con este script sí queda en el repo desde el principio.

Recuerda la jerarquía de `docs/SISTEMA-DE-MARCAS.md` §2: la IA hace **ambiente y
fondo**. Nunca el producto, nunca el logo, nunca un dato.
"""
import argparse
import base64
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import certifi

BASE = "https://api.freepik.com"
CTX = ssl.create_default_context(cafile=certifi.where())

# Nano Banana Pro usa la notación corta; Mystic usa nombres largos. No son
# intercambiables: pasarle "square_1_1" a `pro` devuelve 400.
ASPECTOS_PRO = {
    "reel": "9:16", "story": "9:16", "feed": "1:1", "post": "3:4", "wide": "16:9",
}

ASPECTOS = {
    "reel":   "social_story_9_16",
    "story":  "social_story_9_16",
    "feed":   "square_1_1",
    "post":   "traditional_3_4",
    "wide":   "widescreen_16_9",
}


def clave():
    f = Path.home() / ".magnific_key"
    if f.is_file():
        k = f.read_text().strip()
        if k:
            return k
    env = Path(__file__).resolve().parent.parent.parent / "ASISTENTE PERSONAL" / ".env"
    if env.is_file():
        for l in env.read_text().splitlines():
            if l.startswith("FREEPIK_API_KEY="):
                return l.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("✗ No encuentro la clave. Debe estar en ~/.magnific_key o como\n"
             "  FREEPIK_API_KEY en 'ASISTENTE PERSONAL/.env'")


def pedir(ruta, cuerpo=None, metodo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(
        BASE + ruta, data=datos, method=metodo or ("POST" if datos else "GET"),
        headers={"x-freepik-api-key": clave(), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=120) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        cuerpo_err = e.read().decode(errors="ignore")[:400]
        sys.exit(f"✗ HTTP {e.code} en {ruta}\n  {cuerpo_err}")


def b64_de(ruta):
    return base64.b64encode(Path(ruta).read_bytes()).decode()


def espera(ruta_tarea, task_id, minutos=8):
    """Sondea hasta que la tarea termina. Devuelve la lista de URLs generadas."""
    limite = time.time() + minutos * 60
    espera_s = 3
    while time.time() < limite:
        r = pedir(f"{ruta_tarea}/{task_id}")
        d = r.get("data", r)
        estado = (d.get("status") or "").upper()
        if estado in ("COMPLETED", "SUCCESS"):
            return d.get("generated") or d.get("result") or []
        if estado in ("FAILED", "ERROR"):
            sys.exit(f"✗ La tarea falló: {json.dumps(d)[:300]}")
        print(f"  … {estado or 'EN PROCESO'}", flush=True)
        time.sleep(espera_s)
        espera_s = min(espera_s + 2, 15)
    sys.exit("✗ Se acabó el tiempo de espera. Revisa con:  magnific.py tareas")


def guarda(urls, destino):
    if not urls:
        sys.exit("✗ La tarea terminó sin entregar imagen")
    destino = Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    for i, u in enumerate(urls):
        salida = destino if i == 0 else destino.with_stem(destino.stem + f"_{i+1}")
        if isinstance(u, dict):
            u = u.get("url") or u.get("base64") or ""
        if u.startswith("http"):
            with urllib.request.urlopen(u, context=CTX, timeout=180) as r:
                salida.write_bytes(r.read())
        else:
            salida.write_bytes(base64.b64decode(u))
        kb = salida.stat().st_size // 1024
        print(f"  ✓ {salida}  ({kb} KB)")
    print("\n  MÍRALA antes de usarla:")
    print(f"  python3 scripts/ver-pieza.py {destino}")


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("accion", choices=["generar", "pro", "escalar", "reiluminar",
                                       "estilo", "loras", "tareas", "check"])
    ap.add_argument("entrada", nargs="?", help="prompt (generar) o archivo (el resto)")
    ap.add_argument("--out")
    ap.add_argument("--aspecto", default="feed", choices=list(ASPECTOS))
    ap.add_argument("--prompt", default="")
    ap.add_argument("--ref", help="imagen de referencia para 'estilo'")
    ap.add_argument("--precision", action="store_true", help="upscaler de precisión")
    ap.add_argument("--escala", default="2x")
    ap.add_argument("--resolucion", default="2K", choices=["1K", "2K", "4K"],
                    help="solo para 'pro'")
    ap.add_argument("--refs", nargs="*", default=[],
                    help="hasta 14 imágenes de referencia para 'pro'")
    ap.add_argument("--lora", help="id de un LoRA de la cuenta")
    a = ap.parse_args()

    if a.accion == "check":
        # Verifica la clave SIN gastar créditos: un GET de listado autentica pero no
        # genera nada. Existe porque un diseñador perdió un día entero sin saber si
        # su problema era la clave, el conector o la herramienta equivocada.
        req = urllib.request.Request(
            BASE + "/v1/ai/mystic", headers={"x-freepik-api-key": clave()})
        try:
            with urllib.request.urlopen(req, context=CTX, timeout=30):
                pass
            print("✓ Clave de Magnific/Freepik VÁLIDA — ya puedes generar imágenes.")
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                sys.exit(f"✗ Clave INVÁLIDA o vencida (HTTP {e.code}). Revisa "
                         f"~/.magnific_key:\n  no debe tener espacios ni comillas, "
                         f"solo la clave.")
            print(f"? Freepik respondió HTTP {e.code} — la clave autentica, "
                  f"pero el servicio devolvió algo raro. Reintenta en unos minutos.")
        return 0

    if a.accion == "loras":
        print(json.dumps(pedir("/v1/ai/loras"), ensure_ascii=False, indent=2)[:4000])
        return 0

    if a.accion == "tareas":
        r = pedir("/v1/ai/mystic")
        for t in (r.get("data") or [])[:25]:
            print(f"  {t.get('status','?'):12} {t.get('task_id','')}")
        return 0

    if not a.out:
        sys.exit("✗ Falta --out (dónde guardar el resultado)")

    if a.accion == "pro":
        # Nano Banana Pro (Gemini 3 Pro Image). Es el que hay que usar cuando la
        # pieza necesita TEXTO LEGIBLE dentro de la imagen o control fino de
        # composición: Mystic escribe letras rotas. Verificado el 28-08-2026 —
        # está incluido en el plan actual, no hay que pagar nada aparte.
        # OJO: la ruta va anidada bajo text-to-image/, no suelta como Mystic.
        if not a.entrada:
            sys.exit("✗ Falta el prompt")
        ruta = "/v1/ai/text-to-image/nano-banana-pro"
        cuerpo = {"prompt": a.entrada, "aspect_ratio": ASPECTOS_PRO[a.aspecto],
                  "resolution": a.resolucion}
        if a.refs:
            cuerpo["reference_images"] = [b64_de(r) for r in a.refs[:14]]
        print(f"→ Nano Banana Pro · {a.aspecto} · {a.resolucion}"
              + (f" · {len(a.refs[:14])} referencias" if a.refs else ""))
        r = pedir(ruta, cuerpo)
        guarda(espera(ruta, r["data"]["task_id"]), a.out)
        return 0

    if a.accion == "generar":
        if not a.entrada:
            sys.exit("✗ Falta el prompt")
        cuerpo = {"prompt": a.entrada, "aspect_ratio": ASPECTOS[a.aspecto],
                  "model": "realism", "creative_detailing": 33}
        if a.lora:
            cuerpo["lora"] = a.lora
        print(f"→ Mystic · {a.aspecto} ({ASPECTOS[a.aspecto]})")
        r = pedir("/v1/ai/mystic", cuerpo)
        guarda(espera("/v1/ai/mystic", r["data"]["task_id"]), a.out)
        return 0

    if not a.entrada or not Path(a.entrada).is_file():
        sys.exit(f"✗ No encuentro el archivo: {a.entrada}")

    if a.accion == "escalar":
        ruta = "/v1/ai/image-upscaler-precision" if a.precision else "/v1/ai/image-upscaler"
        cuerpo = {"image": b64_de(a.entrada)}
        if not a.precision:
            cuerpo["scale_factor"] = a.escala
        print(f"→ Magnific {'Precision' if a.precision else 'Upscaler'} · {a.escala}")
        r = pedir(ruta, cuerpo)
        guarda(espera(ruta, r["data"]["task_id"]), a.out)
        return 0

    if a.accion == "reiluminar":
        cuerpo = {"image": b64_de(a.entrada), "prompt": a.prompt or "natural daylight"}
        print("→ Magnific Relight")
        r = pedir("/v1/ai/image-relight", cuerpo)
        guarda(espera("/v1/ai/image-relight", r["data"]["task_id"]), a.out)
        return 0

    if a.accion == "estilo":
        if not a.ref:
            sys.exit("✗ Falta --ref (la imagen cuyo estilo quieres copiar)")
        cuerpo = {"image": b64_de(a.entrada), "reference_image": b64_de(a.ref)}
        if a.prompt:
            cuerpo["prompt"] = a.prompt
        print("→ Transferencia de estilo")
        r = pedir("/v1/ai/image-style-transfer", cuerpo)
        guarda(espera("/v1/ai/image-style-transfer", r["data"]["task_id"]), a.out)
        return 0


if __name__ == "__main__":
    sys.exit(main())
