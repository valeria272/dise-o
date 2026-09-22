# Tierra Calma — bitácora

> Una entrada por jornada, la más nueva arriba. Si no está acá, el que retoma
> mañana no lo sabe.

---

## 2026-09-22 (tarde) — Diego Aguilar

**Qué se hizo:** Se rehízo **la grilla de octubre completa, las 10 piezas (18
archivos)**, porque el cliente la reescribió casi entera ese mismo día a las
16:12Z. Y se corrigió el error de fondo que arrastraban las entregas
anteriores: **las imágenes no se parecían al lugar**.

**⭐ El hallazgo del día: el ADN de imagen estaba mal.** Diego subió a
`APRENDIZAJE IA — NO PUBLICAR/IMAGENES/` el material real —40 fotos de terreno
del 27-04 y las 44 aéreas del dron del 07-08 en 21 MP— y al medirlas quedó
claro que Tierra Calma es **ladera de cerro árida**: cerros ocre pelados,
matorral espinoso ralo, **caminos de ripio anaranjado en curva**, postes de luz,
cercos de madera oscura, palmeras y el valle abajo. Lo entregado el 14-09 eran
praderas verdes con cordillera nevada: otro país. El ADN corregido quedó escrito
en `CLAUDE.md` § 4 bis con la tabla de lo que sí y lo que nunca más.

**Consecuencia práctica:** el **reel del 13/10 ya no es IA**. Sus 6 cortes salen
de las **aéreas REALES** recortadas a 9:16, gradeadas y animadas con Kling 3.0.
El sitio que se ve es el sitio.

**Lo que cambió la grilla del 22-09 16:12Z:**

| Pieza | Antes | Ahora |
|---|---|---|
| 13/10 reel | 4 cortes | **6 cortes** con estructura nueva |
| 20/10 | post estático | **carrusel de 6 slides** |
| 01/10 reel | subtítulos libres | la grilla **dicta** los 3 subtítulos |
| 06/10 carrusel | afirmaciones | preguntas en primera persona |
| 08/10 story | pétalos, sin copy | pieza comercial con bloque de valor |
| 09/10 | post de paisaje | pareja de espaldas + **globos de conversación** |
| 12/10 story | WhatsApp | **mapa azul** Santiago → Padre Hurtado |
| 15/10 story | POV en auto | **interfaz de buscador** glassmorphism |
| 29/10 post | hora azul | **cocina con polaroid y post-it** |

**Dónde quedó:** 18 archivos subidos a la carpeta de entrega, con la
nomenclatura del equipo. Los que ya existían se reemplazaron **sobre el mismo
ID**, así que los enlaces compartidos siguen sirviendo. En el repo,
`OctubreV3.tsx` (12 estáticas) y `OctubreVideoV3.tsx` (los 2 reels); las
primitivas de video se exportaron desde `OctubreVideo.tsx` para no duplicarlas.
Clips, audio y fondos versionados.

Cadena de modelos: **Seedream 5 Pro → Kling 3.0 → ElevenLabs Music v2**,
locución con Antonia Reyes (voz chilena). Ambos reels cierran con
`tc_cierre.mp4`, el cierre oficial que subió Diego ese día.

**Qué sigue:** Esperar la ronda del cliente. Las 10 piezas siguen «En revisión».

**Abierto:**

1. ⚠️ **«Rol individual» y «Acceso controlado» salieron publicados sin
   confirmación escrita.** Están en el corte 4 del reel del 13/10 y en el slide
   4 del carrusel del 20/10. No están en la lista blanca del manual y **la
   propia nota de datos comerciales de la grilla tampoco los incluye** — la
   grilla se contradice a sí misma. Entraron con el OK verbal de Diego el 22-09.
   **Falta el OK de Fran o Blanca.** Es el mismo patrón que dejó «conexión a
   agua potable» publicada en septiembre.
2. **Tres archivos obsoletos siguen en la carpeta de Drive** porque el cliente
   cambió el formato de esos días y no se borran sin permiso:
   `st-08-10.mp4` y `st-15-10.mp4` (esos días ahora son estáticos, ya está el
   `.png`) y `p-20-10.png` (el 20/10 ahora es el carrusel `c-20-10-1..6`).
   Si quedan, el CM puede publicar la versión vieja.
3. Sigue abierto el **mapa oficial** con Carlos: los PNG de `MAPAS` traen
   topónimos corruptos, por eso el mapa del 12/10 se dibujó en SVG desde cero.
4. La marca sigue sin `reglas.yaml`: el QA de las 18 piezas fue a mano.

---

## 2026-09-22 — Diego Aguilar

**Qué se hizo:** Se re-hizo **solo el reel `r-13-10`** con otra cadena de
modelos: imágenes con **Seedream 5 Pro** (9:16, 2k → 1440×2560), video con
**Kling 3.0** (9:16, 1080p, fotograma de inicio) y música con **ElevenLabs
Music v2** (instrumental, 26 s, tranquila pero con arco para que venda). Y el
reel ahora **cierra con el logo animado**, no con el wordmark.

**⚠️ Lo importante del día:** el `/al-dia` encontró que **la grilla se modificó
hoy a las 15:43Z** y que el cliente cambió los textos. En el `r-13-10` los
mensajes del corte 1 y del corte 2 **se intercambiaron** y el del corte 4 se
alargó. La versión entregada el 14-09 tenía los textos viejos. Si se producía
sin revisar, se entregaba obsoleto.

| Corte | 14-09 (v1) | 22-09 (vigente) |
|---|---|---|
| 1 | A 15 min del peaje Padre Hurtado. | Así se ve el camino hasta Tierra Calma. |
| 2 | Escríbenos y coordina tu visita. | A 15 minutos del peaje Padre Hurtado. |
| 3 | Tamaño real ~5.000 m² aprox. Desde UF 2.500. | ~5.000 m² aprox., desde UF 2.500. |
| 4 | Agenda tu visita. | Agenda tu visita y compruébalo en terreno. |

**Dónde quedó:** `r-13-10.mp4` (23,5 s) **reemplazado en Drive sobre el mismo
ID**, así que los enlaces ya compartidos siguen sirviendo. En el repo,
`ReelDronOctV2` en `OctubreVideo.tsx` (la v1 se deja al lado, marcada como
superada, para poder comparar). Clips `k1..k4` y `mus_dron_v2.mp3` versionados.

**Qué sigue:** Las **otras tres piezas de video** (`r-01-10`, `st-08-10`,
`st-15-10`) tienen dos cosas pendientes: cierran con el wordmark en vez del
logo animado, y sus textos también cambiaron en esta ronda. Hay que rehacerlas
igual que ésta.

**Abierto:**

1. **La ronda del 22-09 tocó más piezas y ninguna está corregida todavía:**
   - **D (01/10):** la grilla ahora **dicta los subtítulos exactos** — «La
     primavera ya llegó a Tierra Calma» / «Más verde, más luz, más espacio» /
     «Así se siente el cambio de estación acá».
   - **E (carrusel):** los textos pasaron a preguntas en primera persona
     («¿Tengo que invertir en la electrificación del terreno? No, …») y cambió
     el CTA del slide 4.
   - **F (08/10):** ⚠️ **ya no es «sin texto ni CTA»** — ahora lleva «Este es el
     momento del año en que Tierra Calma se ve así.» + CTA de WhatsApp.
2. **Cero comentarios en Drive.** La ronda entró **por la grilla**, no por
   comentarios — igual que pasa con Between. Revisar siempre la grilla.
3. Siguen abiertos de la jornada anterior: el **mapa oficial** con Carlos, avisar
   lo del **agua potable** publicado en `st-11-09`, y que la marca no tiene
   `reglas.yaml`.

---

## 2026-09-14 — Diego Aguilar

**Qué se hizo:** Se abrió y se cerró octubre completo: **las 10 piezas de la
grilla, en 13 archivos**, entregadas y subidas a Drive. Primero las 9 estáticas
(carrusel de 4 del 06-10, posts del 09, 20 y 29, stories del 12 y 22) y después
las 4 de video (reels del 01 y 13, stories del 08 y 15). Lo que cambió el
sistema es que **el marco dejó de dibujarse en código**: el 14-09 aparecieron en
Drive los PNG con alfa (`MARCOS PUBLICACIONES`) que ya traen dentro el logo y el
contorno de la píldora, así que ahora se miden y se rellenan. La geometría quedó
escrita en `CLAUDE.md` § 4 quinquies. Para los videos se siguió el pipeline que
pidió Diego: **imagen clave con Magnific según el brief de cada corte → video
desde esa misma imagen** (Kling 2.5, 9:16, 1080p, fotograma de inicio) →
normalizar a 30 fps.

**Dónde quedó:** Todo entregado en la carpeta de Drive `1lJG3Xzwh77zSCSDQ4DiPsAJK0fAqcNwF`
(la misma del `Temas_Octubre_2026.docx`), con la nomenclatura de septiembre:
`c-06-10-1..4`, `p-09-10`, `p-20-10`, `p-29-10`, `st-12-10`, `st-22-10`,
`r-01-10.mp4`, `r-13-10.mp4`, `st-08-10.mp4`, `st-15-10.mp4`.

En el repo: `src/compositions/tierracalma/Octubre.tsx` (estáticas) y
`OctubreVideo.tsx` (video), registradas en `Root.tsx` como `TCOct*`. Los marcos,
los fondos, los 10 clips, la música, la locución y `tc_motion.mp4` están
**versionados** — el mes se reproduce byte a byte. Renders en
`out/tierracalma/oct2026/entrega/`.

Decisiones de dirección tomadas mirando el trabajo publicado, no inventadas:

- **Los reels no llevan marco.** Se sacaron fotogramas de `r-17-09.mp4` (el reel
  de septiembre del propio Diego, disco KINGSTON): clip a sangre, texto blanco
  centrado con halo, Inter Tight Light + IvyOra cursiva, y cierre con el wordmark
  en cursiva más "AGENDA TU VISITA" en versales espaciadas. Las stories **sí**
  llevan marco.
- **El carrusel es un solo objeto**: los 4 slides no son intercambiables porque
  el filete se corre entre ellos. Verificado montando la tira de los 4.
- **La locución se generó línea por línea** (voz chilena *Antonia Reyes*): en una
  sola toma duraba 11,2 s y sus pausas no calzaban con los cortes, así que los
  subtítulos habrían ido descuadrados.
- **Música**: las dos pistas Magnific del reel de junio, rescatadas del KINGSTON,
  una por reel — el mes no puede sonar repetido.

**Qué sigue:** Esperar la ronda del cliente sobre la grilla de octubre (las 10
piezas figuran **«En revisión»**, ninguna aprobada todavía). Cuando llegue,
corregir sobre las composiciones, que ya están parametrizadas.

**Abierto:**

1. ⚠️ **El mapa oficial, con Carlos.** `MAPA-1.png` y `MAPA-2.png` **no son
   cartografía real**: traen topónimos corruptos («Pintnia Asdo», «San Jocé»,
   «Lono a Pénhilla», «Av. Vicuiia Mackenna») y escudos de ruta **G-68, 76, 73**
   alrededor de Padre Hurtado — justo el error de la Ruta 68 que el manual
   persigue hace meses. En `p-20-10` se usaron como **textura** (duotono navy,
   desenfoque 2,6 px, velo 0,72) con rótulos propios encima. Es un parche: el
   mapa oficial sigue siendo el pendiente #4 de Carlos.
2. ⚠️ **Avisar lo del agua potable.** El brief de octubre ratifica que «conexión
   a agua potable» es **falso** (es noria del propietario)… y ese dato **salió
   publicado** en la story `st-11-09` de septiembre, en la tarjeta «Tu parcela
   incluye:». Conviene avisarlo antes de que lo note el cliente.
3. **Decidir el cierre de los reels.** El manual dice que `tc_motion` es «el
   cierre obligatorio de todo reel», pero el reel publicado de septiembre cierra
   con el wordmark. Se siguió la pieza publicada. `tc_motion.mp4` quedó convertido
   y versionado: cambiarlo son cinco minutos si Valeria prefiere el logo animado.
4. **Tierra Calma sigue sin `clients/tierra-calma/reglas.yaml`**, así que
   `python3 qa/motor.py --marca tierracalma` no corre. El QA de las 13 piezas se
   hizo a mano, frame a frame.

**Para quien retome — dos dependencias que NO viajan en el repo:**

- **IvyOra** viene de Adobe Fonts y su carpeta está en `.gitignore` a propósito.
  Hay que tenerla activada y correr `bash scripts/tc-ivyora-link.sh`. **Verificar
  en el render, no en el listado**: si la cursiva se ve como una serif común, no
  cargó.
- **El KINGSTON (`D:`)** tiene los editables: `MARCOS.ai` (en
  `DIEGO 2023/COPYWRITERS/MAS CENTER/IA TIERRA CALMA/`, ojo que está dentro de la
  carpeta de MAS CENTER), `TIERRA SEPT.ai`, las 13 piezas 1x de septiembre, los
  reels publicados y `TIERRA CALMA MOTION.mov`.
- El **ffmpeg que trae Remotion no sirve** para el `.mov` del logo: viene sin
  decoder de qtrle y sin filtros de composición. Se usa el de `imageio-ffmpeg`.
- Los **113 prompts de IA del lugar real** (del espacio Magnific «TIERRA CALMA»)
  quedaron catalogados en [`magnific-prompts.json`](magnific-prompts.json).
