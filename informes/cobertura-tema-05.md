# Prueba de cobertura del tema 5 del general

**Siglas de este informe**: Impuesto sobre la Renta de las Personas Físicas (**IRPF**);
Organización de las Naciones Unidas (**ONU**); Presupuestos Generales del Estado (**PGE**).

> **Actualización del 2026-08-30.** Esta prueba se pasó sobre el banco anterior a la pasada de
> verificación, que le añadió preguntas. Las que entraron después están en
> `informes/cobertura-nuevas-2026-08-30.md`, con sus lagunas y cómo se cerraron. **Las dos
> pruebas juntas cubren el banco entero.**

Las **107 preguntas** que el banco tiene en el bloque del III Convenio Colectivo —el más
grande de todo el banco—, con su respuesta oficial, contra el cuerpo del tema.

| | Preguntas | |
|---|---|---|
| **Se contestaban ya con el tema** | **77** | 72 % |
| **Se contestan tras completar el tema** | **7** | 7 % |
| **No son del convenio** | **23** | 21 % |

De las **84 preguntas que sí son del convenio, el tema las contesta todas** una vez
cerrados los siete huecos que la prueba destapó. Las 23 restantes están en el bloque
porque el cuadernillo las agrupó ahí, no porque se contesten con el convenio.

## Dónde se concentra el examen

Contadas por el precepto del que sale la respuesta, no por el que cita el enunciado:

| Capítulo | Preguntas |
|---|---|
| **VI · Tiempos de trabajo y descanso** | **33** |
| **VIII · Régimen disciplinario** | 10 |
| **VII · Retribuciones** | 10 |
| III · Empleo | 9 |
| Anexo 4 · Orquesta y Coro | 6 |
| V · Clasificación profesional | 5 |
| XII · Situaciones del personal | 4 |
| I, II, X, XI y anexos 1, 3 y 5 | 7 |

Casi **cuatro de cada diez** preguntas del convenio salen del capítulo VI, y dentro de él
se repiten tres datos hasta la saciedad: el **descanso mínimo entre jornadas de 12 horas**
(en cuatro cuadernillos distintos), el **máximo de 10 días trabajados en un periodo de 14**
(en cinco) y las **vacaciones de 25 días laborables** (en tres). Quien solo tenga tiempo
para un capítulo, que sea el VI.

## Los siete huecos que la prueba destapó, y dónde están ahora

| Pregunta del examen | Dato | Precepto |
|---|---|---|
| Permanencia mínima para pedir el primer traslado voluntario | **1 año** (2 el segundo) | art. 14.3 |
| A quién se considera en **comisión de destino** | puestos **no permanentes en organismos oficiales**, temporal, **se sigue en activo** | art. 23 |
| Período de prueba en contratos de **más de 6 meses** | **3 meses** (y **1 mes** en los de 6 o menos y de duración incierta) | art. 32 |
| Cuántos **niveles económicos** tiene el salario base | **18** | art. 65 · **imagen** |
| A qué **ámbito ocupacional** pertenece la ocupación tipo «realización» | **Producción de contenidos audiovisuales y multimedia** | anexo 3 · **imagen** |
| Cuántas personas componen el **Comité de Seguridad y Salud Laboral** | **16** (8 + 8) | art. 92, apdos. 5.5 y 6 |
| Bajo qué supervisión se rige el **Archivo de la Orquesta y Coro** | **Dirección del Fondo Documental de RTVE** | anexo 4, art. 11 |

El del artículo 32 no era un hueco sino un **error**, y está contado en
`informes/refutacion-tema-05.md`.

## Lo que la prueba encontró de fondo: el convenio tiene partes que no son texto

Dos de los siete huecos no se podían cerrar leyendo el convenio, porque **el BOE publica
esas partes como imagen**, no como texto: no están en el HTML y por tanto tampoco en la
transcripción. Y no se nota que faltan, porque el texto continúa con normalidad después
del rótulo. Es el mismo modo de fallo del apartado 10 del manual —un hueco de cobertura no
da error—, esta vez en la fuente y no en las herramientas.

Son **cuatro imágenes y una tabla suelta**, ahora descargadas y transcritas en
`fuentes/convenio/imagenes/`:

- **La tabla de niveles del artículo 65.** Dieciocho niveles económicos en total, seis
  letras (A a F) por tres numerales. Nivel básico **D1** en el Grupo I · Subgrupo I (12
  escalones), **E1** en el Grupo I · Subgrupo II (15) y **F1** en el Grupo II (**18**).
  Techo siempre **A3**. Saltos de **0,5 · 1 · 2 · y después 3 años**.
- **El anexo 3 completo**, con los grupos, los ámbitos ocupacionales, las **ocupaciones
  tipo** y su equivalencia con las categorías del XVII convenio. De aquí salen los trece
  ámbitos del artículo 38.
- **Los anexos 1 y 2** (tablas salariales y tabla de incompatibilidades de complementos),
  también transcritos. No por los importes —son los de 2020 y los PGE los suben cada año—,
  sino por **la estructura**, que es lo que se pregunta y lo que no cambia.

## Una respuesta oficial que parece errata y no lo es

«¿A qué ámbito ocupacional pertenece la ocupación tipo de **realización**?» La plantilla
responde **«Producción contenidos audiovisuales y multimedia»**, y la opción
«**Realización** y edición audiovisual» —que es lo que el nombre sugiere— está entre las
alternativas. Parece un error de la plantilla y no lo es: el anexo 3 distingue
**«Realización»**, del **Grupo I**, ámbito de **producción de contenidos**, de
**«Realización (asistencia)»**, del **Grupo II**, ámbito de **realización y edición
audiovisual**. La plantilla acierta. Sin la imagen del anexo 3 no había forma de saberlo,
y el tema habría dado por buena la respuesta equivocada.

Es la tercera vez que una respuesta oficial se comprueba antes de tratarla como errata, y
la primera en que **la sospecha era nuestra y el error también**. Las dos erratas reales
detectadas siguen anotadas en `PENDIENTES.md`.

## Lo que los anexos 1 y 2 añaden al tema

Ninguna pregunta del banco pide un importe, y por eso el tema no los recoge. Lo que sí
recoge, porque es estructura y no cuantía:

- **El salario base depende solo del nivel económico, no del grupo.** Un C2 cobra lo mismo
  en el Grupo I-I que en el Grupo II.
- **De F1 a A3 hay diecisiete saltos y dieciséis son iguales.** El de **D2 a D1** es más
  pequeño —57,91 € frente a 68,31 €— y cae justo en el **nivel básico del Grupo I ·
  Subgrupo I**. Se comprobó ampliando la imagen porque la primera lectura dio por
  constante toda la escala, y no lo es.
- **Los complementos de puesto van en cuatro tramos** (A-B · C-D del Grupo I-I · C-D del
  resto · E-F), con **una excepción**: unidades informativas paga igual en los tres
  primeros.
- **La opción 1 de disponibilidad no incrementa nada**, y el incremento **no depende del
  grupo**.
- **La residencia no sigue el orden intuitivo**: resto de Canarias, Ceuta y Melilla cobra
  **más** que Las Palmas, Gran Canaria y Tenerife, y **Baleares es el más bajo**.
- **Turnicidad tiene dos tablas, de 35 y de 40 horas semanales**, y **la jornada de fin de
  semana, dos columnas, de 3 y de 2 días**: son la letra b) del artículo 50 y la
  disposición transitoria segunda puestas en cifras. Confirman que las dos siguen vivas.
- **El importe de la jornada de rodaje crece con el riesgo, no con la renta**: el destino
  peor pagado es el propio domicilio y el mejor, un país en conflicto bélico.
- **El anexo 1 sí cifra la compensación por menor preaviso** de los artículos 49 y 50, que
  esos artículos mencionan sin importe.
- **Del anexo 2**, los **tres símbolos** —X, «horas» y D—, que **la casilla vacía significa
  compatible**, que **residencia y vivienda son compatibles con todo**, que **la jornada de
  rodaje es el concepto que más usa la D**, y que **festivos ↔ horas extras es la única
  casilla condicionada de la matriz**, incompatible solo en Orquesta y Coro.

## Dos preguntas que el tema contesta sin que haya un artículo que lo diga

- **«¿Cuántos días de libranza genera un fin de semana completo trabajado?» → dos.** No hay
  precepto con esas palabras: sale de juntar el artículo 46.3 (un día de descanso por cada
  festivo trabajado de lunes a viernes) con el 46.4 (descanso mínimo de **dos días
  consecutivos**). El tema trae las dos piezas.
- **«El Convenio Colectivo vigente data del año…» → 2020.** El acuerdo de modificación es
  de 2022 y la corrección de errores de 2021, pero el convenio es el publicado el **22 de
  diciembre de 2020**. Los enunciados de 2024 que hablan del «III Convenio Colectivo 2022»
  —los hay— se refieren al texto ya modificado, no a un convenio nuevo.

## Las 23 que no son del convenio

- **Doce del Estatuto de los Trabajadores**: movilidad funcional a funciones inferiores,
  contenido mínimo del convenio (art. 85), vigencia de los convenios (art. 86), contrato
  de sustitución (art. 15.3), modificación de condiciones del título III, cesión ilegal,
  descentralización productiva, causas de suspensión, contratos temporales, indemnización
  por despido objetivo, devengos extrasalariales y el contrato de formación en alternancia
  del RDL 2/2015. Son materia **G8**.
- **Tres de nómina y Seguridad Social**: retención de IRPF, base de cotización y concepto
  extrasalarial en la nómina.
- **Dos de la Ley 17/2006**, que es el tema 2: el artículo 8 y el vínculo del Presidente de
  la Corporación.
- **Seis de otras materias**, coladas en el mismo cuadernillo: el estándar IASA-TC 03,
  el Tribunal Europeo de Derechos Humanos, el Consejo de Seguridad de la ONU, el director
  del Coro Nacional de España, la tecnología de realidad aumentada en plató y el «limbo»
  escenográfico.

Ninguna de ellas obliga a tocar el tema 5.
