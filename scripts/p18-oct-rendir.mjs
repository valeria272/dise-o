// PISO18 · OCTUBRE 2026 — rinde las estáticas en UN solo empaquetado (19 `remotion still`
// seguidos re-empaquetan 19 veces). Nombres de entrega: convención del portal
// (`docs/PORTAL-VALIDACIONES.html`): `P18 FEED DD-MM Tema N.png` / `P18 ST DD-MM Tema.png`.
//
//   node scripts/p18-oct-rendir.mjs                 # todas, máster ×2,0833 → out/piso18/oct/entrega
//   node scripts/p18-oct-rendir.mjs --borrador      # ×0,5 → out/piso18/oct/borrador
//   node scripts/p18-oct-rendir.mjs F1610 S0910     # sólo las que contengan esos textos
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import fs from 'node:fs';
import {bundle} from '@remotion/bundler';
import {openBrowser, renderStill, selectComposition} from '@remotion/renderer';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const borrador = args.includes('--borrador');
const filtro = args.filter((a) => !a.startsWith('--'));
const escala = borrador ? 0.5 : 2250 / 1080;
const base = path.join(RAIZ, 'out/piso18/oct', borrador ? 'borrador' : 'entrega');

// id → [semana, carpeta, nombre]. La semana es la de la GRILLA de Piso18 (fila 7).
const PIEZAS = {
  'P18O-F0610': [2, 'FEED', 'P18 FEED 06-10 Arreglos florales.png'],
  'P18O-F0910-1': [2, 'FEED', 'P18 FEED 09-10 Fechas 2027 1.png'],
  'P18O-F0910-2': [2, 'FEED', 'P18 FEED 09-10 Fechas 2027 2.png'],
  'P18O-F1310-1': [3, 'FEED', 'P18 FEED 13-10 Atardecer 1.png'],
  'P18O-F1310-2': [3, 'FEED', 'P18 FEED 13-10 Atardecer 2.png'],
  'P18O-F1610-1': [3, 'FEED', 'P18 FEED 16-10 Tu proxima celebracion 1.png'],
  'P18O-F1610-2': [3, 'FEED', 'P18 FEED 16-10 Tu proxima celebracion 2.png'],
  'P18O-F1610-3': [3, 'FEED', 'P18 FEED 16-10 Tu proxima celebracion 3.png'],
  'P18O-F1610-4': [3, 'FEED', 'P18 FEED 16-10 Tu proxima celebracion 4.png'],
  'P18O-F1610-5': [3, 'FEED', 'P18 FEED 16-10 Tu proxima celebracion 5.png'],
  'P18O-F2310-1': [4, 'FEED', 'P18 FEED 23-10 Estacion Tex Mex 1.png'],
  'P18O-F2310-2': [4, 'FEED', 'P18 FEED 23-10 Estacion Tex Mex 2.png'],
  'P18O-F2310-3': [4, 'FEED', 'P18 FEED 23-10 Estacion Tex Mex 3.png'],
  'P18O-F2310-4': [4, 'FEED', 'P18 FEED 23-10 Estacion Tex Mex 4.png'],
  'P18O-F2710': [5, 'FEED', 'P18 FEED 27-10 Wedding planner.png'],
  'P18O-S0710': [2, 'STS', 'P18 ST 07-10 Estacion favorita.png'],
  'P18O-S0910': [2, 'STS', 'P18 ST 09-10 Recuerdos de matrimonio.png'],
  'P18O-S2310': [4, 'STS', 'P18 ST 23-10 Evento corporativo.png'],
  'P18O-S2710': [5, 'STS', 'P18 ST 27-10 Visita virtual.png'],
  // la estática de la animada (último fotograma) y las guías de QA, que NO se suben
  'P18O-S0510': [2, 'STS', 'P18 ST 05-10 Primavera en Piso18 portada.png', 299],
  'P18O-S0710-Guia': [0, 'GUIAS', 'P18 ST 07-10 GUIA.png'],
  'P18O-S0910-Guia': [0, 'GUIAS', 'P18 ST 09-10 GUIA.png'],
  'P18O-S2310-Guia': [0, 'GUIAS', 'P18 ST 23-10 GUIA.png'],
  'P18O-S2710-Guia': [0, 'GUIAS', 'P18 ST 27-10 GUIA.png'],
};

const serveUrl = await bundle({entryPoint: path.join(RAIZ, 'src/P18OctEntry.tsx')});
// un solo navegador para todo el lote: abrir uno por cuadro se colgó en el 17.º (28-09)
const puppeteerInstance = await openBrowser('chrome');
for (const [id, [sem, carpeta, nombre, frame = 0]] of Object.entries(PIEZAS)) {
  if (filtro.length && !filtro.some((f) => id.includes(f))) continue;
  const dir = sem ? path.join(base, `S${sem}`, carpeta) : path.join(base, carpeta);
  fs.mkdirSync(dir, {recursive: true});
  const composition = await selectComposition({serveUrl, id, puppeteerInstance});
  const output = path.join(dir, nombre);
  await renderStill({composition, serveUrl, output, frame, scale: escala, imageFormat: 'png', puppeteerInstance, timeoutInMilliseconds: 120000});
  console.log('✓', path.relative(RAIZ, output));
}
await puppeteerInstance.close({silent: true});
