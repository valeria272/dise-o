/**
 * Entry de DOUBLETREE · OCTUBRE 2026 — las piezas OK PARA DISEÑO de la grilla
 * `13yYW5QacnSRaV422SeBTgFVGwLN5mhTg0anDJzkvaK0`. Mismo patrón que
 * `src/BetweenOctEntry.tsx`: entry propio para no tocar el de septiembre.
 *
 *   npx remotion still src/DtOctEntry.tsx DT-S-Oct-Servicios out/x.png --scale=2.0833
 *   npx remotion render src/DtOctEntry.tsx DT-A-Oct-FamilyTime out/x.mp4
 */
import React from 'react';
import {Composition, Folder, registerRoot} from 'remotion';

import {
  DURACION as DUR_FT,
  DtStFamilyTimeOct,
  DtStFamilyTimeOctGuia,
} from './compositions/hilton/DtStFamilyTimeOct';
import {DtStHonorsOct, DtStHonorsOctGuia} from './compositions/hilton/DtStHonorsOct';
import {DtStServiciosOct, DtStServiciosOctGuia} from './compositions/hilton/DtStServiciosOct';

const story = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;
const animada = {durationInFrames: DUR_FT, fps: 30, width: 1080, height: 1920} as const;

const Raiz: React.FC = () => (
  <>
    <Folder name="DT-Oct-Stories">
      {/* STORIES col C · 01-10 · ANIMADA Family Time primavera */}
      <Composition id="DT-A-Oct-FamilyTime" component={DtStFamilyTimeOct} {...animada} />
      <Composition id="DT-A-Oct-FamilyTime-Guia" component={DtStFamilyTimeOctGuia} {...animada} />
      {/* STORIES col G · 13-10 · ESTÁTICA Servicios del hotel */}
      <Composition id="DT-S-Oct-Servicios" component={DtStServiciosOct} {...story} />
      <Composition id="DT-S-Oct-Servicios-Guia" component={DtStServiciosOctGuia} {...story} />
      {/* STORIES col L · 30-10 · ESTÁTICA Hilton Honors, recordatorio de beneficios */}
      <Composition id="DT-S-Oct-Honors" component={DtStHonorsOct} {...story} />
      <Composition id="DT-S-Oct-Honors-Guia" component={DtStHonorsOctGuia} {...story} />
    </Folder>
  </>
);

registerRoot(Raiz);
