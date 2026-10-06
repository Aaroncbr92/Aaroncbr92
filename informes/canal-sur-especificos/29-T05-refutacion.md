# Puesto 29 · Tema 5 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/05-sistemas-operativos.md` (899 líneas).
Preguntas: `29-T05-preguntas.md`. No se corrige nada: sólo se informa.

## Fuentes releídas y fecha

Todas el 06-10-2026: OSTEP v1.10, caps. 2 (intro), 4 (cpu-intro), 6 (cpu-mechanisms), 7 (cpu-sched),
26 (threads-intro), 28 (threads-locks), 31 (threads-sema), 36 (file-devices) y 32 (threads-bugs),
descargados de pages.cs.wisc.edu/~remzi/OSTEP/; índice de OSTEP (existencia del apéndice
«Monitors»); docs.kernel.org «EEVDF Scheduler». Microsoft Learn y LKMPG no se releyeron: la
verificación los comprobó por script (189 fragmentos literales, 0 fallos) y no hay en ellos dato en
redonda dudoso.

Saltado por exactitud (sí mirado por cobertura): los cinco pasajes «Copiado de RTVE sin cambios»
(tabla de funciones, tabla de modos y su párrafo, gestor de E/S «en tres líneas», «Linux es
monolítico y a la vez modular»). «Copiado del común»: nada.

## Lente 1 · Exactitud

Comprobados contra la fuente, sin hallazgo:

- Atlas como pionero de la llamada al sistema (OSTEP 2 y 6); tabla de *traps*.
- Interrupciones **«only really make sense for slow devices»**, *livelock* → sondeo, *coalescing*
  a cambio de latencia (OSTEP 36, recuadro y § 36.3).
- Estados, transiciones y zombi (OSTEP 4); pila y montículo al crear el proceso.
- Ejemplos numéricos del manual: 110, 50, 103,33 y 50 s; 10 % y 1 % de amortización; cuanto
  múltiplo del periodo del reloj; RR **«one of the worst policies»** para el retorno; STCF malo
  para la respuesta («the third job has to wait for the previous two»: el tema lo generaliza a «el
  último… todos los anteriores», correcto).
- Cálculo propio rehecho: FIFO 25/3 y 5; SJF 5 y 1,67; RR cuanto 1 (A,B,C,A,B,A,B,A,A,A) 20/3 y 1;
  SJF 6 y STCF 5 con llegadas 0 y 2. Correcto.
- «Virtually all of these terms… coined by Edsger Dijkstra» → «casi todos»; cerrojo por inhibición
  de interrupciones **«One of the earliest solutions»**, para un procesador; *spin lock* necesita
  planificador apropiativo en un procesador (OSTEP 26, 28).
- Interbloqueo: orden total **«Probably the most practical»**; detección por grafo y reinicio;
  bases de datos (OSTEP 32).
- Mac OS antiguo y Xerox Alto como cooperativos; reinicio como único remedio (OSTEP 6).
- EEVDF: 6.6 **«(as a new option in 2024)»**, desfase ≥ 0, plazo virtual más temprano, tareas
  sensibles a la latencia con porciones cortas (docs.kernel.org). La fecha «2024» es de la fuente;
  el tema ya avisa de que no la ha contrastado.

**Graves: 0. Menores: 0.** Los nueve errores, sin aparición: no hay normas (1, 2, 4, 7, 8 no
proceden); siglas presentadas (5); salvedades del manual repuestas en verificación (6); recuentos
(«cinco funciones», «seis clases», «siete niveles», «cuatro condiciones», «tres registros») cuadran
(3); afirmaciones sin fuente declaradas como oficio en la Trazabilidad (9).

## Lente 2 · Cobertura del enunciado

Las siete rúbricas del enunciado tienen epígrafe propio y en su orden. El test de 15 preguntas da
10 enteras, 1 a medias y 4 no. Lagunas (se amplía el tema):

| # | Rúbrica | Laguna | Pregunta | Fuente disponible |
|---|---|---|---|---|
| L1 | Conceptos generales | Clasificación de los sistemas operativos: por lotes, multiprogramados, de tiempo compartido (ya están) y además de tiempo real, monousuario/multiusuario, distribuidos o en red | 5 | Buscar manual universitario; OSTEP no la da como tal |
| L2 | Gestión de procesos / planificación | Niveles de planificación (largo, medio y corto plazo), despachador y estado suspendido (modelo de más de tres estados por intercambio) | 7 | Buscar fuente; OSTEP sólo da el modelo de tres estados más inicial y zombi |
| L3 | Algoritmos de planificación | Métricas que faltan: tiempo de espera, rendimiento (productividad) y utilización de la CPU; y la planificación por prioridades fija genérica, que hoy sólo aparece dentro de MLFQ y Windows | 9 | Buscar fuente para cada definición |
| L4 | Concurrencia | Soluciones por programa (Dekker, Peterson), monitores y paso de mensajes. El tema dice que «no se han leído en fuente», pero OSTEP cap. 28 (ya citado) trae el recuadro **«Dekker’s and Peterson’s algorithms»** y OSTEP tiene el apéndice «Monitors» (threads-monitors.pdf, en línea el 06-10-2026) | 13 | OSTEP 28 y apéndice de monitores; para paso de mensajes, buscar |
| L5 | Gestión de procesos (hilos) | Hilos de usuario y de núcleo y los modelos uno a uno / muchos a uno / muchos a muchos | 15 | Buscar fuente (Microsoft Learn sobre UMS/fibras sirve sólo de apoyo parcial) |

Prioridad para el remate (Opus, porque amplía): L4 (fuente ya a mano y la declaración de «no leído»
queda desmentida), L3 y L2 (preguntas de cálculo y de concepto muy probables en el test), L5, L1.
Si alguna no se confirma en fuente, se declara en «Lo que este tema no da», como pide el encargo.
La gestión de memoria (paginación, memoria virtual) queda fuera con razón: el enunciado no la nombra.

## Lentes automáticas

Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

`29-T05-preguntas.md` y este informe. Descargas de OSTEP en el directorio temporal de la sesión.
El tema no se ha tocado.
