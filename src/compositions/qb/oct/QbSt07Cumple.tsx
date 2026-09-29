/**
 * QB · ST 07-10 · 16:00 · ESTÁTICA — CUMPLEAÑOS EN QB  (ST n°3 S1)
 *
 * BRIEF (grilla octubre, STORIES col. E, OK PARA DISEÑAR desde el 28-09 tarde):
 *   Collage de 3 momentos de una celebración con cortes orgánicos y dibujos a
 *   mano. Texto: «Convierte tu cumpleaños en una noche inolvidable» · «5 tragos
 *   de cortesía para el cumpleañero/a» · «Shots de regalo · Postre · Cuenta
 *   separadas · Puedes traer tu propia torta». Interacción: ARMA EL GRUPO Y
 *   RESERVA AHORA (link reserva mesas).
 * COMENTARIO DEL CLIENTE: «veamos opción más simple, siendo una story mostraría
 *   la información más importante de inmediato» (R-43) → sin collage.
 *
 * DIRECCIÓN DE ARTE
 *   · UNA foto a sangre: la torta con bengalas llegando a la mesa (generada, no
 *     hay cumpleaños en las sesiones) → «Imagen referencial».
 *   · La información va ARRIBA y de inmediato.
 *   · ⭐ RONDA 10 (Eli 28-09): «no me gusta la tipografía: usa la Bell para
 *     "convierte tu cumpleaños" y Raleway en "una noche inolvidable"; el "5 tragos
 *     de cortesía" que tenga un ícono igual que la referencia, y lo mismo para
 *     shots de regalo, postre, cuenta separada y puedes traer tu propia torta; la
 *     torta está un poco feíta: añádele detalles verdes como de QB».
 *     → Titular en Bell MT + bajada en Raleway fina. Cada beneficio en su línea con
 *     un ÍCONO DE LÍNEA fino delante, como la ubicación y el teléfono de la ref
 *     «CHEERS». Torta reeditada: cinta verde QB, flores de azúcar verde salvia,
 *     servilleta verde.
 *   · ⭐ RONDA 11 (Eli 28-09): «las tortas tienen decoraciones extrañas, que se vea
 *     una torta bonita de cumpleaños» → torta reeditada: blanca lisa, perlas, cinta
 *     verde QB y ramitas finas arriba. «"Convierte tu cumpleaños" en mayúscula y
 *     "tu cumpleaños" abajo» → CONVIERTE / TU CUMPLEAÑOS en Bell MT. «Los íconos en
 *     recuadros oscurecidos, estilo botones» → cada beneficio es un recuadro negro
 *     translúcido con el ícono y el texto.
 *   · Aire abajo para el sticker del link («ARMA EL GRUPO Y RESERVA AHORA»).
 *   · «Cuenta separadas» va literal del brief (concordancia consultada a contenido).
 *
 * ⭐ RONDA DE CONSTANZA (jefa de diseño, grilla 29-09): «ojo con la separación del
 *   título de historia con el logo, mantengamos a todas la misma separación» →
 *   logo→CONVIERTE pasa de 36 a 53 px, la del AYCD (bloque del KV): el logo no se
 *   mueve (está en el tope de la zona segura) y todo lo de abajo baja 16,5 px.
 *   «Los bullets de los beneficios están muuuy largos, que sean un poco más cortos,
 *   manda el primer beneficio porque es el más largo, pero déjale un poco menos de
 *   aire al fin de la frase» → los cinco recuadros toman el ancho del primero
 *   (max-content) y cierran con el mismo aire que abren (26 px por lado), centrados.
 *
 * ⭐⭐ RONDA 19 — PASA A ANIMADA (Scarlette, hilo en STORIES!E14, 29-09): «ajusté el
 *   formato a animado y te dejé los nuevos textos». Cambiaron los beneficios:
 *   Texto 1: Convierte tu cumpleaños en una noche inolvidable.
 *   Texto 2: DESDE 8 PERSONAS · El cumpleañero recibe 4 tragos + Bucket de 6
 *     cervezas o botella de espumante.
 *   Texto 3: Y SI LA LISTA LLEGA A 15… · Refill ilimitado de 1 trago - bucket de
 *     cervezas - botella de espumante.
 *   Texto 4: HAZ LA LISTA. NOS VEMOS EN QB. · Postre · torta propia · cuentas
 *     divididas · packs de shots.
 *   → Se conserva lo aprobado (foto, logo, titular Bell + Raleway, recuadro oscuro
 *     con filete). Lo que se anima es la INFORMACIÓN: el texto 2 aparece de
 *     inmediato (R-43, «mostraría la información más importante de inmediato») y
 *     el 3 y el 4 lo reemplazan en el mismo recuadro (sin puntos de avance: sobre
 *     las bengalas no se veían). La foto se acerca muy lento (zoom por tamaño, nunca scale()).
 *     Dos voces: Bell MT en el titular y Raleway en todo lo demás.
 *   Estática (la que va a la grilla) = el fotograma del texto 2.
 */
import React from "react";
import {AbsoluteFill, Easing, interpolate, useCurrentFrame} from "remotion";

import {cargarFuentesQbOct, CIFRAS, FotoQB, ImagenReferencial, Linea, LogoQB, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST07_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "CONVIERTE TU CUMPLEAÑOS",
  bajada: "en una noche inolvidable",
  },
  t2: {
  antetitulo: "DESDE 8 PERSONAS",
  recibe: "El cumpleañero recibe",
  fuerte: "4 tragos",
  texto: "+ Bucket de 6 cervezas o botella de espumante",
  },
  t3: {
  antetitulo: "Y SI LA LISTA LLEGA A 15…",
  fuerte: "Refill ilimitado de 1 trago",
  texto: "Bucket de cervezas · Botella de espumante",
  },
  t4: {
  antetitulo: "HAZ LA LISTA. NOS VEMOS EN QB",
  texto: "Postre · Torta propia · Cuentas divididas · Packs de shots",
  },
};

/** 30 fps: texto 2 desde el comienzo, 3 y 4 cada 3 s; el 4 se queda. */
export const QB_ST07_DURACION = 330;
const CAMBIOS = [0, 105, 210];
const FUNDE = 14;
/** Fotograma de la estática: el texto 2 ya asentado. */
export const QB_ST07_ESTATICA = 80;

// ───────────────────────────────────────────────────────────────────────────
// Íconos de línea (trazo 2,2 sobre caja de 44): el registro de los íconos de
// ubicación y teléfono de la ref — finos, sin relleno.
// ───────────────────────────────────────────────────────────────────────────
const T = {fill: "none", stroke: "#fff", strokeWidth: 2.2, strokeLinecap: "round" as const, strokeLinejoin: "round" as const};
const ICONOS: Record<string, React.ReactNode> = {
  copa: <><path d="M9 8 H35 L22 23 Z" {...T} /><path d="M22 23 V37 M15 37 H29" {...T} /><path d="M29 8 L34 3" {...T} /></>,
  shot: <><path d="M13 8 H31 L28 37 H16 Z" {...T} /><path d="M14.3 19 H29.7" {...T} /></>,
  postre: <><path d="M10 21 H34 L30 37 H14 Z" {...T} /><path d="M10 21 C10 10 34 10 34 21" {...T} /><circle cx="22" cy="8" r="2.6" {...T} /></>,
  cuenta: <><path d="M12 5 H32 V38 L28.7 35.5 L25.3 38 L22 35.5 L18.7 38 L15.3 35.5 L12 38 Z" {...T} /><path d="M17 13 H27 M17 19 H27 M17 25 H24" {...T} /></>,
  torta: <><path d="M8 24 H36 V38 H8 Z" {...T} /><path d="M8 30 C12 33 16 27 22 30 C28 33 32 27 36 30" {...T} /><path d="M15 24 V17 M22 24 V15 M29 24 V17" {...T} /><path d="M15 12.5 V13 M22 10.5 V11 M29 12.5 V13" {...T} strokeWidth={3.4} /></>,
};

/** Constanza 29-09: logo→titular = 53 px, la misma separación que el AYCD. */
const AIRE_LOGO = 16.5;

const Item: React.FC<{icono: string; children: React.ReactNode; fuerte?: boolean}> = ({
  icono, children, fuerte = false,
}) => (
  <div style={{height: 68, boxSizing: "border-box",
    display: "flex", alignItems: "center", gap: 20, padding: "0 26px", borderRadius: 12,
    background: "rgba(8,10,9,.62)", border: "1px solid rgba(255,255,255,.14)",
    color: "#fff", fontFamily: "Raleway", fontWeight: fuerte ? 700 : 500, fontSize: fuerte ? 30 : 29, ...CIFRAS}}>
    <svg width={42} height={42} viewBox="0 0 44 44" style={{flex: "none"}}>
      {ICONOS[icono]}
    </svg>
    <span>{children}</span>
  </div>
);

/** Recuadro de la información: el mismo vidrio oscuro con filete de la aprobada. */
const Recuadro: React.FC<{i: number; children: React.ReactNode}> = ({i, children}) => {
  const f = useCurrentFrame();
  const ini = CAMBIOS[i];
  const fin = CAMBIOS[i + 1];
  const entra = i === 0 ? interpolate(f, [4, 4 + FUNDE], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})
    : interpolate(f, [ini, ini + FUNDE], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const sale = fin === undefined ? 0 : interpolate(f, [fin - 2, fin + FUNDE - 6], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const op = entra * (1 - sale);
  if (op <= 0) return null;
  const dy = (1 - Easing.out(Easing.cubic)(entra)) * 26 - sale * 18;
  return (
    <div style={{position: "absolute", top: 660 + AIRE_LOGO + dy, left: 0, right: 0, display: "flex",
      justifyContent: "center", opacity: op}}>
      <div style={{width: 820, boxSizing: "border-box", padding: "34px 40px 38px", borderRadius: 14,
        background: "rgba(8,10,9,.64)", border: "1px solid rgba(255,255,255,.16)", textAlign: "center",
        color: "#fff", fontFamily: "Raleway", ...CIFRAS}}>
        {children}
      </div>
    </div>
  );
};

const Ante: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div style={{fontSize: 30, fontWeight: 700, letterSpacing: "0.14em", marginBottom: 18}}>{children}</div>
);
const Fuerte: React.FC<{children: React.ReactNode; icono?: string}> = ({children, icono}) => (
  <div style={{display: "flex", alignItems: "center", justifyContent: "center", gap: 18, fontSize: 50,
    fontWeight: 800, lineHeight: 1.1}}>
    {icono && <svg width={52} height={52} viewBox="0 0 44 44" style={{flex: "none"}}>{ICONOS[icono]}</svg>}
    <span>{children}</span>
  </div>
);
const Texto: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div style={{fontSize: 31, fontWeight: 400, lineHeight: 1.3, marginTop: 14}}>{children}</div>
);

export const QbSt07Cumple: React.FC = () => {
  const f = useCurrentFrame();
  const d = QB_ST07_DATA;
  const zoom = interpolate(f, [0, QB_ST07_DURACION], [1, 1.06]);
  const [x1, x2, x3, x4] = d.t4.texto.split(" · ");
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoQB src="assets/hilton/qb/oct/07-cumple-torta-verde.jpg" ratio={1770 / 2360} cx={0.5} zoom={zoom} />
      <Velo arriba={[1100, 0.85]} abajo={[520, 0.8]} />
      <LogoQB top={250} ancho={160} />
      <Linea top={372 + AIRE_LOGO} cuerpo={70} familia="BellMT" tracking="0.02em" interlinea={1.02}>
        CONVIERTE<br />TU CUMPLEAÑOS
      </Linea>
      <Linea top={528 + AIRE_LOGO} cuerpo={48} peso={300} tracking="0.01em">{d.pieza.bajada}</Linea>
      <Recuadro i={0}>
        <Ante>{d.t2.antetitulo}</Ante>
        <div style={{fontSize: 30, fontStyle: "italic", fontWeight: 300, marginBottom: 10}}>{d.t2.recibe}</div>
        <Fuerte icono="copa">{d.t2.fuerte}</Fuerte>
        <Texto>{d.t2.texto}</Texto>
      </Recuadro>
      <Recuadro i={1}>
        <Ante>{d.t3.antetitulo}</Ante>
        <Fuerte icono="copa">{d.t3.fuerte}</Fuerte>
        <Texto>{d.t3.texto}</Texto>
      </Recuadro>
      <Recuadro i={2}>
        <Ante>{d.t4.antetitulo}</Ante>
        <div style={{display: "grid", gridTemplateColumns: "1fr 1fr", gap: "18px 24px", marginTop: 6,
          fontSize: 31, fontWeight: 500, textAlign: "left"}}>
          {([["postre", x1], ["torta", x2], ["cuenta", x3], ["shot", x4]] as const).map(([ic, t]) => (
            <div key={ic} style={{display: "flex", alignItems: "center", gap: 14}}>
              <svg width={42} height={42} viewBox="0 0 44 44" style={{flex: "none"}}>{ICONOS[ic]}</svg>
              <span>{t}</span>
            </div>
          ))}
        </div>
      </Recuadro>

      <ImagenReferencial top={1556} />
    </AbsoluteFill>
  );
};
