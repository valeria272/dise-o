---
name: ebema-linkedin-fotos-sucursal
description: EBEMA LinkedIn — las imágenes parten de fotos REALES de sucursal y se recrean con IA más estéticas; nunca rostros de trabajadores
metadata:
  node_type: memory
  type: feedback
  originSessionId: f22d10a7-1802-425a-8233-fcdc9ff10223
  modified: 2026-09-24T18:24:43.801Z
---

**Paulina, 24-09-2026**, sobre la sección LinkedIn de EBEMA:

1. **«Retocada» = foto real como base + imagen nueva con IA que se vea más estética.**
   Se pueden crear escenas nuevas, pero siempre partiendo de las fotos reales de la
   sucursal (entran como `--refs`): la fachada, la bodega y el lugar tienen que
   reconocerse. No es un retoque de color ni una escena inventada de cero.
2. ⛔ **Nunca rostros de trabajadores** en las imágenes de LinkedIn. **Por qué:** EBEMA
   rota personal con frecuencia y las fotos pueden ser antiguas; alguien que ya no
   trabaja ahí no puede aparecer como cara de la sucursal.

**Cómo aplicar:** personas sólo de espaldas, fuera de foco, recortadas o sin cara;
escribirlo en el prompt («sin rostros visibles») y revisar cada imagen antes de
entregar. Fotos base: Drive `3-fotos/fotos_sucursales/<sucursal>/` (IDs en
[[material-diseno-paulina-drive]]). Referencias de pieza: `2-referencias/linkedin/`.
Regla parecida en otra marca, pero independiente: [[between-sin-rostros-de-modelos]].

**Paulina, 25-09-2026** (grilla LinkedIn octubre):
- En video/reel también rige: **nadie mira a cámara**; personas **de perfil o de espaldas** están OK.
- El «POST LINKEDIN» del 15/10 (crecimiento CChC 15,5 %) es **una sola imagen estática**, aunque el brief traiga T1–T4.
- Las referencias de carrusel LinkedIn (`2-referencias/linkedin/carrusel/c_{ebema-1,ebema-2,click,stock}`) usan la **misma gramática que el carrusel de feed** (logo en esquina, versales + caja roja, cápsula blanca); cierre = foto desenfocada + «Gracias al equipo de…» + anillo EBEMA grande al centro.
- ⚠️ El conector Drive se cae («session expired») si se bajan varias imágenes en paralelo con download_file_content: ir de a una. Videos de 300 MB no pasan por el conector.
- ⛔ **Kling (image-to-video) inventa letreros de marcas falsas** si el prompt pide travelling o paneo: rellena lo que está fuera de la foto. En sucursales, sólo acercamientos rectos («la cámara sólo avanza») y revisar el ÚLTIMO cuadro. Pasó en la bodega de Talca, 25-09.
- La gramática medida del reel de saludo de sucursal está en `clients/ebema/CLAUDE.md` § LinkedIn — reel de SALUDO DE SUCURSAL.
- ⭐ **Lo que no existe en foto se GENERA con la estética real de EBEMA** (Paulina, 25-09): si falta un camión, un despacho o una escena, se toma de referencia una foto real de bodega o patio de sucursal (`--refs`) y se le AÑADE el elemento. Así hizo ella las imágenes de las referencias de carrusel LinkedIn (camiones con la marca, bodegas). No se bloquea por «falta la foto».
- Antes de decir que falta material, revisar TODAS las carpetas `fotos_sucursales/<sucursal>` de Drive (no sólo la que ya está bajada).

**Ronda 1 LinkedIn octubre (Paulina, 25-09) — reglas que valen para toda imagen EBEMA:**
- ⛔ **No se crean estructuras que no existen** (naves, edificios, obras dentro del patio). Sobre la foto real SÓLO se añaden **personas, vehículos y materiales**, a criterio. «A cliente eso no le gusta». Una obra al lado de una bodega se lee como «la construcción está dentro del patio de EBEMA».
- ⛔ **Personal de oficina = ropa formal de oficina** (pantalón de vestir y camisa). El uniforme azul con reflectante es sólo de bodega/patio.
- La imagen tiene que tener **iluminación y enfoque comercial**; una foto real plana o con sombras duras se reemplaza aunque sea de la sucursal correcta.
- El texto va donde la foto está despejada (cielo, cielo raso); Paulina prefiere el bloque ARRIBA cuando hay cielo libre.
