# 04 · Ayudante de Producción · Tema 11 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/11-produccion-en-exteriores-y-retransmisiones.md`
(16.028 palabras con `wc`, 15.232 según `indice.py`; 66 epígrafes, sin cambios de rúbrica).
Verificado el 06-10-2026. Fecha de corte: 24-09-2026.

Ficheros tocados: el tema y este informe. Ninguno más. Fuera del repositorio, en el scratchpad:
un script de cotejo y la descarga del consolidado de EUR-Lex del Reglamento 2019/947.

## Lo copiado: sólo comprobación de literalidad

Script de cotejo por frases y celdas de tabla (sin negritas, espacios normalizados) del tema contra
Productor T02, T06 y T08 y RTVE `realizacion/14`.

- **Copiado del común**: aparece literal salvo los cambios declarados por el redactor (remisiones
  «tema N» y «rúbrica…», títulos nuevos, viñeta de contactos institucionales, frases quitadas).
  No se han vuelto a verificar. **Un fallo de copia**: la cita en bloque de las diez tareas de la
  ficha (de Productor T02, líneas 297-313) estaba truncada en «diseñado por el» y faltaban la
  décima tarea y el cierre de la negrita. Restituida y cotejada con el convenio (BOJA 240/2014,
  p. 110).
- **Copiado de RTVE sin cambios** (tabla «Plató | Retransmisión»): celdas literales.
- Ligaduras tipográficas del PDF del Libro de estilo («ﬁ», «ﬂ») en cinco pasajes copiados:
  sustituidas por «fi», «fl» (mismo texto; Productor T08 las conserva, no se ha tocado).

## Lo nuevo y lo adaptado: verificado en la fuente

| Fuente | Leída hoy (06-10-2026) | Resultado |
|---|---|---|
| Ley 13/2022, arts. 144 y 145 (`BOE-A-2022-11311`, redacción única desde 09-07-2022) | Volcado | Citas literales; una salvedad omitida (144.2) |
| Reglamento (UE) 2019/947, art. 19.2 | DOUE original y consolidado EUR-Lex a 01-05-2025 (CELEX 02019R0947-20250501) | Literal; sin cambios en el consolidado |
| X Convenio, anexo III: Ayudante de producción (p. 110), Ayudante de unidades móviles (p. 112), Jefe de radioenlaces y UM, J. Radiofrecuencia | `x-convenio-rtva-boja-240-2014.txt` | Literales; las dos jefaturas tienen el mismo objeto y tareas, como dice el tema |
| Libro de estilo 4.4.1, 4.4.4 (puntos 1 y 4), 8.1 (punto 6) | `libro-de-estilo-333233b.txt` | Literales y bien numerados |
| Temas 5, 6, 7, 8, 9, 12, 14, 17 del puesto y 9 del común | grep de rúbricas | Dos remisiones erróneas (abajo) |
| RTVE `produccion-asistencia/13` §3 (vocabulario adaptado) | Lectura | Apoyado sólo en plantilla; un detalle sin fuente |

## Correcciones aplicadas

1. Fallo de copia (error 9/6): ficha truncada; restituidas la décima tarea («Ayudar al productor
   en el cumplimiento de la legislación de prevención de riesgos laborales») y el cierre.
2. Error 6. Art. 144.2: omitía la salvedad de los servicios a petición («solo se podrá emitir dicho
   resumen informativo si el mismo prestador del servicio ofrece el mismo programa en diferido»).
   Añadida.
3. Error 9. «dicen que el organizador tiene que dejar entrar»: el 144 obliga al titular del derecho
   exclusivo, no al organizador; el 145 al organizador o, si no está establecido en España, al
   titular. Reformulado.
4. Error 1 (cita cruzada). «Y lo que es prevención…»: remitía al tema 17 el riesgo eléctrico, la
   altura, las aglomeraciones y la coordinación de actividades empresariales (RD 171/2004), que el
   tema 17 declara no dar. Ahora: cargas, electricidad en montajes, calor/frío y conducción en
   misión al tema 17; la coordinación (art. 24 Ley 31/1995) al tema 9 del común. La fila del RD
   171/2004 en «Normativa» se cambia por la Ley 31/1995, art. 24, sólo nombrada.
5. Error 1. «El cuaderno ATA» y «Lo que este tema no da» decían que el convenio internacional del
   ATA no se había leído; el tema 12 lo desarrolla (Convenio de Estambul). Ahora remiten al tema 12.
6. Antecedente: «Y de la iluminación, lo que importa a producción:» seguido de «de todo esto»
   (sin antecedente tras el recorte). Fundido en una frase.
7. Error 9. *Mobycam*: «sobre un raíl en el fondo o el borde de la piscina» sin fuente (RTVE no
   pudo leer la ficha del fabricante). Quitado.
8. «Seis de esas diez tareas se ejercen fuera del centro»: no es literal ni exacto (la recepción de
   señales es en el centro). Ahora «tienen su parte en exteriores… (lectura de la ficha)».
9. «Libro de Estilo» → «Libro de estilo».
10. Art. 19.2 cotejado con el consolidado: actualizadas portada («Redacción que se estudia»),
    «Normativa» y «Trazabilidad»; añadida a «Trazabilidad» una fila con las lecturas de hoy
    (fichas y Libro de estilo).

Pasajes cambiados releídos: cada «ese artículo», «el 144», «el 145», «el tema N» tiene antecedente.

## Lentes automáticas

- `negritas.py` (Ley 13/2022, DOUE, RD 393/2007, RD 524/2023, convenio, Libro, Cámara, Contrato-
  programa, Carta, Cámara de España, UIT-R, EUR-Lex): 118 cotejadas, 35 «no está». Son rótulos,
  supuestos, citas del Libro partidas por salto de página o ligaduras (comprobadas a mano), y citas
  del RGC y del RD 517/2024, que están en pasajes copiados del común (sus volcados no están en
  `fuentes/`; no se reverifican). Un «¿art. 40? al menos 30 metros»: pasaje copiado, falso positivo
  por falta del volcado del RD 517/2024.
- `refutar_exactitud.py`: 38 «no literales», todas falsas (epígrafes del Libro de estilo, «4.4»,
  leídos como «art. 4» de una norma BOE). Ninguna de los arts. 144, 145 o 19.
- `refutar_modo.py`: 0. `refutar_prosa.py`: 0. `indice.py`: 66 epígrafes, índice sin cambios.

## Lo que queda abierto

- Reglamento (UE) 376/2014: no leído (declarado en el tema).
- RGC y RD 517/2024 sin volcado local: el tema sólo los usa en pasajes copiados del común.
