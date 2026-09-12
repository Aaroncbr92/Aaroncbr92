# Esquema · Tema 7 del específico de Ingeniería Superior · Telecomunicación · La televisión digital terrestre

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de difusión terrestre ·
`[plan]` = enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: la
televisión digital terrestre (**TDT**); el megahercio (**MHz**) y el gigahercio (**GHz**); y la
multiplexación ortogonal por división en frecuencia (**OFDM**), presentada en el tema 3.

**Cabecera.** Enunciado: punto 7 del anexo · **una pregunta** · **sin norma del boletín**: los
estándares de difusión son normas europeas de un organismo de normalización que este proyecto no ha
consultado.

**La idea que lo ordena** · `[of]` · **Todo el punto se explica por el INTERVALO DE GUARDA.** **De él
salen la inmunidad a los ecos, la red de frecuencia única, el dividendo digital y el efecto de
acantilado.**

<!-- indice -->

## Índice

- [La cadena](#la-cadena)
- [La codificación de canal](#la-codificación-de-canal)
- [La modulación de muchas portadoras](#la-modulación-de-muchas-portadoras)
- [Las redes de frecuencia única](#las-redes-de-frecuencia-única)
- [Bandas y planificación](#bandas-y-planificación)
- [La recepción](#la-recepción)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## La cadena

| Eslabón | Qué hace |
|---|---|
| **codificación y multiplexado** | **forma el flujo con varios programas: tema 6** |
| **distribución primaria** | **lleva el múltiplex del centro de producción a los emisores** |
| **codificación de canal** | **añade redundancia y desordena** |
| **modulación** | **reparte los datos entre miles de portadoras** |
| **amplificación y radiación** | **sube potencia y entrega al sistema radiante: tema 23** |
| **recepción** | **antena, sintonizador, demodulador y descodificador** |

- **LA DISTINCIÓN QUE EL ENUNCIADO PIDE** · `[plan]` · **La distribución primaria transporta el
  múltiplex y no la ve nadie; la difusión lo radia al espectador.** **La primera va por fibra,
  radioenlace o satélite y prima la disponibilidad**: **si cae, se cae la emisión de una región
  entera.**

## La codificación de canal

| Operación | Contra qué protege |
|---|---|
| **aleatorización** | **contra rachas de bits iguales**, que concentrarían energía en frecuencias sueltas |
| **corrección de errores hacia delante** | **contra el ruido**: se arregla sin pedir repetición |
| **entrelazado** | **contra los errores EN RÁFAGA** |

- **EL CONCEPTO CONTRAINTUITIVO** · `[of]` · **Un código corrector arregla bien errores dispersos y mal
  errores agrupados**, y **el canal terrestre produce agrupados.** **El entrelazado reparte los bits de
  cada bloque a lo largo del tiempo**, de modo que **una ráfaga sólo estropea unos pocos bits de cada
  bloque.** **El entrelazado no corrige nada: convierte errores incorregibles en corregibles.**
- **la tasa de código** · `[of]` · **Dice cuántos bits del bloque son de información y cuántos de
  redundancia.** **Más redundancia, más robustez y menos capacidad útil.**

## La modulación de muchas portadoras

- **las tres consecuencias** · `[of]` · **1)** repartir la tasa entre miles de portadoras hace que
  **cada símbolo dure muchísimo**; **2)** eso permite el **intervalo de guarda** —antes de cada símbolo
  se emite una copia de su final y el receptor la descarta—; **3)** un **desvanecimiento selectivo**
  sólo tumba unas portadoras, y **la corrección reconstruye lo que llevaban.**
- **LA PREGUNTA MÁS CONTRAINTUITIVA DEL PUNTO** · `[exam]` · **Señal directa más reflejo de un edificio
  cercano: la imagen se ve NÍTIDA.** **La doble imagen fantasma era un artefacto ANALÓGICO.** **En
  digital, un eco cercano llega dentro de la guarda, se descarta y su energía SUMA a la de la directa.**
- **el límite** · `[of]` · **Un eco que llegue más tarde que la guarda sí interfiere**, y **entonces la
  señal cae de golpe.** **La difusión digital no se degrada poco a poco: aguanta perfecta hasta un
  punto y se desploma.** **Es el efecto de acantilado**, y **hace la planificación más exigente, no
  menos.**

## Las redes de frecuencia única

| | **Frecuencia múltiple** | **Frecuencia única** |
|---|---|---|
| **Cómo es** | **cada emisor, un canal** | **todos los emisores, el mismo canal** |
| **Por qué** | **en analógico era obligatorio** | **en digital el emisor vecino se comporta como un eco** |
| **Qué exige** | **un canal por emisor y sus guardas** | **misma frecuencia, mismo instante y mismo contenido** |
| **Qué ahorra** | **nada** | **ESPECTRO**: es lo que permitió el dividendo digital |
| **Qué complica** | **la planificación de frecuencias** | **la planificación de RETARDOS** |

- **la frase que lo resume** · `[of]` · **Un emisor lejano no es una interferencia: es un eco.**
  **Mientras llegue dentro de la guarda, suma; si llega fuera, interfiere.** **Por eso la guarda se
  elige por la DISTANCIA entre emisores, y una red grande necesita guardas largas, que cuestan
  capacidad.**
- **el intercambio** · `[of]` · **Capacidad, robustez y tamaño de red se reparten un presupuesto
  fijo.** **No hay ajuste bueno en abstracto: hay el que corresponde a una cobertura y a un objetivo de
  servicios.**

## Bandas y planificación

- **la escalera de décadas** · `[of]` · **Cada escalón multiplica por diez**: **de 3 a 30 MHz,
  decamétricas; de 30 a 300, muy altas; de 300 a 3.000, ultraaltas —la banda de la televisión
  terrestre—; de 3 a 30 GHz, superaltas; de 30 a 300, extremadamente altas.**

| Concepto | Qué es |
|---|---|
| **canal** | **la rejilla en que se reparte la banda**: un múltiplex ocupa un canal |
| **cobertura** | **el porcentaje de ubicaciones y de tiempo con calidad de servicio** |
| **relación de protección** | **cuánta señal deseada hace falta frente a una interferente** |
| **dividendo digital** | **el espectro que la difusión libera al pasar a digital** |

- **la observación de servicio** · `[of]` · **La televisión terrestre es el único medio que llega a todo
  el mundo sin contrato, sin conexión y sin identificación.** **Ésa es la razón de servicio público que
  sostiene la obligación de cobertura**, y **lo que la diferencia del envío bajo demanda por red.**

## La recepción

| Elemento | Qué falla |
|---|---|
| **antena** | **mal orientada, degradada o de banda equivocada** |
| **amplificador de mástil** | **saturado por una señal fuerte: intermodulación** |
| **red del edificio** | **derivadores desadaptados, tomas mal terminadas** |
| **sintonizador y demodulador** | **sensibilidad y selectividad limitadas** |

- **los tres síntomas** · `[of]` · **1) bloques o congelación de golpe** → relación señal a ruido en el
  límite, **que puede ser por exceso de señal y no por defecto**; **2) un múltiplex se ve y otro no** →
  problema selectivo en frecuencia; **3) se ve bien y a ratos no** → interferencia intermitente o
  multitrayecto variable: tráfico, vegetación con viento, propagación anómala.

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 12 | Qué se ve al recibir la señal directa más el reflejo de un edificio cercano | **La imagen nítida** ✔ **·** el eco cae dentro del intervalo de guarda y suma |
