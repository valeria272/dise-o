/**
 * Plancha de trazos de Eli — utilidad de EXTRACCIÓN, no una pieza.
 *
 * Rinde `Flechas y trazados, globos BETWEEN.svg` (el editable original de Eli,
 * `1EZHJab1Rp8c8vuTHqAehF6tCk-CiRsXa`) sobre fondo transparente, para poder
 * MIRAR qué trazos existen y recortarlos por canal alfa. Es el mismo camino por
 * el que salieron los ocho de `ILUSTRACIONES` en `BetweenRecursos.tsx`.
 *
 * No se registra en `BetweenEntry.tsx` ni se entrega: sólo vive en `src/Root.tsx`
 * para poder correr `npx remotion still src/index.ts BW-Plancha-Trazos ...`.
 *
 * El viewBox del SVG es 2660,29 × 827,72 → se rinde a 2660×828.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';

export const PlanchaTrazos: React.FC = () => (
  <AbsoluteFill>
    <Img
      src={staticFile('assets/hilton/between/recursos/_plancha-trazos.svg')}
      style={{width: '100%', height: '100%', objectFit: 'contain'}}
    />
  </AbsoluteFill>
);
