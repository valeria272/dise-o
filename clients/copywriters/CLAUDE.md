# COPYWRITERS · Grupo Copylab — manual de la cuenta propia

**Ámbito:** la cuenta `@copywriters.cl`. **Este criterio no se traspasa a ningún
cliente**, igual que el de Paulina no cruza a Hilton (`docs/SISTEMA-DE-MARCAS.md`).

**Firma el criterio y aprueba:** Valeria Traverso.

---

## ⛔ El único sistema vigente — desde el 01-10-2026

El sistema visual de esta cuenta **se creó con este mismo estudio y se cerró el 01-10-2026**
(CASO 001 aprobado). Es el único que existe para producir:

| Qué | Dónde |
|---|---|
| **La ley de ejecución** (el CÓMO) | `creative-system/SISTEMA-VISUAL-2609/reference/CARRUSEL_CASO_001_LEY_30-09.png` |
| El sistema (paleta, voces, taxonomía) | [`creative-system/SISTEMA-VISUAL-2609/LEEME.md`](../../creative-system/SISTEMA-VISUAL-2609/LEEME.md) + `reference/BOARD_SISTEMA_VISUAL_29-09.png` |
| Dirección de arte RRSS (§13 = la ley destilada) | [`creative-system/SISTEMA-VISUAL-2609/DIRECCION-DE-ARTE-RRSS.md`](../../creative-system/SISTEMA-VISUAL-2609/DIRECCION-DE-ARTE-RRSS.md) |
| Las reglas destiladas | `APRENDIZAJES.md` — **R-24 a R-40**; el orden de corrección es **R-34** |
| Tokens · motor · mockups | `src/brand/copylab/tokens-v2.json` · `sistemaV2.ts` · `piezasV2.tsx` · `mockups.tsx` |
| La pieza de referencia en código | `src/compositions/copylab/Caso001.tsx` |
| Ficha y compuerta | `marca.json` · `reglas.yaml` |

**No se analiza el look and feel anterior de la cuenta.** Ni el feed publicado, ni
el Creative OS v1.0 (03-09), ni el pack `MASTER/` (24-09), ni `GclPost`, ni piezas
de lotes viejos (`out/copylab/v1`, `v2`…). Son registro histórico: no son
referencia, no se miden y no se usan para «extender» nada. Si un archivo viejo
contradice al sistema vigente, se corrige el viejo sin consultar.

En una línea: **Bebas Neue Pro SemiExpanded/Expanded ExtraBold** (nunca condensada) ·
mano **Balloon D Extra Bold** como gesto · cuerpo **Neue Haas Grotesk Text Pro** ·
negro `#0B0B0B`, off white `#F5F3EE`, **rosa `#FF3D9C`** como señal · el color es
taxonomía por tipo de contenido.

---

## Quién hace qué

| | Quién |
|---|---|
| **La grilla** (qué se publica, cuándo, con qué copy) | **El equipo de redes sociales.** El estudio no arma grillas de esta cuenta |
| Dónde llegan las grillas | Drive → `COPYWRITERS / GRILLAS IA` (`17K33Ru-CxTNwxfKCCJcmETHUsoLqKPO-`) |
| Producir las piezas de la grilla con el sistema | El estudio (`/pieza copywriters …`) |
| Aprobación de dirección de arte | Valeria |

El brief manda el QUÉ (la grilla de redes); el sistema manda el CÓMO. Si la grilla
pide algo que el sistema no resuelve, se pregunta a Valeria — no se inventa.

## Dónde se deja todo

**Carpeta de la cuenta en Drive:** `1doZoVI8FikFiF-6xGjKwUP6KCGs0wcFU`
(<https://drive.google.com/drive/folders/1doZoVI8FikFiF-6xGjKwUP6KCGs0wcFU>).
Todo lo que se entregue de esta cuenta va ahí. Adentro:

- `GRILLAS IA/` — las grillas que deja redes sociales (entrada)
- `ASESORÍAS/AUDIT - ABR 26/` — material antiguo de abril; no es del feed

El render y su script vuelven al repo el mismo día (`out/copylab/…`); la entrega
final sube a la carpeta de Drive.

---

## Producir una pieza

```
GRILLA DE REDES → QUÉ MANDA (R-16) → IMAGEN → DISEÑO CON LA LÁMINA AL LADO → QA
```

**Una pieza = un archivo** en `src/compositions/copylab/`, con su dirección de arte en
la cabecera. No existe una composición genérica con prop `plantilla`.

```bash
./node_modules/.bin/remotion still CL-<Nombre> out/copylab/<lote>/01.png \
  --browser-executable="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Compuertas técnicas — con el venv compartido (con el python3 del sistema falta
# scipy y las reglas degradan a warning en silencio, R-37)
/Users/Vale/copylab-venv/bin/python3 qa/motor.py --marca copywriters out/copylab/<lote>/*.png
/Users/Vale/copylab-venv/bin/python3 qa/borde.py out/copylab/<lote>/*.png
```

El QA técnico no dice si la pieza está bien. Lo que decide es el **VISUAL MATCH
TEST**: al lado de la lámina ley, ¿podría estar en ella? (R-12). Si una lámina se
ve mal, se corrige en el orden de **R-34**: ancho y peso tipográfico → grosor del
trazo → sombra sobre foto → caja del texto funcional → cromo del mockup →
temperatura de la foto.

⚠️ En este Mac hace falta el sandbox fuera de iCloud: memoria `render-remotion-fix-mac`.

---

## Ejecución probada (01-10-2026, CW-01 · CW-04 · CYBER MOOD)

- **Fotografía primero, aunque el brief diga «tipográfico».** La pieza tipográfica sobre negro fue X-15.
- **Sin cuerpo de texto en Neue Haas dentro de la pieza** (R-44 ✔×3). Se dice en Bebas o en Balloon; la fuente de un dato va al caption.
- **Juega con la tipografía en cada gráfica** (R-45 ✔×3): Bebas Light 300 contra Expanded ExtraBold, Bebas en contorno; Balloon por un trazado con `ManoCurva` (kit), como anillo, arco, o escrito con tinta sobre un objeto de la foto.
- **Video dentro del carrusel** cuando hay algo vivo (R-46): Kling 2.5 Pro desde la foto, `scripts/magnific-video.py`, **de a un clip** (en paralelo Magnific responde «Error consuming credits»). Si hay algo montado encima, se mide el clip cuadro a cuadro.
- **Motion graphic = un objeto con chiste hecho en código** sobre una foto (A-10): caída con resorte, péndulo, giro 3D. La letra sale perfecta porque no la dibuja la IA.

## Lo que no se publica

- Cifras sin fuente verificada ni casos de clientes sin autorización (R-10). El CASO
  001 (Santa Gota) está aprobado **como diseño**, no para publicar.
- Fotografía del equipo, la cultura o el backstage generada con IA: se fotografía de verdad.
- Recreaciones IA sin declarar (R-11).
