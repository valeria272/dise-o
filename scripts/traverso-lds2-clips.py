#!/usr/bin/env python3
"""«Los de siempre — THE ENTRANCE»: los 15 clips de la lista C (EDICION-THE-ENTRANCE.md).
Kling 2.5 Pro por defecto; Kling 2.1 Pro cuando hay frame final (image_tail).
    python3 scripts/traverso-lds2-clips.py --solo c01 c02
Salida: public/assets/traverso/lds2/clips/<clip>.mp4 (5 s cada uno; el montaje recorta)."""
import argparse, os, subprocess, sys
RAIZ=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A=os.path.join(RAIZ,'public','assets','traverso','lds2'); K=os.path.join(A,'keyframes'); C=os.path.join(A,'casting','LOCKED')
OUT=os.path.join(A,'clips'); VIDEO=os.path.join(RAIZ,'scripts','magnific-video.py')
LOCK=("The characters keep EXACTLY their design: real Traverso bottle body, nozzle cap on top, no face, "
      "white round gloves, very short legs, big feet in the product colour, long black tuxedo, white shirt, "
      "bow tie. Yellow left, gold centre, red right. No morphing, no new characters, no text.")
STILL="Locked camera on a tripod, no camera movement, no zoom. "
# clip: (inicio, fin, prompt, coda, modelo)
P={
 'c01':(f'{K}/e01_macro_boquilla.png',None,"Extreme macro of the gold nozzle cap. The spotlight above SWITCHES ON at the very start (from dark to lit in a few frames) and then holds; subtle haze drifting; the cap does not move. "+STILL+LOCK,None,'kling-v2-5-pro'),
 'c02':(f'{K}/e02_macro_guante.png',None,"Extreme macro: the white glove pinches the satin lapel and adjusts it in one small precise movement, then holds. "+STILL+LOCK,None,'kling-v2-5-pro'),
 'c03':(f'{K}/k02_pies.png',None,"Floor-level macro: the three pairs of big mascot feet take slow heavy steps towards the lens, each foot landing flat on the wet floor with reflections, gold feet closest. Camera on the floor, locked. "+LOCK,'fisica','kling-v2-5-pro'),
 'c04':(f'{K}/k03_entrada.png',None,"The three characters walk towards the camera in perfect sync, slow and confident, arms swinging slightly, while the camera dollies BACK slowly keeping them in frame. Spotlights steady. "+LOCK,'fisica','kling-v2-5-pro'),
 'c05':(f'{K}/k04_suave.png',None,"The yellow character calmly adjusts one cuff of his tuxedo with the other white glove, one small movement, then holds still. "+STILL+LOCK,None,'kling-v2-5-pro'),
 'c06':(f'{K}/k05_tradicional.png',None,"The gold character adjusts his black bow tie with both white gloves in one slow confident movement, then lowers the hands. "+STILL+LOCK,None,'kling-v2-5-pro'),
 'c07':(f'{K}/k06_ketchup.png',None,"The red character smooths his lapel with one white glove in a dry precise movement, then stands very straight and still. "+STILL+LOCK,None,'kling-v2-5-pro'),
 'c08':(f'{K}/e07a_falso_reveal.png',None,"The three characters stand still; the gold one in the centre slowly raises both white gloves to his lapels and grips them as if about to open the jacket, then freezes. Tension. "+STILL+LOCK,None,'kling-v2-5-pro'),
 'c09':(f'{C}/TRIO_MASTER_FINAL.png',f'{K}/k07_reveal.png',"THE REVEAL: the three characters raise their white gloves to their lapels at the same time and pull their long tuxedo jackets wide open simultaneously in one decisive movement, revealing the real Traverso bottles and labels underneath, then hold the pose proudly. Locked frontal camera. "+LOCK,'fisica','kling-v2-1-pro'),
 'c10':(f'{K}/e12a_macro_amarillo.png',None,"Product macro: a warm highlight glides slowly along the yellow nozzle cap and shoulder of the bottle as the light moves; the bottle does not move. "+STILL,None,'kling-v2-5-pro'),
 'c11':(f'{K}/e12b_macro_dorado.png',None,"Product macro: a warm highlight sweeps slowly across the gold bottle and its vintage label; the label stays crisp and unchanged; the bottle does not move. "+STILL,None,'kling-v2-5-pro'),
 'c12':(f'{K}/e12c_macro_rojo.png',None,"Product macro: a warm highlight travels slowly over the glossy red bottle and cap; label unchanged; the bottle does not move. "+STILL,None,'kling-v2-5-pro'),
 'c13':(f'{K}/k08_hacia_copylab.png',None,"Seen from behind, the three characters walk towards the glowing GRUPO COPYLAB entrance while the camera FOLLOWS them forward at hip height; the door opens and the warm light grows brighter and brighter until it floods the frame. "+LOCK,'fisica','kling-v2-5-pro'),
 'c14':(f'{K}/k09_nueva_casa.png',None,"Inside the meeting room the three characters walk in from the back and cross the frame from right to left while the camera tracks laterally with them; at the end the red one passes very close to the lens so that his black tuxedo fills the whole frame. "+LOCK,'fisica','kling-v2-5-pro'),
 'c15':(f'{K}/e10_reunion.png',None,"The three characters sit dead serious at the table: the gold one in the centre opens the black folder, the yellow one lifts his coffee cup a few centimetres and sets it down, the red one stays still in front of his laptop. Warm natural light, nothing else moves. "+STILL+LOCK,None,'kling-v2-5-pro'),
}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--solo',nargs='*'); ap.add_argument('--rehacer',action='store_true'); a=ap.parse_args()
    os.makedirs(OUT,exist_ok=True)
    for k in (a.solo or P):
        ini,fin,prompt,coda,modelo=P[k]; out=os.path.join(OUT,f'{k}.mp4')
        if os.path.isfile(out) and not a.rehacer: print('·',k,'ya existe'); continue
        for f in (ini,fin):
            if f and not os.path.isfile(f): sys.exit(f'✗ {k}: falta {f}')
        cmd=[sys.executable,VIDEO,ini,'--out',out,'--prompt',prompt,'--dur','5','--modelo',modelo]
        if fin: cmd+=['--fin',fin]
        if coda: cmd+=['--coda',coda]
        print('===',k); subprocess.run(cmd,check=True)
if __name__=='__main__': main()
