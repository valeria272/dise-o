// ============================================================================
// SANTA GOTA · CIERRE COMÚN — 1920×1080 · el end frame del full screen
// ----------------------------------------------------------------------------
// IDEA      Lo mismo con que termina el reel de la monja: el logo a color sobre
//           el plato oscuro. Acá el plato es el verde botella del envase.
//           Logo grande, URL en lima, nada más. Se queda 3 s en pantalla.
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {santagota as SG} from "../../brand/santagota";
import {LogoColor, Url, useSantaGota} from "../../brand/santagotaUI";

export const CierreTV: React.FC = () => {
  const C = useSantaGota();
  const {width: W} = SG.formatos.full;
  const wLogo = 780;
  return (
    <AbsoluteFill style={{background: C.botella}}>
      <LogoColor x={(W - wLogo) / 2} y={200} w={wLogo} />
      <Url x={0} y={760} size={96} align="center" />
    </AbsoluteFill>
  );
};
