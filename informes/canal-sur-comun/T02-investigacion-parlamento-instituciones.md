# T02 · Investigación · Parlamento de Andalucía e instituciones de la Comunidad

Fase 1 (investigar). Rúbrica a) del punto 2, primera mitad: el Parlamento (composición, atribuciones, funcionamiento) y las instituciones (TSJA, Defensor del Pueblo, Cámara de Cuentas, Oficina contra el Fraude). Todo leído **el 24-09-2026**, redacción vigente ese día.

Siglas: Estatuto de Autonomía para Andalucía (**EAA**); Reglamento del Parlamento de Andalucía (**RPA**); Ley Orgánica del Poder Judicial (**LOPJ**); Tribunal Superior de Justicia de Andalucía (**TSJA**); Consejo General del Poder Judicial (**CGPJ**); Boletín Oficial del Parlamento de Andalucía (**BOPA**); «red.» = redacciones del precepto.

## 0. Fuentes

| Norma | Id. | Lectura |
|---|---|---|
| EAA (LO 2/2007) | BOE-A-2007-5825 | volcado; todos los preceptos citados aquí: 1 red. |
| Ley 1/1986, Electoral de Andalucía | **BOE-A-1986-2788** (localizado con `boe_buscar.py`) | volcado hoy en `fuentes/canal-sur/` |
| Ley 9/1983, Defensor del Pueblo Andaluz | BOE-A-1984-1847 | volcado |
| Ley 1/1988, Cámara de Cuentas | BOE-A-1988-8592 | volcado |
| Ley 2/2021, fraude y corrupción | BOE-A-2021-11380 | volcado |
| LO 6/1985, del Poder Judicial | **BOE-A-1985-12666** (localizado) | `boe.py precepto`; bloques en letra (art. 70 = `asetenta`) |
| RPA | BOE-A-2005-17677 (original) | **consolidado del Parlamento**: ver § 0.1 |

### 0.1. Reglamento vigente: el de 2005

- La web del Parlamento («Normas del Parlamento › Reglamento y otras normas») enlaza un único texto: «REGLAMENTO DEL PARLAMENTO DE ANDALUCÍA (Texto consolidado en vigor)». Según ese texto, fue «Aprobado por el Pleno del Parlamento el día 28 de septiembre de 2005», publicado en el BOPA núm. 292 de 4-X-2005, el BOJA núm. 198 y el BOE núm. 257 de 27-X-2005, con «ENTRADA EN VIGOR: 4 de octubre de 2005» y «TEXTO CONSOLIDADO VIGENTE DESDE: 22 de octubre de 2025». Lo he guardado en `fuentes/canal-sur/documentos/reglamento-parlamento-andalucia-consolidado-2025-10-22.pdf` y `.txt`.
- El BOE (2018-2026) solo devuelve el Acuerdo de 28-IV-2021 (BOE-A-2021-8034), que es una reforma. **No hay Reglamento posterior.** Los de 1991 y 1995 quedaron sustituidos.
- El BOE **no consolida** el RPA (`boe.py indice` → 404), así que no hay cadena de redacciones. Las redacciones del RPA se dan por las notas al pie del consolidado; donde no hay nota, 1 red. **presunta, sin confirmar**. Reformas listadas: 2007, 2008, 2009, 2010, 2012, 2014, 2017, dos en 2020 y 2021. Hay además notas que remiten a acuerdos de 15-V-2019 y 22-X-2025 sobre el art. 46: el de 2025 es la variación de Comisiones que el art. 46.4 permite «sin que dicha modificación se entienda como reforma de este Reglamento».

## 1. Parlamento: naturaleza y autonomía

- **EAA 99.1**: la Junta «está integrada por el Parlamento de Andalucía, la Presidencia de la Junta y el Consejo de Gobierno». **99.2**: también «las instituciones y órganos regulados en el Capítulo VI» (arts. 128-132).
- **100**: «representa al pueblo andaluz»; «es inviolable». **4.1**: sede en Sevilla.
- **102**: «plena autonomía reglamentaria, presupuestaria, administrativa y disciplinaria». Reglamento propio, cuya aprobación o reforma exige «la **mayoría absoluta** de los Diputados»; el Reglamento «establecerá el Estatuto del Diputado». Concuerda con la **RPA DA 1.ª**: la reforma se tramita «sin la intervención del Consejo de Gobierno», con «votación final de totalidad por mayoría absoluta».

## 2. Composición y elección

- **EAA 101.1**: «un **mínimo de 109** Diputados y Diputadas», por sufragio «universal, igual, libre, directo y secreto»; sin mandato imperativo. **101.2**: «elegido por **cuatro años**». Los titulares y suplentes de la Diputación Permanente se prorrogan «hasta la constitución de la nueva Cámara».
- **101.3**: inviolabilidad «aun después de haber cesado». No pueden ser detenidos «sino en caso de flagrante delito»; sobre «inculpación, prisión, procesamiento y juicio» decide el **TSJA**, y fuera de Andalucía la Sala de lo Penal del Tribunal Supremo.
- **104**: circunscripción, la provincia; «Ninguna provincia tendrá más del doble de Diputados que otra»; representación proporcional. Elecciones «entre los **treinta y sesenta días**» posteriores a la expiración; sesión constitutiva «dentro de los **veinticinco días**». Electores y elegibles, los andaluces «mayores de dieciocho años».
- **105**: ley electoral por **mayoría absoluta**, con «criterios de igualdad de género» y debates obligatorios en los medios públicos. **108**: mayoría absoluta del Pleno para las leyes de régimen electoral e instituciones básicas.
- **Ley 1/1986, art. 17** (1 red.): «**109 Diputados**»; «mínimo inicial de **ocho**» por provincia; los «**45** restantes» se reparten por población, con cuota = población de derecho / 45 y restos por mayor fracción decimal. 8 × 8 + 45 = 109: cuadra. **Art. 18.1** (1 red.): barrera del «**3 por 100** de los votos válidos emitidos en la circunscripción» y divisores «1, 2, 3, etc.». «D'Hondt» no aparece en la Ley.
- **Art. 14** (2 red.): convocatoria por Decreto del Presidente de la Junta; no se vota «entre los días 1 de julio a 31 de agosto». **Art. 23.1** (2 red., Ley 5/2005): listas alternas hombre-mujer, «cuatro candidatos suplentes».
- **Art. 4.3** (2 red.): son inelegibles, entre otros, el «Consejero Mayor» y los Consejeros de la Cámara de Cuentas, el Defensor del Pueblo Andaluz y sus Adjuntos, y el Director General de la «**Empresa Pública** de la Radio y Televisión de Andalucía». **Art. 6** (**5 red.**, vigente desde 28-X-2014): incompatibilidades y «dedicación absoluta». La Ley mantiene esos nombres antiguos: se citan tal cual.
- **RPA art. 5**: la condición plena de Diputado exige cuatro requisitos: credencial, declaración de incompatibilidades, declaraciones de bienes y actividades, y juramento o promesa. Pasadas «tres sesiones plenarias» sin cumplirlos, la Mesa suspende derechos. **Art. 19**: cinco causas de pérdida de la condición.

## 3. Atribuciones (EAA 106)

«Corresponde al Parlamento de Andalucía»: **19 ordinales**. Entre otros: potestad legislativa (1.º); impulso (2.º) y control del Consejo de Gobierno, con comisiones de investigación (3.º); presupuestos (4.º); tributos y deuda (5.º); elección del Presidente de la Junta (6.º); responsabilidad política (7.º); incapacidad del Presidente (8.º); Cuenta General, «sin perjuicio del control atribuido a la Cámara de Cuentas» (12.º); control de empresas públicas (14.º) y «de los medios de comunicación social dependientes de la Comunidad Autónoma» (15.º); recursos de inconstitucionalidad (16.º); Senadores (17.º).

- **107**: «principio de presencia equilibrada» en los nombramientos que hace el Parlamento.
- Con las relaciones con el Gobierno, quizá en la otra mitad de la rúbrica, que hay que coordinar: moción de censura por **mayoría absoluta**, propuesta por «una cuarta parte» y votada tras «cinco días» (126.1); cuestión de confianza por mayoría simple (125.1); convalidación de decretos-leyes en «treinta días» (110.2).
- **RPA 128.1**: la reforma del EAA exige en el Parlamento «los **tres quintos** de los miembros».

## 4. Organización y funcionamiento

**EAA 103**:
- Se elige de entre los miembros al Presidente, la Mesa y la Diputación Permanente.
- Funciona «en Pleno y Comisiones». El Pleno «podrá delegar en las Comisiones legislativas» y «podrá recabar en cualquier momento» los asuntos delegados; se reserva siempre las leyes «de contenido presupuestario y tributario» y las de mayoría cualificada.
- «Los períodos ordinarios serán **dos por año** y durarán un total de **ocho meses como mínimo**. El primero se iniciará en septiembre y el segundo en febrero».
- Los grupos participan en la Diputación Permanente y en todas las Comisiones «en proporción a sus miembros».

**RPA** (redacción entre paréntesis según las notas):
- **Sesión constitutiva**: la preside «el Diputado o Diputada electo de mayor edad», con «los dos más jóvenes» como Secretarios (art. 2).
- **Mesa**: «órgano rector de la Cámara»; «Presidente…, **tres Vicepresidentes y tres Secretarios**» (27). Funciones del art. 28 (reformado en 2014). Elección del Presidente (34.1): «mayoría absoluta»; si no, entre los dos más votados. Si el empate persiste «después de cuatro votaciones», gana el candidato de los grupos «con mayor respaldo electoral». Se repite la elección si los contencioso-electorales cambian «más del 10%» de los escaños (33.2).
- **Grupos**: al menos «**cinco**» Diputados (20.1, reformado en 2014); se constituyen en «cinco días» (21.1). Quien no se integra es «no Adscrito», salvo el caso del Grupo Mixto (22.2).
- **Junta de Portavoces**: se reúne «al menos, quincenalmente» y decide por «voto ponderado» (38).
- **Comisiones**: quórum de dos miembros de la Mesa más «la mitad más uno» (42.3). Plazo de «dos meses» por asunto (43.3). Hay **14** permanentes legislativas (46.1, texto de 22-X-2025) y **6** permanentes no legislativas (46.2), entre ellas la «Consultiva de Nombramientos, Relaciones con el Defensor del Pueblo Andaluz y Peticiones» y la de «Control de la Agencia Pública Empresarial de la Radio y Televisión de Andalucía». Las de investigación (52) las piden el Consejo de Gobierno, un grupo o «la décima parte»; el Pleno las rechaza solo «si se opone la mayoría de los miembros»; sus conclusiones «no serán vinculantes para los tribunales».
- **Pleno**: lo convoca el Presidente o se convoca a petición de «dos Grupos parlamentarios o de una quinta parte de los Diputados» (55).
- **Diputación Permanente** (57-59): Mesa más miembros en proporción; actúa en vacaciones, disolución o expiración, y convoca al Pleno «por acuerdo de la mayoría absoluta» (58).
- **Sesiones** (67, reformado en 2014): «del 1 de septiembre al 31 de diciembre y del 1 de febrero al 31 de julio». Extraordinarias a petición de «una cuarta parte de los Diputados o de dos Grupos», o del Presidente de la Junta o del Consejo de Gobierno. Pleno público (69). Comisiones no públicas, con medios acreditados; secretas las del Estatuto de los Diputados y las de investigación, salvo comparecencias (70).
- **Votaciones**: quórum de «la mayoría de sus miembros» (84.1). Mayoría simple: «los votos positivos superen los negativos, sin contar las abstenciones, los votos en blanco y los nulos» (85.2). Mayoría absoluta: «el primer número entero de votos que sigue al número resultante de dividir por dos el total de los miembros de pleno derecho» (85.3). El art. 85 se reformó en 2009.
- **Nombramientos**: el Defensor, «de acuerdo con el procedimiento establecido en la ley reguladora» (181). Los demás, con disposiciones de la Mesa y acuerdo de la Junta de Portavoces «por mayoría al menos de tres quintos» (182).

## 5. Tribunal Superior de Justicia de Andalucía

- **Naturaleza** (EAA 140.1): «el órgano jurisdiccional en que **culmina la organización judicial en Andalucía**», competente en los órdenes «civil, penal, contencioso administrativo, social». **140.2**: «última instancia jurisdiccional de todos los procesos judiciales iniciados en Andalucía… sin perjuicio de la competencia reservada al Tribunal Supremo». **140.3**: unificación del derecho de Andalucía; el BOE dice literalmente «Tribunal de Justicia de Andalucía», sin «Superior». **LOPJ 70** (1 red.): «culminará la organización judicial». **Sede** (EAA 4.2): «**Granada**, sin perjuicio de que algunas Salas puedan ubicarse en otras ciudades».
- **Composición** (LOPJ 72, 1 red.): Salas «de lo Civil y Penal, de lo Contencioso-Administrativo y de lo Social». El Presidente, que preside también la Civil y Penal, tiene «la consideración de Magistrado del Tribunal Supremo mientras desempeñe el cargo». Salas con jurisdicción limitada a varias provincias: art. 78 (1 red.), «con carácter excepcional».
- **Presidente**: EAA 143.1: «representante del Poder Judicial en Andalucía… nombrado por el Rey, a propuesta del Consejo General del Poder Judicial con la participación del Consejo de Justicia de Andalucía». **LOPJ 336.1** (3 red., vigente desde 18-I-2019, LO 4/2018): «cinco años renovable por un único mandato de otros cinco años», entre magistrados con «diez años» en la categoría y «quince años» en la Carrera.
- **Terna parlamentaria** (LOPJ 330.4, **8 red.**, vigente desde 23-I-2025, LO 1/2025): en la Sala de lo Civil y Penal, «una de cada tres plazas se cubrirá por un jurista de reconocido prestigio con más de 10 años de ejercicio profesional en la comunidad autónoma, nombrado a propuesta del Consejo General del Poder Judicial sobre una terna presentada por la Asamblea legislativa».
- **Competencias estatutarias** (EAA 142): **cinco ordinales**. La responsabilidad de los Diputados (101.3) y de los Consejeros (122); los recursos electorales autonómicos; los conflictos de jurisdicción entre órganos de la Comunidad; las cuestiones de competencia entre órganos judiciales andaluces; los conflictos de atribuciones entre Corporaciones locales. La responsabilidad del **Presidente de la Junta** va al **Tribunal Supremo** (118.5).
- **Competencias legales**: LOPJ 73 (Civil y Penal, **9 red.**), 74 (Contencioso, 5 red.; incluye los actos de administración de las Asambleas legislativas y de las instituciones «análogas al Tribunal de Cuentas y al Defensor del Pueblo») y 75 (Social, 3 red.). Los tres, vigentes desde 23-I-2025 (LO 1/2025), sin reformas cruzadas en la cadena.
- **Gobierno interno**: Sala de Gobierno (LOPJ 149.2, 4 red.). **Memoria anual** del Presidente «ante el Parlamento de Andalucía» (EAA 143.3).
- **Consejo de Justicia de Andalucía** (EAA 144): está en el EAA, pero **no aparece en el índice de la LOPJ vigente**. No se puede confirmar que funcione; en el tema, solo el texto estatutario con esa salvedad.

## 6. Defensor del Pueblo Andaluz

- **Naturaleza** (EAA 128.1): «comisionado del Parlamento» para los derechos del Título I de la Constitución «**y en el Título I del presente Estatuto**»; supervisa «las Administraciones públicas de Andalucía». La **Ley 9/1983, art. 1.1** (1 red.) solo menciona la Constitución y la «Administración Autonómica»: manda el EAA. El Defensor colabora con el Defensor del Pueblo estatal (EAA 128.3).
- **Elección**: el EAA 128.2 dice «por **mayoría cualificada**» y remite a una ley. **Ley 9/1983, art. 2** (2 red., vigente desde 19-VII-1996):
  - mandato de «**cinco años**»;
  - la Comisión propone al candidato con voto ponderado;
  - el Pleno se reúne «en término no inferior a **quince días**»;
  - se exigen «las **tres quintas partes** de los miembros del Parlamento»;
  - si no se alcanzan, nuevas propuestas «en el plazo máximo de un mes».
  - **No hay segunda votación con mayoría rebajada.**
- **Requisitos** (art. 3, 1 red.): condición política de andaluz, «con arreglo al artículo 8.º del Estatuto». La remisión es al Estatuto de 1981; hoy es el art. 5.
- **Nombramiento**: lo acredita el Presidente del Parlamento, se publica en el BOJA y toma posesión ante la Mesa (art. 4).
- **Cese** (art. 5, **3 red.**, vigente desde 6-VI-2001): **seis causas**.
  - Las declara el Presidente del Parlamento «en los casos de renuncia, expiración del plazo de mandato, de muerte, incapacidad sobrevenida e inhabilitación absoluta o especial».
  - En los demás casos, «por mayoría de los tres quintos de los diputados, mediante debate y previa audiencia del interesado».
  - Al expirar el mandato sigue en funciones.
- **Estatuto personal**: «no estará sujeto a mandato imperativo alguno. No recibirá instrucciones de ninguna autoridad» (art. 6). Incompatibilidades del art. 7 (2 red.); cese en ellas en «diez días».
- **Adjuntos** (art. 8, **6 red.**, vigente desde 30-VIII-2021, BOE-A-2021-13605): «**tres** personas adjuntas»; una auxilia como «Defensor o Defensora de la Infancia y Adolescencia». Los nombra el Defensor con la conformidad de la Comisión.
- **Quejas y procedimiento**:
  - pueden presentarlas «toda persona, natural o jurídica, que invoque un interés legitimo, sin restricción alguna» (11.1, 2 red.);
  - plazo de «**un año**»; son gratuitas y no requieren abogado (16);
  - se rechazan las anónimas (17.3);
  - no entra en asuntos pendientes de resolución judicial (17.2);
  - el organismo informa en «quince días» (18.1);
  - responde a recomendaciones y advertencias «en término no superior a un mes» (29.1);
  - no puede «modificar o anular» actos (28.1);
  - las quejas sobre Justicia van al Fiscal o al CGPJ (15);
  - puede instar un recurso de inconstitucionalidad del Defensor estatal (26).
- **Relación con el Parlamento**: informe anual «en el período ordinario de sesiones», publicado en el BOPA (31). Se trata en Comisión y en Pleno, sin propuestas de resolución (RPA 183). Su personal es del Parlamento (34) y su presupuesto, una partida del Parlamento (35).
- **Discordancia**: la Ley (arts. 2, 5, 7, 8, 9) cita la «Comisión de Gobierno Interior y Derechos Humanos… artículo 48 del Reglamento». En el RPA vigente es la **Comisión Consultiva de Nombramientos, Relaciones con el Defensor del Pueblo Andaluz y Peticiones (art. 49)**: la Mesa más un Diputado por grupo, con voto ponderado.

## 7. Cámara de Cuentas de Andalucía

- **Naturaleza**: EAA 130: «órgano de **control externo** de la actividad económica y presupuestaria de la Junta de Andalucía, de los entes locales y del resto del sector público», que «depende **orgánicamente** del Parlamento». Ley 1/1988, art. 1 (1 red.): «órgano técnico dependiente del Parlamento», «sin perjuicio» del Tribunal de Cuentas.
- **Ámbito** (art. 2, 4 red.): Junta, Corporaciones Locales, Universidades públicas y demás entidades.
- **Funciones** (art. 4, 1 red.), «con total independencia»: fiscalizar la actividad económico-financiera, en todo caso las subvenciones; los objetivos; asesorar al Parlamento; los contratos. Ejerce además funciones delegadas del Tribunal de Cuentas. El 4.3 conserva la cifra en pesetas.
- **Iniciativa**: la tienen la Cámara y el Parlamento; pueden «interesarla» el Gobierno y las Entidades Locales (art. 6, 3 red.). La Comisión la pide por mayoría simple que represente «al menos, la tercera parte» (34).
- **Plazos**: Cuenta General «antes del **31 de octubre**»; cuentas locales «antes del primero de noviembre»; examen «dentro del plazo de tres meses» (art. 11, **6 red.**, vigente desde 1-I-2026, BOE-A-2026-945). Memoria «antes del 1 de marzo» (35). Indicios de responsabilidad contable, «sin dilación» al Tribunal de Cuentas (12.3).
- **Órganos** (art. 16, 2 red.): **seis**. Pleno de «**siete Consejeros**», que no se constituye sin el Presidente o el Vicepresidente y cuyos empates dirime el Presidente (17, 3 red.). Comisión de Gobierno: Presidente, Vicepresidente y dos Consejeros (18).
- **Elección** (art. 24, 3 red., vigente desde 7-V-2011):
  - los Consejeros los designa el Parlamento «por mayoría de **tres quintas partes** de sus miembros, por un período de **seis años**, renovándose cada tres por tres y cuatro séptimas partes sucesivamente»;
  - todos los grupos, salvo el Mixto, tienen derecho a que al menos uno proceda de su propuesta;
  - la **Presidencia** la nombra «el Presidente de la Junta de Andalucía, a propuesta del Pleno de la Cámara», por «tres años», reelegible;
  - la **Vicepresidencia**, el Pleno de la Cámara, también por tres años.
- **Estatuto de los Consejeros**: «independencia e inamovilidad»; «reconocida competencia profesional» (25). Incompatibilidad total salvo la administración del patrimonio propio (26). Causas de cese tasadas (27, 2 red.).
- **Tramitación parlamentaria**: RPA 184-187. **Discordancias**: el RPA y la Ley electoral dicen «Consejero Mayor» (hoy, «Presidencia»). La Ley llama a la comisión «Hacienda y Presupuestos»; el RPA, «Hacienda y Administración Pública»; la lista de 2025, «Economía, Hacienda, Fondos Europeos y Diálogo Social».

## 8. Oficina Andaluza contra el Fraude y la Corrupción

- **No está en el EAA**; la crea la **Ley 2/2021**.
- **Naturaleza** (art. 6, 1 red.): «entidad de derecho público, con personalidad jurídica propia»; «se adscribe al Parlamento de Andalucía»; actúa «con plena autonomía e independencia funcional».
- **Régimen** (art. 8): un reglamento de régimen interior que propone el Director y **aprueba el Parlamento**.
- **Funciones** (art. 9, 2 red., vigente desde 1-I-2023): **16 letras (a-o, con ñ)**. Entre ellas: investigación e inspección; denuncias y protección del denunciante; recomendaciones, con respuesta en «treinta días»; potestad sancionadora, incluida la de la Ley 3/2005 de altos cargos. Actúa «sin perjuicio» de la Cámara de Cuentas y del Defensor (12.1). No ejerce funciones judiciales y suspende sus actuaciones si actúan el juez o el Fiscal (12.2).
- **Dirección, elección** (art. 25, 1 red.):
  - la elige el Pleno «por mayoría de **tres quintas partes**»;
  - si no se alcanza, «una segunda votación en un plazo **no inferior a quince días**» por **mayoría absoluta**;
  - se exigen «más de **diez años** de experiencia»;
  - los grupos proponen a los candidatos, que comparecen ante la comisión;
  - la **nombra la Presidencia del Parlamento**;
  - el mandato es de «**cinco años**… y **no será renovable**».
- **Cese** (art. 28): **siete causas**. Por negligencia, «mayoría de **dos terceras partes**»; en segunda votación, absoluta. Al expirar el mandato sigue en funciones, y el sucesor toma posesión en «tres meses».
- **Incompatibilidades** (art. 27): siete letras, y dos años de restricciones después del cargo.
- **Organización**: al menos **dos subdirecciones** (29). Funcionarios con el régimen del personal del Parlamento (31). Presupuesto en la sección del Parlamento «como programa específico» (32).
- **Procedimiento**: de oficio. Resolución en «seis meses», ampliable «en tres meses más», con un máximo de «nueve meses» (23.1, 2 red.). Se admiten las denuncias anónimas (DA 2.ª).
- **Relación con el Parlamento**: memoria anual «en los tres primeros meses» y comparecencia (33); informes especiales (34). **DT 2.ª**: hasta que se reforme el RPA, sus relaciones corresponden a la Comisión Consultiva de Nombramientos. El RPA a 22-X-2025 no ha creado otra comisión: la DT 2.ª sigue en vigor.

## 9. Cuadro de mayorías

| Órgano | Elige / nombra | Mayoría | Mandato | Precepto |
|---|---|---|---|---|
| Parlamento | electores | — | 4 años | EAA 101.2 |
| Presidente del Parlamento | Pleno | absoluta; luego, la más votada entre dos | — | RPA 34.1 |
| Defensor del Pueblo Andaluz | Pleno | 3/5, sin rebaja | 5 años | L 9/1983, 2 |
| Consejeros de la Cámara de Cuentas (7) | Parlamento | 3/5 | 6 años | L 1/1988, 24.1 |
| Presidencia de la Cámara de Cuentas | Presidente de la Junta, a propuesta del Pleno de la Cámara | — | 3 años | 24.2 |
| Director de la Oficina | Pleno; nombra la Presidencia del Parlamento | 3/5; luego absoluta | 5 años, no renovable | L 2/2021, 25 |
| Presidente del TSJA | el Rey, a propuesta del CGPJ | — | 5 + 5 | EAA 143.1; LOPJ 336 |

## 10. No confirmado (fuera del tema salvo que se lea)

1. Si el Consejo de Justicia de Andalucía funciona: la LOPJ no lo regula. Tampoco he leído la jurisprudencia que suele citarse.
2. La planta del TSJA (número de magistrados, Salas de Sevilla y Málaga): la Ley de Planta no está leída.
3. El reparto concreto de escaños por provincia y el número de Senadores autonómicos.
4. El número de redacciones de los artículos del RPA: lo da solo el consolidado del Parlamento, no el BOE.
5. Si están aprobados el reglamento interno de la Oficina y el nombramiento de su Director.
6. «D'Hondt» y «suplicatorio» no están en la fuente: en redonda o fuera.

## 11. Discordancias

- **No hay Reglamento posterior a 2005**, contra lo que sugiere el encargo.
- Las Leyes 9/1983 y 1/1988 y la Ley electoral conservan nombres superados (Comisión de Gobierno Interior; Hacienda y Presupuestos; «Consejero Mayor»; «Empresa Pública» de la RTVA; art. 8.º del Estatuto de 1981). Se citan literales, con una nota.

## Ficheros tocados

- Este informe.
- Volcado nuevo: `fuentes/canal-sur/BOE-A-1986-2788.md` y `.redacciones.tsv`.
- `fuentes/canal-sur/documentos/reglamento-parlamento-andalucia-consolidado-2025-10-22.pdf` y `.txt`.
- No he añadido BOE-A-1986-2788 a `volcar.sh`.
