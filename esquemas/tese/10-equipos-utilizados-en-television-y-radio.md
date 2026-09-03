# Esquema · Tema 10 del específico de Técnica de Equipos y Sistemas Electrónicos · Equipos utilizados en televisión y radio

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de sala técnica · `[plan]` =
plantilla oficial. **Siglas**: el panel remoto de control de cámara (**RCP**); los tres primarios
(**RGB**); la línea de alternancia de fase (**PAL**); el conjunto redundante de discos independientes
(**RAID**) y la conexión serie de tecnología avanzada (**SATA**); el terabyte (**TB**); la escucha
previa al atenuador (**PFL**, *pre fade listen*); el efecto de baja frecuencia (**LFE**); el decibelio
referido a 0,775 voltios (**dBu**); el factor de calidad (**Q**); y los conectores **BNC**, **XLR**,
**RJ 45** y el híbrido de fibra de la Sociedad de Ingenieros de Cine y Televisión (**SMPTE**).

**Cabecera.** Enunciado: punto 12 del anexo, el más largo de todos · **19 preguntas: el banco más
grande de la ocupación** · **dos dependen de una figura.**

<!-- indice -->

## Índice

- [La cámara y su óptica](#la-cámara-y-su-óptica)
- [El color](#el-color)
- [Compresión y matriz de conmutación](#compresión-y-matriz-de-conmutación)
- [Los servidores y el RAID](#los-servidores-y-el-raid)
- [El mezclador de sonido](#el-mezclador-de-sonido)
- [Micrófono, vúmetro y efecto Larsen](#micrófono-vúmetro-y-efecto-larsen)
- [Las dos preguntas con figura](#las-dos-preguntas-con-figura)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La cámara y su óptica

- **PREGUNTA 9** · `[of]` · **Una mayor distancia focal disminuye la profundidad de campo.**
- **LA REGLA COMPLETA**: **la profundidad crece con el diafragma cerrado, la distancia y el gran
  angular**; **decrece con el diafragma abierto, la proximidad y el teleobjetivo.**
- **PREGUNTA 66** · `[of]` · **La corrección «Matrix» compensa, combinando las componentes RGB, los
  valores espectrales que no se captaron en la conversión óptico-eléctrica.**
- **CÓMO SE DESCARTAN LAS OTRAS TRES**: **obtener luminancia del RGB lo hace el codificador; recortar
  altas luces lo hace el *knee*; seguir la temperatura de color es otro circuito.**
- **PREGUNTA 1 del segundo llamamiento** · `[of]` · **Es incorrecto que el panel remoto controle el
  enfoque en una producción sin robotizar.**
- **LAS TRES PALABRAS QUE DECIDEN SON «SIN ROBOTIZAR»**: **el panel gobierna ajustes eléctricos**;
  **el enfoque es un movimiento mecánico y sin cabeza robotizada lo hace el cámara.**

## El color

- **PREGUNTA 23** · `[of]` · **En PAL, Y = 0,30R + 0,59G + 0,11B.**
- **LA REGLA MNEMOTÉCNICA**: **verde, rojo, azul de mayor a menor**, y **los tres coeficientes suman
  uno.**
- **PREGUNTA 48** · `[of]` · **4:2:2 significa submuestreo de color.**
- **CÓMO SE LEE LA NOTACIÓN**: **la primera cifra es la referencia de luminancia; las otras dos, cuántas
  muestras de cada diferencia de color hay por cada cuatro de luminancia.**
- **PREGUNTA 25** · `[of]` · **El canal alfa es la señal de escala de grises cuya información es la
  transparencia.** **Un rótulo viaja siempre en dos señales: relleno y llave.** **El alfa es la
  llave.**

## Compresión y matriz de conmutación

- **PREGUNTA 13** · `[of]` · **La ventaja del inter-cuadro es reducir el tamaño aprovechando la
  redundancia temporal entre cuadros sucesivos.**
- **LA PALABRA QUE DECIDE ES «TEMPORAL»**: **la redundancia que aprovecha está en el tiempo, no dentro
  de la imagen.**
- **PREGUNTA 86** · `[of]` · **Una matriz de vídeo conmuta señales de una fuente a varios destinos.**
- **MATRIZ FRENTE A MEZCLADOR**: **la matriz encamina y no cambia la señal; el mezclador combina y
  produce una señal nueva.** **Una matriz no mezcla nada.**

## Los servidores y el RAID

| Nivel | Capacidad útil con *n* discos de tamaño *c* | Discos que puede perder |
|---|---|---|
| **RAID 0** | **n × c** | **Ninguno** |
| **RAID 1** | **c** | **Uno** |
| **RAID 3** | **(n − 1) × c** | **Uno** |
| **RAID 5** | **(n − 1) × c** | **Uno** |

- **PREGUNTA 62** · `[of]` · **Dos discos de 1 TB que se ven como 2 TB son RAID 0.**
- **PREGUNTA 32** · `[of]` · **Cuatro discos de 2 TB en RAID 5 dan 6 TB.** **(4 − 1) × 2.**
- **EL AVISO**: **el RAID 0 no es redundante pese al nombre de la familia.** **Es el que más capacidad
  da y el único que no protege de nada.**

## El mezclador de sonido

- **PREGUNTA 18** · `[of]` · **El ancho de banda de un filtro paramétrico se fija con el factor de
  calidad.** **A más factor, más estrecha la campana.**
- **PREGUNTA 24** · `[of]` · **El PFL reproduce la señal antes del atenuador para monitorizarla sin
  enviarla al bus principal.** **Las siglas lo dicen: *pre fade listen*.**
- **PREGUNTA 95** · `[of]` · **Con la ganancia en −3 dB y un objetivo de 1 dB, el atenuador va a +4
  dB.** **Los decibelios en cadena se suman: −3 + 4 = 1.**
- **PREGUNTA 78** · `[of]` · **0 dBu son 0,775 voltios eficaces.** **Es la tensión que disipa un
  milivatio en 600 ohmios.**

## Micrófono, vúmetro y efecto Larsen

- **PREGUNTA 15** · `[of]` · **La ventaja del hipercardioide es un mayor rechazo lateral.**
- **PREGUNTA 80** · `[of]` · **Un vúmetro mide el nivel con respuesta lenta.** **La lentitud es la
  especificación, no un defecto: sigue la sonoridad, no el pico.**
- **PREGUNTA 88** · `[of]` · **El sonido del altavoz recaptado por el micrófono es el efecto Larsen.**
  **Se combate bajando ganancia, alejando, orientando y con un filtro estrecho.**

## Las dos preguntas con figura

- **PREGUNTA 16** · `[plan]` · **El nivel de salida del preamplificador de la figura es 12 dBu.**
- **PREGUNTA 16 del segundo llamamiento** · `[plan]` · **Los puertos CAM 3 y CAM 4 llevan conector
  SMPTE híbrido de fibra óptica.**
- **ESTE ESQUEMA NO HA VISTO NINGUNA DE LAS DOS IMÁGENES Y NO LAS DESCRIBE.**
- **LA REGLA DE LA FAMILIA DE LA SEGUNDA**: **el BNC lleva coaxial, el XLR audio y el RJ 45 red.**
  **Sólo el híbrido resuelve en un cuerpo lo que una cámara necesita: ida, vuelta y corriente.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 9 | Efecto de la distancia focal en la profundidad de campo | c) Mayor focal, menor profundidad ✔ |
| 13 | Ventaja del inter-cuadro | b) Aprovecha la redundancia temporal ✔ |
| 15 | Ventaja del micrófono hipercardioide | b) Mayor rechazo lateral ✔ |
| 16 | Nivel de salida del preamplificador | d) 12 dBu ✔ **·** figura |
| 18 | Cómo se fija el ancho de banda en un paramétrico | c) Con el factor de calidad ✔ |
| 23 | Ecuación de luminancia del PAL | d) Y = 0,30R + 0,59G + 0,11B ✔ |
| 24 | Función del modo PFL | d) Escucha antes del atenuador ✔ |
| 25 | Qué es el canal alfa | c) Escala de grises de transparencia ✔ |
| 32 | Capacidad de un RAID 5 de cuatro discos de 2 TB | d) 6 TB ✔ |
| 48 | Qué significa 4:2:2 | b) Submuestreo de color ✔ |
| 62 | RAID de dos discos de 1 TB vistos como 2 TB | a) RAID 0 ✔ |
| 66 | Función de la corrección «Matrix» | b) Compensar valores espectrales no captados ✔ |
| 78 | Voltios que son 0 dBu | c) 0,775 voltios eficaces ✔ |
| 80 | Qué mide un vúmetro | a) Nivel con respuesta lenta ✔ |
| 86 | Definición de matriz de vídeo | b) Conmutar de una fuente a varios destinos ✔ |
| 88 | Sonido del altavoz recaptado por el micrófono | b) Efecto Larsen ✔ |
| 95 | Atenuador para pasar de −3 dB a 1 dB | b) +4 dB ✔ |
| 1 (2.º llam.) | Afirmación incorrecta sobre el panel remoto | b) Que controle el enfoque ✔ |
| 16 (2.º llam.) | Conector de los puertos CAM 3 y CAM 4 | d) SMPTE híbrido de fibra ✔ **·** figura |

**Las diecinueve oficiales son correctas** · **dos descansan en la plantilla, y son las dos que llevan
figura.** · **Aviso de estudio**: **tres son cálculo puro, dos son cifras que hay que memorizar y
catorce se contestan sabiendo qué hace cada aparato.** **Es el punto donde más rinde repasar el
inventario de la sala.**
