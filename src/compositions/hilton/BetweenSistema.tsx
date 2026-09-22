/**
 * Sistema gráfico BETWEEN Coffee & Bar — feed, stories y paid.
 *
 * Cada regla de acá viene del feedback de Elisabet Soto (24-08-2026):
 *  - Raleway ExtraBold para titulares en mayúscula; Brushwell solo para títulos
 *    o una palabra clave; máximo 2 familias por pieza.
 *  - Texto beige #fff9eb sobre foto; café #675b49 cuando el fondo es muy claro.
 *  - La foto se oscurece con una capa MULTIPLY lo menos notoria posible.
 *  - Los títulos NUNCA llevan punto final. Bajadas de máximo 3 líneas.
 *  - Respiro y jerarquía: nunca saturar de texto. Marca juvenil con algo de estatus.
 *  - Márgenes: los iconos de Instagram no pueden tapar texto importante.
 */
import React from 'react';
import {
  AbsoluteFill,
  Img,
  continueRender,
  delayRender,
  interpolate,
  staticFile,
  useCurrentFrame,
} from 'remotion';
import {BETWEEN, cargarFuentesBetween, sinPuntoFinal} from '../../brand/hilton-between';

cargarFuentesBetween();

type Tono = 'beige' | 'cafe';
const tinta = (tono: Tono) => (tono === 'cafe' ? BETWEEN.colores.cafe : BETWEEN.colores.beige);

/** Sombra sutil solo cuando el texto va sobre foto (legibilidad en reels/stories). */
const sombraSobreFoto = '0 2px 14px rgba(36,26,18,0.45)';

/* ══════════════════ CIFRAS TABULARES ══════════════════
   ⭐ 01-09-2026, Eli: «los precios debes hacer que se vean opentype tabular,
   como en adobe illustrator, así los números no se ven desordenados».

   ⛔ El camino obvio NO funciona y estuvo puesto sin efecto varios días:
   `fontVariantNumeric: 'tabular-nums'` y `fontFeatureSettings: '"tnum" 1'`
   le piden la función a la FUENTE, y **ningún Raleway del repo trae `tnum`**.
   Verificado leyendo la tabla GSUB/GPOS de los cinco pesos instalados y de la
   variable: la única función numérica que traen es `lnum`. O sea que el CSS
   estaba ahí decorando, igual que el @font-face de Brushwell que fallaba en
   silencio. En Illustrator pasa lo mismo: el «Tabular Lining» del panel
   OpenType no tiene efecto con Raleway.

   Los dígitos de Raleway son PROPORCIONALES. Medido en ExtraBold sobre un em
   de 1000 unidades:
     0=614 · 1=518 · 2=580 · 3=569 · 4=578 · 5=558 · 6=608 · 7=576 · 8=607 · 9=589
   El «1» es 18,5 % más angosto que el «0»: por eso una columna de precios queda
   dispareja y las horas bailan.

   La solución es construir la cifra tabular a mano: cada dígito centrado en una
   caja del ancho del dígito MÁS ANCHO. Es exactamente lo que hace una fuente con
   cifras tabulares, y acá además es verificable midiendo el render. */

/* ⛔ EL INTENTO QUE SE RECHAZÓ DOS VECES — y por qué, exactamente.
   El 01-09 y otra vez el 02-09, Eli vio la story To Go rendida con esto puesto y
   lo devolvió: «los textos y números vuelven a verse extraños, en la anterior
   estaba mejor» y después «el error persiste en los números».

   Las dos veces la caja tabular tenía el ancho del «0», el dígito MÁS GORDO. Con
   eso el «1» —que en Raleway es entre 16 % y 38 % más angosto según el peso—
   queda centrado en una caja que le sobra por los dos lados, y «10:00» se lee
   «1 0:00». O sea que el defecto que la tabular venía a arreglar quedaba peor.

   ⚠️ Durante un día la conclusión escrita acá fue «en texto corrido van
   PROPORCIONALES, no lo toques». Era la conclusión equivocada del experimento
   correcto: el problema no era usar tabular en una frase, era el ancho.

   ⭐⭐⭐ 02-09-2026 — RESUELTO, Y NO ERA «tabular sí o no»

   Eli lo pidió por TERCERA vez: «el error persiste en los números, debe verse
   armonioso y parejo». Las dos veces anteriores se probó la caja tabular con el
   ancho del «0» y se rechazó. El error estuvo en el ANCHO de la caja, no en la
   idea.

   Se midió con la fuente real (`fontTools`, no de oído) y se rindió una prueba
   de cuatro tratamientos sobre «$3.790» y «08:00 a 10:00 hrs»:

     1. proporcional          → «10» queda apretado contra el «0»; las dos horas
                                no parecen hermanas. Es el defecto original.
     2. tabular al ancho del  → el «1» queda AISLADO con hueco a los dos lados.
        «0» (lo que había)      «10:00» se lee «1 0:00». Es lo que Eli rechazó.
     3. tabular al ancho      → ⭐ el bueno. Alinea los dígitos —las horas sí
        MEDIO del peso           quedan hermanas— y el «1» no flota, porque la
                                 caja ya no se estira hasta el dígito más gordo.
     4. proporcional + track  → mejora algo, pero el «1» sigue apretado.

   El ancho medio depende del PESO, y mucho: el «1» de Raleway va de 518/1000 en
   ExtraBold a 450 en Medium y 375 en la variable. Por eso el ancho no puede ser
   una constante única — se pasa el del peso que se está usando. */

/**
 * Ancho de la caja tabular, en em, POR PESO. Es el promedio de los diez dígitos
 * de ese archivo, medido con fontTools sobre los .ttf del repo.
 *
 * ⛔ NO usar el ancho del «0» (0,614): es el máximo y deja al «1» flotando.
 * Con el promedio, los dígitos anchos (0, 6, 8) sobresalen unas 30 milésimas de
 * em a cada lado de su caja — invisible, porque los glifos ya traen su propio
 * espacio lateral— y los angostos dejan de abrir hueco.
 */

/**
 * ⭐⭐⭐ CIFRAS DE CAJA ALTA — la mitad que faltaba, 03-09-2026.
 *
 * Eli, sobre el carrusel To Go: «los números se ven desordenados… aplica
 * OpenType tabular tal cual como se hace en Adobe Illustrator, los números no se
 * ven uno más arriba y abajo que los otros».
 *
 * «Uno más arriba y abajo que los otros» NO es avance horizontal: son **cifras
 * de estilo antiguo**. Y estaban puestas porque **Raleway las trae por
 * DEFECTO**: verificado con fontTools sobre los .ttf del repo, la fuente NO
 * tiene `onum` —no hace falta, es su default— y `lnum` es la función que las
 * sube a caja alta. En «$4.290» el 4 y el 9 bajaban de la línea base y el 2 y
 * el 0 quedaban a altura de x.
 *
 * ⛔ Y esto se había perdido: el manual §9 dice que `lnum` se activó junto con
 * `tnum`, pero cuando se comprobó que `tnum` no existe en la fuente se borró la
 * declaración ENTERA — y con ella se fue el `lnum`, que sí funcionaba.
 *
 * ⚠️ Activarlo CAMBIA los avances, así que no es sólo una línea de CSS: los
 * glifos `.lf` son más anchos (el «0» de ExtraBold pasa de 614 a **707**, un
 * 15 %). Por eso las dos tablas de arriba están re-medidas sobre los glifos de
 * caja alta; si alguien quita el `lnum`, hay que volver a las viejas.
 */
export const CIFRAS_ALTAS: React.CSSProperties = {
  fontVariantNumeric: 'lining-nums',
  fontFeatureSettings: '"lnum" 1',
};

/**
 * Avance REAL de cada dígito, en em, por peso. Medido con `fontTools` sobre los
 * .ttf del repo (em de 1000 → se divide por 1000).
 *
 * Hace falta para COMPENSAR LOS BORDES de cada grupo de dígitos: sin eso, el
 * hueco de la caja tabular del primer dígito se suma al espacio de la palabra
 * anterior. Es el defecto que Eli marcó en la story del 3-sep — entre la «a» y
 * el «10» se veía un espacio doble.
 */
export const ANCHOS_DIGITO_POR_PESO: Record<number, number[]> = {
  //     0     1     2     3     4     5     6     7     8     9
  500: [.690, .441, .590, .585, .577, .558, .606, .534, .598, .606],
  600: [.695, .465, .599, .585, .581, .563, .607, .548, .601, .606],
  800: [.707, .518, .619, .586, .591, .575, .608, .579, .607, .607],
};

/**
 * ⛔⛔ LA CAJA TABULAR ES EL DÍGITO MÁS ANCHO, NO EL PROMEDIO. Corregido el
 * 14-09-2026 con un defecto que Eli cazó mirando: «los numeros y letras se están
 * acercando mucho se solapan».
 *
 * Estaba puesta en el PROMEDIO de los diez dígitos (ExtraBold: 599,7 → 0,600) y
 * el «0» de ExtraBold mide **707**. O sea que la caja era un 18 % más angosta
 * que el glifo más ancho, y `sobra = (caja − real) / 2` salía NEGATIVA: el cero
 * se desbordaba 53 milésimas de em por cada lado. En «08:00 A 10:00 HRS.», que
 * son puros ceros, cada uno se comía el aire del siguiente y se tocaban.
 *
 * El promedio no puede funcionar por definición: una caja tabular sólo alinea si
 * cabe el dígito más ancho. Ahora se calcula como el MÁXIMO de la fila medida,
 * así que no puede volver a desajustarse si alguien re-mide la fuente.
 *
 * ⚠️ Ensancha las tiradas de cifras (~0,107 em por dígito en ExtraBold). En una
 * línea larga puede sangrar el ancho disponible: `between-qa.py` lo marca y se
 * baja el cuerpo. Verificado sobre las cuatro piezas del carrusel To Go.
 */
const _maxFila = (peso: number) => Math.max(...ANCHOS_DIGITO_POR_PESO[peso]);

export const ANCHO_CIFRA_EM_POR_PESO: Record<number, number> = {
  /** Raleway-Medium (500): el más ancho es el «0» con 690. */
  500: _maxFila(500),
  /** Raleway-SemiBold (600): el más ancho es el «0» con 695. */
  600: _maxFila(600),
  /** Raleway-ExtraBold (800): el más ancho es el «0» con 707. */
  800: _maxFila(800),
};

/** Por defecto, el peso de los datos y precios de la marca (ExtraBold). */
export const ANCHO_CIFRA_EM = ANCHO_CIFRA_EM_POR_PESO[800];

/**
 * Envuelve cada dígito de `texto` en una caja de ancho fijo para que todas las
 * cifras avancen igual. Los signos ($ . : , espacios) quedan intactos: en una
 * fuente tabular tampoco se ensanchan.
 *
 * ⚠️ Dentro de la caja el tracking se anula (`letterSpacing: 'normal'`), porque
 * si no el letter-spacing heredado se suma DENTRO del cuadro y descentra el
 * dígito. Úsalo en textos de dato y precio, que van sin tracking; no en el
 * titular, que compone con −0,024em.
 */
export const cifrasTabulares = (
  texto: string,
  /** Peso con el que se está pintando: decide el ancho de la caja. */
  peso: number = 800,
  /**
   * ⭐⭐ Tracking en `em` que la línea lleva por CSS, para replicarlo dentro de
   * la caja tabular. Añadido el 08-09-2026, y arregla un defecto real:
   *
   * cada cifra va en un `inline-block`, y **Chrome no le aplica `letter-spacing`
   * a una caja atómica** — sí a los caracteres de texto. O sea que en una línea
   * con tracking abierto las LETRAS se separan y las CIFRAS no: medido en
   * «08:00 A 22:00 HRS.» a 0,10em, las letras quedaban con 5,8–10,6 px de hueco
   * y los dígitos de cada grupo **pegados** (0,5 y 2,9 px). Se veía como si la
   * hora estuviera en otra tipografía.
   *
   * Se replica como `marginRight` en cada dígito, que es lo que hace
   * `letter-spacing` con un carácter normal. Por defecto 0, así que ninguna
   * pieza ya aprobada cambia.
   */
  trackingEm: number = 0,
): React.ReactNode => {
  const caja = ANCHO_CIFRA_EM_POR_PESO[peso] ?? ANCHO_CIFRA_EM;
  const reales = ANCHOS_DIGITO_POR_PESO[peso] ?? ANCHOS_DIGITO_POR_PESO[800];

  /* Se recorre agrupando los dígitos CONSECUTIVOS en «grupos». El grupo es la
     unidad que importa: dentro de él los dígitos avanzan todos igual (que es lo
     que alinea las cifras), y en sus DOS BORDES se descuenta el hueco con un
     margen negativo, para que el grupo quede a ras del texto que lo rodea.

     Sin esa compensación, el hueco izquierdo de la caja del primer dígito se
     SUMA al espacio anterior: en «a 10:00» se veía un espacio doble, porque el
     «1» de Raleway Medium mide 450/1000 contra una caja de 557. Con el
     descuento, ese borde queda pegado y el hueco se reparte sólo por DENTRO del
     grupo, donde cae entre dos cifras y se lee como espaciado normal —en «10»
     quedan 25 milésimas de em, ~1 px a cuerpo 40. */
  const trozos: React.ReactNode[] = [];
  let i = 0;
  let k = 0;
  while (i < texto.length) {
    if (!/\d/.test(texto[i])) {
      // texto normal: se acumula hasta el próximo dígito
      let j = i;
      while (j < texto.length && !/\d/.test(texto[j])) j++;
      trozos.push(texto.slice(i, j));
      i = j;
      continue;
    }
    let j = i;
    while (j < texto.length && /\d/.test(texto[j])) j++;
    const grupo = texto.slice(i, j);
    grupo.split('').forEach((d, n) => {
      const sobra = (caja - reales[Number(d)]) / 2;
      trozos.push(
        <span
          key={`d${k++}`}
          style={{
            display: 'inline-block',
            width: `${caja}em`,
            textAlign: 'center',
            letterSpacing: 'normal',
            // la función viaja PEGADA a la caja: si un día se hereda otra cosa,
            // el glifo y el ancho medido siguen siendo el mismo par.
            ...CIFRAS_ALTAS,
            // los bordes del grupo van a ras; el interior reparte el hueco.
            // Y al margen derecho se le SUMA el tracking de la línea, porque la
            // caja es atómica y `letter-spacing` no la alcanza (ver arriba).
            marginLeft: n === 0 ? `${-sobra}em` : undefined,
            marginRight: `${(n === grupo.length - 1 ? -sobra : 0) + trackingEm}em`,
          }}
        >
          {d}
        </span>,
      );
    });
    i = j;
  }
  return trozos;
};

/** ¿Vale la pena pasar por `cifrasTabulares`? Evita envolver texto sin dígitos. */
export const tieneCifras = (texto: string) => /\d/.test(texto);

/**
 * Versión tolerante para componentes que reciben `children: React.ReactNode`:
 * si lo que llega es texto plano con dígitos lo pasa por la caja tabular, y si
 * es cualquier otra cosa (un nodo ya armado) lo deja intacto.
 */
export const conCifras = (
  hijos: React.ReactNode,
  peso: number = 800,
  /** Tracking de la línea, en `em`. Ver `cifrasTabulares`. */
  trackingEm: number = 0,
): React.ReactNode =>
  typeof hijos === 'string' && tieneCifras(hijos)
    ? cifrasTabulares(hijos, peso, trackingEm)
    : hijos;

/* ---------- foto de fondo + multiply ---------- */

export const FotoFondo: React.FC<{
  src: string;
  posicion?: string;
  /** Intensidad del multiply. Lo más bajo que permita leer el texto. */
  oscurecer?: number;
}> = ({src, posicion = 'center', oscurecer = 0.28}) => (
  <AbsoluteFill>
    <Img
      src={staticFile(src)}
      style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: posicion}}
    />
    <AbsoluteFill
      style={{
        backgroundColor: BETWEEN.colores.sombra,
        opacity: oscurecer,
        mixBlendMode: 'multiply',
      }}
    />
  </AbsoluteFill>
);

/* ---------- logo ---------- */

export const LogoBetween: React.FC<{
  formato?: 'feed' | 'story' | 'paid';
  /** Eli entrega dos plantillas por formato: logo arriba y logo abajo. */
  posicion?: 'arriba' | 'abajo';
  tono?: Tono;
  /** Ancho en px. Se escala por ancho y el alto sale del ratio — nunca achatado. */
  ancho?: number;
  y?: number;
  /**
   * ⭐ Halo bajo el logo — pedido de Eli el 02-09-2026: «agrega debajo del logo
   * una sombra con opacidad para que se vea el logo bien, muy sutil».
   *
   * Es una elipse difuminada del color sombra de la marca, DEBAJO del logotipo,
   * que asienta el lockup cuando la foto trae hojas y cielo detrás. No es un
   * `textShadow` —el logo es un PNG, no texto— ni oscurecer la foto, que el
   * manual prohíbe.
   *
   * Se pasa la opacidad del centro (0 = sin halo). **0,22 es «muy sutil»**: el
   * degradado se apaga a transparente al 70 % del radio, así que el promedio
   * sobre la caja del logo queda muy por debajo de ese número y no se ve un
   * parche. Por encima de ~0,35 empieza a notarse el óvalo.
   */
  sombra?: number;
}> = ({formato = 'feed', posicion = 'arriba', tono = 'beige', ancho, y, sombra}) => {
  const clave = (formato === 'story' ? 'story' : 'post') + (posicion === 'abajo' ? 'LogoAbajo' : 'LogoArriba');
  const g = BETWEEN.margenes[clave as keyof typeof BETWEEN.margenes] as {
    wordmarkY: number;
    ancho: number;
  };
  const anchoFinal = ancho ?? g.ancho;
  const altoFinal = anchoFinal / BETWEEN.logo.ratio;
  const arriba = y ?? g.wordmarkY;
  // El lockup es el wordmark MÁS el «COFFEE & BAR» de abajo, que cae fuera del
  // alto del PNG: el halo se centra un poco más abajo del centro del archivo y
  // se estira en vertical para cubrir las dos líneas.
  return (
    <>
      {sombra ? (
        <div
          style={{
            position: 'absolute',
            top: arriba + altoFinal * 0.9,
            left: '50%',
            transform: 'translate(-50%, -50%)',
            width: anchoFinal * 2.2,
            height: altoFinal * 5.2,
            background: `radial-gradient(ellipse at center, rgba(36,26,18,${sombra}) 0%, `
              + `rgba(36,26,18,${(sombra * 0.45).toFixed(3)}) 42%, rgba(36,26,18,0) 72%)`,
            pointerEvents: 'none',
          }}
        />
      ) : null}
      <Img
        src={staticFile(tono === 'cafe' ? BETWEEN.logo.cafe : BETWEEN.logo.beige)}
        style={{
          position: 'absolute',
          top: arriba,
          left: '50%',
          transform: 'translateX(-50%)',
          width: anchoFinal,
          height: altoFinal,
        }}
      />
    </>
  );
};

/* ---------- tipografía ---------- */

/**
 * Brushwell (como Kallimata) no trae «¡» ni «¿». Eli resuelve exactamente así:
 * usa el «!» y el «?» girados 180°, que están bien construidos y calzan.
 * Solo aplica a la script — Raleway sí trae los signos de apertura.
 */
const signosVolteados = (texto: string): React.ReactNode[] =>
  [...texto].map((ch, i) =>
    ch === '\u00a1' || ch === '\u00bf' ? (
      <span key={i} style={{display: 'inline-block', transform: 'rotate(180deg)'}}>
        {ch === '\u00a1' ? '!' : '?'}
      </span>
    ) : (
      ch
    ),
  );


/**
 * Halo continuo alrededor del texto: 24 copias del glifo en círculo. 24 pasos
 * porque a radio 6 la separación entre copias vecinas queda en 1,6 px —menos
 * que el grosor de cualquier asta—, así que el borde sale macizo y no dentado.
 */
const haloSticker = (radio: number, color: string): string =>
  Array.from({length: 24}, (_, i) => {
    const a = (i / 24) * Math.PI * 2;
    return `${(Math.cos(a) * radio).toFixed(2)}px ${(Math.sin(a) * radio).toFixed(2)}px 0 ${color}`;
  }).join(', ');

/**
 * Titular. Regla de Eli:
 *  - Si debe DESTACAR: todo en MAYÚSCULA, ~100 (rango 40–122).
 *  - Si es sutil: 40–74 y **solo la primera letra en mayúscula** — más limpio.
 * El componente decide la caja según el tamaño para no volver a equivocarse.
 */
export const Titulo: React.FC<{
  children: string;
  size?: number;
  destacar?: boolean;
  peso?: number;
  tono?: Tono;
  sobreFoto?: boolean;
  style?: React.CSSProperties;
}> = ({
  children,
  size = BETWEEN.tipos.tituloCapsDestacado,
  destacar,
  peso,
  tono = 'beige',
  sobreFoto = true,
  style,
}) => {
  // Sobre 78 la pieza pide protagonismo → mayúsculas. Bajo eso, caja baja.
  const enMayuscula = destacar ?? size >= 78;
  return (
    <div
      style={{
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: peso ?? (enMayuscula ? BETWEEN.pesos.extrabold : BETWEEN.pesos.bold),
        fontSize: size,
        letterSpacing: enMayuscula ? 1 : 0,
        textTransform: enMayuscula ? 'uppercase' : 'none',
        color: tinta(tono),
        lineHeight: enMayuscula ? 1.05 : 1.15,
        textWrap: 'balance',
        textShadow: sobreFoto ? sombraSobreFoto : undefined,
        ...style,
      }}
    >
      {sinPuntoFinal(children)}
    </div>
  );
};

/** Alias histórico; en piezas nuevas usar <Titulo>. */
export const Caps = Titulo;

/** Brushwell. Solo títulos o una palabra clave — jamás números ni párrafos. */
export const Script: React.FC<{
  children: string;
  size?: number;
  tono?: Tono;
  sobreFoto?: boolean;
  style?: React.CSSProperties;
}> = ({children, size = BETWEEN.tipos.scriptSolo, tono = 'beige', sobreFoto = true, style}) => (
  <div
    style={{
      fontFamily: BETWEEN.fuentes.script,
      fontSize: size,
      color: tinta(tono),
      lineHeight: 1.0,
      textShadow: sobreFoto ? sombraSobreFoto : undefined,
      ...style,
    }}
  >
    {signosVolteados(sinPuntoFinal(children))}
  </div>
);

/**
 * Título mixto: línea en Raleway caps + línea en Brushwell.
 * La script sale automáticamente ~20% más grande para equilibrar el peso visual.
 */
export const TituloMixto: React.FC<{
  caps: string;
  script: string;
  sizeCaps?: number;
  tono?: Tono;
  orden?: 'capsPrimero' | 'scriptPrimero';
  destacar?: boolean;
  style?: React.CSSProperties;
}> = ({caps, script, sizeCaps = 72, tono = 'beige', orden = 'capsPrimero', destacar, style}) => {
  const sizeScript = Math.round(sizeCaps * BETWEEN.proporcionScript);
  const lineaCaps = <Titulo size={sizeCaps} destacar={destacar} tono={tono}>{caps}</Titulo>;
  const lineaScript = <Script size={sizeScript} tono={tono} style={{marginTop: 2}}>{script}</Script>;
  return (
    <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', ...style}}>
      {orden === 'capsPrimero' ? lineaCaps : lineaScript}
      {orden === 'capsPrimero' ? lineaScript : lineaCaps}
    </div>
  );
};

/** Bajada o párrafo. Máximo 3 líneas — se recorta el exceso en tiempo de diseño. */
export const Bajada: React.FC<{
  children: React.ReactNode;
  size?: number;
  tono?: Tono;
  sobreFoto?: boolean;
  style?: React.CSSProperties;
}> = ({children, size = BETWEEN.tipos.bajada, tono = 'beige', sobreFoto = true, style}) => (
  <div
    style={{
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.regular,
      fontSize: size,
      color: tinta(tono),
      lineHeight: 1.4,
      maxWidth: 820,
      textWrap: 'balance',
      textShadow: sobreFoto ? sombraSobreFoto : undefined,
      ...style,
    }}
  >
    {children}
  </div>
);

/**
 * Dato de cierre: horario, precio o etiqueta de producto.
 * El tracking (5–10) va SOLO si hace falta compensar la jerarquía, así que
 * `espaciado` es opcional y NO viene puesto por defecto.
 */
export const Dato: React.FC<{
  children: React.ReactNode;
  size?: number;
  tono?: Tono;
  espaciado?: boolean;
  style?: React.CSSProperties;
}> = ({children, size = 30, tono = 'beige', espaciado = false, style}) => (
  <div
    style={{
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.semibold,
      fontSize: size,
      letterSpacing: espaciado ? BETWEEN.trackingHorario : 0,
      textTransform: espaciado ? 'uppercase' : 'none',
      color: tinta(tono),
      textShadow: sombraSobreFoto,
      ...style,
    }}
  >
    {children}
  </div>
);

/** Alias histórico. */
export const Horario = Dato;

/**
 * CTA en caja: café con letras beige por defecto; se invierte cuando el fondo
 * es oscuro y el beige necesita destacar más.
 */
export const CTA: React.FC<{
  children: React.ReactNode;
  size?: number;
  invertido?: boolean;
  style?: React.CSSProperties;
}> = ({children, size = BETWEEN.tipos.cta, invertido = false, style}) => (
  <div
    style={{
      display: 'inline-block',
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.semibold,
      fontSize: size,
      color: invertido ? BETWEEN.colores.cafe : BETWEEN.colores.beige,
      backgroundColor: invertido ? BETWEEN.colores.beige : BETWEEN.colores.cafe,
      padding: '20px 44px',
      borderRadius: 6,
      ...style,
    }}
  >
    {children}
  </div>
);

/** Legales: Raleway regular o italic, 20–26, centrados y con margen. */
export const Legal: React.FC<{
  children: React.ReactNode;
  size?: number;
  italic?: boolean;
  tono?: Tono;
  style?: React.CSSProperties;
}> = ({children, size = BETWEEN.tipos.legal, italic = true, tono = 'beige', style}) => (
  <div
    style={{
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.regular,
      fontStyle: italic ? 'italic' : 'normal',
      fontSize: size,
      color: tinta(tono),
      textAlign: 'center',
      lineHeight: 1.4,
      maxWidth: 840,
      margin: '0 auto',
      textShadow: sombraSobreFoto,
      ...style,
    }}
  >
    {children}
  </div>
);

/* ---------- plantillas ---------- */

export type PiezaProps = {
  foto: string;
  posicionFoto?: string;
  oscurecer?: number;
  caps?: string;
  script?: string;
  tituloSutil?: string;
  sizeCaps?: number;
  bajada?: React.ReactNode;
  horario?: string;
  /** Tracking en el dato de cierre: solo si hace falta jerarquía. */
  espaciarHorario?: boolean;
  /** Fuerza mayúsculas en el título aunque sea chico (o al revés). */
  destacar?: boolean;
  cta?: string;
  ctaInvertido?: boolean;
  legal?: React.ReactNode;
  tono?: Tono;
  /** Cuál de las dos líneas del título va arriba. */
  ordenTitulo?: 'capsPrimero' | 'scriptPrimero';
  conLogo?: boolean;
  logoTono?: Tono;
  /** Plantilla de logo: arriba (por defecto) o abajo. */
  logoPosicion?: 'arriba' | 'abajo';
  alineacion?: 'centro' | 'abajo';
};

const BloqueTexto: React.FC<PiezaProps & {escala?: number}> = ({
  caps,
  script,
  sizeCaps,
  destacar,
  bajada,
  horario,
  espaciarHorario,
  cta,
  ctaInvertido,
  legal,
  tono = 'beige',
  ordenTitulo = 'capsPrimero',
  escala = 1,
}) => (
  <div
    style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: 22 * escala,
      textAlign: 'center',
    }}
  >
    {caps && script ? (
      <TituloMixto
        caps={caps}
        script={script}
        sizeCaps={(sizeCaps ?? 72) * escala}
        tono={tono}
        orden={ordenTitulo}
        destacar={destacar}
      />
    ) : caps ? (
      <Titulo size={(sizeCaps ?? BETWEEN.tipos.tituloCapsDestacado) * escala} destacar={destacar} tono={tono}>
        {caps}
      </Titulo>
    ) : script ? (
      <Script size={(sizeCaps ?? BETWEEN.tipos.scriptSolo) * escala} tono={tono}>
        {script}
      </Script>
    ) : null}
    {bajada ? (
      <Bajada tono={tono} size={BETWEEN.tipos.bajada * escala}>
        {bajada}
      </Bajada>
    ) : null}
    {horario ? (
      <Dato tono={tono} size={(espaciarHorario ? 29 : 36) * escala} espaciado={espaciarHorario}>
        {horario}
      </Dato>
    ) : null}
    {cta ? (
      <CTA invertido={ctaInvertido} size={BETWEEN.tipos.cta * escala} style={{marginTop: 6 * escala}}>
        {cta}
      </CTA>
    ) : null}
    {legal ? (
      <Legal tono={tono} size={BETWEEN.tipos.legal * escala}>
        {legal}
      </Legal>
    ) : null}
  </div>
);

/** Feed / slide de carrusel — 1080×1350. */
export const PiezaFeed: React.FC<PiezaProps> = (props) => {
  const {foto, posicionFoto, oscurecer, conLogo = true, logoTono = 'beige', logoPosicion = 'arriba', alineacion = 'abajo'} = props;
  return (
    <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
      <FotoFondo src={foto} posicion={posicionFoto} oscurecer={oscurecer} />
      {conLogo ? <LogoBetween formato="feed" posicion={logoPosicion} tono={logoTono} /> : null}
      <AbsoluteFill
        style={{
          justifyContent: alineacion === 'centro' ? 'center' : 'flex-end',
          alignItems: 'center',
          padding: '0 90px 96px 90px',
        }}
      >
        <BloqueTexto {...props} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/** Story — 1080×1920, respetando 250px arriba y 340px abajo de zona segura. */
export const PiezaStory: React.FC<PiezaProps> = (props) => {
  const {foto, posicionFoto, oscurecer, conLogo = true, logoTono = 'beige', logoPosicion = 'arriba'} = props;
  return (
    <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
      <FotoFondo src={foto} posicion={posicionFoto} oscurecer={oscurecer} />
      {conLogo ? <LogoBetween formato="story" posicion={logoPosicion} tono={logoTono} /> : null}
      <AbsoluteFill
        style={{
          justifyContent: 'center',
          alignItems: 'center',
          padding: '420px 90px 340px 90px',
        }}
      >
        <BloqueTexto {...props} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/** Paid media en post — 1080×1080. El logo va arriba pero más compacto. */
export const PiezaPaid: React.FC<PiezaProps> = (props) => {
  const {foto, posicionFoto, oscurecer, conLogo = true, logoTono = 'beige', logoPosicion = 'arriba'} = props;
  return (
    <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
      <FotoFondo src={foto} posicion={posicionFoto} oscurecer={oscurecer} />
      {conLogo ? <LogoBetween formato="paid" posicion={logoPosicion} tono={logoTono} /> : null}
      <AbsoluteFill
        style={{
          justifyContent: 'flex-end',
          alignItems: 'center',
          // Meta deja el 10-15% inferior para su UI
          padding: '0 80px 130px 80px',
        }}
      >
        <BloqueTexto {...props} escala={0.9} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* ---------- story animada ---------- */

type Pantalla = Pick<PiezaProps, 'foto' | 'posicionFoto' | 'caps' | 'script' | 'bajada' | 'sizeCaps'>;

export const StoryAnimada: React.FC<{
  pantallas: Pantalla[];
  horario?: string;
  cta?: string;
  legal?: React.ReactNode;
  framesPorPantalla?: number;
}> = ({pantallas, horario, cta, legal, framesPorPantalla = 90}) => {
  const frame = useCurrentFrame();
  const idx = Math.min(Math.floor(frame / framesPorPantalla), pantallas.length - 1);
  const local = frame - idx * framesPorPantalla;
  const p = pantallas[idx];
  const esUltima = idx === pantallas.length - 1;

  const entrada = interpolate(local, [0, 18], [0, 1], {extrapolateRight: 'clamp'});
  const subida = interpolate(local, [0, 18], [36, 0], {extrapolateRight: 'clamp'});

  return (
    <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
      <AbsoluteFill style={{opacity: interpolate(local, [0, 10], [0.4, 1], {extrapolateRight: 'clamp'})}}>
        <FotoFondo src={p.foto} posicion={p.posicionFoto} />
      </AbsoluteFill>
      <LogoBetween formato="story" />
      <AbsoluteFill
        style={{
          justifyContent: 'center',
          alignItems: 'center',
          padding: '420px 90px 340px 90px',
          opacity: entrada,
          transform: `translateY(${subida}px)`,
        }}
      >
        <BloqueTexto
          foto={p.foto}
          caps={p.caps}
          script={p.script}
          sizeCaps={p.sizeCaps}
          bajada={p.bajada}
          horario={esUltima ? horario : undefined}
          cta={esUltima ? cta : undefined}
          legal={esUltima ? legal : undefined}
        />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* ==========================================================================
 * ⭐ GRAMÁTICA MEDIDA — 26-08-2026
 *
 * Todo lo de acá abajo sale de MEDIR las 19 piezas reales que entregó Eli
 * (raw/hilton/between-adn/ref-piezas/), no de interpretar una descripción.
 * Los componentes de más arriba quedaron cortos: titulares a la mitad del
 * tamaño real, script tratada como segunda línea decorativa, bloque centrado
 * y flotando, y sin la caja taupe ni el texto en arco. Eso produjo la grilla
 * de septiembre 2026 que el cliente rechazó.
 *
 * En piezas nuevas: usar ESTOS componentes.
 * ========================================================================== */

/**
 * Caja taupe: fondo #675b49 OPACO, 74 px de alto, texto Raleway **LIGHT** 45.
 * El contraste titular pesadísimo / dato liviano es firma de la marca —
 * no poner el texto de la caja en bold.
 */
export const CajaDato: React.FC<{
  children: React.ReactNode;
  size?: number;
  /** Ancho útil del bloque; la caja nunca lo pasa. */
  anchoDisponible?: number;
  /**
   * ⭐ RONDA 9 (03-09-2026) — pedido de Eli sobre la portada del To Go:
   * «borra el fondo de este texto "Lunes a viernes · 08:00 a 10:00 hrs." ya que
   * se ocupó en el texto de promo».
   * En una pila, la caja taupe es el ÉNFASIS: si las dos líneas la llevan, no
   * hay jerarquía — es la misma lógica que «una sola línea fuerte por pila»
   * (manual §1 bis). La línea sin fondo conserva la tipografía, la caja alta y
   * la altura de la fila, para que el ritmo de la pila no se mueva; lo único
   * que cambia es que el fondo se va y entra la sombra que ya usa `Etiqueta`
   * cuando va sin caja.
   */
  sinFondo?: boolean;
  style?: React.CSSProperties;
}> = ({children, size = BETWEEN.tipos.cajaDato, anchoDisponible = 1080 - 2 * BETWEEN.bloque.margenX, sinFondo = false, style}) => {
  useFuentesListas();
  // la caja va en nowrap, así que si el dato es largo hay que bajar el cuerpo:
  // «SEGUNDO NIVEL · TRABAJAR O REUNIRTE» se salía 46 px por la derecha
  const texto = typeof children === 'string' ? children.toUpperCase() : '';
  const cuerpo = texto
    ? ajustarACaber(texto, size, (v) => `${BETWEEN.pesos.extrabold} ${v}px ${BETWEEN.fuentes.sans}`,
                    anchoDisponible - 2 * BETWEEN.cajas.padX, 0, 0.6)
    : size;
  return (
  <div
    style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      height: BETWEEN.cajas.alto,
      padding: `0 ${sinFondo ? 0 : BETWEEN.cajas.padX}px`,
      backgroundColor: sinFondo ? 'transparent' : BETWEEN.cajas.fondo,
      borderRadius: sinFondo ? 0 : BETWEEN.cajas.radio,
      // sin caja el texto queda sobre la foto: se apoya en la misma sombra que
      // usa `Etiqueta` cuando va suelta.
      textShadow: sinFondo ? '0 2px 16px rgba(36,26,18,0.75)' : 'none',
      fontFamily: BETWEEN.fuentes.sans,
      // MEDIDO en la pieza aprobada: «PARA EMPEZAR EL DÍA» da 488×33 px, que solo
      // calza con ExtraBold. Antes estaba en Light (300) y la caja se veía floja.
      fontWeight: BETWEEN.pesos.extrabold,
      fontSize: cuerpo,
      lineHeight: 1,
      color: BETWEEN.colores.beige,
      textTransform: 'uppercase',
      whiteSpace: 'nowrap',
      ...style,
    }}
  >
    {/* ⭐ Cifras tabulares también acá: es el pedido de Eli para toda la grilla,
        y lo que pasa por esta caja son los horarios («LUNES A VIERNES · 08:00 A
        10:00 HRS»). Con la compensación de bordes de `cifrasTabulares` ya no
        abren el espacio doble que tenían antes de la palabra anterior.

        ⛔ EL `<span>` NO ES DECORATIVO — no lo saques. Esta caja es `display:
        flex`, y `conCifras` devuelve un ARRAY (trozos de texto + un span por
        dígito). Sin envolver, cada trozo se vuelve un flex item y **los nodos
        que son sólo espacio no se pintan**: el horario salió
        «·08:00A10:00HRS.», sin los espacios alrededor de la «a» ni antes de
        «hrs». Lo cazó el render de `BW-F-ToGo-1`, no el typecheck.

        ⚠️ Y la caja tabular ENSANCHA la línea, mientras `ajustarACaber` calcula
        el cuerpo antes sobre el texto plano: si alguna vez sangra el margen,
        `between-qa.py` lo marca y hay que bajar el cuerpo a mano. */}
    <span>{conCifras(children, BETWEEN.pesos.extrabold)}</span>
  </div>
  );
};

/**
 * Pila de cajas taupe. Ojo: las cajas de una pila se **centran entre sí**
 * (medido: caja 1 en x 116–633 y caja 2 en x 189–561, mismo centro 375),
 * no se alinean a la izquierda del bloque.
 */
export const PilaDatos: React.FC<{
  datos: React.ReactNode[];
  /** Índices de `datos` que van SIN la caja taupe. Ver `CajaDato.sinFondo`. */
  sinFondo?: number[];
  style?: React.CSSProperties;
}> = ({datos, sinFondo = [], style}) => (
  <div
    style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: BETWEEN.cajas.gap,
      ...style,
    }}
  >
    {datos.map((d, i) => (
      <CajaDato key={i} sinFondo={sinFondo.includes(i)}>{d}</CajaDato>
    ))}
  </div>
);


/* ---------- ajuste de ancho (la script NUNCA se corta ni se parte) ---------- */

let _ctx: CanvasRenderingContext2D | null = null;
/** Ancho de tinta de un texto, midiendo con canvas (misma fuente que el DOM). */
const medirTexto = (texto: string, css: string): number => {
  if (typeof document === 'undefined') return 0;
  if (!_ctx) _ctx = document.createElement('canvas').getContext('2d');
  if (!_ctx) return 0;
  _ctx.font = css;
  return _ctx.measureText(texto).width;
};

/**
 * Baja el cuerpo hasta que el texto quepa en `maxAncho`.
 *
 * Existe porque en la ronda 4 la script se salía del cuadro en 6 piezas
 * («va contigo», «contundente», «una foto») y en Cowork-1 se partió en dos
 * líneas. En las piezas de Eli la script **jamás** se parte ni toca el borde:
 * cuando la palabra es larga, ella baja el cuerpo.
 */

/**
 * ⛔⛔ EL BUG QUE PARTIÓ LOS TITULARES — no quitar este hook.
 *
 * Todo el ajuste de cuerpo («que el titular quepa en el ancho útil») se calcula
 * midiendo el texto con canvas DURANTE el render. Si en ese momento Raleway o
 * Brushwell todavía no cargaron, `measureText` mide con la fuente de REEMPLAZO,
 * que es más angosta: el cálculo dice «cabe» y no achica nada. Después el
 * navegador pinta con la fuente real, mucho más ancha, y el titular se sale del
 * cuadro por los dos lados. Pasó en 8 de las 27 piezas.
 *
 * Este hook fuerza UN re-render cuando `document.fonts.ready` resuelve, y ahí la
 * medición ya es la buena. El `delayRender` mantiene el frame abierto para que
 * Remotion no fotografíe antes; el tope de 8 s evita que un problema de fuentes
 * cuelgue el render para siempre (ver memoria reel-video-gotchas).
 */
let _fuentesListas = false;

export const useFuentesListas = (): boolean => {
  const [listas, setListas] = React.useState(_fuentesListas);
  React.useEffect(() => {
    if (_fuentesListas || typeof document === 'undefined') return;
    const espera = delayRender('BETWEEN · esperando Brushwell y Raleway');
    let cerrado = false;
    const terminar = () => {
      if (cerrado) return;
      cerrado = true;
      _fuentesListas = true;
      setListas(true);
      continueRender(espera);
    };
    const tope = setTimeout(terminar, 8000);
    void document.fonts.ready.then(() => {
      clearTimeout(tope);
      terminar();
    }).catch(() => {
      clearTimeout(tope);
      terminar();
    });
    return () => clearTimeout(tope);
  }, []);
  return listas;
};

/**
 * ⭐ Métricas de TINTA de una línea, en px, respecto de la línea base.
 *
 * Hace falta porque Between se compone por la tinta, no por la caja de texto:
 * el aire entre la script y la caja alta que midió la pieza aprobada (9 px) es
 * de tinta a tinta. Con `lineHeight` uno nunca llega a ese número — cada familia
 * mete un espacio distinto sobre y bajo la línea base, y Brushwell además
 * tiene remates que se salen del avance.
 */
type Tinta = {
  /** Tinta por sobre la línea base. */
  alto: number;
  /** Tinta por debajo de la línea base. */
  bajo: number;
  /** Lo que el trazo se sale por la izquierda del punto de anclaje. */
  izq: number;
  /** Hasta dónde llega el trazo por la derecha del punto de anclaje. */
  der: number;
  /** Ancho de avance (lo que ocupa la caja de texto). */
  avance: number;
  /** Distancia de la línea base al borde superior de una caja con lineHeight 1. */
  baseEnCaja: number;
};

const medirTinta = (texto: string, css: string, trackingEm = 0, cuerpo?: number): Tinta => {
  const vacio: Tinta = {alto: 0, bajo: 0, izq: 0, der: 0, avance: 0, baseEnCaja: 0};
  if (typeof document === 'undefined') return vacio;
  if (!_ctx) _ctx = document.createElement('canvas').getContext('2d');
  if (!_ctx) return vacio;
  _ctx.font = css;
  // Chrome ≥ 99 aplica letterSpacing en canvas; si no existe, se compensa a mano.
  const soportaTracking = 'letterSpacing' in _ctx;
  if (soportaTracking) (_ctx as CanvasRenderingContext2D & {letterSpacing: string}).letterSpacing = `${trackingEm}em`;
  const m = _ctx.measureText(texto);
  /**
   * ⚠️ El cuerpo va explícito. `parseFloat(css)` NO sirve: cuando el css trae el
   * peso delante («800 117px Raleway») devuelve 800, y el titular se va 200 px
   * fuera del cuadro. Pasó exactamente eso en la primera calibración.
   */
  const size = cuerpo ?? parseFloat(css) ?? 0;
  const extra = soportaTracking ? 0 : trackingEm * size * Math.max(texto.length - 1, 0);
  const fbA = m.fontBoundingBoxAscent ?? m.actualBoundingBoxAscent ?? 0;
  const fbD = m.fontBoundingBoxDescent ?? m.actualBoundingBoxDescent ?? 0;
  if (soportaTracking) (_ctx as CanvasRenderingContext2D & {letterSpacing: string}).letterSpacing = '0px';
  return {
    alto: m.actualBoundingBoxAscent ?? 0,
    bajo: m.actualBoundingBoxDescent ?? 0,
    izq: Math.max(m.actualBoundingBoxLeft ?? 0, 0),
    der: m.actualBoundingBoxRight ?? 0,
    avance: (m.width ?? 0) + extra,
    // en una caja con lineHeight 1 el sobrante se reparte arriba y abajo
    baseEnCaja: (size - (fbA + fbD)) / 2 + fbA,
  };
};

const ajustarACaber = (
  texto: string,
  size: number,
  css: (s: number) => string,
  maxAncho: number,
  tracking = 0,
  minimo = 0.55,
): number => {
  const ancho = medirTexto(texto, css(size)) + tracking * Math.max(texto.length - 1, 0);
  if (!ancho || ancho <= maxAncho) return size;
  return Math.max(Math.floor((size * maxAncho) / ancho), Math.floor(size * minimo));
};

/**
 * ⭐ Titular de Between: caja alta Raleway BLACK + script Brushwell **encima**.
 *
 * Lo que hace distinto a este componente del viejo <TituloMixto>:
 *  - la script va a `proporcionScript` ≈ 1,0 × la caja alta y VA ARRIBA
 *  - las dos líneas se **solapan**: la tinta queda a 2 px (antes: gap de 22)
 *  - el bloque se alinea a la izquierda por defecto (antes: siempre centrado)
 *  - trackings medidos: −1 en la caja alta, +18 en la script
 */
/**
 * ⭐ TITULAR BETWEEN — la unidad tipográfica de la marca.
 *
 * Disposición de la pieza que la diseñadora aprobó como «uso correcto de la
 * tipografía» (C1 S3 N°1): la SCRIPT va ARRIBA, corta y en menor escala; la
 * CAJA ALTA va ABAJO y es la protagonista. Todo centrado sobre el eje.
 *
 * ⛔ Antes esto estaba al revés (caja alta arriba, script gigante abajo, las dos
 * solapadas). Eso produjo la grilla que el cliente rechazó dos veces.
 *
 * Reglas que aplica solo:
 *  · la script se limita a una frase corta — si llega larga, avisa por consola;
 *  · las dos líneas se posicionan por su TINTA, con el aire medido (9 px);
 *  · se centra por la TINTA, no por la caja, para que el remate del pincel de
 *    Brushwell no descuadre el bloque;
 *  · si no cabe en el ancho útil, baja el cuerpo en vez de partir la línea.
 */
export const TitularBetween: React.FC<{
  /** Frase corta o palabra clave. Va ARRIBA y en menor escala que el titular. */
  script?: string;
  /**
   * ⭐ La línea de acompañamiento en RALEWAY en vez de Brushwell.
   *
   * Pedido de Eli el 01-09-2026 para el carrusel Cowork: «desde el slide 2 no
   * agregues la tipografía brushwell, que sea de la familia de raleway, así se
   * diferencia de la portada». La script queda como marca de la PORTADA y las
   * slides interiores bajan a un solo alfabeto.
   *
   * No es una proporción inventada: usa la misma relación que ya tiene la línea
   * `arriba` de `TituloTresPesos` —Raleway 500 a 0,72 × la caja alta, tracking
   * +0,02em y caja alta—, que es el recurso de dos pesos de la marca.
   */
  scriptSans?: boolean;
  /** Titular protagonista, en caja alta. Va ABAJO. */
  caps?: string;
  sizeCaps?: number;
  sizeScript?: number;
  /**
   * ⭐ Aire de TINTA entre la script y la primera línea de caja alta.
   *
   * Por defecto `BETWEEN.aire.scriptATitulo` (9), que es el valor MEDIDO — pero
   * medido sobre una script SIN DESCENDENTES. Cuando la frase trae «p», «y» o
   * «j», sus colas bajan dentro de esos 9 px y el titular queda pegado: en la
   * portada del Cowork, «Tu oficina por hoy» dejaba **12 px** contra las
   * **29,8 px** que separan las dos líneas del propio titular. O sea que el
   * salto ENTRE niveles era menor que el salto DENTRO de un nivel, que es la
   * jerarquía al revés.
   *
   * Es opt-in por la misma razón que `anchoDisponible`: subir el token movería
   * las piezas ya aprobadas. Se pasa a mano en la pieza que lo necesita.
   */
  aireScriptATitulo?: number;
  /**
   * ⭐ Tracking de la caja alta, en `em`. Por defecto `BETWEEN.trackingCaps`
   * (−0,024), que es el valor MEDIDO sobre la pieza de referencia: con él
   * «PERFECTO» da 568 px a 117.
   *
   * Es opt-in por la misma razón que `anchoDisponible` y `aireScriptATitulo`:
   * el token está calibrado y moverlo re-flujaría toda pieza ya aprobada. Se
   * pasa a mano cuando la LÍNEA CONCRETA lo pide, y eso pasa cuando es larga:
   * un −0,024em sobre 8 letras casi no se nota, pero sobre 14 —«¡TE
   * ESPERAMOS!»— acumula ~36 px de cierre y las letras se leen apretadas.
   * Eli lo marcó en la ST 2 de la S3: «no tienen kernig optimo».
   *
   * ⚠️ Aflojar el tracking ENSANCHA la línea, así que `encoger` va a bajar el
   * cuerpo para que siga cabiendo en `anchoDisponible`. Es el intercambio
   * correcto —una letra menos grande pero bien espaciada se lee mejor que una
   * grande y comprimida— pero hay que mirar el resultado, no suponerlo.
   */
  trackingCapsEm?: number;
  /**
   * ⭐ PESO de la caja alta del titular, y del acompañamiento cuando va en
   * Raleway (`scriptSans`). Por defecto ExtraBold (800), que es el valor MEDIDO
   * en la pieza de referencia y con el que están calibrados el tracking y los
   * anchos de cifra — así que es OPT-IN por la misma razón que `anchoDisponible`
   * y `trackingCapsEm`: cambiar el defecto re-flujaría toda pieza ya aprobada.
   *
   * Se pasa a mano cuando la diseñadora lo pide para una pieza. Eli, 09-09-2026,
   * sobre la ST del 22-09: «los títulos que sean en raleway semi bold».
   *
   * ⚠️ Un peso más liviano es más ANGOSTO, así que `ajustarACaber` va a permitir
   * un cuerpo mayor dentro del mismo `anchoDisponible`. Es lo correcto —la línea
   * ocupa la columna igual— pero hay que MIRAR el render, no suponerlo.
   */
  pesoCaps?: number;
  /**
   * ⭐⭐ ¿El titular va en CAJA ALTA? Por defecto sí, que es la gramática de la
   * marca y lo que tienen todas las piezas aprobadas — así que es OPT-IN, igual
   * que `anchoDisponible`, `trackingCapsEm` y `pesoCaps`.
   *
   * Eli lo pidió por primera vez el 21-09-2026, sobre la ST del 30-09: «que este
   * texto sea en solo la primera mayúscula, la demás no, y en raleway pero no
   * tan gruesa, **ya que hay muchos similares en historias**». O sea que el
   * motivo no es estético sino de repertorio: script + caja alta pesada es la
   * fórmula que se repite en TODAS sus stories, y una pieza que quiere
   * distinguirse tiene que salirse de ella.
   *
   * ⚠️ En `false` el texto se pinta TAL CUAL se escribe: la pieza manda la caja,
   * no el componente. Si la frase sigue a la línea de arriba, va en minúscula.
   *
   * ⚠️ Y el tracking pasa a 0. El −0,024em de `BETWEEN.trackingCaps` está
   * calibrado sobre VERSALES —donde aprieta letras de ancho parejo—; sobre caja
   * baja, con astas y colas, ese mismo valor junta las letras y se lee apretado.
   */
  cajaAlta?: boolean;
  tono?: Tono;
  alinear?: 'centro' | 'izquierda';
  /**
   * Ancho de composición.
   *
   * ⚠️ Por defecto sigue siendo el MARGEN (1080 − 2×84 = 912). Lo correcto es
   * componer en `BETWEEN.bloque.columna` (810) —achicar sólo hasta caber en el
   * margen deja toda línea larga clavada en el 84 % del lienzo— pero cambiar el
   * defecto re-flujaba piezas YA APROBADAS: comprobado el 01-09-2026, tres de
   * las cuatro piezas entregadas de la S1 cambiaban entre un 4,5 % y un 5,3 %
   * de sus píxeles. Así que la columna es OPT-IN: se pasa a mano en la pieza
   * que se está cortando. Ver `clients/hilton/CLAUDE.md § LA COLUMNA`.
   */
  anchoDisponible?: number;
  /**
   * Conserva la puntuación final del texto tal como la escribe el brief.
   *
   * Por defecto la pieza pasa por `sinPuntoFinal`, porque la regla de Eli es que
   * «los títulos NUNCA llevan punto final». Pero cuando el texto es una CITA
   * —el carrusel «Primero la foto… ¿o no?» o el chiste del cafecito— el punto
   * va DENTRO de las comillas y es parte de lo que se dice, no un punto de
   * titular. Scarlette pidió expresamente las comillas el 31-08-2026, y el
   * brief trae la puntuación completa, así que ahí se respeta literal.
   */
  mantenerPunto?: boolean;
  /**
   * ⭐⭐ EL CONTORNO TIPO STICKER — grosor en px, 0 o sin pasar = apagado.
   *
   * Es el recurso de la `REF 1` del concurso: ahí el titular no va en una caja
   * rectangular sino con un **contorno claro pegado a las letras**, que es lo
   * que lo despega del fondo y lo hace leer como una calcomanía. Eli lo pidió
   * para la portada del concurso el 21-09-2026: «que se busca CEO del café esté
   * en un marco beige […] que sea como el sticker, igual que la referencia».
   *
   * No es una sombra de caída ni un borde: es un HALO, y se pinta con 24 copias
   * del texto desplazadas en círculo a `grosor/2` de radio (`haloSticker`).
   *
   * ⛔ El camino obvio —`-webkit-text-stroke` con `paint-order: stroke fill`—
   * se probó y se descartó MIRANDO el render ampliado: Chrome aplica el orden
   * de pintado **glifo a glifo**, así que el contorno de cada letra pasa por
   * encima del relleno de la anterior y la palabra queda cruzada por trazos
   * claros. Con el tracking negativo del titular de Between (−0,024em) las
   * letras están lo bastante juntas como para que se note en toda la línea.
   * `text-shadow`, en cambio, se pinta ENTERO detrás del texto del elemento, así
   * que el halo queda continuo alrededor de la palabra — que es exactamente lo
   * que hace el sticker de la referencia.
   *
   * ⚠️ La tinta crece `grosor/2` por lado, y `medirTinta` mide SIN el halo: en
   * la pieza hay que descontarlo al calcular colisiones, márgenes Y el aire
   * entre la script y la caja alta (si no, los dos halos se tocan).
   *
   * Es OPT-IN, por la misma razón que `cajaAlta` y `pesoCaps`: ninguna pieza ya
   * aprobada lo lleva y encenderlo por defecto las re-flujaría a todas.
   */
  contorno?: number;
  /** Color del contorno. Por defecto el beige de la marca. */
  contornoColor?: string;
  style?: React.CSSProperties;
}> = ({
  script,
  scriptSans = false,
  caps,
  sizeCaps = BETWEEN.tipos.tituloCaps,
  sizeScript,
  aireScriptATitulo,
  trackingCapsEm,
  pesoCaps,
  cajaAlta = true,
  contorno = 0,
  contornoColor = BETWEEN.colores.beige,
  tono = 'beige',
  alinear = 'centro',
  anchoDisponible = 1080 - 2 * BETWEEN.bloque.margenX,
  mantenerPunto = false,
  style,
}) => {
  // sin esto se mide con la fuente de reemplazo y el titular no se achica
  useFuentesListas();
  const podar = (t: string) => (mantenerPunto ? t : sinPuntoFinal(t));
  const textoCaps = caps ? podar(caps) : '';
  /**
   * ⚠️ En modo Raleway la línea se pinta en CAJA ALTA, así que se pasa a
   * mayúscula ACÁ y no con `textTransform`. El cuerpo se calcula midiendo con
   * canvas, y canvas mide el string tal cual: medir «muchos pendientes» y
   * pintar «MUCHOS PENDIENTES» da ~20 % de diferencia y el titular se sale del
   * cuadro. Es el bug que partió 8 piezas de la ronda 4.
   */
  /* ⚠️ `scriptSans` sube la línea a caja alta porque su registro es «caja alta
     liviana». Con `cajaAlta={false}` el titular entero va en caja baja, así que
     el acompañamiento la sigue: si no, quedaría «¿EL ALMUERZO / se quedó en
     casa?», que es la contradicción que la pieza está tratando de evitar. */
  const textoScript = script
    ? (scriptSans && cajaAlta ? podar(script).toUpperCase() : podar(script))
    : '';

  if (!scriptSans && textoScript && textoScript.split(/\s+/).length > 4) {
    // eslint-disable-next-line no-console
    console.warn(`[BETWEEN] «${textoScript}» es muy largo para la script. ` +
      `Brushwell es para una frase corta o una palabra clave, no para una bajada.`);
  }

  const trScript = scriptSans ? 0.02 : BETWEEN.trackingScript;
  const trCaps = trackingCapsEm ?? (cajaAlta ? BETWEEN.trackingCaps : 0);
  const wCaps = pesoCaps ?? BETWEEN.pesos.extrabold;
  // el acompañamiento en Raleway sigue al titular: si el titular baja de peso,
  // baja con él (Medium 500 cuando el titular está en el ExtraBold de siempre).
  const wScript = pesoCaps ?? 500;
  const cssCaps = (n: number) => `${wCaps} ${n}px ${BETWEEN.fuentes.sans}`;
  const cssScript = (n: number) => scriptSans
    ? `${wScript} ${n}px ${BETWEEN.fuentes.sans}`
    : `${n}px ${BETWEEN.fuentes.script}`;

  const encoger = (texto: string, base: number, css: (n: number) => string, tr: number) => {
    if (!texto) return base;
    let n = base;
    for (let i = 0; i < 40; i++) {
      const t = medirTinta(texto, css(n), tr, n);
      const ancho = Math.max(t.avance, t.izq + t.der);
      if (!ancho || ancho <= anchoDisponible) break;
      n -= 2;
    }
    return n;
  };

  /**
   * La caja alta puede ir en dos líneas: se separan con «\n».
   * ⚠️ Se pasan YA EN MAYÚSCULA. El CSS las sube con `textTransform`, pero el
   * cálculo del cuerpo se hace con canvas, y canvas mide el string tal cual: si
   * se mide «rico y contundente» y se pinta «RICO Y CONTUNDENTE», la medición
   * sale ~20 % corta, el ajuste cree que cabe y el titular se sale del cuadro.
   * Ese fue el defecto de 8 piezas de la ronda anterior.
   */
  const lineasCaps = textoCaps
    ? textoCaps.split('\n')
        .map((l) => (cajaAlta ? l.trim().toUpperCase() : l.trim()))
        .filter(Boolean)
    : [];
  const nCaps = lineasCaps.reduce(
    (menor, l) => Math.min(menor, encoger(l, sizeCaps, cssCaps, trCaps)),
    sizeCaps,
  );
  const nScript = encoger(
    textoScript,
    sizeScript ?? Math.round(sizeCaps * (scriptSans ? 0.72 : BETWEEN.proporcionScript)),
    cssScript,
    trScript,
  );

  const tCapsPorLinea = lineasCaps.map((l) => medirTinta(l, cssCaps(nCaps), trCaps, nCaps));
  const tCaps = tCapsPorLinea[0] ?? medirTinta('', cssCaps(nCaps), trCaps, nCaps);
  /**
   * Aire entre dos líneas de caja alta. MEDIDO en «¿YA TOMASTE TU / CAFECITO DEL
   * DÍA?» (post n°2 s4): 21 px de tinta a tinta sobre una altura de caja de 59,
   * o sea 0,35 de la altura. Se guarda como proporción para que aguante
   * cualquier cuerpo.
   */
  const aireEntreCaps = Math.round((tCaps.alto || nCaps * 0.73) * 0.35);
  const tScript = medirTinta(textoScript, cssScript(nScript), trScript, nScript);

  /** Cuánto mover la caja para que quede centrada la TINTA y no el avance. */
  const centrarTinta = (t: Tinta) =>
    alinear === 'centro' ? t.avance / 2 - (t.der - t.izq) / 2 : t.izq;

  const aire = aireScriptATitulo ?? BETWEEN.aire.scriptATitulo;
  const altoScript = textoScript ? tScript.alto + tScript.bajo : 0;
  const altoCaps = tCapsPorLinea.reduce(
    (acc, t, i) => acc + t.alto + t.bajo + (i ? aireEntreCaps : 0), 0,
  );
  const alto = altoScript + (textoScript && lineasCaps.length ? aire : 0) + altoCaps;

  const linea = (
    texto: React.ReactNode,
    t: Tinta,
    n: number,
    topTinta: number,
    extra: React.CSSProperties,
  ) => (
    <div
      style={{
        position: 'absolute',
        top: topTinta - (t.baseEnCaja - t.alto),
        left: alinear === 'centro' ? '50%' : 0,
        transform: alinear === 'centro'
          ? `translateX(calc(-50% + ${centrarTinta(t)}px))`
          : `translateX(${centrarTinta(t)}px)`,
        fontSize: n,
        lineHeight: 1,
        whiteSpace: 'nowrap',
        color: tinta(tono),
        /* ⭐ RONDA 8: la sombra existe para que el BEIGE se lea sobre una foto.
           En `cafe` el titular es tinta oscura sobre fondo claro —la ST de la
           vitrina— y ahí la sombra no aporta contraste: sólo ensucia el contorno
           y engorda la letra. Se apaga. */
        textShadow: tono === 'cafe' ? undefined : sombraSobreFoto,
        ...(contorno ? {textShadow: haloSticker(contorno / 2, contornoColor)} : null),
        ...extra,
      }}
    >
      {texto}
    </div>
  );

  return (
    <div style={{position: 'relative', width: '100%', height: alto, ...style}}>
      {textoScript
        ? linea(
            /* el volteo del signo de apertura es un truco para Brushwell, que no
               trae «¿». Raleway sí lo trae, así que en Raleway no se toca. */
            scriptSans ? textoScript : signosVolteados(textoScript),
            tScript, nScript, 0,
            scriptSans
              ? {fontFamily: BETWEEN.fuentes.sans, fontWeight: wScript, letterSpacing: '0.02em'}
              : {fontFamily: BETWEEN.fuentes.script, letterSpacing: `${BETWEEN.trackingScript}em`},
          )
        : null}
      {lineasCaps.map((l, i) => {
        const arriba = altoScript
          + (textoScript ? aire : 0)
          + tCapsPorLinea.slice(0, i).reduce((a, t) => a + t.alto + t.bajo + aireEntreCaps, 0);
        return (
          <React.Fragment key={i}>
            {linea(l, tCapsPorLinea[i], nCaps, arriba, {
              fontFamily: BETWEEN.fuentes.sans,
              fontWeight: wCaps,
              letterSpacing: `${trCaps}em`,
              textTransform: cajaAlta ? 'uppercase' : 'none',
            })}
          </React.Fragment>
        );
      })}
    </div>
  );
};

export const TextoArco: React.FC<{
  children: string;
  size?: number;
  tono?: Tono;
  /** Desplazamiento vertical respecto a la curva medida. */
  offsetY?: number;
  ancho?: number;
  alto?: number;
}> = ({children, size = BETWEEN.tipos.arco, tono = 'beige', offsetY = 0, ancho = 1080, alto = 1350}) => {
  const texto = children.toUpperCase();
  // largo aproximado de la bézier M 108 1097 Q 540 1367 972 1097
  const largoTrazado = 940;
  const cuerpo = ajustarACaber(
    texto,
    size,
    (s) => `${BETWEEN.pesos.regular} ${s}px ${BETWEEN.fuentes.sans}`,
    largoTrazado,
  );
  return (
  <svg
    width={ancho}
    height={alto}
    viewBox={`0 0 ${ancho} ${alto}`}
    style={{position: 'absolute', left: 0, top: offsetY}}
  >
    <path id="arco-between" d="M 108 1097 Q 540 1367 972 1097" fill="none" />
    <text
      fill={tinta(tono)}
      style={{
        fontFamily: BETWEEN.fuentes.sans,
        fontWeight: BETWEEN.pesos.regular,
        fontSize: cuerpo,
        letterSpacing: 0,
      }}
    >
      <textPath href="#arco-between" startOffset="50%" textAnchor="middle">
        {texto}
      </textPath>
    </text>
  </svg>
  );
};

/**
 * ⭐ Plantilla de feed real de Between: bodegón + titular anclado ARRIBA a la
 * izquierda + pila de cajas taupe + texto en arco al pie.
 * Geometría medida en «EL MATCH perfecto» (C1 S2 N°1).
 */
/**
 * ⭐ PIE DE PIEZA — el bloque de cierre de la pieza aprobada.
 *
 * Medido en C1 S3 N°1 (feed, sobre lienzo de 1080×1350):
 *   «PROMOS TO GO»          y 1150–1185 · tinta 413 × 35 · centrado
 *   «De 8:00 a 10:00 hrs»   y 1211–1237 · tinta 317 × 25 · centrado
 * Es lo que da el cierre comercial sin ensuciar el titular: la promo y el
 * horario NO van arriba peleando con la caja alta.
 */
/**
 * ⭐ PANEL TAUPE — la bajada cuando la foto no deja leerla.
 *
 * Instrucción textual del cliente (27-08-2026):
 *   «Cuando no se logra visualizar los textos, puedes dejarlo en una caja del
 *    color café de la marca #675B49.»
 *
 * Es la misma caja de `CajaDato` pero para una frase de varias líneas. Se usa
 * SOLO cuando hace falta: sobre foto oscura y pareja, la bajada va suelta. La
 * alternativa —subir el multiply hasta que el texto se lea— es justamente lo
 * que dejaba las piezas apagadas.
 */
export const PanelTaupe: React.FC<{
  children: React.ReactNode;
  size?: number;
  /**
   * Ancho máximo del panel. Por defecto el MARGEN, por la misma razón que
   * `TitularBetween.anchoDisponible`: cambiar el defecto movía piezas ya
   * aprobadas. Con el margen, la caja de la slide 3 del Cowork salía de 912 px
   * —tocando los dos bordes del bloque— y su texto se partía en TRES líneas,
   * con «segundo nivel,» como renglón corto entre dos largos; por eso las
   * piezas que se cortan hoy pasan `ancho` a mano.
   */
  ancho?: number;
  /** Interlínea. Por defecto 1,3; se aprieta cuando el texto va en dos líneas. */
  interlinea?: number;
  style?: React.CSSProperties;
}> = ({children, size = BETWEEN.tipos.bajada, ancho, interlinea, style}) => (
  <div
    style={{
      maxWidth: ancho ?? 1080 - 2 * BETWEEN.bloque.margenX,
      padding: `${Math.round(BETWEEN.cajas.alto * 0.28)}px ${BETWEEN.cajas.padX}px`,
      backgroundColor: BETWEEN.cajas.fondo,
      borderRadius: BETWEEN.cajas.radio,
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.semibold,
      fontSize: size,
      lineHeight: interlinea ?? 1.3,
      color: BETWEEN.colores.beige,
      textAlign: 'center',
      ...style,
    }}
  >
    {children}
  </div>
);

export const PieDePieza: React.FC<{
  formato: 'feed' | 'story';
  titulo?: string;
  detalle?: string;
}> = ({formato, titulo, detalle}) => {
  // MEDIDO: en feed la tinta del pie arranca en y = 1150; en la story el cierre
  // de Eli arranca en y = 1678, bien por sobre la zona segura de Meta (340 px).
  const arriba = formato === 'feed' ? 1150 : 1678;
  return (
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        right: BETWEEN.bloque.margenX,
        top: arriba,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: 26,
      }}
    >
      {titulo ? (
        <div
          style={{
            fontFamily: BETWEEN.fuentes.sans,
            fontWeight: BETWEEN.pesos.extrabold,
            fontSize: 48,
            letterSpacing: `${BETWEEN.trackingCaps}em`,
            lineHeight: 1,
            textTransform: 'uppercase',
            color: BETWEEN.colores.beige,
            textShadow: sombraSobreFoto,
            textAlign: 'center',
          }}
        >
          {titulo}
        </div>
      ) : null}
      {detalle ? (
        <div
          style={{
            fontFamily: BETWEEN.fuentes.sans,
            fontWeight: BETWEEN.pesos.semibold,
            fontSize: 35,
            lineHeight: 1.2,
            color: BETWEEN.colores.beige,
            textShadow: sombraSobreFoto,
            textAlign: 'center',
          }}
        >
          {/* acá cae el horario de la portada To Go («Lunes a viernes · 08:00 a
              10:00 hrs.»): dos «1» y cuatro «0» que sin caja tabular bailan */}
          {detalle}
        </div>
      ) : null}
    </div>
  );
};

/**
 * Legal al pie, en cursiva. Medido: feed 224 × 11 px a 32 px del borde;
 * story 248 × 27 px, por sobre la zona segura de Meta.
 */
export const LegalAlPie: React.FC<{
  formato: 'feed' | 'story';
  children: React.ReactNode;
}> = ({formato, children}) => (
  <div
    style={{
      position: 'absolute',
      left: 0,
      right: 0,
      bottom: formato === 'feed' ? 22 : 360,
      textAlign: 'center',
      fontFamily: BETWEEN.fuentes.sans,
      fontStyle: 'italic',
      fontWeight: BETWEEN.pesos.regular,
      fontSize: formato === 'feed' ? 20 : 28,
      lineHeight: 1,
      color: BETWEEN.colores.beige,
      opacity: 0.9,
      textShadow: sombraSobreFoto,
    }}
  >
    {children}
  </div>
);

/**
 * ⭐⭐ LA DIRECCIÓN AL PIE — pedido de Scarlette el 22-09-2026 sobre la portada
 * del carrusel PROMOS TO GO: «le puedes sumar la dirección a esta portada».
 *
 * ⛔ No se inventó: está **CALCADA de la lámina de Eli** `C1 S2 CUMPLE N1.png`
 * (`raw/hilton/between/de-eli/cumple-s2-v2/`), que es el único antecedente de
 * dirección puesta sobre una pieza de FEED y salió de la misma petición del
 * cliente («aprovechemos de poner la dirección en G1 abajo», 08-09). Medido
 * sobre ese archivo, a 2250 px de ancho:
 *
 *   · tinta de `AV. Vitacura 2727, Las Condes`  →  x 684–1562 (**ancho 879**)
 *   · **altura de versal 43 px** → cuerpo 29 px en la mesa de 1080
 *   · centrada sobre el eje (centro de tinta 1123, y el lienzo en 1125: la
 *     diferencia es el espacio de tracking que cuelga tras la última letra)
 *   · línea de base a **79 px** del canto inferior; el descendente de la coma
 *     llega a 74
 *   · tinta `#fff9eb` a plena opacidad (medido 253/247/233 sobre madera oscura)
 *
 * ⭐ **El peso salió del TRAZO, no del ojo.** Con el cuerpo ya calzado en 43 px
 * de versal, se midió el ancho de asta en la fila media de la línea y el área
 * de tinta de los dos renders contra el de ella:
 *
 *   | peso | asta (mediana / media) | tinta |
 *   |---|---|---|
 *   | Eli  | 5 / 5,42 | 8.727 |
 *   | 400  | 4 / 4,3  | 7.476 ⛔ flaca |
 *   | **500** | **6 / 5,94** | **9.484** ✅ |
 *   | 600  | 7 / 7,45 | 11.075 ⛔ gorda (35 % más tinta que la de ella) |
 *
 * El semibold que usa el resto del sistema estaba **muy** lejos. Queda Medium,
 * que es el más cercano de los pesos reales de la familia; el sobrante de 8 %
 * es rasterización (Illustrator engorda menos las astas que Chrome).
 * El tracking sale de la misma medición: **0,024 em** deja la línea en 877 px
 * contra los 879 de ella.
 *
 * ⚠️ Va SUELTA al pie, no colgando del bloque: en la lámina de Eli la banda de
 * texto anterior termina 744 px más arriba. Es un pie de página, no una línea
 * más de la pila.
 *
 * ⚠️ La cadena lleva «AV.» en versales y el resto en caja alta y baja, tal como
 * ella la escribió — no es `text-transform`, es el texto.
 */
export const DireccionAlPie: React.FC<{
  formato: 'feed' | 'story';
  children?: React.ReactNode;
}> = ({formato, children}) => (
  <div
    style={{
      position: 'absolute',
      left: 0,
      right: 0,
      /* `bottom` está ajustado CONTRA EL RENDER para que la base caiga a 38 px
         del canto, que es donde la puso Eli. En story se respeta además la zona
         segura de Meta (340 px), como hace `LegalAlPie`. */
      bottom: formato === 'feed' ? 33 : 360,
      textAlign: 'center',
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.medium,
      fontSize: formato === 'feed' ? 29 : 30,
      lineHeight: 1,
      letterSpacing: '0.024em',
      color: BETWEEN.colores.beige,
      textShadow: sombraSobreFoto,
    }}
  >
    {children ?? BETWEEN.datos.direccionPieza}
  </div>
);

export const PiezaFeedBodegon: React.FC<{
  foto: string;
  posicionFoto?: string;
  oscurecer?: number;
  caps?: string;
  script?: string;
  /** La línea de acompañamiento en Raleway en vez de Brushwell. */
  scriptSans?: boolean;
  /** Conserva la puntuación del brief; para textos que son una CITA. */
  mantenerPunto?: boolean;
  sizeCaps?: number;
  /**
   * Cuerpo de la script, cuando la proporción por defecto (1,05 × el titular)
   * la deja MÁS ANCHA que el titular al que acompaña. Ver `TitularBetween`.
   */
  sizeScript?: number;
  /** Aire de tinta script → titular. Ver `TitularBetween.aireScriptATitulo`. */
  aireScriptATitulo?: number;
  /** Bajada bajo el titular. Va antes de las cajas taupe. */
  bajada?: React.ReactNode;
  /** Interlínea de la caja de bajada, para apretar un texto de dos líneas. */
  interlineaBajada?: number;
  /** Cuerpo de la bajada, cuando la jerarquía de la pieza pide otro. */
  sizeBajada?: number;
  /**
   * Ancho máximo de la bajada. El defecto de `Bajada` son 820 px, y al subir el
   * cuerpo un texto que antes entraba en una línea se parte en dos. Se abre sólo
   * lo necesario — nunca más allá del margen (912).
   */
  anchoBajada?: number;
  /**
   * Ancho de la columna del TITULAR. Por defecto el margen (912), para no
   * mover lo ya aprobado; las piezas que se cortan hoy pasan
   * `columna={BETWEEN.bloque.columna}` (810) a mano.
   */
  columna?: number;
  /**
   * Ancho de la caja taupe. Por defecto el mismo que el titular; se aprieta
   * para que el bloque ESCALONE (titular ancho → caja angosta) en vez de
   * apilar dos bandas del mismo ancho, que es lo que se leía como un muro.
   */
  columnaCaja?: number;
  /** Aire entre el titular y la caja taupe. Por defecto el medido (18). */
  aireTituloACaja?: number;
  /**
   * ⭐ EL VELO — pedido de Eli el 01-09-2026: «una transparencia con opacidad
   * como en Adobe Illustrator, que sea multiplicada muy sutil, para que se vea
   * el logo y los textos de arriba. Muy sutil».
   *
   * Es exactamente eso: un rectángulo del color sombra de la marca a pantalla
   * completa, en modo `multiply`, con opacidad baja. Va SOBRE la foto y su
   * multiply propio, y DEBAJO del logo y del texto — como una capa de
   * Illustrator puesta encima de la imagen y debajo de la tipografía.
   *
   * ⚠️ No es lo mismo que subir `oscurecer`. Ese apaga la foto entera para
   * ganar contraste, y el manual lo prohíbe («cuando un texto no se lee, la
   * solución es la caja taupe, no oscurecer la foto»). El velo es una capa
   * aparte, deliberada y muy baja, que asienta el conjunto sin matar la foto.
   * Si hace falta subirlo por encima de ~0,18 el problema es el encuadre.
   */
  velo?: number;
  /**
   * ⭐⭐ DEGRADADO AL PIE — autorizado por Eli el 14-09-2026, sobre la portada
   * del carrusel To Go: «Quiero los textos de la portada como estaban antes, se
   * va a ver bien. Si necesitas algo puedes añadir una transparencia en opacidad
   * o degradado».
   *
   * Es una rampa del color sombra de la marca, opaca abajo y transparente hacia
   * arriba. NO es `oscurecer` —que apaga la foto entera y el manual prohíbe para
   * ganar legibilidad— ni `velo` —que es plano y va a pantalla completa—: acá el
   * cielo de la foto queda intacto y sólo se asienta el pie, que es donde cae el
   * bloque de texto.
   *
   * El número es la opacidad en el BORDE INFERIOR. La rampa arranca a media
   * altura y sube con una parada intermedia, para que no se vea el canto del
   * degradado. Se elige MIDIENDO el contraste de la tinta beige sobre la franja
   * del bloque, no a ojo.
   */
  degradadoPie?: number;
  /** La bajada va DENTRO de una caja taupe, para cuando la foto no la deja leer. */
  bajadaEnCaja?: boolean;
  /**
   * ⭐⭐ EL TITULAR va dentro de la caja taupe. Añadido el 14-09-2026 para la
   * portada del carrusel To Go (FEED col L, 22-sep).
   *
   * Es la regla del manual —«cuando un texto no se lee, la solución es la caja
   * taupe, no oscurecer la foto»— aplicada al TITULAR y no sólo a la bajada.
   * La ocasión: la portada pasó a una FOTOGRAFÍA REAL de la entrada del local
   * (sesión de Sebastián, 09-09) y ahí el tercio inferior son pantalones color
   * crema. MEDIDO sobre las 18 tomas del bloque y en tres posiciones distintas
   * del bloque: la tinta beige da entre 1,16 y 1,48:1 y la marca pide 3:1 para
   * el titular. No hay encuadre que lo arregle —ninguna de las 18 llega— y el
   * velo tendría que subir a ~0,56, muy por encima del tope de 0,18 que fija el
   * propio manual («si hace falta subirlo por encima de ~0,18 el problema es el
   * encuadre»). La caja resuelve con 6,31:1 y NO depende de la foto.
   *
   * ⚠️ El texto de adentro se compone sobre `columna − 2 × cajas.padX`: así la
   * CAJA mide la columna y el titular no se come el margen.
   *
   * ⛔ Y va TODO el bloque adentro, no sólo el titular. Primer intento: la caja
   *    envolvía sólo al titular y «PROMOS TO GO» + el horario quedaban fuera,
   *    en beige sobre los mismos pantalones crema — o sea el problema se mudaba
   *    dos líneas más abajo. Meter cada línea en su propia caja tampoco: tres
   *    bandas taupe apiladas son el «muro» que el manual prohíbe. Una sola caja
   *    para el bloque resuelve el contraste de todo y se lee como un bloque.
   *    Por eso `PilaDatos` va aquí SIEMPRE sin fondo: la caja ya es el énfasis.
   */
  bloqueEnCaja?: boolean;
  datos?: React.ReactNode[];
  /**
   * Índices de `datos` que van SIN la caja taupe. Ver `CajaDato.sinFondo`:
   * en una pila, la caja es el énfasis y repetirla en las dos líneas lo mata.
   */
  datosSinFondo?: number[];
  arco?: string;
  /** Bloque al pie: nombre de la promo + horario, como en la pieza aprobada. */
  pie?: {titulo?: string; detalle?: string};
  /** Legal en cursiva, al ras del borde inferior. */
  legal?: string;
  /**
   * La dirección del local al pie. `true` usa la cadena de marca; un string la
   * reemplaza. Ver `DireccionAlPie` — está calcada de la lámina de Eli.
   */
  direccion?: boolean | string;
  conLogo?: boolean;
  logoTono?: Tono;
  logoPosicion?: 'arriba' | 'abajo';
  /** Halo bajo el logo. Ver `LogoBetween.sombra`. */
  logoSombra?: number;
  alinear?: 'izquierda' | 'centro';
  /**
   * Dónde va el bloque. Por defecto ARRIBA (es lo que hace Eli en los bodegones),
   * pero en las fotos con personas se baja para no pasar texto sobre caras ni
   * ojos — regla dura de ella.
   */
  anclaje?: 'arriba' | 'abajo';
  /**
   * Y exacta del bloque, cuando ni arriba ni abajo sirven. Se usa sobre todo en
   * fotos con personas: bajar el bloque «casi al centro» deja el texto sobre una
   * superficie limpia en vez de sobre la cara. Lo pidió la diseñadora el 28-08.
   */
  topBloque?: number;
  /** Capas encima de la foto: etiquetas con flecha, doodles, mockups. */
  children?: React.ReactNode;
}> = ({
  foto,
  posicionFoto,
  // el bodegón real casi no se oscurece: la foto ya viene con fondo oscuro
  oscurecer = 0.1,
  caps,
  script,
  scriptSans,
  mantenerPunto,
  sizeCaps,
  sizeScript,
  aireScriptATitulo,
  bajada,
  bajadaEnCaja,
  interlineaBajada,
  sizeBajada,
  anchoBajada,
  columna = 1080 - 2 * BETWEEN.bloque.margenX,
  columnaCaja,
  aireTituloACaja = BETWEEN.aire.tituloACaja,
  velo,
  datos,
  datosSinFondo,
  bloqueEnCaja,
  degradadoPie,
  arco,
  pie,
  legal,
  direccion,
  // en el feed de bodegón la marca la pone el vaso, no un logo sobrepuesto
  conLogo = false,
  logoTono = 'beige',
  logoPosicion = 'abajo',
  logoSombra,
  // MEDIDO: las dos piezas aprobadas están centradas sobre el eje. Between
  // compone centrado; el bloque a la izquierda no es su gramática.
  alinear = 'centro',
  anclaje = 'arriba',
  topBloque,
  children,
}) => {
  // Eli entrega DOS plantillas por formato (logo arriba / logo abajo) justo para
  // esto: si el bloque de texto baja, el logo sube. Si no, se pisan — pasó en 5
  // piezas de la ronda 4.
  const posLogo = anclaje === 'abajo' ? 'arriba' : logoPosicion;
  return (
  /* ⭐ `CIFRAS_ALTAS` va en la RAÍZ y se hereda: así también le llega a los
     dígitos que NO pasan por una caja de dato — el «3» de «¡LLÉVATE LOS 3!» del
     titular es uno. `font-variant-numeric` es heredable, y sólo toca cifras. */
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra, ...CIFRAS_ALTAS}}>
    <FotoFondo src={foto} posicion={posicionFoto} oscurecer={oscurecer} />
    {/* el velo va sobre la foto y DEBAJO del logo y del texto */}
    {velo ? (
      <AbsoluteFill style={{
        backgroundColor: BETWEEN.colores.sombra,
        opacity: velo,
        mixBlendMode: 'multiply',
      }} />
    ) : null}
    {degradadoPie ? (
      <AbsoluteFill style={{
        /* ⭐ La rampa NO es lineal, y por eso son cuatro paradas. Con un
           degradado lineal la opacidad sube demasiado lento justo donde arranca
           el bloque: medido sobre la portada To Go, la script quedaba en 2,19:1
           con la tinta beige (la marca pide 3:1) porque a esa altura el lineal
           sólo había llegado al 24 % de su opacidad. Estas paradas la llevan al
           59 % a media altura del bloque y dejan el tercio superior de la foto
           SIN TOCAR, que es la diferencia con `oscurecer`. */
        background:
          `linear-gradient(to top,` +
          /* ⭐ RONDA 25 — Eli: «bájale solo un poco al degradado abajo… muy
             sutil». Se afloja SÓLO el borde inferior (de opaco a 0,88) y las
             paradas de en medio quedan igual: así el pie deja de leerse como
             una banda maciza y el contraste donde cae el bloque no se mueve. */
          ` ${BETWEEN.colores.sombra}e0 0%,` +
          ` ${BETWEEN.colores.sombra}d1 35%,` +
          ` ${BETWEEN.colores.sombra}59 60%,` +
          ` ${BETWEEN.colores.sombra}00 82%)`,
        opacity: degradadoPie,
      }} />
    ) : null}
    {conLogo ? <LogoBetween formato="feed" posicion={posLogo} tono={logoTono} sombra={logoSombra} /> : null}
    <AbsoluteFill>
      <div
        style={{
          position: 'absolute',
          left: BETWEEN.bloque.margenX,
          right: BETWEEN.bloque.margenX,
          // la medida (y=220) es a la TINTA; el ascendente de la caja alta pide unos px.
          // En fotos con personas el bloque baja para no pasar texto sobre caras.
          ...(topBloque !== undefined
            ? {top: topBloque}
            : anclaje === 'arriba'
              ? {top: BETWEEN.bloque.yFeed - 9}
              : {bottom: 130}),
          display: 'flex',
          flexDirection: 'column',
          alignItems: alinear === 'centro' ? 'center' : 'flex-start',
        }}
      >
        {(() => {
          const anchoCaja = columna ?? 1080 - 2 * BETWEEN.bloque.margenX;
          const contenido = (
            <>
              <TitularBetween
                caps={caps} script={script} scriptSans={scriptSans}
                sizeCaps={sizeCaps} sizeScript={sizeScript}
                aireScriptATitulo={aireScriptATitulo}
                alinear={alinear}
                anchoDisponible={bloqueEnCaja ? anchoCaja - 2 * BETWEEN.cajas.padX : columna}
                mantenerPunto={mantenerPunto}
              />
              {bajada && bajadaEnCaja && !bloqueEnCaja ? (
                <PanelTaupe ancho={columnaCaja ?? columna} interlinea={interlineaBajada} style={{marginTop: aireTituloACaja}}>{bajada}</PanelTaupe>
              ) : bajada ? (
                <Bajada size={sizeBajada} style={{marginTop: BETWEEN.aire.tituloABajada, maxWidth: anchoBajada, textAlign: alinear === 'centro' ? 'center' : 'left'}}>{bajada}</Bajada>
              ) : null}
              {datos?.length ? (
                <PilaDatos
                  datos={datos}
                  /* dentro de la caja, la caja YA es el énfasis: ningún dato repite banda */
                  sinFondo={bloqueEnCaja ? datos.map((_, i) => i) : datosSinFondo}
                  style={{marginTop: BETWEEN.aire.tituloACaja}}
                />
              ) : null}
            </>
          );
          return bloqueEnCaja ? (
            <div
              style={{
                /* ⛔ `width` explícito, no `maxWidth`: `TitularBetween` se
                   dimensiona con `width: '100%'`, así que dentro de una caja
                   shrink-to-fit colapsa a una banda de ~80 px. Con `border-box`
                   el contenido mide `anchoCaja − 2 × padX`, que es justo el
                   `anchoDisponible` que recibe el titular. */
                width: anchoCaja,
                boxSizing: 'border-box',
                padding: `${Math.round(BETWEEN.cajas.alto * 0.28)}px ${BETWEEN.cajas.padX}px`,
                backgroundColor: BETWEEN.cajas.fondo,
                borderRadius: BETWEEN.cajas.radio,
                display: 'flex',
                flexDirection: 'column',
                alignItems: alinear === 'centro' ? 'center' : 'flex-start',
              }}
            >
              {contenido}
            </div>
          ) : contenido;
        })()}
      </div>
    </AbsoluteFill>
    {children}
    {arco ? <TextoArco>{arco}</TextoArco> : null}
    {pie ? <PieDePieza formato="feed" {...pie} /> : null}
    {legal ? <LegalAlPie formato="feed">{legal}</LegalAlPie> : null}
    {direccion ? (
      <DireccionAlPie formato="feed">
        {typeof direccion === 'string' ? direccion : BETWEEN.datos.direccionPieza}
      </DireccionAlPie>
    ) : null}
  </AbsoluteFill>
  );
};

/**
 * ⭐ Línea de llamado: línea fina que sale de una etiqueta y apunta a una parte
 * de la foto, con un punto en la punta. Recurso propio de Eli — aparece en las
 * historias de cheesecake, «LUNES DE CAFÉ» y «Día del Cacao».
 * Grosor MEDIDO en ST S1 N°3: **2 px**.
 */
export const LineaLlamado: React.FC<{
  desde: [number, number];
  hasta: [number, number];
  /** Punto en la punta, como en «LA MEJOR FORMA DE EMPEZAR LA SEMANA». */
  punto?: boolean;
  tono?: Tono;
  ancho?: number;
  alto?: number;
}> = ({desde, hasta, punto = true, tono = 'beige', ancho = 1080, alto = 1920}) => (
  <svg width={ancho} height={alto} viewBox={`0 0 ${ancho} ${alto}`} style={{position: 'absolute', inset: 0}}>
    <line
      x1={desde[0]} y1={desde[1]} x2={hasta[0]} y2={hasta[1]}
      stroke={tinta(tono)} strokeWidth={2}
    />
    {punto ? <circle cx={hasta[0]} cy={hasta[1]} r={7} fill={tinta(tono)} /> : null}
  </svg>
);

/**
 * ⭐ Marco de esquinas sobre el producto — las cuatro escuadras finas que Eli
 * pone alrededor del plato (historia del cheesecake). Mismo grosor de 2 px.
 */
export const MarcoEsquinas: React.FC<{
  x: number; y: number; w: number; h: number;
  /** Largo del brazo de cada escuadra. */
  brazo?: number;
  tono?: Tono;
  ancho?: number; alto?: number;
}> = ({x, y, w, h, brazo = 64, tono = 'beige', ancho = 1080, alto = 1920}) => {
  const c = tinta(tono);
  const esquinas = [
    `M ${x} ${y + brazo} L ${x} ${y} L ${x + brazo} ${y}`,
    `M ${x + w - brazo} ${y} L ${x + w} ${y} L ${x + w} ${y + brazo}`,
    `M ${x + w} ${y + h - brazo} L ${x + w} ${y + h} L ${x + w - brazo} ${y + h}`,
    `M ${x + brazo} ${y + h} L ${x} ${y + h} L ${x} ${y + h - brazo}`,
  ];
  return (
    <svg width={ancho} height={alto} viewBox={`0 0 ${ancho} ${alto}`} style={{position: 'absolute', inset: 0}}>
      {esquinas.map((d, i) => (
        <path key={i} d={d} stroke={c} strokeWidth={2} fill="none" />
      ))}
    </svg>
  );
};

/**
 * ⭐ Tarjeta de UI en crema — el recurso de los mockups de Eli (recordatorio,
 * lista de horarios con toggles, píldora de carnet, post de Instagram).
 * Color MEDIDO: `#FFF9EB` (el beige de marca), texto en café, esquinas suaves.
 */
export const TarjetaUI: React.FC<{
  children: React.ReactNode;
  x?: number; y?: number; w?: number;
  radio?: number;
  style?: React.CSSProperties;
}> = ({children, x, y, w, radio = 20, style}) => (
  <div
    style={{
      position: x === undefined ? 'relative' : 'absolute',
      left: x, top: y, width: w,
      backgroundColor: BETWEEN.colores.beige,
      color: BETWEEN.colores.cafe,
      borderRadius: radio,
      padding: '28px 34px',
      fontFamily: BETWEEN.fuentes.sans,
      fontWeight: BETWEEN.pesos.regular,
      fontSize: 34,
      lineHeight: 1.35,
      boxShadow: '0 10px 34px rgba(36,26,18,0.28)',
      ...style,
    }}
  >
    {children}
  </div>
);

/**
 * ⭐ Plantilla de story real: foto clara + logo centrado arriba + titular
 * (caps + script solapada) + lo que haga falta debajo.
 * Geometría medida: logo en y=271 y titular arrancando en y=425.
 */
export const PiezaStoryBetween: React.FC<{
  foto: string;
  posicionFoto?: string;
  oscurecer?: number;
  caps?: string;
  script?: string;
  sizeCaps?: number;
  datos?: React.ReactNode[];
  /**
   * Índices de `datos` que van SIN la caja taupe. Ver `CajaDato.sinFondo`:
   * en una pila, la caja es el énfasis y repetirla en las dos líneas lo mata.
   */
  datosSinFondo?: number[];
  bajada?: React.ReactNode;
  /** La bajada va DENTRO de una caja taupe, para cuando la foto no la deja leer. */
  bajadaEnCaja?: boolean;
  /** Ancho máximo de esa caja. A todo el ancho se ve pesada sobre un producto. */
  anchoBajada?: number;
  legal?: React.ReactNode;
  conLogo?: boolean;
  logoTono?: Tono;
  alinear?: 'izquierda' | 'centro';
  /** En fotos con personas el bloque baja para no pasar texto sobre caras ni ojos. */
  anclaje?: 'arriba' | 'abajo';
  /** Y exacta del bloque, cuando ni arriba ni abajo sirven. */
  topBloque?: number;
  /**
   * Ancho de composición del TITULAR, igual que `PiezaFeedBodegon.columna`.
   *
   * ⭐ AGREGADO EL 02-09-2026. La pieza llamaba a `TitularBetween` sin pasarle
   * `anchoDisponible`, así que el titular se autoescalaba hasta el MARGEN (912)
   * y no había forma de apretarlo desde la story sin tocar el sistema.
   *
   * Hizo falta porque `between-qa.py` marcó `BW-S-Cumple`: tinta a 74 px del
   * canto izquierdo y 72 del derecho, contra los 84 de la marca. La causa es
   * que **Brushwell sobresale de su ancho de avance** —la cola del «¿» inicial
   * y la del «?» final quedan fuera de la caja que mide el autoescalado—, así
   * que la caja cabía y la tinta no. Aparece en toda pieza cuya script empieza
   * con «¿»: también lo dio en `Cumple1`, `ToGo1` y `ToGo4`.
   *
   * Se pasa `BETWEEN.bloque.columna` (810) en la pieza que se está cortando.
   * Sigue siendo OPT-IN por la misma razón que en `TitularBetween`: cambiar el
   * defecto re-flujaría piezas ya aprobadas.
   */
  columnaTitular?: number;
  children?: React.ReactNode;
}> = ({
  foto, posicionFoto, oscurecer = 0.12,
  caps, script, sizeCaps, datos, datosSinFondo, bajada, bajadaEnCaja, anchoBajada, legal,
  conLogo = true, logoTono = 'beige', alinear = 'centro', anclaje = 'arriba',
  topBloque, columnaTitular, children,
}) => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra, ...CIFRAS_ALTAS}}>
    <FotoFondo src={foto} posicion={posicionFoto} oscurecer={oscurecer} />
    {conLogo ? <LogoBetween formato="story" posicion="arriba" tono={logoTono} /> : null}
    <div
      style={{
        position: 'absolute',
        left: BETWEEN.bloque.margenX,
        right: BETWEEN.bloque.margenX,
        // 'abajo' se queda sobre la zona segura de Meta (340 px) con holgura
        ...(topBloque !== undefined
          ? {top: topBloque}
          : anclaje === 'arriba'
            ? {top: BETWEEN.bloque.yStory - 9}
            : {bottom: 430}),
        display: 'flex',
        flexDirection: 'column',
        alignItems: alinear === 'centro' ? 'center' : 'flex-start',
      }}
    >
      <TitularBetween caps={caps} script={script} sizeCaps={sizeCaps} alinear={alinear}
        anchoDisponible={columnaTitular} />
      {datos?.length ? <PilaDatos datos={datos} sinFondo={datosSinFondo} style={{marginTop: BETWEEN.aire.tituloACaja}} /> : null}
      {bajada && bajadaEnCaja ? (
        <PanelTaupe ancho={anchoBajada} style={{marginTop: BETWEEN.aire.tituloACaja}}>{bajada}</PanelTaupe>
      ) : bajada ? (
        <Bajada style={{marginTop: BETWEEN.aire.tituloABajada, textAlign: alinear === 'centro' ? 'center' : 'left'}}>{bajada}</Bajada>
      ) : null}
    </div>
    {children}
    {legal ? (
      <div style={{position: 'absolute', left: 90, right: 90, bottom: 360}}>
        <Legal>{legal}</Legal>
      </div>
    ) : null}
  </AbsoluteFill>
);
