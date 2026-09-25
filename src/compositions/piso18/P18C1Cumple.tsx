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

// (el ancho de mesa es 1080; ya no hace falta como constante: la portada perdió el logotipo)
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

/**
 * ══════════════════════════════════════════════════════════════════════════
 * RONDA 4 · Eli, 25-09-2026 — «le faltan unos toques de color»
 * ══════════════════════════════════════════════════════════════════════════
 *   «agrega una foto de la nueva sesión de habitación (…) en la última slide,
 *   agrega al slide 2 y 3 algunos cuadros de color fucsia de piso18 (…). Otro
 *   elemento al slide 2 que sea foto más fiestera de cumpleaños pero cambia
 *   rostros.» Y aclaró: «yo decía las fotos, reemplazando las actuales».
 *   Después sumó: «agrega iconos a los beneficios (…), agregar botón al último
 *   en un rectángulo o botón».
 *
 * ⚠️ VERSIÓN 3 (misma ronda), Eli: la fiesta «se ve bastante falsa» → se
 *   rehizo más real (flash de fotógrafo de eventos, grano, gesto no posado),
 *   SOLO las dos chicas con los mismos vestidos (ref `base/ref-vestidos.jpg`,
 *   recorte de la v2) y más oscura. Los íconos «no se visualizan» → en la
 *   lista van NÚMEROS en los cuadros y los íconos pasan grandes a una fila
 *   sobre el titular, igual en la slide 3. El botón se sacó: el cierre vuelve
 *   a la línea de la ronda 3. La habitación pasa a `sep_26-313` (ventana,
 *   lámpara, chaise y la bandeja): «más vistosa, con ventana, cama y el
 *   desayuno real». Caja 3840×4800 desde (0,480).
 *   Lo de abajo describe la v2 y queda como historia; los números de la v3
 *   mandan.
 *
 * ⇒ Las fotos REEMPLAZAN el fondo (una 1ª prueba las puso de recuadro y no
 *   era eso):
 * · Slide 2: fiesta PRODUCIDA con Seedream 5 Pro, tomando como referencia la
 *   foto «¡Fiesta, barra libre y karaoke!» del carrusel publicado
 *   (`ref-cumple/actual-3.png`, recorte 60,1470→2190,2560). Misma luz y estelas
 *   de color, **personas distintas**. El prompt fija el grupo en la mitad de
 *   arriba y el 40 % inferior oscuro y desenfocado, que es donde va la lista.
 *   1770×2360 → upscaler de PRECISIÓN ×2 (3536×4720) → 4:5 desde y=0 → 2400×3000.
 * · Slide 3: `sep_26-318` de la sesión `Hotel general sesión SEP 2026`
 *   (Drive 117N-uJjrMSwWj_4Y2cSIH4IwsmMkapQM): la habitación en penumbra arriba
 *   y la bandeja de desayuno sobre la cama abajo, o sea el beneficio «incluye
 *   desayuno». Caja 3840×4800 desde (0,480) en el original 3840×5760 → 2400×3000
 *   (R-17). La 276 (cama completa) se descartó: la sábana blanca caía justo
 *   debajo del texto.
 *   ⇒ Por eso en esta slide el texto SUBE al tercio oscuro de arriba y la
 *   bandeja queda libre abajo.
 * · Los «cuadros fucsia» son el soporte de los íconos: cada beneficio lleva
 *   un cuadro `#D4145A` con el ícono de línea en blanco. ⚠️ Esto estira R-03
 *   («el fucsia nunca decora») a propósito: lo pidió Eli, que firma el criterio
 *   de esta marca.
 * · El botón es el de la marca (`P18.botones.lleno`, píldora fucsia con texto
 *   blanco), el mismo de las historias aprobadas.
 */

/**
 * Íconos: Phosphor Icons 2.1.1, variante DUOTONE (licencia MIT,
 * phosphoricons.com), trazados copiados tal cual sobre su grilla de 256.
 * Ronda 4 v4, Eli: los dibujados a mano «se ven muy extraños» y pidió
 * «iconos que se vean mejor y más desarrollados». El duotone suma un relleno
 * blanco suave (opacidad 0,22) bajo la línea, que es lo que les da volumen.
 * globo=balloon · musica=headphones · coctel=martini · copas=champagne ·
 * cama=bed · invitados=users-three
 */
const ICONOS = {
  globo: (
    <>
      <path d="M137.89,199.13h0L152,232H104l14.09-32.87h0C78.59,192.18,48,144.83,48,104a80,80,0,0,1,160,0C208,144.83,177.41,192.18,137.89,199.13Z" opacity={0.22} />
      <path d="M128,16a88.1,88.1,0,0,0-88,88c0,23.43,9.4,49.42,25.13,69.5,12.08,15.41,26.5,26,41.91,31.09L96.65,228.85A8,8,0,0,0,104,240h48a8,8,0,0,0,7.35-11.15L149,204.59c15.4-5.07,29.83-15.68,41.91-31.09C206.6,153.42,216,127.43,216,104A88.1,88.1,0,0,0,128,16Zm11.87,208H116.13l6.94-16.19c1.64.12,3.28.19,4.93.19s3.29-.07,4.93-.19Zm38.4-60.37C163.94,181.93,146.09,192,128,192s-35.94-10.07-50.27-28.37C64.12,146.27,56,124,56,104a72,72,0,0,1,144,0C200,124,191.88,146.27,178.27,163.63Zm-1-59.74A8.52,8.52,0,0,1,176,104a8,8,0,0,1-7.88-6.68,41.29,41.29,0,0,0-33.43-33.43,8,8,0,1,1,2.64-15.78,57.5,57.5,0,0,1,46.57,46.57A8,8,0,0,1,177.32,103.89Z" />
    </>
  ),
  musica: (
    <>
      <path d="M80,144v40a16,16,0,0,1-16,16H48a16,16,0,0,1-16-16V128H64A16,16,0,0,1,80,144Zm112-16a16,16,0,0,0-16,16v40a16,16,0,0,0,16,16h16a16,16,0,0,0,16-16V128Z" opacity={0.22} />
      <path d="M201.89,54.66A104.08,104.08,0,0,0,24,128v56a24,24,0,0,0,24,24H64a24,24,0,0,0,24-24V144a24,24,0,0,0-24-24H40.36A88,88,0,0,1,128,40h.67a87.71,87.71,0,0,1,87,80H192a24,24,0,0,0-24,24v40a24,24,0,0,0,24,24h16a24,24,0,0,0,24-24V128A103.41,103.41,0,0,0,201.89,54.66ZM64,136a8,8,0,0,1,8,8v40a8,8,0,0,1-8,8H48a8,8,0,0,1-8-8V136Zm152,48a8,8,0,0,1-8,8H192a8,8,0,0,1-8-8V144a8,8,0,0,1,8-8h24Z" />
    </>
  ),
  coctel: (
    <>
      <path d="M200,72l-72,72L56,72Z" opacity={0.22} />
      <path d="M237.66,45.66A8,8,0,0,0,232,32H24a8,8,0,0,0-5.66,13.66L120,147.31V208H88a8,8,0,0,0,0,16h80a8,8,0,0,0,0-16H136V147.31ZM75.31,80H180.69L128,132.69ZM212.69,48l-16,16H59.31l-16-16Z" />
    </>
  ),
  copas: (
    <>
      <path d="M120,176c-44.7,0-43.7-57.87-35.8-104h71.6C163.7,118.13,164.7,176,120,176Z" opacity={0.22} />
      <path d="M149.91,13.53A8,8,0,0,0,142.3,8H97.71a8,8,0,0,0-7.61,5.53,451,451,0,0,0-14.21,59.7c-7.26,44.25-4.35,75.76,8.65,93.66A40,40,0,0,0,112,183.42V232H96a8,8,0,1,0,0,16h48a8,8,0,0,0,0-16H128V183.42a39.94,39.94,0,0,0,27.46-16.53c13-17.9,15.92-49.41,8.66-93.66A451,451,0,0,0,149.91,13.53ZM103.59,24h32.83c3.06,10.19,6.77,24.42,9.8,40H93.8C96.83,48.42,100.53,34.19,103.59,24Zm38.93,133.48C137.38,164.56,130,168,120,168s-17.37-3.44-22.51-10.51C85.9,141.54,86.55,110,91,80H149C153.47,110,154.12,141.52,142.52,157.48ZM232,52a12,12,0,1,1-12-12A12,12,0,0,1,232,52ZM184,20a12,12,0,1,1,12,12A12,12,0,0,1,184,20Zm24,80a12,12,0,1,1-12-12A12,12,0,0,1,208,100Z" />
    </>
  ),
  cama: (
    <>
      <path d="M248,112v56H112V80H216A32,32,0,0,1,248,112Z" opacity={0.22} />
      <path d="M216,72H32V48a8,8,0,0,0-16,0V208a8,8,0,0,0,16,0V176H240v32a8,8,0,0,0,16,0V112A40,40,0,0,0,216,72ZM32,88h72v72H32Zm88,72V88h96a24,24,0,0,1,24,24v48Z" />
    </>
  ),
  invitados: (
    <>
      <path d="M168,144a40,40,0,1,1-40-40A40,40,0,0,1,168,144ZM64,56A32,32,0,1,0,96,88,32,32,0,0,0,64,56Zm128,0a32,32,0,1,0,32,32A32,32,0,0,0,192,56Z" opacity={0.22} />
      <path d="M244.8,150.4a8,8,0,0,1-11.2-1.6A51.6,51.6,0,0,0,192,128a8,8,0,0,1,0-16,24,24,0,1,0-23.24-30,8,8,0,1,1-15.5-4A40,40,0,1,1,219,117.51a67.94,67.94,0,0,1,27.43,21.68A8,8,0,0,1,244.8,150.4ZM190.92,212a8,8,0,1,1-13.85,8,57,57,0,0,0-98.15,0,8,8,0,1,1-13.84-8,72.06,72.06,0,0,1,33.74-29.92,48,48,0,1,1,58.36,0A72.06,72.06,0,0,1,190.92,212ZM128,176a32,32,0,1,0-32-32A32,32,0,0,0,128,176ZM72,120a8,8,0,0,0-8-8A24,24,0,1,1,87.24,82a8,8,0,1,0,15.5-4A40,40,0,1,0,37,117.51,67.94,67.94,0,0,0,9.6,139.19a8,8,0,1,0,12.8,9.61A51.6,51.6,0,0,1,64,128,8,8,0,0,0,72,120Z" />
    </>
  ),
};

/**
 * Un beneficio: cuadro fucsia con su NÚMERO + el texto. Ronda 4 v3, Eli:
 * «los iconos de esa slide siento que no se visualizan nada (…) mi solución
 * sería que fueran solamente un número, uno, dos, tres, cuatro, en esos
 * cuadraditos». La cifra va en IvyPresto: en esta marca las cifras son serif
 * (R-08), y Raleway trae cifras de estilo antiguo que bajan de la línea.
 */
const Beneficio: React.FC<{
  n: number;
  cuerpo: number;
  aire: number;
  children: React.ReactNode;
}> = ({n, cuerpo, aire, children}) => {
  const lado = Math.round(cuerpo * 1.5);
  return (
    <div style={{display: 'flex', alignItems: 'flex-start', gap: cuerpo * 0.62, marginTop: aire}}>
      <div
        style={{
          flex: 'none',
          width: lado,
          height: lado,
          backgroundColor: P18.colores.fucsia,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          // la primera línea del texto queda centrada con el cuadro
          marginTop: (cuerpo * 1.42 - lado) / 2,
          fontFamily: P18.fuentes.titular,
          fontWeight: 400,
          fontSize: cuerpo * 1.02,
          lineHeight: 1,
          color: P18.colores.blanco,
        }}
      >
        {n}
      </div>
      <div
        style={{
          fontFamily: P18.fuentes.texto,
          fontWeight: 500,
          fontSize: cuerpo,
          lineHeight: 1.42,
          color: P18.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        {children}
      </div>
    </div>
  );
};

/**
 * Los íconos, ahora GRANDES y en fila sobre el titular: «colocar los iconos
 * en la parte de arriba de ese mismo slide, los cuatro iconos que destacan».
 * Mismo cuadro fucsia que los números, para que fila y lista se lean como un
 * solo sistema. Va igual en la slide 3 («que la tercera se parezca a la 2»).
 */
const FilaIconos: React.FC<{iconos: (keyof typeof ICONOS)[]; lado?: number}> = ({
  iconos,
  lado = 78,
}) => (
  <div style={{display: 'flex', gap: 18, marginBottom: 40}}>
    {iconos.map((ic) => (
      <div
        key={ic}
        style={{
          width: lado,
          height: lado,
          // Ronda 4 v4, Eli: «en un cuadro con borde blanco en transparencia».
          // Sin relleno: la foto se ve a través. El fucsia queda para los números.
          border: `2px solid ${P18.colores.blanco}`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          filter: 'drop-shadow(0 2px 10px rgba(0,0,0,0.35))',
        }}
      >
        <svg viewBox="0 0 256 256" width={lado * 0.58} height={lado * 0.58} fill={P18.colores.blanco}>
          {ICONOS[ic]}
        </svg>
      </div>
    ))}
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
        ⛔⛔ ESTA PORTADA NO LLEVA LOGOTIPO — ronda 3 de Eli, 15-09-2026.
        *«Y bórrale el logo, muy repetitivo.»*

        Manda sobre lo que dice la gramática medida más arriba («portada: foto a
        sangre + logotipo completo blanco arriba») y sobre la instrucción que el
        cliente había dado para el carrusel del 22-09 («logo en la primera G»).
        El motivo es de FEED, no de pieza: la marca ya viene firmando las piezas
        vecinas del mes y repetirla acá no suma.

        ⇒ Y con el logotipo se va también el velo superior, que existía sólo para
        sostenerlo. Sin él la foto entra limpia y a sangre, que es lo que el brief
        pide para esta slide («Texto: Sin texto»).

        ⚠️ No se generaliza: es el criterio de Eli PARA ESTA PORTADA. En el
        carrusel aprobado `C2 S1 n°1` el logotipo va, y ahí sigue.
      */}
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────────────────────────────────────
// SLIDE 2 · LO QUE INCLUYE — la fiesta + los cuatro puntos con ícono.
// ───────────────────────────────────────────────────────────────────────────
export const P18C1CumpleS2: React.FC = () => {
  cargarFuentesP18();
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Img
        src={staticFile('assets/hilton/piso18/s5-fiesta.jpg')}
        style={{width: '100%', height: '100%', objectFit: 'cover'}}
      />
      {/* «dejarlo un poco más oscurecido»: un velo parejo sobre toda la foto,
          además del de pie que sostiene el texto. */}
      <AbsoluteFill style={{backgroundColor: 'rgba(8,8,10,0.22)'}} />
      <VeloPie hasta={0.66} opacidad={0.9} />

      {/* El bloque va ABAJO: la foto se produjo con las dos chicas arriba y el
          40 % inferior en penumbra justamente para esto. */}
      <div style={{position: 'absolute', left: 92, right: 92, bottom: 110}}>
        <FilaIconos iconos={['globo', 'musica', 'coctel', 'copas']} />
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

        <div style={{marginTop: 40}}>
          <Beneficio n={1} cuerpo={32} aire={0}>
            Ambientación y decoración
          </Beneficio>
          <Beneficio n={2} cuerpo={32} aire={20}>
            DJ en vivo, iluminación y amplificación
          </Beneficio>
          <Beneficio n={3} cuerpo={32} aire={20}>
            Cóctel, estaciones temáticas y trasnoche
          </Beneficio>
          <Beneficio n={4} cuerpo={32} aire={20}>
            ¡Fiesta y barra libre!
          </Beneficio>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────────────────────────────────────
// SLIDE 3 · EL REGALO — la habitación con desayuno + los dos beneficios + CTA.
// ───────────────────────────────────────────────────────────────────────────
export const P18C1CumpleS3: React.FC = () => {
  cargarFuentesP18();
  return (
    <AbsoluteFill style={{backgroundColor: P18.colores.tinta}}>
      <Img
        src={staticFile('assets/hilton/piso18/s5-habitacion.jpg')}
        style={{width: '100%', height: '100%', objectFit: 'cover'}}
      />
      {/*
        Velo de ARRIBA: en `sep_26-313` la ventana con visillo es lo más claro
        de la foto y cae justo detrás del texto. El velo se apaga antes de la
        bandeja, que tiene que quedar limpia: es el desayuno del beneficio.
      */}
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to bottom, rgba(8,8,10,0.66) 0%, rgba(8,8,10,0.58) 34%, rgba(8,8,10,0.30) 48%, rgba(8,8,10,0) 58%)',
        }}
      />

      <div style={{position: 'absolute', left: 92, right: 92, top: 96}}>
        <FilaIconos iconos={['cama', 'invitados']} />
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
          <Beneficio n={1} cuerpo={29} aire={0}>
            Estadía de regalo en DoubleTree by Hilton (incluye desayuno y late check-out).
          </Beneficio>
          <Beneficio n={2} cuerpo={29} aire={20}>
            {/* La «T» de «Tarifa» va en mayúscula porque así está en el brief, y los
                textos en pantalla van literales. No es un error de tipeo. */}
            Beneficios para invitados: Tarifa preferencial en habitaciones y estacionamiento
            liberado.
          </Beneficio>
        </div>

        {/*
          El cierre VUELVE a ser la línea de la ronda 3 («me gusta más como estaba
          en el anterior (…) sin ese botón»): Raleway blanca y `piso18.cl` en el
          fucsia oficial. Cambia sólo de lugar: abajo ahora está la bandeja, con
          platos blancos que no sostienen texto blanco, así que sube al bloque.
        */}
        <div
          style={{
            marginTop: 40,
            fontFamily: P18.fuentes.texto,
            fontWeight: 700,
            fontSize: 28,
            letterSpacing: 0.3,
            color: P18.colores.blanco,
            textShadow: SOMBRA,
          }}
        >
          Cotiza tu cumpleaños en <span style={{color: P18.colores.fucsia}}>piso18.cl</span>
        </div>
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
