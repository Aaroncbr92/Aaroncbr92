# Esquema · Tema 9 del específico de Ingeniería Superior · Telecomunicación · Comunicaciones y radiodifusión por satélite

Telegrama. **Cada línea lleva delante de dónde sale**: `[of]` = oficio de enlaces por satélite ·
`[plan]` = enunciado del propio anexo · `[exam]` = opciones del propio cuadernillo. **Siglas**: la
potencia isótropa radiada equivalente (**PIRE**); el gigahercio (**GHz**); y las letras con que se
nombran las bandas —**L**, **C**, **Ku** y **Ka**—, que se leen en el segundo epígrafe.

**Cabecera.** Enunciado: punto 9 del anexo · **una pregunta** · **sin norma del boletín**: los
estándares de difusión por satélite son normas de un organismo europeo de normalización que este
proyecto no ha consultado.

**La idea que lo ordena** · `[of]` · **El eslabón débil es siempre la BAJADA**, porque **la potencia a
bordo es limitada y el receptor doméstico es pequeño y barato.** **Todo el diseño de la difusión por
satélite consiste en gastar bien esa potencia.**

<!-- indice -->

## Índice

- [Las órbitas](#las-órbitas)
- [Las bandas](#las-bandas)
- [El enlace](#el-enlace)
- [La televisión por satélite](#la-televisión-por-satélite)
- [Los servicios](#los-servicios)
- [Lo que se ha preguntado](#lo-que-se-ha-preguntado)

<!-- /indice -->

## Las órbitas

| Órbita | Cómo se ve desde el suelo | Para qué |
|---|---|---|
| **geoestacionaria** | **FIJA en el cielo**: gira con la Tierra sobre el ecuador | **difusión y enlaces fijos** |
| **media** | **se mueve; hacen falta varios** | **navegación** |
| **baja** | **pasa deprisa: constelaciones y seguimiento** | **baja latencia: datos y observación** |

- **las tres consecuencias de la geoestacionaria** · `[of]` · **1)** la antena no se mueve, **y eso es
  toda la razón de que la difusión sea geoestacionaria**; **2)** la **latencia es alta y no se puede
  bajar**: la señal recorre dos veces la distancia hasta la órbita, **es física, no ingeniería**;
  **3)** una posición orbital es **un recurso escaso** coordinado internacionalmente.

## Las bandas

| Banda | Rasgo | Uso |
|---|---|---|
| **L** | **la más baja: poca atenuación por lluvia, poca capacidad** | **móvil, navegación, radio** |
| **C** | **robusta frente a la lluvia; antenas grandes** | **contribución y difusión en zonas de lluvia intensa** |
| **Ku** | **el compromiso: antenas pequeñas y buena capacidad** | **difusión doméstica y unidades móviles** |
| **Ka** | **la MÁS ALTA: mucha capacidad, antenas muy pequeñas** | **banda ancha por satélite** |

- **LA REGLA QUE RESUELVE LA PREGUNTA** · `[exam]` · **El orden es L, C, Ku, Ka**, y **la de mayor
  frecuencia de las cuatro es la última.** **Va de lo robusto y voluminoso a lo capaz y frágil.**
- **el intercambio que ese orden esconde** · `[of]` · **A más frecuencia, más capacidad y antenas más
  pequeñas, pero MÁS ATENUACIÓN POR LLUVIA.** **Por eso la contribución crítica prefirió
  históricamente bandas bajas**, y **por eso los sistemas modernos llevan control de potencia y
  modulación adaptativa.**

## El enlace

| Mitad | Qué la caracteriza |
|---|---|
| **ascendente** | **potencia y antena grandes**, que están en tierra y se pueden pagar |
| **descendente** | **potencia limitada**: la del satélite, que es lo escaso |

| Parámetro del balance | Qué mide |
|---|---|
| **potencia isótropa radiada equivalente** | **lo que se entrega al espacio en la dirección buena** |
| **pérdidas de espacio libre** | **lo que se pierde sólo por la distancia**: crecen con la frecuencia |
| **atenuación por lluvia** | **lo que absorbe el camino**, y es lo que varía |
| **ganancia frente a temperatura de ruido** | **la calidad del receptor** |
| **margen de enlace** | **lo que sobra sobre el mínimo**: es lo que se come la lluvia |

- **la regla de proyecto** · `[of]` · **Un enlace se dimensiona para el peor caso admitido, no para el
  día bueno.** **Subir un escalón de disponibilidad cuesta mucho margen.**
- **la huella** · `[of]` · **Un haz ancho cubre mucho con poca potencia por metro cuadrado; uno
  estrecho concentra.** **Los satélites modernos usan muchísimos haces estrechos para reutilizar
  frecuencias**, **igual que una red móvil reutiliza canales entre celdas.**

## La televisión por satélite

| Pieza de la recepción | Qué hace |
|---|---|
| **parabólica** | **concentra la energía en el foco** |
| **bloque de bajo ruido** | **amplifica con muy poco ruido propio y BAJA la frecuencia** |
| **cable y repartidores** | **llevan la banda intermedia al receptor** |
| **receptor** | **sintoniza, demodula y descodifica** |

- **las dos cosas del bloque de bajo ruido** · `[of]` · **Baja la frecuencia ANTES del cable**, porque
  **una banda de gigahercios no viaja por un coaxial doméstico**; y **su ruido propio manda sobre todo
  lo demás**, porque **el ruido del primer amplificador se amplifica con la señal en todos los
  siguientes.**
- **lo que explica el salto de generación** · `[of]` · **La modulación y codificación ADAPTATIVAS.**
  **En vez de emitir siempre con el ajuste que aguanta el peor receptor, se ajusta la robustez para
  cada destino.** **Eso convierte en capacidad el margen que antes se desperdiciaba.**

## Los servicios

| Servicio | Qué es |
|---|---|
| **difusión directa al hogar** | **la televisión por satélite, con su acceso condicional** |
| **distribución a cabeceras** | **llevar el múltiplex a operadores y centros emisores** |
| **contribución ocasional** | **enlace desde el lugar de la noticia** |
| **contribución permanente** | **un canal alquilado de forma continua entre sedes** |
| **datos y banda ancha** | **acceso donde no llega la fibra** |
| **recogida de material** | **agencias e intercambios internacionales** |

- **la contribución ocasional se contrata** · `[of]` · **Un enlace por satélite no se «enciende»: se
  reserva, se coordina con el operador y se alinea**, y **eso tiene un calendario que hay que meter en
  la planificación.**
- **EL SATÉLITE ES LA REDUNDANCIA NATURAL DE LA FIBRA** · `[of]` · **Los dos medios fallan por causas
  independientes** —una excavadora frente a una tormenta—. **Poner dos fibras por la misma zanja no es
  redundancia.**

## Lo que se ha preguntado

| Nº | Qué pide | Respuesta |
|---|---|---|
| 92 | Cuál de cuatro bandas de satélite es la de mayor frecuencia | **La Ka** ✔ **·** el orden es L, C, Ku, Ka |
