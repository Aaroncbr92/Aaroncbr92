# Puesto 30 · Tema 3 · Revisión de los pasajes rematados (fase 5 bis)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/03-sistemas-de-edicion-no-lineal.md`.
Entrada: `30-T03-remate.md` (4 correcciones, 3 ampliaciones). Ficheros tocados: el tema y este informe.

## Fuentes releídas (25-09-2026, copia local)

- Avid, *Media Composer User's Guide* R8.0 (1999), texto local: pp. 233-234, 327-330, 336.
- Blackmagic, *DaVinci Resolve 21 Reference Manual*, cap. 8 (extracto `proxy.txt`): pp. 202-203;
  cap. 22 (`conform.txt`): reenlace por bobina y código de tiempo.
- Adobe, «Ingest and Proxy workflow» (Wayback, «Last updated on Jan 7, 2026»).

## Pasaje por pasaje

| Pasaje | Comprobación | Resultado |
|---|---|---|
| § 7 Reenlazar, «A veces pasa…» | p. 336: «Sometimes after you consolidate or move material between systems» | Correcto; «la misma guía» tiene antecedente (guía de 1999, p. 336) |
| § 7 *Decompose*, tercer punto | p. 233: «Decompose breaks any links to the original source clips»; duplicar, paso 2 «(Option)» nuevo *bin*; «Avid recommends this method if you intend to use the Decompose feature.» | Correcto, literal; pp. 233-234 cuadran con las marcas de página |
| § 5, códecs para HDR | p. 202 (marca [[p202]]): los cuatro con DNxHR 444; p. 203: «any of these three codecs are appropriate optimized formats for HDR grading» (16-bit float, ProRes 4444, 4444 XQ); lista de alfa | Correcto; «la página siguiente» remite a p. 202 |
| Aplicación práctica, paso 6 | Avid p. 336 (tape name, timecode); Resolve p. 492 (reel name y timecode); Premiere por rutas en § 7 | Correcto; «epígrafe 7» existe |
| § 7 *Consolidar en Avid* (nuevo) | pp. 327-330: cita inicial, .old/.new desde .01, «does not save storage space», *subclip*, secuencia «automatically relinked», nota de duplicar, tres fines | Literales correctos. **Un error corregido** (abajo) |
| § 6 tabla Resolve, «Playback > Use Optimized Media if Available» | p. 202: «choosing Playback > Use Optimized Media if Available to toggle Optimized media on and off» | Correcto |
| § 6 Premiere, cuatro funciones no admitidas | Página Adobe: las cuatro frases, literales | Correcto; «La misma página» tiene antecedente |

## Corrección aplicada

- § 7 *Consolidar en Avid*. Antes: «Se hace desde el *bin*, porque la *Media Tool* sólo muestra
  *master clips*». La fuente (p. 327) dice que por eso **no** se pueden consolidar con la Media Tool
  *subclips* ni secuencias, y que en el *bin* se consolidan los tres: «you cannot consolidate subclips
  or sequences with the Media tool. You can consolidate master clips, subclips, and sequences in the
  bin.» Ahora: «*Subclips* y secuencias se consolidan desde el *bin*, porque la *Media Tool* sólo
  muestra *master clips*; en el *bin* se pueden consolidar los tres». Error tipo 6 (salvedad omitida).

## Observación sin cambio

- Paso 6: Resolve usa el nombre de bobina sólo si se usa o se activa en los ajustes del proyecto
  (`conform.txt`, «reel name (if used)»); el paso remite al epígrafe 7, que da la fuente con p. 492.
  Suficiente para el supuesto; no se toca.

## Resultado

7 pasajes revisados; 6 correctos y 1 corregido. Antecedentes comprobados. Extensión sin cambio
apreciable (+10 palabras). El tema queda cerrado.
