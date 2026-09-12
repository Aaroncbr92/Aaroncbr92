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
| `sanidad-indicadores-de-salud-2020.pdf` / `.txt` | **«Indicadores de salud 2020. Evolución de los indicadores del estado de salud en España y su magnitud en el contexto de la Unión Europea»**, Ministerio de Sanidad | **2020** | Tema 12: seis de las siete rúbricas del enunciado son sus capítulos |
| `sanidad-indicadores-notas-metodologicas.pdf` / `.txt` | **«Indicadores de Salud. Notas metodológicas y fuentes de información»**, del mismo Ministerio | sin fecha impresa | Tema 12: qué es la operación estadística y por qué se ajusta por edad |
| `sanidad-inclasns-fichas-tecnicas.pdf` / `.txt` | **Fichas técnicas de los «Indicadores clave del Sistema Nacional de Salud»**, del mismo Ministerio | sin fecha impresa | Tema 12: las fórmulas de los indicadores, con numerador, denominador y constante |
| `ntp-1211.pdf` / `.txt` | **NTP 1211: Estadísticas de accidentabilidad en la empresa**, del INSST; declara sustituir a las NTP 1, 2 y 236 | **2024** | Tema 13: los cuatro índices de siniestralidad y el método de las líneas límite |
| `insst-tema-22-epidemiologia-laboral.pdf` / `.txt` | **INSST, temas específicos del proceso selectivo de la Escala de Titulados Superiores, parte 1, tema 22: «Epidemiología laboral»** | **versión de enero de 2026** | Tema 14: cubre casi rúbrica por rúbrica la primera mitad del enunciado |
| `ntp-243`, `ntp-288`, `ntp-289`, `ntp-380`, `ntp-431`, `ntp-607` | La serie de **ambiente interior y síndrome del edificio enfermo** del Centro Nacional de Condiciones de Trabajo | 1987, dos sin año legible, 1993, 1994 y 2001 | Tema 11 de Medicina de Empresa: el concepto, el umbral del veinte por ciento y los contaminantes del aire interior |
| `ntp-242`, `ntp-387`, `ntp-602` | **Ergonomía de la oficina y del puesto con pantalla** | 1989, 1995 y 2001 | Tema 14 de Medicina de Empresa: la función de la ergonomía y los tres grupos de factores del análisis en oficinas |
| `ntp-177`, `ntp-295` | **Carga física de trabajo** y **valoración del riesgo dorsolumbar** | 1986 y 1992 | Tema 15 de Medicina de Empresa: trabajo estático y dinámico, y el consumo metabólico |
| `ntp-179`, `ntp-275`, `ntp-318`, `ntp-349`, `ntp-355`, `ntp-502`, `ntp-534`, `ntp-544` | La serie de **carga mental, estrés y trabajo a turnos** | de 1986 a 2000 | Tema 16 de Medicina de Empresa: las definiciones de carga mental, el síndrome general de adaptación y los factores del trabajo nocturno |
| `ntp-322`, `ntp-462` | **Vibraciones mano-brazo** y **estrés térmico** | 1993 y 1997 | Tema 25 de Medicina de Empresa: el síndrome de vibración y los tres índices del ambiente térmico |
| `ntp-1149.pdf` / `.txt` | **NTP 1149: Voz y trabajo: procedimiento preventivo**, del INSST | **2020** | Tema 30 de Medicina de Empresa: la crítica al cuadro por reconocer sólo los nódulos, y las medidas en tres niveles |
| `ntp-246.pdf` / `.txt` | **NTP 246: Intoxicaciones agudas: primeros auxilios** | 1989 | Tema 32 de Medicina de Empresa: las seis reglas de la conducta ante la lesión ocular química |
| `ntp-489.pdf` / `.txt` | **NTP 489: Violencia en el lugar de trabajo** | **1998** | Tema 33 de Medicina de Empresa: los tres tipos de violencia y las medidas del entorno |
| `ntp-507.pdf` / `.txt` | **NTP 507: Acoso sexual en el trabajo** | **1997** | Tema 33: los dos tipos básicos y la clave del clima organizacional |
| `ntp-705.pdf` / `.txt` | **NTP 705: Síndrome de estar quemado por el trabajo (II): consecuencias, evaluación y prevención** | **2005** | Tema 33: los cinco grupos de consecuencias y los tres niveles de intervención |
| `insst-guia-radiaciones-opticas.pdf` / `.txt` | **«Guía técnica para la evaluación y prevención de los riesgos relacionados con las radiaciones ópticas artificiales»**, del INSST | **2015** | Tema 32 de Medicina de Empresa: el reparto de absorción por tejidos del ojo, los dos mecanismos de daño y el trabajador afáquico |
| `irsst-lipoatrofia.pdf` / `.txt` | Protocolo del **Instituto Regional de Seguridad y Salud en el Trabajo** (**IRSST**) de la Comunidad de Madrid **sobre la lipoatrofia semicircular** | sin fecha impresa | Tema 28 de Medicina de Empresa: la definición, las dos hipótesis etiológicas y la notificación como accidente de trabajo |
| `sanidad-fibromialgia.pdf` / `.txt` | **«Fibromialgia»**, Ministerio de Sanidad, Política Social e Igualdad | **2011** | Tema 28: las cifras de prevalencia, los criterios de 1990 y de 2010 y el impacto laboral |
| `sanidad-sqm-consenso.pdf` / `.txt` / `.ocr.txt` | **«Documento de consenso. Sensibilidad Química Múltiple»**, del mismo Ministerio | **30 de noviembre de 2011** | Tema 28: los seis criterios del Consenso Internacional y la definición de caso española |
| `sanidad-procedimiento-sars-cov-2.pdf` / `.txt` | **«Procedimiento de actuación para los servicios de prevención de riesgos laborales frente a la exposición al coronavirus del síndrome respiratorio agudo grave de tipo 2 (**SARS-CoV-2**)»**, del Ministerio de Sanidad | revisión de **6 de junio de 2022** | Tema 22 de Medicina de Empresa: la vigilancia de la salud y el trabajador especialmente sensible |
| `sns-gpc-ansiedad.pdf` / `.txt` | **«Guía de Práctica Clínica para el Manejo de Pacientes con Trastornos de Ansiedad en Atención Primaria»**, Plan Nacional para el Sistema Nacional de Salud (**SNS**), Agencia Laín Entralgo | **2008** | Tema 33 de Medicina de Empresa: la definición, la etiología y las manifestaciones clínicas |
| `sns-gpc-depresion-adulto.pdf` / `.txt` | **«Guía de Práctica Clínica sobre el Manejo de la Depresión en el Adulto»**, Ministerio de Sanidad y Agencia de Evaluación de Tecnologías Sanitarias de Galicia | **2014** | Tema 33: los factores de riesgo, los criterios de gravedad y la repercusión laboral |
| `insst-gana-en-salud-adicciones.pdf` / `.txt` | **«Gana en salud», tema 5, «Adicciones»**, material de campaña de promoción de la salud del INSST | posterior al corte | Tema 17 de Medicina de Empresa: se usa para el encuadre y se declara su fecha |
| `ntp-443`, `ntp-447` | **Factores psicosociales** y **actuación frente a agentes biológicos** | 1997 y 1997 | Fuentes auxiliares del bloque de Medicina de Empresa |

## Lo que este almacén ganó con Medicina de Empresa

**El volumen de Medicina de Empresa multiplicó este almacén.** Su programa nombra por su nombre
documentos que no son legislación en la mayoría de sus treinta y tres puntos, y para escribirlo hubo
que bajar **treinta y dos notas técnicas de prevención y diecisiete documentos del Instituto y del
Ministerio de Sanidad**, además de crear otros dos almacenes: `fuentes/protocolos-vigilancia/`, con
los veintiséis protocolos del Consejo Interterritorial, y `fuentes/ddc/`, con las diez Directrices
para la Decisión Clínica sobre trastornos musculoesqueléticos del miembro superior.

**Cinco hallazgos nuevos de esta tanda**, todos comprobados a ojo sobre la página y declarados en el
tema donde aparecen:

- **`ntp-288` y `ntp-289`** llevan impreso en su pie **«Año: 197/»**: una fecha truncada. Es el dato
  que la propia nota da como referencia para valorar su vigencia.
- **`ntp-705`** escribe «de un modo realmente preventivos» y «propios des mismo»; y **el volcado de
  varias notas de esa serie devuelve el signo de admiración invertido en lugar de la ele final**
  —«relaciona¡», «grupa¡»—, porque el archivo mapea así ese carácter.
- **`ntp-1149`** escribe «Obervatorio», «trabajdores» y «sobe».
- **`ntp-489`** es de 1998 y **cita dos leyes derogadas** en su apartado de legislación: la Ley
  Orgánica 1/1992 y la Ley 23/1992 de Seguridad Privada.
- **`sns-gpc-ansiedad`** lleva impresa en sus propias páginas la advertencia de que **han transcurrido
  más de cinco años desde su publicación y está pendiente de actualización**. Sigue siendo la guía
  vigente del Sistema Nacional de Salud a la fecha de corte, y el tema la usa para el concepto y la
  clasificación, no para el tratamiento.

**Y una trampa de extracción que conviene conocer**: la **página 59 de
`sanidad-sqm-consenso.pdf`** —que contiene los apartados 5 y 6 de las conclusiones, anamnesis y
exploración física— **va en el archivo como imagen y no tiene capa de texto**. Una extracción
automática se salta esos dos apartados enteros y hace creer que el consenso pasa del apartado 4 al 7.
**No es así.** Se han reconocido ópticamente con `tesseract -l spa --psm 6` sobre un render a 400
puntos por pulgada y se han corregido a mano tres errores del reconocedor contra la imagen de la
página. **El reconocimiento va en `sanidad-sqm-consenso.ocr.txt`, aparte del volcado, y lo dice en su
cabecera.**

## Diez avisos

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

**9. Tres de estos documentos son posteriores a la fecha de corte** —la NTP 1191 de 2024, la NTP 1211
de 2024 y el tema 22 de epidemiología, versión de enero de 2026—. **Ninguno es legislación**, y los
temas 10, 13 y 14 lo declaran. Es el mismo criterio que se siguió con el material de trastornos
musculoesqueléticos en `fuentes/prl-especifico/`.

**10. Dos de estos documentos tienen erratas comprobadas a ojo, y sus temas las declaran.** En
«Indicadores de salud 2020», el texto del apartado de accidentes de trabajo dice que el índice de
frecuencia «pasó de 18,6 en 2012 a 2,00 en 2017» y su propia tabla 3.5.1 da 22,0; y dice 32,1 para
industria donde la tabla da 32,2. En el tema 22 de epidemiología, la tabla 2 imprime «b+c» como total
de una columna que contiene b y d. **Las fórmulas de la NTP 1211 y del tema 22 son imágenes cuya
extracción de texto es ilegible**, y por eso ninguno de los dos temas las transcribe.

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

## Serie de primeros auxilios (tema 25 de Enfermería de Empresa)

**11. La colección completa de notas técnicas de primeros auxilios del Instituto son nueve**, y están
todas aquí: `ntp-246` (intoxicaciones agudas), `ntp-458` (organización en la empresa), `ntp-467`
(obstrucción de las vías respiratorias), `ntp-469` (hemorragias y shock), `ntp-524` (quemaduras),
`ntp-546` (fracturas, luxaciones y esguinces), `ntp-568` (contusiones y heridas), `ntp-605`
(evaluación primaria y soporte vital básico) y `ntp-1062` (soporte vital básico en el adulto). Se
añade la guía `insst-socorrismo-laboral` (noviembre de 2014). El listado del que se sacó la serie
completa es el de emergencias y riesgo grave e inminente del portal del Instituto.

**La 1.062 actualiza a la 605 y el propio catálogo del Instituto lo dice.** El tema 25 sigue a la
1.062 y usa la 605 sólo para declarar que está superada: sus ritmos de reanimación y su comprobación
del pulso carotídeo ya no son los vigentes.

**12. La ruta corta no sirve para la NTP 1062**: devuelve HTML. Hay que sacar la dirección larga de su
página, como con la 586. Las de la serie 246, 458, 467 y 524 sí bajan por la ruta corta; las de la
469, 546 y 568 no.

**13. Cinco erratas comprobadas a ojo en esta serie**, todas declaradas en el epígrafe de hallazgos del
tema 25:

- **`ntp-458`** imprime «GASES ESTÉRILES» en la figura que rotula como los mínimos del anexo VI del
  Real Decreto 486/1997, donde la norma dice «gasas estériles».
- **`ntp-458`** se fecha en 1995 y cita el Real Decreto 1627/1997, de 24 de octubre.
- **`ntp-467`** se fecha en 1995, su NIPO es de 1998 y su bibliografía cita un libro de 1998.
- **`ntp-546`** imprime «Año: 0...»: el campo del año no llegó a componerse.
- **`ntp-524`** imprime «ducha durante 2030 minutos» donde el resto del documento escribe
  «20-30 minutos».

**14. `rd-365-2009-desa.pdf` es la publicación original del diario, no un texto consolidado.** El Real
Decreto 365/2009 **no está en la base de legislación consolidada del BOE**: `herramientas/boe.py`
devuelve 404 para el índice y para cualquier precepto. Por eso se ha bajado el PDF del diario y se ha
volcado además, ya troceado por artículos, en `fuentes/corte-20221221/BOE-A-2009-5490.preceptos.md`,
para que las lentes puedan comprobarlo:

```sh
curl -sSL -o rd-365-2009-desa.pdf "https://www.boe.es/boe/dias/2009/04/02/pdfs/BOE-A-2009-5490.pdf"
```

**Al no haber consolidado, la herramienta del proyecto no puede comprobar si la norma se ha modificado
después de 2009**, y el tema que la cita lo declara.

**15. El Código Penal está volcado entero, para una sola cita.** El tema 25 cita el apartado 1 de su
artículo 195 porque la guía del Instituto lo trae como fundamento del deber de auxiliar. Se ha volcado
la norma completa —`BOE-A-1995-25444`— y no sólo el precepto, por la misma razón que las demás: **una
lente que sólo ve el artículo citado no puede desmentir nada de lo que hay alrededor.**
