---
name: ebema-sistema-diseno
description: EBEMA como implementación de referencia del sistema de marcas — dos marcas, tres esquemas, geometría medida y pipeline que rinde desde clients/ebema/sistema/
metadata:
  type: project
---

`clients/ebema/` es la marca modelo del método [[sistema-de-marcas]] (25-08-2026):
manual, `marca.json`, checklist de cliente, `sistema/` con el pipeline de producción
y `src/brand/ebema.ts` para reels.

**Dos marcas, tres esquemas** que no se mezclan: EBEMA sucursal (marco blanco +
puntitos + píldora de ciudad + `Cotiza por WhatsApp`), EBEMA CLICK (sin marco,
lockup centrado, columna al lado de la persona, `Regístrate Gratis`) y SPC/cerámicas
(sin marco, contenido anclado bajo el logo).

Datos verificados contra los archivos reales, no de memoria:
- **El rojo es `#EC1C23`** — muestreado del logo oficial y de la pieza A3 de Paulina.
  El `#ED1C24` que circuló en los mailings de agosto **está mal**.
- Gris `#6D6F72`. Raleway (Black/ExtraBold/SemiBold/Regular) + **Helvetica Bold
  obligatorio en TODA cifra** (la función `num()` lo hace solo).
- Artboard del kit oficial: 1200×1643. Feed 1080×1350 (4:5), story 1080×1920.

El sistema calibrado (v8, réplica 1:1 del esquema de agosto de Paulina) se promovió
desde `EBEMA/outputs/20260820_paid_septiembre/editables/` a
`clients/ebema/sistema/` (`base.css` + `render.sh` + `build_ejemplo.py` + fonts + img).
**Verificado el 25-08:** copiado a un sandbox limpio genera los 34 HTML y rinde las
piezas idénticas a las aprobadas.

**Why:** era el cliente con el sistema más fiel a lo que hace su diseñadora, pero
vivía enterrado en una carpeta de outputs con fecha — irrepetible el mes siguiente.

**How to apply:** para un mes nuevo se copia `clients/ebema/sistema/` y se cambian
**sólo las listas de texto** de `build.py`. Si falta algo en `base.css`, primero
verificarlo contra una referencia aprobada; si es legítimo, agregarlo al CSS y
documentarlo en el manual — nunca con `style=""` suelto.

**Pendiente con el cliente:** faltan fotos reales de **Chillán, Rancagua y San
Bernardo** (3 de 11 sucursales, hoy con pasillo IA), acceso de Drive para las 4
cuentas del equipo y confirmar la voz del locutor de reels.
