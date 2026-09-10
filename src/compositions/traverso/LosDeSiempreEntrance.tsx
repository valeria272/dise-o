/**
 * TRAVERSO × GRUPO COPYLAB — «LOS DE SIEMPRE · THE ENTRANCE»
 * ------------------------------------------------------------
 * Paquete aprobado: clients/traverso/reel-los-de-siempre/EDICION-THE-ENTRANCE.md
 * 1080×1920 · 24 fps · 24 s. La edición está coreografiada sobre los beats MEDIDOS de
 * public/assets/traverso/lds2/audio/musica-entrance.mp3: silencio 8,0–8,9 · HIT 9,0 ·
 * golpes finales 23,15 y 23,55.
 *
 * Transiciones que nacen de la acción (sin plantillas): hard cuts en los CLACK, whip pans
 * de 4 f en la ráfaga, smash cut a negro, match cuts en los macros, light match cut (la
 * puerta quema a blanco cálido), foreground wipe (el smoking de Ketchup tapa la lente),
 * smash to black final sin fade. Speed ramp en K03 hecho en montaje.
 */
import React from "react";
import {AbsoluteFill, Audio, Img, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {Video} from "@remotion/media";

export const ENT_FPS = 24;
export const ENT_W = 1080;
export const ENT_H = 1920;
export const ENT_DURATION = 24 * ENT_FPS; // 576

const A = "assets/traverso/lds2";
const F = (s: number) => Math.round(s * ENT_FPS);
const INK = "#050505";
const BONE = "#F2EEE7";
const MOSTAZA = "#E8B325";
const ARCHIVO = "LDS Archivo";
const fontPromise =
  typeof FontFace !== "undefined"
    ? new FontFace(ARCHIVO, `url(${staticFile("assets/fonts/copywriters/Archivo-Variable.ttf")})`).load().then((f) => (document as any).fonts.add(f)).catch(() => undefined)
    : Promise.resolve();

type Plano = {
  id: string; from: number; to: number; src: string; trim?: number; rate?: number;
  whipIn?: boolean;        // desenfoque horizontal de entrada (4 f)
  push?: [number, number]; // escala inicio→fin
  origin?: string;
  burn?: boolean;          // la luz quema a blanco cálido al final (K08)
  wipeOut?: boolean;       // oscurece al final (K09: el smoking tapa la lente)
  fadeFromBlack?: number;  // frames
};

const PLANOS: Plano[] = [
  {id: "c01", from: 0.0, to: 0.6, src: "c01.mp4", trim: 0.0},
  {id: "c02", from: 0.6, to: 1.25, src: "c02.mp4", trim: 0.3},
  {id: "c03", from: 1.25, to: 2.0, src: "c03.mp4", trim: 0.4, rate: 1.2},
  // Speed ramp de K03 en tres tramos con velocidad constante (trim = tiempo de origen al inicio del tramo)
  {id: "c04a", from: 2.0, to: 2.5, src: "c04.mp4", trim: 0.2, rate: 1, whipIn: true},
  {id: "c04b", from: 2.5, to: 2.75, src: "c04.mp4", trim: 0.7, rate: 2.4},
  {id: "c04c", from: 2.75, to: 4.5, src: "c04.mp4", trim: 1.3, rate: 0.55},
  {id: "c05", from: 4.5, to: 5.3, src: "c05.mp4", trim: 0.2, rate: 1.2, whipIn: true},
  {id: "c06", from: 5.3, to: 6.1, src: "c06.mp4", trim: 0.2, rate: 1.2, whipIn: true},
  {id: "c07", from: 6.1, to: 7.0, src: "c07.mp4", trim: 0.2, rate: 1.2, whipIn: true},
  {id: "c08", from: 7.0, to: 8.4, src: "c08.mp4", trim: 0.3, rate: 1.3, push: [1.0, 1.06], origin: "50% 30%"},
  // 8,4–9,0 NEGRO (¿QUIÉNES MÁS?)
  {id: "c09", from: 9.0, to: 12.0, src: "c09.mp4", trim: 0.0, rate: 1.6, push: [1.18, 1.0], origin: "50% 45%"},
  {id: "c10", from: 12.0, to: 12.45, src: "c10.mp4", trim: 1.0, rate: 1.5},
  {id: "c11", from: 12.45, to: 12.95, src: "c11.mp4", trim: 1.0, rate: 1.5},
  {id: "c12", from: 12.95, to: 13.5, src: "c12.mp4", trim: 1.0, rate: 1.5},
  {id: "c13", from: 13.5, to: 16.0, src: "c13.mp4", trim: 0.5, rate: 1.6, burn: true},
  {id: "c14", from: 16.0, to: 18.0, src: "c14.mp4", trim: 0.9, rate: 2.0, wipeOut: true, fadeFromBlack: 0},
  {id: "c15", from: 18.0, to: 21.0, src: "c15.mp4", trim: 0.3, rate: 1.2},
];

const Shot: React.FC<{p: Plano}> = ({p}) => {
  const frame = useCurrentFrame();
  const dur = F(p.to - p.from);
  const whip = p.whipIn ? interpolate(frame, [0, 4], [22, 0], {extrapolateRight: "clamp"}) : 0;
  const scale = p.push ? interpolate(frame, [0, dur], p.push, {easing: (x) => 1 - Math.pow(1 - x, 3)}) : 1;
  const burn = p.burn ? interpolate(frame, [dur - 10, dur], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 0;
  const wipe = p.wipeOut ? interpolate(frame, [dur - 6, dur], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 0;
  const fadeIn = p.fadeFromBlack ? interpolate(frame, [0, p.fadeFromBlack], [0, 1], {extrapolateRight: "clamp"}) : 1;
  const rate = p.rate ?? 1;
  return (
    <AbsoluteFill style={{background: INK}}>
      <AbsoluteFill style={{opacity: fadeIn, transform: `scale(${scale})`, transformOrigin: p.origin ?? "50% 50%", filter: whip ? `blur(${whip}px)` : undefined}}>
        <Video src={staticFile(`${A}/clips/${p.src}`)} trimBefore={F(p.trim ?? 0)} playbackRate={rate} volume={0} style={{width: "100%", height: "100%", objectFit: "cover"}} />
      </AbsoluteFill>
      {burn > 0 ? <AbsoluteFill style={{background: "#FFE9C4", opacity: burn}} /> : null}
      {wipe > 0 ? <AbsoluteFill style={{background: INK, opacity: wipe}} /> : null}
    </AbsoluteFill>
  );
};

const Titular: React.FC<{lineas: string[]; size?: number; color?: string; bottom?: number; top?: number; dur: number; fadeOut?: boolean; wdth?: number; wght?: number; tracking?: number}> =
  ({lineas, size = 96, color = BONE, bottom, top, dur, fadeOut = true, wdth = 62, wght = 800, tracking}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({fps, frame, config: {damping: 200, stiffness: 120, mass: 0.6}});
  const tr = tracking ?? interpolate(enter, [0, 1], [0.18, 0.02]);
  const opacity = Math.min(interpolate(frame, [0, 4], [0, 1], {extrapolateRight: "clamp"}), fadeOut ? interpolate(frame, [dur - 4, dur], [1, 0], {extrapolateLeft: "clamp"}) : 1);
  return (
    <AbsoluteFill style={{justifyContent: top !== undefined ? "flex-start" : "flex-end", alignItems: "center", paddingBottom: bottom ?? 0, paddingTop: top ?? 0}}>
      <div style={{opacity, fontFamily: ARCHIVO, fontVariationSettings: `"wdth" ${wdth}, "wght" ${wght}`, fontSize: size, lineHeight: 0.96, letterSpacing: `${tr}em`, color, textAlign: "center", textTransform: "uppercase", textShadow: "0 6px 40px rgba(0,0,0,0.7)", padding: "0 60px"}}>
        {lineas.map((l, i) => <div key={i}>{l}</div>)}
      </div>
    </AbsoluteFill>
  );
};

/** LOS DE SIEMPRE. enorme detrás de los personajes: la capa de texto va DEBAJO del clip recortado
 *  por una máscara suave del centro (los personajes tapan parte de las letras). */
const HeroText: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({fps, frame: frame - 6, config: {damping: 200, stiffness: 140, mass: 0.6}});
  const scale = interpolate(enter, [0, 1], [1.25, 1]);
  const opacity = interpolate(enter, [0, 1], [0, 1]);
  return (
    <AbsoluteFill style={{justifyContent: "center", alignItems: "center", opacity}}>
      <div style={{transform: `scale(${scale}) translateY(-620px)`, fontFamily: ARCHIVO, fontVariationSettings: '"wdth" 62, "wght" 900', fontSize: 210, lineHeight: 0.9, color: MOSTAZA, textAlign: "center", letterSpacing: "-0.01em", textShadow: "0 10px 60px rgba(0,0,0,0.6)"}}>
        LOS DE<br />SIEMPRE.
      </div>
    </AbsoluteFill>
  );
};

const SFX: {src: string; at: number; vol: number; dur?: number; base?: string}[] = [
  {src: "sfx-clack.mp3", at: 0.0, vol: 0.9}, {src: "sfx-clack.mp3", at: 0.6, vol: 0.9}, {src: "sfx-clack.mp3", at: 1.25, vol: 0.9},
  {src: "sfx-pasos.mp3", at: 1.25, vol: 0.7, dur: 0.75, base: "lds"},
  {src: "sfx-whip.mp3", at: 1.95, vol: 0.7},
  {src: "sfx-tela.mp3", at: 4.5, vol: 0.5, base: "lds"}, {src: "sfx-tela.mp3", at: 5.3, vol: 0.5, base: "lds"}, {src: "sfx-tela.mp3", at: 6.1, vol: 0.5, base: "lds"},
  {src: "sfx-whip.mp3", at: 4.45, vol: 0.45}, {src: "sfx-whip.mp3", at: 5.25, vol: 0.45}, {src: "sfx-whip.mp3", at: 6.05, vol: 0.45},
  {src: "sfx-golpe.mp3", at: 9.0, vol: 0.9, base: "lds"}, {src: "sfx-solapas.mp3", at: 9.25, vol: 0.7, base: "lds"},
  {src: "sfx-brillo.mp3", at: 12.0, vol: 0.4}, {src: "sfx-brillo.mp3", at: 12.45, vol: 0.4}, {src: "sfx-brillo.mp3", at: 12.95, vol: 0.4},
  {src: "sfx-pasos.mp3", at: 13.5, vol: 0.35, dur: 2.0, base: "lds"}, {src: "sfx-puerta.mp3", at: 14.8, vol: 0.55, base: "lds"},
  {src: "sfx-oficina.mp3", at: 16.0, vol: 0.3, dur: 5.0, base: "lds"},
  {src: "sfx-carpeta.mp3", at: 18.4, vol: 0.5}, {src: "sfx-taza.mp3", at: 19.6, vol: 0.5},
  {src: "sfx-golpe.mp3", at: 23.5, vol: 0.8, dur: 0.5, base: "lds"},
];

export const LosDeSiempreEntrance: React.FC = () => {
  void fontPromise;
  return (
    <AbsoluteFill style={{background: INK}}>
      {/* LOS DE SIEMPRE. detrás de los personajes durante el reveal */}
      <Sequence from={F(9.0)} durationInFrames={F(3.0)} layout="none"><HeroText /></Sequence>

      {PLANOS.map((p) => (
        <Sequence key={p.id} from={F(p.from)} durationInFrames={F(p.to - p.from)} layout="none">
          {p.id === "c09" ? (
            // el clip del reveal va con un agujero suave arriba para que las letras asomen detrás
            <AbsoluteFill style={{WebkitMaskImage: "linear-gradient(to bottom, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0.35) 14%, #000 26%, #000 100%)", maskImage: "linear-gradient(to bottom, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0.35) 14%, #000 26%, #000 100%)"}}>
              <Shot p={p} />
            </AbsoluteFill>
          ) : (
            <Shot p={p} />
          )}
        </Sequence>
      ))}

      {/* Textos */}
      <Sequence from={F(0.6)} durationInFrames={F(1.4)} layout="none">
        <Titular lineas={["Se supo."]} size={34} wdth={80} wght={500} tracking={0.3} top={1500} dur={F(1.4)} />
      </Sequence>
      <Sequence from={F(2.3)} durationInFrames={F(2.2)} layout="none">
        <Titular lineas={["Vienen", "los de siempre."]} size={92} bottom={230} dur={F(2.2)} />
      </Sequence>
      <Sequence from={F(8.4)} durationInFrames={F(0.6)} layout="none">
        <AbsoluteFill style={{background: INK}} />
        <Titular lineas={["¿Quiénes más?"]} size={84} bottom={900} dur={F(0.6)} fadeOut={false} />
      </Sequence>
      <Sequence from={F(18.4)} durationInFrames={F(2.6)} layout="none">
        <Titular lineas={["Primera reunión."]} size={88} bottom={300} dur={F(2.6)} fadeOut={false} />
      </Sequence>
      <Sequence from={F(19.4)} durationInFrames={F(1.6)} layout="none">
        <Titular lineas={["Cero presentaciones."]} size={64} color={MOSTAZA} bottom={215} dur={F(1.6)} fadeOut={false} wght={600} />
      </Sequence>

      {/* Final: smash to black, sin fade */}
      <Sequence from={F(21.0)} durationInFrames={F(3.0)} layout="none">
        <AbsoluteFill style={{background: INK}} />
        <Sequence from={0} durationInFrames={F(1.0)} layout="none"><Titular lineas={["Los de siempre."]} size={124} bottom={960} dur={F(1.0)} fadeOut={false} /></Sequence>
        <Sequence from={F(1.0)} durationInFrames={F(1.15)} layout="none"><Titular lineas={["Ahora también", "en nuestra mesa."]} size={100} color={MOSTAZA} bottom={920} dur={F(1.15)} fadeOut={false} /></Sequence>
        <Sequence from={F(2.15)} layout="none">
          <Titular lineas={["Bienvenidos, Traverso."]} size={54} wdth={75} wght={600} bottom={1040} dur={999} fadeOut={false} />
          <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: 760}}>
            <div style={{display: "flex", alignItems: "center", gap: 40}}>
              <Img src={staticFile("assets/traverso/logo-blanco.png")} style={{height: 110, objectFit: "contain"}} />
              <div style={{fontFamily: ARCHIVO, fontVariationSettings: '"wdth" 80, "wght" 300', fontSize: 54, color: BONE, opacity: 0.85}}>×</div>
              <Img src={staticFile("brand/copylab/copylab-white.png")} style={{height: 140, objectFit: "contain"}} />
            </div>
          </AbsoluteFill>
        </Sequence>
      </Sequence>

      {/* Sonido: música muteada 0–2 s (cold open sólo con CLACKs), entra fuerte en 2,0 */}
      <Sequence from={F(2.0)} layout="none">
        <Audio src={staticFile(`${A}/audio/musica-entrance.mp3`)} trimBefore={F(2.0)} volume={(f) => interpolate(f, [0, 3], [0, 0.95], {extrapolateRight: "clamp"})} />
      </Sequence>
      {SFX.map((s, i) => (
        <Sequence key={i} from={F(s.at)} durationInFrames={s.dur ? F(s.dur) : undefined} layout="none">
          <Audio src={staticFile(`${s.base === "lds" ? "assets/traverso/lds" : A}/audio/${s.src}`)} volume={s.vol} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
