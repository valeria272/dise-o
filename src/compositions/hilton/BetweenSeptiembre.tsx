/**
 * BETWEEN — grilla SEPTIEMBRE 2026 (feed + stories) · RECONSTRUIDA 26-08-2026
 *
 * Textos LITERALES del brief «BETWEEN _ GRILLA SEPTIEMBRE»
 * (sheet 1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY). Los títulos van sin punto final
 * (el componente lo quita solo). Solo se producen las piezas en estado
 * OK PARA DISEÑAR o CORREGIDO.
 *
 * ⚠️ La primera versión de esta grilla se rechazó entera: titulares a la mitad
 * del tamaño real, bloque centrado y flotando, sin caja taupe ni texto en arco,
 * y fotos oscuras con multiply pesado. Esta versión usa la GRAMÁTICA MEDIDA
 * sobre las 19 piezas reales de Eli — ver `clients/hilton/CLAUDE.md`.
 *
 * Reglas que gobiernan cada pieza de acá:
 *  - titular Raleway Black 76–97 según cuántas líneas ocupe; tiene que llenar
 *    el 55–80 % del ancho. Si baja de 50 %, la pieza se ve chica.
 *  - la script va montada sobre la caja alta (lo hace `TitularBetween` solo)
 *  - promo, precio y horario van en CAJA TAUPE, no en texto suelto
 *  - bloque anclado ARRIBA; centrado solo cuando la foto lo pide
 *  - multiply 0,10–0,16: las fotos ya vienen gradadas, no hace falta oscurecer
 *  - donde el vaso To Go trae el logo, la pieza NO lleva logo sobrepuesto
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {BETWEEN} from '../../brand/hilton-between';
import {
  Dato,
  FotoFondo,
  LogoBetween,
  PiezaFeedBodegon,
  PiezaStoryBetween,
  StoryAnimada,
  TitularBetween,
} from './BetweenSistema';
import {Cuadrantes, Etiqueta, StickerQuiz} from './BetweenRecursos';

/** Fotos YA GRADADAS hacia los números de Eli (scripts/between-gradar.py). */
const F = 'assets/hilton/between/fotos-gradadas/';
const IA = 'assets/hilton/between/ia-sept/';

const HORARIO_TOGO = 'Lunes a viernes · 08:00 a 10:00 hrs';

/* ══════════════════ FEED · 1080×1350 ══════════════════ */

/* --- 1 sept · CARRUSEL PROMOS TO GO --- */

export const ToGo1: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'togo-croissants.jpg'}
    caps="Tu desayuno"
    script="va contigo"
    datos={[HORARIO_TOGO]}
    oscurecer={0.12}
  />
);

export const ToGo2: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'togo-sandwich.jpg'}
    caps="Para algo más"
    script="contundente"
    datos={['Café to go + sándwich', 'Desde $4.290']}
    arco="Ave palta o croissant jamón queso"
    oscurecer={0.12}
  />
);

export const ToGo3: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'togo-croissant-queso.jpg'}
    caps="El match"
    script="perfecto"
    datos={['Café to go + dulce', 'Desde $3.790']}
    arco="Vigilantes, muffin, brownie y más"
    oscurecer={0.12}
  />
);

export const ToGo4: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'togo-empanadas.jpg'}
    caps="¿Por qué"
    script="elegir uno?"
    datos={['Café + salado + dulce', 'Desde $5.290']}
    oscurecer={0.12}
  />
);

/* --- 7 sept · HUMOR | CAFECITO BETWEEN --- */

export const HumorCafecito: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'chica-cafe.jpg'}
    anclaje="abajo"
    posicionFoto="60% center"
    caps="Esa preocupación"
    script="no cabe acá"
    sizeCaps={82}
    conLogo
    logoPosicion="abajo"
    oscurecer={0.16}
  />
);

/* --- 9 sept · CARRUSEL PRIMERO LA FOTO… ¿O NO? --- */

export const Foto1: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'desayuno-mesa.jpg'}
    anclaje="abajo"
    caps="Le voy a sacar"
    script="una foto"
    conLogo
    logoPosicion="abajo"
    oscurecer={0.14}
  />
);

export const Foto2: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'cafe-desayuno.jpg'}
    anclaje="abajo"
    caps="Foto"
    script="primero"
    conLogo
    logoPosicion="abajo"
    oscurecer={0.14}
  />
);

export const Foto3: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'croissant-plato.jpg'}
    caps="Esto merece"
    script="una foto"
    conLogo
    logoPosicion="abajo"
    oscurecer={0.12}
  />
);

export const Foto4: React.FC = () => (
  <PiezaFeedBodegon
    foto={IA + 'torta-empezada.png'}
    caps="Se me olvidó"
    script="la foto"
    conLogo
    logoPosicion="abajo"
    oscurecer={0.14}
  />
);

/* --- 11 sept · ELLA HABLÓ / ELLA ESCUCHÓ --- */

export const EllaHablo: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <FotoFondo src={IA + 'dos-tazas.png'} oscurecer={0.14} />
    <LogoBetween formato="feed" posicion="abajo" />
    {/* Las etiquetas van sobre cada taza: hay que mirar la foto para entender el chiste */}
    <Etiqueta x={330} y={690} size={72} script>
      Ella habló
    </Etiqueta>
    <Etiqueta x={762} y={690} size={72} script>
      Ella escuchó
    </Etiqueta>
    <div style={{position: 'absolute', left: BETWEEN.bloque.x, right: BETWEEN.bloque.x, top: BETWEEN.bloque.yFeed - 9}}>
      <TitularBetween caps="Hay cafés de" script="10 minutos" sizeCaps={86} />
    </div>
  </AbsoluteFill>
);

/* --- 14 sept · CARRUSEL DINÁMICO COWORK EN BETWEEN --- */

export const Cowork1: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'cowork-laptop.jpg'}
    anclaje="abajo"
    caps="Tu oficina por hoy"
    script="puede ser Between"
    sizeCaps={80}
    datos={['Espacio, WiFi y café']}
    conLogo
    logoPosicion="abajo"
    oscurecer={0.18}
  />
);

export const Cowork2: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'winter-garden.jpg'}
    caps="¿Muchos pendientes?"
    script="que sea con café"
    sizeCaps={78}
    conLogo
    logoPosicion="abajo"
    oscurecer={0.18}
  />
);

export const Cowork3: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'segundo-nivel.jpg'}
    caps="¿Necesitas cambiar"
    script="de escenario?"
    sizeCaps={80}
    datos={['Segundo nivel · trabajar o reunirte']}
    conLogo
    logoPosicion="abajo"
    oscurecer={0.18}
  />
);

export const Cowork4: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'servicio-mesa.jpg'}
    anclaje="abajo"
    caps="Tú sigue con lo tuyo"
    script="nosotros el café"
    sizeCaps={80}
    conLogo
    logoPosicion="abajo"
    oscurecer={0.18}
  />
);

/* ══════════════════ STORIES · 1080×1920 ══════════════════ */

/* --- 1 sept · PROMO TO GO | CAFÉ + DULCE --- */

export const StToGoDulce: React.FC = () => (
  <PiezaStoryBetween
    foto={F + 'togo-croissants.jpg'}
    conLogo={false}
    caps="Un dulce comienzo"
    script="para tu mañana"
    sizeCaps={84}
    datos={['Café + dulce desde $3.790', HORARIO_TOGO]}
    oscurecer={0.12}
  />
);

/* --- 3 sept · CAFÉ DE REGALO POR TU CUMPLEAÑOS (CORREGIDO) --- */

export const StCumple: React.FC = () => (
  <PiezaStoryBetween
    foto={F + 'togo-brownie.jpg'}
    conLogo={false}
    caps="¡Disfruta tu cumple"
    script="desde temprano!"
    sizeCaps={84}
    datos={['Un café de regalo para ti']}
    legal="Presenta tu carnet · Lunes a viernes · Todo el día"
    oscurecer={0.14}
  />
);

/* --- 4 sept · HUMOR | SEGÚN MIS CÁLCULOS --- */

export const StCalculos: React.FC = () => (
  <PiezaStoryBetween
    foto={F + 'cowork-laptop.jpg'}
    anclaje="abajo"
    caps="Según mis cálculos"
    script="te hace falta café"
    sizeCaps={82}
    bajada="Por suerte, sabemos dónde encontrarlo"
    oscurecer={0.18}
  />
);

/* --- 9 sept · INTERACTIVA | EMERGENCIA BETWEEN --- */

export const StEmergencia: React.FC = () => (
  <PiezaStoryBetween
    foto={F + 'togo-brownie.jpg'}
    conLogo={false}
    caps="Romper en caso"
    script="de antojo"
    sizeCaps={90}
    oscurecer={0.20}
  >
    <div style={{position: 'absolute', left: 0, right: 0, bottom: 420, display: 'flex', justifyContent: 'center'}}>
      <StickerQuiz
        pregunta="¿CUÁL TOMARÍAS?"
        opciones={['☕ Café', '🥐 Algo dulce', '🥪 Algo salado', '✨ Todas las anteriores']}
      />
    </div>
  </PiezaStoryBetween>
);

/* --- 14 sept · INTERACTIVA | ¿CUÁNDO ES HORA DE CAFÉ? --- */

export const StHoraCafe: React.FC = () => (
  <PiezaStoryBetween
    foto={F + 'togo-croissants.jpg'}
    conLogo={false}
    caps="El mejor momento"
    script="para un café es…"
    sizeCaps={82}
    oscurecer={0.20}
  >
    <div style={{position: 'absolute', left: 0, right: 0, bottom: 420, display: 'flex', justifyContent: 'center'}}>
      <StickerQuiz
        pregunta="Elige tu respuesta"
        opciones={['A. En la mañana', 'B. En la tarde', 'C. En la noche', 'D. Todo el día ✨']}
        correcta={3}
      />
    </div>
  </PiezaStoryBetween>
);

/* --- 16 sept · COWORK | YA ABRIMOS (CORREGIDO) --- */

export const StCowork: React.FC = () => (
  <PiezaStoryBetween
    foto={F + 'mesas-trabajo.jpg'}
    caps="Puedes venir,"
    script="¡te esperamos!"
    sizeCaps={88}
    datos={['Lunes a viernes · 08:00 a 22:00 hrs']}
    bajada="Ven a trabajar desde Between. Tenemos una mesa para ti"
    oscurecer={0.30}
  />
);

/* --- 18 sept · SALUDO FIESTAS PATRIAS --- */

export const StDieciocho: React.FC = () => (
  <PiezaStoryBetween
    foto={F + 'terraza.jpg'}
    caps="Por los sabores"
    script="que nos reúnen"
    sizeCaps={88}
    bajada="Que estas Fiestas Patrias estén llenas de buenos momentos y mucho para compartir"
    oscurecer={0.32}
  />
);

/* --- 21 sept · STRUDEL DE MANZANA (composición editorial en 4) --- */

export const StStrudel: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <AbsoluteFill style={{justifyContent: 'flex-start'}}>
      <Cuadrantes
        alto={1330}
        fotos={[
          IA + 'strudel-masa.png',
          IA + 'strudel-manzana.png',
          IA + 'strudel-canela.png',
          IA + 'strudel-nueces.png',
        ]}
      />
    </AbsoluteFill>
    <LogoBetween formato="story" posicion="arriba" />
    {/*
      El título vive en la banda café que queda bajo los cuadrantes, CENTRADO en
      ella. Antes los cuadrantes medían 1180 y el texto se pegaba arriba de la
      banda, dejando 400 px de vacío abajo: la pieza se veía sin terminar.
    */}
    {/* div plano, no AbsoluteFill: AbsoluteFill fuerza inset:0 y se comía el top */}
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        top: 1330,
        bottom: 340,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        padding: '0 90px',
        gap: 16,
      }}
    >
      <TitularBetween caps="Cuatro ingredientes" script="que saben juntos" sizeCaps={76} alinear="centro" />
      <Dato size={30}>Masa · Manzana · Canela · Nueces</Dato>
    </div>
  </AbsoluteFill>
);

/* --- 22 sept · PRIMAVERA EN BETWEEN --- */

export const StPrimavera: React.FC = () => (
  <PiezaStoryBetween
    foto={IA + 'milkshake-terraza.png'}
    caps="La primavera"
    script="se disfruta así"
    sizeCaps={90}
    bajada="Un milkshake, nuestra terraza y una pausa al sol"
    oscurecer={0.16}
  />
);

/* --- 28 sept · HUMOR | CAFÉ TO GO --- */

export const StHumorToGo: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <FotoFondo src={F + 'terraza-2.jpg'} oscurecer={0.20} />
    {/* vaso real de Between recortado, agrandado a propósito para el chiste */}
    <Img
      src={staticFile(F + 'togo-vaso-nobg.png')}
      style={{
        position: 'absolute',
        width: 560,
        left: '50%',
        bottom: 400,
        transform: 'translateX(-50%)',
        filter: 'drop-shadow(0 30px 46px rgba(36,26,18,0.55))',
      }}
    />
    <div style={{position: 'absolute', left: BETWEEN.bloque.x, right: BETWEEN.bloque.x, top: BETWEEN.bloque.yStory - 9}}>
      <TitularBetween caps="POV: yo cargando" script="mis ganas de café" sizeCaps={80} alinear="centro" />
    </div>
  </AbsoluteFill>
);

/* --- 30 sept · PLATEADA AL CARMENERE --- */

export const StPlateada: React.FC = () => (
  <PiezaStoryBetween
    foto={IA + 'plateada.png'}
    caps="¿El almuerzo"
    script="se quedó en casa?"
    sizeCaps={86}
    datos={['Plateada al Carmenere']}
    bajada="Tranqui, el plan B se ve bastante mejor por acá"
    oscurecer={0.16}
  />
);

/* --- animada de respaldo (plantilla) --- */

export const StAnimadaToGo: React.FC = () => (
  <StoryAnimada
    pantallas={[
      {foto: F + 'togo-croissants.jpg', caps: 'Un dulce comienzo', script: 'para tu mañana', sizeCaps: 68},
      {foto: F + 'togo-sandwich.jpg', caps: 'Café + dulce', sizeCaps: 90, bajada: 'Desde $3.790 · To Go'},
    ]}
    horario={HORARIO_TOGO}
    cta="Pasa por Between y llévalo contigo"
    framesPorPantalla={75}
  />
);
