# Puesto 27 · Oficial Técnico Electricista · Tema 4 · Fase 5, remate

Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/04-canalizaciones-conductores-y-cableado.md`.
Entrada: `27-T04-refutacion.md` (0 graves, 4 menores, 2 lagunas) y `27-T04-preguntas.md` (preguntas 3, 7,
10 y 15). Fecha de trabajo y de lectura de la fuente: 05-10-2026 (el encargo fija «hoy» en 24-09-2026;
todos los preceptos tocados tienen una sola redacción, la original de 2002). Copia previa del tema en
el scratchpad de la sesión (`27t04-antes-remate.md`).

**Resultado: se amplía contenido nuevo** (tabla 11 de canales en 1.9; tensión asignada de la LGA y
otras tres filas en 1.3; regla de varios motores en 2.5; recomendación de 16 mm² en tubos al aire).
De 14.296 a 14.935 palabras (`wc -w`; 14.574 según `indice.py`); portada corregida a «Unas 14.500
palabras».

Ficheros tocados: el tema y este informe. Ninguno más.

## Fuente releída el 05-10-2026

RD 842/2002 (BOE-A-2002-18099), volcado consolidado, por `grep -n`: ITC-BT-14, 3; ITC-BT-19, 2.11;
ITC-BT-20, 2.2 (tabla 2, fila a fila); ITC-BT-21, 1.2.3, 2.3 (tabla de rozas), 3.1, 3.2 (tabla 11);
ITC-BT-28, 4.e; ITC-BT-30, 1.1.3 y 8; ITC-BT-47, 3. Todas, «1 redacción(es) en total».

## Correcciones de la refutación (las cuatro comprobadas y aplicadas)

1. **Menor 1 (ITC-BT-30, 8) · aplicada.** El BOE: «Cuando existan a los lados del pasillo de servicio
   piezas desnudas bajo tensión, no protegidas, aparatos a manipular o instrumentos a observar…
   1,30 metros». Fila de 8.1 rotulada ahora «Equipos enfrentados con partes desnudas, aparatos a
   manipular o instrumentos a observar a los lados», con la frase entera en negrita y: «Basta una de
   las tres cosas: un cuarto de cuadros con aparamenta que se manipula a ambos lados del pasillo pide
   1,30 m aunque no tenga ninguna pieza desnuda». Contesta la pregunta 10.
2. **Menor 2 (ITC-BT-47, 3) · aplicada.** Dos párrafos del BOE: un motor, 125 %; varios, suma del 125 %
   del mayor más los demás. Paso 1 de 2.5 dice ahora: «lámparas de descarga a 1,8 veces (tema 1);
   motores según la ITC-BT-47, apartado 3: un solo motor, **125 % de la intensidad a plena carga del
   motor**; varios, **la suma del 125 % de la intensidad a plena carga del motor de mayor potencia, más
   la intensidad a plena carga de todos los demás** (dos motores de 20 A y 10 A: 1,25 × 20 + 10 = 35 A,
   no 37,5 A)». Contesta la pregunta 15.
3. **Menor 3 (tabla 2 de la ITC-BT-20) · aplicada.** Columna «Sobre aisladores»: «–» en huecos accesibles
   y no accesibles, canal de obra, enterrados y empotrados; «+» sólo en montaje superficial y aéreo.
   1.6 dice ahora: «la instalación sobre aisladores sólo se admite en montaje superficial y aéreo: la
   tabla la marca «–» en huecos de la construcción, accesibles o no, en canal de obra, enterrados y
   empotrados en estructuras».
4. **Menor 4 (ITC-BT-19, 2.11) · aplicada.** Fila de 6.1: «Más de 6 mm² con tornillo de apriete entre una
   arandela metálica bajo su cabeza y una superficie metálica: terminal». 7.2, regla 2: «La puntera no
   la nombra el REBT: es un modo de oficio de cumplir su regla de que, en conductores de varios
   alambres cableados, las conexiones se hagan **de forma que la corriente se reparta por todos los
   alambres componentes** (ITC-BT-19, 2.11)».

## Lagunas (se amplía el tema)

1. **Tensión asignada de la LGA (pregunta 3).** Comprobado en ITC-BT-14, 3. Tabla de 1.3:
   - fila 0,6/1 kV, nueva entrada inicial: «LGA: **Los conductores a utilizar, tres de fase y uno de
     neutro, serán de cobre o aluminio, unipolares y aislados, siendo su tensión asignada 0,6/1 kV.**
     (ITC-BT-14, 3)»; la de pública concurrencia pasa a la literal de ITC-BT-28, 4.e (**Conductores
     rígidos aislados, de tensión asignada no inferior a 0,6/1 kV, armados, colocados directamente
     sobre las paredes**); y se añade ITC-BT-30, 1.1.3 (locales húmedos, cables armados sin tubo:
     **Los conductores tendrán una tensión asignada de 0,6/1 kV**).
   - fila 450/750 V: las otras dos opciones de ITC-BT-28, 4.e, literales (bajo tubos o canales; con
     cubierta en huecos RF-120).
2. **Características mínimas de las canales (pregunta 7).** Comprobado en ITC-BT-21, 3.2, tabla 11, celda
   a celda. En 1.9, tras la cita del número de conductores: frase de remisión literal del 3.2, título
   literal de la tabla, tabla de siete filas (≤ 16 mm / > 16 mm: impacto muy ligera/media; mínima
   +15/–5 ºC; máxima +60/+60 ºC; aislante / continuidad eléctrica-aislante; sólidos 4 / no inferior
   a 2; agua no declarada; no propagador), una línea sobre la temperatura mínima y el párrafo de las
   canales no ordinarias con su inciso literal.
   - Menores de la misma laguna: en 1.8 (al aire), la recomendación literal del 1.2.3 (**Se recomienda
     no utilizar este tipo de instalación para secciones nominales de conductor superiores a 16
     mm2.**); la tabla de rozas se declara en «Lo que este tema no da». Al comprobarla apareció un
     desajuste de la fuente, que se dice en el tema: el BOE la rotula «Tabla 10» y el texto del 2.3
     remite a «las recomendaciones de la tabla 8».

## Otros pasajes cambiados (consecuencia)

- Portada: «Fuente» añade ITC-BT-47; extensión, 14.500 palabras.
- «Qué se puede preguntar»: «…empotrado o enterrado, y las de una canal;».
- Normativa: ITC-BT-21, 3 (tabla 11); ITC-BT-47, apartado 3.
- Trazabilidad: ITC-BT-14 «composición y tensión asignada (apartado 3)»; ITC-BT-21 «3.2 (tabla 11)»;
  fila de ITC-BT-24 a 44 añade ITC-BT-47, 3 y ITC-BT-30, 1.1.3.

## Relectura de antecedentes

«Esa tabla» y «el mismo apartado» (1.9) siguen a la cita del 3.2; «la tabla la marca» (1.6), a «La tabla
2»; «su regla» (7.2), a «el REBT». Todo correcto.

## Lentes (después del remate)

- `indice.py`: índice regenerado, 45 epígrafes; sin cambios de rúbrica.
- `negritas.py` contra el volcado del REBT: 201 negritas, 2 «no están» (los rótulos «Enunciado del
  programa» y «Qué se puede preguntar», que no son citas). Antes: 190 y 2.
- `refutar_modo.py`: 0 hallazgos.
- `refutar_exactitud.py`: 24 «citas no literales», 21 antes. Es ruido de la herramienta, que busca
  artículos y no apartados de ITC; las tres nuevas son citas de ITC que `negritas.py` encuentra
  literales.
- `refutar_prosa.py`: 1 hallazgo, «cables fijados directamente sobre las paredes (ITC-BT-20, 2.2.2)»
  repetido entre la tabla de 1.3 y la rúbrica en cursiva de 1.10. Ya estaba antes del remate y es una
  remisión entre tabla y epígrafe, no relleno. No se toca.

## Para la fase 5 bis

Sólo los pasajes listados arriba. Preguntas 3, 7, 10 y 15: ahora enteras.
