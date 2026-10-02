# Story Cyber MyZoo × Mercado Libre — cómo se armó (02-10-2026)

Entrada: `story_cyber_original.png` (imagen de Paulina). Salida: `out/myzoo/cyber-2026/myzoo_storie_cyber_imagen-limpia_v1.png` (2250×4000).
REFS = `story_cyber_original.png` + `public/assets/myzoo/assets/ps_odorperro.png` + `ps_odorgato.png`

1. Toma: `magnific.py pro "<prompt_v3_base.txt + prompt_v3_C.txt>" --aspecto story --resolucion 4K --refs REFS` → se eligió `v3_C1.png` (de 12 tomas en 3 tandas).
2. `myzoo-cyber-story.py base` → `base.png` (recorte bajo el rollo del papel).
3. Pasada «sin envases» sobre `base_ref.jpg` → `placa_nb.png`; `myzoo-cyber-story.py placa`.
4. `myzoo-cyber-story.py boceto` → packshots reales en posición (el gatillo no tapa el logo).
5. Pasada de integración (luz, sombra, reflejo) sobre `boceto_ref.jpg`, 3 tomas → se eligió `integra_b.png`; `myzoo-cyber-story.py integrar integra_b.png`.
6. `myzoo-f3-calzar.py integrada.png calzada.png calces.json` → etiquetas reales.
7. Pasada de pelaje sobre `perro_rec.png` (1:1, 2K), 2 tomas → `perro_nb_b.png`; `myzoo-cyber-story.py perro perro_nb_b.png`.
8. `myzoo-cyber-story.py final calzada_perro.png myzoo_storie_cyber_imagen-limpia_v1.png`.

Los prompts de los pasos 3, 5 y 7 están en los `.log` y en el historial de la sesión; el de la toma, en `prompt_v3_*.txt`.
Lo que NO funcionó: pedir «tubos detrás del papel» manteniendo «rim light» en los animales (deja halo de recorte); las tandas v1 y v2 dejaron los tubos en los muros.

## 2.ª ronda (02-10): todos los productos + sin productos

Paulina pidió sacar los dos Odor Eliminator y poner el packshot grupal que dejó en Drive
(`5-en-revision/2026-10_octubre/myzoo_agosto-36.png`, 19956×10623, 8 envases) y además una opción sin productos.

- `pack_grupo.png`: el grupal recortado a su zona opaca y a 3200 px de ancho.
- Con productos: `boceto-grupo` → pasada de integración sobre `boceto_grupo_ref.jpg` (3 tomas, se eligió `integra_grupo_a.png`) → `integrar-grupo integra_grupo_a.png` → `myzoo-f3-calzar.py integrada_grupo.png calzada_grupo.png calces_grupo.json` (luz «suave») → `perro perro_nb_b.png calzada_grupo.png calzada_grupo_perro.png` → `final calzada_grupo_perro.png …_v2_todos-los-productos.png grupo integrada_grupo.png`.
- Sin productos: `perro perro_nb_b.png placa.png placa_perro.png` → `final placa_perro.png …_v2_sin-productos.png ninguno`.

## 3.ª ronda (02-10): sin productos, ampliada y con la zona superior más clara

Paulina se queda con la versión sin productos (ella pone la fila de productos adelante). Pidió más espacio
hacia todos los lados (sobre todo abajo y a los costados), el papel amarillo más ancho («que no se vea como
cemento») y la zona superior más iluminada.

- `lienzo placa_perro.png` → la escena al 90 % sobre un lienzo 3072×5504, sin los muros originales, con el
  papel pintado ancho continuando el color real (`campo_papel`) y gris sólo en dos franjas de 200 px.
- Pasada de Nano Banana Pro con `prompt_ampliar_v3.txt` sobre `lienzo_ref.jpg` → se eligió `ampliar_nb_g.png`.
- `ampliar placa_perro.png ampliar_nb_g.png ampliada.png` → vuelven los sujetos originales, el papel nuevo se
  empareja con el real, se alisa el piso libre y se aclara la zona superior (ganancia 1,31 arriba).
- `final ampliada.png myzoo_storie_cyber_imagen-limpia_v3_sin-productos_ampliada.png ninguno`.

Lo que NO funcionó: pedir el papel ancho por texto (lo deja angosto: tomas c, e, f); pintarlo con bloques de
color plano (la pasada copia el escalón y deja costura: toma d); darle a la escena original la luz de la pasada.
Magnific rechazó 2 tomas lanzadas en paralelo con «Error consuming credits»: se piden de a una.
