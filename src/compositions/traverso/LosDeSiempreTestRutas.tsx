/**
 * TEST DE RUTAS MUSICALES — primeros 12 s de «Los de siempre» sobre dos músicas.
 * Ruta A: garage/indie rock desde el primer beat. Ruta B: italiano clásico 0–1,8 s → rompe en garage.
 * Misma estructura de dirección; los cortes se cuadran a los golpes MEDIDOS de cada pista
 * (scripts/beatmap.py). Se exportan dos composiciones: TraversoRutaA y TraversoRutaB.
 */
import React from "react";
import {AbsoluteFill, Audio, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {Video} from "@remotion/media";

export const RUTA_FPS = 24;
export const RUTA_W = 1080;
export const RUTA_H = 1920;
export const RUTA_DURATION = 12 * RUTA_FPS;
const A = "assets/traverso/lds2";
const F = (s: number) => Math.round(s * RUTA_FPS);
const INK = "#050505", BONE = "#F2EEE7", MOSTAZA = "#E8B325", ARCHIVO = "LDS Archivo";
const fontPromise = typeof FontFace !== "undefined" ? new FontFace(ARCHIVO, `url(${staticFile("assets/fonts/copywriters/Archivo-Variable.ttf")})`).load().then((f) => (document as any).fonts.add(f)).catch(() => undefined) : Promise.resolve();

export type Ruta = {
  musica: string;            // archivo en audio/rutas
  offset: number;            // segundos de la pista que se saltan para que el riff caiga en 0 (o en `hasta`)
  cuts: {c1: number; c2: number; c3: number; boom: number; trio: number; r1: number; r2: number; r3: number; prep: number; vacio: number; reveal: number; fin: number};
  vacioMusica: boolean;      // si la pista ya trae el hueco no se corta
  intro?: {src: string; hasta: number};  // Ruta B: italiano hasta `hasta`, después la garage
};

type Plano = {id: string; from: number; to: number; src: string; trim?: number; rate?: number; whipIn?: boolean; push?: [number, number]; origin?: string; punch?: number; zoom?: number; shake?: boolean};
const planos = (T: Ruta["cuts"]): Plano[] => [
  {id: "c01", from: T.c1, to: T.c2, src: "c01.mp4", trim: 0.0, punch: 1.14},
  {id: "c02", from: T.c2, to: T.c3, src: "c02.mp4", trim: 0.3, punch: 1.14},
  {id: "c03", from: T.c3, to: T.boom, src: "c03.mp4", trim: 0.6, rate: 1.3, punch: 1.14},
  {id: "boom", from: T.boom, to: T.trio, src: "c09.mp4", trim: 0.0, rate: 1, punch: 1.22, origin: "50% 40%"},
  {id: "c04a", from: T.trio, to: T.trio + 0.5, src: "c04.mp4", trim: 0.2, rate: 1, whipIn: true},
  {id: "c04b", from: T.trio + 0.5, to: T.trio + 0.75, src: "c04.mp4", trim: 0.7, rate: 2.4},
  {id: "c04c", from: T.trio + 0.75, to: T.r1, src: "c04.mp4", trim: 1.3, rate: 0.55},
  {id: "c05", from: T.r1, to: T.r2, src: "c05.mp4", trim: 0.6, rate: 1.2, zoom: 1.7, origin: "50% 44%", punch: 1.06},
  {id: "c06", from: T.r2, to: T.r3, src: "c06.mp4", trim: 0.2, rate: 1.2, zoom: 1.25, origin: "50% 30%", punch: 1.06},
  {id: "c07", from: T.r3, to: T.prep, src: "c07.mp4", trim: 0.2, rate: 1.2, punch: 1.06},
  {id: "c08", from: T.prep, to: T.reveal, src: "c08.mp4", trim: 0.4, rate: 1.3, push: [1.0, 1.08], origin: "50% 32%"},
  {id: "c09", from: T.reveal, to: T.fin, src: "c09.mp4", trim: 0.0, rate: 1.7, push: [1.22, 1.0], origin: "50% 45%", shake: true},
];

const Shot: React.FC<{p: Plano}> = ({p}) => {
  const frame = useCurrentFrame(); const dur = F(p.to - p.from);
  const whip = p.whipIn ? interpolate(frame, [0, 4], [22, 0], {extrapolateRight: "clamp"}) : 0;
  const push = p.push ? interpolate(frame, [0, dur], p.push, {easing: (x) => 1 - Math.pow(1 - x, 3)}) : 1;
  const punch = p.punch ? interpolate(frame, [0, 3, dur], [p.punch, 1 + (p.punch - 1) * 0.3, 1.0], {extrapolateRight: "clamp"}) : 1;
  const shake = p.shake ? (frame === 1 ? 1.035 : frame === 2 ? 0.985 : frame === 3 ? 1.012 : 1) : 1;
  return (
    <AbsoluteFill style={{background: INK}}>
      <AbsoluteFill style={{transform: `scale(${push * punch * shake * (p.zoom ?? 1)})`, transformOrigin: p.origin ?? "50% 50%", filter: whip ? `blur(${whip}px)` : undefined}}>
        <Video src={staticFile(`${A}/clips/${p.src}`)} trimBefore={F(p.trim ?? 0)} playbackRate={p.rate ?? 1} volume={0} style={{width: "100%", height: "100%", objectFit: "cover"}} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
const Titular: React.FC<{lineas: string[]; size?: number; color?: string; bottom?: number; wdth?: number; wght?: number; tracking?: number}> = ({lineas, size = 96, color = BONE, bottom = 230, wdth = 62, wght = 850, tracking}) => {
  const frame = useCurrentFrame(); const {fps} = useVideoConfig();
  const enter = spring({fps, frame, config: {damping: 16, stiffness: 260, mass: 0.7}});
  const tr = tracking ?? interpolate(enter, [0, 1], [0.12, 0.0]);
  return (
    <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: bottom}}>
      <div style={{transform: `scale(${interpolate(enter, [0, 1], [1.32, 1])})`, filter: `blur(${interpolate(frame, [0, 3], [10, 0], {extrapolateRight: "clamp"})}px)`, fontFamily: ARCHIVO, fontVariationSettings: `"wdth" ${wdth}, "wght" ${wght}`, fontSize: size, lineHeight: 0.94, letterSpacing: `${tr}em`, color, textAlign: "center", textTransform: "uppercase", textShadow: "0 8px 50px rgba(0,0,0,0.75)", padding: "0 50px"}}>
        {lineas.map((l, i) => <div key={i}>{l}</div>)}
      </div>
    </AbsoluteFill>
  );
};
const HeroText: React.FC = () => {
  const frame = useCurrentFrame(); const {fps} = useVideoConfig();
  const enter = spring({fps, frame: frame - 3, config: {damping: 13, stiffness: 220, mass: 0.7}});
  return (
    <AbsoluteFill style={{justifyContent: "center", alignItems: "center", opacity: interpolate(enter, [0, 1], [0, 1])}}>
      <div style={{transform: `scale(${interpolate(enter, [0, 1], [1.5, 1])}) translateY(-620px)`, fontFamily: ARCHIVO, fontVariationSettings: '"wdth" 62, "wght" 900', fontSize: 212, lineHeight: 0.9, color: MOSTAZA, textAlign: "center", letterSpacing: "-0.01em", textShadow: "0 14px 40px rgba(0,0,0,0.85), 0 0 120px rgba(232,179,37,0.25)"}}>LOS DE<br />SIEMPRE.</div>
    </AbsoluteFill>
  );
};

const sfx = (T: Ruta["cuts"]) => [
  {src: "sfx-clack.mp3", at: T.c1, vol: 1.0}, {src: "sfx-impacto.mp3", at: T.c1, vol: 0.5},
  {src: "sfx-clack.mp3", at: T.c2, vol: 1.0}, {src: "sfx-impacto.mp3", at: T.c2, vol: 0.5},
  {src: "sfx-pasos.mp3", at: T.c3, vol: 0.9, dur: 0.4, base: "lds"}, {src: "sfx-impacto.mp3", at: T.c3, vol: 0.6},
  {src: "sfx-bass.mp3", at: T.boom, vol: 0.8}, {src: "sfx-camara.mp3", at: T.boom, vol: 0.5},
  {src: "sfx-whip.mp3", at: T.trio - 0.05, vol: 0.7},
  {src: "sfx-tela.mp3", at: T.r1, vol: 0.6, base: "lds"}, {src: "sfx-tela.mp3", at: T.r2, vol: 0.6, base: "lds"}, {src: "sfx-tela.mp3", at: T.r3, vol: 0.6, base: "lds"},
  {src: "sfx-camara.mp3", at: T.r1 - 0.04, vol: 0.5}, {src: "sfx-camara.mp3", at: T.r2 - 0.04, vol: 0.5}, {src: "sfx-camara.mp3", at: T.r3 - 0.04, vol: 0.5},
  {src: "sfx-tela.mp3", at: T.prep + 0.6, vol: 0.4, base: "lds"},
  {src: "sfx-bass.mp3", at: T.reveal, vol: 1.0}, {src: "sfx-golpe.mp3", at: T.reveal, vol: 0.7, base: "lds"}, {src: "sfx-solapas.mp3", at: T.reveal + 0.2, vol: 0.85, base: "lds"}, {src: "sfx-camara.mp3", at: T.reveal + 0.05, vol: 0.6},
];

export const Test: React.FC<{ruta: Ruta}> = ({ruta}) => {
  void fontPromise; const T = ruta.cuts;
  const musicaDesde = ruta.intro ? ruta.intro.hasta : 0;
  return (
    <AbsoluteFill style={{background: INK}}>
      <Sequence from={F(T.reveal)} durationInFrames={F(T.fin - T.reveal)} layout="none"><HeroText /></Sequence>
      {planos(T).map((p) => (
        <Sequence key={p.id} from={F(p.from)} durationInFrames={Math.max(1, F(p.to - p.from))} layout="none">
          {p.id === "c09" ? <AbsoluteFill style={{WebkitMaskImage: "linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.3) 15%, #000 27%, #000 100%)", maskImage: "linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.3) 15%, #000 27%, #000 100%)"}}><Shot p={p} /></AbsoluteFill> : <Shot p={p} />}
        </Sequence>
      ))}
      <Sequence from={F(T.boom + 0.15)} durationInFrames={F(T.trio - T.boom - 0.15)} layout="none"><Titular lineas={["Ya se supo..."]} size={44} wdth={72} wght={700} tracking={0.18} bottom={250} /></Sequence>
      <Sequence from={F(T.trio + 0.3)} durationInFrames={F(T.r1 - T.trio - 0.3)} layout="none"><Titular lineas={["Vienen", "los de siempre."]} size={100} /></Sequence>

      {/* Música: Ruta B lleva intro italiana y la garage entra en `hasta`; el vacío antes del reveal se corta acá */}
      {ruta.intro ? (
        <Sequence from={0} durationInFrames={F(ruta.intro.hasta)} layout="none"><Audio src={staticFile(`${A}/audio/rutas/${ruta.intro.src}`)} trimBefore={F(0.35)} volume={0.9} /></Sequence>
      ) : null}
      <Sequence from={F(musicaDesde)} durationInFrames={F(T.vacio - musicaDesde)} layout="none">
        <Audio src={staticFile(`${A}/audio/rutas/${ruta.musica}`)} trimBefore={F(ruta.offset + musicaDesde)} volume={0.95} />
      </Sequence>
      <Sequence from={F(T.reveal)} layout="none">
        <Audio src={staticFile(`${A}/audio/rutas/${ruta.musica}`)} trimBefore={F(ruta.offset + T.reveal)} volume={0.95} />
      </Sequence>
      {sfx(T).map((s, i) => (
        <Sequence key={i} from={F(s.at)} durationInFrames={s.dur ? F(s.dur) : undefined} layout="none">
          <Audio src={staticFile(`${s.base === "lds" ? "assets/traverso/lds" : A}/audio/${s.src}`)} volume={s.vol} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};

// ---- Rutas: los números se cuadran a los golpes medidos (ver EDICION-RUTAS-MUSICALES.md) ----
// Ruta A — A-garage-1.mp3 (130 bpm, beat 0,46 s). Offset 1,5 s: el riff arranca en 0,0.
// Golpes medidos (archivo − 1,5): 1,64 (la banda para en 1,5 y vuelve a golpear), 2,34, 4,86, 5,34,
// 6,06, 6,96, 8,58, 9,02, 9,52 (hit −12 dB tras el bache natural 8,5–9,0) → DROP.
export const RUTA_A: Ruta = {musica: "A-garage-1.mp3", offset: 1.5, vacioMusica: false,
  cuts: {c1: 0.0, c2: 0.46, c3: 0.92, boom: 1.64, trio: 2.34, r1: 4.86, r2: 5.34, r3: 6.06, prep: 6.96, vacio: 9.02, reveal: 9.52, fin: 12.0}};
// Ruta B — cuerdas italianas 0–1,64 (tradición) y en el BOOM entra la misma garage en su golpe de 1,64 (actitud).
export const RUTA_B: Ruta = {musica: "A-garage-1.mp3", offset: 1.5, vacioMusica: false, intro: {src: "B-italiano-1.mp3", hasta: 1.64},
  cuts: {c1: 0.0, c2: 0.55, c3: 1.1, boom: 1.64, trio: 2.34, r1: 4.86, r2: 5.34, r3: 6.06, prep: 6.96, vacio: 9.02, reveal: 9.52, fin: 12.0}};
export const TraversoRutaA: React.FC = () => <Test ruta={RUTA_A} />;
export const TraversoRutaB: React.FC = () => <Test ruta={RUTA_B} />;
