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
        fontVariantNumeric: 'tabular-nums',
        color: tinta(tono),
        lineHeight: enMayuscula ? 1.05 : 1.15,
        textWrap: 'balance',
        textShadow: sobreFoto ? sombraSobreFoto : undefined,
        ...style,
      }}
    >
      {sinPuntoFinal(children)}
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
      fontVariantNumeric: 'tabular-nums',
      color: tinta(tono),
      textShadow: sombraSobreFoto,
      ...style,
    }}
  >
    {children}
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
}> = ({children, size = BETWEEN.tipos.cajaDato, anchoDisponible = 1080 - 2 * BETWEEN.bloque.x, style}) => {
  // la caja va en nowrap, así que si el dato es largo hay que bajar el cuerpo:
  // «SEGUNDO NIVEL · TRABAJAR O REUNIRTE» se salía 46 px por la derecha
  const texto = typeof children === 'string' ? children.toUpperCase() : '';
  const cuerpo = texto
    ? ajustarACaber(texto, size, (v) => `300 ${v}px ${BETWEEN.fuentes.sans}`,
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
      fontWeight: 300,
      fontSize: cuerpo,
      lineHeight: 1,
      color: BETWEEN.colores.beige,
      textTransform: 'uppercase',
      whiteSpace: 'nowrap',
      fontVariantNumeric: 'tabular-nums',
      ...style,
    }}
  >
    {children}
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
 * Cuánto se sale la tinta a la IZQUIERDA del punto de origen. Brushwell tiene
 * remates de pincel que vuelan bastante (la «p» de «perfecto» vuela 39 px a 186
 * de cuerpo), y sin compensarlo la palabra se mete en el margen: en la pieza de
 * Eli la tinta de la script cae exacto en x=114, no antes.
 */
const voladizoIzquierdo = (texto: string, css: string): number => {
  if (typeof document === 'undefined') return 0;
  if (!_ctx) _ctx = document.createElement('canvas').getContext('2d');
  if (!_ctx) return 0;
  _ctx.font = css;
  const m = _ctx.measureText(texto);
  return Math.max(m.actualBoundingBoxLeft ?? 0, 0);
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
 *  - la script va a `proporcionScript` = 1,97 × la caja alta (antes: 1,2)
 *  - las dos líneas se **solapan**: la tinta queda a 2 px (antes: gap de 22)
 *  - el bloque se alinea a la izquierda por defecto (antes: siempre centrado)
 *  - trackings medidos: −1 en la caja alta, +18 en la script
 */
export const TitularBetween: React.FC<{
  caps?: string;
  script?: string;
  sizeCaps?: number;
  tono?: Tono;
  alinear?: 'izquierda' | 'centro';
  /** Ancho útil del bloque. Por defecto 1080 − 2×114 = 852 (los márgenes medidos). */
  anchoDisponible?: number;
  style?: React.CSSProperties;
}> = ({
  caps,
  script,
  sizeCaps = BETWEEN.tipos.tituloCaps,
  tono = 'beige',
  alinear = 'izquierda',
  anchoDisponible = 1080 - 2 * BETWEEN.bloque.x,
  style,
}) => {
  const cssScript = (s: number) => `${s}px ${BETWEEN.fuentes.script}`;
  const sizeScript = script
    ? ajustarACaber(
        script,
        Math.round(sizeCaps * BETWEEN.proporcionScript),
        cssScript,
        anchoDisponible,
        BETWEEN.trackingScript,
      )
    : 0;
  const voladizo = script ? Math.round(voladizoIzquierdo(script, cssScript(sizeScript))) : 0;
  // medido: la tinta de la script empieza en el margen (x=114) y la caja alta
  // 37 px más adentro (x=151)
  const sangriaCaps = alinear === 'izquierda' && script ? 37 : 0;
  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: alinear === 'centro' ? 'center' : 'flex-start',
        textAlign: alinear === 'centro' ? 'center' : 'left',
        ...style,
      }}
    >
      {caps ? (
        <div
          style={{
            fontFamily: BETWEEN.fuentes.sans,
            fontWeight: BETWEEN.pesos.black,
            fontSize: sizeCaps,
            letterSpacing: BETWEEN.trackingCaps,
            lineHeight: 1.0,
            textTransform: 'uppercase',
            marginLeft: sangriaCaps,
            // sin esto la caja alta se desborda por la derecha al indentarla
            maxWidth: anchoDisponible - sangriaCaps,
            color: tinta(tono),
            textShadow: sombraSobreFoto,
          }}
        >
          {sinPuntoFinal(caps)}
        </div>
      ) : null}
      {script ? (
        <div
          style={{
            fontFamily: BETWEEN.fuentes.script,
            fontSize: sizeScript,
            letterSpacing: BETWEEN.trackingScript,
            lineHeight: 1.0,
            // en las piezas de Eli la script jamás se parte en dos líneas
            whiteSpace: 'nowrap',
            color: tinta(tono),
            textShadow: sombraSobreFoto,
            // la script se MONTA sobre la caja alta: la tinta queda a ~2 px
            // calibrado: deja la tinta de la script a ~1 px de la caja alta,
            // que es el solape exacto de las piezas de Eli
            marginTop: -sizeScript * 0.23,
            marginLeft: alinear === 'izquierda' ? voladizo : 0,
          }}
        >
          {signosVolteados(sinPuntoFinal(script))}
        </div>
      ) : null}
    </div>
  );
};

/**
 * ⭐ Texto en arco al pie de la pieza («VIGILANTES, MUFFIN, BROWNIE Y MÁS»).
 * Curva medida sobre la pieza real: cuerda 864 px, flecha 135 px.
 * La bézier `M 108 1097 Q 540 1367 972 1097` pasa exactamente por los tres
 * puntos medidos (extremos en y=1097, fondo en y=1232).
 */
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
export const PiezaFeedBodegon: React.FC<{
  foto: string;
  posicionFoto?: string;
  oscurecer?: number;
  caps?: string;
  script?: string;
  sizeCaps?: number;
  datos?: React.ReactNode[];
  arco?: string;
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
}> = ({
  foto,
  posicionFoto,
  // el bodegón real casi no se oscurece: la foto ya viene con fondo oscuro
  oscurecer = 0.1,
  caps,
  script,
  sizeCaps,
  datos,
  arco,
  // en el feed de bodegón la marca la pone el vaso, no un logo sobrepuesto
  conLogo = false,
  logoTono = 'beige',
  logoPosicion = 'abajo',
  alinear = 'izquierda',
  anclaje = 'arriba',
}) => {
  // Eli entrega DOS plantillas por formato (logo arriba / logo abajo) justo para
  // esto: si el bloque de texto baja, el logo sube. Si no, se pisan — pasó en 5
  // piezas de la ronda 4.
  const posLogo = anclaje === 'abajo' ? 'arriba' : logoPosicion;
  return (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <FotoFondo src={foto} posicion={posicionFoto} oscurecer={oscurecer} />
    {conLogo ? <LogoBetween formato="feed" posicion={posLogo} tono={logoTono} /> : null}
    <AbsoluteFill>
      <div
        style={{
          position: 'absolute',
          left: BETWEEN.bloque.x,
          right: BETWEEN.bloque.x,
          // la medida (y=220) es a la TINTA; el ascendente de la caja alta pide unos px.
          // En fotos con personas el bloque baja para no pasar texto sobre caras.
          ...(anclaje === 'arriba' ? {top: BETWEEN.bloque.yFeed - 9} : {bottom: 130}),
          display: 'flex',
          flexDirection: 'column',
          alignItems: alinear === 'centro' ? 'center' : 'flex-start',
        }}
      >
        <TitularBetween caps={caps} script={script} sizeCaps={sizeCaps} alinear={alinear} />
        {datos?.length ? <PilaDatos datos={datos} style={{marginTop: 14}} /> : null}
      </div>
    </AbsoluteFill>
    {arco ? <TextoArco>{arco}</TextoArco> : null}
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
  legal?: React.ReactNode;
  conLogo?: boolean;
  logoTono?: Tono;
  alinear?: 'izquierda' | 'centro';
  /** En fotos con personas el bloque baja para no pasar texto sobre caras ni ojos. */
  anclaje?: 'arriba' | 'abajo';
  children?: React.ReactNode;
}> = ({
  foto, posicionFoto, oscurecer = 0.12,
  caps, script, sizeCaps, datos, bajada, legal,
  conLogo = true, logoTono = 'beige', alinear = 'centro', anclaje = 'arriba', children,
}) => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <FotoFondo src={foto} posicion={posicionFoto} oscurecer={oscurecer} />
    {conLogo ? <LogoBetween formato="story" posicion="arriba" tono={logoTono} /> : null}
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.x,
        right: BETWEEN.bloque.x,
        // 'abajo' se queda sobre la zona segura de Meta (340 px) con holgura
        ...(anclaje === 'arriba' ? {top: BETWEEN.bloque.yStory - 9} : {bottom: 430}),
        display: 'flex',
        flexDirection: 'column',
        alignItems: alinear === 'centro' ? 'center' : 'flex-start',
      }}
    >
      <TitularBetween caps={caps} script={script} sizeCaps={sizeCaps} alinear={alinear} />
      {datos?.length ? <PilaDatos datos={datos} style={{marginTop: 14}} /> : null}
      {bajada ? (
        <Bajada style={{marginTop: 18, textAlign: alinear === 'centro' ? 'center' : 'left'}}>{bajada}</Bajada>
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
