# Puesto 29 · Tema 5 · Preguntas de refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/05-sistemas-operativos.md`.
15 preguntas tipo test, de 4 opciones, repartidas por el enunciado (teoría y aplicación práctica),
distintas de las 10 de control de la redacción. Se contestan **sólo con el tema**.

1. **Conceptos generales.** ¿Por qué se dice que el sistema operativo es un «gestor de recursos»?
   a) Porque traduce programas de alto nivel; b) porque reparte entre varios programas la CPU, la
   memoria y los discos; c) porque sólo se ocupa de los ficheros; d) porque se ejecuta en modo usuario.
   → b. § 1, tabla «Visto como». **Entera.**
2. **Conceptos generales · Windows.** Si un controlador en modo kernel de Windows se bloquea: a) sólo
   se cierra la aplicación que lo usa; b) se bloquea todo el sistema operativo; c) Windows lo
   reinicia en modo usuario; d) no ocurre nada, porque tiene su espacio privado. → b. § 1 «Los modos
   núcleo y usuario». **Entera.**
3. **Componentes funcionales.** En la E/S mapeada en memoria: a) el procesador usa instrucciones de
   E/S explícitas, como los mainframes de IBM; b) los registros del dispositivo se presentan como si
   fueran posiciones de memoria; c) el DMA sustituye al controlador; d) sólo puede usarse con sondeo.
   → b. § 2 «El gestor de entrada y salida». **Entera.**
4. **Estructura.** Un módulo del núcleo Linux: a) corre en modo usuario con su propio espacio de
   código; b) se carga y descarga en el núcleo sin reiniciar y comparte su espacio de código; c)
   convierte Linux en micronúcleo; d) exige recompilar la imagen del núcleo. → b. § 3 «Tipos de
   núcleo». **Entera.**
5. **Conceptos generales · clasificación.** Un sistema operativo que debe garantizar que cada tarea
   responde dentro de un plazo máximo fijado es: a) por lotes; b) de tiempo compartido; c) de tiempo
   real; d) multiprogramado. → c. El tema trata lotes, multiprogramación, tiempo compartido y
   multitarea, pero no la clasificación de los sistemas (tiempo real, monousuario/multiusuario,
   distribuidos, en red). **No.**
6. **Gestión de procesos · aplicación práctica.** Un proceso en ejecución pide leer un bloque de disco;
   la lectura termina mientras otro proceso usa la CPU. Su secuencia de estados es: a) en ejecución →
   bloqueado → en ejecución; b) en ejecución → bloqueado → listo; c) en ejecución → listo → bloqueado;
   d) listo → bloqueado → listo. → b. § 4 «Los estados de un proceso» (transiciones y lo que no hay).
   **Entera.**
7. **Gestión de procesos.** El planificador que decide qué procesos se retiran temporalmente de la
   memoria principal (suspendidos) para reducir el grado de multiprogramación es el de: a) corto
   plazo; b) medio plazo; c) largo plazo; d) el despachador. → b. El tema no distingue niveles de
   planificación (largo, medio y corto plazo) ni el estado suspendido; sólo da los tres estados, el
   inicial y el zombi. **No.**
8. **Planificación · aplicación práctica.** Llegan en el instante 0, en este orden, A (5), B (3) y C (1).
   Con turno rotatorio y cuanto 2, el tiempo medio de retorno es: a) 6; b) 7,33; c) 8; d) 9. → b
   (A 0-2, B 2-4, C 4-5, A 5-7, B 7-8, A 8-9; finalizaciones 9, 8, 5; 22/3). § 5 «Round Robin» y
   «Ejercicio de aplicación» (método y definición). **Entera.**
9. **Planificación · aplicación práctica.** Con los mismos trabajos y FIFO, el tiempo medio de
   espera es: a) 3; b) 4,33; c) 5; d) 7,67. → b ((0 + 5 + 8) / 3). El tema sólo define tiempo de
   retorno y de respuesta; el de espera (y el rendimiento o productividad, y la utilización de la
   CPU) no aparece. Con llegadas simultáneas y sin apropiación coincide numéricamente con el de
   respuesta, pero el tema no lo dice. **A medias.**
10. **Planificación · MLFQ.** En MLFQ, la regla que mueve periódicamente todos los trabajos a la cola
    superior sirve para: a) que un programa no engañe al planificador; b) evitar la inanición de los
    trabajos largos; c) reducir el coste del cambio de contexto; d) conocer de antemano la duración
    de los trabajos. → b. § 5 «Colas multinivel con realimentación». **Entera.**
11. **Planificación · Windows.** Salvo que se indique otra cosa, un proceso de Windows se crea con la
    clase de prioridad: a) IDLE_PRIORITY_CLASS; b) NORMAL_PRIORITY_CLASS; c) HIGH_PRIORITY_CLASS; d)
    REALTIME_PRIORITY_CLASS. → b. § 5 «Cómo planifica Windows». **Entera.**
12. **Concurrencia.** Un semáforo iniciado a 1 se usa como: a) variable de condición; b) cerrojo
    (semáforo binario); c) contador de productores; d) mecanismo para ordenar sucesos entre dos hilos.
    → b. § 6 «Semáforos». **Entera.**
13. **Concurrencia.** El algoritmo de Peterson: a) da exclusión mutua entre dos hilos sólo con
    cargas y almacenamientos en variables compartidas, sin instrucciones atómicas especiales; b)
    necesita *test-and-set*; c) evita el interbloqueo por el algoritmo del banquero; d) es una
    variable de condición. → a. El tema remite Dekker, Peterson y los monitores a «Lo que este tema no
    da» («no se han leído en fuente»). **No.**
14. **Concurrencia · aplicación práctica.** El hilo 1 hace lock(L1) y luego lock(L2); el hilo 2, lock(L2)
    y luego lock(L1). La corrección más práctica es: a) dar más prioridad al hilo 1; b) que los dos
    cojan siempre L1 antes que L2; c) quitar la exclusión mutua de L1; d) acortar el cuanto. → b
    (orden total, rompe la espera circular). § 6 «El interbloqueo». **Entera.**
15. **Gestión de procesos · hilos.** En el modelo de hilos «muchos a uno» (hilos de usuario sin soporte
    del núcleo), si un hilo hace una llamada al sistema bloqueante: a) sólo se bloquea ese hilo; b) se
    bloquea todo el proceso; c) el núcleo reparte los demás hilos entre las CPU; d) el proceso pasa a
    zombi. → b. El tema define hilo, TCB y cambio de contexto entre hilos, y la fibra de Windows, pero
    no distingue hilos de usuario y de núcleo ni sus modelos. **No.**

## Resultado

Entera: 10 (1, 2, 3, 4, 6, 8, 10, 11, 12, 14). A medias: 1 (9). No: 4 (5, 7, 13, 15).
