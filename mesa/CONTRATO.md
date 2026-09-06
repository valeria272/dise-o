# La mesa — el contrato entre ChatGPT y Claude

> **Qué es esto.** El formato fijo en que se hablan la dirección (ChatGPT) y la
> producción (Claude Code). No es una integración: es un acuerdo de formato. Nadie
> se conecta a nada.

## Por qué existe

Hasta el 06-09-2026 el puente entre los dos era **Valeria redactando**. GPT
escribía la dirección en el chat, ella la resumía para Claude; Claude producía,
ella sacaba capturas y se las describía a GPT. Cada vuelta perdía algo: el que
traduce decide, y decidía sin querer.

El repo ya era el bus —`09_PROMPTS_CLAUDE_CODE/MASTER_PROMPT_CLAUDE_CODE.md` es
literalmente un brief de GPT que Claude lee. Lo que faltaba era **la vuelta**.

Con la mesa Valeria deja de redactar y sólo **transporta**: arrastra dos archivos
al chat de GPT, y pega la respuesta de vuelta acá. Ninguno de los dos lados le
pide que interprete nada.

## La vuelta completa

```
    Claude produce ─→ mesa/salida/<pieza>/parte.md + hoja-contacto.png
                              │
                    (los arrastras al chat de GPT)
                              │
    GPT dirige     ─→ un bloque ```json  (el esquema de abajo)
                              │
                    (lo pegas acá, o lo guardas tú)
                              │
                      mesa/entrada/<pieza>-ronda<N>.md
                              │
    Claude ejecuta ─→ scripts/mesa.py plan <pieza>  →  plan de la cola
                              │
                      scripts/cola.py enviar … → esperar → recoger
                              │
                              └──→ y vuelve a empezar con el parte siguiente
```

## Lo que devuelve GPT — el esquema

Un bloque ` ```json ` y nada más. El parte que le llega ya trae estas
instrucciones adentro, así que **no tienes que explicárselo cada vez**.

```json
{
  "pieza": "cap02",
  "ronda": 2,
  "presupuesto": 4,
  "no_se_toca": ["el visor de G", "el eje 180°", "el hueco del f.248"],
  "planos": [
    {
      "id": "cut02",
      "veredicto": "REHACER",
      "por_que": "G gira el cuerpo entero y pierde el visor a los 2,2 s",
      "correccion": "la cabeza gira SOLA y en el último tercio; el cuerpo queda fijo",
      "keyframe": "mismo"
    },
    { "id": "cut01", "veredicto": "APROBADO" }
  ],
  "respuestas": { "¿el 02 es Revisión 7 o Turno de noche?": "Revisión 7" }
}
```

| Campo | Qué es |
|---|---|
| `presupuesto` | **La compuerta del dinero.** Cuántas regeneraciones se autorizan esta ronda. Cada una cuesta créditos de Freepik, o sea plata |
| `no_se_toca` | Lo que ya está aprobado. Existe para que la fábrica no derive de estilo ronda a ronda |
| `veredicto` | `APROBADO` · `AJUSTAR` (mismo keyframe, otro prompt) · `REHACER` (keyframe nuevo primero) |
| `correccion` | En lenguaje de plano, no de prompt. Claude lo traduce |
| `keyframe` | `"mismo"`, o la ruta del keyframe nuevo si hay que rehacerlo antes |

## Las tres reglas duras

1. **El presupuesto manda.** Si los `REHACER` + `AJUSTAR` pasan del `presupuesto`,
   `mesa.py plan` **no genera el plan**: para y te pregunta cuáles entran. Un loop
   sin tope de gasto no es una fábrica, es una fuga.

2. **El canon está por encima de GPT.** Si una corrección contradice
   [`gcl-agent/universo/CANON_LOCK.md`](../gcl-agent/universo/CANON_LOCK.md), gana
   el canon y se te avisa. GPT dirige adentro de los candados, nunca sobre ellos.

3. **GPT no ve el video, ve fotogramas.** El ritmo, el largo de los cortes y el
   timing musical no los puede juzgar desde stills: eso se decide con
   `_timeline.json` y con tus ojos. No le pidas montaje.

## Los comandos

```bash
python3 scripts/mesa.py parte cap02      # arma el parte + la hoja para GPT
python3 scripts/mesa.py plan  cap02      # traduce la respuesta de GPT a un plan
python3 scripts/cola.py enviar gcl-agent/cap02/_plan.json
python3 scripts/cola.py esperar          # UNA espera para todos los planos
```
