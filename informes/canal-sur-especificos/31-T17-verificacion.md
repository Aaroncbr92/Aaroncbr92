# Puesto 31 · Tema 17 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/31-presentador-productor-de-radio/17-etica-profesional-responsabilidad.md`.
Verificado el 3-X-2026; redacción que se estudia, la vigente el 24-IX-2026. Fuentes releídas el 3-X-2026.

## Lo copiado (sólo literalidad)

`diff` contra `temas/canal-sur-especificos/34-redactor-a/18-etica-profesional-responsabilidad.md`:
todo lo que no aparece en el diff es idéntico a 34-T18. Las únicas diferencias son las que el informe
de redacción declara en «Lo cambiado o añadido». No había nada «Copiado de RTVE sin cambios».
Ningún «redactor» suelto en pasajes que debieran hablar del puesto (los tres que quedan son del
texto de 2006 y se refieren de verdad a redactores).

## Lo verificado, dato a dato

| Pasaje | Fuente | Resultado |
|---|---|---|
| Ficha: puesto 2.31, punto 17, grupo B03; enunciado literal | `convocatoria/canal-sur/especificos/31-…md` | Correcto |
| §2, Estatuto 2006: 2.1, 11.2, 12.6, 3.2.5 | `estatuto-profesional-blog.txt` l. 24, 97, 113, 36 | Literal; paráfrasis correctas |
| §3, ficha 9540002 (función básica y tres tareas), anexo III «Definición de funciones», p. 191 BOJA 240/2014 | `x-convenio-rtva-boja-240-2014.txt` l. 162, 6843-6861 | Literal; la deducción va marcada como tal |
| §6, Libro de estilo 8.6 y 8.6.1.7; capítulo «Presencia en cámara» | `libro-de-estilo-333233b.txt` l. 4328-4372 | Literal |
| §9, Libro de estilo 9.10 | ídem, l. 6283-6285 | Literal |
| §9, LGCA art. 85.2 | `BOE-A-2022-11311.md` l. 1152-1158; 1 redacción desde 9-VII-2022 | Literal, **pero salvedad omitida (error 6)**: ver corrección 1 |
| §10, norma del Defensor 6.1 («soporte sonoro») | `norma-reguladora-defensor-audiencia-rtva.txt` l. 115 | Literal |
| Remisiones: LO 2/1997 → tema 6 del común; LO 2/1984 → tema 9 (epígrafe 5) | `temas/canal-sur-comun/06-*.md` (l. 1012-1100); T9 del puesto, `## 5. Rectificación` | Correctas |
| Remisión del patrocinio y las comunicaciones comerciales en radio → «tema 4 del común» | `temas/canal-sur-comun/04-*.md` no trata patrocinio ni art. 85 | **Error 1**: ver corrección 2 |

## Correcciones aplicadas

1. §9 (error 6). El tema decía que el art. 85.2 LGCA «pone además un límite propio» al patrocinio en
   radio. Es al revés: el 85.2 modula el 128.2, que con carácter general excluye «los noticiarios y
   los programas de contenido informativo de actualidad»; la radio sólo excluye los noticiarios.
   Se añade el 128.2 literal (`BOE-A-2022-11311.md` l. 1713, una redacción) y se reescribe la frase.
   Se añade art. 128.2 en la ficha, en «Normativa» y en Trazabilidad.
2. «Lo que este tema no da» (error 1). «lo demás, en el tema 4 del común» era falso. Ahora: el 85.3
   (emplazamiento) está en el tema 11 del puesto (comprobado, l. 369-374) y el régimen completo de las
   comunicaciones comerciales no lo desarrolla este temario.
3. Extensión de la ficha: 8.898 → 8.964 palabras (`indice.py`).

## Lentes

- `negritas.py` (Estatuto 2006, X Convenio, Libro de estilo, LGCA, norma del Defensor, Ley 18/2007,
  LO 2/1997, Carta del Servicio Público): todas las negritas nuevas se encuentran, salvo la de 8.6.1.7,
  que falla sólo por la ligadura «ﬁ» del volcado (cotejada a ojo: literal). Las no encontradas restantes
  son de pasajes copiados (Carta de la FIP sin volcado, cortes de línea); el aviso «previa audiencia
  del interesado → LGCA art. 163» es un falso positivo: el tema cita el 3.3 de la norma del Defensor.
- `refutar_exactitud.py` y `refutar_modo.py` con la LGCA: 0 hallazgos reales (los «no literales»
  son citas de la norma del Defensor que el script atribuye a la LGCA).
- `refutar_prosa.py`: 0 hallazgos.

## Lo que no se pudo confirmar

Nada nuevo; se mantiene lo declarado en la redacción (ámbito del Estatuto vigente, falta de normas
propias de la radio publicadas).

## Ficheros tocados

Sólo el tema 17 y este informe.
