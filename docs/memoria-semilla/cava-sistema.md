---
name: cava-sistema
description: CAVA es el e-commerce de Viña Morandé — un KV mensual (fondo Magnific) del que salen todos los mailings cambiando solo la barra del llamado; botellas y etiquetas intocables; legal de alcohol obligatorio
metadata:
  type: project
---

**CAVA no es una marca de vino: es el e-commerce que vende el portafolio de Viña
Morandé** (Morandé, Mancura, 7 Colores, Adventure, Vistamar). Manual completo en
`clients/cava/CLAUDE.md`, medido el 25-08-2026 sobre las piezas reales.

⭐ **La regla madre:** UN key visual al mes, con el fondo generado en **Magnific**.
Los mailings y piezas de campaña son **el mismo KV** donde cambia **una sola cosa: la
barra dorada con el llamado comercial** ("YA COMENZÓ", "LLÉVATE VINOS DE EXCELENCIA",
"POCAS HORAS"…), más las botellas y precios. El KV **no se rediseña**. Por eso una
campaña es un embudo: PRE → YA COMENZÓ → CARRITO → POCAS HORAS → ÚLTIMO DÍA → SE AGOTAN.

⛔ **Las botellas no se tocan.** Son bottle shots oficiales de la viña y las etiquetas
son de un producto regulado. Prohibido cambiar tamaños relativos, editar etiquetas,
deformar, o inventar/mover sellos de premio (Decanter, James Suckling, Descorchados,
Tim Atkin, Vinous, La Cav). Solo se permite recortar, escalar el conjunto y ajustar
sombra. Los bottle shots viven en el **SharePoint de Morandé** (no tenemos acceso).

⚠️ **Legal obligatorio por ley chilena** en TODA pieza, arriba a la derecha pegado al
borde: caja negra «ADVERTENCIA / EL CONSUMO DE ALCOHOL EN MENORES DE 18 AÑOS SE
ENCUENTRA PROHIBIDO / Ministerio de Salud» + banda tricolor azul `#0063AF` /
blanco / rojo `#E73439`. Sin eso no se entrega.

**Colores medidos:** fondo satén negro texturado `#333234` → `#1A1A1B` → `#070707`
(NO negro plano). Dorado como **degradado metálico**: sombra `#5F3C12` → medio
`#C9A24E` → brillo `#FFF7C1` (nunca plano). Naranjo del isotipo `#DD660E`.

**Why:** es la cuenta donde más fácil se rompe algo grave — manipular una etiqueta de
vino o publicar sin la advertencia son problemas legales, no de diseño.

**How to apply:** la generalización quedó como regla global en
`docs/SISTEMA-DE-MARCAS.md` §2.b «Material regulado». Aplica también a MyZoo (claims
sanitarios) y Abakos (producto financiero). Ver [[adn-desde-editables]].

✅ **Tipografías resueltas** con `/adn` (25-08): titulares en **Bebas Neue Pro**
(familia completa, incluidos SemiExpanded y Expanded) — es display de **solo versales**,
por eso todo va en mayúscula. Cuerpo en **Brandon Grotesque** Light/Bold. Ambas de
**Adobe Fonts**: se activan en Creative Cloud, no se empaquetan. La Bebas Neue libre
(OFL) quedó en `public/assets/cava/fonts/` como base para maquetar.

⭐ **El recuadro del Ministerio de Salud usa `gobCL Bold`**, la tipografía oficial del
Gobierno de Chile (libre) — no una cualquiera. Va incrustada en el editable.

**Mesas de trabajo reales:** el KV del mes es **1080×1350** (feed 4:5); el banner web
es **4600×2200**. Tinta plana declarada: **PANTONE 159 U**.

**Los bottle shots** viven en `MORANDE/Bottle Shot/NUEVA IMAGEN - NEW IMAGE/<LÍNEA>/
<CEPA>/` (SharePoint de la viña + disco externo de la diseñadora), en 1.400–4.100 px
de ancho por 4.000–10.000 de alto. Los sellos, en `MORANDE/material marca/MEDALLAS/`.

✅ **Verificado que NUNCA se deforman:** contrastando nativo vs colocado, cada botella
conserva su ratio al milésimo (Black Series Syrah 0,338 = 0,338). De ahí salió la
**regla global de verificación de proporción** en `docs/SISTEMA-DE-MARCAS.md` §2.b.

**Matiz sobre el fondo:** el KV del Cyber enlaza **23 fondos distintos** — conviven
generados con IA (nombres UUID, patrón Magnific/Freepik) y **stock descargado**
(nombres descriptivos largos). Se prueban muchos hasta dar con el del mes.
