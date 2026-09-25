# Productor/a (puesto 32) · Tema 2 · Redacción

Fase 2, redactar. Tema: `temas/canal-sur-especificos/32-productor-a/02-puesto-de-productor-a-en-rtva-csrtv.md`
(unas 7.700 palabras de cuerpo, 31 epígrafes). Fecha de trabajo y de lectura de todas las fuentes:
25-09-2026 («hoy» del encargo: 24-09-2026; las fuentes son las mismas en ambas fechas).

Ficheros tocados: el tema (nuevo, con su carpeta) y este informe. Un fichero auxiliar en el
scratchpad (el Libro de Estilo normalizado NFKC para pasar `negritas.py`), fuera del repositorio.
Aviso: corrí una vez `indice.py` sin argumentos por error; reescribe los temas del `.tsv` y del
directorio de esquemas, pero `git diff` no muestra ningún cambio en ficheros versionados.

## Avisos al coordinador (manda la fuente)

1. **Ninguno de los dos temas de RTVE está «sin actualizar».** En
   `informes/canal-sur-reuso/produccion-informacion.tsv`, la fila 32/2 lleva `actualizar = sí`. Por
   eso la lista «Copiado de RTVE sin cambios» queda vacía: lo tomado de RTVE va abajo como
   **adaptado**, para que la verificación lo compruebe. Además, al pasar a un tema de Canal Sur le
   he quitado las negritas (en RTVE la negrita es énfasis; aquí significa literal de fuente) y todas
   las referencias a preguntas de examen de RTVE.
2. **He usado una fuente que el material B no traía**: el *Libro de Estilo de Canal Sur Televisión*
   (2004), apartado 4.4 «Producción» (págs. 75-78), 4.1 y 8.1/8.3. Es el único documento publicado
   de la RTVA que describe el trabajo del productor en informativos y retransmisiones, que la ficha
   de 2014 no nombra. Leído directamente en `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`
   (l. 2224-2227, 2593-2744, 4039-4044, 4136-4141).
3. **También he leído en la fuente, fuera del material B**: el anexo VI de la convocatoria (fila de
   Productor/a, pág. 12371/91; el `.txt` rompe las columnas, así que la asignación a columnas la
   saqué de la tabla del PDF con PyMuPDF), la ficha del Realizador (5351000, pág. 196) y la
   redacción de los arts. 17, 19, 21, 26 y 27 de la Ley 18/2007 (`.redacciones.tsv`: una sola
   redacción, la original).
4. Dos citas literales del Libro de Estilo cruzan un salto de página del `.txt` (4.4.1 «La
   organización diaria…» y 4.4.4 «Cualquier gestión…»), y `negritas.py` las da como «NO ESTÁ»; las
   he comprobado a mano y son literales. El resto de las citas del Libro sólo fallan por las
   ligaduras «ﬁ»/«ﬂ»: con el texto normalizado NFKC, `negritas.py` las encuentra.

## Copiado del común (no se re-verifica)

Literal, sin cambiar una palabra; sólo pongo encima mi propio `###`:

| Pasaje en el tema 32-T02 | Origen literal |
|---|---|
| «Quién es la empresa: la RTVA y su sociedad filial»: los tres párrafos del cuerpo («El convenio se firmó…» hasta «…plural del título.») | `temas/canal-sur-comun/07-x-convenio-colectivo.md`, «Las partes: de dos sociedades filiales a una», entero. Delante he añadido una frase mía que presenta el informe de la Cámara, porque el pasaje copiado dice «informe citado»; detrás, un párrafo mío de aplicación |
| «Dónde están definidas sus funciones»: primer párrafo («Fichas de puesto (a las que remite la DA 8.ª)…») | `07`, «Anexo III. Definición de funciones», entero |
| «Grupo, nivel y plantilla»: primer párrafo y lista B01-B05 | `07`, «Artículo 45. Clasificación profesional», entero |
| «Dónde se inserta»: los cuatro guiones del art. 9, estatutos, 19.2.e/f/g y 17.1.d/e/f | `temas/canal-sur-comun/05-ley-18-2007-rtva.md`, «La organización de CSRTV», los cuatro guiones |
| «El marco que la ley fija a esos recursos»: los tres guiones de «Personal (artículo 27):», el guion del 21.2 y el guion de contratación (26 y 19.2.e) | `05`, «Régimen económico, patrimonio, contratación y personal», guiones correspondientes. Los rótulos «Presupuesto:» y «Contratación:» son míos |
| «Medios propios o ajenos»: guion «*Art. 24. Producción propia de programas audiovisuales.*…» | `temas/canal-sur-comun/06-carta-servicio-publico-y-estatuto-profesional.md`, repaso del articulado, guion del art. 24, entero |

## Copiado de otro puesto ya cerrado (Redactor/a, tema 3)

No figura en la lista de «ya cerrado» del encargo, así que decide el verificador si lo salta:

| Pasaje en el tema 32-T02 | Origen |
|---|---|
| «En informativos: productores y editores»: «La producción trabaja en paralelo con la edición:» y los tres guiones | `temas/canal-sur-especificos/34-redactor-a/03-organizacion-redaccion-audiovisual.md`, «Productores y editores», literal |
| «Retransmisiones y directos»: los dos párrafos sobre 8.1 punto 6 y 8.3 | Mismo tema, «Directos», **adaptado** (recortado); las dos citas las he cotejado en el Libro |

## Copiado de RTVE sin cambios

Ninguno (véase el aviso 1: la fila 32/2 está marcada `actualizar = sí`).

## Tomado de RTVE y adaptado (se verifica)

Todo va en el tema como oficio, «práctica de sector», sin norma detrás:

| Pasaje en el tema 32-T02 | Origen y cambios |
|---|---|
| Tabla «Puesto / Qué hace» (ocho filas) | `temas/produccion/05-equipos-humanos.md` §2: las palabras son las mismas; quitadas las negritas |
| «El productor responde de los medios y el dinero; el director, del resultado artístico. Cuando…» | §2: quitado «La distinción que más se pregunta es…»; «de el» corregido a «del» |
| Las dos acepciones de productor ejecutivo | §3: quitados «Y una precisión…» y «que la respuesta oficial recoge» |
| Los cuatro pasos para convocar y el «error más caro» | §7: «Contratar» pasa a «Contratar o asignar»; quitadas las remisiones a los temas 1 y 14 de RTVE y los seguros |
| Tabla editor / productor ejecutivo | `temas/realizacion-tv/10-funciones-del-realizador.md` §5: las palabras son las mismas; quitadas las negritas |
| Regla «el realizador manda sobre CÓMO se ve…», dos celdas de la tabla del §1 y «ANTES / DURANTE» del §2 | §1 y §2, recortados y sin negritas |

Descartado por propio de RTVE o sin fuente: las preguntas y respuestas oficiales del examen de RTVE,
la referencia al III Convenio de RTVE, el operativo de la señal institucional de TVE (§7, sostenido
sólo por la plantilla del examen), el *showrunner*, el regidor y el *gaffer*.

## Redactado nuevo con fuente propia de la RTVA (se verifica)

Ficha de Productor/a (l. 6916-6947 del `.txt` del convenio) y las fichas vecinas (Ayudante de
producción, Realizador, Coordinador de programas, productores musicales, Presentador productor de
radio, Editor de continuidad); la tabla del art. 45 (l. 1426-1541); la dotación del anexo II y sus
sumas (44 y 50); las plazas del anexo I (14); el anexo VI; el organigrama de 2018 (Cámara, anexo
9.2.2, l. 10455-10503); el punto 42 del contrato-programa; todo el Libro de Estilo; las tablas de
recursos y de reparto productor/ayudante (se construyen citando las fichas).

## Lentes automáticas

- `indice.py`: índice generado.
- `refutar_prosa.py`: sin relleno ni negritas rotas. Da como siglas sin presentar CSTV/CSR (se
  presentan en la frase «llama **CSTV** a…», como en el común 07), RTVA (en el título, como en todos
  los temas) y RL/DATOS (dentro de la cita literal del anexo VI; RL se presenta en las siglas).
- `negritas.py` con las ocho fuentes (Libro normalizado): 188 negritas cotejadas; de las 20 que no
  encuentra, 18 son rótulos de convención (enunciado, «Qué se puede preguntar», «Lo que este tema
  no da», «Oficio sin norma detrás») y 2 son las citas que cruzan página (aviso 4).

## Preguntas tipo test para comprobar la cobertura (10)

Cada una, con la rúbrica del enunciado y el pasaje del tema que la contesta. Las diez se contestan
enteras con el tema.

1. **(Puesto)** Según el anexo III del X Convenio, el objeto o función básica del puesto de
   Productor/a es: a) dirigir la realización de los programas; b) diseñar, ejecutar y evaluar el
   plan de producción y el presupuesto para la organización y gestión de los medios técnicos y
   humanos necesarios para los programas; c) realizar la producción ejecutiva de las coproducciones;
   d) coordinar la emisión de los programas en directo. → b). «La ficha de Productor/a». **Entera.**
2. **(Puesto)** El Productor/a y el Ayudante de producción están, en el art. 45 del convenio, en los
   niveles: a) B02 y B03; b) B03 y B03; c) B03 y B04; d) B02 y B04. → c). «Grupo, nivel y
   plantilla». **Entera.**
3. **(Puesto)** En la RTVA, la «producción ejecutiva» de las coproducciones es tarea, según el
   anexo III, del: a) Productor/a; b) Coordinador de programas; c) Realizador; d) Ayudante de
   producción. → b). «El productor entre los puestos vecinos». **Entera.**
4. **(Puesto)** La titulación específica exigida para acceder al puesto de Productor/a en la
   convocatoria de 2026 es: a) Técnico Superior de la rama de Imagen y Sonido; b) Grado en
   Comunicación Audiovisual o Grado en Periodismo; c) cualquier grado con 12 meses de experiencia;
   d) grado más máster oficial. → b); las otras tres son la titulación opcional, que sólo cuenta en
   promoción interna. «Grupo, nivel y plantilla», anexo VI. **Entera.**
5. **(Planificación · retransmisiones)** Según el anexo III, el plan de transmisiones con cuyas
   instrucciones se coordina la recepción de señales lo diseña: a) el Editor de continuidad; b) el
   Realizador; c) el Productor; d) el Ayudante de producción. → c). «Lo que planifica el
   Productor/a» y «Retransmisiones y directos». **Entera.**
6. **(Coordinación)** La ficha del Productor/a dice que la previsión de medios humanos y materiales
   de un programa se hace: a) en coordinación con el director y/o el realizador; b) por orden de la
   Dirección Técnica; c) con el Ayudante de producción; d) en la Mesa de Contratación. → a).
   «Planificación» y «Coordinación». **Entera.**
7. **(Control · informativos)** Según el Libro de Estilo, cuando entre la obligación informativa y
   el coste las posturas no puedan armonizarse, decide: a) el productor; b) el editor; c) la
   Dirección de los Servicios Informativos; d) la Dirección de Producción. → c). «En informativos:
   productores y editores» y «El control del gasto en informativos». **Entera.**
8. **(Control · recursos económicos)** Según el Libro de Estilo, cualquier gestión que lleve
   aparejado un gasto o un compromiso ante proveedores ajenos sólo podrá ejecutarse a través del:
   a) Departamento de Producción; b) editor; c) Gabinete Jurídico; d) realizador. → a). «El control
   del gasto en informativos». **Entera.**
9. **(Recursos · contratación)** El órgano de contratación de la RTVA y de sus sociedades filiales
   es, según la Ley 18/2007: a) el Consejo de Administración; b) el Productor/a del programa; c) la
   Dirección General, sin perjuicio de lo que dispongan los estatutos de las filiales; d) la Mesa de
   Contratación. → c) (art. 19.2.e). «El marco que la ley fija a esos recursos». **Entera.**
10. **(Aplicación práctica · recursos humanos)** Un productor cita para la misma grabación, a la
    misma hora, al iluminador y al cámara. Según el Libro de Estilo: a) es lo correcto, para que el
    equipo llegue junto; b) es un error, porque hasta que el iluminador no termine su tarea no se
    puede iniciar la siguiente fase; c) es indiferente; d) lo decide el realizador. → b) (4.4.2).
    «Convocar al equipo por fases». **Entera.** Variante que también contesta: quién efectúa las
    citaciones y controla las dietas del equipo (el Ayudante de producción, bajo la organización del
    productor).

Reparto: puesto (1-4), planificación (5, 6), coordinación (6, 10), control (7, 8), recursos (8-10),
informativos (7, 8), retransmisiones (5), aplicación práctica (10). Los contenidos audiovisuales
(web, redes, *streaming*) no dan pregunta con fuente propia de la RTVA en este tema: se declara en
«Contenidos audiovisuales» y en «Lo que este tema no da», con remisión a los temas 1 y 9.
