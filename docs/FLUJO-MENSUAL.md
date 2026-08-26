# El flujo de trabajo — cómo se corre un mes con cada cliente

> Es el mismo para todos. Lo que cambia por marca está en `clients/<marca>/CLAUDE.md`.

---

## El ciclo, en una imagen

```
①  KAM cierra el brief         →  el cliente aprobó textos, precios y fechas
②  /al-dia                     →  Claude ve qué hay nuevo en Drive
③  /pieza <marca> <qué>        →  produce
④  /qa <marca>                 →  control de calidad duro
⑤  revisión interna            →  diseño mira antes que el cliente
⑥  entrega a Drive             →  a la carpeta del mes del cliente
⑦  feedback del cliente        →  comentarios EN los archivos de Drive
⑧  /pieza … aplica el feedback →  ronda 2
⑨  aprobado                    →  la corrección se escribe en el manual
```

El paso ⑨ es el que hace que el próximo mes cueste menos. **No es opcional.**

---

## ① El brief — sin esto no se parte

**Es responsabilidad del KAM**, no del diseñador. Un brief listo trae, por pieza:

- Formato y medidas
- Dónde se publica y con qué objetivo
- El botón del anuncio
- **Los textos FINALES** — antetítulo, título, bajada, CTA
- Qué se ve en la imagen, o qué archivo usar
- Si hay promoción: precio, vigencia y el legal exacto
- Los lineamientos gráficos particulares, numerados

El formato completo está en [`BRIEF-DE-DISENO.md`](BRIEF-DE-DISENO.md). El modelo es el
«Brief Diseño Septiembre 2026 — REVEX» de Serena: con un brief así **no hay una sola
pregunta de vuelta**; sin él, son tres o cuatro rondas.

> **Regla:** los textos van **literales** a la pieza. Si cambian después, hay que rehacer.
> Por eso tienen que venir aprobados por el cliente, no en borrador.

---

## ② Ponerse al día

```
/al-dia
```
Antes de producir, siempre. Claude revisa el Drive de la agencia y las carpetas de las
diseñadoras, y te dice qué apareció desde la última vez: grillas nuevas, editables
nuevos, piezas aprobadas, comentarios de clientes sin leer.

Si un cliente cambió su estilo, esto es lo que lo detecta.

---

## ③ Producir

```
/pieza <marca> <lo que necesitas>
```

Lo que Claude hace por dentro, siempre en este orden:

1. **Carga el sistema** — `clients/<marca>/CLAUDE.md` y `marca.json`
2. **Lee el brief** donde el manual diga que vive, y saca los textos verbatim
3. **Resuelve el material** bajando por la jerarquía: foto aprobada → banco curado →
   e-commerce → editables → pieza aprobada → IA (solo ambiente)
4. **Arma** con el pipeline de la marca
5. **Hace QA**
6. **Entrega** con su `ENTREGA.md`

Si la marca no tiene sistema, se detiene y lo dice. No inventa.

---

## ④ Control de calidad

```
/qa <marca o carpeta>
```
Compara contra una referencia aprobada del cliente y corre el checklist de esa marca.
Verifica además, en todas: zonas seguras de Meta, choques de texto, proporción de los
packshots, precios en CLP, legales obligatorios.

**Una pieza que no pasó QA no existe.** No se muestra ni internamente.

---

## ⑤–⑥ Revisión y entrega

Revisión interna primero (diseño), después el cliente. La entrega va a la carpeta del
mes en el Drive del cliente — la ruta está en el manual de cada marca — con un
`ENTREGA.md` que explica qué es cada pieza, de dónde salió cada texto y qué quedó pendiente.

---

## ⑦ El feedback — que llegue bien

> **Pídele al cliente que comente EN los archivos de Drive**, no por WhatsApp ni correo.

Los comentarios de Drive se leen automáticamente, quedan trazables y se aplican uno por
uno sin que se pierda ninguno. Por WhatsApp se pierden y no hay registro de qué se pidió.

---

## ⑨ Cerrar el ciclo — lo que más importa

Cuando el cliente corrige algo, **se escribe en `clients/<marca>/CLAUDE.md`** en el mismo
momento. Ejemplos reales de correcciones que hoy son regla:

- «el logo va pegado arriba, no al medio volando» → Revex y Casablanca
- «los números van en Helvetica Bold» → EBEMA
- «la taza dice KIMBO, hay que borrar el logo» → Between
- «las botellas no se tocan» → CAVA, y se volvió regla de todo el estudio

El manual **es la memoria del estudio**. Un cliente que corrige dos veces lo mismo es
una señal de que no se escribió la primera vez.

---

# El mes, según el tipo de cliente

No todos funcionan igual. Hay tres modos:

## Modo A — Grilla mensual (EBEMA, Selfie, Between, Revex, Casablanca)
El mes viene en una **grilla** (un Sheet) con las piezas por semana. Se produce por lote.

```
/al-dia
/pieza <marca> las piezas de la semana 1 según la grilla
/qa <marca>
```
Topes típicos por mes: 8 gráficas, 3 UGC, 2–4 reels, 1 banner semanal.

## Modo B — KV mensual + derivados (CAVA)
Se construye **un key visual al mes** y de ahí salen todos los mailings **cambiando solo
la barra del llamado comercial**. El KV no se rediseña.

```
/pieza cava el KV de octubre                     ← primero, una vez
/pieza cava el mailing de «último día» con …     ← después, los derivados
```

## Modo C — A pedido (one shots, campañas, packaging)
No hay grilla: llega un brief puntual. Mismo flujo, pero el brief tiene que venir
completo porque no hay contexto mensual del que colgarse.

---

# Qué hace cada quién

| Rol | Responsabilidad |
|---|---|
| **KAM** | Cerrar el brief con el cliente. Textos, precios y fechas **finales**. Conseguir el material que falte |
| **Medios** | La grilla y los formatos que pide cada plataforma |
| **Diseñador + Claude** | Producir, hacer QA, entregar, aplicar feedback, **y escribir lo aprendido en el manual** |
| **Cliente** | Aprobar textos antes de producir. Comentar **en los archivos de Drive** |

---

# Lo que nunca se hace

1. Producir sin los textos finales aprobados
2. Inventar un sistema de marca cuando el cliente ya tiene plantilla viva
3. Publicar un precio o porcentaje sin confirmación escrita del cliente
4. Tocar un packshot regulado: etiquetas, tamaños relativos, sellos de premio
5. Entregar sin el legal obligatorio de la categoría
6. Mostrar una pieza que no pasó QA
7. Cerrar un mes sin escribir en el manual lo que el cliente corrigió
