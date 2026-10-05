# Verificación · Oficial Técnico Electricista (27) · Tema 16 · Eficiencia energética y sostenibilidad en instalaciones

Fase 3. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/16-eficiencia-energetica-y-sostenibilidad-en-instalaciones.md`
(14.650 palabras tras la verificación, según `indice.py`; 35 epígrafes). Fecha de lectura de todas las fuentes: 05-10-2026
(reloj del sistema; el encargo dice «hoy es 24-09-2026»; ninguna fuente cambió entre las dos fechas: la última reforma
aplicada, RD 659/2025, rige desde 23-07-2026; RSIF art. 12, desde 04-09-2025).

Ficheros tocados: el tema y este informe. Volcados temporales en el scratchpad (RD 214/2025, Ley 7/2022, RD 110/2015,
RDL 14/2022, Ley 39/2015 art. 2), no en el repositorio.

## Copiado del común / de RTVE sin cambios

El informe de redacción declara **nada** en las dos listas (lo de RTVE es todo adaptado o cita normas). No había nada
que comprobar con `diff`; se ha verificado el tema entero.

## Fuentes releídas (05-10-2026)

- RD 390/2021 (`BOE-A-2021-9176`, volcado local + `.redacciones.tsv`): arts. 1.2, 3 (vig. 23-07-2026, con la nota de la
  redacción anterior), 4 bis, 4 ter, 4 quáter, 6 (vig. 23-07-2026), 7 bis, 8, 13, 15, 16. RD 659/2025: título, BOE
  núm. 176 de 23-07-2025 (sumario XML).
- RD 56/2016 (`BOE-A-2016-1460`): arts. 2-5 (art. 5 en redacción de 03-06-2021). `boe_buscar.py` «2023/1791» y «Real
  Decreto 56/2016» (2023-2026): sin resultados; «auditorías energéticas»: sólo anuncios de contratos. Confirma el hueco.
- Directiva 2023/1791 (txt DOUE): arts. 2.12, 5.1, 5.2, 6.1, 11.1-11.2, 12.1, 12.4, 36.1, 38, 40.
- RD 214/2025 (`BOE-A-2025-7439`, volcado nuevo): arts. 1.2, 1.3 a) y k), 2, 11 (1-6), 12, dd única, df 4.ª; metadatos
  API (título, BOE núm. 89, 12-04-2025, `fecha_vigencia` 12-06-2025). RD 163/2014: metadatos (`estatus_derogacion: S`,
  `fecha_derogacion: 20250612`) y texto original (participación «de carácter voluntario»).
- Ley 39/2015, art. 2 (`boe.py precepto`). RD 486/1997, anexo IV (volcado local).
- RITE (`BOE-A-2007-15820`): IT 1.2.4.3.5, 1.2.4.4, 1.2.4.5.1-1.2.4.5.4, IT 3.2, 3.4.1-3.4.5 (tablas 3.2 y 3.3), 3.6, 3.7,
  3.8.1-3.8.5, IT 4.2.1-4.2.3, 4.3.1-4.3.4. `boe.py precepto it3-2` avisa «posible reforma cruzada»: es el RDL 14/2022
  (vigencia sin fecha); la redacción aplicable sigue siendo la de 01-07-2021 (RD 178/2021, BOE núm. 71).
- RDL 14/2022 (`BOE-A-2022-12925`, volcado nuevo): art. 29.uno (19/27 ºC) y df 17.ª.2.a (vigencia hasta 01-11-2023).
  El aviso 8 del redactor («no releído») queda cerrado: el dato es correcto.
- Reglamento (UE) 2019/2020 consolidado 01-09-2021: art. 1, art. 2 (puntos 1, 2, 3, 6, 17), anexo I def. 51, 57, 60,
  anexo II 1.a (cuadros 1 y 2), 2 (cuadro 4), 3.a, 3.b.1, anexo III 1.b y 3.w. Ficha del acto
  (publications.europa.eu, notice tree): consolidaciones 20191205, 20210301, 20210701, 20210901; único modificador
  32021R0341. No hay versión posterior.
- RD 1890/2008, art. 2 y rúbricas de arts. 4, 5, 7, 8. RSIF: arts. 12.1.a).4.º, 13.3, 25; IF-14 1.2.1, 1.2.4.2; IF-17 1.1,
  2.3. Reglamento (UE) 2024/573: arts. 4.1, 8.1, 13.3-13.5. Ley 7/2022: arts. 8.1, 20, 21, dd 1.ª; título. RD 110/2015:
  arts. 3.l, 18.1, 26; anexos III, VII, VIII. Guía IDAE 2007: §2.6 y verificaciones anuales.
- Números y fechas de BOE de la «Normativa» cotejados en la API o el sumario XML del BOE (todas correctas).

## Lentes

`negritas.py` contra 15 fuentes: 261 negritas, 6 «NO ESTÁ» (los rótulos y elisiones ya explicados en el aviso 9 del
redactor) y 14 «atribuidas a otro artículo», todas falsos positivos (art. 262.5 LSC, art. 2.3 Ley 39/2015, art. 15
RITE, art. 3.1.c como número cercano). Las negritas nuevas de esta fase están todas en su fuente.
`refutar_exactitud.py`: 39 «no literales», todos falsos positivos (citas de reglamentos UE, IT del RITE o IF del RSIF
que el script ancla en un «artículo» de las normas BOE dadas). `refutar_modo.py`: 0. `refutar_prosa.py`: 0.
`indice.py`: índice regenerado.

## Hallazgos y correcciones (error del catálogo)

1. **1.1 y 1.2 (9).** «Empresas obligadas a informar de sostenibilidad» no es lo que dice el art. 11.1 RD 214/2025
   («obligadas a incluir información de carácter no financiero por el artículo 49.5 del Código de Comercio»).
   Corregido en la tabla y en la salvedad; «sector público estatal» → «sector público administrativo estatal».
2. **1.2 (6).** Faltaba el art. 11.6: las obligaciones de las empresas entran en vigor según el calendario de la Ley
   11/2018. Añadida fila literal.
3. **2.1 (6 y 8).** La declaración responsable es el párrafo segundo de la **letra e)** del 3.2 (no «del 3.2»), y se
   omitía su segunda frase («No obstante… podrá regular un procedimiento más exigente»). Corregido y añadido; también
   en la tabla del RD 659/2025 («Artículo 3.2.e), párrafo segundo»).
4. **2.3 (4 y 6).** La Directiva no «fija obligaciones para los organismos públicos»: obliga a los Estados a velar por
   que el consumo de **todos los organismos públicos en su conjunto** baje un 1,9 % anual (art. 5.1), y ese objetivo
   **«será indicativo»** hasta el 11-10-2027 (art. 5.2, salvedad omitida); el 3 % de renovación también es obligación del
   Estado (art. 6.1). Reescrito.
5. **2.4, alumbrado exterior (9).** «Sí, en aparcamientos, viales interiores y perímetros de más de 1 kW»: los ejemplos
   no salen del art. 2 RD 1890/2008. Queda: instalaciones de alumbrado exterior de más de 1 kW (art. 2.1).
6. **2.4, RITE (3/9).** «Sí, en toda instalación de más de 70 kW» mezclaba umbrales: el programa de gestión energética
   es de toda instalación (IT 3.2.b; la tabla 3.2 empieza en 20 kW); el seguimiento (IT 3.4.4.2) y la inspección
   (IT 4.2.1/4.2.2), por encima de 70 kW. Corregido.
7. **3.2 (6).** IT 3.8.3: añadida la salvedad del uso cultural (un único dispositivo en el vestíbulo).
8. **3.4 (9).** El art. 6.7 RD 390/2021 no recoge consumos medidos: obliga a que las bases de datos **permitan** su
   recopilación. Reformulado («deben permitir la recopilación de…»).
9. **5.4 (9).** «Niveles máximos» del RD 1890/2008 no confirmado en lo leído (art. 7 es «Niveles de iluminación»):
   → «niveles de iluminación».
10. **6.2 (6).** IT 1.2.4.5.1.5: añadida la posibilidad de justificar el incumplimiento «por la dificultad de lograrlo».
11. **6.3 (6).** Art. 13.3 Reg. 2024/573: faltaba la salvedad de gases regenerados o reciclados **«Hasta el 1 de enero
    de 2030»** (sí estaba la del 13.4, hasta 2032). Añadida.
12. **7.2 (9).** «La fluorescente… se gestiona como residuo peligroso» se presentaba como consecuencia del anexo VII.A,
    que sólo declara no peligrosas ciertas fracciones. Ahora se apoya en el asterisco que el anexo VIII pone a los
    grupos con componentes peligrosos (41\*, 51\*, 61\*, 31\*), dicho como lectura del anexo.
13. **Normativa y Trazabilidad (9).** Se citaban el RDL 14/2022 (6.1), el RD 486/1997 (anexos III y IV, 5.4 y 6.1) y la
    Ley 39/2015 (2.4) sin fila. Añadidas, con BOE, fecha y redacción comprobados. Portada: extensión 14.650 palabras.

Comprobado y correcto (sin cambio): todas las cifras y literales de RD 390/2021 (seis elementos del 8.1, 10/5 años,
250/500 m², 25 %, 10 % y 50 m², exclusiones, art. 6, 7 bis), RD 56/2016 (250/50/43, cuatro años, 85 %, nueve meses,
directrices a-d, apartado 5, arts. 4 y 5), Directiva (85/10 TJ, 11-10-2027, 11-10-2026, 500 kW, 1 MW, arts. 36, 38,
40), RD 214/2025 (todas las citas; deroga el RD 163/2014 por su dd única), RITE (IT 1.2.4.4 ap. 2-8, 290 kW y letras
a-c, UNE-EN 15232-1, tabla 3.3 y leyenda, EER ≥ 2, 4 y 15 años, 21/26 ºC y 30-70 %, 1.000 m², DIN A3, ± 0,5 ºC,
0,28 m³/s), Reg. 2019/2020 (fórmula, η 120,0, L 1,5/2,0, F, C 1,08, R, FL T8 89,7→120,0, 0,5 W, cuadro 4, w),
ejemplos numéricos (34,02 W; 105,8 lm/W; EER 2,5 y 2,14; 10 TJ ≈ 2,78 GWh, 85 TJ ≈ 23,6 GWh), RSIF, Reg. 2024/573,
Ley 7/2022 (jerarquía, art. 20, art. 21: dos años/un año/seis + seis meses), RD 110/2015 (categorías, grupos 31\*/32,
códigos LER-RAEE, anexo VII, arts. 3.l y 26), RDL 14/2022, guía IDAE.

Errores del catálogo: 1 cita cruzada (0), 2 ley por reglamento (0), 3 recuentos (0; ver 6), 4 «podrá»/«deberá» (1:
hallazgo 4), 5 siglas (0), 6 salvedad omitida (6: hallazgos 2, 3, 4, 7, 10, 11), 7 derogada como vigente (0), 8
artículo mal (1: hallazgo 3), 9 sin fuente (6: hallazgos 1, 5, 6, 8, 9, 12, más 13).

## Para el coordinador

- `boe.py` no marca derogaciones totales (aviso del redactor, confirmado con RD 163/2014) y señala como «reforma cruzada»
  el RDL 14/2022 sobre la IT 3 del RITE, que es una medida temporal ya agotada: la redacción aplicable es la de 2021.
- Queda abierto, como dice «Lo que este tema no da»: naturaleza de la RTVA/CSRTV a efectos de los arts. 3.1.c RD
  390/2021, 2 RD 56/2016, 11.1 RD 214/2025 y 2.12 de la Directiva.
