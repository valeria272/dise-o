import React from "react";
import {AbsoluteFill, Img, Sequence, staticFile, useCurrentFrame} from "remotion";
import {tierracalma as TC, ensureTierraCalmaFonts} from "../../brand/tierracalma";
import geo from "../../../public/assets/tierracalma/paid-oct/paid-oct.json";

// =============================================================================
// TIERRA CALMA · PAID OCTUBRE 2026 — campaña de WhatsApp del 01-oct
//
// Brief: «Brief Diseño Tierra Calma - Octubre 2026.xlsx» (Ignacio Retamal,
// PERFORMANCE/Octubre 2026). Test A/B: se lanzan las dos el mismo día y se mide
// qué argumento abre más conversaciones.
//
//   02-A «Tu casa cabe, y sobra»      → el TAMAÑO del terreno
//   02-B «El mapa de los 30 minutos»  → la DISTANCIA a Santiago
//
// DIRECCIÓN DE ARTE
// · Las dos salen de FOTO REAL del rodaje del 07-08. Nada de IA: en pauta se
//   muestra el terreno que se vende. 02-A es la cenital del lote de la caseta
//   verde (el de la pieza «5.000 m²» de septiembre); 02-B, un oblicuo de
//   parcelas verdes con casas y los cerros atrás. Santiago NO se ve en ninguna
//   toma del rodaje (neblina): los tiempos los cuentan las cápsulas, no la foto.
// · La casa de 02-A está A ESCALA: 150 m² = 3,00 % del deslinde, calculado en
//   scripts/tc-paid-oct-prep.py. Sólo contorno, sin relleno ni sombra: plano,
//   no render (brief).
// · Tipografía: el titular de 02-A en IvyOra cursiva versales dentro de chips
//   oscuros translúcidos — es la solución de la pieza «5.000 m²» aprobada en
//   septiembre y la del propio boceto del brief. Datos y cápsulas en Inter
//   Tight versales con tracking abierto (regla escrita del brief).
// · Contraste por degradado; los chips son translúcidos, nunca caja opaca.
// · El marco es el asset bloqueado del diseñador. El 1:1 no existía: se deriva
//   del MARCO-POST quitando 270 filas idénticas (ver el script de preparación).
//
// COPY: verbatim del brief. Datos, todos de la lista blanca: 5.000 m² · desde
// UF 2.500 · 30 min de Santiago · 15 min del peaje Padre Hurtado.
// =============================================================================

const A = (n: string) => staticFile(`assets/tierracalma/paid-oct/${n}`);
const MARCO_4x5 = staticFile("assets/tierracalma/marcos/MARCO-POST.png");
const MARCO_1x1 = A("MARCO-POST-1x1.png");
const SANS = TC.fonts.body;
const SERIF = TC.fonts.display;

type Formato = "1x1" | "4x5";
// Geometría del marco medida sobre el alfa del PNG (manual § 4 quinquies).
const FMT = {
  "1x1": {h: 1080, marco: MARCO_1x1, pill: {x: 264, y: 942, w: 540, h: 53}},
  "4x5": {h: 1350, marco: MARCO_4x5, pill: {x: 264, y: 1212, w: 540, h: 53}},
} as const;

// -----------------------------------------------------------------------------
// Primitivas
// -----------------------------------------------------------------------------

const Lienzo: React.FC<{f: Formato; foto: string; children: React.ReactNode}> = ({f, foto, children}) => {
  ensureTierraCalmaFonts();
  return (
    <AbsoluteFill style={{width: 1080, height: FMT[f].h, backgroundColor: TC.colors.ink, overflow: "hidden"}}>
      {/* El JPG viene recortado a la medida exacta: la fila del JPG es la del lienzo. */}
      <Img src={A(foto)} style={{position: "absolute", inset: 0, width: "100%", height: "100%"}} />
      {children}
      <Img src={FMT[f].marco} style={{position: "absolute", inset: 0, width: "100%", height: "100%"}} />
      <Pie f={f} />
    </AbsoluteFill>
  );
};

const Degradado: React.FC<{arriba: number; abajo: number; corte?: number}> = ({arriba, abajo, corte = 52}) => (
  <AbsoluteFill
    style={{
      background: `linear-gradient(to bottom, rgba(6,14,20,${arriba}) 0%, rgba(6,14,20,${arriba * 0.35}) 22%, rgba(6,14,20,0) 38%, rgba(6,14,20,0) ${corte}%, rgba(6,14,20,${abajo * 0.6}) 78%, rgba(6,14,20,${abajo}) 100%)`,
    }}
  />
);

const IPin: React.FC<{s?: number}> = ({s = 24}) => (
  <svg width={s} height={s} viewBox="0 0 24 24" fill="none" style={{flexShrink: 0}}>
    <path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11Z" stroke="#fff" strokeWidth="1.6" strokeLinejoin="round" />
    <circle cx="12" cy="10" r="2.6" stroke="#fff" strokeWidth="1.6" />
  </svg>
);

/** «📍 TIERRA CALMA · PADRE HURTADO» dentro del contorno que ya trae el marco.
    Idéntico en las tres piezas: mismo tamaño y misma posición (brief). */
const Pie: React.FC<{f: Formato}> = ({f}) => {
  const c = FMT[f].pill;
  return (
    <div
      style={{
        position: "absolute",
        left: c.x,
        top: c.y,
        width: c.w,
        height: c.h,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        gap: 11,
      }}
    >
      <IPin s={23} />
      <span
        style={{
          fontFamily: SANS,
          fontWeight: 500,
          fontSize: 23,
          letterSpacing: "0.08em",
          color: "#fff",
          whiteSpace: "nowrap",
        }}
      >
        TIERRA CALMA · PADRE HURTADO
      </span>
    </div>
  );
};

/** Línea de apoyo: más chica, centrada, justo sobre la píldora. */
const Apoyo: React.FC<{y: number}> = ({y}) => (
  <div
    style={{
      position: "absolute",
      left: 0,
      right: 0,
      top: y,
      textAlign: "center",
      fontFamily: SANS,
      fontWeight: 500,
      fontSize: 30,
      letterSpacing: "0.16em",
      color: "#fff",
      whiteSpace: "nowrap",
      textShadow: "0 2px 16px rgba(0,0,0,0.6)",
    }}
  >
    5.000 M² · DESDE UF 2.500
  </div>
);

// -----------------------------------------------------------------------------
// 02-A · Tu casa cabe, y sobra
// -----------------------------------------------------------------------------

/** Chip oscuro translúcido con el titular en IvyOra — el de «5.000 m²» de sept. */
const Chip: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      alignSelf: "flex-start",
      backgroundColor: "rgba(9,20,28,0.64)",
      backdropFilter: "blur(14px)",
      WebkitBackdropFilter: "blur(14px)",
      border: "1.5px solid rgba(255,255,255,0.55)",
      borderRadius: 16,
      padding: "6px 30px 10px",
      fontFamily: SERIF,
      fontStyle: "italic",
      fontWeight: 500,
      fontSize: 66,
      lineHeight: 1.12,
      color: "#fff",
      textTransform: "uppercase",
      whiteSpace: "nowrap",
    }}
  >
    {children}
  </div>
);

const CasaCabe: React.FC<{f: Formato}> = ({f}) => {
  const g = geo[`02A_${f}`];
  const pts = (p: number[][]) => p.map(([x, y]) => `${x},${y}`).join(" ");
  // Etiqueta del plano: a la derecha de la casa, a la altura de su ala larga.
  const der = Math.max(...g.casa.map((p) => p[0]));
  const arr = Math.min(...g.casa.map((p) => p[1]));
  const titularY = f === "1x1" ? 640 : 900;
  return (
    <Lienzo f={f} foto={`a-cenital-${f}.jpg`}>
      <Degradado arriba={0.55} abajo={0.72} corte={f === "1x1" ? 50 : 58} />
      <svg
        width={1080}
        height={FMT[f].h}
        style={{position: "absolute", inset: 0, filter: "drop-shadow(0 1px 3px rgba(0,0,0,0.55))"}}
      >
        <polygon points={pts(g.lote)} fill="none" stroke="#fff" strokeWidth={3} strokeLinejoin="round" />
        <polygon points={pts(g.casa)} fill="none" stroke="#fff" strokeWidth={3} strokeLinejoin="miter" />
      </svg>
      <div
        style={{
          position: "absolute",
          left: der + 22,
          top: arr + 8,
          fontFamily: SANS,
          fontWeight: 500,
          fontSize: 26,
          letterSpacing: "0.12em",
          color: "#fff",
          textShadow: "0 1px 10px rgba(0,0,0,0.7)",
        }}
      >
        150 M²
      </div>
      <div style={{position: "absolute", left: 128, top: titularY, display: "flex", flexDirection: "column", gap: 14}}>
        <Chip>Una casa de 150 m².</Chip>
        <Chip>Y 4.850 m² más.</Chip>
      </div>
      <Apoyo y={f === "1x1" ? 884 : 1146} />
    </Lienzo>
  );
};

// -----------------------------------------------------------------------------
// 02-B · El mapa de los 30 minutos
// -----------------------------------------------------------------------------

/** Flecha dibujada: la fuente no garantiza el glifo «←» y no se deja al azar. */
const Flecha: React.FC = () => (
  <svg width={40} height={28} viewBox="0 0 40 28" fill="none" style={{flexShrink: 0, margin: "0 20px"}}>
    <path d="M38 14H4M14 3L3 14l11 11" stroke="#fff" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

/** La cápsula de línea fina del pie, en grande, con los tiempos adentro. */
const Capsula: React.FC<{lugar: string; tiempo: string}> = ({lugar, tiempo}) => (
  <div
    style={{
      display: "flex",
      alignItems: "center",
      border: "2px solid rgba(255,255,255,0.92)",
      borderRadius: 999,
      padding: "20px 46px",
      backgroundColor: "rgba(9,20,28,0.42)",
      backdropFilter: "blur(10px)",
      WebkitBackdropFilter: "blur(10px)",
      fontFamily: SANS,
      fontWeight: 500,
      fontSize: 46,
      letterSpacing: "0.1em",
      color: "#fff",
      whiteSpace: "nowrap",
    }}
  >
    {lugar}
    <Flecha />
    {tiempo}
  </div>
);

const Mapa30: React.FC<{f: Formato}> = ({f}) => (
  <Lienzo f={f} foto={`b-oblicuo-${f}.jpg`}>
    <Degradado arriba={0.7} abajo={0.86} corte={56} />
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: f === "1x1" ? 300 : 360,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 26,
      }}
    >
      <Capsula lugar="SANTIAGO" tiempo="30 MIN" />
      <Capsula lugar="PEAJE PADRE HURTADO" tiempo="15 MIN" />
    </div>
    <Apoyo y={f === "1x1" ? 884 : 1146} />
  </Lienzo>
);

// -----------------------------------------------------------------------------
// D1 · El fin de semana largo — reemplaza a B4 (decisión del 23-09)
//
// B4 «La primavera» pedía un aéreo con los árboles brotados al atardecer y el
// rodaje es de una mañana nublada de invierno: no existe esa toma. El brief
// manda en ese caso D1, «un cambio de tipografía sobre el archivo existente».
// El fondo es la pieza «alcance» de septiembre con las líneas 1 y 2 borradas
// (ver scripts/tc-paid-oct-prep.py); la línea 3, «TIERRA CALMA.» en serif, es
// la original. Marco, logo y píldora también son los de esa pieza.
//
// ⚠️ El brief escribe «PASALO» (voseo). Va «PÁSALO», igual que en septiembre
// se corrigió «pasalo» → «pásalo» (grilla-septiembre-2026.md § 2.6).
// ⏳ Sólo sirve hasta el 12-oct (fin de semana largo del 12 de octubre).
// -----------------------------------------------------------------------------

/** Línea base de las dos líneas nuevas, medida sobre la pieza de septiembre:
    la línea 2 original apoya en la fila 395 y el paso entre líneas es 66 px. */
const D1_BASE_2 = 395;
const D1_PASO = 66;
const D1_CUERPO = 47; // altura de mayúscula 34 px, la de la pieza original

const FinDeSemana: React.FC<{f: "9x16" | "4x5"}> = ({f}) => {
  ensureTierraCalmaFonts();
  // En una caja de line-height = paso, la línea base cae a medio interlineado
  // + ascendente de Inter Tight (0,969 em) desde el borde superior.
  const desdeArriba = (D1_PASO - D1_CUERPO * 1.211) / 2 + D1_CUERPO * 0.969;
  return (
    <AbsoluteFill style={{width: 1080, height: f === "9x16" ? 1920 : 1350, overflow: "hidden"}}>
      <Img src={A(`d1-${f}.png`)} style={{position: "absolute", inset: 0, width: "100%", height: "100%"}} />
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: D1_BASE_2 - D1_PASO - desdeArriba,
          textAlign: "center",
          fontFamily: SANS,
          fontWeight: 300, // el de la pieza de septiembre, comparado lado a lado
          fontSize: D1_CUERPO,
          lineHeight: `${D1_PASO}px`,
          letterSpacing: "0.01em",
          color: "#fff",
          whiteSpace: "nowrap",
          textShadow: "0 2px 18px rgba(0,0,0,0.35)",
        }}
      >
        EL FIN DE SEMANA LARGO,
        <br />
        PÁSALO ACÁ EN
      </div>
    </AbsoluteFill>
  );
};

export const PAID_OCT_D1: React.FC[] = [() => <FinDeSemana f="9x16" />];
export const PAID_OCT_D1_4x5: React.FC[] = [() => <FinDeSemana f="4x5" />];

// -----------------------------------------------------------------------------
// Series — un frame = una pieza, se rinden con `--sequence`
// -----------------------------------------------------------------------------

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

/** Orden = nombre de entrega. 1:1 → TC_B2_casacabe_1x1, TC_A2_mapa30min_1x1. */
export const PAID_OCT_1x1: React.FC[] = [() => <CasaCabe f="1x1" />, () => <Mapa30 f="1x1" />];
/** 4:5 → TC_B2_casacabe_4x5, TC_A2_mapa30min_4x5. */
export const PAID_OCT_4x5: React.FC[] = [() => <CasaCabe f="4x5" />, () => <Mapa30 f="4x5" />];

export const PaidOct1x1: React.FC = () => <Serie piezas={PAID_OCT_1x1} />;
export const PaidOct4x5: React.FC = () => <Serie piezas={PAID_OCT_4x5} />;
/** D1 → TC_D1_findesemana_9x16 y TC_D1_findesemana_4x5. */
export const PaidOctD1_9x16: React.FC = () => <Serie piezas={PAID_OCT_D1} />;
export const PaidOctD1_4x5: React.FC = () => <Serie piezas={PAID_OCT_D1_4x5} />;
