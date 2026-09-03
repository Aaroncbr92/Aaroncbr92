# Esquema · Tema 5 del específico de Ingeniería Técnica · Telecomunicación · Difusión terrestre y por satélite

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de radiodifusión · `[exam]` =
opciones del propio cuadernillo · `[norma]` = norma técnica nombrada, sin cita literal. **Siglas**: la
televisión digital terrestre (**TDT**); la difusión de vídeo digital terrestre (**DVB-T** y
**DVB-T2**) y por satélite (**DVB-S** y **DVB-S2**); la multiplexación por división de frecuencias
ortogonales codificada (**COFDM**); la modulación de amplitud en cuadratura (**QAM**) y la de
desplazamiento de fase (**PSK**); la modulación de frecuencia (**FM**); el formato de intercambio de
material (**MXF**) y la modulación por desplazamiento mínimo gaussiano (**GMSK**), que aparecen como
opciones falsas; la codificación de vídeo avanzada (**AVC**); el intervalo de guarda (**IG**); el
código de Bose, Chaudhuri y Hocquenghem (**BCH**); y el gigahercio (**GHz**).

**Cabecera.** Enunciado: puntos 5 y 6 del anexo, reunidos porque **sus enunciados son la misma frase
con el medio cambiado** · **3 preguntas, las tres del punto 5** · **del punto 6 no ha caído ninguna
aquí**: la de bandas de satélite va con las antenas.

<!-- indice -->

## Índice

- [Los dos medios frente a frente](#los-dos-medios-frente-a-frente)
- [La modulación terrestre](#la-modulación-terrestre)
- [Las dos generaciones terrestres](#las-dos-generaciones-terrestres)
- [La modulación por satélite](#la-modulación-por-satélite)
- [La distribución primaria](#la-distribución-primaria)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los dos medios frente a frente

| | **Terrestre** | **Satélite** |
|---|---|---|
| **Qué estorba** | **Los ecos: la señal llega por varios caminos** ✔ | **La lluvia y el ruido térmico: señal muy débil** |
| **Modulación** | **Multiportadora, con intervalo de guarda** ✔ | **Monoportadora, por fase** |
| **Ancho de banda por canal** | **8 megahercios** | **Decenas de megahercios** |
| **Cobertura** | **Por emisores, con red de frecuencia única** | **Un haz cubre un país** |
| **Recepción** | **Antena de tejado** | **Parabólica orientada** |

- **LA REGLA QUE ES TODA LA CLAVE** · `[of]` · **Cada medio se defiende de su enemigo.** **En tierra el
  enemigo es el eco y la defensa es repartir la información entre muchas portadoras lentas.** **En
  satélite el enemigo es la debilidad, y la defensa es modulación sencilla y robusta con mucha
  corrección de errores.**

## La modulación terrestre

- **PREGUNTA 42** · `[exam]` · **La modulación de la terrestre de primera generación es COFDM.** **Las
  falsas son siglas de otras materias**: una modulación analógica, un formato de fichero y una
  modulación de telefonía móvil.
- **PREGUNTA 26** · `[exam]` · **Se usa para mejorar la resistencia al multitrayecto.**
- **CÓMO FUNCIONA, EN CUATRO PASOS** · `[of]` · **Miles de portadoras lentas en vez de una rápida** ·
  **cada una lleva poquísima información, así que su símbolo dura mucho** · **entre símbolo y símbolo
  se deja un hueco, el intervalo de guarda** · **un eco con retardo menor que ese hueco cae dentro y NO
  estorba al símbolo siguiente.**
- **LA CONSECUENCIA MAYOR** · `[of]` · **La red de frecuencia única**: **si los ecos no molestan, dos
  emisores pueden transmitir lo mismo en la misma frecuencia.** **El segundo es, para el receptor, un
  eco más.** **Con modulación analógica era imposible.**

| Falsa de la 26 | Por qué cae |
|---|---|
| **Para reducir el retardo** | **Al revés**: el símbolo largo y la guarda AÑADEN retardo |
| **Porque es menos compleja** | **Es mucho más compleja**: transformadas rápidas en los dos extremos |
| **Porque pide menos ancho de banda** | **Ocupa el mismo canal de 8 megahercios** |

- **EL PRECIO DE LA GUARDA** · `[of]` · **Es tiempo en que no se transmite.** **Guarda larga: tolera
  ecos más lejanos y desperdicia más caudal.** **Elegirla es un compromiso entre tamaño de red y
  caudal.**

## Las dos generaciones terrestres

| | **Primera** | **Segunda** |
|---|---|---|
| **Estados por portadora** | **Hasta 64** | **Hasta 256** |
| **Corrección de errores** | **Convolucional más Reed-Solomon** | **Paridad de baja densidad más BCH** |
| **Formato de vídeo** | **MPEG-2** | **MPEG-4 AVC** ✔ |
| **Caudal por canal** | **Unos 19,9 Mbps con parámetros habituales** | **Hasta un 30-50 % más** |
| **Constelación rotada** | **No** | **Sí** |

- **LA REGLA DEL SALTO** · `[of]` · **La segunda no cambia el principio, lo afina**: misma
  multiportadora, misma guarda, misma red de frecuencia única, **mejor corrección y modulación más
  densa.**
- **LA REGLA DE TODO EL TEMARIO** · `[of]` · **Cuantos más estados por símbolo, más caudal y menos
  margen frente al ruido.** **256 estados exigen una relación señal-ruido que muchas recepciones
  domésticas no tienen**: la elección de parámetros es decisión de cobertura, no de laboratorio.

## La modulación por satélite

| | **DVB-S** | **DVB-S2** |
|---|---|---|
| **Modulación** | **Fase en cuadratura** | **La misma, más de 8 y 16 estados** |
| **Corrección de errores** | **Convolucional más Reed-Solomon** | **Paridad de baja densidad más BCH** |
| **Codificación y modulación adaptativas** | **No** | **Sí** |
| **Ganancia de caudal** | **—** | **Alrededor de un 30 %** |

- **POR QUÉ EL SATÉLITE MODULA EN FASE** · `[of]` · **El amplificador del satélite trabaja cerca de la
  saturación para aprovechar la potencia**, y **en saturación la amplitud no se conserva.** **Una
  modulación que sólo usa la fase sobrevive; una que usa la amplitud, no.**
- **LA ADAPTATIVA** · `[of]` · **El sistema mide la calidad del enlace de cada receptor y le manda la
  modulación que puede recibir**: **buen tiempo, más caudal; lluvia, más robustez.** **No se puede hacer
  en difusión pura**, y por eso se usa en contribución y datos.

## La distribución primaria

- **QUÉ ES** · `[of]` · **El transporte desde el centro de producción hasta los centros emisores.** **No
  la ve el espectador y es donde una avería deja una región entera sin televisión.**

| Medio | Rasgo |
|---|---|
| **Fibra óptica** | **El habitual hoy: capacidad y fiabilidad** |
| **Radioenlace** | **Donde la fibra no llega, o como respaldo** |
| **Satélite** | **Cobertura amplia de una vez, y respaldo de los otros dos** |

- **LOS TRES PRINCIPIOS DE DISEÑO** · `[of]` · **Redundancia de camino**: dos rutas físicamente
  distintas, **no dos fibras en la misma zanja** · **conmutación automática**: el cambio no puede
  depender de que alguien lo vea · **supervisión extremo a extremo**: saber que el respaldo funciona
  ANTES de necesitarlo.
- **EL AVISO** · `[of]` · **Una ruta de respaldo que no se prueba no es una ruta de respaldo.** **Falla
  por la misma razón que la copia de seguridad que nadie restaura.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 26 | Por qué esa modulación en la terrestre | **Resistencia al multitrayecto** ✔ |
| 42 | Qué modulación usa la televisión digital terrestre | **COFDM** ✔ |
| 44 | Formato de vídeo de la terrestre de segunda generación | **MPEG-4 AVC** ✔ |
