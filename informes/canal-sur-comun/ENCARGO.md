# Encargo común · Temario común de Canal Sur (Bloque I)

Lo leen todos los agentes que trabajan en el temario común de Canal Sur, sea cual
sea su fase. Antes de nada, lee enteros `metodo/MANUAL.md` y `metodo/ENCARGOS.md`.

**Siglas de este encargo**: Agencia Pública Empresarial de la Radio y Televisión de
Andalucía (**RTVA**); Canal Sur Radio y Televisión, S.A. (**CSRTV**); Boletín Oficial
del Estado (**BOE**); Boletín Oficial de la Junta de Andalucía (**BOJA**); Corporación
de Radio y Televisión Española (**RTVE**).

## La oposición

Concurso-oposición de la RTVA y CSRTV, BOJA núm. 186, de 24-IX-2026. El programa
literal está en `convocatoria/canal-sur/PROGRAMA-COMUN.md`. Las bases **no fijan
fecha de corte**: se estudia **la redacción vigente el día en que se escribe**, y el
tema lo dice en su ficha. El primer ejercicio es un test con preguntas del común,
de teoría específica y de aplicación práctica. **No hay exámenes anteriores**: la
prueba de terminado son de diez a quince preguntas en estilo test de cuatro opciones
que se escriben para cada tema (manual, apartado 7).

## Dónde vive cada cosa

| Qué | Dónde |
|---|---|
| Temas | `temas/canal-sur-comun/NN-titulo.md` |
| Esquemas | `esquemas/canal-sur-comun/NN-titulo.md` |
| Informes de cada fase | `informes/canal-sur-comun/TNN-<fase>-<agente>.md` |
| Normas del BOE, redacción vigente hoy | `fuentes/canal-sur/BOE-A-*.md` (volcadas con `herramientas/boe.py norma`) |
| Documentos que no son norma del BOE | `fuentes/canal-sur/documentos/` (PDF y su `.txt`) |
| Cruce con lo escrito para RTVE | `informes/canal-sur-reuso/comun-gestion.tsv`, filas con `puesto` = 0 |

Si necesitas una norma que no está volcada, vuélcala tú con
`python3 herramientas/boe.py norma <id> fuentes/canal-sur/` **después de comprobar
su identificador por el título** con `herramientas/boe_buscar.py`. Nunca en otra
carpeta de `fuentes/`: las de RTVE están congeladas a otra fecha y no se pisan.

## Reaprovechar lo escrito para RTVE

Los temas de RTVE ya pasaron por el ciclo. **Se reutiliza su texto literal, no se
parafrasea**, con dos cambios obligatorios:

1. **Redacción.** Los temas del general de RTVE estudian la redacción vigente el
   21-12-2022. Todo precepto que se reutilice se vuelve a leer en su redacción
   **vigente hoy** (`boe.py precepto <id> <bloque>`, o el volcado de
   `fuentes/canal-sur/`). Lo que cambió se corrige en el cuerpo, y el cambio se dice
   en una línea: qué cambió, por qué norma y desde cuándo. Las «Notas de
   actualización» de RTVE pasan al cuerpo, porque aquí no hay corte.
2. **Empresa.** Donde RTVE habla de sí misma (sus órganos, su plan de igualdad, su
   convenio, su ley), en Canal Sur no vale: se quita o se sustituye por lo de la RTVA
   leído en su fuente.

Y los epígrafes **reproducen el enunciado de Canal Sur**, literal y en su orden, no
los de RTVE.

## Forma del tema (la de RTVE)

1. `# Tema N del común · <título>`.
2. Ficha entre `<!-- portada -->` y `<!-- /portada -->`, tabla de dos columnas con:
   **Bloque** («Temario común de Canal Sur · punto N»), **Sirve para** («Los cuarenta
   puestos de la convocatoria»), **Fuente**, **Identificador**, **Redacción que se
   estudia** («La vigente el DD/MM/AAAA»), **Extensión**. Sin filas de «Esquema de
   repaso» ni de «Verificación».
3. Las siglas del tema, presentadas de entrada en un párrafo.
4. El enunciado del programa, literal, en bloque de cita, con su procedencia.
5. Un párrafo sobre qué se puede preguntar de este tema.
6. `<!-- indice -->` y `<!-- /indice -->` vacíos: los rellena `herramientas/indice.py`.
7. Los epígrafes, reproduciendo el enunciado en orden (`##` para cada rúbrica,
   `###` dentro).
8. «Normativa que el tema invoca», con identificador y redacción.
9. «Lo que este tema no da, y dónde está».
10. «Trazabilidad».

**Nada de referencias a ficheros del proyecto dentro del tema**: ni rutas, ni nombres
de herramientas, ni de informes. **La negrita es una promesa de literalidad**: lo que
va en negrita está tal cual en la fuente. Lo que no lo está va en redonda.

## Cláusulas (se aplican a todos, literales)

- «Si algo de este encargo no cuadra con la fuente, manda la fuente y dímelo.»
- «Lo que no puedas confirmar, quítalo. No lo sustituyas por lo que recuerdes.»
- «Limítate a tu tema y declara qué otros ficheros has tocado.»
- «Escribe tu informe en un fichero de `informes/` según lo vayas produciendo. No lo
  dejes solo en la respuesta.»
- «Trabaja con la redacción vigente el día en que escribes. Declara la fecha en la
  que leíste cada precepto.»
- En las refutaciones: «Cero hallazgos es un buen resultado si el tema está bien.»
- Al rematar: «Comprueba cada corrección en la fuente antes de aplicarla. Si el
  informe se equivocó, no la apliques y dilo.» y «Relee el resultado entero y
  comprueba que cada "ese artículo", "dicha ley" o "el apartado X" tiene delante el
  antecedente que le corresponde.»

## Los nueve errores que se repiten

1. Cita cruzada. 2. Ley por reglamento. 3. Recuentos que no cuadran. 4. Modo verbal
cambiado («podrá» por «deberá»). 5. Siglas sin presentar. 6. Requisito, excepción o
salvedad omitida. 7. Redacción derogada citada como vigente. 8. Número de artículo
mal. 9. Afirmación sin apoyo en la fuente.
