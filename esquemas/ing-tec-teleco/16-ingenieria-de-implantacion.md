# Esquema · Tema 16 del específico de Ingeniería Técnica · Telecomunicación · Ingeniería de implantación

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de ingeniería de implantación ·
`[plan]` = enunciado del propio anexo. **Siglas**: el pliego de prescripciones técnicas (**PPT**); el
acuerdo de nivel de servicio (**ANS**); las pruebas de aceptación de fábrica y de obra (**FAT** y
**SAT**); la interfaz digital serie (**SDI**); el protocolo de internet (**IP**); y el sistema de
alimentación ininterrumpida (**SAI**).

**Cabecera.** Enunciado: punto 20 del anexo · **cero preguntas** · **es el punto que mejor describe lo
que hace de verdad esta ocupación**: **un ingeniero técnico de telecomunicación en una televisión no
opera equipos, los IMPLANTA.**

**Tema compartido.** **El enunciado de este punto es también, palabra por palabra, el punto 26 del
anexo de Ingeniería Superior · Telecomunicación**, así que **este esquema sirve a las dos
ocupaciones.**

<!-- indice -->

## Índice

- [Las siete fases](#las-siete-fases)
- [La documentación](#la-documentación)
- [La ejecución](#la-ejecución)
- [Las pruebas de aceptación](#las-pruebas-de-aceptación)
- [Medidas y control de calidad](#medidas-y-control-de-calidad)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las siete fases

| Fase | Qué produce | Quién decide |
|---|---|---|
| **Análisis de necesidades** | **Qué hace falta y para qué** | **El área usuaria, con el ingeniero** |
| **Anteproyecto** | **Alternativas con coste y plazo** | **El ingeniero propone, la dirección elige** |
| **Proyecto** | **La solución elegida, con planos y mediciones** | **El ingeniero** |
| **Licitación** | **El pliego y la comparación de ofertas** | **Contratación, con criterios técnicos** |
| **Ejecución** | **La instalación montada** | **El adjudicatario, con dirección facultativa** |
| **Pruebas y recepción** | **La aceptación formal** | **El ingeniero** |
| **Explotación** | **El sistema en servicio, con su mantenimiento** | **La operación** |

- **LA REGLA QUE LAS ORDENA** · `[of]` · **Cada fase se cierra antes de abrir la siguiente.** **Empezar
  a montar sin proyecto cerrado es la causa número uno de sobrecoste**, y **el sobrecoste se paga
  siempre en las pruebas, que es cuando aparece lo que no se pensó.**
- **LO QUE SEPARA UN PROYECTO AUDIOVISUAL DE UNO DE OBRA CORRIENTE** · `[of]` · **Hay una fecha que no
  se puede mover**: una temporada, unas elecciones, un acontecimiento. **Eso obliga a planificar con
  hitos intermedios y con margen, no con optimismo.**

## La documentación

| Documento | Qué contiene |
|---|---|
| **Memoria** | **Qué se hace, por qué y con qué criterios** |
| **Pliego de prescripciones técnicas** | **Qué cumple cada elemento, sin nombrar marcas** |
| **Planos** | **Salas, bastidores, canalizaciones, esquemas de bloques** |
| **Esquemas de interconexión** | **Qué conecta con qué, señal a señal** |
| **Mediciones y presupuesto** | **Cuánto de cada cosa y a qué precio** |
| **Planificación** | **Qué se hace cuándo, con sus dependencias** |

- **DONDE UN INGENIERO SE JUEGA EL PROYECTO** · `[of]` · **El pliego describe PRESTACIONES, no
  productos.** **«Un mezclador de la marca tal» excluye competencia y suele ser ilegal en contratación
  pública**; **«un mezclador con al menos veinticuatro entradas, tres canales de efectos y control por
  red» describe lo mismo y admite ofertas.**
- **EL ERROR CONTRARIO, IGUAL DE CARO** · `[of]` · **Un pliego tan abierto que admite una oferta que no
  sirve.** **La medida de un buen pliego: todo lo que lo cumple vale y todo lo que vale lo cumple.**
- **LA DOCUMENTACIÓN MÁS USADA Y PEOR MANTENIDA** · `[of]` · **Los esquemas de interconexión.** **El día
  que alguien cambia un latiguillo y no lo anota, el esquema deja de servir**, y a partir de ahí nadie
  se fía. **Mantenerlo vivo es parte del trabajo.**

## La ejecución

- **LOS CINCO TRABAJOS, EN ORDEN** · `[of]` · **Obra civil y canalizaciones** —bandejas, tubos,
  pasamuros, suelo técnico— · **alimentación** —cuadros, protecciones, sistemas ininterrumpidos, tomas
  en bastidor— · **cableado** —tendido, etiquetado, conectorizado— · **montaje de equipos** —bastidores,
  fijación, ventilación— · **configuración y puesta en marcha** —direcciones, referencias, perfiles.
- **LA REGLA DEL ORDEN** · `[of]` · **Lo que va dentro de la pared va primero.** **Un cable olvidado se
  paga rompiendo obra**, y por eso **se tiende siempre más de lo que hace falta**: el coste del cable es
  despreciable comparado con el de volver.

| Práctica | Por qué |
|---|---|
| **Etiquetar en los dos extremos con el código del esquema** | **Sin eso, localizar una avería es tirar del cable** |
| **Separar canalizaciones de fuerza y de señal** | **Evitar acoplamientos e inducciones** |
| **Dejar reserva en bandejas y bastidores** | **Toda instalación crece, y antes de lo previsto** |

## Las pruebas de aceptación

| Prueba | Dónde | Qué comprueba |
|---|---|---|
| **De fábrica** | **En casa del suministrador** | **Que el equipo cumple el pliego, antes de moverlo** |
| **De obra** | **En destino, ya montado** | **Que el sistema completo funciona en su sitio y con sus señales** |

- **POR QUÉ LA PRIMERA SE PAGA** · `[of]` · **Rechazar un equipo en fábrica cuesta una semana;
  rechazarlo montado cuesta un mes.**
- **EL PUNTO QUE MÁS SE SALTA** · `[of]` · **El protocolo de pruebas se escribe ANTES.** **Si el
  criterio de aceptación se decide después de medir, siempre se acaba aceptando.** **Un protocolo dice
  qué se mide, con qué instrumento, en qué condiciones y qué valor es correcto.**

| Clase de prueba | Qué comprueba |
|---|---|
| **De continuidad y cableado** | **Que cada cable llega donde dice el esquema y con qué pérdida** |
| **De señal** | **Niveles, retardos, jitter, errores** |
| **Funcionales** | **Que cada camino de señal previsto funciona de extremo a extremo** |
| **De carga y de fallo** | **Que aguanta el caso peor y que la redundancia conmuta de verdad** |

- **LA ÚLTIMA ES LA QUE CASI NUNCA SE HACE Y LA QUE PRUEBA LO IMPORTANTE** · `[of]` · **Una redundancia
  que no se ha provocado nunca no se sabe si funciona.**

## Medidas y control de calidad

| Magnitud | Con qué | Qué revela |
|---|---|---|
| **Pérdida y longitud de cada enlace** | **Comprobador de cableado, reflectómetro** | **Empalmes, cables dañados, tiradas fuera de norma** |
| **Jitter y margen digital** | **Diagrama de ojo** | **Enlaces al límite que fallarán con el tiempo** |
| **Niveles y sonoridad** | **Medidores de audio** | **Que la cadena entrega el nivel acordado** |
| **Latencia extremo a extremo** | **Marcas conocidas** | **Retardos acumulados que estorban en directo** |
| **Sincronismo** | **Comparación contra la referencia** | **Fuentes no bloqueadas** |

- **EL PRINCIPIO QUE HAY QUE SABER ENUNCIAR** · `[of]` · **Se mide contra lo que el PLIEGO pedía, no
  contra lo que el equipo da.** **Si el pliego no lo pedía, no se puede exigir; si lo pedía, no se puede
  aceptar sin ello.**
- **LO QUE CIERRA EL CICLO** · `[of]` · **Documentación final de obra**: **planos actualizados a lo
  realmente ejecutado, esquemas, protocolos de prueba firmados, configuraciones guardadas y manuales.**
  **Una instalación sin eso se ha entregado a medias, y el que la mantenga lo pagará.**

## Lo que se ha preguntado

- **NINGUNA PREGUNTA.**
- **LO RAZONABLEMENTE PREGUNTABLE** · `[of]` · **Las siete fases**, **la diferencia entre las dos
  pruebas de aceptación** y **el principio de medir contra el pliego.**
