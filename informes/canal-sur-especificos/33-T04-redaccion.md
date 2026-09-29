# Realizador/a (puesto 33) · Tema 4 · Fase 2, redacción

Fecha de trabajo: 24-09-2026. Tema: `temas/canal-sur-especificos/33-realizador-a/04-organizacion-control-realizacion.md`
(12.814 palabras según `indice.py`, 52 epígrafes; `refutar_prosa.py`: 1 hallazgo, la sigla CCU en el
título, que es el enunciado literal y no se toca).

Material: `33-investigacion-B-control-directo.md` (4.1 prompter Autocue, 4.2 DMX512, 4.3 RD 1680/2011;
de 12.2, Vizrt) y los cuatro temas de RTVE de `realizacion.tsv` (fila 33/4, 65 %, sin actualizar). Lo
propio de la RTVA se ha leído en sus fuentes el 24-09-2026: fichas del convenio 5351000, 5353000,
5352000 (p. 115), 5342100 (p. 209), 5342101 (p. 186), 5212207 (p. 188), 5341112 (p. 132), 5341111
(p. 133), 5345100 (p. 129), 5302010 (p. 125) en `x-convenio-rtva-boja-240-2014.txt`; RD 1680/2011
(módulos 0905 y 0910) en `fuentes/canal-sur/realizador/BOE-A-2011-19599.txt` (cada cita comprobada por
búsqueda literal); IMS077_3 en `incual-IMS077_3.txt` (CR5.2 y contexto de UC0216_3; CR2.3, CR2.5,
CR2.6, RP3, CR3.1, CR3.3-3.5 y contexto de UC0217_3; CE1.5, CE1.7 y contenidos de MF0217_3). Las citas
de Autocue, ANSI E1.11-2024 y Vizrt vienen de la investigación (leídas allí el 29-09-2026) y no se han
podido releer aquí: las verifica la fase 3.

## Decisiones

- Tema técnico sin norma jurídica: la columna vertebral son las fichas del convenio (quién hace qué en
  el control) y el RD 1680/2011 (lista de equipos y esquema de intercomunicación, 0910 RA 4.d, que da
  los nueve puntos del intercom). No hay lentes de normas que pasar; sólo `refutar_prosa.py` e
  `indice.py`.
- Hallazgo del convenio no recogido en la investigación: el control de cámaras está en las fichas del
  Técnico Electrónico (5342100) y del Oficial Técnico Electrónico (5342101), con tareas idénticas; no
  hay ficha llamada «control de imagen». Tampoco hay ficha de operador de prompter, titulador ni
  servidor: se declara en «Lo que este tema no da».
- De RTVE se quitan todas las preguntas, plantillas, cuadernillos, erratas de examen y la pregunta
  defectuosa 47; el cableado del plató de tres *sets* (pregunta 41); las condiciones del estudio (tema
  5); la gestión de pantallas y su retardo (tema 12); el artículo 156 de la Ley 13/2022 (fuera de la
  rúbrica); la tabla de marcas de grafismo (Vizrt «el más extendido», Chyron, Ventuz, Unreal: RTVE
  declara no haber consultado a los fabricantes; se deja sólo la distinción After Effects/tiempo real,
  como oficio); EVS como marca; la fórmula de la pregunta 74 (se deja el uso de la GPI como oficio).
- «El protocolo más extendido para iluminación» (RTVE) se sustituye por «el protocolo normalizado»:
  lo de «más extendido» no tiene fuente. Se quita la mención a RS-485 (no está en la norma: la norma
  cita ANSI/TIA/EIA-485A-1998).
- El «broadcast standard 70:30» se da como del fabricante, con la advertencia de la investigación.
- Remisiones: transiciones, llaves, DVE, sincronismos → tema 9; IFB en detalle, N-1, dos/cuatro hilos,
  intercom IP → tema 11; pantallas, rotulación, zonas seguras → tema 12; órdenes y cambios de escaleta
  en el prompter → tema 6; MOS en detalle → temario de Operador/a Montador/a de Vídeo.

## Copiado del común

Epígrafes y pasajes copiados literal de temas ya cerrados de Canal Sur (comprobado por script que cada
párrafo o fila está en el origen):

De `temas/canal-sur-especificos/28-operador-a-de-sonido/08-sonido-en-television.md`:
- «### El control de sonido y sus tres salidas»: primer párrafo, tabla y el párrafo «La regla que las
  separa…», sin su última frase («El resto del tema desarrolla…»). En «4. Sonido».
- «### Quién manda en el control»: los dos primeros párrafos (LE 6.5, p. 92, y «El sonido de la
  emisión entra en esa responsabilidad…»), literales. En «4. Sonido».
- «### Qué es y para qué sirve» (intercom): los dos párrafos, literales, bajo «### El intercom».
- «### La matriz, el panel y el confidente»: los tres primeros párrafos, literales (se quita el cuarto,
  del panel del operador de sonido).
- «### El intercom de cámaras»: entero, literal.
- «### IFB e intercom no son lo mismo»: el párrafo «La diferencia con el intercom…» y la tabla,
  literales (se quita el párrafo final sobre sonido).
- De «### Lo que una cámara recibe del control»: el párrafo del manual ATEM sobre el piloto y la
  llamada (CALL), literal, en «### El piloto»; y la frase citada **«El mezclador permite controlar
  unidades URSA Mini…»** con su paréntesis, en «### Los retornos».
- De «### La línea compartida»: las dos citas de Clear-Com (con lead propio).
- De «### El directo se pacta antes»: la cita del LE 8.3 (con lead propio), en «### La comunicación de
  los cambios».

De `temas/canal-sur-especificos/08-camara-operador/09-calidad-tecnica-de-imagen.md`:
- «### Quién responde de ella»: primer párrafo, tabla y segundo párrafo, literales, bajo «### El
  control de imagen: quién responde de la imagen» (no el tercero, del LE).
- «### Los instrumentos de medida»: primer párrafo, tabla y «La regla que separa los dos primeros…»,
  literales (sin la frase de la Sony PXW-Z200).

De `temas/canal-sur-especificos/34-redactor-a/09-presentacion-locucion-comunicacion-oral.md`:
- «### Qué es» (§ 6, prompter): el primer párrafo, literal (no el segundo, de costumbre de oficio,
  sustituido por la documentación de Autocue).

De `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/13-automatizacion-plantillas-mam-newsroom-flujos.md`:
- «### El protocolo MOS»: el primer párrafo, literal, en «### Redacción, servidores y escaleta».
- Las citas del LE 6.1 («Cualquier cambio del contenido de la escaleta…», p. 88), 6.1.1 («Son
  inadmisibles…», p. 88) y 6.1.2 («El redactor ha de ﬁjar siempre…», p. 89), con lead propio.

De `temas/canal-sur-especificos/08-camara-operador/04-soportes-y-accesorios.md`: la frase del
teleprompter y el equilibrio de la columna, adaptada («Y un efecto sobre la cámara: si se cambia…»).
Es adaptación, no copia: se verifica.

## Copiado de RTVE sin cambios

Palabras sin tocar; sólo se han quitado las negritas de énfasis. Lo que no está en esta lista y viene
de RTVE está adaptado (frase de examen quitada, remisión de tema cambiada, lead añadido) y sí se
verifica. Comprobado por script contra los cuatro ficheros.

`temas/realizacion/11-el-estudio-controles-y-plato.md`:
- §1: «La distinción importa en el oficio: el plató es donde se rueda…».
- §3: «Un estudio de televisión tiene varios controles…» y la tabla de controles entera.
  (Adaptada: «Los cuatro primeros son del estudio…», sin la remisión a la pregunta del tema 14.)
- §4: las dos cadenas, «Y en sentido contrario, el retorno:» y «El cable de cámara lleva las dos
  direcciones…».
- §5: «La caja de plató es el panel de conectores…» y «Por qué existe la caja de plató…».
- §6: «La unidad de control de cámara —CCU— es el aparato…», sus tres puntos, y «Las CCU viven en el
  control…».
- §7: «El retorno es la señal que el control devuelve al plató…», la tabla de retornos y «La señal de
  retorno enviada desde el mezclador… en el aire.» (Adaptado: «Por qué importa que sea
  configurable…», sin «del tema 10».)
- §8: los tres puntos de «Va en tres sitios a la vez» y, dentro del párrafo de las ventanas, desde «La
  razón es la definición misma…» hasta el final. (Adaptados: la definición del piloto y el lead de
  las ventanas.)

`temas/realizacion/10-el-mezclador-de-video.md`:
- §1: «Un mezclador de vídeo hace tres cosas…», los tres puntos y «Todo lo demás…» (sin la frase
  final «De ahí el epígrafe 16», quitada).
- §2: las tres viñetas (panel, mezclador, efectos), el párrafo «Arquitectura modular…» y la tabla de
  módulos.
- §5: «Un bus auxiliar es una salida…», la cita del manual ATEM y «Para qué sirven en un plató…».
- §6: la tabla de salidas y «La salida limpia existe porque…».
- §16: «Dos señales de vídeo sólo se pueden conmutar…», «El aparato que las genera…», «Y para lo que
  no se puede sincronizar…» y la cita del resincronizador. (Adaptado: «El precio del sincronizador…».)
- §17: «Un control de realización no es sólo el mezclador…» y «La GPI —interfaz de propósito
  general—…». (Adaptado: el párrafo del piloto, con remisión al epígrafe 8.)

`temas/realizacion/15-la-emision-pantallas-servidores-y-grafismo.md`:
- §4: «Un servidor de vídeo es un disco duro…» y la tabla de funciones. (Adaptado: «Lo que un servidor
  no hace…».)
- §6: «La continuidad es el área que emite el canal…», «Lo que sale de continuidad:» y sus cinco
  viñetas.
- (Adaptados: el titulador de §5, con remisión al tema 9, y la frase de After Effects, con lead propio.)

`temas/realizacion-tv/18-produccion-de-programas-directos-y-grabados.md`: nada copiado directamente
(su § 3 de intercom se toma de la versión ya cerrada en Canal Sur, 28-08).

## Ficheros tocados

- Creado: `temas/canal-sur-especificos/33-realizador-a/04-organizacion-control-realizacion.md`.
- Creado: este informe.
- Ninguno más. Un script de comprobación en el scratchpad, fuera del repositorio.

## Diez preguntas de tribunal, contestadas con el tema

| # | Pregunta (rúbrica) | Respuesta | Dónde | ¿Entera? |
|---|---|---|---|---|
| 1 | Según el X Convenio de la RTVA, ¿qué puesto tiene como tarea «Realizar la mezcla de programas en el control de realización»? (organización / mezclador) | Ayudante Técnico Mezclador (5352000) | Quién ocupa cada puesto; 1, Qué es un mezclador | Sí |
| 2 | ¿Qué salida del mezclador lleva lo mismo que el programa pero sin mosca ni rótulos, y quién la pide? (mezclador) | La limpia (*clean feed*); quien reemite la señal: otra cadena, una plataforma, un archivo | 1, Las salidas | Sí |
| 3 | ¿Qué tres cosas hace la CCU y qué fichas del convenio tienen la tarea «Realizar el control de cámaras»? (CCU) | Alimenta, procesa y sincroniza, permite el ajuste remoto; Técnico Electrónico y Oficial Técnico Electrónico | 2, Qué es la CCU; El control de imagen | Sí |
| 4 | Según la IMS077_3, ¿quién pagina la tituladora del control y a solicitud de quién? ¿Qué ficha diseña el grafismo? (grafismo) | La asistencia, a solicitud de dirección y/o realización y con las directrices del realizador (CR3.5); el Grafista (5345100) | 3, El grafismo en el control; Diseñar, rellenar y lanzar | Sí |
| 5 | ¿Qué tres familias de señales gobierna el control de sonido y qué regla las separa? ¿Qué es «audio sigue vídeo»? (sonido) | Programa, retornos, intercomunicación; nada del intercom al programa y el retorno de quien habla desde fuera sin su propia voz; el sonido de una fuente se abre y cierra con su imagen al conmutarla | 4, El control de sonido y sus tres salidas | Sí |
| 6 | En el DMX512 (ANSI E1.11-2024), ¿cuántos canales de datos tiene un universo, qué es el slot 0 y qué conector usa? (iluminación) | 512 slots de datos; el START Code; XLR de cinco polos | 5, El DMX512 | Sí |
| 7 | En un prompter, ¿por qué se invierte la imagen del monitor, qué proporción de luz deja pasar el cristal de Autocue y por qué lleva piloto propio? (prompter) | Para que el reflejo se lea al derecho; 70 % pasa, 30 % se refleja (proporción del fabricante); porque la capucha tapa el piloto de la cámara | 6, Cómo funciona | Sí |
| 8 | ¿Cuál de estas funciones no la hace un servidor de vídeo: repetición, lista de emisión, bloque publicitario, corrección de color? ¿Qué es el protocolo MOS? (servidores) | Corrección de color; protocolo de comunicación entre los sistemas de redacción y los servidores de objetos de medios (vídeo, audio, imágenes fijas, generadores de caracteres) | 7, El servidor de vídeo; El protocolo MOS | Sí |
| 9 | Según el RD 1680/2011, ¿entre qué puestos se diseña el esquema de intercomunicación del control? ¿Qué es el confidente? (comunicaciones) | Realización, cámaras, regiduría, mesa de audio, reproducción y grabación de vídeo, control de cámaras, control de iluminación, grafismo y conexiones exteriores (0910, RA 4.d); una escucha permanente de un punto sin pulsar | 8, El esquema; La matriz, el panel y el confidente | Sí |
| 10 | Práctica: en el ensayo la cámara 3 no casa con las demás y después se hacen unas ventanas con tres cámaras. ¿A quién se pide la corrección, cómo habla el control de imagen con esa cámara sin interrumpir al resto, y en qué cámaras se enciende el piloto? (CCU, comunicaciones, aplicación práctica) | Al control de cámaras, no al operador; con el aislamiento de cámara; en las tres | 2, El control de imagen; 8, El intercom de cámaras; El piloto; Aplicación práctica | Sí |

Resultado: diez de diez enteras. No hizo falta ampliar el tema.
