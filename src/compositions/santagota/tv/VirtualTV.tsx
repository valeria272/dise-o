// ============================================================================
// SANTA GOTA · VIRTUAL TV · 775×1080 · 29,97 · 450 f = 15,0 s · alfa real
// ----------------------------------------------------------------------------
// V4 — «Una monja acaba de entrar al matinal», recompuesta:
//   0,0–3,0   ENTRA       la monja al 112 % (cabeza + torso), con overshoot; aureola
//   3,0–6,0   GESTO       levanta la sartén y da un golpe de muñeca (cuadros reales, ida y vuelta)
//   6,0–11,0  CLAIM       ella se hunde un poco y la tipografía ocupa el espacio, DETRÁS de ella:
//                         EL ACEITE · QUE LLEGÓ A · REVOLUCIONAR (lima, mayor) · TU COCINA. · plumón
//   11,0–14,4 CIERRE      losa petróleo de borde a borde con el logo oficial grande + SANTAGOTA.CL;
//                         la monja sigue presente, abajo
//   14,4–15,0 SALIDA      ella vuelve a meterse en la tele; la losa se retira
// Nada de cajas de video ni comida gigante. ⚠ PLANTILLA DEL CANAL PENDIENTE (márgenes 48 px).
// ============================================================================
import React from "react";
import {AbsoluteFill, Sequence} from "remotion";
import {MONJA} from "../../../brand/santagotaUI";
import {Cta, HaloAnim, Linea, Logo, MonjaViva, PETROLEO, Plumon, Revela, SFX, Sfx, cae, entra, fade, golpe, pingpong, seg, useFrameFps} from "./comun";

export const DUR_VIRTUAL = seg(15);

const W = 775, H = 1080, M = 48;
const SOMBRA = "0 3px 6px rgba(0,0,0,0.55), 0 6px 30px rgba(0,0,0,0.6)";

/** Gesto real: levanta la sartén y la pasta salta apenas (cuadros 3→5→3), ida y vuelta. */
const cuadroGesto = (frame: number, desde: number, paso = 4) => {
  const sec = [3, 4, 5, 5, 4, 3];
  const i = Math.floor((frame - desde) / paso);
  if (i < 0) return pingpong(frame, 8);
  if (i >= sec.length) return pingpong(frame - desde - sec.length * paso, 8);
  return sec[i];
};

export const VirtualTV: React.FC = () => {
  const {frame, fps} = useFrameFps();

  // — la monja —
  const s = 1.12;
  const CX = 455;                                       // un poco a la derecha del centro: la sartén no se corta por el borde izquierdo
  const tx = CX - MONJA.cabezaCx * s;
  const tyArriba = 130 - MONJA.cabezaTop * s;          // cornette en y=130
  const sube = golpe(frame, fps, 0, 22);
  const e1 = fade(frame, seg(6.0), seg(6.6)); const hClaim = e1 * e1 * (3 - 2 * e1);    // se hunde para el claim
  const e2 = fade(frame, seg(10.8), seg(11.3)); const hMarca = e2 * e2 * (3 - 2 * e2);  // y un poco más para la marca
  const salida = cae(frame, DUR_VIRTUAL - 18, DUR_VIRTUAL - 1) * 900;
  const ty = tyArriba + (1 - sube) * 1000 + hClaim * 240 + hMarca * 150 + salida;
  const cuadro = cuadroGesto(frame - 22, seg(3.4) - 22);
  const halo = fade(frame, seg(1.6), seg(2.0)) * (1 - hClaim);
  const haloY = 100 + (1 - sube) * 1000;

  // — claim (detrás de la monja) —
  const t0 = seg(6.2);
  const c = [entra(frame, fps, t0, 14), entra(frame, fps, t0 + 9, 14), golpe(frame, fps, t0 + 20, 18), entra(frame, fps, t0 + 34, 14)];
  const plumon = fade(frame, seg(7.6), seg(8.1));
  const claimOut = fade(frame, seg(10.6), seg(10.95));

  // — marca —
  const losaIn = golpe(frame, fps, seg(11.05), 14);
  const losaOut = cae(frame, DUR_VIRTUAL - 16, DUR_VIRTUAL - 4);
  const l1 = golpe(frame, fps, seg(11.2), 18);
  const l2 = golpe(frame, fps, seg(11.45), 18);
  const marcaOp = fade(frame, DUR_VIRTUAL - 16, DUR_VIRTUAL - 9, 1, 0);

  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      {/* El claim: tipografía en el espacio, detrás del personaje */}
      <div style={{position: "absolute", left: M, top: 44, zIndex: 1, opacity: 1 - claimOut, transform: `translateX(${-claimOut * 120}px)`}}>
        <Revela p={c[0]}><Linea size={64} style={{textShadow: SOMBRA}}>El aceite</Linea></Revela>
        <Revela p={c[1]} style={{marginTop: 4}}><Linea size={64} style={{textShadow: SOMBRA}}>que llegó a</Linea></Revela>
        <Revela p={c[2]} modo="golpe" origen="0% 70%" style={{marginTop: 10}}><Linea size={80} weight={900} lima style={{letterSpacing: "-0.03em", textShadow: SOMBRA}}>Revolucionar</Linea></Revela>
        <Revela p={c[3]} style={{marginTop: 30}}><Linea size={64} style={{textShadow: SOMBRA}}>tu cocina.</Linea></Revela>
      </div>
      <div style={{opacity: 1 - claimOut}}>
        <Plumon x={M - 4} y={44 + 64 + 4 + 64 + 10 + 92} w={640} grosor={11} p={plumon} z={1} />
      </div>

      {/* La marca: losa petróleo de borde a borde, logo grande y SANTAGOTA.CL */}
      <div style={{position: "absolute", left: 0, top: 30, width: W, height: 440, background: PETROLEO, zIndex: 1, boxShadow: "0 12px 40px rgba(0,0,0,0.4)",
        clipPath: `inset(0 ${(1 - Math.min(1, losaIn)) * 100}% 0 ${Math.min(1, losaOut) * 100}%)`}}>
        <div style={{opacity: marcaOp}}>
          <Logo x={(W - 540) / 2} y={40} w={540} op={Math.min(1, l1 * 2)} sc={0.8 + 0.2 * l1} sombra={false} />
        </div>
      </div>
      <div style={{opacity: marcaOp * Math.min(1, l2 * 2), zIndex: 3}}>
        <Cta x={(W - 520) / 2} y={428} size={52} sc={0.8 + 0.2 * l2} z={3} />
      </div>

      {/* La monja (alfa real), delante de todo */}
      <div style={{position: "absolute", left: 0, top: 0, width: W, height: H, overflow: "hidden", zIndex: 4}}>
        <MonjaViva cuadro={cuadro} s={s} tx={tx} ty={ty} z={4} />
      </div>
      <HaloAnim cx={CX + 8} cy={haloY} w={220} h={46} p={halo} grosor={9} z={5} />

      {/* Sonido (sólo preview; el virtual se entrega mudo) */}
      <Sequence from={0} layout="none">
        <Sfx src={SFX.whoosh2} at={0} vol={0.8} />
        <Sfx src={SFX.pan} at={3.4} vol={0.8} />
        <Sfx src={SFX.impact} at={6.9} vol={0.9} />
        <Sfx src={SFX.marker} at={7.6} vol={0.6} />
        <Sfx src={SFX.sting} at={11.1} vol={0.9} />
        <Sfx src={SFX.whoosh2} at={14.4} vol={0.5} />
      </Sequence>
    </AbsoluteFill>
  );
};
