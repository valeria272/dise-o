#!/bin/bash
# Fondos IA de los MAILINGS de noviembre 2026 · Rentas — Seedream 5 Pro con foto REAL de referencia.
cd "$(dirname "$0")/../../../.."
PY=~/copylab-venv/Scripts/python.exe
F=out/rentas/20261100_grilla_noviembre/fondos
REAL="Photorealistic documentary photo, natural Chilean people with natural skin, candid, no text, no logos, no brands, no watermark."
Q="Keep the real architecture of the reference EXACTLY: the white pergola, the brick walls with built-in grills, the artificial grass, the lamp posts and the surrounding buildings. Do not invent landscape."
gen(){ $PY scripts/magnific.py seedream "$2" --aspecto "$3" --refs $4 --out "$F/ia/$1.png" > "$F/ia/$1.log" 2>&1; echo "[$1] $(tail -1 $F/ia/$1.log)"; }
gen m1_cierre "This is the real barbecue area (quincho) of a condominium in Calama, Chile. $Q Warm late-afternoon light. A family (mother, father and two kids) preparing an asado at the brick grill, the father turning meat on the grill, the kids helping set a wooden table. Wide shot: the family occupies the RIGHT HALF of the frame; the LEFT 45% of the frame is calm (grass, wall and sky) because text goes there. $REAL" wide "$F/refs/quincho.jpg" &
gen m2_banner "Keep this real photo almost unchanged: same framing, same architecture, same objects. Only change the light to a warm sunset: golden low sun, long soft shadows, warm pink-orange sky. Do not add or remove anything. No people. Photorealistic." wide "$F/refs/quincho.jpg" &
gen m2_ficha "Keep this real photo almost unchanged: same buildings, tree, playground and paths. Only change the light to a warm sunset golden hour: low warm sun, long shadows, warm sky, slightly darker and moodier ambience. Do not add or remove anything. No people. Photorealistic." carrusel "$F/refs/areas9628.jpg" &
gen m2_cierre "This is the real barbecue area (quincho) of a condominium in Calama, Chile. $Q Sunset, warm golden light, string lights on the pergola. A family (grandmother, parents and a child) relaxing and laughing together at a wooden table under the pergola, drinks and food, cozy. Wide shot: the family occupies the RIGHT HALF of the frame; the LEFT 45% is calm (grass and warm sky) because text goes there. $REAL" wide "$F/refs/quincho.jpg" &
wait
