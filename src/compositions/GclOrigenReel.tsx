import React from "react";
import {
  AbsoluteFill,
  Img,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {Audio, Video} from "@remotion/media";

/**
 * G.CL — Temporada 1, Capítulo 01: «Cómo llegó G.CL»
 *
 * Versión 3 (19-08-2026). Se rehízo la post entera con el feedback:
 * «la post producción sigue plana · la música baja y sube de la nada · el
 *  destello rosado está pegado con chicle · falta presentarlo mejor».
 *
 * Qué cambió respecto de la v2:
 *  · REJILLA. Todo el corte está sobre 120 BPM (compás de 2 s = 60 frames).
 *    Los cortes caen en tiempo fuerte y la música está escrita a la misma
 *    rejilla, así que imagen y sonido golpean juntos. Es lo que separa un
 *    montaje "plano" de uno que respira.
 *  · GRADACIÓN por plano (contraste, saturación, sombras frías / luces
 *    coral) en vez de una sola veladura para todo.
 *  · FLORACIÓN (bloom) real sobre los planos del personaje: es lo que integra
 *    un render CGI con el resto y le quita el aire de "pegado encima".
 *  · CÁMARA VIVA: ningún plano queda quieto, todos tienen deriva.
 *  · LA LLEGADA ya no es un destello rosado superpuesto. La luz NACE en el
 *    visor y se expande; el cuadro entero sube de exposición y vuelve. Está
 *    motivada por lo que pasa en la imagen.
 *  · FICHA DE PERSONAJE en el vacío: nombre, unidad, altura, función. Era lo
 *    que faltaba para presentarlo.
 *  · HUD recurrente = su punto de vista. Aparece cuando él lee, y se APAGA en
 *    el acto final, cuando deciden las personas. Es el hilo del relato.
 */

export const GCL_ORIGEN_FPS = 30;
export const GCL_ORIGEN_DURATION = 1800; // 60 s

const PINK = "#FF4D8D";
const CORAL = "#FF7A59";

// Fuentes auto-hospedadas — sin delayRender (ver memoria reel-video-gotchas)
let injected = false;
const injectFonts = () => {
  if (injected || typeof document === "undefined") return;
  injected = true;
  const style = document.createElement("style");
  style.textContent = `
    @font-face{font-family:'Syne';src:url(${staticFile(
      "assets/fonts/Syne.ttf"
    )}) format('truetype');font-weight:100 900;font-display:block;}
    @font-face{font-family:'Montserrat';src:url(${staticFile(
      "assets/fonts/Montserrat.ttf"
    )}) format('truetype');font-weight:100 900;font-display:block;}
    @font-face{font-family:'CourierPrime';src:url(${staticFile(
      "assets/fonts/CourierPrimeBold.ttf"
    )}) format('truetype');font-weight:700;font-display:block;}
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

/* ==========================================================================
   1. IMAGEN — gradación, floración, deriva
   ========================================================================== */

type Look = {
  con?: number; // contraste
  sat?: number;
  bri?: number;
  sombra?: string; // tinte de sombras (multiply)
  luz?: string; // tinte de luces (screen)
  luzOp?: number;
};

/**
 * Gradación por plano. Un multiply tenue tiñe las sombras y un screen tenue
 * tiñe las luces: es un split-tone, lo mismo que se hace en una sala de color.
 */
const Grade: React.FC<{look?: Look; children: React.ReactNode}> = ({
  look = {},
  children,
}) => {
  const {
    con = 1.1,
    sat = 1.05,
    bri = 1,
    sombra = "rgba(120,150,215,1)",
    luz = "rgba(255,122,89,1)",
    luzOp = 0.13,
  } = look;
  return (
    <AbsoluteFill
      style={{
        filter: `contrast(${con}) saturate(${sat}) brightness(${bri})`,
        backgroundColor: "#000",
      }}
    >
      {children}
      <AbsoluteFill
        style={{mixBlendMode: "multiply", background: sombra, opacity: 0.1}}
      />
      <AbsoluteFill
        style={{mixBlendMode: "screen", background: luz, opacity: luzOp}}
      />
    </AbsoluteFill>
  );
};

/**
 * Floración. Toma lo que hay detrás, lo desenfoca, lo sube de brillo y lo
 * vuelve a componer en «screen». Es lo que hace que la luz del visor derrame
 * sobre el aire y el personaje deje de verse recortado.
 */
const Bloom: React.FC<{radio?: number; fuerza?: number; brillo?: number}> = ({
  radio = 26,
  fuerza = 0.34,
  brillo = 1.5,
}) => (
  <AbsoluteFill
    style={{
      backdropFilter: `blur(${radio}px) brightness(${brillo}) saturate(1.6)`,
      WebkitBackdropFilter: `blur(${radio}px) brightness(${brillo}) saturate(1.6)`,
      mixBlendMode: "screen",
      opacity: fuerza,
      pointerEvents: "none",
    }}
  />
);

/** Deriva de cámara: ningún plano queda quieto. */
const Deriva: React.FC<{
  dur: number;
  de?: number;
  a?: number;
  dx?: number;
  dy?: number;
  children: React.ReactNode;
}> = ({dur, de = 1.02, a = 1.09, dx = 0, dy = 0, children}) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [0, dur], [0, 1], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill
      style={{
        transform: `scale(${de + (a - de) * p}) translate(${dx * p}px, ${
          dy * p
        }px)`,
      }}
    >
      {children}
    </AbsoluteFill>
  );
};

/**
 * Entrada de plano tipo latigazo: 4 frames de desenfoque direccional y empuje.
 * Reemplaza a los destellos superpuestos — el corte se siente como movimiento
 * de cámara, no como un efecto pegado encima.
 */
const Latigazo: React.FC<{fuerza?: number; children: React.ReactNode}> = ({
  fuerza = 1,
  children,
}) => {
  const frame = useCurrentFrame();
  const p = Math.max(0, 1 - frame / 5);
  return (
    <AbsoluteFill
      style={{
        filter: `blur(${14 * fuerza * p * p}px)`,
        transform: `scale(${1 + 0.05 * fuerza * p})`,
      }}
    >
      {children}
    </AbsoluteFill>
  );
};

const Vineta: React.FC<{fuerza?: number}> = ({fuerza = 0.62}) => {
  const frame = useCurrentFrame();
  const r = 74 + 3 * Math.sin(frame / 44); // la viñeta respira
  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse ${r}% ${
          r - 14
        }% at 50% 45%, transparent 38%, rgba(0,0,0,${fuerza}) 100%)`,
      }}
    />
  );
};

/**
 * LA LLEGADA. La luz nace en el visor (punto), se expande y el cuadro entero
 * sube de exposición medio segundo. Nada de un rectángulo rosado encima.
 */
const LuzNaciente: React.FC<{cx: number; cy: number; fuerza?: number}> = ({
  cx,
  cy,
  fuerza = 1,
}) => {
  const frame = useCurrentFrame();
  const r = interpolate(frame, [0, 4, 22], [0, 26, 190], {
    extrapolateRight: "clamp",
    easing: salida,
  });
  // decae rápido a propósito: el lavado tiene que durar lo justo para que el
  // corte golpee, y despejar antes de que el ojo pierda la G.
  const o =
    fuerza *
    interpolate(frame, [0, 3, 8, 24], [0, 0.95, 0.46, 0], {
      extrapolateRight: "clamp",
    });
  const exp =
    fuerza *
    interpolate(frame, [0, 4, 12, 32], [0, 0.24, 0.09, 0], {
      extrapolateRight: "clamp",
    });
  return (
    <AbsoluteFill style={{pointerEvents: "none"}}>
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse ${r}% ${r * 0.62}% at ${
            cx * 100
          }% ${cy * 100}%, #ffffff 0%, ${PINK} 26%, rgba(255,122,89,.55) 52%, transparent 76%)`,
          opacity: o,
          mixBlendMode: "screen",
        }}
      />
      <AbsoluteFill
        style={{background: "#fff", opacity: exp, mixBlendMode: "screen"}}
      />
    </AbsoluteFill>
  );
};

/**
 * El LED dormido del casco. El clip del visor viene con la G YA encendida — el
 * encendido no existe dentro del material. Así que el encendido ES EL CORTE, y
 * este latido es la carga: el punto rosado parpadea dos veces y después crece
 * hasta que el cuadro no aguanta más y corta.
 */
const Latido: React.FC<{dur: number; cx: number; cy: number}> = ({dur, cx, cy}) => {
  const frame = useCurrentFrame();
  const parpadeo = (at: number, alto: number) =>
    interpolate(frame, [at, at + 2, at + 9], [0, alto, 0], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });
  const carga = interpolate(frame, [dur - 52, dur], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: (t) => Math.pow(t, 2.1),
  });
  const o = Math.max(parpadeo(dur - 88, 0.5), parpadeo(dur - 66, 0.72), carga);
  const r = 5 + 20 * carga + 4 * Math.max(parpadeo(dur - 88, 1), parpadeo(dur - 66, 1));
  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse ${r}% ${r * 0.7}% at ${cx * 100}% ${
          cy * 100
        }%, ${PINK} 0%, rgba(255,122,89,.42) 42%, transparent 74%)`,
        opacity: o * 0.85,
        mixBlendMode: "screen",
        pointerEvents: "none",
      }}
    />
  );
};

/**
 * El guiño. G.CL no tiene cara: su expresión es la G del visor. Para que
 * guiñe, se tapa la G con un óvalo del color exacto del visor (medido sobre el
 * render: rgb(61,12,33)) y en su lugar aparece una raya rosada — el ojo
 * cerrado del dot-matrix. Después vuelve.
 */
const Guino: React.FC<{
  cx: number;
  cy: number;
  w: number;
  h: number;
  dur: number;
  escIni?: number;
  escFin?: number;
}> = ({cx: cx0, cy: cy0, w: w0, h: h0, dur, escIni = 1, escFin = 1}) => {
  const frame = useCurrentFrame();
  // El plano se acerca (ver Emerge), así que la G se mueve y crece: la máscara
  // tiene que seguirla o la raya queda descentrada. Se reconstruye la misma
  // transformación de escala centrada en el cuadro.
  const e = interpolate(frame, [0, dur], [escIni, escFin], {
    extrapolateRight: "clamp",
  });
  const cx = 540 + (cx0 - 540) * e;
  const cy = 960 + (cy0 - 960) * e;
  const w = w0 * e;
  const h = h0 * e;
  // dos parpadeos: uno corto y otro más largo. Con uno solo de 20 frames
  // pasaba desapercibido.
  const cierra = Math.max(
    interpolate(frame, [0, 4, 9, 14], [0, 1, 1, 0], {extrapolateRight: "clamp"}),
    interpolate(frame, [20, 25, 38, 45], [0, 1, 1, 0], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );
  const raya = Math.max(
    interpolate(frame, [3, 6, 9, 12], [0, 1, 1, 0], {extrapolateRight: "clamp"}),
    interpolate(frame, [24, 28, 37, 42], [0, 1, 1, 0], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );
  return (
    <AbsoluteFill style={{pointerEvents: "none"}}>
      <div
        style={{
          position: "absolute",
          left: cx - (w * 1.3) / 2,
          top: cy - (h * 1.35) / 2,
          width: w * 1.3,
          height: h * 1.35,
          borderRadius: "50%",
          background: "rgb(61,12,33)",
          filter: "blur(13px)",
          opacity: cierra,
        }}
      />
      <div
        style={{
          position: "absolute",
          left: cx - (w * 0.62) / 2,
          top: cy - 7,
          width: w * 0.62,
          height: 14,
          borderRadius: 7,
          background: PINK,
          boxShadow: `0 0 26px ${PINK}`,
          opacity: raya,
        }}
      />
    </AbsoluteFill>
  );
};

/**
 * Sale de la oscuridad y avanza hacia la cámara. El material no tiene un plano
 * de él caminando, así que el avance se hace con la lente: la luz sube desde
 * casi negro y el plano se acerca un 30% a lo largo de la escena.
 */
const Emerge: React.FC<{dur: number; children: React.ReactNode}> = ({
  dur,
  children,
}) => {
  const frame = useCurrentFrame();
  const luz = interpolate(frame, [0, 34, 78], [0.12, 0.55, 1], {
    extrapolateRight: "clamp",
    easing: salida,
  });
  const esc = interpolate(frame, [0, dur], [1.0, 1.3], {
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#000",
        filter: `brightness(${luz})`,
        transform: `scale(${esc})`,
      }}
    >
      {children}
    </AbsoluteFill>
  );
};

/**
 * Modo detectando. En el plano del patrón el personaje es una imagen fija y
 * quedaba tieso. Acá se le tapan las dos «X» del visor con el color del propio
 * visor (medido: rgb(42,13,14)) y en su lugar aparecen dos anillos que se
 * contraen como un iris enfocando, más un barrido que recorre el casco.
 * Se lee como que está analizando algo, no como una foto quieta.
 *
 * Las coordenadas se pasan a escala 1 y el componente aplica la escala del
 * Ken Burns del `Still`, igual que el guiño.
 */
const Detectando: React.FC<{
  dur: number;
  ojos: [number, number][];
  tam: number;
  escIni: number;
  escFin: number;
  /** frames que lleva corriendo el <Still> cuando arranca esta secuencia */
  desfase: number;
  /** el mismo `vaiven` del <Still>, para seguir el movimiento */
  vaiven: number;
}> = ({dur, ojos, tam, escIni, escFin, desfase, vaiven}) => {
  const frame = useCurrentFrame();
  const e = interpolate(frame, [0, dur], [escIni, escFin], {
    extrapolateRight: "clamp",
  });
  // Se reconstruye el vaivén del Still con SU contador de frames. El Still
  // aplica `scale(e) translate(dx,dy)`, así que en pantalla el corrimiento es
  // dx*e. Sin esto la máscara se despega de los ojos a medida que el plano se
  // mueve.
  const fs = frame + desfase;
  const ddx = vaiven * (Math.sin(fs / 31) + 0.4 * Math.sin(fs / 13.5)) * e;
  const ddy = vaiven * Math.sin(fs / 24 + 1.7) * 0.7 * e;
  const tapa = interpolate(frame, [0, 10], [0, 1], {
    extrapolateRight: "clamp",
    easing: salida,
  });
  const salir = interpolate(frame, [dur - 12, dur], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  // el iris enfoca: se contrae, se suelta, se contrae más
  const foco = interpolate(
    frame,
    [8, 22, 34, 48, 60, dur],
    [1, 0.46, 0.72, 0.34, 0.42, 0.4],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: salida}
  );
  const aparece = interpolate(frame, [8, 18], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const pulso = 0.86 + 0.14 * Math.sin(frame / 4.5);
  const barrido = ((frame % 46) / 46) * 100;
  return (
    <AbsoluteFill style={{pointerEvents: "none", opacity: salir}}>
      {ojos.map(([ox, oy], i) => {
        const cx = 540 + (ox - 540) * e + ddx;
        const cy = 960 + (oy - 960) * e + ddy;
        const t = tam * e;
        const r = t * 0.42 * foco * pulso;
        return (
          <React.Fragment key={i}>
            {/* tapa la X con el color del visor */}
            <div
              style={{
                position: "absolute",
                left: cx - t * 0.72,
                top: cy - t * 0.72,
                width: t * 1.44,
                height: t * 1.44,
                borderRadius: "50%",
                background: "rgb(42,13,14)",
                filter: "blur(16px)",
                opacity: tapa,
              }}
            />
            {/* anillo exterior */}
            <div
              style={{
                position: "absolute",
                left: cx - r,
                top: cy - r,
                width: r * 2,
                height: r * 2,
                borderRadius: "50%",
                border: `${Math.max(3, t * 0.075)}px solid ${PINK}`,
                boxShadow: `0 0 ${26 * aparece}px ${PINK}`,
                opacity: aparece,
              }}
            />
            {/* punto interior */}
            <div
              style={{
                position: "absolute",
                left: cx - r * 0.24,
                top: cy - r * 0.24,
                width: r * 0.48,
                height: r * 0.48,
                borderRadius: "50%",
                background: "#fff",
                opacity: aparece * 0.9,
              }}
            />
          </React.Fragment>
        );
      })}
      {/* barrido dentro del casco */}
      <div
        style={{
          position: "absolute",
          left: 540 + (270 - 540) * e + ddx,
          width: 540 * e,
          top: 960 + (470 - 960) * e + ddy + (340 * e * barrido) / 100,
          height: 2,
          background: `linear-gradient(90deg, transparent, ${CORAL}, transparent)`,
          opacity: aparece * 0.5,
        }}
      />
    </AbsoluteFill>
  );
};

/** Golpe de cámara. */
const Golpe: React.FC<{at: number; fuerza?: number; children: React.ReactNode}> =
  ({at, fuerza = 0.05, children}) => {
    const frame = useCurrentFrame();
    const p = frame < at ? 0 : Math.max(0, 1 - (frame - at) / 14);
    return (
      <AbsoluteFill style={{transform: `scale(${1 + fuerza * p * p})`}}>
        {children}
      </AbsoluteFill>
    );
  };

/** Grano + aberración de bordes. Última capa. */
const PostFX: React.FC = () => {
  const frame = useCurrentFrame();
  const tex = `assets/gcl/grain/g${frame % 8}.png`;
  return (
    <AbsoluteFill style={{pointerEvents: "none"}}>
      <Img
        src={staticFile(tex)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          mixBlendMode: "overlay",
          opacity: 0.07,
        }}
      />
      {/* caída de nitidez y de luz en los bordes: da lente, no pantalla */}
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(ellipse 96% 92% at 50% 50%, transparent 62%, rgba(0,0,0,.30) 100%)",
        }}
      />
    </AbsoluteFill>
  );
};

/* ==========================================================================
   2. TEXTO
   ========================================================================== */

const PlacaInterna: React.FC<{
  children: React.ReactNode;
  dur: number;
  bottom: number;
  size: number;
  align: "left" | "center";
  regla: boolean;
  sube: boolean;
}> = ({children, dur, bottom, size, align, regla, sube}) => {
  const frame = useCurrentFrame();
  // la variante `sube` entra en 26 frames con salida cúbica: un solo
  // movimiento, lento y limpio.
  const ent = interpolate(frame, [0, sube ? 26 : 9], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: salida,
  });
  const sal = interpolate(frame, [dur - 8, dur], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const linea = interpolate(frame, [6, 20], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: salida,
  });
  return (
    <AbsoluteFill
      style={{
        justifyContent: "flex-end",
        alignItems: align === "center" ? "center" : "flex-start",
        padding: `0 90px ${bottom}px 90px`,
      }}
    >
      <div style={{opacity: 1 - sal}}>
        {regla ? (
          <div
            style={{
              height: 4,
              width: 108 * linea,
              background: `linear-gradient(90deg, ${CORAL}, ${PINK})`,
              marginBottom: 26,
              marginLeft: align === "center" ? "auto" : 0,
              marginRight: align === "center" ? "auto" : 0,
              borderRadius: 2,
            }}
          />
        ) : null}
        <div
          style={{
            fontFamily: DISPLAY,
            fontWeight: 800,
            fontSize: size,
            lineHeight: 1.06,
            // OJO: acá había una animación de interletrado (0,14em -> -0,025em).
            // Con el texto centrado eso hacía que las líneas se cerraran
            // horizontalmente MIENTRAS el bloque subía y escalaba: se leía como
            // dos animaciones encimadas («tiene un bug, como doble animación»).
            // La entrada `sube` ahora mueve UNA sola cosa: sube y enfoca.
            letterSpacing: "-0.025em",
            color: "#fff",
            textAlign: align,
            textShadow: "0 6px 44px rgba(0,0,0,.8)",
            maxWidth: 900,
            filter: `blur(${(1 - ent) * (sube ? 16 : 9)}px)`,
            clipPath: sube
              ? undefined
              : `inset(-30% ${(1 - ent) * 102}% -30% 0)`,
            opacity: sube ? ent : 1,
            transform: sube
              ? `translateY(${(1 - ent) * 44 - sal * 16}px)`
              : `translateY(${(1 - ent) * 20 - sal * 14}px)`,
          }}
        >
          {children}
        </div>
      </div>
    </AbsoluteFill>
  );
};

const Placa: React.FC<{
  children: React.ReactNode;
  at: number;
  dur: number;
  bottom?: number;
  size?: number;
  align?: "left" | "center";
  regla?: boolean;
  sube?: boolean;
}> = ({
  children,
  at,
  dur,
  bottom = 300,
  size = 68,
  align = "left",
  regla = true,
  sube = false,
}) => (
  <Sequence from={at} durationInFrames={dur} layout="none">
    <PlacaInterna
      dur={dur}
      bottom={bottom}
      size={size}
      align={align}
      regla={regla}
      sube={sube}
    >
      {children}
    </PlacaInterna>
  </Sequence>
);

const Reloj: React.FC<{children: React.ReactNode; at: number; dur: number}> = ({
  children,
  at,
  dur,
}) => (
  <Sequence from={at} durationInFrames={dur} layout="none">
    <AbsoluteFill style={{padding: "150px 0 0 90px"}}>
      <RelojInterno>{children}</RelojInterno>
    </AbsoluteFill>
  </Sequence>
);

const RelojInterno: React.FC<{children: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 8], [0, 1], {extrapolateRight: "clamp"});
  return (
    <div
      style={{
        fontFamily: MONO,
        fontWeight: 700,
        fontSize: 30,
        letterSpacing: "0.22em",
        color: PINK,
        opacity: o,
        textShadow: "0 4px 24px rgba(0,0,0,.9)",
      }}
    >
      {children}
    </div>
  );
};

const Rotulo: React.FC = () => (
  <AbsoluteFill style={{padding: "96px 0 0 90px"}}>
    <div
      style={{
        fontFamily: MONO,
        fontWeight: 700,
        fontSize: 20,
        letterSpacing: "0.24em",
        color: "rgba(255,255,255,.7)",
        textShadow: "0 2px 18px rgba(0,0,0,.95)",
      }}
    >
      TEMPORADA 1 · CAPÍTULO 01
    </div>
  </AbsoluteFill>
);

/* ==========================================================================
   3. HUD — el punto de vista de G.CL. Es el hilo del relato: aparece cuando
   él está leyendo, y se apaga en el acto final, cuando deciden las personas.
   ========================================================================== */

const Hud: React.FC<{dur: number; etiqueta: string; barrido?: boolean}> = ({
  dur,
  etiqueta,
  barrido = true,
}) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 12, dur - 10, dur], [0, 1, 1, 0], {
    extrapolateRight: "clamp",
  });
  const esq = interpolate(frame, [0, 14], [0, 1], {
    extrapolateRight: "clamp",
    easing: salida,
  });
  const y = ((frame % 90) / 90) * 100;
  // Brazos cortos a propósito: con 88 px la etiqueta de abajo quedaba dentro
  // del tramo vertical del corchete y se leían pegadas (feedback dos veces:
  // «los textos abajo a la derecha topan»).
  const L = 52;
  const G = 8;
  const esquina = (
    lado: React.CSSProperties,
    rot: number
  ): React.CSSProperties => ({
    position: "absolute",
    width: L * esq,
    height: 3,
    background: PINK,
    opacity: 0.85,
    transform: `rotate(${rot}deg)`,
    transformOrigin: "left center",
    ...lado,
  });
  return (
    <AbsoluteFill style={{opacity: o, pointerEvents: "none"}}>
      {/* marco de esquinas */}
      <div style={esquina({left: `${G}%`, top: `${G}%`}, 0)} />
      <div style={esquina({left: `${G}%`, top: `${G}%`}, 90)} />
      <div style={esquina({right: `${G}%`, top: `${G}%`}, 180)} />
      <div style={esquina({right: `${G}%`, top: `${G}%`}, 90)} />
      <div style={esquina({left: `${G}%`, bottom: `${G}%`}, 0)} />
      <div style={esquina({left: `${G}%`, bottom: `${G}%`}, -90)} />
      <div style={esquina({right: `${G}%`, bottom: `${G}%`}, 180)} />
      <div style={esquina({right: `${G}%`, bottom: `${G}%`}, -90)} />
      {/* barrido */}
      {barrido ? (
        <div
          style={{
            position: "absolute",
            left: `${G}%`,
            right: `${G}%`,
            top: `${G + (100 - 2 * G) * (y / 100)}%`,
            height: 2,
            background: `linear-gradient(90deg, transparent, ${PINK}, transparent)`,
            opacity: 0.5,
          }}
        />
      ) : null}
      {/* la etiqueta sube por encima del corchete: antes se topaban
          (feedback: «los textos abajo a la derecha topan») */}
      <div
        style={{
          position: "absolute",
          right: `${G}%`,
          bottom: `${G}%`,
          marginBottom: 104,
          fontFamily: MONO,
          fontWeight: 700,
          fontSize: 19,
          letterSpacing: "0.2em",
          color: PINK,
          textShadow: "0 2px 14px rgba(0,0,0,.9)",
        }}
      >
        {etiqueta}
      </div>
    </AbsoluteFill>
  );
};

/* ==========================================================================
   4. FICHA DE PERSONAJE — la presentación que faltaba
   ========================================================================== */

// Fila: [rótulo, valor, retardo en frames, columna, alto en px].
// Van ARRIBA, en el aire negro sobre el casco: abajo y a los lados cruzaban al
// personaje y la ficha se leía sucia.
// Cabecera de la ficha. Solo la unidad: la entrada («MARTES · 09:12») se sacó
// por pedido — no aportaba y ensuciaba la parte de arriba.
const FICHA_CABEZA: [string, string, "izq" | "der", number][] = [
  ["UNIDAD", "01 · GRUPO COPYLAB", "izq", 0],
];

// Los roles se DESPLIEGAN DESDE EL CUERPO: la línea nace pegada a él y crece
// hacia afuera, y la palabra recién aparece cuando la línea llegó. Antes la
// línea crecía al revés y se leía como una viñeta puesta encima.
const ROLES: [string, "izq" | "der", number, number][] = [
  ["GROWTH", "izq", 690, 20],
  ["DATA", "der", 828, 34],
  ["AUDITOR", "izq", 966, 48],
  ["ESTRATEGA", "der", 1104, 62],
];

const CUERPO_IZQ = 336; // borde del personaje medido en el render
const CUERPO_DER = 744;
const LARGO = 132;

const Ficha: React.FC<{dur: number}> = ({dur}) => {
  const frame = useCurrentFrame();
  const fuera = interpolate(frame, [dur - 14, dur], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const ent = (retardo: number, largo = 12) =>
    interpolate(frame, [retardo, retardo + largo], [0, 1], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
      easing: salida,
    });
  return (
    <AbsoluteFill style={{pointerEvents: "none", opacity: fuera}}>
      {FICHA_CABEZA.map(([k, v, lado, retardo]) => {
        const p = ent(retardo);
        const izq = lado === "izq";
        return (
          <div
            key={k}
            style={{
              position: "absolute",
              top: 196,
              [izq ? "left" : "right"]: 88,
              textAlign: izq ? "left" : "right",
              opacity: p,
              transform: `translateX(${(izq ? -26 : 26) * (1 - p)}px)`,
            }}
          >
            <div
              style={{
                height: 2,
                width: 54 * p,
                background: PINK,
                marginBottom: 10,
                marginLeft: izq ? 0 : "auto",
              }}
            />
            <div
              style={{
                fontFamily: MONO,
                fontWeight: 700,
                fontSize: 16,
                letterSpacing: "0.26em",
                color: "rgba(255,255,255,.58)",
              }}
            >
              {k}
            </div>
            <div
              style={{
                fontFamily: DISPLAY,
                fontWeight: 800,
                fontSize: 27,
                color: "#fff",
                textShadow: "0 4px 28px rgba(0,0,0,.9)",
                marginTop: 4,
              }}
            >
              {v}
            </div>
          </div>
        );
      })}

      {ROLES.map(([palabra, lado, top, retardo]) => {
        const linea = ent(retardo, 10);
        const texto = ent(retardo + 7, 9);
        const izq = lado === "izq";
        const xi = izq ? CUERPO_IZQ : CUERPO_DER;
        return (
          <React.Fragment key={palabra}>
            <div
              style={{
                position: "absolute",
                top: top + 22,
                left: izq ? xi - LARGO * linea : xi,
                width: LARGO * linea,
                height: 2,
                background: `linear-gradient(${izq ? "270deg" : "90deg"}, ${PINK}, rgba(255,77,141,.15))`,
              }}
            />
            <div
              style={{
                position: "absolute",
                top,
                [izq ? "left" : "right"]: 88,
                fontFamily: DISPLAY,
                fontWeight: 800,
                fontSize: 36,
                letterSpacing: "-0.01em",
                color: "#fff",
                textShadow: "0 4px 26px rgba(0,0,0,.95)",
                whiteSpace: "nowrap",
                opacity: texto,
                transform: `translateX(${(izq ? -18 : 18) * (1 - texto)}px)`,
              }}
            >
              {palabra}
            </div>
          </React.Fragment>
        );
      })}
    </AbsoluteFill>
  );
};

/* ==========================================================================
   5. MEDIOS
   ========================================================================== */

/**
 * Still con push in lento MÁS un vaivén de cámara en mano de baja frecuencia.
 * Sin el vaivén el plano se lee como una foto quieta — feedback 20-08: «el
 * agente queda tieso, sin movimiento».
 */
const Still: React.FC<{
  src: string;
  dur: number;
  from?: number;
  to?: number;
  vaiven?: number;
}> = ({src, dur, from = 1.03, to = 1.13, vaiven = 0}) => {
  const frame = useCurrentFrame();
  const scale = interpolate(frame, [0, dur], [from, to], {
    extrapolateRight: "clamp",
  });
  const dx = vaiven * (Math.sin(frame / 31) + 0.4 * Math.sin(frame / 13.5));
  const dy = vaiven * (Math.sin(frame / 24 + 1.7) * 0.7);
  const rot = vaiven * 0.035 * Math.sin(frame / 37);
  return (
    <AbsoluteFill style={{overflow: "hidden", backgroundColor: "#000"}}>
      <Img
        src={staticFile(src)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          transform: `scale(${scale}) translate(${dx}px, ${dy}px) rotate(${rot}deg)`,
        }}
      />
    </AbsoluteFill>
  );
};

/**
 * Duración real de cada clip, en segundos. Se usa para que ningún plano se
 * congele al final.
 *
 * EL ERROR QUE ESTO EVITA (detectado 20-08 por Valeria: «la chica del primer
 * cut se queda pegada al final»): si el plano dura T segundos en el reel y se
 * reproduce a `rate`, consume T*rate segundos de clip. Si eso supera la duración
 * del archivo, Remotion muestra el último frame congelado el resto del plano.
 * Al auditarlo estaban CUATRO clips en esa situación, no uno.
 */
const DUR_CLIP: Record<string, number> = {
  "assets/gcl/s01_oficina_noche.mp4": 5.033,
  "assets/gcl/s03_visor.mp4": 5.033,
  "assets/gcl/s04_archivo.mp4": 5.033,
  "assets/gcl/s07_void.mp4": 5.033,
  "assets/gcl/s09_turno_noche.mp4": 5.033,
  "assets/gcl/s06b_escritorio.mp4": 2.4,
  "assets/gcl/s08b_ella_mira.mp4": 3.3,
  "assets/gcl/s10b_equipo.mp4": 2.4,
};

/**
 * Devuelve el `rate` pedido, o el máximo que cabe en el clip si el pedido se
 * pasa. Deja un 4% de margen para que nunca toque el último frame.
 */
const rateClip = (src: string, frames: number, deseado: number) => {
  const dur = DUR_CLIP[src];
  if (!dur) return deseado;
  const tope = (dur * 0.96) / (frames / GCL_ORIGEN_FPS);
  return Math.min(deseado, Number(tope.toFixed(3)));
};

const Clip: React.FC<{src: string; rate?: number; trimStart?: number}> = ({
  src,
  rate = 1,
  trimStart = 0,
}) => (
  <AbsoluteFill style={{backgroundColor: "#000"}}>
    <Video
      src={staticFile(src)}
      style={{width: "100%", height: "100%", objectFit: "cover"}}
      playbackRate={rate}
      trimBefore={trimStart}
      volume={() => 0}
      muted
    />
  </AbsoluteFill>
);

/* ==========================================================================
   6. CIERRE DE MARCA
   ========================================================================== */

const LOGO_W = 1000;
const LOGO_H = 889;
const LOGO_DOT = {x: 0.4156, y: 0.3315, r: 0.0615};

const CierreMarca: React.FC<{dur: number}> = ({dur}) => {
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
  const TW0 = 102;
  const TW_PASO = 0.088 * 30; // 2,64 frames por carácter
  const TITULO = "Turno de noche";
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
            fontSize: 62,
            letterSpacing: "-0.02em",
            color: "#fff",
          }}
        >
          Es parte del equipo.
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

/* ==========================================================================
   7. MONTAJE — rejilla de 120 BPM: 1 compás = 60 frames
   ========================================================================== */

const LOOK_NOCHE: Look = {
  con: 1.22,
  sat: 0.9,
  bri: 0.94,
  sombra: "rgba(96,132,210,1)",
  luz: "rgba(255,180,140,1)",
  luzOp: 0.08,
};
const LOOK_PERSONAJE: Look = {
  con: 1.2,
  sat: 1.06,
  bri: 1.02,
  sombra: "rgba(84,110,200,1)",   // sombras frías: separan al personaje del fondo
  luz: "rgba(255,196,158,1)",     // luces cálidas, NO rosadas: el rosado ya lo pone él
  luzOp: 0.1,
};
const LOOK_DATOS: Look = {
  con: 1.26,
  sat: 0.94,
  bri: 0.97,
  sombra: "rgba(70,130,225,1)",
  luz: "rgba(255,208,170,1)",
  luzOp: 0.1,
};
const LOOK_OFICINA: Look = {
  con: 1.12,
  sat: 1.06,
  bri: 1.02,
  sombra: "rgba(120,150,215,1)",
  luz: "rgba(255,150,110,1)",
  luzOp: 0.14,
};

export const GclOrigenReel: React.FC = () => {
  injectFonts();
  const {durationInFrames} = useVideoConfig();

  // Rejilla: compás de 60 frames (2 s @ 120 BPM). Todo cae en tiempo fuerte.
  const A = 0; //     0,0 s  acto 1 · la noche
  const B = 300; //  10,0 s  acto 2 · el casco apagado (1 s más para leer la cita)
  // El corte a la G ES el encendido: cae en el frame 420 = 14,0 s, junto al
  // impacto de la música. Antes el plano del visor entraba a los 12 s con la G
  // ya prendida, así que el golpe aterrizaba sobre una imagen que no cambiaba.
  const C = 420; //  14,0 s  LA LLEGADA
  const D = 510; //  17,0 s  acto 3 · lo primero que hizo
  const E = 675; //  22,5 s
  const F = 810; //  27,0 s  acto 4 · la ficha
  const H = 990; //  33,0 s  acto 5 · ahora trabaja acá
  const I = 1140; // 38,0 s
  const J = 1275; // 42,5 s
  const K = 1410; // 47,0 s  acto 6 · la tesis
  const L = 1605; // 53,5 s  cierre de marca

  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Audio src={staticFile("assets/gcl/vo_r01.mp3")} />
      <Audio src={staticFile("assets/gcl/music_r01.mp3")} />

      {/* ---------- ACTO 1 · La noche ---------- */}
      <Sequence from={A} durationInFrames={B - A}>
        <Grade look={LOOK_NOCHE}>
          <Deriva dur={B - A} de={1.02} a={1.1} dx={-16}>
            <Clip
              src="assets/gcl/s01_oficina_noche.mp4"
              rate={rateClip("assets/gcl/s01_oficina_noche.mp4", B - A, 0.55)}
            />
          </Deriva>
        </Grade>
        <Vineta fuerza={0.7} />
      </Sequence>
      <Reloj at={A + 12} dur={120}>
        11:22 PM
      </Reloj>
      {/* la cita se queda 2,8 s en pantalla (antes 1,5): no alcanzaba a leerse */}
      <Placa at={216} dur={84} size={62}>
        «Esto lo debería hacer
        <br />
        una máquina.»
      </Placa>

      {/* ---------- ACTO 2 · El encendido ---------- */}
      <Sequence from={B} durationInFrames={C - B}>
        <Latigazo fuerza={0.7}>
          <Grade look={LOOK_NOCHE}>
            {/* s02b: al original le sobraba un 22% de negro plano abajo y se veía
                el borde recto de la imagen. La mesa se extiende y se apaga. */}
            <Still
              src="assets/gcl/s02b_casco_apagado.png"
              dur={C - B}
              to={1.16}
              vaiven={5}
            />
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.72} />
        {/* el LED dormido late y carga durante los últimos 1,7 s */}
        <Latido dur={C - B} cx={0.5} cy={0.47} />
      </Sequence>
      <Reloj at={B + 10} dur={70}>
        MARTES
      </Reloj>

      {/* LA LLEGADA. El corte cae en el frame 420 = 14,0 s, exactamente sobre el
          impacto de la música. rate 0,675 usa solo los 2 primeros segundos del
          clip: más allá la G parpadea y se apaga sola. */}
      <Sequence from={C} durationInFrames={D - C}>
        <Golpe at={0} fuerza={0.095}>
          <Grade look={LOOK_PERSONAJE}>
            <Clip
              src="assets/gcl/s03_visor.mp4"
              rate={rateClip("assets/gcl/s03_visor.mp4", D - C, 0.675)}
            />
            <Bloom radio={30} fuerza={0.26} brillo={1.45} />
          </Grade>
        </Golpe>
        <Vineta fuerza={0.5} />
      </Sequence>
      {/* la luz nace en la G (medida: está en 0,78 / 0,47 al momento del corte) */}
      <Sequence from={C} durationInFrames={34} layout="none">
        <LuzNaciente cx={0.78} cy={0.47} />
      </Sequence>

      {/* ---------- ACTO 3 · Lo primero que hizo ---------- */}
      <Sequence from={D} durationInFrames={E - D}>
        <Latigazo>
          <Grade look={LOOK_DATOS}>
            <Deriva dur={E - D} de={1.02} a={1.11} dx={22}>
              <Clip
                src="assets/gcl/s04_archivo.mp4"
                rate={rateClip("assets/gcl/s04_archivo.mp4", E - D, 0.85)}
              />
            </Deriva>
          </Grade>
        </Latigazo>
        <Vineta />
      </Sequence>
      {/* La voz dice «Partió leyendo tres años de campañas». La placa NO lo
          repite: aporta la escala. Ver GCL_SCRIPTS.md — voz y pantalla corren
          en paralelo, nunca en paralelo idéntico. */}
      <Placa at={D + 22} dur={126} size={62}>
        Todo el archivo,
        <br />
        <span style={{color: PINK}}>de una sentada.</span>
      </Placa>

      <Sequence from={E} durationInFrames={F - E}>
        <Latigazo fuerza={0.8}>
          <Grade look={LOOK_DATOS}>
            <Still
              src="assets/gcl/s05_alerta_detecta.png"
              dur={F - E}
              to={1.12}
              vaiven={9}
            />
          </Grade>
        </Latigazo>
        <Vineta />
      </Sequence>
      {/* Voz: «Y encontró un patrón que llevaba ahí desde el principio». */}
      <Placa at={E + 18} dur={110} size={66}>
        Estaba
        <br />
        <span style={{color: CORAL}}>a la vista.</span>
      </Placa>
      {/* modo detectando: los ojos pasan de «X X» a dos iris que enfocan.
          Ojos medidos sobre el PNG y llevados a pantalla a escala 1:
          (407, 674) y (586, 674), tamaño ~140 px. */}
      <Sequence from={E + 26} durationInFrames={100} layout="none">
        <Detectando
          dur={100}
          ojos={[
            [354, 672],
            [566, 655],
          ]}
          tam={168}
          escIni={1.03 + (0.09 * 26) / (F - E)}
          escFin={1.03 + (0.09 * 126) / (F - E)}
          desfase={26}
          vaiven={9}
        />
      </Sequence>

      {/* HUD del acto 3: es él leyendo. La etiqueta cambia cuando encuentra. */}
      <Sequence from={D + 10} durationInFrames={E - D - 16} layout="none">
        <Hud dur={E - D - 16} etiqueta="ARCHIVO · 2023—2026" />
      </Sequence>
      <Sequence from={E + 6} durationInFrames={F - E - 18} layout="none">
        <Hud dur={F - E - 18} etiqueta="PATRÓN · 001" barrido={false} />
      </Sequence>

      {/* ---------- ACTO 4 · La ficha (la presentación) ---------- */}
      {/* Sale de la oscuridad y avanza hacia la cámara; sobre él se despliegan
          los roles. Pedido 20-08. */}
      <Sequence from={F} durationInFrames={H - F}>
        <Grade look={LOOK_PERSONAJE}>
          <Emerge dur={H - F}>
            <Clip
              src="assets/gcl/s07_void.mp4"
              rate={rateClip("assets/gcl/s07_void.mp4", H - F, 0.83)}
            />
          </Emerge>
          <Bloom radio={22} fuerza={0.3} brillo={1.4} />
        </Grade>
      </Sequence>
      {/* cuando cobra vida en el vacío, la luz también nace en él */}
      <Sequence from={F} durationInFrames={34} layout="none">
        <LuzNaciente cx={0.56} cy={0.42} fuerza={0.5} />
      </Sequence>
      {/* los roles se van justo antes de que entre la placa del final */}
      <Sequence from={F + 4} durationInFrames={104} layout="none">
        <Ficha dur={104} />
      </Sequence>
      <Placa at={F + 20} dur={72} size={74} align="center" bottom={318} regla={false}>
        Hola. Soy G.CL.
      </Placa>
      {/* el guiño: la G se cierra y queda una raya. Coordenadas medidas sobre
          el render (la G ocupa x 573-685, y 712-867 en 1080x1920). */}
      {/* El guiño de la G: dos parpadeos mientras está su nombre en pantalla.
          Las coordenadas son a escala 1 (medidas sobre el render: la G está en
          608,799 y mide 114x155) y el componente aplica la escala de Emerge,
          que en estos frames va de 1,077 a 1,157. */}
      <Sequence from={F + 46} durationInFrames={48} layout="none">
        <Guino
          cx={608}
          cy={799}
          w={114}
          h={155}
          dur={48}
          escIni={1 + (0.3 * 46) / (H - F)}
          escFin={1 + (0.3 * 94) / (H - F)}
        />
      </Sequence>
      {/* entra después de los roles y con movimiento propio (sube y se cierra
          el interletrado), no con el barrido de las otras placas */}
      <Placa
        at={F + 106}
        dur={72}
        size={52}
        align="center"
        bottom={300}
        regla={false}
        sube
      >
        Me contrataron para
        <br />
        <span style={{color: PINK}}>cuestionarlo todo.</span>
      </Placa>

      {/* ---------- ACTO 5 · Ahora trabaja acá ---------- */}
      <Sequence from={H} durationInFrames={I - H}>
        <Latigazo>
          <Grade look={LOOK_OFICINA}>
            {/* s06b arranca en el segundo 2,6 del original: es donde deja de
                mirar a cámara y se gira hacia la pantalla de ella. */}
            <Deriva dur={I - H} de={1.02} a={1.08} dx={-18}>
              <Clip
                src="assets/gcl/s06b_escritorio.mp4"
                rate={rateClip("assets/gcl/s06b_escritorio.mp4", I - H, 0.48)}
              />
            </Deriva>
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.55} />
      </Sequence>
      {/* Voz: «Hoy trabaja al lado nuestro». La placa da el carácter. */}
      <Placa at={H + 24} dur={108} size={62}>
        Pregunta. Audita.
        <br />
        <span style={{color: PINK}}>Propone.</span>
      </Placa>

      <Sequence from={I} durationInFrames={J - I}>
        <Latigazo fuerza={0.7}>
          <Grade look={LOOK_OFICINA}>
            {/* s08b arranca en 1,7 s: el giro completo hacia el monitor */}
            <Deriva dur={J - I} de={1.02} a={1.09} dy={-14}>
              <Clip
                src="assets/gcl/s08b_ella_mira.mp4"
                rate={rateClip("assets/gcl/s08b_ella_mira.mp4", J - I, 0.74)}
              />
            </Deriva>
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.55} />
      </Sequence>
      {/* Voz: «Ve lo mismo que ves tú». */}
      <Placa at={I + 50} dur={80} size={60}>
        Y marca
        <br />
        <span style={{color: PINK}}>lo que se te pasó.</span>
      </Placa>
      <Sequence from={I + 44} durationInFrames={86} layout="none">
        <Hud dur={86} etiqueta="PATRÓN DETECTADO" barrido={false} />
      </Sequence>

      <Sequence from={J} durationInFrames={K - J}>
        <Latigazo>
          <Grade look={LOOK_NOCHE}>
            <Deriva dur={K - J} de={1.02} a={1.1} dx={16}>
              <Clip
                src="assets/gcl/s09_turno_noche.mp4"
                rate={rateClip("assets/gcl/s09_turno_noche.mp4", K - J, 0.9)}
              />
            </Deriva>
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.68} />
      </Sequence>
      <Reloj at={J + 12} dur={80}>
        00:58
      </Reloj>
      {/* Voz: «Cuando apagamos las luces, él sigue prendido». El reloj hace
          casi todo el trabajo; la placa solo agrega que nadie se lo pidió. */}
      <Placa at={J + 20} dur={100} size={72}>
        Trabaja <span style={{color: PINK}}>24/7</span>.
      </Placa>

      {/* ---------- ACTO 6 · La tesis. Acá el HUD ya no está: deciden ellos. */}
      <Sequence from={K} durationInFrames={L - K}>
        <Latigazo fuerza={0.9}>
          <Grade look={LOOK_OFICINA}>
            {/* s10b arranca en el segundo 2,0: entra con la G de frente y
                durante el plano se gira hacia el equipo. Que se dé vuelta acá
                es el punto — la decisión la toman ellos, no él. */}
            <Deriva dur={L - K} de={1.03} a={1.09}>
              <Clip
                src="assets/gcl/s10b_equipo.mp4"
                rate={rateClip("assets/gcl/s10b_equipo.mp4", L - K, 0.37)}
              />
            </Deriva>
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.5} />
      </Sequence>
      <Placa at={K + 14} dur={70} size={64}>
        No decide él.
      </Placa>
      <Placa at={K + 92} dur={88} size={64}>
        Decidimos <span style={{color: PINK}}>nosotros</span>.
      </Placa>

      {/* ---------- Cierre de marca ---------- */}
      <Sequence from={L} durationInFrames={durationInFrames - L}>
        <CierreMarca dur={durationInFrames - L} />
      </Sequence>

      <Sequence from={0} durationInFrames={L}>
        <Rotulo />
      </Sequence>
      <Sequence from={0} durationInFrames={L}>
        <PostFX />
      </Sequence>
    </AbsoluteFill>
  );
};
