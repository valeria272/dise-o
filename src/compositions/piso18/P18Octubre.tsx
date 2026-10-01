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

/**
 * SEGUNDA VERSIÓN del logotipo: en la esquina inferior derecha, blanco y siempre a la
 * misma medida (Eli, 29-09: «trata de que siempre ese logotipo en esa esquina sean
 * iguales (…) como una segunda versión, pero con el logo hacia abajo»). Para piezas
 * de foto sin texto; pide un velo leve abajo (`VeloPie`) para leerse. Feed 1080×1350.
 */
const LogoEsquina: React.FC<{alto?: number}> = ({alto = FEED_H}) => (
  <Img
    src={staticFile('assets/hilton/piso18/logo.png')}
    style={{
      position: 'absolute',
      width: 210,
      height: 210 / P18.geometria.logoProporcion,
      left: W - 48 - 210,
      top: alto - 48 - 210 / P18.geometria.logoProporcion,
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
export const PapelBeige: React.FC<{semilla?: number}> = ({semilla = 3}) => (
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
 *
 * Ronda 4, cliente 29-09 (FEED D13): «Falta logo». Va la segunda versión del
 * logotipo, `LogoEsquina`: blanco, abajo a la derecha, sobre un velo leve de pie.
 */
export const P18OF0610: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
    <Foto src="f0610.jpg" />
    {/* Ronda 4c, Eli 29-09: «oscurece abajo muy levemente y que el logo sea en blanco» */}
    <VeloPie hasta={0.3} opacidad={0.42} />
    <LogoEsquina />
  </AbsoluteFill>
);

// ═══════════════════════════════════════════════════════════════════════════
// FEED 09-10 · CARRUSEL «FECHAS 2027 EN TEMPORADA ALTA»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * RONDA 4 · cliente 29-09 (FEED C13): «Según brief la G2 también es imagen,
 * seleccionemos alguna horizontal para que quede dividida de forma continua».
 *
 * Las dos láminas son UNA foto: la 0161 horizontal (la misma de la portada
 * aprobada, ahora sin extender) partida al medio (`f0910-p1/p2`, cajas en
 * `scripts/p18-oct-fotos.py`). Todo lo que cruza el corte es idéntico a los dos
 * lados: el velo de arriba es el mismo en ambas, así el techo no «salta» al
 * deslizar. La S1 sigue sin texto (brief) y lleva el logotipo arriba y centrado
 * (R-12), como pidió el cliente en el post del mismo día. La S2 conserva el
 * titular aprobado de la ronda 1, en blanco sobre la foto (R-06); el calendario
 * de papel sale porque la lámina ya no es papel. La versión de papel quedó en
 * `out/piso18/oct/r3-respaldo/`.
 */
const VeloF0910: React.FC = () => <VeloArriba alfa={0.72} hasta={50} />;

/** S1 · mitad izquierda de la panorámica. Sin texto; sólo el logotipo. */
export const P18OF0910S1: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
    <Foto src="f0910-p1.jpg" />
    {/* Ronda 4d, Eli 29-09 («el fondo negro de esa transición, sigue corrigiéndola»): la
        capa negra de la S2 ya empieza acá, en el tercio derecho, y llega al corte con el
        mismo 0,76 de la S2: al deslizar el oscuro fluye sin escalón. */}
    <AbsoluteFill
      style={{background: 'linear-gradient(to right, rgba(8,8,10,0) 0%, rgba(8,8,10,0) 58%, rgba(8,8,10,0.76) 100%)'}}
    />
    <VeloF0910 />
    <Logo top={P18.geometria.logoYFeed} />
  </AbsoluteFill>
);

/**
 * S2 · Ronda 4b, Eli 29-09: «me gustaba cómo se veía temporada alta con ese diseño y
 * el calendario (…) hacer como una opacidad negra mostrando el calendario, que de fondo
 * se vea esa misma imagen». Vuelve el diseño aprobado (titular a dos voces +
 * calendario con el sábado encerrado) y el papel se cambia por la mitad derecha de la
 * foto continua bajo una capa negra PAREJA en toda la lámina (Eli, 2.ª vuelta: «quiero
 * que la G dos tenga esa transparencia oscurecida» en toda; la foto sigue continua y
 * el cambio de luz en el corte es buscado). Todo el texto pasa a blanco; el fucsia queda en
 * «SE PLANEAN CON TIEMPO» y el círculo del 16, como en la versión aprobada.
 */
const CapaNegraF0910: React.FC = () => (
  <AbsoluteFill
    style={{
      background:
        'rgba(8,8,10,0.76)',
    }}
  />
);

export const P18OF0910S2: React.FC = () => {
  cargarFuentesP18();
  const lineaCal = 'rgba(255,255,255,0.5)';
  const colX = [60, 380, 700, 1020];
  const topCal = 820;
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Foto src="f0910-p2.jpg" />
      <CapaNegraF0910 />
      {/* Ronda 7, cliente 01-10 (FEED C13): «Eliminar temporada alta de la G2» ⇒ sale el
          rótulo «TEMPORADA ALTA 2027»; el resto de la lámina aprobada no se mueve. */}
      <div style={{position: 'absolute', left: 40, right: 40, top: 272, textAlign: 'center', fontFamily: P18.fuentes.titular, color: P18.colores.blanco}}>
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
          color: P18.colores.blanco,
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
            color: P18.colores.blanco,
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
            color: P18.colores.blanco,
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
        {/* Ronda 6, Eli 29-09: criterio de Constanza (R-57) aplicado a todo el mes, espaciado ~0,08 em (antes 4 px = 0,19 em) */}
        <span style={{...RALEWAY, fontWeight: 700, fontSize: 21, letterSpacing: 1.7}}>
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
          // Ronda 6, Eli 29-09: criterio de Constanza (R-57) aplicado a todo el mes, espaciado ~0,08 em (antes 9 px = 0,36 em)
          letterSpacing: 2,
          textIndent: 2,
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
        <div style={{...RALEWAY, fontWeight: 700, fontSize: 24, letterSpacing: 2, textIndent: 2, marginTop: 28 /* R-57, antes 6 px = 0,25 em */}}>
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
// FEED 20-10 · POST ANIMADO «CUMPLEAÑOS EN PISO18»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * OK PARA DISEÑAR el 01-10. Brief: «ambientación de cumpleaños en Piso18, con la torta como
 * protagonista y detalles de mesa personalizados»; «los textos se deben animar pero la
 * imagen debe mantenerse quieta». Cliente (FEED H13): «Que se animen los textos de las cosas
 * que incluye el cumple».
 *
 * La foto NO se mueve (ni acercamiento): sólo entran los textos. Arriba el logotipo y el
 * nombre de la pieza a dos voces (R-06); debajo, los cinco textos del brief uno por uno, con
 * el número en cuadro fucsia de la lista de beneficios aprobada (R-39, C1 S5). Los
 * paréntesis del brief bajan a una segunda línea más liviana para que el renglón no se
 * parta. Sin línea «Cotiza…»: la hoja FEED no trae CTA (R-51).
 * Foto producida sobre el salón real de noche (banq 0044 y 0047), sin personas: las refs del
 * brief son fiestas con gente, pero el visual pedido es la torta y la mesa.
 */
export const P18_F2010_DUR = 240;
const INCLUYE_20: [string, string?][] = [
  ['Ambientación y decoración'],
  ['Servicios audiovisuales', '(DJ en vivo, amplificación, iluminación LED)'],
  ['Estaciones de comida'],
  ['Fiesta y barra libre', '(con opción de incluir karaoke)'],
  ['Comida de trasnoche'],
];

export const P18OF2010: React.FC = () => {
  cargarFuentesP18();
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const entra = (desde: number, dx = 0, dy = 26) => {
    const s = spring({frame: f - desde, fps, config: {damping: 200}, durationInFrames: 22});
    return {opacity: s, transform: `translate(${(1 - s) * dx}px, ${(1 - s) * dy}px)`};
  };
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Foto src="f2010.jpg" />
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to bottom, rgba(8,8,10,0.80) 0%, rgba(8,8,10,0.74) 46%, rgba(8,8,10,0.46) 60%, rgba(8,8,10,0) 74%)',
        }}
      />
      <Logo top={P18.geometria.logoYFeed} />
      <div style={{position: 'absolute', left: 0, right: 0, top: 248, textAlign: 'center', fontFamily: P18.fuentes.titular, color: P18.colores.blanco, textShadow: SOMBRA}}>
        <div style={{...entra(6), fontStyle: 'italic', fontWeight: 300, fontSize: 112, lineHeight: 1}}>Cumpleaños</div>
        <div style={{...entra(14), fontWeight: 400, fontSize: 56, lineHeight: 1.2, letterSpacing: 1}}>EN PISO18</div>
      </div>
      <div style={{position: 'absolute', left: 212, top: 476, display: 'flex', flexDirection: 'column', gap: 20}}>
        {INCLUYE_20.map(([texto, detalle], i) => {
          const desde = 34 + i * 24;
          const caja = spring({frame: f - desde, fps, config: {damping: 14, stiffness: 160}, durationInFrames: 20});
          return (
            <div key={texto} style={{display: 'flex', alignItems: 'flex-start', gap: 22}}>
              <div
                style={{
                  width: 46,
                  height: 46,
                  flexShrink: 0,
                  backgroundColor: P18.colores.fucsia,
                  color: P18.colores.blanco,
                  fontFamily: P18.fuentes.titular,
                  fontWeight: 400,
                  fontSize: 30,
                  lineHeight: '46px',
                  textAlign: 'center',
                  opacity: Math.min(1, caja * 1.4),
                  transform: `scale(${0.6 + 0.4 * caja})`,
                }}
              >
                {i + 1}
              </div>
              <div style={{...entra(desde + 3, -22, 0), color: P18.colores.blanco, textShadow: SOMBRA, ...RALEWAY}}>
                <div style={{fontWeight: 700, fontSize: 33, lineHeight: '46px'}}>{texto}</div>
                {detalle && <div style={{fontWeight: 500, fontSize: 24, lineHeight: 1.25, marginTop: -2, opacity: 0.9}}>{detalle}</div>}
              </div>
            </div>
          );
        })}
      </div>
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
      {/* Ronda 4, cliente 29-09 (STORIES C14): «quitemos botón diseñado para no repetir
          info» ⇒ sin botón; el pie queda libre para el sticker de enlace del CM (E-07). */}
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

const Calado: React.FC<{children: React.ReactNode; style: React.CSSProperties; trazo?: string; solido?: boolean}> = ({
  children,
  style,
  trazo = P18.colores.fucsia,
  solido = false,
}) => (
  <div
    style={{
      position: 'absolute',
      fontFamily: P18.fuentes.titular,
      fontStyle: 'italic',
      fontWeight: 400,
      fontSize: 140,
      lineHeight: 1,
      color: solido ? trazo : 'transparent',
      WebkitTextStroke: solido ? undefined : `2.8px ${trazo}`,
      ...style,
    }}
  >
    {children}
  </div>
);

/*
 * Ronda 4, cliente 29-09 (STORIES D14): «¿Veamos un fondo más entretenido? que sea
 * de algún montaje» ⇒ el papel beige sale y entra la foto de un MONTAJE real del
 * salón (mesa redonda con el centro alto de pampas, deco `piso_18-112`), apagada
 * para que las polaroids manden. Ronda 4b, Eli 29-09: «oscurece un poco más el fondo,
 * y así la palabra dulce con salada y la flechita sean del color fucsia de piso 18»;
 * el titular queda blanco. La composición es la aprobada.
 */
export const P18OS0710: React.FC = () => {
  cargarFuentesP18();
  const blanco = P18.colores.blanco;
  const fucsia = P18.colores.fucsia;
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      {/* Ronda 4c, Eli 29-09: «desenfoque gaussiano, para que no destaque tanto como lo
          que está al frente». El grano de encima evita que el pie liso del mantel se lea
          como foto estirada (R-18). */}
      <Foto src="s0710-fondo.jpg" style={{filter: 'blur(7px)', transform: 'scale(1.03)'}} />
      <AbsoluteFill style={{backgroundColor: 'rgba(8,8,10,0.5)'}} />
      <VeloArriba alfa={0.62} hasta={28} />
      <VeloPie hasta={0.36} opacidad={0.84} />
      <GranoFondo semilla={71} />
      {/* el logotipo dentro de los 250 px de arriba es del sistema (E-03) */}
      <Logo top={118} ancho={230} />
      <div
        style={{
          position: 'absolute',
          left: 60,
          right: 60,
          top: 244,
          textAlign: 'center',
          fontFamily: P18.fuentes.titular,
          color: blanco,
          textShadow: SOMBRA,
        }}
      >
        <div style={{fontSize: 66, fontWeight: 300, lineHeight: 1.08}}>¿Cuál es tu estación</div>
        <div style={{fontSize: 66, fontWeight: 400, fontStyle: 'italic', lineHeight: 1.08}}>
          favorita en Piso18?
        </div>
      </div>

      <Polaroid src="s0710-dulce.jpg" left={520} top={500} ancho={390} giro={4} />
      {/* Ronda 5, Constanza 29-09 (STORIES D8): «se pierde mucho el texto “dulce”
          “salada” en delineado (…) mejor sólido» ⇒ relleno fucsia, ya no calado. */}
      <Calado solido trazo={fucsia} style={{left: 270, top: 410, filter: 'drop-shadow(0 2px 10px rgba(0,0,0,0.7))'}}>Dulce</Calado>

      <Polaroid src="s0710-salada.jpg" left={560} top={1066} ancho={380} giro={-3.5} />
      <Calado solido trazo={fucsia} style={{right: 60, top: 942, textAlign: 'right', filter: 'drop-shadow(0 2px 10px rgba(0,0,0,0.7))'}}>Salada</Calado>

      {/* Las flechas nacen del hueco del sticker (x 60–480 · y 830–1030). */}
      <svg width={W} height={STORY_H} style={{position: 'absolute', inset: 0}}>
        <g fill="none" stroke={fucsia} strokeWidth={4} strokeLinecap="round" strokeLinejoin="round">
          <path d="M 160 810 C 120 710, 260 640, 486 650" />
          <path d="M 464 634 L 490 650 L 466 670" />
          <path d="M 170 1060 C 150 1200, 310 1290, 540 1280" />
          <path d="M 518 1260 L 544 1280 L 520 1300" />
        </g>
      </svg>
      {/* Sin «Cotiza tu evento en piso18.cl»: el brief sólo trae la barra «💖» (Eli 29-09:
          el llamado va SÓLO cuando el brief lo pide). */}
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
          {/* Ronda 4, cliente 29-09 (STORIES F14): «El Que con q mayúscula» */}
          ¿Qué es lo que más recuerdas de{' '}
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
// STORIES 15-10 · ENCUESTA «¿CUÁL SERÍA LA TEMÁTICA DE TU CUMPLEAÑOS SOÑADO?»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * OK PARA DISEÑAR el 29-09. Brief: «sticker de encuesta con 3 paletas visuales (retro,
 * tropical, blanco y dorado)»; interacción: «Bloque de respuestas»; comentario del
 * cliente: «Dejémos cuadro de respuesta a ver si prende».
 *
 * Ref (pin 978125612833263938, «Midori»): el local de noche a sangre, una HOJA de
 * papel rasgada abajo al centro con el texto arriba, y cruzándola una TIRA de tres
 * fotos con marco blanco que se sale de la hoja por los lados. Acá la hoja es el
 * beige de la marca con fibra, el texto es la pregunta (itálica fina + destacado,
 * como la 09-10) y las tres fotos son las tres temáticas, cada una con su nombre en
 * el marco. El papel de abajo queda LIMPIO para el cuadro de respuestas del CM (R-11).
 * Sin «Cotiza…»: el brief no trae CTA (Eli 29-09). Sin el 🎉 del brief: los emojis
 * los pone el CM.
 * Fotos: de fondo las esferas con velas del salón real (deco piso_18-143, ronda 2); las
 * temáticas, generadas sobre la mesa larga real banq46 (`p18-oct-generar.py st15-*`),
 * foto documental sin personas; la hoja, una textura de papel arrugado generada con la
 * ref de guía (`st15-papel`).
 */
const HOJA_15 = {x: 110, y: 470, w: 860, h: 1120};
/**
 * Borde rasgado de abajo, como el de la ref: mordidas HONDAS e irregulares (hasta ~70 px,
 * tres ondas que no se repiten) con un deshilachado fino encima (un punto cada 3 px con
 * ruido fijo). Sin filo blanco: en la ref el borde es del mismo tono del papel.
 * Ronda 2, Eli 29-09: «la textura del papel rasgado igual a la referencia».
 */
const rasgado = (w: number, h: number) => {
  const pts: string[] = ['0px 0px', `${w}px 0px`];
  for (let x = w, i = 0; x >= 0; x -= 3, i++) {
    const r1 = ((i * 7919) % 101) / 101;
    const r2 = ((i * 104729 + 17) % 53) / 53;
    const onda = 22 * Math.sin(x / 67 + 0.4) + 14 * Math.sin(x / 29 + 2.1) + 9 * Math.sin(x / 151 + 1.3);
    const y = h - 48 + onda - 10 * r1 - (r2 > 0.86 ? 12 * r2 : 0);
    pts.push(`${x}px ${y.toFixed(1)}px`);
  }
  return `polygon(${pts.join(', ')})`;
};

const Tematica: React.FC<{src: string; nombre: string}> = ({src, nombre}) => (
  <div style={{width: 272, padding: '11px 11px 0', backgroundColor: '#FFFFFF', boxShadow: '0 10px 28px rgba(0,0,0,0.30)'}}>
    <Img src={oct(src)} style={{width: '100%', aspectRatio: '3 / 4', objectFit: 'cover', display: 'block'}} />
    <div
      style={{
        ...RALEWAY,
        fontWeight: 700,
        fontSize: 19,
        // Ronda 6, Eli 29-09: criterio de Constanza (R-57) aplicado a todo el mes, espaciado ~0,08 em (antes 3 px = 0,16 em)
        letterSpacing: 1.5,
        textIndent: 1.5,
        textAlign: 'center',
        color: P18.colores.tinta,
        padding: '16px 0 18px',
      }}
    >
      {nombre}
    </div>
  </div>
);

export const P18OS1510: React.FC = () => {
  cargarFuentesP18();
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      {/* esferas con velas del salón de noche: poco desenfoque para que las luces brillen */}
      <Foto src="s1510-fondo.jpg" style={{filter: 'blur(1.5px)', transform: 'scale(1.01)'}} />
      <AbsoluteFill style={{backgroundColor: 'rgba(8,8,10,0.34)'}} />
      <GranoFondo semilla={29} />
      <Logo top={P18.geometria.logoYStory} />

      {/* la hoja rasgada */}
      {/* la sombra va en el contenedor: el clip-path del hijo también cortaría la sombra */}
      <div
        style={{
          position: 'absolute',
          left: HOJA_15.x,
          top: HOJA_15.y,
          width: HOJA_15.w,
          height: HOJA_15.h,
          filter: 'drop-shadow(0 14px 26px rgba(0,0,0,0.55))',
        }}
      >
        {/* la hoja es una textura de papel arrugado (`st15-papel`), no el PapelBeige plano */}
        <div style={{position: 'absolute', inset: 0, clipPath: rasgado(HOJA_15.w, HOJA_15.h)}}>
          <Foto src="s1510-papel.jpg" />
        </div>
      </div>
      <div
        style={{
          position: 'absolute',
          left: HOJA_15.x + 50,
          width: HOJA_15.w - 100,
          top: HOJA_15.y + 70,
          textAlign: 'center',
          fontFamily: P18.fuentes.titular,
          color: P18.colores.tinta,
        }}
      >
        <div style={{fontSize: 58, fontWeight: 300, fontStyle: 'italic', lineHeight: 1.1}}>¿Cuál sería la temática</div>
        <div style={{fontSize: 58, fontWeight: 400, lineHeight: 1.1}}>
          de tu <span style={{fontStyle: 'italic', color: P18.colores.fucsia}}>cumpleaños soñado?</span>
        </div>
      </div>

      {/* la tira de tres fotos, al ancho de la hoja: sacarla por los lados como en la ref la mete en la zona que tapa Meta */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: HOJA_15.y + 250,
          display: 'flex',
          justifyContent: 'center',
          gap: 16,
          // la tira termina en x≈964: a la derecha, Meta tapa 115 px (QA, borrador 29-09)
          transform: 'rotate(-1.2deg)',
        }}
      >
        <Tematica src="s1510-retro.jpg" nombre="RETRO" />
        <Tematica src="s1510-tropical.jpg" nombre="TROPICAL" />
        <Tematica src="s1510-dorado.jpg" nombre="BLANCO Y DORADO" />
      </div>
      {/* y 1260–1560: papel limpio para el cuadro de respuestas del CM */}
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════════
// STORIES 13-10 · «CUENTA REGRESIVA AL 2027»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * Tomada el 01-10 por encargo de Eli («toma las stories del 13 y 19 de octubre, sólo que
 * corrige según comentario de cliente»). Cliente (STORIES H14): «Digamos Cuenta regresiva
 * al 2027 · No hablemos de temporada alta» ⇒ el titular es «Cuenta regresiva al 2027» y
 * «temporada» no aparece en la pieza.
 *
 * Ref (pin 368310075797660531, «Mes de aniversario»): un SOBRE de color abierto sobre la
 * foto de una mesa, con la TARJETA blanca asomando y el texto adentro (titular, una línea
 * en píldora de contorno y el regalo), y el legal chico sobre el sobre. Acá el sobre es el
 * fucsia de la marca, la tarjeta es el papel `#F7F5F2` y adentro va la oferta con el bloque
 * de precio aprobado de `ST N°1 S1` («¿Te casas en verano?»): ANTES tachado y AHORA en caja
 * fucsia (R-08), cifras en Raleway con cada dígito en su caja (R-19). La bajada va sobre el
 * sobre, como el legal de la ref; el legal «*Desde 60 invitados», al pie. Brief con CTA
 * («Cotiza ya en piso18.cl») ⇒ botón, invertido para no sumar más fucsia.
 * Foto: la mesa real de matrimonio con flores y esferas (deco `piso_18-88`).
 */
const Cifras: React.FC<{texto: string; cuerpo: number}> = ({texto, cuerpo}) => (
  <span style={{display: 'inline-flex', alignItems: 'baseline'}}>
    {texto.split('').map((c, i) =>
      /\d/.test(c) ? (
        <span key={i} style={{display: 'inline-block', width: cuerpo * P18.cifras.anchoDigitoMax, textAlign: 'center'}}>
          {c}
        </span>
      ) : (
        <span key={i}>{c}</span>
      ),
    )}
  </span>
);

const SOBRE_13 = {x: 110, y: 980, w: 860, h: 580, pico: 480, v: 290};
const TARJETA_13 = {x: 200, y: 548, w: 680};

export const P18OS1310: React.FC = () => {
  cargarFuentesP18();
  const S = SOBRE_13;
  const fucsia = P18.colores.fucsia;
  const cx = S.x + S.w / 2;
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Foto src="s1310-fondo.jpg" />
      <AbsoluteFill style={{backgroundColor: 'rgba(8,8,10,0.30)'}} />
      <VeloArriba alfa={0.66} hasta={30} />
      <VeloPie hasta={0.3} opacidad={0.8} />
      <Logo top={P18.geometria.logoYStory} />

      {/* el sobre por detrás: la solapa abierta y el fondo del bolsillo */}
      <svg width={W} height={STORY_H} style={{position: 'absolute', inset: 0, filter: 'drop-shadow(0 22px 34px rgba(0,0,0,0.45))'}}>
        <path
          d={`M ${S.x} ${S.y} L ${cx - 26} ${S.pico + 14} Q ${cx} ${S.pico - 6} ${cx + 26} ${S.pico + 14} L ${S.x + S.w} ${S.y} L ${S.x + S.w} ${S.y + S.h} L ${S.x} ${S.y + S.h} Z`}
          fill="#B00F49"
        />
      </svg>

      {/* la tarjeta: asoma del sobre y se pierde detrás de las solapas del frente */}
      <div
        style={{
          position: 'absolute',
          left: TARJETA_13.x,
          top: TARJETA_13.y,
          width: TARJETA_13.w,
          height: S.y + S.v - TARJETA_13.y,
          backgroundColor: P18.colores.tarjeta,
          boxShadow: '0 8px 22px rgba(0,0,0,0.30)',
          color: P18.colores.tinta,
          textAlign: 'center',
        }}
      >
        <div style={{marginTop: 46, fontFamily: P18.fuentes.titular, fontStyle: 'italic', fontWeight: 300, fontSize: 78, lineHeight: 1}}>
          Cuenta regresiva
        </div>
        <div style={{fontFamily: P18.fuentes.titular, fontWeight: 400, fontSize: 88, lineHeight: 1.08, letterSpacing: 1}}>
          AL 2027
        </div>
        <div style={{display: 'flex', justifyContent: 'center', marginTop: 22}}>
          <div
            style={{
              ...RALEWAY,
              fontWeight: 700,
              fontSize: 21,
              letterSpacing: 1.7,
              textIndent: 1.7,
              padding: '10px 26px',
              borderRadius: 999,
              border: `1.6px solid ${P18.colores.tinta}`,
              whiteSpace: 'nowrap',
            }}
          >
            DESCUENTO DE VERANO EN TU MATRIMONIO
          </div>
        </div>
        {/* ANTES: la cifra tachada, chica */}
        <div style={{marginTop: 26, display: 'flex', justifyContent: 'center', alignItems: 'baseline', gap: 14, ...RALEWAY, color: 'rgba(26,26,26,0.72)'}}>
          <span style={{fontWeight: 700, fontSize: 20, letterSpacing: 1.6}}>ANTES</span>
          <span style={{position: 'relative', fontWeight: 500, fontSize: 44, lineHeight: 1}}>
            <Cifras texto="$6.000.000" cuerpo={44} />
            <span style={{position: 'absolute', left: -6, right: -6, top: '54%', height: 2.4, backgroundColor: fucsia}} />
          </span>
        </div>
        {/* AHORA: la cifra nueva en la caja fucsia */}
        <div style={{display: 'flex', justifyContent: 'center', marginTop: 16}}>
          <div style={{backgroundColor: fucsia, color: P18.colores.blanco, padding: '12px 38px 16px', ...RALEWAY}}>
            <div style={{fontWeight: 700, fontSize: 22, letterSpacing: 1.8, textIndent: 1.8}}>AHORA</div>
            <div style={{fontWeight: 800, fontSize: 78, lineHeight: 1.02}}>
              <Cifras texto="$4.500.000" cuerpo={78} />
            </div>
          </div>
        </div>
      </div>

      {/* el frente del sobre: dos solapas laterales y la de abajo, con el filete en relieve */}
      <svg width={W} height={STORY_H} style={{position: 'absolute', inset: 0}}>
        <defs>
          <linearGradient id="p18o-sobre-lado" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0" stopColor="#C71255" />
            <stop offset="0.5" stopColor={fucsia} />
            <stop offset="1" stopColor="#C71255" />
          </linearGradient>
          <linearGradient id="p18o-sobre-pie" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stopColor="#DC2A6A" />
            <stop offset="1" stopColor={fucsia} />
          </linearGradient>
        </defs>
        <path
          d={`M ${S.x} ${S.y} L ${cx} ${S.y + S.v} L ${S.x + S.w} ${S.y} L ${S.x + S.w} ${S.y + S.h} L ${S.x} ${S.y + S.h} Z`}
          fill="url(#p18o-sobre-lado)"
        />
        <path
          d={`M ${S.x} ${S.y + S.h} L ${cx - 30} ${S.y + S.v - 22} Q ${cx} ${S.y + S.v - 44} ${cx + 30} ${S.y + S.v - 22} L ${S.x + S.w} ${S.y + S.h} Z`}
          fill="url(#p18o-sobre-pie)"
          style={{filter: 'drop-shadow(0 -4px 8px rgba(80,0,30,0.35))'}}
        />
        {/* filete en relieve, como el del sobre de la ref */}
        <path
          d={`M ${S.x + 14} ${S.y + 30} L ${cx} ${S.y + S.v + 6} L ${S.x + S.w - 14} ${S.y + 30}`}
          fill="none"
          stroke="rgba(255,255,255,0.20)"
          strokeWidth={1.6}
        />
        <path
          d={`M ${S.x + 16} ${S.y + S.h - 14} L ${cx - 26} ${S.y + S.v - 4} Q ${cx} ${S.y + S.v - 24} ${cx + 26} ${S.y + S.v - 4} L ${S.x + S.w - 16} ${S.y + S.h - 14} Z`}
          fill="none"
          stroke="rgba(90,0,34,0.30)"
          strokeWidth={1.6}
        />
      </svg>
      <div
        style={{
          position: 'absolute',
          left: S.x + 150,
          width: S.w - 300,
          top: S.y + S.h - 138,
          textAlign: 'center',
          ...RALEWAY,
          fontStyle: 'italic',
          fontWeight: 500,
          fontSize: 25,
          lineHeight: 1.36,
          color: P18.colores.blanco,
        }}
      >
        Válido para matrimonios realizados en diciembre, enero, febrero o marzo
      </div>

      <Boton top={1608} invertido>
        Cotiza ya en piso18.cl
      </Boton>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 1768,
          textAlign: 'center',
          ...RALEWAY,
          fontStyle: 'italic',
          fontWeight: 500,
          fontSize: 23,
          color: P18.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        *Desde 60 invitados
      </div>
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════════
// STORIES 19-10 · «FIESTA DE EMPRESA DE FIN DE AÑO»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * Tomada el 01-10 por encargo de Eli, con el comentario del cliente (STORIES L14): «Ok pero
 * no digamos diciembre, cerremos en corporativas · Foco fiesta empresa fin de año» ⇒ la
 * bajada termina en «fiestas corporativas» y «diciembre» no aparece en la pieza (tampoco en
 * la gráfica: el brief pedía un calendario apuntando a diciembre).
 *
 * Ref (pin 1096908053025288014): fondo en blanco y negro con grano, una POLAROID a color
 * pegada con cinta y, montada sobre ella, una HOJA de cuaderno arrancada con el texto en
 * rojo. Acá la cinta y el destacado son el fucsia de la marca, la hoja es el papel
 * `#F7F5F2` con renglones y la letra es IvyPresto itálica (el titular empieza con «¿»: no
 * va en Against, R-20). Fondo: mesas del salón de noche (julio evento 50) en blanco y
 * negro; polaroid: brindis de fin de año producido sobre el salón y la barra reales (R-41).
 * Brief con CTA («Asegura tu fecha en piso18.cl») ⇒ botón.
 */
const HOJA_19 = {x: 176, y: 880, w: 740, h: 600};
/** Hoja de cuaderno: mordidas cuadradas del espiral a la izquierda y la esquina de abajo redonda. */
const arrancada = (w: number, h: number) => {
  const pts: string[] = [];
  const paso = 46;
  for (let y = 0, i = 0; y < h; y += paso, i++) {
    const j = ((i * 7919) % 11) - 5; // el desgarro no es parejo
    pts.push(`${26 + j * 0.6}px ${y}px`, `${26 + j * 0.6}px ${y + 12}px`, `${2 + (j > 2 ? 9 : 0)}px ${y + 14 + (j % 3)}px`, `${4}px ${y + 34}px`, `${24 + j * 0.5}px ${y + 36}px`);
  }
  pts.push(`26px ${h}px`, `${w - 30}px ${h}px`, `${w - 8}px ${h - 8}px`, `${w}px ${h - 30}px`, `${w}px 0px`);
  return `polygon(${pts.join(', ')})`;
};

export const P18OS1910: React.FC = () => {
  cargarFuentesP18();
  const H = HOJA_19;
  const fucsia = P18.colores.fucsia;
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Foto src="s1910-fondo.jpg" style={{filter: 'grayscale(1) contrast(1.06) brightness(0.72) blur(2px)', transform: 'scale(1.02)'}} />
      <AbsoluteFill style={{backgroundColor: 'rgba(8,8,10,0.30)'}} />
      <VeloArriba alfa={0.6} hasta={26} />
      <VeloPie hasta={0.3} opacidad={0.8} />
      <GranoFondo semilla={19} />
      <Logo top={P18.geometria.logoYStory} />

      {/* la hoja va primero: la polaroid se monta sobre su borde de arriba, como en la ref */}
      <div style={{position: 'absolute', left: H.x, top: H.y, width: H.w, height: H.h, transform: 'rotate(-0.8deg)', filter: 'drop-shadow(0 14px 24px rgba(0,0,0,0.5))'}}>
        <div style={{position: 'absolute', inset: 0, clipPath: arrancada(H.w, H.h), backgroundColor: P18.colores.tarjeta}}>
          {Array.from({length: 9}).map((_, i) => (
            <div key={i} style={{position: 'absolute', left: 70, right: 28, top: 176 + i * 46, height: 1.4, backgroundColor: 'rgba(26,26,26,0.13)'}} />
          ))}
          <GranoFondo semilla={57} />
        </div>
        <div style={{position: 'absolute', left: 84, right: 44, top: 168, textAlign: 'center', color: P18.colores.tinta}}>
          <div style={{fontFamily: P18.fuentes.titular, fontStyle: 'italic', fontWeight: 400, fontSize: 53, lineHeight: 1.12}}>
            ¿Ya tienen fecha para
            <br />
            el evento de <span style={{color: fucsia}}>fin de año</span>
            <br />
            <span style={{color: fucsia}}>de la empresa?</span>
          </div>
          <div style={{...RALEWAY, fontWeight: 500, fontSize: 29, lineHeight: 1.36, marginTop: 30}}>
            Últimas fechas disponibles
            <br />
            para fiestas corporativas
          </div>
          <div style={{...RALEWAY, fontWeight: 800, fontSize: 31, marginTop: 20, color: fucsia}}>¡Cotiza hoy!</div>
        </div>
      </div>

      {/* la polaroid con su cinta */}
      <div
        style={{
          position: 'absolute',
          left: 292,
          top: 392,
          width: 520,
          padding: '22px 22px 74px',
          backgroundColor: '#FFFFFF',
          transform: 'rotate(2.6deg)',
          boxShadow: '0 18px 40px rgba(0,0,0,0.5)',
        }}
      >
        <Img src={oct('s1910-fiesta.jpg')} style={{width: '100%', aspectRatio: '1 / 1', objectFit: 'cover', display: 'block'}} />
      </div>
      <div
        style={{
          position: 'absolute',
          left: 468,
          top: 372,
          width: 190,
          height: 58,
          transform: 'rotate(-2deg)',
          backgroundColor: fucsia,
          opacity: 0.94,
          boxShadow: '0 3px 8px rgba(0,0,0,0.3)',
        }}
      />

      <Boton top={1572}>Asegura tu fecha en piso18.cl</Boton>
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════════
// STORIES 21-10 · ENCUESTA «ESTACIONES DE COMIDA»
// ═══════════════════════════════════════════════════════════════════════════
/**
 * OK PARA DISEÑAR el 01-10, con el brief ya corregido por contenido (cliente, STORIES M14:
 * «en vs 2 estaciones de comida (salada) y dejar una tercera alternativa que diga las 2»).
 * Brief: «pantalla dividida con fotografías de ambas propuestas: lado A Estación Japonesa,
 * lado B Estación New York»; texto «¿Cuáles arman el menú perfecto para tu evento?» +
 * «(Dato: puedes combinar hasta 2 estaciones)»; sticker de 3 opciones (Japonesa / New York
 * / ¡Las 2!), que pone el CM (R-11).
 *
 * La ref es la misma «Midori» de la 15-10 (seis días antes). Para no repetir esa historia,
 * de la ref se toma la HOJA de papel rasgado con el texto, y la composición es la del
 * brief: la pantalla partida en dos, una estación arriba y otra abajo, con la hoja cruzando
 * el corte. El papel de abajo del texto queda LIMPIO para el sticker. Sin CTA en el brief
 * ⇒ sin botón ni línea (R-51). Fotos producidas sobre el buffet real banq 0052 (R-45).
 */
const HOJA_21 = {x: 120, y: 648, w: 840, h: 640};
const rasgadoDoble = (w: number, h: number) => {
  const pts: string[] = [];
  for (let x = 0, i = 0; x <= w; x += 3, i++) {
    const r1 = ((i * 6007) % 97) / 97;
    const onda = 16 * Math.sin(x / 53 + 1.1) + 10 * Math.sin(x / 23 + 0.3) + 7 * Math.sin(x / 131 + 2.2);
    pts.push(`${x}px ${(34 + onda - 8 * r1).toFixed(1)}px`);
  }
  for (let x = w, i = 0; x >= 0; x -= 3, i++) {
    const r1 = ((i * 7919) % 101) / 101;
    const r2 = ((i * 104729 + 17) % 53) / 53;
    const onda = 22 * Math.sin(x / 67 + 0.4) + 14 * Math.sin(x / 29 + 2.1) + 9 * Math.sin(x / 151 + 1.3);
    pts.push(`${x}px ${(h - 48 + onda - 10 * r1 - (r2 > 0.86 ? 12 * r2 : 0)).toFixed(1)}px`);
  }
  return `polygon(${pts.join(', ')})`;
};

const RotuloEstacion: React.FC<{top: number; nombre: string}> = ({top, nombre}) => (
  <div style={{position: 'absolute', left: 0, right: 0, top, textAlign: 'center', color: P18.colores.blanco, textShadow: '0 2px 18px rgba(0,0,0,0.75)'}}>
    <span style={{fontFamily: P18.fuentes.titular, fontWeight: 300, fontSize: 60, lineHeight: 1}}>Estación </span>
    <span style={{fontFamily: P18.fuentes.titular, fontStyle: 'italic', fontWeight: 400, fontSize: 68, lineHeight: 1}}>{nombre}</span>
  </div>
);

export const P18OS2110: React.FC = () => {
  cargarFuentesP18();
  const H = HOJA_21;
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <div style={{position: 'absolute', left: 0, top: 0, width: W, height: STORY_H / 2, overflow: 'hidden'}}>
        <Foto src="s2110-japonesa.jpg" />
      </div>
      <div style={{position: 'absolute', left: 0, top: STORY_H / 2, width: W, height: STORY_H / 2, overflow: 'hidden'}}>
        <Foto src="s2110-newyork.jpg" />
      </div>
      {/* el logotipo cae sobre la comida: velo de portada más hondo que el de R-14 */}
      <AbsoluteFill
        style={{background: 'linear-gradient(to bottom, rgba(8,8,10,0.88) 0%, rgba(8,8,10,0.8) 17%, rgba(8,8,10,0.3) 24%, rgba(8,8,10,0) 30%)'}}
      />
      {/* un oscuro leve detrás de cada rótulo, pegado a la hoja */}
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to bottom, rgba(8,8,10,0) 22%, rgba(8,8,10,0.5) 31%, rgba(8,8,10,0.5) 68%, rgba(8,8,10,0) 80%, rgba(8,8,10,0) 86%, rgba(8,8,10,0.55) 100%)',
        }}
      />
      <Logo top={P18.geometria.logoYStory} />
      <RotuloEstacion top={552} nombre="Japonesa" />
      <RotuloEstacion top={1300} nombre="New York" />

      <div style={{position: 'absolute', left: H.x, top: H.y, width: H.w, height: H.h, transform: 'rotate(-0.9deg)', filter: 'drop-shadow(0 14px 26px rgba(0,0,0,0.55))'}}>
        <div style={{position: 'absolute', inset: 0, clipPath: rasgadoDoble(H.w, H.h)}}>
          <Foto src="s1510-papel.jpg" />
        </div>
        <div style={{position: 'absolute', left: 50, right: 50, top: 92, textAlign: 'center', fontFamily: P18.fuentes.titular, color: P18.colores.tinta}}>
          <div style={{fontSize: 56, fontWeight: 300, fontStyle: 'italic', lineHeight: 1.1}}>¿Cuáles arman</div>
          <div style={{fontSize: 56, fontWeight: 400, lineHeight: 1.1}}>
            el <span style={{fontStyle: 'italic', color: P18.colores.fucsia}}>menú perfecto</span>
          </div>
          <div style={{fontSize: 56, fontWeight: 400, lineHeight: 1.1}}>para tu evento?</div>
          <div style={{...RALEWAY, fontWeight: 600, fontSize: 25, marginTop: 20}}>
            (Dato: puedes combinar hasta 2 estaciones)
          </div>
        </div>
        {/* y 340–580 de la hoja: papel limpio para el sticker de 3 opciones del CM */}
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
          // Ronda 6, Eli 29-09: criterio de Constanza (R-57) aplicado a todo el mes, espaciado ~0,08 em (antes 6,5 px = 0,30 em)
          letterSpacing: 1.8,
          textIndent: 1.8,
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

/** Guía de zonas seguras de la 15-10, para el render por Chrome (no se sube). */
export const P18OS1510Guia: React.FC = () => (
  <P18OGuiaStory>
    <P18OS1510 />
  </P18OGuiaStory>
);
