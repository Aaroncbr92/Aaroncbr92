# Puesto 28 · Operador/a de Sonido · Tema 7 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/07-sonido-en-radio.md` (10.031 palabras
tras la verificación; ficha puesta a 10.000; índice sin cambios, 49 epígrafes).
Fecha de lectura de todas las fuentes: 25-09-2026 («hoy» del encargo: 24-09-2026).

## Fuentes releídas

| Fuente | Cómo | Fecha |
|---|---|---|
| EBU Tech 3326 Rev. 4 (noviembre 2014) | PDF de tech.ebu.ch pasado a texto; alcance, § 1-4, glosario | 25-09-2026 |
| EBU Tech 3368 v1.0 (noviembre 2014) | Ídem; alcance, § 1-3.7.2 | 25-09-2026 |
| Clear-Com, *Comprehensive Guide to … Partyline Systems* (febrero 2018) | PDF pasado a texto; apartado de híbridos (pp. 17-18) | 25-09-2026 |
| Yamaha CL5/CL3/CL1 V5 Reference Manual; Yamaha, *Get on the Bus* | PDF pasados a texto (Mix Minus, Talkback; resumen de envíos) | 25-09-2026 |
| DPA Mic University, E. Bøgh Brixen, «The basics about comb filtering» | Página web pasada a texto | 25-09-2026 |
| AES TD1008.1.21-9 (24-09-2021) | PDF; tabla 1 comprobada además sobre la imagen de la página | 25-09-2026 |
| RFC 8216 (agosto 2017) | Texto de rfc-editor.org | 25-09-2026 |
| Apple, *Audio requirements – Apple Podcasts for Creators* | Página web pasada a texto | 25-09-2026 |
| UIT-T I.412 (11/1988, en vigor según la ficha de itu.int), versión española | **Nueva**: descargada de itu.int para cerrar las cifras de la RDSI | 25-09-2026 |
| EBU R 128-2023 (V5) y tema 13 del puesto | `fuentes/normas-tecnicas/EBU_R128-2023.txt` (puntos r y s, historial); tema 13 (−23 LUFS, −1 dBTP) | 25-09-2026 |
| Contrato-programa 2024-2026 (BOJA 245/2023) | `fuentes/canal-sur/documentos/…`, sólo para las dos citas del epígrafe «Qué es un pódcast» | 25-09-2026 |

## Pasajes exentos (sólo literalidad)

- **Copiado del común** (Cámara 13 y Redactor 08, cuatro bloques): subcadena exacta de sus temas
  (script, normalizando saltos de línea). No se re-verifican.
- **Copiado de RTVE sin cambios** (ocho bloques de sonido/12 y sonido/06): subcadena exacta del RTVE
  quitando `**` y ✔; la definición del N-1 lo es hasta «excepto la que nos envían.». No se
  re-verifican. Tras las correcciones se volvió a pasar el script: siguen intactos.
- Aviso sin corrección: el punto 103 del Contrato-programa (común) casa con el BOJA salvo por el
  salto de página del PDF.

## Verificado y confirmado

- 155 citas en negrita cotejadas por script con las fuentes; las 9 que el script no casó eran saltos
  de línea o de página del PDF (DSL, «Latency is an issue», MIX/MATRIX, punto 103) o fallos que se
  corrigen abajo.
- Tech 3326: retirada de la ISDN, 15-20 fabricantes, alcance, tres tipos, dos equipos, cuatro áreas,
  Tech 3329, IPv4/IPv6/multidifusión, RTP/UDP, RTCP, 5004/5005, TCP y su puerto, G.711 (PT 0/8, 20 ms),
  G.722 (PT 9, reloj 8 kHz), capa II (PT 14, 90 kHz, tabla 32-384, «frame too large»), L16 y 4 ms,
  DAT12/L20/L24, AAC-hbr, APT-X, Opus 6-510, AMR-WB, § 3.3.5, SDP, SAPv1, SIP y mensajes, 5060, RFC3264.
- Tech 3368: § 1, § 2, perfil asimétrico, tabla 1, a=ebuacip versión 0 y parámetros, búfer
  (§ 3.4-3.4.3, caso del hotel de seis ms), DiffServ, tres protecciones.
- DPA, Clear-Com, Yamaha, RFC 8216, TD1008 (tabla 1 y notas 1 y 7), Apple: citas literales.
- Remisiones a los temas 3, 4, 5, 8, 9, 11, 13 y 15: los ficheros existen y el contenido casa con el
  enunciado; el tema 13 da −23 LUFS y −1 dBTP; la R 128 V5 remite a s2, s3 y Tech 3401.
- Cálculos rehechos: −16 − 2 = −18; −16 − 1 = −17; de −23 a −18 y −16, 5 y 7 LU.

## Correcciones aplicadas (22)

1. **Tabla resumen de códecs (errores 3 y 9)**: decía «PCM 16 bits (12, 20 y 24 opcionales)». En la
   Tech 3326 el § 3.1.5 está entre los obligatorios y sólo el de 12 bits es opcional. Ahora: PCM de 16,
   20 y 24 bits obligatorios; 12 bits opcional; el PCM, opcional en los portátiles.
2. **FEC y retransmisión (error 8)**: la retransmisión se atribuía al «perfil RFC4585». La norma la
   hace según la RFC4588 (MAY), que necesita el perfil RFC4585. Se añaden la FEC según RFC5109 (SHOULD,
   puerto 5006) y la RFC2733 (OPTIONAL), con citas del § 2.2.6-2.2.7.
3. **RDSI (error 9, hueco cerrado)**: las cifras 2 × 64 kbit/s se daban «como conocimiento de la
   materia». Leída la UIT-T I.412: interfaz básica 2 B + D, B a 64 kbit/s, D a 16 kbit/s y de
   señalización, B independientes. Se cita; se quita la viñeta de «Lo que este tema no da» y la mención
   en el oficio de la trazabilidad; se añade a ficha, tabla de recomendaciones y trazabilidad.
4. **«Con RDSI, dos códecs de marcas distintas se entendían» (error 9)**: sin fuente; quitado.
5. **«Su vocabulario obligacional es el de las normas de internet» (error 9)**: la norma no lo dice
   (no cita la RFC 2119); ahora «lo define la propia norma en su alcance».
6. **MAY/OPTIONAL (error 6)**: faltaba «which, if present, SHOULD be implemented as specified…».
7. **Cambio de códec (error 6)**: añadido «Reconfiguration SHOULD be supported.».
8. **DiffServ (error 6)**: añadida la salvedad de la red conocida (§ 3.6).
9. **Respuesta 488**: la norma la da en el ejemplo del búfer; se dice y se cita la frase completa.
10. **Compatibilidad (error 6)**: «los obligatorios (G.722, MPEG capa II)» dejaba fuera G.711 y el PCM.
11. **AAC-LD de bajo retardo**: el aviso del redactor se cierra con el glosario de la Tech 3326
    («Advanced Audio Coding Low Delay»).
12. **Telefonía (error 9)**: «la norma los hace obligatorios para que un códec de radio pueda hablar
    con equipos de telefonía por IP» no está en la norma. Se sustituye por lo que sí dice (20 ms «for
    improved compatibility with voice-over-IP systems») y por la I.412 (G.711 voz, G.722 voz de banda
    ancha por un canal B). El párrafo del móvil se marca como oficio.
13. **DPA, cita con punto y coma (literalidad)**: la lista de dos causas se unía con «;» dentro de la
    negrita; ahora cada causa va en su cita.
14. **DPA 4,5:1 (error 6)**: faltaban «in theory» y la salvedad de los micrófonos direccionales
    (factor 3 basta), relevante en un locutorio.
15. **Clear-Com, «que advierte que el principio es el mismo» (error 9)**: la fuente no lo dice;
    ahora «que los usa también como enlace con la red telefónica».
16. **Polaridad invertida (errores 6 y 9)**: la fuente lo dice del híbrido de un puesto de intercom
    y añade que la copia invertida debe tener exactamente la misma amplitud; se dice y se cita. Se
    añade también la dificultad del equilibrado por las variaciones de impedancia.
17. **Oscilación (error 6)**: la cita se cortaba antes de la causa («acoustic and/or electronic
    coupling…»); completa. Que una pérdida transhíbrida escasa favorezca el pitido se declara oficio.
18. **TD1008, tabla 2 y fórmula (literalidad y error 9)**: la tabla 2 iba en negrita como cita con
    «;» inventados; pasa a redonda traducida (como la tabla 1). «La fórmula que las genera» → la fuente
    la da como **«A useful formula»** para afinar los valores. Se dice a quién va la tabla 2.
19. **TD1008, salvedades (error 6)**: «Distribution Loudness is not to be targeted to the upper
    tolerance»; la tolerancia +2 LU sin voz es también «format-specific, see Table 2»; la revisión a
    −23/−24 está condicionada al avance de los aparatos y metadatos; la remasterización es con
    «linear gain followed by peak limiting if needed». Celda del asistente virtual rellenada.
20. **LUFS = LKFS (literalidad)**: la fuente dice «LUFS: and LKFS…» (así en el PDF); se cita sólo
    «are identical units…».
21. **Apple (error 6)**: la cita se cortaba en «might clip the signal»; falta «if the recommended
    true-peak value is not respected». Corregido también el paso 3 del caso práctico.
22. **Caso práctico (error 3)**: el paso 1 parte de un máster a −24 y el 2 contaba 5 y 7 LU (desde
    −23); ahora se dice desde dónde y que desde −24 es uno más.

Además (error 5): siglas PFL, DIM, IFB y DSCP presentadas; SRT, RIST y RTMP declaradas como nombres
de protocolo. RFC 8216: no es de la IETF sino **«Independent Submission»**; se quita «IETF» delante
de su número y se cita la cabecera. Trazabilidad: fuera la mención al material de investigación
(proceso, no fuente); fechas y filas actualizadas.

## Lo que no se tocó y por qué

- Residuo de `refutar_prosa.py` (ANSI, ATSC, FS, HE, PCMA, PCMU, RX, TOS): dentro de citas literales
  en inglés o como parte de otra sigla; el redactor ya lo dejó así.
- BGAN (sigla de la tabla RTVE) se deja con su desarrollo; no hay fuente leída que lo dé.
- Sugerencia para refutación, no aplicada: el punto 104 del Contrato-programa fija 24 h/día para la
  plataforma de pódcast de Canal Sur; el tema no lo da.

## Lentes

`refutar_prosa.py`: 0 relleno, 0 repetidas, 0 negritas rotas, 8 siglas residuales (arriba).
`indice.py`: índice igual al anterior. Sin lentes de norma: el tema no cita normas legales (la I.412
es una recomendación técnica).

## Otros ficheros tocados

Ninguno fuera del tema y este informe.
