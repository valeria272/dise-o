/**
 * QB · ST 07-10 · 16:00 · ESTÁTICA — CUMPLEAÑOS EN QB  (ST n°3 S1)
 *
 * BRIEF (grilla octubre, STORIES col. E, OK PARA DISEÑAR desde el 28-09 tarde):
 *   Collage de 3 momentos de una celebración con cortes orgánicos y dibujos a
 *   mano. Texto: «Convierte tu cumpleaños en una noche inolvidable» · «5 tragos
 *   de cortesía para el cumpleañero/a» · «Shots de regalo · Postre · Cuenta
 *   separadas · Puedes traer tu propia torta». Interacción: ARMA EL GRUPO Y
 *   RESERVA AHORA (link reserva mesas).
 * COMENTARIO DEL CLIENTE: «veamos opción más simple, siendo una story mostraría
 *   la información más importante de inmediato» (R-43) → sin collage.
 *
 * DIRECCIÓN DE ARTE
 *   · UNA foto a sangre: la torta con bengalas llegando a la mesa (generada, no
 *     hay cumpleaños en las sesiones) → «Imagen referencial».
 *   · La información va ARRIBA y de inmediato.
 *   · ⭐ RONDA 10 (Eli 28-09): «no me gusta la tipografía: usa la Bell para
 *     "convierte tu cumpleaños" y Raleway en "una noche inolvidable"; el "5 tragos
 *     de cortesía" que tenga un ícono igual que la referencia, y lo mismo para
 *     shots de regalo, postre, cuenta separada y puedes traer tu propia torta; la
 *     torta está un poco feíta: añádele detalles verdes como de QB».
 *     → Titular en Bell MT + bajada en Raleway fina. Cada beneficio en su línea con
 *     un ÍCONO DE LÍNEA fino delante, como la ubicación y el teléfono de la ref
 *     «CHEERS». Torta reeditada: cinta verde QB, flores de azúcar verde salvia,
 *     servilleta verde.
 *   · ⭐ RONDA 11 (Eli 28-09): «las tortas tienen decoraciones extrañas, que se vea
 *     una torta bonita de cumpleaños» → torta reeditada: blanca lisa, perlas, cinta
 *     verde QB y ramitas finas arriba. «"Convierte tu cumpleaños" en mayúscula y
 *     "tu cumpleaños" abajo» → CONVIERTE / TU CUMPLEAÑOS en Bell MT. «Los íconos en
 *     recuadros oscurecidos, estilo botones» → cada beneficio es un recuadro negro
 *     translúcido con el ícono y el texto.
 *   · Aire abajo para el sticker del link («ARMA EL GRUPO Y RESERVA AHORA»).
 *   · «Cuenta separadas» va literal del brief (concordancia consultada a contenido).
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {cargarFuentesQbOct, CIFRAS, FotoQB, ImagenReferencial, Linea, LogoQB, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST07_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "CONVIERTE TU CUMPLEAÑOS",
  bajada: "en una noche inolvidable",
  beneficio: "5 tragos de cortesía para el cumpleañero/a",
  resto: "Shots de regalo · Postre · Cuenta separadas · Puedes traer tu propia torta",
  },
};

// ───────────────────────────────────────────────────────────────────────────
// Íconos de línea (trazo 2,2 sobre caja de 44): el registro de los íconos de
// ubicación y teléfono de la ref — finos, sin relleno.
// ───────────────────────────────────────────────────────────────────────────
const T = {fill: "none", stroke: "#fff", strokeWidth: 2.2, strokeLinecap: "round" as const, strokeLinejoin: "round" as const};
const ICONOS: Record<string, React.ReactNode> = {
  copa: <><path d="M9 8 H35 L22 23 Z" {...T} /><path d="M22 23 V37 M15 37 H29" {...T} /><path d="M29 8 L34 3" {...T} /></>,
  shot: <><path d="M13 8 H31 L28 37 H16 Z" {...T} /><path d="M14.3 19 H29.7" {...T} /></>,
  postre: <><path d="M10 21 H34 L30 37 H14 Z" {...T} /><path d="M10 21 C10 10 34 10 34 21" {...T} /><circle cx="22" cy="8" r="2.6" {...T} /></>,
  cuenta: <><path d="M12 5 H32 V38 L28.7 35.5 L25.3 38 L22 35.5 L18.7 38 L15.3 35.5 L12 38 Z" {...T} /><path d="M17 13 H27 M17 19 H27 M17 25 H24" {...T} /></>,
  torta: <><path d="M8 24 H36 V38 H8 Z" {...T} /><path d="M8 30 C12 33 16 27 22 30 C28 33 32 27 36 30" {...T} /><path d="M15 24 V17 M22 24 V15 M29 24 V17" {...T} /><path d="M15 12.5 V13 M22 10.5 V11 M29 12.5 V13" {...T} strokeWidth={3.4} /></>,
};

const Item: React.FC<{top: number; icono: string; children: React.ReactNode; fuerte?: boolean}> = ({
  top, icono, children, fuerte = false,
}) => (
  <div style={{position: "absolute", top, left: 120, width: 840, height: 68, boxSizing: "border-box",
    display: "flex", alignItems: "center", gap: 20, padding: "0 26px", borderRadius: 12,
    background: "rgba(8,10,9,.62)", border: "1px solid rgba(255,255,255,.14)",
    color: "#fff", fontFamily: "Raleway", fontWeight: fuerte ? 700 : 500, fontSize: fuerte ? 30 : 29, ...CIFRAS}}>
    <svg width={42} height={42} viewBox="0 0 44 44" style={{flex: "none"}}>
      {ICONOS[icono]}
    </svg>
    <span>{children}</span>
  </div>
);

export const QbSt07Cumple: React.FC = () => {
  const d = QB_ST07_DATA.pieza;
  const [r1, r2, r3, r4] = d.resto.split(" · ");
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoQB src="assets/hilton/qb/oct/07-cumple-torta-verde.jpg" ratio={1770 / 2360} cx={0.5} />
      <Velo arriba={[1100, 0.85]} abajo={[520, 0.8]} />
      <LogoQB top={250} ancho={160} />
      <Linea top={372} cuerpo={70} familia="BellMT" tracking="0.02em" interlinea={1.02}>
        CONVIERTE<br />TU CUMPLEAÑOS
      </Linea>
      <Linea top={528} cuerpo={48} peso={300} tracking="0.01em">{d.bajada}</Linea>
      <Item top={622} icono="copa" fuerte>{d.beneficio}</Item>
      <Item top={702} icono="shot">{r1}</Item>
      <Item top={782} icono="postre">{r2}</Item>
      <Item top={862} icono="cuenta">{r3}</Item>
      <Item top={942} icono="torta">{r4}</Item>
      <ImagenReferencial top={1556} />
    </AbsoluteFill>
  );
};
