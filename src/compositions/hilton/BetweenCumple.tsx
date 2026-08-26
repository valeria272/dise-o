/**
 * BETWEEN — Café de cumpleaños (grilla septiembre, feed 3 sept)
 *
 * Técnica de montaje que usa Eli: packshot real recortado + fondo generado en
 * Magnific + ilustración de globos + slide de detalles con mockup de post de IG.
 *
 * Textos de la grilla: "ESTE CAFÉ ES PARA TI" /
 * "Si estás de cumpleaños, en Between te invitamos el café".
 * Comentario de diseño: "Agregar elementos cumpleañeros como en el anterior".
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {BETWEEN, cargarFuentesBetween} from '../../brand/hilton-between';
import {Bajada, Dato, Legal, TitularBetween} from './BetweenSistema';
import {Globos, MarcoIGPost} from './BetweenRecursos';

cargarFuentesBetween();

const FONDO = 'assets/hilton/between/fotos/fondo-festivo.png';
const TAZA = 'assets/hilton/between/fotos/taza-latte-nobg.png';
const TAZA_SQ = 'assets/hilton/between/fotos/taza-cuadrada.png';

/** Slide 1 — portada festiva con la taza montada sobre el fondo generado */
export const CumpleFestivoPortada: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <Img src={staticFile(FONDO)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
    {/* multiply mínimo, solo lo justo para que el beige lea */}
    <AbsoluteFill
      style={{
        backgroundColor: BETWEEN.colores.sombra,
        opacity: 0.22,
        mixBlendMode: 'multiply',
      }}
    />

    {/*
      Título con la escala MEDIDA (26-08): la pieza equivalente de Eli
      («¡VEN POR TU CAFÉ / de cumpleaños!») lleva caja alta de 69 px de tinta y
      script de 132 — o sea caps ~96 con la script casi al doble, montada encima.
      Antes iba 80/96 apilados con gap, y por eso se veía chico y ordenadito.
    */}
    <AbsoluteFill style={{alignItems: 'center', paddingTop: 150}}>
      <TitularBetween caps="¡Este café" script="es para ti!" sizeCaps={96} alinear="centro" />
    </AbsoluteFill>

    {/* packshot real */}
    <Img
      src={staticFile(TAZA)}
      style={{
        position: 'absolute',
        width: 640,
        left: '50%',
        bottom: 250,
        transform: 'translateX(-50%)',
        filter: 'drop-shadow(0 32px 42px rgba(36,26,18,0.5))',
      }}
    />

    {/* globos originales de Eli: pocos y sutiles */}
    <Globos
      posiciones={[
        {cual: 'globo', x: 78, y: 604, ancho: 168, rotacion: -12},
        {cual: 'globoAlt', x: 872, y: 690, ancho: 140, rotacion: 16, espejo: true},
      ]}
    />

    <AbsoluteFill
      style={{
        justifyContent: 'flex-end',
        alignItems: 'center',
        gap: 22,
        paddingBottom: 74,
      }}
    >
      <Bajada style={{textAlign: 'center', maxWidth: 780}}>
        Si estás de cumpleaños, en Between te invitamos el café
      </Bajada>
      <Dato size={26} espaciado>Desliza para conocer los detalles ›››</Dato>
    </AbsoluteFill>
  </AbsoluteFill>
);

/** Slide 2 — detalles dentro de un mockup de post de Instagram */
export const CumpleFestivoDetalles: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: BETWEEN.colores.sombra}}>
    <Img
      src={staticFile(FONDO)}
      style={{width: '100%', height: '100%', objectFit: 'cover', filter: 'blur(7px)'}}
    />
    <AbsoluteFill
      style={{
        backgroundColor: BETWEEN.colores.sombra,
        opacity: 0.34,
        mixBlendMode: 'multiply',
      }}
    />

    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center'}}>
      <MarcoIGPost
        foto={<Img src={staticFile(TAZA_SQ)} style={{width: '100%', display: 'block'}} />}
        burbujas={[
          'Te regalamos un café para disfrutar en cafetería o To Go',
          'Accede a este regalo el mismo día de tu cumpleaños',
          'Disponible de lunes a viernes, en cualquier horario',
          'Pregúntanos por los cafés disponibles',
        ]}
      />
    </AbsoluteFill>

    <AbsoluteFill style={{justifyContent: 'flex-end', alignItems: 'center', paddingBottom: 58}}>
      <Legal style={{maxWidth: 820, marginLeft: 'auto', marginRight: 'auto'}}>
        *Presenta tu carnet para canjear tu café de cumpleaños. Extras y personalizaciones no incluidas.
      </Legal>
    </AbsoluteFill>

    <Globos posiciones={[{cual: 'globosPar', x: 56, y: 966, ancho: 172, rotacion: -12}]} />
  </AbsoluteFill>
);
