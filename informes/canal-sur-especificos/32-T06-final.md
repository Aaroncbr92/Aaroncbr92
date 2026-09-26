# Productor/a (puesto 32) · Tema 6 · Fase 5 bis (revisión de lo cambiado en el remate)

Tema: `temas/canal-sur-especificos/32-productor-a/06-recursos-tecnicos-y-materiales.md`.
Alcance: sólo los ocho pasajes que lista `32-T06-remate.md`. Fuentes leídas el 25-09-2026 («hoy»
del encargo: 24-09-2026; los textos son los mismos en ambas fechas).
Ficheros tocados: el tema (una frase) y este informe.

## Cotejo por pasaje

| # | Pasaje | Fuente leída | Resultado |
|---|---|---|---|
| 1 | Sigla SFS | SNG.770-2, anexo 1, 2.1.2 (usa «SFS») | Presentada antes de su primer uso (epígrafe de bandas). Correcto |
| 2 | «Qué se puede preguntar» | — | Coherente con los pasajes 4 y 5. Correcto |
| 3 | «publicado que se ha localizado» | Advertencia del propio tema | Coherente. Correcto |
| 4 | Bandas del DSNG | `UIT-R_SNG.770-2.txt`, anexo 1, 2.1.2 (l. 262-270), 2.3 (l. 327-338), 3.3 (l. 412-430, cruza salto de página); `UIT-R_V.431-8.txt`, nota 5 y cuadro 4 (l. 314-381) | Los seis literales, las cifras de la tabla (C 3,4-4,2 / 4,5-4,8 / 5,85-7,075; Ku 10,7-13,25 / 14,0-14,5; K 17,7-20,2; Ka 27,5-30,0), la nota (1) sobre K y Ka y las fechas (01/2012, 08/2015) cuadran. Paráfrasis fieles. Antecedentes («esas bandas», «del mismo cuadro», «las dos Recomendaciones») presentes. Correcto |
| 5 | Código de tiempo | `SMPTE_ST-12-1-2014.txt`, 5.2 (l. 444-455) y 6.2 (l. 506-517); Resolve 21, `speed.txt`, cap. 58 (l. 110-111) | Literales y reloj de 24 h (00:00:00-23:59:59) correctos. **Corregido**: el tema decía que «los programas de edición» escriben «HH:MM:SS:FF», generalizando desde un solo manual (error 9); el manual usa la forma para fijar una duración. Nueva redacción: «El código se escribe en la forma horas:minutos:segundos:cuadros; el manual de DaVinci Resolve 21, por ejemplo, pide las duraciones en formato **«HH:MM:SS:FF»**.» Sujeto explícito («El código») para que no cuelgue tras la frase del *drop frame* |
| 6 | Iluminación, enumeración | — | Sólo redacción; literales intactos. Correcto |
| 7 | Emisiones | X Convenio (BOJA 240/2014), anexo III, Secretario de emisiones (`x-convenio-rtva-boja-240-2014.txt`, l. 7111-7128) | «Recepcionar, comprobar y archivar el material programado.» literal. Correcto |
| 8 | Ficha y Trazabilidad | Las anteriores | Filas de V.431-8, ST 12-1:2014, Resolve 21 cap. 58 y SNG.770-2 (2.1.2, 2.3, 3.3) coinciden con lo cotejado. Correcto |

## Lentes

- `refutar_prosa.py`: 2 avisos («HH», «MM» como siglas sin presentar): falsos positivos, es la
  notación del código de tiempo, explicada en la misma frase.

Resultado: 1 corrección aplicada (pasaje 5); 0 hallazgos en los otros siete pasajes.
