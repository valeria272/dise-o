// ============================================================================
// COPYWRITERS · CW-04 — «EN ESTE CYBER, UNA IA TAMBIÉN RECOMIENDA.» · 4 láminas
// ----------------------------------------------------------------------------
// BRIEF     clients/copywriters/briefs/202610_BRIEF_ESTUDIO_copywriters.md (CW-04).
//           Pilar «Tendencias de IA», tipo Editorial → NEGRO. Sale 07-10 12:30.
//           Serie INTERNET DEPT. (formato de la grilla 2609, SIN «VOL.» ni fecha).
// DIRECCIÓN Una página de diario: papel off-white, tinta negra, cabezal con
//           doble filete. Lo editorial ES el negro sobre papel, no un fondo negro.
//           · El rosa marca «IA» en la portada y vuelve sólo donde decide la
//             frase (R-25).
//           · Las secciones van como antetítulo en palabras («QUÉ PASÓ.»), no
//             numeradas: R-39 saca las enumeraciones del feed.
//           · Gesto único: el trazo rosa TACHA «el mejor del mercado» en L4.
//             Acá el tachado es el significado (lo que se elimina); por eso es
//             la única vez que un trazo cruza la letra a propósito (R-26).
//           · Sin mono y sin cajas (jefa de diseño, 01-10).
//           · La fuente del dato va al pie, en caja mixta: es una noticia.
// Formato 1080×1350.
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {C2, VOZ2, asegurarFuentesV2, granoSVG} from "../../brand/copylab/sistemaV2";
import {Linea, Trazo} from "../../brand/copylab/piezasV2";

const M = 80;
const TINTA = C2.negro;

const Papel: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{background: C2.offwhite}}>
    <AbsoluteFill style={{backgroundImage: granoSVG(0.1, 11), backgroundSize: "300px 300px"}} />
    {children}
  </AbsoluteFill>
);

const Filete: React.FC<{y: number; grueso?: number}> = ({y, grueso = 3}) => (
  <div style={{position: "absolute", left: M, right: M, top: y, height: grueso,
               background: TINTA}} />
);

/** Cabezal del diario. Grande en la portada, chico en el interior. */
const Cabezal: React.FC<{grande?: boolean}> = ({grande = false}) => {
  const px = grande ? 132 : 58;
  const top = grande ? 92 : 70;
  return (
    <>
      <Filete y={top - 22} grueso={grande ? 6 : 4} />
      <Filete y={top - 12} grueso={1.5} />
      <div style={{position: "absolute", left: M, right: M, top, display: "flex",
                   justifyContent: "center"}}>
        <Linea cuerpo={px} color={TINTA} tracking={grande ? 2 : 1}>INTERNET DEPT.</Linea>
      </div>
      <Filete y={top + px * 0.84 + 16} grueso={1.5} />
      <Filete y={top + px * 0.84 + 26} grueso={grande ? 6 : 4} />
    </>
  );
};

const Antetitulo: React.FC<{y: number; children: React.ReactNode}> = ({y, children}) => (
  <div style={{position: "absolute", left: M, top: y}}>
    <Linea cuerpo={52} color={TINTA} tracking={2.5}>{children}</Linea>
  </div>
);

const Cuerpo: React.FC<{x?: number; y: number; px?: number; ancho?: number;
                        color?: string; children: React.ReactNode}> =
({x = M, y, px = 42, ancho = 1080 - 2 * M, color = "rgba(11,11,11,0.86)", children}) => (
  <div style={{position: "absolute", left: x, top: y, width: ancho,
               fontFamily: VOZ2.cuerpo, fontWeight: 400, fontSize: px,
               lineHeight: 1.34, color}}>{children}</div>
);

const Fuente: React.FC<{children: React.ReactNode}> = ({children}) => (
  <Cuerpo y={1350 - 135 - 60} px={23} color="rgba(11,11,11,0.55)">{children}</Cuerpo>
);

// ====================== 01 · PORTADA ======================
const L1: React.FC = () => (
  <Papel>
    <Cabezal grande />
    <div style={{position: "absolute", left: M - 6, top: 360}}>
      <Linea cuerpo={170} color={TINTA}>EN ESTE CYBER,</Linea>
      <div style={{height: 22}} />
      <div style={{display: "flex", alignItems: "flex-end", gap: 34}}>
        <Linea cuerpo={170} color={TINTA}>UNA</Linea>
        <Linea cuerpo={170} voz="bloque" color={C2.rosa}>IA</Linea>
      </div>
      <div style={{height: 22}} />
      <Linea cuerpo={170} color={TINTA}>TAMBIÉN</Linea>
      <div style={{height: 22}} />
      <Linea cuerpo={170} color={TINTA}>RECOMIENDA.</Linea>
    </div>
  </Papel>
);

// ====================== 02 · QUÉ PASÓ ======================
const L2: React.FC = () => (
  <Papel>
    <Cabezal />
    <Antetitulo y={250}>QUÉ PASÓ.</Antetitulo>
    <div style={{position: "absolute", left: M - 8, top: 372}}>
      <Linea cuerpo={232} voz="bloque" color={TINTA}>CYBERAI</Linea>
    </div>
    <Cuerpo y={630} px={46}>
      El CyberMonday 2026 estrena un asistente de IA que funciona 24/7 dentro de
      Cyber.cl y le recomienda productos a la gente.
    </Cuerpo>
    <Fuente>Fuente: Cámara de Comercio de Santiago, vía BioBio y The Clinic, 29-09-2026.</Fuente>
  </Papel>
);

// ====================== 03 · POR QUÉ IMPORTA ======================
const L3: React.FC = () => (
  <Papel>
    <Cabezal />
    <Antetitulo y={250}>POR QUÉ IMPORTA.</Antetitulo>
    <div style={{position: "absolute", left: M - 4, top: 370}}>
      <Linea cuerpo={112} color={TINTA}>TUS DESCRIPCIONES</Linea>
      <div style={{height: 12}} />
      <Linea cuerpo={112} color={TINTA}>YA NO LAS LEE</Linea>
      <div style={{height: 12}} />
      <Linea cuerpo={112} color={TINTA}>SÓLO UNA PERSONA.</Linea>
    </div>
    <div style={{position: "absolute", left: M - 4, top: 770, display: "flex",
                 alignItems: "flex-end", gap: 30}}>
      <Linea cuerpo={112} color={TINTA}>LAS LEE UNA</Linea>
      <Linea cuerpo={150} voz="bloque" color={C2.rosa}>IA</Linea>
    </div>
    <Cuerpo y={940} px={50}>que decide qué recomendar.</Cuerpo>
  </Papel>
);

// ====================== 04 · QUÉ HACEMOS ======================
const L4: React.FC = () => (
  <Papel>
    <Cabezal />
    <Antetitulo y={250}>QUÉ HACEMOS.</Antetitulo>
    <Cuerpo y={342} px={42}>Descripciones claras y completas:</Cuerpo>
    <div style={{position: "absolute", left: M - 4, top: 430}}>
      {["QUÉ ES.", "PARA QUIÉN.", "PRECIO.", "STOCK."].map((t) => (
        <div key={t} style={{marginBottom: 14}}>
          <Linea cuerpo={88} color={TINTA}>{t}</Linea>
        </div>
      ))}
    </div>
    <Cuerpo y={884} px={42}>Y nada de</Cuerpo>
    <div style={{position: "absolute", left: M - 4, top: 948}}>
      <div style={{position: "relative"}}>
        <Linea cuerpo={74} color="rgba(11,11,11,0.62)">«EL MEJOR DEL MERCADO».</Linea>
        <Trazo x={-12} y={4} ancho={700} grosor={20} giro={0} />
      </div>
    </div>
    <Cuerpo y={1068} px={32} color="rgba(11,11,11,0.72)" ancho={860}>
      Lo mismo que va a pedir ChatGPT cuando lleguen sus avisos a Chile.
    </Cuerpo>
  </Papel>
);

const LAMINAS = [L1, L2, L3, L4];

export const CW04CyberIA: React.FC<{lamina?: number}> = ({lamina = 1}) => {
  asegurarFuentesV2();
  const L = LAMINAS[Math.min(Math.max(lamina, 1), LAMINAS.length) - 1];
  return <L />;
};
