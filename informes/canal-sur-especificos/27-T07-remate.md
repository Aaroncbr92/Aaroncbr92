# Remate · Oficial Técnico Electricista (27) · Tema 7 · Grupos electrógenos, SAI y continuidad de servicio

Fase 5. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/07-grupos-electrogenos-sai-y-continuidad-de-servicio.md`.
Entradas: `27-T07-refutacion.md` (graves 0 · menores 4 · lagunas 3) y `27-T07-preguntas.md` (12 enteras, 2 a medias, 1 no).
Ficheros tocados: el tema y este informe. Nada más.
Fecha de lectura de las fuentes: 05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»; ninguna fuente usada cambia entre las dos fechas).

**Amplió contenido nuevo: sí** (art. 10.2 del REBT; regímenes de carga; sobredimensionado grupo-SAI). Procede la fase 5 bis sobre los pasajes de abajo.

## Comprobación en la fuente

| Corrección | Fuente releída (05-10-2026) | Resultado |
|---|---|---|
| Menor 1 · ámbito de la ITC-BT-28 | `boe.py precepto BOE-A-2002-18099 ib-28`, apdo. 1 «CAMPO DE APLICACIÓN: La presente instrucción se aplica a locales de pública concurrencia…» | Confirmada. Aplicada |
| Menor 2 · «puede ser automática o no automática» | ITC-BT-28, apdo. 2, mismo volcado | Confirmada: la frase lleva «en función de lo que establezcan las reglamentaciones específicas». Aplicada |
| Menor 3 · art. 10.3 desde «Además» | `fuentes/canal-sur/BOE-A-2002-18099.md`, líneas 251-260 (art. 10, redacción única) | Confirmada. Aplicada |
| Menor 4 · «sin corte» del SAI como oficio | Tabla de 3.1 del propio tema («la ITC no asigna categorías a las fuentes»); ITC-BT-28, apdo. 2, no asigna categorías | Confirmada. Aplicada en la entrada del epígrafe 2 (el párrafo de 2.2, copia de RTVE, no se toca: la marca de la entrada lo cubre, como propone la refutación) |
| Laguna 1 · art. 10.2 | Mismo volcado, art. 10.2 | Literal confirmado. Ampliado en 3.3 y remisión en 4.2 |
| Laguna 2 · regímenes de carga | Sin fuente técnica leída (ni investigación ni fase 3 traen una) | Ampliado **como oficio**, sin ninguna cifra de tensión o corriente; lo declara el propio pasaje, «Lo que este tema no da» y «Trazabilidad» |
| Laguna 3 · dimensionado grupo-SAI | Sin fuente técnica leída | Ampliado **como oficio**, sin coeficiente; declarado igual |

Ninguna corrección del informe de refutación resultó equivocada.

## Pasajes cambiados

1. **Portada, Extensión**: 11.600 → 12.400 palabras (recuento de `indice.py`: 11.704 antes, 12.401 después).
2. **«Qué se puede preguntar»**: añade «qué dispositivos exige el REBT a quien los recibe» y «qué regímenes de carga lleva una batería».
3. **Entrada del epígrafe 2**: «A juicio de oficio (la ITC no asigna categorías a las fuentes), el SAI de doble conversión es la única… que cumple la categoría «sin corte»…».
4. **2.4, párrafo nuevo al final** (laguna 3): el grupo que alimenta un SAI se dimensiona por encima de la potencia del SAI; tres razones (corriente distorsionada del rectificador, recarga de la batería sumada a la carga, rendimiento del SAI); la batería no permite un grupo menor; el coeficiente lo da el fabricante, no norma leída. Marcado «(oficio)».
5. **3.1, párrafo nuevo de entrada** (menor 1): la ITC-BT-28 es la de locales de pública concurrencia (su apdo. 1); obliga en ellos; fuera, sirve de referencia.
6. **3.1, primer párrafo** (menor 2): la frase de la ITC citada entera: **«La alimentación para los servicios de seguridad, en función de lo que establezcan las reglamentaciones específicas, puede ser automática o no automática.»**
7. **3.3, art. 10.3** (menor 3): ahora cita desde **«Además de los señalados en las correspondientes instrucciones técnicas complementarias, los órganos competentes…»**, introducido como «El artículo 10.3 del REBT completa esa lista» (antecedente: la lista de la ITC-BT-28, 2.3, justo antes).
8. **3.3, párrafo nuevo** (laguna 1): art. 10.2 del REBT literal entero, con la nota «Es «deberán», no «podrán»» y la salvedad de las ITC.
9. **4.2, frase nueva** antes de «La transferencia ordinaria…»: enlaza el enclavamiento de la ITC-BT-40, 4.2, con el art. 10.2 (remisión a 3.3).
10. **5.1, tabla y párrafo nuevos al final** (laguna 2): carga, flotación e igualación (ésta sólo si el fabricante la prevé); el rectificador como cargador del SAI; el cargador propio de la batería de arranque del grupo; por qué la tensión de flotación no mide capacidad (remisión a 7.2). Marcado «(oficio)», sin cifras.
11. **5.2** (menor 1): «para toda fuente de seguridad **de un local de pública concurrencia** que no sea un equipo autónomo».
12. **7.3** (menor 1): «para las fuentes de los servicios de seguridad **de un local de pública concurrencia**».
13. **Normativa que el tema invoca**: art. 10 «(tipos de suministro y dispositivos que impiden el acoplamiento)»; ITC-BT-28 añade el apdo. 1.
14. **Lo que este tema no da**: añade las tensiones y corrientes de carga y de igualación y los coeficientes de sobredimensionado de un grupo que alimenta un SAI.
15. **Trazabilidad**: art. 10 añade 10.2; ITC-BT-28 añade apdo. 1 y «automática o no automática»; el párrafo de oficio añade los regímenes de carga y el sobredimensionado.

Antecedentes releídos en cada pasaje: «Y añade» (3.1) tiene delante «La ITC-BT-28, apartado 2, define…»; «esa lista» (3.3) tiene delante la ITC-BT-28, 2.3; «los dos suministros» y «ambos» remiten al normal y al complementario recién definidos; las remisiones nuevas (3.4, 3.3, 2.1, 5.2, 7.2) apuntan a epígrafes que tratan lo dicho.

## Preguntas que cambian

- P10 (regímenes de carga): de «a medias» a **entera** (5.1).
- P11 (art. 10.2): de «no» a **entera** (3.3).
- P15 (dimensionado grupo-SAI): de «a medias» a **entera** (2.4).

## Lentes

- `indice.py`: 43 epígrafes, índice sin cambios (no hay epígrafes nuevos).
- `negritas.py` con el REBT y el RIPCI: 106 negritas; 8 «no están», todas ajenas al BOE (dos rótulos del tema y seis citas de Sölter, fuente técnica). 0 mal atribuidas.
- `refutar_exactitud.py`: 18 citas con apartado comprobadas, 12 «no literales», las mismas 12 que da el tema sin tocar (17/12): la lente lee los apartados de las ITC como artículos del Reglamento; `negritas.py` las encuentra todas literales. La cita nueva (art. 10.2) no salta.
- `refutar_modo.py`: 0 hallazgos.
- `refutar_prosa.py`: 0 hallazgos.
