// ============================================================================
// SANTA GOTA · FULL SCREEN · 1920×1080 · 29,97 · 19,95 s · la pieza hero (V3)
// ----------------------------------------------------------------------------
// Regla V3: en NINGÚN cuadro se nota que el reel es vertical. Todo va en RECORTE
// 16:9 cinematográfico (nunca estirado, nunca placa desenfocada), y el claim va
// sobre una imagen real a cuadro completo: el cuadro exacto 8,708 s del reel con
// la cocina EXTENDIDA a los lados por IA (sólo periferia: la monja es siempre el
// cuadro/video real encima, la extensión se generó a partir de ese cuadro).
//
// Lista de planos del reel (24 fps):
//   0,00–0,70 monja al fuego (lado) · 2,00–2,95 EL CHORRO (producto real) · 3,25–3,95 LLAMAS
//   4,00–4,45 ají (cenital) · 5,00–5,95 macro camarones · 7,50–8,20 vierte la pasta
//   8,25–8,70 pasta al fuego · 8,67–9,45 LA MONJA DE FRENTE lanza la pasta · 9,50–10,45 pinzas
//   10,50–10,95 plato · loop 11,0–11,9 emplata el ají
//
//   0,00–4,45  HOOK+RITMO  fuego (burn-through) → monja → chorro → ají → camarones → pasta → fuego
//   4,45–7,30  PRODUCTO    el chorro real, largo y a 0,6× · pinzas · el emplatado
//   7,30–13,3  CLAIM       la monja real a cuadro completo (cocina extendida) + claim cinético
//   13,3–16,6  HERO        la misma toma cobra vida: lanza la pasta (0,45×) con empuje · el plato
//   16,4–19,95 END         látigo lima → end frame petróleo: logo oficial + SANTAGOTA.CL
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, staticFile} from "remotion";
import {Cta, Latigo, Linea, Logo, LOOP, PETROLEO_OSCURO, Plumon, REEL, ReelRecorte, Revela, SFX, Sfx, entra, fade, golpe, seg, useFrameFps, FPS} from "./comun";

export const DUR_FULL = seg(19.95); // 598 f

const W = 1920, H = 1080;

/** Un plano del reel recortado a 16:9 dentro de una Sequence, con un empuje o desplazamiento de entrada. */
const Plano: React.FC<{from: number; dur: number; desde: number; fila: number; rate?: number; src?: string; zoomDe?: number; zoomA?: number; dyDe?: number; enFrames?: number}> = ({
  from, dur, desde, fila, rate = 1, src, zoomDe = 1, zoomA = 1, dyDe = 0, enFrames = 10,
}) => (
  <Sequence from={seg(from)} durationInFrames={seg(dur)} layout="none">
    <PlanoInner desde={desde} fila={fila} rate={rate} src={src} zoomDe={zoomDe} zoomA={zoomA} dyDe={dyDe} enFrames={enFrames} durF={seg(dur)} />
  </Sequence>
);
const PlanoInner: React.FC<{desde: number; fila: number; rate: number; src?: string; zoomDe: number; zoomA: number; dyDe: number; enFrames: number; durF: number}> = ({
  desde, fila, rate, src, zoomDe, zoomA, dyDe, enFrames, durF,
}) => {
  const {frame} = useFrameFps();
  const t = fade(frame, 0, enFrames);
  const e = 1 - Math.pow(1 - t, 3);
  const zoomLento = interpolate(frame, [0, durF], [zoomDe, zoomA], {extrapolateRight: "clamp"});
  const zoom = zoomDe === zoomA ? 1 : zoomLento;
  return <ReelRecorte desde={desde} w={W} h={H} fila={fila} rate={rate} src={src} zoom={zoom * (1 + 0.05 * (1 - e) * (zoomDe === zoomA ? 1 : 0))} dy={dyDe * (1 - e)} />;
};

// ── 0–7,3 s: hook, ritmo y producto ────────────────────────────────────────
const Montaje: React.FC = () => {
  const {frame} = useFrameFps();
  // burn-through: las llamas quedan ENCIMA del plano siguiente en modo screen y se apagan
  const fuegoOp = fade(frame, seg(0.42), seg(0.62), 1, 0);
  return (
    <>
      {/* B  monja al fuego (lado) — ya está debajo cuando el fuego se apaga */}
      <Plano from={0.42} dur={0.68} desde={0.05} fila={720} zoomDe={1.06} zoomA={1.0} />
      {/* A  FUEGO: hook, las llamas llenan el cuadro (3,40–3,90) y se consumen sobre B */}
      <Sequence from={0} durationInFrames={seg(0.62)} layout="none">
        <div style={{position: "absolute", inset: 0, mixBlendMode: frame >= seg(0.42) ? "screen" : "normal", opacity: fuegoOp}}>
          <ReelRecorte desde={3.4} w={W} h={H} fila={880} rate={0.9} zoom={1.04} />
        </div>
      </Sequence>
      {/* C  el chorro baja */}
      <Plano from={1.1}  dur={0.5}  desde={2.1}  fila={520} dyDe={-40} />
      {/* D  el ají cae (misma dirección) */}
      <Plano from={1.6}  dur={0.45} desde={4.0}  fila={900} dyDe={-40} />
      {/* E  macro camarones, empuje lento */}
      <Plano from={2.05} dur={1.2}  desde={5.0}  fila={960} zoomDe={1.0} zoomA={1.08} />
      {/* F  vierte la pasta (baja) */}
      <Plano from={3.25} dur={0.7}  desde={7.55} fila={880} dyDe={-40} />
      {/* G  pasta al fuego, cámara lenta */}
      <Plano from={3.95} dur={0.5}  desde={8.3}  fila={760} rate={0.7} dyDe={40} />
      {/* H  PRODUCTO: el chorro del squeeze, largo, a 0,6× (2,00→2,90) */}
      <Plano from={4.45} dur={1.5}  desde={2.0}  fila={470} rate={0.6} zoomDe={1.0} zoomA={1.05} />
      {/* I  pinzas levantan la pasta */}
      <Plano from={5.95} dur={0.55} desde={9.55} fila={900} dyDe={30} />
      {/* J  el emplatado del ají (loop) */}
      <Plano from={6.5}  dur={0.8}  desde={11.05} fila={900} src={LOOP} zoomDe={1.0} zoomA={1.04} />
    </>
  );
};

// ── 7,3–16,6 s: claim y hero sobre la monja real a cuadro completo ─────────
// Mapeo: el cuadro 8,708 del reel (1080×1920) a escala k; la placa extendida
// (1584×1008, con el recorte original 1080×1080 en x=201, y=209, ancho 590)
// se escala k/0,5463 para que la periferia calce píxel a píxel con el cuadro real.
const K = 0.70;
const KP = K / (590 / 1080);
const PLATE_W = 1584 * KP, PLATE_H = 1008 * KP;
const PLATE_TOP = -(PLATE_H - H) / 2;
const COL_LEFT = 201 * KP;
const COL_TOP = PLATE_TOP + 209 * KP - 300 * K;
const CABEZA = {x: COL_LEFT + 596 * K, y: COL_TOP + 770 * K}; // el centro de la cara en el lienzo

const Escena: React.FC<{vivo: boolean; zoom: number; origen: string}> = ({vivo, zoom, origen}) => (
  <div style={{position: "absolute", inset: 0, overflow: "hidden", transform: `scale(${zoom})`, transformOrigin: origen}}>
    {/* la placa: cocina extendida (sólo periferia IA) */}
    <Img src={staticFile("assets/santagota/plate-cocina-ext.png")}
      style={{position: "absolute", left: 0, top: PLATE_TOP, width: PLATE_W, height: PLATE_H}} />
    {/* la columna REAL: el cuadro exacto o el video, con bordes suavizados 26 px */}
    <div style={{position: "absolute", left: COL_LEFT, top: COL_TOP, width: 1080 * K, height: 1920 * K,
      WebkitMaskImage: "linear-gradient(90deg, transparent 0, #000 26px, #000 calc(100% - 26px), transparent 100%)",
      maskImage: "linear-gradient(90deg, transparent 0, #000 26px, #000 calc(100% - 26px), transparent 100%)"}}>
      {vivo
        ? <OffthreadVideo src={staticFile(REEL)} startFrom={Math.round(8.708 * FPS)} playbackRate={0.45} muted style={{position: "absolute", left: 0, top: 0, width: 1080 * K, height: 1920 * K}} />
        : <Img src={staticFile("assets/santagota/monja-8708-frame.png")} style={{position: "absolute", left: 0, top: 0, width: 1080 * K, height: 1920 * K}} />}
    </div>
  </div>
);

const Claim: React.FC = () => {
  const {frame, fps} = useFrameFps();
  const zoom = 1 + 0.05 * fade(frame, 0, seg(6.0));
  const c = [entra(frame, fps, seg(0.4), 14), entra(frame, fps, seg(0.75), 14), golpe(frame, fps, seg(1.1), 18), entra(frame, fps, seg(1.5), 14)];
  const plumon = fade(frame, seg(2.0), seg(2.5));
  const out = fade(frame, seg(5.6), seg(5.9));
  const velo = fade(frame, seg(0.2), seg(0.7), 0, 1);
  const x = 1032, y = 250;
  return (
    <>
      <Escena vivo={false} zoom={zoom} origen={`${CABEZA.x}px ${CABEZA.y + 80}px`} />
      {/* legibilidad: penumbra localizada detrás del texto, sin rectángulo */}
      <div style={{position: "absolute", inset: 0, opacity: velo * (1 - out),
        background: "radial-gradient(ellipse 620px 560px at 1450px 520px, rgba(6,26,32,0.62) 0%, rgba(6,26,32,0.38) 45%, rgba(6,26,32,0) 100%)"}} />
      <div style={{position: "absolute", left: x, top: y, zIndex: 4, opacity: 1 - out, transform: `translateX(${out * 90}px)`}}>
        <Revela p={c[0]}><Linea size={96}>El aceite</Linea></Revela>
        <Revela p={c[1]} style={{marginTop: 10}}><Linea size={96}>que llegó a</Linea></Revela>
        <Revela p={c[2]} modo="golpe" origen="0% 70%" style={{marginTop: 14}}><Linea size={98} weight={900} lima style={{letterSpacing: "-0.03em"}}>Revolucionar</Linea></Revela>
        <Revela p={c[3]} style={{marginTop: 34}}><Linea size={96}>tu cocina.</Linea></Revela>
      </div>
      <div style={{opacity: 1 - out}}>
        <Plumon x={x - 4} y={y + 96 + 10 + 96 + 14 + 112} w={830} grosor={14} p={plumon} />
      </div>
    </>
  );
};

const Hero: React.FC = () => {
  const {frame} = useFrameFps();
  // empuje hacia ella mientras lanza la pasta (arranca donde quedó el claim: 1,05)
  const zoom = 1.05 + 0.25 * fade(frame, 0, seg(1.4));
  return (
    <>
      <Sequence from={0} durationInFrames={seg(1.35)} layout="none">
        <Escena vivo zoom={zoom} origen={`${CABEZA.x}px ${CABEZA.y + 80}px`} />
      </Sequence>
      {/* el plato: pinzas emplatando y el plato final, a 0,45× (10,06→10,94: antes del logo que trae el reel a 11,0) */}
      <Plano from={1.35} dur={1.95} desde={10.06} fila={900} rate={0.45} zoomDe={1.0} zoomA={1.06} dyDe={30} />
    </>
  );
};

// ── 16,6–19,95 s: end frame ────────────────────────────────────────────────
const End: React.FC = () => {
  const {frame, fps} = useFrameFps();
  const l1 = golpe(frame, fps, 3, 20);
  const l2 = golpe(frame, fps, 11, 20);
  const wLogo = 720;
  return (
    <>
      <div style={{position: "absolute", inset: 0, background: PETROLEO_OSCURO}} />
      <div style={{position: "absolute", inset: 0, background: "radial-gradient(ellipse 900px 620px at 640px 260px, rgba(255,150,60,0.16) 0%, rgba(255,150,60,0) 100%)"}} />
      <div style={{position: "absolute", inset: 0, background: "radial-gradient(ellipse 700px 500px at 1500px 900px, rgba(195,214,0,0.07) 0%, rgba(195,214,0,0) 100%)"}} />
      <Logo x={(W - wLogo) / 2} y={205} w={wLogo} op={Math.min(1, l1 * 2)} sc={0.8 + 0.2 * l1} />
      <Cta x={(W - 640) / 2} y={775} size={72} op={Math.min(1, l2 * 2)} sc={0.8 + 0.2 * l2} rot={-2} />
    </>
  );
};

export const FullTV: React.FC = () => {
  const {frame} = useFrameFps();
  const latigo = fade(frame, seg(16.35), seg(16.85));
  return (
    <AbsoluteFill style={{background: "#000", overflow: "hidden"}}>
      <Sequence from={0} durationInFrames={seg(7.3)} layout="none"><Montaje /></Sequence>
      <Sequence from={seg(7.3)} durationInFrames={seg(6.0)} layout="none"><Claim /></Sequence>
      <Sequence from={seg(13.3)} durationInFrames={seg(3.3)} layout="none"><Hero /></Sequence>
      <Sequence from={seg(16.6)} layout="none"><End /></Sequence>
      <Latigo p={latigo} W={W} H={H} />

      {/* Sonido: cama del reel bajo el montaje, sizzle bajo claim y hero, y los golpes de la edición */}
      <Sequence from={0} layout="none">
        <Audio src={staticFile(REEL)} volume={(f) => interpolate(f, [0, 6, seg(6.7), seg(7.3)], [0, 0.55, 0.55, 0], {extrapolateRight: "clamp"})} />
      </Sequence>
      <Sequence from={seg(7.3)} durationInFrames={seg(9.1)} layout="none">
        <Audio src={staticFile(SFX.sizzle)} loop volume={(f) => interpolate(f, [0, 12, seg(8.5), seg(9.1)], [0, 0.3, 0.3, 0], {extrapolateRight: "clamp"})} />
      </Sequence>
      <Sfx src={SFX.fire} at={0} vol={0.9} />
      <Sfx src={SFX.whoosh2} at={0.42} vol={0.6} />
      <Sfx src={SFX.whoosh} at={1.1} vol={0.7} />
      <Sfx src={SFX.whoosh2} at={1.6} vol={0.6} />
      <Sfx src={SFX.whoosh} at={2.05} vol={0.6} />
      <Sfx src={SFX.whoosh2} at={3.25} vol={0.6} />
      <Sfx src={SFX.whoosh} at={3.95} vol={0.6} />
      <Sfx src={SFX.sizzle} at={4.45} vol={0.8} />
      <Sfx src={SFX.whoosh2} at={5.95} vol={0.6} />
      <Sfx src={SFX.whoosh} at={6.5} vol={0.5} />
      <Sfx src={SFX.whoosh} at={7.3} vol={0.8} />
      <Sfx src={SFX.impact} at={8.4} vol={1} />
      <Sfx src={SFX.marker} at={9.3} vol={0.7} />
      <Sfx src={SFX.whoosh2} at={12.9} vol={0.6} />
      <Sfx src={SFX.pan} at={13.3} vol={0.9} />
      <Sfx src={SFX.whoosh2} at={14.65} vol={0.6} />
      <Sfx src={SFX.whoosh} at={16.4} vol={0.9} />
      <Sfx src={SFX.sting} at={16.7} vol={1} />
    </AbsoluteFill>
  );
};
