# 31-T08 · Verificación · Autocontrol y operación básica

Fase 3. Verificado el 3-X-2026 (fecha de referencia: 24-IX-2026).
Tema: `temas/canal-sur-especificos/31-presentador-productor-de-radio/08-autocontrol-y-operacion-basica.md`.
Leído sólo `ENCARGO.md`, el enunciado del puesto 31 y el informe de redacción.

## 1. Literalidad de lo copiado (sin re-verificar)

Comprobación automática por párrafo, fila de tabla y frase contra 28-T04, 28-T05, 28-T09, 28-T13,
34-T09 y RTVE sonido/07, /12 y /14 (negritas y saltos de línea normalizados). Todos los pasajes de
«Copiado del común» y «Copiado de RTVE sin cambios» aparecen literales; las únicas diferencias son las
omisiones declaradas («(tema N)», «(«Grupos»)», «, que se ven en…», etc.), revisadas una a una con grep
(líneas 199/239, 323/648, 339/664, 346/671, 348/672, 395/433, 413/748, 336/910, 365/939, 370/944,
293/1005 de 28-T0x frente al tema). El pasaje adaptado de 34-T09 (§5) coincide con lo declarado.

## 2. Lo nuevo, releído en su fuente (lecturas: 03-10-2026)

| Dato | Fuente | Resultado |
|---|---|---|
| Citas de López Vigil: locutor/operador y «manejar la consola» (cap. 4); bache (cap. 3); cortina, ráfaga, puente, telón, «no deben truncarse», fondos (cap. 6); ráfaga antes de los *flashes* (cap. 7); cuña: definición, nombre, tres clases, duración, cuatro C, viñetas (cap. 10) | `fuentes/canal-sur/radio/lopez-vigil-manual-urgente-radialistas.txt`, líneas 3182-3212, 1366, 5094-5147, 8971, 12017-12219 | Literales; capítulos confirmados por posición y remisiones internas del libro |
| Glosario 7.5 del Manual de RTVE: cuña (con la errata «desarrollan»), sintonía, careta, cortinilla, golpe, guion de continuidad | `RTVE_manual-de-estilo_anexos.txt`, 240-255, 285 (volcado 02-09-2026) | Literales |
| Manual de RTVE 3.2.1 y 3.2.1.1 (RNE) | `RTVE_manual-de-estilo_rne.txt`, 52, 62, 66 | Literales; un matiz corregido (abajo) |
| Portada y «Recomendaciones técnicas»: versiones de R 68, R 128 V5, R 128 s1 V3, Tech 3341/3343-2023, AES TD1008 | Portadas y trazabilidad de 28-T04/05/09/13 (cerrados) | Coinciden |
| Cálculos (−24,6 LUFS, 1,6 LU; −3 + 4 = 1; −25,6 LUFS) | Aritmética | Correctos |
| Remisiones a los temas 1, 2, 4, 7, 10, 14 y 15 del puesto 31 | Índices de esos temas | Todas tienen destino (tema 4 §6 autocontrol y §7 operador; tema 7 «Dos líneas, dos retornos»; tema 2 indicaciones técnicas de la escaleta; tema 1 «Sus tres utilidades») |
| Ráfaga = contenido corto de la R 128 s1 | Definición copiada de 28-T09 («stingers, bumpers…») | Inferencia declarada como cálculo; se mantiene |

## 3. Correcciones aplicadas

1. **Error 9 (afirmación sin fuente)**, «Abrir y cerrar»: «con el canal apagado, la fuente no llega a
   ninguna mezcla aunque su fader esté arriba». La fuente (Yamaha) sólo dice que el canal queda
   silenciado, y el propio manual sitúa puntos de toma «PRE FADER» antes del [ON]. Queda: «el canal
   queda silenciado aunque su fader esté arriba (Yamaha: «If this is off, the corresponding channel will
   be muted»)».
2. **Error 6/9**, «Tres sentidos de continuidad»: el manual dice que el eje de la continuidad
   informativa es el **boletín horario**; el «de una cadena» era glosa. Queda «el boletín horario […]
   es «el eje de la continuidad informativa» (3.2.1)».
3. **Error 1 (antecedente)**, «Qué es una cuña»: «que ordena con las letras de la palabra» no decía qué
   palabra. Se añade la cita literal de López Vigil («Como la palabra CUÑA comienza por C…»).
4. «De dónde sale este tema»: la lista del vocabulario tomado del glosario incluía «indicativo», que
   el tema no toma del glosario (la fila de «indicativo» es oficio copiado de 28-T09). Se sustituye por
   los términos que sí se citan: cuña, cortinilla, sintonía, careta, golpe, guion de continuidad.
5. Misma sección: «Canal Sur no tiene publicado un libro de estilo de radio» se precisa: el *Libro de
   estilo de Canal Sur Televisión y Canal 2 Andalucía* (RTVA, marzo de 2004) existe y es de televisión
   (portada leída en `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`; no trae definiciones de
   cuña, ráfaga ni cortinilla para radio).
6. «La cuña en autocontrol»: «sonarán igual de fuertes» se rebaja a «tienen la misma sonoridad
   integrada», que es lo que la R 128 permite afirmar.

## 4. Lentes

Tema técnico sin norma legal: `refutar_prosa.py` da los mismos 6 hallazgos que en redacción (palabras
en mayúsculas dentro de citas inglesas de Yamaha y Soundcraft; no son siglas). `indice.py`: 13.617
palabras, 66 epígrafes. Siglas: la AES se presenta en el cuerpo («Qué es la R 128») antes de su uso.

## 5. Avisos

- La «Trazabilidad» da 25-09-2026 como fecha de lectura de EBU, AES, Yamaha, Soundcraft y Rane: es la
  de los temas cerrados de los que se copió; no se han releído (pasajes copiados).
- Siguen pendientes las remisiones heredadas de 31-T07 que señala la redacción (aviso 3); no es este
  tema.

## Ficheros tocados

- El tema 8 (seis correcciones arriba).
- Creado este informe.
