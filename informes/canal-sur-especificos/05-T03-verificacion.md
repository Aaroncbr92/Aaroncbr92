# Verificación · Ayudante de Realización (05) · Tema 3 · Preparación de programas y grabaciones

Fase 3. Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/03-preparacion-programas-grabaciones.md`.
Fecha de lectura de las fuentes: esta sesión. El encargo dice que hoy es 24-09-2026 y el reloj del sistema, 29/30-09-2026.
Las fechas de la portada y de «Trazabilidad» (24-09 y 29-09) se dejan como las puso el redactor.

## 1. Pasajes copiados: sólo se ha comprobado que son literales

Se han cotejado frase a frase (texto normalizado, sin negritas) contra `33-realizador-a/02`, `03`, `04`,
`realizacion/03`, `realizacion/13` y `realizacion-tv/19`.

- **Copiado del común (33-02, 33-03, 33-04)**: todos los pasajes que lista el informe de redacción son
  literales. Las únicas diferencias son los cambios declarados: la remisión «quedan fuera de este tema;
  el grafismo… tema 12», «Las comunicaciones del control se estudian en el tema 4» y «citado en «Antes
  del programa: realizador y ayudante»». La «Continuidad» de 33-04 acaba en el CR2.6. Lo que sigue en
  el tema (CR2.7, CR3.2 de UC0218_3 y RD 0904 RA 5.a y 5.b) es nuevo y se ha verificado (§ 2).
- **Copiado de RTVE sin cambios**: literal (cadena, cronograma, localización, selección de medios, lista
  de planos, departamentos y carra). Las frases de entrada nuevas («Por encima de esa cadena está el
  cronograma.», «Decidir los medios…», «El reparto de departamentos…») son declaradas y no dan datos.
- `negritas.py` sobre todas las fuentes da 201 negritas y 5 no encontradas, todas en pasajes copiados:
  tres rótulos en negrita de «Tres reglas obligatorias», una cita con elisión […] (RA 3.d, que sí está)
  y la definición del MOS. Esa definición sí está en `mos.txt`, pero el volcado la corta en «P rotocol».
  Las citas del Libro de Estilo salían como no encontradas por la ligadura «ﬁ» del volcado; cambiada la
  ligadura, aparecen todas.

## 2. Lo verificado en su fuente

- **IMS077_3** (INCUAL, `incual-IMS077_3.txt`). Coinciden con el texto la numeración y la página de cada
  cita nueva:
  - UC0216_3: CR1.1 y CR1.4 (p. 3), CR3.7 y CR4.7 (p. 4); «fondos documentales audiovisuales» (p. 5).
  - UC0217_3: RP1 y CR1.1 a CR1.8 (p. 7); CR2.5 a CR2.7, CR2.9 y CR3.1 a CR3.5 (p. 8).
  - UC0218_3: CR3.2, CR3.4 y «departamento de documentación y archivo» (p. 11).
  - MF0216_3: CE8.2 (p. 15).
  - MF0217_3: CE1.5 y CE1.9 (p. 18); CE2.1 (en C2) y CE3.3 (p. 19).
  - Ámbito profesional: «departamentos de redacción» y «siempre bajo las órdenes…» (p. 1).
  - Publicación: Orden PCI/797/2019.
- **RD 1680/2011** (`BOE-A-2011-19599.txt`). Coinciden con el BOE los RA y las letras citados:
  - 0903: RA 2.a y 2.b, RA 3.a y el contenido «Comunicación con el personal durante los ensayos…».
  - 0904: RA 2.g, 3.a, 3.c, 3.e, 5.a y 5.b, y los contenidos «Procedimientos de obtención…», «Técnicas
    de elaboración de la escaleta de continuidad» y «Comunicaciones y órdenes para la continuidad…».
  - Datos de la norma: BOE núm. 302, de 16-XII-2011, y los nombres de los módulos 0902 a 0905 y 0910.
  - **RD 500/2024** (de 21 de mayo): su art. 7 modifica el anexo I, pero sólo suprime FOL, EIE y FCT y
    añade módulos transversales. No toca 0902 a 0905 ni 0910, así que la afirmación del tema es correcta.
- **Convenio** (BOJA 240/2014, anexo III). El código, la página y el literal son correctos en las
  fichas del Realizador (5351000, p. 196), el Ayudante de Producción (5212705, p. 110), el Decorador
  (5333000, p. 123: «Localizar…» y «Controlar la construcción…»), el Ayudante de Decoración (5333100,
  p. 109), el Redactor (5212101, p. 198), el Documentalista (5213209, p. 124) y el Ayudante de Archivo
  y Documentación (5213213, p. 108; también el «Facilitar ,»).
- **Libro de Estilo**: 6.1 (la regla del cambio comunicado, citada en la aplicación práctica), 6.1.1 y
  6.1.2 (los textos del redactor), comprobados en `libro-de-estilo-333233b.txt`.
- **MOS**:
  - v4.0 (Document Revision 560, 7-VI-2019): «Insert example 1» y § 2.3, Profile 2, con sus tres citas.
  - v2.8.5: la jerarquía y «Items are sent…».
  - `moscur.txt`: las fechas de publicación.
- **Avid** (`avnews.txt`): «NRCS» y las dos citas.

## 3. Correcciones aplicadas

| Línea aprox. | Error | Antes → después |
|---|---|---|
| Siglas | 5 | Se quitan ODT y UM, que se presentaban y no se usaban. Se presenta MAM (con el texto de 33-04), que el pasaje copiado de 33-04 usaba sin presentar |
| 175 | 9 | «Las fuentes nombran esos dos momentos» → «El enunciado nombra…» |
| 290 | 9 | De dónde llega la escaleta a realización: se marca «(oficio)» porque ninguna fuente lo dice |
| 296 | 9 | «sitúa la revisión al principio del trabajo del ayudante» → «trata la escaleta en la primera realización profesional del ayudante (UC0216_3, RP1)», que es lo que dice la fuente |
| 587 | 6 | Teleprompter: se añade «si el programa lo necesita». CE1.5 lo condiciona así: «si el producto a realizar necesita de un teleprompter» |
| 666 | 3 | «Además de las vecinas…, tres tocan…»: una de las tres (Decorador) ya estaba entre las vecinas. Se nombran las fichas |
| 707 | 1/9 | La RA 3.a del módulo 0903 aparecía bajo «citaciones, de producción». Se aclara que está en el módulo de realización, dentro de la dirección de los ensayos (RA 3), y que el contenido es de ese mismo módulo |
| 850 | 3/6 | Versiones vigentes del MOS: la página «Current Versions» da tres (4.0, 2.8.5 y 3.8.4), no dos. Se añade la 3.8.4 con su literal. Trazabilidad actualizada |
| 909 y 924 | 6 | Las comprobaciones de CE8.2 son de C8 («Coordinar los ensayos…»). Se añade «durante los ensayos (MF0216_3, C8)» |
| 944 | 3 | «el archivo tiene dos fichas»: existe además la del J. Dpto. Archivo y Documentación (5213200, p. 135). Se menciona; añadida a Trazabilidad |
| 1022 | 9 | «el supuesto práctico típico» → «un supuesto práctico posible (no hay exámenes anteriores que digan cuál)» |
| 1037 | 9 | «Cuatro casos que se preguntan en una prueba práctica» → «Cuatro casos de oficio para practicar la prueba práctica» (no hay exámenes anteriores) |
| 1035 | 3 (coherencia) | «Víspera: plan de trabajo y orden de trabajo del día» contradecía el cuadro del epígrafe 3, donde el plan de trabajo se hace en preproducción. Pasa a «Orden de trabajo del día, sacada del plan de trabajo» |

Se han releído los pasajes cambiados: toda remisión («CR1.8», «RA 3», «C8», «ese módulo») tiene
delante su antecedente.

## 4. Lentes

- `negritas.py`: 201 cotejadas; 5 no encontradas, todas explicadas en § 1.
- `refutar_exactitud.py` y `refutar_modo.py` con el RD 1680/2011: 0 comprobadas y 0 hallazgos. El tema
  no cita artículos (cita RA y letras de un anexo), así que estas lentes no tienen dónde anclar. El
  cotejo de RA se hizo a mano (§ 2).
- `refutar_prosa.py`: 0 hallazgos.
- `indice.py`: 35 epígrafes. Los rótulos no cambian.

## 5. Sin resolver o para la refutación

- En los pasajes copiados de 33-02, los rótulos en negrita de «Tres reglas obligatorias» («Los cambios
  se comunican a todos», etc.) no son literales de la fuente. Son copia del común y no se han tocado.
  Si la refutación lo aplica a todo el temario, pasarían a redonda.
- Fechas: el tema declara lecturas del 29-09-2026 y el encargo fija hoy en el 24-09-2026. No se cambian.

## Ficheros tocados

El tema y este informe. (`02-guion-escaleta-documentacion.md` y `05-T02-verificacion.md` aparecen
modificados en git, pero no son de esta verificación.)
