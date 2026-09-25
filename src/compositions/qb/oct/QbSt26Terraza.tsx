/**
 * QB · ST REEL 26-10 · 13:00 · ANIMADA — DISFRUTA LAS TARDES EN NUESTRA TERRAZA
 *
 * BRIEF (STORIES col. W, OK PARA DISEÑAR, sin comentario):
 *   Una st vertical con distintos momentos de una tarde en la terraza de QB,
 *   estética espontánea, cálida y social: registro real de una salida.
 *   E1 terraza con gente — ¿PLAN PARA ESTA TARDE?
 *   E2 cocktails llegando a la mesa — EMPIEZA CON ALGO PARA BRINDAR.
 *   E3 platos al centro, manos compartiendo — SIGUE CON ALGO RICO PARA COMPARTIR.
 *   E4 amigos conversando, riendo — Y QUÉDATE POR EL AMBIENTE.
 *   E5 brindis grupal con la terraza de fondo — LAS TARDES SE DISFRUTAN EN LA
 *      TERRAZA DE QB. · RESERVA TU MESA
 *
 * REFERENCIA: IG DNt2ZRYYj3b (reel) — ⚠️ NO DISPONIBLE: Instagram responde que el
 * enlace es incorrecto o la publicación se borró (24-09). Se sigue el brief.
 *
 * DIRECCIÓN DE ARTE
 *   · TODO REAL. ⭐ Rehecha el 25-09-2026 con la carpeta «videos / CAM» que pasó
 *     Eli: Sony 4K 60p en S-Log3, grabada la TARDE del 10-10-2025 en la terraza
 *     (luz de día que se va, los edificios detrás). S-Log3→Rec.709 con la LUT de
 *     `slog3-a-709.py`; proxies en `scripts/qb-oct-proxies.py`. Sin IA → sin
 *     «Imagen referencial».
 *     E1 8526 invitados en la mesa larga · E2 8586 el trago servido · E3 8516
 *     manos y platos · E4 8574 amigos riendo · E5 8536 pareja brindando
 *   · ⛔ Eli 25-09: en la primera versión salían trabajadores del hotel (8519,
 *     el brindis con dos ejecutivos) — descartado. Sólo invitados en cuadro.
 *   · Un clip por escena, fundido corto entre ellas; el texto de cada escena entra
 *     subiendo y se va con el clip. Todo centrado, dos pesos de Raleway.
 *   · Orgánica. Sin punto en los textos (regla Hilton §F).
 */
import React from "react";
import {AbsoluteFill, interpolate, OffthreadVideo, Sequence, staticFile, useCurrentFrame, Easing} from "remotion";

import {BotonVerde, cargarFuentesQbOct, Linea, LogoQB, Velo} from "./QbOctKit";

cargarFuentesQbOct();

export const QB_ST26_FPS = 30;
const ESCENA = 100;   // 3,33 s
const FUNDIDO = 12;
export const QB_ST26_DURACION = ESCENA * 5 - FUNDIDO * 4 + 30; // + remate

export const QB_ST26_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "¿PLAN PARA ESTA TARDE?",
  texto: "EMPIEZA CON ALGO PARA BRINDAR",
  frase: "SIGUE CON ALGO RICO PARA COMPARTIR",
  bajada: "Y QUÉDATE POR EL AMBIENTE",
  pie: "LAS TARDES SE DISFRUTAN EN LA TERRAZA DE QB",
  cta: "RESERVA TU MESA",
  },
};

const ESCENAS: {clip: string; l1: string; l2?: string}[] = [
  {clip: "t1-terraza", l1: "¿PLAN PARA", l2: "ESTA TARDE?"},
  {clip: "t2-tragos", l1: "EMPIEZA CON ALGO", l2: "PARA BRINDAR"},
  {clip: "t3-compartir", l1: "SIGUE CON ALGO RICO", l2: "PARA COMPARTIR"},
  {clip: "t4-risas", l1: "Y QUÉDATE", l2: "POR EL AMBIENTE"},
  {clip: "t5-brindis", l1: "LAS TARDES SE DISFRUTAN", l2: "EN LA TERRAZA DE"},
];

const Escena: React.FC<{i: number; dur: number}> = ({i, dur}) => {
  const f = useCurrentFrame();
  const e = ESCENAS[i];
  const entrada = i === 0 ? 1 : interpolate(f, [0, FUNDIDO], [0, 1], {extrapolateRight: "clamp"});
  const t = interpolate(f, [6, 22], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic)});
  const ultima = i === ESCENAS.length - 1;
  return (
    <AbsoluteFill style={{opacity: entrada}}>
      <OffthreadVideo src={staticFile(`assets/hilton/qb/oct/clips/${e.clip}.mp4`)} muted
        style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover"}} />
      <Velo arriba={[520, 0.7]} abajo={ultima ? [1150, 0.95] : [900, 0.9]} />
      <div style={{position: "absolute", inset: 0, opacity: t, transform: `translateY(${(1 - t) * 26}px)`}}>
        <Linea top={ultima ? 1180 : 1330} cuerpo={60} peso={300} tracking="0.05em">{e.l1}</Linea>
        {e.l2 && <Linea top={(ultima ? 1180 : 1330) + 70} cuerpo={60} peso={800} tracking="0.02em">{e.l2}</Linea>}
      </div>
      {ultima && <Remate f={f} />}
    </AbsoluteFill>
  );
};

const Remate: React.FC<{f: number}> = ({f}) => {
  const t = interpolate(f, [26, 44], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <div style={{opacity: t}}>
      <LogoQB top={1332} ancho={200} />
      <BotonVerde top={1480} ancho={460} alto={84} cuerpo={36} peso={800}>RESERVA TU MESA</BotonVerde>
    </div>
  );
};

export const QbSt26Terraza: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    {ESCENAS.map((_, i) => {
      const desde = i * (ESCENA - FUNDIDO);
      const dur = i === ESCENAS.length - 1 ? QB_ST26_DURACION - desde : ESCENA;
      return (
        <Sequence key={i} from={desde} durationInFrames={dur}>
          <Escena i={i} dur={dur} />
        </Sequence>
      );
    })}
    <LogoQB top={250} ancho={130} />
  </AbsoluteFill>
);
