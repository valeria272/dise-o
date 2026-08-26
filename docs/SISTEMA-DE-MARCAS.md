# El sistema de marcas del estudio — cómo trabaja Claude en COPYLAB

> Este documento es **la ley**. Vale para EBEMA, Revex, Casablanca, Selfie, Between,
> Abakos, Nueva Urbe, Tierra Calma, Traverso y para toda marca que entre después.
> Si una instrucción del chat choca con esto, gana esto — salvo que el cliente o
> Valeria digan explícitamente lo contrario, y en ese caso se anota en el manual
> de la marca para que no vuelva a pasar.

---

## 0. La regla madre

**El brief manda el QUÉ. El sistema de marca manda el CÓMO.**

Una pieza nueva **extiende** el sistema que ya existe y está aprobado; no inventa uno.
Si el cliente ya tiene plantilla viva de su diseñadora, esa plantilla es la
referencia — aunque el brief describa otra cosa ("fondo minimal", "algo distinto").
Lo minimal va en la foto; la gráfica sigue siendo la de la marca.

Corolarios que ya costaron caro:

- Si una pieza de la marca A se puede recolorear y pasa por la marca B, está mala.
- Los textos en pantalla y los CTA salen **literales del brief**. No se inventan
  botones, claims ni la palabra "gratis".
- Si no hay dato (precio, código, fecha), **no se inventa**: se marca como pendiente
  y se pregunta.

---

## 1. Las 7 capas de un sistema de marca

Una marca está "lista para producir sola" cuando tiene las 7 capas escritas y
verificadas contra material real. Nada de esto se deduce: se **mide** sobre las
piezas aprobadas de la diseñadora del cliente.

| # | Capa | Dónde vive | Qué contiene |
|---|---|---|---|
| 1 | **Identidad** | `clients/<marca>/marca.json` | Colores muestreados píxel a píxel, fuentes con archivo real, logos oficiales y cuál va en cada fondo |
| 2 | **Gramática** | `clients/<marca>/CLAUDE.md` | Cómo se compone: dónde va el logo, el titular, la bajada, el CTA; qué se apila y qué no. Es lo que hace que la marca se reconozca |
| 3 | **Formatos** | `marca.json` → `formatos` | Medidas por uso + zonas seguras Meta + nomenclatura de archivos |
| 4 | **Imagen** | `CLAUDE.md` → "De dónde salen las imágenes" | Banco propio, e-commerce, fotos del cliente, y **sólo al final** IA — con las reglas de qué se puede y qué no generar |
| 5 | **Copy** | `CLAUDE.md` → "Tono" | Voz, vocativo, emojis sí/no, claims permitidos, legales obligatorios |
| 6 | **Pipeline** | `clients/<marca>/sistema/` | El código que produce la pieza: CSS/TSX + script de render + entrega |
| 7 | **QA** | `CLAUDE.md` → "QA obligatorio" | La lista de lo que se revisa **antes** de mostrar nada, con los errores ya cometidos |

---

## 2. Jerarquía de fuentes de imagen — en este orden, sin saltarse pasos

Este orden es innegociable. Cada salto hacia abajo hay que poder justificarlo.

```
1. FOTO APROBADA POR LA DISEÑADORA/JEFA DE DISEÑO DEL CLIENTE
   → carpeta Drive explícita. Manda sobre todo lo demás.

2. BANCO DE IMÁGENES DE LA MARCA (curado, en clients/<marca>/ o raw/<marca>/)
   → si la foto no está en el banco, no se usa.

3. E-COMMERCE DEL CLIENTE (packshots reales)
   → Shopify: /products/<handle>.json · /search/suggest.json · /products.json
   → WooCommerce: /wp-json/wc/store/products?search=
   → El packshot SIEMPRE es el real. Nunca inventado, nunca de stock, nunca espejado.

4. EDITABLES DE LA DISEÑADORA (carpetas Links/ de los .ai empaquetados)
   → ahí están los packshots en alta y las fotos originales.

5. PIEZAS YA APROBADAS (recortar el elemento de una pieza publicada)

6. IA (Magnific/Freepik/Higgsfield/Canva) — SOLO para ambiente y fondo
   → nunca para el producto, nunca para el logo, nunca para un dato.
   → sujeta a las reglas de imagen escritas en el manual de la marca.
```

**Regla de oro transversal:** nunca cruzar ciudades, sucursales ni sedes. La foto de
Antofagasta va sólo en la pieza de Antofagasta.

---

## 2.b ⛔ Material regulado — lo que nunca se manipula

Hay marcas cuyo producto **es un objeto regulado**: su envase lleva información legal,
denominación de origen, grado alcohólico o claims certificados. En esas piezas, el
packshot **no es una imagen: es un documento**.

**Nunca, en ninguna marca:**
- Cambiar el **tamaño relativo** entre productos de una misma pieza
- Editar, reescribir o regenerar una **etiqueta** (marca, año, cepa, formato, gramaje)
- **Estirar, deformar o espejar** un producto
- Inventar o alterar un **sello de certificación o premio**, o su puntaje
- Mover un sello **de un producto a otro**
- Redondear o reformular un **claim certificado**

**Lo único permitido:** recortar sobre el fondo, escalar el conjunto proporcionalmente,
y ajustar sombra o reflejo para integrarlo.

### La verificación de proporción — hazla siempre

Un packshot colocado tiene que dar **el mismo ratio ancho/alto que su archivo
original**. Si difiere, está deformado.

```python
from PIL import Image
nat = Image.open(origen).size            # ej. (1934, 5724) → 0.338
assert abs(w_final/h_final - nat[0]/nat[1]) < 0.005
```

Comprobado en los editables reales de CAVA: la diseñadora **nunca** deforma — cada
botella conserva su proporción nativa al milésimo. Es el estándar.

**Y siempre:** el **legal obligatorio** de la categoría, con su texto exacto.
En alcohol en Chile es el recuadro «ADVERTENCIA · El consumo de alcohol en menores de
18 años se encuentra prohibido · Ministerio de Salud» con la banda tricolor. Sin eso,
la pieza no se entrega.

Marcas del estudio con material regulado: **CAVA** (vinos) · **MyZoo** (claims
sanitarios certificados) · **Abakos** (producto financiero).

---

## 2.c ⛔ Derechos de imagen y licencias de fuente

Dos cosas que no son de diseño pero se rompen en la mesa de diseño.

**Rostros.** Una foto de sesión **no habilita a publicar a la persona**. Si el banco
de fotos de un cliente tiene material antiguo, hay que saber **cuáles caras tienen
derechos vigentes**. Cuando no los tienen: la foto sirve de referencia de encuadre y
ambiente, pero **la cara no sale reconocible** — se reemplaza por un rostro generado
que calce con el perfil local.
Caso real: la sesión de Between de julio 2023 (ver `clients/hilton/CLAUDE.md` §C).

**Fuentes.** Antes de usar una tipografía en trabajo de cliente, abrir su archivo de
licencia. Muchas descargas gratuitas son **versiones DEMO de uso personal** y exigen
comprar licencia comercial.
Caso real: **Cherolina** (Between) es demo «personal use only».

En `marca.json`, toda fuente lleva su origen y si es empaquetable. Si dice
`"de_pago": true` o no tiene licencia declarada, **preguntar antes de entregar**.

---

## 3. El pipeline — de la instrucción a la entrega

Seis pasos. Siempre los mismos, para cualquier marca.

```
① CARGAR   → leer clients/<marca>/CLAUDE.md + marca.json + las referencias reales
② BRIEF    → leer el brief donde viva (Sheet/Doc/celda) y extraer los textos VERBATIM
③ MATERIAL → resolver cada imagen bajando por la jerarquía del punto 2
④ ARMAR    → producir con el pipeline de la marca (clients/<marca>/sistema/)
⑤ QA       → correr el checklist de la marca + zonas seguras + comparar contra la referencia
⑥ ENTREGAR → out/<marca>/<periodo>/ + ENTREGA.md + subida al Drive del cliente
```

**El paso ⑤ no es opcional y no se hace "a ojo".** Antes de mostrarle nada a nadie
se monta la pieza al lado de la referencia aprobada y se revisan los puntos del
checklist uno por uno. Una pieza que no pasó QA no existe.

---

## 4. Zonas seguras Meta — regla global de agencia

Aplica a **toda** pieza de pauta, de toda marca.

| Formato | Reserva |
|---|---|
| 9:16 (Reels/Story) | 250 px arriba · 340 px abajo · 115 px a la derecha (sobre 1080×1920) |
| 4:5 y 1:1 (Feed) | 10–15 % inferior libre |
| Todos | respiro mínimo de 60 px entre cualquier texto y cualquier borde o línea |

Overlay de verificación: `src/components/qa/SafeAreaAds.tsx`.

> ⚠️ **Excepción documentada:** en Revex y Casablanca el bloque de logo va **pegado
> al borde superior** (`top: 0`) también en story, por decisión de marca. La zona
> segura protege el texto, no el logo. Cada marca declara esto en su `marca.json`.

---

## 5. Dónde vive cada cosa

```
EDITOR VIDEOS/                      ← el estudio de diseño. Repo único, con remoto git.
├── docs/
│   ├── SISTEMA-DE-MARCAS.md        ← este archivo
│   ├── ONBOARDING-DISENADORES.md   ← cómo entra un diseñador nuevo
│   └── ESTADO-MARCAS.md            ← madurez y pendientes de cada marca
├── clients/<marca>/
│   ├── CLAUDE.md                   ← el manual (capas 2, 4, 5, 7)
│   ├── marca.json                  ← la ficha legible por máquina (capas 1, 3)
│   ├── CHECKLIST-CLIENTE.md        ← qué falta pedirle al cliente / al Drive
│   └── sistema/                    ← el pipeline de producción (capa 6)
├── src/brand/<marca>.ts            ← kit en código para reels Remotion
├── src/compositions/<marca>/       ← composiciones y sistema gráfico en React
├── raw/<marca>/                    ← material fuente bajado del cliente (gitignored)
├── public/assets/<marca>/          ← assets que usan las composiciones
└── out/<marca>/<periodo>/          ← entregas (gitignored)
```

**`raw/` y `out/` no se versionan** (pesan y son material del cliente). Se
reconstruyen desde el Drive del cliente con los IDs declarados en el manual de
cada marca. Por eso el manual **siempre** lleva la sección "Dónde está el material"
con los IDs de carpeta — sin eso, el repo no es traspasable.

---

## 6. Los proyectos hermanos — quién hace qué

El monorepo tiene otras carpetas que tocan a los mismos clientes. Para que no haya
duplicación:

| Proyecto | Es dueño de |
|---|---|
| **EDITOR VIDEOS** (este) | El **sistema de diseño** y la **producción de piezas**: manuales de marca, kits, gráficas, carruseles, reels, QA y entrega |
| `EBEMA/`, `DISEÑADOR/`, `AGENTE PAID MEDIA/` | Estrategia, cuentas publicitarias, briefs, pacing, reportes |
| `AGENTE CREATIVO RRSS/` | Orgánico de las 4 marcas **propias** de la agencia (no clientes) |

Si un cliente tiene carpeta propia en el monorepo (`EBEMA/`), ahí siguen viviendo
el contexto comercial, las cuentas y los outputs históricos. El **sistema de
diseño** se lee siempre desde `clients/<marca>/`.

---

## 6.b Landings de campaña — el octavo entregable

Decidido el 25-08-2026: el estudio también hace **landings de campaña** (no sitios
corporativos completos, no WordPress).

**Qué transfiere del sistema de marca y qué no:**

| Capa | ¿Sirve para web? |
|---|---|
| Identidad (colores, fuentes, logos) | ✅ **Directo.** `marca.json` es la fuente para los tokens CSS |
| Copy y tono | ✅ Directo |
| Reglas de imagen y jerarquía de fuentes | ✅ Directo — el packshot sigue siendo el real |
| QA (legales, precios CLP, datos verbatim) | ✅ Directo |
| **Gramática** (geometría en px sobre 1080) | ⛔ **No transfiere.** Está pensada para un lienzo fijo de anuncio |
| Formatos y zonas seguras Meta | ⛔ No aplican |

**La gramática de una landing es otra cosa** y hay que declararla aparte: retícula,
escala tipográfica fluida, breakpoints, alturas de sección, comportamiento del hero.
Va en `clients/<marca>/web.json` cuando la marca tenga su primera landing.

**Stack:** Vite + React + TypeScript, igual que `WEBS26/OTROS/auditorias/`. Para el
lenguaje visual y las animaciones están las skills `frontend-design`,
`awwwards-animations` y `animated-component-libraries`. Referencias visuales de la
competencia con `playwright-mcp`.

**Regla de convivencia:** una landing de campaña **extiende** el sistema de la marca
igual que una gráfica. Si la landing y el anuncio que lleva a ella no se parecen,
está mal — el usuario hace clic esperando lo mismo que vio.

**Fuera de alcance:** sitios corporativos de varias páginas, temas de WordPress
(eso vive en `SEO EXPERT/`), y el hosting o el despliegue.

---

## 7. Cómo se abre una marca nueva

1. `cp -r clients/_PLANTILLA clients/<marca>` y renombrar.
2. Bajar 20–60 piezas aprobadas reales de la diseñadora del cliente a `raw/<marca>/ref/`.
3. **Verlas una por una** y escribir la gramática (capa 2) — no resumir, describir.
4. Muestrear colores píxel a píxel de las piezas reales; conseguir los archivos de
   fuente reales; pedir los logos oficiales en PNG con transparencia.
5. Llenar `marca.json` y `CLAUDE.md`.
6. Reproducir **una pieza ya aprobada** desde cero con el sistema. Si no queda
   idéntica, el sistema todavía está mal. Ese es el examen de admisión.
7. Llenar `CHECKLIST-CLIENTE.md` con lo que faltó y pedirlo.

---

## 8. Reglas duras acumuladas — valen para todas las marcas

1. **No inventar sistema de marca.** Si hay plantilla viva aprobada, se extiende.
2. **CTAs y textos en pantalla, literales del brief.**
3. **Packshots reales siempre.** La IA hace fondos, no productos.
4. **Nunca espejar un packshot** (deja la marca al revés).
5. **Precios en CLP chileno**: `$9.900`, punto de miles, sin decimales, sin centavos.
6. **Zonas seguras Meta** en toda pieza de pauta.
7. **Nunca cruzar ciudades/sucursales** en las fotos.
8. **Números y precios** van en la tipografía que la marca define para cifras
   (en EBEMA es Helvetica Bold — no es un detalle, la diseñadora lo corrigió).
9. **QA de recortes con zoom 3×** antes de renderizar cualquier cutout.
10. **Pelo suelto o crespo no se recorta** — se genera la persona sobre el fondo final.
11. Al cerrar, actualizar el manual de la marca con lo aprendido. **El feedback del
    cliente se codifica, no se recuerda.**
