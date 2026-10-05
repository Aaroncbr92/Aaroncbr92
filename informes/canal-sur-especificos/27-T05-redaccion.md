# Puesto 27 · Oficial Técnico Electricista · Tema 5 · Fase 2, redacción

Fecha de trabajo: 05-10-2026 (el encargo fija «hoy» en 24-09-2026; ningún precepto citado cambió
entre ambas fechas: el BOE consolidado del REBT da como última actualización el 18-12-2025). Tema
escrito:
`temas/canal-sur-especificos/27-oficial-tecnico-electricista/05-puestas-a-tierra-y-equipotencialidad.md`
(12.655 palabras según `indice.py`; 7 rúbricas `##` en el orden del enunciado, la primera es el
rótulo «Puestas a tierra y equipotencialidad»; 27 epígrafes `###`).

Ficheros tocados: sólo el tema y este informe.

Material: `27-investigacion-A-electrico.md` § 1, § 6, § 7 y § 9; RTVE `teitse/03` (§ 4, 5 y 6),
`teitse/09` (§ 4 y 5) y `tese/15` (§ 4) — fila 27·5 de `informes/canal-sur-reuso/tecnica.tsv`:
80 %, **actualizar: sí**; AGRUPACION.tsv: 27·5 «nuevo».

Extensión: 12.655 palabras, algo por debajo del tema 3 (13.847). El enunciado tiene siete rúbricas,
y la ITC-BT-18 se cita casi entera y la ITC-BT-24 en sus apartados 2 a 4. Si el coordinador quiere
menos, lo recortable es prosa de oficio en 3.2, 4.2 y 7.3; ningún dato.

Lentes pasadas al cerrar:
- `negritas.py` contra `BOE-A-2002-18099.md` y la guía del INSST (`.txt`): 250 negritas; 3 «no
  están»: 2 rótulos de la plantilla («Enunciado del programa», «Qué se puede preguntar») y la cita
  de la tensión de paso de la guía del INSST (6.4), literal, que la lente no encuentra porque el
  `.txt` parte «separa­dos» con guion blando (línea 2619). El verificador debe cotejarla a mano en
  `fuentes/canal-sur/tecnica/insst-guia-riesgo-electrico-2020.txt`, líneas 2617-2620. 0 «otro
  artículo». (Antes de corregir había 9: cuatro rótulos propios en negrita, ya en redonda; una cita
  que encerraba «(…)» en la negrita, partida en dos; y «conexión equipotencial local no conectada a
  tierra», puesta en el plural literal de la ITC-BT-24, 4.4.)
- `refutar_prosa.py`: 0 hallazgos.

## Fuentes releídas en esta fase

| Fuente | Fecha de lectura | Qué se comprobó |
|---|---|---|
| RD 842/2002 (BOE-A-2002-18099), volcado consolidado `fuentes/canal-sur/BOE-A-2002-18099.md` y `.redacciones.tsv` | 05-10-2026 | ITC-BT-01 (definiciones citadas); ITC-BT-03 apéndice I 2.1.2 (vig. 04-09-2025); ITC-BT-05 2.1, 3, 4.1, 4.2, 6.2 (vig. 30-06-2015); ITC-BT-08 entera; ITC-BT-18 entera (vig. 23-05-2010, BOE-A-2010-8190); ITC-BT-19 2.2.4, 2.3, 2.8, 2.9; ITC-BT-24 entera; ITC-BT-26 1 y 3; ITC-BT-27 2.2; ITC-BT-28 2.1; ITC-BT-38 2.1.3 |
| INSST, Guía técnica riesgo eléctrico, 4.ª ed. 2020 (`fuentes/canal-sur/tecnica/insst-guia-riesgo-electrico-2020.txt`) | 05-10-2026 | Tensiones de contacto y de paso y cuadros 5 y 6 (págs. 37-38) |

## Correcciones y decisiones (manda la fuente)

1. **«El TT es el esquema de las instalaciones alimentadas desde la red pública en España»** (RTVE
   teitse/03 § 4, sin fuente en RTVE; el tema 3 de Canal Sur la quitó por eso): **está en la
   fuente**, ITC-BT-08, 1.4 a). Se recupera con la cita literal (2.3).
2. **«El IT es el de los quirófanos»** (RTVE): la ITC-BT-38 no dice «IT»; exige transformador de
   aislamiento con vigilancia de aislamiento. Se dice así. Se añade la ITC-BT-28, 2.1, que sí
   prefiere el IT (sin corte al primer defecto) para servicios de seguridad.
3. **Ejemplos numéricos de RA** (tabla con 30 mA, 300 mA, 1 A): los mismos valores que el tema 3,
   3.4, ampliados con U = 24 V; declarados como aritmética.
4. **Erratas del BOE conservadas o señaladas**: «300 a 5.00» (tabla 3, césped; la guía del INSST da
   «300 a 500»), «mas seco» (ITC-BT-18, 12), «las corriente de fuga» (7), «no esta distribuido»
   (ITC-BT-24, 4.1.3). La frase del apartado 8 sobre los 2,5 mm² de cobre se cita tal cual y se avisa
   de que no dice en qué condición.
5. **Tabla 1 de la ITC-BT-18**: en el volcado, la fila «No protegido contra la corrosión» trae un
   solo par de valores (25 Cu / 50 Fe); se ponen en ambas columnas con nota.
6. **ITC-BT-18, 11**: remite a la MIE-RAT 13 de 1982, derogada por el RD 337/2014 (investigación
   § 6). Salvedad en 5.3. La fórmula de distancia en terreno mal conductor va en imagen en el BOE:
   no se da y se declara.
7. **ITC-BT-03, «Medidor de aislamiento, según ITC MIE-BT 19»**: referencia al reglamento anterior;
   se cita y se avisa.
8. **Tierras «limpias» o separadas para electrónica** (investigación § 9.9): sin norma leída. El tema
   lo dice y sólo da reglas de oficio subordinadas a la ITC-BT-18, 6.
9. **Distancias entre picas del telurómetro**: RTVE no las daba; tampoco el tema (sin fuente).
10. **ITC-BT-26**: su ámbito es de viviendas y, «en la medida que pueda afectarles», locales
    análogos; el tema lo cita con ese ámbito literal.

## Qué se quitó por propio de RTVE o por ser de otro tema

- Enunciado, ficha y referencias a la convocatoria 1/2022, a «esta ocupación», a la «pregunta 29
  del segundo cuadernillo» y a las respuestas oficiales (tese/15 § 4 y § 5); remisiones a los temas
  de RTVE, sustituidas por las de Canal Sur.
- teitse/09 § 1-3 (regímenes, inspecciones, defectos), § 6 y § 7 (mantenimiento y máquinas): temas
  2, 13 y 14. Quedan sólo los defectos graves de la ITC-BT-05, 6.2, que tocan la tierra.
- teitse/03 § 6, cita de envolventes: resumida en 6.1 con remisión al tema 3.
- tese/15 § 4, el análisis del condensador de filtrado y las opciones falsas: no es de instalación;
  quedan las dos filas de 50 y 100 Hz y el criterio bucle/fuente.
- Las negritas enfáticas y mayúsculas de RTVE: en Canal Sur la negrita sólo marca texto literal.

## Copiado del común

Ninguno. El temario común de Canal Sur (`temas/canal-sur-comun/`) no trata ninguna materia de este
tema, y no hay tema cerrado de Canal Sur del que copiar (AGRUPACION: 27·5 «nuevo»). Del tema 8 de
este mismo puesto (no cerrado) no se ha copiado texto; sólo se remite a él.

## Copiado de RTVE sin cambios

Ninguno. Los tres temas de origen están marcados **«actualizar: sí»** en la fila 27·5 de
`tecnica.tsv`, de modo que ningún pasaje entra en esta categoría: todo lo tomado de RTVE se lista
abajo como adaptado y debe verificarse.

**Tomado de RTVE, para verificar** (literal o casi, sin las negritas y mayúsculas enfáticas):

De `teitse/03-dispositivos-de-proteccion-y-maniobra.md`:
- § 4, tabla de la nomenclatura (sustituida por el texto literal de la ITC-BT-08) y tabla de los tres
  esquemas → 2.1 y 2.2 (resumen); párrafo del IT («el único esquema en el que un primer defecto no
  obliga a cortar») → 2.3, apoyado ahora en la ITC-BT-24, 4.1.3 y la ITC-BT-28, 2.1.
- § 5, cita de la ITC-BT-18, 2 (ampliada con su segundo párrafo); «Las cinco palabras que hay que
  subrayar…» y su razón → 1.1; tabla de partes → 1.2; párrafo de la resistencia y del valor no fijo
  → 5.1; párrafo de la equipotencialidad («todo suba a la vez») → 1.7.
- § 6, tabla de contactos directo/indirecto (con las definiciones literales de la ITC-BT-01 en lugar
  de las de RTVE) y MBTS → 6.1.

De `teitse/09-mantenimiento-medida-y-tomas-de-tierra.md`:
- § 4, aviso de seguridad previo a toda medida → 3.1.
- § 5 entero: qué se mide, método de cinco pasos (paso 1 con la cita de la ITC-BT-18, 3.3), zona de
  potencial nulo y su comprobación, los dos avisos (el primero ahora con la «resistencia global» de
  la ITC-BT-01; el segundo con la letra de la ITC-BT-18, 12 y 3.1), pinza de tierra y su límite, y
  la relación entre valor exigible y sensibilidad del diferencial → 3.2, 3.3 y 5.1. Quitado
  «el neutro de la distribuidora» del primer aviso (en TT no está unido al electrodo de las masas).

De `tese/15-mantenimiento-preventivo-y-correctivo.md`:
- § 4, dos filas del cuadro de frecuencias (50 y 100 Hz) y el matiz bucle/fuente → 7.2.

Lo demás (1.3 a 1.6, 1.7 salvo el párrafo dicho, 2.3 salvo el IT, 3.1 salvo el aviso, 3.4, 4 entero,
5.2 a 5.4, 6.2 a 6.4, 7.1, 7.3 y los tres bloques finales) es redacción nueva sobre el BOE y la guía.

## Preguntas tipo test de comprobación (10)

Respuesta correcta en negrita; a la derecha, dónde la contesta el tema. Repartidas por las siete
rúbricas, con teoría y aplicación práctica. Las diez se contestan enteras con el tema; no ha hecho
falta ampliar (las lagunas que salieron al escribirlas —los defectos graves de la ITC-BT-05 que
tocan la tierra y el apartado 2.1 de la ITC-BT-28— se cubrieron antes de cerrar, en 4.1 y 2.3).

1. (Puesta a tierra, teoría) Según la ITC-BT-18, la puesta a tierra es la unión eléctrica directa de
   una parte del circuito o de una parte conductora con el terreno: a) a través de un interruptor
   diferencial; b) protegida por fusible para evitar sobrecargas; **c) sin fusibles ni protección
   alguna**; d) a través de una impedancia limitadora. — Epígrafe 1.1.
2. (Componentes, teoría) La profundidad de enterramiento de una toma de tierra nunca será inferior
   a: a) 0,30 m; **b) 0,50 m**; c) 0,80 m; d) 1 m. Y un conductor de tierra de cobre enterrado sin
   protección contra la corrosión tendrá como mínimo: **25 mm²**. Y el conductor de protección de
   una línea de fase de 50 mm² del mismo material: **25 mm² (S/2)**. — Epígrafes 1.3 y 1.4.
3. (Equipotencialidad y CPN, teoría) El conductor principal de equipotencialidad tendrá una sección
   no inferior a: **a) la mitad de la del conductor de protección de sección mayor de la instalación,
   con un mínimo de 6 mm²**; b) la del conductor de fase mayor; c) 16 mm² siempre; d) 1,5 mm². Y si
   neutro y protección se han separado en un punto de la instalación: **no está permitido volver a
   unirlos aguas abajo**. — Epígrafes 1.7 y 1.5.
4. (Esquemas, teoría) En el código de esquemas de la ITC-BT-08, la segunda letra «T» significa:
   a) neutro y protección separados; **b) masas conectadas directamente a tierra, independientemente
   de la eventual puesta a tierra de la alimentación**; c) alimentación aislada de tierra; d) masas
   unidas al neutro. Y una instalación receptora alimentada directamente de la red de distribución
   pública de baja tensión tiene esquema: **TT**. — Epígrafes 2.1 y 2.3.
5. (Mediciones, práctica) Al medir la resistencia de una toma de tierra con telurómetro y dos picas
   auxiliares, la medida es válida si: a) la pica de tensión está junto al electrodo; **b) al
   desplazar la pica de tensión la lectura se mantiene, porque está en la zona de potencial nulo**;
   c) se mide sin separar el electrodo para incluir todas las tierras; d) se mide tras una lluvia.
   Y el dispositivo que permite separar el electrodo para medir debe ser: **desmontable
   necesariamente por medio de un útil**. — Epígrafes 3.2 y 1.4.
6. (Continuidad, teoría) Según la ITC-BT-05, la falta de continuidad de los conductores de
   protección se clasifica como defecto: a) leve; **b) grave**; c) muy grave; d) no es defecto si
   hay diferencial. Y en el conductor de protección: **ningún aparato deberá ser intercalado**. —
   Epígrafe 4.1.
7. (Resistencia de tierra, práctica) En esquema TT, con tensión de contacto límite de 50 V y un
   diferencial de 300 mA, la resistencia máxima RA es de unos 167 Ω. Una pica vertical de 2 m en un
   terreno de 500 Ω·m da, según la tabla 5 de la ITC-BT-18: a) 1.000 Ω; **b) 250 Ω, que no cumple**;
   c) 125 Ω, que cumple; d) 25 Ω. — Epígrafes 5.1 y 5.2.
8. (Revisión e independencia, teoría) La comprobación de la puesta a tierra por personal
   técnicamente competente se hará: a) cada cinco años en invierno; **b) al menos anualmente, en la
   época en la que el terreno esté más seco**; c) sólo en la inspección del organismo de control;
   d) cada diez años. Y una toma de tierra es independiente de otra cuando no alcanza respecto a un
   punto de potencial cero una tensión superior a: **50 V** con la máxima corriente de defecto por
   la otra. — Epígrafes 5.4 y 5.3.
9. (Protección de personas, teoría y práctica) En un esquema TN con U0 = 230 V, el tiempo máximo
   de interrupción es: a) 0,1 s; b) 0,2 s; **c) 0,4 s**; d) 5 s. En un esquema TN-C los
   diferenciales: **no podrán utilizarse**. Y en un local no conductor (ITC-BT-24, 4.3): **no debe
   estar previsto ningún conductor de protección**. — Epígrafes 6.2 y 6.3.
10. (Equipos sensibles, teoría y práctica) Cuando una puesta a tierra es necesaria a la vez por
    razones de protección y funcionales: a) prevalece la funcional en salas técnicas; **b)
    prevalecen las prescripciones de las medidas de protección**; c) deben ir a tomas de tierra
    separadas; d) decide el fabricante del equipo. Y en un control aparece un zumbido de 50 Hz que
    cambia al mover los cables de señal: lo más probable es **un bucle de masa (tierra)**, y lo que
    nunca se hace es **cortar el conductor de protección del equipo**. — Epígrafes 7.1, 7.2 y 7.3.
