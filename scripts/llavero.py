#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Llavero del estudio — las credenciales viajan EN el repo, cifradas.

El problema que resuelve: cada diseñador nuevo tenía que pedirle la clave de
Magnific a Valeria por WhatsApp, y el token de Google se mandaba a mano. Ahora
el llavero vive en `credentials/llavero.copylab`, versionado como cualquier otro
archivo, y se abre con **una sola contraseña** que se entrega una vez en el
onboarding.

    python3 scripts/llavero.py abrir     ← lo que corre un diseñador nuevo
    python3 scripts/llavero.py estado    ← ¿está abierto? ¿qué claves tengo?
    python3 scripts/llavero.py ver       ← qué hay dentro (valores enmascarados)

    python3 scripts/llavero.py guardar   ← solo Valeria: rehace el llavero
    python3 scripts/llavero.py guardar --set FREEPIK_API_KEY=FPSX...

Por qué cifrado y no en texto plano, aunque el repo sea privado:
  · una clave en texto plano queda en el HISTORIAL de git para siempre — rotarla
    no la borra, hay que reescribir la historia del repo entero;
  · el repo se clona en el notebook de cada diseñador, en Windows, en OneDrive;
  · si el repo cambia de visibilidad o se forkea una vez, la clave voló.
Cifrado, el archivo público es ruido: sin la contraseña no vale nada.

Al abrirlo escribe, todo ignorado por git:
  · `credentials/.env`   — lo lee `scripts/_entorno.py` y por él todos los scripts
  · `~/.magnific_key`    — lo leen los scripts antiguos de Magnific/Freepik
  · los archivos sueltos del llavero (token.json, client_secret.json) en credentials/
"""
import argparse
import base64
import getpass
import hashlib
import json
import os
import stat
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _entorno import RAIZ  # noqa: E402

LLAVERO = RAIZ / "credentials" / "llavero.copylab"
ENV_LOCAL = RAIZ / "credentials" / ".env"
CABECERA = "COPYLAB-LLAVERO-1"

# Las claves que necesita un diseñador para producir. Todo lo demás del .env del
# monorepo (Slack, Trello, bancos, Meta) NO entra acá: el llavero es del estudio
# de diseño, no de la agencia entera.
CLAVES = [
    ("FREEPIK_API_KEY", "Magnific / Freepik — generación y escalado de imágenes"),
    ("MAGNIFIC_API_KEY", "alias antiguo de la anterior (algunos scripts lo piden)"),
    ("HF_API_KEY", "Higgsfield — video IA"),
    ("HF_SECRET", "Higgsfield — secreto que acompaña a la anterior"),
    ("ANTHROPIC_API_KEY", "API de Claude para los scripts que la usan"),
]

# Archivos completos que también viajan en el llavero.
ARCHIVOS = [
    ("token.json", "token OAuth de Google — Drive, Sheets, Gmail del estudio"),
    ("client_secret.json", "cliente OAuth, para volver a autorizar desde cero"),
]


# ── cifrado ────────────────────────────────────────────────────────────────────
def _fernet(contrasena_texto, sal):
    try:
        from cryptography.fernet import Fernet
    except ImportError:
        sys.exit("✗ Falta la librería de cifrado. Instálala con:\n"
                 "    python3 -m pip install cryptography\n")
    semilla = hashlib.scrypt(contrasena_texto.encode("utf-8"), salt=sal,
                             n=2 ** 15, r=8, p=1, dklen=32,
                             maxmem=64 * 1024 * 1024)
    return Fernet(base64.urlsafe_b64encode(semilla))


def contrasena(confirmar=False):
    """La contraseña del llavero. Se pide una vez y se puede dejar guardada."""
    v = os.environ.get("COPYLAB_LLAVE")
    if v:
        return v.strip()
    guardada = Path.home() / ".copylab-llave"
    if guardada.is_file():
        v = guardada.read_text(encoding="utf-8").strip()
        if v:
            return v
    v = getpass.getpass("Contraseña del llavero del estudio: ").strip()
    if not v:
        sys.exit("✗ Sin contraseña no se puede abrir el llavero.")
    if confirmar and getpass.getpass("Repítela: ").strip() != v:
        sys.exit("✗ Las dos contraseñas no coinciden.")
    if not confirmar:
        r = input("¿La dejo guardada en ~/.copylab-llave para no volver a pedirla? [S/n] ")
        if r.strip().lower() in ("", "s", "si", "sí", "y"):
            guardada.write_text(v + "\n", encoding="utf-8")
            os.chmod(guardada, stat.S_IRUSR | stat.S_IWUSR)
            print("  ✓ guardada — este equipo ya no te la vuelve a pedir")
    return v


def leer_llavero():
    if not LLAVERO.is_file():
        sys.exit(f"✗ No existe {LLAVERO.relative_to(RAIZ)}.\n"
                 "  ¿Hiciste `git pull`? Si eres Valeria, créalo con:\n"
                 "    python3 scripts/llavero.py guardar\n")
    lineas = LLAVERO.read_text(encoding="utf-8").strip().splitlines()
    if not lineas or lineas[0].strip() != CABECERA:
        sys.exit("✗ El llavero está corrupto o es de otra versión.")
    sal = base64.b64decode(lineas[1].strip())
    cuerpo = "".join(l.strip() for l in lineas[2:]).encode()
    from cryptography.fernet import InvalidToken
    try:
        claro = _fernet(contrasena(), sal).decrypt(cuerpo)
    except InvalidToken:
        sys.exit("✗ Contraseña incorrecta.\n"
                 "  Si la guardaste mal: borra ~/.copylab-llave y vuelve a intentar.\n")
    return json.loads(claro)


def escribir_llavero(datos, clave_texto):
    sal = os.urandom(16)
    cuerpo = _fernet(clave_texto, sal).encrypt(
        json.dumps(datos, ensure_ascii=False, indent=1).encode("utf-8"))
    LLAVERO.parent.mkdir(parents=True, exist_ok=True)
    # 72 caracteres por línea: así el archivo es legible y git no lo trata raro.
    texto = cuerpo.decode()
    partido = [texto[i:i + 72] for i in range(0, len(texto), 72)]
    LLAVERO.write_text(
        CABECERA + "\n" + base64.b64encode(sal).decode() + "\n"
        + "\n".join(partido) + "\n", encoding="utf-8")


def enmascarar(v):
    v = str(v)
    return (v[:4] + "…" + v[-3:]) if len(v) > 12 else "…"


# ── comandos ──────────────────────────────────────────────────────────────────
def cmd_abrir(args):
    datos = leer_llavero()
    variables = datos.get("vars", {})
    archivos = datos.get("archivos", {})

    ENV_LOCAL.parent.mkdir(parents=True, exist_ok=True)
    cabecera = ("# Generado por scripts/llavero.py — NO se versiona, NO se edita a mano.\n"
                f"# Llavero del {datos.get('actualizado', '?')}. "
                "Para cambiar una clave: llavero.py guardar --set CLAVE=valor\n")
    ENV_LOCAL.write_text(
        cabecera + "".join(f"{k}={v}\n" for k, v in sorted(variables.items())),
        encoding="utf-8")
    os.chmod(ENV_LOCAL, stat.S_IRUSR | stat.S_IWUSR)
    print(f"✓ {ENV_LOCAL.relative_to(RAIZ)}  ({len(variables)} claves)")

    # Los scripts antiguos de Magnific leen este archivo suelto del HOME.
    fk = variables.get("FREEPIK_API_KEY") or variables.get("MAGNIFIC_API_KEY")
    if fk:
        mk = Path.home() / ".magnific_key"
        mk.write_text(fk.strip() + "\n", encoding="utf-8")
        os.chmod(mk, stat.S_IRUSR | stat.S_IWUSR)
        print(f"✓ {mk}  (Magnific / Freepik)")

    for nombre, contenido in sorted(archivos.items()):
        destino = RAIZ / "credentials" / nombre
        if destino.exists() and not args.forzar:
            print(f"· {destino.relative_to(RAIZ)} ya estaba — lo dejo "
                  "(usa --forzar para pisarlo)")
            continue
        destino.write_text(contenido, encoding="utf-8")
        os.chmod(destino, stat.S_IRUSR | stat.S_IWUSR)
        print(f"✓ {destino.relative_to(RAIZ)}")

    faltan = [k for k, _ in CLAVES if k not in variables]
    if faltan:
        print("\n  Sin llenar todavía en el llavero: " + ", ".join(faltan))
    print("\nListo. Comprueba con:  python3 scripts/llavero.py estado")


def cmd_estado(args):
    print(f"llavero          {LLAVERO.relative_to(RAIZ)}  "
          f"{'✓ está en el repo' if LLAVERO.is_file() else '✗ FALTA — haz git pull'}")
    print(f"abierto en       {ENV_LOCAL.relative_to(RAIZ)}  "
          f"{'✓' if ENV_LOCAL.is_file() else '✗ corre: python3 scripts/llavero.py abrir'}")
    print(f"~/.magnific_key  {'✓' if (Path.home() / '.magnific_key').is_file() else '✗'}")
    for nombre, _ in ARCHIVOS:
        d = RAIZ / "credentials" / nombre
        print(f"{nombre:<19}{'✓' if d.is_file() else '✗'}")
    if not ENV_LOCAL.is_file():
        return
    presentes = {l.split("=", 1)[0] for l in ENV_LOCAL.read_text(encoding="utf-8").splitlines()
                 if "=" in l and not l.startswith("#")}
    print()
    for k, para_que in CLAVES:
        print(f"  {'✓' if k in presentes else '·'} {k:<20} {para_que}")


def cmd_ver(args):
    datos = leer_llavero()
    print(f"Llavero del {datos.get('actualizado', '?')}\n")
    for k, v in sorted(datos.get("vars", {}).items()):
        print(f"  {k:<22} {enmascarar(v)}")
    for k, v in sorted(datos.get("archivos", {}).items()):
        print(f"  {k:<22} archivo, {len(v)} caracteres")


def _fuentes_locales():
    """De dónde saca los valores el comando `guardar`, en orden de preferencia."""
    fuentes = []
    for p in (ENV_LOCAL,
              RAIZ / ".env",
              RAIZ.parent / "ASISTENTE PERSONAL" / ".env",
              Path.home() / "copylab-work" / "respaldo-credenciales" / ".env"):
        if p.is_file():
            fuentes.append(p)
    return fuentes


def cmd_guardar(args):
    variables, archivos, de_donde = {}, {}, {}

    # 1. lo que ya estuviera en el llavero (para no perder nada al re-guardar)
    if LLAVERO.is_file() and not args.desde_cero:
        previo = leer_llavero()
        variables.update(previo.get("vars", {}))
        archivos.update(previo.get("archivos", {}))
        de_donde.update({k: "ya estaba en el llavero" for k in variables})

    # 2. los .env de esta máquina
    nombres = {k for k, _ in CLAVES}
    for f in _fuentes_locales():
        for linea in f.read_text(encoding="utf-8", errors="ignore").splitlines():
            linea = linea.strip()
            if not linea or linea.startswith("#") or "=" not in linea:
                continue
            k, v = linea.split("=", 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k in nombres and v:
                variables[k] = v
                de_donde[k] = str(f)

    # 3. el archivo suelto de Magnific
    mk = Path.home() / ".magnific_key"
    if mk.is_file():
        v = mk.read_text(encoding="utf-8").strip()
        if v:
            variables.setdefault("FREEPIK_API_KEY", v)
            de_donde.setdefault("FREEPIK_API_KEY", str(mk))

    # 4. archivos de credenciales de Google
    if not args.sin_google:
        for nombre, _ in ARCHIVOS:
            for base in (RAIZ / "credentials",
                         RAIZ.parent / "ASISTENTE PERSONAL" / "credentials",
                         Path.home() / "copylab-work" / "respaldo-credenciales"):
                p = base / nombre
                if p.is_file():
                    archivos[nombre] = p.read_text(encoding="utf-8")
                    de_donde[nombre] = str(p)
                    break

    # 5. lo que venga por --set, que manda sobre todo lo anterior
    for par in args.set or []:
        if "=" not in par:
            sys.exit(f"✗ --set espera CLAVE=valor, llegó: {par}")
        k, v = par.split("=", 1)
        variables[k.strip()] = v.strip()
        de_donde[k.strip()] = "--set"

    if not variables and not archivos:
        sys.exit("✗ No encontré ninguna credencial en esta máquina.\n"
                 "  Pásalas a mano:  llavero.py guardar --set FREEPIK_API_KEY=...\n")

    print("Voy a guardar en el llavero:\n")
    for k in sorted(variables):
        print(f"  {k:<22} {enmascarar(variables[k]):<12} ← {de_donde.get(k, '?')}")
    for k in sorted(archivos):
        print(f"  {k:<22} {'archivo':<12} ← {de_donde.get(k, '?')}")
    print()
    r = input("¿Lo cifro y lo dejo listo para subir? [S/n] ").strip().lower()
    if r not in ("", "s", "si", "sí", "y"):
        sys.exit("Cancelado, no toqué nada.")

    ya_hay_contrasena = bool(os.environ.get("COPYLAB_LLAVE")
                             or (Path.home() / ".copylab-llave").is_file()
                             or LLAVERO.is_file())
    clave_texto = contrasena(confirmar=not ya_hay_contrasena)
    escribir_llavero({"version": 1,
                      "actualizado": date.today().strftime("%d-%m-%Y"),
                      "vars": variables,
                      "archivos": archivos}, clave_texto)
    print(f"\n✓ {LLAVERO.relative_to(RAIZ)} escrito y cifrado.")
    print("  Ahora súbelo:  git add credentials/llavero.copylab && git commit && git push")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd")

    a = sub.add_parser("abrir", help="descifra el llavero en esta máquina")
    a.add_argument("--forzar", action="store_true",
                   help="pisa los archivos que ya existan (token.json, etc.)")
    a.set_defaults(func=cmd_abrir)

    sub.add_parser("estado", help="qué credenciales tengo montadas").set_defaults(func=cmd_estado)
    sub.add_parser("ver", help="qué hay dentro del llavero (enmascarado)").set_defaults(func=cmd_ver)

    g = sub.add_parser("guardar", help="rehace el llavero desde esta máquina (solo Valeria)")
    g.add_argument("--set", action="append", metavar="CLAVE=valor",
                   help="agrega o pisa una clave a mano; se puede repetir")
    g.add_argument("--sin-google", action="store_true",
                   help="no incluye token.json ni client_secret.json")
    g.add_argument("--desde-cero", action="store_true",
                   help="ignora el llavero anterior en vez de partir de él")
    g.set_defaults(func=cmd_guardar)

    args = p.parse_args()
    if not args.cmd:
        args = p.parse_args(["estado"])
    args.func(args)


if __name__ == "__main__":
    main()
