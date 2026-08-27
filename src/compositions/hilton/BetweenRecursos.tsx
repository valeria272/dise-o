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

export const BurbujaChat: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      background: 'rgba(103,91,73,0.93)',
      color: '#fff',
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: 600,
      fontSize: 31,
      lineHeight: 1.3,
      padding: '18px 26px',
      borderRadius: 16,
      marginBottom: 18,
      maxWidth: 560,
      alignSelf: 'flex-end',
    }}
  >
    • {children}
  </div>
);

export const MarcoIGPost: React.FC<{
  usuario?: string;
  foto: React.ReactNode;
  burbujas?: string[];
  notaLegal?: string;
  ancho?: number;
}> = ({usuario = 'between.coffeebar', foto, burbujas = [], notaLegal, ancho = 860}) => (
  <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
    <div
      style={{
        width: ancho,
        background: BETWEEN.colores.beige,
        borderRadius: 8,
        padding: '22px 26px',
        boxShadow: '0 24px 60px rgba(0,0,0,0.35)',
      }}
    >
      {/* header */}
      <div style={{display: 'flex', alignItems: 'center', gap: 18, marginBottom: 20}}>
        <div
          style={{
            width: 62, height: 62, borderRadius: '50%',
            border: '2px solid #7a6a58',
            background: '#fff',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: BETWEEN.fuentes.sans, fontSize: 10, fontWeight: 800,
            color: '#3b2f24', letterSpacing: 1,
          }}
        >
          B∃TW
        </div>
        <div style={{fontFamily: BETWEEN.fuentes.sans, fontWeight: 800, fontSize: 34, color: '#3b2f24'}}>
          {usuario}
        </div>
        <div style={{marginLeft: 'auto', fontSize: 34, color: '#3b2f24', letterSpacing: 2}}>•••</div>
      </div>
      {/* foto con burbujas encima */}
      <div style={{position: 'relative', borderRadius: 4, overflow: 'hidden'}}>
        {foto}
        <div
          style={{
            position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column',
            justifyContent: 'center', alignItems: 'flex-end', padding: '20px 22px',
          }}
        >
          {burbujas.map((b) => (
            <BurbujaChat key={b}>{b}</BurbujaChat>
          ))}
        </div>
      </div>
      {/* footer */}
      <div style={{display: 'flex', alignItems: 'center', gap: 24, marginTop: 20, color: '#3b2f24'}}>
        <span style={{fontSize: 40, color: '#e0443a'}}>♥</span>
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
      <div style={{fontFamily: BETWEEN.fuentes.sans, fontWeight: 800, fontSize: 30, color: '#3b2f24', marginTop: 14}}>
        {usuario}
      </div>
    </div>
    {notaLegal ? (
      <div
        style={{
          fontFamily: BETWEEN.fuentes.sans, fontStyle: 'italic', fontWeight: 500,
          fontSize: 27, color: '#fff', textAlign: 'center', marginTop: 30,
          maxWidth: 820, lineHeight: 1.45, textShadow: '0 2px 14px rgba(0,0,0,0.6)',
        }}
      >
        {notaLegal}
      </div>
    ) : null}
  </div>
);

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
}> = ({pregunta, opciones, correcta, ancho = 660}) => (
  <div
    style={{
      width: ancho,
      background: '#ffffff',
      borderRadius: 22,
      padding: '26px 24px 22px',
      boxShadow: '0 18px 44px rgba(36,26,18,0.32)',
      display: 'flex',
      flexDirection: 'column',
      gap: 14,
    }}
  >
    <div
      style={{
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: 700,
        fontSize: 32,
        color: '#1a1a1a',
        textAlign: 'center',
        lineHeight: 1.25,
      }}
    >
      {pregunta}
    </div>
    {opciones.map((o, i) => (
      <div
        key={o}
        style={{
          fontFamily: BETWEEN.fuentes.sans,
          fontWeight: i === correcta ? 700 : 500,
          fontSize: 29,
          color: i === correcta ? BETWEEN.colores.beige : '#2b2b2b',
          background: i === correcta ? BETWEEN.colores.cafe : '#f1ede5',
          borderRadius: 14,
          padding: '15px 22px',
          textAlign: 'center',
        }}
      >
        {o}
      </div>
    ))}
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
 * Pila de cajas taupe anclada ABAJO A LA IZQUIERDA, como en «Promo ToGo /
 * Café grande + Sándwich $4.290». Alternativa al bloque centrado.
 */
export const PilaEsquina: React.FC<{
  lineas: {texto: string; fuerte?: boolean}[];
  lado?: 'izquierda' | 'derecha';
  abajo?: number;
}> = ({lineas, lado = 'izquierda', abajo = 96}) => (
  <div
    style={{
      position: 'absolute',
      [lado]: BETWEEN.bloque.margenX,
      bottom: abajo,
      display: 'flex',
      flexDirection: 'column',
      alignItems: lado === 'izquierda' ? 'flex-start' : 'flex-end',
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
        {l.texto}
      </div>
    ))}
  </div>
);
