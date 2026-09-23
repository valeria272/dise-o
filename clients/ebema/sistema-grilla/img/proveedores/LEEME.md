# Logos de los proveedores de EBEMA

Estos son los logos que van en la **cápsula de co-marca** de la portada de todo
carrusel de familia A: `EBEMA ⊕ <proveedor>`, pegada al borde izquierdo.

> 📥 **Tú no tienes que dejarlos acá.** Déjalos en
> [`raw/ebema/3-logos-y-packshots/`](../../../../../raw/ebema/3-logos-y-packshots/),
> que es la carpeta de material del LEEME de la marca. Yo los verifico, les dejo
> el fondo transparente y los copio acá.
>
> **Por qué existe esta carpeta aparte:** `raw/` está en `.gitignore`. El material
> fuente no viaja al repo, así que un logo que viva sólo ahí no le llega a ninguna
> otra diseñadora y se pierde en un traspaso por ZIP. Sin el logo, la pieza no se
> puede volver a renderizar. Por eso la copia de trabajo vive acá, versionada.

## Cómo tienen que estar

| | |
|---|---|
| Formato | **PNG con transparencia**. Si viene `.ai`, `.eps` o `.svg`, mejor todavía: se exporta acá |
| Alto | **300 px como mínimo** — en la cápsula se usa a 86 px de alto sobre 1080, o sea 179 px reales en la entrega a 2250 |
| Recorte | pegado al contenido, **sin margen blanco alrededor**. Un margen dentro del archivo descuadra la cápsula, que es justo el error que se corrigió el 15-09 con el anillo de EBEMA |
| Color | el oficial del proveedor, sin recolorear |
| Nombre | `logo_<proveedor>.png`, minúscula y sin tildes: `logo_cintac.png`, `logo_novoplast.png` |

`build_carrusel.py` lo toma con una sola línea:

```python
"proveedor_logo": "img/proveedores/logo_masisa.png",
```

## Los que faltan

Salen de las grillas de septiembre y octubre 2026. Los marcados son los que ya están.

- [x] **Masisa** — ⚠️ recortado de una pieza publicada (portada del carrusel de
      junio 2026), no del kit oficial. Conviene reemplazarlo por el vectorial.
- [ ] Cedral *(Pizarreño / Romeral)*
- [ ] Metalcon Cintac
- [ ] Novoplast
- [ ] Surpol
- [ ] Morteros Toro
- [ ] Polpaico
- [ ] CMPC
- [ ] VH *(línea Galvatec)*
- [ ] Forestal Yukon
- [ ] Volcán *(Volcanita)*
- [ ] Etersol
- [ ] CBB
- [ ] Aza *(Perfiles Estrella)*
- [ ] LP *(tableros OSB)*
- [ ] San Juan
- [ ] PointFix
