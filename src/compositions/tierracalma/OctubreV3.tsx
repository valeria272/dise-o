import React from "react";
import {AbsoluteFill, Img, Sequence, staticFile, useCurrentFrame} from "remotion";
import {tierracalma as TC, ensureTierraCalmaFonts} from "../../brand/tierracalma";

// =============================================================================
// TIERRA CALMA · OCTUBRE 2026 · V3 — la grilla del 22-09 (16:12Z)
//
// El cliente rehízo la grilla casi entera. Esta es la versión vigente y deja
// superadas Octubre.tsx (v1, 14-09) y la ronda de las 15:43 del 22-09.
//
// TODO EL COPY SALE VERBATIM DE LA GRILLA. Único arreglo: la grilla escribe
// "la de tus visita"; va "visitas".
//
// ⚠️ "Rol individual" y "Acceso controlado" NO están en la lista blanca del
// manual y la propia nota de datos comerciales de la grilla tampoco los
// incluye. Entran por decisión de Diego (22-09) y SIGUEN SIN confirmación
// escrita de Fran o Blanca. Si alguien los cuestiona, es acá.
//
// LAS IMÁGENES SIGUEN EL ADN CORREGIDO (manual § 4 bis): cerros áridos ocre,
// matorral espinoso ralo, ripio anaranjado, cerco de madera oscura. Las piezas
// que dicen "fotografía real" usan foto REAL del sitio, no IA.
// =============================================================================

const OCT = (n: string) => staticFile(`assets/tierracalma/oct/${n}.jpg`);
const MARCO = (n: string) => staticFile(`assets/tierracalma/marcos/${n}.png`);
const SANS = TC.fonts.body;
const SERIF = TC.fonts.display;

// Geometría medida sobre los PNG del diseñador — ver manual § 4 quinquies.
const POST = {w: 1080, h: 1350, texto: 250, pill: {x: 264, y: 1212, w: 540, h: 53}};
const STORY = {w: 1080, h: 1920, texto: 245, pill: {x: 237, y: 1584, w: 606, h: 73}};
const CARR = {w: 1080, h: 1350, conLogo: 250, sinLogo: 205};

// -----------------------------------------------------------------------------
// Primitivas (las mismas que la v1 — el sistema no cambió, cambió el copy)
// -----------------------------------------------------------------------------

const Lienzo: React.FC<{w: number; h: number; children: React.ReactNode}> = ({w, h, children}) => {
  ensureTierraCalmaFonts();
  return (
    <AbsoluteFill style={{width: w, height: h, backgroundColor: TC.colors.ink, overflow: "hidden"}}>
      {children}
    </AbsoluteFill>
  );
};

const Foto: React.FC<{src: string; foco?: string}> = ({src, foco = "50% 50%"}) => (
  <Img
    src={src}
    style={{
      position: "absolute",
      inset: 0,
      width: "100%",
      height: "100%",
      objectFit: "cover",
      objectPosition: foco,
    }}
  />
);

/** Contraste por degradado + velo parejo. Nunca caja opaca (regla del brief). */
const Degradado: React.FC<{arriba?: number; abajo?: number; velo?: number}> = ({
  arriba = 0.62,
  abajo = 0.5,
  velo = 0.13,
}) => (
  <>
    <AbsoluteFill
      style={{
        background: `linear-gradient(to bottom, rgba(6,14,20,${arriba}) 0%, rgba(6,14,20,${
          arriba * 0.45
        }) 32%, rgba(6,14,20,0) 55%, rgba(6,14,20,${abajo * 0.5}) 82%, rgba(6,14,20,${abajo}) 100%)`,
      }}
    />
    <AbsoluteFill style={{backgroundColor: `rgba(6,14,20,${velo})`}} />
  </>
);

const Marco: React.FC<{archivo: string}> = ({archivo}) => (
  <Img
    src={MARCO(archivo)}
    style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "fill"}}
  />
);

const Cuerpo: React.FC<{
  top: number;
  ancho?: number;
  alinea?: "center" | "flex-start";
  children: React.ReactNode;
}> = ({top, ancho = 820, alinea = "center", children}) => (
  <div
    style={{
      position: "absolute",
      top,
      left: "50%",
      transform: "translateX(-50%)",
      width: ancho,
      display: "flex",
      flexDirection: "column",
      alignItems: alinea,
      textAlign: alinea === "center" ? "center" : "left",
    }}
  >
    {children}
  </div>
);

const Ligera: React.FC<{size?: number; children: React.ReactNode}> = ({size = 66, children}) => (
  <div
    style={{
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: size,
      lineHeight: 1.14,
      letterSpacing: "0.005em",
      color: "#fff",
      textTransform: "uppercase",
      textShadow: "0 2px 22px rgba(0,0,0,0.42)",
      whiteSpace: "pre-line",
    }}
  >
    {children}
  </div>
);

const Remate: React.FC<{size?: number; children: React.ReactNode}> = ({size = 86, children}) => (
  <div
    style={{
      fontFamily: SERIF,
      fontStyle: "italic",
      fontWeight: 500,
      fontSize: size,
      lineHeight: 1.04,
      color: "#fff",
      textTransform: "uppercase",
      textShadow: "0 2px 24px rgba(0,0,0,0.45)",
      whiteSpace: "pre-line",
    }}
  >
    {children}
  </div>
);

const Bajada: React.FC<{size?: number; ancho?: number; children: React.ReactNode}> = ({
  size = 36,
  ancho,
  children,
}) => (
  <div
    style={{
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: size,
      lineHeight: 1.36,
      color: "rgba(255,255,255,0.9)",
      textShadow: "0 2px 16px rgba(0,0,0,0.5)",
      maxWidth: ancho,
      whiteSpace: "pre-line",
    }}
  >
    {children}
  </div>
);

/** Caja de color de marca — así "varía con los colores" que pidió el diseñador. */
const Caja: React.FC<{color: string; size?: number; children: React.ReactNode}> = ({
  color,
  size = 46,
  children,
}) => (
  <div
    style={{
      backgroundColor: color,
      borderRadius: 20,
      padding: "18px 34px",
      fontFamily: SANS,
      fontWeight: 500,
      fontSize: size,
      lineHeight: 1.18,
      color: "#fff",
      textTransform: "uppercase",
      whiteSpace: "pre-line",
    }}
  >
    {children}
  </div>
);

const Aire: React.FC<{h: number}> = ({h}) => <div style={{height: h, flexShrink: 0}} />;

// --- iconos de línea (nunca emoji en pieza de marca) --------------------------
type Ico = {s?: number; c?: string};
const Svg: React.FC<{s: number; children: React.ReactNode}> = ({s, children}) => (
  <svg width={s} height={s} viewBox="0 0 24 24" fill="none" style={{flexShrink: 0}}>
    {children}
  </svg>
);
const IPin: React.FC<Ico> = ({s = 26, c = "#fff"}) => (
  <Svg s={s}>
    <path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11Z" stroke={c} strokeWidth="1.6" strokeLinejoin="round" />
    <circle cx="12" cy="10" r="2.6" stroke={c} strokeWidth="1.6" />
  </Svg>
);
const IWsp: React.FC<Ico> = ({s = 26, c = "#fff"}) => (
  <Svg s={s}>
    <path d="M3.6 20.4l1.2-4a8.2 8.2 0 1 1 3.1 3l-4.3 1Z" stroke={c} strokeWidth="1.6" strokeLinejoin="round" />
    <path
      d="M9 9.2c0 3 2.4 5.3 5.3 5.3.5 0 .9-.4.9-.9v-1l-1.8-.6-.8.9a4.6 4.6 0 0 1-2-2l.9-.8L11 8.3h-1c-.5 0-1 .4-1 .9Z"
      fill={c}
    />
  </Svg>
);
const ICheck: React.FC<Ico> = ({s = 26, c = "#fff"}) => (
  <Svg s={s}>
    <circle cx="12" cy="12" r="9.2" stroke={c} strokeWidth="1.5" />
    <path d="M8 12.3l2.7 2.7L16 9.6" stroke={c} strokeWidth="1.9" strokeLinecap="round" strokeLinejoin="round" />
  </Svg>
);
const IRuta: React.FC<Ico> = ({s = 26, c = "#fff"}) => (
  <Svg s={s}>
    <path d="M4 20c4 0 4-8 8-8s4-8 8-8" stroke={c} strokeWidth="1.6" strokeLinecap="round" />
    <circle cx="4" cy="20" r="1.8" stroke={c} strokeWidth="1.6" />
    <circle cx="20" cy="4" r="1.8" stroke={c} strokeWidth="1.6" />
  </Svg>
);
const ITienda: React.FC<Ico> = ({s = 26, c = "#fff"}) => (
  <Svg s={s}>
    <path d="M4 9h16l-1 11H5L4 9Z" stroke={c} strokeWidth="1.6" strokeLinejoin="round" />
    <path d="M9 9V6a3 3 0 1 1 6 0v3" stroke={c} strokeWidth="1.6" strokeLinecap="round" />
  </Svg>
);
const IDoc: React.FC<Ico> = ({s = 26, c = "#fff"}) => (
  <Svg s={s}>
    <path d="M6 3h8l4 4v14H6V3Z" stroke={c} strokeWidth="1.6" strokeLinejoin="round" />
    <path d="M9 12h6M9 16h6" stroke={c} strokeWidth="1.6" strokeLinecap="round" />
  </Svg>
);
const IRegla: React.FC<Ico> = ({s = 26, c = "#fff"}) => (
  <Svg s={s}>
    <rect x="3" y="8" width="18" height="8" rx="1.6" stroke={c} strokeWidth="1.6" />
    <path d="M7 8v3M11 8v4M15 8v3M19 8v4" stroke={c} strokeWidth="1.6" strokeLinecap="round" />
  </Svg>
);

/** Texto DENTRO del contorno de píldora que ya trae el marco. */
const Pildora: React.FC<{
  caja: {x: number; y: number; w: number; h: number};
  icono?: React.ReactNode;
  size?: number;
  children: React.ReactNode;
}> = ({caja, icono, size = 30, children}) => (
  <div
    style={{
      position: "absolute",
      left: caja.x,
      top: caja.y,
      width: caja.w,
      height: caja.h,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      gap: 13,
    }}
  >
    {icono}
    <span
      style={{
        fontFamily: SANS,
        fontWeight: 500,
        fontSize: size,
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

/** Tarjeta de vidrio — el recurso de mockup del lenguaje de septiembre. */
const Vidrio: React.FC<{
  x?: number;
  y: number;
  w: number;
  rot?: number;
  pad?: string;
  children: React.ReactNode;
}> = ({x, y, w, rot = 0, pad = "28px 32px", children}) => (
  <div
    style={{
      position: "absolute",
      left: x ?? (1080 - w) / 2,
      top: y,
      width: w,
      transform: `rotate(${rot}deg)`,
      background: "linear-gradient(150deg, rgba(255,255,255,0.36), rgba(255,255,255,0.18))",
      border: "1.5px solid rgba(255,255,255,0.5)",
      borderRadius: 30,
      padding: pad,
      backdropFilter: "blur(22px)",
      WebkitBackdropFilter: "blur(22px)",
      boxShadow: "0 26px 60px rgba(0,0,0,0.3)",
    }}
  >
    {children}
  </div>
);

/** Fila de bloque de valor: ícono + texto, alineada a la izquierda. */
const Fila: React.FC<{icono: React.ReactNode; children: React.ReactNode; size?: number}> = ({
  icono,
  children,
  size = 33,
}) => (
  <div style={{display: "flex", alignItems: "center", gap: 16, marginBottom: 14}}>
    {icono}
    <span style={{fontFamily: SANS, fontWeight: 300, fontSize: size, color: "#fff", lineHeight: 1.3}}>
      {children}
    </span>
  </div>
);

/** Globo de conversación blanco, con la colita hacia el lado que se indique. */
const Globo: React.FC<{
  x: number;
  y: number;
  w: number;
  cola: "izq" | "der";
  children: React.ReactNode;
}> = ({x, y, w, cola, children}) => (
  <div style={{position: "absolute", left: x, top: y, width: w}}>
    <div
      style={{
        backgroundColor: "#fff",
        borderRadius: 34,
        padding: "26px 32px",
        fontFamily: SANS,
        fontWeight: 400,
        fontSize: 38,
        lineHeight: 1.3,
        color: TC.colors.ink,
        boxShadow: "0 18px 44px rgba(0,0,0,0.26)",
      }}
    >
      {children}
    </div>
    <div
      style={{
        position: "absolute",
        bottom: -14,
        [cola === "izq" ? "left" : "right"]: 44,
        width: 30,
        height: 22,
        backgroundColor: "#fff",
        clipPath: cola === "izq" ? "polygon(0 0, 100% 0, 30% 100%)" : "polygon(0 0, 100% 0, 70% 100%)",
      } as React.CSSProperties}
    />
  </div>
);

// =============================================================================
// E · 06/10 · CARRUSEL 4 SLIDES · dudas resueltas · Pilar 1
//
// ⭐ REFERENCIA (Pinterest, la pasó Diego el 22-09): pieza de SPACIO HOME,
// 1080×1350. Lo que se toma de ella —y sólo eso, el marco y la paleta no se
// tocan—:
//
//   1. TITULAR MODULADO: la frase cambia de peso y de estilo dentro de sí
//      misma. Sans ligera → una palabra en BOLD → el remate en cursiva serif
//      a una escala mucho mayor (en la referencia, ~2× el resto).
//   2. LA RESPUESTA EN TARJETA: caja de esquinas muy redondeadas, color de
//      marca sólido, anclada a un costado abajo — no centrada. Texto sans
//      regular en caja baja, tres líneas cortas.
//   3. Jerarquía por CONTRASTE DE TAMAÑO, no por color: el ojo cae primero en
//      la palabra cursiva enorme y después baja a la tarjeta.
//
// El brief manda el QUÉ (los textos van verbatim de la grilla) y la
// referencia el CÓMO. Memoria `leer-el-brief-y-su-carpeta-de-referencias`.
// =============================================================================

/** Un tramo del titular modulado: hereda el tamaño salvo que se le dé otro. */
type Tramo = {t: string; peso?: number; size?: number; cursiva?: boolean; salto?: boolean};

/**
 * Titular de pesos mezclados, a la manera de la referencia. Se compone en
 * línea (inline) para que "¿Tengo que invertir en la ELECTRIFICACIÓN del
 * terreno?" fluya como una sola frase y no como bloques apilados.
 */
const Modulado: React.FC<{tramos: Tramo[]; base?: number; ancho?: number}> = ({
  tramos,
  base = 52,
  ancho = 860,
}) => (
  <div
    style={{
      width: ancho,
      textAlign: "center",
      color: "#fff",
      lineHeight: 1.1,
      textShadow: "0 2px 24px rgba(0,0,0,0.5)",
    }}
  >
    {tramos.map((tr, i) => (
      <React.Fragment key={i}>
        {tr.salto ? <br /> : null}
        <span
          style={{
            fontFamily: tr.cursiva ? SERIF : SANS,
            fontStyle: tr.cursiva ? "italic" : "normal",
            fontWeight: tr.peso ?? (tr.cursiva ? 500 : 300),
            fontSize: tr.size ?? base,
            letterSpacing: tr.cursiva ? "0.004em" : "0.005em",
          }}
        >
          {tr.t}
        </span>
      </React.Fragment>
    ))}
  </div>
);

/** La tarjeta de la referencia: esquinas muy redondeadas, anclada a un costado. */
const Tarjeta: React.FC<{
  color: string;
  y: number;
  lado?: "der" | "izq";
  w?: number;
  size?: number;
  children: React.ReactNode;
}> = ({color, y, lado = "der", w = 520, size = 38, children}) => (
  <div
    style={{
      position: "absolute",
      top: y,
      [lado === "der" ? "right" : "left"]: 120,
      width: w,
      backgroundColor: color,
      borderRadius: 30,
      padding: "34px 40px",
      fontFamily: SANS,
      fontWeight: 400,
      fontSize: size,
      lineHeight: 1.26,
      color: "#fff",
      boxShadow: "0 20px 46px rgba(0,0,0,0.3)",
      whiteSpace: "pre-line",
    } as React.CSSProperties}
  >
    {children}
  </div>
);

const E1: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("e-portada")} foco="50% 55%" />
    <Degradado arriba={0.6} abajo={0.4} />
    <Marco archivo="MARCO-CARRUSEL-1" />
    <Cuerpo top={CARR.conLogo} ancho={880}>
      <Modulado
        base={54}
        ancho={880}
        tramos={[
          {t: "¿Dudas antes de "},
          {t: "comprar", peso: 600},
          // salto deliberado: sin él "parcela?" quedaba sola en la segunda línea
          {t: "tu parcela?", salto: true},
        ]}
      />
      <Aire h={26} />
      {/* El remate a gran escala: es lo que hace la referencia con "resultado". */}
      <Modulado base={54} ancho={900} tramos={[{t: "Aquí las resolvemos", cursiva: true, size: 104}]} />
    </Cuerpo>
  </Lienzo>
);

const E2: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("e-luz")} foco="50% 52%" />
    <Degradado arriba={0.58} abajo={0.42} />
    <Marco archivo="MARCO-CARRUSEL-2" />
    <Cuerpo top={CARR.sinLogo} ancho={880}>
      <Modulado
        base={48}
        ancho={880}
        tramos={[
          {t: "¿Tengo que invertir en la "},
          {t: "electrificación", peso: 600, size: 62},
          {t: " del terreno?"},
        ]}
      />
    </Cuerpo>
    <Tarjeta color={TC.colors.olive} y={880}>
      {"No, la electricidad\nsubterránea ya está\ninstalada."}
    </Tarjeta>
  </Lienzo>
);

const E3: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("e-cierre")} foco="50% 50%" />
    <Degradado arriba={0.58} abajo={0.42} />
    <Marco archivo="MARCO-CARRUSEL-3" />
    <Cuerpo top={CARR.sinLogo} ancho={880}>
      <Modulado
        base={52}
        ancho={880}
        tramos={[
          {t: "¿Tengo que "},
          {t: "cerrar", peso: 600, size: 66},
          {t: " yo el terreno?"},
        ]}
      />
    </Cuerpo>
    <Tarjeta color={TC.colors.brown} y={880} lado="izq">
      {"No, el cierre\nperimetral ya\nestá hecho."}
    </Tarjeta>
  </Lienzo>
);

const E4: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("e-casas")} foco="50% 54%" />
    <Degradado arriba={0.6} abajo={0.56} />
    <Marco archivo="MARCO-CARRUSEL-4" />
    <Cuerpo top={CARR.sinLogo} ancho={880}>
      <Modulado
        base={50}
        ancho={880}
        tramos={[
          {t: "¿Cuántas "},
          {t: "casas", peso: 600, size: 64},
          {t: " puedo construir?"},
        ]}
      />
      <Aire h={24} />
      <Modulado base={50} ancho={900} tramos={[{t: "Hasta dos por parcela", cursiva: true, size: 84}]} />
    </Cuerpo>
    <Tarjeta color={TC.colors.slate} y={900} w={500} size={36}>
      {"La tuya y la de\ntus visitas."}
    </Tarjeta>
    <div
      style={{
        position: "absolute",
        left: "50%",
        top: 1150,
        transform: "translateX(-50%)",
        display: "flex",
        alignItems: "center",
        gap: 13,
        border: "1.5px solid rgba(255,255,255,0.85)",
        borderRadius: 999,
        padding: "16px 36px",
      }}
    >
      <IPin s={25} />
      <span
        style={{
          fontFamily: SANS,
          fontWeight: 500,
          fontSize: 27,
          letterSpacing: "0.07em",
          color: "#fff",
          textTransform: "uppercase",
          whiteSpace: "nowrap",
        }}
      >
        Tu parcela en Padre Hurtado espera por ti
      </span>
    </div>
  </Lienzo>
);

// =============================================================================
// F · 08/10 · HISTORIA · "¿Buscando una parcela en Padre Hurtado?" · Pilar 4
// El brief pide FOTOGRAFÍA REAL: acá va foto del sitio, no IA.
// =============================================================================

const F: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <Foto src={OCT("f-real")} foco="50% 45%" />
    <Degradado arriba={0.55} abajo={0.52} />
    <Marco archivo="MARCO-ST" />
    <Cuerpo top={STORY.texto} ancho={840}>
      <Ligera size={50}>{"¿Buscando una parcela\nen Padre Hurtado?"}</Ligera>
      <Aire h={20} />
      <Remate size={62}>{"La mejor forma de saber\nsi es para ti es venir\na conocerla."}</Remate>
    </Cuerpo>
    <Vidrio y={1080} w={760} pad="34px 40px">
      <Fila icono={<IPin s={30} />}>Recorre las parcelas disponibles</Fila>
      <Fila icono={<IRuta s={30} />}>Conoce el entorno y accesos</Fila>
      <Fila icono={<IWsp s={30} />}>Resuelve tus dudas sobre el proceso de compra</Fila>
      <div style={{height: 1, backgroundColor: "rgba(255,255,255,0.35)", margin: "10px 0 16px"}} />
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 500,
          fontSize: 26,
          letterSpacing: "0.18em",
          textTransform: "uppercase",
          color: "rgba(255,255,255,0.88)",
        }}
      >
        Padre Hurtado · RM
      </div>
    </Vidrio>
    <Pildora caja={STORY.pill} icono={<IWsp s={28} />} size={31}>
      Agenda tu visita
    </Pildora>
  </Lienzo>
);

// =============================================================================
// G · 09/10 · POST 4:5 · fin de semana largo · dos globos · Pilar 2
// =============================================================================

const G: React.FC = () => (
  <Lienzo w={POST.w} h={POST.h}>
    <Foto src={OCT("g-pareja")} foco="50% 58%" />
    <Degradado arriba={0.44} abajo={0.46} velo={0.1} />
    <Marco archivo="MARCO-POST" />
    <Globo x={112} y={270} w={600} cola="izq">
      ¿Qué hacemos este fin de semana largo?
    </Globo>
    <Globo x={368} y={470} w={620} cola="der">
      Vamos a conocer esa parcela que tenemos guardada
    </Globo>
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 1108,
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 500,
        fontSize: 29,
        letterSpacing: "0.2em",
        textTransform: "uppercase",
        color: "rgba(255,255,255,0.92)",
        textShadow: "0 2px 18px rgba(0,0,0,0.5)",
      }}
    >
      Tierra Calma · Padre Hurtado
    </div>
    <Pildora caja={POST.pill} icono={<IWsp s={25} />} size={29}>
      Agenda tu visita por WhatsApp
    </Pildora>
  </Lienzo>
);

// =============================================================================
// H · 12/10 · HISTORIA · mapa azul Santiago → Padre Hurtado · Pilar 2
// El mapa se dibuja en SVG: los PNG de MAPAS traen topónimos corruptos.
// =============================================================================

const MapaAzul: React.FC = () => (
  <svg width={1080} height={470} viewBox="0 0 1080 470" style={{position: "absolute", top: 640, left: 0}}>
    {/* retícula tenue */}
    {Array.from({length: 11}).map((_, i) => (
      <line key={`v${i}`} x1={i * 108} y1={0} x2={i * 108} y2={470} stroke="rgba(255,255,255,0.06)" strokeWidth="1" />
    ))}
    {Array.from({length: 5}).map((_, i) => (
      <line key={`h${i}`} x1={0} y1={i * 108} x2={1080} y2={i * 108} stroke="rgba(255,255,255,0.06)" strokeWidth="1" />
    ))}
    {/* la Ruta 78 */}
    <path
      d="M 838 96 C 706 168, 566 240, 402 336"
      stroke={TC.colors.sand}
      strokeWidth="5"
      fill="none"
      strokeLinecap="round"
      strokeDasharray="1 0"
    />
    {/* Santiago */}
    <circle cx="838" cy="96" r="13" fill="rgba(255,255,255,0.9)" />
    <text
      x="806"
      y="58"
      textAnchor="end"
      fill="#fff"
      style={{fontFamily: SANS, fontSize: 40, fontWeight: 300, letterSpacing: "0.1em"}}
    >
      SANTIAGO
    </text>
    {/* etiqueta de la ruta */}
    <text
      x="634"
      y="242"
      textAnchor="middle"
      fill={TC.colors.sand}
      style={{fontFamily: SANS, fontSize: 26, fontWeight: 500, letterSpacing: "0.22em"}}
    >
      RUTA 78
    </text>
    {/* Tierra Calma — pin */}
    <path
      d="M402 336 c 0 0 26 -24 26 -44 a 26 26 0 1 0 -52 0 c 0 20 26 44 26 44 Z"
      transform="translate(0,-2)"
      fill="#fff"
    />
    <circle cx="402" cy="292" r="9" fill={TC.colors.navy} />
    <text
      x="442"
      y="304"
      fill="#fff"
      style={{fontFamily: SERIF, fontSize: 46, fontStyle: "italic", fontWeight: 500}}
    >
      Tierra Calma
    </text>
    <text
      x="442"
      y="342"
      fill="rgba(255,255,255,0.8)"
      style={{fontFamily: SANS, fontSize: 25, fontWeight: 400, letterSpacing: "0.18em"}}
    >
      PADRE HURTADO
    </text>
  </svg>
);

const H: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <AbsoluteFill style={{backgroundColor: TC.colors.navy}} />
    <MapaAzul />
    {/* la foto editorial, abajo */}
    <div style={{position: "absolute", left: 0, right: 0, top: 1120, height: 720, overflow: "hidden"}}>
      <Img src={OCT("h-casa")} style={{width: "100%", height: "100%", objectFit: "cover"}} />
      <AbsoluteFill
        style={{
          background: `linear-gradient(to bottom, ${TC.colors.navy} 0%, rgba(11,44,73,0) 22%, rgba(11,44,73,0) 62%, rgba(11,44,73,0.92) 100%)`,
        }}
      />
    </div>
    <Marco archivo="MARCO-ST" />
    <Cuerpo top={STORY.texto} ancho={860}>
      <Remate size={60}>{"Cerca de Santiago.\nMás cerca de\nla tranquilidad."}</Remate>
    </Cuerpo>
    <div style={{position: "absolute", left: 0, right: 0, top: 486, padding: "0 130px", textAlign: "center"}}>
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 300,
          fontSize: 33,
          lineHeight: 1.36,
          color: "rgba(255,255,255,0.92)",
          textShadow: "0 2px 16px rgba(0,0,0,0.55)",
        }}
      >
        Padre Hurtado te permite seguir conectado con la ciudad, con el espacio y la calma que buscas
        para vivir.
      </div>
    </div>
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 1462,
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 500,
        fontSize: 30,
        letterSpacing: "0.13em",
        textTransform: "uppercase",
        color: TC.colors.sand,
        textShadow: "0 2px 18px rgba(0,0,0,0.75)",
      }}
    >
      Parcelas de aprox. 5.000 m² desde UF 2.500
    </div>
    <Pildora caja={STORY.pill} icono={<IPin s={28} />} size={31}>
      Conoce el proyecto
    </Pildora>
  </Lienzo>
);

// =============================================================================
// J · 15/10 · HISTORIA · "Eso que estabas buscando" · buscador · Pilar 2
// =============================================================================

const Sugerida: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      display: "flex",
      alignItems: "center",
      gap: 14,
      padding: "16px 4px",
      borderTop: "1px solid rgba(255,255,255,0.22)",
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: 31,
      color: "rgba(255,255,255,0.94)",
    }}
  >
    <svg width={22} height={22} viewBox="0 0 24 24" fill="none" style={{flexShrink: 0, opacity: 0.8}}>
      <circle cx="11" cy="11" r="6.6" stroke="#fff" strokeWidth="1.6" />
      <path d="M16 16l4.5 4.5" stroke="#fff" strokeWidth="1.6" strokeLinecap="round" />
    </svg>
    {children}
  </div>
);

const J: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <Foto src={OCT("j-real")} foco="50% 48%" />
    <Degradado arriba={0.5} abajo={0.5} />
    <Marco archivo="MARCO-ST" />

    {/* barra de búsqueda */}
    <Vidrio y={300} w={820} pad="26px 30px">
      <div style={{display: "flex", alignItems: "center", gap: 18}}>
        <svg width={32} height={32} viewBox="0 0 24 24" fill="none" style={{flexShrink: 0}}>
          <circle cx="11" cy="11" r="6.6" stroke="#fff" strokeWidth="1.7" />
          <path d="M16 16l4.5 4.5" stroke="#fff" strokeWidth="1.7" strokeLinecap="round" />
        </svg>
        <span style={{fontFamily: SANS, fontWeight: 400, fontSize: 33, color: "#fff", lineHeight: 1.25}}>
          ¿Dónde vivir con más espacio cerca de Santiago?
        </span>
      </div>
    </Vidrio>

    {/* búsquedas sugeridas */}
    <Vidrio y={490} w={820} pad="12px 30px 20px">
      <Sugerida>Más naturaleza sin alejarme de la ciudad</Sugerida>
      <Sugerida>Un lugar tranquilo para construir mi casa</Sugerida>
      <Sugerida>Parcelas en Padre Hurtado</Sugerida>
    </Vidrio>

    {/* tarjeta de resultado */}
    <Vidrio y={1120} w={820} pad="28px 30px">
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 500,
          fontSize: 24,
          letterSpacing: "0.2em",
          textTransform: "uppercase",
          color: "rgba(255,255,255,0.75)",
          marginBottom: 16,
        }}
      >
        Resultado
      </div>
      <div style={{display: "flex", alignItems: "center", gap: 22}}>
        <Img
          src={OCT("l-real")}
          style={{width: 150, height: 150, objectFit: "cover", borderRadius: 22, flexShrink: 0}}
        />
        <div>
          <div style={{fontFamily: SERIF, fontStyle: "italic", fontWeight: 500, fontSize: 52, color: "#fff"}}>
            Tierra Calma
          </div>
          <div style={{fontFamily: SANS, fontWeight: 300, fontSize: 28, color: "rgba(255,255,255,0.88)"}}>
            Padre Hurtado · Región Metropolitana
          </div>
          <div style={{fontFamily: SANS, fontWeight: 400, fontSize: 30, color: "#fff", marginTop: 10}}>
            El espacio que estabas buscando.
          </div>
        </div>
      </div>
    </Vidrio>

    <Pildora caja={STORY.pill} icono={<IPin s={28} />} size={31}>
      Conoce Tierra Calma
    </Pildora>
  </Lienzo>
);

// =============================================================================
// K · 20/10 · CARRUSEL 6 SLIDES · "qué revisar antes de elegir" · Pilar 2
// El marco de carrusel es de 4 piezas: slide 1 cierra a la izquierda, 2-5 son
// bandas (el mismo dibujo) y el 6 cierra a la derecha. Por eso escala a 6.
// =============================================================================

const Numero: React.FC<{n: string}> = ({n}) => (
  <div
    style={{
      fontFamily: SERIF,
      fontStyle: "italic",
      fontWeight: 400,
      fontSize: 64,
      color: TC.colors.sand,
      lineHeight: 1,
      textShadow: "0 2px 18px rgba(0,0,0,0.5)",
    }}
  >
    {n}
  </div>
);

const K1: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("k-persona")} foco="50% 55%" />
    <Degradado arriba={0.64} abajo={0.36} />
    <Marco archivo="MARCO-CARRUSEL-1" />
    <Cuerpo top={CARR.conLogo} ancho={880}>
      <Ligera size={58}>{"¿Estás pensando en\ncomprar una parcela?"}</Ligera>
      <Aire h={22} />
      <Remate size={68}>{"No mires solo\nlos m²."}</Remate>
      <Aire h={22} />
      <Bajada size={35} ancho={760}>
        Hay otros aspectos que deberías considerar antes de decidir.
      </Bajada>
    </Cuerpo>
  </Lienzo>
);

const K2: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("k-aerea")} foco="50% 50%" />
    <Degradado arriba={0.66} abajo={0.4} />
    <Marco archivo="MARCO-CARRUSEL-2" />
    <Cuerpo top={CARR.sinLogo} ancho={880}>
      <Numero n="01." />
      <Aire h={16} />
      <Ligera size={56}>{"¿Qué tan\nconectado estarás?"}</Ligera>
      <Aire h={24} />
      <Bajada size={35} ancho={790}>
        Revisa accesos, vías principales y qué tan fácil será mantener tu rutina desde tu nueva
        ubicación.
      </Bajada>
      <Aire h={26} />
      <div style={{display: "flex", alignItems: "center", gap: 13}}>
        <IPin s={26} />
        <span
          style={{
            fontFamily: SANS,
            fontWeight: 500,
            fontSize: 28,
            letterSpacing: "0.14em",
            textTransform: "uppercase",
            color: TC.colors.sand,
          }}
        >
          Tierra Calma está en Padre Hurtado, RM
        </span>
      </div>
    </Cuerpo>
  </Lienzo>
);

const K3: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("f-real")} foco="50% 50%" />
    <Degradado arriba={0.68} abajo={0.46} />
    <Marco archivo="MARCO-CARRUSEL-3" />
    <Cuerpo top={CARR.sinLogo} ancho={880}>
      <Numero n="02." />
      <Aire h={16} />
      <Ligera size={58}>{"¿Qué tienes cerca?"}</Ligera>
      <Aire h={26} />
      <div style={{display: "flex", gap: 14, flexWrap: "wrap", justifyContent: "center", maxWidth: 840}}>
        {[
          [<ITienda key="a" s={26} />, "Supermercados"],
          [<ICheck key="b" s={26} />, "Salud"],
          [<IDoc key="c" s={26} />, "Colegios"],
          [<ITienda key="d" s={26} />, "Comercio"],
        ].map(([ico, txt], i) => (
          <div
            key={i}
            style={{
              display: "flex",
              alignItems: "center",
              gap: 11,
              border: "1.5px solid rgba(255,255,255,0.8)",
              borderRadius: 999,
              padding: "12px 26px",
              fontFamily: SANS,
              fontWeight: 500,
              fontSize: 28,
              letterSpacing: "0.06em",
              textTransform: "uppercase",
              color: "#fff",
            }}
          >
            {ico}
            {txt as string}
          </div>
        ))}
      </div>
      <Aire h={26} />
      <Bajada size={35} ancho={800}>
        Pueden hacer una gran diferencia en tu día a día. Tranquilidad no debería significar
        aislamiento.
      </Bajada>
    </Cuerpo>
  </Lienzo>
);

const K4: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("e-cierre")} foco="50% 52%" />
    <Degradado arriba={0.68} abajo={0.42} />
    <Marco archivo="MARCO-CARRUSEL-2" />
    <Cuerpo top={CARR.sinLogo} ancho={880}>
      <Numero n="03." />
      <Aire h={16} />
      <Ligera size={52}>{"¿Qué incluye\nrealmente tu parcela?"}</Ligera>
      <Aire h={28} />
      {/* ⚠️ "Rol individual" y "Acceso controlado" van con el OK de Diego (22-09)
          y siguen sin confirmación escrita de Fran/Blanca — ver cabecera. */}
      <div style={{display: "flex", flexDirection: "column", alignItems: "flex-start", gap: 4}}>
        <Fila icono={<IDoc s={28} />} size={35}>
          Rol individual
        </Fila>
        <Fila icono={<IRegla s={28} />} size={35}>
          Parcelas cercadas
        </Fila>
        <Fila icono={<ICheck s={28} />} size={35}>
          Electricidad
        </Fila>
        <Fila icono={<IPin s={28} />} size={35}>
          Acceso controlado
        </Fila>
        <Fila icono={<IRegla s={28} />} size={35}>
          Aprox. 5.000 m²
        </Fila>
      </div>
    </Cuerpo>
  </Lienzo>
);

const K5: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("k-planos")} foco="50% 50%" />
    <Degradado arriba={0.7} abajo={0.42} />
    <Marco archivo="MARCO-CARRUSEL-3" />
    <Cuerpo top={CARR.sinLogo} ancho={880}>
      <Numero n="04." />
      <Aire h={16} />
      <Ligera size={50}>{"¿Tienes claridad sobre\nel proceso de compra?"}</Ligera>
      <Aire h={26} />
      <Bajada size={35} ancho={800}>
        Antes de avanzar, pregunta por documentación, reserva, formas de pago y escrituración.
      </Bajada>
      <Aire h={22} />
      <Caja color={TC.colors.slate} size={38}>
        {"En Tierra Calma te acompañamos\ndurante el proceso."}
      </Caja>
    </Cuerpo>
  </Lienzo>
);

const K6: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("k-pareja")} foco="50% 56%" />
    <Degradado arriba={0.66} abajo={0.56} />
    <Marco archivo="MARCO-CARRUSEL-4" />
    <Cuerpo top={CARR.sinLogo} ancho={880}>
      <Numero n="05." />
      <Aire h={16} />
      <Ligera size={50}>{"Y lo más importante:"}</Ligera>
      <Aire h={18} />
      <Remate size={72}>{"conócela\nen persona."}</Remate>
      <Aire h={22} />
      <Bajada size={34} ancho={790}>
        El entorno, los accesos y las dimensiones del terreno se entienden mucho mejor cuando estás
        ahí.
      </Bajada>
      <Aire h={22} />
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 500,
          fontSize: 32,
          letterSpacing: "0.14em",
          textTransform: "uppercase",
          color: TC.colors.sand,
          textShadow: "0 2px 16px rgba(0,0,0,0.5)",
        }}
      >
        Parcelas desde UF 2.500
      </div>
    </Cuerpo>
    <div
      style={{
        position: "absolute",
        left: "50%",
        top: 1150,
        transform: "translateX(-50%)",
        display: "flex",
        alignItems: "center",
        gap: 13,
        border: "1.5px solid rgba(255,255,255,0.85)",
        borderRadius: 999,
        padding: "16px 38px",
      }}
    >
      <IWsp s={26} />
      <span
        style={{
          fontFamily: SANS,
          fontWeight: 500,
          fontSize: 29,
          letterSpacing: "0.07em",
          color: "#fff",
          textTransform: "uppercase",
          whiteSpace: "nowrap",
        }}
      >
        Agenda tu visita por WhatsApp
      </span>
    </div>
  </Lienzo>
);

// =============================================================================
// L · 22/10 · HISTORIA · crédito preaprobado · Pilar 3
// =============================================================================

const L: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <Foto src={OCT("l-real")} foco="50% 50%" />
    <Degradado arriba={0.58} abajo={0.5} />
    <Marco archivo="MARCO-ST" />
    <Cuerpo top={STORY.texto} ancho={880}>
      <Ligera size={54}>{"¿Ya tienes tu\ncrédito preaprobado?"}</Ligera>
      <Aire h={22} />
      <Remate size={56}>{"Conoce las parcelas\ndisponibles y las alternativas\npara avanzar en tu compra."}</Remate>
    </Cuerpo>

    <Vidrio y={1080} w={700} rot={-1.6} pad="30px 34px">
      <div style={{display: "flex", alignItems: "center", gap: 18}}>
        <ICheck s={52} />
        <div>
          <div
            style={{
              fontFamily: SANS,
              fontWeight: 500,
              fontSize: 25,
              letterSpacing: "0.16em",
              textTransform: "uppercase",
              color: "rgba(255,255,255,0.82)",
            }}
          >
            Crédito
          </div>
          <div style={{fontFamily: SANS, fontWeight: 500, fontSize: 44, color: "#fff"}}>
            Preaprobado
          </div>
        </div>
      </div>
    </Vidrio>

    <Vidrio y={1280} w={740} rot={1.4} pad="26px 32px">
      <div style={{fontFamily: SANS, fontWeight: 300, fontSize: 34, lineHeight: 1.3, color: "#fff"}}>
        Tierra Calma · Padre Hurtado
        <br />
        Parcelas desde UF 2.500
      </div>
    </Vidrio>

    <Pildora caja={STORY.pill} icono={<IWsp s={28} />} size={30}>
      Conversemos por WhatsApp
    </Pildora>
  </Lienzo>
);

// =============================================================================
// M · 29/10 · POST 4:5 · "Ese proyecto que tienes en mente" · Pilar 1
// El post-it y la polaroid se dibujan encima de la foto de cocina.
// =============================================================================

const M: React.FC = () => (
  <Lienzo w={POST.w} h={POST.h}>
    <Foto src={OCT("m-cocina")} foco="50% 45%" />
    <Degradado arriba={0.4} abajo={0.44} velo={0.08} />

    {/* Polaroid con una foto REAL del terreno */}
    <div
      style={{
        position: "absolute",
        left: 118,
        top: 300,
        width: 232,
        transform: "rotate(-4.5deg)",
        backgroundColor: "#FBF8F2",
        padding: "13px 13px 42px",
        boxShadow: "0 16px 38px rgba(0,0,0,0.34)",
      }}
    >
      <Img src={OCT("j-real")} style={{width: "100%", height: 190, objectFit: "cover", display: "block"}} />
    </div>

    {/* Post-it */}
    <div
      style={{
        position: "absolute",
        left: 372,
        top: 356,
        width: 560,
        transform: "rotate(1.6deg)",
        backgroundColor: TC.colors.cream,
        padding: "38px 42px",
        boxShadow: "0 22px 50px rgba(0,0,0,0.32)",
      }}
    >
      <div
        style={{
          fontFamily: SERIF,
          fontStyle: "italic",
          fontWeight: 500,
          fontSize: 44,
          lineHeight: 1.14,
          color: TC.colors.navy,
          marginBottom: 26,
        }}
      >
        Ese proyecto que tienes en mente…
      </div>
      {["Conocer Tierra Calma", "Elegir mi parcela", "Empezar a proyectar mi casa"].map((t) => (
        <div key={t} style={{display: "flex", alignItems: "center", gap: 14, marginBottom: 14}}>
          <ICheck s={28} c={TC.colors.navy} />
          <span style={{fontFamily: SANS, fontWeight: 300, fontSize: 32, color: TC.colors.ink}}>{t}</span>
        </div>
      ))}
      <div
        style={{
          marginTop: 22,
          paddingTop: 18,
          borderTop: `1px solid ${TC.colors.sand}`,
          fontFamily: SANS,
          fontWeight: 500,
          fontSize: 27,
          letterSpacing: "0.1em",
          textTransform: "uppercase",
          color: TC.colors.brown,
        }}
      >
        Próximo paso: hacerlo realidad
      </div>
    </div>

    <Marco archivo="MARCO-POST" />
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 1108,
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 500,
        fontSize: 28,
        letterSpacing: "0.14em",
        textTransform: "uppercase",
        color: "rgba(255,255,255,0.94)",
        textShadow: "0 2px 18px rgba(0,0,0,0.6)",
      }}
    >
      Aprox. 5.000 m² desde UF 2.500 · Padre Hurtado
    </div>
    <Pildora caja={POST.pill} icono={<IWsp s={25} />} size={29}>
      Agenda tu visita por WhatsApp
    </Pildora>
  </Lienzo>
);

// =============================================================================
// Agrupadores — un frame = una pieza, se rinden con `--sequence`
// =============================================================================

const Serie: React.FC<{piezas: React.FC[]}> = ({piezas}) => {
  const frame = useCurrentFrame();
  return (
    <>
      {piezas.map((P, i) => (
        <Sequence key={i} from={i} durationInFrames={1} layout="none">
          {frame === i ? <P /> : null}
        </Sequence>
      ))}
    </>
  );
};

export const V3_CARR_E = [E1, E2, E3, E4];
export const V3_CARR_K = [K1, K2, K3, K4, K5, K6];
export const V3_POSTS = [G, M];
export const V3_STORIES = [F, H, J, L];

export const V3CarrE: React.FC = () => <Serie piezas={V3_CARR_E} />;
export const V3CarrK: React.FC = () => <Serie piezas={V3_CARR_K} />;
export const V3Posts: React.FC = () => <Serie piezas={V3_POSTS} />;
export const V3Stories: React.FC = () => <Serie piezas={V3_STORIES} />;
