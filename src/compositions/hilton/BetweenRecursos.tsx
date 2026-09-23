/**
 * Recursos gráficos BETWEEN
 *
 * Los globos, flechas, confeti y corazón son las ilustraciones ORIGINALES de Eli
 * (su .ai/.svg de Illustrator), no una aproximación. — los dispositivos que usa Eli en las piezas aprobadas:
 *  - ILUSTRACIONES / Ilustra / Globos: el set original de Eli (globos, flechas, confeti)
 *  - CajaTexto: caja semitransparente para horarios ("DE 08:00 A 10:00 HRS")
 *  - LockupToGo: "To Go" script + "BY BETWEEN" caps
 *  - MarcoIGPost + BurbujaChat: mockup de post de Instagram con burbujas de detalle
 *  - SelectorTexto: mockup de selección de texto iOS ("Copiar | Selec. todo | Consultar")
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {BETWEEN} from '../../brand/hilton-between';
/* `conCifras` construye la caja tabular a mano (Raleway no trae `tnum`). Se
   importa desde el sistema y NO al revés: `BetweenSistema.tsx` no conoce este
   archivo, así que no hay ciclo — verificado antes de agregar el import. */
import {conCifras} from './BetweenSistema';

/* ---------- ilustraciones de Eli ---------- */

/**
 * Ilustraciones ORIGINALES de Eli, extraídas de su archivo de Illustrator
 * («Flechas y trazados, globos BETWEEN.ai/.svg») y recortadas una por una
 * midiendo el canal alfa. Trazo de pincel con desgaste, en el beige de marca.
 *
 * Regla de uso de Eli: acompañan, no dominan. Van en poca proporción de la
 * grilla — del orden del 20% de las historias — y siempre sutiles.
 */
export const ILUSTRACIONES = {
  globo: 'assets/hilton/between/recursos/globo.png',
  globoAlt: 'assets/hilton/between/recursos/globo-alt.png',
  globosPar: 'assets/hilton/between/recursos/globos-par.png',
  confeti: 'assets/hilton/between/recursos/confeti.png',
  corazon: 'assets/hilton/between/recursos/corazon.png',
  flechaBucle: 'assets/hilton/between/recursos/flecha-bucle.png',
  flechaGrande: 'assets/hilton/between/recursos/flecha-grande.png',
  flechaCirculo: 'assets/hilton/between/recursos/flecha-circulo.png',

  /**
   * ⭐ SOL y NUBES — 09-09-2026, pedido de Eli para la ST del 22-09: «la
   * referencia de la ST tenía líneas de dibujo como BW, debes añadir sol y nubes
   * como ilustración, guíate de mis editables para dibujarlo correctamente».
   *
   * ⚠️ Estos tres NO salen de su `.svg`: se comprobó rindiendo su plancha
   * completa (composición `BW-Plancha-Trazos`) y ahí sólo hay confeti, corazón,
   * tres flechas, una flecha abajo y tres globos. O sea que «guíate de mis
   * editables» es **dibújalos con MI mano**, no «cópialos».
   *
   * Se dibujan en `scripts/between-trazos-sol-nubes.py` con su mano MEDIDA sobre
   * su propio archivo: tinta `#fffaee` (su clase `.st2`, que no es el beige
   * `#fff9eb` del texto), contorno RELLENO y no trazo —su pincel está expandido
   * a contornos—, su sombra `drop-shadow-2` (4/4/3, negro 25 %) y el grosor del
   * trazo al 2 % del ancho del dibujo, que es lo que miden los doodles de la
   * referencia de contenido.
   */
  sol: 'assets/hilton/between/recursos/sol.png',
  nube: 'assets/hilton/between/recursos/nube.png',
  nubeChica: 'assets/hilton/between/recursos/nube-chica.png',

  /**
   * ⭐⭐ SEGUNDA TANDA — el boceto que mandó Eli el mismo 09-09 sobre la pieza
   * ya corregida: «necesito una ilustración como la que te dejo en esta
   * captura». Su dibujo pide tres cosas que la primera tanda no tenía:
   *
   *   1. **tamaño**: dibujos grandes que **sangran por los bordes** del cuadro,
   *      no viñetas contenidas dentro del margen;
   *   2. **doble contorno**: la línea va REPASADA, como cuando la mano vuelve
   *      sobre el trazo. Se consigue dibujando la misma línea dos veces — el
   *      temblor se sortea en cada pasada, así que salen parecidas y no iguales;
   *   3. **rayitas de acento**: grupos de dos o tres trazos cortos y curvos,
   *      sueltos, que llenan el aire sin dibujar nada concreto. Son el primo
   *      discreto del `confeti` que ya está en su plancha.
   *
   * `solGrande` está pensado para poner el centro FUERA del cuadro: lo que se ve
   * es un arco enorme en la esquina con sus rayos, que es lo que hace su boceto.
   */
  solGrande: 'assets/hilton/between/recursos/sol-grande.png',
  nubeDoble: 'assets/hilton/between/recursos/nube-doble.png',
  nubeDobleChica: 'assets/hilton/between/recursos/nube-doble-chica.png',
  rayitas: 'assets/hilton/between/recursos/rayitas.png',
} as const;

export type Ilustracion = keyof typeof ILUSTRACIONES;

/** Una ilustración suelta, posicionada en el lienzo. */
export const Ilustra: React.FC<{
  cual: Ilustracion;
  x: number;
  y: number;
  ancho: number;
  rotacion?: number;
  opacidad?: number;
  espejo?: boolean;
}> = ({cual, x, y, ancho, rotacion = 0, opacidad = 1, espejo = false}) => (
  <Img
    src={staticFile(ILUSTRACIONES[cual])}
    style={{
      position: 'absolute',
      left: x,
      top: y,
      width: ancho,
      opacity: opacidad,
      transform: `rotate(${rotacion}deg)${espejo ? ' scaleX(-1)' : ''}`,
      pointerEvents: 'none',
    }}
  />
);

/** Globos repartidos, como en las piezas de cumpleaños de Eli. */
export const Globos: React.FC<{
  posiciones?: {cual?: Ilustracion; x: number; y: number; ancho: number; rotacion?: number; espejo?: boolean}[];
}> = ({
  posiciones = [
    {cual: 'globo', x: 90, y: 640, ancho: 150, rotacion: -10},
    {cual: 'globoAlt', x: 880, y: 720, ancho: 130, rotacion: 14, espejo: true},
  ],
}) => (
  <>
    {posiciones.map((p, i) => (
      <Ilustra
        key={i}
        cual={p.cual ?? 'globo'}
        x={p.x}
        y={p.y}
        ancho={p.ancho}
        rotacion={p.rotacion}
        espejo={p.espejo}
      />
    ))}
  </>
);

/* ---------- caja de texto (horario) ---------- */

export const CajaTexto: React.FC<{
  children: React.ReactNode;
  size?: number;
  style?: React.CSSProperties;
}> = ({children, size = 30, style}) => (
  <div
    style={{
      display: 'inline-block',
      background: 'rgba(103,91,73,0.82)',
      color: BETWEEN.colores.beige,
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: 600,
      fontSize: size,
      letterSpacing: 3,
      textTransform: 'uppercase',
      padding: '10px 26px',
      ...style,
    }}
  >
    {children}
  </div>
);

/* ---------- lockup To Go ---------- */

export const LockupToGo: React.FC<{horario?: string; style?: React.CSSProperties}> = ({
  horario = 'De 08:00 a 10:00 hrs',
  style,
}) => (
  <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', ...style}}>
    <div
      style={{
        fontFamily: BETWEEN.fuentes.script,
        fontSize: 110,
        color: BETWEEN.colores.beige,
        lineHeight: 0.9,
        textShadow: '0 3px 20px rgba(0,0,0,0.5)',
      }}
    >
      To Go
    </div>
    <div
      style={{
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: 700,
        fontSize: 48,
        letterSpacing: 5,
        color: BETWEEN.colores.beige,
        textTransform: 'uppercase',
        marginTop: 4,
        textShadow: '0 3px 20px rgba(0,0,0,0.5)',
      }}
    >
      by Between
    </div>
    {horario ? <CajaTexto style={{marginTop: 12}}>{horario}</CajaTexto> : null}
  </div>
);

/* ---------- mockup post IG con burbujas ---------- */

export const BurbujaChat: React.FC<{
  children: React.ReactNode;
  /**
   * ⭐ RONDA 11 — ancho FIJO, y es una corrección medida sobre el editable de
   * Eli. Ahí las cinco burbujas se dimensionan al contenido y quedan con cinco
   * cantos derechos distintos, y las tres más largas **se salen del marco
   * blanco del mock**: el marco termina en x=882 y la burbuja llega a 943, o
   * sea 61 px afuera. Es el mismo defecto que la memoria
   * `ui-mock-anti-desborde` dejó escrito con la píldora del reel de EBEMA.
   * Con `ancho` las cinco comparten canto —la regla del manual, «una pila de
   * cajas va toda del MISMO ANCHO» (§1 bis)— y no hay forma de que sangren.
   */
  ancho?: number;
  size?: number;
}> = ({children, ancho, size = 31}) => (
  <div
    style={{
      background: 'rgba(103,91,73,0.93)',
      color: '#fff',
      /* Raleway está auto-hospedada y no trae emojis: sin nombrar la fuente de
         color del sistema, Chrome cae en un glifo monocromo y los emojis que
         pidió el cliente («incluir emojis nuevamente») salen como manchas
         grises. Se añade al final de la pila para que solo actúe de reserva. */
      fontFamily: `${BETWEEN.fuentes.sans}, 'Apple Color Emoji', 'Segoe UI Emoji', 'Noto Color Emoji'`,
      fontWeight: 600,
      fontSize: size,
      lineHeight: 1.3,
      padding: `${Math.round(size * 0.55)}px ${Math.round(size * 0.8)}px`,
      borderRadius: 16,
      marginBottom: Math.round(size * 0.5),
      ...(ancho ? {width: ancho, boxSizing: 'border-box' as const} : {maxWidth: 560}),
      alignSelf: 'flex-end',
      display: 'flex',
      gap: Math.round(size * 0.42),
    }}
  >
    <span style={{flexShrink: 0}}>•</span>
    <span>{children}</span>
  </div>
);

/**
 * Checklist de condiciones sobre panel taupe.
 *
 * ⭐ RONDA 5 (31-08-2026), comentario de Scarlette sobre la G2 del cumpleaños:
 * «No me gusta como se ve como post, haria un check list junto con los emojis
 * que piden». Reemplaza al `MarcoIGPost`: el mockup de Instagram metía una foto
 * dentro de la pieza —un post dentro de un post— y ella lo quiere directo.
 *
 * El emoji que pide el cliente se conserva a la izquierda de cada línea y el
 * palito del check va aparte, para que se lea como lista y no como viñeta. La
 * pila de fuentes nombra las de color del sistema por la misma razón que
 * `BurbujaChat`: Raleway está auto-hospedada y no trae emojis.
 */
export const Checklist: React.FC<{
  items: string[];
  titulo?: string;
  notaLegal?: string;
  ancho?: number;
  /** Cuerpo de cada ítem. En STORY hay que bajarlo: el mismo listado que en el
   *  feed convive con el titular Y con el producto, y a 34 px tapa el vaso. */
  size?: number;
  gap?: number;
}> = ({items, titulo, notaLegal, ancho = 860, size = 34, gap = 22}) => (
  <div
    style={{
      width: ancho,
      background: 'rgba(103,91,73,0.93)',
      borderRadius: 18,
      padding: `${Math.round(size * 1.12)}px ${Math.round(size * 1.3)}px`,
      boxShadow: '0 24px 60px rgba(0,0,0,0.35)',
      display: 'flex',
      flexDirection: 'column',
      gap,
    }}
  >
    {titulo ? (
      <div
        style={{
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: BETWEEN.pesos.extrabold,
          fontSize: 40,
          letterSpacing: '-0.01em',
          color: BETWEEN.colores.beige,
          textTransform: 'uppercase',
        }}
      >
        {titulo}
      </div>
    ) : null}

    {items.map((t, i) => (
      <div key={i} style={{display: 'flex', alignItems: 'flex-start', gap: Math.round(size * 0.53)}}>
        <div
          style={{
            flexShrink: 0,
            width: Math.round(size * 1.18),
            height: Math.round(size * 1.18),
            borderRadius: 8,
            border: `${Math.max(2, size * 0.074).toFixed(1)}px solid ${BETWEEN.colores.beige}`,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: Math.round(size * 0.76),
            lineHeight: 1,
            color: BETWEEN.colores.beige,
            fontFamily: BETWEEN.fuentes.sans,
            fontWeight: 800,
          }}
        >
          ✓
        </div>
        <div
          style={{
            fontFamily: `${BETWEEN.fuentes.sans}, 'Apple Color Emoji', 'Segoe UI Emoji', 'Noto Color Emoji'`,
            fontWeight: 600,
            fontSize: size,
            lineHeight: 1.28,
            color: '#fff',
          }}
        >
          {t}
        </div>
      </div>
    ))}

    {notaLegal ? (
      <div
        style={{
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: 500,
          fontSize: Math.round(size * 0.71),
          lineHeight: 1.3,
          color: 'rgba(255,255,255,0.72)',
          marginTop: 4,
        }}
      >
        {notaLegal}
      </div>
    ) : null}
  </div>
);

/**
 * Mock de un post de Instagram: el marco blanco con cabecera, la foto adentro,
 * las burbujas del listado encima y la barra de acciones abajo.
 *
 * ⭐⭐ RONDA 11 (04-09-2026) — vuelve al sistema, y con geometría MEDIDA.
 * Eli entregó su editable de la slide 2 del cumpleaños («para que lo mejores»)
 * y este mock es su diseño. La ronda 5 lo había sacado por criterio propio
 * («un post dentro de un post»); manda la diseñadora, así que vuelve — pero
 * arreglado.
 *
 * Las medidas salen de rasterizar su `.eps` a 1080×1350 y medirlo:
 *   · marco  x 197-882 (685 de ancho) · y 203-1101 (898 de alto)
 *   · ventana de la foto  x 227-855 (628) · y 300-940 (640)
 *   · cabecera 97 px · barra de acciones + usuario 161 px
 * O sea: relleno de 30 px, y la ventana es casi cuadrada (0,98), como un post.
 *
 * Los tres arreglos sobre su archivo:
 *   1. las burbujas ya no se salen del marco ni quedan con cantos desparejos
 *      (ver `BurbujaChat.ancho`);
 *   2. el avatar es el LOGOTIPO real, no las letras «B∃TW» dibujadas a mano;
 *   3. el marco es BLANCO, como el de Instagram. En beige de marca el mock
 *      dejaba de leerse como una captura y se leía como una tarjeta.
 */
export const MarcoIGPost: React.FC<{
  usuario?: string;
  foto: React.ReactNode;
  burbujas?: React.ReactNode[];
  notaLegal?: string;
  /** Ancho del marco. 685 es el del editable de Eli sobre lienzo 1080. */
  ancho?: number;
  /** Alto de la ventana de la foto. 640 en el editable. */
  altoFoto?: number;
  /** Cuerpo de las burbujas. */
  sizeBurbuja?: number;
}> = ({
  usuario = 'between.coffeebar',
  foto,
  burbujas = [],
  notaLegal,
  ancho = 685,
  altoFoto = 640,
  sizeBurbuja = 26,
}) => {
  const relleno = Math.round(ancho * 0.0438);          // 30 sobre 685
  const anchoVentana = ancho - relleno * 2;
  /* Las burbujas se apoyan en el canto derecho de la ventana con un aire de
     `margen`, así que su ancho máximo es la ventana menos los dos aires. */
  const margen = Math.round(anchoVentana * 0.035);
  const anchoBurbuja = anchoVentana - margen * 2;
  return (
    <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
      <div
        style={{
          width: ancho,
          background: '#ffffff',
          borderRadius: 10,
          padding: `${relleno}px ${relleno}px ${Math.round(relleno * 0.9)}px`,
          boxShadow: '0 26px 64px rgba(0,0,0,0.38)',
        }}
      >
        {/* cabecera */}
        <div style={{display: 'flex', alignItems: 'center', gap: 16, marginBottom: relleno * 0.6}}>
          {/* ⛔ RONDA 12 — Eli: «el logo del icono de la segunda slide no es los
              colores que se utiliza. Es fondo café between + logo en beige».
              Estaba al revés: círculo blanco con el logotipo en café. El ícono
              de perfil de la marca es el disco en el CAFÉ `#675B49` con el
              lockup en el beige `#FFF9EB` — los dos colores de marca, en su
              orden. Se le quita también el aro claro, que sobre el disco café
              no aporta y ensuciaba el canto. */}
          <div
            style={{
              width: 66, height: 66, borderRadius: '50%',
              background: BETWEEN.colores.cafe,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              overflow: 'hidden', flexShrink: 0,
            }}
          >
            <Img
              src={staticFile(BETWEEN.logo.beige)}
              style={{width: 44, height: 44 / BETWEEN.logo.ratio, objectFit: 'contain'}}
            />
          </div>
          <div
            style={{
              fontFamily: BETWEEN.fuentes.sans, fontWeight: 700, fontSize: 34,
              color: '#3b2f24', letterSpacing: '-0.005em',
            }}
          >
            {usuario}
          </div>
          <div style={{marginLeft: 'auto', fontSize: 32, color: '#7a6a58', letterSpacing: 3}}>•••</div>
        </div>

        {/* la ventana de la foto, con las burbujas encima */}
        <div
          style={{
            position: 'relative', width: anchoVentana, height: altoFoto,
            borderRadius: 3, overflow: 'hidden',
          }}
        >
          {foto}
          <div
            style={{
              position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column',
              justifyContent: 'center', alignItems: 'flex-end',
              padding: `${margen}px ${margen}px 0`,
            }}
          >
            {burbujas.map((b, i) => (
              <BurbujaChat key={i} ancho={anchoBurbuja} size={sizeBurbuja}>
                {b}
              </BurbujaChat>
            ))}
          </div>
        </div>

        {/* barra de acciones */}
        <div style={{display: 'flex', alignItems: 'center', gap: 26, marginTop: relleno * 0.75, color: '#3b2f24'}}>
          <span style={{fontSize: 42, color: '#e0443a', lineHeight: 1}}>♥</span>
          <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#3b2f24" strokeWidth="1.8">
            <path d="M21 11.5a8.38 8.38 0 0 1-8.5 8.5 8.6 8.6 0 0 1-3.9-.95L3 21l1.95-5.6A8.38 8.38 0 0 1 4 11.5 8.5 8.5 0 0 1 12.5 3 8.38 8.38 0 0 1 21 11.5z" />
          </svg>
          <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#3b2f24" strokeWidth="1.8">
            <path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7z" />
          </svg>
          <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#3b2f24" strokeWidth="1.8" style={{marginLeft: 'auto'}}>
            <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
          </svg>
        </div>
        <div
          style={{
            fontFamily: BETWEEN.fuentes.sans, fontWeight: 700, fontSize: 30,
            color: '#7a6a58', marginTop: 12,
          }}
        >
          {usuario}
        </div>
      </div>
      {notaLegal ? (
        <div
          style={{
            fontFamily: BETWEEN.fuentes.sans, fontStyle: 'italic', fontWeight: 500,
            fontSize: 26, color: BETWEEN.colores.beige, textAlign: 'center', marginTop: 34,
            maxWidth: 820, lineHeight: 1.45, textShadow: '0 2px 14px rgba(0,0,0,0.65)',
          }}
        >
          {notaLegal}
        </div>
      ) : null}
    </div>
  );
};

/* ---------- selector de texto iOS ---------- */

export const SelectorTexto: React.FC<{
  lineas: string[];
  size?: number;
}> = ({lineas, size = 58}) => (
  <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
    {/* toolbar */}
    <div
      style={{
        display: 'flex', alignItems: 'stretch', background: '#fff', borderRadius: 14,
        overflow: 'hidden', boxShadow: '0 10px 30px rgba(0,0,0,0.35)', marginBottom: 34,
        fontFamily: BETWEEN.fuentes.sans, fontWeight: 500, fontSize: 34, color: '#1a1a1a',
      }}
    >
      {['Copiar', 'Selec. todo', 'Consultar'].map((t, i) => (
        <div key={t} style={{padding: '16px 28px', borderLeft: i ? '1px solid #d8d8d8' : 'none'}}>
          {t}
        </div>
      ))}
      <div style={{padding: '16px 22px', borderLeft: '1px solid #d8d8d8', display: 'flex', alignItems: 'center'}}>›</div>
    </div>
    {/* texto con resaltado de selección */}
    <div style={{position: 'relative', textAlign: 'center'}}>
      {lineas.map((l, i) => (
        <div
          key={l}
          style={{
            fontFamily: BETWEEN.fuentes.sans, fontWeight: 500, fontSize: size,
            color: '#fff', lineHeight: 1.35, textShadow: '0 2px 16px rgba(0,0,0,0.55)',
            display: 'inline-block',
            background: 'rgba(64,156,255,0.32)',
            padding: '2px 10px',
            position: 'relative',
          }}
        >
          {l}
          {i === 0 ? (
            <span style={{position: 'absolute', left: -6, top: -18, width: 14, height: 14, borderRadius: '50%', background: '#2f7ff0'}} />
          ) : null}
          {i === lineas.length - 1 ? (
            <span style={{position: 'absolute', right: -6, bottom: -18, width: 14, height: 14, borderRadius: '50%', background: '#2f7ff0'}} />
          ) : null}
        </div>
      ))}
    </div>
  </div>
);

/* ---------- composición editorial en 4 cuadrantes ---------- */

/** Cuatro fotos en rejilla, para piezas de ingredientes (ej. Strudel). */
export const Cuadrantes: React.FC<{
  fotos: string[];
  alto: number;
  gap?: number;
}> = ({fotos, alto, gap = 6}) => (
  <div
    style={{
      display: 'grid',
      gridTemplateColumns: '1fr 1fr',
      gridTemplateRows: '1fr 1fr',
      gap,
      height: alto,
      width: '100%',
    }}
  >
    {fotos.slice(0, 4).map((f) => (
      <div key={f} style={{overflow: 'hidden'}}>
        <Img src={staticFile(f)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      </div>
    ))}
  </div>
);

/* ---------- etiqueta suelta sobre la foto ---------- */

/**
 * Texto chico anclado a un punto del lienzo, para señalar algo dentro de la
 * imagen (ej. las dos tazas de «Ella habló / Ella escuchó»).
 */
export const Etiqueta: React.FC<{
  children: React.ReactNode;
  x: number;
  y: number;
  size?: number;
  script?: boolean;
  /** Sobre foto clara la sombra no alcanza: se apoya en la caja taupe. */
  enCaja?: boolean;
}> = ({children, x, y, size = 40, script = false, enCaja = false}) => (
  <div
    style={{
      position: 'absolute',
      left: x,
      top: y,
      transform: 'translateX(-50%)',
      fontFamily: script ? BETWEEN.fuentes.script : BETWEEN.fuentes.sans,
      fontWeight: script ? 400 : 600,
      fontSize: size,
      color: BETWEEN.colores.beige,
      textShadow: enCaja ? 'none' : '0 2px 16px rgba(36,26,18,0.75)',
      whiteSpace: 'nowrap',
      ...(enCaja
        ? {
            backgroundColor: BETWEEN.cajas.fondo,
            borderRadius: BETWEEN.cajas.radio,
            padding: `${Math.round(size * 0.30)}px ${Math.round(size * 0.62)}px`,
          }
        : {}),
    }}
  >
    {children}
  </div>
);

/* ---------- sticker de encuesta / quiz de Instagram ---------- */

export const StickerQuiz: React.FC<{
  pregunta: string;
  opciones: string[];
  /** Índice de la opción correcta; si se pasa, se resalta. */
  correcta?: number;
  ancho?: number;
  /** Versión baja, para cuando la foto deja poco alto libre sobre la zona
      segura inferior de las historias (340 px). */
  compacto?: boolean;
  /**
   * Opciones en DOS columnas (2×2), como muestra Instagram una encuesta de
   * cuatro alternativas.
   *
   * ⭐ 02-09-2026: hizo falta al poner las cuatro opciones que pide el brief de
   * «Emergencia Between» (las tres del brief más la que agregó el cliente). En
   * una sola columna el sticker mide ~326 px y arrancando en y=1318 terminaba
   * en 1644, o sea DENTRO de la zona segura inferior de Meta (que empieza en
   * 1580). En 2×2 baja a ~199 px y entra sin pelear con la caja.
   */
  dosColumnas?: boolean;
}> = ({pregunta, opciones, correcta, ancho = 660, compacto = false, dosColumnas = false}) => (
  <div
    style={{
      width: ancho,
      background: '#ffffff',
      borderRadius: 22,
      padding: compacto ? '20px 22px 18px' : '26px 24px 22px',
      boxShadow: '0 18px 44px rgba(36,26,18,0.32)',
      display: 'flex',
      flexDirection: 'column',
      gap: compacto ? 10 : 14,
    }}
  >
    <div
      style={{
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: 700,
        fontSize: compacto ? 28 : 32,
        color: '#1a1a1a',
        textAlign: 'center',
        lineHeight: 1.25,
      }}
    >
      {pregunta}
    </div>
    <div
      style={{
        display: dosColumnas ? 'grid' : 'flex',
        ...(dosColumnas
          ? {gridTemplateColumns: '1fr 1fr'}
          : {flexDirection: 'column' as const}),
        gap: compacto ? 10 : 14,
      }}
    >
      {opciones.map((o, i) => (
        <div
          key={o}
          style={{
            /* ⭐ RONDA 4 §3 del manual: Raleway está auto-hospedada y NO trae
               emojis. Sin nombrar la familia de color al final de la pila,
               Chrome cae en un glifo monocromo y los ☕ 🥐 🥪 salen como
               manchas grises. La encuesta de «Emergencia Between» los lleva
               por brief. */
            fontFamily: `${BETWEEN.fuentes.sans}, 'Apple Color Emoji', 'Segoe UI Emoji', 'Noto Color Emoji'`,
            fontWeight: i === correcta ? 700 : 500,
            fontSize: compacto ? 26 : 29,
            color: i === correcta ? BETWEEN.colores.beige : '#2b2b2b',
            background: i === correcta ? BETWEEN.colores.cafe : '#f1ede5',
            borderRadius: 14,
            padding: compacto ? '11px 20px' : '15px 22px',
            textAlign: 'center',
            /* en 2×2 las cuatro celdas tienen que verse del mismo alto aunque
               «Todas las anteriores» sea más largo que «☕ Café» */
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            lineHeight: 1.15,
          }}
        >
          {o}
        </div>
      ))}
    </div>
  </div>
);

/**
 * Sticker de ENLACE de Instagram.
 *
 * Ronda 4, comentario E15 del cliente: «Ok, enlace a carta!». El sticker lo
 * pega el community manager al publicar, pero si la pieza no le reserva el
 * sitio, termina puesto encima del titular. Se dibuja para que el espacio
 * quede tomado en el diseño y la story se apruebe tal como se va a ver.
 */
export const StickerEnlace: React.FC<{texto: string; ancho?: number}> = ({
  texto,
  ancho,
}) => (
  <div
    style={{
      width: ancho,
      display: 'inline-flex',
      alignItems: 'center',
      gap: 14,
      background: '#ffffff',
      borderRadius: 999,
      padding: '18px 30px',
      boxShadow: '0 14px 34px rgba(36,26,18,0.30)',
    }}
  >
    <svg width="34" height="34" viewBox="0 0 24 24" fill="none" aria-hidden>
      <path
        d="M10 13a5 5 0 0 0 7.07 0l2.12-2.12a5 5 0 0 0-7.07-7.07L10.8 5.06M14 11a5 5 0 0 0-7.07 0l-2.12 2.12a5 5 0 0 0 7.07 7.07L13.2 18.94"
        stroke="#1a1a1a"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
    <span
      style={{
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: 700,
        fontSize: 32,
        letterSpacing: '0.02em',
        color: '#1a1a1a',
        textTransform: 'uppercase',
        whiteSpace: 'nowrap',
      }}
    >
      {texto}
    </span>
  </div>
);

/* ═══════════════════════════════════════════════════════════════════════════
   REPERTORIO DE COMPOSICIÓN — agregado 27-08-2026

   Feedback de Valeria: «te quedas en el título arriba o abajo y es un poco
   aburrido… juegan más, tienen signos, flechitas, las fotos de los productos
   en tentadora». Revisando el Instagram real de Between, el vocabulario que
   faltaba usar es este, y las ilustraciones YA estaban extraídas del .svg de
   la diseñadora — solo no se estaban ocupando:

     · «Tu pausa favorita, ahora con togo» → etiqueta + flecha de bucle
       señalando CADA producto («Café grande», «Sándwich Ave palta»)
     · «¿Ya tomaste tu cafecito del día?» → flecha larga que baja desde la
       dirección hasta la taza
     · «Good Morning» → composición PARTIDA en dos fotos, script cruzando la
       costura, más marcas doodle
     · «SI ALGÚN DÍA NO quiero desayunar en Between…» → tres pesos en el mismo
       bloque: caja alta liviana, caja alta pesada y script

   Ninguno de estos recursos se inventa: todos salen de piezas publicadas.
   ═══════════════════════════════════════════════════════════════════════════ */

/**
 * Etiqueta que SEÑALA un producto, con la flecha de bucle de la diseñadora.
 * Es el recurso más reconocible de las piezas de promo y el que hacía falta.
 */
export const EtiquetaFlecha: React.FC<{
  children: React.ReactNode;
  /** Dónde va el texto (centro de la etiqueta), en px sobre lienzo de 1080. */
  x: number;
  y: number;
  /** Hacia dónde apunta: define de qué lado sale la flecha. */
  hacia?: 'derecha' | 'izquierda' | 'abajo';
  size?: number;
  /** Ancho de la flecha. La de bucle real de Eli va entre 150 y 260 px. */
  flecha?: number;
  /** Corrimiento de la flecha respecto del texto. */
  dx?: number;
  dy?: number;
  cual?: 'flechaBucle' | 'flechaGrande';
}> = ({children, x, y, hacia = 'derecha', size = 42, flecha = 220, dx = 0, dy = 0, cual = 'flechaBucle'}) => {
  const espejo = hacia === 'izquierda';
  const fx = hacia === 'abajo' ? x + dx : espejo ? x - flecha * 0.55 + dx : x + flecha * 0.15 + dx;
  const fy = hacia === 'abajo' ? y + size * 1.1 + dy : y - flecha * 0.30 + dy;
  return (
    <>
      <div
        style={{
          position: 'absolute',
          left: x,
          top: y,
          transform: 'translate(-50%, -50%)',
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: 600,
          fontSize: size,
          lineHeight: 1.15,
          color: BETWEEN.colores.beige,
          textShadow: '0 2px 14px rgba(36,26,18,0.7)',
          textAlign: 'center',
          whiteSpace: 'pre-line',
        }}
      >
        {children}
      </div>
      <Ilustra
        cual={cual}
        x={fx}
        y={fy}
        ancho={flecha}
        espejo={espejo}
        rotacion={hacia === 'abajo' ? 90 : 0}
        opacidad={0.95}
      />
    </>
  );
};

/**
 * Composición PARTIDA — dos fotos a media pieza con el texto cruzando la
 * costura, como el post «Good Morning». Rompe el «título arriba, foto abajo»
 * sin salirse de la línea.
 */
/**
 * ⭐ BOTÓN BLANCO — el llamado a la acción, macizo y en blanco.
 *
 * Pedido de Eli el 01-09-2026 para la ST del 1-sep: «la CTA sea "Pasa por
 * Between" y abajo del botón "y llévalo contigo". La idea que sea el único botón
 * en blanco y textos café del color de la marca».
 *
 * Por eso el texto va en `BETWEEN.colores.cafe` (#675b49) y no en beige: sobre
 * blanco macizo el beige no tiene contraste. Es el mismo café de las cajas
 * taupe, o sea el color de la marca, no uno nuevo.
 *
 * ⛔ **Uno por pieza.** Es el único elemento blanco macizo de la gramática: si
 * hay dos, deja de leerse como el llamado. Las demás cajas siguen siendo taupe.
 */
export const BotonBlanco: React.FC<{
  children: React.ReactNode;
  size?: number;
  style?: React.CSSProperties;
}> = ({children, size = 45, style}) => (
  <div
    style={{
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center',
      height: BETWEEN.cajas.alto,
      padding: `0 ${BETWEEN.cajas.padX}px`,
      background: '#ffffff',
      borderRadius: 999,
      boxShadow: '0 14px 34px rgba(36,26,18,0.28)',
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.extrabold,
      fontSize: size,
      lineHeight: 1,
      letterSpacing: '0.01em',
      color: BETWEEN.colores.cafe,
      textTransform: 'uppercase',
      whiteSpace: 'nowrap',
      ...style,
    }}
  >
    {children}
  </div>
);

export const PiezaPartida: React.FC<{
  izquierda: string;
  derecha: string;
  /** 'vertical' parte de arriba a abajo; 'horizontal' parte al medio. */
  eje?: 'vertical' | 'horizontal';
  children?: React.ReactNode;
}> = ({izquierda, derecha, eje = 'vertical', children}) => (
  <AbsoluteFill>
    <div
      style={{
        position: 'absolute',
        inset: 0,
        display: 'flex',
        flexDirection: eje === 'vertical' ? 'row' : 'column',
      }}
    >
      {[izquierda, derecha].map((f, i) => (
        <div key={i} style={{flex: 1, overflow: 'hidden', position: 'relative'}}>
          <Img
            src={staticFile(f)}
            style={{width: '100%', height: '100%', objectFit: 'cover'}}
          />
        </div>
      ))}
    </div>
    {children}
  </AbsoluteFill>
);

/**
 * Bloque de tres pesos en el mismo titular, como «SI ALGÚN DÍA / NO quiero
 * desayunar / en Between…»: caja alta liviana, caja alta pesada y script.
 * Cada línea es opcional.
 */
export const TituloTresPesos: React.FC<{
  arriba?: string;
  fuerte?: string;
  script?: string;
  size?: number;
  alinear?: 'centro' | 'izquierda';
  style?: React.CSSProperties;
}> = ({arriba, fuerte, script, size = 72, alinear = 'centro', style}) => (
  <div
    style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: alinear === 'centro' ? 'center' : 'flex-start',
      textAlign: alinear === 'centro' ? 'center' : 'left',
      color: BETWEEN.colores.beige,
      textShadow: '0 2px 16px rgba(36,26,18,0.55)',
      ...style,
    }}
  >
    {arriba ? (
      <div
        style={{
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: 500,
          fontSize: size * 0.72,
          letterSpacing: '0.02em',
          lineHeight: 1.1,
          textTransform: 'uppercase',
        }}
      >
        {arriba}
      </div>
    ) : null}
    {fuerte ? (
      <div
        style={{
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: BETWEEN.pesos.extrabold,
          fontSize: size,
          letterSpacing: '-0.02em',
          lineHeight: 1.05,
        }}
      >
        {fuerte}
      </div>
    ) : null}
    {script ? (
      <div
        style={{
          fontFamily: BETWEEN.fuentes.script,
          fontSize: size * 0.92,
          lineHeight: 1.05,
          marginTop: -size * 0.06,
          alignSelf: alinear === 'centro' ? 'center' : 'flex-end',
        }}
      >
        {script}
      </div>
    ) : null}
  </div>
);

/**
 * Pila de cajas taupe anclada ABAJO A LA IZQUIERDA, como en «Promo To Go /
 * Café + Sándwich desde $4.290». Alternativa al bloque centrado.
 *
 * ⚠️ El ejemplo decía «Café grande», que el cliente mandó sacar en la ronda 5
 * (31-08-2026). Se corrige acá también para que nadie lo copie del comentario.
 */
export const PilaEsquina: React.FC<{
  lineas: {texto: string; fuerte?: boolean}[];
  lado?: 'izquierda' | 'derecha';
  abajo?: number;
  /**
   * Todas las cajas al ancho de la MÁS ANCHA, en vez de que cada una se ajuste
   * a su texto.
   *
   * ⭐ 02-09-2026, pedido de Eli: «se ve todo desordenado en los textos y no se
   * ve pulcro». Con cada caja a su medida la pila queda en ESCALERA —tres
   * anchos distintos y tres bordes derechos distintos—, y eso es lo que se lee
   * como desorden, más que los números. Igualadas, el bloque tiene un solo
   * borde derecho y se lee como una etiqueta de promo, no como tres apuntes.
   *
   * Se consigue con `alignItems: 'stretch'`: el contenedor está posicionado en
   * absoluto y sólo lleva `left`, así que se encoge al contenido (lo ancho de
   * la línea más larga) y las cajas lo llenan. No hace falta medir en JS.
   */
  igualarAncho?: boolean;
}> = ({lineas, lado = 'izquierda', abajo = 96, igualarAncho = false}) => (
  <div
    style={{
      position: 'absolute',
      /**
       * ⛔ BUG CORREGIDO EL 02-09-2026. Acá decía `[lado]: ...`, y `lado` vale
       * «izquierda» o «derecha» — que NO son propiedades CSS. La clave
       * calculada salía `izquierda: 84`, React la ignoraba y la caja se quedaba
       * SIN desplazamiento: pegada al borde del lienzo en x=0, cortada.
       *
       * Lo cazó el QA en `BW ST 01-09 Promo To Go`, que ya estaba ENTREGADA: sus
       * dos cajas de promo sangraban por el borde izquierdo y la tinta arrancaba
       * a 22 px del canto, contra los 84 de margen. Afecta a toda pieza con
       * `PilaEsquina` — también a las slides 2, 3 y 4 del carrusel To Go.
       */
      [lado === 'derecha' ? 'right' : 'left']: BETWEEN.bloque.margenX,
      bottom: abajo,
      display: 'flex',
      flexDirection: 'column',
      alignItems: igualarAncho
        ? 'stretch'
        : lado === 'izquierda' ? 'flex-start' : 'flex-end',
      gap: 6,
    }}
  >
    {lineas.map((l, i) => (
      <div
        key={i}
        style={{
          backgroundColor: BETWEEN.cajas.fondo,
          borderRadius: 6,
          padding: '10px 20px',
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: l.fuerte ? BETWEEN.pesos.extrabold : 500,
          fontSize: l.fuerte ? 46 : 40,
          lineHeight: 1.1,
          color: BETWEEN.colores.beige,
          whiteSpace: 'nowrap',
        }}
      >
        {/* ⭐ 01-09-2026, Eli: «los precios debes hacer que se vean opentype
            tabular, como en adobe illustrator, así los números no se ven
            desordenados». Acá caen los tres precios del carrusel To Go
            ($4.290 · $3.790 · $5.290). El CSS `tnum` que había antes NO servía
            —Raleway no trae la función—; ver `cifrasTabulares` en
            BetweenSistema.tsx, que construye la caja tabular a mano.

            ⭐⭐ 02-09-2026 — VUELVE, pedido de nuevo por Eli: «para los precios y
            textos usa Opentype tabular como en Adobe Illustrator, ya que los
            números se ven extraños y desordenados. Esto para las grillas».

            Se había retirado el 01-09 porque Eli lo rechazó al verlo rendido, y
            el motivo estaba medido: el «1» de Raleway es 18,5 % más angosto que
            el «0», así que centrado en la caja tabular quedaba flotando con un
            hueco a cada lado y «10:00» se leía como palabra partida.

            ⭐⭐⭐ 5.ª pasada, y acá quedó BIEN — en las DOS líneas.

            En la 4.ª se había sacado la tabular de la línea liviana, porque el
            hueco de la caja del «1» se sumaba al espacio anterior y en «a 10:00»
            se veía un espacio doble. Eli lo devolvió igual, señalando esta misma
            story: «esta de acá no está con el texto tabular y los números se ven
            extraños». Tenía razón: sacarla era esquivar el problema, no
            resolverlo — y en el brief de la pieza los números van APILADOS
            («Café + dulce / desde $3.790» y «Lunes a viernes / 08:00 a 10:00
            hrs.»), o sea justo el caso en que la tabular tiene que estar.

            El defecto se arregló de raíz en `cifrasTabulares`: ahora agrupa los
            dígitos consecutivos y **descuenta el hueco en los dos bordes del
            grupo** con un margen negativo, así que el grupo queda a ras del
            texto que lo rodea y el hueco se reparte sólo por DENTRO, entre
            cifras, donde se lee como espaciado normal (~1 px a cuerpo 40).
            Por eso hay que pasarle el PESO: el descuento se calcula con el
            ancho real de cada dígito, y el «1» va de 450/1000 en Medium a
            518 en ExtraBold. */}
        {conCifras(l.texto, l.fuerte ? BETWEEN.pesos.extrabold : 500)}
      </div>
    ))}
  </div>
);
