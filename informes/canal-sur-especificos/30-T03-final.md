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

---

# Segunda ronda de fase 5 bis (sobre la segunda ronda de remate)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Entrada: `30-T03-remate.md`, «Segunda ronda»
(2 correcciones, 4 ampliaciones). Pasajes localizados con `git diff` del tema. Ficheros tocados: el
tema y este informe.

## Fuentes releídas (25-09-2026, copia local)

- Blackmagic, *DaVinci Resolve 21 Reference Manual*: `proxy.txt` pp. 219-220; `render.txt` p. 4196.
- Avid, *Media Composer User's Guide* R8.0 (1999): p. 332 (número de página en cabecera, como en p. 336).
- Adobe, «Relink media in Premiere» (Wayback, «Last updated on Apr 15, 2026»): «Required manual relinking».
- AMWA, «AS-11» (`amwa-as11.txt`).

## Pasaje por pasaje

| Pasaje | Comprobación | Resultado |
|---|---|---|
| «No da», *Dynamic Relink* sin definición | Sólo se quita texto | Correcto |
| «No da», AS-11 | AMWA: «constrained media file formats (based on MXF) for the delivery of finished media assets to a broadcaster **or publisher**» | Salvedad omitida: corregido |
| § 6 Resolve, *Proxy Handling* | p. 219: *Cut* por icono del visor, *Edit* por *Playback > Proxy Handling*; tres modos, cita «forces the original media playback only», «Media Offline», línea morada en *Prefer Proxies* y *Prefer Camera Originals* | Correcto; «epígrafe 4» tiene la línea morada (cita p. 220) |
| § 6 Resolve, «Use proxy media» | p. 220: cita «if you are editing with proxies and do not have access to the original source media», literal | Correcto |
| § 7 Consolidar, colas | p. 332, paso 6: «60 frames (NTSC) or 50 frames (PAL) to accept the default», sólo para *subclips* o secuencias | Correcto |
| § 7 Premiere, cuatro casos | Página Adobe: los cuatro casos y la cita de *File Extension*, literales; «Link Media dialog box» | Correcto salvo una traducción: corregido |
| § 8 *Single clip* / *Individual clips* | p. 4196: TC «Start timeline timecode at»; cita de cadencia literal; «Most effects are "baked into"»; «Render Timeline Effects», «Render at Source Resolution» | Una salvedad omitida: corregido |
| Trazabilidad (Avid 332, fila AMWA) | Cuadra con lo citado | Correcto |

## Correcciones aplicadas (comprobadas en la fuente)

1. § 7 Premiere. Antes: «un árbol que no cuelga del proyecto ni de su carpeta inmediata». Ahora:
   «que no cuelga de la carpeta del proyecto ni de la que la contiene» («not a subdirectory of the
   project or its immediate parent»; cuadra con la búsqueda automática descrita justo antes).
2. § 8 *Individual clips*. Antes: «Cada clip sale a su propia cadencia». Ahora: «Con cadencias
   mezcladas, cada clip sale a la suya» (la fuente lo condiciona a «a project that uses mixed frame
   rates»). Error tipo 6.
3. «No da», AS-11. Antes: «entregar piezas terminadas a una cadena». Ahora: «a una cadena o a quien
   las publique» («broadcaster or publisher»). Error tipo 6.

## Antecedentes

«la línea morada del epígrafe 4» (§ 4, l. 312); «del diálogo» remite a *Link Media*, nombrado antes;
«(p. 332)» dentro de «Consolidar en Avid», que cita la guía de 1999; «(p. 4196)» abre la lista de
modos. Todos con antecedente.

## Resultado

8 pasajes revisados; 5 correctos y 3 corregidos (menores). Extensión sin cambio apreciable. El tema
queda cerrado.
