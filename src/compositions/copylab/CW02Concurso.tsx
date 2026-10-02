// ============================================================================
// COPYWRITERS · CW-02 — «+3.627 NUEVOS SEGUIDORES.» · CASO 002 · 8 láminas
// ----------------------------------------------------------------------------
// RONDA 3   Valeria (02-10): «tú inventas lineamientos y no te queda tal cual el
//           manual del sistema. Te adjunto la imagen para que hagas EXACTAMENTE
//           esto, que copies cada slide y diseñes tal cual».
//           → LA REFERENCIA MANDA: creative-system/SISTEMA-VISUAL-2609/reference/
//             CW02_REFERENCIA_VALERIA_02-10.png (8 slides). Cada posición y cuerpo
//             de esta pieza se MIDIÓ sobre esa lámina (slide de 382 px → 1080, con
//             35 px recortados arriba y abajo para pasar de ~3:4 a 4:5).
//           · Titulares en Bebas Neue Pro de ancho NORMAL y Bold (así está en la
//             referencia), Balloon en rosa, cinta rosa con Balloon negro, trazos.
// DESVÍOS   Sólo dos, por honestidad del caso, avisados a Valeria:
//           1. Lámina 5: los comentarios de la referencia traen nombres, fotos y
//              frases inventadas. Acá van DIFUMINADOS (se lee la avalancha, no se
//              inventa a nadie). Si llegan capturas reales del post, se montan.
//           2. Lámina 7, tarjeta 03: la referencia trae una cara sonriente generada.
//              Acá la persona va de espaldas, como el resto de la gente de la pieza.
// ⛔ MARCA   NO se nombra («un strip center de Santiago»): sin KV, logo ni mascota.
// CIFRAS    Dashboard del concurso (corte 01-10-2026): 15.616 → 19.243 = +3.627 ·
//           meta 18.000 el 16-09, 12 días antes del cierre · 35.224 vs 10.605 =
//           3,3x · 328.492 cuentas, 323.731 no seguidores = 98 %.
//           ⚠️ «3 ACTIVACIONES SEMANALES» y «teaser / sorteo principal / último
//           impulso» vienen de la referencia de Valeria: el dato verificado es
//           «3 sorteos semanales». Se deja como ella lo escribió.
// FOTOS     Seedream 5 Pro, raw/copywriters/202610/gen/m1–m8: mall, gente de
//           espaldas o desenfocada, sin caras reconocibles, sin marcas.
// Formato 1080×1350.
// ============================================================================
import React from "react";
import {AbsoluteFill, Easing, Img, OffthreadVideo, interpolate, staticFile, useCurrentFrame} from "remotion";
import {C2, VOZ2, SOMBRA_SOBRE_FOTO, asegurarFuentesV2, granoSVG} from "../../brand/copylab/sistemaV2";
import {Flecha, Trazo} from "../../brand/copylab/piezasV2";

export const CW02_FRAMES = 150; // la lámina 1 es video (5 s); el resto se exporta como PNG
const A = (n: string) => `assets/copywriters/202610/${n}`;
const TINTA = "#141313";

// ---------------------------------------------------------------- utilidades
/** Bebas por ALTURA DE MAYÚSCULA medida en la referencia: `cap` en px y
 *  `top` = donde empieza la mayúscula. Bebas Neue Pro: cap ≈ 0,70 em. */
const B: React.FC<{
  x: number; top: number; cap: number; peso?: number; color?: string; tracking?: number;
  italica?: boolean; sombra?: boolean; children: React.ReactNode;
}> = ({x, top, cap, peso = 700, color = C2.offwhite, tracking = 0, italica = false,
       sombra = true, children}) => {
  const px = cap / 0.7;
  return (
    <div style={{
      // Offset MEDIDO sobre el render (la mayúscula caía 24 px bajo lo pedido).
      position: "absolute", left: x, top: top - px * 0.19,
      fontFamily: VOZ2.titular, fontWeight: peso, fontSize: px, lineHeight: 1,
      color, letterSpacing: tracking, whiteSpace: "nowrap", textTransform: "uppercase",
      // La referencia es más pesada que la Bold de ancho normal (no hay ExtraBold de
      // ancho normal en Adobe): se engrosa con un contorno del mismo color.
      WebkitTextStroke: peso >= 700 ? `${px * 0.038}px ${color}` : undefined,
      paintOrder: "stroke fill",
      textShadow: sombra ? SOMBRA_SOBRE_FOTO : undefined,
      transform: italica ? "skewX(-11deg)" : undefined, transformOrigin: "left bottom",
    }}>{children}</div>
  );
};

/** Balloon por altura de mayúscula, girado. */
const Bal: React.FC<{
  x: number; top: number; cap: number; giro?: number; color?: string; sombra?: boolean;
  li?: number; children: React.ReactNode;
}> = ({x, top, cap, giro = -6, color = C2.rosa, sombra = true, li = 1.05, children}) => {
  // Calibrado contra la referencia: con D Extra Bold el ancho salía 17 % mayor.
  const px = (cap / 0.72) * 0.92;
  return (
    <div style={{
      // Offset MEDIDO sobre el render: Balloon quedaba 0,39 × cap por encima.
      position: "absolute", left: x, top: top + px * 0.14,
      // D Extra Bold: la Bold de Balloon sale hueca y delgada al lado de la referencia.
      fontFamily: VOZ2.mano, fontWeight: 800, fontSize: px, lineHeight: li, color,
      textTransform: "uppercase", whiteSpace: "nowrap",
      transform: `rotate(${giro}deg)`, transformOrigin: "left bottom",
      textShadow: sombra ? SOMBRA_SOBRE_FOTO : undefined,
    }}>{children}</div>
  );
};

/** Foto a sangre con desplazamiento/zoom (para calzar con la referencia). */
const Fondo: React.FC<{src: string; tx?: number; ty?: number; zoom?: number; ox?: number; oy?: number;
                       filtro?: string}> =
({src, tx = 0, ty = 0, zoom = 1, ox = 540, oy = 675, filtro}) => (
  <AbsoluteFill style={{transform: `translate(${tx}px, ${ty}px) scale(${zoom})`,
                        transformOrigin: `${ox}px ${oy}px`, filter: filtro}}>
    <Img src={staticFile(A(src))}
         style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover"}} />
  </AbsoluteFill>
);

const Velo: React.FC<{css: string}> = ({css}) => <AbsoluteFill style={{background: css}} />;
const Grano: React.FC = () => (
  <AbsoluteFill style={{backgroundImage: granoSVG(0.05, 5), backgroundSize: "300px 300px"}} />
);

/** Homografía: lleva un rectángulo w×h a las 4 esquinas medidas (CSS matrix3d). */
const homografia = (w: number, h: number, q: [number, number][]) => {
  const src: [number, number][] = [[0, 0], [w, 0], [w, h], [0, h]];
  const M: number[][] = []; const v: number[] = [];
  src.forEach(([x, y], i) => {
    const [u, w2] = q[i];
    M.push([x, y, 1, 0, 0, 0, -u * x, -u * y]); v.push(u);
    M.push([0, 0, 0, x, y, 1, -w2 * x, -w2 * y]); v.push(w2);
  });
  // Eliminación gaussiana 8×8.
  const n = 8;
  for (let i = 0; i < n; i++) {
    let p = i;
    for (let r = i + 1; r < n; r++) if (Math.abs(M[r][i]) > Math.abs(M[p][i])) p = r;
    [M[i], M[p]] = [M[p], M[i]]; [v[i], v[p]] = [v[p], v[i]];
    for (let r = i + 1; r < n; r++) {
      const k = M[r][i] / M[i][i];
      for (let c = i; c < n; c++) M[r][c] -= k * M[i][c];
      v[r] -= k * v[i];
    }
  }
  const s = new Array(n).fill(0);
  for (let i = n - 1; i >= 0; i--) {
    let acc = v[i];
    for (let c = i + 1; c < n; c++) acc -= M[i][c] * s[c];
    s[i] = acc / M[i][i];
  }
  const [a, b, c, d, e, f, g, hh] = s;
  return `matrix3d(${a},${d},0,${g},${b},${e},0,${hh},0,0,1,0,${c},${f},0,1)`;
};

/** Barra de estado y chrome mínimo de una pantalla de teléfono. */
const Estado: React.FC<{oscuro?: boolean}> = ({oscuro = false}) => {
  const c = oscuro ? "#fff" : "#111";
  return (
    <div style={{position: "absolute", left: 0, right: 0, top: 0, height: 44, display: "flex",
                 alignItems: "center", justifyContent: "space-between", padding: "0 26px",
                 fontFamily: VOZ2.cuerpo, fontWeight: 700, fontSize: 17, color: c}}>
      <span>11:24</span>
      <svg width={58} height={14} viewBox="0 0 58 14">
        {[0, 1, 2, 3].map((i) => <rect key={i} x={i * 5} y={10 - i * 3} width={3.4} height={4 + i * 3} rx={1} fill={c} />)}
        <path d="M27 6 a9 9 0 0 1 12 0 M29.5 8.6 a5.5 5.5 0 0 1 7 0" stroke={c} strokeWidth={1.8} fill="none" />
        <circle cx={33} cy={11.2} r={1.4} fill={c} />
        <rect x={42} y={2} width={13} height={9} rx={2.5} stroke={c} strokeWidth={1.2} fill="none" />
        <rect x={43.6} y={3.6} width={9} height={5.8} rx={1.4} fill={c} />
      </svg>
    </div>
  );
};

// ====================== 01 · +3.627 NUEVOS SEGUIDORES (video) ======================
// Video: Kling 2.5 Pro desde m1 (ella se aleja de espaldas, el mall se mueve).
// El texto entra en secuencia: cifra → «NUEVOS SEGUIDORES.» → la cinta se pinta
// de izquierda a derecha → «EN 28 DÍAS.» se escribe encima.
const fijo = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;
const L1: React.FC = () => {
  const f = useCurrentFrame();
  const entra = (d: number) => interpolate(f, [d, d + 12], [0, 1], {...fijo, easing: Easing.out(Easing.cubic)});
  const sube = (d: number) => ({opacity: entra(d), transform: `translateY(${(1 - entra(d)) * 30}px)`});
  const cinta = interpolate(f, [22, 36], [0, 1], {...fijo, easing: Easing.out(Easing.cubic)});
  const mano = interpolate(f, [32, 48], [0, 1], fijo);
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      <OffthreadVideo src={staticFile(A("vm1-mall.mp4"))} muted
        style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover"}} />
      <Velo css="linear-gradient(90deg, rgba(11,11,11,0.45) 0%, rgba(11,11,11,0.1) 55%, rgba(11,11,11,0) 70%)" />
      <Grano />
      <AbsoluteFill style={sube(0)}><B x={86} top={195} cap={235}>+3.627</B></AbsoluteFill>
      <AbsoluteFill style={sube(8)}>
        <B x={120} top={470} cap={72}>NUEVOS</B>
        <B x={120} top={560} cap={72}>SEGUIDORES.</B>
      </AbsoluteFill>
      <div style={{position: "absolute", left: 104, top: 676, width: 486, height: 150,
                   transform: "rotate(-6deg)", transformOrigin: "left top"}}>
        <svg width={486} height={150} style={{position: "absolute", inset: 0, overflow: "visible",
                                              clipPath: `inset(0 ${(1 - cinta) * 100}% 0 0)`}}>
          <path d="M 6 26 C 120 10, 300 18, 480 6 L 476 34 L 486 70 L 474 108 L 482 140 C 330 132, 160 146, 10 150 L 18 118 L 0 84 L 14 52 Z"
                fill={C2.rosa} />
        </svg>
        <div style={{position: "absolute", left: 30, top: 18, fontFamily: VOZ2.mano, fontWeight: 800,
                     fontSize: 100, color: TINTA, textTransform: "uppercase", whiteSpace: "nowrap",
                     clipPath: `inset(0 ${(1 - mano) * 100}% 0 0)`}}>
          EN 28 DÍAS.
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ====================== 02 · LA META ERA 18.000 ======================
const L2: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo src="m2.png" />
    <Velo css="linear-gradient(90deg, rgba(11,11,11,0.5) 0%, rgba(11,11,11,0.15) 60%, rgba(11,11,11,0) 80%)" />
    <Grano />
    <B x={100} top={185} cap={52}>LA META ERA</B>
    <B x={96} top={268} cap={206}>18.000</B>
    <B x={100} top={492} cap={58}>SEGUIDORES.</B>
    <Bal x={140} top={700} cap={72}>LLEGAMOS</Bal>
    <Bal x={128} top={808} cap={78}>12 DÍAS ANTES.</Bal>
    <Trazo x={150} y={880} ancho={540} grosor={20} giro={-6} />
  </AbsoluteFill>
);

// ====================== 03 · UN PREMIO QUE SÍ IMPORTABA ======================
// Cara blanca de la bolsa MEDIDA: x 216–760 · y 650–1290.
const L3: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo src="m3.png" />
    <Velo css="linear-gradient(90deg, rgba(11,11,11,0.55) 0%, rgba(11,11,11,0.2) 50%, rgba(11,11,11,0) 70%)" />
    <Grano />
    <B x={100} top={172} cap={86}>UN PREMIO</B>
    <B x={100} top={282} cap={86}>QUE SÍ</B>
    <B x={100} top={392} cap={86}>IMPORTABA.</B>
    <div style={{position: "absolute", left: 230, top: 930, width: 500, transform: "rotate(-1.5deg)",
                 fontFamily: "'CW Serif', 'DM Serif Display', Georgia, serif", fontSize: 50, lineHeight: 1.12,
                 color: "#2B2A2A", textAlign: "center", textTransform: "uppercase", letterSpacing: 1,
                 mixBlendMode: "multiply", opacity: 0.9}}>
      UN AGUINALDO<br />PARA SEGUIR<br />VOLVIENDO.
    </div>
  </AbsoluteFill>
);

// ====================== 04 · UNA IDEA. TODOS LOS CANALES. ======================
// Pantalla MEDIDA (con el corrimiento de la foto): (45,97) (644,95) (650,1489) (40,1491).
const P4: [number, number][] = [[45, 97], [644, 95], [650, 1489], [40, 1491]];
const IconoRegalo: React.FC<{s: number}> = ({s}) => (
  <svg width={s} height={s} viewBox="0 0 40 40">
    <rect x={5} y={16} width={30} height={20} rx={2} fill={C2.rosa} />
    <rect x={3} y={11} width={34} height={7} rx={2} fill={C2.rosa} />
    <rect x={18} y={11} width={4} height={25} fill="#fff" />
    <path d="M20 11 C 14 2, 7 6, 12 11 Z M20 11 C 26 2, 33 6, 28 11 Z" fill="#fff" />
  </svg>
);
const PantallaReels: React.FC = () => (
  <div style={{position: "absolute", left: 0, top: 0, width: 400, height: 929, overflow: "hidden",
               borderRadius: 30, background: "#000", transformOrigin: "0 0", transform: homografia(400, 929, P4)}}>
    <Img src={staticFile(A("m2.png"))}
         style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover",
                 objectPosition: "50% 40%"}} />
    <AbsoluteFill style={{background: "linear-gradient(180deg, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0) 18%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.55) 100%)"}} />
    <Estado oscuro />
    <div style={{position: "absolute", left: 0, right: 0, top: 54, textAlign: "center", fontFamily: VOZ2.cuerpo,
                 fontWeight: 700, fontSize: 20, color: "#fff"}}>Reels</div>
    <svg width={14} height={22} style={{position: "absolute", left: 22, top: 56}}>
      <path d="M11 3 L3 11 L11 19" stroke="#fff" strokeWidth={2.6} fill="none" strokeLinecap="round" />
    </svg>
    <div style={{position: "absolute", left: 40, right: 40, top: 560, textAlign: "center",
                 fontFamily: VOZ2.titular, fontWeight: 700, fontSize: 52, lineHeight: 0.96, color: "#fff",
                 transform: "rotate(-6deg)", textShadow: "0 3px 12px rgba(0,0,0,0.6)"}}>
      GRAN SORTEO<br />EL AGUINALDO<br />DEL 18
    </div>
    <div style={{position: "absolute", left: 172, top: 760}}><IconoRegalo s={58} /></div>
    {/* Barra de navegación. */}
    <div style={{position: "absolute", left: 0, right: 0, bottom: 0, height: 74, display: "flex",
                 justifyContent: "space-around", alignItems: "center", background: "rgba(0,0,0,0.55)"}}>
      {["M4 14 L14 5 L24 14 V24 H4 Z", "M11 4 a7 7 0 1 1 0 14 a7 7 0 1 1 0 -14 M16 17 L23 24",
        "M4 4 H24 V24 H4 Z M14 9 V19 M9 14 H19", "M14 23 C 4 16, 3 8, 9 6 C 12 5, 14 8, 14 9 C 14 8, 16 5, 19 6 C 25 8, 24 16, 14 23 Z",
        "M14 4 a6 6 0 1 1 0 12 a6 6 0 1 1 0 -12 M4 25 C 6 18, 22 18, 24 25"].map((d, i) => (
        <svg key={i} width={28} height={28} viewBox="0 0 28 28">
          <path d={d} stroke="#fff" strokeWidth={2.2} fill="none" strokeLinejoin="round" />
        </svg>
      ))}
    </div>
  </div>
);
const L4: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo src="m4.png" tx={-190} zoom={1.35} ox={540} oy={300} />
    <PantallaReels />
    <Velo css="linear-gradient(270deg, rgba(11,11,11,0.55) 0%, rgba(11,11,11,0.15) 30%, rgba(11,11,11,0) 42%)" />
    <Grano />
    <B x={700} top={150} cap={58}>UNA IDEA.</B>
    <B x={700} top={222} cap={58}>TODOS</B>
    <B x={700} top={294} cap={58}>LOS CANALES.</B>
    {["REELS", "STORIES", "PAID", "SORTEOS"].map((t, i) => (
      <B key={t} x={792} top={492 + i * 66} cap={38} peso={300} italica tracking={1}>{t}</B>
    ))}
  </AbsoluteFill>
);

// ====================== 05 · +35 MIL COMENTARIOS ======================
// Pantalla MEDIDA (foto bajada 200 px): (632,400) (1071,484) (862,1588) (417,1481).
const P5: [number, number][] = [[632, 400], [1071, 484], [862, 1588], [417, 1481]];
const PantallaComentarios: React.FC = () => (
  <div style={{position: "absolute", left: 0, top: 0, width: 400, height: 990, overflow: "hidden",
               borderRadius: 30, background: "#fff", transformOrigin: "0 0", transform: homografia(400, 990, P5)}}>
    <Estado />
    <svg width={14} height={22} style={{position: "absolute", left: 22, top: 58}}>
      <path d="M11 3 L3 11 L11 19" stroke="#111" strokeWidth={2.4} fill="none" strokeLinecap="round" />
    </svg>
    {/* Comentarios DIFUMINADOS: se ve la avalancha sin inventar nombres ni frases. */}
    <div style={{position: "absolute", left: 0, right: 0, top: 110, filter: "blur(3.2px)"}}>
      {[0, 1, 2, 3, 4, 5, 6].map((i) => (
        <div key={i} style={{display: "flex", alignItems: "center", gap: 16, padding: "16px 22px"}}>
          <div style={{width: 58, height: 58, borderRadius: 29, flex: "none",
                       background: ["#C9A48C", "#8E6E5B", "#D8B9A2", "#6F5446", "#B88F78", "#A07F6A", "#CDAE98"][i]}} />
          <div style={{flex: 1}}>
            <div style={{height: 13, width: 90 + (i * 37) % 60, background: "#222", borderRadius: 7, marginBottom: 10}} />
            <div style={{height: 12, width: 150 + (i * 53) % 110, background: "#888", borderRadius: 6}} />
          </div>
          <svg width={26} height={24} viewBox="0 0 28 26" style={{flex: "none"}}>
            <path d="M14 24 C 4 17, 2 9, 7 6 C 10 4, 13 6, 14 8 C 15 6, 18 4, 21 6 C 26 9, 24 17, 14 24 Z" fill={C2.rosa} />
          </svg>
        </div>
      ))}
    </div>
  </div>
);
const L5: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo src="m5.png" ty={200} />
    <Velo css="linear-gradient(180deg, rgba(11,11,11,1) 0%, rgba(11,11,11,0.9) 14%, rgba(11,11,11,0.4) 30%, rgba(11,11,11,0) 42%)" />
    <PantallaComentarios />
    <Grano />
    <B x={66} top={70} cap={222}>+35 MIL</B>
    <B x={90} top={345} cap={72}>COMENTARIOS</B>
    <B x={90} top={440} cap={72}>EN EL POST.</B>
    <Bal x={96} top={612} cap={112} giro={-6}>3,3X</Bal>
    <Flecha x={350} y={560} ancho={60} alto={60} giro={-60} grosor={6} />
    <Bal x={88} top={800} cap={38} giro={-6} color={C2.offwhite}>VS. EL AÑO PASADO.</Bal>
  </AbsoluteFill>
);

// ====================== 06 · 328 MIL CUENTAS ALCANZADAS ======================
const L6: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo src="m6.png" />
    <Velo css="linear-gradient(90deg, rgba(11,11,11,0.6) 0%, rgba(11,11,11,0.25) 55%, rgba(11,11,11,0) 75%)" />
    <Grano />
    <B x={98} top={525} cap={166}>328 MIL</B>
    <B x={100} top={722} cap={56}>CUENTAS ALCANZADAS.</B>
    <Trazo x={100} y={824} ancho={330} grosor={14} giro={-3} />
    <B x={98} top={900} cap={166}>98%</B>
    <B x={100} top={1112} cap={56}>NO SEGUÍAN</B>
    <B x={100} top={1190} cap={56}>LA CUENTA.</B>
  </AbsoluteFill>
);

// ====================== 07 · TRES CREAN CONVERSACIÓN ======================
const TARJETAS: {x: number; img: string; pos: string; n: string; t: React.ReactNode}[] = [
  {x: 50, img: "m6.png", pos: "50% 72%", n: "01", t: <>TEASER Y<br />CONTENIDO.</>},
  {x: 388, img: "m3.png", pos: "52% 58%", n: "02", t: <>SORTEO<br />PRINCIPAL.</>},
  {x: 726, img: "m7.png", pos: "52% 46%", n: "03", t: <>ÚLTIMO<br />IMPULSO.</>},
];
const L7: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo src="m2.png" filtro="blur(14px) brightness(0.32)" zoom={1.1} />
    <Grano />
    <B x={100} top={44} cap={58}>UN SORTEO ES UN PICO.</B>
    <Bal x={92} top={158} cap={88} giro={-6}>TRES CREAN</Bal>
    <Bal x={196} top={262} cap={88} giro={-6}>CONVERSACIÓN.</Bal>
    <Trazo x={420} y={352} ancho={290} grosor={12} giro={-7} />
    {TARJETAS.map((c) => (
      <div key={c.n} style={{position: "absolute", left: c.x, top: 420, width: 304, height: 655,
                             borderRadius: 26, overflow: "hidden", border: "2px solid rgba(245,243,238,0.32)",
                             background: "#141414"}}>
        <Img src={staticFile(A(c.img))}
             style={{position: "absolute", left: 0, top: 0, width: "100%", height: 470,
                     objectFit: "cover", objectPosition: c.pos}} />
        <div style={{position: "absolute", left: 0, right: 0, top: 300, height: 360,
                     background: "linear-gradient(180deg, rgba(20,20,20,0) 0%, rgba(20,20,20,0.85) 45%, #141414 70%)"}} />
        <div style={{position: "absolute", left: 22, top: 428, fontFamily: VOZ2.titular, fontWeight: 700,
                     fontSize: 74, color: C2.offwhite, lineHeight: 1}}>{c.n}</div>
        <div style={{position: "absolute", left: 22, top: 520, fontFamily: VOZ2.titular, fontWeight: 400,
                     fontSize: 50, color: C2.offwhite, lineHeight: 1.04, textTransform: "uppercase"}}>{c.t}</div>
      </div>
    ))}
    <div style={{position: "absolute", left: 100, top: 1214, width: 60, height: 2, background: C2.offwhite}} />
    <B x={196} top={1200} cap={30} peso={400} tracking={9} sombra={false}>3 ACTIVACIONES SEMANALES</B>
  </AbsoluteFill>
);

// ====================== 08 · NO FUE UN POST. FUE UNA CAMPAÑA. ======================
const L8: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo src="m8.png" />
    <Velo css="linear-gradient(90deg, rgba(11,11,11,0.55) 0%, rgba(11,11,11,0.2) 55%, rgba(11,11,11,0) 75%)" />
    <Grano />
    <B x={98} top={86} cap={162}>NO FUE</B>
    <B x={98} top={272} cap={162}>UN POST.</B>
    <Bal x={96} top={486} cap={122} giro={-6}>FUE UNA</Bal>
    <Bal x={100} top={632} cap={132} giro={-6}>CAMPAÑA.</Bal>
    <Trazo x={100} y={780} ancho={700} grosor={26} giro={-6} />
  </AbsoluteFill>
);

const LAMINAS = [L1, L2, L3, L4, L5, L6, L7, L8];

let serifCargada = false;
const asegurarSerif = () => {
  if (serifCargada || typeof document === "undefined") return;
  serifCargada = true;
  const st = document.createElement("style");
  st.innerHTML = `@font-face{font-family:'CW Serif';src:url(${staticFile("assets/fonts/copywriters/DMSerifDisplay-Regular.ttf")}) format('truetype');font-display:block;}`;
  document.head.appendChild(st);
};

export const CW02Concurso: React.FC<{lamina?: number}> = ({lamina = 1}) => {
  asegurarFuentesV2();
  asegurarSerif();
  const L = LAMINAS[Math.min(Math.max(lamina, 1), LAMINAS.length) - 1];
  return <L />;
};
