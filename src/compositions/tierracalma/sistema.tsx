import React from "react";
import {AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame} from "remotion";
import {tierracalma as TC, ensureTierraCalmaFonts} from "../../brand/tierracalma";

ensureTierraCalmaFonts();

// =============================================================================
// TIERRA CALMA · SISTEMA GRÁFICO DE PIEZAS ESTÁTICAS
//
// Ingeniería inversa del lenguaje de Carlos Figueroa en las grillas de julio y
// agosto 2026 (referencias en Drive: c-07-08-*, c-10-08-*, p-12-08, p-26-08).
//
// LO QUE DEFINE EL LENGUAJE
//   1. La foto es SIEMPRE una imagen IA premium de golden hour. Las tomas de
//      dron del rodaje del 07-08 son de mañana nublada: sirven para video, no
//      para estáticos — matan la percepción premium. Regla de Valeria (19-08).
//   2. Un marco de filete blanco de 1,5 px, esquinas redondeadas, que se
//      DESPLAZA entre slides de un mismo carrusel: se abre para el logo, se va
//      hacia un lado, o se reduce a dos reglas horizontales. Es lo que hace
//      que el carrusel se lea como un solo objeto.
//   3. Tipografía en pareja fija: una línea en Inter Tight Light y la línea de
//      remate en IvyOra Display **cursiva**, casi siempre en MAYÚSCULAS.
//   4. Píldora blanca de esquinas completas para la ubicación o el WhatsApp.
//   5. Slides de proceso: lavado oliva pesado + círculo con ícono de línea +
//      titular en sans BOLD mayúsculas + bajada en sans light.
//
// ANTI-CHOQUE (el error de la versión anterior)
//   Nada se posiciona "a ojo". Cada formato declara zonas verticales que no se
//   solapan —logo, contenido, píldora— y el contenido se apila con flexbox
//   dentro de su zona. Si un bloque no cabe, se encoge la tipografía: nunca
//   invade la zona vecina.
// =============================================================================

export const SANS = TC.fonts.body;
export const SERIF = TC.fonts.display;

export const OLIVA = TC.colors.olive; // lavado sobre foto en slides de proceso — oliva de marca (#4A553F, Carlos 21-08)
export const OLIVA_HONDA = "#39412F"; // relleno de los círculos de ícono
export const TINTA = "#1D2A1E"; // texto dentro de las píldoras blancas

// --- Formatos y sus zonas -----------------------------------------------------
export type Formato = "4x5" | "1x1" | "9x16";

type Zonas = {
  w: number;
  h: number;
  inset: number; // margen del marco
  radio: number;
  logoY: number; // centro vertical del logo
  logoW: number;
  cuerpo: [number, number]; // banda vertical donde vive el texto
  pill: number; // línea base de la píldora (su borde inferior)
  margen: number; // margen lateral del texto
};

export const ZONAS: Record<Formato, Zonas> = {
  // 4:5 — el formato principal del feed.
  "4x5": {w: 1080, h: 1350, inset: 54, radio: 44, logoY: 100, logoW: 250, cuerpo: [250, 1105], pill: 1232, margen: 118},
  // 1:1 — saludos y piezas de una sola idea.
  "1x1": {w: 1080, h: 1080, inset: 54, radio: 44, logoY: 96, logoW: 240, cuerpo: [230, 858], pill: 972, margen: 118},
  // 9:16 — historias. Zona segura del 14% arriba y abajo (regla del brief).
  "9x16": {w: 1080, h: 1920, inset: 56, radio: 52, logoY: 232, logoW: 250, cuerpo: [360, 1430], pill: 1592, margen: 122},
};

// --- Lienzo -------------------------------------------------------------------
export const Lienzo: React.FC<{f: Formato; children: React.ReactNode}> = ({f, children}) => {
  const z = ZONAS[f];
  return (
    <AbsoluteFill style={{width: z.w, height: z.h, background: "#0C1210", overflow: "hidden"}}>{children}</AbsoluteFill>
  );
};

// --- Foto ---------------------------------------------------------------------
// `foco` mueve el encuadre sin recortar mal: es el object-position.
// `kb` convierte la misma pieza en historia animada: la foto se aleja lento y
// lee como un dron ganando altura. SIEMPRE hacia afuera — un zoom in sobre foto
// fija delata que no es video.
export const Foto: React.FC<{
  src: string;
  foco?: string;
  escala?: number;
  kb?: [number, number];
  kbDur?: number;
}> = ({src, foco = "50% 50%", escala = 1, kb, kbDur = 180}) => {
  const frame = useCurrentFrame();
  const s = kb ? interpolate(frame, [0, kbDur], kb, {extrapolateRight: "clamp"}) : escala;
  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      <Img
        src={staticFile(src)}
        style={{width: "100%", height: "100%", objectFit: "cover", objectPosition: foco, transform: `scale(${s})`}}
      />
    </AbsoluteFill>
  );
};

// Entrada de bloque para las versiones animadas. Con `activo` en false no hace
// nada, así la pieza fija y la animada comparten exactamente el mismo layout.
export const Entrada: React.FC<{activo?: boolean; delay?: number; children: React.ReactNode}> = ({
  activo = false,
  delay = 0,
  children,
}) => {
  const frame = useCurrentFrame();
  if (!activo) return <>{children}</>;
  const f = frame - delay;
  const p = interpolate(f, [0, 22], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    // Hereda la columna del <Cuerpo>: si envolviera en un div en bloque, la
    // pieza animada quedaría maquetada distinto de la fija.
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "inherit",
        width: "100%",
        opacity: p,
        transform: `translateY(${interpolate(p, [0, 1], [30, 0])}px)`,
        willChange: "transform",
      }}
    >
      {children}
    </div>
  );
};

// --- Lavado oliva (slides de proceso / ícono) ---------------------------------
export const Lavado: React.FC<{op?: number}> = ({op = 0.9}) => (
  <>
    <AbsoluteFill style={{background: OLIVA, opacity: op, mixBlendMode: "multiply"}} />
    <AbsoluteFill style={{background: OLIVA, opacity: op * 0.46}} />
  </>
);

// --- Scrim: contraste por degradado, nunca por caja opaca (regla del brief) ---
export type Scrim = "arriba" | "abajo" | "ambos" | "centro" | "no";
export const Degradado: React.FC<{tipo?: Scrim; fuerza?: number}> = ({tipo = "ambos", fuerza = 1}) => {
  if (tipo === "no") return null;
  const a = 0.60 * fuerza; // arriba — protege el logo
  const b = 0.86 * fuerza; // abajo — protege el titular y la píldora
  const capas: string[] = [];
  if (tipo === "arriba" || tipo === "ambos")
    capas.push(`linear-gradient(180deg, rgba(9,15,11,${a}) 0%, rgba(9,15,11,${a * 0.42}) 20%, rgba(9,15,11,0) 40%)`);
  if (tipo === "abajo" || tipo === "ambos")
    capas.push(
      `linear-gradient(0deg, rgba(9,15,11,${b}) 0%, rgba(9,15,11,${b * 0.82}) 22%, rgba(9,15,11,${b * 0.42}) 44%, rgba(9,15,11,0) 68%)`,
    );
  if (tipo === "centro")
    capas.push(`linear-gradient(180deg, rgba(9,15,11,0) 6%, rgba(9,15,11,${0.62 * fuerza}) 34%, rgba(9,15,11,${0.62 * fuerza}) 70%, rgba(9,15,11,0) 96%)`);
  // Velo parejo: sin él, un cielo quemado o una guirnalda encendida se comen el
  // texto blanco por mucho degradado que se le ponga encima.
  capas.push(`linear-gradient(0deg, rgba(9,15,11,${0.13 * fuerza}), rgba(9,15,11,${0.13 * fuerza}))`);
  return <AbsoluteFill style={{background: capas.join(","), pointerEvents: "none"}} />;
};

// Altura del filete superior del marco = la ranura entre la gaviota y el wordmark
// del logo (en el PNG 1320×920 está en y≈572). Así la línea pasa POR el logo
// como en las piezas de Carlos, y el logo mismo va limpio, sin líneas propias
// (feedback de Carlos 21-08: "el logo está mal, tiene incorporado las líneas al
// costado"). Todas las variantes del marco comparten esta altura para que un
// carrusel se lea como un solo objeto.
export const topMarco = (z: Zonas) => Math.round(z.logoY + 0.1935 * z.logoW);

// --- Marco --------------------------------------------------------------------
// `hueco` abre el filete superior para que entre el logo. `corrimiento` desplaza
// el marco fuera de cuadro para encadenar slides. `bandas` deja solo dos reglas.
export type MarcoVar = "hueco" | "cerrado" | "bandas" | "derecha" | "izquierda";

export const Marco: React.FC<{f: Formato; variante?: MarcoVar; op?: number}> = ({f, variante = "hueco", op = 0.72}) => {
  const z = ZONAS[f];
  const col = `rgba(255,255,255,${op})`;
  const g = 1.5;

  if (variante === "bandas") {
    // La banda inferior va en el MISMO borde que el marco hueco (h - inset):
    // en inset + 66 pasaba por detrás de la píldora y de la flecha.
    return (
      <AbsoluteFill style={{pointerEvents: "none"}}>
        <div style={{position: "absolute", left: 0, right: 0, top: topMarco(z), height: g, background: col}} />
        <div style={{position: "absolute", left: 0, right: 0, bottom: z.inset, height: g, background: col}} />
      </AbsoluteFill>
    );
  }

  if (variante !== "hueco") {
    // Marcos desplazados: se anclan en los márgenes estándar y SALEN del lienzo
    // por el costado nombrado. El filete visible queda siempre en el margen —
    // nunca cruza el texto (que vive en z.margen) ni la píldora. La versión
    // anterior corría el rectángulo completo 120 px y la línea sobreviviente
    // caía en medio del titular o encima de la píldora.
    const top = topMarco(z);
    const alto = z.h - top - z.inset;
    const fuga = 120 + z.radio; // cuánto se sale del lienzo el lado que escapa
    const left = variante === "izquierda" ? -fuga : z.inset;
    const width = variante === "cerrado" ? z.w - z.inset * 2 : z.w - z.inset + fuga;
    return (
      <AbsoluteFill style={{pointerEvents: "none"}}>
        <div
          style={{
            position: "absolute",
            left,
            top,
            width,
            height: alto,
            border: `${g}px solid ${col}`,
            borderRadius: z.radio,
          }}
        />
      </AbsoluteFill>
    );
  }

  // Variante "hueco": el filete superior se corta a ambos lados del logo.
  // UN SOLO trazado SVG. La versión con divs superpuestos dejaba el borde
  // vertical de la caja principal subiendo recto por dentro de la curva de la
  // esquina — el "muñón" que el cliente marcó en la revisión del 20-08.
  const y0 = topMarco(z);
  const x0 = z.inset;
  const x1 = z.w - z.inset;
  const y1 = z.h - z.inset;
  const r = z.radio;
  const huecoW = z.logoW + 44; // el wordmark mide ~0,89·logoW; quedan ~36 px de aire por lado
  const gapL = (z.w - huecoW) / 2;
  const gapR = (z.w + huecoW) / 2;
  const d = [
    `M ${gapL} ${y0}`,
    `L ${x0 + r} ${y0}`,
    `A ${r} ${r} 0 0 0 ${x0} ${y0 + r}`,
    `L ${x0} ${y1 - r}`,
    `A ${r} ${r} 0 0 0 ${x0 + r} ${y1}`,
    `L ${x1 - r} ${y1}`,
    `A ${r} ${r} 0 0 0 ${x1} ${y1 - r}`,
    `L ${x1} ${y0 + r}`,
    `A ${r} ${r} 0 0 0 ${x1 - r} ${y0}`,
    `L ${gapR} ${y0}`,
  ].join(" ");
  return (
    <AbsoluteFill style={{pointerEvents: "none"}}>
      <svg width={z.w} height={z.h} viewBox={`0 0 ${z.w} ${z.h}`} fill="none">
        <path d={d} stroke={col} strokeWidth={g} strokeLinecap="butt" />
      </svg>
    </AbsoluteFill>
  );
};

// --- Logo ---------------------------------------------------------------------
export const LogoArriba: React.FC<{f: Formato}> = ({f}) => {
  const z = ZONAS[f];
  return (
    <div style={{position: "absolute", left: 0, right: 0, top: z.logoY - z.logoW * 0.24, display: "flex", justifyContent: "center"}}>
      <Img
        src={staticFile(TC.logoWhite)}
        style={{width: z.logoW, filter: "drop-shadow(0 2px 18px rgba(0,0,0,0.45))"}}
      />
    </div>
  );
};

// --- Íconos de línea ----------------------------------------------------------
export type IconoId = "pin" | "casa" | "huespedes" | "huerta" | "quincho" | "whatsapp" | "ruta" | "reloj" | "regla";

const TRAZOS: Record<IconoId, React.ReactNode> = {
  pin: (
    <>
      <path d="M12 21.5s7-6.2 7-11.4A7 7 0 0 0 5 10.1c0 5.2 7 11.4 7 11.4Z" />
      <circle cx="12" cy="10" r="2.6" />
    </>
  ),
  casa: (
    <>
      <path d="M3.5 10.6 12 3.6l8.5 7" />
      <path d="M5.6 9.2v10.4h12.8V9.2" />
      <path d="M10 19.6v-5.2h4v5.2" />
    </>
  ),
  huespedes: (
    <>
      <path d="M2.6 11.4 8.4 6.6l5.8 4.8" />
      <path d="M4.2 10.2v8.6h8.4v-8.6" />
      <path d="M13.4 18.8V12h7.8v6.8Z" />
      <path d="M16.4 18.8v-3.4h1.8v3.4" />
    </>
  ),
  huerta: (
    <>
      <path d="M12 21V11.2" />
      <path d="M12 12.6C12 8.9 9.2 6.2 5.4 6.2c0 3.7 2.8 6.4 6.6 6.4Z" />
      <path d="M12 11.4c0-3.4 2.6-5.9 6.1-5.9 0 3.4-2.7 5.9-6.1 5.9Z" />
      <path d="M4.5 21h15" />
    </>
  ),
  quincho: (
    <>
      <path d="M3.4 9.4 12 4.2l8.6 5.2" />
      <path d="M5.4 9.4V20M18.6 9.4V20" />
      <path d="M3.4 20h17.2" />
      <path d="M9.4 20v-4.4h5.2V20" />
      <path d="M12 7.2v-2" />
    </>
  ),
  whatsapp: (
    <>
      <path d="M20.5 11.7a8.5 8.5 0 0 1-12.6 7.5L3.5 20.5l1.4-4.2a8.5 8.5 0 1 1 15.6-4.6Z" />
      <path d="M9.1 8.6c.3-.1.6 0 .8.3l.9 1.4c.2.3.1.6-.1.8l-.5.5c-.1.2-.2.4-.1.6.4.9 1.2 1.7 2.1 2.1.2.1.4 0 .6-.1l.5-.5c.2-.2.5-.3.8-.1l1.4.9c.3.2.4.5.3.8-.2.7-.9 1.2-1.7 1.2-2.7-.2-5-2.5-5.2-5.2 0-.8.5-1.5 1.2-1.7Z" />
    </>
  ),
  ruta: (
    <>
      <path d="M12 21v-6" />
      <path d="M4.5 4.5h12l2.6 2.9-2.6 2.9h-12Z" />
      <path d="M12 4.5V2.6" />
    </>
  ),
  reloj: (
    <>
      <circle cx="12" cy="12" r="8.4" />
      <path d="M12 7.2V12l3.2 1.9" />
    </>
  ),
  regla: (
    <>
      <path d="M8.2 4.4H6.4A1.4 1.4 0 0 0 5 5.8v13.4a1.4 1.4 0 0 0 1.4 1.4h11.2a1.4 1.4 0 0 0 1.4-1.4V5.8a1.4 1.4 0 0 0-1.4-1.4h-1.8" />
      <path d="M9 3h6v2.8H9Z" />
      <path d="M8.6 12.4l2 2 4.8-4.8" />
    </>
  ),
};

export const Icono: React.FC<{id: IconoId; d: number; color?: string; grosor?: number}> = ({
  id,
  d,
  color = "#FFFFFF",
  grosor = 1.35,
}) => (
  <svg width={d} height={d} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={grosor} strokeLinecap="round" strokeLinejoin="round">
    {TRAZOS[id]}
  </svg>
);

export const CirculoIcono: React.FC<{id: IconoId; d?: number}> = ({id, d = 400}) => (
  <div
    style={{
      width: d,
      height: d,
      borderRadius: "50%",
      border: "2.4px solid rgba(255,255,255,0.95)",
      background: `${OLIVA_HONDA}E8`,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      flexShrink: 0,
    }}
  >
    <Icono id={id} d={d * 0.42} grosor={1.15} />
  </div>
);

// --- Píldora ------------------------------------------------------------------
export const Pildora: React.FC<{
  texto: React.ReactNode;
  icono?: IconoId;
  size?: number;
  solida?: boolean;
}> = ({texto, icono, size = 27, solida = true}) => (
  <div
    style={{
      display: "inline-flex",
      alignItems: "center",
      gap: size * 0.5,
      padding: `${size * 0.78}px ${size * 1.42}px`,
      borderRadius: 999,
      background: solida ? "#FFFFFF" : "rgba(255,255,255,0.06)",
      border: solida ? "none" : "1.4px solid rgba(255,255,255,0.85)",
      boxShadow: solida ? "0 4px 26px rgba(0,0,0,0.22)" : "none",
    }}
  >
    {icono ? <Icono id={icono} d={size * 1.18} color={solida ? TINTA : "#FFFFFF"} grosor={1.6} /> : null}
    <span
      style={{
        fontFamily: SANS,
        fontSize: size,
        fontWeight: 400,
        letterSpacing: "0.055em",
        textTransform: "uppercase",
        color: solida ? TINTA : "#FFFFFF",
        whiteSpace: "nowrap",
        lineHeight: 1,
      }}
    >
      {texto}
    </span>
  </div>
);

// Fila de la píldora: se ancla por su borde inferior, así nunca pisa el cuerpo.
// `conFlecha` reserva el ancho de la flecha de carrusel: la píldora se centra en
// el espacio restante y queda garantizado un respiro mínimo entre ambas — antes
// una píldora ancha llegaba a quedar a 6 px del círculo.
export const ZonaPildora: React.FC<{f: Formato; conFlecha?: boolean; children: React.ReactNode}> = ({
  f,
  conFlecha = false,
  children,
}) => {
  const z = ZONAS[f];
  return (
    <div
      style={{
        position: "absolute",
        left: z.inset,
        right: conFlecha ? z.inset + 164 : z.inset,
        top: z.pill - 96,
        height: 96,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "flex-end",
        gap: 16,
      }}
    >
      {children}
    </div>
  );
};

// --- Flecha de carrusel -------------------------------------------------------
// Centrada verticalmente con la píldora (centro = z.pill − 35) y separada del
// radio de la esquina del marco: antes rozaba el arco inferior derecho y quedaba
// desalineada media línea respecto de la píldora.
export const Flecha: React.FC<{f: Formato; oscura?: boolean}> = ({f, oscura = false}) => {
  const z = ZONAS[f];
  return (
    <div
      style={{
        position: "absolute",
        right: z.inset + 44,
        bottom: z.h - z.pill - 13,
        width: 96,
        height: 96,
        borderRadius: "50%",
        background: oscura ? TC.colors.navy : "#FFFFFF",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        boxShadow: oscura ? "0 6px 26px rgba(11,44,73,0.22)" : "0 6px 30px rgba(0,0,0,0.28)",
      }}
    >
      <svg
        width={40}
        height={40}
        viewBox="0 0 24 24"
        fill="none"
        stroke={oscura ? "#FFFFFF" : TINTA}
        strokeWidth={1.7}
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d="M9 5l7 7-7 7" />
      </svg>
    </div>
  );
};

// --- Cuerpo: la única forma de poner texto ------------------------------------
// Se apila con flexbox dentro de la banda `cuerpo` del formato. Al estar acotado
// por arriba y por abajo, es imposible que invada el logo o la píldora.
export const Cuerpo: React.FC<{
  f: Formato;
  alinear?: "arriba" | "centro" | "abajo";
  centrado?: boolean;
  gap?: number;
  children: React.ReactNode;
}> = ({f, alinear = "abajo", centrado = false, gap = 0, children}) => {
  const z = ZONAS[f];
  const [a, b] = z.cuerpo;
  return (
    <div
      style={{
        position: "absolute",
        left: z.margen,
        right: z.margen,
        top: a,
        height: b - a,
        display: "flex",
        flexDirection: "column",
        gap,
        justifyContent: alinear === "arriba" ? "flex-start" : alinear === "centro" ? "center" : "flex-end",
        alignItems: centrado ? "center" : "flex-start",
        textAlign: centrado ? "center" : "left",
      }}
    >
      {children}
    </div>
  );
};

const SOMBRA = "0 2px 30px rgba(0,0,0,0.42)";

// Línea en sans light. `caps` la pone en mayúsculas.
export const Ligera: React.FC<{
  size: number;
  caps?: boolean;
  color?: string;
  lh?: number;
  peso?: number;
  children: React.ReactNode;
}> = ({size, caps = false, color = "#FFFFFF", lh = 1.14, peso = 300, children}) => (
  <div
    style={{
      fontFamily: SANS,
      fontSize: size,
      fontWeight: peso,
      lineHeight: lh,
      color,
      textTransform: caps ? "uppercase" : "none",
      letterSpacing: caps ? "0.004em" : "-0.008em",
      textShadow: SOMBRA,
    }}
  >
    {children}
  </div>
);

// Línea de remate en IvyOra cursiva. Es la firma tipográfica de la marca.
export const Remate: React.FC<{size: number; caps?: boolean; color?: string; lh?: number; children: React.ReactNode}> = ({
  size,
  caps = true,
  color = "#FFFFFF",
  lh = 1.04,
  children,
}) => (
  <div
    style={{
      fontFamily: SERIF,
      fontStyle: "italic",
      fontWeight: 400,
      fontSize: size,
      lineHeight: lh,
      color,
      textTransform: caps ? "uppercase" : "none",
      letterSpacing: caps ? "-0.005em" : "-0.012em",
      textShadow: SOMBRA,
    }}
  >
    {children}
  </div>
);

// Titular pesado en sans, para los slides de proceso con lavado oliva.
export const Fuerte: React.FC<{size: number; color?: string; lh?: number; children: React.ReactNode}> = ({
  size,
  color = "#FFFFFF",
  lh = 1.06,
  children,
}) => (
  <div
    style={{
      fontFamily: SANS,
      fontSize: size,
      fontWeight: 700,
      lineHeight: lh,
      color,
      textTransform: "uppercase",
      letterSpacing: "-0.017em",
      textShadow: SOMBRA,
    }}
  >
    {children}
  </div>
);

// Etiqueta chica en mayúsculas espaciadas — el eco del "PADRE HURTADO" del logo.
// Blanca por defecto: la arena solo contrasta sobre crema (regla del sistema);
// sobre foto se lavaba. Los slides de fondo crema pasan su color explícito.
export const Etiqueta: React.FC<{size?: number; color?: string; children: React.ReactNode}> = ({
  size = 25,
  color = "#FFFFFF",
  children,
}) => (
  <div
    style={{
      fontFamily: SANS,
      fontSize: size,
      fontWeight: 500,
      letterSpacing: "0.24em",
      textTransform: "uppercase",
      color,
      textShadow: SOMBRA,
    }}
  >
    {children}
  </div>
);

// Cifra grande en IvyOra recta. La regla del brief: la cifra es lo más grande.
export const Cifra: React.FC<{size: number; color?: string; children: React.ReactNode}> = ({
  size,
  color = "#FFFFFF",
  children,
}) => (
  <div
    style={{
      fontFamily: SERIF,
      fontWeight: 400,
      fontSize: size,
      lineHeight: 0.98,
      color,
      letterSpacing: "-0.03em",
      textShadow: SOMBRA,
    }}
  >
    {children}
  </div>
);

export const Filete: React.FC<{ancho?: number; op?: number; margen?: number}> = ({ancho = 100, op = 0.5, margen = 26}) => (
  <div style={{width: ancho, height: 1.4, background: `rgba(255,255,255,${op})`, margin: `${margen}px 0`}} />
);

export const Espacio: React.FC<{h: number}> = ({h}) => <div style={{height: h, flexShrink: 0}} />;
