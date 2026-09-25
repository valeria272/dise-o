# Bitácora — Petra Funeraria

Cliente de paid media de Copylab (Google Search + Meta click-to-WhatsApp). El contexto de
campañas, CRM y marcaje vive en `AGENTE PAID MEDIA*/PETRA/` y en la memoria de ese proyecto.
Acá se guarda lo que produce el estudio.

## 2026-09-22 — Valeria Traverso (con Claude)

**Qué se hizo:** Landing de cotización de servicios funerarios, que es la **variante B de un test A/B** contra la URL actual de `PETRA-Search-Inmediata`.
- **Diseño:** mantiene el look & feel medido del sitio. Usa Mandrel Cond + PP Neue Montreal, el gris carbón `#3f3f3f`, los botones de filete, el óvalo de flores y las fotos propias de Petra.
- **Estrategia:** sigue el diagnóstico de agosto. El llamado es a pedir una cotización, no un catálogo, con los precios a la vista: Ópalo desde 52 UF y Ónix desde 85 UF.
- **Formulario:** tiene 2 pasos. Primero se elige el tipo de consulta: servicio ahora / comparar precios / anticipar. Después se pide el teléfono como obligatorio y el correo como opcional.
- **Conexiones:** envía por la API de Contact Form 7, que genera el correo al equipo. Además escribe al CRM y emite los mismos eventos de Google Tag Manager que ya usa el sitio.

**Dónde quedó:** `clients/petra/landing-cotizacion/`.
- La fuente es `landing-b.src.html`, y `build.py` genera los dos formatos.
- `paquete/wordpress/` trae el bloque para pegar, en una sola línea, y el formulario de CF7.
- `paquete/pagina-independiente/` trae el `index.html` con header, footer, GTM y GA4 propios. Envía a CF7 con `no-cors` porque el servidor de Petra no devuelve CORS.
- ZIP entregado a Valeria en el Escritorio y en Descargas: `petra-landing-cotizacion.zip`.
- Las tipografías no van en git; ver `fonts/LEEME.txt`.
- **Nada está instalado en el sitio.** El login al WordPress desde Claude Code lo bloqueó el control de permisos. Valeria lo monta desde otro agente web.

**Qué sigue:**
- Crear en el WordPress el formulario de CF7, duplicando el id 6. Poner su ID en `data-cf7-id` y publicar la página en `/cotizar-funeral/` con noindex.
- Hacer **una** prueba real: correo + fila en el CRM + evento en la vista previa de GTM.
- Serena arma el experimento 50/50 en Google Ads.

**Abierto:**
- **Volumen:** con ~270 clics/mes, detectar que B duplica la conversión exige ~800 clics por variante, unos 6 meses. Hay que acordar la regla de decisión antes de partir.
- **Precios contradictorios en el sitio de Petra:** la página de planes dice 52–200 UF y la de preguntas frecuentes, 65–195 UF.
- **Notificaciones:** `SLACK_WEBHOOK` del endpoint del CRM está vacío, así que el correo de CF7 es el único aviso al equipo.
- **Licencia de las fuentes,** si se publica fuera de petrafuneraria.com.
- **Rotar la clave** del usuario «editor» del WordPress, que quedó escrita en Slack y en el chat.
