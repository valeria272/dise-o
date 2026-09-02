# Más Center — Landing de captación de terrenos

Landing para que dueños de terrenos postulen su propiedad a Más Center (Grupo IFB).

- **En vivo (pública):** https://mascenter-terrenos.vercel.app
- **Vista previa para aprobar:** https://claude.ai/code/artifact/958bf9c0-ea7c-4a45-b001-453e336e9180
- **Código:** `out/mascenter-terrenos/index.html` — una sola página, CSS y JS embebidos
- **Material fuente:** `raw/mascenter-terrenos/`

## Por qué NO se parece a las landings de cada strip center

La primera versión salió calcada de la landing de Algarrobal y estaba mal: **son dos
encargos distintos**. Una landing de proyecto le vende un local a un arrendatario; ésta
le pide el terreno a un dueño, que es una decisión patrimonial. El público es otro y el
tono también.

| | Landing de proyecto (Algarrobal) | Esta página |
|---|---|---|
| Fondo | claro | **grafito `#131417`** de punta a punta |
| Hero | foto a sangre con cuña roja en diagonal | declaración + panel contenido, sin cuña |
| Estructura | tarjetas redondeadas | **filetes de 1 px**, rejilla asimétrica rótulo + contenido |
| Botones | píldoras | rectos, radio 2 px |
| Cartera | carrusel | **registro** de 12 comunas; la foto sigue a la fila |
| Cifras | tarjeta de vidrio | franja tabular en el primer golpe de vista |
| Rojo | campo de color | acento quirúrgico |

El rojo, el negro, el gris y Poppins siguen siendo los del manual: **cambia la sintaxis,
no el vocabulario.**

## De dónde salió cada decisión

| Capa | Fuente |
|---|---|
| Paleta | **Manual de marca Grupo IFB 2023**, p33–34: `#E52521` · `#65140F` · `#DADADA` · negro |
| Tipografía | **Poppins**, corporativa de Más Center (manual p26). También la usa mascenter.cl |
| Textos | El brief del cliente, literal |
| Módulo «paso a paso» | El print de Arcos Dorados, numerado 01–04 porque sí es una secuencia real |
| Fotos de centros | Bajadas de **mascenter.cl** (21 disponibles, se usaron 12) |
| **Imágenes de terrenos** | **Generadas con Magnific/Mystic** — no existían fotos de paños vacíos |
| Aérea del proyecto | Render de Algarrobal, ya aprobado por el cliente |

Los iconos son **rellenos**, como exige el manual (p37).

## El comparador es la tesis de la página

Arrastrando el control se pasa de un paño vacío a un strip center en operación. Es el
argumento completo del encargo en un solo gesto: *tú aportas la ubicación, nosotros el
resto*. Funciona con mouse, con el dedo y con las flechas del teclado.

## ⚠️ Sobre las imágenes de terrenos

**Las 3 imágenes de terrenos son generadas con IA**, porque el cliente no tiene fotos de
paños vacíos y era el material que faltaba. Van rotuladas **«imagen referencial»** en la
propia página (bajo el hero, bajo el comparador y bajo la tira de ejemplos) para que
nadie las confunda con una propiedad real de Más Center. Si el cliente prefiere fotos
reales de terrenos que estén evaluando, se reemplazan sin tocar el diseño:
`assets/img/terreno-hero.jpg`, `terreno-esquina.jpg`, `terreno-avenida.jpg`.

Los prompts quedaron en `raw/mascenter-terrenos/ia/` junto a los PNG originales en 2K.

## Secciones

1. Hero — declaración, terreno y franja de credenciales
2. La oportunidad
3. Qué buscamos — 5 criterios + **tira de 2 ejemplos de terreno**
4. **De terreno a proyecto** — comparador arrastrable
5. La cartera — registro de 12 centros en operación
6. Cómo evaluamos — las 7 variables
7. Paso a paso — 01 a 04
8. Postulación — única sección en papel, para que el formulario respire
9. Pie

## ⚠️ Decisiones que necesitan al cliente

1. **La superficie mínima dice «XX m²».** Así venía en el brief. Marcada con comentario
   HTML en la tarjeta «Superficie» — es un solo lugar que cambiar.
2. **El correo es `contacto@mascenter.cl`**, tomado de su sitio. Si la captación de
   terrenos tiene buzón propio (`terrenos@`, `desarrollo@`), hay que cambiarlo.
3. **Los 4 pasos son propuesta de la agencia.** Falta que confirmen plazos reales y
   **cómo se llama el área que evalúa** — quedó «equipo de desarrollo».
4. **El formulario valida pero no envía correo.** Falta backend o Contact Form 7.
5. **Dominio.** Sugerencia: `terrenos.mascenter.cl` con CNAME a Vercel. Hoy está en
   `mascenter-terrenos.vercel.app`.

## Verificado en producción

- Sin peticiones con error, sin errores de consola, sin imágenes rotas
- Sin scroll horizontal en 1440 / 768 / 390 px
- Poppins auto-hospedada carga (`document.fonts.check` = true)
- Comparador, registro de centros y validación del formulario funcionando
- `prefers-reduced-motion` respetado
- Español de Chile con tuteo, sin voseo

## Volver a desplegar

```bash
cd out/mascenter-terrenos
npx vercel deploy --prod --yes          # cuenta valeria-1724, proyecto mascenter-terrenos
python3 -m http.server 8899             # para verlo local
```

`preview-artifact.html` (2,5 MB, assets en base64) **no se versiona**: se regenera desde
`index.html` cuando haga falta.
