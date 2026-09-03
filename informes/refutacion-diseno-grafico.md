# Refutación · Diseño Gráfico, los trece temas del específico

**Siglas de este informe**: el modelo de cian, magenta, amarillo y negro (**CMYK**) y el de rojo,
verde y azul (**RGB**); la ultraalta definición (**UHD**); el alto rango dinámico (**HDR**); la
prevención de riesgos laborales (**PRL**); y el Real Decreto Legislativo (**RDL**) 1/1996.

**Las cuatro lentes del proyecto pasadas sobre los trece temas del específico de Diseño Gráfico**, y
lo que sale de la comprobación contra las fuentes.

## Lo que dicen las lentes

| Lente | Qué mira | Resultado |
|---|---|---|
| `refutar_exactitud` | Cada negrita dentro de un bloque anclado en un artículo, contra el texto de ese artículo | **Aplicable en un solo tema, el 13.** **2 negritas comprobadas, 0 no literales** |
| `refutar_modo` | Que el tema no imponga donde la norma faculta, y que recoja las salvedades | **Cero hallazgos** en los trece temas |
| `refutar_prosa` | Relleno, frases repetidas y siglas sin presentar | **Cero hallazgos** en los trece temas y en sus trece esquemas |
| `refutar_documento` | Cada negrita contra el documento no articulado | **No aplicable**, y se explica más abajo |

**Doce de los trece temas no se apoyan en una norma articulada**, así que la lente de exactitud
**devolvería «0 comprobadas, 0 no literales» en los doce**, y **ese cero no dice nada sobre el
tema**. Es el aviso del apartado 10 del manual.

## El único tema con norma articulada

```
refutar_exactitud.py temas/diseno-grafico/13-legislacion-y-derechos-de-autor.md \
    <Real Decreto Legislativo 1/1996, volcado al corte>
negritas comprobadas: 2 ; no literales: 0
```

**Lo citado es el encabezamiento del artículo 14**, que es donde está la palabra que contesta la
pregunta 61: **«Corresponden al autor los siguientes derechos irrenunciables e inalienables».**

**Y el hallazgo de método del bloque está justo ahí**: **sin ese artículo delante, la pregunta 61
parece tener tres respuestas.** **Las opciones que dicen que el derecho se transmite por causa de
muerte, que se extingue con el tiempo y que se puede vender o ceder son las tres VERDADERAS de los
derechos de EXPLOTACIÓN.** **Lo que la pregunta pide es la característica del derecho moral, que es otro**, y ahí
sólo una de las cuatro encaja. **La lente no puede detectar eso: lo detecta leer la norma.**

## Por qué la lente de documento no se aplica aquí

**Ninguna de las fuentes de este bloque es un documento no articulado consultable.** **Doce de los
trece temas van como oficio declarado**, y su materia es de tres clases, todas sin documento que
contrastar:

- **Teoría clásica del diseño y del lenguaje audiovisual** —las mezclas de color, las familias
  tipográficas, las leyes de la percepción, la escala de planos, los estilos de montaje—, **de
  manual y de dominio común.**
- **Documentación de programas comerciales** —los nueve datos del programa de composición, las
  funciones del vectorial, los formatos de fichero—, **que no se ha consultado** y de la que el
  temario **sólo afirma lo que la respuesta oficial afirma.**
- **Oficio de televisión sin bibliografía** —la continuidad y sus piezas, el grafismo informativo—,
  **que el temario escribe como tal y declara como tal.**

**Ése es el rasgo de método de esta ocupación**: **su materia es en su mayor parte oficio y producto
comercial**, y **el temario dice en cada tema qué no ha consultado.**

## Las cinco figuras, declaradas una a una

**La lente no ve las figuras**: **esto es comprobación a mano, pregunta por pregunta.**

| Nº | Tema | Qué se declara | Qué se aporta en su lugar |
|---|---|---|---|
| **5** | 5 | **No se ha visto la imagen y no se describe** | **La tabla de las seis leyes de la Gestalt con lo que se ve en cada una** |
| **22** | 3 | **No se ha visto la cubierta y no se describe** | **De quién es esa colección y desde cuándo**: cualquier figura de ella tiene la misma respuesta |
| **68** | 12 | **No se ha visto el logotipo y no se describe** | **Cuál de los cuatro nombres firma un logotipo universal** |
| **71** | 10 | **No se ha visto el resultado y no se describe** | **La tabla de las cinco operaciones de buscatrazos y cómo se decide mirando** |
| **87** | 13 | **No se ha visto el signo y no se describe** | **La tabla de signos con lo que indica cada uno** |

**En tres de los cinco casos la regla de la familia deja la respuesta prácticamente resuelta antes de
mirar**: **la 22 y la 68 se contestan sabiendo quién es quién**, y **la 87 se contesta descartando dos
opciones que corresponden a otros signos.**

## Lo que las lentes encontraron y hubo que arreglar

**Cuatro hallazgos en este bloque, todos corregidos:**

1. **Tema 3, dos siglas sin presentar.** El título del cartel de Obama iba en mayúsculas y el nombre
   de un logotipo célebre llevaba unas iniciales. **Se escribieron como título y como nombre de
   ciudad**, que además es mejor prosa.
2. **Tema 5, una sigla sin presentar.** Las parejas de letras que piden ajuste de kerning iban
   escritas como pares de mayúsculas. **Ahora se nombran letra a letra.**
3. **Tema 11, una negrita sin cerrar** en una celda de tabla, que habría salido con asteriscos
   visibles en el libro. **La lente de prosa no la ve; se detectó al releer el diff.**
4. **Tema 13, una sigla sin presentar** en la tabla de signos gráficos. **Se sustituyó por su nombre
   desarrollado.**

**Ninguno de los cuatro cambia una respuesta**: **son de forma, y así se dice.**

## Las tres respuestas con aviso, y por qué ninguna es errata

**Ninguna respuesta oficial de este bloque es errónea.** **Tres llevan aviso**, y **en las tres la
opción marcada sigue siendo la mejor de las cuatro**, que es lo que las separa de una errata:

| Nº | Qué falla | Por qué NO es errata |
|---|---|---|
| **9** | **Llama regla de composición a un elemento** | **Las otras tres opciones SÍ son reglas**, y el espacio en blanco es lo único que no lo es. **Con la lectura de «regla frente a elemento» la marcada es la única defendible** |
| **32** | **Dos opciones son defendibles** | **La marcada DESCRIBE lo que una capa es** y la otra sólo dice para qué sirve. **La plantilla elige la más precisa** |
| **95** | **No es de la materia del anexo** | **La respuesta es correcta y no admite discusión**: el defecto está en que la pregunta esté en este examen, no en la plantilla |

**Ninguna es impugnable**, y **las tres van avisadas debajo de su enunciado en el libro**, no en una
nota al pie.

## Lo que queda dicho de este bloque

**Trece temas, ochenta y seis preguntas del específico, cero hallazgos vivos en las cuatro lentes.**
**Dos negritas comprobadas contra norma y ninguna no literal.** **Cinco figuras declaradas una a una
con la regla de su familia.** **Ninguna respuesta oficial es errónea y ninguna es impugnable.**
