# Refutación del tema 11 del específico de Producción (Asistencia)

**Siglas de este informe**: codificación avanzada de vídeo (**AVC**); iniciativa de cine digital
(**DCI**); **DJI** (marca); difusión de vídeo digital (**DVB**); Instituto Europeo de Normas de
Telecomunicación (**ETSI**); Organización Internacional de Normalización (**ISO**); **SMPTE**
(Sociedad de Ingenieros de Cine y Televisión); Unión Europea de Radiodifusión (**UER**); Unión
Internacional de Telecomunicaciones (**UIT**).

El tema **mejor servido de fuentes** del bloque específico hasta la fecha: **siete de sus diez
preguntas** tienen norma, recomendación o ficha detrás. Y lo es **porque se probaron otra vez las
puertas que estaban dadas por cerradas**.

## Qué lente sirve aquí, y por qué

**Las lentes por artículo no valen para casi nada de este tema.** `refutar_exactitud.py` y
`refutar_modo.py` trocean por «Artículo N» y contrastan cada trozo con su precepto. De las nueve
fuentes de este tema, **sólo tres son articulado** —dos leyes y un real decreto—, y de ellas el
tema toma **tres definiciones y dos preceptos sueltos**, no un desarrollo por artículos. Las otras
seis son **recomendaciones de la UIT, normas europeas, un índice de la SMPTE y una ficha de
fabricante**: documentos sin artículos. Correr las lentes por artículo devolvería casi «0
comprobadas, 0 no literales», que es el resultado engañoso del apartado 10 del manual.

Se ha usado **la lente de documento**, con **las nueve fuentes a la vez**:

```
refutar_documento.py temas/produccion/11-transmision-de-senal.md \
    fuentes/corte-20221221/BOE-A-2022-10757.md \
    fuentes/corte-20221221/BOE-A-2019-9513.md \
    fuentes/corte-20221221/BOE-A-2022-11311.md \
    fuentes/normas-tecnicas/UIT-R_S.673-2.txt \
    fuentes/normas-tecnicas/UIT-R_SNG.770-2.txt \
    fuentes/normas-tecnicas/UIT-R_SNG.770-2_portada-en-ingles.txt \
    fuentes/normas-tecnicas/UIT-T_G.984.1.txt \
    fuentes/normas-tecnicas/SMPTE-ST-2110-indice.md \
    fuentes/normas-tecnicas/ETSI_EN-300-744.txt \
    fuentes/normas-tecnicas/ETSI_EN-302-755.txt \
    fuentes/fabricantes/LiveU_LU300S_ficha.txt
```

**Resultado**: **290 negritas comprobadas**, **174 no literales** y **cero cifras huérfanas**.

## Cero cifras huérfanas, y por qué eso no basta

Es la primera vez que un tema de este bloque sale **sin ninguna cifra sin fuente**. Están
comprobadas las que importan: los **23 h y 56 min** del periodo de rotación sideral, los
**2 000** y **10 000 km** de las órbitas baja y media, los **30 Mbps** de la mochila y los de la
red de alta capacidad, los **14 GHz** de la banda preferida para el periodismo por satélite, las
**720 líneas** de la alta definición, la **EN 302 755** y la **ISO/IEC 13818**.

**Pero hay una cifra que el tema da y que no está comprobada, y la lente no la vio**: los
**36.000 km** de altitud de la órbita geoestacionaria. No la vio porque **el tema no la escribe en
negrita**: la cita entrecomillada, como una de las cuatro opciones del examen, y a continuación
avisa de que **no está en la recomendación leída**. Eso es exactamente lo que había que hacer
—decirlo en vez de disimularlo—, pero conviene dejar apuntado que **la lente sólo mira las
negritas**, de modo que **una cifra en texto corriente pasa por delante de ella sin que suene
nada**. Aquí se detectó a mano, buscando en la S.673-2 las tres altitudes de la escala y viendo
que sólo hay dos.

## Las 174 negritas no literales

Revisadas una a una. Se reparten en cuatro grupos, ninguno problemático:

- **Rótulos y encabezados propios del tema**: «Nivel de la fuente», «Aviso de nivel», «La pregunta
  del examen pide la afirmación falsa».
- **Traducciones al castellano de fuentes que están en inglés.** Es el grupo más numeroso y el que
  más cuidado pidió: el índice de la SMPTE, la ficha de LiveU y las dos normas del ETSI están en
  inglés, así que **casi nada de lo que el tema dice sobre ellas puede ser literal**. Se ha
  comprobado que cada traducción dice lo que dice el original, y las expresiones que el tribunal
  puede preguntar en inglés —*fibre to the home*, *digital satellite news gathering*, *Digital
  Video Broadcasting*, *Ancillary Data*— **se dan también en su idioma**.
- **Enunciados y opciones del examen** citados para explicarlos.
- **Las advertencias del propio tema** sobre lo que no puede sostener.

## Tres comprobaciones que sí cambiaron el tema

**1. La sigla DVB pasó de no tener fuente a tenerla literal.** El primer borrador escribía «**DVB**
—*digital video broadcasting*—» sin más, que es exactamente lo que el apartado 1 del manual
prohíbe: **un dato de memoria**. Al detectarlo se reescribió como una declaración de laguna —«el
tema no desarrolla la sigla porque ninguna fuente leída la desarrolla»—, que era honrado pero
pobre. Sólo entonces se probó otra vez el servidor del ETSI, y resultó que **la sigla está
desarrollada en el título de la propia norma**. La versión final la da con la norma detrás.

**2. El MPEG-2 pasó de «desactualizado» a «literal de la norma».** El borrador trataba la
asociación DVB–MPEG-2 del enunciado como **una imprecisión histórica del examen** que el tema
recogía con reservas. Con la **EN 300 744** delante, resulta que **es literal**: la norma dice que
su objetivo es «establecer el marco para la introducción de la televisión digital basada en
MPEG-2». La advertencia que quedaba en pie no era la que se había escrito: no es que el enunciado
sea impreciso, es que **describe la primera generación**, mientras la televisión digital terrestre
española de hoy codifica la alta definición en **H.264/MPEG-4 AVC**. **La corrección cambió el
sentido del párrafo entero**, no una palabra.

**3. La pregunta de los datos del satélite se degradó a propósito.** El borrador razonaba por qué
la **frecuencia de bajada** es el dato imprescindible. Al leer la **SNG.770-2** apareció que la
recomendación exige documentar «anchura de banda y **polarización** de transmisión»: es decir, que
**uno de los distractores es un dato real y necesario**. El tema dejó de justificar la respuesta y
pasó a decir la verdad: **es la respuesta porque el tribunal la corrige así**, y las cuatro
opciones sólo se diferencian en el sexto dato. Es una pérdida aparente —el tema explica menos— y
una ganancia real: **el opositor sabe que ahí hay que memorizar, no razonar**.

## El hallazgo de método: van tres puertas abiertas que se habían dado por cerradas

El tema 9 ya dejó escrita la regla —**dos rutas y un agente de usuario de navegador antes de
escribir «no se ha podido consultar»**— después de descubrir que las fichas de **LiveU** y de
**Astera** estaban disponibles. Este tema añade **la tercera**: `etsi.org` había devuelto
«prohibido» a la descarga directa de sus normas, y **con un agente de navegador la descarga
funciona a la primera**. Era el mismo filtro.

Tres de tres. **El patrón ya no es casualidad**, y la conclusión que hay que sacar es incómoda:
durante buena parte de este proyecto, **la frase «no se ha podido consultar» ha significado en
realidad «no se ha sabido pedir»**. Las fuentes que siguen declaradas inalcanzables —**UER**,
**DCI** y el texto de la **AES10**— se han vuelto a probar con la regla puesta, y esas tres sí se
sostienen; pero quedan sin probar las fichas de **Sony** y **DJI**, que hacen falta para el tema
de exteriores, y se probarán antes de escribirlo.

## Lo que este tema no puede sostener

- **La altitud de 36.000 km** de la órbita geoestacionaria. La S.673-2 da la baja y la media, no
  ésta. El tema lo dice y señala que es **el único de los cuatro datos de esa pregunta sin
  respaldo**.
- **Cuál de los seis datos de acceso al satélite es el imprescindible.** Decisión del tribunal, no
  hecho comprobable.
- **El streaming y la señal Pool.** Uso profesional; van marcados.
- **El contenido de las normas europeas más allá de su portada y su introducción.** No se han
  leído las casi doscientas páginas de cada una, y el tema no afirma nada de ellas.
- **La cifra de la mochila**, que depende de una ficha de fabricante y caduca con el modelo.
