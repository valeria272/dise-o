/**
 * QB · ST 20-10 · 11:00 · ESTÁTICA — ALL YOU CAN DRINK «CONTESTA LA LLAMADA»
 *
 * BRIEF (STORIES col. P, OK PARA DISEÑAR, sin comentario):
 *   Construir la pieza como si fuera una llamada entrante en el celular. En
 *   primer plano 2 o 3 tragos sostenidos por manos, estética nocturna, flash
 *   directo, mood party / salida. De fondo ambiente QB desenfocado, luces
 *   cálidas, reflejos.
 *   Texto: CONTESTA LA LLAMADA… · ALL YOU CAN DRINK · Tragos seleccionados por
 *   $13.990 · MARTES · 18:00 A 21:00 HRS · legal.
 *
 * REFERENCIA: Pinterest 900579256750204422 («Dancefloor calling») — manos
 * brindando con los botones verde/rojo de una llamada entrante.
 *
 * DIRECCIÓN DE ARTE
 *   · Foto REAL: manos con dos tragos de noche en la terraza (sesión de Víctor,
 *     C4216 t=1,5 s), look flash en código.
 *   · La interfaz de llamada: «llamada entrante…» arriba, el que llama es ALL YOU
 *     CAN DRINK —con su nombre y cortes del KV, que no varían— y los dos botones
 *     redondos abajo. Son íconos genéricos, no una captura de iOS.
 *   · ⭐ El precio va en el botón verde con degradado del KV (Eli: no varía).
 *   · PROMO → zona segura de paid.
 */
import React from "react";
import {AbsoluteFill} from "remotion";

import {BloqueAycd, cargarFuentesQbOct, FotoQB, Legal, Linea, LogoQB, MESA, NombreAycd, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST20_DATA: Record<string, Record<string, string>> = {
  pieza: {
  antetitulo: "CONTESTA LA LLAMADA…",
  titular: "ALL YOU CAN DRINK",
  etiqueta: "POR $13.990",
  medida: "MARTES · 18:00 A 21:00 HRS",
  texto: "TRAGOS SELECCIONADOS",
  legal: "Sujeto a consumo de alimentos. Promoción no acumulable con otras ofertas y beneficios.",
  },
};

const Tel: React.FC<{color: string; colgar?: boolean; x: number; top: number; etiqueta: string}> = ({
  color, colgar = false, x, top, etiqueta,
}) => (
  <>
    <div style={{position: "absolute", top, left: x - 60, width: 120, height: 120, borderRadius: 120,
      background: color, display: "flex", alignItems: "center", justifyContent: "center",
      boxShadow: "0 8px 30px rgba(0,0,0,.45)"}}>
      <svg width={58} height={58} viewBox="0 0 24 24" style={{transform: colgar ? "rotate(135deg)" : "none"}}>
        <path fill="#fff" d="M6.6 10.8a15.1 15.1 0 006.6 6.6l2.2-2.2a1 1 0 011-.25 11.4 11.4 0 003.6.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.4 11.4 0 00.57 3.6 1 1 0 01-.25 1z" />
      </svg>
    </div>
    <div style={{position: "absolute", top: top + 132, left: x - 110, width: 220, textAlign: "center",
      color: "#fff", fontFamily: "Raleway", fontSize: 24, fontWeight: 500}}>{etiqueta}</div>
  </>
);

export const QbSt20AycdLlamada: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/20-aycd-llamada.jpg" ratio={2250 / 4000} zoom={1.08} cx={0.45} cy={0.42} />
    <Velo arriba={[860, 0.92]} abajo={[800, 0.95]} />
    <LogoQB top={252} ancho={140} />
    <Linea top={360} cuerpo={30} peso={500} tracking="0.18em" color="rgba(255,255,255,.85)">llamada entrante</Linea>
    <Linea top={404} cuerpo={48} peso={300} tracking="0.05em">{QB_ST20_DATA.pieza.antetitulo}</Linea>
    <NombreAycd top={488} cuerpo={98} />
    <Tel color="#E0413B" colgar x={MESA.w / 2 - 250} top={1075} etiqueta="Rechazar" />
    <Tel color="#66886B" x={MESA.w / 2 + 250} top={1075} etiqueta="Aceptar" />
    <BloqueAycd antetitulo={1290} boton={1340} horario={1450}
      textoAntetitulo={QB_ST20_DATA.pieza.texto} textoHorario={QB_ST20_DATA.pieza.medida} />
    <Legal top={1530} cuerpo={17}>{QB_ST20_DATA.pieza.legal}</Legal>
  </AbsoluteFill>
);
