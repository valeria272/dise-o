#!/usr/bin/env python3
"""Cola de generación — dispara TODOS los planos de una vez, no uno por uno.

    python3 scripts/cola.py enviar  gcl-agent/cap02/_plan.json
    python3 scripts/cola.py estado
    python3 scripts/cola.py esperar          # una sola espera para toda la cola
    python3 scripts/cola.py recoger

POR QUÉ EXISTE (06-09-2026). `scripts/magnific-video.py` manda UN trabajo y se
queda bloqueado hasta 15 minutos esperándolo (su `espera()`). Con 8 cortes eso
son 8 esperas en serie, una detrás de otra, y cada una se come un turno del
agente mirando el techo. Kling tarda 3–8 minutos por clip: en serie son ~45
minutos de reloj, en paralelo son ~8. La API acepta los trabajos de a uno pero
los procesa en paralelo — el cuello nunca fue Freepik, era nuestro.

Este script NO reimplementa el motor: importa `magnific-video.py` y usa sus
funciones. Todas las trampas de la API que están documentadas ahí (la ruta de
consulta que NO es la del POST, `image_tail` sólo en kling, el base64 reducido,
`negative_prompt` que devuelve 404) siguen viviendo en un solo lugar.

EL PLAN es un JSON con una entrada por plano:

    [
      {"id": "cut01",
       "imagen": "gcl-agent/cap02/keyframes/KF01.png",
       "fin":    "gcl-agent/cap02/keyframes/KF02.png",
       "prompt": "sólo su mano mueve el mouse, lento y decidido",
       "out":    "gcl-agent/cap02/clips/cut01.mp4",
       "dur": "5", "modelo": "kling-v2-1-pro", "coda": "fisica"}
    ]

`fin`, `dur`, `modelo` y `coda` son opcionales. `id` es el nombre del plano y es
lo que hace que reenviar sea seguro.

⚠️ REENVIAR NO REGENERA. Cada generación cuesta créditos, o sea plata. Si Freepik
ya aceptó un plano, `enviar` lo salta. Para rehacerlo de verdad hay que pedirlo:
`cola.py enviar plan.json --rehacer cut01`. Lo que SÍ se reintenta solo es el
plano que ni siquiera llegó a enviarse (sin saldo, red caída): eso no se pagó.

⚠️ EL PLAN SE VALIDA ANTES DE GASTAR. Si a un plano le falta el keyframe o pide
`fin` en un modelo que no lo acepta, no se manda NADA: se aborta la cola entera
y se avisa. Un typo no se paga con 8 clips malos.
"""
import argparse
import importlib.util
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

RAIZ = pathlib.Path(__file__).resolve().parent.parent
COLA_POR_DEFECTO = RAIZ / "out" / "_cola" / "cola.json"

# Estados que devuelve Freepik, traducidos a lo único que importa acá.
VIVOS = ("CREATED", "IN_PROGRESS", "PROCESSING", "PENDING")
TERMINALES_MAL = ("FAILED", "ERROR", "TIMEOUT")


def motor():
    """Carga `magnific-video.py` como módulo. Se hace acá y no arriba porque el
    motor importa `certifi` y PIL en el momento de importarse, y así `--help` y
    la validación del plan funcionan en una máquina sin el venv montado."""
    ruta = RAIZ / "scripts" / "magnific-video.py"
    spec = importlib.util.spec_from_file_location("magnific_video", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def pedir_suave(m, ruta, cuerpo=None):
    """Como `m.pedir()` pero NO mata el proceso cuando un trabajo falla.

    El motor hace `sys.exit()` ante un HTTP malo, que para un clip suelto está
    bien. Acá, en cambio, un plano caído no puede tumbar a los otros siete: se
    devuelve el error como dato y la cola sigue."""
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(
        m.BASE + ruta, data=datos, method="POST" if datos else "GET",
        headers={"x-freepik-api-key": m.clave(), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, context=m.CTX, timeout=180) as r:
            return json.loads(r.read()), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}: {e.read().decode()[:300]}"
    except Exception as e:                                   # red caída, DNS, TLS
        return None, f"{type(e).__name__}: {e}"


# ─────────────────────────────────────────────────────────── estado en disco ──
def ruta_real(p):
    """El plan puede escribir rutas relativas a la raíz del repo aunque el script
    se corra desde otra carpeta. Se prueban las dos y gana la que exista."""
    if os.path.isfile(p):
        return p
    return str(RAIZ / p)


def leer(ruta):
    if ruta.is_file():
        return json.loads(ruta.read_text())
    return {"trabajos": {}}


def escribir(ruta, cola):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(cola, indent=2, ensure_ascii=False))


# ──────────────────────────────────────────────────────────────── validación ──
def validar(plan):
    """Revisa el plan ENTERO antes de mandar nada. Devuelve la lista de fallas."""
    fallas, vistos = [], set()
    for i, t in enumerate(plan):
        d = f"plano #{i + 1}"
        tid = t.get("id")
        if not tid:
            fallas.append(f"{d}: le falta el campo `id`")
        elif tid in vistos:
            fallas.append(f"{d}: el id «{tid}» está repetido en el plan")
        else:
            vistos.add(tid)
            d = f"«{tid}»"
        for campo in ("imagen", "prompt", "out"):
            if not t.get(campo):
                fallas.append(f"{d}: le falta el campo `{campo}`")
        img = t.get("imagen")
        if img and not os.path.isfile(ruta_real(img)):
            fallas.append(f"{d}: no existe el keyframe {img}")
        fin, modelo = t.get("fin"), t.get("modelo", "kling-v2-1-pro")
        if fin:
            if not os.path.isfile(ruta_real(fin)):
                fallas.append(f"{d}: no existe el keyframe final {fin}")
            if not modelo.startswith("kling"):
                fallas.append(f"{d}: `fin` (image_tail) sólo lo aceptan los kling, "
                              f"y este pide {modelo}")
        dur = str(t.get("dur", "5"))
        if dur not in ("5", "10"):
            fallas.append(f"{d}: `dur` sólo puede ser 5 o 10, no {dur}")
    return fallas


# ───────────────────────────────────────────────────────────────────── enviar ──
def enviar(a):
    plan = json.loads(pathlib.Path(a.plan).read_text())
    if not isinstance(plan, list):
        sys.exit("✗ el plan tiene que ser una lista de planos")

    fallas = validar(plan)
    if fallas:
        print("✗ el plan no está sano — no se mandó NADA:", file=sys.stderr)
        for f in fallas:
            print(f"   · {f}", file=sys.stderr)
        sys.exit(1)

    cola = leer(a.cola)
    for tid in a.rehacer:
        if cola["trabajos"].pop(tid, None):
            print(f"↺ «{tid}» sacado de la cola — se va a regenerar (cuesta créditos)")

    m = motor()
    nuevos = saltados = 0
    for t in plan:
        tid = t["id"]
        ya = cola["trabajos"].get(tid)
        # Se salta lo que Freepik ACEPTÓ (tiene task_id): eso ya se pagó. Un plano
        # que murió antes de entrar —sin créditos, red caída— no costó nada y se
        # reintenta solo: cargas saldo, vuelves a correr `enviar` y sigue.
        if ya and ya.get("task_id"):
            saltados += 1
            continue
        if ya:
            print(f"↻ {tid} quedó en {ya['estado']} sin llegar a enviarse — se reintenta")
        modelo = t.get("modelo", "kling-v2-1-pro")
        coda = t.get("coda", "")
        cuerpo = {
            "image": m.a_base64(ruta_real(t["imagen"])),
            "prompt": t["prompt"] + ". " + (
                m.CODA_FISICA if coda == "fisica" else (coda or m.NEGATIVO_EN_EL_PROMPT)),
            "duration": str(t.get("dur", "5")),
        }
        if t.get("fin"):
            cuerpo["image_tail"] = m.a_base64(ruta_real(t["fin"]))
        r, err = pedir_suave(m, f"/image-to-video/{modelo}", cuerpo)
        if err:
            print(f"  ✗ {tid}: {err}")
            cola["trabajos"][tid] = {"estado": "ERROR", "error": err, "out": t["out"]}
            continue
        cola["trabajos"][tid] = {
            "estado": "CREATED",
            "task_id": r["data"]["task_id"],
            "consulta": m.ruta_consulta(modelo),
            "modelo": modelo,
            "out": t["out"],
            "enviado": time.strftime("%Y-%m-%d %H:%M:%S"),
            "error": None,
        }
        nuevos += 1
        print(f"  → {tid} enviado  ({modelo}, {cuerpo['duration']}s)")
        escribir(a.cola, cola)                    # se guarda de a uno: si se corta

    escribir(a.cola, cola)                        # la luz, no se pierde ningún id
    print(f"\n{nuevos} enviados · {saltados} ya estaban en la cola · {a.cola}")
    if nuevos:
        print("Ahora: `cola.py esperar` (una sola espera para todos) o `cola.py estado`")


# ───────────────────────────────────────────────────────── consultar y bajar ──
def refrescar(m, cola):
    """Una pasada de consulta sobre todo lo que sigue vivo. Devuelve qué cambió."""
    cambios = []
    for tid, t in cola["trabajos"].items():
        if t["estado"] not in VIVOS:
            continue
        r, err = pedir_suave(m, f"{t['consulta']}/{t['task_id']}")
        if err:
            # Un fallo de red al CONSULTAR no mata el trabajo: sigue vivo allá.
            cambios.append((tid, t["estado"], f"sin respuesta ({err[:40]})"))
            continue
        d = r.get("data", {})
        estado = d.get("status", "?")
        if estado != t["estado"]:
            cambios.append((tid, t["estado"], estado))
        t["estado"] = estado
        if estado == "COMPLETED":
            t["urls"] = d.get("generated") or []
        elif estado in TERMINALES_MAL:
            t["error"] = json.dumps(d)[:300]
    return cambios


def bajar(m, cola):
    """Descarga lo que esté COMPLETED y todavía no esté en disco."""
    bajados = 0
    for tid, t in cola["trabajos"].items():
        if t["estado"] != "COMPLETED" or t.get("descargado"):
            continue
        if not t.get("urls"):
            print(f"  ✗ {tid}: terminó pero no devolvió video")
            continue
        try:
            m.guarda(t["urls"], t["out"])
            t["descargado"] = True
            bajados += 1
        except Exception as e:
            print(f"  ✗ {tid}: no se pudo bajar — {type(e).__name__}: {e}")
    return bajados


def tabla(cola):
    if not cola["trabajos"]:
        print("La cola está vacía.")
        return
    ancho = max(len(k) for k in cola["trabajos"])
    for tid, t in cola["trabajos"].items():
        marca = {"COMPLETED": "✓", "CREATED": "…", "IN_PROGRESS": "…"}.get(t["estado"], "✗")
        extra = "  (bajado)" if t.get("descargado") else ""
        if t["estado"] in TERMINALES_MAL and t.get("error"):
            extra = f"  {t['error'][:70]}"
        print(f"  {marca} {tid.ljust(ancho)}  {t['estado']}{extra}")
    vivos = sum(1 for t in cola["trabajos"].values() if t["estado"] in VIVOS)
    listos = sum(1 for t in cola["trabajos"].values() if t.get("descargado"))
    print(f"\n{listos} en disco · {vivos} generando · {len(cola['trabajos'])} en total")


def estado(a):
    cola = leer(a.cola)
    if cola["trabajos"]:
        m = motor()
        refrescar(m, cola)
        if a.bajar:
            bajar(m, cola)
        escribir(a.cola, cola)
    tabla(cola)


def esperar(a):
    """LA función que justifica el script: UNA espera para toda la cola."""
    cola = leer(a.cola)
    if not cola["trabajos"]:
        sys.exit("✗ la cola está vacía — corre `cola.py enviar <plan.json>` primero")
    m = motor()
    limite = time.time() + a.minutos * 60
    while time.time() < limite:
        for tid, viejo, nuevo in refrescar(m, cola):
            print(f"  · {tid}: {viejo} → {nuevo}")
        bajar(m, cola)
        escribir(a.cola, cola)
        if not any(t["estado"] in VIVOS for t in cola["trabajos"].values()):
            print()
            tabla(cola)
            malos = [k for k, t in cola["trabajos"].items()
                     if t["estado"] in TERMINALES_MAL]
            return 1 if malos else 0
        time.sleep(a.cada)
    print(f"\n⏱ se acabaron los {a.minutos} min de espera. Lo que quedó:")
    tabla(cola)
    print("Los trabajos siguen vivos en Freepik: `cola.py esperar` los retoma.")
    return 1


def recoger(a):
    cola = leer(a.cola)
    m = motor()
    refrescar(m, cola)
    n = bajar(m, cola)
    escribir(a.cola, cola)
    print(f"\n{n} clips bajados en esta pasada.")
    tabla(cola)


def main():
    ap = argparse.ArgumentParser(
        description="Cola de generación de video — todos los planos a la vez.")
    ap.add_argument("--cola", type=pathlib.Path, default=COLA_POR_DEFECTO,
                    help="archivo de estado. Uno por pieza si corres varias a la vez")
    sub = ap.add_subparsers(dest="cmd", required=True)

    e = sub.add_parser("enviar", help="manda todos los planos del plan")
    e.add_argument("plan")
    e.add_argument("--rehacer", nargs="*", default=[],
                   help="ids que SÍ se regeneran aunque ya estén en la cola (gasta créditos)")
    e.set_defaults(fn=enviar)

    s = sub.add_parser("estado", help="una consulta, sin bloquear")
    s.add_argument("--bajar", action="store_true", help="baja de paso lo que ya esté listo")
    s.set_defaults(fn=estado)

    w = sub.add_parser("esperar", help="espera UNA vez a que termine toda la cola")
    w.add_argument("--minutos", type=int, default=25)
    w.add_argument("--cada", type=int, default=20, help="segundos entre consultas")
    w.set_defaults(fn=esperar)

    r = sub.add_parser("recoger", help="baja lo que haya terminado")
    r.set_defaults(fn=recoger)

    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
