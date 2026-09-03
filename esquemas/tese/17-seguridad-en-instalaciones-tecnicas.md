# Esquema · Tema 17 del específico de Técnica de Equipos y Sistemas Electrónicos · Seguridad en instalaciones técnicas

Telegrama. **Cada línea lleva delante de dónde sale**: `[BOE]` = norma del Boletín Oficial del Estado ·
`[of]` = oficio de instalación · `[plan]` = plantilla oficial. **Siglas**: la alta tensión (**AT**) y la
baja tensión (**BT**); la radiofrecuencia (**RF**); los equipos de protección individual (**EPI**); el
reglamento electrotécnico para baja tensión (**REBT**) y sus instrucciones técnicas complementarias
(**ITC-BT**, de donde la **ITC-BT-24**); el neutro (**N**); el voltio (**V**) en valor eficaz de
alterna (**Vrms**) y en continua (**V cc**); el miliamperio (**mA**); y el gigahercio (**GHz**).

**Cabecera.** Enunciado: punto 20 del anexo · **4 preguntas** · **es el ÚNICO punto de los diecisiete
cuyas respuestas están en el Boletín Oficial del Estado**, y **el tema las cita literalmente.**

<!-- indice -->

## Índice

- [Dónde empieza la alta tensión](#dónde-empieza-la-alta-tensión)
- [El riesgo eléctrico y el diferencial](#el-riesgo-eléctrico-y-el-diferencial)
- [La radiofrecuencia y la salud](#la-radiofrecuencia-y-la-salud)
- [La acometida de la unidad móvil](#la-acometida-de-la-unidad-móvil)
- [Los equipos de protección individual](#los-equipos-de-protección-individual)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Dónde empieza la alta tensión

- **PREGUNTA 96** · `[BOE]` · **Se considera alta tensión a partir de 1.000 Vrms en alterna y 1.500 V
  en continua.**
- **HAY QUE SEGUIR UNA CADENA DE DOS NORMAS, PORQUE LA DE PREVENCIÓN NO DA LA CIFRA: LA REMITE.**
- **PRIMER ESLABÓN** · `[BOE]` · **Real Decreto 614/2001, anexo I, definición 5**: «Alta tensión. Baja
  tensión. Tensiones de seguridad: las definidas como tales en los reglamentos electrotécnicos.»
- **SEGUNDO ESLABÓN** · `[BOE]` · **Artículo 2.1 del Real Decreto 842/2002**: **la baja tensión llega
  hasta 1.000 voltios en alterna y 1.500 en continua.** **Por encima ya no hay baja tensión: hay
  alta.**
- **QUIEN BUSQUE EL NÚMERO EN LA NORMA DE PREVENCIÓN NO LO ENCONTRARÁ**, y **esa definición 5 es
  precisamente el aviso.**
- **EL AVISO QUE VALE MÁS QUE LA PREGUNTA**: **la frontera legal no coincide con la sensación de
  peligro.** **Una instalación de 400 voltios es baja tensión y mata igual.** **Lo que la clasificación
  cambia son las exigencias, la cualificación exigida y los procedimientos.**

## El riesgo eléctrico y el diferencial

| Tipo de contacto | Qué es |
|---|---|
| **Directo** | **Tocar una parte que está en tensión por diseño** |
| **Indirecto** | **Tocar una masa puesta en tensión por una avería** ✔ |

- **PREGUNTA 58** · `[BOE]` · **Los interruptores diferenciales protegen a las personas contra los
  contactos indirectos.**
- **CÓMO FUNCIONA**: **compara lo que entra por la fase con lo que vuelve por el neutro; si difieren
  más de su valor asignado, parte de la corriente se va por otro camino y abre.**

| Protección | Qué vigila | A quién protege |
|---|---|---|
| **Diferencial** | **La diferencia entre entrada y retorno** | **A las personas** ✔ |
| **Magnetotérmico** | **La intensidad** | **A la instalación** |
| **Fusible** | **La intensidad** | **A la instalación** |
| **Puesta a tierra** | **Nada: da camino a la fuga** | **Es la que permite que el diferencial actúe** |

- **LA REGLA DE MEMORIA**: **el diferencial protege a las personas y el magnetotérmico a los cables.**
- `[BOE]` · **La ITC-BT-24 sitúa el diferencial en el capítulo de contactos indirectos**, y **fija en
  30 mA la sensibilidad de la protección complementaria frente a contactos directos** y en **50 voltios
  eficaces la tensión límite convencional en condiciones normales.**
- **EL MATIZ QUE LA RESPUESTA OFICIAL RESPETA**: **el diferencial es protección PRINCIPAL contra los
  indirectos y sólo COMPLEMENTARIA contra los directos.**
- **LA DEFINICIÓN LEGAL DE RIESGO ELÉCTRICO INCLUYE MÁS DE LO QUE NADIE ESPERA** · `[BOE]` · **Real
  Decreto 614/2001, anexo I, definición 1**: **choque eléctrico, quemaduras por choque o arco, caídas o
  golpes como consecuencia de choque o arco, e incendios o explosiones originados por la
  electricidad.**

## La radiofrecuencia y la salud

- **PREGUNTA 5** · `[BOE]` · **El efecto que NO se relaciona con la radiación de radiofrecuencia es la
  ionización de materia corporal.**
- **ES LA PREGUNTA MÁS LIMPIA DE LA OCUPACIÓN**: **tres de las cuatro opciones están literalmente en el
  artículo 2 del Real Decreto 299/2016 y la cuarta no.**

| Opción | Dónde está en la norma |
|---|---|
| **Corrientes de contacto** | **Artículo 2.c).5: efecto indirecto** |
| **Calentamiento de los tejidos** | **Artículo 2.b).1: efecto térmico directo** |
| **Ionización de materia corporal** | **En ninguna de las dos letras** ✔ |
| **Corrientes inducidas en las extremidades** | **Artículo 2.b).3: efecto directo** |

- **EL PORQUÉ FÍSICO**: **ionizar es arrancar electrones**, y hace falta energía de ultravioleta duro
  para arriba. **El propio real decreto lo confirma sin decirlo**: **su artículo 2.a) regula los campos
  de 0 Hz a 300 GHz**, que es toda la región no ionizante.
- **LA REGLA DE TRABAJO**: **no subir a una torre con el transmisor emitiendo, respetar las distancias
  señalizadas y no manipular guías ni conectores de salida con potencia aplicada.**

## La acometida de la unidad móvil

- **PREGUNTA 6 del segundo llamamiento** · `[plan]` · **El conector adecuado es el tercero de la
  figura.** **Este esquema no ha visto la figura y no la describe.**
- **LO QUE SÍ SE RAZONA**: **tres fases, neutro y conductor de protección son cinco conductores**, luego
  **el conector es de cinco polos.**

| Configuración | Para qué |
|---|---|
| **2 polos más tierra** | **Monofásico** |
| **3 polos más tierra** | **Trifásico sin neutro** |
| **4 polos más tierra** | **Trifásico con neutro y protección** ✔ |

- **LO DEMÁS QUE MIRAR**: **el calibre** —32, 63 o 125 amperios según el tamaño de la unidad— **y el
  color**: **rojo el trifásico de 400 voltios, azul el monofásico de 230, amarillo el de 110.**
- **EL AVISO, PORQUE ES DONDE OCURREN LOS ACCIDENTES**: **la acometida es lo primero que se conecta y lo
  último que se desconecta, y es donde más energía hay.** **Una unidad móvil enchufada sin conductor de
  protección deja todas sus carcasas sin defensa frente al contacto indirecto**, y con ellas todos los
  soportes de cámara que la gente toca.

## Los equipos de protección individual

- `[BOE]` · **Real Decreto 614/2001, anexo IV, parte A, apartado 2**: **accesorios aislantes · útiles
  aislantes o aislados · pértigas aislantes · dispositivos aislantes o aislados · equipos de protección
  individual.**
- **LA LISTA VA DE FUERA HACIA DENTRO**: **primero se aísla lo que está en tensión, después la
  herramienta, después lo que separa del suelo, y sólo al final lo que el trabajador lleva puesto.**
  **El equipo de protección individual es el último recurso, no el primero.**
- **QUIÉN PUEDE HACER ESTAS OPERACIONES** · `[BOE]` · **anexo IV, parte A, apartado 1**: **maniobras,
  mediciones y verificaciones, sólo trabajadores autorizados; en alta tensión, trabajadores
  cualificados.**

| Figura | Qué exige la norma |
|---|---|
| **Autorizado** | **Que el empresario lo haya autorizado según su capacidad** |
| **Cualificado** | **Autorizado y además con formación acreditada o dos años de experiencia certificada** |

- **LA REGLA QUE ESTE PUNTO DEJA**: **en baja tensión basta con estar autorizado; en alta tensión hay
  que estar cualificado.** **Ésa es la consecuencia práctica de la frontera de los 1.000 voltios.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 5 | Efecto que NO se relaciona con la radiación de RF | c) Ionización de materia corporal ✔ |
| 58 | Para qué se usan los interruptores diferenciales | b) Protección contra contactos indirectos ✔ |
| 96 | A partir de qué valores hay alta tensión | b) 1.000 Vrms y 1.500 V cc ✔ |
| 6 (2.º llam.) | Conector para la acometida de una unidad móvil | c) El tercero ✔ **·** figura |

**Las cuatro oficiales son correctas** · **una descansa en la plantilla y es la que lleva figura** ·
**las otras tres están respaldadas por norma citada literalmente**, cosa que no ocurre en ningún otro
punto del específico. · **Aviso de estudio**: **este punto se estudia con el Boletín Oficial del
Estado.** **Tres cifras: 1.000 y 1.500 voltios, y 30 miliamperios.**
