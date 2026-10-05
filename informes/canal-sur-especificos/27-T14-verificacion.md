# Verificación · Oficial Técnico Electricista (27) · Tema 14 · Medidas eléctricas e instrumentación

Fase 3. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/14-medidas-electricas-e-instrumentacion.md`
(13.229 palabras tras la verificación, 44 epígrafes). Fecha de lectura de todas las fuentes:
05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»; ningún precepto citado cambió
entre ambas fechas).

## Lo copiado

- **Copiado del común**: nada (el informe de redacción lo declara así).
- **Copiado de RTVE sin cambios**: 28 pasajes (`teitse/09` §4-§5 y `teitse/01` §5) comprobados por
  script con el texto normalizado (sin negritas, tildes ni puntuación): los 28 están literalmente en el
  tema y en su fichero RTVE. No se re-verificaron.
- **Adaptado de RTVE** (sí verificado): fila del megóhmetro (5.1) y su explicación (5.2), contra la
  ITC-BT-19, 2.9: correcto; fila 1 del método de tierras (4.3) y aviso 2 (4.4), contra la ITC-BT-18,
  3.3 y 12: correctos; párrafo del valor admisible (4.1), contra la ITC-BT-18, 9, y la ITC-BT-24,
  4.1.2: correcto, con una salvedad omitida (corregida, abajo); histórico y devanados (5.6): oficio,
  ahora rotulado así.

## Fuentes releídas

- BOE consolidado (API, 05-10-2026): metadatos del RD 842/2002 (última actualización 18-12-2025);
  títulos de BOE-A-2025-17507 (RD 770/2025), BOE-A-2014-13681 (RD 1053/2014), BOE-A-2010-8190
  (RD 560/2010), BOE-A-2001-11881 (RD 614/2001, de 8 de junio).
- REBT con `boe.py precepto`: ITC-BT-01; ITC-BT-03 (5 redacciones; diff del apéndice I.2 entre la
  redacción anterior y la del RD 770/2025: idéntico); ITC-BT-05 (2.1 y 3); ITC-BT-18 (3.3, 9,
  tablas 3-5, 12); ITC-BT-19, 2.9 entero; ITC-BT-24, 4.1, 4.1.1, tabla 1 y 4.1.2; ITC-BT-02
  (UNE-EN 61008-1 y 61009-1). Fechas de vigencia de la ficha: todas confirmadas.
- RD 614/2001: anexo I (8, 10, 13, 14), anexo II (B.3, B.4.1 y su rótulo de alta tensión), anexo IV
  (A.1-A.6, B.2 2.ª), anexo V (B.1.2).
- Guía del INSST 2020; Fluke 2003; Circutor CDB; AEMC 2003; FLIR 2011 (los `.txt` de
  `fuentes/canal-sur/tecnica/`), cada cifra y cada cita en su página.

## Lentes

`negritas.py` contra las dos normas y las cinco fuentes técnicas: 187 negritas; 8 «no está», todas
falsas alarmas comprobadas a mano (2 rótulos de forma; 5 citas del INSST con guion blando U+00AD
partido por el `.txt`; 1 de AEMC con la ligadura «ﬁ»). `refutar_exactitud.py`: 4 avisos, falsos
positivos (lee «apartado 2.1» de una ITC o «epígrafe 1.2» del tema como artículos del real decreto).
`refutar_modo.py`: 0. `refutar_prosa.py`: 0. `indice.py`: índice al día.

## Correcciones aplicadas (13)

1. **Error 4 y 6** (5.6). La guía del INSST dice que la descarga tras el ensayo de aislamiento
   **debería** hacerse, y antes avisa de que **en la mayoría de los casos esta carga es muy pequeña**.
   El tema decía «hay que» y omitía la salvedad. Se ha corregido.
2. **Error 6** (4.1). La ITC-BT-18, 9, tiene un párrafo de salvedad, la **rápida eliminación de la
   falta** cuando puedan superarse las tensiones de contacto, que el tema omitía. Se ha añadido.
3. **Error 1** (4.6). «Las tablas 3 y 4 dan resistividades **a título de orientación**»: esa expresión
   es de la tabla 3. Los ejemplos (50 y 3.000 Ω·m) son de la tabla 4, «valores medios». Se han separado.
4. **Error 3** (7.4). Decía «las tres características que la guía de FLIR manda evaluar», pero la guía
   enumera seis requisitos. Ahora se nombran los seis y se explica que se dan los tres que se miden en cifras.
5. **Error 9** (4.3). «Sus bornes suelen rotularse X, Y, Z» no tiene fuente. AEMC dice que otros
   probadores los rotulan X, P, C o C1, P2, C2. Corregido.
6. **Error 9** (1.5, tabla de Circutor). Decía que el comprobador «calcula la tensión de contacto que
   aparecería con IΔn», y el manual no lo dice. Ahora dice que muestra la tensión de contacto y el valor
   calculado de la impedancia del bucle.
7. **Error 9** (1.4). Decía que la impedancia de 0,01 Ω era «del orden de» la de un borne de 10 A en
   general. Es la de **un multímetro Fluke**, y así se dice ahora.
8. **Error 9** (4.4). Según AEMC, la resistividad depende de los «electrolitos (humedad, minerales y
   sales disueltas)». El tema decía «agua y sales». Corregido.
9. **Error 9** (4.5). Lo que incluye la lectura de la pinza: según la guía, las conexiones de enlace
   entre la pica y el **neutro del sistema**, no «hasta el punto de retorno». Corregido.
10. **Error 1** (4.6, epígrafes 1.2 y «Lo que no da»). Remisiones a otros temas sin contenido que las
    respalde:
    - «Centro emisor en terreno rocoso (tema 8, 6.2)»: el tema 8 no habla de terreno rocoso.
    - «Luxómetro: tema 6»: el tema 6 da los niveles de iluminación, pero no describe el instrumento.

    Se han reformulado las dos.
11. **Error 9** (trazabilidad y epígrafe 1.2). La trazabilidad decía que la ITC-BT-05 se nombraba
    «en el índice del epígrafe 1.2», y no se nombraba en el cuerpo. Se ha añadido a 1.2 la cita literal
    de la ITC-BT-05, 2.1 y 3, leída en el BOE, y se han ajustado la fila de trazabilidad y la de normativa.
12. **Error 9** (trazabilidad). La guía del INSST figuraba como «4.ª ed.», dato que la portada no
    confirma. Ahora consta como «Madrid, septiembre de 2020».
13. **Forma**:
    - En 1.2, «**no**» era una negrita de énfasis y se ha pasado a redonda.
    - Se ha quitado la sigla «UL», que no usa ninguna fuente.
    - «(oficio)» rotula ahora dos afirmaciones sin fuente: que los tres equipos suelen ir reunidos en un
      aparato y el valor del histórico.

Releídos los pasajes cambiados: cada «el mismo apartado», «la guía» o «esas verificaciones» tiene
delante su antecedente.

## Confirmado sin cambios (muestra de lo que más riesgo tenía)

- Lista de equipos de la ITC-BT-03 (2.1.2 y 2.2), literal.
- Tabla 3 de la ITC-BT-19 y regla de los 100 m.
- Polaridad del generador, receptores a tierra / entre conductores, circuitos electrónicos, rigidez
  (2U + 1000 V, mínimo 1.500 V, 1 minuto) y su excepción.
- Zs × Ia ≤ U0 y 0,4 s a 230 V.
- RA × Ia ≤ U y el selectivo de 1 s.
- Revisión anual y la de cinco años de la ITC-BT-18, 12.
- Fórmulas de la tabla 5.
- Definiciones y A.1-A.6 del RD 614/2001.
- B.4.1 bajo el rótulo de alta tensión, ya avisado en el tema.
- Cifras de Circutor: 0,45 IΔN, 600/1000 ms, 60 ms, 6/10/30 mA, rampa 0,30-1,40 IΔN, 25/50 V.
- Cifras de AEMC: 62 %, ±10 % a cada lado de la distancia X-Z, ±2/5/10 %, 2,4 kHz, 5 A, A > 20 B,
  ρ = 2πAR.
- Cifras de FLIR: 0,97/36,7 °C, 0,15/98,3 °C, 60 × 60, 640 × 480 y 307.200, 63,9/42,7 °C,
  30 mK, ±2 %/±2 °C, cuatro pasos, puntos fríos.
- Categorías CAT de Fluke y el método de los tres pasos.
- Remisiones a los temas 1, 3 y 8.

## Ficheros tocados

El tema y este informe. Ninguno más.
