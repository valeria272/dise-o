# Carruseles reales, con el criterio escrito

Dos portadas de la grilla de octubre 2026, aprobadas por Paulina el 15-09-2026.
**Son la mejor plantilla para el mes siguiente**: traen el brief citado lámina por
lámina y, en los comentarios, por qué el texto se repartió así y no de otra forma.

| Archivo | Qué es |
|---|---|
| `masisa_octubre.py` | Carrusel completo de 5 láminas (melamina y cantos) |
| `masisa_octubre_BRIEF.md` | Su brief verbatim, el QA y **los prompts** (§ Los prompts — sólo el de la L2 hasta el 16-09-2026; las otras 4 se generaron sin anotarlo y no se pueden reproducir) |
| `etersol_octubre.py` | Sólo la portada (pasto sintético) |

## Para rehacer una pieza

Los lotes con las fotos y los PNG entregables viven en `out/`, que **no viaja en
git** (pesan 6 MB por foto):

- `out/ebema/20260915_grilla_masisa_prueba/`
- `out/ebema/20260915_grilla_etersol_prueba/`

Si hace falta reconstruirlas desde cero, los prompts de Magnific están escritos en
`masisa_octubre_BRIEF.md`. El logo del proveedor sale de `../img/proveedores/`.

```bash
cp -r clients/ebema/sistema-grilla out/ebema/<AAAAMMDD>_<lote>/editables
cd out/ebema/<AAAAMMDD>_<lote>/editables
cp ../../../../clients/ebema/sistema-grilla/ejemplos/masisa_octubre.py build_carrusel.py
# se cambian sólo los textos del brief, las fotos y el logo del proveedor
python build_carrusel.py && bash render.sh <slug>
python ../../../../clients/ebema/sistema-grilla/qa_portada.py salida
```

## Lo que NO se toca al copiarlos

Todo lo que está bajo `.portada` en `base-grilla.css` y el bloque `AJUSTE` del
generador: son las once rondas de corrección de Paulina sobre la portada de Masisa.
Las reglas están en **§4-bis** del manual de la marca, con su medición al lado.
