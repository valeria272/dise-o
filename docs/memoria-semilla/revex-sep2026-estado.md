---
name: revex-sep2026-estado
description: "Dónde quedó REVEX septiembre 2026 al 27-08: ronda 3 rendida en 4:5 y entregada en ZIP; NADA subido al Drive; 5 decisiones abiertas. RESUELTO: scripts y fondos ya versionados en el commit 4351ce3 — la ronda 3 se reproduce byte a byte"
metadata:
  type: project
---

# REVEX septiembre 2026 — estado al 27-08-2026 (fin del día)

## Dónde quedamos, en una línea

**Ronda 3 lista y rendida, esperando que Valeria la revise. No se subió nada al Drive.**

## Lo entregado

- 8 piezas en `out/revex/sep2026/` — **feed 4:5 a 2250×2812** y **story 9:16 a 2250×4000**.
- ZIP de revisión en el Escritorio: **`REVEX-septiembre-ronda3-27-08-2026.zip`** (35 MB).
  Trae ronda 3, ronda 2 para comparar, hoja de contacto, `LEEME.md` y `QUE-FALTA.md`.
- `out/revex/sep2026/_ronda2/` — la ronda 2 **recuperada bajándola del Drive**. No existía
  en el repo: la corrida cuadrada del 26-08 la había sobrescrito.
- Notas largas y verificadas: `out/revex/sep2026/LEEME.md` (comentario por comentario) y
  `out/revex/sep2026/QUE-FALTA.md` (cruce contra el brief).

## Las 5 decisiones abiertas — son de Valeria, no mías

1. **Cómo publicar.** Reemplazar en la raíz de `DISEÑO PAID`
   (`1uMPBBoOpspRKBEqtiZOElJuMEDuaisl2`) para que los comentarios sigan enganchados —es la
   convención que usaron en la ronda 2— o subir carpeta nueva. **Mi recomendación:
   reemplazar en la raíz y borrar la subcarpeta `v2`** (`1cERWSoIsR_p7XzUpZ3LgtKXL2d5a9LeK`,
   cuadrada, del 26-08): esa carpeta es justo lo que descolocó a Serena.
2. **El CTA en la gráfica.** El brief pide «Cotiza por WhatsApp» (outlet) y «Escríbenos por
   WhatsApp» (Temuco y Las Condes). No están: la ronda 2 los sacó porque dirección de área
   pidió eliminar la cápsula («Meta ya pone su botón»). Pendiente desde el 26-08. **Si se
   saca, se saca también en Casablanca.**
3. **WhatsApp general y web en las sucursales.** La hoja «Referencia» del brief los declara
   obligatorios; Temuco y Las Condes no los traen.
4. **La alfombra del concurso.** Lineamiento 2 del brief: tiene que ocupar buena parte del
   cuadro. Choca con Paulina, que pidió showroom claro y minimalista. Los fondos que existen
   cumplen uno u otro, nunca los dos. **Falta generar un ambiente claro con la alfombra
   grande** (Freepik, 10 min).
5. **Tercio inferior del story en outlet.** El brief lo pide libre. Temuco 0,59 · Las Condes
   0,57 · Concurso 0,65 cumplen; **outlet queda en 0,78** porque Serena pidió bajar ese
   bloque y la ronda 2 ya estaba en 0,73. Se dejó como ella pidió, avisando.

⚠️ **Y falta material del cliente:** una **foto vertical del local de Las Condes**. La única
que hay es 2250×1520 y no da para 9:16; el story se resuelve con un parche (estirar hacia
arriba la banda del panel metálico, que por ser corrugado vertical aguanta).

## Cómo retomar

```
scripts/revex-sep2026-piezas.py     # las 8 piezas
scripts/revex_sistema.py            # el sistema (primitivas)
scripts/revex-temuco-showroom.py    # fondo Temuco desde el video oficial
scripts/revex-lcd-fachada.py        # fondos Las Condes
scripts/drive-comentarios.py <folderId> [--json x.json]   # comentarios CON anchor
scripts/drive-bajar.py <folderId> <destino>               # baja una carpeta
```

**Ojo con iCloud.** Ese día el repo estaba evictado a ratos (archivos que pesan en el `stat`
pero leen 0 bytes, ~20 % a la vez) y eso rompe `cp`, `zip` y `git` en silencio. Se trabajó en
el sandbox **`~/copylab-work/revex-sep`** (fuera de iCloud) y se copió de vuelta con
reintentos verificando `len(data) == getsize`. Ver [[icloud-repo-evictado]].

## Lo que hay que recordar del método

**La ronda 3 recién salió bien cuando dejé de reusar el script cuadrado y MEDÍ la ronda 2.**
De ahí salieron las reglas reales: el bloque de sucursal se alinea **abajo** en feed (cierra
en 1105 de 1350) y **arriba** en story (parte en 569 de 1920) — por eso Temuco con 3 líneas y
Las Condes con 2 cierran parejos. Y el anchor de cada comentario de Drive es lo único que
desambigua un «este debe ir más abajo». Ver [[no-inventar-sistema-de-marca]].

**Trampas de material, encontradas midiendo y no mirando:**
- `concurso_amb_*.jpg` es el render OSCURO que Paulina rechazó **dos veces**; el showroom
  claro es `concurso_*.png`. Los nombres engañan, y la corrida cuadrada había vuelto al oscuro.
- `lcd_fachada_story.jpg` traía **1327 px de filas clonadas** desde y=2672. Se detecta por
  varianza vertical ≈ 0 en rachas largas de filas.
- Estirar una banda de foto sólo funciona si el patrón es **vertical**; hay que elegir el
  tramo por desviación horizontal mínima (filas 30-76 daban 10; con 140 se colaba el alero).
- El logotipo del local en la foto choca con el antetítulo: medir su bbox por color **antes**
  de decidir el recorte.
- Paulina entrega en 4:5: sus piezas de julio son 2250×2813.

## ✅ Reproducibilidad — resuelto el 27-08 (commit `4351ce3`)

Serena preguntó por qué ninguna de las 3 rondas se reproducía desde su Mac. **No había otra
máquina ni código secreto**: el sandbox `~/copylab-work/revex-sep/` era una copia byte a byte
del repo. El problema era que los scripts vivían **sólo en el working tree**. Lo commiteado
decía `FEED = (2250, 2250)` — cuadrado, **un formato que nunca se entregó** — de ahí su
"el script del repo sólo hace cuadrado".

Ya está empujado a `estudio/sistema-de-marcas` (repo `valeria272/dise-o`):
los 4 scripts + los **18 fondos** de `public/assets/revex/sep/` (29 MB, excepción explícita
en el `.gitignore`). Versionar el código sin su material no arreglaba nada.

**Verificado:** `revex-sep2026-piezas.py` devuelve las 8 piezas **byte a byte idénticas** a la
ronda 3 entregada. La v1 a 1080×1350 **no se recupera** — no quedó en ningún commit.

⚠️ **Medidas reales de cada ronda** (las del ZIP, no las que se suponía): v2 = **1080×1350**,
v3 = **2250×2812**. El 2250×2250 sólo existió en git; nunca lo vio el cliente.

> **La lección, que vale para toda marca:** si el render sale de un sandbox fuera de iCloud,
> el código vuelve al repo **el mismo día**. Tres rondas se rehicieron de cero por esto.
> Ver [[icloud-repo-evictado]], [[no-inventar-sistema-de-marca]].

Relacionado: [[revex-adn-medido]], [[compuerta-de-material]],
[[leer-el-brief-y-su-carpeta-de-referencias]], [[traspaso-zip-estudio]].
