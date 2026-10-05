# Puesto 27 · Oficial Técnico Electricista · Investigación del bloque A-eléctrico (temas 1, 2, 3, 4, 5, 14 y 15)

Fase 1 · Investigar. Fecha de lectura de todas las fuentes: **05-10-2026** (el encargo fija como «hoy» el
24-09-2026; los volcados se hicieron el 05-10-2026 y el BOE no muestra ninguna redacción con vigencia entre
ambas fechas en las normas usadas). Sólo se investiga lo que el material de RTVE localizado no cubre o lo que ha
cambiado desde su fecha (21-12-2022). Lo de RTVE lo lee el redactor; aquí no se repite.

## 0. Fuentes leídas y ficheros tocados

| Fuente | Identificador / ubicación | Leída |
|---|---|---|
| Real Decreto 842/2002, de 2 de agosto, Reglamento electrotécnico para baja tensión (REBT) e ITC-BT | `BOE-A-2002-18099`, volcado nuevo en `fuentes/canal-sur/BOE-A-2002-18099.md` (+ `.redacciones.tsv`), redacción vigente hoy | 05-10-2026 |
| BOE, análisis de la norma (referencias posteriores) y metadatos de consolidación del REBT | API datos abiertos BOE | 05-10-2026 |
| Real Decreto 614/2001, de 8 de junio, riesgo eléctrico | `BOE-A-2001-11881`, volcado ya existente en `fuentes/canal-sur/` (25-09-2026) | 05-10-2026 |
| Real Decreto 337/2014 (RAT), disposición derogatoria | `fuentes/corte-20221221/BOE-A-2014-6084.md` | 05-10-2026 |
| INSST, *Guía técnica para la evaluación y prevención del riesgo eléctrico*, 4.ª ed., Madrid, septiembre 2020, «actualizada a fecha de julio 2020», NIPO en línea 118-20-047-X | `fuentes/canal-sur/tecnica/insst-guia-riesgo-electrico-2020.pdf` y `.txt` (descargada de insst.es) | 05-10-2026 |
| Decreto 59/2005, de 1 de marzo (Andalucía), texto consolidado de la Junta (versión de 17-02-2024, BOJA núm. 34 de 16-2-2024) | `fuentes/canal-sur/tecnica/boja-decreto-59-2005-consolidado.txt` | 05-10-2026 |
| Títulos de BOE-A-2025-17507, BOE-A-2025-6773, BOE-A-2022-9848, BOE-A-2023-7056, BOE-A-2021-6879 | `boe.es/diario_boe/xml.php` y API | 05-10-2026 |
| Presentación COGITI «Novedades REBT 2026» (22-04-2026), sólo para saber qué NO es vigente | cogiti.es (no guardada en fuentes) | 05-10-2026 |

**Ficheros creados o tocados** (además de este informe): `fuentes/canal-sur/BOE-A-2002-18099.md` y
`.redacciones.tsv` (volcado nuevo con `boe.py norma`); carpeta nueva `fuentes/canal-sur/tecnica/` con los dos
documentos citados. No he tocado temas.

## 1. Lo transversal: qué ha cambiado en el REBT desde el 21-12-2022

Diff de la cadena de redacciones (`fuentes/corte-20221221/…redacciones.tsv` frente al volcado de hoy):
**sólo cambian tres bloques**; el resto del articulado y las ITC-BT 01 y 04 a 52 tienen hoy la misma redacción
que el 21-12-2022.

| Bloque | Redacción a 21-12-2022 | Redacción vigente hoy | Norma |
|---|---|---|---|
| Artículo 25 | Original (2002) | Vigencia **01-07-2023** | **Real Decreto 145/2023, de 28 de febrero**, «por el que se modifican diversas normas reglamentarias en materia de seguridad industrial para su adaptación al principio de reconocimiento mutuo» (`BOE-A-2023-7056`) |
| ITC-BT-02 | Listado de 2020 (Resolución de 9-1-2020, `BOE-A-2020-612`) | Vigencia **04-04-2025** | **Resolución de 20 de marzo de 2025, de la Dirección General de Estrategia Industrial y de la Pequeña y Mediana Empresa**, «por la que se actualiza el listado de normas de la instrucción técnica complementaria ITC BT-02» (`BOE-A-2025-6773`) |
| ITC-BT-03 | Redacción de RD 298/2021 | Vigencia **04-09-2025** | **Real Decreto 770/2025, de 2 de septiembre**, «por el que se modifican diversas normas reglamentarias en materia de seguridad industrial en lo relativo al régimen de contratación de los profesionales habilitados» (`BOE-A-2025-17507`); el BOE lo describe como «SE MODIFICA el apéndice I.1 de la ITC-BT-03» |

Lista completa de reformas que el BOE asocia al REBT (análisis, «referencias posteriores»), por si el tema 2
quiere la historia: RD 560/2010 (art. 22, ITC-BT-03, DA 1.ª a 4.ª), RD 1053/2014 («SE MODIFICA, con efectos de
30 de junio de 2015, las ITC BT-02, BT-04, BT-05, BT-10, BT-16 y BT-25, y SE AÑADE la BT-52»), RD 244/2019
(«SE DEROGA, y SE MODIFICA lo indicado de la ITC-BT-40»), Resolución de 9-1-2020 (ITC-BT-02), RD 542/2020
(«el art. 14, la ITC-BT-04 y … la ITC-BT-52»), RD 298/2021 («el art. 2.2 y la ITC-BT-03»), RD 450/2022
(«la ITC BT-52»), RD 145/2023 (art. 25), Resolución de 20-3-2025 (ITC-BT-02), RD 770/2025 (apéndice I.1 de la
ITC-BT-03); y la Sentencia del TS de 17-2-2004 («SE DECLARA la nulidad del inciso 4.2.c.2 de la ITC BT-03»).
Nota del BOE en la ITC-BT-40: «**Se derogan el apartado 4.3.3 y el tercer párrafo del apartado 7 y se modifican
el apartado 2.c), el apartado 4.3, el apartado 7 y se añade un anexo por la disposición derogatoria única.b) y la
disposición final 2 del Real Decreto 244/2019, de 5 de abril**».

**No hay reforma de 2026.** Metadatos del BOE: consolidación «Finalizado», última actualización
**18-12-2025**; ninguna referencia posterior a RD 770/2025. Una presentación de COGITI (22-04-2026) anuncia un
«nuevo REBT» con prohibición de diferenciales tipo AC, protección contra sobretensiones obligatoria en todas las
instalaciones nuevas y una nueva ITC-BT-53 de corriente continua, pero lo presenta como futuro: «**Fecha
estimada: Publicación del nuevo REBT en 2026 (probable primera mitad)**». **No consta publicado en el BOE: no se
estudia como vigente** (si el redactor lo menciona, como proyecto y sin cifras).

Consecuencia para lo copiado de RTVE: **todos los preceptos que citan los temas teitse/01, 03, 04, 05, 07, 09,
13 y 15 siguen en la misma redacción**, salvo lo que esos temas digan del **artículo 25**, de la **ITC-BT-02**
(su fecha y ediciones) y del **apéndice I de la ITC-BT-03**. Y la ficha «Redacción que se estudia» debe pasar
a «la vigente el 05-10-2026 (última actualización del texto consolidado: 18-12-2025)».

## 2. Tema 1 · Magnitudes, alterna, potencia, energía, factor de potencia, caída de tensión, equilibrado de cargas

RTVE cubre magnitudes, CA, trifásica, potencias, cos φ y caída de tensión (art. 4 REBT e ITC-BT-19 2.2.2, sin
cambios). Falta, con norma:

### 2.1 Equilibrado de cargas (lo que RTVE da «de pasada»)

- REBT, **artículo 16.2** (una redacción, 2002): «**En toda instalación interior o receptora que se proyecte y
  realice se alcanzará el máximo equilibrio en las cargas que soportan los distintos conductores que forman parte
  de la misma, y ésta se subdividirá deforma que las perturbaciones originadas por las averías que pudieran
  producirse en algún punto de ella afecten a una mínima parte de la instalación.**» (sic «deforma»).
- **ITC-BT-19, apartado 2.5 «Equilibrado de cargas»**: «**Para que se mantenga el mayor equilibrio posible en la
  carga de los conductores que forman parte de una instalación, se procurará que aquella quede repartida entre
  sus fases o conductores polares.**»
- **ITC-BT-19, 2.2.2, último párrafo** (neutro): «**En instalaciones interiores, para tener en cuenta las
  corrientes armónicas debidas cargas no lineales y posibles desequilibrios, salvo justificación por cálculo, la
  sección del conductor neutro será como mínimo igual a la de las fases.**» (sic «debidas cargas»).
- **ITC-BT-43, apartado 2.6** («Utilización de receptores que desequilibren las fases…»): «**No se podrán
  instalar sin consentimiento expreso de la Empresa que suministra la energí a, aparatos receptores que produzcan
  desequilibrios importantes en las distribuciones polifásicas.**» (sic «energí a»).
- Ejemplo reglamentario de reparto entre fases: ITC-BT-52 («**Cuando en un circuito trifásico se conecten
  estaciones monofásicas, éstas se repartirán de la forma más equilibrada posible entre las tres fases.**»).

### 2.2 Factor de potencia: lo que fija el REBT

- **ITC-BT-43, apartado 2.7 «Compensación del factor de potencia»**: «**Las instalaciones que suministren energía
  a receptores de los que resulte un factor de potencia inferior a 1, podrán ser compensadas, pero sin que en
  ningún momento la energía absorbida por la red pueda ser capacitiva.**» Dos formas: «**Por cada receptor o
  grupo de receptores que funcionen simultáneamente y se conecten por medio de un sólo interruptor**» (el
  interruptor corta a la vez receptor y condensador) o «**Para la totalidad de la instalación. En este caso, la
  instalación de compensación ha de estar dispuesta para que, de forma automática, asegure que la variación del
  factor de potencia no sea mayor de un ± 10 % del valor medio obtenido durante un prolongado período de
  funcionamiento.**» Además: «**Cuando se instalen condensadores y la conexión de éstos con los receptores pueda
  ser cortada por medio de interruptores, los condensadores irán provistos de resistencias o reactancias de
  descarga a tierra.**» y, en motores asíncronos, condensadores desconectados a la vez que el motor. Normas:
  «**UNE-EN 60831-1 y UNE-EN 60831-2**».
- **ITC-BT-44** (lámparas de descarga): «**será obligatoria la compensación del factor de potencia hasta un valor
  mínimo de 0,9**», y condensadores del equipo auxiliar con resistencia que asegure «**no sea mayor de 50 V
  transcurridos 60 s**» (leer la frase entera en la ITC antes de citarla).
- **ITC-BT-44**: «**Para receptores con lámparas de descarga, la carga mínima prevista en voltiamperios será de 1,8
  veces la potencia en vatios de las lámparas.**»
- **ITC-BT-09** (alumbrado exterior), por si sirve de ejemplo: «**el factor de potencia de cada punto de luz,
  deberá corregirse hasta un valor mayor o igual a 0,90. La máxima caída de tensión entre el origen de la
  instalación y cualquier otro punto de la instalación, será menor o igual que 3%.**»

### 2.3 No confirmado

- La penalización por energía reactiva en la factura (umbral de cos φ) es de la normativa de peajes de la CNMC, no
  del REBT; no la he leído. **Quitar si aparece en RTVE con cifra.**

## 3. Tema 2 · REBT e ITC: documentación, puesta en servicio, verificaciones, inspecciones y mantenimiento

RTVE (teitse/15, 09 y 13) cubre objeto, campo, mapa de las 52 ITC, artículos 18 a 21, ITC-BT-04 y ITC-BT-05.
**Todo eso sigue vigente** (art. 18 y 20: redacción de RD 560/2010; art. 21 y 23: originales; ITC-BT-04:
RD 542/2020; ITC-BT-05: RD 1053/2014). Añadir o corregir:

### 3.1 Artículos 18, 20 y 21 en su letra vigente (para quien redacte desde cero)

- **Art. 18.1**: el procedimiento de puesta en servicio en cinco letras: a) documentación técnica previa,
  «**proyecto o memoria técnica**» según la ITC; b) verificación «**por el instalador, con la supervisión del
  director de obra, en su caso**»; c) inspección inicial por organismo de control «**cuando así se determine en
  la correspondiente ITC**»; d) **certificado de instalación** de la empresa instaladora; e) depósito «**ante el
  órgano competente de la Comunidad Autónoma, con objeto de registrar la referida instalación**». **18.2**:
  «**Las instalaciones eléctricas deberán ser realizadas únicamente por empresas instaladoras.**» **18.3**: la
  distribuidora no conecta sin la copia del certificado diligenciado. **18.4**: suministro provisional por
  resolución motivada. **18.5**: instalaciones temporales (tramitación conjunta).
- **Art. 20** (mantenimiento): «**Los titulares de las instalaciones deberán mantener en buen estado de
  funcionamiento sus instalaciones, utilizándolas de acuerdo con sus características y absteniéndose de
  intervenir en las mismas para modificarlas. Si son necesarias modificaciones, éstas deberán ser efectuadas por
  una empresa instaladora.**»
- **Art. 21** (inspecciones): la ITC determinará a) inspección inicial, b) periódica, c) criterios de valoración y
  medidas, d) plazos.
- **Art. 22.1**: empresas instaladoras son las que «**hayan presentado la declaración responsable de inicio de
  actividad**»; **22.2**: la declaración «**habilita por tiempo indefinido … para el ejercicio de la actividad en
  todo el territorio español**».

### 3.2 ITC-BT-05 vigente (RD 1053/2014), lo que RTVE no copia

- **Apartado 3**: «**Las instalaciones eléctricas en baja tensión deberán ser verificadas, previamente a su puesta
  en servicio y según corresponda en función de sus características, siguiendo la metodología de la norma UNE
  20.460 -6-61.**»
- **Apartado 2.1**: «**Las verificaciones previas a la puesta en servicio de las instalaciones deberán ser
  realizadas por las empresas instaladoras que las ejecuten.**» **2.2**: organismos de control «**según lo
  establecido en el Real Decreto 2.200/1995, de 28 de diciembre**».
- **Apartado 4.1** lista **ocho** letras a) a h) (h: «**Instalaciones de las estaciones de recarga para el vehículo
  eléctrico, que requieran la elaboración de proyecto para su ejecución.**»). Comprobar que la copia de RTVE trae
  las ocho.
- **Apartado 5**: certificado de inspección; calificaciones **favorable / condicionada / negativa**; en
  condicionada, instalaciones en servicio: plazo «**que no podrá superar los 6 meses**»; en negativa, certificado
  «**que se remitirá inmediatamente al Órgano competente de la Comunidad Autónoma**».
- **Apartado 6**: defectos muy graves, graves (lista de 16 guiones, entre ellos «**Valores elevados de resistencia
  de tierra en relación con las medidas de seguridad adoptadas.**», «**Falta de identificación de los conductores
  "neutro" y "de protección"**», «**Ampliaciones o modificaciones de una instalación que no se hubieran tramitado
  según lo establecido en la ITC -BT 04.**», «**La sucesiva reiteración o acumulación de defectos leves.**») y
  leves.
- **Salvedad de texto (error 1 en la propia fuente)**: la ITC-BT-05 2.2 dice «**De acuerdo con lo indicado en el
  artículo 20 del Reglamento**» para las inspecciones, y el apartado 1 dice que desarrolla «**los artículos 18 y
  20**»; hoy el art. 20 es mantenimiento y las inspecciones están en el **art. 21**. Se cita literal, sin
  corregir, avisando.

### 3.3 Mantenimiento: obligaciones de la empresa instaladora (ITC-BT-03 vigente)

- ITC-BT-03 apartado 7 (obligaciones), letras h) a j) leídas: «**h) Mantener al día un registro de las
  instalaciones ejecutadas o mantenidas.**», «**i) Informar a la Administración competente sobre los accidentes
  ocurridos en las instalaciones a su cargo.**», «**j) Conservar a disposición de la Administración, copia de los
  contratos de mantenimiento al menos durante los 5 años inmediatos posteriores a la finalización de los
  mismos.**» (las letras a) a g) no las he copiado: leerlas en el volcado antes de usarlas).
- **Categorías** (3.1 IBTB básica y 3.2 IBTE especialista, con sus nueve modalidades de especialista, entre ellas
  «**Sistemas de supervisión, control y adquisición de datos**» e «**Instalaciones generadoras de baja tensión de
  potencia superior o igual a 10 kW**»). Sin cambios en 2025.
- **Lo que cambió el RD 770/2025 (apéndice I.1, medios humanos)**. Hoy: «**Contar con el personal contratado
  necesario para realizar la actividad en condiciones de seguridad, en número suficiente y durante el tiempo
  necesario para atender las instalaciones que tengan contratadas, con un mínimo de una persona instaladora en
  baja tensión de la misma categoría en la que la empresa se encuentra habilitada. / Se entenderá satisfecho el
  requisito del párrafo anterior cuando el referido personal necesario para realizar la actividad esté contratado
  a través de cualquiera de las modalidades contractuales permitidas en derecho.**» Antes (redacción de 2021)
  exigía instalador «**contratado en plantilla a jornada completa**» con excepciones para socios y autónomos.
  **Si RTVE o cualquier copia habla de «plantilla a jornada completa», es redacción derogada (error 7).**

### 3.4 ITC-BT-02 (listado de normas) vigente

- Encabezado: «**Listado de normas de ITC BT-02, actualizado por Resolución de 20 de marzo de 2025, de la
  Dirección General de Estrategia Industrial y de la Pequeña y Mediana Empresa, que, de acuerdo con el artículo
  26 del Reglamento … se considera que cumplen las condiciones reglamentarias**».
- Nota (*): aplicabilidad de las nuevas ediciones «**el día siguiente de la publicación de la Resolución de 20 de
  marzo de 2025**»; nota (**): «**Fecha final de coexistencia con las normas o ediciones anteriores: 1 de octubre
  de 2025, salvo cuando haya un periodo más prolongado indicado explícitamente para cada norma**».
- Normas útiles para los temas 2 a 5 y 14 que el listado recoge hoy (edición entre paréntesis): **UNE-HD 60364-6**
  «Parte 6: Verificación» (2017, A11 y A12 2018); **UNE-HD 60364-4-41** choques eléctricos (2018, A11 2018,
  A12 2019); **UNE-HD 60364-4-43** sobreintensidades (2024); **UNE-HD 60364-4-443** sobretensiones de origen
  atmosférico o por maniobra (2016); **UNE-HD 60364-5-52** canalizaciones (2022, A12 2023); **UNE-HD 60364-5-54**
  puesta a tierra y conductores de protección (2015, A11 2018, A1 2023); **UNE-EN 60898-1** (2020) y **-2**
  (2022) automáticos; **UNE-EN 60947-2** (2018, A1 2020); **UNE-EN 61008-1** y **61009-1** (2013 y modif.)
  diferenciales; **UNE-EN 60269-1** y **UNE-HD 60269-2/-3** fusibles; **UNE-EN 61643-11** (2013, A11 2018) DPS;
  **UNE-EN 61557-8** (2016) vigilantes de aislamiento IT y **-9** localizadores de fallo; **UNE-EN 50575**
  (2015, A1 2016) cables y reacción al fuego; **UNE-IEC 60479-1** (2022) efectos de la corriente.
- **Cautela**: las notas de correspondencia del listado sólo dicen qué norma sustituye a qué en 25 casos
  (p. ej. «**(23) La referencia original en el texto reglamentario es UNE 20460-3.**», «**(25) … UNE 20572-1.**»).
  **No hay nota que diga que UNE-HD 60364-6 sustituye a la UNE 20.460-6-61 que cita la ITC-BT-05**, ni que
  UNE-HD 60364-5-52 sustituya a la UNE 20.460-5-523 de la ITC-BT-19. No afirmarlo.

### 3.5 Puesta en servicio en Andalucía (lo autonómico)

- **Decreto 59/2005, de 1 de marzo**, art. 5.1 (redacción de Decreto 9/2011, vigencia 3-2-2011): las
  instalaciones del **Grupo II** (no sometidas a autorización) requieren «**únicamente para su puesta en
  funcionamiento la presentación por el interesado ante el órgano competente de una comunicación, acompañada de
  la documentación que reglamentariamente se determine, en la que declara bajo su responsabilidad que cumple con
  los requisitos exigidos**»; y «**La presentación de la comunicación y documentación indicada anteriormente no
  supondrá, en ningún caso, la conformidad técnica a la misma por el órgano competente.**» Art. 5.3: una Orden de
  la Consejería desarrolla documentación y forma de presentación.
- Esa Orden es la **Orden de 5 de marzo de 2013** (título leído en el BOJA, `juntadeandalucia.es/boja/2013/48/1`),
  con Anexo II modificado por Resoluciones de 8-10-2019, 28-9-2023 y 23-3-2026 (títulos leídos en resultados del
  BOJA). **No he leído su articulado**: hueco declarado; el tema puede nombrarla, no desarrollarla.

## 4. Tema 3 · Cuadros, aparamenta y protecciones

RTVE (teitse/03 y 04) cubre magnetotérmico, diferencial, fusibles, maniobra, automatismos y selectividad; nombra
la ITC-BT-23 sin citarla. Falta:

### 4.1 Cuadros: ITC-BT-17 (una redacción, 2002)

- 1.1: «**La altura a la cual se situarán los dispositivos generales e individuales de mando y protección de los
  circuitos, medida desde el nivel del suelo, estará comprendida entre 1,4 y 2 m, para viviendas. En locales
  comerciales, la altura mínima será de 1 m desde el nivel del suelo.**»; en pública concurrencia «**no sean
  accesibles al público en general**».
- 1.2: envolventes «**con un grado de protección mínimo IP 30 según UNE 20.324 e IK07 según UNE-EN 50.102**»;
  posición de servicio «**vertical**»; composición mínima: IGA omnipolar con protección contra sobrecargas y
  cortocircuitos, «**independiente del interruptor de control de potencia**»; diferencial general (salvo otra
  protección según ITC-BT-24); dispositivos de corte omnipolar por circuito; «**Dispositivo de protección contra
  sobretensiones, según ITC-BT-23, si fuese necesario.**» Y: «**En el caso de que se instale más de un interruptor
  diferencial en serie, existirá una selectividad entre ellos.**»
- 1.3: IGA con poder de corte «**de 4.500 A como mínimo**»; demás automáticos y diferenciales «**deberán resistir
  las corrientes de cortocircuito que puedan presentarse en el punto de su instalación**».
- ITC-BT-24 4.1.1 (selectividad diferencial): «**Con miras a la selectividad pueden instalarse dispositivos de
  corriente diferencial-residual temporizada (por ejemplo del tipo «S») en serie con dispositivos de protección
  diferencial-residual de tipo general.**»

### 4.2 Sobretensiones: ITC-BT-23 (una redacción, 2002)

- 1: trata «**sobretensiones transitorias que se transmiten por las redes de distribución y que se originan,
  fundamentalmente, como consecuencia de las descargas atmosféricas, conmutaciones de redes y defectos en las
  mismas**»; no contempla «**la protección de señales de medida, control y telecomunicación**».
- 2.1: protección en cascada con «**tres niveles de protección: basta, media y fina**».
- 2.2 categorías: **I** «**equipos muy sensibles … Ejemplo: ordenadores, equipos electrónicos muy sensibles**»;
  **II** «**electrodomésticos, herramientas portátiles**»; **III** «**armarios de distribución, embarrados,
  aparamenta … canalizaciones … motores con conexión eléctrica fija**»; **IV** «**en el origen o muy próximos al
  origen de la instalación, aguas arriba del cuadro de distribución. Ejemplo: contadores de energía, aparatos de
  telemedida, equipos principales de protección contra sobreintensidades**».
- Tabla 1 (tensión soportada a impulsos 1,2/50, kV): **230/400 trifásica y 230 monofásica: IV 6 · III 4 · II 2,5 ·
  I 1,5**; **400/690 y 1000 trifásica: 8 · 6 · 4 · 2,5**.
- 3: la ITC **no trata la descarga directa del rayo** («**Esta instrucción no trata este caso**»). 3.1 situación
  natural: alimentación «**por una red subterránea en su totalidad**» → no hace falta protección suplementaria;
  línea aérea con conductores aislados con pantalla a tierra en los dos extremos «**se considera equivalente a una
  línea subterránea**». 3.2 situación controlada: alimentación por línea aérea con conductores desnudos o aislados
  → «**se considera necesaria una protección contra sobretensiones de origen atmosférico en el origen de la
  instalación**»; también lo es la situación natural en que convenga proteger «**(por ejemplo, continuidad de
  servicio, valor económico de los equipos, pérdidas irreparables, etc.)**» (argumento directo para un centro de
  producción). Nivel de protección del DPS «**inferior a la tensión soportada a impulso de la categoría de los
  equipos**». Conexión: «**En redes TT o IT, los descargadores se conectarán entre cada uno de los conductores,
  incluyendo el neutro o compensador y la tierra de la instalación. En redes TN-S … entre cada uno de los
  conductores de fase y el conductor de protección. En redes TN-C … entre cada uno de los conductores de fase y el
  neutro o compensador.**»

### 4.3 Sobrecargas: lo que dice y lo que NO dice la ITC-BT-22

- 1.1 a): «**El límite de intensidad de corriente admisible en un conductor ha de quedar en todo caso garantizada
  por el dispositivo de protección utilizado.**» y remite a «**La norma UNE 20.460-4-43**».
- **No confirmado en el REBT**: las condiciones Ib ≤ In ≤ Iz e I2 ≤ 1,45·Iz **no están en el texto de la ITC-BT-22**
  (búsqueda de «1,45» e «Iz» sin resultado); son de la norma UNE, que no he leído. Si RTVE las trae, citarlas
  como de la norma UNE (no del REBT) o quitarlas.

## 5. Tema 4 · Canalizaciones, conductores y cableado

RTVE (teitse/04, 05, 07) cubre designación, canalizaciones, cálculo de secciones, IP y sala audiovisual, pero
declara que «**El temario no da las temperaturas exactas**». Aquí están:

- **Temperaturas de aislamiento** (ITC-BT-07, leyenda de tablas): «**XLPE - Polietileno reticulado. Temperatura
  máxima en el conductor 90 ºC (servicio permanente).**», «**EPR - Etileno propileno. Temperatura máxima en el
  conductor 90 ºC (servicio permanente).**», «**PVC - Policloruro de vinilo. Temperatura máxima en el conductor
  70 ºC (servicio permanente).**» (ITC-BT-07 es de redes subterráneas; la cifra es propiedad del aislamiento).
- **ITC-BT-19 2.2.3**: intensidades admisibles «**se regirán en su totalidad por lo indicado en la Norma UNE
  20.460-5-523 y su anexo Nacional**»; la tabla de la ITC es «**para una temperatura ambiente del aire de 40 ºC**».
- **Identificación (ITC-BT-19 2.2.4)**: «**Cuando exista conductor neutro en la instalación o se prevea para un
  conductor de fase su pase posterior a conductor neutro, se identificarán éstos por el color azul claro. Al
  conductor de protección se le identificará por el color verde-amarillo. Todos los conductores de fase, o en su
  caso, aquellos para los que no se prevea su pase posterior a neutro, se identificarán por los colores marrón o
  negro. / Cuando se considere necesario identificar tres fases diferentes, se utilizará también el color gris.**»
- **Conductores de protección (ITC-BT-19 2.3, tabla 2)**: S ≤ 16 → S (*); 16 < S ≤ 35 → 16; S > 35 → S/2; (*) con
  mínimo «**2,5 mm2 si los conductores de protección no forman parte de la canalización de alimentación y tienen
  una protección mecánica**» / «**4 mm2 si … no tienen una protección mecánica**». «**No se utilizará un conductor
  de protección común para instalaciones de tensiones nominales diferentes.**»
- **ITC-BT-20 2.1.1**: separación con canalizaciones no eléctricas «**una distancia mínima de 3 cm**»; no situarlas
  bajo canalizaciones que condensen; condiciones para compartir canal o hueco (lista a) y b)). **2.1.2**
  accesibilidad; **2.1.3** identificación: «**Cuando la identificación pueda resultar difícil, debe establecerse
  un plano de la instalación que permita, en todo momento, esta identificación mediante etiquetas o señales de
  aviso indelebles y legibles.**»
- **Bandejas (ITC-BT-20 2.2.9)**: «**Sólo se utilizarán conductores aislados con cubierta (incluidos cables
  armados o con aislamiento mineral), unipolares o multipolares según norma UNE 20.460-5-52.**»
- **Pública concurrencia (ITC-BT-28, apartado 4, letra f)**: cables «**no propagadores del incendio y con emisión
  de humos y opacidad reducida. Los cables con características equivalentes a las de la norma UNE 21.123 parte 4 ó
  5; o a la norma UNE 21.1002 (según la tensión asignada del cable), cumplen con esta prescripción.**»; para
  servicios de seguridad no autónomos, cables que «**deben mantener el servicio durante y después del incendio,
  siendo conformes a las especificaciones de la norma UNE-EN 50.200**». Letra e): conductores «**de tensión
  asignada no inferior a 450/750 V**» bajo tubo o canal, o 0,6/1 kV armados sobre pared. **No he encontrado
  «televisión» ni «radio» en el campo de aplicación de la ITC-BT-28**: que un estudio o plató sea pública
  concurrencia no lo dice la ITC por su nombre (aplicar por el aforo/uso; no afirmar).
- **Conexiones**: ITC-BT-19 2.11 ya en RTVE (teitse/07).
- **Reacción al fuego (CPR)**: el listado ITC-BT-02 recoge «**UNE-EN 50575. Cables de energía, control y
  comunicación. Cables para aplicaciones generales en construcciones sujetos a requisitos de reacción al
  fuego.**» (2015, A1 2016). **No he leído** clases (Cca-s1b,d1,a1, etc.) en ninguna fuente: no darlas.
- **No confirmado**: el criterio de cortocircuito (sección por I²t) y las caídas de tensión de la derivación
  individual o LGA (ITC-BT-14/15) no los he leído; si RTVE los trae, el verificador los relee.

## 6. Tema 5 · Puestas a tierra y equipotencialidad

RTVE cubre esquemas, contactos, telurómetro, época seca y zumbido por lazos. Falta la letra de la ITC-BT-18 e
ITC-BT-24 (ambas: la ITC-BT-18 con redacción de RD 560/2010, vigencia 23-5-2010; la ITC-BT-24 original).

- **ITC-BT-18 2** (definición): unión «**directa, sin fusibles ni protección alguna**».
- **ITC-BT-18 3.2, tabla 1** (conductores de tierra enterrados): protegido contra corrosión y mecánicamente →
  «**Según apartado 3.4**»; protegido contra corrosión, no mecánicamente → «**16 mm2 Cobre / 16 mm2 Acero
  Galvanizado**»; no protegido contra corrosión → «**25 mm2 Cobre / 50 mm2 Hierro**».
- **5** tierra funcional: «**deben ser realizadas de forma que aseguren el funcionamiento correcto del equipo**».
  **6**: «**Cuando la puesta a tierra sea necesaria a la vez por razones de protección y funcionales,
  prevalecerán las prescripciones de las medidas de protección.**» (clave para «compatibilidad con equipos
  sensibles»: la tierra funcional del equipo no puede sacrificar la de protección).
- **7** CPN/PEN: sección mínima 10 mm² Cu o Al; no en parte protegida por diferencial; «**Si a partir de un punto
  cualquiera de la instalación, el conductor neutro y el conductor de protección están separados, no estará
  permitido conectarlos entre sí en la continuación del circuito por detrás de este punto.**»
- **8** equipotencialidad: principal «**no inferior a la mitad de la del conductor de protección de sección mayor
  de la instalación, con un mínimo de 6 mm2. Sin embargo, su sección puede ser reducida a 2,5 mm2, si es de
  cobre.**» (sic, tal cual); suplementaria masa-elemento conductor ≥ mitad del de protección de esa masa.
- **9** resistencia: tensiones de contacto no superiores a «**24 V en local o emplazamiento conductor**» y «**50 V
  en los demás casos**». Tabla 5: placa «**R = 0,8 ρ/P**», pica «**R = ρ/L**», conductor horizontal
  «**R = 2 ρ/L**». Tablas 3 y 4 (resistividades) «**a título de orientación**».
- **10** tierras independientes: cuando una no alcanza «**una tensión superior a 50 V cuando por la otra circula
  la máxima corriente de defecto a tierra prevista**».
- **11** separación de la tierra del centro de transformación: distancia «**al menos igual a 15 metros para
  terrenos cuya resistividad no sea elevada (<100 ohmios.m)**». **Salvedad**: el apartado remite al «**punto 1.1
  de la MIE-RAT 13**» del reglamento de 1982, que **está derogado** por el RD 337/2014 (disp. derogatoria única:
  «**Queda derogado … el Real Decreto 3275/1982**»). Se cita literal y se avisa (error 7 si se presenta la MIE-RAT
  como vigente).
- **12** revisión: comprobación por director de obra o empresa instaladora al dar de alta; «**Personal
  técnicamente competente efectuará la comprobación de la instalación de puesta a tierra, al menos anualmente, en
  la época en la que el terreno esté mas seco.**»; electrodos al descubierto «**al menos una vez cada cinco
  años**» donde el terreno no favorezca su conservación.
- **ITC-BT-24 4.1** (corte automático): tensión límite convencional «**igual a 50 V, valor eficaz en corriente
  alterna, en condiciones normales**», menores en ciertos casos, «**como por ejemplo, 24 V para las instalaciones
  de alumbrado público contempladas en la ITC-BT-09, apartado 10**».
  - **TN (4.1.1)**: «**Zs x Ia ≤ U0**»; tabla 1 tiempos: U0 230 V → 0,4 s; 400 V → 0,2 s; > 400 V → 0,1 s.
    «**Cuando el conductor neutro y el conductor de protección sean comunes (esquemas TN-C), no podrá utilizarse
    dispositivos de protección de corriente diferencial-residual.**»
  - **TT (4.1.2)**: «**RA x Ia ≤ U**», RA = «**suma de las resistencias de la toma de tierra y de los conductores
    de protección de masas**», U = «**tensión de contacto límite convencional (50, 24V u otras, según los
    casos)**». (Ejemplo de examen calculable: 50 V / 0,03 A = 1.667 Ω; es aritmética, no dato de norma.)
  - **IT (4.1.3)**: primer defecto «**RA x Id ≤ UL**»; controlador permanente de primer defecto con «**señal
    acústica o visual**»; segundo defecto «**2 x Zs x Ia ≤ U**» (neutro no distribuido) o «**2 x Zs' x Ia ≤ U0**»
    (distribuido); tabla 2: 230/400 → 0,4 s / 0,8 s; 400/690 → 0,2 / 0,4; 580/1000 → 0,1 / 0,2.
- **Compatibilidad con equipos sensibles**: aparte de los apartados 5 y 6 de la ITC-BT-18 y del zumbido (RTVE
  tese/15), **no he encontrado norma leída** que regule tierras «limpias» o separadas para electrónica. No
  inventar; si se trata, como práctica de oficio.

## 7. Tema 14 · Medidas eléctricas e instrumentación

RTVE (teitse/09 y 01) cubre el 95 %. Añadir el ancla normativa y la letra de la medida de aislamiento:

- **ITC-BT-03, apéndice I, 2.1.2** (vigente; no lo tocó el RD 770/2025): equipos mínimos de la empresa
  instaladora básica: «**Telurómetro; Medidor de aislamiento, según ITC MIE-BT 19; Multímetro o tenaza, para las
  siguientes magnitudes: Tensión alterna y continua hasta 500 V; Intensidad alterna y continua hasta 20 A;
  Resistencia; Medidor de corrientes de fuga, con resolución mejor o igual que 1 mA; Detector de tensión;
  Analizador registrador de potencia y energía para corriente alterna trifásica, con capacidad de medida de las
  siguientes magnitudes: potencia activa; tensión alterna; intensidad alterna; factor de potencia; Equipo
  verificador de la sensibilidad de disparo de los interruptores diferenciales, capaz de verificar la
  característica intensidad-tiempo; Equipo verificador de la continuidad de conductores; Medidor de impedancia de
  bucle … con una resolución mejor o igual que 0,1 Ω; Herramientas comunes y equipo auxiliar; Luxómetro con rango
  de medida adecuado para el alumbrado de emergencia**» (los «;» de la fuente van en guiones). Especialista,
  además: «**Analizador de redes, de armónicos y de perturbaciones de red**», electrodos para aislamiento de
  suelos, comprobador del vigilante de aislamiento de quirófanos. (La referencia «ITC MIE-BT 19» es del
  reglamento de 1973; se cita tal cual.)
- **ITC-BT-19 2.9, tabla 3** (resistencia de aislamiento): MBTS/MBTP → ensayo 250 V c.c., «**≥ 0,25**» MΩ;
  «**Inferior o igual a 500 V, excepto caso anterior**» → 500 V, «**≥ 0,5**»; «**Superior a 500 V**» → 1000 V,
  «**≥ 1,0**». Válido para canalizaciones de hasta 100 m; por encima, fraccionar o valor «**inversamente
  proporcional a la longitud total, en hectómetros**». Generador c.c. «**con una corriente de 1 mA para una carga
  igual a la mínima resistencia de aislamiento especificada**». «**Cuando la instalación tenga circuitos con
  dispositivos electrónicos, en dichos circuitos los conductores de fases y el neutro estarán unidos entre sí
  durante las medidas.**» (decisivo en una sala técnica: protege la electrónica). Medida respecto a tierra con
  «**el polo positivo del generador**» a tierra. Si sale bajo, se admite si cada receptor da su valor UNE «**o en
  su defecto 0,5 MΩ**» y la instalación sin receptores cumple. Rigidez: «**2U + 1000 voltios … con un mínimo de
  1.500 voltios**» durante 1 minuto; no en locales con riesgo de incendio o explosión. Fugas no superiores a la
  sensibilidad de los diferenciales.
- **RD 614/2001, anexo IV**: quién mide: «**Las maniobras locales y las mediciones, ensayos y verificaciones sólo
  podrán ser realizadas por trabajadores autorizados.**» (en AT, cualificados); con fuente exterior (megóhmetro),
  B.2.2.ª: que no haya realimentación por otra fuente y que los puntos de corte resistan «**la aplicación
  simultánea de la tensión de ensayo por un lado y la tensión de servicio por el otro**». Y B.4.1 del anexo II:
  transformador de intensidad: «**Se prohíbe la apertura de los circuitos conectados al secundario estando el
  primario en tensión, salvo que sea necesario por alguna causa, en cuyo caso deberán cortocircuitarse los bornes
  del secundario.**»
- **No confirmado**: categorías de medida CAT II/III/IV de los instrumentos (UNE-EN 61010) y métodos de
  termografía (emisividad, ΔT de criterio): no los he leído en fuente. Si RTVE los trae con cifras, el
  verificador debe confirmarlos o quitarlos.

## 8. Tema 15 · Trabajos en instalaciones eléctricas

RD 614/2001 tiene **una sola redacción** (vigencia 21-8-2001) en todos sus bloques: lo que RTVE cita sigue
vigente. Para la LPRL, **usar el común de Canal Sur** (`temas/canal-sur-comun/09-ley-31-1995.md`, ya
verificado), no `general/08`. Falta:

### 8.1 Definiciones y tabla de distancias (anexo I; RTVE no da cifras)

- Definiciones 7 (zona de peligro), 8 (trabajo en tensión, que excluye «**las maniobras y las mediciones, ensayos
  y verificaciones**»), 11 (zona de proximidad), 12 (trabajo en proximidad), 13 (trabajador autorizado), 14
  (cualificado: «**formación acreditada, profesional o universitaria, o a su experiencia certificada de dos o más
  años**»), 15 (jefe de trabajo: «**persona designada por el empresario para asumir la responsabilidad efectiva
  de los trabajos**»).
- **Tabla 1** (cm), fila **Un ≤ 1 kV**: **DPEL-1 50 · DPEL-2 50 · DPROX-1 70 · DPROX-2 300**. Otras filas para
  contraste: 20 kV → 72 · 60 · 122 · 300; 66 kV → 120 · 85 · 170 · 300; 132 kV → 180 · 110 · 330 · 500;
  220 kV → 260 · 160 · 410 · 500; 380 kV → 390 · 250 · 540 · 700. «**Las distancias para valores de tensión
  intermedios se calcularán por interpolación lineal.**» DPEL-1 con riesgo de sobretensión por rayo; DPEL-2 sin
  él; DPROX-1 cuando se puede delimitar con precisión la zona y controlar que no se sobrepasa; DPROX-2 cuando no.

### 8.2 Artículo 4 (técnicas y procedimientos), en letra

- 4.2: «**Todo trabajo en una instalación eléctrica, o en su proximidad, que conlleve un riesgo eléctrico deberá
  efectuarse sin tensión, salvo en los casos que se indican en los apartados 3 y 4 de este artículo.**»
- 4.3 a) operaciones elementales en BT con material para el público; b) tensiones de seguridad. 4.4 a) maniobras,
  mediciones, ensayos y verificaciones «**cuya naturaleza así lo exija**»; b) trabajos cuyas «**condiciones de
  explotación o de continuidad del suministro así lo requieran**» (el supuesto de un centro que emite).
- 4.7: proximidad según anexo V «**o bien se considerarán como trabajos en tensión**». 4.8: atmósferas
  explosivas y electricidad estática, anexo VI.

### 8.3 Consignación: reposición de tensión y disposiciones particulares (anexo II)

- **A.2 Reposición**, en este orden: «**1.º La retirada, si las hubiera, de las protecciones adicionales y de la
  señalización que indica los límites de la zona de trabajo. 2.º La retirada, si la hubiera, de la puesta a
  tierra y en cortocircuito. 3.º El desbloqueo y/o la retirada de la señalización de los dispositivos de corte.
  4.º El cierre de los circuitos para reponer la tensión.**» Y: «**Desde el momento en que se suprima una de las
  medidas inicialmente adoptadas para realizar el trabajo sin tensión en condiciones de seguridad, se considerará
  en tensión la parte de la instalación afectada.**»
- Regla 4 (puesta a tierra y en cortocircuito) obligatoria en AT y en BT sólo «**que, por inducción, o por otras
  razones, puedan ponerse accidentalmente en tensión**»; equipos «**conectarse en primer lugar a la toma de tierra
  y a continuación a los elementos a poner a tierra**».
- B.1 fusibles (BT sin puesta a tierra si corte visible a ambos lados); **B.3 condensadores** (separar, circuito
  de descarga, «**se esperará el tiempo necesario para la descarga**», puesta a tierra y en cortocircuito en
  bornes): directamente aplicable a SAI y baterías de condensadores.
- **Guía técnica INSST (ed. 2020)** sobre la regla 2 (bloqueo): bloqueo «**mediante el empleo de candados o
  cerraduras, combinados, en su caso, con cadenas, pasadores u otros elementos**»; «**Junto al dispositivo de
  bloqueo, se recomienda colocar una señal indicando la prohibición de maniobrar el aparato … así como la
  identificación del trabajador que lo ha accionado.**», y señales con «**la identificación del responsable de la
  desconexión, la fecha y hora de su ejecución y el teléfono de contacto**»; aparatos extraíbles retirados como
  bloqueo; placa aislante entre cuchillas de seccionador. Sentido de las cinco etapas: la cuarta «**es la que
  verdaderamente garantiza el mantenimiento de la situación de seguridad durante el período de tiempo que duren
  los trabajos**». Paso previo: «**la identificación de la zona y de los elementos de la instalación donde se va a
  realizar el trabajo**», que «**forma parte de la planificación del trabajo**». (La Guía no usa la palabra
  «consignación»; es término de oficio.)

### 8.4 Permisos de trabajo (lo que hay en fuente)

- **El RD 614/2001 no regula un «permiso de trabajo» como tal.** Lo más cercano en su letra:
  - Anexo III.B.2 (trabajos en tensión en **alta** tensión): trabajadores cualificados «**autorizados por escrito
    por el empresario**», con procedimiento «**definido por escrito**» que incluya medidas, material y
    «**Las circunstancias que pudieran exigir la interrupción del trabajo**»; autorización renovada si el
    procedimiento cambia o tras más de un año sin hacer ese trabajo; retirada si incumple o por vigilancia de la
    salud. III.B.1: jefe de trabajo que «**se comunicará con el responsable de la instalación**».
  - Anexo V.B.1.3: acceso a recintos y apertura de envolventes por autorizados de otra empresa «**con el
    conocimiento y permiso de este último**» (el titular).
- **Guía INSST 2020** (comentarios al anexo II): en AT, «**El permiso para iniciar los trabajos lo dará el
  responsable de la instalación, preferiblemente por escrito.**» y es «**muy recomendable que el responsable de
  llevar a cabo la supresión de la tensión deje constancia por escrito de que se han concluido todas las etapas
  del proceso**»; al terminar (AT y BT) el responsable constata que todo el personal ha salido y se han retirado
  equipos. Recomienda procedimientos escritos en instalaciones complejas y en AT.
- Fuera de esto, un modelo de permiso de trabajo (formulario, firmas, validez) **no lo he encontrado en fuente
  oficial leída**: hueco declarado; no inventar formato.

### 8.5 Trabajos en tensión y proximidad: letra que falta

- Anexo III.A.1: trabajadores cualificados; con procedimiento estudiado y «**ensayado sin tensión**» si su
  complejidad o novedad lo requiere; donde la comunicación sea difícil, «**al menos, dos trabajadores con
  formación en materia de primeros auxilios**». A.4: «**no llevarán objetos conductores, tales como pulseras,
  relojes, cadenas o cierres de cremallera metálicos**». A.6: suspensión por tormenta, lluvia o viento fuertes.
  C.1 a): en BT la reposición de fusibles puede hacerla un **autorizado** si el portafusible da protección
  completa.
- Anexo V.A.1: viabilidad la determina «**un trabajador autorizado, en el caso de trabajos en baja tensión, o un
  trabajador cualificado, en el caso de trabajos en alta tensión**»; reducir elementos en tensión y zonas de
  peligro (pantallas, barreras…); delimitar e informar. A.2.2: «**La vigilancia no será exigible cuando los
  trabajos se realicen fuera de la zona de proximidad o en instalaciones de baja tensión.**» B.1.1: acceso a
  recintos de servicio eléctrico (entre ellos «**salas de control**») restringido a autorizados o personal bajo su
  vigilancia; puertas señalizadas y cerradas si no hay personal. B.1.2: apertura de envolventes sólo
  autorizados.

### 8.6 Coordinación de actividades empresariales

- RD 614/2001 sólo aporta V.B.1.3 (permiso del titular) y el art. 4/anexos. **El RD 171/2004 ya está desarrollado
  con cita literal en un tema de Canal Sur cerrado**: `temas/canal-sur-especificos/32-productor-a/14-prevencion-
  de-riesgos-laborales-en-la-produccion-audiovisual.md` (epígrafe «El RD 171/2004: definiciones y objetivos» y
  siguientes; dice que tiene «una sola redacción, vigente desde el 30 de abril de» 2004). El redactor puede
  copiar de ahí lo que necesite (titular, principal, información e instrucciones, medios de coordinación) en vez
  de reinvestigar; el volcado `fuentes/canal-sur/BOE-A-2004-1848.md` es de 25-09-2026. El común (`09-ley-31-1995`)
  sólo lo nombra.
- La Guía INSST de riesgo eléctrico **no desarrolla la coordinación empresarial** (búsqueda de «artículo 24»,
  «171/2004», «concurrencia» sin resultado útil).

## 9. Lo que no pude confirmar (resumen para el redactor y el verificador)

1. Cualquier «novedad REBT 2026» (diferenciales tipo AC, DPS obligatorio, ITC-BT-53): **no publicada en el BOE**
   a 05-10-2026 según la consolidación (última actualización 18-12-2025). Única cautela residual: un RD publicado
   después del 18-12-2025 y aún no consolidado no aparecería en la API; no he podido consultar el buscador del BOE
   (no devuelve resultados por petición directa).
2. Condiciones Ib ≤ In ≤ Iz e I2 ≤ 1,45·Iz: no están en el REBT; norma UNE no leída.
3. Clases CPR de cables (Cca, B2ca…): no leídas.
4. Categorías CAT de instrumentos y criterios numéricos de termografía: no leídos.
5. Penalización de reactiva en factura: no leída.
6. Orden andaluza de 5-3-2013 (documentación de puesta en servicio en Andalucía): sólo título.
7. Que la UNE-HD 60364-6 sustituya a la UNE 20.460-6-61 (o la 60364-5-52 a la 20.460-5-523): el listado no lo dice.
8. Modelo de permiso de trabajo: no hay en fuente oficial leída.
9. Tierras «limpias» o separadas para equipos sensibles: sin norma leída.

## 10. Avisos de reutilización

- Ficha de todos los temas copiados de RTVE: cambiar «La vigente el 21/12/2022» por la redacción vigente hoy
  (ver §1); en teitse/15, la frase sobre que la convocatoria fija la versión «última actualización publicada el
  28/04/2021» es **propia de RTVE**: quitarla.
- teitse/15 cita el art. 2 (redacción RD 298/2021, vigencia 1-7-2021): sigue vigente.
- Si algún tema de RTVE trae el listado de la ITC-BT-02 «de 2020», actualizar a la Resolución de 20-3-2025.
- Si algún tema de RTVE trae el art. 25 con rúbrica «Equivalencia de normativa del Espacio Económico Europeo»,
  hoy es «**Artículo 25. Reconocimiento mutuo.**» (RD 145/2023, vigencia 1-7-2023), con mención a Turquía, AELC y
  el «**Reglamento (UE) n.º 2019/515**».
