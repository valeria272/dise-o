// ============================================================================
// COPYWRITERS · CASO 001 — «2X EL RETORNO» · carrusel de 6 láminas
// ----------------------------------------------------------------------------
// DIRECCIÓN DE ARTE — calcada de la referencia de Valeria del 30-09-2026.
//
// Lo que esa referencia corrige del intento anterior, y que ES el sistema:
//
//  1. LA TIPOGRAFÍA NO ES CONDENSADA. Es ancha y pesada — Bebas Neue Pro
//     SemiExpanded / Expanded ExtraBold. Un KPI en el ancho normal se lee
//     flaco y pierde la presencia publicitaria.
//  2. EL SUBRAYADO ES UN TRAZO GRUESO CON PUNTA, no una línea fina. Va como
//     área: ancho en el vientre, afilado donde entra y donde sale.
//  3. EL TEXTO CLARO SOBRE FOTO LLEVA SOMBRA CORTA. Sin ella flota.
//  4. EL TEXTO FUNCIONAL VA EN CAJA MIXTA («vs. 9,8X»), no en versales. Las
//     versales lo vuelven metadata; en caja mixta es una nota al pie.
//  5. LOS MOCKUPS LLEVAN CROMO REAL — encabezado de anuncio, barra de estado
//     del teléfono, remitente. Sin eso son rectángulos, no piezas.
//  6. LA FOTOGRAFÍA ES CÁLIDA Y RÚSTICA: madera, ladrillo, luz de tungsteno.
//
// ⚠️ LAS CIFRAS NO ESTÁN VERIFICADAS y la marca del caso (Santa Gota) es un
//    cliente real: no se publica sin confirmar los números contra la cuenta y
//    sin autorización del cliente. Rige R-10.
//
// Formato 1080×1350. Fotografía: Seedream 5 Pro.
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {C2, VOZ2, SOMBRA_SOBRE_FOTO, asegurarFuentesV2, granoSVG} from "../../brand/copylab/sistemaV2";
import {Flecha, Foto, Linea, Trazo} from "../../brand/copylab/piezasV2";
import {AnuncioIG, MailIOS} from "../../brand/copylab/mockups";

const M = 76;

/** Balloon. Gesto: una vez por lámina, y con cuerpo. */
const Bal: React.FC<{
  x: number; y: number; px: number; color?: string; giro?: number;
  li?: number; sombra?: boolean; children: React.ReactNode;
}> = ({x, y, px, color = C2.rosa, giro = -2, li = 1.04, sombra = false, children}) => (
  <div style={{
    position: "absolute", left: x, top: y,
    fontFamily: VOZ2.mano, fontWeight: 800, fontSize: px, color,
    lineHeight: li, transform: `rotate(${giro}deg)`, textTransform: "uppercase",
    textShadow: sombra ? SOMBRA_SOBRE_FOTO : undefined,
  }}>{children}</div>
);

/** Nota al pie. Caja MIXTA — en versales se vuelve metadata. */
const Nota: React.FC<{
  x: number; y: number; px?: number; color?: string; li?: number;
  children: React.ReactNode;
}> = ({x, y, px = 26, color = "rgba(245,243,238,0.88)", li = 1.4, children}) => (
  <div style={{
    position: "absolute", left: x, top: y, fontFamily: VOZ2.cuerpo,
    fontWeight: 400, fontSize: px, color, lineHeight: li, letterSpacing: 0.2,
  }}>{children}</div>
);

/** Rótulo de unidad bajo un KPI. */
const Unidad: React.FC<{x: number; y: number; px?: number; children: React.ReactNode}> =
({x, y, px = 40, children}) => (
  <div style={{position: "absolute", left: x, top: y}}>
    <Linea cuerpo={px} tracking={2.4} sombra>{children}</Linea>
  </div>
);

const Grano: React.FC = () => (
  <AbsoluteFill style={{backgroundImage: granoSVG(0.05, 5), backgroundSize: "300px 300px"}} />
);

// ====================== 01 · LA FOTO MANDA ======================
const L1: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Foto src="assets/copywriters/caso001/s1-vino-calido.png" foco="64% 44%" />
    <AbsoluteFill style={{
      background: "linear-gradient(98deg, rgba(11,11,11,0.95) 0%, rgba(11,11,11,0.7) 32%, rgba(11,11,11,0) 60%)",
    }} />
    <div style={{position: "absolute", left: M - 8, top: 148}}>
      <Linea cuerpo={318} voz="bloque" sombra>2X</Linea>
    </div>
    <div style={{position: "absolute", left: M, top: 470}}>
      <Linea cuerpo={104} sombra>EL RETORNO.</Linea>
    </div>
    <Bal x={M + 2} y={596} px={66} sombra>MISMA PAUTA.<br />OTRO COPY.</Bal>
    <Trazo x={M + 6} y={742} ancho={330} grosor={17} giro={-2} />
  </AbsoluteFill>
);

// ====================== 02 · LA PRUEBA ======================
const L2: React.FC = () => (
  <AbsoluteFill style={{background: C2.carbon}}>
    <Foto src="assets/copywriters/caso001/s2-madera.png" foco="50% 50%" oscurecer={0.18} />

    <AnuncioIG
      x={30} y={280} w={438} giro={-3} atenuado
      marca="Santa Gota" iniciales="SG"
      imagen={<Foto src="assets/copywriters/caso001/01-vino-servido.png" foco="58% 26%" />}
      copy="Vinos para cada momento." boton="Comprar"
    />
    <AnuncioIG
      x={492} y={322} w={520} giro={2.6}
      marca="Santa Gota" iniciales="SG"
      imagen={<Foto src="assets/copywriters/caso001/s1-vino-calido.png" foco="58% 46%" />}
      copy="Para esas conversaciones que se alargan." boton="Descubrir"
    />

    <Bal x={96} y={120} px={50} color={C2.offwhite} giro={-4} sombra>A.<br />GENÉRICO</Bal>
    <Flecha x={244} y={190} ancho={104} alto={82} giro={58} color={C2.offwhite} grosor={6} />

    <Bal x={646} y={140} px={50} color={C2.offwhite} giro={3} sombra>B.<br />POR DOLOR</Bal>
    <Flecha x={614} y={214} ancho={98} alto={78} giro={122} color={C2.offwhite} grosor={6} />

    <Bal x={128} y={1072} px={70} li={1.02} giro={-4} sombra>
      ¿QUÉ CAMBIÓ?<br />LAS PALABRAS.
    </Bal>
    <Trazo x={132} y={1242} ancho={472} grosor={18} giro={-3} />
  </AbsoluteFill>
);

// ====================== 03 · EL DATO ES EL DISEÑO ======================
const L3: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <div style={{position: "absolute", inset: 0, height: 470, overflow: "hidden"}}>
      <Foto src="assets/copywriters/caso001/s1-vino-calido.png" foco="52% 22%" />
      <AbsoluteFill style={{
        background: "linear-gradient(180deg, rgba(11,11,11,0.26) 0%, rgba(11,11,11,0.86) 62%, rgba(11,11,11,1) 100%)",
      }} />
    </div>
    <Grano />

    <div style={{position: "absolute", left: M - 30, top: 268}}>
      <Linea cuerpo={276} voz="bloque" sombra>19,2X</Linea>
    </div>
    <Unidad x={M - 22} y={516} px={46}>ROAS</Unidad>

    <Bal x={M - 16} y={604} px={54} li={1.06} giro={-4}>
      Y NO SUBIMOS<br />LA PAUTA.
    </Bal>
    <Trazo x={M - 12} y={722} ancho={296} grosor={13} giro={-2} />

    <Nota x={M - 16} y={802} px={30} li={1.5}>vs. 9,8X<br />1,09% → 2,35%</Nota>

    <div style={{
      position: "absolute", left: 436, top: 872,
      transform: "rotate(-3deg)", transformOrigin: "left top",
    }}>
      <Linea cuerpo={206} voz="bloque" color={C2.rosa} sombra>+116%</Linea>
    </div>
    <Unidad x={868} y={1076} px={42}>CTR</Unidad>
  </AbsoluteFill>
);

// ====================== 04 · LA PANTALLA ES LA PRUEBA ======================
const L4: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Foto src="assets/copywriters/caso001/04-telefono.png" foco="50% 50%" />
    <AbsoluteFill style={{
      background: "linear-gradient(104deg, rgba(11,11,11,0.96) 0%, rgba(11,11,11,0.78) 26%, rgba(11,11,11,0.06) 54%)",
    }} />

    {/* Rectángulo de la pantalla MEDIDO sobre la foto: máscara de brillo y
        componente conexa mayor → 362,347 · 372×751 en el lienzo. */}
    <MailIOS
      x={362} y={347} w={372} h={751} giro={-0.5} inclinacion={10}
      hora="11:24" remitente="Santa Gota" iniciales="SG" fecha="ayer, 18.03"
      asunto="Vinos que hacen que la noche se alargue."
      bajada="Menos apuro. Más de lo bueno."
      logo="Santa Gota"
      imagen={<Foto src="assets/copywriters/caso001/s1-vino-calido.png" foco="56% 50%" />}
      copy="Para esas conversaciones que se alargan."
      boton="Descubrir la selección"
      cuerpo="Hay botellas que no se abren. Se comparten. Descubre nuestra selección de vinos pensada para esas conversaciones que se alargan."
    />

    {/* El bloque termina ANTES de que empiece el teléfono: antes «LO MISMO.»
        y «VENDIMOS MÁS.» se montaban sobre el canto del aparato. */}
    <div style={{position: "absolute", left: M, top: 118}}>
      <Linea cuerpo={74} sombra>Y EN EMAIL</Linea>
      <Linea cuerpo={74} sombra>PASÓ</Linea>
      <Linea cuerpo={74} color={C2.rosa} sombra>LO MISMO.</Linea>
    </div>
    <Trazo x={M + 2} y={316} ancho={248} grosor={13} giro={-2} />

    <Bal x={M} y={438} px={44} li={1.1} sombra>
      MANDAMOS<br />MENOS.<br />VENDIMOS MÁS.
    </Bal>
  </AbsoluteFill>
);

// ====================== 05 · EL SEGUNDO DATO ======================
const L5: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Foto src="assets/copywriters/caso001/05-corcho.png" foco="66% 46%" zoom={1.1} />
    <AbsoluteFill style={{
      background: "linear-gradient(94deg, rgba(11,11,11,0.97) 0%, rgba(11,11,11,0.84) 38%, rgba(11,11,11,0.05) 74%)",
    }} />

    <div style={{position: "absolute", left: M - 22, top: 196}}>
      <Linea cuerpo={196} voz="bloque" sombra>47–52%</Linea>
    </div>
    <Unidad x={M - 14} y={378} px={48}>APERTURA</Unidad>

    <div style={{position: "absolute", left: M - 22, top: 462}}>
      <Linea cuerpo={196} voz="bloque" sombra>4–11</Linea>
    </div>
    <Unidad x={M - 14} y={644} px={48}>ÓRDENES</Unidad>

    <Bal x={M - 10} y={764} px={60} li={1.04} giro={-3} sombra>
      SEGMENTAR<br />&gt; SATURAR.
    </Bal>
    <Trazo x={M - 6} y={912} ancho={344} grosor={16} giro={-2} />

    <Nota x={M - 10} y={1004} px={25} li={1.5} color="rgba(245,243,238,0.74)">
      vs. 10–28% apertura /<br />0–1 órdenes enviando a toda la base.
    </Nota>
  </AbsoluteFill>
);

// ====================== 06 · EL CIERRE ======================
const L6: React.FC = () => (
  <AbsoluteFill style={{background: C2.offwhite}}>
    <Foto src="assets/copywriters/caso001/s6-servilleta.png" foco="26% 26%" zoom={1.3} />

    <div style={{position: "absolute", left: M, top: 208}}>
      <Linea cuerpo={70} color={C2.negro} tracking={0.5}>ESCRIBIRLE A</Linea>
    </div>
    <div style={{position: "absolute", left: M - 12, top: 264}}>
      <Linea cuerpo={248} voz="bloque" color={C2.negro}>TODOS</Linea>
    </div>
    <div style={{position: "absolute", left: M, top: 548}}>
      <Linea cuerpo={70} color={C2.negro} tracking={0.5}>ES NO ESCRIBIRLE A</Linea>
    </div>
    <Bal x={M - 18} y={604} px={252} giro={-3} li={1}>NADIE.</Bal>
    <Trazo x={M - 4} y={836} ancho={636} grosor={26} giro={-2} />
  </AbsoluteFill>
);

const LAMINAS = [L1, L2, L3, L4, L5, L6];

export const Caso001: React.FC<{lamina?: number}> = ({lamina = 1}) => {
  asegurarFuentesV2();
  const L = LAMINAS[Math.min(Math.max(lamina, 1), LAMINAS.length) - 1];
  return <L />;
};
