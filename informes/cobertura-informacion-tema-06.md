# Cobertura del tema 6 del específico de Información y Contenidos

**Siglas de este informe**: Corporación de Radio y Televisión Española (**CRTVE**).

**Prueba del apartado 7 del manual**: se contestan las preguntas reales con el tema delante, y donde
el tema no llegue **se amplía el tema, nunca se recorta la pregunta**.

- **Tema**: Manual de Estilo de RTVE.
- **Preguntas de la materia**: **9**. Es **el documento del Anexo 2 más preguntado** de los siete.
- **Contestadas con el tema delante**: **9**.
- **Preguntas verificadas en la fuente**: **9 de 9**.
- **Preguntas apoyadas sólo en la plantilla**: **0**.

**Es el segundo punto del bloque con el cien por cien**, después del código del menor, y el que más
preguntas resuelve por sí solo.

## Lo primero: la fuente que se daba por perdida

`convocatoria/FUENTES.md` anotaba este documento como «**403, no se descarga**», y con eso quedaba
fuera de todo el proyecto. **El 403 no era del servidor de RTVE.**

**El Anexo 2 da la dirección en `http://manualdeestilo.rtve.es/`.** La política de salida de este
entorno **sólo deja pasar `https`**, y devuelve 403 a cualquier petición en claro. **Con `https://`,
la misma dirección responde 200** y sirve el manual entero.

**Regla nueva, ya anotada en `ESTADO.md`: un 403 no dice quién bloquea.** Antes de escribir «no se ha
podido consultar» hay que mirar **el esquema de la dirección** y **quién firma la página de error**.

**Lo que se recuperó**: ocho páginas, una por capítulo, **unas 48.000 palabras**, decodificadas con el
descodificador mixto del proyecto —`rtve.es` sirve la misma página con trozos en UTF-8 y trozos en
cp1252—.

## Dónde estaba cada respuesta

**Las nueve preguntas se reparten entre cuatro capítulos**, y el reparto dice algo del examen:

| Capítulo | Preguntas |
|---|---|
| **1 · CRTVE** | 2 —la referencia informativa y la intimidad de los famosos— |
| **2 · TVE** | 3 —el in situ, los rótulos y los lugares de uso público— |
| **3 · RNE** | 2 —los micrófonos ocultos y retirar la palabra— |
| **4 · Medios Interactivos** | 2 —las características de rtve.es y la participación— |
| **5, 6 y 7** | **0** |

**El examen no ha tocado los tres capítulos finales**, que son **más de la mitad del manual**:
cuestiones sensibles, el lenguaje y los anexos. **El tema los desarrolla con su índice completo**,
porque son la parte más preguntable de todas: el capítulo 6 es gramática pura, que es lo que un test
sabe preguntar.

## Un detalle que conviene tener presente al estudiar

**La misma materia está en el manual dos y tres veces, con redacción distinta.** La grabación oculta
aparece:

- en el **capítulo 1**, como factor que merma la credibilidad —«**el uso inapropiado de la cámara o el
  micrófono oculto**»—;
- en el **capítulo 2**, como regla de televisión —las cámaras y micrófonos «**deben ser claramente
  perceptible**[s]»—;
- y en el **capítulo 3**, como regla de radio, que es **la única de las tres que dice cuándo se puede
  y quién lo decide**.

**El examen preguntó por la del capítulo 3.** Quien haya leído sólo la de televisión contesta que no
se pueden usar bajo ningún concepto, que es la opción a).

## El patrón de las opciones falsas

Leídas las nueve preguntas juntas, **las opciones falsas de este examen se construyen de cuatro
maneras**, y todas exigen haber leído la frase:

1. **Invertir una frase del manual.** La opción que dice que en rtve.es **no** deben incluirse
   sentencias ni leyes es la negación exacta de una regla del capítulo 4, **con su mismo ejemplo**.
2. **Añadir una distinción que el manual no hace**, sobre quién profiere los insultos.
3. **Ofrecer la puerta de atrás**: usar material sobre la vida privada de un famoso obtenido por
   terceros, citando la fuente. **El manual la cierra expresamente.**
4. **Dar por buena la razón que el manual rechaza**: grabar en un centro comercial «por tratarse,
   precisamente, de un lugar de uso público».

**Ninguna es un disparate**, y por eso este punto no se aprueba con criterio profesional general.

## Un tercer caso de enunciado descolocado

**Tres de las nueve preguntas** —la 21 y la 28 del primer cuadernillo y la 17 del segundo— **imprimen
las letras de las opciones separadas de sus textos**: primero «a) b)» o «a) b) c) d)» seguidos, y
después los cuatro textos de corrido.

**No cambia ninguna respuesta** y es el mismo defecto que ya aparece en los temas 1 y 2 de este
temario. **Con éstas van siete enunciados descolocados en el bloque**, lo que empieza a parecer una
característica de la maquetación de estos cuadernillos y no un accidente.

## Lo que este tema añade al proyecto

1. **Una fuente entera recuperada**, con la regla del esquema de la dirección.
2. **El mapa de los ocho capítulos**, que dice dónde buscar cada materia y avisa de que **la misma
   materia aparece varias veces con redacciones distintas**.
3. **La tipología de las opciones falsas**, que es transferible a cualquier examen sobre un documento
   de estilo o un código de conducta.
