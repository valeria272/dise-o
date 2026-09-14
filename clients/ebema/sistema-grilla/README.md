# Sistema de producción — EBEMA GRILLA

> ⚠️ **Esto NO es el sistema de paid.** Para paid está `clients/ebema/sistema/`.
> Grilla se organiza por **familia de contenido**; paid, por submarca. La regla y la
> matriz están en **§0** del manual de la marca; la gramática medida, en **§4-bis**.

| Archivo | Qué es |
|---|---|
| `base-grilla.css` | **El sistema.** Toda la geometría medida sobre las referencias de septiembre 2026 |
| `build_carrusel.py` | Generador de carrusel (familia A). Se copia al mes nuevo y se le cambian **sólo los textos y las fotos** |
| `render.sh` | HTML → PNG con Chrome headless. Diseña a 1080, entrega a 2250 |
| `fonts/` | Raleway (OFL) + Helvetica Bold del kit del cliente |
| `img/` | Logos oficiales y el anillo EBEMA |

## Lienzo

Se diseña a **1080** y se entrega a **2250**, que es como llegan las piezas de Paulina:

| | diseño | entrega |
|---|---|---|
| feed / carrusel | 1080 × 1350 | **2250 × 2813** |
| story / reel | 1080 × 1920 | **2250 × 4000** |

`render.sh` aplica `--force-device-scale-factor=2.0833` (= 2250 / 1080). No cambies
las medidas del CSS para «hacerla más grande»: se cambia la escala del render.

## Las tres familias

**A · producto en stock** — carrusel de 5 láminas en co-marca con el proveedor.
Arco fijo: problema → causa → solución → **tip pro** → cierre.

**B · información de servicio** — horarios y direcciones. El logo va **centrado
arriba**, que es la única excepción del sistema, y los horarios en dos barras rojas.

**C · invitación a plataformas** — Click, catálogo online, ebema.cl. Dos registros:
con lockup Click (C1) o con la firma EBEMA (C2).

## Uso

```bash
cp -r clients/ebema/sistema-grilla out/ebema/<AAAAMMDD>_grilla_<mes>/editables
cd out/ebema/<AAAAMMDD>_grilla_<mes>/editables
# poner las fotos en fotos/ y el logo del proveedor en img/
python build_carrusel.py       # cambiar sólo el diccionario CARRUSEL
bash render.sh
```

## Lo que está calibrado contra la referencia

La lámina de cierre se verificó midiendo el render contra `ebema_c_cedral5.png`:

| Elemento | Referencia | El render | Desvío |
|---|---|---|---|
| Botón WhatsApp | 653,8 × 79,7 · y 916,3 | 653,8 × 79,7 · y 916,3 | **0** |
| Anillo EBEMA | 298,6 × 307,2 · cx 545,5 | 298,1 × 307,2 · cx 545,8 | **< 1 px** |

> El anillo del PNG no llena su lienzo: hay que escalar el `<img>` a **376,3** para
> que el rojo mida 298,6. Está resuelto en el CSS; no lo toques a ojo.

## Lo que falta

- **Logos de los proveedores** (Cedral, Cintac, Novoplast, Surpol, Toro, Polpaico,
  CMPC, VH…). Sin ellos la cápsula de co-marca queda coja. Hay que pedírselos a
  Paulina o sacarlos de los editables.
- El **PNG de la flecha** del pie de portada (`img/flecha.png`).
- Generadores de las familias **B** y **C** — hoy sólo está el de carrusel. Sus
  medidas ya están en el CSS, falta el script.
- Los **reels**: la gramática de motion está medida (§4-bis) pero el reel se arma en
  Remotion, no acá.
