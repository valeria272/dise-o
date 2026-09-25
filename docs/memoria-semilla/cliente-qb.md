---
name: cliente-qb
description: "QB — cerebro del cliente: 36 reglas firmes, última cosecha 2026-09-25. Generado desde clients/qb/APRENDIZAJES.md; leerlo antes de diseñar para qb"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/qb/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para qb: no se traspasa a otra marca.

Criterio: **Elisabet Soto «Eli»** · Aprueba: **el cliente, por la grilla nativa de QB; contenido (Nicolás Ávila) ajusta textos**

## Reglas más confirmadas
- **R-31** · Al corregir en Drive se sube con **nombre nuevo** (v4, v5…): la vista previa de Drive queda cacheada al reemplazar por el mismo ID — _17-09, Eli «no veo el cambio»; repetido en v5, v6 y v7_ · ✔×4
- **R-13** · Antes de diagramar se pregunta **«¿esta va a paid?»**; si sí o hay duda, el texto va dentro de la zona segura (250 / 340 / 115 px en 9:16) — _Eli, 15-09: «El texto es importante que no pueda ir fuera del margen»_ · ✔×3
- **R-32** · Sólo se diseña lo que está `OK PARA DISEÑAR`; `PENDIENTE POR CLIENTE` no se toca — _bitácora 17-09, 21-09, 24-09 (Trivia de brindis, Reel DJ)_ · ✔×3
- **R-04** · ALL YOU CAN DRINK es un bloque cerrado igual al KV: sólo cambia la foto; logo, nombre, botón con degradado y «TODOS LOS MARTES / POR $13.990 / 18:00 a 21:00 hrs» no se tocan — _Eli, 17-09: «botón verde con efecto de degradado y logo + el nombre no»; medido igual al píxel en las ST de junio y septiembre_ · ✔×2
- **R-09** · El logotipo hace de **palabra** en la frase («MEJOR PAYA DE **QB**», «*Sunset* QB»), no de firma en la esquina — _medido en `ST n°2 S3 QB` y `Post n°2 QB SUNSET`, 15-09_ · ✔×2
- **R-15** · Nunca le pidas a un modelo de imagen que escriba la promo: la escena se genera con la pantalla en **verde plano** y encima se monta, con homografía, la gráfica rendida con las fuentes reales — _ST AYCD S5, 17-09; repetido en octubre (06-10 AYCD, 21-10 ticket)_ · ✔×2
- **R-27** · No se genera lo que ya está fotografiado: la fuente son las sesiones propias, y del video se saca la foto, la historia, el reel y el post en movimiento — _Eli, 15-09; aplicado en octubre con las sesiones en video, 24-09_ · ✔×2
- **R-01** · QB es marca independiente: nada de DT, Between ni Piso 18 entra, y nada de QB va para allá — _Eli, 15-09: «QB Restaurant es una marca independiente…»_ · ✔×1
- **R-02** · El feed se ve minimalista y elegante; una pieza cargada no es de QB aunque cumpla el brief — _Eli, 15-09_ · ✔×1
- **R-03** · Cada pieza muestra cóctel, plato o rostro — _Eli, 15-09_ · ✔×1
- **R-05** · Se escribe «ALL YOU CAN DRINK», en versales («ALL» y «DRINK» ExtraBold, «YOU» y «CAN» itálica) — _Eli, 17-09; reglas.yaml `aycd-grafia`_ · ✔×1
- **R-06** · Se escribe «Sunset QB»: «Sunset» en Brushwell, enlazado con el logotipo — _Eli 15-09; medido en `Post n°2 QB SUNSET`; reglas.yaml `sunset-grafia`_ · ✔×1
- **R-07** · En una promo con KV, el KV gana a la redacción del brief; del brief se toma literal sólo lo que el KV no cubre — _ST AYCD 28-09, S5, 17-09_ · ✔×1
- **R-08** · El botón lleva el degradado horizontal (oscuro en bordes, claro al centro) y esquinas vivas — _barrido de `PROMOS QB 2026 AYCD 2026 ST.png`, 17-09; Eli lo declaró intocable_ · ✔×1
- **R-10** · Todo va centrado; el titular es un bloque de dos pesos del mismo cuerpo — _medido en `ST n°2 S3 QB` (una pieza), 15-09_ · ✔×1
- **R-11** · Toda cifra en Raleway lleva **cifras de caja alta (`lnum`)**; activar «tabulares» no hace nada porque `tnum` no existe — _pedido de Eli 15-09 («los números suelen verse extraños»), diagnóstico con fontTools_ · ✔×1
- **R-12** · La letra chica no tiene una sola fuente: Bell MT Italic en el post de Sunset, Raleway Itálica en la ST de AYCD. Mira la pieza antes de elegir — _corrección del 17-09_ · ✔×1
- **R-14** · En una pieza animada, la zona segura se mide en el **último** fotograma — _manual §6_ · ✔×1
- **R-16** · `minAreaRect` sirve para encontrar la pantalla, nunca para montar: los vértices salen de ajustar una recta a cada lado — _Eli, 21-09, ronda 6: «no se ve realista de acuerdo a la perspectiva del celular»_ · ✔×1
- **R-17** · El vidrio del celular refleja el bar (campo de luz desenfocado, espejado, fuerte arriba y débil abajo) — _ronda 6, 21-09; acerca la pieza al KV (35,1 vs 30,5)_ · ✔×1

## Lo que ya costó rondas
- **X-01** · Ejecutar un comentario tachado: se sacó el celular, que era el centro del brief — _ST AYCD S5, ronda 1, 17-09, 1 ronda perdida_
- **X-02** · Celular chico y textos de la pantalla ilegibles («El celular necesito que aumente», «no aumentaste el tamaño») — _ST AYCD S5, rondas 3–4, 2 rondas_
- **X-03** · Encuadrar con `transform: scale()`: textos y filo del recorte reventados — _ST AYCD S5, rondas 3–4, 2 rondas_
- **X-04** · Un mate dibujado desde una forma ideal (más grande o más chico que el teléfono): la letra se corta en el aire o pisa el chasis — _ST AYCD S5, rondas 3, 4 y 5, 3 rondas_
- **X-05** · Pegar la gráfica sin perspectiva (paralelogramo en vez de trapecio) y sin reflejo: «se ve como calcomanía» — _ST AYCD S5, ronda 6, 21-09, 1 ronda_
- **X-06** · Filo verde de croma alrededor de la pantalla (~13.000 px) — _ST AYCD S5, rondas 1–5, cazado en la ronda 6_
- **X-07** · (interno) Estática en el frame 239 porque lo decía la cabecera: la estática y el video mostraban las bandas en lugares distintos — _v7, 23-09, cazado antes de entregar_
