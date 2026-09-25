# Petra Funeraria — Landing de cotización (variante B del test A/B)

Hay dos formatos. **Usa uno solo**, según dónde vaya a vivir la página.

| Carpeta | Úsala si la página va… |
|---|---|
| `wordpress/` | **dentro de petrafuneraria.com** (recomendado): usa el header, el footer y el marcaje que el sitio ya tiene |
| `pagina-independiente/` | **en otro hosting** (Vercel, Netlify, Hostinger, un subdominio): trae su propio header, footer, fuentes, imágenes y marcaje |

Las dos envían al mismo lugar y quedan conectadas igual:

- **Correo al equipo de Petra**, vía Contact Form 7 del sitio. Hoy es el único aviso que recibe el equipo.
- **Fila en el CRM** (Google Sheet), con la columna `landing_page` para distinguir la variante B.
- **Conversiones de Google Ads y del píxel de Meta**, por los mismos eventos de Google Tag Manager que ya usa el sitio (`form_submit_contacto`, `form_submit_prevision`, `whatsapp_click`, `phone_click`).

---

## Paso obligatorio para los dos formatos: el formulario de Contact Form 7

Sin este paso, la página funciona en modo demostración y no envía nada.

1. En el WordPress de Petra: Contacto → Formularios de contacto → **Duplicar** el formulario
   de /contacto/ (id 6), para heredar el destinatario del correo.
2. Configúralo con lo que dice `wordpress/cf7-formulario-landing.txt`. Los valores de las opciones van
   **letra por letra**.
3. Anota el **ID** del formulario nuevo.

---

## Formato A — dentro de WordPress (`wordpress/`)

1. Crea la página «Cotiza tu servicio funerario», enlace `/cotizar-funeral/`, y anota su **ID**.
2. En `PEGAR-EN-WORDPRESS.html`, al comienzo del `<div id="plp" …>`, cambia
   `data-cf7-id="0"` por el ID del formulario y `data-cf7-post="0"` por el ID de la página.
3. Pega el archivo **completo y sin reformatear** en un bloque «HTML personalizado». En el
   editor clásico, usa la pestaña «Código», nunca «Visual». Va en una sola línea a propósito:
   WordPress mete `<p>` en los saltos de línea y rompe el CSS.
4. Yoast → que no aparezca en buscadores (noindex). LiteSpeed → purga la caché de la página.

## Formato B — otro hosting (`pagina-independiente/`)

1. Abre `index.html`, busca `data-cf7-id="0"` y cambia el `0` por el ID del formulario.
   `data-cf7-post` puede quedar en `0`.
2. Sube la carpeta **completa** (`index.html` + `fonts/` + `img/`) tal cual, con las rutas
   relativas intactas. Tiene que publicarse con **https**.
3. Ya trae `noindex`, Google Tag Manager `GTM-5QSHBSC5` y GA4 `G-ZBQ8EHP0XS`, que son los mismos del sitio.
   En local (`localhost` o doble clic en el archivo) el marcaje y los envíos se apagan solos,
   para no ensuciar las estadísticas ni mandar leads falsos.

**Qué cambia respecto de WordPress:**

- **La página envía «a ciegas».** El servidor de Petra no deja que otro dominio lea la respuesta del formulario. El envío llega igual y el correo sale igual, pero la página no puede confirmarlo. Por eso valida todo antes de enviar y deja siempre el lead en el CRM como respaldo.
- **Hay que agregar el dominio nuevo en Google Tag Manager.** Si el píxel o las conversiones filtran por dominio, se agrega en su configuración. Y en GA4 conviene sumarlo en «Configurar dominios» (medición entre dominios).
- **Hay que revisar la licencia de las fuentes.** PP Neue Montreal y Mandrel son fuentes de pago de Petra. Si la licencia web es sólo para petrafuneraria.com, este formato necesita ampliarla. El formato WordPress no tiene este problema.

---

## Antes de mandar tráfico

- **Una sola prueba real**, con el nombre «PRUEBA landing B». Revisa que:
  1. llegó el correo;
  2. apareció la fila en el CRM, y márcala como «PRUEBA interna» en la columna L;
  3. en la vista previa de Google Tag Manager se ve el evento `form_submit_contacto`.
- **El test A/B** se arma en Google Ads → Experimentos, sobre `PETRA-Search-Inmediata`,
  50/50, cambiando sólo la URL final. No uses redirecciones por JavaScript: se pierde el `gclid`.
- Para revisar el diseño sin enviar nada, agrega `?plp_demo=1` a la URL.
