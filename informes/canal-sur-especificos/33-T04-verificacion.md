# Realizador/a (puesto 33) · Tema 4 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/33-realizador-a/04-organizacion-control-realizacion.md`.
Fecha de trabajo declarada por el coordinador: 24-09-2026. Las fuentes que se releyeron o se
descargaron en esta fase llevan la fecha del sistema, 29-09-2026, igual que en la investigación B.
Resultado: 13.178 palabras y 52 epígrafes (`indice.py`), frente a 12.814. La ficha pasa a «13.200
palabras aproximadamente».

## Pasajes copiados: comprobación literal, sin reverificar

Un script del scratchpad parte el tema en párrafos, filas y citas y busca cada uno en su origen.

- **Copiado del común** (28-08, 08-09, 34-09, 30-13): todos los párrafos, filas y citas listados en
  `33-T04-redaccion.md` son literales. Las citas de Clear-Com, de la Tech 3347 y del MOS aparecen tal
  cual en 28-08 y en 30-13. También las del LE 6.1, 6.1.1, 6.1.2, 6.5 y 8.3, que además están en el
  Libro de Estilo.
- **Copiado de RTVE sin cambios** (realizacion/10, 11 y 15): son literales todos los listados, incluidas
  las dos citas del manual ATEM en bloque y el tramo de § 8 desde «La razón es la definición misma…»
  hasta «implicadas.».
- La frase de 08-04 sobre el teleprompter y la columna estaba adaptada, así que se verificó (véase
  hallazgo 12).

## Fuentes releídas en esta fase

| Fuente | Qué se comprobó | Leída |
|---|---|---|
| X Convenio, `x-convenio-rtva-boja-240-2014.txt` | Las diez fichas: cada cita, su ficha y su página (la del código). Hay 114 fichas y 114 cláusulas abiertas, así que «Todas las fichas terminan…» se sostiene. Se buscó si hay fichas de prompter, titulador, servidor o control de imagen | 29-09-2026 |
| RD 1680/2011, BOE-A-2011-19599.txt | 0905 RA 5.b-e, RA 6.a-g y contenidos; 0910 RA 1.d, RA 4.a y 4.c-g y contenidos; BOE núm. 302, de 16-12-2011; referencias posteriores | 29-09-2026 |
| RD 500/2024, BOE-A-2024-10685.txt | Art. séptimo (anexo I: sólo suprime y añade otros módulos), art. octavo y anexo XLI (profesorado) | 29-09-2026 |
| RD 1085/2020, BOE-A-2020-17274 (boe.es, act.php) | Disposición derogatoria única, apartado 2: deroga el anexo de convalidaciones del RD 1680/2011 | 29-09-2026 |
| IMS077_3, incual-IMS077_3.txt | CR5.2 y contexto de UC0216_3; CR2.3, CR2.5, CR2.6, RP3, CR3.1-3.5 y contexto de UC0217_3; CE1.5, CE1.7 y contenidos (ap. 4) de MF0217_3; RD 295/2004 y Orden PCI/797/2019 | 29-09-2026 |
| ANSI E1.11-2024 (PDF que descargó la investigación) | Portada, 1.1, 1.2, 1.3, 3.36, 3.37, 3.45 y 8.6; título; ESTA y USITT; «strictly voluntary» | 29-09-2026 |
| Autocue, *Prompting A-Z* (descargada de nuevo) y *How a prompter works* | Cada entrada del glosario, 70:30, imagen invertida, contrapeso | 29-09-2026 |
| Vizrt, *Viz Pilot Edge User Guide* 3.5, Introduction (descargada de nuevo de la URL 3.5) | Las cinco citas y su orden | 29-09-2026 |
| Manual ATEM en español | Retorno SDI, piloto y relés «por cierre de contacto» | 29-09-2026 |

`negritas.py` cotejó 136 negritas contra estas fuentes. Da 5 «no está», y las 5 son citas con elisión
(…) o […]. Cada tramo se comprobó a mano y es literal. `refutar_prosa.py` da un solo hallazgo: la
sigla CCU en el título, que es el enunciado literal y se queda.

## Hallazgos y correcciones (todas aplicadas y comprobadas en la fuente)

1. **Error 6 y 9, convenio.** El tema decía que el convenio no tiene ficha para el servidor y que
   quién graba y reproduce vídeos «no consta». Pero la ficha del Operador Montador de Vídeo (5212206,
   p. 190) dice **«Grabar, emitir y reproducir videos para programas en todo tipo de eventos y
   producciones con selección alternativa a la realización.»** Se añade a la tabla de puestos, a
   «Los servidores en el control», a «Normativa», a «Lo que este tema no da» y a «Trazabilidad». Se
   quita que la ficha del ayudante ponga en la asistencia los equipos auxiliares: eso lo dice la
   IMS077_3, no la ficha.
2. **Error 6, RD 1680/2011.** El tema no decía que el RD 1085/2020 derogó su anexo de convalidaciones.
   Ahora lo dicen la ficha y «Normativa». También se precisa el alcance del RD 500/2024: en el anexo I
   sólo suprime y añade otros módulos, y no toca los resultados de aprendizaje ni los contenidos de los
   módulos citados.
3. **Error 3.** Donde decía «RA 4.a a 4.g», ahora dice «RA 4.a y 4.c a 4.g», porque la 4.b no se cita.
   Y los nueve puntos del esquema de intercomunicación «coinciden con los equipos de este tema»,
   pero el prompter no está entre ellos. Se cambia por «cubren casi todos» y se advierte que el
   prompter no figura.
4. **Error 1.** Donde decía «cadena del epígrafe anterior», la cadena de la señal está al principio
   del tema, no en el epígrafe anterior. Se corrige la remisión.
5. **Error 5.** Faltaban por presentar BOE, MF, MAM y PP. Se añaden a las siglas.
6. **Error 9.** La frase de que After Effects «no tiene […] salida a la que un mezclador pueda
   enchufarse» no tiene fuente y es discutible. Se sustituye por «no genera el rótulo en el momento a
   la orden del control».
7. **Error 9.** «El servidor almacena y devuelve; no procesa la imagen» era una afirmación absoluta
   sin fuente. Pasa a «no es función de un servidor» (oficio) y se quita «no procesa la imagen».
8. **Error 9.** Tres afirmaciones de RTVE adaptadas no llevaban la marca de oficio: «un solo control
   central», «el precio del sincronizador es el retardo» y el piloto en todas las fuentes del
   compuesto. Ahora la llevan. El piloto por contacto se apoya ahora en el manual ATEM (relés «por
   cierre de contacto»).
9. **Vizrt.** Las citas eran literales, pero salían en otro orden que el de la guía y se presentaban
   como «el flujo». Se ponen en el orden de la guía y se añade la cita que apoya que las plantillas
   son cosa de diseño: **«Template Builder is used by design teams…»**.
10. **IMS077_3, CR3.1.** «Se preparan» tenía por sujeto «el funcionamiento de la tituladora»
   solamente. Se completa con el sujeto real (controles remotos, llegada de señales a los grabadores
   y tituladora).
11. **Aplicación práctica.** El paso 7 citaba CE1.5 también para los retornos, y CE1.5 sólo habla del
   prompter. Para el envío de vídeo a plató se añade CR3.2, y se incluye en «Trazabilidad». En el
   caso «hablar sólo con la cámara 2», la respuesta contradecía el panel descrito (una tecla para
   todos los cámaras). Se reescribe con el aislamiento de cámara según Clear-Com.
12. **Adaptación de 08-04.** «La columna» no tenía antecedente en este tema. Pasa a «la columna del
   pedestal», y se apoya en el contrapeso del glosario de Autocue (**«Counterbalance weight…»**).
13. **DMX512.** «Un aparato motorizado ocupa varios canales» era oficio y queda apoyado en la nota de
   3.37 (**«Automated luminaires usually require a Slot Footprint of greater than one.»**).
14. **Iluminador.** «Que es la que se hace en el control» era una inferencia. Se reformula como oficio.

Sin error: las páginas de las diez fichas, la atribución de cada RA, CR y CE a su módulo o unidad,
las cifras del DMX512 (513 slots, slot 0, 512 de datos, XLR de cinco polos), 70:30, 1/4, 1955, las
fechas y los títulos de la ANSI y del RD.

## Advertencias al coordinador

- Las fechas no cuadran. El encargo dice «hoy es 24-09-2026», pero la investigación y esta fase
  llevan la fecha del sistema, 29-09-2026. Se ha declarado la real.
- En la tabla del glosario de Autocue, el término y la definición van unidos con « — ». En la fuente
  son dos líneas. Las palabras son literales, pero ese guion no está en la fuente.
- La cita del ATEM «para garantizar…», copiada de RTVE sin cambios, no se tocó. En la fuente sigue
  «su procesamiento».

## Ficheros tocados

- Modificado: `temas/canal-sur-especificos/33-realizador-a/04-organizacion-control-realizacion.md`.
- Creado: este informe.
- Nada más en el repositorio. En el scratchpad quedan los scripts de cotejo y las descargas
  (RD 1085/2020, Vizrt 3.5, Autocue A-Z).
