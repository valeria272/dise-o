// ============================================================================
// REEL · ESPACIO FOOD SERVICE 2026 — «Del stand al reel» · v6 (01-10-2026)
// ----------------------------------------------------------------------------
// PEDIDO    Valeria: reel de Espacio Food Service con nuestro equipo de content,
//           que cubrió la feria para Traverso. v5 quedó «demasiado plano»: pidió
//           transiciones entretenidas, variar la tipografía (una más curvilínea) y
//           jugar con la edición.
// FEEDBACK  Jefa de diseño (v4): nada de recuadro rosado ni letra a mano, textos
//           centrados, nada de mono («muy IA»). Se respeta: la curva es la DM Serif
//           Display Italic —editorial, no manuscrita— y todo va centrado y sin cajas.
// MATERIAL  69 clips de Sebastián Serrano · cortes en ~/copylab-work/foodservice_raw/
//           (cortar.py: HLG→SDR, 1080×1920, al beat de «Pump It», 153,65 BPM). Las
//           tomas 07L/08L/09L son versiones largas para el tríptico.
// TRANSIC.  Hechas a medida, ninguna de plantilla (MOTION_PLAYBOOK prohíbe zoom-blur,
//           glitch de preset y whip-pan genérico):
//           · GOLPE: cada toma entra 12 % más cerca y se asienta en 6 f — el corte
//             pega con el bombo.
//           · TRÍPTICO: los tres planos de cocina entran en franjas, una cada 2 beats,
//             desde lados alternados, y quedan cocinando juntos.
//           · OBTURADOR: en «se graba.» la toma se congela y se vuelve foto impresa.
//           · IRIS: el cierre abre un círculo blanco desde el centro con el logo.
//           · FLASH de 2 f sólo en los cambios de capítulo, no en cada corte.
// TIPOS     Dos voces que alternan por línea: DM Serif Display Italic (la curva, el
//           tono) y Bebas Neue Pro SemiExpanded (lo que se tiene que leer). Cada línea
//           entra en su beat: la razón de la tipografía cinética es el ritmo.
// MÚSICA    conMusica → «Pump It» desde 18,312 s (SIN LICENCIA, decisión de Valeria).
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, Easing, Freeze, Img, OffthreadVideo, Sequence, interpolate,
        staticFile, useCurrentFrame} from "remotion";
import {C2, VOZ2, SOMBRA_SOBRE_FOTO, asegurarFuentesV2} from "../../brand/copylab/sistemaV2";

// [desde, frames] de cada toma — copiado de _cortes/cortes.json
const TOMAS: [number, number][] = [
  [0, 47], [47, 23], [70, 24], [94, 23], [117, 24], [141, 23], [164, 23], [187, 24], [211, 23], [234, 24], [258, 23], [281, 24], [305, 23], [328, 23], [351, 24], [375, 23], [398, 12], [410, 12], [422, 23], [445, 70],
];
const FPB = (60 / 153.65) * 30;          // frames por beat
const PLACA = 47;                        // 4 beats
const FIN_TOMAS = 515;
export const REEL_FOODSERVICE_FRAMES = FIN_TOMAS + PLACA;
const T = (i: number) => TOMAS[i][0];
const BLANCO = "#FFFFFF";
const clip = (nombre: string) => staticFile(`assets/foodservice-traverso/${nombre}.mp4`);
const fuente = (i: number) => clip(String(i).padStart(2, "0"));
const salida = Easing.out(Easing.cubic);
const fijo = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

// La curva no está en el motor 2609: se carga acá, sólo para esta pieza.
let curvaCargada = false;
const asegurarCurva = () => {
  if (curvaCargada || typeof document === "undefined") return;
  curvaCargada = true;
  const st = document.createElement("style");
  st.innerHTML = `@font-face{font-family:'FS Curva';src:url(${staticFile("assets/fonts/copywriters/DMSerifDisplay-Italic.ttf")}) format('truetype');font-display:block;}`;
  document.head.appendChild(st);
};
const CURVA = "'FS Curva', 'DM Serif Display', Georgia, serif";

// ---------------------------------------------------------------- piezas de edición
/** Toma a pantalla completa con GOLPE de entrada. */
const Toma: React.FC<{i: number}> = ({i}) => {
  const f = useCurrentFrame();
  const esc = interpolate(f, [0, 6], [1.12, 1], {...fijo, easing: salida});
  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      <OffthreadVideo src={fuente(i)} muted
        style={{width: "100%", height: "100%", objectFit: "cover", transform: `scale(${esc})`}} />
    </AbsoluteFill>
  );
};

/** Una franja del tríptico: entra deslizándose y su clip arranca cuando entra. */
const Franja: React.FC<{nombre: string; k: number}> = ({nombre, k}) => {
  const f = useCurrentFrame();
  const dx = interpolate(f, [0, 7], [k % 2 ? 1080 : -1080, 0], {...fijo, easing: salida});
  return (
    <div style={{position: "absolute", left: 0, top: k * 643, width: 1080, height: 634,
                 overflow: "hidden", transform: `translateX(${dx}px)`}}>
      <OffthreadVideo src={clip(nombre)} muted
        style={{position: "absolute", left: 0, top: -643, width: 1080, height: 1920, objectFit: "cover"}} />
    </div>
  );
};

/** TRÍPTICO: tres franjas que entran una cada 2 beats; f=0 es el inicio de la toma 7. */
const Triptico: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    {["07L", "08L", "09L"].map((nombre, k) => (
      <Sequence key={nombre} from={Math.round(k * 2 * FPB)}>
        <Franja nombre={nombre} k={k} />
      </Sequence>
    ))}
  </AbsoluteFill>
);

/** OBTURADOR: la toma 11 corre 9 f, flash, y se congela como foto impresa. */
const Foto: React.FC = () => {
  const f = useCurrentFrame();
  const CORTE = 9;
  const t = interpolate(f, [CORTE, CORTE + 7], [0, 1], {...fijo, easing: salida});
  const flash = interpolate(f, [CORTE, CORTE + 1, CORTE + 4], [0, 1, 0], fijo);
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      <AbsoluteFill style={{transform: `scale(${1 - 0.2 * t}) rotate(${-5 * t}deg)`}}>
        <div style={{position: "absolute", inset: 0, background: BLANCO, padding: 22 * t,
                     boxShadow: t > 0 ? "0 30px 80px rgba(0,0,0,0.6)" : undefined}}>
          <div style={{width: "100%", height: "100%", overflow: "hidden"}}>
            <Freeze frame={CORTE} active={f >= CORTE}>
              <OffthreadVideo src={fuente(11)} muted style={{width: "100%", height: "100%", objectFit: "cover"}} />
            </Freeze>
          </div>
        </div>
      </AbsoluteFill>
      <AbsoluteFill style={{background: BLANCO, opacity: flash}} />
    </AbsoluteFill>
  );
};

/** IRIS: círculo blanco que se abre desde el centro y deja la placa de Traverso. */
const Placa: React.FC = () => {
  const f = useCurrentFrame();
  const r = interpolate(f, [0, 9], [0, 1300], {...fijo, easing: salida});
  const op = interpolate(f, [6, 12], [0, 1], fijo);
  const esc = interpolate(f, [6, PLACA], [0.94, 1], fijo);
  return (
    <AbsoluteFill>
      <AbsoluteFill style={{background: BLANCO, clipPath: `circle(${r}px at 50% 50%)`}} />
      <AbsoluteFill style={{alignItems: "center", justifyContent: "center", opacity: op}}>
        <Img src={staticFile("assets/traverso/logo.png")} style={{width: 780, transform: `scale(${esc})`}} />
        <div style={{marginTop: 54, fontFamily: CURVA, fontSize: 64, color: C2.negro}}>en Espacio Food Service 2026</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const Flash: React.FC<{en: number}> = ({en}) => {
  const f = useCurrentFrame();
  const op = interpolate(f, [en - 1, en, en + 2], [0, 0.9, 0], fijo);
  return <AbsoluteFill style={{background: BLANCO, opacity: op, pointerEvents: "none"}} />;
};

// ---------------------------------------------------------------- tipografía cinética
type L = {t: string; voz: "curva" | "bebas"; cuerpo?: number; beat: number};
/** Un bloque de líneas centrado; la línea n entra en su beat (relativo a `desde`). */
const Frase: React.FC<{lineas: L[]; desde: number; hasta: number; y?: number}> = ({lineas, desde, hasta, y = 1040}) => {
  const f = useCurrentFrame();
  if (f < desde - 1 || f > hasta + 1) return null;
  const sale = interpolate(f, [hasta - 4, hasta], [1, 0], fijo);
  const tam = (l: L) => l.cuerpo ?? (l.voz === "bebas" ? 120 : 84);
  const alto = lineas.reduce((a, l) => a + tam(l), 0);
  return (
    <>
      <div style={{position: "absolute", left: 0, right: 0, top: y - 140, height: alto + 280, opacity: sale * 0.8,
                   background: "linear-gradient(180deg, rgba(11,11,11,0) 0%, rgba(11,11,11,0.6) 30%, rgba(11,11,11,0.6) 70%, rgba(11,11,11,0) 100%)"}} />
      <div style={{position: "absolute", left: 40, right: 40, top: y, textAlign: "center", opacity: sale}}>
        {lineas.map((l) => {
          const en = desde + Math.round(l.beat * FPB);
          const p = interpolate(f, [en, en + 6], [0, 1], {...fijo, easing: salida});
          const bebas = l.voz === "bebas";
          return (
            <div key={l.t} style={{
              whiteSpace: "nowrap", opacity: p, transform: `translateY(${(1 - p) * 40}px) scale(${0.85 + 0.15 * p})`,
              fontFamily: bebas ? VOZ2.impacto : CURVA, fontWeight: bebas ? 700 : 400,
              fontSize: tam(l), lineHeight: bebas ? 0.95 : 1.1, textTransform: bebas ? "uppercase" : "none",
              color: BLANCO, textShadow: SOMBRA_SOBRE_FOTO,
            }}>{l.t}</div>
          );
        })}
      </div>
    </>
  );
};

// ---------------------------------------------------------------- el reel
/** conMusica: la versión con «Pump It» bajado de YouTube, SIN LICENCIA. */
export const ReelFoodService: React.FC<{conMusica?: boolean}> = ({conMusica = false}) => {
  asegurarFuentesV2();
  asegurarCurva();
  const especial = (i: number) => i === 11 || (i >= 7 && i <= 9);
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      {TOMAS.map(([desde, n], i) => especial(i) ? null : (
        <Sequence key={i} from={desde} durationInFrames={n}><Toma i={i} /></Sequence>
      ))}
      <Sequence from={T(7)} durationInFrames={T(10) - T(7)}><Triptico /></Sequence>
      <Sequence from={T(11)} durationInFrames={TOMAS[11][1]}><Foto /></Sequence>

      {/* Flashes sólo en los cambios de capítulo */}
      {[T(4), T(10), T(19)].map((en) => <Flash key={en} en={en} />)}

      {/* INTRO — fuimos a cubrir Espacio Food Service con nuestro equipo de content */}
      <Frase desde={1} hasta={T(2)} lineas={[
        {t: "Fuimos a cubrir", voz: "curva", beat: 0},
        {t: "Espacio", voz: "bebas", beat: 1},
        {t: "Food Service", voz: "bebas", beat: 2},
        {t: "con nuestro equipo de content", voz: "curva", cuerpo: 66, beat: 3},
      ]} />
      {/* para nuestro cliente Traverso y enterarnos de todo lo nuevo */}
      <Frase desde={T(2) + 1} hasta={T(6) - 1} lineas={[
        {t: "para nuestro cliente", voz: "curva", beat: 0},
        {t: "Traverso", voz: "bebas", cuerpo: 170, beat: 1},
        {t: "y enterarnos de todo lo nuevo", voz: "curva", cuerpo: 66, beat: 3},
      ]} />
      {/* «lo que se cocina,» sobre el tríptico · «se graba.» sobre la foto */}
      <Frase desde={T(7) + 2} hasta={T(10) - 1} y={830} lineas={[
        {t: "lo que se cocina,", voz: "curva", cuerpo: 96, beat: 0},
      ]} />
      <Frase desde={T(10) + 1} hasta={T(12) - 1} y={1500} lineas={[
        {t: "se graba.", voz: "bebas", cuerpo: 150, beat: 0},
      ]} />
      {/* Cierre */}
      <Frase desde={T(19) + 4} hasta={FIN_TOMAS} y={980} lineas={[
        {t: "del stand", voz: "curva", cuerpo: 110, beat: 0},
        {t: "al reel.", voz: "bebas", cuerpo: 190, beat: 1},
      ]} />

      <Sequence from={FIN_TOMAS} durationInFrames={PLACA}><Placa /></Sequence>

      {conMusica && (
        <Audio src={staticFile("assets/foodservice-traverso/temp-pumpit-SIN-LICENCIA.wav")}
               startFrom={Math.round(18.312 * 30)}
               volume={(fr) => interpolate(fr, [0, 3, REEL_FOODSERVICE_FRAMES - 14, REEL_FOODSERVICE_FRAMES],
                                           [0, 0.7, 0.7, 0], fijo)} />
      )}
    </AbsoluteFill>
  );
};
