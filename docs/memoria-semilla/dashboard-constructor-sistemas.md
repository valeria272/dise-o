---
name: dashboard-constructor-sistemas
description: "Proyecto \"Constructor de Sistemas\" — dashboard HTML para que los diseñadores construyan/operen sistemas de marca por cliente; estado, decisiones y pendientes"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9e78f706-06cb-442e-95a4-bc081654cd47
  modified: 2026-08-24T16:59:40.167Z
---

**Qué es (definido con Vale el 24-08-2026):** rediseño del rol de diseño en la agencia. Los diseñadores dejan de producir piezas una a una para grillas de mantención y pasan a construir el SISTEMA de cada cliente (style-prompt.md, plantillas, do & don't, QA). Campañas, lanzamientos y piezas hero siguen 100% humanas.

**Flujo de roles (corrección importante de Vale):** el CM escribe el brief y NO toca nada más. El **diseñador a cargo de la cuenta** construye el sistema, y con el brief en mano genera la pieza desde VSCode (como se hizo con EBEMA, Tierra Calma, Nueva Urbe), audita el 100% (QA nunca automático), deja lo aprobado en el Drive de la agencia y lo monta en la grilla que toca (RRSS, email marketing, paid).

**Líneas rojas:** diseñador dueño del style prompt/plantillas; QA nunca automático; si el 30% de piezas falla por el mismo motivo el problema es el sistema (se arregla el style prompt, no la pieza); campañas/hero fuera del sistema.

**Decisiones cerradas:** formatos = estáticas + carruseles + reels; brief mínimo de 6 campos (pieza/formato, objetivo, mensaje, texto y CTA literal, fecha, referencias) — si falta uno se devuelve; dashboard único genérico con progreso en localStorage por navegador; sistema vive en carpeta por cliente `clientes/<cliente>/` (CLAUDE.md, style-prompt.md, do-dont.md, plantillas/, qa-checklist.md, changelog.md), versionado con git vía Claude ("guarda y sube los cambios").

**Entregado:** dashboard publicado como artifact → https://claude.ai/code/artifact/7d8ae390-d32e-4411-9bc8-3edb3879d460 (archivo fuente en el scratchpad de la sesión del 24-08; título "Constructor de Sistemas", favicon 📐, paleta copywriters.cl crema/navy/lima, 3 módulos + ejercicios, 39 ítems marcables). OJO: se publicó bajo el usuario anterior de Claude; si Vale cambió de cuenta y hay que actualizarlo, puede que la cuenta nueva no sea dueña del artifact — en ese caso, republicar como artifact nuevo y avisarle.

**Pendientes:**
1. Vale va a pasar la lista de clientes para los ejercicios → actualizar la sección "Tu primer cliente" del dashboard con los nombres y dejar armado el esqueleto de carpeta de sistema de cada uno.
2. Mapear la carpeta Drive de editables de clientes ([[drive-editables-clientes]]) apenas el conector funcione, y referenciarla como fuente del Paso 1.
