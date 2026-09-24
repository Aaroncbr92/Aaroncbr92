# T10 · Refutación (fase 4, modo ahorro) · Protección de datos de carácter personal

Tema: `temas/canal-sur-comun/10-proteccion-de-datos.md` (tal como lo dejó la verificación). Leídos
`ENCARGO.md`, `CICLO.md` y `T10-verificacion.md`. Un agente, una lectura del tema y dos lentes.
**No se ha tocado el tema.** Fecha de lectura de todos los preceptos: **24-09-2026**, en los
volcados de `fuentes/canal-sur/` (sacando solo el precepto con `grep`/`sed`).

Formato de cada hallazgo: dónde · qué dice · qué debería decir · fuente literal · gravedad.

## 1. Exactitud contra la fuente

**H1. Régimen sancionador, regla nemotécnica tras la tabla del artículo 83 (líneas 1336-1338).**
- Dice: «el 4 % es para lo que afecta al ciudadano (principios, consentimiento, derechos,
  transferencias); el 2 % para lo que afecta a la organización interna (seguridad, registro,
  delegado, evaluación de impacto)».
- Debería decir: advertir que el consentimiento del niño (art. 8) va al escalón del 2 % (83.4),
  aunque sea «consentimiento»; o quitar «consentimiento» de la regla y decir «condiciones del
  consentimiento del artículo 7».
- Fuente: art. 83.4.a) RGPD: «las obligaciones del responsable y del encargado a tenor de los
  artículos 8, 11, 25 a 39, 42 y 43». La tabla del tema lo dice bien; la regla lo contradice.
- Gravedad: **induce a error** (pregunta 9).

**H2. Art. 72.1.d) LOPDGDD, lista de muy graves (líneas 1277-1278).**
- Dice: «usar los datos para una finalidad incompatible con aquella para la que se recogieron».
- Debería decir: añadir «sin contar con el consentimiento del afectado o con una base legal para
  ello».
- Fuente: art. 72.1.d): «La utilización de los datos para una finalidad que no sea compatible con
  la finalidad para la cual fueron recogidos, sin contar con el consentimiento del afectado o con
  una base legal para ello.»
- Gravedad: menor (error 6, salvedad omitida).

**H3. Evaluación de impacto, art. 35.3.a) RGPD (líneas 873-874).**
- Dice: «sobre cuya base se tomen decisiones con efectos jurídicos».
- Debería decir: «… decisiones que produzcan efectos jurídicos para las personas físicas o que les
  afecten significativamente de modo similar».
- Fuente: art. 35.3.a) RGPD, literal arriba.
- Gravedad: menor (error 6).

**H4. Tabla «Qué le toca a una producción», fila «Escribir a un compañero fuera de su jornada»
(línea 2016).**
- Dice: «Choca con el derecho a la desconexión digital (art. 88), cuyas modalidades fija la
  negociación colectiva».
- Debería decir: el art. 88 es un derecho de trabajadores y empleados públicos cuyo respeto
  garantiza el empleador mediante su política interna (88.3); no dice que un mensaje entre
  compañeros lo vulnere. Mejor: «Mensajes de la empresa fuera de la jornada | Derecho a la
  desconexión digital (art. 88): modalidades según la negociación colectiva o, en su defecto, lo
  acordado entre la empresa y los representantes; política interna del empleador».
- Fuente: art. 88.2: «… se sujetarán a lo establecido en la negociación colectiva o, en su
  defecto, a lo acordado entre la empresa y los representantes de los trabajadores»; 88.3: «El
  empleador, previa audiencia de los representantes de los trabajadores, elaborará una política
  interna…».
- Gravedad: induce a error (afirmación sin apoyo y salvedad omitida; errores 9 y 6).

**H5. La AEPD, artículo 44 (línea 1004).**
- Dice: «Relación no es dependencia: es el cauce ordinario de toda autoridad independiente.»
- Debería decir: quitarlo. El artículo 44 no lo dice, y el tema no cita la Ley 40/2015 para
  afirmarlo. La independencia ya está dicha con la letra del 44.1 («plena independencia de los
  poderes públicos»).
- Gravedad: menor (error 9).

## 2. Cobertura (quince preguntas en `T10-preguntas.md`)

Contestadas solo con el cuerpo del tema: 13 enteras (la 9, con la trampa de H1), 0 a medias y
2 sin respuesta (la 10 y la 11).

**H6. Faltan las condiciones del consentimiento (art. 7 RGPD) y los recursos, la responsabilidad
y la indemnización (capítulo VIII RGPD: arts. 77, 79 y 82).**
- Dónde: «Cuándo es lícito tratar datos» (consentimiento) y «Los derechos de las personas» o «El
  régimen sancionador». Hoy el tema solo nombra el capítulo VIII como uno de los que no admiten
  excepciones periodísticas.
- Qué debería añadir (ampliación, no corrección):
  - Art. 7.1: «el responsable deberá ser capaz de demostrar que aquel consintió el tratamiento de
    sus datos personales»; 7.3: «El interesado tendrá derecho a retirar su consentimiento en
    cualquier momento. La retirada del consentimiento no afectará a la licitud del tratamiento
    basada en el consentimiento previo a su retirada. […] Será tan fácil retirar el consentimiento
    como darlo.»
  - Art. 77.1: derecho a reclamar ante una autoridad de control, «en particular en el Estado
    miembro en el que tenga su residencia habitual, lugar de trabajo o lugar de la supuesta
    infracción»; art. 79 (tutela judicial frente al responsable o encargado); art. 82.1: «Toda
    persona que haya sufrido daños y perjuicios materiales o inmateriales como consecuencia de una
    infracción del presente Reglamento tendrá derecho a recibir del responsable o el encargado del
    tratamiento una indemnización».
- Gravedad: **cambia la respuesta** (preguntas 10 y 11; son preceptos clásicos de test y el
  83.5 del propio tema ya remite al artículo 7).

## 3. Prosa y forma

**H7. Normativa que el tema invoca, fila de la Ley 1/2014 (línea 2038).**
- Dice: «Artículos 3, 43, 44, 45 y 48». El cuerpo solo cita los artículos 43, 45 y 48.
- Debería decir: «Artículos 43, 45 y 48», o citar en el cuerpo lo que se tomó de los artículos 3
  y 44.
- Gravedad: menor.

**H8. Dos pasajes oscuros.**
- Línea 283 (y Trazabilidad, línea 2084): «y ninguna reforma cruzada». Es jerga de trabajo que el
  lector no entiende. Quitarlo o decir qué significa.
- Líneas 1386-1390 (art. 77.3): el paréntesis «(el apartado 3 no se modificó y conserva la
  expresión "en la resolución en la que se imponga la sanción")» parte la cita en dos. Mejor: citar
  el 77.3 seguido y añadir después, en una frase, que conserva la palabra «sanción» aunque el 77.2
  ya no sancione.
- Gravedad: menor.

## 4. Lentes

| Lente | Tramos | Resultado |
|---|---|---|
| `negritas.py` (22 volcados, sus 2 correcciones y el `.txt` del Acuerdo de fusión) | 212 negritas | 12 NO ESTÁ y 19 ¿ART.? Son los mismos que explicó la verificación: 2 rótulos; 8 citas de considerandos (1, 4, 32, 65 y 153) y 2 del Reglamento 2025/2518, que no están en los volcados y que la verificación leyó en la página del BOE y en el texto de la Oficina de Publicaciones (este agente no los ha vuelto a leer). Los 19 ¿ART.? son anclajes en otro número nombrado en la frase. Falsos positivos |
| `refutar_prosa.py` | tema entero | 1: «LORTAD», que se presenta en la misma cita. Falso positivo |
| `refutar_modo.py` (RGPD, LOPDGDD, Leyes 13/2022, 10/2018 y 2/2023, LO 1/1982 y 7/2021) | tema entero | 2 (arts. 8 y 16 de otras normas con la misma numeración). Falsos positivos |

Comprobado sin hallazgo además de lo que ya cotejó la verificación: el recuento de 17 bloques
(12 posteriores a 2022) contra el índice de redacciones; los arts. 4, 5, 8, 11, 12, 13, 15 y 16,
72 a 74 (letras citadas: 72.1.k, 73.k y 73.p) y DF 2.ª y DT 1.ª LOPDGDD; el art. 83.4 RGPD; los
capítulos del título VI de la Ley 13/2022; el art. 22.2 LSSI y su redacción; y que «libertad de
expresión» solo aparece en el art. 85 del articulado de la LOPDGDD.

## 5. Resumen y ficheros

Ocho hallazgos: uno **cambia la respuesta** (H6, ampliación: arts. 7, 77, 79 y 82 RGPD), dos
**inducen a error** (H1, H4) y cinco menores (H2, H3, H5, H7, H8). Ficheros escritos: este informe
y `informes/canal-sur-comun/T10-preguntas.md`. El tema no se ha tocado.
