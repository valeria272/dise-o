---
description: Abre el sistema de diseño de un cliente nuevo — /marca-nueva <nombre>
---

Abre el sistema de diseño de la marca en `$ARGUMENTS`, siguiendo la §7 de
`docs/SISTEMA-DE-MARCAS.md`. Es una vuelta larga y no se puede acortar: un sistema
inventado cuesta más caro que no tener sistema.

## 1. Preparar
```bash
cp -r clients/_PLANTILLA clients/<slug>
mkdir -p raw/<slug>/ref public/assets/<slug>
```

## 2. Conseguir material real — sin esto no se sigue
Necesitas, como mínimo:
- **20–60 piezas aprobadas** de la diseñadora del cliente (feed, story, carrusel)
- Los **logos oficiales** en PNG con transparencia, en todas sus versiones
- Los **archivos de tipografía** reales (o el nombre exacto y quién tiene la licencia)
- Si existe: manual de marca, editables `.ai` empaquetados, banco de imágenes
- Si hay e-commerce: la URL y qué plataforma es

Si falta algo, anótalo en `CHECKLIST-CLIENTE.md` y sigue con lo que haya —
pero deja explícito qué quedó sin verificar.

### 2.b Compuerta — verificar que el material ENTRÓ (no se salta)

Bajar no es tener. Una descarga fallida de Drive deja un HTML de login guardado
con extensión `.jpg` que pesa 900 KB y parece una foto. Así se diseñó Revex
completo sin ver una sola referencia (25-08-2026).

```bash
/Users/Vale/copylab-venv/bin/python3 scripts/verificar-material.py raw/<slug>
/Users/Vale/copylab-venv/bin/python3 scripts/hoja-contacto.py raw/<slug> \
    out/_verificacion/<slug>-material.png
```

1. Si `verificar-material.py` marca algo roto, **vuelve a bajarlo**. No se sigue.
2. Abre la hoja de contacto y **mírala**: ¿son todas de esta marca? Ese mismo día
   la carpeta de referencias de Casablanca tenía 13 piezas de Between, la
   cafetería, y la dirección de arte se replanteó contra ellas.
3. Muéstrale la hoja de contacto a quien pidió el trabajo, con el conteo de piezas
   válidas, **antes** de escribir el manual.

## 3. Estudiar — verlas una por una
No resumas: **describe**. Por cada grupo de piezas, anota dónde va el logo, el
titular, la bajada, el CTA; qué se apila y qué no; qué cambia entre feed y story;
qué registros distintos existen (producto / sucursal / promo / editorial).

Busca la **regla madre**: la frase que resume qué hace que esta marca se vea como
esta marca y no como otra.

## 4. Medir — no estimar
- **Colores:** muestrear píxel a píxel con PIL sobre las piezas reales. Si hay tonos
  parecidos, verificar si son el mismo o no (en Revex hay tres rojos distintos).
- **Geometría:** medir en px, normalizando a 1080 de ancho.
- **Tipografías:** identificar contra los editables o el informe del `.ai`.

## 5. Escribir
Llena `clients/<slug>/CLAUDE.md` y `marca.json` con lo medido. Todo valor lleva su
origen. Nada de "aproximadamente".

## 6. El examen de admisión
**Reproduce desde cero una pieza que el cliente ya aprobó**, usando sólo el sistema
que escribiste. Ponlas lado a lado. Si no queda idéntica, el sistema está mal —
vuelve al paso 3. Este paso no se salta.

## 7. Cerrar
- Llena `CHECKLIST-CLIENTE.md` con todo lo que faltó
- Crea `src/brand/<slug>.ts` si la marca va a llevar video
- Agrega la marca a `docs/ESTADO-MARCAS.md` con su madurez real
- Agrega el puntero en `CLAUDE.md` de la raíz
