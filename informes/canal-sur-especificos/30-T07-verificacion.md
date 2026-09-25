# Puesto 30 · Tema 7 · Verificación (fase 3)

Fecha: 25-09-2026 (encargo fechado 24-09-2026).
Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/07-postproduccion.md`
(tras la verificación, `indice.py`: 12.539 palabras, 49 epígrafes).

## Fuentes releídas y fecha

| Fuente | Qué se releyó | Fecha |
|---|---|---|
| *DaVinci Resolve 21 Reference Manual*, extractos con marcas de página (`fuentes/canal-sur/montador/resolve21-extractos/`) | Cap. 125 (pp. 3085-3095), 127 (pp. 3147, 3150-3153), 131 (pp. 3200-3204), 150 (pp. 3545-3546), 55 (pp. 1194-1199), 56 (pp. 1213-1215), 181 (pp. 4091-4096, 4101-4102, 4121-4122), 187 (pp. 4198, 4205), 188 (p. 4219); número y título de cada capítulo | 25-09-2026 |
| Adobe, ayuda de Premiere (Wayback): «Transitions overview» y «Audio editing with Essential Sound panel» | Párrafos citados; fecha «Jan 7, 2026» | 25-09-2026 |
| Informe UIT-R BT.2408-9 (txt) | Portada y título, § 2.1, tabla 1, § 9 | 25-09-2026 |
| Libro de Estilo de Canal Sur (txt) | Índice (3.16, 9.2, 9.2.12.4), 3.2.2, 3.6.1, 3.16 a 3.16.2, 9.2.12.4, 9.9, 9.9.1, 9.9.2, con página impresa | 25-09-2026 |
| UBU, *Guía para elaborar Material Multimedia Accesible* (txt y PDF, página a página con `pypdf`) | Pp. impresas 4 y 6; metadatos del PDF (30-11-2020) | 25-09-2026 |
| Reglamento electrotécnico para baja tensión (RD 842/2002, BOE-A-2002-18099), `boe.py precepto … a4` | Art. 4; 1 redacción, vigente desde el 18-09-2003 | 25-09-2026 |
| W3C, portadas de IMSC1, WebVTT y DFXP (w3.org/TR) | Desarrollo de las siglas | 25-09-2026 |
| Temas 2, 3, 9 del puesto 30 | Destino de las remisiones internas | 25-09-2026 |

## Pasajes copiados: sólo literalidad

Script de cotejo (bloques del tema normalizados, sin negritas, buscados en el origen):
- Común (28-05, 28-09, 28-13): todos los bloques listados en la redacción aparecen literales; las
  únicas diferencias son los retoques declarados (remisiones «(tema N)» quitadas, «Filtros» → «Los
  filtros de corte», matices 2 y 3 en viñetas). No se re-verifican.
- RTVE sin cambios (R20 §§ 8-11, R02 § 8, R09 §§ 1-4, R03 §§ 5-6): literales una vez quitada la
  negrita. No se re-verifican.
- Lo adaptado de RTVE (tabla de fases, estática de la LUT, curva de velocidad, ficheros gráficos y
  bits, aviso de la LUT, «las familias», «tres y no dos», 4:4:4:4, *ducking*) sí se revisó: coherente
  con el origen y con las fuentes; las remisiones al tema 2 (4:4:4:4, rango legal, «Medir la señal»,
  «Los límites de la señal según la EBU»), al tema 3 (*render*, colas al conformar) y al tema 9
  (ficha del Grafista, 3.16) tienen destino. Sin cambios.

## Correcciones (error del catálogo)

1. **6 salvedad omitida** · 9.2.12.4 (virado, cámara en mano, música) se presentaba como regla general
   de la información; está en 9.2 «Malos tratos» y habla de **«reportajes de sucesos»**. Corregido en
   § 2 «Lo que no se corrige» (se cita la frase de entrada y la extensión a toda la información queda
   como oficio) y en § 7 «La música bajo la voz».
2. **6** · 9.9: faltaba **«no se emitirán si existe un factor de riesgo»** y «y su familia»; se cita
   la frase entera. El supuesto práctico tramaba al menor sin la condición: ahora «si hay factor de
   riesgo». 9.9.1: «asuntos delicados» → los que nombra el texto (delincuencia, malos tratos, asuntos
   judiciales).
3. **6** · BT.2408: 203 cd/m² vale en monitor PQ o HLG de 1 000 cd/m² de pico (tabla 1); añadido.
4. **3 recuento** · «los mismos cuatro objetivos» de Blackmagic: el cap. 125 da seis (hasta *Adding
   Style* y *Quality Control*, p. 3095). Corregido; Trazabilidad ampliada a p. 3095.
5. **9 sin fuente** · «El formato más extendido es el .cube»: el manual no lo dice → «Resolve trabaja
   con el formato .cube».
6. **9** · «En España la red eléctrica es de 50 Hz» era cálculo sin fuente: se ancla en el art. 4.4 del
   Reglamento electrotécnico para baja tensión (RD 842/2002), literal. Añadido a ficha, a la tabla de
   normativa (rótulo ahora «Normativa y recomendaciones técnicas que el tema cita», índice ajustado) y
   a Trazabilidad. Es reglamento, y así se dice (error 2 evitado).
7. **9** · Siglas: quitada la expansión «Consumer Electronics Association» de CEA-608/708 (no
   confirmada; se deja «así los nombra Blackmagic»). IMSC1, WebVTT y DFXP confirmadas en W3C.
8. **8 página mal** · UBU: abiertos/cerrados en la p. 4 (no 4-5); requisitos visuales p. 4 y de tiempo
   p. 6 (no 5-6). Comprobado página a página en el PDF: el número impreso encabeza la página.
9. **8** · Libro 3.16: la «cama» de audio está al final de 3.16.2 (p. 58), no en 3.16; la primera norma,
   3.16 (p. 57). Citas y supuesto ajustados.
10. **6** · Resolve, colas: el diálogo de tres opciones aparece al añadir con Comando-T o el menú
    contextual del punto de edición (p. 1197); añadido.
11. **9** · Adobe: «consejo contrario» → «consejo preventivo» (no contradice a Resolve); «1:00 es un
    segundo» pasa a lectura propia (Adobe no da cadencia; 15 cuadros = medio segundo a 30 i/s).
12. **4/precisión** · Supuesto: «pico por debajo de −1 dBTP» → «que no pase de −1 dBTP» (R 128:
    *shall not exceed*).
13. Ficha «Redacción que se estudia»: R 128 y Tech 3343 no se leyeron el 25-09 sino el 24-09 a través
    de los temas de Sonido (y la Tech 3343 viene del 28-09, no sólo del 28-13): corregido ahí y en
    Trazabilidad. Capítulo de la p. 4219: cap. 188. Extensión: 12.500. UNE 153010: publicada por
    AENOR en 2012 según la guía de Burgos. «Lo que este tema no da»: histograma y CIE sí están en el
    extracto (pp. 3152-3153); se dice que el tema no los desarrolla.

Confirmado sin cambios: todas las citas de Resolve (texto, página y capítulo), las de Adobe, BT.2408 §§
2.1 y 9 (título y fecha 03/2026), Libro 3.2.2 (p. 46), 3.6.1 (p. 50), 9.9.2 (p. 167), UBU (37
caracteres, 15 c/s, permanencias, sincronía); rangos de *Temp* y *Tint*, saturación 50/0/100, zonas
seguras 93/90 %, guías 1:1-4:5-9:16, seis estilos de fundido, duraciones ¼-½-1-2 s, alineaciones
(cuadros de más: lectura correcta), cuentas de colas y de subtítulos (74 c ≈ 5 s; 37 c ≈ 2,5 s).

## Lentes

- `negritas.py` (REBT, Libro, UBU, BT.2408, extractos de Resolve, Adobe): 152 cotejadas; 32 «no
  están»: 27 son de lo copiado del común (Rane, iZotope, R 128, Tech 3343: fuentes no pasadas), 2 por
  elisión «[…]» y 3 del Libro por comillas y saltos de página; comprobadas a mano: literales.
- `refutar_exactitud.py` (REBT): 3 «no literales» falsos positivos (lee §§ 2.1, 3.1, 3.2 como artículos).
- `refutar_modo.py` (REBT): 0. `refutar_prosa.py`: 1 (sigla DCP en Trazabilidad), corregida; 0 después.
  `indice.py`: 49 epígrafes.
- Releídos los pasajes cambiados: «esos reportajes» y las remisiones internas tienen antecedente.

## Ficheros tocados

- Modificado: el tema citado arriba.
- Creado: este informe.
- Volcado auxiliar del BOE-A-2002-18099 en el directorio temporal de trabajo (fuera del proyecto).

## Adenda (relanzamiento de la fase 3, 25-09-2026)

La fase 3 ya estaba hecha (arriba) y el tema había pasado refutación, remate y revisión final
(`30-T07-final.md`). No se repite la verificación completa para no pisar el remate. Sólo se cierra
el pendiente que dejó la revisión final:
- **9 sin fuente** · § 5 «Los criterios del subtitulado», línea 1: «La norma española de subtitulado …»
  → «La norma de subtitulado para personas sordas que cita la guía es la UNE 153010:2012 (AENOR)».
  La guía de Burgos (p. 4 y bibliografía, releída el 25-09-2026) da «UNE 153010» y «AENOR. (2012)»,
  sin llamarla española.
Ficheros tocados: el tema (una línea) y este informe.
