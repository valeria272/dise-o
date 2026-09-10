/**
 * TRAVERSO × GRUPO COPYLAB — «LOS DE SIEMPRE · THE ENTRANCE» V3  (23 s · 24 fps)
 * ----------------------------------------------------------------------------
 * Instrucción central de Valeria: «No quiero más escenas. Quiero más dirección dentro de los
 * segundos que tenemos.» → cero clips nuevos; se rehacen timing, transiciones, música y SFX.
 *
 *  0,0–2,0  microhook tráiler: CLACK boquilla 0,4 · CLACK mano 0,4 · TAC zapato 0,4 · BOOM los tres 0,8
 *           («YA SE SUPO...» chico sobre el BOOM, nunca sobre negro)
 *  2,0–4,5  entrada con speed ramp · VIENEN LOS DE SIEMPRE.
 *  4,5–7,0  tres personalidades a TRES escalas (macro puño · medio corbatín · general solapa), al golpe
 *  7,0–9,75 manos a solapas → microvacío de 4 f (SIN pantalla negra) → BOOM
 *  9,75–12,5 HERO: bass hit + tela + impacto de cámara (2 f) + push-in rápido que frena · LOS DE SIEMPRE.
 * 12,5–13,7 triple product porn 0,4 · 0,4 · 0,4 al beat
 * 13,7–16,3 puerta: riser → sobreexposición total → esa luz es la ventana de la sala
 * 16,3–17,3 entran → WIPE (Ketchup pasa frente a cámara) → CUT
 * 17,3–20,5 reunión: ya sentados, microacto (carpeta / taza / notebook) · PRIMERA REUNIÓN. / CERO PRESENTACIONES.
 * 20,5–23,0 end card 2,5 s: LOS DE SIEMPRE. + AHORA TAMBIÉN EN NUESTRA MESA. → BIENVENIDOS, TRAVERSO. + logos → hard cut
 *
 * Banda: audio/banda-v3.mp3 (scripts/traverso-lds2-banda.py) — golpes en 3,0 · 4,5 · 6,0 · 7,5 ·
 * microvacío 9,6–9,75 · DROP 9,75 · riser 15,3 · groove suave 17,3 · HIT 22,4 · corte 23,0.
 */
import React from "react";
import {AbsoluteFill, Audio, Img, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {Video} from "@remotion/media";

export const ENT3_FPS = 24;
export const ENT3_W = 1080;
export const ENT3_H = 1920;
export const ENT3_DURATION = 23 * ENT3_FPS; // 552

const A = "assets/traverso/lds2";
const F = (s: number) => Math.round(s * ENT3_FPS);
const INK = "#050505";
const BONE = "#F2EEE7";
const MOSTAZA = "#E8B325";
const ARCHIVO = "LDS Archivo";
const fontPromise =
  typeof FontFace !== "undefined"
    ? new FontFace(ARCHIVO, `url(${staticFile("assets/fonts/copywriters/Archivo-Variable.ttf")})`).load().then((f) => (document as any).fonts.add(f)).catch(() => undefined)
    : Promise.resolve();

const DROP = 9.75;
const T = {c1: 0.0, c2: 0.4, c3: 0.8, boom: 1.2, trio: 2.0, r1: 4.5, r2: 5.3, r3: 6.1, prep: 7.0, vacio: 9.6, reveal: DROP,
  porn: 12.5, puerta: 13.7, entran: 16.3, mesa: 17.3, end: 20.5, fin: 23.0};

type Plano = {id: string; from: number; to: number; src: string; trim?: number; rate?: number; whipIn?: boolean; push?: [number, number]; origin?: string; burn?: boolean; punch?: number; zoom?: number; fromWhite?: boolean; freezeTail?: boolean; shake?: boolean};
const PLANOS: Plano[] = [
  {id: "c01", from: T.c1, to: T.c2, src: "c01.mp4", trim: 0.0, punch: 1.14},
  {id: "c02", from: T.c2, to: T.c3, src: "c02.mp4", trim: 0.3, punch: 1.14},
  {id: "c03", from: T.c3, to: T.boom, src: "c03.mp4", trim: 0.6, rate: 1.3, punch: 1.14},
  {id: "boom", from: T.boom, to: T.trio, src: "c09.mp4", trim: 0.0, rate: 1, punch: 1.22, origin: "50% 40%"},
  // entrada con speed ramp (tres tramos a velocidad constante)
  {id: "c04a", from: T.trio, to: T.trio + 0.5, src: "c04.mp4", trim: 0.2, rate: 1, whipIn: true},
  {id: "c04b", from: T.trio + 0.5, to: T.trio + 0.75, src: "c04.mp4", trim: 0.7, rate: 2.4},
  {id: "c04c", from: T.trio + 0.75, to: T.r1, src: "c04.mp4", trim: 1.3, rate: 0.55},
  // tres personalidades, tres escalas
  {id: "c05", from: T.r1, to: T.r2, src: "c05.mp4", trim: 0.6, rate: 1.2, zoom: 1.7, origin: "50% 44%", punch: 1.06},   // MACRO puño
  {id: "c06", from: T.r2, to: T.r3, src: "c06.mp4", trim: 0.2, rate: 1.2, zoom: 1.25, origin: "50% 30%", punch: 1.06},  // MEDIO corbatín
  {id: "c07", from: T.r3, to: T.prep, src: "c07.mp4", trim: 0.2, rate: 1.2, zoom: 1.0, punch: 1.06},                   // GENERAL solapa
  // preparación: manos a solapas, push lento; el microvacío es sólo de audio (la imagen sigue)
  {id: "c08", from: T.prep, to: T.reveal, src: "c08.mp4", trim: 0.4, rate: 1.3, push: [1.0, 1.08], origin: "50% 32%"},
  // HERO
  {id: "c09", from: T.reveal, to: T.porn, src: "c09.mp4", trim: 0.0, rate: 1.7, push: [1.22, 1.0], origin: "50% 45%", shake: true},
  {id: "c10", from: T.porn, to: T.porn + 0.4, src: "c10.mp4", trim: 1.0, rate: 1.5, punch: 1.05},
  {id: "c11", from: T.porn + 0.4, to: T.porn + 0.8, src: "c11.mp4", trim: 1.0, rate: 1.5, punch: 1.05},
  {id: "c12", from: T.porn + 0.8, to: T.puerta, src: "c12.mp4", trim: 1.0, rate: 1.5, punch: 1.05},
  {id: "c13", from: T.puerta, to: T.entran, src: "c13.mp4", trim: 0.3, rate: 1.8, burn: true},
  {id: "c14", from: T.entran, to: T.mesa, src: "c14.mp4", trim: 2.4, rate: 2.5, fromWhite: true},
  {id: "c15", from: T.mesa, to: T.end, src: "c15.mp4", trim: 0.3, rate: 1.3},
];

const Shot: React.FC<{p: Plano}> = ({p}) => {
  const frame = useCurrentFrame();
  const dur = F(p.to - p.from);
  const whip = p.whipIn ? interpolate(frame, [0, 4], [22, 0], {extrapolateRight: "clamp"}) : 0;
  const push = p.push ? interpolate(frame, [0, dur], p.push, {easing: (x) => 1 - Math.pow(1 - x, 3)}) : 1;
  const punch = p.punch ? interpolate(frame, [0, 3, dur], [p.punch, 1 + (p.punch - 1) * 0.3, 1.0], {extrapolateRight: "clamp"}) : 1;
  const shake = p.shake ? (frame === 1 ? 1.035 : frame === 2 ? 0.985 : frame === 3 ? 1.012 : 1) : 1;
  const burn = p.burn ? interpolate(frame, [dur - 9, dur], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 0;
  const white = p.fromWhite ? interpolate(frame, [0, 7], [1, 0], {extrapolateRight: "clamp"}) : 0;
  return (
    <AbsoluteFill style={{background: INK}}>
      <AbsoluteFill style={{transform: `scale(${push * punch * shake * (p.zoom ?? 1)})`, transformOrigin: p.origin ?? "50% 50%", filter: whip ? `blur(${whip}px)` : undefined}}>
        <Video src={staticFile(`${A}/clips/${p.src}`)} trimBefore={F(p.trim ?? 0)} playbackRate={p.rate ?? 1} volume={0} style={{width: "100%", height: "100%", objectFit: "cover"}} />
      </AbsoluteFill>
      {burn > 0 ? <AbsoluteFill style={{background: "#FFE9C4", opacity: burn}} /> : null}
      {white > 0 ? <AbsoluteFill style={{background: "#FFF3DC", opacity: white}} /> : null}
    </AbsoluteFill>
  );
};

const Titular: React.FC<{lineas: string[]; size?: number; color?: string; bottom?: number; top?: number; wdth?: number; wght?: number; tracking?: number; delay?: number}> =
  ({lineas, size = 96, color = BONE, bottom, top, wdth = 62, wght = 850, tracking, delay = 0}) => {
  const frame = useCurrentFrame() - delay;
  const {fps} = useVideoConfig();
  const enter = spring({fps, frame, config: {damping: 16, stiffness: 260, mass: 0.7}});
  const scale = interpolate(enter, [0, 1], [1.32, 1]);
  const tr = tracking ?? interpolate(enter, [0, 1], [0.12, 0.0]);
  const blur = interpolate(frame, [0, 3], [10, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{justifyContent: top !== undefined ? "flex-start" : "flex-end", alignItems: "center", paddingBottom: bottom ?? 0, paddingTop: top ?? 0}}>
      <div style={{opacity: frame < 0 ? 0 : 1, transform: `scale(${scale})`, filter: `blur(${blur}px)`, fontFamily: ARCHIVO, fontVariationSettings: `"wdth" ${wdth}, "wght" ${wght}`, fontSize: size, lineHeight: 0.94, letterSpacing: `${tr}em`, color, textAlign: "center", textTransform: "uppercase", textShadow: "0 8px 50px rgba(0,0,0,0.75)", padding: "0 50px"}}>
        {lineas.map((l, i) => <div key={i}>{l}</div>)}
      </div>
    </AbsoluteFill>
  );
};

/** LOS DE SIEMPRE. detrás de los personajes, con profundidad: sombra de contacto y un velo
 *  oscuro en la zona de las letras para que el trío se lea DELANTE. */
const HeroText: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({fps, frame: frame - 3, config: {damping: 13, stiffness: 220, mass: 0.7}});
  return (
    <AbsoluteFill style={{justifyContent: "center", alignItems: "center", opacity: interpolate(enter, [0, 1], [0, 1])}}>
      <div style={{transform: `scale(${interpolate(enter, [0, 1], [1.5, 1])}) translateY(-620px)`, fontFamily: ARCHIVO, fontVariationSettings: '"wdth" 62, "wght" 900', fontSize: 212, lineHeight: 0.9, color: MOSTAZA, textAlign: "center", letterSpacing: "-0.01em", textShadow: "0 14px 40px rgba(0,0,0,0.85), 0 0 120px rgba(232,179,37,0.25)"}}>
        LOS DE<br />SIEMPRE.
      </div>
    </AbsoluteFill>
  );
};

const SFX: {src: string; at: number; vol: number; dur?: number; base?: string}[] = [
  {src: "sfx-clack.mp3", at: T.c1, vol: 1.0}, {src: "sfx-impacto.mp3", at: T.c1, vol: 0.55},
  {src: "sfx-clack.mp3", at: T.c2, vol: 1.0}, {src: "sfx-impacto.mp3", at: T.c2, vol: 0.55},
  {src: "sfx-pasos.mp3", at: T.c3, vol: 0.9, dur: 0.4, base: "lds"}, {src: "sfx-impacto.mp3", at: T.c3, vol: 0.6},
  {src: "sfx-bass.mp3", at: T.boom, vol: 0.8}, {src: "sfx-camara.mp3", at: T.boom, vol: 0.5},
  {src: "sfx-whip.mp3", at: T.trio - 0.05, vol: 0.7},
  {src: "sfx-tela.mp3", at: T.r1, vol: 0.6, base: "lds"}, {src: "sfx-tela.mp3", at: T.r2, vol: 0.6, base: "lds"}, {src: "sfx-tela.mp3", at: T.r3, vol: 0.6, base: "lds"},
  {src: "sfx-camara.mp3", at: T.r1 - 0.04, vol: 0.5}, {src: "sfx-camara.mp3", at: T.r2 - 0.04, vol: 0.5}, {src: "sfx-camara.mp3", at: T.r3 - 0.04, vol: 0.5},
  {src: "sfx-tela.mp3", at: T.prep + 0.6, vol: 0.4, base: "lds"},
  {src: "sfx-bass.mp3", at: T.reveal, vol: 1.0}, {src: "sfx-golpe.mp3", at: T.reveal, vol: 0.7, base: "lds"}, {src: "sfx-solapas.mp3", at: T.reveal + 0.2, vol: 0.85, base: "lds"}, {src: "sfx-camara.mp3", at: T.reveal + 0.05, vol: 0.6},
  {src: "sfx-impacto.mp3", at: T.porn, vol: 0.55}, {src: "sfx-impacto.mp3", at: T.porn + 0.4, vol: 0.55}, {src: "sfx-impacto.mp3", at: T.porn + 0.8, vol: 0.55},
  {src: "sfx-brillo.mp3", at: T.porn, vol: 0.35}, {src: "sfx-brillo.mp3", at: T.porn + 0.4, vol: 0.35}, {src: "sfx-brillo.mp3", at: T.porn + 0.8, vol: 0.35},
  {src: "sfx-pasos.mp3", at: T.puerta, vol: 0.4, dur: 1.6, base: "lds"}, {src: "sfx-riser.mp3", at: T.entran - 2.0, vol: 0.8}, {src: "sfx-puerta.mp3", at: T.entran - 0.9, vol: 0.55, base: "lds"},
  {src: "sfx-oficina.mp3", at: T.entran, vol: 0.32, dur: 4.2, base: "lds"}, {src: "sfx-camara.mp3", at: T.mesa - 0.06, vol: 0.6},
  {src: "sfx-carpeta.mp3", at: T.mesa + 0.5, vol: 0.55}, {src: "sfx-taza.mp3", at: T.mesa + 1.6, vol: 0.55},
  {src: "sfx-bass.mp3", at: T.end, vol: 0.7}, {src: "sfx-impacto.mp3", at: T.end + 1.2, vol: 0.5},
];

export const LosDeSiempreEntranceV3: React.FC = () => {
  void fontPromise;
  return (
    <AbsoluteFill style={{background: INK}}>
      <Sequence from={F(T.reveal)} durationInFrames={F(T.porn - T.reveal)} layout="none"><HeroText /></Sequence>
      {PLANOS.map((p) => (
        <Sequence key={p.id} from={F(p.from)} durationInFrames={F(p.to - p.from)} layout="none">
          {p.id === "c09" ? (
            <AbsoluteFill style={{WebkitMaskImage: "linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.3) 15%, #000 27%, #000 100%)", maskImage: "linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.3) 15%, #000 27%, #000 100%)"}}><Shot p={p} /></AbsoluteFill>
          ) : <Shot p={p} />}
        </Sequence>
      ))}

      {/* Textos: por golpe, salen por corte */}
      <Sequence from={F(T.boom + 0.15)} durationInFrames={F(T.trio - T.boom - 0.15)} layout="none">
        <Titular lineas={["Ya se supo..."]} size={44} wdth={72} wght={700} tracking={0.18} bottom={250} />
      </Sequence>
      <Sequence from={F(T.trio + 0.3)} durationInFrames={F(T.r1 - T.trio - 0.3)} layout="none">
        <Titular lineas={["Vienen", "los de siempre."]} size={100} bottom={230} />
      </Sequence>
      <Sequence from={F(T.mesa + 0.5)} durationInFrames={F(T.end - T.mesa - 0.5)} layout="none">
        <Titular lineas={["Primera reunión."]} size={90} bottom={300} />
      </Sequence>
      <Sequence from={F(T.mesa + 1.6)} durationInFrames={F(T.end - T.mesa - 1.6)} layout="none">
        <Titular lineas={["Cero presentaciones."]} size={64} color={MOSTAZA} bottom={215} wght={650} />
      </Sequence>

      {/* End card: 2,5 s, dos placas, hard cut */}
      <Sequence from={F(T.end)} durationInFrames={F(T.fin - T.end)} layout="none">
        <AbsoluteFill style={{background: INK}} />
        <Sequence from={0} durationInFrames={F(1.25)} layout="none">
          <Titular lineas={["Los de siempre."]} size={118} bottom={1020} />
          <Titular lineas={["Ahora también", "en nuestra mesa."]} size={72} color={MOSTAZA} bottom={820} wght={700} delay={4} />
        </Sequence>
        <Sequence from={F(1.25)} layout="none">
          <Titular lineas={["Bienvenidos, Traverso."]} size={64} wdth={72} wght={700} bottom={1000} />
          <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: 740}}>
            <div style={{display: "flex", alignItems: "center", gap: 40}}>
              <Img src={staticFile("assets/traverso/logo-blanco.png")} style={{height: 104, objectFit: "contain"}} />
              <div style={{fontFamily: ARCHIVO, fontVariationSettings: '"wdth" 80, "wght" 300', fontSize: 54, color: BONE, opacity: 0.85}}>×</div>
              <Img src={staticFile("brand/copylab/copylab-white.png")} style={{height: 136, objectFit: "contain"}} />
            </div>
          </AbsoluteFill>
        </Sequence>
      </Sequence>

      <Audio src={staticFile(`${A}/audio/banda-v3.mp3`)} volume={0.95} />
      {SFX.map((s, i) => (
        <Sequence key={i} from={F(s.at)} durationInFrames={s.dur ? F(s.dur) : undefined} layout="none">
          <Audio src={staticFile(`${s.base === "lds" ? "assets/traverso/lds" : A}/audio/${s.src}`)} volume={s.vol} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
