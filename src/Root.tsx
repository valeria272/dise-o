import {Composition, Folder} from "remotion";

// Compositions
import {ShowcaseComposition} from "./compositions/Showcase";
import {SanEstebanReel, SE_REEL_FPS, SE_REEL_DURACION} from "./compositions/SanEstebanReel";
import {REEL_TRAFICO, REEL_WSP_ANTOFAGASTA, REEL_MUDANZA} from "./compositions/sanEstebanReelesOctubre";
import {MasCenterReel, REEL_02, REEL_03, duracionReel} from "./compositions/mascenter/MasCenterReel";

// SANTA GOTA — placements de TV (huincha / virtual / full screen). Fase 1: stills.
import {HuinchaTV} from "./compositions/santagota/HuinchaTV";
import {VirtualTV} from "./compositions/santagota/VirtualTV";
import {FullScreenTV} from "./compositions/santagota/FullScreenTV";
import {CierreTV} from "./compositions/santagota/CierreTV";
// Fase 2 — producción: video con alfa (huincha, virtual), full screen y previews.
import {HuinchaTV as HuinchaTVAnim, DUR_HUINCHA} from "./compositions/santagota/tv/HuinchaTV";
import {VirtualTV as VirtualTVAnim, DUR_VIRTUAL} from "./compositions/santagota/tv/VirtualTV";
import {FullTV, DUR_FULL} from "./compositions/santagota/tv/FullTV";
import {HuinchaPreview, VirtualPreview} from "./compositions/santagota/tv/Previews";
import {KF01, KF02, KF03, KF04, KF05, KF06, KF07, KF08, KF09, KF10, KF10Latas} from "./compositions/santagota/spot/Keyframes";
import {V2_01, V2_02, V2_03, V2_04, V2_05, V2_06, V2_07, V2_08a, V2_08b, V2_09, V2_10, V2_11, V2_11Latas} from "./compositions/santagota/spot/KeyframesV2";
import {V3_06, V3_07, V3_08, V3_09, V3_10} from "./compositions/santagota/spot/KeyframesV3";
import {Animatic as SGAnimatic} from "./compositions/santagota/spot/Animatic";
import {AnimaticV2 as SGAnimaticV2} from "./compositions/santagota/spot/AnimaticV2";
import {AnimaticV3 as SGAnimaticV3} from "./compositions/santagota/spot/AnimaticV3";
import {AnimaticV4 as SGAnimaticV4} from "./compositions/santagota/spot/AnimaticV4";
import {AnimaticV5 as SGAnimaticV5} from "./compositions/santagota/spot/AnimaticV5";
import {FullClienteIG, FullClienteIGCapa, DUR_FULL_CLIENTE} from "./compositions/santagota/tv-cliente/FullClienteIG";


// COPYWRITERS — Creative Operating System v1.0. Una pieza = un archivo = una
// dirección de arte. No hay una composición "CopylabPost" con un prop `plantilla`,
// y esa ausencia es el sistema: ver creative-system/COPYWRITERS_CREATIVE_OS.md §1.
import {Signal} from "./compositions/copylab/Signal";
import {Metafora} from "./compositions/copylab/Metafora";
import {Work} from "./compositions/copylab/Work";
import {Proof} from "./compositions/copylab/Proof";
import {People} from "./compositions/copylab/People";
import {Gcl} from "./compositions/copylab/Gcl";
import {TypeLab} from "./compositions/copylab/TypeLab";
import {ReelCover} from "./compositions/copylab/ReelCover";
import {Carrusel} from "./compositions/copylab/Carrusel";
import {ReelSenal, REEL_SENAL_FRAMES} from "./compositions/copylab/ReelSenal";
import {Goma} from "./compositions/copylab/Goma";
import {Feed12} from "./compositions/copylab/Feed12";
import {HeroGoma, HeroNadie01, HeroSantaGota} from "./compositions/copylab/Heroes";
import {Estudio, SistemaNadie} from "./compositions/copylab/Estudios";
import {Post12, Post16} from "./compositions/copylab/Posts12";
import {TipoPost} from "./compositions/copylab/Tipo";
import {Recompuesta} from "./compositions/copylab/Recompuesta";
import {Fuente} from "./compositions/copylab/Fuentes";
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
import {
  OctCarrusel,
  OctPosts,
  OctStories,
  OCT_CARRUSEL,
  OCT_POSTS,
  OCT_STORIES,
} from "./compositions/tierracalma/Octubre";
import {
  ReelPrimaveraOct,
  ReelDronOct,
  ReelDronOctV2,
  StoryPetalos,
  StoryPov,
  REEL_DURATION as OCT_REEL_DUR,
  REEL_DRON_V2_DURATION as OCT_DRON_V2_DUR,
  STORY_DURATION as OCT_STORY_DUR,
} from "./compositions/tierracalma/OctubreVideo";
import {
  V3ReelPrimavera,
  V3ReelDron,
  V3_REEL_D_DURATION,
  V3_REEL_I_DURATION,
} from "./compositions/tierracalma/OctubreVideoV3";
import {
  V3CarrE,
  V3CarrK,
  V3Posts,
  V3Stories,
  V3_CARR_E,
  V3_CARR_K,
  V3_POSTS,
  V3_STORIES,
} from "./compositions/tierracalma/OctubreV3";
import {PaidOct1x1, PaidOct4x5, PaidOctD1_9x16, PaidOctD1_4x5, PAID_OCT_1x1, PAID_OCT_4x5} from "./compositions/tierracalma/PaidOctubre";
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
import {EbemaClickReelOctubre, OCT_DURATION, OCT_FPS} from "./compositions/EbemaClickReelOctubre";
import {EbemaGrillaStoryClickOct, STORY_OCT_DURATION, STORY_OCT_FPS} from "./compositions/ebema/EbemaGrillaStoryClickOct";
import {EbemaLinkedinReelTalca, TALCA_DURATION, TALCA_FPS} from "./compositions/ebema/EbemaLinkedinReelTalca";
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
import {LosDeSiempre, LDS_FPS, LDS_W, LDS_H, LDS_DURATION} from "./compositions/traverso/LosDeSiempre";
import {LosDeSiempreEntrance, ENT_FPS, ENT_W, ENT_H, ENT_DURATION} from "./compositions/traverso/LosDeSiempreEntrance";
import {LosDeSiempreEntranceV2, ENT2_FPS, ENT2_W, ENT2_H, ENT2_DURATION} from "./compositions/traverso/LosDeSiempreEntranceV2";
import {LosDeSiempreEntranceV3, ENT3_FPS, ENT3_W, ENT3_H, ENT3_DURATION} from "./compositions/traverso/LosDeSiempreEntranceV3";
import {LosDeSiempreEntranceV4, ENT4_FPS, ENT4_W, ENT4_H, ENT4_DURATION} from "./compositions/traverso/LosDeSiempreEntranceV4";
import {LosDeSiempreV10, V10_FPS, V10_W, V10_H, V10_DURATION} from "./compositions/traverso/LosDeSiempreV10";
import {LosDeSiempreV9, V9_FPS, V9_W, V9_H, V9_DURATION} from "./compositions/traverso/LosDeSiempreV9";
import {LosDeSiempreV8, V8_FPS, V8_W, V8_H, V8_DURATION} from "./compositions/traverso/LosDeSiempreV8";
import {LosDeSiempreV7, V7_FPS, V7_W, V7_H, V7_DURATION} from "./compositions/traverso/LosDeSiempreV7";
import {LosDeSiempreV6, V6_FPS, V6_W, V6_H, V6_DURATION} from "./compositions/traverso/LosDeSiempreV6";
import {LosDeSiempreV5, V5_FPS, V5_W, V5_H, V5_DURATION} from "./compositions/traverso/LosDeSiempreV5";
import {TraversoRutaA, TraversoRutaB, RUTA_FPS, RUTA_W, RUTA_H, RUTA_DURATION} from "./compositions/traverso/LosDeSiempreTestRutas";
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
import {Cap02Revision7} from "./compositions/gcl/Cap02Revision7";
import {Cap02Bloque1, Cap02VozComparacion, VOZ_COMPARACION_FRAMES} from "./compositions/gcl/Cap02Bloque1";
import {Cap02Bloque2} from "./compositions/gcl/Cap02Bloque2";
import {Cap02FullRough, Cap02FullRoughClean, FULL_FRAMES} from "./compositions/gcl/Cap02FullRough";
import {Cap02ClarityCut, V2_FRAMES} from "./compositions/gcl/Cap02ClarityCut";
import {Cap02ClarityCutV3, V3_FRAMES} from "./compositions/gcl/Cap02ClarityCutV3";
import {Cap02V4, Cap02PremasterReview, V4_FRAMES} from "./compositions/gcl/Cap02V4";
import {Cap02TurnoDeNoche, TURNO_FRAMES} from "./compositions/gcl/Cap02TurnoDeNoche";
import {Cap02TurnoDeNocheV2, TURNO_V2_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV2";
import {Cap02TurnoDeNocheV3, TURNO_V3_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV3";
import {Cap02TurnoDeNocheV4, TURNO_V4_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV4";
import {Cap02TurnoDeNocheV5, TURNO_V5_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV5";
import {Cap02TurnoDeNocheV6, TURNO_V6_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV6";
import {Cap02TurnoDeNocheV7, TURNO_V7_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV7";
import {Cap02TurnoDeNocheV8, TURNO_V8_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV8";
import {Cap02TurnoDeNocheV9, TURNO_V9_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV9";
import {Cap02TurnoDeNocheV10, TURNO_V10_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV10";
import {Cap02TurnoDeNocheV11, TURNO_V11_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV11";
import {Cap02TurnoDeNocheV12, TURNO_V12_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV12";
import {Cap02TurnoDeNocheV13, TURNO_V13_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV13";
import {Cap02TurnoDeNocheV14, TURNO_V14_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV14";
import {Cap02TurnoDeNocheV15, TURNO_V15_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV15";
import {Cap02TurnoDeNocheV16, TURNO_V16_FRAMES} from "./compositions/gcl/Cap02TurnoDeNocheV16";

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
  ToGo1, ToGo1Direccion, ToGo2, ToGo3, ToGo4,
  HumorCafecito,
  Foto1, Foto2, Foto3, Foto4,
  EllaHablo,
  Cowork1, Cowork2, Cowork3, Cowork4,
  StToGoDulce, StCumple, StCalculos, StEmergencia, StHoraCafe,
  StCowork, StDieciocho, StStrudel, StPrimavera, StHumorToGo, StPlateada,
  Cumple1, Cumple2,
} from "./compositions/hilton/BetweenSeptiembre";
import {
  StCumpleC1, StCumpleC2, StCumpleC1Guia, StCumpleC2Guia,
} from "./compositions/hilton/BetweenStCumpleCarrusel";
import {
  StS3HoraCafe, StS3Cowork, StS3Dieciocho, StS3HoraCafeGuia, StS3CoworkGuia,
} from "./compositions/hilton/BetweenStS3";
import {
  C1S3Concurso1, C1S3Concurso2,
} from "./compositions/hilton/BetweenC1S3Concurso";
import {PlanchaTrazos} from "./compositions/hilton/BetweenPlanchaTrazos";
import {PruebaEmoji} from "./compositions/hilton/BetweenPruebaEmoji";
import {
  StS4Strudel, StS4Primavera, StS4StrudelGuia, StS4PrimaveraGuia,
} from "./compositions/hilton/BetweenStS4";
import {
  StS5HumorToGo, StS5Plateada, StS5HumorToGoGuia, StS5PlateadaGuia,
  DURACION_PLATEADA,
} from "./compositions/hilton/BetweenStS5";

import {SelfieBannerSemanaPeluquero} from "./compositions/SelfieBannerSemanaPeluquero";
import {SelfieCarruselFrizz} from "./compositions/SelfieCarruselFrizz";
import {SelfieCarruselEmoji} from "./compositions/SelfieCarruselEmoji";
import {SelfieCarruselFiestas} from "./compositions/SelfieCarruselFiestas";
import {SelfieCarruselClass} from "./compositions/SelfieCarruselClass";

const clFeed = {durationInFrames: 1, fps: 30, width: 1080, height: 1350} as const;
const clStory = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;

export const RemotionRoot: React.FC = () => {
  const btFeed = {durationInFrames: 1, fps: 30, width: 1080, height: 1350} as const;
  const btStory = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;
  return (
    <>
      <Folder name="MasCenter">
        <Composition id="MC-Reel-02" component={MasCenterReel} durationInFrames={duracionReel(REEL_02, 30)} fps={30} width={1080} height={1920} defaultProps={REEL_02} />
        <Composition id="MC-Reel-03" component={MasCenterReel} durationInFrames={duracionReel(REEL_03, 30)} fps={30} width={1080} height={1920} defaultProps={REEL_03} />
        <Composition id="MC-Reel-02-Feed" component={MasCenterReel} durationInFrames={duracionReel(REEL_02, 30)} fps={30} width={1080} height={1080} defaultProps={REEL_02} />
        <Composition id="MC-Reel-03-Feed" component={MasCenterReel} durationInFrames={duracionReel(REEL_03, 30)} fps={30} width={1080} height={1080} defaultProps={REEL_03} />
      </Folder>
      <Folder name="HiltonBetween">
        <Composition id="BW-F-ToGo-1" component={ToGo1} {...btFeed} />
        {/* La misma portada con la dirección al pie — pedido de Scarlette del
            22-09. Va sobre la foto del vaso sobre la mesa y se entrega como
            archivo APARTE: ver `ToGo1Direccion`. */}
        <Composition id="BW-F-ToGo-1-Direccion" component={ToGo1Direccion} {...btFeed} />
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
        {/* S2 · cumpleanos — las dos stories de secuencia del 07-09.
            Las `-Guia` llevan marcada la zona del sticker: son para el CM y NO
            se entregan al cliente. */}
        <Composition id="BW-S-Cumple-C1" component={StCumpleC1} {...btStory} />
        <Composition id="BW-S-Cumple-C2" component={StCumpleC2} {...btStory} />
        <Composition id="BW-S-Cumple-C1-Guia" component={StCumpleC1Guia} {...btStory} />
        <Composition id="BW-S-Cumple-C2-Guia" component={StCumpleC2Guia} {...btStory} />
        {/* S3 · las tres historias de la semana 3, rehechas el 08-09.
            Reemplazan a BW-S-HoraCafe / BW-S-Cowork / BW-S-Dieciocho, que no
            rinden porque sus fotos de origen ya no existen — ver el manual
            § «8 historias de septiembre YA NO SE PUEDEN REHACER».
            Las `-Guia` llevan marcada la zona del sticker: son para el CM y NO
            se entregan al cliente. La del 18-09 no lleva interacción. */}
        <Composition id="BW-S3-HoraCafe" component={StS3HoraCafe} {...btStory} />
        <Composition id="BW-S3-Cowork" component={StS3Cowork} {...btStory} />
        <Composition id="BW-S3-Dieciocho" component={StS3Dieciocho} {...btStory} />
        <Composition id="BW-S3-HoraCafe-Guia" component={StS3HoraCafeGuia} {...btStory} />
        <Composition id="BW-S3-Cowork-Guia" component={StS3CoworkGuia} {...btStory} />
        {/* S3 · CARRUSEL CONCURSO «SE BUSCA: CEO DEL CAFE» — feed 4:5.
            Encargo de la grilla viva (FEED col 10, OK PARA DISENAR). Se entrega
            como «C1 S3 CONCURSO N1/N2.png» en la carpeta S3 · BW del Drive. */}
        {/* ⚠️ `jerarquia` es el orden de lectura que pidió contenido el 21-09
            («principal CONCURSO, después la bajada, y desde ahí SE BUSCA…»).
            `A` es la salida recomendada; `B` protege el cuerpo del titular y
            `ronda5` reproduce la lámina que el cliente está mirando hoy.
            Las dos láminas comparten el valor: un carrusel, un cuerpo de
            titular. Se cambia en la revisión con
            `--props='{"jerarquia":"B"}'`. */}
        <Composition
          id="BW-F-Concurso-1"
          component={C1S3Concurso1}
          defaultProps={{jerarquia: 'A' as const}}
          {...btFeed}
        />
        <Composition
          id="BW-F-Concurso-2"
          component={C1S3Concurso2}
          defaultProps={{jerarquia: 'A' as const}}
          {...btFeed}
        />
        {/* S4 · las dos historias estaticas de la semana 4 (21 y 22-09).
            Encargo de Eli del 09-09: guiadas por las dos referencias que dejo
            contenido en Drive. Las `-Guia` llevan marcada la zona del sticker:
            son para el CM y NO se entregan al cliente. */}
        <Composition id="BW-S4-Strudel" component={StS4Strudel} {...btStory} />
        <Composition id="BW-S4-Primavera" component={StS4Primavera} {...btStory} />
        <Composition id="BW-S4-Strudel-Guia" component={StS4StrudelGuia} {...btStory} />
        <Composition id="BW-S4-Primavera-Guia" component={StS4PrimaveraGuia} {...btStory} />
        {/* ── S5 · 28 y 30 de septiembre ──
            La del 28 es ESTATICA y va sin lockup: el vaso gigante ya trae el
            logotipo impreso. La del 30 es ANIMADA — 9 s, que es lo que pidio
            Eli el 11-09 ("minimo de 8 a 9 segundos", tope 15). Las `-Guia`
            llevan marcada la zona del sticker y NO se entregan al cliente. */}
        <Composition id="BW-S5-HumorToGo" component={StS5HumorToGo} {...btStory} />
        <Composition id="BW-S5-HumorToGo-Guia" component={StS5HumorToGoGuia} {...btStory} />
        <Composition id="BW-S5-Plateada" component={StS5Plateada}
          durationInFrames={DURACION_PLATEADA} fps={30} width={1080} height={1920} />
        <Composition id="BW-S5-Plateada-Guia" component={StS5PlateadaGuia}
          durationInFrames={DURACION_PLATEADA} fps={30} width={1080} height={1920} />
        {/* utilidad de extraccion, no una pieza: ver BetweenPlanchaTrazos.tsx */}
        <Composition id="BW-Plancha-Trazos" component={PlanchaTrazos}
          durationInFrames={1} fps={30} width={2660} height={828} />
        <Composition id="BW-Prueba-Emoji" component={PruebaEmoji}
          durationInFrames={1} fps={30} width={640} height={640} />
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

      <Folder name="SanEsteban">
        <Composition
          id="SE-Reel-Trafico"
          component={SanEstebanReel}
          durationInFrames={SE_REEL_DURACION}
          fps={SE_REEL_FPS}
          width={1080}
          height={1920}
          defaultProps={{escenas: REEL_TRAFICO}}
        />
        <Composition
          id="SE-Reel-WspAntofagasta"
          component={SanEstebanReel}
          durationInFrames={SE_REEL_DURACION}
          fps={SE_REEL_FPS}
          width={1080}
          height={1920}
          defaultProps={{escenas: REEL_WSP_ANTOFAGASTA}}
        />
        <Composition
          id="SE-Reel-Mudanza"
          component={SanEstebanReel}
          durationInFrames={SE_REEL_DURACION}
          fps={SE_REEL_FPS}
          width={1080}
          height={1920}
          defaultProps={{escenas: REEL_MUDANZA}}
        />
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
        <Composition id="TraversoV10" component={LosDeSiempreV10} durationInFrames={V10_DURATION} fps={V10_FPS} width={V10_W} height={V10_H} />
        <Composition id="TraversoV9" component={LosDeSiempreV9} durationInFrames={V9_DURATION} fps={V9_FPS} width={V9_W} height={V9_H} />
        <Composition id="TraversoV8" component={LosDeSiempreV8} durationInFrames={V8_DURATION} fps={V8_FPS} width={V8_W} height={V8_H} />
        <Composition id="TraversoV7" component={LosDeSiempreV7} durationInFrames={V7_DURATION} fps={V7_FPS} width={V7_W} height={V7_H} />
        <Composition id="TraversoV6" component={LosDeSiempreV6} durationInFrames={V6_DURATION} fps={V6_FPS} width={V6_W} height={V6_H} />
        <Composition id="TraversoV5" component={LosDeSiempreV5} durationInFrames={V5_DURATION} fps={V5_FPS} width={V5_W} height={V5_H} />
        <Composition id="TraversoEntranceV4" component={LosDeSiempreEntranceV4} durationInFrames={ENT4_DURATION} fps={ENT4_FPS} width={ENT4_W} height={ENT4_H} />
        <Composition id="TraversoRutaA" component={TraversoRutaA} durationInFrames={RUTA_DURATION} fps={RUTA_FPS} width={RUTA_W} height={RUTA_H} />
        <Composition id="TraversoRutaB" component={TraversoRutaB} durationInFrames={RUTA_DURATION} fps={RUTA_FPS} width={RUTA_W} height={RUTA_H} />
        <Composition
          id="TraversoEntranceV3"
          component={LosDeSiempreEntranceV3}
          durationInFrames={ENT3_DURATION}
          fps={ENT3_FPS}
          width={ENT3_W}
          height={ENT3_H}
        />
        <Composition
          id="TraversoEntranceV2"
          component={LosDeSiempreEntranceV2}
          durationInFrames={ENT2_DURATION}
          fps={ENT2_FPS}
          width={ENT2_W}
          height={ENT2_H}
        />
        <Composition
          id="TraversoEntrance"
          component={LosDeSiempreEntrance}
          durationInFrames={ENT_DURATION}
          fps={ENT_FPS}
          width={ENT_W}
          height={ENT_H}
        />
        <Composition
          id="TraversoLosDeSiempre"
          component={LosDeSiempre}
          durationInFrames={LDS_DURATION}
          fps={LDS_FPS}
          width={LDS_W}
          height={LDS_H}
        />
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
        {/* G.CL · Cap. 02 «Revisión 7» — ROUGH CUT v3. 776f · 25,87 s · 112,5 BPM */}
        <Composition id="GclCap02Bloque1" component={Cap02Bloque1} durationInFrames={138} fps={30} width={1080} height={1920} />
        <Composition id="GclCap02FullRough" component={Cap02FullRough} durationInFrames={FULL_FRAMES} fps={30} width={1080} height={1920} />
        <Composition id="GclCap02PremasterReview" component={Cap02PremasterReview} durationInFrames={V4_FRAMES} fps={30} width={1080} height={1920} />
        <Composition id="GclCap02TurnoDeNocheV2" component={Cap02TurnoDeNocheV2} durationInFrames={TURNO_V2_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV3" component={Cap02TurnoDeNocheV3} durationInFrames={TURNO_V3_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV4" component={Cap02TurnoDeNocheV4} durationInFrames={TURNO_V4_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV5" component={Cap02TurnoDeNocheV5} durationInFrames={TURNO_V5_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV6" component={Cap02TurnoDeNocheV6} durationInFrames={TURNO_V6_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV7" component={Cap02TurnoDeNocheV7} durationInFrames={TURNO_V7_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV8" component={Cap02TurnoDeNocheV8} durationInFrames={TURNO_V8_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV9" component={Cap02TurnoDeNocheV9} durationInFrames={TURNO_V9_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV10" component={Cap02TurnoDeNocheV10} durationInFrames={TURNO_V10_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV11" component={Cap02TurnoDeNocheV11} durationInFrames={TURNO_V11_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV12" component={Cap02TurnoDeNocheV12} durationInFrames={TURNO_V12_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV13" component={Cap02TurnoDeNocheV13} durationInFrames={TURNO_V13_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV14" component={Cap02TurnoDeNocheV14} durationInFrames={TURNO_V14_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV15" component={Cap02TurnoDeNocheV15} durationInFrames={TURNO_V15_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNocheV16" component={Cap02TurnoDeNocheV16} durationInFrames={TURNO_V16_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02TurnoDeNoche" component={Cap02TurnoDeNoche} durationInFrames={TURNO_FRAMES} fps={30} width={1080} height={1920} defaultProps={{}} />
        <Composition id="GclCap02V4" component={Cap02V4} durationInFrames={V4_FRAMES} fps={30} width={1080} height={1920} />
        <Composition id="GclCap02ClarityCutV3" component={Cap02ClarityCutV3} durationInFrames={V3_FRAMES} fps={30} width={1080} height={1920} />
        <Composition id="GclCap02ClarityCut" component={Cap02ClarityCut} durationInFrames={V2_FRAMES} fps={30} width={1080} height={1920} />
        <Composition id="GclCap02FullRoughClean" component={Cap02FullRoughClean} durationInFrames={FULL_FRAMES} fps={30} width={1080} height={1920} />
        <Composition id="GclCap02Bloque2" component={Cap02Bloque2} durationInFrames={294} fps={30} width={1080} height={1920} />
        <Composition id="GclCap02VozComparacion" component={Cap02VozComparacion} durationInFrames={VOZ_COMPARACION_FRAMES} fps={30} width={1080} height={1920} />
        <Composition
          id="GclCap02Revision7"
          component={Cap02Revision7}
          durationInFrames={776}
          fps={30}
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
        {/* OCTUBRE 2026 · V3 — la grilla rehecha del 22-09 (16:12Z). Manda ésta. */}
        <Composition id="TCV3ReelPrimavera" component={V3ReelPrimavera} durationInFrames={V3_REEL_D_DURATION} fps={30} width={1080} height={1920} />
        <Composition id="TCV3ReelDron" component={V3ReelDron} durationInFrames={V3_REEL_I_DURATION} fps={30} width={1080} height={1920} />
        <Composition id="TCV3CarrE" component={V3CarrE} durationInFrames={V3_CARR_E.length} fps={30} width={1080} height={1350} />
        <Composition id="TCV3CarrK" component={V3CarrK} durationInFrames={V3_CARR_K.length} fps={30} width={1080} height={1350} />
        <Composition id="TCV3Posts" component={V3Posts} durationInFrames={V3_POSTS.length} fps={30} width={1080} height={1350} />
        {/* PAID OCTUBRE 2026 — campaña WhatsApp del 01-oct (brief de Ignacio) */}
        <Composition id="TCPaidOct1x1" component={PaidOct1x1} durationInFrames={PAID_OCT_1x1.length} fps={30} width={1080} height={1080} />
        <Composition id="TCPaidOct4x5" component={PaidOct4x5} durationInFrames={PAID_OCT_4x5.length} fps={30} width={1080} height={1350} />
        <Composition id="TCPaidOctD1x9x16" component={PaidOctD1_9x16} durationInFrames={1} fps={30} width={1080} height={1920} />
        <Composition id="TCPaidOctD1x4x5" component={PaidOctD1_4x5} durationInFrames={1} fps={30} width={1080} height={1350} />
        <Composition id="TCV3Stories" component={V3Stories} durationInFrames={V3_STORIES.length} fps={30} width={1080} height={1920} />

        {/* OCTUBRE 2026 — video. Imagen clave con Magnific → Kling 2.5 → 30 fps */}
        <Composition
          id="TCOct01ReelPrimavera"
          component={ReelPrimaveraOct}
          durationInFrames={OCT_REEL_DUR}
          fps={30}
          width={1080}
          height={1920}
        />
        {/* v2 — ronda del cliente del 22-09: textos nuevos, Seedream 5 Pro +
            Kling 3.0 + ElevenLabs Music v2, y cierre con el logo animado. */}
        <Composition
          id="TCOct13ReelDronV2"
          component={ReelDronOctV2}
          durationInFrames={OCT_DRON_V2_DUR}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TCOct13ReelDron"
          component={ReelDronOct}
          durationInFrames={OCT_REEL_DUR}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TCOct08StoryPetalos"
          component={StoryPetalos}
          durationInFrames={OCT_STORY_DUR}
          fps={30}
          width={1080}
          height={1920}
        />
        <Composition
          id="TCOct15StoryPov"
          component={StoryPov}
          durationInFrames={OCT_STORY_DUR}
          fps={30}
          width={1080}
          height={1920}
        />

        {/* OCTUBRE 2026 — sobre los marcos bloqueados del diseñador (MARCOS.ai) */}
        <Composition
          id="TCOctCarrusel"
          component={OctCarrusel}
          durationInFrames={OCT_CARRUSEL.length}
          fps={30}
          width={1080}
          height={1350}
        />
        <Composition
          id="TCOctPosts"
          component={OctPosts}
          durationInFrames={OCT_POSTS.length}
          fps={30}
          width={1080}
          height={1350}
        />
        <Composition
          id="TCOctStories"
          component={OctStories}
          durationInFrames={OCT_STORIES.length}
          fps={30}
          width={1080}
          height={1920}
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
        {/* pieza 16 del brief de octubre 2026 — 14,8 s, cierre oficial de Paulina */}
        <Composition id="EbemaClickReelOctubre" component={EbemaClickReelOctubre} durationInFrames={OCT_DURATION} fps={OCT_FPS} width={1080} height={1920} />
        <Composition id="EbemaGrillaStoryClickOct" component={EbemaGrillaStoryClickOct} durationInFrames={STORY_OCT_DURATION} fps={STORY_OCT_FPS} width={1080} height={1920} />
        {/* LinkedIn 05/10/2026 — saludo sucursal Talca, calcado del reel de La Calera (2160×3840) */}
        <Composition id="EbemaLinkedinReelTalca" component={EbemaLinkedinReelTalca} durationInFrames={TALCA_DURATION} fps={TALCA_FPS} width={2160} height={3840} />
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
      <Folder name="SantaGota">
        {/* Placements de TV — Fase 1: key visuals estáticos. fps 29.97 NTSC en Fase 2. */}
        <Composition id="SG-Huincha" component={HuinchaTV}    durationInFrames={1} fps={30} width={1920} height={216} />
        <Composition id="SG-Virtual" component={VirtualTV}    durationInFrames={1} fps={30} width={775}  height={1080} />
        <Composition id="SG-Full"    component={FullScreenTV} durationInFrames={1} fps={30} width={1920} height={1080} />
        <Composition id="SG-Cierre"  component={CierreTV}     durationInFrames={1} fps={30} width={1920} height={1080} />
        {/* Fase 2 — masters a 29,97 (NTSC). Huincha y Virtual se renderizan como secuencia PNG con alfa → TGA. */}
        <Composition id="SG-HuinchaTV" component={HuinchaTVAnim} durationInFrames={DUR_HUINCHA} fps={29.97} width={1920} height={216} />
        <Composition id="SG-VirtualTV" component={VirtualTVAnim} durationInFrames={DUR_VIRTUAL} fps={29.97} width={775}  height={1080} />
        <Composition id="SG-FullTV"    component={FullTV}        durationInFrames={DUR_FULL}    fps={29.97} width={1920} height={1080} />
        <Composition id="SG-HuinchaTV-Preview" component={HuinchaPreview} durationInFrames={DUR_HUINCHA} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-VirtualTV-Preview" component={VirtualPreview} durationInFrames={DUR_VIRTUAL} fps={29.97} width={1920} height={1080} />
        {/* Spot «UNA GOTA. CAMBIA TODO.» — 10 keyframes (ruta sin monja, 15-09-2026) */}
        <Composition id="SG-KF-01" component={KF01} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-KF-02" component={KF02} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-KF-03" component={KF03} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-KF-04" component={KF04} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-KF-05" component={KF05} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-KF-06" component={KF06} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-KF-07" component={KF07} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-KF-08" component={KF08} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-KF-09" component={KF09} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-KF-10" component={KF10} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-KF-10-latas" component={KF10Latas} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        {/* V2 — segunda dirección creativa (15-09-2026) */}
        <Composition id="SG-V2-01" component={V2_01} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V2-02" component={V2_02} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V2-03" component={V2_03} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V2-04" component={V2_04} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V2-05" component={V2_05} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V2-06" component={V2_06} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V2-07" component={V2_07} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V2-08a" component={V2_08a} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V2-08b" component={V2_08b} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V2-09" component={V2_09} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V2-10" component={V2_10} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V2-11" component={V2_11} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V2-11-latas" component={V2_11Latas} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        {/* V3 — los 4 cuadros críticos (15-09-2026, noche) */}
        <Composition id="SG-V3-06" component={V3_06} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V3-07" component={V3_07} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V3-08" component={V3_08} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V3-09" component={V3_09} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-V3-10" component={V3_10} durationInFrames={1} fps={29.97} width={1920} height={1080} />
        {/* ANIMATIC — montaje completo, 599 cuadros (15-09-2026, noche) */}
        <Composition id="SG-ANIMATIC" component={SGAnimatic} durationInFrames={599} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-ANIMATIC-V2" component={SGAnimaticV2} durationInFrames={599} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-ANIMATIC-V3" component={SGAnimaticV3} durationInFrames={599} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-ANIMATIC-V4" component={SGAnimaticV4} durationInFrames={599} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-ANIMATIC-V5" component={SGAnimaticV5} durationInFrames={599} fps={29.97} width={1920} height={1080} />
        {/* el full que el cliente mandó a TVN + cierre de Instagram (21-09-2026) */}
        <Composition id="SG-FULL-CLIENTE-IG" component={FullClienteIG} durationInFrames={DUR_FULL_CLIENTE} fps={29.97} width={1920} height={1080} />
        <Composition id="SG-FULL-CLIENTE-IG-CAPA" component={FullClienteIGCapa} durationInFrames={DUR_FULL_CLIENTE} fps={29.97} width={1920} height={1080} />
      </Folder>
      <Folder name="Copywriters">
        {/* Feed 4:5 — el formato principal del sistema. */}
        <Composition id="CL-Signal"   component={Signal}   {...clFeed} />
        <Composition id="CL-Metafora" component={Metafora} {...clFeed} />
        <Composition id="CL-Work"     component={Work}     {...clFeed} />
        <Composition id="CL-Proof"    component={Proof}    {...clFeed} />
        <Composition id="CL-People"   component={People}   {...clFeed} />
        <Composition id="CL-Gcl"      component={Gcl}      {...clFeed} />
        <Composition id="CL-TypeLab"  component={TypeLab}  {...clFeed} />
        <Composition id="CL-Goma"     component={Goma}     {...clFeed} />
        <Composition id="CL-Hero1-Goma"      component={HeroGoma}      {...clFeed} />
        <Composition id="CL-Hero2-Nadie01"   component={HeroNadie01}   {...clFeed} />
        <Composition id="CL-Hero3-SantaGota" component={HeroSantaGota} {...clFeed} />
        <Composition id="CL-Estudio"  component={Estudio}  {...clFeed} defaultProps={{k: 1}} />
        <Composition id="CL-Nadie"    component={SistemaNadie} {...clFeed} defaultProps={{sis: 1, n: 1}} />
        <Composition id="CL-Fuente"   component={Fuente}   {...clFeed} defaultProps={{familia: "Acumin Pro ExtraCondensed", peso: 900, nombre: "Acumin", frase: 1 as const}} />
        <Composition id="CL-Recompuesta" component={Recompuesta} {...clFeed} defaultProps={{id: "01"}} />
        <Composition id="CL-Tipo"     component={TipoPost} {...clFeed} defaultProps={{id: "01"}} />
        <Composition id="CL-Post16"   component={Post16}   {...clFeed} defaultProps={{n: 1}} />
        <Composition id="CL-Post12"   component={Post12}   {...clFeed} defaultProps={{n: 1}} />
        <Composition id="CL-Feed12"   component={Feed12}   {...clFeed} defaultProps={{n: 1}} />
        <Composition id="CL-Carrusel" component={Carrusel} {...clFeed} defaultProps={{slide: 1}} />
        {/* 9:16 — respeta las zonas seguras de Meta. */}
        <Composition id="CL-ReelCover" component={ReelCover} {...clStory} />
        <Composition id="CL-ReelSenal" component={ReelSenal} {...clStory} durationInFrames={REEL_SENAL_FRAMES} />
      </Folder>
    </>
  );
};
