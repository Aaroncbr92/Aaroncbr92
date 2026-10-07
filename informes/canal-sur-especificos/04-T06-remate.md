# 04 · Ayudante de Producción · Tema 6 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/06-apoyo-a-la-planificacion-de-recursos-humanos-y-tecnicos.md`.
Rematado el 06-10-2026 (el encargo fecha el 24-09-2026). Entrada: `04-T06-refutacion.md` (0 graves,
1 menor, 2 lagunas) y `04-T06-preguntas.md` (preguntas 14 y 15).

Ficheros tocados: el tema y este informe. Ninguno más (el tema 12 no se toca).

**Amplió: sí** (L1 y L2 añaden contenido nuevo). Procede la fase 5 bis sobre los pasajes 1 y 2.

## Fuentes releídas hoy (06-10-2026)

| Fuente | Qué se comprobó | Resultado |
|---|---|---|
| Decreto 54/1989, BOJA 31/1989 (`produccion/decreto-54-1989-boja-31-1989.txt`, l. 74) | Art. 10.2.a | «comience antes de las veintidós horas o termine después de las quince horas»: disyuntiva confirmada |
| Compilación del SAS (`produccion/sas-decreto-54-1989-texto-compilado.txt`, l. 263-265, 1128-1650) | Art. 10.2.a; anexo III y sus notas; cabecera (incorpora hasta la Orden de 20/09/2002) | 10.2.a igual; nota «*Anexo III redactado según modificación efectuada por artículo 2 del D. 404/2000»; la Orden de 2002 sólo anota el anexo II.A |
| Decreto 404/2000, BOJA Normativa Consolidada (`produccion/decreto-404-2000-boja-138-2000.txt`, l. 51-151, 172) | Anexo III completo, columnas, regla de Madrid; análisis jurídico | Cifras de los nueve países citados coinciden en ambas fuentes |
| Orden 11/07/2006 consolidada (`produccion/orden-2006-07-11-indemnizaciones-consolidada-2024.txt`, l. 13, 21, 31, 49) | Preámbulo, art. 2, nota sobre anexo III | Sólo fija para el extranjero la regla de Madrid |
| Tema 12 del puesto (l. 590 y 722) | Remisión a este tema | M1 confirmado (las líneas del informe de refutación, 532 y 658, estaban desplazadas) |

## Correcciones y lagunas

| Id | ¿Se aplica? | Por qué |
|---|---|---|
| M1 (remisión circular) | Sí | Confirmado en el tema 12 |
| L1 (10.2.a, comisión de mañana) | Sí | Letra confirmada en dos fuentes |
| L2 (anexo III por países) | Sí, con un ajuste | La cita «Anexo III redactado por el artículo 2 del D. 404/2000» que propone el informe no es literal (la fuente dice «Anexo III redactado por el  artículo 2 del  D.[ANDALUCIA]  404/2000»): se dice en redonda, sin negrita. Se añaden Marruecos, Estados Unidos y Resto del Mundo; la «Por manutención» se da con el rótulo de la fuente, sin llamarla «pernoctando», que la fuente no dice |

## Pasajes cambiados

1. **«La dieta y su devengo», tabla del artículo 10.2**: nueva fila «De 9:00 a 13:30, sin pernoctar
   | No | Sí (empieza antes de las 22 h) | Media manutención, según la letra del 10.2.a» y un párrafo
   que lo declara lectura del tema sobre la letra (la letra no distingue; ninguna fuente leída la
   interpreta).
2. **«Las cuantías vigentes», párrafo del extranjero**: sustituye «el tema no da cifras por país»
   por la redacción del anexo III (Decreto 404/2000), la regla de Madrid en negrita literal, tabla
   de nueve países (Portugal, Francia, Reino Unido, Bélgica, Alemania, Italia, Marruecos, Estados
   Unidos, Resto del Mundo), ejemplo de París, salvedad (pesetas/euros de 2000; la Orden de 2002 no
   tocó el anexo III según la compilación del SAS; no se puede descartar una actualización posterior
   sin consolidado oficial) y enlace con las cuantías del convenio (98,81 / 49,41 / 197,62) y el tope
   de la DT 7.ª, sin afirmar cómo opera.
3. **«Lo que este tema no da»**: la viñeta de la tabla por países pasa a decir que el tema da nueve
   países y que no se ha podido descartar una actualización posterior; la remisión al tema 12 queda
   sólo para la documentación (las dietas del extranjero, en este tema) (M1).
4. **«Normativa que el tema invoca»**, fila del Decreto 54/1989: «anexo I» pasa a «anexos I y III»
   en la redacción del Decreto 404/2000.
5. **«Trazabilidad»**: la fila de los Decretos modificadores añade el anexo III; fila nueva para la
   compilación del SAS.

Antecedentes releídos: «la letra a)», «el 10.2.a», «ese anexo», «ese tope», «este tema» tienen
delante su referente.

## Lentes

- `indice.py`: 19.167 palabras, 64 epígrafes (sin epígrafes nuevos; el índice no cambia).
- `negritas.py` contra Decreto 404/2000, Decreto 54/1989, Orden de 2006 y compilación del SAS: las
  negritas nuevas están en la fuente; la única que fallaba (nota del análisis jurídico) se pasó a
  redonda.
- `refutar_prosa.py`: 3 siglas (CSR, RAI, SSFF) de pasajes anteriores y copiados, ninguno tocado
  aquí; sin relleno ni negritas rotas.
- `refutar_exactitud.py` y `refutar_modo.py`: no aplican a lo nuevo (citas de anexos y documentos
  sin articulado del BOE; ningún «podrá/deberá» nuevo).
