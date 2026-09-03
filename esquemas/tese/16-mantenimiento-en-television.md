# Esquema · Tema 16 del específico de Técnica de Equipos y Sistemas Electrónicos · Mantenimiento en televisión

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de explotación. **Siglas**: el
conjunto redundante de discos independientes (**RAID**) y el sistema de alimentación ininterrumpida
(**SAI**).

**Cabecera.** Enunciado: punto 19 del anexo · **3 preguntas, y ninguna es de electrónica**: **dos son
de licencias de programas y una de criterio ante una avería en directo.** **Las tres vienen del segundo
cuadernillo y ninguna del primero**, cosa que no ocurre en ningún otro punto de la ocupación.

<!-- indice -->

## Índice

- [Qué se mantiene en una televisión](#qué-se-mantiene-en-una-televisión)
- [La redundancia](#la-redundancia)
- [El disco averiado en continuidad](#el-disco-averiado-en-continuidad)
- [Licencias y versiones](#licencias-y-versiones)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué se mantiene en una televisión

| Área | Qué la caracteriza |
|---|---|
| **Estudios** | **Muchos equipos móviles y cableado que se manipula a diario** |
| **Continuidades** | **No pueden parar: cada minuto es emisión** |
| **Controles y salas técnicas** | **La columna vertebral: un fallo aquí afecta a todo** |
| **Sistemas de redacción** | **Fallan por informática, no por electrónica** |
| **Postproducción** | **Dependencia fuerte de versiones y licencias** |
| **Sonorización** | **Potencia, cables y realimentación** |

- **LA JERARQUÍA DE PRIORIDADES**: **primero lo que está en antena, después lo que va a estarlo en las
  próximas horas, al final lo recuperable.** **Una sala de edición parada es un problema; una
  continuidad parada es un incidente de emisión.**

## La redundancia

| Nivel | Cuánto tarda en entrar |
|---|---|
| **Repuesto en almacén** | **Ir a por él y configurarlo** |
| **Reserva fría** | **Encenderla y conmutar** |
| **Reserva caliente** | **Accionar la conmutación** |
| **Redundancia interna del equipo** | **Ninguno: sigue con la pieza rota dentro** ✔ |
| **Doble camino permanente** | **Ninguno: no hay conmutación** |

- **LA REGLA QUE LA PREGUNTA 25 MIDE**: **la redundancia existe para que la avería no se note.** **Si
  se ha invertido en ella y aun así se para el servicio, no ha servido de nada.**
- **EL AVISO QUE CASI NADIE RECUERDA**: **una redundancia que no se prueba no existe.** **Probar las
  conmutaciones y descargar los sistemas de alimentación ininterrumpida es tarea del preventivo.**

## El disco averiado en continuidad

- **PREGUNTA 25 del segundo llamamiento** · `[of]` · **Con un disco fallado en un sistema con
  redundancia interna, hay que continuar la emisión normalmente.**
- **POR QUÉ**: **la redundancia interna está haciendo justo aquello para lo que se compró.** **Un
  conjunto en RAID 5 sigue funcionando con un disco menos.**
- **LAS TRES FALSAS, DE MENOS A MÁS DAÑINAS**: **detener la emisión convierte una avería sin
  consecuencias en un corte · copiar en caliente carga el conjunto degradado · reiniciar corta la
  emisión y además somete a los discos supervivientes al momento de mayor esfuerzo.**
- **LO QUE SÍ HAY QUE HACER, Y NO ESTÁ ENTRE LAS OPCIONES**: **sustituir el disco sin parar el servicio
  y vigilar la reconstrucción.** **Emitir y reparar no son incompatibles.**
- **EL AVISO TÉCNICO**: **un conjunto degradado ha agotado su margen.** **Seguir emitiendo es lo
  correcto; olvidarse del disco caído, no.**

## Licencias y versiones

| | **Licencia nominal** | **Licencia flotante** |
|---|---|---|
| **A qué se ata** | **A un equipo o a una persona** | **A un servidor que las presta** |
| **Qué limita** | **Nada más** | **Cuántas se usan a la vez** ✔ |

- **PREGUNTA 15 del segundo llamamiento** · `[of]` · **Las licencias flotantes se comparten, pero sólo
  un número limitado de usuarios puede usarlas a la vez.**
- **POR QUÉ UNA REDACCIÓN LAS COMPRA**: **ochenta redactores y veinte editando a la vez.** **Comprar
  ochenta sería pagar sesenta paradas.**
- **EL INCONVENIENTE QUE SUFRE EL MANTENIMIENTO**: **el redactor que deja el programa abierto y se va
  mantiene su licencia ocupada.** **Saber liberar una licencia colgada es tarea del soporte diario.**
- **PREGUNTA 17 del segundo llamamiento** · `[of]` · **Un proyecto de 2024 no se abrirá en la versión de
  2022.**
- **LA REGLA, QUE ES ASIMÉTRICA**: **un proyecto viejo abierto con programa nuevo suele funcionar; uno
  nuevo abierto con programa viejo, no.** **Un programa puede saber lo que se hizo antes; ninguno puede
  saber lo que se hará después.**
- **CÓMO SE RESUELVE EN LA PRÁCTICA**: **exportando en un formato de intercambio, o igualando versiones
  entre estaciones.** **Lo segundo es lo que el mantenimiento debe perseguir**, porque un parque con
  versiones distintas genera esta incidencia todas las semanas.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 15 (2.º llam.) | Cómo funciona una licencia flotante | c) Se comparten, con límite simultáneo ✔ |
| 17 (2.º llam.) | Problema al abrir un proyecto de 2024 en la versión de 2022 | b) No se abrirá ✔ |
| 25 (2.º llam.) | Qué hacer con un disco averiado en un sistema redundante | b) Continuar la emisión ✔ |

**Las tres oficiales son correctas** y **ninguna descansa en la plantilla.** · **Aviso de estudio**:
**este punto no se estudia con un manual de electrónica.** **Mide criterio de explotación: qué se para
y qué no, qué se duplica, cómo se organizan las licencias y por qué las versiones no van hacia
atrás.**
