# Refutación · Ingeniería Técnica · Telecomunicación, los diecinueve temas del específico

**Siglas de este informe**: la interfaz digital serie (**SDI**); la Sociedad de Ingenieros de Cine y
Televisión (**SMPTE**) y la Sociedad de Ingeniería de Audio (**AES**); la interfaz digital de audio
multicanal (**MADI**); la Unión Europea de Radiodifusión (**EBU**); la Organización Internacional de
Normalización (**ISO**) y la Comisión Electrotécnica Internacional (**IEC**); la biblioteca de
infraestructura de tecnologías de la información (**ITIL**); el protocolo de internet (**IP**); y la
prevención de riesgos laborales (**PRL**).

**Las cuatro lentes del proyecto pasadas sobre los diecinueve temas del específico de Ingeniería
Técnica · Telecomunicación**, y lo que sale de la comprobación contra las fuentes.

## Lo que dicen las lentes

| Lente | Qué mira | Resultado |
|---|---|---|
| `refutar_exactitud` | Cada negrita dentro de un bloque anclado en un artículo, contra el texto de ese artículo | **Aplicable en un solo tema, el 19.** **4 negritas comprobadas, 0 no literales** —una por cita, que es como la lente cuenta cuando la negrita abarca la cita entera |
| `refutar_modo` | Que el tema no imponga donde la norma faculta, y que recoja las salvedades | **Cero hallazgos** en los diecinueve temas |
| `refutar_prosa` | Relleno, frases repetidas y siglas sin presentar | **Cero hallazgos** en los diecinueve temas y en sus diecinueve esquemas |
| `refutar_documento` | Cada negrita contra el documento no articulado | **No aplicable**, y se explica más abajo |

**Dieciocho de los diecinueve temas no se apoyan en una norma articulada volcada**, así que la lente
de exactitud **devolvería «0 comprobadas, 0 no literales» en los dieciocho**, y **ese cero no dice
nada sobre el tema**. Es el aviso del apartado 10 del manual.

## El único tema con norma articulada citada

```
refutar_exactitud.py temas/ing-tec-teleco/19-proteccion-de-datos-personales.md \
    <Ley Orgánica 3/2018 y Reglamento (UE) 2016/679, volcados al corte>
negritas comprobadas: 4 ; no literales: 0
```

**Lo citado son cuatro preceptos**, y **los cuatro se han elegido por lo que un ingeniero de
instalaciones necesita, no por lo que un opositor de gestión estudiaría:**

| Precepto | Por qué está |
|---|---|
| **Artículo 32.1 del reglamento europeo** | **Es el artículo que convierte la protección de datos en requisitos de pliego.** Y su letra b) enumera CUATRO propiedades, no tres: añade la **resiliencia**, con la palabra «permanentes» |
| **Artículo 25.2 del reglamento europeo** | **El «por defecto»**: una grabadora que sale de caja guardando un año y accesible a todo el personal incumple ese apartado |
| **Artículo 22, apartados 1 a 3, de la ley orgánica** | **El mes de conservación y las setenta y dos horas**, y la prohibición de captar el interior de un domicilio |
| **Artículo 89, apartados 2 y 3, de la ley orgánica** | **La prohibición absoluta de vestuarios y aseos**, y la asimetría entre imagen y sonido |

**Y el hallazgo de método de ese tema**: **hay dos plazos de setenta y dos horas en esta materia y no
tienen nada que ver.** **Uno es el plazo para poner una grabación a disposición de la autoridad
—artículo 22.3 de la ley— y otro el de notificar una brecha de seguridad —artículo 33.1 del
reglamento—.** **La lente no puede detectar esa confusión: la detecta leer las dos normas.**

## El tema 17 y la cadena de dos normas

**El tema de seguridad en las instalaciones técnicas no cita literalmente en su cuerpo**, y **remite a
las citas verificadas del tema homólogo de Técnica de Equipos y Sistemas Electrónicos**, escrito en
este mismo proyecto. **Su hallazgo de método se recoge aquí porque vale igual:**

**El Real Decreto 614/2001 NO da la cifra de dónde empieza la alta tensión: la remite** a «los
reglamentos electrotécnicos». **La cifra está en el artículo 2.1 del reglamento electrotécnico para
baja tensión: 1.000 voltios en alterna y 1.500 en continua.** **Quien busque el número en la norma de
prevención no lo encontrará**, y **eso es exactamente lo que su definición avisa.**

## Por qué la lente de documento no se aplica aquí

**Ninguna de las fuentes de este bloque es un documento no articulado consultable.** **Dieciocho de
los diecinueve temas van como oficio declarado**, y su materia es de tres clases, todas sin documento
que contrastar:

- **Normas técnicas tras muro de pago** —las de la Sociedad de Ingenieros de Cine y Televisión, las de
  la Sociedad de Ingeniería de Audio, la familia ISO/IEC 27000 y la biblioteca de gestión de
  servicios—, **que no se han consultado** y de las que el temario **sólo afirma lo que es de uso
  universal en el sector.**
- **Normas de organismos de acceso restringido** —las familias de difusión de vídeo digital, las
  recomendaciones de la Unión Internacional de Telecomunicaciones—, **en la misma situación.**
- **Teoría clásica de tratamiento de señales, de radiocomunicación y de redes, y oficio de
  instalación audiovisual sin bibliografía** —el teorema del muestreo, las clases de amplificador,
  el direccionamiento, la arquitectura de un control de realización—, **que el temario escribe como
  tal y declara como tal.**

**Ése es el rasgo de método de esta ocupación**: **su materia es en su mayor parte norma técnica de
pago y oficio de obra**, y **el temario dice en cada tema qué no ha consultado.**

## Lo que sí se ha calculado en vez de citarse

**Tres respuestas oficiales no descansan en ninguna fuente porque se COMPRUEBAN**, y **el cálculo
queda escrito para que cualquiera lo repita:**

| Nº | Tema | Qué se calcula |
|---|---|---|
| **69** | 2 | **La relación señal-ruido de 6, 8, 10 y 12 bits**, con la fórmula de los 6,02 decibelios por bit. Sólo desde 10 se llega a 60 |
| **18** | 11 | **La resta de dos códigos de tiempo a 25 imágenes por segundo**, campo a campo y con el préstamo de la hora |
| **80** | 15 | **Las direcciones utilizables de una máscara de veinticuatro bits**, y de paso las tres opciones falsas, que son las tres filas siguientes de la tabla |

## Ninguna figura

**Ninguna de las ochenta y cinco preguntas del específico depende de una figura.** **Es el único
examen técnico del proyecto del que puede decirse eso.** **No hay, por tanto, nada que declarar en
este apartado**, que en los demás bloques técnicos es el más largo del informe.

## Lo que las lentes encontraron y hubo que arreglar

**Seis hallazgos en este bloque, todos corregidos:**

1. **Tema 3, dos siglas en el título del tema**, antes del párrafo que las presenta. **El tema y su
   fichero se renombraron**: «La señal audiovisual y su sincronización».
2. **Tema 7, lo mismo.** **Pasó a llamarse «Vídeo y audio sobre red»**, sin siglas en el título.
3. **Tema 8, una negrita sin cerrar** en una celda de tabla, que habría salido con asteriscos
   visibles en el libro.
4. **Tema 11, otra negrita sin cerrar**, del mismo tipo.
5. **Tema 12, una celda de tabla incompleta** en la fila de la interfaz óptica de ocho pistas: le
   faltaban el cierre de negrita y la barra final. **La lente de prosa no ve ninguno de estos tres;
   se detectaron al releer.**
6. **Varias siglas sin presentar** —entre ellas la del código corrector de errores de la segunda
   generación terrestre y las letras de las clases de amplificador—, **añadidas al párrafo de siglas
   de su tema.**

**Ninguno de los seis cambia una respuesta**: **son de forma, y así se dice.**

## Las seis respuestas con aviso, y por qué ninguna es errata

| Nº | Qué dice la respuesta oficial | Qué añade el temario |
|---|---|---|
| **9** | **La función del regulador es garantizar la competencia efectiva** | **El organismo por el que pregunta dejó de existir con ese nombre en 2013.** La pregunta se contesta igual: pide la función, y de las cuatro opciones sólo una describe la de un regulador sectorial |
| **41** | **La interfaz digital serie usa codificación sin retorno a cero** | **En rigor es sin retorno a cero INVERTIDO y con aleatorización previa.** De las cuatro opciones, la marcada es la única de esa familia |
| **52** | **Para una batería de más de 90 decibelios, micrófonos dinámicos** | **En una batería real se combinan las dos familias.** Con la condición del enunciado, la marcada es la correcta: lo que decide es la presión sonora |
| **54** | **El protocolo inalámbrico de tercera versión cifra con 192 bits** | **Es la fuerza de la suite EMPRESARIAL**; el modo personal usa 128. De las cuatro cifras, es la única real de la norma |
| **67** | **Las redes roja y azul llevan la señal de forma balanceada, para redundancia** | **Las dos llevan el flujo COMPLETO, a la vez.** «Balanceada» significa igualmente activas, no que cada una lleve la mitad |
| **86** | **Equipo a concentrador: los dos extremos en código normal** | **Hoy casi todos los aparatos se adaptan solos**, pero la pregunta habla de un concentrador y la norma de cableado sigue siendo la que es |

**Ninguna de las seis es una errata de la plantilla.** **En las seis, la opción marcada es la correcta
de las cuatro ofrecidas**, y **lo que el temario hace es decir lo que el enunciado calla.** Es el
apartado 5 del manual: *el que detecta se equivoca* —hasta que se demuestra lo contrario, la respuesta
oficial es la buena y el que la discute tiene la carga de la prueba—.

## La pregunta ajena al anexo

**La 75, por el reóstato.** **No pertenece a ningún punto de este anexo ni al bloque común.** **Que un
reóstato es un resistor variable es electrónica elemental y no admite discusión.** Este temario **la
clasifica con las antenas y los transmisores por proximidad con los instrumentos y los componentes de
radiofrecuencia, y lo declara** en vez de inventarle un encaje. **Es la misma decisión que se tomó con
la pregunta de geometría del bloque de Diseño Gráfico.**

## Conclusión

**Las cuatro lentes devuelven cero hallazgos vivos en los diecinueve temas y en sus diecinueve
esquemas.** **La única cita literal del bloque —cuatro preceptos de dos normas en el tema 19— pasa la
lente de exactitud con 4 negritas comprobadas —sus cuatro citas— y ninguna no literal.** **Las seis respuestas con
precisión, matiz u observación y la pregunta ajena al anexo van declaradas.** **El bloque está
verificado.**
