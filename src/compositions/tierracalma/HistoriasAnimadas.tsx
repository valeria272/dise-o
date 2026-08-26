import React from "react";
import {AbsoluteFill, Audio, interpolate, staticFile, useCurrentFrame} from "remotion";
import {tierracalma as TC} from "../../brand/tierracalma";
import {H1, H2, H4} from "./Piezas";

// =============================================================================
// TIERRA CALMA · HISTORIAS ANIMADAS — septiembre 2026
//
// Son LAS MISMAS tres historias del feed, no una versión aparte: se renderiza
// el mismo componente con `anim`, que enciende el Ken Burns de la foto y las
// entradas del texto. Antes eran una maqueta paralela y se desincronizaron con
// la fija; ahora es imposible que diverjan.
//
// El zoom siempre va hacia AFUERA y lento — así lee como un dron ganando
// altura. Un zoom in sobre una foto fija delata que no es video.
//
// 9:16 · 30 fps · 6 s (lo que muestra Instagram por historia).
// =============================================================================

export const HISTORIA_DURATION = 180; // 6 s

// Grano finísimo: sin él una foto quieta con zoom se ve "digital".
const Grano: React.FC<{id: string}> = ({id}) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{opacity: 0.05, mixBlendMode: "overlay", pointerEvents: "none"}}>
      <svg width="100%" height="100%">
        <filter id={id}>
          <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves={2} seed={frame % 55} stitchTiles="stitch" />
          <feColorMatrix type="saturate" values="0" />
        </filter>
        <rect width="100%" height="100%" filter={`url(#${id})`} />
      </svg>
    </AbsoluteFill>
  );
};

// Cada historia lleva una pista distinta, en el mismo registro de calma.
const Musica: React.FC<{src: string}> = ({src}) => {
  const frame = useCurrentFrame();
  const v = Math.min(
    interpolate(frame, [0, 20], [0, 1], {extrapolateRight: "clamp"}),
    interpolate(frame, [HISTORIA_DURATION - 40, HISTORIA_DURATION - 4], [1, 0], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    }),
  );
  return <Audio src={staticFile(src)} volume={v * 0.5} loop />;
};

const Envoltura: React.FC<{id: string; musica: string; children: React.ReactNode}> = ({id, musica, children}) => {
  const frame = useCurrentFrame();
  // Fundido a negro al final: la historia encadena con la siguiente sin corte duro.
  const salida = interpolate(frame, [HISTORIA_DURATION - 12, HISTORIA_DURATION], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{background: "#0A1116"}}>
      <Musica src={musica} />
      {children}
      <Grano id={id} />
      <AbsoluteFill style={{background: "#000", opacity: salida, pointerEvents: "none"}} />
    </AbsoluteFill>
  );
};

export const HistoriaPrimavera: React.FC = () => (
  <Envoltura id="tch-1" musica={TC.music.vastness}>
    <H1 anim dur={HISTORIA_DURATION} />
  </Envoltura>
);

export const HistoriaPaso: React.FC = () => (
  <Envoltura id="tch-2" musica={TC.music.sereneView}>
    <H2 anim dur={HISTORIA_DURATION} />
  </Envoltura>
);

export const HistoriaEpoca: React.FC = () => (
  <Envoltura id="tch-3" musica={TC.music.valleySunset}>
    <H4 anim dur={HISTORIA_DURATION} />
  </Envoltura>
);
