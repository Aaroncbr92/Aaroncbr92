# Puesto 30 · Tema 3 · Remate (fase 5)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/03-sistemas-de-edicion-no-lineal.md`.
Entrada: `30-T03-refutacion.md` (4 menores, 3 lagunas) y `30-T03-preguntas.md` (12/1/2).
Ficheros tocados: el tema y este informe.

## Fuentes releídas (25-09-2026, copia local)

- Avid, *Media Composer User's Guide* R8.0 (1999): pp. 233-234 (duplicado y *Decompose*), 327-330
  (*Consolidate*), 336 (*Relink*, «Sometimes after you consolidate…»).
- Blackmagic, *DaVinci Resolve 21 Reference Manual*, cap. 8: pp. 202-203 (medios optimizados).
- Adobe, «Ingest and Proxy workflow» (Wayback; «Last updated on Jan 7, 2026»): «Unsupported features
  in proxy workflows».

## Correcciones (todas confirmadas en la fuente)

1. § 7 Reenlazar. Antes: «Pasa, según la misma guía, **«after you consolidate…»**». Ahora: «A veces
   pasa, dice la misma guía, …» (p. 336: «**Sometimes** after you consolidate…»).
2. § 7 *Decompose*, tercer punto. Antes: «Rompe el enlace con los clips de origen, así que Avid
   recomienda duplicar antes la secuencia y guardar la copia en otro *bin*». Ahora: cita literal
   «Decompose breaks any links to the original source clips»; para conservar la primera versión se
   duplica la secuencia y, en paso opcional, se pasa a un *bin* nuevo; cita «Avid recommends this
   method…» (pp. 233-234; el paso 2 va marcado «(Option)»).
3. § 5, códecs para medios optimizados. Añadido que en p. 203 el manual nombra sólo tres para HDR,
   sin DNxHR 444 (cita literal «any of these three codecs are appropriate optimized formats for HDR
   grading»); la frase de p. 202 queda con su página.
4. Aplicación práctica, paso 6. Antes: «se reenlaza por nombre de fichero, bobina y código de
   tiempo». Ahora: «Avid y Resolve reconocen el clip por nombre de cinta o bobina y código de tiempo;
   Premiere lo busca por sus rutas (epígrafe 7)». Ajuste a la propuesta: Premiere no reenlaza por
   bobina y TC sino por rutas históricas y búsqueda (§ 7 ya lo da), así que se nombra aparte.

## Lagunas ampliadas (contenido nuevo)

1. **Nuevo `### Consolidar en Avid`** en § 7, tras *Decompose* (guía 1999, pp. 327-330): qué hace,
   que se hace desde el *bin*, comportamiento con *master clip* (.old/.new, copia exacta, no ahorra
   espacio), *subclip* (sólo la parte, *master clip* y *subclip* nuevos) y secuencia (reenlace
   automático; duplicar para conservar enlaces), y los tres fines de consolidar secuencias. El
   párrafo de oficio «Con ficheros la cinta ya no está…» queda al final de este apartado.
   Trazabilidad: añadidas pp. 327-330. «Qué se puede preguntar»: añadido *Consolidate*.
2. § 6, tabla de las tres ayudas de Resolve, fila de medios optimizados: se activan y desactivan con
   «Playback > Use Optimized Media if Available» (p. 202).
3. § 6, Premiere. Antes: «están estas dos» (After Effects y Audition). Ahora las **cuatro** que da la
   página: además, «Dynamic Link is not supported for After Effects compositions or projects.» y
   «The option to modify audio channels and interpret footage isn't supported.». La refutación
   contaba tres; la fuente da cuatro: manda la fuente.

No aplicado: nada. «Alternar *proxy*/original desde el monitor de Premiere» no está en las fuentes
locales; no se añade.

## Relectura de antecedentes

Pasajes cambiados releídos: «la misma guía» (§ 7) tiene delante la guía de 1999, p. 336; «la guía»
en *Decompose* y *Consolidate*, ídem; «la página siguiente» remite a la p. 202 citada justo antes;
«La misma página» (Premiere) remite a la de ingesta y *proxies*; «epígrafe 7» en el supuesto existe.

## Lentes

- `indice.py`: índice regenerado (nuevo apartado en § 7; 44 epígrafes; 8.902 palabras de cuerpo).
  Ficha: extensión pasada de «8.500» a «9.000 palabras aproximadamente».
- `refutar_prosa.py`: 0 hallazgos. Tema técnico sin norma: no tocan las demás lentes.

## Resultado

4 correcciones y 3 ampliaciones con contenido nuevo (la mayor, *Consolidate*). Con el tema así, las
preguntas 12, 13 y 14 pasan a contestarse enteras. Procede la fase 5 bis sobre los pasajes cambiados.
