# Puesto 29 · Tema 7 · Verificación (fase 3)

Fecha: 05-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/07-automatizacion-y-administracion-mediante-powershell.md`.
Copia previa en el directorio temporal de la sesión (`29t07-antes-verif.md`).

## Copiado del común / de RTVE sin cambios

El informe de redacción no lista nada en ninguno de los dos apartados (el tema 7 no invoca normas del
común y RTVE no tiene PowerShell). No había nada que comprobar por literalidad: se verificó el tema entero.

## Fuentes y fecha de lectura

Todas releídas el 05-10-2026 sobre las descargas de Microsoft Learn es-es que hizo la redacción ese
mismo día (las 70 páginas que lista su informe: `about_*`, ayuda de los cmdlets, PS101, ciclo de vida,
instalación, diferencias 5.1/7, ficheros, sustitución en cadenas, VS Code). Dos descargas nuevas:
`about_Numeric_Literals` (sufijos `kb`–`pb`, que no tenían fuente) y una segunda descarga de
`about_Foreach` (para buscar la regla de la instrucción frente al alias: no figura en la página).

## Método

1. Literalidad: script que normaliza espacios y busca cada cita en negrita «…» en el texto de las
   fuentes: **364 citas, 0 sin encontrar** (363 de la redacción y una nueva).
2. Prosa en redonda: cada dato, versión, alias, ejemplo atribuido y paráfrasis, releído en su pasaje
   con los nueve errores delante (tablas de versiones y fechas, directivas y ámbitos, parámetros de
   `Get-Help`, búsqueda 12/78, operadores y precedencia, matrices, comillas, comodines, secuencias de
   escape, regex, flujos 1-6 y versiones, `switch`, bucles, `try/catch`, alias y parámetros de los
   cmdlets de ficheros, ejemplo de Archivos de programa, `New-PSDrive -Persist`).
3. Script de aplicación práctica, revisado línea a línea (no hay `pwsh` en el entorno): sintaxis y
   lógica correctas (`@( )` con tubería en varias líneas, `-ErrorAction Stop` dentro de `try`, `$_` en
   `catch`, `>>`, `exit 1`). Un matiz añadido sobre `-WhatIf` (hallazgo 12).

## Hallazgos y correcciones (14)

| # | Error | Pasaje | Corrección |
|---|---|---|---|
| 1 | 9 | § 1 directiva: «el doble clic o la ejecución de un `.ps1` falla hasta que se cambia la directiva» | El doble clic no ejecuta nunca un script (el propio tema cita la regla en *Scripts*). Ahora: ejecutarlo escribiendo su ruta falla; el doble clic no lo ejecuta con ninguna directiva |
| 2 | 9 | § 2: «En la ayuda en inglés que instala `Update-Help`, `-Detailed`, `-Examples` y `-Full` advierten…» | La advertencia está en la ayuda en línea de `Get-Help` en castellano. Atribución corregida |
| 3 | 6 | § 2 tabla, salida sin parámetros | PS101 cap. 2 lista también COMENTARIOS. Añadido |
| 4 | 6 + 1 | § 3 `$Matches`: «lo que encontró el último `-match` (epígrafe 7)» | `about_Automatic_Variables`: no se vacía si el siguiente `-match` falla. Añadida la salvedad; la remisión iba al ep. 7, que no trata `$Matches`: ahora ep. 4 |
| 5 | 6 | § 4: «al convertir a entero redondea al par más cercano» | `about_Arithmetic_Operators`: redondea al entero más cercano y sólo con ,5 al par. Corregido |
| 6 | 9 | § 4: sufijos `100KB`, `1mb`, `512MB` sin fuente | Confirmados en `about_Numeric_Literals`: `kb` a `pb`, potencias de 1024, en mayúsculas o minúsculas. Ampliado y añadida la fuente en Trazabilidad |
| 7 | 6 | § 6: `"{0:N0}" -f 8175133` da `8,175,133` | Es la salida del ejemplo de Microsoft; dicho así (el separador no es universal) |
| 8 | 9 | § 8 tabla: `Measure-Object` «—» | La ayuda da el alias `measure` (todas las plataformas). Corregido |
| 9 | 9 | § 8 tabla: `Group-Object`, `Format-Table`, `Export-Csv` «—» | Alias `group`, `ft`, `epcsv`. Corregido; `Format-List` no se leyó (429 en la redacción) y se dice |
| 10 | 9 | § 8 tabla: `Out-File`, `Tee-Object` «—» | `Tee-Object` tiene `tee` (sólo Windows). Corregido; `Out-File` sin alias en su ayuda |
| 11 | 9 | § 11 tabla: `Select-String` «—» | Alias `sls` (todas las plataformas). Corregido |
| 12 | 6 | § 10 `while`: «# 1, 2, 3» | `about_While`: sólo si `$val` no existe o vale 0. Añadido |
| 13 | 9 | § 10 `foreach`: regla de la posición para distinguir instrucción y alias | No está en la página (leída dos veces); la redacción ya la declaraba oficio. Se mantiene como oficio y se añade lo que sí dice `ForEach-Object`: **«no se puede canalizar la entrada»** a la instrucción |
| 14 | 9 | Trazabilidad: «Los demás ejemplos de código son de la documentación» | Falso: hay ejemplos breves propios (`12 -is [int]`, `(1..10).Where(…)`, `Get-Process notepad && Stop-Process…`, órdenes sobre `C:\Datos` y `app.log`, etc.). Reescrito: son de Microsoft los que el tema le atribuye |

Además, en la aplicación práctica: con `-WhatIf` no se borra nada pero el registro anotaría «Borrado»;
añadido (matiz de oficio, no error).

Comprobado y sin cambio: la contradicción de la página de PowerShell 7 sobre la directiva por defecto
(la redacción la describe bien; la página dice además «RemoteSigned para clientes y servidores
Windows» bajo *Default*, coherente con lo declarado); `Copy-Item` «falla si el destino existe, salvo
con `-Force`» (es lo que dice la página «Trabajar con archivos y carpetas»; se mantiene porque manda
la fuente); `$ErrorActionPreference` por defecto Continue (`about_Preference_Variables`, ejemplo de esa variable).

Sin hallazgo en: ley por reglamento (2), recuentos (3: 12/78 resultados, seis conjuntos de parámetros,
cinco vías de instalación, cuatro perfiles, flujos 1-6, todo cuadra), «podrá»/«deberá» (4), siglas (5),
redacción derogada (7: versiones y fechas de la tabla de ciclo de vida a 05-10-2026), artículo mal (8).

## Lentes

Tema técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`.
`refutar_prosa.py`: 0 hallazgos. `indice.py`: 15.269 palabras, 77 epígrafes (la ficha dice 15.000
aproximadamente: se mantiene). Antecedentes de los pasajes cambiados releídos («ese cmdlet» →
`ForEach-Object`; «la instrucción» → `foreach`; remisión de `$Matches` → ep. 4, donde está).

## Ficheros tocados

El tema y este informe. Descargas `about_Numeric_Literals.txt` y `about_Foreach_b.txt` y copia previa,
en el directorio temporal de la sesión (fuera del repositorio).
