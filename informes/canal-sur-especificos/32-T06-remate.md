# Productor/a (puesto 32) · Tema 6 · Remate

Fase 5. Tema: `temas/canal-sur-especificos/32-productor-a/06-recursos-tecnicos-y-materiales.md`.
Entradas: `32-T06-refutacion.md` y `32-T06-preguntas.md`. Cada corrección se comprobó en la fuente
antes de aplicarla. Fecha de trabajo y de lectura de las fuentes: 25-09-2026 («hoy» del encargo:
24-09-2026).

Ficheros tocados: el tema, este informe y cuatro fuentes nuevas guardadas en
`fuentes/normas-tecnicas/`: `UIT-R_V.431-8.pdf/.txt` (descargada de itu.int el 25-09-2026) y
`SMPTE_ST-12-1-2014.pdf/.txt` (descargada de pub.smpte.org el 25-09-2026; la de 2014 es la última
versión publicada de ST 12-1).

**Amplió contenido nuevo: sí** (lagunas 1 y 2; unas 420 palabras). Procede la fase 5 bis sobre los
pasajes 4 y 5.

## Correcciones: las tres confirmadas y aplicadas

| # | Hallazgo | Fuente comprobada | Resultado |
|---|---|---|---|
| Menor 1 | «El único inventario publicado» | Coherencia con la «Advertencia» del propio tema (sólo consta el de la Cámara de Cuentas; no se puede afirmar que no exista otro) | Aplicada: «El único inventario publicado que se ha localizado» |
| Menor 2 | Emisiones «lo comprueba antes de programarlo» | Convenio, anexo III, Secretario de emisiones (l. 7105-7130): «Recepcionar, comprobar y archivar el material programado.» | Aplicada: «que recibe, comprueba y archiva el material programado» |
| Menor 3 | Doble «y» en la enumeración de cuatro puestos de iluminación | Redacción | Aplicada |

## Lagunas: ampliadas con fuente

| Pregunta | Fuente leída | Qué se añade |
|---|---|---|
| 11, bandas del DSNG («no») | UIT-R SNG.770-2, anexo 1, 2.1.2, 2.3 y 3.3 (volcado local); UIT-R V.431-8 (08/2015), nota 5 y cuadro 4 | Banda de 14 GHz preferida; 6 GHz más difícil de coordinar; 14 y 30 GHz; ejemplo 14/4 GHz. Letras C (4/6 GHz), Ku (11/14 y 12/14 GHz), K (20 GHz), Ka (30 GHz), con la salvedad de V.431 de que no hay correspondencia normalizada y de que K y Ka se agrupan como Ka |
| 13, código de tiempo («a medias») | SMPTE ST 12-1:2014, 5.2 y 6.2; manual de DaVinci Resolve 21, cap. 58 | Dirección de cada cuadro en hora, minuto, segundo y cuadro; reloj de 24 h; cuadros 00-24 a 25 cuadros/s; *drop frame* sólo en 30; forma «HH:MM:SS:FF» |

La clave de la pregunta 11 (C y Ku, y Ka) queda sostenida por la combinación de las dos
Recomendaciones; la de la 13, por ST 12-1 y el manual. No se ha recortado ninguna pregunta. Lo que
no se ha podido confirmar no se ha escrito (atenuación por lluvia según la banda; la cadencia de
cuadros de Canal Sur).

## Pasajes cambiados

1. **Siglas de entrada**: añadida «servicio fijo por satélite (**SFS**)».
2. **Qué se puede preguntar**: «y en qué bandas trabaja» (DSNG) y «cómo se escribe el código de tiempo».
3. **«Los medios de la RTVA: lo que consta publicado»**, primer párrafo: «publicado que se ha localizado».
4. **Nuevo epígrafe `###` «Las bandas de frecuencia del DSNG»** (en «Enlaces», tras «Lo que la UIT-R
   pide al equipo de satélite»): dos párrafos, tabla de letras y cierre. Índice regenerado.
5. **«La lista de decisiones de edición»**: nuevo segundo párrafo sobre el código de tiempo.
6. **«Quién diseña la luz y quién la monta»**: quitado el primer «y» de la enumeración.
7. **«La continuidad en la RTVA»**, último párrafo: la frase de emisiones, con el literal de la ficha.
8. **Ficha (Fuente)** y **Trazabilidad**: añadidas V.431-8 y ST 12-1:2014; ampliada la fila de la
   SNG.770-2 (2.1.2, 2.3, 3.3); fila del manual de Resolve 21; frase de fecha de lectura en el
   remate; en la lista de oficio, «el satélite (salvo las bandas, con fuente)» y «la EDL (salvo el
   código de tiempo, con fuente)».

Relectura de antecedentes: «esas bandas» (pasaje 4) remite a las de 4, 6, 14 y 30 GHz citadas justo
antes; «del mismo cuadro» remite al cuadro 4 de la V.431-8, nombrado en el párrafo anterior; «las dos
Recomendaciones», a la SNG.770-2 y la V.431-8; «Lo define» y «lo escriben» (pasaje 5), al código de
tiempo, sujeto de la frase previa; «(5.2 y 6.2)» va tras la mención de ST 12-1:2014. Sin
referencias colgantes.

## Lentes

- `indice.py`: índice regenerado (un epígrafe más); 15.741 palabras, 86 epígrafes (la ficha anuncia
  15.000 aproximadamente).
- `negritas.py` (convenio, Cámara, contrato-programa, Carta, Libro, Ley 13/2022, SNG.770-2, V.431-8,
  ST 12-1, Resolve 21): 141 cotejadas; 24 «no está», todas preexistentes (rótulos, RD 16/2023 y
  250/2025, SMPTE 2110, Libro con ligaduras, etc.) salvo una nueva, «Conviene utilizar bandas…», que
  en el volcado de la SNG.770-2 cruza un salto de página («Rec. UIT-R SNG.770-2 / 7» en medio); leída
  a mano, literal. 0 mal atribuidas.
- `refutar_exactitud.py` (Ley 13/2022): 7 avisos nuevos, todos falsos positivos: emparejan las citas
  «(anexo 1, 2.1.2)», «(3.3)», «(2.3)» y «(5.2 y 6.2)» de la UIT-R y la SMPTE con artículos 2, 3 y
  6 de la ley. Las citas son literales de sus normas (comprobadas por `negritas.py` y a mano).
- `refutar_modo.py`: 0 hallazgos.
- `refutar_prosa.py`: 0 hallazgos.
