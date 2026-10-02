import React from "react";
import {AbsoluteFill, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from "remotion";
import {Audio} from "@remotion/media";
import {
  AUDIO,
  SANS,
  SANS_MIN,
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
  SLOT,
  CLIP_LEN,
} from "./OctubreVideo";

// =============================================================================
// TIERRA CALMA · NOVIEMBRE 2026 · REEL DEL 04/11 — «Del terreno a tu casa»
//
// Brief (grilla de Carlos, verbatim en clients/tierra-calma/grilla-noviembre-2026.md):
// «Reel IA + dron al estilo de la referencia: el terreno vacío se transforma en
// casa con render IA, mientras aparecen en pantalla los datos técnicos del
// terreno. Transiciones de luz, locución tranquila.» Cuatro cortes:
//
//   1 · aérea del terreno cercado, luz de mañana
//   2 · líneas de luz marcan los deslindes
//   3 · la casa se levanta sobre el terreno
//   4 · vuelve la aérea del terreno completo, atardecer
//
// ⭐ CÓMO ESTÁ HECHO — una sola aérea REAL, tres fotogramas encadenados.
// La base es la DJI_0300 del rodaje del 07-08 (no se usa en ninguna otra pieza del
// mes). Seedream 5 Pro hizo sobre ella tres fotogramas con el MISMO encuadre
// —terreno cercado (`r1`), con la casa (`r2`), al atardecer (`r3`)— y Kling 3.0
// va de uno a otro con fotograma inicial Y final. Por eso los cortes calzan sin
// salto: cada plano termina exactamente donde empieza el siguiente.
//   scripts/tc-nov-imagenes.py (r1 · r2 · r3) · raw/tierracalma/nov2026/reel-d/
//
// «El foco es el terreno, no la casa: la casa sólo muestra el potencial» (NOTA del
// brief). Una sola casa, chica contra la parcela, y ningún plazo de construcción.
//
// ⚠️ EL TEXTO VA ARRIBA, NO AL CENTRO. En los reels de octubre el bloque iba al
// medio; acá el medio del cuadro ES el terreno —la parcela ocupa las filas
// 730–1205— y tapar el sujeto con el titular es justo lo que la cuenta prohíbe
// (R-14). Se acota la banda, no se mueve la imagen.
//
// ⚠️ LOS CORTES NO DURAN 140 FRAMES COMO EN OCTUBRE. La voz de la marca es lenta
// (R-32) y las cuatro líneas MIDEN 143, 161, 144 y 84 frames: ninguna de las tres
// primeras cabe en la ranura de octubre. En vez de acelerar la voz —que dejaría de
// ser la de la marca— los clips corren al 86 % y el corte 2, que es un cuadro
// fijo, dura lo que su línea necesita.
//
// ⚠️ DATOS FUERA DE LA LISTA BLANCA del manual: «ROL individual», «Entrega
// cercada» y «Construye hasta un 10 % de la superficie». Vienen de la Ficha
// Técnica que cita la grilla; falta el OK escrito de Fran o Blanca (R-03).
// =============================================================================

const CLIP = (n: string) => staticFile(`assets/tierracalma/nov/clips/${n}.mp4`);
const SERIF_PIE = SANS;

/** Los clips de Kling duran 151 frames; al 86 % rinden 175. */
const RITMO = 0.86;
const FUNDE = 11;

// Entrada de cada corte. Solapan 11 frames para la disolvencia.
const C1 = 0;
const C2 = 160;
const C3 = 340;
const C4 = 500;
const CIERRE_DESDE = 655;
const CIERRE = 150;
export const NOV_REEL_D_DURATION = CIERRE_DESDE + CIERRE; // 805 = 26,8 s

/**
 * La locución: VOZ DE TIERRA CALMA (Gemini 2.5 Pro · Enceladus), una línea por
 * corte. ⚠️ Duraciones MEDIDAS sobre los mp3 ya recortados de silencio, no
 * estimadas: 4,78 · 5,35 · 4,80 · 2,78 s.
 *
 * Lo que dice cada línea es el texto de pantalla de su corte, leído:
 *   vn1  Parcelas en Padre Hurtado, de cerca de cinco mil metros cuadrados.
 *   vn2  Rol individual, entrega cercada y electricidad subterránea.
 *   vn3  Construye hasta un diez por ciento de la superficie, y hasta dos casas.
 *   vn4  Tu terreno, desde dos mil quinientas UF.
 */
const VOZ: {a: string; desde: number; dura: number}[] = [
  {a: "vn1", desde: 12, dura: 144},
  {a: "vn2", desde: 176, dura: 161},
  {a: "vn3", desde: 352, dura: 144},
  {a: "vn4", desde: 514, dura: 84},
];

const clamp = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

const PlanoLento: React.FC<{src: string; primero?: boolean}> = ({src, primero = false}) => {
  const frame = useCurrentFrame();
  const opacity = primero ? 1 : interpolate(frame, [0, FUNDE], [0, 1], clamp);
  return (
    <AbsoluteFill style={{opacity}}>
      <OffthreadVideo
        src={src}
        muted
        playbackRate={RITMO}
        style={{width: "100%", height: "100%", objectFit: "cover"}}
      />
    </AbsoluteFill>
  );
};

/**
 * ⭐ CORTE 2 · las líneas de luz sobre el deslinde.
 *
 * El plano es `r1` QUIETO —el mismo cuadro en que termina el corte 1 y en que
 * empieza el 3— y la luz recorre el cerco. Los cuatro vértices están MEDIDOS
 * sobre `r-terreno.jpg` (1080×1920), al pie de los postes:
 *
 *   poniente (178, 862) · norte (732, 735) · oriente (1066, 975) · sur (500, 1205)
 *
 * ⛔ No hay cotas en metros: el manual prohíbe publicar m² exactos (§ 2), y un
 * «100 m» dibujado sobre una parcela ilustrativa sería exactamente eso. La única
 * medida que aparece es la aprobada, «~5.000 m²».
 *
 * ⚠️ Si se regenera `r1`, estos cuatro puntos hay que volver a medirlos.
 */
const CERCO: [number, number][] = [
  [178, 862],
  [732, 735],
  [1066, 975],
  [500, 1205],
];
const PERIMETRO = CERCO.reduce((s, p, i) => {
  const q = CERCO[(i + 1) % CERCO.length];
  return s + Math.hypot(q[0] - p[0], q[1] - p[1]);
}, 0);
const TRAZO = `M ${CERCO.map((p) => p.join(" ")).join(" L ")} Z`;
const LUZ = "#F3EEE3";

const Deslindes: React.FC = () => {
  const f = useCurrentFrame();
  const entra = interpolate(f, [0, FUNDE], [0, 1], clamp);
  const avance = interpolate(f, [16, 86], [PERIMETRO, 0], clamp);
  const sale = interpolate(f, [168, 188], [1, 0], clamp);
  const pulso = 0.78 + 0.22 * Math.sin(f / 9);
  const rotulo = interpolate(f, [74, 96], [0, 1], clamp) * sale;
  return (
    <AbsoluteFill style={{opacity: entra}}>
      <Img src={staticFile("assets/tierracalma/nov/r-terreno.jpg")} style={{width: "100%", height: "100%"}} />
      <svg width={1080} height={1920} viewBox="0 0 1080 1920" style={{position: "absolute", inset: 0, opacity: sale}}>
        <defs>
          <filter id="resplandor" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="9" />
          </filter>
        </defs>
        {/* el campo, apenas encendido */}
        <path d={TRAZO} fill={LUZ} opacity={interpolate(f, [70, 100], [0, 0.1], clamp)} />
        {/* el resplandor y la línea */}
        <path
          d={TRAZO}
          fill="none"
          stroke={LUZ}
          strokeWidth={14}
          strokeLinejoin="round"
          strokeDasharray={PERIMETRO}
          strokeDashoffset={avance}
          opacity={0.55 * pulso}
          filter="url(#resplandor)"
        />
        <path
          d={TRAZO}
          fill="none"
          stroke={LUZ}
          strokeWidth={3.2}
          strokeLinejoin="round"
          strokeDasharray={PERIMETRO}
          strokeDashoffset={avance}
        />
        {CERCO.map(([x, y], i) => {
          const op = interpolate(f, [16 + i * 17, 26 + i * 17], [0, 1], clamp);
          return (
            <g key={i} opacity={op}>
              <circle cx={x} cy={y} r={15} fill="none" stroke={LUZ} strokeWidth={1.5} opacity={0.6} />
              <circle cx={x} cy={y} r={6} fill={LUZ} />
            </g>
          );
        })}
      </svg>
      <div
        style={{
          position: "absolute",
          left: 609,
          top: 968,
          transform: "translate(-50%, -50%)",
          opacity: rotulo,
          fontFamily: SERIF_PIE,
          fontWeight: 500,
          fontSize: 34,
          letterSpacing: "0.16em",
          color: "#fff",
          textShadow: HALO,
          whiteSpace: "nowrap",
        }}
      >
        ~5.000 M²
      </div>
    </AbsoluteFill>
  );
};

const Dato: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      display: "flex",
      alignItems: "center",
      gap: 16,
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: SANS_MIN,
      color: "#fff",
      textShadow: HALO,
      marginBottom: 14,
      whiteSpace: "nowrap",
    }}
  >
    <svg width={28} height={28} viewBox="0 0 24 24" fill="none" style={{flexShrink: 0}}>
      <circle cx="12" cy="12" r="9.2" stroke="#fff" strokeWidth="1.5" />
      <path d="M8 12.3l2.7 2.7L16 9.6" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
    {children}
  </div>
);

export const NovReelTerreno: React.FC = () => (
  <Lienzo>
    <Sequence from={C1} durationInFrames={C2 - C1 + FUNDE}>
      <PlanoLento src={CLIP("d1")} primero />
    </Sequence>
    <Sequence from={C2} durationInFrames={C3 - C2 + FUNDE}>
      <Deslindes />
    </Sequence>
    <Sequence from={C3} durationInFrames={C4 - C3 + FUNDE}>
      <PlanoLento src={CLIP("d3")} />
    </Sequence>
    <Sequence from={C4} durationInFrames={CIERRE_DESDE - C4 + 15}>
      <PlanoLento src={CLIP("d4")} />
    </Sequence>
    <Velo arriba={0.62} abajo={0.5} />

    {/* CORTE 1 · «Parcelas en Padre Hurtado · ~5.000 m²» */}
    <Bloque desde={8} dura={150} pos="arriba">
      <Suave>Parcelas en Padre Hurtado</Suave>
      <Aire h={14} />
      <Enfasis>~5.000 m²</Enfasis>
    </Bloque>

    {/* CORTE 2 · «ROL individual · Entrega cercada · Electricidad subterránea» */}
    <Bloque desde={172} dura={166} pos="arriba">
      <div style={{display: "flex", flexDirection: "column", alignItems: "flex-start"}}>
        <Dato>ROL individual</Dato>
        <Dato>Entrega cercada</Dato>
        <Dato>Electricidad subterránea</Dato>
      </div>
    </Bloque>

    {/* CORTE 3 · «Construye hasta un 10% de la superficie · Hasta 2 casas» */}
    <Bloque desde={348} dura={150} pos="arriba">
      <Suave>{"Construye hasta un 10%\nde la superficie"}</Suave>
      <Aire h={16} />
      <Enfasis>Hasta 2 casas</Enfasis>
    </Bloque>

    {/* CORTE 4 · «Tu terreno, desde UF 2.500» + CTA */}
    <Bloque desde={508} dura={160} pos="arriba" sinSalida>
      <Suave>Tu terreno,</Suave>
      <Aire h={10} />
      <Enfasis>desde UF 2.500</Enfasis>
    </Bloque>
    <Bloque desde={566} dura={102} pos="abajo" sinSalida>
      <Suave size={46}>{"Elige tu terreno: pide el plano\ncon las parcelas disponibles."}</Suave>
      <Aire h={26} />
      <Pie>Tierra Calma · Padre Hurtado</Pie>
    </Bloque>

    {VOZ.map((v) => (
      <Sequence key={v.a} from={v.desde} durationInFrames={v.dura + 10}>
        <Audio src={AUDIO(v.a)} volume={1} />
      </Sequence>
    ))}
    <Musica
      src={AUDIO("mus_corporativa_c")}
      vol={0.26}
      duracion={NOV_REEL_D_DURATION}
      baja={VOZ.map((v) => [v.desde, v.desde + v.dura] as [number, number])}
      volBajo={0.09}
    />

    {/* R-30: todo reel cierra con el logo animado oficial. */}
    <Sequence from={CIERRE_DESDE} durationInFrames={CIERRE}>
      <Plano src={staticFile("assets/tierracalma/tc_cierre.mp4")} indice={1} />
    </Sequence>
  </Lienzo>
);

// =============================================================================
// REEL DEL 19/11 — «¿Y si este fuera tu día a día?» · Pilar 2
//
// Brief: «Reel IA de rutina diaria con LUGARES REALES del sector. POV y escenas
// de objetos, sin personas en primer plano.» Seis cortes:
//
//   1 · mañana en la parcela, café en la terraza
//   2 · salida por el camino de acceso
//   3 · llegada al supermercado
//   4 · colegios y centro de salud
//   5 · tarde recreativa
//   6 · aérea de la parcela al atardecer (REAL: DJI_0293, cambio mínimo)
//
// ⭐ EL CORTE 4 NO ES UN MAPA: SON TRES FOTOS REALES. El brief pedía «mapa
// ilustrado»; esta cuenta ya rechazó el mapa dibujado y ninguna cartografía real
// muestra esos lugares. Diego, 01-10: *«para los colegios y cesfam del reels del
// 19 usa estas imágenes, mejora la calidad de las imágenes»*. Son tres capturas de
// calle; se pasaron por Seedream 5 Pro con CAMBIO MÍNIMO (R-24): mismo edificio,
// más nitidez, cielo limpio, y fuera lo que no es del lugar — cables, autos y, en
// el CESFAM, las personas que salían de frente (R-26).
//   scripts/tc-nov-imagenes.py (x1 · x2 · x3) · originales en
//   raw/tierracalma/nov2026/reel-i/adjuntas/
//
// ⚠️ QUÉ FOTO ES QUÉ LUGAR — SUPUESTO, NO DATO. Las fotos llegaron sin nombre. Se
// rotularon en el orden en que el brief nombra los lugares y en el que llegaron:
// 1.ª «Colegio Brasilia» · 2.ª «Colegio Francisco de Aguirre» · 3.ª «CESFAM Juan
// Pablo II» (la tercera sí se reconoce: es un centro de salud). Si las dos
// primeras van al revés, se intercambian dos cadenas en `LUGARES`.
//
// ⚠️ Sigue pendiente lo que la propia grilla pide: confirmar con Blanca que esos
// colegios sean los más cercanos. La hoja de fuentes nombra «Peumayen College»
// donde el brief dice «Colegio Brasilia».
//
// Los supermercados y BSC Sports NO se muestran: no hay foto real de ellos y una
// fachada de Tottus hecha con IA sería inventar un lugar real. Van como escenas
// de objetos —la compra en el maletero, la pala y la pelota en la cancha— y el
// nombre lo pone el texto, que es lo que el brief llama «gráfica con nombres».
//
// Sin locución (el brief no la pide, igual que el reel de dron de octubre, E-06).
// Solo tiempos aprobados: peaje 15 min, Cuesta Barriga 10 min.
// =============================================================================

const SOLAPE = 15;
export const NOV_REEL_I_DURATION = SLOT * 5 + CLIP_LEN - SOLAPE + CIERRE; // 986 = 32,9 s

const LUGARES: {foto: string; nombre: string}[] = [
  {foto: "i-colegio-1", nombre: "Colegio Brasilia"},
  {foto: "i-colegio-2", nombre: "Colegio Francisco de Aguirre"},
  {foto: "i-cesfam", nombre: "CESFAM Juan Pablo II"},
];

/** El corte 4: las tres fotos reales en tarjeta, cada una con su nombre. Entran
 *  de a una, de arriba abajo, y quedan dentro de la zona segura (270–1650). */
const TARJ = {w: 888, h: 350, gap: 40, rotulo: 46};
const Lugares: React.FC = () => {
  const f = useCurrentFrame();
  const entra = interpolate(f, [0, FUNDE], [0, 1], clamp);
  const alto = LUGARES.length * (TARJ.h + TARJ.rotulo) + (LUGARES.length - 1) * TARJ.gap;
  const y0 = 270 + (1380 - alto) / 2;
  return (
    <AbsoluteFill style={{opacity: entra, backgroundColor: "#003326"}}>
      {LUGARES.map((l, i) => {
        const t = f - (8 + i * 16);
        const op = interpolate(t, [0, 16], [0, 1], clamp);
        const dy = interpolate(t, [0, 22], [26, 0], clamp);
        const zoom = interpolate(f, [0, CLIP_LEN], [1.07, 1.0], clamp);
        return (
          <div
            key={l.foto}
            style={{
              position: "absolute",
              left: (1080 - TARJ.w) / 2,
              top: y0 + i * (TARJ.h + TARJ.rotulo + TARJ.gap),
              width: TARJ.w,
              opacity: op,
              transform: `translateY(${dy}px)`,
            }}
          >
            <div
              style={{
                fontFamily: SANS,
                fontWeight: 500,
                fontSize: 27,
                letterSpacing: "0.2em",
                textTransform: "uppercase",
                color: "#F3EEE3",
                height: TARJ.rotulo,
                whiteSpace: "nowrap",
              }}
            >
              {l.nombre}
            </div>
            <div
              style={{
                width: TARJ.w,
                height: TARJ.h,
                borderRadius: 26,
                overflow: "hidden",
                boxShadow: "0 22px 46px rgba(0,0,0,0.38), inset 0 0 0 1px rgba(243,238,227,0.3)",
              }}
            >
              <Img
                src={staticFile(`assets/tierracalma/nov/${l.foto}.jpg`)}
                style={{width: "100%", height: "100%", objectFit: "cover", transform: `scale(${zoom})`}}
              />
            </div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

/**
 * ⭐ CORTE 3 · los supermercados van con su LOGO, en blanco (Constanza Lizana,
 * 02-10: *«añadiría los logos de Tottus, Santa Isabel y Líder Express. Quizás en
 * variante blanca, pero así será más llamativo»*). Reemplazan al nombre escrito en
 * IvyOra: el logo ya lo dice. Son los SVG oficiales pasados a una tinta por
 * `scripts/tc-nov-logos.py` — no se dibujan ni se generan. `alto` en px del lienzo;
 * el de Tottus es menor porque es un logotipo apaisado y los otros dos son sellos.
 */
const LogoSuper: React.FC<{id: string; alto: number}> = ({id, alto}) => (
  <Img
    src={staticFile(`assets/tierracalma/nov/logos/${id}.png`)}
    style={{height: alto, width: "auto", filter: "drop-shadow(0 2px 14px rgba(0,0,0,0.45))"}}
  />
);

export const NovReelDia: React.FC = () => {
  const frame = useCurrentFrame();
  const pulso = 1 + Math.sin((frame - 715) / 7) * 0.05;
  return (
    <Lienzo>
      {["i1", "i2", "i3"].map((n, i) => (
        <Sequence key={n} from={SLOT * i} durationInFrames={CLIP_LEN}>
          <Plano src={CLIP(n)} indice={i} />
        </Sequence>
      ))}
      <Sequence from={SLOT * 3} durationInFrames={CLIP_LEN}>
        <Lugares />
      </Sequence>
      <Sequence from={SLOT * 4} durationInFrames={CLIP_LEN}>
        <Plano src={CLIP("i5")} indice={4} />
      </Sequence>
      <Sequence from={SLOT * 5} durationInFrames={CLIP_LEN}>
        <Plano src={CLIP("i6")} indice={5} />
      </Sequence>
      <Velo arriba={0.5} abajo={0.5} />

      {/* CORTE 1 · «¿Y si este fuera tu día a día?» — en el cielo de la mañana */}
      <Bloque desde={14} dura={118} pos="arriba">
        <Aire h={150} />
        <Enfasis>{"¿Y si este fuera\ntu día a día?"}</Enfasis>
      </Bloque>

      {/* CORTE 2 · «A 15 min del Peaje Padre Hurtado» */}
      <Bloque desde={154} dura={118} pos="arriba">
        <Aire h={110} />
        <Enfasis>{"A 15 min del Peaje\nPadre Hurtado"}</Enfasis>
      </Bloque>

      {/* CORTE 3 · «Tottus y Santa Isabel en Camino a Melipilla · Líder Express en
          San Ignacio» — arriba: el centro del cuadro son las bolsas. */}
      <Bloque desde={294} dura={118} pos="arriba">
        <div style={{display: "flex", alignItems: "center", gap: 46}}>
          <LogoSuper id="tottus" alto={56} />
          <LogoSuper id="santa-isabel" alto={128} />
        </div>
        <Aire h={10} />
        <Suave size={50}>en Camino a Melipilla</Suave>
        <Aire h={30} />
        <LogoSuper id="lider-express" alto={128} />
        <Aire h={10} />
        <Suave size={50}>en San Ignacio</Suave>
      </Bloque>

      {/* CORTE 4 · los nombres van en las tarjetas (`Lugares`) */}

      {/* CORTE 5 · «Fútbol y pádel en BSC Sports · Mirador Cuesta Barriga a 10 min» */}
      <Bloque desde={574} dura={118} pos="arriba">
        <Enfasis>Fútbol y pádel</Enfasis>
        <Aire h={6} />
        <Suave size={50}>en BSC Sports</Suave>
        <Aire h={34} />
        <Enfasis>{"Mirador\nCuesta Barriga"}</Enfasis>
        <Aire h={6} />
        <Suave size={50}>a 10 min</Suave>
      </Bloque>

      {/* CORTE 6 · «~5.000 m² con ROL individual, desde UF 2.500» + CTA */}
      <Bloque desde={714} dura={125} pos="centro" sinSalida>
        <Enfasis>~5.000 m²</Enfasis>
        <Aire h={10} />
        <Suave size={54}>con ROL individual,</Suave>
        <Aire h={10} />
        <Enfasis>desde UF 2.500</Enfasis>
        <Aire h={64} />
        <Suave size={50}>Conoce tu próximo hogar:</Suave>
        <Aire h={26} />
        <div style={{transform: `scale(${pulso})`}}>
          <IconoWsp s={50} />
        </div>
        <Aire h={18} />
        <Pie>Escríbenos por WhatsApp</Pie>
      </Bloque>

      <Musica src={AUDIO("mus_corporativa_d")} vol={0.3} duracion={NOV_REEL_I_DURATION} />
      <Sequence from={SLOT * 5 + CLIP_LEN - SOLAPE} durationInFrames={CIERRE + SOLAPE}>
        <Plano src={staticFile("assets/tierracalma/tc_cierre.mp4")} indice={1} />
      </Sequence>
    </Lienzo>
  );
};
