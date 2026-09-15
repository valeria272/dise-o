# Instantáneas por API — base del diff de la ronda siguiente

Las grillas de **DT, PISO18 y QB** son Google Sheets nativos: no se pueden bajar como
`.xlsx` (el `--publico` de `scripts/bajar-de-drive.py` devuelve vacío) y por eso
`scripts/grilla-instantanea.py`, que trabaja sobre `.xlsx`, no les sirve.

La vía que sí funciona es la API de Sheets con el token del estudio (scope
`spreadsheets`, ya incluido en el llavero):

```bash
PYTHONIOENCODING=utf-8 ~/copylab-venv/Scripts/python.exe \
  scripts/sheet-instantanea.py <idDelSheet> clients/hilton/grillas/api/<marca>-<mes>-AAAAMMDD.json
```

Para detectar la ronda nueva se compara **por conjunto de cadenas** contra la
instantánea anterior: el comentario nuevo se **prepende** en la misma celda sobre el
viejo, así que un diff de línea no lo ve y la celda "modificada" tampoco se nota.

`between-septiembre-2026.md` sigue saliendo de `grilla-instantanea.py`: esa grilla
sí es un `.xlsx` de verdad.

| Archivo | Sheet |
|---|---|
| `dt-sept-*` | `1Egjr13KVuqM7JLXZ2YgRWHi4f6M07vhl2YG8B34bI6g` |
| `dt-oct-*` | `13yYW5QacnSRaV422SeBTgFVGwLN5mhTg0anDJzkvaK0` |
| `p18-sept-*` | `1kF9OwDflz3mFR_NAodu0Y0YJvQj5wbbmAlN7SdRTFAo` |
| `p18-oct-*` | `1bzTQWrTYPoSFwy2iIYCxTKuO-1XNbqT7Nk_vQz39JQA` |
| `qb-sept-*` | `1AYBy9NbXKImlcsCFVWGk-H90QZy65OpBJ9oKy5GRmVE` |
| `qb-oct-*` | `14bhpFxFDRidCiuCT0gSOKgQ8r06gHGLxZlYkzFNHxZc` |

> ⛔ `qb-oct-20260915.json` **es un duplicado literal de la grilla de septiembre**
> (fechas del 31-08 al 21-09 y la vista mensual dice «AGOSTO»). No se diseña nada
> de octubre de QB con ella.
