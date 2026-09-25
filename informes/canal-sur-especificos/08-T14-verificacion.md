# Puesto 08 · Tema 14 · Fase 3 · Verificación

Tema: `temas/canal-sur-especificos/08-camara-operador/14-prevencion-riesgos-exteriores-conduccion-cargas-clima.md`
(13.444 palabras tras la verificación; 46 epígrafes). Fecha de trabajo y de lectura de todas las
fuentes: **24-09-2026**.

Saltado, como manda el encargo: los pasajes listados bajo «Copiado del común» en `08-T14-redaccion.md`
(LPRL 4, 14, 15, 21, 29; Libro de estilo 5.6 en lo ya cerrado; NTP 1090/1091, CNSST, LGSS 156, NTP 502).
Sí verificado: lo nuevo, lo copiado de RTVE (NTP 322 y 462, RD 487/1997, RD 1215/1997, tabla PAS,
situaciones de trabajo) y las ampliaciones del Libro de estilo (atasco, «sesgo de heroicidad»).

## Lentes

- `negritas.py` contra 16 fuentes (BOE, convenios, Libro, guía MMC, NTP): 252 negritas; las no
  encontradas son rótulos, citas del RGC (sin volcado; leídas con `boe.py precepto
  BOE-A-2003-23514 a14/a18/a118`, hoy y `--fecha 20261001`), la redacción original del anexo III.5
  del RD 486/1997 (leída con `--fecha 20230101`), citas de la guía MMC cortadas por guiones blandos
  (comprobadas normalizando: todas literales) y pasajes copiados del común. Las «mal atribuidas»,
  falsos positivos.
- `refutar_exactitud.py` (RD 486, 487, 1215, 773, ET, LPRL): 12 «no literales», todos falsos
  positivos (citas del convenio, del Libro o del RGC con un número de artículo de otra norma);
  comprobados uno a uno a mano.
- `refutar_modo.py`: 0. `refutar_prosa.py`: 0 (antes y después). `indice.py`: regenerado, 46 epígrafes.

## Fuentes releídas (24-09-2026)

`boe.py precepto`: BOE-A-1997-8669 (a1, a7, da, aniii vigente y a 20230101); BOE-A-1997-8670
(a1-a4, a6, an); BOE-A-1997-17824 (ani, anii); BOE-A-1997-12735 (aniii); BOE-A-2003-23514 (a14,
a18, a118, hoy y a 20261001); BOE-A-2015-11430 (a36, a37, a64, a85; a37 a 20250101); BOE-A-2015-3442
(a36.23 y nota STC 172/2020); BOE-A-1995-24292 (a29, recuento). Metadatos BOE (API y diario):
BOE-A-2004-19311 (RD 2177/2004, de 12-11), BOE-A-2023-11187, BOE-A-2024-24840, BOE-A-2024-26693
(Ley 6/2024), BOE-A-2025-24545, BOE-A-2026-13889 (RD 518/2026, de 24-6), BOE-A-2021-962 (BOE núm.
19, 22-01-2021), BOE-A-2021-20261 (RD 1076/2021). Documentos: convenio Interior-FAPE-ANIGP-TV;
X Convenio RTVA (arts. 12, 14, 39, 45, 50, 53; anexos II y III); Libro de estilo 5.6; guía MMC
2024; NTP 322 y 462; INSST, *Socorrismo laboral y primeros auxilios* (2014), 5.2.

## Hallazgos y correcciones aplicadas

| # | Error | Pasaje | Qué decía | Corrección (comprobada en la fuente) |
|---|---|---|---|---|
| 1 | 6 salvedad omitida | «El puesto sale a la calle» | «La definición no incluye conducir» | El anexo III dice que **no es lista cerrada** de funciones; se cita. Conductor/a UM: está en el art. 45 y en el anexo II (la línea 1536 que daba la redacción es del art. 45) |
| 2 | 8 artículo mal | ET 85.1 (texto y «Normativa») | «último párrafo» | Tras la Ley 9/2025 el párrafo de protocolos es el **tercero**; el último es el de movilidad sostenible |
| 3 | 9 / interpretación falsa | Anexo III RD 486/1997 | «el apartado 2 vale en cualquier lugar»; en un plató las cifras «sirven de referencia, no de obligación» | Un plató es local cerrado: el apartado 3 obliga. El apartado 2 se cita con su «en la medida de lo posible»; la unidad móvil queda fuera por el art. 1.2.a) salvo la DA |
| 4 | 5 siglas | ET 2024 | «DANA» sin presentar | Presentada: depresión aislada en niveles altos |
| 5 | 6 salvedad omitida | Convenio art. 53.2 | Omitía «por necesidades del servicio» | Añadido |
| 6 | 6 salvedad omitida | RD 1215, anexo II 4.2.3 | La prohibición de cargas, sin la regla previa ni su condición | Añadida la frase del transporte a mano con sujeción segura y la condición «por su peso o dimensiones» |
| 7 | 6 | RD 1215, anexo II 4.1.1 | Faltaba «y en condiciones ergonómicas aceptables» | Añadido |
| 8 | 3 recuento/selección | Anexo RD 487/1997, grupo 3 | Faltaba el factor «altura segura y postura correcta» (el que más afecta a la cámara al hombro) | Añadido; la tabla es ahora el anexo completo |
| 9 | 1 cita cruzada | Guía MMC, «condiciones ideales» | Daba el ejemplo como definición | Se cita la definición («han minimizado los riesgos…») y luego el ejemplo |
| 10 | 9 | El frío | Manos frías «pierden fuerza y destreza, como dice la guía» | La guía dice entumecimiento y pérdida de destreza manual, no fuerza; corregido |
| 11 | 1 | RGC, reforma | «da nueva redacción a esos preceptos» (tras citar 14, 18 y 118) | Sólo 18.2 y 118 cambian; 14 y 18.1 no. Precisado |
| 12 | 9 | Guía MMC | «15 kg para mujeres, jóvenes y mayores» entre comillas sin fuente | Quitadas las comillas (es la cifra de RTVE que el tema refuta) |
| 13 | 9 | «Lo que no da» | Tablas «de imagen» de las NTP 322 y 462 | La de hipotermia de la NTP 462 está en texto; dejado «tablas… no se transcriben» |

Añadido (dato leído en la fuente, útil para el trabajo nocturno): X Convenio, art. 12.b).9, turno
máximo de siete horas para quien hace la jornada completa entre las 22,00 y las 7,00. Trazabilidad:
añadido el INSST *Socorrismo laboral* (P.A.S., 5.2) como apoyo de la secuencia proteger-avisar-socorrer;
arts. 12 y 45 del convenio en la ficha, «Normativa» y «Trazabilidad». Extensión: 13.400.

## Confirmado sin cambios

RD 486: art. 1.2-1.3, 7.1, DA única (literal, vigente desde el 13-05-2023 por el RDL 4/2023, de
11-5), anexo III.3 y III.5 original. RD 773 anexo III (redacción de 9-12-2021): falta de
visibilidad, frío, nota de la evaluación. RD 1215: anexo I.1.6 (2 m, 90 cm), 4.1.6, 4.2.2-4.2.4.
RGC 14.1, 18.1, 18.2, 18.4, 118.3 y la redacción de 1-10-2026 (18.2 y 118.4, motocicletas). RD 487:
arts. 1.1, 2, 3, 4, 6. Guía MMC 2024: 3 kg, tablas 1, 2 y 5, 25 cm, 1 m/10 m, dos tercios/mitad,
termohigrometría, NIPO 118-24-024-8. ET 36 entero, 37.3.g) (y la segunda g) de la Ley 6/2024, en
vigor 3-3-2025), 64.4.e). Convenio Interior-FAPE: firma 11-12-2020, Resolución de 15-01-2021 (firma
interna del 14), BOE 19, cláusulas 1.ª, 2.ª (1, 2, 3.a, 6, 7), 3.ª (Ministerio, 2), 8.ª; sustituye al
de 17-3-2011. X Convenio: anexo III 5341310, arts. 14.f), 39 (39.066 € y seguro de zonas de riesgo),
50.1 (35 %, 22-7 h), 53.2 (0,27 €/km). Libro de estilo 1.ª ed. (marzo de 2004), 5.6, atasco y
heroicidad. NTP 322 (1991) y 462 (1995): citas, ecuaciones WBGT y las tres alturas; la NTP 322 no
describe cuadros clínicos (declarado). LO 4/2015 36.23 y STC 172/2020 (sólo remisión al tema 12).

## Para la refutación

- La sigla FCSE se presenta pero no se usa en el cuerpo (inofensivo).
- Los cuadros clínicos por calor y la técnica de levantamiento siguen como conocimiento general u
  oficio, sin fuente escrita en el repositorio; así lo declara el tema.

## Otros ficheros tocados

Ninguno fuera del tema y este informe.
