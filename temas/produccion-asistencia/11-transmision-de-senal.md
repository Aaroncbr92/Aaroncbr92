# Tema 11 del específico de Producción (Asistencia) · Medios de transmisión de señal, envío de imágenes y comunicaciones

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Producción (Asistencia) · punto 11 |
| **Sirve para** | **Producción (Asistencia)** |
| **Fuente** | **Sin norma en el enunciado.** Se apoya en la **Ley 11/2022** General de Telecomunicaciones, en el **Plan Técnico Nacional de la TDT**, en la **Ley 13/2022**, en tres recomendaciones de la **UIT** —**S.673-2**, **SNG.770-2** y **G.984.1**—, en dos **normas europeas del DVB**, en el índice oficial de la **SMPTE ST 2110** y en la **ficha de LiveU** |
| **Identificador** | `BOE-A-2022-10757` · `BOE-A-2019-9513` · `BOE-A-2022-11311` · `UIT-R S.673-2` · `UIT-R SNG.770-2` · `UIT-T G.984.1` · `ETSI EN 300 744` · `ETSI EN 302 755` |
| **Redacción que se estudia** | Las **leyes y el real decreto en su texto vigente al 21/12/2022**, las recomendaciones en sus **ediciones 03/2002, 01/2012 y 03/2003**, y la ficha **tal como estaba el 02/09/2026** |
| **Aviso sobre las fuentes** | De sus **10 preguntas**, **siete tienen norma, recomendación o ficha detrás**. Las **tres restantes** —streaming, señal Pool y los datos de acceso al satélite— se apoyan **sólo en la plantilla oficial**, y van marcadas |
| **Extensión** | **4.529 palabras** |

<!-- /portada -->

> **Enunciado de la convocatoria (Anexo 2, temario específico de Producción, punto 11):**
> «MEDIOS DE TRANSMISIÓN DE SEÑAL, ENVIO DE IMÁGENES Y COMUNICACIONES.»

**Diez preguntas**, la tercera materia más preguntada del bloque específico. Y, a diferencia del
tema de escenografía, **este sí tiene fuentes**: siete de las diez se apoyan en una norma, en una
recomendación de la Unión Internacional de Telecomunicaciones o en la ficha del fabricante que el
propio enunciado nombra. El tema marca el nivel de cada afirmación:

| Nivel | Qué sostiene en este tema |
|---|---|
| **1 · Norma del BOE** | La **Ley 11/2022**, General de Telecomunicaciones, para lo que en España se llama **banda ancha** y **red de muy alta capacidad**; el **Plan Técnico Nacional de la Televisión Digital Terrestre** (Real Decreto 391/2019), para saber **qué normas europeas usa la televisión digital española**; y la **Ley 13/2022**, General de Comunicación Audiovisual, para el servicio **a petición** |
| **2 · Organismo de normalización** | Tres recomendaciones de la Unión Internacional de Telecomunicaciones (**UIT**): la **UIT-R S.673-2**, que define **satélite geoestacionario** y el **periodo de rotación de la Tierra**; la **UIT-R SNG.770-2**, que define el periodismo electrónico digital por satélite (*digital satellite news gathering*), **DSNG**, y lo escribe entero; y la **UIT-T G.984.1**, que desarrolla la fibra hasta la vivienda (*fibre to the home*), **FTTH**, y toda su familia. Y el índice oficial de la familia de la Sociedad de Ingenieros de Cine y Televisión (*Society of Motion Picture and Television Engineers*), **SMPTE ST 2110** |
| **4 · Documentación de fabricante** | La ficha de **LiveU** del modelo **LU300S**, que el examen cita por su nombre |
| **5 · La plantilla oficial** | El **streaming**, la **señal Pool** y **qué dato es imprescindible** para acceder a una señal por satélite. Va marcado |

**Tres de las diez** —streaming, señal Pool y los datos de acceso al satélite— **no tienen más
autoridad que la plantilla**. Van dichas como tales.

---

<!-- indice -->

## Índice

- [1. Ancho de banda: qué es y qué limita](#1-ancho-de-banda-qué-es-y-qué-limita)
- [2. El cable y la fibra: FTTH y su familia](#2-el-cable-y-la-fibra-ftth-y-su-familia)
- [3. El satélite](#3-el-satélite)
  - [3.1 La órbita geoestacionaria](#31-la-órbita-geoestacionaria)
  - [3.2 Los datos para acceder a una señal por satélite](#32-los-datos-para-acceder-a-una-señal-por-satélite)
  - [3.3 DSNG](#33-dsng)
- [4. La mochila: transmisión celular agregada](#4-la-mochila-transmisión-celular-agregada)
- [5. La transmisión dentro de la casa: la familia SMPTE ST 2110](#5-la-transmisión-dentro-de-la-casa-la-familia-smpte-st-2110)
- [6. La difusión: la especificación europea (DVB) y la televisión digital terrestre](#6-la-difusión-la-especificación-europea-dvb-y-la-televisión-digital-terrestre)
- [7. Streaming y señal Pool](#7-streaming-y-señal-pool)
  - [7.1 Streaming](#71-streaming)
  - [7.2 La señal Pool](#72-la-señal-pool)
- [8. Los datos que el examen ha preguntado](#8-los-datos-que-el-examen-ha-preguntado)
- [9. Trazabilidad](#9-trazabilidad)

<!-- /indice -->

## 1. Ancho de banda: qué es y qué limita

**Ancho de banda** es, en su sentido físico, **el margen de frecuencias que un canal deja pasar**.
Y de ahí sale la consecuencia por la que el examen pregunta: **cuanta más anchura tiene el canal,
más información cabe por segundo**. Por eso, en la práctica del oficio, «ancho de banda» y
«velocidad» se usan casi como sinónimos, y **la respuesta del examen es que el ancho de banda
limita la velocidad de procesado y transmisión**.

Las tres opciones falsas confunden el ancho de banda con otras tres cosas:

- Que **limita la velocidad de grabación** —eso lo limita el soporte y el códec, no el canal—.
- Que **regula los megahercios de la subida de señal** —invierte la relación: la anchura *se mide*
  en hercios, no los regula—.
- Que **regula la colorimetría** —eso no tiene nada que ver: la colorimetría la fijan los primarios
  y la matriz de la señal—.

**Dónde lo confirma la ley española.** La **Ley 11/2022, de 28 de junio, General de
Telecomunicaciones**, define en su anexo de definiciones la **red de comunicaciones electrónicas
de alta capacidad** como la «**capaz de prestar servicios de acceso de banda ancha a velocidades
de al menos 30 Mbps**». Es decir: **el legislador define la banda ancha por la velocidad que
alcanza**, que es exactamente lo que dice la respuesta del examen leída al revés.

---

## 2. El cable y la fibra: FTTH y su familia

**FTTH responde a *fibre to the home*, fibra hasta la vivienda.** No es una sigla de oficio sin
respaldo: la **Recomendación UIT-T G.984.1 (03/2003)**, «Redes ópticas pasivas con capacidad de
Gigabits: Características generales», la desarrolla en su lista de abreviaturas y la usa en el
cuerpo. Y con ella desarrolla **toda la familia**: la fibra hasta el edificio (*fibre to the building*),
**FTTB**; hasta la acometida (*fibre to the curb*), **FTTC**; y hasta el armario de calle
(*fibre to the cabinet*), **FTTCab**. Es lo que conviene llevar aprendido, porque son los
distractores naturales de esta pregunta:

| Sigla | Desarrollo | Hasta dónde llega la fibra |
|---|---|---|
| **FTTH** | *fibre to the home* | **Hasta la vivienda** |
| **FTTB** | *fibre to the building* | Hasta **el edificio** |
| **FTTC** | *fibre to the curb* | Hasta **la acometida** |
| **FTTCab** | *fibre to the cabinet* | Hasta **el armario** de calle |

La recomendación las ordena de más a menos fibra: las arquitecturas disponibles «van de la fibra
hasta la vivienda, pasando por la fibra hasta el edificio o la acometida, hasta la fibra hasta el
armario». **Cuanto más lejos llega la fibra, menos cobre queda al final**, y ahí está la diferencia
de capacidad entre unas y otras.

Los tres distractores del examen —*Fibrescope To The Hondle*, *File To Transfer Home*, *Fiber To
The High*— **no son siglas de nada**: están construidas cambiando una palabra de la buena. La
manera de no caer es saber que la **H** final es de *home*, y que la familia entera se nombra por
**dónde termina la fibra**.

**Cómo lo dice la ley española.** La misma Ley 11/2022 llama **red de comunicaciones electrónicas
de muy alta capacidad** a la que «**se compone totalmente de elementos de fibra óptica, al menos
hasta el punto de distribución de la localización donde se presta el servicio**». Es la misma idea
—medir la red por hasta dónde llega la fibra— dicha en lenguaje jurídico.

---

## 3. El satélite

### 3.1 La órbita geoestacionaria

Aquí hay fuente exacta, y es la que hace falta: la **Recomendación UIT-R S.673-2 (03/2002)**,
«Términos y definiciones relativos a radiocomunicaciones espaciales». Las definiciones van
encadenadas, y hay que leerlas en orden:

| Término | Definición de la recomendación |
|---|---|
| **Satélite sincrónico** | Satélite cuyo **periodo de revolución sideral medio es igual al periodo de rotación sideral del cuerpo primario** sobre su eje |
| **Satélite geosincrónico** | Satélite sincrónico **de la Tierra**. Y una nota: «**el periodo de rotación sideral de la Tierra es de aproximadamente 23 h y 56 min**» |
| **Satélite estacionario** | Satélite que **permanece fijo con relación a la superficie** del cuerpo primario. Y otra nota: es un satélite sincrónico **de órbita circular, ecuatorial y directa** |
| **Satélite geoestacionario** | Satélite **estacionario cuyo cuerpo primario es la Tierra** |

**La pregunta del examen pide la afirmación falsa**, y con esa cadena delante se contesta sin
dudar:

- «**El período de su órbita es de 48 horas**» → **falsa, y es la respuesta**. Un satélite
  geoestacionario es sincrónico, y ser sincrónico significa **dar una vuelta en lo que la Tierra
  tarda en girar sobre sí misma**: **unas 23 h y 56 min**, no 48.
- «Su posición está estacionada en la misma posición respecto a la Tierra» → **verdadera**: es
  literalmente la definición de *satélite estacionario*.
- «Su órbita se sitúa sobre el ecuador» → **verdadera**: la nota de la recomendación dice que la
  órbita es **ecuatorial**.
- «Su órbita se encuentra a unos 36.000 km de la Tierra» → **se da por verdadera**, y es el dato de
  uso corriente. **Aviso de nivel**: esa altitud **no está en la recomendación leída**, que sí da
  las otras dos de la escala —**órbita baja**, por debajo de unos **2 000 km**, y **órbita media**,
  a unos **10 000 km**—. Para acertar la pregunta no hace falta, porque la falsa es el periodo;
  pero conviene saber cuál de los cuatro datos es el que **no** tiene fuente aquí.

**Lo que sale gratis de la misma recomendación**, y es material de examen evidente: la **órbita
baja (LEO)**, por debajo de unos **2 000 km**; la **órbita media (MEO)**, a unos **10 000 km**; el
**apogeo** y el **perigeo** como puntos de máxima y mínima distancia al centro de la Tierra; y la
**órbita directa** frente a la **retrógrada**, según gire en el mismo sentido que el cuerpo
primario o en el contrario.

### 3.2 Los datos para acceder a una señal por satélite

**La respuesta oficial** a qué datos son imprescindibles para acceder desde el control central a
una señal que un organizador distribuye por satélite: **horario, satélite, posición orbital,
transponder, frecuencia de bajada y symbol rate**.

**Lo que hay que ver en el enunciado.** Las cuatro opciones repiten **cinco datos idénticos**
—horario, satélite, posición orbital, transponder y *symbol rate*— y **sólo se diferencian en el
sexto**: banda, polarización, **frecuencia de bajada** o codificación. Es decir, la pregunta no
mide si se sabe cómo se recibe una señal por satélite: mide **cuál de los cuatro candidatos eligió
el tribunal**. Y eligió la **frecuencia de bajada**.

**Nivel de la fuente: plantilla oficial, y con una salvedad que conviene decir.** Los tres
descartados **no son absurdos**. La propia **Recomendación UIT-R SNG.770-2** exige que el informe
técnico de una estación de periodismo por satélite documente, entre otras características,
«**anchura de banda y polarización de transmisión**»: la polarización es un dato real y necesario.
Lo que el tema puede afirmar honradamente es que **la respuesta correcta es la frecuencia de
bajada porque así lo corrige el tribunal**, no porque las otras tres sean prescindibles en un
control central de verdad.

### 3.3 DSNG

**DSNG responde a *digital satellite news gathering*.** Y no es una sigla de oficio: es el título
de una recomendación de la UIT. La **Recomendación UIT-R SNG.770-2 (01/2012)** se titula, en
español, «**Procedimientos operacionales uniformes para el periodismo electrónico digital por
satélite (DSNG)**», y en su edición inglesa, «*Uniform operational procedures for digital
satellite news gathering (DSNG)*». Ahí está la sigla desarrollada, palabra por palabra.

Las tres opciones falsas del examen cambian una palabra cada una —*Direct* por *Digital*, *Now*
por *News*—, así que **la manera de no fallar es tener las cuatro palabras**: **digital**,
**satellite**, **news**, **gathering**.

**Y ya que la recomendación está leída, lo que dice de verdad**, porque es el corazón de este tema:

> **Definición del DSNG** (apartado 1.1): «Transmisión **temporal y ocasional** de televisión o
> sonido radiofónico **con escaso tiempo de aviso** con fines de difusión, utilizando **estaciones
> terrenas de enlace ascendente portátiles o fácilmente transportables** que operan en el marco del
> **servicio fijo por satélite**».

De esa definición salen tres rasgos que explican cómo se trabaja con una unidad de satélite:

- **Es temporal y con poco aviso.** La recomendación lo repite: la necesidad de recurrir al DSNG
  «suele identificarse sólo días, o incluso horas, antes» de la transmisión. De ahí que todo el
  documento gire alrededor de **autorizaciones rápidas** y **puntos de contacto permanentes** en
  cada administración.
- **El equipo lo maneja poca gente y rápido.** La recomendación fija el listón: debe poder
  **ajustarse y manejarse por un equipo de no más de dos personas** en un tiempo razonablemente
  corto, «por ejemplo, 1 h».
- **La banda preferida es la de 14 GHz.** Como el terminal ha de llevar una antena pequeña para
  ser transportable, la recomendación dice que **se prefiere la banda de 14 GHz**, y explica por
  qué: en la de **6 GHz** la coordinación de frecuencias «resulta más difícil», porque esas bandas
  se comparten con muchos enlaces terrenales fijos.

**Y una pieza para el «y comunicaciones» del enunciado.** La misma recomendación enumera los
servicios de comunicación adicionales que un equipo de satélite puede necesitar: **microondas
punto a punto**, **sistemas de comunicaciones telefónicas**, **micrófonos inalámbricos símplex o
dúplex bidireccionales** y **terminales móviles de satélite para voz y datos**. Es la lista de lo
que hay que prever además de la señal.

---

## 4. La mochila: transmisión celular agregada

El examen cita **por su nombre y su modelo** una mochila de transmisión: la **LU300S** de
**LiveU**. Y pregunta **hasta cuántos megabits por segundo admite**. La respuesta oficial es
**30 Mbps**, frente a 120, 90 y 60.

**La ficha del fabricante lo confirma y explica de dónde sale.** LiveU describe la LU300S como una
unidad portátil que **pesa algo más de 900 gramos** y **admite hasta 30 Mbps**, combinando **hasta
seis conexiones de protocolo de internet (IP)**: **cuatro móviles, una inalámbrica local y una de
red de área local**, con su tecnología de **agregación** —*bonding*— sobre codificación **de alta
eficiencia (HEVC)**. Las conexiones móviles pueden ser **hasta cuatro de quinta o cuarta
generación**, con **dos módems internos de doble tarjeta** y **dos externos**.

**Qué es una mochila, dicho de una vez.** No es una antena: es **un codificador que parte la señal
entre varias conexiones móviles a la vez y las suma**. Ninguna de esas conexiones aguantaría sola
una señal de televisión con garantías; **juntas, y con un protocolo que reordena y recupera lo que
se pierde, sí**. Es la razón de que hoy sustituya al satélite en la mayor parte del directo
informativo: **no necesita permiso de frecuencia ni ventana de segmento espacial**, que es
justamente lo que la recomendación de la UIT dedica páginas a tramitar.

**Un apoyo de memoria, dicho como lo que es.** La cifra de la respuesta —**30 Mbps**— es la misma
que la Ley 11/2022 usa para definir una **red de alta capacidad**. **Las dos cosas no tienen
relación alguna**: es una coincidencia útil para retener el número, no un argumento.

**Nivel de la fuente**: **cuarto**, ficha de fabricante, leída el **2 de septiembre de 2026**. Con
la cautela que ese nivel arrastra: **una ficha cambia sin avisar**, y si LiveU renueva el modelo,
la cifra deja de valer aunque el tema siga escrito igual.

---

## 5. La transmisión dentro de la casa: la familia SMPTE ST 2110

Cuando la señal ya no sale del estudio sino que **circula por él**, el cable coaxial de vídeo ha
dejado paso a **la red de datos**. La familia de normas que ordena eso es la **SMPTE ST 2110**,
«Professional Media Over Managed IP Networks», y su idea central es que **el vídeo, el audio y los
datos auxiliares viajan como flujos separados** por la misma red, en lugar de ir embebidos en una
única señal.

El examen pregunta **qué parte cubre los datos auxiliares embebidos en el flujo**, y la respuesta
es la **ST 2110-40**. El índice oficial que la propia SMPTE publica lo dice en el título:
**«ST 2110-40 — Professional Media Over Managed IP Networks: SMPTE ST 291-1 Ancillary Data»**.

Conviene llevar la familia entera, porque los distractores salen de ella:

| Parte | Qué cubre |
|---|---|
| **ST 2110-10** | Temporización del sistema y definiciones |
| **ST 2110-20** | **Vídeo activo sin comprimir** |
| **ST 2110-21** | Conformado del tráfico y temporización de entrega del vídeo |
| **ST 2110-22** | Vídeo comprimido a **tasa binaria constante** |
| **ST 2110-30** | **Audio digital** por modulación por impulsos codificados |
| **ST 2110-31** | Transporte transparente de **AES3** |
| **ST 2110-40** | **Datos auxiliares** —la ST 291-1— |
| **ST 2110-41** | Marco de **metadatos rápidos** |
| **ST 2110-43** | Lenguaje de marcado de texto temporizado para **rotulación y subtítulos** |

**Y el detalle que resuelve la pregunta aunque falle la memoria**: de las cuatro opciones del
examen —2110-20, 2110-30, 2110-40 y 2110-50—, **la 2110-50 no existe**. No hay ninguna parte con
ese número en la familia publicada. Quien dude entre dos, al menos puede tachar una con
seguridad.

---

## 6. La difusión: la especificación europea (DVB) y la televisión digital terrestre

**DVB responde a *Digital Video Broadcasting*, radiodifusión de vídeo digital**, y no hace falta
creerlo: **es el encabezamiento de las propias normas europeas**. Las publica el Instituto Europeo de
Normas de Telecomunicaciones (*European Telecommunications Standards Institute*), **ETSI**. La
norma **ETSI EN 300 744**,
la del sistema de televisión digital terrestre, se titula «**Digital Video Broadcasting (DVB);
Framing structure, channel coding and modulation for digital terrestrial television**», y su
sucesora **ETSI EN 302 755**, «**Digital Video Broadcasting (DVB); Frame structure channel coding
and modulation for a second generation digital terrestrial television broadcasting system
(DVB-T2)**». Los formatos de compresión que aparecen en esta pregunta llevan todos el nombre del
Grupo de Expertos en Imágenes en Movimiento (*Moving Picture Experts Group*), **MPEG**. La
respuesta oficial del examen describe el DVB así: «una especificación europea de
emisión digital para televisión, asociada al formato de compresión MPEG-2».

**Que es europea, lo dice el BOE.** El **Plan Técnico Nacional de la Televisión Digital
Terrestre**, aprobado por el **Real Decreto 391/2019**, obliga a que los receptores incorporen «la
capacidad de recibir emisiones con la tecnología de transmisión de señales conforme a la **norma
EN 302 755 (DVB-T2)**». Una norma **EN** es una **norma europea**, y el legislador español la cita
por su designación.

**Y que está asociada al MPEG-2, lo dice la propia norma.** La **ETSI EN 300 744** declara en su
introducción que su objetivo es «**establecer el marco para la introducción de la televisión
digital basada en MPEG-2**», y en su descripción del sistema, que éste «**es directamente
compatible con las señales de televisión codificadas en MPEG-2 (ISO/IEC 13818)**». La respuesta
oficial, por tanto, **no es una aproximación de plantilla: es literalmente lo que dice la norma
europea del DVB terrestre**.

**Lo que sí conviene saber es que ese MPEG-2 se ha quedado atrás.** En la redacción vigente a la
fecha de corte, el mismo real decreto manda que la alta definición se codifique conforme a la
**Recomendación UIT-T H.264**, «Codificación de vídeo avanzada» (*advanced video coding*, **AVC**),
«equivalente a la norma internacional (**ISO/IEC 14496-10**), referenciada habitualmente como
**H.264/MPEG-4 AVC**», y prevé la evolución hacia formatos aún más eficientes. El enunciado del
examen describe **la primera generación**; la televisión digital terrestre española de hoy va por
la segunda. **Las dos cosas son ciertas, y hay que tener las dos.**

**Los tres distractores, y por qué se descartan de un vistazo** —los tres describen cosas reales,
pero ninguna es el DVB:

- «Transmisión de señales de radio desde un satélite directamente al domicilio del usuario, con una
  antena parabólica pequeña» → eso es la **recepción directa por satélite**, que es un modo de
  llegada, no una especificación de codificación.
- «Satélites de la banda Ku con tubos de potencia muy fuerte» (el enunciado cita dos por su
  nombre, **TDF** y **TV Satélite**) → eso son **satélites concretos**, no una norma.
- «Estaciones terrenas transportables para acceder y enviar imágenes a los satélites» → **eso es la
  definición del DSNG**, que este mismo tema acaba de leer en la recomendación de la UIT. El examen
  reparte la misma materia entre dos preguntas, y quien la tenga ordenada gana las dos.

---

## 7. Streaming y señal Pool

### 7.1 Streaming

**La respuesta oficial**: el *streaming* es el «método de transmisión de audio y vídeo **en tiempo
real a través de internet sin necesidad de descargar el archivo completo**».

Lo que define al *streaming* es precisamente eso: **la reproducción empieza antes de que el
fichero haya llegado entero**, porque el contenido se sirve en fragmentos que el reproductor va
consumiendo. Los tres distractores describen otras tres cosas:

- «Requiere la descarga completa del archivo antes de reproducirlo» → eso es **descarga**, lo
  contrario del *streaming*.
- «Técnica utilizada exclusivamente para juegos en línea» → falso por el «exclusivamente».
- «Requiere conexión por cable y no funciona con conexión inalámbrica» → falso: el *streaming* es
  indiferente al medio físico.

**Nivel de la fuente: plantilla oficial.** No hay norma que defina el *streaming*. Lo que sí hay
—y conviene tenerlo, porque el examen puede preguntar por el lado jurídico— es la definición legal
del servicio que se presta así: la **Ley 13/2022, General de Comunicación Audiovisual**, llama
**servicio de comunicación audiovisual televisivo a petición**, o **no lineal**, al que «se presta
para el visionado de programas y contenidos audiovisuales **en el momento elegido por el espectador
y a su propia petición**, sobre la base de un **catálogo de programas** seleccionado por el
prestador».

### 7.2 La señal Pool

**La respuesta oficial**: una señal Pool es «una señal de un evento que, debido a su importancia
informativa, **se encarga a la producción de una única televisión y ésta distribuye al resto de
televisiones que la soliciten**».

**Aquí lo que hay que enseñar es a leer el enunciado**, porque las cuatro opciones son **la misma
frase** con un añadido distinto:

| Opción | Qué añade | Por qué falla |
|---|---|---|
| a) | «señal **multicanal**» | Añade un rasgo técnico que la definición no exige |
| b) | «señal **con rótulos**» | Igual, y además el pool suele darse **limpio** para que cada cadena rotule |
| c) | «señal **con audio ambiente**» | Otro rasgo técnico añadido |
| **d)** | **nada** | **Es la correcta** |

**La regla que deja esta pregunta**, y que sirve para muchas otras: **cuando tres opciones son la
misma definición con un adjetivo técnico añadido y la cuarta va sin adjetivos, la buena suele ser
la que va sin adjetivos**. Un *pool* se define por **el acuerdo** —una televisión produce, las
demás reciben—, no por cómo venga la señal.

**Nivel de la fuente: plantilla oficial y uso profesional.** No hay norma que defina la señal Pool.

---

## 8. Los datos que el examen ha preguntado

Diez preguntas. Todas se contestan con el tema delante:

| Materia | Dato preguntado | Nivel |
|---|---|---|
| Redes | El **ancho de banda** limita la **velocidad de procesado y transmisión** | Uso profesional + **Ley 11/2022** |
| Fibra | **FTTH** es *Fiber To The Home* | **UIT-T G.984.1** |
| Satélite | Es **falso** que el periodo de la órbita geoestacionaria sea de **48 horas** | **UIT-R S.673-2** |
| Satélite | Datos para acceder a la señal: incluye la **frecuencia de bajada** | Plantilla oficial |
| Satélite | **DSNG** es *Digital Satellite News Gathering* | **UIT-R SNG.770-2** |
| Estudio sobre IP | Los **datos auxiliares embebidos** son la **SMPTE ST 2110-40** | **Índice oficial de la SMPTE** |
| Transmisión celular | La mochila **LU300S** admite hasta **30 Mbps** | **Ficha de LiveU** |
| Difusión | **DVB**: especificación **europea** de emisión digital de televisión, asociada al **MPEG-2** | **ETSI EN 300 744** + **Real Decreto 391/2019** |
| Internet | **Streaming**: en tiempo real, **sin descargar el archivo completo** | Plantilla oficial |
| Distribución | **Señal Pool**: la produce **una televisión** y la distribuye a las que la piden | Plantilla oficial |

**Siete de las diez tienen norma, recomendación o ficha detrás. Tres, sólo la plantilla.**

**Lo que no se ha preguntado y sale gratis de las mismas fuentes**: de la **S.673-2**, la **órbita
baja** —bajo unos **2 000 km**— y la **media** —unos **10 000 km**—, el **apogeo** y el
**perigeo**, y la **órbita directa** frente a la **retrógrada**; de la **G.984.1**, los otros tres
miembros de la familia —**FTTB**, **FTTC** y **FTTCab**—; de la **SNG.770-2**, que el equipo debe
poder manejarlo **dos personas en una hora** y que la **banda preferida es la de 14 GHz**; de la
**SMPTE ST 2110**, que la **-20** es el vídeo sin comprimir y la **-30** el audio; y de la
**Ley 11/2022**, los **30 Mbps** de la red de alta capacidad y la definición de **muy alta
capacidad** por la fibra hasta el punto de distribución.

---

## 9. Trazabilidad

- **Ley 11/2022, de 28 de junio, General de Telecomunicaciones**, `BOE-A-2022-10757`, leída en su
  texto consolidado **a 21 de diciembre de 2022**, **anexo de definiciones**: de ahí salen la
  **red de alta capacidad** —«acceso de banda ancha a velocidades de al menos 30 Mbps»— y la
  **red de muy alta capacidad** —«totalmente de elementos de fibra óptica, al menos hasta el punto
  de distribución»—.
- **Real Decreto 391/2019, de 21 de junio**, Plan Técnico Nacional de la Televisión Digital
  Terrestre, `BOE-A-2019-9513`, leído a la misma fecha: de ahí salen la exigencia de receptores
  conformes a la **norma EN 302 755 (DVB-T2)** y la codificación de la alta definición conforme a
  la **Recomendación UIT-T H.264**, equivalente a la **ISO/IEC 14496-10**, «referenciada
  habitualmente como H.264/MPEG-4 AVC».
- **Ley 13/2022, de 7 de julio, General de Comunicación Audiovisual**, `BOE-A-2022-11311`,
  misma fecha: la definición de **servicio televisivo a petición**.
- **Recomendación UIT-R S.673-2 (03/2002)**, «Términos y definiciones relativos a
  radiocomunicaciones espaciales»: **satélite sincrónico**, **geosincrónico** —con la nota de las
  **23 h y 56 min**—, **estacionario** —con la nota de la órbita **circular, ecuatorial y
  directa**— y **geoestacionario**, más **LEO** y **MEO**.
- **Recomendación UIT-R SNG.770-2 (01/2012)**, «Procedimientos operacionales uniformes para el
  periodismo electrónico digital por satélite (DSNG)», y su portada en inglés, donde la sigla
  aparece desarrollada: la **definición del DSNG**, el equipo de **dos personas en una hora**, la
  preferencia por la **banda de 14 GHz**, la lista de **comunicaciones adicionales** y la
  exigencia de documentar **anchura de banda y polarización**.
- **Recomendación UIT-T G.984.1 (03/2003)**, «Redes ópticas pasivas con capacidad de Gigabits:
  Características generales»: **FTTH**, **FTTB**, **FTTC** y **FTTCab**, con su desarrollo.
- **Norma europea ETSI EN 300 744 V1.6.2 (2015-10)**, «Digital Video Broadcasting (DVB); Framing
  structure, channel coding and modulation for digital terrestrial television», y **ETSI EN 302 755
  V1.4.1 (2015-07)**, la del **DVB-T2**: de ellas salen **el desarrollo de la sigla DVB** y las dos
  frases sobre el **MPEG-2**.
- **Índice oficial de la familia SMPTE ST 2110**, publicado por la propia SMPTE: los títulos de
  cada parte y la constancia de que **no existe una ST 2110-50**.
- **Ficha de LiveU del modelo LU300S**, leída el **2 de septiembre de 2026**: los **30 Mbps**, las
  **seis conexiones**, el peso **superior a 900 gramos** y la agregación sobre codificación de
  alta eficiencia.

**Lo que este tema no puede sostener, y por eso lo dice:**

- **Los 36.000 km de la órbita geoestacionaria no están en la recomendación leída.** Se recogen
  porque la plantilla da esa opción por verdadera y porque son el dato de uso corriente, pero **la
  fuente de este tema no los contiene**. Sí contiene, en cambio, las altitudes de la órbita baja y
  la media, que son las que se pueden citar con respaldo.
- **Cuál de los seis datos de acceso a una señal por satélite es el imprescindible es una decisión
  del tribunal, no un hecho comprobable.** Los tres descartados —banda, polarización y
  codificación— son datos reales; la recomendación de la UIT llega a exigir que la polarización se
  documente. La respuesta se estudia **porque el tribunal la corrige así**.
- **El streaming y la señal Pool no tienen norma.** Son uso profesional consolidado, y van
  marcados.
- **La asociación DVB–MPEG-2 del enunciado es literal de la norma europea**, pero corresponde a
  **la primera generación**. La norma española vigente a la fecha de corte asocia la alta
  definición al **H.264/MPEG-4 AVC** y obliga a soportar **DVB-T2**. El tema da las dos.
- **De las normas europeas se ha leído la portada y la introducción, no el articulado completo.**
  Son documentos de casi doscientas páginas de ingeniería de modulación, y de ellas este tema sólo
  toma **el título** —que desarrolla la sigla— y **las dos frases sobre el MPEG-2**. Lo demás no se
  afirma.
- **La cifra de la mochila depende de una ficha de fabricante**, no de una norma. Caduca cuando
  cambie el modelo.
