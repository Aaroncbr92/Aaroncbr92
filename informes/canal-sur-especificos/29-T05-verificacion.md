# Puesto 29 · Tema 5 · Verificación (fase 3)

Fecha: 05-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/05-sistemas-operativos.md`. Copia previa en el
directorio temporal de la sesión (`29t05-antes-verif.md`).

## Fuentes y fecha de lectura

Todas releídas el 05-10-2026, sobre las descargas de la redacción (mismo día) y una nueva:

| Fuente | Comprobación |
|---|---|
| OSTEP caps. 2, 4, 5, 6, 7, 8, 10, 26, 28, 30, 31, 36 (v1.10) y 32 (v1.20) | Versión y © de cada capítulo confirmados contra la Trazabilidad (2008–23: caps. 4, 6, 7, 8; 2008–25: 2, 5, 10, 26, 28, 30, 31, 36; 2008–26: 32) |
| Microsoft Learn es-es: «Modo de usuario y modo kernel», «Información general sobre los componentes de Windows» (15-06-2023), «Procesos y subprocesos», «Multitarea», «Prioridades de programación», «Modificadores de contexto» | Texto completo |
| Microsoft Learn es-es, «Biblioteca de kernels en modo kernel de Windows» | **Descargada de nuevo** (no estaba en las descargas de la redacción) |
| docs.kernel.org «EEVDF Scheduler»; LKMPG (edición September 7, 2026, autores confirmados); minix3.org | Texto completo |

## Método

1. Literalidad: script que normaliza ligaduras, comillas y saltos y busca cada negrita «…» (troceada
   por […]) en las fuentes: **189 fragmentos, 0 sin encontrar** (antes de añadir la página de la
   biblioteca de kernels, 1 sin encontrar: la definición de kernel; ahora confirmada).
2. Prosa en redonda: cada dato, cifra y paráfrasis releído en su pasaje con los nueve errores delante.
3. Cálculo propio rehecho: ejercicio de aplicación (FIFO 8,33/5; SJF 5/1,67; RR 6,67/1; SJF 6 y
   STCF 5 con llegadas distintas) y ejemplos del manual (110, 50, 103,33, 50 s; 10 % y 1 %): correctos.

## Copiado del común / de RTVE sin cambios

Nada del común. Los cinco pasajes de RTVE sin cambios se comprobaron sólo por literalidad (script que
compara texto normalizado y sin negritas con RTVE 14): los cinco aparecen tal cual. No se re-verifican.
Lo adaptado de RTVE (tabla de tipos de núcleo, función del núcleo en Unix, función del gestor de E/S)
sí se verificó.

## Hallazgos y correcciones (10)

| # | Error | Pasaje | Corrección |
|---|---|---|---|
| 1 | 9 | § 2: la agrupación (*coalescing*) presentada como «remedio parcial» del *livelock*; «dos riesgos» y sólo uno | OSTEP 36: el remedio del *livelock* es volver a veces al sondeo; la agrupación es una optimización que rebaja el coste de atender interrupciones a cambio de latencia. Reescrito |
| 2 | 6 | § 5 SJF: «Si todos los trabajos llegan a la vez, SJF es óptimo» | OSTEP 7 lo dice con sus supuestos (sólo CPU, duración conocida): añadidos |
| 3 | 6 | § 5 STCF: «STCF es óptimo» | **«given our new assumptions»**: añadida la salvedad |
| 4 | 6 | § 7: «aproximadamente 20 milisegundos» sin la advertencia | Añadido literal **«La duración del período de tiempo depende del sistema operativo y del procesador.»** |
| 5 | 6 | § 6: términos «todos acuñados por Dijkstra» | **«Virtually all»**: «casi todos» |
| 6 | 6 | § 6 cerrojos: «La solución más antigua» | **«One of the earliest solutions»**, ideada para un procesador: corregido |
| 7 | 6 | § 6 prevención: «la técnica más práctica» | **«Probably the most practical»**: «probablemente» |
| 8 | 6 | § 4 hilos: «dos razones» | **«at least two major reasons»**: «al menos dos» |
| 9 | 9 | § 4: fibra y grupo de subprocesos como «unidades más ligeras» | Microsoft no lo dice (el grupo es una colección de hilos): «otras dos piezas» |
| 10 | 9 | § 3 y «Lo que este tema no da»: Windows «no lo clasifican» | La página de la biblioteca de kernels dice **«El término microkernel no se aplica al kernel actual que se usa en el sistema operativo Windows.»** Añadido; sigue sin clasificarse como monolítico ni híbrido |

Trazabilidad: la lista de oficio añade la función del núcleo en Unix y Linux (adaptada de RTVE, sin
fuente leída) y lo que mete cada tipo de núcleo en la tabla; la fila de Microsoft añade el dato del
micronúcleo. Ficha: extensión 9.800 → 10.000 palabras.

Sin hallazgo en: cita cruzada (1), ley por reglamento (2), «podrá»/«deberá» (4), siglas (5),
redacción derogada (7), artículo mal (8). Tema técnico sin norma: no proceden `negritas.py`,
`refutar_exactitud.py` ni `refutar_modo.py`.

## Lentes tras corregir

`refutar_prosa.py`: 0 hallazgos. `indice.py`: 10.002 palabras, 45 epígrafes. Antecedentes de los
pasajes cambiados releídos («para ese caso» → *livelock*; «esos mismos supuestos» → los del párrafo
de SJF, repetidos entre paréntesis).

## Ficheros tocados

El tema y este informe. Descarga de trabajo (`web/klib.*`) y copia previa en el directorio temporal
de la sesión.
