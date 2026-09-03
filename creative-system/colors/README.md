# COLORS

```
#080F14   NEGRO TINTA     fondo por defecto · tinta sobre claro
#F2F4F6   OFF WHITE       fondo claro · el respiro de la grilla
#FFFFFF   BLANCO          tipografía sobre tinta
#FF2D8D   COPY PINK       LA FIRMA
#FF683D   CORAL           secundario, con moderación
#9D4EDD   PÚRPURA         secundario, con moderación
```

## La regla del rosa

**Firma, no relleno.** Una palabra, una intervención, un objeto, una línea, un
detalle, una anomalía.

Puede existir una pieza completamente rosa **cuando el concepto lo justifique**.
En el lote v1 es una de nueve.

## Fondos posibles

Cuatro, y los cuatro planos: tinta · off-white · blanco · rosa.
**Ningún gradiente de fondo.** El único degradado del sistema es el *velo*, y
existe para que el texto se lea sobre una foto — es una función, no un adorno.

Si una pieza necesita un velo al 90% para funcionar, la foto elegida está mala:
se cambia la foto, no se sube el velo.

## Comprobación por programa

`clients/copywriters/reglas.yaml → color-fuera-de-sistema` (bloqueante).

Los topes están calibrados contra un control, no puestos a ojo: inyectando un
azul SaaS `#5B6CFF` sobre una pieza real, la comprobación devuelve **100% fuera**;
las trece piezas del lote quedan entre **0% y 12,8%**. Tope: 18%.
