# Puesto 08 · Tema 13 · Fase 3 · Verificación

Fecha: 24-09-2026. Tema:
`temas/canal-sur-especificos/08-camara-operador/13-produccion-movil-y-transmision.md`.
Leídos sólo `ENCARGO.md`, el enunciado del puesto 08 y el informe de redacción (no `metodo/`).
Saltado, por ir listado bajo «Copiado del común»: tabla de cinco vías y viñetas *Satélite* y
*Mochila* («Enlaces») y el párrafo de los puntos 45-46 del Contrato-programa. Sí se ha verificado lo
copiado de RTVE (IG/09 § 1-3; realización/16 § 5 y § 8) y todo lo nuevo.

## Fuentes releídas (todas el 24-09-2026)

| Fuente | Cómo | Resultado |
|---|---|---|
| Libro de estilo CSTV (`libro-de-estilo-333233b.txt`): Introducción (l. 114-135), 4.4 (l. 2616-2621), 4.4.1 (l. 2640-2642), 4.4.4 paso 2 (l. 2683-2688), 5.6 (l. 3012-3013), 8.1 punto 6 (l. 4039-4045), 8.3 (l. 4136-4141), 8.3.2 (l. 4178-4181, 4196-4197); portada (1.ª ed., marzo 2004) | grep + sed | Todas las citas literales; epígrafes bien asignados (comprobados contra el índice, l. 373-450) |
| Contrato-programa (BOJA 245/2023): título del Acuerdo (l. 10-14), cláusula tercera (l. 598), 3.5 (l. 1288), 3.19 (l. 2044), punto 103 (l. 2089-2103) | grep + sed | Cita del 103 cortada a media frase (ver C3); denominación corregida (C2) |
| UIT-R SNG.770-2 (`.txt` local): considerandos c), e), g); recomienda 8 y 9; anexo 1, 1.1 y 2.2.1 | sed | Literales; dos glosas sobredimensionaban una recomendación (C4, C5) |
| UIT, `itu.int/rec/R-REC-SNG.770/en` | curl | SNG.770-2 (01/2012) «In force»; la -1, «Superseded» |
| SMPTE ST 2110-10:2022 (introducción, 1, 6.3, 7.2, 8.5), -20:2022 (1), -30:2025 (1); portadas | sed | Literales; «Approved» 28-03-2022, 14-12-2022 y 01-10-2025; las tres «Revision of … 2017» |
| `pub.smpte.org/doc/2110/` y fichas `st2110-10/-20/-30` | curl | 13 documentos, iguales al índice local; versiones activas 2022, 2022 y 2025 (aviso 2 del redactor, confirmado) |
| draft-sharabayko-srt-01 (`ietf.org/archive/id`) | curl | Cabecera («Informational», «Expires: 11 March 2022», 7-IX-2021), resumen, 1.1 (l. 211-213), 1.2 (l. 274), tabla 2 (AES-128/192/256), *rendezvous* (l. 1802): conformes |
| Datatracker API (`draft-sharabayko-srt`) | curl | stream ISE (Independent Submission), expirado: confirmado (el redactor lo tomaba de la investigación) |
| Haivision/srt: README (l. 26) y `API-socket-options.md` (l. 161-163, 817-825, 1107-1111) | curl | Definición literal; `SRTO_PASSPHRASE` [10..80]; `SRTO_LATENCY` 120 \* ms, el asterisco remite a la descripción, que dice que el valor lo modifica `SRTO_TRANSTYPE`: la glosa «según el modo de transmisión» se sostiene |
| `specs.amwa.tv/nmos/` | curl (HTML, no extractor) | Definición de NMOS y títulos IS-04, -05, -07, -08: literales |
| NDI «What is NDI» y `white-paper/discovery-and-registration` | curl (HTML) | Las cinco citas, literales |
| `LiveU_LU800_ficha.txt` | grep | Las once citas, literales; no hay cifra de latencia (sólo «the lowest latency», l. 9) |
| `Blackmagic_ATEM_manual-es.txt` (l. 1460-1463, 2673-2677, 7645-7646) y `fuentes/fabricantes/README.md` (l. 86) | grep + sed | Citas literales. Título y «diciembre de 2024» no están en el `.txt` (sólo «© 2024»); constan en la ficha de procedencia del PDF: se mantienen |
| RTVE `informacion-grafica/09` § 1-3 y `realizacion/16` § 5 y § 8 | sed | Copia fiel, con las supresiones que declara el redactor; todo es oficio y va declarado como tal |

## Correcciones aplicadas al tema

| # | Error | Dónde | Antes → después |
|---|---|---|---|
| C1 | 9 afirmación sin fuente | Mochilas: tabla «Lo que no puede prometer», punto 2 de «El retardo…», último párrafo de ese `###` | «un retardo, de segundos», «con segundos de retraso», «se mide en segundos» → quitada la magnitud. No hay fuente leída (la ficha LU800 no da cifra) y el propio tema dice en «Lo que este tema no da» que no hay cifra de latencia de mochila. Ese punto de «no da» también cambia: «La latencia en milisegundos de una mochila…» → «La latencia de una mochila…» |
| C2 | 9 / nombre de la fuente | Ficha, «El *streaming* en Canal Sur», Trazabilidad | «Contrato-programa 2024-2026 de la RTVA y Canal Sur» → «… entre el Consejo de Gobierno de la Junta de Andalucía y la RTVA» (título del Acuerdo de 19-XII-2023) |
| C3 | 6 salvedad omitida | Punto 103 | La cita se cortaba en «servicios ‘a petición’» a media frase; completada hasta «…contenidos audiovisuales.» (ámbito mundial **conforme a la posesión de derechos**) y añadida una línea que lo dice |
| C4 | 4 «podrá» por «deberá» | UIT-R, viñeta «Comunicación» | «llevada a la norma: no se transmite sin un canal…» → «llevada a una recomendación: contar, antes y durante la transmisión, con un canal…» (recomienda 8 es una recomendación) |
| C5 | 9 / 8 | UIT-R, viñeta «Autorización» | «Una unidad de satélite no se enciende sin permiso» (no lo dice recomienda 9) → que la activación requiere autorización lo presupone la Recomendación, que la quiere **«expeditiva»** (considerando e). Añadido considerando e) a Trazabilidad |
| C6 | 9 (sujeto de la cita) | UIT-R, viñeta «Tamaño» | «el terminal **«debe poderse…»**» → «el equipo DSNG» (en 1.1 el sujeto es «el equipo») |
| C7 | 9 | Ficha, «Redacción que se estudia» | «en su única edición publicada» (no confirmable) → «en su primera edición (marzo de 2004), que es la leída» |
| C8 | completitud | Normas técnicas | ST 2110-20: añadido «revisa la de 2017» (portada) |
| C9 | fecha de lectura | Trazabilidad, filas ST 2110 e índice SMPTE | Índice y fichas de versiones releídos hoy; «Qué sostiene» añade fechas y ediciones activas |
| C10 | ficha | Extensión | 7.200 → 7.400 palabras (`indice.py`: 7.377) |

## Comprobado y sin cambios

- Recuentos: cuatro áreas coordinadas (8.3); cuatro datos UIT-R; tres motivos; tres
  consecuencias; nueve partes ST 2110 más OV 2110-0 y RP 2110-23/24/25; no existe -50; cuatro IS.
- «should» / «shall» / «may» de ST 2110-10 (7.2 y 8.5) bien traducidos.
- Remisiones a temas 3, 7, 8, 11 y 14: cuadran con el enunciado. Remisiones internas («Mochilas»,
  «Señales IP», «Coordinación con control») con antecedente.
- Aritmética: 1.000 ÷ 25 = 40 ms; 2 → 80; 4 → 160; a 50 fps, 20 ms.
- Siglas: todas presentadas antes de usarse, salvo IP en el título (aviso no aplicable, igual que
  en el tema 3).
- Aviso 4 del redactor: «8.1, punto 6» es correcto (punto 6 de la lista de 8.1; no hay epígrafe 8.1.6).

## Lentes

Tema técnico sin norma jurídica: `refutar_prosa.py` (1 aviso no aplicable: IP en el título) e
`indice.py` (índice regenerado, 35 epígrafes). Pasajes cambiados releídos: cada «la
Recomendación», «ese», «el mismo Contrato-programa» conserva su antecedente.

## Ficheros tocados

El tema 13 y este informe. Descargas de SRT, NMOS y NDI en el scratchpad (fuera del repositorio).
