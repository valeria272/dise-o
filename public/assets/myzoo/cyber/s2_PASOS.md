# Story 2 Cyber MyZoo × Mercado Libre — «¡Última patita del Cyber!» (viernes 9 de octubre)

Brief en `brief_story2.png` (contenido): mismo sistema gráfico de la story 1 + urgencia (contador, reloj, rayo).
Idea de Paulina (02-10): el gato con un reloj, en la pose del conejo de `ref_pose_conejo.png`; mismos globos
blancos inflados, sumando un reloj. Sólo imagen, sin logo ni texto; los productos los pone ella.

v1: una generación por toma, Nano Banana Pro 4K story, referencia `ref_story1.jpg` (la imagen limpia v3 de la
story 1). Prompt = `prompt_base.txt` + `prompt_A.txt` o `prompt_B.txt` + `prompt_fin.txt`. Sin retoques.
- `v1_A1.png` → opción A (gato en la caja, sostiene el reloj con la pata)
- `v1_A2.png` → opción B (gato en la caja, reloj al pecho y pata levantada)
- `v1_B1.png` → opción C (perro en la caja, gato adelante con el reloj)
La imagen del conejo NO se mandó al generador (es un personaje de película): sólo se describió la pose.

## v2 (02-10): Paulina rechazó la v1 («no me gustó»)
Pidió: perro DENTRO de la caja con cara de sorpresa; gato sentado EN PRIMER PLANO, con una pata toma el reloj y
con la otra lo apunta; sólo los porcentajes inflados, SIN globo de reloj («tiene mucho detalle, la imagen tiene
que ser minimalista»). Prompt `prompt_v2.txt`, misma referencia, 3 tomas, sin retoques.
- `v2_c.png` → opción A (toma el reloj por la corona y lo apunta) · `v2_b.png` → opción B (lo sostiene a dos patas)
- `v2_a.png` descartada: gato chico, no queda en primer plano.

## v3 (02-10): Paulina mandó un BOCETO de distribución (`boceto_paulina.png`)
Gato muy grande en primer plano a la izquierda, cortado por el encuadre; una pata estirada de la que cuelga el
reloj al centro, la otra apuntándolo; la caja con el perro más chica, atrás a la derecha. Pidió revisar que no
haya patas ni manos de más. El boceto (recortado a la mesa de trabajo, `boceto_ref.png`) va como 2.ª referencia.
- `prompt_v3.txt` → tomas a, b, c · `prompt_v3b.txt` (caja más a la derecha, lentes del perro sobre la cabeza,
  pata que apunta sin garra larga) → tomas d, e, f.
- Entregadas: `v3_e.png` (opción A) y `v3_d.png` (opción B). Sin retoques.
- Descartadas: a y f cambian el set (papel mostaza angosto, otro muro) aunque f es la única que deja la caja bien
  a la derecha; b tapa el logo con la cadena; c deja los lentes del perro colgando del cuello y una garra larga.

## v4 (02-10): los globos pasan a decir «20%» (izquierda) y «30%» (derecha), en las DOS stories
Paulina: «corresponden a cada uno» (20 % en todos los productos, 30 % usuarios Meli+, según el legal).
`scripts/myzoo-cyber-porcentajes.py`: recorte 16:9 de la franja de los globos → Nano Banana Pro 4K wide con
`raw/myzoo/cyber/prompt_porcentajes.txt` (2 tomas por imagen, se eligió la `a` en ambas) → `pegar` devuelve
sólo la zona que cambió. Story 1: sobre `cyber/ampliada.png` + `myzoo-cyber-story.py final`. Story 2: sobre `v3_e.png`.
