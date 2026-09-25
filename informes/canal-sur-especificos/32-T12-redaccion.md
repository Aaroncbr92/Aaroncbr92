# Productor/a (puesto 32) · Tema 12 · Fase 2, redactar

Tema: `temas/canal-sur-especificos/32-productor-a/12-gestion-documental-y-trazabilidad.md`
(12.691 palabras de cuerpo según `indice.py`; 8 rúbricas del enunciado en su orden, más aplicación
práctica; 50 epígrafes). «Hoy» del encargo: 24-09-2026. Fecha de trabajo y de lectura de todas las
fuentes: 25-09-2026; ninguno de los preceptos citados tiene redacción con vigencia entre el 24 y el
25-09-2026 (cadenas de `boe.py` comprobadas).

Ficheros tocados: el tema (nuevo) y este informe. En el scratchpad, fuera del repositorio: volcados
de la Ley 7/2011 (BOE-A-2011-18654) y de la Ley 39/2015 (BOE-A-2015-10565), el Libro de estilo
normalizado NFKC y dos JSON de extracción de pasajes literales. `indice.py` se corrió una vez sin
argumentos por error: recorre los temas de `portadas.tsv` y los reescribe idénticos; `git status` no
muestra ningún fichero rastreado modificado. Después se corrió sólo sobre este tema.

## Avisos al coordinador (manda la fuente)

1. **Ley 39/2015 ≠ BOE-A-2015-10566.** El volcado local `BOE-A-2015-10566.md` es la Ley 40/2015; la
   39/2015 es BOE-A-2015-10565, que no estaba en `fuentes/canal-sur/` (leída con `boe.py` en línea).
2. **Art. 70 de la Ley 39/2015 y la CCA.** La CCA (punto 103) aplica el art. 70 a los expedientes de
   RTVA y CSRTV; por el art. 2.2 de la Ley 39/2015 y el 52 de la Ley 9/2007, la RTVA (agencia, persona
   jurídica pública) está en el 2.2.a; CSRTV (sociedad mercantil) en el 2.2.b, sólo para preceptos que
   se le refieran o ejercicio de potestades. El tema lo dice así y presenta el uso de la CCA como
   criterio del órgano de control, no como aplicación directa a CSRTV.
3. **Art. 70.4 frente a la recomendación 300 de la CCA**: la ley excluye del expediente la
   información auxiliar o de apoyo; la CCA recomienda incluirla «de forma complementaria». El tema
   señala la diferencia (trampa de test posible).
4. **Ley 7/2011 y la RTVA**: la ley no nombra a la RTVA ni a CSRTV. El tema deduce que encajan en el
   art. 9.2.d (entidades instrumentales, art. 50.1 y 52 de la Ley 9/2007) y lo declara como lectura,
   no como regla confirmada.
5. **ET 34.9**: el apartado entró en vigor el 13-03-2019 (comprobado con `--fecha 20190310`, ausente,
   y `--fecha 20190314`, presente); el artículo 34 tiene redacción posterior (30-06-2023) por otro
   apartado. El tema fecha el apartado, no el artículo.
6. **Orden de 16-12-1987 (partes de accidente)**: el BOE no la consolida y sólo hay texto original;
   por eso el tema no da los plazos de notificación (cinco días hábiles, veinticuatro horas) aunque
   figuren en ese texto: no se puede asegurar que sigan vigentes. Sólo cita los artículos 1 y 3 de la
   Orden TAS/2926/2002 (consolidada) y remite a los temas 14 y 15.
7. **Fuentes nuevas no traídas por la investigación**: Ley 7/2011; Ley 9/2007 (arts. 50 y 52); Ley
   39/2015 (arts. 2, 17, 26, 70); LCSP (36, 63, 116, 153, 317, 318, 335, 346); Ley 1/2014 (3 y 15); ET
   (34.9, 35.5); Orden TAS/2926/2002; fichas del convenio de Jefe de Departamento de Archivo y
   Documentación, de Servicios Generales y de Ayudante de unidades móviles; Libro de estilo 4.4.4
   (puntos 1, 4, 6, 9) y 9.9.1; CP cláusula octava, puntos 8 y 9; CCA puntos 41, 52 y alegación nº 19.
8. **La investigación decía** que no había modelo publicado de cierre de producción: confirmado; el
   cierre y la memoria van como oficio, apoyados en la ficha, en la recomendación 300 y en los arts.
   12.3 y 13.3 de la Ley 7/2011.

## Copiado del común

Literal, sin re-verificar (temas cerrados de Canal Sur):

| Pasaje en el tema 12 | Origen |
|---|---|
| «Los documentos de la RTVA son documentos públicos»: desde «La que hasta entonces era la Empresa Pública…» hasta «…es una Agencia Pública Empresarial**»» (dos frases) | `temas/canal-sur-comun/05-ley-18-2007-rtva.md`, viñeta «Cambió la forma jurídica de la entidad» (sin el rótulo inicial) |
| «Dónde queda constancia pública del contrato»: viñeta «Cámara de Cuentas: el Estatuto la define…» entera, hasta «(artículo 4.1).» | `temas/canal-sur-comun/05-ley-18-2007-rtva.md`, control externo |
| «El consentimiento que hay que poder demostrar»: párrafo «*Las condiciones del consentimiento (artículo 7 del Reglamento).*…» | `temas/canal-sur-comun/10-proteccion-de-datos.md`, «Cuándo es lícito tratar datos» |
| Mismo epígrafe: viñetas «Artículo 2.2…» y «Artículo 3, el consentimiento de los menores…» | `10-proteccion-de-datos.md`, «Honor, intimidad y propia imagen» |
| «Autorizaciones de menores y otras reglas del tratamiento»: cabecera y cinco filas de la tabla (recoger el consentimiento; mayor de catorce; menor de catorce; imagen y voz de un menor; productora encargada del tratamiento) | `10-proteccion-de-datos.md`, «Qué le toca a una producción de radio o televisión» |
| «Conservar lo necesario, y no más»: cabecera y filas 5.1.b), 5.1.e) y 5.2 de la tabla de principios | `10-proteccion-de-datos.md`, «Los principios» |
| «El archivo audiovisual como destino»: línea «m) «**Velar por la conservación…**»» | `05-ley-18-2007-rtva.md`, «Los quince mandatos de la programación (artículo 4.3)» |
| Mismo epígrafe: viñeta «**Archivos de la RTVA (artículo 20.2)**…» | `temas/canal-sur-comun/04-ley-13-2022-y-ley-10-2018.md` |
| Mismo epígrafe: viñeta «*Art. 27. Archivo y patrimonio audiovisual de la RTVA.*…» | `temas/canal-sur-comun/06-carta-servicio-publico-y-estatuto-profesional.md` |
| «Entregar el material con sus datos»: párrafo «Metadatos son los datos sobre el material…» | `temas/canal-sur-especificos/08-camara-operador/07-formatos-codecs-tarjetas-ingesta-entrega.md`, «Qué son y quién los pone» (tema cerrado, con `08-T07-final.md`) |
| Mismo epígrafe: párrafo «El Libro de estilo de Canal Sur lo trata como un pacto: …la referencia a la cinta es de 2004.» (precedido de una frase puente mía, «El dato que enlaza cada plano… es el código de tiempo.») | `08-camara-operador/07-…`, «El código de tiempo» |

## Copiado de RTVE sin cambios

Fila 32/12 de `informes/canal-sur-reuso/produccion-informacion.tsv`: `actualizar = no`. Literales palabra
por palabra, sólo sin negritas (en RTVE son énfasis; en Canal Sur la negrita significa literal de
fuente), igual que en el tema 3:

| Pasaje en el tema 12 | Origen |
|---|---|
| «El parte de trabajo»: de «Y es coherente con lo que un parte es…» a «…qué hay que rehacer del plan de mañana.» | `temas/produccion-asistencia/06-plan-y-orden-de-trabajo.md` §5, segundo párrafo |
| «El parte de producción y la hoja de script»: «Es el papel que lleva la persona de continuidad —el *script*— … sin saber qué mira.» | `produccion-asistencia/06` §4, segundo párrafo |
| Mismo epígrafe: «La regla que los separa: el *storyboard* dibuja… el parte cuenta cómo fue el día.» | `produccion-asistencia/06` §4, último párrafo |
| «La orden de trabajo diaria»: bloque entero, de «La orden de trabajo diaria convierte…» a «…porque el plan cambia todos los días.» | `temas/produccion/01-la-produccion.md` §7 |
| «La cadena de documentos»: tabla Documento/Cuándo/Qué dice (seis filas) | `produccion-asistencia/06` §1 |
| Mismo epígrafe: «La regla que ordena las tres últimas…» | `produccion-asistencia/06` §1 |
| Mismo epígrafe: «Cada documento se hace con el anterior delante…» | `produccion/01` §4, último párrafo |

## Tomado de RTVE y adaptado (se verifica)

| Pasaje en el tema 12 | Origen y cambio |
|---|---|
| «El parte de trabajo»: «El parte de trabajo se entrega al finalizar la jornada.» | `produccion-asistencia/06` §5: era «La respuesta oficial: al finalizar la jornada de trabajo» |
| Mismo epígrafe: «El parte es diario, no de fase: …» y «De los seis papeles, sólo dos son diarios…» | §5: quitados los distractores del examen y «La regla que cierra el tema:» |
| «El parte de producción y la hoja de script»: tabla de tres documentos | §4: cabecera «Opción falsa» → «Documento»; *storyboard* en cursiva; sin negritas |
| Mismo epígrafe: «La hoja de script es la que anota los datos de los archivos…» | §4, primer párrafo: quitado «La respuesta oficial» |

Descartado por propio de RTVE o del examen de RTVE: las preguntas y plantillas oficiales, los
distractores del PERT, el III Convenio de RTVE, el plan de trabajo y su criterio de ordenación (en el
tema 3 de este puesto) y los cuatro cometidos de la producción.

## Redactado nuevo con fuente (se verifica)

- Ley 7/2011: arts. 2 (a, g, h, i, j, m), 3.1.a, 9.2.d, 10.1, 12, 13.3, 15.1.a, 53, 54, 57.b.
- Ley 9/2007: arts. 50.1 y 52 (1, 2, 3).
- Ley 39/2015: arts. 2, 17, 26.2, 70.
- LCSP: arts. 36.1, 63 (1, 3, 4, 7, 8), 116, 118, 153 (1, 2, 3, 6), 317, 318.a, 335, 346.
- Ley 1/2014: arts. 3.1.c e i, 15.a.
- ET: arts. 34.9, 35.5. Orden TAS/2926/2002: arts. 1 y 3.
- X Convenio: fichas de Productor/a (l. 6921-6944 del `.txt`), Ayudante de producción (l. 4690-4712),
  J. Dpto. Archivo y Documentación (l. 5357-5376), J. Dpto. Servicios Generales (l. 5575-5602),
  Ayudante de unidades móviles (l. 4752-4766); parte de baja (l. 1277).
- Libro de estilo: 4.4 (l. 2606-2623), 4.4.4 puntos 1, 4, 6 y 9 (l. 2668-2735), 9.9.1 (l. 6241-6247).
- CP: cláusula octava, puntos 8 y 9 (l. 3025-3035).
- CCA: puntos 41, 46-52, 103; recomendación 300; alegación nº 19 (l. 17674-17760).

## Lentes automáticas (25-09-2026)

- `refutar_prosa.py`: 2 hallazgos de siglas. SSFF, presentada después en las siglas de entrada;
  TAS es parte del nombre oficial de la orden (falso positivo). 0 de relleno, repeticiones o negritas
  rotas.
- `indice.py`: índice generado; portada escrita a mano intacta (el tema no está en `portadas.tsv`).
- `negritas.py` (Ley 7/2011, extracto de la Ley 39/2015, LCSP, Ley 1/2014, ET, Ley 9/2007, Orden
  TAS/2926/2002, convenio, Libro de estilo NFKC, CCA, CP): 166 negritas; 24 «no están»: 3 rótulos de
  plantilla y 21 de pasajes copiados del común cuyas fuentes (Estatuto, Ley 1/1988, RGPD, LO 1/1982,
  Ley 18/2007, Ley 10/2018, Carta) no se pasaron porque lo copiado no se re-verifica; 8 «atribuidas a
  otro artículo», todas falsos positivos (siete citas del art. 116 cuyo texto menciona el art. 28, y
  el 34.9 del ET seguido de la cita del 35.5). 0 errores reales.

## Oficio (declarado en el tema)

Concepto de trazabilidad; tabla de cualidades aplicadas a producción; mapa documental; índice del
expediente de producción; permiso frente a autorización; registro de permisos; contenido del parte;
reglas de versiones de la orden; rastro documental de la ejecución del contrato; informes de
seguimiento e incidencias; lista de cierre; ficha de entrega del material; contenido de la memoria;
supuesto práctico.

## Preguntas tipo test de comprobación

Diez preguntas que podría poner el tribunal, repartidas por las ocho rúbricas; 3, 7 y 8 son de
aplicación práctica. Todas se contestan enteras con el tema; no ha hecho falta ampliar.

1. **(Gestión documental; teoría)** Según la Ley 7/2011, de Documentos, Archivos y Patrimonio
   Documental de Andalucía, son funciones de la gestión documental: a) la identificación, la
   valoración, la organización, la descripción, la conservación, la custodia, el acceso y el
   servicio ✔; b) sólo la conservación y la custodia; c) la producción, la firma y el registro;
   d) la digitalización y la destrucción. → «Qué es gestión documental y qué es trazabilidad»
   (art. 54.1). **Entera.**
2. **(Expedientes; teoría)** Conforme al artículo 70.4 de la Ley 39/2015, no forma parte del
   expediente administrativo: a) el índice numerado; b) las notas, borradores y opiniones ✔; c) los
   informes preceptivos solicitados antes de la resolución; d) la copia electrónica certificada de
   la resolución. → «Qué es un expediente». **Entera.**
3. **(Expedientes; práctica)** El expediente de un contrato menor de servicios de 9.000 euros sólo
   contiene la orden de pedido y la factura. Para cumplir el artículo 118 de la LCSP le falta:
   a) el pliego de prescripciones técnicas; b) el informe motivado del órgano de contratación sobre
   la necesidad y la no alteración del objeto, y la aprobación del gasto ✔; c) la formalización en
   documento administrativo; d) nada, basta con pedido y factura. Y la Cámara halló en 2018 ese
   defecto en el 97,92 % de los expedientes menores analizados. → «El expediente de contratación»,
   «Lo que la Cámara de Cuentas encontró en 2018». **Entera.**
4. **(Contratos)** Salvo los contratos menores y los basados en acuerdos marco o sistemas dinámicos,
   los contratos de los poderes adjudicadores se perfeccionan: a) con la adjudicación; b) con la
   formalización ✔; c) con la recepción; d) con el pago. ¿Puede empezar su ejecución antes? No,
   salvo emergencia (art. 153.6). → «Cuándo existe el contrato». **Entera.**
5. **(Informes)** En los contratos de servicios, el expediente de contratación debe justificar:
   a) el informe de insuficiencia de medios ✔; b) el informe del comité de antena; c) la memoria del
   programa; d) el parte de trabajo. Ese informe se publica en el perfil de contratante (art. 63.3.a).
   → «El expediente de contratación», «Los informes que exige la contratación». **Entera.**
6. **(Permisos)** Según el Libro de estilo de Canal Sur, las localizaciones, asistencias externas,
   permisos, seguros y acreditaciones: a) las gestiona cada periodista; b) serán canalizadas siempre
   a través de los productores ✔; c) las tramita el Departamento Jurídico; d) las decide el editor.
   → «Qué documenta un permiso». **Entera.**
7. **(Autorizaciones; práctica)** Se va a grabar la imagen de un niño de nueve años sin madurez
   suficiente para consentir. Según la LO 1/1982: a) basta el consentimiento verbal de un profesor;
   b) consentimiento por escrito del representante legal, que lo pone en conocimiento previo del
   Ministerio Fiscal; si en ocho días se opone, resuelve el juez ✔; c) no hace falta si la grabación
   es en la vía pública; d) basta la autorización del ayuntamiento. Y quien debe poder demostrar el
   consentimiento para tratar datos es el responsable (art. 7.1 RGPD). → «El consentimiento que hay
   que poder demostrar». **Entera.**
8. **(Partes; práctica)** Un técnico reclama horas extraordinarias de una grabación de hace dos
   años. El registro diario de jornada: a) ya se ha destruido, se conserva un año; b) debe
   conservarse cuatro años, a disposición de trabajadores, representantes e Inspección ✔; c) sólo lo
   tiene el trabajador; d) no existe si hay parte de trabajo. Y el parte de trabajo se entrega al
   finalizar la jornada. → «Los partes como prueba», «El parte de trabajo». **Entera.**
9. **(Órdenes de trabajo)** La orden de trabajo diaria: a) se entrega al finalizar la jornada;
   b) se reparte la víspera y mira hacia delante ✔; c) es de una vez para toda la producción; d) es
   lo mismo que el plan de trabajo. Y el Libro de estilo manda comunicar los cambios «de manera
   rápida, fehaciente y simultánea». → «La orden de trabajo diaria», «Cada cambio, por escrito».
   **Entera.**
10. **(Cierres de producción)** Según las fichas del X Convenio, «Elaborar, gestionar y cerrar el
    presupuesto y posterior memoria de los programas» corresponde a: a) el Ayudante de producción;
    b) el Productor/a ✔; c) el Jefe de Departamento de Archivo; d) el realizador. Y «Llevar el
    registro y archivo de la documentación correspondiente a la producción», al Ayudante de
    producción; el expediente cerrado debe llevar índice numerado (recomendación 300 de la CCA).
    → «Quién lleva los papeles», «Qué es cerrar una producción», «La lista de cierre». **Entera.**

Cobertura por rúbrica: gestión documental y trazabilidad (1, 10), expedientes (2, 3), contratos (4),
permisos (6), autorizaciones (7), partes (8), órdenes de trabajo (9), informes (5), cierres (10).
