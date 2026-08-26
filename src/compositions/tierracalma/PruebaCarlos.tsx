import React from "react";
import {AbsoluteFill, Audio, Img, interpolate, Sequence, staticFile, useCurrentFrame} from "remotion";
import {tierracalma as TC, ensureTierraCalmaFonts} from "../../brand/tierracalma";
import {Foto, Degradado, Ligera, Remate, Etiqueta, Cifra, Icono, Entrada, TINTA} from "./sistema";
import {Clip, ClipFoto, Grade, Grain, Reveal, Scene, Inner, LogoOutro} from "./kit";

ensureTierraCalmaFonts();

// =============================================================================
// TIERRA CALMA · PRUEBA DE MANO — el lenguaje de Carlos (ref-carlos-sep2026)
//
// Lote de PRUEBA con copies inventados (solo datos de la lista blanca) para
// comparar contra la grilla real de septiembre del diseñador. NO se publica.
//
// Qué cambia respecto de nuestro sistema anterior (manual § 4 quater):
//   1. El texto vive ARRIBA, en el cielo, centrado. La foto respira abajo.
//   2. Logo chico y alto (~185 px), el filete del marco pasa por su ranura.
//   3. La línea de remate puede ir dentro de una CAJA de color de marca
//      (café #6C473D · oliva #4A553F) — eso es lo "lúdico".
//   4. Filas de píldoras de palabra ("HUERTA · FRUTALES · QUINCHO").
//   5. CTA en píldora oscura traslúcida, en caja baja ("Agenda tu visita…").
//   6. Foto real del dron gradeada + IA de estilo de vida, mezcladas.
//   7. Bajadas en caja baja, tipografía más chica y con más aire.
// =============================================================================

const SANS = TC.fonts.body;
const CAFE = TC.colors.brown;
const OLIVA = TC.colors.olive;

// --- Geometría (logo chico y alto, como las piezas de Carlos) -----------------
type FmtPC = "4x5" | "9x16";
type ZPC = {w: number; h: number; inset: number; radio: number; logoW: number; logoTop: number};

const ZONAS_PC: Record<FmtPC, ZPC> = {
  "4x5": {w: 1080, h: 1350, inset: 54, radio: 44, logoW: 185, logoTop: 46},
  "9x16": {w: 1080, h: 1920, inset: 56, radio: 52, logoW: 190, logoTop: 108},
};

// Ranura gaviota/wordmark del PNG del logo (y≈572 de 920, ancho 1320):
// offset vertical desde el borde superior del logo = 0.4333 · logoW.
const ranuraY = (z: ZPC) => Math.round(z.logoTop + 0.4333 * z.logoW);

const LogoAlto: React.FC<{f: FmtPC}> = ({f}) => {
  const z = ZONAS_PC[f];
  return (
    <div style={{position: "absolute", left: 0, right: 0, top: z.logoTop, display: "flex", justifyContent: "center"}}>
      <Img src={staticFile(TC.logoWhite)} style={{width: z.logoW, filter: "drop-shadow(0 2px 16px rgba(0,0,0,0.45))"}} />
    </div>
  );
};

// Marco fino: UN SOLO trazado SVG (regla dura del 20-08 — nada de divs con
// bordes superpuestos). `hueco` corta el filete superior en la ranura del logo.
const MarcoPC: React.FC<{f: FmtPC; variante?: "hueco" | "cerrado" | "bandas"; op?: number}> = ({
  f,
  variante = "hueco",
  op = 0.8,
}) => {
  const z = ZONAS_PC[f];
  const col = `rgba(255,255,255,${op})`;
  const g = 1.5;
  const y0 = ranuraY(z);
  const x0 = z.inset;
  const x1 = z.w - z.inset;
  const y1 = z.h - z.inset;
  const r = z.radio;

  if (variante === "bandas") {
    return (
      <AbsoluteFill style={{pointerEvents: "none"}}>
        <div style={{position: "absolute", left: 0, right: 0, top: y0, height: g, background: col}} />
        <div style={{position: "absolute", left: 0, right: 0, bottom: z.inset, height: g, background: col}} />
      </AbsoluteFill>
    );
  }

  const huecoW = z.logoW + 44;
  const gapL = (z.w - huecoW) / 2;
  const gapR = (z.w + huecoW) / 2;
  const d =
    variante === "hueco"
      ? [
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
        ].join(" ")
      : [
          `M ${x0 + r} ${y0}`,
          `L ${x1 - r} ${y0}`,
          `A ${r} ${r} 0 0 1 ${x1} ${y0 + r}`,
          `L ${x1} ${y1 - r}`,
          `A ${r} ${r} 0 0 1 ${x1 - r} ${y1}`,
          `L ${x0 + r} ${y1}`,
          `A ${r} ${r} 0 0 1 ${x0} ${y1 - r}`,
          `L ${x0} ${y0 + r}`,
          `A ${r} ${r} 0 0 1 ${x0 + r} ${y0}`,
        ].join(" ");
  return (
    <AbsoluteFill style={{pointerEvents: "none"}}>
      <svg width={z.w} height={z.h} viewBox={`0 0 ${z.w} ${z.h}`} fill="none">
        <path d={d} stroke={col} strokeWidth={g} strokeLinecap="butt" />
      </svg>
    </AbsoluteFill>
  );
};

// --- Caja de color de marca (el recurso "lúdico" de Carlos) -------------------
// La segunda línea del titular vive DENTRO de una caja café u oliva traslúcida.
const CajaColor: React.FC<{
  color?: string;
  size?: number;
  caps?: boolean;
  radio?: number;
  children: React.ReactNode;
}> = ({color = CAFE, size = 34, caps = true, radio = 26, children}) => (
  <div
    style={{
      display: "inline-block",
      background: `${color}D9`, // ~85% — traslúcida, deja respirar la foto
      borderRadius: radio,
      padding: `${size * 0.62}px ${size * 1.15}px`,
      boxShadow: "0 4px 30px rgba(0,0,0,0.18)",
    }}
  >
    <div
      style={{
        fontFamily: SANS,
        fontSize: size,
        fontWeight: 300,
        lineHeight: 1.28,
        color: "#FFFFFF",
        textTransform: caps ? "uppercase" : "none",
        letterSpacing: caps ? "0.02em" : "0",
        textAlign: "center",
      }}
    >
      {children}
    </div>
  </div>
);

// --- Fila de píldoras de palabra ("HUERTA · PISCINA · FRUTALES") --------------
const PillFila: React.FC<{palabras: string[]; size?: number}> = ({palabras, size = 25}) => (
  <div style={{display: "flex", gap: 18, justifyContent: "center", flexWrap: "nowrap"}}>
    {palabras.map((p) => (
      <div
        key={p}
        style={{
          background: "rgba(255,255,255,0.94)",
          borderRadius: 999,
          padding: `${size * 0.58}px ${size * 1.2}px`,
          fontFamily: SANS,
          fontSize: size,
          fontWeight: 400,
          letterSpacing: "0.05em",
          textTransform: "uppercase",
          color: TINTA,
          whiteSpace: "nowrap",
          lineHeight: 1,
        }}
      >
        {p}
      </div>
    ))}
  </div>
);

// --- CTA en píldora oscura traslúcida, caja baja (c-04-09-4 de Carlos) --------
const PildoraOscura: React.FC<{size?: number; children: React.ReactNode}> = ({size = 30, children}) => (
  <div
    style={{
      display: "inline-block",
      background: "rgba(16,22,18,0.55)",
      border: "1px solid rgba(255,255,255,0.25)",
      borderRadius: 999,
      padding: `${size * 0.62}px ${size * 1.35}px`,
      fontFamily: SANS,
      fontSize: size,
      fontWeight: 300,
      color: "#FFFFFF",
      whiteSpace: "nowrap",
      lineHeight: 1,
    }}
  >
    {children}
  </div>
);

// --- Píldora de ubicación con borde (pin + mayúsculas espaciadas) -------------
const PildoraPin: React.FC<{size?: number; solidaOliva?: boolean; children: React.ReactNode}> = ({
  size = 26,
  solidaOliva = false,
  children,
}) => (
  <div
    style={{
      display: "inline-flex",
      alignItems: "center",
      gap: size * 0.5,
      background: solidaOliva ? `${OLIVA}E6` : "rgba(255,255,255,0.06)",
      border: solidaOliva ? "none" : "1.4px solid rgba(255,255,255,0.85)",
      borderRadius: 999,
      padding: `${size * 0.68}px ${size * 1.3}px`,
    }}
  >
    <Icono id="pin" d={size * 1.1} grosor={1.6} />
    <span
      style={{
        fontFamily: SANS,
        fontSize: size,
        fontWeight: 400,
        letterSpacing: "0.08em",
        textTransform: "uppercase",
        color: "#FFFFFF",
        whiteSpace: "nowrap",
        lineHeight: 1,
      }}
    >
      {children}
    </span>
  </div>
);

// Bloque de texto ARRIBA, centrado — el cambio nº 1 del rediseño.
const Cielo: React.FC<{f: FmtPC; top?: number; gap?: number; anim?: boolean; children: React.ReactNode}> = ({
  f,
  top,
  gap = 26,
  anim = false,
  children,
}) => {
  const z = ZONAS_PC[f];
  const t = top ?? ranuraY(z) + 64;
  return (
    <div
      style={{
        position: "absolute",
        left: z.inset + 56,
        right: z.inset + 56,
        top: t,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        textAlign: "center",
        gap,
      }}
    >
      {anim ? <Entrada activo delay={6}>{children}</Entrada> : children}
    </div>
  );
};

// Zona inferior centrada para píldoras/CTA (respeta el borde del marco).
const Pie: React.FC<{f: FmtPC; alto?: number; gap?: number; children: React.ReactNode}> = ({
  f,
  alto = 210,
  gap = 18,
  children,
}) => {
  const z = ZONAS_PC[f];
  return (
    <div
      style={{
        position: "absolute",
        left: z.inset + 40,
        right: z.inset + 40,
        bottom: z.inset + 40,
        height: alto,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "flex-end",
        gap,
      }}
    >
      {children}
    </div>
  );
};

// =============================================================================
// POSTS DE PRUEBA · 4:5 — un frame = una pieza (mismo truco que Piezas.tsx)
// =============================================================================

// P1 — portada: IA golden hour, titular en el cielo + caja café + pin oliva.
const P1Portada: React.FC = () => (
  <AbsoluteFill style={{background: "#0C1210"}}>
    <Foto src="assets/tierracalma/ia/e5_tarde.png" foco="50% 78%" />
    <Degradado tipo="arriba" fuerza={1.3} />
    <Degradado tipo="abajo" fuerza={0.5} />
    <MarcoPC f="4x5" variante="hueco" />
    <LogoAlto f="4x5" />
    <Cielo f="4x5" gap={22}>
      <Ligera size={60} caps>
        LA VIDA QUE QUIERES
      </Ligera>
      <Remate size={92}>YA TIENE DIRECCIÓN.</Remate>
      <div style={{height: 6}} />
      <CajaColor color={CAFE} size={33}>
        A 30 MINUTOS DE SANTIAGO
      </CajaColor>
    </Cielo>
    <Pie f="4x5" alto={120}>
      <PildoraPin size={25} solidaOliva>
        TIERRA CALMA · PADRE HURTADO
      </PildoraPin>
    </Pie>
  </AbsoluteFill>
);

// P2 — la cifra + píldoras de palabra: aéreo IA con cielo amplio.
const P2Cifra: React.FC = () => (
  <AbsoluteFill style={{background: "#0C1210"}}>
    <Foto src="assets/tierracalma/ia/e2_1_parcela.png" foco="50% 68%" />
    <Degradado tipo="arriba" fuerza={1.25} />
    <Degradado tipo="abajo" fuerza={0.55} />
    <MarcoPC f="4x5" variante="hueco" />
    <LogoAlto f="4x5" />
    <Cielo f="4x5" gap={20}>
      <Ligera size={56} caps>
        UN TERRENO DE
      </Ligera>
      <Cifra size={158}>5.000 m²</Cifra>
      <div style={{height: 4}} />
      <PillFila palabras={["HUERTA", "FRUTALES", "QUINCHO"]} />
      <div
        style={{
          fontFamily: SANS,
          fontSize: 33,
          fontWeight: 300,
          lineHeight: 1.4,
          color: "rgba(255,255,255,0.94)",
          maxWidth: 680,
          textShadow: "0 2px 26px rgba(0,0,0,0.45)",
        }}
      >
        Espacio para la casa, el jardín y lo que venga después.
      </div>
    </Cielo>
    <Pie f="4x5" alto={120}>
      <PildoraOscura size={29}>Escríbenos por WhatsApp</PildoraOscura>
    </Pie>
  </AbsoluteFill>
);

// P3 — tríptico vertical (c-04-09-2): tres fotos, texto abajo sobre scrim.
const P3Triptico: React.FC = () => {
  // El panel central es foto real de dron (mañana nublada): lleva su propio
  // grade cálido para no leerse de otra marca junto a las dos IA golden hour.
  const paneles: {src: string; foco: string; calida?: boolean}[] = [
    {src: "assets/tierracalma/ia/e2_2_casa.png", foco: "44% 60%"},
    {src: "assets/tierracalma/fotos/f_camino.jpg", foco: "50% 50%", calida: true},
    {src: "assets/tierracalma/ia/e2_4_quincho.png", foco: "56% 55%"},
  ];
  return (
    <AbsoluteFill style={{background: "#0C1210"}}>
      <div style={{position: "absolute", inset: 0, display: "flex"}}>
        {paneles.map((p, i) => (
          <div key={p.src} style={{position: "relative", width: "33.333%", height: "100%", overflow: "hidden"}}>
            <Img
              src={staticFile(p.src)}
              style={{
                width: "100%",
                height: "100%",
                objectFit: "cover",
                objectPosition: p.foco,
                filter: p.calida ? "sepia(0.52) hue-rotate(-6deg) saturate(1.18) contrast(1.07) brightness(0.9)" : undefined,
              }}
            />
            {p.calida ? (
              <div
                style={{
                  position: "absolute",
                  inset: 0,
                  background: "linear-gradient(180deg, rgba(255,186,110,0.5), rgba(255,160,92,0.32))",
                  mixBlendMode: "soft-light",
                }}
              />
            ) : null}
            {i > 0 ? (
              <div style={{position: "absolute", left: 0, top: 0, bottom: 0, width: 2, background: "rgba(255,255,255,0.9)"}} />
            ) : null}
          </div>
        ))}
      </div>
      <Degradado tipo="abajo" fuerza={1.15} />
      <MarcoPC f="4x5" variante="bandas" />
      <div
        style={{
          position: "absolute",
          left: 94,
          right: 94,
          bottom: 128,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          textAlign: "center",
          gap: 22,
        }}
      >
        <Ligera size={52} caps>
          UN SOLO TERRENO,
        </Ligera>
        <Remate size={78}>TRES PLANES DISTINTOS.</Remate>
        <div style={{height: 2}} />
        <PillFila palabras={["LA CASA", "LA HUERTA", "EL QUINCHO"]} size={24} />
        <div
          style={{
            fontFamily: SANS,
            fontSize: 32,
            fontWeight: 300,
            lineHeight: 1.4,
            color: "rgba(255,255,255,0.94)",
            textShadow: "0 2px 26px rgba(0,0,0,0.45)",
          }}
        >
          Y espacio de sobra para cambiar de idea.
        </div>
      </div>
    </AbsoluteFill>
  );
};

// P4 — cierre con evidencia real: la placa de corten del acceso. Sin logo
// (ya está grabado en la placa); marco cerrado y CTA en píldora oscura.
const P4Cierre: React.FC = () => (
  <AbsoluteFill style={{background: "#0C1210"}}>
    <Foto src="assets/tierracalma/fotos/f_placa.jpg" foco="50% 42%" escala={1.04} />
    {/* La foto viene del rodaje nublado: calidez para sacarle el verde frío */}
    <AbsoluteFill
      style={{
        background: "linear-gradient(180deg, rgba(255,190,120,0.34), rgba(255,164,96,0.22))",
        mixBlendMode: "soft-light",
        pointerEvents: "none",
      }}
    />
    <AbsoluteFill style={{background: "rgba(255,176,104,0.05)", mixBlendMode: "overlay", pointerEvents: "none"}} />
    <Degradado tipo="arriba" fuerza={0.8} />
    <Degradado tipo="abajo" fuerza={0.7} />
    <MarcoPC f="4x5" variante="cerrado" />
    <Cielo f="4x5" top={168} gap={24}>
      <Ligera size={58} caps>
        ESTO NO ES UN RENDER.
      </Ligera>
      <CajaColor color={OLIVA} size={34}>
        ES TU PRÓXIMA DIRECCIÓN.
      </CajaColor>
    </Cielo>
    <Pie f="4x5" alto={120}>
      <PildoraOscura size={29}>Agenda tu visita por WhatsApp</PildoraOscura>
    </Pie>
  </AbsoluteFill>
);

const POSTS: React.FC[] = [P1Portada, P2Cifra, P3Triptico, P4Cierre];
export const PRUEBA_POSTS = ["p1_portada", "p2_cifra", "p3_triptico", "p4_cierre"];

export const PruebaPosts4x5: React.FC = () => {
  const i = Math.min(useCurrentFrame(), POSTS.length - 1);
  const Pieza = POSTS[i];
  return <Pieza />;
};

// =============================================================================
// HISTORIA 9:16 — estructura de st-24-09: bajada + serif + caja oliva arriba,
// pin con borde + caja blanca de CTA abajo. `anim` = versión historia animada.
// =============================================================================

export const PruebaHistoria: React.FC<{anim?: boolean}> = ({anim = false}) => (
  <AbsoluteFill style={{background: "#0C1210"}}>
    <Foto
      src="assets/tierracalma/ia/h1_primavera.png"
      foco="50% 72%"
      escala={anim ? undefined : 1}
      kb={anim ? [1.14, 1.0] : undefined}
      kbDur={200}
    />
    <Degradado tipo="arriba" fuerza={1.35} />
    <Degradado tipo="abajo" fuerza={0.8} />
    <MarcoPC f="9x16" variante="hueco" />
    <LogoAlto f="9x16" />
    <Cielo f="9x16" gap={26} anim={anim}>
      <div
        style={{
          fontFamily: SANS,
          fontSize: 45,
          fontWeight: 300,
          lineHeight: 1.32,
          color: "#FFFFFF",
          textShadow: "0 2px 30px rgba(0,0,0,0.42)",
          maxWidth: 760,
        }}
      >
        La primavera se disfruta el doble
      </div>
      <Remate size={82}>EN TU PROPIA PARCELA.</Remate>
      <div style={{height: 8}} />
      <CajaColor color={OLIVA} size={34}>
        PARCELAS DESDE UF 2.500
      </CajaColor>
    </Cielo>
    <Pie f="9x16" alto={300} gap={22}>
      {anim ? (
        <Entrada activo delay={40}>
          <PieHistoria />
        </Entrada>
      ) : (
        <PieHistoria />
      )}
    </Pie>
  </AbsoluteFill>
);

const PieHistoria: React.FC = () => (
  <div style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 22, width: "100%"}}>
    <PildoraPin size={26}>TIERRA CALMA · PADRE HURTADO</PildoraPin>
    <div
      style={{
        background: "rgba(255,255,255,0.95)",
        borderRadius: 36,
        padding: "30px 52px",
        fontFamily: SANS,
        fontSize: 34,
        fontWeight: 400,
        lineHeight: 1.42,
        color: TINTA,
        textAlign: "center",
      }}
    >
      Elige la tuya hoy.
      <br />
      Escríbenos por WhatsApp.
    </div>
  </div>
);

export const PRUEBA_HISTORIA_ANIM_DURATION = 210; // 7 s

// =============================================================================
// REEL DE PRUEBA · 30 s — dron gradeado + IA, texto en el cielo, cajas de
// color, píldoras de palabra y cierre con la placa real + logo motion.
// =============================================================================

const CUTS = {
  camino: {from: 0, dur: 140},
  valle: {from: 140, dur: 150},
  loteo: {from: 290, dur: 140},
  casa: {from: 430, dur: 140},
  porteria: {from: 570, dur: 140},
  placa: {from: 710, dur: 90},
  logo: {from: 800, dur: 100},
};
export const PRUEBA_REEL_DURATION = CUTS.logo.from + CUTS.logo.dur; // 900 = 30 s

// Bloque de texto del reel: arriba, centrado, dentro de la zona segura.
const CieloReel: React.FC<{top?: number; gap?: number; children: React.ReactNode}> = ({
  top = 300,
  gap = 24,
  children,
}) => (
  <div
    style={{
      position: "absolute",
      left: 112,
      right: 112,
      top,
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      textAlign: "center",
      gap,
    }}
  >
    {children}
  </div>
);

const MusicaReel: React.FC = () => {
  const frame = useCurrentFrame();
  const v = Math.min(
    interpolate(frame, [0, 24], [0, 1], {extrapolateRight: "clamp"}),
    interpolate(frame, [PRUEBA_REEL_DURATION - 70, PRUEBA_REEL_DURATION - 6], [1, 0], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    }),
  );
  return <Audio src={staticFile(TC.music.sweetSeptember)} volume={v * 0.7} loop />;
};

export const PruebaReel: React.FC = () => {
  const frame = useCurrentFrame();
  // El marco y el logo acompañan todo el reel y se retiran antes del logo motion.
  const opMarco = interpolate(frame, [CUTS.placa.from + 70, CUTS.logo.from], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{background: "#0C1210"}}>
      {/* 1 · Camino al loteo — el gancho */}
      <Scene cut={CUTS.camino}>
        <Clip src="assets/tierracalma/drone/tc_llano.mp4" dur={CUTS.camino.dur} zoom={[1.06, 1.16]} />
        <Grade strength={0.9} calido={1.5} />
        <Inner>
          <CieloReel>
            <Reveal delay={10}>
              <Ligera size={56} caps>
                LA CIUDAD QUEDA CERCA.
              </Ligera>
            </Reveal>
            <Reveal delay={26}>
              <Remate size={94}>LA CALMA, MÁS CERCA.</Remate>
            </Reveal>
          </CieloReel>
        </Inner>
      </Scene>

      {/* 2 · Valle — el dato de conectividad en caja café */}
      <Scene cut={CUTS.valle}>
        <Clip src="assets/tierracalma/drone/tc_valle_amplio.mp4" dur={CUTS.valle.dur} zoom={[1.05, 1.14]} pan={[-24, 0]} />
        <Grade strength={0.9} calido={1.5} />
        <Inner>
          <CieloReel gap={28}>
            <Reveal delay={8}>
              <CajaColor color={CAFE} size={44}>
                A 30 MIN DE SANTIAGO
              </CajaColor>
            </Reveal>
            <Reveal delay={26}>
              <Etiqueta size={27}>RUTA 78 · SALIDA PADRE HURTADO</Etiqueta>
            </Reveal>
          </CieloReel>
        </Inner>
      </Scene>

      {/* 3 · Loteo cenital — la cifra + píldoras de palabra */}
      <Scene cut={CUTS.loteo}>
        <Clip src="assets/tierracalma/drone/tc_casas_verde.mp4" dur={CUTS.loteo.dur} zoom={[1.12, 1.04]} />
        <Grade strength={1.05} calido={1.4} />
        <Inner>
          <CieloReel gap={22}>
            <Reveal delay={8}>
              <Ligera size={52} caps>
                PARCELAS DE
              </Ligera>
            </Reveal>
            <Reveal delay={20}>
              <Cifra size={172}>5.000 m²</Cifra>
            </Reveal>
            <Reveal delay={40}>
              <PillFila palabras={["HUERTA", "FRUTALES", "QUINCHO"]} size={26} />
            </Reveal>
          </CieloReel>
        </Inner>
      </Scene>

      {/* 4 · IA estilo de vida — la promesa */}
      <Scene cut={CUTS.casa}>
        <ClipFoto src="assets/tierracalma/ia/e2_2_casa.png" dur={CUTS.casa.dur} zoom={[1.16, 1.05]} foco="50% 62%" />
        <Degradado tipo="arriba" fuerza={1.15} />
        <Inner>
          <CieloReel>
            <Reveal delay={10}>
              <Ligera size={56} caps>
                TU CASA, TU RITMO,
              </Ligera>
            </Reveal>
            <Reveal delay={26}>
              <Remate size={94}>TU PROYECTO.</Remate>
            </Reveal>
          </CieloReel>
        </Inner>
      </Scene>

      {/* 5 · Portería — el precio */}
      <Scene cut={CUTS.porteria}>
        <Clip src="assets/tierracalma/drone/tc_porteria_frontal.mp4" dur={CUTS.porteria.dur} zoom={[1.05, 1.13]} />
        <Grade strength={0.95} calido={1.5} />
        <Inner>
          <CieloReel gap={20}>
            <Reveal delay={8}>
              <Etiqueta size={28}>DESDE</Etiqueta>
            </Reveal>
            <Reveal delay={18}>
              <Cifra size={180}>UF 2.500</Cifra>
            </Reveal>
            <Reveal delay={38}>
              <CajaColor color={OLIVA} size={36}>
                PADRE HURTADO · RM
              </CajaColor>
            </Reveal>
          </CieloReel>
        </Inner>
      </Scene>

      {/* 6 · La placa real — evidencia + CTA */}
      <Scene cut={CUTS.placa}>
        <Clip src="assets/tierracalma/drone/tc_acceso_placa.mp4" dur={CUTS.placa.dur} zoom={[1.02, 1.08]} />
        <Grade strength={0.8} calido={1.3} />
        <Inner>
          <div style={{position: "absolute", left: 0, right: 0, bottom: 340, display: "flex", justifyContent: "center"}}>
            <Reveal delay={8}>
              <PildoraOscura size={33}>Agenda tu visita por WhatsApp</PildoraOscura>
            </Reveal>
          </div>
        </Inner>
      </Scene>

      {/* Marco + logo persistentes (el sello del carrusel llevado a video) */}
      <AbsoluteFill style={{opacity: opMarco, pointerEvents: "none"}}>
        <MarcoPC f="9x16" variante="hueco" op={0.75} />
        <LogoAlto f="9x16" />
      </AbsoluteFill>

      <Grain id="grain-prueba" opacity={0.05} />

      {/* Cierre oficial: logo motion, nunca re-animado */}
      <Sequence from={CUTS.logo.from} durationInFrames={CUTS.logo.dur} layout="none">
        <LogoOutro dur={CUTS.logo.dur} />
      </Sequence>

      <MusicaReel />
    </AbsoluteFill>
  );
};
