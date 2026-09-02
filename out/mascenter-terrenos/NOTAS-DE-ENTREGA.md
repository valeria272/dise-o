# Más Center — Landing de captación de terrenos

Landing para que dueños de terrenos postulen su propiedad a Más Center (Grupo IFB).
Hermana de la landing de Algarrobal: mismo esqueleto, mismos movimientos, mismo sistema.

- **En vivo (pública):** https://mascenter-terrenos.vercel.app
- **Vista previa para aprobar:** https://claude.ai/code/artifact/958bf9c0-ea7c-4a45-b001-453e336e9180
- **Código:** `out/mascenter-terrenos/index.html` (una sola página, CSS y JS embebidos)
- **Material fuente:** `raw/mascenter-terrenos/`

## De dónde salió cada decisión

| Capa | Fuente |
|---|---|
| Paleta | **Manual de marca Grupo IFB 2023**, p33–34: Vivid red `#E52521`, Very dark red `#65140F`, Very light gray `#DADADA`, negro |
| Tipografía | **Poppins**, corporativa de Más Center según el manual p26. Es la misma que usa mascenter.cl y la landing de Algarrobal |
| Estructura y textos | El brief que mandó el cliente, literal |
| Módulo «paso a paso» | El print de Arcos Dorados que mandó el cliente, traducido al rojo de la marca |
| Fotos de centros | Bajadas de **mascenter.cl** (21 disponibles, se usaron 12) |
| **Banner del hero** | **Terreno generado con IA** (Magnific/Mystic) — rotulado «Imagen referencial» |
| Foto de «La oportunidad» | Render aéreo de Algarrobal, ya aprobado por el cliente |
| Movimientos | Calcados de `pirquenogalesponiente.mascenter.cl`, igual que en Algarrobal |

El chevron se usa como **borde entre el campo de color y la fotografía**, no como flecha
encima — la regla del sistema. Los iconos son **rellenos**, como exige el manual (p37).

## Secciones

1. Hero — «Identificamos ubicaciones. Desarrollamos oportunidades.»
2. La oportunidad — «¿Tienes un terreno con potencial comercial?»
3. Qué buscamos — 5 criterios
4. El valor de Más Center — cifras con contador (+69.000 m², +30, +400)
5. Centros en operación — carrusel de 12 fotos reales
6. Más que un terreno — las 7 variables de evaluación
7. **Paso a paso** — el módulo que pidió el cliente, 2×2 con checks rojos
8. Conversemos — formulario de postulación
9. Pie con la firma «Encontramos ubicaciones · Creamos espacios · Acercamos comercios y servicios»

## ⚠️ Decisiones que necesitan al cliente

1. **La superficie mínima dice «XX m²».** Así venía en el brief. Está marcada con un
   comentario HTML en la tarjeta «Superficie» — es un solo lugar que cambiar.
2. **El correo de contacto es `contacto@mascenter.cl`**, tomado de su sitio. Si la
   captación de terrenos tiene un buzón propio (tipo `terrenos@` o `desarrollo@`),
   hay que cambiarlo. No se puso teléfono porque no tenemos uno confirmado para esto.
3. **Los 4 pasos del proceso son propuesta de la agencia**, adaptados de la referencia
   de Arcos Dorados. Falta que Más Center confirme los plazos reales y **cómo se llama
   el área que evalúa** — quedó como «equipo de desarrollo» (en McDonald's es «Real Estate»).
4. **El formulario valida pero no envía correo.** Falta enchufarlo al backend o a
   Contact Form 7. Campos: nombre, email, teléfono, región, comuna, superficie,
   dirección/rol, mensaje.
5. **Dominio.** Hoy vive en `mascenter-terrenos.vercel.app`. Sugerencia:
   `terrenos.mascenter.cl` con CNAME a Vercel, o como página dentro del WordPress actual.

## Verificado

- Sin scroll horizontal en 1440 / 768 / 390 px · sin errores de consola
- Las 17 imágenes cargan · carrusel y validación del formulario funcionando
- `prefers-reduced-motion` respetado — apaga apariciones y parallax
- Español de Chile con tuteo, sin voseo

## Reconstruir la vista previa

```bash
cd out/mascenter-terrenos
python3 -m http.server 8899      # y abrir http://localhost:8899
```

El `preview-artifact.html` (2,1 MB, con los assets incrustados en base64) **no se versiona**:
se regenera desde `index.html` cuando haga falta.

## El banner del hero: por qué es un terreno y no un proyecto

Al principio el hero llevaba el render aéreo de Algarrobal. Tenía dos problemas:
es un **render** —y la página se apoya en que los +30 centros ya están operando—, y
es un **proyecto identificable**, no una imagen genérica de la marca.

Se cambió por un **terreno vacío en la esquina de una avenida**: le habla directo a
quien tiene un paño y ve ahí su propia situación. Va rotulado **«Imagen referencial»**
abajo a la derecha porque es generada con IA y no corresponde a una propiedad real de
Más Center.

> 💡 **Lo ideal sigue siendo una foto real con dron** de un centro en operación: resuelve
> las dos cosas de una (es real y es de ellos). Vale la pena pedírsela a Más Center.

## Sobre el rediseño que se descartó

El 02-09-2026 se probó una segunda versión con otro enfoque —expediente institucional
sobre fondo grafito, filetes en vez de tarjetas, comparador arrastrable terreno→proyecto
y un registro de centros en lugar del carrusel— y **el cliente interno la descartó**:
se vuelve a esta versión. Queda en el historial de git (commit `7a507e4`) por si alguna
vez se quiere rescatar alguna pieza suelta.

De ese intento sobrevivieron **3 imágenes de terrenos generadas con IA**. Una de ellas
—`terreno-hero.jpg`— **terminó siendo el banner de esta versión**. Las otras dos
(`terreno-esquina`, `terreno-avenida`) siguen disponibles en `raw/mascenter-terrenos/ia/`.
Ver `PROMPTS-IMAGENES.md`.

## Volver a desplegar

```bash
cd out/mascenter-terrenos
npx vercel deploy --prod --yes     # cuenta valeria-1724, proyecto mascenter-terrenos
python3 -m http.server 8899        # para verlo local
```

---

## Ronda 2 — 02-09-2026 (feedback del KAM)

| # | Comentario | Qué se hizo |
|---|---|---|
| 1 | Los botones redirigen bien | Nada. Verificado. |
| 2 | El logo se siente chico frente a «Postula tu terreno» | Cabecera **46 → 64 px** (50 px al hacer scroll, antes 36). Pie **52 → 66 px**. |
| 3 | El rojo oscuro puede no convencer a Fran | **No se tocó**, tal como se pidió. Queda a la espera de su revisión para definir el Pantone. |
| 4 | Faltan centros: son 23 activos | Carrusel rehecho con **los 23**. Fotos bajadas una a una del sitio oficial (`mascenter.cl/<centro>/`, banners 1920×810), verificadas con hoja de contacto: las 23 son distintas y reales. Recortadas a 3:2 · 1200×800. |
| 5 | Usar la nomenclatura oficial, no la comuna | Rótulo ahora es **nombre oficial** (Más Center Larraín) + **comuna** debajo (La Reina). |
| 6 | Sumar el LinkedIn de Grupo IFB | Agregado en el pie. URL sacada del sitio de IFB: `linkedin.com/company/grupoifb/`. |

### Cambio de proporción de las tarjetas
Las fotos oficiales son panorámicas (2,37:1) y la tarjeta era 4:3. Meterlas ahí
recortaba casi la mitad del ancho, justo lo que define a un strip center.
La tarjeta pasó a **3:2**.

### ⚠️ Tres cosas que quedan pendientes de confirmación

1. **«Más de XX m² de terreno»** sigue publicado en la sección «¿Qué buscamos?».
   El `XX` viene del brief original y nunca llegó el dato. Es la primera condición
   que lee un dueño de terreno — conviene cerrarlo antes de que lo vea Fran.
2. ~~La cifra pasó de «+30» a «23»~~ **RESUELTO (02-09):** el KPI se queda en
   **«+30»**, porque es como la marca lo comunica en todos lados. Se revirtió en
   los tres lugares (sello del hero, contador de trayectoria y meta description).
   Para que no choque, la bajada del carrusel **ya no declara un número**: dice
   «Una cartera en operación de Copiapó a Osorno». Así conviven el KPI de marca
   (+30, que incluye proyectos en desarrollo) y las 23 fichas con foto real.
3. **«Las Flores» y «San Carlos»** son los dos de Las Condes. Se asignó
   `las-condes-san-carlos-de-apoquindo` → Las Flores y `san-carlos-de-apoquindo` →
   San Carlos. **Confirmar que las fotos no quedaron cruzadas.**

Typos de la tabla corregidos al escribir: «Cuidad Empresarial» → Ciudad Empresarial ·
«Sana Maria» → Santa María · «Peñalolen» → Peñalolén · «Los angeles» → Los Ángeles ·
«Con Con» → Concón.
