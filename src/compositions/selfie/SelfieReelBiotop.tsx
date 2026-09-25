/**
 * SELFIE · REEL de prueba «Biotop 700 + 911» (25-09-2026) — 1080×1920, 30 fps, 15 s
 *
 * DIRECCIÓN DE ARTE
 * - Ritmo y mecánica: los de la referencia de Pinterest que dejó Coni
 *   (raw/selfie/ref-animacion/ref.mp4): anillos concéntricos que abren con productos
 *   volando → titular palabra a palabra → héroe del 1.er producto sobre una onda con su
 *   ingrediente flotando → barrido al 2.º → cierre con los dos cruzados y destellos.
 * - Estilo: el aprobado en la prueba Biotop (clients/selfie/CLAUDE.md § EL ESTILO NUEVO):
 *   Scotch Display Condensed Roman + Medium Italic en nude para el titular, Krub para
 *   todo lo demás, ficha coral + caja blanca, coral #FF4374 · salmón #FF8C93 · nude
 *   #F7D4C0, logotipo SELFIE vertical arriba a la derecha.
 * - Textos: SÓLO de las fichas del e-commerce que dejó Coni (beneficios y modo de uso).
 * - Ingredientes flotando = los de cada ficha: kale (700), quinoa y girasol (911), y
 *   gotas de serum. Generados con Seedream 5 Pro (no llevan marca).
 * - Zonas seguras de Reels: nada de texto en los 250 px de arriba, los 340 de abajo ni
 *   la franja derecha de 115 px (memoria paid-media-zonas-seguras).
 * - Sin música: se le pone la de la biblioteca de Instagram al publicar (así lo pide el
 *   brief del Cyber de Selfie para los orgánicos).
 */
import React from "react";
import {
  AbsoluteFill,
  Easing,
  Img,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

const C = {coral: "#FF4374", salmon: "#FF8C93", nude: "#F7D4C0", tinta: "#001E1D", blanco: "#FFFFFF"};
const A = (f: string) => staticFile(`assets/selfie/2026-nuevo-estilo/${f}`);
const clamp = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

let fuentes = false;
const cargaFuentes = () => {
  if (fuentes || typeof document === "undefined") return;
  fuentes = true;
  const caras: Array<[string, number, string, string]> = [
    ["Scotch Display Condensed", 400, "normal", "ScotchDisplayCond-Rm.ttf"],
    ["Scotch Display Condensed", 500, "italic", "ScotchDisplayCond-MdIt.ttf"],
    ["Scotch Display", 500, "italic", "ScotchDisplay-MediumItalic.ttf"],
    ["Krub", 200, "normal", "Krub-ExtraLight.ttf"],
    ["Krub", 500, "normal", "Krub-Medium.ttf"],
    ["Krub", 600, "normal", "Krub-SemiBold.ttf"],
    ["Krub", 600, "italic", "Krub-SemiBoldItalic.ttf"],
    ["Krub", 700, "normal", "Krub-Bold.ttf"],
  ];
  const s = document.createElement("style");
  s.textContent = caras
    .map(
      ([fam, w, st, file]) =>
        `@font-face{font-family:'${fam}';font-weight:${w};font-style:${st};font-display:block;` +
        `src:url(${staticFile(`assets/fonts/selfie-2026/${file}`)}) format('truetype');}`,
    )
    .join("\n");
  document.head.appendChild(s);
};

const sube = (f: number, fps: number, delay = 0, damping = 15) =>
  spring({frame: f - delay, fps, config: {damping, stiffness: 120, mass: 0.8}});

/** Frasco parado (ya preparado a 820 px de alto, 1:1 en el héroe). */
const Frasco: React.FC<{k: "700" | "911"; x: number; y: number; h: number; rot: number; o?: number}> = ({
  k,
  x,
  y,
  h,
  rot,
  o = 1,
}) => (
  <Img
    src={A(`reel/frasco-${k}.png`)}
    style={{
      position: "absolute",
      left: x,
      top: y,
      height: h,
      opacity: o,
      transform: `translate(-50%, -50%) rotate(${rot}deg)`,
      filter: "drop-shadow(-14px 26px 28px rgba(0,30,29,0.28))",
    }}
  />
);

/** Ingrediente que flota: entra con un pop y respira despacio. */
const Flota: React.FC<{src: string; x: number; y: number; w: number; rot: number; delay: number; fase: number}> = ({
  src,
  x,
  y,
  w,
  rot,
  delay,
  fase,
}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const s = sube(f, fps, delay, 11);
  const bob = Math.sin((f + fase) / 16) * 12;
  const gira = Math.sin((f + fase) / 24) * 6;
  return (
    <Img
      src={A(`reel/${src}.png`)}
      style={{
        position: "absolute",
        left: x,
        top: y + bob,
        width: w,
        opacity: s,
        transform: `translate(-50%, -50%) scale(${0.4 + 0.6 * s}) rotate(${rot + gira}deg)`,
        filter: "drop-shadow(-8px 14px 16px rgba(0,30,29,0.22))",
      }}
    />
  );
};

const Logo: React.FC<{o?: number}> = ({o = 1}) => (
  // grilla: x 953 en mesa de 1080; en Reels se corre a la izquierda de la franja de 115 px
  <Img src={A("selfie-logo-vertical.svg")} style={{position: "absolute", left: 925, top: 262, width: 37, opacity: o}} />
);

/** Titular de la marca: Scotch Condensed Roman + 2.ª línea Medium Italic en nude, palabra a palabra. */
const Titular: React.FC<{y: number; delay: number; size?: number; linea2?: string}> = ({
  y,
  delay,
  size = 1,
  linea2 = C.nude,
}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const palabra = (txt: string, i: number) => {
    const s = sube(f, fps, delay + i * 4, 16);
    return (
      <span
        key={txt + i}
        style={{
          display: "inline-block",
          opacity: s,
          transform: `translateY(${(1 - s) * 60}px)`,
          filter: `blur(${(1 - s) * 10}px)`,
          marginRight: "0.22em",
        }}
      >
        {txt}
      </span>
    );
  };
  return (
    <div style={{position: "absolute", top: y, left: 0, width: 1080, textAlign: "center", color: C.blanco}}>
      <div style={{fontFamily: "Scotch Display Condensed", fontWeight: 400, fontSize: 132 * size, lineHeight: 0.9}}>
        {["Dos", "aliados", "para"].map(palabra)}
      </div>
      <div
        style={{
          fontFamily: "Scotch Display Condensed",
          fontWeight: 500,
          fontStyle: "italic",
          fontSize: 140 * size,
          lineHeight: 0.9,
          color: linea2,
        }}
      >
        {["un", "pelo", "en", "orden."].map((t, i) => palabra(t, i + 3))}
      </div>
    </div>
  );
};

/** Ficha de la grilla (mesa 8): caja coral con el nombre + caja blanca con el beneficio. */
const Ficha: React.FC<{nombre: string; serif: string; resto: string; x: number; y: number; w: number; delay: number}> = ({
  nombre,
  serif,
  resto,
  x,
  y,
  w,
  delay,
}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const s1 = sube(f, fps, delay);
  const s2 = sube(f, fps, delay + 7);
  // subrayado a mano bajo la frase en serif (el garabato de la referencia)
  const trazo = interpolate(f, [delay + 14, delay + 32], [0, 1], {...clamp, easing: Easing.out(Easing.cubic)});
  return (
    <div style={{position: "absolute", left: x, top: y, width: w, textAlign: "center"}}>
      <div
        style={{
          position: "relative",
          background: C.coral,
          borderRadius: 16,
          padding: "20px 24px 44px",
          color: C.blanco,
          fontFamily: "Krub",
          fontWeight: 700,
          fontSize: 44,
          lineHeight: 1.08,
          opacity: s1,
          transform: `translateY(${(1 - s1) * 40}px)`,
          boxShadow: "0 0 22px 7px rgba(0,0,0,0.30)",
        }}
      >
        {nombre}
      </div>
      <div
        style={{
          position: "relative",
          margin: "-24px 30px 0",
          background: C.blanco,
          borderRadius: 16,
          padding: "14px 22px 18px",
          color: C.coral,
          fontFamily: "Krub",
          fontWeight: 500,
          fontSize: 40,
          lineHeight: 1.1,
          opacity: s2,
          transform: `translateY(${(1 - s2) * 40}px)`,
        }}
      >
        <span style={{position: "relative", fontFamily: "Scotch Display", fontStyle: "italic", fontSize: 46}}>
          {serif}
          <svg
            viewBox="0 0 300 20"
            preserveAspectRatio="none"
            style={{position: "absolute", left: 0, right: 0, bottom: -10, width: "100%", height: 16, overflow: "visible"}}
          >
            <path
              d="M 4 12 C 60 4, 120 16, 180 9 S 270 6, 296 11"
              fill="none"
              stroke={C.coral}
              strokeWidth={3}
              strokeLinecap="round"
              pathLength={1}
              strokeDasharray={1}
              strokeDashoffset={1 - trazo}
            />
          </svg>
        </span>{" "}
        {resto}
      </div>
    </div>
  );
};

/** Beneficio de la ficha del e-commerce, en píldora blanca con check. */
const Beneficio: React.FC<{txt: string; x: number; y: number; w: number; delay: number; lado: 1 | -1}> = ({
  txt,
  x,
  y,
  w,
  delay,
  lado,
}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const s = sube(f, fps, delay, 14);
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y,
        width: w,
        opacity: s,
        transform: `translateX(${(1 - s) * 80 * lado}px)`,
        display: "flex",
        alignItems: "center",
        gap: 14,
        background: "rgba(255,255,255,0.96)",
        borderRadius: 999,
        padding: "14px 26px",
        fontFamily: "Krub",
        fontWeight: 600,
        fontSize: 34,
        lineHeight: 1.1,
        color: C.coral,
      }}
    >
      <span style={{fontSize: 34, color: C.coral}}>✱</span>
      <span>{txt}</span>
    </div>
  );
};

/* ───────── ESCENA 1 · 0–2 s — anillos que abren y frascos que salen volando ───────── */
const Apertura: React.FC = () => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const zoom = interpolate(f, [0, 60], [0.35, 3.2], {...clamp, easing: Easing.in(Easing.cubic)});
  const anillos = [C.coral, C.nude, C.salmon, C.blanco, C.coral, C.nude];
  const vuelan = [
    {k: "700", a: -30, d: 470, r: -40},
    {k: "911", a: 25, d: 520, r: 35},
    {k: "700", a: 150, d: 500, r: 60},
    {k: "911", a: 205, d: 460, r: -55},
    {k: "700", a: 95, d: 610, r: 15},
    {k: "911", a: 275, d: 600, r: -20},
  ] as const;
  const sale = interpolate(f, [34, 60], [0, 1], {...clamp, easing: Easing.in(Easing.quad)});
  return (
    <AbsoluteFill style={{background: C.salmon, overflow: "hidden"}}>
      {anillos.map((c, i) => (
        <div
          key={i}
          style={{
            position: "absolute",
            left: 540,
            top: 960,
            width: 2200 - i * 340,
            height: 2200 - i * 340,
            borderRadius: "50%",
            background: c,
            transform: `translate(-50%, -50%) scale(${zoom})`,
          }}
        />
      ))}
      {vuelan.map((v, i) => {
        const s = sube(f, fps, i * 2, 12);
        const rad = (v.a * Math.PI) / 180;
        const d = v.d * s + sale * 900;
        return (
          <Frasco
            key={i}
            k={v.k}
            x={540 + Math.cos(rad) * d}
            y={960 + Math.sin(rad) * d}
            h={430}
            rot={v.r + (1 - s) * 180}
            o={s}
          />
        );
      })}
    </AbsoluteFill>
  );
};

/* ───────── ESCENA 2 · 2–4 s — el titular, palabra a palabra, y el círculo que barre ───────── */
const Titulo: React.FC = () => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const a = sube(f, fps, 10, 13);
  const b = sube(f, fps, 16, 13);
  const barre = interpolate(f, [44, 62], [0, 1], {...clamp, easing: Easing.in(Easing.cubic)});
  return (
    <AbsoluteFill style={{background: C.salmon, overflow: "hidden"}}>
      <div
        style={{
          position: "absolute",
          left: -300,
          top: -400,
          width: 1200,
          height: 1200,
          borderRadius: "50%",
          background: C.coral,
          transform: `scale(${0.6 + 0.4 * a})`,
        }}
      />
      <Frasco k="700" x={230 - (1 - a) * 500} y={520} h={560} rot={-18} />
      <Frasco k="911" x={860 + (1 - b) * 500} y={1420} h={540} rot={15} />
      <Titular y={800} delay={0} size={0.8} />
      <div
        style={{
          position: "absolute",
          left: 540,
          top: 1920,
          width: 4200,
          height: 4200,
          borderRadius: "50%",
          background: C.coral,
          transform: `translate(-50%, -50%) scale(${barre})`,
        }}
      />
    </AbsoluteFill>
  );
};

/* ───────── ESCENAS 3 y 4 · el héroe de cada frasco sobre la onda ───────── */
const Heroe: React.FC<{
  k: "700" | "911";
  lado: 1 | -1; // 1 = frasco a la derecha, beneficios a la izquierda
  nombre: string;
  serif: string;
  resto: string;
  beneficios: string[];
  flotan: Array<{src: string; x: number; y: number; w: number; rot: number}>;
  arriba: string;
  abajo: string;
}> = ({k, lado, nombre, serif, resto, beneficios, flotan, arriba, abajo}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const onda = interpolate(f, [0, 18], [1920, 1040], {...clamp, easing: Easing.out(Easing.cubic)});
  const s = sube(f, fps, 6, 12);
  const fx = lado === 1 ? 720 : 360;
  const bob = Math.sin(f / 18) * 8;
  const salida = interpolate(f, [104, 120], [0, 1], {...clamp, easing: Easing.in(Easing.cubic)});
  return (
    <AbsoluteFill style={{background: arriba, overflow: "hidden"}}>
      <svg width={1080} height={1920} style={{position: "absolute", inset: 0}}>
        <path
          d={`M 0 ${onda} C 280 ${onda - 120}, 620 ${onda + 110}, 1080 ${onda - 60} L 1080 1920 L 0 1920 Z`}
          fill={abajo}
        />
      </svg>
      {flotan.map((p, i) => (
        <Flota key={i} {...p} delay={14 + i * 5} fase={i * 23} />
      ))}
      <Frasco k={k} x={fx} y={1180 + (1 - s) * 700 + bob} h={820} rot={lado * 4 * (1 - s)} />
      <Ficha nombre={nombre} serif={serif} resto={resto} x={70} y={300} w={820} delay={10} />
      {beneficios.map((b, i) => (
        <Beneficio
          key={b}
          txt={b}
          x={lado === 1 ? 60 : 500}
          y={930 + i * 150}
          w={lado === 1 ? 480 : 460}
          delay={40 + i * 14}
          lado={lado === 1 ? -1 : 1}
        />
      ))}
      {/* barrido de salida: la onda sube y tapa todo */}
      <div
        style={{
          position: "absolute",
          left: 0,
          width: 1080,
          top: 1920 - salida * 2100,
          height: 2400,
          background: abajo,
          borderRadius: "50% 50% 0 0 / 180px 180px 0 0",
        }}
      />
    </AbsoluteFill>
  );
};

/* ───────── ESCENA 5 · 12–15 s — los dos cruzados, destellos y el llamado ───────── */
const Cierre: React.FC = () => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const a = sube(f, fps, 4, 12);
  const b = sube(f, fps, 10, 12);
  const destello = interpolate(f, [26, 40], [0, 1], clamp);
  const cta = sube(f, fps, 34, 14);
  const burbujas = [
    [120, 980, 34], [960, 900, 22], [200, 1500, 18], [880, 1460, 40], [520, 1600, 16], [80, 1250, 24], [990, 1220, 16],
  ];
  return (
    <AbsoluteFill style={{background: C.salmon, overflow: "hidden"}}>
      <svg width={1080} height={1920} style={{position: "absolute", inset: 0}}>
        <path d="M 600 0 C 830 380, 820 700, 560 980 C 300 1250, 290 1600, 390 1920 L 0 1920 L 0 0 Z" fill={C.coral} />
      </svg>
      {burbujas.map(([x, y, r], i) => {
        const s = sube(f, fps, 12 + i * 3, 10);
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: x,
              top: y + Math.sin((f + i * 20) / 14) * 10,
              width: r * 2,
              height: r * 2,
              borderRadius: "50%",
              border: `3px solid ${C.blanco}`,
              opacity: s * 0.9,
              transform: `translate(-50%, -50%) scale(${s})`,
            }}
          />
        );
      })}
      <Frasco k="700" x={450 - (1 - a) * 700} y={1110} h={640} rot={-16} />
      <Frasco k="911" x={640 + (1 - b) * 700} y={1130} h={640} rot={16} />
      <Titular y={560} delay={0} size={0.8} />
      {/* destellos a los lados del titular, como en la referencia */}
      {[-1, 1].map((l) =>
        [-24, 0, 24].map((ang, i) => (
          <div
            key={`${l}${i}`}
            style={{
              position: "absolute",
              left: 540 + l * 395,
              top: 650 + i * 38 - 38,
              width: 54 * destello,
              height: 5,
              borderRadius: 3,
              background: C.blanco,
              transformOrigin: l === 1 ? "left center" : "right center",
              transform: `translateX(${l === 1 ? 0 : -54 * destello}px) rotate(${l * ang}deg)`,
            }}
          />
        )),
      )}
      <div
        style={{
          position: "absolute",
          top: 1478,
          left: 0,
          width: 1080,
          textAlign: "center",
          opacity: cta,
          transform: `translateY(${(1 - cta) * 30}px)`,
        }}
      >
        <div
          style={{
            display: "inline-block",
            padding: "12px 34px 14px",
            border: `2px solid ${C.blanco}`,
            color: C.blanco,
            fontFamily: "Krub",
            fontSize: 42,
            fontWeight: 200,
          }}
        >
          Encuéntralos en <span style={{fontWeight: 600, fontStyle: "italic"}}>Selfie.cl</span>
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const SelfieReelBiotop: React.FC = () => {
  cargaFuentes();
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{background: C.salmon}}>
      <Sequence durationInFrames={60}>
        <Apertura />
      </Sequence>
      <Sequence from={60} durationInFrames={62}>
        <Titulo />
      </Sequence>
      <Sequence from={120} durationInFrames={120}>
        <Heroe
          k="700"
          lado={1}
          nombre="700 Keratin & Kale Serum"
          serif="Controla el frizz"
          resto="y da más fuerza al pelo."
          beneficios={["Hidrata profundamente", "Repara el cabello dañado", "Reduce el frizz y las puntas abiertas"]}
          flotan={[
            {src: "kale", x: 860, y: 800, w: 230, rot: 20},
            {src: "kale", x: 420, y: 1540, w: 180, rot: -35},
            {src: "gota", x: 540, y: 820, w: 110, rot: 0},
            {src: "gota", x: 960, y: 1450, w: 80, rot: 0},
          ]}
          arriba={C.coral}
          abajo={C.salmon}
        />
      </Sequence>
      <Sequence from={240} durationInFrames={120}>
        <Heroe
          k="911"
          lado={-1}
          nombre="911 Quinoa Serum"
          serif="Sella"
          resto="la cutícula y aporta brillo natural."
          beneficios={["Protege del calor y los rayos UV", "Fórmula ligera y no grasosa", "Hidrata, suaviza y aporta brillo"]}
          flotan={[
            {src: "quinoa", x: 150, y: 780, w: 260, rot: -10},
            {src: "girasol", x: 640, y: 1540, w: 230, rot: 15},
            {src: "gota", x: 560, y: 840, w: 100, rot: 0},
            {src: "quinoa", x: 120, y: 1560, w: 170, rot: 20},
          ]}
          arriba={C.salmon}
          abajo={C.coral}
        />
      </Sequence>
      <Sequence from={360}>
        <Cierre />
      </Sequence>
      <Logo o={interpolate(f, [0, 12], [0, 1], clamp)} />
    </AbsoluteFill>
  );
};
