# Tema 7 del específico de Operador/a Informático · Automatización y administración mediante PowerShell

**Siglas**: RTVA, CSRTV; CLR; LTS; WMF; ISE; VS Code; MSI, MSIX; UAC; UTF-8, BOM; regex; ZIP.

Esqueleto para repasar, no resumen: cada línea es un dato del tema; la explicación está en el tema.

<!-- indice -->
<!-- /indice -->

## 1. El entorno PowerShell
- overview: multiplataforma = shell + scripting + configuración (DSC); acepta y devuelve objetos .NET (CLR), no texto
- lifecycle: 5.1 = .NET Framework 4.5, agosto 2016, WMF 5.1, componente de Windows (su ciclo), preinstalado, `powershell.exe`; no se admite <5.1
- diferencias: 7 = código abierto, .NET Core (desde 6.0), en paralelo, `pwsh.exe`; LTS = LTS de .NET (sólo seguridad y mantenimiento); estable = entre LTS, ≈6 meses tras la siguiente LTS
- Tabla 05-10-2026: 7.6 LTS, 18-03-2026, fin 14-11-2028, .NET 10.0; 7.5 estable, 23-01-2025, fin 10-11-2026, .NET 9.0; 7.4 LTS anterior, 16-11-2023, fin 10-11-2026, .NET 8.0; 5.1 el de Windows
- Versión: `$PSVersionTable`; ya no en 7: ISE, `Microsoft.PowerShell.LocalAccounts`, `PSScheduledJob`, `PSWorkflow`
- Instalación 7: WinGet (recomendada en clientes); MSI (empresa, servidores); MSIX (casual, limitaciones); ZIP (varias versiones, Server Core, IoT, Arm); herramienta global .NET; winget en Windows 11 y Server 2025, no Server 2022; `C:\Program Files\PowerShell\7` = `$PSHOME`
- ps101: no participa en UAC; «Ejecutar como administrador» («Administrador: Windows PowerShell»), sólo si es necesario
- Cmdlet = Verbo-Sustantivo singular; «comando» = cmdlet, función o alias; `-WhatIf` (no ejecuta), `-Confirm` (pide confirmación)
- about_Aliases: `cd`, `chdir` = Set-Location; `ls`, `dir` = Get-ChildItem; sólo en la sesión (perfil); no alias a comando+parámetros (función)
- about_Scripts: `.ps1`; con ruta (`.\`); ni doble clic ni nombre sin ruta; `param` primera instrucción (salvo comentarios, `#Requires`); `#`, `<# #>`; `&` llamada; `. ` *dot sourcing* = ámbito actual
- about_Providers: Alias:; Cert:; Env:; FileSystem (C:); Function:; Registry (HKLM:, HKCU:); Variable:; WSMan:; Certificate, Registry, WSMan sólo Windows
- about_Profiles: no se crea solo; 4 (7, Windows): `$PSHOME\Profile.ps1`; `$PSHOME\Microsoft.PowerShell_profile.ps1`; `$HOME\Documents\PowerShell\Profile.ps1`; `$HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`; en ese orden, CurrentUserCurrentHost último (prevalece, oficio)
- about_Execution_Policies: defensa en profundidad, no límite de seguridad; sólo Windows (Linux/macOS Unrestricted, fija)
- Restricted: sin scripts, perfiles ni módulos de script; AllSigned: todo firmado; RemoteSigned: firma sólo en lo descargado (flujo «procedente de Internet»; `Unblock-File`); Unrestricted: avisa si no es intranet; Bypass: sin avisos; Undefined; Default
- Por defecto (5.1): Restricted en clientes, RemoteSigned en Server (todo Undefined igual); en 7 la página se contradice; el tema da 5.1
- Ámbitos por prioridad: MachinePolicy; UserPolicy (GPO); Process (`$Env:PSExecutionPolicyPreference`); CurrentUser; LocalMachine (defecto; `HKLM:\…`); 7 usa `powershell.config.json`
- GPO invalida todo: «Activar ejecución de scripts», `Administrative Templates\Windows Components\Windows PowerShell`; deshabilitada = Restricted; habilitada: Unrestricted, RemoteSigned, AllSigned
- `Get-ExecutionPolicy [-List]`; `Set-ExecutionPolicy RemoteSigned [-Scope CurrentUser]` (defecto LocalMachine, administrador, efecto inmediato); CurrentUser RemoteSigned + LocalMachine AllSigned → RemoteSigned

## 2. La ayuda
- ps101: `Get-Help` aprende comandos; `Get-Command` los descubre; `-Full`; `-Online` (no en *about*); requieren ayuda instalada; `-Full` y `-Detailed` incompatibles (conjuntos de parámetros); `help` pagina con `more.com` (ISE no)
- Búsqueda: comodín en nombres; si nada, texto completo; `help pr*cess` nada; `help -process` error; una sola coincidencia → contenido
- `about_*`: `help about_*`; ayuda no preinstalada desde 3.0; `Update-Help -Force`; 5.1 como administrador; sin Internet `Save-Help` + `-SourcePath`
- `Get-Command`: cmdlets, alias, funciones, filtros, scripts, aplicaciones; sin parámetros = cmdlets, funciones, alias; `-Name -Noun -Verb` con comodines
- `Get-Member`: propiedades y métodos, alfabético, métodos primero; `TypeName:`; `-MemberType Method`; método siempre con paréntesis: `(Get-Process notepad).Kill()`

## 3. Variables
- about_Variables: `$`; sin distinguir mayúsculas; sin declarar, `$null`; alfanuméricos y `_`; espacios o guion: `${save-items}`; duran la sesión (perfil)
- Clases: usuario; automáticas (no se cambian, `$PSHOME`); de preferencia (se cambian, `$MaximumHistoryCount`)
- vaciar: `Clear-Variable` o `$null`; eliminar: `Remove-Variable` o `Remove-Item Variable:\X`
- Tipado flexible (`GetType()`, `Get-Member`); `[int]$number = 8`: `"12345"` convierte, `"Hello"` error; `[string]$words = "Hello"; $words = 2; $words += 10` → `210`
- Sin comillas o dobles: valor; simples: nombre literal
- Ámbito: por defecto donde se crea (función, script salvo *dot sourcing*); visible en hijos; sólo se cambia donde se creó; Global; Script; Local
- `$_` = `$PSItem`; `$?` True/False; `$LASTEXITCODE`; `$Error` (`$Error[0]` último); `$null`; `$true/$false` ("false" es verdadera); `$Matches` (no se vacía si el siguiente `-match` falla); `$PSHOME`; `$PROFILE`; `$PSVersionTable` (hash, sólo lectura)
- Entorno: `$Env:Foo = 'x'`, `Get-ChildItem Env:`; siempre cadenas; heredan los hijos; cambio sólo en la sesión; máquina/usuario: `System.Environment`; Windows no distingue mayúsculas, Linux/macOS sí

## 4. Operadores
- about_Operators: comparación y lógicos con guion (`>` `<` son redirección)
- `+` (suma, concatena cadenas, matrices, hash); `*` (copia: `"!" * 3`); `/` no trunca; `%` resto
- Orden: paréntesis, signo, `* / %`, `+ -`, bit a bit
- Sufijos `kb mb gb tb pb` (1024); `= += -= *= /= %=`; `++` `--`
- `-eq -ne -gt -ge -lt -le`; `-like` (comodín); `-match` (regex); `-replace` (regex); `-contains`; `-in` (desde 3, inverso); `-is/-isnot`; negados `-not…`
- R1: sin mayúsculas; `-c…` distingue, `-i…` expreso; R2: escalar → booleano, colección → elementos que coinciden, contención y tipo siempre booleano; R3: derecha al tipo de la izquierda (), `$null` a la izquierda; R4: `if (36 > 42)` → false y crea fichero `42` con `36`
- `-like` comodín, cadena entera; `-match` regex, parcial: `'PowerShell' -match 'shell'` V, `-like 'shell'` F, `-like '*shell'` V; `-replace <regex>, <sustituto>`
- `-and -or -xor -not !`; cortocircuito; misma prioridad, izquierda a derecha; falsos: `''`, `$null`, 0; verdaderas: cadenas no vacías
- `-split` (defecto espacio en blanco; delimitador regex); `-join` (defecto `""`): `-join ("a","b","c")` = `abc`; `-join "a","b","c"` no une (unario > coma); `-is`, `-isnot`, `-as`
- Especiales: `( )`; `$( )`; `@( )` siempre matriz; `@{ }` hash; `&` llamada; `&` final = trabajo (`Start-Job`; no en 5.1); `[ ]` conversión/índice; `,` crea matriz (`,1`); `..` (`'a'..'e'` desde 6)
- Sólo 7: ternario `? :` (7.0; comando entre paréntesis); `??` y `??=`; `&&` (derecha si la izquierda fue bien) y `||` (si falló)

## 5. Arrays (matrices) y tablas hash
- about_Arrays: `$A = 22,5,10`; `$B = ,7`; `5..8`; `@()`; `@(Get-Process Notepad)` siempre matriz; sin tipo `System.Object[]`
- Índice desde 0; `$a[-1]` último; `$a[0,2+4..6]` = 0,2,4,5,6; `$a[0..-2]` = primero, último y penúltimo (error común)
- `Count` (cualquier colección) (cadena = caracteres); tamaño fijo: `+=` crea nueva (rendimiento); no se quita: nueva con los elegidos; `+` une
- `ForEach()`; `$a -gt 5`; multidimensional `$rank2[1,1]`
- Hash: `@{ Number = 1; Shape = "Square" }`; `;` o salto; orden no determinista
- Son hash `$PSVersionTable`, `$Matches`; *splatting* = `@variable`

## 6. Strings (cadenas)
- Dobles = expandible: `"$(2+3)"`; sólo variables básicas, índice o miembro → `$( )`; `"${test}ter"` = `Better`
- Simples = literal; regex con `$` entre simples
- Dobles dentro: cadena entre simples o dobladas; simples dentro: entre dobles o `'don''t'`; `` `$ `` literal; escape = acento grave (la doc dice «barra diagonal inversa» pero el ejemplo usa `` `" ``; `\` sólo en regex); «No use comillas inteligentes»
- *Here* («cadenas aquí»): `@" "@` expande, `@' '@` literal; abre con marca + nueva línea; cierra nueva línea + marca; varias líneas
- `-replace` (regex) o `Replace()` (literal)
- System.String (.NET 9.0): `ToUpper()`; `ToLower()`; `Trim()` (+`TrimStart`, `TrimEnd`); `Split()`; `Contains()`; `StartsWith()/EndsWith()`; `IndexOf()` (base 0); `Replace()`; devuelven nueva cadena (asignar); `Contains`, `Replace`, `Split` ordinal (distinguen mayúsculas), operadores PowerShell no; concatenar crea cadena nueva (`System.Text.StringBuilder`)

## 7. Metacaracteres
- about_Wildcards: no distinguen mayúsculas; `*` cero o más; `?` cadenas un carácter, ficheros cero o uno; `[a-l]`; `[bc]`; `` `* `` literal; corchetes en nombre → `-LiteralPath`
- about_Special_Characters: grave; distinguen mayúsculas; sólo en dobles: `` `0 `` nulo (≠ `$null`); `` `a `` alerta; `` `b `` retroceso; `` `e `` escape (6); `` `f `` avance de página; `` `n ``; `` `r ``; `` `t `` tabulación; `` `u{x} `` Unicode (6); `` `v `` tabulación vertical; `--` resto = argumentos; `--%` no analiza
- Regex (motor .NET; sin mayúsculas): `.` salvo `\n`; `[iou]`/`[^iou]`; `[0-9]`; `\d/\D`; `\w` (`[a-zA-Z_0-9]`)/`\W`; `\s/\S`; `*` 0+; `+` 1+; `?` 0 o 1; `{n}` `{n,}` `{n,m}`; `^` inicio `$` final; `\` escape; reservados `[().\^$|?*+{`; `[regex]::Escape()`
- Comodín `*` = cualquier cosa, regex `*` = anterior 0+ (`.*`); comodín `?` un carácter, regex `?` opcional

## 8. Tuberías
- about_Pipelines: `|`; izquierda a derecha; salida según se genera; objetos: `Get-Process notepad | Stop-Process`
- Uno a uno por tubería; por parámetro, un objeto matriz; hash y cadenas no se enumeran (`GetEnumerator()`); `$_`/`$PSItem`
- ByValue: tipo .NET esperado o convertible; ByPropertyName: propiedad con el nombre del parámetro; `Start-Service`: `InputObject` (servicios), `Name` (cadenas o propiedad `Name`); no se fuerza el enlace
- `Where-Object` (`?`, `where`); `ForEach-Object` (`%`, `foreach`); `Select-Object` (`select`; `-Property -First -Last -Unique`); `Sort-Object` (`sort` sólo Windows); `Format-Table` (`ft`); `Export-Csv` (`epcsv`); `Out-File`, `Tee-Object` (`tee` sólo Windows)
- Filtrar a la izquierda (`Get-Service -Name w32time`); el orden cuenta (`Select-Object` quita propiedades); no formatear antes de `Export-Csv`

## 9. Direccionamiento (redirección de la salida)
- about_Redirection: flujos 1 Éxito `Write-Output` (2.0); 2 Error `Write-Error` (2.0); 3 Advertencia `Write-Warning` (3.0); 4 Detallado `Write-Verbose` (3.0); 5 Depuración `Write-Debug` (3.0); 6 Información `Write-Information`, `Write-Host` (5.0); `*` todos (3.0); Progress no redirige
- `>`/`n>` sobrescribe; `>>`/`n>>` añade; `n>&1` al éxito; `*>` todos; `>` = `1>`; sólo se redirige otros flujos al de Éxito; descartar `6> $null`
- `>` ≡ `Out-File` sin parámetros; `Tee-Object`: a fichero o variable y sigue; `Out-File`: `-Append`, `-NoClobber` (defecto sobrescribe), `-Encoding`, `-Force`, `-Width`
- 7: UTF8NoBOM; Out-File guarda vista de pantalla; datos → `Export-Csv`; 7.4: stdout nativo conserva bytes

## 10. Estructuras de control
- Palabra clave + condición entre paréntesis + bloque entre llaves; condición a lógico
- `if/elseif/else`: primer verdadero y sale; muchos `elseif` → `switch`
- `switch (3) { … 3{"It's three."} … 3{"Three again."} }` → ambas líneas (prueba todas); `break` sale; `continue` al valor siguiente; convierte a cadenas; colección: cada elemento (`$_`); `default` único = `else`; exacto y sin mayúsculas
- `for (<Init>; <Condition>; <Repeat>)`: Init una vez; Condition antes de cada vuelta; Repeat al final
- `foreach ($file in Get-ChildItem) {…}`: crea la variable; sin canalización; instrucción (inicio) ≠ alias de `ForEach-Object` (tras `|`)
- `while`: condición antes, puede no ejecutarse; `do {} while (c)` repite si verdadera / `do {} until (c)` si falsa; siempre una vez
- `break` sale; `continue` vuelta siguiente (en `for` ejecuta Repeat, evalúa condición); etiqueta `:myLabel while (…) { break myLabel }`
- `try {} catch [<tipo>] {} finally {}`: al menos `catch` o `finally`; `catch` sin tipo = todos; `$_`/`$PSItem` = `ErrorRecord`; `finally` siempre
- Sólo errores de terminación; resto: `$ErrorActionPreference = 'Stop'` o `-ErrorAction Stop` (defecto `Continue`); `exit` 0 por defecto, ≠0 error, en `$LASTEXITCODE`

## 11. Gestión de ficheros
- Cmdlets Item y Content, valen para todo proveedor
- `Get-ChildItem` (`dir`, `gci` / `ls`); `Get-Item` (`gi`); `Set-Location` (`cd`, `chdir`, `sl`); `New-Item` (`ni`); `Copy-Item` (`copy`, `cpi` / `cp`); `Move-Item` (`mi`, `move` / `mv`); `Rename-Item` (`ren`, `rni`); `Remove-Item` (`del`, `erase`, `rd`, `ri` / `rm`); `Test-Path`; `Get-Content` (`gc`, `type` / `cat`); `Set-Content` (reemplaza); `Add-Content` (`ac`); `Clear-Content` (`clc`); `Select-String` (`sls`; como grep, findstr.exe)
- `Get-ChildItem`: `-Force` (ocultos, sistema); `-Recurse`; `-File`; `-Directory`; `-Filter` el más rápido (lo aplica el proveedor), `-Include`, `-Exclude`; fecha/tamaño → `Where-Object`
- `New-Item -ItemType Directory|File` necesario; `-Force` en carpeta existente no sobrescribe, en fichero sí
- `Copy-Item`: `-Recurse` para carpetas; destino existente: página de archivos y carpetas = error salvo `-Force`; ayuda del cmdlet (ejemplos 2, 12) = sobrescribe; `-Force` = destino de sólo lectura
- `Move-Item`: recursivo por defecto; ficheros entre unidades del mismo proveedor, directorios sólo en la misma unidad; destino existente falla salvo `-Force`
- `Rename-Item -NewName`: sólo nombre; no mueve ni reemplaza (→ `Move-Item`, `-Force`)
- `Remove-Item`: confirma si hay contenido; `-Recurse` sin preguntar; `-Force` (ocultos, sólo lectura)
- `Get-Content`: un objeto por línea (`.Length` = líneas); `-Tail 20` (alias `Last`)
- `Set-Content -Value`; `Add-Content -Value` (valor o tubería); `Export-Csv` (objetos); `Clear-Content` (`-Force` en sólo lectura)
- `Select-String`: regex; fichero, nº de línea y línea
- `Import-Csv`: columna = propiedad; primera fila nombres salvo `-Header`; lee lo de `Export-Csv`
- `New-PSDrive -Name P -Root $env:ProgramFiles -PSProvider FileSystem` (sólo sesión)
- Script de mantenimiento (propio, no ejecutado): `param`, `Test-Path`, `exit 1`, `@(Get-ChildItem … | Where-Object …)`, `foreach` + `try`/`catch` con `-ErrorAction Stop` y `>>`; `-WhatIf` no borra, pero el registro anotaría «Borrado»
