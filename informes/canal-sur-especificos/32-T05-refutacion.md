# Productor/a (puesto 32) · Tema 5 · Refutación

Fase 4, refutar (no corrige). Tema:
`temas/canal-sur-especificos/32-productor-a/05-gestion-de-recursos-humanos-y-condiciones-de-prestacion.md`
(1.121 líneas). Fecha del encargo: 24-09-2026; fuentes leídas el 25-09-2026 (las mismas).
Ficheros tocados: este informe y `32-T05-preguntas.md`. El tema no se ha modificado.

Resultado: **0 graves, 2 menores y 3 lagunas.**

## Alcance

- **Exactitud**: sólo lo que no está en «Copiado del común» ni en «Copiado de RTVE sin cambios»
  (según `32-T05-redaccion.md`). Cotejado con la fuente:
  - X Convenio (BOJA 240/2014, `.txt`): fichas del anexo III (l. 6916-6947, 4687-4716); anexo II,
    diez filas de Productor/a (26+9+6×1+2+1 = 44); art. 21.3.1, 3.3, 3.7, 3.8, B y C (l. 541-641);
    art. 50.11 y 51 (l. 1737-1770); art. 53 entero (l. 1782-1826); cabecera de las transitorias y DT 7.ª
    (l. 2332-2340, 2596); art. 9.5 (l. 240).
  - ET (`BOE-A-2015-11430`, `boe.py --fecha 20260924`): arts. 34 (4 redacciones), 35, 36, 37.1-2 y
    40.6-7. Identificadores de las normas modificadoras comprobados en `.redacciones.tsv` y con
    `boe_buscar.py` (BOE-A-2024-26693 es la Ley 6/2024).
  - Libro de Estilo 2004, 4.4 a 4.4.4 (l. 2597-2690); Cámara de Cuentas 2018, puntos 162, 235,
    236, 250, 252, 253 y anexo 9.1; contrato-programa, punto 68 (l. 1656-1660); convocatoria 2026,
    anexo I (Granada 1, Jaén 1, Sevilla 12; no hay más filas de Productor/a) y fecha del Reglamento de
    la Mesa (l. 64, 104).
  - Todo lo anterior es **correcto**: citas literales, cifras, recuentos y remisiones cuadran.
- **Cobertura**: el tema entero contra el enunciado.

## Hallazgos de exactitud

### Graves

Ninguno.

### Menores

1. **Plus de pernocta sin su condición (error 6)**. L. 723 (tabla «Salida, desplazamiento temporal y
   traslado», fila «Salida»: «fuera de Andalucía, plus de pernocta») y l. 1055-1056 (comprobación 6:
   «fuera de Andalucía, plus de pernocta»). El art. 53.4 lo limita: «Este plus se hará efectivo sólo y
   exclusivamente en los casos en los que el/la trabajador/a [...] prolongue su jornada de trabajo más
   de dos horas sobre su jornada ordinaria». El tema lo dice bien en l. 797 y l. 824-826, pero en estos
   dos pasajes (no copiados del común) se lee como automático. Propuesta: añadir «si la jornada se
   prolonga más de dos horas» en ambos.
2. **«Sin horas extraordinarias» atribuido a todo turno de noche (error 6)**. L. 1039 (tabla «Convenio y
   ET», fila «Nocturno»: «Ocho horas diarias de promedio en quince días; sin horas extraordinarias
   (36.1)» / «Acorta el turno de noche y no le carga horas extra»). El art. 36.1 ET prohíbe las horas
   extraordinarias a los **trabajadores nocturnos** en el sentido del propio artículo (al menos tres
   horas de su jornada diaria, o un tercio de la anual, en periodo nocturno), no a cualquiera que haga un
   turno de noche puntual. El epígrafe «Lo que añade el ET» (l. 510-516) sí da la definición. Propuesta:
   «trabajadores nocturnos (36.1): ocho horas de promedio en quince días; sin horas extraordinarias».

## Cobertura del enunciado

Las ocho materias del enunciado tienen rúbrica propia y en su orden (dimensionamiento, convocatorias,
turnos, jornadas, desplazamientos, dietas, coordinación territorial, normativa laboral interna). La
remisión al común de vacaciones y permisos, al tema 14-15 de la prevención a turnos y al tema 11 de los
menores es correcta.

### Lagunas (se amplía el tema)

1. **RD 1561/1995, de jornadas especiales, art. 19 (trabajo a turnos)** — `BOE-A-1995-21346`, redacción
   única, leída con `boe.py --fecha 20260924`. No aparece en el tema, que presenta las doce horas entre
   jornadas como absolutas (l. 498-499, l. 1036). El art. 19.2: «cuando al cambiar el trabajador de turno
   de trabajo no pueda disfrutar del descanso mínimo entre jornadas establecido en el apartado 3 del
   artículo 34 [...] se podrá reducir el mismo, en el día en que así ocurra, hasta un mínimo de siete
   horas, compensándose la diferencia hasta las doce horas establecidas con carácter general en los días
   inmediatamente siguientes»; el 19.1 permite acumular por periodos de hasta cuatro semanas el medio día
   del descanso semanal del art. 37.1 ET. Encaja en «Turnos › Lo que añade el ET»; conviene decir a la vez
   que el art. 12.b.2 del convenio fija las doce horas como condición mínima, y que el tema no decide si
   la reducción reglamentaria cabe en la RTVA (no hay fuente publicada que lo aclare). Pregunta 7: a
   medias.
2. **ET 36.3, párrafo tercero, y 36.2**. El tema cita los dos primeros párrafos del 36.3 y omite: «Las
   empresas que por la naturaleza de su actividad realicen el trabajo en régimen de turnos, incluidos los
   domingos y días festivos, podrán efectuarlo bien por equipos de trabajadores que desarrollen su
   actividad por semanas completas, o contratando personal para completar los equipos necesarios durante
   uno o más días a la semana.» Es regla de dimensionamiento de equipos a turnos. Conviene añadir también
   el 36.2 (retribución específica del trabajo nocturno por negociación colectiva), que enlaza con el
   complemento de nocturnidad del art. 50. Pregunta 8: no.
3. **ET 35.2, reducción proporcional del tope de horas extraordinarias**. El tema (l. 664-667, l. 682)
   da las ochenta horas y la exclusión de las compensadas en cuatro meses, pero omite la frase del mismo
   apartado: «Para los trabajadores que por la modalidad o duración de su contrato realizasen una jornada
   en cómputo anual inferior a la jornada general en la empresa, el número máximo anual de horas
   extraordinarias se reducirá en la misma proporción que exista entre tales jornadas.» Pesa aquí porque
   la DT 1.ª A.b reduce un 10 % la jornada del personal temporal. Pregunta 9: no. (Es también una
   salvedad omitida, error 6, pero se cuenta una sola vez, como laguna.)

## Preguntas

`32-T05-preguntas.md`: 15 preguntas (11 de teoría, 4 prácticas o de aplicación). **12 enteras, 1 a
medias (7), 2 no (8, 9).** Las tres fallidas coinciden con las lagunas 1 a 3.

## Sin hallazgo (comprobado y descartado)

- La remisión del art. 21.3.B al preaviso de treinta días del 3.3: el tema da los dos textos y no
  decide; correcto.
- «Sólo el Reglamento de la Mesa está publicado» (l. 165) frente a «Sin publicación oficial; portales
  de transparencia» (l. 1074): no se contradicen (publicado, pero no en diario oficial).
- «Málaga es el único centro territorial con plaza de Productor/a de radio (CSR)»: correcto (Sevilla no
  es centro territorial; Algeciras y Jerez tienen Presentador/a productor/a).
- «Son las catorce que resta el artículo 10» (11 + 1 + 2): cuadra con el ET 37.2.
