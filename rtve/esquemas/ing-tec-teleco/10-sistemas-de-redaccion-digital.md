# Esquema · Tema 10 del específico de Ingeniería Técnica · Telecomunicación · Sistemas de redacción digital

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de sistemas de redacción ·
`[exam]` = opciones del propio cuadernillo. **Siglas**: la gestión de activos de medios (**MAM**) y la
de activos digitales (**DAM**); el sistema de gestión de contenido de noticias (**NRCS**); el
intercambio de material de noticias (**MOS**); el formato de intercambio de material (**MXF**); la
interfaz digital serie (**SDI**); la red de área de almacenamiento (**SAN**) y el almacenamiento
conectado a la red (**NAS**).

**Cabecera.** Enunciado: punto 14 del anexo · **3 preguntas** · **las tres de la misma mitad**: ingesta
y gestión del material · **de edición, emisión y conexión con otras salas no ha caído ninguna** · **el
aviso que ordena el punto**: **una redacción digital es un sistema informático que produce
televisión**; quien lo estudie como equipamiento de vídeo falla.

<!-- indice -->

## Índice

- [Las cuatro etapas](#las-cuatro-etapas)
- [La ingesta](#la-ingesta)
- [La gestión del material](#la-gestión-del-material)
- [Edición y emisión](#edición-y-emisión)
- [Almacenamiento y red](#almacenamiento-y-red)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las cuatro etapas

| Etapa | Qué hace | Quién trabaja ahí |
|---|---|---|
| **Ingesta** | **Meter el material**: grabar entradas y volcar tarjetas ✔ | **Operadores de ingesta** |
| **Gestión** | **Catalogar, buscar, controlar versiones** | **Documentación y todos** |
| **Edición** | **Montar las piezas** | **Redactores y montadores** |
| **Emisión** | **Poner la pieza en antena a su hora** | **Control de emisión** |

- **EL ARCHIVO NO ES UNA QUINTA** · `[of]` · **Atraviesa las cuatro**: lo que se conserva se decide en la
  primera y se ejecuta después.
- **LA REGLA QUE ORDENA EL PUNTO** · `[of]` · **Cada etapa mete el material en un sitio y las demás lo
  encuentran por sus DATOS DESCRIPTIVOS, no por su nombre de fichero.** **Ésa es la diferencia entre un
  sistema de redacción y una carpeta compartida.**

## La ingesta

- **PREGUNTA 50** · `[exam]` · **El sistema de ingesta graba las señales de entrada que se transfieren
  al almacenamiento para edición.**
- **PREGUNTA 6** · `[exam]` · **La señal de una agencia de noticias se graba en ingesta.**
- **LAS NUEVE FALSAS SON FUNCIONES DE OTRA ETAPA** · `[exam]` · **Metadatos y catalogación**: gestión ·
  **transferencia a emisión**: conformado · **incrustación de rótulos**: edición · **archivo**: guarda
  lo que ya está dentro · **redacción**: escribe y monta · **continuidad**: articula la emisión.

| Tipo de ingesta | De dónde | Rasgo |
|---|---|---|
| **En directo, desde señal** | **Agencia, satélite, unidad móvil** ✔ | **En tiempo real y NO se puede repetir** |
| **Desde soporte** | **Tarjeta o disco de cámara** | **Más rápido que el tiempo real** |
| **Desde fichero** | **Entrega por red** | **La más rápida y la que más problemas de formato da** |

- **POR QUÉ LA DIRECTA ES LA CRÍTICA** · `[of]` · **Es la única que no se puede repetir**: si falla
  mientras ocurre, no hay segunda oportunidad. **Por eso se graba por partida doble en dos sistemas
  independientes.**
- **LOS TRES DATOS QUE SE CAPTURAN** · `[of]` · **Quién lo trae, de qué es y qué derechos tiene.** **Un
  material sin esos tres está dentro del sistema y está perdido.**

## La gestión del material

- **PREGUNTA 90** · `[exam]` · **La gestión de activos de medios gestiona el vídeo y los ficheros
  multimedia del sistema de redacción.**

| Función | Qué resuelve |
|---|---|
| **Catálogo** | **Datos descriptivos y búsqueda** |
| **Versiones** | **Cuál es la buena y de dónde sale cada una** |
| **Baja resolución** | **Ver y marcar sin mover el fichero grande** |
| **Ciclo de vida** | **Cuánto se guarda y cuándo se borra o se archiva** |
| **Permisos** | **Quién ve, usa y borra qué** |

- **LA PALABRA QUE DECIDE** · `[of]` · **«Gestión»**: de las cuatro opciones, **sólo una nombra una
  función transversal y no un paso concreto.**
- **LA PIEZA QUE LO HACE POSIBLE** · `[of]` · **La copia de baja resolución**: **cada material se
  transcodifica al entrar**, y es esa versión la que **viaja por la red ofimática, se ve en el
  navegador y se marca.** **Sin ella, doscientas personas necesitarían red de vídeo en cada mesa.**
- **LA DISTINCIÓN DE VOCABULARIO** · `[of]` · **Activos DIGITALES es el término general** —fotos,
  documentos, audio—; **activos de MEDIOS es el especializado en audiovisual**: código de tiempo,
  subclips, versiones de montaje y derechos por ventana.

## Edición y emisión

| Nivel de edición | Quién | Sobre qué |
|---|---|---|
| **Ligera, en el puesto** | **El redactor** | **La copia de baja resolución** |
| **Completa, en sala** | **El montador** | **La alta resolución** |

- **EL CONFORMADO** · `[of]` · **La lista de decisiones tomada sobre la copia ligera se aplica al
  material grande.** **Es automático, y ahí aparecen los fallos si los códigos de tiempo no coinciden.**

| Pieza de emisión | Qué hace |
|---|---|
| **Escaleta** | **Dice qué sale y en qué orden**, y viene del sistema de redacción |
| **Servidor de emisión** | **Reproduce en el instante previsto** |
| **Automatización** | **Ejecuta la escaleta: servidor, grafismo y conmutación** |

- **EL PRINCIPIO DE DISEÑO** · `[of]` · **La emisión se separa de todo lo demás**: servidores propios,
  almacenamiento propio y red propia, **porque es el único punto donde un fallo se ve en antena.**
- **LA CONEXIÓN CON OTRAS SALAS** · `[of]` · **Es de dos clases**: **la de SEÑAL, por matriz o por red**,
  y **la de DATOS, por la red informática**, que lleva escaletas, estados y órdenes y **es la que más ha
  crecido.**

## Almacenamiento y red

| | **De producción** | **De archivo** |
|---|---|---|
| **Qué guarda** | **Lo que está en uso** | **Lo que se conserva** |
| **Acceso** | **Inmediato, por red de bloques** | **Diferido: puede estar en cinta** |
| **Coste por terabyte** | **Alto** | **Bajo** |
| **Qué lo dimensiona** | **Cuánto material vivo hay a la vez** | **Cuánto y cuánto tiempo** |

| Red | Qué lleva | Por qué separada |
|---|---|---|
| **De señal** | **Vídeo y audio en tiempo real** | **Caudal enorme y sensible al retardo** |
| **De producción** | **Ficheros, baja resolución, control** | **Caudal alto a ráfagas** |
| **Ofimática** | **Correo, navegación, gestión** | **Es la expuesta a internet** |

- **LA RAZÓN DE LA SEPARACIÓN** · `[of]` · **La red ofimática es la que recibe el correo con el adjunto
  malicioso.** **Si la producción cuelga de ella, un incidente de seguridad puede parar la emisión.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 6 | Dónde se graba la señal de una agencia | **Ingesta** ✔ |
| 50 | De qué se encarga el sistema de ingesta | **Grabar las señales de entrada para edición** ✔ |
| 90 | Qué hace la gestión de activos de medios | **Gestionar el vídeo y los ficheros multimedia** ✔ |
