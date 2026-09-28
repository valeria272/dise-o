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

const Portada: React.FC = () => (
  <>
    <Foto src={foto('c5-portada')} />
    <AbsoluteFill style={{background: 'rgba(9,25,78,0.28)'}} />
    <Velo desde={0.25} pie={0.6} />
    <Logo formato="feed" />
    <div style={{position: 'absolute', top: 560, left: 0, width: 1080, textAlign: 'center', color: BLANCO}}>
      {[
        {t: '5 cosas que hacen especial', w: DT.pesos.medium},
        {t: 'tu estadía en DoubleTree', w: DT.pesos.light},
      ].map((l) => (
        <div key={l.t} style={{fontFamily: DT.fuentes.titular, fontWeight: l.w, fontSize: 70, lineHeight: 1.16, textShadow: SOMBRA, whiteSpace: 'nowrap'}}>
          {l.t}
        </div>
      ))}
      <div style={{display: 'flex', justifyContent: 'center', marginTop: 70}}>
        <FlechaPildora ancho={180} />
      </div>
    </div>
  </>
);

const Punto: React.FC<{i: number}> = ({i}) => {
  const p = PUNTOS[i];
  return (
    <>
      <Foto src={foto(p.foto)} />
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

const Cierre: React.FC = () => (
  <>
    <Foto src={foto('c5-cierre')} />
    <AbsoluteFill style={{background: 'rgba(9,25,78,0.44)'}} />
    <Velo desde={0.3} pie={0.7} />
    <div style={{position: 'absolute', top: 600, left: 0, width: 1080, textAlign: 'center', color: BLANCO}}>
      <div style={{fontFamily: DT.fuentes.titular, fontWeight: DT.pesos.medium, fontSize: 76, lineHeight: 1.1, textShadow: SOMBRA}}>
        Todo listo para recibirte
      </div>
      <div style={{width: 120, height: 1.5, background: 'rgba(250,250,250,0.85)', margin: '44px auto 38px'}} />
      <div
        style={{
          width: 720,
          margin: '0 auto',
          fontFamily: DT.fuentes.titular,
          fontWeight: DT.pesos.light,
          fontSize: 38,
          lineHeight: 1.3,
          wordSpacing: '0.08em',
          textShadow: SOMBRA,
        }}
      >
        Haz clic en el enlace de la bio y reserva tu estadía
      </div>
    </div>
  </>
);

/** `lamina` 1–7: 1 portada, 2–6 los cinco puntos, 7 el cierre. */
export const DtC5CosasOct: React.FC<{lamina: number}> = ({lamina}) => (
  <AbsoluteFill style={{backgroundColor: DT.colores.azul}}>
    {lamina === 1 ? <Portada /> : lamina === 7 ? <Cierre /> : <Punto i={lamina - 2} />}
  </AbsoluteFill>
);
