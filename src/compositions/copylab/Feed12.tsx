// ============================================================================
// FEED 12 — simulación de grilla del Creative Direction Board (24-09-2026)
// ----------------------------------------------------------------------------
// NO son piezas finales. Es la simulación para evaluar el SISTEMA antes de
// mandar 12 imágenes a Magnific. Cada tile es uno de dos tipos:
//   REAL    → material que ya existe (hero de la goma, dron de Tierra Calma,
//             fotograma de G.CL, spot de Santa Gota).
//   BOCETO  → valor tonal + composición + la tipografía REAL en su lugar final.
//             Las formas planas marcan dónde va la imagen de Magnific; no son
//             diseño.
// Board completo: creative-system/FEED-12/BOARD.md
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {C, asegurarFuentes, VOZ} from "../../brand/copylab/sistema";
import {Pieza, Foto, Velo} from "../../brand/copylab/lienzo";

const M = 72;
const KRAFT = "#A9855A";

const Narrow: React.FC<{
  children: React.ReactNode; size: number; color?: string; style?: React.CSSProperties;
}> = ({children, size, color = C.offwhite, style}) => (
  <div style={{
    fontFamily: VOZ.narrow, fontWeight: 700, fontSize: size, lineHeight: 0.9,
    letterSpacing: "-0.01em", textTransform: "uppercase", color, ...style,
  }}>{children}</div>
);

const Serif: React.FC<{children: React.ReactNode; size: number; color?: string; style?: React.CSSProperties}> =
  ({children, size, color = C.rosa, style}) => (
    <div style={{fontFamily: VOZ.editorial, fontStyle: "italic", fontSize: size, lineHeight: 1.02, color, ...style}}>
      {children}
    </div>
  );

const Mono: React.FC<{children: React.ReactNode; color?: string; size?: number; style?: React.CSSProperties}> =
  ({children, color = "rgba(242,244,246,0.75)", size = 22, style}) => (
    <div style={{
      fontFamily: VOZ.data, fontSize: size, lineHeight: 1.35, letterSpacing: "0.12em",
      textTransform: "uppercase", color, ...style,
    }}>{children}</div>
  );

const abs = (s: React.CSSProperties): React.CSSProperties => ({position: "absolute", ...s});

// 01 · GOMA — macro. La goma se entiende antes que la persona.
const T01 = () => (
  <Pieza fondo={C.offwhite} grano={0.14}>
    <Foto src="assets/copylab/feed12/01-goma-macro.jpg" grado="crudo" />
    <div style={abs({left: M, top: 84})}>
      <Narrow size={104}>Escribir<br />es fácil.</Narrow>
    </div>
    <Serif size={52} style={abs({left: M, bottom: 96})}>Lo difícil es saber<br />qué borrar.</Serif>
  </Pieza>
);

// 02 · NADIE LO FIRMÓ 01 — almacén de noche, cartón colgado.
const T02 = () => (
  <Pieza fondo="#0B0E10" grano={0.3}>
    <div style={abs({left: 300, top: 150, width: 560, height: 1200, background: "#3A2716"})} />
    <div style={abs({left: 330, top: 190, width: 500, height: 1160, background: "#6B4A26", opacity: 0.55})} />
    <div style={abs({left: 380, top: 560, width: 420, height: 300, background: KRAFT, transform: "rotate(-3deg)"})}>
      <div style={abs({left: 30, top: 34, fontFamily: VOZ.narrow, fontWeight: 700, fontSize: 74, lineHeight: 0.95, color: "#1A1410"})}>
        HAY PAN<br />AMASADO
      </div>
      <div style={abs({left: 160, top: -18, width: 100, height: 36, background: C.rosa, opacity: 0.92, transform: "rotate(4deg)"})} />
    </div>
    <Mono style={abs({left: M, bottom: 92})}>Nadie lo firmó · Nº01</Mono>
  </Pieza>
);

// 07 · CONCEPTO — la boleta interminable.
const BOLETA = ["RÁPIDO", "BARATO", "DE CALIDAD", "CON TRAYECTORIA", "ATENCIÓN 24/7", "INNOVADOR",
  "CERCANO", "LÍDER", "SUSTENTABLE", "PERSONALIZADO", "GARANTIZADO", "CONFIABLE", "DESPACHO GRATIS", "…"];
const T07 = () => (
  <Pieza fondo={C.offwhite} grano={0.14}>
    <div style={abs({left: 560, top: -40, width: 330, height: 1460, background: C.blanco,
      transform: "rotate(7deg)", boxShadow: "18px 22px 30px rgba(8,15,20,0.16)"})}>
      {BOLETA.map((b, i) => (
        <div key={b} style={abs({left: 34, top: 120 + i * 82, fontFamily: VOZ.data, fontSize: 25,
          letterSpacing: "0.06em", color: "#2C3136", width: 270, display: "flex", justifyContent: "space-between"})}>
          <span>{b}</span><span>1</span>
        </div>
      ))}
    </div>
    <div style={abs({left: M, top: 96})}>
      <Narrow size={112} color={C.tinta}>Tu aviso<br />no es una<br />boleta.</Narrow>
    </div>
  </Pieza>
);

// ---------------------------------------------------------------------------
// v2 — revisión de director creativo (24-09-2026). Tiles nuevos o cambiados.
// ---------------------------------------------------------------------------

// 03 · TRABAJO — Santa Gota: el cuadro real del spot, a sangre.
const V03 = () => (
  <Pieza fondo={C.tinta} grano={0.14}>
    <Foto src="assets/copylab/feed12/10-santagota-frame.jpg" grado="crudo" encuadre="60% 50%" />
    <Velo desde="abajo" fuerza={0.6} corte={0.74} />
    <Mono style={abs({left: M, bottom: 92})} color={C.offwhite}>Santa Gota<br />Spot para TVN · 2026</Mono>
  </Pieza>
);

// 05 · NADIE LO FIRMÓ Nº02 — misma propiedad, otra calle.
const V05 = () => (
  <Pieza fondo="#E7E2D8" grano={0.2}>
    <div style={abs({left: 0, top: 380, width: 1080, height: 820, background: "#B9B4AA"})} />
    <div style={abs({left: 140, top: 470, width: 800, height: 380, background: "#1E2327",
      clipPath: "polygon(8% 0, 92% 0, 100% 100%, 0 100%)"})}>
      <div style={abs({left: 150, top: 70, fontFamily: VOZ.narrow, fontWeight: 700, fontSize: 96,
        lineHeight: 0.95, color: "rgba(255,255,255,0.9)"})}>VENDO<br /><span style={{fontSize: 60}}>ÚNICO DUEÑO</span></div>
    </div>
    <Mono style={abs({left: M, bottom: 92})} color="rgba(8,15,20,0.72)">Nadie lo firmó · Nº02</Mono>
  </Pieza>
);

// 06 · REEL SEÑAL — la portada es la frase muerta, tachada.
const V06 = () => (
  <Pieza fondo={C.tinta} grano={0.26}>
    <div style={abs({left: M, top: 440})}>
      <Narrow size={150}>Calidad y<br />compromiso</Narrow>
    </div>
    <div style={abs({left: M - 14, top: 560, width: 800, height: 16, background: C.rosa, transform: "rotate(-2deg)"})} />
    <div style={abs({left: M - 14, top: 695, width: 900, height: 16, background: C.rosa, transform: "rotate(1.5deg)"})} />
    <Mono style={abs({left: M, bottom: 92})}>Reel</Mono>
  </Pieza>
);

// 07 · LA ONCE — sin servilleta: la frase es la idea.
const V07 = () => (
  <Pieza fondo="#1B1510" grano={0.3}>
    <div style={abs({left: 60, top: 420, width: 960, height: 900, background: "#5B3A26"})} />
    {[[180, 520], [760, 560], [240, 1030], [790, 1060], [480, 800]].map(([x, y], i) => (
      <div key={i} style={abs({left: x, top: y, width: 150, height: 150, borderRadius: "50%", background: "#E8E1D4"})} />
    ))}
    {[[420, 480], [520, 1150], [640, 700]].map(([x, y], i) => (
      <div key={i} style={abs({left: x, top: y, width: 190, height: 110, borderRadius: "45%", background: "#C69A5C"})} />
    ))}
    <div style={abs({left: M, top: 90})}>
      <Narrow size={92}>Si no llega a la once,<br />no llegó.</Narrow>
    </div>
  </Pieza>
);

// 08 · LO FIRMÓ — la persona detrás del cartón Nº01 (retrato real).
const V08 = () => (
  <Pieza fondo="#101315" grano={0.36}>
    <div style={abs({left: 330, top: 330, width: 420, height: 1020, background: "#2A2E31"})} />
    <div style={abs({left: 420, top: 190, width: 240, height: 260, borderRadius: "50%", background: "#2A2E31"})} />
    <div style={abs({left: 560, top: 760, width: 330, height: 230, background: KRAFT, transform: "rotate(-3deg)"})} />
    <div style={abs({left: M, top: 96})}>
      <Narrow size={112}>Lo firmó</Narrow>
      <Serif size={60} style={{marginTop: 18}}>[nombre real].</Serif>
    </div>
    <Mono style={abs({left: M, bottom: 92})}>Nadie lo firmó · Nº01</Mono>
  </Pieza>
);

// 09 · TRABAJO — Tierra Calma, reel de bienvenida.
const V09 = () => (
  <Pieza fondo={C.tinta} grano={0.12}>
    <Foto src="assets/copylab/feed12/03-tierracalma.jpg" grado="crudo" zoom={1.05} />
    <Velo desde="abajo" fuerza={0.55} corte={0.78} />
    <Mono style={abs({left: M, bottom: 92})} color={C.offwhite}>Tierra Calma<br />Reel de bienvenida</Mono>
  </Pieza>
);

// 10 · LA MESA — personas (foto real del equipo; el tile usa placeholder).
const V10 = () => (
  <Pieza fondo={C.tinta} grano={0.4}>
    <Foto src="assets/copylab/people/escritorio-01.png" grado="flash" zoom={1.1} />
    <Velo desde="arriba" fuerza={0.9} corte={0.62} />
    <div style={abs({left: M, top: 90})}>
      <Narrow size={104}>Acá no hay<br />un genio.</Narrow>
      <Serif size={60} style={{marginTop: 18}}>Hay una mesa.</Serif>
    </div>
  </Pieza>
);

// 11 · NADIE LO FIRMÓ Nº03 — en reel (cartón + sonido de la calle).
const V11 = () => (
  <Pieza fondo="#6E7479" grano={0.26}>
    {Array.from({length: 26}).map((_, i) => (
      <div key={i} style={abs({left: 0, top: i * 52, width: 1080, height: 4, background: "rgba(0,0,0,0.25)"})} />
    ))}
    <div style={abs({left: 200, top: 520, width: 640, height: 330, background: C.blanco, transform: "rotate(2deg)"})}>
      <div style={abs({left: 40, top: 50, fontFamily: VOZ.narrow, fontWeight: 700, fontSize: 92, lineHeight: 0.95, color: "#1A1410"})}>
        SE HACEN<br />LLAVES
      </div>
    </div>
    <Mono style={abs({left: M, bottom: 92})} color={C.offwhite}>Nadie lo firmó · Nº03 · Reel</Mono>
  </Pieza>
);

// 12 · EL TIMBRE — el botón que nadie ha apretado.
const V12 = () => (
  <Pieza fondo="#2B2A27" grano={0.3}>
    <div style={abs({left: 230, top: 420, width: 620, height: 860, background: "#8C8A84"})} />
    {Array.from({length: 7}).map((_, i) => (
      <React.Fragment key={i}>
        <div style={abs({left: 290, top: 470 + i * 112, width: 380, height: 70, background: i === 3 ? "#F1EDE4" : "#D9D4C8"})}>
          {i === 3 ? <div style={abs({left: 16, top: 20, fontFamily: VOZ.data, fontSize: 22, letterSpacing: "0.04em", color: "#222"})}>SOLUCIONES INTEGRALES</div> : null}
        </div>
        <div style={abs({left: 700, top: 475 + i * 112, width: 60, height: 60, borderRadius: "50%",
          background: i === 3 ? "#E9D9A0" : "#5E5A52"})} />
      </React.Fragment>
    ))}
    <div style={abs({left: M, top: 96})}>
      <Narrow size={104}>Nadie toca<br />este timbre.</Narrow>
    </div>
  </Pieza>
);

const TILES = [T01, T02, V03, T07, V05, V06, V07, V08, V09, V10, V11, V12];

export const Feed12: React.FC<{n: number}> = ({n}) => {
  asegurarFuentes();
  const T = TILES[Math.max(1, Math.min(12, n)) - 1];
  return <AbsoluteFill><T /></AbsoluteFill>;
};
