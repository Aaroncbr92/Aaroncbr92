# Puesto 30 · Tema 8 · Redacción (fase 2)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Se escribe según avanza.

Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/08-ingesta-digitalizacion-transferencia-verificacion-copias-metadatos-archivo.md`.
Material: `30-investigacion-A-tecnica.md` (§ Tema 8); tema cerrado 08-07 (Cámara Operador); RTVE
`edicion-montaje/05`, `edicion-montaje/01`, `ing-tec-teleco/10` (`canal-sur-reuso/realizacion.tsv`,
fila 30/8: 65 %, «actualizar: no»).

## Avance
- Portada, siglas, enunciado, preguntas, índice y «El punto en la ficha del puesto»: guardado (p1).
- § 1 Ingesta: guardado (p2). § 2 Digitalización: guardado (p3). § 3 Transferencia: guardado (p4).
- § 4 Verificación: guardado (p5). § 5 Copias de seguridad: guardado (p6). § 6 Metadatos: guardado (p7).
- § 7 Archivo: guardado (p8). Aplicación práctica, documentos, lo que no da y trazabilidad (p9).
- Montado con un script que inserta los pasajes de Cámara T07 por número de línea (copia byte a
  byte). Índice generado con la función `epigrafes` de `indice.py` (anclajes de GitHub).
- `refutar_prosa.py`: 0 siglas sin presentar tras completar la lista (SDI, IP, BWF); una «frase
  repetida» que es la cita del convenio en dos tablas (se deja). `negritas.py` contra las fuentes
  nuevas: 121 negritas cotejadas; las 23 que no aparecen son todas de pasajes copiados de Cámara T07
  (fuentes de aquel tema, no pasadas al script).
- Extensión: unas 10.600 palabras con índice (unas 10.000 de cuerpo); siete rúbricas y un tercio
  largo de texto copiado.

## Estructura
Ficha del puesto (4 tareas del convenio que tocan el tema) · § 1 Ingesta (formas, por origen, flujo de
la redacción, tarjeta paso a paso, ingesta en Premiere y Resolve, ingestar frente a importar) · § 2
Digitalización (captura desde cinta en Resolve: requisitos, ajustes, tres métodos y EDL; nombre de
cinta y TC; revisión) · § 3 Transferencia (señal y fichero, envío desde el lugar, FTPES, cálculo de
tiempo, local/NAS/SAN, tres redes) · § 4 Verificación (suma de verificación, seis algoritmos de
Resolve, OAIS QA y Error Checking, verificación de contenido, Libro de estilo 5.3.3) · § 5 Copias
(por qué, 3-2-1, qué más se copia, RAID) · § 6 Metadatos (qué son, en el fichero, en el programa,
en el sistema/MAM, EBUCore) · § 7 Archivo (compactar, producción/archivo, OAIS, LTO-10, LTFS, rótulo
de archivo) · aplicación práctica · documentos · lo que no da · trazabilidad.

## Copiado del común
Del tema 7 de Cámara Operador (`08-camara-operador/07-formatos-codecs-tarjetas-ingesta-entrega.md`,
cerrado). Insertados por número de línea; no se re-verifican salvo lo señalado.

| Líneas en Cámara T07 | Pasaje | Dónde va | Cambios |
|---|---|---|---|
| 806-814 | «Qué es la ingesta», párrafo y tabla de tres formas | § 1 · Qué es la ingesta | Literal. Se omite 816-818 (propio del cámara) |
| 822-842 | «La ingesta de una tarjeta, paso a paso» | § 1 | Literal salvo tres remisiones: «(véase «Copia de seguridad»)» → «(véase «Verificación»)»; «clips sin sonido (cámara lenta, tema 15).» → «clips sin sonido.»; «(véase «Entrega de material»)» → «(véase «Metadatos»)». **El verificador mira sólo esas tres** |
| 846-848 | «La ingesta desde el lugar», primer párrafo | § 3 · El envío desde el lugar | Literal |
| 984-988 | «El envío por red», primer párrafo (FTP/FTPES, Z200 p. 196) | § 3 · El envío desde el lugar | Literal |
| 882-903 | «La copia comprobada: suma de verificación» (DPC), sin el párrafo «Aplicado al cámara» | § 4 | Literal |
| 868-871 | «Por qué» (copia de seguridad) | § 5 | Literal |
| 911-913 | Regla 3-2-1 de INCIBE, primer párrafo | § 5 | Literal (la aplicación es nueva) |
| 921 y 930-935 | RAID: frase de entrada y párrafo «El número del nivel no es…» | § 5 | Literal; la tabla de Cámara se sustituye por la de RTVE 01 (cinco niveles) |
| 666-671 | «Qué son y quién los pone» (metadatos) | § 6 | Literal |
| 795-799 | «Los metadatos dentro del fichero» | § 6 | Literal hasta «(véase «Ingesta»).»; se quita la última frase («Los identificadores únicos… no se tratan»), porque el UMID sí está leído en el tema 15 de este puesto |
| 939-944 | LTO: «Lo que ya no se toca pasa al archivo…» | § 7 | Literal hasta «es archivo (oficio).»; se quita la última frase (propia del cámara) |

## Copiado de RTVE sin cambios
(Temas RTVE marcados «actualizar: no» en `realizacion.tsv`, fila 30/8. Palabras sin tocar; sólo se
quitan las negritas de énfasis de RTVE —en Canal Sur la negrita marca cita literal—, las marcas ✔ de
respuesta de examen y las mayúsculas de énfasis. Comprobado por script, frase a frase, contra el texto
RTVE normalizado.)
- `ing-tec-teleco/10` § 1: tabla de las cuatro etapas (sin ✔); «Y el archivo atraviesa las cuatro…
  se ejecuta después.»; «La regla que ordena el punto: … carpeta compartida.» («DATOS DESCRIPTIVOS»
  en minúscula).
- `ing-tec-teleco/10` § 2: tabla de tipos de ingesta por origen (sin ✔); «Y la razón por la que la
  ingesta en directo es la crítica… sistemas independientes.»; «Los tres datos que se capturan en la
  ingesta… está perdido.»
- `ing-tec-teleco/10` § 3: tabla de las cinco funciones (catálogo, versiones, baja resolución, ciclo
  de vida, permisos).
- `ing-tec-teleco/10` § 5: tabla de los dos almacenamientos (producción y archivo); tabla de las tres
  redes; «Y la razón de la separación… puede parar la emisión.» (sin la frase siguiente, que remite
  al tema 18 de RTVE).
- `edicion-montaje/01` § 2: párrafo «Las siglas: redundant array… unidad completa—.»
- `edicion-montaje/01` § 3: tabla de niveles de RAID (0, 1, 5, 6 y 10).
- `edicion-montaje/01` § 4: tabla «Con tres discos»; «La regla mnemotécnica que no falla: RAID 0,
  cero seguridad. RAID 1, un disco copiado en otro.» (sin la frase de las «cuatro opciones»).
- `edicion-montaje/01` § 5: «Dónde vive el material determina cómo se monta, y el vocabulario aparece
  en los enunciados:»; tabla local/NAS/SAN; «La diferencia que importa al montador…»; «Y en
  cualquiera de los tres, debajo hay un RAID…».
- `edicion-montaje/01` § 7: las dos frases «La conversión analógico-digital, en una frase: … cuántos
  matices.» (dentro del párrafo nuevo de § 2 «Qué es digitalizar»).

## Adaptado de RTVE (sí se verifica)
- `edicion-montaje/01` § 4: «Cómo lo consigue: la paridad.» → «Cómo lo consigue el RAID 5: la
  paridad.»; el resto del párrafo, literal.
- `edicion-montaje/01` § 6: «Lo que el montador necesita saber de la red, más allá de la pregunta:» →
  sin «más allá de la pregunta»; las dos frases siguientes, literales.
- `ing-tec-teleco/10` § 5: «Las tres redes que conviven en una redacción, que es lo más preguntable de
  lo que no ha caído:» → cortada tras «redacción».
- `ing-tec-teleco/10` § 3: párrafo DAM/MAM, con siglas añadidas, mayúsculas quitadas y remisión al
  tema 13.
- Quitado de RTVE por propio de RTVE o sin fuente: respuestas oficiales, opciones falsas y avisos de
  examen de los tres temas; de `edicion-montaje/05`, lo ligado a la plantilla (XDCAM, menú 150, disco,
  recurrencias del sistema de ingesta, audio del HD422) y el rótulo «Op1b-Atom» (el perfil es
  OP-Atom); sus secciones de ingesta y LTO se sustituyen por las de Cámara T07, ya verificadas.
  La definición de LTO de RTVE 05 coincide en sustancia con la del programa LTO, que el tema cita
  ahora en su texto original.

## Escrito nuevo (se verifica entero)
Ficha del convenio (objeto y cuatro tareas; control de calidad en § 4); Premiere (ingesta y
verificación); Resolve cap. 17 (Clone Tool, seis algoritmos, varios destinos, copia fuera), cap. 18
(metadatos, palabras clave, exportación CSV/ALE), cap. 24 (captura desde cinta); EBUCore (Tech 3293
v. 1.10, pp. 3, 7, 8); RP 210 retirada; OAIS (§§ 1.1, 1.6.2, 4.2.2, 4.2.3.3, 4.2.3.4); LTO-10 y
compatibilidad (lto.org/roadmap); LTFS; Libro de estilo 5.3.3 (p. 82) y 9.9.1 (p. 166); aplicación
práctica; cálculo de transferencia. Oficio declarado en cada sitio.

## Fuentes y fecha de lectura
Todas leídas en su pasaje citado el 25-09-2026: convenio (`documentos/x-convenio-rtva-boja-240-2014.txt`,
p. 190), Libro de estilo (`documentos/libro-de-estilo-333233b.txt`), `montador/resolve21-extractos/`
(`mediapool.txt`, `metadata.txt`, `tape.txt`), `montador/web/wb-ingest-proxy-workflow.txt`,
`montador/ebu/tech3293.txt` y `montador/ccsds-650x0m3-oais.txt` (pasados hoy a texto con
`documento.py texto`), `montador/web/ltfs.txt`, `montador/smpte/catalogo-rp210.txt`, y la página LTO
«roadmap» (nuevo `montador/web/lto-roadmap.txt`).

## Discrepancias y avisos
- LTO roadmap: la investigación la leyó sólo con resumen automático («citas a confirmar»). Hoy una
  descarga directa con curl devolvió la página y confirmó al pie de la letra generación, 100 TB
  comprimidos, 1200 MB/s y la compatibilidad hasta la 7.ª; las descargas siguientes cayeron en un
  captcha, y la nota «Assuming a 2.5:1 compression…», la frase de la 8.ª/9.ª/10.ª y la definición se
  leyeron con WebFetch pidiendo literal. Todo guardado con su procedencia en `lto-roadmap.txt`. El
  verificador puede querer releer esas tres en la web.
- OAIS: la investigación cortó la definición de «Long Term»; el tema da la definición completa del
  § 1.6.2. Las definiciones de SIP, AIP, DIP están en el § 1.6.2 (terminología), no en otro.
- Batch Capture Via EDL: aparece en el índice del capítulo 24 (p. 558); su desarrollo (p. 563) no está
  entero en el extracto; el tema sólo lo nombra.
- Resolve nombra el clip capturado con el TC en cuadros («00086400.dpx» para 01:00:00:00): la cuenta
  corresponde a 24 cuadros por segundo; el tema cita el ejemplo sin hacer la cuenta.

Ficheros tocados: el tema 08 (nuevo), este informe, `fuentes/canal-sur/montador/web/lto-roadmap.txt`
(nuevo), `fuentes/canal-sur/montador/ebu/tech3293.txt` y `fuentes/canal-sur/montador/ccsds-650x0m3-oais.txt`
(texto extraído de los PDF). Borradores en el scratchpad de la sesión.

## Diez preguntas tipo test (comprobación antes de entregar)

Contestadas sólo con el tema: E = entera.

1. (Ingesta) La ingesta en directo de una señal de agencia es la crítica porque: a) es la más lenta ·
   b) es la única que no se puede repetir · c) exige transcodificar · d) no lleva metadatos. → b (§ 1,
   «Qué es la ingesta»; por eso se graba por partida doble). E
2. (Ingesta, práctica) Antes de copiar una tarjeta SD, lo primero es: a) formatearla en el ordenador ·
   b) copiar sólo los ficheros de vídeo · c) bloquearla contra escritura · d) renombrar los clips. → c
   (§ 1, paso 1; y se copia entera, paso 2). E
3. (Digitalización) En DaVinci Resolve, la captura desde cinta se guarda como: a) MXF OP1a o MP4 ·
   b) DPX o QuickTime · c) sólo ProRes · d) BWF. → b (§ 2, p. 561-562). E
4. (Digitalización, práctica) Para capturar varios tramos marcados de varias cintas y pasarlos juntos:
   a) *Capture Now* · b) registrar con *Log Clip* y capturar por lotes · c) *Clone Tool* ·
   d) exportar una EDL. → b (§ 2, tabla de métodos; y el nombre de cinta único). E
5. (Transferencia) Señale la correcta: a) en un NAS se piden bloques de disco · b) una SAN sirve
   ficheros por la red ofimática · c) en una SAN se pide un bloque de disco y da el caudal sostenido de
   la edición compartida · d) NAS y SAN sustituyen al RAID. → c (§ 3). E
6. (Transferencia, práctica) Un clip de 12 GB por una línea de 100 Mb/s tarda, como mínimo: a) 2 min ·
   b) 16 min · c) 160 min · d) 1 h 36 min. → b (§ 3, cálculo). E
7. (Verificación) Según el manual de Resolve, la suma de verificación por defecto y la más rápida son:
   a) CRC 32 y MD5 · b) MD5 y XXHASH64 · c) SHA 512 y File Size · d) SHA 256 y CRC 32. → b (§ 4,
   tabla de algoritmos; MD5 da 128 bits). E
8. (Copias de seguridad) Señale la correcta: a) el RAID 1 reparte sin redundancia · b) el RAID 5
   necesita tres discos como mínimo y aguanta la caída de uno · c) un RAID 6 es una copia de seguridad
   · d) la regla 3-2-1 pide tres copias en un mismo dispositivo. → b (§ 5, tablas RAID; 3-2-1 de INCIBE). E
9. (Metadatos) EBUCore, de la EBU, es: a) un códec de archivo · b) un conjunto de metadatos
   descriptivos y técnicos basado en el Dublin Core · c) el identificador único del MXF · d) una norma
   SMPTE retirada. → b (§ 6, Tech 3293 v. 1.10; la RP 210 es la retirada). E
10. (Archivo) En el modelo OAIS, el paquete que el productor entrega al archivo es: a) AIP · b) DIP ·
    c) SIP · d) PDI. → c (§ 7, tabla de paquetes). Y, de la misma rúbrica, la LTO-10 no es compatible
    hacia atrás (§ 7, tabla de compatibilidad). E

Rúbricas cubiertas: ingesta (1, 2), digitalización (3, 4), transferencia (5, 6), verificación (7),
copias de seguridad (8), metadatos (9), archivo (10); teoría (1, 3, 5, 7, 8, 9, 10) y aplicación
práctica (2, 4, 6). Las diez, enteras: no hizo falta ampliar.
