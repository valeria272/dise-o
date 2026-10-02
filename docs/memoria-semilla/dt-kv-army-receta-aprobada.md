---
name: dt-kv-army-receta-aprobada
description: "Eli 02-10 «aprobados, guarda en tu memoria» — DT campaña ARMY (preventa Tarifa ARMY): KV de post 4:5 en 3 opciones tras 9 rondas; el molde es el Cyber DT de mayo, un solo morado medido en el hotel, y lo que Eli corrigió ronda a ronda"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f8de9cbd-b13e-44e6-9f03-a0caa5a889ba
  modified: 2026-10-02T17:54:15.220Z
---

Eli, 02-10-2026: aprobó el **KV de post 4:5 de la preventa «Tarifa ARMY»** de DoubleTree (campaña por
el concierto de BTS, noches del 16 y 17 de octubre) en **tres opciones**, después de 9 rondas, y pidió
guardarlo; el mismo día sumó la dirección del hotel y dos ajustes más, y cerró con «okey, guárdalo en tu memoria». La versión final está en Drive `GRÁFICAS DT ARMY` (`1fu6GlR9uEydLdieUtnIrOrgovibyUOMf`), md5 verificado:
`DT ARMY KV Post PREVENTA - Opción 1 Ciudad / Opción 2 Habitación / Opción 3 Ciudad logo morado.png`.
Código: `src/compositions/hilton/DtArmy.tsx` · `src/DtArmyEntry.tsx` · `scripts/dt-army-{fotos,rendir,revision}.py`.
**Pendiente:** elegir opción → ST, post paid 1:1 y ST paid; después la línea de VENTA ($185.000 → $135.000,
noches 15-16-17, texto en `LINEAS.venta`, sin rendir ni revisar).

**Why:** fueron 9 rondas en una tarde con urgencia; casi todas por cosas que se podían haber acertado antes.

**How to apply (lo que quedó aprobado):**

1. **«Estilo cyber DT» = el Cyber de mayo** (`F:\Paid Hilton 2026\CYBER HILTON 2026 MAYO`, editable y Links
   ahí mismo). NO es el layout de las historias de programa (panel lateral, píldoras): «no es como los
   programas normales, es nuevo». Todo **centrado**: logo · titular en versales Stag · sello a dos voces
   («PREVENTA» + «Tarifa ARMY» en Stag Light Italic) · precio entre dos filetes · botón-barra al pie.
2. **Un solo morado en toda la campaña, el del hotel, MEDIDO en la foto**: `#9639F4` (tono 270°). Titular,
   logo morado, «Tarifa ARMY», tachado y metal del botón salen de ahí. Eli notó cada morado distinto
   (lila 257°, magenta 285° de su propia referencia de metal) y los pidió unificar.
3. **Foto aérea** (`IMAGEN VISTA HOTEL FUCSIA PISO18.tif`): el fucsia se gira a morado por código (sin IA);
   la ciudad queda en **blanco y negro neutro, sin baño ni resplandor morado** («negro atrás y solamente el
   hotel morado»). El hotel va al centro con una zona donde queda SOLO, sin texto ni íconos encima. Velo
   negro parejo arriba (la ciudad se ve detrás del texto) y degradado del pie largo y suave, no en franja.
4. **Precio:** «ANTES $185.000» con **tachado de DOS líneas**, cifra grande en Trade Bold Cn, y debajo, en
   una línea blanca en negrita, «PARA 2 PERSONAS · IVA INCLUIDO».
5. **Fecha** «Noches del 16 y 17 de octubre»: texto suelto en Stag SemiBold, **sin óvalo/cápsula**.
6. **Lo que incluye:** tres columnas iguales, ícono de línea blanco en aro fino (sin relleno ni contorno
   morado) y rótulo centrado debajo. Con el ícono al lado y el texto partido «se ven muy extraños».
7. **Botón (CTA):** placa metálica morada en degradado limpio con franjas de luz, **sin bordes ni brillo
   blancos, sin ícono**, correo en Trade Bold Cn blanco y centrado por la TINTA (medirlo en el render).
7b. ⛔ **Bajo el correo va SIEMPRE la dirección del hotel**: «Av. Vitacura 2727, Las Condes», con ícono de
   ubicación, **en texto blanco suelto en las tres, sin placa ni botón** (Eli sacó la placa blanca que le puse en la habitación). La olvidé y Eli la pidió ya
   aprobadas las tres: «es muy importante». Vale para ST, paid y venta. Está en el copy del brief (📍).
8. **Opción 2 (habitación):** foto real de dos camas («van a ser más amigas») con pie de cama y cojines en
   morado ARMY y globos; **sin luces moradas («parecen de motel»)**. Recuadro del Cyber en **blanco al 80 %**
   con desenfoque suave y filete de 3 px; logo y titular en el morado del hotel, «Tarifa ARMY» morado, y
   **el resto del texto en azul DT `#09194E`, nunca negro**.
9. **Opción 3:** el logo en morado y grande (236 px) hace de «DoubleTree»; el título es sólo «SE VISTE DE
   MORADO», centrado entre logo y «PREVENTA»; sello en Stag Medium; la fecha en BLANCO (la probó en morado y la devolvió a blanco).

**Lo que costó rondas (no repetir):**
- Destellos, resplandores, haces de luz, cápsulas con fondo traslúcido y velos de colores: todo eso lo sacó.
  Eli quiere **limpio**; cada transparencia de más la lee como «pegoteado» o «extraño».
- Sombras/brillos en el texto para salvar legibilidad: «no necesito un filtro, sino que el texto sea morado».
  Si no se lee, se cambia el fondo o el encuadre de la foto, no se le pone glow.
- Desenfoque fuerte del panel: lo quiere mínimo.
- «PREVENTA» en Stag Bold es demasiado gruesa: SemiBold (o Medium).
- Letras muy juntas: Stag en Chrome pide +0,02 a +0,06 em de tracking.
- «Que sea morado» = el elemento se ve morado de verdad; lila claro no cuenta.
- La script del «Day» del Cyber no está en la máquina; Kallimata es muy fina para una palabra corta.
- Los textos: los di provisorios y después aparecieron en el brief de la grilla (DT octubre, hoja FEED,
  fila 10). **Buscar el brief en la grilla ANTES de inventar copy**, aunque el encargo llegue por chat.
  Quedó resumido «2 tragos en QB Restaurant» por su pedido de menos texto (avisado).
- `remotion still` copia `public/` entero (4,3 GB) y se cuelga: armar UN paquete con `--public-dir` mínimo
  (`dt-army-rendir.py`).

Relacionado: [[dt-octubre-2026]], [[no-inventar-sistema-de-marca]], [[cuadro-de-vidrio-de-la-referencia]],
[[leer-el-brief-y-su-carpeta-de-referencias]], [[antes-y-despues-en-html]], [[subir-a-drive-al-aprobar]],
[[sin-antes-en-carpetas-de-semana]], [[avisar-tiempo-estimado]].
