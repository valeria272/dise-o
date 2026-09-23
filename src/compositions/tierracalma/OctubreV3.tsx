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

/**
 * El marco teñido. El PNG del diseñador es BLANCO; sobre un fondo crema
 * desaparece y el carrusel deja de leerse como un objeto continuo. Se usa el
 * mismo archivo como MÁSCARA sobre un div del color que haga falta: la
 * geometría bloqueada no se toca, sólo cambia el color de la tinta.
 */
const MarcoTenido: React.FC<{archivo: string; color: string}> = ({archivo, color}) => (
  <div
    style={{
      position: "absolute",
      inset: 0,
      backgroundColor: color,
      WebkitMaskImage: `url(${MARCO(archivo)})`,
      maskImage: `url(${MARCO(archivo)})`,
      WebkitMaskSize: "100% 100%",
      maskSize: "100% 100%",
      WebkitMaskRepeat: "no-repeat",
      maskRepeat: "no-repeat",
    }}
  />
);

const Marco: React.FC<{archivo: string}> = ({archivo}) => (
  <Img
    src={MARCO(archivo)}
    style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "fill"}}
  />
);

/**
 * ⛔ TODO CENTRADO AL MEDIO (Diego, 23-09). El bloque de texto se centra
 * vertical y horizontalmente en el alto ÚTIL del marco — el que queda entre el
 * logo y la píldora — en vez de colgar de un `top` fijo. Así una frase corta y
 * una larga quedan igual de equilibradas sin recalcular nada a mano.
 */
const Cuerpo: React.FC<{
  desde?: number;
  hasta?: number;
  ancho?: number;
  alinea?: "center" | "flex-start";
  children: React.ReactNode;
}> = ({desde = 230, hasta = 1140, ancho = 880, alinea = "center", children}) => (
  <div
    style={{
      position: "absolute",
      left: "50%",
      transform: "translateX(-50%)",
      top: desde,
      height: hasta - desde,
      width: ancho,
      display: "flex",
      flexDirection: "column",
      alignItems: alinea,
      justifyContent: "center",
      textAlign: alinea === "center" ? "center" : "left",
    }}
  >
    {children}
  </div>
);

/** Un tramo del titular. Sólo dos roles: sans de cuerpo o IvyOra destacada. */
type Tramo = {
  t: string;
  /** IvyOra Display. Es LA forma de destacar una frase — y va siempre en versales. */
  ivy?: boolean;
  cursiva?: boolean;
  size?: number;
  salto?: boolean;
};

/**
 * ⛔ LA ESCALA (Diego, 23-09). Dos reglas y ninguna excepción:
 *
 *   · **Inter Tight varía entre 50 y 70 pt según el LARGO de la frase.** Frase
 *     corta = 70; frase larga = 50. No se elige a ojo: lo calcula `cuerpoSans`
 *     con el número de caracteres, así dos piezas con frases parecidas quedan
 *     al mismo cuerpo sin que nadie las compare a mano.
 *   · **IvyOra Display va a un tamaño FIJO** (`IVY`), no varía.
 *
 * El objetivo es que las dos tipografías se lean a una escala SIMILAR en las
 * portadas de carrusel y en los posts individuales — antes la cursiva saltaba
 * a 96-104 pt y aplastaba a la sans.
 */
const SANS_MIN = 50;
const SANS_MAX = 70;
/** IvyOra Display: tamaño fijo, dentro del mismo rango que la sans. */
const IVY = 68;

const cuerpoSans = (texto: string) => {
  const n = texto.replace(/\s+/g, " ").trim().length;
  const t = Math.min(Math.max((n - 24) / 72, 0), 1); // 24 car. → 70 · 96 → 50
  return Math.round(SANS_MAX - t * (SANS_MAX - SANS_MIN));
};

const Modulado: React.FC<{tramos: Tramo[]; base?: number; ancho?: number}> = ({
  tramos,
  base,
  ancho = 860,
}) => {
  // El cuerpo sale del largo de TODA la frase, contando los dos roles: lo que
  // manda es cuánto texto hay que leer, no de qué tipografía es cada tramo.
  const cuerpo = base ?? cuerpoSans(tramos.map((t) => t.t).join(" "));
  return (
  <div
    style={{
      width: ancho,
      textAlign: "center",
      color: "#fff",
      lineHeight: 1.16,
      textShadow: "0 2px 24px rgba(0,0,0,0.5)",
    }}
  >
    {tramos.map((tr, i) => (
      <React.Fragment key={i}>
        {tr.salto ? <br /> : null}
        <span
          style={{
            fontFamily: tr.ivy ? SERIF : SANS,
            fontStyle: tr.ivy && tr.cursiva ? "italic" : "normal",
            fontWeight: tr.ivy ? 500 : 300,
            fontSize: tr.ivy ? tr.size ?? IVY : tr.size ?? cuerpo,
            letterSpacing: tr.ivy ? "0.01em" : "0.005em",
            // ⛔ REGLA DURA (Diego, 22-09): IvyOra Display SIEMPRE en versales.
            textTransform: tr.ivy ? "uppercase" : "none",
          }}
        >
          {tr.t}
        </span>
      </React.Fragment>
    ))}
    </div>
  );
};

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

/**
 * ⛔ EL GLOBO DE TEXTO — el único recuadro de la marca.
 *
 * Ronda de Diego del 22-09: "que sea un globo de texto", "siempre el recuadro
 * que tenga transparencia", "globo de textos que estén derechos y centrados,
 * quitar espacios libres", "no genera contraste, oscurecer un poco más".
 *
 * Las cinco condiciones, y ninguna es opcional:
 *   1. translúcido (nunca color macizo)   2. oscuro de verdad, para que el
 *   texto blanco despegue   3. derecho, cero rotación   4. centrado
 *   5. ajustado al texto: inline-block + maxWidth, nunca width fijo
 */
const Globo: React.FC<{
  /** Fila del lienzo donde se ancla. Si se omite, el globo va EN FLUJO: entra
      dentro de `Cuerpo` y se centra junto con el titular, como un bloque más.
      Diego, 23-09 sobre `c-20-10-5`: "centrar toda la información". */
  y?: number;
  max?: number;
  size?: number;
  centrado?: boolean;
  op?: number;
  /** Línea destacada del globo: IvyOra Display versales, arriba del cuerpo. */
  destacado?: string;
  children: React.ReactNode;
}> = ({y, max = 760, size = 38, centrado = true, op = 0.58, destacado, children}) => (
  <div
    style={
      y === undefined
        ? {display: "flex", justifyContent: "center"}
        : {position: "absolute", top: y, left: 0, right: 0, display: "flex", justifyContent: "center"}
    }
  >
    <div
      style={{
        display: "inline-block",
        maxWidth: max,
        backgroundColor: `rgba(9,20,28,${op})`,
        backdropFilter: "blur(18px)",
        WebkitBackdropFilter: "blur(18px)",
        border: "1px solid rgba(255,255,255,0.18)",
        borderRadius: 34,
        padding: "30px 38px",
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: size,
        lineHeight: 1.3,
        color: "#fff",
        textAlign: centrado ? "center" : "left",
        whiteSpace: "pre-line",
        boxShadow: "0 22px 50px rgba(0,0,0,0.34)",
      }}
    >
      {destacado ? (
        <div
          style={{
            fontFamily: SERIF,
            fontStyle: "italic",
            fontWeight: 500,
            fontSize: Math.round(size * 1.45),
            lineHeight: 1.06,
            textTransform: "uppercase",
            color: "#fff",
            // Diego (23-09): "interlineado mas juntos". Era 16.
            marginBottom: 8,
          }}
        >
          {destacado}
        </div>
      ) : null}
      {children}
    </div>
  </div>
);

/** Pastilla de CTA con contorno — el remate de los carruseles. */
const Pastilla: React.FC<{y: number; icono?: React.ReactNode; children: React.ReactNode}> = ({
  y,
  icono,
  children,
}) => (
  <div
    style={{
      position: "absolute",
      left: "50%",
      top: y,
      transform: "translateX(-50%)",
      display: "flex",
      alignItems: "center",
      gap: 14,
      border: "1.5px solid rgba(255,255,255,0.85)",
      borderRadius: 999,
      padding: "16px 38px",
    }}
  >
    {icono}
    <span
      style={{
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 28,
        letterSpacing: "0.1em",
        color: "#fff",
        textTransform: "uppercase",
        whiteSpace: "nowrap",
      }}
    >
      {children}
    </span>
  </div>
);

/**
 * Burbuja de conversación blanca con colita. Excepción declarada al globo
 * translúcido de la marca: el brief del 09/10 pide "dos grandes globos de
 * conversación blancos".
 */
const Burbuja: React.FC<{
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
// LAS PIEZAS · ronda de Diego del 22-09
//
// SISTEMA TIPOGRÁFICO: dos roles y nada más (manual § "ORDEN TIPOGRÁFICO").
//   · cuerpo     → Inter Tight Light, caja baja
//   · destacado  → IvyOra Display VERSALES, cuerpo mayor
// Prohibido el bold de la sans para destacar y más de tres tamaños por pieza.
//
// RECUADROS: un solo `Globo`, translúcido, oscuro, derecho, centrado y
// ajustado al texto. Excepción declarada: los globos de conversación del
// 09/10, que el brief pide blancos y con colita.
// =============================================================================

const E1: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("e-portada")} foco="50% 55%" />
    <Degradado arriba={0.6} abajo={0.38} />
    <Marco archivo="MARCO-CARRUSEL-1" />
    <Cuerpo desde={250} hasta={1150}>
      <Modulado
        ancho={880}
        tramos={[{t: "¿Dudas antes de comprar"}, {t: "tu parcela?", salto: true}]}
      />
      <Aire h={26} />
      <Modulado ancho={900} tramos={[{t: "Aquí las resolvemos", ivy: true, cursiva: true}]} />
    </Cuerpo>
  </Lienzo>
);

const E2: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("e-luz")} foco="50% 52%" />
    <Degradado arriba={0.56} abajo={0.4} />
    <Marco archivo="MARCO-CARRUSEL-2" />
    <Cuerpo desde={205} hasta={1150}>
      <Modulado
        ancho={880}
        tramos={[
          {t: "¿Tengo que invertir en la"},
          {t: "electrificación", ivy: true, salto: true},
          {t: "del terreno?", salto: true},
        ]}
      />
    </Cuerpo>
    <Globo y={900} max={720} size={40}>
      {"No, la electricidad subterránea\nya está instalada."}
    </Globo>
  </Lienzo>
);

const E3: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("e-cierre")} foco="50% 50%" />
    <Degradado arriba={0.56} abajo={0.4} />
    <Marco archivo="MARCO-CARRUSEL-3" />
    <Cuerpo desde={205} hasta={1150}>
      <Modulado
        ancho={880}
        tramos={[{t: "¿Tengo que "}, {t: "cerrar", ivy: true}, {t: "yo el terreno?", salto: true}]}
      />
    </Cuerpo>
    <Globo y={900} max={700} size={40}>
      {"No, el cierre perimetral\nya está hecho."}
    </Globo>
  </Lienzo>
);

const E4: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("e-casas")} foco="50% 54%" />
    <Degradado arriba={0.58} abajo={0.52} />
    <Marco archivo="MARCO-CARRUSEL-4" />
    {/* Diego (23-09): "subir un poco, que no tape las casas". Centrado, pero
        dentro del cielo: la techumbre de la casa grande arranca en la fila 574
        y la chimenea en la 554 (medido sobre e-casas.jpg, que va 1:1 con el
        lienzo). El bloque cierra en 532. */}
    <Cuerpo desde={205} hasta={700}>
      <Modulado
        ancho={880}
        tramos={[{t: "¿Cuántas "}, {t: "casas", ivy: true}, {t: "puedo construir?", salto: true}]}
      />
    </Cuerpo>
    {/* Diego: "van juntos ambos textos". En el brief es UNA sola oración
        ("Hasta dos por parcela: la tuya y la de tus visitas"), así que la
        respuesta y su aclaración van en el mismo globo. */}
    <Globo y={850} max={740} size={36} destacado="Hasta dos por parcela">
      la tuya y la de tus visitas.
    </Globo>
    <Pastilla y={1150} icono={<IPin s={34} />}>
      Tu parcela en Padre Hurtado espera por ti
    </Pastilla>
  </Lienzo>
);

// =============================================================================
// F · 08/10 · HISTORIA · "¿Buscando una parcela en Padre Hurtado?" · Pilar 4
// =============================================================================

const F: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <Foto src={OCT("f-fondo")} foco="50% 50%" />
    <Degradado arriba={0.44} abajo={0.46} velo={0.16} />
    <Marco archivo="MARCO-ST" />
    {/* Diego: "bloque de textos alineados al centro-medio". Todo el bloque
        —titular, remate y globo— se centra vertical y horizontalmente en el
        alto útil del marco, en vez de colgar del logo. */}
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 200,
        height: 1380,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: "0 110px",
      }}
    >
      <Modulado
        ancho={840}
        tramos={[{t: "¿Buscando una parcela"}, {t: "en Padre Hurtado?", salto: true}]}
      />
      <Aire h={24} />
      <Modulado
        ancho={880}
        tramos={[
          {t: "La mejor forma de saberlo", ivy: true, cursiva: true},
          {t: "es venir a conocerla", ivy: true, cursiva: true, salto: true},
        ]}
      />
      <Aire h={44} />
      <div
        style={{
          display: "inline-block",
          maxWidth: 760,
          backgroundColor: "rgba(9,20,28,0.58)",
          backdropFilter: "blur(18px)",
          WebkitBackdropFilter: "blur(18px)",
          border: "1px solid rgba(255,255,255,0.18)",
          borderRadius: 34,
          padding: "30px 38px",
          fontFamily: SANS,
          fontWeight: 300,
          fontSize: 35,
          lineHeight: 1.36,
          color: "#fff",
          textAlign: "center",
          whiteSpace: "pre-line",
          boxShadow: "0 22px 50px rgba(0,0,0,0.34)",
        }}
      >
        {"Recorre las parcelas disponibles\nConoce el entorno y accesos\nResuelve tus dudas sobre el proceso de compra"}
      </div>
    </div>
    <Pildora caja={STORY.pill} icono={<IWsp s={28} />} size={31}>
      Agenda tu visita
    </Pildora>
  </Lienzo>
);

// =============================================================================
// G · 09/10 · POST 4:5 · fin de semana largo · Pilar 2
// Excepción declarada: el brief pide "dos grandes globos de conversación
// blancos", así que acá el globo NO es el translúcido oscuro de la marca.
// =============================================================================

const G: React.FC = () => (
  <Lienzo w={POST.w} h={POST.h}>
    <Foto src={OCT("g-pareja")} foco="50% 55%" />
    <Degradado arriba={0.4} abajo={0.44} velo={0.1} />
    <Marco archivo="MARCO-POST" />
    <Burbuja x={112} y={280} w={600} cola="izq">
      ¿Qué hacemos este fin de semana largo?
    </Burbuja>
    <Burbuja x={368} y={480} w={620} cola="der">
      Vamos a conocer esa parcela que tenemos guardada
    </Burbuja>
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 1108,
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 30,
        letterSpacing: "0.18em",
        textTransform: "uppercase",
        color: "rgba(255,255,255,0.92)",
        textShadow: "0 2px 18px rgba(0,0,0,0.55)",
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
// H · 12/10 · HISTORIA · Santiago → Padre Hurtado · Pilar 2
// Diego: "colocar en transparencia el MAPA-3 para la ubicación del lugar".
// MAPA-3 es cartografía REAL (a diferencia de MAPA-1 y 2, que traen los
// topónimos corruptos): va en transparencia sobre el azul de marca y encima
// sólo nuestros rótulos.
// =============================================================================

const H: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <AbsoluteFill style={{backgroundColor: TC.colors.navy}} />
    {/* MAPA-3 en transparencia */}
    <div style={{position: "absolute", left: 0, right: 0, top: 560, height: 620, overflow: "hidden"}}>
      {/* Diego: "al mapa hay que cambiarle el color como las versiones de
          mapa-1 y mapa-2" — va el duotono, no la captura cruda. */}
      <Img
        src={OCT("mapa3-story")}
        style={{width: "100%", height: "100%", objectFit: "cover", opacity: 0.62}}
      />
      <AbsoluteFill
        style={{
          background: `linear-gradient(to bottom, ${TC.colors.navy} 0%, rgba(11,44,73,0.55) 14%, rgba(11,44,73,0) 34%, rgba(11,44,73,0) 66%, rgba(11,44,73,0.55) 86%, ${TC.colors.navy} 100%)`,
        }}
      />
    </div>
    {/* nuestros rótulos, los únicos legibles */}
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 740,
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 32,
        letterSpacing: "0.3em",
        textTransform: "uppercase",
        color: "rgba(255,255,255,0.85)",
      }}
    >
      Santiago
    </div>
    <div style={{position: "absolute", left: 0, right: 0, top: 812, display: "flex", justifyContent: "center"}}>
      <div style={{width: 1, height: 116, backgroundColor: TC.colors.sand}} />
    </div>
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 852,
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 24,
        letterSpacing: "0.26em",
        textTransform: "uppercase",
        color: TC.colors.sand,
      }}
    >
      <span style={{backgroundColor: TC.colors.navy, padding: "0 16px"}}>Ruta 78</span>
    </div>
    <div style={{position: "absolute", left: 0, right: 0, top: 946, display: "flex", justifyContent: "center", alignItems: "center", gap: 14}}>
      <IPin s={36} />
      <span
        style={{
          fontFamily: SERIF,
          fontStyle: "italic",
          fontWeight: 500,
          fontSize: 54,
          textTransform: "uppercase",
          color: "#fff",
        }}
      >
        Tierra Calma
      </span>
    </div>
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 1016,
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 26,
        letterSpacing: "0.22em",
        textTransform: "uppercase",
        color: "rgba(255,255,255,0.8)",
      }}
    >
      Padre Hurtado
    </div>

    {/* la foto editorial, abajo */}
    <div style={{position: "absolute", left: 0, right: 0, top: 1210, height: 710, overflow: "hidden"}}>
      <Img src={OCT("h-casa")} style={{width: "100%", height: "100%", objectFit: "cover"}} />
      <AbsoluteFill
        style={{
          background: `linear-gradient(to bottom, ${TC.colors.navy} 0%, rgba(11,44,73,0.6) 12%, rgba(11,44,73,0.08) 34%, rgba(11,44,73,0.5) 74%, rgba(11,44,73,0.95) 100%)`,
        }}
      />
    </div>
    <Marco archivo="MARCO-ST" />
    {/* Banda alta: acá el medio lo ocupa el mapa. Centrado a 1520 el titular
        caía justo encima de los rótulos SANTIAGO y TIERRA CALMA.
        ⛔ Y no puede empezar antes de la fila 250: ahí Meta pone su interfaz.
        Con `desde={230}` el titular arrancaba en la 228 y la compuerta lo marcó
        como bloqueante — la única pieza de octubre que pisaba la zona segura. */}
    <Cuerpo desde={275} hasta={560}>
      <Modulado
        ancho={880}
        tramos={[
          {t: "Cerca de Santiago.", ivy: true, cursiva: true},
          {t: "Más cerca de la tranquilidad.", ivy: true, cursiva: true, salto: true},
        ]}
      />
      <Aire h={22} />
      <Bajada size={32} ancho={780}>
        Padre Hurtado te permite seguir conectado con la ciudad, con el espacio y la calma que
        buscas para vivir.
      </Bajada>
    </Cuerpo>
    {/* En globo: suelta sobre la foto no generaba contraste. */}
    <Globo y={1420} max={720} size={30} op={0.62}>
      Parcelas de aprox. 5.000 m² desde UF 2.500
    </Globo>
    <Pildora caja={STORY.pill} icono={<IPin s={28} />} size={31}>
      Conoce el proyecto
    </Pildora>
  </Lienzo>
);

// =============================================================================
// J · 15/10 · HISTORIA · "Eso que estabas buscando" · Pilar 2
// Diego: "juntar ambos bloques, es una búsqueda" — la barra y las sugerencias
// son un solo objeto, como en un buscador de verdad.
// =============================================================================

const Sugerida: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      display: "flex",
      alignItems: "center",
      gap: 14,
      padding: "15px 0",
      borderTop: "1px solid rgba(255,255,255,0.18)",
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: 30,
      color: "rgba(255,255,255,0.94)",
    }}
  >
    <svg width={21} height={21} viewBox="0 0 24 24" fill="none" style={{flexShrink: 0, opacity: 0.75}}>
      <circle cx="11" cy="11" r="6.6" stroke="#fff" strokeWidth="1.6" />
      <path d="M16 16l4.5 4.5" stroke="#fff" strokeWidth="1.6" strokeLinecap="round" />
    </svg>
    {children}
  </div>
);

const J: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <Foto src={OCT("j-fondo")} foco="50% 48%" />
    <Degradado arriba={0.5} abajo={0.5} />
    <Marco archivo="MARCO-ST" />

    {/* UN solo bloque: barra + sugerencias. Es una búsqueda, no dos cosas. */}
    <Globo y={330} max={840} size={33} centrado={false}>
      <div style={{display: "flex", alignItems: "center", gap: 18, paddingBottom: 20}}>
        <svg width={32} height={32} viewBox="0 0 24 24" fill="none" style={{flexShrink: 0}}>
          <circle cx="11" cy="11" r="6.6" stroke="#fff" strokeWidth="1.7" />
          <path d="M16 16l4.5 4.5" stroke="#fff" strokeWidth="1.7" strokeLinecap="round" />
        </svg>
        <span style={{fontFamily: SANS, fontWeight: 400, fontSize: 34, color: "#fff", lineHeight: 1.25}}>
          ¿Dónde vivir con más espacio cerca de Santiago?
        </span>
      </div>
      <Sugerida>Más naturaleza sin alejarme de la ciudad</Sugerida>
      <Sugerida>Un lugar tranquilo para construir mi casa</Sugerida>
      <Sugerida>Parcelas en Padre Hurtado</Sugerida>
    </Globo>

    <Globo y={1130} max={840} size={30} centrado={false}>
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 300,
          fontSize: 24,
          letterSpacing: "0.2em",
          textTransform: "uppercase",
          color: "rgba(255,255,255,0.7)",
          marginBottom: 18,
        }}
      >
        Resultado
      </div>
      <div style={{display: "flex", alignItems: "center", gap: 22}}>
        <Img
          src={OCT("l-fondo")}
          style={{width: 140, height: 140, objectFit: "cover", borderRadius: 22, flexShrink: 0}}
        />
        <div>
          <div
            style={{
              fontFamily: SERIF,
              fontStyle: "italic",
              fontWeight: 500,
              fontSize: 46,
              color: "#fff",
              textTransform: "uppercase",
            }}
          >
            Tierra Calma
          </div>
          <div style={{fontFamily: SANS, fontWeight: 300, fontSize: 27, color: "rgba(255,255,255,0.86)"}}>
            Padre Hurtado · Región Metropolitana
          </div>
          <div style={{fontFamily: SANS, fontWeight: 300, fontSize: 29, color: "#fff", marginTop: 10}}>
            El espacio que estabas buscando.
          </div>
        </div>
      </div>
    </Globo>

    <Pildora caja={STORY.pill} icono={<IPin s={28} />} size={31}>
      Conoce Tierra Calma
    </Pildora>
  </Lienzo>
);

// =============================================================================
// K · 20/10 · CARRUSEL 6 SLIDES · qué revisar antes de elegir · Pilar 2
// =============================================================================

const Numero: React.FC<{n: string}> = ({n}) => (
  <div
    style={{
      fontFamily: SERIF,
      fontStyle: "italic",
      fontWeight: 400,
      fontSize: 58,
      textTransform: "uppercase",
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
    <Foto src={OCT("k-persona")} foco="50% 52%" />
    <Degradado arriba={0.6} abajo={0.4} />
    <Marco archivo="MARCO-CARRUSEL-1" />
    {/* Diego (23-09): "subir un poco, que no tape a las personas ni el terreno".
        El cielo limpio de k-persona.jpg llega hasta la fila ~620 y la pareja
        empieza en la 780; el bloque cierra en 589, sobre cielo. */}
    <Cuerpo desde={250} hasta={670}>
      <Modulado
        ancho={880}
        tramos={[{t: "¿Estás pensando en"}, {t: "comprar una parcela?", salto: true}]}
      />
      <Aire h={24} />
      <Modulado ancho={900} tramos={[{t: "No mires solo los m²", ivy: true, cursiva: true}]} />
    </Cuerpo>
    <Globo y={920} max={760} size={35}>
      Hay otros aspectos que deberías considerar antes de decidir.
    </Globo>
  </Lienzo>
);

const K2: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    {/* Diego, 2ª vuelta: "el mapa que cubra toda la composición". Va a sangre,
        no en banda. MAPA-3 es la cartografía real, recoloreada al duotono
        crema→navy de MAPA-1 y MAPA-2. */}
    {/* 13%: deja el pin que ya trae el mapa justo bajo nuestro rótulo. A 46%
        quedaba al borde y se leían DOS pines, el del mapa y el nuestro. */}
    <Foto src={OCT("mapa3-duo")} foco="13% 50%" />
    {/* velos de lectura, arriba y abajo, sobre el propio mapa */}
    <AbsoluteFill
      style={{
        background: `linear-gradient(to bottom, rgba(243,238,227,0.96) 0%, rgba(243,238,227,0.9) 22%, rgba(243,238,227,0.1) 42%, rgba(243,238,227,0.12) 58%, rgba(243,238,227,0.92) 78%, rgba(243,238,227,0.97) 100%)`,
      }}
    />
    <MarcoTenido archivo="MARCO-CARRUSEL-2" color={TC.colors.navy} />
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: CARR.sinLogo,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        textAlign: "center",
        color: TC.colors.navy,
      }}
    >
      <div style={{fontFamily: SERIF, fontStyle: "italic", fontWeight: 400, fontSize: 58, textTransform: "uppercase", color: TC.colors.brown}}>
        01.
      </div>
      <Aire h={16} />
      <div style={{width: 880, lineHeight: 1.16}}>
        <span style={{fontFamily: SANS, fontWeight: 300, fontSize: 46}}>¿Qué tan </span>
        <span style={{fontFamily: SERIF, fontWeight: 500, fontSize: 60, textTransform: "uppercase"}}>conectado</span>
        <br />
        <span style={{fontFamily: SANS, fontWeight: 300, fontSize: 46}}>estarás?</span>
      </div>
    </div>
    {/* el pin sobre el mapa, con nuestro rótulo */}
    {/* El pin propio va EXACTAMENTE sobre el que ya trae el mapa (medido: canvas
        382,590 con el encuadre al 13 %), así se lee uno solo y no dos. */}
    <div
      style={{
        position: "absolute",
        left: 352,
        top: 566,
        display: "flex",
        alignItems: "center",
        gap: 12,
        // base crema: sin ella el rótulo gris que ya trae el mapa se
        // transparentaba por detrás del nuestro y se leían los dos.
        backgroundColor: TC.colors.cream,
        padding: "8px 20px 8px 12px",
        borderRadius: 999,
      }}
    >
      <IPin s={34} c={TC.colors.navy} />
      <span style={{fontFamily: SERIF, fontStyle: "italic", fontWeight: 500, fontSize: 46, textTransform: "uppercase", color: TC.colors.navy}}>
        Tierra Calma
      </span>
    </div>
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 1040,
        padding: "0 140px",
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 34,
        lineHeight: 1.32,
        color: TC.colors.ink,
      }}
    >
      Revisa accesos, vías principales y qué tan fácil será mantener tu rutina desde tu nueva
      ubicación.
      <div style={{marginTop: 18, fontSize: 28, letterSpacing: "0.14em", textTransform: "uppercase", color: TC.colors.brown}}>
        Padre Hurtado · RM
      </div>
    </div>
  </Lienzo>
);

/** Recorte fotográfico del collage de servicios. Derecho, sin rotación. */
const Recorte: React.FC<{src: string; x: number; y: number; w: number; label: string}> = ({
  src,
  x,
  y,
  w,
  label,
}) => (
  <div style={{position: "absolute", left: x, top: y, width: w}}>
    <div style={{backgroundColor: "#FBF8F2", padding: 9, boxShadow: "0 12px 26px rgba(0,0,0,0.22)"}}>
      <Img src={OCT(src)} style={{width: "100%", height: w - 18, objectFit: "cover", display: "block"}} />
    </div>
    <div
      style={{
        marginTop: 10,
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 23,
        letterSpacing: "0.16em",
        textTransform: "uppercase",
        color: TC.colors.navy,
      }}
    >
      {label}
    </div>
  </div>
);

const K3: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    {/* Diego, 2ª vuelta: "eliminar la imagen de fondo y dejar fondo de color de
        la paleta, imágenes derechas y texto fuera del globo". Fondo crema, los
        cuatro recortes sin rotación y el cierre en texto plano, sin globo. */}
    <AbsoluteFill style={{backgroundColor: TC.colors.cream}} />
    <MarcoTenido archivo="MARCO-CARRUSEL-3" color={TC.colors.navy} />
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: CARR.sinLogo,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        textAlign: "center",
        color: TC.colors.navy,
      }}
    >
      <div style={{fontFamily: SERIF, fontStyle: "italic", fontWeight: 400, fontSize: 58, textTransform: "uppercase", color: TC.colors.brown}}>
        02.
      </div>
      <Aire h={16} />
      <div style={{width: 880, lineHeight: 1.16}}>
        <span style={{fontFamily: SANS, fontWeight: 300, fontSize: 48}}>¿Qué tienes </span>
        <span style={{fontFamily: SERIF, fontWeight: 500, fontSize: 62, textTransform: "uppercase"}}>cerca</span>
        <span style={{fontFamily: SANS, fontWeight: 300, fontSize: 48}}>?</span>
      </div>
    </div>
    {/* los cuatro recortes, derechos y en retícula */}
    <Recorte src="sv-super" x={178} y={470} w={312} label="Supermercados" />
    <Recorte src="sv-salud" x={590} y={470} w={312} label="Salud" />
    <Recorte src="sv-colegio" x={178} y={845} w={312} label="Colegios" />
    <Recorte src="sv-comercio" x={590} y={845} w={312} label="Comercio" />
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 1212,
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 31,
        lineHeight: 1.3,
        color: TC.colors.ink,
      }}
    >
      Tranquilidad no debería significar aislamiento.
    </div>
  </Lienzo>
);

/** Indicador gráfico: punto, línea guía y rótulo. Señala sobre la foto. */
const Indicador: React.FC<{x: number; y: number; lado: "izq" | "der"; children: React.ReactNode}> = ({
  x,
  y,
  lado,
  children,
}) => (
  <div
    style={{
      position: "absolute",
      // El que apunta desde la izquierda se ancla por la DERECHA: si no, el
      // rótulo crece hacia afuera del lienzo y se corta ("ACCESO CONTROL...").
      ...(lado === "izq" ? {right: 1080 - x} : {left: x}),
      top: y,
      display: "flex",
      flexDirection: lado === "izq" ? "row-reverse" : "row",
      alignItems: "center",
      gap: 0,
    }}
  >
    <div style={{width: 11, height: 11, borderRadius: 999, backgroundColor: "#fff", boxShadow: "0 0 0 5px rgba(255,255,255,0.28)"}} />
    <div style={{width: 46, height: 1, backgroundColor: "rgba(255,255,255,0.85)"}} />
    <span
      style={{
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 27,
        letterSpacing: "0.1em",
        textTransform: "uppercase",
        color: "#fff",
        whiteSpace: "nowrap",
        textShadow: "0 2px 14px rgba(0,0,0,0.85)",
      }}
    >
      {children}
    </span>
  </div>
);

const K4: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    {/* Diego: "fotografía aérea de una parcela con pequeños indicadores
        gráficos señalando sus características". */}
    {/* Diego, 2ª vuelta: "mucho más lejana del lugar, imagen tipo dron, que
        sea un terreno limpio sin vegetación, listo para construir". */}
    <Foto src={OCT("k-parcela-limpia")} foco="50% 50%" />
    <Degradado arriba={0.6} abajo={0.46} />
    <Marco archivo="MARCO-CARRUSEL-2" />
    {/* Banda alta: en esta slide el medio lo ocupan los indicadores sobre la
        parcela, así que el titular se centra en el espacio que queda libre.
        Centrado a 1150 caía justo encima de "CIERRE PERIMETRAL". */}
    <Cuerpo desde={205} hasta={570}>
      <Numero n="03." />
      <Aire h={16} />
      <Modulado
        ancho={880}
        tramos={[{t: "¿Qué "}, {t: "incluye", ivy: true}, {t: "realmente tu parcela?", salto: true}]}
      />
    </Cuerpo>
    {/* ⚠️ "Rol individual" y "Acceso controlado" van con el OK de Diego y
        siguen sin confirmación escrita de Fran o Blanca. */}
    <Indicador x={252} y={640} lado="der">
      Cierre perimetral
    </Indicador>
    <Indicador x={846} y={772} lado="izq">
      Acceso controlado
    </Indicador>
    <Indicador x={214} y={900} lado="der">
      Electricidad
    </Indicador>
    <Indicador x={868} y={1024} lado="izq">
      Rol individual
    </Indicador>
    {/* Diego (23-09): "no sobrepasar el limite de la linea". Anclado en 1140 el
        globo cerraba en la fila 1312 y la linea inferior del marco esta en la
        1284: la cruzaba por 28 px. Con el interlineado nuevo mide 164 px de
        alto, asi que 1085 lo deja cerrando en 1249 — 35 px por dentro. */}
    <Globo y={1085} max={520} size={34} destacado="Aprox. 5.000 m²">
      por parcela
    </Globo>
  </Lienzo>
);

const K5: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={OCT("k-planos")} foco="50% 50%" />
    <Degradado arriba={0.64} abajo={0.44} />
    <Marco archivo="MARCO-CARRUSEL-3" />
    {/* Diego (23-09): "centrar toda la informacion". Horizontalmente ya estaba
        (desvio maximo medido: 1,5 px); lo que no estaba centrado era el
        CONJUNTO: el titular quedaba a media altura y el globo colgaba abajo,
        con 450 px de vacio arriba y 90 abajo. Aca el globo entra EN FLUJO
        dentro de `Cuerpo`, asi que numero + titular + globo se centran como un
        solo grupo. La banda es simetrica respecto de las lineas del marco
        (filas 131 y 1284): 74 px de aire arriba y abajo. */}
    <Cuerpo desde={205} hasta={1210}>
      <Numero n="04." />
      <Aire h={16} />
      <Modulado
        ancho={880}
        tramos={[
          {t: "¿Tienes claridad sobre"},
          {t: "el proceso de ", salto: true},
          {t: "compra", ivy: true},
          {t: "?"},
        ]}
      />
      <Aire h={46} />
      <Globo max={790} size={35} destacado="En Tierra Calma te acompañamos">
        {"Antes de avanzar, pregunta por documentación, reserva, formas de pago y escrituración."}
      </Globo>
    </Cuerpo>
  </Lienzo>
);

const K6: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    {/* Diego: "pareja caminando dentro de Tierra Calma, con una toma amplia
        que permita dimensionar el espacio" — van pequeños en el cuadro a
        propósito: lo que se mide es el terreno alrededor. */}
    <Foto src={OCT("k-caminando")} foco="50% 52%" />
    <Degradado arriba={0.6} abajo={0.54} />
    <Marco archivo="MARCO-CARRUSEL-4" />
    {/* Diego (23-09): "subir un poco el bloque de texto, que no tape a las
        personas". Las cabezas de la pareja estan en la fila ~672 de
        k-caminando.jpg; el bloque cierra en 617. */}
    <Cuerpo desde={205} hasta={790}>
      <Numero n="05." />
      <Aire h={16} />
      <Modulado ancho={880} tramos={[{t: "Y lo más importante:"}]} />
      <Aire h={18} />
      <Modulado ancho={900} tramos={[{t: "conócela en persona", ivy: true, cursiva: true}]} />
    </Cuerpo>
    <Globo y={880} max={770} size={34} destacado="Parcelas desde UF 2.500">
      {"El entorno, los accesos y las dimensiones del terreno se entienden mucho mejor cuando estás ahí."}
    </Globo>
    <Pastilla y={1170} icono={<IWsp s={30} />}>
      Agenda tu visita por WhatsApp
    </Pastilla>
  </Lienzo>
);

// =============================================================================
// L · 22/10 · HISTORIA · crédito preaprobado · Pilar 3
// Diego: "globo de textos que estén derechos y centrados, quitar espacios
// libres de los globos". Cero rotación y ajustados al texto.
// =============================================================================

const L: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <Foto src={OCT("l-fondo")} foco="50% 50%" />
    <Degradado arriba={0.54} abajo={0.5} />
    <Marco archivo="MARCO-ST" />
    {/* Diego (23-09): "subir bloque de texto". Centrado a 1520 el titular caia
        a 70 px del primer globo y dejaba 640 px de cielo vacio arriba. La banda
        del titular termina donde EMPIEZA el globo (1020), que es el espacio que
        de verdad le queda libre. */}
    <Cuerpo desde={240} hasta={1020}>
      <Modulado
        ancho={880}
        tramos={[{t: "¿Ya tienes tu"}, {t: "crédito preaprobado", ivy: true, salto: true}, {t: "?"}]}
      />
    </Cuerpo>
    <Globo y={1020} max={780} size={36}>
      {"Conoce las parcelas disponibles y las alternativas para avanzar en tu compra."}
    </Globo>
    <Globo y={1270} max={700} size={34} destacado="Parcelas desde UF 2.500">
      Tierra Calma · Padre Hurtado
    </Globo>
    <Pildora caja={STORY.pill} icono={<IWsp s={28} />} size={30}>
      Conversemos por WhatsApp
    </Pildora>
  </Lienzo>
);

// =============================================================================
// M · 29/10 · POST 4:5 · "Ese proyecto que tienes en mente" · Pilar 1
// El post-it y la polaroid son objetos físicos, no globos: van tal cual.
// =============================================================================

const M: React.FC = () => (
  <Lienzo w={POST.w} h={POST.h}>
    <Foto src={OCT("m-cocina")} foco="50% 45%" />
    <Degradado arriba={0.38} abajo={0.42} velo={0.06} />

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
      <Img src={OCT("f-fondo")} style={{width: "100%", height: 190, objectFit: "cover", display: "block"}} />
    </div>

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
          fontSize: 40,
          lineHeight: 1.16,
          textTransform: "uppercase",
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
          fontWeight: 300,
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
    {/* En globo: sobre la cocina clara la línea suelta se perdía. */}
    <Globo y={1058} max={760} size={29} op={0.6}>
      Aprox. 5.000 m² desde UF 2.500 · Padre Hurtado
    </Globo>
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
