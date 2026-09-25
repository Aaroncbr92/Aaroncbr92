# Puesto 08 · Tema 5 · Fase 5 · Remate

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/05-iluminacion-basica.md`.
Base: `08-T05-refutacion.md` (3 menores, 3 lagunas) y `08-T05-preguntas.md` (12 enteras, 1 a medias, 2 no).
Copia previa en el scratchpad (`t05r/05-antes-remate.md`). **Amplía contenido nuevo: sí** (procede 5 bis).

## Fuentes leídas (todas el 24-09-2026)

- EBU Tech 3355, marzo de 2017 (copia local): escalas 1 y 2 del Qa; «Illuminant D65» (cuerpo del texto).
- UIT-R BT.709-6 y BT.2020-2 (copias locales): sólo «D65» / «Reference white (D65)», sin atribución a la CIE.
- Sekonic, ficha del SpectroMaster C-800 (PDF de bbplight.nl, pasado a `.txt`).
- Adobe, *High key lighting vs low key lighting in videography* (adobe.com). curl bloqueado; tres frases
  comprobadas letra a letra con dos lecturas (WebFetch). La página de Canon.es devolvió 403 y no se usó.
- Sony, *PXW-Z100 Operating Guide*, 4-484-009-11(1), © 2013 (copia local): tabla de preajustes de balance.

## Correcciones de exactitud

| Nº | ¿Se aplicó? | Comprobación | Pasaje cambiado |
|---|---|---|---|
| M1 | Sí | EBU, escala 1: «Film-style production, where possibly different cameras, locations and lighting need to be intercut or mixed…pictures are required to match each other well». Confirmado | «La fidelidad de color: IRC y TLCI», segundo punto: ahora nombra las dos escalas como la EBU, completa la cita con «and pictures are required to match each other well» y explica el contraste casar / ser creíble |
| M2 | Sí | Ni BT.709/BT.2020 ni EBU atribuyen D65 a la CIE en lo citado; EBU dice «Illuminant D65» | «La luz de día y el blanco D65»: «el iluminante D65 (la EBU lo llama «**Illuminant D65**»)». La sigla CIE ya no se usaba en ningún otro sitio: quitada de las siglas |
| M3 | Sí | *ATW* no aparece en el tema | Nota de rótulos de menú: se quita ***ATW*** |

## Lagunas: se amplía el tema

| Nº | Epígrafe nuevo o ampliado | Qué se añade | Fuente |
|---|---|---|---|
| L2 (p. 14) | Nuevo `### Medir el color de una fuente` (tras «Los filtros de conversión») | El medidor de color (termocolorímetro en el oficio) frente al fotómetro; lo que mide y da el C-800, con cita; uso en rodaje | Sekonic (literal); el uso, oficio |
| L1 (p. 13) | Nuevo `### Clave alta y clave baja` (tras «Bajar o subir el contraste») | Tabla con la definición de las dos claves, cómo se consiguen, razón de contraste y tono; relación con la razón de contraste | Adobe (literal); razones, oficio |
| L3 (p. 15) | «La luz natural cambia», ampliado | Tabla de la altura del sol (amanecer/atardecer, media mañana, mediodía): dirección, dureza, color y longitud de la sombra (5,7 h a 10°; 1,7 h-h a 30-45°; ≤0,6 h a 60°); preajuste de exterior de Sony para amanecer y atardecer | Longitudes, cálculo (h/tan); Sony Z100 (literal); lo demás, oficio |
| Reserva | «La dominante verde y la mezcla de fuentes», párrafo nuevo | Alumbrado de sodio y mercurio: parpadeo y preajuste de interior que propone Sony; qué se hace en un directo nocturno | Sony Z100 (literal); lo demás, oficio |

No se ha podido confirmar con una fuente leída el color y el espectro de las lámparas de sodio (sólo
fuentes secundarias): no se afirma y va a «Lo que este tema no da», junto con la altura del sol en
Andalucía según la fecha.

## Otros pasajes cambiados

- Portada: «Fuente» añade Sony Z100, Sekonic y Adobe; «Extensión» pasa a 8.600 palabras.
- «Qué se puede preguntar»: medir la temperatura de color, clave alta y baja, altura del sol.
- «Lo que este tema no da»: dos entradas nuevas (sodio y mercurio; altura del sol).
- «Trazabilidad»: tres filas nuevas; la lista de oficio y la de cálculo, ampliadas.
- Relectura de antecedentes: «epígrafe anterior» en el pasaje de la clave apuntaba mal; se cambió a
  «la razón de contraste» y «tabla del epígrafe anterior» («Bajar o subir el contraste», justo antes).

## Lentes

`indice.py`: 8.578 palabras, 38 epígrafes, índice regenerado con los dos epígrafes nuevos.
`refutar_prosa.py`: 3 avisos de siglas (PUB, PXW, URSA: códigos de producto, sin hallazgo, los mismos
que en la refutación). Sin normas jurídicas: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

Sólo el tema 5 y este informe. Los PDF y páginas se guardaron en el scratchpad. Los cambios en
otros temas del puesto que aparecen en `git status` no son míos.
