# Esquema · Tema 6 del específico de Técnica de Equipos, Instalaciones y Sistemas Eléctricos · Instalaciones de enlace y centros de transformación

Telegrama. **Cada línea lleva delante de dónde sale**: `[BOE]` = instrucción técnica citada
literalmente en el tema · `[of]` = oficio de instalaciones · `[norma]` = otro reglamento, nombrado y no
citado · `[plan]` = enunciado del anexo. **Siglas**: el reglamento electrotécnico para baja tensión
(**REBT**) y sus instrucciones (**ITC-BT-10** a **ITC-BT-18**); la caja general de protección
(**CGP**); la línea general de alimentación (**LGA**); la derivación individual (**DI**); el
interruptor de control de potencia (**ICP**); el interruptor general automático (**IGA**); el
reglamento de instalaciones eléctricas de alta tensión (**RAT**); el kilovoltio (**kV**) y el
kilovoltamperio (**kVA**); y el centro de transformación (**CT**).

**Cabecera.** Enunciado: punto 6 del anexo · **la clave de estudio, antes de nada**: **el enunciado
junta dos cosas que están en DOS REGLAMENTOS DISTINTOS.**

| Mitad | Qué reglamento la gobierna |
|---|---|
| **ENLACE** | **El de BAJA tensión**, instrucciones ITC-BT-11 a ITC-BT-17 |
| **CENTROS DE TRANSFORMACIÓN** | **El de ALTA tensión**, Real Decreto 337/2014, y el de líneas de alta tensión |

- **DÓNDE ESTÁ LA FRONTERA** · `[of]` · **el centro de transformación es la puerta por la que la alta
  entra en la casa; el enlace es lo que distribuye la baja desde ahí** · **uno acaba donde empieza el
  otro.**
- **EL CASO DE UNA CORPORACIÓN AUDIOVISUAL** · `[of]` · **un centro de producción grande NO se alimenta
  de la baja tensión de la calle: tiene su PROPIO centro de transformación** · **eso mueve el origen de
  la instalación interior** —con la caída del tema 5— **y mete a la ocupación en el reglamento de alta.**

<!-- indice -->

## Índice

- [Qué es una instalación de enlace](#qué-es-una-instalación-de-enlace)
- [Los esquemas de enlace](#los-esquemas-de-enlace)
- [Las partes, una a una](#las-partes-una-a-una)
- [El centro de transformación](#el-centro-de-transformación)
- [Aviso de estudio](#aviso-de-estudio)

<!-- /indice -->

## Qué es una instalación de enlace

- **LA DEFINICIÓN** · `[BOE]` · **ITC-BT-12, apartado 1.1: se denominan instalaciones de enlace
  aquellas que unen la caja general de protección o cajas generales de protección, incluidas éstas, con
  las instalaciones interiores o receptoras del usuario · comenzarán, por tanto, en el final de la
  acometida y terminarán en los dispositivos generales de mando y protección · se situarán y
  discurrirán siempre por lugares de uso común y quedarán de propiedad del usuario, que se
  responsabilizará de su conservación y mantenimiento.**
- **TRES COSAS QUE HAY QUE LEER AHÍ** · `[of]` · **dónde EMPIEZA y ACABA**: **al final de la acometida
  —caja general incluida— y en los dispositivos generales de mando y protección** · **por dónde VA**:
  **siempre por lugares de USO COMÚN** —**una derivación que atraviesa la vivienda de otro no
  cumple**— · **de quién ES**: **del USUARIO**, que responde de conservación y mantenimiento, **y la
  acometida es de la distribuidora** —**la frontera de propiedad es lo primero que hay que saber ante
  una avería.**

| Parte | Qué es |
|---|---|
| **Caja general de protección** | **Fusibles de la línea general** y **final de la acometida** |
| **Línea general de alimentación** | **De la caja general a la centralización de contadores** |
| **Elementos de ubicación de contadores** | **La centralización o el armario de medida** |
| **Derivación individual** | **De los contadores al cuadro de cada usuario** |
| **Caja del interruptor de control de potencia** | El alojamiento del limitador |
| **Dispositivos generales de mando y protección** | **El cuadro del usuario**, donde acaba el enlace |

- **LA CONFUSIÓN CLÁSICA** · `[of]` · **la ACOMETIDA no es enlace**: **es la parte de la red de
  distribución que alimenta la caja general**, y **es de la distribuidora** · **tipos**: **aérea posada
  sobre fachada, aérea tensada sobre poste, subterránea y aero-subterránea.**

## Los esquemas de enlace

| Esquema | Cuándo | Cómo es |
|---|---|---|
| **UN SOLO usuario** | **Vivienda unifamiliar, nave, centro con un solo suministro** | **Caja general y equipo de medida en una sola envolvente** y **NO existe línea general** |
| **MÁS DE UN usuario** | Edificios de viviendas, locales, oficinas | **Caja general, línea general, centralización y una derivación por usuario** |

- **LO QUE UN EXAMEN PUEDE PEDIR** · `[of]` · **con un solo usuario la línea general DESAPARECE**,
  porque **no hay nada que repartir** · **la caja de protección y medida hace las dos funciones y la
  derivación individual sale de ella.**
- **LAS TRES VARIANTES DEL SEGUNDO** · `[BOE]` · **contadores para dos usuarios alimentados desde el
  mismo lugar**, **centralización en UN lugar** y **centralización en MÁS DE UN lugar.**

## Las partes, una a una

| Caja general de protección | Cómo |
|---|---|
| **Qué contiene** | **Fusibles de la línea general**, uno por fase |
| **Dónde se sitúa** | **Fachada o nicho**, **de libre y permanente acceso**, lo más cerca de la red |
| **De quién es** | **La instalación, del usuario; la maniobra de sus fusibles, de la distribuidora** |

- **EL RASGO DE LA LÍNEA GENERAL QUE SE PREGUNTA** · `[of]` · **NO lleva protección propia en su origen
  distinta de los fusibles de la caja general** · **por eso se dimensiona para la máxima demanda
  prevista de todo el edificio.**
- **LAS CUATRO UNIDADES FUNCIONALES DE LA CENTRALIZACIÓN** · `[BOE]` · **interruptor general de
  maniobra, embarrado general y fusibles de seguridad, medida, y embarrado de protección y bornes de
  salida** · **el local o armario, accesible desde zona común y dedicado a esto.**
- **LOS DOS RASGOS DE LA DERIVACIÓN INDIVIDUAL** · `[of]` · **es INDIVIDUAL**: **una por usuario, sin
  derivaciones intermedias** · **lleva SIEMPRE conductor de PROTECCIÓN**, además de fases y neutro, **y
  un hilo de mando para tarificación cuando se requiere** · **discurre por zona común, en tubo o canal
  que permita retirar y reponer los cables, con registros en cada planta.**

| Dispositivo general | Qué hace |
|---|---|
| **Interruptor general automático** | **Corte omnipolar y protección de la derivación**; **es del usuario** |
| **Interruptor diferencial** | **Contactos indirectos**, uno o varios |
| **Automáticos de cada circuito** | **Protección de cada línea interior** |
| **Protector de sobretensiones**, cuando procede | Transitorias y permanentes |

- **LOS DOS QUE SE CONFUNDEN** · `[of]` · **el de CONTROL DE POTENCIA limita la potencia CONTRATADA y
  es de la distribuidora; el GENERAL AUTOMÁTICO protege la instalación y es del usuario** · **uno es de
  facturación y el otro de seguridad.**

## El centro de transformación

- **AQUÍ CAMBIA EL REGLAMENTO** · `[norma]` · **un centro de transformación es instalación de ALTA
  tensión** y **se rige por el Real Decreto 337/2014 y sus instrucciones**, **no por el de baja.**

| Parte, de la entrada a la salida | Qué es |
|---|---|
| **Celdas de LÍNEA** | **Reciben la alta tensión** y permiten seccionar |
| **Celda de PROTECCIÓN del transformador** | **Interruptor-seccionador y fusibles, o interruptor automático** |
| **Celda de MEDIDA**, si la medida es en alta | Transformadores de tensión y de intensidad |
| **TRANSFORMADOR** | **De potencia**, en aceite o seco |
| **Cuadro de BAJA tensión** | **Salidas protegidas hacia la instalación** |
| **Puestas a TIERRA** | **Dos**: **PROTECCIÓN** de masas y **SERVICIO** del neutro |
| **Servicios auxiliares** | Alumbrado, emergencia, enclavamientos |

- **POR QUÉ SON DOS TIERRAS Y SE SEPARAN** · `[of]` · **la de protección recoge las masas del centro;
  la de servicio es la del neutro de baja** · **si se unen, un defecto en alta sube el potencial de la
  tierra de protección** y **ese potencial aparecería en el neutro de toda la baja** · `[BOE]` · **la
  instrucción de puesta a tierra dedica un apartado a esa SEPARACIÓN.**

| Tipo por emplazamiento | Dónde |
|---|---|
| **Intemperie sobre apoyo** | Pequeñas potencias, medio rural |
| **EDIFICIO prefabricado** | Vía pública y polígonos |
| **LOCAL integrado en el edificio** | **El caso de un centro de trabajo grande** |
| **SUBTERRÁNEO** | Suelo urbano denso |

| Régimen | Quién lo explota |
|---|---|
| **De COMPAÑÍA** | **La distribuidora**, que entrega en baja |
| **De ABONADO** | **El titular**, que recibe en alta |

- **LAS TRES CONSECUENCIAS DE TENER CENTRO PROPIO** · `[of]` · **el titular responde del mantenimiento,
  con revisiones e inspecciones** (tema 9) · **el origen de la instalación interior se traslada a la
  SALIDA del transformador**, con el 4,5 y el 6,5 por ciento del tema 5 · **los trabajos allí son
  trabajos en ALTA TENSIÓN**, con personal cualificado y autorizado (tema 14).
- **LOS ENCLAVAMIENTOS, APLICACIÓN MÁS ESTRICTA DEL TEMA 3** · `[of]` · **la secuencia de maniobra está
  impuesta FÍSICAMENTE por cerraduras y varillas** · **no se abre la celda del transformador sin haber
  puesto antes a tierra**, ni **se cierra el seccionador de tierra con el interruptor cerrado** · **el
  enclavamiento no es una recomendación: es una pieza de metal que impide el orden equivocado.**

## Aviso de estudio

- **LO QUE ESTE TEMA NO CITA** · `[of]` · **el Real Decreto 337/2014 y el 223/2008 se NOMBRAN y no se
  citan**: **están volcados y citados en el temario de Ingeniería Técnica · Industrial** · **aquí no se
  les atribuye ninguna cifra ni prescripción concreta.**
- **LO QUE NO SE DA** · `[of]` · **ninguna sección mínima, ninguna previsión de cargas, ningún
  coeficiente de simultaneidad, ninguna distancia y ninguna resistencia de tierra.**
