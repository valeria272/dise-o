"""Imagen fija de una composición SIN el compositor de Remotion (`remotion.exe`).

Por qué existe: el 29-09-2026 el Control de aplicaciones de Windows empezó a bloquear
`node_modules/@remotion/compositor-win32-x64-msvc/remotion.exe` («Una directiva de Control
de aplicaciones bloqueó este archivo») y `npx remotion still` muere con `spawn UNKNOWN`.
Una imagen fija de sólo imágenes y texto no necesita el compositor: se arma el paquete
web (`remotion bundle`, webpack puro), se le inyecta lo mismo que inyecta el renderer
antes de cargar (`set-props-and-env.js` + `remotion_setBundleMode` de `render-still.js`)
y se captura con el Chrome del sistema en headless.

⚠️ No sirve para composiciones con <Video>/<OffthreadVideo> (ésas sí piden el compositor).

    py scripts/still-por-chrome.py src/DtOct3Entry.tsx DT-C-Oct-Escapada-1 '{"lamina":1}' out/x.png \
        --ancho 1080 --alto 1350 --escala 2.0833 --publico assets/hilton/dt/fonts assets/hilton/dt/oct3 ...
"""
import argparse, functools, http.server, json, os, shutil, subprocess, threading
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TMP = RAIZ / "raw/_still-chrome"

a = argparse.ArgumentParser()
a.add_argument("entry"); a.add_argument("id"); a.add_argument("props"); a.add_argument("salida", nargs="+")
a.add_argument("--ancho", type=int, default=1080); a.add_argument("--alto", type=int, default=1350)
a.add_argument("--escala", type=float, default=1.0)
a.add_argument("--publico", nargs="*", default=[], help="rutas de public/ que usa la pieza (archivos o carpetas)")
a.add_argument("--sin-bundle", action="store_true", help="reusar el paquete ya armado")
g = a.parse_args()

# el id y los props pueden repetirse con «|» para sacar varias láminas del mismo paquete
ids, props = g.id.split("|"), g.props.split("|")
assert len(ids) == len(props) == len(g.salida), "id, props y salida tienen que ir en la misma cantidad"

pub, paquete = TMP / "public", TMP / "bundle"
if not g.sin_bundle:
    shutil.rmtree(TMP, ignore_errors=True)
    pub.mkdir(parents=True)
    for r in g.publico:
        src, dst = RAIZ / "public" / r, pub / r
        dst.parent.mkdir(parents=True, exist_ok=True)
        (shutil.copytree if src.is_dir() else shutil.copy2)(src, dst)
    subprocess.run(f'npx remotion bundle "{g.entry}" --public-dir="{pub}" --out-dir="{paquete}"',
                   shell=True, cwd=RAIZ, check=True, capture_output=True)

INICIO = """<script>
window.remotion_puppeteerTimeout=30000;window.remotion_isMainTab=true;window.remotion_mediaCacheSizeInBytes=null;
window.remotion_initialMemoryAvailable=8e9;window.remotion_sampleRate=48000;
window.process=window.process||{};window.process.env=window.process.env||{};window.process.env.NODE_ENV='production';
window.remotion_broadcastChannel=new BroadcastChannel('remotion-video-frame-extraction');
window.remotion_envVariables='{}';window.remotion_inputProps='{}';window.remotion_initialFrame=0;window.remotion_attempt=1;
window.remotion_proxyPort=0;window.remotion_audioEnabled=false;window.remotion_videoEnabled=true;window.remotion_logLevel='info';
</script>"""
FIN = """<style>html,body{margin:0;overflow:hidden;background:transparent}</style><script>
(function go(){if(!window.remotion_setBundleMode){return setTimeout(go,30);}
window.remotion_setBundleMode({type:'composition',compositionName:%(id)s,serializedResolvedPropsWithSchema:%(props)s,
compositionDurationInFrames:1,compositionFps:30,compositionHeight:%(alto)d,compositionWidth:%(ancho)d,
compositionDefaultCodec:null,compositionDefaultOutName:null,compositionDefaultVideoImageFormat:null,
compositionDefaultPixelFormat:null,compositionDefaultProResProfile:null,compositionDefaultSampleRate:48000});
(function f(){if(window.remotion_setFrame){window.remotion_setFrame(0,%(id)s,1);}else{setTimeout(f,30);}})();})();
</script>"""

base = (paquete / "index.html").read_text(encoding="utf-8")
Manejador = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(paquete))
Manejador.log_message = lambda *x: None
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Manejador)
threading.Thread(target=srv.serve_forever, daemon=True).start()
puerto = srv.server_address[1]

for cid, pr, sal in zip(ids, props, g.salida):
    html = base.replace("<body>", "<body>" + INICIO, 1).replace(
        "</body>", FIN % {"id": json.dumps(cid), "props": json.dumps(pr), "ancho": g.ancho, "alto": g.alto} + "</body>", 1)
    (paquete / "still.html").write_text(html, encoding="utf-8")
    sal = (RAIZ / sal).resolve()
    sal.parent.mkdir(parents=True, exist_ok=True)
    perfil = TMP / "perfil"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={perfil}",
                    f"--window-size={g.ancho},{g.alto}", f"--force-device-scale-factor={g.escala}",
                    "--virtual-time-budget=20000", "--run-all-compositor-stages-before-draw",
                    f"--screenshot={sal}", f"http://127.0.0.1:{puerto}/still.html"],
                   capture_output=True, timeout=180)
    print("ok" if sal.exists() else "FALLÓ", sal.relative_to(RAIZ))
srv.shutdown()
