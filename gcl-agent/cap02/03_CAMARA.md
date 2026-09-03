# C · CAMERA MAP · D · CONTINUITY MAP

---

# C · CAMERA MAP

## C.1 · El eje

La línea de acción va **G.CL → monitor**. Corre a lo largo del escritorio.

Toda cámara fuera de eje vive del **mismo lado: cuadro-izquierda**. Las dos
cámaras que están sobre el eje (frontal y sobre el hombro) son los polos de un
plano/contraplano normal, no un salto.

```
                    pared
        ┌─────────────────────────────┐
        │   lámpara        MONITOR    │
        │      ·             ▓▓▓      │
        │                   ═══╪═══   │  ← CAM-A (sobre el monitor, mirando a G)
        │        teclado  mouse       │
   CAM-B│  ●  ·········  G.CL  ·······│
   CAM-C│  ●              ◉          │
        │        teléfono             │
        └─────────────────────────────┘
                     ▲
                   CAM-D  (sobre el hombro de G, hacia la pantalla)

        ── el eje ── G.CL ←→ MONITOR ──
        CAM-B y CAM-C SIEMPRE a la izquierda del eje. Nunca a la derecha.
```

## C.2 · Las cuatro cámaras

Cuatro posiciones, cuatro tamaños, y ninguna más. **No se inventa un ángulo nuevo
para cada corte** — eso es lo que hace que un montaje parezca clips sueltos.

| | Tamaño | Posición | Altura | Lente | Movimiento | Cuts |
|---|---|---|---|---|---|---|
| **CAM-A** | MASTER frontal | sobre el eje, apenas por encima del monitor | mesa +25 cm | 50 mm | **fija** | 05 (final) · 06 |
| **CAM-B** | MEDIUM lateral | 70° a cuadro-izquierda | mesa +15 cm | 35 mm | fija o arco lento | 02 · 05 |
| **CAM-C** | CLOSE UP | misma posición que B, lente largo | mesa +15 cm | 85 mm | fija | reserva |
| **CAM-D** | EXTREME CU / macro | sobre el hombro derecho de G, sobre el eje | mesa +30 cm | 100 mm macro | **fija** | 01 · 03 · 04 · 08 |

**CAM-D-low** es una variante de D, bajada a la altura de la mesa (+4 cm) para el
teléfono. Misma posición en planta, sólo cambia la altura: sigue siendo la misma
cámara, no una quinta.

## C.3 · Dirección de pantalla

En CAM-B, G.CL **siempre mira a cuadro-derecha** (hacia el monitor). En los 22,8 s
no hay un solo plano donde mire a cuadro-izquierda. Si un keyframe sale espejado,
se rechaza aunque el personaje esté perfecto.

## C.4 · El único movimiento de cámara del capítulo

Está en el **CUT 05**, frames 372–413: un arco de CAM-B a CAM-A, hacia la derecha,
a velocidad constante, que **frena en seco** al llegar al frontal.

Es el único, y por eso significa algo: la cámara también está siendo devuelta a su
posición inicial. Todos los demás planos son **fijos**.

⛔ Prohibido en este capítulo: handheld, shake, push-in orgánico, breathing,
dolly decorativo, crash zoom, orbit. Una cámara que respira ablanda el deadpan.

---

# D · CONTINUITY MAP

## D.1 · Continuidad por corte

Qué tiene que calzar entre un plano y el siguiente. Se revisa **antes** de aprobar
el keyframe, no después de generar el video.

| Corte | Cámara | Estado del set | Pose de G | Luz | Qué debe calzar exactamente |
|---|---|---|---|---|---|
| 01 → 02 | D → B | A → A | sentado → sentado | igual | la mano sobre el mouse, en la misma fase del click |
| 02 → 03 | B → D-low | A → B | de pie, congelado | monitor baja a 35% | la posición de G al fondo y el ángulo del teléfono |
| 03 → 04 | D-low → D-low | B → B | **idéntica** | idéntica | **todo**: es el mismo encuadre con un 4% más |
| 04 → 05 | — → B | B → B | de pie fuera de cuadro | vuelve a 100% | nada: media un negro |
| 05 → 06 | B→A → A | A | sentado | monitor 100%, lámpara a 0 | **el último frame del 05 ES el primero del 06** |
| 06 → 07 | A → negro | — | — | a negro | nada: el visor apagándose es el corte |
| 07 → 08 | negro → D | A | fuera de cuadro | como el 01 | nada: media un negro |
| 08 → 01 | D → D | A → A | fuera de cuadro | idéntica | **el encuadre del 08 y el del 01 son el mismo** |

## D.2 · Las cuatro constantes

Lo que **no puede cambiar** en ningún frame de los 684:

1. **La geometría del escritorio.** Monitor centrado, teclado delante, mouse a la
   derecha, lámpara arriba a la izquierda. (`02_LOCKS.md` § G)
2. **La escala del personaje.** Ancho de casco = 9 teclas.
3. **La dirección de la luz.** Key desde el monitor, práctica desde arriba-izquierda.
4. **La dirección de pantalla.** G mira a cuadro-derecha en todo plano lateral.

## D.3 · La verificación

Con los 12 keyframes sobre la mesa, antes de generar un solo video:

- [ ] ¿Los 12 se ven del **mismo escritorio**? Comparar el canto de la mesa.
- [ ] ¿La lámpara está en el mismo sitio en todos?
- [ ] ¿El ancho del casco mide 9 teclas en todos los que tienen teclado?
- [ ] ¿En todos los laterales G mira a cuadro-derecha?
- [ ] ¿El keyframe final del 05 y el inicial del 06 son **el mismo archivo**?
- [ ] ¿El keyframe del 08 y el del 01 comparten encuadre exacto?
- [ ] ¿Algún plano tiene una luz que no venga del monitor, de la lámpara o del visor?

**Si falla uno: se corrige el keyframe.** Nunca se compensa en el prompt de video.
