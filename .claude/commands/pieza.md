---
description: Produce una pieza de cliente con el sistema de marca — /pieza <marca> <qué necesitas>
---

Vas a producir una pieza para el cliente indicado en `$ARGUMENTS`.

**No improvises nada de la marca.** Todo está escrito. Sigue el pipeline exacto.

## ⓪ Compuerta de material — antes de todo lo demás

**Nada de lo que sigue vale si el material no es lo que dice ser.** El 25-08-2026
Revex se diseñó entero con 8 "referencias" que en realidad eran la página de login
de Google guardada con extensión `.jpg`, y Casablanca se replanteó contra una
carpeta de referencias que contenía piezas de **otra marca** (Between, la cafetería).
Ninguna de las dos cosas se vio, porque nunca se abrieron los archivos.

Antes de leer el brief:

1. **Valida que cada archivo sea una imagen de verdad** (cabecera, no extensión):
   ```bash
   /Users/Vale/copylab-venv/bin/python3 scripts/verificar-material.py raw/<marca>
   ```
   Cualquier archivo roto → volver a bajarlo. **No se sigue con menos material.**

2. **Arma una hoja de contacto y MÍRALA.**
   ```bash
   /Users/Vale/copylab-venv/bin/python3 scripts/hoja-contacto.py raw/<marca> \
       out/_verificacion/<marca>-material.png
   ```
   La abres tú y confirmas dos cosas: **(a)** que todas las piezas son de esta marca,
   **(b)** que reconoces la gramática. Si aparece algo de otro cliente, se saca.

3. **Muéstrale la hoja de contacto a la persona que pidió el trabajo** junto con el
   conteo de piezas válidas. Recién ahí se diseña.

Esta compuerta no se salta ni "porque es una pieza chica". Son 30 segundos contra
tres rondas rehechas.

---

## ① Cargar el sistema de la marca

1. Lee `docs/SISTEMA-DE-MARCAS.md` si aún no lo tienes en contexto.
2. Lee `clients/<marca>/CLAUDE.md` **completo**. Es el manual y manda.
3. Lee `clients/<marca>/marca.json` — colores, fuentes, formatos, geometría.
4. Mira las **referencias reales** del cliente (la ruta está en el manual, sección
   "Dónde está el material"). Si `raw/<marca>/` está vacío, bájalo del Drive antes
   de seguir — con IDs del manual.

Si la marca **no tiene** carpeta en `clients/`, para y dilo: hay que abrirla primero
con `/marca-nueva`. No inventes un sistema.

## ② Brief

Lee el brief donde el manual diga que vive (Sheet, Doc, celda, carpeta). Extrae
**verbatim**: enunciados, bajadas, CTAs, precios, códigos, legales, vigencias.

- Los textos en pantalla y los CTA **salen literales**. No inventes botones ni claims.
- Si falta un dato (precio, código, fecha), **no lo inventes**: anótalo como pendiente
  y sigue con el resto.
- Si el brief describe un estilo que contradice el sistema de la marca, **gana el
  sistema**. El brief manda el QUÉ, el sistema manda el CÓMO.

## ③ Material

Resuelve cada imagen bajando por la jerarquía (§2 de `docs/SISTEMA-DE-MARCAS.md`):
foto aprobada → banco curado → e-commerce → editables → pieza aprobada → IA.
Cada salto hacia abajo tiene que poder justificarse. Respeta las reglas de imagen
escritas en el manual de la marca.

## ④ Armar

Usa el pipeline de la marca (`clients/<marca>/sistema/` o su composición Remotion).
Copia el sistema al lote nuevo y cambia **sólo los textos**. No reescribas el CSS
ni la composición para una pieza puntual.

## ⑤ QA — no es opcional

Corre el checklist de "QA obligatorio" del manual de la marca, punto por punto.
Además, siempre:
- Zonas seguras Meta (`src/components/qa/SafeAreaAds.tsx`)
- Comparar la pieza al lado de una referencia aprobada
- Cero choques de texto con marcos, logos u otros elementos
- Cifras en la tipografía que la marca define para números
- Si hay recortes: revisar el borde con zoom 3×

**Si algo no pasa, arréglalo antes de mostrar.** No entregues con una nota de
"quedó un poco apretado".

## ⑥ Entregar

- Piezas en `out/<marca>/<periodo>/` (o donde diga el manual)
- Los editables junto a las piezas
- Un `ENTREGA.md`: qué es cada pieza, de dónde salió cada texto, qué quedó pendiente
- Subir a la carpeta de Drive del cliente si el manual dice cuál

## ⑦ Cerrar el ciclo

Si en el camino aprendiste algo de la marca —una corrección del cliente, una medida
que faltaba, un error que cometiste— **escríbelo en `clients/<marca>/CLAUDE.md`**
en el mismo commit. El manual es la memoria del estudio.
