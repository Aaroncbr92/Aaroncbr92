# Refutación del tema 10 del específico de Producción (Asistencia)

**Siglas de este informe**: **BS** (serie de recomendaciones de radiodifusión sonora de la UIT);
la baja tensión (**BT**); documentos básicos (**DB**); alto rango dinámico (**HDR**); el logaritmo
híbrido (**HLG**); protección frente al ruido (**HR**); interfaz digital de audio multicanal
(**MADI**); modulación por impulsos codificados (**MIC**); cuantización perceptiva (**PQ**); real
decreto (**RD**); Unión Internacional de Telecomunicaciones (**UIT**); conector de audio
profesional de tres polos (**XLR**).

Primer tema del bloque específico **sin norma jurídica detrás**, y por eso el primero en el que
las lentes trabajan de otra manera.

## Qué lente sirve aquí, y por qué

**Las lentes por artículo no sirven.** `refutar_exactitud.py` y `refutar_modo.py` trocean el tema
por «Artículo N» y contrastan cada trozo con su precepto. Este tema **no cita artículos**: cita
**cuadros de recomendaciones** —«cuadro 3 de la BT.601-7», «cuadro 1 de la BT.2100-1»— y
**definiciones de un glosario**. Correrlas devolvería «**0 comprobadas, 0 no literales**», que es
justamente el resultado que el apartado 10 del manual manda desconfiar.

Se ha usado, por tanto, **la lente de documento**, que contrasta **cada negrita y cada cifra en
negrita contra el texto completo de todas las fuentes a la vez**. Es la misma decisión que se tomó
con el tema de Igualdad y con el de prevención, y por la misma razón.

**Resultado**: **306 negritas comprobadas**, **244 no literales** —revisadas y todas paráfrasis o
rótulos propios— y **4 cifras huérfanas**.

## Las cuatro cifras huérfanas, una a una

| Cifra | Dónde | Qué es |
|---|---|---|
| **2032** (×3) | «Real Decreto 2032/2009» | **El número de la propia norma.** El volcado consolidado del BOE no repite el título de la disposición en su cuerpo, así que su número no aparece dentro del texto. Verificado contra el identificador `BOE-A-2010-927` |
| **67** | «AES67 (*networked audio*)» | Está **dentro de una cita literal de la página de la AES**, que no se pasó a la lente como fuente en esa corrida. Guardada después en `fuentes/normas-tecnicas/AES-normas-de-audio.md` |

**Ninguna cifra del cuerpo normativo quedó sin fuente.**

## Un hallazgo que sí cambió el tema

**Se quitaron dos cifras que no tenían fuente.** El primer borrador decía, al explicar el teorema
de muestreo: «si el oído humano llega a unos 20 kHz, muestrear a **44,1 kHz** o a **48 kHz**
cumple la regla con margen». La lente marcó **48** como cifra huérfana, y al buscarla resultó que
**no está en ninguna de las cuatro fuentes leídas**: son frecuencias de uso corriente, pero este
tema no había leído la norma que las fija —la AES5 o la BS de la UIT—, y **ninguna de las
diecisiete preguntas las pide**.

Se sustituyeron por el único ejemplo que el tema **sí** puede sostener: las frecuencias de la
propia **BT.601-7**, **13,5 MHz** y **6,75 MHz**, que están leídas. Y el tema **dice que no da la
cifra de audio y por qué**.

Es el apartado 1 del manual aplicado tal cual: *lo que no se puede confirmar se quita*. La cifra
era correcta y habría pasado desapercibida; el problema no es que fuera falsa, es que **no estaba
comprobada**, y en un tema donde diez de diecisiete respuestas ya se apoyan en la plantilla, la
diferencia entre lo comprobado y lo plausible es lo único que sostiene el resto.

## Un error de la fuente, no del tema

La **extracción automática de texto** del fichero PDF de la BT.601-7 devolvía, en el cuadro 3,
«**16,75 MHz**» como frecuencia de muestreo de cada señal de diferencia de color. **Es falso.**

Saltó porque **no cuadraba con el resto de la tabla**: si la luminancia se muestrea a 13,5 MHz y
por cada cuatro muestras de luminancia hay dos de cada diferencia de color —y la propia tabla lo
confirma con **720 frente a 360** muestras de línea activa—, la frecuencia tenía que ser
**exactamente la mitad**, 6,75 MHz.

**No se dio por bueno el razonamiento**: se **recortó esa celda del PDF, se amplió seis veces y
se leyó a ojo**. Dice **6,75 MHz**. El «1» venía pegado de la fila de arriba, donde figura «16
periodos del reloj de luminancia».

Queda anotado porque enseña algo sobre el segundo nivel de la jerarquía de fuentes: **con una
norma técnica en PDF, el texto extraído no es la fuente; la página lo es**. Y porque el método
para detectarlo es el de siempre: **la cifra que no cuadra con las otras cifras del mismo cuadro**.

## Lente de prosa

**Cero hallazgos**, tras dos rondas de correcciones. La primera dejó **catorce siglas sin
presentar** —UIT, BT, AES, DB, HR, HDR, HLG, PQ, MADI, MIC, RD, TV, XLR y PDF—, casi todas porque
aparecían por primera vez **dentro de la tabla de niveles de fuente** que abre el tema.

Se resolvió **presentando los tres organismos y las dos convenciones de cita en un párrafo previo
a esa tabla**, y volteando las glosas que iban detrás de la sigla para que fueran delante
—«**cuantización perceptiva** (*perceptual quantization*), **PQ**», no al revés—. La lente exige
que el paréntesis explicativo esté **antes**, y tiene razón: así es como se lee.

Ni tejido conectivo, ni frases repetidas entre epígrafes.

## Lo que este tema declara que no puede sostener

No es un hallazgo de las lentes: es una decisión escrita en el propio tema, y se repite aquí para
que quede en el informe.

- **Diez de las diecisiete respuestas se apoyan en la plantilla oficial y en el uso profesional**,
  no en norma leída: patrones polares, tipos de micrófono por transductor, vectorscopio, N-1,
  trémolo y el eco. El tema **lo marca en cada caso**.
- **La AES10 no se ha leído** —muro de pago, y el buscador de la AES devolvió 404 el mismo día—.
  El tema afirma **qué es** el MADI, que es lo que publica la propia asociación, y **nada de su
  contenido interno**.
- **El DB-HR regula edificios, no platós.** De él se toma **la definición del tiempo de
  reverberación**, no una exigencia aplicable a un estudio de televisión, y el tema lo dice.

## Segunda pasada

La lente de documento y la de prosa se volvieron a correr después de las correcciones. Prosa,
**limpia**. Documento, **las mismas cuatro cifras**, las cuatro identificadas y ninguna del cuerpo
normativo.
