import React from "react";
import {AbsoluteFill, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";

// =============================================================================
// EBEMA · GRILLA · STORY ANIMADA de Ebema Click — 07/10/2026
// 1080×1920 · 30 fps · 558 frames = 18,6 s
//
// Brief (grilla de octubre, bloque 02 · INSTAGRAM / STORIES), verbatim:
//   STORY ANIMADA · Sticker de enlace
//   (Dejar espacio para el sticker desde el inicio, sin tapar la gráfica.)
//   T1: ¿Cuánto tiempo pierdes abasteciéndote?
//   T2: Con Ebema Click compras online, 24/7 y sin filas.
//   T3: Para ferreteros y contratistas de Santiago, Rancagua, Chillán, Concepción,
//       Temuco y Puerto Montt.
//   T4: Y cada mes sorteamos una gift card entre quienes compran.
//   T5: Toca el enlace.
//
// ⭐ LA REFERENCIA QUE MANDA: `storie_click.mp4` de la grilla de JULIO 2026 (Paulina,
// raw/ebema/1-referencias/grilla/video/stories/). Es el mismo guion, texto por texto,
// y dura 18,65 s. Todo lo de abajo está MEDIDO sobre sus fotogramas (2160×3840 → /2):
//   · arcos rojos: anillo centrado en la esquina sup. derecha (r 165–365) y en la
//     inf. izquierda (r 165–410)
//   · lockup Click blanco: tinta x 272,5–806,5 · y 369–479
//   · textos en Raleway REGULAR (no bold): 1 línea blanca + 1 línea en caja roja,
//     cuerpo ≈ 48, bloque entre y 1150 y 1420
//   · T3: las ciudades entran UNA POR UNA, cada una en su cajita roja
//   · cierre en BLANCO: bloques rojos redondeados en las esquinas con filete,
//     anillo EBEMA 404 × 415 en (344, 586), caja «Toca el enlace» 521 × 71 en y 1261
//
// Lo que NO se copia de julio: el cierre decía además «Entra a Ebema Click / y haz
// crecer tu negocio hoy mismo». Octubre no lo trae: sólo T5 «Toca el enlace».
//
// Espacio del sticker: se deja libre la franja y 1450–1600 en todas las escenas (T3
// sube su bloque para no entrar ahí). No se dibuja nada: Paulina pidió el 24-09
// «eliminemos esta caja indicadora de todas las stories».
// =============================================================================
const RED = "#EC1C23", WHITE = "#FFFFFF";
export const STORY_OCT_FPS = 30;

const DIR = "assets/ebema/grilla-oct26/story-animada";
// timeline (frames)
const ESC = [
  {clip: "s1.mp4", from: 0, dur: 108},     // T1 · 3,6 s
  {clip: "s2.mp4", from: 108, dur: 108},   // T2 · 3,6 s
  {clip: "s3.mp4", from: 216, dur: 156},   // T3 · 5,2 s — seis ciudades
  // s4: la frente quedaba bajo el lockup. Se amplía 1,22 desde ARRIBA, lo que baja
  // la cabeza ~70 px sin dejar bordes (se pierde algo del mesón, que no importa).
  {clip: "s4.mp4", from: 372, dur: 96, escala: 1.22},    // T4 · 3,2 s
];
const CIERRE = {from: 468, dur: 90};         // T5 · 3,0 s
export const STORY_OCT_DURATION = CIERRE.from + CIERRE.dur;   // 558

let fontsOk = false;
const ensureFonts = () => {
  if (fontsOk || typeof document === "undefined") return;
  fontsOk = true;
  const f = (w: number, file: string) =>
    `@font-face { font-family:'RalewayEB'; font-weight:${w}; font-display:block; src:url(${staticFile(`assets/ebema/fonts/${file}`)}) format('truetype'); }`;
  const css = [f(400, "Raleway-Regular.ttf"), f(600, "Raleway-SemiBold.ttf"), f(700, "Raleway-Bold.ttf"),
    `@font-face { font-family:'HelvEB'; font-weight:700; font-display:block; src:url(${staticFile("assets/ebema/fonts/Helvetica-Bold.ttf")}) format('truetype'); }`].join("\n");
  const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  const fs = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (fs) ["400", "600", "700"].forEach((w) => fs.load(`${w} 40px RalewayEB`));
};
const RALEWAY = "'RalewayEB', 'Raleway', Arial, sans-serif";
const HELV = "'HelvEB', Helvetica, Arial, sans-serif";

// toda cifra en Helvetica Bold (§3 del manual)
const Num: React.FC<{t: string}> = ({t}) => (
  <>{t.split(/(\d[\d:/]*)/).map((p, i) => (/\d/.test(p) ? <span key={i} style={{fontFamily: HELV}}>{p}</span> : p))}</>
);

const useSpring = (delay: number) => {
  const frame = useCurrentFrame(); const {fps} = useVideoConfig();
  return spring({fps, frame: frame - delay, config: {damping: 16, stiffness: 150}});
};

// salida común de cada bloque de texto: 8 frames antes de cortar
const useSalida = (dur: number) => {
  const frame = useCurrentFrame();
  return interpolate(frame, [dur - 10, dur - 2], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
};

const Linea: React.FC<{delay: number; children: React.ReactNode; size?: number; caps?: boolean; weight?: number}> =
({delay, children, size = 48, caps = true, weight = 400}) => {
  const p = useSpring(delay);
  return (
    <div style={{opacity: p, transform: `translateY(${interpolate(p, [0, 1], [26, 0])}px)`,
      color: WHITE, fontFamily: RALEWAY, fontWeight: weight, fontSize: size, lineHeight: 1.16,
      textTransform: caps ? "uppercase" : "none", whiteSpace: "nowrap", textShadow: "0 2px 14px rgba(0,0,0,.35)"}}>
      {children}
    </div>
  );
};

// la caja roja entra BARRIENDO de izquierda a derecha y el texto aparece encima
const Caja: React.FC<{delay: number; children: React.ReactNode; size?: number; caps?: boolean; ancho?: number; alto?: number}> =
({delay, children, size = 48, caps = true, ancho, alto = 60}) => {
  const p = useSpring(delay);
  const t = useSpring(delay + 5);
  return (
    <div style={{position: "relative", display: "inline-block", height: alto, width: ancho,
      margin: "6px 0", padding: ancho ? 0 : "0 18px"}}>
      <div style={{position: "absolute", inset: 0, background: RED, transformOrigin: "left center",
        transform: `scaleX(${p})`}} />
      <div style={{position: "relative", opacity: t, color: WHITE, fontFamily: RALEWAY, fontWeight: 400,
        fontSize: size, lineHeight: `${alto}px`, textTransform: caps ? "uppercase" : "none",
        whiteSpace: "nowrap", textAlign: "center"}}>{children}</div>
    </div>
  );
};

const Bloque: React.FC<{top: number; dur: number; children: React.ReactNode}> = ({top, dur, children}) => {
  const o = useSalida(dur);
  return (
    <div style={{position: "absolute", left: 0, right: 0, top, display: "flex", flexDirection: "column",
      alignItems: "center", textAlign: "center", opacity: o}}>{children}</div>
  );
};

// los arcos rojos de las esquinas — anillos centrados en la esquina
const Arcos: React.FC = () => {
  const p = useSpring(0);
  // el de abajo se dibuja con centro (0,1920): se refleja en x
  return (
    <svg width={1080} height={1920} style={{position: "absolute", inset: 0}}>
      <g style={{transform: `translate(${interpolate(p, [0, 1], [120, 0])}px, ${interpolate(p, [0, 1], [-120, 0])}px)`}}>
        <path d="M 715 0 A 365 365 0 0 0 1080 365 L 1080 165 A 165 165 0 0 1 915 0 Z" fill={RED} />
      </g>
      <g style={{transform: `translate(${interpolate(p, [0, 1], [-120, 0])}px, ${interpolate(p, [0, 1], [120, 0])}px)`}}>
        <path d={`M 0 ${1920 - 410} A 410 410 0 0 1 410 1920 L 165 1920 A 165 165 0 0 0 0 ${1920 - 165} Z`} fill={RED} />
      </g>
    </svg>
  );
};

const Clip: React.FC<{src: string; dur: number; escala?: number}> = ({src, dur, escala = 1}) => {
  const frame = useCurrentFrame();
  const entra = interpolate(frame, [0, 8], [0, 1], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{opacity: entra}}>
      <OffthreadVideo src={staticFile(`${DIR}/${src}`)} muted playbackRate={src === "s3.mp4" ? 0.95 : 1}
        style={{width: "100%", height: "100%", objectFit: "cover", transform: `scale(${escala})`,
          transformOrigin: "center top"}} />
      {/* velo: parejo y más cargado abajo, donde van el texto y el sticker */}
      <AbsoluteFill style={{background: "linear-gradient(to bottom, rgba(0,0,0,.22) 0%, rgba(0,0,0,.12) 30%, rgba(0,0,0,.20) 50%, rgba(0,0,0,.42) 62%, rgba(0,0,0,.55) 78%, rgba(0,0,0,.58) 100%)"}} />
    </AbsoluteFill>
  );
};

const CIUDADES = ["Santiago", "Rancagua", "Chillán", "Concepción", "Temuco", "Puerto Montt"];

const Cierre: React.FC = () => {
  const frame = useCurrentFrame();
  const p = useSpring(4);
  const anillo = useSpring(10);
  const boton = interpolate(frame, [22, 36], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const bloque = (lado: "sup" | "inf") => {
    const sup = lado === "sup";
    const dx = interpolate(p, [0, 1], [sup ? -560 : 560, 0]);
    return (
      <div style={{position: "absolute", transform: `translateX(${dx}px)`, left: sup ? 0 : 530, top: sup ? 0 : 1693,
        width: 550, height: 227}}>
        {/* filete */}
        <div style={{position: "absolute", left: sup ? -20 : 0, top: sup ? -20 : 0, width: sup ? 547 : 570, height: sup ? 246 : 247,
          border: `3.5px solid ${RED}`, borderRadius: sup ? "0 0 52px 0" : "52px 0 0 0"}} />
        {/* bloque macizo */}
        <div style={{position: "absolute", left: sup ? 0 : 22, top: sup ? 0 : 28, width: sup ? 505 : 528, height: 198,
          background: RED, borderRadius: sup ? "0 0 46px 0" : "46px 0 0 0"}} />
      </div>
    );
  };
  return (
    <AbsoluteFill style={{background: WHITE}}>
      {bloque("sup")}
      {bloque("inf")}
      <Img src={staticFile(`${DIR}/logo_ebema_circulo.png`)} style={{position: "absolute", left: 344 - 30 * 1.649,
        top: 586 - 25 * 1.649, width: 310 * 1.649, opacity: anillo, transform: `scale(${interpolate(anillo, [0, 1], [0.86, 1])})`}} />
      <div style={{position: "absolute", left: 279.5, top: 1261, width: 521, height: 71, background: RED,
        color: WHITE, fontFamily: RALEWAY, fontWeight: 400, fontSize: 44, lineHeight: "71px", textAlign: "center",
        opacity: boton, filter: `blur(${interpolate(boton, [0, 1], [10, 0])}px)`}}>
        Toca el enlace
      </div>
    </AbsoluteFill>
  );
};

export const EbemaGrillaStoryClickOct: React.FC = () => {
  ensureFonts();
  return (
    <AbsoluteFill style={{background: "#111"}}>
      {ESC.map((e) => (
        <Sequence key={e.clip} from={e.from} durationInFrames={e.dur + 8}>
          <Clip src={e.clip} dur={e.dur} escala={(e as {escala?: number}).escala} />
        </Sequence>
      ))}

      {/* marco de las escenas: arcos + lockup (no van en el cierre) */}
      <Sequence from={0} durationInFrames={CIERRE.from}>
        <Arcos />
        {/* ⚠️ En julio la tinta del lockup iba en y 369–479. Acá sube 115 (tinta 254–364):
            Kling acerca la cámara durante el plano y a 369 el lockup le caía en la frente
            al ferretero. Más arriba no se puede: a y < 250 choca con el arco rojo. */}
        <Img src={staticFile(`${DIR}/logo_click_2_blanco_acento.png`)}
          style={{position: "absolute", left: 247, top: 213.8, width: 585}} />
      </Sequence>

      {/* T1 */}
      <Sequence from={ESC[0].from} durationInFrames={ESC[0].dur}>
        <Bloque top={1150} dur={ESC[0].dur}>
          <Linea delay={10}>¿Cuánto tiempo</Linea>
          <Caja delay={18}>pierdes abasteciéndote?</Caja>
        </Bloque>
      </Sequence>

      {/* T2 */}
      <Sequence from={ESC[1].from} durationInFrames={ESC[1].dur}>
        <Bloque top={1130} dur={ESC[1].dur}>
          <Linea delay={8} caps={false} weight={600}>Con Ebema Click</Linea>
          <Linea delay={14} caps={false}><Num t="compras online, 24/7" /></Linea>
          <Caja delay={22} caps={false}>y sin filas.</Caja>
        </Bloque>
      </Sequence>

      {/* T3 — las ciudades de a una. El bloque sube a 930 para no invadir la franja
          del sticker (1450–1600). */}
      <Sequence from={ESC[2].from} durationInFrames={ESC[2].dur}>
        <Bloque top={930} dur={ESC[2].dur}>
          <Linea delay={8}>Para ferreteros y</Linea>
          <Linea delay={13}>contratistas de</Linea>
          <div style={{height: 14}} />
          {CIUDADES.map((c, i) => (
            <Caja key={c} delay={24 + i * 14} caps={false} size={40} ancho={380} alto={56}>{c}</Caja>
          ))}
        </Bloque>
      </Sequence>

      {/* T4 */}
      <Sequence from={ESC[3].from} durationInFrames={ESC[3].dur}>
        <Bloque top={1150} dur={ESC[3].dur}>
          <Linea delay={8} caps={false}>Y cada mes sorteamos</Linea>
          <Caja delay={15} caps={false}>una gift card</Caja>
          <Linea delay={22} caps={false}>entre quienes compran.</Linea>
        </Bloque>
      </Sequence>

      {/* T5 — cierre en blanco */}
      <Sequence from={CIERRE.from} durationInFrames={CIERRE.dur}>
        <Cierre />
      </Sequence>
    </AbsoluteFill>
  );
};
