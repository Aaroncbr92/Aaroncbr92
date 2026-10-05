# Puesto 27 · Oficial Técnico Electricista · Tema 1 · Fase 2, redacción

Fecha de trabajo: 05-10-2026 (el encargo fija «hoy» en 24-09-2026; ningún precepto citado cambió
entre ambas fechas: el BOE consolidado del REBT da como última actualización el 18-12-2025 y los
preceptos citados tienen fechas de vigencia de 2003, 2021 y 2022). Tema escrito:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/01-instalaciones-electricas-de-baja-tension-magnitudes-potencia-y-cargas.md`
(9.867 palabras según `indice.py`; 8 rúbricas en el orden del enunciado —la primera es el rótulo
«Instalaciones eléctricas de baja tensión» que encabeza el enunciado—, 25 epígrafes `###`).

Ficheros tocados: sólo el tema y este informe.

Material: `27-investigacion-A-electrico.md` § 1, § 2 y § 9-10; RTVE `teitse/01` § 1-4 y
`teitse/05` § 2, 3 y 5 (fila 27·1 de `informes/canal-sur-reuso/tecnica.tsv`: 90 %, actualizar: no).

Lentes pasadas al cerrar: `negritas.py` contra `fuentes/canal-sur/BOE-A-2002-18099.md` (43 negritas;
2 «no están», ambas rótulos de la plantilla; 0 «otro artículo»); `refutar_prosa.py`: 0 hallazgos
(había 6, todos mayúsculas enfáticas de RTVE y la sigla MJ: corregidos).

## Fuentes releídas en esta fase

| Fuente | Fecha de lectura | Qué se comprobó |
|---|---|---|
| RD 842/2002 (BOE-A-2002-18099), volcado consolidado `fuentes/canal-sur/BOE-A-2002-18099.md` | 05-10-2026 | Art. 2.1 (vig. 01-07-2021, BOE-A-2021-6879); art. 4.1, 4.2, 4.4, 4.5; art. 16.1 y 16.2 (redacción única) |
| Mismo volcado, ITC-BT-19 | 05-10-2026 | 2.2.1; 2.2.2 entero (cuatro párrafos); 2.2.4; 2.5. Redacción única |
| Mismo volcado, ITC-BT-09, 14, 15 | 05-10-2026 | ITC-BT-09 apartados 3 y 8 (0,90 y 3 %); ITC-BT-14 (0,5 y 1 %; neutro ≈ 50 %); ITC-BT-15 (0,5 / 1 / 1,5 %). Redacción única |
| Mismo volcado, ITC-BT-43, 44, 47, 52 | 05-10-2026 | ITC-BT-43 2.6 y 2.7; ITC-BT-44 3.1 y 3.2; ITC-BT-47 3.1 y 3.2 (125 %); ITC-BT-52 3.1 (vig. 16-06-2022, BOE-A-2022-9848) |

## Correcciones y decisiones (manda la fuente)

1. **ITC-BT-19 2.2.2.** RTVE cortaba el primer párrafo tras «funcionar simultáneamente» y luego
   explicaba la compensación con la derivación individual sin citarla. El tema cita el párrafo
   entero, con la frase de la compensación.
2. **Penalización en factura** (RTVE teitse/01 § 2, fila de la tabla de cos φ, y «el error de
   facturación más caro del oficio»): sin fuente leída (investigación § 2.3 y § 9.5). Quitada; la
   fila se sustituye por la merma de potencia activa de transformadores, grupos y SAI, y la laguna
   se declara en «Lo que este tema no da».
3. **ITC-BT-09.** La investigación daba sólo la frase del apartado 3; se añade la del apartado 8
   («Cada punto de luz deberá tener compensado individualmente…»), leída en el BOE.
4. **ITC-BT-43 2.6, tercer párrafo** («negar el suministro…»): se refiere a los receptores de
   fuertes oscilaciones del párrafo anterior, no claramente a los que desequilibran. Escrito en un
   borrador y quitado para no atribuirlo mal.
5. **Añadido sobre la investigación:** ITC-BT-14 (neutro ≈ 50 % de la fase y caídas de 0,5 y 1 %),
   ITC-BT-15 (0,5, 1 y 1,5 %), ITC-BT-19 2.2.1 y 2.2.4, ITC-BT-44 3.1 primer párrafo, ITC-BT-47 3.1
   y 3.2, art. 2.1, 4.1, 4.5 y 16.1. Todos leídos en el volcado.
6. **Conductividad.** RTVE no daba valor y el REBT tampoco. Los ejemplos de 7.4 usan γ = 48 como
   dato supuesto del ejercicio, declarado así en el tema y en «Lo que este tema no da». El
   verificador debe comprobar que no se presenta como valor de norma.
7. **Investigación § 2.2, ITC-BT-44, «leer la frase entera»:** leída; está en el apartado 3.2 y se
   cita entera.
8. **Erratas del BOE conservadas** en las citas, con nota: «deforma» (art. 16.2), «energí a»
   (ITC-BT-43 2.6), «debidas cargas» (ITC-BT-19 2.2.2).

## Qué se quitó por propio de RTVE o sin fuente

- Referencias al anexo y a la convocatoria 1/2022 de RTVE, a «este proyecto», a los puntos 2, 5,
  6, 9, 14 y 15 del anexo RTVE y al reparto de transformadores y motores con su tema 2.
- teitse/01 § 5 (medida de tensión y corriente) y § 6 (transformadores y motores): el enunciado de
  Canal Sur no los pide; la medida va al tema 14. Del § 6 sólo queda, adaptada, la inducción como
  razón de que la continua no se transforme (epígrafe 3.1).
- teitse/01 § 3: «rendimiento altísimo» y «Ésa es la única razón por la que existe una red de alta
  tensión», afirmaciones sin fuente.
- teitse/05 § 1 (criterio de calentamiento, IB ≤ In ≤ Iz) y § 4 (procedimiento de ocho pasos): son
  del tema 4 y la condición no está en el REBT (investigación § 9.2). Queda sólo la regla de los dos
  criterios, remitida al tema 4.
- teitse/05 § 5, fila de armónicos «salvo justificación por cálculo» se sustituye por la cita
  literal de la ITC-BT-19; «el neutro no lleva protección en muchos esquemas», sin fuente, quitado.

## Copiado del común

Ninguno. El temario común de Canal Sur (`temas/canal-sur-comun/01` a `10`) no trata ninguna
materia de este tema.

## Copiado de RTVE sin cambios

Pasajes técnicos copiados palabra por palabra de temas RTVE marcados «actualizar: no» y que no citan
norma. El único cambio es tipográfico, de la plantilla de Canal Sur: fuera las negritas (en Canal
Sur la negrita marca sólo texto literal de la fuente) y las mayúsculas enfáticas pasadas a
minúscula. El verificador comprueba sólo que son literales.

De `teitse/01-fundamentos-de-electricidad-y-medida.md`:

- § 1, tabla de las tres magnitudes («Tensión, diferencia de potencial o voltaje… Ohmio, Ω») → tema 2.1.
- § 1, «La ley de Ohm relaciona las tres… cualquiera de ellas:», su tabla de tres formas y el
  párrafo «Y la lectura de oficio… acaba en ella.» → tema 2.2.
- § 1, «La resistencia de un conductor, que es la fórmula que este oficio usa todos los días:», la
  fórmula, su tabla de símbolos, las tres consecuencias numeradas y el párrafo «Y la que no se lee…
  y de la temperatura ambiente.» → tema 2.3.
- § 3, «La diferencia de fondo… periódicamente.» y la tabla continua/alterna → tema 3.1.
- § 3, tabla de magnitudes de la señal alterna y el párrafo «El valor EFICAZ… no por el eficaz.» →
  tema 3.2.
- § 3, «En una red trifásica de cuatro conductores… El reglamento da las dos cifras y no las
  relaciona.» → tema 1.2.
- § 4, «Tres tensiones alternas… todo lo demás.», «Por qué se usa…» con sus razones 1 y 2, la
  tabla estrella/triángulo, «La regla que las resume… en la CORRIENTE.» y el párrafo «El NEUTRO y
  por qué existe… carga el neutro.» → tema 3.4.
- § 2, «La potencia en corriente continua es un producto: P = U · I, en vatios.» y la tabla de las
  tres potencias → tema 4.1.
- § 2, «La potencia es lo que se contrata; la energía es lo que se gasta.» → tema 5.
- § 2, «un cos φ bajo significa que por el cable circula más corriente de la que hace falta para el
  trabajo que se hace.» y las tres primeras filas de la tabla de consecuencias → tema 6.1.

De `teitse/05-calculo-de-lineas-longitudes-y-secciones.md`:

- § 2, tabla «Consecuencia de una caída excesiva» → tema 7.1.
- § 3, «Las dos fórmulas del oficio…», sus dos tablas (fórmulas y símbolos), la tabla «Despejando
  la sección» y las cuatro lecturas numeradas → tema 7.3.
- § 5, «En un sistema trifásico equilibrado con cargas LINEALES… se SUMAN en el neutro.» → tema 8.3.

**Adaptado de RTVE, para verificar** (cambia alguna palabra o cita norma): tema 2.3 («fundamento
del cálculo de caída de tensión del epígrafe 7», antes «del punto 5 del anexo»); 3.1 (razón técnica
de la red alterna, sin «única razón» ni «rendimiento altísimo»); 3.4 (razón 3 acortada; «del
oficio» por «de la ocupación»; consecuencia del arranque estrella-triángulo sin remisión al tema 2
RTVE); 4.1 (frase de entrada y párrafo de trifásica); 6.1 (cuarta fila de la tabla); 6.2 (frase de
la batería, sin la remisión al motor del tema 2 RTVE); 7.1 (primer párrafo y regla de los dos
criterios, de teitse/05 § 0); 7.2 (las cinco lecturas de la cita, de teitse/05 § 2); 7.3 (detalle
del 2 y de la raíz de tres, con «y da la caída en la tensión entre fases»; aviso de conductividad);
8.3 (último párrafo, de teitse/05 § 5); y todas las citas del art. 4 y de la ITC-BT-19 2.2.2, que
se han tomado de nuevo del BOE vigente.

Lo demás del tema (1.1, 1.3, 2.1 segunda tabla, 2.2 asociación, 2.4, 3.2 ecuación y números de la
red, 3.3, 4.1 triángulo, 4.2, 5 salvo una frase, 6.1 párrafo de armónicos, 6.2 fórmula y ejemplo,
6.3, 7.2 tabla de tramos, 7.3 fórmulas con la potencia, 7.4, 7.5, 8.1, 8.2, 8.4 y los tres bloques
finales) es redacción nueva.

## Preguntas tipo test de comprobación (10)

Respuesta correcta en negrita; a la derecha, dónde la contesta el tema. Las diez se contestan
enteras con el tema; no ha hecho falta ampliar.

1. (Baja tensión, teoría) Según el artículo 4.1 del REBT, una instalación de corriente alterna de
   tensión nominal 400 V es de: a) muy baja tensión; **b) tensión usual**; c) tensión especial;
   d) alta tensión. — Epígrafe 1.1.
2. (Magnitudes, práctica) Si en una línea se duplica la corriente sin cambiar el conductor, la
   potencia perdida en él por efecto Joule: a) se duplica; b) no varía; **c) se multiplica por
   cuatro**; d) se reduce a la mitad. — Epígrafe 2.4.
3. (Corriente alterna, teoría) En la red española de 230 V y 50 Hz, el valor de pico y el periodo
   son aproximadamente: a) 230 V y 50 ms; **b) 325 V y 20 ms**; c) 400 V y 20 ms; d) 163 V y 10 ms.
   — Epígrafes 1.2 y 3.2.
4. (Corriente alterna, teoría) En un receptor trifásico conectado en estrella: **a) la tensión de
   línea es √3 veces la de fase y las corrientes de línea y de fase son iguales**; b) las tensiones
   son iguales y la corriente de línea es √3 veces la de fase; c) la potencia es tres veces mayor
   que en triángulo; d) no hay punto neutro. — Epígrafe 3.4.
5. (Potencia, práctica) Una carga trifásica de 20 kW a 400 V con cos φ = 0,85 absorbe una corriente
   de línea de unos: a) 29 A; **b) 34 A**; c) 59 A; d) 102 A. — Epígrafe 4.2.
6. (Energía, práctica) Un plató con 20 kW de iluminación encendido 10 horas consume: a) 2 kWh;
   b) 20 kWh; **c) 200 kWh**; d) 720 MJ por hora. — Epígrafe 5.
7. (Factor de potencia, teoría) Según la ITC-BT-43, la compensación del factor de potencia de la
   totalidad de una instalación: a) es obligatoria hasta 0,9; b) puede dejar la instalación en
   régimen capacitivo en vacío; **c) ha de ser automática y asegurar que la variación del factor de
   potencia no sea mayor de ± 10 % del valor medio de un prolongado período de funcionamiento**;
   d) exige un interruptor común para receptor y condensador. — Epígrafe 6.3.
8. (Factor de potencia, práctica) Para llevar una carga de 20 kW de cos φ = 0,85 a cos φ = 0,95
   hace falta una batería de unos: a) 2,0 kvar; **b) 5,8 kvar**; c) 12,4 kvar; d) 20 kvar. —
   Epígrafe 6.2.
9. (Caída de tensión, teoría) En un edificio técnico que no es vivienda ni tiene transformador
   propio, la ITC-BT-19 limita la caída de tensión entre el origen de la instalación interior y
   cualquier punto de utilización a: a) 3 % en todos los circuitos; **b) 3 % en alumbrado y 5 % en
   los demás usos**; c) 4,5 % en alumbrado y 6,5 % en los demás usos; d) 1,5 % en alumbrado y 3 %
   en los demás usos. — Epígrafe 7.2.
10. (Equilibrado de cargas, práctica) Tres circuitos resistivos monofásicos conectados a L1, L2 y L3
    llevan 30, 20 y 10 A. La corriente por el neutro es de unos: a) 0 A; b) 10 A; **c) 17,3 A**;
    d) 60 A. Y en la instalación interior ese neutro, salvo justificación por cálculo, debe tener:
    a) la mitad de sección que las fases; **b) como mínimo la misma sección que las fases**. —
    Epígrafes 8.2 y 8.3.
