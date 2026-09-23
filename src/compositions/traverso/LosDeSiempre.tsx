/**
 * TRAVERSO × GRUPO COPYLAB — Reel de bienvenida «LOS DE SIEMPRE»
 * ----------------------------------------------------------------
 * Biblia: clients/traverso/reel-los-de-siempre/BIBLIA.md
 * 1080×1920 · 30 fps · 26 s. Los cortes salen de la música (musica-v3):
 * golpe 1 en 5,5 s (se encienden los focos) y golpe 2 en 11,0 s (el reveal).
 *
 * Reglas de montaje: hard cuts, nada de transiciones de IA ni efectos;
 * el audio propio de cada clip va muteado — la única cama es la pista.
 * Producto real: k08 es un composite PIL con los packshots reales, no IA.
 */
import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {Video} from "@remotion/media";

export const LDS_FPS = 30;
export const LDS_W = 1080;
export const LDS_H = 1920;
export const LDS_DURATION = 26 * LDS_FPS; // 780

const A = "assets/traverso/lds";
const F = (s: number) => Math.round(s * LDS_FPS);

// Tipografía: Archivo variable (condensada, pesada) — la voz de impacto del estudio.
const ARCHIVO = "LDS Archivo";
const fontPromise =
  typeof FontFace !== "undefined"
    ? new FontFace(ARCHIVO, `url(${staticFile("assets/fonts/copywriters/Archivo-Variable.ttf")})`)
        .load()
        .then((f) => {
          (document as any).fonts.add(f);
        })
        .catch(() => undefined)
    : Promise.resolve();

const INK = "#050505";
const BONE = "#F2EEE7";
const MOSTAZA = "#E8B325";

// ---------------------------------------------------------------- planos
type Plano = {
  id: string;
  from: number; // s
  to: number; // s
  src?: string; // video
  still?: string; // imagen
  trim?: number; // s dentro del clip
  rate?: number; // velocidad de reproducción
  push?: number; // escala final del push-in lento (desde 1)
  origin?: string;
};

const PLANOS: Plano[] = [
  {id: "c01", from: 0, to: 2.5, src: "clips/c01.mp4", trim: 0.3, rate: 1},
  {id: "c02", from: 2.5, to: 5.5, src: "clips/c02.mp4", trim: 0.4, rate: 1.3},
  {id: "c03", from: 5.5, to: 6.7, src: "clips/c03.mp4", trim: 0.1, rate: 1},
  {id: "c04", from: 6.7, to: 7.9, src: "clips/c04.mp4", trim: 0.1, rate: 1},
  {id: "c05", from: 7.9, to: 9.1, src: "clips/c05.mp4", trim: 0.2, rate: 1.2},
  {id: "c06", from: 9.1, to: 11.0, src: "clips/c06.mp4", trim: 0.5, rate: 1},
  {id: "c07", from: 11.0, to: 14.5, src: "clips/c07.mp4", trim: 0.0, rate: 1.4},
  {id: "k08", from: 14.5, to: 16.0, still: "keyframes/k08.png", push: 1.05, origin: "50% 62%"},
  {id: "c09", from: 16.0, to: 18.5, src: "clips/c09.mp4", trim: 0.6, rate: 1.6},
  {id: "k10", from: 18.5, to: 19.5, still: "keyframes/k10.png", push: 1.03, origin: "50% 45%"},
  {id: "c11", from: 19.5, to: 22.0, src: "clips/c11.mp4", trim: 0.3, rate: 1},
];

const Shot: React.FC<{p: Plano}> = ({p}) => {
  const frame = useCurrentFrame();
  const dur = F(p.to - p.from);
  const fadeIn = p.id === "c01" ? interpolate(frame, [0, 18], [0, 1], {extrapolateRight: "clamp"}) : 1;
  const scale = p.push ? interpolate(frame, [0, dur], [1, p.push]) : 1;
  return (
    <AbsoluteFill style={{background: INK, opacity: fadeIn}}>
      {p.src ? (
        <Video
          src={staticFile(`${A}/${p.src}`)}
          trimBefore={F(p.trim ?? 0)}
          playbackRate={p.rate ?? 1}
          volume={0}
          style={{width: "100%", height: "100%", objectFit: "cover"}}
        />
      ) : (
        <Img
          src={staticFile(`${A}/${p.still}`)}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
            transform: `scale(${scale})`,
            transformOrigin: p.origin ?? "50% 50%",
          }}
        />
      )}
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------- textos
/** Titular de teleserie: condensado, mayúsculas, entra por peso (tracking que se cierra). */
const Titular: React.FC<{
  lineas: string[];
  size?: number;
  color?: string;
  bottom?: number;
  dur: number; // frames que dura en pantalla
  outFade?: boolean;
}> = ({lineas, size = 96, color = BONE, bottom = 300, dur, outFade = true}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({fps, frame, config: {damping: 200, stiffness: 90, mass: 0.8}});
  const tracking = interpolate(enter, [0, 1], [0.22, 0.02]);
  const opacity = Math.min(
    interpolate(frame, [0, 8], [0, 1], {extrapolateRight: "clamp"}),
    outFade ? interpolate(frame, [dur - 8, dur], [1, 0], {extrapolateLeft: "clamp"}) : 1
  );
  return (
    <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: bottom}}>
      <div
        style={{
          opacity,
          fontFamily: ARCHIVO,
          fontVariationSettings: '"wdth" 62, "wght" 800',
          fontSize: size,
          lineHeight: 0.98,
          letterSpacing: `${tracking}em`,
          color,
          textAlign: "center",
          textTransform: "uppercase",
          textShadow: "0 6px 40px rgba(0,0,0,0.7)",
          padding: "0 70px",
        }}
      >
        {lineas.map((l, i) => (
          <div key={i}>{l}</div>
        ))}
      </div>
    </AbsoluteFill>
  );
};

/** End card: negro, titular en dos tiempos y los dos logos. */
const EndCard: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t1 = F(0.2);
  const t2 = F(2.0);
  const tLogos = F(2.6);
  const eLogo = spring({fps, frame: frame - tLogos, config: {damping: 200, stiffness: 80}});
  return (
    <AbsoluteFill style={{background: INK}}>
      <Sequence from={t1} durationInFrames={t2 - t1 + 6} layout="none">
        <Titular lineas={["Los de siempre", "tienen nueva agencia."]} size={92} bottom={1000} dur={t2 - t1 + 6} />
      </Sequence>
      <Sequence from={t2} layout="none">
        <Titular lineas={["Bienvenidos,", "Traverso."]} size={104} color={MOSTAZA} bottom={1000} dur={999} outFade={false} />
      </Sequence>
      <AbsoluteFill
        style={{
          justifyContent: "flex-end",
          alignItems: "center",
          paddingBottom: 560,
          opacity: interpolate(eLogo, [0, 1], [0, 1]),
          transform: `translateY(${interpolate(eLogo, [0, 1], [16, 0])}px)`,
        }}
      >
        <div style={{display: "flex", alignItems: "center", gap: 44}}>
          <Img src={staticFile("assets/traverso/logo-blanco.png")} style={{height: 118, objectFit: "contain"}} />
          <div
            style={{
              fontFamily: ARCHIVO,
              fontVariationSettings: '"wdth" 80, "wght" 300',
              fontSize: 58,
              color: BONE,
              opacity: 0.85,
            }}
          >
            ×
          </div>
          <Img src={staticFile("brand/copylab/copylab-white.png")} style={{height: 150, objectFit: "contain"}} />
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------- sonido
const SFX: {src: string; at: number; vol: number; dur?: number}[] = [
  {src: "sfx-pasos.mp3", at: 0.0, vol: 0.55, dur: 5.4},
  {src: "sfx-foco.mp3", at: 5.5, vol: 0.6},
  {src: "sfx-tela.mp3", at: 5.7, vol: 0.35},
  {src: "sfx-foco.mp3", at: 6.7, vol: 0.55},
  {src: "sfx-tela.mp3", at: 6.9, vol: 0.35},
  {src: "sfx-foco.mp3", at: 7.9, vol: 0.55},
  {src: "sfx-tela.mp3", at: 8.1, vol: 0.35},
  {src: "sfx-golpe.mp3", at: 11.0, vol: 0.85},
  {src: "sfx-solapas.mp3", at: 11.35, vol: 0.7},
  {src: "sfx-puerta.mp3", at: 17.2, vol: 0.5},
  {src: "sfx-oficina.mp3", at: 18.5, vol: 0.3, dur: 3.5},
];

export const LosDeSiempre: React.FC = () => {
  void fontPromise;
  return (
    <AbsoluteFill style={{background: INK}}>
      {PLANOS.map((p) => (
        <Sequence key={p.id} from={F(p.from)} durationInFrames={F(p.to - p.from)} layout="none">
          <Shot p={p} />
        </Sequence>
      ))}

      {/* Textos sobre imagen */}
      <Sequence from={F(3.2)} durationInFrames={F(2.2)} layout="none">
        <Titular lineas={["Hay clientes", "que llegan."]} size={88} dur={F(2.2)} bottom={260} />
      </Sequence>
      <Sequence from={F(9.3)} durationInFrames={F(1.65)} layout="none">
        <Titular lineas={["Y hay otros", "que hacen entrada."]} size={88} dur={F(1.65)} bottom={260} />
      </Sequence>
      <Sequence from={F(12.6)} durationInFrames={F(1.9)} layout="none">
        <Titular lineas={["Los de siempre."]} size={124} color={MOSTAZA} dur={F(1.9)} bottom={230} />
      </Sequence>

      {/* Cierre */}
      <Sequence from={F(22.0)} durationInFrames={F(4.0)} layout="none">
        <EndCard />
      </Sequence>

      {/* Sonido: la pista manda; los efectos van debajo */}
      <Audio src={staticFile(`${A}/audio/musica-v3.mp3`)} volume={0.9} />
      {SFX.map((s, i) => (
        <Sequence key={i} from={F(s.at)} durationInFrames={s.dur ? F(s.dur) : undefined} layout="none">
          <Audio src={staticFile(`${A}/audio/${s.src}`)} volume={s.vol} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
