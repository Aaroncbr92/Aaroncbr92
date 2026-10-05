# Refutación · Oficial Técnico Electricista (27) · Tema 7 · Grupos electrógenos, SAI y continuidad de servicio

Fase 4. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/07-grupos-electrogenos-sai-y-continuidad-de-servicio.md`.
No se ha corregido nada. Ficheros tocados: este informe y `27-T07-preguntas.md`.
Fecha de lectura de todas las fuentes: 05-10-2026 (reloj del sistema; el encargo dice «hoy es
24-09-2026»; ninguna fuente usada cambia entre las dos fechas).

Exactitud: se salta lo listado en «Copiado de RTVE sin cambios» de `27-T07-redaccion.md` (no hay
«Copiado del común»). Cobertura: el tema entero.

## Fuentes releídas

| Fuente | Cómo | Resultado |
|---|---|---|
| ITC-BT-40 (BOE-A-2002-18099, `ib-40`, redacción RD 244/2019, vigente desde 07-04-2019) | `boe.py precepto` | Apdos. 1, 2, 3, 4.1, 4.2, 5, 6, 7, 8.2.1, 8.2.2 y 9: todas las negritas literales y bien atribuidas |
| ITC-BT-28 (`ib-28`, redacción única) | `boe.py precepto` | Apdos. 2, 2.1, 2.2, 2.3, 3, 3.1.1-3.1.3, 4.g: literales (con las dos salvedades de abajo) |
| ITC-BT-38, apdo. 2.2 | `boe.py precepto ib-38` | «autonomía no inferior a 2 horas»: bien |
| REBT, art. 10 | volcado, `sed` líneas 250-259 | 10.1 literal; 10.3 recortado (hallazgo 3); 10.2 no está (laguna 1) |
| RIPCI, anexo II, apdo. 1 y tabla I (redacción desde 10-05-2025) | volcado, líneas 844-965 | Literales; quién puede hacer la tabla I, bien |

Cálculos comprobados: 4 × 12 V × 100 Ah = 4.800 Wh y 8 × 1.200 Wh = 9.600 Wh (5.3); 9,6 kWh ÷
20 kW = 0,48 h, «casi media hora» (6.1). Remisiones internas (1.5→3.2, 3.2→6.3, 5.2→7.1, 6.1→1.5
fase 3, 8.3→5.3, 2→3.1 y 2.2): todas con antecedente. `refutar_prosa.py`: 0. Sölter no se ha
releído (lo verificó la fase 3).

## Exactitud

Graves: **0**.

Menores: **4**.

1. **Error 6 · ámbito de la ITC-BT-28** (3.1, 3.2, 5.2 y 7.3). La ITC-BT-28 es la instrucción de
   locales de pública concurrencia; el tema la presenta en el epígrafe 3 como si regulara los
   servicios de seguridad de cualquier edificio («Lo que sí dice el REBT, para las fuentes de los
   servicios de seguridad…», 7.3; «la ITC-BT-28 exige… para toda fuente de seguridad que no sea un
   equipo autónomo», 5.2). La salvedad sólo está en 1.5 y al final de 3.3. Propuesta: una frase a la
   entrada de 3.1 («la ITC-BT-28 es la de locales de pública concurrencia; fuera de ellos, sus
   categorías y fuentes sirven de referencia, no de obligación») y «en un local de pública
   concurrencia» en 5.2 y 7.3.
2. **Error 6 · 3.1, «puede ser automática o no automática»**. El BOE dice **«La alimentación para
   los servicios de seguridad, en función de lo que establezcan las reglamentaciones específicas,
   puede ser automática o no automática.»** El tema corta la condición. Propuesta: citar la frase
   entera.
3. **Error 6 · 3.3, art. 10.3**. El tema dice «El artículo 10.3 añade que **los órganos
   competentes…**», omitiendo el arranque **«Además de los señalados en las correspondientes
   instrucciones técnicas complementarias,»**, que es lo que enlaza con la ITC-BT-28 citada justo
   antes. Propuesta: citar el apartado desde «Además».
4. **Error 9 (presentación) · entrada del epígrafe 2**. «El SAI de doble conversión es la única de
   las fuentes de este tema que cumple la categoría «sin corte» de la ITC-BT-28» va en firme, sin la
   marca de oficio que sí lleva la tabla de 3.1 («la ITC no asigna categorías a las fuentes»).
   Propuesta: añadir «(oficio)» o «a juicio de oficio» en esa frase y en el párrafo de 2.2 que repite
   «la única que cumple la categoría «sin corte»» (este último es copia de RTVE; basta con la frase
   nueva del epígrafe 2).

Sin otros hallazgos: las cifras normativas (85 %/110 %/0,5 s, 49-51 Hz y 5 períodos, 125 % y 1,5 %,
4/n-5-25/n, 0,15/0,5/15 s, 70 %, 15/25/50 %, 300 personas, 100 vehículos, 2.000 m², 100 kVA, 5 s,
una hora, 2 horas) están en su fuente y en su apartado.

## Cobertura del enunciado

Las ocho piezas del enunciado (grupos, SAI, continuidad, transferencia, baterías, autonomía, pruebas,
incidencias) tienen epígrafe propio y en su orden. Preguntas: **12 enteras, 2 a medias, 1 no**
(`27-T07-preguntas.md`).

Lagunas: **3**.

1. **Art. 10.2 del REBT** (pregunta 11, «no»). Es la norma general de la transferencia entre
   suministro normal y complementario: **«Las instalaciones previstas para recibir suministros
   complementarios deberán estar dotadas de los dispositivos necesarios para impedir un acoplamiento
   entre ambos suministros, salvo lo prescrito en las instrucciones técnicas complementarias. La
   instalación de esos dispositivos deberá realizarse de acuerdo con la o las empresas
   suministradoras. De no establecerse ese acuerdo, el órgano competente de la Comunidad Autónoma
   resolverá lo que proceda en un plazo máximo de 15 días hábiles…»**. Ampliar en 3.3 o en 4.2 (dos
   o tres líneas).
2. **Regímenes de carga de la batería** (pregunta 10, «a medias»): flotación, carga y, en su caso,
   igualación; qué controla el cargador del SAI y el del grupo. Sólo oficio o fuente técnica; sin
   cifras de tensión si no se leen en documentación de fabricante (el tema ya declara que no da las
   tensiones de flotación).
3. **Dimensionado conjunto grupo-SAI** (pregunta 15, «a medias»): el tema dice que se eligen juntos
   pero no por qué el grupo se dimensiona por encima de la potencia del SAI (distorsión del
   rectificador, recarga de la batería). Una frase de oficio en 2.4 o 6.2, sin coeficiente si no hay
   fuente.

Menor, no laguna: la ITC-BT-28, 3.1, dice que la instalación del alumbrado de seguridad **«será fija y
estará provista de fuentes propias de energía. Sólo se podrá utilizar el suministro exterior para
proceder a su carga, cuando la fuente propia de energía esté constituida por baterías de acumuladores
o aparatos autónomos automáticos.»**; apoyaría la frase de 3.1 sobre la batería propia del alumbrado
de emergencia, pero es materia del tema 6.

## Recuento

Graves 0 · menores 4 · lagunas 3.
