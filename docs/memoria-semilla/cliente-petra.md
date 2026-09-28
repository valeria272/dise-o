---
name: cliente-petra
description: "PETRA — cerebro del cliente: 12 reglas firmes, última cosecha 2026-09-26. Generado desde clients/petra/APRENDIZAJES.md; leerlo antes de diseñar para petra"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/petra/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para petra: no se traspasa a otra marca.

Criterio: **Valeria Traverso (lo que produce el estudio); las piezas finales de Meta las ejecuta el equipo de diseño de Petra** · Aprueba: **sin identificar (§8)**

## Reglas más confirmadas
- **R-02** · No inventar nada que Petra no publique: testimonios, tiempos de respuesta («te llamamos en 30 min»), precios no publicados (el 11 UF de la planificación anticipada viene de prensa: confirmar antes) — _landing 22-09; propuesta 10-09_ · ✔×2
- **R-03** · Precios en **UF**, nunca en pesos (la UF cambia cada día y obligaría a rehacer piezas) — _propuesta Meta, 10-09; landing 22-09_ · ✔×2
- **R-04** · La pieza pide **cotizar, no el catálogo**: el titular deja de preguntar y carga el dato (precio, plan, incluidos) — _diagnóstico de la propuesta Meta 10-09 (5 de 7 anuncios activos eran una pregunta sin respuesta); landing 22-09_ · ✔×2
- **R-01** · Todo texto informativo sale **literal** de petrafuneraria.com, con trazabilidad frase por frase (`FUENTES.md`) — _landing de cotización, Valeria, 22-09-2026_ · ✔×1
- **R-05** · Gramática de las piezas de Meta: campo plano + titular en versales + foto en óvalo + logotipo abajo; máximo 3 bloques (titular, dato, logo); el logo sobre el campo plano, nunca sobre la foto — _propuesta 10-09, sobre «Anuncio 5 | vertical», la que mejor rinde_ · ✔×1
- **R-06** · Nada de botones dibujados en la gráfica (Meta pone el suyo); foto recortada a *cover*, nunca estirada; sin palabras solas en la última línea del titular — _propuesta 10-09_ · ✔×1
- **R-07** · Foto real de servicio y coherente con el titular: si habla del ataúd, en la foto se ve un ataúd — _propuesta 10-09 (se cambió el detalle de mimbre por la urna Canciller lenga)_ · ✔×1
- **R-08** · Formulario: el teléfono es obligatorio y el correo/mensaje, opcional; el primer paso es un clic (servicio ahora / cotizar / anticipar); quien elige «servicio ahora» ve el teléfono antes que los campos — _landing 22-09, sobre el diagnóstico del 10-08 (3 de 49 leads traían teléfono)_ · ✔×1
- **R-09** · La landing se monta **dentro** de petrafuneraria.com (bloque HTML en `/cotizar-funeral/`, noindex); no como artifact ni en Vercel — _landing 22-09_ · ✔×1
- **R-10** · En WordPress se pega en **una sola línea**, JS sin `//` y todo con prefijo `#plp` + reset: `wpautop` y el tema rompen CSS/JS — _landing 22-09 (así se descuadró la v2 de /gracias/)_ · ✔×1
- **R-11** · Fuera del dominio o con `?plp_demo=1` la landing corre en modo demo: nunca generar leads falsos; una sola prueba real, marcada «PRUEBA interna» en el CRM — _landing 22-09; memoria `probar-sin-avisarle-al-cliente`_ · ✔×1
- **R-12** · Las campañas de Petra no se tocan desde otro agente: el experimento lo arma Serena (Google Ads → Experimentos, 50/50, sólo cambia la URL final; nunca redirect por JS) — _landing 22-09_ · ✔×1

## Lo que ya costó rondas
- **X-01** · Versión larga de la landing (proceso paso a paso, cuota mortuoria como sección, «Nuestra funeraria», preguntas frecuentes): se cortó a «hace una sola cosa, cotizar» — _Valeria, 22-09_
- **X-02** · Frases interpretadas que el sitio no dice: «precios claros», «sin costo ni compromiso», «un director funerario contigo», «música en vivo» — _eliminadas de la landing, 22-09_
- **X-03** · Anuncios que preguntan y no responden («¿Cuánto cuesta un funeral en Petra?» sin decirlo) y cierran en «Conversemos»: traen conversaciones que piden catálogo — _diagnóstico, propuesta 10-09_
- **X-04** · Gráfica peleada con el copy (A7: la imagen pregunta el precio y el texto habla de planificar en vida) — _propuesta 10-09_
