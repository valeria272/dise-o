# Landera — kit de plantillas digitales

Fuentes en este directorio; salidas en `out/landera/plantillas/`.

```bash
cd clients/landera/plantillas
./render.sh feed-cifra 1080 1080 story-cifra 1080 1920 linkedin-portada 1584 396
```

| Pieza | Medida | Para qué |
|---|---|---|
| `feed-cifra` | 1080 × 1080 | Post de dato — la cifra manda |
| `feed-titular` | 1080 × 1080 | Post de mensaje, fondo tinta |
| `feed-foto` | 1080 × 1080 | Post sobre fotografía, con velo |
| `story-cifra` | 1080 × 1920 | Historia — respeta la zona segura |
| `linkedin-portada` | 1584 × 396 | Encabezado de la página de empresa |
| `banner-web` | 1920 × 480 | Cabecera del sitio |
| `presentacion-01…04` | 1920 × 1080 | Las 4 maestras: portada, sección, contenido, cifra |
| `firma-correo.html` | — | **El entregable es el HTML**, no una imagen |

## La firma de correo

Va en tabla, no en flex: los clientes de correo no soportan CSS moderno.

⚠️ **Apunta a `https://landera.cl/img/logo-landera.png`, que todavía no existe.**
Hay que subir el PNG del kit (200 px de ancho, su mínimo digital) y dejar esa URL
viva antes de repartir la firma. `firma-correo-vista.html` es sólo la vista previa
local — esa no se reparte.

## Lo que estas plantillas respetan

- La franja de remate con el ritmo de la lámina 14: hueco fijo, franja viva.
- El logotipo nunca bajo su mínimo (200 px digital).
- Crema o tinta de fondo; el terracota sólo como acento.
- Sobre fotografía, velo hasta llegar a 4,5:1 (lámina 11).

⚠️ **Los textos son de ejemplo.** Las cifras son ilustrativas y la fotografía es
generada: reemplazar por material real antes de publicar.
