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

## Corregido el 15-09-2026 (prueba del carrusel de Masisa)

Seis cosas que sólo aparecen cuando se arma un carrusel de punta a punta. Están
en el CSS con su medición; el detalle, en `out/ebema/20260915_grilla_masisa_prueba/BRIEF.md`.

1. La **caja roja se ajusta a su propio texto**, no al ancho del titular entero.
2. Una caja de **dos renglones es un solo rectángulo**, no dos pegados.
3. El logo se escala **por su anillo rojo, no por el archivo**: `width:118.6` dejaba
   el rojo en 94,1 × 97,4, un 20 % corto. Ahora la firma va a 148,0 con padding 57,2.
4. **Cápsula blanca de la bajada** de la portada, que no estaba medida.
5. La **flecha se dibuja en CSS** — `img/flecha.png` nunca existió.
6. El botón del cierre decía **«Cotiza porwhatsapp»**: `flex` se come el espacio suelto.

El **anillo EBEMA** está ahora en dos versiones con alfa, reconstruidas desde
`logo_ebema_circulo.png` (que viene RGB con fondo blanco):
`logo_ebema_anillo_claro.png` (texto gris, para la cápsula) y
`logo_ebema_anillo_oscuro.png` (texto blanco, para el cierre sobre foto).
Conviene pedirle a Paulina el PNG oficial con transparencia: el contorno
reconstruido queda con algo de ruido.

`build_carrusel_EJEMPLO_masisa.py` es un carrusel real completo, con el brief
citado lámina por lámina. Es la mejor plantilla para el mes siguiente.

## Lo que falta

- **Logos de los proveedores.** Sin ellos la cápsula de co-marca queda coja.
  Se dejan en `raw/ebema/3-logos-y-packshots/` y de ahí pasan a
  `img/proveedores/`, que sí viaja en el repo. La lista de los 16 que usa la
  cuenta y el estado de cada uno están en `img/proveedores/LEEME.md`.
  **Masisa ya está**, recortado de una pieza publicada (falta el vectorial).
- **`clients/ebema/reglas.yaml`**: sin él `qa/motor.py --marca ebema` se niega a
  correr, y EBEMA es la marca de referencia del estudio. Las cifras de §4-bis ya
  están verificadas por código en el `qa.py` del lote de Masisa: hay que llevarlas
  al motor.
- Generadores de las familias **B** y **C** — hoy sólo está el de carrusel. Sus
  medidas ya están en el CSS, falta el script.
- Los **reels**: la gramática de motion está medida (§4-bis) pero el reel se arma en
  Remotion, no acá.
