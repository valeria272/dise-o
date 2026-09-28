/**
 * Entry de DOUBLETREE · OCTUBRE 2026, segunda tanda — las 6 piezas que pasaron a
 * OK PARA DISEÑO el 28-09 (grilla `13yYW5QacnSRaV422SeBTgFVGwLN5mhTg0anDJzkvaK0`).
 * Entry propio, igual que `src/DtOctEntry.tsx`, para no tocar lo ya entregado.
 *
 *   npx remotion still src/DtOct2Entry.tsx DT-S-Oct-FeriadoPlanes out/x.png --scale=2.0833
 */
import React from 'react';
import {Composition, Folder, registerRoot} from 'remotion';

import {DtC5CosasOct} from './compositions/hilton/DtC5CosasOct';
import {DURACION as DUR_CW, DtStCoworkOct, DtStCoworkOctGuia} from './compositions/hilton/DtStCoworkOct';
import {DtFtFamilyTimeOct} from './compositions/hilton/DtFtFamilyTimeOct';
import {DtStFeriadoEr, DtStFeriadoFt, DtStFeriadoPlanes, DtStFeriadoPlanesGuia} from './compositions/hilton/DtStFeriadoOct';

const feed = {durationInFrames: 1, fps: 30, width: 1080, height: 1350} as const;
const animada = {durationInFrames: DUR_CW, fps: 30, width: 1080, height: 1920} as const;
const story = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;

const Raiz: React.FC = () => (
  <>
    <Folder name="DT-Oct2-Stories">
      {/* STORIES col E · 05-10 · feriado ER + FT */}
      <Composition id="DT-S-Oct-FeriadoPlanes" component={DtStFeriadoPlanes} {...story} />
      <Composition id="DT-S-Oct-FeriadoPlanes-Guia" component={DtStFeriadoPlanesGuia} {...story} />
      {/* STORIES col F · 05-10 · feriado Escapada Romántica */}
      <Composition id="DT-S-Oct-FeriadoER" component={DtStFeriadoEr} {...story} />
      {/* STORIES col G · 05-10 · feriado Family Time */}
      <Composition id="DT-S-Oct-FeriadoFT" component={DtStFeriadoFt} {...story} />
      {/* STORIES col K · 22-10 · ANIMADA Coworking */}
      <Composition id="DT-A-Oct-Cowork" component={DtStCoworkOct} {...animada} />
      <Composition id="DT-A-Oct-Cowork-Guia" component={DtStCoworkOctGuia} {...animada} />
    </Folder>
    <Folder name="DT-Oct2-Feed">
      {/* FEED col J · 28-10 · ESTÁTICO Family Time primavera */}
      <Composition id="DT-F-Oct-FamilyTime" component={DtFtFamilyTimeOct} {...feed} />
      {/* FEED col H · 21-10 · CARRUSEL «5 cosas» (7 láminas) */}
      {[1, 2, 3, 4, 5, 6, 7].map((n) => (
        <Composition key={n} id={`DT-C-Oct-5Cosas-${n}`} component={DtC5CosasOct} defaultProps={{lamina: n}} {...feed} />
      ))}
      <Composition id="DT-C-Oct-5Cosas-1B" component={DtC5CosasOct} defaultProps={{lamina: 1, fondo: 'b' as const}} {...feed} />
    </Folder>
  </>
);

registerRoot(Raiz);
