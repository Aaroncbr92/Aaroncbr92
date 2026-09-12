# Tema 13 del específico de Enfermería de Empresa · Estadística descriptiva e inferencial

<!-- portada -->

|  |  |
| --- | --- |
| **Bloque** | Temario específico · Enfermería de Empresa · punto 13 |
| **Sirve para** | **Enfermería de Empresa** |
| **Fuente** | **Sin norma en el enunciado.** La única fuente citada es la **NTP 1211, «Estadísticas de accidentabilidad en la empresa»**, del INSST, 2024; el resto del tema va como oficio declarado |
| **Identificador** | **NTP 1211** |
| **Redacción que se estudia** | Los documentos técnicos del Instituto y del Ministerio, **en la edición que cada uno lleva impresa** |
| **Extensión** | **5.169 palabras** |

<!-- /portada -->

Las siglas de este tema, presentadas de entrada: las Notas Técnicas de Prevención (**NTP**) del
Instituto Nacional de Seguridad y Salud en el Trabajo (**INSST**); el Instituto Nacional de Estadística
(**INE**); y las cuatro abreviaturas con que la NTP que aquí se usa nombra los índices de
siniestralidad y los límites de su control estadístico: el índice de incidencia (**II**), el índice de
frecuencia (**IF**), el índice de gravedad (**IG**), el índice de frecuencia esperado (**IFe**) y los
límites superior (**LS**) e inferior (**LI**).

> Enunciado del programa (Anexo 1 de las Bases de la Convocatoria de Banco de Datos de RTVE, temario
> de la ocupación tipo de Enfermería de Empresa, punto 13):
> «13. La estadística descriptiva: Variables cualitativas y cuantitativas. Variables discretas y
> continuas. Representación gráfica. Medidas de posición. Medidas de dispersión. La estadística
> inferencial: Conceptos básicos. La estimación puntual. El contraste de hipótesis. El Muestreo.
> Errores de muestreo. Intervalos de confianza.»

**El aviso de procedencia de este volumen está entero en el tema 1 y vale aquí.**

**Y este punto obliga a una advertencia de método distinta de las anteriores, porque aquí lo que se
desarrolla no son hechos: son definiciones.**

**La estadística general —qué es una variable cualitativa, qué es una media, qué es un intervalo de
confianza— no es una afirmación sobre el mundo que haya que sostener en una fuente.** **Es
matemática**, y **este tema la desarrolla como oficio declarado, sin atribuirla a ningún autor, sin
citar ninguna escuela y sin dar ninguna cifra.**

**Lo que sí tiene fuente, y muy buena, es la aplicación de todo eso a la salud laboral.** La
NTP 1211, «Estadísticas de accidentabilidad en la empresa», de 2024, **se ha descargado, leído entera y
guardada en el proyecto**, y **es la que da las fórmulas de los cuatro índices de siniestralidad con
sus constantes, la definición de hora efectivamente trabajada y un método completo de control
estadístico con intervalos de confianza.** **Esa NTP dice de sí misma que sustituye a la NTP 1, a la
NTP 2 y a la NTP 236.**

**De modo que este tema se reparte así:**

| Rúbrica del enunciado | Cómo se desarrolla |
|---|---|
| **Variables, representación gráfica, medidas de posición y de dispersión** | **Como oficio declarado**, con ejemplos de la consulta de empresa |
| **Los índices de siniestralidad** | Citados de la **NTP** 1211, **que cierra la laguna que el tema 1 dejó abierta** |
| **Inferencia, estimación, contraste, muestreo, errores e intervalos de confianza** | **Como oficio declarado** en su parte conceptual, y citados de la **NTP** 1211 **en su aplicación al control de la siniestralidad** |

<!-- indice -->

## Índice

- [1. Variables: los dos cortes que hay que saber hacer](#1-variables-los-dos-cortes-que-hay-que-saber-hacer)
- [2. Representación gráfica](#2-representación-gráfica)
- [3. Medidas de posición](#3-medidas-de-posición)
- [4. Medidas de dispersión](#4-medidas-de-dispersión)
- [5. Los índices de siniestralidad, con su fórmula](#5-los-índices-de-siniestralidad-con-su-fórmula)
- [6. Qué cuenta como hora trabajada](#6-qué-cuenta-como-hora-trabajada)
- [7. Estadística inferencial: los conceptos](#7-estadística-inferencial-los-conceptos)
- [8. La inferencia aplicada: el método de las líneas límite](#8-la-inferencia-aplicada-el-método-de-las-líneas-límite)
- [9. Qué hace la enfermería del trabajo](#9-qué-hace-la-enfermería-del-trabajo)
- [10. Lo que este tema no da, y dónde está](#10-lo-que-este-tema-no-da-y-dónde-está)
- [11. Trazabilidad](#11-trazabilidad)

<!-- /indice -->

## 1. Variables: los dos cortes que hay que saber hacer

**Todo lo que sigue en este epígrafe va como oficio.**

**El primer corte, por la naturaleza del dato:**

| Tipo | Qué es | Ejemplo en una consulta de empresa |
|---|---|---|
| **Cualitativa** | **Clasifica en categorías; no se puede operar aritméticamente con ella** | **Sexo, puesto de trabajo, turno, tipo de accidente, apto o no apto** |
| **Cuantitativa** | **Se expresa con un número con el que sí se puede operar** | **Edad, años de exposición, decibelios, capacidad vital forzada, días de baja** |

**Y dentro de las cualitativas conviene distinguir dos**, porque **decide qué se puede hacer con
ellas**: **las NOMINALES, que sólo nombran —sexo, turno, servicio—, y las ORDINALES, que además
ordenan sin que la distancia entre categorías signifique nada —leve, grave, muy grave; nunca, a veces,
siempre—.**

**El segundo corte se aplica sólo a las cuantitativas:**

| Tipo | Qué es | Ejemplo |
|---|---|---|
| **Discreta** | **Sólo toma valores aislados, normalmente por conteo** | **Número de accidentes en un mes, número de dosis de vacuna, número de bajas** |
| **Continua** | **Puede tomar cualquier valor dentro de un intervalo, y sólo la precisión del aparato limita los decimales** | **Talla, peso, nivel de ruido, volumen espirado, concentración de un contaminante** |

**Las dos consecuencias prácticas que ese doble corte tiene, y que son lo que un examen quiere ver:**

1. **El tipo de variable decide el estadístico.** **De una cualitativa se dan frecuencias y porcentajes,
   nunca una media.** **Una «media de turnos» no significa nada.**
2. **El tipo de variable decide el gráfico.** **Y ése es el epígrafe siguiente.**

**Y una advertencia de oficio que en salud laboral vale oro**: **una variable continua se convierte en
cualitativa en cuanto se agrupa en categorías —«normal / alterado», «apto / no apto»—**, y **esa
conversión SIEMPRE pierde información.** **Convertir una espirometría en un sí o un no descarta la
magnitud del cambio**, que **es justamente lo que permite ver una tendencia a lo largo de los años.**
**Se agrupa para decidir; se conserva el número para comparar.**

## 2. Representación gráfica

**La parte conceptual va como oficio.** **La regla es una sola y de ella sale todo:**

| Qué se representa | Gráfico adecuado |
|---|---|
| **Una cualitativa** | **Diagrama de barras separadas o de sectores** |
| **Una cuantitativa discreta** | **Diagrama de barras** |
| **Una cuantitativa continua agrupada en intervalos** | **HISTOGRAMA, con las barras pegadas** |
| **Una cuantitativa a lo largo del tiempo** | **Gráfico de líneas** |
| **Dos cuantitativas entre sí** | **Nube de puntos** |

**La diferencia que más se pregunta y que casi nadie sabe explicar**: **en un diagrama de barras las
barras van SEPARADAS porque las categorías no son contiguas; en un histograma van PEGADAS porque los
intervalos sí lo son.** **No es una convención estética: es la representación de si hay o no continuidad
entre una clase y la siguiente.**

**Y la aplicación que sí tiene fuente.** La NTP 1211 **usa dos gráficos concretos para vigilar la
siniestralidad de una empresa**, citados:

> «En esta NTP, se tratan, concretamente, **el diagrama de IF mes a mes y el diagrama de IF anual
> acumulado**.»

---

**La diferencia entre esos dos gráficos es de las cosas más útiles de este tema:**

1. **El diagrama mes a mes es sensible y ruidoso.** **Un mes con dos accidentes más se nota mucho**,
   y **buena parte de ese movimiento es azar.**
2. **El diagrama anual acumulado es lento y estable.** **Cada punto arrastra todo lo anterior**, de
   modo que **suaviza el ruido y enseña la tendencia**, pero **tarda en reaccionar a un cambio real.**
3. **Por eso se miran los dos.** **Uno avisa pronto y se equivoca a menudo; el otro avisa tarde y se
   equivoca poco.**

## 3. Medidas de posición

**Oficio declarado.** **Sirven para responder a «¿por dónde va este conjunto de datos?».**

| Medida | Qué es | Cuándo se prefiere |
|---|---|---|
| **Media aritmética** | **La suma de los valores dividida por cuántos son** | **Cuando la distribución es simétrica y no hay valores extremos** |
| **Mediana** | **El valor que deja la mitad de los datos por debajo y la mitad por encima** | **Cuando hay valores extremos o la distribución es asimétrica** |
| **Moda** | **El valor que más se repite** | **Es la única que sirve para una variable cualitativa** |
| **Cuantiles** | **Los valores que parten la distribución en partes iguales**: cuartiles en cuatro, deciles en diez, percentiles en cien | **Para situar a un individuo dentro de su grupo** |

**La regla que hay que llevar sabida, con un ejemplo de la consulta**: **la media es sensible a los
valores extremos y la mediana no.** **En una plantilla de cincuenta personas donde cuarenta y nueve han
tenido cero días de baja y una ha tenido trescientos, la media de días de baja es seis y la mediana es
cero.** **La media dice que la plantilla pierde seis días por cabeza, lo cual es falso para las
cuarenta y nueve.** **En siniestralidad y en absentismo, donde casi siempre unos pocos casos concentran
casi todo, la mediana describe mejor a la mayoría y la media describe mejor el coste total.** **Las dos
son ciertas y responden a preguntas distintas.**

**Y el percentil merece una frase propia porque es lo que un sanitario usa a diario**: **decir que una
capacidad vital está en el percentil 15 sitúa a esa persona respecto de su población de referencia**, y
**eso es más informativo que el valor absoluto**, como **se vio en el tema 8 con los valores teóricos.**

## 4. Medidas de dispersión

**Oficio declarado.** **Responden a «¿cuánto se separan los datos entre sí?», que es la pregunta que
completa la anterior.**

| Medida | Qué es |
|---|---|
| **Recorrido o rango** | **La diferencia entre el valor máximo y el mínimo** |
| **Recorrido intercuartílico** | **La diferencia entre el tercer y el primer cuartil**: el rango del 50 % central |
| **Varianza** | **La media de los cuadrados de las desviaciones respecto de la media** |
| **Desviación típica** | **La raíz cuadrada de la varianza**, con lo que **vuelve a las unidades originales** |
| **Coeficiente de variación** | **La desviación típica dividida por la media**: es **relativo y sin unidades** |

**Tres cosas de esa tabla y ninguna es trivial:**

1. **La desviación típica existe porque la varianza está en unidades al cuadrado.** **Una varianza de
   días de baja se mide en días al cuadrado, que no significa nada.** **La raíz devuelve los días.**
2. **El coeficiente de variación es el único que permite comparar la dispersión de dos variables
   distintas.** **No se puede decir si hay más dispersión en la talla o en el nivel de ruido comparando
   sus desviaciones típicas, porque están en unidades distintas**; **dividiendo cada una por su media,
   sí.**
3. **Una media sin una medida de dispersión no informa: engaña.** **Dos servicios con la misma media de
   edad, uno con todos entre cuarenta y cuarenta y cinco y otro mitad de veinticinco y mitad de sesenta,
   necesitan políticas de prevención distintas**, y **la media no los distingue.**

## 5. Los índices de siniestralidad, con su fórmula

**Aquí termina el oficio y empieza la fuente.** **El tema 1 de este volumen dijo expresamente que no
daba las constantes de estos índices porque no se había consultado la fuente; ahora se ha consultado y
aquí van.**

La NTP 1211 **los presenta así**, citada:

> «se exponen los siguientes índices estadísticos: **el índice de incidencia, de frecuencia, de gravedad
> y la duración media de las bajas**.»

---

**El índice de incidencia**, citado:

> «**El índice de incidencia relaciona el número de accidentes de trabajo ocurridos con el número de
> personas trabajadoras expuestas al riesgo** (Ecuación 1). **Representa el número de accidentes
> ocurridos por cada cien mil personas trabajadoras expuestas** y **puede utilizarse cuando no se
> dispone de información sobre el número de horas-persona trabajadas**.»

---

**El índice de frecuencia**, citado:

> «**El índice de frecuencia relaciona el número de accidentes de trabajo con el número total de horas
> trabajadas por el colectivo de personas trabajadoras expuestas al riesgo** (Ecuación 3). **Representa
> el número de accidentes ocurridos por cada millón de horas trabajadas** y, en el caso de accidentes
> mortales, **por cada 100 millones de horas trabajadas**.»

---

**Y la comparación entre los dos que la propia NTP hace**, citada:

> «El cálculo de este índice, además de permitir la comparación entre datos de diferentes empresas o
> administraciones públicas, sectores o áreas geográficas, **aporta información para la valoración del
> riesgo de que ocurra el accidente**. Se podría decir que **aporta información más precisa que el
> índice de incidencia**.»

---

**El índice de gravedad**, citado:

> «**El índice de gravedad** (Ecuación 5) **relaciona el número de días de ausencia en el trabajo como
> consecuencia de los accidentes de trabajo con el tiempo trabajado por las personas expuestas al
> riesgo. Representa el número de días de baja por cada mil horas trabajadas.**»

---

**Y la duración media de las bajas**, citada:

> «Este indicador **relaciona el número de días de baja como consecuencia de los accidentes de trabajo
> con el número de accidentes de trabajo ocurridos** (Ecuación 6). **Permite cuantificar el tiempo
> medio de duración de la baja por accidente.**»

---

**Los cuatro, en un cuadro que ya se puede dar entero:**

| Índice | Qué relaciona | Constante |
|---|---|---|
| **Incidencia** | **Accidentes con personas expuestas** | **Por cada cien mil personas** |
| **Frecuencia** | **Accidentes con horas trabajadas** | **Por cada millón de horas**; los mortales, por cada cien millones |
| **Gravedad** | **Días de baja con horas trabajadas** | **Por cada mil horas** |
| **Duración media** | **Días de baja con accidentes** | **Ninguna: es una media** |

**Y dos precisiones de la NTP que valen una pregunta cada una.**

**La primera, sobre qué es un accidente mortal**, citada:

> «**Un accidente de trabajo mortal es el que ocasiona la muerte de la persona trabajadora accidentada
> en el plazo de un año desde la fecha del accidente.** Esto da lugar a que **un accidente que
> inicialmente se calificó como grave (o incluso leve) sea recalificado como mortal si la persona
> trabajadora fallece como consecuencia de este.**»

---

**Un año, y con recalificación retroactiva.** **Eso significa que las cifras de siniestralidad mortal de
un ejercicio no son definitivas hasta un año después**, y **explica por qué los datos de accidentes se
revisan.**

**La segunda, sobre los días de baja**, citada:

> «**los días de duración de las bajas son los días naturales que la persona trabajadora accidentada
> permanece en situación de incapacidad temporal.** Los días se contabilizan **desde la fecha de baja
> hasta la fecha de alta, ambos días inclusive**, pertenecientes al periodo de baja inicial, de forma
> que **se excluyen en el cómputo total los días de baja debidos a recaídas posteriores.**»

---

**Días NATURALES, ambos extremos incluidos, y sin las recaídas.** **Las tres precisiones cambian el
número**, y **la NTP añade que ese concepto sustituye al de «jornadas no trabajadas» que el Ministerio
de Trabajo empleaba hasta 2015.**

## 6. Qué cuenta como hora trabajada

**Los dos índices que llevan horas en el denominador dependen de qué se cuente como hora**, y **la NTP
lo resuelve remitiendo al criterio del Instituto Nacional de Estadística.** **Es una lista cerrada y de
las que un tribunal pide entera.**

**Lo que SÍ son horas de trabajo efectivas**, citado:

> «**Las horas trabajadas durante el tiempo de trabajo.**
> **El tiempo empleado en el lugar de trabajo esperando o permaneciendo disponible.**
> **Los períodos de descanso en el centro de trabajo, incluidas las pausas para las comidas inferiores a
> una hora.**»

---

**Lo que NO**, citado:

> «**Las vacaciones.**
> **Los días festivos.**
> **Las ausencias por enfermedad y otros motivos pagados.**
> **El tiempo no trabajado por estar afectado por una regulación de empleo.**
> **El tiempo invertido en desplazamientos al o desde el lugar de trabajo.**
> **Las pausas para las comidas superiores a una hora.**»

---

**Dos observaciones que ordenan las dos listas:**

1. **El criterio no es «estar trabajando»: es estar a disposición en el lugar de trabajo.** **Esperar
   cuenta.** **Y la pausa de comida cuenta o no según dure menos o más de una hora**, que **es una
   frontera arbitraria pero cerrada, y por eso comparable.**
2. **El desplazamiento al trabajo NO cuenta como hora trabajada**, y **eso encaja con lo visto en el
   tema 12**: **los índices de incidencia y frecuencia tampoco cuentan en el numerador los accidentes
   in itinere.** **Numerador y denominador son coherentes: los dos se refieren a la jornada.**

## 7. Estadística inferencial: los conceptos

**Vuelve el oficio declarado.**

**El problema que la inferencia resuelve, en una frase**: **casi nunca se puede medir a toda la
población, y hay que decir algo de ella habiendo medido sólo a una parte.**

**El vocabulario mínimo, que hay que usar con precisión:**

| Término | Qué es |
|---|---|
| **Población** | **El conjunto entero sobre el que se quiere concluir** |
| **Muestra** | **El subconjunto que efectivamente se observa** |
| **Parámetro** | **El valor VERDADERO en la población**: siempre desconocido |
| **Estadístico o estimador** | **El valor calculado en la muestra**: es lo que se conoce |
| **Estimación puntual** | **Dar un único número como valor probable del parámetro** |
| **Estimación por intervalo** | **Dar un rango dentro del cual se cree que está el parámetro, con una confianza dada** |

**La distinción entre parámetro y estadístico es la que hay que tener clarísima**: **el parámetro no se
conoce nunca; se estima.** **Toda la inferencia consiste en decir cuánto puede alejarse el estadístico
del parámetro.**

**La estimación puntual y su límite**: **da un número y no dice nada de su precisión.** **Una media de
edad de 44,3 años calculada sobre doce personas y otra calculada sobre mil dan el mismo número y no
merecen la misma confianza.** **Por eso una estimación puntual sin intervalo está incompleta.**

**El intervalo de confianza**, con **la advertencia que más se falla**: el nivel de confianza —95 %, 90 %— **se refiere al PROCEDIMIENTO, no a ese intervalo concreto.** **Quiere decir que si se repitiese el
muestreo muchas veces, ese porcentaje de los intervalos construidos así contendría el parámetro.**
**Y dos cosas lo estrechan: más muestra y menos dispersión.** **Un intervalo ancho no es un fallo del
cálculo: es la manera honrada de decir que se sabe poco.**

**El contraste de hipótesis, en sus cuatro pasos:**

1. **Se formula una hipótesis nula —que no hay diferencia, que no hay efecto— y su alternativa.**
2. **Se elige un nivel de significación, que es el riesgo que se acepta de rechazar la nula siendo
   cierta.**
3. **Se calcula, a partir de la muestra, la probabilidad de observar lo observado si la nula fuese
   cierta.**
4. **Se rechaza o no se rechaza la nula.**

**Y las tres advertencias que evitan los errores más caros:**

1. **Nunca se «acepta» la hipótesis nula: no se rechaza.** **No encontrar diferencia no es demostrar
   que no la haya**; **puede ser que la muestra fuese pequeña.**
2. **Significación estadística no es importancia.** **Con una muestra suficientemente grande, una
   diferencia diminuta sale significativa**, y **una diferencia de dos decibelios o de medio milímetro
   puede no tener ninguna consecuencia para la salud.** **Lo contrario también pasa: una diferencia
   clínicamente relevante puede no salir significativa por falta de muestra.**
3. **Hay dos maneras de equivocarse y son distintas**: **decir que hay efecto cuando no lo hay, y no
   verlo cuando lo hay.** **En prevención, la segunda suele ser la más cara**, porque **deja una
   exposición sin corregir.**

**El muestreo y sus errores:**

| Concepto | Qué es |
|---|---|
| **Muestreo aleatorio** | **Aquel en que cada individuo tiene una probabilidad conocida de entrar en la muestra**: es el que permite calcular el error |
| **Error de muestreo** | **La diferencia entre el estadístico y el parámetro debida sólo al azar de haber cogido a unos y no a otros**: **disminuye al aumentar la muestra** |
| **Error ajeno al muestreo** | **El que no viene del azar**: mala medición, mala selección, no respuesta. **NO disminuye al aumentar la muestra** |

**La regla que de esa tabla sale, y es la más importante de todo el epígrafe**: **aumentar la muestra
sólo corrige el error aleatorio.** **Una muestra mal elegida no mejora por ser grande: mide con más
precisión una cosa equivocada.** **Los sesgos y la validez son materia del tema 14.**

## 8. La inferencia aplicada: el método de las líneas límite

**Y aquí todo lo anterior se junta en un procedimiento real, publicado y citable.**

**Qué es**, citado de la NTP 1211:

> «**Este método de control estadístico consiste en el cálculo de unos valores (límite superior, LS, y
> límite inferior, LI) que delimitan un intervalo de valores aceptables, con un nivel de confianza
> determinado, en función del número de horas trabajadas y del IF esperado**, y en la posterior
> comparación de dichos límites con los IF.»

---

**Para qué sirve, que es la frase clave**, citada:

> «**El método permite detectar, a través de la evolución del IF, si los cambios experimentados son
> debidos a una fluctuación aleatoria o a la entrada de un nuevo factor que ha podido modificar las
> condiciones de trabajo.**»

---

**Ésa es exactamente la pregunta de la inferencia aplicada a una empresa**: **este mes ha habido más
accidentes que el anterior, ¿es azar o ha cambiado algo?** **Un servicio de prevención que reacciona a
cada subida mensual persigue ruido; uno que no reacciona nunca se pierde los cambios reales.** **El
método pone una frontera calculada entre las dos cosas.**

**De dónde sale el índice esperado**, citado:

> «**El IF esperado es un valor previamente fijado por la empresa o administración pública que podrá ser
> o bien el mismo del año anterior, o bien un valor inferior fundamentado en una política de objetivos
> de prevención** de riesgos laborales buscando reducir los accidentes de trabajo.»

---

**Y los tres casos, según cuántas horas haya en el periodo**, citados:

> «**Caso 1. Si, en el periodo considerado, el número de horas trabajadas (N) es inferior a 10.000, no
> es aplicable este método**, debiéndose acumular las horas de dos o más meses consecutivos para poder
> aplicarlo»

---

> «**Caso 2. Si, en el período considerado, N es superior a 10.000 pero inferior a 1.200.000, los
> accidentes de trabajo siguen la distribución de Poisson.** Esto es porque **las propiedades
> estadísticas de los accidentes de trabajo se ajustan a esta distribución.**»

---

> «**Caso 3. Si, en el período considerado, N es superior a 1.200.000**, es decir, N toma valores altos,
> **la distribución de los accidentes de trabajo, que siguen la Ley Poisson, se asemeja a la Normal.**»

---

**Tres lecturas de esos tres casos, y son la mejor síntesis de este tema:**

1. **Con pocas horas no se puede inferir nada, y la NTP lo dice en vez de disimularlo.** **La solución
   que propone no es bajar el listón: es acumular periodos hasta tener datos suficientes.** **Es
   exactamente la lección del epígrafe 7 sobre el tamaño de la muestra.**
2. **Los accidentes de trabajo siguen la distribución de Poisson**, que **es la de los sucesos raros
   contados en un intervalo.** **Esa afirmación no es un supuesto de este temario: la hace la NTP con
   esas palabras.**
3. **Cuando el número de horas es muy grande, la Poisson se parece a la Normal.** **Ésa es la razón de
   que en una empresa grande se puedan usar las fórmulas habituales y en una pequeña no.**

**Y la NTP añade que la ecuación de los límites se construye para un intervalo de confianza del 90 %**,
**y que la aproximación del caso 2 vale también para cualquier número de horas porque su término
adicional se hace despreciable al crecer las horas.** **Eso se resume y no se cita.**

**Lo que este tema NO da de ese método**: **las ecuaciones de los límites.** **La NTP las publica como
imágenes de fórmula y su extracción automática de texto las devuelve ilegibles**, de modo que
**transcribirlas aquí sería copiar lo que no se ha podido leer con seguridad.** **Se declara en el
epígrafe 10 y se dice dónde están.**

## 9. Qué hace la enfermería del trabajo

**Cinco tareas, y ninguna consiste en hacer estadística por hacerla:**

1. **Elegir el estadístico según el tipo de variable**: frecuencias para lo cualitativo, media o mediana
   para lo cuantitativo según haya o no valores extremos.
2. **No dar nunca una medida de posición sin una de dispersión.**
3. **Calcular los índices con la fórmula oficial y las horas bien contadas**, para que **los números de
   la empresa sean comparables con los de su sector.**
4. **Distinguir el ruido del cambio** antes de proponer una medida, con el método de líneas límite o con
   el criterio que sea, **y no reaccionar a cada oscilación mensual.**
5. **Traducir el resultado a una decisión preventiva**, que es lo que el artículo 37.3.f) del
   Reglamento de los Servicios de Prevención pide al personal sanitario: **analizar con criterios
   epidemiológicos y PROPONER medidas.**

**Y la advertencia con que se cierra el tema**: **en una empresa mediana los números de siniestralidad
son pequeños, y con números pequeños casi todo parece significativo y casi nada lo es.** **Tres
accidentes frente a uno el año pasado es un aumento del doscientos por ciento y puede no ser nada.**
**Saber decir eso —y saber decir lo contrario cuando toca— es la utilidad real de este punto del
programa.**

## 10. Lo que este tema no da, y dónde está

| Materia | Dónde está | Estado |
|---|---|---|
| **Las ecuaciones de los límites superior e inferior del método de líneas límite** | Ecuaciones 7 a 10 de la **NTP** 1211 | **Guardada entera; sus fórmulas son imágenes y la extracción de texto las devuelve ilegibles** |
| **Las expresiones matemáticas de los cuatro índices** | **Ecuaciones 1 a 6 de la misma NTP** | **Lo mismo**: este tema da lo que cada índice relaciona y su constante, en palabras de la NTP |
| **El caso práctico resuelto y los diagramas** | **Tablas y figuras de la misma NTP, y la herramienta informática del Instituto que ella nombra** | **No reproducidos** |
| **Las fórmulas de media, varianza, desviación típica y coeficiente de variación** | **Cualquier manual de estadística** | **No consultado**: este tema las define en palabras y no las escribe |
| **Tablas de distribución, valores críticos y pruebas de contraste concretas** | **Manuales de estadística** | **No consultados** |
| **Los tipos de muestreo probabilístico** —aleatorio simple, estratificado, por conglomerados, sistemático— | **Manuales de estadística** | **No consultados**: este tema define qué es un muestreo aleatorio y no enumera sus variantes |

## 11. Trazabilidad

| Regla del método | Fuente | Qué se ha citado |
|---|---|---|
| **Documento técnico oficial** | NTP 1211, **«Estadísticas de accidentabilidad en la empresa»**, del INSST, **2024** | **La enumeración de los cuatro índices**, **lo que relaciona y qué representa cada uno de los cuatro**, **la comparación entre incidencia y frecuencia**, **la definición de accidente mortal y su recalificación**, **la definición de los días de duración de las bajas**, **las dos listas de qué es y qué no es hora de trabajo efectiva**, **los dos diagramas del método de control**, **en qué consiste el método de líneas límite y qué permite detectar**, **de dónde sale el índice de frecuencia esperado** y **los tres casos según el número de horas**, citados literalmente |

**Nueve declaraciones expresas:**

1. **Los epígrafes 1, 2 en su primera mitad, 3, 4 y 7 van ENTEROS como oficio.** **Son definiciones de
   estadística general y no afirmaciones sobre el mundo**: **no se atribuyen a ningún autor, no se
   citan de ninguna fuente y no contienen ninguna cifra.** **Este proyecto no ha consultado ningún
   manual de estadística**, y **por eso este tema define en palabras y no escribe ninguna fórmula
   matemática propia.**
2. La NTP 1211 **es de 2024 y por tanto POSTERIOR a la fecha de corte de este proyecto.** **No es
   legislación y no hay redacción que congelar**, y es el mismo criterio con que este proyecto usó
   material de 2025 en el tema compartido de prevención y la NTP 1191 en el tema 10.
3. La NTP 1211 **declara que sustituye a la NTP 1, a la NTP 2 y a la NTP 236** en lo relativo a los
   índices y a los métodos de control estadístico. **Ninguna de esas tres se ha consultado.**
4. **Este tema NO transcribe ninguna de las diez ecuaciones de la NTP.** **Están publicadas como
   imágenes de fórmula y la extracción automática de texto las devuelve ilegibles**, de modo que
   **copiarlas sería transcribir lo que no se ha podido leer con seguridad.** **Lo que se da de cada
   índice es lo que la NTP dice en prosa: qué relaciona y por cuánto se multiplica.**
5. **Este tema cierra la laguna que el tema 1 dejó abierta.** **Allí se dijo que no se daban las
   constantes de los índices por no haber consultado la fuente.** **Aquí se citan las cuatro de la NTP
   oficial**, y **conviene advertir que la ficha técnica del indicador del Sistema Nacional de Salud
   citada en el tema 12 y esta NTP coinciden en las escalas de incidencia y frecuencia.**
6. **La afirmación de que los accidentes de trabajo siguen la distribución de Poisson es de la NTP y
   así se cita.** **Este tema no la demuestra ni la discute**, y **no desarrolla ninguna de las dos
   distribuciones.**
7. **El intervalo de confianza del 90 % del método de líneas límite y el comportamiento de su término
   adicional se resumen y no se citan.**
8. **Los ejemplos numéricos de los epígrafes 3, 4 y 9 —los días de baja de una plantilla de cincuenta,
   las dos plantillas con la misma media de edad, los tres accidentes frente a uno— son inventados por
   este temario para explicar un concepto**, y **no son datos de ninguna fuente.** **Se dicen como lo
   que son.**
9. **Las materias que este tema roza y que se desarrollan en otro punto van remitidas**: **los
   indicadores de salud laboral, al tema 1**; **la definición y la notificación del accidente de
   trabajo, al tema 6**; **los valores teóricos y los percentiles, al tema 8**; **las fichas técnicas
   de los indicadores del Sistema Nacional de Salud, al tema 12**; y **la incidencia y la prevalencia,
   los sesgos, la validez y los tipos de estudio, al tema 14.**

**El resto del tema va como oficio y así se declara**: los dos cortes de las variables con sus ejemplos
de la consulta de empresa y la advertencia de que agrupar una variable continua pierde información; la
tabla de qué gráfico corresponde a cada variable y la explicación de por qué las barras van separadas y
el histograma pegado; las tres lecturas de la diferencia entre el diagrama mensual y el anual acumulado;
la tabla de medidas de posición con el ejemplo de los días de baja y la regla de que media y mediana
responden a preguntas distintas; la tabla de medidas de dispersión con las tres razones que la
acompañan; las dos observaciones sobre las listas de horas efectivas y la coherencia entre numerador y
denominador; el vocabulario de la inferencia y la distinción entre parámetro y estadístico; la
advertencia sobre lo que significa el nivel de confianza; los cuatro pasos del contraste y sus tres
advertencias; la tabla de errores de muestreo con la regla de que aumentar la muestra sólo corrige el
error aleatorio; las tres lecturas de los tres casos del método de líneas límite; las cinco tareas de la
consulta; y la advertencia final sobre los números pequeños. **Nada de eso está en la fuente citada con
esas palabras**, y el tema no lo presenta como si lo estuviera.
