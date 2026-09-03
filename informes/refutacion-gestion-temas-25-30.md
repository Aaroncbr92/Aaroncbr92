# Refutación · Gestión, temas 25 a 30

## 1 · Qué se hace cuando no hay norma que citar

**Cinco de estos seis puntos no descansan en ninguna norma.** El método del proyecto se apoya en
contrastar afirmaciones contra una fuente de la jerarquía, y aquí esa fuente no existe. La solución
no es bajar el listón sino cambiar el contraste:

- **Doctrina con autor** —puntos 25 y 26—: cada modelo va atribuido a quien lo formuló, y la
  trazabilidad del tema es una lista de autores en lugar de una lista de artículos. Mintzberg,
  Maslow, Herzberg, McClelland, McGregor, Vroom, Adams, Locke, Lewin, Hersey y Blanchard, Burns y
  Bass, Spencer, Kirkpatrick, Wolpe.
- **Matemática rehecha** —puntos 28 y 29—: cada resultado del examen se recalcula en el tema con los
  pasos escritos. La comprobación no es documental: es que el lector pueda repetirla.
- **Documentación de fabricante** —punto 30—: cuarto nivel de la jerarquía, con las dos advertencias
  que ya quedaron escritas para Gestión Administrativa.

Y una regla que sale de aquí y vale para todo el proyecto: **en un tema sin fuente citable, la
negrita no puede prometer literalidad**. En los puntos 28 y 29 **ninguna cifra calculada va en
negrita**; los números van en texto llano con la operación a la vista.

## 2 · Exactitud

- **Puntos 25, 26, 28 y 29**: sin fuente que citar, no procede la lente de exactitud. La revisión
  fue de atribución —¿esto lo dice quien digo que lo dice?— y de aritmética.
- **Punto 27**: **cero no literales** contra la Ley 13/2022 y el III Convenio, tras reanclar el
  artículo 129 en su propio párrafo; antes sus citas caían dentro del bloque del 128.
- **Punto 30**: **cero no literales** contra las nueve páginas de Microsoft, tras rebajar a cursiva
  sesenta y siete marcas de énfasis propio y corregir dos títulos de página que el tema citaba de
  memoria: la de segmentaciones se titula **«Usar segmentaciones para filtrar datos»**, sin «de
  datos», y la de macros, **«Inicio rápido: Crear una macro»**.

## 3 · Modo verbal y salvedades, y un hallazgo inventado

En el punto 27 la lente de modo reclamó al bloque del **artículo 2** una salvedad que no era suya.
El motivo: **la Ley 13/2022 y el III Convenio numeran los dos un artículo 2**, y son cosas distintas
—definiciones en la ley, ámbito temporal en el convenio—. La lente junta los textos de todas las
fuentes para no comparar contra la norma equivocada, y ese remedio abre el fallo simétrico: **exige
al bloque de una norma la salvedad de la otra**.

**Se corrigió la herramienta**: `refutar_modo.py` avisa ahora de las colisiones de numeración, y
sólo de los números que el tema usa, para que quien lea la lista sepa qué líneas mirar dos veces. La
colisión concreta queda además anotada en el propio tema 27.

## 4 · Prosa, y una lente que confundía funciones con siglas

El punto 30 devolvió **decenas de avisos de «sigla sin presentar»** que no eran siglas: `BUSCARV`,
`SUMAR.SI`, `DESREF`, `#¡DIV/0!`. Un tema de hoja de cálculo los tiene a docenas y todos van en
mayúsculas.

**Se corrigió `refutar_prosa.py`** por dos vías: ignora lo que va **entre acentos graves**, que es
código y no prosa; y reconoce como llamada a función **un nombre en mayúsculas con un paréntesis
pegado**, que es lo que aparece dentro de una cita literal donde no se pueden poner acentos graves
sin tocar la cita. Sin esas dos salvedades, los avisos buenos quedaban enterrados.

**Cero hallazgos de prosa en los seis temas** tras la corrección.

## 5 · Plantilla

**Ninguna errata en las diecisiete preguntas.** Dos merecen nota porque su corrección no es obvia:

- **Pregunta 18, la tecnocracia de Mintzberg.** El enunciado la llama *«tecnocracia»* y la respuesta
  correcta *«también denominada staff»*. **Ninguna de las dos expresiones es de Mintzberg**: él dice
  **tecnoestructura** y reserva *staff* para el **staff de apoyo**, que es otra de las cinco partes
  —tan distinta que la pregunta 33 del mismo examen las enumera por separado—. Lo que sí es exacto
  de la opción es su parte decisiva, **«se compone fuera de la línea de jerarquía de autoridad»**,
  que es la definición del modelo y la que descarta las otras tres. **La respuesta oficial es la
  correcta**, y lo que la pregunta enseña es que **se contesta por la posición, no por el nombre**.
- **Pregunta 12, la varianza.** El enunciado **no dice si los tres rendimientos son población o
  muestra**, y de eso depende el divisor: con *N* salen 2,17 % y 14,72 %; con *N−1*, 3,25 % y
  18,03 %. **Las dos parejas están entre las opciones.** La oficial es la de la cuasivarianza, y es
  la defendible por dos razones: tres rendimientos anuales de una acción son una muestra, y es la
  única de las dos cuyos números están **bien redondeados** —la otra convierte 14,72 en 14, que
  redondearía a 15—. **La plantilla es correcta; el enunciado es mejorable**, y el tema lo dice sin
  convertirlo en una errata que no es.

Y una precisión terminológica que tampoco es errata, en la **pregunta 82**: en sentido estricto el
**descuento comercial** es sólo *N · i · n*, y lo que resulta de sumarle la comisión es el
**descuento bancario**. El enunciado da la comisión entre sus datos, de modo que pregunta por el
total, y de las cuatro opciones la oficial es la única que **suma** la comisión en lugar de
multiplicarla o dividirla. **La respuesta oficial es la correcta.**
