# Temarios de oposición · RTVE

Convocatoria de personal laboral fijo de la Corporación de Radio y Televisión
Española. Es la primera oposición del proyecto y la única terminada. La sección
de la web que sale de aquí es **`www.opotemarios.es/RTVE`**.

El método y las herramientas son los del repositorio, compartidos con las demás
oposiciones y explicados en el `README.md` de la raíz. Lo de esta carpeta son
**sus datos**: su convocatoria, sus temas y su catálogo de volúmenes.

> Nada se escribe de memoria. Cada dato se lee en la fuente oficial antes de
> afirmarlo, y lo que no se puede confirmar se quita.

## Qué hay aquí

| Ruta | Qué es |
|---|---|
| `OPOSICION.md` | La ficha de la oposición. Es también la marca por la que las herramientas saben que ésta es la raíz de trabajo. |
| `ESTADO.md` | Qué hay hecho, qué falta, dónde vive cada cosa. |
| `PENDIENTES.md` | Cuaderno de hallazgos, se anote o no se corrija en el momento. |
| `PLAN.md` | El orden de trabajo y por qué es ése. |
| `bloques.py` | El catálogo de volúmenes: fecha de corte, bloques, temas y avisos. Es lo que `herramientas/libro.py` carga para armar el volumen. |
| `portadas.tsv` | La ficha de cabecera de cada tema: norma, identificador, redacción. |
| `convocatoria/` | Programa oficial literal, bases y exámenes de convocatorias anteriores. |
| `temas/` | Un fichero por tema. |
| `esquemas/` | Un esqueleto de repaso por tema. Estilo telegrama, con el artículo delante de cada línea. |
| `fuentes/` | Lo volcado del BOE y de las demás fuentes citables. |
| `banco/` | Preguntas reales de convocatorias anteriores con su respuesta oficial. |
| `informes/` | Un fichero por agente y fase. Nada se queda solo en el chat. |
| `libro-*.{html,pdf,docx}` | Los volúmenes armados. |

## Cómo se trabaja

Estando dentro de esta carpeta, las herramientas resuelven solas dónde están los
datos:

```
cd rtve

# portada e índice de todos los temas, regenerables
python3 ../herramientas/indice.py                          # todos
python3 ../herramientas/indice.py temas/general/07-*.md    # uno

# volúmenes imprimibles, uno por bloque
python3 ../herramientas/libro.py general     && python3 ../herramientas/pdf.py libro-general.html
python3 ../herramientas/libro.py informacion && python3 ../herramientas/pdf.py libro-informacion.html
python3 ../herramientas/word.py informacion                # el mismo, en .docx

# bancos de preguntas
python3 ../herramientas/banco.py                           # bloque común
python3 ../herramientas/banco_especifico.py informacion    # uno por ocupación tipo
```

Desde la raíz del repositorio, lo mismo nombrando la oposición:
`OPO=rtve python3 herramientas/libro.py general`.

## La fecha de corte

Las bases congelan el temario a **21 de diciembre de 2022**. El cuerpo de cada
tema se escribe con la redacción de ese día; lo que cambió después va en una nota
de actualización al final del epígrafe, marcada y fuera del cuerpo examinable.
Está escrita en `bloques.py`, que es de donde la toman los volúmenes.

## Los volúmenes

**Veintiuno, uno por bloque**, cada uno en PDF, Word y HTML. El general sirve a
las veinte ocupaciones; los veinte específicos cierran con **el mismo tema de
prevención de riesgos laborales**, que es un solo fichero.

| Volumen | Ocupación tipo | Temas | Preguntas | Páginas |
|---|---|---:|---:|---:|
| `libro-general` | Las veinte | 8 | 505 | 259 |
| `libro-produccion-asistencia` | Producción (Asistencia) | 18 | 171 | 281 |
| `libro-produccion` | Producción | 17 | 114 | 235 |
| `libro-realizacion` | Realización (Asistencia) | 21 | 254 | 304 |
| `libro-realizacion-tv` | **Realización Televisión** | **23** | **277** | **365** |
| `libro-documentacion` | Documentación | 7 | 130 | 155 |
| `libro-informacion` | Información y Contenidos | 11 | 226 | 217 |
| `libro-gestion-administrativa` | Gestión Administrativa | 13 | 123 | 182 |
| `libro-gestion` | Gestión | 31 | 129 | 323 |
| `libro-montaje-equipos` | Montaje de Equipos Audiovisuales | 11 | 123 | 166 |
| `libro-edicion-montaje` | Edición, Montaje y Procesos Audiovisuales | 11 | 134 | 195 |
| `libro-informacion-grafica` | Información Gráfica y Captación de Imagen y Sonido | 12 | 142 | 219 |
| `libro-sonido` | **Sonido** | 18 | 134 | 207 |
| `libro-tese` | **Técnica de Equipos y Sistemas Electrónicos** | 18 | 162 | 231 |
| `libro-tecnica-informatica` | **Técnica Informática** | 24 | 138 | 256 |
| `libro-diseno-grafico` | **Diseño Gráfico** | 14 | 134 | 188 |
| `libro-ing-tec-teleco` | **Ing. Técnica Telecomunicación** | 20 | 133 | 261 |
| `libro-ing-tec-industrial` | **Ing. Técnica Industrial** | 17 | 48 | 266 |
| `libro-imagen-personal` | **Imagen Personal** | 10 | 132 | 161 |
| `libro-teitse` | **Téc. Equipos, Instalaciones y Sistemas Eléctricos** | 16 | 48 | 237 |
| `libro-ambientacion-vestuario` | **Ambientación Vestuario** | 8 | 48 | 135 |
| `libro-ing-sup-teleco` | **Ing. Superior Telecomunicación** | **27** | 134 | **337** |
| `libro-profesor-orquesta` | **Profesor de Orquesta** | 11 | 134 | 144 |

**Realización Televisión es el volumen más grande del proyecto**: 365 páginas,
veintidós temas propios más el de prevención y **229 preguntas del bloque
específico**, de dos llamamientos con sus dos plantillas completas.

**Y Técnica de Equipos y Sistemas Electrónicos es el más gráfico**: **treinta de
sus 114 preguntas dependen de una imagen**, la proporción más alta del proyecto.
El temario **no describe lo que no ha visto**: declara cada una y aporta la regla
de su familia.

**Y Ingeniería Técnica · Industrial es el primer volumen del proyecto SIN EXAMEN
que estudiar**: la convocatoria anterior no publicó cuadernillo de esa
especialidad. Sus **48 preguntas son las del tema compartido de prevención**, y
no hay ni una del bloque específico. Lo que ocupa su lugar es **el Boletín
Oficial del Estado**: **veintitrés normas volcadas** y **veintinueve citas
literales verificadas** contra el texto de su artículo. Es **la ocupación más
normativa del proyecto** —trece de sus dieciséis puntos nombran uno o varios
reales decretos— y **la que mejor tolera no tener examen**, porque lo que puede
caer está escrito con todas sus letras. El dato va dicho en su portada y en su
apéndice de respuestas, no disimulado.

**Y Técnica de Equipos, Instalaciones y Sistemas Eléctricos es el segundo sin
examen**, y **el contrario de Industrial en otra cosa**: donde aquélla tenía
veintitrés normas para trece puntos, **ésta tiene una sola para catorce**. Toda
la ocupación gira sobre el **Reglamento electrotécnico para baja tensión y sus
cincuenta y dos instrucciones técnicas complementarias**, con el **Real Decreto
614/2001** de riesgo eléctrico detrás de un punto más. **Sus puntos 15 y 16 van
en un solo tema porque nombran el mismo real decreto**, uno por su articulado y
otro por sus instrucciones, y **la unión va declarada en cuatro sitios**.

**Y este bloque obligó a escribir una lente nueva.** La de exactitud ancla sus
comprobaciones en marcadores del tipo «Artículo N», y **una instrucción técnica
numera por apartados**: sobre doce de los quince temas habría devuelto **un cero
vacío**, que es justo lo que el método prohíbe. `refutar_citas` comprueba cada
tramo en negrita de un bloque de cita **como subcadena literal del volcado**:
**28 tramos, 0 no literales**.

**Y Imagen Personal es el contrario exacto de Ingeniería Técnica · Industrial**:
**su anexo específico no nombra ni una sola norma**. Nueve enunciados de una
línea, sin un real decreto detrás, y **los nueve temas van enteros como oficio
declarado**. Eso deja **media herramienta de refutación sin objeto** —sin norma
no hay cita literal que comprobar—, y el proyecto lo dice en vez de publicar el
cero de la lente: en su lugar comprueba **cobertura pregunta a pregunta**,
**contraste opción a opción contra la plantilla** y **declaración de
procedencia** de todo dato que sólo conste en ella.

**Y Ambientación Vestuario es el caso extremo del proyecto**: **no tiene examen
Y su anexo no nombra ninguna norma**. Las dos comprobaciones fuertes del método
faltan a la vez, y **tres de las cinco lentes se quedan sin objeto**. Lo que
ocupa su lugar son **cuatro comprobaciones nombradas**: cobertura punto por punto,
**alcance declarado** —los siete temas dicen qué NO dan y por qué—, **ausencia de
nombre propio** —ni una marca, ni un diseñador, ni una casa de moda— y **ausencia
de cifra sin fuente**: **cero valores numéricos en siete temas**, porque sin norma
que citar cualquier cifra sería una invención.

**Y Técnica Informática es el contrario exacto**: **ninguna de sus 90 preguntas
del específico depende de una imagen**, y es **el único volumen del proyecto que
contesta el examen entero sin remitir ni una vez a la plantilla**. Todo lo que se
pregunta está escrito, y por tanto todo se puede comprobar.

**Ingeniería Técnica · Telecomunicación es el segundo volumen sin una sola
imagen** —ninguna de sus 85 preguntas del específico depende de una figura— y **el
de reparto más desigual del proyecto**: dos de sus veintitrés puntos del anexo se
llevan el 42 % del examen y **diez no se llevan ninguna pregunta**. Cuatro de esos
diez son el corazón del oficio —estudios, continuidades, salas técnicas e
ingeniería de implantación—, y **sus temas se escriben igual, contra el
programa**.

**Y Ingeniería Superior · Telecomunicación es el primer volumen del proyecto que
COMPARTE temas con otro que no es el de prevención**: **siete de sus veintisiete
son, palabra por palabra, siete puntos del anexo de Ingeniería Técnica ·
Telecomunicación**, así que el tema se escribe una sola vez y sirve a las dos
ocupaciones. **La comprobación se hizo carácter a carácter sobre los dos ficheros
de bases**, y dio un hallazgo: en uno de los siete **sólo cambia un signo de
puntuación**, y el temario lo dice así en lugar de afirmar una identidad exacta
que no lo es.

**Y obligó a añadir una comprobación al método que ninguna lente detecta**:
cuando un tema pasa a servir a dos ocupaciones, **hay que reescribir su CABECERA,
no sólo revisar su cuerpo**. Un cuerpo correcto con una cabecera vieja publica una
afirmación falsa en los dos volúmenes a la vez. Se revisan cinco sitios: la ficha
del tema, su primer párrafo, su fila de `portadas.tsv`, la cabecera de su esquema
y la identidad literal del enunciado en los dos anexos.

**Es además el único cuadernillo del proyecto sin ni una pregunta de prevención
de riesgos laborales**, y **el único cuya plantilla se ha extraído por
coordenadas**: su PDF de preguntas trae la fuente incrustada sin tabla de
caracteres, pero el de respuestas no, y sus **96 respuestas salen enteras, sin
huecos, sin duplicados y sin una sola anotación**.

**Y Profesor de Orquesta es el caso más extremo del proyecto en otra
dirección**: **es el único volumen cuyo anexo no nombra ninguna norma Y cuya
materia es historia de la música**. Las dos cosas juntas dejan al temario sin la
fuente que sostiene a todos los demás, y **la consecuencia va dicha sin adornos
en su primer tema**: una fecha de nacimiento o una atribución de obra escritas de
memoria serían exactamente lo que este método prohíbe. **El volumen se apoya en
tres cosas y sólo en tres**: lo que el propio anexo nombra, las **86 respuestas
que la plantilla oficial confirma**, y lo que se sigue de una definición. **Sus
cinco huecos van señalados uno a uno, con lo que hay que buscar en un manual para
rellenarlos.** Un hueco señalado es una tarea; un hueco relleno de invención es
una trampa.

**Es además el primer volumen cuyo programa ha habido que DESCARGAR para
escribirlo**, y de una fuente que publica **seis versiones del mismo Anexo 2**,
una por especialidad instrumental. **Se han comparado las seis y son idénticas
palabra por palabra.** Pero **las cuatro plazas de la 1/2025 son de otras cuatro
especialidades**, así que **que el temario sea también el suyo es una inferencia
razonable y no un dato**, y así va dicho en tres sitios. Seis programas idénticos
hacen esperar un séptimo igual; no lo prueban.

**Y trae una advertencia que ningún otro volumen ha necesitado**: **tres de sus
respuestas CADUCAN** —quién es el director titular de la orquesta, quiénes los
honorarios «recientes», qué titularidad tenía antes otro director—. Van con la
fecha del examen al lado y con la recomendación de comprobarlas antes de la
prueba. **Una fecha de corte congela el texto de una norma, pero no congela quién
ocupa un cargo.**

**Diez respuestas oficiales de 2024 están mal, y van marcadas una a una** con el
precepto, el modelo de cuentas o la ficha de fabricante que las desmiente. El
temario enseña la norma, no la plantilla, **y dice dónde está la costura**.
