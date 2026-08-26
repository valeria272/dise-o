import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  OffthreadVideo,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

// =============================================================================
// EBEMA — Reel 1 Septiembre · "Nuevo Showroom Ebema Antofagasta" (cerámicas)
// 1080×1920 (story) · 1080×1350 (feed) · 30 fps · 18 s (540 frames)
// Sistema gráfico PAID de Paulina llevado a motion: Raleway Black, caja roja
// #EC1C23 detrás de la 2ª línea y media 1ª, marco blanco, logo EBEMA saliendo
// del borde, CTA rojo sin sombra, números en Helvetica. Textos verbatim de la
// grilla de septiembre (brief Reel 1 + copys aprobados).
// VO: public/assets/ebema/vo/r1_01..03.mp3 · Música: musica_reel.mp3 (Mixkit)
// =============================================================================

const RED = "#EC1C23";
const WHITE = "#FFFFFF";
const INK = "#111111";

export const EBEMA_REEL_FPS = 30;
export const EBEMA_REEL_DURATION = 540;

let ebFontsInjected = false;
const ensureEbemaFonts = () => {
  if (ebFontsInjected || typeof document === "undefined") return;
  ebFontsInjected = true;
  const f = (w: number, file: string) =>
    `@font-face { font-family:'RalewayEB'; font-weight:${w}; font-display:block; src:url(${staticFile(`assets/ebema/fonts/${file}`)}) format('truetype'); }`;
  const css = [
    f(400, "Raleway-Regular.ttf"),
    f(600, "Raleway-SemiBold.ttf"),
    f(700, "Raleway-Bold.ttf"),
    f(800, "Raleway-ExtraBold.ttf"),
    f(900, "Raleway-Black.ttf"),
    `@font-face { font-family:'HelvEB'; font-weight:700; font-display:block; src:url(${staticFile("assets/ebema/fonts/Helvetica-Bold.ttf")}) format('truetype'); }`,
  ].join("\n");
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);
  const fs = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (fs) ["400", "600", "700", "800", "900"].forEach((w) => fs.load(`${w} 40px RalewayEB`));
};
const RALEWAY = "'RalewayEB', 'Raleway', Arial, sans-serif";

type Fmt = "story" | "feed";
export type EbemaShowroomReelProps = {format: Fmt; variant?: 1 | 2};

// ---- timeline (frames @30fps) -------------------------------------------------
const T = {
  hookEnd: 78, // 0–2.6 s  hook
  introEnd: 168, // 2.6–5.6 s  "diseño, calidad e innovación"
  cardsEnd: 318, // 5.6–10.6 s  3 íconos
  visitEnd: 432, // 10.6–14.4 s  visita el showroom
  end: 540, // 14.4–18 s  cierre
};
const VO = {a: 21, b: 180, c: 330}; // 0.7 s · 6.0 s · 11.0 s  (Reel 1)
const VO2 = {a: 21, b: 90, c: 219, d: 360}; // Reel 2: 0.7 · 3.0 · 7.3 · 12.0 s

const TXT = {
  1: {
    hookPill: "Septiembre", hook: ["Nuevo Showroom", "Ebema Antofagasta"],
    introKicker: "", intro: ["Diseño, calidad", "e innovación"],
    introBajada: <>ahora tienen <b style={{fontWeight: 800}}>un nuevo espacio</b> en EBEMA Antofagasta</>,
    visitPill: "Antofagasta", visit: ["Visita el Showroom", "este septiembre"],
    visitBajada: <>Encuentra <b style={{fontWeight: 800}}>cerámicas, revestimientos y terminaciones</b> para tu proyecto.</>,
    cierreBtn: "Te esperamos en nuestra sucursal",
    fotos: {hook: "sr01_entrada", intro: "sr02_muro_ceramicas", cards: "sr03_bano", visit: "sr05_pisos", cierre: "sr04_cocina"},
  },
  2: {
    hookPill: "Septiembre", hook: ["Renueva tus espacios", "este septiembre"],
    introKicker: "Más que un showroom,", intro: ["un espacio para", "descubrir nuevas ideas"],
    introBajada: <>Recorre <b style={{fontWeight: 800}}>distintas alternativas</b>, compara productos e inspírate</>,
    visitPill: "Antofagasta", visit: ["Visita el Showroom", "Ebema Antofagasta"],
    visitBajada: <>Encuentra <b style={{fontWeight: 800}}>la inspiración para tu proyecto</b> este septiembre.</>,
    cierreBtn: "Te esperamos",
    fotos: {hook: "sr04_cocina", intro: "sr06_mano", cards: "sr02_muro_ceramicas", visit: "sr05_pisos", cierre: "sr01_entrada"},
  },
} as const;

// ---- helpers -----------------------------------------------------------------
const useIn = (delay = 0, cfg = {damping: 13, stiffness: 170}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  return spring({fps, frame: frame - delay, config: cfg});
};

/** Foto con Ken Burns + velo (filtro negro 20 %). */
const Foto: React.FC<{
  src: string;
  from?: number; // frame local de inicio del movimiento
  zoom?: [number, number];
  pan?: [number, number]; // % horizontal
  posY?: number; // % vertical del encuadre
  velo?: number;
  durationInFrames: number;
}> = ({src, zoom = [1.08, 1.2], pan = [50, 50], posY = 50, velo = 0.2, durationInFrames}) => {
  const frame = useCurrentFrame();
  const z = interpolate(frame, [0, durationInFrames], zoom, {extrapolateRight: "clamp"});
  const p = interpolate(frame, [0, durationInFrames], pan, {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill>
      <Img
        src={staticFile(src)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          objectPosition: `${p}% ${posY}%`,
          transform: `scale(${z})`,
          transformOrigin: "50% 50%",
        }}
      />
      <AbsoluteFill style={{background: `rgba(0,0,0,${velo})`}} />
    </AbsoluteFill>
  );
};

/** Marco blanco + logo EBEMA en caja blanca que sale del borde superior (misma geometría que las estáticas v9: marco 3 px
 *  inset 77/62/71 radio 20; caja 152×186 en x=139; logo 103 px centrado). Nunca flotando (Paulina 21-08). */
const MarcoLogo: React.FC<{fmt: Fmt}> = ({fmt}) => {
  const frame = useCurrentFrame();
  const logoIn = spring({fps: 30, frame: frame - 4, config: {damping: 14, stiffness: 160}});
  return (
    <>
      <div
        style={{
          position: "absolute",
          inset: "77px 62px 71px 62px",
          border: `3px solid ${WHITE}`,
          borderRadius: 20,
          opacity: interpolate(frame, [0, 10], [0, 1], {extrapolateRight: "clamp"}),
        }}
      />
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 139,
          transform: `translateY(${interpolate(logoIn, [0, 1], [-200, 0])}px)`,
          width: 152,
          height: 186,
          background: WHITE,
          borderRadius: "0 0 14px 14px",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          paddingTop: 10,
          zIndex: 6,
        }}
      >
        <Img src={staticFile("assets/ebema/logos/logo_ebema_circulo.png")} style={{width: 103}} />
      </div>
    </>
  );
};

/** Titular 2 líneas: caja roja detrás de toda la 2ª línea y mitad de la 1ª. */
const Titular: React.FC<{l1: string; l2: string; size: number; delay?: number; out?: number}> = ({
  l1,
  l2,
  size,
  delay = 0,
  out,
}) => {
  const frame = useCurrentFrame();
  const s1 = useIn(delay, {damping: 12, stiffness: 190});
  const s2 = useIn(delay + 5, {damping: 12, stiffness: 190});
  const box = useIn(delay + 2, {damping: 16, stiffness: 140});
  const exit = out ? interpolate(frame, [out - 10, out], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 1;
  return (
    <div
      style={{
        position: "relative",
        display: "inline-block",
        padding: "0 26px",
        lineHeight: 1,
        fontFamily: RALEWAY,
        fontWeight: 900,
        fontSize: size,
        color: WHITE,
        textTransform: "uppercase",
        letterSpacing: 0.3,
        textShadow: "0 2px 5px rgba(0,0,0,.22)",
        opacity: exit,
        transform: `scale(${interpolate(exit, [0, 1], [1.06, 1])})`,
      }}
    >
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: size * 0.5,
          bottom: -10,
          background: RED,
          transformOrigin: "0% 50%",
          transform: `scaleX(${box})`,
        }}
      />
      <span
        style={{
          position: "relative",
          display: "block",
          whiteSpace: "nowrap",
          transform: `translateY(${interpolate(s1, [0, 1], [40, 0])}px)`,
          opacity: s1,
        }}
      >
        {l1}
      </span>
      <span
        style={{
          position: "relative",
          display: "block",
          whiteSpace: "nowrap",
          marginTop: 2,
          transform: `translateY(${interpolate(s2, [0, 1], [40, 0])}px)`,
          opacity: s2,
        }}
      >
        {l2}
      </span>
    </div>
  );
};

const Pill: React.FC<{text: string; delay?: number}> = ({text, delay = 0}) => {
  const s = useIn(delay);
  return (
    <div
      style={{
        display: "inline-block",
        border: `3px solid ${WHITE}`,
        borderRadius: 999,
        color: WHITE,
        fontFamily: RALEWAY,
        fontWeight: 700,
        fontSize: 27,
        letterSpacing: 5,
        textTransform: "uppercase",
        padding: "12px 40px",
        opacity: s,
        transform: `scale(${interpolate(s, [0, 1], [0.7, 1])})`,
      }}
    >
      {text}
    </div>
  );
};

const Boton: React.FC<{text: string; delay?: number}> = ({text, delay = 0}) => {
  const s = useIn(delay, {damping: 10, stiffness: 220});
  return (
    <div
      style={{
        display: "inline-block",
        background: RED,
        color: WHITE,
        fontFamily: RALEWAY,
        fontWeight: 700,
        fontSize: 32,
        padding: "16px 48px",
        borderRadius: 10,
        opacity: s,
        transform: `scale(${interpolate(s, [0, 1], [0.6, 1])})`,
      }}
    >
      {text}
    </div>
  );
};

// ---- íconos (línea blanca) ---------------------------------------------------
const Icono: React.FC<{tipo: "ceramicas" | "revestimientos" | "terminaciones"}> = ({tipo}) => {
  const st = {stroke: WHITE, strokeWidth: 5, fill: "none", strokeLinecap: "round" as const, strokeLinejoin: "round" as const};
  if (tipo === "ceramicas")
    return (
      <svg viewBox="0 0 100 100" width="100%" height="100%">
        <rect x="12" y="12" width="34" height="34" rx="3" {...st} />
        <rect x="54" y="12" width="34" height="34" rx="3" {...st} />
        <rect x="12" y="54" width="34" height="34" rx="3" {...st} />
        <rect x="54" y="54" width="34" height="34" rx="3" {...st} />
      </svg>
    );
  if (tipo === "revestimientos")
    return (
      <svg viewBox="0 0 100 100" width="100%" height="100%">
        <path d="M12 30 H88 M12 50 H88 M12 70 H88" {...st} />
        <path d="M35 30 V50 M65 30 V50 M25 50 V70 M50 50 V70 M75 50 V70 M50 10 V30 M50 70 V90" {...st} />
        <rect x="12" y="10" width="76" height="80" rx="4" {...st} />
      </svg>
    );
  return (
    <svg viewBox="0 0 100 100" width="100%" height="100%">
      <rect x="14" y="14" width="52" height="26" rx="5" {...st} />
      <path d="M66 27 H80 V45 H50 V60" {...st} />
      <rect x="42" y="60" width="16" height="28" rx="4" {...st} />
    </svg>
  );
};

const Card: React.FC<{tipo: "ceramicas" | "revestimientos" | "terminaciones"; label: string; delay: number}> = ({tipo, label, delay}) => {
  const s = useIn(delay, {damping: 11, stiffness: 200});
  const t = useIn(delay + 6);
  return (
    <div style={{display: "flex", alignItems: "center", gap: 28, opacity: s, transform: `translateX(${interpolate(s, [0, 1], [-60, 0])}px)`}}>
      <div style={{width: 118, height: 118, borderRadius: 22, background: RED, padding: 20, flexShrink: 0}}>
        <Icono tipo={tipo} />
      </div>
      <div
        style={{
          fontFamily: RALEWAY,
          fontWeight: 900,
          fontSize: 62,
          color: WHITE,
          textTransform: "uppercase",
          textShadow: "0 2px 6px rgba(0,0,0,.3)",
          opacity: t,
          transform: `translateX(${interpolate(t, [0, 1], [30, 0])}px)`,
        }}
      >
        {label}
      </div>
    </div>
  );
};

// ---- escenas -----------------------------------------------------------------
const Centro: React.FC<{fmt: Fmt; top?: string; children: React.ReactNode}> = ({fmt, top, children}) => (
  <div
    style={{
      position: "absolute",
      left: 0,
      right: 0,
      top: top ?? (fmt === "story" ? "50%" : "52%"),
      transform: "translateY(-50%)",
      textAlign: "center",
      padding: "0 80px",
      zIndex: 4,
    }}
  >
    {children}
  </div>
);

const Hook: React.FC<{fmt: Fmt; v: 1 | 2}> = ({fmt, v}) => {
  const t = TXT[v];
  const frame = useCurrentFrame();
  const flash = interpolate(frame, [0, 3, 9], [1, 0.55, 0], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill>
      <Foto src={`assets/ebema/showroom/${t.fotos.hook}.png`} zoom={[1.25, 1.08]} durationInFrames={T.hookEnd} />
      <AbsoluteFill style={{background: WHITE, opacity: flash}} />
      <Centro fmt={fmt}>
        <div style={{marginBottom: 26}}>
          <Pill text={t.hookPill} delay={6} />
        </div>
        <Titular l1={t.hook[0]} l2={t.hook[1]} size={80} delay={10} out={T.hookEnd} />
      </Centro>
    </AbsoluteFill>
  );
};

const Intro: React.FC<{fmt: Fmt; v: 1 | 2}> = ({fmt, v}) => {
  const t = TXT[v];
  return (
  <AbsoluteFill>
    <Foto src={`assets/ebema/showroom/${t.fotos.intro}.png`} zoom={[1.28, 1.4]} pan={[40, 60]} posY={40} durationInFrames={T.introEnd - T.hookEnd} />
    <Centro fmt={fmt}>
      {t.introKicker ? <div style={{fontFamily: RALEWAY, fontWeight: 600, fontSize: 40, color: WHITE, marginBottom: 12, textShadow: "0 1px 6px rgba(0,0,0,.35)"}}>{t.introKicker}</div> : null}
      <Titular l1={t.intro[0]} l2={t.intro[1]} size={t.introKicker ? 72 : 82} delay={2} out={T.introEnd - T.hookEnd} />
      <div style={{marginTop: 26, fontFamily: RALEWAY, fontWeight: 600, fontSize: 30, color: WHITE, textShadow: "0 1px 6px rgba(0,0,0,.35)"}}>
        {t.introBajada}
      </div>
    </Centro>
  </AbsoluteFill>
  );
};

const Cards: React.FC<{fmt: Fmt; v: 1 | 2}> = ({fmt, v}) => (
  <AbsoluteFill>
    <Foto src={`assets/ebema/showroom/${TXT[v].fotos.cards}.png`} zoom={[1.06, 1.18]} pan={[55, 45]} velo={0.52} durationInFrames={T.cardsEnd - T.introEnd} />
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: fmt === "story" ? "50%" : "52%",
        transform: "translateY(-50%)",
        padding: "0 110px",
        display: "flex",
        flexDirection: "column",
        gap: 44,
        zIndex: 4,
      }}
    >
      <Card tipo="ceramicas" label="Cerámicas" delay={4} />
      <Card tipo="revestimientos" label="Revestimientos" delay={34} />
      <Card tipo="terminaciones" label="Terminaciones" delay={64} />
      <div style={{fontFamily: RALEWAY, fontWeight: 600, fontSize: 32, color: WHITE, marginTop: 8, opacity: 1}}>
        <Pill text="para tu proyecto" delay={100} />
      </div>
    </div>
  </AbsoluteFill>
);

const Visita: React.FC<{fmt: Fmt; v: 1 | 2}> = ({fmt, v}) => {
  const t = TXT[v];
  return (
  <AbsoluteFill>
    <Foto src={`assets/ebema/showroom/${t.fotos.visit}.png`} zoom={[1.18, 1.06]} pan={[60, 40]} durationInFrames={T.visitEnd - T.cardsEnd} />
    <Centro fmt={fmt}>
      <div style={{marginBottom: 26}}>
        <Pill text={t.visitPill} delay={4} />
      </div>
      <Titular l1={t.visit[0]} l2={t.visit[1]} size={78} delay={6} out={T.visitEnd - T.cardsEnd} />
      <div style={{marginTop: 26, fontFamily: RALEWAY, fontWeight: 600, fontSize: 30, color: WHITE, textShadow: "0 1px 6px rgba(0,0,0,.35)"}}>
        {t.visitBajada}
      </div>
    </Centro>
  </AbsoluteFill>
  );
};

const Cierre: React.FC<{fmt: Fmt; v: 1 | 2}> = ({fmt, v}) => {
  const t = TXT[v];
  const frame = useCurrentFrame();
  const dur = T.end - T.visitEnd;
  const vid = fmt === "story" ? "cierre_ebema_st" : "cierre_ebema_post";
  const vidFrames = fmt === "story" ? 105 : 94; // 3,5 s / 3,13 s @30fps
  const txt = useIn(52, {damping: 14, stiffness: 150});
  return (
    <AbsoluteFill style={{background: WHITE}}>
      {/* cierre oficial de la marca (Paulina, 21-08): logo EBEMA sobre blanco con las curvas rojas */}
      <Sequence from={0} durationInFrames={vidFrames} layout="none">
        <OffthreadVideo src={staticFile(`assets/ebema/cierres/${vid}_mute.mp4`)} style={{width: "100%", height: "100%", objectFit: "cover"}} muted />
      </Sequence>
      <Sequence from={vidFrames} durationInFrames={dur - vidFrames} layout="none">
        <Img src={staticFile(`assets/ebema/cierres/${vid}_last.png`)} style={{width: "100%", height: "100%", objectFit: "cover"}} />
      </Sequence>
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: fmt === "story" ? "64%" : "68%",
          textAlign: "center",
          padding: "0 90px",
          opacity: txt,
          transform: `translateY(${interpolate(txt, [0, 1], [30, 0])}px)`,
          zIndex: 4,
        }}
      >
        <div style={{fontFamily: RALEWAY, fontWeight: 900, fontSize: fmt === "story" ? 60 : 52, color: "#6D6F72", textTransform: "uppercase", lineHeight: 1.02}}>
          Showroom Ebema<br />Antofagasta
        </div>
        <div style={{marginTop: 30}}>
          <Boton text={t.cierreBtn} delay={64} />
        </div>
      </div>
      <AbsoluteFill style={{background: INK, opacity: interpolate(frame, [dur - 10, dur], [0, 1], {extrapolateLeft: "clamp"})}} />
    </AbsoluteFill>
  );
};

// ---- audio -------------------------------------------------------------------
const Musica: React.FC<{v: 1 | 2}> = ({v}) => {
  const frame = useCurrentFrame();
  // ducking por ARREGLO (no por envolvente): baja en los tramos con voz, en el compás
  const vozTramos: [number, number][] = v === 1
    ? [[VO.a, VO.a + 141], [VO.b, VO.b + 125], [VO.c, VO.c + 152]]
    : [[VO2.a, VO2.a + 81], [VO2.b, VO2.b + 123], [VO2.c, VO2.c + 125], [VO2.d, VO2.d + 133]];
  const enVoz = vozTramos.some(([a, b]) => frame >= a - 6 && frame <= b + 6);
  const base = enVoz ? 0.12 : 0.26;
  const fadeIn = interpolate(frame, [0, 20], [0, 1], {extrapolateRight: "clamp"});
  const fadeOut = interpolate(frame, [T.end - 40, T.end], [1, 0], {extrapolateLeft: "clamp"});
  return <Audio src={staticFile("assets/ebema/musica_reel.mp3")} volume={base * fadeIn * fadeOut} />;
};

// ---- composición -------------------------------------------------------------
export const EbemaShowroomReel: React.FC<EbemaShowroomReelProps> = ({format, variant = 1}) => {
  ensureEbemaFonts();
  const fmt = format;
  const v = variant;
  return (
    <AbsoluteFill style={{background: INK}}>
      <Sequence from={0} durationInFrames={T.hookEnd}><Hook fmt={fmt} v={v} /></Sequence>
      <Sequence from={T.hookEnd} durationInFrames={T.introEnd - T.hookEnd}><Intro fmt={fmt} v={v} /></Sequence>
      <Sequence from={T.introEnd} durationInFrames={T.cardsEnd - T.introEnd}><Cards fmt={fmt} v={v} /></Sequence>
      <Sequence from={T.cardsEnd} durationInFrames={T.visitEnd - T.cardsEnd}><Visita fmt={fmt} v={v} /></Sequence>
      <Sequence from={T.visitEnd} durationInFrames={T.end - T.visitEnd}><Cierre fmt={fmt} v={v} /></Sequence>
      <Sequence from={0} durationInFrames={T.visitEnd}><MarcoLogo fmt={fmt} /></Sequence>
      {v === 1 ? (
        <>
          <Sequence from={VO.a}><Audio src={staticFile("assets/ebema/vo/r1_01.mp3")} /></Sequence>
          <Sequence from={VO.b}><Audio src={staticFile("assets/ebema/vo/r1_02.mp3")} /></Sequence>
          <Sequence from={VO.c}><Audio src={staticFile("assets/ebema/vo/r1_03.mp3")} /></Sequence>
        </>
      ) : (
        <>
          <Sequence from={VO2.a}><Audio src={staticFile("assets/ebema/vo/r2_01.mp3")} /></Sequence>
          <Sequence from={VO2.b}><Audio src={staticFile("assets/ebema/vo/r2_02.mp3")} /></Sequence>
          <Sequence from={VO2.c}><Audio src={staticFile("assets/ebema/vo/r2_03.mp3")} /></Sequence>
          <Sequence from={VO2.d}><Audio src={staticFile("assets/ebema/vo/r2_04.mp3")} /></Sequence>
        </>
      )}
      <Musica v={v} />
    </AbsoluteFill>
  );
};
