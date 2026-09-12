# Esquema · Tema 15 del específico de Técnica de Equipos y Sistemas Electrónicos · Mantenimiento preventivo y correctivo de equipos

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de taller y mantenimiento.
**Siglas**: el hercio (**Hz**); la corriente alterna (**CA**) y la continua (**CC**); y las descargas
electrostáticas (**ESD**, *electrostatic discharge*).

**Cabecera.** Enunciados: puntos 17 y 18 del anexo, reunidos en un tema porque **son la misma frase con
una palabra cambiada** · **2 preguntas, y las dos son de correctivo.**

<!-- indice -->

## Índice

- [Los dos mantenimientos](#los-dos-mantenimientos)
- [El método del correctivo](#el-método-del-correctivo)
- [La soldadura fría](#la-soldadura-fría)
- [El zumbido de 50 hercios](#el-zumbido-de-50-hercios)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Los dos mantenimientos

| | **Preventivo** | **Correctivo** |
|---|---|---|
| **Cuándo** | **Antes de que falle** | **Después de que ha fallado** |
| **Quién decide el momento** | **El plan** | **La avería** |
| **Qué cuesta** | **Horas previstas, en horario elegido** | **Horas imprevistas, a menudo en directo** |

- **LA REGLA ECONÓMICA**: **una hora de preventivo cuesta menos que una de correctivo, porque la de
  correctivo se paga además con la emisión.**
- **LAS TAREAS DEL PREVENTIVO**: **limpieza de filtros y ventiladores · limpieza de ópticas y
  contactos · prueba de baterías y de alimentación ininterrumpida · verificación de medidas ·
  actualizaciones en ventana programada · copia de configuraciones · manipulación con protección
  contra descargas electrostáticas.**
- **LOS DOS AVISOS QUE MÁS SE OLVIDAN**: **una actualización es un cambio y se planifica, con la
  versión anterior guardada**; **y la configuración de un equipo vale tanto como el equipo**, porque un
  repuesto sin ella no sustituye a nada.
- **LO QUE MÁS MATERIAL ESTROPEA SIN QUE NADIE SE ENTERE**: **la descarga electrostática que uno ni
  siente puede dañar una entrada sin destruirla**, y el equipo falla semanas después. **Es la misma
  avería diferida que la soldadura fría.**

## El método del correctivo

1. **Reproducir la avería.** **La que no se reproduce no se arregla ni se comprueba.**
2. **Delimitar la mitad averiada.** **Mirar un punto intermedio: si allí está bien, el fallo va
   después.**
3. **Separar lo eléctrico de lo lógico.**
4. **Sustituir por un elemento sano y comprobar.**
5. **Confirmar con la misma prueba del paso 1**, y sólo entonces devolver el equipo al servicio.

- **EL PASO 2 TIENE NOMBRE**: **búsqueda binaria.** **Una cadena de doce etapas se recorre en cuatro
  medidas partiendo por la mitad y en doce yendo de una en una.**
- **EL AVISO DE FONDO**: **el síntoma no es la avería.** **Un monitor sin imagen puede tener el fallo
  en el monitor, el cable, el distribuidor, la matriz o la fuente.**

## La soldadura fría

- **PREGUNTA 63** · `[of]` · **La que NO es causa de soldadura fría es la estabilidad durante el
  enfriamiento del metal de soldadura.**
- **LA PALABRA QUE RESUELVE LA PREGUNTA ES «ESTABILIDAD»**: **lo que estropea la unión es el
  *movimiento* durante el enfriamiento, no la estabilidad.** **La opción a nombra lo contrario del
  defecto.**
- **LAS TRES CAUSAS REALES**: **superficie sin limpiar · poco estaño · punta poco caliente**, ésta la
  más frecuente.
- **CÓMO SE RECONOCE**: **aspecto mate, granuloso y abombado**, frente al brillante y cóncavo de una
  buena.
- **POR QUÉ ES TRAICIONERA**: **funciona el día que se hace y falla semanas después con la vibración o
  el ciclado térmico.** **Produce fallos intermitentes que no se reproducen cuando uno mira.**
- **EL AVISO DE TALLER**: **hay que calentar la pieza, no el estaño.** **Estaño fundido sobre piezas
  frías es la receta exacta del defecto.**

## El zumbido de 50 hercios

- **PREGUNTA 29 del segundo llamamiento** · `[of]` · **La causa más probable de un zumbido constante de
  50 Hz es un condensador de filtrado defectuoso en la fuente.**
- **LA CIFRA DEL ENUNCIADO LO DICE TODO**: **cincuenta hercios es la frecuencia de la red.** **Un
  zumbido a esa frecuencia no viene de la señal: viene de la alimentación.**
- **CÓMO OCURRE**: **el condensador envejecido pierde capacidad · el rizado crece · esa ondulación se
  cuela en la etapa amplificadora y sale por el altavoz.**
- **LA REGLA DE DIAGNÓSTICO QUE ESTE CASO ENSEÑA**: **la frecuencia del ruido dice de dónde viene.**

| Ruido | De dónde viene |
|---|---|
| **50 Hz** | **De la red: filtrado de la fuente, o bucle de masa** |
| **100 Hz** | **Rizado de un rectificador de doble onda: también la fuente** |
| **Silbido agudo constante** | **Conmutación de una fuente conmutada** |
| **Siseo de banda ancha** | **Ruido térmico: ganancia excesiva en la entrada** |
| **Crujido intermitente** | **Contacto malo: conector sucio o soldadura fría** |

- **EL MATIZ QUE SEPARA LAS DOS CAUSAS DE ZUMBIDO DE RED**: **si cambia al mover los cables de señal es
  un bucle de masa; si no cambia, es la fuente.** **La pregunta dice «constante».**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 63 | Causa que NO lo es de una soldadura fría | a) La estabilidad durante el enfriamiento ✔ |
| 29 (2.º llam.) | Causa de un zumbido constante de 50 Hz | a) Condensador de filtrado defectuoso ✔ |

**Las dos oficiales son correctas** y **ninguna descansa en la plantilla**: **las dos se razonan desde
el síntoma.** · **Aviso de estudio**: **el cuadro de frecuencias de ruido y el aspecto de una soldadura
mala son las dos formas en que este oficio reconoce una avería antes de medir nada.**
