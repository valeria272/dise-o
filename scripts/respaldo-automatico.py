#!/usr/bin/env python3
"""Respaldo automático al terminar una sesión de Claude — nada se queda en el equipo.

Lo llama el hook `SessionEnd` de `.claude/settings.json` (versionado, así que corre
en TODAS las máquinas del equipo, Mac o Windows, sin instalar nada). Existe porque
el estudio no puede depender de que alguien se acuerde de `/cierre`: si la sesión
se cierra sin rito, lo trabajado igual sube a GitHub, y la cosecha nocturna en la
nube (ver docs/MEMORIA-POR-CLIENTE.md) lo destila en el cerebro de cada cliente.

Reglas:
- Commitea TODO lo no ignorado, como /cierre (git add -A), salvo archivos de más
  de 45 MB, que GitHub rechaza: esos se avisan y se quedan fuera.
- pull --rebase antes del push. Si hay conflicto, aborta el rebase y deja el commit
  local: el próximo /abrir o /cierre lo resuelve. Nunca deja el repo a medio rebase.
- No hace nada si hay un merge/rebase en curso o si no hay cambios.
- Nunca falla hacia afuera (exit 0 siempre): un hook que se cae no debe molestar.
"""
import datetime as dt
import pathlib
import re
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
TOPE = 45 * 1024 * 1024
LOG = RAIZ / ".git" / "respaldo-automatico.log"


def git(*args, check=False):
    r = subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=90)
    if check and r.returncode:
        raise RuntimeError(r.stderr.strip() or r.stdout.strip())
    return r


def anotar(msg):
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"{dt.datetime.now():%Y-%m-%d %H:%M} {msg}\n")
    except OSError:
        pass
    print(f"[respaldo] {msg}", file=sys.stderr)


def main():
    gitdir = RAIZ / ".git"
    if not gitdir.exists():
        return
    if gitdir.is_dir() and any((gitdir / x).exists() for x in ("rebase-merge", "rebase-apply", "MERGE_HEAD")):
        return anotar("merge/rebase en curso: no se toca nada")

    git("add", "-A")
    grandes = []
    for ruta in git("diff", "--cached", "--name-only").stdout.splitlines():
        p = RAIZ / ruta
        if p.is_file() and p.stat().st_size > TOPE:
            git("reset", "-q", "--", ruta)
            grandes.append(ruta)
    if grandes:
        anotar(f"fuera por pesar más de 45 MB (súbelos a Drive): {', '.join(grandes)}")

    cambios = git("diff", "--cached", "--name-only").stdout.splitlines()
    if cambios:
        marcas = sorted({m.group(1) for c in cambios
                         if (m := re.match(r"clients/([^/_][^/]*)/", c))})
        quien = git("config", "user.name").stdout.strip() or "sin nombre"
        titulo = f"{', '.join(marcas) or 'ESTUDIO'}: respaldo automático al cerrar la sesión de {quien}"
        cuerpo = ("Lo subió el hook SessionEnd (scripts/respaldo-automatico.py) porque la "
                  "sesión terminó con cambios sin subir. La cosecha nocturna en la nube "
                  f"destila lo aprendido en clients/<marca>/APRENDIZAJES.md.\n\n{len(cambios)} archivo(s).")
        git("commit", "-q", "-m", titulo, "-m", cuerpo)

    rama = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if rama == "HEAD":
        return anotar("HEAD suelto: no se hace push")
    if not git("rev-list", f"@{{u}}..HEAD").stdout.strip() and not cambios:
        return  # nada propio que subir
    if git("pull", "--rebase", "-q").returncode:
        git("rebase", "--abort")
        return anotar("conflicto al traer lo de los demás: el commit quedó LOCAL; "
                      "el próximo /abrir o /cierre lo resuelve")
    r = git("push", "-q")
    anotar("✓ subido a GitHub" if r.returncode == 0 else f"push falló: {r.stderr.strip()[:200]}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # nunca romper el cierre de sesión
        anotar(f"error: {e}")
    sys.exit(0)
