/**
 * PISO18 — CARRUSEL «CUMPLEAÑOS EN PISO18» (FEED col Q · 29-09 · 12:00 · S5)
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL BRIEF, LITERAL
 * ══════════════════════════════════════════════════════════════════════════
 * Hoja FEED, columna del 29 de septiembre, estado **EN REVISIÓN**:
 *
 *     CARRUSEL ESTÁTICO – CUMPLEAÑOS EN PISO18
 *
 *     Slide 1 (portada):
 *     Visual: Torta de cumpleaños decorada sobre la mesa principal, con el
 *     salón de fondo.
 *     Texto: Sin texto
 *
 *     Slide 2:
 *     Visual: Detalle de la decoración (globos, centros de mesa, elementos
 *     temáticos).
 *     Texto:
 *       Tu cumpleaños con todo incluido:
 *       • Ambientación y decoración
 *       • DJ en vivo, iluminación y amplificación
 *       • Cóctel, estaciones temáticas y trasnoche
 *       • ¡Fiesta y barra libre!
 *
 *     Slide 3:
 *     Visual: Grupo de invitados brindando, plano general con la vista de
 *     Santiago de fondo.
 *     Texto:
 *       ¡Nuestro regalo para el festejado!
 *       • Estadía de regalo en DoubleTree by Hilton (incluye desayuno y late
 *         check-out).
 *       • Beneficios para invitados: Tarifa preferencial en habitaciones y
 *         estacionamiento liberado.
 *
 * El cierre `Cotiza tu cumpleaños en piso18.cl` sale del copy de la misma
 * columna (fila F13) — no está inventado. Va al pie de la slide 3, que es la
 * última del carrusel.
 *
 * ⚠️ El brief NO trae comentarios de cliente en esta columna. La celda está
 * limpia: no hay ronda previa que aplicar.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⚠️ LO QUE HAY QUE INFORMARLE A ELI — y no se resuelve desde diseño
 * ══════════════════════════════════════════════════════════════════════════
 * Este es el **segundo carrusel de cumpleaños del mes**: el del 15-09 («¿QUÉ
 * INCLUYEN LOS CUMPLEAÑOS EN PISO18?», publicado, `CARRUSEL CUMPLE ACTUAL
 * 2026`) ya enumera ambientación, audiovisuales, estaciones, fiesta y barra
 * libre y trasnoche — o sea, los mismos cuatro puntos de la slide 2 de acá.
 * Lo único nuevo del 29-09 es **el regalo al festejado** (estadía en
 * DoubleTree + beneficios para invitados).
 *
 * ⇒ Desde diseño se ejecuta el brief como viene y **la discrepancia se
 * informa**. Lo que sí se hizo por criterio propio es que las dos piezas NO se
 * parezcan: el del 15-09 es nocturno, cálido y con el titular en la portada;
 * este es de día, con la ciudad a la vista y la portada limpia.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LAS TRES FOTOS — dos PRODUCIDAS, una real
 * ══════════════════════════════════════════════════════════════════════════
 * ⛔ Se midieron los tres bancos disponibles —110 fotos de `Piso 18_28 ago
 * decoración 2024`, 85 de `Piso 18 agosto` (2023) y las 191 de `3-Finales
 * 2026`— y **no hay ninguna torta de cumpleaños ni ningún brindis**. La torta
 * que se ve en el carrusel publicado del 15-09 no está en ninguna carpeta
 * alcanzable desde acá.
 *
 * Eli decidió el 15-09 resolverlo como en la S4: **cambiar la superficie de la
 * foto real, nunca inventar la escena**. Las dos ausencias se produjeron con
 * Nano Banana Pro pasándole la foto real como referencia, y los prompts van
 * acá abajo porque son lo que hay que repetir si esto se rehace.
 *
 * | Slide | Base real | Qué se cambió |
 * |---|---|---|
 * | 1 | `deco-ago2024/piso_18-141` (mesa de madera + arreglo + ventanal) | Se agregó una torta de tres pisos sobre el extremo despejado de la MISMA mesa. Mesa, arreglo, candelabros, ventanal y edificios reales intactos |
 * | 2 | `deco-ago2024/piso_18-145` | **Nada: es la foto real.** Esferas de vidrio con velas, flores burdeos, fondo azul profundo |
 * | 3 | `banco-2026/0172` (mesa redonda + ventanales con Santiago) | Se agregaron tres copas de espumante DESENFOCADAS en el borde inferior. Mesa, montaje, centro, ventanas y ciudad intactos |
 *
 * PROMPT DE LA SLIDE 1 (el que funcionó, v2 — el v1 dejaba la torta chica y
 * escondida detrás de los candelabros porque el encuadre era el general):
 *   «EDITA la fotografía de la REFERENCIA 1 sin recomponerla. (…) NO SE TOCA:
 *   la mesa larga de madera oscura (…), TODOS los candelabros (…), los
 *   edificios reales de Santiago que se ven por el vidrio, que existen y
 *   conservan su forma exacta (…). EL ÚNICO CAMBIO PERMITIDO: sobre el sector
 *   despejado del primer plano de la misma mesa (…) una TORTA DE CUMPLEAÑOS
 *   real de TRES pisos como elemento protagonista (…) proyecta su sombra de
 *   contacto real según la luz que entra por el ventanal (…). Nada más cambia.»
 *
 * PROMPT DE LA SLIDE 3 (v2 — el v1 dibujaba las manos completas y se notaban):
 *   «(…) EL ÚNICO CAMBIO PERMITIDO: en el borde INFERIOR del cuadro, agrega
 *   SOLO LAS COPAS de un brindis: tres copas altas de espumante alzadas, muy
 *   DESENFOCADAS y con mucho bokeh (…). NO se ve ninguna mano, ningún dedo,
 *   ningún brazo, ningún rostro y ninguna persona (…).»
 *
 * ⭐ Y el prompt decide si recrea o edita: los dos empiezan por «EDITA (…) sin
 * recomponerla», enumeran lo que NO se toca y declaran **un solo** cambio.
 *
 * ⚠️ Ninguna foto se amplía: las tres bases entran a 2400 px de ancho y la
 * entrega es a 2250 → factor 0,94. Nano Banana Pro no tiene 4:5, así que se
 * generó en `post` (3:4) a 4K (3584×4800) y se recortó.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA GRAMÁTICA QUE SE RESPETA
 * ══════════════════════════════════════════════════════════════════════════
 * · Portada: foto a sangre + **logotipo completo blanco arriba, centrado**
 *   (tope y=105 @1080, ancho 272). Nada más — igual que `C2 S1 n°1` aprobada.
 * · El logotipo va **sólo en la primera slide**, como pidió el cliente para el
 *   carrusel del 22-09 («logo en la primera G y que todas las slides sean
 *   limpias»).
 * · Titulares en IvyPresto mezclando roman e itálica; listas y CTA en Raleway,
 *   que es la legible. Ivy poco, sólo para destacar.
 * · El contraste lo pone **el velo**, no la sombra: una sola sombra difusa al
 *   38 %, nunca dos apiladas (ronda 3 de la S4).
 * · El fucsia `#D4145A` sólo en la viñeta y en `piso18.cl`. Es la firma, no un
 *   color de relleno.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {P18, cargarFuentesP18} from '../../brand/piso18';

const W = 1080;
const H = 1350;

/** Sombra de la marca: UNA sola, difusa. Ver ronda 3 de la S4. */
const SOMBRA = '0 2px 30px rgba(0,0,0,0.38)';

/**
 * Velo inferior en degradado. Es el recurso propio de la marca —el mismo que
 * trae la plantilla `logo PISO18.png`— y es lo que sostiene el texto blanco.
 * `hasta` es la altura desde abajo, en fracción, a la que el velo se apaga.
 */
const VeloPie: React.FC<{hasta?: number; opacidad?: number}> = ({
  hasta = 0.68,
  opacidad = 0.82,
}) => (
  <AbsoluteFill
    style={{
      background: `linear-gradient(to top, rgba(8,8,10,${opacidad}) 0%, rgba(8,8,10,${
        opacidad * 0.72
      }) ${hasta * 0.32 * 100}%, rgba(8,8,10,${opacidad * 0.30}) ${
        hasta * 0.66 * 100
      }%, rgba(8,8,10,0) ${hasta * 100}%)`,
    }}
  />
);

/** El logotipo completo, blanco, arriba y centrado. Geometría medida. */
const LogoFeed: React.FC = () => (
  <Img
    src={staticFile('assets/hilton/piso18/logo.png')}
    style={{
      position: 'absolute',
      width: P18.geometria.logoAncho,
      height: P18.geometria.logoAncho / P18.geometria.logoProporcion,
      left: (W - P18.geometria.logoAncho) / 2,
      top: P18.geometria.logoYFeed,
      filter: 'drop-shadow(0 2px 22px rgba(0,0,0,0.45))',
    }}
  />
);

/**
 * Un punto de la lista. La viñeta va en fucsia y **fuera** del flujo del texto,
 * para que las líneas que se parten queden alineadas con la primera y no bajo
 * la viñeta — que es lo que hace que una lista se lea como lista.
 */
const Punto: React.FC<{children: React.ReactNode; cuerpo: number; aire: number}> = ({
  children,
  cuerpo,
  aire,
}) => (
  <div
    style={{
      position: 'relative',
      paddingLeft: cuerpo * 0.92,
      marginTop: aire,
      fontFamily: P18.fuentes.texto,
      fontWeight: 500,
      fontSize: cuerpo,
      lineHeight: 1.42,
      color: P18.colores.blanco,
      textShadow: SOMBRA,
    }}
  >
    <span
      style={{
        position: 'absolute',
        left: 0,
        top: cuerpo * 0.44,
        width: cuerpo * 0.22,
        height: cuerpo * 0.22,
        borderRadius: 999,
        backgroundColor: P18.colores.fucsia,
      }}
    />
    {children}
  </div>
);

// ───────────────────────────────────────────────────────────────────────────
// SLIDE 1 · PORTADA — la torta. Sin texto, como pide el brief.
// ───────────────────────────────────────────────────────────────────────────
export const P18C1CumpleS1: React.FC = () => {
  cargarFuentesP18();
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Img
        src={staticFile('assets/hilton/piso18/s5-torta.jpg')}
        style={{width: '100%', height: '100%', objectFit: 'cover'}}
      />
      {/*
        Velo SUPERIOR, no inferior: acá lo único que hay que sostener es el
        logotipo blanco, y arriba la foto tiene el ventanal claro. Es el mismo
        degradado de la plantilla de la marca, suave.
      */}
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to bottom, rgba(0,0,0,0.42) 0%, rgba(0,0,0,0.20) 26%, rgba(0,0,0,0.06) 42%, rgba(0,0,0,0) 56%)',
        }}
      />
      <LogoFeed />
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────────────────────────────────────
// SLIDE 2 · LO QUE INCLUYE — foto real de decoración + los cuatro puntos.
// ───────────────────────────────────────────────────────────────────────────
export const P18C1CumpleS2: React.FC = () => {
  cargarFuentesP18();
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Img
        src={staticFile('assets/hilton/piso18/s5-deco.jpg')}
        style={{width: '100%', height: '100%', objectFit: 'cover'}}
      />
      <VeloPie hasta={0.72} opacidad={0.86} />

      {/*
        El bloque se ancla ABAJO y no arriba: la foto tiene las esferas de
        vidrio en el tercio alto y son lo que hay que dejar respirar. El texto
        ocupa la zona baja, que en esta toma es la más oscura y la más quieta.
      */}
      <div style={{position: 'absolute', left: 92, right: 92, bottom: 118}}>
        <div
          style={{
            fontFamily: P18.fuentes.titular,
            fontWeight: 300,
            fontSize: 62,
            lineHeight: 1.1,
            color: P18.colores.blanco,
            textShadow: SOMBRA,
          }}
        >
          Tu cumpleaños
          <br />
          <span style={{fontStyle: 'italic', fontWeight: 400}}>con todo incluido:</span>
        </div>

        <div style={{marginTop: 42}}>
          <Punto cuerpo={33} aire={0}>
            Ambientación y decoración
          </Punto>
          <Punto cuerpo={33} aire={22}>
            DJ en vivo, iluminación y amplificación
          </Punto>
          <Punto cuerpo={33} aire={22}>
            Cóctel, estaciones temáticas y trasnoche
          </Punto>
          <Punto cuerpo={33} aire={22}>
            ¡Fiesta y barra libre!
          </Punto>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────────────────────────────────────
// SLIDE 3 · EL REGALO — el brindis con la ciudad + los dos beneficios + CTA.
// ───────────────────────────────────────────────────────────────────────────
export const P18C1CumpleS3: React.FC = () => {
  cargarFuentesP18();
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Img
        src={staticFile('assets/hilton/piso18/s5-brindis.jpg')}
        style={{width: '100%', height: '100%', objectFit: 'cover'}}
      />
      {/*
        ⚠️ ACÁ EL VELO NO PUEDE SER EL DE SIEMPRE, y por qué importa.
        Medida por bandas del 5 %, esta foto es la más CLARA del carrusel: el
        mantel llega a 187 de luminancia media contra los 20 del cielorraso. Un
        velo de pie normal (0,88 desde abajo) deja el texto perfecto **y apaga
        las copas del brindis**, que son justamente lo que se produjo para esta
        slide — se rindió así una vez y las copas desaparecieron.

        ⇒ Va un velo de BANDA: carga en el tramo del mantel, que es donde vive
        el texto, y **afloja en el último 14 %**, que es donde están las copas.
        Así el brindis se sigue leyendo como bokeh cálido detrás de la tipografía
        en vez de convertirse en un degradado negro.
      */}
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to bottom, rgba(8,8,10,0) 30%, rgba(8,8,10,0.34) 48%, rgba(8,8,10,0.74) 62%, rgba(8,8,10,0.80) 84%, rgba(8,8,10,0.66) 100%)',
        }}
      />

      <div style={{position: 'absolute', left: 92, right: 92, bottom: 152}}>
        <div
          style={{
            fontFamily: P18.fuentes.titular,
            fontWeight: 300,
            fontSize: 58,
            lineHeight: 1.1,
            color: P18.colores.blanco,
            textShadow: SOMBRA,
          }}
        >
          ¡Nuestro <span style={{fontStyle: 'italic', fontWeight: 400}}>regalo</span>
          <br />
          para el festejado!
        </div>

        <div style={{marginTop: 38}}>
          <Punto cuerpo={30} aire={0}>
            Estadía de regalo en DoubleTree by Hilton (incluye desayuno y late check-out).
          </Punto>
          <Punto cuerpo={30} aire={20}>
            {/* La «T» de «Tarifa» va en mayúscula porque así está en el brief, y los
                textos en pantalla van literales. No es un error de tipeo mío. */}
            Beneficios para invitados: Tarifa preferencial en habitaciones y estacionamiento
            liberado.
          </Punto>
        </div>
      </div>

      {/*
        El cierre del carrusel. Va en Raleway y discreto —no en píldora— porque
        en feed el botón es de las historias: acá el llamado se lee, no se toca.
        El texto es el del copy de la misma columna de la grilla.
      */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          bottom: 88,
          textAlign: 'center',
          fontFamily: P18.fuentes.texto,
          fontWeight: 700,
          fontSize: 28,
          letterSpacing: 0.3,
          color: P18.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        {/*
          ⛔ `piso18.cl` va en el fucsia OFICIAL `#D4145A` y en ningún otro rosa.
          Aclararlo para que se lea mejor sobre la foto sería inventarle un color
          a la marca — y además acerca el pixel al `#FF007C` de Selfie, que el QA
          rechaza por bloqueante. El contraste lo pone el velo, no el color.
        */}
        Cotiza tu cumpleaños en{' '}
        <span style={{color: P18.colores.fucsia}}>piso18.cl</span>
      </div>
    </AbsoluteFill>
  );
};

/**
 * Guía de QA del carrusel. En feed no hay zona segura de Instagram, pero sí
 * la regla de paid del estudio de dejar libre el 10–15 % inferior, y conviene
 * ver el margen de 92 px con el que se compuso.
 */
export const P18C1CumpleGuia: React.FC = () => (
  <AbsoluteFill>
    <P18C1CumpleS3 />
    <AbsoluteFill style={{pointerEvents: 'none'}}>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          bottom: 0,
          height: H * 0.12,
          background: 'rgba(255,0,0,0.20)',
          borderTop: '2px solid red',
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 92,
          right: 92,
          top: 0,
          bottom: 0,
          border: '1px dashed rgba(0,255,255,0.75)',
        }}
      />
    </AbsoluteFill>
  </AbsoluteFill>
);
