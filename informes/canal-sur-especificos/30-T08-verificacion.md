# Puesto 30 · Tema 8 · Verificación (fase 3)

Fecha: 25-09-2026 (encargo fechado 24-09-2026).
Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/08-ingesta-digitalizacion-transferencia-verificacion-copias-metadatos-archivo.md`
(tras la verificación, `indice.py`: 10.337 palabras, 43 epígrafes; el índice no cambia).

## Fuentes releídas y fecha

| Fuente | Qué se releyó | Fecha |
|---|---|---|
| X Convenio RTVA, BOJA 240, 10-12-2014 (txt) | Anexo III, ficha 5212206, p. 190: objeto y las ocho tareas | 25-09-2026 |
| Libro de estilo Canal Sur 2004 (txt) | 5.3.3 y su página (82); 9, 9.9, 9.9.1 y su página (166); índice | 25-09-2026 |
| Resolve 21, extractos `mediapool.txt` (pp. 373-374), `metadata.txt` (pp. 417-420, 434), `tape.txt` (pp. 558-564) | Cada cita y su página | 25-09-2026 |
| Adobe, «Ingest and proxy workflows in Premiere» (txt) | Fecha «Jan 7, 2026» y las cuatro citas | 25-09-2026 |
| EBU Tech 3293 v. 1.10 (txt) | Portada (Ginebra, abril 2020), pp. 3, 7, 8; §§ 2.1 y 2.3 | 25-09-2026 |
| CCSDS 650.0-M-3 (txt) | Portada (Magenta Book, dic. 2024); §§ 1.1, 1.6.2, 4.2.2, 4.2.3.3, 4.2.3.4 y rótulos 4.2.3.3-4.2.3.8 | 25-09-2026 |
| lto.org roadmap (`lto-roadmap.txt`, guardado en la redacción) y `ltfs.txt` | Todas las citas. Relectura en vivo intentada: curl devuelve 178 bytes (captcha) y WebFetch, página vacía; se trabaja con lo guardado | 25-09-2026 |
| Catálogo SMPTE RP 210 | «withdrawn» | 25-09-2026 |

## Pasajes copiados: sólo literalidad

- Común (Cámara T07, 11 bloques): búsqueda normalizada de cada párrafo en el tema → todos literales;
  en 822-842 las únicas diferencias son las tres remisiones declaradas; en 795-799 y 939-944 sólo
  falta la frase final declarada. No se re-verifican.
- RTVE sin cambios (ing-tec-teleco/10 y edicion-montaje/01): cada frase y fila de tabla está en su
  origen una vez quitadas negritas, ✔ y mayúsculas → literales.
- Adaptado de RTVE (paridad del RAID 5, red, tres redes, DAM/MAM): cotejado con el original; sólo
  cambian los rótulos declarados. Técnicamente correcto; sigue declarado como oficio.

## Correcciones (error del catálogo)

1. **3 recuento** · «Cuatro de sus ocho tareas» tocan el tema, pero § 4 cita una quinta (control
   técnico de calidad) y «Documentos técnicos» también. → «Cinco de sus ocho», con la fila añadida.
2. **6 salvedad omitida** · 9.9.1 del Libro: la regla del rótulo «Archivo» está en el capítulo 9
   («Asuntos comprometidos»), 9.9 «Material objetable», en el párrafo sobre reportajes de
   delincuencia, malos tratos y asuntos judiciales; se presentaba como regla general. Se completa la
   cita (estaba cortada en mitad de frase), se añade el contexto literal y se declara oficio lo
   general; ajustada también la fila «Montaje» de la aplicación práctica.
3. **1 cita cruzada / 9** · LTO: la nota «Assuming a 2.5:1 compression» lleva en la página su llamada
   (*) en la frase de la velocidad (1200 MB/s), no en la de capacidad. Se mueve a la velocidad y se
   quita el cálculo 100 ÷ 2,5 = 40 TB (dependía de aplicar la nota a la capacidad), también en la línea
   de cálculos del cierre. La capacidad nativa sigue en «Lo que este tema no da».
4. **4 «podrá» por «deberá»** · Resolve, cap. 17: «One of the few things you *may want* to do»
   se presentaba como «primer paso» y «sólo después se añade». → «lo propone antes de añadir…; lo
   propone, no lo impone».
5. **4** · OAIS, Replace Media: «sin alterar el contenido» → literal «should not be altered» (la
   información de contenido y la PDI).
6. **9 / precisión** · Resolve p. 562: el nombre 00086400.dpx es el código de tiempo convertido en
   cuadros «based on the ingest frame rate», y lo describe para *Capture Now*. Añadido.
7. **Aviso de la redacción corregido** · «Batch Capture Via EDL» sí está desarrollado en el extracto
   (pp. 563-564). Se añade su definición literal y la regla de no duplicar clips con el mismo nombre de
   cinta y TC de inicio; el rango del capítulo pasa a pp. 558-564 (tres sitios).
8. Menores: «La ficha le da expresamente» → «nombra expresamente»; «Es lo mismo que dice la guía» →
   «Coincide con la guía» (Resolve habla de colisiones; la DPC, de pérdidas accidentales).

Confirmado sin cambios: ficha 5212206 (texto, código, p. 190, anexo III, ocho tareas); 5.3.3 p. 82;
todas las citas de Resolve y sus páginas (373, 374, 417, 418, 420, 434, 558, 559, 561, 562);
opciones de captura (DPX/QuickTime, códecs, 2 a 16 pistas); los seis algoritmos y sus descripciones;
Adobe (fecha y citas); EBUCore (v. 1.10, abril 2020, §§ 2.1, 2.3, pp. 3 y 7); OAIS (definiciones del
§ 1.6.2, cinco clases de PDI, ejemplo ISBN, seis entidades, QA, Error Checking, Disaster Recovery);
LTO (10.ª generación, 100 TB comprimidos, 1200 MB/s, tabla de compatibilidad); LTFS (desde LTO-5,
particiones, arrastrar y soltar); RP 210 retirada; cálculo 12 GB a 100 Mb/s = 960 s = 16 min.

## Lentes (tema técnico sin norma jurídica)

- `negritas.py` (convenio, Libro, Resolve, Adobe, EBU, OAIS, LTO, LTFS): 126 cotejadas; 25 «no están»:
  23 son de pasajes copiados de Cámara T07 (fuentes no pasadas; literalidad comprobada arriba) y 2 del
  Libro 9.9.1 por la ligadura «ﬁ/ﬂ» del txt (suﬁciente, reﬂejada); comprobadas a ojo: literales.
- `refutar_prosa.py`: 0 siglas sin presentar, 0 negritas rotas; 1 frase repetida (cita del convenio en
  dos tablas), se deja.
- `indice.py`: epígrafes sin cambios; índice vigente.
- Relectura de antecedentes en los pasajes cambiados («en ella» → la función *Replace Media*; «esos
  reportajes» → los citados en la frase anterior): correctos.

## Pasajes cambiados (para refutación)

El punto en la ficha (frase y tabla) · § 1 «Qué es la ingesta» (última frase) y «La ingesta en el
programa de edición» (viñeta de Resolve) · § 2 párrafo «Batch Capture Via EDL» y frase del nombre
00086400.dpx · § 4 frase «Coincide con la guía» · § 5 «Por qué», segundo párrafo · § 7 viñeta
*Replace Media*, viñetas de capacidad y velocidad de la LTO, párrafo del rótulo de archivo · tabla de
aplicación práctica (fila Montaje) · Documentos y Trazabilidad (pp. 558-564) · línea de cálculos final.

Ficheros tocados: el tema 08 y este informe. Copia previa del tema en el scratchpad de la sesión.
