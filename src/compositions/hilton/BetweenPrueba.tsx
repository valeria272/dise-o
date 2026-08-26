/**
 * Prueba A/B del sistema medido — 26-08-2026.
 *
 * Reproduce la pieza real «EL MATCH perfecto» (C1 S2 N°1 de Eli) con los
 * componentes nuevos, sobre una foto equivalente del banco. Sirve para
 * comparar contra raw/hilton/between-adn/ref-piezas/C1 S2 N°1.png antes de
 * rehacer la grilla completa.
 */
import React from 'react';

import {PiezaFeedBodegon} from './BetweenSistema';

const F = 'assets/hilton/between/fotos/';

/** Con el sistema MEDIDO: titular 94, script 185 solapada, cajas taupe, arco. */
export const MatchPerfectoNuevo: React.FC = () => (
  <PiezaFeedBodegon
    foto={F + 'togo-brownie.jpg'}
    posicionFoto="center"
    oscurecer={0.12}
    caps="El match"
    script="perfecto"
    datos={['Café to go + dulce', 'Desde $3.790']}
    arco="Vigilantes, muffin, brownie y más"
  />
);
