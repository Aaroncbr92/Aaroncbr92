# T03 · Investigación · La Unión Europea, el Tratado de la Unión Europea y la Carta

Fase 1 (investigar). Parte asignada: primera y segunda rúbricas del punto 3, es decir, «La Unión Europea. Tratado de la Unión Europea y Carta de derechos fundacionales». La representación de la Junta ante la Unión Europea **no** es mía. Todo se leyó el **24-09-2026**. Siglas: Unión Europea (UE); Tratado de la Unión Europea (TUE); Tratado de Funcionamiento de la Unión Europea (TFUE); Carta de los Derechos Fundamentales de la Unión Europea (la Carta); Diario Oficial de la Unión Europea (DOUE); Convenio Europeo para la Protección de los Derechos Humanos y de las Libertades Fundamentales (CEDH); Tribunal de Justicia de la Unión Europea (TJUE); Banco Central Europeo (BCE).

---

## 0. Premisas que no cuadran con la fuente, y avisos para el redactor

1. **Posible errata del BOJA en el enunciado.** El programa dice «**Carta de derechos fundacionales**» (transcrito así en `convocatoria/canal-sur/PROGRAMA-COMUN.md`, punto 3). En el DOUE el texto se titula «**CARTA DE LOS DERECHOS FUNDAMENTALES DE LA UNIÓN EUROPEA**» (2016/C 202/02), y así la nombra el art. 6.1 TUE. No existe una «Carta de derechos fundacionales». El epígrafe del tema debe reproducir el enunciado tal cual, y el cuerpo debe explicar la errata. No he cotejado el enunciado con el PDF del BOJA núm. 186, solo con la transcripción del proyecto.
2. **La versión consolidada vigente es de 2016, y no está al día del Brexit.** Es la última que ha publicado el DOUE (véase el § 1). En ella **el art. 52.1 TUE sigue enumerando «al Reino Unido de Gran Bretaña e Irlanda del Norte»** entre los Estados a los que se aplican los Tratados. El Protocolo n.º 30 habla todavía de «Polonia y el Reino Unido». Con la lista del art. 52.1 no se puede contar a los Estados miembros de hoy. La salida del Reino Unido se hizo por el art. 50, pero el acuerdo de retirada **no lo he leído**, así que ni la fecha ni el procedimiento seguido quedan confirmados en fuente.
3. **Hay cifras del TUE que el derecho derivado ha desplazado, y el tema debe dar las dos:**
   - Parlamento Europeo. El art. 14.2 TUE fija un máximo de «**setecientos cincuenta, más el Presidente**». La Decisión (UE) 2023/2061 del Consejo Europeo (DO L 238, de 27-IX-2023) reparte para la legislatura **2024-2029** un total de **720** escaños (suma de su art. 3, comprobada), **61 para España**.
   - Comisión. El art. 17.5 TUE prevé, desde el 1-XI-2014, «**los dos tercios del número de Estados miembros**», «**a menos que el Consejo Europeo decida por unanimidad modificar dicho número**». La Decisión 2013/272/UE (DO L 165, de 18-VI-2013) dice en su art. 1: «**La Comisión estará compuesta por un número de miembros igual al número de Estados miembros, que incluirá a su Presidente y al Alto Representante**». Los metadatos de la Oficina de Publicaciones la dan en vigor y sin actos que la modifiquen (consulta del 24-09-2026).
   - Abogados generales del Tribunal de Justicia. El art. 252 TFUE dice «**ocho**». La Decisión 2013/336/UE del Consejo los aumenta a «**nueve, con efectos a partir del 1 de julio de 2013**» y a «**once, con efectos a partir del 7 de octubre de 2015**». En los metadatos no he podido confirmar si sigue en vigor.
4. **Preceptos transitorios ya agotados**, que el redactor no debe presentar como regla actual: art. 16.5 TUE (régimen transitorio de mayoría cualificada «hasta el 31 de octubre de 2014» y «entre el 1 de noviembre de 2014 y el 31 de marzo de 2017»); art. 17.4 TUE (la Comisión nombrada entre la entrada en vigor del Tratado de Lisboa y el 31-X-2014); art. 54.2 TUE (entrada en vigor «el 1 de enero de 1993»).
5. **El encargo menciona el art. 13 «y los de cada una» de las instituciones.** En el TUE solo cinco de las siete tienen artículo propio (arts. 14 a 19). Del BCE y del Tribunal de Cuentas el art. 13.3 TUE remite al TFUE. Por eso los he leído en el TFUE (arts. 282, 283, 285 y 286).

---

## 1. Fuentes y versión

- **TUE**: «VERSIÓN CONSOLIDADA DEL TRATADO DE LA UNIÓN EUROPEA», **DOUE C 202, de 7-VI-2016** (CELEX 12016M/TXT). Incluye protocolos, declaraciones y tablas de correspondencias. Fichero: `fuentes/canal-sur/documentos/tue-version-consolidada-doue-c202-2016.txt`.
- **Carta**: «CARTA DE LOS DERECHOS FUNDAMENTALES DE LA UNIÓN EUROPEA (2016/C 202/02)», **DOUE C 202, de 7-VI-2016, p. 389** (CELEX 12016P/TXT). Fichero: `carta-derechos-fundamentales-ue-doue-c202-2016.txt`.
- **TFUE**, del mismo DOUE (CELEX 12016E/TXT), solo para los arts. 20, 223, 231, 234, 238, 244, 251 a 254, 282, 283, 285, 286 y 354. Fichero: `tfue-version-consolidada-doue-c202-2016.txt`.
- **Decisión (UE) 2023/2061** del Consejo Europeo (composición del Parlamento Europeo), **Decisión 2013/272/UE** del Consejo Europeo (número de miembros de la Comisión) y **Decisión 2013/336/UE** del Consejo (abogados generales). Ficheros `decision-*.txt`.
- **Cómo se obtuvo.** La web de EUR-Lex responde 202 sin contenido a toda consulta automática (es un desafío anti-robots). He descargado el mismo documento del **repositorio de la Oficina de Publicaciones** (`publications.europa.eu/resource/celex/<CELEX>`, expresión en español, XHTML del DOUE) y lo he pasado a texto. Cada `.txt` lleva en cabecera la URL y la fecha. No hay PDF. `herramientas/doue.py` no sirve aquí: trabaja con documentos del BOE que reproducen el DOUE en su texto original, y el BOE no publica la versión consolidada.
- **¿Hay una versión consolidada posterior a 2016?** Consulté el punto SPARQL de la Oficina de Publicaciones buscando CELEX del sector 1 con descriptor M o P. El más reciente que devuelve es de **2016** (12016P054, fechado 2016-06-07). No hay ninguna consolidación posterior del TUE ni de la Carta.
- Todos los preceptos citados abajo se leyeron el **24-09-2026**. Los Tratados no tienen cadena de redacciones como el BOE: el texto es el de la versión consolidada de 2016, que integra el Tratado de Lisboa y la adhesión de Croacia.

---

## 2. Estructura del TUE

Preámbulo y **55 artículos** (recuento hecho sobre el texto) en **seis títulos**:

| Título | Rúbrica literal | Artículos |
|---|---|---|
| I | «DISPOSICIONES COMUNES» | 1-8 |
| II | «DISPOSICIONES SOBRE LOS PRINCIPIOS DEMOCRÁTICOS» | 9-12 |
| III | «DISPOSICIONES SOBRE LAS INSTITUCIONES» | 13-19 |
| IV | «DISPOSICIONES SOBRE LAS COOPERACIONES REFORZADAS» | 20 |
| V | «DISPOSICIONES GENERALES RELATIVAS A LA ACCIÓN EXTERIOR DE LA UNIÓN Y DISPOSICIONES ESPECÍFICAS RELATIVAS A LA POLÍTICA EXTERIOR Y DE SEGURIDAD COMÚN» | 21-46 (cap. 1: 21-22; cap. 2, secc. 1 «Disposiciones comunes»: 23-41; secc. 2 «Disposiciones sobre la Política Común de Seguridad y Defensa»: 42-46) |
| VI | «DISPOSICIONES FINALES» | 47-55 |

Datos de las disposiciones finales:

- Art. 47: «**La Unión tiene personalidad jurídica.**»
- Art. 51: «**Los Protocolos y Anexos de los Tratados forman parte integrante de los mismos.**»
- Art. 53: «**El presente Tratado se concluye por un período de tiempo ilimitado.**»
- Art. 54.1: ratificación y depósito «**ante el Gobierno de la República Italiana**».
- Art. 55.1: lista de lenguas. Hay **24** («alemana, búlgara, checa, croata, danesa, eslovaca, eslovena, española, estonia, finesa, francesa, griega, húngara, inglesa, irlandesa, italiana, letona, lituana, maltesa, neerlandesa, polaca, portuguesa, rumana y sueca»; el recuento es mío).
- Fórmula final: «**Hecho en Maastricht, el siete de febrero de mil novecientos noventa y dos.**»

Art. 1:

- **Párr. 1**: «las ALTAS PARTES CONTRATANTES constituyen entre sí una UNIÓN EUROPEA […] a la que los Estados miembros atribuyen competencias para alcanzar sus objetivos comunes».
- **Párr. 3**: «**La Unión se fundamenta en el presente Tratado y en el Tratado de Funcionamiento de la Unión Europea (en lo sucesivo denominados "los Tratados"). Ambos Tratados tienen el mismo valor jurídico. La Unión sustituirá y sucederá a la Comunidad Europea.**»

---

## 3. Valores y objetivos (arts. 2 y 3 TUE)

**Art. 2**: «**La Unión se fundamenta en los valores de respeto de la dignidad humana, libertad, democracia, igualdad, Estado de Derecho y respeto de los derechos humanos, incluidos los derechos de las personas pertenecientes a minorías. Estos valores son comunes a los Estados miembros en una sociedad caracterizada por el pluralismo, la no discriminación, la tolerancia, la justicia, la solidaridad y la igualdad entre mujeres y hombres.**» Son seis valores y seis rasgos de la sociedad (recuento mío).

**Art. 3**, seis apartados:

- 3.1: «**La Unión tiene como finalidad promover la paz, sus valores y el bienestar de sus pueblos.**»
- 3.2: espacio de libertad, seguridad y justicia «**sin fronteras interiores**», con libre circulación de personas y medidas sobre fronteras exteriores, asilo, inmigración y delincuencia.
- 3.3: «**La Unión establecerá un mercado interior.**» Desarrollo sostenible basado en «**un crecimiento económico equilibrado y en la estabilidad de los precios, en una economía social de mercado altamente competitiva, tendente al pleno empleo y al progreso social**» y en la protección del medio ambiente. También combatirá la exclusión social y la discriminación, fomentará la cohesión «**económica, social y territorial**» y «**respetará la riqueza de su diversidad cultural y lingüística y velará por la conservación y el desarrollo del patrimonio cultural europeo**».
- 3.4: «**La Unión establecerá una unión económica y monetaria cuya moneda es el euro.**»
- 3.5: relaciones con el resto del mundo, incluido «**el respeto de los principios de la Carta de las Naciones Unidas**».
- 3.6: «**La Unión perseguirá sus objetivos por los medios apropiados, de acuerdo con las competencias que se le atribuyen en los Tratados.**»

**Art. 4** (relación con los Estados):

- 4.1: «toda competencia no atribuida a la Unión en los Tratados corresponde a los Estados miembros».
- 4.2: respeto de la «identidad nacional […] también en lo referente a la autonomía local y regional»; «**la seguridad nacional seguirá siendo responsabilidad exclusiva de cada Estado miembro**».
- 4.3: «**principio de cooperación leal**».

**Art. 7** (protección de los valores del art. 2):

- 7.1, riesgo claro de violación grave. Propuesta motivada «**de un tercio de los Estados miembros, del Parlamento Europeo o de la Comisión**». Decide el Consejo, «**por mayoría de cuatro quintos de sus miembros y previa aprobación del Parlamento Europeo**».
- 7.2, violación grave y persistente. Decide el **Consejo Europeo**, «**por unanimidad y a propuesta de un tercio de los Estados miembros o de la Comisión y previa aprobación del Parlamento Europeo**».
- 7.3, suspensión de derechos, «incluidos los derechos de voto». El Consejo decide «**por mayoría cualificada**». Salvedad: «Las obligaciones del Estado miembro […] continuarán, en cualquier caso, siendo vinculantes».
- El art. 354 TFUE precisa que el Estado afectado no vota ni cuenta para el cálculo del tercio o de los cuatro quintos.

**Art. 8**: relaciones preferentes con los «países vecinos».

---

## 4. Atribución, subsidiariedad y proporcionalidad (art. 5 TUE)

- 5.1: «**La delimitación de las competencias de la Unión se rige por el principio de atribución. El ejercicio de las competencias de la Unión se rige por los principios de subsidiariedad y proporcionalidad.**» Distingue delimitación (atribución) y ejercicio (los otros dos).
- 5.2, atribución: la Unión actúa «**dentro de los límites de las competencias que le atribuyen los Estados miembros en los Tratados para lograr los objetivos que éstos determinan. Toda competencia no atribuida a la Unión en los Tratados corresponde a los Estados miembros.**»
- 5.3, subsidiariedad: «**en los ámbitos que no sean de su competencia exclusiva, la Unión intervendrá sólo en caso de que, y en la medida en que, los objetivos de la acción pretendida no puedan ser alcanzados de manera suficiente por los Estados miembros, ni a nivel central ni a nivel regional y local, sino que puedan alcanzarse mejor, debido a la dimensión o a los efectos de la acción pretendida, a escala de la Unión.**» La salvedad que no puede perderse es que no rige en las competencias exclusivas. Se aplica según el «Protocolo sobre la aplicación de los principios de subsidiariedad y proporcionalidad» (es el n.º 2). «**Los Parlamentos nacionales velarán por el respeto del principio de subsidiariedad**».
- 5.4, proporcionalidad: «**el contenido y la forma de la acción de la Unión no excederán de lo necesario para alcanzar los objetivos de los Tratados.**»
- Qué competencias son exclusivas lo dice el TFUE, no el TUE. No lo he leído y queda fuera de mi parte.

---

## 5. Ciudadanía y democracia representativa (Título II, arts. 9-12 TUE)

- **Art. 9**: «**Será ciudadano de la Unión toda persona que tenga la nacionalidad de un Estado miembro. La ciudadanía de la Unión se añade a la ciudadanía nacional sin sustituirla.**» Recoge también el principio de igualdad de los ciudadanos. El catálogo de derechos no está en el TUE sino en el **art. 20.2 TFUE**, con cuatro letras:
  - a) circular y residir libremente;
  - b) sufragio activo y pasivo en las elecciones al Parlamento Europeo y en las municipales del Estado de residencia;
  - c) protección diplomática y consular;
  - d) peticiones al Parlamento Europeo, Defensor del Pueblo Europeo y lengua de los Tratados.
- **Art. 10**:
  - 10.1: «**El funcionamiento de la Unión se basa en la democracia representativa.**»
  - 10.2: los ciudadanos «**estarán directamente representados en la Unión a través del Parlamento Europeo**». Los Estados lo están en el Consejo Europeo por su Jefe de Estado o de Gobierno y en el Consejo por sus Gobiernos.
  - 10.3: «Todo ciudadano tiene derecho a participar en la vida democrática de la Unión».
  - 10.4: partidos políticos a escala europea.
- **Art. 11** (democracia participativa; el nombre es mío, el TUE no lo usa):
  - diálogo con asociaciones representativas y sociedad civil;
  - «amplias consultas» de la Comisión;
  - **iniciativa ciudadana** (11.4): «**Un grupo de al menos un millón de ciudadanos de la Unión, que sean nacionales de un número significativo de Estados miembros, podrá tomar la iniciativa de invitar a la Comisión Europea […] a que presente una propuesta adecuada**». El modo es «podrá» e invita, no obliga. Procedimiento: art. 24 TFUE, párr. 1.º.
- **Art. 12**: los Parlamentos nacionales «contribuirán activamente». **Seis letras (a-f)**: información sobre los proyectos, subsidiariedad, espacio de libertad, seguridad y justicia (Europol y Eurojust), revisión de los Tratados (art. 48), información de las solicitudes de adhesión (art. 49) y cooperación interparlamentaria.

---

## 6. Instituciones (Título III)

### 6.1. Art. 13 TUE

- Las instituciones son **siete**, en este orden literal: «**El Parlamento Europeo, — El Consejo Europeo, — El Consejo, — La Comisión Europea […], — El Tribunal de Justicia de la Unión Europea, — El Banco Central Europeo, — El Tribunal de Cuentas.**»
- 13.2: cada institución actúa dentro de sus atribuciones. «**Las instituciones mantendrán entre sí una cooperación leal.**»
- 13.4: el Parlamento, el Consejo y la Comisión «**estarán asistidos por un Comité Económico y Social y por un Comité de las Regiones que ejercerán funciones consultivas**». No son instituciones: posible trampa de test.

### 6.2. Parlamento Europeo (art. 14 TUE)

- Funciones: ejerce «**conjuntamente con el Consejo la función legislativa y la función presupuestaria**», además de «funciones de control político y consultivas». «**Elegirá al Presidente de la Comisión.**»
- Composición: «**Su número no excederá de setecientos cincuenta, más el Presidente**». Representación «**decrecientemente proporcional, con un mínimo de seis diputados por Estado miembro. No se asignará a ningún Estado miembro más de noventa y seis escaños.**» La composición la fija el Consejo Europeo «**por unanimidad, a iniciativa del Parlamento Europeo y con su aprobación**». La vigente es la Decisión 2023/2061: 720 escaños, 61 para España, 96 para Alemania, 6 para Chipre, Luxemburgo y Malta (art. 3). Su art. 4 pide al Parlamento una propuesta para 2029-2034 «a ser posible antes del final de 2027».
- Elección: «**sufragio universal directo, libre y secreto, para un mandato de cinco años**» (14.3).
- «**El Parlamento Europeo elegirá a su Presidente y a la Mesa de entre sus diputados**» (14.4).
- Mayorías en el TFUE: regla general «**por mayoría de los votos emitidos**», salvo disposición en contrario (art. 231). Moción de censura contra la Comisión (art. 234):
  - no se vota antes de «**tres días como mínimo**» y la votación es pública;
  - se aprueba «**por mayoría de dos tercios de los votos emitidos que representen, a su vez, la mayoría de los diputados que componen el Parlamento Europeo**».

### 6.3. Consejo Europeo (art. 15 TUE)

- Funciones: «**dará a la Unión los impulsos necesarios para su desarrollo y definirá sus orientaciones y prioridades políticas generales. No ejercerá función legislativa alguna.**»
- Composición: los «**Jefes de Estado o de Gobierno de los Estados miembros, así como por su Presidente y por el Presidente de la Comisión**». El Alto Representante «participará en sus trabajos» pero no es miembro.
- Reuniones: «**dos veces por semestre por convocatoria de su Presidente**», y reunión extraordinaria «cuando la situación lo exija».
- Decisiones: «**por consenso, excepto cuando los Tratados dispongan otra cosa**».
- Presidente:
  - elegido «**por mayoría cualificada para un mandato de dos años y medio, que podrá renovarse una sola vez**»; se le puede cesar por el mismo procedimiento en caso de «impedimento o falta grave»;
  - tiene cuatro funciones (letras a-d); la d) es presentar un informe al Parlamento Europeo tras cada reunión;
  - asume la representación exterior en política exterior y de seguridad común «sin perjuicio» del Alto Representante;
  - «**no podrá ejercer mandato nacional alguno**».

### 6.4. Consejo (art. 16 TUE)

- Funciones: legislativa y presupuestaria conjuntamente con el Parlamento, más «definición de políticas y de coordinación».
- Composición: «**un representante de cada Estado miembro, de rango ministerial, facultado para comprometer al Gobierno**».
- Regla de voto: «**por mayoría cualificada, excepto cuando los Tratados dispongan otra cosa**».
- Mayoría cualificada (16.4): «**un mínimo del 55 % de los miembros del Consejo que incluya al menos a quince de ellos y represente a Estados miembros que reúnan como mínimo el 65 % de la población de la Unión**». «**Una minoría de bloqueo estará compuesta por al menos cuatro miembros del Consejo**».
- Si no actúa a propuesta de la Comisión o del Alto Representante: «**un mínimo del 72 % de los miembros del Consejo**» con el 65 % de la población (art. 238.2 TFUE).
- Mayoría simple: «mayoría de los miembros que lo componen» (art. 238.1 TFUE).
- Formaciones: Consejo de Asuntos Generales y Consejo de Asuntos Exteriores.
- COREPER (sigla no presentada en la fuente, que dice «Comité de Representantes Permanentes de los Gobiernos de los Estados miembros»): prepara los trabajos.
- Publicidad: «**se reunirá en público cuando delibere y vote sobre un proyecto de acto legislativo**».
- Presidencia: por «**rotación igual**», excepto la de Asuntos Exteriores, que preside el Alto Representante (art. 18.3).

### 6.5. Comisión (art. 17 TUE) y Alto Representante (art. 18 TUE)

- Funciones (17.1): promueve el interés general, vela por la aplicación de los Tratados, supervisa la aplicación del Derecho de la Unión «bajo el control del [TJUE]», ejecuta el presupuesto y gestiona los programas. Asume la representación exterior «con excepción de la política exterior y de seguridad común».
- Iniciativa (17.2): «**Los actos legislativos de la Unión sólo podrán adoptarse a propuesta de la Comisión, excepto cuando los Tratados dispongan otra cosa.**»
- Mandato: «**de cinco años**». La Comisión es independiente.
- Composición: véase el § 0.3 (hoy, un nacional por Estado).
- Nombramiento (17.7):
  1. El Consejo Europeo, «**teniendo en cuenta el resultado de las elecciones al Parlamento Europeo**», propone «**por mayoría cualificada**» un candidato a Presidente.
  2. El Parlamento lo elige «**por mayoría de los miembros que lo componen**». Si no la obtiene, el Consejo Europeo propone otro candidato «**en el plazo de un mes**».
  3. El Consejo, «de común acuerdo con el Presidente electo», adopta la lista de comisarios.
  4. Todo el colegio se somete «**colegiadamente al voto de aprobación del Parlamento Europeo**».
  5. La Comisión la nombra el Consejo Europeo «**por mayoría cualificada**».
- Responsabilidad «**colegiada ante el Parlamento Europeo**» y moción de censura (17.8 TUE y 234 TFUE).
- Alto Representante (art. 18):
  - lo nombra el Consejo Europeo «**por mayoría cualificada, con la aprobación del Presidente de la Comisión**»;
  - está «al frente de la política exterior y de seguridad común»;
  - preside el Consejo de Asuntos Exteriores;
  - es «**uno de los Vicepresidentes de la Comisión**».

### 6.6. Tribunal de Justicia de la Unión Europea (art. 19 TUE)

- Comprende «**el Tribunal de Justicia, el Tribunal General y los tribunales especializados**». Garantiza «el respeto del Derecho en la interpretación y aplicación de los Tratados».
- Tribunal de Justicia: «**un juez por Estado miembro**», asistido por abogados generales (véase el § 0.3).
- Tribunal General: «**al menos […] un juez por Estado miembro**».
- Nombramiento: «**de común acuerdo por los Gobiernos de los Estados miembros para un período de seis años**», con posible renovación.
- El TFUE añade:
  - renovación parcial «cada tres años»;
  - los jueces eligen a su Presidente «por un período de tres años», con mandato renovable;
  - consulta previa al comité del art. 255 (arts. 253 y 254).
- Competencias (19.3), tres letras: recursos; cuestión prejudicial «a petición de los órganos jurisdiccionales nacionales»; demás casos.

### 6.7. BCE y Tribunal de Cuentas (TFUE, por remisión del art. 13.3 TUE)

- **BCE** (arts. 282 y 283 TFUE):
  - «Le corresponderá en exclusiva autorizar la emisión del euro». «Será independiente».
  - Objetivo principal del Sistema Europeo de Bancos Centrales: «**mantener la estabilidad de precios**».
  - El Comité Ejecutivo lo forman «el presidente, el vicepresidente y otros cuatro miembros». Los nombra el Consejo Europeo por mayoría cualificada. Su mandato es de «**ocho años y no será renovable**».
- **Tribunal de Cuentas** (arts. 285 y 286 TFUE):
  - lleva a cabo «La fiscalización, o control de cuentas de la Unión»;
  - «**un nacional de cada Estado miembro**»;
  - mandato de «**seis años**», renovable; el Consejo adopta la lista «previa consulta al Parlamento Europeo»;
  - su Presidente se elige para tres años, con mandato renovable.

---

## 7. Cooperaciones reforzadas (Título IV, art. 20 TUE)

- Solo «**en el marco de las competencias no exclusivas de la Unión**».
- Finalidad: «impulsar los objetivos de la Unión, proteger sus intereses y reforzar su proceso de integración». «**abiertas permanentemente a todos los Estados miembros**».
- Autorización (20.2): la da el Consejo «**como último recurso**», cuando los objetivos «no pueden ser alcanzados en un plazo razonable por la Unión en su conjunto», y «**a condición de que participen en ella al menos nueve Estados miembros**». El procedimiento está en el art. 329 TFUE.
- Votación (20.3): deliberan todos los miembros del Consejo, pero votan solo los participantes.
- Efectos (20.4): los actos «**vincularán únicamente a los Estados miembros participantes**» y «no se considerarán acervo» para los candidatos.

---

## 8. Revisión de los Tratados (art. 48 TUE)

Hay procedimiento ordinario y procedimientos simplificados (48.1).

- **Ordinario** (48.2 a 48.5):
  - Iniciativa: «**El Gobierno de cualquier Estado miembro, el Parlamento Europeo o la Comisión**», que presentan los proyectos al Consejo. Los proyectos pueden «aumentar o reducir las competencias».
  - El Consejo Europeo, previa consulta al Parlamento y a la Comisión, decide examinarlos «**por mayoría simple**». Entonces su Presidente convoca una **Convención**, que adopta «**por consenso**» una recomendación.
  - El Consejo Europeo puede no convocar la Convención, «por mayoría simple, previa aprobación del Parlamento Europeo», y en ese caso da un mandato a la Conferencia.
  - La Conferencia de representantes de los Gobiernos la convoca «**El Presidente del Consejo**». Así lo dice el texto: del Consejo, no del Consejo Europeo.
  - Entrada en vigor: tras la ratificación «**por todos los Estados miembros**».
  - Si, «**transcurrido un plazo de dos años desde la firma**», **cuatro quintas partes** de los Estados han ratificado y otros tienen dificultades, «el Consejo Europeo examinará la cuestión».
- **Simplificado, tercera parte del TFUE** (48.6):
  - decide el Consejo Europeo «**por unanimidad**»;
  - necesita la aprobación de los Estados según sus normas constitucionales;
  - «**no podrá aumentar las competencias atribuidas a la Unión**».
- **Pasarelas** (48.7): paso de unanimidad a mayoría cualificada, o de procedimiento legislativo especial a ordinario.
  - Excluidas: «las decisiones que tengan repercusiones militares o en el ámbito de la defensa».
  - Veto de cualquier Parlamento nacional «**en un plazo de seis meses**».
  - Decide el Consejo Europeo «por unanimidad, previa aprobación del Parlamento Europeo, que se pronunciará por mayoría de los miembros que lo componen».

---

## 9. Adhesión y retirada (arts. 49 y 50 TUE)

- **Art. 49, adhesión**:
  - Puede solicitarla «**Cualquier Estado europeo que respete los valores mencionados en el artículo 2 y se comprometa a promoverlos**».
  - Se informa al Parlamento Europeo y a los Parlamentos nacionales.
  - La solicitud se dirige «**al Consejo, que se pronunciará por unanimidad después de haber consultado a la Comisión y previa aprobación del Parlamento Europeo, el cual se pronunciará por mayoría de los miembros que lo componen**».
  - Se tienen en cuenta «los criterios de elegibilidad acordados por el Consejo Europeo». El TUE no los enumera: los «criterios de Copenhague» no están en el texto.
  - Condiciones de admisión: se fijan en un acuerdo entre los Estados miembros y el solicitante, sujeto a «**la ratificación de todos los Estados contratantes**».
- **Art. 50, retirada**:
  - 50.1: «**Todo Estado miembro podrá decidir, de conformidad con sus normas constitucionales, retirarse de la Unión.**»
  - 50.2: el Estado notifica su intención «**al Consejo Europeo**». El acuerdo de retirada se negocia según el art. 218.3 TFUE y lo celebra el Consejo «**por mayoría cualificada, previa aprobación del Parlamento Europeo**».
  - 50.3: los Tratados dejan de aplicarse desde la entrada en vigor del acuerdo «**o, en su defecto, a los dos años de la notificación**», «**salvo si el Consejo Europeo, de acuerdo con dicho Estado, decide por unanimidad prorrogar dicho plazo**».
  - 50.4: el Estado que se retira no participa. La mayoría cualificada se calcula por el art. 238.3.b) TFUE: «un mínimo del 72 % de los miembros del Consejo que represente a Estados miembros participantes que reúnan como mínimo el 65 % de la población de dichos Estados».
  - 50.5: si quiere volver, pasa por el art. 49.

---

## 10. La Carta

### 10.1. Valor jurídico (art. 6 TUE)

- 6.1: «**La Unión reconoce los derechos, libertades y principios enunciados en la Carta de los Derechos Fundamentales de la Unión Europea de 7 de diciembre de 2000, tal como fue adaptada el 12 de diciembre de 2007 en Estrasburgo, la cual tendrá el mismo valor jurídico que los Tratados.**»
- Salvedades del mismo apartado:
  - «**Las disposiciones de la Carta no ampliarán en modo alguno las competencias de la Unión**»;
  - se interpreta según el título VII de la Carta y «teniendo debidamente en cuenta las explicaciones».
- 6.2: «**La Unión se adherirá al [CEDH]. Esta adhesión no modificará las competencias de la Unión**». **No he podido confirmar en fuente si esa adhesión se ha producido.**
- 6.3: los derechos del CEDH y los de las tradiciones constitucionales comunes forman parte del Derecho de la Unión «**como principios generales**».
- La Carta no está dentro del TUE: se publica aparte, en la serie C del DOUE. Nota final de la Carta: «El texto supra recoge, adaptándola, la Carta proclamada el 7 de diciembre de 2000, a la que sustituirá a partir del día de la entrada en vigor del Tratado de Lisboa». La proclaman «El Parlamento Europeo, el Consejo y la Comisión».
- **Protocolo n.º 30**, sobre la aplicación de la Carta a Polonia y al Reino Unido (art. 1.2): «nada de lo dispuesto en el título IV de la Carta crea derechos que se puedan defender ante los órganos jurisdiccionales de Polonia o del Reino Unido, salvo en la medida en que Polonia o el Reino Unido hayan contemplado dichos derechos en su legislación nacional».

### 10.2. Estructura

Preámbulo y **54 artículos** en **siete títulos** (recuento hecho sobre el texto):

| Título | Rúbrica | Arts. | N.º |
|---|---|---|---|
| I | DIGNIDAD | 1-5 | 5 |
| II | LIBERTADES | 6-19 | 14 |
| III | IGUALDAD | 20-26 | 7 |
| IV | SOLIDARIDAD | 27-38 | 12 |
| V | CIUDADANÍA | 39-46 | 8 |
| VI | JUSTICIA | 47-50 | 4 |
| VII | DISPOSICIONES GENERALES QUE RIGEN LA INTERPRETACIÓN Y LA APLICACIÓN DE LA CARTA | 51-54 | 4 |

Artículos que interesan a Canal Sur:

- **Art. 11**, «Libertad de expresión y de información».
  - 11.1: «Toda persona tiene derecho a la libertad de expresión. Este derecho comprende la libertad de opinión y la libertad de recibir o comunicar informaciones o ideas sin que pueda haber injerencia de autoridades públicas y sin consideración de fronteras.»
  - 11.2: «**Se respetan la libertad de los medios de comunicación y su pluralismo.**»
- Otros artículos con rúbrica relevante:
  - art. 8, «Protección de datos de carácter personal»;
  - art. 13, «Las artes y la investigación científica son libres»;
  - art. 22, «Diversidad cultural, religiosa y lingüística»;
  - art. 26, «Integración de las personas discapacitadas»;
  - art. 42, «Derecho de acceso a los documentos».
- Primer artículo, art. 1: «**La dignidad humana es inviolable. Será respetada y protegida.**»
- Art. 2.2: «**Nadie podrá ser condenado a la pena de muerte ni ejecutado.**»

Las rúbricas de los 54 artículos están en el fichero de la fuente. Las he extraído y comprobado.

### 10.3. Ámbito de aplicación y alcance (arts. 51 a 54)

- **Art. 51, «Ámbito de aplicación».**
  - 51.1: la Carta se dirige a las instituciones, órganos y organismos de la Unión, «dentro del respeto del principio de subsidiariedad, así como **a los Estados miembros únicamente cuando apliquen el Derecho de la Unión**». Los Estados «respetarán los derechos, observarán los principios y promoverán su aplicación». Esta salvedad («únicamente cuando apliquen») es la más preguntable.
  - 51.2: «**no amplía el ámbito de aplicación del Derecho de la Unión más allá de las competencias de la Unión, ni crea ninguna competencia o misión nuevas para la Unión, ni modifica las competencias y misiones definidas en los Tratados**».
- **Art. 52, «Alcance e interpretación de los derechos y principios»** (siete apartados):
  1. Límites: «**deberá ser establecida por la ley y respetar el contenido esencial**». Con respeto del principio de proporcionalidad, «sólo podrán introducirse limitaciones cuando sean necesarias y respondan efectivamente a objetivos de interés general reconocidos por la Unión o a la necesidad de protección de los derechos y libertades de los demás».
  2. Los derechos que son disposiciones de los Tratados se ejercen en las condiciones de estos.
  3. Derechos que corresponden a los del CEDH: «**su sentido y alcance serán iguales a los que les confiere dicho Convenio**», lo que «no obstará a que el Derecho de la Unión conceda una protección más extensa».
  4. Tradiciones constitucionales comunes: se interpretan «en armonía» con ellas.
  5. **Principios**: «podrán aplicarse mediante actos legislativos y ejecutivos». «**Sólo podrán alegarse ante un órgano jurisdiccional en lo que se refiere a la interpretación y control de la legalidad de dichos actos.**»
  6. Legislaciones y prácticas nacionales.
  7. Las explicaciones «serán tenidas debidamente en cuenta».
- **Art. 53, «Nivel de protección»**: la Carta no puede interpretarse «como limitativa o lesiva» de los derechos reconocidos por el Derecho de la Unión, el Derecho internacional, los convenios (en particular el CEDH) y «**las constituciones de los Estados miembros**».
- **Art. 54, «Prohibición del abuso de derecho»**: nada autoriza actividades «tendente[s] a la destrucción de los derechos o libertades» ni limitaciones más amplias que las previstas en la Carta.

---

## 11. Material reutilizable de los temas de RTVE

El cruce `informes/canal-sur-reuso/comun-gestion.tsv` (puesto 0, tema 3) da un **5 %**: «Sólo actualidad de la UE y menciones a la Carta; ni TUE ni representación de la Junta ante la UE». Lo confirmo después de buscar en todo `temas/`. No hay ningún tema de RTVE que desarrolle el TUE ni la Carta. Pasajes aprovechables:

1. `temas/informacion/02-union-europea.md`, **«### Cuántos escaños elige España»**. Redacción:
   > «**La respuesta oficial**: **61**. **Está en la misma fila del mismo cuadro**: la columna de "total escaños" de la fila "total estatal" dice **61**. Y la suma de la tabla de arriba lo confirma: 22 + 20 + 6 + 3 + 3 + 3 + 2 + 1 + 1 = **61**.»

   Es formato de pregunta de examen y no vale tal cual. El dato cuadra con el art. 3 de la Decisión 2023/2061, que es la fuente normativa que conviene citar.
2. Mismo tema, **«## 1. España en la Unión: el tratado de adhesión»**, tabla de fechas: firma el 12-VI-1985; Ley Orgánica 10/1985, de 2 de agosto, «de acuerdo con lo previsto en el artículo 93 de la Constitución»; ratificación el 20-IX-1985; parte desde el 1-I-1986. También la frase «la Unión Europea como tal no existía todavía; nace con el Tratado de Maastricht». Sirve de introducción histórica. Lo de Maastricht cuadra con la fórmula final del TUE y con su art. 54.2 (entrada en vigor el 1-I-1993). No he releído el BOE de la adhesión.
3. Mismo tema, **«## 7. La zona del euro: por qué la página de hoy no vale para 2024»**: cita de la web de la UE, «el euro (€) es la moneda oficial de 21 de los 27 países de la UE». Sirve como glosa del art. 3.4 TUE, pero es una página web consultada el 02-09-2026, no una norma. Si se usa, hay que releerla. Yo no la he releído.
4. `temas/informacion/08-resolucion-parlamento-europeo.md`, **«### Otros considerandos que conviene tener»**: «**Todos los Estados miembros deben respetar los valores del artículo 2 del TUE**». Solo es un ejemplo de invocación del art. 2.
5. `temas/general/01-constitucion-espanola.md`, **«### 5.3. Capítulo tercero. De los Tratados Internacionales»**: «**Artículo 93.** Mediante **ley orgánica** se puede autorizar la celebración de tratados **por los que se atribuya a una organización o institución internacional el ejercicio de competencias derivadas de la Constitución**. Es el artículo por el que España entró en las Comunidades Europeas.» Es la redacción de RTVE y la CE no la he releído hoy. El art. 93 CE no se ha reformado, pero hay que comprobarlo con `boe.py`.
6. `temas/informacion/02-union-europea.md`, **«## 8. Lo que aquí sólo sostiene la plantilla»** (Metsola, Kallas, Schengen): **no reutilizable**. No tiene fuente y es actualidad de 2024.

---

## 12. Lo que no he podido confirmar

- Si el CEDH ya se ha adherido a la Unión (art. 6.2 TUE lo manda, en futuro).
- La fecha y el procedimiento de la retirada del Reino Unido. En consecuencia, el número actual de Estados miembros no está confirmado en norma. Las decisiones de 2023 dan 27 Estados en el reparto del Parlamento (art. 3 de la Decisión 2023/2061, 27 filas contadas), lo cual es un indicio, no una declaración.
- Si sigue vigente la Decisión 2013/336/UE (once abogados generales).
- El número de jueces del Tribunal General. Lo fija el Estatuto del TJUE (art. 254 TFUE), cuya redacción vigente no he leído. El Protocolo n.º 3 de la edición de 2016 no está al día.
- Los nombres de los titulares actuales de las presidencias (Consejo Europeo, Comisión, Parlamento, BCE). Ninguna norma los da.
- El reparto de competencias exclusivas, compartidas y de apoyo (arts. 2 a 6 TFUE). No lo he leído porque queda fuera de la rúbrica literal. Si el redactor lo quiere para explicar la subsidiariedad, hay que leerlo en la fuente.
- La coincidencia literal del enunciado con el BOJA núm. 186 (solo lo he cotejado con la transcripción del proyecto).

---

## 13. Ficheros tocados

- Creado: este informe.
- Creados en `fuentes/canal-sur/documentos/`:
  - `tue-version-consolidada-doue-c202-2016.txt`
  - `carta-derechos-fundamentales-ue-doue-c202-2016.txt`
  - `tfue-version-consolidada-doue-c202-2016.txt`
  - `decision-ce-2023-2061-composicion-parlamento-europeo.txt`
  - `decision-ce-2013-272-numero-miembros-comision.txt`
  - `decision-consejo-2013-336-abogados-generales.txt`
- No he modificado ningún otro fichero del repositorio.
