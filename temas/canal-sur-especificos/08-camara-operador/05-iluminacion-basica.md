# Tema 5 del específico de Cámara Operador · Iluminación básica para cámara

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico de Cámara Operador · punto 5 |
| **Sirve para** | Puesto 2.8, Cámara Operador (grupo B03), y la prueba práctica del puesto |
| **Fuente** | Sin norma jurídica. Recomendaciones UIT-R BT.709-6 y BT.2020-2 (blanco de referencia D65; frecuencia de trama e iluminación); EBU Tech 3355 (marzo de 2017), índice TLCI. Documentación de fabricante: Sony, *PXW-Z200/HXR-NX800 Help Guide* (5-060-574-13(1), 2024); Blackmagic Design, *URSA Broadcast G2 Installation and Operation Manual* (noviembre de 2021); Canon, *XF605 Instruction Manual* (PUB. DIE-0559-000B); ficha del Astera Titan Tube y su informe de ensayo IEC 62471 (29 de mayo de 2026). Lo demás, oficio y cálculo |
| **Redacción que se estudia** | Las ediciones vigentes el 24/09/2026: BT.709-6, BT.2020-2 y EBU Tech 3355 de 2017 |
| **Extensión** | 7.300 palabras aproximadamente |

<!-- /portada -->

Siglas que usa el tema: Agencia Pública Empresarial de la Radio y Televisión de Andalucía
(**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Sector de Radiocomunicaciones de la
Unión Internacional de Telecomunicaciones (**UIT-R**); Unión Europea de Radiodifusión (**EBU**,
*European Broadcasting Union*); Comisión Internacional de la Iluminación (**CIE**); captación
electrónica de noticias (**ENG**, *electronic news gathering*); diodo emisor de luz (**LED**,
*light-emitting diode*); lámpara de haluros metálicos (**HMI**, *hydrargyrum medium-arc iodide*);
filtro de corrección hacia el naranja (**CTO**, *colour temperature orange*) y hacia el azul
(**CTB**, *colour temperature blue*); densidad neutra (**ND**, *neutral density*); índice de
reproducción cromática (**IRC**, en inglés *CRI*, *colour rendering index*, cuyo valor general se
escribe **Ra**); índice de consistencia de la iluminación para televisión (**TLCI**, *television
lighting consistency index*); protocolo de control de luces por multiplexado digital (**DMX**);
pantalla de cristal líquido (**LCD**, *liquid crystal display*) e interfaz digital serie (**SDI**,
*serial digital interface*), que aparecen en una cita de fabricante; kelvin (**K**), unidad de la
temperatura de color; mired (grado micro-recíproco, *micro reciprocal
degree*), unidad de la desviación de color de un filtro; lux (**lx**), lumen (**lm**) y candela
(**cd**); número f (**f**) del diafragma; hercio (**Hz**).

Los rótulos de menú se escriben tal como los imprime el fabricante (***Tint***, ***Flicker
Reduce***, ***ATW***…): son rótulos de la máquina, no siglas.

> **Enunciado del programa** (concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24 de
> septiembre de 2026, anexo V, temario específico del puesto 2.8, punto 5):
>
> Iluminación básica para cámara: temperatura de color, contraste, sombras, luz natural y luz
> artificial.

**Qué se puede preguntar.** No hay exámenes anteriores de este puesto. Por el enunciado, un
tribunal puede preguntar: qué es la temperatura de color y si a más kelvin la luz es más azul o más
roja; qué temperatura tienen el tungsteno de estudio y la luz de día; qué es el blanco D65; cómo se
pasa de kelvin a mired y por qué los filtros se miden en mired; qué hace un CTO y qué hace un CTB;
cómo se corrige la dominante verde; qué mide el TLCI; qué es una relación de contraste, cuántos
pasos son 4:1 u 8:1 y qué luz baja el contraste; de qué depende la dureza de una sombra; dónde van
la luz principal, el relleno y el contraluz; qué son una bandera, un velo o un rebotador; cuánto cae
la luz al doblar la distancia; cómo se resuelve un interior con ventana; por qué parpadea la imagen
con luz de LED o fluorescente. En la prueba práctica: iluminar una entrevista con un equipo ligero,
igualar el color de fuentes mezcladas y exponer contra una ventana.

<!-- indice -->

## Índice

- [Iluminación básica para cámara](#iluminación-básica-para-cámara)
  - [Qué decide la luz](#qué-decide-la-luz)
  - [Las magnitudes de la luz](#las-magnitudes-de-la-luz)
  - [La ley inversa del cuadrado](#la-ley-inversa-del-cuadrado)
  - [El equipo ligero de un operador](#el-equipo-ligero-de-un-operador)
- [Temperatura de color](#temperatura-de-color)
  - [Qué es](#qué-es)
  - [La luz de día y el blanco D65](#la-luz-de-día-y-el-blanco-d65)
  - [El balance de blancos frente a la luz](#el-balance-de-blancos-frente-a-la-luz)
  - [El mired](#el-mired)
  - [Los filtros de conversión: CTO y CTB](#los-filtros-de-conversión-cto-y-ctb)
  - [La dominante verde y la mezcla de fuentes](#la-dominante-verde-y-la-mezcla-de-fuentes)
  - [La fidelidad de color: IRC y TLCI](#la-fidelidad-de-color-irc-y-tlci)
- [Contraste](#contraste)
  - [La relación de contraste](#la-relación-de-contraste)
  - [Medir el contraste en pasos](#medir-el-contraste-en-pasos)
  - [Bajar o subir el contraste](#bajar-o-subir-el-contraste)
  - [El contraste que admite la cámara](#el-contraste-que-admite-la-cámara)
- [Sombras](#sombras)
  - [Luz dura y luz suave](#luz-dura-y-luz-suave)
  - [La dirección de la luz y el esquema de tres puntos](#la-dirección-de-la-luz-y-el-esquema-de-tres-puntos)
  - [Los accesorios que controlan la sombra](#los-accesorios-que-controlan-la-sombra)
  - [La luz por el eje óptico](#la-luz-por-el-eje-óptico)
- [Luz natural](#luz-natural)
  - [En exterior no se ilumina: se corrige](#en-exterior-no-se-ilumina-se-corrige)
  - [La luz natural cambia](#la-luz-natural-cambia)
  - [Interior con ventana](#interior-con-ventana)
- [Luz artificial](#luz-artificial)
  - [Los aparatos](#los-aparatos)
  - [El LED](#el-led)
  - [El regulador y el color](#el-regulador-y-el-color)
  - [El parpadeo](#el-parpadeo)
  - [La seguridad de las fuentes](#la-seguridad-de-las-fuentes)
- [Recomendaciones técnicas que el tema cita](#recomendaciones-técnicas-que-el-tema-cita)
- [Lo que este tema no da, y dónde está](#lo-que-este-tema-no-da-y-dónde-está)
- [Trazabilidad](#trazabilidad)

<!-- /indice -->

## Iluminación básica para cámara

### Qué decide la luz

Iluminar no es hacer que se vea: es decidir cómo se ve. Con la misma cámara, el mismo decorado y
el mismo sujeto, la luz decide cuatro cosas a la vez (oficio):

| Decide | Cómo |
|---|---|
| La exposición | Cuánta luz llega al sensor, y por tanto con qué diafragma se trabaja |
| El modelado | Dónde caen las sombras, y con ellas el volumen del rostro y del decorado |
| La separación | Que el sujeto se despegue del fondo y no se funda con él |
| La atmósfera | El tono: día o noche, cálido o frío, duro o amable |

En un plató de televisión hay una restricción que no existe en el rodaje con una sola cámara: la
luz tiene que servir a todas las cámaras a la vez. No se puede reiluminar para cada tiro, porque los
tiros son simultáneos. De ahí que la iluminación de plató sea más general, más blanda y más frontal
que la de ficción rodada con una cámara. En reportaje ocurre lo contrario: un equipo de cámara lleva
poca luz y tiene que resolver mucho, así que cada aparato del maletín está elegido por su
versatilidad.

### Las magnitudes de la luz

| Magnitud | Qué mide | Unidad |
|---|---|---|
| Flujo luminoso | Toda la luz que emite una fuente | Lumen (lm) |
| Intensidad luminosa | La luz que emite en una dirección | Candela (cd) |
| Iluminancia | La luz que llega a una superficie | Lux (lx) |
| Luminancia | La luz que sale de una superficie hacia el ojo o la cámara | Candela por metro cuadrado |

La distinción entre iluminancia y luminancia es la que más se confunde: la primera es la luz que
cae sobre el sujeto, y se mide con el fotómetro en el sitio del sujeto apuntando a la cámara (luz
incidente); la segunda es la luz que el sujeto devuelve, y se mide apuntando al sujeto (luz
reflejada). La cámara ve luminancias: una camisa blanca y una chaqueta negra bajo la misma
iluminancia dan luminancias muy distintas.

Las fichas de los aparatos dan el flujo: el Astera Titan Tube, por ejemplo, declara «**1340 lm**»,
«**2900 lm**» y «**5800 lm**» según su longitud, como «**Typical values**».

### La ley inversa del cuadrado

La iluminancia que llega a una superficie disminuye con el cuadrado de la distancia a la fuente. La
luz que sale de un punto se reparte sobre una esfera, y la superficie de una esfera crece con el
cuadrado de su radio: al doblar la distancia, la misma luz se reparte sobre cuatro veces más
superficie, así que a cada trozo le llega la cuarta parte (cálculo; vale para fuentes pequeñas
respecto de la distancia).

| Si la distancia se… | La iluminancia queda en… | En pasos de diafragma | Para compensar hay que… |
|---|---|---|---|
| Duplica (×2) | Un cuarto | 2 pasos menos | Cuadruplicar la intensidad |
| Triplica (×3) | Un noveno | Algo más de 3 pasos menos | Multiplicar por nueve |
| Reduce a la mitad (÷2) | El cuádruple | 2 pasos más | Dividir por cuatro |

La consecuencia práctica: un sujeto que se aleja un metro de una luz cercana pierde muchísima luz;
el mismo metro, alejándose de una luz lejana, casi no cambia nada. Por eso la luz cercana castiga el
movimiento del sujeto y la lejana perdona, y por eso un fondo alejado del sujeto queda más oscuro que
él con la misma luz (oficio).

### El equipo ligero de un operador

| Aparato | Qué es | Para qué |
|---|---|---|
| Panel de diodos (LED) | Superficie de emisores, a menudo con temperatura de color ajustable | La luz principal de una entrevista: suave y de bajo consumo |
| Foco de cámara | Pequeño, en la zapata | Relleno de urgencia |
| Fresnel ligero | Lente escalonada, haz controlable | Recorte y contraluz |
| Foco abierto | Sin lente | Mucha luz por poco peso |
| Reflector o rebote | Superficie que devuelve luz | Rellenar sin enchufar nada |
| Difusores y sedas | Delante de la fuente | Suavizar la sombra |
| Banderas y recortadores | Delante de la fuente | Quitar luz de donde no se quiere |
| Filtros de color | Delante de la fuente | Corregir o alterar la temperatura de color |

Las cámaras de reportaje admiten una luz en la zapata que la propia cámara gobierna. La Sony
PXW-Z200 lista entre sus accesorios la «**HVL-LBPC Video Light**» y permite encenderla con la
cámara o con la grabación: «**[Power Link]: Turns the video light on/off when the unit is turned
on/off.**», «**[Rec Link]: Turns the video light on/off when the unit starts/stops recording.**». En
la grabación por intervalos la enciende antes de grabar, «**which allows you to record pictures
under stable light and color temperature conditions (pre-lighting function)**».

Las dos decisiones que gobiernan todo lo demás (oficio):

1. Dura o difusa. Una fuente pequeña respecto del sujeto da sombra dura y de borde definido; una
   fuente grande, sombra suave. Difundir agranda la fuente y suaviza la sombra, y a cambio quita
   luz (epígrafe «Sombras»).
2. Corregir o no corregir. Si hay dos temperaturas de color en la escena, hay que igualarlas o
   elegir cuál manda (epígrafe «Temperatura de color»).

## Temperatura de color

### Qué es

La temperatura de color es la temperatura a la que habría que calentar un cuerpo negro (un emisor
ideal) para que emitiese luz del mismo tono que la fuente que se describe. Se mide en kelvin, y su
escala tiene una particularidad que descoloca: a más kelvin, más azul; a menos kelvin, más rojiza la
luz.

| Fuente | Temperatura de color aproximada | Tono |
|---|---|---|
| Llama de vela | 1.800 K | Muy cálido |
| Lámpara doméstica incandescente | 2.700 K | Cálido |
| Lámpara de estudio de tungsteno-halógeno | 3.200 K | Cálido: el patrón de interior |
| Amanecer y atardecer | 3.000 – 4.000 K | Cálido |
| Fluorescente de blanco frío | 4.000 K | Neutro |
| Luz de día fotográfica | 5.500 K | Neutro-frío: el patrón de exterior |
| HMI y LED de luz día | 5.600 K | Neutro-frío |
| Blanco de referencia D65 de televisión | 6.500 K | Frío |
| Cielo cubierto | 6.500 – 7.500 K | Azulado |
| Sombra a cielo abierto | 8.000 – 10.000 K | Muy azulado |

Las cifras son aproximadas y así se declaran (oficio): una lámpara de estudio se especifica en
3.200 K y un HMI o un LED de día en 5.600 K, pero una vela, una bombilla doméstica o un cielo
cubierto no tienen una cifra única; dependen del ejemplar, de la hora y del tiempo. Lo que la tabla
sostiene sin margen de duda es el orden y los dos patrones del oficio: 3.200 K y 5.500-5.600 K.
Toda la práctica consiste en llevar las fuentes de una escena a uno de los dos, o a un tercero
elegido, para que el balance de blancos de la cámara tenga una sola referencia.

La consecuencia en cámara: una cámara equilibrada para tungsteno que graba a la luz del día da una
imagen azulada, y una equilibrada para día bajo tungsteno da una imagen anaranjada. El balance de
blancos (tema 1) es la corrección electrónica de esa diferencia; los filtros de conversión son su
remedio óptico, en la fuente o en la cámara.

### La luz de día y el blanco D65

Hay dos cifras de «blanco de día», de dos mundos distintos, y las dos son verdad en el suyo:

- 5.500-5.600 K es la luz de día de la fotografía y de la luminotecnia: el patrón al que se
  equilibran los focos de haluros metálicos y los LED de día. Los preajustes de las cámaras usan esta
  referencia: la Canon XF605 trae «**daylight, 5,600 K**» y «**tungsten lamp, 3,200 K**», con la
  advertencia de que «**Color temperatures are approximate and given only as a reference.**»; la
  Sony PXW-Z200 ofrece en modo estándar «**[→3200K]**», «**[→4300K]**», «**[→5600K]**» y
  «**[→6300K]**».
- 6.500 K es el blanco de referencia de la televisión, el iluminante D65 de la CIE. No es una luz
  que se ponga en un plató: es el blanco de la pantalla y de la señal. La Recomendación UIT-R
  BT.709-6 lo fija con sus coordenadas de cromaticidad, «**Cromaticidad supuesta para señales
  primarias iguales (Blanco de referencia) D65**», **x = 0,3127** e **y = 0,3290**, y la BT.2020-2
  repite las mismas: «**Blanco de referencia (D65)**», **0,3127** y **0,3290**.

Si una pregunta habla de iluminar, la luz de día son 5.500-5.600 K; si habla del blanco de la señal
o del monitor, es D65.

### El balance de blancos frente a la luz

El balance de blancos no cambia la luz de la escena: ajusta la cámara a ella. La cámara admite
temperaturas muy por fuera de los patrones —«**2000K to 15000K**» en la Sony PXW-Z200 y
«**color temperature setting (2,000 K to 15,000 K)**» en la Canon XF605—, pero sólo puede
equilibrar una temperatura a la vez. Cuando en el mismo cuadro hay dos fuentes de distinta
temperatura, el balance deja bien una y mal la otra: por eso la mezcla se corrige en la luz, no en
la cámara (oficio).

Además del eje cálido-frío, el balance tiene un segundo eje, verde-magenta. La Z200 lo ajusta con
el parámetro ***Tint***: «**You can also adjust the color temperature using [Shooting] – [White] –
[Tint] in the full menu.**», con un recorrido de «**−99 to +99**» guardado en cada memoria de
balance: «**Sets the white balance [Tint] value saved in memory A.**» Es el mando que corrige en
cámara la dominante verde de algunas fuentes (más abajo, «La dominante verde»).

### El mired

La desviación de color que produce un filtro corrector de la temperatura de color se mide en mired,
nombre que viene de *micro reciprocal degree*, grado micro-recíproco:

Valor en mired = 1.000.000 / temperatura de color en kelvin.

Por qué no se usan kelvin: porque el efecto de un filtro no es una cantidad fija de kelvin. Un
cambio de 100 K es enorme en una fuente de 3.200 K y apenas se nota en una de 10.000 K. El efecto de
un filtro es proporcional a la inversa de la temperatura, y en esa escala inversa un filtro tiene un
valor fijo que se suma o se resta, sea cual sea la fuente (cálculo).

| Temperatura de color | Valor en mired (cálculo) |
|---|---|
| 1.800 K (vela) | 556 |
| 2.700 K | 370 |
| 3.200 K (tungsteno de estudio) | 312,5 |
| 4.000 K | 250 |
| 5.600 K (luz de día) | 178,6 |
| 6.000 K | 166,7 |
| 6.500 K (D65) | 153,8 |
| 10.000 K (sombra) | 100 |

La escala va al revés que la de kelvin: a más kelvin, menos mired. La temperatura más alta es el
número de mired más pequeño.

Dos cuentas que hay que saber hacer:

1. Pasar tungsteno a día: de 3.200 K (312,5 mired) a 5.600 K (178,6 mired) hay un desplazamiento de
   unos −134 mired. El signo negativo es un filtro azul, que sube la temperatura de color.
2. El mismo filtro sobre otra fuente: esos −134 mired aplicados a una luz de 5.600 K la dejan en
   unos 45 mired, que son más de 22.000 K. La cuenta en mired funciona con cualquier fuente; una
   resta en kelvin no funcionaría en ninguno de los dos casos.

La misma lógica aparece en la cámara: en memoria de balance la Z200 se ajusta en pasos de 20 K
hasta 5.600 K, y por encima «**Values above [5600K] can be set at intervals equal to the amount of
color change from [5580K] to [5600K]**»; es decir, por encima de 5.600 K cada paso del mando ya no
son 20 K, sino el salto de kelvin que produce el mismo cambio de color.

### Los filtros de conversión: CTO y CTB

Un gel de color es una lámina translúcida coloreada que se pone delante del foco para cambiar el
color de su luz. Los hay decorativos, de colores saturados, y de conversión, que son los que hacen el
trabajo técnico:

| Gel | Color | Qué hace | Uso típico |
|---|---|---|---|
| CTO | Naranja | Baja la temperatura de color (suma mired) | Llevar luz de día a tungsteno, o dar hora cálida |
| CTB | Azul | Sube la temperatura de color (resta mired) | Llevar tungsteno a luz de día |
| Corrección de verde | Magenta (o verde) | Quita (o añade) la dominante verde | Fuentes con exceso de verde; igualar con fluorescentes |
| Difusión | Blanco lechoso | No cambia el color: suaviza | Ablandar una fuente dura |
| Neutro (ND) | Gris | No cambia el color: quita luz | Bajar una ventana muy brillante |

La dirección es lo que más se equivoca: naranja es cálido, y cálido es menos kelvin. Un filtro azul
hace la luz más azul, así que sube su temperatura de color; un filtro naranja la baja. Un filtro de
conversión cambia el color y además quita luz: ningún filtro añade luz, todo filtro absorbe parte
de la que recibe (oficio). La pérdida concreta de cada gel la da la ficha de su fabricante.

El gel es el dispositivo que se pone delante del foco precisamente para ajustar su temperatura de
color. El regulador de intensidad no lo es, aunque en tungsteno la desplace (epígrafe «Luz
artificial»); el difusor y el reflector no tocan el color.

### La dominante verde y la mezcla de fuentes

Algunas fuentes de descarga y algunos LED no emiten como un cuerpo negro: su luz, además de más o
menos cálida, tira a verde o a magenta. El balance de blancos de la cámara no la corrige del todo si
la mezcla con otras fuentes, porque sólo iguala una. Hay dos remedios (oficio):

- En la fuente: gel magenta en los aparatos que dan verde, o gel verde en los propios para igualarlos
  con los fluorescentes del local cuando no se pueden apagar.
- En la cámara: el eje verde-magenta del balance (***Tint*** en la Z200), válido cuando toda la luz
  de la escena tiene la misma dominante.

La regla con fuentes mezcladas: elegir cuál manda (la que no se puede cambiar: la ventana, los
tubos del techo, el sol) y llevar todas las demás a ella con geles; después, balance de blancos
sobre carta en la luz del sujeto.

### La fidelidad de color: IRC y TLCI

Dos fuentes de la misma temperatura de color pueden reproducir mal los colores si su espectro tiene
huecos. El índice de reproducción cromática (IRC, Ra) lo mide para el ojo; el TLCI, definido por la
EBU en su Tech 3355, lo mide para la cámara de televisión.

Lo que dice la EBU del TLCI (Tech 3355, marzo de 2017):

- El resultado, Qa, se calibró así: «**The formulation for Qa was constrained to produce a value of
  50 for a typical daylight fluorescent tube, and this number appears to represent the watershed
  separating luminaires into those which are correctable for television use, and those which are
  not.**» Es decir, 50 es la frontera entre las fuentes que se pueden corregir para televisión y las
  que no.
- Da dos lecturas del valor según el tipo de trabajo: producción con posproducción («**drama,
  wildlife and any production where significant post-processing is involved**») y «**Live
  multi-camera production [...] such as sport and news where pictures have no post-processing and
  the pictures are required only to be credible**», con la salvedad de que «**these opinions do not
  form hard definitions; there is considerable overlap**».
- Y advierte de que la cifra no tiene un sentido absoluto: «**Neither the CRI nor the original work
  of Sproson and Taylor on the TLCI give any meaning to the computed value for Ra or Qa.**»

Cómo lo publica un fabricante: la ficha del Astera Titan Tube da «**CRI(Ra)/TLCI 3200-6500k*
≥96**», con la nota «**Typical values**»: un índice igual o superior a 96 en todo el recorrido de
3.200 a 6.500 K. Un LED de estudio no se elige por vatios: se elige también por su fidelidad de
color, que es lo que evita caras verdosas en cámara (oficio).

## Contraste

### La relación de contraste

La relación de contraste de iluminación es la proporción entre la luz de la zona más iluminada y la
de la zona en sombra del sujeto (o entre el sujeto y el fondo). Se escribe como una razón —2:1, 4:1,
8:1— y se mide en pasos de diafragma, porque cada paso duplica o reduce a la mitad la luz. Cuanto
mayor es la razón, más dramática y más dura es la imagen; cuanto menor, más plana y más amable
(oficio).

| Relación de contraste | Pasos de diafragma de diferencia |
|---|---|
| 2:1 | 1 paso |
| 4:1 | 2 pasos |
| 8:1 | 3 pasos |
| 16:1 | 4 pasos |
| 32:1 | 5 pasos |

La regla que convierte una en otra: la relación de contraste es 2 elevado al número de pasos
(cálculo). 16 es dos a la cuarta, así que 16:1 son cuatro pasos.

La escala de números f que hay que tener memorizada para contar pasos: 1 · 1,4 · 2 · 2,8 · 4 · 5,6 ·
8 · 11 · 16 · 22. Cada salto es un paso; más luz es número f más pequeño.

### Medir el contraste en pasos

Un ejemplo resuelto. Se mide la luz que refleja el rostro de una persona y el fotómetro da f/8. Se
quiere que el fondo tenga una relación de 16:1 respecto del rostro. ¿Qué lectura hay que conseguir
en el fondo?

1. 16:1 son cuatro pasos de diafragma de diferencia.
2. El fondo tiene que ser más oscuro que el personaje: cuatro pasos menos de luz.
3. Con una medida de luz reflejada, menos luz en el fondo es una lectura con número f más pequeño:
   f/8 → f/5,6 → f/4 → f/2,8 → f/2.
4. El fondo tiene que medir f/2.

El error frecuente es recorrer la escala en el sentido contrario y contestar f/16, o contar tres
pasos y contestar f/2,8. Una relación de 16:1 es un contraste muy alto: un fondo casi negro con un
rostro bien expuesto.

Con luz incidente la cuenta es la misma: si la luz principal da f/8 y el relleno f/4, la diferencia
son dos pasos y la relación es 4:1 (cálculo).

### Bajar o subir el contraste

Para disminuir el contraste hay que subir la sombra, no bajar la luz. Y la luz que sube la sombra es
la luz de relleno: ésa es su definición (oficio). Las demás van en el sentido contrario o en
ninguno:

| Si se… | El contraste… | Por qué |
|---|---|---|
| Sube el relleno, o se acerca un rebotador | Baja | Aclara la zona de sombra |
| Sube la luz principal | Sube | Es la que crea la sombra |
| Pone una bandera en el lado de sombra, o un reflector negro | Sube | Quita luz de la sombra (relleno negativo) |
| Sube el contraluz | No cambia la razón del rostro | Dibuja el borde; no toca la zona de sombra |

### El contraste que admite la cámara

La razón de contraste no es una preferencia estética suelta: es una decisión técnica que depende de
lo que la cámara y la cadena de señal aguantan. Una escena con más diferencia entre luces y sombras
de la que el sensor y la señal admiten obliga a elegir entre quemar las altas luces o empastar las
sombras; el margen de exposición de la cámara, el *knee* y los límites de la señal se desarrollan en
el tema 1. La herramienta para comprobarlo en cámara es la cebra o el falso color, también del
tema 1.

En plató de informativos o de magacín el contraste se mantiene bajo, del orden de 2:1, porque la
imagen se va a ver en condiciones de visionado que no se controlan; en una entrevista de reportaje
se trabaja de 2:1 a 4:1; en ficción se sube a 8:1 y más. Estas cifras son costumbre de oficio, no
norma.

La cadencia también cuesta luz, y eso cambia la exposición, no el contraste: «**if you switch from
25 to 50 frames per second, the amount of light reaching the sensor will be halved. To maintain your
exposure you need to compensate for this change by opening up your lens an extra stop, by opening up
your shutter angle from 180º to 360º or by adding some extra lighting**» (Blackmagic, URSA Broadcast
G2).

## Sombras

### Luz dura y luz suave

La dureza de una luz no depende de su potencia sino del tamaño aparente de la fuente vista desde el
sujeto: cuanto más grande se ve la fuente, más suave es la luz (oficio).

| | Luz dura | Luz suave |
|---|---|---|
| Fuente | Pequeña respecto del sujeto | Grande respecto del sujeto |
| Sombras | Recortadas, con borde nítido | Difusas, con transición larga |
| Modelado | Marcado, con textura de piel visible | Suave, favorecedor |
| Aparatos | Foco de lente, foco abierto, sol directo | Difusor grande, panel, rebote, cielo cubierto |

El tamaño aparente depende también de la distancia: la misma fuente es más suave cerca del sujeto
que lejos, porque cerca se ve más grande. El sol, enorme pero lejanísimo, da una luz dura; el cielo
cubierto, que convierte todo el cielo en fuente, da la luz más suave que existe.

Dos maneras de ablandar una fuente dura: ponerle difusión delante, que agranda la superficie
emisora, o rebotarla contra una superficie blanca, que convierte la superficie en la fuente. Las dos
hacen lo mismo, agrandar el emisor, y las dos quitan luz, que es el precio.

### La dirección de la luz y el esquema de tres puntos

La iluminación de un sujeto se construye con tres luces, y cada una tiene un nombre, una posición y
un cometido (oficio):

| Luz | Dónde va | Qué hace |
|---|---|---|
| Luz principal o llave (*key light*) | Frontal y cruzada, a unos 30-45° del eje de cámara y algo elevada | Es la luz predominante: define la exposición y dónde caen las sombras |
| Luz de relleno (*fill light*) | Al otro lado del eje, más baja de nivel y más suave | Aclara las sombras que deja la principal |
| Contraluz (*back light*) | Detrás del sujeto, apuntando hacia él, elevada | Dibuja el contorno y separa al sujeto del fondo |

«Frontal y cruzada» significa que viene de delante pero no del eje de la cámara: si viniera del eje
aplastaría el rostro y no habría modelado. El contraluz va dirigido hacia el sujeto desde detrás; la
luz de fondo o de decorado, en cambio, va dirigida al decorado. Al esquema se le añaden, según el
trabajo, la luz de fondo, que separa por detrás; la luz de ojos (*eye light*), un aparato pequeño
junto a la cámara que devuelve el brillo a la mirada; y las luces de efecto, que dibujan una
ventana, una farola o una llama.

La posición de la principal decide las sombras que ve la cámara (oficio):

- Cenital (desde arriba): ojos hundidos en sombra; es la luz del sol a mediodía y de los techos de
  oficina.
- Desde abajo: sombras invertidas, inquietantes; se evita salvo como efecto.
- Lateral a 90°: medio rostro en sombra, máximo modelado y máxima textura.
- En el eje de cámara: sin sombras visibles y sin volumen; es la luz del foco de zapata.

En una entrevista, la principal suele ir del lado hacia el que mira el entrevistado: así la mitad
del rostro más próxima a la cámara queda en sombra suave y el rostro gana volumen. La sombra del
sujeto sobre la pared se evita separándolo del fondo y elevando la principal: la sombra cae más
abajo y más lejos, fuera de cuadro (oficio).

### Los accesorios que controlan la sombra

La mitad del trabajo de iluminación es quitar luz de donde no se quiere (oficio):

| Accesorio | Qué es | Qué hace |
|---|---|---|
| Bandera | Bastidor de alambre cubierto de tela negra | Corta la luz: crea sombra, evita que entre en el objetivo |
| Velo o seda (*silk*) | Bastidor cubierto de tela translúcida blanca | Difunde: ablanda la luz que lo atraviesa |
| Rejilla o *net* | Bastidor cubierto de malla | Baja la intensidad sin cambiar la dureza |
| Pulmón o *butterfly* | Bastidor grande de suspensión, con tela intercambiable | Difunde o corta sobre un área amplia, en exterior |
| Viseras (*barn doors*) | Cuatro aletas metálicas en la boca del foco | Recortan el haz groseramente |
| Cortadores (*cutters*) | Banderas estrechas y alargadas | Cortan franjas |
| Rebotador | Superficie blanca, plateada o dorada | Devuelve luz como relleno |
| Ceferino | Brazo articulado de dos o tres tramos con rótulas y mordaza | Sujeta un foco pequeño, una bandera o un difusor donde no hay dónde ponerlo |

Lo que decide entre bandera, velo y rejilla es el material tensado: negro y opaco es bandera;
blanco y translúcido, velo; de malla, rejilla. El nombre de «ceferino» es de oficio español y no
está normalizado: el mismo aparato se llama brazo articulado o *magic arm*.

El aviso de prevención: un brazo articulado sostiene poco peso y en voladizo; lo que cuelga de él va
además asegurado con un cable de seguridad, y el pie que lo aguanta va lastrado con un saco de arena
(oficio; la prevención del puesto, en el tema 14).

### La luz por el eje óptico

Cuando no se quiere ninguna sombra —reproducir un documento o una obra plana, donde cualquier
sombra o reflejo estropea la copia—, se envía la luz a lo largo del eje óptico de la cámara: un
cristal semirreflectante a 45° delante del objetivo, a través del cual mira la cámara, refleja hacia
el sujeto una fuente situada a un lado. La luz sale exactamente desde donde está la cámara, y las
sombras quedan detrás de lo que las produce, donde la cámara no las ve. Es el montaje que en oficio
se llama «fantasma de Pepper», por el truco escénico del siglo XIX que usaba el mismo cristal
inclinado; el teleprónter es el mismo montaje con un texto en lugar de una fuente de luz (oficio).

## Luz natural

### En exterior no se ilumina: se corrige

| | Interior controlado | Exterior |
|---|---|---|
| Fuente dominante | Los aparatos: todo se controla | El sol y el cielo, que no se controlan |
| Problema principal | Que la luz sirva a todas las cámaras y no entre en el objetivo | Que la luz cambie durante la jornada |
| Temperatura de color | La que se elija, normalmente 3.200 K o 5.600 K | La del sol y el cielo, variable |
| Herramienta clave | El foco y su soporte | El rebotador, la difusión grande y el HMI para rellenar |
| Continuidad | Se mantiene sola | Se pierde: hay que rodar los contraplanos deprisa |

En exterior la luz principal ya está puesta: es el sol. El trabajo consiste en rellenar la sombra
con un rebotador o con un HMI, difundir el sol duro con un pulmón y cortar lo que sobra con banderas
(oficio). El HMI es el aparato de exterior porque da luz de día con potencia suficiente para
competir con el sol; un LED de día cumple el mismo papel a menor distancia.

Las decisiones de oficio con sol directo:

- Poner el sol detrás o de lado del sujeto, como contraluz, y rellenar el rostro con un rebotador:
  evita que entorne los ojos y que la sombra de la nariz y de las cejas le marque la cara.
- Si no se puede mover al sujeto, buscar una sombra abierta (luz de cielo, suave y más azulada) y
  rehacer el balance de blancos, o difundir el sol con un pulmón.
- Con mucha luz, el diafragma se cierra y aparece la difracción; se baja la luz con el filtro de
  densidad neutra de la cámara (tema 1), no cerrando el diafragma.

### La luz natural cambia

La luz de día no tiene una temperatura fija: va de unos 3.000-4.000 K al amanecer y al atardecer a
unos 10.000 K en una sombra a cielo abierto (tabla del epígrafe «Qué es»). Cambia también de
dirección y de dureza con la hora y con las nubes. Consecuencias en cámara (oficio):

- El balance de blancos se rehace cuando cambia la luz, no se deja en automático continuo si la
  pieza se va a montar (tema 1).
- Con cielo variable, la exposición también cambia: el fabricante aconseja bajar el umbral de la
  cebra, «**If you’re shooting in variable light such as outdoors on a partly overcast day, setting
  your zebra level lower than 100 can warn you of potential overexposure.**» (Blackmagic, URSA
  Broadcast G2).
- Un plano y su contraplano rodados con dos horas de diferencia tienen el sol en sitios distintos.
  Es un problema de continuidad de iluminación, y se resuelve con el orden de rodaje, no con
  aparatos.

### Interior con ventana

Un interior con una ventana por la que entra luz de día y focos de tungsteno dentro tiene dos
problemas a la vez, y hay que separarlos (oficio):

| Problema | En qué consiste | Remedio |
|---|---|---|
| De color | La ventana da unos 5.600 K y los focos 3.200 K: dos temperaturas en el mismo cuadro | Filtros de conversión: azul (CTB) en los focos, o naranja (CTO) en la ventana |
| De intensidad | La ventana da mucha más luz que los focos: el exterior sale quemado o el interior sale negro | Filtro de densidad neutra en la ventana |

Por qué la intensidad se corrige en la ventana y no en los focos: el problema es que la ventana da
demasiada luz, y no se puede subir la de los focos indefinidamente —no hay potencia, ni enchufes, ni
tiempo—, así que hay que bajar la de la ventana. Y para bajar luz sin tocar el color se usa densidad
neutra.

Los remedios que parecen de intensidad y son de color: un CTB en los focos corrige su color, no
iguala su intensidad; un CTO en los focos los alejaría aún más de la ventana; un CTB en la ventana
enfriaría una luz que ya es azulada y la alejaría del tungsteno.

El remedio completo: densidad neutra en la ventana para la intensidad y, según se quiera unificar
hacia día o hacia tungsteno, naranja en la ventana o azul en los focos. Los filtros comerciales de
ventana pueden combinar las dos correcciones en una sola lámina. Si no hay filtros, las salidas de
reportaje son otras (oficio): usar focos LED de día, que ya igualan el color; encuadrar sin la
ventana o con ella de lado; o exponer para la ventana y dejar al sujeto en silueta cuando la pieza
lo admite (por ejemplo, para ocultar su identidad).

## Luz artificial

### Los aparatos

| Aparato | Cómo funciona | Luz que da |
|---|---|---|
| Fresnel | Lámpara y reflector montados en un mismo bloque que se acerca o se aleja de la lente escalonada, y así se abre (*flood*) o se cierra (*spot*) el haz | Dura y controlable; el aparato clásico de plató |
| Foco abierto (*open face*) | Lámpara y reflector sin lente | Dura, más luz por vatio, menos controlable |
| Recortador (elipsoidal) | Lente y cuchillas internas que recortan la forma del haz | Muy dura, con borde dibujable |
| Panel de LED | Matriz de diodos, a menudo de temperatura ajustable | Suave; cambia de blanco sin gel |
| Tubo de LED | Barra de diodos, a menudo con batería y control inalámbrico | Suave, para rincones y efectos |
| *Softbox* | Caja de tela con difusor frontal sobre una fuente | Suave por construcción |
| Fluorescente de estudio | Tubos de alta frecuencia en batería | Suave, poco calor |
| HMI | Descarga de haluros metálicos: mucha potencia con luz de día | Dura o suave según accesorio; el aparato de exterior |

HMI y LED nombran el tipo de fuente, no el mecanismo: hay fresneles con lámpara HMI y con LED.

### El LED

Los LED son hoy el aparato dominante en reportaje y en plató: poco consumo, poco calor, batería y
temperatura de color ajustable sin geles. El Astera Titan Tube, por ejemplo, se describe como un
tubo que «**emits powerful, tunable whites with ultra-high color rendering as well as colored light
which can be applied to individual pixels or the whole tube**», con motor «**RGBMintAmber**»,
batería interna y control por aplicación y por DMX con o sin cable. Lo que hay que comprobar en un
LED antes de usarlo con cámara es su fidelidad de color (IRC y TLCI, epígrafe «La fidelidad de
color») y que no parpadee con la obturación elegida (más abajo).

### El regulador y el color

Bajar la intensidad no es lo mismo en todas las fuentes (oficio):

- En tungsteno, bajar el regulador enrojece la luz, porque el filamento se enfría: la temperatura de
  color baja. Es un efecto colateral indeseado, el motivo por el que en televisión se evita regular
  por debajo de cierto punto, y no una manera de ajustar la temperatura de color.
- En LED, el regulador baja la intensidad sin mover el color.
- En un foco que no se puede regular, la intensidad se baja con distancia (ley inversa del cuadrado),
  con rejilla, con difusión o con densidad neutra.

### El parpadeo

Muchas fuentes artificiales no emiten de forma continua: su luz varía con la frecuencia de la red o
del circuito que las alimenta. La cámara lo registra como parpadeo o como cambios de color. Lo avisa
el fabricante: «**If shooting under lighting produced by fluorescent lights, sodium lamps,
mercury-vapor lamps, or LEDs, the screen may flicker or colors may vary.**» (Sony, PXW-Z200 Help
Guide); «**Artificial light sources such as tungsten, fluorescent and LED may introduce some flicker
to your images.**» (Blackmagic, URSA Broadcast G2).

Tres cosas que hay que saber:

1. Puede no verse en el visor: «**You may not see these flicker issues when previewing the scene on
   your LCD and SDI feed or while recording, so it’s important to perform a test shoot with the
   lights you plan to use**» (Blackmagic).
2. Depende de la obturación: «**Your shutter setting can also affect the visibility of flicker when
   shooting under lights**» (Blackmagic). En Europa la red es de 50 Hz, y la obturación a 1/50 o
   1/100 es la que evita el parpadeo de la iluminación de red (oficio; tema 1).
3. La cámara puede corregirlo: la Z200 trae ***Flicker Reduce***, con modo «**[Auto] / [On] /
   [Off]**» y la frecuencia «**of the power source supplying the lighting that is causing the
   flicker**», «**[50Hz] / [60Hz]**».

La propia elección de la frecuencia de trama del sistema de televisión tiene en cuenta la luz: «**La
elección de la frecuencia de trama puede estar influida por la frecuencia de la alimentación
eléctrica y el tipo de iluminación utilizada**» (Recomendación UIT-R BT.2020-2).

### La seguridad de las fuentes

Una fuente de luz puede ser un riesgo para la vista y la piel, y su seguridad fotobiológica se
acredita por ensayo según la norma «**IEC 62471:2006 and EN 62471:2008**»,
«**Photobiological safety of lamps and lamp systems**». El informe publicado para el Astera Titan Tube (29 de mayo de 2026)
clasifica la lámpara en el «**Exempt Group**», el grupo exento de riesgo. El resto de riesgos
—calor de las lámparas de tungsteno y HMI, caídas de pies y brazos, cables y electricidad en
exteriores— es oficio de prevención y se trata en los temas 11 y 14.

## Recomendaciones técnicas que el tema cita

| Documento | Qué se toma |
|---|---|
| Recomendación UIT-R BT.709-6 | Blanco de referencia D65 y sus coordenadas x = 0,3127, y = 0,3290 |
| Recomendación UIT-R BT.2020-2 | Las mismas coordenadas de D65; la frecuencia de trama y la iluminación |
| EBU Tech 3355 (marzo de 2017) | El TLCI: el valor 50 como frontera, las dos lecturas por tipo de producción y la salvedad sobre el sentido de la cifra |
| IEC 62471:2006 / EN 62471:2008 | La seguridad fotobiológica de lámparas, por el informe de ensayo de un fabricante |

## Lo que este tema no da, y dónde está

- Qué equipos de iluminación usa CSRTV en reportaje y en plató: no consta en un documento publicado
  localizado. Los ejemplos del tema son aparatos y cámaras del mercado con documentación pública.
- Los umbrales por tramos del TLCI (qué valor se considera aceptable para cada tipo de producción):
  están en una figura de la EBU Tech 3355 que no pudo leerse como texto. El tema da sólo el valor 50
  y las dos lecturas.
- La pérdida de luz y el desplazamiento en mired de cada gel comercial (CTO, CTB y sus fracciones):
  están en las cartas de los fabricantes de filtros, que no pudieron leerse. El tema da el cálculo
  del desplazamiento, no la referencia comercial.
- Las cifras de contraste por género (2:1 en informativos, 2:1-4:1 en entrevista, 8:1 en ficción)
  y el ángulo de la luz principal (30-45°): son costumbre de oficio, sin norma que las fije.
- El balance de blancos, la cebra, el falso color, la obturación y el filtro ND de la cámara, en el
  tema 1; la calidad técnica de la imagen, en el tema 9; la prevención de riesgos con focos, pies,
  cables y electricidad, en los temas 11, 14 y 17.
- Los aparatos de plató (parrillas, cicloramas, mesas de control de iluminación) y el diseño de
  iluminación por género son materia del iluminador, no de este enunciado.

## Trazabilidad

Todas las fuentes se leyeron el 24/09/2026.

| Fuente | Qué sostiene |
|---|---|
| Recomendación UIT-R BT.709-6 (edición en español) | Blanco de referencia D65, x = 0,3127 e y = 0,3290 |
| Recomendación UIT-R BT.2020-2 (edición en español) | D65 con las mismas coordenadas; frecuencia de trama, alimentación eléctrica e iluminación |
| EBU Tech 3355, *Method for the assessment of the colorimetric properties of luminaires* (TLCI-2012 y TLMF-2013), marzo de 2017 | Valor 50 como frontera de corrección; dos lecturas por tipo de producción; sin sentido absoluto de Ra y Qa |
| Sony, *PXW-Z200/HXR-NX800 Help Guide*, 5-060-574-13(1), 2024 | Luz de zapata HVL-LBPC y su encendido; preajustes de balance; recorrido 2.000-15.000 K; ***Tint***; pasos del ajuste de temperatura; parpadeo y ***Flicker Reduce*** |
| Blackmagic Design, *URSA Broadcast G2 Installation and Operation Manual*, noviembre de 2021 | Parpadeo con tungsteno, fluorescente y LED; obturación y parpadeo; cebra con cielo variable; cadencia y luz |
| Canon, *XF605 Instruction Manual*, PUB. DIE-0559-000B (especificaciones) | Preajustes de 5.600 K y 3.200 K; ajuste de 2.000 a 15.000 K |
| Astera, ficha del Titan Tube | Flujo luminoso, IRC y TLCI ≥96 entre 3.200 y 6.500 K, motor RGBMintAmber |
| Informe de ensayo IEC 62471 del Astera Titan Tube (n.º 2602T58190E-SF, 29 de mayo de 2026) | Norma de seguridad fotobiológica y clasificación en el grupo exento |

Oficio sin norma detrás, y así se declara: qué decide la luz; las magnitudes fotométricas y la
distinción entre luz incidente y reflejada; el equipo ligero; la definición de temperatura de color
y la tabla de fuentes; la función de los geles; la regla con fuentes mezcladas; la dureza y el
tamaño aparente; el esquema de tres puntos y las posiciones de la principal; los accesorios de
control; la luz por el eje óptico; el trabajo con sol, la variación de la luz natural y el interior
con ventana; la tabla de aparatos; el regulador y el color. Son cálculo, y se pueden rehacer: la ley
inversa del cuadrado (y su paso a diafragmas), la conversión de kelvin a mired y los desplazamientos
del epígrafe «El mired», y la equivalencia entre relación de contraste y pasos (2 elevado al número
de pasos).
