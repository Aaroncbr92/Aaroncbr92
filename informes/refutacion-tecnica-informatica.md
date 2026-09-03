# Refutación · Técnica Informática, los veintitrés temas del específico

**Siglas de este informe**: el lenguaje de consulta estructurado (**SQL**); el protocolo de
transferencia de hipertexto (**HTTP**) y su versión segura (**HTTPS**), con la capa de conexión segura
(**SSL**); el lenguaje de marcado extensible (**XML**); la Sociedad de Ingenieros de Cine y Televisión
(**SMPTE**) y la Sociedad de Ingeniería de Audio (**AES**); la Organización Internacional de
Normalización (**ISO**); la biblioteca de infraestructura de tecnologías de la información (**ITIL**);
el protocolo mejorado de encaminamiento de pasarela interior (**EIGRP**); el sistema de nombres de
dominio (**DNS**) y el protocolo de transferencia de ficheros (**FTP**); el acceso múltiple por
detección de portadora con detección de colisión (**CSMA/CD**); y el Esquema Nacional de Seguridad
(**ENS**).

**Las cuatro lentes del proyecto pasadas sobre los veintitrés temas del específico de Técnica
Informática**, y lo que sale de la comprobación contra las fuentes.

## Lo que dicen las lentes

| Lente | Qué mira | Resultado |
|---|---|---|
| `refutar_exactitud` | Cada negrita dentro de un bloque anclado en un artículo, contra el texto de ese artículo | **Aplicable en dos temas, el 22 y el 23.** **4 y 2 negritas comprobadas, 0 no literales** |
| `refutar_modo` | Que el tema no imponga donde la norma faculta, y que recoja las salvedades | **Cero hallazgos** en los veintitrés temas |
| `refutar_prosa` | Relleno, frases repetidas y siglas sin presentar | **Cero hallazgos** en los veintitrés temas y en sus veintitrés esquemas |
| `refutar_documento` | Cada negrita contra el documento no articulado | **No aplicable como lente completa**, y se explica más abajo |

**Veintiuno de los veintitrés temas no se apoyan en una norma articulada**, así que la lente de
exactitud **devolvería «0 comprobadas, 0 no literales» en los veintiuno**, y **ese cero no dice nada
sobre el tema**. Es el aviso del apartado 10 del manual, y en este bloque se ha cumplido dos veces:
**la primera pasada del tema 23 devolvió cero porque la lente se invocó sin el fichero de la norma**,
y **la de la primera versión del tema 22 devolvió cero porque sus anclajes iban a mitad de párrafo**,
donde la lente los lee como remisiones y los descarta. **Las dos veces el cero era del método, no del
tema.**

## Los dos temas con norma articulada

```
refutar_exactitud.py temas/tecnica-informatica/22-proteccion-de-datos-personales.md \
    <Ley Orgánica 3/2018 y Reglamento (UE) 2016/679, volcados al corte>
negritas comprobadas: 4 ; no literales: 0

refutar_exactitud.py temas/tecnica-informatica/23-el-esquema-nacional-de-seguridad.md \
    <Real Decreto 311/2022, volcado al corte>
negritas comprobadas: 2 ; no literales: 0
```

**Las citas del anexo I del Real Decreto 311/2022 quedan fuera de ese recuento**, porque **la lente
trocea por «Artículo N» y un anexo no tiene artículos.** **Se han comprobado a mano, carácter a
carácter, contra el volcado consolidado a la fecha de corte**, y coinciden. Lo mismo vale para **la
frase del preámbulo de la Ley Orgánica 3/2018 sobre la edad**, que tampoco vive en un artículo.

**Las ocho citas literales de los dos temas y de sus dos esquemas se han verificado una a una**:

| Cita | Norma | Resultado |
|---|---|---|
| Artículo 5.1.e), el principio de limitación del plazo | Reglamento (UE) 2016/679 | **Literal** |
| Artículo 7.1, «cuando sea mayor de catorce años» | Ley Orgánica 3/2018 | **Literal** |
| Artículo 7.2, el consentimiento del titular de la patria potestad | Ley Orgánica 3/2018 | **Literal** |
| Preámbulo, «se mantiene en catorce años la edad…» | Ley Orgánica 3/2018 | **Literal** |
| Artículo 1.1, la remisión al artículo 156.2 de la Ley 40/2015 | Real Decreto 311/2022 | **Literal** |
| Artículo 1.2, «los principios básicos y requisitos mínimos…» | Real Decreto 311/2022 | **Literal** |
| Artículo 1.2, la enumeración de siete palabras | Real Decreto 311/2022 | **Literal** |
| Anexo I, apartado 2, «se identificarán por sus correspondientes iniciales en mayúsculas» | Real Decreto 311/2022 | **Literal** |

## Por qué la lente de documento no se aplica aquí

**Ninguna de las fuentes de este bloque es un documento no articulado consultable.** Las tres que
podrían serlo están cerradas o son índices:

- **Las normas de la familia ISO 27000 y la biblioteca ITIL están tras un muro de pago** y **no se han
  leído.** El tema 20 va entero como oficio y **así lo declara su trazabilidad.**
- **La norma AES67 está igualmente tras un muro de pago**, y **el tema 19 sólo afirma de ella lo que
  la respuesta oficial afirma.**
- **Del índice público de la familia SMPTE ST 2110 se toman los títulos oficiales de sus partes**,
  citados literalmente. **Nada de su contenido interno**, que tampoco es accesible.

**Ése es el rasgo de método de esta ocupación**: **su materia es de las que la industria publica de
pago**, así que **veintiuno de sus veintitrés temas van como oficio declarado** y **el temario dice
en cada uno qué no ha consultado.**

## Lo que las lentes encontraron y hubo que arreglar

**Cuatro hallazgos reales en este bloque, todos corregidos:**

1. **Tema 22, cero negritas comprobadas.** Los anclajes `**Artículo N**` iban a mitad de párrafo, y
   la lente los descarta ahí porque no distingue una cita de una remisión. **Se movieron a abrir
   párrafo propio**, y la lente pasó a comprobar cuatro.
2. **Tema 23, un aviso de prosa.** El epígrafe de niveles y categorías **abría con una tabla, sin una
   sola línea de prosa delante**, de modo que las dos escalas entraban en mayúsculas sin haberse
   nombrado antes. **Ahora se presentan en minúscula** —bajo, medio y alto; básica, media y alta— y
   se advierte que el anexo I las escribe en mayúsculas.
3. **Tema 3 y su esquema, una sigla sin presentar.** **EIGRP** aparecía en una tabla sin haberse
   presentado nunca. **La lente no lo vio** —el paréntesis de «(v1 y v2)» de la sigla anterior lo
   tapaba—, y **el punto ciego queda anotado** con las tres reglas más estrictas que se probaron y
   por qué ninguna sirve.
4. **Tema 19, una ruta del repositorio dentro del temario.** Su trazabilidad remitía a un fichero del
   proyecto por su nombre. **La lente de índice lo avisó** y **la norma lo prohíbe**: quien estudia no
   tiene el repositorio delante. **Ahora dice lo mismo remitiendo al temario específico de Sonido**,
   donde esa declaración ya se hizo.

## Las tres respuestas con salvedad, y por qué no son erratas

**Ninguna respuesta oficial de este bloque es errónea.** **Tres llevan salvedad o precisión
declarada**, y en las tres **la opción marcada por la plantilla sigue siendo la mejor de las cuatro**,
que es lo que las separa de una errata:

| Nº | Qué falla | Por qué NO es errata |
|---|---|---|
| **5** | El enunciado afirma que en Python no se pueden instanciar clases, y sí se pueden | **Las otras tres opciones son peores**: en Java, C# y C++ también se instancian, y además la clase es obligatoria. **La d) es la única defendible** |
| **71** | Lo que Netscape creó en 1994 fue SSL, no HTTPS | **DNS, FTP y CSMA/CD no aseguran la navegación de ninguna manera.** La b) es la única relacionada con el asunto |
| **88** | La ley dice «mayor de catorce años», no «catorce o más» | **De las cuatro opciones —18, 12, 16 y 14— sólo la de 14 es compatible con el precepto.** El defecto está en el enunciado, no en la plantilla |

**Ninguna es impugnable**, y **las tres van avisadas debajo de su enunciado en el libro**, no en una
nota al pie.

## Lo que queda dicho de este bloque

**Veintitrés temas, noventa preguntas del específico, cero hallazgos vivos en las cuatro lentes.**
**Seis negritas comprobadas contra norma y ninguna no literal.** **Ocho citas verificadas carácter a
carácter.** **Ninguna respuesta descansa en la plantilla y ninguna depende de una figura**: es el
único temario específico del proyecto del que puede decirse las dos cosas a la vez.
