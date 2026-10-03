# 31-T05 · Verificación · Informativos y magazines radiofónicos

Fase 3. Verificado el 03-10-2026 (fecha de referencia del encargo: 24-IX-2026).
Tema: `temas/canal-sur-especificos/31-presentador-productor-de-radio/05-informativos-y-magazines-radiofonicos.md`
(8.515 palabras, 39 epígrafes, tras la verificación).

## Lo copiado: sólo comprobado que es literal

- **Copiado del común** (34-T08, 34-T05, común 06): un script normaliza espacios y negritas, parte
  cada pasaje en frases y busca cada una en los temas de origen. Todas están, salvo las frases de
  entrada y los rótulos que el informe de redacción declara nuevos. No se re-verifican.
- **Copiado de RTVE sin cambios** (`realizacion-tv/07` §9): la frase de definición, la tabla de cinco
  filas (en el original 297-301, sin las negritas) y el fragmento final son literales.

## Verificado en fuente (todo lo demás)

| Fuente (leída el 03-10-2026) | Qué se cotejó | Resultado |
|---|---|---|
| Contrato-programa 2024-2026 (BOJA 245, 26-12-2023) | rótulo 3.1; ap. 3, 4, 5, 6, 7 [sic «ordinario»], 9, 10, 14, 15, 19, 23, 30, 98 (a-d), 99, 106, 109 | Literal y bien numerado. Tres precisiones (abajo) |
| Carta 2024-2029 (BOJA 247) | 13.3 (fragmento); «Tanto en los medios de radio como de televisión» (13.8) | Literal |
| Manual de RTVE, cap. 3 | numeración 3.2-3.2.2, 3.3.1, 3.4.4, 3.5, 3.6; que no fija duración del boletín; que no define el magazine (ningún volcado del Manual lo menciona) | Correcto |
| López Vigil | cap. 7 (8936-9086): todo lo dicho del medio, el flash, el avance, el boletín, la nota 66, los tres modelos, los bloquecitos, la estructura circular, los 20 minutos, los titulares y las tres emisiones; cap. 9 (10757-11310): la definición, los tamaños, la periodicidad, el directo, la conducción, el machismo radiofónico, las cuatro vías, las llamadas y el servicio. ISBN («SBN» en el volcado), copyleft y «Lima, abril 2005» | Literal; una salvedad añadida (abajo) |
| canalsur.es (volcado del 03-10-2026) | menú: Radio, Canal Fiesta, Flamenco Radio | Correcto |

Las 197 negritas pasaron por `negritas.py` con las seis fuentes (Contrato-programa, Carta, López Vigil,
Manual de RTVE, Ley 18/2007 BOE-A-2008-1185, Estatuto profesional). Quedan 20 que no están en ninguna
fuente. Son rótulos y etiquetas en negrita, más la frase del Libro de estilo, que está literal en
`libro-de-estilo-333233b.txt:159`. `refutar_exactitud.py`: las 7 citas «no literales» son falsos
positivos, porque cita artículos de la Carta, del Contrato-programa y del Manual de RTVE, que
contrasta con la Ley 18/2007. `refutar_modo.py` da 0, `refutar_prosa.py` da 0 e `indice.py` ha
quedado bien.

## Correcciones aplicadas

1. **Error 9 (ficha)**: «porque Canal Sur no tiene publicado libro de estilo de radio» → «porque no se
   ha localizado publicado un libro de estilo de radio de Canal Sur», como en «Lo que este tema no
   da» (y como se corrigió en T03).
2. **Error 9 (ap. 99)**: «en todo programa no informativo» y «los programas no informativos» → «en todo
   programa divulgativo, cultural o de entretenimiento», que es lo que dice el apartado.
3. **Error 9 (ap. 99, §5)**: no dice que el Contrato-programa «prevé expresamente» el programa de exteriores.
   Prevé **programas cara al público y con participación de la audiencia**. Reescrito.
4. **Error 6 (ap. 98.c)**: faltaba «fundamentalmente» («El 75% estará basado fundamentalmente en la
   divulgación…»). Añadido.
5. **Error 6 (López Vigil, §1)**: «la estructura del noticiero largo es circular». El manual dice que
   lo son todos, **«especialmente los de larga duración»**, y da dos razones: la oferta (no hay flujo
   que aguante más de media hora) y la demanda. Corregido y añadida la primera razón.

## Nota, sin cambio

El pasaje «La información aparecerá ante el público diferenciada de la opinión» (3.2.3) llama al
documento «Estatuto Profesional». Está copiado del común y es literal en `estatuto-profesional-cgt.txt`.
El tema 17 de este puesto dice que el Estatuto vigente no está publicado. Que lo mire la refutación,
si procede: no lo he tocado, porque es pasaje copiado.

## Ficheros tocados

- Modificado: el tema 05 (las cinco correcciones).
- Creado: este informe.
