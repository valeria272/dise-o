# PETRA — Landing de cotización (variante B del test A/B)

Página para captar **solicitudes de cotización de servicios funerarios** desde Google
Search. Se monta dentro de petrafuneraria.com con el tema actual: mismas tipografías
(Mandrel Cond + PP Neue Montreal), el mismo gris carbón `#3f3f3f`, botones de filete y
el óvalo de flores de la portada.

**Versión corta (22-09-2026), por instrucción de Valeria:** la página hace una sola cosa,
cotizar. Quedaron el formulario, los dos planes con su rango de precio y el llamado final.
Se sacaron el proceso paso a paso, la cuota mortuoria como sección, «Nuestra funeraria» y
las preguntas frecuentes. **Todo el texto informativo es literal del sitio de Petra** —
la trazabilidad frase por frase está en `FUENTES.md`.

| Archivo | Para qué |
|---|---|
| `landing-b.src.html` | La fuente legible. Se edita esta |
| `FUENTES.md` | De dónde salió cada frase, con la cita del sitio. Sirve para mostrárselo al cliente |
| `build.py` | Genera `PEGAR-EN-WORDPRESS.html`. Con `--preview <carpeta>` arma además una vista previa sobre el tema real |
| `PEGAR-EN-WORDPRESS.html` | **Lo que se pega en WordPress.** Una sola línea a propósito |
| `cf7-formulario-landing.txt` | El formulario de Contact Form 7 que recibe los datos y manda el correo |

---

## Por qué está armada así

Viene del diagnóstico del 10-08-2026 (`petra-calidad-leads-catalogo`):

1. **Se pide una cotización, no un catálogo.** El 73 % de los leads quedaba en «Catálogo»
   porque la oferta era gratis y no comprometía a nada. La acción de esta página es
   «Recibir cotización», con los precios a la vista (desde 52 UF), así que el que llena
   el formulario ya sabe en qué rango está.
2. **El teléfono es obligatorio y el mensaje, opcional.** En el sitio era al revés (3 de
   49 leads traían teléfono). Acá el correo también es opcional.
3. **El primer paso es un clic, no un campo.** «¿Cómo te podemos ayudar?» con tres
   opciones: servicio ahora / cotizar un servicio / anticipar. Clasifica el lead por
   arquetipo (lo que la columna del CRM tenía vacía en 46 de 49) y baja la fricción.
4. **Quien elige «servicio ahora» ve el teléfono antes que los campos.** Un funeral
   inmediato no debería esperar a que alguien lea un correo.
5. **Sin menú.** Se esconden el menú y el carrito para no abrir salidas; quedan el logo
   y el botón de WhatsApp del tema. En móvil hay una barra fija Llamar · WhatsApp · Cotizar.
6. **Nada que distraiga.** La página no cuenta la historia de Petra ni explica el proceso:
   eso ya está en el sitio. Acá sólo se cotiza, y el texto informativo es literal del sitio
   (ver `FUENTES.md`), para que nadie pueda decir que es relleno genérico.

## Qué pasa cuando alguien envía el formulario

1. La landing le manda los datos a **Contact Form 7** por su API → sale **el mismo tipo
   de correo que hoy** al equipo de Petra. Esto es lo que avisa: el endpoint del CRM
   tiene `SLACK_WEBHOOK` vacío en la versión local del `.gs`, así que por sí solo no
   avisa a nadie.
2. Si el correo salió, empuja al `dataLayer` el **mismo evento que ya usa GTM**:
   `form_submit_contacto` (o `form_submit_prevision` si eligió anticipar). Eso dispara
   las conversiones de Google Ads y el Lead del píxel **sin tocar GTM**. Además manda
   `generate_lead` a GA4 con el parámetro `lp_variante`.
3. Escribe el lead en el **CRM** (mismo endpoint de Apps Script que usa el sitio), con
   `landing_page = /cotizar-funeral/` y el mensaje prefijado `[B-landing-cotizar]`.
   El teléfono va sólo con dígitos, para esquivar el `#ERROR!` del «+» en el Sheet.
4. Si Contact Form 7 falla, el lead **igual se escribe en el CRM** (marcado `CF7: …`) y
   la persona ve el teléfono y WhatsApp para contactar directo. No se pierde.

Los clics en teléfono y WhatsApp los mide el snippet global del sitio, que ya corre en
todas las páginas: la landing no los duplica.

**Anti-spam:** campo trampa oculto + un envío hecho en menos de 2,5 s se descarta en
silencio. Si llega basura, el paso siguiente es Turnstile (viene de fábrica en CF7 6.1).

---

## Instalación (necesita un admin de WordPress)

1. **Formulario:** crea el formulario de CF7 siguiendo `cf7-formulario-landing.txt` y
   anota su **ID**.
2. **Página:** Páginas → Añadir nueva. Título «Cotiza tu servicio funerario», enlace
   permanente **`/cotizar-funeral/`**. Plantilla por defecto. Publícala vacía para que
   tenga **ID** (sale en la URL del editor: `post=XXX`).
3. **Pegar:** abre `PEGAR-EN-WORDPRESS.html`, reemplaza en la primera etiqueta
   `data-cf7-id="0"` por el ID del formulario y `data-cf7-post="0"` por el ID de la
   página, y pega TODO en:
   - editor de bloques → bloque **«HTML personalizado»**, o
   - editor clásico → pestaña **«Código»/«Texto»** (nunca «Visual»).
   No lo reformatees: una sola línea es lo que evita que `wpautop` meta `<p>` dentro
   del CSS (así se descuadró la v2 de /gracias/).
4. **Yoast:** en la página, «¿Permitir que los motores de búsqueda muestren esta página?»
   → **No**. Es una página de pauta: el tráfico orgánico ensuciaría el test.
5. **LiteSpeed:** purga la caché de la página después de pegar o cambiar algo.
6. **Prueba real (una sola):** envía un formulario con el nombre «PRUEBA landing B».
   Revisa que (a) llegó el correo, (b) apareció la fila en el CRM y (c) en GTM →
   Vista previa se ve el evento `form_submit_contacto`. Después marca la fila como
   «PRUEBA interna» en la columna L del CRM.

> Con `data-cf7-id="0"`, fuera de petrafuneraria.com o con `?plp_demo=1` en la URL, la
> landing corre en **modo demostración**: muestra el agradecimiento pero no manda
> correo ni escribe en el CRM. Sirve para revisar el diseño sin generar leads falsos.

**Vista previa local** (sin tocar el sitio):

```bash
/Users/Vale/copylab-venv/bin/python3 build.py --preview /tmp/petra-prev
# copia las fuentes del tema a /tmp/petra-prev/fonts/ (el servidor de Petra no manda
# CORS, así que no cargan desde otro dominio) y sirve la carpeta:
cd /tmp/petra-prev && python3 -m http.server 8931
```

---

## El test A/B

**Lo lleva Serena** (las campañas de Petra no se tocan desde otro agente).

- **A (control):** la URL final que usan hoy los anuncios de `PETRA-Search-Inmediata`.
- **B:** `https://petrafuneraria.com/cotizar-funeral/`.
- **Cómo:** Google Ads → Experimentos → experimento personalizado sobre
  `PETRA-Search-Inmediata`, **50/50 por búsqueda**, cambiando sólo la URL final en el
  borrador. Mismos anuncios, puja y presupuesto. No usar un redirect por JS: rompe el
  `gclid` y Google lo penaliza.
- **Métrica principal:** leads por clic sumando las tres conversiones (formulario +
  WhatsApp + llamada). Sólo formularios castigaría a B por empujar el teléfono en
  servicios inmediatos.
- **Métrica de calidad:** en el CRM, % de leads que llegan a «cotización enviada» o más,
  cruzando por `landing_page`. Es la que paga el bono del 2 %.

⚠️ **El volumen es chico y hay que decirlo antes de empezar.** Con ~270 clics al mes en
Search y ~3 % de conversión, detectar que B **duplica** la tasa (3 % → 6 %) con 80 % de
potencia exige unos **800 clics por variante**: cerca de **6 meses** a este ritmo. Un
test de 4 semanas no va a dar significancia estadística. Opciones honestas:

1. Correrlo mínimo **6 semanas** y decidir por una regla práctica acordada antes (por
   ejemplo: B se queda si trae más leads por clic **y** al menos igual % de cotizaciones
   en el CRM), sabiendo que es una decisión direccional, no una prueba.
2. Mandar también la campaña `PETRA-Search-Prevision` a B (llega con `form_submit_prevision`)
   para sumar tráfico.

---

## Pendientes y cosas que revisar con Petra

- **Precios que no calzan en su propio sitio:** la página de planes dice **52–200 UF** y
  la de preguntas frecuentes dice **65–195 UF**. La landing usa la de planes (es donde se
  compra). Hay que corregir la de preguntas frecuentes.
- **Tiempo de respuesta:** «te llamamos en menos de 30 minutos» es de lo que más convierte
  en esta categoría, pero no lo puse porque Petra no lo promete en ningún lado. Si lo
  pueden cumplir 24/7, es la primera variante que vale la pena probar.
- **La única promesa que la landing hace y el sitio no dice:** «te contactamos por teléfono
  o WhatsApp» después de enviar el formulario. Es inevitable en un formulario de cotización,
  pero la cumple el equipo de Petra, así que conviene confirmarla con ellos.
- **Testimonios:** no hay ninguno publicado y no se inventaron. Si tienen reseñas de
  Google, van entre los planes y el proceso.
- **Aviso por Slack del CRM:** el `.gs` local tiene `SLACK_WEBHOOK` vacío. Confirmar si
  la versión desplegada lo tiene; si no, el correo de CF7 es el único aviso.
- **GTM publicado:** las conversiones de Google Ads viven en tags del contenedor
  `GTM-5QSHBSC5` creados el 25-06 por API; verificar en la prueba real que el evento sí
  dispara la conversión.
