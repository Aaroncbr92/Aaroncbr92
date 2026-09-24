# T03 · Investigación · La Unión Europea, el Tratado de la Unión Europea y la Carta

Fase 1. Mi parte es «La Unión Europea. Tratado de la Unión Europea y Carta de derechos fundacionales». La representación de la Junta no es mía. Todo se leyó el **24-09-2026**.

Siglas: Unión Europea (UE); Tratado de la Unión Europea (TUE); Tratado de Funcionamiento de la UE (TFUE); Carta de los Derechos Fundamentales de la UE (la Carta); Diario Oficial de la UE (DOUE); Convenio Europeo para la Protección de los Derechos Humanos (CEDH); Tribunal de Justicia de la UE (TJUE); Banco Central Europeo (BCE).

## 0. Premisas que no cuadran con la fuente

1. **Posible errata del BOJA.** El programa (transcripción de `convocatoria/canal-sur/PROGRAMA-COMUN.md`) dice «**Carta de derechos fundacionales**». El DOUE publica la «**CARTA DE LOS DERECHOS FUNDAMENTALES DE LA UNIÓN EUROPEA**» (2016/C 202/02), y así la nombra el art. 6.1 TUE. El epígrafe se deja literal y la errata se explica en el cuerpo. No lo he cotejado con el PDF del BOJA núm. 186.
2. **La versión consolidada vigente es de 2016 y no está al día del Brexit.** El art. 52.1 TUE sigue enumerando «al Reino Unido de Gran Bretaña e Irlanda del Norte», y el Protocolo n.º 30 habla de «Polonia y el Reino Unido». Con esa lista no se puede contar a los Estados de hoy. El acuerdo de retirada **no lo he leído**.
3. **Hay cifras del TUE desplazadas por derecho derivado.** El tema debe dar las dos:
   - **Parlamento.** Art. 14.2 TUE: «**no excederá de setecientos cincuenta, más el Presidente**». La Decisión (UE) 2023/2061 del Consejo Europeo (DO L 238, 27-IX-2023), art. 3, reparte para **2024-2029** un total de **720** escaños en 27 filas (suma comprobada). **España 61**, Alemania 96; Chipre, Luxemburgo y Malta, 6 cada uno.
   - **Comisión.** Art. 17.5 TUE: desde el 1-XI-2014, «**los dos tercios del número de Estados miembros**», «**a menos que el Consejo Europeo decida por unanimidad modificar dicho número**». Decisión 2013/272/UE (DO L 165, 18-VI-2013), art. 1: «**un número de miembros igual al número de Estados miembros, que incluirá a su Presidente y al Alto Representante**». Según los metadatos de la Oficina de Publicaciones, está en vigor y nadie la ha modificado.
   - **Abogados generales.** Art. 252 TFUE: «**ocho**». Decisión 2013/336/UE: «**nueve**» desde el 1-VII-2013 y «**once**» desde el 7-X-2015. No he podido confirmar su vigencia.
4. **Transitorios agotados**, que no son regla actual: art. 16.5 TUE (mayoría cualificada hasta el 31-X-2014 y entre el 1-XI-2014 y el 31-III-2017); art. 17.4 TUE (la Comisión hasta el 31-X-2014); art. 54.2 TUE (entrada en vigor el 1-I-1993).
5. **Solo cinco de las siete instituciones tienen artículo en el TUE** (arts. 14-19). Para el BCE y el Tribunal de Cuentas, el art. 13.3 remite al TFUE, y allí los he leído.

## 1. Fuentes y versión

- **TUE**: «VERSIÓN CONSOLIDADA DEL TRATADO DE LA UNIÓN EUROPEA», **DOUE C 202, de 7-VI-2016** (CELEX 12016M/TXT), con protocolos y declaraciones.
- **Carta**: DOUE C 202, de 7-VI-2016, p. 389 (CELEX 12016P/TXT).
- **TFUE**: mismo DOUE (CELEX 12016E/TXT); solo los artículos que se citan.
- **Decisiones** 2023/2061, 2013/272 y 2013/336.
- **Ficheros** en `fuentes/canal-sur/documentos/`: `tue-version-consolidada-doue-c202-2016.txt`, `carta-derechos-fundamentales-ue-doue-c202-2016.txt`, `tfue-version-consolidada-doue-c202-2016.txt` y tres `decision-*.txt`. Cada uno lleva en cabecera la URL y la fecha.
- **Cómo se obtuvieron.** EUR-Lex responde 202 vacío a toda consulta automática (filtro anti-robots). He descargado el mismo XHTML del DOUE desde el repositorio de la Oficina de Publicaciones (`publications.europa.eu/resource/celex/<CELEX>`, en español). No hay PDF. `doue.py` no sirve: lee reproducciones del BOE en texto original, y el BOE no publica la consolidación.
- **¿Hay una consolidación posterior?** El punto SPARQL de la Oficina de Publicaciones, para CELEX del sector 1 con descriptor M o P, devuelve como más reciente **2016**. No hay consolidación posterior.

## 2. Estructura del TUE

Preámbulo y **55 artículos** (contados) en **seis títulos**:

| Título | Rúbrica | Arts. |
|---|---|---|
| I | «DISPOSICIONES COMUNES» | 1-8 |
| II | «DISPOSICIONES SOBRE LOS PRINCIPIOS DEMOCRÁTICOS» | 9-12 |
| III | «DISPOSICIONES SOBRE LAS INSTITUCIONES» | 13-19 |
| IV | «DISPOSICIONES SOBRE LAS COOPERACIONES REFORZADAS» | 20 |
| V | Acción exterior y política exterior y de seguridad común | 21-46 (cap. 1: 21-22; cap. 2, secc. 1: 23-41; secc. 2, Política Común de Seguridad y Defensa: 42-46) |
| VI | «DISPOSICIONES FINALES» | 47-55 |

- Art. 1:
  - «**La Unión se fundamenta en el presente Tratado y en el Tratado de Funcionamiento de la Unión Europea […]. Ambos Tratados tienen el mismo valor jurídico. La Unión sustituirá y sucederá a la Comunidad Europea.**»
  - Los Estados «atribuyen competencias para alcanzar sus objetivos comunes».
- Art. 47: «**La Unión tiene personalidad jurídica.**»
- Art. 51: los Protocolos y Anexos «forman parte integrante» de los Tratados.
- Art. 53: «**período de tiempo ilimitado**».
- Art. 54.1: depósito «ante el Gobierno de la República Italiana».
- Art. 55: **24 lenguas** (contadas).
- «**Hecho en Maastricht, el siete de febrero de mil novecientos noventa y dos.**»

## 3. Valores y objetivos (arts. 2, 3, 4 y 7 TUE)

- **Art. 2**: «**La Unión se fundamenta en los valores de respeto de la dignidad humana, libertad, democracia, igualdad, Estado de Derecho y respeto de los derechos humanos, incluidos los derechos de las personas pertenecientes a minorías. Estos valores son comunes a los Estados miembros en una sociedad caracterizada por el pluralismo, la no discriminación, la tolerancia, la justicia, la solidaridad y la igualdad entre mujeres y hombres.**» Son seis valores y seis rasgos (contados).
- **Art. 3**, seis apartados:
  1. «**promover la paz, sus valores y el bienestar de sus pueblos**».
  2. Espacio de libertad, seguridad y justicia «sin fronteras interiores».
  3. «**La Unión establecerá un mercado interior**». Además:
     - «economía social de mercado altamente competitiva, tendente al pleno empleo y al progreso social»;
     - cohesión «económica, social y territorial»;
     - «respetará la riqueza de su diversidad cultural y lingüística».
  4. «**una unión económica y monetaria cuya moneda es el euro**».
  5. Relaciones exteriores, con respeto de «la Carta de las Naciones Unidas».
  6. Objetivos solo «de acuerdo con las competencias que se le atribuyen».
- **Art. 4**:
  - Lo no atribuido «corresponde a los Estados miembros».
  - Identidad nacional, «también en lo referente a la autonomía local y regional».
  - «**la seguridad nacional seguirá siendo responsabilidad exclusiva de cada Estado miembro**».
  - «**principio de cooperación leal**».
- **Art. 7**, garantía de los valores:
  - **Riesgo claro** de violación grave. Propuesta de «**un tercio de los Estados miembros, del Parlamento Europeo o de la Comisión**». Constata el Consejo «**por mayoría de cuatro quintos de sus miembros y previa aprobación del Parlamento Europeo**».
  - **Violación grave y persistente.** Constata el Consejo Europeo «**por unanimidad**», a propuesta de un tercio de los Estados o de la Comisión, con aprobación del Parlamento.
  - **Suspensión** de derechos, incluido el voto. La decide el Consejo «**por mayoría cualificada**», y las obligaciones del Estado «continuarán […] siendo vinculantes».
  - Art. 354 TFUE: el Estado afectado no vota ni cuenta para el tercio o los cuatro quintos.

## 4. Atribución, subsidiariedad y proporcionalidad (art. 5 TUE)

- 5.1: «**La delimitación de las competencias de la Unión se rige por el principio de atribución. El ejercicio de las competencias de la Unión se rige por los principios de subsidiariedad y proporcionalidad.**»
- 5.2, atribución: actúa «dentro de los límites de las competencias que le atribuyen los Estados miembros en los Tratados»; lo no atribuido corresponde a los Estados.
- 5.3, subsidiariedad: «**en los ámbitos que no sean de su competencia exclusiva, la Unión intervendrá sólo en caso de que, y en la medida en que, los objetivos de la acción pretendida no puedan ser alcanzados de manera suficiente por los Estados miembros, ni a nivel central ni a nivel regional y local, sino que puedan alcanzarse mejor […] a escala de la Unión.**»
  - **Salvedad**: no rige en las competencias exclusivas.
  - Se aplica según el Protocolo sobre subsidiariedad y proporcionalidad (el n.º 2).
  - «**Los Parlamentos nacionales velarán por el respeto del principio de subsidiariedad**».
- 5.4, proporcionalidad: «**el contenido y la forma de la acción de la Unión no excederán de lo necesario para alcanzar los objetivos de los Tratados.**»
- Qué competencias son exclusivas lo dice el TFUE (arts. 2-6). No lo he leído.

## 5. Ciudadanía y democracia (arts. 9-12 TUE)

- **Art. 9**:
  - «**Será ciudadano de la Unión toda persona que tenga la nacionalidad de un Estado miembro. La ciudadanía de la Unión se añade a la ciudadanía nacional sin sustituirla.**»
  - Los derechos están en el **art. 20.2 TFUE**, cuatro letras: circulación y residencia; sufragio en las elecciones europeas y municipales del Estado de residencia; protección diplomática y consular; petición, Defensor del Pueblo y lengua.
- **Art. 10**:
  - «**El funcionamiento de la Unión se basa en la democracia representativa.**»
  - Los ciudadanos, «directamente representados […] a través del Parlamento Europeo». Los Estados, en el Consejo Europeo y en el Consejo.
  - Derecho a participar en la vida democrática, y partidos políticos europeos.
- **Art. 11.4**, iniciativa ciudadana: «**al menos un millón de ciudadanos de la Unión, que sean nacionales de un número significativo de Estados miembros, podrá tomar la iniciativa de invitar a la Comisión Europea**». Está en «podrá» y es una invitación. El procedimiento, en el art. 24 TFUE.
- **Art. 12**: los Parlamentos nacionales, **seis letras (a-f)**. Entre ellas: la subsidiariedad, la revisión (art. 48) y la información de las adhesiones (art. 49).

## 6. Instituciones

### Art. 13 TUE

- **Siete**, en este orden: «**El Parlamento Europeo, — El Consejo Europeo, — El Consejo, — La Comisión Europea […], — El Tribunal de Justicia de la Unión Europea, — El Banco Central Europeo, — El Tribunal de Cuentas.**»
- «**Las instituciones mantendrán entre sí una cooperación leal.**»
- El Comité Económico y Social y el Comité de las Regiones «ejercerán funciones consultivas». No son instituciones: trampa típica.

### Parlamento Europeo (art. 14 TUE)

- Ejerce «**conjuntamente con el Consejo la función legislativa y la función presupuestaria**», más el control político y funciones consultivas. «**Elegirá al Presidente de la Comisión.**»
- Composición:
  - «**setecientos cincuenta, más el Presidente**»;
  - «**decrecientemente proporcional, con un mínimo de seis diputados**»; máximo de «**noventa y seis**»;
  - la fija el Consejo Europeo «**por unanimidad, a iniciativa del Parlamento Europeo y con su aprobación**».
- «**sufragio universal directo, libre y secreto, para un mandato de cinco años**».
- Elige a su Presidente y a la Mesa.
- TFUE:
  - art. 231: regla general, «**mayoría de los votos emitidos**»;
  - art. 234, moción de censura: plazo de «**tres días como mínimo**», votación pública; «**mayoría de dos tercios de los votos emitidos que representen, a su vez, la mayoría de los diputados**».

### Consejo Europeo (art. 15 TUE)

- «**dará a la Unión los impulsos necesarios […]. No ejercerá función legislativa alguna.**»
- Composición: «**Jefes de Estado o de Gobierno**», más su Presidente y el Presidente de la Comisión. El Alto Representante «participará».
- Se reúne «**dos veces por semestre**».
- Decide «**por consenso, excepto cuando los Tratados dispongan otra cosa**».
- Presidente:
  - elegido «**por mayoría cualificada para un mandato de dos años y medio, que podrá renovarse una sola vez**»;
  - cuatro funciones (a-d), entre ellas un informe al Parlamento tras cada reunión;
  - «**no podrá ejercer mandato nacional alguno**».

### Consejo (art. 16 TUE)

- Funciones: legislativa y presupuestaria con el Parlamento, más definición de políticas y coordinación.
- Composición: «**un representante de cada Estado miembro, de rango ministerial**».
- Regla: «**mayoría cualificada, excepto cuando los Tratados dispongan otra cosa**».
- Mayoría cualificada:
  - «**un mínimo del 55 % de los miembros del Consejo que incluya al menos a quince de ellos y represente a Estados miembros que reúnan como mínimo el 65 % de la población**»;
  - minoría de bloqueo: «**al menos cuatro miembros**»;
  - si no actúa a propuesta de la Comisión o del Alto Representante: «**72 %**» de los miembros con el 65 % de la población (art. 238.2 TFUE).
- Mayoría simple: «mayoría de los miembros que lo componen» (art. 238.1 TFUE).
- Formaciones: Asuntos Generales y Asuntos Exteriores.
- El Comité de Representantes Permanentes prepara los trabajos.
- Sesión pública «cuando delibere y vote sobre un proyecto de acto legislativo».
- Presidencia por «**rotación igual**», salvo Asuntos Exteriores.

### Comisión y Alto Representante (arts. 17 y 18 TUE)

- Funciones:
  - promueve el interés general;
  - vela por la aplicación de los Tratados «bajo el control del [TJUE]»;
  - ejecuta el presupuesto;
  - asume la representación exterior salvo en política exterior y de seguridad común.
- «**Los actos legislativos de la Unión sólo podrán adoptarse a propuesta de la Comisión, excepto cuando los Tratados dispongan otra cosa.**»
- Mandato de «**cinco años**», con plena independencia.
- Nombramiento (17.7):
  1. El Consejo Europeo propone un candidato «**teniendo en cuenta el resultado de las elecciones al Parlamento Europeo**», «**por mayoría cualificada**».
  2. El Parlamento lo elige «**por mayoría de los miembros que lo componen**». Si fracasa, hay nuevo candidato «**en el plazo de un mes**».
  3. El Consejo, de común acuerdo con el Presidente electo, adopta la lista de comisarios.
  4. Voto de aprobación colegiado del Parlamento.
  5. Nombramiento por el Consejo Europeo «**por mayoría cualificada**».
- Responsabilidad «**colegiada ante el Parlamento Europeo**».
- Alto Representante (art. 18):
  - lo nombra el Consejo Europeo «**por mayoría cualificada, con la aprobación del Presidente de la Comisión**»;
  - dirige la política exterior y de seguridad común y preside el Consejo de Asuntos Exteriores;
  - es «**uno de los Vicepresidentes de la Comisión**».

### TJUE (art. 19 TUE)

- Comprende «**el Tribunal de Justicia, el Tribunal General y los tribunales especializados**».
- Tribunal de Justicia: «**un juez por Estado miembro**», con abogados generales.
- Tribunal General: «**al menos […] un juez por Estado miembro**».
- Nombramiento «**de común acuerdo por los Gobiernos […] para un período de seis años**», con posible renovación.
- Arts. 253-254 TFUE: renovación parcial cada tres años; Presidente elegido por tres años; consulta al comité del art. 255.
- Competencias, tres letras: recursos; cuestión prejudicial «a petición de los órganos jurisdiccionales nacionales»; demás casos.

### BCE y Tribunal de Cuentas (TFUE)

- **BCE** (arts. 282-283):
  - «en exclusiva» autoriza la emisión del euro; es «independiente»;
  - objetivo principal: «**mantener la estabilidad de precios**»;
  - Comité Ejecutivo: presidente, vicepresidente y «otros cuatro miembros», nombrados por el Consejo Europeo por mayoría cualificada; mandato de «**ocho años y no será renovable**».
- **Tribunal de Cuentas** (arts. 285-286):
  - «un nacional de cada Estado miembro»;
  - mandato de «**seis años**», renovable; lista adoptada por el Consejo, previa consulta al Parlamento;
  - Presidente por tres años.

## 7. Cooperaciones reforzadas (art. 20 TUE)

- Solo «**en el marco de las competencias no exclusivas**». «Abiertas permanentemente a todos los Estados miembros».
- Autorización:
  - la da el Consejo «**como último recurso**», cuando los objetivos no pueden alcanzarse «en un plazo razonable por la Unión en su conjunto»;
  - «**a condición de que participen en ella al menos nueve Estados miembros**»;
  - procedimiento del art. 329 TFUE.
- Deliberan todos; votan solo los participantes.
- Los actos «**vincularán únicamente a los Estados miembros participantes**» y «no se considerarán acervo» para los candidatos.

## 8. Revisión de los Tratados (art. 48 TUE)

- **Procedimiento ordinario:**
  - Iniciativa: «**El Gobierno de cualquier Estado miembro, el Parlamento Europeo o la Comisión**». Puede «aumentar o reducir las competencias».
  - El Consejo Europeo decide examinarla «**por mayoría simple**» y convoca una **Convención**, que adopta «**por consenso**» una recomendación.
  - Puede prescindir de la Convención por mayoría simple, con aprobación del Parlamento.
  - La Conferencia de los Gobiernos la convoca «**El Presidente del Consejo**». El texto dice del Consejo, no del Consejo Europeo.
  - Las modificaciones entran en vigor tras la ratificación «**por todos los Estados miembros**».
  - Si, «**transcurrido un plazo de dos años desde la firma**», han ratificado **cuatro quintas partes** y otros tienen dificultades, «el Consejo Europeo examinará la cuestión».
- **Simplificado** (tercera parte del TFUE): el Consejo Europeo decide «**por unanimidad**», los Estados lo aprueban, y «**no podrá aumentar las competencias**».
- **Pasarelas** (48.7):
  - de unanimidad a mayoría cualificada, o de procedimiento especial a ordinario;
  - no caben en decisiones militares o de defensa;
  - veto de un Parlamento nacional «**en un plazo de seis meses**»;
  - el Consejo Europeo decide por unanimidad, con aprobación del Parlamento «por mayoría de los miembros que lo componen».

## 9. Adhesión y retirada (arts. 49 y 50 TUE)

- **Art. 49, adhesión:**
  - Puede pedirla «**Cualquier Estado europeo que respete los valores mencionados en el artículo 2 y se comprometa a promoverlos**».
  - Se informa al Parlamento Europeo y a los Parlamentos nacionales.
  - Decide el Consejo «**por unanimidad después de haber consultado a la Comisión y previa aprobación del Parlamento Europeo, el cual se pronunciará por mayoría de los miembros que lo componen**».
  - «Se tendrán en cuenta los criterios de elegibilidad acordados por el Consejo Europeo». El TUE no los enumera.
  - El acuerdo de adhesión se somete a «**la ratificación de todos los Estados contratantes**».
- **Art. 50, retirada:**
  - «**Todo Estado miembro podrá decidir, de conformidad con sus normas constitucionales, retirarse**».
  - Se notifica «**al Consejo Europeo**».
  - El acuerdo lo celebra el Consejo «**por mayoría cualificada, previa aprobación del Parlamento Europeo**».
  - Los Tratados dejan de aplicarse desde la entrada en vigor del acuerdo «**o, en su defecto, a los dos años de la notificación**», «**salvo si el Consejo Europeo, de acuerdo con dicho Estado, decide por unanimidad prorrogar dicho plazo**».
  - El Estado que se retira no participa. La mayoría es la del art. 238.3.b) TFUE: 72 % de los participantes con el 65 % de su población.
  - Si quiere volver, pasa por el art. 49.

## 10. La Carta

### Valor jurídico (art. 6 TUE)

- 6.1: «**La Unión reconoce los derechos, libertades y principios enunciados en la Carta de los Derechos Fundamentales de la Unión Europea de 7 de diciembre de 2000, tal como fue adaptada el 12 de diciembre de 2007 en Estrasburgo, la cual tendrá el mismo valor jurídico que los Tratados.**» Con dos salvedades:
  - «**no ampliarán en modo alguno las competencias de la Unión**»;
  - se interpreta según el título VII y las explicaciones.
- 6.2: «**La Unión se adherirá al [CEDH]**». **No he confirmado si la adhesión se ha producido.**
- 6.3: el CEDH y las tradiciones constitucionales comunes son «**principios generales**».
- La proclaman el Parlamento, el Consejo y la Comisión.
- Nota final: sustituye a la de 2000 «a partir del día de la entrada en vigor del Tratado de Lisboa».
- Protocolo n.º 30, art. 1.2: el título IV no crea derechos justiciables en Polonia ni en el Reino Unido, «salvo en la medida en que […] hayan contemplado dichos derechos en su legislación nacional».

### Estructura

Preámbulo y **54 artículos** (contados):

| Título | Rúbrica | Arts. |
|---|---|---|
| I | DIGNIDAD | 1-5 |
| II | LIBERTADES | 6-19 |
| III | IGUALDAD | 20-26 |
| IV | SOLIDARIDAD | 27-38 |
| V | CIUDADANÍA | 39-46 |
| VI | JUSTICIA | 47-50 |
| VII | DISPOSICIONES GENERALES QUE RIGEN LA INTERPRETACIÓN Y LA APLICACIÓN DE LA CARTA | 51-54 |

Artículos que interesan a Canal Sur:

- Art. 11.1: libertad de expresión, que «comprende la libertad de opinión y la libertad de recibir o comunicar informaciones o ideas sin que pueda haber injerencia de autoridades públicas y sin consideración de fronteras».
- **Art. 11.2**: «**Se respetan la libertad de los medios de comunicación y su pluralismo.**»
- Art. 1: «**La dignidad humana es inviolable.**»
- Otras rúbricas: art. 8, «Protección de datos de carácter personal»; art. 22, «Diversidad cultural, religiosa y lingüística»; art. 42, «Derecho de acceso a los documentos».

### Ámbito y alcance (arts. 51-54)

- **Art. 51**:
  - Se dirige a las instituciones, órganos y organismos «dentro del respeto del principio de subsidiariedad», y «**a los Estados miembros únicamente cuando apliquen el Derecho de la Unión**». Es la salvedad más preguntable.
  - La Carta «**no amplía el ámbito de aplicación del Derecho de la Unión más allá de las competencias de la Unión, ni crea ninguna competencia o misión nuevas**».
- **Art. 52**, siete apartados:
  1. Limitaciones «**establecida[s] por la ley**», que respeten «**el contenido esencial**». Con respeto de la proporcionalidad, solo cuando «sean necesarias y respondan efectivamente a objetivos de interés general reconocidos por la Unión o a la necesidad de protección de los derechos y libertades de los demás».
  2. Los derechos que son disposiciones de los Tratados se ejercen en sus condiciones.
  3. Derechos equivalentes a los del CEDH: «**su sentido y alcance serán iguales**», sin impedir «una protección más extensa».
  4. Tradiciones constitucionales comunes: interpretación «en armonía» con ellas.
  5. Los **principios** «**Sólo podrán alegarse ante un órgano jurisdiccional en lo que se refiere a la interpretación y control de la legalidad**» de los actos que los aplican.
  6. Legislaciones y prácticas nacionales.
  7. Las explicaciones se tendrán «debidamente en cuenta».
- **Art. 53, «Nivel de protección»**: nada es «limitativa o lesiva» de los derechos reconocidos por el Derecho de la Unión, el internacional, el CEDH y «las constituciones de los Estados miembros».
- **Art. 54, «Prohibición del abuso de derecho»**.

## 11. Material reutilizable (RTVE)

El cruce `informes/canal-sur-reuso/comun-gestion.tsv` (puesto 0, tema 3) da un **5 %**: «Sólo actualidad de la UE y menciones a la Carta; ni TUE ni representación de la Junta ante la UE». Lo confirmo buscando en todo `temas/`. Ningún tema desarrolla el TUE ni la Carta. Lo aprovechable:

1. `temas/informacion/02-union-europea.md`, **«## 1. España en la Unión: el tratado de adhesión»**.
   - Tabla de fechas: firma el 12-VI-1985; «**Ley Orgánica 10/1985**» y «**artículo 93 de la Constitución**»; ratificación el 20-IX-1985; España es parte desde el 1-I-1986.
   - La frase: «la Unión Europea como tal no existía todavía; nace con el Tratado de Maastricht». Cuadra con la fórmula final del TUE y con su art. 54.2.
   - Sirve de introducción. No he releído el BOE de la adhesión.
2. El mismo tema, **«### Cuántos escaños elige España»**: «**61**», con la suma «22 + 20 + 6 + 3 + 3 + 3 + 2 + 1 + 1 = **61**». Está en formato de pregunta de examen. Hay que citar en su lugar la Decisión 2023/2061, art. 3.
3. El mismo tema, **«## 7. La zona del euro: por qué la página de hoy no vale para 2024»**: «el euro (€) es la moneda oficial de 21 de los 27 países de la UE». Glosa el art. 3.4. Es una página web leída el 02-09-2026 y habría que releerla.
4. `temas/informacion/08-resolucion-parlamento-europeo.md`, **«### Otros considerandos que conviene tener»**: «**Todos los Estados miembros deben respetar los valores del artículo 2 del TUE**». Solo como ejemplo.
5. `temas/general/01-constitucion-espanola.md`, **«### 5.3. Capítulo tercero. De los Tratados Internacionales»**: «**Artículo 93.** Mediante **ley orgánica** se puede autorizar la celebración de tratados **por los que se atribuya a una organización o institución internacional el ejercicio de competencias derivadas de la Constitución**. Es el artículo por el que España entró en las Comunidades Europeas.» Hay que releer el art. 93 CE vigente con `boe.py`; no lo he hecho.
6. **No reutilizable**: la «## 8. Lo que aquí sólo sostiene la plantilla» del tema 02 (Metsola, Kallas, Schengen). No tiene fuente y es actualidad de 2024.

## 12. Lo que no he podido confirmar

- La adhesión de la UE al CEDH.
- La fecha y el procedimiento de la retirada del Reino Unido. En consecuencia, el número actual de Estados no está confirmado en norma: el art. 3 de la Decisión 2023/2061 tiene 27 filas, lo que es un indicio.
- La vigencia de la Decisión 2013/336/UE.
- El número de jueces del Tribunal General. Lo fija el Estatuto (art. 254 TFUE), cuya redacción vigente no he leído.
- Los titulares actuales de las presidencias.
- El reparto de competencias de los arts. 2-6 TFUE.
- El enunciado frente al PDF del BOJA.

## 13. Ficheros tocados

- Creados: este informe y seis ficheros en `fuentes/canal-sur/documentos/`:
  - `tue-version-consolidada-doue-c202-2016.txt`
  - `carta-derechos-fundamentales-ue-doue-c202-2016.txt`
  - `tfue-version-consolidada-doue-c202-2016.txt`
  - `decision-ce-2023-2061-composicion-parlamento-europeo.txt`
  - `decision-ce-2013-272-numero-miembros-comision.txt`
  - `decision-consejo-2013-336-abogados-generales.txt`
- No he modificado ningún otro fichero.
