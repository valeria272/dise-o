#!/bin/bash
cd "/Users/Vale/Desktop/COPYLAB PROJECTS/EDITOR VIDEOS"
P=/Users/Vale/copylab-venv/bin/python3
for k in p03 p05 p06 p10 p13 p14 p15 p16; do
  pr=$($P -c "import sys; sys.path.insert(0,'out/copylab/posts16'); from prompts import P; print(P['$k'])")
  for v in a b; do
    $P scripts/magnific.py pro "$pr" --aspecto carrusel --resolucion 2K --out out/copylab/posts16/gen/$k-$v.png > out/copylab/posts16/gen/$k-$v.log 2>&1 &
  done
done
wait
