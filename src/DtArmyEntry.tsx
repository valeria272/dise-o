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

import {DtArmyAdaptacion, DtArmyCiudad, DtArmyClienta, DtArmyHabitacion, FormatoArmy, Linea} from './compositions/hilton/DtArmy';

const feed = {durationInFrames: 1, fps: 30, width: 1080, height: 1350} as const;
const LINEAS: {id: string; linea: Linea}[] = [
  {id: 'Preventa', linea: 'preventa'},
  {id: 'Venta', linea: 'venta'},
];

// Las adaptaciones de las opciones 1 y 2 (Eli, 02-10): historia, historia para paid y post para paid (1:1)
const ADAPTACIONES: {id: string; formato: FormatoArmy; alto: number}[] = [
  {id: 'ST', formato: 'st', alto: 1920},
  {id: 'STPaid', formato: 'stPaid', alto: 1920},
  {id: 'PostPaid', formato: 'paid', alto: 1080},
];
const FONDOS = [
  {id: 'Ciudad', fondo: 'ciudad'},
  {id: 'Clienta', fondo: 'clienta'},
] as const;

const Raiz: React.FC = () => (
  <Folder name="DT-Army-KV">
    {LINEAS.map((l) => (
      <React.Fragment key={l.id}>
        <Composition id={`DT-Army-KV-Ciudad-${l.id}`} component={DtArmyCiudad} defaultProps={{linea: l.linea}} {...feed} />
        {/* la tercera opción (Eli, 02-10): la ciudad con el logo en morado haciendo de «DoubleTree» */}
        <Composition id={`DT-Army-KV-CiudadLogo-${l.id}`} component={DtArmyCiudad} defaultProps={{linea: l.linea, variante: 'logo' as const}} {...feed} />
        <Composition id={`DT-Army-KV-Habitacion-${l.id}`} component={DtArmyHabitacion} defaultProps={{linea: l.linea}} {...feed} />
        {/* rondas 12 y 13 (Scarlette y Eli, 02-10): la opción 2 con la fachada del Día del Turismo al atardecer y en
            morado, sin globos, y la tarjeta blanca al centro */}
        <Composition id={`DT-Army-KV-Fachada-${l.id}`} component={DtArmyHabitacion} defaultProps={{linea: l.linea, foto: 'assets/hilton/dt/army/fachada-atardecer.jpg', tarjeta: true}} {...feed} />
        {/* ronda 14 (Eli, 02-10): la opción 2 que queda — la foto de la clienta con filtro morado, sin recuadro */}
        <Composition id={`DT-Army-KV-Clienta-${l.id}`} component={DtArmyClienta} defaultProps={{linea: l.linea}} {...feed} />
        {ADAPTACIONES.map((a) =>
          FONDOS.map((x) => (
            <Composition
              key={a.id + x.id}
              id={`DT-Army-${a.id}-${x.id}-${l.id}`}
              component={DtArmyAdaptacion}
              defaultProps={{linea: l.linea, fondo: x.fondo, formato: a.formato}}
              durationInFrames={1}
              fps={30}
              width={1080}
              height={a.alto}
            />
          )),
        )}
      </React.Fragment>
    ))}
  </Folder>
);

registerRoot(Raiz);
