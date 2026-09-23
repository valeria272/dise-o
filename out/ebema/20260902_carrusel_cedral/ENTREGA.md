# EBEMA — carrusel Cedral · propuesta de rediseño

**Fecha:** 02-09-2026 · **Pieza:** grilla septiembre 2026, **slide 6**
(`docs.google.com/presentation/d/1wHJf4hxDgaitqQJGB2ylc0G0WcRFPZ_lJrYUFqE8dw0`)
**Producto:** revestimiento de fibrocemento Cedral (Pizarreño/Romeral) ·
**Pilar:** Proveedores · **Formato:** 5 láminas de carrusel, 1080×1350 (4:5)

Se entregan **dos rutas** sobre el mismo contenido. Los textos son **verbatim del
brief**: no se agregó ni se quitó una palabra.

---

## Qué le falta a la versión que está hoy en la grilla

Mirando las 5 láminas juntas, no como piezas sueltas:

1. **Las cinco se ven iguales.** Foto oscura + bloque de texto centrado, cinco
   veces. En el feed el carrusel se lee como una sola mancha y no invita a
   deslizar.
2. **No hay señal de avance.** Nada indica que hay 5 láminas ni en cuál va el
   lector.
3. **La portada no muestra el argumento.** El gancho de Cedral es *fachada
   gastada → fachada nueva*, y la portada actual sólo muestra el resultado.
4. **El texto flota sobre la foto** en todas: compite con la imagen en vez de
   apoyarse en ella.

---

## Ruta A — «Método» · cambio contenido

Conserva la gramática de Paulina intacta (marco blanco, caja de logo saliendo del
borde, titular centrado con la caja roja detrás de la 2ª línea completa y de la
mitad de la 1ª, bajada, botón sin sombra). Lo que suma:

| Qué | Por qué |
|---|---|
| **Portada partida antes/después** con corte rojo de 12 px y píldoras `ANTES` / `DESPUÉS` | Pone el argumento de venta en la primera lámina |
| **Caja roja del número**, espejo exacto de la caja del logo (152×186, `top:0`, radio inferior 14) | El carrusel se lee como 3 razones numeradas. La cifra va en **Helvetica Bold**, como manda la regla |
| **Barra de avance de 5 tramos** en el lugar de los puntitos, sobre la línea del marco | Los puntitos decoran; esto informa. Mismo lenguaje, misma esquina |
| **Cierre en rojo plano** con las planchas en panel de radio 20 y borde blanco | Cierra el carrusel con la marca, no con otra foto oscura más |

**Riesgo bajo.** Ningún elemento del sistema se movió de sitio.

## Ruta B — «Zócalo» · cambio de aire

Rompe el centrado. La foto queda limpia de arriba a 970 px y el texto baja a un
zócalo blanco de 380 px alineado a la izquierda: kicker rojo, titular Raleway
Black en negro, bajada en el gris institucional `#6D6F72`, y el número de paso en
Helvetica Bold rojo al 13 % como ancla visual. La barra de avance monta a caballo
sobre el borde del zócalo. El cierre da vuelta el zócalo: rojo pleno, texto y
botón blancos.

**Riesgo medio.** Es el cambio real de aire, y es el que hay que consultarle a
Paulina: el sistema actual compone **centrado sobre la foto**, y esta ruta compone
**alineada a la izquierda sobre blanco**.

---

## Lo que NO se movió, en ninguna de las dos

- Rojo **`#EC1C23`** único — verificado píxel a píxel en las 10 piezas.
- **Raleway** Black / ExtraBold / SemiBold + **Helvetica Bold en toda cifra**
  (`01`, `02`, `03`, `18`), incluido dentro del titular.
- **Logo pegado al borde superior** (`top:0`), nunca flotando.
- **Botón sin sombra.**
- Marco blanco 3 px, radio 20, inset 62 / 77 / 71 (Ruta A).
- Respiro ≥ 50 px entre texto y marco; zona segura inferior de Meta libre.
- Todo sale de `clients/ebema/sistema/base.css` + la capa `carrusel.css`. Cero
  estilos sueltos en el HTML.

## Lo que hay que resolver antes de producir

1. **⛔ Falta el logo de Cedral.** No está en el kit oficial ni en el banco. Acá
   va escrito como kicker tipográfico (`CEDRAL · REVESTIMIENTO DE FIBROCEMENTO`).
   Hay que pedírselo a Paulina o al proveedor y armar el lockup EBEMA + CEDRAL.
2. **Las fotos son IA** (Nano Banana Pro), generadas con las reglas de imagen de
   Paulina: plano amplio, ropa de trabajo, obra ordenada, sin marcas legibles.
   Si Pizarreño/Romeral tiene material propio de Cedral, manda ese.
3. **Confirmar el `18` en Helvetica Bold** dentro del titular. La regla dice
   *toda* cifra; en la pieza actual de la grilla se ve en Raleway. Decide Paulina.
4. Los kickers `01 · INSTALACIÓN` / `02 · DURABILIDAD` / `03 · TERMINACIÓN` son
   míos, no del brief. Si el cliente los quiere fuera, se borran sin tocar nada más.

---

## Cómo se reproduce

```bash
cd out/ebema/20260902_carrusel_cedral/editables
python3 build.py      # → 10 HTML
bash render.sh        # → ../feed/*.png con Chrome headless
```

Los fondos se regeneran con
`scripts/ebema-cedral-fondos.py` (Nano Banana Pro vía Freepik, 4:5 · 2K).
El par antes/después de la portada usa el «después» como referencia para que la
casa, el encuadre y el ángulo sean los mismos.

| Archivo | Qué es |
|---|---|
| `feed/rutaA_L1..L5_feed.png` | Ruta A — «Método» |
| `feed/rutaB_L1..L5_feed.png` | Ruta B — «Zócalo» |
| `feed/_tira_A.jpg` · `_tira_B.jpg` | Las 5 láminas en fila, para mirar el carrusel completo |
| `editables/carrusel.css` | La capa nueva sobre `base.css` |
| `editables/build.py` | Los textos del brief y el armado |
| `fondos/` | Las 7 imágenes generadas |
