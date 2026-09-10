/**
 * TRAVERSO × GRUPO COPYLAB — «LOS DE SIEMPRE · THE ENTRANCE» v2
 * ---------------------------------------------------------------
 * Feedback de Valeria sobre la v1 (09-09-2026, noche):
 *  · hook más potente al inicio → abre con «YA SE SUPO...» escrito a máquina sobre negro con un
 *    pulso grave, y los tres CLACK con micro push-in e impacto.
 *  · los textos pasan muy rápido y sin intención → entran con golpe (escala + tracking), se
 *    sostienen más y SALEN POR CORTE, no por fundido.
 *  · en la oficina se sentaban dos veces → sólo UNA: entran como rockstars (inicio de c14) y
 *    corte directo a la mesa (c15). Se eliminan «PRIMERA REUNIÓN / CERO PRESENTACIONES».
 *  · cierre con el logo ANIMADO de Copylab (el de GclOrigenReel: el punto viaja y el logo aparece)
 *    y el texto «Traverso. Los de siempre, ahora también en nuestra mesa. Bienvenidos a Grupo CopyLab.»
 *  · la música cambia: DROP parametrizado (const DROP) para cuadrar la pista nueva.
 * Los SFX de tela/solapas se mantienen (gustaron).
 */
import React from "react";
import {AbsoluteFill, Audio, Img, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {Video} from "@remotion/media";

export const ENT2_FPS = 24;
export const ENT2_W = 1080;
export const ENT2_H = 1920;
export const ENT2_DURATION = 25 * ENT2_FPS; // 600

const A = "assets/traverso/lds2";
const F = (s: number) => Math.round(s * ENT2_FPS);
const INK = "#050505";
const BONE = "#F2EEE7";
const MOSTAZA = "#E8B325";
const PINK = "#FF2D8D";
const CORAL = "#FF683D";
const ARCHIVO = "LDS Archivo";
const fontPromise =
  typeof FontFace !== "undefined"
    ? new FontFace(ARCHIVO, `url(${staticFile("assets/fonts/copywriters/Archivo-Variable.ttf")})`).load().then((f) => (document as any).fonts.add(f)).catch(() => undefined)
    : Promise.resolve();

// ---------------------------------------------------------------- timeline (segundos)
export const DROP = 9.2;            // el hit de la pista: el reveal cae acá
const T = {
  hook: 0.0,        // YA SE SUPO...
  clack1: 1.0, clack2: 1.5, clack3: 2.0,
  trio: 2.6,        // VIENEN LOS DE SIEMPRE.
  r1: 5.0, r2: 5.8, r3: 6.6,
  falso: 7.4,
  negro: DROP - 0.7,
  reveal: DROP,
  porn: DROP + 3.0,
  puerta: DROP + 4.4,
  entran: DROP + 6.7,
  mesa: DROP + 8.0,
  cierre: DROP + 10.6,  // ≈ 20,0
  fin: 25.0,
};
const MUSICA = "v2-drama.mp3";      // se reemplaza por la variante elegida

type Plano = {id: string; from: number; to: number; src: string; trim?: number; rate?: number; whipIn?: boolean; push?: [number, number]; origin?: string; burn?: boolean; punch?: boolean};
const PLANOS: Plano[] = [
  {id: "c01", from: T.clack1, to: T.clack2, src: "c01.mp4", trim: 0.0, punch: true},
  {id: "c02", from: T.clack2, to: T.clack3, src: "c02.mp4", trim: 0.3, punch: true},
  {id: "c03", from: T.clack3, to: T.trio, src: "c03.mp4", trim: 0.4, rate: 1.2, punch: true},
  {id: "c04a", from: T.trio, to: T.trio + 0.5, src: "c04.mp4", trim: 0.2, rate: 1, whipIn: true},
  {id: "c04b", from: T.trio + 0.5, to: T.trio + 0.75, src: "c04.mp4", trim: 0.7, rate: 2.4},
  {id: "c04c", from: T.trio + 0.75, to: T.r1, src: "c04.mp4", trim: 1.3, rate: 0.55},
  {id: "c05", from: T.r1, to: T.r2, src: "c05.mp4", trim: 0.2, rate: 1.2, whipIn: true},
  {id: "c06", from: T.r2, to: T.r3, src: "c06.mp4", trim: 0.2, rate: 1.2, whipIn: true},
  {id: "c07", from: T.r3, to: T.falso, src: "c07.mp4", trim: 0.2, rate: 1.2, whipIn: true},
  {id: "c08", from: T.falso, to: T.negro, src: "c08.mp4", trim: 0.3, rate: 1.3, push: [1.0, 1.07], origin: "50% 30%"},
  {id: "c09", from: T.reveal, to: T.porn, src: "c09.mp4", trim: 0.0, rate: 1.6, push: [1.18, 1.0], origin: "50% 45%"},
  {id: "c10", from: T.porn, to: T.porn + 0.45, src: "c10.mp4", trim: 1.0, rate: 1.5},
  {id: "c11", from: T.porn + 0.45, to: T.porn + 0.95, src: "c11.mp4", trim: 1.0, rate: 1.5},
  {id: "c12", from: T.porn + 0.95, to: T.puerta, src: "c12.mp4", trim: 1.0, rate: 1.5},
  {id: "c13", from: T.puerta, to: T.entran, src: "c13.mp4", trim: 0.5, rate: 1.7, burn: true},
  {id: "c14", from: T.entran, to: T.mesa, src: "c14.mp4", trim: 0.9, rate: 1.4},   // sólo la entrada, como rockstars
  {id: "c15", from: T.mesa, to: T.cierre, src: "c15.mp4", trim: 0.3, rate: 1.2},   // ya sentados: UNA sola vez
];

const Shot: React.FC<{p: Plano}> = ({p}) => {
  const frame = useCurrentFrame();
  const dur = F(p.to - p.from);
  const whip = p.whipIn ? interpolate(frame, [0, 4], [22, 0], {extrapolateRight: "clamp"}) : 0;
  const push = p.push ? interpolate(frame, [0, dur], p.push, {easing: (x) => 1 - Math.pow(1 - x, 3)}) : 1;
  const punch = p.punch ? interpolate(frame, [0, 3, dur], [1.12, 1.03, 1.0], {extrapolateRight: "clamp"}) : 1;
  const burn = p.burn ? interpolate(frame, [dur - 10, dur], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 0;
  return (
    <AbsoluteFill style={{background: INK}}>
      <AbsoluteFill style={{transform: `scale(${push * punch})`, transformOrigin: p.origin ?? "50% 50%", filter: whip ? `blur(${whip}px)` : undefined}}>
        <Video src={staticFile(`${A}/clips/${p.src}`)} trimBefore={F(p.trim ?? 0)} playbackRate={p.rate ?? 1} volume={0} style={{width: "100%", height: "100%", objectFit: "cover"}} />
      </AbsoluteFill>
      {burn > 0 ? <AbsoluteFill style={{background: "#FFE9C4", opacity: burn}} /> : null}
    </AbsoluteFill>
  );
};

/** Titular con intención: entra por golpe (escala 1,3→1 + tracking que se cierra + 2 f de blur)
 *  y SALE POR CORTE. Nada de fundidos. */
const Titular: React.FC<{lineas: string[]; size?: number; color?: string; bottom?: number; top?: number; wdth?: number; wght?: number; tracking?: number; delay?: number}> =
  ({lineas, size = 96, color = BONE, bottom, top, wdth = 62, wght = 850, tracking, delay = 0}) => {
  const frame = useCurrentFrame() - delay;
  const {fps} = useVideoConfig();
  const enter = spring({fps, frame, config: {damping: 16, stiffness: 260, mass: 0.7}});
  const scale = interpolate(enter, [0, 1], [1.32, 1]);
  const tr = tracking ?? interpolate(enter, [0, 1], [0.12, 0.0]);
  const blur = interpolate(frame, [0, 3], [10, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const opacity = frame < 0 ? 0 : 1;
  return (
    <AbsoluteFill style={{justifyContent: top !== undefined ? "flex-start" : "flex-end", alignItems: "center", paddingBottom: bottom ?? 0, paddingTop: top ?? 0}}>
      <div style={{opacity, transform: `scale(${scale})`, filter: `blur(${blur}px)`, fontFamily: ARCHIVO, fontVariationSettings: `"wdth" ${wdth}, "wght" ${wght}`, fontSize: size, lineHeight: 0.94, letterSpacing: `${tr}em`, color, textAlign: "center", textTransform: "uppercase", textShadow: "0 8px 50px rgba(0,0,0,0.75)", padding: "0 50px"}}>
        {lineas.map((l, i) => <div key={i}>{l}</div>)}
      </div>
    </AbsoluteFill>
  );
};

/** Texto escrito a máquina, carácter por carácter, con cursor. */
const Maquina: React.FC<{texto: string; paso?: number; size?: number; color?: string; top?: number; wdth?: number; wght?: number; align?: "center" | "left"; start?: number}> =
  ({texto, paso = 2, size = 64, color = BONE, top = 880, wdth = 75, wght = 700, start = 0}) => {
  const frame = useCurrentFrame() - start;
  const n = Math.max(0, Math.min(texto.length, Math.floor(frame / paso) + 1));
  const cursor = frame >= 0 && Math.floor(frame / 8) % 2 === 0 ? "▌" : " ";
  return (
    <AbsoluteFill style={{alignItems: "center", paddingTop: top}}>
      <div style={{fontFamily: ARCHIVO, fontVariationSettings: `"wdth" ${wdth}, "wght" ${wght}`, fontSize: size, color, letterSpacing: "0.06em", textTransform: "uppercase", whiteSpace: "pre-wrap", textAlign: "center", padding: "0 80px", lineHeight: 1.15}}>
        {texto.slice(0, n)}<span style={{opacity: 0.8}}>{frame >= 0 && n < texto.length ? cursor : ""}</span>
      </div>
    </AbsoluteFill>
  );
};

/** LOS DE SIEMPRE. enorme detrás de los personajes durante el reveal. */
const HeroText: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({fps, frame: frame - 5, config: {damping: 14, stiffness: 180, mass: 0.7}});
  return (
    <AbsoluteFill style={{justifyContent: "center", alignItems: "center", opacity: interpolate(enter, [0, 1], [0, 1])}}>
      <div style={{transform: `scale(${interpolate(enter, [0, 1], [1.4, 1])}) translateY(-620px)`, fontFamily: ARCHIVO, fontVariationSettings: '"wdth" 62, "wght" 900', fontSize: 210, lineHeight: 0.9, color: MOSTAZA, textAlign: "center", letterSpacing: "-0.01em", textShadow: "0 10px 60px rgba(0,0,0,0.6)"}}>
        LOS DE<br />SIEMPRE.
      </div>
    </AbsoluteFill>
  );
};

/** Cierre: texto a máquina + el logo animado de Copylab (adaptado de GclOrigenReel.CierreMarca:
 *  el punto viaja hasta su lugar en el isotipo y el logo aparece). */
const LOGO_W = 1000, LOGO_H = 889, LOGO_DOT = {x: 0.4156, y: 0.3315, r: 0.0615};
const salida = (t: number) => 1 - Math.pow(1 - t, 3);
const Cierre: React.FC<{dur: number}> = ({dur}) => {
  const frame = useCurrentFrame();
  const LOGO_BOX = {w: 820, h: (820 * LOGO_H) / LOGO_W};
  const LOGO_POS = {left: (1080 - LOGO_BOX.w) / 2, top: 1010};
  const llegada = {x: LOGO_POS.left + LOGO_DOT.x * LOGO_BOX.w, y: LOGO_POS.top + LOGO_DOT.y * LOGO_BOX.h, r: LOGO_DOT.r * LOGO_BOX.w};
  const partida = {x: 540, y: 1700, r: 10};
  const T0 = F(2.4);                       // el punto arranca cuando termina de escribirse el texto
  const viaje = interpolate(frame, [T0, T0 + 26], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: salida});
  const logo = interpolate(frame, [T0 + 16, T0 + 34], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const blanco = interpolate(frame, [T0 + 22, T0 + 36], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const px = partida.x + (llegada.x - partida.x) * viaje, py = partida.y + (llegada.y - partida.y) * viaje, pr = partida.r + (llegada.r - partida.r) * viaje;
  const traverso = interpolate(frame, [T0 + 30, T0 + 42], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{background: INK}}>
      <Maquina texto={"Traverso.\nLos de siempre,\nahora también en nuestra mesa."} paso={1.4} size={54} top={300} />
      <Maquina texto={"Bienvenidos a Grupo CopyLab."} paso={1.6} size={46} color={MOSTAZA} top={640} start={F(1.6)} />
      <AbsoluteFill style={{opacity: logo}}>
        <Img src={staticFile("brand/copylab/copylab-white.png")} style={{position: "absolute", left: LOGO_POS.left, top: LOGO_POS.top, width: LOGO_BOX.w, height: LOGO_BOX.h}} />
        {/* tapamos el punto del PNG para que el que viaja sea el único */}
        <div style={{position: "absolute", left: llegada.x - llegada.r - 2, top: llegada.y - llegada.r - 2, width: (llegada.r + 2) * 2, height: (llegada.r + 2) * 2, borderRadius: "50%", background: INK}} />
      </AbsoluteFill>
      {frame >= T0 ? (
        <>
          <div style={{position: "absolute", left: px - pr, top: py - pr, width: pr * 2, height: pr * 2, borderRadius: "50%", background: `linear-gradient(135deg, ${CORAL}, ${PINK})`, boxShadow: `0 0 ${30 * (1 - viaje)}px rgba(255,45,141,${0.8 * (1 - viaje)})`}} />
          <div style={{position: "absolute", left: px - pr, top: py - pr, width: pr * 2, height: pr * 2, borderRadius: "50%", background: "#fff", opacity: blanco}} />
        </>
      ) : null}
      <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: 220, opacity: traverso}}>
        <Img src={staticFile("assets/traverso/logo-blanco.png")} style={{height: 96, objectFit: "contain", opacity: 0.9}} />
      </AbsoluteFill>
      <AbsoluteFill style={{background: INK, opacity: interpolate(frame, [dur - 1, dur], [0, 0])}} />
    </AbsoluteFill>
  );
};

const SFX: {src: string; at: number; vol: number; dur?: number; base?: string}[] = [
  {src: "sfx-pulso.mp3", at: 0.0, vol: 0.8},
  ...Array.from({length: 10}, (_, i) => ({src: "sfx-tecla.mp3", at: 0.08 + i * 0.083, vol: 0.35})),
  {src: "sfx-clack.mp3", at: T.clack1, vol: 0.95}, {src: "sfx-impacto.mp3", at: T.clack1, vol: 0.5},
  {src: "sfx-clack.mp3", at: T.clack2, vol: 0.95}, {src: "sfx-impacto.mp3", at: T.clack2, vol: 0.5},
  {src: "sfx-clack.mp3", at: T.clack3, vol: 0.95}, {src: "sfx-impacto.mp3", at: T.clack3, vol: 0.5},
  {src: "sfx-pasos.mp3", at: T.clack3, vol: 0.7, dur: 0.6, base: "lds"},
  {src: "sfx-whip.mp3", at: T.trio - 0.05, vol: 0.7},
  {src: "sfx-tela.mp3", at: T.r1, vol: 0.55, base: "lds"}, {src: "sfx-tela.mp3", at: T.r2, vol: 0.55, base: "lds"}, {src: "sfx-tela.mp3", at: T.r3, vol: 0.55, base: "lds"},
  {src: "sfx-whip.mp3", at: T.r1 - 0.05, vol: 0.45}, {src: "sfx-whip.mp3", at: T.r2 - 0.05, vol: 0.45}, {src: "sfx-whip.mp3", at: T.r3 - 0.05, vol: 0.45},
  {src: "sfx-golpe.mp3", at: T.reveal, vol: 0.95, base: "lds"}, {src: "sfx-solapas.mp3", at: T.reveal + 0.25, vol: 0.75, base: "lds"},
  {src: "sfx-brillo.mp3", at: T.porn, vol: 0.4}, {src: "sfx-brillo.mp3", at: T.porn + 0.45, vol: 0.4}, {src: "sfx-brillo.mp3", at: T.porn + 0.95, vol: 0.4},
  {src: "sfx-pasos.mp3", at: T.puerta, vol: 0.35, dur: 1.8, base: "lds"}, {src: "sfx-puerta.mp3", at: T.puerta + 1.2, vol: 0.55, base: "lds"},
  {src: "sfx-oficina.mp3", at: T.entran, vol: 0.3, dur: 4.0, base: "lds"},
  {src: "sfx-carpeta.mp3", at: T.mesa + 0.4, vol: 0.5}, {src: "sfx-taza.mp3", at: T.mesa + 1.5, vol: 0.5},
  {src: "sfx-golpe.mp3", at: T.cierre, vol: 0.8, dur: 0.6, base: "lds"},
  {src: "sfx-impacto.mp3", at: T.cierre + 2.4, vol: 0.5},
];

export const LosDeSiempreEntranceV2: React.FC = () => {
  void fontPromise;
  return (
    <AbsoluteFill style={{background: INK}}>
      <Sequence from={F(T.reveal)} durationInFrames={F(T.porn - T.reveal)} layout="none"><HeroText /></Sequence>
      {PLANOS.map((p) => (
        <Sequence key={p.id} from={F(p.from)} durationInFrames={F(p.to - p.from)} layout="none">
          {p.id === "c09" ? (
            <AbsoluteFill style={{WebkitMaskImage: "linear-gradient(to bottom, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0.35) 14%, #000 26%, #000 100%)", maskImage: "linear-gradient(to bottom, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0.35) 14%, #000 26%, #000 100%)"}}><Shot p={p} /></AbsoluteFill>
          ) : <Shot p={p} />}
        </Sequence>
      ))}

      {/* HOOK: negro + YA SE SUPO... a máquina con pulso grave */}
      <Sequence from={F(T.hook)} durationInFrames={F(T.clack1 - T.hook)} layout="none">
        <AbsoluteFill style={{background: INK}} />
        <Maquina texto="Ya se supo..." paso={2} size={72} top={880} wght={800} wdth={68} />
      </Sequence>

      {/* Textos: entran por golpe, salen por corte */}
      <Sequence from={F(T.trio + 0.25)} durationInFrames={F(T.r1 - T.trio - 0.25)} layout="none">
        <Titular lineas={["Vienen", "los de siempre."]} size={100} bottom={230} />
      </Sequence>
      <Sequence from={F(T.negro)} durationInFrames={F(T.reveal - T.negro)} layout="none">
        <AbsoluteFill style={{background: INK}} />
        <Titular lineas={["¿Quiénes más?"]} size={96} bottom={900} />
      </Sequence>

      {/* Cierre con logo animado */}
      <Sequence from={F(T.cierre)} durationInFrames={F(T.fin - T.cierre)} layout="none">
        <Cierre dur={F(T.fin - T.cierre)} />
      </Sequence>

      {/* Música: muteada en el hook, entra con el primer CLACK */}
      <Sequence from={F(T.clack1)} layout="none">
        <Audio src={staticFile(`${A}/audio/${MUSICA}`)} trimBefore={0} volume={(f) => interpolate(f, [0, 3], [0, 0.95], {extrapolateRight: "clamp"})} />
      </Sequence>
      {SFX.map((s, i) => (
        <Sequence key={i} from={F(s.at)} durationInFrames={s.dur ? F(s.dur) : undefined} layout="none">
          <Audio src={staticFile(`${s.base === "lds" ? "assets/traverso/lds" : A}/audio/${s.src}`)} volume={s.vol} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
