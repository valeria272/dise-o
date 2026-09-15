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

import {
  DtStFiestasPatrias,
  DtStFiestasPatriasGuia,
} from './compositions/hilton/DtStFiestasPatrias';
import {DtStTurismo, DtStTurismoGuia} from './compositions/hilton/DtStTurismo';

const story = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;

const Raiz: React.FC = () => (
  <>
    <Folder name="DT-Stories">
      {/*
        ⭐ Eli aprobó la variante A (escuadras) el 10-09. La variante B —sólo
        las dos horizontales— queda descartada y se retiró: dejarla registrada
        es dejar a mano la pieza que NO se entrega.
      */}
      <Composition id="DT-S-DiaTurismo" component={DtStTurismo} {...story} />
      <Composition id="DT-S-DiaTurismo-Guia" component={DtStTurismoGuia} {...story} />

      {/*
        STORIES col H · 18-09 · SALUDO FIESTAS PATRIAS.
        ⭐ RONDA 2: Eli mandó la referencia armada y la pieza pasó a ser un
        COLLAGE, con el titular en itálica y el logotipo abajo. Las dos variantes
        de la ronda 1 —regla corta y escuadras— quedaron sin efecto y se
        retiraron: dejarlas registradas es dejar a mano la pieza que no se entrega.
      */}
      <Composition id="DT-S-FiestasPatrias" component={DtStFiestasPatrias} {...story} />
      <Composition
        id="DT-S-FiestasPatrias-Guia"
        component={DtStFiestasPatriasGuia}
        {...story}
      />
    </Folder>
  </>
);

registerRoot(Raiz);
