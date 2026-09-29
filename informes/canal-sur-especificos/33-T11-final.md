# Realizador/a (puesto 33) · Tema 11 · Fase 5 bis, revisión del remate

Tema: `temas/canal-sur-especificos/33-realizador-a/11-sonido-para-realizacion.md`.
Fecha de trabajo: 29-09-2026 (encargo del 24-09-2026). Entrada: `33-T11-remate.md` y `git diff` del tema.
Alcance: sólo los pasajes que cambió el remate.

## Fuentes releídas (29-09-2026)

| Fuente | Fichero | Pasajes |
|---|---|---|
| EBU R 123 (Geneva, July 2009), anexo 2, 2.1, 2.2, 2.3.3, 2.3.4, y leyenda de siglas (IT = International Sound) | `fuentes/normas-tecnicas/EBU_R123.txt` l. 7-8, 803, 860-927 | `### El comentario y el sonido internacional` |
| INCUAL IMS077_3 (Orden PCI/797/2019): UC0216_3 RP5 CR5.1; MF0216_3 C8 CE8.2 | `fuentes/canal-sur/realizador/incual-IMS077_3.txt` l. 20, 103, 206-213, 506, 673-700 | `### La pértiga, el encuadre y la luz` |
| RD 1680/2011, 0905, RA 3 e) | `fuentes/canal-sur/realizador/BOE-A-2011-19599.txt` l. 651 | Fila Preparación |
| Tema 4 del puesto, fila del confidente | `04-organizacion-control-realizacion.md` l. 1086 | Fila Intercom |
| Tema 3 (señal internacional sin comentarios, l. 1061) y tema 14 (pistas EBU R 123) | temas del puesto | Remisiones |

## Resultado por pasaje

- Pértiga: los dos literales (CR5.1, CE8.2) coinciden con la fuente; CR5.1 está en UC0216_3 y CE8.2 en MF0216_3 (C8, ensayos). Oficio declarado. Sin cambios.
- Sonido internacional: definición SMPTE (2.2), 2.1 y 2.3.3 literales. Correcciones aplicadas tras releer:
  1. Salvedad omitida (error 6): el anexo 2 dice que *International Sound* y *Clean FX* se usan como equivalentes **pero** «(used to) mean quite different things». Añadida en negrita.
  2. *World Feed* (2.3.4): el tema atribuía al «segundo mezclador» el sonido; la fuente dice que la imagen la monta un segundo mezclador de vídeo y que un mezclador de sonido aparte pone el audio; y los *stems* se ponen «available… to the mixers». Reescrita la fila.
  3. *Clean FX*: «se usa sobre todo» → «se usa normalmente» (fuente: «typically used»).
  4. «y sonido lo mezcla encima» → «y el equipo de sonido lo mezcla encima» (antecedente).
  5. FX sin presentar (`refutar_prosa.py`): «*Clean FX* (efectos limpios; FX, *effects*)».
  - «IT» confirmado en la leyenda de la R 123.
- Filas Preparación e Intercom y la frase de «Lo que este tema no da» (cifras −23 LUFS, ±1 LU en l. 1035): conformes.
- Portada, siglas (INCUAL), «Qué se puede preguntar», índice y Trazabilidad: conformes; la fila de la R 123 ya cubre el anexo 2.

Antecedentes: «La misma recomendación», «Distingue», «su módulo formativo», «La jirafa», «ésa»: todos con antecedente delante.

## Lentes

`refutar_prosa.py`: 0 hallazgos tras la corrección 5. `indice.py`: 57 epígrafes, 12.644 palabras (la portada dice 12.600 aprox., vale).

## Ficheros tocados

El tema 11 y este informe. Ningún otro.
