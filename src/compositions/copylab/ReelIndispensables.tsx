// ============================================================================
// COPYWRITERS · REEL «INDISPENSABLES DE AGENCIA» (orgánico, 01-10-2026) — v4
// ----------------------------------------------------------------------------
// DIRECCIÓN DE ARTE
//
// Material REAL del equipo: Drive › CONTENIDO ORGÁNICO › JULIO › «INDISPENSABLES DE
// OFICINA» (grabado por Sebastián Serrano en julio). Crudos en raw/copywriters/julio/,
// tramos usados en public/assets/copywriters/indispensables/.
//
// Formato del trend «Appear» (medido, R-41): coreografía de manos → en el golpe aparece
// el objeto. La música la pone Valeria al publicar (R-42): este archivo va SIN canción,
// sólo con los «pop» de aparición.
//
// v4 (Valeria, 01-10: «las tipografías pasan desapercibidas, se ven fomes, quizás va muy
// rápido; transiciones y edición más pro»):
//   · MÁS LENTO: cada objeto se queda 2,2 s (antes 0,8 s) para que el chiste se lea.
//   · TIPOGRAFÍA CON PESO: el «para qué» entra palabra por palabra como sello (ficha
//     cel-flash-stomp de video-shotcraft: 6 f, escala 1,18→0,98→1, giro ±2,5° alterno), en
//     Bebas SemiExpanded grande (118), cada palabra en su PLACA negra; la palabra que decide
//     la frase en placa ROSA con letra negra (R-25). Se lee sobre cualquier fondo y repite la
//     gramática de la placa «DE AGENCIA.» del hook.
//   · TRANSICIONES: barrido (whip-pan, ficha shot-transitions «E»): 8 f que recorren 1,2
//     pantallas con curva pronunciada y desenfoque de movimiento horizontal; cada toma se
//     sostiene ≥20 f a cada lado.
//   · REMATE: «VIERNES.» cae con destello rosa del mundo entero (el mundo tiembla, la
//     palabra no) y cierra en placa negra con la firma (R-23).
//
// HOOK — texto DETRÁS de la persona (silueta con mediapipe, silueta-p1/), rosa #FF3D9C.
// CIERRE — recreación con IA (Seedream 5 Pro + Kling 2.5 con caras, ropa y pasillo
// reales), declarada en pantalla (R-11).
// 01-10-2026: fuera la persona de la botella, ya no trabaja en la agencia (R-43).
//
// 02-10 (Valeria): EXCEPCIONES a pedido de la dueña del sistema — se enumeran los
// indispensables (N°1, N°2, N°3; R-39 los deja fuera del feed) y se quita el rótulo
// «Recreación con IA» (R-11 pide declararla).
//
// Formato 1080×1920 · 30 fps · 456 frames (15,2 s).
//
// 02-10 (feedback del equipo de diseño): clips del iPhone re-etiquetados de HLG/BT.2020 a
// BT.709 (Chrome los tonemapeaba y cambiaban de color contra los de IA y las siluetas);
// mano ajena borrada al final de p1-vacio-2861-largo (scripts/copywriters-indispensables-
// limpia-mano.py); cierre más lejano y corto.
// ============================================================================
import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  OffthreadVideo,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
  Easing,
} from "remotion";
import {C2, VOZ2, SOMBRA_SOBRE_FOTO, asegurarFuentesV2} from "../../brand/copylab/sistemaV2";
import cajasSilueta from "../../../public/assets/copywriters/indispensables/silueta-p1/cajas.json";
import cajasTecho from "../../../public/assets/copywriters/indispensables/silueta-b-techo/cajas.json";
import cajasAterriza from "../../../public/assets/copywriters/indispensables/silueta-b-aterriza/cajas.json";

export const REEL_INDISPENSABLES_FRAMES = 456;

const A = "assets/copywriters/indispensables";
const ROSA = C2.rosa;
const W = 1080;
const BARRIDO = 8;
// Relleno de las placas en «em»: Bebas Neue Pro deja aire sobre las mayúsculas, así que con
// relleno parejo la letra queda baja. Medido sobre el render el 02-10 (Valeria: «que quede
// al medio de la altura»): arriba 0,03 em, abajo 0,12 em centra la caja alta.
const PLACA_ARRIBA = 0.03;
const PLACA_ABAJO = 0.12;

// ── Línea de tiempo ─────────────────────────────────────────────────────────
const T = {
  hook: 0, // primer plano de las manos
  titulo: 15, // el título cae detrás de él
  p1: 60, // persona 1 — aparece
  p2c: 126, // persona 2 — coreografía (entra con barrido)
  p2: 156, // persona 2 — aparece
  p3c: 222, // persona 3 — coreografía (entra con barrido)
  p3: 252, // persona 3 — aparece
  cierre: 318, // la caminata (entra con barrido)
  placa: 414, // firma (02-10: el cierre bajó de 120 a 96 frames)
};

const Video: React.FC<{clip: string; desde?: number}> = ({clip, desde = 0}) => (
  <OffthreadVideo src={staticFile(`${A}/${clip}.mp4`)} startFrom={desde} muted />
);

// ── Barrido (whip-pan) ──────────────────────────────────────────────────────
// `sale`: el plano se va en sus últimos 8 frames. `entra`: llega en sus primeros 8.
const curva = Easing.bezier(0.7, 0, 0.3, 1);
const Barrido: React.FC<{children: React.ReactNode; largo: number; entra?: boolean; sale?: boolean; id: string}> = ({
  children,
  largo,
  entra,
  sale,
  id,
}) => {
  const f = useCurrentFrame();
  let x = 0;
  let blur = 0;
  if (entra && f < BARRIDO) {
    const p = curva(f / BARRIDO);
    x = (1 - p) * W * 1.2;
    blur = 46 * Math.sin(Math.PI * Math.min(1, (f + 1) / BARRIDO));
  }
  if (sale && f >= largo - BARRIDO) {
    const p = curva((f - (largo - BARRIDO)) / BARRIDO);
    x = -p * W * 1.2;
    blur = 46 * Math.sin(Math.PI * p);
  }
  return (
    <AbsoluteFill style={{transform: `translateX(${x}px)`, filter: blur > 0.5 ? `url(#${id})` : undefined}}>
      <svg width={0} height={0} style={{position: "absolute"}}>
        <filter id={id} x="-20%" y="0%" width="140%" height="100%">
          <feGaussianBlur stdDeviation={`${blur} 0`} />
        </filter>
      </svg>
      {children}
    </AbsoluteFill>
  );
};

// ── Tipografía: sello + trazo ───────────────────────────────────────────────
const sello = (f: number, en: number, giro: number) => {
  const p = interpolate(f, [en, en + 6], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.poly(5)),
  });
  const s = f < en ? 0 : p < 0.7 ? interpolate(p, [0, 0.7], [1.18, 0.98]) : interpolate(p, [0.7, 1], [0.98, 1]);
  return {
    opacity: f < en ? 0 : 1,
    transform: `scale(${s}) rotate(${interpolate(p, [0, 1], [giro * 1.6, giro])}deg)`,
    display: "inline-block" as const,
  };
};

// Una frase que entra palabra por palabra, cada palabra en su placa (se lee sobre
// cualquier fondo: pared clara, puerta café o pasillo). Placas negras con letra off white;
// la palabra que decide la frase va en placa ROSA con letra negra (R-25: el rosa es
// señal, va sobre la palabra que manda). `clave` = índices de esas palabras.
const Frase: React.FC<{lineas: string[][]; clave: number[]; en: number; cuerpo?: number}> = ({
  lineas,
  clave,
  en,
  cuerpo = 118,
}) => {
  const f = useCurrentFrame();
  let k = 0;
  return (
    <div style={{textAlign: "center"}}>
      {lineas.map((ln, li) => (
        <div key={li} style={{whiteSpace: "nowrap", marginBottom: cuerpo * 0.1}}>
          {ln.map((w) => {
            const idx = k++;
            const giro = idx % 2 ? -2.5 : 2.5;
            const esClave = clave.includes(idx);
            return (
              <span
                key={idx}
                style={{
                  fontFamily: VOZ2.impacto,
                  fontWeight: 800,
                  fontSize: cuerpo,
                  lineHeight: 1,
                  color: esClave ? C2.negro : C2.offwhite,
                  background: esClave ? ROSA : C2.negro,
                  // Bebas trae aire sobre las mayúsculas: relleno asimétrico (medido 02-10) para que la
                  // letra quede al centro de la altura de la placa.
                  padding: `${cuerpo * PLACA_ARRIBA}px ${cuerpo * 0.14}px ${cuerpo * PLACA_ABAJO}px`,
                  margin: `0 ${cuerpo * 0.04}px`,
                  boxShadow: "0 8px 24px rgba(0,0,0,0.28)",
                  ...sello(f, en + idx * 4, giro),
                }}
              >
                {w}
              </span>
            );
          })}
        </div>
      ))}
    </div>
  );
};

// ── El objeto aparece ───────────────────────────────────────────────────────
const Aparece: React.FC<{clip: string; lineas: string[][]; clave: number[]; numero?: number}> = ({clip, lineas, clave, numero}) => {
  const f = useCurrentFrame();
  const escala = interpolate(f, [0, 8], [1.09, 1.0], {extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  const empuje = interpolate(f, [8, 66], [1.0, 1.035], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const destello = interpolate(f, [0, 3], [0.45, 0], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill>
      <AbsoluteFill style={{transform: `scale(${escala * empuje})`}}>
        <Video clip={clip} desde={30} />
      </AbsoluteFill>
      <AbsoluteFill style={{background: C2.offwhite, opacity: destello}} />
      {/* 02-10 (Valeria): se ENUMERAN los indispensables para que el hook se entienda como
          el inicio de una lista. El número es lo único rosa; el chiste va en placas negras. */}
      <AbsoluteFill style={{alignItems: "center", paddingTop: numero !== undefined ? 180 : 230}}>
        {numero !== undefined && (
          <>
            <Frase lineas={[[`INDISPENSABLE`, `N°${numero}`]]} clave={[0, 1]} en={3} cuerpo={74} />
            <div style={{height: 16}} />
          </>
        )}
        <Frase lineas={lineas} clave={clave} en={numero !== undefined ? 12 : 8} cuerpo={numero !== undefined ? 96 : 118} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ── HOOK: el título detrás de la persona 1 ──────────────────────────────────
const golpeTitulo = (f: number, en: number) => {
  const p = interpolate(f, [en, en + 5], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.back(1.6)),
  });
  return {
    opacity: f < en ? 0 : 1,
    transform: `scale(${interpolate(p, [0, 1], [1.7, 1])}) rotate(${interpolate(p, [0, 1], [-4, 0])}deg)`,
  };
};
const temblor = (f: number, golpes: number[]) => {
  for (const g of golpes) {
    const d = f - g;
    if (d >= 0 && d < 4) return {x: [6, -5, 3, -1][d], y: [-4, 3, -2, 1][d]};
  }
  return {x: 0, y: 0};
};
const HookDetras: React.FC<{yaPuesto?: boolean; largo?: number; volando?: boolean}> = ({yaPuesto, largo = T.p1 - T.titulo, volando}) => {
  const f = useCurrentFrame();
  // En la B el título ya cayó durante el aterrizaje: llega puesto (golpes en el pasado).
  const L = yaPuesto ? [-99, -99, -99] : [6, 16, 26]; // INDIS- · PENSA- · BLES
  const ag = yaPuesto ? -99 : 33;
  const fin = largo;
  // B2: el título se va VOLANDO hacia arriba, letra a letra, y queda un respiro sin texto
  // antes de que aparezcan los objetos (Valeria, 02-10: «el indispensable 1 parece junto al
  // título»). Si no, sale como antes: escala y fundido en los últimos 6 frames.
  const SALE = volando ? fin - 22 : fin - 6; // empieza a irse
  const sale = volando
    ? interpolate(f, [SALE, SALE + 12], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})
    : interpolate(f, [fin - 6, fin], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const saleEsc = volando ? 1 : interpolate(f, [fin - 6, fin], [1, 1.25], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const vuela = (k: number) =>
    volando ? interpolate(f, [SALE + k * 2, SALE + k * 2 + 10], [0, -1500], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.in(Easing.cubic)}) : 0;
  const empuje = volando ? interpolate(f, [SALE, fin], [1, 1.05], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 1;
  const t = temblor(f, [...L, ag]);
  const i = Math.max(0, Math.min(cajasSilueta.length - 1, f));
  const [x, y, w, h] = cajasSilueta[i] as number[];
  return (
    <AbsoluteFill style={{transform: `translate(${t.x}px, ${t.y}px) scale(${empuje})`}}>
      <Video clip="p1-vacio-2861-largo" desde={15} />
      <AbsoluteFill style={{alignItems: "center", paddingTop: 175, opacity: volando ? 1 : sale, transform: `scale(${saleEsc})`}}>
        {["INDIS-", "PENSA-", "BLES"].map((l, k) => (
          <div key={l} style={{transform: `translateY(${vuela(2 - k)}px)`}}>
            <div style={{fontFamily: VOZ2.bloque, fontWeight: 800, fontSize: 212, lineHeight: 0.84, color: ROSA, ...golpeTitulo(f, L[k])}}>
              {l}
            </div>
          </div>
        ))}
      </AbsoluteFill>
      <Img src={staticFile(`${A}/silueta-p1/${String(i).padStart(2, "0")}.png`)} style={{position: "absolute", left: x, top: y, width: w, height: h}} />
      {/* «DE AGENCIA.» delante de él, en placa negra: la etiqueta pegada encima */}
      <AbsoluteFill style={{alignItems: "center", justifyContent: "flex-end", paddingBottom: 450, opacity: volando ? 1 : sale, transform: `translateY(${volando ? -vuela(3) * 1.4 : 0}px)`}}>
        <div style={{...golpeTitulo(f, ag), background: C2.negro, padding: `${92 * PLACA_ARRIBA}px 26px ${92 * PLACA_ABAJO}px`, transformOrigin: "50% 50%"}}>
          <span style={{fontFamily: VOZ2.impacto, fontWeight: 800, fontSize: 92, color: C2.offwhite, lineHeight: 1}}>DE AGENCIA.</span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ── CIERRE ──────────────────────────────────────────────────────────────────
// 02-10 (Pau y Coni: «les cambia la cara al caminar», «esa no soy yo»): plano MÁS LEJANO y
// MÁS CORTO. Sólo el primer tramo del clip, donde vienen lejos, a 0,8× (96 frames = cuadros
// 0–77 del clip); las caras quedan chicas y el cierre dura 3,2 s en vez de 4.
const VIER = 50; // «VIERNES.» cae
const Cierre: React.FC = () => {
  const f = useCurrentFrame();
  const vier = VIER;
  // El mundo destella en rosa en el golpe; la palabra no se mueve (cel-flash-stomp).
  const flash = f >= vier && f < vier + 8 && Math.floor((f - vier) / 2) % 2 === 0 ? 0.42 : 0;
  return (
    <AbsoluteFill>
      <OffthreadVideo src={staticFile(`${A}/cierre-kling.mp4`)} playbackRate={0.8} muted />
      <AbsoluteFill style={{background: ROSA, opacity: flash, mixBlendMode: "multiply"}} />
      {/* Arriba la premisa; abajo, sobre el suelo, el giro. Las caras quedan libres en medio. */}
      <AbsoluteFill style={{alignItems: "center", paddingTop: 230}}>
        <Frase lineas={[["TODO", "ESTO", "ES"], ["INDISPENSABLE."]]} clave={[3]} en={6} cuerpo={100} />
      </AbsoluteFill>
      <AbsoluteFill style={{alignItems: "center", justifyContent: "flex-end", paddingBottom: 400}}>
        <Frase lineas={[["HASTA", "QUE", "LLEGA", "EL"]]} clave={[]} en={30} cuerpo={84} />
        <div style={{transform: "rotate(-5deg)", marginTop: 2}}>
          <div style={{fontFamily: VOZ2.mano, fontWeight: 800, fontSize: 220, lineHeight: 1, color: ROSA, textShadow: SOMBRA_SOBRE_FOTO, ...golpeTitulo(f, vier)}}>
            VIERNES.
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// Placa final: firma R-23 sobre negro, entra como sello.
const Placa: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{background: C2.negro, alignItems: "center", justifyContent: "center"}}>
      <div style={{textAlign: "center", transform: "translateY(-80px)"}}>
        <div style={{fontFamily: VOZ2.bloque, fontWeight: 800, fontSize: 150, lineHeight: 0.9, color: C2.offwhite, ...golpeTitulo(f, 2)}}>
          COPYWRITERS
        </div>
        <div style={{position: "relative", display: "inline-block", marginTop: 26}}>
          <Frase lineas={[["ESTRATEGIA,", "CREATIVIDAD"], ["Y", "RESULTADOS."]]} clave={[3]} en={10} cuerpo={64} />
        </div>
      </div>
    </AbsoluteFill>
  );
};

const SFX: React.FC<{en: number; id: string; vol?: number}> = ({en, id, vol = 0.9}) => (
  <Sequence from={en} durationInFrames={30}>
    <Audio src={staticFile(`${A}/sfx/${id}.mp3`)} volume={vol} />
  </Sequence>
);

// El cuerpo del reel (versión A completa). En la B el primer plano de las manos se
// reemplaza por la caída: `conManos` = false.
const Cuerpo: React.FC<{conManos: boolean; tituloPuesto?: boolean; enumerar?: boolean; extra?: number}> = ({
  conManos,
  tituloPuesto,
  enumerar,
  extra = 0,
}) => {
  const n = (k: number) => (enumerar ? k : undefined);
  return (
    <AbsoluteFill>
      {conManos && (
        <Sequence durationInFrames={T.titulo}>
          <Video clip="hook-2861" desde={78} />
        </Sequence>
      )}
      <Sequence from={T.titulo} durationInFrames={T.p1 - T.titulo + extra}>
        <HookDetras yaPuesto={tituloPuesto} largo={T.p1 - T.titulo + extra} volando={extra > 0} />
      </Sequence>
      {extra > 0 && <SFX en={T.p1 + extra - 22} id="whoosh" vol={0.8} />}
      {/* todo lo que sigue al título se corre `extra` frames */}
      <Sequence from={extra}>

      {/* persona 1 — sale con barrido */}
      <Sequence from={T.p1} durationInFrames={T.p2c - T.p1 + BARRIDO}>
        <Barrido id="b1" largo={T.p2c - T.p1 + BARRIDO} sale>
          <Aparece clip="p1-lleno-2861" numero={n(1)} lineas={[["PARA", "EL", "REEL", "QUE"], ["NADIE", "PIDIÓ."]]} clave={enumerar ? [] : [4, 5]} />
        </Barrido>
      </Sequence>

      {/* persona 2 — entra con barrido, coreografía, aparece, sale con barrido */}
      <Sequence from={T.p2c} durationInFrames={T.p2 - T.p2c}>
        <Barrido id="b2" largo={T.p2 - T.p2c} entra>
          <Video clip="p2-coreo-2849" />
        </Barrido>
      </Sequence>
      <Sequence from={T.p2} durationInFrames={T.p3c - T.p2 + BARRIDO}>
        <Barrido id="b3" largo={T.p3c - T.p2 + BARRIDO} sale>
          <Aparece clip="p2-lleno-2850" numero={n(2)} lineas={[["PARA", "LA", "REUNIÓN"], ["QUE", "PUDO", "SER"], ["UN", "MAIL."]]} clave={enumerar ? [] : [6, 7]} />
        </Barrido>
      </Sequence>

      {/* persona 3 */}
      <Sequence from={T.p3c} durationInFrames={T.p3 - T.p3c}>
        <Barrido id="b4" largo={T.p3 - T.p3c} entra>
          <Video clip="p4-coreo-2864" />
        </Barrido>
      </Sequence>
      <Sequence from={T.p3} durationInFrames={T.cierre - T.p3 + BARRIDO}>
        <Barrido id="b5" largo={T.cierre - T.p3 + BARRIDO} sale>
          <Aparece clip="p4-lleno-2864" numero={n(3)} lineas={[["PARA", "LA", "IDEA"], ["DE", "LAS", "18:59."]]} clave={enumerar ? [] : [5]} />
        </Barrido>
      </Sequence>

      {/* cierre — entra con barrido */}
      <Sequence from={T.cierre} durationInFrames={T.placa - T.cierre}>
        <Barrido id="b6" largo={T.placa - T.cierre} entra>
          <Cierre />
        </Barrido>
      </Sequence>
      <Sequence from={T.placa}>
        <Placa />
      </Sequence>

      {/* sonido: sólo efectos (la música la pone Valeria al publicar) */}
      {!tituloPuesto &&
        [T.titulo + 6, T.titulo + 16, T.titulo + 26, T.titulo + 33].map((g) => <SFX key={g} en={g} id="pop_b" vol={0.5} />)}
      <SFX en={T.p1} id="pop_a" />
      <SFX en={T.p2c - 3} id="whoosh" vol={0.6} />
      <SFX en={T.p2} id="pop_b" />
      <SFX en={T.p3c - 3} id="whoosh" vol={0.6} />
      <SFX en={T.p3} id="pop_a" />
      <SFX en={T.cierre - 3} id="whoosh" vol={0.6} />
      <SFX en={T.cierre + VIER} id="pop_b" />
      <SFX en={T.placa + 2} id="pop_a" vol={0.7} />
      </Sequence>
    </AbsoluteFill>
  );
};

// ── VERSIÓN A ───────────────────────────────────────────────────────────────
export const ReelIndispensables: React.FC = () => {
  asegurarFuentesV2();
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      <Cuerpo conManos />
    </AbsoluteFill>
  );
};

// ── VERSIÓN B — el hook es el aterrizaje: rompe el techo de la oficina y cae ────
// (Valeria, 01-10: «el primer personaje aterrizando en la oficina, animado con Magnific»;
// 02-10: «que abra cuando rompe el techo, no desde el cielo; fuera "así llegamos a la
// agencia"; que el hook sea INDISPENSABLES»).
// 1) TECHO: rompe el cielo falso de ESA sala (Seedream 5 Pro con su cara y su ropa reales +
//    Kling 2.5). 2) Corte en la acción a un clip de Kling INVERTIDO (salta hacia arriba
//    desde el cuadro real → al revés cae, aterriza y se para EXACTO en el cuadro real).
// El título INDIS-/PENSA-/BLES cae mientras rompe el techo, DETRÁS de él (siluetas
// silueta-b-techo/ y silueta-b-aterriza/). 02-10 (Valeria: «no queda claro si los textos
// quedan detrás o adelante; haz un efecto bueno»): él ROMPE el título igual que el techo —
// las letras estallan en el corte con destello— y se rearman de golpe cuando aterriza.
// Al seguir el video real el título ya está puesto. Sin rótulo de IA (excepción, ver arriba).
const TECHO = 20; // b-techo, primeros 0,67 s
const ATERRIZA = 73; // b-aterriza (invertido): entra por arriba, aterriza y se para
const ATERRIZA_EN = TECHO + 39; // el frame en que toca el suelo
const HOOK_B = TECHO + ATERRIZA;
const DESFASE_B = HOOK_B - T.titulo; // el cuerpo arranca donde termina el aterrizaje
export const REEL_INDISPENSABLES_B_FRAMES = REEL_INDISPENSABLES_FRAMES + DESFASE_B;
const LB = [3, 11, 19]; // INDIS- · PENSA- · BLES caen mientras rompe el techo

const Silueta: React.FC<{carpeta: string; i: number}> = ({carpeta, i}) => {
  const cajas = carpeta === "silueta-b-techo" ? cajasTecho : cajasAterriza;
  const k = Math.max(0, Math.min(cajas.length - 1, i));
  const [x, y, w, h] = cajas[k] as number[];
  return <Img src={staticFile(`${A}/${carpeta}/${String(k).padStart(2, "0")}.png`)} style={{position: "absolute", left: x, top: y, width: w, height: h}} />;
};

// El título que se rompe: cada letra es una pieza. Cae como sello (LB), estalla cuando
// él pasa por encima (EXPLOTA, el corte con destello) y vuelve de golpe a su lugar
// cuando él toca el suelo (REARMA → ATERRIZA_EN). Trayectorias deterministas.
const EXPLOTA = TECHO + 1;
const VUELA = 14; // frames que dura el estallido
const REARMA = ATERRIZA_EN - 7; // las piezas vuelven en 7 frames y se asientan con el golpe
const azar = (n: number) => {
  const x = Math.sin(n * 127.1 + 311.7) * 43758.5453;
  return x - Math.floor(x);
};
const TituloQueSeRompe: React.FC = () => {
  const f = useCurrentFrame();
  const lineas = ["INDIS-", "PENSA-", "BLES"];
  let n = 0;
  return (
    <AbsoluteFill style={{alignItems: "center", paddingTop: 175}}>
      {lineas.map((l, k) => (
        <div key={l} style={{...golpeTitulo(f, LB[k]), whiteSpace: "nowrap"}}>
          {l.split("").map((c, j) => {
            const id = n++;
            // dirección: hacia afuera del centro del título + ruido
            const lado = (j - (l.length - 1) / 2) / l.length;
            const vx = (lado * 1.6 + (azar(id) - 0.5)) * 1100;
            const vy = (azar(id + 50) * 0.9 + 0.2) * 900 * (k === 0 ? -0.6 : 1);
            const giro = (azar(id + 90) - 0.5) * 720;
            let p = 0; // 0 = en su lugar · 1 = lejos
            if (f >= EXPLOTA && f < REARMA) {
              p = interpolate(f, [EXPLOTA, EXPLOTA + VUELA], [0, 1], {extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
            } else if (f >= REARMA) {
              p = interpolate(f, [REARMA, ATERRIZA_EN], [1, 0], {extrapolateRight: "clamp", easing: Easing.in(Easing.cubic)});
            }
            const velocidad = f >= EXPLOTA && f < EXPLOTA + 6 ? 1 : f >= REARMA && f < ATERRIZA_EN ? 0.8 : 0;
            return (
              <span
                key={j}
                style={{
                  display: "inline-block",
                  fontFamily: VOZ2.bloque,
                  fontWeight: 800,
                  fontSize: 212,
                  lineHeight: 0.84,
                  color: ROSA,
                  transform: `translate(${vx * p}px, ${vy * p}px) rotate(${giro * p}deg) scale(${1 + p * 0.35})`,
                  opacity: p > 0.85 ? interpolate(p, [0.85, 1], [1, 0]) : 1,
                  filter: velocidad ? `blur(${4 + p * 6}px)` : undefined,
                }}
              >
                {c}
              </span>
            );
          })}
        </div>
      ))}
    </AbsoluteFill>
  );
};

const HookB: React.FC = () => {
  const f = useCurrentFrame();
  const destello = interpolate(f, [TECHO - 1, TECHO, TECHO + 3], [0, 0.5, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const t = temblor(f, [...LB, EXPLOTA, ATERRIZA_EN]);
  const enTecho = f < TECHO;
  return (
    <AbsoluteFill style={{transform: `translate(${t.x * 2}px, ${t.y * 2}px)`}}>
      {/* 1 · el plano */}
      <Sequence durationInFrames={TECHO}>
        <Video clip="b-techo" />
      </Sequence>
      <Sequence from={TECHO} durationInFrames={ATERRIZA}>
        <Video clip="b-aterriza" />
      </Sequence>
      {/* 2 · el título, detrás de él: cae, él lo ROMPE al pasar y se rearma cuando aterriza */}
      <TituloQueSeRompe />
      {/* 3 · él, encima del título */}
      {enTecho ? <Silueta carpeta="silueta-b-techo" i={f} /> : <Silueta carpeta="silueta-b-aterriza" i={f - TECHO} />}
      {/* 4 · «DE AGENCIA.» cae cuando toca el suelo */}
      <AbsoluteFill style={{alignItems: "center", justifyContent: "flex-end", paddingBottom: 450}}>
        <div style={{...golpeTitulo(f, ATERRIZA_EN), background: C2.negro, padding: `${92 * PLACA_ARRIBA}px 26px ${92 * PLACA_ABAJO}px`}}>
          <span style={{fontFamily: VOZ2.impacto, fontWeight: 800, fontSize: 92, color: C2.offwhite, lineHeight: 1}}>DE AGENCIA.</span>
        </div>
      </AbsoluteFill>
      <AbsoluteFill style={{background: C2.offwhite, opacity: destello}} />
    </AbsoluteFill>
  );
};

const VersionB: React.FC<{enumerar?: boolean; extra?: number}> = ({enumerar, extra = 0}) => {
  asegurarFuentesV2();
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      <Sequence durationInFrames={HOOK_B}>
        <HookB />
      </Sequence>
      <Sequence from={DESFASE_B}>
        <Cuerpo conManos={false} tituloPuesto enumerar={enumerar} extra={extra} />
      </Sequence>
      {LB.map((g) => (
        <SFX key={g} en={g} id="pop_b" vol={0.55} />
      ))}
      <SFX en={EXPLOTA} id="whoosh" vol={0.8} />
      <SFX en={ATERRIZA_EN} id="pop_a" vol={1} />
    </AbsoluteFill>
  );
};

// B-enumerada (02-10): «INDISPENSABLE N°1, N°2, N°3». Guardada como opción.
export const ReelIndispensablesB: React.FC = () => <VersionB enumerar />;

// B2 (02-10): sin enumerar. El título se queda más y se va volando hacia arriba, letra a
// letra; queda un respiro sin texto y recién aparecen los objetos del N°1.
const EXTRA_B2 = 66 - (T.p1 - T.titulo); // el tramo de pose sin manos alcanza 66 frames
export const REEL_INDISPENSABLES_B2_FRAMES = REEL_INDISPENSABLES_B_FRAMES + EXTRA_B2;
export const ReelIndispensablesB2: React.FC = () => <VersionB extra={EXTRA_B2} />;
