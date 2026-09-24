# Sondeo de viabilidad · Canal Sur (RTVA), concurso-oposición 2026

Fecha del sondeo: 24 de septiembre de 2026, el mismo día de la publicación en el BOJA.

**Siglas**: Agencia Pública Empresarial de la Radio y Televisión de Andalucía (**RTVA**);
Canal Sur Radio y Televisión, S.A. (**CSRTV**); Boletín Oficial de la Junta de Andalucía
(**BOJA**); Boletín Oficial del Estado (**BOE**); Corporación de Radio y Televisión
Española (**RTVE**); prevención de riesgos laborales (**PRL**).

## 1. La convocatoria

- **Resolución de 21 de septiembre de 2026**, de la Dirección General de la RTVA y de
  CSRTV. **BOJA núm. 186, de 24 de septiembre de 2026**, 95 páginas. Guardada en
  `convocatoria/canal-sur/2026-bases-boja-186.pdf`, con su texto extraído al lado.
- **228 plazas** de personal laboral fijo: 193 de CSRTV y 35 de la RTVA, en **40
  puestos** y 11 centros. Sevilla se lleva 148. Contadas sobre el Anexo I; la suma
  cuadra con el «Total general» del BOJA.
- **Cuatro fases sucesivas**: reingreso de excedencia, traslados, promoción interna y
  concurso-oposición libre. Las plazas que no se cubren en una fase pasan a la siguiente.
  **Cuántas llegan a la oposición libre no se sabe hasta que acaban las tres primeras.**
- **Plazo de solicitudes**: diez días laborables desde el día siguiente al de la
  publicación en el BOJA. Plataforma: `oposiciones.canalsur.es`.
- **Oposición libre** (base 14): oposición 55 %, concurso hasta 45 %. Dos ejercicios
  eliminatorios:
  1. **Test** sobre el temario común y el específico, con tres clases de pregunta
     (común, teoría específica y aplicación práctica). El reparto entre ellas lo fija el
     tribunal y lo publica antes del ejercicio.
  2. **Prueba práctica** de aptitud profesional del puesto.
- Umbral de cada ejercicio: **el 50 % de la media de las diez mejores notas**.
- Reservas (base 4): **22 plazas** para personas con discapacidad y **4** para víctimas
  de violencia de género.

**Las bases no fijan** el número de preguntas, la penalización, la duración, la fecha
del examen ni **ninguna fecha de corte normativa**. A falta de corte se trabaja con la
redacción vigente el día en que se escribe, y cada tema lo declara.

## 2. El programa

Anexo V, transcrito literal en `convocatoria/canal-sur/`:

- **Temario común: 10 temas**, el mismo para los cuarenta puestos. Nombra normas: la
  Constitución, el Estatuto de Autonomía, la Ley 13/2022, la Ley 10/2018 audiovisual de
  Andalucía, la Ley 18/2007 de la RTVA, la Ley 12/2007, la Ley 15/2022, la Ley 4/2023, la
  Ley 31/1995 y la normativa de protección de datos. Tres documentos **no son norma del
  BOE**: la **Carta del Servicio Público de la RTVA 2024-2029**, el **Estatuto
  profesional de la RTVA y Canal Sur** y el **X Convenio Colectivo Interprovincial de la
  RTVA**. Hay que encontrarlos y declarar su procedencia.
- **Temarios específicos: 40**, de 11 temas (Auxiliar Administrativo) a 29 (Letrado).
  Todos los ficheros están en `convocatoria/canal-sur/especificos/`, y el índice con temas y
  plazas en `convocatoria/canal-sur/README.md`.
- **Sólo tres específicos citan normas por su número** (Jefe de Sección de Coordinación
  Territorial, Redactor y Auditor). Los otros treinta y siete describen oficio y nombran
  leyes, como mucho, por su título. En el lenguaje del proyecto, la mayoría son como
  Imagen Personal: sin norma que citar, la exactitud se sostiene en la fuente técnica
  y en declarar el alcance.
- El BOJA titula cada bloque **«Temario específico propuesto»**. Es el texto publicado y
  el que se transcribe; si sale una corrección de errores, se vuelve a comparar.

**Comprobación de la transcripción**: el texto de los 41 ficheros se ha comparado
palabra a palabra con el extraído del Anexo V. **No falta ninguna palabra del cuerpo**;
las diferencias son los rótulos que pasan a título y ficha. La numeración de cada
puesto es correlativa, sin saltos.

## 3. Los exámenes anteriores

**No hay.** La nota de prensa de la propia RTVA dice que es el primer proceso de estas
características en más de veinte años. El proceso de estabilización de 2022 (bases de 22
de diciembre de 2022, adjudicaciones de octubre y diciembre de 2024) **no publica
cuadernillos ni plantillas** en su página. Tampoco hay test en las bolsas internas.

Consecuencia: **los cuarenta volúmenes serían «sin examen»**, como Ingeniería Técnica
Industrial o Ambientación Vestuario en RTVE. No hay acta de reparto que hacer (pasos 3 y
4 del traspaso), ni banco del que sacar la prueba de terminado. La prueba de cada tema
tendrá que ser **de diez a quince preguntas en el estilo que anuncia la base 14**
(teoría y aplicación práctica), y hay que decirlo en la portada de cada volumen.

## 4. Lo que ya hay en la bóveda

- **Vigentes** en `fuentes/`: la Ley 31/1995 de PRL (`BOE-A-1995-24292`) y la Ley 13/2022
  General de Comunicación Audiovisual (`BOE-A-2022-11311`). Se vuelven a volcar el día
  que se escriba el tema, por si han cambiado.
- En `fuentes/corte-20221221/` están la Constitución y muchas otras normas, pero
  **congeladas al corte de RTVE**. No sirven para Canal Sur sin volcarlas de nuevo con la
  redacción vigente, en su propia carpeta y sin pisar las de RTVE.
- **Temas de RTVE reutilizables como estructura, no como texto**: Constitución, Ley
  13/2022, PRL, protección de datos e igualdad. Los enunciados son distintos y el corte
  también; cualquier tema que pase a servir a las dos oposiciones exige reescribir su
  cabecera (apartado 10 del traspaso).
- Las normas andaluzas (Estatuto, Leyes 18/2007, 10/2018, 12/2007 y 9/2007) y la Ley
  15/2022 y la Ley 4/2023 **no están volcadas**. Sus identificadores se resuelven con
  `boe_buscar.py` antes de volcar nada; **no se escriben aquí de memoria**.

## 5. Veredicto

**Viable, con dos condiciones que se dicen en cada volumen**: no hay examen anterior, y
la mayoría de los específicos no nombran norma.

**Orden propuesto**:

1. **El temario común** (10 temas): sirve a los cuarenta puestos y es el único
   con norma detrás en casi todos sus epígrafes.
2. **Los específicos por número de plazas**: Redactor (61), Cámara Operador (21),
   Operador de Sonido (21), Operador Montador de Vídeo (17), Productor (14). Suman 134
   de las 228 plazas.

## 6. Lo que el sondeo no puede cerrar

- **El número de preguntas, la penalización y el reparto** entre común, teoría y
  práctica: los publica el tribunal antes del ejercicio.
- **La fecha del examen** y **cuántas plazas llegan** a la oposición libre.
- **Dónde se publican** la Carta del Servicio Público 2024-2029, el Estatuto profesional
  y el X Convenio Colectivo, y si el convenio está en el BOJA o sólo en la web de la RTVA.
- Si llegará una **corrección de errores** del Anexo V.
- **La decisión del titular**: qué puestos se hacen y en qué rama. El traspaso pide una
  rama por oposición; esta sesión trabaja en `claude/nice-carson-1zypx5`.
