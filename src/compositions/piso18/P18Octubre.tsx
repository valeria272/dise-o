/**
 * PISO18 — GRILLA OCTUBRE 2026 · las 11 piezas en OK PARA DISEÑAR al 28-09
 *
 * Encargo de Eli, 28-09-2026: «diseñando la grilla de piso18 que esté okey para
 * diseñar feed y stories, guíate de las referencias, que sea muy igual solo que
 * con la identidad visual de PISO18».
 *
 * Grilla `PISO18 GRILLA OCTUBRE 2026` (`1bzTQWrTYPoSFwy2iIYCxTKuO-1XNbqT7Nk_vQz39JQA`),
 * leída en vivo el 28-09 (igual a `clients/hilton/grillas/api/p18-oct-20260928.json`).
 * Referencias en `raw/hilton/piso18/oct/refs/` (`scripts/p18-oct-refs.py`).
 * Fotos al tamaño de entrega con su caja de recorte: `scripts/p18-oct-fotos.py`.
 *
 * | id | pieza | referencia que se calca |
 * |---|---|---|
 * | P18O-F0610 | FEED 06-10 post arreglos | centro de mesa en primer plano, sin texto |
 * | P18O-F0910-1/2 | FEED 09-10 carrusel fechas 2027 | S2: papel + titular + calendario con el día encerrado |
 * | P18O-F1310-1/2 | FEED 13-10 carrusel atardecer | S2: versales chicas + palabra gigante en itálica abajo |
 * | P18O-F1610-1…5 | FEED 16-10 carrusel celebraciones | collage 2×2 con la hoja de papel y el clip al centro |
 * | P18O-F2310-1…4 | FEED 23-10 carrusel Tex-Mex | el post propio «Estación de trinchado» |
 * | P18O-F2710 | FEED 27-10 post wedding planner | la foto de la ref, «sin texto ni cuadro, dejar logo» |
 * | P18O-S0510 | ST 05-10 animada primavera | titular a la izquierda arriba sobre mesa florida |
 * | P18O-S0710 | ST 07-10 estación favorita | «This / That»: dos polaroids, rótulos calados y flechas |
 * | P18O-S0910 | ST 09-10 recuerdos | nota de papel con cintas sobre la foto |
 * | P18O-S2310 | ST 23-10 corporativo | cuadro de vidrio sobre el salón |
 * | P18O-S2710 | ST 27-10 visita virtual | la ST de recorrido anterior: dos teléfonos |
 *
 * ⛔ Piso18 es marca propia (R-02). Sin «bodas» (R-01). Sin punto en títulos ni
 * bajadas (R-24). El fucsia sólo en lo que se quiere que el ojo pegue (R-03).
 * La interacción no se dibuja: se deja el aire y el sticker lo pone el CM (R-11).
 */
import React from 'react';
import {
  AbsoluteFill,
  Img,
  OffthreadVideo,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  Easing,
} from 'remotion';
import {P18, cargarFuentesP18, GranoFondo} from '../../brand/piso18';

const W = 1080;
const FEED_H = 1350;
const STORY_H = 1920;
const SOMBRA = '0 2px 30px rgba(0,0,0,0.38)';
const oct = (f: string) => staticFile(`assets/hilton/piso18/oct/${f}`);

/**
 * ⭐ Raleway SIEMPRE con cifras de caja alta. Sus cifras por defecto son de estilo
 * antiguo: el 3, 5, 7 y 9 bajan de la línea base y el 0 queda a media altura, y eso
 * es lo que Eli vio como «los números se ven desequilibrados y extraños» (ronda 1,
 * 28-09: «2027», «piso18.cl», «EN PISO18»). Memoria `raleway-no-tiene-tabulares`.
 */
const RALEWAY: React.CSSProperties = {fontFamily: P18.fuentes.texto, fontFeatureSettings: '"lnum" 1'};

// ───────────────────────────────────────────────────────────────────────────
// Piezas comunes
// ───────────────────────────────────────────────────────────────────────────
const Foto: React.FC<{src: string; style?: React.CSSProperties}> = ({src, style}) => (
  <Img src={oct(src)} style={{width: '100%', height: '100%', objectFit: 'cover', ...style}} />
);

/** Logotipo completo, arriba y centrado, sin deformar (R-12). `oscuro` = sobre papel. */
const Logo: React.FC<{top: number; ancho?: number; oscuro?: boolean}> = ({
  top,
  ancho = P18.geometria.logoAncho,
  oscuro,
}) => (
  <Img
    src={staticFile('assets/hilton/piso18/logo.png')}
    style={{
      position: 'absolute',
      width: ancho,
      height: ancho / P18.geometria.logoProporcion,
      left: (W - ancho) / 2,
      top,
      // sobre papel el logotipo va en la tinta de la marca, no en negro puro
      filter: oscuro ? 'brightness(0) opacity(0.88)' : undefined,
    }}
  />
);

/** Velo superior de marca (R-14): alfa 0,588 arriba → 0 al 41,7 % del alto. */
const VeloArriba: React.FC<{alfa?: number; hasta?: number}> = ({alfa = 0.588, hasta = 41.7}) => (
  <AbsoluteFill
    style={{
      background: `linear-gradient(to bottom, rgba(8,8,10,${alfa}) 0%, rgba(8,8,10,${
        alfa * 0.45
      }) ${hasta * 0.55}%, rgba(8,8,10,0) ${hasta}%)`,
    }}
  />
);

/** Velo inferior en degradado, el que sostiene el texto blanco (mismo de C1 S5). */
const VeloPie: React.FC<{hasta?: number; opacidad?: number}> = ({hasta = 0.6, opacidad = 0.82}) => (
  <AbsoluteFill
    style={{
      background: `linear-gradient(to top, rgba(8,8,10,${opacidad}) 0%, rgba(8,8,10,${
        opacidad * 0.72
      }) ${hasta * 32}%, rgba(8,8,10,${opacidad * 0.3}) ${hasta * 66}%, rgba(8,8,10,0) ${
        hasta * 100
      }%)`,
    }}
  />
);

/** Botón de historia: sólo los dos esquemas de la marca (R-10). */
const Boton: React.FC<{top: number; children: React.ReactNode; invertido?: boolean}> = ({
  top,
  children,
  invertido,
}) => {
  const e = invertido ? P18.botones.invertido : P18.botones.lleno;
  return (
    <div style={{position: 'absolute', left: 0, right: 0, top, display: 'flex', justifyContent: 'center'}}>
      <div
        style={{
          backgroundColor: e.fondo,
          color: e.texto,
          ...RALEWAY,
          fontWeight: 700,
          fontSize: 33,
          letterSpacing: 0.6,
          padding: '26px 58px',
          borderRadius: 999,
          whiteSpace: 'nowrap',
          boxShadow: '0 6px 26px rgba(26,16,10,0.34)',
        }}
      >
        {children}
      </div>
    </div>
  );
};

/** Cierre de feed y de historias con sticker: la LÍNEA, no la píldora (R-40). */
const LineaCotiza: React.FC<{top: number; texto?: string; tinta?: string; sombra?: boolean; cuerpo?: number}> = ({
  top,
  texto = 'Cotiza tu evento en',
  tinta = P18.colores.blanco,
  sombra = true,
  cuerpo = 28,
}) => (
  <div
    style={{
      position: 'absolute',
      left: 0,
      right: 0,
      top,
      textAlign: 'center',
      ...RALEWAY,
      fontWeight: 700,
      fontSize: cuerpo,
      letterSpacing: 0.3,
      color: tinta,
      textShadow: sombra ? SOMBRA : undefined,
    }}
  >
    {texto} <span style={{color: P18.colores.fucsia}}>piso18.cl</span>
  </div>
);

/**
 * Papel beige con fibra (pedido de Eli en la S4: «al fondo beige añade textura de
 * papel sutil beige»). Nunca beige sobre la tarjeta casi blanca (R-05).
 */
const PapelBeige: React.FC<{semilla?: number}> = ({semilla = 3}) => (
  <AbsoluteFill style={{backgroundColor: P18.colores.beige}}>
    <svg width="100%" height="100%" style={{position: 'absolute', inset: 0}} preserveAspectRatio="none">
      <filter id={`p18o-papel-${semilla}`}>
        <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves={3} seed={semilla} />
        <feColorMatrix type="saturate" values="0" />
      </filter>
      <filter id={`p18o-veta-${semilla}`}>
        <feTurbulence type="fractalNoise" baseFrequency="0.004 0.018" numOctaves={3} seed={semilla + 7} />
        <feColorMatrix type="saturate" values="0" />
      </filter>
      <rect width="100%" height="100%" filter={`url(#p18o-papel-${semilla})`} opacity={0.16} style={{mixBlendMode: 'multiply'}} />
      <rect width="100%" height="100%" filter={`url(#p18o-veta-${semilla})`} opacity={0.1} style={{mixBlendMode: 'multiply'}} />
    </svg>
  </AbsoluteFill>
);

/**
 * Clip de archivador de la hoja (ref del 16-10). Ronda 1, Eli 28-09: «las cositas de
 * archivadora en el color fucsia de piso 18, esos pinchitos que se vean un poco
 * mejor» ⇒ cuerpo en `#D4145A` con el pliegue un tono más hondo y un brillo de metal
 * pintado; las patas, alambre plateado con luz y sombra.
 */
const Clip: React.FC<{x: number; y: number; escala?: number}> = ({x, y, escala = 1}) => (
  <svg
    width={76 * escala}
    height={104 * escala}
    viewBox="0 0 76 104"
    style={{position: 'absolute', left: x, top: y, filter: 'drop-shadow(0 5px 7px rgba(0,0,0,0.38))'}}
  >
    <defs>
      <linearGradient id="p18o-clip-cuerpo" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0" stopColor="#A80F47" />
        <stop offset="0.22" stopColor={P18.colores.fucsia} />
        <stop offset="0.5" stopColor="#E8457F" />
        <stop offset="0.78" stopColor={P18.colores.fucsia} />
        <stop offset="1" stopColor="#A80F47" />
      </linearGradient>
      <linearGradient id="p18o-clip-alambre" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0" stopColor="#8E8E96" />
        <stop offset="0.45" stopColor="#F2F2F4" />
        <stop offset="1" stopColor="#9A9AA2" />
      </linearGradient>
    </defs>
    {/* las dos patas de alambre, plegadas hacia atrás */}
    <path d="M24 50 C 16 24, 20 7, 32 7 C 43 7, 45 24, 38 50" fill="none" stroke="#6E6E76" strokeWidth={5.2} strokeLinecap="round" />
    <path d="M24 50 C 16 24, 20 7, 32 7 C 43 7, 45 24, 38 50" fill="none" stroke="url(#p18o-clip-alambre)" strokeWidth={3.4} strokeLinecap="round" />
    <path d="M38 50 C 31 26, 35 12, 46 12 C 57 12, 59 26, 52 50" fill="none" stroke="#6E6E76" strokeWidth={5.2} strokeLinecap="round" />
    <path d="M38 50 C 31 26, 35 12, 46 12 C 57 12, 59 26, 52 50" fill="none" stroke="url(#p18o-clip-alambre)" strokeWidth={3.4} strokeLinecap="round" />
    {/* el cuerpo: trapecio con los cantos apenas redondeados */}
    <path d="M10 48 Q10 46 12 46 L64 46 Q66 46 66 48 L71 98 Q71 101 68 101 L8 101 Q5 101 5 98 Z" fill="url(#p18o-clip-cuerpo)" />
    {/* el pliegue de arriba y el filo inferior */}
    <path d="M12 46 L64 46 Q66 46 66 48 L65 57 L11 57 L10 48 Q10 46 12 46 Z" fill="#9E0D42" />
    <path d="M13 50 L63 50" stroke="rgba(255,255,255,0.35)" strokeWidth={1.4} />
    <path d="M6 97 L70 97" stroke="rgba(0,0,0,0.22)" strokeWidth={2} />
  </svg>
);

/** Hoja de papel con otras dos debajo, como el fajo de la referencia. */
const HojaPapel: React.FC<{
  left: number;
  top: number;
  ancho: number;
  alto: number;
  giro?: number;
  fajo?: boolean;
  children: React.ReactNode;
}> = ({left, top, ancho, alto, giro = 0, fajo = true, children}) => (
  <div style={{position: 'absolute', left, top, width: ancho, height: alto, transform: `rotate(${giro}deg)`}}>
    {fajo && (
      <>
        <div style={{position: 'absolute', inset: 0, transform: 'translate(10px, 14px) rotate(1.6deg)', backgroundColor: '#ECEAE6', boxShadow: '0 10px 30px rgba(0,0,0,0.30)'}} />
        <div style={{position: 'absolute', inset: 0, transform: 'translate(-6px, 8px) rotate(-1.2deg)', backgroundColor: '#F1EFEB', boxShadow: '0 6px 18px rgba(0,0,0,0.22)'}} />
      </>
    )}
    <div
      style={{
        position: 'absolute',
        inset: 0,
        backgroundColor: P18.colores.tarjeta,
        boxShadow: '0 14px 40px rgba(0,0,0,0.34)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        textAlign: 'center',
        color: P18.colores.tinta,
      }}
    >
      {children}
    </div>
  </div>
);

// ═══════════════════════════════════════════════════════════════════════════
// FEED 06-10 · POST «ARREGLOS FLORALES DE PRIMAVERA» — Texto: sin texto
// ═══════════════════════════════════════════════════════════════════════════
/**
 * Ref (pin 99712579247992360): un centro de mesa en primer plano, vertical, sin
 * texto ni logo. Foto real `piso_18-7` (deco ago-2024): el arreglo con rosas
 * terracota, follaje oliva y la vela, que es exactamente la paleta del brief
 * («verde oliva, terracota y joya»). Sin logotipo: la ref no lo trae y Eli ya
 * pidió portadas limpias («bórrale el logo, muy repetitivo», 15-09).
 */
export const P18OF0610: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
    <Foto src="f0610.jpg" />
  </AbsoluteFill>
);

// ═══════════════════════════════════════════════════════════════════════════
// FEED 09-10 · CARRUSEL «FECHAS 2027 EN TEMPORADA ALTA»
// ═══════════════════════════════════════════════════════════════════════════
/** S1 · panorámica del salón ambientado para matrimonio. Sin texto. */
export const P18OF0910S1: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
    <Foto src="f0910-1.jpg" />
  </AbsoluteFill>
);

/**
 * S2 · «Las grandes historias se planean con tiempo. Asegura tu fecha 2027»
 *
 * Ref (pin 807129564520273185, «Makers Market»): papel claro, una línea chica en
 * versales, un titular a dos voces (palo seco rojo + script encima), una fecha
 * y, abajo, un calendario de tres días con el del medio encerrado a mano.
 * Traducido a Piso18: el papel es el beige de la marca con fibra; las dos voces
 * son las de su titular (itálica fina + VERSALES, R-06) y el rojo pasa al fucsia
 * en la línea que se quiere que el ojo pegue. El calendario es un fin de semana
 * real de la temporada alta 2027: viernes 15, sábado 16 y domingo 17 de enero
 * (el 1-1-2027 cae viernes), con el sábado encerrado en fucsia.
 */
export const P18OF0910S2: React.FC = () => {
  cargarFuentesP18();
  const lineaCal = 'rgba(26,26,26,0.42)';
  const colX = [60, 380, 700, 1020];
  const topCal = 820;
  return (
    <AbsoluteFill>
      <PapelBeige semilla={9} />
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 186,
          textAlign: 'center',
          ...RALEWAY,
          fontWeight: 700,
          fontSize: 26,
          letterSpacing: 7,
          textIndent: 7,
          color: P18.colores.tinta,
        }}
      >
        TEMPORADA ALTA 2027
      </div>
      <div style={{position: 'absolute', left: 40, right: 40, top: 272, textAlign: 'center', fontFamily: P18.fuentes.titular, color: P18.colores.tinta}}>
        <div style={{fontSize: 118, fontWeight: 300, fontStyle: 'italic', lineHeight: 1.04}}>
          Las grandes historias
        </div>
        <div style={{fontSize: 80, fontWeight: 400, lineHeight: 1.2, letterSpacing: 1.5, color: P18.colores.fucsia}}>
          SE PLANEAN CON TIEMPO
        </div>
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 590,
          textAlign: 'center',
          ...RALEWAY,
          fontWeight: 500,
          fontSize: 40,
          letterSpacing: 1.2,
          color: P18.colores.tinta,
        }}
      >
        Asegura tu fecha 2027
      </div>

      {/* ── el calendario, a sangre por abajo como en la ref ───────────── */}
      <svg width={W} height={FEED_H} style={{position: 'absolute', inset: 0}}>
        <line x1={0} y1={topCal} x2={W} y2={topCal} stroke={lineaCal} strokeWidth={2} />
        <line x1={0} y1={topCal + 76} x2={W} y2={topCal + 76} stroke={lineaCal} strokeWidth={2} />
        {colX.map((x) => (
          <line key={x} x1={x} y1={topCal} x2={x} y2={FEED_H} stroke={lineaCal} strokeWidth={2} />
        ))}
      </svg>
      {['VIERNES', 'SÁBADO', 'DOMINGO'].map((d, i) => (
        <div
          key={d}
          style={{
            position: 'absolute',
            left: colX[i],
            width: colX[i + 1] - colX[i],
            top: topCal + 22,
            textAlign: 'center',
            ...RALEWAY,
            fontWeight: 500,
            fontSize: 28,
            letterSpacing: 2,
            textIndent: 2,
            color: P18.colores.tinta,
          }}
        >
          {d}
        </div>
      ))}
      {['15', '16', '17'].map((n, i) => (
        <div
          key={n}
          style={{
            position: 'absolute',
            left: colX[i],
            width: colX[i + 1] - colX[i],
            top: topCal + 112,
            textAlign: 'center',
            fontFamily: P18.fuentes.titular,
            // Thin: las cifras de la ref son finas; en Light pesaban más que todo el bloque
            fontWeight: 100,
            fontSize: 236,
            lineHeight: 1,
            color: P18.colores.tinta,
          }}
        >
          {n}
        </div>
      ))}
      {/* El círculo a mano: dos vueltas que no cierran igual, como un plumón. */}
      <svg width={W} height={FEED_H} style={{position: 'absolute', inset: 0}}>
        <path
          d="M 700 1028 C 706 940, 610 916, 540 920 C 450 924, 380 970, 386 1052 C 392 1140, 470 1180, 548 1178 C 640 1176, 712 1126, 706 1042 C 702 990, 668 950, 600 934"
          fill="none"
          stroke={P18.colores.fucsia}
          strokeWidth={6}
          strokeLinecap="round"
        />
        <path
          d="M 690 1050 C 700 970, 620 930, 548 930 C 470 932, 398 980, 398 1050"
          fill="none"
          stroke={P18.colores.fucsia}
          strokeWidth={3.2}
          strokeLinecap="round"
          opacity={0.8}
        />
      </svg>
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════════
// FEED 13-10 · CARRUSEL «ATARDECER DESDE PISO18»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * S1 · el ventanal real de Piso18 (banq `0003`) reiluminado a la hora dorada con
 * Nano Banana Pro: en ninguna sesión hay un atardecer (ya lo anotó `P18StLuzVista`).
 */
export const P18OF1310S1: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
    <Foto src="f1310-1.jpg" />
  </AbsoluteFill>
);

/**
 * S2 · «Escribe tu historia de amor con esta vista»
 * Ref (pin 1096908053015943345, «un recuerdo eterno»): arriba una línea fina de
 * llamado con flechas; abajo versales chicas muy espaciadas, una palabra gigante
 * en itálica que casi toca los bordes y la firma debajo. Acá la palabra gigante
 * es «con esta vista» en IvyPresto itálica, la línea de arriba es el cotiza de la
 * cuenta y la firma es el logotipo.
 */
export const P18OF1310S2: React.FC = () => {
  cargarFuentesP18();
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Foto src="f1310-2.jpg" />
      <VeloArriba alfa={0.42} hasta={16} />
      <VeloPie hasta={0.55} opacidad={0.78} />
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 62,
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          gap: 18,
          color: P18.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        <span style={{fontFamily: P18.fuentes.titular, fontStyle: 'italic', fontWeight: 300, fontSize: 30}}>
          Cotiza tu evento
        </span>
        <svg width={110} height={14} viewBox="0 0 110 14">
          <line x1={0} y1={7} x2={104} y2={7} stroke="#FFFFFF" strokeWidth={1.6} />
          <path d="M97 1 L105 7 L97 13" fill="none" stroke="#FFFFFF" strokeWidth={1.6} />
        </svg>
        <span style={{...RALEWAY, fontWeight: 700, fontSize: 21, letterSpacing: 4}}>
          PISO18.CL
        </span>
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 880,
          textAlign: 'center',
          ...RALEWAY,
          fontWeight: 700,
          fontSize: 25,
          letterSpacing: 9,
          textIndent: 9,
          color: P18.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        ESCRIBE TU HISTORIA DE AMOR
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 912,
          textAlign: 'center',
          fontFamily: P18.fuentes.titular,
          fontStyle: 'italic',
          fontWeight: 300,
          fontSize: 186,
          lineHeight: 1.08,
          letterSpacing: -2,
          color: P18.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        con esta vista
      </div>
      <Logo top={1166} ancho={200} />
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════════
// FEED 16-10 · CARRUSEL «TU PRÓXIMA CELEBRACIÓN EN PISO18»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * Ref (pin 723812971449850107, «Event archive»): cuatro fotos a sangre en 2×2,
 * sin separación, y al centro un fajo de hojas blancas sujeto con un clip negro,
 * con una línea chica en itálica, el titular grande en versales y una línea mini
 * de cierre. Es la ref que dejó Scarlette cuando pidió armar el carrusel con
 * todos los tipos de evento. La hoja se repite chica en las slides siguientes
 * con el nombre de cada evento, para que el carrusel se lea como un archivo.
 *
 * Cuadros: salón de noche (banq 0044) · barra de tragos (julio evento 103) ·
 * mesa larga de matrimonio (banq 0047) · lounge (banq 0019). Todos reales.
 */
export const P18OF1610S1: React.FC = () => {
  cargarFuentesP18();
  const cuadros = ['f1610-c1.jpg', 'f1610-c2.jpg', 'f1610-c3.jpg', 'f1610-c4.jpg'];
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      {cuadros.map((c, i) => (
        <div
          key={c}
          style={{
            position: 'absolute',
            left: (i % 2) * (W / 2),
            top: Math.floor(i / 2) * (FEED_H / 2),
            width: W / 2,
            height: FEED_H / 2,
            overflow: 'hidden',
          }}
        >
          <Foto src={c} />
        </div>
      ))}
      <HojaPapel left={250} top={430} ancho={580} alto={470} giro={-1.2}>
        <div style={{fontFamily: P18.fuentes.titular, fontStyle: 'italic', fontWeight: 300, fontSize: 46, lineHeight: 1}}>
          Cada celebración
        </div>
        <div style={{fontFamily: P18.fuentes.titular, fontWeight: 400, fontSize: 84, lineHeight: 0.98, marginTop: 20, letterSpacing: 0.5}}>
          ENCUENTRA
          <br />
          SU LUGAR
        </div>
        <div style={{...RALEWAY, fontWeight: 700, fontSize: 24, letterSpacing: 6, textIndent: 6, marginTop: 28}}>
          EN PISO18
        </div>
      </HojaPapel>
      <Clip x={296} y={384} escala={1.15} />
    </AbsoluteFill>
  );
};

/** Slides 2 a 4: la foto del tipo de evento y su hoja con el nombre. */
const SlideEvento: React.FC<{foto: string; nombre: string; giro: number}> = ({foto, nombre, giro}) => {
  cargarFuentesP18();
  const ancho = nombre.length > 12 ? 640 : 480;
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Foto src={foto} />
      <VeloPie hasta={0.38} opacidad={0.5} />
      <HojaPapel left={(W - ancho) / 2} top={1040} ancho={ancho} alto={170} giro={giro} fajo={false}>
        <div style={{fontFamily: P18.fuentes.titular, fontStyle: 'italic', fontWeight: 300, fontSize: 70, lineHeight: 1}}>
          {nombre}
        </div>
      </HojaPapel>
      <Clip x={(W - ancho) / 2 + 40} y={998} />
    </AbsoluteFill>
  );
};

export const P18OF1610S2: React.FC = () => <SlideEvento foto="f1610-2.jpg" nombre="Matrimonios" giro={-1} />;
export const P18OF1610S3: React.FC = () => <SlideEvento foto="f1610-3.jpg" nombre="Cumpleaños" giro={1.1} />;
export const P18OF1610S4: React.FC = () => (
  <SlideEvento foto="f1610-4.jpg" nombre="Eventos corporativos" giro={-0.8} />
);

/** S5 · cierre: la lámpara cálida (deco `piso_18-26`) y la hoja con el llamado. */
export const P18OF1610S5: React.FC = () => {
  cargarFuentesP18();
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Foto src="f1610-5.jpg" />
      <VeloPie hasta={0.62} opacidad={0.84} />
      <HojaPapel left={150} top={800} ancho={780} alto={290} giro={-0.8}>
        <div style={{fontFamily: P18.fuentes.titular, fontWeight: 300, fontSize: 52, lineHeight: 1.1}}>
          Reserva ahora tu fecha
          <br />
          de diciembre
        </div>
        <div style={{fontFamily: P18.fuentes.titular, fontStyle: 'italic', fontWeight: 400, fontSize: 56, lineHeight: 1.1, marginTop: 6, color: P18.colores.fucsia}}>
          y celebra a tu manera
        </div>
      </HojaPapel>
      <Clip x={196} y={756} escala={1.1} />
      <LineaCotiza top={1156} cuerpo={34} />
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════════
// FEED 23-10 · CARRUSEL «ESTACIÓN TEX-MEX»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * Ref (instagram.com/p/Dc_mQ4kEUA4): el carrusel PROPIO de Piso18 «Estación de
 * trinchado». Se calca su portada tal cual: logotipo centrado, «Estación» enorme
 * en IvyPresto, el apellido en versales Raleway debajo y «Desliza» con su
 * flecha al pie. Las slides 2 a 4 van sin texto, como el brief.
 * Las cuatro fotos se PRODUCEN (Seedream 5 Pro sobre el buffet real banq 0052):
 * no hay una estación Tex-Mex en ninguna sesión.
 */
export const P18OF2310S1: React.FC = () => {
  cargarFuentesP18();
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Foto src="f2310-1.jpg" />
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to bottom, rgba(8,8,10,0.55) 0%, rgba(8,8,10,0.40) 38%, rgba(8,8,10,0.05) 60%, rgba(8,8,10,0.10) 76%, rgba(8,8,10,0.78) 100%)',
        }}
      />
      <Logo top={250} ancho={250} />
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 362,
          textAlign: 'center',
          fontFamily: P18.fuentes.titular,
          fontWeight: 400,
          fontSize: 196,
          lineHeight: 1,
          color: P18.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        Estación
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 574,
          textAlign: 'center',
          ...RALEWAY,
          fontWeight: 700,
          fontSize: 54,
          letterSpacing: 4,
          textIndent: 4,
          color: P18.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        TEX MEX
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 1228,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: 6,
          color: P18.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        <svg width={86} height={14} viewBox="0 0 86 14">
          <line x1={0} y1={7} x2={80} y2={7} stroke="#FFFFFF" strokeWidth={2} />
          <path d="M73 1 L81 7 L73 13" fill="none" stroke="#FFFFFF" strokeWidth={2} />
        </svg>
        <span style={{fontFamily: P18.fuentes.titular, fontStyle: 'italic', fontWeight: 300, fontSize: 40}}>
          Desliza
        </span>
      </div>
    </AbsoluteFill>
  );
};

const SoloFoto: React.FC<{src: string}> = ({src}) => (
  <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
    <Foto src={src} />
  </AbsoluteFill>
);
export const P18OF2310S2: React.FC = () => <SoloFoto src="f2310-2.jpg" />;
export const P18OF2310S3: React.FC = () => <SoloFoto src="f2310-3.jpg" />;
export const P18OF2310S4: React.FC = () => <SoloFoto src="f2310-4.jpg" />;

// ═══════════════════════════════════════════════════════════════════════════
// FEED 27-10 · POST «WEDDING PLANNER PISO18»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * La celda de la ref dice, literal: «REF DE FOTO, SIN TEXTO NI CUADRO, DEJAR
 * LOGO PISO18». Manda sobre el campo «Texto» del brief (“Tu matrimonio, sin
 * complicaciones.”), que queda para el copy. ⇒ foto + logotipo, nada más.
 * La foto se PRODUCE (Seedream 5 Pro sobre la mesa real banq 0047): una planner
 * de negro ajustando un puesto, como la de la ref; una sola persona, gesto no
 * posado (R-41). El logotipo lleva el velo sutil de portada (R-14).
 */
export const P18OF2710: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
    <Foto src="f2710.jpg" />
    <VeloArriba alfa={0.5} hasta={30} />
    <Logo top={P18.geometria.logoYFeed} />
  </AbsoluteFill>
);

// ═══════════════════════════════════════════════════════════════════════════
// STORIES 05-10 · ANIMADA «PRIMAVERA EN PISO18»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * Ref texto (pin 392235448818997442, «06 wedding seating styles»): el titular a
 * la IZQUIERDA en el tercio alto, una línea grande en versales y una chica
 * debajo. Ref foto (pin 874613190144855677): mesa larga con flores de colores
 * intensos y luz cálida. El hilo de Scarlette pedía llevar lo vibrante y vegetal
 * a la ambientación del salón: la foto es la mesa real con follaje colgante,
 * esferas de vidrio y tulipanes (deco `piso_18-74`).
 * Movimiento: acercamiento lento y continuo sobre la foto (o el clip, si hay) y
 * el texto entra escalonado. Posición y contraste del botón se miden en el
 * ÚLTIMO fotograma (R-30).
 */
export const P18_S0510_DUR = 300;

export const P18OS0510: React.FC<{clip?: string}> = ({clip}) => {
  cargarFuentesP18();
  const f = useCurrentFrame();
  const {fps, durationInFrames} = useVideoConfig();
  const zoom = interpolate(f, [0, durationInFrames], [1.0, 1.09], {
    easing: Easing.inOut(Easing.sin),
  });
  const entra = (desde: number) => {
    const s = spring({frame: f - desde, fps, config: {damping: 200}, durationInFrames: 26});
    return {opacity: s, transform: `translateY(${(1 - s) * 34}px)`};
  };
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta, overflow: 'hidden'}}>
      <AbsoluteFill style={{transform: `scale(${zoom})`, transformOrigin: '50% 60%'}}>
        {clip ? (
          <OffthreadVideo src={oct(clip)} muted style={{width: '100%', height: '100%', objectFit: 'cover'}} />
        ) : (
          <Foto src="s0510.jpg" />
        )}
      </AbsoluteFill>
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to bottom, rgba(8,8,10,0.70) 0%, rgba(8,8,10,0.52) 22%, rgba(8,8,10,0.18) 40%, rgba(8,8,10,0) 52%, rgba(8,8,10,0) 66%, rgba(8,8,10,0.42) 100%)',
        }}
      />
      <div style={entra(4)}>
        <Logo top={P18.geometria.logoYStory} />
      </div>
      <div style={{position: 'absolute', left: 84, right: 84, top: 430, color: P18.colores.blanco, textShadow: SOMBRA}}>
        <div style={{...entra(14), fontFamily: P18.fuentes.titular, fontStyle: 'italic', fontWeight: 300, fontSize: 128, lineHeight: 1}}>
          La primavera
        </div>
        <div style={{...entra(24), fontFamily: P18.fuentes.titular, fontWeight: 400, fontSize: 66, lineHeight: 1.12, letterSpacing: 1, marginTop: 10}}>
          YA SE VIVE EN PISO18
        </div>
        <div style={{...entra(36), ...RALEWAY, fontWeight: 500, fontSize: 34, lineHeight: 1.45, marginTop: 26, maxWidth: 780}}>
          Luz natural, flores de estación y el ambiente perfecto para tu próximo evento
        </div>
      </div>
      <div style={entra(52)}>
        <Boton top={1440}>Cotiza tu evento en piso18.cl</Boton>
      </div>
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════════
// STORIES 07-10 · ENCUESTA «¿CUÁL ES TU ESTACIÓN FAVORITA EN PISO18?»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * Ref (pin 938930222333732959, «This or that»): papel claro, dos polaroids
 * giradas en diagonal, cada una con su rótulo grande CALADO («This», «That»), y
 * al medio a la izquierda el sticker con dos flechas que apuntan a cada foto.
 * Acá los rótulos son «Dulce» y «Salada» (el brief: «Estación dulce / Estación
 * salada»), calados en fucsia con IvyPresto itálica; el papel es el beige de la
 * marca. El hueco del sticker queda LIMPIO: la barra «💖» la pone el CM (R-11),
 * y las flechas salen de ese hueco. Fotos reales: postres (banq 0021) y la mesa
 * de quesos (banq 0052), del mismo evento. Cierre en línea, como la encuesta
 * aprobada de la S4.
 */
const Polaroid: React.FC<{src: string; left: number; top: number; ancho: number; giro: number}> = ({
  src,
  left,
  top,
  ancho,
  giro,
}) => (
  <div
    style={{
      position: 'absolute',
      left,
      top,
      width: ancho,
      padding: `${ancho * 0.045}px ${ancho * 0.045}px ${ancho * 0.16}px`,
      backgroundColor: '#FFFFFF',
      transform: `rotate(${giro}deg)`,
      boxShadow: '0 16px 36px rgba(40,28,14,0.28)',
    }}
  >
    <Img src={oct(src)} style={{width: '100%', aspectRatio: '1000 / 1026', objectFit: 'cover', display: 'block'}} />
  </div>
);

const Calado: React.FC<{children: React.ReactNode; style: React.CSSProperties}> = ({children, style}) => (
  <div
    style={{
      position: 'absolute',
      fontFamily: P18.fuentes.titular,
      fontStyle: 'italic',
      fontWeight: 400,
      fontSize: 140,
      lineHeight: 1,
      color: 'transparent',
      WebkitTextStroke: `2.8px ${P18.colores.fucsia}`,
      ...style,
    }}
  >
    {children}
  </div>
);

export const P18OS0710: React.FC = () => {
  cargarFuentesP18();
  return (
    <AbsoluteFill>
      <PapelBeige semilla={17} />
      {/* el logotipo dentro de los 250 px de arriba es del sistema (E-03) */}
      <Logo top={118} ancho={230} oscuro />
      <div
        style={{
          position: 'absolute',
          left: 60,
          right: 60,
          top: 244,
          textAlign: 'center',
          fontFamily: P18.fuentes.titular,
          color: P18.colores.tinta,
        }}
      >
        <div style={{fontSize: 66, fontWeight: 300, lineHeight: 1.08}}>¿Cuál es tu estación</div>
        <div style={{fontSize: 66, fontWeight: 400, fontStyle: 'italic', lineHeight: 1.08}}>
          favorita en Piso18?
        </div>
      </div>

      <Polaroid src="s0710-dulce.jpg" left={520} top={500} ancho={390} giro={4} />
      <Calado style={{left: 270, top: 410}}>Dulce</Calado>

      <Polaroid src="s0710-salada.jpg" left={560} top={1066} ancho={380} giro={-3.5} />
      <Calado style={{right: 60, top: 942, textAlign: 'right'}}>Salada</Calado>

      {/* Las flechas nacen del hueco del sticker (x 60–480 · y 830–1030). */}
      <svg width={W} height={STORY_H} style={{position: 'absolute', inset: 0}}>
        <g fill="none" stroke={P18.colores.fucsia} strokeWidth={4} strokeLinecap="round" strokeLinejoin="round">
          <path d="M 160 810 C 120 710, 260 640, 486 650" />
          <path d="M 464 634 L 490 650 L 466 670" />
          <path d="M 170 1060 C 150 1200, 310 1290, 540 1280" />
          <path d="M 518 1260 L 544 1280 L 520 1300" />
        </g>
      </svg>

      <LineaCotiza top={1528} tinta={P18.colores.tinta} sombra={false} />
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════════
// STORIES 09-10 · ENCUESTA «RECUERDOS DE MATRIMONIO»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * Ref (pin 743023638582449991, «Unpopular wedding opinions»): foto de fondo
 * apagada, título arriba en dos voces, y al centro una NOTA de papel pegada con
 * dos cintas, con la frase en serif y la encuesta adentro; al pie, una línea
 * fina y el sitio. Acá la frase es la pregunta del brief y la encuesta (La fiesta
 * / La comida / La decoración) la pega el CM en el hueco de la nota (R-11).
 * La foto es la pista real (julio evento 110) con invitados PRODUCIDOS: la pista
 * del banco está vacía y los rostros reales no se publican.
 *
 * ⚠️ El brief dice «de una matrimonio»: se corrigió a «un matrimonio».
 */
const Cinta: React.FC<{left: number; top: number; giro: number; ancho?: number}> = ({left, top, giro, ancho = 170}) => (
  <div
    style={{
      position: 'absolute',
      left,
      top,
      width: ancho,
      height: 54,
      transform: `rotate(${giro}deg)`,
      backgroundColor: 'rgba(222,205,178,0.86)',
      boxShadow: '0 2px 6px rgba(0,0,0,0.18)',
    }}
  />
);

export const P18OS0910: React.FC = () => {
  cargarFuentesP18();
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Foto src="s0910.jpg" />
      <AbsoluteFill style={{backgroundColor: 'rgba(8,8,10,0.34)'}} />
      <VeloArriba alfa={0.6} hasta={30} />
      {/* el pie morado de la pista no sostiene el fucsia de `piso18.cl`: se apaga */}
      <VeloPie hasta={0.34} opacidad={0.86} />
      <Logo top={P18.geometria.logoYStory} />
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 400,
          textAlign: 'center',
          fontFamily: P18.fuentes.titular,
          fontStyle: 'italic',
          fontWeight: 300,
          fontSize: 92,
          color: P18.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        Como invitado,
      </div>
      <div
        style={{
          position: 'absolute',
          left: 120,
          top: 580,
          width: 840,
          height: 560,
          transform: 'rotate(-1.6deg)',
          backgroundColor: P18.colores.tarjeta,
          boxShadow: '0 18px 44px rgba(0,0,0,0.40)',
        }}
      >
        <div
          style={{
            position: 'absolute',
            left: 60,
            right: 60,
            top: 70,
            textAlign: 'center',
            fontFamily: P18.fuentes.titular,
            fontWeight: 400,
            fontSize: 60,
            lineHeight: 1.14,
            color: P18.colores.tinta,
          }}
        >
          ¿qué es lo que más recuerdas de{' '}
          <span style={{fontStyle: 'italic', color: P18.colores.fucsia}}>un matrimonio?</span>
        </div>
        {/* y 300–600 de la nota: libre para la encuesta del CM */}
      </div>
      <Cinta left={820} top={556} giro={38} />
      <Cinta left={74} top={930} giro={-52} ancho={150} />
      <div style={{position: 'absolute', left: 250, right: 250, top: 1500, height: 2, backgroundColor: 'rgba(255,255,255,0.75)'}} />
      {/* El sitio va BLANCO, como el de la ref: el fucsia sobre la pista morada no se
          lee (medido en el borrador del 28-09). */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 1528,
          textAlign: 'center',
          ...RALEWAY,
          fontWeight: 700,
          fontSize: 30,
          letterSpacing: 1,
          color: P18.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        Cotiza tu evento en piso18.cl
      </div>
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════════
// STORIES 23-10 · «EVENTO CORPORATIVO FIN DE AÑO»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * Ref (pin 1096908053026703148, «Unforgettable is what we do»): foto del salón a
 * sangre y, encima, un CUADRO DE VIDRIO de esquinas redondas con el titular
 * adentro en dos cuerpos y una etiqueta blanca chica. El texto va ADENTRO del
 * cuadro (memoria `cuadro-de-vidrio-de-la-referencia`). Foto: el lounge real de
 * noche (banq 0018) montado como cóctel corporativo con mesas altas, producido
 * con Seedream 5 Pro («salón montado para evento corporativo elegante, mesas
 * altas e iluminación cálida»).
 */
export const P18OS2310: React.FC = () => {
  cargarFuentesP18();
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Foto src="s2310.jpg" />
      <AbsoluteFill style={{backgroundColor: 'rgba(8,8,10,0.18)'}} />
      <VeloArriba alfa={0.55} hasta={22} />
      <Logo top={P18.geometria.logoYStory} />
      <div
        style={{
          position: 'absolute',
          left: 90,
          top: 400,
          width: 900,
          height: 600,
          borderRadius: 58,
          border: '2px solid rgba(255,255,255,0.55)',
          background: 'linear-gradient(160deg, rgba(255,255,255,0.20) 0%, rgba(255,255,255,0.07) 55%, rgba(255,255,255,0.12) 100%)',
          backdropFilter: 'blur(5px)',
          boxShadow: '0 20px 60px rgba(0,0,0,0.25)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 130,
          right: 130,
          top: 470,
          textAlign: 'center',
          fontFamily: P18.fuentes.titular,
          color: P18.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        <div style={{fontSize: 96, fontWeight: 300, lineHeight: 1.04}}>Antes de que</div>
        <div style={{fontSize: 100, fontWeight: 400, fontStyle: 'italic', lineHeight: 1.04}}>
          termine octubre...
        </div>
      </div>
      <div
        style={{
          position: 'absolute',
          left: 180,
          right: 180,
          top: 760,
          padding: '24px 34px',
          borderRadius: 20,
          backgroundColor: 'rgba(255,255,255,0.93)',
          textAlign: 'center',
          ...RALEWAY,
          fontWeight: 500,
          fontSize: 32,
          lineHeight: 1.4,
          color: P18.colores.tinta,
          boxShadow: '0 8px 24px rgba(0,0,0,0.20)',
        }}
      >
        ¿Ya agendaste tu evento corporativo de fin de año en Piso18?
      </div>
      <Boton top={1080}>Cotiza tu evento en piso18.cl</Boton>
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════════
// STORIES 27-10 · «VISITA VIRTUAL WEB»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * «REF ANTERIOR»: la historia de recorrido virtual que ya hizo la cuenta
 * (`P18StRecorrido`, S5 sept): dos teléfonos escalonados sobre el salón
 * desaturado, con el sándwich de versales. Se repite la gramática y cambia lo
 * de adentro: la pantalla del frente es el TOUR REAL de Matterport
 * (my.matterport.com/show/?m=3yZiEXQ4Jft, capturado en headless el 28-09) y la
 * de atrás, el lounge real (banq 0001).
 * Sin botón: el CTA es «📍 Descúbrelo aquí», o sea el sticker de enlace al tour,
 * la misma excepción del cliente en la ST de recorrido (no redundar). Los
 * 300 px de abajo quedan libres para ese sticker.
 */
const TEL = {ancho: 344, alto: 746, radio: 44, marco: 11};
const Telefono: React.FC<{src: string; x: number; y: number; giro: number; rotulo: string}> = ({
  src,
  x,
  y,
  giro,
  rotulo,
}) => (
  <div
    style={{
      position: 'absolute',
      left: x,
      top: y,
      width: TEL.ancho,
      height: TEL.alto,
      transform: `rotate(${giro}deg)`,
      borderRadius: TEL.radio,
      backgroundColor: '#14141A',
      padding: TEL.marco,
      boxShadow: '0 30px 70px rgba(0,0,0,0.62), 0 0 0 1px rgba(255,255,255,0.10)',
    }}
  >
    <div style={{position: 'relative', width: '100%', height: '100%', borderRadius: TEL.radio - TEL.marco, overflow: 'hidden', backgroundColor: '#000'}}>
      <Img src={oct(src)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      <div style={{position: 'absolute', left: '50%', top: 14, transform: 'translateX(-50%)', width: 84, height: 22, borderRadius: 999, backgroundColor: '#0A0A0C'}} />
      <div style={{position: 'absolute', left: 0, right: 0, bottom: 0, height: 118, background: 'linear-gradient(to top, rgba(6,6,9,0.86) 0%, rgba(6,6,9,0) 100%)'}} />
      <div style={{position: 'absolute', left: 0, right: 0, bottom: 26, display: 'flex', justifyContent: 'center'}}>
        <div
          style={{
            flexShrink: 0,
            whiteSpace: 'nowrap',
            backgroundColor: 'rgba(255,255,255,0.94)',
            color: P18.colores.tinta,
            ...RALEWAY,
            fontWeight: 700,
            fontSize: TEL.ancho * 0.052,
            letterSpacing: 1.6,
            textIndent: 1.6,
            padding: `${TEL.ancho * 0.026}px ${TEL.ancho * 0.062}px`,
            borderRadius: 999,
          }}
        >
          {rotulo}
        </div>
      </div>
    </div>
  </div>
);

export const P18OS2710: React.FC = () => {
  cargarFuentesP18();
  const SOLAPE = 34;
  const bloqueX = (W - (TEL.ancho * 2 - SOLAPE)) / 2;
  return (
    <AbsoluteFill style={{backgroundColor: '#0C0C10'}}>
      <Foto
        src="s2710-fondo.jpg"
        style={{filter: 'grayscale(0.88) brightness(0.44) contrast(1.04) blur(7px)', transform: 'scale(1.04)'}}
      />
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to bottom, rgba(6,6,10,0.80) 0%, rgba(6,6,10,0.55) 26%, rgba(6,6,10,0.34) 48%, rgba(6,6,10,0.56) 78%, rgba(6,6,10,0.74) 100%)',
        }}
      />
      <GranoFondo semilla={43} />
      <Logo top={P18.geometria.logoYStory} />
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 392,
          textAlign: 'center',
          ...RALEWAY,
          fontWeight: 700,
          fontSize: 22,
          letterSpacing: 6.5,
          textIndent: 6.5,
          color: 'rgba(255,255,255,0.72)',
        }}
      >
        VISITA VIRTUAL 360°
      </div>
      <div
        style={{
          position: 'absolute',
          left: 76,
          right: 76,
          top: 452,
          textAlign: 'center',
          color: P18.colores.blanco,
          fontFamily: P18.fuentes.titular,
          textShadow: SOMBRA,
        }}
      >
        <div style={{fontSize: 80, fontWeight: 300, lineHeight: 1.08}}>Empieza a conocer</div>
        <div style={{fontSize: 80, fontWeight: 400, fontStyle: 'italic', lineHeight: 1.08}}>
          Piso18 desde donde estés
        </div>
      </div>
      <Telefono src="s2710-salon.jpg" x={bloqueX} y={770} giro={-3.4} rotulo="EL LOUNGE" />
      <Telefono src="s2710-tour.jpg" x={bloqueX + TEL.ancho - SOLAPE} y={716} giro={3.0} rotulo="360°" />
    </AbsoluteFill>
  );
};

/** Guía de QA de historia: zonas seguras de Instagram en rojo. No se entrega. */
export const P18OGuiaStory: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill>
    {children}
    <div style={{position: 'absolute', left: 0, right: 0, top: 0, height: P18.seguras.story.arriba, background: 'rgba(255,0,0,0.22)', borderBottom: '2px solid red'}} />
    <div style={{position: 'absolute', left: 0, right: 0, bottom: 0, height: P18.seguras.story.abajo, background: 'rgba(255,0,0,0.22)', borderTop: '2px solid red'}} />
  </AbsoluteFill>
);
