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

# ── Consola de Windows ────────────────────────────────────────────────────────
# PowerShell escribe en cp1252 y revienta con UnicodeEncodeError al imprimir un
# «✓» o un «✗». Lo peor no es el error: es que salta DESPUÉS de que el script ya
# hizo el trabajo, así que parece que falló algo cuando no falló nada. Se arregló
# a mano en siete scripts entre agosto y septiembre de 2026, y volvió a aparecer
# en el octavo y el noveno. Va acá porque todos los scripts del estudio importan
# este módulo: el décimo ya nace arreglado.
for _flujo in (sys.stdout, sys.stderr):
    try:
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

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
    """Ruta al .env compartido, o None.

    `credentials/.env` es lo que deja `scripts/llavero.py abrir` — es la vía
    normal en la máquina de un diseñador, que no tiene el monorepo entero.
    """
    return _primera_que_exista([
        os.environ.get("COPYLAB_ENV"),
        RAIZ / "credentials" / ".env",
        RAIZ / ".env",
        RAIZ.parent / "ASISTENTE PERSONAL" / ".env",
        pathlib.Path.home() / "copylab-work" / "respaldo-credenciales" / ".env",
    ])


def clave_freepik():
    """La clave de Magnific/Freepik, o None. Un único lugar para todos los scripts.

    Orden: variable de entorno · el llavero abierto · el archivo suelto del HOME.
    Si devuelve None, casi siempre es que falta correr `llavero.py abrir`.
    """
    v = os.environ.get("FREEPIK_API_KEY") or os.environ.get("MAGNIFIC_API_KEY")
    if v:
        return v.strip()
    ruta = env_compartido()
    if ruta:
        for linea in ruta.read_text(encoding="utf-8", errors="ignore").splitlines():
            linea = linea.strip()
            if linea.startswith(("FREEPIK_API_KEY=", "MAGNIFIC_API_KEY=")):
                v = linea.split("=", 1)[1].strip().strip('"').strip("'")
                if v:
                    return v
    suelto = pathlib.Path.home() / ".magnific_key"
    if suelto.is_file():
        v = suelto.read_text(encoding="utf-8").strip()
        if v:
            return v
    return None


FALTA_CLAVE = (
    "✗ No encuentro la clave de Magnific / Freepik.\n"
    "  Ábrela desde el llavero del repo:\n"
    "      python3 scripts/llavero.py abrir\n"
    "  (la contraseña del estudio se entrega una vez, en el onboarding)\n"
)


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


# ── El navegador que rinde los HTML a PNG ────────────────────────────────────
#
# ⚠️ 03-09-2026: seis archivos tenían quemado
# `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`. En el Mac de
# Valeria funciona; en el PC de otra diseñadora y en cualquier máquina Linux,
# `render.sh` moría en la primera línea. Es el mismo problema que el `python3`
# inexistente de Windows que se arregló en `python_venv()`, así que la solución
# vive en el mismo lugar: una sola lista, que todos consultan.
#
# Se acepta cualquier Chromium: Chrome, Chromium, Edge y Brave rinden idéntico
# con `--headless=new`, y en un servidor sin Chrome instalado el Chromium que
# deja Playwright es lo único que hay.
def navegador():
    """Ruta al Chrome/Chromium de esta máquina, o None si no hay ninguno.

    Orden: variable de entorno · lo instalado en el sistema · el Chromium de
    Playwright. Devuelve un `str` porque casi siempre va a un subproceso.
    """
    import glob
    import shutil

    # 1. Puesta a mano. `PUPPETEER_EXECUTABLE_PATH` va incluida porque es la que
    #    ya definen varias imágenes de CI.
    for var in ("COPYLAB_CHROME", "CHROME_PATH", "PUPPETEER_EXECUTABLE_PATH"):
        v = os.environ.get(var)
        if v and pathlib.Path(v).exists():
            return str(v)

    # 2. En el PATH (el caso normal en Linux).
    for cmd in ("google-chrome", "google-chrome-stable", "chromium",
                "chromium-browser", "chrome"):
        hallado = shutil.which(cmd)
        if hallado:
            return hallado

    home = pathlib.Path.home()
    fijas = [
        # macOS
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        home / "Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        # Windows
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        home / "AppData/Local/Google/Chrome/Application/chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        # Linux, fuera del PATH
        "/usr/bin/google-chrome",
        "/opt/google/chrome/chrome",
        "/snap/bin/chromium",
    ]
    hallado = _primera_que_exista(fijas)
    if hallado:
        return str(hallado)

    # 3. El Chromium que instala Playwright. En un servidor headless suele ser
    #    el único navegador de la máquina, y el número de build cambia con cada
    #    versión — por eso se busca con comodín en vez de fijarlo.
    raices = [os.environ.get("PLAYWRIGHT_BROWSERS_PATH"),
              "/opt/pw-browsers",
              home / ".cache/ms-playwright",
              home / "AppData/Local/ms-playwright"]
    patrones = ["chromium-*/chrome-linux/chrome",
                "chromium-*/chrome-mac/Chromium.app/Contents/MacOS/Chromium",
                "chromium-*/chrome-win/chrome.exe",
                "chromium_headless_shell-*/chrome-linux/headless_shell"]
    for raiz in raices:
        if not raiz:
            continue
        for patron in patrones:
            for c in sorted(glob.glob(str(pathlib.Path(raiz) / patron)), reverse=True):
                if pathlib.Path(c).exists():
                    return c
    return None


FALTA_NAVEGADOR = (
    "\u2717 No encuentro Chrome ni Chromium en esta m\u00e1quina.\n"
    "  Sin navegador no hay render de HTML a PNG.\n"
    "  Inst\u00e1lalo desde https://www.google.com/chrome/ o, si ya lo tienes\n"
    "  en una ruta rara, ind\u00edcalo:  export COPYLAB_CHROME=\"/ruta/al/chrome\"\n"
)


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
    # `--navegador` existe para los render.sh: imprime la ruta y sale 1 si no
    # hay ninguno, para que el shell pueda cortar con `|| exit 1`.
    if "--navegador" in sys.argv:
        _n = navegador()
        if not _n:
            sys.stderr.write(FALTA_NAVEGADOR)
            raise SystemExit(1)
        print(_n)
        raise SystemExit(0)

    print(f"RAIZ            {RAIZ}")
    print(f"public/assets   {ASSETS}  {'✓' if ASSETS.exists() else '✗ FALTA'}")
    print(f"raw/            {RAW}  {'✓' if RAW.exists() else '— (se baja de Drive)'}")
    print(f"out/            {OUT}")
    print(f"token Google    {token_google() or '✗ no está en esta máquina'}")
    print(f".env compartido {env_compartido() or '✗ no está en esta máquina'}")
    _k = clave_freepik()
    print(f"Magnific/Freepik {(_k[:4] + '…' + _k[-3:]) if _k else '✗ corre: python3 scripts/llavero.py abrir'}")
    print(f"python          {python_venv()}")
    _nav = navegador() or "✗ no hay Chrome/Chromium acá"
    print(f"navegador       {_nav}")
