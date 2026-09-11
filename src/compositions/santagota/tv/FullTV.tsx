// ============================================================================
// SANTA GOTA · FULL SCREEN · 1920×1080 · 29,97 · 20 s · la pieza hero
// ----------------------------------------------------------------------------
// Fotografía primero. El reel vertical nunca se estira: o va en COLUMNA 9:16
// sobre una placa desenfocada del mismo video, o se RECORTA a 16:9 donde el
// plano lo permite (los macros de comida y el chorro de aceite).
//
// Lista de planos del reel (medida con seek exacto, 11-09-2026):
//   0,00–0,70 abierto, monja al fuego · 0,75–1,20 camarones crudos · 1,25–1,95 abierto
//   2,00–2,95 EL CHORRO del squeeze (producto real) · 3,00–3,20 mano+botella lateral
//   3,25–3,95 LLAMAS · 4,00–4,45 ají cayendo (cenital) · 4,50–4,95 sartén al fuego
//   5,00–5,95 macro camarones+ají · 6,00–7,45 colador · 7,50–8,20 vierte la pasta
//   8,25–8,70 pasta al fuego · 8,75–9,45 LA MONJA DE FRENTE lanza la pasta
//   9,50–10,45 pinzas al plato · 10,50–10,95 plato · 11,00–12,46 plato con logo
//
//   0–3    HOOK      la monja lanza la pasta (cámara lenta, columna) → el chorro
//   3–8    PRODUCTO  llamas · ají · camarones · pasta · pinzas — cortes secos
//   8–13   CLAIM     columna con la cocina en vivo + el claim sobre la placa
//   13–17  HERO      partida: el chorro real | la monja con la sartén (foto)
//   17–20  END       el plato del reel, logo oficial y SANTAGOTA.CL
// Audio: la pista del reel continua (0–12,4 s) + la del loop hasta el final.
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, Img, Sequence, interpolate, staticFile} from "remotion";
import {Monja, MONJA} from "../../../brand/santagotaUI";
import {C, Cta, HaloAnim, Linea, Logo, LOOP, Plumon, REEL, ReelColumna, ReelRecorte, entra, fade, seg, useFrameFps} from "./comun";

export const DUR_FULL = seg(19.95); // 598 f — bajo los 20 s

const W = 1920, H = 1080;
const COL = 608; // ancho de la columna 9:16
const CABEZA_COL = {cx: Math.round(596 * COL / 1080), top: Math.round(641 * COL / 1080)}; // la cabeza de la monja dentro de la columna

/** Un plano del reel recortado a 16:9 con un rate opcional, dentro de una Sequence. */
const Plano: React.FC<{from: number; dur: number; desde: number; fila: number; rate?: number}> = ({from, dur, desde, fila, rate = 1}) => (
  <Sequence from={seg(from)} durationInFrames={seg(dur)} layout="none">
    <ReelRecorte desde={desde} w={W} h={H} fila={fila} rate={rate} />
  </Sequence>
);

const Hook: React.FC = () => {
  const {frame} = useFrameFps();
  const halo = fade(frame, seg(0.35), seg(0.75));
  const x = 1180;
  return (
    <>
      {/* 0–1,4 s: la monja lanza la pasta, a 0,5× */}
      <Sequence from={0} durationInFrames={seg(1.4)} layout="none">
        <ReelColumna desde={8.75} x={x} rate={0.5} W={W} H={H} />
        <HaloAnim cx={x + CABEZA_COL.cx} cy={CABEZA_COL.top - 44} w={170} h={38} p={halo} grosor={7} />
      </Sequence>
      {/* 1,4–3 s: el chorro de aceite, producto real, a 0,6× */}
      <Plano from={1.4} dur={1.6} desde={2.0} fila={600} rate={0.6} />
    </>
  );
};

const Montaje: React.FC = () => (
  <>
    <Plano from={0}    dur={0.9}  desde={3.25} fila={640} rate={0.8} />  {/* llamas */}
    <Plano from={0.9}  dur={0.55} desde={4.0}  fila={900} rate={0.8} />  {/* ají cayendo */}
    <Plano from={1.45} dur={1.2}  desde={5.0}  fila={960} rate={0.8} />  {/* macro camarones */}
    <Plano from={2.65} dur={0.9}  desde={7.5}  fila={880} rate={0.8} />  {/* vierte la pasta */}
    <Plano from={3.55} dur={0.55} desde={8.25} fila={760} rate={0.8} />  {/* pasta al fuego */}
    <Plano from={4.1}  dur={0.9}  desde={9.5}  fila={880} rate={1} />    {/* pinzas al plato */}
  </>
);

const Claim: React.FC = () => {
  const {frame, fps} = useFrameFps();
  const cl = [seg(0.3), seg(0.65), seg(1.0), seg(1.45)].map((d) => entra(frame, fps, d));
  const plumon = fade(frame, seg(1.9), seg(2.5));
  const out = fade(frame, seg(4.6), seg(4.95), 1, 0);
  const x = 800, xc = 90;
  return (
    <>
      {/* la cocina en vivo, en columna a la izquierda: abierto → abierto → chorro → llamas → pinzas */}
      <Sequence from={0}         durationInFrames={seg(1.0)} layout="none"><ReelColumna desde={0.0}  x={xc} rate={0.7} W={W} H={H} /></Sequence>
      <Sequence from={seg(1.0)}  durationInFrames={seg(1.0)} layout="none"><ReelColumna desde={1.25} x={xc} rate={0.7} W={W} H={H} /></Sequence>
      <Sequence from={seg(2.0)}  durationInFrames={seg(1.3)} layout="none"><ReelColumna desde={2.0}  x={xc} rate={0.7} W={W} H={H} /></Sequence>
      <Sequence from={seg(3.3)}  durationInFrames={seg(0.9)} layout="none"><ReelColumna desde={3.25} x={xc} rate={0.75} W={W} H={H} /></Sequence>
      <Sequence from={seg(4.2)}  durationInFrames={seg(0.8)} layout="none"><ReelColumna desde={9.5}  x={xc} rate={1} W={W} H={H} /></Sequence>
      <div style={{position: "absolute", inset: 0, background: "linear-gradient(90deg, rgba(4,14,18,0) 36%, rgba(4,14,18,0.45) 55%, rgba(4,14,18,0.6) 100%)"}} />
      <div style={{position: "absolute", left: x, top: 262, opacity: out, zIndex: 4}}>
        <Linea size={96} op={cl[0]} dy={(1 - cl[0]) * 36}>El aceite</Linea>
        <Linea size={96} op={cl[1]} dy={(1 - cl[1]) * 36} style={{marginTop: 10}}>que llegó a</Linea>
        <Linea size={112} weight={900} lima op={cl[2]} dy={(1 - cl[2]) * 36} style={{marginTop: 14}}>Revolucionar</Linea>
        <Linea size={96} op={cl[3]} dy={(1 - cl[3]) * 36} style={{marginTop: 34}}>tu cocina.</Linea>
      </div>
      <div style={{opacity: out}}>
        <Plumon x={x - 6} y={262 + 96 + 10 + 96 + 14 + 110} w={980} grosor={15} p={plumon} />
      </div>
    </>
  );
};

const Hero: React.FC = () => {
  const {frame, fps} = useFrameFps();
  const halo = fade(frame, seg(0.6), seg(1.0));
  const push = 1 + 0.045 * (frame / seg(4)); // empuje lento sobre la foto
  const entraMonja = entra(frame, fps, 0, 22);
  // la monja (recorte del fotograma 8,75) a 0,95, cabeza en x=1440 del cuadro
  const s = 0.95;
  const ty = 1080 - (MONJA.sartenBase + 40) * s;
  const tx = 1440 - MONJA.cabezaCx * s;
  return (
    <>
      {/* izquierda: el chorro real, luego las llamas, luego el plato */}
      <div style={{position: "absolute", left: 0, top: 0, width: 960, height: H, overflow: "hidden"}}>
        <Sequence from={0}         durationInFrames={seg(1.9)} layout="none"><ReelRecorte desde={2.0}  w={1706} h={H} fila={600} rate={0.5} style={{left: -373}} /></Sequence>
        <Sequence from={seg(1.9)}  durationInFrames={seg(1.4)} layout="none"><ReelRecorte desde={3.25} w={1706} h={H} fila={640} rate={0.5} style={{left: -373}} /></Sequence>
        <Sequence from={seg(3.3)}  durationInFrames={seg(0.8)} layout="none"><ReelRecorte desde={10.5} w={1706} h={H} fila={900} rate={0.6} style={{left: -373}} /></Sequence>
      </div>
      {/* derecha: la monja con la sartén sobre la placa petróleo de la propia cocina */}
      <div style={{position: "absolute", left: 960, top: 0, width: 960, height: H, overflow: "hidden", background: "#07242E"}}>
        <Img src={staticFile("assets/santagota/reel-llamas-5.4.png")}
          style={{position: "absolute", left: -480, top: -700, width: 1920, height: 1920 * 1920 / 1080, filter: "blur(30px) brightness(0.4) saturate(1.2)", transform: `scale(${push})`}} />
        <div style={{position: "absolute", left: -960, top: 0, width: W, height: H, transform: `scale(${push})`, transformOrigin: "1440px 900px", opacity: entraMonja}}>
          <Monja s={s} tx={tx} ty={ty + (1 - entraMonja) * 60} z={2} />
        </div>
      </div>
      <div style={{position: "absolute", left: 958, top: 0, width: 4, height: H, background: C.lima, opacity: 0.9}} />
      <HaloAnim cx={1440 + 4} cy={MONJA.cabezaTop * s + ty - 46} w={190} h={44} p={halo} grosor={8} />
    </>
  );
};

const End: React.FC = () => {
  const {frame, fps} = useFrameFps();
  const l1 = entra(frame, fps, 4, 22);
  const l2 = entra(frame, fps, 12, 22);
  const wLogo = 760;
  return (
    <>
      <div style={{position: "absolute", inset: 0, overflow: "hidden", background: "#0B0A08"}}>
        <Img src={staticFile("assets/santagota/reel-plato-10.6.png")}
          style={{position: "absolute", left: 0, top: 540 - 960 * (W / 1080), width: W, height: 1920 * (W / 1080), filter: "blur(4px) brightness(0.3) saturate(0.85)"}} />
      </div>
      <Logo x={(W - wLogo) / 2} y={230} w={wLogo} op={l1} sc={0.9 + 0.1 * l1} />
      <Cta x={(W - 640) / 2} y={790} size={72} op={l2} sc={0.9 + 0.1 * l2} rot={-2} />
    </>
  );
};

export const FullTV: React.FC = () => {
  const {frame} = useFrameFps();
  const fin = fade(frame, DUR_FULL - 10, DUR_FULL - 1, 1, 0);
  // pequeño «dip» a negro entre CLAIM y HERO y antes del END
  const dip = (a: number) => interpolate(Math.abs(frame - a), [0, 5], [0.85, 0], {extrapolateRight: "clamp"});
  const dipOp = Math.max(dip(seg(13)), dip(seg(17)));
  return (
    <AbsoluteFill style={{background: "#000", overflow: "hidden"}}>
      <div style={{position: "absolute", inset: 0, opacity: fin}}>
        <Sequence from={0} durationInFrames={seg(3)} layout="none"><Hook /></Sequence>
        <Sequence from={seg(3)} durationInFrames={seg(5)} layout="none"><Montaje /></Sequence>
        <Sequence from={seg(8)} durationInFrames={seg(5)} layout="none"><Claim /></Sequence>
        <Sequence from={seg(13)} durationInFrames={seg(4)} layout="none"><Hero /></Sequence>
        <Sequence from={seg(17)} layout="none"><End /></Sequence>
        <div style={{position: "absolute", inset: 0, background: "#000", opacity: dipOp, pointerEvents: "none"}} />
      </div>
      {/* Audio continuo: reel completo, luego el loop hasta el final, con fundido */}
      <Sequence from={0} layout="none">
        <Audio src={staticFile(REEL)} volume={(f) => interpolate(f, [0, 8, seg(11.4), seg(12.4)], [0, 1, 1, 0], {extrapolateRight: "clamp"})} />
      </Sequence>
      <Sequence from={seg(11.4)} layout="none">
        <Audio src={staticFile(LOOP)} startFrom={seg(0.6)}
          volume={(f) => interpolate(f, [0, seg(1.0), DUR_FULL - seg(11.4) - seg(1.2), DUR_FULL - seg(11.4)], [0, 1, 1, 0], {extrapolateRight: "clamp"})} />
      </Sequence>
    </AbsoluteFill>
  );
};
