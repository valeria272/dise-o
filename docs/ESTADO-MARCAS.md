# Estado de las marcas — madurez y checklist por cliente

> Auditado el **25-08-2026** sobre lo que hay realmente en el repo, no sobre lo que
> recordamos. Se revisa el primer lunes de cada mes.
> Las 7 capas están definidas en [`SISTEMA-DE-MARCAS.md`](SISTEMA-DE-MARCAS.md) §1.

## ⚠️ La cartera real es el doble de lo que teníamos mapeado

Buceo del Drive **AGENCIA COPYWRITERS** (`16kNWE2mkbLh1uTb5Jc5TuDhYwM0OOw0A`) el
25-08-2026. La carpeta tiene 16 clientes, pero las planificaciones de medios
revelan **~24 cuentas activas** — el sistema de diseño cubre hoy 7.

| Con sistema de diseño (7) | Activos SIN sistema (17) |
|---|---|
| EBEMA/Click · Revex · Casablanca · Selfie · Between · Tierra Calma · Abakos* · San Esteban** | **Weleda Chile** · **Weleda Argentina** · **CAVA** · **Más Center** · **RENDIC** · **Japi Jane** · **FORK** · **PETRA** · **Ecotecnos** · **PRT** · INU (Nueva Urbe) · Rentas Nueva Urbe · MyZoo · Traverso · Santa Gota · QB / DoubleTree / Piso18 |

\* Abakos tiene manual pero sin gramática medida.

\*\* San Esteban (07-09-2026) tiene manual y **gramática medida** sobre las 7 gráficas
aprobadas de septiembre, pero le falta la capa de imagen: la carpeta de material de
octubre está vacía y la sesión fotográfica no es accesible. Ver
`clients/san-esteban/CHECKLIST-CLIENTE.md`.

> ℹ️ **Weleda (Chile y Argentina) no lleva diseño de la agencia** — las piezas las
> manda el cliente (confirmado 25-08-2026). Solo planificación de medios. Por lo mismo
> **no** necesita sistema de marca acá, y la duda del voseo argentino queda cerrada:
> no escribimos copy para esa cuenta.

### El equipo, según quién firma los archivos

| Rol | Personas |
|---|---|
| **Diseño** | Elisabet Soto «Eli» (Hilton: DT/QB/BW/P18) · Constanza Lizana «Coni» (Selfie) · Paulina Bustamante (EBEMA — es del cliente, no de la agencia) |
| **Medios / planificación** | Ignacio Retamal · Sebastián Córdova |
| **KAM / cuentas** | Serena Abarca · Constanza Olivares · Ámbar Gallardo · Carlos Figueroa · Francisco Fouilloux |

### ⭐ Ya existe un formato de brief de diseño, y es bueno

`Brief Diseño Septiembre 2026 - REVEX` (Drive `1JegSXFNuM0SWxuRU6g5dfplXiF2ktD93`,
de Serena). Por pieza trae: formato y medidas · dónde se publica · objetivo · botón ·
material de referencia · **qué se ve en la imagen** · antetítulo / título / bajada /
CTA separados · copy del anuncio (que NO va en la gráfica) · **lineamientos gráficos
numerados** · qué decía la gráfica anterior · y una hoja de datos de referencia con
direcciones, horarios, links y reglas de marca.

**Este es el contrato de entrada del sistema.** Un brief así se ejecuta sin una sola
pregunta de vuelta. Uno que no lo tenga genera cuatro rondas. Adoptarlo para todas
las marcas es la palanca más grande que hay: ver [`docs/BRIEF-DE-DISENO.md`](BRIEF-DE-DISENO.md).

### Lo que el buceo corrigió

| Marca | Error que tenía | Corregido |
|---|---|---|
| **Revex** | Tenía **Vitacura** como sucursal de Revex | **Juan XXIII 6359 es el showroom de CASABLANCA.** Revex tiene 3 locales: Las Condes Design, Temuco y el Patio Outlet. Ya corregido en el manual y en el kit |
| **Revex** | Sin horarios ni redacción exacta de la dirección | Los 3 horarios + «PISO 1, LOCAL 112» (no «Local 112 primer piso») |
| **Revex** | Sin regla de precios | Un porcentaje se publica **solo con confirmación escrita** de la clienta |

Es exactamente el tipo de error que el sistema existe para eliminar: estuvo meses en
el manual y nadie lo notó hasta contrastarlo con el brief real.

---

## Avance del 25-08-2026 — editables de Coni y Eli

| Marca | Qué se levantó | Estado |
|---|---|---|
| **Between** | `/adn` completo desde los editables de Eli. **Brushwell resuelto** e instalada. Geometría del logo medida sobre sus plantillas | ✅ desbloqueada |
| **MyZoo** | Manual + ficha. **Envase medido y completo** (140×160 mm, CMYK, 3 Pantone, Neutraface). Claims regulados del catálogo | ◐ envase sí, digital no |
| **CAVA** | **Sistema completo**: es el e-commerce de Viña Morandé. KV mensual con fondo Magnific → mailings que solo cambian la barra del llamado. Paleta medida, jerarquía de 10 niveles, 49 vinos catalogados, **legal de alcohol resuelto** | ✅ falta solo la tipografía |
| **Selfie** | Estructura de trabajo de Coni por semana, nomenclatura de mailing, campañas y tamaños de banner | ✅ ya estaba, se completó |

**Hallazgo transversal:** el `Informe.txt` de un `.ai` empaquetado es la mejor fuente
que existe. Método en el comando **`/adn`**. Reveló, por ejemplo, que en Between
conviven **9 scripts** distintas y que Raleway se usa en el rango completo.

**Corrección de regla:** «el logo va pegado arriba» es de **Revex y Casablanca**,
NO es global. En **Between va centrado y con margen**, con dos plantillas por formato.

---

## Tabla de madurez

Leyenda: ● completa · ◐ parcial · ○ falta

| Marca | Manual | Ficha `.json` | Kit código | Sistema producción | Identidad | Gramática | Imagen | Copy | QA | Listo para correr solo |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **EBEMA / Click** | ● | ● | ● | ● | ● | ● | ◐ | ● | ● | **SÍ** (falta foto de 3 sucursales) |
| **Revex** | ● | ○ | ● | ◐ | ● | ● | ● | ● | ● | casi — falta ficha `.json` |
| **Casablanca** | ● | ● | ● | ◐ | ● | ● | ● | ● | ● | casi — geometría **medida** sobre 55 piezas (26-08); faltan los archivos de tipografía y el registro editorial sin medir |
| **Selfie** | ● | ○ | ● | ◐ | ● | ● | ● | ● | ● | casi — falta ficha `.json` |
| **Between** (Hilton) | ● | ○ | ● | ● | ◐ | ● | ◐ | ● | ◐ | **no** — falta `Brushwell.otf` |
| **Tierra Calma** | ● | ○ | ● | ● | ● | ● | ● | ● | ● | casi — falta ficha `.json` |
| **Abakos** | ◐ | ○ | ● | ○ | ● | ◐ | ● | ● | ◐ | **no** — gramática sin medir |
| **Nueva Urbe** | ○ | ○ | ● | ○ | ◐ | ○ | ○ | ◐ | ○ | **no** |
| **Traverso** | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | **no** |
| **Piso 18** (Hilton) | ● | ● | ● | ○ | ● | ◐ | ◐ | ◐ | ● | casi — gramática medida sobre **7 piezas** (el método pide 20–60) |
| DT / QB (Hilton) | ◐ | ○ | ○ | ○ | ◐ | ○ | ○ | ◐ | ○ | **no** |

**Lectura:** EBEMA es la referencia. Revex, Casablanca, Selfie y Tierra Calma están
a un paso (ficha `.json`, media hora cada una). Abakos, Nueva Urbe, Traverso y las 2
marcas restantes de Hilton necesitan la vuelta completa de la §7 del sistema.

> ⭐ **Piso 18 quedó documentado el 22-09-2026** por instrucción de Eli — igual que QB,
> es marca **independiente** dentro del complejo.
>
> ⚠️ **Corrección del mismo día:** el primer diagnóstico dijo que a Piso 18 le faltaba
> el sistema. **Era falso.** Ya tenía kit de código medido (`src/brand/piso18.ts`, 425
> líneas), los 20 cortes de IvyPresto en el repo, el logotipo limpio recortado en
> `public/assets/piso18/` y reglas de QA calibradas en modo control. Lo que faltaba era
> el **manual legible** y la **ficha** — y eso es lo que se escribió.
>
> Lo que sigue abierto de verdad: la gramática está medida sobre **7 piezas** cuando el
> método pide 20–60, y `ref-eli-sep2026/` sigue vacía. Ver
> `clients/piso18/CHECKLIST-CLIENTE.md`.

---

## Checklist por marca — qué falta pedir

### 🔵 EBEMA / EBEMA CLICK — `clients/ebema/`
Detalle completo en [`clients/ebema/CHECKLIST-CLIENTE.md`](../clients/ebema/CHECKLIST-CLIENTE.md).
- 🔴 Fotos reales de **Chillán, Rancagua y San Bernardo** (pedidas desde el 20-08)
- 🔴 Acceso de lectura al Drive de piezas aprobadas para **las 4 cuentas de Claude** del equipo
- 🔴 Confirmar voz del locutor de reels (Lorenzo vs Ignacio)
- 🟡 Editables `.ai` de las piezas de **sucursal** (sólo tenemos el de Click)
- 🟡 Códigos y precios oficiales de SPC en una hoja estable
- 🟡 ~23 fotos de bodega en alta que faltaron por tamaño

### 🔴 REVEX — `clients/revex/`
- 🔴 **Nombre real de la tipografía script** de la diseñadora (hoy se usa Sacramento como sustituto verificado)
- 🔴 **Foto de la fachada de Temuco** (pendiente desde la entrega de septiembre)
- 🟡 Confirmar si Gotham es la tipografía oficial (hoy Montserrat como sustituto)
- 🟡 Crear `marca.json` — los valores ya están en `src/brand/revex.ts`, hay que exportarlos
- 🟢 Mover el sistema a `clients/revex/sistema/` (hoy en `src/compositions/revex/sistema.tsx`)

### 🔴 CASABLANCA — `clients/casablanca/`
> Manual, `marca.json` y `CHECKLIST-CLIENTE.md` rehechos el **26-08-2026** con
> geometría medida sobre **55 piezas aprobadas** (`raw/casablanca/ref/`). Examen de
> admisión en `out/casablanca/examen/`. Detalle completo en `CHECKLIST-CLIENTE.md`.
- 🔴 **Las 3 piezas del feed publicado (registro editorial) como PNG** — no están en Drive ni en las grillas de paid; ese registro es el único sin medir
- 🔴 El archivo de la **serif itálica** real (hoy Playfair Display Italic 900 + tracking como sustituto — la 'z' no calza)
- 🔴 El archivo de la **sans** real (es más ancha que Poppins; probablemente la corporativa de Grupo Revex)
- 🟡 La script manuscrita de «Colección …»
- 🟡 Confirmar con Serena si el feed va en **1:1 o 4:5** (35 piezas en 1:1, sólo agosto en 4:5)
- 🟢 Fotos propias de ambiente — hoy se depende de render IA

### 🔴 SELFIE — `clients/selfie/`
- 🔴 **Acceso a la carpeta de diseño de Coni** (`1knb1O6u3SC5_DJ8fJpRrIbGhL_5riaZ_`) — tiene permisos propios, no se ve por link
- 🔴 **Logo oficial de Selfie Class** (hoy va como texto en el carrusel S4)
- 🔴 Referencia del carrusel **"WTF es..."** (el brief apunta a un IG que no abrió)
- 🟡 Confirmar los 3 espacios comerciales de septiembre que están "por confirmar"
- 🟡 Packshot en alta de **OSiS+ Session** (el del e-commerce está en baja)
- 🟡 Crear `marca.json` desde `src/brand/selfie.ts`

### 🔴 BETWEEN (Hilton) — `clients/hilton/`
- 🔴 **`Brushwell.otf` del Drive de Eli** — bloquea la ronda 2 completa. El token OAuth
  con scope `drive.file` no baja archivos de terceros: hay que pedírselo directo a Eli
  o subirlo a una carpeta compartida
- 🟡 Paletas de **QB** y **Piso18** (los `.ai` están en Drive, sin extraer)
- 🟡 `Stag LCG` para DT — es de pago, confirmar licencia del cliente

### 🟡 TIERRA CALMA — `clients/tierra-calma/`
- 🟡 Los 3 pendientes de Carlos: titular en el cielo, IA con referencia real, mapa oficial
- 🟡 **IvyOra** se activa vía Adobe Fonts en cada máquina — cada diseñador tiene que activarla
  en su Creative Cloud (no se empaqueta). Fallback: Instrument Serif
- 🟡 Crear `marca.json` desde `src/brand/tierracalma.ts`

### 🟠 ABAKOS — `clients/abakos/`
- 🔴 **Medir la gramática.** Hoy el manual tiene identidad y reglas de contenido, pero
  no la geometría: dónde va el logo, el titular, el CTA, con qué medidas. Necesito
  **10–20 piezas aprobadas** del cliente para medirlas
- 🔴 Style guide oficial en PDF (está en Drive `BRANDING LOGOS/MARCA`, sin extraer)
- 🟡 Créditos de Higgsfield para regenerar los personajes con consistencia

### 🟠 NUEVA URBE — `src/brand/nuevaurbe.ts`, sin manual
- 🔴 **Crear el manual** — hoy sólo existe el kit de colores
- 🔴 **Bajar sus reels de referencia** (>10 MB, el conector de Drive los corta) para calcar el cierre
- 🔴 Definir si INU y Rentas comparten sistema o son dos marcas (tienen 2 IG distintos)
- 🟡 Grillas mensuales: dónde viven y quién las cierra

### 🔴 TRAVERSO — sin nada
- 🔴 **Vuelta completa de onboarding** (§7 del sistema). Hay material en
  `raw/traverso/` y `assets/traverso/` pero ni manual ni kit
- 🔴 Piezas aprobadas de referencia para medir la gramática

### 🔴 DT / QB / PISO18 (Hilton) — sin sistema
- 🔴 Los `.ai` de Eli para extraer paletas y gramática de QB y Piso18
- 🔴 Definir prioridad: son 3 marcas más, cada una con su vuelta completa

---

## 🔴 El bloqueante estructural del traspaso

Auditado el 25-08-2026: el repo tiene **173 archivos versionados**. `public/assets/`
(433 MB — fuentes, logos oficiales, packshots) **no está en git**. Un diseñador que
clone hoy recibe el código y los manuales, pero **ninguna composición le va a
renderizar**.

Hay que elegir uno de los dos caminos y ejecutarlo antes de sumar al primer diseñador:

| Opción | Qué implica | Costo |
|---|---|---|
| **A (recomendada)** Versionar el núcleo: `public/assets/fonts/` + todos los logos ≈ **18 MB** | `git clone` + `npm install` y el repo funciona. Lo pesado (331 MB de video y foto en alta) se baja por marca desde Drive | Una vez, ~15 min |
| **B** Espejo completo de `public/assets/` en una carpeta de Drive + script de sync | Más fácil de mantener, nada en git | Cada clon parte con ~30 min de descarga |

Detalle en [`ONBOARDING-DISENADORES.md`](ONBOARDING-DISENADORES.md) paso 5.

---

## Lo que necesito de ustedes — transversal, vale para toda marca

| # | Qué | Por qué |
|---|---|---|
| 1 | **Acceso de Drive para las 4 cuentas de Claude del equipo**, no sólo la de Valeria | Sin referencias, un diseñador nuevo trabaja a ciegas. Es el bloqueante #1 de todo el plan |
| 2 | **Piezas aprobadas de cada cliente**, 20–60 por marca, en una carpeta estable | Es la materia prima del sistema. Sin ellas se adivina |
| 3 | **Los archivos de tipografía reales** de cada marca (o el nombre exacto y de quién es la licencia) | Hoy la mitad de las marcas corre con sustitutos |
| 4 | **Logos oficiales en PNG con transparencia**, en todas sus versiones de fondo | Recrear un logo a mano es un error garantizado |
| 5 | **Que el feedback del cliente llegue como comentario en el archivo de Drive** | Se lee automáticamente y queda trazable. Por WhatsApp se pierde |
| 6 | **Los briefs con textos finales** | Salen verbatim a la pieza; si cambian después, se rehace todo |

---

## Prioridad sugerida para los próximos 60 días

| Orden | Qué | Esfuerzo | Por qué primero |
|---|---|---|---|
| 1 | Acceso de Drive para las 4 cuentas | del cliente | Destraba todo lo demás |
| 2 | `marca.json` de Revex, Casablanca, Selfie, Tierra Calma | ~30 min c/u | Ya está la información; sólo falta exportarla |
| 3 | Fotos de Chillán / Rancagua / San Bernardo | del cliente | Cierra EBEMA al 100 % |
| 4 | `Brushwell.otf` | de Eli | Destraba Between |
| 5 | Gramática medida de Abakos | 1 sesión | Es cliente activo con piezas mensuales |
| 6 | Manual de Nueva Urbe | 1 sesión | Cliente activo sin sistema |
| 7 | Onboarding de Traverso | 1 sesión | Cliente nuevo, mejor sistematizarlo antes de acumular deuda |
| 8 | QB y Piso18 | 2 sesiones | Volumen alto, hoy 100 % manual |
