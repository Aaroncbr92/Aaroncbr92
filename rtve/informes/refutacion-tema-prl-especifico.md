# Refutación del tema de prevención de riesgos laborales del específico

**Siglas de este informe**: la baja tensión (**BT**); la Comisión Nacional de Seguridad y Salud en
el Trabajo (**CNSST**); **DN** (trozo de palabra que el detector toma por sigla); Organización
Internacional de Normalización (**ISO**); instrucciones técnicas complementarias en general
(**ITC**); sus notas técnicas de prevención (**NTP**); prevención de riesgos laborales (**PRL**);
real decreto (**RD**); trastornos musculoesqueléticos (**TME**).

Es el primer tema del proyecto que **no tiene una norma detrás, sino once fuentes**, y dos de
sus cinco rúbricas **no tienen artículo que citar**. Eso cambia dónde está el riesgo: aquí lo
fácil no es equivocarse de plazo, es **rellenar con lo que suena bien**.

## 0 · Lo que dijo la fuente

**Once fuentes, todas leídas en el original y todas guardadas en disco.** Seis son normas
volcadas a la **fecha de corte, 21 de diciembre de 2022**; cinco son documentación técnica.

| Fuente | Qué aporta |
| --- | --- |
| **Ley 31/1995** | rúbrica 1 entera, y el **artículo 20** para incendios |
| **RD 488/1997** (`BOE-A-1997-8671`) | rúbrica 2. **12 bloques, una sola redacción, nunca modificado** |
| **RD 486/1997** (`BOE-A-1997-8669`) | evacuación y protección contra incendios en el lugar de trabajo |
| **RD 513/2017** (`BOE-A-2017-6606`) | clases de fuego, extintores, BIE |
| **RD 2267/2004** (`BOE-A-2004-21216`) | establecimientos industriales |
| **RD 614/2001** (`BOE-A-2001-11881`) y **RD 842/2002** (`BOE-A-2002-18099`) | riesgo eléctrico |
| **RD 39/1997, art. 34** (`BOE-A-1997-1853`) | las cuatro disciplinas preventivas |
| **RDLeg 8/2015, arts. 156 y 157** (`BOE-A-2015-11724`) | accidente de trabajo y enfermedad profesional |
| **Guía Técnica del INSST sobre pantallas**, junio 2021 | todo lo que el RD 488/1997 no concreta |
| **INSST, TME de la extremidad superior** | rúbrica 3 completa |
| **NTP 536, NTP 1090 y 1091, y el documento de la CNSST** | extintores y riesgos viarios |

**Tres hallazgos de la propia fuente:**

1. **El RD 488/1997 no ha sido modificado nunca.** Los **12 bloques** del texto consolidado
   tienen **una sola redacción**, la de 1997. El texto al corte y el de hoy son el mismo.
2. **La Guía Técnica de pantallas de 2021 abandonó el criterio de horas.** Dice literalmente que
   **«actualmente es muy difícil establecer una frontera sencilla que delimite dicho concepto
   basándose exclusivamente en un determinado número de horas de uso diarias o semanales»**.
   Cualquier material que siga dando **«cuatro horas diarias o veinte semanales»** para definir
   al trabajador usuario de pantallas **reproduce la versión de 1998**. Es un dato que **invalida
   media biblioteca de apuntes** y que solo se ve abriendo la Guía vigente.
3. **La distancia de la pantalla tiene dos números, no uno**: **nunca menos de 300 mm** y
   **entre 400 y 750 mm** para los tamaños habituales de oficina. El examen pregunta por «la
   distancia mínima recomendada» y da por buena **400**. Quien memorice solo uno de los dos
   falla la mitad de las veces.

## 1 · El hallazgo de método: dónde acaba este tema y dónde empieza el 8

**Antes de escribir una línea hubo que separar dos temas que el banco mezcla.** `banco/g8.md`
tiene **91 entradas** clasificadas como «prevención de riesgos», y no son de un tema: son de
dos. **52 preguntas son de la Ley 31/1995** —el tema 8 del general— y **40 de este tema**: son
**92 preguntas en 91 entradas**, porque la de cuántos Delegados de Prevención debería tener RTVE
viene **pegada en la transcripción a una pregunta de este tema**.

No es una comodidad de reparto: el **enunciado del específico**, idéntico en las tres
ocupaciones, nombra **pantallas de visualización, trastornos musculoesqueléticos, incendios y
accidente in itinere o in misión**, y **el del general nombra solo la Ley 31/1995**. Sin esa
separación, el tema 8 habría salido con **40 preguntas sin contestar** que no eran suyas, o este
habría duplicado la ley entera.

## 2 · Los fallos de la lente, otra vez del apartado 10

La lente que corresponde aquí es `refutar_documento.py`, la que contrasta **cada negrita y cada
cifra contra el texto completo de las fuentes**, porque las lentes por artículo no sirven para
una guía técnica ni para una NTP. Tenía **un fallo tipográfico con consecuencias**.

**El guion de corte de los PDF.** Un PDF parte las palabras al final del renglón —«distancias
**vi-\\nsuales**»—, y la lente **sustituía el guion por un espacio**, de modo que la palabra
quedaba rota. Resultado: **una cita copiada literalmente de la Guía Técnica salía marcada como
«no literal»**. Eso no da error; hace algo peor: **enseña a no mirar la lista**, que es
exactamente donde se esconde el hallazgo de verdad.

Y dentro del fallo había otro más fino: la clase de caracteres era **`[‐-―]`**, que es el rango
**U+2010 a U+2015** y **no incluye el guion normal U+002D**, que es justo el que usan los PDF.
El primer arreglo, por eso, **no cambió ni una cifra**: 359 no literales antes y 359 después. Se
detectó porque **una corrección que no mueve el contador es una corrección que no se ha
aplicado**.

Arreglado de verdad —coser la palabra partida **antes** de tratar los demás guiones, y con el
guion normal dentro de la clase—, los falsos «no literales» bajaron de **359 a 333**:
**veintiséis citas correctas** que la lente marcaba por motivos tipográficos.

**Regresión sobre el tema 6**, que es el otro que usa esta lente: **792 negritas comprobadas y
339 no literales, antes y después**. Ninguna de sus citas cruzaba una palabra partida, así que
el arreglo no le afecta y **no destapa nada nuevo allí**.

**Estado final de la lente sobre este tema**, ya con las once fuentes y las tres ampliaciones:
**863 negritas comprobadas, 365 no literales y 6 cifras huérfanas**. Las 365 se han repasado una
a una: son **rótulos del propio tema** («**3.3. Las pausas.**»), **glosas que resumen** lo que la
fuente dice más largo, y **datos de trazabilidad** que no están en el articulado —la fecha de la
Guía Técnica, el nombre de una norma ISO—. **Ninguna es una afirmación sin apoyo**, después de
quitar la del ratón.

## 3 · Hallazgos del tema

**a) Una afirmación sin apoyo en la fuente, quitada.** El tema decía que entre los requisitos de
diseño del anexo del RD 488/1997 estaba que **«el cuerpo del ratón debe adecuarse a la anatomía
de la mano»**. **El anexo no menciona el ratón.** Lo trata la **Guía Técnica**, y lo dice de otro
modo: el diseño de esos dispositivos **«habrá de conjugar tanto la eficacia respecto a la función
para la que han sido creados, como la adaptación al usuario permitiendo un uso fácil y rápido y
evitando a la vez las posibles pérdidas de control, los errores y la realización de esfuerzos
innecesarios»**, con remisión a la **EN ISO 9241-410:2008**. Corregido: ahora el tema da la cita
de la Guía y **advierte de que la formulación del examen es del enunciado, no de la fuente**.
Es el **error 9 del catálogo**, y venía de copiar la opción del examen en vez de la fuente.

**b) Una salvedad omitida.** La lente de modo verbal, pasada contra la Ley 31/1995, marcó el
**artículo 28**: el tema resumía el mismo nivel de protección de temporales y de trabajadores de
empresa de trabajo temporal, pero **se dejaba el reparto de responsabilidades y el «sin
perjuicio de lo dispuesto en el párrafo anterior»**. Añadido: **la usuaria responde de las
condiciones de ejecución y de la información; la empresa de trabajo temporal, de la formación y
la vigilancia de la salud**.

**c) Cuatro lagunas de cobertura, cerradas ampliando el tema.** Salieron de la prueba del
apartado 7 y **se han cerrado con fuente, no recortando la pregunta**:

- **Las cuatro disciplinas preventivas** —**medicina del trabajo, seguridad en el trabajo,
  higiene industrial, y ergonomía y psicosociología aplicada**—, del **artículo 34 del RD
  39/1997**. Sin ellas el tema no contestaba qué es **«seguridad en el trabajo»**, y de paso
  ordenan las cinco rúbricas.
- **El riesgo eléctrico**: **contacto directo e indirecto** del **RD 614/2001**, y los umbrales
  del **RD 842/2002** —**baja tensión hasta 1.000 V en alterna y 1.500 V en continua**—.
- **Las BIE en establecimientos industriales**: la tabla del **anexo III del RD 2267/2004**
  —**riesgo bajo, DN 25 mm, simultaneidad 2, 60 min**—.
- **El interruptor diferencial**, añadido el 2026-08-30 al resolver el cuaderno de pendientes.
  Se había dejado fuera con una objeción propia —«el RD 614/2001 no lo nombra»— que resultó
  equivocada: la **ITC-BT-24 del RD 842/2002** lo coloca **en los dos capítulos**, y su
  apartado **3.5** está **dentro del de contactos directos**, con el umbral de **30 mA**. **La
  plantilla oficial tenía razón y la anotación no.**

## 4 · Cifras

**Ninguna cifra del tema falta de las fuentes.** Las **seis «cifras huérfanas»** que marca la
lente son **los números de las NTP 1090 y 1091**, que los PDF escriben **«1.090» y «1.091»** con
punto de millar. Se comprueban a mano y se declaran.

Comprobadas una a una: los **300** y **400-750 mm** de la Guía, los **40°** de inclinación, los
**30 minutos** de las pausas, la **regla 20-20-20**, el **8 %** y el **0,6 %** del túnel
carpiano, el **60 %** del ganglión, las **dos veces por minuto** y el **50 %** de la ISO
11228-3, los **30 segundos** de ciclo y el **30 %** de capacidad muscular, los **5 mm** de
profundidad de la nota de la NTP 536, los **20 kg** del extintor portátil, los **80-120 cm** y
los **15 m** del RD 513/2017, los **5 m**, **50 m**, **20/30 m** y **300-600 kPa** de las BIE,
la tabla 2.1 entera del RD 2267/2004, y los **1.000/1.500 V** y **50/75 V** del reglamento
electrotécnico.

## 5 · Prosa

Cero relleno y cero frases repetidas entre epígrafes. **Siete siglas** marcadas, todas ruido del
detector: **BC** (agente extintor), **DN** (diámetro nominal), **ISO** y **UNE** (organismos de
normalización), **OCRA** (nombre de un método), **NO** en mayúscula por énfasis y **LGSS**, que
sí se presenta pero con una fórmula que el detector no reconoce.

**Repasado el 2026-09-02, al meter el tema en los tres volúmenes: eran diez, no siete, y una era
de verdad.** Las tres nuevas entraron con la corrección del 30 de agosto —la del interruptor
diferencial— y con ella el epígrafe 4.8, que el informe ya no volvió a mirar. **EN** es ruido de
la misma familia que ISO y UNE: va dentro de la designación de una norma, «EN ISO 9241-410:2008».
**ITC** y **BT** no lo eran: el tema escribía «la ITC-BT-24 de ese mismo reglamento» y
**glosaba su título pero no sus siglas**, de modo que quien no venga de instalaciones eléctricas
no sabe que está leyendo una *instrucción técnica complementaria* del reglamento de *baja
tensión*. Se han desarrollado las dos en su primera aparición, dentro de la frase.

**Repasado otra vez el 2026-09-03, y por el mismo motivo: el tema se había vuelto a tocar.** El
énfasis **«NO»** en mayúscula, que estaba contado como ruido, se sustituyó por ***no*** en cursiva
en todos los temas del proyecto, y con él desapareció ese aviso. **Quedan seis**, todos ruido del
detector y todos declarados aquí: **DN** (diámetro nominal), **EN**, **ISO** y **UNE** (prefijos de
norma y organismos de normalización), **OCRA** (nombre de un método) y **LGSS**, que sí se presenta
pero con una fórmula que el detector no reconoce. **BC** dejó de salir al enseñar a la lente que una
sigla también se presenta **con su desarrollo detrás** —«UGT (Unión General de Trabajadores)»— y no
sólo delante.

**La lección es de método, no de contenido**: una corrección posterior al informe **deja el
informe mintiendo**, y aquí lo dejó dando siete donde había diez. Cuando se toca un tema ya
refutado, hay que volver a pasarle las lentes, aunque el cambio venga de una fuente buena y
parezca cerrado.

**El esquema son 2.937 palabras y 107 líneas de contenido.** En **líneas está por debajo** de la
referencia del apartado 9 del manual —unas 130—; en **palabras, un 47 % por encima** de las
2.000. Y queda **muy por debajo del de la Ley 31/1995**, que se va a 3.966. La diferencia no es
de disciplina: es que aquel tema es **enumeración cerrada de un extremo a otro** y este tiene
más prosa que se puede comprimir.

*(Cifras corregidas el 2026-08-30: este informe daba «2.802 palabras y 166 líneas», medidas con
`wc` en locale C —que cuenta de menos en texto acentuado— y contando líneas vacías.)*

## 6 · Lo que queda fuera, y por qué

De las **40 preguntas del banco que son de este tema**, **cinco no se contestan con el cuerpo
delante y no se han incorporado**. Las razones están en `informes/cobertura-tema-prl-especifico.md`;
en resumen: **tres son de materia de otro tema del específico** —la espuma de efectos
especiales, el incendio del bazar de la caridad de 1897 y la sala de dimmers—, **una es de
actualidad** —el incendio de Campanar— y **una es un cálculo hidráulico** del cuadernillo de
Ingeniero Superior Industrial, ocupación que no preparamos. **Ninguna de las cinco viene de los
cuadernillos de las tres ocupaciones que preparamos.** Una sexta —el interruptor diferencial—
estaba en esa lista con una objeción propia, salió de ella al resolverse el cuaderno de
pendientes, y hoy la contesta el tema.

## Resumen

| | Hallazgos | Estado |
|---|---|---|
| Separación de temas que el banco mezclaba | **91 preguntas eran de dos temas: 51 y 40** | resuelto antes de escribir |
| Lente ciega | **1 fallo doble** (guion de corte de PDF, y la clase que no incluía el guion normal) | corregido; **26 falsos «no literales»** menos |
| Afirmación sin apoyo en la fuente | **1** (el ratón) | corregida con la cita de la Guía |
| Salvedad omitida | **1** (art. 28, reparto usuaria/ETT) | corregida |
| Lagunas de cobertura cerradas ampliando | **4** (disciplinas preventivas, riesgo eléctrico, BIE industriales, interruptor diferencial) | cerradas con fuente |
| Cifras inventadas | **0** | las 6 «huérfanas» son «1.090» y «1.091» con punto de millar |
| Estado final de la lente | **863 comprobadas · 365 no literales** | repasadas una a una |
| Preguntas fuera del tema, declaradas | **5** | ninguna de las tres ocupaciones que preparamos |
