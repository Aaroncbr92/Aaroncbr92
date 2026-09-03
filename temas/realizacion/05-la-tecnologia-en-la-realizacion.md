# Tema 5 del específico de Realización (Asistencia) · La tecnología en el ámbito de la realización

Las siglas de este tema, presentadas de entrada: la Unión Internacional de Telecomunicaciones
(**UIT**, *ITU* en inglés) y su Sector de Radiocomunicaciones (**UIT-R**); el Instituto Europeo de
Normas de Telecomunicación (**ETSI**, del inglés *European Telecommunications Standards
Institute*); la difusión de vídeo digital (**DVB**, del inglés *digital video broadcasting*) y su
variante terrestre (**DVB-T**) y de segunda generación (**DVB-T2**); la televisión digital terrestre
(**TDT**); la alta definición (**HD**), la ultraalta definición (**UHD**) y el alto rango dinámico
(**HDR**, del inglés *high dynamic range*); la codificación de vídeo de alta eficiencia (**HEVC**,
del inglés *high efficiency video coding*) y la codificación versátil de vídeo (**VVC**, del inglés
*versatile video coding*); la modulación de amplitud en cuadratura (**QAM**, del inglés *quadrature
amplitude modulation*); la multiplexación por división de frecuencias ortogonales (**OFDM**, del
inglés *orthogonal frequency division multiplexing*); la cuantización perceptiva (**PQ**, del inglés
*perceptual quantization*) y el logaritmo híbrido (**HLG**, del inglés *hybrid log-gamma*); la
frecuencia ultraalta (**UHF**, del inglés *ultra high frequency*); la Comisión Internacional de la
Iluminación (**CIE**, del francés *Commission Internationale de l'Éclairage*); el Grupo de Expertos
en Imágenes en Movimiento (**MPEG**, del inglés *Moving Picture Experts Group*); la iniciativa
del cine digital (**DCI**, del inglés *Digital Cinema Initiatives*); la codificación avanzada de
vídeo (**AVC**, del inglés *advanced video coding*); el sistema de codificación de color de la
Academia (**ACES**, del inglés *Academy Color Encoding System*) y su espacio primario **AP0**; la
función de transferencia electroóptica (**EOTF**, del inglés *electro-optical transfer function*) y
sus parientes la optoelectrónica (**OETF**) y la optoóptica (**OOTF**); la Organización
Internacional de Normalización (**ISO**) y la Comisión Electrotécnica Internacional (**CEI**, *IEC*
en inglés); la pantalla de cristal líquido (**LCD**, del inglés *liquid crystal display*); la
modulación por impulsos codificados (**MIC**, *PCM* en inglés); el sistema natural de color
(**NCS**, del inglés *Natural Colour System*); la definición convencional (**SD**, del inglés
*standard definition*); y el espacio de color uniforme (**UCS**, del inglés *uniform chromaticity
scale*).

> Enunciado de la convocatoria (Anexo 2, temario específico de Realización (Asistencia),
> bloque 2, «La tecnología en el ámbito de la realización»): «2.1. Conocimientos básicos de
> televisión. 2.1.1. Colorimetría: Conceptos básicos. Espacio de color. Rango dinámico, resolución
> UHD, 4K, Aparatos de medida. 2.1.2. Monitorización y control de la señal de TV. Sistemas de
> televisión digital: TDT. Modulación, relación de aspecto, compresión. 2.1.3. La televisión digital
> en HD, UHD, 4K y 8K.»

**Este es el bloque más preguntado del examen después del mezclador: treinta y cuatro preguntas de
las doscientas nueve del específico.** Y es el único del temario cuya materia está escrita en normas
publicadas: las Recomendaciones del UIT-R para el color y la señal, y las normas del ETSI para la
difusión terrestre. Aquí no se argumenta desde el oficio; se cita.

<!-- indice -->

## Índice

- [1. La luz y el color](#1-la-luz-y-el-color)
- [2. Cómo se ordena el color: los sistemas de representación](#2-cómo-se-ordena-el-color-los-sistemas-de-representación)
- [3. El espacio de color y su amplitud](#3-el-espacio-de-color-y-su-amplitud)
- [4. De la luz a la señal: luminancia y diferencia de color](#4-de-la-luz-a-la-señal-luminancia-y-diferencia-de-color)
- [5. La digitalización: muestreo, cuantificación y codificación](#5-la-digitalización-muestreo-cuantificación-y-codificación)
- [6. Profundidad de bits y rango legal](#6-profundidad-de-bits-y-rango-legal)
- [7. El rango dinámico y el HDR](#7-el-rango-dinámico-y-el-hdr)
- [8. Resolución: de la HD al 8K](#8-resolución-de-la-hd-al-8k)
- [9. La relación de aspecto y sus arreglos](#9-la-relación-de-aspecto-y-sus-arreglos)
- [10. La compresión](#10-la-compresión)
- [11. La televisión digital terrestre](#11-la-televisión-digital-terrestre)
- [12. Los aparatos de medida](#12-los-aparatos-de-medida)
- [13. El 3D y la autoestereoscopia](#13-el-3d-y-la-autoestereoscopia)
- [14. Los datos que el examen ha preguntado](#14-los-datos-que-el-examen-ha-preguntado)
- [15. Trazabilidad](#15-trazabilidad)

<!-- /indice -->

## 1. La luz y el color

La luz visible es una franja estrecha del espectro electromagnético, y dentro de ella **la longitud
de onda determina el tono que percibimos**: las longitudes cortas —en torno a 400 nanómetros— se ven
azules y violetas; las largas —en torno a 700— se ven rojas.

Y hay una relación física que el examen pregunta dos veces con distinta cara: **cuanto más corta es
la longitud de onda, mayor es la frecuencia y mayor la energía del fotón**. De ahí que el azul y el
violeta sean los colores llamados *fríos* y estén en el extremo energético del espectro visible, y
que más allá del violeta empiece el ultravioleta, que ya daña. La opción que dice «a mayor longitud
de onda, mayor frecuencia» invierte la relación: **longitud de onda y frecuencia son inversamente
proporcionales**, siempre.

**Un objeto opaco no emite color: lo devuelve.** Iluminado con luz blanca —que contiene todas las
longitudes de onda—, absorbe unas y refleja otras, y las que refleja son las que vemos. Un objeto se
ve verde porque **absorbe todo el espectro visible salvo las longitudes de onda correspondientes al
verde**, que rebotan hacia el ojo. Que el ojo humano sea más sensible al verde es cierto y tiene
consecuencias —está en el epígrafe 4— pero no explica por qué *ese* objeto se ve verde y el de al
lado rojo.

**La saturación depende de lo ancho que sea el espectro reflejado o emitido.** Un color puro es el
que ocupa una banda estrecha: un láser, una lámpara de sodio, un filtro muy selectivo. Conforme se
ensancha la banda, el color se lava hacia el blanco, que es la suma de todas. Así que **cuanto más
estrecho es el espectro, más saturado es el color**, y el blanco es el caso límite de espectro
máximamente ancho y saturación cero.

Tres magnitudes describen cualquier color y aparecen en todas las herramientas del oficio:

| Magnitud | Otros nombres | Qué mide |
|---|---|---|
| **Matiz** | Tono, *hue* | El color en sí: rojo, verde, azul |
| **Saturación** | Pureza, *chroma* | Cuánto se aparta del gris del mismo brillo |
| **Brillo** | Luminosidad, *value*, *lightness* | Cuánta luz llega |

---

## 2. Cómo se ordena el color: los sistemas de representación

Ordenar los colores es viejo y hay varias formas de hacerlo. El examen pregunta por cuatro y sólo
una responde a la definición de las tres magnitudes del epígrafe anterior:

| Sistema | En qué se basa |
|---|---|
| **Munsell** | **Matiz, valor (brillo) y croma (saturación)**: los tres ejes, ordenados como un sólido |
| **Diagrama UCS** | Un diagrama de cromaticidad del CIE con la escala deformada para que distancias iguales se perciban como diferencias iguales |
| **Sistema NCS** | Colores naturales: cuánto tiene un color de cada uno de los seis colores elementales |
| **Triángulo de Maxwell** | La mezcla aditiva de tres primarios, colocados en los vértices |

**El sistema de Munsell es el que se organiza por brillo, matiz y saturación**, y es el que el
examen busca. Los otros tres son sistemas de color legítimos, pero ninguno de ellos toma esas tres
magnitudes como sus tres ejes: el UCS y el triángulo de Maxwell son diagramas de cromaticidad
—dejan el brillo fuera— y el NCS descompone en colores elementales, no en magnitudes.

Junto a ellos está el instrumento de referencia del vídeo: **el diagrama de cromaticidad CIE de
1931**, donde cada color se sitúa por dos coordenadas, *x* e *y*. Sobre ese diagrama se dibujan los
espacios de color del epígrafe siguiente, y por eso las normas del UIT-R definen sus primarios
justamente así.

---

## 3. El espacio de color y su amplitud

**Un espacio de color es el triángulo que tres primarios dibujan sobre el diagrama de
cromaticidad.** Todo lo que cae dentro del triángulo se puede reproducir mezclando los tres
primarios; todo lo que cae fuera, no. Cuanto más separados están los vértices, mayor es la superficie
y más colores caben: eso es la **amplitud** o *gamut*.

Los primarios están escritos con nombre y coordenadas en las Recomendaciones del UIT-R, y se citan
literalmente:

**Recomendación UIT-R BT.709-6**, el espacio de la alta definición, coordenadas de cromaticidad
(CIE, 1931):

> Color primario / – Rojo (R) / – Verde (G) / – Azul (B) / 0,640 / 0,300 / 0,150 / 0,330 / 0,600 /
> 0,060. Cromaticidad supuesta para señales primarias iguales (Blanco de referencia) D65 / x /
> y / 0,3127 / 0,3290.

**Recomendación UIT-R BT.2020-2**, el espacio de la ultraalta definición:

> Colores primarios y blanco de referencia. Coordenadas de cromaticidad (CIE, 1931) x y. Rojo
> primario (R) 0,708 0,292. Verde primario (G) 0,170 0,797. Azul primario (B) 0,131 0,046. Blanco de
> referencia (D65) 0,3127 0,3290.

Los dos comparten blanco de referencia —el iluminante **D65**— y difieren en los primarios: los del
2020 están mucho más lejos del centro, y por eso el triángulo es mucho mayor.

Con esas coordenadas en la mano, el orden de amplitud de los cuatro espacios que el examen pone a
ordenar es éste:

| Espacio | Para qué se usa | Amplitud |
|---|---|---|
| **Rec. 709** | Televisión de alta definición | La menor de las cuatro |
| **DCI P3** | Cine digital y pantallas de cine | Mayor que la 709, sobre todo hacia el rojo y el verde |
| **Rec. 2020** | Ultraalta definición | Muy superior a las dos anteriores |
| **AP0** | Espacio de trabajo interno de *ACES*, para intercambio y archivo | La mayor: **contiene el visible entero** |

**De menor a mayor: Rec. 709, DCI P3, Rec. 2020, AP0.** El **AP0** no es un espacio de pantalla:
sus primarios son *imaginarios* —caen fuera del diagrama de cromaticidad, en colores que no existen—
justamente para que su triángulo envuelva todo lo que el ojo humano puede ver. Ningún monitor lo
reproduce; es un contenedor para no perder información entre etapas.

**La trampa del enunciado está en el AP0.** Quien conozca los tres primeros y no el cuarto puede dar
por bueno un orden que acabe en Rec. 2020, y las cuatro opciones están construidas para que eso
falle.

---

## 4. De la luz a la señal: luminancia y diferencia de color

El ojo humano distingue mucho mejor los cambios de brillo que los de color. La televisión explota
esa asimetría desde que existe: en lugar de transmitir rojo, verde y azul por separado, transmite
**una señal de luminancia (Y) y dos de diferencia de color (C<sub>B</sub> y C<sub>R</sub>,
o U y V en la nomenclatura analógica)**.

**La luminancia no es la media de los tres primarios: es una suma ponderada**, y los pesos salen de
la sensibilidad del ojo a cada color. La **Recomendación UIT-R BT.601-7**, la de la televisión
convencional, lo escribe así en su determinación de la señal de luminancia:

> 0,299 / 0,587 / 0,114

Es decir, **el verde aporta el 58,7 %, el rojo el 29,9 % y el azul el 11,4 %** — redondeados en el
examen a 59 %, 30 % y 11 %. La respuesta oficial a la pregunta 90 del primer cuadernillo es
«59 % Verde + 30 % Rojo + 11 % Azul», y **es exacta**: coincide con los coeficientes del UIT-R
para la definición convencional.

Los coeficientes **no son los mismos en todos los sistemas**, y esto es lo que el tema tiene que
añadir a la respuesta oficial. Cada espacio de color tiene los suyos, porque dependen de los
primarios:

| Recomendación | Sistema | Rojo | Verde | Azul |
|---|---|---|---|---|
| **UIT-R BT.601-7** | Definición convencional | 0,299 | **0,587** | 0,114 |
| **UIT-R BT.709-6** | Alta definición | 0,2126 | **0,7152** | 0,0722 |
| **UIT-R BT.2020-2** | Ultraalta definición | 0,2627 | **0,6780** | 0,0593 |

La BT.709-6 lo escribe en su apartado 3.2, «Determinación de la señal de luminancia»:

> E Y  0,2126 R E  0,7152 G E  0,0722 B E

**En los tres el verde manda**, que es lo que la pregunta pide reconocer; pero **quien memorice
«59-30-11» como si fuera universal se equivocará en cuanto le pregunten por HD o por UHD.** El
enunciado de la 90 habla de vídeo por componentes en general y la plantilla acepta los coeficientes
de la BT.601: el temario lo recoge así y advierte de los otros dos.

---

## 5. La digitalización: muestreo, cuantificación y codificación

Convertir una señal analógica en digital son **tres pasos en un orden que no se puede alterar**:

1. **Muestreo.** Se toma el valor de la señal a intervalos regulares. Lo que se decide aquí es *cada
   cuánto* se mira, es decir, la **frecuencia de muestreo**. La BT.601-7 la fija en **13,5 MHz** para
   la luminancia de la norma 4:2:2.
2. **Cuantificación.** A cada muestra se le asigna el valor más próximo de una escala finita. Lo que
   se decide aquí es *con cuánta finura* se mide, es decir, la **profundidad de bits**. La BT.601-7
   la describe como «MIC con cuantificación uniforme, 8 ó 10 bits por muestra».
3. **Codificación.** Cada valor cuantificado se escribe como una palabra binaria, y se le añade lo
   que haga falta para transportarlo.

**Muestreo, cuantificación y codificación**, en ese orden. El orden importa porque cada paso trabaja
sobre el resultado del anterior: no se puede cuantificar lo que aún no se ha muestreado, ni codificar
lo que aún no tiene valor asignado.

**El submuestreo de crominancia es una segunda economía, encima de la primera.** Como el ojo ve peor
el color que el brillo, se toman menos muestras de C<sub>B</sub> y C<sub>R</sub> que de Y. La
notación de tres cifras dice cuántas:

| Notación | Luminancia | Crominancia | Dónde se usa |
|---|---|---|---|
| **4:4:4** | Una muestra por píxel | Una muestra por píxel | Grafismo, croma, masterizado |
| **4:2:2** | Una muestra por píxel | **Una de cada dos** en horizontal | Producción y contribución profesional |
| **4:2:0** | Una muestra por píxel | Una de cada dos en horizontal **y en vertical** | Emisión y distribución |

**En 4:2:2, la luminancia se muestrea en cada píxel y las dos diferencias de color cada dos.** Ésa es
la respuesta oficial a la pregunta 36 del segundo cuadernillo, y es correcta. La BT.601-7 lo describe
como una operación posterior sobre la señal completa:

> Para obtener las componentes 4:2:2 Y, CR, CB, debe efectuarse el filtrado de paso bajo y el
> submuestreo en las señales 4:4:4 CR, CB anteriormente descritas.

Y la misma norma remata el reparto en el anexo de estructuras de muestreo:

> Los números respectivos de muestras de diferencia de color en la norma 4:2:2 se pueden obtener
> dividiendo el número de muestras de luminancia por 2.

**Las opciones falsas de esa pregunta cambian C<sub>R</sub> y C<sub>B</sub> por «Y+R» e «Y+B».** Las
señales de diferencia de color son **restas**, no sumas: R−Y y B−Y. Quien lea deprisa el signo se
lleva la opción equivocada.

---

## 6. Profundidad de bits y rango legal

**La profundidad de color es cuántos valores distintos puede tomar cada muestra**, y se mide en bits
por componente: con *n* bits caben 2<sup>n</sup> valores.

| Profundidad | Valores por componente | Qué permite |
|---|---|---|
| **1 bit** | 2 | Sólo dos estados: **una imagen monocromática** |
| **8 bits** | 256 | Distribución y emisión convencional |
| **10 bits** | 1.024 | Producción profesional, HDR |
| **12 bits** | 4.096 | Cine digital, masterizado HDR |

**Una imagen de 1 bit de profundidad es monocromática**, y aquí conviene despejar una confusión de
vocabulario que el examen no aclara: monocromático **no** quiere decir «en escala de grises», sino
**de un solo color**, en el sentido de que cada píxel sólo puede estar encendido o apagado. Blanco y
negro puros, sin grises intermedios. Las opciones que dicen «completamente oscura» o «totalmente
blanca» describirían una imagen de 1 bit **con todos los píxeles al mismo valor**, que es un caso
particular, no la definición.

**Y el rango legal.** Aunque en 8 bits caben 256 valores del 0 al 255, la televisión **no los usa
todos**: reserva los extremos para señalización y para que los rebasamientos no se recorten. La
Recomendación UIT-R BT.601-7 lo escribe así:

> el nivel de negro corresponde al nivel 16,00d y el nivel de blanco de cresta corresponde al nivel
> 235,00d. El nivel de la señal puede ocasionalmente sobrepasar el nivel 235,00d o estar por debajo
> del nivel 16,00d.

**El rango legal de una señal de vídeo de 8 bits va del 16 al 235**, y la BT.709-6 confirma la
correspondencia en 10 bits con la tabla de asignación de niveles de cuantificación:

> Nivel de negro R, G, B, Y – Acromático CB, CR – Valor de cresta nominal – R, G, B, Y – CB, CR /
> 16 128 235 16 y 240 / 64 512 940 64 y 960

Con lo cual las cuatro opciones de la pregunta 61 del segundo cuadernillo se explican solas: **el
16-235 es el rango legal de 8 bits; el 64-940 es el mismo rango legal en 10 bits**; el 0-255 es el
rango *completo* de 8 bits, no el legal; y el «256 al 3760» no corresponde a nada.

---

## 7. El rango dinámico y el HDR

**El rango dinámico es la distancia entre la luz más tenue y la más brillante que un sistema puede
registrar o mostrar a la vez.** No es el número de colores —eso es el espacio de color— ni el número
de píxeles: es cuánto contraste cabe dentro de una misma imagen.

**Un mayor rango dinámico da detalle simultáneo en las sombras y en las altas luces.** Con rango
corto hay que elegir: o se expone para la ventana y el interior se va a negro, o se expone para el
interior y la ventana se quema. Con rango largo caben las dos cosas.

Sobre esa idea se construye el HDR, y la **Recomendación UIT-R BT.2100-1** define **dos** funciones
de transferencia para producirlo e intercambiarlo:

> se utilicen las especificaciones de cuantización perceptiva (PQ) e híbrida Log-Gamma (HLG) de la
> presente Recomendación

Las dos no son intercambiables, y el examen pregunta por la primera:

| | **PQ** | **HLG** |
|---|---|---|
| Qué es | Cuantización perceptiva | Logaritmo híbrido |
| Referencia | **A la pantalla**: cada valor codificado es una luminancia absoluta en cd/m² | **A la escena**: la luminancia final depende del pico de la pantalla |
| Retrocompatibilidad | No la tiene: una pantalla convencional no lo interpreta | La tiene en buena medida, por construirse sobre una curva de tipo gamma |
| Metadatos | Los usa para adaptar el contenido a cada pantalla | No los necesita |
| Pico | **10.000 cd/m²** | Definido por la pantalla, con γ = 1,2 para el pico nominal de 1.000 cd/m² |

**El PQ tiene un pico de brillo máximo de 10.000 cd/m²**, y esa cifra está en el propio cuadro de la
norma: la función de transferencia electroóptica de referencia del PQ multiplica el valor lineal
normalizado —en la gama [0:1]— por **10000** para dar la luminancia presentada en cd/m². Es el
factor que fija el techo de la curva.

**Aquí hay que advertir de una cosa antes de citar la cifra.** El texto extraído del PDF de la
BT.2100-1 desordena las fórmulas: la EOTF de referencia aparece como «1 2 2 1 1 3 2 1 1 0, máx 10000
EOTF m m m D E c c c E Y Y E F», que no se puede leer como fórmula. La cifra **10000** está ahí, y la
página del PDF la muestra en su sitio, pero **quien cite esta norma tiene que mirar la página, no el
volcado de texto**. Es la regla que el propio proyecto tiene escrita para las normas técnicas y que
aquí se aplica.

Y las tres opciones falsas de la pregunta 64 describen, cada una, algo real que **no** es el PQ: «se
basa en la curva Rec.709» describe una gamma convencional; «es retrocompatible y tiene metadata»
mezcla un rasgo del HLG con otro del PQ; y «es un sistema referenciado a la escena» es exactamente
la definición del **HLG**, no del PQ. La pregunta separa las dos curvas por su rasgo más distintivo.

---

## 8. Resolución: de la HD al 8K

**La resolución es el número de píxeles de la imagen**, y se escribe como horizontales por
verticales:

| Nombre | Resolución | Relación de aspecto |
|---|---|---|
| **SD** (definición convencional, 576i) | 720 × 576 | 4:3 o 16:9 |
| **HD Ready** | 1280 × 720 | 16:9 |
| **Full HD** | 1920 × 1080 | 16:9 |
| **4K UHD** o **UHD-1** | **3840 × 2160** | 16:9 |
| **DCI 4K** | 4096 × 2160 | 17:9 |
| **8K UHD** o **UHD-2** | 7680 × 4320 | 16:9 |

**La resolución 4K UHD es 3840 × 2160**, que es exactamente **el doble de ancho y el doble de alto
que el Full HD**, y por tanto **cuatro veces su número de píxeles**. El 4096 × 2160 también se llama
4K, pero es el **4K del cine digital**, el del DCI, y no es el de la televisión: confundirlos es el
error que la pregunta 95 castiga.

**Y el UHD no es sólo resolución.** Ésta es la clave de la pregunta 24, que enuncia cuatro
afirmaciones sobre la televisión 4K y sólo da por buena una:

- «Todos los dispositivos 4K son compatibles con contenido 8K» es **falso**: un panel de 3840 × 2160
  no puede mostrar 7680 × 4320 sin reescalar, y muchos ni siquiera aceptan la señal.
- «La 4K se basa únicamente en la mejora de resolución» es **falso**: la UHD trae además espacio de
  color ampliado —la Rec. 2020—, mayor profundidad de bits, HDR y cadencias altas.
- «Ofrece cuatro veces la resolución del Full HD, pero no mejora ni el color ni el rango dinámico»
  es **falso por su segunda mitad**, y ésta es la opción que más se parece a la verdad: la primera
  mitad es exacta y la segunda contradice a la BT.2020 y a la BT.2100. **Media verdad no es una
  respuesta.**
- «Requiere un ancho de banda significativamente mayor, lo que puede limitar su accesibilidad en
  zonas con conexiones lentas» es **verdad** y es la respuesta oficial.

**Cuatro veces los píxeles son, a igualdad de todo lo demás, cuatro veces los datos**, y por eso el
UHD sólo llegó a ser posible cuando llegó un códec capaz de comprimirlo: el del epígrafe 10.

---

## 9. La relación de aspecto y sus arreglos

**La relación de aspecto es la proporción entre el ancho y el alto de la imagen**, y se obtiene
dividiendo **el número de píxeles horizontales entre el número de píxeles verticales** —siempre que
los píxeles sean cuadrados, que es lo normal en digital—.

Ni la distancia focal, ni el tipo de objetivo, ni el tamaño del sensor la determinan por sí solos:
el objetivo cambia el **campo** que entra, no la **forma** del rectángulo; y el tamaño del sensor
importa por su forma, no por su tamaño. Dos sensores de tamaños muy distintos con la misma matriz de
píxeles dan la misma relación de aspecto.

Las relaciones que el examen maneja, escritas de las dos formas:

| Relación | Como decimal | Dónde |
|---|---|---|
| **4:3** | **1,33:1** | Televisión convencional |
| **16:9** | **1,77:1** | **Alta definición y televisión digital** |
| **1,85:1** | 1,85:1 | Cine, formato panorámico |
| **2,39:1** | 2,39:1 | Cine, formato anamórfico |

**El 16:9 es 1,77:1**, porque 16 ÷ 9 = 1,777… Es aritmética, y esa pregunta se responde dividiendo.

**Cuando una imagen no encaja en la pantalla, hay que decidir qué se sacrifica.** Los dos arreglos
clásicos:

- **Letterboxing**: se añaden **dos franjas negras horizontales**, arriba y abajo, para meter una
  imagen ancha en una pantalla menos ancha **sin recortarla ni deformarla**.
- **Pillarboxing**: las franjas van **a los lados**, para meter una imagen estrecha —un 4:3— en una
  pantalla ancha.

Las tres opciones falsas de la pregunta 88 —*lineboxing*, *franeboxing*, *paineboxing*— no son
términos del oficio: están inventadas sobre la forma de la palabra correcta.

**Y un defecto que aparece cuando la resolución no da para el detalle: el *aliasing*.** Es la
distorsión que surge **cuando en los detalles finos de la imagen aparecen patrones de
interferencia** —el moiré de una camisa de rayas, los dientes de sierra de una línea diagonal—
porque la frecuencia espacial del motivo supera la que el muestreo puede representar. Los *jaggies*
son **una manifestación visible del aliasing** —el escalonado de los bordes—, no el fenómeno; el
*rolling shutter* es un defecto de obturador, no de muestreo espacial; y el *burst* es la salva de
color de la señal analógica. La opción correcta es **aliasing**, que es el nombre del fenómeno.

---

## 10. La compresión

**Comprimir es quitar lo que sobra.** Y lo que sobra tiene dos formas:

- **La redundancia**: información **repetida o predecible**. Un cielo azul uniforme repite el mismo
  valor miles de veces; dos fotogramas consecutivos de un plano fijo son casi idénticos.
- **La entropía**: **la información nueva o esencial**, la que no se puede deducir de nada anterior.
  Es lo que queda cuando se ha quitado toda la redundancia, y es lo que hay que transmitir.

**En compresión, la entropía es la información nueva o esencial.** Esa es la respuesta oficial a la
pregunta 79 y conviene fijarla junto a su contraria, porque las cuatro opciones de esa pregunta
juegan justamente con esa pareja: «la información repetida o predecible» describe la **redundancia**,
y «la información cuya eliminación no afecta al contenido» describe lo **irrelevante** —lo que la
compresión con pérdidas tira—.

Las cuatro maneras de clasificar un códec:

| Eje | Términos | Diferencia |
|---|---|---|
| Qué se pierde | **Sin pérdidas** (*lossless*) / **con pérdidas** (*lossy*) | Si el descomprimido es idéntico al original o sólo se le parece |
| Cuántos fotogramas | **Intraframe** / **Interframe** | Si cada fotograma se comprime solo o mirando a los vecinos |
| Para qué | De **producción** / de **distribución** | Si prima la calidad y la edición o el tamaño del archivo |
| Tasa | **Constante** / **variable** | Si el flujo de bits es fijo o se adapta a la dificultad |

**La compresión interframe es la que combina varios fotogramas a la vez**: codifica un fotograma de
referencia entero y, a partir de él, sólo las diferencias. La intraframe comprime cada fotograma por
separado, como si fuera una fotografía, y por eso es la que se usa en producción: cualquier
fotograma se puede abrir sin reconstruir los anteriores, que es lo que un montador necesita.

Los códecs que el examen nombra:

| Códec | Nombre completo | Año | Resoluciones |
|---|---|---|---|
| **MPEG-2** | Norma ISO/IEC 13818-2 | 1995 | Hasta HD; **no válido para 4K** |
| **H.264 / AVC** | *Advanced video coding* | 2003 | Hasta 4K, con dificultad |
| **H.265 / HEVC** | *High efficiency video coding* | 2013 | **Hasta 8K** |
| **VP9** | Códec abierto de Google | 2013 | Hasta 8K |
| **AV1** | *AOMedia Video 1* | 2018 | Hasta 8K |
| **H.266 / VVC** | *Versatile video coding* | 2020 | Hasta 8K |

**El MPEG-2 es el que no sirve para 4K.** Su diseño es de 1995, para la televisión convencional y la
alta definición temprana; ni sus tamaños de bloque ni sus herramientas de predicción dan para
3840 × 2160 con una tasa razonable. Los otros tres de esa pregunta —HEVC, VP9 y AV1— son
posteriores y están hechos para eso.

**El HEVC es el códec estándar de la emisión UHD en España**, y es el que responde a las dos
preguntas idénticas que los dos cuadernillos repiten. La razón es la ya dicha: la UHD multiplica por
cuatro los datos y el HEVC ofrece **aproximadamente la mitad de tasa binaria que el H.264 para la
misma calidad percibida**. El VVC es más eficiente todavía, pero es de 2020 y **no es el códec de la
emisión UHD en España**; el H.264 es el de la HD y no da el salto.

**Y una advertencia sobre la pregunta 27, la del H.265.** Su respuesta oficial —«permite la
codificación de vídeo en resoluciones de hasta 8K»— es correcta, pero la opción es más modesta de lo
que el códec merece: lo característico del HEVC no es el techo de resolución sino **la mitad de tasa
para la misma calidad**. Las tres opciones falsas dicen justamente lo contrario de eso —doble ancho
de banda, 50 % menos eficiente— o una falsedad plana: que no sirve para tiempo real, cuando es
precisamente el códec de la emisión en directo.

---

## 11. La televisión digital terrestre

**La TDT se transmite por ondas hertzianas terrestres**, desde estaciones en tierra, a través de la
atmósfera, **sin necesidad de cable ni de satélite**, y se recibe **con antenas convencionales de
UHF**. Ésa es la definición y es lo que la distingue de sus dos alternativas: el cable lleva la señal
por un medio físico hasta el domicilio, y el satélite la rebota desde la órbita.

Las dos preguntas que el examen dedica a esto —una en cada cuadernillo— están construidas con la
misma trampa: **opciones que empiezan bien y terminan metiendo un cable o un satélite**. «Se
transmite por ondas hertzianas terrestres… y recibidas por cable o satélite en cada edificio»
describe una cabecera de distribución, no la TDT. Y «ondas de radio terrestres… a través de la
atmósfera vía satélite» es una contradicción en sus propios términos: o es terrestre o es por
satélite.

**La norma que rige esa emisión es europea, no española.** La primera generación es la
**ETSI EN 300 744**, *Digital Video Broadcasting (DVB); Framing structure, channel coding and
modulation for digital terrestrial television*; la segunda, la **ETSI EN 302 755**, del DVB-T2, que
es la que soporta la emisión en alta definición y ultraalta definición.

**Y la modulación.** La norma lo escribe en su apartado 4.3.5, «Signal constellations and mapping»:

> The system uses Orthogonal Frequency Division Multiplex (OFDM) transmission. All data carriers in
> one OFDM frame are modulated using either QPSK, 16-QAM, 64-QAM, non-uniform 16-QAM or non-uniform
> 64-QAM constellations.

Hay que leer eso con cuidado, porque **son dos cosas distintas y las dos se llaman «modulación» en
lenguaje corriente**:

- **La OFDM es el reparto en portadoras**: en lugar de una portadora ancha, miles de portadoras
  estrechas y ortogonales entre sí. Es lo que da a la TDT su resistencia al eco y lo que permite las
  redes de frecuencia única.
- **La QAM es lo que se hace con cada una de esas portadoras**: modularla en **amplitud y en fase a
  la vez**, de modo que cada símbolo transporte varios bits. La EN 300 744 admite QPSK, 16-QAM y
  64-QAM; el DVB-T2 de la EN 302 755 añade la **256-QAM**, que su lista de abreviaturas define como
  *256-ary Quadrature Amplitude Modulation*.

**La modulación digital de cuadratura (QAM) es la que la TDT usa en cada portadora**, y es la
respuesta oficial. Las tres opciones falsas —AM, FM y PM— son modulaciones **analógicas** de una sola
magnitud: la QAM combina amplitud y fase, que es lo que la hace digital y eficiente.

---

## 12. Los aparatos de medida

**Un monitor de imagen dice si algo se ve bien; un aparato de medida dice si la señal está bien.** Y
no es lo mismo: un monitor mal calibrado enseña una imagen equivocada con toda convicción. Ésta es
la razón de que un control de realización tenga siempre, al lado de las pantallas, instrumentos que
no interpretan nada.

| Aparato | Qué representa | Para qué sirve |
|---|---|---|
| **Monitor de forma de onda** | La **luminancia** de la señal a lo largo de la línea, en un eje vertical graduado | Ver niveles de vídeo, negros, blancos y rebasamientos |
| **Vectorscopio** | La **crominancia** en coordenadas polares: el ángulo es el matiz, el radio la saturación | Ver la **pureza de los colores** y comprobar la fase |
| **Osciloscopio digital** | Cualquier forma de onda, de vídeo o de audio, en función del tiempo | Analizar **sincronismos** y calidad de señal |
| **Rasterizador** | Varias representaciones a la vez, generadas por *software* y volcadas a un monitor externo | Monitorizar **señales en HD** mientras se muestran sus representaciones |

**El monitor de forma de onda es el aparato de la calidad en directo.** La pregunta 20 del primer
cuadernillo pide la herramienta fundamental para garantizar la calidad de una transmisión en directo
detectando errores a tiempo y corrigiendo parámetros **como el nivel de vídeo**, y ese último inciso
es el que decide: **nivel de vídeo es luminancia, y la luminancia se mide en el monitor de forma de
onda**. Un servidor de *streaming* transporta, un editor no lineal monta y un gestor de contenidos
archiva; ninguno mide.

**El vectorscopio muestra la pureza de los colores.** Su pantalla es un círculo con seis cajas
—rojo, verde, azul, cian, magenta y amarillo—: la dirección del trazo dice el matiz y la distancia al
centro dice la saturación. No representa luminancia; para eso está el otro aparato. Y no muestra «el
diagrama del ojo», que es una herramienta de transmisión digital para medir la calidad del enlace,
no del color.

**Y aquí está la pregunta que este tema tiene que matizar: la 20 del segundo cuadernillo.** Pregunta
qué hacer para comprobar una señal en blanco y negro con un vectorscopio, y la respuesta oficial es
**«un vectorscopio no representa señales de blanco y negro»**.

**La respuesta oficial es la correcta de las cuatro, y su enunciado es impreciso.** Un vectorscopio
alimentado con una señal monocroma **sí representa algo**: un punto en el centro de la pantalla,
porque la saturación es cero y no hay vector que apuntar en ninguna dirección. Lo que la opción
quiere decir —y dice mal— es que **en una señal sin color no hay nada que el vectorscopio pueda
comprobar**: el instrumento no está ciego, es que no hay materia. Las otras tres opciones son
peores y por razones claras: las dos del barrido —a frecuencia de línea o de campo— describen
controles de un **osciloscopio**, no de un vectorscopio, que no tiene barrido temporal; y la de los
0,70 V y 0 V describe una medida de **niveles**, que es cosa del **monitor de forma de onda**.

**No es una errata de plantilla**, porque la opción marcada es la única defendible; es una redacción
que confunde «no representa» con «no sirve para comprobar». El opositor la acierta si sabe qué mide
cada aparato.

---

## 13. El 3D y la autoestereoscopia

La televisión en relieve reproduce la visión binocular: **dar a cada ojo una imagen ligeramente
distinta**, tomada desde un punto de vista separado unos centímetros. La diferencia entre los
sistemas está en **cómo se separan las dos imágenes** al llegar al espectador.

| Sistema | Cómo separa las dos imágenes | Gafas |
|---|---|---|
| **Anaglifo** | Por color: un filtro rojo y otro cian | Sí |
| **Polarización pasiva** | Por el plano de polarización de la luz | Sí |
| **Obturación activa** | Por tiempo: cada ojo se tapa alternativamente, sincronizado con la pantalla | Sí, **gafas LCD de obturación** |
| **Autoestereoscopia** | **Por filtros ópticos en la propia pantalla**, que dirigen espacialmente cada imagen a cada ojo | **No** |

**La autoestereoscopia es la que no necesita gafas**, y es lo que su nombre dice: la pantalla misma
hace el trabajo de separación. La respuesta oficial la describe como «la generación de la imagen 3D
en la pantalla receptora mediante una serie de filtros que permiten el entrelazado vertical espacial
de las imágenes dirigidas a cada ojo», y es exacta: los dos métodos reales son la **barrera de
paralaje** —una rejilla que tapa a cada ojo las columnas que no le tocan— y la **red lenticular**
—una lámina de microlentes cilíndricas que desvía cada columna hacia un lado—. Los dos son filtros
sobre la pantalla y los dos trabajan por columnas verticales.

Las tres opciones falsas describen, otra vez, cosas reales que no son la pregunta: la de las **gafas
LCD de obturación** es la obturación activa; la de las **líneas pares e impares** es el 3D
entrelazado por líneas de la polarización pasiva; y la de las capas superpuestas que se desplazan no
corresponde a ningún sistema estereoscópico.

---

## 14. Los datos que el examen ha preguntado

| Nº | Cuadernillo | Qué pregunta | Oficial |
|---|---|---|---|
| 13 | primero | Qué es la autoestereoscopia | d) Filtros en la pantalla, entrelazado vertical espacial ✔ |
| 18 | primero | Cómo se transmite la TDT | a) Ondas hertzianas terrestres, sin cable ni satélite, antenas UHF ✔ |
| 20 | primero | Herramienta para la calidad en directo | d) Un monitor de forma de onda ✔ |
| 24 | primero | Afirmación correcta sobre la televisión 4K | d) Requiere un ancho de banda mayor ✔ |
| 26 | primero | Longitud de onda y color percibido | b) A menor longitud, mayor energía y color más frío ✔ |
| 27 | primero | Afirmación correcta sobre el H.265 | d) Codifica hasta 8K ✔ |
| 28 | primero | Por qué vemos verde un objeto | c) Absorbe todo el espectro salvo el verde ✔ |
| 37 | primero | Espacios de color de menor a mayor amplitud | d) Rec. 709, DCI P3, Rec. 2020, AP0 ✔ |
| 42 | primero | Qué determina la relación de aspecto | a) Píxeles horizontales entre píxeles verticales ✔ |
| 62 | primero | Qué visualiza un vectorscopio | b) La pureza de los colores ✔ |
| 63 | primero | Códec de la emisión UHD en España | c) HEVC ✔ |
| 70 | primero | Códec NO válido para 4K | b) MPEG-2 ✔ |
| 79 | primero | Qué es la entropía en compresión | c) La información nueva o esencial ✔ |
| 90 | primero | Composición de la señal de luminancia | d) 59 % Verde + 30 % Rojo + 11 % Azul ✔ |
| 94 | primero | Compresión que combina varios fotogramas | b) Interframe ✔ |
| 95 | primero | Resolución 4K UHD | a) 3840 × 2160 ✔ |
| 105 | primero | Espectro luminoso y color percibido | b) Cuanto más estrecho, más saturado ✔ |
| 120 | primero | Imagen de 1 bit de profundidad | c) Monocromática ✔ |
| 20 | segundo | Vectorscopio con señal en blanco y negro | c) No representa señales de blanco y negro **·** imprecisa |
| 22 | segundo | Modulación de la TDT | c) Modulación digital de cuadratura (QAM) ✔ |
| 24 | segundo | El osciloscopio en televisión | c) Permite analizar formas de onda de vídeo y audio ✔ |
| 28 | segundo | Impacto del rango dinámico | b) Más detalle en sombras y altas luces ✔ |
| 36 | segundo | Qué significa 4:2:2 | a) Luminancia en cada píxel, Cr y Cb cada dos ✔ |
| 54 | segundo | Los tres procesos de la digitalización | a) Muestreo-cuantificación-codificación ✔ |
| 59 | segundo | De qué se encargan los rasterizadores | c) Monitorizar HD con representaciones en otro monitor ✔ |
| 61 | segundo | Rango legal de una señal de 8 bits | b) Del 16 al 235 ✔ |
| 64 | segundo | Característica del estándar PQ | d) Pico de brillo máximo de 10.000 cd/m² ✔ |
| 66 | segundo | Imagen de 1 bit de profundidad | c) Monocromática ✔ |
| 85 | segundo | Relación de aspecto del 16:9 | d) 1.77:1 ✔ |
| 87 | segundo | Distorsión con patrones de interferencia | c) Aliasing ✔ |
| 88 | segundo | Dos franjas negras horizontales | c) Letterboxing ✔ |
| 89 | segundo | Sistema basado en brillo, matiz y saturación | d) Munsell ✔ |
| 105 | segundo | Cómo se transmite la TDT | b) Ondas hertzianas, sin cable ni satélite, antenas UHF ✔ |
| 106 | segundo | Códec de la emisión UHD en España | c) HEVC ✔ |

**Treinta y tres de las treinta y cuatro respuestas oficiales son correctas.** La restante —la **20
del segundo cuadernillo**— tiene marcada la única opción defendible con un enunciado impreciso, que
el epígrafe 12 corrige: un vectorscopio alimentado con una señal monocroma sí pinta algo —un punto
en el centro—; lo que no hay es vector que comprobar. **No es errata de plantilla.**

**Y dos parejas de preguntas repetidas entre cuadernillos**, palabra por palabra: la del códec de la
emisión UHD (63 y 106) y la de la imagen de 1 bit (120 y 66). Es la señal más clara de que estos dos
datos son de los que el tribunal considera básicos.

**Un aviso de estudio sobre la 90.** Su respuesta oficial recoge los coeficientes de la
**Recomendación UIT-R BT.601-7**, que son los de la definición convencional. **La alta definición y
la ultraalta usan otros**, recogidos en el cuadro del epígrafe 4. La pregunta es correcta tal como
está redactada; el error sería quedarse con el 59-30-11 creyéndolo universal.

---

## 15. Trazabilidad

**Éste es el primer tema del bloque específico de Realización (Asistencia) que se apoya en normas
publicadas**, y todas son del segundo nivel de la jerarquía de fuentes —organismo de normalización—:

| Norma | Qué sostiene aquí | Fichero |
|---|---|---|
| **Recomendación UIT-R BT.601-7** | Coeficientes de luminancia 0,299 / 0,587 / 0,114; muestreo 4:2:2 y frecuencia de 13,5 MHz; niveles 16 y 235 | `fuentes/normas-tecnicas/UIT-R_BT.601-7.pdf` |
| **Recomendación UIT-R BT.709-6** | Primarios y blanco D65 de la HD; coeficientes 0,2126 / 0,7152 / 0,0722; asignación de niveles en 8 y 10 bits | `fuentes/normas-tecnicas/UIT-R_BT.709-6.pdf` |
| **Recomendación UIT-R BT.2020-2** | Primarios y blanco de la UHD; coeficientes 0,2627 / 0,6780 / 0,0593 | `fuentes/normas-tecnicas/UIT-R_BT.2020-2.pdf` |
| **Recomendación UIT-R BT.2100-1** | Las dos funciones de transferencia del HDR, PQ y HLG, y el techo de 10.000 cd/m² del PQ | `fuentes/normas-tecnicas/UIT-R_BT.2100-1.pdf` |
| **ETSI EN 300 744** | OFDM y constelaciones QPSK, 16-QAM y 64-QAM del DVB-T | `fuentes/normas-tecnicas/ETSI_EN-300-744.pdf` |
| **ETSI EN 302 755** | La 256-QAM del DVB-T2 | `fuentes/normas-tecnicas/ETSI_EN-302-755.pdf` |

**Todas las citas entre comillas de este tema salen de esas seis normas y están comprobadas sobre el
texto español publicado por la UIT** —las cuatro Recomendaciones se descargaron en su versión en
español— **y sobre el texto inglés del ETSI**, que sólo publica en inglés.

**Con una salvedad escrita, que es la que obliga a mirar la página.** La fórmula de la EOTF de
referencia del PQ **no se puede citar desde el texto extraído**: el volcado desordena los símbolos y
los exponentes. Lo que este tema afirma de ella —que multiplica el valor lineal normalizado por
10.000 para dar cd/m²— está leído **en la página del PDF**, no en el volcado, tal como exige la regla
del propio proyecto para las normas técnicas: con una norma técnica en PDF, el texto extraído no es
la fuente; la página lo es.

**Lo que va como oficio y no como norma**, y así se declara: el orden de amplitud de los cuatro
espacios de color —el AP0 no está en ninguna Recomendación del UIT-R, sino en la especificación ACES
de la Academia, que no se ha consultado—; la tabla de sistemas de representación del color, que
recoge cuatro sistemas de uso general; la tabla de códecs con sus años y techos de resolución; los
cuatro sistemas de televisión en relieve; y la descripción de para qué sirve cada aparato de medida
en un control de realización.

**Y una fuente que no se ha podido traer.** La especificación del **DCI** para el espacio P3 sigue
sin ser accesible: `dcimovies.com` responde, pero es una aplicación de JavaScript que no sirve
ningún documento por ruta estática, y así consta ya en `fuentes/fabricantes/README.md`. Lo que este
tema dice del P3 —que es más amplio que la Rec. 709 y menos que la Rec. 2020— es conocimiento
corriente del sector y **no está respaldado por su norma**.
