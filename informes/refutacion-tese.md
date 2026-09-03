# Refutación · Técnica de Equipos y Sistemas Electrónicos, los diecisiete temas

**Siglas de este informe**: la radiofrecuencia (**RF**); la Sociedad de Ingenieros de Cine y
Televisión (**SMPTE**) y la Sociedad de Ingeniería de Audio (**AES**); la interfaz digital multicanal
de audio (**MADI**); el multiplexado digital de iluminación (**DMX512**); el Instituto de Ingenieros
Eléctricos y Electrónicos (**IEEE**); el conjunto redundante de discos independientes (**RAID**); y el
gigahercio (**GHz**).

**Las cuatro lentes del proyecto pasadas sobre los diecisiete temas del específico de Técnica de
Equipos y Sistemas Electrónicos**, y lo que sale de la comprobación contra las fuentes.

## Lo que dicen las lentes

| Lente | Qué mira | Resultado |
|---|---|---|
| `refutar_exactitud` | Cada negrita dentro de un bloque anclado en un artículo, contra el texto de ese artículo | **Aplicable en un solo tema, el 17.** **13 negritas comprobadas, 0 no literales** |
| `refutar_modo` | Que el tema no imponga donde la norma faculta, y que recoja las salvedades | **Cero hallazgos** en los diecisiete temas |
| `refutar_prosa` | Relleno, frases repetidas y siglas sin presentar | **Cero hallazgos** en los diecisiete temas y en sus diecisiete esquemas |
| `refutar_documento` | Cada negrita contra el documento no articulado | **No aplicable como lente completa**, y se explica más abajo |

**Dieciséis de los diecisiete temas no se apoyan en una norma articulada**, así que la lente de
exactitud **devolvería «0 comprobadas, 0 no literales» en los dieciséis**, y **ese cero no dice nada
sobre el tema**. Es el aviso del apartado 10 del manual.

## El único tema con normas articuladas: el 17

**El tema de seguridad en instalaciones técnicas cita tres normas del Boletín Oficial del Estado**, y
**es el único de la ocupación al que la lente de exactitud se le puede pasar:**

```
refutar_exactitud.py temas/tese/17-seguridad-en-instalaciones-tecnicas.md \
    fuentes/corte-20221221/BOE-A-2002-18099.preceptos.md \
    fuentes/corte-20221221/BOE-A-2016-7303.md
negritas comprobadas: 13 ; no literales: 0
```

**Las citas del anexo I y del anexo IV del Real Decreto 614/2001 quedan fuera de ese recuento**,
porque **la lente trocea por «Artículo N» y un anexo no tiene artículos.** **Se han comprobado a mano,
carácter a carácter, contra el volcado consolidado a la fecha de corte**, y las cinco coinciden.

**Y hay un hallazgo de herramienta que este tema produjo**, del apartado 5 del manual —*el que detecta
se equivoca*—: **la lente descartaba el ancla del reglamento electrotécnico** porque su filtro de
remisiones ajenas —el que evita que «el artículo 4 de la Ley 17/2006» abra un bloque— **también
descartaba «Artículo 2 del Reglamento electrotécnico», que aquí NO es una remisión ajena sino la
norma que el tema está citando.** **Se corrigió el tema, no la lente**: el ancla se reformuló como
«Artículo 2, apartado 1, del Real Decreto 842/2002», y las trece negritas pasaron a comprobarse.

## La cadena de dos normas de la alta tensión

**Es el hallazgo de método de este bloque.** **La pregunta 96 pide a partir de qué valores hay alta
tensión «en materia de riesgos laborales»**, y **la norma de riesgos laborales no da la cifra:**

> «Alta tensión. Baja tensión. Tensiones de seguridad: **las definidas como tales en los reglamentos
> electrotécnicos**.»
> — Real Decreto 614/2001, anexo I, definición 5

**Quien busque el número ahí no lo encontrará.** **La cifra está en el artículo 2.1 del Real Decreto
842/2002**, que fija la baja tensión hasta 1.000 voltios en alterna y 1.500 en continua, **y de ahí
sale por diferencia dónde empieza la alta.** **El temario escribe la cadena entera con las dos citas
y declara que la lectura del límite superior de la baja como inicio de la alta es suya, no de la
norma.**

## La pregunta más limpia del proyecto

**La pregunta 5 —qué efecto NO se relaciona con la radiación de radiofrecuencia— se contesta leyendo
una lista.** **El artículo 2 del Real Decreto 299/2016 enumera los efectos directos e indirectos de
los campos electromagnéticos**, y **tres de las cuatro opciones están literalmente en él**:

| Opción | Dónde está |
|---|---|
| Corrientes de contacto | Artículo 2.c).5 |
| Calentamiento de los tejidos | Artículo 2.b).1 |
| Corrientes inducidas en las extremidades | Artículo 2.b).3 |
| **Ionización de materia corporal** | **En ninguna de las dos letras** |

**Las letras b y c se citan enteras y sin cortes en el tema, incluidos los cuatro efectos indirectos
que la pregunta no usa**, precisamente **para que se vea que la ionización no aparece en ninguno de
los nueve supuestos que la norma enumera.**

## Lo que no se ha podido verificar y por qué

**Treinta respuestas descansan en la plantilla oficial, y todas por el mismo motivo: dependen de una
imagen.** **Es la proporción más alta de todo el proyecto.**

**La regla que este bloque ha seguido, sin excepción**: **no se describe lo que no se ha visto.** **En
lugar de inventar la figura, el tema da la regla de la familia** —cómo se reconoce una
autopolarización por fuente, qué forma tiene cada diagrama polar, cómo se distinguen los cuatro modos
de un monitor de forma de onda, qué lleva cada conector de una base de cámara— **y declara
expresamente que la respuesta concreta viene de la plantilla.**

**En dos casos la regla de la familia deja la pregunta prácticamente resuelta**, y así se dice:

- **La 12 del segundo cuadernillo** —la frecuencia de una senoide— **se calcula entera** salvo por el
  número de divisiones que ocupa un ciclo, y **el tema escribe el método y la tabla de
  correspondencia.**
- **La 19 del segundo cuadernillo** —qué transición hace falta— **se razona hasta el final**: las tres
  opciones que proponen transición terminan todas en «a N hembra» porque no podían terminar en otra
  cosa, **y lo único que la figura decide es qué conector tiene la salida del equipo.**

## Las normas técnicas que este bloque NO ha consultado

**Se declara expresamente, tema por tema, y aquí se reúne:**

| Norma | Dónde haría falta | Qué se ha hecho en su lugar |
|---|---|---|
| **SMPTE 259M, 292M y 424M** | Tema 8 | Los caudales se dan como órdenes de magnitud de cada generación; ninguna pregunta depende de ellos |
| **AES3, AES10 y AES11** | Temas 8 y 9 | Se cita la **presentación pública** de las normas de la Sociedad de Ingeniería de Audio: qué normas existen y qué numeración tienen, **nada de su contenido** |
| **Familia SMPTE ST 2110** | Tema 9 | Se cita el **índice público** con los títulos oficiales de sus partes, verificados literalmente. Eso hace que la respuesta a la pregunta 41 **no descanse en la plantilla** |
| **DMX512** | Tema 11 | Las cifras —512 canales, un byte por canal, un solo sentido, terminación— se dan como uso universal del sector. **Ninguna pregunta depende de ellas** |
| **Familia IEEE 802.11** | Tema 12 | Las bandas se dan como uso universal y coinciden con la respuesta oficial |
| **Estándar T568B** | Tema 12 | El orden de colores se reproduce **de la propia respuesta oficial**, y la explicación de por qué el par azul ocupa los contactos 4 y 5 es oficio |
| **Norma de cableado estructurado** | Tema 12 | Las categorías y sus alcances son órdenes de magnitud; la pregunta caída no depende de ellos |
| **Recomendaciones de la Unión Europea de Radiodifusión sobre líneas de prueba** | Tema 14 | El cuadro de qué mide cada señal es uso universal del oficio |

## Por qué la lente de documento no cierra este bloque

**`refutar_documento` contrasta cada negrita contra un documento suelto no articulado**, y **este
bloque no tiene ese documento**: las normas que lo sostendrían están tras muro de pago o no se han
volcado, y así consta. **Pasarle la lente sin fuente devolvería todas las negritas como «no
literales»**, que es ruido, no verificación.

**Lo que sí se ha hecho en su lugar**, tema por tema:

| Camino de verificación | Dónde se ha usado |
|---|---|
| **Cita literal de norma del BOE** | Temas 1 y 17 |
| **Cita literal de índice o presentación pública de norma técnica** | Temas 8 y 9 |
| **Cálculo escrito y comprobable** | Temas 1, 2, 5, 10, 12, 13 y 14: la ley de Ohm, el código de colores, la conversión de bases, la capacidad RAID, las máscaras de subred, la frecuencia por divisiones y la regla de Carson |
| **Regla de familia declarada, con la respuesta atribuida a la plantilla** | Temas 1, 2, 3, 4, 5, 10, 12, 13, 14 y 17 |
| **Razonamiento que no depende de la figura** | Temas 13 y 14, donde queda escrito por qué |

## Lo que queda dicho

**Diecisiete temas, cero hallazgos de modo y cero de prosa; trece negritas comprobadas contra el
Boletín Oficial del Estado y ninguna no literal.** **Treinta respuestas declaradas dependientes de la
plantilla, todas por depender de una imagen.** **Ninguna respuesta oficial de este bloque es errónea y
ninguna es impugnable.**
