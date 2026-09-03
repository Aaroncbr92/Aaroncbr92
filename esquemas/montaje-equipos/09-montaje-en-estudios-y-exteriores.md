# Esquema · Tema 9 del específico de Montaje de Equipos Audiovisuales · Montaje de equipos en estudios y exteriores

Telegrama. **Cada línea lleva delante de dónde sale**: `[REBT]` = Real Decreto 842/2002, reglamento
electrotécnico para baja tensión, con su **ITC-BT-24** · `[614]` = Real Decreto 614/2001, riesgo
eléctrico · `[1215]` = Real Decreto 1215/1997, equipos de trabajo · `[BT.2020]` = Recomendación
UIT-R BT.2020-2 · `[of]` = oficio · `[plan]` = plantilla oficial. **Todas las normas, en su redacción
vigente al 21/12/2022.**

**Cabecera.** Enunciado: «5. MONTAJE DE EQUIPOS AUDIOVISUALES EN ESTUDIOS Y EXTERIORES» con sus seis
subpuntos · **13 preguntas: EL BANCO MÁS GRANDE DE ESTA OCUPACIÓN** · **siete de las trece son de
electricidad básica** · **una descansa sólo en la plantilla (59)**.

<!-- indice -->

## Índice

- [El plano de emplazamiento](#el-plano-de-emplazamiento)
- [Las líneas y sus conectores](#las-líneas-y-sus-conectores)
- [Las resoluciones](#las-resoluciones)
- [Lingas y arriostramiento](#lingas-y-arriostramiento)
- [El enlace punto a punto](#el-enlace-punto-a-punto)
- [Las cuatro magnitudes](#las-cuatro-magnitudes)
- [La trampa de la pregunta 93](#la-trampa-de-la-pregunta-93)
- [Los aparatos de medida](#los-aparatos-de-medida)
- [Las protecciones del cuadro](#las-protecciones-del-cuadro)
- [Lo que la norma exige](#lo-que-la-norma-exige)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## El plano de emplazamiento

- `[of]` · **QUÉ ES**: el dibujo que dice **dónde va cada cosa**: cámaras, micros, soportes, cuadros,
  cajas de conexión, unidad móvil y **por dónde va cada tirada de cable**.
- **PARA QUÉ, EN TRES COSAS**: **fija posiciones** antes de que llegue el equipo · **calcula
  metrajes** (cuánto cable cargar) · **reparte la carga**, eléctrica y estructural.
- **LA REGLA DE ORO**: **fuerza y señal NO comparten canaleta**, y **en el plano se ve antes que en el
  suelo**.
- **LO QUE EL PLANO NO DICE**: estado real de los apoyos, altura libre, accesibilidad y **de dónde sale
  la corriente**. **Se valida sobre el terreno antes de descargar.**

## Las líneas y sus conectores

| Línea | Cable | Conector |
|---|---|---|
| **Vídeo en banda base** | Coaxial | **BNC**, **75 Ω** |
| **Vídeo por fibra** | Fibra | **LC**, **SC** o híbrido de cámara |
| **Audio** | Par apantallado | **XLR** de tres polos |
| **Red y datos** | Par trenzado | **RJ45** |
| **Radiofrecuencia** | Coaxial | **N**, BNC, TNC (**roscado en intemperie**) |
| **Cámara** | Triax o **fibra híbrida** | Multipolo del fabricante |

- **LOS TRES CUIDADOS DE LA TIRADA**: **radio de curvatura** (sobre todo en fibra) · **protección del
  paso** de personas y vehículos · **etiquetado en LOS DOS extremos**.
- **EL BUCLE DE SERVICIO NO ES DESORDEN**: **permite mover el equipo medio metro** y **evita que la
  tracción tire del conector**.

## Las resoluciones

| Formato | Píxeles |
|---|---|
| **HD** | 1.280 × 720 |
| **Full HD** | 1.920 × 1.080 |
| **UltraHD** | **3.840 × 2.160** |
| **8K** | 7.680 × 4.320 |

- **PREGUNTA 37** · **UltraHD = 3.840 × 2.160.**
- `[BT.2020]` · **NO ES SÓLO PLANTILLA**: el **Cuadro 1, «Características espaciales de la imagen»**,
  da **«7 680 × 4 320»** y **«3 840 × 2 160»**, con formato **«16:9»** y píxeles cuadrados.
- **LA FALSA QUE NO EXISTE**: **2.560 × 4.320** —invierte y mezcla cifras del 8K—. Las otras dos son
  HD y Full HD.
- **LA REGLA QUE NO FALLA**: **UltraHD es EXACTAMENTE CUATRO VECES Full HD** (doble de ancho, doble de
  alto) **y 8K es cuatro veces UltraHD.**

## Lingas y arriostramiento

- **PREGUNTA 53** · **Una linga sirve PARA COLGAR CÁMARAS Y OTROS ACCESORIOS EN ESTRUCTURAS
  ELEVADAS.** Las falsas describen **la cabeza de fluido**, algo que **ninguna linga hace**, y **los
  brazos mágicos**.
- **PREGUNTA 69** · **ARRIOSTRAR = AFIANZAR LA CÁMARA Y EL TRÍPODE A ESTRUCTURAS O PRACTICABLES.** De
  *riostra*, **la pieza diagonal que impide que una estructura se deforme**.
- **CUÁNDO SE ARRIOSTRA, SIEMPRE**: **altura sobre andamio o practicable · tribuna · óptica larga con
  viento · cualquier caída que alcance a personas.**
- **LA LINGA DE SEGURIDAD VA ADEMÁS DEL ANCLAJE PRINCIPAL, NUNCA EN SU LUGAR.**
- `[1215]` · **anexo I.2.b)**: **«En las máquinas para elevación de cargas deberá figurar una
  indicación claramente visible de su carga nominal»** y **«Los accesorios de elevación deberán estar
  marcados de tal forma que se puedan identificar las características esenciales para un uso
  seguro.»**
- `[plan]` · **PREGUNTA 59** · **El dato obligatorio en la placa de una linga es EL AÑO Y MES DE
  FABRICACIÓN.** **La norma obliga a marcar «las características esenciales» pero NO las enumera**:
  la lista está en las **UNE-EN** de producto, no consultadas.
- **LO QUE SÍ SE SOSTIENE**: **la fecha permite calcular la vida útil restante**, y por eso va en la
  placa. Falsas: **el color** no identifica nada normalizado · **el número de serie** identifica la
  pieza **pero no su edad** · **el nombre del operador** no cabe en algo que pasa de mano en mano.

## El enlace punto a punto

| Parte | Qué hace |
|---|---|
| **Disco parabólico** | **CONCENTRA LA RADIACIÓN EN UN HAZ ESTRECHO.** Es un **reflector PASIVO** |
| **Iluminador** | En el foco de la parábola: **ES LA ANTENA PROPIAMENTE DICHA** |
| **Cabeza transmisora o receptora** | La electrónica de radiofrecuencia |
| **Trípode** | Sostiene y **apunta** |
| **Latiguillo coaxial** | Entre cabeza e iluminador, con **conector N** |

- **PREGUNTA 57** · **Lo que NO es parte de un enlace punto a punto es EL CONECTOR LC**: **el LC es de
  FIBRA, y el enlace es RADIO.**
- **PREGUNTA 82** · **El latiguillo con conector N se conecta EN EL ILUMINADOR.** **El disco es una
  superficie metálica sin conector**; **lo que va conectado es el iluminador de su foco.**
- **POR QUÉ CONECTOR N Y NO BNC**: **es ROSCADO** —en intemperie no se suelta— y **aguanta más potencia
  y más frecuencia**.
- **EL MONTAJE, EN ORDEN**: nivelar soporte → montar disco → **iluminador en el foco con la
  POLARIZACIÓN correcta** → latiguillo → cabeza → alimentar → **y SÓLO ENTONCES apuntar**.

## Las cuatro magnitudes

| Magnitud | Qué es | Unidad |
|---|---|---|
| **Tensión** | La diferencia de potencial que empuja los electrones | Voltio |
| **Intensidad** | La carga que pasa por segundo | Amperio |
| **Resistencia** | La oposición al paso de la corriente | Ohmio |
| **POTENCIA** | **EL TRABAJO DESARROLLADO EN UN TIEMPO DETERMINADO** | Vatio |

- **PREGUNTA 7** · **Trabajo en un tiempo determinado = POTENCIA.** Falsas: **ley de Ohm** (una
  relación), **fuerza motriz** (la causa) y **electrones** (las partículas).
- **PREGUNTA 17** · **La resistencia que posee UN MATERIAL ESPECÍFICO es la RESISTIVIDAD.**
- **LA DISTINCIÓN QUE LA PREGUNTA PIDE**: **RESISTENCIA = propiedad DE UNA PIEZA** (este cable, esta
  longitud, esta sección; en ohmios) · **RESISTIVIDAD = propiedad DEL MATERIAL** (el cobre, el
  aluminio; en ohmios por metro, **no depende de la forma**).
- **POR ESO SE CABLEA EN COBRE**: **no porque un cable concreto tenga poca resistencia, sino porque el
  cobre, COMO MATERIAL, tiene poca resistividad.**
- **LEY DE OHM**: **I = V / R.**

## La trampa de la pregunta 93

- **PREGUNTA 93** · **A MAYOR RESISTENCIA, MENOR FLUJO DE CORRIENTE.** **La resistencia está en el
  denominador.**
- **LA OPCIÓN c) ES LA MEJOR TRAMPA DEL CUADERNILLO**: **empieza bien** —«cuanto mayor sea la
  resistencia, menor será el flujo»— **y acaba mal**: «**por lo tanto la intensidad es DIRECTAMENTE
  proporcional a la resistencia**». **Se contradice a sí misma en la misma frase**: es
  **INVERSAMENTE** proporcional.
- **LA BUENA ES LA a) PORQUE DICE LO MISMO Y SE CALLA.**
- **CÓMO SE ESTUDIA ESTA TRAMPA**: **cuando dos opciones empiezan igual, la diferencia está en la
  coletilla**, y la coletilla lleva la palabra que decide.

## Los aparatos de medida

| Se mide | Con | Cómo se conecta |
|---|---|---|
| **Tensión** | **VOLTÍMETRO** | **En paralelo**, sin abrir el circuito |
| **Intensidad** | **Amperímetro** | **En serie**, o con pinza |
| **Resistencia** | **OHMÍMETRO** | **Sobre el elemento aislado y SIN TENSIÓN** |
| **Frecuencia** | Frecuencímetro | En paralelo |
| Varias | Polímetro o multímetro | Según escala |

- **PREGUNTA 58** · **La resistencia se mide con el OHMÍMETRO.**
- **PREGUNTA 96** · **La tensión se mide con el VOLTÍMETRO.** **AVISO**: **la opción d) dice
  «ohmiómetro», que es la misma palabra de la opción a) con otra grafía**: **el examen ofrece el mismo
  aparato dos veces, y ninguna es la buena.**
- **EL AVISO DE OFICIO**: **la resistencia se mide sin tensión y con el elemento desconectado.** Medir
  en circuito alimentado **da lectura falsa y puede dañar el aparato**.

## Las protecciones del cuadro

| Dispositivo | De qué protege | Cómo se reconoce |
|---|---|---|
| **Interruptor general automático** | Corta toda la instalación | Es el de cabecera |
| **Interruptor de control de potencia** | **Limita la potencia contratada** | Es de la compañía |
| **Interruptor automático** o magnetotérmico | **Sobreintensidades y cortocircuitos** | **Corta por sí mismo** |
| **INTERRUPTOR DIFERENCIAL** | **Derivaciones y contactos indirectos** | **LLEVA BOTÓN DE TEST** |
| **RELÉ TÉRMICO** | **DETECTA intensidades no admisibles** | Va con un contactor; **NO CORTA SOLO** |

- **PREGUNTA 77** · **El que consta de botón de testeo y protege de derivaciones es el INTERRUPTOR
  DIFERENCIAL.**
- **QUÉ HACE, EN UNA FRASE**: **compara la corriente que entra con la que sale; si no son iguales, una
  parte se ha ido por otro camino** —tierra o persona— **y corta**.
- **POR QUÉ TIENE BOTÓN**: **puede pasar años sin actuar, y sin probarlo nadie sabe si sigue vivo.**
- `[REBT ITC-BT-24, 3.5]` · **«El empleo de dispositivos de corriente diferencial-residual, cuyo valor
  de corriente diferencial asignada de funcionamiento sea inferior o igual a 30 mA, se reconoce como
  medida de protección complementaria…»** y **«Esta medida de protección está destinada solamente a
  complementar otras medidas de protección contra los contactos directos.»**
- **DE AHÍ SALEN LOS 30 mA Y LA ADVERTENCIA**: **un diferencial NO sustituye al aislamiento ni a la
  puesta a tierra: los complementa.**
- **PREGUNTA 51** · **El relé térmico DETECTA LAS INTENSIDADES NO ADMISIBLES por el circuito.** **La
  clave es el verbo: DETECTAR.** Detecta por el calentamiento de sus bimetales **y ordena la apertura
  al contactor**, pero **no interrumpe por sí mismo**.
- **LAS TRES FALSAS DESCRIBEN OTRO APARATO**: **a) el diferencial** («detecta y elimina defectos de
  aislamiento») · **c) el fusible o el magnetotérmico** («cortar automáticamente… cuando la intensidad
  es muy alta») · **d) el magnetotérmico con todas sus palabras** («cortar por sí mismo»).
- **LA FRASE QUE RESUELVE LA 51**: **el relé térmico DETECTA Y AVISA; el magnetotérmico DETECTA Y
  CORTA.**

## Lo que la norma exige

- `[REBT]` · **Artículo 2**: **«Corriente alterna: igual o inferior a 1.000 voltios. Corriente
  continua: igual o inferior a 1.500 voltios.»** **Los 1.000 V en alterna son la frontera**: todo lo
  de un plató y una unidad móvil está por debajo.
- `[614]` · **Artículo 3**: la instalación **«deberá adaptarse a las condiciones específicas del propio
  lugar»**, teniendo en cuenta **«la presencia de superficies muy conductoras, agua o humedad»**. **Eso
  es el exterior de una retransmisión.**
- `[614]` · **Artículo 4**: **«Todo trabajo en una instalación eléctrica, o en su proximidad, que
  conlleve un riesgo eléctrico deberá efectuarse sin tensión»**, salvo los casos de sus apartados 3
  y 4.
- **LA REGLA DE MONTAJE QUE SALE DE AHÍ**: **se cablea con el cuadro abierto y se da tensión al final,
  nunca al revés.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 7 | Trabajo desarrollado en un tiempo determinado | d) Potencia ✔ |
| 17 | Resistencia de un material específico | b) Resistividad ✔ |
| 37 | Resolución de grabación UltraHD | d) 3.840 × 2.160 ✔ |
| 51 | Qué es un relé térmico | b) Detecta las intensidades no admisibles ✔ |
| 53 | Para qué sirve una linga | a) Colgar cámaras en estructuras elevadas ✔ |
| 57 | Cuál NO es parte de un enlace punto a punto | d) Conector LC ✔ |
| 58 | Con qué se mide la resistencia | b) Ohmímetro ✔ |
| 59 | Dato obligatorio en la placa de una linga | b) Año y mes de fabricación ✔ **·** sólo con la plantilla |
| 69 | Qué significa «arriostramiento» | d) Afianzar cámara y trípode a estructuras ✔ |
| 77 | Interruptor con botón de testeo | d) Interruptor diferencial ✔ |
| 82 | Dónde se conecta el latiguillo con conector N | d) En el iluminador ✔ |
| 93 | Si aumenta la resistencia | a) A mayor resistencia, menor flujo ✔ |
| 96 | Con qué se mide la tensión | c) Voltímetro ✔ |

**Las trece oficiales son correctas**, y **una descansa sólo en la plantilla**. · **Aviso de
reparto**: **trece de noventa y seis, y SIETE son electricidad básica.** **Quien domine tensión,
intensidad, resistencia, potencia y las cinco protecciones del cuadro se lleva más del 7 % del
examen.** · **Aviso de formato**: **la 93 lleva un distractor que se contradice a sí mismo** y **la 96
ofrece el mismo aparato con dos ortografías**: **hay que leer la opción entera antes de marcarla.**
