# Esquema · Tema 19 del específico de Técnica Informática · Sistemas de producción digital audiovisual

Telegrama. **Cada línea lleva delante de dónde sale**: `[norma]` = índice público de una norma de
organismo técnico · `[of]` = oficio de instalaciones de producción · `[exam]` = opciones del propio
cuadernillo. **Siglas**: la Sociedad de Ingenieros de Cine y Televisión (**SMPTE**), que publica la
familia **SMPTE ST 2110**; la Sociedad de Ingeniería de Audio (**AES**), que publica la norma
**AES67**; el protocolo de internet (**IP**) y el de datagramas de usuario (**UDP**); el protocolo de
tiempo de precisión (**PTP**); la interfaz digital serie (**SDI**); la modulación por impulsos
codificados (**PCM**); y el audio y el vídeo (**A/V**), como los abrevia el enunciado.

**Cabecera.** Enunciado: punto 22 del anexo · **2 preguntas** · **ninguna lleva figura** · **las dos
piden lo mismo: el número de una norma.** · **Es el ÚNICO punto de esta ocupación cuya respuesta está
verificada contra un documento público de un organismo de normalización**, y no como oficio.

<!-- indice -->

## Índice

- [Por qué el vídeo se mete en la red de datos](#por-qué-el-vídeo-se-mete-en-la-red-de-datos)
- [La familia SMPTE ST 2110](#la-familia-smpte-st-2110)
- [El audio sobre red](#el-audio-sobre-red)
- [La arquitectura básica](#la-arquitectura-básica)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Por qué el vídeo se mete en la red de datos

- **EL CAMBIO, EN UNA FRASE**: **la matriz y el cable coaxial se están sustituyendo por un conmutador
  y un cable de red.**

| Ventaja | Por qué |
|---|---|
| **Un solo cable para todo** | **Vídeo, audio, control y datos por la misma infraestructura** |
| **Sin límite de tamaño** | **Un conmutador crece añadiendo equipos; una matriz tiene tamaño fijo** |
| **Equipo genérico** | **Electrónica de red corriente, no aparatos de un solo fabricante** |
| **Flexibilidad** | **Reconfigurar es cambiar una suscripción, no recablear** |

| Garantía que el cable daba sola | Cómo se recupera en la red |
|---|---|
| **Sincronismo** | **Con un reloj de precisión repartido por la propia red** |
| **Latencia previsible** | **Con calidad de servicio y una red bien dimensionada** |
| **Entrega ordenada y completa** | **Con redundancia de camino y corrección de errores** |

- **ÉSA ES LA RAZÓN DE SER DE LAS DOS NORMAS QUE EL EXAMEN PREGUNTA**: **existen para poner de acuerdo
  a los fabricantes en cómo se recupera cada garantía perdida.**

## La familia SMPTE ST 2110

- **PREGUNTA 30** · `[exam]` · **El conjunto de estándares para audio, vídeo y datos auxiliares sobre
  redes IP es SMPTE 2110.**
- **LAS TRES FALSAS SON EL MISMO NÚMERO CON LAS CIFRAS CAMBIADAS** —2001, 2100, 2010—: **memoria de
  cuatro dígitos.** **El apoyo que funciona es la pareja**: **2110 para los flujos separados y 2022
  para la redundancia.**
- **QUÉ HACE LA FAMILIA**: **descompone la señal en flujos separados** —vídeo, audio y datos— **y los
  vuelve a juntar con un reloj común.** **Eso la distingue de la interfaz digital serie, donde todo
  iba incrustado en la misma trama.**

| Parte | Título oficial | De qué trata |
|---|---|---|
| **ST 2110-10** | `[norma]` «System Timing and Definitions» | **El reloj y las definiciones comunes** |
| **ST 2110-20** | `[norma]` «Uncompressed Active Video» | **El vídeo sin comprimir** |
| **ST 2110-30** | `[norma]` «PCM Digital Audio» | **El audio** ✔ |
| **ST 2110-40** | `[norma]` «SMPTE ST 291-1 Ancillary Data» | **Los datos auxiliares** |

## El audio sobre red

- **PREGUNTA 63** · `[exam]` · **El estándar de interoperabilidad de la Sociedad de Ingeniería de
  Audio para audio sobre IP y Ethernet es AES67.**
- **OTRA VEZ LAS FALSAS SON EL MISMO NÚMERO DESPLAZADO** —AES65, AES66, AES68—: **memoria.**
- **EL ATAJO**: **67 va con 2110-30**, porque **la parte de audio de la familia de la SMPTE se apoya en
  él.** **Las dos preguntas del punto son las dos caras de la misma pareja.**
- **QUÉ APORTA, EN UNA LÍNEA**: **que sistemas de audio sobre red de fabricantes distintos se
  entiendan**, frente a los protocolos propietarios de cada casa.
- **EL AVISO**: **el texto de la norma está tras un muro de pago y no se ha leído.** **Lo que se
  afirma de ella es lo que la respuesta oficial afirma.**

## La arquitectura básica

| Bloque | Qué contiene |
|---|---|
| **Captación** | **Cámaras y micrófonos**, hoy con salida sobre red |
| **Encaminamiento** | **La red de conmutadores que sustituye a la matriz** |
| **Sincronismo** | **Un reloj maestro que reparte tiempo por la propia red** |
| **Producción** | **Mezcladores, servidores de repetición, grafismo** |
| **Almacenamiento** | **Servidores de vídeo y gestores de material** |
| **Control** | **Los sistemas que dicen qué se encamina a dónde** |

- **LOS DOS RASGOS QUE UN INFORMÁTICO DEBE ENTENDER**, y son los que más problemas dan:
  1. **La red de producción no es la red ofimática.** **Se separa físicamente o por redes lógicas**,
     porque **el vídeo sin comprimir llena un enlace de diez gigabits con unas pocas señales.**
  2. **El envío es a varios destinos, no a uno.** **Una cámara publica su flujo y quien lo necesita se
     suscribe**, lo que exige que la electrónica gestione bien la suscripción a grupos. **Una red que
     no la gestione inunda todos los puertos y se cae sola.**

## Lo que se ha preguntado

| Nº | Qué pide | Oficial |
|---|---|---|
| 30 | Estándares de la SMPTE para audio, vídeo y datos sobre IP | d) SMPTE 2110 ✔ **·** verificado en el índice de la SMPTE |
| 63 | Estándar de la AES para audio sobre IP y Ethernet | c) AES67 ✔ |

**Las dos oficiales son correctas** · **ninguna descansa en la plantilla** · **la primera está
verificada contra el índice público de la propia sociedad.** · **Aviso de estudio**: **el punto entero
cabe en dos números, 2110 y 67**, y **se aprenden como pareja**: van juntos en la instalación y el
examen los preguntó en el mismo cuadernillo.
