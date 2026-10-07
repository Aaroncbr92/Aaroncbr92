# 04 · Ayudante de Producción · Tema 13 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/13-produccion-de-informativos-y-actualidad.md`.
Fecha de corte: 24-09-2026. Fuentes leídas el 06-10-2026 (fecha del sistema). Ficheros tocados: el
tema y este informe.

## Copiado (sólo literalidad)

Comprobado con un script que busca cada línea de los rangos declarados en `04-T13-redaccion.md`
(común: Redactor/a 03 y 10, Productor/a 02 y 08; RTVE: `produccion/12`, `realizacion-tv/10`)
dentro del tema, quitando las negritas en lo de RTVE: todo literal. Las únicas líneas que no casan
son las de los cambios que declara el redactor (título de 268, 03:338 y 347, 03:427-428,
10:254-256, 08:991-992, 08:1023). Antecedentes de esos cambios comprobados: «en el epígrafe
anterior» (Ley 18/2007, art. 31) tiene delante «Eventos especiales: procesos electorales…»; tema 8
(contratación) y tema 17 (PRL) son los puntos que tocan en este puesto.

Nota sin corregir (pasaje copiado, fuera de mi ciclo): «Libro de estilo, 8.1.7» en «La seguridad del
equipo» es el punto 7 de 8.1 (no hay epígrafe 8.1.7); el mismo tema escribe «8.1, punto 6» más arriba.

## Verificado (lo nuevo y lo adaptado)

- **Libro de estilo** (`libro-de-estilo-333233b.txt`, ligaduras normalizadas): 4.4 (pp. 75: intro,
  plazos, tiempo, desglose), 4.4.1, 4.4.2, 4.4.4 puntos 1, 2, 3, 4, 7, 8, 10; 4.3; 4.3.5; 5.6; cap. 6,
  p. 88 (antes de 6.1); 6.2.1; 6.3.4; 3.17.1.4; 9.2.9; 9.6.3.1; 9.9.1; siglas AFP, EP, UER, FORTA;
  1.ª ed., marzo de 2004; no nombra al Ayudante de producción. Literales y bien numerados.
- **Convenio**, art. 73.3: literal.
- **Ley 13/2022** (BOE-A-2022-11311), arts. 144.1-5 y 145.1: literales; redacción única desde 09-07-2022.
  101.3 cotejado.
- **RD 517/2024** (BOE-A-2024-11377), art. 40.3.a, leído con `boe.py` (redacción única, vigente
  desde 25-06-2024).
- **Convenio Interior-FAPE-ANIGP-TV** (BOE-A-2021-962), cláusula 8.ª: cuatro años desde su eficacia
  tras publicarse (22-01-2021); la salvedad del tema es correcta.
- **SNTV / ACN**: cotejados con `fuentes/institucionales/SNTV_portada.txt` y `ACN_portada.txt` (leídas
  el 02-09-2026): rótulo, «más de 40 deportes», agencia global de vídeo deportivo, empresa conjunta
  de AP e IMG. Señal institucional (RTVE, adaptada): fiel.
- Oficio (recorrido de la convocatoria, tablas de recursos, de recepción de señales, de coordinación
  territorial, de planificación hacia atrás, supuestos): declarado como oficio; remisiones internas
  comprobadas.

## Correcciones aplicadas

| # | Pasaje | Error | Cambio |
|---|---|---|---|
| 1 | «Las agencias», 9.9.1 | 6 salvedad omitida | La regla es para el archivo que ilustra delincuencia, malos tratos, asuntos judiciales…, y sigue: «al menos con suficiente margen como para ser leído sin apremio por el espectador». Añadido el contexto y la frase |
| 2 | «Las agencias», 9.2.9 | 6 | Está en el epígrafe de malos tratos: se dice |
| 3 | «Las agencias», 9.6.3.1 | 6 | Está en el epígrafe de terrorismo: se dice |
| 4 | Convenio 73.3 | 6 | La excepción es «excepcionalmente» y «siempre que no perjudique los intereses legítimos del servicio público» |
| 5 | Supuesto 1, paso 5 | 8 artículo mal | «8.1.6» → «8.1, punto 6» |
| 6 | Supuesto 2, dron | 4/6 | «son cinco días naturales» → «la antelación mínima es de cinco días naturales» |
| 7 | Supuesto 2, registro de origen | 1 cita cruzada | Quitada la cita de 9.9.1 (rotulación de material objetable, no registro): «4.3; lo del archivo, oficio» |
| 8 | «La última hora» | 9 | «no trata la última hora como tal» → «no dedica un epígrafe a la última hora» (la menciona en 3.9.1 y en el cap. 6) |

## Lentes

`negritas.py` (Libro de estilo, convenio, Ley 13/2022): las 51 que no aparecen son rótulos o citas de
otras fuentes que vienen de pasajes copiados (UIT-R, Contrato-programa, Carta, Ley 18/2007, Manual de
RTVE); ninguna de lo nuevo. `refutar_exactitud.py`: ninguna incidencia en 101, 144 o 145 (el resto,
falsos positivos: números de epígrafe del Libro tomados por artículos). `refutar_modo.py`: 0.
`refutar_prosa.py`: 0. `indice.py`: 60 epígrafes, ~12.100 palabras.
