# Refutación · Sonido, los diecisiete temas

**Siglas de este informe**: el protocolo de internet (**IP**); la Sociedad de Ingeniería de Audio
(**AES**) y la Unión Europea de Radiodifusión (**EBU**, y **UER** en español); la interfaz digital
multicanal de audio (**MADI**); el kilohercio (**kHz**) y el decibelio (**dB**).

**Las cuatro lentes del proyecto pasadas sobre los diecisiete temas del específico de Sonido**, y lo
que sale de la comprobación contra las fuentes.

## Lo que dicen las lentes

| Lente | Qué mira | Resultado |
|---|---|---|
| `refutar_exactitud` | Cada negrita dentro de un bloque anclado en un artículo, contra el texto de ese artículo | **No aplicable: ningún tema de este bloque cita un articulado.** Las unidades legales se citan **celda a celda de un cuadro**, no por artículo |
| `refutar_modo` | Que el tema no imponga donde la norma faculta, y que recoja las salvedades | **Cero hallazgos** en los diecisiete temas |
| `refutar_prosa` | Relleno, frases repetidas y siglas sin presentar | **Cero hallazgos** en los diecisiete temas y en sus diecisiete esquemas |
| `refutar_documento` | Cada negrita contra el documento no articulado | **No aplicable como lente completa**, y se explica más abajo |

**Ninguno de los diecisiete temas se apoya en un articulado**, así que la lente de exactitud
**devolvería «0 comprobadas, 0 no literales» en los diecisiete**, y **ese cero no dice nada sobre el
tema**. Es exactamente el aviso del apartado 10 del manual: **una lente que devuelve cero es la señal
de peligro, no el aprobado.** Por eso la verificación de este bloque se ha hecho por otros caminos,
que este informe documenta uno a uno.

## El hallazgo de este bloque: las unidades son legales

**Es el resultado más importante de la refutación de Sonido**, y **obligó a volver sobre temas de
otras ocupaciones ya escritos.**

**El Real Decreto 2032/2009** (`BOE-A-2010-927`), por el que se establecen las unidades legales de
medida, **pone en el Boletín Oficial del Estado el pascal, el voltio, el ohmio y el faradio**, y lleva
además **una nota sobre el decibelio**. Es decir: **la unidad de presión sonora que pregunta la
cuestión 89 no es convenio del oficio, es derecho vigente.**

**La regla que este bloque deja para el resto del proyecto, y que se ha escrito en el manual de
trabajo**: **antes de declarar «oficio» una materia técnica, hay que preguntarse si sus magnitudes
tienen unidad legal.** **Se hizo, y aparecieron el lux, la candela por metro cuadrado y la luminancia
del temario de Realización Televisión**, que hasta entonces iban como oficio.

**Cómo se cita**: **una fila de cuadro no se puede citar como prosa corrida**, de modo que **se cita
celda a celda, separadas por `·`**, y **el tema dice expresamente que lo hace así.**

## Lo que no se ha podido verificar y por qué

**Cuatro respuestas descansan en la plantilla oficial**, y **el temario lo declara en el tema, en el
cuadro de datos y en el informe de cobertura.** **No se describe lo que no se ha visto ni se atribuye
a una fuente lo que no se ha leído:**

1. **El modelo de micrófono para bombo de batería** es memoria de catálogo de fabricante. **Este
   proyecto no ha volcado ningún catálogo**, y el tema aporta la regla de la familia.
2. **El gesto de la mano del control de radio** no está en ninguna fuente pública. **Es un convenio
   de casa**, y **es la respuesta peor documentada de las ochenta y seis.**
3. **El tamaño máximo del bed en Dolby Atmos** es una cifra de especificación comercial no
   consultada.
4. **La frecuencia máxima de muestreo de AES67** está en un texto tras muro de pago que **no se ha
   leído**, y así consta en `fuentes/normas-tecnicas/AES-normas-de-audio.md`.

**A ellas se añade el número de flujos de la pregunta 47**, dato de implementación del fabricante,
**aunque el ancho de banda de esa misma pregunta sí sale de la cuenta y la cuenta queda escrita.**

## Las cuatro salvedades sobre respuestas correctas

**Ninguna respuesta oficial de este bloque es errónea.** **Cuatro llevan nota, y la nota va impresa
junto a la pregunta en el libro:**

- **La pregunta 44 tiene dos opciones idénticas.** No es un fallo de extracción: **la c) y la d) dicen
  exactamente lo mismo.** La respuesta sigue siendo correcta.
- **La fórmula de la pregunta 36 tiene un desajuste de unidades con su propio enunciado**: sólo da
  milisegundos con la frecuencia en hercios, y el enunciado la escribe en kilohercios.
- **La pregunta 46 pide «lo más aproximado» y hace falta**: el valor exacto es 2,67 y la opción
  marcada es 2,5, que es la más próxima de las cuatro.
- **La pregunta 82 llama al multímetro «herramienta fundamental para medir la impedancia»**, y un
  multímetro corriente mide resistencia en continua. **Es la mejor de las cuatro opciones y no es
  exacta.**

## El error del propio anexo

**El punto 12 del anexo de la convocatoria dice «Norma AES R-128».** **La R 128 no es una norma de la
Sociedad de Ingeniería de Audio: es una recomendación de la Unión Europea de Radiodifusión.** **El
temario lo declara**, porque **un opositor que busque «norma AES R 128» no encontrará el documento.**

## Por qué la lente de documento no cierra este bloque

**`refutar_documento` contrasta cada negrita contra un documento suelto no articulado.** **Este bloque
no tiene ese documento**: las normas que lo sostendrían —AES3, AES10, AES11, AES67, la R 128— **están
tras muro de pago y no se han leído**, y así consta. **Pasarle la lente sin fuente devolvería todas
las negritas como «no literales»**, que es ruido, no verificación.

**Lo que sí se ha hecho en su lugar**, tema por tema:

| Camino de verificación | Dónde se ha usado |
|---|---|
| **Cálculo escrito y comprobable** | Temas 1, 2, 8, 9, 10 y 16: la impedancia en paralelo, la aritmética del decibelio, el retardo a tempo, el tamaño de fichero, la alineación de altavoces y el ancho de banda |
| **Cita literal de norma del BOE** | Temas 1 y 2: las unidades legales, celda a celda |
| **Cita literal de presentación pública de norma** | Tema 17: qué normas de la Sociedad de Ingeniería de Audio existen y qué numeración tienen, **sin nada de su contenido interno** |
| **Declaración expresa de dependencia de la plantilla** | Temas 5, 12, 15 y 16 |
| **Desarrollo contra el programa, sin banco** | Tema 3, que no tiene ni una pregunta |

## Lo que queda dicho

**Diecisiete temas, cero hallazgos de modo y cero de prosa.** **Cuatro respuestas declaradas
dependientes de la plantilla, cuatro salvedades escritas junto a su pregunta y un error de
nomenclatura del propio anexo, declarado.** **Ninguna respuesta oficial de este bloque es errónea.**
