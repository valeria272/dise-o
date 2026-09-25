/**
 * QB · ST 22-10 · ANIMADA — ENSALADA DE CAMARÓN PANKO
 *
 * BRIEF (STORIES col. S, OK PARA DISEÑAR):
 *   Tomar como referencia el reel adjunto, propuesta íntima, cercana y sensorial.
 *   La Ensalada de camarón panko en primer plano sobre la mesa, estética cálida y
 *   gastronómica. Una persona comiendo sólo a través de la mano y los cubiertos.
 *   E1 plano cerrado del plato — OPCIONES FRESCAS PARA TU ALMUERZO
 *   E2 la mano entra con el tenedor — ENSALADA DE CAMARÓN PANKO
 *   E3 detalle de los ingredientes — FRESCA, CRUJIENTE Y LLENA DE SABOR
 *   E4 el tenedor toma un bocado — UNA COMBINACIÓN HECHA PARA DISFRUTAR.
 *      DESCÚBRELA EN NUESTRA CARTA
 *
 * ⭐ COMENTARIO DEL CLIENTE: «Lo haría anclado a la recomendación del chef
 * (misma línea gráfica) añadir Imagen referencial abajo, contemplar esto para
 * todo material que no sea real».
 *   ⇒ La pieza toma la línea del KV «Recomendación del chef» (ST n°1 S4 JUL CHEF
 *     QB): «RECOMENDACIÓN / DEL CHEF» en Bell MT versales, textos en Raleway
 *     bold versales, recuadro fino para el cierre, el plato abajo.
 *   ⇒ «*Imagen referencial» fijo al pie.
 *
 * REFERENCIA: IG arubabonbini DYYlzztgEFM — plato cálido con vela, una mano con
 * tenedor, muy cerca.
 *
 * DIRECCIÓN DE ARTE
 *   · No hay foto real del plato (Eli, 24-09: «genérala con IA»). El plato es de
 *     Seedream 5 Pro, con los ingredientes del brief.
 *   · ⚠️ EL MOVIMIENTO DE LA MANO QUEDÓ PENDIENTE: los clips de Kling (mano con
 *     tenedor) fallaron y la API de Magnific se quedó sin créditos el 24-09. Esta
 *     versión anima la foto con movimientos de cámara (acercamiento, paneo,
 *     detalle). Cuando haya créditos: `python scripts/qb-oct-clips.py`.
 *   · Encuadre sin `transform: scale()`: FotoQB cambia el tamaño real (§4e).
 *   · Orgánica.
 */
import React from "react";
import {AbsoluteFill, Easing, interpolate, Sequence, useCurrentFrame} from "remotion";

import {cargarFuentesQbOct, FotoQB, ImagenReferencial, Linea, LogoQB, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

export const QB_ST22_FPS = 30;
const E = 96;
const F = 12;
export const QB_ST22_DURACION = E * 4 - F * 3 + 36;

export const QB_ST22_DATA: Record<string, Record<string, string>> = {
  pieza: {
  antetitulo: "RECOMENDACIÓN DEL CHEF",
  titular: "OPCIONES FRESCAS PARA TU ALMUERZO",
  nombre: "ENSALADA DE CAMARÓN PANKO",
  texto: "FRESCA, CRUJIENTE Y LLENA DE SABOR",
  frase: "UNA COMBINACIÓN HECHA PARA DISFRUTAR",
  cta: "DESCÚBRELA EN NUESTRA CARTA",
  },
};

type Plano = {src: string; ratio: number; z: [number, number]; cx: [number, number]; cy: [number, number];
  l1: string; l2?: string};
const PLANOS: Plano[] = [
  {src: "22-ensalada", ratio: 2250 / 4050, z: [1.0, 1.12], cx: [0.5, 0.5], cy: [0.55, 0.6],
    l1: "OPCIONES FRESCAS", l2: "PARA TU ALMUERZO"},
  {src: "22-ensalada", ratio: 2250 / 4050, z: [1.3, 1.42], cx: [0.42, 0.56], cy: [0.62, 0.6],
    l1: "ENSALADA DE", l2: "CAMARÓN PANKO"},
  {src: "22-ensalada-detalle", ratio: 2250 / 4000, z: [1.0, 1.1], cx: [0.5, 0.5], cy: [0.48, 0.44],
    l1: "FRESCA, CRUJIENTE", l2: "Y LLENA DE SABOR"},
  {src: "22-ensalada-detalle", ratio: 2250 / 4000, z: [1.12, 1.28], cx: [0.46, 0.5], cy: [0.55, 0.58],
    l1: "UNA COMBINACIÓN", l2: "HECHA PARA DISFRUTAR"},
];

const Escena: React.FC<{i: number; dur: number}> = ({i, dur}) => {
  const f = useCurrentFrame();
  const p = PLANOS[i];
  const k = interpolate(f, [0, dur], [0, 1], {extrapolateRight: "clamp", easing: Easing.inOut(Easing.sin)});
  const lerp = (a: [number, number]) => a[0] + (a[1] - a[0]) * k;
  const entrada = i === 0 ? 1 : interpolate(f, [0, F], [0, 1], {extrapolateRight: "clamp"});
  const t = interpolate(f, [8, 24], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic)});
  const ultima = i === PLANOS.length - 1;
  const tc = interpolate(f, [40, 58], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{opacity: entrada}}>
      <FotoQB src={`assets/hilton/qb/oct/${p.src}.jpg`} ratio={p.ratio} zoom={lerp(p.z)} cx={lerp(p.cx)} cy={lerp(p.cy)} />
      <Velo arriba={[760, 0.95]} abajo={[760, 0.95]} />
      <div style={{position: "absolute", inset: 0, opacity: t, transform: `translateY(${(1 - t) * 24}px)`}}>
        <Linea top={ultima ? 1300 : 1390} cuerpo={50} peso={800} tracking="0.03em">{p.l1}</Linea>
        {p.l2 && <Linea top={(ultima ? 1300 : 1390) + 60} cuerpo={50} peso={800} tracking="0.03em">{p.l2}</Linea>}
      </div>
      {ultima && (
        <div style={{position: "absolute", top: 1444, left: (MESA.w - 700) / 2, width: 700, height: 96,
          border: "2px solid rgba(255,255,255,.9)", background: "rgba(0,0,0,.35)", display: "flex",
          alignItems: "center", justifyContent: "center", color: "#fff", fontFamily: "Raleway",
          fontWeight: 700, fontSize: 38, letterSpacing: "0.03em", opacity: tc}}>
          DESCÚBRELA EN NUESTRA CARTA
        </div>
      )}
    </AbsoluteFill>
  );
};

export const QbSt22Ensalada: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    {PLANOS.map((_, i) => {
      const desde = i * (E - F);
      const dur = i === PLANOS.length - 1 ? QB_ST22_DURACION - desde : E;
      return (
        <Sequence key={i} from={desde} durationInFrames={dur}>
          <Escena i={i} dur={dur} />
        </Sequence>
      );
    })}
    {/* La línea del chef: fija en toda la pieza */}
    <LogoQB top={250} ancho={150} />
    <Linea top={372} cuerpo={82} familia="BellMT" interlinea={1}>RECOMENDACIÓN</Linea>
    <Linea top={454} cuerpo={112} familia="BellMT" interlinea={1}>DEL CHEF</Linea>
    <ImagenReferencial top={1556} />
  </AbsoluteFill>
);
