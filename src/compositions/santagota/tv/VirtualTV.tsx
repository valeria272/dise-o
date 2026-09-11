// ============================================================================
// SANTA GOTA · VIRTUAL TV · 775×1080 · 29,97 · 15 s (450 f) · alfa real
// ----------------------------------------------------------------------------
// «La monja se mete en la tele.» Arriba, transparencia: la cabeza y la aureola
// flotan sobre el set. Abajo, un panel FOTOGRÁFICO (el reel: llamas, el chorro
// del squeeze, los camarones) por detrás del cual ella asoma.
//   0–1,5 s  el panel sube y ella asoma      · 1,5–6 s mira (respira), aureola
//   6–10 s   el panel pasa a la acción: aceite real cayendo, fuego
//   9,5–13 s claim sobre la foto              · 13–15 s logo + SANTAGOTA.CL
// ⚠ PLANTILLA DEL CANAL PENDIENTE: márgenes provisorios de 48 px.
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, Sequence, interpolate, staticFile} from "remotion";
import {Monja, MONJA} from "../../../brand/santagotaUI";
import {Cta, HaloAnim, Linea, Logo, Plumon, ReelRecorte, entra, fade, seg, useFrameFps} from "./comun";

export const DUR_VIRTUAL = seg(15);

export const VirtualTV: React.FC = () => {
  const {frame, fps} = useFrameFps();
  const W = 775, H = 1080;
  const M = 48;
  const panelTop = 470;
  const panelH = H - panelTop;

  // — panel sube —
  const sube = entra(frame, fps, 0, 24);
  const panelY = panelTop + (1 - sube) * (panelH + 40);

  // — monja asoma por detrás (cabeza en y=110), respira —
  const s = 1;
  const asoma = entra(frame, fps, 10, 28);
  const respira = 1 + 0.012 * Math.sin(frame / 14);
  const tyFinal = 110 - MONJA.cabezaTop * s;
  const ty = tyFinal + (1 - asoma) * 520;
  const tx = W / 2 - MONJA.cabezaCx * s;
  const halo = fade(frame, seg(1.9), seg(2.35));
  const monjaOut = fade(frame, seg(13.0), seg(13.5), 1, 0); // baja cuando entra la marca
  const tyOut = ty + (1 - monjaOut) * 140;

  // — claim —
  const cl = [seg(9.6), seg(9.95), seg(10.3), seg(10.75)].map((d) => entra(frame, fps, d));
  const plumon = fade(frame, seg(11.2), seg(11.75));
  const claimOut = fade(frame, seg(12.9), seg(13.25), 1, 0);
  const velo = interpolate(frame, [seg(9.4), seg(9.9)], [0, 0.5], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});

  // — marca —
  const l1 = entra(frame, fps, seg(13.3), 20);
  const l2 = entra(frame, fps, seg(13.6), 20);
  const piezaOp = fade(frame, DUR_VIRTUAL - 12, DUR_VIRTUAL - 1, 1, 0);

  return (
    <AbsoluteFill style={{overflow: "hidden", opacity: piezaOp}}>
      {/* La monja, detrás del panel */}
      <div style={{position: "absolute", left: 0, top: 0, width: W, height: H, overflow: "hidden", zIndex: 1,
        transform: `scale(${respira})`, transformOrigin: `${W / 2}px ${panelTop}px`}}>
        <Monja s={s} tx={tx} ty={tyOut} z={1} />
      </div>
      <HaloAnim cx={W / 2 + 6} cy={70} w={150} h={34} p={halo * monjaOut} grosor={7} z={2} />

      {/* El panel fotográfico */}
      <div style={{position: "absolute", left: 0, top: panelY, width: W, height: panelH, overflow: "hidden", zIndex: 3, background: "#120F0C",
        boxShadow: "0 -18px 60px rgba(0,0,0,0.45)"}}>
        {/* 0–6 s: llamas quietas con un empuje lento */}
        <Sequence from={0} durationInFrames={seg(6)} layout="none">
          <Img src={staticFile("assets/santagota/reel-llamas-5.4.png")}
            style={{position: "absolute", left: -40, top: -560 - frame * 0.35, width: 860, height: 860 * 1920 / 1080, filter: "brightness(0.75) saturate(1.1)"}} />
        </Sequence>
        {/* 6–10,5 s: el reel de corrido desde el chorro (2,0 s): aceite real → llamas → ají → camarones */}
        <Sequence from={seg(6)} durationInFrames={seg(4.5)} layout="none">
          <ReelRecorte desde={2.0} w={W} h={panelH} fila={700} style={{top: 0}} />
        </Sequence>
        {/* 10,5–15 s: macro de camarones → colador → pasta al fuego (reel 5,0 → 9,5: corta antes de que ella aparezca) */}
        <Sequence from={seg(10.5)} durationInFrames={seg(4.5)} layout="none">
          <ReelRecorte desde={5.0} w={W} h={panelH} fila={960} style={{top: 0}} />
        </Sequence>
        {/* velo para el claim */}
        <div style={{position: "absolute", inset: 0, background: `rgba(8,20,26,${velo})`}} />
        <div style={{position: "absolute", left: 0, right: 0, top: 0, height: 4, background: "#C3D600", opacity: 0.9}} />

        {/* El claim, sobre la foto */}
        <div style={{position: "absolute", left: M, top: 70, opacity: claimOut, zIndex: 4}}>
          <Linea size={58} op={cl[0]} dy={(1 - cl[0]) * 30}>El aceite</Linea>
          <Linea size={58} op={cl[1]} dy={(1 - cl[1]) * 30} style={{marginTop: 6}}>que llegó a</Linea>
          <Linea size={76} weight={900} lima op={cl[2]} dy={(1 - cl[2]) * 30} style={{marginTop: 10}}>Revolucionar</Linea>
          <Linea size={58} op={cl[3]} dy={(1 - cl[3]) * 30} style={{marginTop: 22}}>tu cocina.</Linea>
        </div>
        <div style={{opacity: claimOut}}>
          <Plumon x={M - 4} y={70 + 58 + 6 + 58 + 10 + 74} w={W - 2 * M - 30} grosor={11} p={plumon} />
        </div>

        {/* Marca */}
        <Logo x={(W - 330) / 2} y={140} w={330} op={l1} sc={0.85 + 0.15 * l1} />
        <Cta x={(W - 420) / 2} y={400} size={46} op={l2} sc={0.85 + 0.15 * l2} />
      </div>
    </AbsoluteFill>
  );
};
