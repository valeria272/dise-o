// ============================================================================
// SANTA GOTA · HUINCHA TV · 1920×216 · 29,97 · 209 f = 6,97 s (≤ 7,00 s) · alfa real
// ----------------------------------------------------------------------------
// V4 — UNA sola composición horizontal continua, de borde a borde.
//   0,00–1,45  la monja ASOMA por el borde inferior, ENORME: la cara ocupa toda la
//              altura (cornette fuera de cuadro por arriba, mentón en el borde de abajo).
//   1,45–4,40  entra una FRANJA petróleo de 1920 px (borde izquierdo → borde derecho),
//              la monja se superpone a ella; encima, el claim grande: EL ACEITE QUE
//              LLEGÓ A · REVOLUCIONAR (lima, golpe) · TU COCINA. · plumón.
//   4,40–6,55  la MISMA franja cambia de contenido: el claim sale por la izquierda y
//              entran por la derecha el logo oficial y SANTAGOTA.CL, grandes.
//   6,55–6,97  la franja se retira y la monja vuelve a bajar.
// Fuera de la monja y la franja, TRANSPARENTE (se ve el programa).
// ============================================================================
import React from "react";
import {AbsoluteFill, Sequence} from "remotion";
import {MONJA} from "../../../brand/santagotaUI";
import {Cta, Linea, Logo, MonjaViva, PETROLEO, Plumon, Revela, SFX, Sfx, cae, entra, fade, golpe, pingpong, seg, useFrameFps} from "./comun";

export const DUR_HUINCHA = 209; // 6,97 s — bajo los 7,00 s exactos

const W = 1920, H = 216;
const FRANJA_TOP = 40; // la franja va de y=40 al borde inferior; la cara sobresale por arriba

export const HuinchaTV: React.FC = () => {
  const {frame, fps} = useFrameFps();

  // — la monja: cara a toda la altura (cornette a −34, mentón en el borde), cabeza en x=250 —
  const s = 1.0;
  const cx = 250;
  const tx = cx - MONJA.cabezaCx * s;
  const tyFinal = -34 - MONJA.cabezaTop * s;
  const sube = golpe(frame, fps, 0, 18);
  const hunde = 6 * Math.sin(Math.PI * fade(frame, seg(1.45), seg(1.8)));        // reacciona a la franja
  const baja = cae(frame, DUR_HUINCHA - 13, DUR_HUINCHA - 1) * 330;               // salida
  const ty = tyFinal + (1 - sube) * 300 + hunde + baja;
  const cuadro = pingpong(frame - 16, 7);

  // — la franja: de borde a borde —
  const franjaIn = golpe(frame, fps, seg(1.45), 14);
  const franjaOut = cae(frame, DUR_HUINCHA - 12, DUR_HUINCHA - 2);

  // — claim —
  const c1 = entra(frame, fps, seg(1.6), 14);
  const c2 = golpe(frame, fps, seg(1.9), 16);
  const c3 = entra(frame, fps, seg(2.2), 14);
  const plumon = fade(frame, seg(2.6), seg(3.05));
  const claimOut = fade(frame, seg(4.4), seg(4.65));

  // — marca (entra por la derecha en la misma franja) —
  const m = entra(frame, fps, seg(4.55), 16);
  const marcaOp = fade(frame, DUR_HUINCHA - 12, DUR_HUINCHA - 6, 1, 0);

  const xT = 500;

  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      {/* La franja, 1920 px, con barrido de entrada (izq→der) y de salida */}
      <div style={{position: "absolute", left: 0, top: FRANJA_TOP, width: W, height: H - FRANJA_TOP, background: PETROLEO, zIndex: 1,
        clipPath: `inset(0 ${(1 - Math.min(1, franjaIn)) * 100}% 0 ${Math.min(1, franjaOut) * 100}%)`}}>
        {/* claim */}
        <div style={{position: "absolute", left: xT, top: 12, transform: `translateX(${-claimOut * 160}px)`, opacity: 1 - claimOut}}>
          <Revela p={c1} modo="izq">
            <Linea size={42} weight={700} sombra={false}>El aceite que llegó a</Linea>
          </Revela>
          <div style={{display: "flex", alignItems: "baseline", gap: 28, marginTop: 0}}>
            <Revela p={c2} modo="golpe" origen="0% 70%">
              <Linea size={100} weight={900} lima sombra={false} style={{letterSpacing: "-0.03em"}}>Revolucionar</Linea>
            </Revela>
            <Revela p={c3} modo="abajo">
              <Linea size={56} sombra={false}>tu cocina.</Linea>
            </Revela>
          </div>
        </div>
        <div style={{opacity: 1 - claimOut}}>
          <Plumon x={xT - 4} y={162} w={820} grosor={9} p={plumon} />
        </div>
        {/* marca: entra desde la derecha, por la misma franja */}
        <div style={{position: "absolute", left: 0, top: 0, width: W, height: H, opacity: marcaOp * Math.min(1, m * 3), transform: `translateX(${(1 - m) * 420}px)`}}>
          <Logo x={720} y={14 - FRANJA_TOP} w={300} sombra={false} />
          <Cta x={1062} y={44} size={62} />
        </div>
      </div>

      {/* La monja asoma, ENCIMA de la franja (se superpone a ella) */}
      <div style={{position: "absolute", left: 0, top: 0, width: W, height: H, overflow: "hidden", zIndex: 2}}>
        <MonjaViva cuadro={cuadro} s={s} tx={tx} ty={ty} z={2} />
      </div>

      {/* Sonido (sólo para el preview; la huincha se entrega muda) */}
      <Sequence from={0} layout="none">
        <Sfx src={SFX.whoosh2} at={0} vol={0.8} />
        <Sfx src={SFX.whoosh} at={1.45} vol={0.7} />
        <Sfx src={SFX.impact} at={1.9} vol={0.9} />
        <Sfx src={SFX.marker} at={2.6} vol={0.6} />
        <Sfx src={SFX.sting} at={4.55} vol={0.9} />
      </Sequence>
    </AbsoluteFill>
  );
};
