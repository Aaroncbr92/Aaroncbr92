# Puesto 29 · Tema 7 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). No corrijo: el tema queda como estaba.
Tema: `temas/canal-sur-especificos/29-operador-a-informatico/07-automatizacion-y-administracion-mediante-powershell.md`
(1.722 líneas, unas 15.700 palabras con código).

## Alcance

- «Copiado del común» y «Copiado de RTVE sin cambios»: ninguno (informe de redacción). Lente de
  exactitud sobre el tema entero.
- Fuentes: las descargas de Microsoft Learn es-es hechas el 05-10-2026 por la redacción (93 ficheros
  en el directorio temporal de la sesión), releídas el **06-10-2026** sobre los pasajes concretos, y una
  descarga nueva el 06-10-2026: `about_Operators?view=powershell-5.1`.
- Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.

## Lente 1 · Exactitud

Comprobado contra la fuente y correcto (muestra de la prosa en redonda, que es donde cae el error 9):
alias de los 21 cmdlets de las tablas de los ep. 8 y 11 (todas las plataformas / sólo Windows, uno a
uno); tabla de ciclo de vida (fechas y .NET: la corrección del desplazamiento de columnas es buena,
la fila «.NET 11.0» es de la 7.7 preliminar); winget, MSIX por defecto desde 7.6.0, `--installer-type
wix`; ámbitos y almacenamiento de la directiva (5.1 y 7), GPO, Unrestricted y la intranet; rutas de
los cuatro perfiles; búsqueda 12/78 y `help pr*cess`; `Get-Help -Detailed/-Examples` sólo con ayuda
instalada; `Get-Command` y la importación de módulo; sufijos `kb`–`pb` (1024, cualquier combinación
de mayúsculas); redondeo al par y precedencia aritmética; `1,2,3 -eq 2`, `1 -eq '1.0'`, `-ieq`,
`-like`/`-match`; `..` con caracteres desde PS 6; `` `e `` y `` `u{x} `` desde PS 6; flujos 1-6 y sus
versiones; redirección nativa en 7.4; `[ordered]` desde 3.0 y su posición; sintaxis simplificada de
`Where-Object` desde 3.0; `-Depth` desde 5.0; `switch` (default único, Exact por defecto, `-File`,
`$Matches` con `-Regex`); `$HOME`/`USERPROFILE`, `$Using:`, `$Private:`, variables de entorno
(cadenas, herencia, mayúsculas en Linux); `Move-Item` (falla si existe, `-Force`), `Rename-Item`,
`Remove-Item` y confirmación, `New-PSDrive -Persist` sólo remotas.

### Hallazgos

| # | Gravedad | Error | Pasaje | Qué dice la fuente | Propuesta |
|---|---|---|---|---|---|
| G1 | Grave | 6 (salvedad omitida) + 9 | Ep. 11 «Crear, copiar, mover, renombrar»: «*Copy-Item* falla si el destino existe, salvo con `-Force`, que **«funciona aunque el destino sea de solo lectura»**» | Lo dice la página «Trabajar con archivos y carpetas» (**«Si el archivo de destino ya existe, se produce un error en el intento de copia. Para sobrescribir un destino preexistente, use el parámetro Force»**). Pero la ayuda del propio cmdlet `Copy-Item` lo contradice en dos ejemplos sin `-Force`: ej. 2, **«sobrescribiendo los archivos con el mismo nombre»**; ej. 12, **«Observe que los archivos con el mismo nombre se sobrescriben en la carpeta de destino.»** Y define `-Force` como **«copia elementos que no se pueden cambiar de otro modo, como copiar en un archivo o alias de solo lectura»**. El tema da como regla la versión de la guía y calla la del cmdlet. Una pregunta de examen («¿qué pasa si el destino existe?») se contesta mal con el tema (pregunta 15) | Declarar la contradicción como se hizo con la directiva por defecto: la ayuda del cmdlet muestra que sobrescribe ficheros con el mismo nombre; `-Force` hace falta para destinos de sólo lectura; la guía de muestras dice que falla. Ajustar el punto «Puntos que un tribunal…» no hace falta (el script no copia) |
| M1 | Menor | 6 (salvedad omitida) | Ep. 4 «Especiales», fila «`&` al final» (operador en segundo plano), en la tabla general, mientras el párrafo siguiente aparta «Los de PowerShell 7, que no existen en Windows PowerShell 5.1» | `about_Operators?view=powershell-5.1` (leída el 06-10-2026) no tiene el operador en segundo plano: sólo el de llamada `&`. La página de 7 no le pone versión, por eso la redacción quitó la novedad; pero la de 5.1 sí permite afirmar que en 5.1 no existe | Añadir en la fila «(no existe en Windows PowerShell 5.1)» con la fuente `about_Operators` 5.1 en Trazabilidad, o pasarlo a la lista de los de PowerShell 7 diciendo sólo que 5.1 no lo tiene |

Sin hallazgo en: cita cruzada (1; las remisiones a epígrafes, comprobadas), ley por reglamento (2),
recuentos (3), «podrá»/«deberá» (4), siglas (5), redacción derogada (7), artículo mal (8).

Observación sin hallazgo: `about_Arithmetic_Operators` dice literalmente **«Cuando el cociente de una
operación de división es un entero, PowerShell redondea…»** (traducción errónea de *cast to an
integer*); la paráfrasis del tema («al convertir a entero») es la lectura correcta y no se cita.

## Lente 2 · Cobertura

Las once rúbricas del enunciado tienen epígrafe propio y en su orden. Quince preguntas en
`29-T07-preguntas.md`: **13 enteras, 1 a medias (15), 1 no (11)**; además una variante de la 7 a
medias (M1) y una complementaria sin respuesta.

| # | Laguna | Rúbrica | Propuesta |
|---|---|---|---|
| L1 | Métodos de cadena de .NET (`ToUpper()`, `ToLower()`, `Trim()`, `Substring()`, `Split()`, `Contains()`, `StartsWith()`, `IndexOf()`): el tema sólo da `Replace()` y remite a `Get-Member`. Se quitaron porque la página de `System.String` dio error 429 | Strings | Ampliar la fila «Otros métodos» de «Operaciones con cadenas» leyendo `System.String` en learn.microsoft.com/es-es/dotnet/api/system.string (o los ejemplos de `about_Methods` y de la guía de sustitución en cadenas) |
| L2 | Inversos y vecinos de los cmdlets de fichero: `Import-Csv` (el tema da `Export-Csv`), `Get-Item`, `Clear-Content` | Gestión de ficheros | Añadir dos o tres filas a la tabla de «Los cmdlets de elementos», con su ayuda en Microsoft Learn |

## Recuento

Graves: 1 (G1). Menores: 1 (M1). Lagunas: 2 (L1, L2).

## Ficheros tocados

`informes/canal-sur-especificos/29-T07-preguntas.md` y este informe. Descarga nueva
(`about_Operators` 5.1) leída en línea, sin guardar en el repositorio. El tema no se ha tocado.
