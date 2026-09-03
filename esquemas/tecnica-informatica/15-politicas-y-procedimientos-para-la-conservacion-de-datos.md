# Esquema · Tema 15 del específico de Técnica Informática · Políticas y procedimientos para la conservación de datos

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de administración de sistemas.
**Siglas**: el objetivo de punto de recuperación (**RPO**) y el objetivo de tiempo de recuperación
(**RTO**); el conjunto redundante de discos independientes (**RAID**); la cinta lineal abierta
(**LTO**); el plan de continuidad de negocio (**PCN**); y el Esquema Nacional de Seguridad (**ENS**),
del que trata el tema 23.

**Cabecera.** Enunciado: punto 18 del anexo · **CERO preguntas** · **el tema se escribe igual, contra
el programa**: **segundo caso de esta ocupación, tras el punto 14, y cuarto del proyecto.** · **La
razón para no despacharlo deprisa**: **es el punto que el Esquema Nacional de Seguridad convierte en
obligación jurídica.** **Lo que aquí es «política de conservación», en el tema 23 está escrito en un
real decreto.**

<!-- indice -->

## Índice

- [Las dos cifras que ordenan la materia](#las-dos-cifras-que-ordenan-la-materia)
- [Copia, archivo y redundancia](#copia-archivo-y-redundancia)
- [La regla 3-2-1, y lo que hoy se le añade](#la-regla-3-2-1-y-lo-que-hoy-se-le-añade)
- [Las cinco piezas de una política](#las-cinco-piezas-de-una-política)
- [Lo que la ley obliga a conservar y a destruir](#lo-que-la-ley-obliga-a-conservar-y-a-destruir)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las dos cifras que ordenan la materia

| Objetivo | Qué pregunta | Qué determina |
|---|---|---|
| **Punto de recuperación** | **¿Cuántos datos puedo permitirme perder?** | **Cada cuánto se copia** |
| **Tiempo de recuperación** | **¿Cuánto puedo estar parado?** | **Cómo y desde dónde se restaura** |

- **LAS DECIDE EL NEGOCIO, NO EL TÉCNICO.**
- **EL EJEMPLO QUE LO CONCRETA**: **veinticuatro horas de punto de recuperación admiten una copia
  diaria; quince minutos exigen replicación continua.** **Una semana de tiempo de recuperación admite
  recuperar de cinta; una hora, no.**
- **EL ERROR DE MÉTODO MÁS FRECUENTE**: **fijar la política mirando lo que la herramienta puede
  hacer.** **Se fija al revés**: primero cuánto se puede perder y cuánto se puede estar parado,
  después la herramienta que lo cumple.

## Copia, archivo y redundancia

| | **Redundancia** | **Copia de seguridad** | **Archivo** |
|---|---|---|---|
| **De qué protege** | **Del fallo de un componente** | **Del borrado, la corrupción y el desastre** | **De nada: preserva** |
| **Qué contiene** | **Lo mismo que el original, ahora** | **El estado en varios momentos pasados** | **Lo que ya no está en producción y hay que conservar** |
| **Ejemplo** | **RAID, replicación** | **Copia diaria con retención** | **Fondo documental, obligación legal** |

- **LA FRASE QUE LO RESUME**: **el RAID no es una copia de seguridad.** **Si alguien borra un fichero,
  se borra a la vez en los dos discos.** **La redundancia protege del disco que se rompe, no de la
  persona que se equivoca ni del programa que cifra los ficheros.**

## La regla 3-2-1, y lo que hoy se le añade

| Cifra | Qué exige |
|---|---|
| **3** | **Tres copias**: el original y dos más |
| **2** | **En dos soportes distintos** |
| **1** | **Al menos una fuera del emplazamiento** |

- **LO QUE HA OBLIGADO A AÑADIR LA EXTORSIÓN POR CIFRADO**: **al menos una copia inmutable o fuera de
  línea.** **Una copia accesible desde la red con las mismas credenciales que el sistema copiado se
  cifra con él**, y entonces las tres copias son la misma copia.

| Tipo | Qué copia | Restaurar exige |
|---|---|---|
| **Completa** | **Todo** | **Sólo la última completa** |
| **Diferencial** | **Lo cambiado desde la última completa** | **La completa y la última diferencial** |
| **Incremental** | **Lo cambiado desde la anterior, sea cual sea** | **La completa y todas las incrementales** |

- **LA REGLA DE ELECCIÓN**: **la incremental es la más barata de hacer y la más cara de restaurar; la
  completa, al revés.** **Como se copia todos los días y se restaura casi nunca, lo corriente es
  combinarlas.**

## Las cinco piezas de una política

1. **Qué se copia**, con inventario: **no se puede copiar lo que no se sabe que existe.**
2. **Cada cuánto**, derivado del objetivo de punto de recuperación.
3. **Dónde**, con al menos un destino fuera del emplazamiento.
4. **Cuánto se guarda** —la retención— **y cuándo se destruye.**
5. **Cada cuánto se PRUEBA la restauración.**

- **EL AVISO, SIN ADORNOS**: **una copia que no se ha restaurado nunca no se sabe si sirve.** **Los
  fallos aparecen al restaurar** —soporte ilegible, clave de cifrado perdida, base de datos copiada en
  caliente sin consistencia— **y aparecen el día del desastre si no se han buscado antes.**

## Lo que la ley obliga a conservar y a destruir

| Norma | Qué impone |
|---|---|
| **Ley Orgánica 3/2018 y el reglamento europeo** | **Limitación del plazo**: los datos personales se conservan **el tiempo necesario para el fin que los justificó** (tema 22) |
| **Esquema Nacional de Seguridad** | **Medidas de copias y de trazabilidad** según la categoría del sistema (tema 23) |

- **LA TENSIÓN QUE DEFINE EL PUNTO**: **el técnico tiende a guardarlo todo por si acaso y la norma
  obliga a borrar lo que ya no hace falta.**
- **UNA POLÍTICA COMPLETA DICE TAMBIÉN CÓMO SE DESTRUYE**: **borrado seguro del soporte o destrucción
  física**, porque **un disco desechado sin borrar es una fuga de datos.**

## Lo que se ha preguntado

**Ninguna pregunta.**

**Aviso de estudio**: **punto corto y de conceptos, sin cifras que memorizar salvo la regla 3-2-1.**
**Lo preguntable son las dos siglas de objetivo, la diferencia entre copia y redundancia y los tres
tipos de copia.** **Media hora bien empleada.**
