# Redacción · Oficial Técnico Electricista (27) · Tema 16 · Eficiencia energética y sostenibilidad en instalaciones

Fase 2. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/16-eficiencia-energetica-y-sostenibilidad-en-instalaciones.md`
(14.293 palabras según `indice.py`, contando tablas; 35 epígrafes). Material: `27-investigacion-C-clima-gestion.md`
§0, §10.2, §10.4, §10.5, §12.1, §9.1 y §16. Reuso RTVE según `informes/canal-sur-reuso/tecnica.tsv` (fila 27/16):
`temas/ing-tec-industrial/12-eficiencia-energetica.md`, 25 %, actualizar: **sí**. Fecha declarada de lectura de
todas las fuentes: 05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»; ninguna fuente citada
cambió entre las dos fechas: la última reforma aplicada, el RD 659/2025, rige desde el 23-07-2026).

Lentes corridas: `indice.py` (índice generado), `refutar_prosa.py` (0 hallazgos tras presentar ATECYR, AMICYF,
UNE y MW), `negritas.py` contra las 14 fuentes de la trazabilidad (257 negritas; ver aviso 9).

Ficheros tocados: el tema (nuevo), este informe y una fuente nueva:
`fuentes/canal-sur/documentos/reglamento-ue-2019-2020-consolidado-2021-09-01.txt` (texto de la versión
consolidada 02019R2020-20210901 bajada de publications.europa.eu el 05-10-2026 y pasada a texto). Volcados
temporales en el scratchpad (RD 110/2015, Ley 7/2022, RD 214/2025), no en el repositorio.

## Estructura

1 Marco (1.1 qué norma obliga a quién; 1.2 huella de carbono, RD 214/2025); 2 Ahorro energético (2.1 certificación:
finalidad, ámbito, exclusiones; 2.2 artículo 6, seis elementos del 8.1, validez, etiqueta, reforma de
2025; 2.3 auditorías RD 56/2016 y Directiva 2023/1791; 2.4 aplicación a la casa con salvedades); 3 Monitorización
(3.1 IT 1.2.4.4; 3.2 IT 3.4.4.2, 3.4.5, 3.8.3; 3.3 IT 1.2.4.3.5 y exención IT 4.3.4; 3.4 medida eléctrica y CPD,
art. 12 Directiva); 4 Mantenimiento orientado a eficiencia (4.1 IT 3.2 y tabla 3.3 con ejemplo de EER; 4.2 IT
3.4.4.1 e inspección IT 4.2.2/4.3; 4.3 IT 3.6.2 y 3.7; 4.4 oficio y guía IDAE); 5 LED (5.1 definiciones del Reg.
2019/2020; 5.2 Ponmax con ejemplo, requisitos funcionales, exenciones de plató y emergencia; 5.3 embalaje;
5.4 sustitución por LED); 6 Climatización eficiente (6.1 IT 3.8; 6.2 IT 1.2.4.5; 6.3 IF-17 2.3, IF-14 y Reg.
2024/573 art. 13); 7 Residuos (7.1 Ley 7/2022; 7.2 RAEE; 7.3 refrigerantes y aceites; 7.4 caso resuelto);
normativa; lo que no da; trazabilidad.

## Fuentes leídas por el redactor (05-10-2026)

- RD 390/2021 (`BOE-A-2021-9176`, `boe.py precepto`): arts. 1, 3, 4 bis, 4 ter, 4 quáter (rúbrica y ap. 1), 6, 7 bis,
  8, 13 y 16, con la cadena de redacciones (3, 6, 4 bis-quáter y 7 bis: vigentes desde 23-07-2026).
- RD 56/2016 (`BOE-A-2016-1460`): arts. 2 a 5.
- RD 214/2025 (`BOE-A-2025-7439`): arts. 1, 2, 3, 11, 12, dd, dt y df 4.ª. RD 163/2014: metadatos y análisis de la
  API de datos abiertos del BOE (`estatus_derogacion: S`, `fecha_derogacion: 20250612`; «SE DEROGA, con efectos
  desde el 12 de junio de 2025, por Real Decreto 214/2025»).
- Ley 39/2015, art. 2. RD 1890/2008, art. 2 (volcado `fuentes/canal-sur/BOE-A-2008-18634.md`).
- RITE (`fuentes/canal-sur/BOE-A-2007-15820.md`, grep): IT 1.2.4.3.5.1, IT 1.2.4.4 ap. 1-8, IT 1.2.4.5.1-1.2.4.5.4,
  IT 3.2, IT 3.4 (3.4.1 primer párrafo, 3.4.2 con tabla 3.3, 3.4.3, 3.4.4, 3.4.5), IT 3.6, IT 3.7, IT 3.8.1-3.8.3,
  IT 4.2.2 ap. 1-3.a, IT 4.3.2-4.3.4. Redacción de IT 1, 3 y 4: vigente desde 01-07-2021 (`.redacciones.tsv`).
- RSIF (`fuentes/canal-sur/BOE-A-2019-15228.md`): arts. 12.1.a).4.º (vig. 04-09-2025), 13, 25; IF-14 1.2.1 y 1.2.4.2
  (vig. 10-05-2025); IF-17 1.1 y 2.3.
- Reglamento (UE) 2024/573 (`fuentes/canal-sur/documentos/reglamento-ue-2024-573.txt`): arts. 4.1, 8.1-8.2, 13.3, 13.4.
- Directiva (UE) 2023/1791 (`fuentes/canal-sur/documentos/directiva-ue-2023-1791.txt`): arts. 2 («organismos
  públicos»), 5.1, 6.1, 11.1-11.2, 12.1-12.5, 36, 38, 40.
- Buscador del BOE por título (`boe_buscar.py`): «2023/1791», «auditorías energéticas», «eficiencia energética»,
  «centros de datos» (2023-2026): ninguna norma de transposición; confirma el hueco de la investigación.
- Reglamento (UE) 2019/2020, consolidado 01-09-2021 (nuevo, ver arriba): arts. 1-9; anexo I def. 15, 50, 51, 57 y
  60; anexo II puntos 1.a (cuadros 1 y 2), 2 (cuadro 4), 3.a, 3.b; anexo III puntos 1, 2 y 3 (letra w). La ficha
  del acto (notice XML) lista consolidaciones hasta 20210901 y sólo el modificador 32021R0341.
- Ley 7/2022 (`BOE-A-2022-5809`): arts. 8, 20, 21 y disposición derogatoria primera.
- RD 110/2015 (`BOE-A-2015-1762`): arts. 3, 16, 18, 26, 44 (sólo para no afirmar nada de financiación) y anexos III,
  VII (A y B.1) y VIII (grupos de tratamiento 31* y 32 y sus códigos LER-RAEE).
- Guía técnica de mantenimiento de instalaciones térmicas (IDAE, 2007) (`idae-guia-mantenimiento-termicas.txt`):
  apartado 2.6 (fines del PMP) y lista de verificaciones anuales (líneas 470-485 y 5930-5941).

## Avisos para el verificador

1. **RTVE desactualizado en un punto entero: el RD 163/2014 está derogado** desde el 12-06-2025 por el RD 214/2025,
   que además crea la obligación de calcular la huella (art. 11). El epígrafe 5 de RTVE («es voluntario», «no
   obliga a nadie», «el propio real decreto lo dice tres veces») **no se ha copiado**; 1.2 se redacta de nuevo sobre
   el RD 214/2025. **Ojo con `boe.py`**: para `BOE-A-2014-3379` responde «vigente hoy» y una sola redacción; la
   derogación sólo aparece en los metadatos de la API (`estatus_derogacion`). Vale la pena avisar al coordinador:
   la herramienta no detecta normas derogadas enteras.
2. **Errores de RTVE corregidos al adaptar** (cotejados con el BOE vigente): «Los tres elementos de la
   certificación» → seis (art. 8.1; error 3, ya señalado por la investigación); «el artículo 7 bis no estaba en
   vigor… este tema no afirma nada» → en vigor desde 23-07-2026, se da su contenido; las letras c) y e) del 3.1 de
   RTVE simplificaban «pertenecientes u ocupados por una Administración Pública» (Ley 39/2015, art. 2.3): se cita
   literal. La tabla de RTVE «Sí, por dos vías» para una corporación pública no se traslada: para RTVA/CSRTV no está
   comprobado que sean Administración Pública ni gran empresa (2.4 y «Lo que no da»).
3. **Lo propio de RTVE quitado**: referencias a «tema 1/3/7» de su temario, «este proyecto», «fecha de corte», el
   epígrafe 6 entero (sus dos «observaciones de oficio» se reformulan: el plató en 2.1 como lectura de oficio; la
   flota en 2.3), la portada y la trazabilidad de RTVE.
4. **Formato**: RTVE pone en negrita casi toda su prosa propia. En Canal Sur negrita = literal; al copiar se ha
   quitado la negrita a lo que no es literal y se han sustituido los resúmenes en negrita por el literal del BOE
   entre comillas. Por eso **nada de lo tomado de RTVE es «sin cambios»** (ver abajo) y todo se verifica.
5. RD 56/2016 art. 3.2 sigue citando el RD 235/2013 (derogado): se dice en 2.3 sin corregir el texto.
6. RSIF (art. 13.3, IF-14) y RD 110/2015 (art. 18.1) remiten a la Ley 22/2011, derogada por la dd 1.ª de la Ley
   7/2022 (comprobado en el BOE, cierra el «no comprobado» de la investigación §16.4). Dicho en 7.1.
7. Reglamento 2019/2020: la fórmula de X_LMF,MIN viene en imagen en la versión consolidada y no se reproduce. Que el
   LED cae en la fila «Otras fuentes luminosas del ámbito no mencionadas anteriormente» del cuadro 1 es lectura del
   cuadro (no lo nombra), y así se dice. Exenciones citadas: anexo III punto 1.b (emergencia) y punto 3.w (platós,
   añadida por el 2021/341, marcada ▼M1).
8. Cifras de oficio, declaradas como tales: conversión TJ → kWh (1 kWh = 3,6 MJ; 10 TJ ≈ 2,78 GWh; 85 TJ ≈ 23,6 GWh),
   definición del EER, ejemplo de enfriadora (datos supuestos) y ejemplo de Ponmax (1,08 × 31,5 = 34,02 W).
   Los 19/27 ºC del RDL 14/2022 y su fin el 01-11-2023 se toman de la investigación (§0), no releídos por el redactor.
9. `negritas.py`: 9 «NO ESTÁ». Dos rótulos de forma («Enunciado del programa», «Qué se puede preguntar»), como en
   T06 y T15; dos títulos oficiales de norma (RD 214/2025 y Ley 7/2022) que están en los metadatos del BOE y no en
   el cuerpo del volcado; dos citas con elisión («1.º Administrativo… 11.º» del art. 3.1.e y «a) Administrativo.
   b) Comercial… c) Pública concurrencia» de la IT 3.8.1.2), cuyos tramos sí están; y tres rótulos propios en negrita
   que se han pasado a cursiva (ya corregido). Las 13 «atribuidas a otro artículo» son falsos positivos: la negrita
   está en el artículo correcto (11 del RD 214/2025, 3 y 16 del RD 390/2021) y el script toma como atribución un
   número cercano de la misma fila (art. 262.5 LSC, art. 2.3 Ley 39/2015, art. 15 RITE, art. 3.1.c).

## Copiado del común

Nada. El tema no desarrolla ninguna norma del temario común de Canal Sur, y ningún epígrafe se ha copiado de un tema
ya cerrado de Canal Sur (tampoco de los temas 6, 9 y 10 de este puesto, que aún no han cerrado el ciclo; se remite
a ellos en «Lo que este tema no da»).

## Copiado de RTVE sin cambios

Nada. La fila 27/16 de `tecnica.tsv` marca el tema de RTVE como «actualizar: sí», y todo lo que se podía tomar de él
cita normas (RD 390/2021, RD 1890/2008, RD 56/2016, RD 163/2014): no es pasaje técnico sin norma de un tema sin
actualizar. Además el RD 390/2021 ha cambiado después de la fecha de RTVE y el RD 163/2014 está derogado.

## Adaptado de RTVE (se verifica entero)

- 1.1: la tabla «a quién obliga cada norma» y la frase del error de estudio, ampliadas a nueve normas.
- 2.1: tablas del ámbito (3.1), de los tres supuestos de reforma (3.1.d), agrupación de los once usos, exclusiones
  (3.2) y la lectura de la letra c), con el literal del BOE vigente en lugar del resumen.
- 2.2: tabla del artículo 6, «un certificado no legaliza nada», «sin registro no vale», copia del certificado (6.8).
- 2.3: auditorías (arts. 2-5 del RD 56/2016): cifras 250/50/43, tabla del 3.1, alternativas del 3.2, directrices del
  3.3 con la lectura de la letra c), arts. 4 y 5.
- 5.4: la idea del «o luminarias» de la modificación de importancia del RD 1890/2008 (art. 2.3.c), con el literal.

## Diez preguntas tipo test (comprobación de cobertura antes de entregar)

Contestadas sólo con el tema. Todas **enteras**. La 10 obligó a ampliar 7.2: el tema no decía con fuente que
el tubo fluorescente es residuo peligroso; se añadió el párrafo de los grupos 31* y 32 del anexo VIII y el anexo VII.A
del RD 110/2015.

1. (Ahorro · certificación) La validez máxima de un certificado de eficiencia energética con calificación G es de:
   a) diez años; b) cuatro años; **c) cinco años**; d) quince años. — 2.2, art. 13.1. **Entera.**
2. (Ahorro · certificación) Según el art. 8.1 del RD 390/2021, la certificación de eficiencia energética se compone
   de: a) tres elementos; b) cuatro; c) cinco; **d) seis**. — 2.2. **Entera.**
3. (Ahorro · auditorías) Una gran empresa del RD 56/2016 debe auditarse: a) cada dos años, el 100 % del consumo;
   **b) cada cuatro años, al menos el 85 % del consumo de energía final**; c) cada cinco años, el 85 %; d) cada cuatro
   años, el 50 %. — 2.3. **Entera.**
4. (Sostenibilidad) El registro de huella de carbono y la obligación de calcularla se regulan hoy en: a) el RD
   163/2014, voluntario; **b) el RD 214/2025, que derogó el RD 163/2014**; c) la Ley 7/2022; d) el RD 56/2016. —
   1.2. **Entera.**
5. (Monitorización) El RITE obliga a registrar las horas de funcionamiento de bombas y ventiladores cuya potencia
   eléctrica del motor sea mayor que: a) 5 kW; b) 10 kW; **c) 20 kW**; d) 70 kW. — 3.1, IT 1.2.4.4.6. **Entera.**
6. (Monitorización) Un edificio no residencial con más de 290 kW de calefacción o refrigeración deberá estar
   equipado, cuando sea técnica y económicamente viable, con: a) contador horario por planta; **b) un sistema de
   automatización y control de edificios**; c) un analizador de redes portátil; d) un visualizador DIN A3. — 3.3.
   **Entera.**
7. (Mantenimiento orientado a eficiencia · práctica) En la lectura trimestral de una enfriadora de 400 kW se miden
   300 kW de potencia frigorífica y 120 kW de potencia eléctrica absorbida. Su EER instantáneo y su situación ante la
   inspección son: **a) 2,5, por encima del mínimo de 2 exigido en inspección**; b) 0,4, por debajo; c) 2,5, por
   debajo del mínimo de 3; d) 420, no aplicable. — 4.1 y 4.2 (EER = frío/eléctrica; IT 4.2.2.3.a). **Entera.**
8. (Tecnología LED · práctica) Una lámpara LED no direccional de red declara 3.600 lm y CRI 80. Con el Reglamento
   (UE) 2019/2020, su potencia máxima permitida es aproximadamente: a) 30 W; **b) 34 W**; c) 36 W; d) 45 W. — 5.2,
   ejemplo resuelto. **Entera.** (Y, de paso, L70B50 = 50 % de la población por debajo del 70 % del flujo inicial:
   5.1.)
9. (Climatización eficiente) En un recinto administrativo refrigerado con energía convencional, la temperatura del
   aire: a) no será superior a 26 ºC; **b) no será inferior a 26 ºC, con humedad relativa entre el 30 % y el 70 %**;
   c) no será inferior a 27 ºC; d) no será inferior a 24 ºC. — 6.1, IT 3.8.2.1. **Entera.** (La salvedad de las
   salas técnicas, IT 3.8.2.3, también está.)
10. (Gestión de residuos) Los tubos fluorescentes retirados en una reforma, residuo peligroso por su mercurio, pueden
    almacenarse en el lugar de producción como máximo: a) dos años; b) un año; **c) seis meses, ampliables por la
    comunidad autónoma otros seis como máximo**; d) tres meses. Y van en la categoría: 3.1 del anexo III del RD
    110/2015. — 7.1 (art. 21 Ley 7/2022), 7.2 (fluorescente = grupo 31*, fuera de la lista de fracciones no
    peligrosas del anexo VII.A; añadido al comprobar esta pregunta) y 7.4. **Entera** tras la ampliación.

Reparto: certificación 2, auditorías 1, sostenibilidad 1, monitorización 2, mantenimiento 1, LED 1, climatización 1,
residuos 1; aplicación práctica en 7, 8 y 10.
