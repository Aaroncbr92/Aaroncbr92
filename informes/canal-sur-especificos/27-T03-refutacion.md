# Puesto 27 · Oficial Técnico Electricista · Tema 3 · Fase 4, refutación

Fecha de trabajo: 05-10-2026 (el encargo fija «hoy» en 24-09-2026). Tema refutado:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/03-cuadros-electricos-aparamenta-y-protecciones.md`.
No se corrige nada: sólo se informa. Ficheros tocados: este informe y `27-T03-preguntas.md`.

`27-T03-redaccion.md` lista «Copiado del común: ninguno» y «Copiado de RTVE sin cambios: ninguno»
(teitse/03 y 04, «actualizar: sí»): la exactitud mira el tema entero, como la cobertura.

## Fuentes releídas

| Fuente | Fecha de lectura | Qué se comprobó |
|---|---|---|
| RD 842/2002 (BOE-A-2002-18099), volcado consolidado `fuentes/canal-sur/BOE-A-2002-18099.md` | 05-10-2026 | Art. 15.3 y 16.2 (1 redacción); ITC-BT-01 (contactores, corriente de fuga, nivel de protección); ITC-BT-02 (vig. 04-04-2025): los once títulos citados y nota (7); ITC-BT-09 4; ITC-BT-17 entera; ITC-BT-19 2.2.4, 2.4, 2.6, 2.7, 2.9; ITC-BT-22 entera con notas (1) a (6); ITC-BT-23 entera con tabla 1; ITC-BT-24 3.2, 3.5, 4.1 a 4.1.3 con tabla 1; ITC-BT-28 1, 2.1 y 4 a)-f); ITC-BT-34 1, 3.1, 3.2; ITC-BT-47 3.1, 3.2, 4, 5; ITC-BT-52 6.1, 6.3, 6.4 (vig. 16-06-2022). Número de redacciones de cada bloque |
| RD 614/2001 (BOE-A-2001-11881), anexo IV | 05-10-2026 | A.1 y B.1 |
| INSST, guía técnica de riesgo eléctrico (`fuentes/canal-sur/tecnica/insst-guia-riesgo-electrico-2020.txt`, portada, introducción y líneas 4560-4625) | 05-10-2026 | Citas de seccionadores e interruptores, medidas frente a la maniobra errónea, datos de edición |

Lentes: `negritas.py` (REBT, RD 614/2001, guía INSST): 192 negritas, 4 «no están» (2 rótulos de
plantilla, 2 citas de la guía con guiones blandos, cotejadas a mano: literales), 0 en otro artículo.
Cada cita de ITC se leyó además bajo el rótulo de su apartado: todas en el apartado que dice el
tema. Cálculos rehechos (3.4: 1.667 / 167 / 50 / 80 Ω y 460 A; 8.3: 6 V): cuadran. Selectividad:
`grep` de «selectiv» y «tipo «S»» en todo el REBT da sólo los seis preceptos de la tabla de 8.1;
«curva C», sólo la ITC-BT-52 6.3. La tabla está completa.

## Lente 1 · Exactitud

Graves: 0.

Menores: 4.

1. **Prosa rota, 3.5**: «La solución que el / se desprende del apartado citado es subdividir». Resto
   de la corrección de la verificación. Propuesta: «La solución que se desprende del apartado
   citado es subdividir».
2. **Error 9, epígrafe 7 y Trazabilidad**: «4.ª edición» de la guía del INSST. El texto guardado
   sólo dice «Madrid, septiembre 2020» y que la edición actualiza la revisión de 2014; el ordinal no
   consta. Propuesta: «edición de septiembre de 2020» y quitar «4.ª».
3. **Error 6, 3.2**: «La instrucción se aplica a las instalaciones eléctricas temporales de ferias,
   exposiciones, muestras, stands y manifestaciones análogas (apartado 1)». El apartado 1 de la
   ITC-BT-34 dice **ferias, exposiciones, muestras, stands, alumbrados festivos de calles, verbenas
   y manifestaciones análogas**. Propuesta: completar la enumeración (y ponerla en negrita, ya que
   se da como literal).
4. **Error 9, 1.4**: la tabla de posiciones del código IP (letra adicional «cuando es mayor que la
   que da la primera cifra», letra suplementaria «información complementaria del fabricante») y «La
   letra X significa "no especificado"» son contenido de la UNE-EN 60529, que el tema declara no
   leída, y no figuran entre lo declarado como oficio en «Trazabilidad». Propuesta: añadir «la
   lectura de las posiciones del código IP» a la lista de oficio, o citar una fuente que lo dé.

Confirmado sin cambios: todas las citas literales, los rótulos de apartado, las redacciones de la
portada (todo una redacción salvo ITC-BT-02 y 52), las erratas del BOE conservadas («instalació n»,
«deforma», «esta», «kv») y la entrada duplicada del contactor de contactos cerrados de la ITC-BT-01.

## Lente 2 · Cobertura del enunciado

Las nueve materias del enunciado (cuadros y aparamenta, automáticos, diferenciales, fusibles,
contactores, relés, seccionadores, selectividad, sobretensiones) tienen epígrafe `##` propio y en su
orden. Test de 15 preguntas (`27-T03-preguntas.md`): 8 enteras, 2 a medias, 5 no.

Lagunas (7). Seis son datos que el tema declara «norma de producto no leída»; son de lo más
preguntado en un test de electricista, y el remate debe buscarles fuente citable (norma UNE-EN,
manual universitario o documentación de fabricante) o, si no la encuentra, dejarlas declaradas:

1. Múltiplos de disparo magnético de las curvas B, C y D (pregunta 3, no). Encaja en 2.3.
2. Corriente convencional de funcionamiento I2 ≤ 1,45 Iz junto a Ib ≤ In ≤ Iz (pregunta 4, a
   medias). Encaja en 2.1.
3. Qué detectan los diferenciales tipo F y tipo B (continua lisa en el B) (pregunta 7, no).
   Encaja en 3.3.
4. Clases de fusible gG y aM, y gR/semiconductores (pregunta 9, no). Encaja en 4.
5. Categorías de empleo de los contactores, al menos AC-1 y AC-3 (pregunta 10, no). Encaja en 5.1.
6. Significado de las cifras del código IP, al menos las que cita el REBT (IP 30, IP2X, IP4X, IP
   XXB, IP XXD; y la IK07) (pregunta 14, a medias). Encaja en 1.4.
7. **Ésta sí está en el BOE**: ITC-BT-47, apartado 5, segundo y tercer párrafos: un solo
   dispositivo contra la falta de tensión puede proteger a más de un motor si están en un mismo local
   y la suma de potencias absorbidas no supera 10 kW, o si cada uno queda automáticamente en el
   estado inicial de arranque; y no se exige al motor que arranca automáticamente en condiciones
   preestablecidas (pregunta 12, no). Encaja en 6.1, sustituyendo el «(…)».

Sugerencia sin rango de laguna: tipos de DPS (1, 2 y 3) y sus ondas de ensayo, ligados a la
protección basta, media y fina de 9.2; mismo problema de fuente que las lagunas 1 a 6.
