/**
 * Entry de BETWEEN · OCTUBRE 2026 — rinde sólo esta tanda, rápido.
 *   npx remotion still src/BetweenOctEntry.tsx BW-O-01-Ganador out.png --scale=2.0833
 */
import React from 'react';
import {Composition, registerRoot} from 'remotion';
import * as O from './compositions/hilton/BetweenOctubre';

const feed = {durationInFrames: 1, fps: 30, width: 1080, height: 1350} as const;
const story = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;

const Raiz: React.FC = () => (
  <>
    <Composition id="BW-O-01-Ganador" component={O.StOct01Ganador} {...story} />
    <Composition id="BW-O-01-Ganador-Guia" component={O.StOct01GanadorGuia} {...story} />
    <Composition id="BW-O-02-ToGoPov" component={O.StOct02ToGoPov} {...story} durationInFrames={O.DURACION_TOGO_POV} />
    <Composition id="BW-O-02-ToGoPov-Guia" component={O.StOct02ToGoPovGuia} {...story} durationInFrames={O.DURACION_TOGO_POV} />
    <Composition id="BW-O-05-PasoPorUnCafe" component={O.StOct05PasoPorUnCafe} {...story} />
    <Composition id="BW-O-05-PasoPorUnCafe-Guia" component={O.StOct05PasoPorUnCafeGuia} {...story} />
    <Composition id="BW-O-07-Cumple" component={O.StOct07Cumple} {...story} />
    <Composition id="BW-O-08-Trivia" component={O.StOct08Trivia} {...story} />
    <Composition id="BW-O-08-Trivia-Guia" component={O.StOct08TriviaGuia} {...story} />
    <Composition id="BW-O-19-Cowork" component={O.StOct19Cowork} {...story} />
    <Composition id="BW-O-20-LoDicen" component={O.StOct20LoDicen} {...story} />
    <Composition id="BW-O-27-Eventos" component={O.StOct27Eventos} {...story} />
    <Composition id="BW-O-27-Eventos-Guia" component={O.StOct27EventosGuia} {...story} />
    <Composition id="BW-O-28-Bonjour" component={O.StOct28Bonjour} {...story} />
    <Composition id="BW-O-28-Bonjour-Guia" component={O.StOct28BonjourGuia} {...story} />
    <Composition id="BW-O-F05-Reunion" component={O.FeedOct05Reunion} {...feed} />
    <Composition id="BW-O-F14-Espacios" component={O.FeedOct14Espacios} {...feed} />
  </>
);

registerRoot(Raiz);
