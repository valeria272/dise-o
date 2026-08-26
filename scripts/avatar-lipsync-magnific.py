"""Prueba real: lipsync LatentSync (API Magnific) sobre el video base de Valeria.
Sube los dos archivos a Drive (token compartido, scopes completos), los hace públicos por enlace,
manda el job a Magnific, espera y descarga el resultado.
"""
import json, os, sys, time, mimetypes
from pathlib import Path
import certifi, requests
os.environ.setdefault("SSL_CERT_FILE", certifi.where())
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _entorno import RAIZ as _RAIZ, token_google as _token_google, env_compartido as _env_compartido


S = Path(__file__).parent
VIDEO = S / sys.argv[1] if len(sys.argv) > 1 else S / "test_base_720_15s.mp4"
AUDIO = S / sys.argv[2] if len(sys.argv) > 2 else S / "test_voz_real_30-45.mp3"
OUT = S / (sys.argv[3] if len(sys.argv) > 3 else "resultado_latentsync.mp4")

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]
TOKEN = str(_token_google())
KEY = Path("~/.magnific_key").expanduser().read_text().strip()
API = "https://api.magnific.com/v1/ai/lip-sync/latent-sync"


def drive():
    c = Credentials.from_authorized_user_file(TOKEN, SCOPES)
    if not c.valid:
        c.refresh(Request())
        if set(SCOPES) - set(c.scopes or []):
            sys.exit("ABORTA: el refresco perdió scopes")
        json.dump(json.loads(c.to_json()), open(TOKEN, "w"), indent=2)
    return build("drive", "v3", credentials=c, cache_discovery=False)


def subir_publico(d, path: Path) -> str:
    mt = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
    f = d.files().create(body={"name": f"avatar-test-{path.name}"},
                         media_body=MediaFileUpload(str(path), mimetype=mt, resumable=False),
                         fields="id").execute()
    fid = f["id"]
    d.permissions().create(fileId=fid, body={"type": "anyone", "role": "reader"}).execute()
    url = f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t"
    r = requests.get(url, stream=True, timeout=60)
    ct = r.headers.get("content-type", "")
    print(f"  subido {path.name} → {fid} ({ct})")
    if not (ct.startswith("video") or ct.startswith("audio") or "octet" in ct):
        sys.exit(f"El enlace directo no entrega el archivo (content-type {ct})")
    return url, fid


def main():
    d = drive()
    print("→ subiendo a Drive…")
    video_url, vid = subir_publico(d, VIDEO)
    audio_url, aid = subir_publico(d, AUDIO)

    print("→ enviando a Magnific LatentSync…")
    r = requests.post(API, headers={"x-magnific-api-key": KEY, "Content-Type": "application/json"},
                      json={"video_url": video_url, "audio_url": audio_url}, timeout=120)
    print("  ", r.status_code, r.text[:400])
    r.raise_for_status()
    task = r.json()["data"]["task_id"]

    t0 = time.time()
    while True:
        time.sleep(10)
        s = requests.get(f"{API}/{task}", headers={"x-magnific-api-key": KEY}, timeout=60)
        if s.status_code >= 400:
            print("  poll", s.status_code, s.text[:300]); continue
        data = s.json()["data"]
        st = data.get("status")
        print(f"  [{time.time()-t0:4.0f}s] {st}")
        if st == "COMPLETED":
            urls = data.get("generated") or []
            break
        if st == "FAILED":
            sys.exit(f"FALLÓ: {json.dumps(data)[:500]}")
        if time.time() - t0 > 1500:
            sys.exit("timeout")
    if not urls:
        sys.exit("sin salida")
    with requests.get(urls[0], stream=True, timeout=600) as g:
        g.raise_for_status()
        OUT.write_bytes(g.content)
    print(f"✅ resultado → {OUT} ({OUT.stat().st_size/1e6:.1f} MB)")
    # limpiar Drive
    for fid in (vid, aid):
        try:
            d.files().delete(fileId=fid).execute()
        except Exception as e:
            print("  no pude borrar", fid, e)
    json.dump({"task": task, "video": str(VIDEO), "audio": str(AUDIO), "out": str(OUT), "urls": urls},
              open(OUT.with_suffix(".json"), "w"), indent=1)


if __name__ == "__main__":
    main()
