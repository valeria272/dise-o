/**
 * BETWEEN — detalles ILUSTRADOS de las Fiestas Patrias (08-09-2026)
 *
 * ⚠️ POR QUÉ ESTO EXISTE, Y POR QUÉ NO CONTRADICE EL MANUAL.
 * La regla de la marca es que «los globos y flechas salen del `.svg` de Eli. No
 * se dibujan a mano ni se generan con IA — ya existen y tienen el trazo de la
 * marca», y esa regla se respetó en las dos primeras rondas de la S3: el brindis
 * de la referencia se resolvió con dos tazas de verdad, fotografiadas.
 *
 * En la ronda 3 Eli pidió lo contrario, explícitamente y para esta pieza:
 *
 *   «Para la ST 3 sucede que el contexto es 18 de septiembre de fiestas patrias
 *    de Chile, necesito que sea detalles ILUSTRADOS y haz más similar a la
 *    referencia con los colores de between.»
 *
 * O sea que el trazo que hay que igualar acá es el del REFERENTE que ella eligió
 * (`raw/hilton/between/ref-s3-eli/REF 1 (STORIE 3 S3).jpg`): línea suelta, de un
 * solo color, con puntas redondeadas, sobre un cartel de color. Y el repertorio
 * de Eli no tiene ninguno de estos dos motivos —no hay brindis ni guirnalda—,
 * así que no había de dónde tomarlos.
 *
 * **Las dos condiciones que se mantienen**, para que esto no se vuelva una
 * licencia general:
 *   1. Un solo color, y es de la marca: se le pasa `tinta` y en la pieza va el
 *      café `#675B49`. Nada de rojo, azul ni blanco de bandera — Eli pidió «con
 *      los colores de between» y la bandera chilena no es la paleta de Between.
 *   2. Trazo de grosor constante con `strokeLinecap="round"`, como el referente.
 *      No se imita el pincel de Brushwell ni los garabatos del `.svg` de Eli:
 *      son otro lenguaje y mezclarlos sí sería inventarle un trazo a la marca.
 *
 * Los dos motivos se dibujan sobre un `viewBox` fijo y se escalan por ancho, así
 * que se pueden reusar en cualquier formato sin deformarse.
 */
import React from 'react';

/* ══════════════════════════════════════════════════════════════════════════
   GUIRNALDA DE BANDERITAS

   El detalle de Fiestas Patrias más reconocible que no es la bandera misma. La
   cuerda es una cuadrática que se descuelga en el centro y las banderitas se
   reparten sobre ella con la inclinación de la tangente, alternando maciza y de
   contorno — que es el ritmo que usan las guirnaldas de verdad y el que evita
   que se lea como una fila de triángulos pegados.
   ══════════════════════════════════════════════════════════════════════════ */

const VB_GUIRNALDA = {w: 760, h: 150};

/** Punto y ángulo de una cuadrática en t, para colgar cada banderita. */
const enLaCuerda = (t: number) => {
  const [x0, y0] = [8, 16];
  const [cx, cy] = [380, 118];
  const [x1, y1] = [752, 16];
  const u = 1 - t;
  const x = u * u * x0 + 2 * u * t * cx + t * t * x1;
  const y = u * u * y0 + 2 * u * t * cy + t * t * y1;
  // derivada de la cuadrática → tangente → inclinación de la banderita
  const dx = 2 * u * (cx - x0) + 2 * t * (x1 - cx);
  const dy = 2 * u * (cy - y0) + 2 * t * (y1 - cy);
  return {x, y, giro: (Math.atan2(dy, dx) * 180) / Math.PI};
};

export const GuirnaldaBanderitas: React.FC<{
  ancho: number;
  tinta: string;
  /** Cuántas banderitas. 9 es lo que cabe sin que se toquen a este ancho. */
  cuantas?: number;
  trazo?: number;
}> = ({ancho, tinta, cuantas = 9, trazo = 5}) => {
  const escala = ancho / VB_GUIRNALDA.w;
  const bandera = {ancho: 46, alto: 62};
  return (
    <svg
      width={ancho}
      height={VB_GUIRNALDA.h * escala}
      viewBox={`0 0 ${VB_GUIRNALDA.w} ${VB_GUIRNALDA.h}`}
      fill="none"
      stroke={tinta}
      strokeWidth={trazo}
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden
    >
      <path d="M8,16 Q380,118 752,16" />
      {Array.from({length: cuantas}).map((_, i) => {
        // se dejan los extremos libres: la primera y la última banderita no
        // cuelgan del nudo, igual que en una guirnalda colgada de verdad
        const t = (i + 1) / (cuantas + 1);
        const {x, y, giro} = enLaCuerda(t);
        const macizo = i % 2 === 0;
        const w = bandera.ancho / 2;
        return (
          <g key={i} transform={`translate(${x} ${y}) rotate(${giro})`}>
            <path
              d={`M${-w},2 L${w},2 L0,${bandera.alto} Z`}
              fill={macizo ? tinta : 'none'}
              strokeWidth={trazo}
            />
          </g>
        );
      })}
    </svg>
  );
};

/* ══════════════════════════════════════════════════════════════════════════
   EL BRINDIS — dos tazas de café que se chocan

   Es el motivo central del referente (ahí son dos copas de vino) traído al
   producto de la marca.

   ⛔ SIN BRAZOS NI MANOS, Y ES UNA DECISIÓN, NO UNA OMISIÓN.
   El referente los tiene y se intentaron dos veces. La primera, con la mano
   maciza, dejó dos manchas café que sobre el beige se leían como borrones. La
   segunda, con la mano de contorno, dejó **dos aros cruzando la taza y el asa**:
   a tamaño de historia no se leía una mano, se leían dos círculos de más. Y una
   mano mal dibujada es peor que ninguna — es la misma lección que el manual ya
   tiene escrita para las manos generadas con IA («hay una mano de más» fue un
   rechazo). Dos tazas chocándose con sus chispas es un pictograma que se lee
   solo, y se lee a 1080 px de ancho.

   ⚠️ LA GEOMETRÍA QUE HACE QUE SE LEA EL CHOQUE, medida sobre el render:
     · bases en x=300 y x=460, y cada taza girada 10° SOBRE SU BASE hacia el
       centro. Ojo con el sentido: la izquierda va `rotate(+10)` y la derecha
       `rotate(-10) scale(-1 1)`. Con los signos al revés las bocas se abren
       hacia afuera y las tazas quedan a 200 px — que es lo que pasó al primer
       intento y por eso no había brindis;
     · con esos valores las bocas quedan a **8 px**. Si se solapan, las dos se
       leen como un objeto raro; si se separan más de ~20, se pierde el gesto;
     · el asa va SIEMPRE al lado de AFUERA, así la silueta interior queda limpia
       y el punto de contacto es sólo borde contra borde.
   ══════════════════════════════════════════════════════════════════════════ */

const VB_BRINDIS = {w: 760, h: 340};

/** Una taza, con la BASE en el origen para poder girarla sobre su propia base. */
const Taza: React.FC<{trazo: number}> = ({trazo}) => (
  <g>
    {/* cuerpo: boca ancha arriba, base angosta */}
    <path d="M-52,-140 C-50,-72 -44,-26 -38,-10 C-32,6 -16,14 0,14 C16,14 32,6 38,-10 C44,-26 50,-72 52,-140" />
    {/* la boca */}
    <path d="M-52,-140 c0,-14 23,-25 52,-25 c29,0 52,11 52,25 c0,14 -23,25 -52,25 c-29,0 -52,-11 -52,-25 z" />
    {/* el café adentro, una sola curva */}
    <path d="M-34,-138 c10,7 21,10 34,10 c13,0 24,-3 34,-10" strokeWidth={trazo * 0.85} />
    {/* el asa, al lado de afuera */}
    <path d="M-52,-112 c-27,1 -42,15 -42,32 c0,17 15,29 35,29" />
  </g>
);

/** Voluta de vapor. Dos por taza y bien altas: chicas se leen como apóstrofos. */
const Vapor: React.FC<{trazo: number}> = ({trazo}) => (
  <g strokeWidth={trazo * 0.9}>
    <path d="M-16,-14 c-16,-26 14,-38 -2,-64 c-10,-16 2,-26 6,-34" />
    <path d="M20,-24 c-16,-26 14,-38 -2,-64 c-8,-13 1,-22 5,-29" />
  </g>
);

export const BrindisTazas: React.FC<{
  ancho: number;
  tinta: string;
  trazo?: number;
}> = ({ancho, tinta, trazo = 5}) => {
  const escala = ancho / VB_BRINDIS.w;
  const base = 300;      // y de las bases de las dos tazas
  const giro = 10;
  return (
    <svg
      width={ancho}
      height={VB_BRINDIS.h * escala}
      viewBox={`0 0 ${VB_BRINDIS.w} ${VB_BRINDIS.h}`}
      fill="none"
      stroke={tinta}
      strokeWidth={trazo}
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden
    >
      <g transform={`translate(300 ${base}) rotate(${giro})`}>
        <Taza trazo={trazo} />
      </g>
      {/* la de la derecha es la misma geometría espejada, así las dos tazas son
          idénticas y el asa le queda al lado de afuera */}
      <g transform={`translate(460 ${base}) rotate(${-giro}) scale(-1 1)`}>
        <Taza trazo={trazo} />
      </g>

      {/* el vapor, sobre cada boca */}
      <g transform={`translate(310 ${base - 172})`}>
        <Vapor trazo={trazo} />
      </g>
      <g transform={`translate(450 ${base - 172}) scale(-1 1)`}>
        <Vapor trazo={trazo} />
      </g>

      {/* Las chispas del choque. Van CORTAS y METIDAS entre las dos columnas de
          vapor (x 342–418): estiradas hacia afuera se cruzaban con las volutas y
          el remate de arriba se leía como una maraña. La recta contra la onda es
          lo que las distingue del vapor. */}
      <path d="M380,124 L380,100" strokeWidth={trazo} />
      <path d="M356,132 L342,116" strokeWidth={trazo} />
      <path d="M404,132 L418,116" strokeWidth={trazo} />
    </svg>
  );
};

/* ══════════════════════════════════════════════════════════════════════════
   LA BANDERITA DE CHILE

   Eli, ronda 4: «añade una ilustración cute de la bandera de Chile, similar a la
   ilustracion». O sea: el motivo es la bandera, pero el lenguaje es el mismo que
   la guirnalda y el brindis — línea suelta, un solo color, puntas redondeadas.

   ⚠️ VA EN UNA SOLA TINTA, y es una decisión de paleta, no un olvido. Eli pidió
   dos cosas en el mismo mensaje: la bandera de Chile Y «los colores de between».
   El rojo y el azul de la bandera no están en la paleta de la marca, y meterlos
   rompería la pieza — así que la bandera se dibuja como se dibuja una bandera en
   una ilustración de una tinta: **la geometría hace el trabajo**. El cantón
   cuadrado arriba a la izquierda, la estrella de cinco puntas calada dentro de
   él y la división horizontal son lo que la vuelve inconfundiblemente chilena;
   ninguna otra bandera tiene esa combinación.

   La estrella se dibuja en el color del PAPEL y no en `none`: sobre el cantón
   macizo tiene que leerse en negativo, como el blanco de la bandera de verdad.
   Por eso el componente pide `fondo`.

   Lo «cute»: la tela ondea —el borde libre es una S y las dos franjas la siguen—,
   el mástil es corto y con la punta redondeada, y todo va inclinado. Una bandera
   recta y rectangular se lee como un ícono de menú de idioma.
   ══════════════════════════════════════════════════════════════════════════ */

const VB_BANDERA = {w: 300, h: 240};

export const BanderaChile: React.FC<{
  ancho: number;
  tinta: string;
  /** Color del papel: la estrella se cala con él sobre el cantón macizo. */
  fondo: string;
  trazo?: number;
  /** Inclinación en grados. Positiva = la punta sube a la derecha. */
  giro?: number;
}> = ({ancho, tinta, fondo, trazo = 5, giro = -8}) => {
  const escala = ancho / VB_BANDERA.w;
  return (
    <svg
      width={ancho}
      height={VB_BANDERA.h * escala}
      viewBox={`0 0 ${VB_BANDERA.w} ${VB_BANDERA.h}`}
      fill="none"
      stroke={tinta}
      strokeWidth={trazo}
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden
    >
      <g transform={`rotate(${giro} 150 130)`}>
        {/* el mástil */}
        <path d="M56,224 L56,36" strokeWidth={trazo * 1.4} />
        {/* la tela: el borde de arriba y el de abajo ondean, y el borde libre
            es una S — es lo que da el vuelo */}
        <path d="M56,44 C112,30 168,58 224,44 C244,39 258,42 268,48 C258,74 258,112 268,140 C258,146 244,149 224,144 C168,158 112,130 56,144 Z" />
        {/* La división horizontal, siguiendo la misma onda que la tela.
            ⚠️ TERMINA EN x=256 y no en 266: el borde libre de la tela pasa por
            x≈268 y con la punta redondeada del trazo la línea SOBRESALÍA de la
            bandera — al zoom se veía una espina saliendo por la derecha. */}
        <path d="M56,94 C112,80 168,108 224,94 C240,90 250,92 256,95" />
        {/* El cantón: cuadrado, arriba a la izquierda, macizo.
            ⚠️ Sus bordes de arriba y de abajo van SOBRE las mismas curvas de la
            tela y de la división, evaluadas en x=118: arriba y≈41, abajo y≈91.
            La primera versión los puso en 48 y 99 —a ojo— y el cantón quedaba
            14 px más abajo que la división: al zoom se veía un escalón en la
            esquina inferior derecha. Si se mueve la onda de la tela, hay que
            volver a evaluar estos dos puntos. */}
        <path d="M56,44 C77,38 98,39 118,41 C117,58 117,76 118,91 C98,88 77,89 56,94 Z"
              fill={tinta} />
        {/* La estrella de cinco puntas, calada en el color del papel. Centro
            (87,66) —el centro real del cantón— radio 21 y radio interior 8,6. */}
        <path
          d="M87,45 L92.1,59 L107,59.5 L95.2,68.7 L99.3,83 L87,74.6 L74.7,83 L78.8,68.7 L67,59.5 L81.9,59 Z"
          fill={fondo}
          stroke={fondo}
          strokeWidth={trazo * 0.5}
        />
      </g>
    </svg>
  );
};
