import React from "react";
import {AbsoluteFill, Img, Sequence, staticFile, useCurrentFrame} from "remotion";
import {tierracalma as TC} from "../../brand/tierracalma";
import {MapaEstatico} from "./MapaEstatico";
import {
  Cifra,
  CirculoIcono,
  Cuerpo,
  Degradado,
  Entrada,
  Espacio,
  Etiqueta,
  Filete,
  Flecha,
  Foto,
  Fuerte,
  Icono,
  Lavado,
  Ligera,
  Lienzo,
  LogoArriba,
  Marco,
  Pildora,
  Remate,
  SANS,
  ZonaPildora,
  ZONAS,
} from "./sistema";

// =============================================================================
// TIERRA CALMA · PIEZAS ESTÁTICAS · SEPTIEMBRE 2026
//
// Un frame = una pieza. Se rinden de una pasada con `--sequence`:
//   npx remotion render TCPiezas4x5 out/.../seq --sequence --image-format=png
//
// Las fotos son IA (public/assets/tierracalma/ia/), no dron: el material del
// rodaje del 07-08 es de mañana nublada y baja la percepción premium. Se
// reserva para los reels. Regla de Valeria, 19-08-2026.
//
// El copy sale VERBATIM de clients/tierra-calma/grilla-septiembre-2026.md.
// Los datos, de la lista blanca de src/brand/tierracalma.ts → claims.
// =============================================================================

const IA = (n: string) => `assets/tierracalma/ia/${n}.png`;
const UBIC = "Padre Hurtado · Región Metropolitana";

// -----------------------------------------------------------------------------
// E1 · 01/09 · Carrusel 4:5 · "Tu nueva rutina empieza aquí" · Pilar 2
// -----------------------------------------------------------------------------
const E1s1: React.FC = () => (
  <Lienzo f="4x5">
    <Foto src={IA("e1_1_amanecer")} foco="50% 46%" />
    <Degradado tipo="ambos" />
    <Marco f="4x5" variante="hueco" />
    <LogoArriba f="4x5" />
    <Cuerpo f="4x5">
      <Etiqueta>Así se vive en Tierra Calma</Etiqueta>
      <Espacio h={26} />
      <Ligera size={78} caps>
        Tu nueva rutina
      </Ligera>
      <Remate size={98}>empieza aquí.</Remate>
    </Cuerpo>
    <ZonaPildora f="4x5" conFlecha>
      <Pildora icono="pin" texto={UBIC} />
    </ZonaPildora>
    <Flecha f="4x5" />
  </Lienzo>
);

const E1s2: React.FC = () => (
  <Lienzo f="4x5">
    <Foto src={IA("e1_3_camino")} foco="50% 54%" />
    <Degradado tipo="ambos" fuerza={1.05} />
    <Marco f="4x5" variante="derecha" op={0.6} />
    <Cuerpo f="4x5" alinear="centro">
      <Ligera size={74} caps>
        Desde Santiago,
      </Ligera>
      <Remate size={92}>
        derecho al
        <br />
        surponiente.
      </Remate>
      <Filete ancho={120} margen={42} />
      <Ligera size={38} peso={300} color="rgba(255,255,255,0.9)" lh={1.26}>
        Autopista del Sol · Ruta 78, salida Padre Hurtado.
        <br />
        Después, la Cuesta Barriga.
      </Ligera>
    </Cuerpo>
    <ZonaPildora f="4x5" conFlecha>
      <Pildora icono="ruta" texto="Autopista del Sol · Ruta 78" />
    </ZonaPildora>
    <Flecha f="4x5" />
  </Lienzo>
);

// Slide de mapa: fondo crema, tinta navy. Rompe el ritmo de foto del carrusel.
const E1s3: React.FC = () => {
  const z = ZONAS["4x5"];
  return (
    <Lienzo f="4x5">
      <AbsoluteFill style={{background: TC.colors.cream}} />
      <div
        style={{
          position: "absolute",
          left: z.inset,
          top: z.inset,
          right: z.inset,
          bottom: z.inset,
          border: `1.4px solid rgba(11,44,73,0.22)`,
          borderRadius: z.radio,
        }}
      />
      <div style={{position: "absolute", left: 0, right: 0, top: 96}}>
        <MapaEstatico />
      </div>
      <div style={{position: "absolute", left: z.margen, right: z.margen, bottom: 176}}>
        <div
          style={{
            fontFamily: SANS,
            fontSize: 25,
            fontWeight: 600,
            letterSpacing: "0.24em",
            textTransform: "uppercase",
            color: "#9C8963",
            marginBottom: 22,
          }}
        >
          Cómo se llega
        </div>
        <div style={{fontFamily: SANS, fontSize: 62, fontWeight: 300, lineHeight: 1.1, color: TC.colors.navy, letterSpacing: "-0.012em"}}>
          Conectado con Santiago.
        </div>
        <div
          style={{
            fontFamily: TC.fonts.display,
            fontStyle: "italic",
            fontSize: 74,
            fontWeight: 400,
            lineHeight: 1.06,
            color: TC.colors.navy,
            letterSpacing: "-0.015em",
            marginTop: 4,
          }}
        >
          Sin renunciar a la calma.
        </div>
      </div>
      <div style={{position: "absolute", left: z.margen, bottom: 96, display: "flex", alignItems: "center", gap: 14}}>
        <Icono id="reloj" d={30} color={TC.colors.navy} grosor={1.6} />
        <span style={{fontFamily: SANS, fontSize: 29, fontWeight: 400, color: TC.colors.navy, opacity: 0.82}}>
          30 min de Santiago · 15 del peaje Padre Hurtado
        </span>
      </div>
      <Flecha f="4x5" oscura />
    </Lienzo>
  );
};

const E1s4: React.FC = () => (
  <Lienzo f="4x5">
    <Foto src={IA("e1_4_llegada")} foco="50% 50%" />
    <Lavado op={0.88} />
    <Marco f="4x5" variante="bandas" op={0.5} />
    <Cuerpo f="4x5" alinear="centro" centrado>
      <CirculoIcono id="whatsapp" d={382} />
      <Espacio h={74} />
      <Fuerte size={64}>
        Vivir en parcela
        <br />
        no es vivir aislado.
      </Fuerte>
      <Espacio h={26} />
      <Ligera size={48} color="rgba(255,255,255,0.92)" lh={1.2}>
        Colegios, supermercado y bancos
        <br />
        a minutos de tu casa.
      </Ligera>
    </Cuerpo>
    <ZonaPildora f="4x5">
      <Pildora icono="whatsapp" texto="Escríbenos y te enviamos el plano" />
    </ZonaPildora>
  </Lienzo>
);

// -----------------------------------------------------------------------------
// E2 · 04/09 · Carrusel 4:5 · "Tu parcela. Tus reglas." · Pilar 1
// El slide 3 va con casa de huéspedes, NO con cabañas Airbnb: el reglamento
// permite máximo dos casas por parcela (alerta 2.3 de la grilla).
// -----------------------------------------------------------------------------
const E2s1: React.FC = () => (
  <Lienzo f="4x5">
    <Foto src={IA("e2_1_parcela")} foco="50% 52%" />
    <Degradado tipo="ambos" />
    <Marco f="4x5" variante="hueco" />
    <LogoArriba f="4x5" />
    <Cuerpo f="4x5">
      <Etiqueta>~5.000 m² · desde UF 2.500</Etiqueta>
      <Espacio h={26} />
      <Ligera size={82} caps>
        Tu parcela.
      </Ligera>
      <Remate size={104}>Tus reglas.</Remate>
    </Cuerpo>
    <ZonaPildora f="4x5" conFlecha>
      <Pildora icono="pin" texto={UBIC} />
    </ZonaPildora>
    <Flecha f="4x5" />
  </Lienzo>
);

const SlideIcono: React.FC<{
  foto: string;
  icono: React.ComponentProps<typeof CirculoIcono>["id"];
  titulo: React.ReactNode;
  bajada: React.ReactNode;
}> = ({foto, icono, titulo, bajada}) => (
  <Lienzo f="4x5">
    <Foto src={IA(foto)} foco="50% 50%" />
    <Lavado op={0.9} />
    <Marco f="4x5" variante="bandas" op={0.5} />
    <Cuerpo f="4x5" alinear="centro" centrado>
      <CirculoIcono id={icono} d={382} />
      <Espacio h={74} />
      <Fuerte size={66}>{titulo}</Fuerte>
      <Espacio h={26} />
      <Ligera size={48} color="rgba(255,255,255,0.92)" lh={1.2}>
        {bajada}
      </Ligera>
    </Cuerpo>
    <Flecha f="4x5" />
  </Lienzo>
);

const E2s2: React.FC = () => (
  <SlideIcono
    foto="e2_2_casa"
    icono="casa"
    titulo="La casa principal"
    bajada={
      <>
        El proyecto que llevas años
        <br />
        dibujando en tu cabeza.
      </>
    }
  />
);

const E2s3: React.FC = () => (
  <SlideIcono
    foto="e2_3_huespedes"
    icono="huespedes"
    titulo={
      <>
        Y una casa
        <br />
        de huéspedes
      </>
    }
    bajada={
      <>
        Una segunda vivienda en el mismo
        <br />
        terreno. Y la huerta al lado.
      </>
    }
  />
);

const E2s4: React.FC = () => (
  <Lienzo f="4x5">
    <Foto src={IA("e2_4_quincho")} foco="50% 30%" />
    <Degradado tipo="ambos" fuerza={1.18} />
    <Marco f="4x5" variante="izquierda" op={0.6} />
    <Cuerpo f="4x5">
      <Ligera size={74} caps>
        Una parcela es
      </Ligera>
      <Remate size={94}>
        el comienzo de
        <br />
        mucho más.
      </Remate>
      <Filete ancho={120} margen={42} />
      <Ligera size={38} color="rgba(255,255,255,0.9)" lh={1.26}>
        La casa. La huerta. El quincho.
        <br />
        Lo que tú decidas.
      </Ligera>
    </Cuerpo>
    <ZonaPildora f="4x5">
      {/* CTA verbatim del brief. El precio ya vive en la etiqueta del slide 1:
          repetirlo acá alargaba la píldora hasta rozar el marco. */}
      <Pildora icono="whatsapp" texto="Agenda tu visita" />
    </ZonaPildora>
  </Lienzo>
);

// -----------------------------------------------------------------------------
// E3 · 08/09 · Post 4:5 · "5.000 m². Desde UF 2.500." · Pilar 3
// La cifra es el elemento más grande de la pieza (regla del brief de pauta).
// -----------------------------------------------------------------------------
const E3: React.FC = () => (
  <Lienzo f="4x5">
    <Foto src={IA("e3_ficha")} foco="50% 72%" />
    <Degradado tipo="ambos" fuerza={1.16} />
    <Marco f="4x5" variante="hueco" />
    <LogoArriba f="4x5" />
    <Cuerpo f="4x5" alinear="abajo" centrado>
      <Ligera size={30} caps color="rgba(255,255,255,0.78)" peso={500}>
        Superficie
      </Ligera>
      <Espacio h={12} />
      <Cifra size={152}>~5.000 m²</Cifra>
      <Filete ancho={130} margen={40} />
      <Ligera size={30} caps color="rgba(255,255,255,0.78)" peso={500}>
        Desde
      </Ligera>
      <Espacio h={12} />
      <Cifra size={152}>UF 2.500</Cifra>
      <Espacio h={26} />
      <Ligera size={31} caps color="rgba(255,255,255,0.8)" peso={500}>
        Padre Hurtado, RM
      </Ligera>
    </Cuerpo>
    <ZonaPildora f="4x5">
      <Pildora icono="reloj" texto="30 min de Santiago · 15 del peaje" />
    </ZonaPildora>
  </Lienzo>
);

// -----------------------------------------------------------------------------
// E4 · 18/09 · Post 1:1 · Saludo Fiestas Patrias · Pilar 1
// Escena IA de golden hour, no una postal plana: es la pieza más compartida del
// mes y tiene que verse como el resto de la marca.
// -----------------------------------------------------------------------------
const E4: React.FC = () => (
  <Lienzo f="1x1">
    <Foto src={IA("e4_patrio")} foco="50% 52%" />
    <Degradado tipo="ambos" fuerza={1.05} />
    <Marco f="1x1" variante="hueco" />
    <LogoArriba f="1x1" />
    <Cuerpo f="1x1" alinear="abajo">
      <Etiqueta>18 y 19 de septiembre</Etiqueta>
      <Espacio h={24} />
      <Ligera size={66} caps>
        ¡Felices
      </Ligera>
      <Remate size={88}>Fiestas Patrias!</Remate>
      <Espacio h={30} />
      <Ligera size={36} color="rgba(255,255,255,0.92)" lh={1.28}>
        Que estos días estén llenos de buenos momentos,
        <br />
        tradiciones y encuentros junto a quienes más quieres.
      </Ligera>
      <Espacio h={18} />
      <Ligera size={33} color="rgba(255,255,255,0.74)">
        Con cariño, Tierra Calma.
      </Ligera>
    </Cuerpo>
  </Lienzo>
);

// -----------------------------------------------------------------------------
// E5 · 21/09 · Post 4:5 · "Dos formas de vivir el día" · Pilar 4
// Partido en dos: la misma parcela a las 7 y a las 19. Layout propio.
// -----------------------------------------------------------------------------
const E5: React.FC = () => {
  const z = ZONAS["4x5"];
  const mitad = z.h / 2;
  return (
    <Lienzo f="4x5">
      {/* mitad superior — la mañana */}
      <div style={{position: "absolute", left: 0, right: 0, top: 0, height: mitad, overflow: "hidden"}}>
        <Img src={staticFile(IA("e5_manana"))} style={{width: z.w, height: z.h, objectFit: "cover", objectPosition: "50% 40%"}} />
        {/* La mañana es una imagen alta en clave: sin este refuerzo + velo, el
            logo blanco y el marco desaparecían contra el cielo. */}
        <div
          style={{
            position: "absolute",
            inset: 0,
            background:
              "linear-gradient(180deg, rgba(10,16,12,0.78) 0%, rgba(10,16,12,0.34) 38%, rgba(10,16,12,0.58) 100%), linear-gradient(0deg, rgba(10,16,12,0.14), rgba(10,16,12,0.14))",
          }}
        />
      </div>
      {/* mitad inferior — la tarde */}
      <div style={{position: "absolute", left: 0, right: 0, top: mitad, height: mitad, overflow: "hidden"}}>
        <Img
          src={staticFile(IA("e5_tarde"))}
          style={{width: z.w, height: z.h, objectFit: "cover", objectPosition: "50% 58%", position: "absolute", top: -mitad}}
        />
        <div
          style={{
            position: "absolute",
            inset: 0,
            background:
              "linear-gradient(0deg, rgba(10,16,12,0.72) 0%, rgba(10,16,12,0.18) 40%, rgba(10,16,12,0.5) 100%), linear-gradient(0deg, rgba(10,16,12,0.13), rgba(10,16,12,0.13))",
          }}
        />
      </div>
      <div style={{position: "absolute", left: 0, right: 0, top: mitad, height: 1.4, background: "rgba(255,255,255,0.75)"}} />

      <Marco f="4x5" variante="hueco" op={0.6} />
      <LogoArriba f="4x5" />

      <div style={{position: "absolute", left: z.margen, right: z.margen, top: mitad - 250, height: 210, display: "flex", flexDirection: "column", justifyContent: "flex-end"}}>
        <Etiqueta size={24}>07:30 · la mañana</Etiqueta>
        <Espacio h={20} />
        <Ligera size={62} lh={1.12}>
          No siempre eliges
          <br />
          cómo empieza el día.
        </Ligera>
      </div>

      <div style={{position: "absolute", left: z.margen, right: z.margen, top: mitad + 62, height: 250}}>
        <Etiqueta size={24}>19:30 · la tarde</Etiqueta>
        <Espacio h={20} />
        <Remate size={82} caps={false}>
          Pero sí cómo
          <br />
          quieres terminarlo.
        </Remate>
      </div>

      <ZonaPildora f="4x5">
        <Pildora icono="pin" texto="Parcelas en Padre Hurtado · UF 2.500" />
      </ZonaPildora>
    </Lienzo>
  );
};

// -----------------------------------------------------------------------------
// E6 · 29/09 · Post 4:5 · "¿Buscas dónde invertir?" · Pilar 3
// Sin la cifra del 2,8%: no está validada (alerta 2.4 de la grilla).
// -----------------------------------------------------------------------------
const E6: React.FC = () => (
  <Lienzo f="4x5">
    <Foto src={IA("e6_inversion")} foco="50% 50%" />
    <Degradado tipo="ambos" fuerza={1.08} />
    <Marco f="4x5" variante="hueco" />
    <LogoArriba f="4x5" />
    <Cuerpo f="4x5">
      {/* A 72 la línea sans no cabía y se quebraba en dos, rompiendo la pareja
          tipográfica (una sans + el remate serif). */}
      <Ligera size={58} caps>
        ¿Buscas dónde invertir?
      </Ligera>
      <Remate size={96}>
        Invierte en
        <br />
        tu futuro.
      </Remate>
      <Filete ancho={120} margen={42} />
      <Ligera size={38} color="rgba(255,255,255,0.9)" lh={1.28}>
        Una parcela no depende del mercado del arriendo:
        <br />
        gana valor con el desarrollo de su propio entorno.
        <br />
        Y mientras tanto, la usas.
      </Ligera>
    </Cuerpo>
    <ZonaPildora f="4x5">
      {/* Ícono de ficha, no el pin: la píldora lleva datos de superficie y
          precio, no una ubicación. */}
      <Pildora icono="regla" texto="~5.000 m² · desde UF 2.500" />
    </ZonaPildora>
  </Lienzo>
);

// -----------------------------------------------------------------------------
// HISTORIAS 9:16
// -----------------------------------------------------------------------------
type STProps = {anim?: boolean; dur?: number};
const KB: [number, number] = [1.16, 1.02];

export const H1: React.FC<STProps> = ({anim, dur = 180}) => (
  <Lienzo f="9x16">
    <Foto src={IA("h1_primavera")} kb={anim ? KB : undefined} kbDur={dur} foco="50% 48%" />
    <Degradado tipo="ambos" />
    <Marco f="9x16" variante="hueco" />
    <LogoArriba f="9x16" />
    <Cuerpo f="9x16" alinear="abajo">
      <Entrada activo={anim} delay={6}>
      <Etiqueta>Padre Hurtado · septiembre</Etiqueta>
      <Espacio h={26} />
      <Ligera size={78} caps>
        La primavera
      </Ligera>
      <Remate size={98}>ya se siente.</Remate>
      <Espacio h={28} />
      <Ligera size={40} color="rgba(255,255,255,0.9)" lh={1.24}>
        Más verde, más luz, más ganas
        <br />
        de estar afuera.
      </Ligera>
    </Entrada>
    </Cuerpo>
    <ZonaPildora f="9x16">
      <Pildora icono="whatsapp" texto="Coordina tu visita" />
    </ZonaPildora>
  </Lienzo>
);

// H2 · qué incluye tu parcela. Solo datos de la lista blanca: se sacó
// "conexión a agua potable" (el agua es por noria del propietario) y no se
// listan rol individual ni cierre perimetral hasta que Fran los valide.
export const H2: React.FC<STProps> = ({anim, dur = 180}) => (
  <Lienzo f="9x16">
    <Foto src={IA("h2_incluye")} kb={anim ? KB : undefined} kbDur={dur} foco="50% 50%" />
    <Lavado op={0.9} />
    <Marco f="9x16" variante="bandas" op={0.5} />
    <Cuerpo f="9x16" alinear="centro" centrado>
      <Entrada activo={anim} delay={6}>
      <CirculoIcono id="regla" d={352} />
      <Espacio h={68} />
      <Fuerte size={66}>Qué incluye tu parcela</Fuerte>
      <Espacio h={44} />
      {[
        ["~5.000 m²", "de superficie por parcela"],
        ["Canchas de fútbol y pádel", "dentro del proyecto"],
        ["Colegios, super y bancos", "a minutos"],
      ].map(([t, s], i) => (
        <div key={t} style={{width: "100%", padding: "26px 0", borderTop: i === 0 ? "none" : "1px solid rgba(255,255,255,0.24)"}}>
          <div style={{fontFamily: TC.fonts.display, fontSize: 58, fontWeight: 400, color: "#FFFFFF", lineHeight: 1.06, letterSpacing: "-0.02em"}}>
            {t}
          </div>
          <div style={{fontFamily: SANS, fontSize: 27, fontWeight: 400, letterSpacing: "0.14em", textTransform: "uppercase", color: TC.colors.sand, marginTop: 12}}>
            {s}
          </div>
        </div>
      ))}
    </Entrada>
    </Cuerpo>
    <ZonaPildora f="9x16">
      <Pildora icono="whatsapp" texto="Te enviamos la ficha completa" />
    </ZonaPildora>
  </Lienzo>
);

export const H4: React.FC<STProps> = ({anim, dur = 180}) => (
  <Lienzo f="9x16">
    <Foto src={IA("h4_epoca")} kb={anim ? KB : undefined} kbDur={dur} foco="50% 54%" />
    <Degradado tipo="ambos" />
    <Marco f="9x16" variante="hueco" />
    <LogoArriba f="9x16" />
    <Cuerpo f="9x16" alinear="abajo">
      <Entrada activo={anim} delay={6}>
      <Etiqueta>~5.000 m² · desde UF 2.500</Etiqueta>
      <Espacio h={26} />
      <Ligera size={78} caps>
        Cualquier época
      </Ligera>
      <Remate size={98}>del año.</Remate>
      <Espacio h={28} />
      <Ligera size={40} color="rgba(255,255,255,0.9)" lh={1.24}>
        A 30 minutos de Santiago,
        <br />
        todo el año.
      </Ligera>
    </Entrada>
    </Cuerpo>
    <ZonaPildora f="9x16">
      <Pildora icono="whatsapp" texto="Agenda tu visita" />
    </ZonaPildora>
  </Lienzo>
);

// -----------------------------------------------------------------------------
// Contenedores de render: un frame = una pieza.
// -----------------------------------------------------------------------------
const Hoja: React.FC<{piezas: {id: string; C: React.FC}[]}> = ({piezas}) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{background: "#000"}}>
      {piezas.map(({id, C}, i) => (
        <Sequence key={id} from={i} durationInFrames={1} layout="none">
          {frame === i ? <C /> : null}
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};

// El `id` es el nombre de archivo de la entrega y lo lee scripts/tc-entrega.sh
// directamente de acá, para que el código y el nombre no se desincronicen.
// Nomenclatura heredada de julio y agosto: c- carrusel, p- post, st- historia.
type Pieza = {id: string; C: React.FC};

export const PIEZAS_4x5: Pieza[] = [
  {id: "c-01-09-1", C: E1s1},
  {id: "c-01-09-2", C: E1s2},
  {id: "c-01-09-3", C: E1s3},
  {id: "c-01-09-4", C: E1s4},
  {id: "c-04-09-1", C: E2s1},
  {id: "c-04-09-2", C: E2s2},
  {id: "c-04-09-3", C: E2s3},
  {id: "c-04-09-4", C: E2s4},
  {id: "p-08-09", C: E3},
  {id: "p-21-09", C: E5},
  {id: "p-29-09", C: E6},
];
export const PIEZAS_1x1: Pieza[] = [{id: "p-18-09", C: E4}];
export const PIEZAS_9x16: Pieza[] = [
  {id: "st-03-09", C: H1},
  {id: "st-10-09", C: H2},
  {id: "st-24-09", C: H4},
];

export const Piezas4x5: React.FC = () => <Hoja piezas={PIEZAS_4x5} />;
export const Piezas1x1: React.FC = () => <Hoja piezas={PIEZAS_1x1} />;
export const Piezas9x16: React.FC = () => <Hoja piezas={PIEZAS_9x16} />;
