import React from "react";
import {Sequence, staticFile, useCurrentFrame} from "remotion";
import {Audio} from "@remotion/media";
import {
  CLIP,
  AUDIO,
  SANS,
  SLOT,
  CLIP_LEN,
  HALO,
  Lienzo,
  Plano,
  Velo,
  Bloque,
  Suave,
  Enfasis,
  Pie,
  Aire,
  IconoWsp,
  Musica,
} from "./OctubreVideo";

// =============================================================================
// TIERRA CALMA · LOS DOS REELS DE OCTUBRE · V3
// Grilla rehecha por el cliente el 22-09-2026 a las 16:12Z. Manda ésta.
//
// Qué cambió respecto de lo entregado el 14-09:
//   · el reel de dron pasó de 4 a SEIS cortes, con estructura nueva
//     (hook → ubicación → espacio → lo que compras → info comercial → cierre)
//   · el reel de primavera lleva los subtítulos que la grilla ahora DICTA,
//     palabra por palabra
//   · ⭐ los planos del reel de dron NO son IA: son las aéreas REALES del
//     rodaje del 07-08 (21 MP, `raw/tierracalma/fotos-reales/dron/`),
//     recortadas a 9:16, gradeadas para sacarles la calima de la mañana
//     nublada y animadas con Kling 3.0. El sitio que se ve ES el sitio.
//   · ambos cierran con `tc_cierre.mp4`, el cierre oficial que subió el
//     diseñador el 22-09 (ya viene montado sobre blanco)
//
// ⚠️ "Rol individual" y "Acceso controlado" (corte 4 del reel de dron) NO
// están en la lista blanca del manual. Entran con el OK de Diego del 22-09 y
// siguen SIN confirmación escrita de Fran o Blanca.
//
// Cadena de modelos: Seedream 5 Pro → Kling 3.0 → ElevenLabs Music v2.
// Locución: Antonia Reyes (voz chilena), una línea por subtítulo.
// =============================================================================

const CIERRE = 150; // el logo animado dura 5 s a 30 fps
const SOL = 15; // solape de la disolvencia hacia el cierre

export const V3_REEL_D_DURATION = SLOT * 3 + CLIP_LEN - SOL + CIERRE;
export const V3_REEL_I_DURATION = SLOT * 5 + CLIP_LEN - SOL + CIERRE;

const Cierre: React.FC<{desde: number}> = ({desde}) => (
  <Sequence from={desde} durationInFrames={CIERRE + SOL}>
    <Plano src={staticFile("assets/tierracalma/tc_cierre.mp4")} indice={1} />
  </Sequence>
);

// -----------------------------------------------------------------------------
// D · 01/10 · REEL "La primavera llegó a Tierra Calma" · Pilar 4
// -----------------------------------------------------------------------------

const VOZ: {a: string; desde: number; dura: number}[] = [
  {a: "vp1", desde: 30, dura: 59},
  {a: "vp2", desde: 170, dura: 88},
  {a: "vp3", desde: 310, dura: 64},
];

export const V3ReelPrimavera: React.FC = () => (
  <Lienzo>
    <Sequence from={0} durationInFrames={CLIP_LEN}>
      <Plano src={CLIP("p1")} indice={0} />
    </Sequence>
    <Sequence from={SLOT} durationInFrames={CLIP_LEN}>
      <Plano src={CLIP("p2")} indice={1} />
    </Sequence>
    <Sequence from={SLOT * 2} durationInFrames={CLIP_LEN}>
      <Plano src={CLIP("p3")} indice={2} />
    </Sequence>
    <Sequence from={SLOT * 3} durationInFrames={CLIP_LEN}>
      <Plano src={CLIP("p4")} indice={3} />
    </Sequence>
    <Velo arriba={0.32} abajo={0.46} />

    {/* Los subtítulos los DICTA la grilla: no se reescriben. */}
    <Bloque desde={25} dura={92} pos="abajo">
      <Suave size={48}>La primavera ya llegó a Tierra Calma</Suave>
    </Bloque>
    <Bloque desde={165} dura={108} pos="abajo">
      <Enfasis size={62}>Más verde, más luz, más espacio</Enfasis>
    </Bloque>
    <Bloque desde={305} dura={96} pos="arriba">
      <Suave size={46}>Así se siente el cambio de estación acá</Suave>
    </Bloque>
    <Bloque desde={445} dura={120} pos="centro" sinSalida>
      <Enfasis size={58}>{"Tierra Calma\nPadre Hurtado"}</Enfasis>
      <Aire h={40} />
      <Pie>Déjanos tus dudas por WhatsApp</Pie>
    </Bloque>

    {VOZ.map((v) => (
      <Sequence key={v.a} from={v.desde} durationInFrames={v.dura + 10}>
        <Audio src={AUDIO(v.a)} volume={1} />
      </Sequence>
    ))}
    <Musica
      src={AUDIO("mus_primavera_v3")}
      vol={0.26}
      duracion={V3_REEL_D_DURATION}
      baja={VOZ.map((v) => [v.desde, v.desde + v.dura] as [number, number])}
      volBajo={0.09}
    />
    <Cierre desde={SLOT * 3 + CLIP_LEN - SOL} />
  </Lienzo>
);

// -----------------------------------------------------------------------------
// I · 13/10 · REEL "Conoce Tierra Calma" · SEIS cortes · aéreas REALES
// -----------------------------------------------------------------------------

const Bullet: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      display: "flex",
      alignItems: "center",
      gap: 14,
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: 40,
      color: "#fff",
      textShadow: HALO,
      marginBottom: 12,
    }}
  >
    <svg width={26} height={26} viewBox="0 0 24 24" fill="none" style={{flexShrink: 0}}>
      <circle cx="12" cy="12" r="9.2" stroke="#fff" strokeWidth="1.5" />
      <path
        d="M8 12.3l2.7 2.7L16 9.6"
        stroke="#fff"
        strokeWidth="1.8"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
    {children}
  </div>
);

export const V3ReelDron: React.FC = () => {
  const frame = useCurrentFrame();
  const pulso = 1 + Math.sin((frame - 715) / 7) * 0.05;
  return (
    <Lienzo>
      {["a1", "a2", "a3", "a4", "a5", "a6"].map((n, i) => (
        <Sequence key={n} from={SLOT * i} durationInFrames={CLIP_LEN}>
          <Plano src={CLIP(n)} indice={i} />
        </Sequence>
      ))}
      <Velo arriba={0.4} abajo={0.46} />

      {/* CORTE 1 · hook */}
      <Bloque desde={14} dura={118} pos="arriba">
        <Suave size={44}>{"¿Buscando una parcela\nen Padre Hurtado?"}</Suave>
        <Aire h={18} />
        <Enfasis size={56}>{"Esto es lo que encontrarás\nen Tierra Calma."}</Enfasis>
      </Bloque>

      {/* CORTE 2 · ubicación y acceso */}
      <Bloque desde={154} dura={118} pos="arriba">
        <Pie>Padre Hurtado · RM</Pie>
        <Aire h={22} />
        <Enfasis size={58}>{"A 15 min del Peaje\nPadre Hurtado"}</Enfasis>
        <Aire h={20} />
        <Suave size={36}>{"y conectado con las principales\nvías del sector."}</Suave>
      </Bloque>

      {/* CORTE 3 · el espacio. La cifra es el elemento más grande de la pieza. */}
      <Bloque desde={294} dura={118} pos="arriba">
        <Enfasis size={74}>{"Cerca de 5.000 m²"}</Enfasis>
        <Aire h={18} />
        <Suave size={38}>
          {"para hacer realidad tu proyecto.\nMás espacio para construir,\ndisfrutar y proyectar."}
        </Suave>
      </Bloque>

      {/* CORTE 4 · lo que estás comprando */}
      <Bloque desde={434} dura={118} pos="arriba">
        <Suave size={42}>Tu parcela cuenta con:</Suave>
        <Aire h={26} />
        <div style={{display: "flex", flexDirection: "column", alignItems: "flex-start"}}>
          <Bullet>Electricidad hasta cada parcela</Bullet>
          <Bullet>Rol individual</Bullet>
          <Bullet>Cierre perimetral</Bullet>
          <Bullet>Acceso controlado</Bullet>
        </div>
      </Bloque>

      {/* CORTE 5 · información comercial */}
      <Bloque desde={574} dura={118} pos="arriba">
        <Enfasis size={70}>{"Parcelas desde\nUF 2.500"}</Enfasis>
        <Aire h={26} />
        <Pie>Tierra Calma · Padre Hurtado</Pie>
      </Bloque>

      {/* CORTE 6 · cierre */}
      <Bloque desde={714} dura={125} pos="centro" sinSalida>
        <Suave size={40}>{"Hay cosas que una foto\nno puede mostrarte."}</Suave>
        <Aire h={22} />
        <Enfasis size={54}>{"Ven a conocer tu próxima\nparcela en persona."}</Enfasis>
        <Aire h={34} />
        <div style={{transform: `scale(${pulso})`}}>
          <IconoWsp s={50} />
        </div>
        <Aire h={18} />
        <Pie>Agenda tu visita por WhatsApp</Pie>
      </Bloque>

      <Musica src={AUDIO("mus_dron_v2")} vol={0.3} duracion={V3_REEL_I_DURATION} />
      <Cierre desde={SLOT * 5 + CLIP_LEN - SOL} />
    </Lienzo>
  );
};
