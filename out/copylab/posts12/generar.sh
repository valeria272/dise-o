#!/bin/bash
cd "/Users/Vale/Desktop/COPYLAB PROJECTS/EDITOR VIDEOS"
P=/Users/Vale/copylab-venv/bin/python3
for k in p01 p02 p03 p05 p06 p07 p09 p10 p12; do
  pr=$($P -c "import sys; sys.path.insert(0,'out/copylab/posts12'); from prompts import P; print(P['$k'])")
  for v in a b; do
    $P scripts/magnific.py pro "$pr" --aspecto carrusel --resolucion 2K --out out/copylab/posts12/gen/$k-$v.png > out/copylab/posts12/gen/$k-$v.log 2>&1 &
  done
done
wait
ls out/copylab/posts12/gen/*.png | wc -l
