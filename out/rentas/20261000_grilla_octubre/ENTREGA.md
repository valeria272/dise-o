# RENTAS NUEVA URBE · VALLE ALTIPLÁNICO — grilla OCTUBRE 2026

> Producido el 02-09-2026. Sistema: `clients/nueva-urbe/CLAUDE.md` · criterio vigente:
> **Paulina Bustamante (septiembre 2026)**, decidido por Valeria.

## Qué está listo

| Pieza | Fecha | Archivos | Estado |
|---|---|---|---|
| **Carrusel Halloween** | mar 27-oct | `feed/rentas_c-halloween1..5.png` · 4500×5625 | ✅ **Listo para revisión** |

Los 5 fondos son **imágenes IA** (Nano Banana Pro, 4K), por decisión de Valeria: el brief
pide personas manipulando cinta, ganchos y telarañas, y eso no existe en el banco del cliente.
Se ambientaron para que se lean como un departamento de Valle Altiplánico —muro beige claro,
porcelanato claro, persiana zebra, luz natural cálida— y **sin marcas legibles** en los envases.

**Corregido tras la revisión de Valeria:** la caja del logo estaba **65 % más alta de la cuenta**
(1088×1351 en vez de 1088×821) y el logotipo quedaba hundido contra el borde inferior — el padding
porcentual del CSS peleaba con el `aspect-ratio`. Ahora va en píxeles y calza con la referencia:
ratio 0,755 contra 0,754, aire superior 17,8 %.

**QA hecho:**
- Las 5 piezas a **4500×5625** exactos y con los hex medidos (`#1372F1` / `#CCDC00`).
- **Manos revisadas con zoom 4×** en las cuatro láminas que las muestran: anatomía correcta,
  cinco dedos, nudillos y uñas bien formados. Ninguna se descartó.
- **Contraste** del titular de la portada contra su fondo: **9,63:1** (mínimo legible 4,5:1).
- **Margen inferior libre 6,4 %–7,0 %**, dentro del rango propio de Paulina (5,8 %–16 %).
- Cortes de línea **a mano**: al dejar envolver solo quedaban huérfanas («removibles», «pared.»).
- Cero `style=""` suelto en el HTML: todo sale de `base.css`.

**Textos:** verbatim del brief (`RENTAS_NUEVA_URBE_GRILLA_OCTUBRE_2026_1.pptx`).
Los cortes de línea son míos.

## Qué falta y por qué

| Pieza | Fecha | Bloqueo |
|---|---|---|
| Reel comercial | mar 6-oct | falta metraje limpio de Valle Altiplánico |
| Estático «Sin comisión» | mar 13-oct | falta foto real del interior / quincho |
| Carrusel PAID «Arrienda fácil» | mar 20-oct | faltan fotos reales (visita, contrato, ejecutivo) |
| Historia proyecto | 2-oct | falta foto real de interior + áreas comunes |
| Historia Halloween | 29-oct | falta foto de fachada / áreas comunes |

**La causa es una sola: no hay material fotográfico bruto de Valle Altiplánico.**
Se intentó sacarlo de los 6 reels entregados (son 4K, 2160×3840, así que un fotograma sirve
como foto), pero **los reels están subtitulados casi de punta a punta**: de 611 fotogramas
analizados a 6 fps, solo **12** quedan sin gráfica encima, y son todos del mismo instante.
La marca manda **foto real del condominio**, así que no se reemplaza con IA.

Hace falta abrir en Drive:
- `PROYECTOS INMOBILIARIOS / VALLE ALTIPLÁNICO` — `1_TUAwOKmMX3vYmEJuYzipVtK1ODMKpFh`
- `VALLE ALTIPLÁNICO / videos-dron` — `1SMwy6tUMfQnqe3SpDzifg3lhyH4-AiKc`
- `MATERIAL CLIENTE 2024` — `14ztIGZ0Zxs9zo6QryXxjzVORqa6R4zf7` (los MP4 del cliente, sin subtítulos)
- `LOGOS INU` — `1fO3qfzO8FBBg7Kpr5IL-IQWO65zJrgo-` (para tener los logos oficiales)

Mientras tanto, los logos se **extrajeron de las piezas entregadas**: `logo_rentas.png`
(590×550, de la caja blanca de `rentas_c-benef1` a 4500 px) y `logo_valle_blanco.png`
(870×456, del banner `rentas-mail_1.3`). Sirven, pero conviene reemplazarlos por los oficiales.

## Decisiones que hay que confirmar

1. **⚠️ El WhatsApp del estático del 13-oct.** El brief de **grilla** dice `+56 9 9707 9951`,
   que es el número de **Travesía (INU, venta)**. El brief de **mailing del mismo mes** usa
   `9955` dos veces y su nota final dice literal «(2) número de WhatsApp (se usa +56 9 9707 9955)».
   Julio y agosto también usaron 9955. Valeria eligió «verbatim del brief» **antes** de que
   apareciera esa nota.
2. **El botón `RENTAS.INU.CL` de la lámina 5.** No está en el brief; es el cierre canónico del
   sistema (aparece en todos los carruseles y reels de Rentas). Si el cliente lo quiere fuera,
   se borra sin tocar nada más.
3. **⚠️ El precio y la superficie no calzan entre canales.** El brief y el feed de Instagram
   (post del 18-ago) dicen **desde $715.000 y desde 59 m²**; el sitio `rentas.inu.cl` publica
   **desde $780.000 y desde 74,76 m²**. Puede ser otra tipología, pero conviene alinearlo antes
   de que salga una pieza con una cifra y la web muestre otra.
4. **Valle Altiplánico SÍ tiene piscina** — se ve en el dron de mayo. El brief de septiembre la
   nombraba y el de octubre no. Vale la pena recuperarla como atributo.
5. **La torre del frente dice «LAGUNA VERDE»** en la fachada, en el metraje de mayo. Asumo que es
   el nombre de la torre dentro del condominio; conviene confirmarlo antes de publicar ese plano.

## Cómo reproducirlo

```bash
cd out/rentas/20261000_grilla_octubre/editables
python3 build.py      # genera los HTML desde los textos del brief
bash render.sh        # HTML -> PNG con Chrome headless, a 4500 px
```
