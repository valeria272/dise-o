# Qué se automatiza y qué se deja a mano

> Análisis del **02-09-2026** sobre las cuatro cuentas que quedaron asignadas:
> Paulina (EBEMA · MyZoo · Traverso) y Diego (Más Center). CAVA y Selfie quedan
> fuera hasta que vuelva Coni.
>
> **El criterio:** se automatiza el **esqueleto** —lo que se repite mes a mes sin
> decisión creativa— y se deja a mano **la idea**. Una cuenta es automatizable
> cuando la pieza nueva es la misma estructura con otro contenido; no lo es cuando
> cada pieza es un concepto distinto.

| Cuenta | Veredicto | Por qué |
|---|---|---|
| **EBEMA** | 🟢 **Ya está a medio construir** — cerrar los extremos | El sistema existe y replica 1:1 el esquema de Paulina |
| **Más Center** | 🟢 **Automatizable, y con manual oficial** | Esqueleto idéntico en 4 meses medidos |
| **MyZoo** | 🟡 **Parcial** — sólo los formatos de campaña | Convive con packaging Pantone que no se automatiza |
| **Traverso** | 🔴 **A mano** | Cada pieza es un concepto único; el valor está en la idea |

---

## 🟢 EBEMA — lo que falta es conectar los extremos

**El sistema ya existe** en [`clients/ebema/sistema/`](../clients/ebema/sistema/):
`base.css` con toda la geometría medida y los tres esquemas (sucursal / `.click` /
`.spc`), `build_ejemplo.py` como generador, `render.sh` (HTML → PNG con Chrome
headless, receta validada), las fuentes reales (Raleway + la Helvetica Bold del kit
del cliente) y los logos oficiales. Es la v8 del 21-08, **la que replica 1:1 el
esquema de agosto de Paulina**.

Hoy el flujo es: copiar la carpeta al mes nuevo, **editar a mano las listas de texto**
en `build.py`, renderizar. O sea el diseño ya está automatizado; lo que sigue manual
es la entrada y la salida.

**Lo que falta, en orden:**

1. **Leer el brief del Sheet** en vez de tipear las listas. El brief mensual ya existe
   y tiene la estructura buena — el mismo formato del brief de Revex que el estudio
   adoptó como contrato de entrada.
2. **Cubrir el feed orgánico.** El sistema está calibrado sobre las piezas de paid y
   mailing. La grilla de septiembre de Paulina trae además **8 carruseles de producto**
   (`c_cedral`, `c_cintac`, `c_novoplast`, `c_surpol`, `c_toro`, `c_stock`, `c_click`,
   `c_ebema`), **stories** y **una rama LinkedIn con carruseles propios**. Hay que
   medir esos tres esquemas antes de decir que EBEMA está automatizado.
3. **Salida con la nomenclatura de Paulina** —`ebema_c_<tema><n>.png`, minúscula y
   guion bajo— y subida a la estructura `9. MES / {feed, stories, LinkedIn}`.

**Riesgo bajo:** el sistema ya pasó por rondas reales con el cliente y está calibrado
contra piezas aprobadas. Es la cuenta que más rápido devuelve el trabajo invertido.

---

## 🟢 MÁS CENTER — el esqueleto es una constante, y está medido

### La evidencia
Medí las portadas de **junio, julio y septiembre** (`c-09-06-1`, `c-11-06-1`,
`p-05-06`, `c-07-07-1`, `c-15-07-1`, `c-16-09-1`, `p-25-09`):

| Elemento | Qué hace | Constancia |
|---|---|---|
| **Logo MÁS CENTER** | Blanco, centrado arriba, con «GRUPO IFB» bajo el chevron | **y 148–188 px en las cuatro piezas.** Idéntico |
| **Titular** | Mayúsculas, Poppins pesada, blanco, 2–3 líneas | Constante; varía izquierda/centrado |
| **Pastilla de bajada** | Extremos redondeados, roja, texto blanco | ~76 px de alto por línea, ~55 % del ancho |
| **Flecha circular** | Negra, abajo a la derecha, indica «desliza» | En todas |
| **Foto** | A sangre, 4:5 | En todas |

**Septiembre confirma la tesis en vez de romperla.** Cambió la *piel* —la mascota
«Localito» con chupalla y poncho, los banderines, el mapa de Chile— pero el esqueleto
está intacto: mismo logo en la misma banda, mismo titular en mayúsculas, misma
pastilla roja abajo. **Lo dieciochero entró como contenido, no como estructura.**

### El manual oficial ya estaba en el repo
[`raw/mascenter-terrenos/manual-marca.pdf`](../raw/mascenter-terrenos/manual-marca.pdf)
— Manual de marca Grupo IFB 2023, 42 páginas, con una sección 6 dedicada a Más Center:

- **Tipografía: Poppins, familia completa** (p. 26). Confirmado, no inferido.
  ⚠️ Ojo: Grupo IFB **no** usa Poppins (Helvetica Neue + Cera Pro). Son marcas
  distintas dentro del mismo manual — no mezclar.
- **Rojo oficial: `#E52521`** «Vivid red» (p. 33). Complementarios: `#65140F` rojo
  muy oscuro, `#DADADA` gris muy claro, negro.
- **«Los títulos van dentro de pastillas con los extremos redondeados»** (p. 37) —
  la pastilla que veo en todas las piezas **es un recurso oficial del manual**, no un
  invento del diseñador.
- **Estilo fotográfico:** personas reunidas o en actividades, pasando un buen rato,
  sonriendo y conversando (p. 39).
- Las fotos que **no van a corte llevan bordes redondeados** (p. 40); las ilustraciones
  pueden superponerse a las fotos (p. 41) — que es exactamente lo que hacen el planeta
  del Día del Medio Ambiente y el «Localito».
- **Usos indebidos del logo:** no inclinar, no gradientes, no sombras, no 3D, no varios
  colores, no estirar, no contornear.

Y en el repo ya existe [`scripts/mascenter_sistema.py`](../scripts/mascenter_sistema.py),
con el chevron **trazado fila por fila desde el logo** y la paleta medida del brochure.

### Tres defectos que la automatización arregla sola

Esto salió de medir, no de opinar:

| Defecto | Medido | Debería ser |
|---|---|---|
| **El tamaño no es exacto** | `1081×1350` y `1081×1351` según la pieza (ratio 1,2488 / 1,2498) | `1080×1350` siempre (ratio 1,2500) |
| **El rojo está fuera de manual** | `#DC1914` en las pastillas | `#E52521` según el manual (p. 33) |
| **El margen del texto baila** | Bloque a 85 px en una pieza, 104 px en otra | Una sola constante |

Ninguno se ve a ojo. Los tres desaparecen el día que la pieza se genera por código.

### Qué NO se automatiza
La elección de la foto, la aparición de la mascota, el concepto del mes y el
co-branding (el mes del Mundial la portada llevaba logo de Panini). Eso lo sigue
decidiendo una persona; la máquina arma la pieza una vez tomada la decisión.

### Lo que falta antes de producir
Correr `/adn` sobre los editables de Diego para cerrar **el peso exacto de Poppins**
de los titulares, la geometría de la pastilla (radio, padding, alto por línea) y la
flecha. La geometría de arriba es medición sobre PNG exportado, que aproxima bien
pero no reemplaza al editable.

---

## 🟡 MYZOO — se automatiza el formato de campaña, no la cuenta

MyZoo son **dos disciplinas distintas** bajo un mismo nombre:

**Lo automatizable — los formatos de campaña del feed.** La pieza `WTF` que revisé
(`myzoo_c_xtremevet1`, 2250×2813, 4:5 exacto) es plantilla pura: logo circular negro
centrado arriba, palabra-gancho enorme en celeste con contorno blanco, bajada en dos
líneas de itálica gris con una palabra subrayada, foto lifestyle ocupando la mitad
inferior y un doodle celeste (un corazón) superpuesto. Las series `c_partners` (8
piezas), `c_detective` (3) y `c_xtremevet` (4) repiten el patrón cambiando gancho,
foto y doodle.

**Lo que no se toca — el packaging.** Etiquetas de envases de 5 litros con Pantone,
por línea de producto (`SHAMPOO AVENA VIT`, `ACOND AVENA VIT`, `XTREME VET`,
`SHAMPOO GROOMER GRADE`), y pendones de 18 MP para impresión. Eso es producción
gráfica con control de color, no generación por plantilla.

**Bloqueo:** MyZoo **no tiene manual ni kit** en el estudio. Antes de automatizar
nada hay que correr `/adn` sobre sus editables — que además están repartidos entre
Paulina (digital) y Coni (packaging).

---

## 🔴 TRAVERSO — dejarlo a mano, y no es una derrota

Miré la grilla de septiembre completa
([`raw/traverso/GRILLA-SEPTIEMBRE.md`](../raw/traverso/GRILLA-SEPTIEMBRE.md)):
12 posteos de feed, 4 tácticas, 4 reels estratégicos y 4 orgánicos.

**Las piezas son ideas, no ejecuciones de plantilla:**

- «Limón alfombra roja — NUEVO LOOK. MISMO LIMÓN.»
- «Kaiju mostaza inunda Santiago»
- «Ketchup piquero a la piscina de papas»
- «Porrón túnel del tiempo — 130 AÑOS VIAJANDO A TU MESA.»
- «Debate nacional — ¿CON O SIN AJÍ?»

Cada una es un concepto distinto, con un montaje distinto. Automatizar eso sería
producir doce veces la misma pieza con distinto texto, que es exactamente lo que hace
mala una cuenta creativa.

**Además tiene tres candados técnicos:**

1. **Optima** (regular / bold / extra black) es la tipografía del brandbook. Es de
   pago y no está en Google Fonts.
2. El logo es una **bandera ondulada** en Pantone Reflex Blue C + Pantone Yellow C,
   con prohibición explícita de cambiar color, deformar o inclinar.
3. La **curva property** azul aplicada a corte y el **color de familia por producto**
   (huincha diferenciadora: ketchup rojo, mostaza amarilla) exigen decisión por pieza.

**Lo único que vale la pena automatizar acá es el chasis**: logo bandera bien puesto,
curva property en el borde inferior, zona de titular en Optima Extra Black y sello
1896 donde corresponda. Un molde para que la idea se monte rápido y salga a medida —
no un generador de piezas.

---

## El orden que propongo

1. **EBEMA**, porque el 70 % ya está hecho y calibrado contra piezas aprobadas.
   Falta medir los tres esquemas del orgánico y enchufar el brief.
2. **Más Center**, porque tiene manual oficial, esqueleto medido y tres defectos
   objetivos que la automatización corrige de entrada. Necesita `/adn` sobre los
   editables de Diego primero.
3. **MyZoo**, sólo el formato de campaña, y después de `/adn`.
4. **Traverso**: chasis sí, piezas no.

> **Nota sobre Diego:** entra al estudio desde ahora, así que Más Center deja de ser
> una cuenta sin sistema. Hay que sumarlo al llavero, a `/abrir` y `/cierre`, y abrir
> `clients/mascenter/` con manual y `marca.json` — el manual de marca oficial ya está
> en el repo y da para arrancar hoy.
