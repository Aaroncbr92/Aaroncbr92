# Productor/a (puesto 32) · Tema 5 · Remate

Fase 5. Tema:
`temas/canal-sur-especificos/32-productor-a/05-gestion-de-recursos-humanos-y-condiciones-de-prestacion.md`.
Entrada: `32-T05-refutacion.md` (0 graves, 2 menores, 3 lagunas) y `32-T05-preguntas.md` (7 a medias;
8 y 9, no). Fecha del encargo 24-09-2026; fuentes releídas el 25-09-2026 en su redacción vigente a
24-09-2026.

**Resultado: se amplió contenido nuevo** (RD 1561/1995, ET 36.2, 36.3 párrafo tercero y 35.2
segunda frase). Procede la fase 5 bis sobre los pasajes listados abajo. Extensión: 11.717 → 12.369
palabras (portada, 11.600 → 12.300).

## Comprobación en la fuente antes de aplicar

| Hallazgo | Fuente releída | ¿El informe acierta? |
| --- | --- | --- |
| Menor 1, plus de pernocta sin condición | X Convenio, art. 53.4 (`.txt`, l. 1830-1838): «sólo y exclusivamente [...] prolongue su jornada de trabajo más de dos horas» | Sí; aplicado |
| Menor 2, «sin horas extraordinarias» a todo nocturno | ET 36.1 (`boe.py --fecha 20260924`, redacción única) | Sí; aplicado |
| Laguna 1, RD 1561/1995 art. 19 | `BOE-A-1995-21346`, arts. 1, 2 y 19, redacción única; título comprobado en boe.es | Sí; aplicado. Añado el art. 2.1-2.2 (compensación, no sustituible por dinero), que condiciona el 19 |
| Laguna 2, ET 36.3 párr. 3.º y 36.2 | ET 36, redacción única | Sí; aplicado |
| Laguna 3, ET 35.2 reducción proporcional | ET 35, redacción única | Sí; aplicado |

Ninguna corrección del informe resultó errónea.

## Pasajes cambiados

1. **Portada, «Fuente»**: se añade «Real Decreto 1561/1995, sobre jornadas especiales de trabajo
   (`BOE-A-1995-21346`), artículos 2 y 19». **Extensión**: 12.300.
2. **Turnos › Lo que añade el ET, entrada**: «…regula el trabajo nocturno y a turnos; el reglamento de
   jornadas especiales matiza, en el trabajo a turnos, el descanso entre jornadas del 34.3 y el semanal
   del 37.1:».
3. **Ídem, art. 36, nuevo guion «Apartado 2»**: literal del 36.2 y enlace al complemento de
   nocturnidad del art. 50 («Complementos ligados al turno», epígrafe del mismo tema).
4. **Ídem, art. 36, guion «Apartado 3»**: se añade literal el párrafo tercero (turnos por semanas
   completas o contratando personal para completar equipos).
5. **Ídem, nuevo bloque tras el apartado 4**: RD 1561/1995, art. 19.1 y 19.2 literales; art. 2.1
   (literal parcial) y 2.2 (en redonda, con la salvedad del supuesto sectorial del art. 18); aplicación: la regla estatal no es absoluta en el cambio de
   turno, pero el convenio fija las doce horas (12.b.2) y los dos días (12.b.3) sin prever reducciones y
   no hay fuente publicada de la RTVA; el tema no decide.
6. **Jornadas › Horas extraordinarias, guion «Apartado 2»**: se añade literal la reducción
   proporcional del tope y su aplicación a la DT 1.ª A.b (marcada «aplicación del tema»).
7. **Desplazamientos, tabla «Salida…»**: «si se pernocta fuera de Andalucía y la jornada se prolonga más
   de dos horas, plus de pernocta».
8. **Normativa laboral interna › Convenio y ET, tabla**: fila «Descanso entre jornadas», columna ET, con
   la salvedad del RD 1561/1995 (19.2); fila «Nocturno», columna ET limitada a «trabajadores nocturnos»
   con su definición, y columna del productor ajustada.
9. **Comprobaciones, punto 6**: condición del plus de pernocta.
10. **Normativa que el tema invoca**: nueva fila RD 1561/1995 (arts. 2 y 19).
11. **Trazabilidad**: nueva fila RD 1561/1995 (arts. 1, 2 y 19, leído el 25/09/2026).

Relectura de antecedentes: «esas reducciones» (pasaje 5) tiene delante el art. 19; «Su artículo 2.1»
remite al Real Decreto nombrado en el párrafo anterior; «el mismo apartado» (pasaje 6) es el 35.2 del
guion; «esa retribución» (pasaje 3), la del 36.2 citado. Correctos.

## Lentes

- `indice.py`: índice sin cambios (50 epígrafes; no se crearon rúbricas).
- `negritas.py --todas` con ET, RD 1561/1995 y convenio: todas las negritas nuevas, «ok» en su fuente.
  Los «NO ESTÁ» restantes son de fuentes no pasadas (Cámara, Libro de Estilo, contrato-programa) y
  preexistentes; los tres «¿ART.?» del art. 36 son falsos positivos (el cotejo los sitúa en el art. 36).
- `refutar_exactitud.py` (ET, RD): 5 negritas y 14 citas «no literales», todas del convenio (no
  pasado como fuente a esta lente) y preexistentes; ninguna de los pasajes cambiados.
- `refutar_modo.py` (ET, RD): 2 avisos. Art. 35: salta en la tabla de contraste copiada del tema 7 del
  común («ochenta al año» sin la salvedad); la salvedad ya está en el guion del apartado 2 inmediatamente
  anterior, y el texto copiado del común no se toca. Art. 37: preexistente, fuera de los apartados que
  el tema estudia.
- `refutar_prosa.py`: 3 siglas (CSR, ESTRUC, RAI) preexistentes; ninguna de los pasajes cambiados.

## Ficheros tocados

- El tema 5 del puesto 32.
- `fuentes/canal-sur/BOE-A-1995-21346.md` y su `.redacciones.tsv` (volcado nuevo con `boe.py norma`,
  para las lentes).
- Este informe.

`indice.py` sin argumentos se corrió una vez por error de uso; sólo recorre los temas de
`portadas.tsv`, que no incluye los del puesto 32, y es idempotente. Las modificaciones en otros temas
del puesto 32 que muestra `git status` no son de este remate.
