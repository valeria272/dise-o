/**
 * Prueba de calibración — 27-08-2026.
 *
 * Reproduce con nuestros componentes la pieza que la diseñadora marcó como
 * «uso correcto de la tipografía» (raw/hilton/between-adn/ref-tipografia-ok/
 * C1 S3 N°1.png). Se rinde sobre NEGRO a propósito: lo que se compara es la
 * TINTA, no la foto.
 *
 * Objetivo medido en la pieza de ella, sobre lienzo de 1080:
 *   script «El Match»            403 × 124, centrada, tinta arriba en y = 180
 *   caja alta «PERFECTO»         567 ×  85, centrada, tinta arriba en y = 312
 *   caja taupe                   597 ×  66, centrada, arriba en y = 416
 */
import React from 'react';
import {AbsoluteFill} from 'remotion';

import {BETWEEN} from '../../brand/hilton-between';
import {CajaDato, TitularBetween} from './BetweenSistema';

export const CalibracionTipografia: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: '#000'}}>
    <div style={{position: 'absolute', left: 0, right: 0, top: BETWEEN.bloque.yFeed}}>
      <TitularBetween script="El Match" caps="Perfecto" alinear="centro" />
      <div style={{display: 'flex', justifyContent: 'center', marginTop: BETWEEN.aire.tituloACaja}}>
        <CajaDato>Para empezar el día</CajaDato>
      </div>
    </div>
  </AbsoluteFill>
);
