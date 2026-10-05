# Verificación · Oficial Técnico Electricista (27) · Tema 18 · Innovación aplicada al mantenimiento

Fase 3. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/18-innovacion-aplicada-al-mantenimiento.md`
(12.886 → 13.087 palabras). Fecha de lectura de todas las fuentes: 05-10-2026 (el encargo fija «hoy» en 24-09-2026;
ninguna fuente citada cambia entre ambas fechas: comprobado con los metadatos del BOE).

**Copiado del común / Copiado de RTVE sin cambios**: el informe de redacción dice «Nada» en las dos listas, así que no
había nada que saltar ni que cotejar con diff: se ha verificado el tema entero.

Ficheros tocados: el tema y este informe. Temporales en el scratchpad (`v18/`), fuera del repositorio.

## Fuentes releídas (05-10-2026)

- RD 244/2019 (`boe.py precepto`): arts. 2, 3, 4, 5 y 14 vigentes; arts. 3 y 4 además con `--fecha` 20230101,
  20250701, 20250801, 20251201, 20251210 y 20260301. Metadatos de la API: BOE-A-2019-5089 (última actualización
  23-03-2026), BOE-A-2026-6544 (RDL 7/2026, de 20 de marzo; vig. 22-03-2026; no derogado), BOE-A-2025-24545 (Ley 9/2025,
  de 3 de diciembre; vig. 05-12-2025), BOE-A-2022-22685 (RDL 20/2022), BOE-A-2021-4572 (RD 178/2021).
- REBT, ITC-BT-40 apartados 1-4.3.4 (volcado de 05-10-2026; redacción del RD 244/2019).
- RITE (volcado): apéndice 1; IT 1.2.4.3.5, IT 1.2.4.4, IT 2.3.4, IT 3.3 (nota de la tabla), IT 4.2.1-4.2.3 (rótulos),
  IT 4.3.1-4.3.4; tabla de redacciones.
- RD 56/2016, art. 3 entero.
- Reglamento (UE) 2023/1542 (volcado): art. 3.1 (puntos 13, 15, 25, 27, 28), 12, 13, 14, 61.1, 77-78 (rótulos), 95, 96;
  anexos V, VI y VII; las cuatro correcciones enteras; ficha del BOE (doc.php), «Referencias posteriores».
- tienda.aenor.com, fichas: ISO/IEC 30141:2024, ISO/IEC 30173:2023, ISO 17359:2018, UNE-EN ISO 52120-1:2022.
- Vista previa oficial de la ISO/IEC 30173, ed. 1.0 2023-11 (elstandard.se/documents/preview/3076501): prólogo y 3.1.1.
  ISO committee.iso.org/standard/81442: fecha 2023-11-08, ed. 1, JTC 1/SC 41.

## Lentes

- `negritas.py` (5 fuentes): 166 negritas; 19 «NO ESTÁ», todas comprobadas a mano: 2 rótulos, 13 de fichas de catálogo
  y vista previa ISO (todas confirmadas en su fuente), 3 de la redacción anterior del art. 3.g).iii (confirmadas con
  `--fecha 20260301`), 1 rótulo de título UNE. 2 «otro artículo», falsos positivos (anexo V tras el art. 96 en el
  volcado; 14.1 citado junto a remisión a «epígrafe 6.3»).
- `refutar_exactitud.py`: 54 citas; 7 «no literales», falsos positivos (toma por artículo números de epígrafe o de
  apartado de IT/ITC: «art. 8», «art. 4», «art. 2»…); todas las negritas están en su precepto.
- `refutar_modo.py`: 0 hallazgos. `refutar_prosa.py`: 0 hallazgos. Índice: rótulos sin cambios.

## Correcciones aplicadas (error del catálogo)

1. **Ficha y «Normativa», redacción del RITE (7)**: decía IT 1, IT 2 e IT 4 en la del RD 178/2021. La IT 2 tiene una sola
   redacción, la original (vig. 29-02-2008; tabla de redacciones). Corregido: IT 1, IT 3, IT 4 y apéndice 1 del RD
   178/2021; IT 2 original.
2. **6.5, pasaporte (9/1)**: «Los artículos que regulan el pasaporte (77 y 78) se rehicieron en una corrección de errores
   de 2024» es falso. DOUE-L-2024-81259 corrige los arts. 77 y 78 **del Reglamento (UE) 2024/1781** (su art. 78 añade un
   apartado 10 al art. 77 del 2023/1542). El aviso del redactor heredaba el error. Sustituido por «El pasaporte lo
   regulan los artículos 77 y 78, y este tema no da su contenido».
3. **Ficha, «Normativa» y «Trazabilidad», Reglamento 2023/1542 (7)**: sólo se declaraban las correcciones; la ficha del
   BOE lista modificaciones: art. 77 (Reglamento 2024/1781), art. 48 (Reglamento 2025/1561) y anexo I (Reglamento
   2026/1738, de 8 de julio). Ninguna toca los preceptos citados; ahora se dice.
4. **6.2, Directiva 2006/66/CE (9)**: «deroga, según su título» (aviso 9 del redactor). Leído el art. 95: **«Queda
   derogada con efecto a partir del 18 de agosto de 2025»**, con disposiciones que siguen aplicándose. Añadido y art. 95
   en «Normativa». La frase «será obligatorio…» es la fórmula final tras el art. 96, no un apartado de éste: precisado.
5. **7.8 (8/9)**: «quien se acoge no podrá participar de otro mecanismo de venta» — el sujeto en el 14.3 es **el
   productor**. Corregido; «la factura puede llegar a cero» marcado como lectura de oficio.
6. **7.9 (6)**: la potencia admisible del 4.3.1 se daba sin la salvedad del 4.3: **«A las instalaciones de autoconsumo sin
   excedentes no les son de aplicación los apartados 4.3.1, 4.3.4»** ni lo del apartado 9 relativo a la distribuidora.
   Añadida.
7. **6.4 (6)**: añadida la salvedad del 12.2.a): los parámetros del anexo V **«solo se aplicarán en la medida en que exista
   un peligro correspondiente»**.
8. **5.4 (6)**: la auditoría cada cuatro años tiene la alternativa del sistema de gestión certificado (art. 3.2.b).
   Añadida.
9. **6.6 (6)**: el 61.1 obliga a los productores **o** a sus organizaciones de responsabilidad del productor. Añadido.
10. **8.4 (9)**: la glosa de las IT 4.2.1-4.2.3 («calefacción, aire acondicionado») no seguía sus rótulos: ahora
    «sistemas de calefacción, ventilación y agua caliente sanitaria; aire acondicionado y ventilación; instalación térmica
    completa».
11. **3.1, UNE-EN 13306 (9)**: la clasificación (predictivo dentro del preventivo basado en la condición) no está leída
    en la norma vigente; la investigación la tomó de una reproducción secundaria de la edición de 2010. Se mantiene con
    ese aviso explícito.
12. **2.1 (9)**: «en vigor desde el 27 de agosto de 2024» → la ficha da fecha de edición y estado, no fecha de vigencia.
13. **4.1 (aviso 3 del redactor)**: confirmadas en la vista previa oficial IEC la definición 3.1.1 con sus remisiones
    (3.1.8) y (3.1.3), las notas 1 y 2 (no hay nota 3 en la versión publicada) y el prólogo: **«subcommittee 41: Internet
    of Things and Digital Twin»**, ahora citado literal; «Trazabilidad» cambia la reproducción secundaria por esa vista
    previa.
14. **5.1**: «IT 2.3.4.4» → «IT 2.3.4, apartado 4» (no existe la IT 2.3.4.4).

## Confirmado sin cambios (muestra de lo que más riesgo tenía)

- Historia del art. 3.g).iii (aviso 1 del redactor): RDL 20/2022 (cubierta, suelo industrial o estructuras, 2.000 m);
  RDL 7/2025 (5 MW, 5.000 m), derogado; vuelve la de 2.000 m (BOE-A-2025-15313); RDL 7/2026: fotovoltaica o eólica hasta
  5 MW, 5.000 m, sin exigencia de ubicación. Correcto.
- Art. 4.5.b): la excepción entra con la Ley 9/2025 (inciso ii., vig. 05-12-2025; ausente el 01-12-2025); el RDL 7/2026
  pasa los incisos a letras. Correcto. Comunidad de energías renovables en el 4.7: correcto.
- Cifras: 100 kW (4.2.a.ii y 3.c), 500 m, 5 MW/5.000 m, 800 VA, 30 mA, 100 kVA, 70 kW / 20 kW (IT 1.2.4.4), 290 kW,
  2 años (IT 3.3), 5 kg, 2 kWh, fechas del Reglamento (18-02-2024, 18-08-2024, 18-08-2025, 18-08-2026, 18-02-2027),
  puntos 13/15/25/27/28 del art. 3.1, los once títulos del anexo V, los diez parámetros del anexo VII. Todo literal.
- Remisiones a otros temas del puesto: tema 12 epígrafes 1.3, 2.3, 3.3, 6.1, 6.2, 7.5; tema 13 1.4; tema 7 4.1:
  existen y tratan lo que se dice.
- Fichas AENOR: 30141 (2024-08-27, En Vigor, resumen y «second edition»), 30173 (2023-11-08, En Vigor, resumen),
  17359 (2018-01-24, En Vigor, resumen), 52120-1:2022 (título, 2022-10-19, En Vigor, «Anula a UNE-EN 15232-1:2018»).

## Pendiente para refutar

- La fecha efectiva de la etiqueta del 13.1 (acto de ejecución del 13.10) sigue sin localizar; el tema no la afirma.
- `indice.py` no procesa el tema (no está en `portadas.tsv`), como avisó el redactor.
