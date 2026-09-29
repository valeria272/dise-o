// Video de una composición SIN el compositor de Remotion (`remotion.exe` bloqueado por
// el Control de aplicaciones de Windows desde el 29-09-2026).
//
// Mismo método que `p18-oct-rendir-chrome.mjs` (Thumbnail de @remotion/player en una
// página local + Chrome headless por CDP), pero fotograma a fotograma: la página expone
// `__ir(n)`, que re-rinde el Thumbnail en el fotograma n y avisa cuando las fuentes y
// las imágenes están listas. Salen PNG numerados; el MP4 lo arma ffmpeg aparte.
//
// ⚠️ Sólo imágenes, texto y SVG. <Video>/<OffthreadVideo>/<Audio> no.
//
//   node scripts/reel-por-chrome.mjs <archivo.tsx> <Export> <ancho> <alto> <duracion> <carpeta> [--solo 0,40,120]
import path from 'node:path';
import fs from 'node:fs';
import http from 'node:http';
import {spawn} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import esbuild from 'esbuild';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const [archivo, exp, ancho, alto, duracion, carpeta] = process.argv.slice(2);
const iSolo = process.argv.indexOf('--solo');
const solo = iSolo > 0 ? process.argv[iSolo + 1].split(',').map(Number) : null;
const W = Number(ancho), H = Number(alto), N = Number(duracion);
const SALIDA = path.resolve(RAIZ, carpeta);
const TMP = path.join(RAIZ, 'raw/_reel-chrome');
fs.mkdirSync(TMP, {recursive: true});
fs.mkdirSync(SALIDA, {recursive: true});

const rel = path.relative(TMP, path.resolve(RAIZ, archivo)).replaceAll('\\', '/').replace(/\.tsx$/, '');
fs.writeFileSync(path.join(TMP, 'entry.tsx'), `import React from 'react';
import {flushSync} from 'react-dom';
import {createRoot} from 'react-dom/client';
import {Thumbnail} from '@remotion/player';
import {${exp} as C} from '${rel}';
const root = createRoot(document.getElementById('r')!);
const pinta = (n: number) => flushSync(() => root.render(
  <Thumbnail component={C} compositionWidth={${W}} compositionHeight={${H}}
    frameToDisplay={n} durationInFrames={${N}} fps={30} style={{width: ${W}, height: ${H}}} />));
const espera = (ms: number) => new Promise((r) => setTimeout(r, ms));
const cuadro = () => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));
(window as any).__ir = async (n: number) => {
  (window as any).__listo = 0;
  pinta(n);
  await document.fonts.ready;
  await Promise.all([...document.images].map((im) => im.decode().catch(() => null)));
  await cuadro();
  (window as any).__listo = 1;
};
(async () => { pinta(0); for (let i = 0; i < 2; i++) { await espera(800); await document.fonts.ready;
  await Promise.all([...document.images].map((im) => im.decode().catch(() => null))); }
  (window as any).__arranco = 1; })();
`);
fs.writeFileSync(path.join(TMP, 'index.html'),
  '<!doctype html><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:#000;overflow:hidden}</style><div id="r"></div><script src="/__r/entry.js"></script>');
await esbuild.build({
  entryPoints: [path.join(TMP, 'entry.tsx')], bundle: true, outfile: path.join(TMP, 'entry.js'), format: 'iife',
  jsx: 'automatic', loader: {'.tsx': 'tsx', '.ts': 'ts'}, define: {'process.env.NODE_ENV': '"production"'}, logLevel: 'error',
});

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
  ws.onmessage = (e) => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); } };
  const cdp = (method, params = {}) => new Promise((ok, mal) => {
    const id = ++n;
    pend.set(id, (m) => (m.error ? mal(new Error(`${method}: ${m.error.message}`)) : ok(m.result)));
    ws.send(JSON.stringify({id, method, params}));
  });
  const valor = async (expr) => (await cdp('Runtime.evaluate', {expression: expr, returnByValue: true, awaitPromise: true})).result.value;
  await cdp('Emulation.setDeviceMetricsOverride', {width: W, height: H, deviceScaleFactor: 1, mobile: false});
  await cdp('Page.navigate', {url: `http://127.0.0.1:${puerto}/__r/index.html?${Date.now()}`});
  for (let i = 0; i < 150 && !(await valor('window.__arranco || 0')); i++) await espera(200);
  const faltan = await valor(`[...document.fonts].filter(f => f.status !== 'loaded').map(f => f.family).join(',')`);
  if (faltan) console.warn('⚠️ fuentes sin cargar:', faltan);
  const cuadros = solo ?? [...Array(N).keys()];
  const t0 = Date.now();
  for (const k of cuadros) {
    await valor(`window.__ir(${k})`);
    const {data} = await cdp('Page.captureScreenshot', {format: 'png'});
    fs.writeFileSync(path.join(SALIDA, `f${String(k).padStart(4, '0')}.png`), Buffer.from(data, 'base64'));
    if (k % 50 === 0) console.log(`  ${k}/${N}  ${((Date.now() - t0) / 1000).toFixed(0)} s`);
  }
  console.log(`✓ ${cuadros.length} fotogramas en ${path.relative(RAIZ, SALIDA)}`);
} finally {
  try { ws?.close(); } catch {}
  chrome.kill();
  server.close();
}
