// PISO18 · OCTUBRE 2026 — render de ESTÁTICAS sin el compositor de Remotion.
//
// Por qué existe: el 29-09-2026 Smart App Control de Windows empezó a bloquear
// `node_modules/@remotion/compositor-win32-x64-msvc/remotion.exe` («Una directiva de
// Control de aplicaciones bloqueó este archivo») y `renderStill` muere con
// `spawn UNKNOWN`. Las estáticas no necesitan el compositor (sólo lo usa el video):
// acá cada pieza se monta con `<Thumbnail>` de @remotion/player en una página local
// y la fotografía Chrome headless al tamaño de entrega (×2,0833).
//
// ⚠️ Sólo estáticas. Las animadas (MP4) siguen necesitando `p18-oct-rendir.mjs`.
// Si el compositor corre, usa `p18-oct-rendir.mjs`: es la vía normal.
//
//   node scripts/p18-oct-rendir-chrome.mjs F0610 F0910 S0710
import path from 'node:path';
import fs from 'node:fs';
import http from 'node:http';
import {spawn} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import esbuild from 'esbuild';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const TMP = path.join(RAIZ, 'out/piso18/oct/.chrome-render');
const ENTREGA = path.join(RAIZ, 'out/piso18/oct/entrega');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const ESCALA = 2250 / 1080;

// id → [export de P18Octubre.tsx, alto de mesa, semana, carpeta, nombre] (mismo mapa que p18-oct-rendir.mjs)
const PIEZAS = {
  'P18O-F0610': ['P18OF0610', 1350, 2, 'FEED', 'P18 FEED 06-10 Arreglos florales.png'],
  'P18O-F0910-1': ['P18OF0910S1', 1350, 2, 'FEED', 'P18 FEED 09-10 Fechas 2027 1.png'],
  'P18O-F0910-2': ['P18OF0910S2', 1350, 2, 'FEED', 'P18 FEED 09-10 Fechas 2027 2.png'],
  'P18O-S0710': ['P18OS0710', 1920, 2, 'STS', 'P18 ST 07-10 Estacion favorita.png'],
  'P18O-S0910': ['P18OS0910', 1920, 2, 'STS', 'P18 ST 09-10 Recuerdos de matrimonio.png'],
  'P18O-S1510': ['P18OS1510', 1920, 3, 'STS', 'P18 ST 15-10 Cumpleanos sonado.png'],
  'P18O-F1310-2': ['P18OF1310S2', 1350, 3, 'FEED', 'P18 FEED 13-10 Atardecer 2.png'],
  'P18O-F1610-1': ['P18OF1610S1', 1350, 3, 'FEED', 'P18 FEED 16-10 Tu proxima celebracion 1.png'],
  'P18O-S2710': ['P18OS2710', 1920, 5, 'STS', 'P18 ST 27-10 Visita virtual.png'],
  'P18O-S1510-Guia': ['P18OS1510Guia', 1920, 0, 'GUIAS', 'P18 ST 15-10 GUIA.png'],
};

const filtro = process.argv.slice(2);
const ids = Object.keys(PIEZAS).filter((id) => !filtro.length || filtro.some((f) => id.includes(f)));
if (!ids.length) throw new Error('ninguna pieza coincide');

// 1 · la página: una pieza por hash (#P18OF0610), a 1080 de ancho
fs.mkdirSync(TMP, {recursive: true});
fs.writeFileSync(
  path.join(TMP, 'entry.tsx'),
  `import React from 'react';
import {createRoot} from 'react-dom/client';
import {Thumbnail} from '@remotion/player';
import * as O from '../../../../src/compositions/piso18/P18Octubre';
const [nombre, alto] = location.hash.slice(1).split(':');
const C = (O as any)[nombre];
createRoot(document.getElementById('r')!).render(
  <Thumbnail component={C} compositionWidth={1080} compositionHeight={Number(alto)}
    frameToDisplay={0} durationInFrames={1} fps={30} style={{width: 1080, height: Number(alto)}} />,
);
// listo = fuentes cargadas + todas las <img> decodificadas, dos veces seguidas
const espera = (ms: number) => new Promise((r) => setTimeout(r, ms));
(async () => {
  for (let i = 0; i < 2; i++) {
    await espera(800);
    await document.fonts.ready;
    await Promise.all([...document.images].map((im) => im.decode().catch(() => null)));
  }
  (window as any).__listo = 1 + document.fonts.size;
})();
`,
);
fs.writeFileSync(
  path.join(TMP, 'index.html'),
  '<!doctype html><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:#000;overflow:hidden}</style><div id="r"></div><script src="/__r/entry.js"></script>',
);
await esbuild.build({
  entryPoints: [path.join(TMP, 'entry.tsx')],
  bundle: true,
  outfile: path.join(TMP, 'entry.js'),
  format: 'iife',
  jsx: 'automatic',
  loader: {'.tsx': 'tsx', '.ts': 'ts'},
  define: {'process.env.NODE_ENV': '"production"'},
  logLevel: 'error',
});

// 2 · servidor: /__r/* es la página; todo lo demás sale de public/ (lo que pide staticFile)
const TIPOS = {'.js': 'text/javascript', '.html': 'text/html', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.otf': 'font/otf', '.ttf': 'font/ttf', '.woff2': 'font/woff2', '.woff': 'font/woff', '.svg': 'image/svg+xml'};
const server = http.createServer((req, res) => {
  const u = decodeURIComponent(req.url.split('?')[0]);
  const f = u.startsWith('/__r/') ? path.join(TMP, u.slice(5)) : path.join(RAIZ, 'public', u);
  if (!fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, {'Content-Type': TIPOS[path.extname(f).toLowerCase()] || 'application/octet-stream'});
  fs.createReadStream(f).pipe(res);
});
await new Promise((ok) => server.listen(0, '127.0.0.1', ok));
const puerto = server.address().port;

// 3 · Chrome por el protocolo de depuración (CDP): esperar __listo y capturar
const perfil = path.join(TMP, 'perfil');
fs.rmSync(perfil, {recursive: true, force: true});
const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run',
  `--user-data-dir=${perfil}`, '--remote-debugging-port=0', 'about:blank'], {stdio: 'ignore'});
const espera = (ms) => new Promise((r) => setTimeout(r, ms));
let ws;
try {
  let puertoCdp;
  for (let i = 0; i < 100 && !puertoCdp; i++) {
    await espera(200);
    const f = path.join(perfil, 'DevToolsActivePort');
    if (fs.existsSync(f)) puertoCdp = fs.readFileSync(f, 'utf-8').split('\n')[0].trim();
  }
  if (!puertoCdp) throw new Error('Chrome no abrió el puerto de depuración');
  const pags = await (await fetch(`http://127.0.0.1:${puertoCdp}/json`)).json();
  ws = new WebSocket(pags.find((p) => p.type === 'page').webSocketDebuggerUrl);
  await new Promise((ok, mal) => { ws.onopen = ok; ws.onerror = mal; });
  let n = 0;
  const pend = new Map();
  ws.onmessage = (e) => {
    const m = JSON.parse(e.data);
    if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); }
  };
  const cdp = (method, params = {}) => new Promise((ok, mal) => {
    const id = ++n;
    pend.set(id, (m) => (m.error ? mal(new Error(`${method}: ${m.error.message}`)) : ok(m.result)));
    ws.send(JSON.stringify({id, method, params}));
  });
  for (const id of ids) {
    const [exp, alto, sem, carpeta, nombre] = PIEZAS[id];
    await cdp('Emulation.setDeviceMetricsOverride', {width: 1080, height: alto, deviceScaleFactor: ESCALA, mobile: false});
    await cdp('Page.navigate', {url: `http://127.0.0.1:${puerto}/__r/index.html?${Date.now()}#${exp}:${alto}`});
    let listo = null;
    for (let i = 0; i < 150 && !listo; i++) {
      await espera(200);
      const r = await cdp('Runtime.evaluate', {expression: 'window.__listo || 0', returnByValue: true});
      listo = r.result.value;
    }
    if (!listo) throw new Error(`${id}: la página no quedó lista en 30 s`);
    const {data} = await cdp('Page.captureScreenshot', {format: 'png', captureBeyondViewport: false});
    const dir = sem ? path.join(ENTREGA, `S${sem}`, carpeta) : path.join(ENTREGA, carpeta);
    fs.mkdirSync(dir, {recursive: true});
    const salida = path.join(dir, nombre);
    fs.writeFileSync(salida, Buffer.from(data, 'base64'));
    console.log("✓", path.relative(RAIZ, salida), `(${listo - 1} fuentes)`);
  }
} finally {
  try { ws?.close(); } catch {}
  chrome.kill();
  server.close();
}
