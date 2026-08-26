---
name: direccion-de-arte
description: Criterio de dirección de arte para piezas de cliente del estudio COPYLAB. Cómo leer una referencia, cómo decidir cuando el brief no alcanza, qué hace que una pieza sea buena o vergonzosa, y cuándo parar en vez de producir. Úsala en toda pieza de marca — antes de armar y antes de entregar.
---

# Dirección de arte — el criterio, no la ejecución

`/pieza` dice **cómo se produce**. Esta skill dice **cómo se decide**. Las dos se
usan juntas: la ejecución sin criterio es lo que produjo, en agosto de 2026, tres
cuentas rehechas 3 y 4 veces cada una.

---

## 0. La pregunta que se contesta primero

> **¿Tengo con qué hacer esta pieza bien?**

Si la respuesta es no, **la respuesta correcta es decirlo, no producir algo peor.**
Una pieza entregada con material malo cuesta más que una pieza no entregada: gasta
la confianza del cliente y obliga a rehacer.

Antes de armar nada:

```bash
python3 scripts/verificar-material.py raw/<marca>
python3 scripts/hoja-contacto.py raw/<marca> out/_verificacion/<marca>.png
```

Y **mira la hoja de contacto**. Dos preguntas: ¿son todas de esta marca?
¿reconozco la gramática? En agosto la carpeta de referencias de Casablanca tenía 13
piezas de una cafetería y la dirección de arte se replanteó contra ellas.

---

## 1. Leer una referencia: se mide, no se estima

Un rango descrito en palabras («titular entre 40 y 122») **no es una medida: es la
señal de que falta medir**. Cuando eso pasó en Between, el titular real era 97, se
usó 60, y la grilla completa de 27 piezas se cayó.

De cada referencia hay que sacar, en píxeles y normalizado a 1080 de ancho:

| Qué | Cómo |
|---|---|
| Colores | muestrear con PIL, píxel a píxel. En Revex hay **tres rojos distintos** |
| Cuerpo del titular | altura de mayúscula real sobre la pieza, no el nombre de un estilo |
| Posición de cada bloque | bbox sobre el canal alfa o sobre la máscara de tinta |
| Proporción entre elementos | titular ÷ bajada, logo ÷ ancho de pieza |

**Calibrar contra el propio render.** Brushwell sale ~20 % más ancha en Chrome que
en PIL. Renderiza, mide tu pieza con la misma máscara que usaste en la del
diseñador, y corrige hasta que la tinta calce.

### Qué referencia manda
```
1. El FEED PUBLICADO de la marca        ← el benchmark real
2. Las entregas terminadas del diseñador (carpetas de entrega semanal)
3. Los editables empaquetados (Informe.txt) ← ver /adn
4. El brief y su carpeta de referencias
```
Una marca puede tener **dos registros vivos a la vez**. Si los ves distintos, no
elijas en silencio: pregunta cuál manda para esta pieza.

---

## 2. La regla madre

> **El brief manda el QUÉ. El sistema de la marca manda el CÓMO.**

El brief trae datos, SKU, medidas, CTA, legales, vigencias — y esos van **literales**.
El sistema trae la gramática visual — y esa **se extiende, nunca se reinventa**.

Cuando el brief pide algo que el sistema no tiene («un bloque de datos separado»),
la respuesta correcta es **traducirlo a un elemento que ya existe** (la cápsula de
borde blanco, la caja gris), no inventar un elemento nuevo.

Cuando el brief y una instrucción nueva se contradicen: **se dice y se deja escrito
en el código**, no se resuelve en silencio.

---

## 3. Qué hace vergonzosa una pieza

Estas son las que de verdad pasaron. Cada una es una compuerta.

### 3.1 La foto
- ⛔ **Nunca estirar una foto para llenar un formato.** Repetir la última franja de
  píxeles hacia abajo produce **rayas verticales**: en la story de Revex Las Condes
  eso ocupó el **34 % de la pieza**. Si la foto es horizontal y la pieza es 9:16,
  las salidas son: recortar bien, buscar otra foto, o **decir que falta la foto**.
- ⛔ **Costuras.** Dos imágenes pegadas dejan un salto de brillo en una fila. Se
  detecta midiendo la diferencia media entre filas contiguas.
- ⛔ **Fondo oscuro e ilegible.** Un plano de local mal iluminado no es un fondo:
  es una excusa. Brillo medio bajo 40/255 en una zona grande = revisar.
- ⛔ **Elementos del fondo que chocan con el texto** — el logo del local detrás del
  titular, el letrero del vecino, gente sin derechos de imagen.
- ✅ La foto de ambiente es **protagonista**, no relleno. Si sobra espacio vacío en
  el tercio inferior, la composición está mal resuelta.

### 3.2 El texto
- ⛔ Más de 3 bloques apilados. Las referencias buenas tienen **texto mínimo**.
- ⛔ Textos o CTA inventados. Salen **literales del brief**.
- ⛔ Palabras solas en la segunda línea.
- ⛔ Botones dibujados dentro de la gráfica cuando la plataforma ya pone el suyo
  (WhatsApp en Meta). Si se sacó una vez, **no vuelve**.

### 3.3 La marca
- ⛔ Producto, logo o dato generados por IA. La IA hace **ambiente y fondo**, nunca
  el producto. Ver la jerarquía de imagen en `docs/SISTEMA-DE-MARCAS.md` §2.
- ⛔ Packshot espejado (deja la marca al revés), deformado o reescalado a ojo.
- ⛔ Cruzar ciudades o sucursales: la foto de Antofagasta va sólo en la de Antofagasta.
- ⛔ **Dos marcas hermanas con el mismo esqueleto y distinto color.** Revex y
  Casablanca son del mismo dueño y no se diseñan igual. Si una pieza de Revex se
  puede recolorear a gris y pasar por Casablanca, está mala.

---

## 4. Antes de mostrar

```bash
python3 scripts/ver-pieza.py out/<marca>/<periodo>     # míralas todas juntas
python3 scripts/ver-pieza.py out/<marca>/reel.mp4      # un video también se MIRA
```

Y el lado a lado que no se salta: **tu pieza junto a una aprobada del cliente**.
Si no se parecen, el sistema está mal — no la pieza.

Checklist duro:
- [ ] Zonas seguras Meta (`src/components/qa/SafeAreaAds.tsx`)
- [ ] Cero choques de texto con marcos, logos u otros elementos
- [ ] Cifras en la tipografía que la marca define para números
- [ ] Recortes revisados con zoom 3×; pelo suelto jamás recortado
- [ ] Precios en CLP chileno: `$9.900`, punto de miles, sin decimales
- [ ] Medidas exactamente las que pidió el brief. **Avisar no reemplaza cumplir**

---

## 5. Cuándo parar

Para y dilo — no produzcas — cuando:

1. El material no pasó la compuerta y no se puede rebajar.
2. La única forma de llenar el formato es estirar o inventar.
3. El brief pide un elemento que el sistema no tiene y no hay forma de traducirlo.
4. Dos instrucciones se contradicen y no sabes cuál manda.
5. La marca no tiene manual en `clients/` → hay que abrirla con `/marca-nueva`.

Decirlo cuesta un mensaje. No decirlo cuesta tres rondas.

---

## 6. Cerrar el ciclo

Toda corrección del cliente **se codifica en `clients/<marca>/CLAUDE.md` en el mismo
commit**. El manual es la memoria del estudio: lo que no queda escrito se vuelve a
equivocar. Y ojo — codificar sólo las reglas de texto y ninguna de imagen es
exactamente cómo Revex acumuló 30 feedbacks con el layout correcto y la foto rota.
