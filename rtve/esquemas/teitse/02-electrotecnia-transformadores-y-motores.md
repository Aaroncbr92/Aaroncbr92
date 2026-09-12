# Esquema · Tema 2 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Electrotecnia: transformadores y motores

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio eléctrico y teoría clásica de
máquinas · `[plan]` = enunciado del anexo. **Siglas y símbolos**: el reglamento electrotécnico para
baja tensión (**REBT**); el voltamperio (**VA**) y el kilovoltamperio (**kVA**); el vatio (**W**);
revoluciones por minuto (**r.p.m.**); la relación de transformación (**m**); y el número de pares de
polos (**p**).

**Cabecera.** Enunciado: punto 2 del anexo, **las MÁQUINAS eléctricas** · **el enunciado es el índice y
conviene aprovecharlo**: **primera mitad el transformador** —generalidades, teoría, acoplamiento en
paralelo, autotransformador, aislamiento galvánico, pérdidas—, **segunda mitad el motor** —tipos,
disposición estrella-triángulo, guardamotores— · **reparto con el tema 1**: **aquél los NOMBRA y éste
los DESARROLLA**; **los fundamentos están allí y aquí se usan, no se repiten.**

<!-- indice -->

## Índice

- [El transformador](#el-transformador)
- [El aislamiento galvánico](#el-aislamiento-galvánico)
- [El autotransformador](#el-autotransformador)
- [El acoplamiento en paralelo](#el-acoplamiento-en-paralelo)
- [Pérdidas y rendimiento](#pérdidas-y-rendimiento)
- [Los motores](#los-motores)
- [Estrella-triángulo y los demás arranques](#estrella-triángulo-y-los-demás-arranques)
- [El guardamotor](#el-guardamotor)
- [Aviso de estudio](#aviso-de-estudio)

<!-- /indice -->

## El transformador

- **DEFINICIÓN CON SUS TRES CONDICIONES** · `[of]` · **máquina ESTÁTICA que transfiere energía entre
  dos circuitos de alterna, cambiando tensión y corriente y MANTENIENDO la frecuencia.**

| Palabra | Por qué está |
|---|---|
| **Estática** | **Sin partes móviles**: el rendimiento más alto de todas las máquinas eléctricas |
| **Alterna** | **Necesita flujo VARIABLE**: en continua no funciona |
| **Mantiene la frecuencia** | **Cambiarla es cosa de un variador, no de un transformador** |

| Parte | Qué es |
|---|---|
| **Núcleo magnético** | **Chapa de acero al silicio APILADA Y AISLADA**, para conducir flujo y limitar parásitas |
| **Primario** | **El que recibe la energía** |
| **Secundario** | **El que la entrega** |
| **Aislamientos, cuba, refrigerante, pasantes** | El resto, en los de potencia |

- **EL PRINCIPIO EN CUATRO PASOS** · `[of]` · **la tensión alterna del primario hace circular corriente
  alterna** → **esa corriente crea FLUJO ALTERNO en el núcleo** → **el flujo atraviesa el secundario y
  por ser variable induce tensión** → **la tensión inducida es proporcional a las espiras.**
- **LA FÓRMULA DEL PUNTO** · `[of]` · **m = N₁ / N₂ = U₁ / U₂ = I₂ / I₁** · **tensiones DIRECTAMENTE
  proporcionales a las espiras** · **corrientes INVERSAMENTE**: **el lado de más tensión lleva menos
  corriente** · **la aparente es prácticamente la misma en los dos lados.**
- **LA LECTURA QUE JUSTIFICA UN CENTRO DE TRANSFORMACIÓN** · `[of]` · **elevar la tensión reduce la
  corriente en la misma proporción y las pérdidas caen con el CUADRADO** · **multiplicar la tensión por
  diez divide las pérdidas por cien.**

## El aislamiento galvánico

- **QUÉ ES** · `[of]` · **la separación ELÉCTRICA entre primario y secundario** · **la energía pasa por
  el campo magnético, no por un conductor**: **no hay camino de corriente entre los dos circuitos.**

| Uso | Qué resuelve |
|---|---|
| **Seguridad de las personas** | **Un secundario aislado y sin tierra no cierra circuito por una persona en contacto con un solo conductor** |
| **Romper bucles de masa** | **Elimina la corriente entre dos equipos unidos por su masa y alimentados de puntos distintos** |
| **Adaptar regímenes de neutro** | Crea localmente un esquema distinto del de la red |
| **Reducir perturbaciones** | Sobre todo con **pantalla electrostática entre devanados** |

- **EL USO QUE TOCA A UNA CASA QUE EMITE** · `[of]` · **dos equipos de audio unidos por la malla y
  alimentados de dos cuadros distintos**: **la diferencia de potencial entre las dos tierras hace
  circular corriente por esa malla** · **esa corriente SE OYE** · **un transformador de aislamiento
  corta el bucle.**
- **EL AVISO DONDE SE FALLA** · `[of]` · **un AUTOTRANSFORMADOR NO da aislamiento galvánico** · **por
  eso el enunciado del anexo nombra las dos cosas seguidas.**

## El autotransformador

- **QUÉ ES** · `[of]` · **un transformador con UN SOLO devanado y una derivación intermedia** ·
  **primario y secundario comparten devanado**, y por tanto **están unidos eléctricamente.**

| | **Dos devanados** | **AUTOTRANSFORMADOR** |
|---|---|---|
| **Devanados** | **Dos, separados** | **Uno, con toma intermedia** |
| **Aislamiento galvánico** | **SÍ** | **NO** |
| **Tamaño y coste a igual potencia** | Mayor | **MENOR** |
| **Rendimiento** | Alto | **Aún más alto** |
| **Corriente de cortocircuito** | Limitada por su impedancia | **Mayor**, por menor impedancia |
| **Relación práctica** | Cualquiera | **Mejor cuanto más próxima a uno** |

- **POR QUÉ ES MÁS PEQUEÑO** · `[of]` · **sólo la parte NO COMÚN transfiere potencia por inducción; el
  resto va por conducción directa** · **la máquina se dimensiona por la parte inducida**, y **el ahorro
  crece cuanto más parecidas son las dos tensiones.**

| Se usa | No se usa |
|---|---|
| **Adaptar 400 a 230 voltios** en tensiones próximas | **Donde haga falta aislamiento por seguridad** |
| **Arranque de motores** por reducción de tensión | **Donde el secundario deba tener otro régimen de neutro** |
| **Estabilizadores y reguladores** | **En equipos médicos o de medida que exijan separación** |

- **LA REGLA EN UNA LÍNEA** · `[of]` · **es un transformador barato al que se le ha quitado la
  propiedad que a veces es la más importante.**

## El acoplamiento en paralelo

- **CUÁNDO** · `[of]` · **cuando la demanda supera a un transformador**, o **para poder dejar uno fuera
  de servicio sin cortar el suministro.**

| Condición | Qué pasa si falta |
|---|---|
| **1 · Misma relación de transformación** | **Corriente de circulación entre los dos, sin carga** |
| **2 · Igual tensión de cortocircuito** | **Reparto desigual**: uno se sobrecarga antes |
| **3 · Mismo índice horario** o compatible | **Desfase entre secundarios y corriente muy alta** |
| **4 · Misma secuencia de fases** | **Igual: desfase y circulación** |
| **5 · Potencias no muy dispares** | Reparto difícil; **relación recomendada no mayor de 1 a 3** |

- **LA QUE DECIDE EL REPARTO** · `[of]` · **la carga se reparte en proporción INVERSA a la tensión de
  cortocircuito**: **el de menor impedancia se lleva más** · **dos máquinas iguales con impedancias
  distintas no van al cincuenta por ciento**, y **el conjunto no da la suma de las dos.**
- **LA QUE PRODUCE EL ACCIDENTE** · `[of]` · **el índice horario es el DESFASE primario-secundario en
  múltiplos de treinta grados** · **con índices incompatibles, entre secundarios aparece una diferencia
  de tensión que sólo limita su propia impedancia**: **cortocircuito permanente.**

## Pérdidas y rendimiento

| Familia | Dónde | De qué dependen | Ensayo |
|---|---|---|---|
| **HIERRO o VACÍO** | **En el núcleo**: histéresis y parásitas | **De la TENSIÓN y la frecuencia**; **casi constantes** | **De VACÍO** |
| **COBRE o CARGA** | **En los devanados**, por Joule | **Del CUADRADO de la corriente** | **De CORTOCIRCUITO** |

- **LA CONSECUENCIA DE OFICIO** · `[of]` · **el hierro se paga las veinticuatro horas, cargado o
  vacío** · **un transformador sobredimensionado gasta lo mismo en vacío y aprovecha peor.**
- **EL PUNTO DE RENDIMIENTO MÁXIMO** · `[of]` · **cuando las pérdidas en el cobre IGUALAN a las del
  hierro** · **como las del cobre van con el cuadrado de la carga, ese punto está POR DEBAJO de la
  plena carga.**

| Pérdida del hierro | Qué es | Cómo se reduce |
|---|---|---|
| **HISTÉRESIS** | **Lo que cuesta invertir la imanación en cada ciclo** | **Acero al silicio de grano orientado** |
| **PARÁSITAS o de Foucault** | **Corrientes inducidas en la masa del núcleo** | **APILANDO CHAPAS finas AISLADAS** |

- **EL DETALLE QUE TODOS HAN VISTO Y POCOS NOMBRAN** · `[of]` · **el núcleo no es un bloque de hierro,
  es un paquete de chapas barnizadas y aisladas entre sí** · **eso corta el camino a las corrientes que
  circularían por la masa.**

| Ensayo | Cómo | Qué da |
|---|---|---|
| **VACÍO** | **Secundario abierto, primario a tensión nominal** | **Pérdidas del hierro y corriente de vacío** |
| **CORTOCIRCUITO** | **Secundario en corto, primario a tensión reducida hasta la nominal** | **Pérdidas del cobre y TENSIÓN DE CORTOCIRCUITO** |
| **Relación de transformación** | Tensiones en vacío | **Relación e índice horario** |
| **Aislamiento** | Megóhmetro entre devanados y a masa | **Estado del aislamiento** |
| **Rigidez dieléctrica** | Sobre muestra de aceite | **Envejecimiento y humedad del refrigerante** |

## Los motores

| Familia | Cómo funciona | Dónde |
|---|---|---|
| **ASÍNCRONO TRIFÁSICO** | **Campo giratorio en el estátor; el rotor va ARRASTRADO, siempre algo más despacio** | **El industrial por excelencia**: bombas, ventiladores, compresores, ascensores |
| **Asíncrono MONOFÁSICO** | **Artificio de arranque**: condensador o espira de sombra | Pequeña potencia |
| **SÍNCRONO** | **Gira EXACTAMENTE a la velocidad del campo** | Grandes potencias, compensación, generación |
| **CONTINUA** | Escobillas y colector; **par y velocidad fáciles de regular** | Tracción, servos; en retroceso |
| **Paso a paso y servos** | **Posicionamiento controlado** | Automatismos, cabezas robotizadas |

| Concepto | Qué es |
|---|---|
| **Velocidad de SINCRONISMO** | **La del campo**: **n = 60 · f / p** |
| **DESLIZAMIENTO** | **Diferencia relativa entre sincronismo y velocidad real** |
| **Rotor de JAULA** | **Barras cortocircuitadas por dos anillos**: el más robusto |
| **Rotor BOBINADO** | **Devanado accesible**: permite resistencias de arranque |

- **LA PREGUNTA CONCEPTUAL DEL PUNTO** · `[of]` · **si girase a sincronismo el rotor no vería flujo
  variable** → **sin flujo variable no hay tensión inducida** → **sin tensión no hay corriente** →
  **sin corriente no hay par** · **el motor gira porque va RETRASADO.**
- **EL PROBLEMA QUE TODO LO DEMÁS RESUELVE** · `[of]` · **la CORRIENTE DE ARRANQUE**: **varias veces la
  nominal** · **provoca caídas de tensión, dispara protecciones y castiga la mecánica.**

## Estrella-triángulo y los demás arranques

| Fase | Conexión | Qué recibe cada devanado | Qué pasa |
|---|---|---|---|
| **Arranque** | **ESTRELLA** | **La de línea dividida por raíz de tres** | **Corriente y par a UN TERCIO** |
| **Marcha** | **TRIÁNGULO** | **La de línea entera** | **Régimen nominal** |

- **TRES COSAS QUE HAY QUE SABER DECIR** · `[of]` · **sólo es posible si el motor puede trabajar en
  TRIÁNGULO a la tensión de red** —**lo dice la placa**— · **baja la corriente a un tercio pero también
  el PAR**, así que **no sirve con par resistente alto** · **la conmutación produce TRANSITORIO**, y
  **la temporización del contactor de paso es lo que lo limita.**
- **EL ESQUEMA DE POTENCIA** · `[of]` · **TRES contactores** —red, estrella, triángulo— **con
  enclavamiento mecánico y eléctrico entre los dos últimos**, porque **cerrarlos a la vez es un
  cortocircuito franco entre fases.** (Tema 3.)

| Método | Qué hace | Coste |
|---|---|---|
| **Directo** | **Plena tensión** | El más barato; **sólo motores pequeños o redes fuertes** |
| **Estrella-triángulo** | **Tensión reducida en dos escalones** | Barato; **par a un tercio** |
| **Por autotransformador** | **Escalones elegibles** | Más caro; **más par para la misma corriente** |
| **Resistencias rotóricas** | **Sólo rotor bobinado** | **Mucho par**, poco usado hoy |
| **ARRANCADOR PROGRESIVO** | **Rampa de tensión electrónica** | **Sin escalones ni transitorios** |
| **VARIADOR DE FRECUENCIA** | **Cambia tensión Y frecuencia** | **El más caro y el único que regula en marcha** |

- **LA OBSERVACIÓN QUE ORDENA LA TABLA** · `[of]` · **los cuatro primeros sólo ARRANCAN; los dos
  últimos GOBIERNAN** · **el variador es lo único que cambia la velocidad de un asíncrono en servicio**,
  porque **la velocidad depende de la frecuencia** · **eso ha desplazado al motor de continua.**

## El guardamotor

| Función | Guardamotor | Magnetotérmico de línea |
|---|---|---|
| **Térmica de SOBRECARGA** | **Sí, y REGULABLE** a la nominal del motor | Fija, según calibre |
| **Magnética de CORTOCIRCUITO** | **Sí, tarada alto** para tolerar el arranque | Curva de línea, más sensible |
| **Maniobra manual** | **Sí**: sirve de seccionamiento | Sí |
| **Falta de fase** | **Sí, en los diferenciales de fase** | No |

- **LOS TRES RASGOS, JUNTOS** · `[of]` · **térmica REGULABLE**, porque **se ajusta a la corriente de
  PLACA del motor, no a la del cable** · **magnética MUY ALTA** —del orden de una docena de veces la
  nominal—, **o dispararía en cada arranque** · **detección de FALTA DE FASE**, la avería que más
  motores quema: **el motor sigue girando y absorbe por las dos fases restantes mucho más.**
- **LA ALTERNATIVA CLÁSICA** · `[of]` · **contactor + RELÉ TÉRMICO + fusibles** · **térmico la
  sobrecarga, fusibles el cortocircuito, contactor la maniobra** · **el guardamotor reúne las tres.**
- **LAS CLASES DE DISPARO** · `[of]` · **se designan por el tiempo máximo de disparo a una sobrecarga
  dada** —**clases 10, 20 y 30**— y **se eligen por el TIEMPO DE ARRANQUE de la carga**: **mucha
  inercia pide clase alta**, o **la térmica dispara antes de llegar a velocidad.**
- **EL AVISO QUE CIERRA EL PUNTO** · `[of]` · **la protección del MOTOR y la de la LÍNEA son dos cosas
  distintas y hacen falta las dos** · **el guardamotor protege la máquina; el cable se protege por su
  intensidad admisible.** (Temas 3 y 5.)

## Aviso de estudio

- **ESTE TEMA NO CITA NINGUNA NORMA** · `[plan]` · **el enunciado del punto no nombra ninguna**:
  **nombra materias de electrotecnia** · **lo de abajo es teoría clásica de máquinas y oficio.**
- **LO QUE NO SE DA** · `[of]` · **ninguna cifra de tarado, ningún múltiplo exacto de corriente de
  arranque, ninguna tabla de clases y ningún rendimiento**: **son dato de producto** · **donde hace
  falta un orden de magnitud se dice con esas palabras y no como un valor.**
