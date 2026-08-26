# Sistema de producción EBEMA

El sistema gráfico calibrado, promovido desde
`EBEMA/outputs/20260820_paid_septiembre/editables/` (v8, 21-08-2026), que es la
versión que replica 1:1 el esquema de agosto de Paulina.

| Archivo | Qué es |
|---|---|
| `base.css` | **El sistema.** Toda la geometría medida. Los tres esquemas (sucursal / `.click` / `.spc`) |
| `build_ejemplo.py` | Generador de referencia (septiembre 2026). Se copia al mes nuevo y se le cambian **sólo las listas de texto** |
| `render.sh` | HTML → PNG con Chrome headless. Receta validada, sin `--user-data-dir` |
| `fonts/` | Raleway (OFL) + Helvetica Bold del kit del cliente |
| `img/` | Logos oficiales y chips de tonos SPC |

## Uso

```bash
DEST="../../../../EBEMA/outputs/$(date +%Y%m%d)_paid_octubre/editables"
mkdir -p "$DEST" "$DEST/../feed" "$DEST/../story" "$DEST/../fondos"
cp base.css render.sh "$DEST/"; cp -r fonts img "$DEST/"
cp build_ejemplo.py "$DEST/build.py"
# editar las listas SUCURSALES / CLICK / TONOS de build.py con los textos del brief
python3 "$DEST/build.py" && bash "$DEST/render.sh"
```

## Reglas

- Si una pieza necesita algo que `base.css` no tiene: primero verificar contra una
  referencia aprobada. Si es legítimo, **agregarlo al CSS** y documentarlo en
  `clients/ebema/CLAUDE.md`. Nunca con `style=""` suelto en el HTML.
- `num()` en `build.py` envuelve toda cifra en Helvetica Bold. Un número escrito
  fuera de esa función queda en Raleway y está mal.
- `Helvetica-Bold.ttf` viene del kit que entregó la diseñadora del cliente
  (licencia de Ebema). No redistribuir fuera del proyecto.
