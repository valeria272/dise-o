---
name: sistema-de-marcas
description: PUNTO DE ENTRADA del estudio de diseño — el método por marca, los 6 comandos, dónde está cada cosa y el estado de las 9 marcas. Leer esto primero al abrir un chat de trabajo de cliente
metadata:
  type: project
---

# El estudio de diseño COPYLAB — empieza por acá

Todo el trabajo de cliente de `EDITOR VIDEOS` corre sobre un método único desde el
**25-08-2026**. Si vas a hacer una pieza para un cliente, **lee primero**
`docs/SISTEMA-DE-MARCAS.md` en el repo — es la ley.

## La regla madre
**El brief manda el QUÉ; el sistema de marca manda el CÓMO.** Una pieza nueva
**extiende** el sistema aprobado del cliente; nunca inventa uno, aunque el brief
describa otra cosa. Si la marca no tiene sistema, se abre con `/marca-nueva` — no se
improvisa.

## Los 6 comandos
| Comando | Para qué |
|---|---|
| `/al-dia [marca]` | **SIEMPRE antes de producir.** Qué hay nuevo en Drive: grillas, editables, comentarios |
| `/pieza <marca> <qué>` | Producir: carga el sistema, lee el brief, arma, QA y entrega |
| `/qa <marca o ruta>` | Control de calidad antes de mostrar nada |
| `/adn <marca> <id-drive>` | Extraer el sistema real desde los editables del diseñador |
| `/marca-nueva <nombre>` | Abrir un cliente que no existe todavía |
| `/arranque` | Primer arranque en una máquina nueva |

## Dónde está cada cosa
```
clients/<marca>/CLAUDE.md     el manual (gramática, imagen, copy, QA, errores)
clients/<marca>/marca.json    la ficha máquina (colores, fuentes, formatos, geometría)
clients/_estado-sync.json     última revisión de Drive
src/brand/<marca>.ts          kit en código para video
docs/SISTEMA-DE-MARCAS.md     el método — LA LEY
docs/FLUJO-MENSUAL.md         cómo se corre un mes por cliente (3 modos)
docs/QUIEN-HACE-QUE.md        qué debe cada persona del equipo
docs/ESTADO-MARCAS.md         madurez y pendientes de las ~24 cuentas
docs/MAPA-DRIVE.md            IDs de Drive + cómo llegar a las diseñadoras
docs/BRIEF-DE-DISENO.md       el contrato de entrada
docs/QUE-PUEDO-Y-QUE-NO.md    límites reales y estado de los MCP
```

## Estado de las marcas (25-08-2026)
**Listas para producir (5):** EBEMA/Click · Selfie · Between ·
Tierra Calma · CAVA.
**Parciales:** MyZoo (envase sí, digital no) · Abakos (gramática sin medir).
**Sin sistema:** Nueva Urbe, Traverso, QB, Piso 18 y ~11 más — ver [[cartera-real-y-drive]].

## Reglas globales que valen para TODA marca
1. No inventar sistema de marca — ver [[no-inventar-sistema-de-marca]]
2. Textos y CTAs **literales del brief**; si falta un dato, se pregunta
3. **Material regulado** (`docs/SISTEMA-DE-MARCAS.md` §2.b): no tocar etiquetas,
   tamaños relativos ni sellos de premio; legal obligatorio de la categoría siempre
4. **Verificar la proporción** de todo packshot: ancho/alto final == el del original
5. **Derechos de imagen y licencias de fuente** (§2.c): una foto de sesión no habilita
   a publicar a la persona; muchas fuentes «gratis» son demo de uso personal
6. Zonas seguras de Meta en toda pieza de pauta
7. **Cuando el cliente corrige, se escribe en el manual de la marca** — en el mismo
   commit. El manual es la memoria del estudio

**Why:** se acumulaba deuda de criterio — cada mes se re-deducían colores, medidas y
reglas que el cliente ya había corregido, y el feedback se perdía entre chats.

**How to apply:** ver también [[flujo-operativo-estudio]] (el ciclo de 9 pasos),
[[adn-desde-editables]] (la mejor fuente para levantar una marca) y
[[traspaso-zip-estudio]] (cómo se le pasa el estudio a otro diseñador).
