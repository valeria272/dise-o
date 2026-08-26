---
description: Extrae el ADN de una marca desde los editables del diseñador — /adn <marca> <id-carpeta-drive>
---

Extrae el sistema real de una marca desde los **editables empaquetados** del
diseñador. Es la fuente más fiel que existe: dice las tipografías exactas, las
medidas de mesa de trabajo y de dónde salió cada imagen.

## 1. Ubicar el material
Lista la carpeta de Drive de `$ARGUMENTS`. Busca:
- Carpetas `*_Carpeta` → son paquetes de Illustrator. Adentro: `Fonts/`, `Links/` y
  un **`<nombre> Informe.txt`** ← **este archivo es el oro**
- Carpeta de tipografías
- Plantillas de márgenes o guías
- Sesiones de fotos y sus ediciones

## 2. Leer el Informe.txt — lo que entrega
| Sección | Qué sacar |
|---|---|
| **Dimensiones de la mesa de trabajo** | El formato master real (ojo: suele ser 2×) |
| **Fuentes protegidas no empaquetadas** | Las de Adobe Fonts — hay que activarlas, no vienen |
| **Fuentes** | Las que sí vienen en `Fonts/`, con su formato |
| **Enlaces no disponibles** | Las rutas del disco de la diseñadora → revela su estructura de carpetas y los bancos de foto |
| **Imágenes enlazadas** | Nombre, tipo, resolución y tamaño de cada imagen usada |

> Los nombres de archivo de las imágenes IA **traen el prompt adentro**
> (`magnific_reemplaza-el-muffin-de-la_XXXX.png`). Ahí está el método de la
> diseñadora: qué le pide a la IA y qué conserva de la foto real.

## 3. Medir las plantillas de márgenes
Si hay PNG de márgenes o guías, **no los mires a ojo: mídelos**.
```python
from PIL import Image; import numpy as np
im = Image.open(f).convert("RGBA"); a = np.array(im); vis = a[...,3] > 8
# bloques de contenido por fila, bbox de cada uno, y escalar a lienzo de 1080
```
Anota posición, alto, ancho y si va centrado. Escala todo a 1080 de ancho.

## 4. Instalar y verificar las fuentes
Copia las que tengan licencia a `public/assets/<marca>/fonts/`. **Verifica que
rendericen** con PIL antes de darlas por buenas: acentos, Ñ, signos y números.

## 5. Escribir
- Geometría medida → `src/brand/<marca>.ts` y `clients/<marca>/marca.json`
- Método, flujo de imagen y pendientes → `clients/<marca>/CLAUDE.md`
- **Todo valor lleva su origen.** Si algo se dedujo y no se midió, decirlo.

## 6. Lo que NO se puede
Los `.ai` no se abren, y suelen pesar cientos de MB. Si hace falta la geometría
interna, pedirle a la diseñadora un PDF o un export de las mesas de trabajo.
