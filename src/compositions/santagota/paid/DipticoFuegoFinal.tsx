/**
 * SANTA GOTA · E1 de pauta «Uno para el fuego. Otro para el final.» — 4:5 (1080×1350) y 9:16 (1080×1920). 01-10-2026.
 *
 * Etapa «entender»: dos aceites distintos, cada uno con su trabajo (nunca «dos tamaños»).
 * Producto EN MANOS REALES de la jornada del 10-09, sin recortes (DSC00197 · DSC00227);
 * fotos: scripts/santagota-e1-fotos.py. Capa dibujada: la misma del carrusel «Elige tu pecado».
 * Precio del Pack Squeeze leído de santagota.cl/products.json el 01-10-2026.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {LIMA, Titular, Subrayado, Precio, mano} from "./CarruselPecado";

const DIR = "assets/santagota/e1";
const pie: React.CSSProperties = {...mano, position: "absolute", color: "#fff", textShadow: "0 3px 12px rgba(30,0,5,0.55)", whiteSpace: "nowrap"};

/** Costura a mano entre las dos mitades. */
const Costura: React.FC<{vertical: boolean; largo: number; en: number}> = ({vertical, largo, en}) => {
  const n = 12;
  const pts = Array.from({length: n + 1}, (_, i) => {
    const t = (i / n) * largo;
    const o = (i % 2 ? 5 : -5) + (i % 3 ? 2 : -2);
    return vertical ? `${en + o},${t}` : `${t},${en + o}`;
  }).join(" ");
  return (
    <svg style={{position: "absolute", inset: 0, overflow: "visible"}} width={1080} height={vertical ? largo : 1920}>
      <polyline points={pts} fill="none" stroke="#fff" strokeWidth={7} strokeLinejoin="round" strokeLinecap="round" />
    </svg>
  );
};

export const DipticoFeed: React.FC = () => (
  <AbsoluteFill>
    <Img src={staticFile(`${DIR}/fuego-45.jpg`)} style={{position: "absolute", left: 0, top: 0, width: 540, height: 1350}} />
    <Img src={staticFile(`${DIR}/final-45.jpg`)} style={{position: "absolute", left: 540, top: 0, width: 540, height: 1350}} />
    <Costura vertical largo={1350} en={540} />

    <Titular x={56} y={96} size={70} rot={-6} lineas={[{t: "UNO PARA EL", c: "#fff"}]} />
    <Titular x={60} y={150} size={150} rot={-6} lineas={[{t: "FUEGO.", c: LIMA}]} />
    <Titular x={590} y={96} size={70} rot={-4} lineas={[{t: "OTRO PARA EL", c: "#fff"}]} />
    <Titular x={600} y={150} size={150} rot={-4} lineas={[{t: "FINAL.", c: LIMA}]} />

    <Precio x={430} y={330} d={220} arriba="los dos" precio="$18.990" rot={-6} />

    <div style={{...pie, left: 280, top: 1090, fontSize: 32, transform: "rotate(-4deg)", textAlign: "right", width: 220}}>
      750 ml<br />cocinar y saltear
    </div>
    <div style={{...pie, left: 580, top: 1090, fontSize: 32, transform: "rotate(3deg)"}}>
      500 ml<br />aderezar y terminar
    </div>
  </AbsoluteFill>
);

export const DipticoStory: React.FC = () => (
  <AbsoluteFill>
    <Img src={staticFile(`${DIR}/fuego-916.jpg`)} style={{position: "absolute", left: 0, top: 0, width: 1080, height: 960}} />
    <Img src={staticFile(`${DIR}/final-916.jpg`)} style={{position: "absolute", left: 0, top: 960, width: 1080, height: 960}} />
    <Costura vertical={false} largo={1080} en={960} />

    <Titular x={575} y={300} size={74} rot={-6} lineas={[{t: "UNO PARA EL", c: "#fff"}]} />
    <Titular x={585} y={360} size={160} rot={-6} lineas={[{t: "FUEGO.", c: LIMA}]} />
    <Subrayado x={595} y={540} w={330} rot={-6} />
    <div style={{...pie, left: 610, top: 600, fontSize: 34, transform: "rotate(-5deg)"}}>750 ml · cocinar y saltear</div>

    <Titular x={60} y={1010} size={74} rot={-4} lineas={[{t: "OTRO PARA EL", c: "#fff"}]} />
    <Titular x={70} y={1070} size={160} rot={-4} lineas={[{t: "FINAL.", c: LIMA}]} />
    <div style={{...pie, left: 690, top: 1470, fontSize: 36, transform: "rotate(3deg)", textAlign: "right", width: 330}}>
      500 ml<br />aderezar y terminar
    </div>

    <Precio x={790} y={830} d={230} arriba="los dos" precio="$18.990" rot={8} />
  </AbsoluteFill>
);
