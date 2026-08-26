---
description: Control de calidad de piezas antes de entregar — /qa <marca o ruta>
---

**Carga primero la skill `direccion-de-arte`** — el §3 «qué hace vergonzosa una
pieza» es el checklist duro de este comando, y el §4 trae las herramientas:
`scripts/ver-pieza.py` para mirarlas todas juntas (o un video cuadro a cuadro).

Control de calidad sobre lo indicado en `$ARGUMENTS` (una marca, una carpeta o un
archivo). **Sé duro.** El objetivo es encontrar problemas, no aprobar.

1. Lee `clients/<marca>/CLAUDE.md` — secciones "QA obligatorio" y "Errores ya
   cometidos" — y `marca.json`.
2. Abre **cada** pieza y una referencia aprobada del cliente, y compáralas.
3. Revisa punto por punto el checklist de la marca. Además, transversal:

```
[ ] Colores exactos de marca.json (muestrear el píxel, no confiar en la vista)
[ ] Tipografías correctas por rol; cifras en la fuente de números de la marca
[ ] Logo: archivo oficial, versión correcta para ese fondo, posición del sistema
[ ] Zonas seguras Meta: 9:16 → 250 arriba / 340 abajo / 115 derecha; feed → 12% inferior
[ ] Respiro ≥60 px entre texto y cualquier borde, línea o elemento
[ ] Cero choques: texto vs marco, texto vs logo, texto vs decoración
[ ] Texto sobre zona libre de la foto, nunca sobre caras
[ ] Sin palabras huérfanas ni saltos de línea feos
[ ] Textos y CTA verbatim del brief — verificar contra el brief, no de memoria
[ ] Precios en CLP chileno ($9.900, punto de miles, sin decimales)
[ ] Legales presentes si hay promoción
[ ] Packshots reales, no espejados, sin halo ni sombra baked-in (zoom 3×)
[ ] PROPORCIÓN del packshot: ancho/alto final == ancho/alto del archivo original
[ ] Si la marca tiene material regulado: legal obligatorio presente, claims literales,
    sellos/premios correctos para ese producto y esa cosecha
[ ] Formato y medida correctos según marca.json
[ ] Nomenclatura de archivos correcta
[ ] Si la pieza es de una sucursal/sede: la foto es de ESA sucursal
```

4. Informa con una tabla: pieza · hallazgo · gravedad (🔴 bloquea / 🟡 arreglar /
   🟢 menor) · qué hay que hacer.
5. Si hay 🔴, **arréglalos** y vuelve a correr el QA.
6. Si un hallazgo revela un hueco del sistema (una regla que no estaba escrita),
   agrégala al manual de la marca.

Nunca reportes "todo bien" sin haber abierto las piezas y comparado contra la
referencia.
