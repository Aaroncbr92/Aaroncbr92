# Esquema · Tema 4 del específico de Ingeniería Superior · Telecomunicación · Medios de transmisión, conectores y compresión

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de instalaciones audiovisuales ·
`[plan]` = enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: la
interfaz digital serie (**SDI**) y su versión de alta definición (**HD-SDI**); el conector de bayoneta
**BNC** y su versión de alta densidad **HD-BNC**; el conector de audio **XLR**; el conector registrado
45 (**RJ45**); los módulos enchufables **SFP** y **QSFP**; el bus serie universal (**USB**); la
interfaz multimedia de alta definición (**HDMI**) y la digital de vídeo (**DVI**); el protocolo de
internet (**IP**); el gigabit por segundo (**Gbit/s**); y el ohmio (**Ω**).

**Cabecera.** Enunciado: punto 4 del anexo · **seis preguntas** · **sin norma**: el punto no nombra
ninguna y el tema va como oficio.

**El deslinde con el punto 3** · `[plan]` · **Allí, cómo se manda; aquí, por qué medio se manda.**

**La idea que lo ordena** · `[of]` · **El medio guiado se controla y el no guiado se comparte.** **Un
cable no se lo quita nadie y no cambia con el tiempo; un enlace radio depende del espectro, del clima
y de quién más transmita.** **Lo crítico va por cable siempre que se pueda.**

<!-- indice -->

## Índice

- [Los dos grandes grupos](#los-dos-grandes-grupos)
- [Par trenzado y coaxial](#par-trenzado-y-coaxial)
- [La fibra](#la-fibra)
- [Los conectores](#los-conectores)
- [Los sistemas de un centro](#los-sistemas-de-un-centro)
- [La compresión](#la-compresión)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los dos grandes grupos

| Familia | Qué es | Ejemplos |
|---|---|---|
| **guiados** | **la energía viaja confinada** | **par trenzado, coaxial, fibra, guía de onda** |
| **no guiados** | **la energía se radia** | **radioenlace, satélite, óptica en espacio libre** |

## Par trenzado y coaxial

- **por qué se trenza** · `[of]` · **para que el ruido entre igual en los dos hilos y se cancele al
  restarlos.** **No es blindaje: es simetría.**
- **el coaxial y su magnitud clave** · `[of]` · **la impedancia característica**: **75 ohmios en vídeo
  y 50 en radiofrecuencia.** **Encajan igual y no son intercambiables**: **el desajuste produce
  reflexiones que un equipo de medida ve y un ojo no.**
- **LA CONSECUENCIA QUE ORDENA UN CENTRO** · `[of]` · **La atenuación del coaxial crece con la
  frecuencia**, así que **el mismo cable que lleva definición estándar cientos de metros no lleva doce
  gigabits ni la décima parte.** **Al subir de grado de interfaz la longitud admisible se desploma**,
  y **eso —no el precio— es lo que empuja a la fibra y a la red.**

## La fibra

| | **Monomodo** | **Multimodo** |
|---|---|---|
| **Núcleo** | **muy fino** | **más grueso** |
| **Caminos** | **uno** | **varios a la vez** |
| **Dispersión modal** | **no la tiene** | **la tiene**: ensancha el pulso |
| **Atenuación** | **menor** | **mayor** |
| **Distancia** | **larga y muy larga** | **corta: dentro de un centro** |
| **Fuente** | **láser**, más caro | **diodo o láser de superficie**, más barato |

- **LA REGLA QUE RESUELVE LA PREGUNTA** · `[exam]` · **Para larga distancia, MONOMODO, y la razón es
  su MENOR ATENUACIÓN** —más la ausencia de dispersión modal—, **no que su recubrimiento sea más
  robusto ni que lleve varias longitudes de onda.**
- **la falsa que invierte los términos** · `[exam]` · **Llevar varias longitudes de onda a la vez es
  multiplexado por división en longitud de onda**, y **se hace precisamente sobre monomodo.**

## Los conectores

| Conector | Para qué | Rasgo que lo define |
|---|---|---|
| **BNC** | **vídeo digital en serie, radiofrecuencia** | **bayoneta, un cuarto de vuelta** |
| **HD-BNC** | **lo mismo, en alta densidad** | **más pequeño: caben más en el mismo panel** |
| **XLR de tres contactos** | **audio simétrico y digital** | **pestillo, y masa que entra primero** |
| **RJ45** | **red de datos** | **ocho contactos y lengüeta** |
| **de fibra: bayoneta, encaje y compacto** | **fibra** | **el compacto es el de alta densidad; los otros dos, de encaje y de un cuarto de vuelta** |
| **multipolar rectangular** | **instalaciones fijas y unidades móviles** | **carcasa rectangular con inserto de muchos contactos** |
| **multipolar circular** | **cámaras y equipo de campo** | **cierre de empuje y tracción, guiado por chavetero** |
| **HDMI, DVI y** ***DisplayPort*** | **monitorado e informática** | **de consumo o de informática, no de emisión** |
| **USB en sus tipos** | **datos y periféricos** | **el tipo C es reversible; los demás no** |
| **módulos enchufables** | **alojan el transceptor en el propio equipo** | **enchufables en caliente: se cambia el módulo, no el equipo** |

- **LA VENTAJA DEL DE ALTA DENSIDAD ES MECÁNICA, NO ELÉCTRICA** · `[exam]` · **No es específico de
  alta ni de ultraalta definición, ni lleva varias señales**: **ocupa menos y permite más conectores
  por panel.** **Las tres falsas atribuyen al tamaño una propiedad de la señal.**
- **un módulo enchufable no es un conector** · `[of]` · **es un transceptor**: **con él se elige la
  óptica, la longitud de onda y el alcance**, y **el mismo equipo sirve para cobre o para fibra según
  lo que se le ponga.**
- **EL AVISO DE MÉTODO SOBRE LAS PREGUNTAS CON FOTOGRAFÍA** · `[of]` · **Cuatro preguntas de este
  cuadernillo piden identificar un conector, un panel o un esquema a partir de una imagen.** **Este
  temario no describe lo que no ha visto**: **da en su lugar la regla de la familia** —cómo se reconoce
  un conector de fibra por su cuerpo, un multipolar por su carcasa y uno de bus por su sección—.

## Los sistemas de un centro

| Sistema | Qué lleva |
|---|---|
| **vídeo digital en serie por coaxial** | **una señal por cable, sin comprimir** |
| **fibra punto a punto** | **la misma señal, más lejos y sin ruido** |
| **cable de cámara con conductores mixtos** | **señal, retorno, comunicaciones, mando y ALIMENTACIÓN por un solo cuerpo** |
| **red de paquetes** | **muchas señales por el mismo enlace: temas 19 y 20** |
| **enlace inalámbrico** | **cámara sin cordón umbilical** |

- **no son cables de señal: son cordones umbilicales** · `[of]` · **Por eso una cámara de estudio se
  conecta con un cable y no con seis.**
- **la red cambia la topología, no sólo el cable** · `[of]` · **Con interfaz serie, para llevar una
  señal a tres sitios hace falta un distribuidor; con red, cualquier equipo se suscribe a cualquier
  flujo.** **Eso hace del tema 19 un cambio de arquitectura y no de medio.**

## La compresión

| Familia | Qué quita | Qué se recupera |
|---|---|---|
| **sin pérdida** | **redundancia estadística** | **lo original, bit a bit** |
| **con pérdida** | **además, lo que el ojo o el oído no aprecian** | **algo parecido**, y **degrada en cada vuelta** |

| Redundancia | Qué explota |
|---|---|
| **espacial** | **que los píxeles vecinos se parecen** |
| **temporal** | **que un cuadro se parece al anterior** |
| **estadística** | **que unos símbolos son más frecuentes que otros** |
| **perceptiva** | **que el ojo y el oído no distinguen todo lo que se les da** |

| | **Intracuadro** | **Intercuadro** |
|---|---|---|
| **Qué comprime** | **cada cuadro por separado** | **un cuadro contra sus vecinos** |
| **Grupo de imágenes** | **NO TIENE** | **sí, con referencias y predichos** |
| **Corte de montaje** | **en cualquier cuadro** | **limpio sólo en los de referencia** |
| **Eficiencia** | **menor** | **mucho mayor a igual calidad** |
| **Dónde manda** | **producción y postproducción** | **contribución, distribución y emisión** |

- **LA REGLA DE EXAMEN** · `[exam]` · **Una señal con compresión intracuadro no tiene grupo de
  imágenes.** **No es que sea de dos, de cuatro o de ocho: es que el concepto no aplica**, porque
  **cada cuadro se codifica solo.**
- **la regla de oficio del flujo** · `[of]` · **Se comprime poco y dentro del cuadro mientras el
  material se trabaja; mucho y entre cuadros cuando ya no se va a tocar.** **El número de
  recodificaciones importa tanto como la calidad de cada una.**
- **lo que sorprende** · `[of]` · **La eficiencia se paga en RETARDO.** **Un códec que predice a partir
  del cuadro siguiente necesita tenerlo**, y **eso obliga a esperar.** **Por eso un directo con vuelta
  usa códecs menos eficientes que una emisión en un solo sentido.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 2 | Característica principal del conector de bayoneta de alta densidad | **Ocupa menos y permite más conectores en el mismo espacio** ✔ **·** ventaja mecánica, no eléctrica |
| 15 | Qué conversor muestra la imagen | **La opción oficial** ✔ **·** pregunta con fotografía: el temario da la regla de la familia y no describe lo que no ha visto |
| 22 | Qué tipo de panel de conexiones muestra la imagen | **La opción oficial** ✔ **·** igual: multipolar reconocible por su carcasa |
| 41 | Por qué la fibra de larga distancia es monomodo | **Por su menor atenuación** ✔ **·** no por el recubrimiento ni por llevar varias longitudes de onda |
| 68 | Qué conector de fibra muestra la imagen | **La opción oficial** ✔ **·** el compacto es el de alta densidad |
| 76 | Qué conector de bus muestra la imagen | **La opción oficial** ✔ **·** se reconoce por la sección del cuerpo |
