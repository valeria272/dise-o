import {staticFile} from "remotion";

// ============================================================
// TIERRA CALMA (Padre Hurtado, RM) — cliente · parcelas 5.000 m²
// Fuente de verdad para nuevas piezas: importar desde acá en vez
// de re-declarar colores/fuentes en cada composición.
// Manual completo del cliente: clients/tierra-calma/CLAUDE.md
// ============================================================

// TIPOGRAFÍA — leer antes de tocar.
//
// La marca usa **IvyOra Display** (Adobe Fonts) + **Inter Tight**.
//
// · Inter Tight es libre y está auto-hospedada en public/assets/fonts/.
// · IvyOra viene de la suscripción de Adobe Fonts de la usuaria. Está activada
//   en este equipo, pero Adobe **no la registró en CoreText**: el sistema no la
//   ve y Chrome —el motor de render de Remotion— tampoco (probado con las 9
//   variantes de nombre; todas caían al serif por defecto).
//   Por eso `scripts/tc-ivyora-link.sh` crea **enlaces simbólicos** desde
//   public/assets/fonts/ivyora/ a los .otf que Adobe ya tiene en disco.
//   No se copia ni se versiona nada: la carpeta está en .gitignore y los bytes
//   siguen en el directorio de Adobe. Es el mismo uso que hace Illustrator.
//
// ⚠️ Si los enlaces se rompen (Adobe re-sincroniza y cambia los nombres
//    internos), correr de nuevo `bash scripts/tc-ivyora-link.sh`.
// ⚠️ Para web/artifacts esta vía NO sirve: eso exige un "web project" de Adobe
//    Fonts. Ahí hay que usar Instrument Serif como equivalente.

const IVY = `'IvyOra Display'`;

export const tierracalma = {
  colors: {
    navy: "#0B2C49", // institucional — color del LOGO ANIMADO oficial (tc_motion.mp4)
    green: "#003326", // verde profundo — color del logo ESTÁTICO (tc_logo.png)
    cream: "#F3EEE3", // crema cálido de fondo
    paper: "#FFFFFF",
    ink: "#12181C", // texto oscuro sobre claro
    sand: "#C9B99A", // acento tierra para filetes y subrayados
    // Paleta secundaria de marca, enviada por Carlos Figueroa (diseño) el 21-08-2026:
    // "variar con los colores de la marca". Para lavados, píldoras, fondos de
    // slides de proceso y cartelas — NO para reemplazar navy/verde del logo.
    slate: "#3C525F", // azul pizarra
    olive: "#4A553F", // verde oliva
    brown: "#6C473D", // café tierra
    mist: "rgba(255,255,255,0.72)", // texto secundario sobre foto
  },
  fonts: {
    // Titulares y CIFRAS. La cifra es el elemento más grande de la pieza.
    display: `${IVY}, 'Instrument Serif', Georgia, serif`,
    // Bajadas, listas, etiquetas en mayúsculas con tracking.
    body: "'Inter Tight', 'Inter', 'Helvetica Neue', sans-serif",
    /**
     * ⚠️ LA MANO — un tercer rol RESTRINGIDO, agregado el 24-09-2026.
     *
     * El manual dice «sólo DOS roles tipográficos». Esta es la excepción y tiene
     * un solo uso declarado: el **post-it manuscrito** de `p-29-10`, que el
     * brief pide con esas palabras (*"un post-it grande… escrito a mano"*) y que
     * la referencia que pasó Diego el 24-09 confirma.
     *
     * ⛔ NO se usa en titulares, ni en cifras, ni en CTA, ni en ninguna otra
     * pieza. Si aparece en una segunda pieza sin que nadie lo pida, está mal.
     *
     * Ojo: `Caveat` es además **la mano de Copywriters** (la cuenta propia).
     * Compartir el archivo no es compartir el sistema, pero conviene saberlo
     * antes de darle más espacio acá.
     */
    mano: "'Caveat', 'Segoe Script', cursive",
    mono: "ui-monospace, monospace",
  },
  name: "Tierra Calma",
  url: "tierracalma.cl",
  tagline: "Parcelas en Padre Hurtado. Más espacio. Más calma. Más vida.",
  category: "Inmobiliaria / parcelas de agrado",
  logo: "assets/tierracalma/tc_logo.png", // estático (verde)
  logoWhite: "assets/tierracalma/tc_logo_white.png", // knockout para sobre foto
  logoMotion: "assets/tierracalma/tc_motion.mp4", // OFICIAL animado (navy sobre blanco) — cierre de todo reel

  // Música de marca: instrumentales en registro de calma (Mixkit, libres).
  // Una distinta por reel, mismo estilo — el mes no puede sonar repetido.
  music: {
    sereneView: "assets/tierracalma/mus_serene-view.mp3",
    valleySunset: "assets/tierracalma/mus_valley-sunset.mp3",
    vastness: "assets/tierracalma/mus_vastness.mp3",
    sweetSeptember: "assets/tierracalma/mus_sweet-september.mp3",
  },

  // DATOS APROBADOS — los únicos publicables sin pedir permiso.
  // Fuente: "Brief Diseño Tierra Calma | Septiembre 2026" (Drive · PERFORMANCE).
  claims: {
    superficie: "5.000 m²",
    precio: "desde UF 2.500",
    santiago: "30 min de Santiago",
    peaje: "15 min del peaje Padre Hurtado",
    equipamiento: "canchas de fútbol y pádel",
    servicios: "colegios, supermercado y bancos a minutos",
    comuna: "Padre Hurtado, RM",
    ruta: "Autopista del Sol (Ruta 78), salida Padre Hurtado", // NO es la Ruta 68
  },
} as const;

// IvyOra (enlazada) + Inter Tight + Instrument Serif de respaldo, todas por
// @font-face. Nunca `loadGoogleFont()`: cuelga el render con delayRender.
let tcFontsInjected = false;
export const ensureTierraCalmaFonts = () => {
  if (tcFontsInjected || typeof document === "undefined") return;
  tcFontsInjected = true;
  const f = (n: string) => staticFile(`assets/fonts/${n}.ttf`);
  const weights: [number, string][] = [
    [300, "Light"],
    [400, "Regular"],
    [500, "Medium"],
    [600, "SemiBold"],
    [700, "Bold"],
  ];
  // IvyOra Display: 5 pesos + itálicas. Los archivos son enlaces a Adobe Fonts.
  const ivy: [number, string][] = [
    [100, "Thin"],
    [300, "Light"],
    [400, "Regular"],
    [500, "Medium"],
    [700, "Bold"],
  ];
  const ivyFace = (fam: string, prefix: string) =>
    ivy
      .map(([w, n]) =>
        [
          `@font-face { font-family:'${fam}'; font-style:normal; font-weight:${w}; font-display:block;
      src:url(${staticFile(`assets/fonts/ivyora/${prefix}-${n}.otf`)}) format('opentype'); }`,
          `@font-face { font-family:'${fam}'; font-style:italic; font-weight:${w}; font-display:block;
      src:url(${staticFile(`assets/fonts/ivyora/${prefix}-${n === "Regular" ? "Italic" : `${n}Italic`}.otf`)}) format('opentype'); }`,
        ].join("\n"),
      )
      .join("\n");

  const style = document.createElement("style");
  style.textContent = `
    ${ivyFace("IvyOra Display", "IvyOraDisplay")}
    ${ivyFace("IvyOra Text", "IvyOraText")}
    ${weights
      .map(
        ([w, n]) => `@font-face { font-family:'Inter Tight'; font-style:normal; font-weight:${w}; font-display:block;
      src:url(${f(`InterTight-${n}`)}) format('truetype'); }`,
      )
      .join("\n")}
    @font-face { font-family:'Inter Tight'; font-style:italic; font-weight:400; font-display:block;
      src:url(${f("InterTight-Italic")}) format('truetype'); }
    @font-face { font-family:'Instrument Serif'; font-style:normal; font-weight:400; font-display:block;
      src:url(${f("InstrumentSerif")}) format('truetype'); }
    @font-face { font-family:'Instrument Serif'; font-style:italic; font-weight:400; font-display:block;
      src:url(${f("InstrumentSerif-Italic")}) format('truetype'); }
    @font-face { font-family:'Caveat'; font-style:normal; font-weight:400 700; font-display:block;
      src:url(${staticFile("assets/fonts/copywriters/Caveat-Variable.ttf")}) format('truetype'); }
  `;
  document.head.appendChild(style);
  // Los .catch NO son decorativos: IvyOra viene de Adobe Fonts y sólo existe en
  // los equipos que la tienen activada y enlazada (scripts/tc-ivyora-link.sh).
  // Donde no está, estas cargas fallan; sin recoger el rechazo, Remotion lo lee
  // como error de página y aborta el render de CUALQUIER marca — Casablanca y
  // Revex incluidas, que no tienen nada que ver con Tierra Calma. Mismo patrón
  // que TierraCalmaReel.tsx ya usaba para Montserrat.
  const fs = (document as unknown as {
    fonts?: {load: (s: string) => Promise<unknown>};
  }).fonts;
  if (fs) {
    const cargar = (spec: string) => fs.load(spec).catch(() => undefined);
    ivy.forEach(([w]) => {
      cargar(`${w} 100px "IvyOra Display"`);
      cargar(`italic ${w} 100px "IvyOra Display"`);
    });
    weights.forEach(([w]) => cargar(`${w} 40px "Inter Tight"`));
    cargar('400 100px "Instrument Serif"');
  }
};
