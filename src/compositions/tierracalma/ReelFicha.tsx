import React from "react";
import {AbsoluteFill, Audio, interpolate, Sequence, staticFile, useCurrentFrame} from "remotion";
import {
  BandScrim,
  BigFigure,
  Body,
  Clip,
  FADE,
  Grade,
  Grain,
  Headline,
  Inner,
  Kicker,
  LogoOutro,
  Reveal,
  Rule,
  SafeBlock,
  Scene,
  SANS,
  TC,
} from "./kit";

// =============================================================================
// TIERRA CALMA · REEL 02 SEPTIEMBRE — "Lo que ya viene resuelto"
// Pilar 3 · Inversión & Plusvalía. Publicación: 15-09-2026.
//
// POR QUÉ ESTA PIEZA: la duda más repetida en los comentarios de la pauta es
// "más información". Esto es la ficha del proyecto en video, con la cifra como
// elemento más grande de cada plano — la misma regla del brief de pauta
// ("las piezas con cifra concreta cuestan 4,5× menos que las que hablan de
// privacidad, naturaleza y comunidad"), llevada al orgánico.
//
// SOLO DATOS DE LA LISTA BLANCA (src/brand/tierracalma.ts → claims). Nada de
// rol individual, cierres perimetrales ni factibilidad de agua sin validar.
//
// MATERIAL PROPIO del rodaje con dron del 07-08-2026. Cierra en la PLACA del
// acceso — el remate más honesto que tiene la marca: el proyecto construido.
// 9:16 · 30 fps · ~27 s.
// =============================================================================

const CUTS = {
  hook: {from: 0, dur: 100},
  metros: {from: 100, dur: 115},
  precio: {from: 215, dur: 115},
  tiempos: {from: 330, dur: 120},
  entorno: {from: 450, dur: 140},
  cta: {from: 590, dur: 110},
  logo: {from: 700, dur: 100},
};

export const REEL_FICHA_DURATION = CUTS.logo.from + CUTS.logo.dur; // 800 = 26,7 s

// ---------------------------------------------------------------------------
const Hook: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_niebla.mp4" dur={CUTS.hook.dur + FADE} zoom={[1.1, 1.0]} />
    <Grade />
    <BandScrim from={30} to={78} strength={0.4} />
    <Grain id="tcf-g1" />
    <Inner>
      <SafeBlock top={660}>
        <Reveal delay={8}>
          <Kicker>Padre Hurtado · Región Metropolitana</Kicker>
        </Reveal>
        <Reveal delay={16}>
          <Headline size={86} weight={400}>
            Antes de enamorarte
            <br />
            del paisaje,
            <br />
            <span style={{fontStyle: "italic", fontWeight: 500}}>pregunta lo aburrido.</span>
          </Headline>
        </Reveal>
      </SafeBlock>
    </Inner>
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
const Metros: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_loteo.mp4" dur={CUTS.metros.dur + FADE} zoom={[1.0, 1.09]} />
    <Grade strength={1.15} />
    <BandScrim />
    <Grain id="tcf-g2" />
    <Inner>
      <BigFigure kicker="Superficie" figure={<>~5.000 m²</>} label="por parcela" size={150} />
    </Inner>
  </AbsoluteFill>
);

const Precio: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_loteo_caminos.mp4" dur={CUTS.precio.dur + FADE} zoom={[1.08, 1.0]} pan={[26, 0]} />
    <Grade strength={1.15} />
    <BandScrim />
    <Grain id="tcf-g3" />
    <Inner>
      <BigFigure
        kicker="Valor"
        figure={
          <>
            desde
            <br />
            UF 2.500
          </>
        }
        size={140}
      />
    </Inner>
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
// Dos tiempos en la misma cartela: el dato que mata el miedo a "quedar lejos".
const Tiempos: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_llano.mp4" dur={CUTS.tiempos.dur + FADE} zoom={[1.0, 1.1]} />
    <Grade strength={1.2} />
    <BandScrim from={30} to={82} strength={0.5} />
    <Grain id="tcf-g4" />
    <Inner>
      <SafeBlock top={700} align="center">
        <Reveal delay={6}>
          <Kicker align="center">Distancias</Kicker>
        </Reveal>
        <Reveal delay={14}>
          <Headline size={132} weight={400} align="center" lh={1} tracking="-0.035em">
            30 min
          </Headline>
        </Reveal>
        <Reveal delay={22}>
          <Body size={32} align="center">
            de Santiago
          </Body>
        </Reveal>
        <Reveal delay={44}>
          <Rule width={110} align="center" />
        </Reveal>
        <Reveal delay={52}>
          <Headline size={132} weight={400} align="center" lh={1} tracking="-0.035em">
            15 min
          </Headline>
        </Reveal>
        <Reveal delay={60}>
          <Body size={32} align="center">
            del peaje Padre Hurtado
          </Body>
        </Reveal>
      </SafeBlock>
    </Inner>
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
// Entorno y equipamiento. Van juntos a propósito: son los dos datos aprobados
// que responden "¿y qué hay alrededor?" sin prometer nada por validar.
const Entorno: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_casas_verde2.mp4" dur={CUTS.entorno.dur + FADE} zoom={[1.12, 1.0]} pan={[-30, 0]} />
    <Grade strength={1.25} />
    <BandScrim from={28} to={86} strength={0.48} />
    <Grain id="tcf-g5" />
    <Inner>
      <SafeBlock top={620}>
        <Reveal delay={6}>
          <Kicker>Alrededor</Kicker>
        </Reveal>
      </SafeBlock>
      <div style={{position: "absolute", left: 84, right: 84, top: 780}}>
        {[
          ["Colegios, supermercado y bancos", "a minutos"],
          ["Canchas de fútbol y pádel", "dentro del proyecto"],
        ].map(([t, s], i) => (
          <Reveal key={t} delay={18 + i * 22} from={30}>
            <div style={{padding: "34px 0", borderTop: i === 0 ? "none" : "1px solid rgba(255,255,255,0.22)"}}>
              <div
                style={{
                  fontFamily: TC.fonts.display,
                  fontSize: 62,
                  fontWeight: 400,
                  color: "#FFFFFF",
                  lineHeight: 1.06,
                  letterSpacing: "-0.02em",
                  textShadow: "0 3px 34px rgba(0,0,0,0.55)",
                }}
              >
                {t}
              </div>
              <div
                style={{
                  fontFamily: SANS,
                  fontSize: 27,
                  fontWeight: 400,
                  letterSpacing: "0.16em",
                  textTransform: "uppercase",
                  color: TC.colors.sand,
                  marginTop: 14,
                }}
              >
                {s}
              </div>
            </div>
          </Reveal>
        ))}
      </div>
    </Inner>
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
const Cta: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_acceso_placa.mp4" dur={CUTS.cta.dur + FADE} zoom={[1.28, 1.05]} pan={[0, -170]} />
    <Grade strength={1.2} />
    <AbsoluteFill
      style={{
        background: "linear-gradient(180deg, transparent 26%, rgba(6,12,18,0.5) 44%, rgba(6,12,18,0.5) 64%, transparent 82%)",
        pointerEvents: "none",
      }}
    />
    <Grain id="tcf-g6" />
    <Inner>
      <SafeBlock top={740} align="center">
        <Reveal delay={4}>
          <Kicker size={25} align="center" color="rgba(255,255,255,0.8)">
            Lo demás te lo mandamos por escrito
          </Kicker>
        </Reveal>
        <Reveal delay={14}>
          <Headline size={90} weight={400} align="center" lh={1.06}>
            Escríbenos y te
            <br />
            enviamos <span style={{fontStyle: "italic", fontWeight: 500}}>la ficha</span>
          </Headline>
        </Reveal>
        <Reveal delay={38}>
          <Rule width={130} align="center" />
        </Reveal>
        <Reveal delay={46}>
          <Body size={31} align="center" color="rgba(255,255,255,0.86)">
            WhatsApp en el perfil.
          </Body>
        </Reveal>
      </SafeBlock>
    </Inner>
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
// Música: «Valley Sunset» (Mixkit, libre). Una pista distinta por reel, mismo registro.
const Musica: React.FC = () => {
  const frame = useCurrentFrame();
  const total = REEL_FICHA_DURATION;
  const v = Math.min(
    interpolate(frame, [0, 30], [0, 1], {extrapolateRight: "clamp"}),
    interpolate(frame, [total - 70, total - 10], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}),
  );
  return <Audio src={staticFile(TC.music.valleySunset)} volume={v * 0.62} loop />;
};

export const ReelFicha: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <Musica />
    <Scene cut={CUTS.hook}>
      <Hook />
    </Scene>
    <Scene cut={CUTS.metros}>
      <Metros />
    </Scene>
    <Scene cut={CUTS.precio}>
      <Precio />
    </Scene>
    <Scene cut={CUTS.tiempos}>
      <Tiempos />
    </Scene>
    <Scene cut={CUTS.entorno}>
      <Entorno />
    </Scene>
    <Scene cut={CUTS.cta}>
      <Cta />
    </Scene>
    <Sequence from={CUTS.logo.from} durationInFrames={CUTS.logo.dur}>
      <LogoOutro dur={CUTS.logo.dur} />
    </Sequence>
  </AbsoluteFill>
);
