# Remate · Oficial Técnico Electricista (27) · Tema 10 · Reglamento de instalaciones térmicas en los edificios

Fase 5. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/10-reglamento-de-instalaciones-termicas-en-los-edificios.md`.
Entradas: `27-T10-refutacion.md` (M1-M3, L1, L2 y una observación) y `27-T10-preguntas.md` (8, 9, 13, 14, 15).
Fuente releída el **05-10-2026** (reloj del sistema; el encargo dice «hoy es 24-09-2026»; el RITE no
tiene redacción posterior al 01-07-2021): RITE consolidado, `fuentes/canal-sur/BOE-A-2007-15820.md`,
líneas 543-544 (art. 31.6), 1661-1666 (IT 1.2.4.8), 1767-1786 (IT 1.3.4.1.2.7), 2375-2380 (IT 3.8.2.2
y 3.8.3) y las cabeceras de redacción de los arts. 1 a 44.

Ficheros tocados: el tema y este informe.

## Cada corrección, comprobada en la fuente

| Hallazgo | ¿Lo confirma la fuente? | Aplicado |
|---|---|---|
| M1 · art. 31.6 cortado | Sí: sigue «y a las condiciones técnicas de la normativa bajo cuya vigencia fueron autorizadas.» y un párrafo sobre la adecuación que pueden acordar las comunidades autónomas | Sí, 5.3 |
| M2 · IT 3.8.3 sin la salvedad del uso cultural ni la ubicación | Sí, literal | Sí, 4.8 |
| M3 · falta la IT 3.8.2.2 | Sí, literal | Sí, 4.8 (con remisión a 2.5) |
| L1 · IT 1.2.4.8 | Sí, literal. No se escribe en el tema que la introdujo el RD 178/2021: el volcado no da redacción por instrucción técnica y no se ha podido confirmar | Ampliación, final de 2.4 |
| L2 · IT 1.3.4.1.2.7, apartados 2.3, 3.1, 3.2, 4.2 | Sí, literal (7,5/10 cm²/kW, menos de 10 m, 50/30 cm, 10·A, 20 Pa, 250 cm²) | Ampliación, 3.3; quitado de «Lo que este tema no da» |
| Observación · portada | Confirmado en las cabeceras: arts. 1, 8, 13, 14, 27 y 43, «1 redacción(es) en total», aplicable desde 20080229 | Sí, portada |

El informe de refutación no se equivocó en nada; no hay corrección rechazada.

## Pasajes cambiados

1. **Portada.** «Fuente»: se añade IT 1.2.4.8. «Redacción que se estudia»: se añade «y los artículos 1,
   8, 13, 14, 27 y 43 conservan la redacción original, aplicable desde el 29/02/2008». «Extensión»:
   16.400 → 17.100 palabras.
2. **2.4, al final (nuevo, L1).** Párrafo y cita de la IT 1.2.4.8: evaluación global; obligación de
   evaluar al instalar, sustituir o mejorar; documentarla en el proyecto o memoria técnica;
   inspeccionable y sancionable; resultados al propietario; definición de eficiencia energética
   general; documento reconocido. Cierra con una línea de oficio (declarada) sobre la sustitución de
   un generador.
3. **3.3, ventilación (ampliado, L2).** La frase sobre 5 cm²/kW y 1,8·PN + 10·A pasa a lista de tres
   tipos: orificios (2.1 y 2.3, gases), conducto (3.1 y 3.2), forzada (4.1 y 4.2). Una negrita del
   apartado 3.2 que salió parafraseada se rehízo literal tras pasar `negritas.py`.
4. **4.8 (M3).** Tras la cita de la IT 3.8.2.1, la IT 3.8.2.2 literal con remisión al epígrafe 2.5.
5. **4.8, «Información y control» (M2).** Primer punto: ubicación del visualizador y salvedad del uso
   cultural (un único dispositivo en el vestíbulo).
6. **5.3 (M1).** Art. 31.6 completo, con su segundo párrafo.
7. **«Lo que este tema no da».** Fuera «ventilación natural por conducto».
8. **Trazabilidad.** IT 1.2.4.8 en la lista; en «oficio», el aviso sobre la sustitución de un generador.

Antecedentes releídos: «dicha evaluación» (2.4) tiene delante la cita de la IT 1.2.4.8; «El mismo
apartado añade» (5.3) sigue a la cita del art. 31.6; los «apartado 2.1… 4.2» de 3.3 cuelgan de la
IT 1.3.4.1.2.7, nombrada en la frase anterior; «Todas estas medidas» (2.4) sigue a la lista de
medidas del epígrafe.

## Preguntas

Con el tema rematado, las 15 salen enteras: 8 (2.4), 9 (3.3), 13 (5.3), 14 (4.8), 15 (4.8 y 2.5).

## Lentes

- `indice.py`: 17.081 palabras, 42 epígrafes, índice sin cambios (el tema no está en `portadas.tsv`;
  la extensión de la portada se puso a mano).
- `negritas.py` (contra el RITE): 311 negritas; 8 no están en el RITE, todas previas (2 rótulos y 6
  del Real Decreto-ley 14/2022, que no se pasó como fuente; ya cotejadas en verificación); 2
  «atribuidas a otro artículo», previas. Ninguna nueva.
- `refutar_exactitud.py`: 119 citas, 92 «no literales» (antes 105/78): las 14 nuevas son citas a IT,
  que la lente lee como artículo; cotejadas a mano, literales.
- `refutar_modo.py`: 0. `refutar_prosa.py`: 0.

## Para la fase 5 bis

Hubo ampliación (pasajes 2 y 3): toca revisión de los pasajes cambiados por otro Opus.
