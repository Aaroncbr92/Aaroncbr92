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

