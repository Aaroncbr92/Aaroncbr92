# Esquema · Tema 13 del específico de Técnica de Equipos y Sistemas Electrónicos · Equipos de medida y control

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de medida · `[plan]` = plantilla
oficial. **Siglas**: la modulación de amplitud (**AM**) y la de frecuencia (**FM**); la difusión de
vídeo digital terrestre de segunda generación (**DVB-T2**); la señal de reloj (**CLK**); el megahercio
(**MHz**) y el gigahercio (**GHz**); el milivoltio (**mV**); el vatio (**W**) y el kilovatio (**kW**);
la radiofrecuencia (**RF**); el conector coaxial roscado de la serie N; y **RG213U**, que es una
referencia de catálogo de cable coaxial y no unas siglas.

**Cabecera.** Enunciado: punto 15 del anexo · **8 preguntas** · **tres dependen de una figura** · **es
el punto que define el oficio: un técnico de esta ocupación es, antes que nada, alguien que mide.**

<!-- indice -->

## Índice

- [El osciloscopio](#el-osciloscopio)
- [Las dos preguntas de osciloscopio con figura](#las-dos-preguntas-de-osciloscopio-con-figura)
- [El polímetro y la pila](#el-polímetro-y-la-pila)
- [El instrumento que no lo es](#el-instrumento-que-no-lo-es)
- [La medida de potencia en radiofrecuencia](#la-medida-de-potencia-en-radiofrecuencia)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## El osciloscopio

| Mando | Qué gradúa | Unidades |
|---|---|---|
| **Amplitud** | **Eje vertical** | **Voltios por división** |
| **Base de tiempos** | **Eje horizontal** | **Segundos por división** |
| **Disparo** | **Dónde empieza a dibujar** | **Nivel y flanco** |

- **PREGUNTA 73** · `[of]` · **En un osciloscopio de dos canales, la base de tiempos es única para los
  dos.**
- **LA REGLA QUE RESUELVE LA PREGUNTA ENTERA**: **lo que es del eje vertical va por canal; lo que es
  del eje horizontal es común.** **Si cada canal tuviera su base de tiempos, las dos trazas no serían
  comparables y el aparato no serviría para lo único para lo que se compran dos canales.**
- **PREGUNTA 24 del segundo llamamiento** · `[of]` · **Para medir el reloj de un microprocesador entre
  100 MHz y 5 GHz hay que usar una sonda de alta impedancia.**
- **EL PRINCIPIO GENERAL**: **el instrumento forma parte del circuito que mide.** **Una sonda de baja
  impedancia carga el nodo, baja la amplitud y redondea los flancos**: **el equipo se para al poner la
  punta.**

## Las dos preguntas de osciloscopio con figura

- **PREGUNTA 12 del segundo llamamiento** · `[plan]` · **La senoide de la figura, con 200 microsegundos
  por división, tiene 1 kHz.**
- **EL MÉTODO, QUE SÍ SE ESCRIBE ENTERO**: **contar las divisiones de un ciclo · multiplicarlas por la
  escala · la frecuencia es la inversa del periodo.**

| Divisiones por ciclo | Periodo | Frecuencia |
|---|---|---|
| **5** | **1 ms** | **1 kHz** ✔ |
| **2,5** | **500 µs** | **2 kHz** |
| **0,5** | **100 µs** | **10 kHz** |

- **EL DATO DE LOS 500 mV NO INTERVIENE**: **está para comprobar que se sabe que la frecuencia sale del
  eje horizontal.**
- **PREGUNTA 49** · `[plan]` · **La imagen es una señal de radio AM con modulación del 100 %.**
- **LA REGLA DE LA FAMILIA**: **al 100 % la envolvente toca el cero en los mínimos; al 50 % se queda a
  la mitad; por encima del 100 % cruza y se invierte.** **En FM la envolvente es plana y en digital se
  ve como ruido.** **La pregunta se juega entre el 50 y el 100.**

## El polímetro y la pila

| Posición | Qué mide | Cómo se conecta |
|---|---|---|
| **Voltímetro (V)** | **Tensión** | **En paralelo** |
| **Amperímetro (A)** | **Corriente** | **En serie: hay que abrir el circuito** |
| **Ohmímetro (Ω)** | **Resistencia y continuidad** | **Con el circuito sin alimentar** ✔ |
| **Capacitancia (F)** | **Capacidad** | **Con el condensador descargado y fuera** |

- **PREGUNTA 13 del segundo llamamiento** · `[of]` · **Para medir continuidad, el multímetro va en
  ohmímetro.** **Continuidad es que haya camino, y que haya camino es que la resistencia sea casi
  nula.**
- **PREGUNTA 11 del segundo llamamiento** · `[of]` · **La polaridad de un altavoz se averigua conectando
  una pila y observando el movimiento del cono.**
- **POR QUÉ ES INGENIOSA**: **el enunciado prohíbe la fuente de señal, y la pila es el único elemento
  de los cuatro que da corriente sin ser fuente de señal.**
- **PARA QUÉ SIRVE EN LA PRÁCTICA**: **dos altavoces con polaridad opuesta se cancelan en graves.**
  **Es de las averías más difíciles de oír y de las más fáciles de encontrar con una pila.**

## El instrumento que no lo es

- **PREGUNTA 64** · `[of]` · **El que NO se usa en diagnóstico es el «Trompeter».**
- **POR QUÉ**: **es un fabricante de conectores y paneles**, y **un panel de conexiones no diagnostica
  nada: es cableado.**
- **EL INVENTARIO DEL ENUNCIADO, ABREVIADO**: **polímetro** —tensión, corriente, resistencia—;
  **osciloscopio** —forma de onda—; **monitor de forma de onda** —vídeo en el tiempo—;
  **vectorscopio** —crominancia—; **analizador de espectro** —energía por frecuencia—; **medidor de
  campo** —señal recibida—; **vúmetro** —nivel lento—; **picómetro** —nivel de pico—; **vatímetro**
  —potencia—; **medidor de redes de RF**; **medidor de modulación**; **analizador de audio.**
- **LA PAREJA QUE MÁS SE CONFUNDE**: **vúmetro y picómetro.** **El primero dice cómo suena de fuerte;
  el segundo, si va a saturar.**

## La medida de potencia en radiofrecuencia

- **PREGUNTA 19 del segundo llamamiento** · `[plan]` · **La transición necesaria es de 1 5/8" a N
  hembra.**
- **LO QUE SÍ SE RAZONA SIN VER LA FIGURA**: **el cable acaba en N macho por los dos lados y la carga
  tiene N hembra**, luego **el otro extremo necesita por fuerza una N hembra**; **lo único que la
  figura decide es qué conector tiene la salida del equipo.**
- **LAS MEDIDAS SON DIÁMETROS DE LÍNEA COAXIAL RÍGIDA**: **7/8" para cientos de vatios · 1 5/8" para
  unos pocos kilovatios · 3 1/8" y mayores para decenas.**
- **LAS DOS REGLAS DE LA MEDIDA DE POTENCIA**: **la carga tiene que aguantar lo que se le va a meter**
  —aquí 500 vatios contra una carga de 1 kilovatio, el doble de margen— **y nunca se mide un transmisor
  sin carga**, porque la energía reflejada destruye la etapa de salida.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 49 | Qué representa la imagen de osciloscopio | d) AM al 100 % ✔ **·** figura |
| 64 | Instrumento que NO se usa en el diagnóstico | d) Trompeter ✔ |
| 73 | Afirmación correcta sobre un osciloscopio de dos canales | c) La base de tiempos es única ✔ |
| 11 (2.º llam.) | Cómo hallar la polaridad de un altavoz | b) Con una pila ✔ |
| 12 (2.º llam.) | Frecuencia de la senoide de la figura | a) 1 kHz ✔ **·** figura |
| 13 (2.º llam.) | Posición del multímetro para continuidad | d) Ohmímetro ✔ |
| 19 (2.º llam.) | Transición necesaria para medir potencia | a) 1 5/8" a N hembra ✔ **·** figura |
| 24 (2.º llam.) | Sonda para medir el reloj de un microprocesador | b) De alta impedancia ✔ |

**Las ocho oficiales son correctas** · **tres descansan en la plantilla, y son las tres que llevan
figura.** · **Aviso de estudio**: **cinco se contestan con principios que no cambian nunca**, y **las
tres restantes exigen leer una pantalla, que es lo que este oficio hace todos los días.**
