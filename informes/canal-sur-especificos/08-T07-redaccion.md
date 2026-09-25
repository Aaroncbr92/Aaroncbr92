# Puesto 08 · Tema 7 · Fase 2 · Redacción

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/08-camara-operador/07-formatos-codecs-tarjetas-ingesta-entrega.md`.
Se escribe por partes, guardando cada epígrafe.

## Fuentes leídas (todas el 24-09-2026)

- `08-investigacion-C-sonido-formatos.md` § Tema 7 y «Lo que no se pudo confirmar».
- RTVE: `temas/informacion-grafica/03-la-camara-y-el-sensor.md`, `temas/edicion-montaje/05-soportes-formatos-e-ingesta.md`,
  `temas/realizacion-tv/12-formatos-y-procesos-de-registro.md`.
- Citas releídas por mí en su copia local antes de escribirlas: Sony PXW-Z200 Help Guide (pp. 67-68, 95-99, 153,
  160-161, 196, 251-252, 310, 336); Sony ILCE-1 Help Guide (extractos: formatos, notas de tarjeta); Sony ILCE-7SM3
  «Characteristics of each file format»; LOC fdd000389 (ProRes 422) y fdd000013 (MXF); Avid DNxHD white paper 2012;
  Panasonic AVC-Intra FAQ; DPC «Fixity and checksums»; UIT-R BT.2020-2 (cuadro 1) y BT.709-6 (2.2, 2.4);
  *Libro de estilo de Canal Sur* 2004 (5.3.3, pp. 81-82; 9.9.1).
- Releídas con WebFetch el 24-09-2026: INCIBE, «Definiendo mi estrategia de copias de seguridad» (29-09-2021), la
  frase de la regla 3-2-1 coincide con la de la investigación; SD Association, «Speed Class», las tres frases de clases
  coinciden; la página no da cifras en MB/s.

## Progreso
- Cabecera, siglas, enunciado y «Qué se puede preguntar» guardados.
- Epígrafe «Formatos de grabación» guardado.
- Epígrafe «Códecs» guardado.
- Epígrafe «Tarjetas» guardado.
- Epígrafe «Metadatos» guardado.
- Epígrafes «Ingesta» y «Copia de seguridad» guardados.
- Epígrafe «Entrega de material», documentos, huecos y trazabilidad guardados.
- Índice generado con `herramientas/indice.py` (el tema no está en `portadas.tsv`: sólo toca el índice).
- `refutar_prosa.py`: siglas sin presentar corregidas (PCM, PSNR, SD, USB, VPG; LT/HQ/XQ y modelos declarados como
  rótulos). Negritas no literales (rótulos de listas) pasadas a redonda.
- Cotejo propio de negritas «…» contra las copias locales: todas casan salvo SDA e INCIBE (web, releídas con
  WebFetch). Corregidas dos citas que no eran literales (lista de formatos de la Z200, que unía líneas con «·»; la
  frase de la EBU R 122 de la ficha LOC).
- Extensión final: unas 10.800 palabras de cuerpo (el enunciado tiene siete rúbricas).

## Copiado del común

Ninguno. El temario común de Canal Sur no tiene materia técnica de formatos; ningún epígrafe se ha copiado
literal de un tema cerrado de Canal Sur. (Tampoco se ha copiado de los temas 1-15 de este puesto, que no están
cerrados; se remite a ellos: tema 9 para compresión y tasas EBU, 6 sonido, 11 equipo, 12 derechos, 13 envío,
15 cámara lenta y multicámara; tema 10 del común para protección de datos.)

## Copiado de RTVE sin cambios

Ninguno literal sin tocar: todo lo tomado de RTVE se ha adaptado (fuera las respuestas oficiales, números de
pregunta, opciones falsas y negritas de énfasis; negrita sólo para citas literales). Pasa por verificación.

## Adaptado de RTVE (verificar)

| Pasaje del tema | Origen RTVE | Qué se cambió |
|---|---|---|
| Formatos › De la cinta al fichero (ventajas del XDCAM) | edicion-montaje/05 § 5 | Sin preguntas de menú ni capacidad del disco; sin «volcar mientras se graba» |
| Formatos › Esencia, códec, contenedor… (tabla) | edicion-montaje/05 § 1 | Añadido H.265; «o junto a él» en metadatos |
| Formatos › Qué define un formato (UHD/DCI, 29,97, muestreo) | realizacion-tv/12 §§ 1, 3, 4 | Resoluciones HD/UHD pasadas a UIT-R BT.709/BT.2020 leídas; DCI declarado oficio |
| Formatos › Los contenedores (tabla de autores, MXF contenedor, patrones) | realizacion-tv/12 § 6; edicion-montaje/05 § 3 | **Corrección**: RTVE daba OP-Atom sólo como «entorno de Avid»; la ficha LOC y el FAQ de Panasonic lo dan también en cámaras P2. Normas ST 378/390 añadidas |
| Formatos › Los formatos de proyecto | edicion-montaje/05 § 2 | Sin la pregunta 14 |
| Formatos › El *proxy* | realizacion-tv/12 § 7; informacion-grafica/03 § 7 | Añadidos datos Z200 |
| Formatos › La tasa y la capacidad (regla) | edicion-montaje/05 § 5 | Ejemplos de cálculo nuevos |
| Códecs › Qué es un códec (DCT, audio PCM sin comprimir) | realizacion-tv/12 § 5; edicion-montaje/05 § 6 | Resumido |
| Tarjetas › Los soportes de estado sólido (SxS, P2, XDCAM) | realizacion-tv/12 § 10 | Sin «SWS»; P2 con OP-Atom (FAQ) |
| Metadatos › El código de tiempo (LTC/VITC, 80 bits, DF) | realizacion-tv/12 §§ 3, 8 | Sin el reparto de bits (RTVE lo daba sin norma leída); 32 bits de usuario casan con las 8 cifras hex de la Z200 |
| Metadatos › La aritmética del código de tiempo | realizacion-tv/12 § 9 | Sin la pregunta 4 |
| Ingesta › Qué es la ingesta (tres formas) | edicion-montaje/05 § 8 | Sin el sistema comercial ni la pregunta 23 |
| Copia › RAID | realizacion-tv/12 § 12 | Añadido que RAID 0 no protege y que no protege de corrupción |
| Copia › LTO | edicion-montaje/05 § 7 | Sin la pregunta 21 |

Del tema RTVE informacion-grafica/03 no se toma nada más: sus epígrafes de sensor ya están en el tema 1, y los de
menú (Picture Cache, Access Point, dos cámaras) se sustituyen por la Z200 leída.

## Ficheros tocados

Sólo el tema 7 y este informe. Ninguna fuente modificada.

## Preguntas tipo test de control (10)

Contestadas sólo con el tema. Resultado: las diez, enteras.

1. **(Formatos)** MXF es: a) un códec intracuadro de la SMPTE; b) un contenedor; c) un formato de proyecto como
   AAF; d) un perfil de H.264. → b. Tema: «Los contenedores» (no dice nada de cómo está comprimido; ST 377-1). **Entera.**
2. **(Formatos, práctica)** ¿Cuántos minutos nominales caben en una tarjeta de 128 GB a 200 Mb/s? a) unos 21;
   b) unos 34; c) unos 85; d) unos 170. → c. Tema: «La tasa y la capacidad» (cuenta desarrollada). **Entera.**
3. **(Formatos)** Resolución del UHD de televisión según UIT-R BT.2020: a) 4.096 × 2.160; b) 3.840 × 2.160, 16:9;
   c) 3.840 × 2.160, 17:9; d) 7.680 × 4.800. → b. Tema: «Qué define un formato de grabación». **Entera.**
4. **(Códecs)** ¿Qué compresión es más adecuada para editar y aguanta mejor el movimiento? a) GOP largo;
   b) intracuadro; c) H.265 en GOP largo; d) ninguna diferencia. → b. Tema: «Intracuadro y GOP largo» (Sony y
   Panasonic). **Entera.**
5. **(Códecs)** ¿Con qué norma SMPTE se codificó Avid DNxHD? a) ST 377-1; b) VC-3; c) RDD 36; d) ST 390. → b.
   Tema: «Avid DNxHD (SMPTE VC-3)»; los distractores (MXF, ProRes, OP-Atom) también están en el tema. **Entera.**
6. **(Tarjetas)** En una tarjeta SD, el número de la clase de velocidad (p. ej. V30) indica: a) la capacidad;
   b) la velocidad mínima de escritura; c) la velocidad máxima de lectura; d) la generación. → b. Tema: «Las
   clases de velocidad». **Entera.**
7. **(Tarjetas, práctica)** Un ordenador pide formatear una tarjeta recién grabada al conectarla: a) aceptar;
   b) aceptar y copiar después; c) no formatear nunca en respuesta a ese aviso; d) formatear en modo rápido. → c.
   Tema: «Formatear», regla 2 (ILCE-1), y regla de oficio de copia comprobada. **Entera.**
8. **(Metadatos, práctica)** A 25 fps, duración de 00:47:17:23 a 01:23:54:00 (exclusiva): a) 00:35:36:01;
   b) 00:36:36:02; c) 00:36:42:01; d) 00:35:35:00. → b. Tema: «La aritmética del código de tiempo». **Entera.**
   (Variante: modo que corre aunque no se grabe → Free Run; bits de usuario → 8 cifras hexadecimales: en el tema.)
9. **(Ingesta y copia)** Según la Digital Preservation Coalition, para detectar daños accidentales en ficheros
   basta: a) SHA-256; b) MD5; c) comparar tamaños; d) un RAID 1. → b. Tema: «La copia comprobada»; el RAID y la
   comparación de tamaños, descartados en el tema. **Entera.** (Variante: regla 3-2-1 → tres copias, dos
   dispositivos, una en otro lugar: en el tema.)
10. **(Entrega)** ¿Por qué no se envía material por FTP sin cifrar? a) es más lento; b) contenido, usuario y
    contraseña van sin cifrar; c) no admite MXF; d) no admite *proxy*. → b. Tema: «El envío por red» (Z200,
    p. 196). **Entera.**

Cobertura por rúbrica del enunciado: formatos (1-3), códecs (4-5), tarjetas (6-7), metadatos (8), ingesta y copia
(9), entrega (10). No hizo falta ampliar el tema.
