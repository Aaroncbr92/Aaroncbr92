# Verificación · Ayudante de Realización (05) · Tema 17 · Accesibilidad, subtitulado, audiodescripción y lenguaje inclusivo en la puesta en antena

Fase 3. Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/17-accesibilidad-subtitulado-audiodescripcion-lenguaje-inclusivo.md`.
Fecha de lectura de todas las fuentes: 30-09-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»).

## 1. Literalidad de lo copiado (sin re-verificar)

Script línea a línea contra 33/16, 30/11, 33/03 y RTVE `produccion/11` (esta, también sin negritas).
Toda línea no nueva del tema está literal en alguna de esas fuentes. Las líneas distintas (291) caen en
las zonas declaradas como nuevas o son exactamente los cambios que lista la redacción: títulos y niveles
de rúbrica, «(epígrafe N)» → «(arriba)», «el mismo capítulo» → «el capítulo 9.7 del Libro de estilo de
2004» (en 33/16 el antecedente es el 9.7, correcto), «quien monta producción ajena» → «quien prepara la
emisión…», «Para el montador… se entrega» → «Para la puesta en antena… se emite», «tema 12» → «tema 15».
La tabla de grafismo y el párrafo de la llave posterior de RTVE: literales (salvo negritas quitadas).
Ninguna copia no declarada.

## 2. Lo nuevo, dato a dato

| Pasaje | Fuente releída | Resultado |
| --- | --- | --- |
| Ley 8/2017: título, una redacción (vig. 04-02-2018), cap. IX y su rúbrica, arts. 41.1, 41.2.f), 41.4 (dos frases), 41.5, 42.1; «deberán» en 41.1 | `boe.py precepto BOE-A-2018-1549` ci-7, a4-3, a4-4; título por el XML del BOE | Literal, correcto. `negritas.py` y `refutar_modo.py` sobre el pasaje: 0 hallazgos |
| Ficha 5353000, dos tareas literales, anexo III, p. 111 | `documentos/x-convenio-rtva-boja-240-2014.txt`, l. 4724-4736 («Núm. 240 página 111») | Literal, correcto |
| IMS077_3: competencia general y entorno (p. 1), UC0217_3 RP1 (p. 7), CR2.5 (p. 8), MF0218_3 contenidos (p. 24) | `realizador/incual-IMS077_3.txt` (marcadores «N de 25») | Literal y páginas correctas. La cita de la competencia general acaba en «audiovisual»: el texto sigue, sin cambiar el sentido |
| «publicada por la Orden PCI/797/2019» | Ficha del INCUAL («Publicación: Orden PCI/797/2019 · Referencia normativa: RD 295/2004»); título de la Orden en el BOE (`boe_buscar.py`, BOE-A-2019-10917): «por la que se **actualizan** cualificaciones… establecidas por el Real Decreto 295/2004» | **Corregido** (error 2/9): «establecida por el Real Decreto 295/2004 y actualizada por la Orden PCI/797/2019». «Catálogo Nacional de Cualificaciones Profesionales»: confirmado por ese título |
| «la cualificación profesional del puesto» (entrada del epígrafe 5) | Mismo documento: describe el oficio, no el puesto de la RTVA (el propio tema lo dice dos líneas después) | **Corregido**: «del oficio» |
| Lista «Antes de salir al aire», supuesto práctico y tabla «Qué le toca al ayudante»: cada cifra y remisión (102.2 LGCA 90 %/15 h; Carta 13.9; C-p puntos 12 y 93; 101.3 y 101.1.h LGCA; 31.1.i LAA; CNLSE 6.1, 6.2, 6.3.1-6.3.3, 6.4: 1/6, izquierda, cinco puntos de luz, 1/125-1/250 s, palmo de aire, desaparecer sin texto; UNE 153010 por Burgos: 37 caracteres, 15 cps, mínimo 1 s y máximo 6 s, 74 caracteres ≈ 5 s; Guía CAA recomendación 1; Libro de estilo 9.7.3 y 11.1.4; Ley 8/2017 41.5; IMS077_3 RP1 y CR2.5) | Contra el pasaje copiado del tema que lo sostiene y, en lo nuevo, contra la fuente | Todo cuadra; lo que no tiene norma va como «oficio» o «lectura propia» |
| «El grafismo y la señal de programa», párrafo de aplicación | Cita «grafismo, mosca, simbología, señalética»: literal de la guía del CNLSE (6.3.1, en el tema); lo demás, declarado oficio | Correcto |
| Cabecera: «De dónde sale», remisiones a temas 9, 11, 12, 15 y a los temas 4 y 8 del común | Enunciado del puesto y `PROGRAMA-COMUN.md` | Correcto |
| Portada, «Fuente» | Cuerpo del tema | **Ampliada**: faltaban normas que el tema cita (CE art. 49, RD 1112/2018, X Convenio ficha 5353000) y la referencia RD 295/2004 de la IMS077_3 |
| «Normativa que el tema invoca» | Cotejada contra el cuerpo (cada artículo listado aparece en él) | **Añadidos**: Ley 18/2007 art. 4.1.f) (invocado por la Carta) y la Orden PCI/797/2019. Lo demás, correcto |
| «Lo que este tema no da» y «Trazabilidad» | Cuerpo y fuentes | Correcto; en la fila del INCUAL se añade RD 295/2004 y BOE-A-2019-10917 |

## 3. Lentes

- `negritas.py` sobre lo nuevo (Ley 8/2017, IMS077_3, convenio): 15 cotejadas, todas halladas en su fuente.
- `refutar_modo.py` (Ley 8/2017): 0 hallazgos.
- `refutar_prosa.py`: 1 (la frase repetida de las cadenas de la Ley 9/2018, literal del común; se deja). Siglas sin presentar y negritas rotas: ninguna.
- `indice.py`: 18.857 palabras, 43 epígrafes (la portada dice «18.800 aproximadamente»: vale).
- No se pasan `refutar_exactitud.py` sobre las normas del común: son pasajes copiados que no se re-verifican.

## 4. Resumen

Cuatro correcciones y dos ampliaciones de listas, ningún dato quitado: IMS077_3 «publicada por» →
«establecida por el RD 295/2004 y actualizada por la Orden PCI/797/2019» (en el cuerpo y en la
trazabilidad); «del puesto» → «del oficio»; portada «Fuente» completada; «Normativa» completada.
Pasajes cambiados releídos: cada antecedente está delante.

Otros ficheros tocados: ninguno, salvo este informe. Copia previa en el scratchpad (`05t17v/antes.md`).
