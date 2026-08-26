import React from "react";
import {AbsoluteFill, Audio, interpolate, Sequence, staticFile, useCurrentFrame} from "remotion";
import {
  BandScrim,
  Clip,
  ClipFoto,
  FADE,
  Grade,
  Grain,
  Headline,
  Inner,
  Kicker,
  LogoOutro,
  Reveal,
  SafeBlock,
  Scene,
  TC,
} from "./kit";

// =============================================================================
// TIERRA CALMA · REEL 03 SEPTIEMBRE — "Hay celebraciones que merecen más espacio"
// Pilar 1 · Calidad de vida. Publicación: 17-09-2026.
//
// No vende el 18: siembra el próximo. Es la decisión del brief y se respeta.
//
// CÓMO SE DESTRABÓ. El corte 2 pedía "mesa larga montada en la parcela", una
// toma que el rodaje del 07-08 no tiene. La grilla dejaba la pieza bloqueada
// esperando material. Se resolvió con IA —exactamente lo que hizo el diseñador
// en agosto con la pieza del quincho (c-10-08-2)— y se anima con Ken Burns.
// El zoom de los planos fijos va hacia AFUERA o muy lento: un push-in rápido
// sobre una foto se nota al tiro.
//
// Mezcla deliberada: los aéreos son metraje propio (evidencia), la escena de
// sobremesa es IA (la promesa). 9:16 · 30 fps · ~22 s.
// =============================================================================

const CUTS = {
  hook: {from: 0, dur: 118},
  mesa: {from: 118, dur: 130},
  asado: {from: 248, dur: 96},
  amplitud: {from: 344, dur: 118},
  cierre: {from: 462, dur: 130},
  logo: {from: 592, dur: 96},
};

export const REEL_CELEBRACION_DURATION = CUTS.logo.from + CUTS.logo.dur; // 688 = 22,9 s

// ---------------------------------------------------------------------------
const Hook: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_valle_amplio.mp4" dur={CUTS.hook.dur + FADE} zoom={[1.04, 1.14]} />
    <Grade calido={2.6} />
    <BandScrim from={28} to={80} strength={0.44} />
    <Grain id="tcc-g1" />
    <Inner>
      <SafeBlock top={660}>
        <Reveal delay={8}>
          <Kicker>Padre Hurtado · Región Metropolitana</Kicker>
        </Reveal>
        <Reveal delay={16}>
          <Headline size={88} weight={400}>
            Hay celebraciones
            <br />
            que simplemente
            <br />
            <span style={{fontStyle: "italic", fontWeight: 500}}>necesitan más espacio.</span>
          </Headline>
        </Reveal>
      </SafeBlock>
    </Inner>
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
const Mesa: React.FC = () => (
  <AbsoluteFill>
    <ClipFoto src="assets/tierracalma/ia/r3_mesa.png" dur={CUTS.mesa.dur + FADE} zoom={[1.18, 1.05]} foco="50% 58%" />
    <Grade strength={0.9} />
    <BandScrim from={26} to={72} strength={0.42} />
    <Grain id="tcc-g2" />
    <Inner>
      <SafeBlock top={640}>
        <Reveal delay={10}>
          <Headline size={82} weight={400}>
            Donde la conversación
            <br />
            <span style={{fontStyle: "italic", fontWeight: 500}}>dura horas.</span>
          </Headline>
        </Reveal>
        <Reveal delay={44}>
          <Headline size={82} weight={400}>
            Y nadie mira el reloj.
          </Headline>
        </Reveal>
      </SafeBlock>
    </Inner>
  </AbsoluteFill>
);

// Respiro sin texto: es feedback de Constanza — no saturar de tipografía.
const Asado: React.FC = () => (
  <AbsoluteFill>
    <ClipFoto src="assets/tierracalma/ia/r3_asado.png" dur={CUTS.asado.dur + FADE} zoom={[1.2, 1.06]} foco="50% 64%" />
    <Grade strength={0.85} />
    <Grain id="tcc-g3" />
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
const Amplitud: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_llano.mp4" dur={CUTS.amplitud.dur + FADE} zoom={[1.14, 1.0]} />
    <Grade strength={1.05} calido={2.6} />
    <BandScrim from={30} to={82} strength={0.46} />
    <Grain id="tcc-g4" />
    <Inner>
      <SafeBlock top={720} align="center">
        <Reveal delay={8}>
          <Headline size={80} weight={400} align="center" lh={1.14}>
            Más espacio.
            <br />
            Más tranquilidad.
            <br />
            <span style={{fontStyle: "italic", fontWeight: 500}}>Más momentos para compartir.</span>
          </Headline>
        </Reveal>
      </SafeBlock>
    </Inner>
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
const Cierre: React.FC = () => (
  <AbsoluteFill>
    <ClipFoto src="assets/tierracalma/ia/r3_amplio.png" dur={CUTS.cierre.dur + FADE} zoom={[1.14, 1.02]} foco="50% 46%" />
    <Grade strength={1.0} />
    <BandScrim from={30} to={84} strength={0.48} />
    <Grain id="tcc-g5" />
    <Inner>
      <SafeBlock top={700} align="center">
        <Reveal delay={6}>
          <Kicker size={25} align="center" color="rgba(255,255,255,0.82)">
            Este 18
          </Kicker>
        </Reveal>
        <Reveal delay={14}>
          <Headline size={82} weight={400} align="center" lh={1.1}>
            Empieza a imaginar
            <br />
            cómo podrían ser
            <br />
            <span style={{fontStyle: "italic", fontWeight: 500}}>tus próximas celebraciones.</span>
          </Headline>
        </Reveal>
      </SafeBlock>
    </Inner>
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
// Música: «Sweet September» (Mixkit, libre) — la cuarta pista, para que el mes
// no suene repetido. Es pedido explícito de Valeria.
const Musica: React.FC = () => {
  const frame = useCurrentFrame();
  const total = REEL_CELEBRACION_DURATION;
  const v = Math.min(
    interpolate(frame, [0, 30], [0, 1], {extrapolateRight: "clamp"}),
    interpolate(frame, [total - 70, total - 10], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}),
  );
  return <Audio src={staticFile(TC.music.sweetSeptember)} volume={v * 0.62} loop />;
};

export const ReelCelebracion: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <Musica />
    <Scene cut={CUTS.hook}>
      <Hook />
    </Scene>
    <Scene cut={CUTS.mesa}>
      <Mesa />
    </Scene>
    <Scene cut={CUTS.asado}>
      <Asado />
    </Scene>
    <Scene cut={CUTS.amplitud}>
      <Amplitud />
    </Scene>
    <Scene cut={CUTS.cierre}>
      <Cierre />
    </Scene>
    <Sequence from={CUTS.logo.from} durationInFrames={CUTS.logo.dur}>
      <LogoOutro dur={CUTS.logo.dur} />
    </Sequence>
  </AbsoluteFill>
);
