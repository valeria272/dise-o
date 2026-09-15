/**
 * Entry point de PISO18 — rinde las piezas de la marca sin depender de
 * `src/Root.tsx`. Mismo patrón que `src/DtEntry.tsx` y `src/BetweenEntry.tsx`.
 *
 *   npx remotion still src/P18Entry.tsx P18-ST-LuzVista out/pieza.png --scale=2.0833
 *
 * ⭐ La mesa es 1080 de ancho y se entrega a **2250** (×2,0833), que es el máster
 * medido sobre las piezas APROBADAS de la cuenta: la historia `ST N°1 S1.png` es
 * 2250×4000 y el carrusel `C2 S1 n°*.png` es 2250×2813.
 *
 * ⚠️ Esto CORRIGE la lectura de los `.ai`, cuya mesa de trabajo es 1080×1350:
 * el editable se arma a 1080 pero lo aprobado y publicado se entrega a 2250.
 *
 * ⛔ Piso18 es marca propia: nada de DoubleTree se le traspasa, ni al revés.
 */
import React from 'react';
import {Composition, Folder, registerRoot} from 'remotion';

import {P18StLuzVista, P18StLuzVistaGuia} from './compositions/piso18/P18StLuzVista';
import {P18StEncuesta, P18StEncuestaGuia} from './compositions/piso18/P18StEncuesta';
import {
  P18StMontaje,
  P18StMontajeGuia,
  P18_MONTAJE_DUR,
  P18_MONTAJE_FPS,
} from './compositions/piso18/P18StMontaje';

const story = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;

const Raiz: React.FC = () => (
  <>
    <Folder name="P18-Stories">
      {/* STORIES col L · 22-09 18:00 · ST ESTÁTICA «LA LUZ DE LA VISTA» */}
      <Composition id="P18-ST-LuzVista" component={P18StLuzVista} {...story} />
      <Composition id="P18-ST-LuzVista-Guia" component={P18StLuzVistaGuia} {...story} />

      {/* STORIES col N · 25-09 12:00 · ST ESTÁTICA «ENCUESTA MESA IDEAL» */}
      <Composition id="P18-ST-Encuesta" component={P18StEncuesta} {...story} />
      <Composition id="P18-ST-Encuesta-Guia" component={P18StEncuestaGuia} {...story} />

      {/* STORIES col M · 23-09 18:00 · ST ANIMADA «TIMELAPSE MONTAJE» */}
      <Composition
        id="P18-ST-Montaje"
        component={P18StMontaje}
        durationInFrames={P18_MONTAJE_DUR}
        fps={P18_MONTAJE_FPS}
        width={1080}
        height={1920}
      />
      <Composition
        id="P18-ST-Montaje-Guia"
        component={P18StMontajeGuia}
        durationInFrames={P18_MONTAJE_DUR}
        fps={P18_MONTAJE_FPS}
        width={1080}
        height={1920}
      />
    </Folder>
  </>
);

registerRoot(Raiz);
