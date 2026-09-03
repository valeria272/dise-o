import {Composition, Folder} from "remotion";

// Compositions
import {ShowcaseComposition} from "./compositions/Showcase";
import {RentasReelOctubre} from "./compositions/rentas/RentasReelOctubre";
import {NuevaUrbeFacilidadesReel, NU_REEL_DURATION, NU_REEL_FPS} from "./compositions/NuevaUrbeFacilidadesReel";
import {VideoSquare01} from "./compositions/VideoSquare01";
import {BSaleProbe} from "./compositions/BSaleProbe";
import {BSale2Probe} from "./compositions/BSale2Probe";
import {PivotConnectReel} from "./compositions/PivotConnectReel";
import {PivotConnectReelWow} from "./compositions/PivotConnectReelWow";
import {FbCoverBanner} from "./compositions/FbCoverBanner";
import {FbProfilePic} from "./compositions/FbProfilePic";
import {ScopeMediaTestReel} from "./compositions/ScopeMediaTestReel";
import {ScopeProofReel, SCOPE_PROOF_DURATION} from "./compositions/ScopeProofReel";
import {ScopeReel2, SCOPE_REEL2_DURATION} from "./compositions/ScopeReel2";
import {BravaReel, BRAVA_REEL_DURATION} from "./compositions/BravaReel";
import {TierraCalmaReel, TIERRACALMA_REEL_DURATION} from "./compositions/TierraCalmaReel";
import {ReelUbicacion, REEL_UBICACION_DURATION} from "./compositions/tierracalma/ReelUbicacion";
import {ReelFicha, REEL_FICHA_DURATION} from "./compositions/tierracalma/ReelFicha";
import {ReelCelebracion, REEL_CELEBRACION_DURATION} from "./compositions/tierracalma/ReelCelebracion";
import {ReelPrimavera, REEL_PRIMAVERA_DURATION} from "./compositions/tierracalma/ReelPrimavera";
import {Piezas4x5, Piezas9x16, Piezas1x1, PIEZAS_4x5, PIEZAS_9x16, PIEZAS_1x1} from "./compositions/tierracalma/Piezas";
import {Specimen} from "./compositions/tierracalma/Specimen";
import {HistoriaPrimavera, HistoriaPaso, HistoriaEpoca, HISTORIA_DURATION} from "./compositions/tierracalma/HistoriasAnimadas";
import {PruebaPosts4x5, PruebaHistoria, PruebaReel, PRUEBA_POSTS, PRUEBA_HISTORIA_ANIM_DURATION, PRUEBA_REEL_DURATION} from "./compositions/tierracalma/PruebaCarlos";

import {AdCostsChileReel, AD_COSTS_REEL_DURATION} from "./compositions/AdCostsChileReel";
import {CasoExitoConsumoReel, CASO_EXITO_REEL_DURATION} from "./compositions/CasoExitoConsumoReel";
import {AdvertiqHero, ADVERTIQ_HERO_DURATION, ADVERTIQ_HERO_FPS} from "./compositions/AdvertiqHero";
import {AbakosReelSeptiembre, ABAKOS_REEL_DURATION, ABAKOS_REEL_FPS} from "./compositions/AbakosReelSeptiembre";
import {AbakosReelGastos, ABAKOS_GASTOS_DURATION, ABAKOS_GASTOS_FPS} from "./compositions/AbakosReelGastos";
import {AbakosCarruselDieciocho} from "./compositions/AbakosCarruselDieciocho";
import {EbemaShowroomReel, EBEMA_REEL_DURATION, EBEMA_REEL_FPS} from "./compositions/EbemaShowroomReel";
import {EbemaClickReel, EBEMA_CLICK_DURATION, EBEMA_CLICK_FPS} from "./compositions/EbemaClickReel";
import {RevexLaminadosSlide} from "./compositions/RevexLaminadosCarrusel";
import {RevexSepPieza, REVEX_SEP_PIEZAS} from "./compositions/RevexSeptiembre";
import {RevexSep2026, REVEX_SEP26} from "./compositions/RevexSep2026";
import {CasablancaSep2026, CB_SEP26} from "./compositions/CasablancaSep2026";
import {CasablancaEditorial, CB_ED} from "./compositions/CasablancaEditorial";
import {CasablancaSep, CB_SEP} from "./compositions/CasablancaSep";
import {
  RevexPreviewFeed,
  RevexPreviewStory,
  CasablancaPreviewFeed,
  CasablancaPreviewStory,
} from "./compositions/RevexCasablancaPreview";
import {
  TraversoPasamelaReel,
  TRAVERSO_REEL_DURATION,
  TRAVERSO_REEL_FPS,
} from "./compositions/TraversoPasamelaReel";
import {GclPost, GCL_POST_DEMO} from "./compositions/gcl/GclPost";
import {
  GclOrigenReel,
  GCL_ORIGEN_DURATION,
  GCL_ORIGEN_FPS,
} from "./compositions/GclOrigenReel";
import {
  GclTurnoNocheReel,
  GCL_R02_DURATION,
  GCL_R02_FPS,
} from "./compositions/GclTurnoNocheReel";

// Social templates
import {TikTokVideo} from "./templates/social/TikTokVideo";
import {InstagramReel} from "./templates/social/InstagramReel";
import {YouTubeShort} from "./templates/social/YouTubeShort";

// Content templates
import {Presentation} from "./templates/content/Presentation";
import {Testimonial} from "./templates/content/Testimonial";

// Promo templates
import {Announcement} from "./templates/promo/Announcement";
import {BeforeAfterDemo} from "./compositions/BeforeAfterDemo";

// Editing templates
import {TalkingHeadEdit} from "./templates/editing/TalkingHeadEdit";
import {PodcastClip} from "./templates/editing/PodcastClip";

import {
  ToGo1, ToGo2, ToGo3, ToGo4,
  HumorCafecito,
  Foto1, Foto2, Foto3, Foto4,
  EllaHablo,
  Cowork1, Cowork2, Cowork3, Cowork4,
  StToGoDulce, StCumple, StCalculos, StEmergencia, StHoraCafe,
  StCowork, StDieciocho, StStrudel, StPrimavera, StHumorToGo, StPlateada,
  Cumple1, Cumple2,
} from "./compositions/hilton/BetweenSeptiembre";

import {SelfieBannerSemanaPeluquero} from "./compositions/SelfieBannerSemanaPeluquero";
import {SelfieCarruselFrizz} from "./compositions/SelfieCarruselFrizz";
import {SelfieCarruselEmoji} from "./compositions/SelfieCarruselEmoji";
import {SelfieCarruselFiestas} from "./compositions/SelfieCarruselFiestas";
import {SelfieCarruselClass} from "./compositions/SelfieCarruselClass";

export const RemotionRoot: React.FC = () => {
  const btFeed = {durationInFrames: 1, fps: 30, width: 1080, height: 1350} as const;
  const btStory = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;
  return (
    <>
      <Folder name="HiltonBetween">
        <Composition id="BW-F-ToGo-1" component={ToGo1} {...btFeed} />
        <Composition id="BW-F-ToGo-2" component={ToGo2} {...btFeed} />
        <Composition id="BW-F-ToGo-3" component={ToGo3} {...btFeed} />
        <Composition id="BW-F-ToGo-4" component={ToGo4} {...btFeed} />
        <Composition id="BW-F-Cumple-1" component={Cumple1} {...btFeed} />
        <Composition id="BW-F-Cumple-2" component={Cumple2} {...btFeed} />
        <Composition id="BW-F-HumorCafecito" component={HumorCafecito} {...btFeed} />
        <Composition id="BW-F-Foto-1" component={Foto1} {...btFeed} />
        <Composition id="BW-F-Foto-2" component={Foto2} {...btFeed} />
        <Composition id="BW-F-Foto-3" component={Foto3} {...btFeed} />
        <Composition id="BW-F-Foto-4" component={Foto4} {...btFeed} />
        <Composition id="BW-F-EllaHablo" component={EllaHablo} {...btFeed} />
        <Composition id="BW-F-Cowork-1" component={Cowork1} {...btFeed} />
        <Composition id="BW-F-Cowork-2" component={Cowork2} {...btFeed} />
        <Composition id="BW-F-Cowork-3" component={Cowork3} {...btFeed} />
        <Composition id="BW-F-Cowork-4" component={Cowork4} {...btFeed} />
        <Composition id="BW-S-ToGoDulce" component={StToGoDulce} {...btStory} />
        <Composition id="BW-S-Cumple" component={StCumple} {...btStory} />
        <Composition id="BW-S-Calculos" component={StCalculos} {...btStory} />
        <Composition id="BW-S-Emergencia" component={StEmergencia} {...btStory} />
        <Composition id="BW-S-HoraCafe" component={StHoraCafe} {...btStory} />
        <Composition id="BW-S-Cowork" component={StCowork} {...btStory} />
        <Composition id="BW-S-Dieciocho" component={StDieciocho} {...btStory} />
        <Composition id="BW-S-Strudel" component={StStrudel} {...btStory} />
        <Composition id="BW-S-Primavera" component={StPrimavera} {...btStory} />
        <Composition id="BW-S-HumorToGo" component={StHumorToGo} {...btStory} />
        <Composition id="BW-S-Plateada" component={StPlateada} {...btStory} />
      </Folder>
      <Folder name="Selfie">
        <Composition
          id="SelfieCarruselFiestas"
          component={SelfieCarruselFiestas}
          durationInFrames={1}
          fps={30}
          width={2250}
          height={2813}
          defaultProps={{slide: 1}}
        />
        <Composition
          id="SelfieCarruselClass"
          component={SelfieCarruselClass}
          durationInFrames={1}
          fps={30}
          width={2250}
          height={2813}
          defaultProps={{slide: 1}}
        />
        <Composition
          id="SelfieCarruselEmoji"
          component={SelfieCarruselEmoji}
          durationInFrames={1}
          fps={30}
          width={2250}
          height={2813}
          defaultProps={{slide: 1}}
        />
        <Composition
          id="SelfieCarruselFrizz"
          component={SelfieCarruselFrizz}
          durationInFrames={1}
          fps={30}
          width={2250}
          height={2813}
          defaultProps={{slide: 1}}
        />
        <Composition
          id="SelfieBannerSemanaPeluquero"
          component={SelfieBannerSemanaPeluquero}
          durationInFrames={1}
          fps={30}
          width={2001}
          height={686}
        />
      </Folder>
      <Folder name="Probe">
        <Composition
          id="BSaleProbe"
          component={BSaleProbe}
          durationInFrames={2520}
          fps={60}
          width={1080}
          height={1920}
        />
        <Composition id="ProbeStorytime" component={BSale2Probe} durationInFrames={2520} fps={60} width={1080} height={1920} defaultProps={{file: "pivotconnect_raw/videi antiguo con storytime.mp4"}} />
        <Composition id="ProbePosible1" component={BSale2Probe} durationInFrames={1520} fps={30} width={1080} height={1920} defaultProps={{file: "pivotconnect_raw/Posible 1.MOV"}} />
        <Composition id="ProbeInicio" component={BSale2Probe} durationInFrames={230} fps={30} width={4320} height={7680} defaultProps={{file: "pivotconnect_raw/INICIOPIVOTCONNECT.mp4"}} />
        <Composition id="ProbeEdicion" component={BSale2Probe} durationInFrames={180} fps={30} width={1080} height={1920} defaultProps={{file: "pivotconnect_raw/EDICIÓN BSALE.mp4"}} />
        <Composition id="ProbeOnbording" component={BSale2Probe} durationInFrames={180} fps={30} width={1080} height={1920} defaultProps={{file: "pivotconnect_raw/onbording.MOV"}} />
        <Composition id="ProbeOnboarding2" component={BSale2Probe} durationInFrames={162} fps={30} width={1080} height={1920} defaultProps={{file: "pivotconnect_raw/onboarding 2.MOV"}} />
      </Folder>

      <Folder name="Clients">
        <Composition
          id="NuevaUrbeFacilidadesReel"
          component={NuevaUrbeFacilidadesReel}
          durationInFrames={NU_REEL_DURATION}
          fps={NU_REEL_FPS}
          width={1080}
          height={1920}
        />
        {(["portada", "haya", "perla", "nude", "eucalipto", "cierre"] as const).map(
          (slide, i) => (
            <Composition
              key={slide}
              id={`RevexLam0${i + 1}`}
              component={RevexLaminadosSlide}
              durationInFrames={1}
              fps={30}
              width={1080}
              height={1350}
              defaultProps={{slide}}
            />
          ),
        )}
        {REVEX_SEP_PIEZAS.map(({id, pieza, fmt}) => (
          <Composition
            key={id}
            id={id}
            component={RevexSepPieza}
            durationInFrames={1}
            fps={30}
            width={1080}
            height={fmt === "story" ? 1920 : 1080}
            defaultProps={{pieza, fmt}}
          />
        ))}
        {/* PAID SEPTIEMBRE 2026 — piezas del brief */}
        {REVEX_SEP26.flatMap(({id, pieza, fmt}) =>
          [false, true].map((qa) => (
            <Composition
              key={`${id}${qa ? "QA" : ""}`}
              id={`${id}${qa ? "QA" : ""}`}
              component={RevexSep2026}
              durationInFrames={1}
              fps={30}
              width={1080}
              /* ronda 2: el feed de estas marcas es 4:5, no cuadrado */
              height={fmt === "story" ? 1920 : 1350}
              defaultProps={{pieza, fmt, qa}}
            />
          )),
        )}
        {CB_SEP26.flatMap(({id, pieza, fmt}) =>
          [false, true].map((qa) => (
            <Composition
              key={`${id}${qa ? "QA" : ""}`}
              id={`${id}${qa ? "QA" : ""}`}
              component={CasablancaSep2026}
              durationInFrames={1}
              fps={30}
              width={1080}
              /* ronda 2: el feed de estas marcas es 4:5, no cuadrado */
              height={fmt === "story" ? 1920 : 1350}
              defaultProps={{pieza, fmt, qa}}
            />
          )),
        )}
        {/* CASABLANCA — septiembre 2026, desde el brief + las referencias de la diseñadora */}
        {CB_SEP.flatMap(({id, pieza, fmt, w, h}) =>
          [false, true].map((qa) => (
            <Composition
              key={`${id}${qa ? "-QA" : ""}`}
              id={`${id}${qa ? "-QA" : ""}`}
              component={CasablancaSep}
              durationInFrames={1}
              fps={30}
              width={w}
              height={h}
              defaultProps={{pieza, fmt, qa}}
            />
          )),
        )}
        {/* CASABLANCA — replanteo editorial 25-08-2026 (reemplaza a CB_SEP26) */}
        {CB_ED.flatMap(({id, pieza, fmt, w, h}) =>
          [false, true].map((qa) => (
            <Composition
              key={`${id}${qa ? "-QA" : ""}`}
              id={`${id}${qa ? "-QA" : ""}`}
              component={CasablancaEditorial}
              durationInFrames={1}
              fps={30}
              width={w}
              height={h}
              defaultProps={{pieza, fmt, qa}}
            />
          )),
        )}
        {/* PREVIEW DE SISTEMA — Revex y Casablanca (post + story, con y sin QA) */}
        {(
          [
            ["RvxPrevFeed", RevexPreviewFeed, 1080, 1350],
            ["RvxPrevStory", RevexPreviewStory, 1080, 1920],
            ["CbPrevFeed", CasablancaPreviewFeed, 1080, 1350],
            ["CbPrevStory", CasablancaPreviewStory, 1080, 1920],
          ] as const
        ).flatMap(([id, component, w, h]) =>
          [false, true].map((qa) => (
            <Composition
              key={`${id}${qa ? "QA" : ""}`}
              id={`${id}${qa ? "QA" : ""}`}
              component={component as React.FC<{qa?: boolean}>}
              durationInFrames={1}
              fps={30}
              width={w}
              height={h}
              defaultProps={{qa}}
            />
          )),
        )}
        <Composition
          id="TraversoPasamelaReel"
          component={TraversoPasamelaReel}
          durationInFrames={TRAVERSO_REEL_DURATION}
          fps={TRAVERSO_REEL_FPS}
          width={1080}
          height={1920}
        />
        <Composition
          id="GclOrigenReel"
          component={GclOrigenReel}
          durationInFrames={GCL_ORIGEN_DURATION}
          fps={GCL_ORIGEN_FPS}
          width={1080}
          height={1920}
        />
        <Composition
          id="GclTurnoNocheReel"
          component={GclTurnoNocheReel}
          durationInFrames={GCL_R02_DURATION}
          fps={GCL_R02_FPS}
          width={1080}
          height={1920}
        />
        <Composition
          id="AbakosReelSeptiembre"
          component={AbakosReelSeptiembre}
          durationInFrames={ABAKOS_REEL_DURATION}
          fps={ABAKOS_REEL_FPS}
          width={1080}
          height={1920}
        />
        <Composition
          id="AbakosReelGastos"
          component={AbakosReelGastos}
          durationInFrames={ABAKOS_GASTOS_DURATION}
          fps={ABAKOS_GASTOS_FPS}
          width={1080}
          height={1920}
        />
        {[1, 2, 3, 4, 5, 6].map((n) => (
          <Composition
            key={n}
            id={`AbakosCarrusel${n}`}
            component={AbakosCarruselDieciocho}
            durationInFrames={1}
            fps={30}
            width={1080}
            height={1080}
            defaultProps={{slide: n}}
          />
        ))}
        <Composition
          id="TCHistoriaPrimavera"
          component={HistoriaPrimavera}
          durationInFrames={HISTORIA_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TCHistoriaPaso"
          component={HistoriaPaso}
          durationInFrames={HISTORIA_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TCHistoriaEpoca"
          component={HistoriaEpoca}
          durationInFrames={HISTORIA_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TCPruebaPosts4x5"
          component={PruebaPosts4x5}
          durationInFrames={PRUEBA_POSTS.length}
          fps={30}
          width={1080}
          height={1350}
        />
        <Composition
          id="TCPruebaHistoria"
          component={PruebaHistoria}
          durationInFrames={1}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TCPruebaHistoriaAnim"
          component={PruebaHistoria}
          durationInFrames={PRUEBA_HISTORIA_ANIM_DURATION}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{anim: true}}
        />
        <Composition
          id="TCPruebaReel"
          component={PruebaReel}
          durationInFrames={PRUEBA_REEL_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TCSpecimen"
          component={Specimen}
          durationInFrames={1}
          fps={30}
          width={1800}
          height={1450}
        />
        <Composition
          id="TCPiezas4x5"
          component={Piezas4x5}
          durationInFrames={PIEZAS_4x5.length}
          fps={30}
          width={1080}
          height={1350}
        />
        <Composition
          id="TCPiezas9x16"
          component={Piezas9x16}
          durationInFrames={PIEZAS_9x16.length}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TCPiezas1x1"
          component={Piezas1x1}
          durationInFrames={PIEZAS_1x1.length}
          fps={30}
          width={1080}
          height={1080}
        />
        <Composition
          id="TCSep02Ficha"
          component={ReelFicha}
          durationInFrames={REEL_FICHA_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TCSep03Celebracion"
          component={ReelCelebracion}
          durationInFrames={REEL_CELEBRACION_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TCSep04Primavera"
          component={ReelPrimavera}
          durationInFrames={REEL_PRIMAVERA_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TCSep01Ubicacion"
          component={ReelUbicacion}
          durationInFrames={REEL_UBICACION_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TierraCalmaReel"
          component={TierraCalmaReel}
          durationInFrames={TIERRACALMA_REEL_DURATION}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{closeStyle: "signature" as const}}
        />
        <Composition
          id="TierraCalmaReelLogo"
          component={TierraCalmaReel}
          durationInFrames={TIERRACALMA_REEL_DURATION}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{closeStyle: "logoOnly" as const}}
        />
        <Composition
          id="CasoExitoConsumoReel"
          component={CasoExitoConsumoReel}
          durationInFrames={CASO_EXITO_REEL_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="PivotConnectReel"
          component={PivotConnectReel}
          durationInFrames={2520}
          fps={60}
          width={1080}
          height={1920}
        />
        <Composition
          id="PivotConnectReelWow"
          component={PivotConnectReelWow}
          durationInFrames={1200}
          fps={30}
          width={1080}
          height={1920}
        />
      </Folder>

      <Folder name="Test-Reels">
        <Composition
          id="BravaReel"
          component={BravaReel}
          durationInFrames={BRAVA_REEL_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="ScopeReel2"
          component={ScopeReel2}
          durationInFrames={SCOPE_REEL2_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="ScopeProofReel"
          component={ScopeProofReel}
          durationInFrames={SCOPE_PROOF_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="ScopeMediaTestReel"
          component={ScopeMediaTestReel}
          durationInFrames={900}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="AdCostsChileReel"
          component={AdCostsChileReel}
          durationInFrames={AD_COSTS_REEL_DURATION}
          fps={30}
          width={1080}
          height={1920}
        />
      </Folder>

      <Folder name="FB-Pages">
        <Composition id="HypeCover" component={FbCoverBanner} durationInFrames={1} fps={30} width={1640} height={856} defaultProps={{brand: "hype" as const}} />
        <Composition id="RocketCover" component={FbCoverBanner} durationInFrames={1} fps={30} width={1640} height={856} defaultProps={{brand: "rocket" as const}} />
        <Composition id="HypeProfile" component={FbProfilePic} durationInFrames={1} fps={30} width={720} height={720} defaultProps={{brand: "hype" as const}} />
        <Composition id="RocketProfile" component={FbProfilePic} durationInFrames={1} fps={30} width={720} height={720} defaultProps={{brand: "rocket" as const}} />
      </Folder>

      <Folder name="Square-Videos">
        <Composition
          id="EbemaShowroomReelStory"
          component={EbemaShowroomReel}
          durationInFrames={EBEMA_REEL_DURATION}
          fps={EBEMA_REEL_FPS}
          width={1080}
          height={1920}
          defaultProps={{format: "story" as const}}
        />
        <Composition id="EbemaShowroomReel2Story" component={EbemaShowroomReel} durationInFrames={EBEMA_REEL_DURATION} fps={EBEMA_REEL_FPS} width={1080} height={1920} defaultProps={{format: "story" as const, variant: 2 as const}} />
        <Composition id="EbemaShowroomReel2Feed" component={EbemaShowroomReel} durationInFrames={EBEMA_REEL_DURATION} fps={EBEMA_REEL_FPS} width={1080} height={1350} defaultProps={{format: "feed" as const, variant: 2 as const}} />
        <Composition id="EbemaClickReelStory" component={EbemaClickReel} durationInFrames={EBEMA_CLICK_DURATION} fps={EBEMA_CLICK_FPS} width={1080} height={1920} defaultProps={{format: "story" as const}} />
        <Composition id="EbemaClickReelFeed" component={EbemaClickReel} durationInFrames={EBEMA_CLICK_DURATION} fps={EBEMA_CLICK_FPS} width={1080} height={1350} defaultProps={{format: "feed" as const}} />
        <Composition
          id="EbemaShowroomReelFeed"
          component={EbemaShowroomReel}
          durationInFrames={EBEMA_REEL_DURATION}
          fps={EBEMA_REEL_FPS}
          width={1080}
          height={1350}
          defaultProps={{format: "feed" as const}}
        />
        <Composition
          id="VideoSquare01"
          component={VideoSquare01}
          durationInFrames={1688}
          fps={60}
          width={1080}
          height={1080}
        />
      </Folder>

      <Folder name="ADVERTIQ">
        <Composition
          id="AdvertiqHero"
          component={AdvertiqHero}
          durationInFrames={ADVERTIQ_HERO_DURATION}
          fps={ADVERTIQ_HERO_FPS}
          width={1920}
          height={1080}
        />
      </Folder>

      <Folder name="Examples">
        <Composition
          id="Showcase"
          component={ShowcaseComposition}
          durationInFrames={300}
          fps={30}
          width={1920}
          height={1080}
        />
      </Folder>

      <Folder name="Social">
        <Composition
          id="TikTok"
          component={TikTokVideo}
          durationInFrames={270}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{
            hook: "Did you know this?",
            body: "AI can edit videos now using just code.",
            cta: "Follow for more",
          }}
        />
        <Composition
          id="InstagramReel"
          component={InstagramReel}
          durationInFrames={240}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{
            headline: "Your headline here",
            subtext: "Supporting text goes here",
            brandName: "Brand",
          }}
        />
        <Composition
          id="YouTubeShort"
          component={YouTubeShort}
          durationInFrames={300}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{
            title: "Your Title Here",
            subtitle: "Subtitle goes here",
          }}
        />
      </Folder>

      <Folder name="Content">
        <Composition
          id="Presentation"
          component={Presentation}
          durationInFrames={450}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{
            slides: [
              {title: "Welcome", body: "This is slide one"},
              {title: "The Problem", body: "Here's what we're solving"},
              {title: "The Solution", body: "Here's how we solve it"},
            ],
          }}
        />
        <Composition
          id="Testimonial"
          component={Testimonial}
          durationInFrames={180}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{
            quote:
              "This product completely changed how we work. Highly recommended.",
            author: "Jane Doe",
            role: "CEO at Company",
          }}
        />
      </Folder>

      <Folder name="Promo">
        <Composition
          id="Announcement"
          component={Announcement}
          durationInFrames={300}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{
            preTitle: "Introducing",
            title: "Something Amazing",
            subtitle: "The future is here",
            cta: "Learn More",
          }}
        />
        <Composition
          id="BeforeAfter"
          component={BeforeAfterDemo}
          durationInFrames={180}
          fps={30}
          width={1920}
          height={1080}
        />
      </Folder>

      <Folder name="Editing">
        <Composition
          id="TalkingHeadEdit"
          component={TalkingHeadEdit}
          durationInFrames={900}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{
            videoSrc: "assets/video.mp4",
            showCaptions: true,
            captionPreset: "bold" as const,
            removeSilence: false,
          }}
        />
        <Composition
          id="PodcastClip"
          component={PodcastClip}
          durationInFrames={900}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{
            videoSrc: "assets/video.mp4",
            clipStartSeconds: 0,
            clipEndSeconds: 30,
            showCaptions: true,
            captionPreset: "bold" as const,
          }}
        />
      </Folder>

      {/* ------------------------------------------------------------------
          GCL — piezas estáticas del feed de Grupo Copylab (@copywriters.cl).
          Sistema visual: negro + rosado eléctrico (src/brand/gcl.tokens.json).
          No se renderizan a mano: las pide el agente social con
          AGENTE SOCIAL MEDIA/tools/remotion_render.py
      ------------------------------------------------------------------- */}
      <Folder name="GCL">
        <Composition
          id="GclPost"
          component={GclPost}
          durationInFrames={1}
          fps={30}
          width={1080}
          height={1350}
          defaultProps={GCL_POST_DEMO}
        />
        <Composition
          id="GclHistoria"
          component={GclPost}
          durationInFrames={1}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={GCL_POST_DEMO}
        />
        <Composition
          id="GclCuadrado"
          component={GclPost}
          durationInFrames={1}
          fps={30}
          width={1080}
          height={1080}
          defaultProps={GCL_POST_DEMO}
        />
      </Folder>
      <Folder name="Rentas">
        <Composition
          id="RentasReelOctubre"
          component={RentasReelOctubre}
          durationInFrames={900}
          fps={30}
          width={1080}
          height={1920}
        />
      </Folder>
    </>
  );
};
