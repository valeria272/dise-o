---
name: cliente-piso18
description: "PISO18 — cerebro del cliente: 69 reglas firmes, última cosecha 2026-10-03. Generado desde clients/piso18/APRENDIZAJES.md; leerlo antes de diseñar para piso18"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/piso18/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para piso18: no se traspasa a otra marca.

Criterio: **Elisabet Soto «Eli»**, con revisión de la jefa de diseño **Constanza Lizana** · Aprueba: **el cliente Hilton, por comentarios en la grilla (contenido: Carlos Figueroa y Scarlette Muñoz)**

## Reglas más confirmadas
- **R-31** · Una pieza corregida se reemplaza en Drive **conservando su enlace** — _S4 rondas 4, 5, 6 y 7 (16 al 22-09)_ · ✔×7 (28-09: rondas 2 y 3 de octubre) · 29-09: ronda 4: 8 archivos reemplazados · ✔×8 (29-09 rondas 5 y 6: 6 láminas, md5 verificado) · 01-10: G2 de Fechas 2027 (✔×9) · 02-10: rondas 8, 9 y 10, 19 archivos reemplazados con md5 verificado (✔×10)
- **R-33** · Lo nuevo de la grilla se detecta por diff de **conjunto de cadenas** contra la instantánea anterior: el comentario se prepende y no lo delatan ni la celda ni el `modifiedTime` — _confirmado el 16, 17 (×2), 22-09 y 28-09 (grilla oct: 8 comentarios nuevos del cliente en celdas que estaban vacías; 28-09 noche: la grilla reordenó 3 piezas entregadas)_ · ✔×7 · 29-09: grilla 29-09 12:21Z: 5 comentarios nuevos sobre piezas entregadas · 01-10: C13 con comentario nuevo arriba y el viejo tachado (✔×8)
- **R-32** · La revisión se publica como página de antes/después; nada interno va a la carpeta de entrega, que ve el cliente (`@hilton.com` con permiso de escritura) — _hallazgo 16-09; rondas 4–7 aprobadas así_ · ✔×6 (28-09: páginas r1 y r2 de octubre) · 29-09: páginas r4 y st1510 · 02-10: páginas r8 y r9 (✔×7)
- **R-01** · «bodas» no se escribe nunca: va matrimonio(s) o novios, aunque el brief o el hashtag lo traigan — _Eli, 15-09-2026; ratificada por el cliente en `FEED!I14` el 17-09 («no usemos la palabra BODA»)_ · ✔×4 (28-09: las 11 de octubre sin «boda») · 29-09: ronda 4 y ST 15-10 sin «boda»
- **R-17** · La caja de recorte de cada pieza queda escrita en el script que la produce — _S4, 16-09: dos recortes hubo que reconstruirlos por correlación_ · ✔×4 (28-09: `scripts/p18-oct-fotos.py`) · 29-09: cajas de fin160, deco112, deco143 en `p18-oct-fotos.py` · 01-10: cajas y tramos de video de la ronda 7 (✔×5) · 02-10: tramos nuevos del 30-10, caja del letrero nivelado y cajas de las capas de globos (✔×6)
- **R-11** · La interacción no se dibuja: se deja el aire y el sticker real lo pone el CM — _manual; marca.json `botones`_ · ✔×3 (28-09: ST 07 y 09-10) · 29-09: ST 15-10, hueco para el cuadro de respuestas
- **R-18** · Todo fondo oscuro plano lleva grano (`GranoFondo`); `foto-estirada` no se calibra, se arregla la pieza — _S5, 15-09; referencia de Eli «tiene un cuero», no negro digital_ · ✔×3 (28-09: ST 27-10) · 29-09: ST 07-10: el grano arregló la «foto estirada» del QA
- **R-24** · Ni títulos ni bajadas llevan punto (final ni intermedio), aunque el brief lo traiga — _regla del cliente Hilton, 23-09-2026, citada en el manual de Piso 18_ · ✔×3 (28-09: grilla de octubre) · 29-09: ronda 4 y ST 15-10
- **R-34** · Una pieza se identifica por su **título**, nunca por la columna: la grilla corre fechas sin avisar — _16-09 (NOCHE 25→23), 17-09, 22-09 (animada 23→24)_ · ✔×3
- **R-06** · El titular alterna una línea en itálica fina y otra en VERSALES, en la misma familia — _medido en las 7 aprobadas, 22-09_ · ✔×2 (28-09: 09-10 S2, 13-10 S2, 16-10 y las historias de octubre) · ⚠️ revisada 2026-10-02: las dos voces son el TOPE por bloque, no un piso; cuando un rótulo o una pregunta mezcla más, se rechaza → ver R-62
- **R-09** · Cierre: `Cotiza en` blanco + `piso18.cl` en caja fucsia · `Av. Vitacura 2727, Las Condes` centrada · legal al pie con asterisco — _manual 22-09_ · ✔×2
- **R-12** · El logotipo va arriba y centrado, tope y≈207 @1080 en historia y ≈105 en feed, y nunca se deforma — _kit 15-09; manual_ · ✔×2 (28-09: historias de octubre)
- **R-15** · El zoom de una foto tiene tope 1,0: un recorte que ampliaría se rechaza y se busca otro plano en el banco — _Eli, 16-09, G3 S4: «No tiene que verse en los costados ni la mesa»_ · ✔×2
- **R-23** · El brief es de contenido, no de diseño: un «Este no va» del cliente **no se le lleva a Eli** — _Eli, 22-09: «no tomes eso de ese no va ya que es para contenido no yo»_ · ✔×2 (28-09: el reordenamiento de fechas de la grilla tampoco es suyo, ver R-50)
- **R-27** · Antes de tocar un draft de CapCut, CapCut cerrado (0 procesos); se relee y respalda el draft, y lo que Eli editó encima no se toca — _22-09: se perdió una corrección y hubo que reconectar el clip tres veces_ · ✔×2
- **R-38** · Los íconos salen de un set profesional (Phosphor duotone) y van en cuadro **transparente con borde blanco**; los dibujados a mano no — _Eli, 25-09, C1 S5: «iconos que se vean mejor y más desarrollados, se ven muy extraños»; aprobado_ · ✔×2 (02-10: cinco íconos Phosphor en el post animado del 20-10, aprobado)
- **R-40** · En el feed el cierre es la **línea** «Cotiza … en piso18.cl» (piso18.cl en fucsia), no el botón píldora de las historias — _Eli, 25-09, C1 S5: «me gusta más como estaba en el anterior (…) sin ese botón»_ · ✔×2 (28-09: 16-10 S5)
- **R-41** · Personas generadas: foto de **fotógrafo de eventos** (flash directo, grano, gesto no posado, escena oscura) y pocas personas; y nunca las mismas caras de una pieza publicada — _Eli, 25-09, C1 S5: «se ve bastante falsa (…) sacaría a los dos chicos»_ · ✔×2 (28-09: pista 09-10 y wedding planner, aprobadas) · ⚠️ revisada 2026-10-02: antes de generar gente se busca la foto REAL → ver R-63
- **R-43** · Raleway va SIEMPRE con **cifras de caja alta** (`lnum`): las de estilo antiguo (el 3, 5, 7 y 9 bajan de la línea base, el 0 queda a media altura) se leen «desequilibradas y extrañas» — _Eli, 28-09, grilla oct: «los números y la tipografía de Raleway tiene que verse armónica (…) se está viendo muy desequilibrado»; «acuérdate de lo mismo en toda la grilla»_ · ✔×2 · 29-09: Eli: «los números se ven súper bien» en el calendario
- **R-44** · Una grilla con referencias se calca pieza por pieza: la composición de la ref, con la paleta, las tipografías y el logo de Piso18 — _Eli, 28-09: «guíate de las referencias, que sea muy igual solo que con la identidad visual de PISO18»; 11 piezas aprobadas así_ · ✔×2 · 29-09: ST 15-10 calcada de la ref Midori · 01-10: ST 13 y 19-10 calcadas de su ref · ✔×3 (02-10: las dos aprobadas con ajustes de textura y foto; la estructura calcada no se tocó)

## Lo que ya costó rondas
- **X-01** · Una transición que no termina: el plano que sale tapando al que entra y una curva que gasta el 68 % del recorrido en 4 fotogramas — _ST N°3 S4, reclamo del cliente 22-09; el defecto venía desde la ronda 3_
- **X-02** · Un grade que se nota: la terraza «extraña y oscura» (piel 135→122,6, sombras 65→35,7) — _reel S4 Jazz, Eli 22-09, 1 ronda_
- **X-03** · Abrir la animada con el video del salón vacío — _ST N°3 S4, cliente 17-09 (lo había pedido Eli en la ronda 3), 1 ronda_
- **X-04** · Un encuadre donde el mesón y los costados protagonizan — _G3 del carrusel S4, cliente ronda 4 + Eli ronda 5, 2 rondas_
- **X-05** · Portada con reflejos al valor de la tinta detrás del logotipo (p90 = 253): el promedio decía «oscura» y no se leía — _C1 S4 N°1, Eli ronda 5, 1 ronda_
- **X-06** · Beige sobre la tarjeta casi blanca — _S4 ronda 2, Eli_
- **X-07** · Fondo oscuro liso sin grano: el QA lo bloquea como foto estirada — _ST N°1 y N°2 S5, 15-09_
- **X-08** · `#BodaDePrimavera` en el copy — _carrusel del 21-09 (`FEED!I14`), el cliente lo aprobó sólo al cambiarlo a `#EventoDePrimavera`_
- **X-09** · (interno) Escribir un `src/brand/piso18.ts` «nuevo» sin leer el que existía: casi se destruye el kit — _22-09, lo pilló `tsc`_
- **X-10** · La foto nueva montada como recuadro con bloque fucsia desplazado encima del fondo viejo — _C1 S5, Eli 25-09, 1 vuelta (se leyó mal el pedido)_
- **X-11** · Íconos de línea dibujados a mano, chicos, dentro de los cuadros fucsia de la lista — _C1 S5, Eli 25-09: «no se visualizan nada», 2 vueltas hasta Phosphor con borde blanco_
- **X-12** · Fiesta generada con cuatro personas a plena luz, sonrisas de banco de imágenes — _C1 S5, Eli 25-09: «se ve bastante falsa», 1 vuelta_
- **X-13** · Botón píldora fucsia en la última slide del carrusel — _C1 S5, Eli 25-09, 1 vuelta_
- **X-14** · `sep_26-318` (habitación en penumbra, sin ventana a la vista) como foto del regalo — _C1 S5, Eli 25-09: «me gustó, pero pondría otra más vistosa», 1 vuelta_
- **X-15** · Raleway con cifras de estilo antiguo en «2027», «piso18.cl» y «EN PISO18» — _grilla oct ronda 1, Eli 28-09, 1 vuelta_
- **X-16** · Un reiluminado con un cielo en los vidrios de arriba y otro distinto reflejado abajo — _FEED 13-10 S1, Eli 28-09, 1 vuelta_
- **X-17** · Comida generada «de estudio» (bokeh exagerado, brillo, platos de catálogo) — _Tex-Mex ronda 1, Eli 28-09, 1 vuelta_
- **X-18** · El detalle de un carrusel con el mismo plano general de la portada y demasiada comida — _Tex-Mex S2 ronda 2, Eli 28-09, 1 vuelta_
- **X-19** · (interno) Invitados generados posando de frente con los brazos arriba — _ST 09-10, tirada 1, cazado antes de mostrar (el mismo rechazo de X-12)_
- **X-20** · La G2 de un carrusel como papel plano cuando el brief la pide como imagen — _FEED Fechas 2027, cliente C13 29-09, 1 ronda_
- **X-21** · Sacar el calendario aprobado al pasar la G2 a foto — _Eli 29-09: «me gustaba cómo se veía temporada alta con ese diseño y el calendario», 1 vuelta_
- **X-22** 
