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
| `story-cifra` | 1080 × 1920 | Historia de dato — respeta la zona segura |
| `story-titular` | 1080 × 1920 | Historia de mensaje, fondo tinta |
| `story-foto` | 1080 × 1920 | Historia sobre fotografía, con velo |
| `fondo-pc-crema` · `fondo-pc-tinta` · `fondo-pc-patron` | 1920 × 1080 | Fondos de escritorio corporativos (lámina 24). Logotipo abajo a la derecha, lejos de los íconos |
| `linkedin-portada` | 1584 × 396 | Encabezado de la página de empresa |
| `banner-web` | 1920 × 480 | Cabecera del sitio |
| `presentacion-01…04` | 1920 × 1080 | Las 4 maestras: portada, sección, contenido, cifra |
| `banner-web-hero` | 1920 × 640 | Cabecera del sitio, foto con velo |
| `banner-web-seccion` | 1920 × 320 | Encabezado de sección, tinta con franja |
| `banner-linkedin-post` | 1200 × 627 | Publicación de LinkedIn |
| `firma-01…04` | — | **El entregable es el HTML**, no una imagen. Cuatro cargos |

## Las firmas de correo

Cuatro archivos, una sola plantilla. Lo único que cambia es el cargo y qué bajada
del logotipo le toca: **Farmland Management** para quien le habla al inversionista
(gerencia, inversiones) y **Gestión Agrícola** para quien opera en terreno
(operaciones, campo).

Van en tabla, no en flex: los clientes de correo no soportan CSS moderno.

⚠️ **Apunta a `https://landera.cl/img/logo-landera.png`, que todavía no existe.**
Hay que subir el PNG del kit (200 px de ancho, su mínimo digital; el `width` del HTML se corrigió de 150 a 200 el 05-09) y dejar esa URL
viva antes de repartir la firma. Los `vista-firma-*.html` son sólo previsualizaciones
locales — esas no se reparten.

## Lo que estas plantillas respetan

- La franja de remate con el ritmo de la lámina 14: hueco fijo, franja viva.
- El logotipo nunca bajo su mínimo (200 px digital).
- Crema o tinta de fondo; el terracota sólo como acento.
- Sobre fotografía, velo hasta llegar a 4,5:1 (lámina 11).

⚠️ **Los textos son de ejemplo.** Las cifras son ilustrativas y la fotografía es
generada: reemplazar por material real antes de publicar.
