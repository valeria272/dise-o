/**
 * BETWEEN — OCTUBRE 2026 · lo que está OK PARA DISEÑAR de la S1 a la S5
 *
 * Grilla `1EnZOwUptY6SftX-CF9ZFwXUuzPCGZ76L` leída EN VIVO el 24-09 (CSV + gid
 * y conector con comentarios; el `.xlsx` bajado coincidía celda a celda).
 * Encargo de Eli, 24-09: «diseña solamente lo que está ok para diseñar […]
 * guíate de lo visual, de los comentarios de diseño y cliente y de la
 * referencia». Todo lo que está en REVISAR CONTENIDO / EN REVISIÓN / PENDIENTE
 * POR CLIENTE queda fuera (9-10, 22-10, 25-10 y 29-10 en historias).
 *
 *   STORIES
 *   col C · 01-10 · ESTÁTICA · Anuncio ganador concurso (ADAPTACIÓN DEL POST)
 *   col D · 02-10 · ANIMADA  · Promos To Go en POV            · LINK CARTA
 *   col G · 05-10 · ESTÁTICA · Paso por un café y… (collage)   · LINK CARTA
 *   col H · 07-10 · ESTÁTICA · Café gratis por cumpleaños
 *   col I · 08-10 · ESTÁTICA · Trivia Between                  · CAJA DE PREGUNTAS
 *   col L · 19-10 · ESTÁTICA · Cowork
 *   col M · 20-10 · ESTÁTICA · Lo dicen ustedes
 *   col Q · 26-10 · ANIMADA  · «WTF…» — ⛔ NO se diseña: dice GRABAR ORGÁNICO
 *   col R · 27-10 · ESTÁTICA · ¿Buscas un espacio para tu evento? · CTA + enlace web eventos
 *   col T · 28-10 · ESTÁTICA · Desayuno Bonjour                · LINK CARTA
 *   FEED
 *   col F · 05-10 · ESTÁTICO · Esa reunión podría ser un café
 *   col L · 14-10 · ESTÁTICO · Espacios Between — «Que sea sutil la ilustración»
 *
 * Reglas que cruzan toda la tanda (manual `clients/hilton/CLAUDE.md`):
 *   · textos LITERALES de la grilla, **sin punto** en títulos ni bajadas (regla
 *     del cliente del 23-09 para las 4 cuentas); el legal sí lo lleva.
 *   · la interacción NO se dibuja: se deja la zona limpia y la copia `Guia`
 *     la marca para el CM.
 *   · el vaso con logotipo impreso firma solo: esa pieza va SIN lockup.
 *   · «hay muchos similares en historias»: no todas con script + caja alta.
 *     Cada pieza toma un registro distinto del repertorio de la marca.
 */
import React from 'react';
import {
  AbsoluteFill,
  Img,
  interpolate,
  OffthreadVideo,
  staticFile,
  useCurrentFrame,
  Easing,
} from 'remotion';
import {BETWEEN} from '../../brand/hilton-between';
import {
  Bajada,
  CajaDato,
  CIFRAS_ALTAS,
  conCifras,
  FotoFondo,
  LogoBetween,
  TitularBetween,
  useFuentesListas,
} from './BetweenSistema';
import {Ilustra} from './BetweenRecursos';

const F = 'assets/hilton/between/oct/';
const G = 'assets/hilton/between/oct/gen/';
const C = BETWEEN.colores;
const SANS = BETWEEN.fuentes.sans;
const SOMBRA = '0 2px 16px rgba(36,26,18,0.75)';

/* ─── zona reservada para el sticker real de Instagram (sólo en la GUÍA) ─── */
type Zona = {ancho: number; alto: number; top: number; left?: number};
const ZonaReservada: React.FC<{zona: Zona; etiqueta: string}> = ({zona, etiqueta}) => (
  <div
    style={{
      position: 'absolute',
      left: zona.left ?? (1080 - zona.ancho) / 2,
      top: zona.top,
      width: zona.ancho,
      height: zona.alto,
      border: '3px dashed rgba(255,45,141,0.95)',
      borderRadius: 22,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      whiteSpace: 'pre-line',
      textAlign: 'center',
      fontFamily: SANS,
      fontWeight: 700,
      fontSize: 26,
      lineHeight: 1.35,
      color: '#ff2d8d',
      background: 'rgba(255,255,255,0.10)',
    }}
  >
    {etiqueta}
  </div>
);

const Columna: React.FC<{top: number; ancho?: number; children: React.ReactNode}> = ({
  top,
  ancho = BETWEEN.bloque.columna,
  children,
}) => (
  <div
    style={{
      position: 'absolute',
      left: (1080 - ancho) / 2,
      width: ancho,
      top,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    }}
  >
    {children}
  </div>
);

/** Logotipo en café de marca (`logo-cafe-marca.png`; `tono="cafe"` del kit es NEGRO). */
const LogoCafe: React.FC<{top?: number; ancho?: number}> = ({top = 271, ancho = 282}) => (
  <Img
    src={staticFile('assets/hilton/between/logo-cafe-marca.png')}
    style={{position: 'absolute', top, left: (1080 - ancho) / 2, width: ancho}}
  />
);

/**
 * Flecha dibujada: trazo beige de grosor constante con puntas redondas y una
 * sombra suave para leerse sobre la foto. La punta se calcula con la tangente
 * del final del trazo (último punto de control → punto final), así sigue la
 * curva sin importar hacia dónde apunte. Va DENTRO de un <svg> de 1080×1920.
 */
const Flecha: React.FC<{d: string; grosor?: number; punta?: number; color?: string}> = ({
  d,
  grosor = 7,
  punta = 24,
  color = C.beige,
}) => {
  const n = d.replace(/[A-Za-z]/g, ' ').trim().split(/[\s,]+/).map(Number);
  const [x2, y2] = [n[n.length - 2], n[n.length - 1]];
  const [x1, y1] = [n[n.length - 4], n[n.length - 3]];
  const ang = Math.atan2(y2 - y1, x2 - x1);
  const ala = (s: number) =>
    `${x2 - punta * Math.cos(ang + s * 0.5)} ${y2 - punta * Math.sin(ang + s * 0.5)}`;
  const trazo = {
    fill: 'none',
    stroke: color,
    strokeWidth: grosor,
    strokeLinecap: 'round' as const,
    strokeLinejoin: 'round' as const,
    filter: 'drop-shadow(0 2px 4px rgba(36,26,18,0.45))',
  };
  return (
    <g>
      <path d={d} style={trazo} />
      <path d={`M ${ala(1)} L ${x2} ${y2} L ${ala(-1)}`} style={trazo} />
    </g>
  );
};

const Texto: React.FC<{
  size: number;
  peso?: number;
  color?: string;
  italic?: boolean;
  sombra?: boolean;
  style?: React.CSSProperties;
  children: React.ReactNode;
}> = ({size, peso = 500, color = C.beige, italic, sombra, style, children}) => (
  <div
    style={{
      fontFamily: SANS,
      fontSize: size,
      fontWeight: peso,
      fontStyle: italic ? 'italic' : 'normal',
      color,
      lineHeight: 1.25,
      textAlign: 'center',
      whiteSpace: 'pre-line',
      textShadow: sombra ? SOMBRA : undefined,
      ...style,
    }}
  >
    {children}
  </div>
);

/* ══════════════════════════════════════════════════════════════════════════
   01-10 · ST ANUNCIO GANADOR CONCURSO — «ADAPTACIÓN DEL POST»

   El post es el carrusel C1 S3 CONCURSO ya publicado (N1 r13). La historia lo
   ADAPTA, no lo reinventa: el mismo papel beige rosado, la misma modelo
   recortada tipo sticker con su borde blanco, tinta y logo en café, el titular
   con contorno de sticker y la cajita inclinada — que ahora dice el sello que
   pide el brief, «VACANTE CERRADA».
   ⭐ Fondo: la lámina aprobada `c1-portada-papel.jpg` INTACTA, abajo, y el papel
   liso continuado hacia arriba (espejo de su franja superior + mezcla de 300
   px). No se regeneró: la tirada de Nano Banana escribía «COFFEE AGN» en el vaso.
   El «[BOTÓN @usuario]» es la mención: zona reservada para el sticker real.
   ══════════════════════════════════════════════════════════════════════════ */
const ZONA_MENCION: Zona = {ancho: 460, alto: 96, top: 805}; // medido r3: centrado entre «Felicidades» y «Te ganaste»

/**
 * ⭐ RONDA CONSTANZA 29-09 (grilla col C, comentario nativo): «demasiadas
 * variantes tipográficas y muchos tamaños, se ve desordenado, unifiquemos […] y
 * donde dice "Ya tenemos CEO del café" no queda bien delineado».
 *  · Tres voces y nada más, todas Raleway: TITULAR (ExtraBold 112, las dos
 *    líneas al MISMO cuerpo), CAJA (ExtraBold 45, el sello y el premio iguales)
 *    y TEXTO (SemiBold 36, sin itálica: Felicidades, Te ganaste, el aviso del
 *    premio y el cierre). Antes eran 8 combinaciones de cuerpo/peso/estilo.
 *  · «Delineado»: el halo de 24 sombras (`contorno` del kit) salía escalonado
 *    en «YA TENEMOS» al 2× — dientes de sierra en cada curva. Ahora es un trazo
 *    SVG redondo (asoma 7 px, como el halo de antes) en una capa DEBAJO del relleno (dos <text>, no
 *    paint-order, que Chrome aplica glifo a glifo y cruza las letras).
 */
const CEO_LINEAS = ['YA TENEMOS', 'CEO DEL CAFÉ'];
const CEO_SIZE = 112;
const CEO_PASO = 112; // de línea base a línea base: 30 px de aire entre mayúsculas
const TituloCeo: React.FC = () => {
  const alto = 22 + CEO_SIZE * 0.71 + CEO_PASO + 10;
  const capa = (trazo: boolean) =>
    CEO_LINEAS.map((l, i) => (
      <text
        key={l + trazo}
        x={500}
        y={22 + CEO_SIZE * 0.71 + i * CEO_PASO}
        textAnchor="middle"
        fontFamily={SANS}
        fontSize={CEO_SIZE}
        fontWeight={800}
        letterSpacing={`${BETWEEN.trackingCaps}em`}
        fill={trazo ? C.beige : C.cafe}
        stroke={trazo ? C.beige : 'none'}
        strokeWidth={trazo ? 14 : 0}
        strokeLinejoin="round"
        strokeLinecap="round"
      >
        {l}
      </text>
    ));
  return (
    <svg width={1000} height={alto} style={{overflow: 'visible'}}>
      {capa(true)}
      {capa(false)}
    </svg>
  );
};

const TXT_CEO = {size: 36, peso: 600, color: C.cafe} as const;

export const StOct01Ganador: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: '#dfc9bb'}}>
    <FotoFondo src={F + 's-ganador.jpg'} oscurecer={0} />
    <LogoCafe />
    <Columna top={411}>
      <div
        style={{
          transform: 'rotate(-3deg)',
          backgroundColor: C.cafe,
          color: C.beige,
          fontFamily: SANS,
          fontWeight: 800,
          fontSize: BETWEEN.tipos.cajaDato,
          padding: '12px 34px 14px',
          lineHeight: 1,
        }}
      >
        VACANTE CERRADA
      </div>
      <div style={{height: 28}} />
      <TituloCeo />
      <Texto {...TXT_CEO} style={{marginTop: 22}}>
        Felicidades
      </Texto>
      <div style={{height: ZONA_MENCION.alto + 14}} />
      <Texto {...TXT_CEO}>Te ganaste</Texto>
      <div style={{marginTop: 14, display: 'flex'}}>
        <CajaDato style={{backgroundColor: C.beige, color: C.cafe}}>1 MES DE CAFÉ GRATIS</CajaDato>
      </div>
      {/* Ronda cliente 28-09 (grilla col C): «falta algo que diga que lo
          contactaremos para entregarle información sobre su premio». Va en el
          nivel del premio (aire corto) y el cierre se separa más (R-38).
          Hilo de Nicolás 01-10 (STORIES!C12): «Cambiemos el texto de abajo por
          este → Te contactaremos por interno con la información de tu premio.»
          Sin punto final (regla Hilton) y el corte antes de «con». */}
      <Texto {...TXT_CEO} style={{marginTop: 16}}>
        {'Te contactaremos por interno\ncon la información de tu premio'}
      </Texto>
      <Texto {...TXT_CEO} style={{marginTop: 30}}>
        Gracias a todos por participar
      </Texto>
    </Columna>
    {guia ? <ZonaReservada zona={ZONA_MENCION} etiqueta={'MENCIÓN @usuario\n460 × 96'} /> : null}
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   02-10 · ST ANIMADA — PROMOS TO GO EN POV

   Referencia: mano con el café sobre la vereda, «¿Qué te hace feliz? Yo:».
   Toma: fotograma generado con el vaso To Go VIGENTE (sesión 09-09) y el muffin
   REAL (M313) como referencias, animado con Seedance 2.5 en el Space «Between
   octubre» (Kling 2.1 falló). El vaso trae el logotipo impreso → SIN lockup.
   Dos tiempos, como pide el brief («Luego entra:»):
     0–3,3 s  ¿QUÉ MEJORA TU MAÑANA?
   ⭐ Ronda cliente 28-09 (grilla col D): «Está rara esa forma de llevar el café
   con muffin arriba (desproporcionado, muffin muy chico) … más natural y en
   proporciones. Eliminemos el Yo:». Toma r2 (`s-togo-pov-r2.mp4`): cada mano
   lleva lo suyo — vaso en la derecha, muffin en su papel tulipa en la
   izquierda — a escala real; Nano Banana Pro 4K (logo «BƎTWEEN» revisado al
   300 %) animado con Kling 2.5 Pro. Fuera el «Yo:».
     3,3–8 s  CAFÉ + DULCE TO GO · Desde $2.990 · Muffin, brownie… · horario
   ⚠️ El brief escribe «$2,990» con coma; en pesos chilenos el separador es el
   punto (la misma grilla escribe «$1.990» en el feed). Va «$2.990» y se avisa.
   ══════════════════════════════════════════════════════════════════════════ */
export const DURACION_TOGO_POV = 240;
const ZONA_CARTA_POV: Zona = {ancho: 300, alto: 140, top: 1330, left: 735};

const entra = (frame: number, desde: number, dur = 12) =>
  interpolate(frame, [desde, desde + dur], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });

export const StOct02ToGoPov: React.FC<{guia?: boolean; capa?: boolean}> = ({guia = false, capa = false}) => {
  useFuentesListas();
  const frame = useCurrentFrame();
  const a = entra(frame, 6) * (1 - entra(frame, 92, 10));
  const b1 = entra(frame, 102);
  const b2 = entra(frame, 114);
  const b3 = entra(frame, 126);
  const b4 = entra(frame, 138);
  const sube = (t: number) => ({opacity: t, transform: `translateY(${(1 - t) * 24}px)`});
  return (
    <AbsoluteFill style={{backgroundColor: capa ? 'transparent' : C.sombra}}>
      {capa ? null : <OffthreadVideo src={staticFile(F + 's-togo-pov-r2.mp4')} muted style={{width: 1080, height: 1920}} />}
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(180deg, rgba(36,26,18,0.34) 0%, rgba(36,26,18,0.16) 30%, rgba(36,26,18,0) 42%)',
        }}
      />
      {/* ⭐ RONDA CONSTANZA 29-09 (grilla col D): «¿qué mejora tu mañana?, menos
          interlineado» → el kit mide la tinta con el «¿» que baja y la tilde de la «Ñ»
          que sube; con −0,2 el aire VISIBLE entre mayúsculas bajó de ~55 a ~25 px.
          Eli 29-09: «demasiado junto, la Ñ muy cerca de la M y la E» → −0,08 (~12 px más). */}
      <Columna top={256}>
        <div style={sube(a)}>
          <TitularBetween
            caps={'¿Qué mejora\ntu mañana?'}
            aireEntreCapsProp={-0.08}
            sizeCaps={100}
            tono="beige"
            alinear="centro"
            anchoDisponible={BETWEEN.bloque.columna}
          />
        </div>
      </Columna>
      <Columna top={330}>
        <div style={sube(b1)}>
          <TitularBetween
            caps="Café + dulce To Go"
            sizeCaps={100}
            tono="beige"
            alinear="centro"
            anchoDisponible={BETWEEN.bloque.columna}
          />
        </div>
        <div style={{...sube(b2), marginTop: BETWEEN.aire.tituloACaja, display: 'flex'}}>
          <CajaDato>DESDE $2.990</CajaDato>
        </div>
        {/* ⭐ RONDA CONSTANZA 29-09: «Muffin, brownie…» del MISMO tamaño que la
            caja del horario, y la letra un poco más grande en proporción,
            manteniendo su variante (SemiBold, caja baja). Las dos cajas se
            estiran al ancho de la más larga (el horario). */}
        <div style={{display: 'flex', flexDirection: 'column', alignItems: 'stretch'}}>
          <div style={{...sube(b3), marginTop: BETWEEN.cajas.gap, display: 'flex'}}>
            <CajaDato size={41} style={{textTransform: 'none', fontWeight: 600, flex: 1}}>Muffin, brownie, vigilantes u otros</CajaDato>
          </div>
          <div style={{...sube(b4), marginTop: BETWEEN.cajas.gap, display: 'flex'}}>
            <CajaDato size={38} style={{flex: 1}}>LUNES A VIERNES · 08:00 A 10:00 HRS</CajaDato>
          </div>
        </div>
      </Columna>
      {guia ? <ZonaReservada zona={ZONA_CARTA_POV} etiqueta={'STICKER\nLINK CARTA\n300 × 140'} /> : null}
    </AbsoluteFill>
  );
};

/* ══════════════════════════════════════════════════════════════════════════
   05-10 · ST ESTÁTICA — PASO POR UN CAFÉ Y… (collage de cuatro)

   Cuatro FOTOS REALES de la sesión de modelos 25-jul-2025 y de platos de
   enero, más UNA escena generada donde no hay material permitido:
     · COWORK  → M107 (taza blanca en mano, notebook; logo HP borrado)
     · DULCE   → Between-28, croissants (la taza KIMBO queda FUERA del recorte)
     · ATENCIÓN → generada: sólo MANOS del barista entregando la taza. En
       estáticos NO se enfoca a los trabajadores (regla de Javier).
     · CONVERSA → M17, dos amigas en la terraza.
   La frase protagonista va en la cruz del collage, en tarjeta beige con el
   logotipo café: el lockup no puede ir arriba porque ahí cae la costura.
   Cada razón en dos niveles: «Me quedo por» liviano + la razón en caja taupe.
   ══════════════════════════════════════════════════════════════════════════ */
const Bloque: React.FC<{
  src: string;
  x: number;
  y: number;
  posicion?: string;
}> = ({src, x, y, posicion = 'center'}) => (
  <Img
    src={staticFile(src)}
    style={{
      position: 'absolute',
      left: x,
      top: y,
      width: 540,
      height: 960,
      objectFit: 'cover',
      objectPosition: posicion,
    }}
  />
);

const Razon: React.FC<{x: number; top: number; razon: string}> = ({x, top, razon}) => (
  <div style={{position: 'absolute', left: x, width: 540, top, display: 'flex', justifyContent: 'center'}}>
    <div
      style={{
        backgroundColor: BETWEEN.cajas.fondo,
        borderRadius: BETWEEN.cajas.radio,
        padding: '14px 30px 16px',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: 6,
      }}
    >
      <div style={{fontFamily: SANS, fontWeight: 500, fontSize: 26, color: C.beige, lineHeight: 1}}>Me quedo por</div>
      <div style={{fontFamily: SANS, fontWeight: 800, fontSize: 32, color: C.beige, lineHeight: 1, whiteSpace: 'nowrap'}}>
        {razon}
      </div>
    </div>
  </div>
);

const ZONA_CARTA_COLLAGE: Zona = {ancho: 300, alto: 140, top: 1100};

export const StOct05PasoPorUnCafe: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: C.beige}}>
    <Bloque src={F + 'c-cowork.jpg'} x={0} y={0} posicion="40% 62%" />
    <Bloque src={F + 'c-dulce.jpg'} x={540} y={0} posicion="55% 60%" />
    <Bloque src={G + 'gen-05-10a.jpg'} x={0} y={960} posicion="50% 45%" />
    <Bloque src={F + 'c-conversa.jpg'} x={540} y={960} posicion="45% 40%" />
    {/* costuras beige */}
    <div style={{position: 'absolute', left: 536, top: 0, width: 8, height: 1920, backgroundColor: C.beige}} />
    <div style={{position: 'absolute', left: 0, top: 956, width: 1080, height: 8, backgroundColor: C.beige}} />

    {/* ⭐ RONDA 2 (Eli): las razones de abajo SUBEN —«la atención» tapaba la taza—
        y de la frase salen FLECHAS a cada una. */}
    <Razon x={0} top={680} razon="SU COWORK" />
    <Razon x={540} top={680} razon="ALGO DULCE" />
    <Razon x={0} top={1150} razon="LA ATENCIÓN" />
    <Razon x={540} top={1150} razon="UNA BUENA CONVERSA" />
    <svg width={1080} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
      <Flecha d="M 330 868 Q 300 830 285 792" />
      <Flecha d="M 750 868 Q 780 830 795 792" />
      <Flecha d="M 330 1052 Q 300 1098 285 1140" />
      <Flecha d="M 750 1052 Q 780 1098 795 1140" />
    </svg>

    {/* la frase, en la cruz */}
    <div
      style={{
        position: 'absolute',
        left: 150,
        width: 780,
        top: 872,
        height: 176,
        backgroundColor: C.beige,
        borderRadius: 20,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        boxShadow: '0 10px 30px rgba(36,26,18,0.28)',
      }}
    >
      <Img src={staticFile('assets/hilton/between/logo-cafe-marca.png')} style={{width: 170, marginBottom: 14}} />
      <div style={{fontFamily: SANS, fontWeight: 800, fontSize: 60, color: C.cafe, lineHeight: 1, letterSpacing: '-0.01em'}}>
        PASO POR UN CAFÉ Y…
      </div>
    </div>
    {guia ? <ZonaReservada zona={ZONA_CARTA_COLLAGE} etiqueta={'STICKER LINK CARTA\n300 × 140'} /> : null}
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   07-10 · HISTORIA — CAFÉ GRATIS POR CUMPLEAÑOS

   Referencia: bebida con una vela ondulada encendida y una polaroid. Escena
   generada con el vaso To Go vigente como referencia: vela en la tapa,
   polaroid con corazón SIN escritura. El vaso firma → SIN lockup.
   Registro: script Brushwell «Un regalo» + caja alta, el de las piezas de
   cumpleaños aprobadas.
   ══════════════════════════════════════════════════════════════════════════ */
const AIRE_REGALO = -4;
export const StOct07Cumple: React.FC<{src?: string}> = ({src = G + 'gen-07-10-final.jpg'}) => (
  <AbsoluteFill style={{backgroundColor: C.sombra}}>
    <FotoFondo src={src} oscurecer={0.06} />
    {/* ⭐ RONDA CONSTANZA 29-09 (grilla col H): «mucho interlineado en el llamado
        principal y lo de ven por tu café» → la script baja sobre la caja alta
        (la cola de la «g» entra al aire de la mayúscula, como en la ref) y la
        bajada pasa de 1,4 a 1,12 de interlínea. */}
    <Columna top={300}>
      <TitularBetween
        script="Un regalo"
        caps="en tu día"
        aireScriptATitulo={AIRE_REGALO}
        tono="beige"
        alinear="centro"
        anchoDisponible={BETWEEN.bloque.columna}
      />
      <Bajada size={42} style={{marginTop: BETWEEN.aire.tituloABajada, lineHeight: 1.12, textAlign: 'center', whiteSpace: 'pre-line', fontWeight: 500}}>
        {'Ven por tu café gratis\nel día de tu cumpleaños'}
      </Bajada>
      {/* el legal sube al bloque: al bajar la escena, el vaso ocupa la mesa del pie */}
      <div
        style={{
          marginTop: 22,
          width: 700,
          textAlign: 'center',
          fontFamily: SANS,
          fontStyle: 'italic',
          fontSize: 24,
          lineHeight: 1.35,
          color: C.beige,
          opacity: 0.92,
          textShadow: SOMBRA,
        }}
      >
        *Válido de lunes a viernes desde las 08:00 a 22:00, el mismo día de tu cumpleaños,
        presentando tu carnet al momento de solicitarlo.
      </div>
    </Columna>
    <Ilustra cual="globosPar" x={40} y={700} ancho={230} opacidad={0.85} />
    {/* ⭐ HILO NICOLÁS 29-09 (STORIES!H13): «Agreguemos a la Polaroid "Happy
        Birthday" con el corazoncito al lado». Escrito a mano en el margen blanco
        de la polaroid, girado con ella (−9,8°, medido sobre el borde de la foto
        interior) y en tinta que multiplica sobre el papel. */}
    <div
      style={{
        position: 'absolute',
        left: POLA.x,
        top: POLA.y,
        transform: `translate(-50%, -50%) rotate(${POLA.giro}deg)`,
        display: 'flex',
        alignItems: 'center',
        gap: 6,
        whiteSpace: 'nowrap',
        mixBlendMode: 'multiply',
      }}
    >
      <span style={{fontFamily: BETWEEN.fuentes.script, fontSize: POLA.size, lineHeight: 1, color: '#3a2c24'}}>
        Happy Birthday
      </span>
      <svg width={POLA.corazon} height={POLA.corazon} viewBox="0 0 24 22" style={{marginTop: 14}}>
        <path d="M12 21 C5 15 1 11 1 6.5 C1 3.4 3.4 1 6.4 1 C8.6 1 10.6 2.3 12 4.3 C13.4 2.3 15.4 1 17.6 1 C20.6 1 23 3.4 23 6.5 C23 11 19 15 12 21 Z" fill="#c8102e" />
      </svg>
    </div>
    {/* ⚖️ HILO NICOLÁS 29-09: «Agregar el legal "Imagen referencial" abajito».
        Mismo legal que las ST de S4/S5 de septiembre (beige, cursiva, 28, sombra
        suave), pero al margen IZQUIERDO: al centro caería encima del vaso. */}
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        bottom: BETWEEN.bloque.margenX,
        fontFamily: SANS,
        fontStyle: 'italic',
        fontWeight: BETWEEN.pesos.regular,
        fontSize: 28,
        lineHeight: 1,
        color: C.beige,
        opacity: 0.9,
        textShadow: '0 2px 16px rgba(36,26,18,0.75)',
      }}
    >
      *Imagen referencial.
    </div>
  </AbsoluteFill>
);
/** Centro del margen inferior de la polaroid en lienzo de 1080, medido sobre el máster 2250:
 *  punto medio entre el borde de la foto interior (−11,3°) y el canto del papel (−10,3°).
 *  Ronda 7 (Eli): «mejora la posición con respecto a la polaroid y que sea al centro». */
const POLA = {x: 801.5, y: 1874.5, giro: -10.8, size: 24, corazon: 15};

/* ══════════════════════════════════════════════════════════════════════════
   08-10 · HISTORIA — TRIVIA BETWEEN

   Referencia: mochila de línea blanca llena de emojis sobre rojo con rayos. En
   Between: el VASO To Go dibujado en línea beige (grosor constante, puntas
   redondas — la excepción del manual cuando el brief pide ilustración) lleno de
   emojis, con UNO solo repetido (el 🥐, dos veces). Fondo café de marca con
   rayos: lo «vibrante» sale del contraste, no de un color fuera de paleta.
   ⚠️ Emojis: Noto Color Emoji de Google (licencia libre), no los de Apple de las
   piezas de Eli — no se pueden redistribuir y la trivia necesita 30.
   Comentario de diseño: «se propuso lo mismo para QB, pero ok para Between».
   ══════════════════════════════════════════════════════════════════════════ */
const EMOJIS = [
  '2615', '1f369', '1f9c1', '1f36a', '1f96f', '1f370',
  '1f382', '1f36b', '1f950', '1f9c7', '1f95e', '1f353',
  '1f34b', '1f951', '1f35e', '1f49b', '2b50', '1f60d',
  '1f90e', '1f389', '1f96a', '1f373', '1f95b', '1f950',
  '1f375', '1f36e', '1f95c', '1f9c3', '1f60b', '1f33b',
];
const ZONA_PREGUNTAS: Zona = {ancho: 660, alto: 150, top: 1330};

export const StOct08Trivia: React.FC<{guia?: boolean}> = ({guia = false}) => {
  // vaso: cuerpo trapecio (arriba 470, abajo 380), tapa encima
  const cx = 540;
  const top = 830;
  const bot = 1300;
  const wTop = 480;
  const wBot = 390;
  const cuerpo = `M ${cx - wTop / 2} ${top} L ${cx + wTop / 2} ${top} L ${cx + wBot / 2} ${bot} Q ${cx + wBot / 2} ${bot + 14} ${cx + wBot / 2 - 16} ${bot + 14} L ${cx - wBot / 2 + 16} ${bot + 14} Q ${cx - wBot / 2} ${bot + 14} ${cx - wBot / 2} ${bot} Z`;
  const cols = 5;
  const tam = 76;
  return (
    <AbsoluteFill
      style={{
        background: `repeating-conic-gradient(from 0deg at 50% 62%, #6f6251 0deg 7.5deg, ${C.cafe} 7.5deg 15deg)`,
      }}
    >
      <AbsoluteFill
        style={{background: 'radial-gradient(circle at 50% 62%, rgba(103,91,73,0) 0%, rgba(58,47,35,0.55) 85%)'}}
      />
      <LogoBetween formato="story" posicion="arriba" tono="beige" />
      <Columna top={420}>
        {/* ⭐ RONDA 2 (Eli, 24-09): «que sea en beige, en Raleway, no en mayúscula,
            normal» — el registro de la referencia («¿Puedes encontrar el emoji
            repetido?»): una sola familia, caja baja, sin Brushwell. */}
        <Texto size={46} peso={600} sombra>
          Trivia Between
        </Texto>
        <Texto size={70} peso={700} sombra style={{marginTop: 8, lineHeight: 1.08, letterSpacing: '-0.01em'}}>
          {'Encuentra el\nemoji repetido'}
        </Texto>
      </Columna>
      <svg width={1080} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
        <defs>
          <clipPath id="vaso">
            <path d={cuerpo} />
          </clipPath>
        </defs>
        <g clipPath="url(#vaso)">
          {EMOJIS.map((c, i) => {
            const fila = Math.floor(i / cols);
            const col = i % cols;
            const x = cx - (cols * 88) / 2 + col * 88 + 6 + (fila % 2 ? 22 : -10);
            const y = top + 28 + fila * 76;
            return (
              <image
                key={i}
                href={staticFile(F + `emoji/u${c}.png`)}
                x={x}
                y={y}
                width={tam}
                height={tam}
                transform={`rotate(${((i * 37) % 30) - 15} ${x + tam / 2} ${y + tam / 2})`}
              />
            );
          })}
        </g>
        <path d={cuerpo} fill="none" stroke={C.beige} strokeWidth={6} strokeLinejoin="round" />
        {/* tapa */}
        <rect x={cx - wTop / 2 - 26} y={top - 44} width={wTop + 52} height={44} rx={14} fill="none" stroke={C.beige} strokeWidth={6} />
        <path d={`M ${cx - wTop / 2 + 10} ${top - 44} Q ${cx - wTop / 2 + 30} ${top - 92} ${cx - wTop / 2 + 80} ${top - 92} L ${cx + wTop / 2 - 80} ${top - 92} Q ${cx + wTop / 2 - 30} ${top - 92} ${cx + wTop / 2 - 10} ${top - 44}`} fill="none" stroke={C.beige} strokeWidth={6} strokeLinecap="round" />
      </svg>
      {guia ? <ZonaReservada zona={ZONA_PREGUNTAS} etiqueta={'CAJA DE PREGUNTAS\n660 × 190'} /> : null}
      <Columna top={1478}>
        <Texto size={36} peso={600} sombra>
          {'El primero en acertar\ngana un premio sorpresa'}
        </Texto>
      </Columna>
    </AbsoluteFill>
  );
};

/* ══════════════════════════════════════════════════════════════════════════
   19-10 · ST ESTÁTICA — COWORK

   La mesa y el espacio son REALES: el cowork del 2.º piso (IMG_8539), editado
   con Nano Banana para sumar notebook sin marca, libreta, lápiz y taza blanca
   total. Referencia «Coffee Break»: POV de la mesa de trabajo.
   Registro: caja BAJA en Raleway SemiBold (fuera de la fórmula script + caps).
   ══════════════════════════════════════════════════════════════════════════ */
export const StOct19Cowork: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: C.sombra}}>
    {/* ⭐ El tercio de arriba se PARTE: cielo raso claro arriba, cortinas oscuras
        a los costados desde y≈430. Ni beige ni café se leen en todo el ancho, así
        que el texto va DENTRO de un cuadro de vidrio beige con el fondo
        difuminado — el recurso que Eli aprobó en la ST del 30-09. */}
    <FotoFondo src={G + 'gen-19-10b.jpg'} oscurecer={0.04} />
    {/* RONDA 3 (Eli): «el logo bórralo, porque no se ve» — la pieza va sin lockup.
        ⭐ RONDA 4 (Eli): «la tipografía igual a la ref». La de «Coffee Break.» es un
        bloque ALINEADO A LA IZQUIERDA: rótulo chico con pin de ubicación arriba,
        titular muy pesado en caja normal con interlínea cerrada, y una línea de
        dato chica debajo separada por una barra. Todo claro sobre la parte oscura
        de arriba → velo sólo en ese tercio, como el muro de la referencia. */}
    <AbsoluteFill
      style={{background: 'linear-gradient(180deg, rgba(36,26,18,0.62) 0%, rgba(36,26,18,0.5) 26%, rgba(36,26,18,0) 46%)'}}
    />
    <div style={{position: 'absolute', left: 84, top: 300, width: 912}}>
      <div style={{display: 'flex', alignItems: 'center', gap: 12}}>
        <svg width={26} height={34} viewBox="0 0 26 34">
          <path d="M13 1C6.4 1 1 6.2 1 12.7 1 21.4 13 33 13 33s12-11.6 12-20.3C25 6.2 19.6 1 13 1z" fill={C.beige} />
          <circle cx={13} cy={12.5} r={4.6} fill={C.sombra} />
        </svg>
        <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 30, color: C.beige, textShadow: SOMBRA}}>
          Between Coffee &amp; Bar
        </div>
      </div>
      <div
        style={{
          marginTop: 18,
          fontFamily: SANS,
          fontWeight: 800,
          fontSize: 104,
          lineHeight: 1.0,
          letterSpacing: '-0.025em',
          color: C.beige,
          whiteSpace: 'pre-line',
          textShadow: SOMBRA,
        }}
      >
        {'Tu escritorio\nde hoy puede\nverse así'}
      </div>
      <div style={{marginTop: 26, display: 'flex', alignItems: 'center', gap: 18}}>
        <div style={{width: 4, height: 40, backgroundColor: C.beige, borderRadius: 2}} />
        <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 34, color: C.beige, textShadow: SOMBRA}}>
          WiFi + café + un espacio para trabajar
        </div>
      </div>
    </div>
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   20-10 · ST ESTÁTICA — LO DICEN USTEDES

   Cenital REAL (Between-20) extendida a 9:16 con aire alrededor de la taza.
   Tarjetas tipo review de la referencia: crema, estrellas en taupe, texto café.
   ⚠️ Los cuatro textos son los EJEMPLOS DE TONO del brief («solo como referencia
   para luego reemplazar por reviews reales»). Van provisorios y se avisa: hay
   que pedir las reseñas reales antes de publicar.
   ══════════════════════════════════════════════════════════════════════════ */
const Review: React.FC<{x: number; y: number; texto: string; rot?: number}> = ({x, y, texto, rot = 0}) => (
  <div
    style={{
      position: 'absolute',
      left: x,
      top: y,
      width: 430,
      padding: '24px 28px 26px',
      backgroundColor: C.beige,
      borderRadius: 22,
      boxShadow: '0 12px 30px rgba(20,12,6,0.35)',
      transform: `rotate(${rot}deg)`,
    }}
  >
    <div style={{fontSize: 30, letterSpacing: 4, color: C.cafe, lineHeight: 1}}>★★★★★</div>
    <div style={{marginTop: 12, fontFamily: SANS, fontWeight: 600, fontSize: 31, lineHeight: 1.28, color: C.cafe}}>
      {texto}
    </div>
  </div>
);

export const StOct20LoDicen: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: C.sombra}}>
    <FotoFondo src={G + 'gen-20-10.jpg'} oscurecer={0.12} />
    <LogoBetween formato="story" posicion="arriba" tono="beige" sombra={0.22} />
    <Review x={86} y={420} texto="«Mi lugar favorito para trabajar con un café»" rot={-2} />
    <Review x={562} y={625} texto="«Siempre vuelvo por la atención»" rot={2} />
    <Review x={86} y={1090} texto="«Buen café y un espacio donde dan ganas de quedarse»" rot={1.5} />
    <Review x={562} y={1290} texto="«Perfecto para una pausa o una reunión»" rot={-2} />
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        top: 1480,
        textAlign: 'center',
        fontFamily: SANS,
        // ⭐ 30-09 (reglas nuevas, R-140 de Constanza): sin itálica suelta y el
        // mismo peso que el texto de las tarjetas; sobre la madera, SemiBold.
        fontWeight: 600,
        fontSize: 36,
        lineHeight: 1.3,
        color: C.beige,
        textShadow: SOMBRA,
        whiteSpace: 'pre-line',
      }}
    >
      {'Gracias por hacer de Between\nparte de sus días'}
    </div>
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   27-10 · ST ESTÁTICO — ¿BUSCAS UN ESPACIO PARA TU PRÓXIMO EVENTO?

   Foto REAL: M139, grupo en la terraza (sesión de modelos 25-jul-2025).
   El texto vive en el toldo, sobre las caras NO: las caras arrancan en y≈770.
   Interacción: «CTA: Cotiza tu evento con nosotros» + «Enlace a web eventos
   Between» → es el sticker de enlace: zona reservada, con el texto del CTA
   anotado en la guía.
   ══════════════════════════════════════════════════════════════════════════ */
const ZONA_EVENTO: Zona = {ancho: 560, alto: 130, top: 1420};

export const StOct27Eventos: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: C.sombra}}>
    <FotoFondo src={G + 'gen-27-10d.jpg'} oscurecer={0.06} />
    <AbsoluteFill
      style={{background: 'linear-gradient(180deg, rgba(36,26,18,0.35) 0%, rgba(36,26,18,0) 36%)'}}
    />
    <LogoBetween formato="story" posicion="arriba" tono="beige" sombra={0.22} />
    {/* ⭐ RONDA 2: la foto nueva trae las persianas detrás del titular —franjas
        claras y oscuras— y ninguna tinta se lee suelta: panel taupe translúcido
        con el fondo difuminado. */}
    <div
      style={{
        position: 'absolute',
        left: 84,
        width: 912,
        top: 420,
        padding: '40px 36px 42px',
        borderRadius: 36,
        backgroundColor: 'rgba(103,91,73,0.86)',
        backdropFilter: 'blur(7px)',
        WebkitBackdropFilter: 'blur(7px)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <TitularBetween
        caps={'¿Buscas un espacio\npara tu próximo evento?'}
        sizeCaps={72}
        aireEntreCapsProp={0.1}
        tono="beige"
        alinear="centro"
        anchoDisponible={840}
      />
      <Texto size={40} peso={600} style={{marginTop: 20}}>
        Tenemos el lugar perfecto
      </Texto>
    </div>
    {guia ? (
      <ZonaReservada zona={ZONA_EVENTO} etiqueta={'STICKER DE ENLACE · web eventos\n«Cotiza tu evento con nosotros»'} />
    ) : null}
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   28-10 · ST ESTÁTICO — DESAYUNO BONJOUR

   El croissant de jamón y queso es REAL (Between-42 sin KIMBO), extendido a
   9:16 con luz de mañana. Referencia: la HORA gigante arriba («07:50») y una
   flecha de línea que señala el plato con su nombre. Acá la hora es la del
   brief, 08:00, y la flecha es la de la plancha de Eli.
   ══════════════════════════════════════════════════════════════════════════ */
const BONJOUR_CAJA = 560;
const ZONA_CARTA_BONJOUR: Zona = {ancho: 300, alto: 140, top: 1420, left: 690};

export const StOct28Bonjour: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: C.sombra}}>
    <FotoFondo src={G + 'gen-28-10.jpg'} oscurecer={0.05} />
    {/* la taza blanca de atrás cae bajo «las buenas mañanas»: velo sólo arriba */}
    <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(36,26,18,0.45) 0%, rgba(36,26,18,0.35) 40%, rgba(36,26,18,0) 55%)'}} />
    <LogoBetween formato="story" posicion="arriba" tono="beige" sombra={0.22} />
    <Columna top={400}>
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 800,
          fontSize: 250,
          lineHeight: 0.9,
          color: C.beige,
          letterSpacing: '-0.02em',
          fontVariantNumeric: 'lining-nums tabular-nums',
          textShadow: SOMBRA,
        }}
      >
        08:00
      </div>
      <div style={{height: 26}} />
      <TitularBetween
        caps={'Así parten\nlas buenas mañanas'}
        sizeCaps={74}
        aireEntreCapsProp={0.1}
        tono="beige"
        alinear="centro"
        anchoDisponible={BETWEEN.bloque.columna}
      />
      <Bajada size={40} style={{marginTop: BETWEEN.aire.tituloABajada, textAlign: 'center', whiteSpace: 'pre-line', fontWeight: 600}}>
        {'Desayuno Bonjour\npara comenzar el día'}
      </Bajada>
    </Columna>
    {/* ⭐ RONDA 2 (Eli): «la flecha, igual a la referencia, más fluida, más bonita,
        con un poco más de grosor y que no tape los textos» → un solo trazo con un
        rulo, como el de «07:50», que sale del costado de la bajada y baja al
        croissant sin cruzar ninguna línea de texto. */}
    <svg width={1080} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
      <Flecha
        grosor={9}
        punta={30}
        d="M 830 900 C 960 915 975 1015 895 1030 C 830 1042 835 975 885 990 C 945 1008 900 1095 790 1140"
      />
    </svg>
    <div style={{position: 'absolute', left: 0, right: 0, top: 1440, display: 'flex', justifyContent: 'center'}}>
      <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 10}}>
        {/* ⭐ 30-09 (R-144): las dos cajas de la pila, del MISMO ancho.
            Y el «11» sale de la caja tabular: dos «1» seguidos quedaban cada uno
            centrado en su caja y se leía «1 1:30». Va proporcional con lnum. */}
        <CajaDato size={40} style={{width: BONJOUR_CAJA}}>DESAYUNOS BETWEEN</CajaDato>
        <CajaDato size={40} style={{width: BONJOUR_CAJA}}>
          <span style={{display: 'inline-flex', alignItems: 'baseline', whiteSpace: 'pre'}}>
            {conCifras('08:00 A ', BETWEEN.pesos.extrabold)}
            <span style={{...CIFRAS_ALTAS}}>11</span>
            {conCifras(':30 HRS', BETWEEN.pesos.extrabold)}
          </span>
        </CajaDato>
      </div>
    </div>
    {guia ? <ZonaReservada zona={ZONA_CARTA_BONJOUR} etiqueta={'STICKER\nLINK CARTA\n300 × 140'} /> : null}
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   FEED 05-10 · ESTÁTICO — ESA REUNIÓN PODRÍA SER UN CAFÉ

   Foto REAL: M104, dos amigas con notebook y café en el lounge. Del cuadro se
   borraron el televisor y el logo HP (edición con Nano Banana sobre la foto).
   Referencia: dos manos brindando con tazas sobre dos notebooks.
   ══════════════════════════════════════════════════════════════════════════ */
export const FeedOct05Reunion: React.FC<{src?: string}> = ({src = G + 'gen-f05-10d.jpg'}) => (
  <AbsoluteFill style={{backgroundColor: C.sombra}}>
    <FotoFondo src={src} oscurecer={0.1} />
    <AbsoluteFill
      style={{background: 'linear-gradient(180deg, rgba(36,26,18,0.4) 0%, rgba(36,26,18,0) 34%)'}}
    />
    <LogoBetween formato="feed" posicion="arriba" tono="beige" sombra={0.22} />
    <Columna top={BETWEEN.bloque.yFeed + 40}>
      <TitularBetween
        script="Reúnete en Between"
        caps={'y dale otro aire\na tu jornada'}
        sizeCaps={78}
        tono="beige"
        alinear="centro"
        anchoDisponible={BETWEEN.bloque.columna}
      />
      {/* ⭐ RONDA 29-09 (Eli): la bajada se solapaba con los notebooks abajo → sube
          bajo «a tu jornada»; la «y» queda arriba («…en Between y»), un poco más
          gruesa y más grande. */}
      {/* ⭐ RONDA 29-09 b (Eli): el relleno beige de las letras lleva además un
          contorno café de marca, delgado y sutil, «estilo lifestyle».
          RONDA 29-09 c: «un poco más» de trazo y sin puntas cuadradas → va en SVG,
          porque -webkit-text-stroke une en inglete (picos en la M, la A, la v) y
          no deja redondear. Trazo de 5 px por DETRÁS del relleno (paint-order):
          asoman 2,5 px, con uniones y remates redondos. */}
      <svg
        width={1000}
        height={112}
        style={{marginTop: BETWEEN.aire.tituloABajada, overflow: 'visible', filter: 'drop-shadow(0 2px 8px rgba(36,26,18,0.6))'}}
      >
        {['Encuentra tu mesa en Between y', 'cambia la sala de reuniones por algo mejor'].map((linea, i) => (
          <text
            key={linea}
            x={500}
            y={38 + i * 47.5}
            textAnchor="middle"
            fontFamily={SANS}
            fontSize={38}
            fontWeight={700}
            fill={C.beige}
            stroke={C.cafe}
            strokeWidth={5}
            strokeLinejoin="round"
            strokeLinecap="round"
            paintOrder="stroke fill"
          >
            {linea}
          </text>
        ))}
      </svg>
    </Columna>
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   FEED 14-10 · ESTÁTICO — ESPACIOS BETWEEN

   Foto REAL: M68, el lounge con los sillones de cuero y la barra al fondo.
   Referencia: foto lifestyle con un dibujo de línea encima. Comentario de la
   grilla: «Que sea sutil la ilustración» → trazos de la plancha de Eli, chicos,
   al 70 %, apoyados en el FONDO y nunca sobre las personas.
   ══════════════════════════════════════════════════════════════════════════ */
export const FeedOct14Espacios: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: C.sombra}}>
    {/* ⭐ RONDA 3 (Eli): «oscurece un poco el fondo para que la ilustración se note,
        sólo un poco, como una transparencia» y el titular en BEIGE. El velo parejo
        hace leer la línea blanca; el degradado de arriba, que el beige se lea sobre
        la tela clara del techo. Con el velo el logo café dejaba de leerse, así que
        pasa a beige junto con el titular. */}
    <FotoFondo src={G + 'gen-f14-10b.jpg'} oscurecer={0.2} />
    <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(36,26,18,0.42) 0%, rgba(36,26,18,0.3) 22%, rgba(36,26,18,0) 40%)'}} />
    {/* ⭐ RONDA 4 (Eli): «que la ilustración quede ARRIBA de la transparencia y
        engruesa muy poquito». El dibujo se aisló de la foto por contraste local
        (trazo claro, fino y sin saturación) y va como capa propia sobre el velo,
        engrosado ~2 px a 2250. */}
    <Img src={staticFile(G + 'f14-lineas.png')} style={{position: 'absolute', left: 0, top: 0, width: 1080, height: 1350}} />
    <LogoBetween formato="feed" posicion="arriba" tono="beige" sombra={0.22} />
    <Columna top={BETWEEN.bloque.yFeed + 40}>
      <TitularBetween
        caps={'Espacios que invitan\na quedarse'}
        sizeCaps={84}
        aireEntreCapsProp={0.2}
        tono="beige"
        alinear="centro"
        anchoDisponible={BETWEEN.bloque.columna}
      />
      {/* la bajada cae sobre el muro verde: en caja taupe (regla del cliente) */}
      <div
        style={{
          marginTop: 20,
          backgroundColor: BETWEEN.cajas.fondo,
          borderRadius: BETWEEN.cajas.radio,
          padding: '14px 34px 16px',
        }}
      >
        {/* ⭐ 30-09 (R-118): la bajada del feed se tiene que leer → Bold 38.
            Eli r9: el titular «muy junto» con 0,1 → 0,2; y el corte «…y buenos» /
            «momentos en Between» (el anterior «se veía extraño»). */}
        <Texto size={38} peso={700}>
          {'Café, comodidad y buenos\nmomentos en Between'}
        </Texto>
      </div>
    </Columna>
  </AbsoluteFill>
);

/* ══════════════════════════════════════════════════════════════════════════
   FEED 01-10 · CARRUSEL — PROMOS TO GO (4 láminas)

   Grilla col E, OK PARA DISEÑAR 30-09. Hilo Scarlette → Nicolás: «ajustar
   carrusel con info de PROMOS TO GO» (ya ajustado en el brief). Comentario de
   diseño: «propuesta nueva […] el último carrusel es reciclado», «mismo formato
   que el diseño que subimos ahora último, pero con diseño actualizado (respetar
   la misma info de cada slide)» y «si usamos IA ver que las proporciones de los
   vasos y las comidas sean adecuadas».
   Ref (Pinterest «NON COFFE IS READY»): los vasos en fila y un rótulo con su
   nombre SOBRE cada uno → acá el rótulo es tamaño + precio.

   Escenas: Nano Banana Pro con los tres vasos aprobados por Eli el 22-09 (ya a
   escala real 0,712/0,861/1) y la comida de la sesión 25-jul-2025 como
   referencia (`scripts/between-oct-generar.py`, claves fd01-*). La 4 es la «a»
   con el vigilante borrado por edición (4e): se leía como mini croissant.

   Sistema (reglas vigentes S3+): 3 voces Raleway (R-140) — TITULAR 800 versales
   84 con aire 0,2 (R-156) · CAJA 800 para precios, todas del mismo ancho (R-144),
   cifras tabulares (R-45) · TEXTO 700/38 (R-118) para bajada, rótulos y horario.
   Sin lockup: el vaso firma (R-33). Sin Brushwell (R-36: sólo portada, y acá la
   portada ya es producto). Sin punto final. Legal «*Imágenes referenciales.»
   como en el carrusel anterior, porque hay producto generado.
   ══════════════════════════════════════════════════════════════════════════ */
const TOGO_CAJA = 210;
const TOGO_PRECIOS = {
  cafe: ['$1.990', '$2.790', '$2.990'],
  sandwich: ['$3.490', '$4.290', '$4.490'],
  dulce: ['$2.990', '$3.790', '$3.990'],
  tres: ['$4.490', '$5.290', '$5.490'],
} as const;
// Eli 30-09: «antes de Mediano, etc., va "Café"»
const TAMANOS = ['Café Mediano', 'Café Grande', 'Café XL'] as const;

/** Rótulo de un tamaño: nombre en TEXTO y precio en CAJA (ancho fijo, R-144). */
const RotuloPrecio: React.FC<{nombre: string; precio: string}> = ({nombre, precio}) => (
  <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 8}}>
    <Texto size={38} peso={700} sombra>
      {nombre}
    </Texto>
    <CajaDato size={44} style={{width: TOGO_CAJA}}>
      <span style={{display: 'inline-flex', alignItems: 'baseline', whiteSpace: 'pre'}}>
        {conCifras(precio, BETWEEN.pesos.extrabold)}
      </span>
    </CajaDato>
  </div>
);

const FilaPrecios: React.FC<{precios: readonly string[]; top: number}> = ({precios, top}) => (
  <div style={{position: 'absolute', top, left: 0, right: 0, display: 'flex', justifyContent: 'center', gap: 16}}>
    {/* columnas del MISMO ancho: con «Café Mediano» más largo, el gap parejo corría los ejes */}
    {TAMANOS.map((t, i) => (
      <div key={t} style={{width: 270, display: 'flex', justifyContent: 'center'}}>
        <RotuloPrecio nombre={t} precio={precios[i]} />
      </div>
    ))}
  </div>
);

/**
 * Eli 30-09: «flechitas como guía visual, igual a la referencia, una de las
 * primeras» → la flecha PUNTEADA con un rulo que baja del titular al primer
 * rótulo de la ref, y las rayitas de acento («///») junto a otro. Trazo beige
 * punteado de remate redondo; la punta, sólida, sigue la tangente del final.
 */
const FlechaPunteada: React.FC<{d: string}> = ({d}) => {
  const n = d.replace(/[A-Za-z]/g, ' ').trim().split(/[\s,]+/).map(Number);
  const [x2, y2] = [n[n.length - 2], n[n.length - 1]];
  const [x1, y1] = [n[n.length - 4], n[n.length - 3]];
  const ang = Math.atan2(y2 - y1, x2 - x1);
  const ala = (s: number) => `${x2 - 20 * Math.cos(ang + s * 0.55)} ${y2 - 20 * Math.sin(ang + s * 0.55)}`;
  const base = {fill: 'none', stroke: C.beige, strokeWidth: 4.5, strokeLinecap: 'round' as const, strokeLinejoin: 'round' as const};
  return (
    <g style={{filter: 'drop-shadow(0 2px 4px rgba(36,26,18,0.55))'}}>
      <path d={d} style={{...base, strokeDasharray: '2 13'}} />
      <path d={`M ${ala(1)} L ${x2} ${y2} L ${ala(-1)}`} style={base} />
    </g>
  );
};

/**
 * Las tres rayitas de acento de la ref, en abanico desde (x, y).
 * Eli 30-09 r3 (con un recorte de muestra): «más grandes y mejor diseñadas» →
 * CUÑAS, no líneas: finas en la punta que mira al producto y anchas con corte
 * recto afuera. La del centro, un poco más larga; esquinas apenas suavizadas
 * con un trazo del mismo color.
 */
const Acento: React.FC<{x: number; y: number; giro?: number; escala?: number}> = ({x, y, giro = 0, escala = 1}) => {
  const cuna = (largo: number, ancho: number) => {
    const g = 12; // aire entre el vértice común y el nacimiento de cada cuña
    return `M -1.5 ${-g} L 1.5 ${-g} L ${ancho / 2} ${-g - largo} L ${-ancho / 2} ${-g - largo} Z`;
  };
  return (
    <g
      transform={`translate(${x} ${y}) rotate(${giro}) scale(${escala})`}
      style={{filter: 'drop-shadow(0 2px 5px rgba(36,26,18,0.55))'}}
    >
      {[
        {a: -44, largo: 44, ancho: 17},
        {a: 0, largo: 56, ancho: 19},
        {a: 44, largo: 44, ancho: 17},
      ].map((r) => (
        <path
          key={r.a}
          d={cuna(r.largo, r.ancho)}
          transform={`rotate(${r.a})`}
          fill={C.beige}
          stroke={C.beige}
          strokeWidth={2.5}
          strokeLinejoin="round"
        />
      ))}
    </g>
  );
};

const CapaFlechas: React.FC<{children: React.ReactNode}> = ({children}) => (
  <svg width={1080} height={1350} style={{position: 'absolute', left: 0, top: 0}}>
    {children}
  </svg>
);

const LegalReferencial: React.FC = () => (
  <div style={{position: 'absolute', right: 60, bottom: 34}}>
    <Texto size={20} peso={500} sombra>
      *Imágenes referenciales.
    </Texto>
  </div>
);

/** Velo de arriba para el titular y de abajo para el horario; la foto no se oscurece (R-42). */
const VelosToGo: React.FC<{pie?: boolean}> = ({pie = true}) => (
  <>
    <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(36,26,18,0.42) 0%, rgba(36,26,18,0.25) 26%, rgba(36,26,18,0) 42%)'}} />
    {pie ? (
      <AbsoluteFill style={{background: 'linear-gradient(0deg, rgba(36,26,18,0.55) 0%, rgba(36,26,18,0.3) 9%, rgba(36,26,18,0) 17%)'}} />
    ) : null}
  </>
);

const TituloToGo: React.FC<{caps: string; top?: number}> = ({caps, top = 96}) => (
  <Columna top={top}>
    <TitularBetween
      caps={caps}
      sizeCaps={84}
      aireEntreCapsProp={0.2}
      tono="beige"
      alinear="centro"
      anchoDisponible={BETWEEN.bloque.columna}
    />
  </Columna>
);

/**
 * ⭐ RONDA CLIENTE 01-10 (grilla FEED E15): «Acá falta una slide de introducción, como lo
 * hemos hecho anteriormente, donde vaya la info de horarios y esas cosas. En la G2 se
 * elimina la info de horarios y en la G4 debemos poner logo Between a la bolsa […] debe ser
 * con logo actual».
 *  · Lámina 0 nueva: la introducción lleva el horario (como la portada del carrusel de
 *    septiembre). Sólo textos que ya estaban en el brief: «Promos To Go» y el horario.
 *  · El horario sale de las láminas de producto (en septiembre vivía sólo en la portada).
 *  · La bolsa es la BLANCA que usa el local (foto del cliente en la grilla) con el
 *    logotipo vigente calzado en café de marca (`scripts/bw-fd-01-10-bolsa-logo.py`).
 *
 * Eli 01-10 (r16), después de probar las cinco sobre fotos reales de la sesión To Go: «no lograste un
 * buen resultado en las fotos del carrusel; más como las del inicio, déjalas así, sólo la portada y
 * la última ajústalas». Las láminas del medio vuelven a las escenas aprobadas el 30-09 (1-a, 2-a,
 * 3-a) con los comentarios del cliente; portada = mano con café destapado (0h-b); última = café XL
 * + bolsa blanca con logo (n5).
 */
export const FeedOct01ToGo0: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: C.sombra}}>
    <FotoFondo src={G + 'gen-fd01-0m-logo.jpg'} oscurecer={0.04} />
    <VelosToGo pie={false} />
    <TituloToGo caps="Promos to go" />
    <Columna top={96 + 84 + 26}>
      <Texto size={38} peso={700} sombra>
        De lunes a viernes
      </Texto>
      <div style={{marginTop: 14, display: 'flex'}}>
        <CajaDato size={44}>
          <span style={{display: 'inline-flex', alignItems: 'baseline', whiteSpace: 'pre'}}>
            {conCifras('De 8:00 a 10:00 hrs', BETWEEN.pesos.extrabold)}
          </span>
        </CajaDato>
      </div>
    </Columna>
    <LegalReferencial />
  </AbsoluteFill>
);

/** 1 · TU CAFÉ TO GO — cada precio sobre su vaso, como los rótulos de la ref. */
export const FeedOct01ToGo1: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: C.sombra}}>
    <FotoFondo src={G + 'gen-fd01-1-a.jpg'} oscurecer={0.04} />
    <VelosToGo pie={false} />
    <TituloToGo caps="Tu café to go" />
    {/* Eli 30-09: «que centre según cada vaso» → eje = centro de la TAPA, medido
        con regla sobre el render a 1080×1350 (antes 205/488/770, corridos) */}
    {[
      // Eli 30-09 r6 (línea roja sobre la portada): Mediano y Grande «chocaban» con
      // su tapa → los tres rótulos a la MISMA altura que el del XL (top 374)
      // Eli 01-10 (r17): sin la línea de horarios quedó un hueco bajo el título → los
      // rótulos suben. r18 (su captura con la franja roja sobre las láminas 2–4): NO a la
      // altura del horario de la portada sino a la de la FILA DE PRECIOS de las láminas 3 y 4
      // (`FilaPrecios top={290}`), para que la secuencia quede pareja
      {x: 225, tope: 436},
      {x: 531, tope: 436},
      {x: 844, tope: 436},
    ].map((v, i) => (
      <div key={i} style={{position: 'absolute', left: v.x - 150, width: 300, top: v.tope - 146, display: 'flex', justifyContent: 'center'}}>
        <RotuloPrecio nombre={TAMANOS[i]} precio={TOGO_PRECIOS.cafe[i]} />
      </div>
    ))}
    {/* como la ref: del titular baja la punteada con rulo al primer rótulo; acento junto al último */}
    <CapaFlechas>
      {/* Eli 30-09 r5, con su garabato en rojo sobre la portada: cada flecha SALE DEL
          PRECIO, hace un rulo sobre la tapa y ENTRA al vaso. Su captura venía recortada
          distinto, así que el trazo se calcó RELATIVO a cada caja, tapa y vaso
          (Mediano: caja 120–330 × 598–664, tapa desde 690 · Grande: caja 426–636 ×
          526–592, tapa desde 618 · XL: caja 739–949 × 428–494, tapa desde 520). */}
      {/* r19 (Eli: «las flechas más arriba, junto; no importa si no están cerca de los cafés,
          sólo que apunten») → cortas (~90 px), pegadas bajo cada caja de precio, con un rulo
          chico y la punta hacia su vaso. r20: «se ven muy cortas ahora» → el doble de largo
          (~180 px, de 424 a 606) y el rulo más amplio. Reemplaza lo de la r18: */}
      {/* r18 (Eli: «las flechas se ven muy largas»): ya no nacen en la caja del precio; son
          cortas y parejas, parten ~110–130 px sobre cada tapa, y el rulo sobre la tapa y la
          entrada al vaso quedan donde estaban */}
      <FlechaPunteada d="M 225 424 C 241 468 233 512 199 522 C 153 534 143 474 181 472 C 217 470 237 536 225 606" />
      <FlechaPunteada d="M 531 424 C 515 468 523 512 557 522 C 603 534 613 474 575 472 C 539 470 519 536 531 606" />
      <FlechaPunteada d="M 844 424 C 828 468 836 512 870 522 C 916 534 926 474 888 472 C 852 470 832 536 844 606" />
      <Acento x={930} y={288} giro={48} />
    </CapaFlechas>
    <LegalReferencial />
  </AbsoluteFill>
);

/** 2 · CAFÉ + SÁNDWICH */
export const FeedOct01ToGo2: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: C.sombra}}>
    <FotoFondo src={G + 'gen-fd01-2-a.jpg'} oscurecer={0.04} />
    <VelosToGo pie={false} />
    <TituloToGo caps={'Café + sándwich'} />
    <Columna top={96 + 84 + 26}>
      <Texto size={38} peso={700} sombra>
        Ave Palta o Jamón Queso
      </Texto>
    </Columna>
    <FilaPrecios precios={TOGO_PRECIOS.sandwich} top={290} />
    <LegalReferencial />
  </AbsoluteFill>
);

/** 3 · CAFÉ + OPCIÓN DULCE */
export const FeedOct01ToGo3: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: C.sombra}}>
    <FotoFondo src={G + 'gen-fd01-3-a.jpg'} oscurecer={0.04} />
    <VelosToGo pie={false} />
    <TituloToGo caps={'Café + opción dulce'} />
    <Columna top={96 + 84 + 26}>
      <Texto size={38} peso={700} sombra>
        Vigilantes · Muffin · Brownie · Otros
      </Texto>
    </Columna>
    <FilaPrecios precios={TOGO_PRECIOS.dulce} top={290} />
    <CapaFlechas>
      <Acento x={1005} y={752} giro={40} />
    </CapaFlechas>
    <LegalReferencial />
  </AbsoluteFill>
);

/** 4 · CAFÉ + SÁNDWICH + DULCE — la más abundante */
export const FeedOct01ToGo4: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: C.sombra}}>
    {/* Eli 01-10 (r21): «ajusta la bolsa, no se parece a la de la portada» → la MISMA bolsa de la
        portada (vertical, asas de papel torcido paradas, punta a ~419; r22 un 10 % más grande), pegada a medida y detrás del
        muffin (`scripts/bw-fd-01-10-bolsa-portada.py`); el resto de la foto son los píxeles de la n5 */}
    <FotoFondo src={G + 'gen-fd01-n6-logo.jpg'} oscurecer={0.04} />
    <VelosToGo pie={false} />
    <TituloToGo caps={'Café + sándwich\n+ dulce'} />
    {/* la caja del XL rozaba el borde de la bolsa (tope ~457) → la fila sube a 300;
        01-10: con la bolsa blanca las asas llegan a ~417 → sube a 284 */}
    <FilaPrecios precios={TOGO_PRECIOS.tres} top={284} />
    <CapaFlechas>
      {/* Eli 01-10: café XL a la izquierda de la bolsa → el acento va sobre su tapa, sin tocar la bolsa */}
      <Acento x={214} y={566} giro={-34} />
    </CapaFlechas>
    <LegalReferencial />
  </AbsoluteFill>
);

/* variantes GUÍA — llevan dibujada la zona del sticker. No se entregan al cliente. */
export const StOct01GanadorGuia: React.FC = () => <StOct01Ganador guia />;
export const StOct02ToGoPovGuia: React.FC = () => <StOct02ToGoPov guia />;
/** Sólo la capa de texto, con alfa: se monta sobre la toma con ffmpeg (remotion.exe bloqueado). */
export const StOct02ToGoPovCapa: React.FC = () => <StOct02ToGoPov capa />;
export const StOct02ToGoPovCapaGuia: React.FC = () => <StOct02ToGoPov capa guia />;
export const StOct05PasoPorUnCafeGuia: React.FC = () => <StOct05PasoPorUnCafe guia />;
export const StOct08TriviaGuia: React.FC = () => <StOct08Trivia guia />;
export const StOct27EventosGuia: React.FC = () => <StOct27Eventos guia />;
export const StOct28BonjourGuia: React.FC = () => <StOct28Bonjour guia />;
