# MyZoo · grilla octubre 2026 — estáticos «Por diseñar»

> Producido por el estudio el 22-09-2026 para revisión de Valeria y de Paulina,
> que es la diseñadora de la cuenta. **Todavía no está subido al Drive ni al portal.**
> Fuente: «MyZoo | Grilla Octubre 2026», hoja «Grilla Octubre ». Salen las 4 columnas
> con estado «Por diseñar» y «ok» del cliente en COMENTARIOS CLIENTE TEXTO.
> Las demás piezas estáticas siguen «En revisión» y varias tienen cambios pedidos
> por el cliente.

| Archivo | Fecha | Formato | Col. |
|---|---|---|---|
| `01.10_post_repelente.png` | 01-10 | Post 2250×2813 (4:5) | C |
| `02.10_storie_preguntazoo.png` | 02-10 | Story 2250×4000 (9:16) | D |
| `05.10_post_mercadolibre.png` | 05-10 | Post 2250×2813 | G |
| `08.10_post_crueltyfree.png` | 08-10 | Post 2250×2813 | I |

`_revision/02.10_storie_preguntazoo_CON-STICKER.png` muestra dónde cae la caja de
preguntas de Instagram. **No se publica**: la caja la pone el CM al subir la story.

Van en 2250 px de ancho con la nomenclatura de Paulina: fecha primero, minúscula y guion bajo.

## De dónde sale cada texto (todo literal de la grilla)

- **01-10:** en la placa del gabinete, «ROMPER EN CASO DE PASEO» + huella. Titular: «ANTES DE SALIR, / PROTÉGELO». Bajada: «Haz de la prevención parte de cada paseo». Etiqueta: «Espuma Repelente de Insectos para Perros MyZoo». Lleva logo y «Amor que se siente».
- **02-10:** sello PREGUNTAZOO. Titular: «¿Qué te gustaría preguntarle a nuestra experta?». Bajada: «Baño, pelaje, frecuencia de lavado, productos, rutinas de cuidado… Déjanos tu duda y podría ser respondida en nuestro próximo Reel».
- **05-10:** titular «¡MYZOO LLEGA A TODO CHILE!». Bajada: «De norte a sur, tus favoritos MyZoo más cerca de ti». Llamado: «ENCUÉNTRANOS EN MERCADO LIBRE».
- **08-10:** titular «CUIDARLOS TAMBIÉN ES ELEGIR RESPONSABLEMENTE». Sello Te Protejo, más «MyZoo es Cruelty Free» y «Certificados por ONG Te Protejo».

## Decisiones que hay que validar

1. **Sin punto final.** El brief los trae, pero el cliente pidió el 27-08 que las piezas vayan sin punto. Los emojis 🐾 y 💚 no van en el arte: el 🐾 lo reemplaza la huella del claim oficial y los emojis quedan en el copy.
2. **Logo con «Amor que se siente» debajo** en las 4, legible y no «enano». Sale del comentario del cliente del 01-08 y de los 4 briefs. En septiembre las piezas iban sin claim.
3. **El sello PREGUNTAZOO no existe.** Busqué en el Drive y no hay ningún logo de la sección. El que va es una **propuesta** armada con piezas del sistema: pastilla negra como el círculo del logo, «ZOO» en el amarillo del logo y la huella. Hay que aprobarlo o reemplazarlo.
4. **La veterinaria es generada.** El brief dice «ojalá sea la que ocuparemos». Cuando exista una foto de ella, se reemplaza.
5. **Mercado Libre:** la camioneta va **sin logo**, porque la IA no dibuja marcas de terceros, y el mapa de Chile es ilustrado a partir de la silueta real. Si se quiere el logo oficial de Mercado Libre en el llamado, hay que conseguir el archivo.
6. **Cruelty Free:** sobre el fondo amarillo, el titular y la bajada van en tinta, porque el blanco no se lee. La franja coral se mantiene.

## Cómo se hizo (para reproducir)

- **Escenas:** `scripts/myzoo-oct-escenas.py`, con Nano Banana Pro.
  - La IA hace la escena. Todos los **productos son los packshots reales** montados por código; donde va un envase, la IA dibujó uno liso de relleno que después se borra.
  - Para que el sujeto quedara bajo el titular hubo que achicar la escena y rellenar el fondo que faltaba (`outpaint`): ni el prompt ni un boceto de diagramación lo lograron.
- **Armado:** `scripts/myzoo-oct-armar.py`, en PIL con Neutraface Text, que es la tipografía de los editables. Las fuentes están en `public/assets/fonts/myzoo/`.
- **Material:** `raw/myzoo/`. Tiene 23 referencias digitales publicadas, packshots, logos, `feedback-cliente.md` e `INVENTARIO.md`.
