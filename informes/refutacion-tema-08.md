# Refutación del tema 8 del general

Ley 31/1995, de Prevención de Riesgos Laborales. Legislación consolidada, `boe.py` sirve, y
esta vez **la fuente se portó bien**: 88 bloques, ninguna reforma cruzada, y una diferencia de
solo dos bloques entre la redacción del corte y la de hoy. Lo que dio trabajo fueron **las
lentes**, otra vez, y una **derogación masiva que no se ve leyendo el índice**.

## 0 · Lo que dijo la fuente

Volcada la norma entera en las dos fechas —**vigente hoy** y **21 de diciembre de 2022**—:

- **88 bloques.** **Ninguna reforma cruzada detectada.**
- **24 preceptos con más de una redacción**, leídos enteros: artículos **3, 5, 7, 9, 14, 16,
  23, 24, 26, 30, 31, 32, 39, 42, 43, 45, 46, 47, 48, 49, 50, 51 y 52**, y la **disposición
  adicional quinta**, que tiene cuatro.
- **Entre el corte y hoy solo cambian dos bloques de 88**: el **artículo 7.1.a)** y la
  **disposición adicional quinta**, ambos por la **disposición final primera de la Ley 1/2026,
  de 8 de abril, integral de impulso de la economía social**. Ninguno toca los capítulos III,
  IV ni V, y ninguno afecta a un artículo preguntado. Van en la nota de actualización.
- **La foto que cita el programa es anterior al corte.** «Última actualización publicada
  08/09/2022» es el **Real Decreto-ley 16/2022**; el corte es el 21 de diciembre. **El texto
  que cita el programa y el examinable son el mismo**, cosa que no había pasado en ningún tema
  anterior de este bloque.

### El hallazgo de la fuente: el capítulo VII está casi entero derogado

**Nueve bloques traen nota del BOE sobre derogación**, todos del capítulo VII y todos del
**Real Decreto Legislativo 5/2000 (LISOS)**, con efectos **desde el 1 de enero de 2001**:

- **artículos 46, 47, 48, 49, 50, 51 y 52**: derogados enteros;
- **artículo 42**: derogados los apartados **2, 4 y 5**;
- **artículo 45**: derogados los **párrafos primero y segundo del apartado 1** y **todo el
  apartado 2**.

**No se ve leyendo el índice**: los rótulos siguen ahí, «Infracciones leves», «Infracciones
graves», «Sanciones», y solo el cuerpo dice «(Derogado)». Un tema escrito de memoria —o
copiado de un manual antiguo— enumera con toda naturalidad las infracciones de los artículos
46, 47 y 48 de la Ley 31/1995, que están hoy en los **artículos 11, 12 y 13 de la LISOS**. Es
el **error 7 del catálogo** servido en bandeja, y el tema lo advierte en su segundo epígrafe
con la tabla precepto a precepto.

## 1 · Las lentes: dos fallos propios, los dos del apartado 10

Sobre este tema las lentes **sí arrancaron** —544 negritas comprobadas de entrada—, pero al
mirar a qué artículo atribuían cada cosa aparecieron dos agujeros. Ninguno da error: los dos
**atribuyen mal en silencio**, que es la firma del apartado 10.

### Fallo 1 · El artículo 32 bis no se comprobaba nunca

El patrón de la fuente estaba anclado en `Artículo (\d+)$`. **«Artículo 32 bis» no acaba en
dígito**, así que:

- **no entraba en el diccionario de artículos** y **nunca se comprobaba**;
- y, peor, **su texto en el tema se contrastaba contra el artículo 32**, que habla de otra cosa
  —la prohibición a las Mutuas—. Las negritas sobre recursos preventivos salían como «no
  literales» del artículo 32 y quien mirase la lista concluiría que el tema inventa.

Arreglado el patrón en **las dos lentes** —`bis`, `ter`, `quáter`, `quinquies`— y hechas
cadenas las claves, porque **«32 bis» es un artículo y no un número**. El artículo 32 bis pasó
a comprobarse: **16 negritas suyas**, de las que la lente marca nueve —cuatro son rótulos del
propio tema, cuatro son texto de la **disposición adicional decimocuarta** explicada a
continuación y una es la cita de la **Ley 54/2003**—. **Error de fondo, uno**, corregido: el
tema decía «permaneciendo» donde el 32 bis.3 dice «**debiendo permanecer**».

### Fallo 2 · Una remisión dentro de una frase abría epígrafe

El tema explica el artículo 13 y dentro dice «conoce las actuaciones que desarrollen las
Administraciones… a que se refieren los **artículos 7, 8, 9 y 11**». Ese marcador **abría
bloque**, y a partir de ahí **todo el resto de la explicación del artículo 13 —composición,
votos, quién preside, secretaría, funcionamiento— se comprobaba contra el texto del artículo
7**. La lente informaba, contaba y no se quejaba de nada.

El arreglo tuvo dos intentos, y el primero estaba mal:

1. **Primer intento**: descartar todo marcador que no empiece renglón. Bajó los falsos
   positivos, pero **dejó de mirar catorce marcadores del tema 7** —los artículos **105**,
   **111 a 113**, **139 a 142** y **98**, descritos en una línea dentro de una frase—. Cambiar
   una atribución mala por un artículo sin mirar es cambiar un problema por otro peor. Se
   detectó comparando las cifras antes y después: **de 261 negritas comprobadas a 241**. Una
   comprobación que baja al «arreglarla» es la señal.
2. **Segundo intento, el que está**: distinguir las dos clases de marcador. El que **abre
   epígrafe** —párrafo, encabezado, viñeta, fila de tabla o cita— manda sobre **todo su
   párrafo**, y una remisión interior ya no se lo corta. El que va **dentro de una frase** se
   queda **solo con su frase**: si es una remisión, apenas arrastra ruido; si es una mención
   con contenido, se comprueba igual.

Resultado sobre el tema 7, que es donde más se notaba: **de 241 negritas a 250**, y **un
hallazgo nuevo** en los artículos 97 y 98, que el tema trataba juntos en una línea y
atribuía mal —decía «los programas **deben** tener calificación por edades» colgando del
artículo 97, cuando eso es el **artículo 98.1**, «**están obligados a**». Corregido en el tema
7, y declarado abajo.

## 2 · Hallazgos del tema 8

La lente de modo verbal y salvedades dio **once**. Ocho eran reales y están corregidos; tres
son falsos positivos declarados.

| Art. | Qué faltaba |
| --- | --- |
| **18.1** | La salvedad estaba, pero escrita con un «pero» en vez del **«no obstante»** de la norma. Reescrita con la palabra de la ley |
| **28.5** | Faltaba **«sin perjuicio de lo dispuesto en el párrafo anterior»**: la responsabilidad de la empresa usuaria sobre las condiciones de ejecución **no decae** porque la ETT deba formar e informar |
| **31.3** | Faltaba que la asunción por servicio ajeno se entiende **«sin perjuicio de cualquiera otra atribución legal o reglamentaria de competencia a otras entidades u organismos»** |
| **34.3.d)** | Faltaba la excepción: **«ello no obstante, podrán constituirse Comités de Seguridad y Salud en otros ámbitos cuando las razones de la actividad y el tipo y frecuencia de los riesgos así lo aconsejen»**. El tema daba como absoluta la regla del Comité único |
| **35.4** | Faltaba el **«no obstante lo dispuesto en el presente artículo»** que abre la habilitación al convenio |
| **36.2.d)** | Faltaba **«sin perjuicio de lo dispuesto en el artículo 40»** en materia de colaboración con la Inspección |
| **37.1** | Otra vez un «pero» donde la norma dice **«no obstante lo anterior»**, justo en la excepción que se pregunta: qué tiempo **no** se imputa al crédito horario |
| **45.1** | Faltaba señalar que lo que queda vivo del apartado arranca con un **«no obstante lo anterior»** |

Y dos correcciones de literalidad que salieron de la lente de exactitud:

- **Artículo 6.1.d)**: el tema decía «procedimientos de evaluación de riesgos»; la ley dice
  **«procedimientos de evaluación de los riesgos para la salud de los trabajadores»**.
- **Artículo 32 bis.3**: el tema decía «permaneciendo en el centro de trabajo»; la ley dice
  **«debiendo permanecer»**. Es la diferencia entre describir y obligar, que es el **error 4
  del catálogo**.

## 3 · Cifras

**Ninguna cifra del tema falta de la ley.** Comprobadas una a una contra el texto: la escala
completa de Delegados de Prevención (**2/3/4/5/6/7/8** con sus siete tramos, más **hasta 30** y
**de 31 a 49**), los umbrales de **6**, **10**, **25** y **50** trabajadores, los **quince días**
del informe del Delegado, las **veinticuatro horas** de la autoridad laboral y los **tres días
hábiles** de la impugnación, los **doscientos días** del cómputo, la **incapacidad superior a
un día** del artículo 23.1.e), el **33 %** de la disposición adicional quinta y los **tres
meses** de la entrada en vigor.

## 4 · Lo que la lente sigue marcando, y por qué no se toca

Quedan **tres hallazgos**, los tres del mismo tipo: **texto de una disposición adicional
explicado dentro del bloque del artículo con el que enlaza**.

| Marca | Qué es de verdad |
| --- | --- |
| art. 9 «la norma solo dice *podrán* y el tema dice *deben*» | El «deberán pertenecer a los grupos de titulación A o B» es de la **disposición adicional decimoquinta**, no del artículo 9. La lente no trocea las disposiciones |
| art. 35 «la norma solo dice *podrán* y el tema dice *debe*» | El «deberá estar previsto en sus Estatutos» es de la **disposición adicional décima** |
| art. 3 «la norma solo dice *puedan* y el tema dice *obligadas*» | Es una glosa que cita el enunciado de examen —«¿qué empresas están obligadas a cumplir la Ley 31/1995?»—, no una cita de la norma |

Los tres se dejan porque **poner la disposición junto al artículo que la completa es lo que
sirve para estudiar**, y separarlas para contentar a la lente empeoraría el tema. La lente no
sabe leer disposiciones adicionales: eso es una carencia conocida, no un error del tema.

De las **243 negritas «no literales»**, revisadas todas: son rótulos del propio tema
(«**16.2. Los dos instrumentos esenciales**»), paráfrasis que resuelven una remisión —el tema
escribe «las visitas de las letras a) y c) del **artículo 36.2**» donde la ley dice «del número
2 del artículo anterior»— y datos de trazabilidad que no están en el articulado, como la
**Ley 35/2014** o la **Ley 54/2003**, comprobados en las notas de reforma del BOE.

## 5 · Prosa

Cero relleno y cero frases repetidas entre epígrafes. Cinco siglas sin presentar, corregidas:
**AGE** (sustituida por el nombre entero), **CE**, **EPI**, **ETT** y **FSP**. El detector sigue
marcando ETT y FSP porque no reconoce la forma en que se presentan, pero un lector sí.

**Y una desviación que se declara en vez de disimularla.** El apartado 9 del manual da como
referencia **unas 2.000 palabras y unas 130 líneas** de esquema. El de este tema son
**3.856 palabras y 199 líneas**, tras dos pasadas de compresión que solo quitaron explicación
—de 4.018 palabras a 3.856—. La razón: **54 artículos y 18 disposiciones adicionales**, y un
temario en el que el tribunal pregunta enumeraciones cerradas y literales (las ocho
definiciones del artículo 4, los nueve principios del 15, las seis obligaciones del 29, los
siete tramos del 35.2). La regla del manual para esta tensión es **quitar explicación y nunca
el dato normativo**, y eso es lo que se ha hecho; el resultado sigue por encima de la
referencia y queda dicho.

## 6 · Efecto sobre lo ya cerrado

Los dos arreglos de las lentes obligaban a repasar los seis temas anteriores. Cifras finales:

| Tema | Negritas comprobadas | Hallazgos de modo |
| --- | --- | --- |
| **1 · Constitución** | 463 | **3** (falsos positivos ya documentados; uno menos que antes) |
| **2 · Ley 17/2006** | 176 | **0** |
| **3 · Ley 5/2017** | 0 | **0** — no es un pase: la norma tiene «Artículo único» y se verificó a mano |
| **4 · Ley 8/2009** | 67 | **0** |
| **5 · Convenio Colectivo** | 486 | **3** (los falsos positivos conocidos) |
| **7 · Ley 13/2022** | 250 | **11** (las salvedades declaradas de artículos resumidos en una línea) |
| **8 · Ley 31/1995** | 556 | **3** (los declarados arriba) |

**Fichero tocado fuera del tema, declarado**: `temas/general/07-ley-13-2022.md`. Se reescribió
la línea de los artículos 97 y 98 —ahora **«Arts. 97 y 98»**, con **«utilizarán un sistema de
descriptores»** para el 97 y **«están obligados a que los programas emitidos dispongan de una
calificación por edades»** para el 98— porque el tema los trataba juntos y la lente, al
comprobarlos por fin, atribuía al 97 lo que dice el 98. Nada más se ha tocado de otros temas.

## Resumen

| | Hallazgos | Estado |
|---|---|---|
| Derogación invisible en la fuente | **9 bloques del capítulo VII** | recogida en el tema con tabla precepto a precepto |
| Lentes ciegas | **2 fallos** (artículos «bis» sin comprobar; remisión dentro de frase abriendo epígrafe) | corregidos, con un primer intento fallido que también se corrigió |
| Hallazgos de fondo en el tema | **10** | corregidos |
| Cifras inventadas | **0** | — |
| Falsos positivos declarados | **3** | la lente no trocea disposiciones adicionales |
| Esquema por encima de la referencia | **3.856 palabras / 199 líneas** | declarado, con la razón |
