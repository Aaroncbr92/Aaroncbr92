# Puesto 29 · Tema 5 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/05-sistemas-operativos.md` (de unas 10.000
a 12.800 palabras). Entrada: `29-T05-refutacion.md` (0 graves, 0 menores, 5 lagunas) y
`29-T05-preguntas.md` (10 enteras, 1 a medias y 4 no).

**Amplía: sí.** No había correcciones de exactitud que aplicar; las cinco lagunas se han cubierto con
fuente leída hoy, sin recortar ninguna pregunta. Toca la fase 5 bis sobre los pasajes de abajo.

## Fuentes leídas (todas el 06-10-2026)

| Fuente | Para qué |
|---|---|
| OSTEP v1.10, cap. 28 «Locks» (threads-locks.pdf), recuadro «Dekker’s and Peterson’s algorithms» | L4 |
| OSTEP, apéndice D «Monitors (Deprecated)» (threads-monitors.pdf) | L4 |
| J. Bell, apuntes CS 385 de la Universidad de Illinois en Chicago, sobre Silberschatz, Galvin y Gagne, 9.ª ed.: caps. 1, 3, 4 y 6 (www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/) y su página principal (fechas 2006-2013) | L1, L2, L3, L4 (paso de mensajes), L5 |
| docs.kernel.org, «Deadline Task Scheduling» y «Real-time preemption · Theory of operation» | L1 (tiempo real) |

Intentadas sin éxito: las transparencias oficiales del manual de Silberschatz en codex.cs.yale.edu
(certificado TLS caducado: no se forzó) y la página «RTOS fundamentals» de FreeRTOS (se genera con
JavaScript y no da texto). Las 64 negritas nuevas se cotejaron por script contra el texto de esas
fuentes: 64 encontradas, 0 fallos.

## Lagunas y cómo se cubren

| # | Pregunta | Cobertura | Dónde |
|---|---|---|---|
| L1 | 5 | Tiempo compartido (multiusuario y multitarea), tiempo real (plazo; control de procesos; `SCHED_DEADLINE` para multimedia y *streaming*; PREEMPT_RT; `SCHED_FIFO`), empotrados, distribuidos y de red. Monousuario y tiempo real estricto/no estricto: sin fuente, declarados en «Lo que este tema no da» | § 1, nuevo «Clases de sistemas operativos» |
| L2 | 7 | Modelo de cinco estados; planificadores de largo, medio y corto plazo; despachador y latencia de despacho. El nombre «suspendido» no está en las fuentes leídas: declarado | § 4 «Los estados de un proceso» (párrafo nuevo); § 5, nuevo «Los niveles de planificación y el despachador» |
| L3 | 9 | Utilización de la CPU, productividad y tiempo de espera; T espera = T retorno − T ráfaga (cálculo); columna de espera en el ejercicio; planificación por prioridades, convenio de números, internas/externas, apropiativa o no, inanición y envejecimiento, ejemplo de 8,2 ms rehecho | § 5 «Qué decide el planificador…», «Ejercicio de aplicación», nuevo «Planificación por prioridades» |
| L4 | 13 | Dekker y Peterson (sólo cargas y almacenamientos; `flag` y `turn`; no valen en el soporte físico actual); monitores (Brinch Hansen, Hoare; cerrojo implícito; Java `synchronized`; semánticas de Hoare y de Mesa; regla del `while`); memoria compartida y paso de mensajes (send/receive, nombrado, sincronización, cola) | § 6, nuevos «Soluciones por programa: Dekker y Peterson», «Monitores», «Memoria compartida y paso de mensajes» |
| L5 | 15 | Hilos de usuario y de núcleo; modelos muchos a uno (bloqueo de todo el proceso), uno a uno, muchos a muchos y dos niveles | § 4 «Hilos», bloque nuevo |

Recalculado: ejercicio con espera media FIFO 5, SJF 1,67, RR cuanto 1 10/3 ≈ 3,33 (A 4, B 4, C 2,
contados también intervalo a intervalo); ejemplo de prioridades P2, P5, P1, P3, P4, esperas 0, 1, 6,
16, 18, media 41/5 = 8,2, que coincide con la cifra de los apuntes. La pregunta 9 de la refutación
(FIFO A5, B3, C1: 4,33) se contesta ya con la definición y la fórmula del tema.

## Pasajes cambiados

1. Ficha: «Fuente» (añadidos los apuntes de J. Bell), «Redacción que se estudia» (fecha del
   remate), «Extensión» (12.800 palabras).
2. «Qué se puede preguntar» y su frase de aplicación práctica: añadidos tiempo real y distribuido,
   hilos de usuario y de núcleo, niveles de planificación y despachador, espera, utilización y
   productividad, prioridades y envejecimiento, Dekker y Peterson, monitor, memoria compartida y
   paso de mensajes.
3. § 1, epígrafe nuevo «Clases de sistemas operativos» (tabla y párrafo de tiempo real).
4. § 4 «Los estados de un proceso», párrafo nuevo del modelo de cinco estados.
5. § 4 «Hilos», bloque nuevo «Hilos de usuario y de núcleo» con tabla de modelos.
6. § 5 «Qué decide el planificador y cómo se mide», tabla de tres criterios y párrafo de la fórmula.
7. § 5, epígrafe nuevo «Los niveles de planificación y el despachador».
8. § 5 «Ejercicio de aplicación», columna «Espera media» y párrafo que la explica.
9. § 5, epígrafe nuevo «Planificación por prioridades».
10. § 6, epígrafes nuevos «Soluciones por programa: Dekker y Peterson», «Monitores» y «Memoria
    compartida y paso de mensajes».
11. «Lo que este tema no da»: quitado el punto que decía que monitores, paso de mensajes, Dekker y
    Peterson no se habían leído en fuente (desmentido por la refutación); añadidos el estado
    suspendido, los sistemas monousuario, el tiempo real estricto/no estricto y las llamadas
    concretas de comunicación entre procesos.
12. «Trazabilidad»: tres filas nuevas (OSTEP cap. 28 y apéndice D; apuntes de J. Bell; núcleo Linux
    de tiempo real), nota sobre la fecha y el alcance de los apuntes, y dos añadidos a la lista de
    oficio y a la de cálculo.

Releídos los pasajes cambiados: cada «los apuntes» tiene delante su presentación; «este apéndice»
se cambió por «les dedica un apéndice titulado» porque no tenía antecedente.

## Lentes

- `indice.py`: índice regenerado, 51 epígrafes, 12.798 palabras.
- `refutar_prosa.py`: 0 hallazgos (siglas, relleno, repeticiones, negritas rotas).
- Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`;
  en su lugar, el cotejo por script de las 64 negritas nuevas contra las fuentes (0 fallos).

## Ficheros tocados

El tema y este informe. Descargas en el directorio temporal de la sesión. Nada más.
