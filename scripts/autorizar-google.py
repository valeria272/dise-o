#!/usr/bin/env python3
"""
Autoriza esta máquina contra Google y escribe `credentials/token.json`.

Para cuando tienes el **client secret** del estudio pero no el token — el caso
típico al montar el estudio en un PC nuevo sin el Mac a mano.

Abre el navegador, inicias sesión con la cuenta del estudio, aceptas los permisos
y el token queda escrito. Una sola vez por máquina.

Uso:
    python scripts/autorizar-google.py
    python scripts/autorizar-google.py --cliente ruta/al/client_secret.json

⚠️ Pide **los 6 scopes de siempre**. No recortarlos: el mismo token lo usan los
scripts de correo, calendario y planillas del monorepo, y guardar uno recortado
deja a los demás sin permisos.
"""
import argparse
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CRED = RAIZ / "credentials"

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cliente", default=None,
                    help="client_secret.json (por defecto se busca en credentials/)")
    ap.add_argument("--salida", default=str(CRED / "token.json"))
    a = ap.parse_args()

    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        sys.exit("Falta google-auth-oauthlib.  Corre:\n"
                 "    python -m pip install google-auth-oauthlib")

    if a.cliente:
        cliente = Path(a.cliente)
    else:
        candidatos = sorted(CRED.glob("client_secret*.json")) + [CRED / "credentials.json"]
        cliente = next((c for c in candidatos if c.exists()), None)

    if not cliente or not cliente.exists():
        sys.exit(
            "No encontré el client secret.\n\n"
            f"Deja el archivo del estudio en:  {CRED}\n"
            "  · se llama client_secret*.json (o credentials.json)\n"
            "  · en el Mac está en  ASISTENTE PERSONAL/credentials/\n\n"
            "Si tampoco lo tienes, el camino corto es copiar directamente el\n"
            "token.json ya autorizado desde esa misma carpeta del Mac."
        )

    CRED.mkdir(parents=True, exist_ok=True)
    print(f"Cliente: {cliente.name}")
    print("Se va a abrir el navegador. Inicia sesión con la cuenta del estudio.\n")

    flujo = InstalledAppFlow.from_client_secrets_file(str(cliente), SCOPES)
    cred = flujo.run_local_server(port=0, prompt="consent")

    faltan = set(SCOPES) - set(cred.scopes or [])
    if faltan:
        sys.exit(f"⛔ Google devolvió un token RECORTADO. Faltan: {faltan}\n"
                 "No se guarda: degradaría el token del resto del monorepo.")

    salida = Path(a.salida)
    salida.write_text(cred.to_json(), encoding="utf-8")
    print(f"\n✓ Token escrito en {salida}")
    print("Compruébalo con:  python scripts/_entorno.py")


if __name__ == "__main__":
    main()
