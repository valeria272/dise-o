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

// ============================================================
// ABAKOS — Reel Septiembre · "TU TIEMPO TAMBIÉN VALE"
// 1080×1920 · 30 fps · 15 s (450 frames)
// Brand (Abakos_StyleGuide): morado #433491 · magenta #EE00A8
// naranjo #FC8222 · amarillo #FFB533 · Poppins · estilo flat
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

export const ABAKOS_REEL_FPS = 30;
export const ABAKOS_REEL_DURATION = 450; // 15 s

// --- Fuentes locales (patrón TierraCalma: @font-face inyectado, sin delayRender) ---
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
  if (f) {
    ["400", "500", "600", "700", "800"].forEach((w) => f.load(`${w} 40px Poppins`));
  }
};

const POPPINS = "'Poppins', 'Helvetica Neue', sans-serif";

// Timeline (frames @30fps)
const HOOK_END = 100; // 0.0–3.3s  hook fila
const SPLIT_END = 215; // 3.3–7.2s  split screen
const PHONE_END = 320; // 7.2–10.7s beneficio celular
// 320–450 CTA

// ------------------------------------------------------------
// Escena 1 — HOOK: la fila, fría y gris
// ------------------------------------------------------------
const HookScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const zoom = interpolate(frame, [0, HOOK_END], [1.12, 1.22]);
  const lineIn = spring({fps, frame, config: {damping: 16, stiffness: 130}});
  const pasoIn = spring({fps, frame: frame - 32, config: {damping: 11, stiffness: 200}});
  const out = interpolate(frame, [HOOK_END - 12, HOOK_END], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{backgroundColor: "#1c1a26", opacity: out}}>
      <Img
        src={staticFile("assets/abakos/fila.png")}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          objectPosition: "70% 40%",
          transform: `scale(${zoom})`,
          filter: "grayscale(0.75) brightness(0.62) contrast(1.05)",
        }}
      />
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(28,26,38,0.25) 0%, rgba(28,26,38,0.05) 45%, rgba(28,26,38,0.72) 100%)",
        }}
      />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          padding: "0 90px",
          gap: 34,
        }}
      >
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 700,
            fontSize: 88,
            lineHeight: 1.12,
            color: "#FFFFFF",
            textAlign: "center",
            opacity: lineIn,
            transform: `translateY(${interpolate(lineIn, [0, 1], [46, 0])}px)`,
            textShadow: "0 6px 30px rgba(0,0,0,0.55)",
          }}
        >
          ¿Filas y papeleos?
        </div>
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 800,
            fontSize: 132,
            color: "#FFFFFF",
            backgroundColor: ABAKOS.magenta,
            padding: "6px 56px 14px",
            borderRadius: 28,
            transform: `scale(${interpolate(pasoIn, [0, 1], [2.4, 1])}) rotate(${interpolate(
              pasoIn,
              [0, 1],
              [10, -3],
            )}deg)`,
            opacity: pasoIn,
          }}
        >
          Paso.
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------
// Escena 2 — SPLIT SCREEN: fila (arriba) vs celular en casa (abajo)
// ------------------------------------------------------------
const SplitScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const dur = SPLIT_END - HOOK_END;

  const topIn = spring({fps, frame, config: {damping: 15, stiffness: 110}});
  const bottomIn = spring({fps, frame: frame - 8, config: {damping: 15, stiffness: 110}});
  const cardIn = spring({fps, frame: frame - 26, config: {damping: 13, stiffness: 140}});
  const drift = interpolate(frame, [0, dur], [1.08, 1.16]);
  const out = interpolate(frame, [dur - 12, dur], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{backgroundColor: ABAKOS.purple, opacity: out}}>
      {/* Mitad superior: la fila (fría) */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          right: 0,
          height: "50%",
          overflow: "hidden",
          transform: `translateY(${interpolate(topIn, [0, 1], [-100, 0])}%)`,
        }}
      >
        <Img
          src={staticFile("assets/abakos/fila.png")}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
            objectPosition: "72% 35%",
            transform: `scale(${drift})`,
            filter: "grayscale(0.7) brightness(0.72)",
          }}
        />
      </div>
      {/* Mitad inferior: en casa con el celular (cálida) */}
      <div
        style={{
          position: "absolute",
          bottom: 0,
          left: 0,
          right: 0,
          height: "50%",
          overflow: "hidden",
          transform: `translateY(${interpolate(bottomIn, [0, 1], [100, 0])}%)`,
        }}
      >
        <Img
          src={staticFile("assets/abakos/celular.png")}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
            objectPosition: "50% 30%",
            transform: `scale(${drift})`,
            filter: "saturate(1.08) brightness(1.03)",
          }}
        />
      </div>
      {/* Divisor de marca */}
      <div
        style={{
          position: "absolute",
          top: "calc(50% - 5px)",
          left: 0,
          right: 0,
          height: 10,
          background: `linear-gradient(90deg, ${ABAKOS.magenta}, ${ABAKOS.orange}, ${ABAKOS.yellow})`,
          transform: `scaleX(${Math.min(topIn, bottomIn)})`,
        }}
      />
      {/* Tarjeta central con el mensaje */}
      <AbsoluteFill style={{justifyContent: "center", alignItems: "center"}}>
        <div
          style={{
            backgroundColor: ABAKOS.paper,
            borderRadius: 36,
            padding: "52px 64px",
            maxWidth: 830,
            textAlign: "center",
            transform: `scale(${interpolate(cardIn, [0, 1], [0.7, 1])})`,
            opacity: cardIn,
            boxShadow: "0 24px 80px rgba(20,10,60,0.45)",
          }}
        >
          <div
            style={{
              fontFamily: POPPINS,
              fontWeight: 700,
              fontSize: 62,
              lineHeight: 1.18,
              color: ABAKOS.purple,
            }}
          >
            Solicita tu préstamo{" "}
            <span style={{color: ABAKOS.magenta}}>Abakos</span> 100% online.
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------
// Escena 3 — BENEFICIO: desde tu celular, en pocos minutos
// ------------------------------------------------------------
const PILLS = ["100% online", "Desde tu celular", "En pocos minutos"];

const PhoneScene: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const dur = PHONE_END - SPLIT_END;

  const zoom = interpolate(frame, [0, dur], [1.04, 1.1]);
  const textIn = spring({fps, frame: frame - 6, config: {damping: 14, stiffness: 120}});
  const out = interpolate(frame, [dur - 12, dur], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{backgroundColor: "#241d3d", opacity: out}}>
      {/* Clip con movimiento real (image-to-video): ella scrollea y sonríe,
          para no repetir la misma foto del split anterior */}
      <OffthreadVideo
        muted
        src={staticFile("assets/abakos/celular-video.mp4")}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          transform: `scale(${zoom})`,
          filter: "saturate(1.08)",
        }}
      />
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(180deg, rgba(36,29,61,0.0) 30%, rgba(36,29,61,0.28) 62%, rgba(36,29,61,0.9) 100%)",
        }}
      />
      <AbsoluteFill
        style={{
          justifyContent: "flex-end",
          alignItems: "center",
          paddingBottom: 210,
          flexDirection: "column",
          gap: 44,
        }}
      >
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 700,
            fontSize: 72,
            lineHeight: 1.16,
            color: "#FFFFFF",
            textAlign: "center",
            padding: "0 100px",
            opacity: textIn,
            transform: `translateY(${interpolate(textIn, [0, 1], [50, 0])}px)`,
            textShadow: "0 6px 30px rgba(0,0,0,0.5)",
          }}
        >
          Desde tu celular y en pocos minutos.
        </div>
        <div style={{display: "flex", gap: 22, flexWrap: "wrap", justifyContent: "center"}}>
          {PILLS.map((pill, i) => {
            const p = spring({fps, frame: frame - 24 - i * 9, config: {damping: 12, stiffness: 170}});
            const bg = [ABAKOS.magenta, ABAKOS.orange, ABAKOS.yellow][i];
            return (
              <div
                key={pill}
                style={{
                  fontFamily: POPPINS,
                  fontWeight: 600,
                  fontSize: 38,
                  color: i === 2 ? ABAKOS.ink : "#FFFFFF",
                  backgroundColor: bg,
                  padding: "16px 38px",
                  borderRadius: 999,
                  opacity: p,
                  transform: `translateY(${interpolate(p, [0, 1], [40, 0])}px) scale(${interpolate(
                    p,
                    [0, 1],
                    [0.8, 1],
                  )})`,
                }}
              >
                {pill}
              </div>
            );
          })}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------
// Escena 4 — CTA final con logo oficial
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
      {/* Panel blanco que sube — estilo flat de la marca */}
      <AbsoluteFill
        style={{
          backgroundColor: ABAKOS.cream,
          transform: `translateY(${interpolate(wash, [0, 1], [100, 0])}%)`,
          borderRadius: interpolate(wash, [0, 1], [120, 0]),
        }}
      />
      {/* Puntos de marca */}
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
          Ingresa a <span style={{fontWeight: 800, color: ABAKOS.purple}}>abakos.cl</span>
          <br />
          y realiza tu solicitud.
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
// Música: "Sounds Good" (Mixkit, licencia libre para uso comercial)
const MusicTrack: React.FC = () => {
  const frame = useCurrentFrame();
  const volume = interpolate(
    frame,
    [0, 12, ABAKOS_REEL_DURATION - 50, ABAKOS_REEL_DURATION - 4],
    [0, 0.85, 0.85, 0],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp"},
  );
  return <Audio src={staticFile("assets/abakos/musica-reel1.mp3")} volume={volume} />;
};

export const AbakosReelSeptiembre: React.FC = () => {
  ensureAbakosFonts();
  return (
    <AbsoluteFill style={{backgroundColor: ABAKOS.purple}}>
      <MusicTrack />
      <Sequence from={0} durationInFrames={HOOK_END}>
        <HookScene />
      </Sequence>
      <Sequence from={HOOK_END} durationInFrames={SPLIT_END - HOOK_END}>
        <SplitScene />
      </Sequence>
      <Sequence from={SPLIT_END} durationInFrames={PHONE_END - SPLIT_END}>
        <PhoneScene />
      </Sequence>
      <Sequence from={PHONE_END}>
        <CtaScene />
      </Sequence>
    </AbsoluteFill>
  );
};
