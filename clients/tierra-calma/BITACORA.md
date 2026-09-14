# Tierra Calma — bitácora

> Una entrada por jornada, la más nueva arriba. Si no está acá, el que retoma
> mañana no lo sabe.

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
