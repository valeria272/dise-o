/**
 * Entry de DOUBLETREE · OCTUBRE 2026, tercera tanda — el carrusel Escapada Romántica
 * del 07-10, que pasó a OK PARA DISEÑO el 28-09 20:08Z (grilla `13yYW5QacnSRaV422SeBTgFVGwLN5mhTg0anDJzkvaK0`).
 * Entry propio, como `src/DtOct2Entry.tsx`, para no tocar lo ya entregado.
 *
 *   npx remotion still src/DtOct3Entry.tsx DT-C-Oct-Escapada-1 out/x.png --scale=2.0833
 */
import React from 'react';
import {Composition, Folder, registerRoot} from 'remotion';

import {DtCEscapadaOct} from './compositions/hilton/DtCEscapadaOct';

const feed = {durationInFrames: 1, fps: 30, width: 1080, height: 1350} as const;

const Raiz: React.FC = () => (
  <Folder name="DT-Oct3-Feed">
    {/* FEED col C · 07-10 · CARRUSEL Escapada Romántica (2 láminas) */}
    {[1, 2].map((n) => (
      <Composition key={n} id={`DT-C-Oct-Escapada-${n}`} component={DtCEscapadaOct} defaultProps={{lamina: n}} {...feed} />
    ))}
  </Folder>
);

registerRoot(Raiz);
