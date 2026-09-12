# Esquema · Tema 16 del específico de Sonido · El audio sobre redes de datos

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de redes de audio · `[norma]` =
norma de organismo técnico · `[plan]` = plantilla oficial. **Siglas**: el protocolo de internet
(**IP**) y el de datagramas de usuario (**UDP**); el protocolo de control de transmisión (**TCP**); el
protocolo de tiempo de precisión (**PTP**, *precision time protocol*); la norma de audio en red de la
Sociedad de Ingeniería de Audio (**AES67**); los megabits por segundo (**Mbps**); el kilohercio
(**kHz**); y **Dante**, que es un nombre comercial y no unas siglas.

**Cabecera.** Enunciado: punto 14 del anexo, «Audio sobre IP» · **9 preguntas: el segundo banco del volumen** ·
**cinco son de Dante, dos de cuentas de ancho de banda, una de protocolo y una de reloj.**

<!-- indice -->

## Índice

- [Qué protocolo lleva el audio](#qué-protocolo-lleva-el-audio)
- [El reloj](#el-reloj)
- [Qué es Dante](#qué-es-dante)
- [La latencia](#la-latencia)
- [Las cuentas de ancho de banda](#las-cuentas-de-ancho-de-banda)
- [La norma abierta: AES67](#la-norma-abierta-aes67)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué protocolo lleva el audio

- **PREGUNTA 7** · `[of]` · **El protocolo que se usa por norma general para audio en red es UDP.**
- **POR QUÉ NO TCP**: **el audio en directo no se puede retransmitir.** **Un paquete que llega tarde
  ya no vale**, porque su instante pasó. **Se prefiere perderlo a esperarlo.**
- **CÓMO SE PROTEGE ENTONCES**: **con redundancia de camino y con corrección de errores hacia
  delante**, no con retransmisión.

## El reloj

- **PREGUNTA 58** · `[norma]` · **Dante sincroniza el reloj mediante el protocolo PTP.**
- **POR QUÉ HACE FALTA**: **todos los equipos tienen que muestrear en el mismo instante.** **Sin reloj
  común, los flujos se desalinean y aparecen clics.**
- **LA CIFRA QUE LO DISTINGUE**: **el PTP trabaja con precisión de microsegundos o mejor**, frente a
  los milisegundos del protocolo de red corriente.

## Qué es Dante

- **PREGUNTA 72** · `[of]` · **Dante es un protocolo que permite la transmisión de señales de audio y
  control a través de una red Ethernet.**
- **PREGUNTA 75** · `[of]` · **Dante permite transmisiones unicast y multicast.**
- **PREGUNTA 76** · `[of]` · **Un conmutador en una red Dante conecta múltiples dispositivos y
  gestiona el tráfico de datos.**
- **LA IDEA QUE UNIFICA LAS TRES**: **Dante es audio y control sobre una red normal.** **No hace falta
  cableado especial: hace falta una red bien configurada.**
- **CUÁNDO SE USA CADA ENVÍO**: **unicast cuando un flujo va a un solo destino; multicast cuando el
  mismo flujo va a varios.** **Mandar por unicast a diez destinos son diez flujos y diez veces el
  ancho de banda.**

## La latencia

- **PREGUNTA 73** · `[of]` · **Con alta latencia en una red Dante se introduce retraso y se afecta a
  la sincronización.**
- **DE QUÉ DEPENDE**: **del número de saltos de conmutador, de la carga de la red y de la latencia
  configurada en cada dispositivo.**
- **LA REGLA DE AJUSTE**: **la latencia se pone tan baja como la red aguante sin perder paquetes**, y
  **la de la red entera es la del dispositivo más lento.**

## Las cuentas de ancho de banda

- **LA FÓRMULA**: **canales × frecuencia de muestreo × bits, más la carga de cabeceras.**
- **PREGUNTA 43** · `[of]` · **32 canales bidireccionales a 48 kHz y 24 bits usan aproximadamente 73
  Mbps.**
- **CÓMO SALE**: **32 × 48.000 × 24 ≈ 36,9 Mbps en un sentido**, y **bidireccional es el doble**: unos
  73.
- **PREGUNTA 47** · `[plan]` · **10 canales en unicast a 48 kHz y 24 bits dan 18 Mbps y 3 flujos.**
- **DE DÓNDE SALEN LOS 3 FLUJOS**: **Dante agrupa hasta cuatro canales por flujo en unicast.** **Diez
  canales piden tres flujos: cuatro, cuatro y dos.**
- **DE DÓNDE SALEN LOS 18 Mbps**: **los diez canales en crudo son 11,5 Mbps** —10 × 1,152—, **y el
  resto es sobrecarga de cabeceras**: **los paquetes de audio en tiempo real son pequeños y
  frecuentes, así que la proporción de cabecera es alta.**
- **POR QUÉ AUN ASÍ DESCANSA EN LA PLANTILLA**: **la agrupación de cuatro canales por flujo es dato de
  implementación del fabricante**, y **el temario declara que no ha consultado su documentación.**

## La norma abierta: AES67

- **PREGUNTA 52** · `[plan]` · **La máxima frecuencia de muestreo de AES67 es 96 kHz.**
- **QUÉ ES AES67**: **la norma que permite que sistemas de fabricantes distintos se entiendan entre
  sí**, frente a los protocolos propietarios.
- **POR QUÉ DESCANSA EN LA PLANTILLA**: **el texto de la norma está tras un muro de pago y el temario
  declara que no lo ha leído.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 7 | Qué protocolo se usa por norma general para audio en red | d) UDP ✔ |
| 43 | Ancho de banda de 32 canales bidireccionales | c) 73 Mbps ✔ |
| 47 | Ancho de banda y flujos de 10 canales en unicast | d) 18 Mbps y 3 flujos ✔ **·** sólo con la plantilla |
| 52 | Máxima frecuencia de muestreo de AES67 | b) 96 kHz ✔ **·** sólo con la plantilla |
| 58 | Con qué protocolo sincroniza Dante el reloj | c) PTP ✔ |
| 72 | Qué es el protocolo Dante | c) Transmisión de audio y control por Ethernet ✔ |
| 73 | Qué ocurre con alta latencia en una red Dante | b) Se introduce retraso y afecta a la sincronización ✔ |
| 75 | Qué permite Dante | a) Transmisiones unicast y multicast ✔ |
| 76 | Qué es un conmutador en una red Dante | a) Conecta varios dispositivos y gestiona el tráfico ✔ |

**Las nueve oficiales son correctas** · **dos descansan sólo en la plantilla.** · **Aviso de
estudio**: **la fórmula del ancho de banda contesta una pregunta entera y media de otra**, y **es la
misma cuenta del tema 9 con otra unidad.**
