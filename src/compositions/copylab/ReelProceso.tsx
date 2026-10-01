// ============================================================================
// COPYWRITERS · REEL «LOS 16 CORTES» — trend «Process» (octubre 2026)
// ----------------------------------------------------------------------------
// DIRECCIÓN DE ARTE
//
// Prueba de las skills de reels (tt-trend-mapper, 7/8 → subirse). Propuesta para
// el equipo de redes sociales: la grilla es de ellos, no del estudio.
//
// EL TREND (medido sobre el reel de referencia ig-DcevnEKRwBA, 7,47 s, 152 BPM):
// cuatro capítulos con una etiqueta centrada que NO se mueve —«The inspo» →
// «The sourcing» → «The sewing» → «The result»— y cada cambio clavado en un golpe
// del audio: 0,37 s · 1,33 s · 2,97 s · 4,53 s. El resultado se queda quieto casi
// 3 s. Se respeta esa métrica al frame.
//
// EL GIRO: en el tercer capítulo el trend muestra UNA toma del oficio. Nosotros
// mostramos los 16 cortes reales del CAP.02 de G, uno por cada ~3 frames. El
// proceso de una agencia es eso: versiones. La cifra es la medida (16 archivos en
// out/gcl/cap02-v3/corte/), no la de PostG (R-10).
//
// TODO es material real del repo: el texto del GUION V3, los keyframes de la
// prueba Pro vs Seedream, un cuadro de cada corte y el tramo del robot dios del
// corte 16. No se generó nada para esta pieza.
//
// Etiqueta: Neue Haas Grotesk Text en caja mixta (texto funcional, R-31), con
// sombra corta sobre foto (R-30). Sin logo, sin enumeraciones, sin microtexto
// (R-08, R-39). El rosa ya está en la escena (el halo de G): no se agrega.
//
// AUDIO: `conMusica` pone el audio del trend SOLO como pista temporal para juzgar
// el ritmo. El audio real se agrega en la app de Instagram al publicar (licencia
// por tipo de cuenta). La versión limpia se rinde sin audio.
//
// Formato 1080×1920 · 30 fps · 224 frames (7,47 s).
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
} from "remotion";
import {C2, VOZ2, SOMBRA_SOBRE_FOTO, asegurarFuentesV2} from "../../brand/copylab/sistemaV2";

export const REEL_PROCESO_FRAMES = 224;

// Cortes medidos en la referencia (frames a 30 fps).
const REVELA = 11; // 0,37 s — la página sale del negro
const CAP2 = 40; // 1,33 s
const CAP3 = 89; // 2,97 s
const CAP4 = 136; // 4,53 s

const A = "assets/copywriters/proceso";

const Etiqueta: React.FC<{texto: string; sobreClaro?: boolean}> = ({texto, sobreClaro}) => (
  <AbsoluteFill style={{alignItems: "center", justifyContent: "center"}}>
    <div
      style={{
        fontFamily: VOZ2.cuerpo,
        fontWeight: 500,
        fontSize: 64,
        letterSpacing: -0.5,
        color: sobreClaro ? C2.negro : C2.offwhite,
        textShadow: sobreClaro ? "none" : SOMBRA_SOBRE_FOTO,
        transform: "translateY(-40px)",
      }}
    >
      {texto}
    </div>
  </AbsoluteFill>
);

const Cubre: React.FC<{src: string; escala?: number}> = ({src, escala = 1}) => (
  <Img
    src={staticFile(src)}
    style={{width: "100%", height: "100%", objectFit: "cover", transform: `scale(${escala})`}}
  />
);

// Los cortes traen quemada la cabecera «TEMPORADA 1 · CAPÍTULO 02» y el reloj: es
// metadata que el feed ya no lleva (R-39). Se amplía desde abajo para sacarla.
const SIN_CABECERA: React.CSSProperties = {transform: "scale(1.14)", transformOrigin: "50% 100%"};

// Capítulo 1 — el texto real del GUION V3 (gcl-agent/universo/06_VIDEO_REELS/
// CAP_02_TURNO_DE_NOCHE/GUION_V3_MANANA_LO_VEO.md), tal cual.
const ElGuion: React.FC = () => {
  const f = useCurrentFrame();
  const abre = interpolate(f, [0, REVELA, REVELA + 5], [0, 0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const recorte = interpolate(abre, [0, 1], [50, 0]);
  const escala = interpolate(f, [REVELA, CAP2], [1.04, 1.0], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      <AbsoluteFill
        style={{
          background: C2.offwhite,
          clipPath: `inset(${recorte}% ${recorte}% ${recorte}% ${recorte}%)`,
          transform: `scale(${escala})`,
          padding: "300px 90px",
          fontFamily: VOZ2.cuerpo,
          color: C2.negro,
        }}
      >
        <div style={{fontSize: 44, fontWeight: 700, lineHeight: 1.2}}>
          G.CL — CAP.02 · TURNO DE NOCHE
          <br />
          GUION V3 «MAÑANA LO VEO»
        </div>
        <div style={{fontSize: 38, lineHeight: 1.4, marginTop: 40, opacity: 0.85}}>
          El post-it es un pedido del cliente («URGENTE · pedido del cliente: ajustar campaña ·
          ENTREGA 09:00») y Pancho escribe debajo, en lápiz azul, «mañana lo veo, 9 AM :)» antes
          de irse.
        </div>
        <div style={{fontSize: 38, lineHeight: 1.4, marginTop: 560, opacity: 0.85}}>
          El canal entre pisos es un tubo neumático (vidrio y bronce, luces rosadas por piso):
          baja el pedido, sube el trabajo al amanecer, vuelve a bajar la respuesta.
        </div>
      </AbsoluteFill>
      {f >= 0 && <Etiqueta texto="El guion" sobreClaro={abre > 0.5} />}
    </AbsoluteFill>
  );
};

// Capítulo 2 — la prueba real de generadores para los keyframes (Pro vs Seedream).
const LasPruebas: React.FC = () => {
  const f = useCurrentFrame();
  const escala = interpolate(f, [0, CAP3 - CAP2], [1.0, 1.05]);
  const celdas = [
    `${A}/k2-trio-nivel-menos-1-pro.jpg`,
    `${A}/k2-trio-nivel-menos-1-seedream.jpg`,
    `${A}/k3-g-halo-estacion-pro.jpg`,
    `${A}/k3-g-halo-estacion-seedream.jpg`,
  ];
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gridTemplateRows: "1fr 1fr",
          gap: 6,
          width: "100%",
          height: "100%",
          transform: `scale(${escala})`,
        }}
      >
        {celdas.map((c) => (
          <div key={c} style={{overflow: "hidden"}}>
            <Cubre src={c} />
          </div>
        ))}
      </div>
      <Etiqueta texto="Las pruebas" />
    </AbsoluteFill>
  );
};

// Capítulo 3 — EL GIRO: un cuadro de cada uno de los 16 cortes.
const LosCortes: React.FC = () => {
  const f = useCurrentFrame();
  const dur = CAP4 - CAP3;
  const i = Math.min(15, Math.floor((f * 16) / dur));
  const n = String(i + 1).padStart(2, "0");
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      <AbsoluteFill style={SIN_CABECERA}>
        <Cubre src={`${A}/corte${n}.jpg`} />
      </AbsoluteFill>
      <Etiqueta texto="Los 16 cortes" />
    </AbsoluteFill>
  );
};

// Capítulo 4 — el resultado: el tramo del robot dios del corte 16 (8,5 s → 11,7 s).
const ElResultado: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <AbsoluteFill style={SIN_CABECERA}>
      <OffthreadVideo src={staticFile(`${A}/resultado-corte16.mp4`)} muted />
    </AbsoluteFill>
    <Etiqueta texto="El resultado" />
  </AbsoluteFill>
);

export const ReelProceso: React.FC<{conMusica?: boolean}> = ({conMusica = true}) => {
  asegurarFuentesV2();
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      <Sequence durationInFrames={CAP2}>
        <ElGuion />
      </Sequence>
      <Sequence from={CAP2} durationInFrames={CAP3 - CAP2}>
        <LasPruebas />
      </Sequence>
      <Sequence from={CAP3} durationInFrames={CAP4 - CAP3}>
        <LosCortes />
      </Sequence>
      <Sequence from={CAP4} durationInFrames={REEL_PROCESO_FRAMES - CAP4}>
        <ElResultado />
      </Sequence>
      {conMusica && <Audio src={staticFile(`${A}/TEMP-audio-trend-process.mp4`)} />}
    </AbsoluteFill>
  );
};
