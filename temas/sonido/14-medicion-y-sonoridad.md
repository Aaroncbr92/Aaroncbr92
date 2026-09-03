# Tema 14 del específico de Sonido · Medición y sonoridad

Las siglas y unidades de este tema, presentadas de entrada: la Unión Europea de Radiodifusión
(**EBU**, *European Broadcasting Union*, la **UER** en español) y su recomendación **R 128**; la
unidad de sonoridad a escala completa (**LUFS**, *loudness unit full scale*) y la unidad de sonoridad
relativa (**LU**); las tres escalas temporales del medidor —momentánea (**M**), a corto plazo (**S**,
*short-term*) e integrada (**I**)—; el pico real (*true peak*) y su unidad (**dBTP**); la puerta de
medida (*gating*); el decibelio a escala completa (**dBFS**), que el tema 7 ya presentó; y el
vúmetro y el picómetro, que son los medidores que la sonoridad vino a sustituir.

> Enunciado de la convocatoria (Anexo 2, temario específico de Sonido, punto 12):
> «MEDICIÓN Y SONORIDAD. Norma AES R‐128, Lufs, niveles estándar en Broadcast Dbfs. Control de
> dinámica.»

**Seis preguntas.** **Y el punto que más ha cambiado el oficio en los últimos quince años**: **antes
de la R 128, el nivel de una emisión se medía por PICOS; desde ella, se mide por SONORIDAD.** **Ese
cambio es la razón de que la publicidad ya no suene más fuerte que el programa.**

**Un apunte sobre el propio enunciado**: **el anexo la llama «norma AES R-128».** **La R 128 no es de
la AES: es una recomendación de la Unión Europea de Radiodifusión.** **El temario desarrolla la
recomendación que el enunciado quiere decir y señala la atribución equivocada.**

<!-- indice -->

## Índice

- [1. Por qué la sonoridad y no el pico](#1-por-qué-la-sonoridad-y-no-el-pico)
- [2. Qué establece la R 128](#2-qué-establece-la-r-128)
- [3. Qué significa LUFS](#3-qué-significa-lufs)
- [4. Las tres escalas temporales](#4-las-tres-escalas-temporales)
- [5. Los medidores clásicos y qué miden](#5-los-medidores-clásicos-y-qué-miden)
- [6. El control de dinámica](#6-el-control-de-dinámica)
- [7. Los datos que el examen ha preguntado](#7-los-datos-que-el-examen-ha-preguntado)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. Por qué la sonoridad y no el pico

**El problema que la R 128 vino a resolver es viejo y todo el mundo lo ha sufrido**: **dos programas
que no se pasan del máximo pueden sonar muy distinto de fuerte.**

**La razón es que un medidor de picos mide el instante más alto y el oído no oye instantes: oye
promedios ponderados.** **Una emisión muy comprimida tiene el mismo pico que una sin comprimir y suena
mucho más fuerte**, porque **todo su contenido está pegado al techo.**

| Se mide | Qué contesta | Con qué se mide |
|---|---|---|
| **Pico** | **¿Me paso del máximo técnico?** | **Picómetro, dBFS, dBTP** |
| **Sonoridad** | **¿Cómo de fuerte lo va a percibir el oyente?** | **Medidor de sonoridad, LUFS** |

**Y las dos preguntas hay que contestarlas a la vez**: **una emisión tiene que cumplir un objetivo de
SONORIDAD y no pasar de un techo de PICO.** **Ésa es exactamente la estructura de la R 128.**

## 2. Qué establece la R 128

**La recomendación EBU R 128 establece la normalización del nivel de sonoridad en las emisiones de
audio.** Ésa es la respuesta oficial a la pregunta 26.

**Sus tres cifras, que son las que hay que saber:**

| Parámetro | Valor |
|---|---|
| **Sonoridad de programa objetivo** | **−23 LUFS** |
| **Máximo de pico real** | **−1 dBTP** |
| **Tolerancia en directo** | **±1 LU** |

**Las tres opciones falsas de la pregunta 26 llevan la recomendación a otro terreno** —compresión de
vídeo, resolución de alta definición, normas de transmisión en directo—, y **la palabra que decide es
«sonoridad».**

**La pregunta 69**: **el máximo valor de pico real aceptado por la R 128 es −1 dBTP.** Ésa es la
respuesta oficial.

**Por qué no cero, que es lo que parecería lógico**: **porque el pico real no es el pico de las
muestras.** **Entre dos muestras la onda reconstruida puede pasar por encima de las dos**, así que
**una señal que en muestras marca 0 dBFS puede tener un pico real superior.** **Ese exceso lo descubre
el codificador de emisión y lo convierte en distorsión.** **El decibelio de margen es lo que lo
evita.**

**La pregunta 95**: **la tolerancia de desviación que la EBU permite en la medición de LUFS para
programas en directo es de ±1 dB.** Ésa es la respuesta oficial.

**Y la razón de que exista esa tolerancia sólo para el directo**: **un programa grabado se puede
medir entero y ajustar.** **Un directo no**: **su sonoridad integrada no se conoce hasta que
termina.** **La recomendación admite ese margen porque exigir exactitud sería exigir lo imposible.**

## 3. Qué significa LUFS

**El acrónimo LUFS significa Loudness Unit Full Scale.** Ésa es la respuesta oficial a la pregunta 37.

**Y las dos unidades que hay que separar, porque se confunden todo el rato:**

| Unidad | Qué es | Cuándo se usa |
|---|---|---|
| **LUFS** | **Una medida ABSOLUTA**, referida a la escala completa | **«Este programa está a −23 LUFS»** |
| **LU** | **Una medida RELATIVA**: una diferencia | **«Le faltan 2 LU»**, o **«la tolerancia es ±1 LU»** |

**Un LU y un decibelio valen lo mismo**: **son la misma escala logarítmica.** **La diferencia no es de
tamaño, es de si el número apunta a un absoluto o a una diferencia.** **Es exactamente la relación que
hay entre los dBFS y los dB del tema 2.**

**Y lo que hace de la sonoridad una medida distinta del nivel es que va PONDERADA**: **el medidor
aplica una curva —la llamada K— que se parece a cómo oye el oído**, realzando medios y agudos y
quitando peso a los graves más profundos. **Por eso un bombo enorme sube menos los LUFS de lo que
sube el picómetro.**

## 4. Las tres escalas temporales

**Las escalas temporales de un medidor de sonoridad en modo EBU son M, S e I.** Ésa es la respuesta
oficial a la pregunta 39.

| Escala | Ventana | Para qué sirve |
|---|---|---|
| **M** —momentánea— | **400 milisegundos** | **Ver lo que pasa AHORA**: es la que se mueve con la música |
| **S** —a corto plazo— | **3 segundos** | **Ver la tendencia**: la que se usa para mezclar |
| **I** —integrada— | **El programa entero** | **La cifra que tiene que dar −23 LUFS**: es la que se entrega |

**Las tres opciones falsas son invenciones verosímiles** —«Small y Large», «Peak, Shell y Flat»,
«Node, Cut»—, y **la pregunta se contesta reconociendo la terna real.**

**La pregunta 24, que es la más fina del punto**: **en un medidor de sonoridad con modo EBU, la escala
short-term NO está puerteada.** Ésa es la respuesta oficial.

**Qué es la puerta y por qué existe**: **la sonoridad integrada de un programa no debe contar los
silencios.** **Si contara, una película con muchos pasajes callados daría una cifra bajísima y habría
que subirla entera hasta que los diálogos gritaran.** **La puerta descarta lo que está por debajo de
un umbral, y así la cifra integrada refleja el material que de verdad suena.**

**Y la clave de la pregunta es a QUÉ escala se le aplica:**

| Escala | ¿Puerteada? | Por qué |
|---|---|---|
| **M** —momentánea— | **No** | **Es un instrumento de lectura instantánea**: tiene que enseñar lo que hay |
| **S** —corto plazo— ✔ | **No** | **Lo mismo**: es lectura, no promedio de programa |
| **I** —integrada— | **SÍ**, con dos umbrales | **Es la cifra del programa**: sin puerta, los silencios la falsearían |

**Las tres opciones falsas ofrecen niveles de puerta** —−18, −10 y −70 LU—, y **una de ellas es
tentadora porque es real**: **el umbral absoluto de la puerta de la escala integrada anda por ahí.**
**Pero la pregunta no pregunta por la integrada: pregunta por la short-term, y ésa no tiene puerta.**

## 5. Los medidores clásicos y qué miden

**El enunciado del punto habla de «niveles estándar en Broadcast dBFS», y eso obliga a poner los
medidores en orden.**

| Medidor | Qué mide | Cómo responde |
|---|---|---|
| **Vúmetro** | **Un promedio**: se aproxima a la sensación de volumen | **Lento**: 300 milisegundos de integración |
| **Picómetro (PPM)** | **Los picos** | **Rápido**, pero **no llega al pico real** |
| **Medidor de pico de muestra** | **El valor de la muestra más alta**, en dBFS | **Instantáneo y exacto en muestras** |
| **Medidor de pico real** | **El pico de la onda RECONSTRUIDA**, en dBTP | **Sobremuestrea para verlo** |
| **Medidor de sonoridad** | **La sonoridad ponderada**, en LUFS | **Tres ventanas**: M, S, I |

**Y el error de concepto más caro, que este cuadro deshace**: **el vúmetro no protege contra el
recorte** —es demasiado lento— **y el picómetro no dice cómo de fuerte suena.** **Hacen falta los
dos, y por eso la R 128 fija un objetivo de sonoridad Y un techo de pico.**

## 6. El control de dinámica

**El enunciado lo pide expresamente y el examen no lo pregunta en este punto**, porque **sus preguntas
de compresor están en el punto 5, que es el tema 7.**

**Lo que aquí hay que añadir es cómo se relaciona la compresión con la sonoridad**, que **es lo que un
técnico de emisión maneja:**

1. **Comprimir SUBE la sonoridad sin subir el pico.** **Ésa es la razón de que la publicidad se
   comprimiera hasta el absurdo antes de la R 128.**
2. **Con la R 128, comprimir ya no da ventaja de volumen**: **si la sonoridad integrada tiene que ser
   −23 LUFS, comprimir más sólo obliga a bajar más el conjunto.** **Lo que se gana en densidad se
   pierde en nivel.**
3. **Lo que sí se sigue ganando es CONSISTENCIA**: **una emisión comprimida se oye mejor en un coche.**
   **La compresión pasa de ser un arma de volumen a una decisión de inteligibilidad**, que es lo que
   siempre debió ser.

## 7. Los datos que el examen ha preguntado

| Nº | Lo que pregunta | Respuesta oficial |
|---|---|---|
| 24 | A qué nivel está puerteada la escala short-term | d) No está puerteada ✔ |
| 26 | Qué establece la recomendación EBU R 128 | d) La normalización del nivel de sonoridad ✔ |
| 37 | Qué significa el acrónimo LUFS | b) Loudness Unit Full Scale ✔ |
| 39 | Escalas temporales de un medidor en modo EBU | c) M, S, I ✔ |
| 69 | Máximo valor de pico real de la R 128 | c) −1 dBTP ✔ |
| 95 | Tolerancia de LUFS que la EBU permite en directo | b) ±1 dB ✔ |

**Las seis respuestas oficiales son correctas.**

**Y el aviso de estudio, que es el mejor de la ocupación**: **este punto son TRES CIFRAS y una terna.**
**−23 LUFS, −1 dBTP, ±1 LU, y las escalas M, S e I.** **Con eso se contestan las seis.** **Ningún
otro punto del temario da seis preguntas por cuatro datos.**

## 8. Trazabilidad

**Este tema no cita ninguna norma.** Su materia es la medición de sonoridad, y **va como oficio y con
recomendación de referencia declarada.**

| Nivel | Fuente | Preguntas |
|---|---|---|
| **Segundo: organismo de radiodifusión** | **Recomendación EBU R 128**: **su existencia y su objeto.** **El texto de la recomendación NO se ha consultado** | Preguntas 24, 26, 39, 69 y 95 |

**Cuatro declaraciones expresas:**

1. **El texto de la recomendación EBU R 128 no se ha volcado en este proyecto.** **Las cifras que este
   tema da —−23 LUFS, −1 dBTP, ±1 LU y las ventanas de 400 milisegundos y 3 segundos— son las de uso
   universal en la industria y coinciden con las respuestas oficiales**, y **el temario las declara
   como tales en lugar de atribuirlas a un apartado de un documento que no ha leído.** **Es la misma
   situación que este proyecto ya declaró con la AES10 en el temario de Producción (Asistencia).**
2. **El enunciado del Anexo 2 llama «norma AES R-128» a una recomendación de la Unión Europea de
   Radiodifusión.** **La atribución es equivocada**, y **el temario lo señala.** **No cambia ninguna
   respuesta**: **el examen pregunta por el contenido de la recomendación, no por quién la publica.**
3. **La curva de ponderación K y el mecanismo de la puerta se describen aquí de forma conceptual**, y
   **sus coeficientes exactos están en la recomendación no consultada.** **Lo que la pregunta 24 mide
   es a qué escala se aplica la puerta, no su valor**, y **eso el tema lo sostiene.**
4. **La tabla de medidores del epígrafe 5 es una clasificación asentada del sector**, no normalizada, y
   **el tema la presenta como conocimiento común de la materia.**

**El resto del tema va como oficio y así se declara**: la distinción entre medir pico y medir
sonoridad, la diferencia entre LUFS y LU, la razón de que el pico real exija un margen bajo cero, la
función de la puerta y la relación entre compresión y sonoridad después de la R 128. **Nada de eso
está en un boletín oficial ni en una norma técnica de las consultadas**, y el tema no lo presenta como
si lo estuviera.
