# Esquema · Tema 21 del específico de Realización Televisión · Realización online y transmedia

Telegrama. **Cada línea lleva delante de dónde sale**: `[fab]` = documentación de fabricante, citada
literal · `[of]` = oficio de producción virtual y teoría de la narrativa transmedia · `[plan]` =
plantilla oficial.

**Cabecera.** Enunciado: «4.9. Nuevas herramientas y sistemas de producción y realización on line.
Estrategia trasmedia» · **7 preguntas** · **el punto MÁS MODERNO del anexo** · **CUATRO son tecnología
de plató virtual y TRES son narrativa inmersiva.** **Las siete comparten una idea: LA IMAGEN QUE SE
EMITE YA NO ES SÓLO LA QUE ENTRA POR EL OBJETIVO.**

<!-- indice -->

## Índice

- [Virtual, aumentada y mixta](#virtual-aumentada-y-mixta)
- [El seguimiento de cámara: Mo-Sys](#el-seguimiento-de-cámara-mo-sys)
- [Cuántos motores de render](#cuántos-motores-de-render)
- [El foreground con un solo motor](#el-foreground-con-un-solo-motor)
- [El storyworld](#el-storyworld)
- [El agency](#el-agency)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Virtual, aumentada y mixta

| Tecnología | Qué hace con el entorno real |
|---|---|
| **Realidad virtual (RV)** | **LO SUSTITUYE ENTERO** |
| **Realidad aumentada (RA)** | **LO CONSERVA y le añade objetos ENCIMA** |
| **Realidad mixta (RM)** | **Lo conserva y le añade objetos QUE INTERACTÚAN CON ÉL**: se ocluyen detrás de lo real |

- **PREGUNTA 69** · `[of]` · **La RA permite INTERACTUAR con elementos virtuales en tiempo real DENTRO
  de una transmisión en directo; la RV SUSTITUYE COMPLETAMENTE el entorno.**
- **UNA SOLA COMPROBACIÓN LAS SEPARA**: **¿QUEDA ALGO DEL MUNDO REAL?** **En RA, sí. En RV, no.**
- **LA FALSA c) INVIERTE LOS TÉRMINOS**: **es la respuesta correcta puesta del revés**, y **es el
  distractor más frecuente de todo el cuadernillo.**
- **PREGUNTA 91** · `[plan]` · **La fotografía es de REALIDAD MIXTA.** **Depende de una imagen.**
  **Regla de familia**: **1)** si no se ve el plató, VIRTUAL · **2)** si se ve y el objeto virtual queda
  SIEMPRE DELANTE, AUMENTADA · **3)** si lo real PUEDE TAPAR a lo virtual —oclusión, sombra, apoyo en el
  suelo—, MIXTA. **LA OCLUSIÓN ES LA FIRMA.**
- **«REALIDAD INVERSA» NO EXISTE**: **descartar una opción por no nombrar nada es tan válido como
  reconocer la buena.** **Este cuadernillo lo permite dos veces: aquí y con la «perla» del tema 16.**

## El seguimiento de cámara: Mo-Sys

- **PREGUNTA 30** · `[fab]` · **Permite UNA INTEGRACIÓN PRECISA DE GRÁFICOS EN TIEMPO REAL en entornos
  virtuales y aumentados.**
- **LA DOCUMENTACIÓN DEL FABRICANTE LO DICE, LITERAL**: **«…combine ‘absolute’ marker-based tracking
  (StarTracker)… to deliver accurate, real-time tracking. Supporting AR graphics workflows and in-camera
  VFX…»** **Las tres piezas de la respuesta están ahí: PRECISIÓN, TIEMPO REAL, ENTORNOS VIRTUALES Y
  AUMENTADOS.**
- **CÓMO FUNCIONA**: **marcas RETRORREFLECTANTES en el techo del plató y un sensor sobre la cámara que
  las lee.** **La ficha del StarTracker Max: «Ceiling, wall or floor mounted retro-reflective stickers or
  digital LED wall markers».** **De ahí sale la posición ABSOLUTA, y a ella se suman los codificadores de
  zoom y foco.**
- **LAS TRES FALSAS**: **«mayoritariamente con drones»** → **es un sistema DE PLATÓ** · **«sólo
  seguimiento de sujetos humanos»** → **lo que se sigue es LA CÁMARA** · **«datos por Bluetooth»** →
  **un enlace de corto alcance no transporta datos de posición con la latencia del directo.**

## Cuántos motores de render

- **PREGUNTA 76** · `[of]` · **Para 3 CÁMARAS Y UNA CABEZA CALIENTE hacen falta 4 MOTORES.**
- **LA CUENTA ES UNO POR CÁMARA**, porque **un motor dibuja el decorado DESDE UN PUNTO DE VISTA
  CONCRETO**, con su posición, orientación y focal. **Cuatro puntos de vista, cuatro dibujos
  simultáneos.**
- **LA CLAVE ESTÁ EN LA CABEZA CALIENTE: ES UNA CÁMARA.** **Para el motor es un punto de vista más.**
- **LAS FALSAS**: **«1 solo motor con potencia suficiente»** → **confunde POTENCIA con SIMULTANEIDAD**:
  **cada salida tiene que estar disponible A LA VEZ, porque el realizador puede cortar a cualquiera en
  cualquier momento; si sólo se renderiza la del aire, EL PREVIO ESTÁ VACÍO** · **«5 porque la cabeza
  caliente necesita 2»** → **inventa una excepción plausible: la cabeza necesita UNO, como cualquier
  cámara.** **Lo que sí necesita más es SEGUIMIENTO —resolver los ejes del brazo—, y eso no es
  *render*.**

## El foreground con un solo motor

- **PREGUNTA 85** · `[of]` · **Hace falta UN INCRUSTADOR CON CAPACIDAD PARA GESTIONAR DIFERENTES
  MÁSCARAS.**
- **EL PROBLEMA**: **una incrustación normal tiene DOS capas** —decorado detrás, presentador delante—.
  **Una TERCERA capa por delante del presentador exige decirle al incrustador que ese trozo va ENCIMA.**
- **ESO ES UNA MÁSCARA**: **dice, PÍXEL A PÍXEL, qué parte de la capa virtual va delante y qué parte va
  detrás.** **El motor entrega el decorado y ADEMÁS la máscara.**
- **POR QUÉ NO HACEN FALTA DOS MOTORES**: **el mismo motor puede dibujar fondo y primer término en UNA
  salida y entregar aparte la información de qué es qué.** **Dos motores serían UNA manera; no la
  única.**

## El storyworld

- **PREGUNTA 81** · `[of]` · **Es UNA TÉCNICA QUE IMPLICA QUE LAS PERSONAS USUARIAS PARTICIPEN EN UN
  UNIVERSO FICTICIO**, y sirve para crear cualquier contexto: **ficción, MARCA, cultura o nación.**
- **POR QUÉ ESTÁ BAJO «ESTRATEGIA TRANSMEDIA»**: **un relato transmedia no cuenta la misma historia en
  varios medios: cuenta PARTES DISTINTAS DE UN MISMO MUNDO en cada medio.** **Lo que las une no es la
  trama: es EL MUNDO.**
- **LA SEGUNDA MITAD ES LA QUE SORPRENDE**: **un *storyworld* NO TIENE POR QUÉ SER DE FICCIÓN.** **Una
  marca construye un mundo con sus valores, sus personajes y sus reglas.**
- **LAS FALSAS LO REDUCEN A UN DOCUMENTO**: **confunden *story-WORLD* con *story-BOARD*** · **lo hacen un
  apartado de la biblia** · **lo ponen DESPUÉS del guion, cuando el mundo se construye ANTES.**
- **EL PUENTE CON EL TEMA 8**: **la biblia CONTIENE la descripción del mundo, pero el mundo NO ES la
  biblia.** **La biblia es el documento; el *storyworld* es lo que el público habita.**

## El agency

- **PREGUNTA 118** · `[of]` · **En narrativa interactiva, es LA SENSACIÓN que llega a tener el usuario de
  PROVOCAR CAMBIOS SIGNIFICATIVOS en el contexto inmersivo.**
- **DOS PALABRAS HACEN LA DEFINICIÓN**: **«SENSACIÓN»** → **no mide cuánto cambia el relato de verdad,
  sino cuánto CREE el usuario que lo cambia**: **tres finales bien colocados dan más agencia que cien
  variantes mal repartidas** · **«SIGNIFICATIVOS»** → **elegir el color de una camisa NO da agencia: la
  decisión tiene que tocar algo que importe.**
- **LAS TRES FALSAS TRASLADAN LA PALABRA A OTRAS DISCIPLINAS**: **teoría del guion** —el arbitrio del
  personaje— · **efectos visuales** —el realismo del CGI— · **tecnología digital** —la compresión—.
  **Es el mismo procedimiento del punto dulce del tema 14: escribir bien la definición de OTRA COSA.**
- **LA PALABRA QUE DECIDE ES «INTERACTIVA»**: **en un relato lineal, por bueno que sea, NO HAY
  AGENCIA.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 30 | Qué define el seguimiento de cámara Mo-Sys | c) Integración precisa de gráficos en tiempo real ✔ **·** fabricante |
| 69 | Diferencia entre realidad aumentada y virtual | a) La RA añade, la RV sustituye ✔ |
| 76 | Cuántos motores de render | c) 4 ✔ |
| 81 | Qué es un *storyworld* | c) Técnica de participación en un universo ficticio ✔ |
| 85 | Qué hace falta para un *foreground* con un motor | a) Un incrustador con máscaras ✔ |
| 91 | Qué tecnología se ve en la fotografía | c) Realidad mixta ✔ **·** sólo con la plantilla |
| 118 | A qué se refiere el *agency* | a) La sensación de provocar cambios significativos ✔ |

**Las siete oficiales son correctas y UNA descansa sólo en la plantilla.** · **Aviso de estudio**:
**las cuatro de plató se contestan con UNA SOLA IDEA —cada punto de vista necesita su propio dibujo— y
las tres de narrativa, con TRES DEFINICIONES.** **Es de los temas más rentables de la ocupación por
hora de estudio.**
