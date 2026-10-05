# Puesto 27 · Oficial Técnico Electricista · Tema 3 · Fase 5, remate

Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/03-cuadros-electricos-aparamenta-y-protecciones.md`.
Entrada: `27-T03-refutacion.md` (0 graves, 4 menores, 7 lagunas y una sugerencia) y `27-T03-preguntas.md`
(8 enteras, 2 a medias, 5 no). Fecha de trabajo y de lectura de las fuentes: 05-10-2026 (el encargo
fija «hoy» en 24-09-2026). Copia previa del tema en el scratchpad de la sesión (`27t03-antes-remate.md`).

**Resultado: se amplía contenido nuevo.** De 14.195 a 17.031 palabras (`indice.py`); portada
corregida a «Unas 17.000 palabras». No cambian los epígrafes (40), así que el índice sigue igual.

Ficheros tocados: el tema, este informe y una carpeta nueva de fuente,
`fuentes/canal-sur/tecnica/schneider-eig/` (siete páginas en wikitexto y dos figuras del código IP
pasadas a PNG). Nada más.

## Fuentes nuevas leídas el 05-10-2026

| Fuente | Cómo | Para qué |
|---|---|---|
| RD 842/2002, ITC-BT-47, apartado 5 entero; ITC-BT-34, apartado 1 | `grep -n` en `fuentes/canal-sur/BOE-A-2002-18099.md` (una sola redacción) | Laguna 7 y menor 3 |
| INSST, guía de riesgo eléctrico, portada e introducción (líneas 33-43 y 239-240 del `.txt`) | `grep` | Menor 2: sólo consta «Madrid, septiembre 2020» y la revisión de 2014; ningún ordinal |
| Schneider Electric, *Electrical Installation Guide* (wiki en línea, `electrical-installation.org/enw`), páginas «Fundamental characteristics of a circuit-breaker» (figura H28), «Practical values for a protective scheme», «Elementary switching devices» (H5, H10), «Types of RCDs», «Motor starter configurations» (N83), «Protection provided for enclosed equipment: codes IP and IK» (E66, E67, E68, E69, E70) y «The Surge Protection Device (SPD)» (J18) | `curl ...&action=raw`; las figuras E66 y E67 del código IP son SVG con el texto en trazos, pasadas a PNG con `cairosvg` y leídas como imagen | Lagunas 1 a 6 y la sugerencia de los tipos de DPS |

Por qué esta fuente: el encargo admite documentación de fabricante para lo técnico; es una guía
de diseño completa, de acceso libre, que explica las normas IEC que el tema declaraba no leídas. Se
cita traducida, en redonda y atribuida en cada pasaje; nunca como texto de norma. Las normas
(UNE-EN 60898-1, 60269, 62423, 60529, 61643-11; IEC 60755, 60947-4-1, 62262) siguen sin leerse y así
lo dice el tema.

## Correcciones de la refutación

1. **Menor 1 (prosa rota, 3.5) · aplicada.** Ahora: «La solución que se desprende del apartado
   citado es subdividir».
2. **Menor 2 («4.ª edición», 7 y Trazabilidad) · aplicada.** Comprobado: el `.txt` sólo dice
   «Edición: Madrid, septiembre 2020». Ahora «edición de septiembre de 2020» en los dos sitios.
3. **Menor 3 (ITC-BT-34, 1, 3.2) · aplicada.** Cotejada con el BOE. Ahora, en negrita: «La
   instrucción se aplica a **las instalaciones eléctricas temporales de ferias, exposiciones,
   muestras, stands, alumbrados festivos de calles, verbenas y manifestaciones análogas**
   (apartado 1).» Se añade el apartado 1 a «Normativa» y a «Trazabilidad».
4. **Menor 4 (código IP sin fuente, 1.4) · aplicada mediante fuente.** La fila «letra adicional
   … cuando es mayor que la que da la primera cifra» no la confirma la guía, así que se quita esa
   coletilla. La tabla se rehace con la guía (ver laguna 6), y la regla de la X se apoya ahora en la
   figura E66 («Where a characteristic numeral is not required to be specified, it shall be replaced
   by the letter "X"»).

## Lagunas: ampliación

| Laguna | Dónde | Qué se añade | Pregunta |
|---|---|---|---|
| 1 · curvas B, C, D | 2.3, tras la tabla de curvas | Tabla con 3-5, 5-10 y 10-20 In (IEC 60898, figura H28); nota de los 50 In para D y de los 10-14 In de Schneider; en los industriales (IEC 60947-2) decide el fabricante; Ir = In; ejemplo PIA 16 A (B 48-80, C 80-160, D 160-320 A) | 3 |
| 2 · I2 ≤ 1,45 Iz | 2.1, sustituye el párrafo «regla de oficio… no leída» | Las tres condiciones (Ib ≤ In ≤ Iz; I2 ≤ 1,45 Iz con tiempo convencional de 1 o 2 h; poder de corte ≥ Icc); en automáticos la segunda se cumple sola; en fusibles k2 = 1,6-1,9 y In ≤ Iz/k3 (k3 = 1,31 por debajo de 16 A; 1,10 desde 16 A); ejemplo Ib 20 A, Iz 27 A | 4 |
| 3 · diferenciales F y B | 3.3, tabla de clases y párrafo nuevo | AC, F y B con la guía (IEC 60755 / 62423): F, multifrecuencia y continua lisa superpuesta de 10 mA; B, además, continua lisa y de 50 a 1.000 Hz; «muñecas rusas»; usos típicos | 7 |
| 4 · clases de fusible | 4, tras «datos que se piden» | Designación por dos letras (g/a, G/M); clases gG, aM, gM; gI; corrientes convencionales gG (1,25 y 1,6 In en 1 h, de más de 16 A a 63 A). Los fusibles de semiconductores (gR) **no** constan en lo leído y quedan declarados | 9 |
| 5 · categorías de empleo | 5.1, tras «datos que se piden al comprarlo» | Tabla AC-1 a AC-4 (IEC 60947-4-1, figura N83); ejemplo de 150 A en AC-3 (corte 8 In, cierre 10 In, cos φ 0,35); «discontactor» limitado a 8-10 In | 10 |
| 6 · código IP e IK | 1.4, sustituye la tabla y el párrafo siguiente | Estructura del código (E66), tabla de cada valor de las dos cifras y de las letras (E67), lectura de IP 30, IP2X, IP4X, IP XXB, IP XXD; IK00-IK10, IK07 = 2 J (E68, IEC 62262); recomendación del fabricante IP 30 / IK07 en salas técnicas | 14 |
| 7 · ITC-BT-47, 5 | 6.1, sustituye el «(…)» | Cita entera en negrita (10 kW, estado inicial de arranque, excepción del arranque automático y de los limitadores) y párrafo de tres datos | 12 |
| Sugerencia · tipos de DPS | 9.4, tras la mención de la UNE-EN 61643-11 | Tabla tipos 1, 2 y 3 con ondas 10/350, 8/20 y 1,2/50 + 8/20; Iimp, Imax, Uc, Up, In (19 veces); tipo 1+2; correspondencia de oficio con la cascada basta/media/fina | — |

Además: siglas nuevas presentadas en la entrada (DPS tipos 1-3; gG, gM, aM; AC-1 a AC-4; Im, Ir, I2,
k2, k3, Iimp, Imax, In del DPS, Uc, Up; Hz, µs); «Qué se puede preguntar» recoge lo nuevo;
«Normativa» añade las IEC 60755, 60947-4-1 y 62262 como no leídas; «Lo que este tema no da» sustituye
las dos viñetas de normas no leídas por una que explica el uso de la guía, y añade los fusibles de
semiconductores; «Trazabilidad» añade la fila de la guía; el párrafo final de oficio aclara que lo de
la guía va atribuido.

Con esto, las quince preguntas de `27-T03-preguntas.md` se contestan enteras con el tema.

## Pasajes cambiados (para la fase 5 bis)

Portada (Fuente, Extensión); siglas; «Qué se puede preguntar»; 1.4 (desde «El código IP, en lo que
hay que saber leer» hasta «…deja de tener IP (oficio)»); 2.1 (desde «Esa norma UNE no se ha leído»
hasta el ejemplo de fusible gG); 2.3 (desde «B es la que antes dispara» hasta «…corriente de defecto
es baja»); 3.2 (frase del apartado 1 de la ITC-BT-34); 3.3 (tabla de clases y párrafo de la UNE-EN
62423 con sus tres viñetas); 3.5 (frase de la subdivisión); 4 (desde «Las clases de fusible de baja
tensión» hasta «…no se dan aquí»); 5.1 (desde «Las categorías de empleo de los contactores» hasta
«…distintas de las del contactor»); 6.1 (cita del apartado 5 y párrafo «Tres datos»); 7 (edición de
la guía del INSST); 9.4 (desde «Lo que de esa norma explica» hasta «…con tipo 3»); Normativa; Lo que
este tema no da; Trazabilidad (filas INSST, Schneider, ITC-BT-34 y 47) y párrafo final.

Antecedentes releídos: «Esa norma UNE» (2.1) tiene delante la UNE 20.460-4-43; «la misma guía»
(2.1, 2.3, 3.3, 5.1, 9.4) tiene siempre delante la guía de Schneider citada en el mismo pasaje; «Dos
matices de la misma tabla» (2.3), la tabla de márgenes; «Esa norma no se ha leído» (3.3), la
UNE-EN 62423; «ese apartado» (6.1), el apartado 5 recién citado; «el dato del epígrafe 2.1» (4),
la condición I2 ≤ 1,45 Iz.

## Lentes

- `indice.py`: 17.031 palabras, 40 epígrafes (antes 14.195 y 40).
- `negritas.py` (REBT, RD 614/2001, guía INSST): 194 cotejadas (192 antes); las mismas 4 «no están»
  (dos rótulos de plantilla y las dos citas de la guía del INSST con guiones blandos, ya cotejadas a
  mano en la refutación); 0 en otro artículo. Las dos nuevas (ITC-BT-34, 1 e ITC-BT-47, 5), literales.
- `refutar_exactitud.py`: 30 citas con apartado entre paréntesis, 29 «no literales» (antes 31 y 30):
  el falso positivo conocido de las ITC, que no numeran por artículos; nada nuevo.
- `refutar_modo.py`: 0 hallazgos.
- `refutar_prosa.py`: 0 hallazgos, sin diferencias respecto de antes.

**Pide fase 5 bis**: la ampliación es de unas 2.800 palabras con fuente nueva.
