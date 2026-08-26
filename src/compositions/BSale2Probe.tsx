import {AbsoluteFill, OffthreadVideo, staticFile} from "remotion";

type Props = {file: string};

export const BSale2Probe: React.FC<Props> = ({file}) => {
  return (
    <AbsoluteFill style={{backgroundColor: "black"}}>
      <OffthreadVideo src={staticFile(file)} />
    </AbsoluteFill>
  );
};
