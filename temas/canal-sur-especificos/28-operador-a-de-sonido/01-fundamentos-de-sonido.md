# Tema 1 del específico de Operador/a de Sonido · Fundamentos de sonido

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Operador/a de Sonido · punto 1 |
| **Sirve para** | Puesto 2.28, Operador/a de Sonido (grupo B03): preguntas de teoría específica y de aplicación práctica del test, y la prueba práctica del puesto |
| **Fuente** | Norma: Real Decreto 2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida (el hercio, el pascal y el decibelio). Documentación de fabricante: DPA Microphones, *Mic University* (fase, polaridad y filtro en peine); Rane, RaneNote 155 (rango dinámico); RTW (correlación de fase). Manuales universitarios: OpenStax, *University Physics* y *Psychology 2e* (onda longitudinal, velocidad según el medio, células ciliadas, localización); UNSW Physclips (timbre y envolvente); B. Shinn-Cunningham, *Encyclopedia of Computational Neuroscience* (efecto de precedencia). Organismos oficiales: protocolo de vigilancia sanitaria de las personas trabajadoras expuestas a ruido (fisiología del oído); guía de aplicación del Documento Básico HR del Código Técnico de la Edificación (velocidad, aislamiento y acondicionamiento, ley de masa). Lo demás, oficio y cálculo |
| **Redacción que se estudia** | La vigente el 24/09/2026: el capítulo II del Real Decreto 2032/2009 en la redacción publicada en el BOE el 29/04/2020, vigente desde el 30/04/2020; su capítulo IV, en la redacción original, vigente desde el 22/03/2010 |
| **Extensión** | 9.300 palabras aproximadamente |

<!-- /portada -->

Siglas y unidades que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Sistema Internacional de
unidades (**SI**); hercio (**Hz**) y kilohercio (**kHz**); pascal (**Pa**) y micropascal (**µPa**);
newton (**N**); decibelio (**dB**), belio (**B**) y neper (**Np**); nivel de presión sonora (**dB
SPL**, *sound pressure level*); decibelios referidos a 0,775 voltios (**dBu**), a 1 voltio (**dBV**),
a 1 milivatio (**dBm**) y a la escala completa digital (**dBFS**, *decibels relative to full
scale*); curvas de criterio de ruido de fondo (**NC**, *noise criteria*, y **NR**, *noise rating*);
tiempo de reverberación medido como caída de sesenta decibelios (**RT60** o **T60**); coeficiente de
absorción (**α**); índice de
transmisión de la palabra (**STI**, *speech transmission index*); conector de audio profesional de
tres polos (**XLR**); Documento Básico HR, protección frente al ruido, del Código Técnico de la
Edificación (**DB HR**). Los fabricantes se citan por su nombre comercial: DPA Microphones (DPA),
Rane y RTW.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.28, punto 1):
>
> Fundamentos de sonido: ondas, frecuencia, amplitud, fase, dinámica, timbre, audición y acústica
> básica.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué es el sonido, si es onda longitudinal o transversal y si se propaga en
el vacío; en qué medio va más deprisa; qué relación une frecuencia,
periodo y longitud de onda, y cuánto mide la onda de un tono dado; cuál es la unidad legal de
frecuencia y la de presión; qué margen de frecuencias oye el ser humano; en qué se diferencian el
ruido blanco y el rosa, y cuál se usa para medir salas; qué exige la norma española cuando se usa
el decibelio; cuál es la referencia del dB SPL, del dBu, del dBV y del dBFS; cuántos decibelios son
el doble de tensión y el doble de potencia; qué es la fase, por qué un mismo retardo es un desfase
distinto en cada frecuencia, y por qué invertir la polaridad no es desfasar; qué es un filtro en
peine y la regla del 3:1; qué indica un correlador de fase en −1, 0 y +1; qué es el rango dinámico y
cuánto rango da cada bit; de qué depende el timbre y qué papel tiene la envolvente; qué parte del
oído convierte la vibración en impulsos nerviosos; con qué pistas se localiza un sonido y qué es el
efecto de precedencia; qué son las curvas isofónicas y en qué banda es
más sensible el oído; qué es el enmascaramiento; qué es el tiempo de reverberación y de qué depende;
qué superficies favorecen las ondas estacionarias y por qué no se corrigen ecualizando; qué quiere
una sala para la palabra frente a una para la música; en qué se diferencia aislar de acondicionar y
qué dice la ley de masa. En la prueba práctica: calcular longitudes de
onda y diferencias de nivel, detectar un problema de fase entre dos micrófonos y colocar micrófonos
en una sala difícil.

<!-- indice -->

## Índice

- [Ondas](#ondas)
  - [Qué es el sonido y qué lo describe](#qué-es-el-sonido-y-qué-lo-describe)
  - [La relación entre longitud de onda y frecuencia](#la-relación-entre-longitud-de-onda-y-frecuencia)
- [Frecuencia](#frecuencia)
  - [El hercio, unidad legal](#el-hercio-unidad-legal)
  - [El margen de frecuencias audibles](#el-margen-de-frecuencias-audibles)
  - [El ruido rosa y el ruido blanco](#el-ruido-rosa-y-el-ruido-blanco)
- [Amplitud](#amplitud)
  - [La presión sonora y el pascal](#la-presión-sonora-y-el-pascal)
  - [El decibelio, y por qué siempre necesita una referencia](#el-decibelio-y-por-qué-siempre-necesita-una-referencia)
  - [La aritmética del decibelio](#la-aritmética-del-decibelio)
  - [La amplitud y la distancia](#la-amplitud-y-la-distancia)
- [Fase](#fase)
  - [Qué es la fase](#qué-es-la-fase)
  - [Un mismo retardo, un desfase distinto en cada frecuencia](#un-mismo-retardo-un-desfase-distinto-en-cada-frecuencia)
  - [Polaridad no es fase](#polaridad-no-es-fase)
  - [Interferencia y filtro en peine](#interferencia-y-filtro-en-peine)
  - [Cómo se ve la fase en el control](#cómo-se-ve-la-fase-en-el-control)
- [Dinámica](#dinámica)
  - [El rango dinámico de una señal](#el-rango-dinámico-de-una-señal)
  - [El margen dinámico de un equipo](#el-margen-dinámico-de-un-equipo)
  - [Techo, suelo y margen de seguridad en la práctica](#techo-suelo-y-margen-de-seguridad-en-la-práctica)
- [Timbre](#timbre)
  - [Las tres cualidades del sonido](#las-tres-cualidades-del-sonido)
  - [El timbre y los armónicos](#el-timbre-y-los-armónicos)
  - [El timbre y la envolvente](#el-timbre-y-la-envolvente)
- [Audición](#audición)
  - [El camino del sonido por el oído](#el-camino-del-sonido-por-el-oído)
  - [Cómo oímos: las curvas isofónicas](#cómo-oímos-las-curvas-isofónicas)
  - [El margen audible y el enmascaramiento](#el-margen-audible-y-el-enmascaramiento)
  - [El oído y la fase](#el-oído-y-la-fase)
  - [Dónde está el sonido: localización y efecto de precedencia](#dónde-está-el-sonido-localización-y-efecto-de-precedencia)
  - [La audición como riesgo](#la-audición-como-riesgo)
- [Acústica básica](#acústica-básica)
  - [Qué le hace una sala al sonido](#qué-le-hace-una-sala-al-sonido)
  - [El tiempo de reverberación](#el-tiempo-de-reverberación)
  - [Los modos propios y las ondas estacionarias](#los-modos-propios-y-las-ondas-estacionarias)
  - [La sala para la palabra frente a la sala para la música](#la-sala-para-la-palabra-frente-a-la-sala-para-la-música)
  - [Aislar no es acondicionar](#aislar-no-es-acondicionar)
  - [Lo que la sala le hace al trabajo del técnico](#lo-que-la-sala-le-hace-al-trabajo-del-técnico)
- [Normativa que el tema invoca](#normativa-que-el-tema-invoca)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Ondas

### Qué es el sonido y qué lo describe

El sonido es una onda de presión que viaja por un medio elástico, y se describe con cuatro
magnitudes:

| Magnitud | Qué es | Unidad |
|---|---|---|
| Frecuencia | El número de ciclos por segundo | Hercio (Hz) |
| Periodo | El tiempo que dura un ciclo: la inversa de la frecuencia | Segundo |
| Longitud de onda | La distancia que recorre la onda en un ciclo | Metro |
| Amplitud | La magnitud de la variación de presión | Pascal, o decibelio en escala relativa |

El número de ciclos por segundo es la frecuencia, y su unidad es el hercio. Las dos confusiones
habituales son el periodo —que es el tiempo de un ciclo, no el número de ciclos— y el decibelio,
que mide amplitud, no frecuencia.

No hay sonido en el vacío, y la onda no transporta materia: transporta una perturbación.

En el aire la onda sonora es LONGITUDINAL: las partículas vibran en la misma dirección en que
avanza la onda, no de través. El manual universitario de física de OpenStax lo dice así: **«Sound
waves in air and most fluids are longitudinal, because fluids have almost no shear strength»** (las
ondas sonoras en el aire y en la mayoría de los fluidos son longitudinales, porque los fluidos casi
no resisten el esfuerzo cortante). La onda es una sucesión de zonas de más y de menos presión:
**«These compressions (high-pressure regions) and rarefactions (low-pressure regions) move out as
longitudinal pressure waves»** (esas compresiones, zonas de alta presión, y enrarecimientos, zonas
de baja presión, se alejan como ondas de presión longitudinales). En los sólidos no es así del todo:
**«In solids, sound waves can be both transverse and longitudinal»** (en los sólidos las ondas
sonoras pueden ser tanto transversales como longitudinales). Y no hay que confundirla con una onda
de radio, que es electromagnética (tema 12).

### La relación entre longitud de onda y frecuencia

La relación que las une, y que hay que tener a mano en todo el temario: la longitud de onda es
la velocidad del sonido dividida entre la frecuencia. Con 340 metros por segundo, un tono de 340
hercios mide un metro; uno de 34 hercios, diez metros; y uno de 3.400, diez centímetros.

| Frecuencia | Periodo (1/f) | Longitud de onda (340/f) |
|---|---|---|
| 34 Hz | 29,4 ms | 10 m |
| 100 Hz | 10 ms | 3,4 m |
| 340 Hz | 2,94 ms | 1 m |
| 1.000 Hz | 1 ms | 34 cm |
| 3.400 Hz | 0,294 ms | 10 cm |
| 10.000 Hz | 0,1 ms | 3,4 cm |

Los 340 m/s son la cifra redonda de oficio para el aire a temperatura ambiente; la velocidad real
depende de la temperatura del aire, y las cuentas del examen se hacen con la cifra que dé el
enunciado. La guía de aplicación del Documento Básico de protección frente al ruido del Código
Técnico de la Edificación toma **«344»** m/s para el aire y advierte que la velocidad **«Depende de
las condiciones ambientales (presión y temperatura)»**; el manual de OpenStax da **«At 0°C, the
speed of sound is 331 m/s, whereas at 20.0 °C, it is 343 m/s, less than a 4% increase»** (a 0 °C,
331 m/s; a 20 °C, 343 m/s: menos de un 4 % más).

La velocidad cambia mucho más con el MEDIO que con la temperatura. OpenStax lo explica: **«Because
liquids and solids are relatively rigid and very difficult to compress, the speed of sound in such
media is generally greater than in gases»** (como los líquidos y los sólidos son relativamente
rígidos y muy difíciles de comprimir, el sonido va en ellos, en general, más deprisa que en los
gases). Su tabla «Speed of Sound in Various Media» da, entre otros:

| Medio | Velocidad del sonido |
|---|---|
| Aire (gases, a 0 °C) | 331 m/s |
| Agua dulce (líquidos, a 20 °C) | 1.480 m/s |
| Agua de mar (líquidos, a 20 °C) | 1.540 m/s |
| Acero (sólidos, onda longitudinal) | 5.960 m/s |

El orden que hay que retener es, en general, aire < agua < sólidos rígidos (la misma tabla trae
sólidos blandos más lentos: **«Vulcanized rubber 54»** m/s): en el agua dulce, unas cuatro veces y media más
deprisa que en el aire; en el acero, unas dieciocho (cálculo sobre la tabla). La guía del Código
Técnico lo lleva a la edificación: **«El sonido viaja mucho más deprisa en los sólidos que en el
aire. Por ejemplo, la velocidad del sonido en ladrillo es aproximadamente 9 veces mayor que en el
aire.»** De ahí que el ruido de un golpe en el forjado llegue lejos por la estructura (se ve en «Acústica
básica»).

De ahí salen dos consecuencias que reaparecen en los temas de acústica y de micrófonos: los
graves son largos —por eso atraviesan tabiques y no se dejan absorber por materiales finos— y los
agudos son cortos —por eso son direccionales y los detiene cualquier obstáculo—.

Aplicación práctica: un obstáculo sólo «hace sombra» a las ondas más cortas que él. Un atril de
medio metro detiene los agudos de una voz, pero para un grave de 100 Hz (3,4 m) es transparente;
por eso un panel absorbente fino corrige las reflexiones agudas de un locutorio y no toca su
retumbe grave, que pide trampas de graves (se ve en «Acústica básica»).

## Frecuencia

### El hercio, unidad legal

La frecuencia se mide en hercios, y el hercio es unidad legal en España. El Real Decreto
2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida, lo incluye
en la tabla 3 de su capítulo II, **«Unidades SI derivadas coherentes con nombres y símbolos
especiales»**, con la magnitud **«frecuencia»**, el nombre **«hercio»** y el símbolo **«Hz»**, y
lo acota en la nota (d) de esa tabla: **«El hercio sólo se utiliza para los fenómenos
periódicos»**. Un hercio es un ciclo por segundo (s⁻¹).

### El margen de frecuencias audibles

El margen de frecuencias audible por un ser humano va de 20 Hz a 20.000 Hz. Es un valor
convencional para un oído joven y sano.

| Zona | Margen | Qué hay ahí |
|---|---|---|
| Infrasonidos | Por debajo de 20 Hz | No se oyen; se sienten |
| Graves | 20 – 250 Hz | El cuerpo del sonido |
| Medios | 250 – 4.000 Hz | La inteligibilidad de la voz |
| Agudos | 4.000 – 20.000 Hz | El brillo y el detalle |
| Ultrasonidos | Por encima de 20.000 Hz | No se oyen |

Los límites entre graves, medios y agudos son de oficio, no de norma. El margen audible se
estrecha con la edad por el extremo agudo. Un margen de frecuencias no es un margen dinámico: el
primero se da en hercios y el segundo en decibelios (se ve en «Dinámica»).

### El ruido rosa y el ruido blanco

En el ruido rosa la energía disminuye a medida que aumenta la frecuencia. Los dos ruidos de
referencia, y qué los separa:

| Ruido | Cómo reparte la energía | Cómo suena |
|---|---|---|
| Blanco | La misma energía por HERCIO: es plano por frecuencia | Agudo, siseante |
| Rosa | La misma energía por OCTAVA: cae 3 dB por octava | Equilibrado, como una cascada |

Por qué el rosa cae y aun así se considera «plano»: porque cada octava tiene el doble de
hercios que la anterior. La octava de 100 a 200 Hz contiene 100 hercios; la de 1.000 a 2.000
contiene 1.000. Para que las dos tengan la misma energía total, la energía POR HERCIO tiene que
caer a la mitad, y eso son 3 dB por octava.

De ahí que el ruido rosa sea el que se usa para medir y ecualizar salas: el oído percibe por
octavas, y un analizador por bandas de octava lo ve horizontal.

Las confusiones habituales: la caída de 6 dB por octava es la del ruido marrón o browniano, no la
del rosa; «la misma energía en todas las frecuencias» describe al blanco; y el uso del ruido para
enmascarar conversaciones en oficinas es una aplicación, no una definición.

Una octava es el intervalo entre una frecuencia y su doble (de 1.000 a 2.000 Hz); el margen audible
de 20 Hz a 20 kHz abarca unas diez octavas, porque 2¹⁰ = 1.024.

## Amplitud

### La presión sonora y el pascal

La amplitud de una onda sonora es la magnitud de la variación de presión, y la unidad legal de
presión es el pascal. El Real Decreto 2032/2009 lo recoge en la misma tabla 3 de su capítulo II;
con las celdas separadas por puntos, porque un cuadro no admite otro entrecomillado y cada celda va
literal:

> **«presión, tensión» · «pascal» · «Pa» · «N/m2»**

Un pascal es un newton por metro cuadrado. Y el orden de magnitud es lo que hace falta entender:
el umbral de audición está en 20 micropascales —veinte millonésimas de pascal— y el umbral de
dolor, en torno a 20 pascales. Un millón de veces más.

Ese margen de un millón a uno es la razón de que el sonido no se mida en pascales sino en
decibelios.

Tres unidades cercanas que miden otra cosa, y que un test puede poner como opción falsa:

| Unidad | Qué mide de verdad |
|---|---|
| Newton | Fuerza, no presión: le falta dividir por la superficie |
| Bar y milibar | Presión, sí, pero no es unidad del SI: el real decreto la recoge en su tabla 8, entre las unidades ajenas al SI de sectores específicos, con el valor **«1 bar = 0,1 MPa = 100 kPa»**: cien mil pascales |
| W/m² | Intensidad: potencia por unidad de superficie, que es otra magnitud |

### El decibelio, y por qué siempre necesita una referencia

El decibelio también está en el real decreto, en la tabla 8 de su capítulo IV, junto al belio y al
neper. El apartado 4 de ese capítulo, en cita literal:

> **«La tabla 8 cita también las unidades de las magnitudes logarítmicas, el neper, el belio y el
> decibelio. Estas son unidades adimensionales y se emplean para proporcionar información sobre la
> naturaleza logarítmica del cociente de magnitudes.»**

El mismo apartado precisa que **«El belio y el decibelio, B y dB, 1 dB = (1/10) B, se emplean para
expresar el valor de logaritmos de base 10 de cocientes entre magnitudes»** y que **«Las unidades
neper, belio y decibelio se aceptan para su uso con el SI pero no se consideran unidades SI.»**

Y la nota (i) de la tabla 8, que es la frase que ordena todo el uso del decibelio en audio:

> **«Cuando se usan estas unidades, es importante indicar cuál es la naturaleza de la magnitud en
> cuestión y el valor de referencia empleado.»**

De esa frase se sigue la regla que hay que llevarse del tema entero: un decibelio a secas no
significa nada. Un decibelio es siempre la relación entre una magnitud y una referencia, y
cambiar la referencia cambia el número.

| Escala | Referencia | Dónde se usa |
|---|---|---|
| dB SPL | 20 micropascales, el umbral de audición | Presión sonora en el aire |
| dBu | 0,775 voltios | Nivel de línea profesional |
| dBV | 1 voltio | Nivel de línea de consumo |
| dBFS | La escala digital completa: 0 es el máximo y todo lo demás es negativo | Audio digital |
| dBm | 1 milivatio sobre una impedancia dada | Potencia |

Con esa tabla se entiende por qué el umbral de audición son 0 dB SPL (20 µPa es la propia
referencia) y el umbral de dolor unos 120 dB SPL: 20 Pa son un millón de veces 20 µPa, y 20 × log
10⁶ = 120 dB. Los niveles de línea, las impedancias y la conversión entre escalas eléctricas son
materia del tema 2.

### La aritmética del decibelio

Las cuentas de decibelios se hacen con una sola tabla en la cabeza.

Para magnitudes de AMPLITUD —tensión, presión sonora— la fórmula es 20 por el logaritmo decimal del
cociente. Para magnitudes de POTENCIA, es 10 por ese logaritmo. Ésa es la distinción que más
se falla.

| Relación | En amplitud (20 × log) | En potencia (10 × log) |
|---|---|---|
| × 2 | +6 dB | +3 dB |
| × 4 | +12 dB | +6 dB |
| × 10 | +20 dB | +10 dB |
| × 1,41 (raíz de dos) | +3 dB | +1,5 dB |
| × 1/2 | −6 dB | −3 dB |

Tres cuentas resueltas, que son las que un test pone:

1. La diferencia entre una señal de 1 voltio y una de 2 voltios es de 6 dB: veinte por el logaritmo
   decimal de dos son aproximadamente seis. La trampa es la opción de 3 dB, que es la respuesta
   correcta si la magnitud fuera POTENCIA. Doblar la potencia son 3 dB; doblar la amplitud son 6.
2. La misma cuenta al revés: si un micrófono capta 80 dB SPL y otro 74 dB SPL, la señal del primero
   es aproximadamente 2 veces mayor en amplitud. La diferencia es de 6 dB, y 6 dB de amplitud son un
   factor de dos. Quien tome los 6 dB como «seis veces» o quien use la fórmula de potencia (que da
   unas 4 veces) acaba en una respuesta falsa.
3. Dos fuentes iguales y no correladas suman unos 3 dB, no el doble de decibelios: se suman sus
   potencias (× 2 → +3 dB). Dos señales idénticas y en fase suman 6 dB, porque se suman sus
   amplitudes (× 2 → +6 dB); y en contrafase se anulan (se ve en «Fase»).

### La amplitud y la distancia

En campo libre la presión cae con la distancia. La cifra la da DPA: **«The SPL from point sources
drops by 6 dB/doubling of distance.»** Si la boca se toma como fuente puntual (aproximación de
oficio), pasar el micrófono de 40 a 20 cm sube la voz unos 6 dB y de 40 a 10 cm unos 12 dB, mientras
el ruido de fondo, que llega de lejos y de todas partes, apenas cambia. Por eso acercar el micrófono
es el primer recurso contra el ruido y contra la sala; dentro de un recinto la caída deja de
cumplirse lejos de la fuente, donde manda la reverberación (se ve en «Acústica básica»).

## Fase

### Qué es la fase

La fase dice en qué punto de su ciclo está una onda en un instante dado, y sólo tiene sentido al
comparar. DPA Microphones lo explica así: **«Phase can only be expressed if the actual waveform is
compared to a reference or another waveform – and at a given frequency.»** Es decir, se compara una
onda con otra, y a una frecuencia concreta.

El desfase nace de un retardo. DPA: **«The phase shift occurs due to a shift in time, a delay.»** Y
enumera sus tres causas típicas: que dos micrófonos estén a distinta distancia de la fuente, que se
aplique una línea de retardo, o la física de un filtro eléctrico. Se expresa como ángulo: **«Usually,
we describe a phase shift by the so-called phase angle in the range of ±180°»**. Un ciclo completo
son 360°; medio ciclo, 180°; un cuarto de ciclo, 90°.

### Un mismo retardo, un desfase distinto en cada frecuencia

La fase depende de la frecuencia porque un mismo tiempo es una fracción distinta del periodo de
cada una. El ejemplo de DPA: el periodo de 1 kHz dura 1 ms, y un desfase de 90° (un cuarto de
periodo) equivale a 0,25 ms; a 2 kHz el periodo dura 0,5 ms, y los mismos 90° son 0,125 ms. Su
conclusión: **«the time shift of a constant phase shift varies with frequency»**.

Leído al revés, que es como se presenta en el trabajo: un retardo fijo produce un desfase que
crece con la frecuencia. Un retardo de 1 ms es un ciclo entero (360°, en fase) a 1 kHz, medio ciclo
(180°, en contrafase) a 500 Hz y un cuarto de ciclo (90°) a 250 Hz. Y 1 ms de retardo son unos 34 cm
de diferencia de recorrido con 340 m/s. Por eso dos micrófonos a distinta distancia de la misma
fuente nunca están «en fase» o «en contrafase» sin más: lo están a unas frecuencias sí y a otras no.

Los ecualizadores también desfasan. DPA: **«Most equalizers or equalizing circuits may exhibit
frequency-dependent phase shifts»** (se desarrolla en el tema 5).

### Polaridad no es fase

Invertir la polaridad es cambiar el signo de la señal: lo positivo pasa a negativo y al revés. DPA:
**«the signal is multiplied by "-1"»**. Se dice a menudo que eso es desfasar 180°, y DPA lo matiza:
**«This is, however, not exactly correct. A phase shift requires a time shift, i.e., a delay, which
is not involved in swopping polarity. On the other hand, after inversion, the signal is now 180° out
of phase»**. La inversión afecta a todas las frecuencias por igual y sin retardo; un retardo sólo da
180° a unas frecuencias concretas: aquella cuyo medio periodo coincide con el retardo y sus múltiplos impares (con 1 ms, 500,
1.500, 2.500 Hz…), que son los huecos del filtro en peine del epígrafe siguiente.

El botón de inversión de las mesas lleva la letra griega fi: **«The Greek letter φ [small letter
phi] on the button indicates the function of inversion. Sometimes, it looks like the letter Ø»**.
Aunque se le llame «botón de fase», lo que hace es invertir la polaridad.

El convenio de polaridad del micrófono en conexión balanceada, según DPA: **«pin 2 always represents
the in-phase signal of the acting sound pressure»**; una presión creciente sobre la membrana da una
tensión positiva creciente en la patilla 2. DPA acota a quién se aplica: **«This is true for
balanced condenser microphones for professional audio (not necessarily measurement microphones),
while dynamic microphones behave a little differently»** (vale para los micrófonos de condensador
balanceados de audio profesional, no necesariamente para los de medida, y los dinámicos se
comportan algo distinto). Un cable con las patillas 2 y 3 cruzadas invierte la
polaridad de todo lo que pasa por él (el conexionado es materia de los temas 2 y 11).

### Interferencia y filtro en peine

Cuando dos señales iguales se suman, la fase decide el resultado: en fase se refuerzan (+6 dB, se
vio en «Amplitud»), en contrafase se anulan, y entre medias suman a medias. Si una de las dos llega
con retardo, cada frecuencia se suma con una fase distinta y la respuesta queda llena de picos y
huecos regulares: es el filtro en peine. DPA lo define: **«Comb filtering occurs when a sound adds
to itself within a short time interval. This interval typically ranges from less than one ms to
approximately 25 ms.»** Y da sus dos orígenes: las reflexiones, y que haya más de un micrófono abierto
captando la misma señal en posiciones distintas. Pone una condición: **«the levels of the signals
must be within 10 dB from each other»**. El nombre sale de la forma de la respuesta, que parece un
peine.

El caso de plató que DPA describe: en una tertulia, el micrófono del presentador suena algo
embarrado y el del invitado limpio, porque la voz del presentador entra por los dos micrófonos, a
distinta distancia.

Los remedios, según DPA:

| Remedio | Qué dice |
|---|---|
| Separar niveles | Atenuar el sonido retardado que capta el micrófono **«by at least 10 dB»** |
| Regla del 3:1 | **«a neighboring microphone should be at least three times further away, (given the sensitivity and the gain is the same on both microphones). (20 *log (1/3) ≈ -10 dB)»**: el micrófono vecino, al menos tres veces más lejos de la fuente que el suyo |
| Micrófonos en línea equidistante | La proporción sube, en teoría: **«should be 4.5:1»**; con micrófonos direccionales, DPA admite que el factor 3 suele bastar aunque haya dos vecinos |
| Reflexiones | Quitar o girar la superficie que refleja, absorberla, o poner el micrófono sobre ella: **«In this way, it becomes a boundary layer microphone»** |

Aplicación práctica: en una mesa de tertulia con cuatro invitados, cada micrófono lo más cerca
posible de su boca, los vecinos al menos a tres veces esa distancia, y los micrófonos que no
hablan, cerrados o bajados; un atril o una mesa de cristal justo debajo del micrófono es una fuente
de peine por reflexión.

### Cómo se ve la fase en el control

Para la mezcla estéreo, la herramienta es el correlador de fase. El fabricante de medidores RTW
explica su uso: **«Mostly, phase correlation is used to determine the mono compatibility of a
stereo signal, but depending on where you use it, it can also reveal other things, such as bad
microphone placement»**. Su escala: **«from -1 (switched polarity) over 0 (unrelated) to 1
(identical)»**. En +1 los dos canales son iguales (mono); en 0 no guardan relación; hacia −1 están
en contrafase, y al sumarlos a mono se cancelan. RTW da como orientación de fabricante que **«Normal
stereo mixes usually show correlation values between 0.3 and 0.7»**. La medición y el control de
calidad se desarrollan en el tema 13, y la compatibilidad mono en el 14.

## Dinámica

### El rango dinámico de una señal

La dinámica es la variación de nivel de un sonido en el tiempo: la distancia entre sus pasajes más
fuertes y los más débiles. El fabricante Rane lo define así: **«The dynamic range of an audio
passage is the ratio of the loudest signal to the quietest signal»**; como es un cociente, se da en
decibelios. Una locución de informativos tiene poca dinámica; una orquesta sinfónica, mucha. Los
procesadores que la modifican —compresor, limitador, expansor, puerta— son materia del tema 5, y su
medida como sonoridad y rango de sonoridad, del tema 13.

### El margen dinámico de un equipo

El margen dinámico de un equipo es la diferencia, en decibelios, entre el nivel de señal máximo y el
nivel de ruido del equipo.

| Extremo | Qué es |
|---|---|
| El techo | El nivel máximo que el equipo admite antes de distorsionar |
| El suelo | El ruido propio del equipo: el siseo que hay incluso sin señal de entrada |

El margen dinámico es la distancia entre los dos. Por debajo del suelo la señal se pierde en el
ruido; por encima del techo se distorsiona. Lo utilizable es lo que hay en medio.

Las definiciones falsas cambian uno de los dos extremos: «entre el nivel de señal mínimo y el
ruido» (el mínimo y el ruido son prácticamente lo mismo); «entre el umbral de audición máximo, o
mínimo, y el ruido del equipo» (mezclan una magnitud del oído con una del equipo). El margen
dinámico de un equipo se mide con las dos magnitudes de ese equipo. El margen dinámico del oído es
otra cosa —la diferencia entre el sonido más débil que se percibe y el que produce dolor— y es del
orden de 120 dB.

Esa cifra cuadra con la cuenta del epígrafe «Amplitud» (de 20 µPa a 20 Pa, un millón a uno, 120 dB)
y con la que da Rane para el equipo profesional: **«Professional-grade signal processing equipment
can output maximum levels of +26 dBu, with the best noise floors being down around -94 dBu. This
gives a dynamic range of 120 dB -- an impressive number coinciding nicely with the 120 dB dynamic
range of normal human hearing»** (cifras del fabricante: +26 − (−94) = 120 dB).

El cálculo que va con el margen: cada bit de cuantificación aporta unos 6 dB de margen dinámico
teórico (20 × log 2 ≈ 6,02 dB), así que 16 bits dan unos 96 dB y 24 bits unos 144 dB. Por eso el
audio de producción se graba a 24 bits.

### Techo, suelo y margen de seguridad en la práctica

La regla de oficio que se sigue de todo lo anterior: la señal se trabaja lo bastante alta para
separarse del ruido y lo bastante baja para no tocar el techo, y la distancia que se deja hasta el
techo es el margen de seguridad (*headroom*). En digital el techo es absoluto —0 dBFS—, y lo que lo
supera se recorta sin remedio. Los niveles de alineación y el margen que fija la Unión Europea de
Radiodifusión son materia de los temas 5 y 13.

## Timbre

### Las tres cualidades del sonido

Todo lo que se oye se describe con tres cualidades, y cada una depende de una magnitud física
distinta. Confundirlas es el error que este punto castiga.

| Cualidad | Qué distingue | De qué magnitud depende |
|---|---|---|
| Tono | Grave o agudo | De la frecuencia: los ciclos por segundo |
| Intensidad | Fuerte o débil | De la amplitud: la magnitud de la variación de presión |
| Timbre | Qué instrumento suena | De la composición armónica y de la envolvente (cómo empieza, se sostiene y se apaga) |

La frecuencia no es el tono, es su causa. Se mide en hercios y es física; el tono es percepción.
La misma distinción vale para las otras dos: la amplitud es física, la intensidad percibida es
psicoacústica, y por eso se mide en decibelios, que es una escala logarítmica ajustada a cómo oye el
oído.

### El timbre y los armónicos

La propiedad del sonido directamente relacionada con las intensidades relativas de sus armónicos
es el timbre.

Qué son los armónicos. Cuando un instrumento da una nota, no produce una sola frecuencia:
produce la fundamental —que es la que determina el tono— y una serie de múltiplos enteros de
ella, los armónicos. Un la de 440 Hz lleva componentes en 880, 1.320, 1.760 y así sucesivamente.

Lo que cambia de un instrumento a otro no son las frecuencias, sino cuánto pesa cada una. Un
violín y una flauta que dan el mismo la tienen los mismos armónicos; lo que difiere es la
intensidad relativa de cada uno.

En un test, «frecuencia» no es una cualidad del sonido sino una magnitud física, y la intensidad y
el tono dependen de la amplitud y de la fundamental: ninguna de las tres es el timbre.

Y una consecuencia de oficio: el timbre es lo que un ecualizador modifica. Al subir o bajar
bandas se cambia el peso relativo de los armónicos, y por eso la ecualización cambia el carácter de
una voz sin cambiar la nota que dice.

Dos consecuencias más para el operador (oficio): como los armónicos de una voz o de un instrumento
llegan muy por encima de su fundamental, cortar agudos apaga el timbre aunque la nota siga
entendiéndose; y como los agudos son los más direccionales (se vio en «Ondas»), un micrófono fuera
del eje de la boca capta la misma voz con otro timbre, más apagado.

### El timbre y la envolvente

Los armónicos no lo son todo. La Escuela de Física de la Universidad de Nueva Gales del Sur, en su web Physclips, lo dice
sin rodeos: **«Timbre depends strongly on envelope: on how the sound varies over time. (Timbre also
depends on spectrum.)»** (el timbre depende mucho de la envolvente, de cómo varía el sonido en el
tiempo; y también del espectro). En una nota musical se pueden distinguir a veces cuatro fases, que
la misma fuente enumera como **«Attack, decay, sustain and release»**; no todas las notas las tienen
todas (la del clave, en la práctica, no tiene sostenimiento: sólo un ataque rápido y una caída lenta):

| Fase | Qué hace el nivel |
|---|---|
| Ataque (*attack*) | Sube deprisa al empezar la nota |
| Caída (*decay*) | Baja después del ataque |
| Sostenimiento (*sustain*) | Apenas varía mientras la nota dura |
| Extinción (*release*) | Cae hasta cero al terminar |

Y lo que más pesa es el arranque: **«Without the starting (and sometimes finishing) transients, it
is very difficult to recognise different musical instruments»** (sin los transitorios de arranque, y
a veces los de final, es muy difícil reconocer los instrumentos). Su ejemplo: una grabación de
clave reproducida al revés reparte la energía entre las frecuencias exactamente igual y, sin
embargo, a su autor deja de sonarle a instrumento de cuerda y le recuerda, si acaso, a un viejo
órgano de pedales.

Consecuencia para el operador (oficio): lo que recorta o suaviza los ataques —una puerta que abre
tarde, un compresor de ataque rápido (tema 5)— cambia el timbre tanto como un ecualizador.

## Audición

### El camino del sonido por el oído

El recorrido lo da el protocolo de vigilancia sanitaria específica de las personas trabajadoras
expuestas a ruido, del Consejo Interterritorial del Sistema Nacional de Salud, en su «Recuerdo
fisiológico». Primero el oído externo: **«Las ondas sonoras, son
recogidas por el pabellón auditivo y llegan por el conducto auditivo externo hasta la membrana del
tímpano donde la hacen vibrar.»** Después el oído medio y el interno:

> **«El movimiento de la membrana del tímpano se comunica a través de la cadena de huesecillos del
> oído medio (martillo, yunque y estribo) a la ventana oval. A través de dicha ventana, y debido a
> los movimientos del estribo, se genera una onda en el líquido del oído interno y allí donde esta
> onda alcanza su máxima amplitud se genera una estimulación de las células ciliadas que producen un
> impulso eléctrico correspondiente a unas frecuencias determinadas.»**

| Parte | Qué hay | Qué hace |
|---|---|---|
| Oído externo | Pabellón y conducto auditivo | Recoge la onda y la lleva al tímpano |
| Oído medio | Tímpano y huesecillos (martillo, yunque, estribo) | Pasa la vibración a la ventana oval |
| Oído interno | Cóclea, con su líquido y sus células ciliadas | Convierte la vibración en impulsos nerviosos |

La pieza que convierte la vibración en señal nerviosa es, pues, la cóclea, con sus células ciliadas;
el manual de psicología de OpenStax completa el trayecto: **«As hair cells become activated, they
generate neural impulses that travel along the auditory nerve to the brain»** (al activarse, las
células ciliadas generan impulsos nerviosos que viajan por el nervio auditivo hasta el cerebro). El
tímpano y los huesecillos sólo transmiten.

Y cada frecuencia tiene su sitio en la cóclea. El protocolo: **«las bajas frecuencias son detectadas
en la parte más superior de la cóclea, próxima al helicotrema. Las altas frecuencias, por el
contrario, se captan en la zona inferior de esta, es decir, junto a la ventana oval.»** Ése es el
enlace con el riesgo laboral del tema 16: el mismo protocolo dice que las células ciliadas externas
próximas a la ventana oval perciben **«las frecuencias agudas, entre ellas las de 3.000 Hz y 6.000 Hz, las cuales
suelen verse habitualmente afectadas por el efecto nocivo del ruido»**.

### Cómo oímos: las curvas isofónicas

El conjunto de curvas que representan la sensibilidad del oído a diferentes frecuencias para todo
el margen audible son las curvas isofónicas.

Qué dicen: que el oído no es plano. Para que un tono de 50 hercios se perciba tan fuerte
como uno de 1.000, el de 50 tiene que sonar bastante más alto en presión. Cada curva une los
puntos que se perciben igual de fuertes, y la unidad de esa percepción es el fon.

Las tres consecuencias de oficio, que es lo que las hace útiles y no una curiosidad:

1. La sensibilidad cambia con el NIVEL. A volumen bajo el oído pierde graves y agudos; a volumen
   alto se aplana. Por eso una mezcla que suena bien fuerte se queda sin fondo al bajarla, y por
   eso existe el botón *loudness* de los equipos domésticos.
2. El oído es más sensible entre 2 y 5 kilohercios, que es la banda de la inteligibilidad de la
   voz. Ahí un decibelio de más se nota mucho más que en cualquier otro sitio.
3. Por eso las escalas de medida llevan ponderación: la curva A del sonómetro imita la respuesta
   del oído a nivel bajo, y es la que usa la normativa de ruido laboral.

No hay que confundirlas con las curvas NC y NR, que fijan cuánto ruido de fondo se tolera en un
recinto, por bandas de octava: no describen el oído, describen cuánto ruido admite una sala.

La consecuencia para el control: se mezcla a un nivel de escucha estable y moderado, y se
comprueba la mezcla también a volumen bajo, que es como la oirá buena parte del público.

### El margen audible y el enmascaramiento

El margen audible del oído humano se sitúa convencionalmente entre 20 hercios y 20 kilohercios, y
se estrecha con la edad por el extremo agudo.

El enmascaramiento es el fenómeno por el que un sonido hace inaudible a otro. Sus tres reglas:

1. Un sonido enmascara mejor a los de frecuencia PRÓXIMA, y más hacia arriba que hacia abajo:
   un grave potente tapa a los medios; un agudo no tapa a los graves.
2. El enmascaramiento crece con el nivel del enmascarador.
3. Hay enmascaramiento TEMPORAL además del simultáneo: un sonido fuerte tapa a lo que viene
   inmediatamente después, y en menor medida a lo inmediatamente anterior.

Y es la base de la compresión de audio con pérdida: un códec que descarta lo que el oído no va a oír
necesita saber exactamente qué enmascara qué.

Aplicación práctica (oficio): una música con mucha energía en la banda de la voz tapa la locución
aunque vaya más baja; en vez de bajar toda la música, se le abre hueco en esa banda o se la hace
ceder cuando entra la voz (tema 5).

### El oído y la fase

El oído es poco sensible a la fase de las componentes de un sonido aislado. DPA muestra dos ondas
de forma muy distinta con las mismas componentes y advierte: **«they sound the same if reproduced
in a linear system, as the ear only to a minor degree is sensitive to phase»**. Lo que sí se oye es
la suma de una señal con su copia retardada —el filtro en peine— y la contrafase entre canales,
que hace desaparecer al pasar a mono lo que va en contrafase.

### Dónde está el sonido: localización y efecto de precedencia

Con dos oídos se localiza. El manual de OpenStax distingue dos clases de pistas: **«the auditory
system uses both monaural (one-eared) and binaural (two-eared) cues to localize sound»** (el sistema
auditivo usa pistas monoaurales, de un oído, y biaurales, de los dos). Las monoaurales salen de cómo
el pabellón modifica el sonido, y ayudan a situarlo **«above or below and in front or behind»**
(arriba o abajo, delante o detrás). Las biaurales son las del plano horizontal: **«Binaural cues, on
the other hand, provide information on the location of a sound along a horizontal axis»** (las
biaurales informan de la posición de un sonido a lo largo del eje horizontal). Son dos:

| Pista biaural | Qué es, según OpenStax |
|---|---|
| Diferencia interaural de nivel | **«a sound coming from the right side of your body is more intense at your right ear than at your left ear because of the attenuation of the sound wave as it passes through your head»**: el sonido que viene de la derecha llega más fuerte al oído derecho, porque la cabeza lo atenúa |
| Diferencia interaural de tiempo | **«the small difference in the time at which a given sound wave arrives at each ear»**: la pequeña diferencia en el instante en que la misma onda llega a cada oído |

Son las mismas dos diferencias, de nivel y de tiempo, con las que trabajan el panorama de la mesa y
las técnicas de microfonía estéreo (temas 3 y 14; la relación es de oficio).

En una sala llegan además las reflexiones, cada una desde otra dirección, y el oído no se pierde
gracias al efecto de precedencia. La definición, de la *Encyclopedia of Computational Neuroscience*
(B. Shinn-Cunningham, Universidad de Boston): **«when two sound sources reach a listener close
together in time, listeners often hear a single "fused" image whose perceived direction is near the
location of the first-arriving sound»** (cuando dos sonidos llegan al oyente muy juntos en el
tiempo, se suele oír una sola imagen fundida, situada cerca de la posición del que llegó primero).
La misma fuente le da como sinónimo **«Law of the first wavefront»** (ley del primer frente de onda);
en el oficio se le llama también efecto Haas. Sus plazos: con chasquidos breves es más fuerte
**«when the leading click precedes the lagging click by 1–5 ms»** y se debilita enseguida, hasta
oírse el segundo como un suceso aparte; **«For more "natural" sounds, like speech or music, the
precedence effect persists for tens of ms»** (con la voz o la música dura decenas de milisegundos).
Es lo que hay detrás de la frontera de oficio de los 50 ms que se da en «Acústica básica», y de los
refuerzos retardados de una sonorización (tema 10): mientras el sonido del escenario llegue primero,
el oído sitúa allí la fuente.

### La audición como riesgo

El oído del operador es su herramienta de trabajo, y la exposición prolongada a niveles altos
—monitores, auriculares, directos— lo daña. Los niveles de exposición, la ponderación A en la
normativa de ruido laboral y las medidas preventivas son materia del tema 16.

## Acústica básica

### Qué le hace una sala al sonido

Entre la fuente y el oyente, una sala cerrada añade tres cosas al sonido directo:

| Componente | Qué es | Qué aporta |
|---|---|---|
| Sonido directo | Lo que llega en línea recta | La inteligibilidad y la localización |
| Primeras reflexiones | Los rebotes que llegan en los primeros milisegundos | Refuerzan si llegan pronto; estorban si llegan tarde |
| Cola reverberante | La suma de miles de rebotes que decae | El cuerpo, la envolvente y, si sobra, la confusión |

La frontera de los cincuenta milisegundos es la que decide: una reflexión que llega antes de ese
plazo el oído la SUMA al sonido directo y la percibe como refuerzo. La que llega después se
percibe como eco separado. Sobre esa frontera se construye toda la acústica de salas para la
palabra.

Con 340 m/s, 50 ms son unos 17 metros de recorrido de más: una pared de fondo a unos 8,5 m que
devuelva el sonido con fuerza ya se oye como eco (cálculo sobre la cifra de oficio).

### El tiempo de reverberación

El tiempo de reverberación es cuánto tarda el sonido de una sala en caer sesenta decibelios
después de que la fuente calle. Por eso se llama RT60.

Y los valores que se buscan según para qué sea la sala:

| Uso | RT60 orientativo | Por qué |
|---|---|---|
| Estudio de locución o control | Por debajo de 0,3 s | Se quiere oír la fuente, no el local |
| Teatro y sala de conferencias | De 0,8 a 1,2 s | La palabra necesita claridad: la cola larga la emborrona |
| Sala de concierto sinfónico | De 1,8 a 2,2 s | La música quiere cuerpo y envolvente |
| Catedral | Más de 5 s | Ininteligible para la palabra, y es lo que el canto gregoriano aprovecha |

Las cifras de RT60 son orientativas y ninguna es normativa: son órdenes de magnitud para entender la
escala, no valores que memorizar.

La relación que gobierna el número es la fórmula de Sabine: el tiempo de reverberación crece con
el VOLUMEN de la sala y decrece con la ABSORCIÓN que hay dentro. Una sala grande y desnuda
retumba; la misma sala llena de gente, no. El público es el mayor absorbente de un teatro, y por
eso una sala se mide vacía sabiendo que va a sonar distinta llena.

La absorción de cada material se expresa con su coeficiente de absorción (α), la fracción de la
energía que incide sobre él y no se refleja: de 0 (lo refleja todo) a 1 (lo absorbe todo). Depende
de la frecuencia, y los materiales finos absorben agudos y dejan pasar los graves (se vio en
«Ondas»).

### Los modos propios y las ondas estacionarias

Las superficies que favorecen en mayor medida la producción de ondas estacionarias en una sala
son las paralelas.

Qué es una onda estacionaria: cuando una onda rebota entre dos superficies enfrentadas y la
distancia entre ellas es un múltiplo de media longitud de onda, la onda que va y la que vuelve se
suman siempre en los mismos puntos. El resultado es un patrón fijo de máximos y mínimos que no se
mueve: hay sitios de la sala donde esa frecuencia suena mucho más y sitios donde casi no
suena.

Por qué las paralelas son las culpables: porque el rebote vuelve exactamente por donde vino.
Basta con inclinar una de las dos paredes unos grados para que la energía se disperse y el modo se
deshaga, y ésa es la razón de que los estudios de grabación tengan paredes y techos que no son
paralelos.

Las tres consecuencias de oficio, que es lo que hace útil la respuesta:

1. Los modos son un problema de GRAVES. A frecuencias altas la longitud de onda es tan pequeña
   que los modos se solapan y desaparecen como fenómeno audible. Los que se oyen son los de las
   primeras decenas de hercios.
2. Cuanto más pequeña y más cúbica es la sala, peores modos tiene. Una habitación con las tres
   dimensiones parecidas concentra sus modos en las mismas frecuencias.
3. No se corrigen ecualizando. Un mínimo de presión no se arregla subiendo esa banda: en ese
   punto la onda se cancela, y subir el nivel sólo satura el resto de la sala. Se corrige con
   trampas de graves, con la geometría o moviendo la escucha.

Un cálculo con la regla de la media longitud de onda: entre dos paredes paralelas a 3,4 m, el
primer modo cae donde media longitud de onda mide 3,4 m, es decir, una onda de 6,8 m: 340 / 6,8 =
50 Hz; y siguen sus múltiplos, 100, 150 Hz… (cálculo con la cifra de oficio de 340 m/s).

### La sala para la palabra frente a la sala para la música

| | Palabra —teatro, conferencia— | Música —concierto— |
|---|---|---|
| Qué se busca | INTELIGIBILIDAD | Envolvente y cuerpo |
| RT60 | Corto | Largo |
| Primeras reflexiones | Cuantas más y más pronto, mejor: refuerzan la voz | Se buscan LATERALES, que son las que dan sensación de anchura |
| Qué la arruina | El eco y la cola larga | Una sala demasiado seca, que deja la música desnuda |
| Cómo se mide | Índice de transmisión de la palabra (STI) y porcentaje de consonantes perdidas | Tiempo de reverberación, claridad musical y anchura aparente |

Y la solución de compromiso de las salas polivalentes es mecánica, no electrónica: cortinas,
paneles giratorios y techos móviles que cambian la absorción de la sala según el uso. Un teatro
que hace ópera y congresos cambia físicamente de acústica entre uno y otro.

### Aislar no es acondicionar

Todo lo anterior —reverberación, modos, reflexiones— es acondicionamiento: lo que pasa DENTRO de una
sala. Impedir que el ruido de fuera entre es otra cosa, el aislamiento, y confundirlos es el error
que se paga en un locutorio. La guía de aplicación del Documento Básico de protección frente al ruido
del Código Técnico de la Edificación los separa:

| | Aislamiento acústico | Acondicionamiento acústico |
|---|---|---|
| Qué es | El **«conjunto de procedimientos empleados para reducir o evitar la transmisión de ruidos (tanto aéreos como estructurales) de un recinto a otro o desde el exterior hacia el interior de un recinto o viceversa»** | **«una serie de medidas que se toman para conseguir en un recinto unas condiciones acústicas y un ambiente sonoro interior determinados conforme al uso que se le va a dar al recinto»** |
| Cuántos recintos | **«siempre se tiene en consideración a dos recintos diferentes»** | **«implica a un único recinto, es decir, el sonido es generado y percibido en el mismo recinto»** |
| Con qué se logra | Masa y estanquidad de los cerramientos (abajo) | **«mediante revestimientos de las superficies interiores, reduciendo las componentes reflejadas del sonido»**; va **«vinculado a los tiempos de reverberación»** |

El aislamiento de una pared simple depende, según la guía, **«sobre todo de su masa por unidad de
superficie, su rigidez y el amortiguamiento intrínseco en el material o en los bordes del panel»**; y
de la masa dice: **«Se espera un aumento
en el aislamiento al aumentar la masa, ya que cuanto más pesada es la partición, menos vibra en
respuesta a las ondas sonoras y, por tanto, menos energía radiará hacia el otro lado.»** Es la ley de
masa, con dos consecuencias que se preguntan: **«La ley de masa predice que el aislamiento aumentará
en 6dB al duplicar la masa superficial o la frecuencia (6dB/octava)»**, y **«Todos los materiales
aíslan menos las bajas frecuencias (125 Hz, 250 Hz) que las frecuencias medias (500 Hz, 1000 Hz) y
que las frecuencias altas (2000 Hz, 4000 Hz).»** La propia guía advierte que es una primera
aproximación que **«no explica bien su comportamiento real»**, porque **«sólo se cumple en un cierto
intervalo de frecuencias»**, entre la de resonancia y la crítica o de coincidencia, en las que el
aislamiento cae. En las ventanas de fachada manda la estanquidad: **«La calidad acústica de una carpintería viene fijada principalmente por su
estanquidad al aire»**, y el sellado del marco con la pared es **«otra causa de debilitamiento
acústico»**.

Aplicación práctica: si a un locutorio le entra el tráfico de la calle, forrar las paredes con
espuma fina no sirve —es acondicionamiento, y además los materiales finos no paran los graves (se vio
en «Ondas»)—; tampoco ecualizar ni tocar la ganancia. Lo eficaz es aislar: más masa en los
cerramientos y carpinterías estancas y bien selladas. Los golpes y las vibraciones son un caso aparte: como el
sonido corre más deprisa por los sólidos, la guía indica **«interponer un material aislante elástico
con el objeto de que la energía del impacto se transforme en una deformación elástica del material en
vez de en energía sonora»**.

### Lo que la sala le hace al trabajo del técnico

| Decisión de oficio | Qué manda la acústica |
|---|---|
| Dónde poner el micrófono | Cuanto peor es la sala, más cerca: acercarse aumenta el directo y no la reverberación |
| Qué micrófono elegir | En sala mala, direccional: rechaza lo que viene de los lados y del fondo |
| Cuánta potencia hace falta | No la que cubra la sala, sino la que gane al ruido de fondo medido con las curvas NC |
| Dónde poner los altavoces | Lejos de las paredes y apuntando al público, no a las superficies reflectantes |
| Cuánta ganancia admite un directo | La que la sala deje antes de realimentar: es el acoplamiento del tema 10 |

La regla que resume el tema: la sala es parte de la cadena de audio, y es la única parte que no
se puede cambiar por otra. Se trabaja con ella o contra ella, pero no sin ella.

La sonorización de salas —altavoces, cobertura, realimentación— es materia del tema 10.

## Normativa que el tema invoca

| Norma | Qué se toma |
|---|---|
| Real Decreto 2032/2009, de 30 de diciembre, por el que se establecen las unidades legales de medida | Capítulo II, tabla 3: el hercio, unidad de frecuencia, y su nota (d); el pascal, unidad de presión (N/m²). Capítulo IV, apartado 4 y tabla 8: el belio y el decibelio como unidades de magnitudes logarítmicas, adimensionales, aceptadas para su uso con el SI pero no unidades SI; 1 dB = (1/10) B; la nota (i), que obliga a indicar la magnitud y el valor de referencia; el bar, fuera del SI, igual a 100 kPa |

## Lo que este tema no da, y dónde está

- La fisiología de la voz, y la del oído más allá del recorrido de la onda y de la cóclea: sin
  fuente leída; tampoco las frecuencias a las que domina cada pista biaural. La frontera de los 50 ms
  se da como oficio, no como cifra exacta de una fuente.
- La fórmula de la velocidad del sonido en función de la temperatura: el tema da los valores de 0 y
  20 °C y usa para las cuentas la cifra redonda de oficio, 340 m/s.
- La difracción y la distancia crítica por su nombre, y los índices de aislamiento del Código
  Técnico de la Edificación y sus exigencias: fuera de este tema.
- La fórmula de Sabine con su constante numérica y la medición normalizada del tiempo de
  reverberación: no se han leído en fuente; el tema da sólo la relación cualitativa (volumen y
  absorción) y valores de RT60 orientativos.
- El goniómetro o vectorscopio: sin fuente leída; el tema da sólo el correlador de fase.
- Los niveles eléctricos (dBu, dBV), las impedancias y la masa, en el tema 2; la polaridad de los
  micrófonos y sus patrones, en el tema 3; la ecualización, los filtros y los procesadores de
  dinámica, en el tema 5; la sonorización y la realimentación, en el tema 10; el conexionado, en el
  tema 11; la sonoridad, los medidores de pico y la correlación de fase como control de calidad, en
  el tema 13; la compatibilidad mono y el *downmix*, en el tema 14; el ruido como riesgo laboral, en
  el tema 16.
- Lo propio de CSRTV (salas, estudios, locutorios y su acústica): no consta en un documento
  publicado localizado.

## Trazabilidad

Fuentes leídas el 25/09/2026 (las añadidas en el remate, también ese día). La norma, en el texto consolidado del BOE vigente ese día.

| Fuente | Qué sostiene |
|---|---|
| Real Decreto 2032/2009, de 30 de diciembre (BOE núm. 18, de 21/01/2010), texto consolidado: capítulo II en la redacción publicada el 29/04/2020, vigente desde el 30/04/2020; capítulo IV en la redacción original, vigente desde el 22/03/2010 | Hercio y su nota (d); pascal = N/m²; decibelio, belio y neper como unidades adimensionales aceptadas con el SI; 1 dB = (1/10) B; nota (i) sobre magnitud y valor de referencia; bar = 100 kPa |
| DPA Microphones, *Mic University*, E. Bøgh Brixen, «Polarity, phase and delay» | Definición de fase; desfase por retardo y sus causas; ángulo ±180°; fase y tiempo a 1 y 2 kHz; el oído poco sensible a la fase; ecualizadores y desfase; polaridad frente a fase; el botón φ/Ø; patilla 2 en fase con la presión |
| DPA Microphones, *Mic University*, E. Bøgh Brixen, «The basics about comb filtering (and how to avoid it)» | Definición de filtro en peine, de menos de 1 ms a unos 25 ms; sus dos orígenes; niveles dentro de 10 dB; el caso de tertulia; atenuar al menos 10 dB; regla 3:1 y 4,5:1; micrófono de capa límite |
| DPA Microphones, citado en el tema 6 del específico de Cámara Operador | Caída de 6 dB por duplicar la distancia en una fuente puntual |
| Rane, RaneNote 155, «Dynamics Processors — Technology & Applications», R. Jeffs, S. Holden y D. Bohn, septiembre de 2005 | Definición de rango dinámico; +26 dBu, −94 dBu y 120 dB del equipo profesional y del oído (cifras del fabricante) |
| RTW, «Focus: The Multi Correlator», T. Valter, 9/08/2019 | Uso del correlador de fase; escala −1, 0, +1; valores de 0,3 a 0,7 en mezclas estéreo normales (cifra del fabricante) |
| OpenStax, *University Physics Volume 1* (manual universitario de acceso abierto, Rice University), apartados 17.2 «Sound Waves» y 17.3 «Speed of Sound», en la edición de LibreTexts | Onda longitudinal en el aire y en los fluidos; compresiones y enrarecimientos; transversal y longitudinal en sólidos; 331 m/s a 0 °C y 343 m/s a 20 °C; mayor velocidad en líquidos y sólidos; tabla «Speed of Sound in Various Media» (aire, agua dulce, agua de mar, acero, caucho vulcanizado) |
| OpenStax, *Psychology 2e*, R. M. Spielman, W. J. Jenkins y M. D. Lovett, 2020, apartado 5.4 «Hearing» | Células ciliadas e impulsos por el nervio auditivo; pistas monoaurales y biaurales; diferencias interaurales de nivel y de tiempo |
| UNSW (University of New South Wales), School of Physics, Physclips, «Timbre and envelope» | El timbre depende de la envolvente y del espectro; ataque, caída, sostenimiento y extinción; los transitorios de arranque; la clave al revés |
| B. Shinn-Cunningham, «Auditory Precedence Effect», *Encyclopedia of Computational Neuroscience*, Springer, 2013 (DOI 10.1007/978-1-4614-7320-6_101-5) | Definición del efecto de precedencia; sinónimo «Law of the first wavefront»; 1–5 ms con chasquidos y decenas de ms con voz o música |
| Consejo Interterritorial del Sistema Nacional de Salud, «Protocolo para la vigilancia sanitaria específica de las personas trabajadoras expuestas a ruido» (Sanidad, 2022), apartado 2.1.3 «Recuerdo fisiológico» y 2.1.4 | Recorrido de la onda por el oído externo, medio e interno; tonotopía de la cóclea; células de los agudos junto a la ventana oval y frecuencias de 3.000 y 6.000 Hz |
| Guía de aplicación del DB HR Protección frente al ruido (Código Técnico de la Edificación), anejo 1 «Conceptos previos» | 344 m/s y dependencia de presión y temperatura; sólidos más rápidos, ladrillo unas 9 veces; aislamiento frente a acondicionamiento; masa, rigidez y amortiguamiento de la pared simple; ley de masa y su intervalo de validez (+6 dB al duplicar masa o frecuencia; menos aislamiento en graves); estanquidad de la carpintería; material elástico contra el ruido de impactos |

Oficio sin norma detrás, y así se declara: la onda de presión y sus magnitudes; el nombre de
efecto Haas; que el panorama y la microfonía estéreo trabajen con las mismas diferencias de nivel y
de tiempo; que una puerta o un compresor cambien el timbre al tocar los ataques; la relación entre
velocidad, frecuencia y longitud de onda y la cifra de 340 m/s; graves largos y agudos cortos; el
margen audible de 20 Hz a 20 kHz y sus zonas; los ruidos blanco, rosa y marrón; los umbrales de 20
µPa y unos 20 Pa; las referencias de dB SPL, dBu, dBV, dBFS y dBm; la doble fórmula del decibelio;
la suma de fuentes correladas y no correladas; que la caída de 6 dB por distancia doble sólo valga en campo libre; las tres cualidades del sonido y los armónicos; las
curvas isofónicas, el fon, la banda de 2 a 5 kHz y la ponderación A; las curvas NC y NR; el
enmascaramiento; el margen dinámico de un equipo y el del oído; el *headroom*; el sonido directo,
las primeras reflexiones y la cola; la frontera de los 50 ms; el RT60 y sus valores orientativos;
Sabine en forma cualitativa; el coeficiente de absorción; los modos y las ondas estacionarias; la
sala para la palabra frente a la sala para la música; las decisiones de colocación. Es cálculo, y se
puede rehacer: las proporciones de velocidad agua/aire y acero/aire; las longitudes de onda y los periodos de la tabla; 20 × log 10⁶ = 120 dB; los 6 dB
por bit y los 96 y 144 dB; las fases de un retardo de 1 ms; los 17 m de 50 ms; el primer modo de 50
Hz entre paredes a 3,4 m.
