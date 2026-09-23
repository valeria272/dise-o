# Gemela digital de Valeria en HeyGen — cómo clonarla BIEN

> Objetivo: un solo avatar (el que incluye el plan) que sea **exactamente Valeria**:
> su cara, sus dientes, su voz y su forma de moverse. Se hace **una vez** y con material
> grabado a propósito. Un avatar hecho con material a medias se rehace recién el mes
> siguiente (HeyGen permite rehacerlo una vez por ciclo de facturación).

Estado al 03-09-2026 (medido contra la API, no supuesto):

| Qué | Estado |
|---|---|
| Conector MCP | ✅ **conectado y funcionando** (`get_current_user` responde) |
| Plan de la cuenta | ⛔ **free** — y ahí se cae todo, ver abajo |
| Avatares privados | 1 grupo `pedro` (2 looks, `photo_avatar`, del 26-06). Ninguno es Valeria |
| Voces clonadas | ninguna |
| Material de entrenamiento | ✅ **existe** — los masters aparecieron en `~/Downloads` |

**Los dos muros, verificados con la llamada real:**

- `create_digital_twin` → `403 forbidden`: *"Avatar creation requires a paid plan."*
- `clone_voice` → `402 plan_upgrade_required`: *"Voice cloning is not available on the free tier."*

No es problema de material ni de formato: **el plan gratis no deja crear avatares ni clonar
voz por API**. Hay que subir de plan antes de volver a intentar.

**Lo que ya quedó listo y subido** (assets vivos en HeyGen, no hay que rehacerlos):

| Qué | Asset ID | Local |
|---|---|---|
| Metraje 4K vertical 2160×3840, 62 s | `374b03f321ae4de69eb1cb20e2032849` | `raw/valeria/2026-09-heygen/entrenamiento_4k_2160x3840.mp4` |
| Voz, 116 s mono 44,1 kHz | `2f865e7b7f5542e18588333fd2e934ec` | `raw/valeria/2026-09-heygen/voz_116s.mp3` |

⚠️ **Dos trampas medidas el 03-09:**

1. **Los masters vienen rotados 90° sin metadata de rotación.** `019Z8029.MOV` y `019Z8028.MOV`
   son 4096×2160 MJPEG, pero el pixel está acostado. Se enderezan con `transpose=2` (antihorario);
   `transpose=1` los deja de cabeza. Sin eso, HeyGen entrena un avatar acostado.
2. **El tope de subida de assets es 200 MB.** El master pesa 3,5 GB y videotoolbox a 40 Mbps
   deja 293 MB — también rebota. Lo que pasa: `libx264 -preset fast -crf 21 -maxrate 22M` → 112 MB
   con calidad de sobra.

⚠️ **Y falta metraje:** los dos masters duran 62 s y 54 s. HeyGen pide **mínimo 2 minutos
sin cortes** para el Digital Twin, y las tomas no se pueden unir. Aunque se pague el plan,
lo más probable es que 62 s se rechace. Para la voz sí sirve unirlas (116 s, ya hecho).

---

## 1. Por qué ahora sí HeyGen (y qué cambió desde el 20-08)

El 20-08 se descartó HeyGen porque le alargaba los dientes. Ese avatar se hizo con
**una foto** (photo avatar, motor Avatar IV): el modelo inventa toda la boca.

Lo que se hace ahora es distinto: un **Digital Twin de video con Avatar V**. Se entrena con
2 o más minutos de metraje real y usa **el video completo como referencia**, no un solo
frame. HeyGen lo describe como "virtually indistinguishable from the original". Es la
única vía dentro de HeyGen que puede dar "exactamente yo".

La vía de lipsync sobre video real (sync. vía fal.ai, `docs/AVATAR-VALERIA.md`) sigue
siendo válida y no se pisa con esta: HeyGen sirve para guiones nuevos sin rodaje;
el lipsync sirve para doblar un video real ya grabado.

---

## 2. Conectar HeyGen (lo hace Valeria, 3 minutos)

Los conectores de claude.ai se activan en la cuenta de cada persona. No se puede desde
Claude Code.

1. Entrar a **claude.ai** con la cuenta de siempre.
2. `+` → **Connectors** → **Manage connectors** → **Add custom connector**.
3. Nombre: `HeyGen`. URL:
   ```
   https://mcp.heygen.com/mcp/v1/
   ```
4. **Connect** → autorizar con la cuenta de HeyGen (`valeria@copywriters.cl`, conectada el 03-09-2026).
5. Opcional: permisos en **Always allow**.
6. **Abrir un chat nuevo** en Claude Code. Verificar con `ToolSearch "+heygen"`:
   tienen que aparecer herramientas `mcp__heygen__*` (`create_digital_twin`,
   `list_avatar_groups`, `create_video_agent`, `list_voices`, etc.).

No se necesita API key. Los créditos son los del plan de HeyGen.
Si algún día se prefiere API key (para crons sin OAuth), va al llavero cifrado
(`credentials/`), nunca por WhatsApp, y **ojo**: si `HEYGEN_API_KEY` está definida,
los skills ignoran el MCP.

---

## 3. Lo que hay que grabar (tres piezas, una sola sesión)

Todo en la misma sesión, misma luz, misma ropa, mismo fondo. Cámara fija en trípode.
Se graba **en el iPhone o en la cámara de siempre a 4K**, 30 fps o más. El master del
20-08 (`019Z8029.mp4`, 62 s) **ya no está en el disco** y de todos modos era corto:
HeyGen exige mínimo 2 minutos.

### 3.1 Metraje de entrenamiento — 3 minutos seguidos

Este es el que define el avatar. Reglas medidas de la guía de HeyGen:

| Qué | Regla |
|---|---|
| Duración | **Mínimo 2 min sin cortes.** Grabar 3 para tener margen. No editar, no cortar, no unir tomas |
| Resolución | 4K a 30 fps o más (1080p es el mínimo; 4K tarda más en procesar pero da mejor avatar) |
| Encuadre | Medio cuerpo, de frente, de la cintura al aire sobre la cabeza. Cámara a la altura de los ojos |
| Mirada | **A la cámara todo el tiempo.** No mirar al costado ni arriba/abajo |
| Cabeza | Giros de no más de 30° a cada lado |
| Manos | Gestos naturales pero **siempre bajo el pecho**. Nunca frente a la cara |
| Inicio | 2 a 3 s en silencio, boca cerrada en reposo, mirando a cámara |
| Pausas | 1 a 2 s entre frases largas, **con los labios cerrados**. De esas pausas HeyGen saca el "reposo" del avatar |
| Ropa | Lisa, sin logos grandes ni textos ni estampados finos (moiré). Nada que tape el cuello |
| Fondo | Limpio y quieto. Ideal el mismo fondo que después se quiera ver en los videos |
| Luz | Pareja de frente, sin sombras duras ni ventana atrás. Luz de día difusa o softbox |
| Sonido | Pieza silenciosa, sin aire acondicionado ni tráfico. Micrófono de solapa o el iPhone cerca (1 m máximo) |
| Expresión | **Más expresiva de lo que se siente natural**: HeyGen lo pide explícitamente para Avatar V. Sonreír, asentir, cejas |
| Qué decir | Hablar normal, en español, del trabajo: qué es Copywriters, un caso, una opinión. No leer monótono. No reír a carcajadas (deforma la boca en el entrenamiento) |

### 3.2 Video de consentimiento — 20 segundos

Obligatorio. Misma persona, misma sesión. Máximo 30 s. Mirar a cámara y leer
**exactamente** este texto (HeyGen acepta cualquier idioma; el original en inglés es el
que mejor pasa el filtro automático):

> "Hey there! I'm speaking with LOTS of energy, while staying natural and confident.
> This helps HeyGen capture my voice, my expressions, and my motion, so my avatar can
> behave JUST like me in ANY video!"

Si al subirlo HeyGen muestra un código, hay que decirlo alto y claro. Se rechaza si es
grabación de pantalla, si está oscuro o si el audio no se entiende.

### 3.3 Muestra de voz — 3 minutos de audio limpio

El Digital Twin saca la voz del metraje, pero la guía de Avatar V recomienda **una
grabación de voz dedicada** para el clon. Sirve la pista de audio de la sesión si el
micrófono estuvo cerca; si no, grabar aparte con el iPhone a 20 cm en Notas de voz:

- 3 minutos hablando con la energía real de Valeria (no leer plano).
- Sin música, sin eco, sin ruido de fondo. Calidad > duración.
- Una frase con entusiasmo, una seria, una pregunta, un cierre. Variedad de tono.

Con 30 s ya sale un clon instantáneo; con 1 a 3 minutos HeyGen entrena el clon
profesional, que es el que se quiere.

---

## 4. Pipeline cuando esté el conector y el material

Todo va por el MCP, nunca por curl a `api.heygen.com`. Los skills instalados lo
resuelven; este es el orden:

1. Guardar el material en `raw/valeria/2026-09-heygen/` (gitignored):
   `entrenamiento_4k.mp4`, `consentimiento.mp4`, `voz_3min.m4a`.
2. Subir el metraje como asset y crear el avatar:
   `create_digital_twin(name="Valeria", file=<asset>)` → devuelve `group_id`.
   Procesa 10 a 20 min en 1080p, más en 4K.
3. Subir el consentimiento cuando HeyGen lo pida (desde la app web si la cuenta no es
   enterprise; por API solo enterprise).
4. Clonar la voz: `POST /v3/voices` con `voz_3min.m4a` (herramienta `clone_voice` del
   MCP o `heygen voice create`). Guardar `voice_id`.
5. Escribir `AVATAR-VALERIA.md` en la raíz del repo con `group_id`, `voice_id` y las
   secciones Appearance/Voice: es lo que lee `heygen-video` para producir.
6. Activar **Avatar V** en el look (es opt-in por look, no viene por defecto).
7. **Prueba de fidelidad** antes de dar por bueno el avatar: un guion de 30 s en español
   con una frase con muchas "s" y "f" (dientes visibles) y una sonrisa. Exportar y
   comparar contra un frame real del metraje. Mirar dientes, encías, comisuras y el
   borde del pelo. Si los dientes se alargan, el avatar se rehace con más luz frontal y
   más pausas con boca cerrada. Solo hay una repetición al mes: mirar bien.

Costo de referencia: un minuto de video con Avatar IV cuesta 4 USD en 1080p y 5 USD en
4K por API. Avatar V cobra más. El plan gratis tiene 1 slot de avatar y créditos
limitados; para producir de verdad hace falta Creator o superior.

---

## 5. Lo que ya existe y sirve

| Archivo | Para qué |
|---|---|
| `public/assets/valeria/base/voz_base_62s.mp3` | Clon de voz **instantáneo** de prueba mientras no exista la muestra de 3 min |
| `public/assets/valeria/base/base_1080.mp4` (62 s) | Referencia visual para comparar dientes/boca. No sirve para entrenar (corto y 1080p) |
| `raw/valeria/v07*.jpg` | Frames del 18-08. Sirven como foto de respaldo, no para el twin |
| `~/.claude/skills/heygen-skills/` | Skills `heygen-avatar`, `heygen-video`, `heygen-translate` |
| `docs/AVATAR-VALERIA.md` | La vía de lipsync sobre video real (fal.ai). Sigue vigente |

Fuentes: guía de grabación del Digital Twin, video de consentimiento, FAQ de Digital Twin,
guía de Avatar V y referencia de la API, todas en help.heygen.com y developers.heygen.com
(revisadas el 03-09-2026).

---

## 6. La vía gratis que sí funcionó — Higgsfield (03-09-2026)

Con HeyGen bloqueado por plan, la gemela se hizo igual **sin pagar nada nuevo**: Higgsfield
está en plan **Plus con 955 créditos** sin usar. Probado de punta a punta con el material real.

⚠️ **CORRECCIÓN (mismo día).** Primero se dijo que Magnific no servía, tras sondear
`api.freepik.com` y recibir 404 en `/lipsync`, `/avatar` y `/text-to-speech`. **Está mal: el
lipsync de Magnific vive en otro host**, `api.magnific.com`, y es el que resolvió el problema
— ver §7. Las dos APIs no son la misma aunque la cuenta sí lo sea.

⛔ **Y la cara NO se genera.** El §6 completo describe la vía que Valeria **rechazó** el
03-09: `wan2_7` regenera la cara en cada frame y le agrega ojeras, arrugas y dientes de IA.
Sirve la **voz**; para la cara, ir directo al §7.

**La cadena:**

1. `media_upload` (files[]) → `curl PUT` a cada `upload_url` → `media_confirm` por tipo.
2. `create_voice_from_confirmed_audio` con `voz_116s.mp3` → voz clonada al instante.
   **Voz de Valeria: `c9e28ab7-a225-4ce6-8fa4-8371d33b9b36` (`voice_type: element`).**
3. `generate_audio` model `seed_audio` + `voice_type: element` + ese `voice_id` → el guion en su voz.
4. `generate_video` model **`wan2_7`**, `medias`: `start_image` (frame real de ella) +
   `audio_references` (**el `job_id` del TTS**, no una URL), `duration` 2–15 s, 1080p, 9:16.

**Costo medido:** el ciclo completo gastó **61 créditos**. Un clip suelto de 5 s a 1080p = 12,5.

**QA obligatorio antes de dar por buena una pieza:**

- **La voz.** `wan2_7` genera audio propio por defecto, así que hay que probar que usó el tuyo:
  correlación cruzada de la envolvente entre el audio del MP4 y el WAV del TTS. En la prueba dio
  **1.000 con desfase 0,00 s**. Sin este chequeo no se sabe.
- **La cara.** Hoja de contacto de 5 frames recortados al rostro — mirar dientes y comisuras.
- **Las manos.** Un frame completo: dedos y anillo.

**Límite honesto:** Higgsfield genera **por clip de 2 a 15 s**, no un avatar reusable con ID.
Para algo largo se encadenan clips y la consistencia depende del `start_image`. Para "guion
largo → un solo video", HeyGen sigue siendo mejor — pero cuesta plan pagado.

**La prueba:** `out/valeria/gemela-higgsfield/prueba01_8s_1080p.mp4` (8 s, 1080p vertical).


---

## 7. La vía buena para la cara — lipsync sobre el metraje real

**La regla:** para que una persona real se reconozca, no se le genera la cara — **se le mueve
la boca sobre su propio metraje**. Los píxeles de sus ojos, su piel, sus dientes y sus manos
son los suyos, no una aproximación.

```bash
python3 scripts/avatar-lipsync-magnific.py <video_base.mp4> <audio.mp3> <salida.mp4>
```

Sube los dos archivos a Drive, los publica por enlace, manda el job a **LatentSync**
(`POST https://api.magnific.com/v1/ai/lip-sync/latent-sync`, header `x-magnific-api-key`),
espera y descarga. **166 s para 15 s de video.**

**El pipeline completo de una pieza nueva:**

1. `generate_audio` de Higgsfield con la voz clonada (`c9e28ab7-a225-4ce6-8fa4-8371d33b9b36`)
   → el guion en su voz.
2. Cortar del master real un tramo **del largo del audio**, enderezado (`transpose=2`) y
   escalado a 1080×1920, **sin audio** (`-an`).
3. Correr el script.

**Lo que hay que mirar antes de entregar:**

- **Recorte 1:1 de la cara, real al lado del resultado.** Caja de ~520×520 sobre el cuadro de
  1080×1920. **Nunca juzgar en miniaturas** — a 400 px de alto el defecto no se ve y se
  aprueba basura.
- La **boca queda algo más blanda** que el resto de la cara: es el límite de LatentSync.
  Invisible a tamaño de reproducción, visible con zoom. Un plano más abierto lo disimula.
- Medir **dónde termina el habla de verdad** (el TTS deja cola de silencio) y que el video
  la cubra.

**El límite real:** el lipsync no inventa planos. Necesita metraje de ella para cada pieza, y
hoy sólo hay 62 s y 54 s de una sola sesión — misma ropa, mismo fondo. Para tener variedad
hay que grabar más, y esa misma sesión de 3 minutos serviría además para HeyGen Avatar V.

**Resultado:** `out/valeria/gemela-lipsync/reel01_lipsync_15s.mp4`.
