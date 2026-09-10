/**
 * TRAVERSO × GRUPO COPYLAB — «LOS DE SIEMPRE» V7 · la presentación WOW, puerta → ya sentados con el equipo, cierre con logo animado (21 s · 24 fps)
 * ------------------------------------------------------------------------------------------
 * Una sola historia, una sola canción: LLEGAN → LOS DESCUBRIMOS → REVEAL → LLEGAN A GRUPO COPYLAB
 * → ENTRAN → YA ESTÁN EN LA REUNIÓN. Cada plano responde «¿qué ocurre después?».
 * Test obligatorio: sin textos y sin audio se tiene que entender que estos tres llegaron a Copylab.
 *
 * Música: audio/banda-v7.mp3 = A-garage-1 desde 1,52 s, sin empalmes; sólo se vacía 9,1–9,5.
 * Eventos medidos (scripts/beatmap.py): 1,62 · 2,32 · 2,78 · 3,24 · 3,94 · 4,84 · 5,32 · 6,04 ·
 * 6,48 (hit −9) · breakdown 8,5–9,0 · DROP 9,50 · 11,80 · parada 14,5–15,0 · 15,50 · 16,40 ·
 * 17,56 (bajón) · 20,08 · HIT 21,94 · corte 22,50.
 *
 *  0,00–3,24  HOOK: la caminata es la columna; se intercalan pie / smoking / boquilla al beat
 *  3,24–6,48  LOS DESCUBRIMOS: Suave (puño) → WHIP lateral → Tradicional (corbatín) → WHIP → Ketchup (solapa)
 *             → en el hit 6,48 volvemos al trío, que se detiene
 *  6,48–9,50  breakdown natural de la misma canción → manos a las solapas → vacío → DROP
 *  9,50–11,80 REVEAL: abren, LOS DE SIEMPRE.
 * 11,80–14,32 MATCH CUT al destino: de espaldas hacia la entrada GRUPO COPYLAB; la luz de la puerta quema
 * 14,32–15,50 cruzan: Ketchup pasa frente a lente → FOREGROUND WIPE (la banda para sola 14,5–15,0)
 * 15,50–20,08 ya están sentados. Microacciones. PRIMERA REUNIÓN. → CERO PRESENTACIONES.
 * 20,08–22,50 hard cut: LOS DE SIEMPRE. / AHORA TAMBIÉN EN NUESTRA MESA. → BIENVENIDOS, TRAVERSO. + marcas
 * Sin product porn: no responde a «¿qué ocurre después?».
 */
import React from "react";
import {AbsoluteFill, Audio, Img, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {Video} from "@remotion/media";

export const V7_FPS = 24;
export const V7_W = 1080;
export const V7_H = 1920;
export const V7_DURATION = Math.round(21.0 * V7_FPS); // 504
const A = "assets/traverso/lds2";
const F = (s: number) => Math.round(s * V7_FPS);
const INK = "#050505", BONE = "#F2EEE7", MOSTAZA = "#E8B325", ARCHIVO = "LDS Archivo";
const fontPromise = typeof FontFace !== "undefined" ? new FontFace(ARCHIVO, `url(${staticFile("assets/fonts/copywriters/Archivo-Variable.ttf")})`).load().then((f) => (document as any).fonts.add(f)).catch(() => undefined) : Promise.resolve();

// Eventos MEDIDOS de audio/banda-v7.mp3 (la misma canción, offset 4,42): 1,04 · 1,94 · 2,42 · 3,14 ·
// 3,58 (hit −9: paran) · breakdown 5,6–6,1 · vacío 6,15–6,6 · DROP 6,60 · 9,36 (corte a GRUPO COPYLAB) ·
// parada 11,58–12,08 (la puerta) · 12,58 (wipe → sentados) · bajón 14,58 · 17,08 (end card) · HIT 19,08 · corte 19,6
const T = {r1: 1.5, r2: 1.94, r3: 2.42, walkBack: 3.14, trio: 3.58, vacio: 6.15, reveal: 6.6, destino: 9.36, mesa: 12.08, end: 16.5, fin: 21.0};

type Plano = {id: string; from: number; to: number; src: string; trim?: number; rate?: number; punch?: number; zoom?: number; origin?: string; push?: [number, number];
  whipOut?: boolean; whipIn?: boolean; burn?: boolean; fromWhite?: boolean; wipeOut?: boolean; shake?: boolean; dark?: boolean; lightsOn?: boolean};
// La caminata (c04) es la columna del hook: cada vez que vuelve, sigue desde donde iba (trim = 0,2 + tiempo de reel)
const PLANOS: Plano[] = [
  // UNA sola entrada: trío en movimiento → macro → amarillo → dorado → rojo (acentos de 0,44–0,7 s) → trío
  {id: "walk",  from: 0.00, to: 1.04, src: "c04.mp4", trim: 0.20, rate: 1.0, punch: 1.08},
  {id: "smok",  from: 1.04, to: T.r1, src: "c02.mp4", trim: 0.30, rate: 1.0, punch: 1.12},
  {id: "suave", from: T.r1, to: T.r2, src: "c05.mp4", trim: 0.6, rate: 1.0, zoom: 1.6, origin: "50% 44%", punch: 1.08, whipOut: true},
  // dorado y rojo salen del PROPIO trío master (c09 antes de abrirse): idénticos al lock, sin desenfoque
  {id: "trad",  from: T.r2, to: T.r3, src: "c09.mp4", trim: 0.15, rate: 1.0, zoom: 1.9, origin: "50% 34%", punch: 1.06, whipIn: true, whipOut: true},
  {id: "ket",   from: T.r3, to: T.walkBack, src: "c09.mp4", trim: 0.15, rate: 1.0, zoom: 1.9, origin: "80% 36%", punch: 1.06, whipIn: true},
  {id: "walk2", from: T.walkBack, to: T.trio, src: "c04.mp4", trim: 3.34, rate: 0.8},
  // paran en el hit; manos a las solapas sobre el breakdown; vacío; DROP
  {id: "paran", from: T.trio, to: T.reveal, src: "c08.mp4", trim: 0.3, rate: 1.4, push: [1.0, 1.09], origin: "50% 32%", dark: true},
  {id: "reveal", from: T.reveal, to: T.destino, src: "c09.mp4", trim: 0.0, rate: 1.75, push: [1.22, 1.0], origin: "50% 45%", shake: true, lightsOn: true},
  // LOS DE SIEMPRE → packaging → CUT directo a GRUPO COPYLAB (UN solo plano desde atrás)
  {id: "destino", from: T.destino, to: T.mesa, src: "c13.mp4", trim: 0.3, rate: 1.75, burn: true},
  // la luz de la puerta se convierte en la sala: YA están sentados, leyendo el contrato, con el equipo de espaldas
  {id: "mesa", from: T.mesa, to: T.end, src: "c16.mp4", trim: 0.2, rate: 1.0, fromWhite: true, push: [1.0, 1.06], origin: "50% 45%"},
];

const Shot: React.FC<{p: Plano}> = ({p}) => {
  const frame = useCurrentFrame(); const dur = F(p.to - p.from);
  const push = p.push ? interpolate(frame, [0, dur], p.push, {easing: (x) => 1 - Math.pow(1 - x, 3)}) : 1;
  const punch = p.punch ? interpolate(frame, [0, 3, dur], [p.punch, 1 + (p.punch - 1) * 0.3, 1.0], {extrapolateRight: "clamp"}) : 1;
  const shake = p.shake ? (frame === 1 ? 1.035 : frame === 2 ? 0.985 : frame === 3 ? 1.012 : 1) : 1;
  // whip lateral: sale hacia la izquierda con desenfoque de movimiento; entra desde la derecha
  // el cuadro se agranda durante el barrido para que nunca asome negro en los bordes
  const outX = p.whipOut ? interpolate(frame, [dur - 5, dur], [0, -22], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 0;
  const inX = p.whipIn ? interpolate(frame, [0, 5], [22, 0], {extrapolateRight: "clamp"}) : 0;
  const whipScale = 1 + Math.abs(outX + inX) / 22 * 0.55;
  const blur = Math.max(p.whipOut ? interpolate(frame, [dur - 5, dur], [0, 26], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 0,
                        p.whipIn ? interpolate(frame, [0, 5], [26, 0], {extrapolateRight: "clamp"}) : 0);
  const burn = p.burn ? interpolate(frame, [dur - 9, dur], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 0;
  const white = p.fromWhite ? interpolate(frame, [0, 6], [1, 0], {extrapolateRight: "clamp"}) : 0;
  const wipe = p.wipeOut ? interpolate(frame, [dur - 4, dur], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 0;
  // luces apagadas: la escena baja a 35 % y se enfría un poco; en el reveal los focos se ENCIENDEN de golpe
  const dark = p.dark ? interpolate(frame, [0, 8], [0.7, 0.35], {extrapolateRight: "clamp"}) : 1;
  const lights = p.lightsOn ? interpolate(frame, [0, 2, 5], [0.35, 1.35, 1.0], {extrapolateRight: "clamp"}) : 1;
  return (
    <AbsoluteFill style={{background: INK}}>
      <AbsoluteFill style={{transform: `translateX(${outX + inX}%) scale(${push * punch * shake * whipScale * (p.zoom ?? 1)})`, transformOrigin: p.origin ?? "50% 50%", filter: `${blur ? `blur(${blur}px) ` : ""}brightness(${dark * lights})${p.dark ? " saturate(0.8)" : ""}`}}>
        <Video src={staticFile(`${A}/clips/${p.src}`)} trimBefore={F(p.trim ?? 0)} playbackRate={p.rate ?? 1} volume={0} style={{width: "100%", height: "100%", objectFit: "cover"}} />
      </AbsoluteFill>
      {burn > 0 ? <AbsoluteFill style={{background: "#FFE9C4", opacity: burn}} /> : null}
      {white > 0 ? <AbsoluteFill style={{background: "#FFF3DC", opacity: white}} /> : null}
      {wipe > 0 ? <AbsoluteFill style={{background: INK, opacity: wipe}} /> : null}
    </AbsoluteFill>
  );
};

const Titular: React.FC<{lineas: string[]; size?: number; color?: string; bottom?: number; wdth?: number; wght?: number; tracking?: number; delay?: number}> =
  ({lineas, size = 96, color = BONE, bottom = 230, wdth = 62, wght = 850, tracking, delay = 0}) => {
  const frame = useCurrentFrame() - delay; const {fps} = useVideoConfig();
  const enter = spring({fps, frame, config: {damping: 16, stiffness: 260, mass: 0.7}});
  const tr = tracking ?? interpolate(enter, [0, 1], [0.12, 0.0]);
  return (
    <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: bottom}}>
      <div style={{opacity: frame < 0 ? 0 : 1, transform: `scale(${interpolate(enter, [0, 1], [1.32, 1])})`, filter: `blur(${interpolate(frame, [0, 3], [10, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})}px)`, fontFamily: ARCHIVO, fontVariationSettings: `"wdth" ${wdth}, "wght" ${wght}`, fontSize: size, lineHeight: 0.94, letterSpacing: `${tr}em`, color, textAlign: "center", textTransform: "uppercase", textShadow: "0 8px 50px rgba(0,0,0,0.75)", padding: "0 50px"}}>
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

/** «Ahora en Grupo CopyLab» + el logo ANIMADO de Copylab (adaptado de GclOrigenReel.CierreMarca:
 *  el punto coral viaja hasta su lugar en la «g» y el logo aparece). */
const LOGO_W = 1000, LOGO_H = 889, LOGO_DOT = {x: 0.4156, y: 0.3315, r: 0.0615};
const salida = (t: number) => 1 - Math.pow(1 - t, 3);
const CierreCopylab: React.FC<{dur: number}> = ({dur}) => {
  const frame = useCurrentFrame(); const {fps} = useVideoConfig();
  const BOX = {w: 760, h: (760 * LOGO_H) / LOGO_W}; const POS = {left: (1080 - BOX.w) / 2, top: 780};
  const llegada = {x: POS.left + LOGO_DOT.x * BOX.w, y: POS.top + LOGO_DOT.y * BOX.h, r: LOGO_DOT.r * BOX.w};
  const partida = {x: 540, y: 1560, r: 8};
  const viaje = interpolate(frame, [4, 26], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: salida});
  const logo = interpolate(frame, [16, 32], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const blanco = interpolate(frame, [22, 34], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const px = partida.x + (llegada.x - partida.x) * viaje, py = partida.y + (llegada.y - partida.y) * viaje, pr = partida.r + (llegada.r - partida.r) * viaje;
  const enter = spring({fps, frame, config: {damping: 16, stiffness: 260, mass: 0.7}});
  return (
    <AbsoluteFill style={{background: INK}}>
      <AbsoluteFill style={{alignItems: "center", paddingTop: 560}}>
        <div style={{transform: `scale(${interpolate(enter, [0, 1], [1.3, 1])})`, fontFamily: ARCHIVO, fontVariationSettings: '"wdth" 68, "wght" 750', fontSize: 62, color: BONE, textTransform: "uppercase", letterSpacing: "0.02em", textAlign: "center"}}>Ahora en Grupo CopyLab.</div>
      </AbsoluteFill>
      <AbsoluteFill style={{opacity: logo}}>
        <Img src={staticFile("brand/copylab/copylab-white.png")} style={{position: "absolute", left: POS.left, top: POS.top, width: BOX.w, height: BOX.h}} />
        <div style={{position: "absolute", left: llegada.x - llegada.r - 2, top: llegada.y - llegada.r - 2, width: (llegada.r + 2) * 2, height: (llegada.r + 2) * 2, borderRadius: "50%", background: INK}} />
      </AbsoluteFill>
      {frame >= 4 ? (<>
        <div style={{position: "absolute", left: px - pr, top: py - pr, width: pr * 2, height: pr * 2, borderRadius: "50%", background: "linear-gradient(135deg, #FF683D, #FF2D8D)", boxShadow: `0 0 ${30 * (1 - viaje)}px rgba(255,45,141,${0.8 * (1 - viaje)})`}} />
        <div style={{position: "absolute", left: px - pr, top: py - pr, width: pr * 2, height: pr * 2, borderRadius: "50%", background: "#fff", opacity: blanco}} />
      </>) : null}
      <AbsoluteFill style={{background: INK, opacity: interpolate(frame, [dur - 1, dur], [0, 0])}} />
    </AbsoluteFill>
  );
};

// Sound design integrado con la canción, nunca compitiendo: pasos, tela, puerta, sub-hit del reveal, oficina sutil.
const SFX: {src: string; at: number; vol: number; dur?: number; base?: string}[] = [
  {src: "sfx-pasos.mp3", at: 0.0, vol: 0.45, dur: 1.0, base: "lds"}, {src: "sfx-tela.mp3", at: 1.04, vol: 0.45, base: "lds"},
  {src: "sfx-tela.mp3", at: T.r1, vol: 0.5, base: "lds"}, {src: "sfx-camara.mp3", at: T.r2 - 0.08, vol: 0.5}, {src: "sfx-camara.mp3", at: T.r3 - 0.08, vol: 0.5},
  {src: "sfx-pasos.mp3", at: T.walkBack, vol: 0.4, dur: 0.44, base: "lds"}, {src: "sfx-impacto.mp3", at: T.trio, vol: 0.45}, {src: "sfx-tela.mp3", at: T.trio + 1.0, vol: 0.4, base: "lds"},
  {src: "sfx-bass.mp3", at: T.reveal, vol: 0.95}, {src: "sfx-clack.mp3", at: T.reveal, vol: 0.9}, {src: "sfx-solapas.mp3", at: T.reveal + 0.2, vol: 0.8, base: "lds"}, {src: "sfx-camara.mp3", at: T.reveal + 0.05, vol: 0.5},
  {src: "sfx-impacto.mp3", at: T.destino, vol: 0.5}, {src: "sfx-pasos.mp3", at: T.destino, vol: 0.4, dur: 2.0, base: "lds"}, {src: "sfx-riser.mp3", at: T.mesa - 1.2, vol: 0.6}, {src: "sfx-puerta.mp3", at: T.mesa - 0.5, vol: 0.55, base: "lds"},
  {src: "sfx-camara.mp3", at: T.mesa - 0.08, vol: 0.55}, {src: "sfx-oficina.mp3", at: T.mesa, vol: 0.28, dur: 4.5, base: "lds"},
  {src: "sfx-carpeta.mp3", at: T.mesa + 0.6, vol: 0.5}, {src: "sfx-taza.mp3", at: T.mesa + 2.2, vol: 0.4},
  {src: "sfx-bass.mp3", at: 19.08, vol: 0.85}, {src: "sfx-impacto.mp3", at: 20.55, vol: 0.4},
];

export const LosDeSiempreV7: React.FC = () => {
  void fontPromise;
  return (
    <AbsoluteFill style={{background: INK}}>
      <Sequence from={F(T.reveal)} durationInFrames={F(T.destino - T.reveal)} layout="none"><HeroText /></Sequence>
      {PLANOS.map((p) => (
        <Sequence key={p.id} from={F(p.from)} durationInFrames={Math.max(1, F(p.to - p.from))} layout="none">
          {p.id === "reveal" ? <AbsoluteFill style={{WebkitMaskImage: "linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.3) 15%, #000 27%, #000 100%)", maskImage: "linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.3) 15%, #000 27%, #000 100%)"}}><Shot p={p} /></AbsoluteFill> : <Shot p={p} />}
        </Sequence>
      ))}
      {/* copy: sólo el que aporta concepto */}
      <Sequence from={F(13.5)} durationInFrames={F(T.end - 13.5)} layout="none"><Titular lineas={["Primera reunión."]} size={84} bottom={300} /></Sequence>
      <Sequence from={F(14.58)} durationInFrames={F(T.end - 14.58)} layout="none"><Titular lineas={["Cero presentaciones."]} size={64} color={MOSTAZA} bottom={215} wght={650} /></Sequence>
      <Sequence from={F(T.end)} durationInFrames={F(T.fin - T.end)} layout="none">
        <AbsoluteFill style={{background: INK}} />
        <Sequence from={0} durationInFrames={F(1.1)} layout="none">
          <Titular lineas={["Los de siempre."]} size={118} bottom={1020} />
          <Titular lineas={["Ahora también", "en nuestra mesa."]} size={72} color={MOSTAZA} bottom={820} wght={700} delay={4} />
        </Sequence>
        <Sequence from={F(1.1)} durationInFrames={F(1.2)} layout="none">
          <Titular lineas={["Bienvenidos, Traverso."]} size={72} wdth={68} wght={750} bottom={1000} />
          <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: 760}}>
            <Img src={staticFile("assets/traverso/logo-blanco.png")} style={{height: 150, objectFit: "contain"}} />
          </AbsoluteFill>
        </Sequence>
        <Sequence from={F(2.3)} layout="none"><CierreCopylab dur={F(T.fin - T.end - 2.3)} /></Sequence>
      </Sequence>
      <Audio src={staticFile(`${A}/audio/banda-v7.mp3`)} volume={0.95} />
      {SFX.map((s, i) => (
        <Sequence key={i} from={F(s.at)} durationInFrames={s.dur ? F(s.dur) : undefined} layout="none">
          <Audio src={staticFile(`${s.base === "lds" ? "assets/traverso/lds" : A}/audio/${s.src}`)} volume={s.vol} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
