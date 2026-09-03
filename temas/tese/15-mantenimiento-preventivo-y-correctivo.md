# Tema 15 del específico de Técnica de Equipos y Sistemas Electrónicos · Mantenimiento preventivo y correctivo de equipos

Las siglas de este tema, presentadas de entrada: el hercio (**Hz**), unidad de frecuencia; la corriente
alterna (**CA**) y la corriente continua (**CC**); y las descargas electrostáticas (**ESD**,
*electrostatic discharge*), contra las que se protege el material electrónico durante su manipulación.

> Enunciados de la convocatoria (Anexo 2, temario específico de Técnica de Equipos y Sistemas
> Electrónicos, puntos 17 y 18):
> «MANTENIMIENTO PREVENTIVO DE EQUIPOS: Elementos de los equipos de imagen y sonido. Mantenimiento
> preventivo, actualización y reconfiguración y verificación de los equipos de imagen y sonido.»
>
> «MANTENIMIENTO CORRECTIVO DE EQUIPOS: Técnicas de diagnóstico y localización de averías de los
> equipos de imagen y sonido. Técnicas de mantenimiento correctivo, actualización y reconfiguración y
> verificación en los equipos de imagen y sonido.»

**Este tema reúne dos puntos del anexo**, y **conviene decir por qué**: **los enunciados 17 y 18 son la
misma frase con una palabra cambiada** —«preventivo» y «correctivo»—, **y el examen los ha tratado
como uno solo.** **Separarlos daría dos temas que se repetirían entre sí**, que es lo que el manual de
este proyecto prohíbe.

**Dos preguntas.** **Y las dos son de mantenimiento correctivo**: **una soldadura que sale mal y un
amplificador que zumba.** **Del preventivo no ha caído ninguna**, y eso se dice porque **cambia lo que
hay que estudiar de cada mitad**: **del correctivo, el método; del preventivo, el calendario.**

<!-- indice -->

## Índice

- [1. Los dos mantenimientos](#1-los-dos-mantenimientos)
- [2. El método del correctivo](#2-el-método-del-correctivo)
- [3. La soldadura fría](#3-la-soldadura-fría)
- [4. El zumbido de 50 hercios](#4-el-zumbido-de-50-hercios)
- [5. Los datos que el examen ha preguntado](#5-los-datos-que-el-examen-ha-preguntado)
- [6. Trazabilidad](#6-trazabilidad)

<!-- /indice -->

## 1. Los dos mantenimientos

**La diferencia no está en lo que se hace, sino en cuándo se hace:**

| | **Preventivo** | **Correctivo** |
|---|---|---|
| **Cuándo se hace** | **Antes de que falle, según calendario o según horas de uso** | **Después de que ha fallado** |
| **Quién decide el momento** | **El plan de mantenimiento** | **La avería** |
| **Qué cuesta** | **Horas previstas, en horario elegido** | **Horas imprevistas, a menudo en directo** |
| **Qué se gana** | **Que la avería no llegue, o llegue avisada** | **Nada: se recupera lo que ya se perdió** |

**Y la regla económica que ordena los dos**: **una hora de preventivo cuesta menos que una hora de
correctivo, porque la de correctivo se paga además con la emisión.** **De ahí que en una instalación
de televisión el preventivo se haga de madrugada y en los huecos de programación.**

**Lo que un plan de preventivo contiene, que es lo que el enunciado del punto 17 nombra:**

| Tarea | Cada cuánto, típicamente |
|---|---|
| **Limpieza de filtros de aire y ventiladores** | **La más frecuente de todas**: un equipo que no ventila se recalienta y envejece antes |
| **Limpieza de ópticas y de superficies de contacto** | **Periódica** |
| **Comprobación de baterías y de sistemas de alimentación ininterrumpida** | **Periódica, con prueba de descarga** |
| **Verificación de medidas: niveles, sincronismos, respuesta** | **Con los instrumentos del tema 13** |
| **Actualización de programas y de configuraciones** | **En ventana programada y con vuelta atrás preparada** |
| **Copia y archivo de las configuraciones de cada equipo** | **Después de cada cambio** |
| **Manipulación del material con protección contra descargas electrostáticas** | **Siempre que se abra un equipo**: pulsera a tierra, tapete conductor y bolsa antiestática para las tarjetas |

**La última fila merece una línea, porque es la que más material estropea sin que nadie se entere**:
**una descarga electrostática de las que uno ni siente puede dañar una entrada de circuito integrado
sin destruirla del todo**, y **el equipo sigue funcionando hasta que falla semanas después.** **Es la
misma clase de avería diferida que la soldadura fría del epígrafe 3.**

**Los dos avisos del preventivo que más veces se olvidan:**

- **Una actualización es un cambio, y un cambio se planifica.** **Actualizar el programa de un equipo
  la víspera de un directo es correctivo disfrazado de preventivo.** **La regla es tener guardada la
  versión anterior y saber cómo se vuelve a ella antes de empezar.**
- **La configuración de un equipo vale tanto como el equipo.** **Un equipo de repuesto sin la
  configuración del averiado no sustituye a nada.** **Por eso la copia de configuraciones es parte
  del preventivo y no del archivo.**

## 2. El método del correctivo

**El enunciado del punto 18 habla de «técnicas de diagnóstico y localización de averías»**, y **el
método tiene un orden que conviene respetar porque ahorra la mayor parte del trabajo:**

1. **Reproducir la avería.** **Una avería que no se reproduce no se puede arreglar ni comprobar.**
   **El primer trabajo es saber en qué condiciones exactas aparece.**
2. **Delimitar la mitad averiada.** **Se busca un punto intermedio de la cadena y se mira si allí la
   señal está bien.** **Si lo está, el fallo va después; si no, va antes.** **Cada comprobación parte
   en dos lo que queda por mirar.**
3. **Separar lo eléctrico de lo lógico.** **Un equipo que no arranca y uno que arranca y no hace lo
   que debe son dos averías de familias distintas.**
4. **Sustituir por un elemento sano y comprobar.** **Cambiar el cable, cambiar la tarjeta, cambiar la
   fuente.** **Es lo más rápido cuando hay repuesto, y lo que la explotación normalmente exige.**
5. **Confirmar que la avería ha desaparecido con la misma prueba del paso 1**, y **sólo entonces
   devolver el equipo al servicio.**

**El paso 2 tiene nombre y merece una línea aparte**: **es la búsqueda binaria, y es lo que separa un
diagnóstico de una hora de uno de un día.** **Una cadena de doce etapas se recorre en cuatro medidas si
se parte por la mitad y en doce si se va de una en una.** **La pareja generador-osciloscopio del tema
13 es el instrumento de ese método.**

**Y el aviso de fondo del correctivo**: **el síntoma no es la avería.** **Un monitor sin imagen puede
tener el fallo en el monitor, en el cable, en el distribuidor, en la matriz o en la fuente.** **Los
dos casos que el examen ha preguntado son, precisamente, dos síntomas cuyo origen hay que deducir.**

## 3. La soldadura fría

**La pregunta 63 es negativa**: **la respuesta que NO es una causa válida de una soldadura fría es la
estabilidad durante el enfriamiento del metal de soldadura.** Ésa es la respuesta oficial.

---

**Qué es una soldadura fría**: **una unión que parece hecha y no lo está.** **El estaño se ha
depositado sobre las piezas pero no ha llegado a mojarlas ni a formar aleación con ellas**, de modo
que **hay contacto mecánico y no hay contacto eléctrico fiable.** **Se reconoce por su aspecto mate,
granuloso y abombado**, frente al brillante y cóncavo de una soldadura buena.

**Y es la avería más traicionera del oficio**, porque **funciona al principio.** **La unión conduce el
día que se hace y deja de conducir semanas después, con la vibración o con el ciclado térmico**, y
entonces **produce fallos intermitentes que no se reproducen cuando uno mira.**

**Las cuatro causas que las opciones barajan, con su veredicto:**

| Opción | Qué describe | Veredicto |
|---|---|---|
| **a) Estabilidad durante el enfriamiento** | **Que las piezas no se muevan mientras el estaño solidifica** | **Es la condición de una soldadura *buena***, no una causa de fallo ✔ |
| **b) Superficie sin limpiar** | **Óxido, grasa o suciedad entre el estaño y el metal** | **Causa real**: el estaño no puede mojar lo que no toca |
| **c) Poca cantidad de soldadura** | **Estaño insuficiente para cubrir la unión** | **Causa real** |
| **d) Punta del soldador poco caliente** | **El estaño se funde pero las piezas no alcanzan temperatura** | **Causa real, y la más frecuente de las tres** |

**La palabra que resuelve la pregunta es «estabilidad».** **Lo que estropea una soldadura es el
movimiento durante el enfriamiento, no la estabilidad**: **si las piezas se mueven mientras el estaño
solidifica, la aleación se rompe por dentro y sale una soldadura fría.** **La opción a nombra
justamente lo contrario del defecto**, y **por eso es la única de las cuatro que no es una causa.**

**El aviso de oficio, que es lo que hay que llevar aprendido**: **hay que calentar la pieza, no el
estaño.** **La punta se apoya a la vez en la patilla y en la isla, se espera un par de segundos y se
acerca el estaño al conjunto caliente, no a la punta.** **El estaño fundido sobre piezas frías es la
receta exacta de la soldadura fría.**

## 4. El zumbido de 50 hercios

**La pregunta 29 del segundo cuadernillo**: **en un amplificador de audio que presenta un zumbido
constante de 50 Hz en la salida, la causa más probable es un condensador de filtrado defectuoso en la
fuente de alimentación.** Ésa es la respuesta oficial.

---

**Y esta pregunta es un ejemplo perfecto de deducir el origen a partir del síntoma**, **porque la
cifra del enunciado lo dice todo: cincuenta hercios es la frecuencia de la red eléctrica en España.**
**Un zumbido a esa frecuencia exacta no viene de la señal: viene de la alimentación.**

**Cómo funciona una fuente de alimentación lineal, que es lo que hay que tener claro:**

1. **El transformador baja la tensión de red**, que sigue siendo alterna a cincuenta hercios.
2. **El rectificador la convierte en una tensión que ya no cambia de signo pero sí de valor**: es una
   sucesión de jorobas.
3. **El condensador de filtrado alisa esas jorobas** hasta dejar una tensión casi constante.
4. **Lo que queda de ondulación después del condensador se llama rizado**, y **su frecuencia es la de
   red o su doble, según cómo esté hecho el rectificador.**

**Y ahí está la avería**: **un condensador de filtrado envejecido pierde capacidad**, **el rizado
crece**, y **esa ondulación se cuela en la etapa amplificadora y sale por el altavoz como un zumbido
grave y constante.**

**Las tres opciones falsas, y por qué el síntoma no encaja con ninguna:**

| Opción | Qué síntoma daría en realidad |
|---|---|
| **b) Transistor de salida en cortocircuito** | **Silencio, distorsión brutal o tensión continua en el altavoz**: la avería suele llevarse el altavoz por delante, y no produce un zumbido limpio |
| **c) Resistencia de polarización abierta en el preamplificador** | **Ausencia de señal en ese canal o distorsión por polarización perdida**, no un tono de red |
| **d) Fusible quemado en la alimentación de los altavoces** | **Silencio absoluto en la vía protegida**: un fusible fundido no produce sonido, lo quita |

**La regla de diagnóstico que este caso enseña, y vale para muchas más averías**: **la frecuencia del
ruido dice de dónde viene.**

| Frecuencia del zumbido o ruido | De dónde viene |
|---|---|
| **50 Hz** | **De la red**: filtrado de la fuente, o un bucle de masa que capta el campo de red |
| **100 Hz** | **Del rizado de un rectificador de doble onda**: también la fuente |
| **Un silbido agudo y constante** | **De la conmutación de una fuente conmutada** |
| **Un siseo de banda ancha** | **Ruido térmico**: ganancia excesiva en una etapa de entrada |
| **Un crujido intermitente** | **Contacto malo**: conector sucio, soldadura fría del epígrafe anterior |

**Y el matiz que separa las dos causas de zumbido de red**: **si el zumbido cambia al tocar o mover los
cables de señal, es un bucle de masa; si no cambia, es la fuente.** **La pregunta dice «constante»**,
y esa palabra apunta a la fuente.

## 5. Los datos que el examen ha preguntado

| Nº | Qué pide | Respuesta oficial |
|---|---|---|
| 63 | Causa que NO lo es de una soldadura fría | a) La estabilidad durante el enfriamiento ✔ |
| 29 (2.º llam.) | Causa más probable de un zumbido constante de 50 Hz | a) Condensador de filtrado defectuoso ✔ |

**Las dos respuestas oficiales son correctas**, y **ninguna descansa en la plantilla**: **las dos se
razonan desde el síntoma.**

**El aviso de estudio**: **este punto tiene dos preguntas y un enunciado doble, y las dos preguntas
caídas son de correctivo.** **Lo que más rinde es el cuadro de frecuencias del epígrafe 4 y el aspecto
de una soldadura mala**, **porque son las dos formas en que este oficio reconoce una avería antes de
medir nada.** **Del preventivo, lo preguntable es el calendario de tareas y la disciplina de guardar
configuraciones.**

## 6. Trazabilidad

**Este tema no cita ninguna fuente de forma literal.**

**Cuatro declaraciones expresas:**

1. **Los cincuenta hercios de la red eléctrica española son un dato de conocimiento común**, y **es
   además el dato que el propio enunciado de la pregunta 29 proporciona.** **El temario no lo
   atribuye a ninguna norma.**
2. **La descripción de la soldadura fría, sus causas y su aspecto es oficio de taller.** **No se ha
   consultado ninguna norma de soldadura de material electrónico**, y **la pregunta 63 se contesta
   por eliminación de las tres causas reales, razonamiento que queda escrito.**
3. **El funcionamiento de una fuente de alimentación lineal y el origen del rizado del epígrafe 4 son
   materia del tema 3 de esta misma ocupación**, donde se tratan como electrónica de potencia.
   **Ninguna norma se ha consultado para ellos.**
4. **El cuadro de tareas de preventivo del epígrafe 1 y su periodicidad son orientativos.** **No
   proceden de ningún plan de mantenimiento de RTVE ni de ninguna documentación de la corporación**,
   y **el temario no los presenta como el plan de nadie**: son el contenido habitual de un plan de
   este tipo, escrito como guía de estudio.

**El resto del tema va como oficio y así se declara**: la tabla que separa los dos mantenimientos, los
dos avisos sobre actualizaciones y configuraciones, los cinco pasos del método correctivo, la búsqueda
binaria, la clasificación de las opciones falsas de las dos preguntas y el cuadro de frecuencias de
ruido. **Nada de eso está en un boletín oficial ni en una norma técnica de las consultadas**, y el
tema no lo presenta como si lo estuviera.
