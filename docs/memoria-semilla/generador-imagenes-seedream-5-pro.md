---
name: generador-imagenes-seedream-5-pro
description: "El generador de imágenes por defecto del estudio es Seedream 5 Pro (vía API de Freepik), por decisión de Diego el 23-09-2026; rutas, formato de referencias y trampas"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 51151e77-6ceb-4e19-866b-8b1f241bf928
  modified: 2026-09-23T20:00:18.653Z
---

**Para generar imágenes se usa Seedream 5 Pro**, no Mystic ni Nano Banana Pro
como primera opción. Diego, 23-09-2026: *«para la generación de imágenes utiliza
seedream 5 pro»*.

```bash
~/copylab-venv/Scripts/python.exe scripts/magnific.py seedream "<prompt>" --aspecto story|post|feed --out ...
~/copylab-venv/Scripts/python.exe scripts/magnific.py seedream "<qué cambiar>" --refs foto-real.jpg --out ...
```

**Why:** lo pidió explícitamente tras ver las imágenes de Mystic y Nano Banana
en el PAID de Tierra Calma. Y en la práctica rindió mejor: con una foto real de
referencia respetó la traza (dejó grises los caminos pavimentados) mejor que
Nano Banana Pro.

**How to apply:**
- Rutas (sondeadas el 23-09, no estaban documentadas): `text-to-image/seedream-v5-pro`
  y `text-to-image/seedream-v5-pro-edit`. `seedream-5-pro` sin la «v» da 404.
- `reference_images` = lista de **strings en data URI**. Base64 pelado pasa la
  validación y la tarea FALLA después en el servicio.
- Resolución `1.5k` o `2k`; aspectos con los nombres largos de Mystic.
- **Escribe la composición en el prompt** (qué % de cielo arriba, dónde va la
  escena, qué queda libre abajo): sin eso pone a la gente grande y abajo, y la
  píldora o el titular le caen encima.
- Excepción que sigue vigente: si la imagen necesita **texto legible adentro**,
  eso sigue siendo Nano Banana Pro ([[freepik-api-generacion-imagenes]]).

Relacionado: [[tierra-calma-paid-octubre-2026]].
