# LANDERA — Farmland Management

> **Estado al 03-09-2026: EN DEFINICIÓN.** El color primario y el logotipo todavía
> están en ronda con el cliente. **No se produce ninguna pieza hasta que cierren.**
> Lo que sí está hecho es el sistema medido (`marca.json`) y el plan del manual.

Marca nueva del cliente que antes era **C&D / CYD Management**. Administra campos
e inversión agrícola en Chile. Dos bajadas conviviendo: **Farmland Management**
(institucional, inversionista) y **Gestión Agrícola** (operación, terreno).

| Qué | Dónde |
|---|---|
| Sistema medido (colores, fuentes, geometría) | [`marca.json`](marca.json) |
| PDF de origen del cliente | `raw/landera/PROPUESTA-BASE-V2.pdf` |
| Variantes de color producidas | `scripts/landera_recolorear.py` |
| Versión invertida (fondo blanco, líneas verdes) | `scripts/landera_invertir.py` |
| Referencia de brandbook del estudio | `BRANDGUIDELINES_PIVOT.pdf` (20 láminas, mismo formato) |

---

## 1. Lo primero que hay que saber: este manual nació sobre otro

El PDF de Landera se armó **encima del archivo de Pivot**, y quedaron residuos
vivos adentro. No es una sospecha: los colores coinciden exactamente.

| Residuo | Qué es en realidad | Dónde quedó en Landera |
|---|---|---|
| `002151` | **Navy primario de Pivot** | 17 trazos de la pág. 4, las líneas sobre cada peso de Aptos |
| `5B5B5B` | **Gris terciario de Pivot** (su color de texto) | Cuerpo de texto de Landera **y** mal pegado en la ficha del terracota |
| CMYK `0/76/60/0` | El CMYK del gris de Pivot | Declarado como si fuera el del terracota |
| `1C4907` | Verde oscuro fuera de paleta | Un trazo suelto en la pág. 5 |

**Consecuencia práctica:** la ficha del **Color secundario Terracota** dice
`HEXADECIMAL 5B5B5B` y `RGB 91/91/91`, que es un gris. El cuadro que está al lado
pinta `#E4361F`. **El bueno es el del cuadro.** Hay que corregir la ficha antes de
cerrar el manual, o el cliente va a mandar a imprimir un gris.

Al construir el manual completo, **el archivo se arma de cero sobre la plantilla,
no duplicando el PDF actual** — si no, los residuos viajan otra vez.

---

## 2. El sistema, medido

Los valores completos están en `marca.json`. Lo esencial:

| Color | Hex | Rol |
|---|---|---|
| Verde oliva | `#687B5D` | primario |
| Terracota | `#E4361F` | secundario |
| Blue Grey | `#33353E` | terciario — es el color del logotipo en portada |
| Gris piedra | `#666461` | neutro |
| Crema | `#FAF1E8` | neutro / fondo de tapas |

**Tipografías:** **Barkentina** (única, sin variantes) para el logotipo y
**Aptos** en todas sus variantes para el resto.

> ⚠️ **Barkentina no está en ninguna máquina del estudio** y no viene con Office.
> Hay que pedirle el archivo a la diseñadora antes de componer una sola lámina.
> Aptos sí está: viene con Microsoft Office, en el bundle de Word.

> ⚠️ **Los subsets embebidos en el PDF no sirven** para escribir texto nuevo.
> Illustrator los guarda con codificación propia: `has_glyph` dice que el glifo
> está y al componer sale «nversi n agr cola» en vez de «Inversión agrícola».
> Siempre el TTF completo.

### Dos reglas duras que ya declara el propio manual

1. **Siempre terminaciones redondeadas.** Está escrito en la pág. 5 y vale para
   todo elemento gráfico.
2. **Los íconos son lineales con un detalle sólido** en primario o secundario,
   siguiendo la línea del isotipo.

---

## 3. El manual completo — qué lleva y qué no

La referencia del estudio es `BRANDGUIDELINES_PIVOT.pdf`: 20 láminas de
1008×612 pt, con cabecera numerada, columna de texto a la izquierda y la
demostración a la derecha. **Landera usa esa misma anatomía**, pero no el mismo
contenido: Pivot es una tecnológica de eCommerce con tres marcas, y Landera es
una gestora de campos con una marca y dos bajadas.

### Anatomía de la lámina (heredada de la plantilla)

```
┌──────────────────────────────────────────────────────────┐
│  05   Brand guideline                                     │  ← nº + rótulo
│  ────────────────────────────────────────────────────────│  ← línea x 40,8→967,2 · y 58
│                                                           │
│  Sección          │                                       │
│  Subsección       │        LA DEMOSTRACIÓN                │  ← ~70 % del ancho
│                   │                                       │
│  Párrafo          │                                       │
│  justificado      │                                       │
│                   │                              landera  │  ← logo al pie, gris claro
└──────────────────────────────────────────────────────────┘
```

### Estructura propuesta — 22 láminas

| # | Lámina | Nota |
|---|---|---|
| 01 | Portada | Ya existe |
| 02 | **Índice** | Falta |
| 03 | **Introducción** | Falta. Para qué es el manual y a quién obliga |
| 04 | Logotipo oficial | Construcción y las dos bajadas |
| 05 | **Área de reserva** | Falta. Medida en una unidad del propio isotipo |
| 06 | **Tamaño mínimo** | Falta. En cm, impreso y digital |
| 07 | Versiones | Principal, secundaria, isotipo — ya existe, hay que separarla |
| 08 | **Monocromía** | Positivo, negativo y escala de grises |
| 09 | **Usos incorrectos I — color** | Falta |
| 10 | **Usos incorrectos II — forma** | Falta. Rotar, condensar, agregar textos |
| 11 | **El logotipo sobre fotografía** | ⭐ Falta y es clave — ver §4 |
| 12 | Tipografía | Ya existe |
| 13 | Sistema cromático | Ya existe — **corregir la ficha del terracota** |
| 14 | **Las franjas como sistema** | ⭐ Falta. Construcción, escala y usos del elemento del isotipo |
| 15 | Iconografía | Ya existe — falta nombrar cada ícono |
| 16 | **Papelería** | Falta. Tarjeta, hoja carta, sobre, firma de correo |
| 17 | **Informe de gestión** | ⭐ Falta y es LA pieza — ver §4 |
| 18 | **Plantilla de presentación** | Falta |
| 19 | **Digital** | Falta. Avatar, favicon, LinkedIn (no Instagram primero) |
| 20 | **Señalética de campo y vehículos** | ⭐ Falta y es específico — ver §4 |
| 21 | **Equipamiento de terreno** | Falta. Su «merchandising» real |
| 22 | Contraportada | Ya existe |

De las 22, **hoy existen 6**.

---

## 4. Lo que Landera lleva y Pivot no

Acá está el criterio. Copiar el índice de Pivot tal cual daría un manual correcto
y genérico; estas cuatro láminas son las que lo hacen de esta marca.

**11 · El logotipo sobre fotografía.** Landera vende tierra. Su comunicación va a
estar siempre sobre campo, cielo y cultivo, y ese es justo el fondo donde un
logotipo se pierde. Pivot puede darse el lujo de prohibir el logo sobre foto
(lo hace, en su pág. 9); Landera no puede prohibirlo porque es su caso normal.
Hay que resolverlo: qué versión va sobre foto clara, cuál sobre foto oscura, y
el velo mínimo cuando la foto no da contraste.

**14 · Las franjas como sistema.** El activo gráfico más fuerte que ya tiene la
marca son las líneas concéntricas del isotipo — evocan surcos y curvas de nivel.
Hoy aparecen sueltas en una lámina de «elementos base». Merecen su propia página:
cómo se construyen, en qué escalas, cuándo se usan como remate y cuándo como
textura de fondo.

**17 · El informe de gestión.** Un farmland manager le rinde cuentas a
inversionistas: el informe trimestral **es** su pieza principal, más que cualquier
flyer. Tiene tablas, cifras de superficie y de rendimiento, y mapas de predios.
Sin una lámina que lo norme, cada informe va a salir distinto.

**20 · Señalética de campo y vehículos.** La marca vive en terreno: portones de
predio, letreros de acceso, camionetas. Es el equivalente real del «stand de
eventos» de Pivot.

### Lo que NO va

| De Pivot | Por qué no |
|---|---|
| Convivencia con logos de partners/sistemas | Es el problema de una tecnológica con integraciones. Landera no lo tiene. Si aparece co-branding con un fondo de inversión, se resuelve en la lámina de papelería |
| Merchandising de oficina (polerones, lanyards, stickers, cajas de regalo) | Landera no hace eventos de tecnología. Su equipamiento es de terreno: chaqueta, casco, libreta de campo |
| Instagram como plataforma principal | Es B2B de inversión: manda LinkedIn. Instagram, si va, va después |
| Tres marcas | Landera es **una** marca con dos bajadas. La lámina de versiones se simplifica |

---

## 5. Antes de producir una sola lámina

- [ ] El cliente cerró el **color primario** (verde, un gris, o la invertida)
- [ ] Llegaron **Base** y **Base 1** para comparar
- [ ] Está el archivo de **Barkentina**
- [ ] Se decidió si la **fila monocromática** queda en 4 o 5 versiones
- [ ] Se corrigió la **ficha del terracota** (`5B5B5B` → `#E4361F`)
- [ ] Hay **fotografía real de los campos** que administran, o se decide generarla
- [ ] El archivo se arma **desde la plantilla**, no duplicando el PDF actual

---

## 6. Historial

**03-09-2026** — Se midió el sistema completo sobre `PROPUESTA BASE V2.pdf` y se
detectaron los residuos de Pivot. Se produjeron tres variantes con gris de
primario y la versión invertida (fondo blanco, líneas verdes) que pidió el
cliente. Se levantó el plan del manual completo contra la referencia del estudio.
