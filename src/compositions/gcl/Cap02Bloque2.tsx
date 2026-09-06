// ============================================================================
// G.C.L. / CAP.02 — «ES UN CAMBIO CHICO» · BLOQUE 2 · SHOTS 04–07
// 294 frames · 9,8 s · 0:04,8 – 0:14,6 del capítulo · storyboard V1.6 (story lock)
// ----------------------------------------------------------------------------
// El setup y el nivel 1: el post-it («mm.»), la bandeja de Marta con el copy ya
// marcado, las dos hojas en el escritorio y el tap, y las nueve sobre la mesa.
//
//   04  EL POST-IT     f.0–71     NA-1 · G llega, levanta, lee. Música a cero. «mm.»
//   05  LA BANDEJA     f.72–137   MA-04 · el copy con GRATIS encerrado · el layout que no cabe
//   06  DOS HOJAS      f.138–209  MA-02 · un tap, un cajón se abre solo · el contador en 0
//   07  NUEVE          f.210–293  MA-05 · nueve hojas llegan · R.01 con la regla
//
// TODO LO QUE SE LEE ES POST: el post-it, el contenido de las hojas (copy.png,
// layout.png, f_*.png de scripts/cap02-hojas.py), el contador. Las hojas se
// generan en blanco y el arte se pega encima, deformado a la perspectiva.
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from "remotion";
import {VOZ, asegurarFuentes} from "../../brand/copylab/sistema";
import {Grano} from "../../brand/copylab/lienzo";

const v = (n: string) => staticFile(`assets/gcl/cap02/bloque2/${n}`);
const hoja = (n: string) => staticFile(`assets/gcl/cap02/hojas/${n}`);
const ROSA = "#FF2D8D";

const Clip: React.FC<{src: string; desdeS?: number; escala?: number}> = ({src, desdeS = 0, escala = 1}) => (
  <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
    <OffthreadVideo src={v(src)} startFrom={Math.round(desdeS * 30)} muted
      style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover", transform: `scale(${escala})`}} />
  </AbsoluteFill>
);

/** Una placa (arte de hoja) pegada sobre el plano con una transformación
 *  plana: posición, tamaño, rotación y un poco de perspectiva. Las coordenadas
 *  se miden sobre el frame del clip; se afinan mirando el render. */
const Placa: React.FC<{src: string; x: number; y: number; w: number; rot?: number; op?: number; persp?: string}> = ({src, x, y, w, rot = 0, op = 1, persp}) => (
  <div style={{position: "absolute", left: x, top: y, width: w, transform: `${persp ?? ""} rotate(${rot}deg)`, transformOrigin: "top left", opacity: op, mixBlendMode: "multiply"}}>
    <Img src={hoja(src)} style={{width: "100%", display: "block"}} />
  </div>
);

/** El post-it, a mano, sobre el post-it rosado en blanco que generó el modelo. */
const PostIt: React.FC<{texto: string; x: number; y: number; w: number; rot?: number; op: number}> = ({texto, x, y, w, rot = 0, op}) => (
  <div style={{
    position: "absolute", left: x, top: y, width: w, transform: `rotate(${rot}deg)`, transformOrigin: "center",
    fontFamily: VOZ.mano, fontSize: w * 0.19, lineHeight: 1.05, color: "#1a1418", textAlign: "center", opacity: op,
    textShadow: "0 0 1px rgba(0,0,0,.3)",
  }}>
    {texto}
  </div>
);

/** El cartel del pilar: DÍAS SIN UN CAMBIO CHICO y el contador de fichas. */
const Contador: React.FC<{valor: number; x: number; y: number; w: number}> = ({valor, x, y, w}) => (
  <div style={{position: "absolute", left: x, top: y, width: w, fontFamily: VOZ.data, color: "#1c2024"}}>
    <div style={{background: "#e8e6df", padding: `${w * 0.05}px ${w * 0.06}px`, fontSize: w * 0.075, letterSpacing: 1, lineHeight: 1.15, textAlign: "center", boxShadow: "0 2px 6px rgba(0,0,0,.5)"}}>
      DÍAS SIN UN<br />CAMBIO CHICO
    </div>
    <div style={{display: "flex", justifyContent: "center", gap: w * 0.03, marginTop: w * 0.05}}>
      {String(valor).padStart(3, "0").split("").map((d, i) => (
        <div key={i} style={{background: "#111", color: "#f2f2ea", fontSize: w * 0.18, width: w * 0.2, textAlign: "center", lineHeight: 1.25, borderRadius: 3, boxShadow: "inset 0 -2px 0 rgba(255,255,255,.08)"}}>{d}</div>
      ))}
    </div>
  </div>
);

export const Cap02Bloque2: React.FC = () => {
  asegurarFuentes();
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Audio src={staticFile("assets/gcl/cap02/bloque2_audio.wav")} />

      {/* SHOT 04 · EL POST-IT · f.0–71 · G llega, levanta la carpeta, despega el post-it y lo lee. «mm.» en el f.50 */}
      <Sequence from={0} durationInFrames={72}>
        <Clip src="s04_postit.mp4" desdeS={0} />
        {/* el texto aparece cuando el post-it queda frente al visor: se afina con el render */}
        <PostIt texto={"ES UN\nCAMBIO\nCHICO"} x={0} y={0} w={0} op={0} />
      </Sequence>

      {/* SHOT 05 · LA BANDEJA · f.72–137 · el copy con GRATIS encerrado; el guante lo toma; el layout no cabe; la tercera hoja tapa el lente */}
      <Sequence from={72} durationInFrames={66}>
        <Clip src="s05_bandeja.mp4" desdeS={0} />
      </Sequence>

      {/* SHOT 06 · DOS HOJAS · f.138–209 · el tap en el f.180; el cajón se abre solo · el contador en 0 */}
      <Sequence from={138} durationInFrames={72}>
        <Clip src="s06_doshojas.mp4" desdeS={0} />
        <Contador valor={0} x={0} y={0} w={0} />
      </Sequence>

      {/* SHOT 07 · NUEVE · f.210–293 · las hojas llegan desde el norte y se abren en abanico; R.01 pasa con la regla */}
      <Sequence from={210} durationInFrames={84}>
        <Clip src="s07_nueve.mp4" desdeS={0} />
      </Sequence>

      <Grano op={0.05} />
      {f < 0 ? null : null}
    </AbsoluteFill>
  );
};
