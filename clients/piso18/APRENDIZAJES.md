# PISO 18 Centro de Eventos — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para PISO 18.** Nada de acá se copia a otra marca, ni a una hermana
> (DoubleTree, QB y Between son cuentas aparte aunque compartan edificio y Drive).
> Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> Criterio: **Elisabet Soto «Eli»**, con revisión de la jefa de diseño **Constanza Lizana** · Aprueba: **el cliente Hilton, por comentarios en la grilla (contenido: Carlos Figueroa y Scarlette Muñoz)**
> Última cosecha: **2026-09-29** · Cosechas: **10**

## 1. Quién es el cliente

Centro de eventos en el piso 18 del complejo Hilton (Av. Vitacura 2727, Las Condes).
Vende matrimonios, cumpleaños y celebraciones; el objetivo comercial de cada pieza es
**llevar a cotizar** en `piso18.cl`. Habla en tono de invitación elegante: la foto del
evento manda, el texto acompaña y el fucsia marca sólo la oferta. Comparte edificio con
DoubleTree, **no sistema gráfico**. Ojo con una palabra: «bodas» no se escribe nunca.

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | Eli encarga al estudio; la grilla (brief de contenido) la dejan Carlos Figueroa y Scarlette Muñoz |
| Quién aprueba (cliente) | Hilton, en la grilla. Eli revisa y aprueba antes, mirando una página de antes/después |
| Por dónde llega el feedback | Comentarios en celda de la grilla (hojas FEED · STORIES · ORGÁNICO), **prependidos** sobre el anterior; encargo directo de Eli; y **hilos nativos de la jefa de diseño Constanza Lizana** con @Eli, anclados a la celda del brief (desde el 29-09, R-59) |
| Dónde se entrega | `S<n> HILTON <MES> 2026 › PISO18` en Drive (la carpeta hereda permisos de escritura del cliente); banners en `10sST2d5K43vVYFgtn084AsAMNRwCYEoe` |
| Ritmo | Grilla mensual por semanas (S1–S5); estáticas, historias animadas en Remotion y reels en CapCut |
| Rondas típicas | Carrusel S4: 5 rondas. Historia animada S4: 7 rondas (orden de fotos, titular y, sobre todo, la transición) |

## 3. Identidad en corto

- **Fucsia `#D4145A`** (lo fijó Eli; la medición sólo verifica) · blanco sobre foto · tinta `#1A1A1A` · tarjeta `#F7F5F2` · beige `#EFE6D9` · beige hondo `#E6DACA`.
- **IvyPresto Headline** (titulares, poco) · IvyPresto Display (bajadas) · **Raleway** (el caballo de batalla) · Against (alterna, sin `¿` ni `¡`).
- Logotipo `public/assets/piso18/logo-piso18-completo.png`, arriba y centrado, proporción 2,4825.
- Máster **2250 px**: feed 2250×2813 · historia 2250×4000 · promo 1080×1080 · banner web PC/mobile (sin medir).
- Kit que manda sobre cualquier número: `src/brand/piso18.ts`.

## 4. Reglas firmes

- **R-01** · «bodas» no se escribe nunca: va matrimonio(s) o novios, aunque el brief o el hashtag lo traigan — _Eli, 15-09-2026; ratificada por el cliente en `FEED!I14` el 17-09 («no usemos la palabra BODA»)_ · ✔×4 (28-09: las 11 de octubre sin «boda») · 29-09: ronda 4 y ST 15-10 sin «boda»
- **R-02** · Nada de DoubleTree entra en Piso 18 (ni tipografía, ni paleta, ni logo, ni «LA LEY DE ELI»), y nada de acá va para allá — _Eli: «Todo es propio y diferente a DT, recuerda no mezclar las marcas»; reglas.yaml_ · ✔×1
- **R-03** · El fucsia nunca decora: sólo caja del precio, filete, `piso18.cl` del CTA, destacado del titular y botones — _medido en las 7 aprobadas; manual 22-09_ · ✔×1 · ⚠️ revisada 2026-09-25: Eli pidió «cuadros de color fucsia» como toque de color en el carrusel S5 → ver R-39 · y el 28-09 los clips del 16-10 → ver R-47 · y el 29-09 «Dulce/Salada» y las flechas de la ST 07-10, por pedido de Eli
- **R-04** · El fucsia de Selfie (`#FF007C`) no entra: el QA lo corta a ΔE 12 — _Eli, 15-09; reglas.yaml `fucsia-de-selfie`_ · ✔×1
- **R-05** · El beige `#EFE6D9` no se pone sobre la tarjeta `#F7F5F2`: ahí no se lee como beige — _Eli, ronda 2 S4_ · ✔×1
- **R-06** · El titular alterna una línea en itálica fina y otra en VERSALES, en la misma familia — _medido en las 7 aprobadas, 22-09_ · ✔×2 (28-09: 09-10 S2, 13-10 S2, 16-10 y las historias de octubre)
- **R-07** · Dos registros que no se mezclan: promo (foto oscurecida + caja fucsia con la cifra) y editorial (tarjeta blanca festoneada, sin caja ni cifra) — _manual 22-09, sobre `ST N°1 S1` y `C2 S1 n°2`_ · ✔×1
- **R-08** · Bloque de precio: `ANTES` chico sobre la cifra tachada, `AHORA` sobre la cifra nueva en caja fucsia, cifras en serif; en descuento, el % gigante con `DCTO.` al costado — _manual 22-09_ · ✔×1
- **R-09** · Cierre: `Cotiza en` blanco + `piso18.cl` en caja fucsia · `Av. Vitacura 2727, Las Condes` centrada · legal al pie con asterisco — _manual 22-09_ · ✔×2
- **R-10** · Siempre hay botón en las historias (y en algunos reels), sólo en dos esquemas: fucsia/blanco o blanco/fucsia — _Eli, 15-09: «Siempre hay que hacer botones en las historias»_ · ✔×1
- **R-11** · La interacción no se dibuja: se deja el aire y el sticker real lo pone el CM — _manual; marca.json `botones`_ · ✔×3 (28-09: ST 07 y 09-10) · 29-09: ST 15-10, hueco para el cuadro de respuestas
- **R-12** · El logotipo va arriba y centrado, tope y≈207 @1080 en historia y ≈105 en feed, y nunca se deforma — _kit 15-09; manual_ · ✔×2 (28-09: historias de octubre)
- **R-13** · `logo PISO18.png` no es un logo: es una plantilla de historia con velo negro en degradado. Mide el alfa antes de montar — _manual 22-09_ · ✔×1
- **R-14** · La portada de carrusel lleva el velo de marca (alfa 0,588 arriba → 0 al 41,7 % del alto) **debajo** del logotipo; se rehace desde la foto limpia — _Eli, 16-09, S4 ronda 5: «Oscurece un poco arriba con una transparencia muy sutil»_ · ✔×1
- **R-15** · El zoom de una foto tiene tope 1,0: un recorte que ampliaría se rechaza y se busca otro plano en el banco — _Eli, 16-09, G3 S4: «No tiene que verse en los costados ni la mesa»_ · ✔×2
- **R-16** · Si Eli manda una captura con el encuadre, el recorte se deduce midiendo tres puntos comunes, no a ojo — _S4 ronda 5, 16-09_ · ✔×1
- **R-17** · La caja de recorte de cada pieza queda escrita en el script que la produce — _S4, 16-09: dos recortes hubo que reconstruirlos por correlación_ · ✔×4 (28-09: `scripts/p18-oct-fotos.py`) · 29-09: cajas de fin160, deco112, deco143 en `p18-oct-fotos.py`
- **R-18** · Todo fondo oscuro plano lleva grano (`GranoFondo`); `foto-estirada` no se calibra, se arregla la pieza — _S5, 15-09; referencia de Eli «tiene un cuero», no negro digital_ · ✔×3 (28-09: ST 27-10) · 29-09: ST 07-10: el grano arregló la «foto estirada» del QA
- **R-19** · Las cifras no se alinean con CSS (Raleway no trae `tnum`): cada dígito en una caja al **máximo** de la fila — _kit 15-09; `$4.500.000` vs `$6.000.000`_ · ✔×1
- **R-20** · Un titular que empieza con `¿` o `¡` no se compone en Against — _manual; «¿Te casas en verano?»_ · ✔×1
- **R-21** · IvyPresto (OTF CFF) se verifica en cada render con `p18FuentesListas()`; nunca se da por cargada — _manual; precedente Brushwell_ · ✔×1
- **R-22** · De la carpeta `14jOWfpSm7Nm1lXAABZNThZAa5_5BulzC` no se usan fotos de 2020 hacia abajo, por fecha EXIF de captura — _orden de Eli, manual_ · ✔×1
- **R-23** · El brief es de contenido, no de diseño: un «Este no va» del cliente **no se le lleva a Eli** — _Eli, 22-09: «no tomes eso de ese no va ya que es para contenido no yo»_ · ✔×2 (28-09: el reordenamiento de fechas de la grilla tampoco es suyo, ver R-50)
- **R-24** · Ni títulos ni bajadas llevan punto (final ni intermedio), aunque el brief lo traiga — _regla del cliente Hilton, 23-09-2026, citada en el manual de Piso 18_ · ✔×3 (28-09: grilla de octubre) · 29-09: ronda 4 y ST 15-10
- **R-25** · La corrección de color que se nota está mal: la piel no baja más de ~2 puntos, las sombras no se desploman, recorte en 0,00 % — _Eli, 22-09, terraza del reel S4: «hazlo sutil como para que no se note»_ · ✔×1
- **R-26** · «Quemado» casi nunca es sobreexposición: se diagnostica midiendo punto de negro, dominante, micro contraste y recorte, y se hornea con ffmpeg (los deslizadores de CapCut quedan en cero) — _reel S4, 6ª sesión 22-09_ · ✔×1
- **R-27** · Antes de tocar un draft de CapCut, CapCut cerrado (0 procesos); se relee y respalda el draft, y lo que Eli editó encima no se toca — _22-09: se perdió una corrección y hubo que reconectar el clip tres veces_ · ✔×2
- **R-28** · En la historia animada (Remotion) los planos se escriben del primero al último para que el que entra quede arriba, con curva simétrica — _reclamo del cliente 22-09: «se queda pegada a la mitad»_ · ✔×1
- **R-29** · Una transición se mide en secuencia PNG en **todas** las transiciones: cero fotogramas congelados dentro del empuje y cero saltos >25 fuera — _S4 ronda 7, 22-09; reglas.yaml v5_ · ✔×1
- **R-30** · En una historia animada, posición y contraste del botón se miden en el último fotograma — _manual; reglas.yaml_ · ✔×1
- **R-31** · Una pieza corregida se reemplaza en Drive **conservando su enlace** — _S4 rondas 4, 5, 6 y 7 (16 al 22-09)_ · ✔×7 (28-09: rondas 2 y 3 de octubre) · 29-09: ronda 4: 8 archivos reemplazados · ✔×8 (29-09 rondas 5 y 6: 6 láminas, md5 verificado)
- **R-32** · La revisión se publica como página de antes/después; nada interno va a la carpeta de entrega, que ve el cliente (`@hilton.com` con permiso de escritura) — _hallazgo 16-09; rondas 4–7 aprobadas así_ · ✔×6 (28-09: páginas r1 y r2 de octubre) · 29-09: páginas r4 y st1510
- **R-33** · Lo nuevo de la grilla se detecta por diff de **conjunto de cadenas** contra la instantánea anterior: el comentario se prepende y no lo delatan ni la celda ni el `modifiedTime` — _confirmado el 16, 17 (×2), 22-09 y 28-09 (grilla oct: 8 comentarios nuevos del cliente en celdas que estaban vacías; 28-09 noche: la grilla reordenó 3 piezas entregadas)_ · ✔×7 · 29-09: grilla 29-09 12:21Z: 5 comentarios nuevos sobre piezas entregadas
- **R-34** · Una pieza se identifica por su **título**, nunca por la columna: la grilla corre fechas sin avisar — _16-09 (NOCHE 25→23), 17-09, 22-09 (animada 23→24)_ · ✔×3
- **R-35** · El GIF de una pieza animada va a 25 fps, sin difuminado y a 540×960; lo que se publica en Instagram es el MP4 — _Eli, 22-09: «guárdalo igual en gif»; `scripts/p18-s4-gif.py`_ · ✔×1
- **R-36** · El titular va prácticamente a sangre (29 px de margen @1080): el respiro de borde de la marca es 26 px, no los 60 de agencia — _medido en `ST N°1 S1`; reglas.yaml_ · ✔×1
- **R-37** · «Agrega una foto a la slide» es **reemplazar el fondo**, no montar un recuadro encima — _Eli, 25-09, C1 S5: «yo decía las fotos, reemplazando las actuales»_ · ✔×1
- **R-38** · Los íconos salen de un set profesional (Phosphor duotone) y van en cuadro **transparente con borde blanco**; los dibujados a mano no — _Eli, 25-09, C1 S5: «iconos que se vean mejor y más desarrollados, se ven muy extraños»; aprobado_ · ✔×1
- **R-39** · Lista de beneficios en carrusel: **número** blanco (IvyPresto) en cuadro fucsia `#D4145A`; los íconos, grandes y en fila sobre el titular, iguales en todas las slides de la lista — _Eli, 25-09, C1 S5: «que fueran solamente un número (…) en esos cuadraditos»; aprobado_ · ✔×1
- **R-40** · En el feed el cierre es la **línea** «Cotiza … en piso18.cl» (piso18.cl en fucsia), no el botón píldora de las historias — _Eli, 25-09, C1 S5: «me gusta más como estaba en el anterior (…) sin ese botón»_ · ✔×2 (28-09: 16-10 S5)
- **R-41** · Personas generadas: foto de **fotógrafo de eventos** (flash directo, grano, gesto no posado, escena oscura) y pocas personas; y nunca las mismas caras de una pieza publicada — _Eli, 25-09, C1 S5: «se ve bastante falsa (…) sacaría a los dos chicos»_ · ✔×2 (28-09: pista 09-10 y wedding planner, aprobadas)
- **R-42** · La foto del beneficio DoubleTree sale de la sesión **Hotel general SEP 2026** y tiene que ser vistosa: ventana, cama y el desayuno real a la vista — _Eli, 25-09, C1 S5: eligió así contra `sep_26-318`; va `sep_26-313`_ · ✔×1
- **R-43** · Raleway va SIEMPRE con **cifras de caja alta** (`lnum`): las de estilo antiguo (el 3, 5, 7 y 9 bajan de la línea base, el 0 queda a media altura) se leen «desequilibradas y extrañas» — _Eli, 28-09, grilla oct: «los números y la tipografía de Raleway tiene que verse armónica (…) se está viendo muy desequilibrado»; «acuérdate de lo mismo en toda la grilla»_ · ✔×2 · 29-09: Eli: «los números se ven súper bien» en el calendario
- **R-44** · Una grilla con referencias se calca pieza por pieza: la composición de la ref, con la paleta, las tipografías y el logo de Piso18 — _Eli, 28-09: «guíate de las referencias, que sea muy igual solo que con la identidad visual de PISO18»; 11 piezas aprobadas así_ · ✔×2 · 29-09: ST 15-10 calcada de la ref Midori
- **R-45** · Comida generada = **foto documental del fotógrafo del evento** (luz del salón, casi todo nítido, porciones de banquetería con imperfecciones), con el buffet real de Piso18 de referencia; nunca comida de estudio con bokeh y brillo — _Eli, 28-09, Tex-Mex: «que se vean mucho más realistas porque se están viendo un poco extrañas»_ · ✔×2 · 29-09: temáticas de la 15-10, Eli: «se quedaron perfectas»
- **R-46** · En un carrusel de detalles, cada slide cambia el plano de la portada (ángulo cenital, menos cantidad) y no repite la vista general — _Eli, 28-09, Tex-Mex S2: «se ve muy similar a la portada (…) tal vez la vista más cenital y se ve demasiada cantidad de tacos»_ · ✔×1
- **R-47** · Los elementos de papelería gráfica (los clips de la hoja) van en fucsia `#D4145A` — _Eli, 28-09, FEED 16-10: «las cositas de archivadora en color fucsia de piso 18»_ · ✔×1
- **R-48** · Un ventanal reiluminado lleva **un solo cielo continuo**; si el carrusel ya tiene una lámina aprobada, esa va de referencia de color — _Eli, 28-09, 13-10 S1: «se ve como dos tipos de atardeceres y eso se ve súper extraño»_ · ✔×1
- **R-49** · Para acercar el color de una foto a la referencia sin perderla, se EDITA esa misma foto (Nano Banana Pro: sólo el color de algunas flores); no se regenera — _Eli, 28-09, 06-10: «me gusta mucho la actual (…) en vez de ciertos rosados, esos tonos azulitos»; aprobado_ · ✔×1
- **R-50** · Sólo diseño: cuando la grilla **mueve de fecha** una pieza ya entregada, no se renombra ni se mueve nada en Drive; se avisa a Eli qué quedó desalineado y se deja el script listo (`scripts/p18-oct-reordenar.py`) — _Eli, 28-09: «solo de diseño no muevas cosas que no son mi trabajo, es las piezas diseñadas»_ · ✔×1
- **R-51** · El llamado (botón o línea «Cotiza/Reserva … en piso18.cl») va **sólo si el brief trae CTA**; si trae otra interacción (barra, encuesta, respuestas) no se agrega — _Eli, 29-09: «Solamente si está en el brief, no lo agregues siempre»; cliente en ST 05-10: «quitemos botón diseñado para no repetir info»_ · ✔×1 (ST 07-10 y 15-10)
- **R-52** · Segunda versión del logotipo: **esquina inferior derecha, blanco**, 210 px @1080, margen 48, sobre un velo leve de pie (`LogoEsquina`), siempre a la misma medida; para fotos sin texto — _Eli, 29-09, FEED Arreglos: «que el logo sea en blanco (…) que siempre ese logotipo en esa esquina sean iguales»_ · ✔×1
- **R-53** · Carrusel de foto continua: UNA foto horizontal partida al medio con el corte en un hueco; si la lámina con texto va oscurecida, va **entera** oscurecida y la capa **empieza ya en la lámina anterior** (0 → valor pleno en el corte) para que el negro fluya sin escalón — _cliente FEED C13 29-09 («seleccionemos alguna horizontal para que quede dividida de forma continua») + Eli, 3 vueltas_ · ✔×1
- **R-54** · Si la ref trae papel (hoja rasgada, nota), va una **textura de papel real** (generada con la ref de guía) y el rasgado con mordidas hondas del mismo tono; el papel plano y el zigzag no pasan — _Eli, 29-09, ST 15-10: «la textura muy, muy igual al papel que está ahí»_ · ✔×1
- **R-55** · El fondo de una historia es una escena real de Piso18 **con sus luces** (esferas con velas, guirnaldas), poco desenfocada para que brillen, y lo lindo de la foto queda a la vista, no detrás del texto — _Eli, 29-09, ST 15-10: «más con luces que tiene Piso18, una escena más bonita»_ · ✔×1
- **R-56** · «Fondo de algún montaje» = foto real de un salón montado, oscurecida (~0,5) y con desenfoque gaussiano para que no compita con lo del frente; rótulos y flechas encima, en fucsia — _cliente ST D14 29-09 + Eli, 2 vueltas_ · ✔×1
- **R-57** · Los rótulos en Raleway de caja alta llevan espaciado **discreto (~0,08 em, 2 px a 26 px)**; el espaciado abierto de letra por letra (0,27 em) se lee como diseño de IA — _Constanza Lizana (jefa de diseño), 29-09, FEED 09-10 G2: «Ojo con esa separación de letra x letra en las palabras, es demasiado ia :(»_ · ✔×2 (Eli 29-09 la extendió a todo el mes: 13-10, 16-10, ST 15-10, ST 27-10)
- **R-58** · Texto grande sobre una foto va en **relleno sólido**, no calado/contorno: el trazo fino se pierde contra la foto — _Constanza Lizana, 29-09, ST 07-10: «Se pierde mucho el texto "dulce" "salada" en delineado, prueba con la línea más gruesa o bien mejor sólido»_ · ✔×1
- **R-59** · La jefa de diseño (Constanza Lizana) comenta con **hilos nativos de la grilla que mencionan a Eli**, no en las celdas: el diff de celdas no los ve. Leer siempre `read_file_content` con `includeComments=true` y filtrar por autor y fecha; los estados de sus piezas pasan a EN CAMBIOS / EN CAMBIOS DISEÑO — _29-09, ronda 5_ · ✔×1

## 5. Excepciones

- **E-01** · R-01 es la **única** excepción conocida a que los textos en pantalla vayan literales del brief — _reglas.yaml `sin-bodas`_
- **E-02** · El velo de R-14 va sólo en la **portada**: las otras slides no llevan logotipo y el brief las quiere limpias — _Eli, 16-09_
- **E-03** · La zona segura de Meta se relaja en orgánico: el logotipo vive dentro de los 250 px de arriba por sistema y el legal al pie llega al 3 % de tinta — _calibrado sobre `ST N°1 S1`, reglas.yaml_
- **E-04** · Los reels se montan en **CapCut** (Eli); las historias animadas se escriben en **Remotion** (`P18StMontaje.tsx`) — _manual 22-09_
- **E-05** · La S3 de septiembre la hizo Eli a mano: no se toca, y el token del estudio no puede reemplazar sus archivos — _Eli, 16-09: «solo toma s4 ya que yo hice la s3»_
- **E-06** · En las historias de encuesta y de barra de reacción (07 y 09-10) el cierre va en **línea**, «Cotiza tu evento en piso18.cl», y no en píldora, como en `ST N°4 S4`: el botón competiría con el sticker — _grilla oct, aprobado 28-09_ · ⚠️ revisada 2026-09-29: sin CTA en el brief no va ni la línea (R-51); la 09-10 la conservó por decisión de Eli
- **E-07** · Una historia con sticker de enlace (visita virtual 27-10) va sin botón, con el pie libre para el sticker — _la misma excepción del cliente del 18-09; aprobado 28-09_
- **E-08** · Si la celda REF dice «sin texto ni cuadro, dejar logo», manda sobre el campo «Texto» del brief: va foto + logo, y el texto queda para el copy — _FEED 27-10 wedding planner, aprobado 28-09_

## 6. Lo que se aprueba a la primera

- **A-01** · Cambiar la apertura de la animada por una foto de arreglos que sea **el mismo arreglo del plano 2 visto de lejos** (sin rostros, sin logo de la pared, sin ampliar) — _ST N°3 S4, ronda 6, Eli «Aprobado» 17-09_
- **A-02** · Los planos que no se tocan pasan solos: `C1 S4 N°2`, `C1 S4 N°4` y `ST N°2 S4` quedaron de la ronda 3 sin cambios — _S4, 16-09_
- **A-03** · Encuesta con la opción B cambiada a mesa puesta evitando repetir una foto del feed de 4 días antes (`piso_18-28` y no `piso_18-85`) — _ST N°4 S4, ronda 4, 16-09_
- **A-04** · Post nuevo con la foto que el cliente eligió por nombre + logotipo: «Que sea esta foto, con logo y estamos» — _Post n°2 S4 25-09, ronda 4_
- **A-05** · La selección y el orden de fotos de la animada, y su ritmo (2,2 s por plano, 13 s) — _cliente 22-09: «Está ok la selección de fotos»_
- **A-06** · Carrusel de beneficios con fondo a sangre, números en cuadro fucsia, fila de íconos Phosphor con borde blanco y cierre en línea — _C1 S5 ronda 4 v4, Eli «aprobados me gusta» 25-09 (costó 4 vueltas en el día, ver X-10…X-14)_
- **A-07** · A la primera, calcando la ref: FEED 13-10 S2 («con esta vista»), FEED 27-10 wedding planner (IA con una sola planner) y las cinco historias de octubre — 05-10 animada con Kling 2.5 sobre la foto real, 07-10 «Dulce / Salada», 09-10 nota con cintas, 23-10 cuadro de vidrio, 27-10 teléfonos con el tour de Matterport — _Eli, 28-09_
- **A-08** · Estructura a la primera, con sólo cifras y clips corregidos: FEED 09-10 S2 (papel beige + calendario con el día encerrado en fucsia) y FEED 16-10 (collage 2×2 + fajo de hojas con clip) — _Eli, 28-09: «me encantó»_
- **A-09** · Las tres temáticas de cumpleaños generadas sobre la mesa real (retro, tropical, blanco y dorado), la ST Primavera sin botón y la «¿Qué» de la 09-10 — _Eli 29-09: «las fotos se quedaron perfectas»; «para el ST de primavera, sin botón, quedó ok»_

## 7. Lo que se rechaza

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
- **X-22** · Capa oscura en rampa sólo dentro de la G2 — _Eli 29-09: «quiero que la G dos tenga esa transparencia oscurecida», 1 vuelta_
- **X-23** · Logo arriba y centrado en negro sobre el mantel claro — _FEED Arreglos, Eli 29-09 → esquina y blanco, 2 vueltas_
- **X-24** · Botón diseñado en una historia que repite la info del sticker — _ST 05-10, cliente C14 29-09_
- **X-25** · Encuesta sobre papel beige plano — _ST 07-10, cliente D14 29-09: «¿Veamos un fondo más entretenido?»_
- **X-26** · Rótulos y flechas en blanco sobre el montaje, con el fondo poco oscuro — _ST 07-10, Eli 29-09, 1 vuelta_
- **X-27** · Papel plano con borde en dientes de sierra — _ST 15-10, Eli 29-09, 1 vuelta_
- **X-28** · Fondo de la mesa apagada, sin luces, con lo bonito tapado por la hoja — _ST 15-10, Eli 29-09, 1 vuelta_
- **X-29** · Rótulo de caja alta con letter-spacing 7 px (0,27 em) — _FEED 09-10 G2, Constanza 29-09_
- **X-30** · Rótulos calados (contorno 2,8 px) sobre foto oscurecida — _ST 07-10, Constanza 29-09_

## 8. Preguntas abiertas

- «Este no va» sobre el post del 23-09 (`FEED!M14`, «PISO18 DE NOCHE»): ya no es de Eli (R-23). **¿Qué reemplaza contenido?** → Carlos Figueroa / Scarlette Muñoz.
- ¿El apilado invertido de R-28 está en otras historias animadas de la cuenta? → Eli (propuesto, sin respuesta).
- La música del reel S4 es el instrumental de *Flowers* (Miley Cyrus): exposición de marca → **Valeria**.
- El reel S4 Jazz sigue sin exportar ni subir; el salto de luz entre la entrada de Jaz (mediana 52) y las flores (151): ¿se suaviza? → Eli.
- El **banner web** (PC y mobile, 72/150 PPP) es un formato de la marca sin medir → Eli.
- ¿Los 1080×1080 son piezas de publicación o previews de grilla? ¿Existe manual del cliente que documente `#D4145A`? → Eli / KAM.
- «Ese sería para el G3 de la S3»: se aplicó a la S4. Si era el `C1 S3`, está sin hacer → Eli.
- `Post S4 PISO18 25-09.png` es la pieza del 23-09: el portal levanta por nombre, arréglalo antes de pasarla por ahí → Eli.
- Ampliar el token del estudio a `drive.readonly` (hilos nativos de la grilla dan 404) → **Valeria**.
- Falta calibrar el QA contra las **26 aprobadas** que ya están en `raw/hilton/piso18/` → estudio.
- La ronda 4 del C1 S5 la aprobó Eli, pero el cambio no pasó por la grilla: ¿el cliente la vio? → Eli / KAM.
- `P18C1Cumple.tsx` no declara sus textos al QA, así que la regla «sin bodas» queda «sin verificar» en cada corrida → estudio.

- ~~ST 09-10 «de una matrimonio»~~ → resuelto el 28-09: va «un matrimonio» y Eli lo aprobó.
- El upscaler de precisión de Magnific falla seguido («terminó sin entregar imagen»): Tex-Mex S2 y S3 y el wedding planner quedaron ampliados ×1,22–1,27. ¿Se reintenta antes de publicar? → estudio / Eli
- Las piezas de octubre no declaran sus textos al QA, así que «sin bodas» queda «sin verificar» (se revisó a mano) → estudio
- La grilla reordenó 3 piezas ya entregadas (Fechas 2027 09→06-10 · Arreglos 06→09-10 · Tu próxima celebración 16-10 S3 → 30-10 S5, contenido idéntico). En Drive siguen con la fecha vieja y el portal levanta por nombre. ¿Quién renombra? → Eli / KAM (script `scripts/p18-oct-reordenar.py`, sin correr)
- Smart App Control de Windows bloquea el compositor de Remotion en la máquina de Eli desde el 29-09: los MP4 (ST 16 y 30-10) no se pueden rendir ahí → **Valeria**
- ~~El cliente preguntó «¿el montaje es real o IA?»~~ → respondido en la celda D13 el 29-09 («ES REAL SOLO SE MODIFICO UN POCO EL COLOR») y tachado.
- Los dos hilos de Constanza (FEED C9, STORIES D8) siguen **abiertos** en la grilla y las piezas en EN CAMBIOS / EN CAMBIOS DISEÑO: ¿quién los responde/cierra y devuelve el estado? → Eli
- ¿El criterio de espaciado de Constanza aplica a septiembre y a las piezas futuras de otras diseñadoras en Piso18? Se aplicó sólo a octubre → Eli / Constanza
- La ST 09-10 conserva «Cotiza tu evento en piso18.cl» sin CTA en el brief (R-51): Eli la dio por buena; ¿se mantiene? → Eli

## 9. Registro de cosechas

### 2026-09-29 (tarde) — Elisabet Soto con Claude · RONDA 5: comentarios de Constanza Lizana — CORREGIDAS Y EN DRIVE
- Constanza, en hilos nativos (verbatim): FEED C9 «Aquí en el slide 2 "Temporada alta 2027" Ojo con esa separación de letra x letra en las palabras, es demasiado ia :(» · STORIES D8 «Se pierde mucho el texto "dulce" "salada" en delineado, prueba con la línea más gruesa o bien mejor sólido».
- nuevas **R-57** espaciado discreto · **R-58** texto sobre foto en sólido · **R-59** los hilos de la jefa de diseño se leen aparte. Rechazos **X-29**, **X-30**. Página https://claude.ai/artifact/3JstsrpP24PacLKw8VR8zc; md5 en Drive verificado.
- Ronda 6 (misma tarde), Eli: «ahora sabiendo ese aprendizaje, ve si hay algo que corregir a futuro de grilla de oct» → R-57 aplicada a 13-10 G2 («ESCRIBE TU HISTORIA DE AMOR» 0,36 y «PISO18.CL» 0,19), 16-10 G1 («EN PISO18» 0,25), ST 15-10 (temáticas 0,16) y ST 27-10 («VISITA VIRTUAL 360°» 0,30) — reemplazadas en Drive (md5 verificado). «TEX MEX» (0,07) ya cumplía. Página https://claude.ai/artifact/Hxn9fNwxfKnR4iJPMN9v4D.
- ✔ subieron: **R-31** (×8), **R-57** (×2). §2 actualizado: Constanza comenta por hilos nativos. §8: 2 preguntas nuevas.
- Eli, 29-09: «como siempre de aquí en adelante reemplaza los cambios que realizaste y déjalos en Drive» → toda corrección se reemplaza en Drive en el mismo turno, sin esperar OK (preferencia de Eli, memoria `subir-a-drive-al-aprobar`).
- Técnica: el render por Chrome dibuja distinto la perspectiva 3D (celulares de la ST 27-10 corridos) → se injertó sólo la franja del rótulo sobre el PNG aprobado.
- Fuera de alcance: el criterio de Constanza también llegó a DT y Between el mismo día, pero se cosecha en `clients/hilton/`, no acá. Candidata a regla del estudio (para Valeria): «rótulos en caja alta con espaciado discreto; el tracking abierto se lee como IA».

### 2026-09-29 — Elisabet Soto con Claude · RONDA 4 de octubre + ST 15-10 nueva (8 vueltas en el día) — APROBADAS Y EN DRIVE
- Cliente en la grilla (verbatim): FEED C13 «Según brief la G2 también es imagen, seleccionemos alguna horizontal para que quede dividida de forma continua?» · FEED D13 «Falta logo, el montaje es real o IA?» · ST C14 «Ok, pero quitemos botón diseñado para no repetir info» · ST D14 «Veamos un fondo más entretenido? que sea d ealgún montaje» · ST F14 «El Que con q mayúscula».
- nuevas **R-51** CTA sólo si el brief lo trae · **R-52** logo de esquina blanco, siempre igual · **R-53** carrusel de foto continua con la capa que empieza en la lámina anterior · **R-54** papel = textura real + rasgado hondo · **R-55** fondo con las luces de Piso18 · **R-56** fondo de montaje desenfocado con rótulos fucsia.
- ✔ subieron: R-01 (×4), R-11 (×3), R-17 (×4), R-18 (×3), R-24 (×3), R-31 (×7), R-32 (×6), R-33 (×7), R-43 (×2), R-44 (×2), R-45 (×2). R-03 anotada (fucsia en Dulce/Salada). ⚠️ E-06 revisada por R-51. Aprobada **A-09**; rechazos **X-20…X-28**. §8: 3 preguntas nuevas.
- Fuera de alcance: nada se copió a DT, QB ni Between. Candidatas a regla del estudio (para Valeria): «el llamado a cotizar va sólo si el brief trae CTA» y el render de estáticas por Chrome cuando Windows bloquea Remotion.

### 2026-09-29 — Claude nocturno (nube) · revisión de rutina, sin sesiones nuevas
- sin aprendizajes nuevos: el único commit que `memoria-cliente.py pendientes` marcó (`2e2cf62`) es el mismo commit que ya cosechó la revisión de la grilla de octubre (ver la entrada de abajo, R-50). Se lista a sí mismo porque tocó `BITACORA.md` y `APRENDIZAJES.md` en el mismo commit.

### 2026-09-28 (noche) — Elisabet Soto con Claude · revisión de la grilla de octubre, sin piezas nuevas
- **Sin diseño:** todo lo que está en OK ya estaba entregado y aprobado. Siguen fuera: FEED 20-10 cumpleaños (PENDIENTE POR CLIENTE, ahora «POST ANIMADO» con una pregunta de Carlos sin responder), ST 08-10 (PENDIENTE), ST 13/15/16/19/21/30-10 (EN REVISIÓN) y el reel del Día del Chef (sin estado).
- nueva **R-50** sólo diseño: no se renombra ni se mueve en Drive lo que la grilla reordena. ✔ subieron R-23 (×2) y R-33 (×6). §8: 1 pregunta nueva (quién renombra las 3 piezas movidas).
- Fuera de alcance: nada se copió a DT, QB ni Between.

### 2026-09-28 (tarde) — Elisabet Soto con Claude · GRILLA DE OCTUBRE, 11 piezas, 3 vueltas — APROBADA
- nuevas **R-43** Raleway siempre con `lnum` · **R-44** calcar la ref con la identidad de Piso18 · **R-45** comida IA = foto documental · **R-46** el detalle cambia el plano de la portada · **R-47** clips en fucsia · **R-48** un solo cielo en el ventanal · **R-49** editar la foto para acercar el color a la ref.
- ✔ subieron: R-01 (×3), R-06 (×2), R-11 (×2), R-12 (×2), R-17 (×3), R-18 (×2), R-24 (×2), R-31 (×6), R-32 (×5), R-40 (×2), R-41 (×2). R-03 queda anotada con los clips (R-47).
- nuevas **E-06** cierre en línea en las encuestas · **E-07** sin botón con sticker de enlace · **E-08** la celda REF manda sobre el campo Texto. Aprobadas **A-07** y **A-08**. Rechazos **X-15…X-19**.
- Fuera de alcance: nada se copió a DT, QB ni Between. Candidata a regla del estudio (para Valeria): «Raleway siempre con cifras de caja alta (`lnum`)», que ya costó rondas en QB y Between.

### 2026-09-28 — Claude con Eli · `/al-dia hilton`, foco S1 de octubre (sin piezas)
- **Sin reglas nuevas:** no se diseñó nada. ✔ sube R-33 (×5).
- Llegaron los primeros comentarios del cliente de octubre. Son de **contenido** (R-23) y se aplican cuando la pieza pase a OK. Verbatim: FEED 13-10 «Ojo que no queden todos los carruseles juntos» · FEED 20-10 «Puede ser animado y ponemos lo que trae el cumple» · ST 13-10 «No hablemos de temporada alta» · ST 15-10 «Dejémos cuadro de respuesta a ver si prende» · ST 16-10 «Solo texto principal» · ST 19-10 «Foco fiesta empresa fin de añoi» · ST 21-10 «Busquemos otra dinámica» · ST 30-10 «Dejémos El broche perfecto para tu historia».
- S1 en OK: FEED 06-10 flores y 09-10 fechas 2027; ST 05-10 primavera, 07-10 encuesta de estaciones y 09-10 encuesta de recuerdos. La ST 08-10 «pasos» quedó PENDIENTE POR CLIENTE. §8: 1 pregunta nueva («una matrimonio»).

### 2026-09-26 — Claude nocturno (nube) · revisión de rutina, sin sesiones nuevas
- sin aprendizajes nuevos: los 2 commits de ayer (67429c1, adead40) ya están cosechados en las entradas de abajo (C1 S5 cumpleaños ronda 4 aprobada; lectura de la grilla de octubre sin piezas). El único que `pendientes` marcó (adead40) es el mismo que hizo la última cosecha del día.

### 2026-09-25 (noche) — Claude con Eli · lectura de la grilla de octubre, sin piezas
- **Sin aprendizajes nuevos:** no se diseñó nada. Grilla oct leída en vivo: FEED 7/7 EN REVISIÓN, STORIES 12 sin estado, reel orgánico sin estado; ningún comentario del cliente. Los 18 hilos son internos (Scarlette → Carlos, contenido), 4 abiertos: reel Día del Chef, ST 30-10, ST 19-10 y ST 08-10.

### 2026-09-25 — Elisabet Soto · C1 S5 cumpleaños, ronda 4 (4 vueltas, aprobada)
- nuevo **R-37** foto = reemplazar el fondo · **R-38** íconos Phosphor en cuadro transparente con borde blanco · **R-39** números en cuadro fucsia + fila de íconos · **R-40** cierre de feed en línea, sin botón · **R-41** personas generadas con look de fotógrafo de eventos · **R-42** foto DoubleTree de la sesión SEP 2026, con ventana, cama y desayuno.
- ✔ subieron: R-09 (×2), R-15 (×2, upscaler en vez de ampliar), R-17 (×2, cajas de recorte en la cabecera), R-31 (×5), R-32 (×4).
- ⚠️ R-03 revisada: el fucsia entra como cuadro de los números por pedido de Eli.
- nuevo **A-06**; rechazos **X-10…X-14**.
- Fuera de alcance: nada de esto se copió a DT, QB ni Between. Candidata a regla del estudio (para Valeria): «los íconos salen de un set profesional, nunca dibujados a mano».

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-36** · destilados de `CLAUDE.md` (22-09), `reglas.yaml` v5, `marca.json` y 12 entradas de bitácora (16 al 22-09).
- nuevo **E-01…E-05**, **A-01…A-05**, **X-01…X-09** · sacados de las rondas 2–7 de la S4, la S5 y el reel Jazz.
- ✔×N contados sobre la bitácora: R-31 (4 reemplazos con enlace), R-33 (4 comentarios prependidos), R-34 (3 corrimientos de columna).
- Contradicciones anotadas, no resueltas: `marca.json` y `CHECKLIST-CLIENTE.md` todavía dan `ref-cumple` por bloqueada (se resolvió el 22-09); el manual lista 3 formatos y la bitácora del 17-09 ya suma el banner web; `reglas.yaml` fecha la cita «Todo es propio…» el 09-09 en la cabecera y el 15-09 en la regla.
- Fuera de alcance: no se leyó `clients/hilton/`; no hay notas de memoria con piso18/p18 en el nombre.
