// ============================================================================
// G.C.L. / CAP.02 — «ES UN CAMBIO CHICO» · V4 NARRATIVE + CHARACTER CUT
// 1524 frames · 50,8 s · 30 fps · 1080×1920 · base: CLARITY CUT V3 · 06-09-2026
// ----------------------------------------------------------------------------
// Pasada QUIRÚRGICA sobre la V3 (Valeria): la lógica del universo tiene que
// verse — ARRIBA (humanos) → SEND → INTAKE (Nivel -1) → G interpreta y resuelve
// → Marta / R.01 / Server operan según su función. Los personajes se definen
// por comportamiento: G el resolutivo (cuerpo ultrarrápido, estado cero
// estrés) · R.01 el ansioso/aperrado · Marta la veterana · Server el sobrepasado.
//
//   ARRIBA      0–53      microprólogo: laptop, mano humana, «es un cambio chico» → Enviar
//   whip        54–59     match cut vertical → Nivel -1
//   hook+…      60–972    la V3 corrida 60 f, con dos insertos de G ULTRARRÁPIDO (541, 761) y uno en la ráfaga
//   FALSA VICT. 973–1135  LISTO ✓ · R.01 se apaga · Marta trr… STOP · Server standby · G termina · SILENCIO · café
//   2ª SOLICITUD 1136–1221 tsh-TUNK · G gira · «una cosita más…»
//   PAYOFF      1222–1305 R.01 sale y BIP… · Server OVERLOAD → STANDBY · Marta trrr… CLAC
//   G           1306–1455 G ya está trabajando (rápido, sin drama) · última imagen: todos fundidos, G operativo
//   negro·firma 1456–1523
//
// Fuera el «NO.» (nadie estableció que Marta opine). Hard locks intactos.
// Nuevo generado: S00 (arriba) y S19 (G teclea ultrarrápido con la cabeza quieta).
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


/** Un clip a velocidad: G ultrarrápido (cuerpo a ×2–×3; la cabeza ya venía quieta del clip). */
const Rapido: React.FC<{src: string; desdeS?: number; vel: number}> = ({src, desdeS = 0, vel}) => (
  <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
    <OffthreadVideo src={src} startFrom={Math.round(desdeS * 30)} playbackRate={vel} muted
      style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover"}} />
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


/** Un plano (w×h, origen 0 0) pegado sobre un cuadrilátero del frame con una
 *  homografía (matrix3d de scripts/homografia-css.py). */
const Quad: React.FC<{m3d: string; w: number; h: number; children: React.ReactNode}> = ({m3d, w, h, children}) => (
  <div style={{position: "absolute", left: 0, top: 0, width: w, height: h, transform: m3d, transformOrigin: "0 0", overflow: "hidden"}}>{children}</div>
);

/** ARRIBA: el compositor de mensajes en el laptop. Escribe «es un cambio chico»
 *  letra a letra, el cursor va a Enviar, clic, el mensaje sube como enviado. */
const Composer: React.FC<{f: number}> = ({f}) => {
  const texto = "es un cambio chico";
  const n = Math.min(texto.length, Math.max(0, Math.floor((f - 6) / 1.55)));
  const enviado = f >= 46;
  const apretado = f >= 44 && f < 46;
  return (
    <div style={{width: "100%", height: "100%", background: "#F4F4F2", fontFamily: "Helvetica, Arial, sans-serif", color: "#1a1a1a", position: "relative"}}>
      <div style={{position: "absolute", left: 0, top: 0, right: 0, height: 64, background: "#fff", borderBottom: "1px solid #e2e2e0", display: "flex", alignItems: "center", padding: "0 34px", fontSize: 26, color: "#666"}}>
        <div style={{width: 30, height: 30, borderRadius: 15, background: "#d8d8d4", marginRight: 16}} />diseño · cambios
      </div>
      {enviado ? (
        <div style={{position: "absolute", right: 40, top: 130, background: "#1a1a1a", color: "#fff", padding: "20px 30px", borderRadius: "26px 26px 6px 26px", fontSize: 40, maxWidth: 640}}>
          {texto}<div style={{fontSize: 20, color: "#bbb", textAlign: "right", marginTop: 6}}>enviado ✓</div>
        </div>
      ) : null}
      <div style={{position: "absolute", left: 40, right: 40, bottom: 40, height: 110, background: "#fff", border: "2px solid #d6d6d2", borderRadius: 24, display: "flex", alignItems: "center", padding: "0 30px", fontSize: 40}}>
        <span style={{flex: 1, color: enviado ? "#c0c0bc" : "#1a1a1a"}}>{enviado ? "escribe un mensaje…" : texto.slice(0, n)}{!enviado && f % 16 < 8 ? "|" : ""}</span>
        <div style={{background: "#1a1a1a", color: "#fff", padding: "16px 34px", borderRadius: 18, fontSize: 32, transform: apretado ? "scale(.93)" : "scale(1)"}}>Enviar</div>
      </div>
    </div>
  );
};

/** Ventanas que cambian en el monitor izquierdo del 09 (G procesa varias cosas a la vez). */
const Pantalla: React.FC<{f: number; m3d: string}> = ({f, m3d}) => {
  const k = Math.floor(f / 3) % 4;
  const vistas = [
    {bg: "#1d2330", cabecera: "#2b3345", cuerpo: "#f2f2ee"}, {bg: "#f4f4f2", cabecera: "#d9d9d6", cuerpo: "#ffffff"},
    {bg: "#141414", cabecera: "#2a2a2a", cuerpo: "#0f0f0f"}, {bg: "#e9eef7", cabecera: "#c9d5ea", cuerpo: "#ffffff"},
  ][k];
  return (
    <Quad m3d={m3d} w={600} h={1000}>
      <div style={{width: "100%", height: "100%", background: vistas.bg, opacity: 0.92}}>
        <div style={{height: 60, background: vistas.cabecera}} />
        <div style={{margin: 30, height: 380, background: vistas.cuerpo, opacity: 0.9}} />
        <div style={{margin: 30, height: 200, background: vistas.cuerpo, opacity: 0.6}} />
        <div style={{position: "absolute", left: 40 + (k * 90) % 300, top: 520 + (k * 130) % 300, width: 260, height: 160, background: "#fff", boxShadow: "0 10px 30px rgba(0,0,0,.4)"}} />
      </div>
    </Quad>
  );
};

/** El parpadeo de las pantallas sobre la escena (G ultrarrápido): un velo frío que cambia cada 2–3 f. */
const Parpadeo: React.FC<{f: number; op?: number}> = ({f, op = 0.10}) => (
  <AbsoluteFill style={{background: `linear-gradient(90deg, rgba(180,210,255,${op * ((f % 5) / 4)}) 0%, transparent 60%)`, mixBlendMode: "screen", pointerEvents: "none"}} />
);

/** El whip vertical entre ARRIBA y ABAJO (6 f): arriba se va por arriba, abajo entra por abajo. */
const Whip: React.FC<{p: number; arriba: React.ReactNode; abajo: React.ReactNode}> = ({p, arriba, abajo}) => (
  <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
    <AbsoluteFill style={{transform: `translateY(${-p * 1920}px)`, filter: `blur(${p * (1 - p) * 40}px)`}}>{arriba}</AbsoluteFill>
    <AbsoluteFill style={{transform: `translateY(${(1 - p) * 1920}px)`, filter: `blur(${p * (1 - p) * 40}px)`}}>{abajo}</AbsoluteFill>
  </AbsoluteFill>
);

// cuadriláteros medidos (se rellenan con scripts/homografia-css.py)
const M3D_LAPTOP = "matrix3d(0.440097, -0.066177, 0.000000, -0.000103, -0.022256, 0.601824, 0.000000, 0.000042, 0.000000, 0.000000, 1.000000, 0.000000, 412.000000, 764.000000, 0.000000, 1.000000)";
const M3D_MONITOR09 = "matrix3d(0.385659, -0.004407, 0.000000, -0.000033, 0.000000, 0.402000, 0.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1040.000000, 0.000000, 1.000000)";

export const V4_FRAMES = 1524;

/** La marca de revisión: un FAIL declarado se ve en pantalla (sólo en el REVIEW CUT). */
const MarcaFail: React.FC<{texto: string}> = ({texto}) => (
  <div style={{position: "absolute", left: 40, top: 40, padding: "10px 16px", background: ROSA, color: "#080F14", fontFamily: VOZ.data, fontSize: 26, letterSpacing: 2}}>{texto}</div>
);

export const Cap02V4: React.FC<{marcas?: boolean}> = ({marcas = false}) => {
  asegurarFuentes();
  const f = useCurrentFrame();
  const Arriba = <><Clip src={b3("s00_arriba.mp4")} desdeS={0.3} /><Quad m3d={M3D_LAPTOP} w={1000} h={620}><Composer f={f} /></Quad></>;
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Audio src={staticFile("assets/gcl/cap02/v4_audio.wav")} />

      {/* ═══ ARRIBA · 0–53 · alguien humano, en Copywriters, escribe «es un cambio chico» y aprieta Enviar ═══ */}
      <Sequence from={0} durationInFrames={54}>{Arriba}</Sequence>
      {/* whip vertical · 54–59 · match cut ARRIBA → NIVEL -1 (el tubo) */}
      <Sequence from={54} durationInFrames={6}>
        <Whip p={(f - 54 + 1) / 6} arriba={Arriba} abajo={<Clip src={b1("s01_tubo.mp4")} desdeS={1.7} />} />
      </Sequence>

      {/* ═══ INTRIGA · 60–131 · el hook (V3 + 60) · TSH-TUNK: la solicitud se materializa ═══ */}
      <Sequence from={60} durationInFrames={21}><Clip src={b1("s01_tubo.mp4")} desdeS={1.7} /></Sequence>
      <Sequence from={81} durationInFrames={12}>
        <Clip src={b1("s02a_marta.mp4")} desdeS={3.6} />
        <LCD linea1={f - 81 < 6 ? "LISTA" : "AY."} caja={{x: 250, y: 640, w: 170, h: 62}} />
      </Sequence>
      <Sequence from={93} durationInFrames={12}><Clip src={b1("s02b_server.mp4")} desdeS={3.62} /></Sequence>
      <Sequence from={105} durationInFrames={12}><Clip src={b1("s02c_r01.mp4")} desdeS={1.95} /></Sequence>
      <Sequence from={117} durationInFrames={15}><Clip src={b1("s02d_g.mp4")} desdeS={2.0} /></Sequence>
      <Sequence from={132} durationInFrames={48}><Clip src={b1("s03_wide.mp4")} desdeS={2.2} /></Sequence>

      {/* ═══ REVELACIÓN · 04 · 180–276 · G recoge la solicitud del intake y la lee ═══ */}
      <Sequence from={180} durationInFrames={52}>
        <Clip src={b2("s04_postit.mp4")} desdeS={2.3} />
        {marcas ? <MarcaFail texto="FAIL — G SCALE / PROPORTION · regenerar para MASTER" /> : null}
      </Sequence>
      <Sequence from={232} durationInFrames={45}><PostItMacro texto={<>es un<br />cambio<br />chico</>} /></Sequence>

      {/* ═══ COPY · DISEÑO · 277–384 ═══ */}
      <Sequence from={277} durationInFrames={18}><Clip src={b2("s05_bandeja.mp4")} desdeS={0.3} /></Sequence>
      <Sequence from={295} durationInFrames={42}><Inserto src="v2_copy.png" rot={-4} /></Sequence>
      <Sequence from={337} durationInFrames={12}><Clip src={b1("s02a_marta.mp4")} desdeS={2.4} /></Sequence>
      <Sequence from={349} durationInFrames={36}><Inserto src="v2_layout.png" rot={3} /></Sequence>

      {/* 06 · 385–444 */}
      <Sequence from={385} durationInFrames={60}>
        <Clip src={b2("s06_doshojas.mp4")} desdeS={1.6} />
        <Contador valor={0} x={296} y={846} w={120} />
      </Sequence>

      {/* ═══ FORMATOS · 445–540 · G ULTRARRÁPIDO 1 · 541–570 (los rehace: cuerpo a ×2, cabeza quieta) ═══ */}
      <Sequence from={445} durationInFrames={48}><Clip src={b2("s07_nueve.mp4")} desdeS={1.8} /></Sequence>
      <Sequence from={493} durationInFrames={36}><Inserto src="v2_formatos.png" rot={-2} /></Sequence>
      <Sequence from={529} durationInFrames={12}><Clip src={b2("s07_nueve.mp4")} desdeS={4.0} /></Sequence>
      <Sequence from={541} durationInFrames={30}>
        <Rapido src={b3("s19_g_ultrarrapido.mp4")} desdeS={0.5} vel={2} />
        <Parpadeo f={f} />
      </Sequence>

      {/* 08 · R.01 trabado · 571–636 · el aperrado se complica solo */}
      <Sequence from={571} durationInFrames={66}><Clip src={b3("s08_r01_regla.mp4")} desdeS={0} /></Sequence>

      {/* ═══ VIDEO · 637–736 · G «mm.», varias ventanas a la vez, tap → la luz por el cable → ticker ═══ */}
      <Sequence from={637} durationInFrames={36}>
        <Clip src={b3("s09_g_pantallas.mp4")} desdeS={1.9} />
        <Sequence from={10}><Pantalla f={f} m3d={M3D_MONITOR09} /></Sequence>
      </Sequence>
      <Sequence from={673} durationInFrames={24}>
        <Fija src={b3("MF-cielo.jpg")} />
        <LuzCable p={(f - 673) / 24} />
      </Sequence>
      <Sequence from={697} durationInFrames={40}>
        <Clip src={b3("s09_ticker.mp4")} desdeS={2.5} />
        <Ticker texto={`VIDEO · RENDER ${Math.min(9, Math.floor((f - 697) / 4))}/9`} />
      </Sequence>

      {/* ═══ LANDING · 737–760 · G ULTRARRÁPIDO 2 · 761–780 · 10 · 781–846 ═══ */}
      <Sequence from={737} durationInFrames={24}><Inserto src="v2_landing.png" rot={2} /></Sequence>
      <Sequence from={761} durationInFrames={20}>
        <Rapido src={b3("s19_g_ultrarrapido.mp4")} desdeS={1.2} vel={2.5} />
        <Parpadeo f={f} op={0.14} />
      </Sequence>
      <Sequence from={781} durationInFrames={66}><Clip src={b3("s10_caos.mp4")} desdeS={0.9} /></Sequence>

      {/* ═══ PAUTA · 847–870 · 10b · 871–900 · R.01 arrastra la lista ═══ */}
      <Sequence from={847} durationInFrames={24}><Inserto src="v2_pauta.png" rot={-3} /></Sequence>
      <Sequence from={871} durationInFrames={30}><Clip src={b3("s10b_kilometro.mp4")} desdeS={0} /></Sequence>

      {/* ═══ SATURACIÓN · ráfaga · 901–948 · hoja · R.01 · RENDER OK · G ×3 ═══ */}
      <Sequence from={901} durationInFrames={12}><Clip src={b2("s05_bandeja.mp4")} desdeS={0.5} /></Sequence>
      <Sequence from={913} durationInFrames={12}><Clip src={b3("s10b_kilometro.mp4")} desdeS={0.3} escala={1.25} /></Sequence>
      <Sequence from={925} durationInFrames={12}>
        <Clip src={b3("s09_ticker.mp4")} desdeS={2.5} />
        <Ticker texto={f - 925 < 6 ? "VIDEO · RENDER 9/9" : "VIDEO · OK"} />
      </Sequence>
      <Sequence from={937} durationInFrames={12}>
        <Rapido src={b3("s19_g_ultrarrapido.mp4")} desdeS={0.2} vel={3} />
        <Parpadeo f={f} op={0.18} />
      </Sequence>

      {/* ═══ PRESENTACIÓN · 949–972 ═══ */}
      <Sequence from={949} durationInFrames={24}><Inserto src="v2_presentacion.png" rot={-2} /></Sequence>

      {/* ═══ FALSA VICTORIA · 973–1135 · LISTO ✓ · todos paran · SILENCIO · el café ═══ */}
      <Sequence from={973} durationInFrames={24}>
        <Clip src={b3("s09_ticker.mp4")} desdeS={2.5} />
        <Ticker texto="CAMBIO CHICO · LISTO ✓" />
      </Sequence>
      <Sequence from={997} durationInFrames={20}><Clip src={b3("s08_r01_regla.mp4")} desdeS={1.4} /></Sequence>   {/* R.01 se detiene, agotado */}
      <Sequence from={1017} durationInFrames={24}>
        <Clip src={b1("s02a_marta.mp4")} desdeS={2.4} />
        <LCD linea1={f - 1017 < 16 ? "LISTA" : ""} caja={{x: 250, y: 640, w: 170, h: 62}} />   {/* la última hoja · trr… trr… STOP */}
      </Sequence>
      <Sequence from={1041} durationInFrames={20}>
        <Clip src={b3("s09_ticker.mp4")} desdeS={2.5} />
        <Ticker texto={f - 1041 < 8 ? "STANDBY" : ""} />
      </Sequence>
      <Sequence from={1061} durationInFrames={15}><Rapido src={b3("s19_g_ultrarrapido.mp4")} desdeS={2.4} vel={1} /></Sequence>   {/* el último proceso · el s19 sirve hasta 3,0 s: después el visor se vuelve pantalla */}
      <Sequence from={1076} durationInFrames={60}>
        <Sequence from={0} durationInFrames={18}><Clip src={b3("s13_calma.mp4")} desdeS={0} /></Sequence>
        <Sequence from={18}><Fija src={b3("s13_hold.jpg")} /></Sequence>
        <Contador valor={f < 1100 ? 0 : 1} x={868} y={708} w={56} />
      </Sequence>

      {/* ═══ SEGUNDA SOLICITUD · 1136 · tsh-TUNK rompe la calma · G gira al intake · «una cosita más…» ═══ */}
      <Sequence from={1136} durationInFrames={20}><Clip src={b1("s01_tubo.mp4")} desdeS={1.7} /></Sequence>
      <Sequence from={1156} durationInFrames={18}><Fija src={b3("S16_G.jpg")} /></Sequence>
      <Sequence from={1174} durationInFrames={48}><PostItMacro texto={<>una<br />cosita<br />más…</>} /></Sequence>

      {/* ═══ PAYOFF · 1222–1305 · R.01 sale y BIP… · Server OVERLOAD → STANDBY · Marta trrr… CLAC ═══ */}
      <Sequence from={1222} durationInFrames={15}><Clip src={b3("s10b_kilometro.mp4")} desdeS={0} /></Sequence>
      <Sequence from={1237} durationInFrames={15}><Clip src={b3("s08_r01_regla.mp4")} desdeS={1.4} /></Sequence>
      <Sequence from={1252} durationInFrames={24}>
        <Clip src={b1("s02b_server.mp4")} desdeS={3.62} />
        <Ticker texto={f - 1252 < 10 ? ((f - 1252) % 4 < 2 ? "OVERLOAD" : "") : "STANDBY"} />
      </Sequence>
      <Sequence from={1276} durationInFrames={30}>
        <Clip src={b3("s15_no.mp4")} desdeS={0.2} />
        <LCD linea1={f - 1276 < 22 ? ((f - 1276) % 6 < 3 ? "IMPRIM." : "") : ""} caja={{x: 250, y: 640, w: 170, h: 62}} />
      </Sequence>

      {/* ═══ G · 1306–1365 · ya está trabajando · ÚLTIMA IMAGEN · 1366–1455 · todos fundidos, G operativo ═══ */}
      <Sequence from={1306} durationInFrames={60}>
        <Rapido src={b3("s19_g_ultrarrapido.mp4")} desdeS={0} vel={1.4} />
        <Parpadeo f={f} op={0.12} />
      </Sequence>
      <Sequence from={1366} durationInFrames={69}><Clip src={b3("s17_desastre.mp4")} desdeS={0.2} /></Sequence>
      <Sequence from={1435} durationInFrames={21}><Clip src={b3("s17_desastre_rev.mp4")} desdeS={2.58} /></Sequence>
      <Sequence from={1456} durationInFrames={8}><AbsoluteFill style={{backgroundColor: "#000"}} /></Sequence>
      <Sequence from={1464} durationInFrames={60}><Firma /></Sequence>
      <Grano op={0.05} />
    </AbsoluteFill>
  );
};

/** REVIEW CUT pre-master: la V4 tal cual, con los FAIL declarados marcados en pantalla. */
export const Cap02PremasterReview: React.FC = () => <Cap02V4 marcas />;
