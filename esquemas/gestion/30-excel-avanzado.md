# Esquema · Gestión 30: Excel avanzado (versión Excel 2019)

Esqueleto para repasar. Todo desarrollado y verificado en el tema.

**Siglas**: Visual Basic para Aplicaciones (**VBA**), el procesamiento analítico
en línea (**OLAP**, del inglés *online analytical processing*), el coeficiente de determinación
(**R²**) y el Boletín Oficial del Estado (**BOE**).

<!-- indice -->

## Índice

- [Referencias](#referencias)
- [Funciones](#funciones)
- [Anidación](#anidación)
- [Tablas de datos](#tablas-de-datos)
- [Tablas dinámicas](#tablas-dinámicas)
- [Macros](#macros)
- [Análisis de datos](#análisis-de-datos)
- [El aviso](#el-aviso)

<!-- /indice -->

## Referencias

`A1` relativa · `$A$1` absoluta · `$A1` y `A$1` **mixtas**. La tecla **F4** recorre los cuatro
estados.
*La mixta es la que resuelve las tablas de doble entrada con una sola fórmula.*
Errores: `#¡DIV/0!` · `#¿NOMBRE?` · `#¡VALOR!` · `#¡REF!` · `#N/A` · `#¡NUM!` · `#¡NULO!`.

## Funciones

- **Búsqueda**: `BUSCARV` —cuarto argumento: `FALSO` exacta, `VERDADERO` aproximada, **que exige la
  primera columna ordenada**— · `BUSCARH` · **`INDICE` + `COINCIDIR`**, sin la limitación de buscar
  sólo en la primera columna.
- **Lógicas**: `SI`, `Y`, `O`, `NO`, `SI.ERROR`, `SI.CONJUNTO`.
- **Condicionales**: `SUMAR.SI` / `SUMAR.SI.CONJUNTO`, `CONTAR.SI`, `PROMEDIO.SI`.
  *Ojo al orden: en `SUMAR.SI` el rango de suma va al final; en `SUMAR.SI.CONJUNTO`, al principio.*
- **Financieras**: `PAGO`, `VA`, `VF`, `TASA`, `NPER`, `VNA`, `TIR`.
- **Matriciales**: en 2019 se introducen con **`Ctrl + Mayús + Intro`**. **Las matrices dinámicas
  no existen en Excel 2019.**

## Anidación

Una función como argumento de otra; la interior se evalúa primero.
`SI` anidados en orden excluyente · `SI.ERROR(BUSCARV(...); "No encontrado")` · `INDICE` con
`COINCIDIR` dentro.
Límites: **64 niveles** y **255 argumentos**. Depurar con **F9** y con **Fórmulas › Evaluar
fórmula**.

## Tablas de datos

**Análisis de hipótesis**: cambiar valores para ver cómo afectan al resultado de una fórmula.
Tres herramientas: **Escenarios** (conjuntos con nombre) · **Buscar objetivo** (una variable, hacia
atrás) · **Tabla de datos** (**una o dos** variables, muchos resultados a la vez).
En la de dos variables, **la fórmula va en la esquina**. Genera una matricial `TABLA` que **no se
puede editar por partes**.

## Tablas dinámicas

Datos de origen: **columnas con una sola fila de encabezado**, sin filas vacías ni celdas
combinadas.
**Cuatro áreas**: **Filas · Columnas · Valores · Filtros**.
Resumen por defecto: **Suma** para datos numéricos, **Contar** para texto.
No se actualiza sola: hay que **actualizar**, y mejor construirla sobre una **tabla**.

**Campo calculado frente a elemento calculado**:

| | **Campo calculado** | **Elemento calculado** |
|---|---|---|
| Añade | un campo nuevo | un elemento dentro de un campo |
| Opera sobre | **la suma** de los datos | **los registros individuales** |

*Con sumas y multiplicaciones coinciden; con divisiones, promedios o porcentajes, no.*
No disponibles con origen **OLAP**.

**Segmentación de datos**: botones para filtrar que además **muestran el estado del filtro**, cosa
que el desplegable de Filtros no hace. Una misma segmentación puede gobernar **varias tablas
dinámicas** → cuadro de mando. Su versión para fechas es la **escala de tiempo**.

## Macros

**Una acción o un conjunto de acciones que se puede ejecutar todas las veces que se desee.** Se
graban los clics y las pulsaciones, y después se pueden modificar.
**Primero hay que mostrar la pestaña Desarrollador, que está oculta por defecto.**
Grabar: **Programador › Código › Grabar macro** —nombre, tecla de método abreviado, descripción—.
Decisiones que cambian el resultado: **dónde guardarla** —este libro, uno nuevo o el **Libro de
macros personal**— y **referencias relativas o absolutas**.
Editar: **Macros › Editar** → Editor de Visual Basic.
Guardar en **`.xlsm`**: un `.xlsx` no admite macros. Al abrir, hay que **habilitar el contenido**.

## Análisis de datos

Complemento **Herramientas para análisis**, que **hay que activar**.
- **Estadística descriptiva**: informe **de una sola variable**, con tendencia central y dispersión.
  *Devuelve «varianza de la muestra», es decir, la cuasivarianza del punto 29.*
- **Media móvil**: proyecta con el promedio de **N períodos anteriores**. Elegir N es elegir cuánto
  ruido se sacrifica a cambio de cuánto retraso.
- **Regresión**: **mínimos cuadrados**, con **una o más variables independientes**; se apoya en
  `LINEST`. Devuelve **R²**. *Mide asociación, no causa.*

## El aviso

**Ninguna pregunta cae aquí**, y sin embargo el temario de Gestión Administrativa, examinado el
mismo año, **sí preguntó por ofimática**. Es materia del anexo y hay que llevarla.