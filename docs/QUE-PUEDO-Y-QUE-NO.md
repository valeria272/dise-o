# Qué puede hacer Claude en este estudio, y qué no

> Escrito el 25-08-2026 con lo verificado en esta máquina y en el Drive de la agencia.
> Sirve para no pedirle a Claude cosas que no puede, y para no hacer a mano cosas que sí.

---

## ✅ Lo que hace bien, hoy, sin ayuda

| Tarea | Detalle |
|---|---|
| **Producir gráficas de una marca con sistema** | EBEMA, Revex, Casablanca, Selfie, Between, Tierra Calma. Feed, story, mailing, carrusel |
| **Leer el brief del Sheet o Doc** y sacar los textos literales | Incluye hojas con celdas de imagen y notas |
| **Bajar material del Drive del cliente** | Referencias, fotos aprobadas, editables, briefs |
| **Leer los comentarios del cliente** en los archivos de Drive | Y aplicarlos uno por uno, trazables |
| **Subir la entrega** a la carpeta del cliente | Con `ENTREGA.md` explicando cada pieza |
| **Variantes en volumen** | 11 sucursales × 2 formatos, o 11 variantes de precio. Es donde más rinde |
| **Reels y video** | Remotion, voz en off (edge-tts), música, cierres oficiales del cliente |
| **QA con criterio** | Zonas seguras, choques, recortes con zoom, colores muestreados píxel a píxel |
| **Medir un sistema de marca** desde piezas aprobadas | Colores, geometría, tipografías. Es como se armó EBEMA |
| **Packshots desde e-commerce** | Shopify (Selfie) y WooCommerce vía JSON público |

## ⚠️ Lo que hace, pero necesita que alguien valide

| Tarea | Por qué |
|---|---|
| **Imágenes con IA** | Genera ambiente y fondos. **El producto y el logo siempre son reales.** Cada imagen necesita ojo humano antes de componer |
| **Proponer textos** | Puede escribir copy, pero lo que va en la pieza sale del brief. Si propone, hay que marcarlo como propuesta |
| **Marcas sin gramática medida** | Abakos, Nueva Urbe, Traverso: puede hacer algo razonable, pero no está calibrado contra piezas aprobadas |
| **Decidir si una promo es publicable** | Necesita confirmación escrita del cliente para cualquier precio o porcentaje |

## ⛔ Lo que NO puede

| No puede | Por qué | Qué hacer |
|---|---|---|
| **Abrir, editar o exportar archivos `.ai`, `.psd`, `.indd`** | No tiene Adobe | Pedir el editable empaquetado; las carpetas `Links/` y el `Informe.txt` sí se leen |
| **Usar fuentes que no tiene el archivo** | IvyOra (Adobe Fonts) y Agrandir (de pago) no se empaquetan | Activar en Creative Cloud, o pedirle el archivo al cliente |
| **Bajar archivos >10 MB por el conector de Drive** | Límite del MCP | `curl` si es link-shared, o que lo compartan por link |
| **Ver carpetas de Drive con permisos propios** | Ej: la carpeta de diseño de Coni | Pedir acceso explícito |
| **Bajar archivos de terceros con el token OAuth** | El scope es `drive.file`: solo archivos propios | Usar el conector MCP, o que muevan el archivo a una carpeta compartida |
| **Generar personajes IA consistentes** | Higgsfield está desconectado | Reconectar el conector, o usar Magnific/Freepik con sus límites |
| **Aprobar una pieza** | El criterio final es del cliente y de la jefa de diseño | Siempre entrega a revisión |
| **Inventar un dato que falta** | Regla dura | Lo marca como pendiente y pregunta |
| **Publicar o lanzar campañas** | No es su rol acá | Eso vive en `AGENTE PAID MEDIA/` |

---

## Claude Design (`/design`) — ¿suma o es lo que ya hacemos?

**Veredicto corto: no reemplaza el pipeline. Suma en una etapa distinta.**

**Qué es:** genera un lienzo con varias mesas de trabajo, publicado como Artifact,
donde una persona puede seleccionar elementos, editar textos en línea, mover cosas
y guardar una versión nueva.

**Por qué NO sirve para producir piezas de cliente:**

1. **El formato de salida no calza.** Entrega una página web, no un PNG de
   1080 × 1350. Meta necesita el píxel exacto y el archivo pesa lo que pesa.
2. **Invita justo a la deriva que el sistema evita.** El valor de `clients/<marca>/`
   es que una pieza **no puede** salirse del sistema aprobado. Un lienzo libre de
   edición reintroduce el problema que costó cuatro rondas en Selfie y en EBEMA.
3. **Las tipografías de pago no viajan.** Agrandir, IvyOra y Helvetica del kit están
   licenciadas al cliente; en el repo se controlan, en un artifact publicado no.

**Dónde sí conviene usarlo:**

| Etapa | Por qué ahí sí |
|---|---|
| **Propuestas a cliente** | Mostrar 3 rutas visuales antes de que exista un sistema. Nadie las va a pautear |
| **Marca nueva (`/marca-nueva`)** | Poner las referencias del cliente lado a lado en un lienzo para estudiar la gramática |
| **Presentar la grilla del mes** | Que el cliente vea las 8 piezas juntas y comente, sin abrir Drive |
| **Piezas internas de la agencia** | Donde no hay un sistema de cliente que respetar |

**Regla:** si la pieza la va a ver un cliente como anuncio, va por el pipeline.
Si es para conversar, puede ir por el lienzo.

---

## Conectores MCP — estado real (verificado hoy)

| Conector | Estado | Impacto si falta |
|---|---|---|
| **Google Drive** | ✅ funcionando | **Es el único imprescindible.** Sin él no hay referencias ni entregas |
| **Meta Ads** | ✅ disponible | Sin él no se pueden bajar las creatividades ya publicadas |
| Context7 | ✅ disponible | Menor |
| Gmail · Calendar · Slack · Windsor.ai | ⚠️ requieren autorización | Menor para diseño |
| **Higgsfield** | ❌ desconectado | **Bloquea** los personajes IA de Abakos y el UGC |
| **Canva** | ❌ desconectado | Bloquea el brand kit de Canva y Magic Studio |

No hay servidores MCP locales: todo son conectores de claude.ai. Cada diseñador los
activa en **claude.ai → Settings → Connectors** con su correo `@copywriters.cl`.
Los conectores **no viajan en el ZIP**.
