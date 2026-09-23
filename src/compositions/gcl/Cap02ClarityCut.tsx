// ============================================================================
// G.C.L. / CAP.02 — «ES UN CAMBIO CHICO» · CLARITY CUT V2
// 1454 frames · 48,5 s · 30 fps · 1080×1920 · STORY LOCK V1.6 · 06-09-2026
// ----------------------------------------------------------------------------
// Pasada de CLARIDAD + RITMO + LEGIBILIDAD + CONTINUIDAD + COMEDIA sobre el
// FULL ROUGH V1, con el material ya producido. Diagnóstico de la V1: nosotros
// entendíamos más que el espectador; los cambios pasaban en 0,4 s y nada decía
// qué era cada consecuencia. La V2:
//
//   · da 1,2–1,5 s a cada texto que hay que leer (post-it, copy, layout,
//     formatos, «una cosita más», «NO.»);
//   · le pone SELLO a cada consecuencia (hojas v2_*.png): COPY → DISEÑO →
//     FORMATOS ×9 → VIDEO → LANDING → PAUTA → PRESENTACIÓN. Primero tres
//     claras (1,2–1,4 s), después el resto en 0,7–0,8 s: ya se entendió la regla;
//   · recupera el tiempo de lo redundante (wide, misión de R.01, caos, sube,
//     calma) y se lo da a la información. 3,3 s más corta que la V1;
//   · el sonido puntúa: clic → COPY · ping → DISEÑO · trrr → FORMATOS ·
//     hum+ticker → VIDEO · sello en cada hoja · muere a muestra cero en la carpeta.
//
// CANON: ningún plano nuevo. Todo es reedición, recorte, hold, inserto y post.
// El G del 04 (más alto) se recorta a lo mínimo indispensable (52 f) y se marca
// como pendiente #1 para el MASTER.
//
//   01–02  0–71     hook (igual)          LANDING 647–670 · 10   671–736
//   03     72–119   wide (−18 f)          PAUTA   737–760 · 10b  761–808
//   04     120–216  post-it (macro 45 f)  10c     809–853 · ráfaga 854–889
//   05     217–324  copy 42 f · layout 36 PRESENTACIÓN 890–913 · 11 914–1003
//   06     325–384  tap → cajón           12      1004–1081 · 13 1082–1201
//   07     385–480  nueve · formatos 36 f 14      1202–1279 · 15 1280–1357
//   08     481–546  R.01 trabado          16      1358–1393 · firma 1394–1453
//   09     547–646  G · cielo · ticker VIDEO
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from "remotion";
import {VOZ, ancho, asegurarFuentes} from "../../brand/copylab/sistema";
import {Grano} from "../../brand/copylab/lienzo";

const b1 = (n: string) => staticFile(`assets/gcl/cap02/bloque1/${n}`);
const b2 = (n: string) => staticFile(`assets/gcl/cap02/bloque2/${n}`);
const b3 = (n: string) => staticFile(`assets/gcl/cap02/bloque3/${n}`);
const hoja = (n: string) => staticFile(`assets/gcl/cap02/hojas/${n}`);
const ROSA = "#FF2D8D";

const Clip: React.FC<{src: string; desdeS?: number; escala?: number; origen?: string}> = ({src, desdeS = 0, escala = 1, origen = "50% 50%"}) => (
  <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
    <OffthreadVideo src={src} startFrom={Math.round(desdeS * 30)} muted
      style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover", transform: `scale(${escala})`, transformOrigin: origen}} />
  </AbsoluteFill>
);

const Fija: React.FC<{src: string}> = ({src}) => (
  <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
    <Img src={src} style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover"}} />
  </AbsoluteFill>
);

/** El LCD de Marta (bloque 1). */
const LCD: React.FC<{linea1: string; caja: {x: number; y: number; w: number; h: number}}> = ({linea1, caja}) => (
  <div style={{position: "absolute", left: caja.x, top: caja.y, width: caja.w, height: caja.h, fontFamily: VOZ.data, color: "#B8F5A0",
    background: "rgba(10,30,8,0.55)", textShadow: "0 0 6px #7CFF5A", padding: "4px 8px", fontSize: caja.h * 0.36, lineHeight: 1.15, letterSpacing: 1, overflow: "hidden"}}>
    <div>{linea1}</div>
  </div>
);

/** El ticker del Server sobre la placa del nicho (coordenadas del MF-06). */
const Ticker: React.FC<{texto: string}> = ({texto}) => (
  <div style={{position: "absolute", left: 300, top: 486, width: 480, height: 40, fontFamily: VOZ.data, fontSize: 28, letterSpacing: 3, color: "#FF9A3C",
    textShadow: "0 0 10px #FF7A1A, 0 0 2px #fff", background: "rgba(20,8,0,.55)", textAlign: "center", lineHeight: "40px", overflow: "hidden", whiteSpace: "nowrap"}}>
    {texto}
  </div>
);

const LuzCable: React.FC<{p: number}> = ({p}) => {
  const x = interpolate(p, [0, 1], [540, 720]); const y = interpolate(p, [0, 1], [1700, 260]);
  return <div style={{position: "absolute", left: x - 24, top: y - 24, width: 48, height: 48, borderRadius: "50%",
    background: `radial-gradient(circle, #FFE9C9 0%, ${ROSA}AA 35%, transparent 70%)`, filter: "blur(4px)", opacity: p < 0.02 || p > 0.98 ? 0 : 1}} />;
};

const Contador: React.FC<{valor: number; x: number; y: number; w: number}> = ({valor, x, y, w}) => (
  <div style={{position: "absolute", left: x, top: y, width: w, fontFamily: VOZ.data, color: "#1c2024"}}>
    <div style={{background: "#e8e6df", padding: `${w * 0.05}px ${w * 0.06}px`, fontSize: w * 0.075, letterSpacing: 1, lineHeight: 1.15, textAlign: "center", boxShadow: "0 2px 6px rgba(0,0,0,.5)"}}>DÍAS SIN UN<br />CAMBIO CHICO</div>
    <div style={{display: "flex", justifyContent: "center", gap: w * 0.03, marginTop: w * 0.05}}>
      {String(valor).padStart(3, "0").split("").map((d, i) => (
        <div key={i} style={{background: "#111", color: "#f2f2ea", fontSize: w * 0.18, width: w * 0.2, textAlign: "center", lineHeight: 1.25, borderRadius: 3}}>{d}</div>
      ))}
    </div>
  </div>
);

/** INSERTO: la hoja a pantalla completa. En la V2 entra con un golpe de sello
 *  (2 f de escala 1,04 → 1) para que el ojo vaya al sello, y se queda quieta. */
const Inserto: React.FC<{src: string; rot?: number}> = ({src, rot = -3}) => {
  const f = useCurrentFrame();
  const s = interpolate(f, [0, 3], [1.05, 1], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{backgroundColor: "#0b0d0e", justifyContent: "center", alignItems: "center"}}>
      <div style={{width: 940, transform: `rotate(${rot}deg) scale(${s})`, boxShadow: "0 30px 80px rgba(0,0,0,.7)"}}>
        <Img src={hoja(src)} style={{width: "100%", display: "block"}} />
      </div>
    </AbsoluteFill>
  );
};

const PostItMacro: React.FC<{texto: React.ReactNode}> = ({texto}) => (
  <AbsoluteFill style={{backgroundColor: "#0b0d0e", justifyContent: "center", alignItems: "center"}}>
    <div style={{width: 760, height: 760, background: "linear-gradient(170deg,#ff5fa8 0%,#ff2d8d 55%,#e0207a 100%)", transform: "rotate(-6deg)", boxShadow: "0 40px 90px rgba(0,0,0,.75)", display: "flex", alignItems: "center", justifyContent: "center", padding: 60}}>
      <div style={{fontFamily: VOZ.mano, fontSize: 168, lineHeight: 0.98, color: "#1a1418", textAlign: "center", transform: "rotate(2deg)"}}>{texto}</div>
    </div>
  </AbsoluteFill>
);

const Visor: React.FC<{x: number; y: number; r: number; delta: number}> = ({x, y, r, delta}) => (
  <div style={{position: "absolute", left: x - r, top: y - r, width: r * 2, height: r * 2, borderRadius: "50%",
    background: "radial-gradient(circle, rgba(0,0,0,.45) 0%, transparent 70%)", opacity: Math.abs(delta), mixBlendMode: "multiply"}} />
);

const Firma: React.FC = () => {
  const f = useCurrentFrame();
  const l = (n: number) => interpolate(f, [n, n + 8], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{backgroundColor: "#080F14", justifyContent: "center", alignItems: "center"}}>
      <div style={{textAlign: "center", fontFamily: VOZ.data, color: "#F2F4F6", letterSpacing: 6}}>
        <div style={{fontFamily: VOZ.impacto, fontVariationSettings: ancho(78, 900), fontSize: 72, letterSpacing: 2, opacity: l(4)}}>G.C.L.</div>
        <div style={{fontSize: 22, marginTop: 22, opacity: l(16)}}>DEPARTAMENTO DE COSAS IMPOSIBLES</div>
        <div style={{fontSize: 18, marginTop: 30, opacity: l(28), color: "#98A2AD"}}>COPYWRITERS</div>
      </div>
    </AbsoluteFill>
  );
};

export const V2_FRAMES = 1454;

export const Cap02ClarityCut: React.FC = () => {
  asegurarFuentes();
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Audio src={staticFile("assets/gcl/cap02/v2_audio.wav")} />

      {/* ═══ INTRIGA · 0–71 · el hook aprobado, intacto ═══════════════════ */}
      <Sequence from={0} durationInFrames={21}>
        <Clip src={b1("s01_tubo.mp4")} desdeS={1.7} />
        {f < 4 ? <AbsoluteFill style={{backgroundColor: "#000"}} /> : null}
      </Sequence>
      <Sequence from={21} durationInFrames={12}>
        <Clip src={b1("s02a_marta.mp4")} desdeS={3.6} />
        <LCD linea1={f - 21 < 6 ? "LISTA" : "AY."} caja={{x: 250, y: 640, w: 170, h: 62}} />
      </Sequence>
      <Sequence from={33} durationInFrames={12}><Clip src={b1("s02b_server.mp4")} desdeS={3.62} /></Sequence>
      <Sequence from={45} durationInFrames={12}><Clip src={b1("s02c_r01.mp4")} desdeS={1.95} /></Sequence>
      <Sequence from={57} durationInFrames={15}><Clip src={b1("s02d_g.mp4")} desdeS={2.0} /></Sequence>

      {/* 03 · 72–119 · el único que camina · 48 f (V1: 66). El establishing ya cumplió a los 1,6 s */}
      <Sequence from={72} durationInFrames={48}><Clip src={b1("s03_wide.mp4")} desdeS={2.2} /></Sequence>

      {/* ═══ REVELACIÓN · 04 · 120–216 · «es un cambio chico» 1,5 s (V1: 0,67 s) ═══ */}
      <Sequence from={120} durationInFrames={52}><Clip src={b2("s04_postit.mp4")} desdeS={2.3} /></Sequence>
      <Sequence from={172} durationInFrames={45}><PostItMacro texto={<>es un<br />cambio<br />chico</>} /></Sequence>

      {/* ═══ CONSECUENCIA 1 · COPY · 217–288 · la bandeja → la hoja 1,4 s (V1: 0,4 s) ═══ */}
      <Sequence from={217} durationInFrames={18}><Clip src={b2("s05_bandeja.mp4")} desdeS={2.0} /></Sequence>
      <Sequence from={235} durationInFrames={42}><Inserto src="v2_copy.png" rot={-4} /></Sequence>
      <Sequence from={277} durationInFrames={12}><Clip src={b2("s05_bandeja.mp4")} desdeS={3.3} /></Sequence>   {/* el guante toma la segunda */}
      {/* ═══ CONSECUENCIA 2 · DISEÑO · 289–324 · no cabe · 1,2 s ═══ */}
      <Sequence from={289} durationInFrames={36}><Inserto src="v2_layout.png" rot={3} /></Sequence>

      {/* 06 · 325–384 · G arregla (tap, f.367) → un cajón se abre solo (368) · contador 000 */}
      <Sequence from={325} durationInFrames={60}>
        <Clip src={b2("s06_doshojas.mp4")} desdeS={1.6} />
        <Contador valor={0} x={296} y={846} w={120} />
      </Sequence>

      {/* ═══ CONSECUENCIA 3 · FORMATOS ×9 · 385–480 · llegan las nueve → la hoja 1,2 s → R.01 con la regla ═══ */}
      <Sequence from={385} durationInFrames={48}><Clip src={b2("s07_nueve.mp4")} desdeS={1.8} /></Sequence>
      <Sequence from={433} durationInFrames={36}><Inserto src="v2_formatos.png" rot={-2} /></Sequence>
      <Sequence from={469} durationInFrames={12}><Clip src={b2("s07_nueve.mp4")} desdeS={4.0} /></Sequence>

      {/* ═══ ACELERACIÓN · 08 · 481–546 · R.01 trabado contra la caja · 2,2 s (V1: 3,4) ═══ */}
      <Sequence from={481} durationInFrames={66}><Clip src={b3("s08_r01_regla.mp4")} desdeS={2.6} /></Sequence>

      {/* ═══ CONSECUENCIA 4 · VIDEO · 547–646 · G «mm.» + tap → la luz por el cable → el ticker 1,3 s ═══ */}
      <Sequence from={547} durationInFrames={36}><Clip src={b3("s09_g_pantallas.mp4")} desdeS={1.9} /></Sequence>
      <Sequence from={583} durationInFrames={24}>
        <Fija src={b3("MF-cielo.jpg")} />
        <LuzCable p={(f - 583) / 24} />
      </Sequence>
      <Sequence from={607} durationInFrames={40}>
        <Clip src={b3("s09_ticker.mp4")} desdeS={2.5} />
        <Ticker texto={`VIDEO · RENDER ${Math.min(9, Math.floor((f - 607) / 4))}/9`} />
      </Sequence>

      {/* ═══ CONSECUENCIA 5 · LANDING · 647–666 (0,8 s: la regla ya se entendió) → 10 · 667–736 · medio Nivel -1 ═══ */}
      <Sequence from={647} durationInFrames={24}><Inserto src="v2_landing.png" rot={2} /></Sequence>
      <Sequence from={671} durationInFrames={66}><Clip src={b3("s10_caos.mp4")} desdeS={0.9} /></Sequence>

      {/* ═══ CONSECUENCIA 6 · PAUTA · 737–756 → 10b · 757–808 · un kilómetro · el tirón en el 799 ═══ */}
      <Sequence from={737} durationInFrames={24}><Inserto src="v2_pauta.png" rot={-3} /></Sequence>
      <Sequence from={761} durationInFrames={48}><Clip src={b3("s10b_kilometro.mp4")} desdeS={2.5} /></Sequence>   {/* el tirón a los 3,77 s = f.799 */}

      {/* 10c · 809–853 · el que baja y se va · ida 30 f + vuelta 15 f (el mismo clip al revés) */}
      <Sequence from={809} durationInFrames={30}><Clip src={b3("s10c_piernas.mp4")} desdeS={1.3} escala={2} origen="50% 100%" /></Sequence>
      <Sequence from={839} durationInFrames={15}><Clip src={b3("s10c_piernas_rev.mp4")} desdeS={2.73} escala={2} origen="50% 100%" /></Sequence>

      {/* ═══ SATURACIÓN · ráfaga · 854–889 · hoja · R.01 · RENDER OK ═══ */}
      <Sequence from={854} durationInFrames={12}><Clip src={b2("s05_bandeja.mp4")} desdeS={2.75} /></Sequence>
      <Sequence from={866} durationInFrames={12}><Clip src={b3("s10b_kilometro.mp4")} desdeS={1.2} escala={1.25} /></Sequence>
      <Sequence from={878} durationInFrames={12}>
        <Clip src={b3("s09_ticker.mp4")} desdeS={2.5} />
        <Ticker texto={f - 878 < 6 ? "VIDEO · RENDER 9/9" : "VIDEO · OK"} />
      </Sequence>

      {/* ═══ CONSECUENCIA 7 · PRESENTACIÓN · 890–913 → 11 · la carpeta · 914–1003 · el golpe en el 1001 ═══ */}
      <Sequence from={890} durationInFrames={24}><Inserto src="v2_presentacion.png" rot={-2} /></Sequence>
      <Sequence from={914} durationInFrames={90}><Clip src={b3("s11_carpeta.mp4")} desdeS={1.6} /></Sequence>

      {/* ═══ RESOLUCIÓN · 12 · sube · 1004–1081 · 2,6 s (V1: 4,0) ═══ */}
      <Sequence from={1004} durationInFrames={78}><Clip src={b3("s12_sube.mp4")} desdeS={2.2} /></Sequence>

      {/* ═══ SILENCIO · CAFÉ · 13 · 1082–1201 · 4,0 s (V1: 5,0) · el contador pasa a 1 en el 1152 ═══ */}
      <Sequence from={1082} durationInFrames={120}>
        <Sequence from={0} durationInFrames={18}><Clip src={b3("s13_calma.mp4")} desdeS={0} /></Sequence>
        <Sequence from={18}><Fija src={b3("s13_hold.jpg")} /></Sequence>
        <Contador valor={f < 1152 ? 0 : 1} x={868} y={708} w={56} />
      </Sequence>

      {/* ═══ 14 · 1202–1279 · tsh-TUNK · «una cosita más…» 1,6 s ═══ */}
      <Sequence from={1202} durationInFrames={78}>
        <Clip src={b1("s01_tubo.mp4")} desdeS={1.7} />
        <Sequence from={30} durationInFrames={48}><PostItMacro texto={<>una<br />cosita<br />más…</>} /></Sequence>
      </Sequence>

      {/* ═══ 15 · 1280–1357 · Marta, un rodillo · NO. 1,4 s ═══ */}
      <Sequence from={1280} durationInFrames={78}>
        <Clip src={b3("s15_no.mp4")} desdeS={2.6} />
        <Sequence from={36} durationInFrames={42}><Inserto src="NO.png" rot={-2} /></Sequence>
      </Sequence>

      {/* ═══ 16 · 1358–1393 · G · micro reacción (visor −15 %) · contador 000 ═══ */}
      <Sequence from={1358} durationInFrames={36}>
        <Fija src={b3("S16_G.jpg")} />
        <Contador valor={0} x={296} y={846} w={120} />
        <Visor x={540} y={905} r={170} delta={f - 1358 >= 14 && f - 1358 < 26 ? -0.15 : 0} />
      </Sequence>

      <Sequence from={1394} durationInFrames={60}><Firma /></Sequence>
      <Grano op={0.05} />
    </AbsoluteFill>
  );
};
