// ─────────────────────────────────────────────────────────────────────────────
// EBEMA · LinkedIn · Reel animado «Saludo sucursal Talca» — 05/10/2026
//
// DIRECCIÓN DE ARTE — calcada del reel publicado de La Calera (sept. 2026),
// `raw/ebema/linkedin/ref/reel/reel_calera_sept.mp4`, medido a 2160×3840:
//   · caja roja llena arriba-izquierda 0–1011 × 0–395 (radio ~100) + filete de 8 px
//     a 36/48 px de distancia (1048–1055 × 444–451); abajo-derecha espejo
//     (llena 1104–2160 × 3442–3840, filete 1060–1067 × 3386–3393). Fijas todo el video.
//   · logo en pastilla blanca 1432–1875 × 0–451 arriba-derecha.
//   · Raleway: título «SUCURSAL EBEMA» 600 a 137 px (alto de mayúscula 94); nombre
//     de la sucursal 700 a 161 px dentro de una caja roja redondeada de 1305 × 189.
//     Cuerpo 500 (Medium) a 104,5 px, interlínea 128, resaltado en caja roja de 105.
//     (Se comparó el GROSOR DE TRAZO contra 400/600/700: 9 px = Medium.)
//   · textos entran y salen con desenfoque + fundido (~0,4 s).
//   · pantalla partida en 1920: arriba entra desde la izquierda, abajo desde la derecha.
//   · cierre blanco: frase en caja roja + bajada gris #808080 + anillo EBEMA 661 px.
//
// TEXTOS: literales del brief (GRILLA OCTUBRE 2026 - EBEMA, LinkedIn 05/10).
// ⛔ Paulina 25-09: nadie mira a cámara (perfil o espaldas está bien). Imágenes:
// fotos REALES de la sucursal animadas con Kling (clips.sh) + el video real de la
// grúa (C0044, 0–2,3 s a media velocidad).
// ─────────────────────────────────────────────────────────────────────────────
import React from "react";
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame, Easing} from "remotion";

export const TALCA_FPS = 30;
const DIR = "assets/ebema/linkedin-oct26/talca";
const RED = "#EC1C23", GRIS = "#808080";

// timeline (frames a 30 fps)
const S1 = {from: 0, dur: 96};      // SUCURSAL EBEMA / TALCA
const S2 = {from: 96, dur: 102};    // T1
const S3 = {from: 198, dur: 108};   // T2 — partida oficinas / recepción
const S4 = {from: 306, dur: 117};   // T3 — partida grúa / nave
const CIERRE = {from: 423, dur: 120};
const SOLAPE = 16;   // cuadros que un fondo sigue vivo bajo la escena que entra
export const TALCA_DURATION = CIERRE.from + CIERRE.dur;   // 543 = 18,1 s

let fontsOk = false;
const ensureFonts = () => {
  if (fontsOk || typeof document === "undefined") return;
  fontsOk = true;
  const f = (w: number, file: string) =>
    `@font-face { font-family:'RalewayLK'; font-weight:${w}; font-display:block; src:url(${staticFile(`assets/ebema/fonts/${file}`)}) format('truetype'); }`;
  const st = document.createElement("style");
  st.textContent = [f(500, "Raleway-Medium.ttf"), f(600, "Raleway-SemiBold.ttf"), f(700, "Raleway-Bold.ttf")].join("\n");
  document.head.appendChild(st);
  const fs = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (fs) ["500", "600", "700"].forEach((w) => fs.load(`${w} 40px RalewayLK`));
};
const RALEWAY = "'RalewayLK', 'Raleway', Arial, sans-serif";

// entrada/salida con desenfoque, como La Calera
const useBlurInOut = (inAt: number, dur: number, inLen = 12, outLen = 10) => {
  const f = useCurrentFrame();
  const a = interpolate(f, [inAt, inAt + inLen], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  const b = interpolate(f, [dur - outLen, dur], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.in(Easing.cubic)});
  const v = Math.min(a, b);
  return {opacity: v, filter: `blur(${(1 - v) * 18}px)`};
};

const Fondo: React.FC<{src: string; video?: boolean; rate?: number; zoom?: [number, number]; origen?: string; velo?: boolean; dur: number}> =
({src, video = true, rate = 1, zoom = [1, 1], origen = "50% 50%", velo = false, dur}) => {
  const f = useCurrentFrame();
  const z = interpolate(f, [0, dur], zoom, {extrapolateRight: "clamp"});
  const st: React.CSSProperties = {width: "100%", height: "100%", objectFit: "cover", transform: `scale(${z})`, transformOrigin: origen};
  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      {video ? <OffthreadVideo src={staticFile(src)} muted playbackRate={rate} style={st} /> : <Img src={staticFile(src)} style={st} />}
      <AbsoluteFill style={{background: "rgba(0,0,0,.20)"}} />
      {velo && <AbsoluteFill style={{background: "linear-gradient(180deg, rgba(0,0,0,0) 45%, rgba(0,0,0,.42) 72%, rgba(0,0,0,.30) 100%)"}} />}
    </AbsoluteFill>
  );
};

// una línea del cuerpo, por tramos: [texto, rojo?]. La Calera resalta PALABRAS dentro
// de la línea («Un equipo [comprometido] con el»), no la línea entera.
type Tramo = [string, boolean?];
const Linea: React.FC<{tramos: Tramo[]}> = ({tramos}) => (
  <div style={{height: 128, display: "flex", justifyContent: "center", alignItems: "flex-start", whiteSpace: "pre"}}>
    {tramos.map(([t, rojo], i) => (
      <span key={i} style={{display: "inline-block", height: 105, lineHeight: "105px", padding: rojo ? "0 22px" : 0,
        background: rojo ? RED : "transparent", color: "#fff", fontFamily: RALEWAY, fontWeight: 500, fontSize: 104.5,
        textShadow: rojo ? "none" : "0 3px 18px rgba(0,0,0,.5)"}}>{t}</span>
    ))}
  </div>
);

const Bloque: React.FC<{top: number; dur: number; inAt?: number; lineas: Tramo[][]}> =
({top, dur, inAt = 8, lineas}) => {
  const s = useBlurInOut(inAt, dur);
  return (
    <div style={{position: "absolute", left: 0, right: 0, top, ...s}}>
      {lineas.map((l, i) => <Linea key={i} tramos={l} />)}
    </div>
  );
};

const Titulo: React.FC<{dur: number}> = ({dur}) => {
  const s = useBlurInOut(15, dur);
  return (
    <div style={{position: "absolute", left: 0, right: 0, top: 2392, textAlign: "center", ...s}}>
      <div style={{fontFamily: RALEWAY, fontWeight: 600, fontSize: 137, color: "#fff", lineHeight: "135px",
        textShadow: "0 3px 18px rgba(0,0,0,.45)"}}>SUCURSAL EBEMA</div>
      <div style={{margin: "7px auto 0", width: 1305, height: 189, borderRadius: 40, background: RED,
        fontFamily: RALEWAY, fontWeight: 700, fontSize: 161, lineHeight: "189px", color: "#fff"}}>TALCA</div>
    </div>
  );
};

// pantalla partida: arriba entra desde la izquierda, abajo desde la derecha
const Partida: React.FC<{arriba: React.ReactNode; abajo: React.ReactNode}> = ({arriba, abajo}) => {
  const f = useCurrentFrame();
  const e = {extrapolateLeft: "clamp" as const, extrapolateRight: "clamp" as const, easing: Easing.out(Easing.cubic)};
  const xa = interpolate(f, [0, 10], [-2160, 0], e);
  const xb = interpolate(f, [2, 12], [2160, 0], e);
  return (
    <>
      <div style={{position: "absolute", left: 0, top: 0, width: 2160, height: 1920, overflow: "hidden", transform: `translateX(${xa}px)`}}>{arriba}</div>
      <div style={{position: "absolute", left: 0, top: 1920, width: 2160, height: 1920, overflow: "hidden", transform: `translateX(${xb}px)`}}>{abajo}</div>
    </>
  );
};

// cajas rojas de esquina + filete; en el cierre vuelven a entrar
const Esquinas: React.FC = () => {
  const f = useCurrentFrame();
  const e = {extrapolateLeft: "clamp" as const, extrapolateRight: "clamp" as const, easing: Easing.out(Easing.cubic)};
  const re = interpolate(f, [CIERRE.from, CIERRE.from + 4, CIERRE.from + 16], [0, 1, 0], e);
  const dx = re * -700, dy = re * -260;
  const caja: React.CSSProperties = {position: "absolute", background: RED, borderRadius: 100};
  const filete: React.CSSProperties = {position: "absolute", border: `8px solid ${RED}`, borderRadius: 140, boxSizing: "border-box"};
  return (
    <>
      <div style={{...filete, left: -400, top: -400, width: 1456, height: 852, transform: `translate(${dx}px,${dy}px)`}} />
      <div style={{...caja, left: -400, top: -400, width: 1411, height: 795, transform: `translate(${dx}px,${dy}px)`}} />
      <div style={{...filete, left: 1060, top: 3386, width: 1500, height: 900, transform: `translate(${-dx}px,${-dy}px)`}} />
      <div style={{...caja, left: 1104, top: 3442, width: 1456, height: 798, transform: `translate(${-dx}px,${-dy}px)`}} />
    </>
  );
};

const Pastilla: React.FC = () => {
  const f = useCurrentFrame();
  const o = interpolate(f, [CIERRE.from, CIERRE.from + 6], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <div style={{position: "absolute", left: 1432, top: -60, width: 443, height: 511, background: "#fff",
      borderRadius: 48, opacity: o, display: "flex", alignItems: "flex-end", justifyContent: "center", paddingBottom: 72}}>
      <Img src={staticFile("assets/ebema/linkedin-oct26/logo_ebema_color.png")} style={{width: 300}} />
    </div>
  );
};

const Cierre: React.FC = () => {
  const f = useCurrentFrame();
  const e = {extrapolateLeft: "clamp" as const, extrapolateRight: "clamp" as const, easing: Easing.out(Easing.cubic)};
  const y = interpolate(f, [0, 8], [-3840, 0], e);
  const anillo = interpolate(f, [4, 16], [0, 1], e);
  const t1 = useBlurInOut(18, 9999, 12);
  const t2 = useBlurInOut(30, 9999, 12);
  return (
    <AbsoluteFill style={{background: "#fff", transform: `translateY(${y}px)`}}>
      <div style={{position: "absolute", left: 0, right: 0, top: 1154, textAlign: "center", ...t1}}>
        <span style={{display: "inline-block", height: 131, lineHeight: "131px", padding: "0 100px", background: RED,
          color: "#fff", fontFamily: RALEWAY, fontWeight: 500, fontSize: 101, whiteSpace: "nowrap"}}>El equipo de Talca,</span>
      </div>
      <div style={{position: "absolute", left: 0, right: 0, top: 1316, textAlign: "center", color: GRIS,
        fontFamily: RALEWAY, fontWeight: 500, fontSize: 101, lineHeight: "128px", whiteSpace: "nowrap", ...t2}}>
        resolviendo el día a día de la zona.
      </div>
      <Img src={staticFile("assets/ebema/linkedin-oct26/logo_ebema_color.png")}
        style={{position: "absolute", left: 760, top: 1788, width: 661, opacity: anillo,
          transform: `scale(${interpolate(anillo, [0, 1], [0.85, 1])})`}} />
    </AbsoluteFill>
  );
};

export const EbemaLinkedinReelTalca: React.FC = () => {
  ensureFonts();
  return (
    <AbsoluteFill style={{background: "#000"}}>
      {/* FONDOS: cada uno sigue SOLAPE cuadros bajo la escena que entra (la partida y el
          barrido blanco entran POR ENCIMA del plano anterior, como en La Calera; si no, se
          ve negro — pasó en el 1er render, 25-09). Los textos van aparte, con su duración. */}
      <Sequence from={S1.from} durationInFrames={S1.dur + SOLAPE}>
        {/* IMG_6995 frontal: el título cae en el suelo (con la lateral caía sobre la pared blanca).
            El hormigón es claro → velo hacia abajo para que el blanco se lea. */}
        <Fondo src={`${DIR}/clips/s1_30.mp4`} dur={S1.dur} zoom={[1, 1.03]} velo />
      </Sequence>
      <Sequence from={S2.from} durationInFrames={S2.dur + SOLAPE}>
        {/* r1 25-09: la bodega exterior no pasó («deficiente en iluminación y enfoque comercial»);
            ahora la nave interior (Bodega Central 6), piso claro → velo */}
        <Fondo src={`${DIR}/clips/s2_30.mp4`} dur={S2.dur} zoom={[1, 1.03]} velo />
      </Sequence>
      <Sequence from={S3.from} durationInFrames={S3.dur + SOLAPE}>
        <Partida arriba={<Fondo src={`${DIR}/clips/s3a_30.mp4`} dur={S3.dur} />}
                 abajo={<Fondo src={`${DIR}/clips/s3b_30.mp4`} dur={S3.dur} />} />
      </Sequence>
      <Sequence from={S4.from} durationInFrames={S4.dur + SOLAPE}>
        <Partida arriba={<Fondo src={`${DIR}/clips/s4a_grua_real.mp4`} dur={S4.dur} />}
                 abajo={<Fondo src={`${DIR}/clips/s4b_30.mp4`} dur={S4.dur} />} />
      </Sequence>
      {/* TEXTOS */}
      <Sequence from={S1.from} durationInFrames={S1.dur}><Titulo dur={S1.dur} /></Sequence>
      <Sequence from={S2.from} durationInFrames={S2.dur}>
        <Bloque top={2350} dur={S2.dur} lineas={[
          [["Impulsando la construcción", true]], [["de la zona desde nuestra"]], [["sucursal Talca.", true]]]} />
      </Sequence>
      <Sequence from={S3.from} durationInFrames={S3.dur}>
        <Bloque top={1790} dur={S3.dur} inAt={12} lineas={[
          [["Un equipo "], ["comprometido", true], [" con el"]], [["abastecimiento de la región.", true]]]} />
      </Sequence>
      <Sequence from={S4.from} durationInFrames={S4.dur}>
        <Bloque top={1790} dur={S4.dur} inAt={12} lineas={[
          [["Logística eficiente", true], [" para los"]], [["desafíos constructivos", true], [" de la zona."]]]} />
      </Sequence>
      <Sequence from={CIERRE.from} durationInFrames={CIERRE.dur}>
        <Cierre />
      </Sequence>
      <Pastilla />
      <Esquinas />
      <Audio src={staticFile(`${DIR}/musica.mp3`)}
        volume={(f) => interpolate(f, [0, 15, TALCA_DURATION - 30, TALCA_DURATION], [0, 0.8, 0.8, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})} />
    </AbsoluteFill>
  );
};
