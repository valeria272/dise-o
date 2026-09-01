/**
 * Entry point de BETWEEN — rinde toda la grilla sin depender de src/Root.tsx.
 *   npx remotion still src/BetweenEntry.tsx <id> <salida>
 */
import React from 'react';
import {Composition, Folder, registerRoot} from 'remotion';
import {
  Cowork1, Cowork2, Cowork3, Cowork4,
  Cumple1, Cumple2,
  HumorCafecito,
  Foto1, Foto2, Foto3, Foto4,
  EllaHablo,
  ToGo1, ToGo2, ToGo3, ToGo4,
  StToGoDulce, StCumple, StCalculos, StEmergencia, StHoraCafe,
  StCowork, StDieciocho, StStrudel, StPrimavera, StHumorToGo, StPlateada,
} from './compositions/hilton/BetweenSeptiembre';
import {CalibracionTipografia} from './compositions/hilton/BetweenPrueba';

const feed = {durationInFrames: 1, fps: 30, width: 1080, height: 1350} as const;
const story = {durationInFrames: 1, fps: 30, width: 1080, height: 1920} as const;

const Raiz: React.FC = () => (
  <>
    <Folder name="BW-Prueba">
      <Composition id="BW-P-Calibracion" component={CalibracionTipografia} {...feed} />
    </Folder>
    <Folder name="BW-Feed">
      <Composition id="BW-F-ToGo-1" component={ToGo1} {...feed} />
      <Composition id="BW-F-ToGo-2" component={ToGo2} {...feed} />
      <Composition id="BW-F-ToGo-3" component={ToGo3} {...feed} />
      <Composition id="BW-F-ToGo-4" component={ToGo4} {...feed} />
      <Composition id="BW-F-Cumple-1" component={Cumple1} {...feed} />
      <Composition id="BW-F-Cumple-2" component={Cumple2} {...feed} />
      <Composition id="BW-F-HumorCafecito" component={HumorCafecito} {...feed} />
      <Composition id="BW-F-Foto-1" component={Foto1} {...feed} />
      <Composition id="BW-F-Foto-2" component={Foto2} {...feed} />
      <Composition id="BW-F-Foto-3" component={Foto3} {...feed} />
      <Composition id="BW-F-Foto-4" component={Foto4} {...feed} />
      <Composition id="BW-F-EllaHablo" component={EllaHablo} {...feed} />
      <Composition id="BW-F-Cowork-1" component={Cowork1} {...feed} />
      <Composition id="BW-F-Cowork-2" component={Cowork2} {...feed} />
      <Composition id="BW-F-Cowork-3" component={Cowork3} {...feed} />
      <Composition id="BW-F-Cowork-4" component={Cowork4} {...feed} />
    </Folder>
    <Folder name="BW-Stories">
      <Composition id="BW-S-ToGoDulce" component={StToGoDulce} {...story} />
      <Composition id="BW-S-Cumple" component={StCumple} {...story} />
      <Composition id="BW-S-Calculos" component={StCalculos} {...story} />
      <Composition id="BW-S-Emergencia" component={StEmergencia} {...story} />
      <Composition id="BW-S-HoraCafe" component={StHoraCafe} {...story} />
      <Composition id="BW-S-Cowork" component={StCowork} {...story} />
      <Composition id="BW-S-Dieciocho" component={StDieciocho} {...story} />
      <Composition id="BW-S-Strudel" component={StStrudel} {...story} />
      <Composition id="BW-S-Primavera" component={StPrimavera} {...story} />
      <Composition id="BW-S-HumorToGo" component={StHumorToGo} {...story} />
      <Composition id="BW-S-Plateada" component={StPlateada} {...story} />
    </Folder>
  </>
);

registerRoot(Raiz);
