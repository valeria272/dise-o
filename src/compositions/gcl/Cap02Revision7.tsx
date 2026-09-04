// ============================================================================
// G.CL · CAPÍTULO 02 — «REVISIÓN 7»
// ROUGH CUT · 584 frames · 19,47 s · 30 fps · 1080×1920 · rejilla 112,5 BPM
// ----------------------------------------------------------------------------
// ESTO ES UN ROUGH CUT. Existe para contestar UNA pregunta: ¿el episodio
// entretiene? Por eso está entero —los 8 planos, la música, los SFX y todo el
// texto— y por eso NO está pulido. Lo que falte se arregla después de la
// aprobación, no antes (instrucción de producción del 04-09-2026).
//
// LA REGLA DE ESTE MONTAJE
//   Ningún plano es una pieza suelta. Es UNA escena continua: mismo G, misma
//   escala, mismo escritorio, misma luz, misma óptica, misma geografía. Los
//   cortes son POR ACCIÓN, nunca por transición. No hay zoom, ni glitch, ni
//   efecto que no esté en `07_MONTAJE.md`.
//
//   El ritmo lo construye el MONTAJE, no G. Él se mueve lento, seco y preciso
//   mientras el mundo se acelera alrededor. Por eso ningún clip va acelerado:
//   cada plano corre a velocidad real y lo que cambia es cuánto dura.
//
// DE DÓNDE SALE CADA PLANO
//   cut01     KF01 → KF02   kling-v2-1-pro con `image_tail`
//   cut02     KF03 → KF04   idem — los dos keyframes se regeneraron el 04-09
//                            para sacarle los audífonos humanos del casco (v4)
//   cut05a    KF08 → KF07   generado HACIA ADELANTE (la física real es que las
//   cut05b    KF09 → KF08   cosas caen) y **invertido** con invertir-clip.sh
//   cut06     KF09 → KF10   el plano más importante: 28 frames sin nada
//
//   El frame final (`image_tail`) es lo que hace que esto sea una escena y no
//   ocho clips: 05A TERMINA en el frame donde 05B EMPIEZA. La continuidad es
//   física, no de montaje.
//
// LO QUE NO SE GENERA (y por eso no puede derivar): pantalla, botón, cursor,
// los 7 mensajes, la placa, el contador de versiones y todo el CUT 07.
// ============================================================================
import React from "react";
import {
  AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate,
  staticFile, useCurrentFrame,
} from "remotion";
import {C, VOZ, asegurarFuentes, ancho} from "../../brand/copylab/sistema";
import {Grano} from "../../brand/copylab/lienzo";
import {Tachado} from "../../brand/copylab/mano";

/** Un trazo a mano no aparece: se DIBUJA. `Tachado` no tiene progreso propio,
 *  así que se revela de izquierda a derecha con un clip-path. */
const Revelado: React.FC<{p: number; children: React.ReactNode}> = ({p, children}) => (
  <div style={{
    position: "absolute", inset: 0,
    clipPath: `inset(0 ${(1 - p) * 100}% 0 0)`,
  }}>
    {children}
  </div>
);

const ROSA = C.rosa;          // #FF2D8D — la firma
const TINTA = C.tinta;        // #080F14

const v = (n: string) => staticFile(`assets/gcl/cap02/${n}`);

// ── Utilidades ──────────────────────────────────────────────────────────────
/** Un plano recortado: empieza en el segundo `desdeS` del clip. */
const Clip: React.FC<{src: string; desdeS: number; escala?: number}> = ({
  src, desdeS, escala = 1,
}) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
      <OffthreadVideo
        src={v(src)}
        startFrom={Math.round(desdeS * 30)}
        muted
        style={{
          position: "absolute", width: "100%", height: "100%",
          objectFit: "cover",
          transform: `scale(${escala})`,
          opacity: frame < 0 ? 0 : 1,
        }}
      />
    </AbsoluteFill>
  );
};

const Fija: React.FC<{src: string; escala?: number}> = ({src, escala = 1}) => (
  <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
    <Img
      src={v(src)}
      style={{
        position: "absolute", width: "100%", height: "100%",
        objectFit: "cover", transform: `scale(${escala})`,
      }}
    />
  </AbsoluteFill>
);

// ════════════════════════════════════════════════════════════════════════════
// OPENING · f.0–15 · LA FIRMA DE LA SERIE
// ----------------------------------------------------------------------------
// Sólo existe el visor. Ni logo, ni placa corporativa, ni nombre de la agencia:
// la cara de G ES el identificador (decisión v4, cambio 3). Es lo único
// permanente de la serie junto con el PING — por eso está fuera de tempo.
// ════════════════════════════════════════════════════════════════════════════
const PUNTOS_G = [
  "..#####..", ".##...##.", "##.......", "##.......", "##..####.",
  "##....##.", ".##...##.", "..#####..",
];

const Boot: React.FC = () => {
  const f = useCurrentFrame();
  const paso = 3.2;   // los puntos encajan de a poco
  return (
    <AbsoluteFill style={{backgroundColor: "#000", justifyContent: "center", alignItems: "center"}}>
      <div style={{
        display: "grid",
        gridTemplateColumns: `repeat(9, 26px)`,
        gridTemplateRows: `repeat(8, 26px)`,
        gap: 8,
        filter: `blur(${interpolate(f, [0, 12], [7, 0], {extrapolateRight: "clamp"})}px)`,
      }}>
        {PUNTOS_G.flatMap((fila, y) =>
          fila.split("").map((c, x) => {
            const orden = (y * 9 + x) * 0.11;
            const on = c === "#" && f > orden * paso;
            return (
              <div key={`${x}-${y}`} style={{
                width: 26, height: 26, borderRadius: "50%",
                backgroundColor: on ? ROSA : "rgba(255,45,141,0.05)",
                boxShadow: on ? `0 0 22px ${ROSA}` : "none",
                opacity: on ? interpolate(f, [0, 14], [0.7, 1], {extrapolateRight: "clamp"}) : 1,
              }} />
            );
          }),
        )}
      </div>
    </AbsoluteFill>
  );
};

// ════════════════════════════════════════════════════════════════════════════
// CUT 01 · f.16–79 · LA PANTALLA
// ----------------------------------------------------------------------------
// El plano dura 64 frames y no menos: el cursor tiene que ir LENTO. La lentitud
// es lo que hace creer que terminó de verdad. El click cae en el f.64 (48 de
// este bloque) y el corte al 02 es POR ACCIÓN sobre ese click, que queda
// apretado — el botón nunca se ve volver a subir.
// ════════════════════════════════════════════════════════════════════════════
const Pantalla: React.FC = () => {
  const f = useCurrentFrame();
  const CLICK = 48;                                    // f.64 absoluto
  const encima = f >= 44;
  const apretado = f >= CLICK;
  // El cursor va de la izquierda al botón y SE QUEDA ahí: el corte al 02 es por
  // acción sobre el click, así que nunca se ve el botón volver a subir.
  const cx = interpolate(f, [2, 30, 43], [9, 40, 47], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp",
  });
  // El archivo se va en el f.70 (22 de este bloque + 48). Sin eso, «mandó el
  // archivo» hay que creerlo; con eso, se ve.
  const vuelo = interpolate(f, [54, 66], [0, 1], {
    extrapolateLeft: "clamp", extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{perspective: 1500, pointerEvents: "none"}}>
      <div style={{
        position: "absolute", left: "29%", top: "26%", width: "70%", height: "37%",
        transform: "rotateY(-13deg) skewY(2.6deg)", transformOrigin: "left center",
        fontFamily: VOZ.data, color: "#e4ebf2",
      }}>
        <div style={{position: "absolute", left: "4%", top: "6%", fontSize: 26,
          letterSpacing: 2, opacity: 0.42}}>
          PARA: CLIENTE
        </div>
        <div style={{
          position: "absolute", left: "4%", top: "20%",
          display: "inline-flex", alignItems: "center", gap: 14,
          border: "2px solid rgba(228,235,242,0.30)", borderRadius: 5,
          padding: "13px 20px", fontSize: 31, letterSpacing: 0.2,
          opacity: 1 - vuelo,
          transform: `translate(${vuelo * 260}px, ${-vuelo * 130}px) scale(${1 - vuelo * 0.25})`,
        }}>
          <span style={{opacity: 0.5}}>▤</span>
          REVISION_07_FINAL_FINAL.pdf
        </div>
        <div style={{
          position: "absolute", left: "4%", top: "58%",
          padding: "20px 54px",
          fontFamily: VOZ.impacto, fontVariationSettings: ancho(104, 800),
          fontSize: 38, letterSpacing: 1.5,
          color: encima ? "#080F14" : "#cfd8e2",
          backgroundColor: encima ? ROSA : "rgba(228,235,242,0.13)",
          boxShadow: encima && !apretado ? `0 0 52px ${ROSA}77` : "none",
          transform: apretado ? "translateY(4px) scale(0.982)" : "none",
        }}>
          ENVIAR
        </div>
        <div style={{
          position: "absolute", left: `${cx}%`, top: "62%",
          filter: "drop-shadow(0 3px 6px rgba(0,0,0,0.95))",
          transform: apretado ? "scale(0.88)" : "scale(1)",
        }}>
          <svg width="36" height="49" viewBox="0 0 34 46">
            <path d="M2 2 L2 34 L11 26 L17 40 L23 37 L17 24 L28 24 Z"
              fill="#fff" stroke="#111" strokeWidth="2" strokeLinejoin="round" />
          </svg>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ════════════════════════════════════════════════════════════════════════════
// BLOQUE 03 · f.144–247 · LOS MENSAJES
// ----------------------------------------------------------------------------
// El chiste no lo hace G: lo hace el MONTAJE. La rampa 32→16→12→12→8→8→4→4→4→4
// alterna DOS planos que ya existen y no cuesta una generación más. Y G no
// reacciona en ninguno: ni un grado. Cuanto menos reacciona, más gracioso es.
// ════════════════════════════════════════════════════════════════════════════
const MENSAJES = [
  {f: 146, t: "Nos encantó 🙌"},
  {f: 194, t: "Solo una cosita…"},
  {f: 218, t: "El logo un poquito más grande"},
  {f: 234, t: "Y el azul un poco más azul"},
  {f: 242, t: "Perdón, última cosa"},
  {f: 246, t: "Lo vio la gerencia"},
  {f: 250, t: "¿Podemos volver a la primera?"},
];

/** Los mensajes van SOBRE el teléfono del plano, en su perspectiva. */
const Telefono: React.FC<{desde: number}> = ({desde}) => {
  const f = useCurrentFrame() + desde;      // ⚠️ frame ABSOLUTO, no el de la Sequence
  const visibles = MENSAJES.filter((m) => m.f <= f).slice(-4);
  return (
    <AbsoluteFill style={{pointerEvents: "none"}}>
      <div style={{
        position: "absolute", left: "11%", top: "60.5%", width: "80%",
        transform: "rotate(5.5deg) skewX(-7deg)", transformOrigin: "left top",
        display: "flex", flexDirection: "column", gap: 14,
      }}>
        {visibles.map((m) => {
          const edad = f - m.f;
          return (
            <div key={m.f} style={{
              alignSelf: "flex-start", maxWidth: "94%",
              backgroundColor: "#e9eef3", color: "#10151b",
              borderRadius: "20px 20px 20px 5px",
              padding: "17px 26px", fontFamily: VOZ.data, fontSize: 34,
              lineHeight: 1.25, letterSpacing: -0.2,
              opacity: interpolate(edad, [0, 3], [0, 1], {extrapolateRight: "clamp"}),
              transform: `translateY(${interpolate(edad, [0, 4], [10, 0], {extrapolateRight: "clamp"})}px)`,
              boxShadow: "0 6px 26px rgba(0,0,0,0.5)",
            }}>
              {m.t}
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

// ════════════════════════════════════════════════════════════════════════════
// TÍTULO · f.272–303 · el DROP cae exacto en el downbeat
// ----------------------------------------------------------------------------
// Sin transición visual. El golpe ES el puente: se pasa de la sentencia al
// colapso por un corte seco y un sub-bass, no por un fundido.
// ════════════════════════════════════════════════════════════════════════════
const Placa: React.FC<{segunda: string}> = ({segunda}) => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{
      backgroundColor: TINTA, justifyContent: "center", alignItems: "flex-start",
      opacity: interpolate(f, [0, 3], [0, 1], {extrapolateRight: "clamp"}),
    }}>
      <div style={{width: "84%", marginLeft: "8%"}}>
        <div style={{
          fontFamily: VOZ.impacto, fontVariationSettings: ancho(78, 900),
          fontSize: 168, lineHeight: 0.9, color: C.blanco, letterSpacing: -3,
        }}>
          REVISIÓN 7.
        </div>
        <div style={{
          marginTop: 26, fontFamily: VOZ.editorial, fontStyle: "italic",
          fontSize: 76, lineHeight: 1.1, color: ROSA,
        }}>
          {segunda}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ════════════════════════════════════════════════════════════════════════════
// CUT 05 · el contador de versiones. NO se genera: se compone, para que se lea.
// ════════════════════════════════════════════════════════════════════════════
const Contador: React.FC = () => {
  const f = useCurrentFrame();
  const i = Math.min(6, Math.floor(f / 8));
  const n = 7 - i;
  return (
    <AbsoluteFill style={{pointerEvents: "none"}}>
      <div style={{
        position: "absolute", right: 74, top: 168, textAlign: "right",
        fontFamily: VOZ.data, color: ROSA, opacity: 0.92,
      }}>
        <div style={{fontSize: 24, letterSpacing: 3, opacity: 0.65}}>VERSIÓN</div>
        <div style={{
          fontFamily: VOZ.impacto, fontVariationSettings: ancho(72, 900),
          fontSize: 168, lineHeight: 0.86, textShadow: `0 0 40px ${ROSA}66`,
        }}>
          {String(n).padStart(2, "0")}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ════════════════════════════════════════════════════════════════════════════
// CUT 07 · f.480–559 · EL REMATE · 100 % Remotion
// ----------------------------------------------------------------------------
// El remate NO es de G, es del guion. Él ya no reacciona: se apagó en el 06.
// Un solo gesto a mano: tacha el 7 y escribe el 1. Mismas palabras que la placa
// del cliente, sentido opuesto — el cliente tenía razón y ésa es la desgracia.
// ════════════════════════════════════════════════════════════════════════════
const Remate: React.FC = () => {
  const f = useCurrentFrame();
  // El bloque son 80 frames y no se toca. Lo que se corrigió el 04-09 es CUÁNDO
  // pasa cada cosa dentro: antes el tachón llegaba en el f.536 y el 1 en el
  // f.548, o sea el remate del capítulo aparecía 4 frames antes del corte y no
  // se alcanzaba a leer. Ahora la corrección se adelanta 22 frames y quedan
  // 22 frames —0,73 s— para SENTARSE sobre «REVISIÓN 1.». Ése es el chiste.
  const g = (a: number, b: number) =>
    interpolate(f, [a, b], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const titulo = g(8, 20);      // f.488 — entra la misma placa del cliente
  const bajada = g(22, 34);     // f.502 — y la frase que le da vuelta el sentido
  const tach = g(38, 50);       // f.518 — el lápiz tacha el 7  ← SFX en el f.515
  const uno = g(50, 58);        // f.530 — y escribe el 1
  return (
    <AbsoluteFill style={{backgroundColor: TINTA, justifyContent: "center", alignItems: "flex-start"}}>
      <div style={{width: "84%", marginLeft: "8%"}}>
        <div style={{position: "relative", display: "inline-block", opacity: titulo}}>
          <div style={{
            fontFamily: VOZ.impacto, fontVariationSettings: ancho(78, 900),
            fontSize: 168, lineHeight: 0.9, color: C.blanco, letterSpacing: -3,
          }}>
            REVISIÓN 7.
          </div>
          {/* el 1 escrito arriba, como se corrige en un papel de verdad */}
          <div style={{
            position: "absolute", left: 736, top: -166,
            fontFamily: VOZ.mano, fontSize: 176, color: ROSA, lineHeight: 1,
            opacity: uno, transform: `rotate(-9deg) translateY(${(1 - uno) * 16}px)`,
          }}>
            1
          </div>
          {/* y el tachón encima del 7, sólo del 7 */}
          <Revelado p={tach}>
            <Tachado x={716} y={42} w={132} color={ROSA} grosor={14} semilla={2} angulo={-11} />
          </Revelado>
        </div>
        <div style={{
          marginTop: 26, fontFamily: VOZ.editorial, fontStyle: "italic",
          fontSize: 76, lineHeight: 1.12, color: C.offwhite, opacity: bajada,
        }}>
          La buena era la primera.
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ════════════════════════════════════════════════════════════════════════════
// EL MONTAJE
// ----------------------------------------------------------------------------
// La síncopa: 16 · 64 · 64 · 32 · 16 · 12 · 12 · 8 · 8 · 4 · 4 · 4 · 4 · 24 ·
// 32 · 64 · 64 · 48 · 80 · 24.  De 4 frames a 80. Relación 20:1.
// ════════════════════════════════════════════════════════════════════════════
export const Cap02Revision7: React.FC = () => {
  asegurarFuentes();
  const f = useCurrentFrame();

  // La rampa del bloque 03 alterna dos planos que ya existen.
  const RAMPA: Array<[number, number, "D" | "B"]> = [
    [144, 32, "D"], [176, 16, "B"], [192, 12, "D"], [204, 12, "B"],
    [216, 8, "D"], [224, 8, "B"], [232, 4, "D"], [236, 4, "B"],
    [240, 4, "D"], [244, 4, "B"],
  ];

  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Audio src={v("audio_rough.wav")} />

      {/* ── OPENING · firma de serie · fuera de tempo ─────────────────── */}
      <Sequence from={0} durationInFrames={16}><Boot /></Sequence>

      {/* ── CUT 01 · normalidad · SILENCIO ────────────────────────────── */}
      <Sequence from={16} durationInFrames={64}>
        <Clip src="cut01.mp4" desdeS={0.15} />
        <Pantalla />
      </Sequence>

      {/* ── CUT 02 · alivio · entra el beat en el downbeat del f.80 ────── */}
      {/* Arranca en 1,60 s del clip y los beats caen donde dice el guion:
          taza en el f.116 (36 dentro del plano) · se queda quieto · y en el
          f.136 —con el PING— la cabeza BAJA hacia el teléfono. Sólo la cabeza:
          el torso no gira. A velocidad real: G nunca se acelera. */}
      <Sequence from={80} durationInFrames={64}>
        <Clip src="cut02.mp4" desdeS={1.60} />
      </Sequence>

      {/* ── BLOQUE 03 · la escalada · G no reacciona ni un grado ───────── */}
      {RAMPA.map(([desde, dur, cam]) => (
        <Sequence key={desde} from={desde} durationInFrames={dur}>
          {cam === "D" ? <Fija src="KF05_c3.jpg" /> : <Fija src="cut02_freeze.png" />}
          {cam === "D" ? <Telefono desde={desde} /> : null}
        </Sequence>
      ))}

      {/* ── CUT 04 · la sentencia · EL HUECO. 24 frames sin nada ───────── */}
      <Sequence from={248} durationInFrames={24}>
        <Fija src="KF05_c3.jpg" escala={1.04} />
        <Telefono desde={248} />
      </Sequence>

      {/* ── TÍTULO · el drop, exacto en el downbeat del f.272 ──────────── */}
      <Sequence from={272} durationInFrames={32}>
        <Placa segunda="«Volvamos a la primera»." />
      </Sequence>

      {/* ── CUT 05A · el mundo retrocede. Clip invertido ───────────────── */}
      {/* Entra de espaldas en el f.344 = 40 frames dentro del plano. */}
      <Sequence from={304} durationInFrames={64}>
        <Clip src="cut05a.mp4" desdeS={2.57} />
        <Contador />
      </Sequence>

      {/* ── CUT 05B · cae en la silla · el ÚNICO movimiento de cámara ──── */}
      {/* ENLACE DURO: el último frame ES el primero del CUT 06. */}
      <Sequence from={368} durationInFrames={64}>
        <Clip src="cut05b.mp4" desdeS={2.60} />
      </Sequence>

      {/* ── CUT 06 · DEAD INSIDE · silencio absoluto ───────────────────── */}
      {/* 28 frames en que no pasa NADA. Es el plano más importante de la
          interpretación: la quietud es actuación. */}
      <Sequence from={432} durationInFrames={48}>
        <Clip src="cut06.mp4" desdeS={1.97} />
      </Sequence>

      {/* ── CUT 07 · el remate · negro ─────────────────────────────────── */}
      <Sequence from={480} durationInFrames={80}><Remate /></Sequence>

      {/* ── CUT 09 · post-gag · llega el PING y NO reacciona ───────────── */}
      <Sequence from={560} durationInFrames={24}>
        <Fija src="KF09_master_frontal.jpg" />
      </Sequence>

      {/* Grano: es lo único que se le suma a todo. Un frame quieto sin grano
          se lee como una foto pegada, no como un plano. */}
      <Grano op={0.05} />
      {f >= 584 ? <AbsoluteFill style={{backgroundColor: "#000"}} /> : null}
    </AbsoluteFill>
  );
};
