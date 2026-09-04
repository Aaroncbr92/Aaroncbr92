# Refutación · Ambientación Vestuario, los siete temas del específico

**Siglas de este informe**: la prevención de riesgos laborales (**PRL**).

**Las cinco lentes del proyecto pasadas sobre los siete temas propios de Ambientación Vestuario**, y
**lo que sale es un caso que el método no había tenido nunca del todo así**: **tres de las cinco no
tienen nada que mirar.**

## Lo que dicen las lentes

| Lente | Qué mira | Resultado |
|---|---|---|
| `refutar_exactitud` | Cada negrita dentro de un bloque anclado en un artículo, contra el texto de ese artículo | **NO APLICABLE**: **el anexo no nombra ninguna norma y no hay ninguna cita** |
| `refutar_citas` | Cada tramo en negrita dentro de un bloque de cita, contra el volcado | **NO APLICABLE**: **por la misma razón** |
| `refutar_documento` | Cada negrita contra un documento no articulado | **NO APLICABLE**: **no hay documento** |
| `refutar_modo` | Que el tema no imponga donde la norma faculta, y que recoja las salvedades | **Cero hallazgos** en los siete temas |
| `refutar_prosa` | Relleno, frases repetidas, siglas sin presentar **y negritas rotas o anidadas** | **Cero hallazgos** en los siete temas y en sus siete esquemas |

**Y hay que decir en voz alta lo que significan esas tres primeras filas**, porque **es exactamente el
peligro del apartado 10 del manual**: **si se ejecutaran, las tres devolverían «0 comprobadas, 0 no
literales»**, y **ese cero no dice que los temas estén bien: dice que la lente no ha mirado nada.**
**Publicar ese cero sin explicarlo sería peor que no pasarlas.**

## Lo que ocupa el lugar de las tres lentes que faltan

**Cuatro comprobaciones, y las cuatro se han hecho:**

| Comprobación | Qué es | Resultado |
|---|---|---|
| **1 · Cobertura punto por punto** | **Que cada punto del anexo tenga su tema y que ningún tema invada el punto de otro** | **8 de 8**, sin uniones ni particiones |
| **2 · ALCANCE DECLARADO** | **Que cada tema diga qué NO da y por qué**, en su trazabilidad | **7 de 7**, y **reunido en el informe de cobertura** |
| **3 · Ausencia de nombre propio** | **Que no haya marcas, modelos, diseñadores, casas de moda ni títulos de película** | **Cero nombres propios** en los siete temas |
| **4 · Ausencia de cifra sin fuente** | **Que no haya ningún valor numérico que no proceda de una fuente leída** | **Cero cifras** de temperatura, gramaje, talla, holgura, humedad, iluminancia, presupuesto o plazo |

**La cuarta es la más estricta de todo el proyecto y conviene decir por qué**: **en un bloque con norma,
una cifra se puede citar.** **Aquí no hay norma, así que la regla se vuelve absoluta**: **cualquier
número que este temario escribiera sería un número inventado.** **Por eso no hay ninguno**, y **donde
el temario necesita un orden de magnitud lo dice con palabras** —«más alta», «la más baja de los
tres», «varias veces»— **y no con un valor.**

## Lo que la lente de modo ha vigilado

**Cero hallazgos al final no significa cero correcciones durante.** **En un bloque sin norma, la lente
de modo cambia de objeto**: **ya no vigila que el tema no imponga donde la norma faculta —no hay
norma—, sino que el tema no presente como REGLA lo que es CRITERIO.**

| Riesgo | Dónde aparecía | Cómo se resuelve |
|---|---|---|
| **Convertir un criterio profesional en una obligación** | **El uso de prenda tradicional ajena**, tema 2; **la seguridad química del envejecido**, tema 5 | **Se dicen como criterio declarado**, y **el tema advierte de que no le atribuye ninguna norma** |
| **Dar por regla lo que depende del encargo** | **Pinzar la espalda de una prenda**, tema 2; **el margen de costura generoso**, tema 3 | **Cada uno va con la condición que lo hace válido**: el plan de cámaras en un caso, la vida futura de la prenda en el otro |
| **Presentar como técnica única lo que son varias** | **Los sistemas de patronaje**, tema 3; **los orígenes de una prenda**, tema 6 | **Van en tabla, con cuándo conviene cada uno y qué hay que vigilar** |

## Lo que la lente de prosa ha corregido por el camino

**Treinta y seis avisos de sigla en los siete temas**, y **ninguno era una sigla.** **Todos eran
castellano corriente escrito en mayúsculas por énfasis** —`CONTAR`, `SUFRIR`, `ROTURA`, `ORILLO`,
`PEINE`, `VARA`, `TELAR`, `FOSO`—, **y varios eran justamente el vocabulario técnico del oficio**, que
en un temario de vestuario aparece a docenas.

**La regla del proyecto se confirma y se estrecha para este tipo de bloque**: **el énfasis se hace con
negrita, no con mayúsculas**, y **un término técnico que se está definiendo va en negrita, nunca en
versales.** **Con eso los treinta y seis desaparecieron sin tocar una idea.**

**Y una nota sobre la lente misma, que este bloque estrenó**: **la comprobación de negritas rotas o
anidadas vive ya dentro de `refutar_prosa.py`**, y **detectó nueve anidamientos en el primer tema de
este bloque**, producidos **exactamente por el mecanismo documentado**: sustituir una palabra en
versales por la misma en negrita dentro de un párrafo que ya iba entero en negrita. **Se repararon
lowercaseando la palabra en vez de anidar la negrita**, que es **la reparación correcta y la que el
método venía pidiendo.**

## El punto 8 y la décima redacción del tema compartido

**El enunciado de prevención de esta ocupación no coincidía con ninguna de las nueve redacciones que el
tema compartido tenía listadas**, y **es la más corta de todas.** **Tres rasgos, los tres
transcritos como están:**

1. **«Manipulación de cargas», sin la palabra «manual».**
2. **«Riesgo de alturas, escaleras de mano»**: **es la única de las veinte ocupaciones que nombra las
   escaleras de mano.** **La materia ya estaba desarrollada** —apartado 6.3 del tema compartido, con
   su norma citada—, **así que lo que faltaba era el mapa, no el contenido.**
3. **No lleva punto final**, y **así se transcribe.**

**El tema compartido queda en diez redacciones para veinte ocupaciones.** **Es la segunda vez en dos
bloques que una ocupación nueva destapa una redacción no listada**, y **eso ya no es casualidad: es la
regla escrita en `PENDIENTES.md`** —**cuando entra una ocupación, del tema compartido se relee la
cabecera, no sólo el cuerpo.**

## Lo que este bloque deja al método

1. **Tres lentes sin objeto es un estado válido, y hay que escribirlo entero.** **No basta con decir
   «no aplicable»**: **hay que decir qué se ha hecho en su lugar**, y **aquí son cuatro comprobaciones
   nombradas y con su resultado.**
2. **Sin norma, la regla de las cifras se vuelve absoluta.** **En un bloque normativo, una cifra sin
   fuente es un descuido; aquí sería una invención.** **Cero cifras en siete temas**, y **el orden de
   magnitud se dice con palabras.**
3. **La comprobación de negritas ya no se puede olvidar.** **Está dentro de la lente de prosa y suma
   al total**, así que **un tema con una negrita anidada no la pasa.** **Este bloque es el primero que
   la ha usado en caliente, y le encontró nueve.**
