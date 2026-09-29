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
  DtStFamilyTimeOctR5,
  DtStFamilyTimeOctR5Grafica,
  DtStFamilyTimeOctR5Guia,
  DtStFamilyTimeOctVideo,
  DtStFamilyTimeOctVideoGrafica,
  DtStFamilyTimeOctVideoGuia,
} from './compositions/hilton/DtStFamilyTimeOct';
import {DtStFamilyTimeOctR9, DtStFamilyTimeOctR9Grafica} from './compositions/hilton/DtStFamilyTimeOctR9';
import {DtStFamilyTimeOctR8, DtStFamilyTimeOctR8Grafica, DtStFamilyTimeOctR8Guia} from './compositions/hilton/DtStFamilyTimeOctR8';
import {DtStFamilyTimeOctR6, DtStFamilyTimeOctR6Grafica, DtStFamilyTimeOctR6Guia} from './compositions/hilton/DtStFamilyTimeOctR6';
import {DtFtOpinionOct, DtFtOpinionOctGuia} from './compositions/hilton/DtFtOpinionOct';
import {DtStHonorsOct, DtStHonorsOctGuia} from './compositions/hilton/DtStHonorsOct';
import {DtStServiciosOct, DtStServiciosOctGuia} from './compositions/hilton/DtStServiciosOct';

const story = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;
const feed = {durationInFrames: 1, fps: 30, width: 1080, height: 1350} as const;
const animada = {durationInFrames: DUR_FT, fps: 30, width: 1080, height: 1920} as const;

const Raiz: React.FC = () => (
  <>
    <Folder name="DT-Oct-Stories">
      {/* STORIES col C · 01-10 · ANIMADA Family Time primavera */}
      <Composition id="DT-A-Oct-FamilyTime" component={DtStFamilyTimeOct} {...animada} />
      <Composition id="DT-A-Oct-FamilyTime-Guia" component={DtStFamilyTimeOctGuia} {...animada} />
      {/* ronda 4 (28-09): la familia fija en video, todo en clips */}
      <Composition id="DT-A-Oct-FamilyTime-Video" component={DtStFamilyTimeOctVideo} {...animada} />
      <Composition id="DT-A-Oct-FamilyTime-Video-Guia" component={DtStFamilyTimeOctVideoGuia} {...animada} />
      <Composition id="DT-A-Oct-FamilyTime-Video-Grafica" component={DtStFamilyTimeOctVideoGrafica} {...animada} />
      {/* ronda 8 (28-09): familia completa (fotos expandidas) + cortina en vez de fundido */}
      <Composition id="DT-A-Oct-FamilyTime-R9" component={DtStFamilyTimeOctR9} {...animada} />
      <Composition id="DT-A-Oct-FamilyTime-R9-Grafica" component={DtStFamilyTimeOctR9Grafica} {...animada} />
      <Composition id="DT-A-Oct-FamilyTime-R8" component={DtStFamilyTimeOctR8} {...animada} />
      <Composition id="DT-A-Oct-FamilyTime-R8-Guia" component={DtStFamilyTimeOctR8Guia} {...animada} />
      <Composition id="DT-A-Oct-FamilyTime-R8-Grafica" component={DtStFamilyTimeOctR8Grafica} {...animada} />
      {/* ronda 6-7 (28-09): sólo fotos, titular fuera de la caja, bajada sutil */}
      <Composition id="DT-A-Oct-FamilyTime-R6" component={DtStFamilyTimeOctR6} {...animada} />
      <Composition id="DT-A-Oct-FamilyTime-R6-Guia" component={DtStFamilyTimeOctR6Guia} {...animada} />
      <Composition id="DT-A-Oct-FamilyTime-R6-Grafica" component={DtStFamilyTimeOctR6Grafica} {...animada} />
      {/* ronda 5 (28-09): video sólo en la 1ª toma, fotos de transición */}
      <Composition id="DT-A-Oct-FamilyTime-R5" component={DtStFamilyTimeOctR5} {...animada} />
      <Composition id="DT-A-Oct-FamilyTime-R5-Guia" component={DtStFamilyTimeOctR5Guia} {...animada} />
      <Composition id="DT-A-Oct-FamilyTime-R5-Grafica" component={DtStFamilyTimeOctR5Grafica} {...animada} />
      {/* STORIES col G · 13-10 · ESTÁTICA Servicios del hotel */}
      <Composition id="DT-S-Oct-Servicios" component={DtStServiciosOct} {...story} />
      <Composition id="DT-S-Oct-Servicios-Guia" component={DtStServiciosOctGuia} {...story} />
      {/* STORIES col L · 30-10 · ESTÁTICA Hilton Honors, recordatorio de beneficios */}
      <Composition id="DT-S-Oct-Honors" component={DtStHonorsOct} {...story} />
      <Composition id="DT-S-Oct-Honors-Guia" component={DtStHonorsOctGuia} {...story} />
    </Folder>
    <Folder name="DT-Oct-Feed">
      {/* FEED col D · 10-10 · ESTÁTICO Opinión (reseña de Google) */}
      <Composition id="DT-F-Oct-Opinion" component={DtFtOpinionOct} {...feed} />
      <Composition id="DT-F-Oct-Opinion-Guia" component={DtFtOpinionOctGuia} {...feed} />
    </Folder>
  </>
);

registerRoot(Raiz);
