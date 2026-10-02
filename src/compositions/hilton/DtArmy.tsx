/**
 * DOUBLETREE · CAMPAÑA ARMY (02-10-2026) — KV de post 4:5 de la PREVENTA «Tarifa ARMY».
 * ST y paid se adaptan cuando Eli elija el KV; la línea de VENTA quedó en pausa («omite por ahora venta»).
 *
 * Encargo de Eli por chat: «estilo cyber DT, pero claramente se tiñe de morado»; la foto aérea del
 * tarjetón con el hotel «morado army». Los TEXTOS salen del brief de contenido (grilla DT octubre,
 * hoja FEED, fila 10, «POST 1 — PREVENTA "TARIFA ARMY"»), actualizado el 02-10 con «Antes $185.000»
 * e «IVA INCLUIDO».
 *
 * El molde es el Cyber DT de mayo (`F:\Paid Hilton 2026\CYBER HILTON 2026 MAYO`, `CYBER HOTEL post n°1`):
 * titular en versales Stag · el sello a dos voces («CYBER / Day» → «PREVENTA / Tarifa ARMY») · la
 * fecha entre dos filetes → el PRECIO entre dos filetes · la barra del pie → el correo.
 *
 * ── RONDA 2 ── centrado, sin destellos ni panel lateral («no es como los programas normales»),
 *   ciudad en negro con el hotel morado y más zoom, «que destaque preventa».
 * ── RONDA 3 ── titular en dos líneas y entero en lila; un poco de tracking; «ANTES $185.000»
 *   tachado + IVA INCLUIDO; lo que incluye abajo y con ícono; opción 2 con la habitación de DOS
 *   CAMAS y el degradado del Cyber en un solo morado, sin luces («parecen de motel»).
 * ── RONDA 4 (Eli, 02-10) ──────────────────────────────────────────────────────────────────────
 * · «Está demasiado desenfocada la imagen… sólo un poquito, cosa que se note lo de detrás, o si no
 *   netamente quítalo» → el desenfoque del panel baja de 8 a 1,5 px.
 * · «baja un poco el color morado de arriba de la transparencia para que se pueda notar más el
 *   moradito de ese texto» → α de arriba 0,34 → 0,22; el titular gana sombra.
 * · «el CTA todavía se ve extraño… moradito con un degradado, bien estilo cyber y letras blancas» →
 *   la barra deja de ser lila con texto oscuro: es morada en degradado, con filete y letras blancas.
 * · «preventa está demasiado grueso» → Stag Bold → SemiBold.
 * · «se ve mucho texto, la idea es que se vea lo menos posible» → «para 2 personas · IVA incluido»
 *   en UNA línea bajo la cifra, y el tercer incluido resumido (⚠️ es resumen mío del brief: avisado).
 * · «mejora un poco la calidad de los íconos» → redibujados, en medallón.
 * · Opción 1: «mejores un poco la diagramación y que se vea más atractivo» → menos alto de texto
 *   arriba, el hotel con más aire y haces de luz morada, la fecha en cápsula, lo que incluye en fila.
 * · Opción 2: «unos morados más army, unos detalles de BTS podría ser» → la foto, no la gráfica.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';
import {Stag, TRADE_CN} from './dtOct2';

cargarFuentesDT();

const BLANCO = DT.colores.blanco;
const NEGRO = '#07050F';
/**
 * RONDA 7 (Eli): «unifica los colores morados de los textos y el logo… el color que utilices que sea el
 * mismo que se utilizó para el hotel». Medido en la foto (`hotel-morado.jpg`): todo el edificio está en
 * tono 270°, saturación ≈ 0,77; la cara iluminada es #9639F4 y el tono medio #7F32CE.
 * · MORADO  — la cara iluminada: textos y logo sobre negro.
 * · MORADO_MEDIO — el mismo tono, un punto más oscuro: texto sobre el botón blanco (variante `blanco`, hoy sin uso).
 */
const MORADO = '#9639F4';
const MORADO_MEDIO = '#7F32CE';
const FILETE = 'linear-gradient(90deg, rgba(255,255,255,0.45) 0%, #FFFFFF 50%, rgba(255,255,255,0.45) 100%)';
const SOMBRA = '0 3px 10px rgba(7,5,15,0.6), 0 0 2px rgba(7,5,15,0.5)';
/** La sombra de los textos. En la habitación va en 'none' (Eli, ronda 5: «no hagas esas sombras en los textos»). */
const Sombra = React.createContext<string>(SOMBRA);
/**
 * La tinta del texto. Por defecto la pieza es oscura (texto blanco, «Tarifa ARMY» con la textura
 * metálica). RONDA 8 (Eli): el recuadro de la habitación pasa a BLANCO, así que ahí el texto va en
 * negro y lo que era lila/blanco de acento va en el morado del hotel.
 */
type TintaT = {texto: string; filete: string; aro: string; divisor: string; script: string | null; tacha: string};
const TINTA_OSCURA: TintaT = {texto: BLANCO, filete: FILETE, aro: 'rgba(255,255,255,0.8)', divisor: 'rgba(255,255,255,0.32)', script: null, tacha: '#9639F4'};
// RONDA 9 (Eli): «los textos no en negro sino en azul DT o morado en la op. 2» → azul DoubleTree (#09194E),
// que es el color de la marca y deja el morado del hotel como acento (logo, titular, «Tarifa ARMY», tachado).
const TINTA_CLARA: TintaT = {texto: DT.colores.azul, filete: 'rgba(9,25,78,0.55)', aro: 'rgba(9,25,78,0.75)', divisor: 'rgba(9,25,78,0.25)', script: '#9639F4', tacha: '#9639F4'};
const Tinta = React.createContext<TintaT>(TINTA_OSCURA);

export type Linea = 'preventa' | 'venta';
type Icono = 'cama' | 'taza' | 'copa';

const LINEAS: Record<Linea, {
  titulo: [string, string];
  sello: string;
  script: string;
  antes?: string;
  precio: string;
  bajoPrecio: string;
  fecha: string;
  incluye: {icono: Icono; l: string[]}[];
  legal: string;
}> = {
  preventa: {
    titulo: ['DOUBLETREE', 'SE VISTE DE MORADO'],
    sello: 'PREVENTA',
    script: 'Tarifa ARMY',
    antes: '$185.000',
    precio: '$115.000',
    bajoPrecio: 'PARA 2 PERSONAS · IVA INCLUIDO',
    // Eli, 02-10: «es para fechas de 16 y 17 de octubre, no más fechas» (coincide con el brief)
    fecha: 'Noches del 16 y 17 de octubre',
    incluye: [
      {icono: 'cama', l: ['Habitación', 'para 2']},
      {icono: 'taza', l: ['Desayuno', 'buffet']},
      // ⚠️ brief: «Experiencia pre o post concierto en QB Restaurant con 2 tragos». Resumido por el
      // pedido de Eli de «lo menos posible» de texto; el texto completo va en el copy del post.
      {icono: 'copa', l: ['2 tragos en', 'QB Restaurant']},
    ],
    legal: '*Preventa válida del 5 al 11 de octubre. Habitación Standard o Doble, sujeta a disponibilidad.',
  },
  // VENTA: Eli, 02-10 «omite por ahora venta». Queda con el texto del brief, sin rendir ni revisar.
  venta: {
    titulo: ['TU NOCHE DE CONCIERTO', 'EMPIEZA AQUÍ'],
    sello: 'TARIFA',
    script: 'ARMY',
    antes: '$185.000',
    precio: '$135.000',
    bajoPrecio: 'PARA 2 PERSONAS · IVA INCLUIDO',
    fecha: 'Noches del 15, 16 y 17 de octubre',
    incluye: [
      {icono: 'cama', l: ['Habitación', 'para 2']},
      {icono: 'taza', l: ['Desayuno', 'buffet']},
      {icono: 'copa', l: ['2 tragos + 1 entrada', 'en QB Restaurant']},
    ],
    legal: '*Válido para reservas del 12 al 17 de octubre. Habitación Standard o Doble, sujeta a disponibilidad.',
  },
};
const CORREO = 'reservas.dtv@hilton.com';
/** La dirección del hotel, como la escribe el brief en el copy del post («📍 Av. Vitacura 2727, Las Condes»). */
const DIRECCION = 'Av. Vitacura 2727, Las Condes';

// ── Las piezas ─────────────────────────────────────────────────────────────────────────────────

/**
 * Titular en versales Stag, dos líneas a UNA medida (R-05): «DOUBLETREE» a cuerpo 64 y «SE VISTE DE
 * MORADO» a 39,5 dan el mismo ancho (≈ 440 px con tracking 0,05 em, medido con la fuente). Todo en lila.
 */
const Titular: React.FC<{lineas: [string, string]; k?: number; color?: string}> = ({lineas, k = 1, color = MORADO}) => (
  <div style={{textAlign: 'center', color, textShadow: React.useContext(Sombra), fontFamily: DT.fuentes.titular, fontWeight: DT.pesos.medium, letterSpacing: '0.05em', whiteSpace: 'nowrap'}}>
    <div style={{fontSize: 64 * k, lineHeight: 1}}>{lineas[0]}</div>
    <div style={{marginTop: 5 * k, fontSize: 39.5 * k, lineHeight: 1, wordSpacing: '0.04em'}}>
      <Stag t={lineas[1]} />
    </div>
  </div>
);

/**
 * El sello «CYBER / Day». La script del «Day» no está en esta máquina y Kallimata (la que sí hay) es
 * de trazo fino: «Army» no se leía. Va en Stag Light Italic, que es como DT escribe el acento
 * manuscrito (E-09) y como el propio Cyber arma «Escapada / Romántica», con la textura metálica en lila.
 */
const Sello: React.FC<{palabra: string; script: string; cuerpo: number; peso?: number}> = ({palabra, script, cuerpo, peso = DT.pesos.semibold}) => {
  const sombra = React.useContext(Sombra);
  const tinta = React.useContext(Tinta);
  return (
  <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
    <div style={{fontFamily: DT.fuentes.titular, fontWeight: peso, fontSize: cuerpo, lineHeight: 1, letterSpacing: '0.06em', marginRight: '-0.06em', color: tinta.texto, textShadow: sombra, whiteSpace: 'nowrap'}}>
      {palabra}
    </div>
    <div
      style={{
        marginTop: -cuerpo * 0.1,
        fontFamily: DT.fuentes.titular,
        fontStyle: 'italic',
        fontWeight: DT.pesos.light,
        fontSize: cuerpo * 0.66,
        lineHeight: 1.08,
        letterSpacing: '0.035em',
        wordSpacing: '0.06em',
        padding: `0 ${cuerpo * 0.2}px`,
        whiteSpace: 'nowrap',
        ...(tinta.script
          ? {color: tinta.script}
          : {
              backgroundImage: `url(${staticFile('assets/hilton/dt/army/textura-lila.jpg')})`,
              backgroundSize: 'cover',
              WebkitBackgroundClip: 'text',
              backgroundClip: 'text',
              color: 'transparent',
            }),
        filter: sombra === 'none' ? undefined : 'drop-shadow(0 4px 6px rgba(7,5,15,0.55))',
      }}
    >
      {script}
    </div>
  </div>
  );
};

/**
 * «ANTES $…» tachado, y el precio entre dos filetes con «para 2 personas · IVA incluido» debajo.
 * RONDA 8 (Eli): «en las tres opciones necesito que el tachado sea con dos líneas, porque así
 * generalmente se hace» → dos trazos paralelos sobre la cifra, en el morado del hotel.
 */
const Precio: React.FC<{antes?: string; precio: string; bajo: string; cuerpo: number; ancho: number}> = ({antes, precio, bajo, cuerpo, ancho}) => {
  const tinta = React.useContext(Tinta);
  const trazo = Math.max(2.5, cuerpo * 0.03);
  return (
    <div style={{width: ancho, margin: '0 auto', textAlign: 'center', color: tinta.texto, textShadow: React.useContext(Sombra)}}>
      {antes ? (
        // RONDA 5: «el precio del antes tiene que ser un poquitito más grande» (0,34 → 0,43 del cuerpo de la cifra)
        <div style={{marginBottom: cuerpo * 0.13, fontFamily: TRADE_CN, fontWeight: 700, fontSize: cuerpo * 0.43, lineHeight: 1, letterSpacing: '0.05em', display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
          <span style={{marginRight: cuerpo * 0.11}}>ANTES</span>
          <span style={{position: 'relative'}}>
            {antes}
            <span style={{position: 'absolute', left: -6, right: -6, top: '31%', height: trazo, background: tinta.tacha}} />
            <span style={{position: 'absolute', left: -6, right: -6, top: '55%', height: trazo, background: tinta.tacha}} />
          </span>
        </div>
      ) : null}
      <div style={{height: 3, background: tinta.filete}} />
      <div style={{paddingTop: cuerpo * 0.16, fontFamily: TRADE_CN, fontWeight: 700, fontSize: cuerpo, lineHeight: 0.9, letterSpacing: '0.025em', whiteSpace: 'nowrap'}}>{precio}</div>
      {/* RONDA 5: «para dos personas más IVA incluido no se está notando mucho» → Trade Bold Cn y de 0,20 a 0,27 */}
      <div style={{padding: `${cuerpo * 0.06}px 0 ${cuerpo * 0.12}px`, fontFamily: TRADE_CN, fontWeight: 700, fontSize: cuerpo * 0.27, lineHeight: 1.1, letterSpacing: '0.09em', whiteSpace: 'nowrap'}}>{bajo}</div>
      <div style={{height: 3, background: tinta.filete}} />
    </div>
  );
};

/**
 * La fecha, texto suelto en Stag negrita. RONDA 7 (Eli): «quita en la 1 y en la 3 ese óvalo que
 * utilizaste en noches del 16 al 17 de octubre, que quede sin ese botón… y aumenta un poco el tamaño».
 */
const Fecha: React.FC<{t: string; cuerpo: number; color?: string}> = ({t, cuerpo, color}) => (
  <div style={{textAlign: 'center', fontFamily: DT.fuentes.titular, fontWeight: DT.pesos.semibold, fontSize: cuerpo, lineHeight: 1, letterSpacing: '0.025em', wordSpacing: '0.08em', color: color ?? React.useContext(Tinta).texto, textShadow: React.useContext(Sombra), whiteSpace: 'nowrap'}}>
    <Stag t={t} />
  </div>
);

/** Íconos de línea sobre caja de 48, trazo redondo: cama de perfil, taza con platillo, copa de cóctel. */
const ICONOS: Record<Icono, React.ReactNode> = {
  cama: (
    <>
      <path d="M6 13 V37" />
      <path d="M42 37 V27.5 a5.5 5.5 0 0 0 -5.5 -5.5 H22 V30" />
      <path d="M6 30 H42" />
      <rect x="10" y="22" width="9" height="6" rx="3" />
    </>
  ),
  taza: (
    <>
      <path d="M10 20 H33 V27 a9.5 9.5 0 0 1 -9.5 9.5 H19.5 A9.5 9.5 0 0 1 10 27 Z" />
      <path d="M33 22.5 H35.5 a4.2 4.2 0 0 1 0 8.4 H32.4" />
      <path d="M6 40.5 H37" />
      <path d="M17 15 c-1.6 -2 1.6 -3.4 0 -5.6 M24 15 c-1.6 -2 1.6 -3.4 0 -5.6" />
    </>
  ),
  copa: (
    <>
      <path d="M10 11 H38 L24 27 Z" />
      <path d="M24 27 V39.5" />
      <path d="M16.5 39.5 H31.5" />
      <path d="M15.3 17 H32.7" />
      <path d="M27 21 L35 7" />
    </>
  ),
};

/**
 * Lo que incluye: tres COLUMNAS iguales, el ícono en medallón arriba y el rótulo centrado debajo,
 * separadas por filetes. (Eli, 02-10: «los íconos me molestan mucho, la disposición como está, se
 * ven muy extraños los textos» — iban con el ícono a la izquierda y el texto partido al lado, cada
 * ítem con un ancho distinto.)
 */
const Incluye: React.FC<{items: {icono: Icono; l: string[]}[]; cuerpo: number; columna: number}> = ({items, cuerpo, columna}) => {
  const d = cuerpo * 2.5; // diámetro del medallón
  const sombra = React.useContext(Sombra);
  const tinta = React.useContext(Tinta);
  return (
    <div style={{display: 'flex', justifyContent: 'center', color: tinta.texto, textShadow: sombra}}>
      {items.map((it, i) => (
        <div
          key={it.icono}
          style={{width: columna, display: 'flex', flexDirection: 'column', alignItems: 'center', borderLeft: i ? `1.5px solid ${tinta.divisor}` : undefined, boxSizing: 'border-box'}}
        >
          <div
            style={{
              width: d,
              height: d,
              borderRadius: '50%',
              // RONDA 7 (Eli): «los íconos, para todos, quítale eso morado que tiene» → sin relleno ni contorno
              // morado: aro blanco fino y nada más
              border: `1.6px solid ${tinta.aro}`,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              boxSizing: 'border-box',
            }}
          >
            <svg width={d * 0.6} height={d * 0.6} viewBox="0 0 48 48" fill="none" stroke={tinta.texto} strokeWidth="2.3" strokeLinecap="round" strokeLinejoin="round">
              {ICONOS[it.icono]}
            </svg>
          </div>
          <div style={{marginTop: cuerpo * 0.42, textAlign: 'center', fontFamily: DT.fuentes.titular, fontWeight: DT.pesos.regular, fontSize: cuerpo, lineHeight: 1.18, letterSpacing: '0.02em', wordSpacing: '0.08em', whiteSpace: 'nowrap'}}>
            {it.l.map((x) => (
              <div key={x}>
                <Stag t={x} />
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};

const Legal: React.FC<{t: string; top: number; ancho: number}> = ({t, top, ancho}) => (
  <div
    style={{position: 'absolute', top, left: (1080 - ancho) / 2, width: ancho, textAlign: 'center', color: React.useContext(Tinta).texto, fontFamily: DT.fuentes.texto, fontSize: 19, lineHeight: 1.3, letterSpacing: '0.02em', textShadow: React.useContext(Sombra), opacity: 0.92}}
  >
    {t}
  </div>
);

/**
 * El botón del pie (la barra «MUY PRONTO» del Cyber). RONDA 5 (Eli, 02-10): «se ve muy falso el
 * CTA, tiene que verse más brilloso, más real… te voy a dejar el degradado, es metálico… no necesita
 * el ícono de correo, pero engrósalo el texto» → la placa se rellena con SU textura de metal morado
 * cepillado (`metal-morado.jpg`, tal cual la mandó), con canto claro arriba y oscuro abajo como una
 * placa real; sin ícono; el correo en Trade Bold Condensed.
 */
/**
 * RONDA 6 (Eli): «el botón, quítale eso blanco que tiene en los bordes… era algo similar a ese tipo de
 * degradado pero mejóralo, se está viendo muy extraño… los tres botones se ve parte blanca y eso se ve
 * muy mal… fíjate que se vea mejor centrado el texto, se ve muy abajo».
 * → Sin filetes ni reflejo blanco. El metal ya no es su imagen estirada (el cepillado se deformaba):
 *   es un degradado limpio con las mismas franjas de luz de su referencia (una brillante al 30 % y otra
 *   al 88 %), en sus mismos morados. El texto se centra por la TINTA (minúsculas sin descendentes: el
 *   centro óptico es el de la altura de x), medido en el render.
 * `blanco`: el de la habitación — «podría ser blanco con el texto morado».
 */
// RONDA 7: el metal pasa del magenta de la referencia al tono del hotel (270°), con las mismas franjas de luz.
const METAL =
  'linear-gradient(to bottom, rgba(255,255,255,0.07) 0%, rgba(255,255,255,0) 45%, rgba(14,4,30,0.3) 100%), ' +
  'linear-gradient(90deg, #2B0D4D 0%, #401470 9%, #7F32CE 22%, #A04DFA 31%, #7730C2 40%, #44167A 52%, #2D0E50 64%, #401470 76%, #7A30C8 88%, #4A1884 95%, #2F0F54 100%)';

const Boton: React.FC<{top: number; cuerpo?: number; blanco?: boolean}> = ({top, cuerpo = 40, blanco}) => (
  <div style={{position: 'absolute', top, left: 0, width: 1080, display: 'flex', justifyContent: 'center'}}>
    <div
      style={{
        height: cuerpo * 1.72,
        padding: `0 ${cuerpo * 1.2}px`,
        display: 'flex',
        alignItems: 'center',
        background: blanco ? '#FFFFFF' : METAL,
        borderRadius: 4,
        color: blanco ? MORADO_MEDIO : BLANCO,
        fontFamily: TRADE_CN,
        fontWeight: 700,
        fontSize: cuerpo,
        lineHeight: 1,
        letterSpacing: '0.055em',
        whiteSpace: 'nowrap',
        boxShadow: '0 10px 24px rgba(7,5,15,0.55), 0 2px 5px rgba(7,5,15,0.45)',
      }}
    >
      <span style={{display: 'block', transform: `translateY(${cuerpo * BOTON_DY}px)`}}>{CORREO}</span>
    </div>
  </div>
);
/** Corrección vertical del texto del botón, en em, para que la TINTA quede centrada (se mide en el render). */
const BOTON_DY = 0;

/**
 * La ubicación del hotel, bajo el correo. RONDA 10 (Eli, 02-10, ya aprobadas las tres): «olvidaste añadir
 * abajo del correo el texto de la ubicación del hotel, es muy importante».
 * Sobre negro va suelta, en blanco. `placa`: sobre la foto de la habitación va dentro de una placa del
 * mismo vidrio blanco del recuadro, en azul DT (lo chico sobre foto va dentro de una forma, R-136).
 */
const Direccion: React.FC<{top: number; placa?: boolean; cuerpo?: number}> = ({top, placa, cuerpo = 26}) => {
  const color = placa ? DT.colores.azul : BLANCO;
  return (
    <div style={{position: 'absolute', top, left: 0, width: 1080, display: 'flex', justifyContent: 'center'}}>
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          color,
          fontFamily: DT.fuentes.texto,
          fontSize: cuerpo,
          lineHeight: 1,
          letterSpacing: '0.04em',
          whiteSpace: 'nowrap',
          textShadow: placa ? undefined : SOMBRA,
          ...(placa ? {background: 'rgba(255,255,255,0.86)', borderRadius: 999, padding: `${cuerpo * 0.42}px ${cuerpo * 0.95}px ${cuerpo * 0.3}px`} : {}),
        }}
      >
        <svg width={cuerpo * 0.82} height={cuerpo * 1.02} viewBox="0 0 24 30" fill="none" stroke={color} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" style={{marginRight: cuerpo * 0.36, marginTop: -cuerpo * 0.16}}>
          <path d="M12 28 C5.5 19.5 2.5 15 2.5 11 a9.5 9.5 0 0 1 19 0 C21.5 15 18.5 19.5 12 28 Z" />
          <circle cx="12" cy="11" r="3.4" />
        </svg>
        {DIRECCION}
      </div>
    </div>
  );
};

/** `morado` = el logotipo blanco con la tinta del hotel (#9639F4); lo genera `scripts/dt-army-fotos.py`. */
const LOGOS = {blanco: 'assets/hilton/dt/logo-dt-blanco.png', morado: 'assets/hilton/dt/army/logo-dt-morado.png'} as const;
const LogoDT: React.FC<{top: number; ancho: number; tinta?: keyof typeof LOGOS}> = ({top, ancho, tinta = 'blanco'}) => (
  <Img
    src={staticFile(LOGOS[tinta])}
    style={{position: 'absolute', top, left: (1080 - ancho) / 2, width: ancho, height: ancho / DT.geometria.logoProporcion}}
  />
);

const Fila: React.FC<{top: number; children: React.ReactNode}> = ({top, children}) => (
  <div style={{position: 'absolute', top, left: 0, width: 1080}}>{children}</div>
);

// ═══════════════════════════════════════════════════════════════════════════════════════════════
// 1 · CIUDAD — la foto aérea: todo negro, el hotel morado y grande, el texto al eje
// ═══════════════════════════════════════════════════════════════════════════════════════════════
// La foto completa (4000×2247) se coloca por la CAJA del hotel (x 2122–2478 · y 949–1530).
const FOTO = {src: 'assets/hilton/dt/army/hotel-morado.jpg', w: 4000, h: 2247, cajaX: 2300, cajaY0: 949} as const;

/**
 * `variante="logo"` es la TERCERA opción (Eli, 02-10): «en la primera deja un poco más grande el
 * logo, quita la palabra DoubleTree y deja el logo morado. "Se viste de morado" que sea el título, y
 * "preventa tarifa army" se ve demasiado gruesa todavía y bájalo un poco». El logotipo hace de
 * primera línea del titular y va en lila; el sello baja a Stag Medium.
 *
 * RONDA 6 (Eli), opciones 1 y 3:
 * · «la idea es que se vea negro atrás y solamente el hotel morado» → fuera el resplandor y los haces
 *   morados: lo único con color en la foto es el hotel.
 * · «dejaste de lado la imagen de fondo y eso igual tiene que mostrarse más… se ven muy pegoteadas las
 *   transparencias» → UN velo negro parejo (α 0,70) bajo el texto de arriba, por el que se ve la ciudad,
 *   en vez de la escalera de transparencias; la cápsula de la fecha ya no lleva fondo traslúcido.
 * · «sube más la imagen del hotel, un poco más al centro, una parte donde quede como solo» → el bloque
 *   de arriba se compacta (termina en y ≈ 640) y la fecha baja con lo que incluye: entre y ≈ 660 y 985
 *   el hotel queda solo, sin nada encima.
 * · Opción 3: «"se viste de morado" está muy arriba, tienes que centrarlo entre el logo [y PREVENTA]…
 *   que se vea un poco más grande el logo, no se lee mucho el Santiago–Vitacura» → logo de 190 a 236 px
 *   y el título con el mismo aire arriba y abajo (30 px de versal a versal).
 */
export const DtArmyCiudad: React.FC<{linea: Linea; variante?: 'titular' | 'logo'}> = ({linea, variante = 'titular'}) => {
  const c = LINEAS[linea];
  const conLogo = variante === 'logo';
  const s = 0.9;
  const TECHO = conLogo ? 676 : 662; // y del techo del hotel en la pieza
  return (
    <AbsoluteFill style={{backgroundColor: NEGRO}}>
      <Img
        src={staticFile(FOTO.src)}
        style={{position: 'absolute', width: FOTO.w * s, height: FOTO.h * s, left: 540 - FOTO.cajaX * s, top: TECHO - FOTO.cajaY0 * s}}
      />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            // RONDA 7 (Eli): «esa transición de degradado de abajo, que sea más sutil: que de abajo sea más
            // negro y vaya cada vez con menos degradado» → el pie ya no cierra en una franja de 80 px: sube
            // parejo desde el borde (0,97) hasta desaparecer a media altura del hotel, en 560 px.
            'linear-gradient(to bottom, rgba(7,5,15,0.78) 0%, rgba(7,5,15,0.7) 12%, rgba(7,5,15,0.7) 43%, rgba(7,5,15,0.28) 48%, rgba(7,5,15,0) 52%, rgba(7,5,15,0) 58%, rgba(7,5,15,0.14) 63%, rgba(7,5,15,0.34) 68%, rgba(7,5,15,0.56) 73%, rgba(7,5,15,0.74) 78%, rgba(7,5,15,0.86) 84%, rgba(7,5,15,0.94) 91%, rgba(7,5,15,0.97) 100%)',
        }}
      />

      {conLogo ? (
        <>
          <LogoDT top={26} ancho={236} tinta="morado" />
          <Fila top={241}>
            <div style={{textAlign: 'center', color: MORADO, textShadow: SOMBRA, fontFamily: DT.fuentes.titular, fontWeight: DT.pesos.medium, fontSize: 46, lineHeight: 1, letterSpacing: '0.06em', wordSpacing: '0.04em', whiteSpace: 'nowrap'}}>
              {c.titulo[1]}
            </div>
          </Fila>
          <Fila top={295}>
            <Sello palabra={c.sello} script={c.script} cuerpo={96} peso={DT.pesos.medium} />
          </Fila>
          <Fila top={458}>
            <Precio antes={c.antes} precio={c.precio} bajo={c.bajoPrecio} cuerpo={90} ancho={470} />
          </Fila>
        </>
      ) : (
        <>
          <LogoDT top={38} ancho={124} />
          <Fila top={158}>
            <Titular lineas={c.titulo} k={0.72} />
          </Fila>
          <Fila top={252}>
            <Sello palabra={c.sello} script={c.script} cuerpo={104} />
          </Fila>
          <Fila top={436}>
            <Precio antes={c.antes} precio={c.precio} bajo={c.bajoPrecio} cuerpo={92} ancho={470} />
          </Fila>
        </>
      )}

      {/* el pie: fecha, lo que incluye, el botón y el legal, sobre el negro */}
      <Fila top={976}>
        {/* sin óvalo y más grande (28 → 37). RONDA 11 (Eli): «y noches en la op 3, ese texto a blanco» → en la
            opción 3 vuelve de morado a blanco, igual que en la 1 */}
        <Fecha t={c.fecha} cuerpo={37} />
      </Fila>
      <Fila top={1036}>
        <Incluye items={c.incluye} cuerpo={22} columna={290} />
      </Fila>
      <Boton top={1166} cuerpo={38} />
      <Direccion top={1246} />
      <Legal t={c.legal} top={1300} ancho={960} />
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════════════════════════════
// 2 · HABITACIÓN — el post del Cyber: foto a sangre y panel de cristal al centro
// ═══════════════════════════════════════════════════════════════════════════════════════════════
// Panel medido en `CYBER HOTEL post n°1` (@1080): x 152 · y 187 · 776 × 971 · filete blanco ≈ 5 px.
// Su degradado, medido comparando la franja del panel con la foto de afuera cada 50 px: arriba el
// azul va a α ≈ 0,30, al medio ≈ 0,6 y desde el 80 % es azul macizo.
const PANEL = {x: 152, y: 187, ancho: 776, alto: 971, radio: 38} as const;

export const DtArmyHabitacion: React.FC<{linea: Linea; foto?: string}> = ({linea, foto = 'assets/hilton/dt/army/habitacion-army-b.jpg'}) => {
  const c = LINEAS[linea];
  return (
    <AbsoluteFill style={{backgroundColor: NEGRO}}>
      <Img src={staticFile(foto)} style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover'}} />

      <div
        style={{
          position: 'absolute',
          left: PANEL.x,
          top: PANEL.y,
          width: PANEL.ancho,
          height: PANEL.alto,
          borderRadius: PANEL.radio,
          boxSizing: 'border-box',
          // RONDA 8 (Eli): «quitémosle definitivamente el morado que tiene, todo ese como transición… sólo que
          // quede como un desenfoque más sutil… podría ser todo como un blanco sutil, ese recuadro con un
          // poquito de opacidad… DoubleTree se viste de morado, o sea el mismo color que unificamos, para que
          // se note, e igual el logo sea morado… y el botón sea como el de las tres opciones».
          // → el recuadro es vidrio BLANCO (α 0,80, desenfoque 3 px): la habitación se adivina detrás. Logo y
          //   titular en el morado del hotel; el resto del texto en negro, con el morado sólo de acento
          //   («Tarifa ARMY» y el tachado). El botón es el metálico de las otras dos.
          border: '3px solid rgba(255,255,255,0.96)',
          background: 'rgba(255,255,255,0.8)',
          backdropFilter: 'blur(3px)',
          WebkitBackdropFilter: 'blur(3px)',
          boxShadow: '0 16px 50px rgba(7,5,15,0.3)',
        }}
      />

      <Sombra.Provider value="none">
        <Tinta.Provider value={TINTA_CLARA}>
          <LogoDT top={232} ancho={132} tinta="morado" />
          <Fila top={362}>
            <Titular lineas={c.titulo} k={0.76} />
          </Fila>
          <Fila top={462}>
            <Sello palabra={c.sello} script={c.script} cuerpo={104} />
          </Fila>
          <Fila top={644}>
            <Precio antes={c.antes} precio={c.precio} bajo={c.bajoPrecio} cuerpo={94} ancho={480} />
          </Fila>
          <Fila top={862}>
            <Fecha t={c.fecha} cuerpo={34} />
          </Fila>
          <Fila top={922}>
            <Incluye items={c.incluye} cuerpo={21} columna={226} />
          </Fila>
          {/* el legal va DENTRO del recuadro, al pie, como en las láminas de precio del Cyber */}
          <Legal t={c.legal} top={1084} ancho={650} />
        </Tinta.Provider>
      </Sombra.Provider>

      <Boton top={1176} cuerpo={38} />
      {/* RONDA 11 (Eli): «en la op 2, en texto blanco sin botón y queda» → fuera la placa blanca */}
      <Direccion top={1262} />
    </AbsoluteFill>
  );
};
