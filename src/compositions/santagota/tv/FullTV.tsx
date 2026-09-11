// ============================================================================
// SANTA GOTA · FULL SCREEN · 1920×1080 · 29,97 · 19,95 s · la pieza hero (V4)
// ----------------------------------------------------------------------------
// V4 = pauta de montaje cerrada (11-09-2026): sin zooms ni empujes digitales,
// cortes secos motivados, recorte 16:9 estático por plano, claim sobre la monja
// GRANDE con un solo cambio de plano sutil (cut-in), payoff con el lanzamiento
// real y corte directo al end frame quieto.
//
// Lista de planos del reel (24 fps, a cuadro exacto):
//   0,00–0,70 monja al fuego (lado) · 2,00–2,94 EL CHORRO (producto real) · 2,98–3,22 brazo+botella,
//   se enciende a 3,23 · 3,40–3,92 LLAMAS grandes · 3,94–4,45 ají (cenital) · 4,50–4,95 sartén al fuego ·
//   5,00–5,95 macro camarones · 7,50–8,20 vierte la pasta · 8,25–8,62 pasta al fuego ·
//   8,667–9,35 LA MONJA DE FRENTE lanza la pasta · 9,50–10,45 pinzas · 10,50–10,95 plato · 11,0+ logo del reel (no usar)
//   loop 11,05–11,95 emplata el ají
//
//   0,00–1,20  HOOK        las llamas llenan el cuadro (3,32→3,92 a 0,5×) — sin texto, sin logo, sin zoom
//   1,20–2,70  ACEITE      el chorro real: botella, aceite y sartén (0,62×) — match cut vertical al ají
//   2,70–4,20  INGREDIENTES ají cae y termina · macro camarones
//   4,20–5,70  PASTA       vierte la pasta y la pasta al fuego (0,72×) — corte seco
//   5,70–7,50  MONJA+PRODUCTO la monja al fuego (0,6×) · brazo con la botella y se enciende (0,6×)
//   7,50–9,00  COCINA 2    sartén al fuego · el emplatado del ají
//   9,00–13,50 HERO+CLAIM  la monja de frente, grande (cocina extendida sólo periferia); cut-in en REVOLUCIONAR
//   13,50–16,80 PAYOFF     la misma toma cobra vida: lanza la pasta (0,5×) · pinzas y plato (0,7×)
//   16,80–19,95 END        corte directo: logo oficial + SANTAGOTA.CL, quietos
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, staticFile} from "remotion";
import {Cta, Linea, Logo, LOOP, PETROLEO_OSCURO, Plumon, REEL, ReelRecorte, Revela, SFX, Sfx, entra, fade, golpe, seg, useFrameFps, FPS} from "./comun";

export const DUR_FULL = seg(19.95); // 598 f

const W = 1920, H = 1080;

/** Un plano del reel recortado a 16:9, ESTÁTICO, dentro de una Sequence. */
const Plano: React.FC<{from: number; dur: number; desde: number; fila: number; rate?: number; src?: string}> = ({from, dur, desde, fila, rate = 1, src}) => (
  <Sequence from={seg(from)} durationInFrames={seg(dur)} layout="none">
    <ReelRecorte desde={desde} w={W} h={H} fila={fila} rate={rate} src={src} />
  </Sequence>
);

// ── 0–9 s: hook, aceite, ingredientes, pasta, monja + producto, cocina 2 ────
const Montaje: React.FC = () => (
  <>
    <Plano from={0}    dur={1.2}  desde={3.32}  fila={880} rate={0.5} />               {/* HOOK: las llamas ya están y crecen (3,32→3,92) */}
    <Plano from={1.2}  dur={1.5}  desde={2.0}   fila={540} rate={0.62} />              {/* ACEITE: botella + chorro + sartén */}
    <Plano from={2.7}  dur={0.5}  desde={3.96}  fila={900} />                          {/* ají cae (match cut vertical) y termina */}
    <Plano from={3.2}  dur={1.0}  desde={5.0}   fila={960} />                          {/* macro camarones */}
    <Plano from={4.2}  dur={1.5}  desde={7.5}   fila={880} rate={0.72} />              {/* PASTA: vierte → al fuego */}
    <Plano from={5.7}  dur={1.1}  desde={0.05}  fila={720} rate={0.6} />               {/* MONJA al fuego, cara y lentes */}
    <Plano from={6.8}  dur={0.7}  desde={2.98}  fila={760} rate={0.6} />               {/* PRODUCTO: brazo con la botella, se enciende */}
    <Plano from={7.5}  dur={0.6}  desde={4.5}   fila={900} rate={0.75} />              {/* COCINA 2: sartén al fuego */}
    <Plano from={8.1}  dur={0.9}  desde={11.05} fila={900} src={LOOP} />               {/* el emplatado del ají */}
  </>
);

// ── 9–16,8 s: hero + claim + payoff sobre la monja real ────────────────────
// Mapeo: el cuadro 8,708 del reel (1080×1920) a escala K, cabeza en (600, 420/440).
// La placa extendida (1584×1008; el recorte original 1080×1080 —filas 300–1380— está
// en x=201, y=209 con 590 px de ancho) se escala K/0,5463 y se alinea al cuadro real.
const KPLATE = 590 / 1080;
const geo = (K: number, cabezaY: number) => {
  const KP = K / KPLATE;
  const colLeft = 600 - 596 * K;
  const colTop = cabezaY - 770 * K;
  return {K, colLeft, colTop, plateLeft: colLeft - 201 * KP, plateTop: colTop + 300 * K - 209 * KP, plateW: 1584 * KP, plateH: 1008 * KP};
};
const ABIERTO = geo(1.0, 420);
const CERRADO = geo(1.2, 440);

const Escena: React.FC<{g: ReturnType<typeof geo>; vivo?: boolean; desde?: number; rate?: number}> = ({g, vivo = false, desde = 8.667, rate = 0.5}) => (
  <div style={{position: "absolute", inset: 0, overflow: "hidden"}}>
    <Img src={staticFile("assets/santagota/plate-cocina-ext.png")}
      style={{position: "absolute", left: g.plateLeft, top: g.plateTop, width: g.plateW, height: g.plateH}} />
    <div style={{position: "absolute", left: g.colLeft, top: g.colTop, width: 1080 * g.K, height: 1920 * g.K,
      WebkitMaskImage: "linear-gradient(90deg, transparent 0, #000 26px, #000 calc(100% - 26px), transparent 100%)",
      maskImage: "linear-gradient(90deg, transparent 0, #000 26px, #000 calc(100% - 26px), transparent 100%)"}}>
      {vivo
        ? <OffthreadVideo src={staticFile(REEL)} startFrom={Math.round(desde * FPS)} playbackRate={rate} muted style={{position: "absolute", left: 0, top: 0, width: 1080 * g.K, height: 1920 * g.K}} />
        : <Img src={staticFile("assets/santagota/monja-8708-frame.png")} style={{position: "absolute", left: 0, top: 0, width: 1080 * g.K, height: 1920 * g.K}} />}
    </div>
  </div>
);

const Claim: React.FC = () => {
  const {frame, fps} = useFrameFps();
  const CUT = seg(1.4); // cut-in sobre REVOLUCIONAR
  const c = [entra(frame, fps, seg(0.3), 14), entra(frame, fps, seg(0.7), 14), golpe(frame, fps, CUT, 18), entra(frame, fps, seg(1.9), 14)];
  const plumon = fade(frame, seg(2.3), seg(2.8));
  const out = fade(frame, seg(4.1), seg(4.45));
  const velo = fade(frame, seg(0.1), seg(0.5));
  const x = 1080, y = 300;
  return (
    <>
      <Escena g={frame < CUT ? ABIERTO : CERRADO} />
      {/* legibilidad: penumbra localizada detrás del texto, sin rectángulo */}
      <div style={{position: "absolute", inset: 0, opacity: velo * (1 - out),
        background: "radial-gradient(ellipse 640px 560px at 1480px 510px, rgba(6,26,32,0.6) 0%, rgba(6,26,32,0.36) 45%, rgba(6,26,32,0) 100%)"}} />
      <div style={{position: "absolute", left: x, top: y, zIndex: 4, opacity: 1 - out}}>
        <Revela p={c[0]}><Linea size={84}>El aceite</Linea></Revela>
        <Revela p={c[1]} style={{marginTop: 10}}><Linea size={84}>que llegó a</Linea></Revela>
        <Revela p={c[2]} modo="golpe" origen="0% 70%" style={{marginTop: 14}}><Linea size={94} weight={900} lima style={{letterSpacing: "-0.03em"}}>Revolucionar</Linea></Revela>
        <Revela p={c[3]} style={{marginTop: 32}}><Linea size={84}>tu cocina.</Linea></Revela>
      </div>
      <div style={{opacity: 1 - out}}>
        <Plumon x={x - 4} y={y + 84 + 10 + 84 + 14 + 108} w={790} grosor={14} p={plumon} />
      </div>
    </>
  );
};

const Payoff: React.FC = () => (
  <>
    {/* la misma toma cobra vida: lanza la pasta (8,667→9,24 a 0,5×; después la pasta se sale por la izquierda) */}
    <Sequence from={0} durationInFrames={seg(1.15)} layout="none">
      <Escena g={CERRADO} vivo desde={8.667} rate={0.5} />
    </Sequence>
    {/* pinzas, emplatado y plato (9,55→10,93 a 0,64×) — termina antes del logo que trae el reel */}
    <Plano from={1.15} dur={2.15} desde={9.55} fila={900} rate={0.64} />
  </>
);

// ── 16,8–19,95 s: end frame quieto ─────────────────────────────────────────
const End: React.FC = () => {
  const wLogo = 720;
  return (
    <>
      <div style={{position: "absolute", inset: 0, background: PETROLEO_OSCURO}} />
      <div style={{position: "absolute", inset: 0, background: "radial-gradient(ellipse 900px 620px at 640px 260px, rgba(255,150,60,0.16) 0%, rgba(255,150,60,0) 100%)"}} />
      <div style={{position: "absolute", inset: 0, background: "radial-gradient(ellipse 700px 500px at 1500px 900px, rgba(195,214,0,0.07) 0%, rgba(195,214,0,0) 100%)"}} />
      <Logo x={(W - wLogo) / 2} y={205} w={wLogo} />
      <Cta x={(W - 640) / 2} y={775} size={72} rot={-2} />
    </>
  );
};

export const FullTV: React.FC = () => (
  <AbsoluteFill style={{background: "#000", overflow: "hidden"}}>
    <Sequence from={0} durationInFrames={seg(9.0)} layout="none"><Montaje /></Sequence>
    <Sequence from={seg(9.0)} durationInFrames={seg(4.5)} layout="none"><Claim /></Sequence>
    <Sequence from={seg(13.5)} durationInFrames={seg(3.3)} layout="none"><Payoff /></Sequence>
    <Sequence from={seg(16.8)} layout="none"><End /></Sequence>

    {/* Sonido: cama de cocina (sizzle en loop) bajo todo el montaje; pocos golpes, sólo donde la edición los pide */}
    <Sequence from={0} durationInFrames={seg(16.8)} layout="none">
      <Audio src={staticFile(SFX.sizzle)} loop volume={(f) => interpolate(f, [0, 10, seg(16.3), seg(16.8)], [0, 0.4, 0.4, 0], {extrapolateRight: "clamp"})} />
    </Sequence>
    <Sfx src={SFX.fire} at={0} vol={0.9} />
    <Sfx src={SFX.whoosh} at={1.2} vol={0.5} />
    <Sfx src={SFX.fire} at={7.05} vol={0.5} />
    <Sfx src={SFX.whoosh} at={9.0} vol={0.6} />
    <Sfx src={SFX.impact} at={10.4} vol={1} />
    <Sfx src={SFX.marker} at={11.3} vol={0.6} />
    <Sfx src={SFX.pan} at={13.5} vol={0.9} />
    <Sfx src={SFX.sting} at={16.8} vol={1} />
  </AbsoluteFill>
);
