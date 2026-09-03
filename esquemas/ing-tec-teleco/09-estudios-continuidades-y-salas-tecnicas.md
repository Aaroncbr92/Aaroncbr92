# Esquema · Tema 9 del específico de Ingeniería Técnica · Telecomunicación · Estudios, continuidades y salas técnicas

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de instalación audiovisual ·
`[plan]` = enunciado del propio anexo. **Siglas**: la interfaz digital serie (**SDI**); el protocolo de
internet (**IP**); el sistema de alimentación ininterrumpida (**SAI**); la calefacción, ventilación y
aire acondicionado (**HVAC**); el protocolo de tiempo de precisión (**PTP**); y el multiplexado digital
de iluminación (**DMX512**).

**Cabecera.** Enunciado: puntos 11, 12 y 13 del anexo, reunidos porque **son la misma frase con el
nombre de la sala cambiado** · **cero preguntas: el mayor bloque a cero de la ocupación** · **son la
mitad práctica del oficio**: lo que piden es saber DIBUJAR una instalación, y **eso es lo que un examen
escrito no sabe preguntar bien.**

<!-- indice -->

## Índice

- [Lo común a las tres salas](#lo-común-a-las-tres-salas)
- [El estudio y su control](#el-estudio-y-su-control)
- [La continuidad](#la-continuidad)
- [Controles y salas técnicas](#controles-y-salas-técnicas)
- [Sincronización y referencia](#sincronización-y-referencia)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Lo común a las tres salas

| Palabra del enunciado · `[plan]` | Qué hay que saber decir |
|---|---|
| **Equipamiento** | **Qué aparatos hay y para qué está cada uno** |
| **Diagrama a bloques** | **Cómo se dibujan y en qué orden va la señal** |
| **Interconexión** | **Qué conecta con qué, y por qué medio** |
| **Sincronización** | **De dónde sale el tiempo** |
| **Referencia** | **Contra qué se mide y se ajusta** |

| Capa | Qué resuelve |
|---|---|
| **Alimentación** | **Corriente, con respaldo y protección diferencial** |
| **Climatización** | **Sacar el calor que el equipo genera** |
| **Señal** | **Vídeo y audio, por matriz o por red** |
| **Sincronización** | **La referencia común de tiempo** |
| **Control y datos** | **La red que configura, supervisa y ordena** |

- **EL PRINCIPIO QUE ORDENA LAS CINCO** · `[of]` · **Cada capa se diseña para que su fallo no arrastre a
  las demás.** **Una sala bien hecha aguanta un corte de red de datos sin perder la señal, y un fallo
  de climatización sin perder la alimentación.**

## El estudio y su control

| Espacio | Qué hay |
|---|---|
| **El plató** | **Cámaras, iluminación, escenografía, sonido de escena, retornos** |
| **El control** | **Realización, sonido, iluminación y a veces grafismo** |

- **EL DIAGRAMA A BLOQUES, EN ORDEN** · `[of]` · **Las cámaras entran por sus unidades de control** ·
  **las señales pasan por matriz o por red** · **el mezclador elige el programa y hace transiciones y
  efectos** · **el grafismo se incrusta, antes o después según el diseño** · **la salida de programa va
  a emisión, a grabación y a los retornos de plató.**

| Señal de vuelta | Para qué |
|---|---|
| **Retorno de programa** | **Que en plató se vea lo que sale** |
| **Retorno de cámara** | **Que el operador vea su propia señal ajustada** |
| **Intercomunicación y orden** | **Que el realizador hable con cada puesto** |

- **EL ERROR DE DISEÑO MÁS FRECUENTE** · `[of]` · **Olvidar el retorno y la intercomunicación.** **La
  señal de ida se dibuja siempre; la de vuelta se olvida**, y sin ella **el plató no funciona aunque la
  imagen sea perfecta.**
- **LAS UNIDADES DE CONTROL DE CÁMARA** · `[of]` · **Son la mitad del control que no se ve**: ahí se
  ajusta **diafragma, negro, equilibrio de blancos y matriz de color de cada cámara**, y **de ahí sale
  que las cuatro cámaras de un plató parezcan la misma.** **Es trabajo de un técnico dedicado, no del
  realizador.**

## La continuidad

- **QUÉ ES** · `[of]` · **La sala desde la que sale el canal.** **Su trabajo es que la emisión no se
  interrumpa nunca**, y su diseño lo gobierna eso.
- **EL DIAGRAMA A BLOQUES** · `[of]` · **Fuentes** —servidores de emisión, estudios, exteriores, cartón
  de reserva— · **matriz o conmutación de emisión** · **mezclador de continuidad** · **inserción de
  identidad**: mosca, cortinillas, sobreimpresiones · **procesado final**: sonoridad y legalización de
  niveles · **salida a difusión, duplicada.**

| Principio | Qué obliga |
|---|---|
| **Redundancia en toda la cadena** | **Dos de todo lo que puede fallar, y conmutación automática** |
| **Cartón de reserva** | **Algo que emitir si todo cae**: nunca negro |
| **Supervisión permanente** | **Alarmas de ausencia de vídeo, de audio y de nivel** |

- **LA DIFERENCIA DE MENTALIDAD** · `[of]` · **En un estudio un fallo estropea una grabación; en
  continuidad se ve en toda España.** **Una continuidad se diseña suponiendo que las cosas van a
  fallar.**
- **LA PIEZA MÁS HUMILDE Y MÁS IMPORTANTE** · `[of]` · **El detector de ausencia de señal**: vigila la
  salida y **conmuta automáticamente al respaldo si hay negro o silencio unos segundos.** **No mejora
  nada cuando todo va bien; es lo único que sirve cuando algo va mal.**

## Controles y salas técnicas

- **QUÉ LAS DIFERENCIA** · `[of]` · **No producen ni emiten**: **encaminan, miden, procesan y guardan.**

| Sala | Qué contiene |
|---|---|
| **Control central** | **Matriz principal, referencia, supervisión de toda la casa** |
| **Sala de equipos** | **Bastidores: servidores, procesadores, conversores, alimentación** |
| **Sala de intercambios** | **Lo que entra y sale del centro**: satélite, fibra, agencias |
| **Sala de medida** | **Instrumentos y puesto de comprobación** |

- **LOS CUATRO CRITERIOS DE UNA SALA DE EQUIPOS** · `[of]` · **Bastidores accesibles por delante y por
  detrás**, con pasillo de servicio · **reparto de calor por pasillo frío y pasillo caliente**, no por
  temperatura media · **canalizaciones separadas para alimentación y para señal**, y cruces
  perpendiculares donde coincidan · **etiquetado en los dos extremos de todos los latiguillos**, con
  documentación actualizada.
- **POR QUÉ EL CUARTO ES TÉCNICO Y NO ADMINISTRATIVO** · `[of]` · **Una instalación sin etiquetar no se
  puede reparar deprisa**, y **reparar deprisa es lo que se pide a las tres de la madrugada.**
- **LA OBSERVACIÓN** · `[of]` · **Las salas técnicas son las que nadie visita y las que deciden si la
  casa funciona.** **Su diseño es el trabajo más propio de esta ocupación.**

## Sincronización y referencia

| Concepto | Qué es |
|---|---|
| **Sincronización** | **Que todas las fuentes empiecen cada cuadro en el mismo instante** |
| **Referencia** | **La señal común contra la que todos se alinean** |

- **POR QUÉ HACE FALTA** · `[of]` · **Conmutar entre dos fuentes no sincronizadas produce un salto.**
  **Bloqueadas a la misma referencia, la conmutación es limpia.**
- **LA CADENA DE REFERENCIA** · `[of]` · **Un generador maestro, con respaldo y conmutación
  automática** · **distribución hasta cada sala** · **en cada equipo, entrada de referencia y ajuste de
  fase.**

| Fuente sin referencia: solución | Qué hace | Qué cuesta |
|---|---|---|
| **Sincronizador de cuadro** | **Guarda un cuadro y lo lee al ritmo de la casa** | **Un cuadro de retardo** |
| **Bloquear la fuente remota** | **Que llegue ya alineada** | **Referencia común en los dos extremos** |

- **SOBRE RED** · `[of]` · **La referencia es el protocolo de tiempo de precisión, y el principio no
  cambia**: sigue habiendo maestro, distribución y **la obligación de comprobar que llega a todas
  partes.**

## Lo que se ha preguntado

- **NINGUNA PREGUNTA.**
- **LO RAZONABLEMENTE PREGUNTABLE** · `[of]` · **El diagrama a bloques de un control de realización**,
  **los tres principios de una continuidad** y **la cadena de referencia.**
- **LA ADVERTENCIA** · `[of]` · **Si el examen siguiente decide entrar por aquí, tiene TRES puntos del
  anexo para hacerlo.**
