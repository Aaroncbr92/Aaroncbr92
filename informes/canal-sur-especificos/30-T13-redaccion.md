# Puesto 30 · Tema 13 · Redacción (fase 2)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Se escribe según avanza.

Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/13-automatizacion-plantillas-mam-newsroom-flujos.md`.
Material: `30-investigacion-A-tecnica.md` (§ Tema 13 y § 8.3); RTVE `ing-tec-teleco/10` y
`ing-sup-teleco/14` (55 %, `actualizar: no`); Redactor/a T07 (cerrado); convenio y fuentes guardadas
en `fuentes/canal-sur/montador/`.

## Fuentes releídas y fecha

| Fuente | Qué se releyó | Fecha |
|---|---|---|
| X Convenio RTVA, txt local | Fichas 5212206 (p. 190) y 5212204 (p. 127) | 25-09-2026 |
| mosprotocol.com (mos.txt, moscur.txt, mosfaq.txt) | Portada, versiones vigentes y FAQ completas | 25-09-2026 |
| Avid, avnews.txt y avpm.txt | Páginas de Newsroom Management y Production Management | 25-09-2026 |
| EBU Tech 3293 v1.10, txt | § 1 (p. 7) y § 2.1 (p. 8); paginación comprobada por las cabeceras | 25-09-2026 |
| Resolve 21, extractos | proxy.txt (pp. 198, 215-216), vars.txt (pp. 345-346), titles.txt (p. 1215), render.txt (pp. 4185, 4193-4194, 4215), integr.txt (p. 4418) | 25-09-2026 |
| Adobe (Wayback), wb-ame.txt y wb-ingest-proxy-workflow.txt | Cola y *preset* por defecto de Media Encoder; flujo de *proxies* | 25-09-2026 |
| Libro de estilo de Canal Sur y Manfredi (2010) | No releídos: llegan en pasajes copiados de Redactor/a T07 (leídos allí el 24-09-2026) | — |

## Qué se hizo

Tema escrito por partes (portada y siglas; De dónde sale y 1 Automatización; 2 Plantillas; 3 MAM/PAM;
4 Newsroom; 5 Flujos integrados; aplicación práctica, «no da» y trazabilidad), guardando cada parte en
el fichero del tema. Los pasajes copiados se extrajeron por número de línea con un script, para que la
copia sea literal. Índice con `indice.py`; `refutar_prosa.py`: 1 hallazgo, falso positivo (MAM en el
título, presentada en las siglas). Tema técnico sin norma legal: no proceden `negritas.py`,
`refutar_exactitud.py` ni `refutar_modo.py`. Extensión: 8.300 palabras (`indice.py`).

Nuevo respecto de lo copiado, todo leído en su fuente el 25-09-2026: ficha 5212206 (tarea de emisión
automatizada y las demás tareas en la tabla de § 5) y ficha 5212204; MOS completo; Avid NRCS y
Production Management; EBUCore; Resolve (carpetas vigiladas, segundo plano, cola, *render* remoto,
*presets* .xml, variables, rótulos, integraciones y MAM); Adobe (Media Encoder, *proxies*).

Observaciones a la investigación:
- Resolve p. 4418 dice además, literal, que **«several Media Asset Management (MAM) systems»** se
  acceden por los *Workflow Integration Plugins* (ejemplo EditShare FLOW): no estaba en la investigación
  y se ha añadido.
- El Blackmagic Proxy Generator documenta carpetas vigiladas (proxy.txt, pp. 215-216); la
  investigación sólo marcaba como no leídas las de Adobe. Se usan las de Blackmagic; las de Adobe siguen
  en «no da».
- *Render* remoto: el manual pone tres condiciones (la investigación no lo trataba); se recogen las tres.
- MediaCentral | Asset Management: no confirmado en página; quitado, como pedía la investigación.
- El temario RTVE `ing-tec-teleco/10` presenta MOS como «intercambio de material de noticias»: la
  fuente dice *Media Object Server Communications Protocol*. No se copió esa sigla; se tomó de la fuente.
- Expansiones sin fuente leída que quedan en siglas: PAM (*production asset management*, «como lo nombra
  la industria»), TCP/IP, XML, API y UIT. El verificador decide si bastan.

## Copiado del común

Pasajes copiados literal de temas cerrados de Redactor/a
(`temas/canal-sur-especificos/34-redactor-a/07-redaccion-audiovisual-television.md`), extraídos por
líneas:

| Origen (líneas) | Pasaje | Dónde va en este tema |
|---|---|---|
| T07 (351-366) | «La escaleta»: definición (6.1), partes de emisión, cambios (6.1), nombre del vídeo (6.1.1) y textos del redactor (6.1.2), sin el rótulo | § 4 «El sistema de redacción en Canal Sur» |
| T07 (377-381) | Párrafo «Lo que el redactor deja en la escaleta es de todo el equipo…» (6.1.2) | ídem |
| T07 (385-398) | Párrafo de Manfredi (2010) y viñetas de iNews e iNews Instinct (pp. 139-140); se omite la viñeta de claves de redacción | ídem |

## Copiado de RTVE sin cambios

Los dos temas RTVE están marcados `actualizar: no` en `canal-sur-reuso/realizacion.tsv`. Palabras sin
tocar (incluidas las mayúsculas de énfasis del original); se quitó la negrita, porque en Canal Sur la
negrita marca literal de fuente y esos temas declaran no citar ninguna, y se quitó el signo ✔ de dos
filas de tabla. En el tema van presentados como oficio.

`temas/ing-tec-teleco/10-sistemas-de-redaccion-digital.md`:

| Líneas | Pasaje | Dónde va |
|---|---|---|
| 52-57 | Tabla de las cuatro etapas del flujo (sin ✔ en la fila de ingesta) | § 5 «Qué es un flujo integrado» |
| 59-60 | «Y el archivo atraviesa las cuatro…» | ídem |
| 62-64 | «La regla que ordena el punto…» | ídem |
| 99-101 | «Y la razón por la que la ingesta en directo es la crítica…» | § 5 «La entrada: vías de ingesta» |
| 103-105 | «Los tres datos que se capturan en la ingesta…» | ídem |
| 116-122 | Tabla de las cinco funciones del MAM | § 3 «Qué hace un MAM» |
| 130-133 | Desde «Cada material se transcodifica…» hasta «…en cada mesa.» | § 3 «La copia de baja resolución» |
| 135-138 | «Y la distinción de vocabulario que conviene tener…» (DAM/MAM) | § 3 «Qué hace un MAM» |
| 146-153 | Tabla de los dos niveles de edición y párrafo del conformado | § 4 «La edición dentro de la redacción» |
| 157-165 | Tabla de la emisión en tres piezas y principio de separar la emisión | § 1 «La emisión automatizada» |
| 179-184 | Tabla de los dos almacenamientos | § 3 «Dónde vive el material» |
| 188-196 | Tabla de las tres redes y razón de la separación (sin la frase de l. 197, remisión a su tema 18) | § 5 «Las redes que sostienen el flujo» |

`temas/ing-sup-teleco/14-sistemas-de-redaccion-e-informativos.md`:

| Líneas | Pasaje | Dónde va |
|---|---|---|
| 35-38 | «Y la idea que ordena el punto: … la ESCALETA es la base de datos…» | § 4 «El sistema de redacción» |
| 59-60 | «Qué es: la herramienta donde se escribe…» | ídem |
| 64-71 | Tabla de lo que contiene el sistema de redacción | ídem |
| 75-80 | Puntos 1 y 2 de «las tres cosas que hacen útil ese sistema» | ídem |
| 90-95 | Tabla de las cuatro vías de ingesta | § 5 «La entrada: vías de ingesta» |
| 99-101 | Regla 1 de la ingesta | ídem |
| 105-107 | Regla 3 de la ingesta | ídem |
| 109-111 | Desde «la ingesta es donde el almacenamiento se llena» (sin «Y el aviso que enlaza con el tema 18:») | § 3 «Dónde vive el material» |
| 117-123 | Tabla edición de informativos / postproducción (sin su rótulo, que remite al tema 15 de RTVE) | § 4 «La edición dentro de la redacción» |
| 125-132 | «Y las dos consecuencias técnicas de esa columna izquierda» y sus dos puntos | ídem |
| 158-161 | «Y la observación de arquitectura que cierra el punto…» | ídem |
| 175-180 | «Y las dos reglas que hay que llevar aprendidas» (redundancia y degradación) | § 5 «Cuando algo falla» |

## Adaptado de RTVE (sí se verifica)

- `ing-sup-teleco/14`, regla 2 de la ingesta (l. 102-104): se quita «, y eso viene del tema 11».
- `ing-sup-teleco/14`, tabla de degradación (l. 167-174): se quitan «: tema 20» y «: tema 24» de dos
  filas; el resto de la tabla, igual.
- `ing-sup-teleco/14`, punto 3 de «las tres cosas» (l. 81-84): reescrito en prosa propia para enlazar
  con MOS, que sí tiene fuente.

## Ficheros tocados

El tema 13 (nuevo) y este informe. Ficheros de trabajo en el directorio temporal de la sesión.

## Diez preguntas tipo test y comprobación

| Nº | Rúbrica | Pregunta (respuesta correcta en cursiva) | ¿La contesta el tema? |
|---|---|---|---|
| 1 | Automatización | Según su ficha del convenio, ¿qué tarea tiene el Operador/a Montador/a respecto de la emisión automatizada? a) Programar el sistema de automatización; b) *Etiquetar, grabar e introducir en base de datos la información para la emisión automatizada de programas y bloques publicitarios*; c) Supervisar la continuidad; d) Ninguna | Entera (§ 1 y § 5) |
| 2 | Automatización | En la emisión de un informativo, ¿qué pieza ejecuta la escaleta disparando servidor, grafismo y conmutación? a) El MAM; b) El servidor de emisión; c) *La automatización*; d) El apuntador | Entera (§ 1) |
| 3 | Automatización | En el Blackmagic Proxy Generator, al copiar un fichero nuevo en una carpeta vigilada… a) hay que lanzar la transcodificación a mano; b) *se transcodifica automáticamente a *proxy*, sin intervención, en una subcarpeta «Proxy»*; c) se borra el original; d) se envía a la cola de *render* | Entera (§ 1) |
| 4 | Plantillas | Los *presets* de *render* personalizados de DaVinci Resolve se exportan en ficheros… a) .drp; b) *.xml*; c) .mogrt; d) .edl | Entera (§ 2) |
| 5 | Plantillas | En Resolve, una variable de metadatos se introduce en un campo de texto escribiendo… a) #; b) *%*; c) @; d) $ | Entera (§ 2) |
| 6 | MAM/PAM | ¿Cuál de estas NO es una de las cinco funciones del MAM que da el tema? a) Catálogo; b) Ciclo de vida; c) Permisos; d) *Conmutación de la señal de emisión* | Entera (§ 3) |
| 7 | MAM/PAM | Según EBU Tech 3293, EBUCore es… a) un códec; b) *«the Dublin Core for media»*; c) un protocolo de redacción; d) un contenedor | Entera (§ 3) |
| 8 | Newsroom | El protocolo MOS… a) es una norma SMPTE; b) *comunica los sistemas de redacción (NCS) con servidores de objetos de medios, y su versión 4.0 (2019) usa Secure Web Sockets*; c) lo publicó la EBU en 1998; d) sólo sirve para audio | Entera (§ 4) |
| 9 | Newsroom | Según el Libro de estilo de Canal Sur, el nombre de una noticia en escaleta… a) lo cambia el montador al exportar; b) *debe respetarse por obligación, salvo el vídeo terminado antes de hacerse la escaleta*; c) lo fija la automatización; d) es libre | Entera (§ 4) |
| 10 | Flujos integrados (práctica) | En una redacción integrada, el redactor corta sobre la copia ligera y la pieza se emite en alta. ¿Qué operación aplica sus decisiones al material grande, y dónde aparecen los fallos? a) La ingesta, si falta espacio; b) *El conformado, si los códigos de tiempo no coinciden*; c) La exportación, si el *preset* es otro; d) El archivo, si falta metadato | Entera (§ 4, tabla de dos niveles y conformado; aplicación práctica) |

Las diez se contestan enteras con el tema; no ha hecho falta ampliar.
