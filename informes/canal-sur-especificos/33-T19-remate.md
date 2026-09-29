# Realizador/a (puesto 33) · Tema 19 · Fase 5, remate

Tema: `temas/canal-sur-especificos/33-realizador-a/19-prevencion-riesgos-laborales.md`.
Fecha de trabajo: 24-09-2026 (fecha del encargo); fuentes leídas el 29-09-2026 (fecha del sistema).
Entrada: `33-T19-refutacion.md` (0 hallazgos de exactitud; 3 lagunas) y `33-T19-preguntas.md`
(12 enteras, 1 a medias, 2 no). Las tres lagunas se cubren ampliando el tema; ninguna pregunta se recorta.

## Comprobación en la fuente antes de aplicar (29-09-2026)

| Laguna | Fuente | Resultado |
| --- | --- | --- |
| P13 · RD 773/1997, art. 9 | BOE-A-1997-12735, bloque a9 (1 redacción, 1997), `fuentes/canal-sur/` | Confirmada: remite al apartado 2 del art. 18 LPRL |
| P14 · ET, art. 36.1 | `boe.py precepto BOE-A-2015-11430 a36` (1 redacción, vigente desde 13-11-2015) | Confirmada: de las diez de la noche a las seis de la mañana |
| P15 · LGSS, art. 157 | `boe.py precepto BOE-A-2015-11724 a157` (1 redacción, vigente desde 02-01-2016) | Confirmada: definición literal de enfermedad profesional |

El informe de refutación no se equivocó en ninguna de las tres.

## Pasajes cambiados

1. **§2, «Otros riesgos del puesto: estrés y trabajo a turnos»**: la frase «Qué es trabajo nocturno
   (artículo 36.1…) … no se dan aquí» pasa a dar, en negrita literal, el primer inciso del 36.1
   («a los efectos de lo dispuesto en esta ley, se considera trabajo nocturno el realizado entre
   las diez de la noche y las seis de la mañana»); sólo el plus de nocturnidad queda remitido.
2. **§4, «El artículo 156 de la LGSS»**, tras la tabla del 156.2: párrafo nuevo con el art. 157
   literal (enfermedad profesional) y una frase de lectura del tema sobre la letra e).
3. **§5, «El Real Decreto 773/1997»**, entre los arts. 8 y 10: «Consulta y participación
   (artículo 9)», literal.
4. **Portada (Fuente)**: LGSS «artículos 156 y 157»; **Extensión**: 16.934 → 17.162 palabras.
5. **Normativa que el tema invoca**: RD 773/1997 «Arts. 2 a 10»; LGSS «Arts. 156 y 157»; ET
   «Art. 36.1, primer inciso, y 36.4».
6. **Lo que este tema no da**: se quita «qué es trabajo nocturno»; queda «el resto del artículo
   36.1 (jornada del trabajador nocturno)», el plus de nocturnidad y la ordenación de turnos.
7. **Trazabilidad**: frase con las tres lecturas del remate (29-09-2026); fila LGSS «arts. 156 y 157».

Antecedentes releídos: «del mismo Estatuto» sigue al 36.4 citado; «la letra e)» sigue a la tabla
del 156.2; «este Real Decreto» es literal dentro del epígrafe del RD 773/1997; el art. 18 LPRL
está en el §1.

## Lentes

- `indice.py`: 17.162 palabras, 38 epígrafes (el tema no está en `portadas.tsv`; extensión puesta a mano).
- `negritas.py` con RD 773/1997, ET y LGSS: las tres negritas nuevas, «ok» en su fuente.
- `refutar_exactitud.py`: sin avisos sobre los pasajes nuevos.
- `refutar_modo.py`: 4 avisos (arts. 15, 17, 19, 29) que cruzan artículos de la LPRL con el ET
  pasado como fuente; falsos positivos, fuera de los pasajes cambiados.
- `refutar_prosa.py`: 0 hallazgos.

Resultado: con el remate, las 15 preguntas quedan enteras. Se amplió contenido nuevo → pasa a 5 bis.

Ficheros tocados: el tema 19 y este informe.
