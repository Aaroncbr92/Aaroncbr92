# Fase 5 bis · Ayudante de Realización (05) · Tema 6 · Realización multicámara en directo

Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/06-realizacion-multicamara-directo.md`.
Alcance: sólo el `###` «El cálculo hacia atrás desde la hora de salida» (nuevo en el remate, según
`05-T06-remate.md`). Las correcciones menores 1 y 2 del remate (cita cruzada y repeticiones) no se
listaron para esta fase; no se revisan.

Fuente releída el 30-09-2026 (reloj del sistema; el encargo fecha la tarea el 24-09-2026):
IMS077_3, `fuentes/canal-sur/realizador/incual-IMS077_3.txt`, p. 8, CR2.6 y CR2.7 (UC0217_3).

## Datos comprobados

- **«el tiempo acumulado se ajusta a las indicaciones del control de continuidad»**: literal de CR2.7. Correcto.
- **«la cuenta atrás y tiempos parciales»**: literal de CR2.6. Correcto.
- «al realizador y al director del programa (CR2.7)»: CR2.7 dice «transmitiendo las diferencias en
  los tiempos al realizador y al director del programa». Correcto.
- Antecedente: CR2.6 y CR2.7 están citados enteros en «Las llamadas de tiempo», justo antes. Correcto.
- Aritmética de la tabla (salida 21:30:00; 3'00'' + 8'00'' + 4'30'' + 4'00'' + 4'30'' = 24'00''):
  arranques previstos 21:25:30, 21:21:30, 21:17:00, 21:09:00, 21:06:00; desfases 0, 15'', 40'', 40''.
  Correctos.
- Método y término *backtiming*: declarados como oficio, sin disfrazarlos de norma. Correcto.

## Correcciones aplicadas (3)

1. Atribución: «(CR2.7) … (UC0217_3, CR2.6)» dejaba la UC colgada sólo del segundo criterio.
   Queda «(CR2.7) … (CR2.6); los dos criterios, de la UC0217_3, están citados enteros en «Las
   llamadas de tiempo»». Comprobado: ambos son de UC0217_3 (RP2).
2. Salvedad omitida (error 6): «tiempo acumulado … la diferencia es el mismo desfase» sólo vale si
   el primer bloque arrancó a su hora. Añadido «si el primer bloque arrancó a su hora».
3. Ejemplo: «a las 21:26:10 todavía no ha empezado» no cuadraba: la conexión (21:22:10 + 4'00'')
   termina a las 21:26:10, y la despedida arranca entonces. Queda «Si la conexión dura lo previsto,
   la despedida, que tenía que arrancar a las 21:25:30, arranca a las 21:26:10: el programa va 40
   segundos largo». El desfase (40'') no cambia.

## Lentes

- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` con IMS077_3: las dos negritas del pasaje están en la fuente; los «no está» son de
  otras fuentes (Libro de Estilo, convenio, NTP, Autocue, ficha 5351000) y de pasajes fuera de alcance.
- `indice.py`: 15.932 palabras, 64 epígrafes; la ficha («15.900 aproximadamente») sigue valiendo.

## Ficheros tocados

El tema 06 (sólo ese `###`) y este informe.
