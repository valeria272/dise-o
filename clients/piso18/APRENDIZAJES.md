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
> Criterio: **Elisabet Soto «Eli»** · Aprueba: **el cliente Hilton, por comentarios en la grilla (contenido: Carlos Figueroa y Scarlette Muñoz)**
> Última cosecha: **2026-09-25** · Cosechas: **1**

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
| Por dónde llega el feedback | Comentarios en celda de la grilla (hojas FEED · STORIES · ORGÁNICO), **prependidos** sobre el anterior; encargo directo de Eli |
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

- **R-01** · «bodas» no se escribe nunca: va matrimonio(s) o novios, aunque el brief o el hashtag lo traigan — _Eli, 15-09-2026; ratificada por el cliente en `FEED!I14` el 17-09 («no usemos la palabra BODA»)_ · ✔×2
- **R-02** · Nada de DoubleTree entra en Piso 18 (ni tipografía, ni paleta, ni logo, ni «LA LEY DE ELI»), y nada de acá va para allá — _Eli: «Todo es propio y diferente a DT, recuerda no mezclar las marcas»; reglas.yaml_ · ✔×1
- **R-03** · El fucsia nunca decora: sólo caja del precio, filete, `piso18.cl` del CTA, destacado del titular y botones — _medido en las 7 aprobadas; manual 22-09_ · ✔×1
- **R-04** · El fucsia de Selfie (`#FF007C`) no entra: el QA lo corta a ΔE 12 — _Eli, 15-09; reglas.yaml `fucsia-de-selfie`_ · ✔×1
- **R-05** · El beige `#EFE6D9` no se pone sobre la tarjeta `#F7F5F2`: ahí no se lee como beige — _Eli, ronda 2 S4_ · ✔×1
- **R-06** · El titular alterna una línea en itálica fina y otra en VERSALES, en la misma familia — _medido en las 7 aprobadas, 22-09_ · ✔×1
- **R-07** · Dos registros que no se mezclan: promo (foto oscurecida + caja fucsia con la cifra) y editorial (tarjeta blanca festoneada, sin caja ni cifra) — _manual 22-09, sobre `ST N°1 S1` y `C2 S1 n°2`_ · ✔×1
- **R-08** · Bloque de precio: `ANTES` chico sobre la cifra tachada, `AHORA` sobre la cifra nueva en caja fucsia, cifras en serif; en descuento, el % gigante con `DCTO.` al costado — _manual 22-09_ · ✔×1
- **R-09** · Cierre: `Cotiza en` blanco + `piso18.cl` en caja fucsia · `Av. Vitacura 2727, Las Condes` centrada · legal al pie con asterisco — _manual 22-09_ · ✔×1
- **R-10** · Siempre hay botón en las historias (y en algunos reels), sólo en dos esquemas: fucsia/blanco o blanco/fucsia — _Eli, 15-09: «Siempre hay que hacer botones en las historias»_ · ✔×1
- **R-11** · La interacción no se dibuja: se deja el aire y el sticker real lo pone el CM — _manual; marca.json `botones`_ · ✔×1
- **R-12** · El logotipo va arriba y centrado, tope y≈207 @1080 en historia y ≈105 en feed, y nunca se deforma — _kit 15-09; manual_ · ✔×1
- **R-13** · `logo PISO18.png` no es un logo: es una plantilla de historia con velo negro en degradado. Mide el alfa antes de montar — _manual 22-09_ · ✔×1
- **R-14** · La portada de carrusel lleva el velo de marca (alfa 0,588 arriba → 0 al 41,7 % del alto) **debajo** del logotipo; se rehace desde la foto limpia — _Eli, 16-09, S4 ronda 5: «Oscurece un poco arriba con una transparencia muy sutil»_ · ✔×1
- **R-15** · El zoom de una foto tiene tope 1,0: un recorte que ampliaría se rechaza y se busca otro plano en el banco — _Eli, 16-09, G3 S4: «No tiene que verse en los costados ni la mesa»_ · ✔×1
- **R-16** · Si Eli manda una captura con el encuadre, el recorte se deduce midiendo tres puntos comunes, no a ojo — _S4 ronda 5, 16-09_ · ✔×1
- **R-17** · La caja de recorte de cada pieza queda escrita en el script que la produce — _S4, 16-09: dos recortes hubo que reconstruirlos por correlación_ · ✔×1
- **R-18** · Todo fondo oscuro plano lleva grano (`GranoFondo`); `foto-estirada` no se calibra, se arregla la pieza — _S5, 15-09; referencia de Eli «tiene un cuero», no negro digital_ · ✔×1
- **R-19** · Las cifras no se alinean con CSS (Raleway no trae `tnum`): cada dígito en una caja al **máximo** de la fila — _kit 15-09; `$4.500.000` vs `$6.000.000`_ · ✔×1
- **R-20** · Un titular que empieza con `¿` o `¡` no se compone en Against — _manual; «¿Te casas en verano?»_ · ✔×1
- **R-21** · IvyPresto (OTF CFF) se verifica en cada render con `p18FuentesListas()`; nunca se da por cargada — _manual; precedente Brushwell_ · ✔×1
- **R-22** · De la carpeta `14jOWfpSm7Nm1lXAABZNThZAa5_5BulzC` no se usan fotos de 2020 hacia abajo, por fecha EXIF de captura — _orden de Eli, manual_ · ✔×1
- **R-23** · El brief es de contenido, no de diseño: un «Este no va» del cliente **no se le lleva a Eli** — _Eli, 22-09: «no tomes eso de ese no va ya que es para contenido no yo»_ · ✔×1
- **R-24** · Ni títulos ni bajadas llevan punto (final ni intermedio), aunque el brief lo traiga — _regla del cliente Hilton, 23-09-2026, citada en el manual de Piso 18_ · ✔×1
- **R-25** · La corrección de color que se nota está mal: la piel no baja más de ~2 puntos, las sombras no se desploman, recorte en 0,00 % — _Eli, 22-09, terraza del reel S4: «hazlo sutil como para que no se note»_ · ✔×1
- **R-26** · «Quemado» casi nunca es sobreexposición: se diagnostica midiendo punto de negro, dominante, micro contraste y recorte, y se hornea con ffmpeg (los deslizadores de CapCut quedan en cero) — _reel S4, 6ª sesión 22-09_ · ✔×1
- **R-27** · Antes de tocar un draft de CapCut, CapCut cerrado (0 procesos); se relee y respalda el draft, y lo que Eli editó encima no se toca — _22-09: se perdió una corrección y hubo que reconectar el clip tres veces_ · ✔×2
- **R-28** · En la historia animada (Remotion) los planos se escriben del primero al último para que el que entra quede arriba, con curva simétrica — _reclamo del cliente 22-09: «se queda pegada a la mitad»_ · ✔×1
- **R-29** · Una transición se mide en secuencia PNG en **todas** las transiciones: cero fotogramas congelados dentro del empuje y cero saltos >25 fuera — _S4 ronda 7, 22-09; reglas.yaml v5_ · ✔×1
- **R-30** · En una historia animada, posición y contraste del botón se miden en el último fotograma — _manual; reglas.yaml_ · ✔×1
- **R-31** · Una pieza corregida se reemplaza en Drive **conservando su enlace** — _S4 rondas 4, 5, 6 y 7 (16 al 22-09)_ · ✔×4
- **R-32** · La revisión se publica como página de antes/después; nada interno va a la carpeta de entrega, que ve el cliente (`@hilton.com` con permiso de escritura) — _hallazgo 16-09; rondas 4–7 aprobadas así_ · ✔×3
- **R-33** · Lo nuevo de la grilla se detecta por diff de **conjunto de cadenas** contra la instantánea anterior: el comentario se prepende y no lo delatan ni la celda ni el `modifiedTime` — _confirmado el 16, 17 (×2) y 22-09_ · ✔×4
- **R-34** · Una pieza se identifica por su **título**, nunca por la columna: la grilla corre fechas sin avisar — _16-09 (NOCHE 25→23), 17-09, 22-09 (animada 23→24)_ · ✔×3
- **R-35** · El GIF de una pieza animada va a 25 fps, sin difuminado y a 540×960; lo que se publica en Instagram es el MP4 — _Eli, 22-09: «guárdalo igual en gif»; `scripts/p18-s4-gif.py`_ · ✔×1
- **R-36** · El titular va prácticamente a sangre (29 px de margen @1080): el respiro de borde de la marca es 26 px, no los 60 de agencia — _medido en `ST N°1 S1`; reglas.yaml_ · ✔×1

## 5. Excepciones

- **E-01** · R-01 es la **única** excepción conocida a que los textos en pantalla vayan literales del brief — _reglas.yaml `sin-bodas`_
- **E-02** · El velo de R-14 va sólo en la **portada**: las otras slides no llevan logotipo y el brief las quiere limpias — _Eli, 16-09_
- **E-03** · La zona segura de Meta se relaja en orgánico: el logotipo vive dentro de los 250 px de arriba por sistema y el legal al pie llega al 3 % de tinta — _calibrado sobre `ST N°1 S1`, reglas.yaml_
- **E-04** · Los reels se montan en **CapCut** (Eli); las historias animadas se escriben en **Remotion** (`P18StMontaje.tsx`) — _manual 22-09_
- **E-05** · La S3 de septiembre la hizo Eli a mano: no se toca, y el token del estudio no puede reemplazar sus archivos — _Eli, 16-09: «solo toma s4 ya que yo hice la s3»_

## 6. Lo que se aprueba a la primera

- **A-01** · Cambiar la apertura de la animada por una foto de arreglos que sea **el mismo arreglo del plano 2 visto de lejos** (sin rostros, sin logo de la pared, sin ampliar) — _ST N°3 S4, ronda 6, Eli «Aprobado» 17-09_
- **A-02** · Los planos que no se tocan pasan solos: `C1 S4 N°2`, `C1 S4 N°4` y `ST N°2 S4` quedaron de la ronda 3 sin cambios — _S4, 16-09_
- **A-03** · Encuesta con la opción B cambiada a mesa puesta evitando repetir una foto del feed de 4 días antes (`piso_18-28` y no `piso_18-85`) — _ST N°4 S4, ronda 4, 16-09_
- **A-04** · Post nuevo con la foto que el cliente eligió por nombre + logotipo: «Que sea esta foto, con logo y estamos» — _Post n°2 S4 25-09, ronda 4_
- **A-05** · La selección y el orden de fotos de la animada, y su ritmo (2,2 s por plano, 13 s) — _cliente 22-09: «Está ok la selección de fotos»_

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

## 9. Registro de cosechas

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-36** · destilados de `CLAUDE.md` (22-09), `reglas.yaml` v5, `marca.json` y 12 entradas de bitácora (16 al 22-09).
- nuevo **E-01…E-05**, **A-01…A-05**, **X-01…X-09** · sacados de las rondas 2–7 de la S4, la S5 y el reel Jazz.
- ✔×N contados sobre la bitácora: R-31 (4 reemplazos con enlace), R-33 (4 comentarios prependidos), R-34 (3 corrimientos de columna).
- Contradicciones anotadas, no resueltas: `marca.json` y `CHECKLIST-CLIENTE.md` todavía dan `ref-cumple` por bloqueada (se resolvió el 22-09); el manual lista 3 formatos y la bitácora del 17-09 ya suma el banner web; `reglas.yaml` fecha la cita «Todo es propio…» el 09-09 en la cabecera y el 15-09 en la regla.
- Fuera de alcance: no se leyó `clients/hilton/`; no hay notas de memoria con piso18/p18 en el nombre.
