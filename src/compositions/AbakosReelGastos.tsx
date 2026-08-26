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

// ============================================================
// ABAKOS — Reel Septiembre · VIDEO 2
// "SEPTIEMBRE TIENE MÁS GASTOS QUE DÍAS"
// 1080×1920 · 30 fps · ~19 s
// Meme de dos tiempos: "Yo entrando a septiembre" → "Septiembre:"
// → lluvia de gastos → cierre responsable → CTA
// ============================================================

const ABAKOS = {
  purple: "#433491",
  magenta: "#EE00A8",
  orange: "#FC8222",
  yellow: "#FFB533",
  ink: "#2B2450",
  paper: "#FFFFFF",
  cream: "#F7F5FF",
};

export const ABAKOS_GASTOS_FPS = 30;
export const ABAKOS_GASTOS_DURATION = 580; // ~19.3 s

let abFontsInjected = false;
const ensureAbakosFonts = () => {
  if (abFontsInjected || typeof document === "undefined") return;
  abFontsInjected = true;
  const css = `
    @font-face { font-family: 'Poppins'; font-style: normal; font-weight: 400; font-display: block;
      src: url(${staticFile("assets/fonts/Poppins-Regular.ttf")}) format('truetype'); }
    @font-face { font-family: 'Poppins'; font-style: normal; font-weight: 500; font-display: block;
      src: url(${staticFile("assets/fonts/Poppins-Medium.ttf")}) format('truetype'); }
    @font-face { font-family: 'Poppins'; font-style: normal; font-weight: 600; font-display: block;
      src: url(${staticFile("assets/fonts/Poppins-SemiBold.ttf")}) format('truetype'); }
    @font-face { font-family: 'Poppins'; font-style: normal; font-weight: 700; font-display: block;
      src: url(${staticFile("assets/fonts/Poppins-Bold.ttf")}) format('truetype'); }
    @font-face { font-family: 'Poppins'; font-style: normal; font-weight: 800; font-display: block;
      src: url(${staticFile("assets/fonts/Poppins-ExtraBold.ttf")}) format('truetype'); }
  `;
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);
  const f = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (f) ["400", "500", "600", "700", "800"].forEach((w) => f.load(`${w} 40px Poppins`));
};

const POPPINS = "'Poppins', 'Helvetica Neue', sans-serif";

// Timeline (frames @30fps)
const OPT_END = 110; //   0.0–3.7s  optimista
const HIT_END = 225; //   3.7–7.5s  llega septiembre (18)
const GASTOS_END = 350; // 7.5–11.7s lluvia de gastos
const CALMA_END = 465; // 11.7–15.5s cierre responsable
// 465–580 CTA

const fadeOut = (frame: number, dur: number) =>
  interpolate(frame, [dur - 12, dur], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

// Etiqueta estilo "meme caption"
const MemeTag: React.FC<{children: React.ReactNode; progress: number}> = ({children, progress}) => (
  <div
    style={{
      fontFamily: POPPINS,
      fontWeight: 700,
      fontSize: 54,
      color: "#FFFFFF",
      backgroundColor: "rgba(30,24,60,0.82)",
      padding: "18px 44px",
      borderRadius: 999,
      opacity: progress,
      transform: `translateY(${interpolate(progress, [0, 1], [-40, 0])}px)`,
    }}
  >
    {children}
  </div>
);

// ------------------------------------------------------------
// Escena 1 — OPTIMISTA: "Yo entrando a septiembre"
// ------------------------------------------------------------
const OptimistaScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  // Entrada "wow" del título POV: dos líneas que aterrizan con golpe
  const line1 = spring({fps, frame, config: {damping: 10, stiffness: 210}});
  const line2 = spring({fps, frame: frame - 8, config: {damping: 10, stiffness: 210}});
  const quoteIn = spring({fps, frame: frame - 26, config: {damping: 12, stiffness: 150}});
  // Escalado + corrimiento hacia abajo: deja la cara del protagonista
  // despejada bajo el bloque de títulos POV
  const zoom = interpolate(frame, [0, OPT_END], [1.3, 1.38]);

  return (
    <AbsoluteFill style={{backgroundColor: ABAKOS.cream, opacity: fadeOut(frame, OPT_END)}}>
      <Img
        src={staticFile("assets/abakos/optimista-h.png")}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          objectPosition: "50% 35%",
          transform: `translateY(275px) scale(${zoom})`,
          filter: "saturate(1.06) brightness(1.02)",
        }}
      />
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(25,20,50,0.55) 0%, rgba(25,20,50,0.12) 40%, rgba(25,20,50,0.0) 62%, rgba(25,20,50,0.45) 100%)",
        }}
      />
      {/* Título POV — lectura guiada de arriba hacia abajo */}
      <AbsoluteFill style={{alignItems: "center", paddingTop: 130, flexDirection: "column", gap: 26}}>
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 800,
            fontSize: 92,
            letterSpacing: 1,
            color: "#FFFFFF",
            backgroundColor: ABAKOS.purple,
            padding: "6px 44px 14px",
            borderRadius: 24,
            transform: `scale(${interpolate(line1, [0, 1], [2.6, 1])}) rotate(${interpolate(
              line1,
              [0, 1],
              [-9, -2],
            )}deg)`,
            opacity: line1,
            boxShadow: "0 18px 50px rgba(15,8,45,0.45)",
          }}
        >
          YO ENTRANDO
        </div>
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 800,
            fontSize: 92,
            letterSpacing: 1,
            color: "#FFFFFF",
            backgroundColor: ABAKOS.magenta,
            padding: "6px 44px 14px",
            borderRadius: 24,
            transform: `scale(${interpolate(line2, [0, 1], [2.6, 1])}) rotate(${interpolate(
              line2,
              [0, 1],
              [9, 2],
            )}deg)`,
            opacity: line2,
            boxShadow: "0 18px 50px rgba(15,8,45,0.45)",
          }}
        >
          A SEPTIEMBRE:
        </div>
        <div
          style={{
            marginTop: 18,
            fontFamily: POPPINS,
            fontWeight: 700,
            fontSize: 62,
            lineHeight: 1.15,
            color: ABAKOS.ink,
            backgroundColor: ABAKOS.yellow,
            padding: "22px 46px",
            borderRadius: 999,
            textAlign: "center",
            opacity: quoteIn,
            transform: `translateY(${interpolate(quoteIn, [0, 1], [46, 0])}px) scale(${interpolate(
              quoteIn,
              [0, 1],
              [0.8, 1],
            )}) rotate(-1.5deg)`,
            boxShadow: "0 18px 44px rgba(15,8,45,0.35)",
          }}
        >
          ¡Este mes sí me organizo!
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------
// Escena 2 — GOLPE: "Septiembre:" (anticuchos + terremotos)
// ------------------------------------------------------------
const SeptiembreScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const dur = HIT_END - OPT_END;

  const slam = spring({fps, frame, config: {damping: 10, stiffness: 220}});
  const textIn = spring({fps, frame: frame - 20, config: {damping: 13, stiffness: 140}});
  const zoom = interpolate(frame, [0, dur], [1.18, 1.06]);
  // mini sacudida al aterrizar el "Septiembre:"
  const shake = frame < 14 ? Math.sin(frame * 2.4) * interpolate(frame, [0, 14], [9, 0]) : 0;

  return (
    <AbsoluteFill style={{backgroundColor: "#1d1428", opacity: fadeOut(frame, dur)}}>
      <AbsoluteFill style={{transform: `translateX(${shake}px)`}}>
        <Img
          src={staticFile("assets/abakos/dieciocho.png")}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
            objectPosition: "50% 55%",
            transform: `scale(${zoom})`,
            filter: "saturate(1.1)",
          }}
        />
        <AbsoluteFill
          style={{
            background:
              "linear-gradient(180deg, rgba(29,20,40,0.5) 0%, rgba(29,20,40,0.05) 40%, rgba(29,20,40,0.78) 100%)",
          }}
        />
      </AbsoluteFill>
      <AbsoluteFill style={{alignItems: "center", paddingTop: 170}}>
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 800,
            fontSize: 96,
            color: "#FFFFFF",
            backgroundColor: ABAKOS.orange,
            padding: "8px 60px 16px",
            borderRadius: 26,
            transform: `scale(${interpolate(slam, [0, 1], [2.2, 1])}) rotate(${interpolate(
              slam,
              [0, 1],
              [-8, 2],
            )}deg)`,
            opacity: slam,
          }}
        >
          Septiembre:
        </div>
      </AbsoluteFill>
      <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: 220}}>
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 700,
            fontSize: 54,
            lineHeight: 1.24,
            color: "#FFFFFF",
            textAlign: "center",
            padding: "0 80px",
            maxWidth: 980,
            opacity: textIn,
            transform: `translateY(${interpolate(textIn, [0, 1], [46, 0])}px)`,
            textShadow: "0 6px 30px rgba(0,0,0,0.55)",
          }}
        >
          “Se viene el 18 y los anticuchos con los terremotos{" "}
          <span style={{color: ABAKOS.yellow, fontWeight: 800}}>no salen gratis”.</span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------
// Escena 3 — LLUVIA DE GASTOS
// ------------------------------------------------------------
const GASTOS: {icon: string; label: string; color: string; x: number; y: number; rot: number}[] = [
  {icon: "💡", label: "Cuenta de servicios", color: ABAKOS.magenta, x: 90, y: 330, rot: -5},
  {icon: "🚌", label: "Transporte", color: ABAKOS.orange, x: 620, y: 560, rot: 4},
  {icon: "🛒", label: "Compras del hogar", color: ABAKOS.purple, x: 120, y: 680, rot: -3},
  {icon: "🔧", label: "Reparación pendiente", color: ABAKOS.orange, x: 470, y: 1180, rot: 5},
  {icon: "🎁", label: "Compromisos familiares", color: ABAKOS.magenta, x: 100, y: 1360, rot: -4},
];

const GastosScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const dur = GASTOS_END - HIT_END;

  const zoom = interpolate(frame, [0, dur], [1.05, 1.12]);
  const tagIn = spring({fps, frame, config: {damping: 15, stiffness: 130}});
  // sacudida sutil mientras caen los gastos
  const shake = interpolate(frame, [20, 90], [3, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{backgroundColor: "#241d3d", opacity: fadeOut(frame, dur)}}>
      <AbsoluteFill style={{transform: `translateX(${Math.sin(frame * 1.7) * shake}px)`}}>
        <Img
          src={staticFile("assets/abakos/agobiado-h.png")}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
            objectPosition: "50% 28%",
            transform: `scale(${zoom})`,
          }}
        />
        <AbsoluteFill style={{backgroundColor: "rgba(29,22,50,0.34)"}} />
      </AbsoluteFill>
      <AbsoluteFill style={{alignItems: "center", paddingTop: 150}}>
        <MemeTag progress={tagIn}>Y los gastos llegan todos juntos…</MemeTag>
      </AbsoluteFill>
      {GASTOS.map((g, i) => {
        const p = spring({fps, frame: frame - 16 - i * 10, config: {damping: 11, stiffness: 180}});
        return (
          <div
            key={g.label}
            style={{
              position: "absolute",
              left: g.x,
              top: g.y,
              display: "flex",
              alignItems: "center",
              gap: 20,
              backgroundColor: ABAKOS.paper,
              borderRadius: 999,
              padding: "16px 34px 16px 16px",
              boxShadow: "0 16px 44px rgba(15,8,45,0.4)",
              opacity: p,
              transform: `translateY(${interpolate(p, [0, 1], [-70, 0])}px) rotate(${
                g.rot * p
              }deg) scale(${interpolate(p, [0, 1], [0.7, 1])})`,
            }}
          >
            <div
              style={{
                width: 76,
                height: 76,
                borderRadius: "50%",
                backgroundColor: g.color,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: 40,
              }}
            >
              {g.icon}
            </div>
            <div style={{fontFamily: POPPINS, fontWeight: 600, fontSize: 40, color: ABAKOS.ink}}>
              {g.label}
            </div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------
// Escena 4 — CALMA: cierre responsable
// ------------------------------------------------------------
const CalmaScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const dur = CALMA_END - GASTOS_END;

  const wash = spring({fps, frame, config: {damping: 16, stiffness: 120}});
  const l1 = spring({fps, frame: frame - 12, config: {damping: 14, stiffness: 130}});
  const l2 = spring({fps, frame: frame - 34, config: {damping: 14, stiffness: 130}});
  const l3 = spring({fps, frame: frame - 56, config: {damping: 12, stiffness: 150}});

  return (
    <AbsoluteFill style={{backgroundColor: ABAKOS.purple, opacity: fadeOut(frame, dur)}}>
      <AbsoluteFill
        style={{
          backgroundColor: ABAKOS.purple,
          transform: `translateY(${interpolate(wash, [0, 1], [100, 0])}%)`,
        }}
      />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          gap: 58,
          padding: "0 100px",
        }}
      >
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 700,
            fontSize: 64,
            lineHeight: 1.24,
            color: "#FFFFFF",
            textAlign: "center",
            opacity: l1,
            transform: `translateY(${interpolate(l1, [0, 1], [44, 0])}px)`,
          }}
        >
          Cuando varios gastos llegan juntos,{" "}
          <span style={{color: ABAKOS.yellow}}>evalúa tus opciones con calma.</span>
        </div>
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 500,
            fontSize: 48,
            lineHeight: 1.3,
            color: "rgba(255,255,255,0.92)",
            textAlign: "center",
            opacity: l2,
            transform: `translateY(${interpolate(l2, [0, 1], [40, 0])}px)`,
          }}
        >
          Pide solamente lo que necesitas
          <br />y puedes pagar.
        </div>
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 700,
            fontSize: 46,
            lineHeight: 1.25,
            color: ABAKOS.ink,
            backgroundColor: ABAKOS.yellow,
            padding: "26px 48px",
            borderRadius: 30,
            textAlign: "center",
            opacity: l3,
            transform: `scale(${interpolate(l3, [0, 1], [0.8, 1])}) rotate(${interpolate(
              l3,
              [0, 1],
              [3, -1.5],
            )}deg)`,
          }}
        >
          ¡Para tener los choripanes o<br />
          anticuchos que quieras este 18! 🇨🇱
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------
// Escena 5 — CTA (misma línea del reel 1)
// ------------------------------------------------------------
const CtaScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const wash = spring({fps, frame, config: {damping: 16, stiffness: 120}});
  const logoIn = spring({fps, frame: frame - 8, config: {damping: 13, stiffness: 140}});
  const textIn = spring({fps, frame: frame - 22, config: {damping: 14, stiffness: 130}});
  const btnIn = spring({fps, frame: frame - 36, config: {damping: 11, stiffness: 160}});
  const pulse = 1 + 0.02 * Math.sin((frame - 36) / 9);

  return (
    <AbsoluteFill style={{backgroundColor: ABAKOS.purple}}>
      <AbsoluteFill
        style={{
          backgroundColor: ABAKOS.cream,
          transform: `translateY(${interpolate(wash, [0, 1], [100, 0])}%)`,
          borderRadius: interpolate(wash, [0, 1], [120, 0]),
        }}
      />
      {[ABAKOS.magenta, ABAKOS.orange, ABAKOS.yellow].map((c, i) => (
        <div
          key={c}
          style={{
            position: "absolute",
            width: 46,
            height: 46,
            borderRadius: "50%",
            backgroundColor: c,
            top: 330 + i * 26,
            left: 150 + i * 380,
            opacity: 0.9 * logoIn,
            transform: `translateY(${interpolate(logoIn, [0, 1], [60, 0])}px)`,
          }}
        />
      ))}
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          gap: 64,
          padding: "0 90px",
        }}
      >
        <Img
          src={staticFile("assets/abakos/logo.svg")}
          style={{
            width: 640,
            opacity: logoIn,
            transform: `scale(${interpolate(logoIn, [0, 1], [0.7, 1])})`,
          }}
        />
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 600,
            fontSize: 56,
            lineHeight: 1.25,
            color: ABAKOS.ink,
            textAlign: "center",
            opacity: textIn,
            transform: `translateY(${interpolate(textIn, [0, 1], [40, 0])}px)`,
          }}
        >
          Conoce las condiciones
          <br />
          en <span style={{fontWeight: 800, color: ABAKOS.purple}}>abakos.cl</span>.
        </div>
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 700,
            fontSize: 46,
            color: "#FFFFFF",
            backgroundColor: ABAKOS.magenta,
            padding: "26px 70px",
            borderRadius: 999,
            opacity: btnIn,
            transform: `scale(${interpolate(btnIn, [0, 1], [0.7, 1]) * pulse})`,
          }}
        >
          abakos.cl →
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------
// Música: "Summer's Here" (Mixkit 91, licencia libre comercial sin
// atribución). Elegida por medición: 0 bajones de energía en los
// primeros 40 s (la cumbia y el funk anteriores no convencieron).
const MusicTrack: React.FC = () => {
  const frame = useCurrentFrame();
  const volume = interpolate(
    frame,
    [0, 12, ABAKOS_GASTOS_DURATION - 50, ABAKOS_GASTOS_DURATION - 4],
    [0, 0.7, 0.7, 0],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp"},
  );
  return <Audio src={staticFile("assets/abakos/musica-reel2-final.mp3")} volume={volume} />;
};

export const AbakosReelGastos: React.FC = () => {
  ensureAbakosFonts();
  return (
    <AbsoluteFill style={{backgroundColor: ABAKOS.purple}}>
      <MusicTrack />
      <Sequence from={0} durationInFrames={OPT_END}>
        <OptimistaScene />
      </Sequence>
      <Sequence from={OPT_END} durationInFrames={HIT_END - OPT_END}>
        <SeptiembreScene />
      </Sequence>
      <Sequence from={HIT_END} durationInFrames={GASTOS_END - HIT_END}>
        <GastosScene />
      </Sequence>
      <Sequence from={GASTOS_END} durationInFrames={CALMA_END - GASTOS_END}>
        <CalmaScene />
      </Sequence>
      <Sequence from={CALMA_END}>
        <CtaScene />
      </Sequence>
    </AbsoluteFill>
  );
};
