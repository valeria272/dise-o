/**
 * DOUBLETREE · FEED 21-10-2026 18:00 · CARRUSEL – 5 cosas que hacen especial tu
 * estadía en DoubleTree. Estado de la grilla (28-09): OK PARA DISEÑO.
 * Comentario para diseño: «Que sean 5 […] la primera la hospitalidad […] la segunda
 * habitación […] la tercera espacios recreativos […] la cuarta ubicación […] y la
 * quinta del gym» → ya está así en el brief: portada + 5 puntos + cierre = 7 láminas.
 *
 * ⚠️ La fila DISEÑOS de esa columna dice «REEL», pero el brief y el comentario son de
 * un CARRUSEL de láminas. Se diseña lo que dice el brief; la discrepancia se informa.
 *
 * ── Referencias (REF 1 pin 1096908053028487646 · REF 2 pin.it/1PYPHQtyv) ─────
 * Las dos son PORTADAS: foto a sangre con velo, titular serif CENTRADO al medio del
 * cuadro, una línea chica que lo acompaña y la invitación a deslizar abajo (flecha
 * en círculo / en píldora). Se toma eso; en DT la flecha es la píldora de contorno
 * de `C1 FT N1` (aprobada) y el titular va en Stag a dos pesos, mismo cuerpo (R-04).
 * Las interiores no tienen ref: siguen el carrusel «Tu día» aprobado (foto real a
 * sangre, velo azul que nace en 0, texto blanco alineado a la izquierda a 88 px).
 *
 * Firma UNA vez (R-11): el logotipo va sólo en la portada. Sin punto en títulos ni
 * bajadas (R-60): las bajadas del brief terminan en punto y acá se les quita; el
 * «01.» es la numeración del brief y se deja. Fotos reales, ninguna generada salvo
 * la hospitalidad, que es la escena de check-in del banco de la familia (25-09).
 */
import React from 'react';
import {AbsoluteFill} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';
import {FlechaPildora, Foto, Logo, SOMBRA, Velo} from './dtOct2';

cargarFuentesDT();

const BLANCO = DT.colores.blanco;
const M = DT.geometria.margenLateral;

const PUNTOS = [
  {
    n: '01.',
    t: 'La hospitalidad de siempre',
    s: 'Tu llegada comienza con un check-in cálido, un welcome drink y nuestra clásica galleta',
    foto: 'c5-hospitalidad',
  },
  {n: '02.', t: 'Tu refugio perfecto', s: 'Habitaciones amplias y muy cómodas, diseñadas para tu descanso absoluto', foto: 'c5-habitacion'},
  {
    n: '03.',
    t: 'Espacios para ti',
    s: 'Desconecta en nuestro Winter Garden o avanza en tus proyectos desde el cowork',
    foto: 'c5-espacios',
    // el tragaluz blanco del Winter Garden llega al borde: velo suave arriba (QA «texto al borde»)
    veloArriba: 0.34,
  },
  {
    n: '04.',
    t: 'Conectados con la ciudad',
    s: 'Ubicación estratégica para que te muevas con facilidad a tus reuniones o paseos',
    foto: 'c5-ubicacion',
  },
  {n: '05.', t: 'Tu rutina no se detiene', s: 'Gimnasio equipado y disponible 24/7 para recargar energías a tu ritmo', foto: 'c5-gym'},
] as const;

const foto = (k: string) => `assets/hilton/dt/oct2/${k}.jpg`;

/**
 * RONDA 2 (Eli, 28-09): «la portada se ve extraña… que sea como la referencia»: «5 cosas» como el
 * «What to Expect», «hacen especial» como el «When You Stay», y «tu estadía en DoubleTree» más bajo y
 * más chico, cerca de la flecha, «tal cual como está la dos referencia». Y otra foto: la fachada ya se
 * usó mucho. Se calca la REF 2 medida (736×920 → ×1,467): texto chico al 20 % del alto, el titular
 * serif grande debajo, la foto entera oscurecida pareja, y abajo (86 %) la línea en itálica sobre la
 * píldora con la flecha.
 *   A · el sillón del lounge (sesión SEP 2026, `sep_26-246`), como el sofá de la ref.
 *   B · la familia en el sofá del banco aprobado (25-09), la opción más literal de la ref.
 */
const Portada: React.FC<{fondo: 'a' | 'b'}> = ({fondo}) => (
  <>
    <Foto src={foto(fondo === 'a' ? 'c5-portada' : 'c5-portada-b')} />
    <AbsoluteFill style={{background: 'rgba(9,25,78,0.3)'}} />
    <Velo desde={0.4} pie={0.7} />
    <Logo formato="feed" />
    {/* RONDA 3 (Eli, 28-09): «el 5 cosas que hacen especial queden abajo junto a tu estadía en
        DoubleTree… así como la referencia 2, pero abajo junto a la flecha». Todo el texto baja y se
        apila sobre la flecha; arriba queda sólo el logo y la foto respira. */}
    <div style={{position: 'absolute', bottom: 132, left: 0, width: 1080, textAlign: 'center', color: BLANCO}}>
      <div style={{fontFamily: DT.fuentes.texto, fontSize: 40, letterSpacing: '0.02em', textShadow: SOMBRA}}>5 cosas que</div>
      <div
        style={{
          fontFamily: DT.fuentes.titular,
          fontWeight: DT.pesos.regular,
          fontSize: 128,
          lineHeight: 1,
          letterSpacing: '-0.01em',
          marginTop: 14,
          textShadow: SOMBRA,
          whiteSpace: 'nowrap',
        }}
      >
        hacen especial
      </div>
      <div
        style={{
          marginTop: 22,
          fontFamily: DT.fuentes.titular,
          fontStyle: 'italic',
          fontWeight: DT.pesos.light,
          fontSize: 36,
          letterSpacing: '0.01em',
          textShadow: SOMBRA,
        }}
      >
        tu estadía en DoubleTree
      </div>
      <div style={{display: 'flex', justifyContent: 'center', marginTop: 26}}>
        <FlechaPildora ancho={176} />
      </div>
    </div>
  </>
);

const Punto: React.FC<{i: number}> = ({i}) => {
  const p = PUNTOS[i];
  return (
    <>
      <Foto src={foto(p.foto)} />
      {'veloArriba' in p ? <Velo desde={0.75} pie={p.veloArriba} lado="arriba" /> : null}
      <Velo desde={0.42} pie={0.86} />
      <div style={{position: 'absolute', left: M, right: M, bottom: 118, color: BLANCO}}>
        <div style={{fontFamily: DT.fuentes.titular, fontWeight: DT.pesos.light, fontSize: 62, lineHeight: 1.1, textShadow: SOMBRA}}>{p.n}</div>
        <div style={{fontFamily: DT.fuentes.titular, fontWeight: DT.pesos.medium, fontSize: 62, lineHeight: 1.12, marginTop: 4, textShadow: SOMBRA}}>
          {p.t}
        </div>
        <div style={{width: 96, height: 1.5, background: 'rgba(250,250,250,0.85)', margin: '30px 0 26px'}} />
        <div
          style={{
            maxWidth: 780,
            fontFamily: DT.fuentes.titular,
            fontWeight: DT.pesos.regular,
            fontSize: 33,
            lineHeight: 1.32,
            wordSpacing: '0.08em',
            textShadow: SOMBRA,
          }}
        >
          {p.s}
        </div>
      </div>
    </>
  );
};

/** Ronda 2: el cierre hace ESPEJO de la portada (continuidad del carrusel): la misma foto oscurecida
 * pareja, el titular serif grande arriba y el llamado chico en itálica abajo, donde la portada tenía
 * «tu estadía en DoubleTree». El lounge iluminado de la sesión SEP 2026 (`sep_26-250`), otro ángulo que la portada. */
const Cierre: React.FC = () => (
  <>
    <Foto src={foto('c5-cierre')} />
    <AbsoluteFill style={{background: 'rgba(9,25,78,0.3)'}} />
    <Velo desde={0.4} pie={0.7} />
    {/* RONDA 3 (Eli, 28-09): «todo listo para recibirte me gustaría que quede abajo, así está todo
        compensado con la portada»: el titular baja sobre el llamado, a la misma altura que la portada. */}
    <div style={{position: 'absolute', bottom: 150, left: 0, width: 1080, textAlign: 'center', color: BLANCO}}>
      <div
        style={{
          fontFamily: DT.fuentes.titular,
          fontWeight: DT.pesos.regular,
          fontSize: 104,
          lineHeight: 1.04,
          letterSpacing: '-0.01em',
          textShadow: SOMBRA,
        }}
      >
        Todo listo
        <br />
        para recibirte
      </div>
      <div
        style={{
          marginTop: 30,
          fontFamily: DT.fuentes.titular,
          fontStyle: 'italic',
          fontWeight: DT.pesos.light,
          fontSize: 36,
          letterSpacing: '0.01em',
          textShadow: SOMBRA,
        }}
      >
        Haz clic en el enlace de la bio y reserva tu estadía
      </div>
    </div>
  </>
);

/** `lamina` 1–7: 1 portada, 2–6 los cinco puntos, 7 el cierre. */
export const DtC5CosasOct: React.FC<{lamina: number; fondo?: 'a' | 'b'}> = ({lamina, fondo = 'a'}) => (
  <AbsoluteFill style={{backgroundColor: DT.colores.azul}}>
    {lamina === 1 ? <Portada fondo={fondo} /> : lamina === 7 ? <Cierre /> : <Punto i={lamina - 2} />}
  </AbsoluteFill>
);
