# Bitácora — Revex

## 2026-08-27 — Serena Abarca (con Claude)

**Qué se hizo:** Se cerró la grilla de septiembre en 4:5 (2250 × 2812) después de seis
rondas. Se resolvieron los 10 comentarios de Paulina y los 10 de Serena. Correcciones:
los tres cuadros rojos del concurso (CONCURSO, la fecha y la dirección completa), el
interlineado de Temuco, el ícono de WhatsApp en el outlet, la textura del fondo rojo
—el patrón le ponía un velo negro al 17 % de las placas y se leían como bloques sueltos—
y el degradado del concurso, que se apagaba antes del borde y se veía cortado. Se
cambiaron tres fondos por material que mandó Paulina.

**Dónde quedó:** Las 8 piezas subidas al Drive en `DISEÑO PAID / GRÁFICAS SEPTIEMBRE`,
ordenadas en CONCURSO, TEMUCO, LAS CONDES y OUTLET. `scripts/revex-sep2026-piezas.py`
con el arreglo del outlet; `scripts/revex-sep-subir.py` nuevo (sube a una carpeta por
nombre, generaliza al de v2); `scripts/revex-outlet-textura.py` quedó obsoleto al mover
el arreglo al render. Tres fondos nuevos en `public/assets/revex/sep/`.

**Qué sigue:** Nada urgente. Si vuelve feedback, el render corre desde el repo limpio:
Valeria versionó los scripts y los 18 fondos en el commit `4351ce3`.

**Abierto:** La foto de Temuco es un frame de video cuya sucursal **no está verificada**
— el cliente compartió su carpeta TEMUCO con la fachada real del Ebema, identificada por
señalética. Regla nueva: una pieza de sucursal no se entrega sin que alguien con acceso
al original confirme la sucursal. Ver el manual, § ronda 4.

## 2026-09-02 — Serena Abarca (con Claude)

**Qué se hizo:** La clienta pidió cambiar SOLO el fondo de la portada del carrusel
«Tus muros también merecen un upgrade» por el render limpio del muro de mármol que
mandó (1000 × 1000, `public/assets/revex/sep/muros_marmol_limpia.jpg`). La pieza no
existía en el repo, así que se midió píxel a píxel la publicada
(`public/assets/revex/sep/muros_upgrade_original.png`) y se reconstruyó la capa
gráfica completa en `scripts/revex-muros-upgrade-foto-limpia.py`. Todo calza:
bloque de logo 356 × 356 a top 0 y barra 250–1797 / 944–1124 idénticos al píxel;
titular con IoU 78 % y tinta 99 % (la referencia de admisión de la marca es 71 %);
cápsula y flecha en la misma caja de 878 × 91.

**Tipografía:** el titular de esta portada es **Montserrat wght 720**, no 775. Se
identificó comparando glifos con la máscara exacta de la línea 2 —que va sobre rojo
macizo, así que su matte se extrae sin error—: 720 da IoU 83,4 % y tinta +0,9 %;
700 → 82,6 %, 750 → 79,8 %. El CTA es Montserrat 400, cap 43, tracking +0,015 em.

**Encuadre:** la foto limpia trae UNA lámpara y a cuadro pleno cae justo debajo del
bloque de logo (lámpara x 653–1022 vs. bloque x 846–1201). Se recortan 174 px por la
izquierda y 25 por arriba para que la lámpara despeje el bloque por 40 px. La variante
sin recortar queda en `--variante plena`.

**Velo:** es lo único que no se copia. El fondo viejo era un render oscuro; el limpio
es de día, con el mármol en 233 de luma, y sobre eso el titular blanco no se lee. Se
puso un degradado que arranca en y 500 —arriba el mármol, que es el producto, queda
intacto— y deja el fondo del titular en 167,7, exactamente la luma que tenía la pieza
aprobada (167,7). Segunda caída suave hasta y 1340 para que el CTA no quede flojo.

**✅ APROBADA por la clienta el 02-09-2026** sin ajustes, en la primera vuelta.

**Dónde quedó:** `out/revex/sep2026/rvx_muros-upgrade_panea_2048.png` (2048 × 2048,
mismo tamaño que la publicada, entra como reemplazo directo) + comparativa
antes/después. Copias en el Escritorio. **No se subió al Drive: no hay token de Google
en esta máquina.** Pasa el QA de marca (7 reglas).

**Qué sigue:** Subirla al Drive reemplazando la portada del carrusel en la carpeta de
entrega (`1uMPBBoOpspRKBEqtiZOElJuMEDuaisl2`) — hay que hacerlo desde una máquina con
token de Google o con el conector de Drive — y pedirle a la clienta el render del muro
en tamaño grande.

**Abierto:** La foto del cliente es de 1000 px y hay que subirla 2,48×. En el detalle
fino (el mueble de madera) la energía de borde queda en 441 contra 719 de la publicada
— se nota sólo al 100 %, no en feed. Si la clienta tiene el render en grande, se
reemplaza el archivo en la misma ruta y se vuelve a correr el script sin tocar nada más.
