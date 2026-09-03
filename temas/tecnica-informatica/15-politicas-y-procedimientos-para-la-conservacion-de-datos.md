# Tema 15 del específico de Técnica Informática · Políticas y procedimientos para la conservación de datos

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Técnica Informática · punto 18 |
| **Sirve para** | **Técnica Informática** |
| **Fuente** | **Sin norma: no la hay.** Su materia es la política de conservación como buena práctica, y **va entero como oficio** |
| **Identificador** | — |
| **Redacción que se estudia** | No procede: **ninguna norma sostiene este tema** |
| **Punto sin banco** | **CERO preguntas en el cuadernillo.** El tema se escribe igual, contra el programa |
| **Enlace normativo** | **Lo que aquí es buena práctica, el Esquema Nacional de Seguridad del punto 26 lo convierte en obligación jurídica** |
| **Extensión** | **1.252 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: el objetivo de punto de recuperación (**RPO**,
*recovery point objective*) y el objetivo de tiempo de recuperación (**RTO**, *recovery time
objective*); el conjunto redundante de discos independientes (**RAID**); la cinta lineal abierta
(**LTO**, *linear tape open*); el plan de continuidad de negocio (**PCN**); y el Esquema Nacional de
Seguridad (**ENS**), del que trata el tema 23.

> Enunciado de la convocatoria (Anexo 2, temario específico de Técnica Informática, punto 18):
> «Políticas y procedimientos para la conservación de datos.»

**Cero preguntas.** **Este punto del anexo no ha dado ni una en el cuadernillo**, y **el tema se
escribe igual, contra el programa.** **Es el segundo caso de esta ocupación, tras el punto 14, y el
cuarto del proyecto.**

**Y hay una razón para no despacharlo deprisa**: **este punto es el que el Esquema Nacional de
Seguridad convierte en obligación jurídica.** **Lo que aquí se llama «política de conservación» es lo
que el tema 23 encuentra escrito en un real decreto.**

<!-- indice -->

## Índice

- [1. Las dos cifras que ordenan toda la materia](#1-las-dos-cifras-que-ordenan-toda-la-materia)
- [2. Copia de seguridad no es archivo, y ninguna de las dos es redundancia](#2-copia-de-seguridad-no-es-archivo-y-ninguna-de-las-dos-es-redundancia)
- [3. La regla 3-2-1 y lo que hoy se le añade](#3-la-regla-3-2-1-y-lo-que-hoy-se-le-añade)
- [4. El procedimiento que casi nadie cumple](#4-el-procedimiento-que-casi-nadie-cumple)
- [5. Lo que la ley obliga a conservar y a destruir](#5-lo-que-la-ley-obliga-a-conservar-y-a-destruir)
- [6. Lo que el examen ha preguntado](#6-lo-que-el-examen-ha-preguntado)
- [7. Trazabilidad](#7-trazabilidad)

<!-- /indice -->

## 1. Las dos cifras que ordenan toda la materia

**Antes de hablar de copias hay que fijar dos objetivos**, y **son los dos que decide el negocio, no
el técnico:**

| Objetivo | Qué pregunta | Qué determina |
|---|---|---|
| **Punto de recuperación** | **¿Cuántos datos puedo permitirme perder?** | **Cada cuánto se copia** |
| **Tiempo de recuperación** | **¿Cuánto puedo estar parado?** | **Cómo y desde dónde se restaura** |

**El ejemplo que lo hace concreto**: **un objetivo de punto de recuperación de veinticuatro horas
admite una copia diaria; uno de quince minutos exige replicación continua.** **Y un objetivo de tiempo
de recuperación de una semana admite recuperar de cinta; uno de una hora, no.**

**El error de método más frecuente**: **fijar la política mirando lo que la herramienta puede hacer.**
**Se fija al revés**: **primero se acuerda cuánto se puede perder y cuánto se puede estar parado, y
después se elige la herramienta que lo cumple.**

## 2. Copia de seguridad no es archivo, y ninguna de las dos es redundancia

**Es la confusión que más datos ha destruido**, y conviene dejarla clara:

| | **Redundancia** | **Copia de seguridad** | **Archivo** |
|---|---|---|---|
| **De qué protege** | **Del fallo de un componente** | **Del borrado, la corrupción y el desastre** | **De nada: preserva** |
| **Qué contiene** | **Lo mismo que el original, ahora** | **El estado en varios momentos pasados** | **Lo que ya no está en producción y hay que conservar** |
| **Ejemplo** | **RAID, replicación** | **Copia diaria con retención** | **Fondo documental, obligación legal** |

**Y la frase que lo resume**: **el RAID no es una copia de seguridad.** **Si alguien borra un fichero,
se borra a la vez en los dos discos.** **La redundancia protege del disco que se rompe, no de la
persona que se equivoca ni del programa que cifra los ficheros.**

## 3. La regla 3-2-1 y lo que hoy se le añade

**La regla clásica, que sigue siendo el mínimo defendible:**

| Cifra | Qué exige |
|---|---|
| **3** | **Tres copias de los datos**: el original y dos más |
| **2** | **En dos soportes distintos** |
| **1** | **Al menos una fuera del emplazamiento** |

**Y lo que la extorsión por cifrado ha obligado a añadir**: **al menos una copia inmutable o fuera de
línea.** **Una copia accesible desde la red con las mismas credenciales que el sistema copiado se cifra
con él**, y entonces las tres copias son la misma copia.

**Los tipos de copia, con su coste:**

| Tipo | Qué copia | Restaurar exige |
|---|---|---|
| **Completa** | **Todo** | **Sólo la última completa** |
| **Diferencial** | **Lo cambiado desde la última completa** | **La completa y la última diferencial** |
| **Incremental** | **Lo cambiado desde la copia anterior, sea cual sea** | **La completa y todas las incrementales desde entonces** |

**La regla de elección**: **la incremental es la más barata de hacer y la más cara de restaurar; la
completa, al revés.** **Y como se copia todos los días y se restaura casi nunca, lo corriente es
combinarlas.**

## 4. El procedimiento que casi nadie cumple

**Una política de conservación tiene cinco piezas, y la quinta es la que se olvida:**

1. **Qué se copia**, con inventario: no se puede copiar lo que no se sabe que existe.
2. **Cada cuánto**, derivado del objetivo de punto de recuperación.
3. **Dónde**, con al menos un destino fuera del emplazamiento.
4. **Cuánto se guarda**, que es la retención, y **cuándo se destruye**.
5. **Cada cuánto se PRUEBA la restauración.**

**El aviso, dicho sin adornos**: **una copia que no se ha restaurado nunca no se sabe si sirve.**
**Los fallos aparecen al restaurar** —un soporte ilegible, una clave de cifrado perdida, una base de
datos copiada en caliente sin consistencia—, **y aparecen el día del desastre si no se han buscado
antes.** **La prueba de restauración es la única parte de la política que demuestra que el resto
funciona.**

## 5. Lo que la ley obliga a conservar y a destruir

**Este punto tiene dos caras y el técnico sólo suele ver una.** **Conservar tiene un límite legal, y no
sólo un mínimo:**

| Norma | Qué impone |
|---|---|
| **Ley Orgánica 3/2018 y el reglamento europeo** | **Limitación del plazo de conservación**: los datos personales se conservan **el tiempo necesario para el fin que los justificó**, y después se suprimen o se anonimizan. **Es la materia del tema 22** |
| **Esquema Nacional de Seguridad** | **Medidas de copias de seguridad y de trazabilidad** según la categoría del sistema. **Es la materia del tema 23** |

**Y de ahí la tensión que define este punto**: **el técnico tiende a guardarlo todo por si acaso y la
norma obliga a borrar lo que ya no hace falta.** **Una política de conservación completa dice también
cuándo se destruye**, y **cómo se destruye**: **borrado seguro del soporte o destrucción física**,
porque **un disco desechado sin borrar es una fuga de datos.**

## 6. Lo que el examen ha preguntado

**Ninguna pregunta.**

**El aviso de estudio**: **es un punto corto y de conceptos, sin cifras que memorizar salvo la regla
3-2-1.** **Lo preguntable son las dos siglas de objetivo, la diferencia entre copia y redundancia y
los tres tipos de copia.** **Media hora bien empleada.**

## 7. Trazabilidad

**Este tema no cita ninguna fuente de forma literal**, y **no tiene ninguna respuesta oficial que
sostener.**

**Tres declaraciones expresas:**

1. **Los objetivos de punto y de tiempo de recuperación, la regla 3-2-1 y los tres tipos de copia son
   oficio de administración de sistemas**, de uso universal. **No proceden de ninguna norma, y así se
   dice.**
2. **Lo que el epígrafe 5 atribuye a la Ley Orgánica 3/2018 y al Esquema Nacional de Seguridad se
   desarrolla, con cita literal, en los temas 22 y 23 de esta misma ocupación.** **Aquí se enuncia sin
   citarlo**, para no repetir.
3. **Este temario no describe la política de conservación de RTVE**, que no ha consultado. **Lo que el
   tema contiene es la arquitectura habitual de una política de este tipo**, escrita como guía de
   estudio a partir del enunciado del anexo.

**El tema entero va como oficio y así se declara**, porque **su punto del anexo no tiene norma propia
detrás ni preguntas que contestar.**
