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
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, staticFile, useCurrentFrame} from "remotion";
import {VOZ, asegurarFuentes} from "../../brand/copylab/sistema";
import {Grano} from "../../brand/copylab/lienzo";

const v = (n: string) => staticFile(`assets/gcl/cap02/bloque2/${n}`);
const hoja = (n: string) => staticFile(`assets/gcl/cap02/hojas/${n}`);

const Clip: React.FC<{src: string; desdeS?: number; escala?: number}> = ({src, desdeS = 0, escala = 1}) => (
  <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
    <OffthreadVideo src={v(src)} startFrom={Math.round(desdeS * 30)} muted
      style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover", transform: `scale(${escala})`}} />
  </AbsoluteFill>
);

/** Una placa (arte de hoja) pegada sobre el plano con una transformación
 *  plana: posición, tamaño, rotación y un poco de perspectiva. Las coordenadas
 *  se miden sobre el frame del clip; se afinan mirando el render. */
export const Placa: React.FC<{src: string; x: number; y: number; w: number; rot?: number; op?: number; persp?: string}> = ({src, x, y, w, rot = 0, op = 1, persp}) => (
  <div style={{position: "absolute", left: x, top: y, width: w, transform: `${persp ?? ""} rotate(${rot}deg)`, transformOrigin: "top left", opacity: op, mixBlendMode: "multiply"}}>
    <Img src={hoja(src)} style={{width: "100%", display: "block"}} />
  </div>
);

/** El post-it, a mano, sobre el post-it rosado en blanco que generó el modelo. */
export const PostIt: React.FC<{texto: string; x: number; y: number; w: number; rot?: number; op: number}> = ({texto, x, y, w, rot = 0, op}) => (
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

/** INSERTO: la hoja a pantalla completa. Es la forma honesta de que el copy y el
 *  layout se LEAN en 2 s: un plano detalle de la hoja, no un arte pegado sobre un
 *  papel que se mueve. 12 frames cada uno. */
const Inserto: React.FC<{src: string; rot?: number}> = ({src, rot = -3}) => (
  <AbsoluteFill style={{backgroundColor: "#0b0d0e", justifyContent: "center", alignItems: "center"}}>
    <div style={{width: 940, transform: `rotate(${rot}deg)`, boxShadow: "0 30px 80px rgba(0,0,0,.7)"}}>
      <Img src={hoja(src)} style={{width: "100%", display: "block"}} />
    </div>
  </AbsoluteFill>
);

/** EL POST-IT, macro. El storyboard pedía rack focus al post-it; a 50 mm el papel
 *  mide 90 px y no se lee. Un inserto macro es el mismo gesto —acercarse a lo
 *  que él lee— y se lee. El post-it en la mano: pantalla completa, a mano. */
const PostItMacro: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: "#0b0d0e", justifyContent: "center", alignItems: "center"}}>
    <div style={{
      width: 760, height: 760, background: "linear-gradient(170deg,#ff5fa8 0%,#ff2d8d 55%,#e0207a 100%)",
      transform: "rotate(-6deg)", boxShadow: "0 40px 90px rgba(0,0,0,.75)",
      display: "flex", alignItems: "center", justifyContent: "center", padding: 60,
    }}>
      <div style={{fontFamily: VOZ.mano, fontSize: 168, lineHeight: 0.98, color: "#1a1418", textAlign: "center", transform: "rotate(2deg)"}}>
        es un<br />cambio<br />chico
      </div>
    </div>
  </AbsoluteFill>
);

export const Cap02Bloque2: React.FC = () => {
  asegurarFuentes();
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Audio src={staticFile("assets/gcl/cap02/bloque2_audio.wav")} />

      {/* SHOT 04 · EL POST-IT · f.0–71 · G llega, levanta la carpeta, despega el post-it y lo lee. «mm.» en el f.50 */}
      <Sequence from={0} durationInFrames={72}>
        <Clip src="s04_postit.mp4" desdeS={2.3} />   {/* levanta la carpeta a 2,5 s, el post-it frente al visor desde 4,2 */}
        {/* el texto aparece cuando el post-it queda frente al visor: se afina con el render */}
        {/* el inserto macro entra cuando el post-it queda frente al visor (f.52) y se queda hasta el corte: ahí cae el «mm.» */}
        <Sequence from={52} durationInFrames={20}><PostItMacro /></Sequence>
      </Sequence>

      {/* SHOT 05 · LA BANDEJA · f.72–137 · el copy con GRATIS encerrado; el guante lo toma; el layout no cabe; la tercera hoja tapa el lente */}
      <Sequence from={72} durationInFrames={66}>
        <Clip src="s05_bandeja.mp4" desdeS={2.0} />   {/* el guante entra a los 2,0 s, toma a los 3,5 */}
        {/* los dos insertos: el copy (GRATIS encerrado) y el layout (no cabe). 12 f cada uno */}
        <Sequence from={16} durationInFrames={12}><Inserto src="copy.png" rot={-4} /></Sequence>
        <Sequence from={44} durationInFrames={12}><Inserto src="layout.png" rot={3} /></Sequence>
      </Sequence>

      {/* SHOT 06 · DOS HOJAS · f.138–209 · el tap en el f.180; el cajón se abre solo · el contador en 0 */}
      <Sequence from={138} durationInFrames={72}>
        <Clip src="s06_doshojas.mp4" desdeS={1.6} />   {/* el tap a los 3,0 s = f.42 local */}
        <Contador valor={0} x={296} y={846} w={120} />
      </Sequence>

      {/* SHOT 07 · NUEVE · f.210–293 · las hojas llegan desde el norte y se abren en abanico; R.01 pasa con la regla */}
      <Sequence from={210} durationInFrames={84}>
        <Clip src="s07_nueve.mp4" desdeS={1.8} />   {/* las hojas llegan 2,0–3,8; R.01 con la regla pasa 4,0–4,6 */}
      </Sequence>

      <Grano op={0.05} />
      {f < 0 ? null : null}
    </AbsoluteFill>
  );
};
