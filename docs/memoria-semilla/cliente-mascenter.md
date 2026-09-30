---
name: cliente-mascenter
description: "MASCENTER — cerebro del cliente: 69 reglas firmes, última cosecha 2026-09-30. Generado desde clients/mascenter/APRENDIZAJES.md; leerlo antes de diseñar para mascenter"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/mascenter/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para mascenter: no se traspasa a otra marca.

Criterio: **Diego Aguilar (su criterio manda en las piezas; decisión final de marca: Valeria Traverso)** · Aprueba: **Sebastián Córdova (paid) · Francesca Pavissich (landings y presentación comercial)**

## Reglas más confirmadas
- **R-10** · Los rótulos de locatarios reales se revisan a zoom 1:1; si la IA los reescribe, se parcha el letrero real con `parche_letrero.py` y no se insiste con el prompt — _Nano Banana Pro reescribió «cencosud» dos veces, 04-09-2026; Seedream escribió «Litle Caesars» y «Little Cagars» en la portada del 08-10 (Chamisero II) y se parchó con el letrero de la foto real, 28-09-2026_ · ✔×5
- **R-33** · Carrusel de locatarios: foto real a sangre, banda de color con borde curvo, logo del locatario en círculo blanco sobre la banda, nombre Bold 45 + descripción Book 42 + 📍 «Más Center + lugar» Medium 35, flecha en círculo. La banda es roja por defecto; verde `#299A80` servicios/súper, cian `#01B8C1` clases, mostaza `#CFAF30` mascotas, rosa `#D64E74` madre/San Valentín — _editables mar-2025 → sept-2026_ · ✔×5
- **R-38** · Imagen que se lea «Más Center»: gente comprando en los centros reales, con pin y dirección, sin banco de imágenes. La IA sirve para mejorar una foto real o generar centros de región; un render IA va rotulado «imagen referencial» — _grilla ene: «le falta imágenes más "Más Center"… alguien en una tienda, o con bolsas de compra»; jul: «Indicar de forma sutil que es una imagen referencial»; ago: «foto casual, auténtica, no de banco de imágenes»_ · ✔×5
- **R-01** · La pieza del mes es la del mes anterior con otro contenido: el esqueleto de paid no se rediseña, se rellena, y tiene que confundirse con `LinkAd Tráfico a Ig 1 - post.png` — _medido en 4 meses de piezas aprobadas; manual §2, 04-09-2026_ · ✔×4
- **R-37** · Toda cifra lleva su fuente en letra chica (Memoria 2025, DF, CBRE); en LinkedIn las cifras de mercado van en el copy del post, no en las láminas — _grilla feb: «agregar en parte inferior y más pequeño: Fuente: Diario Financiero»; brief LinkedIn sept_ · ✔×4
- **R-58** · Las entregas del orgánico van a la carpeta del mes de la grilla (octubre: «10. OCTUBRE» `1h7_dB1HxA2KBThQhUuUinHG24DP9wHwK`) con la nomenclatura de Diego `c-dd-mm-n.png` / `p-dd-mm.png`. El token del estudio (`drive.file`) no LISTA esa carpeta pero SÍ crea archivos en ella; cada ronda se reemplaza en sitio (mismo fileId, md5 verificado) — _Diego: «todo lo generado lo dejas acá», 28-09-2026_ · ✔×4
- **R-03** · (⚠️ precisada 2026-09-25: abr–ago el paid usó `#E52521`; `#DC1914` rige desde septiembre y en todo el orgánico) Rojos de paid: pastilla y bajada `#DC1914`, burbuja CTA `#D80000`, ningún otro en la columna de texto — _6 piezas de septiembre + agosto; `reglas.yaml › rojo-de-sistema`, 04-09-2026_ · ✔×3
- **R-30** · **La tipografía de Más Center es Gotham**: Gotham Black para titular en pastilla y display de impacto; Gotham Rounded Bold (nombre de locatario, titular de arriendo), Medium (bajada, CTA, dirección), Book (descripción) y Light (pastillas de beneficios). La fuente se lee en el `.ai` (PyMuPDF `get_text('dict')`) antes de medir glifos — _editables de Diego abr–sept 2026 + `.aep` de jun–ago, leído 25-09-2026; Diego pidió usar su carpeta como referencia; 28-09 Diego: «migra el sistema a gotham» → sistema migrado y calibrado contra el `.ai`_ · ✔×3
- **R-34** · Logo de Más Center en toda pieza, también en LinkedIn aunque la línea sea IFB — _cliente, grilla feb: «cambie el enfoque a Más Center y no IFB. Cambiemos el logo por el de Más Center»; mar: «poner en la imagen el logo de Más Center»_ · ✔×3
- **R-43** · Localito: comunidad, concursos, efemérides, paid de tráfico y avisos; nunca arriendo ni LinkedIn. Desde agosto existe el corpóreo real y en sept–oct protagoniza reels de humor — _grillas ago–oct 2026_ · ✔×3 (refuerza R-06)
- **R-55** · ⭐ Antes de diseñar una pieza de un tema que ya existió (Mercado Campesino, Día del Niño, efemérides, locatarios), buscar la pieza anterior en los `.ai` de Diego (`PyMuPDF get_text()` por mesa, con la palabra clave del tema) y usarla de PLANTILLA: se mide con `scripts/mascenter-geo-plantilla.py` y se reutilizan sus vectores (onda, lockups) renderizados del propio `.ai`. La REF de la grilla da la idea; la plantilla viva manda el estilo — _Diego, 26-10: «el post del 26-10 sigue esta plantilla» (Día del Campesino, JULIO IFB.ai mesa 22) tras una v1 de diseño propio; 01-10: «ten en cuenta el enlace REF para la portada pero mantiene el estilo de la plantilla», 28-09-2026_ · ✔×3
- **R-02** · ⚠️ revisada 2026-09-25 → ver **R-30**. ~~En paid la tipografía es Montserrat, aunque el manual 2023 diga Poppins; la letra se identifica por glifos sobre la pieza aprobada — _Valeria lo vio a ojo y rechazó la ronda 1 («esa tipografía tampoco es»); medido glifo a glifo, 04/05-09-2026_ · ✔×2~~ La medición sólo comparó contra Poppins.
- **R-04** · Medida exacta 1080×1080 / 1080×1920, nunca 1081 como entrega el cliente — _medición 02-09-2026; `marca.json › reglas_duras`_ · ✔×2
- **R-06** · Localito sólo en la campaña de comunidad; nunca en la de arriendo — _manual §1, 04-09-2026_ · ✔×2
- **R-08** · Textos verbatim del brief; la conversión a versales la hace el sistema — _manual §6; QA del 24-09-2026 (tres pantallas pasan 7 palabras y no se tocaron)_ · ✔×2
- **R-14** · Reels con la pista de julio/agosto del cliente (~81 BPM, `pista-mascenter.m4a`); sin voz, el texto cuenta la historia — _Valeria, ronda 2 («sin música»), 05-09-2026_ · ✔×2
- **R-20** · Fotos «fachada o pasillo con gente», nunca stock genérico; los banners del home de `mascenter.cl` no sirven (stock europeo y cafetería) — _brief de octubre; landing terrenos, 02-09-2026_ · ✔×2
- **R-21** · Un cambio de cara al cliente se da por hecho sólo cuando `curl` a la URL en vivo lo muestra; commitear no es publicar — _Francesca vio el correo viejo un día entero, landing terrenos, 09-09-2026_ · ✔×2
- **R-22** · Un formulario publicado no promete lo que no hace: ni «Recibimos tu postulación» sin envío ni una subida de archivos que `mailto:` no transporta — _Francesca, rondas 5 y 6 de la landing de terrenos, 09/10-09-2026_ · ✔×2
- **R-28** · Una ronda se re-sube en sitio (mismo fileId y enlace, md5 verificado) — _paid octubre, 05-09 y 24-09-2026_ · ✔×2

## Lo que ya costó rondas
- **X-01** · Poppins en paid por seguir el manual sin medir — _paid octubre ronda 1, 04-09-2026, 1 ronda_
- **X-02** · Reels sin música — _ronda 1, 04-09-2026_
- **X-03** · Barrido y tiempos inventados; y también la copia literal del reel de agosto (tipeo letra a letra 0,32 s + golpe de rojo 0,30 s) — _rondas 1 y 2, 04/05-09-2026: costaron 2 rondas_
- **X-04** · Clip de Kling con letras finas que vibran — _Fashion's Park Coyhaique, ronda 4, 05-09-2026_
- **X-05** · Última línea del titular del reel dentro de la franja que tapa Reels (y=1606, x≈1020) — _reels v4 → v5, 24-09-2026_
- **X-06** · Rediseño «institucional» completo de la landing (grafito, filetes, comparador arrastrable) sin mostrar antes una sección de muestra: «no te quedó muy bien» — _landing de terrenos, 02-09-2026, 1 ronda; se volvió a la v1_
- **X-07** · Render de un proyecto identificable como hero de marca — _landing de terrenos, 02-09-2026_
- **X-08** · Correo genérico `contacto@mascenter.cl` en la captación de terrenos — _Francesca, 09-09-2026_
- **X-09** · Formulario que dice «Recibimos tu postulación» sin enviar nada — _landing de terrenos, 09-09-2026_
- **X-11** · Montserrat en paid: salió de medir glifos sin tener a Gotham entre las candidatas; el editable decía Gotham desde el principio — _hallado 25-09-2026; afecta el paid de octubre ya entregado_
- **X-12** · Efemérides «de reciclaje» sin respaldo: «Más Center no tiene puntos de reciclaje» — _Scarlette, grilla may_
- **X-13** · Stories de interacción sin gancho: «Malísimo, esto no va a hacer que nadie interactúe» — _Scarlette, grilla may_
- **X-14** · Localito recortado a mano de un PNG con fondo blanco (restos blancos) o la pose del paid con teléfono en una pieza orgánica — _carrusel 04-10 ronda 1, 28-09-2026, 1 ronda_
- **X-15** · Fotos donde la banda, el círculo del logo o la caja del titular cortan al sujeto (orejas, patas, cara) — _Diego, 04-10 ronda 1: «se corta en algunos casos», 28-09-2026, 1 ronda_
- **X-16** · Logo de Más Center sobre el color de la banda del tema (mostaza) en vez de rojo — _Diego, 04-10 ronda 1, 28-09-2026_
- **X-17** · Localito pegado sobre la foto como recorte que «vuela», sin piso ni sombra — _Diego, portada 08-10, 28-09-2026, 1 ronda_
- **X-18** · Rótulos de estructura de la grilla en la gráfica: nombres de local salidos de «Slide N – Local» y etiquetas «✓ Decoración / Dulces…» — _Diego, 04-10 y 08-10, 28-09-2026, 1 ronda para dos carruseles_
- **X-19** · Post de un tema recurrente diseñado desde cero (26-10 v1: retrato con titular rojo detrás de la vendedora y banda verde) existiendo la pieza de julio del mismo tema — _Diego: «el post del 26-10 sigue esta plantilla», 28-09-2026, 1 ronda_
- **X-20** · Una imagen a la altura de los ojos de la fachada con locales rotulados (Seedream + Wan): las letras de las tiendas se deforman — _Diego, C1 del reel Linderos, 29-09-2026, 1 ronda_
- **X-21** · Inventar con IA el terreno del proyecto (paño en obra junto a la Ruta 5) sin su ubicación real: Die
