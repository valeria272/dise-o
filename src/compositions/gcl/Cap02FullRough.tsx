// ============================================================================
// G.C.L. / CAP.02 — «ES UN CAMBIO CHICO» · FULL ROUGH V1
// 1554 frames · 51,8 s · 30 fps · 1080×1920 · STORY LOCK V1.6 · night run 05-09
// ----------------------------------------------------------------------------
// El capítulo entero, de principio a firma. Bloques 1 y 2 tal como se aprobaron
// (hook V2 con hard cuts = 138 f, así que desde el SHOT 04 todo va 6 frames
// antes que en el storyboard). Un solo audio para todo: full_audio.wav.
//
//   01–03   0–137      bloque 1 (V2)            10c    864–917    el que baja y se va
//   04–07   138–431    bloque 2                 ráfaga 918–953    tres consecuencias
//   08      432–533    la misión de R.01        11     954–1043   la carpeta
//   09      534–641    el cable                 12     1044–1163  sube
//   10      642–773    medio Nivel -1           13     1164–1313  calma
//   10b     774–863    un kilómetro             14–16  1314–1493  una cosita más · NO. · G
//                                               firma  1494–1553
//
// Donde una generación rompió canon y no se pudo arreglar en 2 intentos va un
// STILL canon con la marca PLACEHOLDER — CANON FAILURE (sólo en la versión
// ROUGH; la CLEAN no lleva marcas). Prioridad: canon > historia > continuidad.
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from "remotion";
import {VOZ, ancho, asegurarFuentes} from "../../brand/copylab/sistema";
import {Grano} from "../../brand/copylab/lienzo";
import {Cap02Bloque1} from "./Cap02Bloque1";
import {Cap02Bloque2} from "./Cap02Bloque2";

const v = (n: string) => staticFile(`assets/gcl/cap02/bloque3/${n}`);
const hoja = (n: string) => staticFile(`assets/gcl/cap02/hojas/${n}`);
const ROSA = "#FF2D8D";

const Clip: React.FC<{src: string; desdeS?: number; escala?: number; op?: number}> = ({src, desdeS = 0, escala = 1, op = 1}) => (
  <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden", opacity: op}}>
    <OffthreadVideo src={v(src)} startFrom={Math.round(desdeS * 30)} muted
      style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover", transform: `scale(${escala})`}} />
  </AbsoluteFill>
);

const Fija: React.FC<{src: string; escala?: number; placeholder?: boolean; marcas: boolean}> = ({src, escala = 1, placeholder, marcas}) => (
  <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
    <Img src={v(src)} style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover", transform: `scale(${escala})`}} />
    {placeholder && marcas ? (
      <div style={{position: "absolute", left: 40, top: 40, padding: "10px 16px", background: ROSA, color: "#080F14", fontFamily: VOZ.data, fontSize: 26, letterSpacing: 2}}>
        PLACEHOLDER — CANON FAILURE
      </div>
    ) : null}
  </AbsoluteFill>
);

/** El ticker del Server: una línea de matriz de puntos rojo-ámbar sobre la
 *  placa negra del nicho. Coordenadas medidas sobre el MF-06. */
const Ticker: React.FC<{texto: string; op?: number}> = ({texto, op = 1}) => (
  <div style={{
    position: "absolute", left: 300, top: 486, width: 480, height: 40, opacity: op,
    fontFamily: VOZ.data, fontSize: 30, letterSpacing: 4, color: "#FF9A3C", textShadow: "0 0 10px #FF7A1A, 0 0 2px #fff",
    background: "rgba(20,8,0,.55)", textAlign: "center", lineHeight: "40px", overflow: "hidden", whiteSpace: "nowrap",
  }}>
    {texto}
  </div>
);

/** La luz que corre por el cable (Post, sobre el still del cielo). */
const LuzCable: React.FC<{p: number}> = ({p}) => {
  const x = interpolate(p, [0, 1], [540, 720]);
  const y = interpolate(p, [0, 1], [1700, 260]);
  return (
    <div style={{position: "absolute", left: x - 24, top: y - 24, width: 48, height: 48, borderRadius: "50%",
      background: `radial-gradient(circle, #FFE9C9 0%, ${ROSA}AA 35%, transparent 70%)`, filter: "blur(4px)", opacity: p < 0.02 || p > 0.98 ? 0 : 1}} />
  );
};

/** El contador del pilar — mismo componente que en el bloque 2. */
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

/** Insertos de lectura (mismo lenguaje que el bloque 2). */
const Inserto: React.FC<{src: string; rot?: number}> = ({src, rot = -3}) => (
  <AbsoluteFill style={{backgroundColor: "#0b0d0e", justifyContent: "center", alignItems: "center"}}>
    <div style={{width: 940, transform: `rotate(${rot}deg)`, boxShadow: "0 30px 80px rgba(0,0,0,.7)"}}>
      <Img src={hoja(src)} style={{width: "100%", display: "block"}} />
    </div>
  </AbsoluteFill>
);

const PostItMacro: React.FC<{texto: React.ReactNode}> = ({texto}) => (
  <AbsoluteFill style={{backgroundColor: "#0b0d0e", justifyContent: "center", alignItems: "center"}}>
    <div style={{width: 760, height: 760, background: "linear-gradient(170deg,#ff5fa8 0%,#ff2d8d 55%,#e0207a 100%)", transform: "rotate(-6deg)", boxShadow: "0 40px 90px rgba(0,0,0,.75)", display: "flex", alignItems: "center", justifyContent: "center", padding: 60}}>
      <div style={{fontFamily: VOZ.mano, fontSize: 168, lineHeight: 0.98, color: "#1a1418", textAlign: "center", transform: "rotate(2deg)"}}>{texto}</div>
    </div>
  </AbsoluteFill>
);

/** El ±15 % del visor: una máscara de luminancia sobre la G, como en el prototipo. */
const Visor: React.FC<{x: number; y: number; r: number; delta: number}> = ({x, y, r, delta}) => (
  <div style={{position: "absolute", left: x - r, top: y - r, width: r * 2, height: r * 2, borderRadius: "50%",
    background: delta > 0 ? `radial-gradient(circle, ${ROSA}66 0%, transparent 70%)` : "radial-gradient(circle, rgba(0,0,0,.45) 0%, transparent 70%)",
    opacity: Math.abs(delta), mixBlendMode: delta > 0 ? "screen" : "multiply"}} />
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

export const FULL_FRAMES = 1554;

export const Cap02FullRough: React.FC<{marcas?: boolean}> = ({marcas = true}) => {
  asegurarFuentes();
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Audio src={staticFile("assets/gcl/cap02/full_audio.wav")} />

      {/* ── BLOQUES 1 y 2 · aprobados · sin su audio propio ─────────────── */}
      <Sequence from={0} durationInFrames={138}><Cap02Bloque1 audio={null} /></Sequence>
      <Sequence from={138} durationInFrames={294}><Cap02Bloque2 audio={null} /></Sequence>

      {/* ── 08 · LA MISIÓN DE R.01 · 432–533 ───────────────────────────── */}
      <Sequence from={432} durationInFrames={102}>
        <Clip src="s08_r01_regla.mp4" desdeS={0} />
      </Sequence>

      {/* ── 09 · EL CABLE · 534–641 · fallback por defecto: G apretado → cielo → ticker ── */}
      <Sequence from={534} durationInFrames={40}>
        <Clip src="s09_g_pantallas.mp4" desdeS={0} />
      </Sequence>
      <Sequence from={574} durationInFrames={30}>
        <Fija src="MF-cielo.jpg" marcas={marcas} />
        <LuzCable p={(f - 574) / 30} />
      </Sequence>
      <Sequence from={604} durationInFrames={38}>
        <Clip src="s09_ticker.mp4" desdeS={0} />
        <Ticker texto={`RENDER ${Math.min(9, 1 + Math.floor((f - 604) / 4))}/9`} />
      </Sequence>

      {/* ── 10 · MEDIO NIVEL -1 · 642–773 ──────────────────────────────── */}
      <Sequence from={642} durationInFrames={132}>
        <Clip src="s10_caos.mp4" desdeS={0} />
      </Sequence>

      {/* ── 10b · UN KILÓMETRO · 774–863 ───────────────────────────────── */}
      <Sequence from={774} durationInFrames={90}>
        <Clip src="s10b_kilometro.mp4" desdeS={0} />
      </Sequence>

      {/* ── 10c · EL QUE BAJA Y SE VA · 864–917 · el clip de ida, y el mismo al revés ── */}
      <Sequence from={864} durationInFrames={54}>
        <Clip src="s10c_piernas.mp4" desdeS={0} />
      </Sequence>

      {/* ── RÁFAGA · 918–953 · a hoja · b R.01 sobre el papel · c ticker ── */}
      <Sequence from={918} durationInFrames={12}><Clip src="../bloque2/s05_bandeja.mp4" desdeS={2.75} /></Sequence>
      <Sequence from={930} durationInFrames={12}><Clip src="s10b_kilometro.mp4" desdeS={1.2} escala={1.25} /></Sequence>
      <Sequence from={942} durationInFrames={12}>
        <Clip src="s09_ticker.mp4" desdeS={2.5} />
        <Ticker texto={f - 942 < 6 ? "RENDER 9/9" : "RENDER OK"} />
      </Sequence>

      {/* ── 11 · LA CARPETA · 954–1043 ─────────────────────────────────── */}
      <Sequence from={954} durationInFrames={90}>
        <Clip src="s11_carpeta.mp4" desdeS={0} />
      </Sequence>

      {/* ── 12 · SUBE · 1044–1163 ──────────────────────────────────────── */}
      <Sequence from={1044} durationInFrames={120}>
        <Clip src="s12_sube.mp4" desdeS={0} />
      </Sequence>

      {/* ── 13 · CALMA · 1164–1313 · el contador pasa a 1 en el 1252 ───── */}
      <Sequence from={1164} durationInFrames={150}>
        <Clip src="s13_calma.mp4" desdeS={0} />
        <Contador valor={f < 1252 ? 0 : 1} x={868} y={708} w={56} />
      </Sequence>

      {/* ── 14 · UNA COSITA MÁS · 1314–1385 · el tubo (mismo clip del 01) + el post-it macro ── */}
      <Sequence from={1314} durationInFrames={72}>
        <Clip src="../bloque1/s01_tubo.mp4" desdeS={1.7} />
        <Sequence from={30} durationInFrames={42}><PostItMacro texto={<>una<br />cosita<br />más…</>} /></Sequence>
      </Sequence>

      {/* ── 15 · NO. · 1386–1457 · Marta imprime una hoja · inserto NO. ── */}
      <Sequence from={1386} durationInFrames={72}>
        <Clip src="s15_no.mp4" desdeS={0} />
        <Sequence from={40} durationInFrames={32}><Inserto src="NO.png" rot={-2} /></Sequence>
      </Sequence>

      {/* ── 16 · G · 1458–1493 · still canon + visor −15 % + contador 0 · negro ── */}
      <Sequence from={1458} durationInFrames={36}>
        <Fija src="S16_G.jpg" marcas={marcas} />
        <Contador valor={0} x={296} y={846} w={120} />
        <Visor x={540} y={905} r={170} delta={f - 1458 >= 14 && f - 1458 < 26 ? -0.15 : 0} />
      </Sequence>

      {/* ── FIRMA · 1494–1553 ──────────────────────────────────────────── */}
      <Sequence from={1494} durationInFrames={60}><Firma /></Sequence>

      <Grano op={0.05} />
    </AbsoluteFill>
  );
};

export const Cap02FullRoughClean: React.FC = () => <Cap02FullRough marcas={false} />;
