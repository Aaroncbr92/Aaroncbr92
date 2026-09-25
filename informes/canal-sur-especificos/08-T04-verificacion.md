# Puesto 08 · Tema 4 · Fase 3 · Verificación

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/04-soportes-y-accesorios.md`.
Leído: `ENCARGO.md`, enunciado 08, `08-T04-redaccion.md`, § Tema 4 y tabla de fuentes de
`08-investigacion-B-captacion.md`, fila 8/4 de `canal-sur-reuso/imagen-iluminacion.tsv`.

«Copiado del común»: ninguno, nada que saltar. Lentes: tema técnico sin norma → sólo
`refutar_prosa.py` e `indice.py` (no proceden `negritas.py`, `refutar_exactitud.py`, `refutar_modo.py`).

## Fuentes releídas (todas el 24-09-2026)

| Fuente | Dónde | Resultado |
|---|---|---|
| Libro de estilo CS, 1.ª ed. marzo 2004 | `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt` (l. 1962-1967, 2790-2799, 4702-4705, 116-117, 2837-2845) | Las cinco citas, literales; páginas 59, 80 y 130 correctas; no nombra cardán, *slider*, PTZ ni grúa |
| Blackmagic, manual ATEM (dic. 2024 según README de `fuentes/fabricantes/`) | `fuentes/fabricantes/Blackmagic_ATEM_manual-es.txt` (l. 2803-2813, 4451-4503) | Citas literales; dos correcciones (abajo) |
| DJI RS 4 Pro, ficha | `fuentes/fabricantes/DJI_RS-4-Pro_ficha.txt` (descargada 02-09-2026) | Todos los valores confirmados; corrección de forma en la carga |
| LiveU LU800 | `fuentes/fabricantes/LiveU_LU800_ficha.txt` (l. 16, 22) | Dos citas literales |
| Manfrotto MVS060A | `manfrotto.com/global-en/camera-slider-60cm-mvs060a/`, descargada hoy con agente de navegador (HTTP 200) y cotejada línea a línea | Cita del extractor no literal; corregida |
| Tiffen «Steadicam» | `tiffen.com/pages/steadicam`, descargada hoy (HTTP 200) | Cita literal (con salto de línea entre comillas en el HTML); no da inventor ni año, como declara el tema |
| RTVE: `informacion-grafica/05`, `montaje-equipos/04`, `/07`, `/08`, `realizacion-tv/14` | leídos enteros o por los pasajes | Lo copiado es literal salvo negritas y añadidos de enlace; nada de catálogo reintroducido |

## Correcciones aplicadas

1. **Error 9 (Manfrotto).** «**10 kg safety payload**» no está en la página: pone «Safety Payload
   Weight: 10 kg». «60 cm de recorrido» no consta: 60 cm es el nombre del producto («Camera Slider,
   60cm»). Reescrito con los literales; añadida la cita del montaje («on a tripod, on the ground or
   any level surface»). Actualizada la fila de Trazabilidad.
2. **Error 3 (ATEM).** «documenta las tres vías de control» con una tabla de cuatro filas → palanca
   del panel + tres vías de conexión (serie, red IP, retorno SDI).
3. **Error 6 (ATEM).** La frase del puerto RS-422 es del modelo ATEM 4 M/E Constellation, puerto
   «denominado REMOTE»: salvedad añadida.
4. **Error 9 (Libro de estilo).** Los planos fijos de colchón se piden para «panorámicas y
   'travellings'» (5.3.2), no «para cualquier movimiento»: corregido.
5. **Error 8/9 (Documentos citados).** El 5.2 se titula «La grabación adecuada», no «grabación en
   exteriores»: corregido.
6. **Error 9 (RTVE adaptado).** «La grúa pequeña, de brazo corto, se llama *jib* o *mini jib*»: RTVE
   (realizacion-tv/14) da *mini jib* = grúa pequeña y *jib* = grúa de brazo rígido o pluma. Corregido.
7. **Error 6 (RTVE, choque de vocabulario).** montaje-equipos/04 llama cangrejo a la base de ruedas;
   realizacion-tv/14 recoge «cangrejo (o araña)» como soporte que evita que el trípode resbale.
   Añadida una salvedad de oficio en «Trípode».
8. **Afirmación absoluta.** «el único criterio publicado de la casa sobre soportes» → «… que se ha
   localizado».
9. **Forma (DJI).** «Tested Payload» y «4.5 kg (10 lbs)» están en líneas distintas de la ficha: se
   citan por separado.
10. **Siglas (error 5).** DJI añadida a la lista de marcas. `refutar_prosa.py`: queda un aviso,
    VISCA, falso positivo (presentada en siglas). `indice.py`: índice sin cambios (7.958 palabras).

## Comprobado y sin cambio

Literales del Libro de estilo 3.17.1, 5.2 y 9.2.12.4 y su carácter de recomendaciones; los datos
DJI (recorridos, velocidades, autonomía con su salvedad, peso, puertos); LiveU IP Pipe y producción
remota; ATEM VISCA IP, retorno SDI, varias unidades, sensibilidad. RTVE: tablas y pasajes de la
cadena, cabezas, cola de milano, pedestal, grúa, balances, técnicas, cabeza caliente, líneas y
montaje, PTZ, CCU/RCP: literales. «Pasivo es, por definición, lo que no consume energía» está en
realizacion-tv/14 (se mantiene como oficio). RS-422 como serie diferencial: oficio de RTVE; el ATEM
sí confirma RS-422 para cabezales.

## Lo que no se ha podido confirmar

Nada nuevo que quitar además de lo corregido. Sigue declarado en el tema: medidas de copa, cargas de
catálogo, longitud del par trenzado, inventor/año de Steadicam, orden de equilibrado de un cardán.

## Ficheros tocados

`temas/canal-sur-especificos/08-camara-operador/04-soportes-y-accesorios.md` y este informe. Copias
web descargadas sólo al scratchpad (no añadidas a `fuentes/`).
