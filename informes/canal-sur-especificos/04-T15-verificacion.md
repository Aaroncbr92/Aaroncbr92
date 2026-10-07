# 04 · Ayudante de Producción · Tema 15 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/15-herramientas-ofimaticas-y-aplicaciones-de-gestion.md`.
Fecha de corte: 24-09-2026. Lecturas de esta fase: 06-10-2026 (fecha del sistema).
Ficheros tocados: el tema y este informe.

## 1. Lo copiado (sólo literalidad)

- «Copiado del común» (Operador/a Informático T11, T12; Redactor/a T03): `diff` por bloques contra
  T11 (167-178, 213-225, 624-706, 229-255, 460-468, 917-941, 578-605, 739-763, 777-805, 764-776,
  946-958, 571-577): idénticos; las únicas diferencias son los rótulos `###` que el tema reubica y los
  dos párrafos propios declarados (tema 365-366 y 394-395). T12 178-185 y Redactor T03 257-261:
  cotejo línea a línea, todas presentes. No se reverifican.
- «Copiado de RTVE sin cambios»: ninguno. La cita de segmentación tomada de RTVE `gestion/30` se
  verifica abajo (está en la página).

## 2. Fuentes releídas hoy (06-10-2026)

- RD 311/2022 (BOE-A-2022-7191), arts. 1 y 2 con `boe.py`: redacción única, vig. 05-05-2022. Art. 1.2 y
  2.1 literales.
- Ley 40/2015 (BOE-A-2015-10566), art. 2 con `boe.py`: redacción única, vig. 02-10-2016.
- Cámara de Cuentas, fiscalización RTVA-CSRTV 2018 (BOJA 36/2021, `.txt` en `fuentes/canal-sur/documentos/`):
  puntos 99, 205, 226, 227, nota 41, apartado 9.2 y 9.2.1.
- Soporte de Microsoft, descargado con curl y pasado a texto: «Conceptos básicos sobre bases de datos»,
  «Conceptos básicos del diseño de una base de datos», «¿Qué es el Autoguardado?», «Crear o programar
  una cita», «Compartir y acceder a un calendario con permisos de edición o delegación en Outlook»,
  «Filtrar datos de una tabla o un rango en Excel», «Filtrar valores únicos o quitar valores
  duplicados», «Utilice el formato condicional…», «Usar segmentaciones para filtrar datos».
  Las 77 negritas de los epígrafes nuevos (filtro, duplicados, formato condicional, segmentación,
  Autoguardado, citas, edición/delegado, bases de datos) están literales en su página. Comprobados
  también los datos en redonda: Datos > Filtro y flecha del encabezado; pestaña Segmentación >
  Conexiones de informe; Historial de versiones por fecha y hora; grupo Asistentes; cuadro Aviso;
  Responder con reunión (remitente en «Para», correo en el cuerpo).

## 3. Correcciones aplicadas

1. **Error 6 (salvedad omitida), ERP.** El punto 227 no es un juicio propio del informe de 2018 sobre
   2018: recoge «las conclusiones del informe de fiscalización» de 2015 sobre sistemas de información
   de las agencias públicas empresariales, que el punto 226 da por vigentes porque no hubo inversiones
   desde 2012. Se dice así y se añade el punto 226 a la ficha y a Trazabilidad.
2. **Error 7 (redacción derogada como vigente), Comité TIC.** El apartado 9.2 del informe dice que la
   organización interna la regulaba la Disposición nº 4, de 7-IV-2016, «sustituida el 25 de octubre de
   2019 por la Disposición nº 6». El tema presentaba las funciones en presente sin salvedad. Se añade la
   salvedad, «según el informe» en la presidencia, se reescribe la frase del ENS («El informe de 2018 sí
   atribuye…») y se añade a «Lo que este tema no da» que no consta publicada la Disposición nº 6.
3. **Error 6, Ley 40/2015, art. 2.2.b).** La cita se cortaba con comillas de cierre y sin «[…]»,
   omitiendo «que quedarán sujetas a lo dispuesto en las normas de esta Ley que específicamente se
   refieran a las mismas». Se completa con esa salvedad y se marca el corte.
4. **Error 9 (menor), Trazabilidad.** Título de hoy de la página de Access: «Conceptos básicos sobre
   bases de datos» (se aplica a Access para Microsoft 365, 2024, 2021, 2019 y 2016), no «…de las bases de
   datos» (365, 2021, 2019). Título de la página de calendario: «…de edición o delegación…», no «…o
   delegado…».
5. Ficha: extensión 9.800 → 10.000 palabras (9.986 tras las salvedades).

Antecedentes revisados: «esas conclusiones» (punto 226, delante), «la salvedad ya dicha sobre la
Disposición nº 6» (epígrafe anterior), «la que describe el informe» (Disposición nº 4, en el cuerpo).

## 4. Sin cambio

- Negrita del ERP: en el `.txt` aparece «ERP41» (llamada de la nota 41); la negrita omite la llamada.
  Literal.
- El «sector público institucional» de la Ley 40/2015 está en el art. 2.1.d) y el 2.2: correcto.
- Discrepancia «Puede ver cuando estoy ocupado» (copiado del común) frente a «Puede ver si estoy ocupado»
  de la página de edición/delegado: ya anotada en la redacción. No se toca, por ser copia del común; se
  señala al coordinador.
- Párrafo propio 129-131 («en la mayoría de los casos siguen valiendo para 2019, 2021 y 2024»): las
  páginas leídas lo confirman en su «Se aplica a» salvo segmentación (365, 2024, 2021) y citas (365,
  2024, 2021). Se mantiene: dice «la mayoría».

## 5. Lentes (el tema cita normas)

- `negritas.py` con RD 311/2022, Ley 40/2015, Cámara de Cuentas y las nueve páginas de Microsoft: 230
  negritas; las 138 «no están» son las de los pasajes copiados del común (sus páginas de Microsoft no se
  descargan, por la regla) más la del ERP (llamada de nota). Ninguna de las normas ni del informe falla.
- `refutar_exactitud.py`: 2 «no literales», falsos positivos: lee «(4.4)» del Libro de estilo como
  «art. 4».
- `refutar_modo.py`: 0 hallazgos.
- `refutar_prosa.py`: 1, falso positivo («BUSCAR», función de Excel). `indice.py`: 41 epígrafes, sin
  cambio de rúbricas.
