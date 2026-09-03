# Esquema · Tema 4 del específico de Técnica de Equipos y Sistemas Electrónicos · Amplificadores operacionales

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio y electrónica analógica ·
`[plan]` = plantilla oficial. **Siglas**: el amplificador operacional (**AO**) y el voltio (**V**).

**Cabecera.** Enunciado: punto 4 del anexo · **5 preguntas** · **tres dependen de un esquema y dos se
razonan.**

<!-- indice -->

## Índice

- [Qué es un amplificador operacional](#qué-es-un-amplificador-operacional)
- [Las tres reglas que resuelven cualquier circuito](#las-tres-reglas-que-resuelven-cualquier-circuito)
- [El seguidor](#el-seguidor)
- [Las tres preguntas con esquema](#las-tres-preguntas-con-esquema)
- [Lo que el enunciado pide y el examen no pregunta](#lo-que-el-enunciado-pide-y-el-examen-no-pregunta)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Qué es un amplificador operacional

- **PREGUNTA 46** · `[of]` · **Una propiedad teórica del amplificador operacional es la alta impedancia
  de entrada.**
- **EL AMPLIFICADOR IDEAL, EN CUATRO RASGOS**: **ganancia infinita en lazo abierto · impedancia de
  entrada infinita · impedancia de salida nula · ancho de banda infinito.**
- **POR QUÉ IMPORTA LA IMPEDANCIA DE ENTRADA ALTA**: **para no cargar el circuito que se está
  midiendo**, que es la misma idea de la sonda del tema 13.

## Las tres reglas que resuelven cualquier circuito

1. **La entrada no consume corriente.** **Impedancia de entrada infinita.**
2. **Con realimentación negativa, las dos entradas están al mismo potencial.** **Es el
   cortocircuito virtual.**
3. **La salida hace lo que haga falta para que la regla 2 se cumpla.**

- **CON ESAS TRES SE DEDUCEN TODAS LAS CONFIGURACIONES**: **inversor, no inversor, seguidor, sumador,
  restador, integrador y derivador.** **No hay que memorizar fórmulas: hay que aplicar las tres
  reglas.**

## El seguidor

- **QUÉ HACE**: **la salida copia la entrada.** **Ganancia uno.**
- **PARA QUÉ SIRVE ENTONCES**: **para adaptar impedancias.** **Entra con impedancia altísima y sale con
  impedancia casi nula**, y eso permite conectar una fuente débil a una carga exigente.
- **PREGUNTA 5 del segundo llamamiento** · `[of]` · **De un seguidor con 3 voltios a la entrada y 2 a
  la salida se concluye que está dañado: la salida debería ser 3 V.**
- **POR QUÉ ES UNA PREGUNTA BUENA**: **mide si se ha entendido qué hace el circuito**, no si se
  memorizó una fórmula. **Un seguidor que no sigue está roto: no hay otra lectura.**

## Las tres preguntas con esquema

- **PREGUNTA 33** · `[plan]` · **Ante una entrada cuadrada se obtiene una señal triangular.**
- **PREGUNTA 43** · `[plan]` · **Con 2,5 V a la entrada, la salida es 2,5 V.**
- **PREGUNTA 65** · `[plan]` · **El valor de tensión a la salida del circuito es 6 V.**
- **ESTE ESQUEMA NO HA VISTO NINGUNO DE LOS TRES CIRCUITOS Y NO LOS DESCRIBE.**
- **LA REGLA DE LA FAMILIA DE LA 33**: **el circuito que convierte una onda cuadrada en triangular es
  el integrador.** **Integrar una constante da una rampa**, y una cuadrada es una sucesión de
  constantes de signo alterno.
- **LA REGLA DE LA FAMILIA DE LA 43**: **una salida igual a la entrada es un seguidor.**
- **LA REGLA DE LA FAMILIA DE LA 65**: **cualquier salida se obtiene aplicando las tres reglas del
  epígrafe anterior al esquema que se tenga delante.**

## Lo que el enunciado pide y el examen no pregunta

- **EL COMPARADOR**: **el mismo componente sin realimentación negativa.** **La salida se va a un
  extremo o al otro según qué entrada sea mayor.**
- **EL SUMADOR Y EL RESTADOR**: **la base de una mesa de mezclas analógica y de una entrada
  diferencial.**

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 33 | Qué señal se obtiene ante una entrada cuadrada | d) Una señal triangular ✔ **·** sólo con la plantilla |
| 43 | Tensión de salida con 2,5 V a la entrada | d) 2,5 V ✔ **·** sólo con la plantilla |
| 46 | Propiedad teórica de un amplificador operacional | c) Alta impedancia de entrada ✔ |
| 65 | Valor de tensión a la salida del circuito | a) 6 V ✔ **·** sólo con la plantilla |
| 5 (2.º llam.) | Qué se concluye de un seguidor con 3 V dentro y 2 fuera | b) Está dañado ✔ |

**Las cinco oficiales son correctas** · **tres descansan sólo en la plantilla.** · **Aviso de
estudio**: **las tres reglas del epígrafe 2 son todo el punto.** **Quien las tenga interiorizadas
resuelve cualquier esquema que le pongan delante, y quien no, no resuelve ninguno.**
