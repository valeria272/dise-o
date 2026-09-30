/**
 * SANTA GOTA × GRUPO COPYLAB — reel de BIENVENIDA para @copywriters.cl (30-09-2026 · 24 fps · 1080×1920)
 * ------------------------------------------------------------------------------
 * Base: el reel más potente que hicimos para la cuenta desde septiembre, medido en la API de Instagram
 * el 30-09 — «Somos de quienes nunca piden permiso para pecar en la cocina» (07-09, la monja):
 * 4.809 reproducciones · 3.197 cuentas · 243 compartidos · 407 interacciones (el siguiente, el spot
 * vertical del 29-09, iba en 3.068 / 94). Se usa el máster 1080×1920 sin tocar: ni un corte, ni un texto.
 *
 * CIERRE (misma gramática que la bienvenida de Traverso V10): corte seco a negro sobre el final del reel,
 * «BIENVENIDOS, / SANTA GOTA.» por golpes (Archivo, la voz de Copywriters) con el nombre en el lima de la
 * marca, y la dupla de logos Santa Gota × Grupo Copylab con peso visual parejo.
 *
 * MÚSICA (ronda 2, Valeria: «el cierre con un tum, bajo la misma música del reel»): la canción del reel se
 * ESTIRA, no se agrega nada. ~142 bpm (pulso 0,4209 s). Al llegar a 10,975 s vuelve a 8,445 s (6 pulsos,
 * ambos cortes en el valle justo antes de un golpe, fundido de 15 ms) → el golpe final del reel (10,99) cae
 * en 13,52 s, sobre los logos. Pista: bienvenida/musica-extendida.wav. El logo del reel se congela 5 cuadros
 * para que el corte a negro caiga en pulso (12,67 s).
 */
import React from "react";
import {AbsoluteFill, Audio, Freeze, Img, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {Video} from "@remotion/media";

export const SGB_FPS = 24;
export const SGB_W = 1080;
export const SGB_H = 1920;
const REEL = 299;                       // 12,46 s del máster
const CORTE = 304;                      // 12,67 s — pulso de la música (el último cuadro del reel se congela 5 f)
const TUM = 325;                        // 13,54 s — el golpe final del reel, estirado
export const SGB_DURATION = TUM + 36;   // termina con la cola del golpe (la canción se apaga en 14,7): sin hueco mudo en el loop

const INK = "#050505", BONE = "#F2EEE7", LIMA = "#C3D600", ARCHIVO = "SGB Archivo";
const fontPromise = typeof FontFace !== "undefined" ? new FontFace(ARCHIVO, `url(${staticFile("assets/fonts/copywriters/Archivo-Variable.ttf")})`).load().then((f) => (document as any).fonts.add(f)).catch(() => undefined) : Promise.resolve();

/** Cada línea entra por golpe (escala 1,5 → 1 con sobreimpulso, rotación −3° → 0, desenfoque 3 f), escalón de 3 f. */
const Golpe: React.FC<{lineas: {t: string; color?: string; size: number}[]; bottom: number; delay?: number}> = ({lineas, bottom, delay = 0}) => {
  const frame = useCurrentFrame() - delay; const {fps} = useVideoConfig();
  return (
    <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: bottom}}>
      <div style={{textAlign: "center", padding: "0 40px"}}>
        {lineas.map((l, i) => {
          const f = frame - i * 3;
          const e = spring({fps, frame: f, config: {damping: 9, stiffness: 320, mass: 0.6}});
          return (
            <div key={i} style={{opacity: f < 0 ? 0 : 1, transform: `scale(${interpolate(e, [0, 1], [1.5, 1])}) rotate(${interpolate(e, [0, 1], [-3, 0])}deg)`, filter: `blur(${interpolate(f, [0, 3], [12, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})}px)`, fontFamily: ARCHIVO, fontVariationSettings: '"wdth" 88, "wght" 900', fontSize: l.size, lineHeight: 0.92, letterSpacing: "-0.02em", color: l.color ?? BONE, textTransform: "uppercase"}}>{l.t}</div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/** SANTA GOTA × GRUPO COPYLAB, logos planos en blanco; la animación termina en ~0,4 s. */
const Marcas: React.FC = () => {
  const frame = useCurrentFrame(); const {fps} = useVideoConfig();
  const enter = spring({fps, frame, config: {damping: 11, stiffness: 240, mass: 0.7}});
  const CW = 520, CH = (CW * 889) / 1000;                 // caja del logo de Copylab (el trazo ocupa ~52 %)
  return (
    <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: 560, opacity: interpolate(enter, [0, 1], [0, 1]), transform: `translateY(${interpolate(enter, [0, 1], [40, 0])}px) scale(${interpolate(enter, [0, 1], [1.15, 1])})`}}>
      <div style={{display: "flex", alignItems: "center", gap: 30}}>
        <Img src={staticFile("assets/santagota/logo-plano-blanco.png")} style={{width: 380, objectFit: "contain"}} />
        <div style={{fontFamily: ARCHIVO, fontVariationSettings: '"wdth" 80, "wght" 300', fontSize: 84, color: BONE, opacity: 0.85}}>×</div>
        <Img src={staticFile("brand/copylab/copylab-white.png")} style={{width: CW, height: CH, margin: "0 -115px"}} />
      </div>
    </AbsoluteFill>
  );
};

export const BienvenidaSantaGota: React.FC = () => {
  void fontPromise;
  return (
    <AbsoluteFill style={{background: INK}}>
      <Sequence from={0} durationInFrames={REEL} layout="none">
        <Video src={staticFile("assets/santagota/bienvenida/monja-reel-07sept.mp4")} volume={0} style={{width: "100%", height: "100%", objectFit: "cover"}} />
      </Sequence>
      <Sequence from={REEL} durationInFrames={CORTE - REEL} layout="none">
        <Freeze frame={REEL - 1}>
          <Video src={staticFile("assets/santagota/bienvenida/monja-reel-07sept.mp4")} style={{width: "100%", height: "100%", objectFit: "cover"}} />
        </Freeze>
      </Sequence>
      <Sequence from={CORTE} layout="none">
        <AbsoluteFill style={{background: INK}} />
        <Golpe bottom={1000} lineas={[{t: "Bienvenidos,", size: 132}, {t: "Santa Gota.", size: 150, color: LIMA}]} />
        <Sequence from={TUM - CORTE} layout="none"><Marcas /></Sequence>
      </Sequence>
      <Audio src={staticFile("assets/santagota/bienvenida/musica-extendida.wav")} />
    </AbsoluteFill>
  );
};
