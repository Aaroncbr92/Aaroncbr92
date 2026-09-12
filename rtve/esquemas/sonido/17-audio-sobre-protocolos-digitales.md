# Esquema · Tema 17 del específico de Sonido · Audio sobre protocolos digitales

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de instalación digital ·
`[norma]` = norma de organismo técnico. **Siglas**: la interfaz digital multicanal de audio (**MADI**,
*multichannel audio digital interface*), que la Sociedad de Ingeniería de Audio (**AES**) publica como
**AES10**; la norma de dos canales de esa misma sociedad (**AES3**) y su norma de sincronismo
(**AES11**); el código de tiempo longitudinal (**LTC**, *longitudinal timecode*); y el reloj de palabra
(*word clock*).

**Cabecera.** Enunciado: punto 15 del anexo, «Audio sobre protocolos digitales» · **5 preguntas** · **tres son de
MADI y dos de sincronía.**

<!-- indice -->

## Índice

- [Las interfaces digitales de audio](#las-interfaces-digitales-de-audio)
- [El MADI](#el-madi)
- [La sincronía: qué sincroniza qué](#la-sincronía-qué-sincroniza-qué)
- [El código de tiempo](#el-código-de-tiempo)
- [Conversión y compatibilidad](#conversión-y-compatibilidad)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las interfaces digitales de audio

| Interfaz | Canales | Por dónde va |
|---|---|---|
| **AES3** | **2** | **Par equilibrado con conector de tres contactos, o coaxial** |
| **MADI** | **Hasta 64** | **Coaxial o fibra óptica** |
| **Word clock** | **Ninguno: sólo reloj** | **Coaxial** |

## El MADI

- **PREGUNTA 77** · `[norma]` · **El protocolo MADI permite hasta 64 canales de audio.**
- **PREGUNTA 61** · `[of]` · **De forma estándar, el MADI óptico es multimodo.**
- **PREGUNTA 28** · `[of]` · **El método más eficiente para asegurar el funcionamiento de un sistema
  MADI es implementar rutas de transmisión redundantes.**
- **POR QUÉ LA REDUNDANCIA Y NO OTRA COSA**: **un enlace MADI lleva 64 canales por un solo cable.**
  **Si ese cable falla, se caen los 64 a la vez.** **Duplicar el camino es la única defensa
  proporcionada al riesgo.**
- **ENLACE CON OTROS TEMARIOS**: **es la misma idea que la conmutación sin costuras del vídeo sobre
  redes**, aplicada al audio y con cable en vez de con flujo.

## La sincronía: qué sincroniza qué

- **PREGUNTA 27** · `[of]` · **El word clock sincroniza equipos digitales.**
- **LOS TRES RELOJES QUE NO HAY QUE CONFUNDIR:**

| Señal | Qué sincroniza |
|---|---|
| **Word clock** | **La frecuencia de muestreo de los equipos de audio** ✔ |
| **Código de tiempo** | **La posición temporal: qué instante del programa es** |
| **Sincronismo de vídeo** | **El cuadro y la línea de la imagen** |

- **EL ERROR CLÁSICO**: **creer que el código de tiempo sincroniza el muestreo.** **No lo hace**: dice
  dónde estamos, no a qué ritmo se muestrea.

## El código de tiempo

- **PREGUNTA 19** · `[of]` · **Una palabra de código de tiempo longitudinal tiene 80 bits por
  fotograma.**
- **QUÉ LLEVAN ESOS 80 BITS**: **horas, minutos, segundos y fotograma; bits de usuario; y una palabra
  de sincronismo que además dice en qué dirección se está reproduciendo.**
- **POR QUÉ SE LLAMA LONGITUDINAL**: **se graba como una señal de audio en una pista longitudinal**, y
  por eso se puede leer con un equipo de sonido corriente.

## Conversión y compatibilidad

- **LA REGLA DE ORO DE UNA INSTALACIÓN DIGITAL**: **un solo reloj maestro y todos los demás
  esclavos.**
- **QUÉ PASA SI NO**: **dos equipos con relojes independientes acumulan diferencia y producen un clic
  cada vez que se desbordan.** **Es la avería más común y la más difícil de atribuir.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 19 | Bits de una palabra de LTC por fotograma | a) 80 ✔ |
| 27 | Qué hace el word clock | a) Sincroniza equipos digitales ✔ |
| 28 | Método más eficiente para asegurar un sistema MADI | c) Rutas de transmisión redundantes ✔ |
| 61 | Cómo es de forma estándar el MADI óptico | b) Multimodo ✔ |
| 77 | Qué permite el protocolo MADI | a) Hasta 64 canales de audio ✔ |

**Las cinco oficiales son correctas** y **ninguna descansa sólo en la plantilla.** · **Aviso de
estudio**: **el cuadro de los tres relojes es lo que este punto deja para siempre**, y **explica la
mitad de las averías de una instalación digital.**
