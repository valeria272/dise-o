import React from "react";
import {AbsoluteFill, Img, staticFile, useVideoConfig} from "remotion";

// ============================================================
// PISOS CASABLANCA — Septiembre 2026
// C1 · Carrusel 4 productos autorizados (feed 1080x1080 + story 1080x1920)
// C2 · Post showroom Vitacura, 3 tarjetas (mismos formatos)
//
// Línea gráfica de agosto (carrusel_casablanca de Paulina):
// tarjeta blanca colgante con logo gris, serif itálica de alto
// contraste (Playfair Display ≈ la de las piezas), sans geométrica
// (Montserrat), filetes finos, sin precios ni urgencia.
//
// ⚠️ FONDOS C1: provisorios — textura cenital real de cada producto
// (fotos del sitio pisoscasablanca.cl). El brief pide UN MISMO
// AMBIENTE amplio en las 4 tarjetas cambiando solo el piso →
// se generan con Nano Banana (Higgsfield) cuando se reconecte el
// conector. Basta reemplazar los archivos bg de PRODUCTS.
// ============================================================

export const GRIS_LOGO = "#6b6b66";
export const CARBON = "#3a3733"; // titulares sobre muro claro (C1)
export const GRIS_TEXTO = "#5f5b55"; // secundarios sobre muro claro
const FONT_SERIF = "'Playfair Display', 'Georgia', serif";
const FONT_SANS = "'Montserrat', 'Helvetica Neue', sans-serif";
const FONT_SCRIPT = "'Sacramento', cursive";

const injectFonts = () => {
  if (typeof document === "undefined") return;
  if (document.getElementById("casablanca-fonts")) return;
  const style = document.createElement("style");
  style.id = "casablanca-fonts";
  style.textContent = `
    @font-face {
      font-family: 'Montserrat';
      src: url(${JSON.stringify(staticFile("assets/fonts/Montserrat.ttf"))}) format('truetype');
      font-weight: 100 900;
      font-style: normal;
      font-display: block;
    }
    @font-face {
      font-family: 'Playfair Display';
      src: url(${JSON.stringify(staticFile("assets/fonts/PlayfairDisplay-Italic.ttf"))}) format('truetype');
      font-weight: 400 900;
      font-style: italic;
      font-display: block;
    }
    @font-face {
      font-family: 'Playfair Display';
      src: url(${JSON.stringify(staticFile("assets/fonts/PlayfairDisplay.ttf"))}) format('truetype');
      font-weight: 400 900;
      font-style: normal;
      font-display: block;
    }
    @font-face {
      font-family: 'Sacramento';
      src: url(${JSON.stringify(staticFile("assets/fonts/Sacramento.ttf"))}) format('truetype');
      font-weight: 400;
      font-style: normal;
      font-display: block;
    }
  `;
  document.head.appendChild(style);
  document.fonts.load("italic 700 100px 'Playfair Display'").catch(() => {});
  document.fonts.load("600 100px Montserrat").catch(() => {});
};
injectFonts();

// ------------------------------------------------------------
// Datos C1 — los 4 productos autorizados (NO mostrar otros)
// ------------------------------------------------------------
type C1Card = {
  look: string;
  nombre: string;
  medida: string;
  frase: string;
  bg: string; // escena: mismo living, solo cambia el piso instalado
  tabla: string; // packshot vertical de la tabla real del producto
};

const C1_CARDS: C1Card[] = [
  {
    look: "Look Natural UV",
    nombre: "Roble Natural UV",
    medida: "14/3 · 190 × 1900 mm",
    frase: "LA CALIDEZ DEL ROBLE CON PROTECCIÓN UV, EN FORMATO AMPLIO",
    bg: "assets/casablanca/escena_natural_uv_grande.jpg",
    tabla: "assets/casablanca/tabla_natural_uv_grande.png",
  },
  {
    look: "Look Natural UV",
    nombre: "Roble Natural UV",
    medida: "10/1.2 · 167 × 1200 mm",
    frase: "EL MISMO ACABADO, EN UNA PROPORCIÓN MÁS CONTENIDA",
    bg: "assets/casablanca/escena_natural_uv_chico.jpg",
    tabla: "assets/casablanca/tabla_natural_uv_chico.png",
  },
  {
    look: "Look Rústico",
    nombre: "Roble Aserrado",
    medida: "14/3 · 190 × 1900 mm",
    frase: "TEXTURA ASERRADA Y VETA A LA VISTA: CARÁCTER EN CADA TABLA",
    bg: "assets/casablanca/escena_aserrado.jpg",
    tabla: "assets/casablanca/tabla_aserrado.png",
  },
  {
    look: "Look Tradicional",
    nombre: "Cumarú",
    medida: "12/2 · 120 × 2130 mm",
    frase: "TABLA LARGA Y ANGOSTA, DEL FORMATO CLÁSICO QUE NO SE PASA DE MODA",
    bg: "assets/casablanca/escena_cumaru.jpg",
    tabla: "assets/casablanca/tabla_cumaru.png",
  },
];

// ------------------------------------------------------------
// Datos C2 — showroom Vitacura (fotos reales del cliente)
// ------------------------------------------------------------
type C2Card = {
  etiqueta?: string;
  titulo: string;
  bajada?: string[];
  bg: string;
  bgPosFeed: string;
  bgPosStory: string;
  // zoom vertical en story: muestra el tramo superior de la foto ampliado
  // (baja las caras para que no choquen con la tarjeta del logo)
  zoomStory?: number;
};

const C2_CARDS: C2Card[] = [
  {
    etiqueta: "SHOWROOM CASABLANCA · VITACURA",
    titulo: "Ven a ver tu piso en persona",
    bg: "assets/casablanca/showroom_t1_interior.jpg",
    bgPosFeed: "center center",
    bgPosStory: "62% center",
  },
  {
    titulo: "Compara texturas, tonos y formatos",
    bajada: ["Con asesoría de nuestro equipo"],
    bg: "assets/casablanca/showroom_t2_equipo.jpg",
    bgPosFeed: "center 20%",
    bgPosStory: "center top",
    zoomStory: 1.32,
  },
  {
    titulo: "Te esperamos",
    bajada: [
      "Juan XXIII 6359, Vitacura",
      "Agenda tu visita por WhatsApp +56 9 6653 5124",
    ],
    bg: "assets/casablanca/showroom_t3_fachada.jpg",
    bgPosFeed: "center 68%",
    bgPosStory: "38% 72%",
  },
];

// ------------------------------------------------------------
// Piezas compartidas
// ------------------------------------------------------------

// Tarjeta blanca del logo — cuelga del borde superior, esquinas rectas.
// Es el ancla del sistema de agosto y va idéntica en todas las piezas.
// (en story el borde superior es zona de UI de Instagram: 250 px libres)
const LogoCard: React.FC<{story?: boolean}> = ({story}) => (
  <div
    style={{
      position: "absolute",
      top: story ? 280 : 0,
      left: "50%",
      transform: "translateX(-50%)",
      width: 220,
      padding: story ? "34px 0 30px" : "48px 0 30px",
      backgroundColor: "#ffffff",
      display: "flex",
      justifyContent: "center",
    }}
  >
    <Img
      src={staticFile("assets/casablanca/logo_gris.png")}
      style={{width: 132, height: "auto"}}
    />
  </div>
);

// Foto full-bleed + velo cálido para legibilidad
const Background: React.FC<{
  src: string;
  position?: string;
  veil: string;
  zoom?: number;
}> = ({src, position = "center", veil, zoom = 1}) => (
  <>
    <Img
      src={staticFile(src)}
      style={{
        position: "absolute",
        top: 0,
        left: 0,
        width: "100%",
        height: `${zoom * 100}%`,
        objectFit: "cover",
        objectPosition: position,
      }}
    />
    <AbsoluteFill style={{background: veil}} />
  </>
);

// Filete blanco de 1 px — va pegado arriba y abajo de la bajada
const Filete: React.FC<{width?: number}> = ({width = 620}) => (
  <div
    style={{width, height: 1, backgroundColor: "rgba(255,255,255,0.75)"}}
  />
);

// CTA del sistema: rectángulo blanco sólido, esquinas rectas, texto gris.
const CtaBloque: React.FC<{texto: string}> = ({texto}) => (
  <div
    style={{
      backgroundColor: "#ffffff",
      color: "#4a4741",
      fontFamily: FONT_SANS,
      fontSize: 34,
      fontWeight: 500,
      letterSpacing: 0.5,
      padding: "20px 58px",
    }}
  >
    {texto}
  </div>
);

// ------------------------------------------------------------
// C1 — tarjeta de producto (sistema de mayo, el que aprobó la clienta)
// ------------------------------------------------------------
// Escena de living con el piso instalado como protagonista + packshot de la
// tabla real en vertical con su píldora gris. Texto blanco sobre la madera,
// tarjeta blanca del logo arriba al centro y CTA en rectángulo blanco sólido.
const C1Slide: React.FC<{card: number}> = ({card}) => {
  const {height} = useVideoConfig();
  const story = height > 1400;
  const data = C1_CARDS[card - 1];

  // Oscurecimiento cálido hacia abajo: el piso se apaga lo justo para que el
  // texto blanco lea, sin perder la veta.
  const veil = story
    ? "linear-gradient(180deg, rgba(28,20,13,0.10) 0%, rgba(28,20,13,0.06) 34%, rgba(28,20,13,0.30) 60%, rgba(28,20,13,0.62) 84%, rgba(28,20,13,0.68) 100%)"
    : "linear-gradient(180deg, rgba(28,20,13,0.12) 0%, rgba(28,20,13,0.06) 28%, rgba(28,20,13,0.34) 56%, rgba(28,20,13,0.64) 84%, rgba(28,20,13,0.70) 100%)";

  // Proporciones calcadas de las piezas de mayo: la tabla termina justo antes
  // de que empiece la cursiva, y el bloque de texto ocupa el tercio inferior.
  const tablaTop = story ? 430 : 112;
  const tablaAlto = story ? 560 : 400;
  const bloqueTop = story ? 1030 : 534;

  return (
    <AbsoluteFill style={{backgroundColor: "#2a201a", fontFamily: FONT_SANS}}>
      <Background src={data.bg} veil={veil} />
      <LogoCard story={story} />

      {/* Packshot: la tabla real del producto, en vertical, con sombra */}
      <Img
        src={staticFile(data.tabla)}
        style={{
          position: "absolute",
          top: tablaTop,
          left: story ? 128 : 118,
          width: Math.round(tablaAlto * 0.32),
          height: tablaAlto,
          objectFit: "cover",
          boxShadow: "0 18px 46px rgba(0,0,0,0.45)",
        }}
      />

      {/* Píldora gris cruzando la tabla, con la ficha del producto */}
      <div
        style={{
          position: "absolute",
          top: tablaTop + Math.round(tablaAlto * 0.19),
          left: story ? 72 : 62,
          backgroundColor: "rgba(72,70,66,0.90)",
          color: "#fff",
          padding: "14px 26px",
          textAlign: "center",
        }}
      >
        <div style={{fontSize: 25, fontWeight: 400, letterSpacing: 0.4}}>
          Piso de Ingeniería
        </div>
        <div style={{fontSize: 27, fontWeight: 700, marginTop: 4}}>
          {data.medida}
        </div>
      </div>

      {/* Bloque de texto inferior */}
      <div
        style={{
          position: "absolute",
          top: bloqueTop,
          left: 0,
          width: "100%",
          paddingLeft: story ? 100 : 78,
          paddingRight: story ? 130 : 78,
          boxSizing: "border-box",
          color: "#fff",
        }}
      >
        {/* Colección, en cursiva */}
        <div
          style={{
            fontFamily: FONT_SCRIPT,
            fontSize: 68,
            lineHeight: 1,
            marginLeft: 12,
            textShadow: "0 2px 12px rgba(0,0,0,0.45)",
          }}
        >
          {data.look}
        </div>

        {/* Nombre del producto — lo más grande */}
        <div
          style={{
            marginTop: 26,
            fontFamily: FONT_SERIF,
            fontStyle: "italic",
            fontWeight: 700,
            fontSize: story ? 104 : 100,
            lineHeight: 1.1,
            textAlign: "center",
            textShadow: "0 4px 20px rgba(0,0,0,0.5)",
          }}
        >
          {data.nombre}
        </div>

        {/* Filete + frase + filete */}
        <div
          style={{
            marginTop: 24,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 16,
          }}
        >
          <Filete width={story ? 810 : 890} />
          <div
            style={{
              fontSize: 24,
              fontWeight: 500,
              letterSpacing: 2,
              lineHeight: 1.5,
              textAlign: "center",
              maxWidth: 650,
              textShadow: "0 2px 10px rgba(0,0,0,0.5)",
            }}
          >
            {data.frase}
          </div>
          <Filete width={story ? 810 : 890} />
        </div>

        {/* CTA */}
        <div
          style={{
            marginTop: 30,
            display: "flex",
            justifyContent: "center",
          }}
        >
          <CtaBloque texto="COTIZA POR WHATSAPP" />
        </div>

        {/* Indicador de deslizar — solo tarjeta 1 */}
        {card === 1 && (
          <div
            style={{
              marginTop: 20,
              textAlign: "center",
              fontSize: 22,
              fontWeight: 500,
              letterSpacing: 3,
              textShadow: "0 2px 8px rgba(0,0,0,0.45)",
            }}
          >
            desliza y descubre&nbsp;&nbsp;⟶
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------
// C2 — showroom
// ------------------------------------------------------------
const C2Slide: React.FC<{card: number}> = ({card}) => {
  const {height} = useVideoConfig();
  const story = height > 1400;
  const data = C2_CARDS[card - 1];

  // Texto abajo sobre velo cálido; la foto respira arriba
  const veil = story
    ? "linear-gradient(180deg, rgba(20,15,10,0.18) 0%, rgba(20,15,10,0.06) 34%, rgba(20,15,10,0.14) 52%, rgba(22,16,11,0.78) 82%, rgba(22,16,11,0.88) 100%)"
    : "linear-gradient(180deg, rgba(20,15,10,0.16) 0%, rgba(20,15,10,0.05) 30%, rgba(20,15,10,0.16) 52%, rgba(22,16,11,0.78) 82%, rgba(22,16,11,0.9) 100%)";

  return (
    <AbsoluteFill style={{backgroundColor: "#241c14", fontFamily: FONT_SANS}}>
      <Background
        src={data.bg}
        position={story ? data.bgPosStory : data.bgPosFeed}
        veil={veil}
        zoom={story ? data.zoomStory ?? 1 : 1}
      />
      <LogoCard story={story} />

      <div
        style={{
          position: "absolute",
          bottom: story ? 420 : 172,
          left: 0,
          width: "100%",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          textAlign: "center",
          color: "#fff",
          paddingLeft: 70,
          paddingRight: story ? 120 : 70,
          boxSizing: "border-box",
        }}
      >
        {/* Indicador de deslizar — tarjeta 1, arriba del bloque */}
        {card === 1 && (
          <div
            style={{
              marginBottom: 28,
              fontSize: 25,
              fontWeight: 500,
              letterSpacing: 3,
              opacity: 0.9,
              textShadow: "0 2px 8px rgba(0,0,0,0.4)",
            }}
          >
            desliza y descubre&nbsp;&nbsp;⟶
          </div>
        )}

        {data.etiqueta && (
          <div
            style={{
              fontSize: 27,
              fontWeight: 600,
              letterSpacing: 8,
              marginBottom: 26,
              textShadow: "0 2px 10px rgba(0,0,0,0.5)",
            }}
          >
            {data.etiqueta}
          </div>
        )}

        <div
          style={{
            fontFamily: FONT_SERIF,
            fontStyle: "italic",
            fontWeight: 700,
            fontSize: card === 3 ? 116 : 92,
            lineHeight: 1.12,
            maxWidth: 880,
            textShadow: "0 4px 22px rgba(0,0,0,0.55)",
          }}
        >
          {data.titulo}
        </div>

        {data.bajada && (
          <div
            style={{
              marginTop: 34,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              gap: 20,
            }}
          >
            <Filete width={440} />
            <div
              style={{
                fontSize: 35,
                fontWeight: 500,
                lineHeight: 1.5,
                letterSpacing: 0.5,
                textShadow: "0 2px 10px rgba(0,0,0,0.5)",
              }}
            >
              {data.bajada.map((l) => (
                <div key={l}>{l}</div>
              ))}
            </div>
            <Filete width={440} />
          </div>
        )}

        {/* CTA solo en la tarjeta de cierre */}
        {card === 3 && (
          <div style={{marginTop: 52}}>
            <CtaBloque texto="AGENDA TU VISITA" />
          </div>
        )}

      </div>
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------
// Entry
// ------------------------------------------------------------
export type CasablancaSlideProps = {
  piece: "c1" | "c2";
  card: number;
};

export const CasablancaSlide: React.FC<CasablancaSlideProps> = ({piece, card}) => {
  injectFonts();
  return piece === "c1" ? <C1Slide card={card} /> : <C2Slide card={card} />;
};

export const casablancaDefaults: CasablancaSlideProps = {piece: "c1", card: 1};
