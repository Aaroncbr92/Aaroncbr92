# Puesto 08 · Tema 6 · Fase 4 · Refutación

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/06-captacion-de-sonido.md`
(9.535 palabras, 43 epígrafes según `indice.py`). Refuto, no corrijo. Leídos sólo `ENCARGO.md`, el
enunciado del puesto 08 y los informes de redacción y verificación de T06.

## Fuentes releídas (todas el 24-09-2026)

- *Libro de estilo de Canal Sur*, 2004 (copia `.txt`): 3.2.2 (p. 46), 3.17.1 y 3.17.1.3 (pp. 59-60),
  5.3.3 (p. 81), p. 82 y 5.4 enteros, 6.4 (p. 92), 8.3.2 (p. 117), 8.6.1 (p. 122). Literales conformes.
- EBU R 68-2000 (entera): opinión de 16 bits, 9/8 dB, 3/6/15 dB, 18 dB, notas 1 y 2. Conforme.
- EBU R 128-2023: historial (V3 de junio de 2014, ±0,5 LU), a), b), c), h), i), k), m), n), notas.
  Conforme.
- EBU Tech 3341-2023 (V4, nov. 2023): M, S, I y § 2.4. Conforme.
- EBU Tech 3343-2023: § 3.1 (welcome bonus), § 3.5.1 (−24 LUFS), § 8.1 entero, p. 43 (1 dB,
  0,5 dB, −2 dBTP). Conforme.
- Sony PXW-Z200 Help Guide 5-060-574-13(1): pp. 16, 99, 136, 139, 260-261, 298, 336-338. Conforme.

Copiado del común: ninguno (informe de redacción); nada que saltar.

Lentes: `refutar_prosa.py`, 1 aviso (PXW, código de producto: sin hallazgo); `indice.py` no cambia
el fichero. Sin normas jurídicas: no proceden las lentes de norma.

## Hallazgos de exactitud

Graves: ninguno. Menores: 4.

| Nº | Error | Línea / pasaje | Qué pasa | Propuesta |
|---|---|---|---|---|
| M1 | 9 (matiz) | l. 454-455, «los picos reales suelen quedar hasta 3 dB por encima» | La R 68 dice **«can be 3 dB greater»**: posibilidad, no frecuencia | «pueden quedar hasta 3 dB por encima» |
| M2 | 6 salvedad omitida | l. 791-793, cita de las barras (p. 82) | Se corta antes de **«Si hay dos noticias en el mismo soporte deben separarse con un minuto de barras.»**, que es la otra mitad de la regla (pregunta 11) | Completar la cita |
| M3 | 6 salvedad omitida | l. 542 y l. 787, ***[1kHz Tone on Color Bars]*** | La nota del manual (p. 261): **«When set to [On], the 1 kHz reference tone signal is output on CH3/CH4, even if [CH3 Input Select]/[CH4 Input Select] are set to [Off].»** Afecta al reparto de canales 3 y 4 (pregunta 12) | Añadir la nota en la tabla de mandos |
| M4 | 9 sin fuente | l. 593, «Es como se ha trabajado en cine desde que existe el sonoro» | Afirmación histórica sin fuente leída; no aporta a la pregunta | Quitarla o declararla oficio |

Comprobado sin hallazgo: todos los literales del Libro de estilo (incluidas las erratas del
original: «lo permitan», «puede ser recomendable es el TC»), de la R 68, R 128, Tech 3341, Tech 3343
y de la Z200 (conmutador, avisos, menú de audio con valores de fábrica, TC, especificaciones);
cálculos (6,02 dB/bit, 96/144 dB, 9 + 6 = 15 dB); ±0,5 LU de 2014 sólo en el historial.

## Cobertura del enunciado

Los cinco elementos (microfonía, niveles, sincronía, ambiente, criterios básicos) tienen `##` propio
en el orden del enunciado. Preguntas en `08-T06-preguntas.md`: 11 enteras, 1 a medias, 3 no (dos de
ellas por M2 y M3).

Lagunas (2), a ampliar en el remate con fuente (si no se encuentra, declarar como oficio o en «Lo
que este tema no da»):

| Nº | Rúbrica | Qué falta | Pregunta |
|---|---|---|---|
| L1 | Microfonía | Efecto de proximidad de los direccionales (realce de graves al acercarlos) | 13 |
| L2 | Microfonía / cadena | Línea balanceada (simétrica) del XLR y por qué rechaza el ruido en cables largos | 14 |

De reserva, sin contar como laguna: la ley del inverso del cuadrado en sonido (unos 6 dB por
duplicar la distancia), que daría la cifra a «la distancia manda más que el patrón» (pregunta 15).

## Otros ficheros tocados

Sólo este informe y `08-T06-preguntas.md`. El tema no se ha modificado.
