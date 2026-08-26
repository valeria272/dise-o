import {
  AbsoluteFill,
  Audio,
  Img,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {Video} from "@remotion/media";

export const TRAVERSO_REEL_FPS = 30;

const NAVY = "#001489";
const YELLOW = "#FEDD00";

/**
 * "Está en todas las mesas de Chile" — spot dieciochero.
 * El hilo es una anáfora: cada plano es otra mesa, y el registro emocional cambia
 * (oficio, intimidad, camaradería, ternura) hasta cerrar en la mesa que las reúne.
 * Cada plano: archivo, frames en pantalla y desde qué segundo del clip original.
 */
/**
 * `zoom` reencuadra el plano (recorta los bordes): se usa en el carrito nocturno
 * para dejar fuera de cuadro el letrero de la cerveza — nada de marcas de terceros.
 * Máximo dos risas en todo el spot: obreros y abuela con nieto; el resto, contenido.
 */
type ShotDef = {src: string; frames: number; trimStart: number; zoom?: number};

const SHOTS: ShotDef[] = [
  {src: "assets/traverso/reel/11-maestro-mostaza.mp4", frames: 126, trimStart: 0.3, zoom: 1.32},
  {src: "assets/traverso/reel/14-fonda-anticuchos.mp4", frames: 108, trimStart: 0.3},
  {src: "assets/traverso/reel/12-once-casa.mp4", frames: 114, trimStart: 0.3},
  {src: "assets/traverso/reel/06-obreros.mp4", frames: 96, trimStart: 0.5},
  {src: "assets/traverso/reel/13-asado-padre-hijo.mp4", frames: 108, trimStart: 0.3},
  {src: "assets/traverso/reel/15-ramada-mesa.mp4", frames: 108, trimStart: 0.3},
  {src: "assets/traverso/reel/04-abuela-nieto.mp4", frames: 96, trimStart: 0.5},
  {src: "assets/traverso/reel/05d-mesa-cierre.mp4", frames: 138, trimStart: 0.2},
];

const OUTRO_FRAMES = 90;

/** Cuánto se encabalgan dos planos vecinos: el fundido dura justo eso. */
const CROSSFADE = 14;

/**
 * Los planos se solapan CROSSFADE frames, así que cada uno arranca antes de que
 * termine el anterior y ambos conviven durante el fundido.
 */
const SHOT_STARTS = SHOTS.reduce<number[]>((acc, _shot, i) => {
  acc.push(i === 0 ? 0 : acc[i - 1] + SHOTS[i - 1].frames - CROSSFADE);
  return acc;
}, []);

const REEL_END = SHOT_STARTS[SHOTS.length - 1] + SHOTS[SHOTS.length - 1].frames;

export const TRAVERSO_REEL_DURATION = REEL_END + OUTRO_FRAMES - CROSSFADE;

/** Plano con fundido de entrada y de salida; el primero entra desde negro. */
const Shot: React.FC<{shot: (typeof SHOTS)[number]; index: number}> = ({shot, index}) => {
  const frame = useCurrentFrame();

  const fadeIn = interpolate(frame, [0, index === 0 ? 20 : CROSSFADE], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const fadeOut = interpolate(
    frame,
    [shot.frames - CROSSFADE, shot.frames],
    [1, 0],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp"}
  );

  // El audio propio de cada clip va MUTEADO: cada clip IA trae su propia música
  // de fondo y al montarlos la banda sonora saltaba de un estilo a otro.
  // La única cama sonora del spot es la pista de música continua.
  return (
    <AbsoluteFill style={{opacity: Math.min(fadeIn, fadeOut)}}>
      <Video
        src={staticFile(shot.src)}
        trimBefore={Math.round(shot.trimStart * TRAVERSO_REEL_FPS)}
        volume={0}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          transform: shot.zoom ? `scale(${shot.zoom})` : undefined,
          transformOrigin: "50% 92%",
        }}
      />
    </AbsoluteFill>
  );
};

/**
 * Bajada de la anáfora: "EN LA MESA" fija arriba en blanco chico, y debajo
 * la mesa concreta en amarillo. La repetición del primer renglón es el hilo del spot.
 */
const Mesa: React.FC<{cual: string; big?: boolean}> = ({cual, big}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const enter = spring({fps, frame, config: {damping: 200, stiffness: 80, mass: 0.7}});
  const y = interpolate(enter, [0, 1], [30, 0]);
  const opacity = interpolate(frame, [0, 9], [0, 1], {extrapolateRight: "clamp"});

  return (
    <AbsoluteFill
      style={{
        justifyContent: "flex-end",
        alignItems: "center",
        paddingBottom: 250,
        background:
          "linear-gradient(to top, rgba(0,0,0,0.74) 0%, rgba(0,0,0,0.34) 25%, rgba(0,0,0,0) 45%)",
      }}
    >
      <div
        style={{
          transform: `translateY(${y}px)`,
          opacity,
          textAlign: "center",
          padding: "0 76px",
          display: "flex",
          flexDirection: "column",
          gap: 12,
        }}
      >
        {big ? null : (
          <span
            style={{
              fontFamily: "Optima, 'Marcellus', Candara, serif",
              fontSize: 34,
              letterSpacing: "0.3em",
              color: "rgba(255,255,255,0.9)",
              textTransform: "uppercase",
              textShadow: "0 4px 20px rgba(0,0,0,0.7)",
            }}
          >
            En la mesa
          </span>
        )}
        <span
          style={{
            fontFamily: "Optima, 'Marcellus', Candara, serif",
            fontSize: big ? 84 : 76,
            fontWeight: 700,
            lineHeight: 1.06,
            color: big ? "#ffffff" : YELLOW,
            textShadow: "0 6px 32px rgba(0,0,0,0.66)",
            textTransform: "uppercase",
            textWrap: "balance",
          }}
        >
          {cual}
        </span>
      </div>
    </AbsoluteFill>
  );
};

const Outro: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const logoIn = spring({fps, frame, config: {damping: 200, stiffness: 70, mass: 0.7}});
  const logoScale = interpolate(logoIn, [0, 1], [0.88, 1]);
  const logoOpacity = interpolate(frame, [0, 12], [0, 1], {extrapolateRight: "clamp"});

  const claimOpacity = interpolate(frame, [18, 34], [0, 1], {extrapolateRight: "clamp"});
  const claimY = interpolate(frame, [18, 34], [20, 0], {extrapolateRight: "clamp"});

  const lineWidth = interpolate(frame, [34, 52], [0, 260], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // El azul entra encima del último plano, que a esta altura ya se está yendo.
  const bgIn = interpolate(frame, [0, CROSSFADE], [0, 1], {extrapolateRight: "clamp"});

  return (
    <AbsoluteFill
      style={{
        backgroundColor: NAVY,
        justifyContent: "center",
        alignItems: "center",
        gap: 44,
        opacity: bgIn,
      }}
    >
      <Img
        src={staticFile("assets/traverso/logo-blanco.png")}
        style={{width: 700, transform: `scale(${logoScale})`, opacity: logoOpacity}}
      />

      <div style={{height: 3, width: lineWidth, backgroundColor: YELLOW, borderRadius: 2}} />

      <div
        style={{
          opacity: claimOpacity,
          transform: `translateY(${claimY}px)`,
          textAlign: "center",
        }}
      >
        <div
          style={{
            fontFamily: "Optima, 'Marcellus', Candara, serif",
            fontSize: 62,
            fontStyle: "italic",
            color: "#ffffff",
          }}
        >
          El sabor que siempre nos une
        </div>
        <div
          style={{
            marginTop: 26,
            fontFamily: "Optima, 'Marcellus', Candara, serif",
            fontSize: 26,
            letterSpacing: "0.34em",
            color: YELLOW,
            textTransform: "uppercase",
          }}
        >
          Desde 1896
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const TraversoPasamelaReel: React.FC = () => {
  return (
    <AbsoluteFill style={{backgroundColor: "#000000"}}>
      {SHOTS.map((shot, i) => (
        <Sequence key={shot.src} from={SHOT_STARTS[i]} durationInFrames={shot.frames}>
          <Shot shot={shot} index={i} />
        </Sequence>
      ))}

      <Sequence from={SHOT_STARTS[0] + 16} durationInFrames={86}>
        <Mesa cual="de las tres de la mañana" />
      </Sequence>

      <Sequence from={SHOT_STARTS[1] + 14} durationInFrames={76}>
        <Mesa cual="de la fonda" />
      </Sequence>

      <Sequence from={SHOT_STARTS[2] + 14} durationInFrames={80}>
        <Mesa cual="de la once" />
      </Sequence>

      <Sequence from={SHOT_STARTS[3] + 12} durationInFrames={68}>
        <Mesa cual="de los que madrugan" />
      </Sequence>

      <Sequence from={SHOT_STARTS[4] + 12} durationInFrames={76}>
        <Mesa cual="de toda la vida" />
      </Sequence>

      <Sequence from={SHOT_STARTS[5] + 12} durationInFrames={76}>
        <Mesa cual="del 18" />
      </Sequence>

      <Sequence from={SHOT_STARTS[7] + 20} durationInFrames={100}>
        <Mesa cual="Está en todas las mesas de Chile." big />
      </Sequence>

      <Sequence from={REEL_END - CROSSFADE} durationInFrames={OUTRO_FRAMES}>
        <Outro />
      </Sequence>

      {/* Única banda sonora del spot: continua de principio a fin, sin saltos. */}
      <Audio
        src={staticFile("assets/traverso/musica.mp3")}
        volume={(f) =>
          interpolate(
            f,
            [0, 25, TRAVERSO_REEL_DURATION - 34, TRAVERSO_REEL_DURATION],
            [0, 0.42, 0.42, 0],
            {extrapolateLeft: "clamp", extrapolateRight: "clamp"}
          )
        }
      />
    </AbsoluteFill>
  );
};
