#!/usr/bin/env python3
"""Memoria por cliente — el cerebro de cada cuenta viaja a git, a Drive y a Claude.

Por qué existe: el aprendizaje de una cuenta (qué rechaza el cliente, qué aprueba a
la primera, sus excepciones) quedaba enterrado en bitácoras de miles de líneas o en
la memoria local de UNA máquina. Si la diseñadora faltaba, el conocimiento faltaba
con ella. Ahora cada cliente tiene `clients/<marca>/APRENDIZAJES.md`, y /cierre no
cierra hasta que la cosecha del día está escrita ahí.

Subcomandos:
  verificar [marca ...]   ¿Cada marca tocada hoy tiene su cosecha de hoy? (exit 1 si no)
  semilla   [marca ...]   Regenera docs/memoria-semilla/cliente-<marca>.md (+ índice)
  drive     [marca ...]   Sube APRENDIZAJES.md como Google Doc a «MEMORIA DEL ESTUDIO»
  cerrar    [marca ...]   verificar → semilla → drive. Es lo que llama /cierre
  auditar                 Tabla: última sesión en bitácora vs última cosecha, por marca

Sin marcas, `verificar` y `cerrar` detectan solas las marcas tocadas hoy (commits de
hoy + cambios sin commitear). `semilla`, `drive` y `auditar` aceptan --todas.

Uso:  python scripts/memoria-cliente.py cerrar
      python scripts/memoria-cliente.py verificar hilton
      python scripts/memoria-cliente.py auditar
"""
import argparse
import datetime as dt
import json
import os
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = pathlib.Path(__file__).resolve().parent.parent
CLIENTES = RAIZ / "clients"
SEMILLA = RAIZ / "docs/memoria-semilla"
IDS_DRIVE = CLIENTES / "_memoria-drive.json"
RAIZ_DRIVE = "16kNWE2mkbLh1uTb5Jc5TuDhYwM0OOw0A"  # AGENCIA COPYWRITERS
CARPETA_DRIVE = "MEMORIA DEL ESTUDIO — cerebro por cliente"

# Prefijos de scripts, out/, public/assets/, raw/ y composiciones → carpeta de clients/
ALIAS = {
    "between": "hilton", "bw": "hilton", "dt": "hilton", "doubletree": "hilton",
    "p18": "piso18", "tc": "tierra-calma", "tierracalma": "tierra-calma",
    "rentas": "nueva-urbe", "inu": "nueva-urbe", "nuevaurbe": "nueva-urbe",
    "copylab": "copywriters", "gcl": "copywriters", "cap02": "copywriters",
    "santagota": "santa-gota", "sanesteban": "san-esteban", "click": "ebema",
    "sallobos": "sal-lobos", "cb": "casablanca",
}
IGNORAR = {"clients/_estado-sync.json", "clients/_memoria-drive.json"}


def marcas_existentes():
    return sorted(p.name for p in CLIENTES.iterdir()
                  if p.is_dir() and not p.name.startswith(("_", ".")))


def a_marca(token, marcas):
    t = token.lower()
    t = re.sub(r"\.(tsx?|py|sh|md|json|ya?ml)$", "", t)
    if t in marcas:
        return t
    if t in ALIAS:
        return ALIAS[t]
    compacto = t.replace("-", "")
    for m in marcas:  # «CasablancaSep2026» → casablanca, «sanEstebanReel» → san-esteban
        if compacto.startswith(m.replace("-", "")):
            return m
    for a, m in ALIAS.items():
        if len(a) > 3 and compacto.startswith(a):
            return m
    return None


def marca_de_ruta(ruta, marcas):
    if ruta in IGNORAR:
        return None
    p = ruta.split("/")
    if p[0] == "clients" and len(p) > 2:
        return p[1] if p[1] in marcas else None
    if p[0] in ("out", "raw") and len(p) > 1:
        return a_marca(p[1], marcas)
    if p[:2] == ["public", "assets"] and len(p) > 2:
        return a_marca(p[2], marcas)
    if p[:2] in (["src", "compositions"], ["src", "brand"]) and len(p) > 2:
        return a_marca(p[2], marcas)
    if p[0] == "scripts" and len(p) == 2:
        return a_marca(re.split(r"[-_.]", p[1])[0], marcas)
    return None


def git(*args):
    r = subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.stdout


def marcas_tocadas_hoy():
    marcas = marcas_existentes()
    rutas = set()
    for linea in git("status", "--porcelain", "-uall").splitlines():
        ruta = linea[3:].split(" -> ")[-1].strip('"')
        rutas.add(ruta)
    yo = git("config", "user.name").strip()
    hoy = dt.date.today().isoformat()
    log = git("log", f"--since={hoy} 00:00", f"--author={yo}", "--name-only", "--format=")
    rutas.update(l for l in log.splitlines() if l.strip())
    tocadas = {marca_de_ruta(r, marcas) for r in rutas}
    tocadas.discard(None)
    return sorted(tocadas)


# ─── Lectura del cerebro ──────────────────────────────────────────────────────

def leer(marca):
    f = CLIENTES / marca / "APRENDIZAJES.md"
    return f.read_text(encoding="utf-8") if f.exists() else None


def cosechas(texto):
    """Fechas de las entradas de «Registro de cosechas», la más nueva primero."""
    bloque = texto.split("## 9.", 1)[-1] if "## 9." in texto else texto
    return re.findall(r"^### (\d{4}-\d{2}-\d{2})", bloque, flags=re.M)


def seccion(texto, n):
    m = re.search(rf"^## {n}\..*?$(.*?)(?=^## \d+\.|\Z)", texto, flags=re.M | re.S)
    return m.group(1) if m else ""


def reglas(texto):
    """[(✔, línea)] de la sección 4, más confirmadas primero."""
    out = []
    for l in seccion(texto, 4).splitlines():
        if l.startswith("- **R-"):
            m = re.search(r"✔\s*×\s*(\d+)", l)
            out.append((int(m.group(1)) if m else 1, l.strip()))
    return sorted(out, key=lambda x: -x[0])


def ultima_bitacora(marca):
    f = CLIENTES / marca / "BITACORA.md"
    if not f.exists():
        return None, 0
    fechas = re.findall(r"^## (\d{4}-\d{2}-\d{2})", f.read_text(encoding="utf-8"), flags=re.M)
    return (fechas[0] if fechas else None), fechas


# ─── verificar ────────────────────────────────────────────────────────────────

def verificar(marcas):
    hoy = dt.date.today().isoformat()
    otras = [m for m in marcas_existentes()]
    fallas = []
    for m in marcas:
        t = leer(m)
        if t is None:
            fallas.append(f"{m}: no tiene clients/{m}/APRENDIZAJES.md — créalo desde clients/_PLANTILLA/")
            continue
        c = cosechas(t)
        if not c or c[0] != hoy:
            fallas.append(f"{m}: falta la cosecha de hoy ({hoy}) en «9. Registro de cosechas»"
                          + (f" — la última es del {c[0]}" if c else ""))
            continue
        # No mezclar: la entrada de hoy no debería nombrar otras marcas.
        entrada = re.split(r"^### ", t.split("## 9.", 1)[-1], flags=re.M)[1]
        nombradas = [o for o in otras if o != m and re.search(rf"\b{re.escape(o)}\b", entrada, re.I)]
        aviso = f"  ▲ la cosecha de hoy nombra otras marcas ({', '.join(nombradas)}): revisa que no se haya colado criterio ajeno" if nombradas else ""
        print(f"✓ {m}: cosecha de hoy escrita · {len(reglas(t))} reglas firmes" + (f"\n{aviso}" if aviso else ""))
    for f in fallas:
        print(f"✗ {f}")
    return not fallas


# ─── semilla ──────────────────────────────────────────────────────────────────

def semilla(marcas):
    SEMILLA.mkdir(parents=True, exist_ok=True)
    for m in marcas:
        t = leer(m)
        if t is None:
            continue
        c = cosechas(t)
        cab = re.search(r"Criterio:.*", t)
        rs = reglas(t)
        top = "\n".join(l for _, l in rs[:20]) or "_(todavía sin reglas firmes)_"
        rechazos = "\n".join(l.strip() for l in seccion(t, 7).splitlines() if l.startswith("- **X-"))[:3000]
        nota = f"""---
name: cliente-{m}
description: "{m.upper()} — cerebro del cliente: {len(rs)} reglas firmes, última cosecha {c[0] if c else '—'}. Generado desde clients/{m}/APRENDIZAJES.md; leerlo antes de diseñar para {m}"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/{m}/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para {m}: no se traspasa a otra marca.

{cab.group(0).strip('> ') if cab else ''}

## Reglas más confirmadas
{top}

## Lo que ya costó rondas
{rechazos or '_(sin rechazos registrados)_'}
"""
        (SEMILLA / f"cliente-{m}.md").write_text(nota, encoding="utf-8")
    # Índice: una sola nota que lista todos los cerebros.
    filas = []
    for m in marcas_existentes():
        t = leer(m)
        if t:
            c = cosechas(t)
            filas.append(f"- [{m}](cliente-{m}.md) — {len(reglas(t))} reglas · última cosecha {c[0] if c else '—'}")
    (SEMILLA / "cliente-indice.md").write_text(f"""---
name: cliente-indice
description: "Índice de los cerebros por cliente (clients/<marca>/APRENDIZAJES.md) — leer el de la marca antes de diseñar; nunca aplicar el de otra"
metadata:
  type: reference
---

Cada cuenta tiene su cerebro en `clients/<marca>/APRENDIZAJES.md`, alimentado en cada
`/cierre`. ⛔ El criterio de una marca NO se traspasa a otra. Método completo:
`docs/MEMORIA-POR-CLIENTE.md`.

{chr(10).join(filas)}
""", encoding="utf-8")
    idx = SEMILLA / "MEMORY.md"
    linea = "- [⭐⭐ Cerebro por cliente](cliente-indice.md) — clients/<marca>/APRENDIZAJES.md: leer el de la marca ANTES de diseñar; se alimenta en cada /cierre; nunca aplicar el de otra marca"
    if idx.exists() and "cliente-indice.md" not in idx.read_text(encoding="utf-8"):
        txt = idx.read_text(encoding="utf-8").rstrip("\n").split("\n")
        pos = next((i for i, l in enumerate(txt) if l.startswith("- [")), len(txt))
        txt.insert(pos, linea)
        idx.write_text("\n".join(txt) + "\n", encoding="utf-8")
    print(f"✓ semilla: {len(marcas)} nota(s) cliente-*.md + índice en docs/memoria-semilla/")


# ─── drive ────────────────────────────────────────────────────────────────────

def servicio_drive():
    sys.path.insert(0, str(RAIZ / "scripts"))
    from _entorno import token_google
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    ruta = token_google()
    creds = Credentials.from_authorized_user_file(str(ruta))
    if not creds.valid:
        creds.refresh(Request())
        # Nunca guardar un token recortado (regla del monorepo: 6 scopes).
        if set(creds.scopes or []) >= set(json.loads(pathlib.Path(ruta).read_text()).get("scopes", [])):
            pathlib.Path(ruta).write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def drive(marcas):
    try:
        from googleapiclient.http import MediaInMemoryUpload
        svc = servicio_drive()
    except Exception as e:  # sin token o sin librerías: se avisa, no se bloquea el cierre
        print(f"✗ Drive no disponible ({e.__class__.__name__}: {e}). El cerebro SÍ quedó en git; "
              f"súbelo después con: python scripts/memoria-cliente.py drive {' '.join(marcas)}")
        return False
    ids = json.loads(IDS_DRIVE.read_text(encoding="utf-8")) if IDS_DRIVE.exists() else {}

    def vivo(fid):
        try:
            f = svc.files().get(fileId=fid, fields="id,trashed", supportsAllDrives=True).execute()
            return not f.get("trashed")
        except Exception:
            return False

    carpeta = ids.get("_carpeta")
    if not carpeta or not vivo(carpeta):
        carpeta = svc.files().create(body={
            "name": CARPETA_DRIVE, "mimeType": "application/vnd.google-apps.folder",
            "parents": [RAIZ_DRIVE],
            "description": "Lo generan los /cierre del estudio (scripts/memoria-cliente.py). "
                           "No editar a mano: la fuente es clients/<marca>/APRENDIZAJES.md en GitHub.",
        }, fields="id", supportsAllDrives=True).execute()["id"]
        ids["_carpeta"] = carpeta
    ok = True
    for m in marcas:
        t = leer(m)
        if t is None:
            continue
        media = MediaInMemoryUpload(t.encode("utf-8"), mimetype="text/markdown", resumable=False)
        nombre = f"{m.upper()} — cerebro del cliente"
        try:
            if ids.get(m) and vivo(ids[m]):
                svc.files().update(fileId=ids[m], media_body=media, body={"name": nombre},
                                   supportsAllDrives=True).execute()
            else:
                ids[m] = svc.files().create(body={
                    "name": nombre, "parents": [carpeta],
                    "mimeType": "application/vnd.google-apps.document",
                }, media_body=media, fields="id", supportsAllDrives=True).execute()["id"]
            print(f"✓ Drive: {m} → https://docs.google.com/document/d/{ids[m]}")
        except Exception as e:
            ok = False
            print(f"✗ Drive: {m} no se subió ({e})")
    IDS_DRIVE.write_text(json.dumps(ids, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return ok


# ─── auditar ──────────────────────────────────────────────────────────────────

def auditar():
    print(f"{'marca':<14} {'bitácora':<11} {'cosecha':<11} {'reglas':>6}  sesiones sin cosechar")
    for m in marcas_existentes():
        ult, fechas = ultima_bitacora(m)
        t = leer(m)
        c = cosechas(t) if t else []
        pend = sum(1 for f in (fechas or []) if not c or f > c[0])
        estado = "SIN CEREBRO" if t is None else (f"⚠️ {pend}" if pend else "al día")
        print(f"{m:<14} {ult or '—':<11} {(c[0] if c else '—'):<11} {len(reglas(t)) if t else 0:>6}  {estado}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("accion", choices=["verificar", "semilla", "drive", "cerrar", "auditar"])
    ap.add_argument("marcas", nargs="*")
    ap.add_argument("--todas", action="store_true")
    a = ap.parse_args()
    if a.accion == "auditar":
        return auditar()
    todas = marcas_existentes()
    malas = [m for m in a.marcas if m not in todas]
    if malas:
        sys.exit(f"✗ No existe clients/{malas[0]}/ — marcas: {', '.join(todas)}")
    if a.todas:
        marcas = [m for m in todas if leer(m)]
    elif a.marcas:
        marcas = a.marcas
    else:
        marcas = marcas_tocadas_hoy()
        print(f"Marcas tocadas hoy: {', '.join(marcas) or 'ninguna'}")
    if not marcas:
        return
    if a.accion == "verificar":
        sys.exit(0 if verificar(marcas) else 1)
    if a.accion == "semilla":
        return semilla(marcas)
    if a.accion == "drive":
        sys.exit(0 if drive(marcas) else 1)
    if a.accion == "cerrar":
        if not verificar(marcas):
            sys.exit("\n⛔ No se cierra: escribe la cosecha de hoy en el APRENDIZAJES.md de cada marca de arriba.")
        semilla(marcas)
        drive(marcas)


if __name__ == "__main__":
    main()
