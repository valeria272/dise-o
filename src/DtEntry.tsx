/**
 * Entry point de DOUBLETREE — rinde las piezas de DT sin depender de src/Root.tsx.
 * Mismo patrón que `src/BetweenEntry.tsx`.
 *
 *   npx remotion still src/DtEntry.tsx DT-S-DiaTurismo out/pieza.png --scale=2.0833
 *
 * La mesa es 1080 de ancho y se entrega a 2250 (×2,0833), que es el máster con
 * el que Eli entrega — 66 historias ya salieron a 2250×4000.
 */
import React from 'react';
import {Composition, Folder, registerRoot} from 'remotion';

import {DtStTurismo, DtStTurismoGuia} from './compositions/hilton/DtStTurismo';

const story = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;

const Raiz: React.FC = () => (
  <>
    <Folder name="DT-Stories">
      <Composition id="DT-S-DiaTurismo" component={DtStTurismo} {...story} />
      <Composition id="DT-S-DiaTurismo-Guia" component={DtStTurismoGuia} {...story} />
    </Folder>
  </>
);

registerRoot(Raiz);
