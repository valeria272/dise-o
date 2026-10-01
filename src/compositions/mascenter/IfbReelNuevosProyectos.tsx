/**
 * GRUPO IFB · MÁS CENTER — reel de LinkedIn del 23-10-2026 «Nuevos proyectos Más Center».
 *
 * Brief: GRILLA DE CONTENIDOS IFB - OCTUBRE 2026.xlsx › GRILLA LINKEDIN › I8 (la fecha de la celda se lee
 * «23-03» por un error de formato del Excel; es el 23-10). Textos VERBATIM del brief (cortes 1–4 + cierre).
 *
 * REF (hipervínculo de I8, pin 2814818512168314 → raw/mascenter/octubre-2026/refs-linkedin/reel-23-10/ref.mp4):
 * reel inmobiliario de 15 s. Cielo con nubes de fondo, el edificio recortado SUBE desde abajo, el nombre
 * fijo arriba, y tarjetas con foto + etiquetas blancas que entran y salen GIRANDO en 3D como un carrusel.
 * Cierre: el texto aparece en el cielo y un botón.
 *
 * Adaptación IFB: el nombre fijo es el lockup Grupo IFB | Más Center; el edificio es un strip center
 * (Seedream sobre el render web de Buin, cielo recortado por color); cada tarjeta es un render de un
 * proyecto distinto (Chicureo, Linderos, 4 Esquinas, Algarrobal) con el texto del corte en etiquetas;
 * el «botón» del cierre es la pastilla celeste con «2026 – 2028». Paleta IFB: navy #112C3A, celeste #BAEAEE.
 * Etiquetas medidas sobre su texto con aire generoso (R-65: nunca texto al límite del contenedor).
 */
import React from "react";
import {AbsoluteFill, Audio, Easing, Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";

const NAVY = "#112C3A";
const CELESTE = "#BAEAEE";
const A = (f: string) => staticFile(`assets/mascenter/reel-23-10/${f}`);

let fontsInjected = false;
const FUENTES: [string, number, string][] = [
  ["Gotham Black", 900, "assets/fonts/mascenter/Gotham-Black.ttf"],
  ["GothamRnd", 700, "assets/fonts/mascenter/GothamRnd-Bold.ttf"],
  ["GothamRnd", 400, "assets/fonts/mascenter/GothamRnd-Book.ttf"],
];
const ensureFonts = () => {
  if (fontsInjected || typeof document === "undefined") return;
  fontsInjected = true;
  const style = document.createElement("style");
  style.textContent = FUENTES.map(([f, w, src]) => `@font-face{font-family:'${f}';font-weight:${w};font-display:block;src:url(${staticFile(src)}) format('truetype')}`).join("");
  document.head.appendChild(style);
  const fs = (document as any).fonts;
  if (fs?.load) FUENTES.forEach(([f, w]) => fs.load(`${w} 100px '${f}'`).catch(() => undefined));
};
ensureFonts();

const suave = Easing.out(Easing.cubic);
const entra = Easing.bezier(0.16, 1, 0.3, 1);
const cl = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

// ── guion (frames a 30 fps) ────────────────────────────────────────────────
type Tarjeta = {img: string; lineas: string[]; desde: number; hasta: number};
const TARJETAS: Tarjeta[] = [
  {img: "t1-chicureo.jpg", lineas: ["SEGUIMOS CRECIENDO."], desde: 40, hasta: 118},
  {img: "t2-linderos.jpg", lineas: ["NUEVOS PROYECTOS."], desde: 112, hasta: 190},
  {img: "t3-4esquinas.jpg", lineas: ["NUEVOS PUNTOS."], desde: 184, hasta: 262},
  {img: "t4-algarrobal.jpg", lineas: ["NUEVAS OPORTUNIDADES", "PARA CRECER JUNTO A LAS COMUNIDADES."], desde: 256, hasta: 368},
];
const CIERRE = 360;
export const IFB_REEL_FRAMES = 480;

const GIRO_IN = 18;
const GIRO_OUT = 14;
const CARD_W = 640;
const CARD_H = 496;
const CARD_TOP = 600;

const Etiqueta: React.FC<{texto: string; size: number; delay: number; t: number}> = ({texto, size, delay, t}) => {
  const p = interpolate(t, [delay, delay + 12], [0, 1], {...cl, easing: suave});
  return (
    <div style={{
      display: "inline-block", background: "#fff", color: NAVY, borderRadius: size * 0.55,
      padding: `${size * 0.42}px ${size * 0.9}px ${size * 0.36}px`, fontFamily: "GothamRnd", fontWeight: 700,
      fontSize: size, lineHeight: 1, letterSpacing: "0.01em", whiteSpace: "nowrap",
      opacity: p, transform: `translateX(${(1 - p) * -40}px)`,
    }}>{texto}</div>
  );
};

const TarjetaGiro: React.FC<{t: Tarjeta; frame: number}> = ({t, frame}) => {
  if (frame < t.desde || frame > t.hasta) return null;
  const local = frame - t.desde;
  const dur = t.hasta - t.desde;
  const pin = interpolate(local, [0, GIRO_IN], [0, 1], {...cl, easing: entra});
  const pout = interpolate(local, [dur - GIRO_OUT, dur], [0, 1], {...cl, easing: Easing.in(Easing.cubic)});
  // entra desde la derecha girando sobre Y y sale por la izquierda girando al otro lado (carrusel 3D de la REF)
  const rot = (1 - pin) * 70 - pout * 70;
  const tx = (1 - pin) * 420 - pout * 420;
  const op = Math.min(pin * 1.6, 1) * (1 - pout);
  const size = t.lineas.length > 1 ? 33 : 42;
  return (
    <div style={{position: "absolute", left: 0, top: 0, width: 1080, height: 1920, perspective: 1500}}>
      <div style={{
        position: "absolute", left: (1080 - CARD_W) / 2, top: CARD_TOP, width: CARD_W, height: CARD_H,
        transform: `translateX(${tx}px) rotateY(${rot}deg)`, transformOrigin: "50% 50%", opacity: op,
      }}>
        <div style={{position: "absolute", inset: 0, borderRadius: 30, overflow: "hidden", border: "6px solid rgba(255,255,255,.92)",
          boxShadow: "0 24px 60px rgba(8,30,50,.28)"}}>
          <Img src={A(t.img)} style={{width: "100%", height: "100%", objectFit: "cover",
            transform: `scale(${interpolate(local, [0, dur], [1.08, 1.0])})`}} />
        </div>
        <div style={{position: "absolute", left: -44, top: 38, display: "flex", flexDirection: "column", alignItems: "flex-start", gap: 12}}>
          {t.lineas.map((l, i) => <Etiqueta key={i} texto={l} size={size} delay={GIRO_IN - 4 + i * 6} t={local} />)}
        </div>
      </div>
    </div>
  );
};

export const IfbReelNuevosProyectos: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const cieloZoom = interpolate(frame, [0, IFB_REEL_FRAMES], [1.1, 1.0]);
  const cieloY = interpolate(frame, [0, IFB_REEL_FRAMES], [30, -30]);
  const sube = interpolate(frame, [4, 46], [1, 0], {...cl, easing: entra});
  const lockOp = interpolate(frame, [0, 16], [0, 1], cl);

  const fin = frame - CIERRE;
  const s1 = spring({fps, frame: fin, config: {damping: 200}});
  const s2 = spring({fps, frame: fin - 8, config: {damping: 200}});
  const sPas = spring({fps, frame: fin - 22, config: {damping: 14, stiffness: 140}});
  const velo = interpolate(frame, [CIERRE - 10, CIERRE + 10], [0, 1], cl);
  const salida = interpolate(frame, [IFB_REEL_FRAMES - 12, IFB_REEL_FRAMES - 1], [1, 0], cl);

  return (
    <AbsoluteFill style={{background: "#2b6fa3", overflow: "hidden"}}>
      {/* pista generada con Magnific (ElevenLabs Music v2, instrumental corporativa ~110 BPM, 18 s); fundido de salida */}
      <Audio src={A("musica.mp3")} volume={(f) => interpolate(f, [0, 6, IFB_REEL_FRAMES - 30, IFB_REEL_FRAMES - 1], [0, 0.85, 0.85, 0], cl)} />
      <Img src={A("cielo.jpg")} style={{position: "absolute", width: 1080, height: 1920,
        transform: `translateY(${cieloY}px) scale(${cieloZoom})`}} />
      {/* velo navy suave en el cielo alto para que el texto blanco del cierre se lea sobre las nubes */}
      <AbsoluteFill style={{background: "linear-gradient(180deg, rgba(17,44,58,.55) 0%, rgba(17,44,58,.35) 38%, rgba(17,44,58,0) 60%)", opacity: 0.3 + velo * 0.7}} />

      <Img src={A("heroe.png")} style={{position: "absolute", left: 0, top: 1920 - 1944 + 40, width: 1080,
        transform: `translateY(${sube * 1000}px) scale(${1 + sube * 0.06})`, transformOrigin: "50% 100%"}} />

      <Img src={A("lockup.png")} style={{position: "absolute", left: (1080 - 470) / 2, top: 190, width: 470, opacity: lockOp}} />

      {TARJETAS.map((t, i) => <TarjetaGiro key={i} t={t} frame={frame} />)}

      {fin >= 0 && (
        <div style={{position: "absolute", left: 0, top: 430, width: 1080, textAlign: "center", color: "#fff", opacity: salida}}>
          <div style={{fontFamily: "Gotham Black", fontWeight: 900, fontSize: 86, lineHeight: "92px", textTransform: "uppercase",
            opacity: s1, transform: `translateY(${(1 - s1) * 40}px)`}}>7 nuevos<br />desarrollos</div>
          <div style={{fontFamily: "Gotham Black", fontWeight: 900, fontSize: 86, lineHeight: "92px", textTransform: "uppercase",
            opacity: s2, transform: `translateY(${(1 - s2) * 40}px)`}}>Más Center.</div>
          <div style={{display: "inline-block", marginTop: 44, background: CELESTE, color: NAVY, borderRadius: 40,
            padding: "22px 56px 18px", fontFamily: "GothamRnd", fontWeight: 700, fontSize: 52, lineHeight: 1,
            opacity: Math.min(sPas * 1.4, 1), transform: `scale(${0.8 + sPas * 0.2})`}}>2026 – 2028</div>
        </div>
      )}
    </AbsoluteFill>
  );
};
