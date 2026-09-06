#!/usr/bin/env python3
"""La mesa — el ida y vuelta con ChatGPT, sin que nadie tenga que redactar.

    python3 scripts/mesa.py parte cap02     # arma lo que le arrastras a GPT
    python3 scripts/mesa.py plan  cap02     # traduce lo que GPT contestó

El contrato completo está en `mesa/CONTRATO.md`. Léelo antes que este archivo.

POR QUÉ EXISTE (06-09-2026). El puente entre la dirección (GPT) y la producción
(Claude) era Valeria redactando en las dos direcciones, y el que traduce decide.
Acá GPT recibe hechos —qué se generó, con qué modelo, cómo se ve— y devuelve
dirección en un formato fijo que se ejecuta sin interpretar.

⚠️ ESTE SCRIPT NO PIENSA POR NADIE. `plan` arma un plan BORRADOR: mete la
corrección de GPT en el prompt tal como llegó. La redacción del prompt —que es
donde se gana o se pierde un plano— sigue siendo trabajo de Claude y tuyo. El
script se encarga de lo aburrido: que no falte nada, que no se gaste de más y
que nadie tenga que copiar rutas a mano.
"""
import argparse
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
MESA = RAIZ / "mesa"
VEREDICTOS = ("APROBADO", "AJUSTAR", "REHACER")

try:                                    # Windows: la consola decodifica en cp1252
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


# ──────────────────────────────────────────────────────────────────── PARTE ──
def duracion(clip):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(clip)],
        capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def fotogramas(clip, destino, tid):
    """Tres fotogramas por plano: entrada, medio y salida. Con esos tres GPT ve
    si el personaje derivó, que es el fallo que más se repite (candado 4)."""
    d = duracion(clip)
    if d <= 0:
        return []
    sacados = []
    for etiqueta, t in (("1-entra", 0.1), ("2-medio", d / 2), ("3-sale", max(d - 0.15, 0))):
        out = destino / f"{tid}_{etiqueta}.jpg"
        r = subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.2f}",
             "-i", str(clip), "-frames:v", "1", "-q:v", "3", str(out)],
            capture_output=True)
        if r.returncode == 0 and out.is_file():
            sacados.append(out)
    return sacados


def parte(a):
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        sys.exit("✗ hace falta ffmpeg (y ffprobe) para sacar los fotogramas.\n"
                 "  macOS:  brew install ffmpeg")

    plan = json.loads(pathlib.Path(a.plan).read_text()) if a.plan else []
    cola = json.loads(pathlib.Path(a.cola).read_text())["trabajos"] if \
        pathlib.Path(a.cola).is_file() else {}
    if not plan and not cola:
        sys.exit(f"✗ no encuentro ni el plan ni la cola. Pásalos con --plan / --cola")

    por_id = {t["id"]: t for t in plan}
    ids = list(dict.fromkeys(list(por_id) + list(cola)))

    destino = MESA / "salida" / a.pieza
    fotos = destino / "fotogramas"
    if fotos.exists():
        shutil.rmtree(fotos)
    fotos.mkdir(parents=True)

    filas, faltantes, sin_clip = [], [], []
    for tid in ids:
        t, c = por_id.get(tid, {}), cola.get(tid, {})
        clip = pathlib.Path(c.get("out") or t.get("out", ""))
        if clip and not clip.is_absolute():
            clip = RAIZ / clip
        estado = c.get("estado", "SIN ENVIAR")
        if clip and clip.is_file():
            n = len(fotogramas(clip, fotos, tid))
            if not n:
                sin_clip.append(f"{tid} (el archivo existe pero ffmpeg no lo leyó)")
        else:
            sin_clip.append(f"{tid} ({estado})")
        if estado in ("FAILED", "ERROR", "TIMEOUT"):
            faltantes.append(f"**{tid}** — {estado}: {(c.get('error') or '')[:160]}")
        filas.append((tid, estado, c.get("modelo", t.get("modelo", "—")),
                      str(t.get("dur", "5")) + "s",
                      "sí" if t.get("fin") else "no",
                      (t.get("prompt", "") or "")[:90]))

    # La hoja de contacto la arma el script que ya existe — no se duplica.
    # 3 columnas = una fila por plano: entrada · medio · salida, en ese orden.
    hoja = destino / "hoja-contacto.png"
    r = subprocess.run([sys.executable, str(RAIZ / "scripts" / "hoja-contacto.py"),
                        str(fotos), str(hoja), "3"], capture_output=True, text=True)
    if r.returncode != 0 or not hoja.is_file():
        print("⚠ no se pudo armar la hoja de contacto — el parte igual queda escrito.")
        print("  " + (r.stderr.strip().splitlines() or ["sin detalle"])[-1])
        hoja = None

    # ⚠️ El fence se busca anclado a principio de línea. El contrato menciona
    # ```json DENTRO de una frase para explicárselo a GPT, y partir por la
    # primera aparición suelta traía esa frase en vez del esquema.
    contrato = (MESA / "CONTRATO.md").read_text()
    m = re.search(r"^```json\n(.+?)^```", contrato, re.S | re.M)
    if not m:
        sys.exit("✗ mesa/CONTRATO.md perdió el bloque ```json con el esquema. "
                 "Sin eso el parte no le puede decir a GPT cómo contestar.")
    esquema = m.group(1)

    doc = [f"# Parte de producción — {a.pieza}", ""]
    doc += [f"Ronda {a.ronda} · {len(filas)} planos · generado por `scripts/mesa.py`.", ""]
    doc += ["## Qué se generó", "",
            "| Plano | Estado | Modelo | Dur | Frame final | Prompt que se mandó |",
            "|---|---|---|---|---|---|"]
    doc += [f"| {i} | {es} | {mo} | {du} | {fi} | {pr} |"
        for i, es, mo, du, fi, pr in filas]
    doc += [""]
    if faltantes:
        doc += ["## Lo que falló", ""] + [f"- {x}" for x in faltantes] + [""]
    if sin_clip:
        doc += ["## Planos sin fotograma en la hoja", "",
                "No están en la hoja de contacto, así que no los juzgues:", ""]
        doc += [f"- {x}" for x in sin_clip] + [""]
    doc += ["## Lo que necesito que decidas", "",
            "<!-- Claude: acá van las preguntas reales de esta ronda, una por línea.",
            "     Si no hay ninguna, borra esta sección entera. -->", ""]
    doc += ["---", "",
            "## Cómo contestar este parte", "",
            "Mira la hoja de contacto adjunta (`hoja-contacto.png`): son tres",
            "fotogramas por plano — entrada, medio y salida. Contesta **con un solo",
            "bloque ```json** en este formato y nada más:", "",
            "```json", esquema.rstrip(), "```", "",
            "`presupuesto` es cuántas regeneraciones autorizas esta ronda: cada una",
            "cuesta créditos. `no_se_toca` es lo que ya está aprobado y no se",
            "rediscute.", "",
            "⚠️ **No juzgues ritmo ni duración de los cortes desde estos fotogramas** —",
            "no se ve el movimiento. El montaje se decide con el timeline, no acá."]

    salida = destino / "parte.md"
    salida.write_text("\n".join(doc) + "\n")
    print(f"\n✓ {corta(salida)}")
    if hoja:
        print(f"✓ {corta(hoja)}")
    print("\nArrastra ESOS DOS al chat de ChatGPT. Su respuesta se guarda en")
    print(f"   mesa/entrada/{a.pieza}-ronda{a.ronda + 1}.md")


# ───────────────────────────────────────────────────────────────────── PLAN ──
def extraer_json(texto):
    m = re.search(r"```json\s*(.+?)```", texto, re.S)
    crudo = m.group(1) if m else texto
    try:
        return json.loads(crudo)
    except json.JSONDecodeError as e:
        sys.exit(f"✗ lo que contestó GPT no es JSON válido: {e}\n"
                 f"  Pídele que lo repita como UN bloque ```json, sin texto alrededor.")


def ultima_entrada(pieza):
    ent = sorted((MESA / "entrada").glob(f"{pieza}-ronda*.md"),
                 key=lambda p: int(re.search(r"ronda(\d+)", p.name).group(1)))
    if not ent:
        sys.exit(f"✗ no hay ninguna respuesta de GPT en mesa/entrada/{pieza}-ronda*.md")
    return ent[-1]


def corta(p):
    """La ruta relativa a la raíz si está adentro; si no, tal cual. `--entrada`
    puede apuntar a cualquier parte y `relative_to` revienta con eso."""
    try:
        return str(pathlib.Path(p).relative_to(RAIZ))
    except ValueError:
        return str(p)


def plan(a):
    entrada = pathlib.Path(a.entrada) if a.entrada else ultima_entrada(a.pieza)
    if not entrada.is_file():
        sys.exit(f"✗ no existe {entrada}")
    d = extraer_json(entrada.read_text())
    print(f"→ {corta(entrada)}  ·  ronda {d.get('ronda', '?')}")

    planos = d.get("planos") or []
    malos = [p for p in planos if p.get("veredicto") not in VEREDICTOS]
    if malos:
        sys.exit("✗ hay veredictos que no existen: "
                 + ", ".join(f"{p.get('id')}={p.get('veredicto')}" for p in malos)
                 + f"\n  Sólo valen: {', '.join(VEREDICTOS)}")

    presupuesto = d.get("presupuesto")
    if presupuesto is None:
        sys.exit("✗ la respuesta no trae `presupuesto`. Sin tope de gasto no se "
                 "arma el plan — pídeselo a GPT.")

    tocan = [p for p in planos if p["veredicto"] in ("AJUSTAR", "REHACER")]
    # `--solo` se aplica ANTES de mirar el presupuesto: es justamente la salida
    # cuando GPT pidió más de lo autorizado y tú elegiste con cuáles quedarte.
    if a.solo:
        fuera = [i for i in a.solo if i not in [p["id"] for p in tocan]]
        if fuera:
            print(f"⚠ --solo nombra planos que GPT no pidió tocar: {', '.join(fuera)}")
        tocan = [p for p in tocan if p["id"] in a.solo]

    if len(tocan) > presupuesto:
        print(f"\n✗ {'--solo elige' if a.solo else 'GPT pide regenerar'} "
              f"{len(tocan)} planos y el presupuesto de la ronda es {presupuesto}.",
              file=sys.stderr)
        for p in tocan:
            print(f"   · {p['id']} ({p['veredicto']}) — {p.get('por_que', '')[:70]}",
                  file=sys.stderr)
        sys.exit("\n  No se arma el plan. Decide cuáles entran y córrelo con "
                 "`--solo <id> <id>`, o pídele a GPT que priorice.")

    base = {t["id"]: t for t in json.loads(pathlib.Path(a.base).read_text())} \
        if pathlib.Path(a.base).is_file() else {}
    if not base:
        sys.exit(f"✗ no encuentro el plan original en {a.base} — es de donde salen "
                 f"los keyframes, las rutas de salida y los modelos. Pásalo con --base.")

    nuevo, sin_base = [], []
    for p in tocan:
        orig = base.get(p["id"])
        if not orig:
            sin_base.append(p["id"])
            continue
        t = dict(orig)
        correccion = (p.get("correccion") or "").strip()
        if correccion:
            # El prompt viejo + la corrección tal cual llegó. Redactarlo bien es
            # trabajo de Claude: esto es un borrador, y el script lo dice.
            t["prompt"] = f"{orig['prompt']}. {correccion}"
        kf = p.get("keyframe")
        if kf and kf != "mismo":
            t["imagen"] = kf
        nuevo.append(t)

    if sin_base:
        print(f"⚠ GPT nombró planos que no están en el plan original: "
              f"{', '.join(sin_base)} — quedaron fuera.")
    if not nuevo:
        print("\n✓ nada que regenerar: GPT aprobó todo lo de esta ronda.")
        return 0

    destino = pathlib.Path(a.out or a.base.replace(".json", f"-ronda{d.get('ronda','X')}.json"))
    destino.write_text(json.dumps(nuevo, indent=2, ensure_ascii=False))

    print(f"\n✓ {corta(destino)}  ·  {len(nuevo)} planos  (de {presupuesto} autorizados)")
    for p in tocan:
        if p["id"] in [t["id"] for t in nuevo]:
            print(f"   · {p['id']} {p['veredicto']} — {p.get('por_que','')[:64]}")
    if d.get("no_se_toca"):
        print("\n  No se toca:", " · ".join(d["no_se_toca"]))
    print("\n⚠ ESTE PLAN ES UN BORRADOR. Los prompts traen la corrección de GPT")
    print("  pegada tal cual — léelos y redáctalos antes de gastar créditos.")
    print(f"  Y revisa que nada contradiga gcl-agent/universo/CANON_LOCK.md:")
    print("  el canon gana sobre GPT, siempre.")
    print(f"\n  Cuando estén buenos:  python3 scripts/cola.py enviar {corta(destino)}")


def main():
    ap = argparse.ArgumentParser(description="La mesa — ver mesa/CONTRATO.md")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("parte", help="arma el parte + la hoja de contacto para GPT")
    p.add_argument("pieza")
    p.add_argument("--plan", help="el plan que se ejecutó (para el prompt y los keyframes)")
    p.add_argument("--cola", default=str(RAIZ / "out" / "_cola" / "cola.json"))
    p.add_argument("--ronda", type=int, default=1)
    p.set_defaults(fn=parte)

    q = sub.add_parser("plan", help="traduce la respuesta de GPT a un plan de cola")
    q.add_argument("pieza")
    q.add_argument("--entrada", help="por defecto, la ronda más alta de mesa/entrada/")
    q.add_argument("--base", default="", help="el plan original, de donde salen keyframes y rutas")
    q.add_argument("--out", help="dónde escribir el plan nuevo")
    q.add_argument("--solo", nargs="*", default=[], help="ids que sí entran, si te pasaste del presupuesto")
    q.set_defaults(fn=plan)

    a = ap.parse_args()
    if a.cmd == "plan" and not a.base:
        a.base = str(RAIZ / "gcl-agent" / a.pieza / "_plan.json")
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
