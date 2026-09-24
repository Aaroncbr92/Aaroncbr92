# T07 · Investigación · X Convenio Colectivo de la RTVA y cuadro de licencias y permisos

Fase: **investigar**. Tema 7 del temario común de Canal Sur: «Articulado del X
Convenio Colectivo Interprovincial de RTVA y sus sociedades filiales. Cuadro de
licencias y permisos.»

**Fecha de lectura de todo lo citado: 24-09-2026.** Las normas del BOE se han leído
en su redacción vigente ese día con `herramientas/boe.py precepto`; el convenio, en
el texto del BOJA.

Siglas: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (RTVA);
Canal Sur Radio y Televisión, S.A. (CSRTV); Boletín Oficial de la Junta de
Andalucía (BOJA); Boletín Oficial del Estado (BOE); Comisión de Vigilancia e
Interpretación del convenio (COMVI); Estatuto de los Trabajadores, texto refundido
aprobado por Real Decreto Legislativo 2/2015 (ET); Registro y Depósito de Convenios
Colectivos del Ministerio de Trabajo (REGCON); disposición adicional (DA);
disposición transitoria (DT).

## 0. Fuentes usadas y ficheros tocados

| Fuente | Fichero |
|---|---|
| X Convenio, BOJA núm. 240, de 10-XII-2014, pp. 49–213 (Resolución de 2-XII-2014, DG de Relaciones Laborales) | `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.{pdf,txt}` (ya estaba) |
| Consulta REGCON por el código del convenio, hecha el 24-09-2026 | `fuentes/canal-sur/documentos/regcon-71000253011989-consulta-2026-09-24.{html,txt}` (nuevo) |
| Reglamento de la Mesa de Contratación de RTVA y CSRTV (portal de transparencia, subido en 2026-03) | `fuentes/canal-sur/documentos/reglamento-mesa-contratacion-rtva-csrtv-2026.{pdf,txt}` (nuevo) |
| Informe de fiscalización de la Cámara de Cuentas de Andalucía sobre RTVA y CSRTV (ejercicio 2018), BOJA núm. 36, de 23-II-2021 | `fuentes/canal-sur/documentos/camara-cuentas-fiscalizacion-rtva-csrtv-2018-boja-36-2021.{pdf,txt}` (nuevo) |
| Cuadro sindical «Permisos, licencias y reducciones de jornada en Canal Sur - RTVA» (CCOO, PDF de 22-VI-2017) | `fuentes/canal-sur/documentos/permisos-licencias-rtva-ccoo-2017.{pdf,txt}` (nuevo; **no oficial**) |
| Noticia de CCOO-FSC Andalucía de 07-02-2025 | `fuentes/canal-sur/documentos/ccoo-fsc-noticia-2025-02-07.{html,txt}` (nuevo; **no oficial**) |
| Ley 7/2024, de 23 de diciembre, del Presupuesto de Andalucía para 2025 (BOE-A-2025-413; el BOE no la consolida, se guarda el diario) | `fuentes/canal-sur/documentos/ley-7-2024-presupuesto-andalucia-2025-boe-a-2025-413.{html,txt}` (nuevo) |
| ET (BOE-A-2015-11430) | `fuentes/canal-sur/BOE-A-2015-11430.md` (volcado nuevo) |
| Ley 3/2012, de 21 de septiembre, de Andalucía (BOE-A-2012-13126) | `fuentes/canal-sur/BOE-A-2012-13126.md` (volcado nuevo) |
| Ley 8/2025, de 22 de diciembre, del Presupuesto de Andalucía para 2026 (BOE-A-2026-945) | `fuentes/canal-sur/BOE-A-2026-945.md` (volcado nuevo) |

Identificadores del BOE comprobados por título con `herramientas/boe_buscar.py`
antes de volcar. Además de este informe, **no he tocado ningún otro fichero** fuera
de los nuevos que lista la tabla. (En `documentos/` hay un
`fusion-csrtv-boja-219-2015.*` que no es mío.)

Comprobación de identidad del texto: el PDF que RTVA y CSRTV cuelgan hoy como «X
Convenio Colectivo» en sus portales de transparencia (Junta de Andalucía,
`/sites/default/files/2022-05/Convenio_Colectivo_(BOJA)_0.pdf` en la ficha de RTVA y
`/sites/default/files/2026-03/X_Convenio_Colectivo_(BOJA)_0.pdf` en la de CSRTV, el
mismo fichero) es el mismo BOJA núm. 240/2014, 165 páginas: extraído el texto,
**no difiere en nada** del `.txt` del repositorio. Ninguno de los dos portales
publica versión consolidada, tablas salariales posteriores ni otros acuerdos: en
«Convenios colectivos y acuerdos» solo figuran el X Convenio y el Reglamento de la
Mesa de Contratación.

## 1. Vigencia y modificaciones

### 1.1. Qué dice el texto

- **Identificación** (Resolución de 2-XII-2014, preámbulo): convenio «de la empresa
  Agencia Pública Empresarial de la Radio y Televisión de Andalucía y sus Sociedades
  Filiales, Canal Sur Radio, S.A., y Canal Sur Televisión, S.A. (Cód.
  71000253011989), suscrito por la representación de la empresa y la de los
  trabajadores con fecha 23 de mayo de 2014 y ratificado el 9 de julio de 2014». La
  resolución se dicta al amparo del «artículo 90, apartados 2 y 3, del Real Decreto
  Legislativo 1/1995» (ET de 1995, hoy derogado) y del Real Decreto 713/2010. Título
  literal del convenio: «X CONVENIO COLECTIVO INTERPROVINCIAL PARA LA AGENCIA PÚBLICA
  EMPRESARIAL DE LA RADIO Y TELEVISIÓN DE ANDALUCÍA Y SUS SOCIEDADES FILIALES, CANAL
  SUR RADIO, S.A., CANAL SUR TV, S.A., Y SUS TRABAJADORES/AS».
- **Art. 4 (Ámbito temporal)**: «El presente Convenio entrará en vigor a todos los
  efectos el día 1 de enero de 2013, con las excepciones que en cada caso se
  determinen, y su duración será de tres años a contar desde dicha fecha, es decir
  hasta el 31 de diciembre de 2015, con independencia de la fecha en que, una vez
  registrado, sea publicado oficialmente.»
- **Art. 5 (Denuncias)**: «Este Convenio Colectivo quedará automáticamente
  prorrogado, salvo que alguna de las partes lo denuncie con una antelación de tres
  meses antes de su vencimiento.» No fija la duración de cada prórroga.

### 1.2. ¿Prorrogado o en ultraactividad?

**Prorrogado, por falta de denuncia registrada, según el art. 5 del propio
convenio; el art. 86.2 ET dice lo mismo como regla supletoria.** Apoyo:

1. **REGCON** (consulta por código 71000253011989, 24-09-2026): cinco trámites y
   ninguno posterior a 2014. Literal de las filas: «CONVENIO COLECTIVO (TEXTO NUEVO)
   Andalucía 10/12/2014 01/01/2013 31/12/2015»; «ACUERDO AMPLIACIÓN ULTRAACTIVIDAD
   Andalucía 05/02/2014 01/01/2010 31/12/2012»; «PROMOCIÓN DE NEGOCIACIÓN Andalucía
   11/12/2012 …»; «DENUNCIA Andalucía 23/10/2012 01/01/2010 31/12/2012»; «CONVENIO
   COLECTIVO (TEXTO NUEVO) Andalucía 11/02/2011 01/01/2010 31/12/2012». La denuncia,
   la promoción de negociación y la ampliación de ultraactividad son **del IX
   Convenio** (vigencia 2010-2012; la ampliación es la Resolución de 28-I-2014, BOJA
   núm. 24, de 5-II-2014, «Acuerdo de prorrogar la ultraactividad del IX Convenio
   Colectivo»). **Del X no hay denuncia, ni promoción de negociación, ni revisión
   salarial, ni acuerdo de comisión, ni modificación inscritos.** Buscado también por
   denominación («CANAL SUR», «RTVA», «RADIOTELEVISION ANDALUZA», «AGENCIA PUBLICA
   EMPRESARIAL RADIO», «CANAL SUR RADIO Y TELEVISION»): solo aparece, además, el Plan
   de Igualdad de RTVA-CSRTV (código 90144283112024, inscrito el 30/09/2024,
   vigencia 01/01/2023-31/12/2026), que no es parte del convenio.
2. **Cámara de Cuentas de Andalucía**, informe de fiscalización del ejercicio 2018
   (Resolución de 9-II-2021, BOJA núm. 36, de 23-II-2021), punto 118: «El citado
   Convenio entró en vigor con efectos el día 1 de enero de 2013, con una duración
   inicial de tres años (hasta el 31 de diciembre de 2015). Durante el ejercicio 2018
   se encuentra prorrogado, situación que sigue manteniéndose durante la realización
   del trabajo de fiscalización.» Punto 234: «El X Convenio Colectivo que se
   encuentra actualmente en vigor está prorrogado. Se publicó mediante Resolución de
   2 de diciembre de 2014, de la Dirección General de Relaciones Laborales, previo
   por tanto al proceso de fusión. En términos generales es el mismo texto desde que
   se creó la empresa y regula las condiciones laborales del personal de la radio,
   de la televisión y de la agencia.»
3. **La propia empresa lo trata hoy como vigente**: Reglamento de la Mesa de
   Contratación, DA primera: «el vigente X Convenio Colectivo»; convocatoria de 228
   plazas (BOJA núm. 186, de 24-IX-2026), base 6.3: «el Anexo III del vigente
   Convenio Colectivo de la RTVA y su sociedad filial», y base 2.1: «El proceso
   selectivo se regirá por el X Convenio Colectivo Interprovincial…».
4. **ET vigente, art. 86** (2 redacciones; la vigente desde 31-12-2021, Real
   Decreto-ley 32/2021): ap. 2, «Salvo pacto en contrario, los convenios colectivos
   se prorrogarán de año en año si no mediara denuncia expresa de las partes.»; ap.
   3, «La vigencia de un convenio colectivo, **una vez denunciado** y concluida la
   duración pactada, se producirá en los términos que se hubiesen establecido en el
   propio convenio. Durante las negociaciones para la renovación de un convenio
   colectivo, en defecto de pacto, se mantendrá su vigencia […]». La ultraactividad
   del ap. 3 presupone denuncia; no consta ninguna, así que el supuesto es el de
   prórroga del art. 5 del convenio y del art. 86.2 ET.

Lo que **no** puedo confirmar: si alguna parte denunció el X Convenio sin inscribir
la denuncia en REGCON, o si hay mesa negociadora de un XI Convenio. No he encontrado
nada publicado.

### 1.3. Modificaciones del articulado desde 2014: ninguna publicada

- **BOJA** (buscador de la sede electrónica, filtro de fecha desde el 11-12-2014,
  búsquedas «"Radio y Televisión de Andalucía" convenio colectivo», «"Canal Sur"
  "convenio colectivo"», «RTVA inscripción depósito publicación»): **ninguna**
  resolución de la autoridad laboral sobre este convenio posterior a la de 2-XII-2014.
  Ni corrección de errores, ni revisión salarial, ni acuerdo de comisión
  negociadora, ni tablas, ni prórroga pactada. Salen solo convocatorias de empleo de
  RTVA y CSRTV, nombramientos, contratos-programa, la Carta de servicio público y los
  informes de la Cámara de Cuentas.
- **REGCON**: ídem (apartado 1.2).
- **Portales de transparencia de RTVA y CSRTV**: solo el BOJA de 2014 y el
  Reglamento de la Mesa de Contratación (apartado 1.4).

**Conclusión: el texto del articulado es hoy, letra por letra, el del BOJA núm.
240/2014.** Lo que ha cambiado es el **contexto normativo** de las DT (apartado 1.5)
y el nombre de la empresa (apartado 1.6).

### 1.4. Un acuerdo que desarrolla el articulado sin modificarlo: el Reglamento de la Mesa de Contratación

No está en el BOJA ni en REGCON; lo cuelgan RTVA y CSRTV en transparencia (fichero
`20260310_REGLAMENTO MESA CONTRATACIÓN.pdf`, 86 páginas). El texto **no lleva
fecha**. La convocatoria de 228 plazas (BOJA 186/2026, fundamentos y base 2.1) lo
cita como «Reglamento de la Mesa de Contratación de 12 de marzo de 2026»; el nombre
del fichero dice 10-03-2026 y el PDF se generó el 11-03-2026. **La fecha exacta del
acuerdo no la puedo confirmar en el propio texto.**

Qué dice que toque el articulado:

- Punto 1: «El objeto del presente Reglamento es desarrollar el Artículo 24 y
  concordantes del X Convenio Colectivo Interprovincial de la Agencia Pública
  Empresarial de la Radio y Televisión de Andalucía y su Sociedad Filial, Canal Sur
  Radio y Televisión, S.A.» y, para el personal fijo, desarrolla «los Artículos 15 y
  siguientes del citado convenio».
- Punto 2.1, composición: «Cinco representantes del Comité Intercentros los cuales
  tendrán en la Mesa el mismo porcentaje del voto ponderado resultante de las
  Elecciones Sindicales» y «otros cinco representantes de la Dirección» (coincide con
  art. 24 del convenio: «cinco representantes del Comité Intercentros y cinco de la
  Dirección»; el voto ponderado es añadido del reglamento).
- Punto 23 (desempeño de funciones superiores): «De acuerdo con lo establecido en el
  Artículo 21.2.4 del Convenio Colectivo, el plazo máximo para el desempeño de
  funciones de superior grupo/puesto es un año salvo aquellas excepciones que
  determine la Mesa de Contratación. Tal y como ha sido acordado en la Mesa de
  Contratación, en aquellos casos de realización de funciones de superior categoría
  motivados por la sustitución de personas trabajadoras en situación de Incapacidad
  Temporal, la duración máxima será la de dicha situación de IT.»
- **DA primera**: «El "registro de cambios de grupo" regulado en el Art. 21,
  Apartado 2.6 del vigente X Convenio Colectivo se desarrollará por la bolsa interna
  para el desempeño temporal de servicios de diferente y/o superior grupo
  profesional o puesto de trabajo (en adelante Bolsas internas) regulada en el
  Capítulo III de este reglamento, al quedar así satisfecha la auténtica finalidad
  del contenido de dicho precepto convencional.»
- DT cuarta: requisitos mínimos de formación para la próxima promoción interna por
  grupo (B01 «Licenciatura o Grado + Máster oficial»; B02 «Grado universitario/
  Diplomatura/Ingeniería Técnica»; B03 «Grado Formativo Superior (FP Superior o
  equivalente)/Diplomatura/Ingeniería Técnica»; B04 «Grado Formativo (FP Grado Medio
  o equivalente)»; B05 «ESO, Bachillerato o Grado Básico») y experiencia mínima
  (B02 48 meses; B03 36; B04 24; B05 12). El art. 18 del convenio solo exigía
  «capacidad, conocimiento y titulación o requisitos necesarios» y «antigüedad en la
  Empresa de al menos seis meses».

### 1.5. Las disposiciones transitorias y la Ley 3/2012: qué queda en 2026

El bloque de DT del convenio **no modifica** el articulado: dice que ciertas
cláusulas quedan «suspendidas» por el Decreto-ley 1/2012 y la Ley 3/2012 de
Andalucía «mientras se mantenga la vigencia de dichas disposiciones» (párrafo que
encabeza las DT). La DT décima prevé que, si se liberan esas restricciones o la
Junta aprueba mejoras para el sector público, «la misma se trasladaría al personal de
RTVA y sus Sociedades Filiales».

Estado hoy de los preceptos de la Ley 3/2012 en que se apoya cada DT (leídos en
BOE-A-2012-13126, redacción vigente a 24-09-2026; la Ley 3/2012 se aplica, art. 3.c,
a «Las agencias públicas empresariales, sociedades mercantiles del sector público
andaluz»):

- **Ley 7/2024, de 23 de diciembre, del Presupuesto de Andalucía para 2025**,
  disposición derogatoria única, letra e): quedan derogados «Los artículos 6, 13, 16,
  17, 21, 26 y 32 de la Ley 3/2012». Efectos: 1-1-2025 (la cadena del BOE fecha la
  redacción «(Derogado)» de los arts. 26 y 32 el 20250101).
- **Ley 8/2025, de 22 de diciembre, del Presupuesto de Andalucía para 2026**, DA
  cuarta: «durante el año 2026 solo se mantendrá la aplicación de las medidas
  contenidas en los artículos 15, 18, 19, 22, 27, 28.2 y 29 de la Ley 3/2012, de 21
  de septiembre, tras la revisión prevista en su artículo 4.» (La Ley 7/2024, DA
  cuarta, decía lo mismo para 2025 con «28» entero en lugar de «28.2».)

Cruce con cada DT del convenio:

| DT del convenio | Precepto de la Ley 3/2012 en que se apoya | Situación en 2026 |
|---|---|---|
| DT 1ª A.a (jornada de 37 h 30 min del personal fijo) | arts. 23 y 25 (y DL 1/2012) | Art. 25 fuera de la lista de la DA 4ª Ley 8/2025: no se aplica en 2026 |
| DT 1ª A.b (jornada y retribuciones −10 % del temporal) | art. 23 | Fuera de la lista: no se aplica en 2026 |
| DT 1ª C (suspende el compromiso de contratar el 50 % de las horas extra descansadas, art. 14.d) | «Ley 3/2012» sin artículo | Sin precepto concreto que cruzar |
| DT 2ª (vacaciones: 22 días hábiles) | art. 26 | **Derogado** desde 1-1-2025 (Ley 7/2024) |
| DT 3ª (permisos: traslado 1 día; 4 días de asuntos propios) | no cita artículo; la materia es la del art. 26 («Vacaciones y permisos») | Art. 26 **derogado** desde 1-1-2025 |
| DT 4ª (amortización de plazas por jubilación; jubilación parcial) | art. 11.5 de la Ley de Presupuestos de 2013 | No comprobado para 2026 |
| DT 5ª A (−10 % retribuciones del temporal) | art. 23.1 | Fuera de la lista: no se aplica en 2026 |
| DT 5ª B y C (antigüedad a 45 € trienio/mes) | art. 19 | **Se mantiene** en 2026 |
| DT 5ª C (reducción del 5 % de la masa salarial) | DL 2/2010; art. 24 | Art. 24 fuera de la lista en 2026 |
| DT 6ª (complemento de IT: 50 % días 1-3, 75 % días 4-20, 100 % desde el 21) | art. 14 | Fuera de la lista: no se aplica en 2026 |
| DT 7ª (dietas y kilometraje topados al Decreto 54/1989) | art. 22 | **Se mantiene** en 2026 |
| DT 8ª (suspensión de la acción social, salvo discapacidad) | art. 28 (y DL 2/2012) | En 2026 solo se mantiene el **28.2** (prohibición de aportar a planes de pensiones); el 28.1 (suspensión de la acción social) queda fuera |
| DT 9ª (crédito horario sindical: el del convenio) | art. 32 | **Derogado** desde 1-1-2025 |

**Lo que no puedo confirmar**: cómo aplica hoy RTVA-CSRTV estas DT (si ha vuelto a
las 35 horas, a los 24 días de vacaciones o a los 6-8 días de asuntos propios). No
hay acuerdo publicado que lo diga. Dos indicios, **no oficiales y de parte**:

- El cuadro sindical de CCOO de 2017 recoge «VACACIONES 24 DÍAS LABORABLES […] ART.
  13 CONVENIO COLECTIVO CONFORME AL ACUERDO DE COM.V.I. DE 19 SET 2016» y los
  asuntos propios del art. 33.B (hasta 6, más 1 con más de 10 años y un octavo con
  más de 15), y cita otros acuerdos de la COMVI (19-9-2016, 26-2-2016, 3-10-2016,
  24-10-2016) que no he podido ver.
- La noticia de CCOO de 07-02-2025 dice: «Volvemos a reclamar el fin de los recortes
  que los sindicatos firmantes del X Convenio Colectivo nos impusieron, mediante
  disposiciones "transitorias" hace ya más de una década: Vacaciones, permisos,
  dietas y kilometrajes, ayudas sociales y retribuciones, antigüedad, etc.»

Los dos dicen cosas distintas sobre vacaciones y permisos, y ninguno es fuente
normativa. **Para el tema: lo seguro es el texto del convenio, el de las DT y el
estado de la Ley 3/2012 en 2025-2026. Cómo se aplica en la empresa, no.**

La Cámara de Cuentas (puntos 74-78) sostiene además que la antigüedad lineal de 45 €
de la DT 5ª «no cumple con lo establecido en el art.19.1 de la Ley 3/2012», porque
ese artículo limita el complemento al importe del grupo equivalente del VI Convenio
del personal laboral de la Junta: «grupo I y II 47,59€; III 32,96€ y IV y V 28,24€».
Es opinión del órgano fiscalizador, no una modificación del convenio.

### 1.6. Denominación de la empresa: dos filiales en el texto, una hoy

El convenio habla de «sus Sociedades Filiales, Canal Sur Radio, S.A., y Canal Sur
Televisión, S.A.». Cámara de Cuentas, punto 8: «El 23 de febrero de 2016, las
sociedades mercantiles Canal Sur Radio S.A. y Canal Sur Televisión S.A., mediante
acuerdo de Junta General con carácter universal, adoptaron la decisión de aprobar la
fusión por absorción de Canal Sur Radio S.A. (absorbida) por parte de Canal Sur
Televisión S.A. (absorbente) […]. Con efectos 1 de abril de 2016, la escritura
pública de fusión quedó inscrita en el Registro Mercantil de Sevilla, pasándose a
denominar la sociedad absorbente, Canal Sur Radio y Televisión S.A. (CSRTV).» El
Reglamento de la Mesa de Contratación ya llama al convenio «X Convenio Colectivo
Interprovincial de la Agencia Pública Empresarial de la Radio y Televisión de
Andalucía y su Sociedad Filial, Canal Sur Radio y Televisión, S.A.». **El enunciado
del programa conserva el plural «sociedades filiales» del título de 2014.**

## 2. Estructura del articulado (contada sobre el texto)

Índice (BOJA pp. 49-51); articulado y disposiciones, pp. 52-91; Anexo I, pp. 91-92;
Anexo II, pp. 92-100; Anexo III, pp. 100-213. **11 capítulos, 74 artículos, 10
disposiciones adicionales, 10 disposiciones transitorias (precedidas de un párrafo
introductorio común), 3 anexos. No hay disposiciones derogatorias ni finales.**

| Capítulo | Rúbrica (cuerpo) | Artículos | N.º |
|---|---|---|---|
| Primero | Disposiciones Generales | 1-9 | 9 |
| Segundo | Jornadas y descansos | 10-14 | 5 |
| Tercero | Provisión de plazas y promoción | 15-20 | 6 |
| Cuarto | Organización | 21-24 | 4 |
| Quinto | Seguridad y Salud en el Trabajo | 25-31 | 7 |
| Sexto | Régimen de personal | 32-36 | 5 |
| Séptimo | Prestaciones Sociales | 37-44 | 8 |
| Octavo | Trabajo y retribución | 45-54 | 10 |
| Noveno | Acción Sindical | 55-62 | 8 |
| Décimo | Régimen disciplinario | 63-72 | 10 |
| Undécimo | Incompatibilidades y Garantías Procesales | 73-74 | 2 |
| **Total** | | | **74** |

Artículos: 1 Ámbito funcional; 2 Ámbito territorial; 3 Ámbito personal; 4 Ámbito
temporal; 5 Denuncias; 6 Prelación normativa; 7 Vinculación a la totalidad; 8
Absorción y compensación; 9 Comisión de Vigilancia e Interpretación (COMVI); 10
Jornada de trabajo; 11 Calendario laboral; 12 Turnos y horarios; 13 Vacaciones; 14
Horas extraordinarias; 15 Provisión de plazas; 16 Reincorporación de excedencia; 17
Traslado; 18 Promoción; 19 Concurso oposición libre; 20 Tribunales; 21 Movilidad; 22
Permuta de puestos de trabajo; 23 Períodos de prueba; 24 Mesa de Contratación; 25
Salud laboral; 26 Comité de Salud Laboral; 27 Comité Intercentros de Seguridad y
Salud Laboral; 28 Evaluación de riesgos laborales; 29 Planificación de la actividad
preventiva; 30 Prendas y protecciones de seguridad; 31 Unidad Basica de Salud y
Asistencia Sanitaria; 32 Excedencias; 33 Licencias, permisos, reducciones de jornada
y facilidades para estudios; 34 Plantilla y registro de personal; 35 Reconocimiento
de antigüedad; 36 Formación Profesional; 37 Ayuda escolar y ayuda a hijos/as con
minusvalía; 38 Becas de estudio; 39 Seguro de vida e invalidez; 40 Prestaciones
complementarias por incapacidad temporal; 41 Servicio de comida por prestación
laboral; 42 Anticipos; 43 Grupo de empresa; 44 Jubilaciones; 45 Clasificación
profesional; 46 Comisión Valoración de Puestos de Trabajo; 47 Conceptos
retributivos; 48 Salario base; 49 Complementos salariales personales; 50
Complementos de puesto de trabajo; 51 Complementos por cantidad y calidad de trabajo;
52 Pagas; 53 Dietas, kilometraje y plus de pernocta; 54 Principio general sobre
retribución; 55 Delegados/as de Personal; 56 Comité de Empresa; 57 Competencias del
Comité de Empresa; 58 Comité Intercentros; 59 Local y tablón de anuncios; 60 Acción
sindical; 61 Delegados/as Sindicales; 62 Asambleas; 63 Norma general; 64 Faltas; 65
Faltas leves; 66 Faltas graves; 67 Faltas muy graves; 68 Abuso de autoridad; 69
Sanciones; 70 Cumplimiento de las sanciones; 71 Prescripción de faltas; 72
Procedimiento sancionador; 73 Incompatibilidades; 74 Garantías procesales.

**Diferencias entre índice y cuerpo** (manda el cuerpo): art. 26 «Comité Salud
Laboral» (índice) / «Comité de Salud Laboral» (cuerpo); art. 31 «Asistencia
sanitaria» / «Unidad Basica de Salud y Asistencia Sanitaria»; art. 40 «Prestaciones
por incapacidad temporal» / «Prestaciones complementarias por incapacidad temporal»;
art. 52 «Pagas extraordinarias» / «Pagas»; DA 1ª «Salarios y otros conceptos
retributivos» / «Salario y otros conceptos retributivos»; DA 6ª «Cláusula de
conciencia» / «Cláusula de conciencia y derecho de autor»; DT 3ª «Permisos y
reducciones de jornada» / «Permisos»; DT 7ª «plus de pernocta» / «plus de pernota»
(errata del cuerpo); Anexo I «Tablas Salariales» / «REMUNERACIÓN MENSUAL/ANUAL BRUTA Y
TABLA DE ANTIGÜEDAD».

Disposiciones adicionales (10): 1ª Salario y otros conceptos retributivos; 2ª
Desconexiones provinciales; 3ª Conciliación de la vida laboral y familiar; 4ª
Contingencias comunes; 5ª Empresas de servicios; 6ª Cláusula de conciencia y derecho
de autor; 7ª (sin rúbrica: externalización sin merma de plantilla); 8ª Definición de
funciones; 9ª (sin rúbrica: límite de la masa salarial); 10ª Plan de Igualdad.

Disposiciones transitorias (10): 1ª Jornada y horarios; 2ª Vacaciones; 3ª Permisos;
4ª Jubilaciones; 5ª Retribuciones; 6ª Incapacidad temporal; 7ª Dietas, kilometraje y
plus de pernota; 8ª Acción Social; 9ª Crédito horario de los representantes
sindicales; 10ª (sin rúbrica: traslado de mejoras y liberación de restricciones).

Anexos (3): I, remuneración mensual/anual bruta por niveles B01-B05 y tabla de
trienios; II, plantilla estructural por puesto, entidad (RTVA, CSTV, CSR),
localidad, nivel y dotación «ESTRUC. IX CC» / «ESTRUC. X CC», con totales por centro
y sin total general (sumando los totales de Sevilla, 244 RTVA + 686 Canal Sur TV +
147 Canal Sur Radio, y «TOTAL DIRECCIONES TERRITORIALES» 452, salen 1.529; la suma es
mía); III, definición de funciones, 114 fichas de puesto («CÓDIGO PUESTO»,
«DENOMINACION DEL PUESTO», «OBJETO O FUNCIÓN BÁSICA DEL PUESTO», «TAREAS MÁS
SIGNIFICATIVAS DEL PUESTO»), contadas por la cadena «CÓDIGO PUESTO».

## 3. El «cuadro de licencias y permisos»

### 3.1. Dónde está

**En el convenio no hay ningún «cuadro» de licencias y permisos.** La palabra
«cuadro» sale tres veces en el texto y ninguna con este sentido (DT 5ª B, «el cuadro
que figura en el Anexo I» de antigüedad; y dos fichas del Anexo III, «cuadro de
luminotecnia» y «cuadro de imagen»). Ningún anexo trata de permisos. La regulación
está en el **art. 33, «Licencias, permisos, reducciones de jornada y facilidades
para estudios»**, en seis bloques (A permisos y ausencias retribuidas, con la lista
de letras a) a n) y los plazos de preaviso de cada una; B asuntos propios; C turno más
favorable; D reducciones de jornada; E licencias no retribuidas; F parejas de hecho),
**afectado por la DT 3ª**. Materias vecinas: vacaciones (art. 13 y DT 2ª),
excedencias (art. 32), crédito horario sindical (arts. 55, 56, 61 y DT 9ª).

Que existe un «cuadro de licencias y permisos» como **documento interno** lo dice la
noticia de CCOO de 07-02-2025: «El cuadro de licencias y permisos debe estar
actualizado y accesible a todas y todos los trabajadores para no generar confusión
en los derechos que nos corresponden.» **No he encontrado ese cuadro oficial
publicado** (ni en BOJA, ni en REGCON, ni en los portales de transparencia de RTVA y
CSRTV). Lo más parecido que hay en abierto es el cuadro sindical de CCOO de 2017
(12 páginas, columnas «PERMISOS / DURACIÓN / PREAVISO / JUSTIFICANTE»), que mezcla el
art. 33 con permisos de la Junta de Andalucía asumidos por acuerdos de la COMVI.
**No es fuente oficial y no lo transcribo como tal**; lo resumo en 3.3.

### 3.2. Transcripción literal del art. 33 y de la DT 3ª

Transcrito del BOJA núm. 240/2014, pp. 64-68 (art. 33) y 88 (DT 3ª). Se quitan las cabeceras y pies
de página del BOJA y se reconstruyen los saltos de párrafo; el texto va letra por
letra, erratas incluidas («trabajador/ a» por corte de línea queda unido).

<!-- inicio transcripción literal art. 33 -->

> Artículo 33. Licencias, permisos, reducciones de jornada y facilidades para estudios.
>
> A. Permisos y ausencias retribuidas.
>
> Apartado 1. La Agencia Pública Empresarial de la Radio Televisión de Andalucía y sus Sociedades Filiales concederá, de acuerdo con lo establecido en la vigente normativa laboral, las siguientes licencias:
>
> a) 20 días naturales en caso de matrimonio del/la trabajador/a.
>
> b) 3 días naturales, a partir del hecho causante, en los casos de nacimiento, adopción de hijo/a y enfermedad grave u hospitalización que demande ayuda inminente por parte del/la trabajador/a o fallecimiento de parientes hasta el segundo grado de consanguinidad o afinidad. Cuando, por tales motivos, el/la trabajador/a necesitase hacer un desplazamiento al efecto, el plazo será de 5 días. Este permiso será flexible y podrá disfrutarse justamente después del hecho causante o de manera no consecutiva en los veinte días posteriores al hecho, comunicándose a la empresa la planificación de los mismos para facilitar la organización del trabajo. En los casos de nacimiento de hijos/as prematuros/as o en los que, por cualquier motivo, éstos/as tengan que permanecer hospitalizados/as después del parto y mientras dure esta situación, el/la trabajador/a tendrá derecho a ausentarse del lugar de trabajo hasta un máximo de 2 horas diarias, percibiendo las retribuciones íntegras. En dichos supuestos, el permiso de maternidad puede computarse, a instancia de la madre o, en caso de que ella falte, del padre, a partir de la fecha del alta hospitalaria. Se excluyen de este cómputo las primeras seis semanas posteriores al parto, de descanso obligatorio para la madre.
>
> c) 2 días por traslado de domicilio habitual, y tres por traslado de Centro de Trabajo. Sólo se podrá hacer uso de esta licencia una vez durante el año natural.
>
> d) Por el tiempo indispensable, para el cumplimiento de un deber inexcusable de carácter público o personal y por deberes relacionados con la conciliación de la vida familiar y laboral. Se entiende como deber inexcusable de carácter público o personal la obligación que incumbe a una persona cuyo incumplimiento le genera una responsabilidad de índole penal, civil o administrativa. Se entiende por deber de carácter público inexcusable, a título de ejemplo, las citaciones efectuadas por Autoridades, asistencias a Tribunales, asistencia a Plenos por parte de personal electo, así como cualquier otra de análoga naturaleza.
>
> e) Un día en los casos de matrimonio de hijos/as, hermanos/as o padres/madres y dos días en caso de que el matrimonio tenga lugar en otra provincia no limítrofe a la del Centro de Trabajo.
>
> f) Para realizar funciones sindicales o de representación del personal en los términos establecidos en el presente Convenio Colectivo.
>
> g) Por lactancia de un/a hijo/a menor de doce meses, los/as trabajadores/as tendrán derecho a una hora de ausencia al trabajo, la cual podrán dividir en dos fracciones. En caso de parto múltiple el trabajador o trabajadora tendrá derecho a dos horas diarias de ausencia al trabajo por cada hijo/a en concepto de lactancia de hijos/as menores de doce meses. En caso de que los dos convivientes trabajen en la Agencia Pública Empresarial de la RTVA y sus Sociedades Filiales sólo uno podrá hacer uso de este derecho.
>
> Se establece la posibilidad de sustituir, por decisión de la madre, el permiso de lactancia de los/las hijos/as menores de doce meses por un permiso que acumule en jornadas completas el tiempo correspondiente. Dicho permiso se incrementará proporcionalmente en los casos de parto múltiple.
>
> h) En los supuestos de adopción, nacimiento y acogimiento, tanto preadoptivo como permanente, de menores de hasta seis años la suspensión tendrá una duración de dieciséis semanas ininterrumpidas, ampliables en el supuesto de adopción o acogimiento múltiple en dos semanas más por cada hijo/a a partir del segundo, contadas a la elección del/la trabajador/a, bien a partir de la decisión administrativa o judicial de acogimiento, bien a partir de la resolución judicial por la que se constituye la adopción. La duración será asimismo, de dieciséis semanas en los supuestos de adopción o acogimiento de menores, mayores de seis años de edad, cuando se trate de menores con capacidades diferenciadas o que por sus circunstancias y experiencias personales o que por provenir del extranjero, tengan especiales dificultades de inserción social y familiar debidamente acreditadas por los servicios sociales competentes. En caso de que la madre y el padre trabajen, el período de suspensión se distribuirá a opción de los/as interesados/as, que podrán disfrutarlos de forma simultánea o sucesiva, siempre con períodos ininterrumpidos y con los límites señalados.
>
> En el supuesto de parto, adopción, acogimiento preadoptivo o permanente, una vez agotado el permiso por maternidad o adopción y a continuación del mismo, el personal incluido en el ámbito de aplicación de este convenio tendrá derecho a un permiso retribuido de cuatro semanas adicionales. Este permiso sólo podrá disfrutarse por un progenitor cuando el otro trabaje. En el caso de que ambos sean titulares del permiso, únicamente uno de ellos podrá disfrutar del mismo.
>
> En los casos de disfrute simultáneo de períodos de descanso, la suma de los mismos no podrá exceder de las veinte semanas previstas anteriormente en el caso de nacimiento o adopción o de las que correspondan en caso de adopción, nacimiento o acogimiento múltiple.
>
> Los períodos a que se refiere este epígrafe podrán disfrutarse en régimen de jornada completa o a tiempo parcial, previo acuerdo entre la empresa y los/las trabajadores/as afectados/as, en los términos que legalmente se determinen.
>
> Durante el disfrute de este permiso se podrá participar en los cursos de formación que convoque la empresa no computándose ese tiempo en el tiempo de permiso.
>
> En caso de fallecimiento de la madre durante el permiso, el otro progenitor podrá hacer uso de la totalidad o, en su caso, de la parte que reste de permiso.
>
> i) Se establece la concesión de 15 días consecutivos de permiso por nacimiento, acogimiento o adopción de un/a hijo/a, a disfrutar por el padre o por el otro progenitor, a partir de la fecha del nacimiento, de la decisión administrativa judicial de acogimiento o de la resolución judicial por la que se constituya la adopción. Este permiso es independiente del disfrute de los permisos contemplados en el apartado «h».
>
> En los supuestos de adopción internacional, cuando sea necesario el desplazamiento previo de los padres al país de origen del/la adoptado/a, el período de suspensión, previsto para cada caso en este epígrafe, podrá iniciarse hasta cuatro semanas antes de la resolución por la que se constituye la adopción.
>
> Se podrá disfrutar de un permiso de hasta dos meses de duración, percibiendo durante este período exclusivamente las retribuciones básicas (salario base y antigüedad), en los supuestos de adopción internacional cuando sea necesario el desplazamiento previo de los padres al país de origen del adoptado.
>
> Se establece el derecho de las madres y de los padres a acumular el período de disfrute de vacaciones al permiso de maternidad, lactancia y paternidad, aún habiendo expirado ya el año natural a que tal período corresponda.
>
> Los/Las trabajadores/as de RTVA y SS.FF. que tengan hijos/as con discapacidad psíquica, física o sensorial tendrán derecho a ausentarse del trabajo por el tiempo indispensable, previa justificación al efecto, para asistir durante su jornada de trabajo a reuniones de coordinación de su centro de educación especial, donde reciba tratamiento o para acompañarlo si ha de recibir apoyo adicional en el ámbito sanitario.
>
> j) Para concurrir a exámenes y demás pruebas de aptitud, durante los días de su celebración. La Agencia Pública Empresarial de la RTVA y sus Sociedades Filiales concederá los permisos necesarios, por el tiempo máximo de doce días al año, a los/las trabajadores/as que, inscritos/as en cursos organizados en centros oficiales reconocidos por el Ministerio de Educación, y Consejería de Educación, para la obtención de un título académico oficial, tengan que concurrir a exámenes. Dicha licencia retribuida se otorgará igualmente a los/as trabajadores/as que concurran a exámenes convocados por la Empresa. La Empresa, en todo caso, exigirá los oportunos justificantes acreditativos del disfrute efectivo por el/la trabajador/a de este derecho.
>
> k) Para la realización de exámenes prenatales y técnicas de preparación al parto.
>
> l) Por ser preciso atender el cuidado de un familiar de primer grado, el/la trabajador/a tendrá derecho a solicitar una reducción de hasta el cincuenta por ciento de la jornada laboral, con carácter retribuido, por razones de enfermedad muy grave y por el plazo máximo de un mes.
>
> m) Permiso por razón de violencia de género sobre la mujer trabajadora: las faltas de asistencia de las trabajadoras víctimas de violencia de género, totales o parciales, tendrán la consideración de justificadas por el tiempo y en las condiciones en que así lo determinen los servicios sociales de atención o de salud según proceda.
>
> Asimismo, las trabajadoras víctimas de violencia sobre la mujer, para hacer efectiva su protección o su derecho de asistencia social integral, tendrán derecho a la reducción de la jornada con disminución proporcional de la retribución, o la reordenación del tiempo de trabajo, a través de la adaptación del horario, de la aplicación del horario flexible o de otras formas de ordenación del tiempo de trabajo que sean aplicables.
>
> n) Permiso por cuidado de hijo menor afectado por cáncer u otra enfermedad grave: el/la trabajador/a tendrá derecho, siempre que ambos progenitores, adoptantes o acogedores de carácter preadoptivo o permanente trabajen, a una reducción de la jornada de trabajo de al menos la mitad de la duración de aquélla, percibiendo las retribuciones íntegras con cargo a los presupuestos del órgano o entidad donde venga prestando sus servicios, para el cuidado, durante la hospitalización y tratamiento continuado, del hijo menor de edad afectado por cáncer (tumores malignos, melanomas o carcinomas) o por cualquier otra enfermedad grave que implique un ingreso hospitalario de larga duración y requiera la necesidad de su cuidado directo, continuo y permanente acreditado por el informe del servicio Público de Salud u órgano administrativo sanitario de la Comunidad Autónoma o, en su caso, de la entidad sanitaria concertada correspondiente y, como máximo, hasta que el menor cumpla los 18 años.
>
> Cuando concurran en ambos progenitores, adoptantes o acogedores de carácter preadoptivo o permanente, por el mismo sujeto y hecho causante, las circunstancias necesarias para tener derecho a este permiso o, en su caso, puedan tener la condición de beneficiarios de la prestación establecida para este fin en el Régimen de la Seguridad Social que les sea de aplicación, el/la trabajador/a tendrá derecho a la percepción de las retribuciones íntegras durante el tiempo que dure la reducción de su jornada de trabajo, siempre que el otro progenitor, adoptante o acogedor de carácter preadoptivo o permanente, sin perjuicio del derecho a la reducción de jornada que le corresponda, no cobre sus retribuciones íntegras en virtud de este permiso o como beneficiario de la prestación establecida para este fin en el Régimen de la Seguridad Social que le sea de aplicación. En caso contrario, sólo se tendrá derecho a la reducción de jornada, con la consiguiente reducción de retribuciones. Asimismo, en el supuesto de que ambos presten servicios en el mismo órgano o entidad, ésta podrá limitar su ejercicio simultáneo por razones fundadas en el correcto funcionamiento del servicio.
>
> Durante la vigencia del presente Convenio, la COMVI procederá a elaborar un reglamento que regule el procedimiento y concrete las condiciones y supuestos en los que esta reducción de jornada se podrá acumular en jornadas completas.
>
> Apartado 2. El/La trabajador/a habrá de solicitar la correspondiente licencia a la Dirección de Organización, RR.HH. y Servicios Generales en los siguientes plazos:
>
> - Letra a) 15 días de antelación.
>
> - Letra b) Tan pronto como suceda el hecho.
>
> - Letra c) 15 días de antelación.
>
> - Letra d) 15 días de antelación o con la misma fecha en que ha sido objeto de citación el/la trabajador/a.
>
> - Letra e) 15 días de antelación.
>
> - Letra f) La comunicación se efectuará con 48 horas de antelación, o desde que se tenga conocimiento del hecho.
>
> - Letra g) 15 días de antelación.
>
> - Letra h) 15 días de antelación o tan pronto sea conocido el hecho.
>
> - Letras i y j) tan pronto sea conocido el hecho.
>
> - Letra k), La comunicación se efectuará con 48 horas de antelación, o desde que se tenga conocimiento del hecho
>
> - Letra l), 7 días de antelación
>
> - Letra m), Para las faltas de asistencia se estará a lo determinado por los servicios sociales o de salud.
>
> - Letra n), Desde que se acrediten las circunstancias especificadas en dicho apartado para tener derecho a la reducción de jornada señalada en el mismo.
>
> Apartado 3. El/La trabajador/a deberá presentar justificación suficiente del motivo alegado para la solicitud del permiso o licencia concedido o a conceder. En los supuestos de reducción de jornada el personal deberá preavisar a la Dirección de Organización, RR.HH. y SS.GG. con quince días de antelación la fecha en la que se reincorporará a su jornada ordinaria
>
> B) Permiso retribuido para asuntos propios.
>
> Apartado 1. Todo/a trabajador/a tendrá derecho a un día de permiso retribuido por año de servicio prestado independientemente del período de vacaciones establecido con carácter general.
>
> Apartado 2. El máximo de días por este concepto no podrá exceder de seis anuales, con las siguientes excepciones:
>
> 1. Las/os trabajadoras/es que tengan una antigüedad superior a los diez años podrán disfrutar de un día de permiso retribuido adicional
>
> 2. Las/os trabajadoras/es con una antigüedad superior a los quince años podrán disfrutar de un octavo día de permiso retribuido.
>
> Apartado 3. El período de disfrute coincidirá con el año natural del nacimiento del derecho. Transcurrido el mismo sin haberse solicitado caducará este derecho. El disfrute no podrá acumularse a ningún período de vacaciones. No obstante podrá unirse si las necesidades del servicio lo permiten, previo consentimiento de la Empresa.
>
> Apartado 4. La fecha de disfrute se fijará de común acuerdo con la Agencia Pública Empresarial de la RTVA y sus Sociedades Filiales.
>
> Apartado 5. En el caso de que por necesidades del servicio no se puedan disfrutar los días de asuntos propios en el año natural del nacimiento del derecho, se podrán disfrutar dos días de asuntos propios en el primer mes del año siguiente, previo acuerdo con la Empresa.
>
> C) Turno más favorable.
>
> Apartado 1. La Agencia Pública Empresarial de la RTVA y sus Sociedades Filiales adscribirá al/la trabajador/a al turno más favorable para facilitar el cumplimiento de las obligaciones académicas oficiales, de acuerdo con las disposiciones legales de carácter general. Cuando concurran varios/as trabajadores/as de igual puesto de trabajo y especialidad solicitando un permiso de estas características, será concedido por la Empresa de acuerdo con la representación de los/las trabajadores/as, teniendo en cuenta los siguientes criterios:
>
> - Antigüedad.
>
> - Aprovechamiento académico.
>
> - Orden de solicitud.
>
> Apartado 2. La Agencia Pública Empresarial de la RTVA y sus Sociedades Filiales podrá adscribir al/la trabajador/a a un turno más favorable, por causa de embarazo, para la asistencia a exámenes prenatales y técnicas de preparación al parto.
>
> Apartado 3. Igualmente la empresa facilitará el cambio de puesto de trabajo, o en su caso, funciones de aquellas trabajadoras que, por su estado de gestación puedan estar sometidas a riesgos.
>
> Apartado 4. La Agencia Pública Empresarial de la RTVA y sus Sociedades Filiales podrá adscribir al/la trabajador/a a un turno más favorable al objeto de que presten cuidados a familiares enfermos que convivan con el/la trabajador/a, necesiten asistencia permanente y no tengan otros medios de auxilio.
>
> Apartado 5. Se podrán beneficiar de un turno más favorable por cuidado de un/a hijo/a menor de seis años de edad, aquellos/as trabajadores/as que así lo soliciten.
>
> Apartado 6. Durante la vigencia del presente Convenio, la COMVI procederá a elaborar un reglamento que regule el procedimiento y determine los criterios de valoración de las circunstancias subjetivas y objetivas concurrentes en la solicitud de los turnos más favorables que se establecen en el presente convenio colectivo
>
> D) Reducciones de jornada.
>
> Apartado 1. Reducción de jornada no retribuida para el perfeccionamiento profesional.
>
> La reducción de jornada para la asistencia a cursos de formación profesional específicos, de acuerdo con las disposiciones legales de carácter general, se efectuará con arreglo a las siguientes condiciones y procedimiento, y siempre que se cumplan los siguientes requisitos:
>
> - Que el/la trabajador/a haya superado el período de prueba.
>
> - Que esté inscrito en un curso de Formación Profesional de un Centro Oficial, Sindical o registrado en el Ministerio de Trabajo.
>
> - Que el curso sea específico para la actualización o perfeccionamiento de los conocimientos de la profesión que ejerce en la Agencia Pública Empresarial de la RTVA y sus Sociedades Filiales.
>
> - En todo caso la reducción de la jornada será del 50%.
>
> - Que se comunique a la comisión de formación
>
> Apartado 2. Reducción de jornada por guarda legal.
>
> Quien por razones de guarda legal tenga a su cuidado directo algún/a menor de doce años o a un/a disminuido/a físico/a, psíquico/a o sensorial que no desempeñe otra actividad retribuida, tendrá derecho a una reducción de la jornada de trabajo diaria, con la disminución proporcional del salario entre, al menos, un octavo y un máximo de la mitad de la duración de aquélla.
>
> Tendrá el mismo derecho quien precise encargarse del cuidado directo de un familiar, hasta el segundo grado de consanguinidad o afinidad, que por razones de edad, accidente o enfermedad no pueda valerse por sí mismo, y que no desempeñe actividad retribuida.
>
> La reducción de jornada contemplada en este apartado constituye un derecho individual de los/las trabajadores/as. No obstante, si dos o más trabajadores/as de RTVA y SS.FF. generasen este derecho por el mismo hecho causante, la empresa podrá limitar su ejercicio simultáneo por razones justificadas de funcionamiento de la empresa.
>
> Apartado 3. Los permisos, turnos más favorables y reducciones de jornada concedidos en razón de estudios, promoción y formación profesional, deberán acreditarse mediante el pertinente certificado. Los turnos más favorables y reducciones de jornada podrán ser anulados en caso de falta de aprovechamiento, debiendo este ser acreditado debidamente. Durante la vigencia del presente Convenio, la COMVI procederá a elaborar un reglamento que regule el procedimiento y concrete tales circunstancias.
>
> Apartado 4. Los/Las trabajadores/as afectados/as por este Convenio tendrán derecho a una reducción de la jornada del 50%, por un período mínimo de treinta días, con la correspondiente reducción proporcional de sus retribuciones, siempre que la solicitud correspondiente no sea incardinable en alguno de los supuestos de reducción de jornada o licencias no retribuidas establecidos en el presente Convenio Colectivo.
>
> E) Licencias o permisos no retribuidos.
>
> En caso extraordinario debidamente acreditado, se concederán licencias por el tiempo que sea preciso sin percibo de haberes, con el consentimiento de la Agencia Pública Empresarial de la RTVA y sus Sociedades Filiales y sin que exceda, en todo caso, de seis meses en el año natural en el que se solicite.
>
> F) Parejas de hecho.
>
> Las parejas de hecho tendrán los mismos beneficios que establece el Convenio Colectivo para las parejas de derecho, debiendo acreditar para ello una convivencia de al menos seis meses de duración mediante el correspondiente Certificado de Empadronamiento o Convivencia.

<!-- fin art. 33 -->

Y la DT 3ª, que lo afecta:

> Disposición transitoria tercera. Permisos.
>
> A. Traslado de domicilio.- El permiso de dos (2) días por traslado de domicilio habitual establecido en el art. 33. A. 1.c) de este Convenio Colectivo queda establecido en un (1) día.
>
> B. Días de asuntos propios. Las Licencias y permisos regulados en el art. 33 de este Convenio Colectivo quedan en suspenso y pasan a ser exclusivamente de un total de 4 días al año que podrán ser acumulados a los de vacaciones anuales.


### 3.3. El art. 33 en forma de cuadro (para el redactor)

Resumen **mío** del art. 33.A, con las cifras literales del texto y el plazo de
solicitud de su apartado 2. La columna «DT 3ª» dice si esta la afecta.

| Letra | Supuesto | Duración (literal) | Solicitud (art. 33.A.2) | DT 3ª |
|---|---|---|---|---|
| a | Matrimonio del trabajador | «20 días naturales» | «15 días de antelación» | — |
| b | Nacimiento, adopción, enfermedad grave u hospitalización «que demande ayuda inminente», fallecimiento de parientes hasta 2.º grado | «3 días naturales, a partir del hecho causante»; con desplazamiento «5 días»; flexible, «en los veinte días posteriores al hecho» | «Tan pronto como suceda el hecho» | — |
| b (2.º párr.) | Hijos prematuros u hospitalizados tras el parto | ausencia «hasta un máximo de 2 horas diarias, percibiendo las retribuciones íntegras» | ídem | — |
| c | Traslado de domicilio / de centro de trabajo | «2 días» / «tres»; «una vez durante el año natural» | «15 días de antelación» | Domicilio: **1 día** |
| d | Deber inexcusable público o personal; deberes de conciliación | «Por el tiempo indispensable» | «15 días de antelación o con la misma fecha en que ha sido objeto de citación» | — |
| e | Matrimonio de hijos, hermanos o padres | «Un día»; «dos días» si en provincia no limítrofe | «15 días de antelación» | — |
| f | Funciones sindicales o de representación | «en los términos establecidos en el presente Convenio» | «48 horas de antelación, o desde que se tenga conocimiento» | — |
| g | Lactancia de hijo menor de 12 meses | «una hora», divisible en dos fracciones; parto múltiple «dos horas diarias […] por cada hijo/a»; acumulable en jornadas completas «por decisión de la madre» | «15 días de antelación» | — |
| h | Adopción, nacimiento, acogimiento | «dieciséis semanas ininterrumpidas» (+2 por hijo desde el segundo en múltiple); después, «permiso retribuido de cuatro semanas adicionales» | «15 días de antelación o tan pronto sea conocido el hecho» | — |
| i | Permiso del padre u otro progenitor | «15 días consecutivos»; adopción internacional: «hasta dos meses» con solo retribuciones básicas | «tan pronto sea conocido el hecho» | — |
| j | Exámenes | «durante los días de su celebración»; «tiempo máximo de doce días al año» | «tan pronto sea conocido el hecho» | — |
| k | Exámenes prenatales y preparación al parto | (sin duración) | «48 horas de antelación, o desde que se tenga conocimiento» | — |
| l | Enfermedad muy grave de familiar de 1.er grado | reducción «de hasta el cincuenta por ciento», retribuida, «plazo máximo de un mes» | «7 días de antelación» | — |
| m | Violencia de género | faltas justificadas según los servicios sociales o de salud; reducción o reordenación | «se estará a lo determinado por los servicios sociales o de salud» | — |
| n | Hijo menor con cáncer u otra enfermedad grave | reducción «de al menos la mitad», retribuciones íntegras, «hasta que el menor cumpla los 18 años» | «Desde que se acrediten las circunstancias» | — |

Resto del art. 33: B, asuntos propios, «un día […] por año de servicio», máximo
«seis anuales», +1 con antigüedad «superior a los diez años», «un octavo día» con
antigüedad «superior a los quince años» (DT 3ª B: «un total de 4 días al año» que
«podrán ser acumulados a los de vacaciones»); C, turno más favorable (estudios,
embarazo, familiares enfermos convivientes, hijo menor de seis años); D, reducciones
de jornada (perfeccionamiento, «del 50%», no retribuida; guarda legal, «entre, al
menos, un octavo y un máximo de la mitad»; voluntaria «del 50%, por un período mínimo
de treinta días»); E, licencia no retribuida, máximo «seis meses en el año natural»;
F, parejas de hecho, «convivencia de al menos seis meses».

**Cuadro sindical de CCOO (2017), no oficial**: además de lo anterior recoge, con cita
de su origen, permisos que **no están en el art. 33** y que atribuye a acuerdos de la
COMVI o a normas de la Junta de Andalucía:

- «PERMISO POR GESTACIÓN (acuerdo personal laboral Junta Andalucía 15/04/2016 BOJA
  14/04/16 y COMVI 26/02/2016)»: «A PARTIR DE LA SEMANA 37 DE GESTACIÓN O DE LA
  SEMANA 35 SI ES PARTO MÚLTIPLE, HASTA EL PARTO».
- «POR ENFERMEDAD INFECTO-CONTAGIOSA HIJO MENOR DE 9 AÑOS (ART. 9.1.E.2. INSTRUCCIÓN
  4/2012 […] COMVI 19/09/2016)»: «3 DÍAS NATURALES CONTINUADOS».
- Desplazamiento del art. 33.A.1.b: «LA DISTANCIA PARA QUE EXISTA DESPLAZAMIENTO DEBE
  SER SUPERIOR A LOS 30 KM, DESDE EL DOMICILIO HABITUAL DEL TRABAJADOR. (COMVI
  3/10/2016)».
- Licencia no retribuida «PARA CUIDAR CONYUGE CON TRATAMIENTOS PALIATIVOS (ACUERDO
  9/7/2013 CONSEJO DE GOBIERNO Y COMVI 24/10/2016)»: «HASTA UN AÑO DE DURACIÓN, QUE
  PODRÁ SER AMPLIADO UNA VEZ POR IGUAL PERIODO».
- Ausencias por consulta médica propia o de familiares e indisposición, con
  justificante.
- Lactancia «PARA HIJOS MENORES DE 16 MESES» y acumulación «MÁXIMO 4 SEMANAS» (cita la
  Instrucción 4/2012 de la Junta), frente a los doce meses del art. 33.A.1.g.
- Paternidad de «4 SEMANAS» (cita la Ley 9/2009 y el art. 48.7 ET), frente a los 15
  días del art. 33.A.1.i; y en asuntos propios, solicitud «AL MENOS, 48 HORAS ANTES».

Ninguno de esos acuerdos de la COMVI está publicado; no los he visto. **Todo esto
queda fuera como dato del tema**, salvo para decir que existen fuera del convenio.
Además, varias entradas de ese cuadro de 2017 ya no casan con el ET de hoy (por
ejemplo, la paternidad de 4 semanas; véase el apartado 5).

## 4. El resto del articulado, por capítulos

### Capítulo I. Disposiciones generales (arts. 1-9)

- **Art. 1**: regula las relaciones laborales «entre la Agencia Pública Empresarial de
  la RTVA y SS.FF. y su personal». La Agencia y sus filiales «se configuran como una
  unidad de Empresa», con posibilidad de que los grupos profesionales «presten
  servicios, indistintamente para cualquiera de las Empresas»; «La unidad de empresa
  no implicará la movilidad geográfica».
- **Art. 2**: todos los centros actuales «así como en otros centros que se puedan
  crear en el futuro».
- **Art. 3**: afecta a todos los trabajadores con **seis exclusiones** «expresamente»:
  a) «Colaboradores/as y asesores/as»; b) «Actores, actrices, músicos, cantantes,
  orquestas, coros y agrupaciones musicales»; c) «El personal artístico en general,
  cuyos servicios sean contratados para actuaciones concretas»; d) agentes
  publicitarios y adaptadores literarios y musicales de obras no escritas para radio
  o televisión; e) «El personal directivo de alta gestión o de libre designación»;
  f) profesionales con contrato civil o mercantil. La empresa da «anualmente» al
  Comité Intercentros la relación de este personal.
- **Arts. 4 y 5**: véase apartado 1.1.
- **Art. 6**: las normas del convenio «se aplicarán con carácter prioritario y
  preferente respecto a cualquier otra disposición o norma legal»; en lo no previsto,
  el ET y, «en su defecto», las demás disposiciones generales.
- **Art. 7**: convenio «indivisible», «todo orgánico unitario».
- **Art. 8**: las mejoras «no serán absorbibles y compensables» con las que establezca
  una disposición legal, «salvo cuando expresamente se pacte lo contrario».
- **Art. 9, COMVI**: se constituye «en el plazo de quince días a contar desde la
  firma»; «cinco miembros» de los trabajadores y «otros tantos» de la empresa, con
  «dos asesores/as» por parte; **seis funciones** (a-f: interpretar, vigilar,
  arbitrar, dar conocimiento de acuerdos, «Conocer y mediar en los conflictos
  individuales y/o colectivos», y materias no previstas); funciona por «su propio
  reglamento». Ap. 5: «Será obligatorio que, previo a la interposición de
  reclamaciones ante la jurisdicción laboral, se interponga reclamación ante la
  COMVI.»

### Capítulo II. Jornadas y descansos (arts. 10-14)

- **Art. 10**: jornada anual de «mil quinientas cuarenta horas», equivalente a
  «treinta y cinco horas» semanales. Se obtiene restando a 365 días: «Once fiestas de
  carácter nacional», «Una fiesta de carácter autonómico», «Dos fiestas de carácter
  local», «Veinticuatro días laborables de vacaciones al año (excluidos sábados)»,
  descanso semanal, los días 24 y 31 de diciembre («festivos a todos los efectos»;
  si no se disfrutan, acumulables a vacaciones) y los días de ajuste. **DT 1ª**:
  jornada del fijo, «treinta y siete horas y treinta minutos semanales […] de
  promedio en cómputo anual»; temporales, interinos e indefinidos no fijos, jornada
  y retribuciones reducidas un 10 %; horario flexible de ±1 hora con presencia
  obligatoria «entre las 9 y las 14 horas» (mañana) o «entre las 16,00 horas y las
  21,00 horas» (tarde). Estado en 2026: apartado 1.5.
- **Art. 11**: la Dirección hace los calendarios por centro; se negocian con el Comité
  de Empresa o Delegados y los ratifican el Comité Intercentros y la Dirección. Si una
  fiesta «retribuible y no recuperable» cae en sábado, «se trasladará al viernes
  precedente».
- **Art. 12**: turnos publicados «entre los días 15 y 25 del mes precedente». Mínimos
  (ap. b): jornada ordinaria «no sea superior a nueve horas diarias ni inferior a cinco
  horas, salvo horarios de Fin de Semana»; descanso entre jornadas «de al menos doce
  horas»; máximo «cinco días» seguidos y «dos días como mínimo de descanso
  consecutivo», a ser posible sábado y domingo; procesos productivos especiales de
  menos de siete días (Navidad, Fin de Año, Virgen de la Cabeza, Gala 28-F,
  Carnavales, Ferias) con cómputo semanal de 35 horas y exceso pagado en descanso o
  «al módulo de 17,17 € brutos/hora»; de más de siete y menos de quince días (Semana
  Santa, Carnavales, Rocío, Ferias), cómputo bisemanal «a razón de 70 horas»; permuta
  de turnos entre dos trabajadores con aprobación de la empresa (negativa «motivada
  por escrito»); rotación de turnos sin acuerdo, «máxima de tres meses»; quien trabaje
  la jornada completa entre las 22,00 y las 7,00 horas no puede tener turno «superior
  a siete horas». Modalidades (ap. c): partido (separación «mínima […] de una hora y
  máxima de dos»), continuado (con «descanso de veinte minutos computable […] como
  tiempo real de trabajo») y fin de semana («once horas el sábado, once horas el
  domingo y cinco horas el viernes o el lunes»; sin acuerdo, rotatorio «por períodos
  semestrales» con cuatro criterios en orden: circunstancias familiares y personales,
  estudios acreditados, antigüedad en la empresa, antigüedad en el grupo).
- **Art. 13, vacaciones**: «veinticuatro días laborables de vacaciones (excluidos
  sábados)» (DT 2ª: «22 días hábiles, sin computar los sábados», con hasta 5 sueltos
  acumulables a asuntos propios). Se retribuyen con el salario base más la media de
  los complementos del último semestre (referencia, agosto). Se disfrutan «en los
  meses de verano (julio, agosto y septiembre […]) preferentemente en los meses de
  julio y agosto». Si la empresa las desplaza fuera de ese período, compensación «del
  12% del salario base mensual, más tres días hábiles de vacaciones». Si las pide el
  trabajador entre octubre y junio, «prima de tres días hábiles». Fraccionables «en un
  máximo de dos períodos, sin que ninguno de ellos sea inferior a siete días
  naturales». Turnos fijados «como mínimo, con tres meses de antelación», con
  preferencia de quienes tengan responsabilidades familiares y rotación anual. Se
  interrumpen por baja de enfermedad común, accidente no laboral, enfermedad
  profesional, riesgo en embarazo o lactancia o permiso de maternidad/paternidad.
- **Art. 14, horas extra**: siempre compensadas en descanso: «por cada hora
  extraordinaria realizada el/la trabajador/a tendrá derecho a un descanso
  compensatorio de dos horas»; se descansan en febrero, junio y octubre (las hechas
  hasta el 1 de cada uno de esos meses); compromiso de contratar «el 50% de las horas
  extraordinarias descansadas» (suspendido por la DT 1ª C); «los diez primeros
  minutos» no computan, la primera media hora se abona entera en descanso y «a partir
  del minuto 31» se paga el tiempo real.

### Capítulo III. Provisión de plazas y promoción (arts. 15-20)

- **Art. 15**: el personal fijo solo por «pruebas de admisión y/o concursos»
  convocados por el Director General de la RTVA «de acuerdo con el Consejo de
  Administración». Orden de provisión de vacantes o plazas nuevas: «a) Reingreso de
  excedencia. b) Traslado. c) Promoción. d) Concurso oposición libre.» La Mesa de
  Contratación participa «hasta la constitución de los tribunales».
- **Art. 16**: los excedentes voluntarios pueden pedir su incorporación «previo a la
  realización del traslado, promoción y concurso».
- **Art. 17, traslado**: fijos que quieran cambiar de localidad «sin cambio de puesto
  de trabajo» con antigüedad «de al menos un año»; plazo mínimo de solicitudes de
  «diez días naturales»; resuelve el Tribunal del art. 20 por nivel de conocimiento y
  titulación, circunstancias profesionales y antigüedad en el puesto y destino.
- **Art. 18, promoción**: fijos que quieran cambiar de grupo, con capacidad,
  conocimiento, titulación y antigüedad «de al menos seis meses»; plazo mínimo de
  «diez días naturales»; «mediante concurso de méritos, una vez efectuado el
  correspondiente concurso de traslado».
- **Art. 19, concurso-oposición libre**: para lo no cubierto en las fases de los
  arts. 16 a 18; pueden optar también los trabajadores «en situación de activo o
  excedente»; la convocatoria fija vacantes, puesto, nivel, requisitos, temarios y
  pruebas.
- **Art. 20, tribunales**: «Seis miembros en representación de RTVA y SS.FF.» (uno
  presidente y otro secretario) y «Cinco representantes nombrados por la
  representación de los/las trabajadores/as, preferentemente de igual o superior grupo
  profesional»; **seis funciones** (a-f); puede incorporar asesores especialistas.

### Capítulo IV. Organización (arts. 21-24)

- **Art. 21.1, movilidad funcional** dentro del mismo grupo, sin cambio de localidad,
  sin más límite que las titulaciones; no reduce el total de puestos y exige formación
  previa.
- **Art. 21.2, ascenso y promoción**: principio de «aptitud y capacidad»; «único
  sistema» el del convenio; la nueva retribución se devenga desde que se desempeñan
  las funciones. Funciones de nivel superior: diferencia retributiva mientras dure,
  situación que «nunca tendrá una duración superior a un año, salvo aquellas
  excepciones que determine la Mesa de Contratación», «sin que en ningún caso
  adquiera su pertenencia al grupo profesional superior». Registro de cambios de grupo
  en enero (ap. 2.6; véase la DA 1ª del Reglamento de la Mesa, apartado 1.4).
- **Art. 21.3, movilidad geográfica**. A) Traslados forzosos indefinidos: antes, «se
  agotará la vía de la voluntariedad»; si exigen cambio de residencia: «Indemnización
  equivalente a tres mensualidades del salario base», gastos de traslado y «Abono de
  240,40 € mensuales, como ayuda a vivienda»; notificación «con al menos treinta días»,
  negociación en los quince siguientes; opción entre traslado o extinción indemnizada;
  incorporación en plazo no inferior a «treinta días naturales»; derecho del cónyuge o
  conviviente de la empresa a trasladarse si hay vacante de su grupo; sin acuerdo,
  recurso a la COMVI en cinco días (que resuelve en diez) y mediación del CEMAC o del
  SERCLA; la decisión «no resultará ejecutiva hasta que no concluya la mediación»; la
  plaza que se deja no se cubre en «dos años». **Tres excepciones** (ap. 3.7):
  trabajadores de «cuarenta y ocho o más años», traslado por motivos disciplinarios y
  representantes legales «hasta pasado dos años desde el cese». Criterios (ap. 3.8):
  plaza más cercana, menor antigüedad y, a igualdad, menos cargas familiares y no estar
  estudiando. B) Desplazamientos temporales «hasta el límite de un año»; si superan
  tres meses, «cuatro días laborables» en el domicilio de origen «por cada tres
  meses»; agotados los doce meses, no se puede repetir en «cuatro años».
- **Art. 22, permuta**: entre dos fijos «de igual puesto de trabajo», aunque presten
  servicios en distintas empresas.
- **Art. 23, período de prueba**: «el que señale la normativa legal vigente en cada
  momento»; computa como antigüedad; se puede desistir «sin necesidad de preaviso»; la
  rescisión se comunica a la representación.
- **Art. 24, Mesa de Contratación**: reglamento propio (bolsas, acceso,
  contrataciones); la empresa puede contratar directamente, fuera de bolsas, «hasta un
  10% de la contratación media anual»; «cinco representantes del Comité Intercentros y
  cinco de la Dirección».

### Capítulo V. Seguridad y salud (arts. 25-31)

- **Art. 25**: comités de seguridad y salud en los centros «que cuenten con 50 ó más
  trabajadores/as», con las competencias del art. 39 de la Ley 31/1995.
- **Art. 26**: composición del art. 38 de esa ley, pero los delegados de prevención
  pueden ser trabajadores no representantes con «una formación mínima de 40 horas»;
  reunión «al menos una vez al mes»; «20 horas retribuidas al mes», acumulables «como
  máximo en cada trimestre».
- **Art. 27, Comité Intercentros de Seguridad y Salud Laboral**: al amparo del art.
  38.3 de la Ley 31/1995, sede en San Juan de Aznalfarache; «un máximo de 7 miembros»
  por los trabajadores, designados por el Comité Intercentros entre los delegados de
  prevención, e igual número por la empresa.
- **Arts. 28-29**: evaluaciones de riesgos por puesto conforme a los arts. 3 a 7 del
  Real Decreto 39/1997; planificación anual (arts. 8 y 9); descanso de «diez minutos
  por cada hora de trabajo continuado en pantallas de visualización de datos», no
  acumulable; programa de drogodependencias; terapia de espalda «en un 75% en tiempo
  de trabajo y en un 25% fuera».
- **Art. 30**: prendas homologadas; el Comité de Salud Laboral fija las de cada puesto
  «anualmente».
- **Art. 31**: unidad básica de salud laboral en localidades con «más de 100
  trabajadores/as», dirigida por médico del trabajo.

### Capítulo VI. Régimen de personal (arts. 32, 34-36; el 33 va en el apartado 3)

- **Art. 32, excedencias**: además de las del ET («que se aplicarán en sus propios
  términos»), concesión «obligatoria» a quien tenga «al menos un año de antigüedad» y
  la pida con «treinta días» de antelación. **Tres modalidades**:
  - I. **Voluntaria**: concesión en «treinta días», duración «no […] inferior a seis
    meses ni superior a diez años», prorrogable con aviso de treinta días sin superar
    diez años; para otra, «tres años de servicio efectivo». **Con reserva de puesto**
    si no pasa de «tres años» y se cumplen tres requisitos: no ir a otra emisora ni a
    proveedores de RTVA; que los excedentes con reserva no superen «el 5%» de la
    plantilla; que no perjudique gravemente la actividad. En los demás casos, solo
    derecho preferente al reingreso. Se pierde el reingreso si no se pide «con 15 días
    de antelación» al vencimiento (extinción automática); incorporación «dentro de los
    dos meses»; el tiempo «no computará a ningún efecto».
  - II. **Forzosa**: cargo público no permanente; funciones sindicales de ámbito
    provincial o superior; duración, la del mandato; reincorporación «en los treinta
    días siguientes al cese»; mismas garantías para cooperación con el «Tercer Mundo» o
    labor humanitaria.
  - III. **Especial**: cuidado de hijos, «no superior a seis años» por cada hijo
    (desde el fin de la licencia de embarazo o de adopción); si padre y madre están en
    el convenio, «solamente uno de ellos»; computa para antigüedad; reingreso «en
    cualquier momento». También el nombramiento de libre designación en RTVA y la
    privación de libertad (excedencia «en el plazo de treinta días» tras condena y
    reingreso en «dos meses» desde la libertad).
- **Art. 34**: plantilla actualizada «al uno de Enero», con **siete datos** (nombre,
  antigüedad, grupo, puesto, nivel, fecha de nombramiento o promoción y número de
  registro), publicada «en los tres primeros meses del año».
- **Art. 35**: computa como antigüedad el tiempo trabajado antes de las oposiciones
  si no hubo interrupción «superior a seis meses».
- **Art. 36, formación**: Comisión de Formación paritaria de «al menos […] diez
  miembros, cinco» y cinco; **tres objetivos** (actualizar, especializar, idiomas);
  el plan es obligatorio solo si la empresa lo subvenciona «totalmente» y se hace
  «dentro del horario de trabajo»; el trabajo en prácticas «no será nunca utilizado».

### Capítulo VII. Prestaciones sociales (arts. 37-44)

- **Art. 37**: «180,30 euros anuales» por hijo hasta los cuatro años (contrato
  «superior a seis meses» en el año) y «150,25 euros anuales» de cinco a 18; pago
  «en una sola vez en el mes de agosto»; hijos con discapacidad, «96,00 euros
  mensuales» hasta «los cuarenta años inclusive». DT 8ª: acción social suspendida
  «salvo las de atención a personas con discapacidad».
- **Art. 38**: becas por la cantidad que determine la COMVI.
- **Art. 39, seguro colectivo**: muerte natural «15.025 €»; invalidez permanente total
  «27.046 €»; absoluta «39.066€»; fallecimiento en accidente «27.046 €»; en accidente
  de circulación «39.066 €».
- **Art. 40**: complemento de IT hasta «el cien por cien de su retribución ordinaria
  desde el primer día» (DT 6ª: 50 % días 1-3, 75 % días 4-20, 100 % desde el 21 en
  enfermedad común; 100 % en contingencias profesionales, hospitalización o
  intervención); complemento de maternidad hasta el salario.
- **Art. 41**: vales de comida para entradas entre «las 12 y 15 horas» o «las 19 y 22
  horas» (o salidas desde las 16 y 23); comedor en centros de más de 100; o en metálico
  «11,33 €».
- **Art. 42**: anticipo de la nómina hasta «el 90%» de la última mensualidad, con
  «seis meses de antigüedad», a devolver «hasta tres meses»; anticipo personal de
  «tres mensualidades netas», sin interés, «en 18 meses».
- **Art. 43**: acuerdo anual con el Grupo de Empresa.
- **Art. 44, jubilaciones**: indemnización por jubilación B01 «21.035,42 €», B02
  «19.532,89 €», B03 «18.030,36 €», B04 «16.527,83 €», B05 «15.025,30 €»; jubilación
  anticipada con «al menos cinco años de antigüedad», escalas por años de anticipación
  (1 a 5; p. ej. B01 de «24.040,48 €» a «36.060,73 €»); comisión para incentivar bajas
  entre «57 y 59 años» con «150.000 euros anuales»; aportaciones al plan de pensiones
  +5 % (B01 «373,35 €» … B05 «266,68 €»). En 2026 sigue aplicándose el art. 28.2 de la
  Ley 3/2012, que prohíbe aportar a planes de pensiones (apartado 1.5).

### Capítulo VIII. Trabajo y retribución (arts. 45-54)

- **Art. 45, clasificación profesional**: grupos y puestos en **cinco niveles
  salariales, B01 a B05** (p. ej. B01 jefes de departamento, letrado, auditor; B02
  realizador, redactor, documentalista, técnico superior informático, titulado
  superior; B03 jefes de sección, operador de sonido, cámara, ayudante de realización,
  productor, grafista, titulado medio; B04 administrativo, locutor de continuidad,
  guionista, operador montador de vídeo, ayudante de producción; B05 auxiliar
  administrativo, auxiliar de servicios generales, sastra/sastre, gruista).
- **Art. 46**: Comisión permanente de Valoración de Puestos, en «1 mes», de «cinco» y
  «cinco»; las definiciones de puestos, en la DA 8ª (Anexo III).
- **Art. 47**: estructura: A) salario base; B) complementos: personales
  (antigüedad), de puesto (nocturnidad, quebranto de moneda, mando orgánico, especial
  responsabilidad, disponibilidad, turnicidad, polivalencia, guardia localizable, plus
  de sábados, domingos y festivos, idioma, penosidad y peligrosidad), por calidad y
  cantidad (calidad, procesos productivos especiales, horas extra, pacto de trabajo),
  de vencimiento superior al mes (pagas de junio, Navidad, marzo y septiembre) y
  extrasalariales (dietas, kilometraje, plus de pernocta).
- **Art. 48**: salario base del Anexo I para 2013, revisable según la DA 1ª.
- **Art. 49, antigüedad**: trienios «sin tope limitativo», a razón de «0,0024 del
  salario base anual fijado para el nivel B03»; los temporales cobran antigüedad si
  la interrupción no supera «180 días»; se devengan desde «el día 1 del mes» en que se
  cumplen. DT 5ª: «45 € trienio/mes» lineal.
- **Art. 50, complementos de puesto**: nocturnidad «35% del salario base» (período
  nocturno «entre las 22.00 horas y las 7.00 horas»); sábados, domingos y festivos
  «59,46 euros» (entero si la jornada supera tres horas), y «128,06 euros» por
  tarde/noche del 24 y 31 de diciembre o cualquier turno del 25 de diciembre y 1 de
  enero; quebranto de moneda «35,36 euros mensuales»; mando orgánico «30%»; especial
  responsabilidad «30% o el 45%» (el del 45 % es incompatible con horas extra pagadas y
  con turnicidad); disponibilidad «30%» (más de quince días al mes) o «15%» (menos),
  incompatible con turnicidad; turnicidad «5%»; polivalencia «12%»; idiomas «5%»;
  penosidad y peligrosidad «15%»; guardia localizable «1%» del salario base mensual
  en descanso y «2.5%» en sábado, domingo o festivo, con convocatoria mínima de
  «cuatro horas».
- **Art. 51**: calidad en el trabajo «15% o el 25%»; pacto de trabajo presentado al
  Comité Intercentros «como mínimo tres días antes».
- **Art. 52, pagas**: junio (del 25 al 30) y Navidad (del 15 al 20 de diciembre), de
  salario base más la media de complementos del semestre anterior; marzo y septiembre
  (del 25 al 30), de «quince días de salario base más antigüedad», más «300,51 euros»
  en marzo y «750 euros» en septiembre.
- **Art. 53, dietas**: en España, «55,52» €/día (comida y cena), media dieta «27,76»,
  con alojamiento a cargo del trabajador «101,12 euros»; en el extranjero, «98,81»,
  media «49,41», sin alojamiento concertado «197,62»; dieta de rodaje a más de «30
  kilómetros» con regreso después de las 16:00 o las 23:00; kilometraje «0,27 euros por
  kilómetro»; plus de pernocta fuera de Andalucía «69,09 euros», que compensa «las
  cuatros primeras horas extraordinarias», si la jornada se prolonga «más de dos
  horas». DT 7ª: tope del Decreto 54/1989 (vigente en 2026 por el art. 22 de la Ley
  3/2012).
- **Art. 54**: cantidades brutas.
- **Anexo I** (2013), salario base mensual: B01 «2.279,07 €», B02 «2.057,14 €», B03
  «1.835,21 €», B04 «1.613,18 €», B05 «1.391,16 €»; total anual B01 «35.236,56 €» …
  B05 «21.917,91 €»; incremento anual según la Ley de Presupuestos (DA 1ª y nota del
  Anexo I), con el límite de masa salarial de la DA 9ª. Para 2026, la Ley 8/2025, art.
  18.1: «la masa salarial del personal laboral al servicio del sector público andaluz
  no experimentará crecimiento respecto de su cuantía a 31 de diciembre de 2025, sin
  perjuicio de la aplicación de lo dispuesto en el artículo 12.2».

### Capítulo IX. Acción sindical (arts. 55-62)

- **Art. 55**: delegados de personal en centros de menos de 50 («De 6 a 30 […]: 1»;
  «De 31 a 49 […]: 3»), con «28 horas» de licencia al mes.
- **Art. 56**: comité de empresa de «5 miembros» (50-100), «9» (100-250), «13»
  (251-500); crédito de «30 horas/mes» (50-250) o «45 horas/mes» (251 en adelante),
  acumulable «en cómputo anual por candidatura»; no computan las reuniones convocadas
  por la empresa ni la negociación del convenio.
- **Art. 57**: competencias del comité (información trimestral y anual, modelos de
  contrato, vigilancia, capacidad procesal «por decisión mayoritaria»); reunión
  trimestral sobre contrataciones civiles.
- **Art. 58, Comité Intercentros**: al amparo del «artículo 63.3» del ET de 1995;
  sede en San Juan de Aznalfarache; «máximo de trece miembros», procurando «cinco» de
  Sevilla, «dos» de Málaga y «seis» de Almería, Cádiz, Córdoba, Granada, Huelva y
  Jaén; competencia exclusiva en lo que afecte a más de un centro.
- **Art. 60**: sección sindical con garantías si obtiene el «15%» de los votos (centros
  de 50 a 100) o el «10%» (101 en adelante).
- **Art. 61**: un delegado sindical por sección; «30 horas/mes» o «45 horas/mes».
- **Art. 62, asambleas**: dentro de la jornada «hasta un máximo de ocho horas
  anuales»; a petición del «30%» de la plantilla del centro; preaviso de «48 horas»,
  reducible a «24 horas».

### Capítulo X. Régimen disciplinario (arts. 63-72)

- **Art. 63**: no es indisciplina negarse a órdenes contrarias al convenio o al
  ordenamiento; nadie puede ser despedido por toxicomanía «salvo que éstas repercutan
  gravemente».
- **Art. 64**: faltas «leves, graves y muy graves», según «importancia, trascendencia y
  malicia».
- **Art. 65**: **13 faltas leves** (p. ej. impuntualidad de más de diez y menos de
  treinta minutos, o tres retrasos de menos de diez minutos «durante un período de dos
  meses consecutivos»; no avisar la ausencia en las «dos primeras jornadas» ni mandar
  el parte en «los ocho primeros días»; «Fumar en cualquier lugar o dependencia no
  autorizada»).
- **Art. 66**: **18 faltas graves** (entre ellas, «La reiteración o reincidencia en
  tres faltas leves […] dentro del período de tres meses»; la falta de respeto «ante el
  micrófono o en actos públicos»; no declarar una segunda actividad incompatible).
- **Art. 67**: **20 faltas muy graves** (entre ellas, «La tercera falta grave en un
  período de noventa días naturales»; la reiteración en falta grave sancionada «en un
  período de seis meses»; acoso sexual y acoso moral, definidos).
- **Art. 68, abuso de autoridad**: acto arbitrario de un jefe o de un trabajador de
  grupo superior; la empresa «abrirá expediente».
- **Art. 69, sanciones máximas**: leves, amonestación verbal, escrita o «Suspensión de
  empleo y sueldo de un día»; graves, «de dos a veinte días»; muy graves, «de veintiuno
  a sesenta días» o «Despido con pérdida de todos los derechos».
- **Art. 70**: las suspensiones por faltas graves o muy graves no se cumplen si se
  acredita haber demandado; se ejecutan tras la sentencia.
- **Art. 71**: prescripción, «en los términos que establece el artículo 60.2 del
  Estatuto de los Trabajadores» (ET 2015, art. 60.2, redacción única: leves «a los diez
  días», graves «a los veinte días», muy graves «a los sesenta días» desde que la
  empresa las conoce «y, en todo caso, a los seis meses de haberse cometido»).
- **Art. 72, procedimiento**: pliego de cargos por escrito para graves y muy graves;
  alegaciones en «cuatro días hábiles»; informe del Comité de Empresa o delegado en
  «cinco días hábiles»; resolución de la Dirección.

### Capítulo XI. Incompatibilidades y garantías procesales (arts. 73-74)

- **Art. 73**: incompatible con cualquier actividad que menoscabe los deberes; no se
  puede trabajar para proveedores de RTVA; incompatibilidad expresa con otras empresas
  de radiodifusión, agencias, prensa, publicidad, electrónica profesional, cine,
  discográficas y espectáculos, salvo colaboración esporádica autorizada por el
  «Director/a Gerente de la RTVA, una vez oído el Comité de Empresa».
- **Art. 74**: defensa jurídica, costas y fianzas a cargo de la empresa para el
  personal procesado o demandado «por razón de su trabajo», «con derecho a libre
  elección de abogado/a y procurador/a».

### Disposiciones adicionales (lo que no se ha dicho antes)

DA 2ª: desconexiones provinciales (cuatro operadores montadores de vídeo rotatorios
con especial responsabilidad del «30%», no consolidable). DA 3ª: bonificación fiscal
para hijos en edad de guardería. DA 4ª: no externalizar la gestión de la IT por
contingencias comunes. DA 5ª: vigilancia de los convenios de las contratas; la
contratación con empresas de trabajo temporal, «negociada». DA 6ª: secreto
profesional, «cláusula de conciencia y derecho de autor». DA 7ª: la externalización
no puede mermar «la plantilla estructural actual». DA 10ª: negociar planes de
igualdad «Dentro de los 6 meses siguientes».

## 5. Lo que no he podido confirmar, erratas del texto y choques con el ET vigente

### 5.1. No confirmado

- **Cómo se aplican hoy** jornada, vacaciones, asuntos propios, traslado de domicilio,
  IT y acción social en RTVA-CSRTV, después de que la Ley 7/2024 derogara los arts. 26
  y 32 de la Ley 3/2012 y de que la Ley 8/2025 dejara de aplicar en 2026 sus arts. 14,
  23, 24, 25 y 28.1 (apartado 1.5). No hay acuerdo publicado; los dos documentos
  sindicales se contradicen. **El redactor debe dar el texto del convenio, el de las DT
  y el estado de la Ley 3/2012, sin afirmar cómo se aplica.**
- **El «cuadro de licencias y permisos» oficial** de la empresa (lo menciona CCOO en
  2025) no está publicado. Tampoco los acuerdos de la COMVI de 2016 que cita el cuadro
  sindical de 2017.
- **La fecha del Reglamento de la Mesa de Contratación**: el texto no la trae (la
  convocatoria dice 12-03-2026).
- **Si se ha denunciado el X Convenio** sin inscribirlo, o si se negocia un XI: nada
  publicado.
- **Tablas salariales posteriores a 2013**: no hay ninguna publicada ni inscrita. Las
  cuantías del Anexo I y de los arts. 37, 41, 50 y 53 son las de 2013. No puedo decir
  las de hoy.
- **DT 4ª** (art. 11.5 de la Ley de Presupuestos de 2013; jubilación parcial): no he
  comprobado qué queda en 2026.

### 5.2. Erratas y remisiones del propio texto (manda el texto, pero el redactor debe saberlo)

- **Art. 66.3**: «La alegación de motivos falsos para la obtención de las licencias a
  que se refiere el **artículo 27** de este Convenio». Las licencias están en el **art.
  33**; el 27 es el Comité Intercentros de Seguridad y Salud Laboral. Remisión errónea
  (seguramente arrastrada de otra numeración).
- **Art. 21.3.6.a**, dentro del art. 21: «con los efectos previstos en el artículo 21»
  (se remite a sí mismo).
- **Art. 58.1** y la resolución de publicación citan el **Real Decreto Legislativo
  1/1995** (ET de 1995), derogado. Hoy el comité intercentros está en el art. 63.3 del
  ET de 2015, con el mismo tope: «Solo por convenio colectivo podrá pactarse la
  constitución y funcionamiento de un comité intercentros con un máximo de trece
  miembros».
- **Art. 71** remite al «artículo 60.2 del Estatuto de los Trabajadores»: el número
  coincide en el ET de 2015 (redacción única).
- Rúbricas distintas entre índice y cuerpo: apartado 2.
- **DT 3ª B**: el epígrafe dice «Días de asuntos propios», pero el texto dice «Las
  Licencias y permisos regulados en el art. 33 […] quedan en suspenso y pasan a ser
  exclusivamente de un total de 4 días al año». Leído literalmente, suspende todo el
  art. 33. El cuadro sindical de 2017 y el propio epígrafe lo leen como si se refiriera
  solo a los asuntos propios. **Ambigüedad del texto; no la resuelvo.**

### 5.3. Donde el ET vigente dice otra cosa (textos a la vista, sin conclusiones mías)

El art. 6 del convenio da prioridad a sus normas «respecto a cualquier otra disposición
o norma legal». El ET vigente fija mínimos que no casan con algunas cifras de 2014.
Pongo solo los casos en que la diferencia **está escrita** en el ET (BOE-A-2015-11430,
leído el 24-09-2026; art. 37 con 15 redacciones, la vigente desde 3-3-2025 por la Ley
6/2024; art. 48 vigente desde 31-7-2025 por el Real Decreto-ley 9/2025, convalidado por
Resolución del Congreso de 9-IX-2025, BOE-A-2025-17999; art. 46 vigente desde
30-6-2023; art. 38 con redacción única).

| Convenio (2014) | ET vigente |
|---|---|
| 33.A.1.b: «3 días naturales» (5 con desplazamiento) por enfermedad grave u hospitalización o fallecimiento hasta 2.º grado | 37.3.b: «Cinco días por accidente o enfermedad graves, hospitalización o intervención quirúrgica sin hospitalización que precise reposo domiciliario del cónyuge, pareja de hecho o parientes hasta el segundo grado […] así como de cualquier otra persona […] que conviva con la persona trabajadora»; 37.3.b bis: «Dos días por el fallecimiento […]. Cuando con tal motivo la persona trabajadora necesite hacer un desplazamiento al efecto, el plazo se ampliará en dos días.» |
| 33.A.1.a: «20 días naturales en caso de matrimonio»; F: parejas de hecho con «convivencia de al menos seis meses» | 37.3.a: «Quince días naturales en caso de matrimonio o registro de pareja de hecho.» |
| 33.A.1.c: 2 días por traslado de domicilio (DT 3ª: 1) | 37.3.c: «Un día por traslado del domicilio habitual.» |
| 33.A.1.d: deber inexcusable «de carácter público o personal» | 37.3.d: deber inexcusable «de carácter público y personal, comprendido el ejercicio del sufragio activo» |
| 33.A.1.g: lactancia de hijo «menor de doce meses»; acumulación «por decisión de la madre»; si los dos trabajan en la empresa «sólo uno podrá hacer uso de este derecho» | 37.4: hora de ausencia «hasta que este cumpla nueve meses» (hasta doce si ambos lo ejercen «con la misma duración y régimen», con reducción de salario desde los nueve); «Quien ejerza este derecho, por su voluntad, podrá sustituirlo por una reducción de su jornada en media hora con la misma finalidad o acumularlo en jornadas completas»; «constituye un derecho individual de las personas trabajadoras sin que pueda transferirse su ejercicio»; la empresa solo puede limitar el ejercicio simultáneo «por razones fundadas y objetivas […] debidamente motivadas por escrito», ofreciendo «un plan alternativo» |
| 33.A.1.b (2.º párr.): prematuros, ausencia «hasta un máximo de 2 horas diarias, percibiendo las retribuciones íntegras» | 37.5: ausencia de «una hora» y reducción «hasta un máximo de dos horas, con la disminución proporcional del salario» (el convenio mejora) |
| 33.A.1.h: suspensión de «dieciséis semanas» | 48.4: nacimiento, «diecinueve semanas» para la madre biológica y para el otro progenitor («treinta y dos» en monoparentalidad); 48.5: adopción, guarda y acogimiento, «diecinueve semanas para cada adoptante, guardador o acogedor» |
| 33.A.1.i: padre u otro progenitor, «15 días consecutivos» | 48.4: el progenitor distinto de la madre biológica, «diecinueve semanas»; «Este derecho es individual de la persona trabajadora sin que pueda transferirse su ejercicio al otro progenitor» |
| 33.A.1.h (último párr.): «En caso de fallecimiento de la madre […], el otro progenitor podrá hacer uso de la totalidad o […] de la parte que reste» | 48.4: «En caso de fallecimiento de uno de los progenitores, el otro progenitor podrá hacer uso de la totalidad o, en su caso, de la parte que reste de permiso.» |
| 33.A.1.n: hijo con cáncer, «como máximo, hasta que el menor cumpla los 18 años», y «siempre que ambos progenitores […] trabajen» | 37.6 (3.er párr. y ss.): «como máximo, hasta que el hijo […] cumpla los veintitrés años»; hasta los 26 con discapacidad «igual o superior al 65 por ciento» |
| 33.D.2: guarda legal de menor de doce años o «disminuido/a»; familiar hasta 2.º grado; la empresa limita el ejercicio simultáneo «por razones justificadas» | 37.6: menor de doce años o «persona con discapacidad»; incluye «cónyuge o pareja de hecho» y el familiar consanguíneo de la pareja de hecho; limitación solo «por razones fundadas y objetivas […] motivadas por escrito», con «plan alternativo» |
| 33.A.1.m: solo violencia de género | 37.8: «víctimas de violencia de género, de violencia sexual o de víctimas del terrorismo», con derecho también a trabajo a distancia |
| (no está) | 37.3.f: sesiones de información y preparación e informes previos a la idoneidad en adopción, guarda o acogimiento; 37.3.g: hasta cuatro días por imposibilidad de acceder al centro por catástrofe o riesgo grave; 37.3.g [sic]: actos preparatorios de la donación de órganos; 37.9: ausencia por fuerza mayor familiar, retribuidas «las horas […] equivalentes a cuatro días al año» |
| 32.III.1: excedencia por cuidado de hijos «no superior a seis años»; si padre y madre están en el convenio, «solamente uno de ellos podrá ejercer este derecho» | 46.3: «no superior a tres años» (el convenio mejora); «constituye un derecho individual»; la empresa solo puede limitar el ejercicio simultáneo por razones «fundadas y objetivas […] motivadas por escrito», con plan alternativo. Además, excedencia por cuidado de familiar «no superior a dos años», que el convenio no regula (pero su art. 32 remite a las del ET «en sus propios términos») |
| 32.I: voluntaria, «no […] inferior a seis meses ni superior a diez años»; otra, tras «tres años de servicio efectivo» | 46.2: «por un plazo no menor a cuatro meses y no mayor a cinco años»; otra vez, «si han transcurrido cuatro años desde el final de la anterior». (El art. 32 del convenio suma sus excedencias a las del ET.) |
| 13.7: interrupción de las vacaciones por IT y maternidad/paternidad | 38.3: si coinciden con IT por embarazo, parto o lactancia o con las suspensiones del art. 48.4, 48.5 y 48.7, derecho a disfrutarlas después «aunque haya terminado el año natural»; por otras IT, siempre que no hayan pasado «más de dieciocho meses a partir del final del año» |
| 14: horas extra sin tope anual | 35.2: «no podrá ser superior a ochenta al año» (el ET es el límite; el convenio no lo contradice, lo calla) |

Coinciden (sin choque): 12.b.2 y ET 34.3 (doce horas entre jornadas); 23 (período de
prueba «el que señale la normativa legal vigente») y ET 14; 71 y ET 60.2.

Lo que **no** he hecho: decidir qué prevalece en cada caso (eso es doctrina sobre la
relación ley-convenio y no la he leído en un precepto). Solo pongo los dos textos.
