/**
 * Entry de DOUBLETREE · CAMPAÑA ARMY (02-10-2026). Entry propio, como los de octubre, para no
 * tocar lo ya entregado.
 *
 * Eli (02-10): «por ahora concéntrate sólo en el KV de post normal, así después adaptamos». Ronda 2:
 * centrado y más Cyber, en dos diseños — `Ciudad` (la aérea, hotel morado) y `Habitacion` (la cama
 * con detalles morados y el panel de cristal del Cyber).
 *
 *   python scripts/dt-army-rendir.py
 */
import React from 'react';
import {Composition, Folder, registerRoot} from 'remotion';

import {DtArmyCiudad, DtArmyHabitacion, Linea} from './compositions/hilton/DtArmy';

const feed = {durationInFrames: 1, fps: 30, width: 1080, height: 1350} as const;
const LINEAS: {id: string; linea: Linea}[] = [
  {id: 'Preventa', linea: 'preventa'},
  {id: 'Venta', linea: 'venta'},
];

const Raiz: React.FC = () => (
  <Folder name="DT-Army-KV">
    {LINEAS.map((l) => (
      <React.Fragment key={l.id}>
        <Composition id={`DT-Army-KV-Ciudad-${l.id}`} component={DtArmyCiudad} defaultProps={{linea: l.linea}} {...feed} />
        {/* la tercera opción (Eli, 02-10): la ciudad con el logo en morado haciendo de «DoubleTree» */}
        <Composition id={`DT-Army-KV-CiudadLogo-${l.id}`} component={DtArmyCiudad} defaultProps={{linea: l.linea, variante: 'logo' as const}} {...feed} />
        <Composition id={`DT-Army-KV-Habitacion-${l.id}`} component={DtArmyHabitacion} defaultProps={{linea: l.linea}} {...feed} />
      </React.Fragment>
    ))}
  </Folder>
);

registerRoot(Raiz);
