# BRAND — el ADN

El sistema no vive en este documento: vive en el código, para que no pueda
desincronizarse.

| Qué | Dónde | Lo lee |
|---|---|---|
| Los tokens (colores, voces, formatos, topes, prohibiciones) | `src/brand/copylab/tokens.json` | TypeScript **y** Python |
| Carga de fuentes y utilidades | `src/brand/copylab/sistema.ts` | Remotion |
| Composición tipográfica | `src/brand/copylab/tipografia.tsx` | Las piezas |
| Intervenciones a mano | `src/brand/copylab/mano.tsx` | Las piezas |
| Lienzo y tratamiento fotográfico | `src/brand/copylab/lienzo.tsx` | Las piezas |
| Reglas ejecutables de QA | `clients/copywriters/reglas.yaml` | `qa/motor.py` |

**Un color escrito dos veces es un color que algún día va a estar
desincronizado.** Por eso `tokens.json` es JSON y no TypeScript: el agente social
en Python lee exactamente el mismo archivo.

## La marca, en una línea

Copywriters / Grupo Copylab — agencia de marketing digital en Santiago. **No es
sólo copy:** performance, datos y tecnología + creatividad, marca y comunidad.
Firma de cierre: *estrategia, creatividad y resultados*.

## Qué NO es este sistema

El sistema del **feed**. La **web** de copywriters.cl tiene su propio kit
(crema `#F8F6F1`, navy `#0F2B4C`, lime `#C8F135`) en `src/brand/copywriters.ts`,
y ese lime **no entra al feed**. Son dos medios, dos sistemas, y ninguno de los
dos está mal.
