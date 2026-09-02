/**
 * Sistema gráfico BETWEEN Coffee & Bar — feed, stories y paid.
 *
 * Cada regla de acá viene del feedback de Elisabet Soto (24-08-2026):
 *  - Raleway ExtraBold para titulares en mayúscula; Brushwell solo para títulos
 *    o una palabra clave; máximo 2 familias por pieza.
 *  - Texto beige #fff9eb sobre foto; café #675b49 cuando el fondo es muy claro.
 *  - La foto se oscurece con una capa MULTIPLY lo menos notoria posible.
 *  - Los títulos NUNCA llevan punto final. Bajadas de máximo 3 líneas.
 *  - Respiro y jerarquía: nunca saturar de texto. Marca juvenil con algo de estatus.
 *  - Márgenes: los iconos de Instagram no pueden tapar texto importante.
 */
import React from 'react';
import {
  AbsoluteFill,
  Img,
  continueRender,
  delayRender,
  interpolate,
  staticFile,
  useCurrentFrame,
} from 'remotion';
import {BETWEEN, cargarFuentesBetween, sinPuntoFinal} from '../../brand/hilton-between';

cargarFuentesBetween();

type Tono = 'beige' | 'cafe';
const tinta = (tono: Tono) => (tono === 'cafe' ? BETWEEN.colores.cafe : BETWEEN.colores.beige);

/** Sombra sutil solo cuando el texto va sobre foto (legibilidad en reels/stories). */
const sombraSobreFoto = '0 2px 14px rgba(36,26,18,0.45)';

/* ══════════════════ CIFRAS TABULARES ══════════════════
   ⭐ 01-09-2026, Eli: «los precios debes hacer que se vean opentype tabular,
   como en adobe illustrator, así los números no se ven desordenados».

   ⛔ El camino obvio NO funciona y estuvo puesto sin efecto varios días:
   `fontVariantNumeric: 'tabular-nums'` y `fontFeatureSettings: '"tnum" 1'`
   le piden la función a la FUENTE, y **ningún Raleway del repo trae `tnum`**.
   Verificado leyendo la tabla GSUB/GPOS de los cinco pesos instalados y de la
   variable: la única función numérica que traen es `lnum`. O sea que el CSS
   estaba ahí decorando, igual que el @font-face de Brushwell que fallaba en
   silencio. En Illustrator pasa lo mismo: el «Tabular Lining» del panel
   OpenType no tiene efecto con Raleway.

   Los dígitos de Raleway son PROPORCIONALES. Medido en ExtraBold sobre un em
   de 1000 unidades:
     0=614 · 1=518 · 2=580 · 3=569 · 4=578 · 5=558 · 6=608 · 7=576 · 8=607 · 9=589
   El «1» es 18,5 % más angosto que el «0»: por eso una columna de precios queda
   dispareja y las horas bailan.

   La solución es construir la cifra tabular a mano: cada dígito centrado en una
   caja del ancho del dígito MÁS ANCHO. Es exactamente lo que hace una fuente con
   cifras tabulares, y acá además es verificable midiendo el render. */

/** Ancho de la caja tabular, en em. Es el avance del «0», el dígito más ancho. */
export const ANCHO_CIFRA_EM = 0.614;

/**
 * Envuelve cada dígito de `texto` en una caja de ancho fijo para que todas las
 * cifras avancen igual. Los signos ($ . : , espacios) quedan intactos: en una
 * fuente tabular tampoco se ensanchan.
 *
 * ⚠️ Dentro de la caja el tracking se anula (`letterSpacing: 'normal'`), porque
 * si no el letter-spacing heredado se suma DENTRO del cuadro y descentra el
 * dígito. Úsalo en textos de dato y precio, que van sin tracking; no en el
 * titular, que compone con −0,024em.
 */
export const cifrasTabulares = (texto: string): React.ReactNode =>
  texto.split(/(\d)/).map((parte, i) =>
    /^\d$/.test(parte) ? (
      <span
        key={i}
        style={{
          display: 'inline-block',
          width: `${ANCHO_CIFRA_EM}em`,
          textAlign: 'center',
          letterSpacing: 'normal',
        }}
      >
        {parte}
      </span>
    ) : (
      parte
    ),
  );

/** ¿Vale la pena pasar por `cifrasTabulares`? Evita envolver texto sin dígitos. */
export const tieneCifras = (texto: string) => /\d/.test(texto);

/**
 * Versión tolerante para componentes que reciben `children: React.ReactNode`:
 * si lo que llega es texto plano con dígitos lo pasa por la caja tabular, y si
 * es cualquier otra cosa (un nodo ya armado) lo deja intacto.
 */
export const conCifras = (hijos: React.ReactNode): React.ReactNode =>
  typeof hijos === 'string' && tieneCifras(hijos) ? cifrasTabulares(hijos) : hijos;

/* ---------- foto de fondo + multiply ---------- */

export const FotoFondo: React.FC<{
  src: string;
  posicion?: string;
  /** Intensidad del multiply. Lo más bajo que permita leer el texto. */
  oscurecer?: number;
}> = ({src, posicion = 'center', oscurecer = 0.28}) => (
  <AbsoluteFill>
    <Img
      src={staticFile(src)}
      style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: posicion}}
    />
    <AbsoluteFill
      style={{
        backgroundColor: BETWEEN.colores.sombra,
        opacity: oscurecer,
        mixBlendMode: 'multiply',
      }}
    />
  </AbsoluteFill>
);

/* ---------- logo ---------- */

export const LogoBetween: React.FC<{
  formato?: 'feed' | 'story' | 'paid';
  /** Eli entrega dos plantillas por formato: logo arriba y logo abajo. */
  posicion?: 'arriba' | 'abajo';
  tono?: Tono;
  /** Ancho en px. Se escala por ancho y el alto sale del ratio — nunca achatado. */
  ancho?: number;
  y?: number;
}> = ({formato = 'feed', posicion = 'arriba', tono = 'beige', ancho, y}) => {
  const clave = (formato === 'story' ? 'story' : 'post') + (posicion === 'abajo' ? 'LogoAbajo' : 'LogoArriba');
  const g = BETWEEN.margenes[clave as keyof typeof BETWEEN.margenes] as {
    wordmarkY: number;
    ancho: number;
  };
  const anchoFinal = ancho ?? g.ancho;
  return (
    <Img
      src={staticFile(tono === 'cafe' ? BETWEEN.logo.cafe : BETWEEN.logo.beige)}
      style={{
        position: 'absolute',
        top: y ?? g.wordmarkY,
        left: '50%',
        transform: 'translateX(-50%)',
        width: anchoFinal,
        height: anchoFinal / BETWEEN.logo.ratio,
      }}
    />
  );
};

/* ---------- tipografía ---------- */

/**
 * Brushwell (como Kallimata) no trae «¡» ni «¿». Eli resuelve exactamente así:
 * usa el «!» y el «?» girados 180°, que están bien construidos y calzan.
 * Solo aplica a la script — Raleway sí trae los signos de apertura.
 */
const signosVolteados = (texto: string): React.ReactNode[] =>
  [...texto].map((ch, i) =>
    ch === '\u00a1' || ch === '\u00bf' ? (
      <span key={i} style={{display: 'inline-block', transform: 'rotate(180deg)'}}>
        {ch === '\u00a1' ? '!' : '?'}
      </span>
    ) : (
      ch
    ),
  );


/**
 * Titular. Regla de Eli:
 *  - Si debe DESTACAR: todo en MAYÚSCULA, ~100 (rango 40–122).
 *  - Si es sutil: 40–74 y **solo la primera letra en mayúscula** — más limpio.
 * El componente decide la caja según el tamaño para no volver a equivocarse.
 */
export const Titulo: React.FC<{
  children: string;
  size?: number;
  destacar?: boolean;
  peso?: number;
  tono?: Tono;
  sobreFoto?: boolean;
  style?: React.CSSProperties;
}> = ({
  children,
  size = BETWEEN.tipos.tituloCapsDestacado,
  destacar,
  peso,
  tono = 'beige',
  sobreFoto = true,
  style,
}) => {
  // Sobre 78 la pieza pide protagonismo → mayúsculas. Bajo eso, caja baja.
  const enMayuscula = destacar ?? size >= 78;
  return (
    <div
      style={{
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: peso ?? (enMayuscula ? BETWEEN.pesos.extrabold : BETWEEN.pesos.bold),
        fontSize: size,
        letterSpacing: enMayuscula ? 1 : 0,
        textTransform: enMayuscula ? 'uppercase' : 'none',
        color: tinta(tono),
        lineHeight: enMayuscula ? 1.05 : 1.15,
        textWrap: 'balance',
        textShadow: sobreFoto ? sombraSobreFoto : undefined,
        ...style,
      }}
    >
      {conCifras(sinPuntoFinal(children))}
    </div>
  );
};

/** Alias histórico; en piezas nuevas usar <Titulo>. */
export const Caps = Titulo;

/** Brushwell. Solo títulos o una palabra clave — jamás números ni párrafos. */
export const Script: React.FC<{
  children: string;
  size?: number;
  tono?: Tono;
  sobreFoto?: boolean;
  style?: React.CSSProperties;
}> = ({children, size = BETWEEN.tipos.scriptSolo, tono = 'beige', sobreFoto = true, style}) => (
  <div
    style={{
      fontFamily: BETWEEN.fuentes.script,
      fontSize: size,
      color: tinta(tono),
      lineHeight: 1.0,
      textShadow: sobreFoto ? sombraSobreFoto : undefined,
      ...style,
    }}
  >
    {signosVolteados(sinPuntoFinal(children))}
  </div>
);

/**
 * Título mixto: línea en Raleway caps + línea en Brushwell.
 * La script sale automáticamente ~20% más grande para equilibrar el peso visual.
 */
export const TituloMixto: React.FC<{
  caps: string;
  script: string;
  sizeCaps?: number;
  tono?: Tono;
  orden?: 'capsPrimero' | 'scriptPrimero';
  destacar?: boolean;
  style?: React.CSSProperties;
}> = ({caps, script, sizeCaps = 72, tono = 'beige', orden = 'capsPrimero', destacar, style}) => {
  const sizeScript = Math.round(sizeCaps * BETWEEN.proporcionScript);
  const lineaCaps = <Titulo size={sizeCaps} destacar={destacar} tono={tono}>{caps}</Titulo>;
  const lineaScript = <Script size={sizeScript} tono={tono} style={{marginTop: 2}}>{script}</Script>;
  return (
    <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', ...style}}>
      {orden === 'capsPrimero' ? lineaCaps : lineaScript}
      {orden === 'capsPrimero' ? lineaScript : lineaCaps}
    </div>
  );
};

/** Bajada o párrafo. Máximo 3 líneas — se recorta el exceso en tiempo de diseño. */
export const Bajada: React.FC<{
  children: React.ReactNode;
  size?: number;
  tono?: Tono;
  sobreFoto?: boolean;
  style?: React.CSSProperties;
}> = ({children, size = BETWEEN.tipos.bajada, tono = 'beige', sobreFoto = true, style}) => (
  <div
    style={{
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.regular,
      fontSize: size,
      color: tinta(tono),
      lineHeight: 1.4,
      maxWidth: 820,
      textWrap: 'balance',
      textShadow: sobreFoto ? sombraSobreFoto : undefined,
      ...style,
    }}
  >
    {children}
  </div>
);

/**
 * Dato de cierre: horario, precio o etiqueta de producto.
 * El tracking (5–10) va SOLO si hace falta compensar la jerarquía, así que
 * `espaciado` es opcional y NO viene puesto por defecto.
 */
export const Dato: React.FC<{
  children: React.ReactNode;
  size?: number;
  tono?: Tono;
  espaciado?: boolean;
  style?: React.CSSProperties;
}> = ({children, size = 30, tono = 'beige', espaciado = false, style}) => (
  <div
    style={{
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.semibold,
      fontSize: size,
      letterSpacing: espaciado ? BETWEEN.trackingHorario : 0,
      textTransform: espaciado ? 'uppercase' : 'none',
      color: tinta(tono),
      textShadow: sombraSobreFoto,
      ...style,
    }}
  >
    {conCifras(children)}
  </div>
);

/** Alias histórico. */
export const Horario = Dato;

/**
 * CTA en caja: café con letras beige por defecto; se invierte cuando el fondo
 * es oscuro y el beige necesita destacar más.
 */
export const CTA: React.FC<{
  children: React.ReactNode;
  size?: number;
  invertido?: boolean;
  style?: React.CSSProperties;
}> = ({children, size = BETWEEN.tipos.cta, invertido = false, style}) => (
  <div
    style={{
      display: 'inline-block',
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.semibold,
      fontSize: size,
      color: invertido ? BETWEEN.colores.cafe : BETWEEN.colores.beige,
      backgroundColor: invertido ? BETWEEN.colores.beige : BETWEEN.colores.cafe,
      padding: '20px 44px',
      borderRadius: 6,
      ...style,
    }}
  >
    {children}
  </div>
);

/** Legales: Raleway regular o italic, 20–26, centrados y con margen. */
export const Legal: React.FC<{
  children: React.ReactNode;
  size?: number;
  italic?: boolean;
  tono?: Tono;
  style?: React.CSSProperties;
}> = ({children, size = BETWEEN.tipos.legal, italic = true, tono = 'beige', style}) => (
  <div
    style={{
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.regular,
      fontStyle: italic ? 'italic' : 'normal',
      fontSize: size,
      color: tinta(tono),
      textAlign: 'center',
      lineHeight: 1.4,
      maxWidth: 840,
      margin: '0 auto',
      textShadow: sombraSobreFoto,
      ...style,
    }}
  >
    {children}
  </div>
);

/* ---------- plantillas ---------- */

export type PiezaProps = {
  foto: string;
  posicionFoto?: string;
  oscurecer?: number;
  caps?: string;
  script?: string;
  tituloSutil?: string;
  sizeCaps?: number;
  bajada?: React.ReactNode;
  horario?: string;
  /** Tracking en el dato de cierre: solo si hace falta jerarquía. */
  espaciarHorario?: boolean;
  /** Fuerza mayúsculas en el título aunque sea chico (o al revés). */
  destacar?: boolean;
  cta?: string;
  ctaInvertido?: boolean;
  legal?: React.ReactNode;
  tono?: Tono;
  /** Cuál de las dos líneas del título va arriba. */
  ordenTitulo?: 'capsPrimero' | 'scriptPrimero';
  conLogo?: boolean;
  logoTono?: Tono;
  /** Plantilla de logo: arriba (por defecto) o abajo. */
  logoPosicion?: 'arriba' | 'abajo';
  alineacion?: 'centro' | 'abajo';
};

const BloqueTexto: React.FC<PiezaProps & {escala?: number}> = ({
  caps,
  script,
  sizeCaps,
  destacar,
  bajada,
  horario,
  espaciarHorario,
  cta,
  ctaInvertido,
  legal,
  tono = 'beige',
  ordenTitulo = 'capsPrimero',
  escala = 1,
}) => (
  <div
    style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: 22 * escala,
      textAlign: 'center',
    }}
  >
    {caps && script ? (
      <TituloMixto
        caps={caps}
        script={script}
        sizeCaps={(sizeCaps ?? 72) * escala}
        tono={tono}
        orden={ordenTitulo}
        destacar={destacar}
      />
    ) : caps ? (
      <Titulo size={(sizeCaps ?? BETWEEN.tipos.tituloCapsDestacado) * escala} destacar={destacar} tono={tono}>
        {caps}
      </Titulo>
    ) : script ? (
      <Script size={(sizeCaps ?? BETWEEN.tipos.scriptSolo) * escala} tono={tono}>
        {script}
      </Script>
    ) : null}
    {bajada ? (
      <Bajada tono={tono} size={BETWEEN.tipos.bajada * escala}>
        {bajada}
      </Bajada>
    ) : null}
    {horario ? (
      <Dato tono={tono} size={(espaciarHorario ? 29 : 36) * escala} espaciado={espaciarHorario}>
        {horario}
      </Dato>
    ) : null}
    {cta ? (
      <CTA invertido={ctaInvertido} size={BETWEEN.tipos.cta * escala} style={{marginTop: 6 * escala}}>
        {cta}
      </CTA>
    ) : null}
    {legal ? (
      <Legal tono={tono} size={BETWEEN.tipos.legal * escala}>
        {legal}
      </Legal>
    ) : null}
  </div>
);

/** Feed / slide de carrusel — 1080×1350. */
export const PiezaFeed: React.FC<PiezaProps> = (props) => {
  const {foto, posicionFoto, oscurecer, conLogo = true, logoTono = 'beige', logoPosicion = 'arriba', alineacion = 'abajo'} = props;
  return (
    <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
      <FotoFondo src={foto} posicion={posicionFoto} oscurecer={oscurecer} />
      {conLogo ? <LogoBetween formato="feed" posicion={logoPosicion} tono={logoTono} /> : null}
      <AbsoluteFill
        style={{
          justifyContent: alineacion === 'centro' ? 'center' : 'flex-end',
          alignItems: 'center',
          padding: '0 90px 96px 90px',
        }}
      >
        <BloqueTexto {...props} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/** Story — 1080×1920, respetando 250px arriba y 340px abajo de zona segura. */
export const PiezaStory: React.FC<PiezaProps> = (props) => {
  const {foto, posicionFoto, oscurecer, conLogo = true, logoTono = 'beige', logoPosicion = 'arriba'} = props;
  return (
    <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
      <FotoFondo src={foto} posicion={posicionFoto} oscurecer={oscurecer} />
      {conLogo ? <LogoBetween formato="story" posicion={logoPosicion} tono={logoTono} /> : null}
      <AbsoluteFill
        style={{
          justifyContent: 'center',
          alignItems: 'center',
          padding: '420px 90px 340px 90px',
        }}
      >
        <BloqueTexto {...props} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/** Paid media en post — 1080×1080. El logo va arriba pero más compacto. */
export const PiezaPaid: React.FC<PiezaProps> = (props) => {
  const {foto, posicionFoto, oscurecer, conLogo = true, logoTono = 'beige', logoPosicion = 'arriba'} = props;
  return (
    <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
      <FotoFondo src={foto} posicion={posicionFoto} oscurecer={oscurecer} />
      {conLogo ? <LogoBetween formato="paid" posicion={logoPosicion} tono={logoTono} /> : null}
      <AbsoluteFill
        style={{
          justifyContent: 'flex-end',
          alignItems: 'center',
          // Meta deja el 10-15% inferior para su UI
          padding: '0 80px 130px 80px',
        }}
      >
        <BloqueTexto {...props} escala={0.9} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* ---------- story animada ---------- */

type Pantalla = Pick<PiezaProps, 'foto' | 'posicionFoto' | 'caps' | 'script' | 'bajada' | 'sizeCaps'>;

export const StoryAnimada: React.FC<{
  pantallas: Pantalla[];
  horario?: string;
  cta?: string;
  legal?: React.ReactNode;
  framesPorPantalla?: number;
}> = ({pantallas, horario, cta, legal, framesPorPantalla = 90}) => {
  const frame = useCurrentFrame();
  const idx = Math.min(Math.floor(frame / framesPorPantalla), pantallas.length - 1);
  const local = frame - idx * framesPorPantalla;
  const p = pantallas[idx];
  const esUltima = idx === pantallas.length - 1;

  const entrada = interpolate(local, [0, 18], [0, 1], {extrapolateRight: 'clamp'});
  const subida = interpolate(local, [0, 18], [36, 0], {extrapolateRight: 'clamp'});

  return (
    <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
      <AbsoluteFill style={{opacity: interpolate(local, [0, 10], [0.4, 1], {extrapolateRight: 'clamp'})}}>
        <FotoFondo src={p.foto} posicion={p.posicionFoto} />
      </AbsoluteFill>
      <LogoBetween formato="story" />
      <AbsoluteFill
        style={{
          justifyContent: 'center',
          alignItems: 'center',
          padding: '420px 90px 340px 90px',
          opacity: entrada,
          transform: `translateY(${subida}px)`,
        }}
      >
        <BloqueTexto
          foto={p.foto}
          caps={p.caps}
          script={p.script}
          sizeCaps={p.sizeCaps}
          bajada={p.bajada}
          horario={esUltima ? horario : undefined}
          cta={esUltima ? cta : undefined}
          legal={esUltima ? legal : undefined}
        />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* ==========================================================================
 * ⭐ GRAMÁTICA MEDIDA — 26-08-2026
 *
 * Todo lo de acá abajo sale de MEDIR las 19 piezas reales que entregó Eli
 * (raw/hilton/between-adn/ref-piezas/), no de interpretar una descripción.
 * Los componentes de más arriba quedaron cortos: titulares a la mitad del
 * tamaño real, script tratada como segunda línea decorativa, bloque centrado
 * y flotando, y sin la caja taupe ni el texto en arco. Eso produjo la grilla
 * de septiembre 2026 que el cliente rechazó.
 *
 * En piezas nuevas: usar ESTOS componentes.
 * ========================================================================== */

/**
 * Caja taupe: fondo #675b49 OPACO, 74 px de alto, texto Raleway **LIGHT** 45.
 * El contraste titular pesadísimo / dato liviano es firma de la marca —
 * no poner el texto de la caja en bold.
 */
export const CajaDato: React.FC<{
  children: React.ReactNode;
  size?: number;
  /** Ancho útil del bloque; la caja nunca lo pasa. */
  anchoDisponible?: number;
  style?: React.CSSProperties;
}> = ({children, size = BETWEEN.tipos.cajaDato, anchoDisponible = 1080 - 2 * BETWEEN.bloque.margenX, style}) => {
  useFuentesListas();
  // la caja va en nowrap, así que si el dato es largo hay que bajar el cuerpo:
  // «SEGUNDO NIVEL · TRABAJAR O REUNIRTE» se salía 46 px por la derecha
  const texto = typeof children === 'string' ? children.toUpperCase() : '';
  const cuerpo = texto
    ? ajustarACaber(texto, size, (v) => `${BETWEEN.pesos.extrabold} ${v}px ${BETWEEN.fuentes.sans}`,
                    anchoDisponible - 2 * BETWEEN.cajas.padX, 0, 0.6)
    : size;
  return (
  <div
    style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      height: BETWEEN.cajas.alto,
      padding: `0 ${BETWEEN.cajas.padX}px`,
      backgroundColor: BETWEEN.cajas.fondo,
      borderRadius: BETWEEN.cajas.radio,
      fontFamily: BETWEEN.fuentes.sans,
      // MEDIDO en la pieza aprobada: «PARA EMPEZAR EL DÍA» da 488×33 px, que solo
      // calza con ExtraBold. Antes estaba en Light (300) y la caja se veía floja.
      fontWeight: BETWEEN.pesos.extrabold,
      fontSize: cuerpo,
      lineHeight: 1,
      color: BETWEEN.colores.beige,
      textTransform: 'uppercase',
      whiteSpace: 'nowrap',
      ...style,
    }}
  >
    {conCifras(children)}
  </div>
  );
};

/**
 * Pila de cajas taupe. Ojo: las cajas de una pila se **centran entre sí**
 * (medido: caja 1 en x 116–633 y caja 2 en x 189–561, mismo centro 375),
 * no se alinean a la izquierda del bloque.
 */
export const PilaDatos: React.FC<{
  datos: React.ReactNode[];
  style?: React.CSSProperties;
}> = ({datos, style}) => (
  <div
    style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: BETWEEN.cajas.gap,
      ...style,
    }}
  >
    {datos.map((d, i) => (
      <CajaDato key={i}>{d}</CajaDato>
    ))}
  </div>
);


/* ---------- ajuste de ancho (la script NUNCA se corta ni se parte) ---------- */

let _ctx: CanvasRenderingContext2D | null = null;
/** Ancho de tinta de un texto, midiendo con canvas (misma fuente que el DOM). */
const medirTexto = (texto: string, css: string): number => {
  if (typeof document === 'undefined') return 0;
  if (!_ctx) _ctx = document.createElement('canvas').getContext('2d');
  if (!_ctx) return 0;
  _ctx.font = css;
  return _ctx.measureText(texto).width;
};

/**
 * Baja el cuerpo hasta que el texto quepa en `maxAncho`.
 *
 * Existe porque en la ronda 4 la script se salía del cuadro en 6 piezas
 * («va contigo», «contundente», «una foto») y en Cowork-1 se partió en dos
 * líneas. En las piezas de Eli la script **jamás** se parte ni toca el borde:
 * cuando la palabra es larga, ella baja el cuerpo.
 */

/**
 * ⛔⛔ EL BUG QUE PARTIÓ LOS TITULARES — no quitar este hook.
 *
 * Todo el ajuste de cuerpo («que el titular quepa en el ancho útil») se calcula
 * midiendo el texto con canvas DURANTE el render. Si en ese momento Raleway o
 * Brushwell todavía no cargaron, `measureText` mide con la fuente de REEMPLAZO,
 * que es más angosta: el cálculo dice «cabe» y no achica nada. Después el
 * navegador pinta con la fuente real, mucho más ancha, y el titular se sale del
 * cuadro por los dos lados. Pasó en 8 de las 27 piezas.
 *
 * Este hook fuerza UN re-render cuando `document.fonts.ready` resuelve, y ahí la
 * medición ya es la buena. El `delayRender` mantiene el frame abierto para que
 * Remotion no fotografíe antes; el tope de 8 s evita que un problema de fuentes
 * cuelgue el render para siempre (ver memoria reel-video-gotchas).
 */
let _fuentesListas = false;

export const useFuentesListas = (): boolean => {
  const [listas, setListas] = React.useState(_fuentesListas);
  React.useEffect(() => {
    if (_fuentesListas || typeof document === 'undefined') return;
    const espera = delayRender('BETWEEN · esperando Brushwell y Raleway');
    let cerrado = false;
    const terminar = () => {
      if (cerrado) return;
      cerrado = true;
      _fuentesListas = true;
      setListas(true);
      continueRender(espera);
    };
    const tope = setTimeout(terminar, 8000);
    void document.fonts.ready.then(() => {
      clearTimeout(tope);
      terminar();
    }).catch(() => {
      clearTimeout(tope);
      terminar();
    });
    return () => clearTimeout(tope);
  }, []);
  return listas;
};

/**
 * ⭐ Métricas de TINTA de una línea, en px, respecto de la línea base.
 *
 * Hace falta porque Between se compone por la tinta, no por la caja de texto:
 * el aire entre la script y la caja alta que midió la pieza aprobada (9 px) es
 * de tinta a tinta. Con `lineHeight` uno nunca llega a ese número — cada familia
 * mete un espacio distinto sobre y bajo la línea base, y Brushwell además
 * tiene remates que se salen del avance.
 */
type Tinta = {
  /** Tinta por sobre la línea base. */
  alto: number;
  /** Tinta por debajo de la línea base. */
  bajo: number;
  /** Lo que el trazo se sale por la izquierda del punto de anclaje. */
  izq: number;
  /** Hasta dónde llega el trazo por la derecha del punto de anclaje. */
  der: number;
  /** Ancho de avance (lo que ocupa la caja de texto). */
  avance: number;
  /** Distancia de la línea base al borde superior de una caja con lineHeight 1. */
  baseEnCaja: number;
};

const medirTinta = (texto: string, css: string, trackingEm = 0, cuerpo?: number): Tinta => {
  const vacio: Tinta = {alto: 0, bajo: 0, izq: 0, der: 0, avance: 0, baseEnCaja: 0};
  if (typeof document === 'undefined') return vacio;
  if (!_ctx) _ctx = document.createElement('canvas').getContext('2d');
  if (!_ctx) return vacio;
  _ctx.font = css;
  // Chrome ≥ 99 aplica letterSpacing en canvas; si no existe, se compensa a mano.
  const soportaTracking = 'letterSpacing' in _ctx;
  if (soportaTracking) (_ctx as CanvasRenderingContext2D & {letterSpacing: string}).letterSpacing = `${trackingEm}em`;
  const m = _ctx.measureText(texto);
  /**
   * ⚠️ El cuerpo va explícito. `parseFloat(css)` NO sirve: cuando el css trae el
   * peso delante («800 117px Raleway») devuelve 800, y el titular se va 200 px
   * fuera del cuadro. Pasó exactamente eso en la primera calibración.
   */
  const size = cuerpo ?? parseFloat(css) ?? 0;
  const extra = soportaTracking ? 0 : trackingEm * size * Math.max(texto.length - 1, 0);
  const fbA = m.fontBoundingBoxAscent ?? m.actualBoundingBoxAscent ?? 0;
  const fbD = m.fontBoundingBoxDescent ?? m.actualBoundingBoxDescent ?? 0;
  if (soportaTracking) (_ctx as CanvasRenderingContext2D & {letterSpacing: string}).letterSpacing = '0px';
  return {
    alto: m.actualBoundingBoxAscent ?? 0,
    bajo: m.actualBoundingBoxDescent ?? 0,
    izq: Math.max(m.actualBoundingBoxLeft ?? 0, 0),
    der: m.actualBoundingBoxRight ?? 0,
    avance: (m.width ?? 0) + extra,
    // en una caja con lineHeight 1 el sobrante se reparte arriba y abajo
    baseEnCaja: (size - (fbA + fbD)) / 2 + fbA,
  };
};

const ajustarACaber = (
  texto: string,
  size: number,
  css: (s: number) => string,
  maxAncho: number,
  tracking = 0,
  minimo = 0.55,
): number => {
  const ancho = medirTexto(texto, css(size)) + tracking * Math.max(texto.length - 1, 0);
  if (!ancho || ancho <= maxAncho) return size;
  return Math.max(Math.floor((size * maxAncho) / ancho), Math.floor(size * minimo));
};

/**
 * ⭐ Titular de Between: caja alta Raleway BLACK + script Brushwell **encima**.
 *
 * Lo que hace distinto a este componente del viejo <TituloMixto>:
 *  - la script va a `proporcionScript` ≈ 1,0 × la caja alta y VA ARRIBA
 *  - las dos líneas se **solapan**: la tinta queda a 2 px (antes: gap de 22)
 *  - el bloque se alinea a la izquierda por defecto (antes: siempre centrado)
 *  - trackings medidos: −1 en la caja alta, +18 en la script
 */
/**
 * ⭐ TITULAR BETWEEN — la unidad tipográfica de la marca.
 *
 * Disposición de la pieza que la diseñadora aprobó como «uso correcto de la
 * tipografía» (C1 S3 N°1): la SCRIPT va ARRIBA, corta y en menor escala; la
 * CAJA ALTA va ABAJO y es la protagonista. Todo centrado sobre el eje.
 *
 * ⛔ Antes esto estaba al revés (caja alta arriba, script gigante abajo, las dos
 * solapadas). Eso produjo la grilla que el cliente rechazó dos veces.
 *
 * Reglas que aplica solo:
 *  · la script se limita a una frase corta — si llega larga, avisa por consola;
 *  · las dos líneas se posicionan por su TINTA, con el aire medido (9 px);
 *  · se centra por la TINTA, no por la caja, para que el remate del pincel de
 *    Brushwell no descuadre el bloque;
 *  · si no cabe en el ancho útil, baja el cuerpo en vez de partir la línea.
 */
export const TitularBetween: React.FC<{
  /** Frase corta o palabra clave. Va ARRIBA y en menor escala que el titular. */
  script?: string;
  /**
   * ⭐ La línea de acompañamiento en RALEWAY en vez de Brushwell.
   *
   * Pedido de Eli el 01-09-2026 para el carrusel Cowork: «desde el slide 2 no
   * agregues la tipografía brushwell, que sea de la familia de raleway, así se
   * diferencia de la portada». La script queda como marca de la PORTADA y las
   * slides interiores bajan a un solo alfabeto.
   *
   * No es una proporción inventada: usa la misma relación que ya tiene la línea
   * `arriba` de `TituloTresPesos` —Raleway 500 a 0,72 × la caja alta, tracking
   * +0,02em y caja alta—, que es el recurso de dos pesos de la marca.
   */
  scriptSans?: boolean;
  /** Titular protagonista, en caja alta. Va ABAJO. */
  caps?: string;
  sizeCaps?: number;
  sizeScript?: number;
  tono?: Tono;
  alinear?: 'centro' | 'izquierda';
  /**
   * Ancho de composición.
   *
   * ⚠️ Por defecto sigue siendo el MARGEN (1080 − 2×84 = 912). Lo correcto es
   * componer en `BETWEEN.bloque.columna` (810) —achicar sólo hasta caber en el
   * margen deja toda línea larga clavada en el 84 % del lienzo— pero cambiar el
   * defecto re-flujaba piezas YA APROBADAS: comprobado el 01-09-2026, tres de
   * las cuatro piezas entregadas de la S1 cambiaban entre un 4,5 % y un 5,3 %
   * de sus píxeles. Así que la columna es OPT-IN: se pasa a mano en la pieza
   * que se está cortando. Ver `clients/hilton/CLAUDE.md § LA COLUMNA`.
   */
  anchoDisponible?: number;
  /**
   * Conserva la puntuación final del texto tal como la escribe el brief.
   *
   * Por defecto la pieza pasa por `sinPuntoFinal`, porque la regla de Eli es que
   * «los títulos NUNCA llevan punto final». Pero cuando el texto es una CITA
   * —el carrusel «Primero la foto… ¿o no?» o el chiste del cafecito— el punto
   * va DENTRO de las comillas y es parte de lo que se dice, no un punto de
   * titular. Scarlette pidió expresamente las comillas el 31-08-2026, y el
   * brief trae la puntuación completa, así que ahí se respeta literal.
   */
  mantenerPunto?: boolean;
  style?: React.CSSProperties;
}> = ({
  script,
  scriptSans = false,
  caps,
  sizeCaps = BETWEEN.tipos.tituloCaps,
  sizeScript,
  tono = 'beige',
  alinear = 'centro',
  anchoDisponible = 1080 - 2 * BETWEEN.bloque.margenX,
  mantenerPunto = false,
  style,
}) => {
  // sin esto se mide con la fuente de reemplazo y el titular no se achica
  useFuentesListas();
  const podar = (t: string) => (mantenerPunto ? t : sinPuntoFinal(t));
  const textoCaps = caps ? podar(caps) : '';
  /**
   * ⚠️ En modo Raleway la línea se pinta en CAJA ALTA, así que se pasa a
   * mayúscula ACÁ y no con `textTransform`. El cuerpo se calcula midiendo con
   * canvas, y canvas mide el string tal cual: medir «muchos pendientes» y
   * pintar «MUCHOS PENDIENTES» da ~20 % de diferencia y el titular se sale del
   * cuadro. Es el bug que partió 8 piezas de la ronda 4.
   */
  const textoScript = script
    ? (scriptSans ? podar(script).toUpperCase() : podar(script))
    : '';

  if (!scriptSans && textoScript && textoScript.split(/\s+/).length > 4) {
    // eslint-disable-next-line no-console
    console.warn(`[BETWEEN] «${textoScript}» es muy largo para la script. ` +
      `Brushwell es para una frase corta o una palabra clave, no para una bajada.`);
  }

  const trScript = scriptSans ? 0.02 : BETWEEN.trackingScript;
  const cssCaps = (n: number) => `${BETWEEN.pesos.extrabold} ${n}px ${BETWEEN.fuentes.sans}`;
  const cssScript = (n: number) => scriptSans
    ? `500 ${n}px ${BETWEEN.fuentes.sans}`
    : `${n}px ${BETWEEN.fuentes.script}`;

  const encoger = (texto: string, base: number, css: (n: number) => string, tr: number) => {
    if (!texto) return base;
    let n = base;
    for (let i = 0; i < 40; i++) {
      const t = medirTinta(texto, css(n), tr, n);
      const ancho = Math.max(t.avance, t.izq + t.der);
      if (!ancho || ancho <= anchoDisponible) break;
      n -= 2;
    }
    return n;
  };

  /**
   * La caja alta puede ir en dos líneas: se separan con «\n».
   * ⚠️ Se pasan YA EN MAYÚSCULA. El CSS las sube con `textTransform`, pero el
   * cálculo del cuerpo se hace con canvas, y canvas mide el string tal cual: si
   * se mide «rico y contundente» y se pinta «RICO Y CONTUNDENTE», la medición
   * sale ~20 % corta, el ajuste cree que cabe y el titular se sale del cuadro.
   * Ese fue el defecto de 8 piezas de la ronda anterior.
   */
  const lineasCaps = textoCaps
    ? textoCaps.split('\n').map((l) => l.trim().toUpperCase()).filter(Boolean)
    : [];
  const nCaps = lineasCaps.reduce(
    (menor, l) => Math.min(menor, encoger(l, sizeCaps, cssCaps, BETWEEN.trackingCaps)),
    sizeCaps,
  );
  const nScript = encoger(
    textoScript,
    sizeScript ?? Math.round(sizeCaps * (scriptSans ? 0.72 : BETWEEN.proporcionScript)),
    cssScript,
    trScript,
  );

  const tCapsPorLinea = lineasCaps.map((l) => medirTinta(l, cssCaps(nCaps), BETWEEN.trackingCaps, nCaps));
  const tCaps = tCapsPorLinea[0] ?? medirTinta('', cssCaps(nCaps), BETWEEN.trackingCaps, nCaps);
  /**
   * Aire entre dos líneas de caja alta. MEDIDO en «¿YA TOMASTE TU / CAFECITO DEL
   * DÍA?» (post n°2 s4): 21 px de tinta a tinta sobre una altura de caja de 59,
   * o sea 0,35 de la altura. Se guarda como proporción para que aguante
   * cualquier cuerpo.
   */
  const aireEntreCaps = Math.round((tCaps.alto || nCaps * 0.73) * 0.35);
  const tScript = medirTinta(textoScript, cssScript(nScript), trScript, nScript);

  /** Cuánto mover la caja para que quede centrada la TINTA y no el avance. */
  const centrarTinta = (t: Tinta) =>
    alinear === 'centro' ? t.avance / 2 - (t.der - t.izq) / 2 : t.izq;

  const aire = BETWEEN.aire.scriptATitulo;
  const altoScript = textoScript ? tScript.alto + tScript.bajo : 0;
  const altoCaps = tCapsPorLinea.reduce(
    (acc, t, i) => acc + t.alto + t.bajo + (i ? aireEntreCaps : 0), 0,
  );
  const alto = altoScript + (textoScript && lineasCaps.length ? aire : 0) + altoCaps;

  const linea = (
    texto: React.ReactNode,
    t: Tinta,
    n: number,
    topTinta: number,
    extra: React.CSSProperties,
  ) => (
    <div
      style={{
        position: 'absolute',
        top: topTinta - (t.baseEnCaja - t.alto),
        left: alinear === 'centro' ? '50%' : 0,
        transform: alinear === 'centro'
          ? `translateX(calc(-50% + ${centrarTinta(t)}px))`
          : `translateX(${centrarTinta(t)}px)`,
        fontSize: n,
        lineHeight: 1,
        whiteSpace: 'nowrap',
        color: tinta(tono),
        textShadow: sombraSobreFoto,
        ...extra,
      }}
    >
      {texto}
    </div>
  );

  return (
    <div style={{position: 'relative', width: '100%', height: alto, ...style}}>
      {textoScript
        ? linea(
            /* el volteo del signo de apertura es un truco para Brushwell, que no
               trae «¿». Raleway sí lo trae, así que en Raleway no se toca. */
            scriptSans ? textoScript : signosVolteados(textoScript),
            tScript, nScript, 0,
            scriptSans
              ? {fontFamily: BETWEEN.fuentes.sans, fontWeight: 500, letterSpacing: '0.02em'}
              : {fontFamily: BETWEEN.fuentes.script, letterSpacing: `${BETWEEN.trackingScript}em`},
          )
        : null}
      {lineasCaps.map((l, i) => {
        const arriba = altoScript
          + (textoScript ? aire : 0)
          + tCapsPorLinea.slice(0, i).reduce((a, t) => a + t.alto + t.bajo + aireEntreCaps, 0);
        return (
          <React.Fragment key={i}>
            {linea(l, tCapsPorLinea[i], nCaps, arriba, {
              fontFamily: BETWEEN.fuentes.sans,
              fontWeight: BETWEEN.pesos.extrabold,
              letterSpacing: `${BETWEEN.trackingCaps}em`,
              textTransform: 'uppercase',
            })}
          </React.Fragment>
        );
      })}
    </div>
  );
};

export const TextoArco: React.FC<{
  children: string;
  size?: number;
  tono?: Tono;
  /** Desplazamiento vertical respecto a la curva medida. */
  offsetY?: number;
  ancho?: number;
  alto?: number;
}> = ({children, size = BETWEEN.tipos.arco, tono = 'beige', offsetY = 0, ancho = 1080, alto = 1350}) => {
  const texto = children.toUpperCase();
  // largo aproximado de la bézier M 108 1097 Q 540 1367 972 1097
  const largoTrazado = 940;
  const cuerpo = ajustarACaber(
    texto,
    size,
    (s) => `${BETWEEN.pesos.regular} ${s}px ${BETWEEN.fuentes.sans}`,
    largoTrazado,
  );
  return (
  <svg
    width={ancho}
    height={alto}
    viewBox={`0 0 ${ancho} ${alto}`}
    style={{position: 'absolute', left: 0, top: offsetY}}
  >
    <path id="arco-between" d="M 108 1097 Q 540 1367 972 1097" fill="none" />
    <text
      fill={tinta(tono)}
      style={{
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: BETWEEN.pesos.regular,
        fontSize: cuerpo,
        letterSpacing: 0,
      }}
    >
      <textPath href="#arco-between" startOffset="50%" textAnchor="middle">
        {texto}
      </textPath>
    </text>
  </svg>
  );
};

/**
 * ⭐ Plantilla de feed real de Between: bodegón + titular anclado ARRIBA a la
 * izquierda + pila de cajas taupe + texto en arco al pie.
 * Geometría medida en «EL MATCH perfecto» (C1 S2 N°1).
 */
/**
 * ⭐ PIE DE PIEZA — el bloque de cierre de la pieza aprobada.
 *
 * Medido en C1 S3 N°1 (feed, sobre lienzo de 1080×1350):
 *   «PROMOS TO GO»          y 1150–1185 · tinta 413 × 35 · centrado
 *   «De 8:00 a 10:00 hrs»   y 1211–1237 · tinta 317 × 25 · centrado
 * Es lo que da el cierre comercial sin ensuciar el titular: la promo y el
 * horario NO van arriba peleando con la caja alta.
 */
/**
 * ⭐ PANEL TAUPE — la bajada cuando la foto no deja leerla.
 *
 * Instrucción textual del cliente (27-08-2026):
 *   «Cuando no se logra visualizar los textos, puedes dejarlo en una caja del
 *    color café de la marca #675B49.»
 *
 * Es la misma caja de `CajaDato` pero para una frase de varias líneas. Se usa
 * SOLO cuando hace falta: sobre foto oscura y pareja, la bajada va suelta. La
 * alternativa —subir el multiply hasta que el texto se lea— es justamente lo
 * que dejaba las piezas apagadas.
 */
export const PanelTaupe: React.FC<{
  children: React.ReactNode;
  size?: number;
  /**
   * Ancho máximo del panel. Por defecto el MARGEN, por la misma razón que
   * `TitularBetween.anchoDisponible`: cambiar el defecto movía piezas ya
   * aprobadas. Con el margen, la caja de la slide 3 del Cowork salía de 912 px
   * —tocando los dos bordes del bloque— y su texto se partía en TRES líneas,
   * con «segundo nivel,» como renglón corto entre dos largos; por eso las
   * piezas que se cortan hoy pasan `ancho` a mano.
   */
  ancho?: number;
  /** Interlínea. Por defecto 1,3; se aprieta cuando el texto va en dos líneas. */
  interlinea?: number;
  style?: React.CSSProperties;
}> = ({children, size = BETWEEN.tipos.bajada, ancho, interlinea, style}) => (
  <div
    style={{
      maxWidth: ancho ?? 1080 - 2 * BETWEEN.bloque.margenX,
      padding: `${Math.round(BETWEEN.cajas.alto * 0.28)}px ${BETWEEN.cajas.padX}px`,
      backgroundColor: BETWEEN.cajas.fondo,
      borderRadius: BETWEEN.cajas.radio,
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.semibold,
      fontSize: size,
      lineHeight: interlinea ?? 1.3,
      color: BETWEEN.colores.beige,
      textAlign: 'center',
      ...style,
    }}
  >
    {conCifras(children)}
  </div>
);

export const PieDePieza: React.FC<{
  formato: 'feed' | 'story';
  titulo?: string;
  detalle?: string;
}> = ({formato, titulo, detalle}) => {
  // MEDIDO: en feed la tinta del pie arranca en y = 1150; en la story el cierre
  // de Eli arranca en y = 1678, bien por sobre la zona segura de Meta (340 px).
  const arriba = formato === 'feed' ? 1150 : 1678;
  return (
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        right: BETWEEN.bloque.margenX,
        top: arriba,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: 26,
      }}
    >
      {titulo ? (
        <div
          style={{
            fontFamily: BETWEEN.fuentes.sans,
            fontWeight: BETWEEN.pesos.extrabold,
            fontSize: 48,
            letterSpacing: `${BETWEEN.trackingCaps}em`,
            lineHeight: 1,
            textTransform: 'uppercase',
            color: BETWEEN.colores.beige,
            textShadow: sombraSobreFoto,
            textAlign: 'center',
          }}
        >
          {titulo}
        </div>
      ) : null}
      {detalle ? (
        <div
          style={{
            fontFamily: BETWEEN.fuentes.sans,
            fontWeight: BETWEEN.pesos.semibold,
            fontSize: 35,
            lineHeight: 1.2,
            color: BETWEEN.colores.beige,
            textShadow: sombraSobreFoto,
            textAlign: 'center',
          }}
        >
          {/* acá cae el horario de la portada To Go («Lunes a viernes · 08:00 a
              10:00 hrs.»): dos «1» y cuatro «0» que sin caja tabular bailan */}
          {tieneCifras(detalle) ? cifrasTabulares(detalle) : detalle}
        </div>
      ) : null}
    </div>
  );
};

/**
 * Legal al pie, en cursiva. Medido: feed 224 × 11 px a 32 px del borde;
 * story 248 × 27 px, por sobre la zona segura de Meta.
 */
export const LegalAlPie: React.FC<{
  formato: 'feed' | 'story';
  children: React.ReactNode;
}> = ({formato, children}) => (
  <div
    style={{
      position: 'absolute',
      left: 0,
      right: 0,
      bottom: formato === 'feed' ? 22 : 360,
      textAlign: 'center',
      fontFamily: BETWEEN.fuentes.sans,
      fontStyle: 'italic',
      fontWeight: BETWEEN.pesos.regular,
      fontSize: formato === 'feed' ? 20 : 28,
      lineHeight: 1,
      color: BETWEEN.colores.beige,
      opacity: 0.9,
      textShadow: sombraSobreFoto,
    }}
  >
    {children}
  </div>
);

export const PiezaFeedBodegon: React.FC<{
  foto: string;
  posicionFoto?: string;
  oscurecer?: number;
  caps?: string;
  script?: string;
  /** La línea de acompañamiento en Raleway en vez de Brushwell. */
  scriptSans?: boolean;
  /** Conserva la puntuación del brief; para textos que son una CITA. */
  mantenerPunto?: boolean;
  sizeCaps?: number;
  /** Bajada bajo el titular. Va antes de las cajas taupe. */
  bajada?: React.ReactNode;
  /** Interlínea de la caja de bajada, para apretar un texto de dos líneas. */
  interlineaBajada?: number;
  /**
   * Ancho de la columna del TITULAR. Por defecto el margen (912), para no
   * mover lo ya aprobado; las piezas que se cortan hoy pasan
   * `columna={BETWEEN.bloque.columna}` (810) a mano.
   */
  columna?: number;
  /**
   * Ancho de la caja taupe. Por defecto el mismo que el titular; se aprieta
   * para que el bloque ESCALONE (titular ancho → caja angosta) en vez de
   * apilar dos bandas del mismo ancho, que es lo que se leía como un muro.
   */
  columnaCaja?: number;
  /** Aire entre el titular y la caja taupe. Por defecto el medido (18). */
  aireTituloACaja?: number;
  /**
   * ⭐ EL VELO — pedido de Eli el 01-09-2026: «una transparencia con opacidad
   * como en Adobe Illustrator, que sea multiplicada muy sutil, para que se vea
   * el logo y los textos de arriba. Muy sutil».
   *
   * Es exactamente eso: un rectángulo del color sombra de la marca a pantalla
   * completa, en modo `multiply`, con opacidad baja. Va SOBRE la foto y su
   * multiply propio, y DEBAJO del logo y del texto — como una capa de
   * Illustrator puesta encima de la imagen y debajo de la tipografía.
   *
   * ⚠️ No es lo mismo que subir `oscurecer`. Ese apaga la foto entera para
   * ganar contraste, y el manual lo prohíbe («cuando un texto no se lee, la
   * solución es la caja taupe, no oscurecer la foto»). El velo es una capa
   * aparte, deliberada y muy baja, que asienta el conjunto sin matar la foto.
   * Si hace falta subirlo por encima de ~0,18 el problema es el encuadre.
   */
  velo?: number;
  /** La bajada va DENTRO de una caja taupe, para cuando la foto no la deja leer. */
  bajadaEnCaja?: boolean;
  datos?: React.ReactNode[];
  arco?: string;
  /** Bloque al pie: nombre de la promo + horario, como en la pieza aprobada. */
  pie?: {titulo?: string; detalle?: string};
  /** Legal en cursiva, al ras del borde inferior. */
  legal?: string;
  conLogo?: boolean;
  logoTono?: Tono;
  logoPosicion?: 'arriba' | 'abajo';
  alinear?: 'izquierda' | 'centro';
  /**
   * Dónde va el bloque. Por defecto ARRIBA (es lo que hace Eli en los bodegones),
   * pero en las fotos con personas se baja para no pasar texto sobre caras ni
   * ojos — regla dura de ella.
   */
  anclaje?: 'arriba' | 'abajo';
  /**
   * Y exacta del bloque, cuando ni arriba ni abajo sirven. Se usa sobre todo en
   * fotos con personas: bajar el bloque «casi al centro» deja el texto sobre una
   * superficie limpia en vez de sobre la cara. Lo pidió la diseñadora el 28-08.
   */
  topBloque?: number;
  /** Capas encima de la foto: etiquetas con flecha, doodles, mockups. */
  children?: React.ReactNode;
}> = ({
  foto,
  posicionFoto,
  // el bodegón real casi no se oscurece: la foto ya viene con fondo oscuro
  oscurecer = 0.1,
  caps,
  script,
  scriptSans,
  mantenerPunto,
  sizeCaps,
  bajada,
  bajadaEnCaja,
  interlineaBajada,
  columna = 1080 - 2 * BETWEEN.bloque.margenX,
  columnaCaja,
  aireTituloACaja = BETWEEN.aire.tituloACaja,
  velo,
  datos,
  arco,
  pie,
  legal,
  // en el feed de bodegón la marca la pone el vaso, no un logo sobrepuesto
  conLogo = false,
  logoTono = 'beige',
  logoPosicion = 'abajo',
  // MEDIDO: las dos piezas aprobadas están centradas sobre el eje. Between
  // compone centrado; el bloque a la izquierda no es su gramática.
  alinear = 'centro',
  anclaje = 'arriba',
  topBloque,
  children,
}) => {
  // Eli entrega DOS plantillas por formato (logo arriba / logo abajo) justo para
  // esto: si el bloque de texto baja, el logo sube. Si no, se pisan — pasó en 5
  // piezas de la ronda 4.
  const posLogo = anclaje === 'abajo' ? 'arriba' : logoPosicion;
  return (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <FotoFondo src={foto} posicion={posicionFoto} oscurecer={oscurecer} />
    {/* el velo va sobre la foto y DEBAJO del logo y del texto */}
    {velo ? (
      <AbsoluteFill style={{
        backgroundColor: BETWEEN.colores.sombra,
        opacity: velo,
        mixBlendMode: 'multiply',
      }} />
    ) : null}
    {conLogo ? <LogoBetween formato="feed" posicion={posLogo} tono={logoTono} /> : null}
    <AbsoluteFill>
      <div
        style={{
          position: 'absolute',
          left: BETWEEN.bloque.margenX,
          right: BETWEEN.bloque.margenX,
          // la medida (y=220) es a la TINTA; el ascendente de la caja alta pide unos px.
          // En fotos con personas el bloque baja para no pasar texto sobre caras.
          ...(topBloque !== undefined
            ? {top: topBloque}
            : anclaje === 'arriba'
              ? {top: BETWEEN.bloque.yFeed - 9}
              : {bottom: 130}),
          display: 'flex',
          flexDirection: 'column',
          alignItems: alinear === 'centro' ? 'center' : 'flex-start',
        }}
      >
        <TitularBetween
          caps={caps} script={script} scriptSans={scriptSans}
          sizeCaps={sizeCaps} alinear={alinear} anchoDisponible={columna}
          mantenerPunto={mantenerPunto}
        />
        {bajada && bajadaEnCaja ? (
          <PanelTaupe ancho={columnaCaja ?? columna} interlinea={interlineaBajada} style={{marginTop: aireTituloACaja}}>{bajada}</PanelTaupe>
        ) : bajada ? (
          <Bajada style={{marginTop: BETWEEN.aire.tituloABajada, textAlign: alinear === 'centro' ? 'center' : 'left'}}>{bajada}</Bajada>
        ) : null}
        {datos?.length ? <PilaDatos datos={datos} style={{marginTop: BETWEEN.aire.tituloACaja}} /> : null}
      </div>
    </AbsoluteFill>
    {children}
    {arco ? <TextoArco>{arco}</TextoArco> : null}
    {pie ? <PieDePieza formato="feed" {...pie} /> : null}
    {legal ? <LegalAlPie formato="feed">{legal}</LegalAlPie> : null}
  </AbsoluteFill>
  );
};

/**
 * ⭐ Línea de llamado: línea fina que sale de una etiqueta y apunta a una parte
 * de la foto, con un punto en la punta. Recurso propio de Eli — aparece en las
 * historias de cheesecake, «LUNES DE CAFÉ» y «Día del Cacao».
 * Grosor MEDIDO en ST S1 N°3: **2 px**.
 */
export const LineaLlamado: React.FC<{
  desde: [number, number];
  hasta: [number, number];
  /** Punto en la punta, como en «LA MEJOR FORMA DE EMPEZAR LA SEMANA». */
  punto?: boolean;
  tono?: Tono;
  ancho?: number;
  alto?: number;
}> = ({desde, hasta, punto = true, tono = 'beige', ancho = 1080, alto = 1920}) => (
  <svg width={ancho} height={alto} viewBox={`0 0 ${ancho} ${alto}`} style={{position: 'absolute', inset: 0}}>
    <line
      x1={desde[0]} y1={desde[1]} x2={hasta[0]} y2={hasta[1]}
      stroke={tinta(tono)} strokeWidth={2}
    />
    {punto ? <circle cx={hasta[0]} cy={hasta[1]} r={7} fill={tinta(tono)} /> : null}
  </svg>
);

/**
 * ⭐ Marco de esquinas sobre el producto — las cuatro escuadras finas que Eli
 * pone alrededor del plato (historia del cheesecake). Mismo grosor de 2 px.
 */
export const MarcoEsquinas: React.FC<{
  x: number; y: number; w: number; h: number;
  /** Largo del brazo de cada escuadra. */
  brazo?: number;
  tono?: Tono;
  ancho?: number; alto?: number;
}> = ({x, y, w, h, brazo = 64, tono = 'beige', ancho = 1080, alto = 1920}) => {
  const c = tinta(tono);
  const esquinas = [
    `M ${x} ${y + brazo} L ${x} ${y} L ${x + brazo} ${y}`,
    `M ${x + w - brazo} ${y} L ${x + w} ${y} L ${x + w} ${y + brazo}`,
    `M ${x + w} ${y + h - brazo} L ${x + w} ${y + h} L ${x + w - brazo} ${y + h}`,
    `M ${x + brazo} ${y + h} L ${x} ${y + h} L ${x} ${y + h - brazo}`,
  ];
  return (
    <svg width={ancho} height={alto} viewBox={`0 0 ${ancho} ${alto}`} style={{position: 'absolute', inset: 0}}>
      {esquinas.map((d, i) => (
        <path key={i} d={d} stroke={c} strokeWidth={2} fill="none" />
      ))}
    </svg>
  );
};

/**
 * ⭐ Tarjeta de UI en crema — el recurso de los mockups de Eli (recordatorio,
 * lista de horarios con toggles, píldora de carnet, post de Instagram).
 * Color MEDIDO: `#FFF9EB` (el beige de marca), texto en café, esquinas suaves.
 */
export const TarjetaUI: React.FC<{
  children: React.ReactNode;
  x?: number; y?: number; w?: number;
  radio?: number;
  style?: React.CSSProperties;
}> = ({children, x, y, w, radio = 20, style}) => (
  <div
    style={{
      position: x === undefined ? 'relative' : 'absolute',
      left: x, top: y, width: w,
      backgroundColor: BETWEEN.colores.beige,
      color: BETWEEN.colores.cafe,
      borderRadius: radio,
      padding: '28px 34px',
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.regular,
      fontSize: 34,
      lineHeight: 1.35,
      boxShadow: '0 10px 34px rgba(36,26,18,0.28)',
      ...style,
    }}
  >
    {children}
  </div>
);

/**
 * ⭐ Plantilla de story real: foto clara + logo centrado arriba + titular
 * (caps + script solapada) + lo que haga falta debajo.
 * Geometría medida: logo en y=271 y titular arrancando en y=425.
 */
export const PiezaStoryBetween: React.FC<{
  foto: string;
  posicionFoto?: string;
  oscurecer?: number;
  caps?: string;
  script?: string;
  sizeCaps?: number;
  datos?: React.ReactNode[];
  bajada?: React.ReactNode;
  /** La bajada va DENTRO de una caja taupe, para cuando la foto no la deja leer. */
  bajadaEnCaja?: boolean;
  /** Ancho máximo de esa caja. A todo el ancho se ve pesada sobre un producto. */
  anchoBajada?: number;
  legal?: React.ReactNode;
  conLogo?: boolean;
  logoTono?: Tono;
  alinear?: 'izquierda' | 'centro';
  /** En fotos con personas el bloque baja para no pasar texto sobre caras ni ojos. */
  anclaje?: 'arriba' | 'abajo';
  /** Y exacta del bloque, cuando ni arriba ni abajo sirven. */
  topBloque?: number;
  children?: React.ReactNode;
}> = ({
  foto, posicionFoto, oscurecer = 0.12,
  caps, script, sizeCaps, datos, bajada, bajadaEnCaja, anchoBajada, legal,
  conLogo = true, logoTono = 'beige', alinear = 'centro', anclaje = 'arriba',
  topBloque, children,
}) => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <FotoFondo src={foto} posicion={posicionFoto} oscurecer={oscurecer} />
    {conLogo ? <LogoBetween formato="story" posicion="arriba" tono={logoTono} /> : null}
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        right: BETWEEN.bloque.margenX,
        // 'abajo' se queda sobre la zona segura de Meta (340 px) con holgura
        ...(topBloque !== undefined
          ? {top: topBloque}
          : anclaje === 'arriba'
            ? {top: BETWEEN.bloque.yStory - 9}
            : {bottom: 430}),
        display: 'flex',
        flexDirection: 'column',
        alignItems: alinear === 'centro' ? 'center' : 'flex-start',
      }}
    >
      <TitularBetween caps={caps} script={script} sizeCaps={sizeCaps} alinear={alinear} />
      {datos?.length ? <PilaDatos datos={datos} style={{marginTop: BETWEEN.aire.tituloACaja}} /> : null}
      {bajada && bajadaEnCaja ? (
        <PanelTaupe ancho={anchoBajada} style={{marginTop: BETWEEN.aire.tituloACaja}}>{bajada}</PanelTaupe>
      ) : bajada ? (
        <Bajada style={{marginTop: BETWEEN.aire.tituloABajada, textAlign: alinear === 'centro' ? 'center' : 'left'}}>{bajada}</Bajada>
      ) : null}
    </div>
    {children}
    {legal ? (
      <div style={{position: 'absolute', left: 90, right: 90, bottom: 360}}>
        <Legal>{legal}</Legal>
      </div>
    ) : null}
  </AbsoluteFill>
);
