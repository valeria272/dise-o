// ============================================================================
// G.CL — CIERRE DE SERIE (el del CAP.01, parametrizado)
// Loader de puntos → «tagline» → logo Grupo CopyLab → PRÓXIMO CAPÍTULO a máquina.
// Sacado tal cual de GclOrigenReel.tsx (CierreMarca) el 25-09-2026; sólo cambian
// la frase y el título del próximo capítulo. Dura ~`TW0 + largo título × 2,64 + 20` f.
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame} from "remotion";

const PINK = "#FF4D8D";
const CORAL = "#FF7A59";

let injected = false;
const injectFonts = () => {
  if (injected || typeof document === "undefined") return;
  injected = true;
  const style = document.createElement("style");
  style.textContent = `
    @font-face{font-family:'Syne';src:url(${staticFile("assets/fonts/Syne.ttf")}) format('truetype');font-weight:100 900;font-display:block;}
    @font-face{font-family:'Montserrat';src:url(${staticFile("assets/fonts/Montserrat.ttf")}) format('truetype');font-weight:100 900;font-display:block;}
    @font-face{font-family:'CourierPrime';src:url(${staticFile("assets/fonts/CourierPrimeBold.ttf")}) format('truetype');font-weight:700;font-display:block;}
  `;
  document.head.appendChild(style);
  document.fonts?.load("800 100px Syne").catch(() => {});
  document.fonts?.load("700 100px Montserrat").catch(() => {});
  document.fonts?.load("700 60px CourierPrime").catch(() => {});
};
injectFonts();

const DISPLAY = "'Syne', 'Montserrat', sans-serif";
const MONO = "'Montserrat', monospace";
const MAQUINA = "'CourierPrime', 'Courier New', monospace";
const salida = (t: number) => 1 - Math.pow(1 - t, 3);

export const cierreFrames = (titulo: string, tw0 = 102) => Math.ceil(tw0 + titulo.length * 0.088 * 30 + 24);

const LOGO_W = 1000;
const LOGO_H = 889;
const LOGO_DOT = {x: 0.4156, y: 0.3315, r: 0.0615};

export const CierreSerie: React.FC<{dur: number; tagline: string; titulo: string; tw0?: number}> = ({dur, tagline, titulo, tw0 = 102}) => {
  const frame = useCurrentFrame();
  const dots = [
    {cx: 256, cy: 132, r: 15},
    {cx: 167, cy: 169, r: 18},
    {cx: 130, cy: 258, r: 21},
    {cx: 167, cy: 347, r: 24},
  ];
  const swoosh = interpolate(frame, [17, 27], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const wordmark = interpolate(frame, [29, 37], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const faseA = interpolate(frame, [52, 64], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const logo = interpolate(frame, [66, 84], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const ISO = {size: 420, left: (1080 - 420) / 2, top: 770};
  const isoScale = ISO.size / 512;
  const partida = {
    x: ISO.left + 167 * isoScale,
    y: ISO.top + 347 * isoScale,
    r: 24 * isoScale,
  };
  const LOGO_BOX = {w: 1060, h: (1060 * LOGO_H) / LOGO_W};
  const LOGO_POS = {left: (1080 - 1060) / 2, top: (1920 - LOGO_BOX.h) / 2};
  const llegada = {
    x: LOGO_POS.left + LOGO_DOT.x * LOGO_BOX.w,
    y: LOGO_POS.top + LOGO_DOT.y * LOGO_BOX.h,
    r: LOGO_DOT.r * LOGO_BOX.w,
  };

  const viaje = interpolate(frame, [56, 84], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: salida,
  });
  const puntoX = partida.x + (llegada.x - partida.x) * viaje;
  const puntoY = partida.y + (llegada.y - partida.y) * viaje;
  const puntoR = partida.r + (llegada.r - partida.r) * viaje;
  const puntoVisible = frame >= 56 ? 1 : 0;

  // Colofón de serie. Se escribe a máquina, carácter por carácter, y cada
  // letra cae junto a su clac en la banda sonora: en musica-gcl.py el
  // llamado es maquina(56.90, 14, 0.088) y el cierre entra en el segundo
  // 53,5, así que la primera letra va en el frame 102 de esta secuencia.
  const TW0 = tw0;
  const TW_PASO = 0.088 * 30; // 2,64 frames por carácter
  const TITULO = titulo;
  const letras = Math.max(
    0,
    Math.min(TITULO.length, Math.floor((frame - TW0) / TW_PASO) + 1)
  );
  const rotulo = interpolate(frame, [TW0 - 22, TW0 - 6], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const cursor =
    frame > TW0 - 10 && Math.floor((frame - TW0) / 9) % 2 === 0 ? 1 : 0.15;
  const proximo = interpolate(frame, [dur - 12, dur - 1], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <AbsoluteFill style={{opacity: logo}}>
        <Img
          src={staticFile("assets/gcl/logo_copylab_blanco.png")}
          style={{
            position: "absolute",
            left: LOGO_POS.left,
            top: LOGO_POS.top,
            width: LOGO_BOX.w,
            height: LOGO_BOX.h,
          }}
        />
      </AbsoluteFill>
      {frame >= 50 ? (
        <div
          style={{
            position: "absolute",
            left: llegada.x - llegada.r - 2,
            top: llegada.y - llegada.r - 2,
            width: (llegada.r + 2) * 2,
            height: (llegada.r + 2) * 2,
            borderRadius: "50%",
            backgroundColor: "#000",
          }}
        />
      ) : null}

      <div
        style={{
          position: "absolute",
          left: puntoX - puntoR,
          top: puntoY - puntoR,
          width: puntoR * 2,
          height: puntoR * 2,
          borderRadius: "50%",
          background: `linear-gradient(135deg, ${CORAL}, ${PINK})`,
          opacity: puntoVisible,
          boxShadow: `0 0 ${28 * (1 - viaje)}px rgba(255,77,141,${
            0.8 * (1 - viaje)
          })`,
        }}
      />
      <div
        style={{
          position: "absolute",
          left: puntoX - puntoR,
          top: puntoY - puntoR,
          width: puntoR * 2,
          height: puntoR * 2,
          borderRadius: "50%",
          backgroundColor: "#fff",
          opacity:
            puntoVisible *
            interpolate(frame, [72, 86], [0, 1], {
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
            }),
        }}
      />

      <AbsoluteFill style={{opacity: faseA}}>
        <svg
          width={ISO.size}
          height={ISO.size}
          viewBox="0 0 512 512"
          style={{position: "absolute", left: ISO.left, top: ISO.top}}
        >
          <defs>
            <linearGradient id="gclgrad" x1="0" y1="1" x2="1" y2="0">
              <stop offset="0" stopColor={CORAL} />
              <stop offset="1" stopColor={PINK} />
            </linearGradient>
          </defs>
          <g fill="url(#gclgrad)">
            {dots.map((d, i) => {
              const o = interpolate(frame, [3 + i * 3, 9 + i * 3], [0, 1], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              });
              if (i === 3 && frame >= 55) return null;
              return <circle key={i} cx={d.cx} cy={d.cy} r={d.r * o} opacity={o} />;
            })}
            <g
              opacity={swoosh}
              style={{
                transformOrigin: "190px 380px",
                transform: `scale(${swoosh})`,
              }}
            >
              <path d="M 190 380 C 248 428, 330 414, 376 330 C 392 300, 399 264, 396 226 C 386 280, 356 336, 300 362 C 262 379, 222 376, 190 380 Z" />
            </g>
          </g>
        </svg>
        <div
          style={{
            position: "absolute",
            left: 0,
            right: 0,
            top: 1258,
            opacity: wordmark,
            textAlign: "center",
            fontFamily: DISPLAY,
            fontWeight: 800,
            fontSize: tagline.length > 24 ? 56 : 62,
            lineHeight: 1.12,
            whiteSpace: "pre-line",
            padding: "0 90px",
            letterSpacing: "-0.02em",
            color: "#fff",
          }}
        >
          {tagline}
        </div>
      </AbsoluteFill>

      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 1330,
          textAlign: "center",
          opacity: proximo,
        }}
      >
        <div
          style={{
            fontFamily: MONO,
            fontWeight: 700,
            fontSize: 19,
            letterSpacing: "0.26em",
            color: "rgba(255,255,255,.5)",
            opacity: rotulo,
          }}
        >
          PRÓXIMO CAPÍTULO
        </div>
        <div
          style={{
            fontFamily: MAQUINA,
            fontWeight: 700,
            fontSize: 46,
            letterSpacing: "0.02em",
            color: PINK,
            marginTop: 16,
            whiteSpace: "pre",
          }}
        >
          {TITULO.slice(0, letras)}
          <span style={{opacity: cursor, color: "rgba(255,255,255,.85)"}}>_</span>
        </div>
      </div>
    </AbsoluteFill>
  );
};

