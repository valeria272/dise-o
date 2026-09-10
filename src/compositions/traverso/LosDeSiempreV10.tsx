/**
 * TRAVERSO × GRUPO COPYLAB — «LOS DE SIEMPRE» V10 · CIERRE — focos → abren al tiro; copy grande; cierre con más personalidad (18,3 s · 24 fps)
 * ------------------------------------------------------------------------------
 * Dirección, composición, montaje y sonido. Personajes y clips intactos (salvo c17: la entrada con
 * la franja horizontal ARRIBA de las boquillas — arquitectura, no personajes).
 *
 * LA PRESENTACIÓN ESCÉNICA (en post, sobre el hero shot c08):
 *   3,58 se detienen en semioscuridad (silueta con brillos)
 *   4,04 CLACK foco IZQUIERDO · 4,26 CLACK CENTRO · 4,74 CLACK DERECHO — tres golpes reales de la canción;
 *        cada foco «destapa» la iluminación real del plano con una máscara elíptica
 *   4,74 aparece LOS DE SIEMPRE. (reveal 1: quiénes son) — sin fade
 *   5,2–6,15 manos a las solapas · 6,15–6,6 microvacío · 6,60 DROP: abren → etiquetas (reveal 2: qué marca)
 * ENTRADA: un solo plano hero (c17) → Ketchup pasa frente a lente (cola de c14) → reunión (c16).
 * CIERRE: dos cards. Último golpe 19,08 → negro seco 19,6.
 * Música: audio/banda-v10.mp3 (una pieza continua, offset 4,42). Eventos: 1,04 · 1,94 · 2,42 · 3,14 · 3,58 ·
 * 4,04 · 4,26 · 4,74 · 5,2 · 5,66 · 6,1 · vacío 6,15–6,6 · 6,60 · 9,36 · parada 11,58–12,08 · 12,58 · 14,58 · 17,08 · 19,08.
 */
import React from "react";
import {AbsoluteFill, Audio, Img, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {Video} from "@remotion/media";

export const V10_FPS = 24;
export const V10_W = 1080;
export const V10_H = 1920;
export const V10_DURATION = Math.round(20.9 * V10_FPS); // 502
const A = "assets/traverso/lds2";
const F = (s: number) => Math.round(s * V10_FPS);
const INK = "#050505", BONE = "#F2EEE7", MOSTAZA = "#E8B325", ARCHIVO = "LDS Archivo";
const fontPromise = typeof FontFace !== "undefined" ? new FontFace(ARCHIVO, `url(${staticFile("assets/fonts/copywriters/Archivo-Variable.ttf")})`).load().then((f) => (document as any).fonts.add(f)).catch(() => undefined) : Promise.resolve();

// banda-v10 (offset 6,02): macro 1,98 · paran 2,44 · CLACK 3,60 / 4,06 / 4,50 (bache natural debajo) ·
// DROP 5,00 = abren AL TIRO · 7,76 GRUPO COPYLAB · parada 9,98–10,48 (la puerta) · 10,98 sentados ·
// bajón 12,98 (CERO PRESENTACIONES) · 15,48 end card · HIT 17,48 · corte 18,3
// Feedback del equipo (Coni): menos negro antes de los focos (la caminata y el macro ocupan ese tiempo) y
// el primer end card se alarga para que se lea la segunda línea.
const T = {walk: 0.0, macro: 2.44, stop: 3.14, foco1: 3.6, foco2: 4.06, foco3: 4.5, reveal: 5.0,
  destino: 7.76, mesa: 9.98, end: 15.48, card2: 18.9, fin: 20.9};

type Plano = {id: string; from: number; to: number; src: string; trim?: number; rate?: number; punch?: number; zoom?: number; origin?: string; push?: [number, number];
  whipOut?: boolean; whipIn?: boolean; burn?: boolean; fromWhite?: boolean; wipeOut?: boolean; shake?: boolean; stage?: boolean};
const PLANOS: Plano[] = [
  {id: "walk",  from: T.walk, to: T.macro, src: "c04.mp4", trim: 0.20, rate: 1.0, punch: 1.06},
  {id: "macro", from: T.macro, to: T.stop, src: "c02.mp4", trim: 0.30, rate: 1.0, punch: 1.12},
  // ya detenidos: semisilueta; el escenario los presenta foco a foco
  // detenidos, quietos (c09 antes de abrirse): los focos los presentan y en el DROP abren AL TIRO
  {id: "stage", from: T.stop, to: T.reveal, src: "c09.mp4", trim: 0.0, rate: 0.55, push: [1.0, 1.04], origin: "50% 32%", stage: true},
  {id: "reveal", from: T.reveal, to: T.destino, src: "c09.mp4", trim: 1.4, rate: 1.4, push: [1.18, 1.0], origin: "50% 45%", shake: true},
  // entrada APROBADA: un plano hero; la luz de la puerta quema y se convierte en la sala
  {id: "destino", from: T.destino, to: T.mesa, src: "c17.mp4", trim: 0.4, rate: 1.9, burn: true},
  // YA están sentados. Nada entre medio.
  {id: "mesa", from: T.mesa, to: T.end, src: "c16.mp4", trim: 0.2, rate: 1.0, push: [1.0, 1.05], origin: "50% 45%", fromWhite: true},
];

/** Los tres focos: máscaras elípticas centradas en cada personaje que destapan la versión iluminada. */
const FOCOS = [
  {cx: "24%", cy: "36%", at: 3.6},
  {cx: "50%", cy: "32%", at: 4.06},
  {cx: "76%", cy: "36%", at: 4.5},
];

const Shot: React.FC<{p: Plano}> = ({p}) => {
  const frame = useCurrentFrame(); const dur = F(p.to - p.from);
  const push = p.push ? interpolate(frame, [0, dur], p.push, {easing: (x) => 1 - Math.pow(1 - x, 3)}) : 1;
  const punch = p.punch ? interpolate(frame, [0, 3, dur], [p.punch, 1 + (p.punch - 1) * 0.3, 1.0], {extrapolateRight: "clamp"}) : 1;
  const shake = p.shake ? (frame === 1 ? 1.035 : frame === 2 ? 0.985 : frame === 3 ? 1.012 : 1) : 1;
  const outX = p.whipOut ? interpolate(frame, [dur - 5, dur], [0, -22], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 0;
  const inX = p.whipIn ? interpolate(frame, [0, 5], [22, 0], {extrapolateRight: "clamp"}) : 0;
  const whipScale = 1 + Math.abs(outX + inX) / 22 * 0.55;
  const blur = Math.max(p.whipOut ? interpolate(frame, [dur - 5, dur], [0, 26], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 0, p.whipIn ? interpolate(frame, [0, 5], [26, 0], {extrapolateRight: "clamp"}) : 0);
  const burn = p.burn ? interpolate(frame, [dur - 8, dur], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 0;
  const white = p.fromWhite ? interpolate(frame, [0, 6], [1, 0], {extrapolateRight: "clamp"}) : 0;
  const wipe = p.wipeOut ? interpolate(frame, [dur - 4, dur], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 0;
  const transform = `translateX(${outX + inX}%) scale(${push * punch * shake * whipScale * (p.zoom ?? 1)})`;
  const video = <Video src={staticFile(`${A}/clips/${p.src}`)} trimBefore={F(p.trim ?? 0)} playbackRate={p.rate ?? 1} volume={0} style={{width: "100%", height: "100%", objectFit: "cover"}} />;
  if (p.stage) {
    // tiempo absoluto del plano dentro del reel
    const t = p.from + frame / V10_FPS;
    return (
      <AbsoluteFill style={{background: INK}}>
        {/* base: silueta en penumbra, conserva brillos (contraste alto) */}
        <AbsoluteFill style={{transform, transformOrigin: p.origin, filter: "brightness(0.26) contrast(1.4) saturate(0.7)"}}>{video}</AbsoluteFill>
        {/* cada foco destapa la iluminación real del plano; se enciende en 2 f con un pequeño sobreimpulso */}
        {FOCOS.map((f, i) => {
          const on = interpolate(t, [f.at, f.at + 0.06, f.at + 0.2], [0, 1.25, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
          if (on <= 0) return null;
          const mask = `radial-gradient(ellipse 30% 46% at ${f.cx} ${f.cy}, rgba(0,0,0,1) 0%, rgba(0,0,0,0.9) 45%, rgba(0,0,0,0.35) 72%, rgba(0,0,0,0) 100%)`;
          return (
            <AbsoluteFill key={i} style={{WebkitMaskImage: mask, maskImage: mask, opacity: Math.min(1, on)}}>
              <AbsoluteFill style={{transform, transformOrigin: p.origin, filter: `brightness(${on})`}}>{video}</AbsoluteFill>
            </AbsoluteFill>
          );
        })}
        {/* con los tres encendidos, el piso y el aire vuelven a su luz normal (el conjunto se abre) */}
        <AbsoluteFill style={{transform, transformOrigin: p.origin, opacity: interpolate(t, [T.foco3, T.foco3 + 0.12], [0, 0.9], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})}}>{video}</AbsoluteFill>
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{background: INK}}>
      <AbsoluteFill style={{transform, transformOrigin: p.origin ?? "50% 50%", filter: blur ? `blur(${blur}px)` : undefined}}>{video}</AbsoluteFill>
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
/** LOS DE SIEMPRE. cae en el tercer CLACK, sin fade: 3 f de golpe y se queda detrás de los personajes. */
const HeroText: React.FC = () => {
  const frame = useCurrentFrame(); const {fps} = useVideoConfig();
  const enter = spring({fps, frame, config: {damping: 12, stiffness: 300, mass: 0.6}});
  return (
    <AbsoluteFill style={{justifyContent: "center", alignItems: "center"}}>
      <div style={{transform: `scale(${interpolate(enter, [0, 1], [1.6, 1])}) translateY(-620px)`, fontFamily: ARCHIVO, fontVariationSettings: '"wdth" 62, "wght" 900', fontSize: 212, lineHeight: 0.9, color: MOSTAZA, textAlign: "center", letterSpacing: "-0.01em", textShadow: "0 14px 40px rgba(0,0,0,0.85), 0 0 120px rgba(232,179,37,0.25)"}}>LOS DE<br />SIEMPRE.</div>
    </AbsoluteFill>
  );
};

/** Titular con personalidad: cada línea entra por golpe (escala 1,5 → 1 con sobreimpulso, rotación −3° → 0,
 *  desenfoque 3 f) y con un escalón de 3 f entre líneas. Bold ancho, tracking negativo. */
const Golpe: React.FC<{lineas: string[]; size?: number; color?: string; bottom?: number; delay?: number}> = ({lineas, size = 100, color = BONE, bottom = 230, delay = 0}) => {
  const frame = useCurrentFrame() - delay; const {fps} = useVideoConfig();
  return (
    <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: bottom}}>
      <div style={{textAlign: "center", padding: "0 40px"}}>
        {lineas.map((l, i) => {
          const f = frame - i * 3;
          const e = spring({fps, frame: f, config: {damping: 9, stiffness: 320, mass: 0.6}});
          return (
            <div key={i} style={{opacity: f < 0 ? 0 : 1, transform: `scale(${interpolate(e, [0, 1], [1.5, 1])}) rotate(${interpolate(e, [0, 1], [-3, 0])}deg)`, filter: `blur(${interpolate(f, [0, 3], [12, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})}px)`, fontFamily: ARCHIVO, fontVariationSettings: '"wdth" 88, "wght" 900', fontSize: size, lineHeight: 0.92, letterSpacing: "-0.02em", color, textTransform: "uppercase", textShadow: "0 10px 50px rgba(0,0,0,0.8)"}}>{l}</div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/** TRAVERSO × GRUPO COPYLAB con peso visual parejo (ancho similar), 1,7× que en V8, y el último frame
 *  aguanta como gráfica de campaña: la animación termina en 0,4 s y quedan ≥ 1,5 s limpios. */
const LOGO_DOT = {x: 0.4156, y: 0.3315, r: 0.0615}; // el punto de la «g» dentro del PNG (1000×889)
const Marcas: React.FC = () => {
  const frame = useCurrentFrame(); const {fps} = useVideoConfig();
  const enter = spring({fps, frame: frame - 6, config: {damping: 11, stiffness: 240, mass: 0.7}});
  const op = interpolate(enter, [0, 1], [0, 1]); const y = interpolate(enter, [0, 1], [40, 0]);
  const CW = 370, CH = (CW * 889) / 1000;                 // caja del logo de Copylab
  const dot = {x: LOGO_DOT.x * CW, y: LOGO_DOT.y * CH, r: LOGO_DOT.r * CW};
  // el guiño: a los 0,9 s el punto se cierra (aplasta) y se abre, como un ojo
  const W0 = F(0.9);
  const wink = interpolate(frame, [W0, W0 + 3, W0 + 4, W0 + 8], [1, 0.08, 0.08, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: 580, opacity: op, transform: `translateY(${y}px) scale(${interpolate(enter, [0, 1], [1.15, 1])})`}}>
      <div style={{display: "flex", alignItems: "center", gap: 48}}>
        <Img src={staticFile("assets/traverso/logo-blanco.png")} style={{width: 460, objectFit: "contain"}} />
        <div style={{fontFamily: ARCHIVO, fontVariationSettings: '"wdth" 80, "wght" 300', fontSize: 84, color: BONE, opacity: 0.85}}>×</div>
        <div style={{position: "relative", width: CW, height: CH}}>
          <Img src={staticFile("brand/copylab/copylab-white.png")} style={{position: "absolute", left: 0, top: 0, width: CW, height: CH}} />
          {/* tapamos el punto del PNG y dibujamos el nuestro, que guiña */}
          <div style={{position: "absolute", left: dot.x - dot.r - 2, top: dot.y - dot.r - 2, width: (dot.r + 2) * 2, height: (dot.r + 2) * 2, borderRadius: "50%", background: INK}} />
          <div style={{position: "absolute", left: dot.x - dot.r, top: dot.y - dot.r, width: dot.r * 2, height: dot.r * 2, borderRadius: "50%", background: "#fff", transform: `scaleY(${wink})`}} />
        </div>
      </div>
    </AbsoluteFill>
  );
};

// Pocos SFX, de calidad: 3 CLACKs · acento · DROP (sub + tela) · puerta/aire · oficina · golpe final
const SFX: {src: string; at: number; vol: number; dur?: number; base?: string}[] = [
  {src: "sfx-pasos.mp3", at: 0.0, vol: 0.45, dur: 1.9, base: "lds"},
  {src: "sfx-tela.mp3", at: T.macro, vol: 0.5, base: "lds"},
  {src: "sfx-pasos.mp3", at: T.stop, vol: 0.35, dur: 0.4, base: "lds"},
  {src: "sfx-clack.mp3", at: T.foco1, vol: 0.9}, {src: "sfx-clack.mp3", at: T.foco2, vol: 0.9}, {src: "sfx-clack.mp3", at: T.foco3, vol: 1.0}, {src: "sfx-impacto.mp3", at: T.foco3, vol: 0.5},
  {src: "sfx-bass.mp3", at: T.reveal, vol: 1.0}, {src: "sfx-solapas.mp3", at: T.reveal + 0.1, vol: 0.85, base: "lds"},
  {src: "sfx-pasos.mp3", at: T.destino, vol: 0.35, dur: 1.4, base: "lds"}, {src: "sfx-riser.mp3", at: T.mesa - 1.1, vol: 0.55}, {src: "sfx-puerta.mp3", at: T.mesa - 0.45, vol: 0.6, base: "lds"},
  {src: "sfx-camara.mp3", at: T.mesa - 0.06, vol: 0.5}, {src: "sfx-oficina.mp3", at: T.mesa, vol: 0.28, dur: 5.5, base: "lds"}, {src: "sfx-carpeta.mp3", at: T.mesa + 0.8, vol: 0.45},
  {src: "sfx-impacto.mp3", at: 12.98, vol: 0.5},
  {src: "sfx-impacto.mp3", at: T.end, vol: 0.45}, {src: "sfx-bass.mp3", at: 19.98, vol: 0.28},
];

export const LosDeSiempreV10: React.FC = () => {
  void fontPromise;
  return (
    <AbsoluteFill style={{background: INK}}>
      {/* reveal 1: LOS DE SIEMPRE. en el tercer CLACK, detrás de los personajes hasta que termina el reveal 2 */}
      <Sequence from={F(T.foco3)} durationInFrames={F(T.destino - T.foco3)} layout="none"><HeroText /></Sequence>
      {PLANOS.map((p) => (
        <Sequence key={p.id} from={F(p.from)} durationInFrames={Math.max(1, F(p.to - p.from))} layout="none">
          {p.id === "stage" || p.id === "reveal"
            ? <AbsoluteFill style={{WebkitMaskImage: "linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.3) 15%, #000 27%, #000 100%)", maskImage: "linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.3) 15%, #000 27%, #000 100%)"}}><Shot p={p} /></AbsoluteFill>
            : <Shot p={p} />}
        </Sequence>
      ))}
      {/* reunión: dos textos con un beat de comedia entre medio */}
      <Sequence from={F(10.98)} durationInFrames={F(T.end - 10.98)} layout="none"><Titular lineas={["Primera reunión."]} size={88} bottom={360} /></Sequence>
      <Sequence from={F(12.98)} durationInFrames={F(T.end - 12.98)} layout="none"><Golpe lineas={["Cero", "presentaciones."]} size={112} color={MOSTAZA} bottom={150} /></Sequence>
      {/* cierre: DOS cards, golpe final y negro seco */}
      <Sequence from={F(T.end)} durationInFrames={F(T.fin - T.end)} layout="none">
        <AbsoluteFill style={{background: INK}} />
        <Sequence from={0} durationInFrames={F(T.card2 - T.end)} layout="none">
          <Golpe lineas={["Los de siempre."]} size={132} bottom={1040} />
          <Golpe lineas={["Ahora también", "en nuestra mesa."]} size={86} color={MOSTAZA} bottom={800} delay={5} />
        </Sequence>
        <Sequence from={F(T.card2 - T.end)} layout="none">
          <Golpe lineas={["Bienvenidos,", "Traverso."]} size={104} bottom={1040} />
          <Marcas />
        </Sequence>
      </Sequence>
      {/* la música baja desde el end card (15,48) para que el cierre se entienda: 0,95 → 0,35 hasta el golpe final, y muere en el negro */}
      <Audio src={staticFile(`${A}/audio/banda-v10.mp3`)} volume={(f) => interpolate(f, [F(T.end), F(17.0), F(T.card2), F(T.fin) - 2, F(T.fin)], [0.95, 0.4, 0.35, 0.22, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})} />
      {SFX.map((s, i) => (
        <Sequence key={i} from={F(s.at)} durationInFrames={s.dur ? F(s.dur) : undefined} layout="none">
          <Audio src={staticFile(`${s.base === "lds" ? "assets/traverso/lds" : A}/audio/${s.src}`)} volume={s.vol} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
