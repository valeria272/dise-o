# CAP.02 · Música — prompt para la app web de Magnific

La API de música de Magnific responde **410 desde el 23-09-2026**: la pista se genera a mano en
la app web (magnific.com → Audio / Music) con la cuenta del estudio, y se baja a
`public/assets/gcl/cap02-v3/musica/`.

**Una sola pista de ~45 s.** El montaje la corta según el mapa musical del GUION_FINAL §21:
entra en 0:07, se corta en seco con el primer DING (0:13), vuelve más intensa en 0:16,5 y
termina en un golpe en 0:22. Por eso se pide con **dos secciones y un final seco**.

## Prompt (en inglés, que es como mejor responde)

```
Instrumental indie rock, early-2000s New York garage rock revival sound. Dry, tight, punchy
drums with a busy hi-hat; a driving eighth-note bass line with a strong groove; two
interlocking guitars, one clean and staccato, one slightly crunchy playing short syncopated
stabs. Cool, urban, elegant, nervous, restrained energy — confident, not epic. 135 BPM, key of
A minor. First half: tight groove, a little held back. Second half: same riff but more
intense, more distortion and drive, open hi-hats. Ends on one sharp full-band stop hit, no
fade out. No vocals, no synths, no electronic beats, no orchestra.
```

**No nombrar bandas** en el prompt (los generadores las filtran o las imitan demasiado cerca).
La referencia de espíritu es The Strokes, sin copiar ninguna canción.

## Si sale mal
- Suena corporativa o «stock» → agregar *«raw, live band recording, slightly lo-fi»*.
- Suena electrónica → repetir *«no synths, no electronic drums»* al principio.
- No termina en golpe → pedir *«ends abruptly on a single staccato hit»*; si igual no, el corte
  se hace en el montaje sobre el último tiempo fuerte.
- Generar **2–3 opciones** y elegir por el groove de la primera sección, que es la que más se oye.
