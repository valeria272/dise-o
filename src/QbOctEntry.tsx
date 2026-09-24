/**
 * Entry point de QB — GRILLA OCTUBRE 2026 (historias). Sólo las piezas que la
 * grilla viva marcaba OK PARA DISEÑAR el 24-09-2026: 11 historias, 0 de feed.
 *
 *   npx remotion still  src/QbOctEntry.tsx QB-OCT-ST01 out/qb/oct/x.png --scale=2.0833
 *   npx remotion render src/QbOctEntry.tsx QB-OCT-ST22 out/qb/oct/x.mp4 --scale=2.0833
 *
 * La mesa es 1080×1920 y se entrega a 2250×4000 (×2,0833).
 * ⛔ QB es marca INDEPENDIENTE: nada de DT, Between ni Piso18.
 */
import React from "react";
import {Composition, Folder, registerRoot} from "remotion";

import {QbSt01BancoChile} from "./compositions/qb/oct/QbSt01BancoChile";
import {QbSt06Aycd} from "./compositions/qb/oct/QbSt06Aycd";
import {QbSt08Cmr} from "./compositions/qb/oct/QbSt08Cmr";
import {QbSt09Sunset} from "./compositions/qb/oct/QbSt09Sunset";
import {QbSt14Adivina} from "./compositions/qb/oct/QbSt14Adivina";
import {QbSt15MejoresAmigos} from "./compositions/qb/oct/QbSt15MejoresAmigos";
import {QbSt20AycdLlamada} from "./compositions/qb/oct/QbSt20AycdLlamada";
import {QbSt21Estacionamiento} from "./compositions/qb/oct/QbSt21Estacionamiento";
import {QbSt23CloseFriends} from "./compositions/qb/oct/QbSt23CloseFriends";
import {QbSt22Ensalada, QB_ST22_DURACION} from "./compositions/qb/oct/QbSt22Ensalada";
import {QbSt26Terraza, QB_ST26_DURACION} from "./compositions/qb/oct/QbSt26Terraza";

const Q = {fps: 30, width: 1080, height: 1920} as const;

const Raiz: React.FC = () => (
  <Folder name="QB-Octubre">
    <Composition id="QB-OCT-ST01" component={QbSt01BancoChile} durationInFrames={1} {...Q} />
    <Composition id="QB-OCT-ST06" component={QbSt06Aycd} durationInFrames={1} {...Q} />
    <Composition id="QB-OCT-ST08" component={QbSt08Cmr} durationInFrames={1} {...Q} />
    <Composition id="QB-OCT-ST09" component={QbSt09Sunset} durationInFrames={1} {...Q} />
    <Composition id="QB-OCT-ST14" component={QbSt14Adivina} durationInFrames={1} {...Q} />
    <Composition id="QB-OCT-ST15" component={QbSt15MejoresAmigos} durationInFrames={1} {...Q} />
    <Composition id="QB-OCT-ST20" component={QbSt20AycdLlamada} durationInFrames={1} {...Q} />
    <Composition id="QB-OCT-ST21" component={QbSt21Estacionamiento} durationInFrames={1} {...Q} />
    <Composition id="QB-OCT-ST23" component={QbSt23CloseFriends} durationInFrames={1} {...Q} />
    <Composition id="QB-OCT-ST22" component={QbSt22Ensalada} durationInFrames={QB_ST22_DURACION} {...Q} />
    <Composition id="QB-OCT-ST26" component={QbSt26Terraza} durationInFrames={QB_ST26_DURACION} {...Q} />
  </Folder>
);

registerRoot(Raiz);
