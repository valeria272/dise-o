# Qué tiene que hacer cada persona para arrancar

> Estado al **25-08-2026**. Ordenado por quién debe actuar, no por marca.
> Lo marcado 🔴 bloquea trabajo; 🟡 lo hace más lento.

---

## 👤 Valeria — 4 cosas, y la primera destraba todo

| | Qué | Por qué |
|---|---|---|
| 🔴 1 | **Crear las cuentas `@copywriters.cl` de los 4 diseñadores en claude.ai** y darles acceso al Drive de la agencia | Sin esto no pueden ver material de clientes. Es el bloqueante #1 |
| 🔴 2 | **Mandarles el ZIP** (`bash scripts/empaquetar.sh` → queda en tu Escritorio) | — |
| 🟡 3 | Decidir si se compra la licencia de **Cherolina** (~USD 20–40) | **Probablemente no hace falta**: Brushwell + el truco del signo volteado ya cubre el 100 % del español |
| 🟡 4 | Feedback de **Revex y Casablanca** que quedó pendiente | Son 2 de las 5 marcas cerradas; si algo está mal, mejor corregirlo antes de que los diseñadores produzcan sobre eso |

---

## 👤 Cada diseñador — día 1

Sigue [`LEEME-PRIMERO.md`](../LEEME-PRIMERO.md), que asume que no tienes nada instalado.

```
[ ] Instalar Chrome, Node.js, VSCode y Claude Code
[ ] Entrar a claude.ai con tu cuenta @copywriters.cl
[ ] Settings → Connectors → activar Google Drive          ← imprescindible
[ ] Descomprimir el ZIP en ~/copylab/  (NUNCA en Escritorio ni Documentos)
[ ] Abrir la carpeta en VSCode → Terminal → escribir: claude
[ ] Escribir: /arranque
```

Después, cada vez que te sientes a trabajar:
```
/al-dia                 ← primero, siempre
/pieza <marca> <qué>
/qa <marca>
```

### Si te toca Tierra Calma
Activa **IvyOra** en tu Creative Cloud (Adobe Fonts). No viene en el ZIP: su licencia
es por asiento. Sin activarla, cae a Instrument Serif y se ve distinto.

### Si te toca CAVA
Activa **Bebas Neue Pro** y **Brandon Grotesque** en tu Creative Cloud. La Bebas Neue
libre viene en el ZIP y sirve para maquetar, pero la entrega final usa la Pro.

### Si te toca Selfie
Necesitas **Agrandir** (de pago, licencia del cliente). Pídesela a Coni.

---

## 👤 Constanza Lizana «Coni» — 4 cosas

| | Qué | Para qué |
|---|---|---|
| 🔴 1 | **Un editable empaquetado de CAVA de cualquier mes** | Ya tengo el KV y el banner, pero no un mailing. Con eso queda cerrada al 100 % |
| 🔴 2 | **10–20 piezas digitales aprobadas de MyZoo** | Tengo el envase medido y completo, pero **la gramática digital no está** |
| 🟡 3 | El archivo de **Agrandir** para el equipo, o confirmar cómo se licencia | Selfie no se puede producir sin ella |
| 🟡 4 | Los **RGB equivalentes** de los 3 Pantone de MyZoo (114 C, 708 C, Neutral Black C) | Para que el digital calce con el envase |

También: **«Agregar acceso directo a Mi unidad»** en `Diseños EDITABLES` y `CONI`.
Hoy llego a tus archivos buscando por dueño, pero con el acceso directo entran al índice
y es directo.

---

## 👤 Elisabet Soto «Eli» — 3 cosas

| | Qué | Para qué |
|---|---|---|
| 🔴 1 | **Cuál de las 9 scripts va en qué caso** | Tu editable declara Brushwell, Kallimata, Canvas Script, Allura, Backstroke, Pacifico, Brush Script MT, Forte y MV Boli. Uso Brushwell como principal, pero no sé cuándo entran las otras |
| 🟡 2 | Las paletas de **QB** y **Piso 18** (o los `.ai` en una carpeta que pueda leer) | Son 2 marcas activas del complejo, sin sistema |
| 🟡 3 | Confirmar la licencia de **Stag LCG** (DoubleTree) | Es de pago |

**Gracias por la carpeta `GRILLA IA BETWEEN`** — con eso Between quedó con el ADN más
completo de todas las marcas: Brushwell instalada, márgenes medidos, tus reglas de foto
codificadas y las ilustraciones vectoriales en el repo.

---

## 👤 Paulina Bustamante — 2 cosas (EBEMA)

| | Qué | Para qué |
|---|---|---|
| 🔴 1 | **Fotos reales de Chillán, Rancagua y San Bernardo** | 3 de 11 sucursales van con pasillo IA genérico. Pedidas desde el 20-08 |
| 🟡 2 | Los **editables `.ai` de las piezas de sucursal** | Solo tengo el de Ebema Click. Con los de sucursal mido la geometría en vez de deducirla |

---

## 👤 KAMs (Serena, Constanza Olivares, Ámbar, Carlos) — 1 sola cosa

**Que el brief llegue con el formato de Serena.** El «Brief Diseño Septiembre 2026 —
REVEX» es el modelo: por pieza trae formato, objetivo, botón, material, qué se ve en la
imagen, antetítulo/título/bajada/CTA separados, y lineamientos numerados.

Con un brief así se produce **sin una sola pregunta de vuelta**. Sin él, son 3–4 rondas.
El formato está en [`BRIEF-DE-DISENO.md`](BRIEF-DE-DISENO.md).

Lo mínimo que no se puede omitir:
```
[ ] Marca y qué pieza es
[ ] Formato y medidas exactas
[ ] Los textos FINALES (antetítulo / título / bajada / CTA)
[ ] Qué se ve en la imagen, o qué archivo usar
[ ] Objetivo y botón del anuncio
[ ] Si hay promoción: precio, vigencia y legal exacto
[ ] Dónde se sube la entrega
```

Y una cosa más: **pedirle al cliente que comente en los archivos de Drive**, no por
WhatsApp. Los comentarios de Drive se leen automáticamente y quedan trazables.

---

## 🔴 Lo único que falta probar de verdad

**Correr `/arranque` en un Mac que no sea el de Valeria.** Todo está verificado en
simulación —descomprimí el ZIP en una carpeta limpia y el sistema de EBEMA rindió
idéntico— pero **nadie lo ha hecho todavía en otra máquina**. Hasta que eso pase, el
traspaso está probado en teoría.

Es la primera tarea del primer diseñador que entre.

---

## Dónde está cada marca hoy

| Marca | Se puede producir | Qué falta |
|---|:--:|---|
| **EBEMA / Click** | ✅ | fotos de 3 sucursales |
| **Revex** | ✅ | nombre real de la script; foto vitrina Temuco |
| **Casablanca** | ✅ | confirmar la serif itálica oficial |
| **Selfie** | ✅ | Agrandir; logo de Selfie Class |
| **Between** | ✅ | cuál script en qué caso |
| **Tierra Calma** | ✅ | activar IvyOra en cada máquina |
| **CAVA** | ✅ | un editable de mailing; acceso a bottle shots |
| **MyZoo** | ⚠️ envase sí, digital no | piezas digitales aprobadas |
| **Abakos** | ⚠️ | gramática sin medir — faltan piezas aprobadas |
| Nueva Urbe · Traverso · QB · Piso 18 · y 11 más | ❌ | vuelta completa de `/marca-nueva` |

**7 marcas listas para producir hoy.** El detalle completo, en
[`ESTADO-MARCAS.md`](ESTADO-MARCAS.md).
