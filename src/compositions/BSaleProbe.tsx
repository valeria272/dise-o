import {AbsoluteFill, OffthreadVideo, staticFile} from "remotion";

export const BSaleProbe: React.FC = () => {
  return (
    <AbsoluteFill style={{backgroundColor: "black"}}>
      <OffthreadVideo src={staticFile("raw/BSALE_original.mp4")} />
    </AbsoluteFill>
  );
};
