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
/** ⚠️ Lo mismo, pero PNG. La tarjeta del mapa va sin comprimir: `mapa3.jpg` ya
 *  es JPEG y un segundo pase de compresión vuelve a ablandar los cantos de la
 *  cartografía, que es justo lo que Diego marcó como «pixelado». */
const OCT_PNG = (n: string) => staticFile(`assets/tierracalma/oct/${n}.png`);
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
 * ⭐ EL MARCO TEÑIDO POR TRAMOS.
 *
 * El marco es un **asset bloqueado**: no se redibuja, sólo se recolorea con
 * máscara. Pero cuando el fondo cambia de claro a oscuro dentro de la misma
 * pieza —el mapa es papel en la banda del medio y navy arriba y abajo— **un
 * filete de un solo color deja de verse en un tramo**. Así que se tiñe por
 * tramos, con `clipPath`, y el filete contrasta con lo que cruza.
 *
 * ⚠️ **Medir antes de usarlo:** sólo `MARCO-ST` lleva filete vertical.
 * `MARCO-CARRUSEL-2` tiene tinta únicamente en las filas 130 y 1285, que caen
 * sobre color macizo y no necesitan nada.
 *
 * `cortes` va en píxeles del lienzo y de arriba hacia abajo; el último `y` tiene
 * que ser el alto de la pieza.
 *
 * 🗄️ Historia: existió el 24-09, se retiró el 25-09 cuando el mapa pasó a trazos
 * sobre navy, y volvió el mismo día al volver el mapa a papel claro.
 */
const MarcoTramos: React.FC<{
  archivo: string;
  alto: number;
  cortes: {y: number; color: string}[];
}> = ({archivo, alto, cortes}) => (
  <>
    {cortes.map((c, i) => (
      <div
        key={c.y}
        style={{
          position: "absolute",
          inset: 0,
          clipPath: `inset(${i === 0 ? 0 : cortes[i - 1].y}px 0 ${alto - c.y}px 0)`,
        }}
      >
        <MarcoTenido archivo={archivo} color={c.color} />
      </div>
    ))}
  </>
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

/**
 * ⛔ «TIERRA CALMA» NUNCA SE PARTE ENTRE DOS LÍNEAS (Diego, 24-09-2026).
 * Vale para toda pieza, no sólo para el reel donde se detectó. Ver el gemelo en
 * `OctubreVideo.tsx` y la regla en el manual § Tipografía.
 */
const INDIVISIBLE = /(Tierra Calma|Padre Hurtado|UF\s[\d.]+|[\d.]+\sm²)/gi;

const sinPartir = (hijos: React.ReactNode): React.ReactNode => {
  if (typeof hijos !== "string") return hijos;
  return hijos
    .split(INDIVISIBLE)
    .map((parte, i) =>
      /^(tierra calma|padre hurtado|uf\s[\d.]+|[\d.]+\sm²)$/i.test(parte) ? (
        <span key={i} style={{whiteSpace: "nowrap"}}>
          {parte}
        </span>
      ) : (
        parte
      ),
    );
};

const Modulado: React.FC<{tramos: Tramo[]; base?: number; ancho?: number; tinta?: string}> = ({
  tramos,
  base,
  ancho = 860,
  tinta,
}) => {
  // El cuerpo sale del largo de TODA la frase, contando los dos roles: lo que
  // manda es cuánto texto hay que leer, no de qué tipografía es cada tramo.
  const cuerpo = base ?? cuerpoSans(tramos.map((t) => t.t).join(" "));
  return (
  <div
    style={{
      width: ancho,
      textAlign: "center",
      // `tinta` es para las slides de fondo crema: ahí el titular va en navy y
      // el halo —que existe para despegar el blanco de una foto— sobra.
      color: tinta ?? "#fff",
      lineHeight: 1.16,
      textShadow: tinta ? "none" : "0 2px 24px rgba(0,0,0,0.5)",
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
          {sinPartir(tr.t)}
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


/** Texto DENTRO del contorno de píldora que ya trae el marco. */
const Pildora: React.FC<{
  caja: {x: number; y: number; w: number; h: number};
  icono?: React.ReactNode;
  size?: number;
  /** Separación icono-texto. Se baja cuando el texto no cabe holgado. */
  gap?: number;
  /** ⚠️ Sobre campo CLARO hay que pasarla: el blanco por defecto desaparece. */
  tinta?: string;
  children: React.ReactNode;
}> = ({caja, icono, size = 30, gap = 13, tinta = "#fff", children}) => (
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
      gap,
    }}
  >
    {icono}
    <span
      style={{
        fontFamily: SANS,
        fontWeight: 500,
        fontSize: size,
        letterSpacing: "0.07em",
        color: tinta,
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
          {sinPartir(destacado)}
        </div>
      ) : null}
      {sinPartir(children)}
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

/** Doble check de WhatsApp: azul = visto. */
const ICheckWsp: React.FC = () => (
  <svg width={34} height={20} viewBox="0 0 34 20" fill="none" style={{flexShrink: 0}}>
    <path d="M2 11.2l4.6 4.6L17.6 4.8" stroke="#53BDEB" strokeWidth="2.2"
      strokeLinecap="round" strokeLinejoin="round" />
    <path d="M14.4 11.2l4.6 4.6L30 4.8" stroke="#53BDEB" strokeWidth="2.2"
      strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

/** El verde de la burbuja saliente de WhatsApp. */
const VERDE_WSP = "#D9FDD3";

/**
 * Burbuja de conversación con colita. Excepción declarada al globo translúcido
 * de la marca: el brief del 09/10 pide "dos grandes globos de conversación".
 *
 * Diego (23-09): *"la conversación no parece ser como de WhatsApp, debería
 * llevar el color, los check de enviado y visto"*. La burbuja SALIENTE —la de
 * la derecha, la que escribe quien publica— va en verde y cierra con el doble
 * check azul; la entrante se queda blanca, que es como se ven de verdad.
 */
const Burbuja: React.FC<{
  x: number;
  y: number;
  w: number;
  cola: "izq" | "der";
  children: React.ReactNode;
}> = ({x, y, w, cola, children}) => {
  const mia = cola === "der";
  const fondo = mia ? VERDE_WSP : "#fff";
  return (
    <div style={{position: "absolute", left: x, top: y, width: w}}>
      <div
        style={{
          backgroundColor: fondo,
          borderRadius: 34,
          padding: mia ? "26px 32px 18px" : "26px 32px",
          fontFamily: SANS,
          fontWeight: 400,
          fontSize: 38,
          lineHeight: 1.3,
          color: TC.colors.ink,
          boxShadow: "0 18px 44px rgba(0,0,0,0.26)",
        }}
      >
        {children}
        {mia ? (
          <div style={{display: "flex", justifyContent: "flex-end", marginTop: 6}}>
            <ICheckWsp />
          </div>
        ) : null}
      </div>
      <div
        style={{
          position: "absolute",
          bottom: -14,
          [cola === "izq" ? "left" : "right"]: 44,
          width: 30,
          height: 22,
          backgroundColor: fondo,
          clipPath: cola === "izq" ? "polygon(0 0, 100% 0, 30% 100%)" : "polygon(0 0, 100% 0, 70% 100%)",
        } as React.CSSProperties}
      />
    </div>
  );
};

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
    {/* ⭐ Diego (25-09): *"cambia a la pareja, de pose, de ropa, todo"*, manteniendo
        la idea. Sale `g-pareja` —de pie, centrados, quietos sobre pasto parejo— y
        entra `g-pareja2`: caminando de espaldas por el camino de ripio ocre, él
        abrazándola, ropa distinta. Generada con Seedream 5 Pro siguiendo el ADN
        del lugar (§ 4 bis): matorral nativo ralo pero en verde de primavera,
        cerros ocres SIN nieve, cerco de madera oscura horizontal, luminarias.
        ⚠️ Medido antes de instalarla: da como máximo **+0,654** contra cualquier
        otra imagen del mes (y +0,575 contra la que reemplaza), lejos del +0,85
        que marca «es la misma foto». */}
    <Foto src={OCT("g-pareja2")} foco="50% 55%" />
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
    {/* Diego (23-09, sobre p-09-10): "el boton esta muy apretado, debe ser mas
        ancho". El contorno de la pildora viene DIBUJADO dentro de
        MARCO-POST.png —asset bloqueado, no se puede ensanchar—, asi que lo que
        cede es el texto: medido, ocupaba 559 px de los 574 de la pildora, o sea
        9 px de aire a la izquierda y 6 a la derecha. Con estos valores baja a
        ~505 y deja ~34 px por lado. El CTA no se acorta: va verbatim del brief.
        Va en las DOS piezas de post, que comparten marco y texto. */}
    <Pildora caja={POST.pill} icono={<IWsp s={23} />} size={26} gap={11}>
      Agenda tu visita por WhatsApp
    </Pildora>
  </Lienzo>
);

// =============================================================================
// H · 12/10 · HISTORIA · Santiago → Padre Hurtado · Pilar 2
// Diego: "colocar en transparencia el MAPA-3 para la ubicación del lugar".
// MAPA-3 es la ÚNICA cartografía real que tiene la cuenta: MAPA-1 y MAPA-2
// salieron de IA y traen topónimos corruptos y escudos G-68.
// =============================================================================

/**
 * ⭐ H · 12/10 · HISTORIA — el mapa del lugar.
 *
 * ⛔ EL MAPA ES PAPEL Y VA A SANGRE (Diego, 24-09-2026, con referencia adjunta)
 * ──────────────────────────────────────────────────────────────────────────────
 * *"Mejoremos la forma en que mostramos el mapa, que se vea integrado de buena
 * forma y que se lea bien. Quita el pin de Tierra Calma, solo deja el del mapa
 * original."* Y después, con una pieza de la propia marca adjunta:
 * *"exactamente la pieza del 20-10-2 sigue esta referencia… mismo ejemplo para
 * el mapa de la st-12-10"*.
 *
 * La referencia está en `clients/tierra-calma/referencias/`. Su gramática:
 *
 *   · el mapa **a sangre**, ocupando el ancho completo
 *   · el mapa es **papel**: duotono a la LUZ del crema, con sus topónimos
 *     oscuros. Nunca al revés — un mapa oscuro sobre fondo oscuro es textura
 *   · el mapa **se disuelve** en el color de marca con degradado, sin borde
 *   · **ningún texto de la pieza se apoya sobre el mapa**: todos se apoyan sobre
 *     el color sólido en el que el mapa se deshace
 *   · la ubicación va en **píldora de contorno**, no en placa maciza
 *   · el filete del marco cambia de color según lo que cruza — ver `MarcoTramos`
 *
 * ⛔ LO QUE NO SE COPIÓ: **su mapa.** Ese es uno de los corruptos —dice «Los
 * Maitenss», «Av. El Goneuiualdde» y trae escudos **G-68** alrededor de Padre
 * Hurtado, justo el error que el manual persigue hace meses—. La cartografía
 * sigue saliendo de `MAPA-3`, que es real.
 *
 * ⭐ POR QUÉ SALE NUESTRO RÓTULO Y QUEDA EL DEL MAPA
 * ─────────────────────────────────────────────────
 * **Tierra Calma ya está en Google Maps.** MAPA-3 trae su pin rojo y su
 * etiqueta, puestos por Google. Nuestra píldora crema encima era una segunda
 * marca tapando la primera — y la primera vale más, porque es la prueba de que
 * el lugar existe y se puede buscar.
 *
 * El pin sobrevive al duotono porque `scripts/tc-mapas-duotono.py` lo aísla y lo
 * repone en su rojo original: es lo único cromático de la pieza. El resto del
 * mapa —incluido el POI rojo del CESFAM, que no es nuestro— se apaga.
 *
 * ⚠️ GEOMETRÍA. `mapa3-banda-st.jpg` es un recorte de 800×348 y la banda mide
 * 1080×470: **misma proporción**, así que el archivo se muestra 1:1. Si se
 * cambia la banda, se cambia el recorte en el script — no el `objectFit` acá.
 *
 * El script imprime **dónde cae cada topónimo en el lienzo**, y ese es el
 * control: el pin en (185, 842), Maipú en (952, 579) y Padre Hurtado en
 * (729, 910) tienen que quedar **dentro de la banda limpia** (565–930). Un
 * topónimo bajo el degradado es un topónimo que no se lee.
 *
 * Qué entra en el recorte, y por qué:
 *   · el pin (287,315), con aire alrededor
 *   · «Maipú» (855,120) — el ancla de Santiago que sostiene el titular. Sin
 *     ella, «CERCA DE SANTIAGO» es una afirmación que el mapa no respalda
 *   · «Padre Hurtado» (690,365) — el topónimo que la pieza nombra
 *   · el escudo de la **Ruta 78** (687,263) — la vía correcta, la que el manual
 *     persigue desde que una pieza publicó «Ruta 68»
 */

/** La banda del mapa: a sangre, y con su propia proporción de recorte. */
/**
 * ⭐ LA BANDA DEL MAPA — en TRAZOS desde el 25-09.
 *
 * `escala 1,0` y `desdeFila 110` no son a ojo: el contorno de la comuna ocupa las
 * filas **143-473** del archivo (330 px) y la banda mide 515, así que a escala
 * 1:1 entra completo —del 528 al 858 del lienzo— con aire por los dos lados. Y
 * 1:1 importa por sí solo: el archivo se muestra a su resolución nativa, sin
 * remuestrear. Un contorno cortado por el borde parece un error de encuadre.
 */
const MAPA = {top: 495, h: 515, escala: 1.0, desdeFila: 110};

/** Placa de dato, como las del pie de la referencia. */
const Placa: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      display: "inline-block",
      backgroundColor: "rgba(201,185,154,0.16)",
      padding: "11px 26px",
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: 27,
      letterSpacing: "0.04em",
      color: TC.colors.cream,
      textTransform: "uppercase",
      whiteSpace: "nowrap",
    }}
  >
    {children}
  </div>
);

const Fuerte: React.FC<{children: React.ReactNode}> = ({children}) => (
  <span style={{fontWeight: 600, color: "#fff"}}>{children}</span>
);

const H: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <AbsoluteFill style={{backgroundColor: TC.colors.navy}} />

    {/* ⭐ EL MAPA. Diego, 25-09: *"vuelve a tomar el mapa-padre hurtado, déjalo
        tal cual con el mismo efecto de color con el contraste de fondo, elimina
        los iconos"*. Es el archivo real en duotono de marca (`tc-mapa-ph.py`),
        no un trazado: tres vueltas de líneas extraídas por gradiente quedaron
        pixeladas y se descartaron. El degradado de los cuatro lados lo disuelve
        en el navy del lienzo, así que no hay canto ni caja. */}
    <div
      style={{
        position: "absolute",
        left: 0,
        top: MAPA.top,
        width: STORY.w,
        height: MAPA.h,
        overflow: "hidden",
      }}
    >
      <Img
        src={OCT("mapa-ph-banda-st")}
        style={{
          position: "absolute",
          left: (STORY.w - 893 * MAPA.escala) / 2,
          top: -MAPA.desdeFila * MAPA.escala,
          width: 893 * MAPA.escala,
          height: 631 * MAPA.escala,
          display: "block",
        }}
      />
      <AbsoluteFill
        style={{
          background: `linear-gradient(to bottom, ${TC.colors.navy} 0%, rgba(11,44,73,0) 11%,
                        rgba(11,44,73,0) 89%, ${TC.colors.navy} 100%),
                       linear-gradient(to right, ${TC.colors.navy} 0%, rgba(11,44,73,0) 15%,
                        rgba(11,44,73,0) 85%, ${TC.colors.navy} 100%)`,
        }}
      />
    </div>

    {/* ⭐ Titular sobre navy macizo, CENTRADO y con «CERCA DE SANTIAGO.» en una
        sola línea (Diego, 25-09). Vuelve a la regla de la cuenta —todo centrado
        al medio— de la que esta pieza se había salido al armarse sobre la
        referencia de Sonatta, que alineaba a la izquierda.
        ⚠️ La línea única no es sólo estética: ahorra 62 px de alto, y esos 62 px
        son los que dejan subir la banda del mapa de la fila 543 a la 495 y
        mostrarlo a escala 1:1 en vez de reducido al 90 %. */}
    <div style={{position: "absolute", left: 0, right: 0, top: 250, textAlign: "center"}}>
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 300,
          fontSize: 56,
          lineHeight: 1.1,
          letterSpacing: "0.005em",
          color: "#fff",
        }}
      >
        CERCA DE SANTIAGO.
      </div>
      <div
        style={{
          fontFamily: SERIF,
          fontStyle: "italic",
          fontWeight: 500,
          fontSize: IVY,
          lineHeight: 1.06,
          textTransform: "uppercase",
          color: "#fff",
          marginTop: 12,
          whiteSpace: "nowrap",
        }}
      >
        MÁS CERCA DE
        <br />
        LA TRANQUILIDAD
      </div>
    </div>

    {/* La ubicación, en píldora de contorno como la referencia.
        ⚠️ DOS COSAS MEDIDAS, NO ELEGIDAS:
        · Va **rellena de navy macizo**, no transparente. Con el mapa en trazos
          debajo, una píldora calada deja pasar los caminos por detrás del texto
          — que es exactamente lo que estas vueltas vinieron a prohibir.
        · Va en la fila 966 y no antes: el vértice sur del contorno comunal
          cierra en la 957 (495 + (572-110)×1,0). Trece píxeles más arriba y la
          píldora le corta la punta a la comuna. */}
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 970,
        display: "flex",
        justifyContent: "center",
      }}
    >
      <div
        style={{
          display: "inline-flex",
          alignItems: "center",
          gap: 13,
          backgroundColor: TC.colors.navy,
          border: `1px solid rgba(243,238,227,0.55)`,
          borderRadius: 999,
          padding: "13px 34px",
          fontFamily: SANS,
          fontWeight: 400,
          fontSize: 28,
          letterSpacing: "0.1em",
          textTransform: "uppercase",
          color: TC.colors.cream,
          whiteSpace: "nowrap",
        }}
      >
        <IPin s={26} c={TC.colors.cream} />
        Padre Hurtado · Región Metropolitana
      </div>
    </div>

    {/* la foto del sitio real */}
    <div
      style={{
        position: "absolute",
        left: 96,
        top: 1062,
        width: 888,
        height: 296,
        overflow: "hidden",
        borderRadius: "56px 0 56px 0",
      }}
    >
      {/* Diego (24-09): "cambiemos la imagen a una de las que se tomó con el
          dron". Sale el render IA de las dos casas y entra el sitio REAL: la
          aérea del 07-08, recortada y gradada por
          `scripts/tc-foto-dron-story.py`. A la izquierda el llano con sus
          parcelas, a la derecha la ladera con el camino de ripio. */}
      <Img
        src={OCT("h-dron")}
        style={{width: "100%", height: "100%", objectFit: "cover", display: "block"}}
      />
      <AbsoluteFill
        style={{
          background: "linear-gradient(to bottom, rgba(11,44,73,0) 45%, rgba(11,44,73,0.8) 100%)",
        }}
      />
    </div>

    {/* el remate, cruzando el borde inferior de la foto */}
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 1292,
        display: "flex",
        alignItems: "flex-end",
        justifyContent: "center",
        gap: 22,
      }}
    >
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 300,
          fontSize: 38,
          lineHeight: 1.12,
          color: TC.colors.cream,
          textAlign: "right",
          paddingBottom: 18,
        }}
      >
        A 15 minutos
        <br />
        del peaje
      </div>
      <div
        style={{
          fontFamily: SERIF,
          fontStyle: "italic",
          fontWeight: 500,
          fontSize: 92,
          lineHeight: 1,
          color: TC.colors.cream,
        }}
      >
        Padre Hurtado
      </div>
    </div>

    {/* las placas de datos */}
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 1424,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 10,
      }}
    >
      <Placa>
        Parcelas de <Fuerte>aprox. 5.000 m²</Fuerte> · desde <Fuerte>UF 2.500</Fuerte>
      </Placa>
      <Placa>
        Electricidad y cierre perimetral <Fuerte>ya instalados</Fuerte>
      </Placa>
    </div>

    {/* ⚠️ El marco, teñido por tramos: crema sobre el navy y navy sobre el mapa
        claro. Un filete crema cruzando el papel del mapa no se ve. Los cortes
        caen donde el degradado ya resolvió a un lado o al otro: la banda va de
        la 495 a la 1010 y abre y cierra en el 11 % y el 89 % de su alto. */}
    <MarcoTramos
      archivo="MARCO-ST"
      alto={STORY.h}
      cortes={[
        {y: 560, color: TC.colors.cream},
        {y: 950, color: TC.colors.navy},
        {y: STORY.h, color: TC.colors.cream},
      ]}
    />
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

/**
 * ⛔ LA CABECERA DEL CARRUSEL — número + titular, SIEMPRE en la misma fila.
 *
 * Diego, 23-09-2026: *"veo cada slide desarticulada; lo ideal sería que la
 * ubicación de cada número con el título estén en el mismo lugar que la slide 2,
 * que sería la principal del resto de los puntos"*.
 *
 * La slide 2 ancla en `CARR.sinLogo` (fila **205**) y esa es la referencia de
 * todo el carrusel. Por eso esta cabecera **NO se centra vertical**: un carrusel
 * es un solo objeto y, al deslizar, el número tiene que caer en la misma fila.
 * Es la excepción declarada a «todo centrado al medio» para las slides 2 a 6.
 *
 * Antes cada slide se maquetaba por su lado —dos a mano sobre crema y tres con
 * `Cuerpo` centrado— y por eso el número aparecía a tres alturas distintas.
 */
const Cabecera: React.FC<{
  n: string;
  /** `crema` = fondo de color, tinta navy y sin halo. `foto` = sobre fotografía. */
  sobre?: "foto" | "crema";
  children: React.ReactNode;
}> = ({n, sobre = "foto", children}) => (
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
    }}
  >
    <div
      style={{
        fontFamily: SERIF,
        fontStyle: "italic",
        fontWeight: 400,
        fontSize: 58,
        textTransform: "uppercase",
        color: sobre === "crema" ? TC.colors.brown : TC.colors.sand,
        lineHeight: 1,
        textShadow: sobre === "crema" ? "none" : "0 2px 18px rgba(0,0,0,0.5)",
      }}
    >
      {n}
    </div>
    <Aire h={16} />
    {children}
  </div>
);

const K1: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    {/* Diego (24-09): "cambiemos la foto de portada, es la misma que el post del
        09/10". Y lo era: medido, `k-persona` y `g-pareja` daban +0,933 de
        parecido visual — dos generaciones del mismo prompt. `k-portada` se
        generó con Seedream 5 Pro siguiendo el ADN del manual y da como máximo
        +0,754 contra cualquiera de las otras. Una persona sola, no pareja: la
        pareja ya sale en la slide 6 y en el post del 09/10.
        El cielo limpio llega hasta la fila 638 del lienzo; el titular cierra en
        la 589. */}
    <Foto src={OCT("k-portada")} foco="50% 50%" />
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

/**
 * ⭐ K2 · 20/10 · CARRUSEL 2/6 — «¿Qué tan conectado estarás?»
 *
 * ⛔ EL MAPA SE ROTULA, NO SE AMPLÍA (Diego, 25-09)
 * ─────────────────────────────────────────────────
 * *"Los textos del mapa se siguen viendo pixelados, si tienes que rediseñarlo
 * hazlo."* Y, en el mismo mensaje: *"no cambies el contenido, vuelve al texto de
 * antes"* — así que el panel de datos que había probado sale y vuelve la bajada.
 *
 * **La letra del mapa mide 11 px en el archivo.** Es una captura de pantalla:
 * once píxeles no dan para más, y el recorte ya iba 1:1, así que no había
 * escala que corregir. Borrarla para recomponerla tampoco resultó — ver el
 * detalle de los cuatro métodos probados en `scripts/tc-mapa-ph.py`.
 *
 * ⭐ **LO QUE SÍ RESUELVE: rotular encima.** El mapa queda intacto y la pieza
 * repone **sólo los nombres que la slide necesita**, en Inter Tight, con un velo
 * de papel detrás que tapa el original. Los demás topónimos quedan de textura,
 * que es su papel de todos modos. Un mapa diseñado rotula lo que la pieza dice,
 * no todo lo que hay.
 *
 * ⚠️ Los rótulos van por **coordenada medida sobre `mapa3.jpg`**, trasladada al
 * recorte de la tarjeta. Si cambia el recorte, hay que rehacer la traslación —
 * `ROTULO()` la hace en un solo lugar para que no se disperse.
 */

/** La tarjeta del mapa. `w`×`h` son EXACTAMENTE las del recorte: no se escala. */
const TARJETA_K2 = {x: 70, y: 470, w: 940, h: 500};
/** Esquina superior izquierda del recorte dentro de `mapa3.jpg`. */
const RECORTE_K2 = {x: 150, y: 90};
/** Pasa una coordenada de `mapa3.jpg` a píxeles del lienzo. */
const ROTULO = (x: number, y: number) => ({
  left: TARJETA_K2.x + x - RECORTE_K2.x,
  top: TARJETA_K2.y + y - RECORTE_K2.y,
});

/**
 * Un topónimo repuesto sobre el mapa. El `textShadow` no es un efecto: es el
 * velo de papel que tapa la letra original de la captura, del color del propio
 * mapa. Sin él se leerían las dos.
 */
const Toponimo: React.FC<{
  x: number;
  y: number;
  size?: number;
  peso?: number;
  children: React.ReactNode;
  ancla?: "centro" | "izq";
}> = ({x, y, size = 30, peso = 500, ancla = "centro", children}) => (
  <div
    style={{
      position: "absolute",
      ...ROTULO(x, y),
      // «izq» deja el rótulo A LA DERECHA del punto: es lo que necesita el de
      // Tierra Calma para no taparle el pin, que es el elemento que el material
      // ya trae y que Diego pidió conservar.
      transform: ancla === "izq" ? "translate(0, -50%)" : "translate(-50%, -50%)",
      whiteSpace: "nowrap",
      fontFamily: SANS,
      fontWeight: peso,
      fontSize: size,
      letterSpacing: "0.02em",
      color: "#12291F",
      textShadow:
        "0 0 7px #EDE7D8, 0 0 7px #EDE7D8, 0 0 12px #EDE7D8, 0 0 12px #EDE7D8, 0 0 18px #EDE7D8",
    }}
  >
    {children}
  </div>
);

const K2: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    {/* ⭐ Diego (24-09): "siento que quedan muy cortadas visualmente la 2da y la
        3ra de las demás, cambiar por el color VERDE del manual". */}
    <AbsoluteFill style={{backgroundColor: TC.colors.green}} />

    <Cabecera n="01.">
      <Modulado
        ancho={880}
        tinta={TC.colors.cream}
        tramos={[{t: "¿Qué tan "}, {t: "conectado", ivy: true}, {t: "estarás?", salto: true}]}
      />
    </Cabecera>

    {/* ⭐ LA TARJETA. El `<Img>` va con el tamaño exacto del archivo y sin
        `objectFit`: cualquier reescalado acá vuelve a ablandar la cartografía. */}
    <div
      style={{
        position: "absolute",
        left: TARJETA_K2.x,
        top: TARJETA_K2.y,
        width: TARJETA_K2.w,
        height: TARJETA_K2.h,
        borderRadius: 28,
        overflow: "hidden",
        boxShadow: "0 22px 44px rgba(0,0,0,0.34), inset 0 0 0 1px rgba(243,238,227,0.35)",
      }}
    >
      <Img
        src={OCT_PNG("mapa3-tarjeta-k2")}
        style={{width: TARJETA_K2.w, height: TARJETA_K2.h, display: "block"}}
      />
    </div>

    {/* Los rótulos repuestos. Coordenadas medidas sobre `mapa3.jpg`. */}
    <Toponimo x={306} y={315} size={31} peso={600} ancla="izq">
      {sinPartir("Tierra Calma")}
    </Toponimo>
    <Toponimo x={690} y={365} size={33} peso={600}>
      {sinPartir("Padre Hurtado")}
    </Toponimo>
    <Toponimo x={862} y={120} size={30}>
      Maipú
    </Toponimo>
    <Toponimo x={462} y={515} size={28}>
      Peñaflor
    </Toponimo>
    <Toponimo x={687} y={263} size={24} peso={600}>
      RUTA 78
    </Toponimo>

    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 1010,
        padding: "0 140px",
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 34,
        lineHeight: 1.32,
        color: TC.colors.cream,
      }}
    >
      Revisa accesos, vías principales y qué tan fácil será mantener tu rutina desde tu nueva
      ubicación.
      <div style={{marginTop: 18, fontSize: 28, letterSpacing: "0.14em", textTransform: "uppercase", color: TC.colors.sand}}>
        {sinPartir("Padre Hurtado")} · RM
      </div>
    </div>

    {/* El marco va crema entero: medido sobre el PNG, `MARCO-CARRUSEL-2` sólo
        lleva tinta en las filas 130 y 1285, y las dos caen sobre verde macizo. */}
    <MarcoTenido archivo="MARCO-CARRUSEL-2" color={TC.colors.cream} />
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
        // Sobre el verde de la slide, no sobre crema (Diego, 24-09).
        color: TC.colors.cream,
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
    {/* ⭐ Diego (24-09): al verde del manual, igual que la slide 2 — ver el
        comentario de `K2`. Los recortes fotográficos conservan su paspartú
        crema: sobre verde profundo funcionan como polaroids y son lo que le da
        el aire editorial a la slide. */}
    <AbsoluteFill style={{backgroundColor: TC.colors.green}} />
    <MarcoTenido archivo="MARCO-CARRUSEL-3" color={TC.colors.cream} />
    <Cabecera n="02.">
      <Modulado
        ancho={880}
        tinta={TC.colors.cream}
        tramos={[{t: "¿Qué tienes "}, {t: "cerca", ivy: true}, {t: "?"}]}
      />
    </Cabecera>
    {/* los cuatro recortes, derechos y en retícula */}
    {/* Diego (23-09): "hay mucho espacio entre ese titulo y las fotos". Bajaban
        de 470 y el titular cierra en ~363, o sea 107 px de hueco contra 31 que
        quedaban abajo. A 430 el reparto queda parejo: ~67 arriba, ~57 abajo. */}
    <Recorte src="sv-super" x={178} y={430} w={312} label="Supermercados" />
    <Recorte src="sv-salud" x={590} y={430} w={312} label="Salud" />
    <Recorte src="sv-colegio" x={178} y={805} w={312} label="Colegios" />
    <Recorte src="sv-comercio" x={590} y={805} w={312} label="Comercio" />
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
        color: TC.colors.cream,
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
    <Cabecera n="03.">
      <Modulado
        ancho={880}
        tramos={[{t: "¿Qué "}, {t: "incluye", ivy: true}, {t: "realmente tu parcela?", salto: true}]}
      />
    </Cabecera>
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
    <Cabecera n="04.">
      <Modulado
        ancho={880}
        tramos={[
          {t: "¿Tienes claridad sobre"},
          {t: "el proceso de ", salto: true},
          {t: "compra", ivy: true},
          {t: "?"},
        ]}
      />
    </Cabecera>
    {/* El globo vuelve a su ancla. El 23-09 a las 15:01 Diego pidió "centrar toda
        la información" y se metió EN FLUJO bajo el titular; esa misma tarde, al
        mirar el carrusel entero, pidió que el número y el título quedaran donde
        la slide 2. Manda lo segundo: el carrusel es un solo objeto. A 880 el
        globo cae donde el de la slide 6, que es el ritmo de la familia. */}
    <Globo y={880} max={790} size={35} destacado="En Tierra Calma te acompañamos">
      {"Antes de avanzar, pregunta por documentación, reserva, formas de pago y escrituración."}
    </Globo>
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
    {/* Diego (23-09): "que no tape a las personas". Con la cabecera anclada en
        205 el bloque cierra en ~440 y las cabezas de la pareja estan en la fila
        ~672 de k-caminando.jpg. */}
    <Cabecera n="05.">
      <Modulado ancho={880} tramos={[{t: "Y lo más importante:"}]} />
      <Aire h={18} />
      <Modulado ancho={900} tramos={[{t: "conócela en persona", ivy: true, cursiva: true}]} />
    </Cabecera>
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
// =============================================================================

/**
 * ⭐ L · 22/10 · HISTORIA — rehecha el 25-09 sobre la referencia que pasó Diego.
 *
 * *"Para la st del 22-10 haz la historia según esta referencia."* Guardada en
 * [`referencias/2026-09-25_ventana-lista.png`](../../../clients/tierra-calma/referencias/2026-09-25_ventana-lista.png).
 *
 * Su gramática, tal como se aplicó:
 *   · **campo claro**, no fotografía a sangre — acá el crema de marca
 *   · titular de **dos pesos**, alineado a la izquierda
 *   · la imagen dentro de una **tarjeta tipo ventana**: esquinas redondeadas,
 *     panel de color y la fila de tres puntos del cromo de un navegador
 *   · una **insignia flotante** con ícono, montada sobre la esquina de la tarjeta
 *   · el dato con **check en círculo**
 *
 * ⛔ **Lo que NO se copió: su bold para destacar.** La referencia destaca con la
 * sans en negrita; en esta marca **destaca IvyOra en versales** y sólo hay dos
 * roles tipográficos (§ 4, R-10/R-11). Copiar el recurso habría sido romper el
 * sistema por imitar a otra marca.
 *
 * ⛔ **Y no se inventó lista.** La referencia trae cuatro beneficios en checklist;
 * el copy de esta pieza tiene un dato. Va **una** fila con check —el destacado
 * que la pieza ya traía— y la firma debajo. Si la lista tiene que ser de cuatro,
 * los cuatro puntos los tiene que dar el brief.
 *
 * ⚠️ **El campo claro obliga a dos cosas que el resto de las piezas no necesita:**
 *   · el marco va **teñido en navy** (`MarcoTenido`): el PNG es crema y sobre
 *     crema desaparece — logo, filete y contorno de la píldora incluidos;
 *   · la píldora del CTA recibe `tinta`, porque su texto es blanco por defecto.
 *
 * ⚠️ La foto de la tarjeta es `h-telefono`, que en la entrega V3 estaba sin usar.
 * De paso resuelve que `l-fondo` estaba en DOS piezas del mes: el fondo de esta
 * y la miniatura del resultado de búsqueda de `st-15-10` (R-20).
 */

/** La tarjeta-ventana: panel de color con el cromo arriba y la foto dentro. */
const VENTANA = {x: 96, y: 760, w: 888, h: 620, aire: 28, cromo: 78};

const L: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <AbsoluteFill style={{backgroundColor: TC.colors.cream}} />

    {/* titular de dos pesos: la sans enuncia, IvyOra destaca */}
    <div style={{position: "absolute", left: 96, top: 350, width: 880}}>
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 300,
          fontSize: 58,
          lineHeight: 1.1,
          color: TC.colors.navy,
        }}
      >
        ¿Ya tienes tu
      </div>
      <div
        style={{
          marginTop: 10,
          fontFamily: SERIF,
          fontStyle: "italic",
          fontWeight: 500,
          fontSize: IVY,
          lineHeight: 1.06,
          textTransform: "uppercase",
          color: TC.colors.navy,
        }}
      >
        CRÉDITO
        <br />
        PREAPROBADO?
      </div>
    </div>

    <div
      style={{
        position: "absolute",
        left: 96,
        top: 620,
        width: 820,
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 34,
        lineHeight: 1.34,
        color: "rgba(11,44,73,0.82)",
      }}
    >
      Conoce las parcelas disponibles y las alternativas para avanzar en tu compra.
    </div>

    {/* ⭐ LA TARJETA-VENTANA */}
    <div
      style={{
        position: "absolute",
        left: VENTANA.x,
        top: VENTANA.y,
        width: VENTANA.w,
        height: VENTANA.h,
        borderRadius: 40,
        backgroundColor: TC.colors.green,
        boxShadow: "0 26px 50px rgba(11,44,73,0.18)",
      }}
    >
      {/* los tres puntos del cromo, a la derecha como en la referencia */}
      <div
        style={{
          position: "absolute",
          right: 44,
          top: VENTANA.cromo / 2 - 8,
          display: "flex",
          gap: 13,
        }}
      >
        {[0, 1, 2].map((i) => (
          <div
            key={i}
            style={{width: 16, height: 16, borderRadius: 999, backgroundColor: "rgba(243,238,227,0.75)"}}
          />
        ))}
      </div>
      <div
        style={{
          position: "absolute",
          left: VENTANA.aire,
          top: VENTANA.cromo,
          width: VENTANA.w - VENTANA.aire * 2,
          height: VENTANA.h - VENTANA.cromo - VENTANA.aire,
          borderRadius: 26,
          overflow: "hidden",
        }}
      >
        <Img
          src={OCT("h-telefono")}
          style={{width: "100%", height: "100%", objectFit: "cover", objectPosition: "50% 72%", display: "block"}}
        />
      </div>
    </div>

    {/* la insignia flotante, montada sobre la esquina de la tarjeta */}
    <div
      style={{
        position: "absolute",
        // ⚠️ Montada SOBRE la esquina de la tarjeta pero dentro del filete: a
        // la izquierda de la columna 96 el marco la corta.
        left: 128,
        top: 702,
        width: 118,
        height: 118,
        borderRadius: 32,
        backgroundColor: TC.colors.green,
        border: `10px solid ${TC.colors.cream}`,
        boxSizing: "border-box",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <IWsp s={52} c={TC.colors.cream} />
    </div>

    {/* el dato, con el check en círculo de la referencia */}
    <div
      style={{
        position: "absolute",
        left: 96,
        top: 1424,
        display: "flex",
        alignItems: "center",
        gap: 22,
      }}
    >
      <div
        style={{
          width: 58,
          height: 58,
          borderRadius: 999,
          backgroundColor: TC.colors.green,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          flexShrink: 0,
        }}
      >
        <ICheck s={30} c={TC.colors.cream} />
      </div>
      <span
        style={{
          fontFamily: SERIF,
          fontStyle: "italic",
          fontWeight: 500,
          fontSize: 44,
          textTransform: "uppercase",
          color: TC.colors.navy,
          whiteSpace: "nowrap",
        }}
      >
        {sinPartir("Parcelas desde UF 2.500")}
      </span>
    </div>

    <div
      style={{
        position: "absolute",
        left: 176,
        top: 1494,
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 30,
        letterSpacing: "0.12em",
        textTransform: "uppercase",
        color: "rgba(11,44,73,0.6)",
      }}
    >
      {sinPartir("Tierra Calma")} · {sinPartir("Padre Hurtado")}
    </div>

    {/* ⚠️ Marco TEÑIDO: el PNG es crema y sobre campo crema desaparece entero. */}
    <MarcoTenido archivo="MARCO-ST" color={TC.colors.navy} />
    <Pildora caja={STORY.pill} icono={<IWsp s={28} c={TC.colors.navy} />} size={30} tinta={TC.colors.navy}>
      Conversemos por WhatsApp
    </Pildora>
  </Lienzo>
);
// =============================================================================
// M · 29/10 · POST 4:5 · "Ese proyecto que tienes en mente" · Pilar 1
// El post-it y la polaroid son objetos físicos, no globos: van tal cual.
// =============================================================================

/**
 * ⭐ M · 29/10 · POST — los tres papeles del refrigerador.
 *
 * Diego, 24-09-2026: *"tiene que ser post-it pegados en el refrigerador como la
 * referencia, **que se vea real**"* y, después, *"el texto de Aprox. 5.000 m²
 * también que sea un post-it"*.
 *
 * ⛔ EL REPARTO DEL TRABAJO ES LA REGLA, NO UN DETALLE:
 *
 *   · **La IA hace el OBJETO** — la puerta, los tres papeles con su textura,
 *     arrugas, esquina enrollada y sombra de contacto, y los imanes.
 *   · **El código pone el CONTENIDO** — la fotografía dentro de la ventana de la
 *     polaroid y la letra encima de cada papel. Eso es dato, y el dato **nunca**
 *     lo escribe la IA.
 *
 * Por eso el fondo se generó con **los tres papeles en blanco**, y el prompt lo
 * dice tres veces: basta que el modelo escriba una palabra para que la pieza
 * quede con texto que nadie aprobó.
 *
 * El dato comercial ya no va en un recuadro de marca flotando sobre el acero:
 * **va escrito en la nota crema**, que es lo que Diego pidió. Es la única forma
 * de que la pieza no mezcle dos lenguajes —papel y gráfica— sobre el mismo
 * objeto.
 *
 * ⛔ LO QUE NO SE COPIÓ de la referencia: su nota chica dice «Sueña · Planifica ·
 * Hazlo · Realidad». Ese copy no está en el brief.
 *
 * ⚠️ GEOMETRÍA MEDIDA sobre `m-refri.jpg` (1770×2360), pasada al lienzo con
 * `cover` de 1080×1350 — escala **0,610** y `foco="50% 92%"`, que recorta **83
 * px** arriba. Ese 92 % no es estético: con el 50 % de siempre el post-it
 * cerraba en la fila 1243 y **se metía bajo la píldora del marco** (1212).
 *
 *   ventana polaroid  origen 366-818 · 578-985    → lienzo 223-499 · 270-518
 *   nota crema        origen 1028-1405 · 632-1098 → lienzo 627-857 · 303-587
 *   post-it           origen 401-1251 · 1304-2112 → lienzo 245-763 · 712-1205
 *   esquina enrollada origen x 1050+ · y 1850+    → lienzo x 558+ · y 1046+
 *
 * Cada papel lleva **su propia inclinación**, medida sobre el borde superior:
 * una foto derecha sobre un papel torcido se desborda por una esquina y delata
 * el montaje.
 */
const POLAROID = {x: 223, y: 270, w: 276, h: 248, giro: -8};
const NOTA = {x: 627, y: 303, w: 230, h: 284, giro: -5};
const POSTIT = {x: 245, y: 712, w: 518, h: 493, giro: -1.5};

const M: React.FC = () => (
  <Lienzo w={POST.w} h={POST.h}>
    <Foto src={OCT("m-refri")} foco="50% 92%" />

    {/* la fotografía DENTRO de la ventana de la polaroid, con su inclinación */}
    <div
      style={{
        position: "absolute",
        left: POLAROID.x,
        top: POLAROID.y,
        width: POLAROID.w,
        height: POLAROID.h,
        transform: `rotate(${POLAROID.giro}deg)`,
        overflow: "hidden",
      }}
    >
      <Img
        src={OCT("f-fondo")}
        style={{width: "100%", height: "100%", objectFit: "cover", display: "block"}}
      />
      <AbsoluteFill style={{backgroundColor: "rgba(120,96,64,0.12)"}} />
    </div>

    {/* ⭐ EL DATO COMERCIAL, escrito en la nota crema. `multiply` hace que la
        tinta siga las arrugas del papel en vez de flotar encima. */}
    <div
      style={{
        position: "absolute",
        left: NOTA.x,
        top: NOTA.y,
        width: NOTA.w,
        height: NOTA.h,
        transform: `rotate(${NOTA.giro}deg)`,
        // El texto tocaba el borde derecho del papel: más aire a los lados y un
        // punto menos de cuerpo. En una nota chica el respiro es lo que la hace
        // leerse como papel escrito y no como etiqueta.
        padding: "50px 28px 18px",
        mixBlendMode: "multiply",
        fontFamily: TC.fonts.mano,
        fontWeight: 600,
        fontSize: 31,
        lineHeight: 1.22,
        color: "#16314C",
        textAlign: "center",
      }}
    >
      {sinPartir("Aprox. 5.000 m²")}
      <br />
      {sinPartir("desde UF 2.500")}
      <div style={{marginTop: 12, fontWeight: 500, fontSize: 27, color: "#4A5C4E"}}>
        {sinPartir("Padre Hurtado")}
      </div>
    </div>

    {/* ⭐ EL POST-IT: la lista, escrita a mano sobre el papel */}
    <div
      style={{
        position: "absolute",
        left: POSTIT.x,
        top: POSTIT.y,
        width: POSTIT.w,
        height: POSTIT.h,
        transform: `rotate(${POSTIT.giro}deg)`,
        padding: "52px 44px 40px",
        mixBlendMode: "multiply",
        fontFamily: TC.fonts.mano,
        color: "#16314C",
      }}
    >
      <div style={{fontWeight: 600, fontSize: 46, lineHeight: 1.08, marginBottom: 20}}>
        Ese proyecto que
        <br />
        tienes en mente…
      </div>
      {["Conocer Tierra Calma", "Elegir mi parcela", "Empezar a proyectar mi casa"].map((l) => (
        <div key={l} style={{display: "flex", alignItems: "center", gap: 12, marginBottom: 8}}>
          <ICheck s={24} c="#16314C" />
          <span style={{fontWeight: 500, fontSize: 35, lineHeight: 1.1}}>{sinPartir(l)}</span>
        </div>
      ))}
      {/* Cortado en dos líneas cortas a propósito: la esquina del papel se
          enrolla desde x ≈ 558 bajo la fila 1046, y una línea larga se iría con
          el enrollado. */}
      <div style={{marginTop: 14, fontWeight: 600, fontSize: 37, lineHeight: 1.1, width: 300}}>
        Próximo paso:
        <br />
        hacerlo realidad.
      </div>
    </div>

    <Marco archivo="MARCO-POST" />
    <Pildora caja={POST.pill} icono={<IWsp s={23} />} size={26} gap={11}>
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
