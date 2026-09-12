# Esquema · Tema 1 del específico de Técnica de Equipos y Sistemas Electrónicos · Conceptos básicos de electricidad

Telegrama. **Cada línea lleva delante de dónde sale**: `[BOE]` = norma del Boletín Oficial del Estado ·
`[of]` = oficio y electrotecnia · `[plan]` = plantilla oficial. **Siglas**: la corriente alterna
(**CA**) y la continua (**CC**); el milivatio (**mW**) y el voltio (**V**).

**Cabecera.** Enunciado: punto 1 del anexo · **6 preguntas** · **cuatro se razonan y dos dependen de un
esquema que este esquema no ha visto.**

<!-- indice -->

## Índice

- [Las unidades son legales](#las-unidades-son-legales)
- [La ley de Ohm y la potencia](#la-ley-de-ohm-y-la-potencia)
- [Serie y paralelo](#serie-y-paralelo)
- [La corriente alterna y el trifásico](#la-corriente-alterna-y-el-trifásico)
- [El factor de potencia](#el-factor-de-potencia)
- [Potencia y semiciclos](#potencia-y-semiciclos)
- [Las dos preguntas con esquema](#las-dos-preguntas-con-esquema)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las unidades son legales

- `[BOE]` · **El voltio, el ohmio y el faradio están en el Real Decreto 2032/2009**, de unidades
  legales de medida, **citado celda a celda en el tema.**
- **LO QUE ESO SIGNIFICA**: **las unidades de este punto no son convenio del oficio: son derecho
  vigente.**

## La ley de Ohm y la potencia

- **LA LEY**: **V = I × R.** **De ella salen las tres fórmulas de potencia**: **P = V × I · P = I² × R
  · P = V² / R.**
- **CUÁL USAR**: **la que sólo pida datos que se tengan.** **Es lo único que hay que decidir.**

## Serie y paralelo

| | **Serie** | **Paralelo** |
|---|---|---|
| **Corriente** | **La misma por todos** | **Se reparte** |
| **Tensión** | **Se reparte** | **La misma en todos** ✔ |
| **Resistencia** | **Se suman** | **La inversa de la suma de inversas** |

- **PREGUNTA 40** · `[of]` · **En un circuito en paralelo, la tensión es la misma en todos los
  componentes.**
- **CÓMO NO CONFUNDIRSE NUNCA**: **en paralelo los dos extremos son los mismos dos nudos**, luego la
  tensión sólo puede ser una.

## La corriente alterna y el trifásico

- **PREGUNTA 59** · `[of]` · **Las fases de un sistema trifásico están desfasadas 120 grados.**
- **POR QUÉ 120**: **360 dividido entre tres.** **Es la única manera de repartir el círculo entre tres
  fases de forma equilibrada**, y de ahí que la suma de las tres en un sistema equilibrado sea cero.

## El factor de potencia

- **PREGUNTA 31** · `[of]` · **El factor de potencia es la relación entre la potencia activa y la
  aparente.**
- **LAS TRES POTENCIAS**: **activa** —la que trabaja, en vatios—, **reactiva** —la que va y viene, en
  voltamperios reactivos— **y aparente** —la suma vectorial, en voltamperios.
- **POR QUÉ IMPORTA EN UNA INSTALACIÓN**: **un factor de potencia bajo obliga a cables y protecciones
  mayores para la misma potencia útil**, y la compañía lo penaliza.

## Potencia y semiciclos

- **PREGUNTA 28** · `[of]` · **La potencia disipada en una resistencia es positiva en los dos
  semiciclos.**
- **EL RAZONAMIENTO EN UNA LÍNEA**: **P = I² × R**, y **un cuadrado nunca es negativo.** **La corriente
  cambia de signo; la potencia no.**
- **CONSECUENCIA FÍSICA**: **la resistencia calienta igual en los dos medios ciclos**, y por eso una
  onda alterna sí calienta pese a promediar cero.

## Las dos preguntas con esquema

- **PREGUNTA 7 del segundo llamamiento** · `[plan]` · **La tensión entre dos puntos del circuito es
  −1,6 V.**
- **PREGUNTA 26 del segundo llamamiento** · `[plan]` · **La potencia que entrega la fuente con carga es
  144 mW.**
- **ESTE ESQUEMA NO HA VISTO NINGUNO DE LOS DOS CIRCUITOS Y NO LOS DESCRIBE.** **La regla de la
  familia**: **se resuelven con la ley de Ohm y con las leyes de nudos y mallas**, y **el signo
  negativo de la primera sólo dice en qué orden se han tomado los dos puntos.**
- **LO QUE SÍ SE PUEDE LLEVAR APRENDIDO**: **una tensión negativa no es un error de cuenta**: es la
  misma tensión medida al revés.

## Lo que se ha preguntado

| Nº | Qué pregunta | Oficial |
|---|---|---|
| 28 | Potencia en la resistencia según el semiciclo | b) Positiva en los dos ✔ |
| 31 | Qué es el factor de potencia | a) Relación entre potencia activa y aparente ✔ |
| 40 | Qué ocurre con la tensión en un circuito en paralelo | a) Es la misma en todos los componentes ✔ |
| 59 | Desfase de las fases de un sistema trifásico | a) 120º ✔ |
| 7 (2.º llam.) | Tensión entre dos puntos de un circuito | a) −1,6 V ✔ **·** sólo con la plantilla |
| 26 (2.º llam.) | Potencia que entrega una fuente con carga | b) 144 mW ✔ **·** sólo con la plantilla |

**Las seis oficiales son correctas** · **dos descansan sólo en la plantilla, y son las dos que llevan
esquema.** · **Aviso de estudio**: **la tabla de serie y paralelo y las tres fórmulas de potencia son
lo que hay que llevar en la cabeza**: **con ellas se resuelven las cuatro preguntas razonables y se
ataca cualquier circuito de los que llevan figura.**
