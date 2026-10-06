# Puesto 29 · Tema 5 · Revisión final (fase 5 bis)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/05-sistemas-operativos.md`. Alcance: sólo los
12 pasajes que lista `29-T05-remate.md` (identificados con `git diff` contra el último commit).

## Fuentes releídas (todas el 06-10-2026)

| Fuente | Pasajes |
|---|---|
| OSTEP v1.10, cap. 28 «Locks» (threads-locks.pdf, © 2008–25), recuadro de Dekker y Peterson | 10 |
| OSTEP, apéndice D «Monitors (Deprecated)» (threads-monitors.pdf, © 2008–23) | 10 |
| J. Bell, apuntes CS 385 (UIC), caps. 1, 3, 4 y 6, y página principal | 3, 4, 5, 6, 7, 9, 10, 12 |
| docs.kernel.org, «Deadline Task Scheduling» y «Theory of operation» (Real-time preemption) | 3 |

## Cotejo

- Negritas nuevas: 64, cotejadas por script contra el texto de las fuentes. 64 encontradas, 0 fallos.
- Cálculos rehechos: ejercicio (espera FIFO 5; SJF 5/3 ≈ 1,67; RR cuanto 1 A 4, B 4, C 2, media
  10/3 ≈ 3,33) y prioridades (P2, P5, P1, P3, P4; esperas 0, 1, 6, 16, 18; 41/5 = 8,2). Correctos.
- Paráfrasis en redonda comprobadas en la fuente: Brinch Hansen y Hoare; Lampson y Redell, Xerox PARC;
  semántica de Mesa (de bloqueado a listo, el que avisa sigue hasta salir); C++ sin monitores;
  Dijkstra, Dekker «matemático»; código de Peterson (`flag`, `turn = 1 - self`, espera activa,
  salida bajando `flag`); despachador (cambio de contexto, modo usuario, salto; «as fast as
  possible»); prioridades internas y externas; convenio de 0 como la más alta; hilos que deben
  corresponderse con hilos de núcleo; muchos a uno sin reparto entre CPU; Linux como ejemplo de uno a
  uno; ventajas de muchos a muchos; dos niveles; procesos cooperantes; montaje más o menos difícil;
  colas de capacidad cero, limitada e ilimitada; `SCHED_FIFO`. Correctas.
- Antecedentes: «esos dos estados añadidos», «la tabla anterior», «más abajo» (Windows, 0-31 en
  § 5), «este epígrafe», «los apuntes» y «les dedica un apéndice»: todos tienen delante su referente.

## Correcciones aplicadas (4)

1. § 6 Dekker y Peterson, error 9: «Antes de las instrucciones atómicas se buscó…» contradice la
   fuente, que dice que el apoyo del procesador **«had been around from the earliest days of
   multiprocessing»**. Ahora: «Además de con instrucciones atómicas, se buscó…».
2. § 5 Prioridades, precisión: SJF usa la inversa de **«the next expected burst time»**; «duración
   prevista» pasa a «duración prevista de la próxima ráfaga».
3. § 5 Prioridades, error 9: se atribuía a los apuntes que el ejemplo era no apropiativo y con todos
   los trabajos en el instante 0; los apuntes sólo dan ráfagas y prioridades. Ahora se dice que no
   dan llegadas y que el cálculo supone el instante 0.
4. Trazabilidad: «puestos al día para la primavera de 2013» se corrige según la página principal
   («is currently being updated ( again ) for Spring 2013»): montados en la primavera de 2006 y en
   curso de actualización para la de 2013.

## Lentes

`refutar_prosa.py`: 0 hallazgos. `indice.py`: 51 epígrafes, 12.812 palabras (la ficha dice 12.800
aproximadamente: vale).

## Ficheros tocados

El tema y este informe. Descargas en el directorio temporal de la sesión.
