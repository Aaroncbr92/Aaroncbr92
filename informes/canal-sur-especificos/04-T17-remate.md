# 04 · Ayudante de Producción · Tema 17 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/17-prevencion-de-riesgos-laborales-aplicada-al-puesto-de-trabajo.md`.
Fecha de corte: 24-09-2026. Fuentes releídas el 06-10-2026 (fecha del sistema).
Ficheros tocados: el tema y este informe. **Amplía**: sí (dos citas literales nuevas).

## Comprobación en la fuente (06-10-2026)

- RD 486/1997 (BOE-A-1997-8669), anexo I, apartado 10.8.º (redacción de BOE-A-2004-19311, aplicable
  desde 03-12-2004): literal confirmado. El informe acertó.
- RD 487/1997 (BOE-A-1997-8670), art. 4, primer párrafo (1 redacción): literal confirmado. Acertó.
- RD 487/1997, anexo, factor «suelo… resbaladizo»: confirmado que el anexo no dice «mojado». Acertó.

## Pasajes cambiados

1. **Epígrafe 2, «Estudios, platós y montajes», primera viñeta** (menor 2 + laguna 1, pregunta 12).
   Antes: «Las vías de evacuación: el decorado, las gradas del público y los cables no pueden
   estrecharlas ni cerrarlas. Las medidas de emergencia y evacuación son las del artículo 20…».
   Ahora: «Las vías de evacuación (apartado 10.8.º): **«Las vías y salidas de evacuación […] Las
   puertas de emergencia no deberán cerrarse con llave.»** Por eso el decorado, las gradas del
   público y los cables no pueden estrecharlas ni cerrarlas. Las medidas de emergencia y evacuación
   de la empresa son, además, las del artículo 20 de la Ley 31/1995 (epígrafe 1).»
2. **Epígrafe 2, «Manipulación manual de cargas», párrafo del art. 4** (laguna 2, pregunta 8).
   Se antepone el primer párrafo literal: **«De conformidad con los artículos 18 y 19 de la Ley de
   Prevención de Riesgos Laborales, el empresario deberá garantizar que los trabajadores y los
   representantes de los trabajadores reciban una formación e información adecuadas […]»**, y el
   párrafo existente pasa a introducirse con «Y en particular, el empresario **«proporcionará…»**».
3. **Epígrafe 2, «Exteriores: el trabajo al aire libre», último párrafo** (menor 1). «La lluvia añade
   el suelo mojado, que es factor de riesgo…» → «La lluvia puede dejar el suelo resbaladizo, que es
   factor de riesgo del anexo del RD 487/1997 al cargar el material.» La fila «no esperar sobre suelo
   mojado» de la tabla anterior se deja: es consejo de oficio frente al frío, no atribuido al anexo.
4. **«Normativa que el tema invoca»**, fila RD 486/1997: «anexo I (apartado 12)» → «anexo I
   (apartados 10.8.º y 12)».
5. **«Trazabilidad»**, frase de fechas: se añade el apartado 10.8.º del anexo I del RD 486/1997 entre
   lo leído el 06-10-2026. La fila del RD 486/1997 ya daba la redacción del anexo I (03-12-2004).

Antecedentes releídos: «estrecharlas ni cerrarlas» → las vías; «Y en particular, el empresario» →
art. 4 recién citado; «el anexo del RD 487/1997» con su norma delante. Correctos.

## Lentes

- `indice.py`: regenerado (17.347 palabras, 38 epígrafes; no cambian los epígrafes).
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` (RD 486 y 487): las dos negritas nuevas, encontradas. Aviso «¿ART. 18?» sobre
  «proporcionará…»: falso positivo (la lente toma los «artículos 18 y 19» de la negrita anterior;
  el texto está en el art. 4 y el tema lo dice). Los «NO ESTÁ» son de la Ley 31/1995 y del RD
  773/1997, no pasados a esta lente y copiados del común o ya verificados.
- `refutar_exactitud.py` / `refutar_modo.py` (RD 486 y 487): sin hallazgos en los pasajes cambiados;
  `refutar_modo` 0 hallazgos.

Las 15 preguntas, con el tema rematado: 15 enteras. Procede fase 5 bis (el remate amplió).
