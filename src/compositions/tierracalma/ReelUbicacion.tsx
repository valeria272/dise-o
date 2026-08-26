import React from "react";
import {AbsoluteFill, Audio, interpolate, Sequence, staticFile, useCurrentFrame} from "remotion";
import {BandScrim, Body, Clip, FADE, Grade, Grain, Headline, Inner, Kicker, LogoOutro, Reveal, Rule, SafeBlock, Scene, TC, SANS} from "./kit";
import {Mapa, MAPA_PUNTOS} from "./Mapa";

// =============================================================================
// TIERRA CALMA · REEL 01 SEPTIEMBRE — "¿Dónde queda Tierra Calma?"
// Pilar 2 · Ubicación & Conectividad. Publicación: 09-09-2026.
//
// POR QUÉ ESTA PIEZA: en el informe de julio, las dos dudas que más se repiten
// en los comentarios son "más información" y "dónde queda / cómo llego", y las
// dos aparecen SOLO en los anuncios pagados. Este reel las contesta en orgánico.
//
// El mapa es un esquema editorial dibujado en SVG, no un mapa real: orienta sin
// revelar el pin exacto (requisito del brief) y no depende de assets externos.
//
// MATERIAL PROPIO del rodaje con dron del 07-08-2026 (nada de clips genéricos).
// El CTA cierra en la PORTERÍA real del proyecto: es la prueba de que existe.
// 9:16 · 30 fps · 30 s.
// =============================================================================

const CUTS = {
  hook: {from: 0, dur: 105},
  ruta: {from: 105, dur: 165},
  refer: {from: 270, dur: 108},
  cerca: {from: 378, dur: 192},
  conect: {from: 570, dur: 108},
  cta: {from: 678, dur: 120},
  logo: {from: 798, dur: 102},
};

export const REEL_UBICACION_DURATION = CUTS.logo.from + CUTS.logo.dur; // 900 = 30 s

// ---------------------------------------------------------------------------
// 1 · HOOK — aéreo real y la pregunta.
const Hook: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_valle_ancho.mp4" dur={CUTS.hook.dur + FADE} zoom={[1.12, 1.0]} pan={[30, 0]} />
    <Grade />
    <Grain id="tc-g1" />
    <Inner>
      <SafeBlock top={640}>
        <Reveal delay={8}>
          <Kicker>Padre Hurtado · Región Metropolitana</Kicker>
        </Reveal>
        <Reveal delay={16}>
          <Headline size={104} weight={400}>
            ¿Dónde queda
            <br />
            <span style={{fontStyle: "italic", fontWeight: 500}}>Tierra Calma</span>?
          </Headline>
        </Reveal>
        <Reveal delay={34}>
          <Rule />
        </Reveal>
        <Reveal delay={40}>
          <Body size={31}>Te damos algunas referencias para que puedas ubicarte.</Body>
        </Reveal>
      </SafeBlock>
    </Inner>
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
// 2 · CÓMO LLEGAR — el trazado se dibuja solo.
const Ruta: React.FC = () => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [2, FADE + 106], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const zoom = interpolate(frame, [0, CUTS.ruta.dur + FADE], [1.0, 1.09], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill>
      <Mapa progress={p} zoom={zoom} focus={{x: 560, y: 660}} show={{
          peaje: interpolate(p, [0.5, 0.72], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}),
          pueblo: interpolate(p, [0.86, 1], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}),
        }} />
      {/* scrim inferior en crema para que el texto no pelee con el trazado */}
      <AbsoluteFill
        style={{background: `linear-gradient(180deg, transparent 46%, ${TC.colors.cream} 62%, ${TC.colors.cream} 100%)`, pointerEvents: "none"}}
      />
      <Inner>
        <SafeBlock top={1236}>
          <Reveal delay={4}>
            <Kicker color={TC.colors.navy}>Cómo llegar</Kicker>
          </Reveal>
          <Reveal delay={12}>
            <Headline size={74} weight={400} color={TC.colors.navy}>
              Desde Santiago,
              <br />
              <span style={{fontStyle: "italic"}}>derecho al surponiente.</span>
            </Headline>
          </Reveal>
          <Reveal delay={54}>
            <Rule width={120} />
          </Reveal>
          <Reveal delay={62}>
            <Body size={32} color="rgba(11,44,73,0.82)">
              Autopista del Sol · Ruta 78
              <br />
              Salida Padre Hurtado
              <br />
              Camino G-68 · Cuesta Barriga
            </Body>
          </Reveal>
        </SafeBlock>
      </Inner>
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// 3 · LA REFERENCIA — el hito que dice "ya estás cerca".
const Referencia: React.FC = () => {
  const frame = useCurrentFrame();
  const zoom = interpolate(frame, [0, CUTS.refer.dur + FADE], [1.34, 1.52], {extrapolateRight: "clamp"});
  const conaf = interpolate(frame, [FADE + 14, FADE + 40], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill>
      <Mapa progress={1} zoom={zoom} focus={{x: 400, y: 1180}} show={{pueblo: 1, conaf}} showRuta={false} />
      <AbsoluteFill
        style={{background: `linear-gradient(180deg, ${TC.colors.cream} 0%, ${TC.colors.cream} 31%, transparent 42%)`, pointerEvents: "none"}}
      />
      <Inner>
        <SafeBlock top={318}>
          <Reveal delay={2}>
            <Kicker color={TC.colors.navy}>Una referencia clave</Kicker>
          </Reveal>
          <Reveal delay={10}>
            <Headline size={68} weight={400} color={TC.colors.navy}>
              Cuando veas la brigada
              <br />
              <span style={{fontStyle: "italic"}}>ya estás cerca.</span>
            </Headline>
          </Reveal>
        </SafeBlock>
      </Inner>
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// 4 · QUÉ TIENES CERCA — lista editorial con filetes, sin iconos ni emojis.
const ITEMS = ["Colegios", "Supermercado y comercio", "Bancos", "Centros médicos"];

const Cerca: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_casas_verde.mp4" dur={CUTS.cerca.dur + FADE} zoom={[1.0, 1.1]} pan={[-40, 0]} />
    <Grade strength={1.15} />
    <BandScrim from={22} to={92} strength={0.5} />
    <Grain id="tc-g4" />
    <Inner>
      <SafeBlock top={520}>
        <Reveal delay={6}>
          <Headline size={66} weight={400}>
            Porque vivir en una parcela
            <br />
            no significa vivir <span style={{fontStyle: "italic"}}>aislado.</span>
          </Headline>
        </Reveal>
      </SafeBlock>
      <div style={{position: "absolute", left: 84, right: 84, top: 900}}>
        {ITEMS.map((t, i) => (
          <Reveal key={t} delay={46 + i * 14} from={26}>
            <div
              style={{
                display: "flex",
                alignItems: "baseline",
                gap: 26,
                padding: "22px 0",
                borderTop: i === 0 ? "none" : "1px solid rgba(255,255,255,0.22)",
              }}
            >
              <span style={{fontFamily: SANS, fontSize: 20, letterSpacing: "0.2em", color: TC.colors.sand, minWidth: 44}}>
                {String(i + 1).padStart(2, "0")}
              </span>
              <span style={{fontFamily: TC.fonts.display, fontSize: 52, fontWeight: 400, color: "#FFFFFF", textShadow: "0 3px 30px rgba(0,0,0,0.5)"}}>
                {t}
              </span>
            </div>
          </Reveal>
        ))}
        <Reveal delay={112} from={22}>
          <div style={{marginTop: 26}}>
            <Body size={30} color="rgba(255,255,255,0.8)">
              Todo en el entorno de Padre Hurtado.
            </Body>
          </div>
        </Reveal>
      </div>
    </Inner>
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
// 5 · CONECTIVIDAD — el mapa se aleja y muestra la relación completa.
const Conectividad: React.FC = () => {
  const frame = useCurrentFrame();
  const zoom = interpolate(frame, [0, CUTS.conect.dur + FADE], [1.5, 1.02], {extrapolateRight: "clamp"});
  const focus = {
    x: interpolate(frame, [0, CUTS.conect.dur + FADE], [400, MAPA_PUNTOS.P_PUEBLO.x + 100], {extrapolateRight: "clamp"}),
    y: interpolate(frame, [0, CUTS.conect.dur + FADE], [1180, 1000], {extrapolateRight: "clamp"}),
  };
  return (
    <AbsoluteFill>
      <Mapa progress={1} zoom={zoom} showRuta={false} focus={focus} show={{peaje: 1, pueblo: 1, tc: interpolate(frame, [FADE + 6, FADE + 30], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})}} />
      <AbsoluteFill
        style={{background: `linear-gradient(180deg, ${TC.colors.cream} 0%, ${TC.colors.cream} 33%, transparent 44%)`, pointerEvents: "none"}}
      />
      <Inner>
        <SafeBlock top={300}>
          <Reveal delay={6}>
            <Headline size={70} weight={400} color={TC.colors.navy}>
              Tranquilidad cuando llegas.
              <br />
              <span style={{fontStyle: "italic"}}>Conectividad</span> cuando la necesitas.
            </Headline>
          </Reveal>
          <Reveal delay={30}>
            <Kicker color={TC.colors.navy} size={22}>
              Padre Hurtado · Región Metropolitana
            </Kicker>
          </Reveal>
        </SafeBlock>
      </Inner>
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------
// 6 · CTA — vuelve el paisaje real y se pide el comentario.
const Cta: React.FC = () => (
  <AbsoluteFill>
    <Clip src="assets/tierracalma/drone/tc_porteria.mp4" dur={CUTS.cta.dur + FADE} zoom={[1.06, 1.0]} />
    <Grade strength={0.55} />
    {/* Plano ya oscuro (portería con lluvia): apenas un velo para asentar el texto. */}
    <AbsoluteFill
      style={{
        background: "linear-gradient(180deg, transparent 22%, rgba(6,12,18,0.3) 40%, rgba(6,12,18,0.3) 66%, transparent 86%)",
        pointerEvents: "none",
      }}
    />
    <Grain id="tc-g6" />
    <Inner>
      <SafeBlock top={700} align="center">
        <Reveal delay={4}>
          <Kicker size={25} align="center" color="rgba(255,255,255,0.8)">
            ¿Quieres conocer la ubicación exacta?
          </Kicker>
        </Reveal>
        <Reveal delay={14}>
          <Headline size={92} weight={400} align="center" lh={1.06}>
            Comenta
            <br />
            <span style={{fontStyle: "italic", fontWeight: 500}}>«UBICACIÓN»</span>
          </Headline>
        </Reveal>
        <Reveal delay={38}>
          <Rule width={130} align="center" />
        </Reveal>
        <Reveal delay={46}>
          <Body size={31} align="center" color="rgba(255,255,255,0.86)">
            y te enviamos la ruta para que puedas conocer Tierra Calma.
          </Body>
        </Reveal>
      </SafeBlock>
      <div style={{position: "absolute", left: 84, right: 84, top: 1420, textAlign: "center"}}>
        <Reveal delay={58}>
          <Kicker size={23} align="center" color="rgba(255,255,255,0.72)">
            5.000 m² · desde UF 2.500 · 30 min de Santiago
          </Kicker>
        </Reveal>
      </div>
    </Inner>
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
// Música: «Serene View» (Mixkit, libre). Cada reel del mes lleva una pista distinta
// dentro del mismo registro de calma — el mes no puede sonar repetido.
const Musica: React.FC = () => {
  const frame = useCurrentFrame();
  const total = REEL_UBICACION_DURATION;
  const v = Math.min(
    interpolate(frame, [0, 30], [0, 1], {extrapolateRight: "clamp"}),
    interpolate(frame, [total - 70, total - 10], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}),
  );
  return <Audio src={staticFile(TC.music.sereneView)} volume={v * 0.62} loop />;
};

export const ReelUbicacion: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <Musica />
    <Scene cut={CUTS.hook}>
      <Hook />
    </Scene>
    <Scene cut={CUTS.ruta}>
      <Ruta />
    </Scene>
    <Scene cut={CUTS.refer}>
      <Referencia />
    </Scene>
    <Scene cut={CUTS.cerca}>
      <Cerca />
    </Scene>
    <Scene cut={CUTS.conect}>
      <Conectividad />
    </Scene>
    <Scene cut={CUTS.cta}>
      <Cta />
    </Scene>
    <Sequence from={CUTS.logo.from} durationInFrames={CUTS.logo.dur}>
      <LogoOutro dur={CUTS.logo.dur} />
    </Sequence>
  </AbsoluteFill>
);
