// ============================================================================
// SANTA GOTA · HUINCHA TV · 1920×216 · 29,97 · 209 f = 6,97 s (≤ 7,00 s) · alfa real
// ----------------------------------------------------------------------------
// V3 — «La monja se mete en la tele»: intervención sobre el programa, no banda.
//   0,00–0,50  HOOK   la monja ASOMA por el borde inferior (cara + lentes + hábito,
//                     cabeza de ~200 px), sube con overshoot y se detiene seca.
//   1,45–4,40  CLAIM  una losa petróleo se barre desde la izquierda y el claim entra
//                     cinético: EL ACEITE QUE LLEGÓ A · REVOLUCIONAR (golpe, lima) ·
//                     TU COCINA. · plumón naranja. La monja se hunde 8 px con el golpe.
//   4,40–6,55  MARCA  el claim sale por la izquierda, la losa se acorta y entran el
//                     logo oficial y SANTAGOTA.CL, grandes.
//   6,55–6,97  SALIDA la losa se barre hacia la izquierda y la monja vuelve a bajar.
// Todo lo que no es monja ni losa es TRANSPARENTE (se ve el programa).
// ============================================================================
import React from "react";
import {AbsoluteFill, Sequence} from "remotion";
import {MONJA} from "../../../brand/santagotaUI";
import {Bloque, Cta, HaloAnim, Linea, Logo, MonjaViva, Plumon, Revela, SFX, Sfx, cae, entra, fade, golpe, pingpong, seg, useFrameFps} from "./comun";

export const DUR_HUINCHA = 209; // 6,97 s — bajo los 7,00 s exactos

const W = 1920, H = 216;

export const HuinchaTV: React.FC = () => {
  const {frame, fps} = useFrameFps();

  // — la monja: cabeza de ~200 px, cornette en y=22, asoma desde abajo —
  const s = 0.72;
  const cx = 250;
  const tx = cx - MONJA.cabezaCx * s;
  const tyFinal = 22 - MONJA.cabezaTop * s;
  const sube = golpe(frame, fps, 0, 18);
  const hunde = 8 * Math.sin(Math.PI * fade(frame, seg(1.45), seg(1.8)));        // reacciona al golpe de la losa
  const baja = cae(frame, DUR_HUINCHA - 13, DUR_HUINCHA - 1) * 300;               // salida: vuelve a bajar
  const ty = tyFinal + (1 - sube) * 280 + hunde + baja;
  const cuadro = pingpong(frame - 16, 7);                                         // micro-vida de la pose

  const halo = fade(frame, seg(0.75), seg(1.1));

  // — la losa —
  const xB = 505;
  const losaIn = golpe(frame, fps, seg(1.45), 14);
  const losaW = fade(frame, seg(4.4), seg(4.75), 1190, 860);                      // se acorta para la marca
  const losaOut = cae(frame, DUR_HUINCHA - 12, DUR_HUINCHA - 2);

  // — claim —
  const c1 = entra(frame, fps, seg(1.55), 14);
  const c2 = golpe(frame, fps, seg(1.85), 16);
  const c3 = entra(frame, fps, seg(2.15), 14);
  const plumon = fade(frame, seg(2.55), seg(3.0));
  const claimOut = fade(frame, seg(4.4), seg(4.62));
  const xT = 552;

  // — marca —
  const l1 = golpe(frame, fps, seg(4.62), 18);
  const l2 = golpe(frame, fps, seg(4.85), 18);
  const marcaOp = fade(frame, DUR_HUINCHA - 12, DUR_HUINCHA - 6, 1, 0);

  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      {/* La monja asoma (recortada por el borde inferior de la huincha) */}
      <div style={{position: "absolute", left: 0, top: 0, width: W, height: H, overflow: "hidden", zIndex: 2}}>
        <MonjaViva cuadro={cuadro} s={s} tx={tx} ty={ty} z={2} />
      </div>
      <HaloAnim cx={cx + 4} cy={14 + hunde + baja} w={124} h={22} p={halo} grosor={5} z={6} />

      {/* La losa petróleo: claim → marca */}
      <Bloque x={xB} y={-6} w={losaW} h={H + 12} p={losaIn} q={losaOut} z={3}>
        {/* claim */}
        <div style={{position: "absolute", left: xT - xB, top: 22, transform: `translateX(${-claimOut * 140}px)`, opacity: 1 - claimOut}}>
          <Revela p={c1} modo="izq">
            <Linea size={40} weight={700} sombra={false}>El aceite que llegó a</Linea>
          </Revela>
          <div style={{display: "flex", alignItems: "baseline", gap: 24, marginTop: 2}}>
            <Revela p={c2} modo="golpe" origen="0% 70%">
              <Linea size={90} weight={900} lima sombra={false} style={{letterSpacing: "-0.03em"}}>Revolucionar</Linea>
            </Revela>
            <Revela p={c3} modo="abajo">
              <Linea size={48} sombra={false}>tu cocina.</Linea>
            </Revela>
          </div>
        </div>
        <div style={{opacity: 1 - claimOut}}>
          <Plumon x={xT - xB - 4} y={182} w={740} grosor={9} p={plumon} />
        </div>
        {/* marca */}
        <div style={{opacity: marcaOp}}>
          <Logo x={60} y={28} w={250} op={Math.min(1, l1 * 2)} sc={0.7 + 0.3 * l1} sombra={false} />
          <Cta x={365} y={70} size={54} op={Math.min(1, l2 * 2)} sc={0.7 + 0.3 * l2} />
        </div>
      </Bloque>

      {/* Sonido (solo para el preview; la huincha se entrega muda) */}
      <Sequence from={0} layout="none">
        <Sfx src={SFX.whoosh2} at={0} vol={0.9} />
        <Sfx src={SFX.whoosh} at={1.45} vol={0.8} />
        <Sfx src={SFX.impact} at={1.85} vol={0.9} />
        <Sfx src={SFX.marker} at={2.55} vol={0.7} />
        <Sfx src={SFX.whoosh2} at={4.4} vol={0.6} />
        <Sfx src={SFX.sting} at={4.62} vol={0.9} />
        <Sfx src={SFX.whoosh2} at={6.55} vol={0.6} />
      </Sequence>
    </AbsoluteFill>
  );
};
