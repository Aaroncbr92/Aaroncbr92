# Realizador/a (puesto 33) · Tema 8 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/33-realizador-a/08-camaras-opticas-soportes-encuadres.md`
Fecha de trabajo: 24-09-2026 (encargo); fuentes leídas el 29-09-2026 (fecha del sistema).
Resultado: 17.723 palabras, 86 epígrafes (`indice.py`); `refutar_prosa.py`: 0 hallazgos.

## 1. Lo copiado: sólo cotejo de literalidad

Script de cotejo por párrafo (y por fila de tabla), con espacios normalizados, contra los seis temas
cerrados de origen (común) y contra los dos de RTVE sin negritas ni ✔:

- 322 párrafos o filas literales del común (08/01, 08/02, 08/04, 08/09, 08/15, 32/09). No se
  re-verifican.
- 51 literales de RTVE. Otros ocho párrafos que el redactor declaró «sin cambios» difieren sólo en lo
  que su informe dice que quitó (incisos de examen, «epígrafe 7», mayúscula inicial): 490, 549, 554,
  558, 650, 1110, 1224 y la tabla de 1062. Comprobado con diff por palabras. No se re-verifican.
- Adaptados de RTVE (1084 «zum portátil / de caja»; 1273 remisión): verificados, ver hallazgo 4.
- 95 párrafos o filas son texto nuevo o adaptado: verificados todos (apartado 2).

## 2. Lo verificado

Cada negrita del texto nuevo buscada en su fuente (script propio de cotejo normalizado, y
`negritas.py` con las tres fuentes: los «no está» que da son todos de pasajes copiados en inglés o
del Libro de Estilo con ligadura «ﬂ», en texto del común). Todas las negritas nuevas son literales.
Además, ubicación de cada cita:

| Fuente | Qué se comprobó | Leída |
|---|---|---|
| RD 1680/2011, `fuentes/canal-sur/realizador/BOE-A-2011-19599.txt` (BOE núm. 302, de 16-12-2011) | 0903 RA 1.b y contenidos; 0904 RA 4.c; 0905 RA 3.c, 3.d, 5.b; 0910 RA 2, 2.a, 2.c, 2.d, 2.h, contenidos (steadycam, travelling, robotizadas) y orientaciones pedagógicas. Módulo, RA y letra correctos en todas | 29-09-2026 |
| RD 500/2024, `BOE-A-2024-10685.txt`, art. séptimo | Suprime FOL, EIE y FCT, añade módulos, renombra «Proyecto»; no toca 0903-0910 | 29-09-2026 |
| RD 1085/2020, BOE-A-2020-17274 (`boe.py precepto … dd`) | Disp. derogatoria única, ap. 2: deroga el anexo de convalidaciones del RD 1680/2011 | 29-09-2026 |
| X Convenio, `x-convenio-rtva-boja-240-2014.txt` | Anexo III; ficha 5341310 en BOJA p. 116 y 5351000 en p. 196; cuatro tareas citadas, literales | 29-09-2026 |
| Libro de Estilo, `libro-de-estilo-333233b.txt` y PDF (página del PDF = página impresa) | 3.17.1 p. 59; 3.17.1.1 p. 59; 3.17.1.2 p. 59; 3.17.1.5 p. 61; 5.1 p. 79; 5.2 p. 80; 5.3.1 p. 80; 5.3.2 p. 81; 6.4 p. 92; 8.6 p. 121; 8.6.1 p. 122; 9.2.12.4 p. 130; «recomendaciones … métodos de trabajo» (presentación) | 29-09-2026 |
| Temas 33/01 (epígrafes «El eje en multicámara», «El encuadre en la entrevista y en el directo») | Existen las remisiones | 29-09-2026 |

Cálculo comprobado: de f/1,4 a f/22, ocho pasos; 2^8 = 256.

## 3. Hallazgos y correcciones (aplicadas)

1. **Error 8.** «un sola cámara … que determine el realizador» citado como 3.17.1: está en 3.17.1.5
   (p. 61). Corregido en el epígrafe y en «Trazabilidad» (que además daba 3.17.1 en p. 61).
2. **Error 8.** Aplicación práctica, «Segundo recorrido» (3.17.1) → 3.17.1.5.
3. **Error 9.** Aplicación práctica, «La óptica a la altura de la mirada del entrevistado (5.2)»: el
   LE 5.2 dice **«a la altura de la teórica mirada del espectador»**. Corregido; lo de los ojos de
   quien se graba queda como práctica (ya lo decía el pasaje copiado del común).
4. **Error 1.** «las tres cosas del epígrafe «La profundidad de campo»»: los tres factores de ese
   epígrafe (apertura, focal, distancia de enfoque) no son las tres acciones de la lista (la tercera es
   la separación sujeto-pantalla). Reescrita la entradilla: «tres cosas … (los factores de la
   profundidad de campo, en el epígrafe …)».
5. **Error 6.** Faltaba la salvedad del RD 1085/2020 (deroga el anexo de convalidaciones del
   RD 1680/2011), que sí da el tema 4. Añadida en «Normativa» y fila en «Trazabilidad».
6. Precisión: «entre las actividades que propone para alcanzarlo» (0910) → son las actividades de
   enseñanza-aprendizaje de las orientaciones pedagógicas para los objetivos del módulo, no del RA.
7. Forma: negrita que no era literal (títulos de los tres casos prácticos) → pasan a `###`; índice
   regenerado. «around 33%» sin negrita en la tabla práctica → en negrita (es literal de EBU R 118,
   igual que en el pasaje copiado).
8. Duplicado: «Sus posiciones de trabajo tienen nombre propio:» precedía al párrafo copiado que dice
   lo mismo. Quitado.
9. Portada: extensión 17.600 → 17.700.

Sin hallazgos en: convenio, RD 1680/2011 (módulos y letras), RD 500/2024, resto de citas del LE,
remisiones internas y a otros temas, siglas (`refutar_prosa.py`).

Pasajes cambiados releídos: cada «ese epígrafe», «(5.2)», «(3.17.1.5)» tiene su antecedente.

## Lentes

`negritas.py` (RD 1680/2011, LE, convenio): 142 negritas, 0 atribuidas a otro precepto; las 93 «no
está» son de fuentes no pasadas (EBU, fabricantes, copiado del común). `refutar_exactitud.py` y
`refutar_modo.py` no se pasaron: las fuentes son `.txt` sin articulado BOE (el RD se cita por
módulo y RA) y el tema no usa «podrá/deberá» de norma. `refutar_prosa.py`: 0. `indice.py`: regenerado.

## Ficheros tocados

- Modificado: `temas/canal-sur-especificos/33-realizador-a/08-camaras-opticas-soportes-encuadres.md`.
- Creado: este informe.
- Nota: `indice.py` se lanzó una vez sin argumento (regenera todos los temas del .tsv); `git status`
  no muestra cambios en ficheros versionados.
- Aviso al coordinador: el directorio temporal de la sesión lo comparten agentes en paralelo (otro
  sobrescribió un fichero de trabajo mío con datos del tema 10); los de éste van en `t08r33/`.
