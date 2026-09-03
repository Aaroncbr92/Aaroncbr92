# Esquema · Tema 1 del específico de Edición, Montaje y Procesos Audiovisuales · Conocimientos básicos de electrónica e informática aplicadas

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio, sin norma detrás.

**Cabecera.** Enunciado: «1.1. Conocimientos básicos de electrónica aplicada · 1.2. Conocimientos
básicos de informática aplicada» · **4 preguntas** · **las cuatro son de informática y NINGUNA de
electrónica** · **tres de las cuatro son de RAID**.

<!-- indice -->

## Índice

- [Los tres problemas de una sala](#los-tres-problemas-de-una-sala)
- [Qué es un RAID](#qué-es-un-raid)
- [Los niveles](#los-niveles)
- [RAID 5](#raid-5)
- [Local, NAS y SAN](#local-nas-y-san)
- [Los cuatro aparatos de red](#los-cuatro-aparatos-de-red)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los tres problemas de una sala

- **CAPACIDAD** —una hora de alta definición sin comprimir pasa de los 100 GB— · **VELOCIDAD** —si el
  disco no da el caudal del códec, **el vídeo se corta**— · **SEGURIDAD** —**un disco se rompe y el
  material de una jornada no se vuelve a grabar**—.
- **EL RAID RESUELVE LOS TRES A LA VEZ.** Por eso es lo que el examen pregunta.

## Qué es un RAID

- **PREGUNTA 26** · **Un RAID es un tipo de almacenamiento en el que LOS DATOS SE ESCRIBEN EN VARIOS
  DISCOS DENTRO DE UN MISMO SISTEMA.**
- **LAS SIGLAS**: *redundant array of independent disks* = **conjunto REDUNDANTE de discos
  INDEPENDIENTES**. **Redundante** = hay información de más para reconstruir · **conjunto** = varios
  discos vistos como uno · **independientes** = cada disco es una unidad completa.
- **LAS TRES FALSAS CONFUNDEN EL RAID CON SU USO**: «varios proyectos en un disco» = **usar un disco**
  · «discos de distinto formato» = **el RAID pide discos IGUALES** · «un proyecto en varios discos» =
  **el RAID reparte BLOQUES, no proyectos**.
- **LA DISTINCIÓN QUE RESUELVE LA PREGUNTA**: **el RAID es una forma de ESCRIBIR, no de organizar el
  trabajo.**

## Los niveles

| Nivel | Cómo escribe | Gana | Pierde |
|---|---|---|---|
| **RAID 0** | ***Striping***: reparte **sin redundancia** | Velocidad y **toda la capacidad** | **NINGUNA seguridad** |
| **RAID 1** | ***Mirroring***: **duplica un disco en otro** | **Seguridad** | **La mitad de la capacidad** |
| **RAID 5** | *Striping* **con paridad distribuida** | **Velocidad y tolerancia a fallo** | **Mínimo TRES discos** |
| **RAID 6** | **Doble paridad** | Aguanta **dos** caídas | Más capacidad y escritura perdidas |
| **RAID 10** | Espejos en *striping* | **Velocidad y seguridad** | La mitad, y **cuatro discos** |

- **PREGUNTA 4** · **La correcta: «en RAID 1, también conocido como sistema espejo, se duplican los
  datos de un disco en otro».**
- **LAS TRES FALSAS SON LA MISMA TRAMPA: CAMBIAN EL NÚMERO.** «RAID 0 el más fiable» → **es el MENOS**
  · «RAID 0 es el espejo» → **el espejo es el 1** · «en RAID 1 se reparte sin redundancia» → **eso es
  el 0**.
- **LA REGLA QUE NO FALLA**: **RAID 0, CERO seguridad. RAID 1, UN disco copiado en otro.**

## RAID 5

- **PREGUNTA 92** · **Su principal ventaja: SU TOLERANCIA A ERRORES APORTA VELOCIDAD Y PROTECCIÓN DE
  LOS DATOS.**
- **CÓMO: LA PARIDAD.** Reparte como el RAID 0 **y añade en cada franja un bloque de paridad, en un
  disco distinto cada vez**. Si cae un disco, **reconstruye desde los otros y la paridad**.
- **CON TRES DISCOS**: capacidad útil **dos de tres** · pierde **uno** sin caerse · **lectura rápida**
  · **escritura más lenta** (hay que calcular la paridad).
- **LAS TRES FALSAS**: «máximo dos discos» → **exige TRES como mínimo** · «no ofrece redundancia» →
  **la paridad ES la redundancia** · «superior a cualquier otro nivel» → **el 0 es más rápido y el 6
  más seguro: el 5 es el EQUILIBRIO, no el máximo**.
- **AVISO DE OFICIO**: **un RAID NO es una copia de seguridad.** Protege del fallo de un disco, **no
  del borrado accidental ni del incendio.**

## Local, NAS y SAN

| Sistema | Qué es | Dónde |
|---|---|---|
| **Local** | Discos dentro de la estación | Una sola sala |
| **NAS** | **Sirve FICHEROS por la red** | Trabajo compartido ligero, archivo |
| **SAN** | **Sirve BLOQUES de disco** | **Edición compartida en tiempo real** |

- **LA DIFERENCIA QUE IMPORTA**: **en un NAS se pide un FICHERO; en una SAN se pide un BLOQUE.** Por
  eso **la SAN da el caudal sostenido** que la reproducción de vídeo necesita.
- **Y DEBAJO DE LOS TRES HAY UN RAID**: no son alternativas al RAID, son **maneras de presentarlo**.

## Los cuatro aparatos de red

| Aparato | Qué hace | Dónde trabaja |
|---|---|---|
| **Hub** | **Repite por todos los puertos**, sin mirar | El nivel más bajo. **Obsoleto** |
| **Switch** | **Envía al puerto del destinatario** (dirección MAC) | **DENTRO de una red local** |
| **Router** | **Une redes distintas** y encamina (dirección IP) | **ENTRE redes** |
| «Interconectador» | **NO EXISTE** | — |

- **PREGUNTA 32** · **El aparato para conectar una red local con una de área extensa es el ROUTER o
  ENRUTADOR.**
- **LA REGLA**: **el switch mueve DENTRO; el router mueve ENTRE.** Local y extensa **son dos redes
  distintas**.
- **LO QUE HAY QUE SABER ADEMÁS**: **el vídeo por red no perdona la congestión.** Por eso **la red de
  producción va separada de la ofimática**.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 4 | Afirmación correcta sobre niveles RAID | d) En RAID 1, espejo, se duplican los datos ✔ |
| 26 | Qué es el almacenamiento RAID | d) Los datos se escriben en varios discos ✔ |
| 32 | Aparato entre red local y red extensa | a) Router o enrutador ✔ |
| 92 | Principal ventaja de RAID 5 | c) Tolerancia a errores: velocidad y protección ✔ |

**Las cuatro oficiales son correctas y ninguna descansa sólo en la plantilla.** · **Aviso de
reparto**: **el anexo dedica un subpunto a la electrónica y el examen no ha preguntado nada de ella.
Las cuatro son de informática y tres, de RAID.**
