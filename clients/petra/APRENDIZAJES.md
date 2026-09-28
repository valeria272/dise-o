# PETRA Funeraria — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para PETRA.** Nada de acá se copia a otra marca, ni a una hermana.
> Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> ⚠️ **Cuenta con poca evidencia de diseño.** Petra todavía no tiene `CLAUDE.md` ni
> `marca.json` en el estudio: lo que hay es una propuesta de mensajes para Meta (10-09) y una
> landing de cotización (22-09), ninguna con feedback del cliente registrado. El contexto de
> campañas, CRM y marcaje vive en `AGENTE PAID MEDIA*/PETRA/`.
>
> Criterio: **Valeria Traverso (lo que produce el estudio); las piezas finales de Meta las ejecuta el equipo de diseño de Petra** · Aprueba: **sin identificar (§8)**
> Última cosecha: **2026-09-26** · Cosechas: **2**

## 1. Quién es el cliente

Petra Funeraria, «funeraria contemporánea» en Providencia (Av. Francisco Bilbao 926, Santiago).
Cliente de **paid media** de Copylab: Google Search (`PETRA-Search-Inmediata`, `PETRA-Search-Prevision`)
y Meta click-to-WhatsApp. Vende planes con precio público en UF (**Ópalo** 52–69 UF, **Ónix** 85–200 UF)
y planificación anticipada. El sitio habla en femenino plural («**nosotras** nos encargamos») y con
calidez («una despedida hecha con amor»). El problema comercial: llegan conversaciones que piden
el catálogo y no cotizan.

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | Valeria encarga al estudio; **Serena Abarca** lleva las campañas y el test A/B |
| Quién aprueba (cliente) | Sin registrar en el estudio |
| Por dónde llega el feedback | Sin registros todavía |
| Dónde se entrega | ZIP a Valeria (Escritorio y Descargas); ella lo monta desde otro agente web. Fuente en `clients/petra/landing-cotizacion/` |
| Ritmo | A pedido (propuesta de mensajes, landing) |
| Rondas típicas | Sin datos. La landing tuvo una versión larga y una corta por instrucción interna de Valeria |

## 3. Identidad en corto

- **Sitio (landing):** Mandrel Cond + PP Neue Montreal (licenciadas, sin CORS: no cargan desde otro dominio) · gris carbón `#3f3f3f` · botones de filete · el **óvalo de flores** de la portada · fotos propias del sitio.
- **Anuncios de Meta (medidos con PIL sobre sus creatividades):** campo plano oliva `#525834` o celeste `#AAB9BE`, titular en versales, foto en óvalo, logotipo abajo. Logo oficial en `clients/petra/material/logo*.svg`.
- Los mockups de la propuesta usan BodoniModa + Montserrat **sólo como referencia de armado**: no son las fuentes de Petra.
- Formatos Meta: 1080×1350 y 1080×1920 con zonas seguras (250 arriba / 340 abajo en 9:16).

## 4. Reglas firmes

- **R-01** · Todo texto informativo sale **literal** de petrafuneraria.com, con trazabilidad frase por frase (`FUENTES.md`) — _landing de cotización, Valeria, 22-09-2026_ · ✔×1
- **R-02** · No inventar nada que Petra no publique: testimonios, tiempos de respuesta («te llamamos en 30 min»), precios no publicados (el 11 UF de la planificación anticipada viene de prensa: confirmar antes) — _landing 22-09; propuesta 10-09_ · ✔×2
- **R-03** · Precios en **UF**, nunca en pesos (la UF cambia cada día y obligaría a rehacer piezas) — _propuesta Meta, 10-09; landing 22-09_ · ✔×2
- **R-04** · La pieza pide **cotizar, no el catálogo**: el titular deja de preguntar y carga el dato (precio, plan, incluidos) — _diagnóstico de la propuesta Meta 10-09 (5 de 7 anuncios activos eran una pregunta sin respuesta); landing 22-09_ · ✔×2
- **R-05** · Gramática de las piezas de Meta: campo plano + titular en versales + foto en óvalo + logotipo abajo; máximo 3 bloques (titular, dato, logo); el logo sobre el campo plano, nunca sobre la foto — _propuesta 10-09, sobre «Anuncio 5 | vertical», la que mejor rinde_ · ✔×1
- **R-06** · Nada de botones dibujados en la gráfica (Meta pone el suyo); foto recortada a *cover*, nunca estirada; sin palabras solas en la última línea del titular — _propuesta 10-09_ · ✔×1
- **R-07** · Foto real de servicio y coherente con el titular: si habla del ataúd, en la foto se ve un ataúd — _propuesta 10-09 (se cambió el detalle de mimbre por la urna Canciller lenga)_ · ✔×1
- **R-08** · Formulario: el teléfono es obligatorio y el correo/mensaje, opcional; el primer paso es un clic (servicio ahora / cotizar / anticipar); quien elige «servicio ahora» ve el teléfono antes que los campos — _landing 22-09, sobre el diagnóstico del 10-08 (3 de 49 leads traían teléfono)_ · ✔×1
- **R-09** · La landing se monta **dentro** de petrafuneraria.com (bloque HTML en `/cotizar-funeral/`, noindex); no como artifact ni en Vercel — _landing 22-09_ · ✔×1
- **R-10** · En WordPress se pega en **una sola línea**, JS sin `//` y todo con prefijo `#plp` + reset: `wpautop` y el tema rompen CSS/JS — _landing 22-09 (así se descuadró la v2 de /gracias/)_ · ✔×1
- **R-11** · Fuera del dominio o con `?plp_demo=1` la landing corre en modo demo: nunca generar leads falsos; una sola prueba real, marcada «PRUEBA interna» en el CRM — _landing 22-09; memoria `probar-sin-avisarle-al-cliente`_ · ✔×1
- **R-12** · Las campañas de Petra no se tocan desde otro agente: el experimento lo arma Serena (Google Ads → Experimentos, 50/50, sólo cambia la URL final; nunca redirect por JS) — _landing 22-09_ · ✔×1

## 5. Excepciones

- **E-01** · De las 4 propuestas de Meta, sólo la de **urgencia** («Cuando ya pasó») sigue yendo a WhatsApp; las otras van al sitio — _propuesta 10-09_
- **E-02** · Única promesa que la landing hace y el sitio no: «te contactamos por teléfono o WhatsApp». Es inevitable en un formulario, pero hay que confirmarla con Petra — _landing 22-09_
- **E-03** · El estudio entrega **dirección de mensaje y referencia de armado**; la ejecución final de las piezas de Meta la hace el equipo de diseño de Petra — _propuesta 10-09_

## 6. Lo que se aprueba a la primera

- **A-01** · (dato de la cuenta, no aprobación) La pieza que mejor rinde es la **única con foto real de un servicio** (ataúd de mimbre con flores): A5 vertical, CTR 4,68 %, 180 conversaciones, $2.031 por conversación — _Meta, 90 días al 10-09-2026_
- _Sin aprobaciones del cliente registradas todavía._

## 7. Lo que se rechaza

- **X-01** · Versión larga de la landing (proceso paso a paso, cuota mortuoria como sección, «Nuestra funeraria», preguntas frecuentes): se cortó a «hace una sola cosa, cotizar» — _Valeria, 22-09_
- **X-02** · Frases interpretadas que el sitio no dice: «precios claros», «sin costo ni compromiso», «un director funerario contigo», «música en vivo» — _eliminadas de la landing, 22-09_
- **X-03** · Anuncios que preguntan y no responden («¿Cuánto cuesta un funeral en Petra?» sin decirlo) y cierran en «Conversemos»: traen conversaciones que piden catálogo — _diagnóstico, propuesta 10-09_
- **X-04** · Gráfica peleada con el copy (A7: la imagen pregunta el precio y el texto habla de planificar en vida) — _propuesta 10-09_

## 8. Preguntas abiertas

- **¿Quién aprueba del lado de Petra y por dónde llega el feedback?** (Serena / Valeria).
- **¿Se aprobó la propuesta de mensajes de septiembre?** ¿Qué hizo el equipo de diseño de Petra con ella? (Serena).
- **Precios contradictorios en el sitio:** planes 52–200 UF vs preguntas frecuentes 65–195 UF. La landing usa el de planes; Petra debería corregir el otro (Serena → Petra).
- **Precio de la planificación anticipada:** no está en el sitio; la prensa habla de 11 UF. Confirmar antes de ponerlo en una pieza.
- **¿Pueden prometer respuesta en 30 minutos, 24/7?** Si sí, por escrito: es la primera variante que vale probar.
- **¿Tienen reseñas de Google?** No hay testimonios publicados y no se inventan.
- **Regla de decisión del test A/B** antes de partir: con ~270 clics/mes, ver que B duplica exige ~800 clics por variante (~6 meses). ¿6 semanas y regla direccional, o sumar `PETRA-Search-Prevision`? (Serena).
- **Aviso al equipo:** `SLACK_WEBHOOK` del CRM está vacío; el correo de CF7 es el único aviso. ¿La versión desplegada lo tiene?
- **Instalación pendiente:** formulario CF7 duplicado del id 6, página `/cotizar-funeral/` con noindex, una prueba real (correo + CRM + evento GTM `GTM-5QSHBSC5`).
- **Licencia de las fuentes** si algo se publica fuera de petrafuneraria.com.
- **Rotar la clave del usuario «editor» del WordPress**, que quedó escrita en Slack y en el chat.
- ¿«Nosotros» o «nosotras»? La propuesta de Meta dice «Nosotros coordinamos todo»; el sitio habla en femenino. Confirmar la voz antes de publicar.
- ¿Hace falta abrir `clients/petra/CLAUDE.md` y `marca.json` con `/marca-nueva`, o el estudio seguirá sólo en landing y dirección de mensaje?

## 9. Registro de cosechas

### 2026-09-26 — Claude nocturno (nube) · revisión de rutina, sin sesiones nuevas
- sin aprendizajes nuevos: `clients/petra/BITACORA.md` (creado en `66b38a1`, con la entrada del 22-09 sobre la landing de cotización) ya está reflejado en la siembra inicial de abajo — R-08 a R-12, y las preguntas de §8 sobre precios contradictorios, el `SLACK_WEBHOOK` vacío y rotar la clave del WordPress. `41b800b` es la misma siembra. El resto de `66b38a1` (G.CL, feed Copywriters, Santa Gota) no es de esta marca.

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-12** · sembradas desde `clients/petra/BITACORA.md`, `landing-cotizacion/README.md` y `FUENTES.md` (22-09) y la propuesta de mensajes de Meta (`propuesta-sep2026.html` y `armar-propuesta-sep2026.py`, 10-09).
- nuevo **X-01…X-04** · recortes internos de la landing y el diagnóstico de los anuncios activos; ninguno viene de feedback del cliente.
- sin aprobaciones del cliente: la cuenta todavía no tiene manual ni ficha de marca en el estudio, por eso §8 va cargada.
- abierto · contradicción de precios en el sitio (52–200 vs 65–195 UF) y voz «nosotros/nosotras».
