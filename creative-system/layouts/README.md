# LAYOUTS — arquitecturas, no plantillas

Acá no hay componentes de layout. Es deliberado: un componente `<PostConFoto>`
es una plantilla con otro nombre.

Lo que hay son **arquitecturas de composición** que el sistema usa, y el criterio
para elegir una. Se elige por lo que la idea pide, nunca por defecto.

| Arquitectura | La idea que la pide | Ejemplo |
|---|---|---|
| **Tipografía a sangre** | La frase es la pieza | `Signal` · `ReelCover` |
| **Bloque + aire negro** | La declaración necesita silencio alrededor | `Signal` (45% del lienzo vacío arriba) |
| **Texto en la banda oscura de la foto** | La imagen carga la idea y el texto la nombra | `Metafora` |
| **Asimétrico 50/50** | Hay un objeto que mirar y algo que decir | `Work` |
| **Objeto tipográfico** | El dato ES la imagen | `Proof` |
| **Imagen sola + anotación** | Documental. Titular sería convertirlo en campaña | `People` |
| **Pila degradada** | El argumento está en la repetición | `TypeLab` |
| **Alternancia de fondo** | Secuencia: el cambio da pulso | `Carrusel` |

## Las herramientas de composición

En `src/brand/copylab/`:

- `<Bloque lineas={[…]} base={N}>` — cada línea decide voz, escala, ancho, peso,
  color y desplazamiento.
- `<Corte>` — un bloque macizo que parte el lienzo.
- `<Filo>` — un filete de 2 px que ordena sin dibujar una retícula visible.
- `<Velo>` — legibilidad sobre foto. Función, no ambientación.
- `<ZonaSegura>` — overlay de QA. **Nunca se exporta encendido.**

## Sobre la retícula

Margen base 80 px sobre 1080. **Punto de partida, no retícula.** Debe existir
aire, debe existir tensión, puede existir asimetría. Una pieza puede sangrar al
borde si el concepto lo pide.

## Sobre el ancho de medida

El sistema **no** escala el texto automáticamente para que quepa. Autoajustar es
lo que convierte un sistema en una plantilla: la escala es una decisión de
dirección de arte.

El que atrapa un desborde es el QA (`respiro-borde` de agencia), y el que lo
arregla es una persona — bajando el cuerpo, rebreakeando la línea o, muchas
veces la mejor salida, **reescribiendo el copy**.
