# Retomar — UGC OPPO Reno16 (chat nuevo)

Abre un **chat nuevo** de Claude Code en `EDITOR VIDEOS` y pega esto:

---

Retomemos el UGC de OPPO Reno16. Lee la memoria `higgsfield-ugc-next.md`.

Ejecuta en orden:
1. Verifica Higgsfield con `ToolSearch "+higgsfield"`.
2. Clona mi voz desde `public/assets/oppo/voz_chilena.m4a` con `create_voice`.
3. Genera la VO del guión aprobado con esa voz (español de Chile).
4. Genera la creadora (Soul, variante A) + video Seedance 2.0, 9:16.
5. El OPPO Reno16 debe verse **TAL CUAL** la foto oficial — usa `public/assets/oppo/reno16_lila.jpg` como referencia/inserto. NO dejes que el modelo invente el teléfono.
6. Muéstrame el resultado para revisar **voz y acting**.

---

## Estado de assets (verificado 2026-07-21)

| Asset | Ruta | Detalle |
|---|---|---|
| Voz a clonar | `public/assets/oppo/voz_chilena.m4a` | 49s, 1.4 MB |
| Reno16 lila | `public/assets/oppo/reno16_lila.jpg` | 958×1183, frente + dorso |
| Reno16 blanco perla | `public/assets/oppo/reno16_blanco.jpg` | 1600×883, solo dorso |

**Color sugerido: lila** — es la única foto con frente y dorso (más útil para el inserto) y conecta mejor con el target 18-28 de "Make Your Moment". Si prefieres blanco perla, dilo en el chat nuevo.

## Guión aprobado (~11s)

> "Anoche saqué esta foto. Sin flash, sin editar. Y no soy fotógrafa: solo tenía el Reno16. No gana por especificaciones… gana porque no te pierdes el momento."

Cierre en pantalla: **Make Your Moment**

## Por qué hay que abrir chat nuevo

Claude Code fija el set de conectores MCP al **crear** la conversación. El chat anterior nació antes de que Higgsfield estuviera conectado, así que ahí nunca carga — ni reconectando, ni reabriendo la app, ni con `/compact`.
