# COPYWRITERS · Grupo Copylab — manual de la cuenta propia

> **Antes de tocar una pieza:** lee
> [`creative-system/COPYWRITERS_CREATIVE_OS.md`](../../creative-system/COPYWRITERS_CREATIVE_OS.md).
> Este archivo es el resumen operativo; el sistema completo está allá.

**Ámbito:** la cuenta `@copywriters.cl`. **Este criterio no se traspasa a ningún
cliente**, igual que el de Paulina no cruza a Hilton (regla del estudio,
`docs/SISTEMA-DE-MARCAS.md`). Que sea la cuenta de la casa no la hace un caso
especial.

**Firma el criterio:** Valeria Traverso.

---

## La regla madre

**Copywriters no tiene una plantilla. Tiene criterio.**

La consistencia sale de tipografía, dirección de arte, tratamiento fotográfico,
paleta, tono, composición, intervención y jerarquía. **No de repetir el mismo
layout.** Dos piezas seguidas pueden ser completamente distintas y seguir
pareciendo Copywriters.

Si el feed empieza a parecer un template de Instagram, el sistema falló.

---

## Producir una pieza

```
INSIGHT → IDEA → 3 RUTAS → CONCEPTO → DIRECCIÓN DE ARTE
       → FORMATO → COPY → IMAGEN → DISEÑO
```

**Una pieza = un archivo** en `src/compositions/copylab/`, con su dirección de
arte escrita en la cabecera. No existe una composición genérica con un prop
`plantilla`, y esa ausencia **es** el sistema.

```bash
# Registrar en src/Root.tsx como CL-<Nombre> y renderizar
./node_modules/.bin/remotion still CL-Signal out/copylab/v2/01-signal.png \
  --browser-executable="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# La compuerta. Una pieza que no pasa, no se muestra.
python3 qa/motor.py --marca copywriters out/copylab/v2/*.png
```

⚠️ En este Mac hace falta el sandbox fuera de iCloud: memoria
`render-remotion-fix-mac`.

---

## Los cinco topes que más se rompen

1. **Una anomalía fuerte por pieza.** No dos.
2. **1–2 intervenciones a mano**, cada una con razón semántica. No decorar: intervenir.
3. **El logo NO va por defecto.** En el lote v1 aparece en 1 de 9.
4. **El rosa es firma, no relleno.**
5. **Ningún dato inventado en una pieza PROOF.**

---

## Errores ya cometidos (03-09-2026) — no repetirlos

| Qué pasó | Qué aprendimos |
|---|---|
| El remate rosado de METÁFORA caía sobre gris medio y a tamaño de feed desaparecía | El velo sobre foto no ambienta: **deja leer**. Si hace falta 90% de velo, la foto está mala |
| La cifra de PROOF se desbordaba 15 px y la fractura se leía como error de render | Una caída de 52 px con deriva lateral separa el trozo; 24 px sin deriva lo **fractura** |
| El «0:14» del cover quedó 30 px bajo la interfaz de Instagram | En 9:16 el margen derecho de esta marca es **155 px**, no 80 |
| La lámina 03 del carrusel se salía 41 px | Bajarle el cuerpo sólo a esa lámina la deja más chica que sus hermanas. Lo correcto fue **reescribir el copy** para que las tres midan lo mismo |
| La primera imagen de la metáfora invirtió el concepto | Cuando una generación falla no faltan adjetivos: **falta una decisión de cámara** |
| La primera generación de G.CL traía el anillo de audífonos rojo | La biblia manda **coral**. No se arregla en post: se regenera |

---

## Lo que el QA NO puede comprobar

Que el remate rosado se lea. Se intentó automatizar con dos métricas distintas y
ninguna separa el control malo de las piezas buenas — el detalle del experimento
está escrito en `reglas.yaml`. **Es un punto de revisión humano.**

Y, por supuesto, si la idea es buena. Eso lo decide el CREATIVE SCORE.
