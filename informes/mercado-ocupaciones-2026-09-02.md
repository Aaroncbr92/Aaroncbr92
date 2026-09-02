# Qué ocupación tipo conviene escribir después, y por qué

Hecho el 2026-09-02, con los tres temarios que tenemos ya cerrados. **No es una
opinión sobre qué temario sería bonito**: es el cruce de cuatro cifras que se
pueden comprobar una a una, y todas salen de las bases específicas de la
convocatoria 1/2022 o de los cuadernillos de 2024 que ya están en el proyecto.

Las cuatro son:

1. **Puestos convocados por concurso-oposición**, no puestos totales. El temario
   sólo sirve al que hace examen. Los del **punto 6** de las Bases Generales son
   **concurso de méritos**: se resuelven con la antigüedad del anexo 5 y **no hay
   examen**. Contarlos infla el mercado.
2. **Titulación exigida**, que decide el tamaño del embudo. Bachillerato o ciclo
   superior deja entrar a cualquiera; un grado universitario, a menos; y una
   ocupación técnica, sólo a quien viene del oficio aunque no lo pida el papel.
3. **Cuánto pesa el temario general en su examen**, medido sobre los cuadernillos
   de octubre de 2024 con `herramientas/calibrar.py`. Ese bloque **ya está
   escrito**, y es el mismo para las más de cincuenta ocupaciones.
4. **Si el temario específico tiene norma detrás.** Donde la hay, el método corre
   entero —volcado, verificación, cuatro lentes— y el tema sale verificado. Donde
   no, cada dato hay que cazarlo a mano, que es lo que costó el punto 1 de
   Información y Contenidos.

## Las cifras

| Ocupación tipo | Puestos | Con examen | Titulación | General en su examen |
|---|---:|---:|---|---:|
| Información y Contenidos *(hecho)* | 474 | 245 | grado | 22-28 % |
| **Sonido** | 102 | 87 | bachillerato / CFGS | 9 % |
| **Gestión Administrativa** | **98** | **80** | **bachillerato / CFGS** | **29 %** |
| Información gráfica y captación de imagen y sonido | 81 | 67 | — | 9 % |
| **Gestión** | **60** | **52** | **grado o licenciatura** | **30 %** |
| Producción (Asistencia) *(hecho)* | 54 | 39 | — | 31-34 % |
| Producción | 35 | 31 | — | 31 % |
| Documentación *(hecho)* | 30 | 23 | — | 18 % |
| Realización Televisión | 30 | 23 | — | 4-12 % |
| Imagen Personal | 10 | 9 | — | 12 % |

El peso del general es de `informes/calibracion-examenes-2024.md`, clasificación
por palabras clave: **sirve para ordenar, no para dar una cifra por buena**.

**Y hay un descuadre en las bases de Documentación**, anotado aquí porque cuenta:
el texto dice «del total de los **30** puestos» y su propia tabla suma **37**
—13 + 1 + 23—. No cambia nada de lo que hemos hecho; queda dicho porque la cifra
de arriba es la del texto.

## Las dos que salen

### 1 · Gestión Administrativa — 98 puestos, 80 con examen

**Es la de embudo más ancho de todo el proceso.** Pide **bachillerato o ciclo
formativo de grado superior**, no pide experiencia audiovisual, y de sus 98
puestos **80 se juegan en examen** —64 turno libre y 16 de discapacidad—. Ninguna
otra ocupación junta tantas plazas de examen con tan poca barrera de entrada.

**El trabajo ya hecho rinde aquí más que en ningún sitio.** El temario general es
el **29 %** de su cuadernillo de 2024 —28 de 96 preguntas—, el tercer porcentaje
más alto de los 87 exámenes transcritos, por delante de las tres ocupaciones que
hemos preparado salvo Producción.

**Y su específico es sobre todo norma.** Sus diez puntos son gestión
administrativa y acto administrativo, contrato de trabajo, Seguridad Social,
nóminas y retenciones, y **el Plan General de Contabilidad, que las propias bases
citan con su referencia del BOE** —núm. 278, de 20/11/2007, texto consolidado,
última modificación de 30 de enero de 2021—. Eso es exactamente lo que hace
`boe.py`.

**Lo que hay que decir en contra, porque lo hay.** Sus puntos 6 a 10 —matemática
financiera, probabilidad y estadística, ofimática, **Windows 10 Pro versión
22H2** e Internet— **no tienen BOE**. El de Windows se verifica contra la
documentación de Microsoft, que es el cuarto nivel de la jerarquía, y los de
matemáticas no se verifican contra una fuente: se demuestran. **Es media
ocupación de trabajo de otro tipo**, y conviene saberlo antes de empezar y no a
mitad.

### 2 · Gestión — 60 puestos, 52 con examen

**Menos plazas, pero es el caso en el que el método funciona entero.** Su temario
específico es **derecho del trabajo puro**: empieza por el **Estatuto de los
Trabajadores**, que las bases citan como «Real Decreto Legislativo 2/2015, BOE
núm. 255, de 24/10/2015, **última actualización publicada el 8/9/2022**» —o sea,
**anterior a nuestra fecha de corte del 21 de diciembre de 2022**, con lo que el
texto consolidado que hay que estudiar es el que ya sabemos volcar y **no se
mueve**—. Después: convenios colectivos, contrato de trabajo, modificación de
condiciones, tiempo de trabajo, salario, derechos y deberes. **Todo con norma
detrás**, como los temas 2 y 17 de Producción, que son los que salieron limpios a
la primera.

**Su examen es el más largo de los tres tamaños** —108 preguntas, 90 más 18 de
reserva— y el general pesa el **30 %**.

**Pero la razón de ponerla la segunda no es ésa: es que se solapa con la
primera.** «El contrato de trabajo: concepto y naturaleza, forma, modalidades,
duración, modificación, suspensión y extinción» es **el punto 2 de Gestión
Administrativa y el punto 4 de Gestión**, casi con las mismas palabras; y
Seguridad Social, salario y nóminas vuelven a cruzarse. **Dos libros por bastante
menos que el doble de trabajo**, y el segundo con la fuente ya volcada.

**En contra**: pide **titulación universitaria**, así que su embudo es más
estrecho que el de Gestión Administrativa.

## La que no elijo, y por qué

**Sonido tiene más plazas que las dos** —102, con 87 de examen— y también pide
sólo bachillerato. **Va tercera por dos motivos.** El temario general es apenas
el **9 %** de su cuadernillo, un tercio de lo que rinde en Gestión: casi todo
sería trabajo nuevo. Y su específico es técnico, del tipo que en Producción
obligó a bajar a UIT, AES y ETSI y dejó una norma —la AES10 del MADI— **detrás de
un muro de pago**. Es un buen tercer libro; no es el siguiente.

## El dato de mercado que no es nuestro y hay que tratar como tal

La prensa de 2026 da por próxima una **convocatoria 1/2025 ampliada**, con cifras
que van de 868 a más de mil puestos, y la compara con los 1.470 de la 1/2022.
**No lo hemos comprobado en fuente oficial** y por eso no está en la tabla: es
prensa, no BOE ni bases. Si se confirma, **mueve el calendario, no el orden**: las
ocupaciones administrativas son las que más plazas repiten convocatoria tras
convocatoria, porque son las que más rotación tienen.

## Fuentes

- Bases específicas 1/2022 de **Gestión Administrativa** y de **Gestión**,
  guardadas en `convocatoria/bases/` con su transcripción. Publicadas por la
  sección sindical de USO en RTVE.
- Las demás cifras de puestos, leídas en las bases específicas de cada ocupación
  del mismo origen, y las de las tres que preparamos, en las que ya teníamos.
- Reparto por materia: `informes/calibracion-examenes-2024.md`, sobre las
  transcripciones de `convocatoria/examenes/`.
