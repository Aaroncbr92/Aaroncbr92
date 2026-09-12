# Directrices para la Decisión Clínica en Enfermedades Profesionales (DDC)

Colección del **Instituto Nacional de Seguridad y Salud en el Trabajo**, elaborada con la
colaboración del **Instituto de Salud Carlos III**. Cada directriz toma **una enfermedad del cuadro
de enfermedades profesionales** —el del Real Decreto 1299/2006— y la recorre entera: definición y
fisiopatología, síntomas y signos, anamnesis, exploración con sus maniobras, pruebas
complementarias, diagnóstico diferencial, vulnerabilidad, condiciones y actividades de riesgo,
agente y código del cuadro, repercusión en incapacidad temporal y permanente, requisitos de
calificación como enfermedad profesional y un algoritmo de decisión.

Aquí está volcada **la serie TME**, de trastornos musculoesqueléticos de origen profesional del
miembro superior, **completa: diez directrices, todas de 2022**.

| Fichero | Enfermedad | Código del cuadro |
| --- | --- | --- |
| `ddc-tme-01.pdf` / `.txt` | Patología tendinosa crónica del manguito rotador | 2D0101 |
| `ddc-tme-02.pdf` / `.txt` | Síndrome por compresión del nervio cubital en el codo | 2F0101 |
| `ddc-tme-03.pdf` / `.txt` | Afectación osteoarticular por vibraciones transmitidas mano-brazo | 2B0201, 2B0202 y 2B0203 |
| `ddc-tme-04.pdf` / `.txt` | Epicondilitis | 2D0201 |
| `ddc-tme-05.pdf` / `.txt` | Epitrocleítis | 2D0201, compartido con la epicondilitis |
| `ddc-tme-06.pdf` / `.txt` | Síndrome del canal de Guyón | 2F0301 |
| `ddc-tme-07.pdf` / `.txt` | Síndrome del túnel carpiano | 2F0201 |
| `ddc-tme-08.pdf` / `.txt` | Parálisis del nervio radial por compresión | 2F0601 |
| `ddc-tme-09.pdf` / `.txt` | Higroma crónico del codo | 2C0601 |
| `ddc-tme-10.pdf` / `.txt` | Tendinitis y tenosinovitis del pulgar | 2D0301 |

**Los códigos de la tercera columna son los que cada directriz imprime de sí misma.** Quien quiera
contrastarlos tiene el cuadro volcado en `fuentes/corte-20221221/BOE-A-2006-22169.md`.

## Tres avisos

**1. No son derecho.** Son directrices clínicas del Instituto: orientan la decisión del médico del
trabajo y **no obligan**. Lo que obliga es el cuadro del Real Decreto 1299/2006 y el régimen de la
Ley 31/1995. Los temas que las citan lo dicen.

**2. Llevan erratas y este proyecto las señala.** La primera directriz escribe **«maguito»** por
«manguito» dos veces —en el epígrafe del cuadro y en el de calificación— y **«movimientos
repetititvos»** por «repetitivos». Y la tercera, que trata de vibraciones, encabeza su tabla del
cuadro con **«AGENTES, SUBAGENTES Y ACTIVIDADES PROFESIONALES CON RIESGOS PARA EL SÍNDROME DEL CANAL
EPITRÓCLEO-OLECRANIANO POR COMPRESIÓN DEL NERVIO CUBITAL EN EL CODO»**, que es el título de la
segunda: un resto de copia y pega entre directrices hermanas. Las cuatro se han comprobado a la
vista sobre la página, entre doscientos sesenta y trescientos puntos por pulgada. **Se citan tal
como están impresas y se advierte.**

**3. Los tiempos de incapacidad temporal que dan no son suyos**: los toman del **Manual de Tiempos
Óptimos de Incapacidad Temporal del Instituto Nacional de la Seguridad Social**, que **no está
volcado en este proyecto**. Quien cite un plazo de estas directrices está citando la directriz, no
el manual.

## Cómo se vuelven a bajar

La página de la colección es
`https://www.insst.es/ddc-directrices-para-la-decision-clinica`, y de ella salen los enlaces a
`https://www.insst.es/documents/94886/4346055/DDC-TME-NN...pdf/...`. El texto se extrae con
`pymupdf`, expandiendo las ligaduras, y se guarda junto al PDF con el mismo nombre.
