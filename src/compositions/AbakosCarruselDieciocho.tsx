import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

// ============================================================
// ABAKOS — VIDEO 3 · Carrusel 1:1 "DESPUÉS DEL 18, ORDENA PRIMERO"
// 6 láminas estáticas 1080×1080 (stills)
// v2 — feedback Valeria: logo REAL en todas las láminas (nunca
// recrear el wordmark), cero textos inventados (solo los del
// brief), portada con billetera vacía y más energía visual.
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
const STEP_COLORS = [ABAKOS.magenta, ABAKOS.orange, ABAKOS.yellow, ABAKOS.purple];

const Dots: React.FC<{active: number}> = ({active}) => (
  <div style={{display: "flex", gap: 14, justifyContent: "center"}}>
    {Array.from({length: 6}, (_, i) => (
      <div
        key={i}
        style={{
          width: i === active ? 44 : 16,
          height: 16,
          borderRadius: 999,
          backgroundColor: i === active ? ABAKOS.magenta : "rgba(67,52,145,0.18)",
        }}
      />
    ))}
  </div>
);

// Fondo con energía: círculo gigante tintado + puntos de marca
const Bg: React.FC<{tint: string}> = ({tint}) => (
  <>
    <div
      style={{
        position: "absolute",
        width: 900,
        height: 900,
        borderRadius: "50%",
        backgroundColor: tint,
        opacity: 0.1,
        right: -300,
        bottom: -280,
      }}
    />
    <div
      style={{
        position: "absolute",
        width: 320,
        height: 320,
        borderRadius: "50%",
        border: `26px solid ${tint}`,
        opacity: 0.12,
        left: -120,
        top: 300,
      }}
    />
    {[ABAKOS.magenta, ABAKOS.orange, ABAKOS.yellow].map((c, i) => (
      <div
        key={c}
        style={{
          position: "absolute",
          width: 22,
          height: 22,
          borderRadius: "50%",
          backgroundColor: c,
          top: 200 + i * 36,
          right: 110 + i * 44,
          opacity: 0.85,
        }}
      />
    ))}
  </>
);

// Marco común: SIEMPRE el logo oficial (vector) arriba
const Frame: React.FC<{children: React.ReactNode; slide: number; tint: string}> = ({
  children,
  slide,
  tint,
}) => {
  ensureAbakosFonts();
  return (
    <AbsoluteFill
      style={{
        backgroundColor: ABAKOS.cream,
        fontFamily: POPPINS,
        padding: 84,
        flexDirection: "column",
        justifyContent: "space-between",
        overflow: "hidden",
      }}
    >
      <Bg tint={tint} />
      <div style={{display: "flex", justifyContent: "flex-start"}}>
        <Img src={staticFile("assets/abakos/logo.svg")} style={{width: 270}} />
      </div>
      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          position: "relative",
        }}
      >
        {children}
      </div>
      <Dots active={slide - 1} />
    </AbsoluteFill>
  );
};

// Lámina de paso, con más onda: tile inclinado + número gigante outline
const StepSlide: React.FC<{n: number; text: React.ReactNode; icon: string}> = ({n, text, icon}) => {
  const color = STEP_COLORS[(n - 2) % STEP_COLORS.length];
  return (
    <Frame slide={n} tint={color}>
      {/* número gigante de fondo */}
      <div
        style={{
          position: "absolute",
          right: -14,
          top: -46,
          fontWeight: 800,
          fontSize: 330,
          lineHeight: 1,
          color: "transparent",
          WebkitTextStroke: `5px ${color}`,
          opacity: 0.35,
        }}
      >
        {String(n - 1).padStart(2, "0")}
      </div>
      <div style={{display: "flex", flexDirection: "column", gap: 52, position: "relative"}}>
        <div
          style={{
            width: 170,
            height: 170,
            borderRadius: 48,
            backgroundColor: color,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontSize: 86,
            transform: "rotate(-7deg)",
            boxShadow: `0 22px 50px ${color}55`,
          }}
        >
          {icon}
        </div>
        <div style={{fontWeight: 800, fontSize: 76, lineHeight: 1.2, color: ABAKOS.ink, maxWidth: 880}}>
          {text}
        </div>
        <div
          style={{
            height: 14,
            width: 300,
            borderRadius: 999,
            background: `linear-gradient(90deg, ${ABAKOS.magenta}, ${ABAKOS.orange}, ${ABAKOS.yellow})`,
          }}
        />
      </div>
    </Frame>
  );
};

export const AbakosCarruselDieciocho: React.FC<{slide: number}> = ({slide}) => {
  ensureAbakosFonts();

  // Lámina 1 — portada: billetera vacía después del 18
  if (slide === 1) {
    return (
      <Frame slide={1} tint={ABAKOS.magenta}>
        <div style={{display: "flex", flexDirection: "column", gap: 48, alignItems: "center"}}>
          <div style={{position: "relative"}}>
            <div
              style={{
                width: 600,
                height: 400,
                borderRadius: 42,
                overflow: "hidden",
                transform: "rotate(-3deg)",
                boxShadow: "0 34px 80px rgba(30,15,80,0.3)",
                border: "12px solid #FFFFFF",
              }}
            >
              <Img
                src={staticFile("assets/abakos/billetera.png")}
                style={{width: "100%", height: "100%", objectFit: "cover", objectPosition: "50% 40%"}}
              />
            </div>
            {/* guiño al 18 (visual, sin texto inventado) */}
            <div
              style={{
                position: "absolute",
                right: -34,
                top: -34,
                width: 108,
                height: 108,
                borderRadius: "50%",
                backgroundColor: ABAKOS.yellow,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: 54,
                transform: "rotate(8deg)",
                boxShadow: "0 14px 34px rgba(30,15,80,0.25)",
              }}
            >
              🇨🇱
            </div>
          </div>
          <div
            style={{
              fontWeight: 800,
              fontSize: 68,
              lineHeight: 1.2,
              color: ABAKOS.ink,
              textAlign: "center",
              padding: "0 20px",
            }}
          >
            ¿El 18 dejó tus cuentas{" "}
            <span style={{color: ABAKOS.magenta}}>más apretadas de lo esperado?</span>
          </div>
        </div>
      </Frame>
    );
  }

  if (slide === 2) return <StepSlide n={2} icon="💰" text={<>Revisa cuánto dinero tienes disponible.</>} />;

  if (slide === 3)
    return (
      <StepSlide
        n={3}
        icon="📅"
        text={
          <>
            Prioriza servicios básicos y pagos con{" "}
            <span style={{color: ABAKOS.orange}}>fecha de vencimiento cercana.</span>
          </>
        }
      />
    );

  if (slide === 4)
    return (
      <StepSlide
        n={4}
        icon="🎯"
        text={
          <>
            Define el monto mínimo que{" "}
            <span style={{color: ABAKOS.magenta}}>realmente necesitas resolver.</span>
          </>
        }
      />
    );

  if (slide === 5)
    return (
      <StepSlide
        n={5}
        icon="🧮"
        text={
          <>
            Simula el costo completo{" "}
            <span style={{color: ABAKOS.purple}}>antes de solicitar financiamiento.</span>
          </>
        }
      />
    );

  // Lámina 6 — cierre + CTA exacto del brief, con el logo OFICIAL
  return (
    <Frame slide={6} tint={ABAKOS.purple}>
      <div style={{display: "flex", flexDirection: "column", gap: 64, alignItems: "center"}}>
        <div
          style={{
            fontWeight: 800,
            fontSize: 62,
            lineHeight: 1.3,
            color: ABAKOS.ink,
            textAlign: "center",
            whiteSpace: "nowrap",
          }}
        >
          No se trata de pedir más.
          <br />
          Se trata de <span style={{color: ABAKOS.magenta}}>pedir mejor.</span>
        </div>
        <div
          style={{
            fontFamily: POPPINS,
            fontWeight: 700,
            fontSize: 38,
            color: "#FFFFFF",
            backgroundColor: ABAKOS.magenta,
            padding: "26px 48px",
            borderRadius: 999,
            textAlign: "center",
            whiteSpace: "nowrap",
            boxShadow: "0 20px 50px rgba(238,0,168,0.35)",
          }}
        >
          Conoce las condiciones en abakos.cl
        </div>
      </div>
    </Frame>
  );
};
