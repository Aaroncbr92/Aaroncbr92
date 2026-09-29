# Realizador/a (puesto 33) · Tema 11 · Fase 3, verificación

Fecha de trabajo: 24-09-2026 (fecha del encargo); fuentes releídas en esta sesión, el 29-09-2026
(fecha del sistema). Tema: `temas/canal-sur-especificos/33-realizador-a/11-sonido-para-realizacion.md`
(11.847 palabras según `indice.py`, 55 epígrafes; antes 11.800 aprox.).

## Fuentes releídas

| Fuente | Fichero | Qué se ha comprobado |
|---|---|---|
| EBU R 37-2007 (PDF de la UER) | `r037.pdf` / `r037.txt` del scratchpad de la investigación | Todas las citas de § 5; título, «Geneva / February 2007»; Tabla 1 cotejada por coordenadas de palabra en el PDF: «Sound before picture» sobre «≤ 40 ms», «Sound after picture» sobre «≤ 60 ms»; que la R 37 no explica la asimetría ni por qué los márgenes por etapa son menores |
| RD 1680/2011 (BOE-A-2011-19599; BOE núm. 302, de 16-12-2011) | `fuentes/canal-sur/realizador/BOE-A-2011-19599.txt` | 0905 (título; RA 3 a), e), h); RA 5 a); contenidos «Dinámica del uso…» y «Coordinación de efectos…»); 0910 (título; RA 4 c), d)): todas literales y en su módulo, RA y letra |
| RD 500/2024 (BOE-A-2024-10685) | `fuentes/canal-sur/realizador/BOE-A-2024-10685.txt` | Fecha (21 de mayo); en el RD 1680/2011 sólo añade anexo III (profesorado, «Cuarenta») y aparece en la tabla de créditos: no toca RA ni contenidos de 0905 y 0910 |
| Libro de Estilo, 1.ª ed., marzo de 2004 | copia normalizada `le-nfkc.txt` del scratchpad | 8.6.1, p. 122: punto 2 (telas) y punto 6 (adornos), literales; 8.3.2 («en la despedida sólo habla el presentador») |
| EBU Tech 3343-2023 | `tech3343.txt` del scratchpad | Título («Guidelines for Production of Programmes in accordance with EBU R 128», Ginebra, noviembre de 2023); § 3.5.2 «Show», cita literal |

Lentes: `negritas.py` con RD 1680/2011, Libro de Estilo, R 37, Tech 3343, Tech 3347 y Tech 3326: 86
cotejadas, 39 «no están»: todas de pasajes copiados de temas cerrados (Shure, DPA, Clear-Com, Yamaha,
Soundcraft, ATEM, ST 2110-10 y dos del Libro de Estilo con ligaduras); todas las citas nuevas o
adaptadas se hallan. `refutar_exactitud.py` y `refutar_modo.py` con el RD: 0 hallazgos (el RD se
cita por RA y letra, no por artículo; cotejado a mano). `refutar_prosa.py`: 0. `indice.py`: 55
epígrafes, índice correcto.

## Lo copiado: sólo comprobación de literalidad

Cotejo por script, párrafo a párrafo y celda a celda (sin negritas), contra 28-03, 28-06, 28-08, 28-12,
28-15, `realizacion/09` y `realizacion-tv/17`, con diff de palabras en lo que no casaba:

- **Copiado del común**: literal. Las únicas diferencias son las declaradas (remisiones quitadas o
  cambiadas en «La escucha del control», «Dónde se usa el IFB», «Cómo se monta en la mesa», «Los
  monitores del plató», «Cuatro hilos», «Cómo se habla con sonido», «Las capas», «Sistema único»,
  «La redundancia», PTP, supuesto punto 1; «el CNAF» → «la norma de atribución de frecuencias»;
  última columna de la tabla de la Tech 3347; párrafo del operador de sonido quitado en «El directo
  se pacta antes»).
- **Copiado de RTVE sin cambios** (alimentación fantasma, tabla de patrones, tabla de usos del
  retardo): literal.

Lo adaptado, verificado: las remisiones nuevas apuntan a epígrafes que existen (§ 1, § 2, § 3, § 4,
«El N-1», «Pocos micrófonos abiertos»; tema 4 «Comunicaciones», sincronizadores y «IFB e intercom no
son lo mismo»; tema 13 código de tiempo y doblaje; tema 15 «Directos IP»; tema 6 llamadas y órdenes;
tema 18). «Norma de atribución de frecuencias»: correcto y genérico. Nueva columna de la tabla Tech
3347: coherente con la frase copiada «el comentario es programa». Párrafo RTVE «una señal no se puede
adelantar…» y tabla diegético/extradiegético: literales salvo lo declarado.

## Correcciones aplicadas

| # | Pasaje | Error | Antes → ahora | Fuente |
|---|---|---|---|---|
| 1 | § 5, «Qué pide la R 37 a la cadena» | 6 | La cita empezaba en «Member organisations should…» y omitía la salvedad → «siempre que se pueda» y cita desde **«That, whenever possible, Member organisations should…»** | R 37, p. 2 |
| 2 | § 5, «Qué es la sincronía labial» | 6 | Umbral del 50 % sin su condición → se añade **«under the viewing conditions defined in EBU Recommendation R28»** | R 37, p. 2 |
| 3 | § 5, «Los márgenes», primera viñeta | 9 | Que los márgenes por etapa son menores «porque los desfases se van sumando» figuraba como «lectura de la tabla» → «oficio: la R 37 no da la razón» | R 37 (no lo dice) |
| 4 | § 1, tabla del plató (Público) | 9 | «guía de la UER para mezclar programas» → «guía de la UER para producir programas conforme a la R 128» (es su título y su objeto) | Tech 3343, portada |
| 5 | Ficha, Fuente | 9 | La Tech 3343-2023, citada en el texto, no figuraba → añadida | — |
| 6 | Siglas | 5 (a la inversa) | VoIP presentada y nunca usada → quitada | — |
| 7 | Trazabilidad, fila RTVE | 1 | «(el sonido; producción de programas directos y grabados)»: de `realizacion-tv/18` no se toma nada; las dos fuentes son los temas «El sonido» → «(el sonido, en Realización Televisión y en Realización Asistencia)» | Títulos de `realizacion/09` y `realizacion-tv/17` |
| 8 | Trazabilidad, fila R 37 | — | Se añaden la condición de la R 28 y «whenever possible» | R 37 |

Releídos los pasajes cambiados: cada «la R 37», «otra recomendación» y «su título» tiene delante su
antecedente.

## Comprobado sin hallazgo

- RD 1680/2011: ocho citas literales, módulo, RA y letra correctos; título de los módulos 0905 y 0910;
  «nueve puntos» del esquema del 0910 RA 4 d) (recuento correcto); ficha de Normativa (fecha, BOE,
  modificación por el RD 500/2024).
- R 37: fecha, título, cifras 5/15 ms y 40/60 ms, destello de un fotograma en blanco de pico y pitido
  de 1 kHz al nivel de alineación, conservación en ficheros, «should». Cálculos 340 × 0,06 = 20,4 m y
  1/25 = 40 ms: correctos y declarados.
- LE 8.6.1 punto 6 y p. 122; 8.3.2 en el supuesto del realizador.
- Tabla del realizador: RA 3 e), LE 8.6.1 y 8.3.2 bien atribuidos; el sentido de la corrección del
  desfase coincide con el párrafo adaptado de RTVE.
- «Lo que este tema no da»: BT.1359-1 declarada como no leída; sin cifras suyas en el tema.

## Para la refutación

- Quedan como oficio declarado: lectura de conjunto del RD, planos en plató, coordinación y hoja de
  microfonía, asimetría de la R 37 y suma por etapas, dónde se pierde la sincronía, tabla del
  realizador (incluido «confidente en el ayudante o el productor»: el tema 4 sólo pone el ejemplo de
  la ayudante).
- «La sonoridad… aquí sólo se nombran»: el supuesto copiado de 28-08 da −23 LUFS, ±1 LU y −1 dBTP;
  no se ha tocado (copiado del común).

## Ficheros tocados

- Modificado: `temas/canal-sur-especificos/33-realizador-a/11-sonido-para-realizacion.md`.
- Creado: este informe. Copia previa del tema y guiones de cotejo, en el scratchpad
  (`v33t11/`), fuera del repositorio. Ningún otro fichero.
