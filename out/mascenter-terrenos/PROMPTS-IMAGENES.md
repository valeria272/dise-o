# Imágenes de terreno — cómo se generaron

> ⚠️ **NO están en uso.** Se hicieron para el rediseño que se descartó el 02-09-2026.
> Los archivos siguen en `raw/mascenter-terrenos/ia/` por si se quieren sumar a la
> versión vigente. Esto queda escrito para poder reproducirlas o rehacerlas.

Las 3 imágenes de paños vacíos son **generadas con Magnific (Mystic)**, porque Más Center
no tiene fotos de terrenos disponibles y era el material que faltaba para esta página.
Van rotuladas «imagen referencial» en la propia landing.

Herramienta: `AGENTE CREATIVO RRSS/tools/magnific.py` · key en `~/.magnific_key`
Originales 2K en `raw/mascenter-terrenos/ia/` (no versionado).

```bash
P=/Users/Vale/copylab-venv/bin/python3
cd "COPYLAB PROJECTS/AGENTE CREATIVO RRSS"
```

## terreno-hero.jpg — la aérea del hero y el «antes» del comparador
`--aspect widescreen_16_9 --resolution 2k`
> Aerial drone photograph, golden hour, of a large empty vacant urban land plot on the
> corner of a wide main avenue in a Chilean city. Flat dry grass and bare earth, wire
> fence around the perimeter. Real traffic on the avenue, new low-rise residential
> neighbourhood and apartment blocks surrounding it, Andes mountain range visible far in
> the hazy background. Documentary real-estate photography, natural colours, high detail,
> no text, no signs, no logos, no people

## terreno-esquina.jpg — ejemplo «esquina con flujo y semáforo»
`--aspect widescreen_16_9 --resolution 2k`
> Elevated photograph from across the street of an empty fenced vacant lot at a busy urban
> intersection in Chile, mid afternoon. Dry grass, gravel, concrete kerb, traffic lights
> and cars passing, pedestrians on the sidewalk, consolidated residential buildings behind.
> Overcast bright natural light, documentary real-estate photography, realistic, no text,
> no signs, no logos

## terreno-avenida.jpg — ejemplo «frente a avenida principal»
`--aspect widescreen_16_9 --resolution 2k`
> Ground level wide photograph of a large vacant commercial land plot fronting a busy four
> lane avenue in Chile, seen from the opposite sidewalk. Empty flat terrain behind a simple
> wire fence, light poles, bus stop, cars and a bus in motion blur, dense residential
> neighbourhood and hills in the distance. Late afternoon warm light, documentary
> real-estate photography, realistic, no text, no billboards, no logos

## Una que se descartó
`terreno-residencial.png` (4:5, terreno junto a loteo nuevo) salió con el primer plano
arenoso leyéndose como **duna costera** y las casas con aire europeo. No se usó.

## proyecto-aereo.jpg — el «después» del comparador
No es IA: es el render aéreo de Algarrobal que el cliente ya aprobó, recortado al mismo
ratio que `terreno-hero.jpg` (2000×1116) para que el comparador calce.
