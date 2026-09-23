import React from "react";
import {
  AbsoluteFill,
  Img,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
} from "remotion";
import {Audio, Video} from "@remotion/media";

/**
 * G.CL — Temporada 1, Capítulo 02: «Turno de noche»
 *
 * Storyboard y guion: gcl-agent/R02_STORYBOARD.md
 * Locución: gcl-agent/videos/vo/R02_GUION_LOCUCION.md
 *
 * v3 — EPISODIO ANIMADO. La v2 era un documental de 32 s con fotos fijas y
 * empuje de escala, y quedó PLANA: «todas las imágenes del principio son
 * estáticas». Acá casi todos los planos son **clips animados de verdad**
 * (image-to-video con Kling 2.1 pro desde los keyframes), el capítulo pasa
 * entero en la sala de reuniones real —no en un vacío negro abstracto— y tiene
 * arco de episodio con cuatro gags: la zapatilla que asoma del portal, el
 * saltito del hallazgo, los paneles que se le caen y el bostezo.
 *
 * LA FÓRMULA: la voz en off sigue siendo documental e impasible, y **el chiste
 * lo hace la imagen**. Si la voz también hiciera el chiste, el capítulo se
 * caería en aviso simpático. El narrador nunca se ríe.
 *
 * Se mantiene todo el sistema del capítulo 1 (rejilla de 120 BPM, gradación por
 * plano, floración, latigazos, HUD como punto de vista, cierre de marca con el
 * punto que aterriza en la «g»). Los componentes están duplicados a propósito:
 * el R01 está aprobado y renderizado, y no se toca. Cuando exista el capítulo
 * 03 se extraen los dos a un módulo común.
 */

export const GCL_R02_FPS = 30;
export const GCL_R02_DURATION = 1200; // 40 s

const PINK = "#FF4D8D";
const CORAL = "#FF7A59";

/**
 * LOS TRES DATOS DEL ACTO 2. Salen de los logs de los agentes de la agencia.
 * `null` = todavía no verificado: se dibuja como pendiente y NO se publica así.
 * Regla dura del capítulo: los datos son reales o el bloque se borra.
 */
const DATOS: {valor: number | null; etiqueta: string}[] = [
  {valor: null, etiqueta: "campañas revisadas"},
  {valor: null, etiqueta: "comentarios respondidos"},
  {valor: null, etiqueta: "alertas levantadas"},
];

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

/** Separador de miles chileno: 1.248. Sin decimales, nunca. */
const miles = (n: number) =>
  String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ".");

/* ==========================================================================
   1. IMAGEN — gradación, floración, movimiento
   ========================================================================== */

type Look = {
  con?: number;
  sat?: number;
  bri?: number;
  sombra?: string;
  luz?: string;
  luzOp?: number;
};

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

/**
 * Plano fijo con vida. `empuje` es el recorrido de escala y `vaiven` el
 * cabeceo. En este capítulo los valores son MÁS AGRESIVOS que en el R01: los
 * planos duran la mitad, así que el movimiento tiene que leerse en 30 frames.
 */
const Plano: React.FC<{
  src: string;
  dur: number;
  de?: number;
  a?: number;
  dx?: number;
  dy?: number;
  vaiven?: number;
  mano?: number;
}> = ({src, dur, de = 1.04, a = 1.16, dx = 0, dy = 0, vaiven = 0, mano = 0}) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [0, dur], [0, 1], {extrapolateRight: "clamp"});
  const e = de + (a - de) * salida(p);
  // cámara en mano: dos senos incoherentes, nunca un random (parpadearía)
  const mx =
    mano * (Math.sin(frame / 5.3) + 0.6 * Math.sin(frame / 2.7 + 1.1)) +
    vaiven * Math.sin(frame / 29);
  const my =
    mano * (Math.sin(frame / 6.9 + 2.2) + 0.5 * Math.sin(frame / 3.4)) +
    vaiven * 0.7 * Math.sin(frame / 23 + 1.7);
  const rot = mano * 0.06 * Math.sin(frame / 8.5) + vaiven * 0.03 * Math.sin(frame / 37);
  return (
    <AbsoluteFill style={{overflow: "hidden", backgroundColor: "#000"}}>
      <Img
        src={staticFile(src)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          transform: `scale(${e}) translate(${dx * salida(p) + mx}px, ${
            dy * salida(p) + my
          }px) rotate(${rot}deg)`,
        }}
      />
    </AbsoluteFill>
  );
};

/** Entrada de plano tipo latigazo: se lee como movimiento de cámara. */
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
  const r = 74 + 3 * Math.sin(frame / 44);
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

/** La luz nace en el visor y se expande. Nunca un degradado rosado encima. */
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

/** Grano + caída de bordes. Última capa, sobre todo el reel. */
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
   2. RÓTULOS Y RELOJ
   ========================================================================== */

const Rotulo: React.FC<{dur: number}> = ({dur}) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 10, dur - 16, dur], [0, 0.7, 0.7, 0], {
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{padding: "96px 0 0 90px"}}>
      <div
        style={{
          fontFamily: MONO,
          fontWeight: 700,
          fontSize: 20,
          letterSpacing: "0.24em",
          color: "#fff",
          opacity: o,
          textShadow: "0 2px 18px rgba(0,0,0,.95)",
        }}
      >
        TEMPORADA 1 · CAPÍTULO 02
      </div>
    </AbsoluteFill>
  );
};

/**
 * El reloj de observación. En el capítulo 1 marcaba una hora fija; acá CORRE
 * al segundo: es el recurso más barato que existe para que el primer plano de
 * un documental no se lea como una foto.
 */
const RelojCorriendo: React.FC<{desde: string; dur: number}> = ({desde, dur}) => {
  const frame = useCurrentFrame();
  const [h, m, s] = desde.split(":").map(Number);
  const t = h * 3600 + m * 60 + s + Math.floor(frame / GCL_R02_FPS);
  const dd = (n: number) => String(n).padStart(2, "0");
  const o = interpolate(frame, [0, 8, dur - 10, dur], [0, 1, 1, 0], {
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{padding: "150px 0 0 90px"}}>
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
        {dd(Math.floor(t / 3600) % 24)}:{dd(Math.floor(t / 60) % 60)}:
        {dd(t % 60)}
      </div>
    </AbsoluteFill>
  );
};

const RelojFijo: React.FC<{dur: number; children: React.ReactNode}> = ({
  dur,
  children,
}) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 8, dur - 10, dur], [0, 1, 1, 0], {
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{padding: "150px 0 0 90px"}}>
      <div
        style={{
          fontFamily: MONO,
          fontWeight: 700,
          fontSize: 30,
          letterSpacing: "0.22em",
          color: CORAL,
          opacity: o,
          textShadow: "0 4px 24px rgba(0,0,0,.9)",
        }}
      >
        {children}
      </div>
    </AbsoluteFill>
  );
};

/* ==========================================================================
   3. FICHA — la versión de este capítulo. No repite los campos del capítulo 1
   (allá: altura y función); acá describe el turno, que es de lo que va el
   episodio, y remata con un chiste dicho con cara de palo.
   ========================================================================== */

// La ficha es del mismo humor que el narrador: dice datos con cara de palo.
// «RELEVO — NADIE» es el chiste, y no lo subraya nadie.
const CAMPO: [string, string, number][] = [
  ["UNIDAD", "01 · GRUPO COPYLAB", 0],
  ["TURNO", "23:00 – 07:40", 11],
  ["RELEVO", "NADIE", 22],
];

const FichaCampo: React.FC<{dur: number}> = ({dur}) => {
  const frame = useCurrentFrame();
  const fuera = interpolate(frame, [dur - 12, dur], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{padding: "230px 0 0 90px", opacity: fuera}}>
      {CAMPO.map(([k, v, retardo]) => {
        const e = interpolate(frame, [retardo, retardo + 14], [0, 1], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
          easing: salida,
        });
        return (
          <div
            key={k}
            style={{
              display: "flex",
              alignItems: "baseline",
              gap: 18,
              marginBottom: 14,
              opacity: e,
              transform: `translateX(${(1 - e) * -26}px)`,
            }}
          >
            <div
              style={{
                width: 4 + 30 * e,
                height: 2,
                background: CORAL,
                opacity: 0.9,
              }}
            />
            <div
              style={{
                fontFamily: MONO,
                fontWeight: 700,
                fontSize: 17,
                letterSpacing: "0.22em",
                color: "rgba(255,255,255,.55)",
                minWidth: 118,
              }}
            >
              {k}
            </div>
            <div
              style={{
                fontFamily: MONO,
                fontWeight: 700,
                fontSize: 21,
                letterSpacing: "0.14em",
                color: "#fff",
                textShadow: "0 2px 18px rgba(0,0,0,.95)",
              }}
            >
              {v}
            </div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

/* ==========================================================================
   4. HUD — el punto de vista de G.CL. Se enciende cuando él lee y SE APAGA
   cuando entra la gente: ahí ya no mira él.
   ========================================================================== */

const Hud: React.FC<{dur: number; etiqueta: string}> = ({dur, etiqueta}) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 12, dur - 10, dur], [0, 1, 1, 0], {
    extrapolateRight: "clamp",
  });
  const esq = interpolate(frame, [0, 14], [0, 1], {
    extrapolateRight: "clamp",
    easing: salida,
  });
  const y = ((frame % 70) / 70) * 100; // barrido más rápido que en el R01
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
      <div style={esquina({left: `${G}%`, top: `${G}%`}, 0)} />
      <div style={esquina({left: `${G}%`, top: `${G}%`}, 90)} />
      <div style={esquina({right: `${G}%`, top: `${G}%`}, 180)} />
      <div style={esquina({right: `${G}%`, top: `${G}%`}, 90)} />
      <div style={esquina({left: `${G}%`, bottom: `${G}%`}, 0)} />
      <div style={esquina({left: `${G}%`, bottom: `${G}%`}, -90)} />
      <div style={esquina({right: `${G}%`, bottom: `${G}%`}, 180)} />
      <div style={esquina({right: `${G}%`, bottom: `${G}%`}, -90)} />
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
   5. LOS PANELES DE DATOS — construidos en código, no generados.
   Es lo que permite que la cifra SUBA y aterrice en el tiempo fuerte: con un
   render de IA el número sería una imagen fija y el acto 2 perdería su motor.
   ========================================================================== */

/** La cifra corre y aterriza. Si el dato no está verificado, no inventa nada. */
const Contador: React.FC<{
  valor: number | null;
  etiqueta: string;
  aterriza: number;
}> = ({valor, etiqueta, aterriza}) => {
  const frame = useCurrentFrame();
  // aterriza <= 0 = la cifra ya llegó (planos de sostén: no vuelve a subir)
  const p =
    aterriza <= 0
      ? 1
      : interpolate(frame, [0, aterriza], [0, 1], {
          extrapolateRight: "clamp",
          easing: salida,
        });
  // el golpe de escala cuando la cifra se detiene: es lo que la hace "aterrizar"
  const golpe =
    aterriza <= 0 ? 0 : frame < aterriza ? 0 : Math.max(0, 1 - (frame - aterriza) / 10);
  const texto = valor === null ? "———" : miles(valor * p);
  return (
    <div style={{textAlign: "center"}}>
      <div
        style={{
          fontFamily: DISPLAY,
          fontWeight: 800,
          fontSize: 196,
          lineHeight: 1,
          letterSpacing: "-0.045em",
          color: "#fff",
          textShadow: `0 0 60px rgba(255,77,141,${0.35 + 0.3 * golpe})`,
          transform: `scale(${1 + 0.06 * golpe})`,
        }}
      >
        {texto}
      </div>
      <div
        style={{
          fontFamily: MONO,
          fontWeight: 700,
          fontSize: 26,
          letterSpacing: "0.2em",
          color: PINK,
          marginTop: 22,
          textTransform: "uppercase",
        }}
      >
        {etiqueta}
      </div>
      {valor === null ? (
        <div
          style={{
            display: "inline-block",
            marginTop: 26,
            padding: "7px 16px",
            border: `2px solid ${CORAL}`,
            borderRadius: 4,
            fontFamily: MONO,
            fontWeight: 700,
            fontSize: 17,
            letterSpacing: "0.2em",
            color: CORAL,
          }}
        >
          DATO PENDIENTE
        </div>
      ) : null}
    </div>
  );
};

/* El componente `Panel` (caja con borde y barras dibujadas) y `FondoVivo` (el
   plano desenfocado que le hacía de fondo) salieron del capítulo el 02-09-2026.
   Las cifras iban dentro de una caja sobre un fondo borroso y era exactamente
   lo que se leía como «gráfico plano pegado encima». Ahora el número va suelto
   sobre el plano vivo, sin caja — ver el componente `Cifra` del montaje. */

const LINEAS = [
  "> turno 23:00-07:40",
  "> patrones: 3",
  "> fuera de rango: 1",
];

const Resumen: React.FC<{dur: number}> = ({dur}) => {
  const frame = useCurrentFrame();
  const PASO = 0.62; // frames por carácter — es una máquina, no una persona
  const sal = interpolate(frame, [dur - 8, dur], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  let consumido = 3;
  return (
    <AbsoluteFill style={{opacity: sal}}>
      {/* velo bajo el texto: el plano de abajo es el canto oscuro de la mesa,
          pero el Courier necesita un piso propio para no depender de él */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(to top, rgba(0,0,0,.86) 0%, rgba(0,0,0,.55) 34%, transparent 62%)",
        }}
      />
      <AbsoluteFill
        style={{justifyContent: "flex-end", padding: "0 100px 260px"}}
      >
      {LINEAS.map((l) => {
        const inicio = consumido;
        consumido += l.length * PASO + 4;
        const n = Math.max(
          0,
          Math.min(l.length, Math.floor((frame - inicio) / PASO))
        );
        const ultima = n > 0 && n < l.length;
        return (
          <div
            key={l}
            style={{
              fontFamily: MAQUINA,
              fontWeight: 700,
              fontSize: 40,
              letterSpacing: "0.02em",
              lineHeight: 1.7,
              color: l.includes("fuera de rango") ? CORAL : "rgba(255,255,255,.92)",
              textShadow: "0 3px 22px rgba(0,0,0,.95)",
              whiteSpace: "pre",
            }}
          >
            {l.slice(0, n)}
            {ultima ? (
              <span style={{color: PINK, opacity: frame % 12 < 6 ? 1 : 0.2}}>
                _
              </span>
            ) : null}
          </div>
        );
      })}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* ==========================================================================
   5 bis. CLIPS ANIMADOS — el motor visual de esta versión.
   Los planos salen de `scripts/gcl-r02-clips.py` (Kling 2.1 pro, image-to-video):
   **5,04 s a 24 fps**, no a 30. Y Kling empieza a desviarse pasados unos
   2 segundos —en el R01 hizo girar al personaje hasta dejarlo de espaldas sin
   el visor—, así que el montaje usa sólo el primer tramo de cada clip.
   ========================================================================== */

// Todos los clips de Kling duran 5,04 s y ningún plano del reel pasa de 2 s,
// así que a rate 1 nunca se llega al final: no hay riesgo de que un plano se
// congele en su último fotograma, que fue el error del R01 («la chica del
// primer cut se queda pegada»). Si algún plano creciera más allá de 4,6 s hay
// que bajarle el `rate`.

/**
 * ⚠️ `trim` va en SEGUNDOS y acá se convierte a frames.
 *
 * Remotion recibe `trimBefore` en **frames**, no en segundos. Escribir
 * `trim={1.8}` pensando en segundos recorta 1,8 FRAMES —o sea, nada— y el plano
 * se ve entero desde el principio. Costó un render entero descubrirlo: el panel
 * del plano en que escribe salía celeste porque el recorte que lo evitaba no
 * estaba haciendo nada. Los recortes de este capítulo se midieron mirando los
 * clips en segundos, así que la conversión vive acá y no en cada llamada.
 */
const Clip: React.FC<{
  src: string;
  rate?: number;
  trim?: number;
  /** Recorte por acercamiento. Sirve para sacar de cuadro lo que la IA metió
   *  y no queremos: pantallas de laptop con texto inventado, bordes sucios. */
  zoom?: number;
}> = ({src, rate = 1, trim = 0, zoom = 1}) => (
  <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
    <Video
      src={staticFile(src)}
      style={{
        width: "100%",
        height: "100%",
        objectFit: "cover",
        transform: zoom === 1 ? undefined : `scale(${zoom})`,
      }}
      playbackRate={rate}
      trimBefore={Math.round(trim * GCL_R02_FPS)}
      volume={() => 0}
      muted
    />
  </AbsoluteFill>
);

/* ==========================================================================
   7. CIERRE DE MARCA — el 4º punto del G-Swoosh aterriza como el punto de la
   «g» de Grupo CopyLab. Idéntico al del capítulo 1: es la firma de la serie.
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
  // El cierre del R01 duraba 195 frames; acá tiene 150. Lo que NO se comprime:
  // el viaje del punto (con menos de 28 frames se lee como un salto) y el
  // tiempo que la firma queda en pantalla — en la v1 duraba 10 frames.
  const swoosh = interpolate(frame, [14, 26], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const wordmark = interpolate(frame, [30, 40], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const faseA = interpolate(frame, [70, 84], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const logo = interpolate(frame, [84, 104], [0, 1], {
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

  const viaje = interpolate(frame, [72, 104], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: salida,
  });
  const puntoX = partida.x + (llegada.x - partida.x) * viaje;
  const puntoY = partida.y + (llegada.y - partida.y) * viaje;
  const puntoR = partida.r + (llegada.r - partida.r) * viaje;

  // Colofón: anuncia el capítulo 03, igual que el R01 anunció este.
  const TW0 = 112;
  const TW_PASO = 2.0; // musica-gcl-r02.py: maquina(30.73, 13, 0.0667)
  const TITULO = "Nueve minutos";
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
  const proximo = interpolate(frame, [dur - 8, dur - 1], [1, 0], {
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
      {frame >= 66 ? (
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
          opacity: frame >= 72 ? 1 : 0,
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
            (frame >= 72 ? 1 : 0) *
            interpolate(frame, [92, 106], [0, 1], {
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
            <linearGradient id="gclgradr02" x1="0" y1="1" x2="1" y2="0">
              <stop offset="0" stopColor={CORAL} />
              <stop offset="1" stopColor={PINK} />
            </linearGradient>
          </defs>
          <g fill="url(#gclgradr02)">
            {dots.map((d, i) => {
              const o = interpolate(frame, [3 + i * 3, 9 + i * 3], [0, 1], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              });
              if (i === 3 && frame >= 71) return null;
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
   8. MONTAJE — rejilla de 120 BPM: compás 60 frames, negra 15 frames.
   Todos los cortes caen en múltiplos de 15.
   ========================================================================== */

const LOOK_NOCHE: Look = {
  con: 1.24,
  sat: 0.88,
  bri: 0.92,
  sombra: "rgba(96,132,210,1)",
  luz: "rgba(255,180,140,1)",
  luzOp: 0.07,
};
const LOOK_PERSONAJE: Look = {
  con: 1.2,
  sat: 1.06,
  bri: 1.02,
  sombra: "rgba(84,110,200,1)",
  luz: "rgba(255,196,158,1)",
  luzOp: 0.1,
};
const LOOK_DATOS: Look = {
  con: 1.28,
  sat: 0.94,
  bri: 0.96,
  sombra: "rgba(70,130,225,1)",
  luz: "rgba(255,208,170,1)",
  luzOp: 0.1,
};
const LOOK_MANANA: Look = {
  con: 1.1,
  sat: 1.08,
  bri: 1.05,
  sombra: "rgba(130,155,215,1)",
  luz: "rgba(255,186,124,1)",
  luzOp: 0.16,
};

export const GclTurnoNocheReel: React.FC = () => {
  injectFonts();

  /* ------------------------------------------------------------------------
     v5 — LO QUE SE REHIZO Y POR QUÉ (feedback: «está raro», con las cuatro
     dimensiones marcadas: movimiento, personaje, ritmo y sonido).

     1. FUERA LA CÁMARA LENTA. Kling entrega 24 fps y el reel va a 30: a
        velocidad normal ya se repite 1 de cada 5 fotogramas, y con `rate` bajo
        la repetición se dispara. Medido: el salto repetía cada fotograma 2,1
        veces y el tecleo 2,8. Eso no se ve lento, se ve ESCALONADO.
     2. FUERA LOS PLANOS QUE NO SE MUEVEN. Se midió el cambio medio entre
        fotogramas de cada plano; los dos más muertos (el visor enfocado y el
        manoteo) salieron del capítulo.
     3. FUERA LOS GRÁFICOS SOBRE FONDO MUERTO. Las tres cifras ya no tienen
        plano propio con un panel dibujado: van **encima del plano vivo** en el
        que ocurre lo que cuentan.
     4. DURACIONES VARIADAS. En la v4 casi todos los planos duraban 45 frames
        exactos y el montaje se sentía mecánico. Ahora van de 30 a 90 según lo
        que cada plano tenga que decir, y los que de verdad se mueven —abrir el
        portal, llegar el equipo— son los que se quedan más rato.
     ------------------------------------------------------------------------ */

  // ACTO 1 · se van
  const S1 = 0;     //  0,0 s (2,5) se van conversando
  const S2 = 75;    //  2,5 s (1,0) la mano baja el interruptor   ♪ clac
  const S3 = 105;   //  3,5 s (1,5) el interruptor YA APAGADO     ♪ golpe grave
  const S4 = 150;   //  5,0 s (1,0) la mesa vacía
  // ACTO 2 · la llegada
  const S5 = 180;   //  6,0 s (1,5) LA GRIETA y las dos manos     ♪ rasgado
  const S6 = 225;   //  7,5 s (3,0) LA ABRE — el plano que más se mueve del reel
  const S7 = 315;   // 10,5 s (1,5) EL SALTO                      ♪ whoosh + impacto
  const S8 = 360;   // 12,0 s (2,0) EL GUIÑO a cámara             ♪ tintineo
  // ACTO 3 · a trabajar
  const S9 = 420;   // 14,0 s (2,5) chasquea y encienden paneles  ♪ crack · DATO 1
  const S10 = 495;  // 16,5 s (2,5) EL HALLAZGO                   ♪ acorde + campana
  const S11 = 570;  // 19,0 s (2,0) el patrón y el saltito        ♪ boing · DATO 2
  const S12 = 630;  // 21,0 s (2,0) la alerta                     ♪ braam · DATO 3
  const S13 = 690;  // 23,0 s (2,0) LO CORRIGE                    ♪ tick
  const S14 = 750;  // 25,0 s (2,0) el resumen se escribe         ♪ máquina
  // ACTO 4 · amanece y llega el equipo
  const S15 = 810;  // 27,0 s (3,0) amanece — él sigue DE PIE
  const S16 = 900;  // 30,0 s (2,0) llega el equipo y lo saluda   ♪ se abre
  const S17 = 960;  // 32,0 s (1,5) EL CHOQUE DE MANOS            ♪ ¡PLAF!
  const S18 = 1005; // 33,5 s (1,5) el equipo alrededor           ♪ acorde grande
  const FIN = 1050; // 35,0 s (5,0) cierre de marca

  /** Las cifras van sueltas sobre el plano vivo, sin caja: la caja era lo que
   *  hacía que los datos se leyeran como un gráfico pegado encima. */
  const Cifra: React.FC<{i: number; dur: number; aterriza: number}> = ({
    i,
    dur,
    aterriza,
  }) => (
    <Sequence from={0} durationInFrames={dur} layout="none">
      <AbsoluteFill style={{justifyContent: "flex-end", padding: "0 0 260px"}}>
        <Contador
          valor={DATOS[i].valor}
          etiqueta={DATOS[i].etiqueta}
          aterriza={aterriza}
        />
      </AbsoluteFill>
    </Sequence>
  );

  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Audio src={staticFile("assets/gcl/r02/music_r02.mp3")} />

      {/* ---------- ACTO 1 · Se van ---------- */}
      <Sequence from={S1} durationInFrames={S2 - S1}>
        <Grade look={LOOK_NOCHE}>
          <Clip src="assets/gcl/r02/clips/c01_se_van.mp4" />
        </Grade>
        <Vineta fuerza={0.68} />
      </Sequence>

      <Sequence from={S2} durationInFrames={S3 - S2}>
        <Latigazo fuerza={0.8}>
          <Grade look={LOOK_NOCHE}>
            <Clip src="assets/gcl/r02/clips/c02_interruptor.mp4" trim={0.9} />
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.78} />
      </Sequence>

      <Sequence from={S3} durationInFrames={S4 - S3}>
        <Latigazo fuerza={1.2}>
          <Grade look={{...LOOK_NOCHE, bri: 0.82}}>
            <Clip src="assets/gcl/r02/clips/c02b_apagado.mp4" />
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.86} />
      </Sequence>

      <Sequence from={S4} durationInFrames={S5 - S4}>
        <Grade look={LOOK_NOCHE}>
          <Plano src="assets/gcl/r02/c04_mesa_vacia.jpg" dur={S5 - S4} de={1.03} a={1.06} />
        </Grade>
        <Vineta fuerza={0.8} />
      </Sequence>

      <Sequence from={S1} durationInFrames={S4 - S1} layout="none">
        <Rotulo dur={S4 - S1} />
      </Sequence>
      <Sequence from={S1 + 8} durationInFrames={S4 - S1 - 8} layout="none">
        <RelojCorriendo desde="23:41:07" dur={S4 - S1 - 8} />
      </Sequence>

      {/* ---------- ACTO 2 · La llegada ---------- */}
      <Sequence from={S5} durationInFrames={S6 - S5}>
        <Golpe at={0} fuerza={0.06}>
          <Grade look={LOOK_PERSONAJE}>
            <Clip src="assets/gcl/r02/clips/c05_grieta.mp4" />
            <Bloom radio={30} fuerza={0.3} brillo={1.45} />
          </Grade>
        </Golpe>
        <Vineta fuerza={0.55} />
      </Sequence>
      <Sequence from={S5} durationInFrames={26} layout="none">
        <LuzNaciente cx={0.5} cy={0.42} fuerza={0.7} />
      </Sequence>

      {/* 3 segundos: es el plano que más se mueve de todo el reel y en la v4
          duraba lo mismo que los demás. Acá se queda y respira. */}
      <Sequence from={S6} durationInFrames={S7 - S6}>
        <Latigazo fuerza={0.7}>
          <Grade look={LOOK_PERSONAJE}>
            <Clip src="assets/gcl/r02/clips/c06_abre.mp4" trim={0.4} />
            <Bloom radio={28} fuerza={0.28} brillo={1.45} />
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.58} />
      </Sequence>

      <Sequence from={S7} durationInFrames={S8 - S7}>
        <Latigazo>
          <Grade look={LOOK_PERSONAJE}>
            <Clip src="assets/gcl/r02/clips/c07_salta.mp4" />
            <Bloom radio={26} fuerza={0.26} brillo={1.4} />
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.6} />
      </Sequence>

      <Sequence from={S8} durationInFrames={S9 - S8}>
        <Grade look={LOOK_PERSONAJE}>
          <Clip src="assets/gcl/r02/clips/c08_guino.mp4" trim={0.3} />
          <Bloom radio={26} fuerza={0.24} brillo={1.4} />
        </Grade>
        <Vineta fuerza={0.58} />
      </Sequence>
      <Sequence from={S8 + 10} durationInFrames={S9 - S8 - 10} layout="none">
        <FichaCampo dur={S9 - S8 - 10} />
      </Sequence>

      {/* ---------- ACTO 3 · A trabajar ---------- */}
      {/* La cifra va ENCIMA del plano en que se encienden los paneles. En la v4
          tenía un plano propio con un panel dibujado sobre fondo desenfocado, y
          era justo lo que se veía plano. */}
      <Sequence from={S9} durationInFrames={S10 - S9}>
        <Latigazo>
          <Grade look={LOOK_DATOS}>
            <Clip src="assets/gcl/r02/clips/c09_chasquea.mp4" trim={0.6} />
            <Bloom radio={24} fuerza={0.26} brillo={1.4} />
          </Grade>
        </Latigazo>
        <Vineta />
        <Cifra i={0} dur={S10 - S9} aterriza={45} />
      </Sequence>

      <Sequence from={S10} durationInFrames={S11 - S10}>
        <Golpe at={0} fuerza={0.07}>
          <Grade look={LOOK_PERSONAJE}>
            <Clip src="assets/gcl/r02/clips/c13_sorpresa.mp4" trim={0.3} />
            <Bloom radio={28} fuerza={0.3} brillo={1.45} />
          </Grade>
        </Golpe>
        <Vineta fuerza={0.56} />
      </Sequence>

      <Sequence from={S11} durationInFrames={S12 - S11}>
        <Latigazo>
          <Grade look={LOOK_DATOS}>
            <Clip src="assets/gcl/r02/clips/c14_patron.mp4" trim={0.4} />
            <Bloom radio={26} fuerza={0.28} brillo={1.45} />
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.58} />
        <Cifra i={1} dur={S12 - S11} aterriza={30} />
      </Sequence>

      <Sequence from={S12} durationInFrames={S13 - S12}>
        <Golpe at={0} fuerza={0.07}>
          <Grade look={{...LOOK_DATOS, luz: "rgba(255,150,110,1)", luzOp: 0.16}}>
            <Clip src="assets/gcl/r02/clips/c15_alerta.mp4" trim={0.3} />
            <Bloom radio={26} fuerza={0.28} brillo={1.45} />
          </Grade>
        </Golpe>
        <Vineta fuerza={0.6} />
        <Cifra i={2} dur={S13 - S12} aterriza={30} />
      </Sequence>

      <Sequence from={S13} durationInFrames={S14 - S13}>
        <Latigazo>
          <Grade look={LOOK_PERSONAJE}>
            <Clip src="assets/gcl/r02/clips/c17_corrige.mp4" trim={0.3} />
            <Bloom radio={24} fuerza={0.26} brillo={1.4} />
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.58} />
      </Sequence>

      <Sequence from={S14} durationInFrames={S15 - S14}>
        <Latigazo>
          <Grade look={LOOK_PERSONAJE}>
            <Clip src="assets/gcl/r02/clips/c16_teclea.mp4" trim={1.0} />
            <Bloom radio={22} fuerza={0.2} brillo={1.35} />
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.66} />
      </Sequence>
      <Sequence from={S14} durationInFrames={S15 - S14} layout="none">
        <Resumen dur={S15 - S14} />
      </Sequence>

      <Sequence from={S9} durationInFrames={S15 - S9} layout="none">
        <Hud dur={S15 - S9} etiqueta="TURNO · NOCHE 1" />
      </Sequence>

      {/* ---------- ACTO 4 · Amanece y llega el equipo ---------- */}
      <Sequence from={S15} durationInFrames={S16 - S15}>
        <Grade look={LOOK_MANANA}>
          <Clip src="assets/gcl/r02/clips/c19_amanece.mp4" />
          <Bloom radio={22} fuerza={0.18} brillo={1.3} />
        </Grade>
        <Vineta fuerza={0.52} />
      </Sequence>
      <Sequence from={S15 + 45} durationInFrames={S16 - S15 - 45} layout="none">
        <RelojFijo dur={S16 - S15 - 45}>07:40</RelojFijo>
      </Sequence>

      <Sequence from={S16} durationInFrames={S17 - S16}>
        <Latigazo fuerza={0.8}>
          <Grade look={LOOK_MANANA}>
            <Clip src="assets/gcl/r02/clips/c20_llegan.mp4" trim={0.3} />
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.5} />
      </Sequence>

      <Sequence from={S17} durationInFrames={S18 - S17}>
        <Golpe at={0} fuerza={0.05}>
          <Grade look={LOOK_MANANA}>
            <Clip src="assets/gcl/r02/clips/c21_highfive.mp4" trim={1.4} />
            <Bloom radio={20} fuerza={0.2} brillo={1.35} />
          </Grade>
        </Golpe>
        <Vineta fuerza={0.5} />
      </Sequence>

      <Sequence from={S18} durationInFrames={FIN - S18}>
        <Latigazo>
          <Grade look={LOOK_MANANA}>
            <Clip src="assets/gcl/r02/clips/c22_equipo.mp4" trim={0.4} zoom={1.18} />
          </Grade>
        </Latigazo>
        <Vineta fuerza={0.52} />
      </Sequence>

      <Sequence from={FIN} durationInFrames={GCL_R02_DURATION - FIN}>
        <CierreMarca dur={GCL_R02_DURATION - FIN} />
      </Sequence>

      <PostFX />
    </AbsoluteFill>
  );
};
