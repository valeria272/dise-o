#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resolución portable de rutas y credenciales.

Lo usa cualquier script de este repo para no quemar `/Users/Vale/...`, que rompe
en el Mac de otro diseñador. Es compatible hacia atrás: si el monorepo está donde
siempre estuvo, encuentra lo mismo que antes.

    from _entorno import RAIZ, OUT, RAW, PUBLIC, token_google, env_compartido, cargar_env

Orden de búsqueda de credenciales (la primera que exista gana):
  1. variable de entorno  COPYLAB_TOKEN / COPYLAB_ENV
  2. credentials/ dentro de este repo   ← lo que viaja en el ZIP si se decide incluirlo
  3. ../ASISTENTE PERSONAL/  (el layout del monorepo de Valeria)
  4. ~/copylab-work/respaldo-credenciales/
"""
import os
import pathlib
import sys

# ── Raíz del repo: derivada de la ubicación de este archivo, nunca quemada ──
RAIZ = pathlib.Path(__file__).resolve().parent.parent
PUBLIC = RAIZ / "public"
ASSETS = PUBLIC / "assets"
OUT = RAIZ / "out"
RAW = RAIZ / "raw"
CLIENTS = RAIZ / "clients"


def _primera_que_exista(candidatas):
    for c in candidatas:
        if c and pathlib.Path(c).exists():
            return pathlib.Path(c)
    return None


def token_google():
    """Ruta al token OAuth de Google, o None si no está en esta máquina."""
    return _primera_que_exista([
        os.environ.get("COPYLAB_TOKEN"),
        RAIZ / "credentials" / "token.json",
        RAIZ.parent / "ASISTENTE PERSONAL" / "credentials" / "token.json",
        pathlib.Path.home() / "copylab-work" / "respaldo-credenciales" / "token.json",
    ])


def env_compartido():
    """Ruta al .env compartido, o None."""
    return _primera_que_exista([
        os.environ.get("COPYLAB_ENV"),
        RAIZ / ".env",
        RAIZ.parent / "ASISTENTE PERSONAL" / ".env",
        pathlib.Path.home() / "copylab-work" / "respaldo-credenciales" / ".env",
    ])


def cargar_env():
    """Carga el .env compartido en os.environ. Devuelve un dict con lo cargado."""
    ruta = env_compartido()
    cargadas = {}
    if not ruta:
        return cargadas
    for linea in ruta.read_text(encoding="utf-8", errors="ignore").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        k, v = linea.split("=", 1)
        k, v = k.strip(), v.strip().strip('"').strip("'")
        os.environ.setdefault(k, v)
        cargadas[k] = v
    return cargadas


def exigir(ruta, que, comando_ayuda=""):
    """Aborta con un mensaje útil en vez de un traceback críptico."""
    if ruta:
        return ruta
    msg = f"\n✗ No encuentro {que} en esta máquina.\n"
    if comando_ayuda:
        msg += f"  {comando_ayuda}\n"
    msg += "  Ver: docs/TRASPASO-ZIP.md § credenciales\n"
    raise SystemExit(msg)


# El venv compartido, si existe; si no, el intérprete con el que se corre esto.
#
# ⚠️ Windows (31-08-2026): antes esto solo miraba el layout POSIX `venv/bin/python3`
# y caía a la cadena literal "python3", que en Windows NO existe como comando —
# los scripts que la usaban para lanzar subprocesos fallaban en seco. Ahora mira
# también `venv\Scripts\python.exe` y, si no hay venv, devuelve `sys.executable`,
# que siempre es un intérprete válido en cualquier sistema.
def python_venv():
    candidatas = [
        pathlib.Path.home() / "copylab-venv" / "bin" / "python3",       # macOS / Linux
        RAIZ / "venv" / "bin" / "python3",
        pathlib.Path.home() / "copylab-venv" / "Scripts" / "python.exe",  # Windows
        RAIZ / "venv" / "Scripts" / "python.exe",
        RAIZ / ".venv" / "Scripts" / "python.exe",
        RAIZ / ".venv" / "bin" / "python3",
    ]
    for c in candidatas:
        if c.exists():
            return str(c)
    return sys.executable or "python3"


if __name__ == "__main__":
    print(f"RAIZ            {RAIZ}")
    print(f"public/assets   {ASSETS}  {'✓' if ASSETS.exists() else '✗ FALTA'}")
    print(f"raw/            {RAW}  {'✓' if RAW.exists() else '— (se baja de Drive)'}")
    print(f"out/            {OUT}")
    print(f"token Google    {token_google() or '✗ no está en esta máquina'}")
    print(f".env compartido {env_compartido() or '✗ no está en esta máquina'}")
    print(f"python          {python_venv()}")
