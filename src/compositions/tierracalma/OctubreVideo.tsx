import React from "react";
import {
  AbsoluteFill,
  interpolate,
  OffthreadVideo,
  Sequence,
  staticFile,
  useCurrentFrame,
} from "remotion";
import {Audio} from "@remotion/media";
import {tierracalma as TC, ensureTierraCalmaFonts} from "../../brand/tierracalma";

// =============================================================================
// TIERRA CALMA · PIEZAS DE VIDEO · OCTUBRE 2026
//
// Los reels NO llevan el marco. La referencia es el propio reel de septiembre
// del diseñador (`r-17-09.mp4`, disco KINGSTON): clip a sangre, texto blanco
// centrado con halo suave, la pareja Inter Tight Light + IvyOra cursiva, y el
// cierre con el wordmark en cursiva sobre el último plano más "AGENDA TU
// VISITA." en versales espaciadas abajo.
//
// ✅ RESUELTO el 22-09-2026: el cierre del reel SÍ es el logo animado. El
// diseñador subió `TIERRA CALMA CIERRE.mov` a Drive, que es byte a byte el
// mismo archivo que `TIERRA CALMA MOTION.mov` del KINGSTON (sha256 idéntico) —
// o sea, el `tc_motion.mp4` que ya estaba convertido acá. Lo usa la v2 del reel
// de dron (abajo). Los reels de la primera entrega cerraban con el wordmark
// porque así lo hacía el reel publicado de septiembre; se corrigen al
// re-entregarlos.
//
// PIPELINE DE LOS CLIPS (pedido por el diseñador, 14-09-2026):
//   1. imagen clave con Magnific, siguiendo el brief de cada corte
//   2. video desde ESA imagen (Kling 2.5, 9:16, 1080p, keyframe de inicio)
//   3. normalizar a 30 fps  ← los clips salen a 24 y eso mete frames negros
//
// Las disolvencias van A MANO con opacidad. Nunca TransitionSeries con GL
// sobre video: mete frames negros (memoria `reel-video-gotchas`).
// =============================================================================

export const FPS = 30;

export const CLIP = (n: string) => staticFile(`assets/tierracalma/oct/clips/${n}.mp4`);
export const AUDIO = (n: string) => staticFile(`assets/tierracalma/audio/${n}.mp3`);

export const SANS = TC.fonts.body;
const SERIF = TC.fonts.display;

// Los clips de 5 s vienen con 151 fotogramas útiles. El hueco de 140 deja 11
// de solape para la disolvencia sin pasarse del final del archivo.
export const SLOT = 140;
export const CLIP_LEN = 151;
const FADE = 11;
export const REEL_DURATION = SLOT * 3 + CLIP_LEN; // 571 = 19,03 s
export const STORY_DURATION = 300; // 10 s

// Zona segura 9:16 del brief: 14 % libre arriba y abajo.
const SEGURO_SUP = 270;
const SEGURO_INF = 1920 - 270;

// -----------------------------------------------------------------------------
// Primitivas
// -----------------------------------------------------------------------------

export const Lienzo: React.FC<{children: React.ReactNode}> = ({children}) => {
  ensureTierraCalmaFonts();
  return <AbsoluteFill style={{backgroundColor: "#0A0F12"}}>{children}</AbsoluteFill>;
};

/** Un plano con su disolvencia de entrada hecha a mano. */
export const Plano: React.FC<{src: string; indice: number; foco?: string}> = ({
  src,
  indice,
  foco = "50% 50%",
}) => {
  const frame = useCurrentFrame();
  const opacity = indice === 0 ? 1 : interpolate(frame, [0, FADE], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{opacity}}>
      <OffthreadVideo
        src={src}
        muted
        style={{width: "100%", height: "100%", objectFit: "cover", objectPosition: foco}}
      />
    </AbsoluteFill>
  );
};

/** Velo de gradación: sin él el texto blanco se pierde en el cielo claro. */
export const Velo: React.FC<{arriba?: number; abajo?: number}> = ({arriba = 0.34, abajo = 0.42}) => (
  <AbsoluteFill
    style={{
      background: `linear-gradient(to bottom, rgba(6,14,20,${arriba}) 0%, rgba(6,14,20,0) 34%, rgba(6,14,20,0) 58%, rgba(6,14,20,${abajo}) 100%)`,
    }}
  />
);

type Pos = "arriba" | "centro" | "abajo";

/** Bloque de texto con entrada y salida por opacidad + un desplazamiento mínimo. */
export const Bloque: React.FC<{
  desde: number;
  dura: number;
  pos?: Pos;
  /** El cierre del reel NO se desvanece: queda fijo hasta el último fotograma,
   *  que es además el que la gente captura de pantalla. */
  sinSalida?: boolean;
  children: React.ReactNode;
}> = ({desde, dura, pos = "centro", sinSalida = false, children}) => {
  const frame = useCurrentFrame();
  const t = frame - desde;
  if (t < -2 || t > dura + 2) return null;
  const opacity = sinSalida
    ? interpolate(t, [0, 14], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})
    : interpolate(t, [0, 14, dura - 14, dura], [0, 1, 1, 0], {
        extrapolateLeft: "clamp",
        extrapolateRight: "clamp",
      });
  const y = interpolate(t, [0, 22], [16, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const justify = pos === "arriba" ? "flex-start" : pos === "abajo" ? "flex-end" : "center";
  return (
    <AbsoluteFill
      style={{
        paddingTop: SEGURO_SUP,
        paddingBottom: 1920 - SEGURO_INF,
        paddingLeft: 96,
        paddingRight: 96,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: justify,
        textAlign: "center",
        opacity,
        transform: `translateY(${y}px)`,
      }}
    >
      {children}
    </AbsoluteFill>
  );
};

export const HALO = "0 2px 26px rgba(0,0,0,0.52), 0 0 70px rgba(0,0,0,0.28)";

/**
 * ⛔ LA ESCALA (Diego, 23-09), la misma que las estáticas:
 *   · Inter Tight varía entre 50 y 70 pt según el LARGO de la frase.
 *   · IvyOra Display va a un tamaño FIJO.
 * `Pie` queda fuera: es la etiqueta en versales espaciadas, otro rol.
 */
export const SANS_MIN = 50;
export const SANS_MAX = 70;
export const IVY = 68;

export const cuerpoSans = (texto: string) => {
  const n = texto.replace(/\s+/g, " ").trim().length;
  const t = Math.min(Math.max((n - 24) / 72, 0), 1);
  return Math.round(SANS_MAX - t * (SANS_MAX - SANS_MIN));
};

const largoDe = (c: React.ReactNode): string =>
  typeof c === "string" ? c : Array.isArray(c) ? c.map(largoDe).join(" ") : "";

/** Línea narrativa: sans ligera en caja baja, como en el reel de septiembre. */
/**
 * ⛔ «TIERRA CALMA» NUNCA SE PARTE ENTRE DOS LÍNEAS (Diego, 24-09-2026).
 *
 * *"Para el reel del 01-10 hay que dejar en el primer frame la frase Tierra
 * Calma juntos en la misma línea **(siempre)**"*. El primer subtítulo salía
 * «La primavera ya llegó a Tierra / Calma».
 *
 * Se resuelve en el COMPONENTE y no llamada por llamada: con la escala
 * automática (`cuerpoSans`) el cuerpo cambia según el largo de la frase, así que
 * una línea que hoy cabe puede partirse mañana al editarle una palabra. Vale
 * igual para «Padre Hurtado», la otra unidad de dos palabras que aparece en casi
 * todas las piezas.
 */
const INDIVISIBLE = /(Tierra Calma|Padre Hurtado)/gi;

export const sinPartir = (hijos: React.ReactNode): React.ReactNode => {
  if (typeof hijos !== "string") return hijos;
  return hijos
    .split(INDIVISIBLE)
    .map((parte, i) =>
      /^(tierra calma|padre hurtado)$/i.test(parte) ? (
        <span key={i} style={{whiteSpace: "nowrap"}}>
          {parte}
        </span>
      ) : (
        parte
      ),
    );
};

export const Suave: React.FC<{size?: number; children: React.ReactNode}> = ({size, children}) => (
  <div
    style={{
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: size ?? cuerpoSans(largoDe(children)),
      lineHeight: 1.3,
      color: "#fff",
      textShadow: HALO,
      whiteSpace: "pre-line",
    }}
  >
    {sinPartir(children)}
  </div>
);

/** Línea enfática: IvyOra cursiva en versales. */
export const Enfasis: React.FC<{size?: number; children: React.ReactNode}> = ({size = IVY, children}) => (
  <div
    style={{
      fontFamily: SERIF,
      fontStyle: "italic",
      fontWeight: 500,
      fontSize: size,
      lineHeight: 1.14,
      color: "#fff",
      textTransform: "uppercase",
      textShadow: HALO,
      whiteSpace: "pre-line",
    }}
  >
    {sinPartir(children)}
  </div>
);

/** Versales espaciadas de pie, el remate del reel de septiembre. */
export const Pie: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      fontFamily: SANS,
      fontWeight: 500,
      fontSize: 27,
      letterSpacing: "0.26em",
      textTransform: "uppercase",
      color: "rgba(255,255,255,0.88)",
      textShadow: HALO,
    }}
  >
    {children}
  </div>
);

export const Aire: React.FC<{h: number}> = ({h}) => <div style={{height: h, flexShrink: 0}} />;

export const IconoWsp: React.FC<{s?: number}> = ({s = 54}) => (
  <svg width={s} height={s} viewBox="0 0 24 24" fill="none">
    <path
      d="M3.6 20.4l1.2-4a8.2 8.2 0 1 1 3.1 3l-4.3 1Z"
      stroke="#fff"
      strokeWidth="1.5"
      strokeLinejoin="round"
    />
    <path
      d="M9 9.2c0 3 2.4 5.3 5.3 5.3.5 0 .9-.4.9-.9v-1l-1.8-.6-.8.9a4.6 4.6 0 0 1-2-2l.9-.8L11 8.3h-1c-.5 0-1 .4-1 .9Z"
      fill="#fff"
    />
  </svg>
);

/**
 * Música de fondo con entrada, salida y ATENUACIÓN POR TRAMOS durante la
 * locución. Los tramos se declaran a mano: nada de ducking por envolvente
 * (memoria `audio-y-post-de-reels`).
 */
export const Musica: React.FC<{
  src: string;
  vol?: number;
  duracion: number;
  baja?: [number, number][];
  volBajo?: number;
}> = ({src, vol = 0.24, duracion, baja = [], volBajo = 0.1}) => (
  <Audio
    src={src}
    volume={(f) => {
      const entrada = interpolate(f, [0, 24], [0, 1], {
        extrapolateLeft: "clamp",
        extrapolateRight: "clamp",
      });
      const salida = interpolate(f, [duracion - 45, duracion], [1, 0], {
        extrapolateLeft: "clamp",
        extrapolateRight: "clamp",
      });
      const enVoz = baja.some(([a, b]) => f >= a - 12 && f <= b + 12);
      return vol * entrada * salida * (enVoz ? volBajo / vol : 1);
    }}
  />
);

// =============================================================================
// D · 01/10 · REEL "La primavera llegó a Tierra Calma" · Pilar 4
// Locución tranquila + subtítulos, como pide el brief. Voz chilena.
// =============================================================================

const VO: {archivo: string; desde: number; dura: number; texto: string}[] = [
  {archivo: "vo1", desde: 30, dura: 66, texto: "La primavera ya se instaló\nen Tierra Calma."},
  {archivo: "vo2", desde: 170, dura: 95, texto: "Más luz, más verde\ny más silencio alrededor."},
  {archivo: "vo3", desde: 310, dura: 66, texto: "Así empieza octubre\nen el sector."},
  {archivo: "vo4", desde: 450, dura: 117, texto: ""},
];

export const ReelPrimaveraOct: React.FC = () => (
  <Lienzo>
    <Sequence from={0} durationInFrames={CLIP_LEN}>
      <Plano src={CLIP("d1")} indice={0} foco="50% 45%" />
    </Sequence>
    <Sequence from={SLOT} durationInFrames={CLIP_LEN}>
      <Plano src={CLIP("d2")} indice={1} />
    </Sequence>
    <Sequence from={SLOT * 2} durationInFrames={CLIP_LEN}>
      <Plano src={CLIP("d3")} indice={2} />
    </Sequence>
    <Sequence from={SLOT * 3} durationInFrames={CLIP_LEN}>
      <Plano src={CLIP("d4")} indice={3} />
    </Sequence>

    <Velo arriba={0.3} abajo={0.46} />

    {/* Subtítulos: el brief los pide explícitamente junto con la locución. */}
    <Bloque desde={25} dura={95} pos="abajo">
      <Suave>{VO[0].texto}</Suave>
    </Bloque>
    <Bloque desde={165} dura={112} pos="abajo">
      <Enfasis size={58}>{"Más luz, más verde\ny más silencio alrededor."}</Enfasis>
    </Bloque>
    <Bloque desde={305} dura={92} pos="arriba">
      <Suave>{VO[2].texto}</Suave>
    </Bloque>

    {/* Cierre: wordmark en cursiva sobre el último plano, como en septiembre. */}
    <Bloque desde={445} dura={126} pos="centro" sinSalida>
      <Enfasis size={80}>Tierra Calma</Enfasis>
      <Aire h={22} />
      <Suave size={38}>Padre Hurtado · desde UF 2.500</Suave>
      <Aire h={54} />
      <Pie>Agenda tu visita</Pie>
    </Bloque>

    {VO.map((v) => (
      <Sequence key={v.archivo} from={v.desde} durationInFrames={v.dura + 10}>
        <Audio src={AUDIO(v.archivo)} volume={1} />
      </Sequence>
    ))}

    <Musica
      src={AUDIO("mus_ambient")}
      vol={0.26}
      duracion={REEL_DURATION}
      baja={VO.map((v) => [v.desde, v.desde + v.dura] as [number, number])}
      volBajo={0.09}
    />
  </Lienzo>
);

// =============================================================================
// I · 13/10 · REEL IA/DRON · 4 cortes con overlays · Pilar 4
// Los textos salen VERBATIM de la grilla. Sin locución: el brief no la pide.
// =============================================================================

export const ReelDronOct: React.FC = () => {
  const frame = useCurrentFrame();
  // Latido del ícono de WhatsApp del corte 4 ("ícono de WhatsApp animado").
  const pulso = 1 + Math.sin((frame - 435) / 7) * 0.05;
  return (
    <Lienzo>
      <Sequence from={0} durationInFrames={CLIP_LEN}>
        <Plano src={CLIP("i1")} indice={0} />
      </Sequence>
      <Sequence from={SLOT} durationInFrames={CLIP_LEN}>
        <Plano src={CLIP("i2")} indice={1} />
      </Sequence>
      <Sequence from={SLOT * 2} durationInFrames={CLIP_LEN}>
        <Plano src={CLIP("i3")} indice={2} />
      </Sequence>
      <Sequence from={SLOT * 3} durationInFrames={CLIP_LEN}>
        <Plano src={CLIP("i4")} indice={3} />
      </Sequence>

      <Velo arriba={0.36} abajo={0.44} />

      {/* Corte 1 · ubicación */}
      <Bloque desde={14} dura={118} pos="arriba">
        <Enfasis size={62}>{"A 15 min del peaje\nPadre Hurtado."}</Enfasis>
        <Aire h={18} />
        <Pie>Ruta 78 · Autopista del Sol</Pie>
      </Bloque>

      {/* Corte 2 · invitación */}
      <Bloque desde={154} dura={118} pos="abajo">
        <Suave size={48}>{"Escríbenos y coordina\ntu visita."}</Suave>
      </Bloque>

      {/* Corte 3 · el dato. La cifra es el elemento más grande de la pieza. */}
      <Bloque desde={294} dura={118} pos="arriba">
        <Pie>Tamaño real</Pie>
        <Aire h={20} />
        <Enfasis size={78}>{"~5.000 m² aprox."}</Enfasis>
        <Aire h={20} />
        <Suave size={42}>Desde UF 2.500</Suave>
      </Bloque>

      {/* Corte 4 · cierre con el ícono animado */}
      <Bloque desde={434} dura={135} pos="centro" sinSalida>
        <div style={{transform: `scale(${pulso})`}}>
          <IconoWsp s={58} />
        </div>
        <Aire h={30} />
        <Enfasis size={72}>Agenda tu visita.</Enfasis>
        <Aire h={46} />
        <Pie>Tierra Calma · Padre Hurtado</Pie>
      </Bloque>

      <Musica src={AUDIO("mus_instrumental")} vol={0.3} duracion={REEL_DURATION} />
    </Lienzo>
  );
};

// =============================================================================
// STORIES — éstas SÍ llevan el marco, porque son pieza de feed/story estática
// en movimiento, no reel.
// =============================================================================

const MarcoST: React.FC = () => (
  <img
    src={staticFile("assets/tierracalma/marcos/MARCO-ST.png")}
    style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "fill"}}
  />
);

const PildoraST: React.FC<{icono?: React.ReactNode; children: React.ReactNode}> = ({
  icono,
  children,
}) => (
  <div
    style={{
      position: "absolute",
      left: 237,
      top: 1584,
      width: 606,
      height: 73,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      gap: 14,
    }}
  >
    {icono}
    <span
      style={{
        fontFamily: SANS,
        fontWeight: 500,
        fontSize: 33,
        letterSpacing: "0.07em",
        color: "#fff",
        textTransform: "uppercase",
        whiteSpace: "nowrap",
      }}
    >
      {children}
    </span>
  </div>
);

// -----------------------------------------------------------------------------
// F · 08/10 · HISTORIA "Primavera en el sector" · Pilar 4
// El brief dice SIN texto en pantalla y SIN llamado a la acción: es mood puro.
// Por eso la píldora del marco lleva sólo la ubicación, que no es un CTA.
// -----------------------------------------------------------------------------

export const StoryPetalos: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(
    frame,
    [0, 18, STORY_DURATION - 20, STORY_DURATION],
    [0, 1, 1, 0],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp"},
  );
  return (
    <Lienzo>
      <AbsoluteFill style={{opacity}}>
        <OffthreadVideo
          src={CLIP("f1")}
          muted
          style={{width: "100%", height: "100%", objectFit: "cover"}}
        />
        <Velo arriba={0.3} abajo={0.34} />
        <MarcoST />
        <PildoraST>Tierra Calma · Padre Hurtado</PildoraST>
      </AbsoluteFill>
      <Musica src={AUDIO("mus_ambient")} vol={0.3} duracion={STORY_DURATION} />
    </Lienzo>
  );
};

// -----------------------------------------------------------------------------
// J · 15/10 · HISTORIA "Conoce Tierra Calma, agenda tu visita" · Pilar 2
// -----------------------------------------------------------------------------

export const StoryPov: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(
    frame,
    [0, 18, STORY_DURATION - 20, STORY_DURATION],
    [0, 1, 1, 0],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp"},
  );
  return (
    <Lienzo>
      <AbsoluteFill style={{opacity}}>
        <OffthreadVideo
          src={CLIP("j1")}
          muted
          style={{width: "100%", height: "100%", objectFit: "cover"}}
        />
        <Velo arriba={0.42} abajo={0.4} />
        <MarcoST />
        <Bloque desde={22} dura={STORY_DURATION - 50} pos="arriba">
          <Suave size={44}>Más cerca de Santiago</Suave>
          <Aire h={16} />
          <Enfasis size={62}>de lo que imaginas.</Enfasis>
        </Bloque>
        <PildoraST icono={<IconoWsp s={28} />}>Escríbenos al WhatsApp</PildoraST>
      </AbsoluteFill>
      <Musica src={AUDIO("mus_instrumental")} vol={0.28} duracion={STORY_DURATION} />
    </Lienzo>
  );
};

// =============================================================================
// I · 13/10 · REEL IA/DRON — **V2, ronda del cliente del 22-09-2026**
//
// ⛔ `ReelDronOct` (arriba) quedó SUPERADO. La grilla se modificó el 22-09 a las
// 15:43Z y cambió el texto de tres de los cuatro cortes: los mensajes del corte
// 1 y del corte 2 SE INTERCAMBIARON y el del 4 se alargó. Se deja la v1 en el
// archivo porque es lo que se entregó el 14-09 y permite comparar; lo que se
// publica es esta v2.
//
//   corte   14-09 (v1)                      22-09 (v2, vigente)
//   1       A 15 min del peaje…             Así se ve el camino hasta Tierra Calma.
//   2       Escríbenos y coordina tu visita. A 15 minutos del peaje Padre Hurtado.
//   3       Tamaño real ~5.000 m²…          ~5.000 m² aprox., desde UF 2.500.
//   4       Agenda tu visita.               Agenda tu visita y compruébalo en terreno.
//
// CADENA DE MODELOS PEDIDA POR EL DISEÑADOR (22-09):
//   imagen  → **Seedream 5 Pro** (9:16, 2k → 1440×2560)
//   video   → **Kling 3.0** (9:16, 1080p, fotograma de inicio)
//   música  → **ElevenLabs Music v2**, instrumental, 26 s
//
// Y el CIERRE ahora sí es el logo animado: el diseñador subió a Drive
// `TIERRA CALMA CIERRE.mov` el 22-09, que es byte a byte el mismo archivo que
// `TIERRA CALMA MOTION.mov` del KINGSTON (sha256 verificado). Queda zanjada la
// discrepancia que estaba anotada en la cabecera de este archivo.
// =============================================================================

const OUTRO = 150; // el logo animado dura 5 s a 30 fps
const SOLAPE_OUTRO = 15;
export const REEL_DRON_V2_DURATION = SLOT * 3 + CLIP_LEN - SOLAPE_OUTRO + OUTRO;

export const ReelDronOctV2: React.FC = () => {
  const frame = useCurrentFrame();
  const pulso = 1 + Math.sin((frame - 435) / 7) * 0.05;
  return (
    <Lienzo>
      <Sequence from={0} durationInFrames={CLIP_LEN}>
        <Plano src={CLIP("k1")} indice={0} />
      </Sequence>
      <Sequence from={SLOT} durationInFrames={CLIP_LEN}>
        <Plano src={CLIP("k2")} indice={1} />
      </Sequence>
      <Sequence from={SLOT * 2} durationInFrames={CLIP_LEN}>
        <Plano src={CLIP("k3")} indice={2} />
      </Sequence>
      <Sequence from={SLOT * 3} durationInFrames={CLIP_LEN}>
        <Plano src={CLIP("k4")} indice={3} />
      </Sequence>

      <Velo arriba={0.36} abajo={0.44} />

      {/* Corte 1 · el camino */}
      <Bloque desde={14} dura={118} pos="arriba">
        <Suave size={46}>Así se ve el camino</Suave>
        <Aire h={14} />
        <Enfasis size={66}>hasta Tierra Calma.</Enfasis>
      </Bloque>

      {/* Corte 2 · la distancia */}
      <Bloque desde={154} dura={118} pos="arriba">
        <Enfasis size={64}>{"A 15 minutos del peaje\nPadre Hurtado."}</Enfasis>
        <Aire h={18} />
        <Pie>Ruta 78 · Autopista del Sol</Pie>
      </Bloque>

      {/* Corte 3 · el dato. La cifra es el elemento más grande de la pieza. */}
      <Bloque desde={294} dura={118} pos="arriba">
        <Enfasis size={80}>{"~5.000 m² aprox.,"}</Enfasis>
        <Aire h={16} />
        <Suave size={46}>desde UF 2.500</Suave>
      </Bloque>

      {/* Corte 4 · cierre con el ícono animado */}
      <Bloque desde={434} dura={120} pos="centro">
        <div style={{transform: `scale(${pulso})`}}>
          <IconoWsp s={58} />
        </div>
        <Aire h={28} />
        {/* 54 px: a 62 la segunda linea se partia y dejaba "TERRENO." solo. */}
        <Enfasis size={54}>{"Agenda tu visita\ny compruébalo en terreno."}</Enfasis>
      </Bloque>

      {/* Cierre oficial: el logo animado del diseñador, sobre blanco. */}
      <Sequence
        from={SLOT * 3 + CLIP_LEN - SOLAPE_OUTRO}
        durationInFrames={OUTRO + SOLAPE_OUTRO}
      >
        <Plano src={staticFile("assets/tierracalma/tc_motion.mp4")} indice={1} />
      </Sequence>

      <Musica
        src={AUDIO("mus_dron_v2")}
        vol={0.32}
        duracion={REEL_DRON_V2_DURATION}
      />
    </Lienzo>
  );
};
