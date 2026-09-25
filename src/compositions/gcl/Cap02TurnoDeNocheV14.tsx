// ============================================================================
// G.CL / CAP.02 — «TURNO DE NOCHE» · CORTE 14 · = corte 13 musicalizado con «Reptilia» (The Strokes, instrumental)
// 30 fps · 1080×1920 · 25-09-2026
// ----------------------------------------------------------------------------
// Manda: gcl-agent/universo/06_VIDEO_REELS/CAP_02_TURNO_DE_NOCHE/GUION_V3_MANANA_LO_VEO.md (§ corte 6)
// Corte 14 (Valeria: «música más trend, más cool: The Strokes instrumental»): temp track «Reptilia»
// (157,9 BPM, beat = 11,4 f). ⚠️ TEMP TRACK sin licencia: para publicar, poner la canción desde la
// biblioteca de música de Instagram/TikTok al subir el reel, o licenciarla. Ver TRAMOS_MUSICA.
// Corte 13 (Valeria: «el último cambio»): NO se reenvía el mensaje hacia abajo. Pancho lee el mail del
// cliente («volvemos a la versión anterior») y cortamos directo a los de abajo explotando: se da por
// entendido que ya se enteraron. Sin «Reenviar», sin tubo bajando, sin cápsula, sin «NUEVO INPUT».
// El cierre (Departamento de cosas imposibles + próximo capítulo) va SIN MÚSICA: sólo el tecleo.
// Corte 12: los PERSONAJES terminan en la explosión (negro), y después viene la tarjeta de CopyLab.
// Corte 11 (Valeria: «me parece bien»): +1 s al inicio para leer el post-it; el capítulo TERMINA cuando
// explotan. Justo ahí. Nada después: sin tiznados, sin halo cayendo, sin trombón, sin tarjeta de cierre.
// Corte 10 sobre el corte 7 (la línea aprobada): la versión que mandan es la V3 (el cliente pide
// cambios «sobre una versión», así «volver a la anterior» tiene sentido) y la MÚSICA se une:
// un solo tema (temp-g) que cambia de estado — entero en el trabajo, CANSADO (grave y lento) en el
// descanso, FRESCO (su intro, un pelo más rápido) bajo la comedia de la mañana, y su GOLPE FINAL
// como botón del cierre. La comedia de oficina (temp-k) entra encima del tema fresco en el sorbo.
// Últimos cambios (25-09, noche): música de principio a fin con cuatro pistas y cross-fades ·
// Pancho desde atrás (P02b, menos cara = más real), se va a las 18:30 y se corta cuando se para ·
// +5 s de trabajo tipo Pixar: brainstorm en el pinboard, pelea tirando de la misma hoja hasta
// que se rompe, Rolo pinta a brochazos y G mide con regla · descansan con «zzz» y brindan ·
// match cut al sorbo de café de Pancho · cierre con dinamismo: whooshes, el halo se le cae a G.
// Cambios de Valeria sobre el corte 5:
//   · fuera la voz robótica del hook y fuera Pancho escribiendo: música de INTRIGA desde el post-it,
//     Pancho lo ve, un PENSAMIENTO sale de su cabeza («lo veo mañana, 9 AM»), cierra y se va
//   · fuera el WOW de Gin (no se entiende quién es): un solo bloque largo de trabajo, inspirados,
//     con interacción (se ponen de acuerdo, discuten), MENSAJES entre ellos y CÓDIGOS en pantalla,
//     y un HUD de avance para que se lea qué están haciendo
//   · «V1 LISTA» con tiempo · sube · llega al computador de Pancho · descansan y CELEBRAN con café
//   · el envío al cliente y la respuesta con tiempo · el equipo recibe el nuevo input → explotan → cierre
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame} from "remotion";
import {VOZ, asegurarFuentes} from "../../brand/copylab/sistema";
import {Superficie, Track, frameClip} from "./superficie";
import {SuperficieCurva, Perfil} from "./superficie-curva";
import {CierreSerie, cierreFrames} from "./CierreSerie";
import trackP04 from "./track/P04.json";
import POSTITS from "./track/postits.json";

const ROSA = "#FF2D8B";
const v = (n: string) => staticFile(`assets/gcl/cap02-v3/video/${n}.mp4`);
const fx = (n: string) => staticFile(`assets/gcl/cap02-v3/sfx/${n}.mp3`);
const clamp = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

const TAGLINE = "COPYLAB\nDepartamento de cosas imposibles.";
const PROXIMO = "Batalla campal: G vs humanos"; // ← por definir con Valeria
const CIERRE_TW0 = 84;
const CIERRE = cierreFrames(PROXIMO, CIERRE_TW0);

type Plano = {
  id: string; clip?: string; dur: number; desde?: number; vel?: number;
  zoom?: {s: number; x: string; y: string; s1?: number}; sacudir?: number;
  still?: boolean; grano?: boolean; negro?: boolean;
};
const PLANOS: Plano[] = [
  // HOOK — 18:59 · música de intriga desde el primer cuadro
  {id: "P01", dur: 63, zoom: {s: 1.0, x: "50%", y: "50%", s1: 1.10}},
  {id: "P02b", dur: 60, desde: 1.2, vel: 1.0, grano: true},
  // EL TUBO ▼ — 19:02
  {id: "N02", dur: 18, desde: 0.3, vel: 2.2},
  {id: "N03", dur: 24, desde: 0.4, vel: 1.8},
  {id: "P04", dur: 33, desde: 1.8, zoom: {s: 1.55, x: "535px", y: "640px"}},
  // OH NO / G HERO
  {id: "P05", dur: 18, vel: 1.2},
  {id: "P06", dur: 27, desde: 0.3, vel: 2},
  // ILUMINACIÓN
  {id: "N04", dur: 18, desde: 0.3, vel: 1.4},
  {id: "N05", dur: 21, desde: 0.3},
  {id: "N06", dur: 27, desde: 0.3, vel: 1.2},
  {id: "N07", dur: 27, desde: 0.4, vel: 1.4},
  // TRABAJO — 19:30 → 05:40 · un solo bloque largo, inspirados: se ponen de acuerdo, códigos, mensajes, gags
  {id: "T1", clip: "N08", dur: 24, desde: 0.1, vel: 1.6, sacudir: 3},
  {id: "T2", clip: "N20", dur: 24, desde: 0.2, vel: 1.4},
  {id: "T3", clip: "N09", dur: 12, desde: 0.5, vel: 2},
  {id: "T4", clip: "P08a", dur: 18, desde: 0.5, vel: 1.8},
  {id: "T5", clip: "N17", dur: 33, desde: 0.3, vel: 1.4},
  {id: "T6", clip: "N08", dur: 18, desde: 0.7, vel: 1.6, sacudir: 3},
  {id: "T7", clip: "N18", dur: 33, desde: 0.3, vel: 1.6},
  {id: "T8", clip: "P08b", dur: 18, desde: 0.5, vel: 1.8},
  {id: "T9", clip: "P19", dur: 24, desde: 0.8, vel: 1.8},
  {id: "T10", clip: "N19", dur: 30, desde: 0.3, vel: 1.5},
  {id: "T11", clip: "P20", dur: 12, desde: 0.5, vel: 2},
  {id: "T12", clip: "N08", dur: 18, desde: 0.1, vel: 1.6, sacudir: 3},
  {id: "T13", clip: "N09", dur: 10, desde: 2.5, vel: 2},
  // +5 s tipo Pixar: crean, pelean, cada uno a su manera
  {id: "X1", clip: "N23", dur: 36, desde: 0.3, vel: 1.5},
  {id: "X2", clip: "N24", dur: 57, desde: 1.0, vel: 1.5},
  {id: "X3", clip: "N25", dur: 33, desde: 0.3, vel: 1.5},
  {id: "X4", clip: "N08", dur: 12, desde: 0.1, vel: 1.6, sacudir: 3},
  {id: "T14", clip: "P08c", dur: 24, desde: 0.5, vel: 1.4},
  // V1 LISTA — con tiempo
  {id: "LISTA", clip: "P08c", dur: 45, desde: 1.6, vel: 0.6},
  // SUBE ▲ y llega
  {id: "N10", dur: 24, desde: 0.8, vel: 1.5},
  {id: "SUBE", clip: "N02-sube", dur: 15, desde: 3.8, vel: 2.2},
  {id: "N11", dur: 42, desde: 1.4, vel: 1.2},
  // DESCANSAN (zzz) y CELEBRAN con café → match cut al sorbo de Pancho
  {id: "P22", dur: 48, desde: 0.5},
  {id: "N22", dur: 60, desde: 0.3, vel: 1.2},
  // 09:00 — con ritmo
  {id: "P17", dur: 30, desde: 0.5, vel: 1.3, grano: true},
  {id: "MAIL", clip: "P17", dur: 78, desde: 3.5, vel: 0.2, grano: true},
  {id: "RESP", clip: "P17", dur: 60, desde: 4.2, vel: 0.15, grano: true},
  // corte directo: ABAJO explotan (ya se enteraron — no hace falta mostrar el reenvío)
  {id: "N13", dur: 56, desde: 1.0, vel: 1.8},
  {id: "NEGRO", dur: 14, negro: true},
  {id: "CIERRE", dur: CIERRE},
];
const INICIO: Record<string, number> = {};
{let t = 0; for (const p of PLANOS) {INICIO[p.id] = t; t += p.dur;}}
export const TURNO_V14_FRAMES = PLANOS.reduce((a, p) => a + p.dur, 0);
const en = (id: string, extra = 0) => INICIO[id] + extra;
const P = (id: string) => PLANOS.find((p) => p.id === id)!;

// ── TEXTO DIEGÉTICO ─────────────────────────────────────────────────────────

/** El pedido del cliente, en plumón. Deja libre el cuarto de abajo para Pancho. */
const TextoCliente: React.FC<{w: number}> = ({w}) => (
  <>
    <div style={{fontSize: w * 0.22, fontWeight: 700, color: "#b3122e", textDecoration: "underline", textDecorationThickness: 4}}>URGENTE</div>
    <div style={{fontSize: w * 0.105, fontWeight: 600, marginTop: w * 0.03, color: "#b3122e"}}>pedido del cliente:</div>
    <div style={{fontSize: w * 0.135, fontWeight: 600}}>ajustar campaña</div>
    <div style={{fontSize: w * 0.14, fontWeight: 700, marginTop: w * 0.01}}>ENTREGA 09:00</div>
  </>
);

type DatosPostIt = {quad: [number, number][]; perfil: Perfil};
const postit = (id: string) => (POSTITS as unknown as Record<string, DatosPostIt | undefined>)[id];

/** El post-it pegado en el monitor, que se CURVA al despegarse: el texto va en tiras sobre el
 *  perfil medido (P01 y N01 son el mismo encuadre; el perfil de P01 no tiene la mano encima). */
const PostIt: React.FC = () => {
  const d = postit("P01");
  if (!d) return null;
  const yTop = d.perfil[0][0], yBot = d.perfil[d.perfil.length - 1][0];
  const W = 560, H = 520;
  return (
    <>
      <SuperficieCurva perfil={d.perfil} y0={yTop + 20} y1={yTop + (yBot - yTop) * 0.72} w={W} h={H} offsetY={-12} tiras={10}
        style={{mixBlendMode: "multiply"}}>
        <div style={{width: W, height: H, display: "flex", flexDirection: "column", justifyContent: "center", fontFamily: VOZ.mano,
          textAlign: "center", color: "#1d1a33", lineHeight: 0.95, filter: "blur(0.5px)"}}>
          <TextoCliente w={W} />
        </div>
      </SuperficieCurva>
    </>
  );
};


/** P04: Marta imprime EL pedido que bajó por el tubo. Sale de la ranura hacia arriba. */
const TIRA_QUAD: [number, number][] = [[478, 470], [594, 470], [594, 832], [478, 832]];
const TiraMarta: React.FC<{f: number}> = ({f}) => {
  const p = P("P04");
  const k = frameClip(trackP04 as Track, f, p.desde ?? 0, p.vel ?? 1);
  const sale = interpolate(f, [0, 26], [1, 0], clamp);
  const lineas = ["URGENTE", "pedido del", "cliente:", "ajustar", "campaña", "ENTREGA", "09:00"];
  return (
    <Superficie track={trackP04 as Track} k={k} quad={TIRA_QUAD} w={116} h={362} offsetY={-12}
      style={{overflow: "hidden", mixBlendMode: "multiply"}}>
      <div style={{transform: `translateY(${sale * 362}px)`, textAlign: "center", fontFamily: VOZ.data, fontWeight: 600,
        fontSize: 19, lineHeight: "40px", color: "#2a2730", letterSpacing: 1, filter: "blur(0.3px)", paddingTop: 14}}>
        {lineas.map((l, i) => <div key={i} style={{fontWeight: i === 0 ? 800 : 600, fontSize: i === 0 ? 23 : 19}}>{l}</div>)}
      </div>
    </Superficie>
  );
};

/** El pensamiento de Pancho, saliendo de su cabeza. CABEZA = borde superior-izquierdo de la cabeza en P02b (px). */
const CABEZA = {x: 350, y: 300}; // borde superior-DERECHO de la cabeza en P02b: la burbuja va a la derecha
const Pensamiento: React.FC = () => {
  const f = useCurrentFrame();
  const p = spring({frame: f - 8, fps: 30, config: {damping: 11, stiffness: 150}});
  const sale = interpolate(f, [52, 60], [1, 0], clamp); // se va con él
  const burbujas = [{x: CABEZA.x + 30, y: CABEZA.y - 10, r: 9, d: 0}, {x: CABEZA.x + 80, y: CABEZA.y - 70, r: 15, d: 3}, {x: CABEZA.x + 130, y: CABEZA.y - 140, r: 22, d: 6}];
  return (
    <div style={{position: "absolute", inset: 0, opacity: sale}}>
      {burbujas.map((b, i) => {
        const s = spring({frame: f - b.d, fps: 30, config: {damping: 12}});
        return <div key={i} style={{position: "absolute", left: b.x - b.r, top: b.y - b.r - 12, width: b.r * 2, height: b.r * 2, borderRadius: "50%",
          background: "#fff", transform: `scale(${s})`, boxShadow: "0 6px 20px rgba(0,0,0,0.35)"}} />;
      })}
      <div style={{position: "absolute", left: CABEZA.x + 60, top: 230, width: 430, padding: "34px 36px", borderRadius: 120, background: "#fff",
        transform: `scale(${interpolate(p, [0, 1], [0.4, 1])})`, transformOrigin: "10% 100%", opacity: p,
        boxShadow: "0 16px 50px rgba(0,0,0,0.4)", fontFamily: VOZ.mano, fontSize: 50, fontWeight: 600, color: "#1d1a33",
        textAlign: "center", lineHeight: 1.05}}>
        lo veo mañana,<br />9 AM 😌
      </div>
    </div>
  );
};

// ── TEXTO EN PANTALLA ───────────────────────────────────────────────────────
const Cabecera: React.FC<{hora?: string; color?: string}> = ({hora, color = ROSA}) => (
  <div style={{position: "absolute", left: 64, top: 150, fontFamily: VOZ.data, letterSpacing: 4}}>
    <div style={{fontSize: 22, color: "rgba(242,244,246,0.7)"}}>TEMPORADA 1 · CAPÍTULO 02</div>
    {hora && <div style={{fontSize: 30, color, marginTop: 10}}>{hora}</div>}
  </div>
);

/** El reloj corre durante un bloque de trabajo (minutos desde las 00:00, puede pasar de medianoche). */
const Reloj: React.FC<{id: string; de: string; a: string; m0: number; m1: number}> = ({id, de, a, m0, m1}) => {
  const f = useCurrentFrame();
  const t0 = en(de), t1 = en(a);
  const m = Math.round(interpolate(f + en(id), [t0, t1], [m0, m1], clamp)) % (24 * 60);
  const hh = String(Math.floor(m / 60)).padStart(2, "0"), mm = String(m % 60).padStart(2, "0");
  return <Cabecera hora={`${hh}:${mm}`} />;
};
const RelojTrabajo: React.FC<{id: string}> = ({id}) => <Reloj id={id} de="T1" a="LISTA" m0={19 * 60} m1={24 * 60 + 5 * 60 + 40} />;

const Golpe: React.FC<{texto: string}> = ({texto}) => (
  <div style={{position: "absolute", left: 0, right: 0, top: 1300, textAlign: "center", fontFamily: VOZ.narrow, fontWeight: 800,
    fontSize: 132, letterSpacing: 2, color: "#F2F4F6", textShadow: "0 4px 30px rgba(0,0,0,0.7)"}}>
    {texto} <span style={{color: ROSA}}>✓</span>
  </div>
);

const Dato: React.FC<{texto: string; top?: number; left?: number; color?: string; size?: number}> = ({texto, top = 1330, left = 64, color = ROSA, size = 30}) => (
  <div style={{position: "absolute", left, top, fontFamily: VOZ.data, fontSize: size, letterSpacing: 4, color,
    textShadow: "0 2px 14px rgba(0,0,0,0.9)"}}>{texto}</div>
);


/** HUD de avance: se lee qué están haciendo. Va llenándose a lo largo del bloque de trabajo. */
const HUD: React.FC<{id: string}> = ({id}) => {
  const f = useCurrentFrame();
  const g = f + en(id);
  const tramo = (a: string, b: string) => interpolate(g, [en(a), en(b)], [0, 100], clamp);
  const items = [
    {n: "COPY", v: tramo("T1", "T4")},
    {n: "DISEÑO", v: tramo("T5", "T8")},
    {n: "EXPORT", v: tramo("T10", "LISTA")},
  ];
  const op = interpolate(f, [0, 8], [0, 1], clamp);
  return (
    <div style={{position: "absolute", right: 64, top: 150, width: 330, opacity: op, fontFamily: VOZ.data, letterSpacing: 3}}>
      <div style={{fontSize: 20, color: "rgba(242,244,246,0.6)", textAlign: "right"}}>NIVEL −1 · AVANCE</div>
      {items.map((it) => (
        <div key={it.n} style={{marginTop: 14}}>
          <div style={{display: "flex", justifyContent: "space-between", fontSize: 24, color: it.v >= 100 ? ROSA : "#F2F4F6"}}>
            <span>{it.n}</span><span>{it.v >= 100 ? "✓" : `${Math.round(it.v)} %`}</span>
          </div>
          <div style={{height: 6, background: "rgba(242,244,246,0.18)", marginTop: 6, borderRadius: 3}}>
            <div style={{height: 6, width: `${it.v}%`, background: ROSA, borderRadius: 3}} />
          </div>
        </div>
      ))}
    </div>
  );
};

/** Códigos en la pantalla de G (N08): líneas rosadas que corren sobre el laptop de la izquierda. */
const Codigo: React.FC = () => {
  const f = useCurrentFrame();
  const lineas = ["> brief.parse()", "  cliente: urgente", "  entrega: 09:00", "> copy.generar(v=1)", "  tono: directo", "  claims: 3", "> diseño.layout()",
    "  grid: 4x5", "  paleta: G", "> export.pdf()", "  ok ✓", "> enviar(tubo ▲)", "  esperando…", "> copy.iterar()", "  v1 → v1.1", "  ok ✓"];
  const desde = Math.floor(f / 4);
  return (
    <div style={{position: "absolute", left: 30, top: 940, width: 340, height: 300, overflow: "hidden", padding: "10px 14px",
      fontFamily: VOZ.data, fontSize: 21, lineHeight: "30px", color: ROSA, mixBlendMode: "screen", opacity: 0.9,
      textShadow: "0 0 8px rgba(255,45,139,0.9)", transform: "perspective(900px) rotateY(18deg)", transformOrigin: "0 50%"}}>
      {Array.from({length: 9}).map((_, i) => <div key={i}>{lineas[(desde + i) % lineas.length]}</div>)}
    </div>
  );
};

/** Mensajes entre ellos: tarjetas de datos de los robots. */
const Mensaje: React.FC<{de: string; txt: string; top?: number}> = ({de, txt, top = 1440}) => {
  const f = useCurrentFrame();
  const p = spring({frame: f - 2, fps: 30, config: {damping: 12, stiffness: 170}});
  return (
    <div style={{position: "absolute", left: 64, top, transform: `translateX(${(1 - p) * -60}px)`, opacity: p, padding: "16px 24px",
      borderRadius: 16, background: "rgba(8,15,20,0.78)", border: "1px solid rgba(255,45,139,0.5)", fontFamily: VOZ.data, letterSpacing: 2}}>
      <div style={{fontSize: 20, color: ROSA}}>{de}</div>
      <div style={{fontSize: 28, color: "#F2F4F6", marginTop: 4}}>{txt}</div>
    </div>
  );
};

/** Sello grande (V1 LISTA): entra golpeando, un poco torcido, y se queda. */
const Sello: React.FC<{texto: string}> = ({texto}) => {
  const f = useCurrentFrame();
  const s = interpolate(f, [0, 5], [1.7, 1], clamp);
  const op = interpolate(f, [0, 2], [0, 1], clamp);
  return (
    <div style={{position: "absolute", left: 0, right: 0, top: 1150, display: "flex", justifyContent: "center", opacity: op}}>
      <div style={{transform: `rotate(-6deg) scale(${s})`, border: `12px solid ${ROSA}`, borderRadius: 22, padding: "14px 48px",
        fontFamily: VOZ.narrow, fontWeight: 800, fontSize: 150, letterSpacing: 6, color: ROSA, lineHeight: 1, textAlign: "center",
        textShadow: "0 0 30px rgba(0,0,0,0.6)", background: "rgba(8,15,20,0.35)"}}>
        {texto}
      </div>
    </div>
  );
};

/** El tubo: contador de pisos mientras la cápsula viaja. */
const Pisos: React.FC<{sube?: boolean}> = ({sube}) => {
  const f = useCurrentFrame();
  const orden = ["PISO 3", "PISO 2", "PISO 1", "PISO 0", "NIVEL −1"];
  const lista = sube ? [...orden].reverse() : orden;
  const i = Math.min(lista.length - 1, Math.floor(f / 3));
  return (
    <div style={{position: "absolute", right: 64, top: 150, textAlign: "right", fontFamily: VOZ.data, letterSpacing: 4}}>
      <div style={{fontSize: 22, color: "rgba(242,244,246,0.7)"}}>TUBO {sube ? "▲" : "▼"}</div>
      <div style={{fontSize: 30, color: ROSA, marginTop: 10}}>{lista[i]}</div>
    </div>
  );
};

/** Lo que trae la cápsula al escritorio de Pancho, al amanecer. */
const NotaTubo: React.FC = () => {
  const f = useCurrentFrame();
  const p = spring({frame: f - 10, fps: 30, config: {damping: 12}});
  return (
    <div style={{position: "absolute", left: 150, right: 150, top: 1180, transform: `translateY(${(1 - p) * 60}px) rotate(-3deg)`, opacity: p,
      background: "#F4EBD0", padding: "26px 34px", borderRadius: 6, boxShadow: "0 14px 40px rgba(0,0,0,0.5)", fontFamily: VOZ.data, color: "#2a2730"}}>
      <div style={{fontSize: 22, letterSpacing: 3, opacity: 0.7}}>NIVEL −1 → PANCHO · 06:47</div>
      <div style={{fontSize: 46, fontWeight: 700, marginTop: 10}}>V3 lista.</div>
      <div style={{fontSize: 46, fontWeight: 700}}>Revisar ✓</div>
    </div>
  );
};

// ── EL CORREO DE PANCHO (inserto de pantalla) — con tiempo para leerlo ─────
const Cursor: React.FC<{x: number; y: number; clic?: boolean}> = ({x, y, clic}) => (
  <svg width={54} height={70} viewBox="0 0 18 24" style={{position: "absolute", left: x, top: y, transform: clic ? "scale(0.85)" : undefined,
    filter: "drop-shadow(0 3px 6px rgba(0,0,0,0.5))"}}>
    <path d="M1 1 L1 19 L6 14.5 L9.5 22 L12.5 20.7 L9 13.3 L15.5 13.3 Z" fill="#fff" stroke="#111" strokeWidth={1.3} />
  </svg>
);

const Ventana: React.FC<{children: React.ReactNode; titulo: string}> = ({children, titulo}) => (
  <div style={{position: "absolute", left: 60, right: 60, top: 430, borderRadius: 30, overflow: "hidden", background: "#FBFBFC",
    boxShadow: "0 40px 100px rgba(0,0,0,0.65)", fontFamily: VOZ.funcional, color: "#1b1b1f", transform: "perspective(1800px) rotateX(4deg)"}}>
    <div style={{display: "flex", alignItems: "center", gap: 14, padding: "22px 30px", background: "#EDEEF1", fontSize: 26, color: "#555"}}>
      <span style={{width: 18, height: 18, borderRadius: 9, background: "#FF5F57"}} />
      <span style={{width: 18, height: 18, borderRadius: 9, background: "#FEBC2E"}} />
      <span style={{width: 18, height: 18, borderRadius: 9, background: "#28C840"}} />
      <span style={{marginLeft: 20}}>{titulo}</span>
    </div>
    <div style={{padding: "10px 40px 40px"}}>{children}</div>
  </div>
);

const Campo: React.FC<{k: string; val: React.ReactNode}> = ({k, val}) => (
  <div style={{display: "flex", gap: 18, padding: "22px 0", borderBottom: "2px solid #E6E7EA", fontSize: 34}}>
    <span style={{color: "#8a8b90", width: 120}}>{k}</span><span style={{fontWeight: 600}}>{val}</span>
  </div>
);

const Boton: React.FC<{texto: string; activo: boolean}> = ({texto, activo}) => (
  <div style={{display: "inline-block", marginTop: 34, padding: "22px 54px", borderRadius: 18, fontSize: 38, fontWeight: 700, color: "#fff",
    background: ROSA, transform: activo ? "scale(0.94)" : undefined, boxShadow: activo ? "0 0 0 10px rgba(255,45,139,0.25)" : "none"}}>
    {texto}
  </div>
);

const Fondo: React.FC = () => <AbsoluteFill style={{backdropFilter: "blur(18px)", background: "rgba(8,15,20,0.45)"}} />;

const MailEnvio: React.FC = () => {
  const f = useCurrentFrame();
  const cuerpo = "Hola, va la campaña ajustada. Saludos.";
  const letras = Math.floor(interpolate(f, [8, 36], [0, cuerpo.length], clamp));
  const cx = interpolate(f, [40, 54], [900, 190], clamp), cy = interpolate(f, [40, 54], [1500, 1128], clamp);
  const clic = f >= 56 && f < 61;
  const vuela = interpolate(f, [62, 72], [0, 1], clamp);
  return (
    <>
      <Fondo />
      <div style={{position: "absolute", inset: 0, transform: `translateY(${-vuela * 1400}px) scale(${1 - vuela * 0.3})`, opacity: 1 - vuela}}>
        <Ventana titulo="Nuevo mensaje">
          <Campo k="Para" val="Cliente" />
          <Campo k="Asunto" val="Campaña ajustada ✓" />
          <div style={{marginTop: 22, display: "inline-flex", gap: 14, alignItems: "center", padding: "14px 22px", borderRadius: 14,
            background: "#FFE3EF", color: "#B0125E", fontSize: 30, fontWeight: 600}}>📎 campaña_V3_final.pdf</div>
          <div style={{marginTop: 26, fontSize: 34, minHeight: 90, color: "#333"}}>{cuerpo.slice(0, letras)}</div>
          <Boton texto="Enviar" activo={clic} />
        </Ventana>
      </div>
      {f >= 62 && (
        <div style={{position: "absolute", left: 0, right: 0, top: 900, textAlign: "center", fontFamily: VOZ.funcional, fontSize: 48, fontWeight: 700,
          color: "#F2F4F6", opacity: interpolate(f, [62, 68], [0, 1], clamp)}}>Enviado ✓ <span style={{color: "rgba(242,244,246,0.6)", fontWeight: 400}}>09:03</span></div>
      )}
      {vuela < 1 && <Cursor x={cx} y={cy} clic={clic} />}
    </>
  );
};

/** La respuesta: SÓLO el mensaje del cliente. Nada más en la bandeja. */
const MailRespuesta: React.FC = () => {
  const f = useCurrentFrame();
  const entra = spring({frame: f - 6, fps: 30, config: {damping: 13, stiffness: 170}});
  return (
    <>
      <Fondo />
      <div style={{position: "absolute", left: 60, right: 60, top: 640, transform: `translateY(${(1 - entra) * -80}px) scale(${0.9 + 0.1 * entra})`,
        opacity: entra, borderRadius: 30, overflow: "hidden", background: "#FBFBFC", boxShadow: "0 40px 100px rgba(0,0,0,0.65)",
        fontFamily: VOZ.funcional, color: "#1b1b1f"}}>
        <div style={{padding: "22px 30px", background: "#EDEEF1", fontSize: 26, color: "#555"}}>Recibidos · 1 nuevo</div>
        <div style={{padding: "36px 40px 44px", background: "#FFE3EF"}}>
          <div style={{display: "flex", fontSize: 32, fontWeight: 700}}><span>Cliente</span><span style={{marginLeft: "auto", fontWeight: 400, color: "#8a8b90"}}>09:04</span></div>
          <div style={{fontSize: 30, color: "#8a8b90", marginTop: 6}}>RE: Campaña ajustada ✓</div>
          <div style={{fontSize: 50, fontWeight: 700, marginTop: 18, lineHeight: 1.18}}>¡Gracias! Mejor volvamos a la versión anterior 🙏</div>
        </div>
      </div>
    </>
  );
};


// ── UN PLANO ────────────────────────────────────────────────────────────────
const Sobre: React.FC<{id: string}> = ({id}) => {
  const f = useCurrentFrame();
  if (id === "P01") return <PostIt />;
  if (id === "P04") return <TiraMarta f={f} />;
  return null;
};

const Encima: React.FC<{id: string}> = ({id}) => {
  switch (id) {
    case "P01": return <Cabecera hora="18:30" />;
    case "P02b": return <><Cabecera hora="18:30" /><Pensamiento /></>;
    case "N02": return <Pisos />;
    case "SUBE": return <Pisos sube />;
    case "N03": case "P04": case "P05": return <Cabecera hora="18:33" />;
    case "P06": case "N04": case "N05": case "N06": case "N07": return <Cabecera hora="18:36" />;
    case "T1": case "T6": case "T12": return <><RelojTrabajo id={id} /><HUD id={id} /><Codigo /></>;
    case "T4": return <><RelojTrabajo id={id} /><HUD id={id} /><Golpe texto="COPY" /></>;
    case "T8": return <><RelojTrabajo id={id} /><HUD id={id} /><Golpe texto="DISEÑO" /></>;
    case "T9": return <><RelojTrabajo id={id} /><HUD id={id} /><Mensaje de="MARTA → G" txt="V1 y V2 archivadas ✓" /></>;
    case "T11": return <><RelojTrabajo id={id} /><HUD id={id} /><Mensaje de="ROLO → G" txt="fuentes listas ✓" /></>;
    case "X1": return <><RelojTrabajo id={id} /><HUD id={id} /><Mensaje de="G → TODOS" txt="ideas al pinboard" /></>;
    case "X2": return <><RelojTrabajo id={id} /><HUD id={id} /><Mensaje de="ROLO ↔ G" txt="¡es mía! · ¡no, mía!" /></>;
    case "X3": return <><RelojTrabajo id={id} /><HUD id={id} /><Mensaje de="ROLO · G" txt="brochazo · milímetro" /></>;
    case "T14": return <><RelojTrabajo id={id} /><HUD id={id} /><Mensaje de="G → TODOS" txt="V3 · export… 98 %" /></>;
    case "LISTA": return <><Cabecera hora="05:41" /><HUD id={id} /><Sello texto="V3 LISTA ✓" /></>;
    case "N10": return <Cabecera hora="06:02" />;
    case "N11": return <><Cabecera hora="06:47" /><NotaTubo /></>;
    case "P22": return <><Cabecera hora="06:48" /><Zzz /><Dato texto="TURNO TERMINADO ✓" top={1560} /></>;
    case "N22": return <Cabecera hora="06:55" />;
    case "P17": return <Cabecera hora="09:00" />;
    case "MAIL": return <><Cabecera hora="09:03" /><MailEnvio /></>;
    case "RESP": return <><Cabecera hora="09:04" /><MailRespuesta /></>;
    case "N13": return <Cabecera hora="09:05" />;
    default: return id.startsWith("T") || id.startsWith("X") ? <><RelojTrabajo id={id} /><HUD id={id} /></> : <Cabecera />;
  }
};

const Clip: React.FC<{p: Plano}> = ({p}) => {
  const f = useCurrentFrame();
  const z = p.zoom;
  const s = z ? interpolate(f, [0, p.dur], [z.s, z.s1 ?? z.s], clamp) : 1;
  const amp = p.sacudir ? p.sacudir * Math.max(0, 1 - f / 12) : 0;
  const dx = amp * Math.sin(f * 2.3), dy = amp * Math.cos(f * 3.1);
  return (
    <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
      <div style={{position: "absolute", inset: 0, transform: `translate(${dx}px, ${dy}px) scale(${s * (amp ? 1.03 : 1)})`,
        transformOrigin: z ? `${z.x} ${z.y}` : "50% 50%"}}>
        {p.still
          ? <Img src={staticFile(`assets/gcl/cap02-v3/video/${p.clip ?? p.id}.png`)} style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover"}} />
          : <OffthreadVideo src={v(p.clip ?? p.id)} startFrom={Math.round((p.desde ?? 0) * 30)} playbackRate={p.vel ?? 1} muted
              style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover"}} />}
        <Sobre id={p.id} />
      </div>
    </AbsoluteFill>
  );
};

/** «zzz» flotando sobre Rolo dormido (P22: Rolo boca abajo en el piso, abajo a la derecha). */
const Zzz: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <>
      {[0, 1, 2].map((i) => {
        const t = ((f / 30 + i * 0.8) % 2.4) / 2.4;
        return <div key={i} style={{position: "absolute", left: 400 + t * 90, top: 1330 - t * 170, fontFamily: VOZ.mano, fontSize: 40 + i * 16,
          fontWeight: 700, color: "#F2F4F6", opacity: Math.sin(t * Math.PI), textShadow: "0 2px 12px rgba(0,0,0,0.8)",
          transform: `rotate(${-10 + t * 20}deg)`}}>z</div>;
      })}
    </>
  );
};

/** Grano de película + viñeta suave sobre los planos con humanos (les quita el brillo de render). */
const Grano: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{pointerEvents: "none"}}>
      <svg width="100%" height="100%" style={{position: "absolute", inset: 0, opacity: 0.16, mixBlendMode: "overlay"}}>
        <filter id="grano"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed={f % 7} stitchTiles="stitch" />
          <feColorMatrix type="saturate" values="0" /></filter>
        <rect width="100%" height="100%" filter="url(#grano)" />
      </svg>
      <AbsoluteFill style={{background: "radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.35) 100%)"}} />
    </AbsoluteFill>
  );
};

/** Destello de la explosión (N13). */
const BOOM_F = 16;
const Destello: React.FC = () => {
  const f = useCurrentFrame();
  return <AbsoluteFill style={{background: "#fff", opacity: interpolate(f, [BOOM_F - 1, BOOM_F, BOOM_F + 5], [0, 1, 0], clamp)}} />;
};

// ── SONIDO — un solo «mm» (Marta al recibir). Sin voces humanas, sin voz robótica en el hook. ──
type Pista = {src: string; desde: number; vol?: number; hasta?: number};
const SONIDO: Pista[] = [
  {src: fx("oficina-noche"), desde: 0, hasta: en("N02"), vol: 0.4},
  {src: fx("laptop-clac"), desde: en("P02b", 22)},
  {src: fx("tubo-baja"), desde: en("N02"), vol: 0.9},
  {src: fx("capsula-clonk"), desde: en("N03", 3)},
  {src: fx("marta-trrr"), desde: en("P04"), vol: 0.8, hasta: en("P05")},
  {src: fx("marta-mm"), desde: en("P04", 20)},                      // ← el único
  {src: fx("rolo-bips"), desde: en("P05"), vol: 0.85, hasta: en("P06", 6)},
  {src: fx("rolo-servos"), desde: en("P05"), vol: 0.7, hasta: en("P06")},
  {src: fx("g-halo-hum"), desde: en("P06", 8), vol: 0.8},
  // iluminación
  {src: fx("riser"), desde: en("N04", 4), vol: 0.8},
  {src: fx("coro-celestial"), desde: en("N05"), vol: 0.9, hasta: en("N07", 10)},
  {src: fx("datos-entran"), desde: en("N07"), vol: 0.9},
  // trabajo
  {src: fx("teclado-frenesi"), desde: en("T1"), vol: 0.7, hasta: en("T2")},
  {src: fx("g-panel-tick"), desde: en("T2", 8), vol: 1},
  {src: fx("rolo-revive"), desde: en("T2", 6), vol: 0.7},
  {src: fx("rolo-bips"), desde: en("T3"), vol: 0.5, hasta: en("T4")},
  {src: fx("g-panel-tick"), desde: en("T4"), vol: 0.9},
  {src: fx("rolo-bips"), desde: en("T5"), vol: 0.5, hasta: en("T5", 12)},
  {src: fx("g-eh"), desde: en("T5", 10), vol: 0.9},
  {src: fx("teclado-frenesi"), desde: en("T6"), vol: 0.6, hasta: en("T7")},
  {src: fx("rolo-servos"), desde: en("T7"), vol: 0.6, hasta: en("T8")},
  {src: fx("rolo-bips"), desde: en("T7", 6), vol: 0.7, hasta: en("T8")},
  {src: fx("g-glitch"), desde: en("T7", 14), vol: 0.3},
  {src: fx("g-panel-tick"), desde: en("T8"), vol: 0.9},
  {src: fx("papel"), desde: en("T9", 2), vol: 0.6},
  {src: fx("g-panel-tick"), desde: en("T9", 6), vol: 0.7},
  {src: fx("marta-trrr-largo"), desde: en("T10"), vol: 0.8, hasta: en("T11")},
  {src: fx("rolo-bips"), desde: en("T10", 8), vol: 0.6, hasta: en("T11")},
  {src: fx("papeles-caen"), desde: en("T11"), vol: 0.6},
  {src: fx("g-panel-tick"), desde: en("T11", 4), vol: 0.7},
  {src: fx("teclado-frenesi"), desde: en("T12"), vol: 0.6, hasta: en("T13")},
  // +5 s Pixar
  {src: fx("chinche"), desde: en("X1", 4), vol: 0.9},
  {src: fx("chinche"), desde: en("X1", 16), vol: 0.9},
  {src: fx("marta-trrr"), desde: en("X1", 8), vol: 0.4, hasta: en("X2")},
  {src: fx("rolo-servos"), desde: en("X2"), vol: 0.7, hasta: en("X2", 40)},
  {src: fx("rolo-bips"), desde: en("X2", 4), vol: 0.6, hasta: en("X2", 40)},
  {src: fx("g-eh"), desde: en("X2", 12), vol: 0.8},
  {src: fx("papel-rasga"), desde: en("X2", 40)},
  {src: fx("boing"), desde: en("X2", 44), vol: 0.9},
  {src: fx("rolo-clonc"), desde: en("X2", 47), vol: 0.7},
  {src: fx("brocha"), desde: en("X3", 3), vol: 0.9},
  {src: fx("g-panel-tick"), desde: en("X3", 16), vol: 0.8},
  {src: fx("g-panel-tick"), desde: en("X3", 22), vol: 0.8},
  {src: fx("teclado-frenesi"), desde: en("X4"), vol: 0.6, hasta: en("T14")},
  {src: fx("g-panel-tick"), desde: en("T14", 4), vol: 0.7},
  // V1 lista
  {src: fx("timbre-seco"), desde: en("LISTA", 2)},
  {src: fx("sting-triunfal"), desde: en("LISTA", 4)},
  {src: fx("g-risa"), desde: en("LISTA", 20), vol: 0.8},
  // sube y llega
  {src: fx("tubo-sube"), desde: en("N10", 10), vol: 0.9},
  {src: fx("tubo-sube"), desde: en("SUBE"), vol: 0.6},
  {src: fx("oficina-manana"), desde: en("N11"), hasta: en("N22"), vol: 0.35},
  {src: fx("capsula-clonk"), desde: en("N11", 4)},
  {src: fx("papel"), desde: en("N11", 12), vol: 0.6},
  // descansan
  {src: fx("g-apagado"), desde: en("P22", 2), vol: 0.5},
  {src: fx("ronquido"), desde: en("P22", 6), vol: 0.8},
  // café
  {src: fx("cafe-laptop"), desde: en("N22", 8), vol: 0.9},
  {src: fx("rolo-bips-calma"), desde: en("N22", 14), vol: 0.6},
  {src: fx("sorbo"), desde: en("N22", 40), vol: 0.9},
  // 09:00 — match cut al sorbo
  {src: fx("sorbo"), desde: en("P17", 2), vol: 0.9},
  {src: fx("oficina-manana"), desde: en("P17"), hasta: en("N13"), vol: 0.4},
  {src: fx("cafe-laptop"), desde: en("P17", 10), vol: 0.7},
  {src: fx("click-enviar"), desde: en("MAIL", 56)},
  {src: fx("whoosh"), desde: en("MAIL", 62), vol: 0.8},
  {src: fx("ding"), desde: en("RESP", 6)},
  // abajo explotan (corte directo desde la cara de Pancho)
  {src: fx("riser"), desde: en("RESP", 45), vol: 0.9},
  {src: fx("g-glitch"), desde: en("N13", 4), vol: 0.6},
  {src: fx("explosion"), desde: en("N13", BOOM_F - 1)},
];

// Música: «Reptilia» (The Strokes, instrumental) como TEMP TRACK, cortada al beat (157,9 BPM).
//   1. HOOK + TUBO: el riff del bajo solo (canción 0:00) arranca con el zoom al post-it y tictaquea bajo el
//      laptop, el pensamiento, el tubo y Marta. Bajo el coro celestial del robot dios se agacha (duck).
//   2. TRABAJO: la BATERÍA ENTRA exacto en T1 (canción 10,62 s = primer bombo) y el riff entero empuja
//      todo el montaje hasta el sello «V3 LISTA»: ahí muere seco con el sting.
//   3. CANSADO: el mismo riff del bajo, a 0,78×, sin agudos y con eco (temp-strokes-cansado.wav) mientras
//      sube, llega, duermen y brindan. Callback agotado del hook.
//   4. MAÑANA: la reentrada de la banda (canción 79,55 s, tras el break) cae en el SORBO de Pancho; Pancho
//      fresco a toda máquina… hasta que el DING del cliente la mata en seco. Silencio, riser, explosión.
//   5. CIERRE: sin música (sólo el tecleo).
const STROKES = "assets/gcl/cap02-v3/musica/temp-strokes-reptilia.wav";
const STROKES_CANSADO = "assets/gcl/cap02-v3/musica/temp-strokes-cansado.wav";
const BOMBO_1 = 10.62;                       // s de canción: primer golpe de batería
const DESDE_HOOK = en("T1") - Math.round(BOMBO_1 * 30); // el riff arranca acá para que el bombo caiga en T1
const TRAMOS_MUSICA: {src: string; desde: number; hasta: number; desdeS: number; vol: number; ini?: number; fin?: number; duck?: [number, number, number]}[] = [
  {src: STROKES, desde: DESDE_HOOK, hasta: en("LISTA", 5), desdeS: 0, vol: 0.55, ini: 6, fin: 3,
    duck: [en("N05") - DESDE_HOOK, en("T1") - DESDE_HOOK, 0.55]},
  {src: STROKES_CANSADO, desde: en("LISTA", 30), hasta: en("P17", 12), desdeS: 0, vol: 0.6, ini: 24, fin: 18},
  {src: STROKES, desde: en("P17"), hasta: en("RESP", 6), desdeS: 79.55 - 2 / 30, vol: 0.5, ini: 2, fin: 3},
];

export const Cap02TurnoDeNocheV14: React.FC = () => {
  asegurarFuentes();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      {PLANOS.map((p) => (
        <Sequence key={p.id} from={INICIO[p.id]} durationInFrames={p.dur}>
          {p.id === "CIERRE" ? <CierreSerie dur={p.dur} tagline={TAGLINE} titulo={PROXIMO} tw0={CIERRE_TW0} />
            : p.negro ? <AbsoluteFill style={{backgroundColor: "#000"}} />
            : <><Clip p={p} />{p.grano && <Grano />}<Encima id={p.id} />{p.id === "N13" && <Destello />}</>}
        </Sequence>
      ))}
      {SONIDO.map((s, i) => (
        <Sequence key={i} from={s.desde} durationInFrames={s.hasta ? s.hasta - s.desde : undefined}>
          <Audio src={s.src} volume={s.vol ?? 1} />
        </Sequence>
      ))}
      {TRAMOS_MUSICA.map((m, i) => (
        <Sequence key={`m${i}`} from={m.desde} durationInFrames={m.hasta - m.desde}>
          <Audio src={staticFile(m.src)} startFrom={Math.round(m.desdeS * 30)}
            volume={(f) => m.vol * interpolate(f, [0, m.ini ?? 8, m.hasta - m.desde - (m.fin ?? 6), m.hasta - m.desde], [0, 1, 1, 0], clamp)
              * (m.duck ? interpolate(f, [m.duck[0] - 8, m.duck[0], m.duck[1] - 4, m.duck[1]], [1, m.duck[2], m.duck[2], 1], clamp) : 1)} />
        </Sequence>
      ))}
      {Array.from({length: PROXIMO.length}).map((_, i) => (
        <Sequence key={`t${i}`} from={en("CIERRE", CIERRE_TW0 + Math.round(i * 0.088 * 30))} durationInFrames={8}>
          <Audio src={fx("g-panel-tick")} volume={0.5} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
