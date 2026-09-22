# Cómo diseña el equipo — lo que revela el Drive

> Levantado el **02-09-2026** barriendo Drive por `owner` para las cuatro personas que
> firman archivos de diseño, ventana **01-06-2026 → 02-09-2026**.
>
> **Para qué sirve:** el sistema de marcas dice cómo se diseña *bien*; este documento
> dice cómo se diseña *acá*. Nomenclatura, estructura de carpetas, formatos de entrega
> y cadencia real de cada cuenta. Una pieza que no calza con esto obliga a la KAM a
> renombrar y a mover archivos, aunque el diseño esté impecable — y el portal de
> validaciones levanta **por nombre de archivo**.
>
> Se actualiza cuando `/al-dia` encuentre un patrón nuevo. No reemplaza a
> [`SISTEMA-DE-MARCAS.md`](SISTEMA-DE-MARCAS.md) ni a los manuales de
> `clients/<marca>/CLAUDE.md`: los complementa con la realidad operativa.

---

## 1. Quién firma qué — el mapa real, no el heredado

`docs/MAPA-DRIVE.md` tenía a Diego Aguilar en una sola cuenta («Pivot Connect») y a
Paulina como diseñadora *del cliente*. El barrido dice otra cosa:

| Persona | Cuentas que toca de verdad (jun–sep 2026) | Cadencia |
|---|---|---|
| **Elisabet Soto «Eli»** | Hilton completo: **DoubleTree · QB · Between · Piso18**. Orgánico + **paid** + **imprenta** | Diaria, la más alta |
| **Paulina Bustamante** | **Produce: EBEMA (grilla · Click · paid) · MyZoo · Traverso.** Su criterio cuenta además en **Nueva Urbe (INU + Rentas) · Revex · Casablanca** | Por lote mensual |
| **Diego Aguilar** | **Más Center · Selfie · Redmagister** | Por lote mensual |
| **Constanza Lizana «Coni»** | **Selfie · CAVA · QB · MyZoo (packaging) · Algarrobal · C&D** | Media; **cero desde el 28-08** |

**Tres correcciones que importan:**

1. **Diego no es «el de Pivot Connect».** Es el más activo después de Eli y produce
   grillas completas de Más Center. **No usa el estudio** — cero commits en el repo,
   no está en `QUIEN-HACE-QUE.md` ni en el llavero.
2. **Selfie la tocan dos personas.** Coni (el sistema medido, `clients/selfie/`) y
   Diego (banners y feed de septiembre, subidos el 31-08). El manual asigna Selfie a
   Coni. **Sin resolver quién firma, el estudio no puede producir Selfie**: aplicarle
   el criterio de una a lo que hizo la otra es inventar un sistema.
3. **Coni tiene un documento «Vacaciones Coni»** del 24-08 y no sube nada desde el
   28-08. Su silencio probablemente no es un atraso.

---

## 2. Elisabet Soto «Eli» — Hilton (DT · QB · Between · Piso18)

### Cómo nombra
Códigos cortos, **marca + tipo + número + semana**, con `N°` (con el símbolo de grado):

| Patrón | Ejemplo real | Qué es |
|---|---|---|
| `C<n> S<n> N°<n>` | `C1 S1 N°1`, `C2 S1 n°2` | Slide de carrusel, semana N |
| `C1 S1 N°1 NOVIOS` | carpeta | El carrusel lleva **el tema en el nombre de la carpeta**, no en el archivo |
| `ST N°<n> S<n>` | `ST N°1 S1`, `ST 2 S1`, `ST 5 S1` | Story. **El formato no es estable** (`ST N°1` / `ST 2`) |
| `BW <TIPO> <DD-MM> <tema>` | `BW FEED 01-09 Cowork 1 portada`, `BW ST 03-09 Cafe de regalo cumpleanos` | **Between usa fecha de publicación + tema descriptivo.** Es el más legible del equipo |
| `Reel n°<n> S<n> <MARCA> <tema>` | `Reel n°1 S4 QB PASTAS NUEVAS(C3)`, `REEL N°3 S4 QB AGOS SONIDOS` | Reel; el `(C3)` referencia la casilla de la grilla |
| `C1 ER`, `C1 FT`, `CARRUSEL NB` | `C1 ER N°1` | **Iniciales de campaña**: ER = Escapada Romántica, FT = ¿?, NB = ¿? |

**Between escribe sin tildes en los nombres** (`Cumpleanos`, `Cafe`) — es deliberado y
evita problemas de codificación entre Windows y Mac. **Respetarlo.**

### Cómo estructura
```
S1 HILTON SEP 2026 /
S2 HILTON SEP 2026 /
    ├── DT /  C1 ER DT S2 /        ← una carpeta por carrusel
    └── BW /                        ← una por marca del complejo
```
Semana → marca → carrusel. La carpeta del carrusel **es** la unidad de entrega.

### Lo que casi nadie tiene: Eli también hace imprenta
Y tiene un paquete de entrega fijo, siempre el mismo:

| Archivo | Para qué |
|---|---|
| `<pieza>.ai` | Editable vivo |
| `<pieza> - texto contorneado.ai` | Para la imprenta (sin dependencia de fuentes) |
| `<pieza> <medida>.pdf` | `Acrílico 12,5x18cm`, `Planner DT 2026 31,5 cm x 18,5 cm OI`, `ACCESO MONTACARGA (IZQUIERDA) 60x20cm` |
| `<pieza> original imprenta.pdf` y `<pieza> cmyk.pdf` | Dos versiones: la de trabajo y la convertida |
| `<pieza> 150ppp.jpg` + `<pieza>.png` | Previsualización para aprobar |
| `Links/` + `Fonts/` | El `.ai` viaja **empaquetado** |

**La medida va en el nombre del archivo, siempre.** Y `OI` = orientación horizontal
(*oblong*/apaisado) en el planner.

### Pantallas digitales (QB)
`SUNSET QB PANTALLA 1080X1920PX 72PPP.png` — **cuatro variables en el nombre**:
pieza · medida · resolución · formato. Entrega la matriz completa: 1080×1920 y
1230×720, cada una en 72 y 150 ppp, cada una en PNG y JPG = **8 archivos por pieza**.

### Lo que hay que aprender de Eli
- **El nombre del archivo es la ficha técnica.** Medida, resolución y destino van ahí.
- **Nunca entrega un `.ai` suelto**: va con `Links/`, `Fonts/` y una versión contorneada.
- **Una carpeta por carrusel**, nunca piezas sueltas mezcladas.
- Una pieza aprobada **se re-sube al mismo archivo** para no romper el enlace del portal
  (así se hizo con «Cowork 2 winter garden», que conserva un nombre que ya no describe
  la foto — a propósito).

---

## 3. Paulina Bustamante — EBEMA/Click · MyZoo · Traverso

> **Produce** EBEMA en sus tres destinos (grilla · Click · paid), MyZoo y Traverso.
> **Su criterio también cuenta** en Nueva Urbe (INU + Rentas), Revex y Casablanca,
> aunque las piezas de esas tres no las arme ella. Confirmado por ella el 22-09-2026.

### Cómo nombra
**Todo en minúscula, con guion bajo, marca al principio.** Es la nomenclatura más
regular del equipo y la más fácil de automatizar:

```
<marca>_c_<tema><n>.png       ebema_c_stock1.png · myzoo_c_partners8.png · ebema_c_piazza3.png
<marca>_<pieza>_<tema>.png    myzoo_pendon_alma.png
<marca>-mail_<n>.<n>_<mes><año>.png   rentas-mail_2.3_septiembre2026.png · inu-mail_1-1_septiembre2026.png
<marca>_st-<DD.MM>.png        inu_st-09.09.png · inu_st-17.09.png
<marca>_estatico-<DDmes>.png  inu_estatico-18sept.png
reel_<tema>_<mes>.mp4         reel_click_sept.mp4 · reel_calera_sept.mp4 · reel_cat_sept.mp4
```

`c_` = carrusel. El número al final es la slide. **Sin espacios, sin mayúsculas, sin
tildes** — se puede procesar por script sin comillas.

### Cómo estructura — EBEMA septiembre es el modelo
```
9. SEPTIEMBRE /
    ├── feed /       c_cedral/ c_cintac/ c_novoplast/ c_surpol/ c_toro/  + reel_*.mp4
    ├── stories /
    └── LinkedIn /   c_stock/ c_click/ c_ebema-1/ c_ebema-2/  + reel_calera_sept.mp4
```
**LinkedIn tiene su propia rama con sus propios carruseles** — no es un reaprovechado
del feed. Cuando el estudio produzca EBEMA tiene que entregar las tres.

Nueva Urbe separa por pieza: `mail_1/` y `mail_2/`, cada uno con sus tres imágenes
(`1-1`, `1-2`, `1-3`). Un mailing = una carpeta = tres módulos.

### ⭐ Lo más valioso: cómo consigue el material que falta
La carpeta `material_revex/` (27-08) tiene `suc_temuco/`, `suc_lascondes/` y
`alfombras_concurso/`, y adentro archivos llamados **`a2026-08-27-15h23m43s639.png`**.
Ese formato de nombre —fecha, hora, minuto, segundo y milisegundo— es el de una
**captura de fotograma de video**.

**Paulina resolvió con un frame de video la foto de fachada de Temuco que el estudio
tenía anotada como bloqueante desde la entrega de septiembre.** Es exactamente la
regla de «agotar el material antes de bloquear», y acá está la prueba de que la
diseñadora la aplica antes que nosotros.

**Corolario:** antes de declarar que falta una foto, revisar si Paulina ya la extrajo.
`material_<marca>/` es el primer lugar donde mirar.

### ⚠️ Genera con ChatGPT, no con Magnific
`fotos_casablanca_suc/` y `casablanca fondos/` traen PNG llamados
`ChatGPT Image 28 ago 2026, 09_36_35 a.m..png`. Son imágenes generadas, mezcladas en la
misma carpeta con **fotos reales** (`lascondes-6.png`, `lascondes-8.png`, de junio).

**Nada de esa carpeta entra a una pieza sin pasar por la compuerta de material.** El
nombre no distingue lo real de lo generado, y ese es justo el error que costó la
entrega de Revex/Casablanca del 25-08.

---

## 4. Diego Aguilar — Más Center · Selfie · Redmagister

### Dos nomenclaturas distintas, y la diferencia es el tipo de cuenta

**Más Center — por fecha de publicación:**
```
c-<DD>-<MM>-<slide>.png    c-07-09-1 · c-16-09-5      (carrusel)
p-<DD>-<MM>.png            p-25-09 · P-29-09          (post estático)
r-<DD>-<MM>.mp4            r-14-09_1 · r-21-09        (reel)
st-<DD>-<MM>.png           st-18-09 · st-23-09        (story)
```
Una letra, la fecha, el número de slide. **El archivo dice cuándo se publica, no de qué
se trata** — sirve para una grilla apretada donde lo que manda es el calendario.
Excepciones cuando la pieza no tiene fecha fija: `st-ganador`, `st-precaucion`.

**Selfie y Redmagister — por tema:**
```
INV O VER.png / INV O VER_1..4.png     (carrusel; base sin sufijo + numeradas)
HILOS UNEN.png / HILOS UNEN_1..3.png
post-trafico.png · carrusel-wsp-1..3.png · st-wsp.png · rem-wsp.mp4
DESK.png · MOBILE.png                   (banners, por dispositivo)
```
`rem-` = reel. `wsp` = WhatsApp. **La primera slide va sin sufijo** y las siguientes con
`_1`, `_2` — o sea `INV O VER.png` es la portada, no la slide 1.

### Su estructura
`9. SEPTIEMBRE / {FEED, ST, BANNER}` para orgánico;
`PERFORMANCE / 2026 / SEPTIEMBRE / RENDIC / {FEED, ST, REELS}` para pauta.
Carpetas `OPCIONES/` y `CORREGIDO/` cuando hay ronda — **la versión corregida vive en su
propia carpeta**, no pisa la original.

### Lo que hay que saber antes de tocar sus marcas
- **Más Center no tiene manual en el estudio.** Hay trabajo previo (brochure, PPT
  comercial, dos landings) pero ninguna gramática medida. Producir su grilla hoy sería
  inventarle un sistema.
- **Redmagister no existía en el mapa del estudio.** Cuenta nueva, sin nada.

---

## 5. Constanza Lizana «Coni» — Selfie · CAVA · QB · MyZoo packaging · Algarrobal

### Cómo nombra — la más estructurada del equipo
**MAYÚSCULAS, la pieza primero, `_` como separador de campos, `-NN` para la secuencia:**

```
GRILLAAGO_S4_DDPELUQUERO-04.png       tipo + MES + semana + campaña - slide
MAILAGO_S4_PROMOCHILA-TINTURAS.png
BANNER AGO_S4_SEMANADPELUQUERODESK.png / ...MOBILE.png
BT_S4_AGOSTO_CARRUSEL_25-08-01..06.png
QB_S4__ST_27-08.png
CAVA_AGO_BRIEF<n>-<NN>.png
```

### ⭐ Dos patrones que valen para todo el estudio

**a) CAVA: una carpeta por brief, numeración continua entre briefs.**
```
BRIEF1/ CAVA_AGO_BRIEF1.png
BRIEF2/ CAVA_AGO_BRIEF2-02.png, -03
BRIEF3/ CAVA_AGO_BRIEF3-04.png, -05
...
BRIEF8/ CAVA_AGO_BRIEF8-16, -17, -18
```
El sufijo `-NN` **no se reinicia** en cada brief: corre 01→18 a través de los ocho.
Así una pieza suelta se puede ubicar en el mes entero sin abrir la carpeta. El brief del
Sheet y la carpeta de entrega quedan **atados uno a uno**.

**b) La campaña JJ: numeración continua a través de FORMATOS.**
```
1080x1080/  CARRUSEL_CAMPAÑA_JJ_Meta_S1_Feed_1080x1080-01 … -05
1080x1920/  ..._Story_1080x1920-06 … -10
1200X/      ..._Display_1200X628-11 … -15
300x250/    ..._Display_300x250-16 … -20
```
Veinte piezas, cuatro medidas, **una sola serie numérica** — y la medida va dentro del
nombre *y* en la carpeta. Es la forma más limpia de entregar una campaña multi-formato
que vi en el Drive. **Adoptarla cuando el estudio entregue paid multi-medida.**

### Versionado de documentos largos
`BROCHURE_ALGARROBALV2 → V7 → V8`, con las anteriores movidas a `VERSIONES ANTERIORES/`.
La versión va **pegada al nombre, sin separador**.

### Packaging MyZoo
`EDITABLES TODAS LAS ETIQUETAS/` con `<PRODUCTO> <FORMATO>_Carpeta/` empaquetado
(`Fonts/`, `Informe.txt`): `SHAMPOO AVENA VIT 5LITROS`, `ACOND AVENA VIT 5LITROS`,
`XTREME VET 5LTS`, `SHAMPOO GROOMER GRADE 5LTS _MAR`. **El formato (5 litros) es parte
del nombre del producto** — hay líneas distintas por envase.

Coni es **dueña de `LOGO CLIENTES` y de `Diseños EDITABLES`**: cualquier logo oficial
sale de ahí, y ahí está la carpeta `PAU` con lo que le pasa a Paulina.

---

## 6. Lo que vale para todas las marcas

| Regla | De dónde salió |
|---|---|
| **El nombre del archivo es la ficha técnica.** Medida, resolución, fecha o slide van en el nombre — el portal levanta por nombre | Eli (imprenta y pantallas), Diego (fechas) |
| **Una carpeta por unidad de entrega** — un carrusel, un brief, un mailing. Nunca piezas sueltas mezcladas | Los cuatro |
| **Numeración continua** dentro del mes o de la campaña, no reiniciada por formato | Coni (CAVA y JJ) |
| **LinkedIn se diseña aparte**, no se recicla el feed | Paulina (EBEMA) |
| **Un editable nunca viaja solo**: `Links/` + `Fonts/` + versión con texto contorneado | Eli, Paulina, Coni |
| **La corrección va en carpeta propia** (`CORREGIDO/`, `VERSIONES ANTERIORES/`), no pisa el original… | Diego, Coni |
| **…salvo que la pieza ya esté en el portal**: ahí se re-sube al MISMO archivo para no romper el enlace | Eli (Between) |
| **Un `createdTime` viejo con `modifiedTime` nuevo es un REEMPLAZO**, no una pieza nueva — es como se detecta una ronda que nadie avisó | Nueva Urbe, 31-08 |
| **Dos archivos con el mismo tamaño exacto en dos carpetas son la misma pieza duplicada** | El carrusel ER en orgánico y en paid |
| **Antes de decir «falta la foto», mirar `material_<marca>/`**: la diseñadora quizá ya sacó el frame del video | Paulina (Temuco) |
| **Una imagen generada con IA y una foto real pueden estar en la misma carpeta y no distinguirse por el nombre.** Compuerta de material, siempre | Paulina (Casablanca) |

---

## 7. Lo que este barrido NO puede decir

- **No mide diseño.** Salen nombres, carpetas, pesos y fechas — no colores, tipografías
  ni retículas. Para eso hay que bajar las piezas y medirlas (`/adn`).
- **No lee los comentarios de los clientes.** El token del estudio tiene scope
  `drive.file` y solo ve archivos que él mismo subió: los comentarios sobre piezas que
  subió una diseñadora a mano son invisibles desde acá.
- **La ventana es jun–sep 2026** y la paginación de Drive devuelve 5 resultados por
  página, así que **no es exhaustivo**: es el patrón, no el inventario.

## 8. Qué falta decidir (no lo puede resolver el sistema)

1. **¿Diego entra al estudio?** Hoy produce tres cuentas sin llavero, sin `/abrir` y sin
   bitácora. Si sigue afuera, esas tres cuentas nunca van a tener sistema.
2. **¿Quién firma Selfie?** Coni tiene el sistema medido; Diego subió septiembre.
3. **Más Center y Redmagister no tienen manual.** Producirlas hoy es inventar.
