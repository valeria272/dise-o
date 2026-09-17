/**
 * Entry point de QB RESTAURANT — rinde las piezas de la marca sin depender de
 * `src/Root.tsx`. Mismo patrón que `src/P18Entry.tsx` y `src/DtEntry.tsx`.
 *
 *   npx remotion render src/QbEntry.tsx QB-ST-AYCD-S5 out/qb/st-aycd-28-09.mp4 --scale=2.0833
 *   npx remotion still  src/QbEntry.tsx QB-ST-AYCD-S5 out/qb/ultimo.png --frame=239 --scale=2.0833
 *
 * ⭐ La mesa es 1080×1920 y se entrega a **2250×4000** (×2,0833), que es el
 * máster medido sobre las historias aprobadas de QB.
 *
 * ⛔ QB es marca INDEPENDIENTE: nada de DoubleTree, Between ni Piso18 se le
 * traspasa, ni al revés (Eli, 15-09-2026).
 */
import React from "react";
import {Composition, Folder, registerRoot} from "remotion";

import {
  QBStAycdS5,
  QB_ST_AYCD_S5_DURACION,
  QB_ST_AYCD_S5_FPS,
} from "./compositions/qb/QBStAycdS5";
import {QBPantallaAycd, QB_PANTALLA} from "./compositions/qb/QBPantallaAycd";

const Raiz: React.FC = () => (
  <>
    <Folder name="QB-Stories">
      {/* STORIES · 28-09 15:00 · ST ANIMADA «ALL YOU CAN DRINK» */}
      <Composition
        id="QB-ST-AYCD-S5"
        component={QBStAycdS5}
        durationInFrames={QB_ST_AYCD_S5_DURACION}
        fps={QB_ST_AYCD_S5_FPS}
        width={1080}
        height={1920}
      />
    </Folder>

    <Folder name="QB-Insumos">
      {/* La gráfica que va DENTRO del celular. No es entrega: se rinde como
          still y se pega en perspectiva con scripts/qb-aycd-s5-montar.py */}
      <Composition
        id="QB-Pantalla-AYCD"
        component={QBPantallaAycd}
        durationInFrames={1}
        fps={30}
        width={QB_PANTALLA.w}
        height={QB_PANTALLA.h}
      />
    </Folder>
  </>
);

registerRoot(Raiz);
