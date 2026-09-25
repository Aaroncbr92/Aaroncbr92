# Puesto 30 · Tema 15 · Verificación (fase 3)

Fecha: 25-09-2026 (encargo fechado 24-09-2026).
Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/15-organizacion-nomenclatura-trazabilidad-colaboracion.md`.

## Lo copiado: sólo literalidad

- **Copiado del común** (Redactor/a T03, 270-278 y 282-293): `diff` byte a byte contra el tema,
  antes y después de corregir: idéntico. No se re-verifica.
- **Copiado de RTVE sin cambios** (`edicion-montaje/07`): tabla de vistas (111-115) idéntica tras
  quitar `**`; fragmento de 83-85 idéntico, palabra por palabra, al texto de la línea 123 del tema.
- **Adaptado de RTVE** (tabla de vocabulario): las dos columnas son literales de RTVE sin negrita; **sí
  se verificó** en la guía de Avid de 1999: el *bin* contiene los *master clips*, enlazados a los
  ficheros de material, y las secuencias y *subclips* (p. 66); el *subclip* es un trozo marcado de un
  *master clip* (p. 211); el proyecto se guarda separado de los ficheros de material (p. 33). Se añade
  esa fuente delante de la tabla y en «Trazabilidad».

## Fuentes releídas (todas el 25-09-2026)

| Fuente | Cómo |
|---|---|
| Avid *MC User's Guide* R8.0, 1999 | txt local; pp. 33, 35-36, 41, 66, 72-74, 126-127, 211, 261, 269-270; portada (Part 0130-04015-01 Rev. A, May 1999) |
| Avid *Audio-Video Editing Workflows*, 2010 | txt local; pp. 11, 18, 19, 25 (los encabezados marcan el comienzo de página; el cap. 3 empieza en la 18) |
| Avid *What's New* 2023.3 | txt local; p. 2 |
| Avid KB en275293 | descargada con curl hoy; «Last Updated: August 11, 2023» |
| ELEMENTS, blog | descargado con curl hoy; `datePublished` 2023-01-24; autor Filip Milovanovic |
| SMPTE ST 377-1:2019 | txt local (frontal): definiciones de Package ID y UMID, nota del UMID extendido, referencia a ST 330:2011 |
| EBU Tech 3293 v1.10 | txt local, 3.5 (pp. 18-19); el PDF que sirve hoy tech.ebu.ch es idéntico (`cmp`) al local: v1.10 sigue siendo la vigente |
| Libro de Estilo CSTV 2004 | txt local; 3.17.1.5 (p. 61), 5.3.3 (p. 81), 6.1-6.1.2 (pp. 88-89); portada: 1.ª ed., marzo de 2004, ISBN 84-609-0453-9 |
| X Convenio, BOJA 240/2014 | txt local; anexo III, ficha 5212206, p. 190 (objeto y ocho tareas) |

Las 78 citas en negrita que vienen de una fuente (74 al primer intento, 4 partidas por salto de página) se buscaron por script en los volcados (normalizando
comillas, guiones, ligaduras y espacios): todas están, las que cruzan salto de página comprobadas a
mano (*Attic*, pp. 35-36; mayúsculas, pp. 126-127; LE 6.1.2, pp. 88-89). Páginas y epígrafes de cada
cita: correctos. Las negritas que no son cita son rótulos de lista o de párrafo, como en los temas
cerrados del 28.

## Hallazgos y correcciones (todas comprobadas en la fuente antes de aplicarlas)

1. **Error 3, recuento.** La KB de Avid enumera **cinco** apartados de precaución (compatibilidad,
   complementos, efectos, material, copia de seguridad) bajo «the following items»; el tema decía
   «cuatro» y daba la copia como «regla general» aparte. Ahora: «cinco precauciones», la copia como 5.
2. **Error 9.** Complementos de terceros «en la misma versión»: la KB sólo dice «but also their
   versions». Ahora: «y atención también a sus versiones».
3. **Error 6, salvedad omitida.** ELEMENTS da, en «Bin Locking Requirements», además del
   almacenamiento, el requisito de licencia (Ultimate, Enterprise y licencia perpetua; no First ni «the
   popular subscription plan»). Añadido, fechado en 2023 y atribuido al artículo.
4. **Error 9.** «La única regla de nombres que la casa tiene publicada»: contradicho por el propio
   tema (6.1.1 y 6.1.2 son dos reglas) y no comprobable en absoluto. Ahora: «Las reglas de nombres que
   la casa tiene publicadas están en el Libro de Estilo».
5. **Error 9.** «CSRTV no tiene publicada una convención…» → «No consta que CSRTV tenga publicada…».
6. **Precisión (p. 41).** La condición de la guía es mover *bins* y proyectos entre plataformas; los
   caracteres se prohíben en nombres de proyectos, *bins* y usuarios. Redactado así.
7. **Portada.** Citaba el *What's New* 2022.10, que el tema no usa (el redactor lo leyó y lo
   descartó). Quitado.
8. **Trazabilidad.** Añadidas las pp. 33, 66 y 211 de la guía de 1999 y «requisitos de licencia» en
   la fila de ELEMENTS.

Sin hallazgo: tareas de la ficha (ocho, dos citadas, texto literal), anexo III, remisiones a los
temas 3, 8, 9, 13 y 14 (coinciden con el enunciado), cinco operaciones y tres vistas del *bin*, *Attic*
(.bak + número, la más alta es la última), truncado a seis caracteres, 32 caracteres del nombre de
cinta, UMID básico de 32 bytes y extendido de 64, órdenes Lock/Protect/Unlock y colores, carpetas
«To/From Audio Editor», «Sequence_ForMix», errata «recomendable es» del LE (está en el original).
Lo marcado «oficio» queda como tal.

Antecedentes de los pasajes cambiados releídos («el mismo artículo» en 3 remite a ELEMENTS; en la
lista de la KB, «El mismo artículo» sigue remitiendo a la KB).

## Lentes (ENCARGO: tema técnico sin norma legal)

- `refutar_prosa.py`: 0 hallazgos.
- `indice.py` sobre el tema: 28 epígrafes, 6.631 palabras; índice sin cambios.
- No proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

- Editado: el tema 15. Creado: este informe.
- Aviso: una primera llamada a `indice.py` sin argumentos regeneró los seis temas de
  `temas/general/`; `git diff` confirma que su contenido no cambió (sólo la fecha de modificación).
