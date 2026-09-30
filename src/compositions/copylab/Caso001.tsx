// ============================================================================
// COPYWRITERS · CASO 001 — «2X EL RETORNO» · carrusel de 6 láminas
// ----------------------------------------------------------------------------
// DIRECCIÓN DE ARTE — según creative-system/SISTEMA-VISUAL-2609/DIRECCION-DE-ARTE-RRSS.md
//
// No es una infografía: es una HISTORIA en seis momentos. Cada lámina tiene UNA
// idea y se entiende en un segundo. Nada se explica dos veces.
//
// El KPI ES EL DISEÑO. «19,2X» y «47–52%» ocupan más de la mitad de su lámina y
// NO viven dentro de una caja, una tarjeta ni un dashboard: son la composición.
// Lo secundario se descubre después, y por eso está chico y abajo.
//
// Balloon es GESTO, no una segunda capa de texto: aparece una vez por lámina,
// como el comentario al margen de alguien que ya vio el resultado.
//
// La paginación 01/06 se queda —está en la referencia de Valeria— porque dentro
// de un carrusel TIENE función: dice dónde vas en una historia de seis. En un
// post suelto no hay dónde ir, y ahí se elimina.
//
// ⛔ No hay firma COPYWRITERS.CL en ninguna lámina. La identidad se reconoce por
//    el sistema, no por firmar.
// ⛔ El cierre no lleva metodología ni CTA: el aprendizaje ES el cierre.
//
// ⚠️ LAS CIFRAS NO ESTÁN VERIFICADAS. Vienen del board del 30-09 y rige R-10:
//    no se publica sin fuente, ni sin autorización del cliente. PLACEHOLDER
//    hasta que Valeria confirme.
//
// Formato 1080×1350. Fotografía: Seedream 5 Pro (30-09-2026), ambiente y objeto.
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {C2, VOZ2, asegurarFuentesV2, granoSVG} from "../../brand/copylab/sistemaV2";
import {Flecha, Foto, Subrayado} from "../../brand/copylab/piezasV2";

const M = 76;

// --- piezas locales ---------------------------------------------------------

/** Paginación. Discreta, arriba a la izquierda. Sólo existe dentro del carrusel. */
const Pagina: React.FC<{n: number; claro?: boolean}> = ({n, claro = true}) => (
  <div style={{
    position: "absolute", left: M, top: 42,
    fontFamily: VOZ2.data, fontSize: 17, fontWeight: 500, letterSpacing: 2.6,
    color: claro ? "rgba(245,243,238,0.55)" : "rgba(11,11,11,0.45)",
  }}>
    {String(n).padStart(2, "0")} / 06
  </div>
);

/** Bebas. El tamaño lo decide la jerarquía, no una escala. */
const B: React.FC<{
  t: string; px: number; color?: string; li?: number; ls?: number;
}> = ({t, px, color = C2.offwhite, li = 0.84, ls = 0}) => (
  <div style={{
    fontFamily: VOZ2.titular, fontWeight: 700, fontSize: px, lineHeight: li,
    color, textTransform: "uppercase", letterSpacing: ls, whiteSpace: "nowrap",
  }}>{t}</div>
);

/** Balloon. Gesto, una vez por lámina. */
const Bal: React.FC<{
  x: number; y: number; px: number; color?: string; giro?: number;
  li?: number; children: React.ReactNode;
}> = ({x, y, px, color = C2.rosa, giro = -2, li = 1.1, children}) => (
  <div style={{
    position: "absolute", left: x, top: y,
    fontFamily: VOZ2.mano, fontWeight: 700, fontSize: px, color,
    lineHeight: li, transform: `rotate(${giro}deg)`, textTransform: "uppercase",
  }}>{children}</div>
);

/** Texto funcional. Sans limpia, chica. Nunca compite con Bebas. */
const Fn: React.FC<{
  x: number; y: number; px?: number; color?: string; peso?: number;
  li?: number; ls?: number; children: React.ReactNode;
}> = ({x, y, px = 22, color = C2.gris, peso = 400, li = 1.4, ls = 0.6, children}) => (
  <div style={{
    position: "absolute", left: x, top: y,
    fontFamily: VOZ2.cuerpo, fontWeight: peso, fontSize: px, color,
    lineHeight: li, letterSpacing: ls, textTransform: "uppercase",
  }}>{children}</div>
);

/** Círculo de marcador: encierra la frase que remata la lámina. */
const Circulo: React.FC<{
  x: number; y: number; w: number; h: number; giro?: number;
}> = ({x, y, w, h, giro = -4}) => (
  <svg width={w} height={h} style={{
    position: "absolute", left: x, top: y, overflow: "visible",
    transform: `rotate(${giro}deg)`,
  }}>
    <path
      d={`M ${w * 0.5} ${h * 0.04}
          C ${w * 0.9} ${h * 0.02}, ${w * 1.02} ${h * 0.44}, ${w * 0.93} ${h * 0.72}
          C ${w * 0.84} ${h * 0.99}, ${w * 0.3} ${h * 1.03}, ${w * 0.1} ${h * 0.84}
          C ${w * -0.04} ${h * 0.66}, ${w * -0.02} ${h * 0.22}, ${w * 0.32} ${h * 0.07}`}
      stroke={C2.rosa} strokeWidth={7} strokeLinecap="round" fill="none" />
  </svg>
);

const Grano: React.FC = () => (
  <AbsoluteFill style={{backgroundImage: granoSVG(0.05, 5), backgroundSize: "300px 300px"}} />
);

// ===========================================================================
// 01 · LA FOTO MANDA. El dato entra como titular, no como dato.
// ===========================================================================
const L1: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Foto src="assets/copywriters/caso001/01-vino-servido.png" foco="62% 40%" />
    {/* Velo corto sólo por la izquierda: la copa y el chorro quedan intactos. */}
    <AbsoluteFill style={{
      background: "linear-gradient(100deg, rgba(11,11,11,0.94) 0%, rgba(11,11,11,0.72) 34%, rgba(11,11,11,0) 62%)",
    }} />
    <Pagina n={1} />

    {/* El 2X se sale por abajo de su caja y pisa la foto: es imagen, no texto. */}
    <div style={{position: "absolute", left: M - 16, top: 188}}>
      <B t="2X" px={472} />
    </div>
    <div style={{position: "absolute", left: M, top: 606}}>
      <B t="EL RETORNO." px={96} />
    </div>

    <Bal x={M + 4} y={742} px={58} li={1.14}>
      MISMA PAUTA.<br />OTRO COPY.
    </Bal>
    <Subrayado x={M + 6} y={874} ancho={306} alto={30} grosor={11} giro={-2} />
  </AbsoluteFill>
);

// ===========================================================================
// 02 · LA PRUEBA. Dos anuncios reales, uno al lado del otro. Cero explicación.
// ===========================================================================
const Anuncio: React.FC<{
  x: number; y: number; giro: number; foto: string; foco: string; copy: string;
}> = ({x, y, giro, foto, foco, copy}) => (
  <div style={{
    position: "absolute", left: x, top: y, width: 392, height: 588,
    background: C2.offwhite, transform: `rotate(${giro}deg)`,
    boxShadow: "0 34px 76px rgba(0,0,0,0.62)", overflow: "hidden",
  }}>
    <div style={{position: "absolute", inset: 0, height: 304, overflow: "hidden"}}>
      <Foto src={foto} foco={foco} />
    </div>
    <div style={{
      position: "absolute", left: 28, top: 346, width: 336,
      fontFamily: VOZ2.cuerpo, fontWeight: 400, fontSize: 34, lineHeight: 1.24,
      color: C2.negro,
    }}>{copy}</div>
    <div style={{
      position: "absolute", left: 28, bottom: 32, width: 336, padding: "16px 0",
      background: C2.negro, textAlign: "center",
      fontFamily: VOZ2.cuerpo, fontWeight: 500, fontSize: 21, color: C2.offwhite,
      letterSpacing: 0.4,
    }}>Descubrir</div>
  </div>
);

const L2: React.FC = () => (
  <AbsoluteFill style={{background: C2.carbon}}>
    <Foto src="assets/copywriters/caso001/02-concreto.png" foco="50% 50%" oscurecer={0.26} />
    <Pagina n={2} />

    {/* A recibe el plano plano y aburrido; B el dramático. La inversión
          es el argumento: mismo presupuesto, distinta idea. */}
    <Anuncio x={36} y={318} giro={-2.4}
             foto="assets/copywriters/caso001/03-vino-macro.png" foco="50% 50%"
             copy="Vinos para cada momento." />
    <Anuncio x={652} y={352} giro={2}
             foto="assets/copywriters/caso001/01-vino-servido.png" foco="56% 44%"
             copy="Para esas conversaciones que se alargan." />
    <Flecha x={470} y={620} ancho={150} alto={92} giro={4} color="rgba(245,243,238,0.9)" grosor={6} />

    <Bal x={106} y={200} px={46} color={C2.offwhite} giro={-3}>A.<br />GENÉRICO</Bal>
    <Bal x={722} y={232} px={46} color={C2.offwhite} giro={2}>B.<br />POR DOLOR</Bal>

    <Fn x={466} y={506} px={19} color="rgba(245,243,238,0.8)" li={1.35} ls={2}>
      MISMO<br />PRESUPUESTO.
    </Fn>

    <Bal x={392} y={952} px={52} li={1.12}>
      ¿QUÉ CAMBIÓ?<br />LAS PALABRAS.
    </Bal>
    <Subrayado x={396} y={1076} ancho={318} alto={30} grosor={11} giro={-2} />
  </AbsoluteFill>
);

// ===========================================================================
// 03 · PUBLICIDAD CONSTRUIDA DESDE DATA — no un reporte.
// ---------------------------------------------------------------------------
// Los números NO se apilan ordenados: son elementos gráficos.
//
// · 19,2X se sale del lienzo por los DOS lados. Está cropeado a propósito: un
//   número que no cabe se lee como magnitud, no como cifra de planilla.
// · +116% es el SEGUNDO impacto, no un igual: entra más chico, desplazado a la
//   derecha, girado y pisando al primero. La asimetría es la tensión.
// · La comparación (9,8X · 1,09%→2,35%) es letra chica. Se descubre después.
// · Balloon CRUZA el número en diagonal. No es una nota debajo del contenido:
//   es alguien rayando encima del resultado.
// ===========================================================================
const L3: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Foto src="assets/copywriters/caso001/03-vino-macro.png" foco="58% 44%" />
    <AbsoluteFill style={{
      background: "linear-gradient(200deg, rgba(11,11,11,0.55) 0%, rgba(11,11,11,0.9) 46%, rgba(11,11,11,0.99) 100%)",
    }} />
    <Grano />
    <Pagina n={3} />

    {/* Primer impacto: se sale por izquierda y por derecha. */}
    <div style={{position: "absolute", left: -78, top: 286}}>
      <B t="19,2X" px={500} />
    </div>
    <Fn x={790} y={742} px={30} ls={3} color="rgba(245,243,238,0.92)">ROAS</Fn>

    {/* Segundo impacto: más chico, corrido, girado, pisando al primero. */}
    <div style={{
      position: "absolute", left: 386, top: 700,
      transform: "rotate(-4deg)", transformOrigin: "left top",
    }}>
      <B t="+116%" px={238} color={C2.rosa} />
    </div>
    <Fn x={402} y={906} px={26} ls={2.6} color={C2.rosa}>CTR</Fn>

    {/* Balloon atravesando el número. Sin subrayado: el gesto es el cruce. */}
    <div style={{
      position: "absolute", left: 64, top: 520,
      transform: "rotate(-9deg)", transformOrigin: "left top",
      fontFamily: VOZ2.mano, fontWeight: 700, fontSize: 60,
      color: C2.offwhite, textTransform: "uppercase", whiteSpace: "nowrap",
    }}>
      Y NO SUBIMOS LA PAUTA.
    </div>

    {/* La comparación vive chica y abajo. Nunca compite. */}
    <Fn x={M} y={1124} px={21} li={1.6} ls={1} color="rgba(183,183,183,0.8)">
      VS. 9,8X CON COPY GENÉRICO<br />CTR 1,09% → 2,35%
    </Fn>
  </AbsoluteFill>
);

// ===========================================================================
// 04 · CAMBIO DE CANAL. La pantalla ES la prueba.
// ---------------------------------------------------------------------------
// El email va COMPUESTO sobre la pantalla del teléfono, no descrito al lado.
// Un teléfono con la pantalla en blanco no prueba nada: la lámina existe para
// mostrar la pieza que funcionó, y esa pieza es el correo.
//
// La interfaz está medida sobre la foto (pantalla en 362,356 · 382×726, girada
// medio grado) y la escribe el sistema, no la IA.
// ===========================================================================

/** El correo, dentro de la pantalla. Tipografía del sistema, no del generador. */
const Correo: React.FC = () => (
  <div style={{
    position: "absolute", left: 362, top: 356, width: 382, height: 726,
    transform: "rotate(-0.5deg)", transformOrigin: "left top",
    background: "#FFFFFF", overflow: "hidden",
  }}>
    <div style={{
      position: "absolute", left: 20, top: 16, right: 20,
      display: "flex", justifyContent: "space-between",
      fontFamily: VOZ2.cuerpo, fontSize: 14, color: "#9A9A9A", letterSpacing: 0.2,
    }}>
      <span>&#8249;&nbsp;&nbsp;Inbox</span><span>11:24</span>
    </div>

    <div style={{
      position: "absolute", left: 22, top: 62,
      fontFamily: VOZ2.cuerpo, fontSize: 16, color: "#8C8C8C",
    }}>Para ti,</div>

    <div style={{
      position: "absolute", left: 22, top: 90, width: 318,
      fontFamily: VOZ2.cuerpo, fontWeight: 400, fontSize: 28, lineHeight: 1.26,
      color: "#141414",
    }}>Vinos que hacen que la noche se alargue.</div>

    <div style={{position: "absolute", left: 22, top: 236, width: 338, height: 236,
                 overflow: "hidden"}}>
      <Foto src="assets/copywriters/caso001/01-vino-servido.png" foco="54% 52%" />
    </div>

    <div style={{
      position: "absolute", left: 22, top: 508, width: 338, padding: "15px 0",
      background: "#141414", textAlign: "center",
      fontFamily: VOZ2.cuerpo, fontWeight: 500, fontSize: 18, color: "#FFFFFF",
    }}>Ver selección</div>
  </div>
);

const L4: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Foto src="assets/copywriters/caso001/04-telefono.png" foco="56% 62%" />
    <AbsoluteFill style={{
      background: "linear-gradient(176deg, rgba(11,11,11,0.95) 0%, rgba(11,11,11,0.55) 26%, rgba(11,11,11,0) 44%)",
    }} />
    <Pagina n={4} />

    <Correo />

    {/* El titular termina antes de que empiece el teléfono. */}
    <div style={{position: "absolute", left: M, top: 132}}>
      <B t="Y EN EMAIL" px={92} />
      <div style={{display: "flex", gap: 20}}>
        <B t="PASÓ" px={92} />
        <B t="LO MISMO." px={92} color={C2.rosa} />
      </div>
    </div>
    <Subrayado x={M + 194} y={292} ancho={312} alto={28} grosor={10} />

    {/* La Balloon baja al negro limpio del pie: arriba chocaba con la pantalla. */}
    <Bal x={M} y={1146} px={46} li={1.12}>
      MANDAMOS MENOS.<br />VENDIMOS MÁS.
    </Bal>
  </AbsoluteFill>
);

// ===========================================================================
// 05 · EL SEGUNDO DATO. Mismo mecanismo que la 03 — es la rima de la historia.
// ===========================================================================
const L5: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Foto src="assets/copywriters/caso001/05-corcho.png" foco="72% 42%" />
    <AbsoluteFill style={{
      background: "linear-gradient(96deg, rgba(11,11,11,0.97) 0%, rgba(11,11,11,0.82) 40%, rgba(11,11,11,0) 72%)",
    }} />
    <Pagina n={5} />

    <div style={{position: "absolute", left: M - 8, top: 236}}>
      <B t="47–52%" px={196} />
    </div>
    <Fn x={M} y={432} px={30} ls={2.6}>APERTURA</Fn>

    <div style={{position: "absolute", left: M - 8, top: 556}}>
      <B t="4–11" px={196} />
    </div>
    <Fn x={M} y={752} px={30} ls={2.6}>ÓRDENES</Fn>

    {/* Va sobre el negro limpio, NO sobre el sacacorchos: ahí era ilegible. */}
    <Bal x={116} y={906} px={50} li={1.08} giro={-3}>SEGMENTAR<br />&gt; SATURAR.</Bal>
    <Circulo x={64} y={866} w={426} h={214} />

    <Fn x={M} y={1176} px={20} li={1.55} ls={1.1} color="rgba(183,183,183,0.82)">
      VS. 10–28% APERTURA / 0–1 ÓRDENES<br />ENVIANDO A TODA LA BASE.
    </Fn>
  </AbsoluteFill>
);

// ===========================================================================
// 06 · EL CIERRE. La idea es el contraste TODOS / NADIE.
// ---------------------------------------------------------------------------
// Las dos palabras CONSTRUYEN la pieza; el resto de la frase es tejido
// conectivo y va chico. Antes el texto quedaba arrinconado y «A NADIE.»
// se leía como una anotación suelta: ahora es el segundo bloque enorme.
//
// El contraste también es tipográfico, y ahí está la idea:
//   TODOS  → Bebas, rígida, uniforme, masa.
//   NADIE. → Balloon, humana, singular, escrita a mano.
// La tipografía dice lo mismo que el copy. NADIE. se sale por la derecha.
//
// Sin paginación: es el remate, no un paso más.
// ===========================================================================
const L6: React.FC = () => (
  <AbsoluteFill style={{background: C2.offwhite}}>
    <Foto src="assets/copywriters/caso001/06-papel-mancha.png" foco="50% 42%" />

    <div style={{position: "absolute", left: M, top: 214}}>
      <B t="ESCRIBIRLE A" px={62} color={C2.negro} ls={1} />
    </div>
    <div style={{position: "absolute", left: M - 18, top: 262}}>
      <B t="TODOS" px={326} color={C2.negro} />
    </div>

    <div style={{position: "absolute", left: M, top: 610}}>
      <B t="ES NO ESCRIBIRLE A" px={62} color={C2.negro} ls={1} />
    </div>

    {/* Balloon ES el titular acá, no un comentario. Enorme y saliéndose. */}
    <div style={{
      position: "absolute", left: M - 26, top: 660,
      transform: "rotate(-4deg)", transformOrigin: "left top",
      fontFamily: VOZ2.mano, fontWeight: 700, fontSize: 296,
      color: C2.rosa, textTransform: "uppercase", whiteSpace: "nowrap",
      lineHeight: 1,
    }}>
      NADIE.
    </div>
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------

const LAMINAS = [L1, L2, L3, L4, L5, L6];

export const Caso001: React.FC<{lamina?: number}> = ({lamina = 1}) => {
  asegurarFuentesV2();
  const L = LAMINAS[Math.min(Math.max(lamina, 1), LAMINAS.length) - 1];
  return <L />;
};
