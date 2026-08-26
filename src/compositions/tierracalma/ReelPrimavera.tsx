import React from "react";
import {AbsoluteFill, Audio, interpolate, Sequence, staticFile, useCurrentFrame} from "remotion";
import {BandScrim, Body, Clip, FADE, Grade, Grain, Headline, Inner, Kicker, LogoOutro, Reveal, Rule, SafeBlock, Scene, TC} from "./kit";

// =============================================================================
// TIERRA CALMA · REEL 04 SEPTIEMBRE — "Primavera en Tierra Calma"
// Pilar 4 · Naturaleza & Bienestar. Publicación: 25-09-2026 (primavera parte el 21).
//
// Es el respiro del mes: corto, atmosférico, sin dato duro. La escena 3 va SIN
// TEXTO a propósito — feedback de Constanza: no saturar de tipografía, dejar
// que el paisaje respire.
// 9:16 · 30 fps · ~21 s.
// =============================================================================

const CUTS = {
  estacion: {from: 0, dur: 110},
  campo: {from: 110, dur: 110},
  respiro: {from: 220, dur: 100},
  primavera: {from: 320, dur: 110},
  cta: {from: 430, dur: 90},
  logo: {from: 520, dur: 100},
};

export const REEL_PRIMAVERA_DURATION = CUTS.logo.from + CUTS.logo.dur; // 620 = 20,7 s

const Estacion: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_niebla.mp4" dur={CUTS.estacion.dur + FADE} zoom={[1.12, 1.0]} pan={[24, 0]} />
    <Grade />
    <Grain id="tcp-g1" />
    <Inner>
      <SafeBlock top={700}>
        <Reveal delay={10}>
          <Headline size={92} weight={400}>
            Se nota cuando
            <br />
            cambia la estación.
          </Headline>
        </Reveal>
      </SafeBlock>
    </Inner>
  </AbsoluteFill>
);

const Campo: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_valle_verde.mp4" dur={CUTS.campo.dur + FADE} zoom={[1.0, 1.1]} pan={[-34, 0]} />
    <Grade />
    <Grain id="tcp-g2" />
    <Inner>
      <SafeBlock top={760}>
        <Reveal delay={10}>
          <Headline size={104} weight={500} italic lh={1.02}>
            El campo
            <br />
            despierta primero.
          </Headline>
        </Reveal>
      </SafeBlock>
    </Inner>
  </AbsoluteFill>
);

// Escena sin texto — a propósito.
const Respiro: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_valle_ancho.mp4" dur={CUTS.respiro.dur + FADE} zoom={[1.1, 1.0]} pan={[30, 0]} />
    <Grade strength={0.7} />
    <Grain id="tcp-g3" />
  </AbsoluteFill>
);

const Primavera: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_casas_verde.mp4" dur={CUTS.primavera.dur + FADE} zoom={[1.0, 1.09]} />
    <Grade strength={1.15} />
    <BandScrim from={32} to={80} strength={0.44} />
    <Grain id="tcp-g4" />
    <Inner>
      <SafeBlock top={740} align="center">
        <Reveal delay={8}>
          <Kicker align="center">Primavera en</Kicker>
        </Reveal>
        <Reveal delay={16}>
          <Headline size={116} weight={400} align="center" lh={1.02} tracking="-0.03em">
            Padre Hurtado
          </Headline>
        </Reveal>
      </SafeBlock>
    </Inner>
  </AbsoluteFill>
);

const Cta: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_porteria_frontal.mp4" dur={CUTS.cta.dur + FADE} zoom={[1.08, 1.0]} />
    <Grade strength={1.2} />
    <AbsoluteFill
      style={{
        background: "linear-gradient(180deg, transparent 42%, rgba(6,12,18,0.42) 58%, rgba(6,12,18,0.42) 82%, transparent 96%)",
        pointerEvents: "none",
      }}
    />
    <Grain id="tcp-g5" />
    <Inner>
      <SafeBlock top={1090} align="center">
        <Reveal delay={6}>
          <Headline size={98} weight={400} align="center" lh={1.04}>
            Ven a <span style={{fontStyle: "italic", fontWeight: 500}}>conocerla.</span>
          </Headline>
        </Reveal>
        <Reveal delay={26}>
          <Rule width={120} align="center" />
        </Reveal>
        <Reveal delay={34}>
          <Body size={31} align="center" color="rgba(255,255,255,0.86)">
            Escríbenos al WhatsApp del perfil.
          </Body>
        </Reveal>
      </SafeBlock>
    </Inner>
  </AbsoluteFill>
);

// Música: «Vastness» (Mixkit, libre). Una pista distinta por reel, mismo registro.
const Musica: React.FC = () => {
  const frame = useCurrentFrame();
  const total = REEL_PRIMAVERA_DURATION;
  const v = Math.min(
    interpolate(frame, [0, 30], [0, 1], {extrapolateRight: "clamp"}),
    interpolate(frame, [total - 70, total - 10], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}),
  );
  return <Audio src={staticFile(TC.music.vastness)} volume={v * 0.62} loop />;
};

export const ReelPrimavera: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <Musica />
    <Scene cut={CUTS.estacion}>
      <Estacion />
    </Scene>
    <Scene cut={CUTS.campo}>
      <Campo />
    </Scene>
    <Scene cut={CUTS.respiro}>
      <Respiro />
    </Scene>
    <Scene cut={CUTS.primavera}>
      <Primavera />
    </Scene>
    <Scene cut={CUTS.cta}>
      <Cta />
    </Scene>
    <Sequence from={CUTS.logo.from} durationInFrames={CUTS.logo.dur}>
      <LogoOutro dur={CUTS.logo.dur} />
    </Sequence>
  </AbsoluteFill>
);
