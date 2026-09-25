# Puesto 08 · Tema 6 · Fase 5 bis · Revisión de lo que cambió el remate

Fecha: 25-09-2026 (encargo fechado el 24-09-2026). Tema:
`temas/canal-sur-especificos/08-camara-operador/06-captacion-de-sonido.md`. Alcance: sólo los pasajes
de `08-T06-remate.md`, localizados con un `diff` contra la copia previa al remate.

## Fuentes leídas (25-09-2026)

- DPA Microphones: las seis páginas citadas, **descargadas de nuevo con curl** (no me fié sólo del
  extracto del remate). Las 20 citas en negrita de los pasajes nuevos se cotejaron por programa
  contra el texto de las páginas: 20/20 literales.
- EBU R 68-2000 (`.txt` local), considerandos: «can be 3 dB greater».
- *Libro de estilo* (`.txt` local, líneas 2870-2872): la frase de las dos noticias, literal.
- Sony PXW-Z200 Help Guide (`.txt` local, p. 261): la nota de [1kHz Tone on Color Bars], literal.

## Resultado por pasaje

| Pasaje | Veredicto |
|---|---|
| M1 «pueden quedar» (R 68) | Correcto; antecedente («esos picos») en su sitio |
| M2 cita de las barras | Correcta y completa |
| M3 fila [1kHz Tone on Color Bars] | Nota literal; «Para qué» fiel a la nota |
| M4 frase del cine, borrada | Correcto quitarla; el párrafo queda cerrado |
| XLR y línea balanceada | Citas literales. Dos afirmaciones sin fuente (ver abajo) |
| Efecto de proximidad | Citas literales; la paráfrasis de la causa, fiel a DPA. **«exactly 90 degrees» no estaba en el extracto guardado**: está en la página (apartado «On-axis vs. off-axis»); añadido al extracto |
| «Los ambientes ruidosos» | Cita literal; 6 y 12 dB bien calculados; oficio declarado |
| Siglas EMI, CMRR, SPL | Presentadas antes de su uso |
| Portada, preguntas, índice, Trazabilidad | Coherentes; anclas de índice presentes |

## Correcciones aplicadas (error 9)

1. «va por XLR y no por una clavija de consumo»: DPA no habla de clavijas de consumo. Queda «va por
   XLR, en línea balanceada».
2. «va a una entrada XLR, no al minijack de consumo»: DPA no dice que el minijack sea no balanceado.
   Se marca «(oficio)» y se añade a la lista de oficio de «Trazabilidad».

Sin más hallazgos.

## Lentes

`indice.py`: 10.686 palabras, 45 epígrafes. `refutar_prosa.py`: 0 negritas rotas; los mismos 4
avisos de siglas que en el remate (PXW, DPA, EMC, RFI), sin hallazgo.

## Ficheros tocados

El tema 6; `fuentes/fabricantes/DPA_mic-university_extractos.txt` (se añade el pasaje de los 90
grados); este informe.
