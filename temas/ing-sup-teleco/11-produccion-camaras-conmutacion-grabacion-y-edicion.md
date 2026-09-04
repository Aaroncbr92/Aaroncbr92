# Tema 11 del específico de Ingeniería Superior · Telecomunicación · Elementos de producción (I): cámaras, ópticas, conmutación, grabación y edición

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Ing. Superior Telecomunicación · punto 11 |
| **Sirve para** | **Ing. Superior Telecomunicación** |
| **Fuente** | **Sin norma: no la hay.** Su materia son las cámaras, la conmutación y la edición, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma se cita literalmente en este tema** |
| **Lo que hace un plató** | **No es la cámara: es la IGUALACIÓN.** Dos cámaras del mismo modelo con la misma luz no dan la misma imagen si no se igualan |
| **Extensión** | **2.693 palabras** |

<!-- /portada -->

Las siglas y símbolos de este tema, presentados de entrada: la unidad de control de cámara (**CCU**);
el panel de control remoto (**RCP**) y el panel maestro de configuración (**MSU**); el dispositivo de
carga acoplada (**CCD**) y el sensor de semiconductor complementario (**CMOS**); la interfaz de entrada
y salida de propósito general (**GPI**, *general purpose interface*); el audio que sigue al vídeo
(**AFV**, *audio follow video*); la interfaz digital en serie (**SDI**); el cable de triple malla
(**triax**); la relación entre apertura y focal (**número f**); el rango dinámico en pasos de
diafragma (**stops**); el código de tiempo (**TC**); la edición no lineal (**NLE**); la lista de
decisiones de montaje (**EDL**); y el material de origen y su copia de trabajo (**proxy**).

> Enunciado del programa (Anexo 2 de la convocatoria 1/2022, temario específico de la ocupación tipo
> de Ingeniería Superior · especialidad Telecomunicación, punto 11):
> «Elementos de producción (I): Cámaras, ópticas y elementos de suspensión. Cadenas de cámaras.
> Sistemas de conmutación de señales de vídeo, audio y datos. Equipos, sistemas y formatos de
> grabación. Equipos y sistemas de edición y postproducción. Transmisión cableada (Triax y Fibra) y
> transmisión inalámbrica.»

**Es el primero de los ocho puntos de «elementos de producción» del anexo**, y **conviene decir cómo se
reparten**: **el I trae la imagen y la conmuta; el II trae el sonido, la luz y la medida; del III al V
están las salas; el VI, los informativos; el VII, la postproducción; y el VIII, el grafismo.**

**Y la idea que ordena este punto**: **una cámara de estudio no es una cámara: es el extremo de una
CADENA.** **La óptica, el cuerpo, el cable, la unidad de control y el panel del operador de control de
imagen son un solo aparato repartido por el edificio**, y **todo lo que aquí se estudia se entiende
mejor así.**

<!-- indice -->

## Índice

- [1. La cadena de cámara](#1-la-cadena-de-cámara)
- [2. La óptica](#2-la-óptica)
- [3. El sensor](#3-el-sensor)
- [4. Los elementos de suspensión](#4-los-elementos-de-suspensión)
- [5. La conmutación](#5-la-conmutación)
- [6. La grabación y la edición](#6-la-grabación-y-la-edición)
- [7. Transmisión cableada e inalámbrica](#7-transmisión-cableada-e-inalámbrica)
- [8. Trazabilidad](#8-trazabilidad)

<!-- /indice -->

## 1. La cadena de cámara

**Sus piezas, del objeto a la señal:**

| Pieza | Qué hace |
|---|---|
| **ÓPTICA** | **Forma la imagen sobre el sensor** y decide encuadre, profundidad y luminosidad |
| **Bloque óptico y SENSOR** | **Convierte la luz en señal eléctrica** |
| **Cabeza de cámara** | **Procesa, codifica y manda**; lleva visor, intercomunicación y señalización |
| **CABLE**: triax o fibra | **Señal, retorno, comunicaciones, mando y ALIMENTACIÓN**, en un solo cordón |
| **UNIDAD DE CONTROL** | **El otro medio aparato**: alimenta, recupera la señal, procesa y la entrega a la instalación |
| **PANEL de control remoto** | **Donde el control de imagen ajusta diafragma, negros y matriz** |
| **Panel maestro** | **Configuración y ajuste fino** de todas las cámaras a la vez |

**Y las dos observaciones que hay que hacer de esa tabla:**

1. **El operador de cámara encuadra y enfoca; el de CONTROL DE IMAGEN expone e iguala.** **Son dos
   personas y dos puestos**, y **la razón es que la exposición y el color tienen que ser los mismos en
   todas las cámaras del plató**: **eso no se puede hacer desde el visor.**
2. **Igualar cámaras es la tarea invisible de un plató.** **Dos cámaras del mismo modelo con la misma
   luz no dan la misma imagen si no se igualan**, y **un corte entre dos cámaras desiguales se ve
   inmediatamente.**

## 2. La óptica

**Los parámetros que hay que manejar:**

| Parámetro | Qué decide |
|---|---|
| **DISTANCIA FOCAL** | **El ángulo de visión**: corta abre, larga cierra |
| **Rango de zum** | **Cuánto varía esa focal** |
| **APERTURA máxima** | **Cuánta luz entra**: decide con qué luz se puede trabajar |
| **PROFUNDIDAD DE CAMPO** | **Cuánto queda enfocado por delante y por detrás del punto de enfoque** |
| **Distancia mínima de enfoque** | Cuánto se puede acercar |
| **Extensor** | **Multiplica la focal** a costa de luminosidad |

**Las tres reglas que gobiernan la profundidad de campo, y hay que saberlas juntas porque siempre se
preguntan combinadas**: **la profundidad DISMINUYE al abrir el diafragma, al alargar la focal y al
acercarse al motivo.** **Y crece con el tamaño del sensor en el sentido contrario al que la intuición
dice**: **a igual encuadre, un sensor mayor da menos profundidad de campo.**

**Y la advertencia de oficio sobre el zum**: **un zum no es un travelín.** **El zum cambia el ángulo de
visión y comprime la perspectiva; el travelín cambia el punto de vista.** **Confundirlos es un error de
lenguaje que un ingeniero no debe cometer al hablar con realización.**

## 3. El sensor

**Los parámetros que definen a un sensor:**

| Parámetro | Qué es |
|---|---|
| **TAMAÑO** | **La superficie sensible**, en pulgadas de designación heredada |
| **Número de PÍXELES** | La rejilla |
| **TAMAÑO del píxel** | **Superficie del sensor dividida por número de píxeles** |
| **SENSIBILIDAD** | **Cuánta señal da con poca luz** |
| **RANGO DINÁMICO** | **Cuántos pasos de diafragma hay entre el ruido y la saturación** |
| **Tipo de obturación** | **Global o por barrido**, con su artefacto característico |

**La relación que un examen pregunta directamente y que hay que saber razonar**: **a igual número de
píxeles, un sensor MÁS GRANDE ofrece generalmente MAYOR rango dinámico**, y **la razón es que cada
píxel es más grande y por tanto CAPTA MÁS LUZ**: **recoge más señal antes de saturarse y su ruido
relativo es menor.**

**Y las tres opciones falsas de esa pregunta, con por qué lo son**: **decir que el tamaño no influye
porque el rango es un parámetro «del proceso optoelectrónico» separa artificialmente el sensor de su
física; decir que un sensor más pequeño da MÁS rango porque sus píxeles pequeños son más sensibles
invierte la relación** —un píxel pequeño capta menos luz, no más—; **y decir que lo que influye es la
resolución temporal confunde dos parámetros que no tienen que ver.**

**Y el aviso de oficio sobre la obturación por barrido**: **un sensor que lee la imagen línea a línea
deforma lo que se mueve deprisa y parte los flashes.** **En una cámara de estudio no suele importar; en
una de acción o en una que graba pantallas, sí.**

## 4. Los elementos de suspensión

**El enunciado los nombra y suelen olvidarse:**

| Elemento | Qué aporta |
|---|---|
| **TRÍPODE con rótula fluida** | **Movimiento amortiguado y repetible** |
| **PEDESTAL de estudio** | **Altura ajustable con compensación de peso** y desplazamiento suave |
| **Plataforma rodante y travelín** | **Desplazamiento sobre ruedas o raíles** |
| **GRÚA y brazo** | **Movimiento en altura y en arco** |
| **CABEZA CALIENTE o robotizada** | **Movimiento MOTORIZADO de la cabeza**, con control remoto |
| **Estabilizador corporal y cardán** | **Cámara en movimiento sin vibración** |
| **Cámara sobre cable** | **Vuelo sobre un recinto**, en deportes y espectáculos |

**Y la pregunta que un examen hace de esto, con su razonamiento**: **si hay que controlar el movimiento
de una cabeza de cámara y además el foco y el zum de su óptica, sin operador delante, el sistema es de
ROBOTIZACIÓN.** **No un «sistema de movimiento axial» ni una «rotación neumática», que no son
categorías de este oficio, ni un sistema de monitorización, que observa y no mueve.**

**Las tres cosas que un sistema de robotización necesita y que conviene saber:**

1. **Control de la CABEZA** —giro horizontal y vertical— **y de la ÓPTICA** —zum, foco y a veces
   diafragma—.
2. **MEMORIAS de posición.** **Poder volver exactamente al mismo encuadre es lo que lo hace útil en un
   informativo diario.**
3. **Protección contra COLISIÓN.** **Una cabeza robotizada que no sabe dónde está el decorado lo
   golpea**, y **eso obliga a límites programados.**

## 5. La conmutación

**El enunciado dice «de señales de vídeo, audio y datos», y esa terna es lo que hay que separar:**

| Equipo | Qué conmuta | Cuándo |
|---|---|---|
| **MEZCLADOR de producción** | **Vídeo, con transiciones y efectos** | **En directo, para producir un programa** |
| **MATRIZ de conmutación** | **Señales, punto a punto, sin efecto** | **Para encaminar**: qué llega a dónde |
| **Matriz de audio** | Igual, con audio | |
| **Matriz de datos y de control** | Igual, con señales de mando | |
| **Matriz de teclado, vídeo y ratón** | **Los puestos de trabajo informáticos** | **Para que un puesto maneje varias máquinas** |

**La distinción que hay que dejar clara**: **un mezclador PRODUCE y una matriz ENCAMINA.** **El
mezclador tiene barras de programa y previo, transiciones, incrustadores y efectos; la matriz sólo
conecta una entrada con una salida**, y **su virtud es no tocar la señal.**

**Y el AUDIO QUE SIGUE AL VÍDEO, que es la pregunta**: **es un modo de operación asociado a los
CONMUTADORES DE VÍDEO Y AUDIO**, y **consiste en que al conmutar una fuente de vídeo se conmuta con
ella su audio asociado.** **No es un modo de las cámaras, ni del sistema de multipantalla, ni de los
servidores de grabación.** **Su utilidad es evidente en un directo**: **quien pincha imagen no tiene
que acordarse de pinchar el sonido.**

**Y la señal de disparo, que es la otra pregunta del punto**: **la interfaz de propósito general es una
SEÑAL DE DISPARO.** **Un contacto que se cierra o un nivel que cambia**, sin más contenido: **no es un
sincronismo, ni radiofrecuencia, ni audio.** **Sirve para que un equipo le diga a otro «ahora»**:
arranca la grabación, lanza el vídeo, cambia el rótulo, enciende el piloto.

**Las dos reglas de oficio sobre esas señales:**

1. **Son la interconexión más barata y la más frágil.** **Un contacto suelto no da error, sencillamente
   no dispara**, y **el fallo aparece en directo.**
2. **En una instalación sobre red, ese contacto se sustituye por un mensaje.** **Se gana registro y
   diagnóstico y se pierde la inmediatez del cable**, y **por eso los disparos críticos se siguen
   cableando.**

## 6. La grabación y la edición

**Los soportes, por generación:**

| Soporte | Rasgo |
|---|---|
| **CINTA** | **Acceso secuencial**: hay que rebobinar. **Sobrevive en archivo por su coste y su vida** |
| **Disco óptico** | Acceso directo y robustez de manipulación |
| **TARJETA de estado sólido** | **Sin partes móviles, rápida y frágil ante el borrado accidental** |
| **SERVIDOR de producción** | **La grabación es un fichero en una cabina**: es lo que domina hoy |

**Lo que hay que saber decir del paso de la cinta al fichero, porque es la clave del oficio actual**:
**con cinta, el material ESTÁ en un sitio y hay que llevarlo; con fichero, el material está DISPONIBLE
y lo que hay que gestionar son permisos, catálogo y copias.** **El trabajo se traslada del transporte a
la gestión**, y **por eso los temas 14, 18 y 19 existen.**

**La edición no lineal, con sus conceptos:**

| Concepto | Qué es |
|---|---|
| **INGESTA** | **Meter el material en el sistema**, con sus metadatos |
| **Copia de trabajo ligera** | **Una versión de baja tasa para montar sin mover el original** |
| **LÍNEA DE TIEMPO** | Donde se ordena el montaje |
| **Lista de decisiones** | **El montaje descrito por referencias al original**, sin medios |
| **CONFORMADO** | **Rehacer el montaje sobre el material de alta calidad** |
| **RENDERIZADO** | Calcular lo que no se puede reproducir al vuelo |

**Y las dos reglas que ordenan un flujo de trabajo con copias ligeras:**

1. **El original NO se toca.** **Se monta sobre la copia y se conforma al final**, y **eso protege el
   material y permite trabajar sin ancho de banda.**
2. **El código de tiempo es lo que ata las dos.** **Si la copia y el original no comparten código de
   tiempo, el conformado no cuadra**, y **ése es el fallo más frecuente de una ingesta mal
   configurada.**

## 7. Transmisión cableada e inalámbrica

**Lo que el enunciado cierra**, y **que enlaza con el tema 4:**

| Sistema | Qué lleva | Su límite |
|---|---|---|
| **TRIAX** | **Todo el cordón umbilical por un coaxial de triple malla** | **Distancia y ancho de banda**: es tecnología madura |
| **FIBRA híbrida** | **Lo mismo, con fibras y conductores de fuerza** | **Manipulación**: el conector es delicado y hay que limpiarlo |
| **Cámara INALÁMBRICA** | **Enlace de radio o de milimétricas** | **Espectro, latencia y interferencia**: hay que coordinar frecuencias |

**Y las dos observaciones de oficio:**

1. **Un cordón umbilical es una decisión de instalación, no de cámara.** **Cambiar de triax a fibra en
   un plató es una obra**, y **por eso conviven los dos durante años.**
2. **Lo inalámbrico se PLANIFICA.** **Un directo con varias cámaras sin cable, micrófonos
   inalámbricos e intercomunicación necesita un plan de frecuencias**, y **improvisarlo es como se
   pierde una señal en el peor momento.**

## 8. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Primero: norma del BOE en vigor a la fecha de corte** | **NINGUNA** | **Este punto no nombra ninguna norma y no hay ninguna que lo sostenga** |

**El aviso de método sobre este punto sin norma es el del tema 3 y vale aquí.**

**Cinco declaraciones expresas:**

1. **Este tema NO da ninguna distancia focal, ningún número f, ningún tamaño de sensor, ningún rango
   dinámico en pasos, ninguna distancia máxima de triax y ninguna frecuencia de enlace inalámbrico.**
   **Son dato de fabricante y de plan de frecuencias**, y **una cifra que no se ha leído en su fuente
   no se escribe.** **Lo que el temario da es en qué sentido influye cada variable.**
2. **Este tema NO nombra ningún fabricante, ningún modelo de cámara, ningún formato de grabación por
   su nombre comercial y ningún programa de edición.**
3. **Las tres respuestas que la plantilla oficial de esta ocupación confirma —el modo de audio que
   sigue al vídeo como propio de los conmutadores, el sensor mayor como el de mayor rango dinámico y
   la interfaz de propósito general como señal de disparo— se recogen con su razonamiento**, y **el
   temario declara que la confirmación viene de la plantilla, en las preguntas 40, 60 y 95.**
4. **La relación entre tamaño de sensor y rango dinámico se enuncia con la cautela con que la enuncia
   la propia pregunta —«generalmente»—**, porque **depende también de la tecnología del sensor**, y
   **el temario no afirma que sea una ley sin excepción.**
5. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **los medios
   y conectores, al tema 4**; **el sonido y la iluminación, al tema 12**; **las salas y su
   interconexión, al tema 13**; **la ingesta y los informativos, al tema 14**; **la postproducción, al
   tema 15**; **y el almacenamiento, al tema 18.**

**El resto del tema va como oficio y así se declara**: la lectura del reparto de los ocho puntos de
elementos de producción, la idea de que una cámara de estudio es el extremo de una cadena repartida por
el edificio, la separación entre el operador de cámara y el de control de imagen y la observación de
que igualar cámaras es la tarea invisible del plató, las tres reglas de la profundidad de campo con la
nota sobre el tamaño de sensor, la advertencia de que un zum no es un travelín, el razonamiento sobre
el rango dinámico del sensor y el descarte de las tres opciones falsas, el aviso sobre la obturación
por barrido, las tres cosas que necesita un sistema de robotización, la distinción entre mezclador y
matriz, la explicación del modo de audio que sigue al vídeo, las dos reglas sobre las señales de
disparo, la lectura del paso de la cinta al fichero como traslado del transporte a la gestión, las dos
reglas del flujo con copias ligeras y las dos observaciones sobre el cordón umbilical y la
planificación de lo inalámbrico. **Nada de eso está en un boletín oficial ni en ninguna fuente
consultada para este proyecto**, y el tema no lo presenta como si lo estuviera.
