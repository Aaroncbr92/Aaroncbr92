# Tema 5 del específico de Operador/a Informático · Sistemas operativos

**Siglas**: SO sistema operativo; E/S entrada y salida; DMA acceso directo a memoria; ISR rutina de interrupción; PCB/TCB bloque de control de proceso/hilo; PC contador de programa; FIFO=FCFS; SJF; STCF=PSJF; RR; MLFQ; SQMS/MQMS cola única/múltiple; EEVDF; VD plazo virtual; CFS; OSTEP.

Esqueleto para repasar, no resumen: fuente delante de cada línea. Leído 05/06-10-2026.

<!-- indice -->
<!-- /indice -->

## 1. Conceptos generales

- OSTEP 2: SO = software que facilita ejecutar programas, compartir memoria, usar dispositivos; antes «supervisor», «master control program».
- OSTEP 2: máquina virtual; biblioteca estándar (cientos de llamadas); gestor de recursos (CPU, memoria, disco). Tres piezas: virtualización, concurrencia, persistencia.
- OSTEP 2 objetivos: abstracciones; rendimiento; protección; fiabilidad; energía, seguridad, movilidad.
- OSTEP 6: usuario restringido (E/S -> excepción, se termina); núcleo: todo, incluidas operaciones privilegiadas.
- Microsoft: aplicaciones en usuario, núcleo del SO en kernel, algunos controladores en usuario. Usuario: espacio virtual privado, fallo aislado. Kernel: espacio único compartido, fallo de controlador cae todo.
- OSTEP 6 llamada al sistema: *trap* salta al núcleo y sube a modo núcleo; *return-from-trap* baja a usuario; tabla de *traps* preparada en el arranque; se ve como función de la biblioteca C (`open()`, `read()`); nacieron en Atlas.
- OSTEP 4: mecanismo = cómo (cambio de contexto); política = cuál (planificación); separables.
- J. Bell 1: tiempo compartido (multiusuario multitarea); tiempo real (plazo d_j; control de procesos); empotrados (automóviles, climatización); distribuidos (ordenadores heterogéneos en red).
- Linux Deadline: `SCHED_DEADLINE` para tareas periódicas o esporádicas (multimedia, streaming, control); PREEMPT_RT = tiempo real; `SCHED_FIFO`: la de más prioridad se elige ya. Oficio: tiempo real = garantía de plazo.

## 2. Componentes funcionales

- Cinco funciones (oficio): procesos; memoria; ficheros (datos persistentes); E/S (acceso estándar por llamadas); protección y seguridad.
- Gestor de E/S (oficio): convierte la petición en órdenes al controlador; no es ALU, planificador ni pila de red. Windows: «administrador de E/S», `IoCreateDevice`.
- OSTEP 36 registros: estado, orden, datos. Controlador: sabe cómo funciona el dispositivo y lo encapsula; Linux: capa de bloques; más del 70 % del código del SO; causa principal de caídas.
- Sondeo (*polling*): lee estado hasta que esté listo; rápidos.
- Interrupciones: duerme al proceso; al acabar, ISR; solo lentos; solapa cálculo y E/S.
- DMA: dispositivo-memoria sin CPU; interrupción al terminar; transferencias grandes.
- Avalancha de interrupciones = *livelock* (vuelve el sondeo); *coalescing*: menos coste, más latencia. Registros: E/S explícita (mainframes IBM) o mapeada en memoria; ambas en uso.

## 3. Estructura

- Microsoft: kernel = funcionalidad básica (programar hilos, enrutar interrupciones).
- Oficio, núcleo Unix/Linux: procesos, memoria, dispositivos; no interfaz gráfica, servicios de red (demonios; pila en el núcleo) ni terminales.
- Monolítico (oficio): todo en modo núcleo; Linux con módulos.
- Micronúcleo: lo mínimo en modo núcleo, resto en usuario; MINIX 3; LKMPG: GNU Hurd, Zircon (Fuchsia, Google).
- LKMPG módulo Linux: código que se carga y descarga sin reiniciar; sin módulos: recompilar y reiniciar. Comparte el espacio de código del núcleo: su fallo es fallo del núcleo (todo monolítico); en micronúcleos, espacio propio.
- Oficio: micronúcleo aísla fallos; monolítico evita coste de fronteras. Microsoft: «microkernel» no se aplica a Windows.

## 4. Gestión de procesos

- OSTEP 4: proceso = programa en ejecución. Microsoft: aplicación = uno o varios procesos; subproceso = unidad a la que se asigna tiempo de procesador.
- Estado de máquina: espacio de direcciones; registros (PC, puntero de pila); E/S (ficheros abiertos). Creación: carga código y datos (*eagerly* antiguos, *lazily* modernos), pila (quizá montículo), E/S (Unix: tres descriptores), salto al punto de entrada.
- Tres estados (OSTEP 4, fig. 4.2): ejecución, listo, bloqueado. Listo->ejecución *Scheduled*; ejecución->listo *Descheduled*; ejecución->bloqueado *I/O: initiate*; bloqueado->listo *I/O: done*. No bloqueado->ejecución ni listo->bloqueado.
- *Zombie state* (Unix): el padre recoge el retorno con `wait()`. J. Bell 3, cinco estados: New, Ready, Running, Waiting, Terminated.
- PCB (OSTEP 4): estructura C por proceso (process descriptor) en la lista de procesos; xv6 `proc`: registros, estado, identificador, padre, ficheros abiertos, directorio actual.
- OSTEP 5 operaciones: Create, Destroy, Wait, Miscellaneous Control, Status.
- Unix: `fork()` crea hijo copia del padre; `wait()` espera al hijo; `exec()` programa nuevo; el intérprete usa las tres (separarlas permite redirigir y tuberías); señales.
- OSTEP 26 hilo: comparte espacio de direcciones; registros, PC y pila propios; TCB; sin cambio de tabla de páginas. Sirven para paralelismo y solapar E/S.
- Microsoft: fibra (programada a mano); grupo de subprocesos (llamadas asincrónicas).
- J. Bell 4: hilos de usuario (sin núcleo) y de núcleo (todos los SO modernos).
- Muchos a uno: eficiente; llamada bloqueante bloquea el proceso; sin varias CPU; pocos hoy.
- Uno a uno: un hilo de núcleo por hilo de usuario; más coste; límite de hilos; ejemplo Linux.
- Muchos a muchos: multiplexa en igual o menor número de hilos de núcleo; sin límite ni bloqueo total; variante *two-tier*.
- OSTEP 6 cambio de contexto: el planificador decide; guarda registros del que sale en su pila de núcleo y restaura los del que entra; coste: cachés.
- Microsoft pasos: 1 guardar contexto; 2 si sigue listo, al final de la cola de su prioridad; 3 buscar cola de prioridad más alta con listos; 4 quitar el de la cabeza, restaurar contexto, reanudar. Causas: quantum expirado y otro de igual o mayor prioridad listo; uno de mayor prioridad listo; espera del que corre. Sin procesador: suspendidos, `SuspendThread`, `SwitchToThread`, esperando sincronización o entrada.

## 5. Algoritmos de planificación

- OSTEP 7: retorno = finalización − llegada; respuesta = primera ejecución − llegada; rendimiento y equidad chocan.
- J. Bell 6: utilización de CPU (maximizar; 40 % ligera a 90 % pesada); productividad = procesos por unidad de tiempo (maximizar); espera = tiempo en cola de listos (reducir).
- J. Bell 6: largo plazo (qué trabajo entra); medio plazo (opcional, saca procesos); corto plazo o de CPU (~100 ms).
- Despachador: da la CPU al elegido; latencia de despacho.
- OSTEP 7: no apropiativo = cada trabajo hasta el final; apropiativo quita la CPU (casi todos hoy). FIFO y SJF no; STCF, RR, MLFQ sí.
- FIFO/FCFS: por llegada; efecto convoy. A=100, B=C=10 a la vez: retorno medio 110 s ((100+110+120)/3).
- SJF: el más corto; B y C antes: 50 s ((10+20+120)/3); óptimo en retorno (llegada simultánea, solo CPU, duración conocida). Límites: no apropiativo (B y C llegan en 10: 103,33 s); duraciones irreales.
- STCF/PSJF: SJF apropiativo, al llegar uno elige el de menor tiempo restante; mismo ejemplo 50 s (((120−0)+(20−10)+(30−10))/3); óptimo en retorno, malo en respuesta.
- RR: cuanto (*time slice*), múltiplo del periodo de reloj (10 ms: 10, 20...); corto = mejor respuesta; demasiado corto = domina el cambio de contexto (10 ms con cambio de 1 ms: ~10 %; 100 ms: <1 %, amortización). Bueno en respuesta, de los peores en retorno; SJF/STCF al revés.
- E/S: se bloquea, otro usa la CPU, interrupción lo devuelve a listo; ráfaga = trabajo corto; solapamiento.
- Ejercicio (cálculo propio; espera = retorno − ráfaga) A=6, B=3, C=1 en 0. FIFO: finaliza 6, 9, 10; retorno 25/3 ≈ 8,33; respuesta 5; espera 5. SJF (C, B, A): 10, 4, 1; retorno 5; respuesta y espera ≈ 1,67. RR cuanto 1 (A,B,C,A,B,A,B,A,A,A): 10, 7, 3; retorno ≈ 6,67; respuesta 1; espera (4+4+2)/3 ≈ 3,33.
- Llegadas distintas, A (0, dura 6) y B (2, dura 2): SJF retornos 6 y 6, media 6; STCF B de 2 a 4, A termina en 8, retornos 8 y 2, media 5.
- J. Bell 6 prioridades: generaliza SJF; sin convención de número alto (libro: 0; Windows: 31); internas o externas; apropiativa o no. Inanición (*indefinite blocking*); remedio: envejecimiento (*aging*).
- Ejemplo 8,2 ms (cálculo propio, llegada en 0): P1 10 (prio 3), P2 1 (1), P3 2 (4), P4 1 (5), P5 5 (2); orden P2, P5, P1, P3, P4; esperas 0, 1, 6, 16, 18; 41/5 = 8,2.
- OSTEP 8 MLFQ: R1 mayor prioridad corre; R2 iguales, RR; R3 nuevo, cola superior; R4 agotado el tiempo en un nivel (ceda o no la CPU), baja; R5 tras un tiempo S, todos arriba.
- MLFQ: aproxima SJF sin duraciones; R5 (*priority boost*) evita inanición; R4 evita engañar al planificador. Base de BSD UNIX, Solaris, Windows NT y posteriores.
- OSTEP 10: SQMS una cola (simple, cerrojos, pierde afinidad de caché); MQMS una por CPU (desequilibrio; migración; *work stealing*).
- Microsoft Windows: prioridades 0 (solo subproceso de página cero) a 31; RR entre los de más prioridad; el de mayor prioridad desaloja al menor sin terminar su intervalo y recibe segmento completo. Base = clase del proceso + nivel del hilo; seis clases (`IDLE_PRIORITY_CLASS` a `REALTIME_PRIORITY_CLASS`, defecto `NORMAL_PRIORITY_CLASS`); siete niveles (`THREAD_PRIORITY_IDLE` a `THREAD_PRIORITY_TIME_CRITICAL`, defecto `THREAD_PRIORITY_NORMAL`). Prioridad máxima prolongada deja sin tiempo a los demás; tiempo real interrumpe ratón, teclado, disco.
- docs.kernel.org EEVDF: desde Linux 6.6 («new option in 2024»; fecha no comprobada), deja CFS; CPU por igual a igual prioridad; desfase (*lag*); entre desfase >= 0 elige VD más temprano; porciones cortas a las sensibles a latencia.

## 6. Concurrencia

- OSTEP 26: dos hilos suman a un contador (leer, sumar, escribir); un cambio en medio pierde una suma.
- Sección crítica: código con recurso compartido, no concurrente. Condición de carrera (*data race*): resultado según el momento. Programa indeterminado: salida variable. Exclusión mutua: dentro uno, los demás no. Atomicidad: «all or nothing».
- OSTEP 28 cerrojo: variable libre o adquirida (un hilo); `lock()`/`unlock()`; POSIX *mutex*. Criterios: exclusión mutua, equidad, rendimiento. *Spin lock* con *test-and-set*: gira gastando CPU; un procesador exige planificador apropiativo. Inhibir interrupciones: solo un procesador.
- Dekker (años sesenta): solo lecturas y escrituras; Peterson lo refinó; dos hilos; `flag[2]` (intención) y `turn`: marca `flag`, `turn = 1 - self`, espera mientras el otro quiera y sea su turno; salir: baja `flag`. No valen en hardware moderno (memoria relajada).
- OSTEP 31 semáforo: entero con `sem_wait()` (P, decrementa, espera si negativo) y `sem_post()` (V, incrementa, despierta a uno). Negativo = hilos esperando. Inicial 1: cerrojo (binario); 0: ordenar sucesos.
- OSTEP 30 variable de condición: cola explícita; espera y *signal*; nombre de Hoare.
- OSTEP apéndice D, monitores (obsoletos): Brinch Hansen, Hoare; un hilo activo; cerrojo implícito; Java *synchronized*; C++ no. `wait()` bloquea, `signal()` despierta a uno. Hoare: despierta y ejecuta ya. Mesa (Lampson y Redell, Xerox PARC): solo pista; casi todos hoy; `while`, no `if`.
- J. Bell: memoria compartida (rápida, difícil de montar, mala entre ordenadores, exige sincronizar); paso de mensajes (sencillo, entre ordenadores, llamada por mensaje, lento): `send`/`receive`; directo o indirecto (buzones, puertos); bloqueante o no; cola cero, limitada, ilimitada.
- Productor-consumidor (búfer acotado; servidor web, `grep foo file.txt | wc -l`): semáforos `empty` y `full` + cerrojo solo en la sección crítica (si envuelve las esperas, interbloqueo).
- Lectores-escritores: cerrojo de lectura y escritura.
- Filósofos: cinco, tenedor entre cada dos; Dijkstra: uno coge en orden distinto; utilidad práctica baja.
- OSTEP 32 (v1.20) interbloqueo, cuatro condiciones: exclusión mutua; retención y espera; sin apropiación; espera circular; si falta una, no hay.
- Prevención: orden total de cerrojos (la más práctica); coger todos de forma atómica; `pthread_mutex_trylock()` (*livelock*, espera aleatoria); *lock-free*. Evitación: algoritmo del banquero de Dijkstra; muy limitado. Detección: grafo de recursos, ciclos, reinicio; bases de datos.
- Inanición: nunca obtiene recurso o CPU aunque el sistema avance. Interbloqueo: nadie avanza; *livelock*: trabajan sin progresar.

## 7. Multitarea y multiprogramación

- OSTEP 2 lotes: un programa cada vez, operador humano. Multiprogramación: varios trabajos en memoria; mejora la CPU ante E/S lenta; trajo protección de memoria y concurrencia.
- Tiempo compartido: CPU a intervalos cortos; cada uno más lento. Oficio: multiprogramación aprovecha la CPU ante E/S; tiempo compartido da respuesta interactiva.
- Microsoft multitarea: divide el tiempo entre procesos o subprocesos; «preferente» = apropiativa; suspende al acabar el segmento (~20 ms, según SO y procesador); multiprocesador: hilos repartidos.
- OSTEP 6 cooperativa: espera llamada al sistema u operación ilegal; `yield`; confía en los procesos; bucle infinito = reiniciar; Macintosh antiguo, Xerox Alto.
- Apropiativa: interrupción de reloj -> manejador del SO; no se fía; coste de cambios de contexto; sistemas actuales.
- Oficio: un procesador = concurrencia sin paralelismo; varios = paralelismo.
