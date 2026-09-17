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
  DURACION as DUR_C1S5,
  DtC1S5Desayuno,
  DtC1S5Gym,
  DtC1S5Habitacion,
  DtC1S5Lobby,
  DtC1S5Portada,
  DtC1S5Salon,
} from './compositions/hilton/DtC1S5Dia';
import {DtFtHonors, DtFtHonorsGuia} from './compositions/hilton/DtFtHonors';
import {
  DtStFiestasPatrias,
  DtStFiestasPatriasGuia,
} from './compositions/hilton/DtStFiestasPatrias';
import {
  DURACION as DUR_PRUEBA,
  DtStPruebaAntes,
  DtStPruebaDespues,
  DtStPruebaGuia,
} from './compositions/hilton/DtStPrueba';
import {DtStTurismo, DtStTurismoGuia} from './compositions/hilton/DtStTurismo';

const story = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;
/**
 * FEED 4:5. La mesa es 1080×1350 y se entrega a 2250 de ancho (×2,0833), que es
 * el máster de las tres piezas aprobadas de la cuenta y el de la plantilla de
 * márgenes `logo-post.png`.
 */
const feed = {durationInFrames: 1, fps: 30, width: 1080, height: 1350} as const;
/**
 * FEED 4:5 en VIDEO — el carrusel animado de la S5.
 *
 * ⚠️ Acá el máster **no** es 2250: Instagram entrega video a 1080 de ancho y
 * vuelve a comprimir cualquier cosa más grande. Se rinde 1080×1350 directo,
 * sin `--scale`.
 *
 * 150 frames a 30 fps = **5,0 s**, bajo el tope de 6 s que puso Eli.
 */
const feedVideo = {
  durationInFrames: DUR_C1S5,
  fps: 30,
  width: 1080,
  height: 1350,
} as const;

/**
 * BANCO DE PRUEBAS — la ST que mandó Eli el 17-09 para ver si su edición de
 * Premiere se puede mejorar desde código. **No es pieza de grilla.**
 * 289 fotogramas a 30 fps = 9,64 s, la duración exacta del .prproj.
 */
const pruebaSt = {
  durationInFrames: DUR_PRUEBA,
  fps: 30,
  width: 1080,
  height: 1920,
} as const;

const Raiz: React.FC = () => (
  <>
    <Folder name="DT-Prueba-ST">
      {/*
        ⚠️ NO ES GRILLA. Es el banco de pruebas del 17-09: la misma historia con
        la edición de Premiere reconstruida (`Antes`) y con la edición nueva
        (`Despues`). Mismas fotos, mismos textos, misma diagramación — lo único
        que cambia es la edición, para que la comparación aísle eso.
      */}
      <Composition id="DT-Prueba-Antes" component={DtStPruebaAntes} {...pruebaSt} />
      <Composition id="DT-Prueba-Despues" component={DtStPruebaDespues} {...pruebaSt} />
      <Composition id="DT-Prueba-Guia" component={DtStPruebaGuia} {...pruebaSt} />
    </Folder>

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

    <Folder name="DT-Feed">
      {/*
        FEED col K · 23-09 18:00 · ESTÁTICO HILTON HONORS, estado OK PARA DISEÑO.
        La referencia es `Ref post s4.jpg`, que Eli subió a REFERENCIAS S4 DT el
        15-09 a las 13:43 — y que resulta ser el mismo pin que enlaza el brief.
      */}
      <Composition id="DT-F-HiltonHonors" component={DtFtHonors} {...feed} />
      <Composition id="DT-F-HiltonHonors-Guia" component={DtFtHonorsGuia} {...feed} />
    </Folder>

    <Folder name="DT-Carrusel-S5">
      {/*
        FEED col M · 28-09 12:00 · CARRUSEL DE VIDEOS «TU DÍA EN DOUBLETREE».
        Estado de la grilla: REVISAR CONTENIDO.

        Las referencias son las dos que subió Eli el 17-09 a
        `S5 HILTON SEP 2026 › DT › REFERENCIA CARRUSEL`.

        ⏸ `DT-V-S5-Gym` está armada pero NO SE ENTREGA: es el slide que
        contenido todavía no escribe. Queda registrada a propósito —su foto ya
        está elegida— para que entre en un render cuando llegue el texto.
      */}
      <Composition id="DT-V-S5-Portada" component={DtC1S5Portada} {...feedVideo} />
      <Composition id="DT-V-S5-Desayuno" component={DtC1S5Desayuno} {...feedVideo} />
      <Composition id="DT-V-S5-Salon" component={DtC1S5Salon} {...feedVideo} />
      <Composition id="DT-V-S5-Lobby" component={DtC1S5Lobby} {...feedVideo} />
      <Composition id="DT-V-S5-Habitacion" component={DtC1S5Habitacion} {...feedVideo} />
      <Composition id="DT-V-S5-Gym" component={DtC1S5Gym} {...feedVideo} />
    </Folder>
  </>
);

registerRoot(Raiz);
