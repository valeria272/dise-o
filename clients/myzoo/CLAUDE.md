# MYZOO — manual de marca

> **Cliente:** MyZoo — cuidado y limpieza de mascotas (retail + profesional/groomer)
> **Cuenta:** always-on · **Diseño:** Constanza Lizana «Coni» + Paulina Bustamante
> **Ficha máquina:** `clients/myzoo/marca.json` · **Qué falta:** `CHECKLIST-CLIENTE.md`
> **Levantado el 25-08-2026** desde los editables de Coni y los PDF de marca.

Antes de diseñar, leer [`docs/SISTEMA-DE-MARCAS.md`](../../docs/SISTEMA-DE-MARCAS.md).

---

## 1. Qué es la marca

Línea chilena de shampoos, acondicionadores y desinfectantes para mascotas,
**desarrollada en Australia**. Vende en dos canales: consumidor final y
**groomer / clínica veterinaria** (formatos de 5 litros, diluibles).

**Bajada de marca:** **«AM♥R QUE SE SIENTE»** — el corazón reemplaza la O de AMOR.

### Líneas de producto
| Línea | Qué es | Dilución |
|---|---|---|
| **Avena Coloidal** | Shampoo + Acondicionador con vitamina E. Pieles sensibles, irritadas o con alergias | 1:2 |
| **Expert Care** | Shampoo de hidratación profunda. Aceite de argán, vitamina E, té verde | — |
| **Groomer Grade** | El mismo concepto en formato profesional | **1:10** |
| **Xtreme Vet** | Desinfectante de grado hospitalario para superficies clínicas | — |

### Packs
`Trío pet dog` · `Trío pet cat` · `Pieles Sensibles`
Las gráficas de pack llevan siempre **«**Imágenes referenciales**»**.

### Claims certificados — se pueden usar, son del cliente
Certificación **ONG Te Protejo (Cruelty Free)** · hipoalergénico · materias primas de
origen natural · libre de metales pesados · certificaciones internacionales ·
eco amigable, libre de cloro · libre de fosfatos · pH neutro · no tóxico.

Xtreme Vet además: elimina el **99 %** de los gases del mal olor · **99,9999 %** de
hongos, virus y bacterias · **99,9 %** del parvovirus.

> ⚠️ Los porcentajes y certificaciones son **claims regulados**. Van literales del
> catálogo del cliente, nunca redondeados ni reformulados.

---

## 2. ⭐ Son dos disciplinas distintas: envase y digital

**No se diseñan igual y no comparten especificación.** Antes de partir, definir cuál es.

| | **Envase / etiqueta** | **Digital (RRSS y pauta)** |
|---|---|---|
| Color | **CMYK + tintas planas Pantone** | RGB |
| Unidades | **milímetros** | píxeles |
| Mesa de trabajo | **140 × 160 mm** (etiqueta 5 L) | 1080×1350 · 1080×1920 |
| Tipografía | **Neutraface Text** + Roboto | por confirmar (ver pendientes) |
| Entrega | PDF de impresión + troquel | PNG |

### Envase — medido del editable `XTREME VET 5LTS.ai`
- **Mesa de trabajo:** 140 × 160 mm · modo **CMYK**, sin perfil
- **Tintas planas:** `PANTONE 114 C` · `PANTONE 708 C` · `PANTONE Neutral Black C`
- **Tipografías empaquetadas:** Neutraface Text — Light Italic, Demi Italic, Bold,
  Bold Italic (**es de pago**, viene en el paquete)
- **Tipografías de Adobe Fonts** (no vienen, hay que activarlas): Roboto Light,
  Medium, Bold
- Sin imágenes enlazadas: **el envase es 100 % vectorial**

> Las etiquetas de 5 L viven en Drive `ETIQUETAS 5 LITROS` →
> `EDITABLES TODAS LAS ETIQUETAS` (`1hdBjVE56ZA1BZ7v1oGJbMgRkV_Ig3Ncc`), un paquete
> `*_Carpeta` por SKU con su `Fonts/` y su `Informe.txt`.

### Packaging de packs
`PACK_MYZOO_ESSENTIALS` y `PACK_MYZOO_EXTRACARE`, cada uno con variante
**«OJOS AMARILLOS»** — hay dos versiones del arte según el color de ojos de la
mascota. Se entregan con **troquel**, **montaje** y **fichas técnicas**, y los
finales salen en PDF (`PACK_MYZOO_FINALEXTRACARE.pdf`, `PACK_MYZOO_FINALESSENTIALS.pdf`).

---

## 3. Dónde está el material

| Qué | Dónde |
|---|---|
| **Catálogo de productos** (PDF) | Drive `1COktMo0iu_mSNdGgyp-QJsMIPuab9XUq` |
| **Lanzamientos** (PDF, con los claims) | Drive `1LFXRPH1t7ZJX3TVSDScun3TKAYnWBufg` |
| Logo oficial | Drive `LOGO CLIENTES/MYZOO` → `12A2fADHDGLHuDW3XQmA2gV4FGNBa_I4a` |
| Editables de etiquetas 5 L | `1hdBjVE56ZA1BZ7v1oGJbMgRkV_Ig3Ncc` |
| Packs (troquel/montaje/fichas) | `1-LwGhwmPTolUuZsRUH3cTZQ6QeqCZsTc` |
| Editable de mailing | `myzoo_editable_mail.ai` — `1SZkt5VS6SA1DGkC6AhnI6_ssLVOYZIF1` |
| Editable petvet | `petvet_myzoo_editables.ai` — `1tcMhgZIfUlhvuVy54IDeNBab3kGjYZN8` |
| Imágenes del sitio web | ver memoria `myzoo-web-imagenes` — 46 imágenes mapeadas |

---

## 4. QA obligatorio

```
[ ] ¿Es envase o digital? Especificación correcta (CMYK+Pantone+mm vs RGB+px)
[ ] Claims y porcentajes LITERALES del catálogo del cliente
[ ] "**Imágenes referenciales**" en toda gráfica de pack
[ ] Dilución correcta por línea (Avena 1:2 · Groomer Grade 1:10)
[ ] Variante de ojos correcta si es pack (normal / OJOS AMARILLOS)
[ ] Logo del PNG oficial, nunca recreado
[ ] Si es impresión: troquel incluido y tintas planas declaradas
```

---

## 5. Pendientes

- [ ] **Neutraface Text** es de pago — conseguir el archivo o confirmar licencia
- [ ] **Roboto** se activa por Adobe Fonts en cada máquina
- [ ] **La gramática digital no está medida.** Tengo el envase, no las piezas de RRSS.
      Faltan 10–20 piezas digitales aprobadas para medir la retícula
- [ ] Los valores RGB equivalentes de PANTONE 114 C, 708 C y Neutral Black C
- [ ] Confirmar si el digital usa Neutraface o es otra familia
