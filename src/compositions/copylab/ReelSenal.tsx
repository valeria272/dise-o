// ============================================================================
// 10 · REEL / SEÑAL — «No es tu producto. Es cómo lo dices.»
// ----------------------------------------------------------------------------
// INSIGHT   Toda empresa chilena escribe las mismas cuatro frases muertas, y
//           esas frases le cuestan plata. No es un problema de presupuesto:
//           es que nadie se atrevió a decir algo concreto.
// IDEA      No explicar el servicio: ejecutarlo en pantalla. Cada frase muerta
//           entra grande, se TACHA, y cae la versión que sí vende. El reel es
//           una demo del producto, no un aviso del producto.
// HOOK      Sin preámbulo. El primer fotograma YA es una frase muerta que el
//           espectador reconoce como propia — el impacto está antes de 1,5 s
//           (COPYWRITERS_CREATIVE_OS, familia «reel»).
// RITMO     Cuatro pares que ACELERAN: 2,5 s · 2,0 s · 1,67 s · 1,5 s. La
//           aceleración es el mecanismo — al cuarto par el espectador ya sabe
//           lo que viene y lo completa solo. Ahí es cuando comparte.
// ANOMALÍA Una: el salto de escala del remate, donde «PRODUCTO.» baja a la
//           mitad del cuerpo de «NO ES TU». Todo lo demás se comporta.
// INTERV.  El tachado, y nada más. El rosa NUNCA decora acá: sólo anula. Esa
//           disciplina es lo que permite que aparezca cuatro veces sin volverse
//           relleno (tokens.json → jerarquiaColor.regla).
// VOCES    3 por escena: impacto (la frase muerta) · editorial (la que vende) ·
//           data (el índice). Es el tope del sistema.
// ZONAS    9:16 con zonas seguras de Meta: 250 arriba, 340 abajo, 115 derecha.
// ⚠️ COPY  Propuesto por el estudio para la cuenta propia — no viene de un
//           brief. Si Valeria cambia una línea, se cambia acá y se re-renderiza.
// ============================================================================
import React from "react";
import {
  AbsoluteFill,
  Audio,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {C, asegurarFuentes, margen} from "../../brand/copylab/sistema";
import {Bloque, Indice, Linea as TLinea} from "../../brand/copylab/tipografia";
import {Pieza} from "../../brand/copylab/lienzo";
import {Tachado} from "../../brand/copylab/mano";

// ---------------------------------------------------------------------------
// El guion. Cada par es: la frase que escribe todo el mundo → la que vende.
// `muerta` es un arreglo de LÍNEAS porque el quiebre es una decisión de
// composición, no un ajuste automático de ancho.
// ---------------------------------------------------------------------------
type Par = {
  /** Líneas explícitas: cada una decide su ancho y su escala. Con un string[]
   *  el bloque sólo se puede rellenar; con líneas se puede componer — y es lo
   *  que evita que «Y COMPROMISO» se salga del lienzo. */
  muerta: TLinea[];
  /** Ancho del trazo en px. Sobrepasa un poco la línea más larga, como una mano. */
  tachaW: number;
  /** Dónde cruza el trazo, medido desde el tope del bloque. */
  tachaY: number;
  viva: string;
  base: number;
  dur: number;
};

const PARES: Par[] = [
  {
    muerta: [{t: "SOMOS", wdth: 66}, {t: "LÍDERES", wdth: 66}, {t: "EN EL RUBRO", wdth: 66}],
    // cruza «LÍDERES» (línea 1 de 3): centro 253 − 22 de offset del trazo
    base: 196, tachaW: 760, tachaY: 226,
    viva: "Llegamos en 24 horas.", dur: 75,
  },
  {
    // «Y COMPROMISO» se condensa al tope (62) y baja de cuerpo: es la línea
    // más larga del guion y a 196/66 se salía del lienzo.
    muerta: [{t: "CALIDAD", wdth: 66}, {t: "Y COMPROMISO", wdth: 62, esc: 0.8}],
    // cruza «Y COMPROMISO» (línea 2): 168,6 + 67,4 = 236 − 22
    base: 196, tachaW: 900, tachaY: 214,
    viva: "Si se rompe, te lo cambiamos.", dur: 60,
  },
  {
    muerta: [{t: "SOLUCIONES", wdth: 66}, {t: "INTEGRALES", wdth: 66}],
    // cruza «INTEGRALES» (línea 2): 168,6 + 84,3 = 253 − 22
    base: 196, tachaW: 900, tachaY: 231,
    viva: "Hacemos la pega completa.", dur: 50,
  },
  {
    muerta: [{t: "CONTÁCTANOS", wdth: 66}, {t: "PARA MÁS", wdth: 66}, {t: "INFORMACIÓN", wdth: 66}],
    // cruza «PARA MÁS» (línea 2 de 3): 144,5 + 72,2 = 217 − 22
    base: 168, tachaW: 700, tachaY: 195,
    viva: "Te cotizo hoy.", dur: 45,
  },
];

const TOP_BLOQUE = 640; // dentro de la zona segura de arriba (250) con aire
const TOP_VIVA = 1210; // y por encima de la zona segura de abajo (1580)

// ---------------------------------------------------------------------------
// Una escena: frase muerta → tachado → frase viva. Cortes duros, sin fundidos
// entre escenas: el fundido cruzado es de presentación corporativa, no de reel.
// ---------------------------------------------------------------------------
const Par: React.FC<{p: Par; M: number}> = ({p, M}) => {
  const f = useCurrentFrame();
  const {width: W} = useVideoConfig();

  // La frase muerta entra de golpe y se asienta. 4 cuadros, no 20.
  const entra = interpolate(f, [0, 4], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const asienta = interpolate(f, [0, 7], [1.045, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});

  // El tachado se DIBUJA de izquierda a derecha: es una mano, no un rectángulo
  // que aparece. Arranca al 42% de la escena.
  const t0 = Math.round(p.dur * 0.42);
  const traza = interpolate(f, [t0, t0 + 6], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});

  // La frase viva cae después del tachado, no antes: el orden ES el argumento.
  const v0 = t0 + 7;
  const vOp = interpolate(f, [v0, v0 + 6], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const vDy = interpolate(f, [v0, v0 + 8], [26, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});

  return (
    <Pieza fondo={C.tinta} grano={0.2}>
      <Indice familia="Señal" ref="reel" style={{position: "absolute", left: M, top: 272}} />

      <div
        style={{
          position: "absolute",
          left: M,
          top: TOP_BLOQUE,
          opacity: entra,
          transform: `scale(${asienta})`,
          transformOrigin: "left top",
        }}
      >
        <Bloque
          base={p.base}
          lineas={p.muerta.map((l): TLinea => ({wght: 900, ...l}))}
        />
      </div>

      {/* Anula la frase, no la empresa. El rosa acá sólo hace este trabajo.
          El recorte va sobre un AbsoluteFill: sobre un div suelto el `Tachado`
          queda fuera de la caja (es absoluto) y se recorta entero. */}
      <AbsoluteFill
        style={{clipPath: `inset(0 ${((W - (M - 14) - p.tachaW * traza) / W) * 100}% 0 0)`}}
      >
        <Tachado
          x={M - 14}
          y={TOP_BLOQUE + p.tachaY}
          w={p.tachaW}
          grosor={11}
          semilla={11}
          angulo={-1.6}
        />
      </AbsoluteFill>

      <div
        style={{
          position: "absolute",
          left: M,
          top: TOP_VIVA,
          opacity: vOp,
          transform: `translateY(${vDy}px)`,
        }}
      >
        <Bloque
          base={p.base}
          sangria={0.012}
          lineas={[{t: p.viva, voz: "editorial", esc: 0.34, color: C.offwhite}]}
        />
      </div>
    </Pieza>
  );
};

// ---------------------------------------------------------------------------
// El remate. Acá el rosa cambia de trabajo por única vez: deja de anular y
// firma. Por eso la línea editorial es la última cosa que se ve.
// ---------------------------------------------------------------------------
const Remate: React.FC<{M: number; dur: number}> = ({M, dur}) => {
  const f = useCurrentFrame();
  const a = interpolate(f, [0, 5], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const b = interpolate(f, [14, 22], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const bDy = interpolate(f, [14, 24], [22, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const c = interpolate(f, [dur - 40, dur - 30], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});

  return (
    <Pieza fondo={C.tinta} grano={0.2}>
      <Indice familia="Señal" ref="reel" style={{position: "absolute", left: M, top: 272}} />

      <div style={{position: "absolute", left: M, top: TOP_BLOQUE, opacity: a}}>
        <Bloque
          base={196}
          lineas={[
            {t: "NO ES TU", wdth: 66, wght: 900},
            // La anomalía de la pieza: el producto se empequeñece porque el
            // producto no es el problema.
            {t: "PRODUCTO.", wdth: 92, wght: 900, esc: 0.5, dy: 10},
          ]}
        />
      </div>

      <div style={{position: "absolute", left: M, top: TOP_VIVA, opacity: b, transform: `translateY(${bDy}px)`}}>
        <Bloque
          base={196}
          sangria={0.012}
          lineas={[{t: "Es cómo lo dices.", voz: "editorial", esc: 0.42, color: C.rosa}]}
        />
      </div>

      <div style={{position: "absolute", left: M, top: 1470, opacity: c}}>
        <Indice familia="copywriters.cl" color={C.offwhite} size={26} />
      </div>
    </Pieza>
  );
};

export const ReelSenal: React.FC = () => {
  asegurarFuentes();
  const {width: W, durationInFrames} = useVideoConfig();
  const M = margen(W);

  let t = 0;
  const bloques = PARES.map((p) => {
    const desde = t;
    t += p.dur;
    return {p, desde};
  });
  const remateDesde = t;
  const remateDur = durationInFrames - remateDesde;

  return (
    <AbsoluteFill style={{backgroundColor: C.tinta}}>
      {bloques.map(({p, desde}, i) => (
        <Sequence key={i} from={desde} durationInFrames={p.dur}>
          <Par p={p} M={M} />
        </Sequence>
      ))}

      <Sequence from={remateDesde} durationInFrames={remateDur}>
        <Remate M={M} dur={remateDur} />
      </Sequence>

      {/* Música propia de la cuenta (la del reel R01 del universo G.CL). */}
      <Audio src={staticFile("assets/gcl/music_r01.mp3")} volume={0.55} />
    </AbsoluteFill>
  );
};

/** 4 pares (75+60+50+45 = 230) + remate de 100 = 330 cuadros = 11,0 s a 30 fps. */
export const REEL_SENAL_FRAMES = 330;
