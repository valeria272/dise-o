#!/bin/bash
# Fondos IA · RONDA 2 (Constanza Lizana, comentarios en Drive del 02-10-2026).
# Los originales de la ronda 1 se conservan; estos salen con sufijo propio.
#   pd_3c       «WTF esta foto… arréglala»: la pareja quedaba DETRÁS del mesón, que va contra el muro.
#   al_3b       «no me tinca ahí el spot… quizás más a la sombra»: el sofá bajo la pérgola.
#   al_4b       «falta el techo en el quincho para que sea igual al original».
#   m1_cierre_b «eliminemos ese faro»: edición mínima sobre la misma foto.
#   m2_cierre_b «falta el techo original y se cerraría un poco la boca a la tipa».
cd "$(dirname "$0")/../../../.."
PY=~/copylab-venv/Scripts/python.exe
F=out/rentas/20261100_grilla_noviembre/fondos
REAL="Photorealistic documentary photo, natural Chilean people with natural skin, candid, not posed, no text, no logos, no brands, no watermark."
Q="Keep the real architecture of the reference EXACTLY as it is: the white slatted pergola ROOF covering the whole barbecue area and standing on its white posts, the brick grills UNDER that pergola roof, the grey concrete wall behind, the artificial grass, the two lamp posts and the white surrounding buildings with red and blue details. Same camera position and framing as the reference, seen from outside the pergola. Do not invent landscape, do not remove the pergola roof."
gen(){ $PY scripts/magnific.py seedream "$2" --aspecto "$3" --refs $4 --out "$F/ia/$1.png" > "$F/ia/$1.log" 2>&1; echo "[$1] $(tail -1 $F/ia/$1.log)"; }
S="${1:-}"
run(){ if [ -z "$S" ] || [ "$S" = "$1" ]; then gen "$@" & fi; }

run pd_3c "This is the real kitchen of an apartment in the Valle Altiplanico condominium. Keep the kitchen EXACTLY: the granite counter runs along the WALL, with light wood cabinets below and above it, the gas hob on the counter, the built-in microwave in the upper cabinets and the oven below the counter. Wider view from the kitchen aisle. A young couple in their 30s stands in the aisle IN FRONT of the counter, on the camera side, side by side, turned three-quarters towards the camera, the counter and cabinets are BEHIND them. They calmly read together a short printed rental contract that the man holds, relaxed, gentle smiles. Nobody is behind the counter, nobody is inside the furniture: physically coherent bodies, natural hands with five fingers, legs standing on the floor. The paper has no legible text. The couple is in the LOWER 60% of the frame, on the right half; the upper part of the frame is the calm upper cabinet wall. Soft natural daylight. $REAL" carrusel "$F/refs/cocina.jpg"

run al_3b "This is the real barbecue area (quincho) of a condominium in Calama, Chile. $Q Warm late-afternoon light. A simple wooden outdoor sofa is placed UNDER the pergola roof, fully inside its SHADE, at the left side of the pergola next to the left brick grill, standing on the floor under the roof, clearly not out on the open sunny lawn and not blocking the grills. A woman in her 30s is arranging colorful cushions and a light linen throw blanket on it, a cozy shaded corner. The woman and the sofa are in the LOWER HALF of the frame; the upper 40% of the frame is calm sky above the pergola. $REAL" carrusel "$F/refs/quincho.jpg"

run al_4b "This is the real barbecue area (quincho) of a condominium in Calama, Chile. $Q Sunset, warm golden light, a few warm string lights hanging under the pergola roof. A group of six friends and family of different ages, with one child, gathered around a wooden table that stands UNDER the pergola roof, right in front of the brick grills, laughing gently and sharing food and drinks. The white pergola roof is clearly visible ABOVE the people and above the grills, exactly as in the reference. Group in the LOWER HALF of the frame, medium-wide shot; the upper 35% of the frame is calm warm sky above the pergola roof. $REAL" carrusel "$F/refs/quincho.jpg"

run m1_cierre_b "Keep this photo EXACTLY unchanged: same family, same faces, same clothes, same pergola, same brick grills, same table, same framing and light. The ONLY change: remove the dark lamp post that stands on the right side in front of the dining table and the little girl. Fill in naturally what was hidden behind it (the wooden table, the chair, the girl, the grass and the pergola). Do not add anything, do not change anything else. Photorealistic, no text." wide "$F/ia/m1_cierre.png"

run m2_cierre_b "This is the real barbecue area (quincho) of a condominium in Calama, Chile. $Q Sunset, warm golden light, a few warm string lights under the pergola roof. A family (grandmother, mother, father and a boy) relaxing together at a wooden table that stands UNDER the pergola roof, in front of the brick grills, drinks and food on the table, cozy. Everyone has a calm, gentle, closed-mouth smile; nobody laughs with the mouth wide open. The white pergola roof is clearly visible above the family and above the grills, exactly as in the reference. Wide shot: the family occupies the RIGHT HALF of the frame; the LEFT 45% of the frame is calm (grass, pergola post and warm sky) because text goes there. $REAL" wide "$F/refs/quincho.jpg"

# al_3b salió bien ubicado pero lejos. Una toma más cerrada (al_3c) volvió a sacar el sofá al sol:
# se descartó. Se usa al_3b escalada 2× (magnific.py escalar --escala 2 --precision) y recortada.

# m2_cierre_b quedó bien (techo y sonrisas calmas) pero con un farol pegado a la familia:
# mismo criterio que el comentario del cierre 03-11 («eliminemos ese faro… incómodo para la familia»).
run m2_cierre_c "Keep this photo EXACTLY unchanged: same family, same faces, same clothes, same pergola roof, same brick grills, same table, same framing and light. The ONLY change: remove the dark lamp post that stands on the right side of the frame next to the man. Fill in naturally what was hidden behind it (the pergola, the wall, the grass and the sky). Do not add anything, do not change anything else. Photorealistic, no text." wide "$F/ia/m2_cierre_b.png"
wait
