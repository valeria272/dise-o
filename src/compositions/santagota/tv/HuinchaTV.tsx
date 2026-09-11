// ============================================================================
// SANTA GOTA · HUINCHA TV · 1920×216 · 29,97 · 7 s (210 f) · alfa real
// ----------------------------------------------------------------------------
// La monja GRANDE asoma desde el borde inferior (cabeza = 200 de los 216 px).
// Placa fotográfica: la foto de Instagram del wok con llamas, desenfocada y
// oscurecida (sólo ambiente). Información por etapas para que todo tenga
// tamaño:  0–1,5 s monja · 1,5–4,5 s claim · 4,5–7 s logo + SANTAGOTA.CL.
// Todo lo que no es la banda es transparente.
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {Monja, MONJA} from "../../../brand/santagotaUI";
import {C, Cta, HaloAnim, Linea, Logo, Plumon, entra, fade, seg, useFrameFps} from "./comun";

export const DUR_HUINCHA = seg(7);

export const HuinchaTV: React.FC = () => {
  const {frame, fps} = useFrameFps();
  const W = 1920, H = 216;

  // — monja: cabeza de ~200 px, centrada en x=300, sube desde abajo —
  const s = 0.62;
  const cabezaCx = 300;
  const tx = cabezaCx - MONJA.cabezaCx * s;
  const tyFinal = 26 - MONJA.cabezaTop * s;
  const subida = entra(frame, fps, 3, 26);
  const ty = tyFinal + (1 - subida) * 230;
  const halo = fade(frame, seg(1.0), seg(1.4));

  // — claim (1,5–4,5 s) —
  const c1 = entra(frame, fps, seg(1.5));
  const c2 = entra(frame, fps, seg(1.85));
  const plumon = fade(frame, seg(2.5), seg(3.0));
  const claimOut = fade(frame, seg(4.4), seg(4.75), 1, 0);

  // — marca (4,5–7 s) —
  const l1 = entra(frame, fps, seg(4.6), 20);
  const l2 = entra(frame, fps, seg(4.85), 20);

  const bandaOp = fade(frame, DUR_HUINCHA - 8, DUR_HUINCHA - 1, 1, 0);
  const bandaSube = entra(frame, fps, 0, 12); // la banda entra desde abajo en 0,35 s
  const xClaim = 600;

  return (
    <AbsoluteFill style={{overflow: "hidden", opacity: bandaOp, transform: `translateY(${(1 - bandaSube) * H}px)`}}>
      {/* La banda: placa fotográfica (ambiente) */}
      <div style={{position: "absolute", left: 0, top: 0, width: W, height: H, overflow: "hidden", background: "#1A1410"}}>
        <Img src={staticFile("assets/santagota/ig-monja-wok.jpg")}
          style={{position: "absolute", left: 0, top: -1160, width: 1920, height: 1920, filter: "blur(7px) brightness(0.5) saturate(1.15)", transform: "scale(1.06)"}} />
        <div style={{position: "absolute", inset: 0, background: "linear-gradient(90deg, rgba(10,8,6,0.15) 0%, rgba(10,8,6,0.55) 35%, rgba(10,8,6,0.55) 80%, rgba(10,8,6,0.3) 100%)"}} />
        <div style={{position: "absolute", left: 0, right: 0, top: 0, height: 3, background: C.lima, opacity: 0.9}} />
      </div>

      {/* La monja asoma */}
      <div style={{position: "absolute", left: 0, top: 0, width: W, height: H, overflow: "hidden"}}>
        <Monja s={s} tx={tx} ty={ty} z={2} />
      </div>
      <HaloAnim cx={cabezaCx + 4} cy={12} w={92} h={17} p={halo} grosor={5} />

      {/* El claim */}
      <div style={{position: "absolute", left: xClaim, top: 26, opacity: claimOut, zIndex: 4}}>
        <Linea size={46} op={c1} dy={(1 - c1) * 30}>El aceite que llegó a</Linea>
        <div style={{display: "flex", alignItems: "baseline", gap: 22, marginTop: 6, opacity: c2, transform: `translateY(${(1 - c2) * 34}px)`}}>
          <Linea size={86} weight={900} lima>Revolucionar</Linea>
          <Linea size={52}>tu cocina.</Linea>
        </div>
      </div>
      <div style={{opacity: claimOut}}>
        <Plumon x={xClaim - 4} y={182} w={800} grosor={10} p={plumon} />
      </div>

      {/* Marca */}
      <Logo x={840} y={30} w={250} op={l1} sc={0.85 + 0.15 * l1} />
      <Cta x={1180} y={64} size={54} op={l2} sc={0.85 + 0.15 * l2} />
    </AbsoluteFill>
  );
};
