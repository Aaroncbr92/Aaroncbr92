# Refutación · Ingeniería Superior · Telecomunicación, los veintisiete temas del específico

**Siglas de este informe**: la interfaz digital serie (**SDI**); el protocolo de internet (**IP**); el
protocolo de tiempo de precisión (**PTP**); la Organización Internacional de Normalización (**ISO**) y
la Comisión Electrotécnica Internacional (**IEC**), que publican juntas la familia **ISO/IEC 27000**;
la biblioteca de infraestructura de tecnologías de la información (**ITIL**); el Esquema Nacional de
Seguridad (**ENS**); la Ley General de Comunicación Audiovisual (**LGCA**); y la prevención de riesgos
laborales (**PRL**).

**Las cinco lentes del proyecto pasadas sobre los diecinueve temas propios de esta ocupación**, y lo
que sale de la comprobación contra las fuentes. **Los siete temas compartidos con Ingeniería Técnica ·
Telecomunicación y el de prevención están refutados en sus propios informes**, y **no se vuelven a
comprobar aquí**: son el mismo fichero.

## Lo que dicen las lentes

| Lente | Qué mira | Resultado |
|---|---|---|
| `refutar_modo` | Que el tema no imponga donde la norma faculta, y que recoja las salvedades | **Cero hallazgos** en los diecinueve temas y en sus diecinueve esquemas |
| `refutar_prosa` | Relleno, frases repetidas, siglas sin presentar y negritas rotas o anidadas | **Cero hallazgos** en los diecinueve temas y en sus diecinueve esquemas |
| `refutar_exactitud` | Cada negrita dentro de un bloque anclado en un artículo, contra el texto de ese artículo | **Aplicable en DOS temas, el 21 y el 25.** **7 y 9 negritas comprobadas, 0 no literales** |
| `refutar_citas` | Cada tramo en negrita de un bloque de cita, contra el volcado entero | **Aplicable en los mismos dos.** **7 y 9 tramos comprobados, 0 no literales** |
| `refutar_documento` | Cada negrita contra el documento no articulado, y las cifras sin fuente | **Aplicable en los mismos dos.** **Cero cifras huérfanas en el tema 21**; **nueve en el 25, todas identificadores de norma**, y se explican abajo |

**Diecisiete de los diecinueve temas no se apoyan en ninguna norma volcada**, así que **tres de las
cinco lentes no tienen objeto en ellos**, y **el cero que devolverían no diría «está bien»: diría «no
he mirado nada».** **Es el aviso del apartado 10 del manual**, y **lo que ocupa su lugar va nombrado y
contado en el epígrafe siguiente.**

## Lo que sustituye a las tres lentes sin objeto

**En un punto sin norma, la comprobación no puede ser de literalidad y tiene que ser de otra cosa.**
**Estas cuatro se han hecho una a una sobre los diecisiete temas:**

| Comprobación | Cómo se ha hecho | Resultado |
|---|---|---|
| **Cobertura punto por punto** | **Cada enunciado del anexo, frase a frase, contra el índice del tema que lo desarrolla** | **Los veintinueve puntos cubiertos**, con la única unión —los 13, 14 y 15— razonada en el informe de cobertura |
| **Alcance declarado** | **Cada tema termina enumerando lo que NO da y por qué** | **Los diecinueve lo hacen**, en su epígrafe de trazabilidad |
| **Ausencia de nombre propio** | **Ningún fabricante, ningún modelo comercial y ningún producto se afirma como respuesta** | **Ninguno**, salvo los que la propia pregunta nombra en su enunciado |
| **Ausencia de cifra sin fuente** | **Cada cifra en negrita rastreada hasta la plantilla oficial, hasta el enunciado de la pregunta o hasta la definición de la que se deriva** | **Todas tienen origen escrito en el tema**, y **lo que no lo tiene no está** |

**La cuarta merece detalle, porque es la que más trabajo cuesta y la que más protege.** **Sin norma que
citar, cualquier número es una invención potencial**, así que **los temas declaran uno a uno de dónde
viene cada cifra que dan:**

| Tema | Cifras que da | De dónde vienen |
|---|---|---|
| **3** | **270 Mbit/s, 1,485 Gbit/s, 2,970 Gbit/s y 11,88 Gbit/s**, con sus intervalos unitarios | **De las opciones de la pregunta 23**, confirmadas por la plantilla |
| **5** | **40, 20 y 33,3 milisegundos** por cuadro | **Del inverso de la cadencia**, y el resultado de cien milisegundos lo confirma la pregunta 16 |
| **6** | **Ocho por ocho píxeles** | **De la pregunta 65**, confirmada por la plantilla |
| **8** | **1920 × 1080, 3840 × 2160, 7680 × 4320**, la escalera de interfaces y **doce bits** | **De los enunciados y de las plantillas de las preguntas 61, 67 y 84** |
| **17** | **19 decibelios sobre milivatio** y la escalera de bandas | **De las preguntas 31 y 33**, confirmadas por la plantilla |
| **18** | **Ocho bits, mil veinticuatro bytes, 32.768 bits** y **el mínimo de tres discos** | **De la definición de las unidades y de las preguntas 20 y 70** |
| **19** | **Los cinco parámetros de los cuatro generadores** | **Del enunciado de la pregunta 73**, literalmente |
| **21** | **44,1, 48 y 96 kilohercios, 24 bits y 64 canales** | **De los enunciados de las preguntas 4 y 64 y de la plantilla** |

**Y los que no dan ninguna cifra lo dicen también**: **los temas 7, 9, 10, 11, 12, 13, 14, 15, 16 y
25 no dan ni un caudal, ni un nivel, ni una tolerancia, ni una capacidad**, y **su epígrafe de
trazabilidad enumera exactamente qué se ha callado y por qué.**

## Los dos temas con norma citada

**El punto 23 del anexo cierra su enunciado con «Regulación básica de la radiodifusión sonora en
España»**, y **el punto 27 tiene una norma que su enunciado no nombra pero que obliga a una
corporación pública.** **Son los dos únicos temas propios de esta ocupación con cita literal.**

```
refutar_citas.py temas/ing-sup-teleco/21-sonido.md \
    fuentes/corte-20221221/BOE-A-2022-11311.md
tramos de cita comprobados: 7 ; no literales: 0

refutar_exactitud.py temas/ing-sup-teleco/21-sonido.md \
    fuentes/corte-20221221/BOE-A-2022-11311.md
negritas comprobadas: 7 ; no literales: 0
```

| Precepto de la Ley 13/2022 | Por qué está |
|---|---|
| **Artículo 76, apartados 3 y 4** | **Es la regla que ordena todo el título**: comunicación previa sin espectro, licencia en concurso con espectro |
| **Artículo 77, apartado 1** | **Quién otorga la licencia**: por encima de una Comunidad Autónoma, el Consejo de Ministros |
| **Artículo 78, apartado 2** | **El límite más redondo de los cuatro de concentración**: cinco licencias en un mismo ámbito |
| **Artículo 80, apartado 4** | **La prohibición terminante del subarriendo** |
| **Artículo 83, apartado 3** | **La franja de la una a las cinco**, que es la limitación horaria más preguntable del título |

```
refutar_citas.py temas/ing-sup-teleco/25-seguridad-en-tecnologias-de-la-informacion.md \
    fuentes/corte-20221221/BOE-A-2022-7191.md
tramos de cita comprobados: 9 ; no literales: 0

refutar_exactitud.py temas/ing-sup-teleco/25-seguridad-en-tecnologias-de-la-informacion.md \
    fuentes/corte-20221221/BOE-A-2022-7191.md
negritas comprobadas: 9 ; no literales: 0
```

| Precepto del Real Decreto 311/2022 | Por qué está |
|---|---|
| **Artículo 1, apartado 2** | **Enumera SIETE propiedades de la información, no tres**: añade acceso, trazabilidad, autenticidad y conservación |
| **Artículo 2, apartados 1 y 3** | **El esquema no se queda dentro de la casa**: alcanza al proveedor que presta servicio al sector público, y de ahí a los pliegos |
| **Artículo 5** | **Los siete principios básicos, todos en un solo artículo**: la lista más preguntable de la norma |
| **Artículo 9** | **Las líneas de defensa han de ser organizativas, FÍSICAS y lógicas**: una instalación con sólo capas lógicas no tiene defensa en profundidad |
| **Artículo 11, apartados 1 y 2** | **La seguridad separada de la explotación**: es una regla de seguridad y no de organigrama |

## Las nueve cifras huérfanas del tema 25, una a una

**La lente de documento marca nueve cifras en negrita que no aparecen en el volcado del Esquema
Nacional de Seguridad.** **Se han mirado las nueve y NINGUNA es un dato**: **las nueve son
identificadores de norma.**

| Cifra | Dónde aparece | Qué es |
|---|---|---|
| **27000** *(cuatro veces)* | **La familia de normas de gestión de la seguridad** | **El número con que el propio enunciado del anexo la nombra** |
| **27001** *(dos veces)* | **La norma certificable**, y **el enunciado del punto 22 de Ingeniería Técnica** | **Igual**: número de norma, transcrito del anexo |
| **27002** | **El catálogo de buenas prácticas** | **Igual** |
| **311** *(dos veces)* | **El Real Decreto 311/2022** | **El identificador de la propia norma citada**, que no está dentro de su articulado |

**Por qué no se quitan**: **una cifra huérfana es un aviso, no un veredicto.** **Lo que el método
prohíbe es afirmar un DATO que no se ha leído en su fuente** —un plazo, un porcentaje, una capacidad—,
y **ninguna de estas nueve lo es.** **Se declaran aquí y se dejan**, porque **quitar el número de una
norma haría el temario ilegible y no ganaría ni un gramo de verdad.**

## Lo que este bloque declara en lugar de afirmar

**Cinco decisiones de método que van escritas en el temario y no escondidas en este informe:**

1. **Las normas técnicas que el anexo nombra —las de interfaz, las de producción sobre red, las de
   audio, la familia de gestión de la seguridad y la biblioteca de gestión de servicios— NO se han
   consultado.** **Son publicaciones de pago de organismos privados y este proyecto no tiene su
   texto.** **De ellas sólo se recoge lo que la plantilla oficial confirma**, y **el temario no les
   atribuye ni una cláusula, ni un requisito, ni una cifra.**
2. **Las cinco preguntas que dependen de una figura van declaradas una a una**, en el apéndice de
   respuestas del volumen y en el informe de cobertura. **El temario no describe lo que no ha visto**:
   **da la regla de la familia y deja la respuesta en la plantilla.**
3. **La pregunta 91 llega con una opción corrompida desde la transcripción óptica.** **Se declara como
   defecto de la transcripción y no del examen**, y **la respuesta oficial no se ve afectada.**
4. **El orden de los criterios del algoritmo de elección del reloj maestro se DERIVA de dos preguntas
   de la plantilla y así se dice**: **la prioridad primera antes que la clase de reloj, y la clase de
   reloj antes que la precisión, la desviación y la prioridad segunda.** **El temario NO afirma el
   orden relativo de los tres últimos**, porque **ninguna pregunta lo desempata**, y **decirlo de
   memoria sería exactamente lo que este método prohíbe.**
5. **El reparto entre el punto 19 y el punto 25 va declarado en la cabecera del tema 17**, porque **los
   dos hablan de antenas**: **aquí los parámetros y la propagación; allí, en el tema compartido, las
   líneas, las guías, los transmisores y la medida de distorsiones.** **No se solapan y no se recorta
   contenido.**

## La comprobación que esta ocupación ha obligado a hacer y no estaba en el método

**Al entrar esta ocupación, siete temas ya escritos pasaron a servir a dos.** **Y el fallo que eso
podía producir no lo detecta ninguna de las cinco lentes**: **un tema con el cuerpo correcto y la
CABECERA vieja publica una afirmación falsa —«sirve para Ingeniería Técnica»— en los dos volúmenes a la
vez.**

**La comprobación añadida, y queda escrita para la próxima ocupación que comparta temas:**

| Qué se revisa | Por qué |
|---|---|
| **La ficha del tema** | **La fila «sirve para» miente en cuanto entra la segunda ocupación** |
| **El primer párrafo tras el enunciado** | **Es donde el tema dice a quién sirve, y un lector lo lee antes que la ficha** |
| **La fila de `portadas.tsv`** | **Es de donde el generador saca la ficha impresa** |
| **La cabecera del esquema** | **El esquema se imprime detrás del tema y repite la afirmación** |
| **El enunciado citado** | **Hay que comprobar que los dos anexos lo dicen igual, carácter a carácter, y decir dónde NO** |

**La última es la que ha dado hallazgo**: **el punto 25 de este anexo y el 18 del de Ingeniería Técnica
tienen las mismas palabras en el mismo orden pero un signo de puntuación distinto.** **El temario dice
«palabra por palabra, con un solo signo de puntuación distinto» en lugar de «idéntico»**, que es lo que
había escrito antes de la comprobación.

## Conclusión

**Las dos lentes con objeto en los diecisiete temas sin norma devuelven cero, y las cinco devuelven
cero en los dos temas con norma.** **Las cuatro comprobaciones que sustituyen a las lentes sin objeto
están hechas, nombradas y contadas.** **Las nueve cifras que la lente de documento marca son
identificadores de norma y se declaran una a una.** **Las cinco preguntas con figura, la que llega con
una opción ilegible y el reparto entre los dos puntos de antenas van declarados en el propio
temario.** **El bloque está refutado al 100 %.**
