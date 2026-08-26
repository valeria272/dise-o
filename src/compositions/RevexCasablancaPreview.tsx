import React from "react";
import {AbsoluteFill} from "remotion";
import {SafeAreaAds, SAFE_ZONES} from "../components/qa/SafeAreaAds";
import {
  FondoRevex,
  LogoBlockRevex,
  GanchoScriptRevex,
  TitularRevex,
  BulletLineRevex,
  DatoBoxRevex,
  CuerpoRevex,
  CtaRevex,
  BanderolaRevex,
} from "./revex/sistema";
import {
  FondoCasablanca,
  LogoCardCasablanca,
  TitularCasablanca,
  BajadaCasablanca,
  CtaCasablanca,
  BanderolaCasablanca,
} from "./casablanca/sistema";

/**
 * PREVIEW DE SISTEMA — Revex y Casablanca, post y story.
 * Revex compone CENTRADO y denso (gancho cursivo, barras, cajas, bullets).
 * Casablanca es aire: tarjeta grande, serif itálica abajo, versales y filetes.
 * El contenido es de demostración; los textos definitivos salen del brief.
 */

type QA = {qa?: boolean};

// ─────────────────────────────── REVEX ───────────────────────────────

/** Post de sucursal — modelo: jul_post-condes + rvx_estatico jun. */
export const RevexPreviewFeed: React.FC<QA> = ({qa = false}) => {
  const z = SAFE_ZONES.feed45;
  return (
    <AbsoluteFill>
      <FondoRevex src="assets/revex/sep/lcd_fachada.jpg" velo={0.6} focus="center 30%" />
      <LogoBlockRevex />
      <AbsoluteFill
        style={{
          alignItems: "center",
          justifyContent: "center",
          paddingTop: 190,
          paddingBottom: z.bottom,
          paddingLeft: z.left,
          paddingRight: z.right,
          gap: 44,
        }}
      >
        <TitularRevex linea1="EL SHOWROOM CON MEJOR" linea2="ATENCIÓN PERSONALIZADA" size={51} />
        <BulletLineRevex texto="Ahora en Las Condes" size={34} />
        <DatoBoxRevex pregunta="¿Cómo llegar?" dato="Av. Las Condes 9765, primer piso" size={33} />
        <CtaRevex texto="gruporevex.cl" variante="outline" size={28} />
      </AbsoluteFill>
      <SafeAreaAds format="feed45" show={qa} />
    </AbsoluteFill>
  );
};

/** Story de producto — modelo: rvx_storie_1 (Tu hogar merece → Viena Nuez). */
export const RevexPreviewStory: React.FC<QA> = ({qa = false}) => {
  const z = SAFE_ZONES.story;
  return (
    <AbsoluteFill>
      <FondoRevex src="assets/revex/bg2_haya.png" velo={0.52} />
      <LogoBlockRevex story />
      <AbsoluteFill
        style={{
          alignItems: "center",
          justifyContent: "flex-start",
          paddingTop: 590,
          paddingLeft: z.left,
          paddingRight: z.right,
          gap: 52,
        }}
      >
        <GanchoScriptRevex cursiva="Tu hogar merece" barra="lo mejor en revestimientos" size={104} />
        <BanderolaRevex
          muestra="assets/revex/plank_haya.png"
          categoria="Piso laminado"
          producto="Ambras Haya"
          ancho={185}
          alto={330}
          flagSide="left"
        />
        <CuerpoRevex
          size={31}
          lineas={[
            [{t: "En "}, {t: "Grupo Revex", bold: true}, {t: " encuentras "}, {t: "laminados,", bold: true}],
            [{t: "vinílicos, porcelanatos", bold: true}, {t: " y más."}],
          ]}
        />
        <CtaRevex texto="Cotiza por WhatsApp" size={30} />
      </AbsoluteFill>
      <SafeAreaAds format="story" show={qa} />
    </AbsoluteFill>
  );
};

// ───────────────────────────── CASABLANCA ─────────────────────────────

/** Post — modelo: CB_pisos / Casablanca_pisos: UNA idea abajo, nada más. */
export const CasablancaPreviewFeed: React.FC<QA> = ({qa = false}) => {
  const z = SAFE_ZONES.feed45;
  return (
    <AbsoluteFill>
      <FondoCasablanca src="assets/casablanca/amb_natural_uv_grande.jpg" velo={0.42} />
      <LogoCardCasablanca />
      <AbsoluteFill
        style={{
          justifyContent: "flex-end",
          alignItems: "center",
          paddingBottom: z.bottom + 40,
          paddingLeft: z.left + 30,
          paddingRight: z.right + 30,
          gap: 40,
        }}
      >
        <TitularCasablanca texto="Roble Natural UV" size={86} />
        <BajadaCasablanca texto="Limpio, versátil y atemporal" size={26} />
        <CtaCasablanca texto="Conócelo acá →" variante="outline" size={26} />
      </AbsoluteFill>
      <SafeAreaAds format="feed45" show={qa} />
    </AbsoluteFill>
  );
};

/** Story — modelo: carruseles mayo/julio (muestra izquierda + etiqueta gris, serif abajo). */
export const CasablancaPreviewStory: React.FC<QA> = ({qa = false}) => {
  const z = SAFE_ZONES.story;
  return (
    <AbsoluteFill>
      <FondoCasablanca src="assets/casablanca/amb_aserrado.jpg" velo={0.44} />
      <LogoCardCasablanca story />
      <div style={{position: "absolute", left: 255, top: 720}}>
        <BanderolaCasablanca
          tabla="assets/casablanca/tabla_aserrado.png"
          producto="Roble Aserrado"
          alto={430}
        />
      </div>
      <AbsoluteFill
        style={{
          justifyContent: "flex-end",
          alignItems: "center",
          paddingBottom: z.bottom + 60,
          paddingLeft: z.left + 30,
          paddingRight: z.right + 30,
          gap: 44,
        }}
      >
        <TitularCasablanca texto="Roble Aserrado Natural" size={78} />
        <BajadaCasablanca texto="Textura auténtica, carácter real" size={25} width="78%" />
        <CtaCasablanca texto="Cotiza por WhatsApp" variante="versales" size={24} />
      </AbsoluteFill>
      <SafeAreaAds format="story" show={qa} />
    </AbsoluteFill>
  );
};
