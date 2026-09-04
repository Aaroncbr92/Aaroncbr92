# Fuentes de salud laboral que no son legislación

Los temarios de **Enfermería de Empresa** y de **Medicina de Empresa** tienen puntos cuyo
enunciado **nombra un documento técnico concreto** en lugar de una norma —y alguno lo nombra sin
decir que lo hace, como el punto 11, cuyas rúbricas «Recomendaciones de Vacunación en Población
Adulta» y «Vacunación en trabajadores sanitarios» son dos publicaciones del Ministerio de Sanidad. Cuando eso ocurre, el
documento se baja entero y se guarda aquí —el PDF y su texto extraído—, para que cualquier
afirmación del tema se pueda comprobar y para que la lente `refutar_documento.py` tenga contra
qué contrastar.

La legislación va donde va siempre: volcada con `herramientas/boe.py` a
`fuentes/corte-20221221/`.

| Fichero | Qué es | Edición | Para qué |
| --- | --- | --- | --- |
| `ntp-218.pdf` / `.txt` | **NTP 218: La espirometría forzada en Medicina del Trabajo**, redactada por Joaquín Pérez Nicolás, Diplomado en Enfermería, del Centro Nacional de Condiciones de Trabajo | **1988** | Tema 8 de Enfermería de Empresa, que el propio enunciado del programa remite a esta NTP |
| `ntp-586.pdf` / `.txt` | **NTP 586: Control biológico: concepto, práctica e interpretación**, redactada por Jordi Obiols Quinto y Xavier Guardino Solá, del Centro Nacional de Condiciones de Trabajo | **2001** | Tema 10 de Enfermería de Empresa: la mitad de «recogida de muestras» del punto |
| `ntp-1191.pdf` / `.txt` | **NTP 1191: Salud cardiovascular: recomendaciones para su gestión en el ámbito laboral**, del INSST | **2024** | Tema 10: por qué un servicio de prevención se ocupa del corazón |
| `sanidad-vacunacion-entorno-laboral.pdf` / `.txt` | **«Entorno laboral»**, capítulo 5 de **«Vacunación en grupos de riesgo de todas las edades y en determinadas situaciones»**, Ponencia de Programa y Registro de Vacunaciones, Ministerio de Sanidad | archivo generado en **septiembre de 2018**; el capítulo no lleva fecha impresa | Tema 11: los siete colectivos laborales de riesgo y qué le toca al servicio de prevención |
| `sanidad-vacunacion-poblacion-adulta.pdf` / `.txt` | **«Vacunación en población adulta»**, de la misma Ponencia | **septiembre de 2018** | Tema 11: la rúbrica «Recomendaciones de Vacunación en Población Adulta» del enunciado |
| `sanidad-vacunacion-trabajadores-sanitarios.pdf` / `.txt` | **«Vacunación en trabajadores sanitarios»**, de la misma Ponencia | **abril de 2017** | Tema 11: la rúbrica del mismo nombre del enunciado |

## Ocho avisos

**1. Las NTP no son obligatorias.** El pie de la propia NTP 218 lo dice: «*Las NTP son guías de
buenas prácticas. Sus indicaciones no son obligatorias salvo que estén recogidas en una
disposición normativa vigente. A efectos de valorar la pertinencia de las recomendaciones
contenidas en una NTP concreta es conveniente tener en cuenta su fecha de edición.*» Se usa como
**fuente citable y estable**, no como derecho.

**2. La NTP 218 es de 1988 y ella misma pide que se tenga en cuenta su fecha.** No se ha
buscado ninguna edición posterior ni ninguna NTP que la actualice, y **el tema 8 lo declara**.

**3. El enunciado del programa pide más de lo que la NTP contiene.** Pide «indicaciones,
contraindicaciones relativas y absolutas» y «mantenimiento del espirómetro», y **ninguna de esas
tres cosas está en la NTP 218**. Se comprobó leyendo el documento entero. El tema 8 lo declara
como laguna, con la tarea que la cierra.

**4. Un cuadro de esta NTP es una imagen y no sale en la extracción de texto.** El cuadro de
**síndromes de alteración ventilatoria** es una figura: la extracción automática sólo devuelve
su leyenda. Se leyó **recortando esa zona de la página 4 del PDF y ampliándola a 300 puntos por
pulgada**, igual que se hizo con el cuadro 3 de la BT.601-7 en `fuentes/normas-tecnicas/`. Las
fórmulas de regresión y el criterio de calidad **sí salen en el texto extraído**, y aun así se
comprobaron a ojo del mismo modo, porque **son cifras** y una cifra mal extraída no se nota
leyendo.

**5. Los tres ejemplos resueltos de la NTP contienen cinco errores.** Se han rehecho a mano las
cinco fórmulas de los tres ejemplos y los porcentajes de sus tres cuadros de resultados. Cuatro son
erratas tipográficas —un signo perdido, una variable sin sustituir, una línea mal rotulada—, y **el
quinto es un valor teórico equivocado**: en el segundo ejemplo, el flujo espiratorio forzado entre el
25 y el 75 por ciento sale 3.82 al aplicar la fórmula y el documento imprime 3.02, aunque **el
porcentaje del propio cuadro está calculado con 3.82**. En ese mismo ejemplo el índice de Tiffeneau
teórico sale 79.87 y el documento imprime 85.00. Ninguno de los cinco cambia la interpretación de
ningún ejemplo. Todo ello está declarado en el epígrafe 9 del tema 8.

**6. La NTP 1191 es posterior a la fecha de corte.** Es de 2024. **No hay nada que congelar**: no es
legislación, y el dato que de ella se cita lo fecha ella misma en 2022, anterior al corte. El tema 10
lo declara. Es el mismo criterio que se siguió con el material de trastornos musculoesqueléticos en
`fuentes/prl-especifico/`.

**7. Hay un documento del Instituto que no se ha podido bajar, y conviene dejarlo dicho.** La
monografía **«Aplicaciones de la electrocardiografía en salud laboral. Guía práctica para el médico
del trabajo»**, de **1994**, sería la fuente propia de la primera mitad del tema 10. El **4 de
septiembre de 2026**, tanto su página en el portal del Instituto como la dirección directa de su
archivo respondieron con un **error de página no encontrada**. Está catalogada y no está servida. El
tema 10 lo declara y no suple el hueco.

**8. Los tres documentos del Ministerio de Sanidad son anteriores a la fecha de corte** —2017 y
2018— **y por eso no hay nada que congelar**: no son legislación. Pero **son recomendaciones, y las
recomendaciones se revisan**. Este proyecto **no ha buscado versiones posteriores**, y el tema 11 lo
declara, con aviso expreso sobre el calendario vacunal. Se bajan del portal del Ministerio con el
mismo agente de navegador que las NTP:

```sh
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
B=https://www.sanidad.gob.es/areas/promocionPrevencion/vacunaciones
curl -sSL -A "$UA" -e "https://www.sanidad.gob.es/" -o sanidad-vacunacion-trabajadores-sanitarios.pdf "$B/vacunas/docs/Vacunacion_sanitarios.pdf"
curl -sSL -A "$UA" -e "https://www.sanidad.gob.es/" -o sanidad-vacunacion-poblacion-adulta.pdf "$B/programasDeVacunacion/docs/Vacunacion_poblacion_adulta.pdf"
curl -sSL -A "$UA" -e "https://www.sanidad.gob.es/" -o sanidad-vacunacion-entorno-laboral.pdf "$B/programasDeVacunacion/riesgo/docs/Entorno_Laboral.pdf"
```

## Cómo se vuelve a bajar

```sh
cd fuentes/salud-laboral
curl -sSL -o ntp-218.pdf "https://www.insst.es/documents/d/portal-insst/ntp_218-pdf"
python3 -c "import pymupdf; d=pymupdf.open('ntp-218.pdf'); open('ntp-218.txt','w',encoding='utf-8').write('\n'.join(p.get_text() for p in d))"
```

La ruta `documents/d/portal-insst/ntp_NNN-pdf` sirve para unas NTP y no para otras: para la 218 sí y
para la 586 no. Cuando devuelve un error, la que sirve es la dirección larga que la propia página de
la NTP lleva dentro, y **hay que pedirla con agente de navegador y con `Referer`**, porque sin ellos
el portal devuelve la página HTML en lugar del PDF y `curl` la guarda con extensión `.pdf` sin
protestar:

```sh
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
curl -sSL -A "$UA" -e "https://www.insst.es/" -o ntp-586.pdf "<dirección larga del PDF>"
```

**Conviene comprobar siempre con `file` que lo bajado es un PDF y no una página de error.**
