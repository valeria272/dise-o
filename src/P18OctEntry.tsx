/**
 * Entry de la grilla de OCTUBRE 2026 de PISO18 — rinde sin depender de `src/Root.tsx`,
 * igual que `src/P18Entry.tsx`.
 *
 *   npx remotion still src/P18OctEntry.tsx P18O-F0610 out/pieza.png --scale=2.0833
 *   npx remotion render src/P18OctEntry.tsx P18O-S0510 out/pieza.mp4
 *
 * La mesa es 1080 de ancho y se entrega a 2250 (×2,0833): feed 2250×2813,
 * historia 2250×4000. El video va a 1080×1920 (ver `scripts/p18-rendir.py`).
 * Piezas y dirección de arte: `src/compositions/piso18/P18Octubre.tsx`.
 */
import React from 'react';
import {Composition, Folder, registerRoot} from 'remotion';
import * as O from './compositions/piso18/P18Octubre';

const feed = {durationInFrames: 1, fps: 30, width: 1080, height: 1350} as const;
const story = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;

const FEED: [string, React.FC][] = [
  ['P18O-F0610', O.P18OF0610],
  ['P18O-F0910-1', O.P18OF0910S1],
  ['P18O-F0910-2', O.P18OF0910S2],
  ['P18O-F1310-1', O.P18OF1310S1],
  ['P18O-F1310-2', O.P18OF1310S2],
  ['P18O-F1610-1', O.P18OF1610S1],
  ['P18O-F1610-2', O.P18OF1610S2],
  ['P18O-F1610-3', O.P18OF1610S3],
  ['P18O-F1610-4', O.P18OF1610S4],
  ['P18O-F1610-5', O.P18OF1610S5],
  ['P18O-F2310-1', O.P18OF2310S1],
  ['P18O-F2310-2', O.P18OF2310S2],
  ['P18O-F2310-3', O.P18OF2310S3],
  ['P18O-F2310-4', O.P18OF2310S4],
  ['P18O-F2710', O.P18OF2710],
];

const STORIES: [string, React.FC][] = [
  ['P18O-S0710', O.P18OS0710],
  ['P18O-S0910', O.P18OS0910],
  ['P18O-S2310', O.P18OS2310],
  ['P18O-S2710', O.P18OS2710],
];

const Animada: React.FC = () => <O.P18OS0510 clip="s0510.mp4" />;
const AnimadaEstatica: React.FC = () => <O.P18OS0510 />;

const Raiz: React.FC = () => (
  <>
    <Folder name="P18-Oct-Feed">
      {FEED.map(([id, C]) => (
        <Composition key={id} id={id} component={C} {...feed} />
      ))}
    </Folder>
    <Folder name="P18-Oct-Stories">
      {STORIES.map(([id, C]) => (
        <Composition key={id} id={id} component={C} {...story} />
      ))}
      <Composition id="P18O-S0510" component={Animada} {...story} durationInFrames={O.P18_S0510_DUR} />
      <Composition id="P18O-S0510-foto" component={AnimadaEstatica} {...story} durationInFrames={O.P18_S0510_DUR} />
      {STORIES.map(([id, C]) => (
        <Composition
          key={`${id}-Guia`}
          id={`${id}-Guia`}
          component={() => (
            <O.P18OGuiaStory>
              <C />
            </O.P18OGuiaStory>
          )}
          {...story}
        />
      ))}
    </Folder>
  </>
);

registerRoot(Raiz);
