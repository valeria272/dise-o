/**
 * MÁS CENTER — story animada «La fórmula para un Halloween de miedo» (KiosClub), grilla IFB octubre 2026,
 * pestaña GRILLA STORIES, celda B8. 1080×1920 · 30 fps · 12 s.
 *
 * Tres cortes del brief (los rótulos «CORTE N» no van, R-51):
 *   1 · caldero vacío + humo → «¿QUÉ NECESITA UN HALLOWEEN DULCE?»
 *   2 · dulces cayendo en tres tandas → «UN POCO DE ESTO…» / «OTRO POCO DE ESTO…» / «Y DE ESTO TAMBIÉN.»
 *   3 · explosión de humo + reveal del caldero lleno → «HALLOWEEN YA SE ACERCA.» + bajada + 📍 KiosClub San Carlos
 * Fondos y dulces: Seedream 5 Pro (caldero sobre lila como la REF del brief; dulces genéricos sin marcas, recortados
 * por croma). Tipografía del reel de la marca (R-45): titular GothamRounded Bold en versales, pastilla roja GothamRnd
 * Book. Montaje del estudio (R-12): textos palabra a palabra con fundido y 26 px, sin golpes de rojo.
 * El botón 🍬 de la interacción lo pone la CM en Instagram: se deja libre la franja 1500–1650.
 * Sin pista: la de la marca está en FUENTES ESTUDIO y no está en esta máquina (se agrega al publicar o en otra ronda).
 */
import React from "react";
import {AbsoluteFill, Easing, Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";

const ROJO = "#DC1914";
// Diego 30-09: «el fondo cámbialo por fondo naranjo, el texto no se lee bien, prueba dejándolo con un tono más oscuro del
// manual de marca» → fondo naranjo y textos en el rojo oscuro del manual Grupo IFB 2023 (marca.json › rojo_oscuro_manual).
const OSCURO = "#65140F";
const K = "assets/mascenter/kiosclub/";
const FUENTES: [string, number, string][] = [
  ["GothamRounded", 700, "assets/fonts/mascenter/GothamRounded-Bold.ttf"],
  ["GothamRnd", 400, "assets/fonts/mascenter/GothamRnd-Book.ttf"],
  ["GothamRnd", 500, "assets/fonts/mascenter/GothamRnd-Medium.ttf"],
];
let fuentesListas = false;
const cargarFuentes = () => {
  if (fuentesListas || typeof document === "undefined") return;
  fuentesListas = true;
  const s = document.createElement("style");
  s.textContent = FUENTES.map(([f, w, src]) => `@font-face{font-family:'${f}';font-weight:${w};font-display:block;src:url(${staticFile(src)}) format('truetype')}`).join("");
  document.head.appendChild(s);
};

export const KIOSCLUB_FRAMES = 360;
const BOCA_Y = 1040;           // borde del caldero en el fondo 1080×1920 (medido: y 1052 en 1944 − 12 de recorte)
const TANDAS = [                // [inicio, dulces]; los índices salen de la hoja recortada (sin los cortados ni el de texto falso)
  [96, [2, 4, 8, 14, 26, 33]],
  [141, [7, 9, 17, 20, 29, 36]],
  [186, [5, 12, 16, 21, 30, 34, 35, 41]],
] as const;

const PIN = (
  <svg viewBox="0 0 40 40" style={{width: 36, height: 36, marginTop: -6}}>
    <path d="M9 33 L19 21" stroke="#e8e8e8" strokeWidth={3.2} strokeLinecap="round" />
    <circle cx={24} cy={15} r={10.5} fill="#EC4C5C" stroke="#fff" strokeWidth={1.6} />
    <circle cx={20.5} cy={11.5} r={3.4} fill="#ffc2c8" />
  </svg>
);

// Texto que entra palabra a palabra con fundido y 26 px (R-12) y sale con fundido.
const Palabras: React.FC<{texto: string; desde: number; hasta: number; style: React.CSSProperties}> = ({texto, desde, hasta, style}) => {
  const f = useCurrentFrame();
  const sale = interpolate(f, [hasta - 8, hasta], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  if (f < desde || f > hasta) return null;
  const lineas = texto.split("\n");
  let n = 0;
  return (
    <div style={{...style, opacity: sale}}>
      {lineas.map((l, i) => (
        <div key={i} style={{whiteSpace: "nowrap"}}>
          {l.split(" ").map((p, j) => {
            const t0 = desde + n++ * 3;
            const e = interpolate(f, [t0, t0 + 12], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
            return <span key={j} style={{display: "inline-block", opacity: e, transform: `translateY(${(1 - e) * 26}px)`, marginRight: "0.28em"}}>{p}</span>;
          })}
        </div>
      ))}
    </div>
  );
};

// Un dulce que cae con gravedad hasta la boca del caldero, gira y se hunde (escala y fundido) con un puff.
const Dulce: React.FC<{i: number; t0: number; x: number; tam: number; giro: number}> = ({i, t0, x, tam, giro}) => {
  const f = useCurrentFrame();
  const t = f - t0;
  if (t < 0 || t > 30) return null;
  const caida = 22;
  const p = Math.min(t / caida, 1);
  const y = -200 + (BOCA_Y + 40 + 200) * p * p;
  const hunde = interpolate(t, [caida - 4, caida + 4], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const puff = interpolate(t, [caida - 2, caida + 8], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <>
      <Img src={staticFile(`${K}dulce-${String(i).padStart(2, "0")}.png`)}
        style={{position: "absolute", left: x - tam / 2, top: y - tam / 2, width: tam, transform: `rotate(${giro * p}deg) scale(${0.4 + 0.6 * hunde})`, opacity: hunde, filter: "drop-shadow(0 10px 14px rgba(40,0,60,.35))"}} />
      {puff > 0 && puff < 1 && (
        <div style={{position: "absolute", left: x - 90, top: BOCA_Y - 70, width: 180, height: 120, borderRadius: "50%",
          background: "radial-gradient(closest-side, rgba(235,255,240,.75), rgba(235,255,240,0))", opacity: 1 - puff, transform: `scale(${0.6 + puff})`}} />
      )}
    </>
  );
};

export const KiosclubStoryHalloween: React.FC = () => {
  cargarFuentes();
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const zoom = interpolate(f, [0, 240], [1, 1.05], {extrapolateRight: "clamp"});
  const reveal = interpolate(f, [228, 244], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const flash = interpolate(f, [222, 232, 252], [0, 1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const zoomFinal = interpolate(f, [228, 360], [1.06, 1.0], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.quad)});
  const humo = (f % 90) / 90;
  const titulo: React.CSSProperties = {position: "absolute", left: 40, right: 40, top: 320, textAlign: "center", color: OSCURO, fontFamily: "GothamRounded",
    fontWeight: 700, fontSize: 74, lineHeight: "84px", textTransform: "uppercase"};
  const pastilla = spring({fps, frame: f - 262, config: {damping: 200}});
  return (
    <AbsoluteFill style={{background: "#f19a5e", overflow: "hidden"}}>
      <Img src={staticFile(`${K}B-caldero-vacio-naranjo.jpg`)} style={{position: "absolute", width: 1080, height: 1920, transform: `scale(${zoom})`, transformOrigin: "50% 60%"}} />
      {/* humo que sube del caldero vacío */}
      {[0, 0.33, 0.66].map((d, i) => {
        const q = (humo + d) % 1;
        return <div key={i} style={{position: "absolute", left: 300 + i * 110, top: BOCA_Y - 120 - q * 420, width: 320, height: 260, borderRadius: "50%",
          background: "radial-gradient(closest-side, rgba(230,255,235,.45), rgba(230,255,235,0))", opacity: (1 - q) * (1 - reveal), transform: `scale(${0.7 + q * 0.8})`}} />;
      })}
      {TANDAS.map(([t0, idx]) => idx.map((i, j) => (
        <Dulce key={`${t0}-${i}`} i={i} t0={t0 + j * 5} x={360 + ((j * 137) % 360)} tam={170 + ((j * 53) % 60)} giro={(j % 2 ? 1 : -1) * (90 + j * 30)} />
      )))}
      {/* reveal: caldero lleno */}
      <Img src={staticFile(`${K}B-caldero-lleno-naranjo.jpg`)} style={{position: "absolute", width: 1080, height: 1920, opacity: reveal, transform: `scale(${zoomFinal})`, transformOrigin: "50% 62%"}} />
      <AbsoluteFill style={{background: "radial-gradient(circle at 50% 58%, rgba(255,255,255,.95), rgba(255,235,215,.6) 45%, rgba(255,255,255,0) 75%)", opacity: flash}} />
      <Img src={staticFile("assets/mascenter/logo-blanco.svg")} style={{position: "absolute", left: 437, top: 117, width: 206, filter: "drop-shadow(0 2px 10px rgba(101,20,15,.35))"}} />

      <Palabras texto={"¿Qué necesita\nun Halloween dulce?"} desde={-40} hasta={92} style={titulo} />
      <Palabras texto={"Un poco de esto…"} desde={96} hasta={140} style={titulo} />
      <Palabras texto={"Otro poco de esto…"} desde={141} hasta={185} style={titulo} />
      <Palabras texto={"Y de esto también."} desde={186} hasta={226} style={titulo} />
      <Palabras texto={"Halloween\nya se acerca."} desde={244} hasta={362} style={{...titulo, top: 250}} />

      {f >= 258 && (
        <div style={{position: "absolute", left: 0, right: 0, top: 432, display: "flex", flexDirection: "column", alignItems: "center", gap: 12,
          opacity: pastilla, transform: `translateY(${(1 - pastilla) * 26}px)`}}>
          <div style={{background: ROJO, color: "#fff", borderRadius: 34, padding: "12px 36px 16px", fontFamily: "GothamRnd", fontWeight: 400, fontSize: 40, lineHeight: "48px", textAlign: "center"}}>
            Encuentra tus dulces favoritos<br />en KiosClub.
          </div>
          <div style={{display: "flex", alignItems: "center", gap: 6, color: OSCURO, fontFamily: "GothamRnd", fontWeight: 500, fontSize: 32, lineHeight: "38px"}}>
            {PIN}<span>Más Center San Carlos de Apoquindo</span>
          </div>
          <div style={{color: OSCURO, fontFamily: "GothamRnd", fontWeight: 400, fontSize: 30, lineHeight: "36px", marginTop: -12}}>
            Av. Plaza 1.250, Las Condes.
          </div>
          <div style={{marginTop: 2, background: "#1c1c1c", borderRadius: 16, padding: "10px 22px"}}>
            <Img src={staticFile(`${K}logo-kiosclub.png`)} style={{width: 210, display: "block"}} />
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};
