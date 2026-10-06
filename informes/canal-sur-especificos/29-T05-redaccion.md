# Puesto 29 · Tema 5 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real,
como en la investigación). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/05-sistemas-operativos.md`.
Material: `29-investigacion-B-sistemas.md` (§ Tema 5); RTVE
`temas/tecnica-informatica/14-arquitectura-y-administracion-de-sistemas-operativos.md` («actualizar: no»).

## Fuentes releídas y fecha

La investigación dejaba huecos (núcleos sin cita, multitarea cooperativa, problemas clásicos) y
citas de capítulos no extractados. Se descargaron y leyeron los capítulos de OSTEP y las páginas
siguientes, todas el 05-10-2026:

| Fuente | Qué se leyó |
|---|---|
| OSTEP v1.10: intro (cap. 2), cpu-intro (4), cpu-api (5), cpu-mechanisms (6), cpu-sched (7), cpu-sched-mlfq (8), cpu-sched-multi (10), threads-intro (26), threads-locks (28), threads-cv (30), threads-sema (31), file-devices (36); threads-bugs (32) en v1.20 | Pasajes citados; versión y © de cada capítulo anotados en la Trazabilidad |
| Microsoft Learn es-es: «Modo de usuario y modo kernel», «Información general sobre los componentes de Windows», «Biblioteca de kernels en modo kernel de Windows», Win32 «Procesos y subprocesos», «Multitarea», «Prioridades de programación», «Modificadores de contexto» | Texto completo de cada página |
| docs.kernel.org, «EEVDF Scheduler» | Párrafo inicial |
| *The Linux Kernel Module Programming Guide* (sysprog21.github.io/lkmpg, 7-9-2026) | §1.3 y §5.5 (módulos, monolítico, micronúcleos) |
| minix3.org | Párrafo de presentación (micronúcleo) |

Comprobación de literalidad por script: todas las negritas «…» del tema se buscan en el texto
normalizado de las fuentes (ligaduras y saltos de línea unificados); las 183 aparecen tal cual (dos se
corrigieron durante la comprobación: una llamada de nota del PDF partía la definición de SO, que va ahora en tres trozos, y las
llamadas bibliográficas de la cita de MLFQ se marcan ahora con […]).

## Qué se hizo

Siete rúbricas en el orden del enunciado: conceptos generales; componentes funcionales; estructura;
gestión de procesos; algoritmos de planificación; concurrencia; multitarea y multiprogramación.
45 epígrafes; `indice.py`: 9.864 palabras. `refutar_prosa.py`: 0 hallazgos (4 siglas sin presentar en
la primera pasada, corregidas). Tema técnico sin norma: no proceden `negritas.py`,
`refutar_exactitud.py` ni `refutar_modo.py`. El tema no está en `herramientas/portadas.tsv`, como los
demás de Canal Sur: la ficha va escrita a mano.

Negrita = literal de la fuente (OSTEP en inglés, con glosa propia en redonda; Microsoft en castellano,
con sus erratas, p. ej. «Un proceso , en», «modo kernel . El»). Lo copiado de RTVE va en redonda (RTVE
lo tenía todo en negrita sin ser cita).

Decisiones frente al material:

- Clasificación de núcleos: se mantiene monolítico y micronúcleo, ahora con fuente (LKMPG y MINIX 3).
  **Se quita «Híbrido · Windows»** de la tabla de RTVE: ninguna fuente leída lo sostiene; se declara
  en «Lo que este tema no da». La columna de ejemplos cambia (Minix → MINIX 3, GNU Hurd, Zircon).
- Se quita el párrafo de RTVE «casi todo es un fichero… hasta un dispositivo de red se manejan con
  las mismas llamadas que un fichero corriente»: sin fuente y dudoso para las interfaces de red.
- Se quita el «rasgo de diseño de Unix: el núcleo hace lo imprescindible…»: choca con el núcleo
  monolítico de Linux y no tiene fuente.
- Lo propio de RTVE (preguntas 19, 25, 41, 72, 90, reparto de preguntas, órdenes de Linux, tabla de
  administración del punto 17, «software de base») no entra: las órdenes y la administración son de
  los temas 6-9 de este puesto. Las respuestas oficiales de las preguntas 72 y 90 se reescriben como
  contenido (función del gestor de E/S y del núcleo, y qué no hacen).
- Huecos de la investigación cubiertos con fuente: multitarea cooperativa (OSTEP cap. 6, con Mac OS
  antiguo y Xerox Alto), problemas clásicos (cap. 30-31), cerrojos (cap. 28), variables de condición,
  prevención/evitación/detección del interbloqueo, E/S (cap. 36), multiprocesador (cap. 10).
- Aviso de la investigación sobre EEVDF respetado: se cita literal «(as a new option in 2024)» y se
  declara que no se ha comprobado la fecha de la versión 6.6.
- El ejercicio de aplicación (6/3/1 unidades y el caso A=6, B=2 en 2) es cálculo propio, declarado.

## Copiado del común

Nada. Ningún tema cerrado de Canal Sur (común ni específicos) trata sistemas operativos.

## Copiado de RTVE sin cambios

Pasajes técnicos copiados literal, palabra por palabra, de
`temas/tecnica-informatica/14-arquitectura-y-administracion-de-sistemas-operativos.md` (marcado sin
actualizar). Único cambio: se quita la negrita (RTVE no citaba fuente).

| Pasaje en RTVE 14 | Dónde va |
|---|---|
| § 1, tabla «Función / De qué se ocupa» (cinco filas) | § 2 «Las funciones del sistema» |
| § 1, tabla «Modo / Qué puede hacer / Qué corre ahí» (dos filas) | § 1 «Los modos núcleo y usuario» |
| § 1, párrafo «La razón de que existan los dos: un error de un programa no puede llevarse el sistema por delante. Cuando un programa necesita algo del soporte físico, no lo toca: lo pide.» | ídem |
| § 3, párrafo «Qué hace el gestor de entrada y salida, en tres líneas: … y el gestor se entiende con el aparato.» (dos frases) | § 2 «El gestor de entrada y salida» |
| § 2, párrafo «Linux es monolítico y a la vez modular: los controladores se cargan y descargan en caliente, que es lo que permite añadir soporte físico sin recompilar.» | § 3 «Tipos de núcleo» (este sí tiene apoyo en la LKMPG, citada justo antes) |

Adaptado de RTVE (no literal; sí se verifica): la frase de entrada a la tabla de funciones; la
tabla de tipos de núcleo (filas monolítico y micronúcleo, columna de ejemplo cambiada, fila híbrido
quitada); la función del núcleo en Unix/Linux y lo que no hace (de la pregunta 90 y su tabla de
distractores); la función del gestor de E/S y lo que no hace (de la pregunta 72 y su tabla).

## Ficheros tocados

Sólo el tema y este informe. Descargas de trabajo en el directorio temporal de la sesión (OSTEP y
páginas web), fuera del repositorio.

## Preguntas de control (10, tipo test)

Repartidas por las rúbricas del enunciado; teoría y aplicación práctica. Se contestan con el tema.

1. **Conceptos generales.** En una llamada al sistema, ¿qué instrucción salta al núcleo y eleva el
   privilegio a modo núcleo? a) *return-from-trap*; b) *trap*; c) `yield`; d) `fork()`.
   → b. Tema § 1 «La llamada al sistema». **Entera.**
2. **Estructura.** MINIX 3 es un ejemplo de: a) núcleo monolítico; b) micronúcleo; c) núcleo
   modular sin modo núcleo; d) hipervisor. → b. § 3 «Tipos de núcleo». **Entera.**
3. **Componentes funcionales.** La técnica que mueve datos entre un dispositivo y la memoria
   principal sin apenas intervención de la CPU y avisa al terminar con una interrupción es: a) el
   sondeo; b) la E/S mapeada en memoria; c) el DMA; d) la agrupación de interrupciones. → c. § 2 «El
   gestor de entrada y salida». **Entera.**
4. **Gestión de procesos.** ¿Qué transición no existe en el modelo de tres estados? a) en ejecución →
   bloqueado; b) bloqueado → listo; c) listo → bloqueado; d) listo → en ejecución. → c. § 4 «Los
   estados de un proceso». **Entera** (el tema lo dice expresamente).
5. **Gestión de procesos.** En Unix, el proceso que ha terminado y cuyo padre aún no ha recogido su
   código de retorno con `wait()` está en estado: a) bloqueado; b) zombi; c) listo; d) suspendido.
   → b. § 4. **Entera.**
6. **Planificación · aplicación práctica.** Tres trabajos llegan en el instante 0 en el orden A (6),
   B (3), C (1). Con FIFO, el tiempo medio de retorno es: a) 5; b) 6,67; c) 8,33; d) 10. → c (25/3).
   § 5 «Ejercicio de aplicación». **Entera** (y con SJF 5, con RR cuanto 1 6,67).
7. **Planificación.** ¿Cuál de estos algoritmos es apropiativo? a) FIFO; b) SJF; c) STCF; d) FCFS.
   → c. § 5 «Planificación apropiativa y no apropiativa». **Entera.**
8. **Planificación · Windows.** Los niveles de prioridad de los hilos en Windows van de: a) 0 a 15;
   b) 0 a 31, y sólo el hilo de página cero puede tener 0; c) −20 a 19; d) 1 a 99. → b. § 5 «Cómo
   planifica Windows». **Entera.**
9. **Concurrencia.** ¿Cuál no es una de las cuatro condiciones necesarias del interbloqueo? a)
   exclusión mutua; b) retención y espera; c) inanición; d) espera circular. → c. § 6 «El
   interbloqueo» y «La inanición». **Entera.**
10. **Multitarea y multiprogramación.** En la multitarea cooperativa, el sistema recupera la CPU: a)
    con una interrupción de reloj cada cuanto; b) cuando el proceso hace una llamada al sistema o una
    operación ilegal; c) mediante DMA; d) con el algoritmo del banquero. → b. § 7 «Multitarea
    apropiativa y cooperativa». **Entera.**

Resultado: 10 de 10 enteras; no hizo falta ampliar. Otras que el tema también contesta: valor −3 de
un semáforo (3 hilos esperando); segmento de tiempo de Windows (≈ 20 ms); planificador vigente de
Linux (EEVDF desde 6.6); finalidad de la multiprogramación (aprovechar la CPU durante la E/S).
