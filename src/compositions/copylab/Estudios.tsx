// ============================================================================
// ESTUDIOS — Creative Direction Board 3 (24-09-2026, feedback del director)
// ----------------------------------------------------------------------------
// «Claude entendió las reglas, pero perdió la dirección de arte.» Las HERO v1
// pasaban el QA técnico y NO el creativo: titular arriba, serif abajo, mono al
// pie. Esto es la respuesta: la MISMA foto de la goma en 6 composiciones que no
// comparten layout, y 4 sistemas para NADIE LO FIRMÓ.
// Benchmark: creative-system/MASTER/reference/LOOK_AND_FEEL_REFERENCE.png
// (VISUAL MATCH TEST, MASTER/09).
//
// La mano está recortada (h1-mano-nobg.png, @imgly local) y se monta ENCIMA
// del tipo con la misma transformación que la foto: así la tipografía puede
// pasar entre el papel y los dedos.
// Las fotos de NADIE LO FIRMÓ son RECREACIONES (Nano Banana Pro) y lo dicen
// en el arte: nunca se hacen pasar por hallazgo documental.
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {C, asegurarFuentes, VOZ} from "../../brand/copylab/sistema";
import {Grano} from "../../brand/copylab/lienzo";

const W = 1080;
const H = 1350;
const GOMA = {src: "assets/copylab/hero/h1-goma-full.jpg", w: 1770, h: 2360};
const MANO = "assets/copylab/hero/h1-mano-nobg.png";

/** Foto posicionada: escala s, origen (x, y) en el lienzo. */
const Placa: React.FC<{src: string; w: number; s: number; x: number; y: number; style?: React.CSSProperties}> =
  ({src, w, s, x, y, style}) => (
    <Img src={staticFile(src)} style={{position: "absolute", left: x, top: y, width: w * s, ...style}} />
  );

const Goma: React.FC<{s: number; x: number; y: number}> = (p) => <Placa src={GOMA.src} w={GOMA.w} {...p} />;
const Mano: React.FC<{s: number; x: number; y: number}> = (p) => <Placa src={MANO} w={GOMA.w} {...p} />;

const narrow = (size: number, color: string, extra?: React.CSSProperties): React.CSSProperties => ({
  fontFamily: VOZ.narrow, fontWeight: 700, fontSize: size, lineHeight: 0.84,
  letterSpacing: "-0.02em", textTransform: "uppercase", color, whiteSpace: "nowrap", ...extra,
});
const serif = (size: number, color: string, extra?: React.CSSProperties): React.CSSProperties => ({
  fontFamily: VOZ.editorial, fontStyle: "italic", fontSize: size, lineHeight: 0.9, color, whiteSpace: "nowrap", ...extra,
});
const mono = (color: string, extra?: React.CSSProperties): React.CSSProperties => ({
  fontFamily: VOZ.data, fontSize: 20, lineHeight: 1.4, letterSpacing: "0.14em", textTransform: "uppercase", color, ...extra,
});
const abs = (s: React.CSSProperties): React.CSSProperties => ({position: "absolute", ...s});

/** Borrón con borde de goma: elipse desplazada por ruido. */
const Borron: React.FC<{id: string; cx: number; cy: number; rx: number; ry: number; rot?: number; seed?: number}> =
  ({id, cx, cy, rx, ry, rot = -14, seed = 7}) => (
    <defs>
      <filter id={`${id}-f`} x="-30%" y="-30%" width="160%" height="160%">
        <feTurbulence type="fractalNoise" baseFrequency="0.045" numOctaves="3" seed={seed} />
        <feDisplacementMap in="SourceGraphic" scale="70" />
      </filter>
      <mask id={id} maskUnits="userSpaceOnUse" x="0" y="0" width={W} height={H}>
        <rect x="0" y="0" width={W} height={H} fill="white" />
        <g filter={`url(#${id}-f)`}>
          <ellipse cx={cx} cy={cy} rx={rx} ry={ry} fill="black" transform={`rotate(${rot} ${cx} ${cy})`} />
        </g>
      </mask>
    </defs>
  );

// ---------------------------------------------------------------------------
// HERO 1 — seis estudios con la misma foto
// ---------------------------------------------------------------------------

// E1 · TIPOGRAFÍA COMO IMAGEN — la goma le está comiendo el «FÁCIL.».
const E1 = () => {
  const s = 0.62, x = -8, y = -70;
  return (
    <AbsoluteFill style={{background: C.tinta}}>
      <Goma s={s} x={x} y={y} />
      <div style={abs({left: 44, top: 40, ...narrow(168, C.offwhite)})}>Escribir es</div>
      <svg width={W} height={H} style={abs({left: 0, top: 0})}>
        <Borron id="e1" cx={600} cy={800} rx={230} ry={105} rot={-10} />
        <g style={{fontFamily: VOZ.narrow, fontWeight: 700, letterSpacing: "-0.03em"}}>
          <text x="20" y="1010" fontSize="400" fill={C.tinta} opacity="0.09">FÁCIL.</text>
          <text x="20" y="1010" fontSize="400" fill={C.tinta} mask="url(#e1)">FÁCIL.</text>
        </g>
      </svg>
      <Mano s={s} x={x} y={y} />
      <div style={abs({left: 60, top: 1120, ...mono("rgba(8,15,20,0.75)")})}>Lo difícil es saber qué borrar.</div>
      <Grano op={0.16} />
    </AbsoluteFill>
  );
};

// E2 · CROP EXTREMO — la goma del tamaño de un auto; la serif es UNA palabra.
const E2 = () => {
  const s = 1.85, x = -1010, y = -1660;
  return (
    <AbsoluteFill style={{background: C.offwhite}}>
      <Goma s={s} x={x} y={y} />
      <div style={abs({left: -30, top: 880, ...serif(520, C.tinta, {letterSpacing: "-0.03em"})})}>borrar.</div>
      <Mano s={s} x={x} y={y} />
      <div style={abs({left: 56, top: 56, ...mono(C.offwhite)})}>Escribir es fácil.<br />Lo difícil es saber qué</div>
      <Grano op={0.14} />
    </AbsoluteFill>
  );
};

// E3 · COLISIÓN EDITORIAL — el rosa como evento: la mano rompe el bloque.
const E3 = () => {
  const s = 0.6, x = 160, y = 250;
  return (
    <AbsoluteFill style={{background: C.tinta}}>
      <Goma s={s} x={x} y={y} />
      <div style={abs({left: 0, top: 0, width: W, height: 720, background: C.rosa})} />
      <div style={abs({left: 26, top: 36, ...narrow(262, C.tinta, {lineHeight: 0.82})})}>Escribir<br />es fácil.</div>
      <Mano s={s} x={x} y={y} />
      <div style={abs({left: 56, top: 1130, ...serif(62, C.offwhite)})}>Lo difícil es<br />saber qué borrar.</div>
      <Grano op={0.12} />
    </AbsoluteFill>
  );
};

// E4 · ESPACIO NEGATIVO RADICAL — el vacío es lo que ya se borró.
const E4 = () => (
  <AbsoluteFill style={{background: C.offwhite}}>
    <div style={abs({left: 40, top: 300, opacity: 0.045, filter: "blur(1.5px)", ...narrow(230, C.tinta, {lineHeight: 0.86})})}>Escribir<br />es fácil<br />y rápido</div>
    <div style={abs({left: 612, top: 902, width: 396, height: 376, overflow: "hidden"})}>
      <Goma s={0.62} x={-298} y={-640} />
    </div>
    <div style={abs({left: 72, top: 72, ...narrow(46, C.tinta)})}>Escribir es fácil.</div>
    <div style={abs({left: 72, top: 1216, ...mono("rgba(8,15,20,0.6)")})}>Lo difícil es saber<br />qué borrar.</div>
    <Grano op={0.1} />
  </AbsoluteFill>
);

// E5 · CASI SIN TIPOGRAFÍA — la foto sola, encuadre incómodo; sólo la firma.
const E5 = () => {
  const s = 1.05, x = -560, y = -760;
  return (
    <AbsoluteFill style={{background: C.tinta}}>
      <div style={abs({left: 0, top: 0, width: W, height: H, transform: "rotate(-90deg)", transformOrigin: "50% 50%"})}>
        <Goma s={s * 1.25} x={x - 80} y={y - 300} />
      </div>
      <div style={abs({left: 56, bottom: 60, ...mono(C.offwhite)})}>Lo difícil es saber qué borrar.</div>
      <Grano op={0.18} />
    </AbsoluteFill>
  );
};

// E6 · EXPERIMENTAL — el texto como material: una pared de borradores y la
// goma abriendo un camino limpio.
const E6 = () => {
  const s = 0.62, x = -8, y = -70;
  const lineas = Array.from({length: 13});
  return (
    <AbsoluteFill style={{background: C.tinta}}>
      <Goma s={s} x={x} y={y} />
      <svg width={W} height={H} style={abs({left: 0, top: 0})}>
        <defs>
          <filter id="e6-f" x="-20%" y="-20%" width="140%" height="140%">
            <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="3" seed="3" />
            <feDisplacementMap in="SourceGraphic" scale="46" />
          </filter>
          <mask id="e6" maskUnits="userSpaceOnUse" x="0" y="0" width={W} height={H}>
            <rect x="0" y="0" width={W} height={H} fill="white" />
            <g filter="url(#e6-f)">
              <path d="M 470 820 L 1120 520 L 1120 700 L 560 960 Z" fill="black" />
              <path d="M 470 820 L -40 1060 L -40 1240 L 560 960 Z" fill="black" />
            </g>
          </mask>
        </defs>
        <g mask="url(#e6)" style={{fontFamily: VOZ.narrow, fontWeight: 700}}>
          {lineas.map((_, i) => (
            <text key={i} x={-20 - (i % 3) * 60} y={120 + i * 100} fontSize="118" letterSpacing="-2"
              fill={i < 3 ? "rgba(242,244,246,0.9)" : "rgba(8,15,20,0.82)"}>
              ESCRIBIR ES FÁCIL ESCRIBIR ES FÁCIL
            </text>
          ))}
        </g>
      </svg>
      <Mano s={s} x={x} y={y} />
      <div style={abs({left: 600, top: 980, transform: "rotate(-24deg)", transformOrigin: "0 0", ...serif(86, C.rosa)})}>qué borrar.</div>
      <Grano op={0.16} />
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// NADIE LO FIRMÓ — cuatro sistemas × dos números
// ---------------------------------------------------------------------------
type Ficha = {src: string; w: number; s: number; x: number; y: number; n: string; soporte: string};
const FICHAS: Record<number, Ficha> = {
  1: {src: "assets/copylab/hero/n01-pan.jpg", w: 1856, s: 0.62, x: -32, y: -40, n: "01", soporte: "Cartón y plumón"},
  2: {src: "assets/copylab/hero/n02-vendo.jpg", w: 1856, s: 0.62, x: -34, y: -40, n: "02", soporte: "Betún blanco sobre luneta"},
  3: {src: "assets/copylab/hero/n03-llaves.jpg", w: 1780, s: 0.62, x: -12, y: -30, n: "03", soporte: "Esmalte sobre lata"},
};
// Sistema D: la serif toma un color de la FOTO, no el rosa por defecto
// (MASTER/09 · menos branding evidente). Nº01 rosa = la cinta de su cartel.
const TINTE_D: Record<number, string> = {1: C.rosa, 2: C.offwhite, 3: "#E3B341"};
// Encuadre propio de cada número en D: el cartel no puede quedar bajo la cabecera.
const POS_D: Record<number, {s: number; x: number; y: number}> = {
  1: {s: 0.72, x: -122, y: 20},
  2: {s: 0.72, x: -124, y: 20},
  3: {s: 0.72, x: -100, y: 330},
};
const POS_A: Record<number, {s: number; x: number; y: number}> = {
  1: {s: 0.68, x: 88, y: -80},
  2: {s: 0.68, x: 86, y: -80},
  3: {s: 0.6, x: 160, y: -20},
};
// Recortes cerrados sobre el cartel (sistema C). Nº02 deja fuera la insignia
// inventada del auto («CORSVOLET»).
const CERCA: Record<number, {s: number; x: number; y: number}> = {
  1: {s: 1.5, x: -330, y: -1180},
  2: {s: 0.98, x: -240, y: -620},
};

// A · ARCHIVO — número gigante vertical que se sale del lienzo + ficha de catálogo.
const SA: React.FC<{n: number}> = ({n}) => {
  const f = FICHAS[n];
  return (
    <AbsoluteFill style={{background: C.tinta}}>
      <Placa src={f.src} w={f.w} {...POS_A[n]} />
      <div style={abs({left: 0, top: 0, width: 320, height: H, background: C.tinta})} />
      <div style={abs({left: -70, top: H + 20, transform: "rotate(-90deg)", transformOrigin: "0 0",
        ...narrow(520, C.offwhite, {lineHeight: 0.8})})}>Nº{f.n}</div>
      <div style={abs({right: 48, bottom: 48, width: 380, background: C.offwhite, padding: "22px 24px",
        ...mono(C.tinta, {fontSize: 17, lineHeight: 1.6})})}>
        <div style={{fontWeight: 500}}>Nadie lo firmó · Nº{f.n}</div>
        <div>Autor: desconocido</div>
        <div>Soporte: {f.soporte}</div>
        <div style={{opacity: 0.6}}>Recreación publicitaria</div>
      </div>
      <Grano op={0.16} />
    </AbsoluteFill>
  );
};

// B · SELLO — la firma que nadie puso, estampada encima.
const SB: React.FC<{n: number}> = ({n}) => {
  const f = FICHAS[n];
  const rot = n === 1 ? -9 : 7;
  const pos = n === 1 ? {left: 380, top: 250} : {left: 20, top: 720};
  return (
    <AbsoluteFill style={{background: C.tinta}}>
      <Placa src={f.src} w={f.w} s={f.s} x={f.x} y={f.y} />
      <svg width={W} height={H} style={abs({left: 0, top: 0})}>
        <defs>
          <filter id={`sb${n}`}>
            <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed={n * 5} result="r" />
            <feColorMatrix in="r" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.1 1.45" result="a" />
            <feComposite in="SourceGraphic" in2="a" operator="in" />
          </filter>
        </defs>
        <g filter={`url(#sb${n})`} transform={`translate(${pos.left} ${pos.top}) rotate(${rot})`}>
          <rect x="0" y="0" width="620" height="330" fill="none" stroke={C.rosa} strokeWidth="14" />
          <rect x="22" y="22" width="576" height="286" fill="none" stroke={C.rosa} strokeWidth="5" />
          <text x="44" y="150" fontSize="128" fill={C.rosa} style={{fontFamily: VOZ.narrow, fontWeight: 700, letterSpacing: "-2px"}}>NADIE LO</text>
          <text x="44" y="276" fontSize="128" fill={C.rosa} style={{fontFamily: VOZ.narrow, fontWeight: 700, letterSpacing: "-2px"}}>FIRMÓ</text>
          <text x="400" y="276" fontSize="96" fill={C.rosa} style={{fontFamily: VOZ.editorial, fontStyle: "italic"}}>Nº{f.n}</text>
        </g>
      </svg>
      <div style={abs({left: 48, bottom: 48, ...mono(C.offwhite, {fontSize: 17})})}>Recreación publicitaria</div>
      <Grano op={0.16} />
    </AbsoluteFill>
  );
};

// C · CINTA — el rosa como material: cinta de peligro que cruza el lienzo.
const SC: React.FC<{n: number}> = ({n}) => {
  const f = FICHAS[n];
  const c = CERCA[n];
  const rot = n === 1 ? -14 : -7;
  const top = n === 1 ? 980 : 644;
  const texto = `NADIE LO FIRMÓ · Nº${f.n} · `.repeat(6);
  return (
    <AbsoluteFill style={{background: C.tinta}}>
      <Placa src={f.src} w={f.w} s={c.s} x={c.x} y={c.y} />
      <div style={abs({left: -200, top, width: W + 400, height: 150, background: C.rosa,
        transform: `rotate(${rot}deg)`, boxShadow: "0 16px 30px rgba(0,0,0,0.35)", overflow: "hidden"})}>
        <div style={abs({left: 0, top: 18, ...narrow(118, C.tinta)})}>{texto}</div>
      </div>
      <div style={abs({left: 48, top: 48, ...mono(C.offwhite, {fontSize: 17})})}>Recreación publicitaria</div>
      <Grano op={0.16} />
    </AbsoluteFill>
  );
};

// D · PORTADA — revista de cultura urbana: la cabecera se come el lienzo.
const SD: React.FC<{n: number}> = ({n}) => {
  const f = FICHAS[n];
  return (
    <AbsoluteFill style={{background: C.tinta}}>
      <Placa src={f.src} w={f.w} {...POS_D[n]} />
      <div style={abs({left: -24, top: -34, ...narrow(390, C.offwhite, {letterSpacing: "-0.035em"})})}>NADIE</div>
      <div style={abs({left: 300, top: 250, ...serif(210, TINTE_D[n])})}>lo firmó</div>
      <div style={abs(n === 1 ? {right: 44, top: 520} : n === 2 ? {left: 30, top: 900} : {right: 40, top: 960})}>
        <div style={serif(300, n === 3 ? "#E3B341" : C.offwhite)}>{f.n}</div>
      </div>
      <div style={abs({left: 48, bottom: 48, ...mono(C.offwhite, {fontSize: 17})})}>
        Nº{f.n} · Santiago · Recreación publicitaria
      </div>
      <Grano op={0.16} />
    </AbsoluteFill>
  );
};

const ESTUDIOS = [E1, E2, E3, E4, E5, E6];
const SISTEMAS = [SA, SB, SC, SD];

export const Estudio: React.FC<{k: number}> = ({k}) => {
  asegurarFuentes();
  const E = ESTUDIOS[k - 1];
  return <E />;
};

export const SistemaNadie: React.FC<{sis: number; n: number}> = ({sis, n}) => {
  asegurarFuentes();
  const S = SISTEMAS[sis - 1];
  return <S n={n} />;
};
