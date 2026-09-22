# PISO 18 Centro de Eventos — manual de marca

> Abierto el **22-09-2026** por instrucción de Eli: *«piso18 o p18 debo abrirlo igual
> por separado que cada marca»*.
>
> ⭐ **Lo que faltaba NO era el sistema: era este manual.** Piso 18 ya tenía kit de
> código medido (`src/brand/piso18.ts`, 425 líneas, 15-09-2026), reglas ejecutables
> calibradas en modo control (`reglas.yaml` v3) y seis composiciones. Lo que no
> existía era la capa legible y la ficha `marca.json`. Este documento **sintetiza** lo
> que ya estaba medido; no lo reemplaza. **Ante cualquier duda de un número manda el
> kit de código**, que dice de dónde sale cada uno.

## ⛔ Piso 18 es marca propia

Comparte edificio con DoubleTree, **no sistema gráfico**. Palabras de Eli:
*«Todo es propio y diferente a DT, recuerda no mezclar las marcas.»* Nada de DT entra
—ni tipografía, ni paleta, ni logo, ni banco, ni «LA LEY DE ELI», que se dictó para
DT— y nada de acá va para allá.

⛔ **El caso que lo demuestra:** «bodas» está **prohibido** en Piso 18 y es
**obligatorio** en DoubleTree, donde `Noche de Bodas` es el nombre propio de un
programa del hotel. La misma palabra, veredicto opuesto según la marca.

⛔ Y el fucsia de acá **no** es el de Selfie (`#FF007C`).

## La regla madre

> **La foto del evento manda y ocupa todo; el texto vive sobre un velo oscuro; y el
> fucsia se reserva para lo único que se quiere que el ojo pegue.**

En las 7 piezas aprobadas el fucsia **nunca decora**: es la caja del precio, el filete
del recuadro, el `piso18.cl` del CTA, el destacado dentro de un titular y los botones.
Si en una pieza nueva aparece en algo que no es la oferta, está mal usado.

## Paleta — dictada por Eli el 15-09, verificada midiendo

| Rol | Hex | Para qué |
|---|---|---|
| **Fucsia Piso18** | `#D4145A` | La firma. Caja del precio, filete, `piso18.cl`, destacado del titular, botones |
| Blanco | `#FFFFFF` | Tinta sobre foto: logotipo, titulares y cifras |
| Tinta | `#1A1A1A` | Sobre la tarjeta blanca del cierre de carrusel |
| Tarjeta | `#F7F5F2` | El papel de la tarjeta festoneada |
| Beige | `#EFE6D9` | Fondo de soporte, pedido por Eli en la ronda 2 de la S4 |
| Beige hondo | `#E6DACA` | La banda que cruza el tercio alto |

⚠️ **El fucsia lo fijó Eli, no la medición.** Sobre los JPG aprobados se lee `#D6145B`
y `#D5135A` — a 2 de distancia, que es ruido de compresión. **La medición verifica,
nunca fija.**

⚠️ El beige **no** es la tarjeta: `#F7F5F2` es casi blanco (luminancia 242) y sobre él
«beige» no se lee como beige. La ronda 2 de la S4 salió así y hubo que corregirla.

## Tipografías — ✅ resueltas y rindiendo

| Familia | Para qué | Estado |
|---|---|---|
| **IvyPresto Headline** | La principal. Titulares y destacados, **poco** | ✅ 20 cortes en `public/assets/fonts/piso18/ivypresto/` |
| **IvyPresto Display** | Bajadas serif | ✅ |
| **Raleway** | El caballo de batalla: párrafos, cifras, CTA, legal | ✅ libre en el repo |
| **Against** | Alterna de Ivy, cuando Ivy se usa mucho | ⚠️ 232 glifos, **sin `¿` ni `¡`** |

⭐ **IvyPresto es de Adobe Fonts y aun así rinde.** `scripts/p18-ivypresto-link.py`
copia los cortes desde Creative Cloud buscándolos por nombre interno. En una máquina
nueva hay que correrlo de nuevo.

⚠️ Son `.otf` **CFF** — el formato que Chrome rechazó en silencio con Brushwell y por
el que se rindieron 27 piezas de Between con una serif de reemplazo. Acá **sí** cargan
(probado en headless el 15-09), pero **se verifica en cada render** con
`p18FuentesListas()`. Nunca se da por hecho.

⛔ **«¿Te casas en verano?» NO se compone en Against**: no trae `¿`, Chrome sustituye el
signo con otra fuente y se nota.

⛔⛔ **Las cifras no se alinean con CSS.** Ningún Raleway del estudio declara `tnum`:
Chrome ignora `tabular-nums` **en silencio**. El `1` mide 0,450 em y el `0` 0,614 — un
36 % más angosto, y eso descuadra `$4.500.000` contra `$6.000.000`, que es justo la
comparación que hacen las promos. Se alinea **por código**, con cada dígito en una caja
al **máximo** de la fila (`P18.cifras.anchoDigitoMax`), nunca al promedio.

## Formatos y geometría — medidos, normalizados a 1080 de ancho

| Formato | Entrega | Ratio |
|---|---|---|
| Feed / carrusel | **2250 × 2813** | 4:5 |
| Historia | **2250 × 4000** | 9:16 |
| Promo cuadrada | 1080 × 1080 | 1:1 |

⭐ **El máster es 2250, y eso corrige la lectura del `.ai`**: la mesa de los editables
es 1080 × 1350, pero lo aprobado y publicado va a 2250 de ancho (×2,0833).

### El logotipo

✅ **Está limpio y listo**: `public/assets/piso18/logo-piso18-completo.png` (566 × 228),
recortado por alfa y recompuesto por luminancia.

| | Ancho @1080 | Tope y |
|---|---|---|
| Historia | 272,2 | 206,9 |
| Feed | ~275 | 105,1 |

⭐ **Mide lo mismo en historia y en carrusel** (225,6 la línea `CENTRO DE EVENTOS` en
las dos). Va arriba y centrado. ⛔ **Nunca se deforma:** escala uniforme desde su
proporción real (2,4825).

⚠️ **La trampa:** el `logo PISO18.png` del material de origen **no es un logotipo** —
es una plantilla de historia 2250×4000 con un velo negro en degradado que ocupa el
99,4 % de sus píxeles con alfa. El velo es **intencional y parte del sistema**: es lo
que hace legible el titular sobre la foto. Pero quien lo monte creyendo que es un logo
le pega encima un velo a una pieza que quizá no lo quería.

### El titular va prácticamente a sangre

Medido en `ST N°1 S1`: la línea «ESTA ES TU OPORTUNIDAD» ocupa **1021,9 de 1080** y
deja 29 px de margen. Por eso el check de respiro de borde está calibrado a 26 px y no
a los 60 de agencia: **con el tope de agencia, la pieza que el cliente firmó salía
rechazada.**

## Gramática — dos registros, y no se mezclan

| Registro | Cómo se ve | Piezas |
|---|---|---|
| **Promo / precio** | Foto oscurecida, titular, **caja fucsia maciza** con la cifra, legal chico al pie | `ST N°1 S1`, `Post Matrimonio 1.1`, `Post cumpleaños 1.1`, `C1 S4 N°2` |
| **Editorial / invitación** | **Tarjeta blanca festoneada** centrada, serif itálica, dominio chico abajo. Sin caja y sin cifra | `C2 S1 n°2` |

**El titular alterna itálica fina y versales**, en la misma familia — es lo más
reconocible de la marca:

- *¿Te casas en verano?* → **ESTA ES TU OPORTUNIDAD**
- *¿QUÉ INCLUYEN* → **LOS CUMPLEAÑOS** → *EN PISO18?*

**El bloque de precio:** `ANTES` chico sobre la cifra tachada, `AHORA` sobre la cifra
nueva en caja fucsia. Cifras en serif. En descuento, el porcentaje gigante (`50%`,
`30%`) con `DCTO.` chico al costado.

**El cierre:** `Cotiza en` blanco + `piso18.cl` en caja fucsia · `Av. Vitacura 2727,
Las Condes` centrada · legal al pie, cuerpo mínimo, con asterisco.

## Los botones — dictado de Eli, 15-09

*«Siempre hay que hacer botones en las historias, y en algunos reels.»* Redirigir a
cotizar es el objetivo comercial de la cuenta.

⛔ **Dos esquemas y no hay un tercero.** Ni otro color, ni degradado, ni transparente
sobre la foto.

| | Fondo | Texto |
|---|---|---|
| Lleno | `#D4145A` | `#FFFFFF` |
| Invertido | `#FFFFFF` | `#D4145A` |

⚠️ **La interacción no se dibuja**: se deja el aire y el sticker real lo pone el CM.
Y si la historia es **animada**, la posición y el contraste del botón se miden en el
**último fotograma**.

## Reglas duras

1. **Sin bodas.** Nunca se escribe. Es la única excepción a que los textos vayan
   literales del brief: se reemplaza por matrimonio(s) o novios. Ratificada por
   escrito por el cliente el 17-09 (`FEED!I14`).
2. **El brief es de contenido, no de diseño.** La grilla la dejan Carlos Figueroa y
   Scarlette Muñoz. Un «Este no va» del cliente **no se le lleva a Eli** — extendido a
   Piso 18 por ella el 22-09-2026.
3. **Todo fondo oscuro plano lleva grano** (`GranoFondo`). Sin él dos filas contiguas
   son idénticas y el check de foto estirada bloquea la pieza — y además se ve mejor:
   la referencia que dio Eli no tiene un negro digital de fondo, tiene un cuero.
4. **La foto se PRODUCE, no se recorta.** El banco es 3:2 horizontal y el feed pide 4:5.
5. **El logotipo nunca se deforma.**
6. De la carpeta `14jOWfpSm7Nm1lXAABZNThZAa5_5BulzC` **no se usan fotos de 2020 hacia
   abajo** (orden de Eli), filtrando por fecha de captura **EXIF**, no la de Drive.

## Imagen

⭐ **Generar con IA ya es parte de la gramática**, no un atajo: los editables de mayo,
junio y agosto traen `magnific_*.png` y `freepik__*.png` montados.

⚠️ **El banco real vive en el disco externo `F:`**, no en Drive. Lo que hay en el repo
es una muestra. Las rutas están en `marca.json`.

## Video — los reels se editan sobre el draft de CapCut

Eli monta los reels de Piso 18 en **CapCut Desktop**, y sus proyectos se pueden
reescribir desde código: `draft_content.json` es JSON plano. El método y las
cuatro trampas están en la memoria `capcut-draft-se-edita-desde-codigo`.

⛔⛔ **CapCut abierto pisa todo lo que escribas.** Carga el proyecto al abrirlo y
guarda su copia en memoria al salir. El 22-09 se perdió así una corrección
completa. Antes de tocar el draft: `tasklist | grep CapCut` tiene que dar **0**.
Reemplazar un **archivo de video** sí es seguro con CapCut abierto — sólo hay que
cerrar y reabrir el proyecto para que lo recargue.

⛔ **Y Eli edita encima.** Fusiona tramos en *Clip combinado*, mueve puntos de
entrada. Antes de escribir se relee el draft y se respalda el suyo; lo que no
pidió, no se toca.

### ⭐⭐ La corrección de color que se nota, está mal

Criterio de Eli, 22-09-2026, sobre la terraza del reel S4: *«se ve muy mal, se ve
extraño y oscuro… hazlo sutil como para que no se note».*

**Una pieza «quemada» casi nunca está sobreexpuesta.** Acá el material tenía p99
= 239 y **0,00 % de píxeles en 254**: nada recortado. Lo que había era **velo
atmosférico** de rodar a contraluz. Se diagnostica midiendo cuatro cosas, no
mirando:

| Qué | Cómo se lee |
|---|---|
| **Punto de negro** (p0.5) | si está por sobre ~25, hay velo |
| **Dominante** (R−B por zonas) | pareja en sombras, medios y altas = velo, no luz |
| **Micro contraste** (varianza del laplaciano) | contra la **mediana del propio reel** |
| **Recorte** (% ≥ 254) | si es ~0, no hay nada quemado que recuperar |

**Y la vara de que la corrección es correcta es que la exposición NO se mueva.**
Se mide antes y después:

- **la piel** (máscara YCrCb) no baja más de ~2 puntos — es lo que delata el
  exceso: la versión rechazada la llevaba de 135,0 a 122,6;
- **las sombras** (el 25 % más oscuro) no se desploman — la rechazada, de 65 a 35,7;
- la **mediana** y el **p99** quedan casi iguales (144,3→143,7 y 238,3→238,7);
- el **recorte se mantiene en 0,00 %**.

Lo único que sí cambia: el punto de negro baja (28,9→11,7), la dominante se parte
por dos (−7,0→−3,1) y el micro contraste se duplica (762→1.549).

⚠️ **Los deslizadores de CapCut no sirven para esto.** Su contraste pivotea en el
50 % (127 de 255) y la mediana de un plano a contraluz está en 144: subir
contraste lo empuja **más arriba**. Por eso la corrección se **hornea** con ffmpeg
(`scripts/p18-reel-jazz-grade-terraza.py`), con **rodilla `tanh`** al final para
comprimir las altas en vez de recortarlas, y los deslizadores del clip se dejan
**en cero** para no corregir dos veces.

⭐ **Antes de rescatar una toma, mídela contra las otras del reel.** La que abre
el montaje de flores parecía candidata a arreglo y resultó ser de las mejores del
material: nitidez 7.652 contra una mediana de 3.782. No necesitaba nada.

### El audio de un reel

El ducking **se mide, no se hace a ojo**: se extrae la locución con ffmpeg, se
arma la envolvente RMS en ventanas de 50 ms sobre la línea de tiempo y el umbral
sale del percentil 15 del piso de ruido + 9 dB. La música **sólo sube en los
silencios largos (≥1,3 s)** — levantarla en cada pausa de 0,8 s suena a bombeo.
Los keyframes de volumen de CapCut llevan `time_offset` en tiempo de **fuente**.

⚠️ **La música comercial es exposición de marca.** El reel de la S4 va con el
instrumental de *Flowers* de Miley Cyrus. Se avisó; la decisión es de Valeria.

## QA

```bash
python qa/motor.py --marca piso18 <piezas>
```

Las reglas están **calibradas en modo control contra las piezas aprobadas**, con el
número y su porqué escritos en `reglas.yaml`. ⛔ **`foto-estirada` no se calibra**: se
arregla la pieza, no la regla.

## Lo que falta

Ver [`CHECKLIST-CLIENTE.md`](CHECKLIST-CLIENTE.md). Lo principal: la muestra medida es
de **7 piezas** cuando el método pide 20–60, `raw/hilton/piso18/ref-eli-sep2026/` está
vacía, y las 11 referencias de `ref-cumple` siguen sin bajarse — ver
[`REFERENCIAS-CUMPLE.md`](REFERENCIAS-CUMPLE.md).
