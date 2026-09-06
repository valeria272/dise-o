// ============================================================================
// G.C.L. / CAP.02 — «ES UN CAMBIO CHICO» · BLOQUE 1 · SHOTS 01–03
// 144 frames · 4,8 s · 30 fps · 1080×1920 · storyboard V1.6 FINAL (story lock)
// ----------------------------------------------------------------------------
// El bloque de prueba del capítulo. Acá se decide si el reel funciona: hook,
// identidad, continuidad, velocidad de corte, actuación de G, Marta, R.01, el
// Server, luz, cámara, sonido, transiciones. Si esto no engancha, lo demás no
// importa.
//
// LO QUE ESTE BLOQUE PRUEBA, plano por plano (V1.6):
//   01  EL TUBO        f.0–20    MF-08 · la carpeta cae a la canasta · cut on impact
//   02  LA RONDA       f.21–77   cuatro fijos con whips en montaje:
//         02a Marta    f.21–35   LCD LISTA → AY. · la primera hoja · whip →
//         02b Server   f.36–50   la ámbar se APAGA · el ticker se borra · whip ↓
//         02c R.01     f.51–62   frena en seco · el mástil azota · tilt ↑
//         02d G        f.63–77   la taza en la boca · la baja · «eh?»
//   03  EL ÚNICO...    f.78–143  MF-01 · smash cut · G se levanta y camina · entra la música
//
// PRODUCCIÓN: cada estación es su propio clip (kling con image_tail), los whips
// son whip-out / whip-in en Remotion (traslación + blur), el LCD y el ticker se
// componen acá. NUNCA se genera texto legible.
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, OffthreadVideo, Sequence, staticFile, useCurrentFrame} from "remotion";
import {VOZ, asegurarFuentes} from "../../brand/copylab/sistema";
import {Grano} from "../../brand/copylab/lienzo";

const v = (n: string) => staticFile(`assets/gcl/cap02/bloque1/${n}`);

// ── Un clip recortado, encajado por alto ─────────────────────────────────────
const Clip: React.FC<{src: string; desdeS?: number; escala?: number}> = ({src, desdeS = 0, escala = 1}) => (
  <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
    <OffthreadVideo src={v(src)} startFrom={Math.round(desdeS * 30)} muted
      style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover", transform: `scale(${escala})`}} />
  </AbsoluteFill>
);

// ── EL WHIP ──────────────────────────────────────────────────────────────────
// La RONDA se diseñó como un plano con tres whips y se produce como cuatro
// fijos. El whip es lo que los vuelve UN plano: los últimos `n` frames de una
// estación se van (whip-out) en una dirección y los primeros `n` de la
// siguiente llegan (whip-in) desde la opuesta, con blur. 3 frames bastan: el
// ojo completa el movimiento. Más de 4 y se ve el truco.
//
// ⚠️ Lección del primer render (05-09): con Sequences que se suceden sin
// solaparse, en los 3 frames del whip el cuadro saliente ya se fue y el
// entrante todavía no llega → NEGRO. Un whip no es un corte a negro: es dos
// cuadros emborronados que se cruzan. Por eso cada estación dura 3 frames MÁS
// que su lugar en el timeline (su whip-out se solapa con el whip-in de la
// siguiente), y el desplazamiento es del 70 % del ancho, no del 100 %: así
// los dos se ven pasar.
type Dir = "der" | "izq" | "abajo" | "arriba";
const VEC: Record<Dir, [number, number]> = {der: [1, 0], izq: [-1, 0], abajo: [0, 1], arriba: [0, -1]};

const Whip: React.FC<{
  dur: number; salida?: Dir; entrada?: Dir; n?: number; children: React.ReactNode;
}> = ({dur, salida, entrada, n = 3, children}) => {
  const f = useCurrentFrame();
  let tx = 0, ty = 0, blur = 0;
  if (entrada && f < n) {
    const p = 1 - f / n;                                  // 1 → 0
    const [x, y] = VEC[entrada];
    tx = -x * p * 760; ty = -y * p * 1340; blur = p * 32;
  }
  if (salida && f >= dur - n) {
    const p = (f - (dur - n) + 1) / n;                     // 0 → 1
    const [x, y] = VEC[salida];
    tx = x * p * 760; ty = y * p * 1340; blur = p * 32;
  }
  return (
    // Sin fondo negro propio: durante el solape tiene que verse el cuadro de abajo.
    <AbsoluteFill style={{overflow: "hidden"}}>
      <AbsoluteFill style={{transform: `translate(${tx}px, ${ty}px)`, filter: blur ? `blur(${blur}px)` : undefined}}>
        {children}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ── EL LCD DE MARTA ──────────────────────────────────────────────────────────
// Dos líneas verdes sobre negro, en la posición del LCD del MF-04. Es como
// habla Marta cuando no imprime. `LISTA` → `AY.` en el f.28 absoluto (7 de 02a).
const LCD: React.FC<{linea1: string; linea2?: string; caja: {x: number; y: number; w: number; h: number; rot?: number}}> = ({linea1, linea2 = "", caja}) => (
  <div style={{
    position: "absolute", left: caja.x, top: caja.y, width: caja.w, height: caja.h,
    transform: `rotate(${caja.rot ?? 0}deg)`, fontFamily: VOZ.data, color: "#B8F5A0",
    background: "rgba(10,30,8,0.55)", textShadow: "0 0 6px #7CFF5A", padding: "4px 8px",
    fontSize: caja.h * 0.36, lineHeight: 1.15, letterSpacing: 1, overflow: "hidden",
  }}>
    <div>{linea1}</div><div>{linea2}</div>
  </div>
);

// ── EL BLOQUE ────────────────────────────────────────────────────────────────
export const Cap02Bloque1: React.FC = () => {
  asegurarFuentes();
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Audio src={staticFile("assets/gcl/cap02/bloque1_audio.wav")} />

      {/* SHOT 01 · EL TUBO · negro 4 f, después la carpeta cae. Cut on impact. */}
      <Sequence from={0} durationInFrames={21}>
        <Clip src="s01_tubo.mp4" desdeS={2.15} />   {/* la carpeta asoma a los 2,3 s y cae a los 2,9: sale del tubo en el f.6, impacto en el f.19 */}
        {f < 4 ? <AbsoluteFill style={{backgroundColor: "#000"}} /> : null}
      </Sequence>

      {/* 02a · MARTA · f.21–35 · LISTA → AY. y la primera hoja · whip-out a la derecha */}
      <Sequence from={21} durationInFrames={18}>
        <Whip dur={18} salida="der">
          <Clip src="s02a_marta.mp4" desdeS={3.6} />   {/* la hoja sube 3,6–4,1 s */}
          <LCD linea1={f - 21 < 7 ? "LISTA" : "AY."} caja={{x: 250, y: 640, w: 170, h: 62}} />
        </Whip>
      </Sequence>

      {/* 02b · SERVER · f.36–50 · la ámbar se apaga, el ticker se borra · whip-in desde la izquierda, whip-out abajo */}
      <Sequence from={36} durationInFrames={18}>
        <Whip dur={18} entrada="izq" salida="abajo">
          <Clip src="s02b_server.mp4" desdeS={3.55} />  {/* la ámbar se apaga a los 3,8 s: 7 frames encendida, 8 apagada */}
        </Whip>
      </Sequence>

      {/* 02c · R.01 · f.51–62 · frena en seco, el mástil azota · whip-in desde arriba, tilt-up al final */}
      <Sequence from={51} durationInFrames={15}>
        <Whip dur={15} entrada="arriba" salida="arriba">
          <Clip src="s02c_r01.mp4" desdeS={1.95} />   {/* frena a los 2,1 s, el mástil azota 2,2–2,4 */}
        </Whip>
      </Sequence>

      {/* 02d · G · f.63–77 · la taza en la boca, la baja, «eh?» · whip-in desde abajo (viene del tilt) */}
      <Sequence from={63} durationInFrames={15}>
        <Whip dur={15} entrada="abajo">
          <Clip src="s02d_g.mp4" desdeS={1.9} />   {/* baja la taza 1,9–2,4 s. ⚠️ kling metió un push-in lento: en 15 frames casi no se nota, pero es polish pendiente */}
        </Whip>
      </Sequence>

      {/* SHOT 03 · EL ÚNICO QUE CAMINA · f.78–143 · smash cut al wide. Entra la música. */}
      <Sequence from={78} durationInFrames={66}>
        <Clip src="s03_wide.mp4" desdeS={2.2} />   {/* se para a los 2,3 s y camina hacia cámara-izquierda hasta los 4,4 */}
      </Sequence>

      <Grano op={0.05} />
    </AbsoluteFill>
  );
};
