# Tema 5 · III Convenio Colectivo de la Corporación RTVE

Esqueleto para repasar. Todo lo de aquí está desarrollado y verificado en
`temas/general/05-convenio-colectivo.md`.

<!-- indice -->

## Índice

- [Identificación](#identificación)
- [Las dos trampas de numeración](#las-dos-trampas-de-numeración)
- [Capítulos](#capítulos)
- [Cap. I-V · lo que cae](#cap-i-v--lo-que-cae)
- [Cap. VI · Tiempos de trabajo (el más preguntado)](#cap-vi--tiempos-de-trabajo-el-más-preguntado)
- [Cap. VII · Retribuciones](#cap-vii--retribuciones)
- [Cap. VIII · Disciplinario (el segundo más preguntado)](#cap-viii--disciplinario-el-segundo-más-preguntado)
- [Cap. IX-XIII](#cap-ix-xiii)
- [Disposiciones](#disposiciones)
- [Anexos](#anexos)

<!-- /indice -->

## Identificación

**Cuatro documentos anteriores al corte**, no tres:

- **BOE-A-2020-16744** · Resolución 15/12/2020 · BOE 332 de **22/12/2020** · texto del convenio, **anexos 1-6**.
- **BOE-A-2021-1334** · 29/01/2021 · corrección de errores: **añade el anexo 7** (factores personales y de arraigo).
- **BOE-A-2021-8252** · 18/05/2021 · **sustituye entero el anexo 7** por el **baremo del art. 14.3**. **Es el vigente al corte.**
- **BOE-A-2022-20256** · acuerdo de 10/11/2022 · BOE núm. 289, de **02/12/2022** · modifica **12, 13, 16, 17, 18, 21, 27, 30, 63, 102**, nueva **DT 8.ª**, nueva **DT 10.ª**, **anexo 8**.

**Después del corte** (no examinable, pero desactualiza cualquier material reciente): **BOE-A-2023-9620** (corrige el anexo 3) · **BOE-A-2023-17840** (arts. **42, 50, 52, 57, 72, 91**, DT 3.ª y 9.ª, DF 1.ª) · **BOE-A-2024-4470** (arts. 13, 18, 21, 99.3 y 4, anexo 1, DT 8.ª, DF 1.ª) · **BOE-A-2025-24095** (cap. III entero, arts. 102 y 104.5, anexos 7 y 8, añade DT 11.ª y 12.ª).
- **No es legislación consolidada**: no hay texto refundido oficial. `boe.py` no sirve.
- **116 artículos · 13 capítulos · 3 DA · 9+1 DT · 1 DF · 1 derogatoria · 8 anexos.**

## Las dos trampas de numeración

- **Arts. 16 y 17 intercambiados en 2022**: hoy **16 = reingreso de excedentes**, **17 = promoción / cambio de ocupación tipo**.
- **Art. 63.5**: 2020 = prácticas **70 / 80**; 2022 = **alternancia 60 / 75** y **práctica profesional 70**. Los 70/80 sobreviven en la **DT 10.ª** para los ya contratados.

## Capítulos

| | Cap. | Arts. |
|---|---|---|
| I | Disposiciones generales | 1-7 |
| II | Comisión de producción interna | 8-9 |
| III | Empleo | 10-32 |
| IV | Formación | 33-35 |
| V | Clasificación profesional | 36-40 |
| VI | **Tiempos de trabajo y descanso** | 41-62 |
| VII | **Sistema retributivo** | 63-77 |
| VIII | **Derechos y deberes. Régimen disciplinario** | 78-90 |
| IX | Actividades sindicales | 91 |
| X | Seguridad y salud laboral | 92-95 |
| XI | Suspensión y extinción | 96-99 |
| XII | Situaciones del personal | 100-107 |
| XIII | Actividades sociales | 108-116 |

## Cap. I-V · lo que cae

- Cinco exclusiones del ámbito personal · tope de **25 contratos** de alta dirección.
- **Comisión paritaria 7+7**, quórum **4 por parte**, resuelve en **10 días**. Mediación **obligatoria si la pide una parte**; **arbitraje voluntario**.
- **Art. 7**: ordenación del trabajo = facultad exclusiva, **sin perjuicio de los derechos de la RLT**.
- **Art. 14 traslados**: forzoso (no sobre quien tenga **≥5 años**) / convenido (**1 año prorrogable a 3**, **salvo el motivado por traslado forzoso del cónyuge, que es indefinido**) / **voluntario: fijo + misma ocupación tipo + 1 año de permanencia (2 el segundo)**. Baremo, **tres criterios**: **a)** antigüedad máx. **35 pts** (0,5/año empresa máx. 10 · 0,5/año ocupación tipo máx. 10 · **1 pt/año en el registro, máx. 15**) · **b)** enfermedad, discapacidad o dependencia **12 pts**, solo con acreditación oficial · **c)** **agrupación familiar 8 pts**. Los baremos de b) y c), **en el anexo 7**. Empate → **sexo menos representado** en esa ocupación tipo y destino. Traslado **inmediato**; incorporación hasta **8 meses** por causa motivada; **adjudicada y definitiva, no cabe renuncia**.
- **Art. 15 registro de traslados**: inscripción previa imprescindible · **validez 3 años** renovables.
- **Art. 23 comisión de destino**: puestos **no permanentes en organismos oficiales**, temporal, **se sigue en activo**.
- **Art. 32 período de prueba**: **>6 meses → 3 meses**; **≤6 meses y duración incierta → 1 mes**. Cualquiera de las partes puede terminar **sin preaviso y sin indemnización**, **salvo las retribuciones devengadas**; informe del mando en **7 días naturales**; superado, **computa a todos los efectos**.
- **Art. 36-38**: **dos grupos**, **trece ámbitos ocupacionales**. Ámbito ≠ ocupación tipo. Salen del **anexo 3, que el BOE publica como imagen** (transcrito en `fuentes/convenio/imagenes/`).
  - **Realización** → ámbito **Producción de contenidos audiovisuales y multimedia** (Grupo I). **Realización (asistencia)** → ámbito **Realización y edición audiovisual** (Grupo II). El examen cruza las dos.
- **Art. 39 movilidad funcional**: a grupo superior **máx. 6 meses en un año u 8 alternos en dos**, sin consolidar, cobrando lo que se hace; a inferior, **manteniendo el salario consolidado**.

## Cap. VI · Tiempos de trabajo (el más preguntado)

- **41**: jornada = tiempo obligado; horario = instrumento de concreción. Distribución irregular: **máx. 7 jornadas/año**, **nunca Nochevieja ni Navidad**, **preaviso 5 días**.
- **42**: **37,5 h semanales / 7,5 diarias**, cómputo **anual** (DA 144.ª Ley 6/2018). Cuadrantes **mensuales, día 25**. Temporal = fijo.
- **43 horarios**: continuado (**15 min de descanso = trabajo**) · con pausa (**mín. 1 h, no es trabajo**; sin comedor **+30 min recuperables**; imposible parar → **20 min computados**) · **nocturno 22:00-07:00** · a turnos.
  - **Desayuno**: jornada entre **4:00 y 7:00**. **Comida**: empieza antes de **13:30** y acaba después de **15:30**. **Cena**: antes de **21:00** / después de **22:30**.
  - Trabajador nocturno: **≥3 h diarias** o **≥1/3 de la jornada anual**. Rotación **≤2 semanas**.
  - **Descanso entre jornadas: 12 h** · festivos trabajados **antes de un año** · horas extras compensadas **en 4 meses** · **PVD: 10 min cada 2 h**, no acumulables (única regla no adaptable).
- **44 conciliación** (a-n): lactante **5 semanas** · guarda legal **1/8 a 1/2** · menor con cáncer **≥1/2 hasta los 18** · flexibilidad **1 h** (menores de 14) y **2 h** (discapacidad ≥33 %) · RRHH hasta **2 h** · **bolsa por discapacidad: 30 h (≥33 %) / 130 h (≥65 %)**, no recuperable, preaviso **48 h**, tope **4 h/día** · **bolsa general del 5 % de la jornada, recuperable en 3 meses** · desconexión: solo variabilidad, **hasta las 20:00** · **24 y 31 de diciembre**.
- **45**: **doce** complementos con variabilidad horaria.
- **46**: cómputo **mensual** · diaria **5 a 10 h** · semanal **máx. 50 h** · **10 días de trabajo en 14**, descanso mínimo **2 consecutivos**; **10 seguidos → 4 días ininterrumpidos** · **2 fines de semana libres al mes**.
- **47 / 48**: **obligación**, no facultad. Tope **anual** (mando orgánico) vs **mensual** (especial responsabilidad).
- **49 disponibilidad**: respeta **12 h**. Opción 1 (día 25, **inamovible**) · 2 (**3 cambios**, replanificación **día 8**, no afecta a descansos) · 3 (**voluntaria**, compromiso **trimestral**). Preaviso **24 h**; prolongación **4 h antes**; **máx. 3 días/mes**; descansos y fines de semana **5 días**.
- **50 turnicidad**: cadencia **semanal**; jornada tipo = la letra **b)** (duración distinta, previo acuerdo con la RLT); cambios **máx. 2 días/mes**; imprevisto → ampliación **máx. 3 h**, nunca más de **10 h**.
- **51 guardias**: **voluntarias**; sin voluntarios, **rotatorias** para edificios y señales. **No retribuyen horas extras.** Máx. **2 periodos/mes**.
- **52 fin de semana**: **3 días**, **máx. 11 h/día**, **30 h = 37,5 h**. Rotación **máx. 4 meses**. Festivos de **viernes o lunes**.
- **54 rodaje**: no se aplican jornada ni descanso del convenio; **máx. 12 h efectivas**. **55 pactos**: negociados **10 días antes**, obligatorios.
- **57 comisión de servicio**: **≥45 km** · obligatoria con **72 h** · **45 días nacional / 2 meses extranjero, +30**. Viaje: solo viajar → **máx. 10 h = una jornada**; conduciendo **>6 h → jornada ≤7,5 h**. Pernocta: **≥10 h**, o vuelta **desde las 22:00 con más de 2 h**, o decisión por seguridad.
- **59 horas extras**: **aceptación previa del interesado**; **la mitad** compensable con **+75 %** en **4 meses**.
- **60 vacaciones**: **25 días laborables** · preferente **1 jun - 30 sep** · pendientes **hasta el 15 de enero** · **+3 días** (turnicidad 20-24 h y Canarias/Baleares/Ceuta/Melilla) · **+1 día** si la mitad va fuera del preferente · fraccionamiento **≥50 % en un periodo** · preferencia por **antigüedad**, luego **edad**, durante **4 años** · solicitud **antes del 1 de abril**, respuesta **antes del 1 de mayo**, fuera de plazo **15 días**.
- **61 licencias**: matrimonio **15 naturales** · fallecimiento **3 laborables, 5 fuera de provincia** · enfermedad grave **igual, discontinuos** · **desde 2021: 16+16+16 semanas, 6 obligatorias, 10 voluntarias, cesión NO** · lactante **hasta 9 meses**, ampliable a **12** si ambos · deber personal **≤1/5 de las horas del trimestre** · particulares **3 días**, caducan · exámenes **1 día, 2 fuera de la comunidad** · traslado **1 / 2 días** · acompañamiento médico no recuperable **4 h/día, 28 h/año**, ampliable a **42**. No retribuida: **1 vez al año, ≤3 meses, 2 periodos**, no computa a antigüedad ni vacaciones. **Solo la baja médica justifica ausencia por enfermedad.**
- **62**: teletrabajo → **anexo 5**.

## Cap. VII · Retribuciones

- **63**: salario = toda percepción, dinero o especie. No lo son: indemnizaciones, prestaciones de SS, jubilación voluntaria, traslados y despidos. Pago **por mensualidades vencidas**, **salvo los complementos de periodicidad superior al mes**.
- **64 anticipos**: **≤90 % del líquido mensual**, **máx. 10 al año** · **3 especiales**, **2 mensualidades** de base + antigüedad, **reintegro en 4 meses (≥10 % cada uno)** · incompatibles con especiales pendientes.
- **65 salario base**: **18 niveles** (A-F × 1-3). Básico **D1** (Grupo I-I, 12 niveles), **E1** (Grupo I-II, 15), **F1** (Grupo II, 18). Techo **A3**, que consolida **+3 % cada 4 años**. Saltos: **0,5, 1, 2 y luego 3 años**. Requisitos: **permanencia + cursos superados**.
- **66 complementos**: **valores 1 a 4** (A/B=1; C/D en I-I=2; C/D en I-II=3; E/F=4). **Cinco clases**: personales · **de puesto (no consolidables)** · calidad y cantidad · vencimiento superior al mes (**pagas de junio y diciembre**) · **residencia (Baleares, Canarias, Ceuta, Melilla)**.
- **67 gratificación absorbible**: mando orgánico **>2 años**, **25 %** durante **2 años**, absorbible **salvo trienios**.
- **68 complemento de convenio**: **14 mensualidades**, solo altas **anteriores al 1/1/2014**.
- **70 antigüedad**: **trienio**, consolidable, solo **servicio efectivo**, desde el **día 1 del mes**.
- **71 puestos** (doce): mando orgánico requiere **2 años de antigüedad, sin sanciones vivas, formación y experiencia**; **acción positiva** por sexo menos representado. Disponibilidad **tipo 1 / 1+2 / 1+3**. **Polivalencia = distintos ámbitos, mismo grupo.** Rodaje **por país** (UE, renta alta, renta baja, **seguridad**, **conflicto**), lista actualizada por la **Comisión paritaria**. **Idiomas: 100 % uno, 200 % dos o más.**
- **72 calidad/cantidad**: **festivo** (y Nochebuena/Nochevieja **20:30-01:00**) · **hora extra = bruto anual con prorratas ÷ horas anuales del centro**; festiva **+1/7,5 del complemento de festivo** · formación (**Instituto RTVE**) · tribunales · **comidas con copago del 50 %**; **no usar el comedor no da derecho al abono**.
- **73**: **nocturnidad por cada hora entre las 22:00 y las 7:00**.
- **74 pagas extras**: **dos**, junio y diciembre = **base + antigüedad + complemento de convenio**. Devengo **1 ene-30 jun** y **1 jul-31 dic**.
- **75 dietas**: **≥45 km** · cuantía **única** · hotel **3 estrellas, doble de uso individual** · **contra factura**; pernocta **<24 h → dieta completa** · sin pernocta **>9 h → comida y cena**; **≤9 h → según los tramos 13:30/15:30 y 21:00/22:30** · **>24 h → dieta completa por cada 24 h** · extranjero: **desde la llegada al país hasta la llegada a España** · cursos obligatorios **a ≥45 km = comisión de servicio**.
- **77**: IT, permiso por nacimiento y riesgo en el embarazo → **100 % de la retribución básica** de los **12 meses anteriores** + parte proporcional de extras.

## Cap. VIII · Disciplinario (el segundo más preguntado)

- **78**: **13 derechos** (defensa en el expediente, secreto profesional como derecho y deber). **79**: **10 deberes** (respetar la Constitución; informar de dolencias, **cuya omisión exonera a RTVE**).
- **80**: indicios penales → **suspende la tramitación**; cautelares: **suspensión de empleo máx. 30 días** (prórroga **por acuerdo**) y **movilidad**. **El proceso penal y la suspensión interrumpen la prescripción.**
- **81**: **importancia, intencionalidad y trascendencia**.

| | Leve (82) | Grave (83) | Muy grave (84) |
|---|---|---|---|
| Retraso | **>5 y <10 min**, 3 veces en 60 días | **>30 min**, 3 veces en 60 días | — |
| Inasistencia | **1 día** en un mes | **2 a 4 días** en un mes | **5 o más** en 6 meses |
| Reiteración | — | 2 faltas leves en **3 meses** | 2 faltas graves en **1 año** |
| Nº de tipos | 11 | 15 | 26 |
| **Sanción (85)** | **amonestación** o **1-2 días** | **3-15 días** | **16-30**, **31-60** o **despido** |

- **86 procedimiento**: la ejerce la **Presidencia**, delegable · **días hábiles** · graves y muy graves: pliego **+ 7 días** → propuesta **+ 7 días** → resolución, todo **con traslado a la RLT** · **IT o vacaciones suspenden hasta 3 meses e interrumpen la prescripción** · se puede apartar del servicio **cobrando** · leves: **4 días** para alegar, **efectos suspendidos**, resolución **≤7 días**.
- **87 notificación**: preferentemente **en el centro**; la firma **no es conformidad**; **un solo segundo intento**; **dos fallidos o rechazo → trámite cumplido**.

| | Leves | Graves | Muy graves |
|---|---|---|---|
| **Prescripción de la infracción (88)** | **10 días** | **20 días** | **60 días** |
| **Prescripción de la sanción (89)** | **15 días** | **1 mes** | **2 meses** |

- **90 cancelación**: **al año**, **sin reincidencia** y **a solicitud del interesado** (no es automática), desde el **fin del cumplimiento**.

## Cap. IX-XIII

- **91**: **«más representativo» = 10 %** · escala de delegados **50-250: 1 · 251-750: 2 · 751-2.000: 4 · >2.000: 11** (**en suspenso** por el RDL 20/2012) · **Madrid = un solo centro** · mínimo **7 h** si el centro tiene ≤25 personas · bolsa: tope **+100 %**, más **7.000 h** de la empresa · **4 asambleas/año**, preaviso **48 h** · **Comité Intercentros: 12 personas, 40 h/mes absorbentes** · elecciones **provinciales**, **20 de marzo de 2024**.
- **92-95**: ámbito **sin exclusiones, incluidas subcontratas** (art. 24 LPRL) · **CGSSL paritario: 8 + 8 = 16**; **CSSL en centros de ≥50** · formación preventiva **en la contratación, dentro de jornada, coste nunca del trabajador** · protocolos de **violencia psicológica** y **drogodependencias** · **severidad muy alta**: solo con otra persona cualificada del mismo grupo.
- **96 suspensión**: 7 causas · violencia de género **6 meses, hasta 18 por el juez** · IP total revisable **+2 años de reserva** · **1 a 12 meses ampliables 12** por estudios, ONG o **UER**, sin computar ni cotizar.
- **97 extinción**: 10 causas · **abandono >10 días naturales = baja voluntaria**. **98**: preaviso de **15 días**; se pierden **todos los derechos**.
- **99 jubilación**: forzosa al **100 % de la pensión**, **sin indemnización**; voluntaria y anticipada: **2.084 €/mes**, tope **50.000 €**, **5 años previos** en activo, solicitud **6 meses antes**; reposición con convocatoria **≤18 meses**; **si los PGE lo impiden, decae la jubilación forzosa**.
- **100-107**: activo o excedencia · **102 voluntaria**: **1 año** de antigüedad, concesión **≤30 días**, **4 meses a 10 años**, nueva tras **4 años**, reingreso desde los **4 meses**, se pierde si no se pide **1 mes antes**; **2022 añade la letra g)** (jubilación forzosa del 99.1) · **103 reserva de plaza**: **>2 años**, sector público, reingreso en **1 mes** · **104 especial**: reserva de puesto y **computa trienios**; cargo público, **2 meses** para volver · **105 enfermedad**: **30 días** desde el alta · **106 cuidado**: **3 años y medio**, menores de **12 años** y familiares de **2.º grado**, con reserva; adopción internacional **10 semanas antes** · **107 incompatibilidades**: prohibidas las empresas proveedoras y **las de radiodifusión, producción, agencias y prensa**; **registro** en RRHH.
- **108-116**: Comisión de Acción Social **4 + 6**, técnica **2 + 3**, **2 reuniones/año**; **fondo 0,37 %** · accidentes **60.101,22 €** · vida **voluntario, cuota 60,10 €** · zonas de conflicto **120.000 €** · plan de pensiones **nivel fijo 0,90 %** · defensa jurídica: autorización en **30 días naturales**, **silencio positivo** · seguro de salud **0,71 %**, comisión **5 + 5** cada **6 meses**, **antigüedad >6 meses**.

## Disposiciones

- **DA 2.ª huelga**: bruto anual ÷ **365**; días sin descuento **140** (14 festivos + vacaciones + **102** descansos); resultado ÷ **225**.
- **DA 3.ª**: **1,75 % + 0,25 %** (disponibilidad tipos 2 y 3) + **0,30 %** al plan de pensiones.
- **DT 2.ª**: fin de semana **de dos días** para quienes lo hacían desde el **1/1/2011**, **máx. 12 h/día**.
- **DT 8.ª (2022)**: estabilización 2022 por la **Ley 20/2021**; DA 6.ª y 8.ª → **concurso de méritos**. (La de 2020: escrita eliminatoria, méritos solo con **≥50/100**, primas **≤31 pts** = **3/año + 5 + 5**.)
- **DT 10.ª (2022)**: prácticas anteriores al RDL 32/2021 siguen al **70 / 80**.
- **DF 1.ª**: jornadas **el mes siguiente**; jubilación forzosa **a los 6 meses**; art. 99.4 el **1/1/2020**.

## Anexos

**1** tablas salariales · **2** incompatibilidades · **3** clasificación —**los tres, solo imagen en el BOE**, transcritos en `fuentes/convenio/imagenes/`— · **4** Orquesta y Coro · **5** teletrabajo · **6** externalización · **7** (2021) **baremo de enfermedad/discapacidad/dependencia y agrupación familiar** del art. 14.3 · **8** (2022) ocupaciones análogas.

- **Anexo 7**: **enfermedad, discapacidad o dependencia hasta 12 pts**, escala **2·4·6·9·12**, por parentesco (solicitante o cónyuge · familiar de 1.º · familiar de 2.º, que **solo entra desde grado I o 33 %**) y grado. **Agrupación familiar hasta 8 pts**, escala **1·2·4·6·8**, cruzando situación (sin hijos · hijos de 12 a 18 · hijos hasta 12, también monoparental y divorcio · divorcio sin hijos) con distancia **<100 km · 100-250 km · >250 km**, tramo al que se equipara **insular/Ceuta/Melilla con familia en península y a la inversa**. Más cerca el parentesco y mayor el grado, más puntos; menores los hijos y mayor la distancia, más puntos.

- **Anexo 1 · tablas salariales** (las publicadas son las de **2020**; los PGE las suben, la estructura no cambia):
  - **Salario base: el importe depende solo del nivel, no del grupo.** De F1 a A3, **17 saltos**; **16 iguales** (~68,31 €) y **el de D2 a D1 más pequeño** (57,91 €).
  - Complementos de puesto en **cuatro tramos**: **A-B · C-D del Grupo I-I · C-D del resto · E-F**. Excepción: **unidades informativas paga igual en los tres primeros** y solo baja en E-F.
  - **Incremento de disponibilidad**: **opción 1 = 0 €**, opción 2 fija, opción 3 algo más del doble que la 2. **Igual en los cuatro tramos.**
  - **Residencia**: **resto de Canarias, Ceuta y Melilla > Las Palmas/Gran Canaria/Tenerife > Baleares**, que es el más bajo.
  - **Turnicidad: dos tablas, 35 h y 40 h semanales** — la letra b) del art. 50 en la práctica. **Fin de semana: dos columnas, 3 días y 2 días** (la de 2, por la DT 2.ª, se paga menos).
  - **Rodaje: el importe crece con el riesgo, no con la renta.** Menor a mayor: pernocta en domicilio · U.E. · renta alta · renta baja · **riesgo sanitario** · **conflicto bélico**.
  - **Guardias: cuatro importes**, no dos: localizable L-V, localizable S-D, y **día requerido** en cada franja. El **día S-D se paga a más del doble** que el L-V, aunque la **franja localizable de fin de semana cueste menos**.
  - **El anexo sí cifra el preaviso de los arts. 49 y 50**, que esos artículos mencionan sin importe.
  - **Orquesta y Coro emparejados**: concertino = ayudante de dirección · solista = jefe de cuerda = pianista del coro · tutti = profesor de coro = inspectores.
  - **Comidas**: la de **rodaje** es la más alta; después con factura, sin factura y desayuno.
- **Anexo 2 · incompatibilidades**: matriz **22 × 22**, tres símbolos —**X** incompatible a efectos económicos · **horas** incompatible por horas · **D** se acredita la diferencia—; **casilla vacía = compatible**.
  - **Residencia y vivienda son compatibles con todo**: las dos únicas filas vacías.
  - **La jornada de rodaje es la que más usa la D** (mando orgánico, responsabilidad, puesto de orquesta, disponibilidad, unidades informativas, nocturnidad).
  - **Gratif. diversa, formación, nocturnidad y horas extras se cruzan entre sí «por horas»**, nunca con X.
  - **Festivos ↔ horas extras solo son incompatibles en Orquesta y Coro**, «X (OyC)»: la **única casilla condicionada** del anexo.
  - Frente a **jornada de rodaje**: **puesto de orquesta → D**, **instrumentos musicales → X**.
- **Anexo 4** (30 arts., 5 caps.): **Grupo I-I, ámbito Orquesta y Coro**, exige **título superior de música**. Comisiones de régimen interno **4 miembros, cada 2 años, mínimo 3**; mesa = **más antiguo, mayor y menor**; empate **por sorteo**. Programación **2 veces/año**, información **15 días antes**. **Archivo bajo la Dirección del Fondo Documental.**
  - Jornada: **65,7 % de conjunto** · **≤6 sesiones semanales en 5 días** · **26 sesiones irregulares de 4 h**, **≤9 por trimestre**, **≤2 en fin de semana al mes**, festivos **+20 %**; contador a cero el **1 de enero**. Plan general **3 meses antes**; descanso semanal **2 días** (suspensión) / **5 días** (asignación).
  - Sesiones: **≤4 h**, **máx. 2 al día** (**≤3 h cada una**, salvo general + concierto) · **ensayo general ≤2 h 30**, sin nada antes ni entre medias · **concierto = 4 h** · **grabación ≤3 h** · parcial avisado **24 h**, no lo es **<30 min** · prueba acústica **45 min**, **1 h** con imagen y sonido.
  - Descansos: **15 min por hora**, entre periodos de **1 h a 1 h 15** · dos sesiones **≤12 h de extremo a extremo** · **12 h entre días** · **2 días consecutivos** de descanso semanal.
  - Giras: plan **2 semanas antes** · **≤4 h 30 de viaje** permite ensayo de 3 h o concierto; **si se pasa, no se actúa y no es descanso** · **>6 días → un día de descanso semanal** y cabe **jornada de rodaje**.
  - Licencias **7 días antes**, **5 veces al año**, servicio = **3/4 de cada cuerda con un solista** · excedencias **máx. 10 a la vez**, **plazas únicas sin límite** · faltas: **grave** faltar a más de un ensayo del mismo programa; **muy grave** faltar a **concierto, grabación o actuación con público** · vacaciones **en un solo turno** · vestuario **cada 3 años** · entradas **50 %, 4 por actuación, 2 abonos** · al aire libre **18-29 ºC**, interior **20-27 ºC**.
- **Anexo 5 teletrabajo**: **voluntario y reversible**, acuerdo individual de **1 año**, denuncia **1 mes antes**; reversibilidad **2 primeros meses** o al año, preaviso **15 días** · **1 a 4 días semanales**, reunión **semanal**, **al menos una jornada presencial** · **equipos de la empresa**, gastos del domicilio **a cargo de la persona** · **no altera salario base ni complementos personales**; los cambios pedidos por la persona **no se compensan**; **los turnos no varían**. Anterior a la **Ley 10/2021**.
- **Anexo 6**: diez categorías **a extinguir** (telefonistas, recepcionistas, conserjes, ordenanzas, auxiliares de régimen interno, antenistas, oficiales y ayudantes de oficios, conductores de unidades móviles, guardés, limpiador); **preferencia del personal fijo**.
