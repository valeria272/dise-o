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
/**
 * Eli, 02-10: «A toda la OP 2 añade el signo + en vez del punto: debe decir "+ IVA", sin "incluido"».
 * ⚠️ Sólo la opción 2 (post y sus tres adaptaciones). La opción 1 sigue con el texto del brief,
 * «PARA 2 PERSONAS · IVA INCLUIDO»: las dos opciones dicen cosas distintas sobre el precio (avisado a Eli).
 */
const BAJO_PRECIO_OP2 = 'PARA 2 PERSONAS + IVA';
/** La dirección del hotel, como la escribe el brief en el copy del post («📍 Av. Vitacura 2727, Las Condes»). */
const DIRECCION = 'Av. Vitacura 2727, Las Condes';

// ── Las piezas ─────────────────────────────────────────────────────────────────────────────────

/**
 * El sello «CYBER / Day». La script del «Day» no está en esta máquina y Kallimata (la que sí hay) es
 * de trazo fino: «Army» no se leía. Va en Stag Light Italic, que es como DT escribe el acento
 * manuscrito (E-09) y como el propio Cyber arma «Escapada / Romántica», con la textura metálica en lila.
 */
/** Ancho ÷ alto de `army-pincel.png` (2600 × 1330). */
const ARMY_PROPORCION = 2600 / 1330;
/** Cuánto se monta el rótulo «ARMY» sobre la línea de «PREVENTA», en cuerpos (el PNG trae aire arriba a la izquierda). */
const SELLO_MONTA = 0.12;
/**
 * RONDA 14 (Eli, 02-10): «quieren literal el army con el corazón. Y "Tarifa" déjalo en las tres más pequeño,
 * arriba de army. PREVENTA en los tres menos grueso».
 * · «ARMY» es el rótulo de la clienta, calcado, con su corazón y en su lila (`army-pincel.png`, lo arma
 *   `scripts/dt-army-fachada.py`). Sube hacia la derecha: la «Y» se mete bajo «PREVENTA», como en la maqueta.
 * · «Tarifa», en Stag Light Italic y chica, va arriba a la izquierda del rótulo, en el hueco que deja el
 *   arranque de la «A».
 * · «PREVENTA» baja de SemiBold / Medium a Regular.
 * `army` = alto del rótulo en cuerpos de «PREVENTA».
 */
const Sello: React.FC<{palabra: string; script: string; cuerpo: number; peso?: number; army?: number}> = ({palabra, script, cuerpo, peso = DT.pesos.regular, army = 1.9}) => {
  const sombra = React.useContext(Sombra);
  const tinta = React.useContext(Tinta);
  const resto = script.replace(/\s*ARMY$/, '');
  const alto = cuerpo * army;
  const ancho = alto * ARMY_PROPORCION;
  return (
  <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
    <div style={{fontFamily: DT.fuentes.titular, fontWeight: peso, fontSize: cuerpo, lineHeight: 1, letterSpacing: '0.06em', marginRight: '-0.06em', color: tinta.texto, textShadow: sombra, whiteSpace: 'nowrap'}}>
      {palabra}
    </div>
    <div style={{marginTop: -cuerpo * SELLO_MONTA, display: 'flex', alignItems: 'flex-start', justifyContent: 'center'}}>
      {resto ? (
        <div style={{marginTop: alto * 0.2, marginRight: -ancho * 0.1, fontFamily: DT.fuentes.titular, fontStyle: 'italic', fontWeight: DT.pesos.light, fontSize: cuerpo * 0.46, lineHeight: 1, letterSpacing: '0.035em', color: tinta.texto, textShadow: sombra, whiteSpace: 'nowrap'}}>
          {resto}
        </div>
      ) : null}
      <Img
        src={staticFile('assets/hilton/dt/army/army-pincel.png')}
        style={{height: alto, width: ancho, filter: sombra === 'none' ? undefined : 'drop-shadow(0 4px 6px rgba(7,5,15,0.55))'}}
      />
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
      <div style={{padding: `${cuerpo * 0.06}px 0 ${cuerpo * 0.12}px`, fontFamily: TRADE_CN, fontWeight: 700, fontSize: cuerpo * 0.27, lineHeight: 1.1, letterSpacing: '0.09em', whiteSpace: 'nowrap'}}>
        {/* Eli, 02-10: «el signo + céntralo entre el texto, se ve extraño» → el «+» de Trade Bold Cn se apoya en la
            línea de base y queda 0,115 em bajo el centro de las versales (medido en el render): se sube eso mismo.
            «Y el + más cerca un poco del IVA» → menos aire a su derecha que a su izquierda */}
        {bajo.split(' + ').map((t, i) => (
          <React.Fragment key={t}>
            {i ? <span style={{display: 'inline-block', margin: '0 0.16em 0 0.34em', transform: 'translateY(-0.115em)'}}>+</span> : null}
            {t}
          </React.Fragment>
        ))}
      </div>
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

const Legal: React.FC<{t: string; top: number; ancho: number; cuerpo?: number}> = ({t, top, ancho, cuerpo = 19}) => (
  <div
    style={{position: 'absolute', top, left: (1080 - ancho) / 2, width: ancho, textAlign: 'center', color: React.useContext(Tinta).texto, fontFamily: DT.fuentes.texto, fontSize: cuerpo, lineHeight: 1.3, letterSpacing: '0.02em', textShadow: React.useContext(Sombra), opacity: 0.92}}
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

// `plano` (ronda 14, opción 2): «así la dos mejor» [la maqueta] · «sin lo metálico» → morado liso, esquinas redondas.
const Boton: React.FC<{top: number; cuerpo?: number; blanco?: boolean; plano?: boolean}> = ({top, cuerpo = 40, blanco, plano}) => (
  <div style={{position: 'absolute', top, left: 0, width: 1080, display: 'flex', justifyContent: 'center'}}>
    <div
      style={{
        height: cuerpo * 1.72,
        padding: `0 ${cuerpo * 1.2}px`,
        display: 'flex',
        alignItems: 'center',
        background: blanco ? '#FFFFFF' : plano ? MORADO_MEDIO : METAL,
        borderRadius: plano ? 12 : 4,
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
  const TECHO = 738; // y del techo del hotel en la pieza (ronda 15: baja con el bloque del precio, que creció)
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
            // RONDA 15: el velo de arriba llega hasta el pie del precio (y ≈ 730) y el del pie parte bajo el techo del hotel
            'linear-gradient(to bottom, rgba(7,5,15,0.78) 0%, rgba(7,5,15,0.7) 12%, rgba(7,5,15,0.7) 50%, rgba(7,5,15,0.28) 54%, rgba(7,5,15,0) 57%, rgba(7,5,15,0) 61%, rgba(7,5,15,0.16) 65%, rgba(7,5,15,0.36) 69%, rgba(7,5,15,0.56) 73%, rgba(7,5,15,0.74) 78%, rgba(7,5,15,0.86) 84%, rgba(7,5,15,0.94) 91%, rgba(7,5,15,0.97) 100%)',
        }}
      />

      {/* RONDA 13 (Scarlette, 02-10): «yo no usaría esto bajo del logo» [el titular «DOUBLETREE SE VISTE DE
          MORADO»]; Eli: «eso para los 3» → fuera el titular en las tres: del logo se pasa directo al sello, que
          crece con el sitio que quedó. */}
      {/* RONDA 15 (Eli, 02-10, sobre la página de revisión): «quiero que el botón quede igual como está en la
          opción 2, para que todo se vea centrado. Sube un poco más "Noches del 16 y 17 de octubre" y los íconos, al
          igual que está en la opción 2. Y necesito que el antes y el precio y todo eso quede un poco más grande…
          las tres tal cual como está en la opción 2… para que se vea todo bien unificado».
          → las opciones 1 y 3 toman los TAMAÑOS y la columna de la 2 (sello, precio, fecha, íconos, botón liso,
            dirección, legal) y su mismo pie; la fecha y los íconos suben 126 px y quedan sobre el hotel, bajo el
            precio. Sólo cambia el logo: blanco en la 1 (igual al de la 2), morado y más grande en la 3. */}
      {conLogo ? <LogoDT top={20} ancho={218} tinta="morado" /> : <LogoDT top={30} ancho={178} />}
      <Fila top={conLogo ? 208 : 202}>
        <Sello palabra={c.sello} script={c.script} cuerpo={112} army={conLogo ? 1.8 : 1.85} />
      </Fila>
      <Fila top={512}>
        <Precio antes={c.antes} precio={c.precio} bajo={c.bajoPrecio} cuerpo={100} ancho={520} />
      </Fila>

      <Fila top={850}>
        <Fecha t={c.fecha} cuerpo={40} />
      </Fila>
      <Fila top={922}>
        <Incluye items={c.incluye} cuerpo={24} columna={300} />
      </Fila>
      <Boton top={1076} cuerpo={42} plano />
      <Direccion top={1178} cuerpo={28} />
      <Legal t={c.legal} top={1280} ancho={960} />
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════════════════════════════
// 2 · LA FOTO DE LA CLIENTA — el hotel al atardecer con filtro morado, todo el texto al eje sobre la foto
// ═══════════════════════════════════════════════════════════════════════════════════════════════
/**
 * RONDA 14 (Eli, 02-10, con la maqueta de Scarlette): «así la dos mejor y queda» · «la foto de la op 2 literal
 * del de la clienta que mandó, en un filtro morado» · botón «sin lo metálico».
 * Sin recuadro: logo blanco arriba (como en la pieza de la clienta), «PREVENTA / Tarifa ARMY», el precio entre
 * filetes, la fecha, lo que incluye, el botón morado liso, la dirección y el legal, todo sobre la foto. Un velo
 * morado oscuro, parejo, asienta la foto bajo el texto (sin recuadros ni brillos).
 */
export const DtArmyClienta: React.FC<{linea: Linea}> = ({linea}) => {
  const c = LINEAS[linea];
  return (
    <AbsoluteFill style={{backgroundColor: NEGRO}}>
      <Img src={staticFile('assets/hilton/dt/army/clienta-morada.jpg')} style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', objectPosition: 'center top'}} />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'linear-gradient(to bottom, rgba(18,6,40,0.12) 0%, rgba(18,6,40,0.3) 14%, rgba(18,6,40,0.5) 30%, rgba(18,6,40,0.56) 70%, rgba(18,6,40,0.74) 88%, rgba(18,6,40,0.86) 100%)',
        }}
      />
      <LogoDT top={30} ancho={178} />
      <Fila top={202}>
        <Sello palabra={c.sello} script={c.script} cuerpo={112} army={1.85} />
      </Fila>
      <Fila top={512}>
        <Precio antes={c.antes} precio={c.precio} bajo={BAJO_PRECIO_OP2} cuerpo={100} ancho={520} />
      </Fila>
      <Fila top={778}>
        <Fecha t={c.fecha} cuerpo={40} />
      </Fila>
      <Fila top={858}>
        <Incluye items={c.incluye} cuerpo={24} columna={300} />
      </Fila>
      <Boton top={1076} cuerpo={42} plano />
      <Direccion top={1178} cuerpo={28} />
      <Legal t={c.legal} top={1280} ancho={960} />
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

/**
 * RONDA 13 (Eli, 02-10) — `tarjeta`: la opción 2 con «esta distribución» (el post de BTS Journal que mandó):
 * la foto entera en morado y una TARJETA BLANCA al centro, opaca y de esquinas redondas, con el logo arriba.
 * El fondo es la fachada del hotel al atardecer («que se parezca al fondo de la clienta»). Sin titular bajo
 * el logo (Scarlette: «yo no usaría esto bajo del logo»), la tarjeta parte más abajo y deja ver el cielo y la
 * cornisa del hotel.
 */
export const DtArmyHabitacion: React.FC<{linea: Linea; foto?: string; tarjeta?: boolean}> = ({linea, foto = 'assets/hilton/dt/army/habitacion-army-b.jpg', tarjeta}) => {
  const c = LINEAS[linea];
  const panelY = tarjeta ? 236 : PANEL.y;
  return (
    <AbsoluteFill style={{backgroundColor: NEGRO}}>
      <Img src={staticFile(foto)} style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover'}} />

      <div
        style={{
          position: 'absolute',
          left: PANEL.x,
          top: panelY,
          width: PANEL.ancho,
          height: PANEL.y + PANEL.alto - panelY,
          borderRadius: PANEL.radio,
          boxSizing: 'border-box',
          // RONDA 8 (Eli): el recuadro es vidrio BLANCO (α 0,80, desenfoque 3 px), logo y titular en el morado
          // del hotel y el resto del texto en la tinta clara. Como `tarjeta` es blanco casi macizo (α 0,94),
          // como la tarjeta de la referencia: sobre la fachada, la grilla de ventanas se colaba por el vidrio.
          border: '3px solid rgba(255,255,255,0.96)',
          background: tarjeta ? 'rgba(255,255,255,0.94)' : 'rgba(255,255,255,0.8)',
          backdropFilter: 'blur(3px)',
          WebkitBackdropFilter: 'blur(3px)',
          boxShadow: '0 16px 50px rgba(7,5,15,0.3)',
        }}
      />

      <Sombra.Provider value="none">
        <Tinta.Provider value={TINTA_CLARA}>
          {/* RONDA 13: sin el titular «DOUBLETREE SE VISTE DE MORADO» (Scarlette; Eli: «eso para los 3») */}
          <LogoDT top={tarjeta ? 270 : 240} ancho={tarjeta ? 140 : 150} tinta="morado" />
          <Fila top={tarjeta ? 410 : 396}>
            <Sello palabra={c.sello} script={c.script} cuerpo={tarjeta ? 108 : 112} />
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

// ═══════════════════════════════════════════════════════════════════════════════════════════════
// ADAPTACIONES — historia, historia para paid y post para paid (1:1) de las opciones 1 y 2
// ═══════════════════════════════════════════════════════════════════════════════════════════════
/**
 * Eli, 02-10: «OP 1 y 2 quedaron, por favor ten las adaptaciones listas para todas cuando te diga cuál quede».
 * Es el MISMO KV del post (mismo orden, mismas piezas, botón liso) llevado a tres formatos:
 * · `st`     — historia orgánica 1080 × 1920 (máster 2250 × 4000). El legal va al pie (~1740), como en las
 *              historias de DT.
 * · `stPaid` — historia para Meta Ads: nada entre y 0–250 ni bajo y 1580 (ahí van el perfil y el botón del
 *              anuncio), y 60 px de margen a los lados.
 * · `paid`   — post de paid 1080 × 1080 (Hilton entrega el paid en cuadrado y a 1080, sin ampliar).
 * `fondo`: `ciudad` (opción 1: la aérea con el hotel morado) o `clienta` (opción 2: su foto con filtro morado).
 */
export type FormatoArmy = 'st' | 'stPaid' | 'paid';
type Caja = {top: number; cuerpo: number};
const FORMATOS: Record<FormatoArmy, {
  alto: number;
  logo: {top: number; ancho: number};
  sello: Caja;
  precio: Caja & {ancho: number};
  fecha: Caja;
  incluye: Caja & {columna: number};
  boton: Caja;
  direccion: Caja;
  legal: Caja & {ancho: number};
  /** la aérea: escala de la foto, la y del techo del hotel (queda justo bajo el precio) y `velo`: el mínimo de
   *  negro sobre el hotel (0 = se ve limpio; en el cuadrado no hay sitio y la fecha y los íconos van encima) */
  hotel: {s: number; techo: number; velo: number};
  /** todo el bloque de texto escalado desde arriba (`k`) y corrido (`dy`), para centrarlo en el alto */
  bloque?: {k: number; dy: number};
  /** px que el velo de arriba se abre ANTES del pie del precio, cuando el hotel sube a pegarse al precio */
  adelanta?: number;
}> = {
  st: {
    alto: 1920,
    // el logo parte en y 256: en las historias de DT va bajo la franja de 250 px de la interfaz
    logo: {top: 256, ancho: 180},
    sello: {top: 420, cuerpo: 120},
    precio: {top: 760, cuerpo: 108, ancho: 560},
    fecha: {top: 1216, cuerpo: 44},
    incluye: {top: 1296, cuerpo: 26, columna: 310},
    boton: {top: 1474, cuerpo: 46},
    direccion: {top: 1586, cuerpo: 30},
    legal: {top: 1736, cuerpo: 22, ancho: 900},
    hotel: {s: 1.1, techo: 1004, velo: 0},
  },
  stPaid: {
    alto: 1920,
    logo: {top: 262, ancho: 170},
    sello: {top: 428, cuerpo: 112},
    precio: {top: 746, cuerpo: 100, ancho: 520},
    fecha: {top: 1050, cuerpo: 40},
    incluye: {top: 1122, cuerpo: 24, columna: 300},
    boton: {top: 1290, cuerpo: 42},
    direccion: {top: 1392, cuerpo: 28},
    legal: {top: 1488, cuerpo: 19, ancho: 900},
    // Eli, 02-10: «para paid ST zona segura la op 1, que el hotel suba un poco, cerca del precio» → el techo sube
    // 36 px (976 → 940) y el velo de arriba se abre antes, para que el hotel se vea desde el filete del precio
    hotel: {s: 1.05, techo: 940, velo: 0},
    adelanta: 26,
  },
  paid: {
    alto: 1080,
    logo: {top: 30, ancho: 126},
    sello: {top: 148, cuerpo: 90},
    precio: {top: 390, cuerpo: 82, ancho: 440},
    fecha: {top: 604, cuerpo: 34},
    incluye: {top: 662, cuerpo: 20, columna: 262},
    boton: {top: 794, cuerpo: 36},
    direccion: {top: 878, cuerpo: 24},
    legal: {top: 946, cuerpo: 17, ancho: 940},
    hotel: {s: 0.8, techo: 580, velo: 0.46},
    // Eli, 02-10: «en post paid centra toda la info, ya que se ve extraño, y que crezca un poco en ambos» → el
    // bloque (y 30–968) crece 6 % y queda con el mismo aire arriba y abajo (43 px)
    bloque: {k: 1.06, dy: 11},
  },
};

// El recorte de la aérea que usan las adaptaciones (x 1560–3040 · y 0–1900 de la foto completa), ampliado 2× con
// el escalador de precisión para que la historia a máster no salga blanda. Lo arma `scripts/dt-army-fachada.py`.
const RECORTE = {src: 'assets/hilton/dt/army/hotel-morado-recorte.jpg', x0: 1560, y0: 0, w: 1480, h: 1900} as const;

export const DtArmyAdaptacion: React.FC<{linea: Linea; fondo: 'ciudad' | 'clienta'; formato: FormatoArmy}> = ({linea, fondo, formato}) => {
  const c = LINEAS[linea];
  const F = FORMATOS[formato];
  const pct = (y: number) => `${((y / F.alto) * 100).toFixed(2)}%`;
  const {k, dy} = F.bloque ?? {k: 1, dy: 0};
  // el filete de abajo del precio, ya con el bloque escalado, menos lo que el velo se adelanta
  const finPrecio = (F.precio.top + F.precio.cuerpo * 2.1 + 6) * k + dy - (F.adelanta ?? 0);
  const techo = F.hotel.techo * k + dy;
  const v = (a: number) => `rgba(7,5,15,${Math.max(a, F.hotel.velo)})`;
  return (
    <AbsoluteFill style={{backgroundColor: NEGRO}}>
      {fondo === 'ciudad' ? (
        <>
          <Img
            src={staticFile(RECORTE.src)}
            style={{position: 'absolute', width: RECORTE.w * F.hotel.s, height: RECORTE.h * F.hotel.s, left: 540 - (FOTO.cajaX - RECORTE.x0) * F.hotel.s, top: techo - (FOTO.cajaY0 - RECORTE.y0) * F.hotel.s}}
          />
          {/* el mismo velo del post, atado al pie del precio: negro parejo arriba, limpio en el techo del hotel y
              un degradado largo hacia el pie */}
          <div
            style={{
              position: 'absolute',
              inset: 0,
              background: `linear-gradient(to bottom, rgba(7,5,15,0.78) 0%, rgba(7,5,15,0.7) 10%, rgba(7,5,15,0.7) ${pct(finPrecio - 55)}, ${v(0.28)} ${pct(finPrecio)}, ${v(0)} ${pct(finPrecio + 42)}, ${v(0)} ${pct(finPrecio + 95)}, ${v(0.16)} ${pct(finPrecio + 150)}, ${v(0.36)} ${pct(finPrecio + 205)}, ${v(0.56)} ${pct(finPrecio + 260)}, ${v(0.74)} ${pct(Math.min(F.alto - 3, finPrecio + 325))}, ${v(0.86)} ${pct(Math.min(F.alto - 2, finPrecio + 405))}, ${v(0.94)} ${pct(Math.min(F.alto - 1, finPrecio + 500))}, rgba(7,5,15,0.97) 100%)`,
            }}
          />
        </>
      ) : (
        <>
          {/* la foto de la clienta es 4:5: en 9:16 se recorta por los lados con el hotel al centro; en 1:1, por abajo */}
          {/* Eli, 02-10: «en ambas ST que no se vea esa línea del hotel» → con el recorte al 64 % se asomaba en el borde
              derecho una franja del edificio vecino; al 57 % el muro del hotel llega hasta el borde */}
          <Img src={staticFile('assets/hilton/dt/army/clienta-morada.jpg')} style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', objectPosition: formato === 'paid' ? 'center top' : '57% center'}} />
          <div
            style={{
              position: 'absolute',
              inset: 0,
              background:
                'linear-gradient(to bottom, rgba(18,6,40,0.12) 0%, rgba(18,6,40,0.3) 14%, rgba(18,6,40,0.5) 30%, rgba(18,6,40,0.56) 70%, rgba(18,6,40,0.74) 88%, rgba(18,6,40,0.86) 100%)',
            }}
          />
        </>
      )}

      <div style={{position: 'absolute', left: 0, top: 0, width: 1080, height: F.alto, transform: `translateY(${dy}px) scale(${k})`, transformOrigin: '540px 0px'}}>
      <LogoDT top={F.logo.top} ancho={F.logo.ancho} />
      <Fila top={F.sello.top}>
        <Sello palabra={c.sello} script={c.script} cuerpo={F.sello.cuerpo} army={1.85} />
      </Fila>
      <Fila top={F.precio.top}>
        <Precio antes={c.antes} precio={c.precio} bajo={fondo === 'clienta' ? BAJO_PRECIO_OP2 : c.bajoPrecio} cuerpo={F.precio.cuerpo} ancho={F.precio.ancho} />
      </Fila>
      <Fila top={F.fecha.top}>
        <Fecha t={c.fecha} cuerpo={F.fecha.cuerpo} />
      </Fila>
      <Fila top={F.incluye.top}>
        <Incluye items={c.incluye} cuerpo={F.incluye.cuerpo} columna={F.incluye.columna} />
      </Fila>
      <Boton top={F.boton.top} cuerpo={F.boton.cuerpo} plano />
      <Direccion top={F.direccion.top} cuerpo={F.direccion.cuerpo} />
      <Legal t={c.legal} top={F.legal.top} ancho={F.legal.ancho} cuerpo={F.legal.cuerpo} />
      </div>
    </AbsoluteFill>
  );
};
