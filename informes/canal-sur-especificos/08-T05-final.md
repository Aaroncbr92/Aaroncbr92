# Puesto 08 · Tema 5 · Fase 5 bis · Revisión de los pasajes del remate

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/05-iluminacion-basica.md`.
Alcance: sólo los pasajes listados en `08-T05-remate.md`, localizados por diff contra la copia previa
del remate (`scratchpad/t05r/05-antes-remate.md`).

## Fuentes releídas (todas el 24-09-2026)

- EBU Tech 3355 (copia local `t3355.txt`): escalas 1 y 2 del Qa (Figure 4) e «Illuminant D65» (Anexo 4).
- Sony, *PXW-Z100 Operating Guide*, 4-484-009-11(1), © 2013 (copia local `cam08/z100.txt`): tabla de preajustes, aviso de parpadeo, especificación «“Outdoor” (5 600K)».
- Sekonic, ficha del SpectroMaster C-800 (`t05r/c800.txt`).
- Adobe, página «low-key-vs-high-key-lighting» (adobe.com; la URL «high-key-vs-low-key» da 404). Tres citas confirmadas letra a letra con WebFetch.

## Resultado por pasaje

| Pasaje | Veredicto | Acción |
|---|---|---|
| M1 TLCI, dos escalas (cita EBU) | Literal correcto | Ninguna |
| M2 «Illuminant D65» | Literal en EBU (p. Anexo 4); sigla CIE ya no se usa | Ninguna |
| M3 quitar *ATW* | Correcto | Ninguna |
| Medir el color de una fuente | «Los actuales son espectrómetros»: generalización sin fuente (error 9). Citas Sekonic literales; IRC/TLCI en «such as CRI, TM-30, SSI, TLCI/TLMF» | Se sustituye por lo que dice la ficha: «Spectrometer (Color Meter)» e «Illuminance Meter» |
| Sodio y mercurio | «Su luz no es la de un cuerpo negro, así que ningún balance la deja neutra»: dato espectral que el propio remate declara no confirmado (error 9, y contradice «Lo que no da») | Se quita; se pone el aviso literal de Sony «may flicker or change colors» |
| Clave alta y baja | Tres citas Adobe literales; antecedente «tabla del epígrafe anterior» correcto (Bajar o subir el contraste) | «Predominan los tonos claros» marcado como oficio; «Predomina la sombra» sustituido por el literal «a majority of the scene in shadow» |
| Altura del sol | Cálculos correctos (1/tan10° = 5,67; 1/tan30° = 1,73; 1/tan45° = 1; 1/tan60° = 0,58). «Mediodía: a 60° o más» presentado como general (error 6, salvedad omitida) | Fila: «Mediodía con el sol alto»; frase nueva: las alturas son ejemplos, dependen de fecha y latitud |
| Preajuste Sony amanecer/atardecer | Literal correcto; la inferencia «sin compensar» se apoya en el valor del preajuste | Se añade «“Outdoor” (5 600K)» literal |
| Portada, preguntas, Lo que no da, Trazabilidad | Coherentes | Trazabilidad: filas Sony y Sekonic completadas |

Antecedentes releídos: «epígrafe «El parpadeo»» existe (posterior, citado por nombre); «esas lámparas», «esas horas», «la primera / la segunda» tienen su antecedente inmediato.

## Lentes

`indice.py`: 8.637 palabras, 38 epígrafes. `refutar_prosa.py`: 3 avisos de siglas (PUB, PXW, URSA), los mismos de antes; sin hallazgo.

## Ficheros tocados

Sólo el tema 5 y este informe.
