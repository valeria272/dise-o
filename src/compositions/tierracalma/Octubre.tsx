import React from "react";
import {AbsoluteFill, Img, Sequence, staticFile, useCurrentFrame} from "remotion";
import {tierracalma as TC, ensureTierraCalmaFonts} from "../../brand/tierracalma";

// =============================================================================
// TIERRA CALMA · PIEZAS ESTÁTICAS · OCTUBRE 2026
//
// ⛔ EL MARCO ES UN ASSET BLOQUEADO DEL DISEÑADOR — NO SE REDIBUJA.
// Vive en public/assets/tierracalma/marcos/ y sale de MARCOS.ai. Trae dentro
// el logo (gaviota + wordmark + PADRE HURTADO) y el contorno de la píldora.
// Acá sólo se rellena: foto debajo, texto dentro de las zonas medidas.
//
// El carrusel es UN SOLO OBJETO: el filete se corre entre slides (1 cierra a la
// izquierda, 2 y 3 son bandas sin verticales, 4 cierra a la derecha). Por eso
// cada slide tiene su propio PNG y no se pueden intercambiar.
//
// GEOMETRÍA MEDIDA sobre los PNG (no estimada — ver clients/tierra-calma/CLAUDE.md):
//
//            filete x      regla sup   regla inf   píldora
//   post     65 → 1016     y 130       y 1236      x 264-803 · y 1212-1264
//   story    64 → 1016     y 129       y 1620      x 237-843 · y 1584-1657
//   carrusel según slide   y 130       y 1284      — no lleva —
//
// Un frame = una pieza. Se rinden de una pasada con `--sequence`.
//
// El copy sale VERBATIM de la grilla de octubre (Drive, Carlos Figueroa) y los
// datos de la lista blanca ampliada por el brief de octubre: se suman
// electricidad subterránea, cierre perimetral y máximo 2 casas por parcela.
// ⛔ NO se menciona conexión a agua potable (es noria del propietario).
// =============================================================================

const OCT = (n: string) => staticFile(`assets/tierracalma/oct/${n}.jpg`);
const MARCO = (n: string) => staticFile(`assets/tierracalma/marcos/${n}.png`);

const SANS = TC.fonts.body;
const SERIF = TC.fonts.display;

// --- zonas por formato, en px del lienzo -------------------------------------
const Z = {
  post: {w: 1080, h: 1350, texto: 250, pill: {x: 264, y: 1212, w: 540, h: 53}},
  story: {w: 1080, h: 1920, texto: 245, pill: {x: 237, y: 1584, w: 606, h: 73}},
  carr: {w: 1080, h: 1350, textoConLogo: 250, textoSinLogo: 205},
} as const;

// -----------------------------------------------------------------------------
// Primitivas
// -----------------------------------------------------------------------------

const Lienzo: React.FC<{w: number; h: number; children: React.ReactNode}> = ({w, h, children}) => {
  ensureTierraCalmaFonts();
  return (
    <AbsoluteFill style={{width: w, height: h, backgroundColor: TC.colors.ink, overflow: "hidden"}}>
      {children}
    </AbsoluteFill>
  );
};

const Foto: React.FC<{src: string; foco?: string; escala?: number}> = ({
  src,
  foco = "50% 50%",
  escala = 1,
}) => (
  <Img
    src={src}
    style={{
      position: "absolute",
      inset: 0,
      width: "100%",
      height: "100%",
      objectFit: "cover",
      objectPosition: foco,
      transform: `scale(${escala})`,
    }}
  />
);

/**
 * Contraste por DEGRADADO, nunca por caja opaca (regla del brief). El velo
 * parejo no es decorativo: sin él un cielo de atardecer se come el texto blanco.
 */
const Degradado: React.FC<{arriba?: number; abajo?: number; velo?: number}> = ({
  arriba = 0.62,
  abajo = 0.5,
  velo = 0.13,
}) => (
  <>
    <AbsoluteFill
      style={{
        background: `linear-gradient(to bottom, rgba(6,14,20,${arriba}) 0%, rgba(6,14,20,${
          arriba * 0.45
        }) 32%, rgba(6,14,20,0) 55%, rgba(6,14,20,${abajo * 0.5}) 82%, rgba(6,14,20,${abajo}) 100%)`,
      }}
    />
    <AbsoluteFill style={{backgroundColor: `rgba(6,14,20,${velo})`}} />
  </>
);

const Marco: React.FC<{archivo: string}> = ({archivo}) => (
  <Img
    src={MARCO(archivo)}
    style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "fill"}}
  />
);

/** Bloque de texto: arranca bajo el logo y se apila hacia abajo, centrado. */
const Cuerpo: React.FC<{top: number; ancho?: number; children: React.ReactNode}> = ({
  top,
  ancho = 790,
  children,
}) => (
  <div
    style={{
      position: "absolute",
      top,
      left: "50%",
      transform: "translateX(-50%)",
      width: ancho,
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      textAlign: "center",
    }}
  >
    {children}
  </div>
);

/** Línea sans en versales — la mitad "fría" de la pareja tipográfica. */
const Ligera: React.FC<{size?: number; children: React.ReactNode}> = ({size = 76, children}) => (
  <div
    style={{
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: size,
      lineHeight: 1.13,
      letterSpacing: "0.005em",
      color: "#fff",
      textTransform: "uppercase",
      textShadow: "0 2px 22px rgba(0,0,0,0.42)",
      whiteSpace: "pre-line",
    }}
  >
    {children}
  </div>
);

/** Remate serif cursivo — la palabra emotiva. Nunca dos serifs ni dos sans. */
const Remate: React.FC<{size?: number; children: React.ReactNode}> = ({size = 102, children}) => (
  <div
    style={{
      fontFamily: SERIF,
      fontStyle: "italic",
      fontWeight: 500,
      fontSize: size,
      lineHeight: 1.02,
      letterSpacing: "0.004em",
      color: "#fff",
      textTransform: "uppercase",
      textShadow: "0 2px 24px rgba(0,0,0,0.45)",
      whiteSpace: "pre-line",
    }}
  >
    {children}
  </div>
);

/** Bajada en caja baja — el aire que pedía el lenguaje de septiembre. */
const Bajada: React.FC<{size?: number; ancho?: number; children: React.ReactNode}> = ({
  size = 38,
  ancho,
  children,
}) => (
  <div
    style={{
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: size,
      lineHeight: 1.36,
      color: "rgba(255,255,255,0.9)",
      textShadow: "0 2px 16px rgba(0,0,0,0.5)",
      maxWidth: ancho,
      whiteSpace: "pre-line",
    }}
  >
    {children}
  </div>
);

/** Caja de color de marca — así "varía con los colores" que pidió el diseñador. */
const Caja: React.FC<{color: string; size?: number; children: React.ReactNode}> = ({
  color,
  size = 50,
  children,
}) => (
  <div
    style={{
      backgroundColor: color,
      borderRadius: 20,
      padding: "20px 38px",
      fontFamily: SANS,
      fontWeight: 500,
      fontSize: size,
      lineHeight: 1.16,
      letterSpacing: "0.008em",
      color: "#fff",
      textTransform: "uppercase",
      whiteSpace: "pre-line",
    }}
  >
    {children}
  </div>
);

const Espacio: React.FC<{h: number}> = ({h}) => <div style={{height: h, flexShrink: 0}} />;

// --- iconos de línea, dibujados (nunca emoji en pieza de marca) --------------
const IconoPin: React.FC<{s?: number}> = ({s = 26}) => (
  <svg width={s} height={s} viewBox="0 0 24 24" fill="none" style={{flexShrink: 0}}>
    <path
      d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11Z"
      stroke="#fff"
      strokeWidth="1.6"
      strokeLinejoin="round"
    />
    <circle cx="12" cy="10" r="2.6" stroke="#fff" strokeWidth="1.6" />
  </svg>
);

const IconoWsp: React.FC<{s?: number}> = ({s = 26}) => (
  <svg width={s} height={s} viewBox="0 0 24 24" fill="none" style={{flexShrink: 0}}>
    <path
      d="M3.6 20.4l1.2-4a8.2 8.2 0 1 1 3.1 3l-4.3 1Z"
      stroke="#fff"
      strokeWidth="1.6"
      strokeLinejoin="round"
    />
    <path
      d="M9 9.2c0 3 2.4 5.3 5.3 5.3.5 0 .9-.4.9-.9v-1l-1.8-.6-.8.9a4.6 4.6 0 0 1-2-2l.9-.8L11 8.3h-1c-.5 0-1 .4-1 .9Z"
      fill="#fff"
    />
  </svg>
);

const IconoRegla: React.FC<{s?: number}> = ({s = 26}) => (
  <svg width={s} height={s} viewBox="0 0 24 24" fill="none" style={{flexShrink: 0}}>
    <rect x="3" y="8" width="18" height="8" rx="1.6" stroke="#fff" strokeWidth="1.6" />
    <path d="M7 8v3M11 8v4M15 8v3M19 8v4" stroke="#fff" strokeWidth="1.6" strokeLinecap="round" />
  </svg>
);

/**
 * Texto DENTRO del contorno de píldora que ya trae el marco. No se dibuja la
 * píldora: se rellena la que existe. Por eso el texto va corto — si no cabe en
 * una línea el diseño está mal, no la píldora.
 */
const Pildora: React.FC<{
  caja: {x: number; y: number; w: number; h: number};
  icono?: React.ReactNode;
  size?: number;
  tracking?: number;
  children: React.ReactNode;
}> = ({caja, icono, size = 31, tracking = 0.07, children}) => (
  <div
    style={{
      position: "absolute",
      left: caja.x,
      top: caja.y,
      width: caja.w,
      height: caja.h,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      gap: 14,
    }}
  >
    {icono}
    <span
      style={{
        fontFamily: SANS,
        fontWeight: 500,
        fontSize: size,
        letterSpacing: `${tracking}em`,
        color: "#fff",
        textTransform: "uppercase",
        whiteSpace: "nowrap",
      }}
    >
      {children}
    </span>
  </div>
);

/** Tarjeta de vidrio — el recurso de mockup que ya usaron las stories de sept. */
const Vidrio: React.FC<{
  x: number;
  y: number;
  w: number;
  rot?: number;
  children: React.ReactNode;
}> = ({x, y, w, rot = 0, children}) => (
  <div
    style={{
      position: "absolute",
      left: x,
      top: y,
      width: w,
      transform: `rotate(${rot}deg)`,
      background: "linear-gradient(150deg, rgba(255,255,255,0.34), rgba(255,255,255,0.17))",
      border: "1.5px solid rgba(255,255,255,0.5)",
      borderRadius: 30,
      padding: "30px 34px",
      backdropFilter: "blur(22px)",
      WebkitBackdropFilter: "blur(22px)",
      boxShadow: "0 26px 60px rgba(0,0,0,0.3)",
    }}
  >
    {children}
  </div>
);

// =============================================================================
// E · 06/10 · CARRUSEL 4 SLIDES · "Todo lo que ya no tienes que resolver"
// Pilar 1 · Calidad de vida. El filete se corre entre slides: es un solo objeto.
// =============================================================================

const E1: React.FC = () => (
  <Lienzo w={Z.carr.w} h={Z.carr.h}>
    <Foto src={OCT("e-portada")} foco="50% 58%" />
    <Degradado arriba={0.66} abajo={0.34} />
    <Marco archivo="MARCO-CARRUSEL-1" />
    {/* 860 / 64 px: a 72 px la línea "comprar tu parcela?" se partía en tres. */}
    <Cuerpo top={Z.carr.textoConLogo} ancho={870}>
      <Ligera size={64}>{"¿Dudas antes de\ncomprar tu parcela?"}</Ligera>
      <Espacio h={22} />
      <Remate size={94}>{"Aquí las\nresolvemos."}</Remate>
    </Cuerpo>
  </Lienzo>
);

const E2: React.FC = () => (
  <Lienzo w={Z.carr.w} h={Z.carr.h}>
    <Foto src={OCT("e-luz")} foco="50% 52%" />
    <Degradado arriba={0.6} abajo={0.34} />
    <Marco archivo="MARCO-CARRUSEL-2" />
    <Cuerpo top={Z.carr.textoSinLogo} ancho={820}>
      <Ligera size={76}>{"¿Y la luz?"}</Ligera>
      <Espacio h={26} />
      <Caja color={TC.colors.olive} size={50}>
        {"Electricidad subterránea\nya instalada."}
      </Caja>
    </Cuerpo>
  </Lienzo>
);

const E3: React.FC = () => (
  <Lienzo w={Z.carr.w} h={Z.carr.h}>
    <Foto src={OCT("e-cierre")} foco="50% 50%" />
    <Degradado arriba={0.6} abajo={0.34} />
    <Marco archivo="MARCO-CARRUSEL-3" />
    <Cuerpo top={Z.carr.textoSinLogo} ancho={820}>
      <Ligera size={76}>{"¿Y el cierre?"}</Ligera>
      <Espacio h={26} />
      <Caja color={TC.colors.brown} size={50}>
        {"Cierre perimetral\nya hecho."}
      </Caja>
    </Cuerpo>
  </Lienzo>
);

const E4: React.FC = () => (
  <Lienzo w={Z.carr.w} h={Z.carr.h}>
    <Foto src={OCT("e-casas")} foco="50% 54%" />
    <Degradado arriba={0.62} abajo={0.52} />
    <Marco archivo="MARCO-CARRUSEL-4" />
    <Cuerpo top={Z.carr.textoSinLogo} ancho={840}>
      <Ligera size={68}>{"¿Cuánto puedo construir?"}</Ligera>
      <Espacio h={20} />
      <Remate size={86}>{"Máximo dos casas\npor parcela."}</Remate>
      <Espacio h={22} />
      <Bajada size={38} ancho={700}>
        La tuya y la de tus visitas.
      </Bajada>
    </Cuerpo>
    {/* El carrusel no trae píldora en el marco: el CTA se dibuja acá. */}
    <div
      style={{
        position: "absolute",
        left: "50%",
        top: 1120,
        transform: "translateX(-50%)",
        display: "flex",
        alignItems: "center",
        gap: 14,
        border: "1.5px solid rgba(255,255,255,0.85)",
        borderRadius: 999,
        padding: "17px 40px",
      }}
    >
      <IconoWsp s={27} />
      <span
        style={{
          fontFamily: SANS,
          fontWeight: 500,
          fontSize: 31,
          letterSpacing: "0.07em",
          color: "#fff",
          textTransform: "uppercase",
          whiteSpace: "nowrap",
        }}
      >
        Escríbenos por el plano
      </span>
    </div>
  </Lienzo>
);

// =============================================================================
// G · 09/10 · POST ESTÁTICO 4:5 · fin de semana largo · Pilar 2
// =============================================================================

const G: React.FC = () => (
  <Lienzo w={Z.post.w} h={Z.post.h}>
    <Foto src={OCT("g-acceso")} foco="50% 56%" />
    <Degradado arriba={0.64} abajo={0.46} />
    <Marco archivo="MARCO-POST" />
    {/* 2 + 2: con "conocer" en la línea sans quedaba un huérfano de una palabra. */}
    <Cuerpo top={Z.post.texto} ancho={880}>
      <Ligera size={66}>{"Fin de semana largo,\nbuen momento para"}</Ligera>
      <Espacio h={20} />
      <Remate size={88}>{"conocer el sector\nen persona."}</Remate>
    </Cuerpo>
    <Pildora caja={Z.post.pill} icono={<IconoPin s={25} />} size={30}>
      Tierra Calma · Padre Hurtado
    </Pildora>
  </Lienzo>
);

// =============================================================================
// K · 20/10 · POST COMERCIAL 4:5 · "Sin letra chica" · Pilar 2
//
// ⚠️ El mapa va en DUOTONO y DESENFOCADO a propósito: el PNG original
// (MAPA-2.png, de MARCOS.ai) trae topónimos corruptos —"San Jocé",
// "Lono a Pénhilla", "Av. Vicuiia Mackenna"— y escudos de ruta que no
// corresponden. Se usa como TEXTURA cartográfica; los rótulos que se leen son
// los nuestros. No publicar el mapa con sus etiquetas nítidas.
// =============================================================================

const Dato: React.FC<{etiqueta: string; children: React.ReactNode}> = ({etiqueta, children}) => (
  <div style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 10}}>
    <span
      style={{
        fontFamily: SANS,
        fontWeight: 500,
        fontSize: 27,
        letterSpacing: "0.2em",
        textTransform: "uppercase",
        color: "rgba(255,255,255,0.78)",
      }}
    >
      {etiqueta}
    </span>
    {children}
  </div>
);

const K: React.FC = () => (
  <Lienzo w={Z.post.w} h={Z.post.h}>
    <Foto src={OCT("k-mapa")} foco="50% 50%" escala={1.04} />
    {/* Velo navy: baja el mapa a textura y deja respirar el dato. */}
    <AbsoluteFill style={{backgroundColor: "rgba(11,44,73,0.72)"}} />
    <AbsoluteFill
      style={{
        background:
          "radial-gradient(ellipse at 50% 46%, rgba(11,44,73,0) 32%, rgba(8,26,44,0.72) 100%)",
      }}
    />
    <Marco archivo="MARCO-POST" />
    <Cuerpo top={Z.post.texto} ancho={860}>
      <Ligera size={74}>{"Sin letra chica."}</Ligera>
      <Espacio h={16} />
      <Bajada size={37} ancho={680}>
        Las dos preguntas que más se repiten al buscar parcela, respondidas acá.
      </Bajada>
      <Espacio h={72} />
      <Dato etiqueta="Dónde queda">
        <Remate size={70}>{"a 15 min del peaje\nPadre Hurtado"}</Remate>
        <span
          style={{
            fontFamily: SANS,
            fontWeight: 500,
            fontSize: 32,
            letterSpacing: "0.17em",
            textTransform: "uppercase",
            color: TC.colors.sand,
            marginTop: 6,
          }}
        >
          Ruta 78 · Autopista del Sol
        </span>
      </Dato>
      <Espacio h={54} />
      <div style={{width: 210, height: 1, backgroundColor: "rgba(255,255,255,0.42)"}} />
      <Espacio h={54} />
      <Dato etiqueta="Cuánto cuesta">
        {/* La cifra es siempre el elemento más grande de la pieza. */}
        <div
          style={{
            fontFamily: SERIF,
            fontWeight: 400,
            fontSize: 150,
            lineHeight: 0.94,
            color: "#fff",
            letterSpacing: "-0.01em",
          }}
        >
          UF 2.500
        </div>
        <span
          style={{
            fontFamily: SANS,
            fontWeight: 300,
            fontSize: 34,
            color: "rgba(255,255,255,0.85)",
          }}
        >
          desde · parcelas de ~5.000 m²
        </span>
      </Dato>
    </Cuerpo>
    <Pildora caja={Z.post.pill} icono={<IconoWsp s={25} />} size={30}>
      Escríbenos por el plano
    </Pildora>
  </Lienzo>
);

// =============================================================================
// M · 29/10 · POST ESTÁTICO 4:5 · cierre de mes, hora azul · Pilar 1
// =============================================================================

const M: React.FC = () => (
  <Lienzo w={Z.post.w} h={Z.post.h}>
    <Foto src={OCT("m-horazul")} foco="50% 60%" />
    <Degradado arriba={0.5} abajo={0.44} velo={0.08} />
    <Marco archivo="MARCO-POST" />
    {/* 84/900: a 100 px el remate se partía en cuatro líneas y cruzaba la casa. */}
    <Cuerpo top={Z.post.texto} ancho={920}>
      <Ligera size={64}>{"Cada mes que pasa,"}</Ligera>
      <Espacio h={18} />
      <Remate size={84}>{"más cerca de tu\npróximo verano acá."}</Remate>
    </Cuerpo>
    <Pildora caja={Z.post.pill} icono={<IconoRegla s={25} />} size={30}>
      Tierra Calma · desde UF 2.500
    </Pildora>
  </Lienzo>
);

// =============================================================================
// H · 12/10 · HISTORIA 9:16 · contacto WhatsApp del feriado · Pilar 2
// El número comercial visible lo pide el brief explícitamente.
// =============================================================================

const H: React.FC = () => (
  <Lienzo w={Z.story.w} h={Z.story.h}>
    <Foto src={OCT("h-telefono")} foco="50% 58%" />
    <Degradado arriba={0.6} abajo={0.5} />
    <Marco archivo="MARCO-ST" />
    <Cuerpo top={Z.story.texto} ancho={800}>
      <Ligera size={64}>{"Feriado largo,\nbuen momento para"}</Ligera>
      <Espacio h={18} />
      <Remate size={90}>{"coordinar\ntu visita."}</Remate>
    </Cuerpo>

    <Vidrio x={128} y={905} w={560} rot={-2.4}>
      <div style={{display: "flex", alignItems: "center", gap: 16}}>
        <IconoWsp s={40} />
        <div>
          <div
            style={{
              fontFamily: SANS,
              fontWeight: 500,
              fontSize: 27,
              letterSpacing: "0.16em",
              textTransform: "uppercase",
              color: "rgba(255,255,255,0.82)",
            }}
          >
            WhatsApp
          </div>
          <div style={{fontFamily: SANS, fontWeight: 500, fontSize: 45, color: "#fff"}}>
            +56 9 9158 6643
          </div>
        </div>
      </div>
    </Vidrio>

    <Vidrio x={356} y={1108} w={600} rot={1.8}>
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 300,
          fontSize: 37,
          lineHeight: 1.32,
          color: "#fff",
        }}
      >
        Escríbenos hoy y coordinamos tu visita al sector.
      </div>
    </Vidrio>

    <Pildora caja={Z.story.pill} icono={<IconoWsp s={28} />} size={33}>
      Escríbenos hoy
    </Pildora>
  </Lienzo>
);

// =============================================================================
// L · 22/10 · HISTORIA 9:16 · crédito preaprobado · Pilar 3
// Repetición a propósito de una historia que ya funcionó (nota de la grilla).
// =============================================================================

const L: React.FC = () => (
  <Lienzo w={Z.story.w} h={Z.story.h}>
    <Foto src={OCT("l-terraza")} foco="50% 55%" />
    <Degradado arriba={0.58} abajo={0.5} />
    <Marco archivo="MARCO-ST" />
    {/* 64/920: "PODRÍAS ESTAR MÁS CERCA" es la línea más ancha del mes; a 76 se
        partía en tres y el remate se metía en la viga del alero. */}
    <Cuerpo top={Z.story.texto} ancho={920}>
      <Ligera size={60}>{"¿Ya tienes un\ncrédito preaprobado?"}</Ligera>
      <Espacio h={20} />
      <Remate size={64}>{"Podrías estar más cerca\nde lo que piensas."}</Remate>
    </Cuerpo>

    <Vidrio x={150} y={1010} w={620} rot={-2}>
      <div style={{display: "flex", alignItems: "center", gap: 18}}>
        <svg width={52} height={52} viewBox="0 0 24 24" fill="none" style={{flexShrink: 0}}>
          <circle cx="12" cy="12" r="9.2" stroke="#fff" strokeWidth="1.5" />
          <path
            d="M8 12.3l2.7 2.7L16 9.6"
            stroke="#fff"
            strokeWidth="1.9"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
        <div>
          <div
            style={{
              fontFamily: SANS,
              fontWeight: 500,
              fontSize: 26,
              letterSpacing: "0.16em",
              textTransform: "uppercase",
              color: "rgba(255,255,255,0.82)",
            }}
          >
            Crédito
          </div>
          <div style={{fontFamily: SANS, fontWeight: 500, fontSize: 44, color: "#fff"}}>
            Preaprobado
          </div>
        </div>
      </div>
    </Vidrio>

    <Vidrio x={300} y={1214} w={640} rot={1.6}>
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 300,
          fontSize: 36,
          lineHeight: 1.3,
          color: "#fff",
        }}
      >
        Parcelas de ~5.000 m², desde UF 2.500 en Padre Hurtado.
      </div>
    </Vidrio>

    <Pildora caja={Z.story.pill} icono={<IconoWsp s={28} />} size={33}>
      Escríbenos al WhatsApp
    </Pildora>
  </Lienzo>
);

// =============================================================================
// Agrupadores — un frame = una pieza, se rinden con `--sequence`
// =============================================================================

const Serie: React.FC<{piezas: React.FC[]}> = ({piezas}) => {
  const frame = useCurrentFrame();
  return (
    <>
      {piezas.map((P, i) => (
        <Sequence key={i} from={i} durationInFrames={1} layout="none">
          {frame === i ? <P /> : null}
        </Sequence>
      ))}
    </>
  );
};

export const OCT_CARRUSEL = [E1, E2, E3, E4];
export const OCT_POSTS = [G, K, M];
export const OCT_STORIES = [H, L];

export const OctCarrusel: React.FC = () => <Serie piezas={OCT_CARRUSEL} />;
export const OctPosts: React.FC = () => <Serie piezas={OCT_POSTS} />;
export const OctStories: React.FC = () => <Serie piezas={OCT_STORIES} />;
