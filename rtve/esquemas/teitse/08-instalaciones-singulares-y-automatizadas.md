# Esquema · Tema 8 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Instalaciones singulares y automatizadas en edificios e industrias

Telegrama. **Cada línea lleva delante de dónde sale**: `[BOE]` = reglamento o instrucción citados
literalmente en el tema · `[of]` = oficio de instalaciones y de control · `[plan]` = enunciado del
anexo. **Siglas**: el reglamento electrotécnico para baja tensión (**REBT**) y sus instrucciones
(**ITC-BT-27** a **ITC-BT-39**, **ITC-BT-51**); el sistema de gestión técnica de edificios (**BMS**,
*building management system*); el autómata programable (**PLC**, *programmable logic controller*); el
control de supervisión y adquisición de datos (**SCADA**); el grado de protección (**IP**); el metro
cuadrado (**m²**); y la Asociación Española de Normalización (**UNE**).

**Cabecera.** Enunciado: punto 8 del anexo · **junta dos cosas distintas y hay que separarlas.**

| Mitad | Qué es | Dónde está |
|---|---|---|
| **SINGULARES** | **Las que el reglamento saca de la regla general** por emplazamiento o uso | **Instrucciones PARTICULARES**, ITC-BT-27 a ITC-BT-39 |
| **AUTOMATIZADAS** | **Las que se gobiernan solas**: domótica, inmótica, control industrial | **ITC-BT-51 y, sobre todo, EN NINGUNA NORMA**: es oficio |

- **LA REGLA QUE GOBIERNA LA PRIMERA MITAD** · `[BOE]` · **artículo 2.5: las específicas SUSTITUYEN,
  MODIFICAN O COMPLEMENTAN a las generales** · `[of]` · **una instalación singular no es una
  instalación aparte: es una normal a la que se le añade o se le cambia algo.**

<!-- indice -->

## Índice

- [Cómo se decide que una instalación es singular](#cómo-se-decide-que-una-instalación-es-singular)
- [Locales de pública concurrencia](#locales-de-pública-concurrencia)
- [Los servicios de seguridad](#los-servicios-de-seguridad)
- [El alumbrado de emergencia](#el-alumbrado-de-emergencia)
- [Instalaciones automatizadas](#instalaciones-automatizadas)
- [Lo singular en una casa que emite](#lo-singular-en-una-casa-que-emite)
- [Aviso de estudio](#aviso-de-estudio)

<!-- /indice -->

## Cómo se decide que una instalación es singular

| Causa | Ejemplos |
|---|---|
| **El agua** | **Húmedos, mojados, piscinas y fuentes, saunas** |
| **Polvo o corrosión** | **Polvorientos, con riesgo de corrosión** |
| **La temperatura** | **Elevada o muy baja** |
| **INCENDIO O EXPLOSIÓN** | **Atmósferas explosivas, almacenes de inflamables** |
| **La ocupación** | **Locales de pública concurrencia** |
| **La condición de las personas** | **Quirófanos y salas de intervención** |
| **El carácter temporal** | **Obras, ferias, exposiciones, casetas** |
| **El emplazamiento móvil** | **Caravanas, puertos deportivos, vehículos** |

- **LAS DOS COSAS QUE CASI SIEMPRE CAMBIAN** · `[of]` · **el GRADO DE PROTECCIÓN exigido sube** ·
  **aparecen VOLÚMENES o ZONAS con reglas distintas dentro del mismo local.**
- **EL CONCEPTO QUE HAY QUE SABER NOMBRAR** · `[of]` · **la reglamentación de locales singulares no
  regula el LOCAL: regula ZONAS dentro del local** · **lo que se puede instalar a un metro de una
  bañera y a tres no es lo mismo, y el local es el mismo.**

## Locales de pública concurrencia

- **POR QUÉ ES LA MÁS IMPORTANTE PARA UNA CORPORACIÓN AUDIOVISUAL** · `[of]` · **un plató con público,
  un auditorio, un estudio de radio con invitados y hasta un aparcamiento cubierto de más de cinco
  vehículos entran en ella.**

| Familia | Cuándo entra |
|---|---|
| **Espectáculos y actividades recreativas** | **Cualquiera que sea su capacidad**: cines, teatros, auditorios, estadios, pabellones, salas de fiesta, discotecas |
| **Reunión, trabajo y usos sanitarios** | **Unos, con cualquier ocupación** —templos, museos, salas de conferencias y congresos, hoteles, bares, aeropuertos, estaciones, **estacionamientos cerrados y cubiertos para más de 5 vehículos**, hospitales, asilos, guarderías—; **otros, si la ocupación pasa de 50 personas** —bibliotecas, centros de enseñanza, comercios, **oficinas con público**, gimnasios, salas de exposiciones, centros culturales— |

- **LA REGLA DE CÁLCULO, MUY PREGUNTABLE** · `[BOE]` · **ITC-BT-28, apartado 1: la ocupación prevista
  de los locales se calculará como 1 persona por cada 0,8 m2 de superficie útil, a excepción de
  pasillos, repartidores, vestíbulos y servicios.**
- **DÓNDE HAY QUE FIJARSE** · `[of]` · **en la EXCEPCIÓN**: **pasillos, repartidores, vestíbulos y
  servicios NO cuentan**, porque **son superficie de paso y no de estancia.**
- **LA CLÁUSULA QUE AMPLÍA MUCHO** · `[BOE]` · **se aplica además a todos los locales no contemplados
  antes cuando tengan capacidad de ocupación de MÁS DE 100 PERSONAS.**

## Los servicios de seguridad

- **QUÉ SON** · `[BOE]` · **alumbrados de emergencia, sistemas contra incendios, ascensores y otros
  servicios urgentes indispensables**, fijados por las reglamentaciones específicas de las autoridades
  competentes.
- **LA CLASIFICACIÓN POR DURACIÓN DE CONMUTACIÓN** · `[BOE]` · **ITC-BT-28, apartado 2: sin corte,
  alimentación automática asegurada de forma continua durante el periodo de transición · con corte muy
  breve, disponible en 0,15 segundos como máximo · con corte breve, en 0,5 segundos como máximo · con
  corte mediano, en 15 segundos como máximo · con corte largo, en más de 15 segundos.**

| Categoría | Qué tecnología la cumple |
|---|---|
| **Sin corte** | **Alimentación ininterrumpida en línea** (tema 12) |
| **Corte muy breve** | **Conmutación estática** |
| **Corte breve** | Conmutación rápida |
| **Corte mediano** | **Un grupo electrógeno bien arrancado** (tema 11) |
| **Corte largo** | **Un grupo que tarda más, o puesta en marcha manual** |

- **LA CONCLUSIÓN DEL PUNTO** · `[of]` · **ningún grupo electrógeno cumple «sin corte» ni «corte muy
  breve», porque tiene que ARRANCAR** · **lo que da continuidad es la batería; lo que da autonomía es
  el combustible** · **una instalación crítica necesita las dos encadenadas.**
- **LAS FUENTES ADMITIDAS** · `[BOE]` · **baterías de acumuladores, generadores independientes y
  derivaciones separadas de la red de distribución efectivamente independientes de la alimentación
  normal.**
- **LAS CUATRO CONDICIONES** · `[BOE]` · **emplazamiento accesible SÓLO a personas cualificadas o
  expertas** · **emplazamiento VENTILADO**, sin que gases y humos lleguen a locales accesibles · **no
  se admiten derivaciones separadas de red pública salvo que se asegure que las dos no pueden fallar a
  la vez** · **una sola fuente para seguridad NO vale para otros usos**; **con varias sí se comparte**,
  si **al fallar una la potencia restante basta para todos los servicios de seguridad.**
- **LA CUARTA ES LA QUE MÁS SE INCUMPLE** · `[of]` · **un grupo comprado para la seguridad al que se le
  cuelgan cargas de confort deja de garantizarla** · **la manera correcta de compartirlo es con
  DESLASTRE automático.**
- **EL UMBRAL DE ARRANQUE, DATO MUY CONCRETO** · `[BOE]` · **la fuente propia se pone en funcionamiento
  al faltar la tensión de los suministros de la distribuidora, o cuando descienda por debajo del 70 %
  de su valor nominal.**

## El alumbrado de emergencia

| Tipo | Para qué |
|---|---|
| **De SEGURIDAD** | **Para EVACUAR o evitar el pánico y los riesgos** |
| **De REEMPLAZAMIENTO** | **Para que la ACTIVIDAD continúe** |

| Subtipo del de seguridad | Qué asegura |
|---|---|
| **EVACUACIÓN** | **Que se vean e identifiquen las vías de salida** |
| **AMBIENTE o ANTIPÁNICO** | **Que se evite el pánico y se llegue a las vías** |
| **ZONAS DE ALTO RIESGO** | **Que se interrumpan con seguridad los procesos peligrosos** antes de salir |

- **LA DIFERENCIA QUE CASI NADIE ENUNCIA** · `[of]` · **el de seguridad sirve para IRSE; el de
  reemplazamiento, para QUEDARSE** · **un quirófano y un control de emisión piden el segundo; un
  pasillo, el primero.**
- **LAS DOS FORMAS DE ALIMENTARLO** · `[of]` · **aparatos AUTÓNOMOS, con batería en cada luminaria** —
  **mantenimiento luminaria a luminaria**— o **luminarias de FUENTE CENTRAL** —**concentra las baterías
  y exige cable resistente al fuego.**

## Instalaciones automatizadas

| Nivel | Qué gobierna | Cómo se llama |
|---|---|---|
| **Vivienda** | **Confort, energía, seguridad y comunicaciones** | **Domótica** |
| **Edificio** | **Las instalaciones de un edificio o complejo** | **Inmótica o gestión técnica** |
| **Proceso industrial** | **Una máquina o una línea** | **Automatización industrial** |

| Elemento | Qué hace |
|---|---|
| **Sensores** | **Miden o detectan** (tema 4) |
| **Actuadores** | **Ejecutan**: relés, contactores, válvulas, variadores |
| **Controladores** | **Deciden**: autómatas programables, controladores libres |
| **Red o bus** | **Comunica** |
| **Supervisión** | **Muestra y registra** |

| Arquitectura | Cómo es | Qué aporta |
|---|---|---|
| **CENTRALIZADA** | **Un controlador con toda la lógica y todo cableado a él** | **Sencilla y barata en instalaciones pequeñas** |
| **DISTRIBUIDA** | **Varios dispositivos con lógica propia sobre un bus** | **Sigue funcionando si cae uno**; crece bien |

- **LA REGLA QUE DECIDE ENTRE LAS DOS** · `[of]` · **cada nivel debe seguir funcionando si el de arriba
  desaparece** · **un edificio cuya iluminación se apaga porque cayó el servidor de supervisión está
  mal diseñado**, y **la solución no es un servidor mejor: es que el mando local no dependa de él.**
- **EL AVISO DE SEGURIDAD, CON CONSECUENCIA FÍSICA** · `[of]` · **un control de instalaciones en la
  misma red que la ofimática pone cuadros, calderas y grupos a un clic de quien abra un correo
  malicioso** · **la separación de redes no es comodidad: es seguridad.**
- **LA INSTRUCCIÓN QUE SÍ EXISTE** · `[of]` · **la ITC-BT-51**, de sistemas de automatización, gestión
  técnica de la energía y seguridad para viviendas y edificios, **nombrada por lo que regula y no
  citada.**

## Lo singular en una casa que emite

| Emplazamiento | Qué instrucción lo alcanza | Qué le exige |
|---|---|---|
| **Plató y auditorio** | **La de pública concurrencia** | **Servicios de seguridad, emergencia, prescripciones de espectáculos** |
| **Aparcamiento cubierto de más de cinco vehículos** | **La misma** | Lo mismo, y **proyecto sin límite de potencia con ventilación forzada** |
| **Talleres de decorados, con pinturas y disolventes** | **La de riesgo de incendio o explosión** | **Clasificación de zonas y material adecuado** |
| **Instalaciones temporales, ferias y eventos** | **La de instalaciones temporales** | **Régimen documental propio** (tema 13) |

- **LA CONCLUSIÓN DE MÉTODO** · `[of]` · **la pregunta correcta no es «¿qué dice el reglamento?» sino
  «¿QUÉ INSTRUCCIÓN PARTICULAR le alcanza?»** · **aplicar sólo la general a un local que tiene la suya
  es el error de proyecto más caro del oficio.**

## Aviso de estudio

- **LO QUE NO SE DA** · `[of]` · **ni grados de protección por local, ni dimensiones de volúmenes de
  baños y piscinas, ni niveles de iluminación de emergencia, ni autonomías** · **están en las tablas de
  las instrucciones particulares y, los de iluminación, en el Código Técnico.**
- **LAS CIFRAS QUE SÍ SE DAN** · `[BOE]` · **1 persona por cada 0,8 m² con su excepción**, **0,15 · 0,5
  · 15 segundos** y **el 70 % de la tensión nominal como umbral de arranque.**
- **LA SEGUNDA MITAD VA COMO OFICIO** · `[of]` · **ninguna documentación de fabricante de autómatas,
  buses o supervisión**, y **ningún producto ni protocolo nombrado por su marca.**
