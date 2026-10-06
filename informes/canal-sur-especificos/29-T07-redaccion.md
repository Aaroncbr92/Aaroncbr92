# Puesto 29 · Tema 7 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real,
como en la investigación). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/07-automatizacion-y-administracion-mediante-powershell.md`.
Material: `29-investigacion-B-sistemas.md` (§ Tema 7). `AGRUPACION.tsv`: tema 7 «nuevo». Fila de
`informes/canal-sur-reuso/informatica.tsv`: «PowerShell no está desarrollado en ningún tema de RTVE»
(0 %). Todo el tema es nuevo.

## Avance (por epígrafes, guardados uno a uno)

1. Entorno PowerShell (qué es, 5.1 frente a 7, instalación, editores y elevación, cmdlets/alias/scripts,
   proveedores, perfil, directiva de ejecución).
2. Ayuda (`Get-Help`, búsqueda, *about*, `Update-Help`/`Save-Help`, `Get-Command`, `Get-Member`).
3. Variables (clases, creación y borrado, tipos, comillas, ámbito, automáticas, entorno).
4. Operadores (aritméticos, asignación, comparación, lógicos, split/join, tipo, especiales, los de PS 7).
5. Arrays y tablas hash.
6. Strings (comillas, escape, *here-strings*, operaciones).
7. Metacaracteres (comodines, secuencias de escape, expresiones regulares).
8. Tuberías (objetos, uno a uno, ByValue/ByPropertyName, cmdlets de utilidad, buenas prácticas).
9. Direccionamiento (flujos 1-6, `>`, `>>`, `n>&1`, `*>`, `Out-File`, `Tee-Object`, codificación).
10. Estructuras de control (`if`, `switch`, `for`, `foreach`, `while`, `do`, `break`/`continue`,
    `try/catch/finally`, `exit`).
11. Gestión de ficheros (cmdlets *Item* y *Content* con alias, parámetros, `Select-String`,
    `New-PSDrive`) y un script de aplicación práctica.

`indice.py`: 15.133 palabras (con bloques de código), 77 epígrafes. `refutar_prosa.py`: 0 hallazgos
(4 siglas sin presentar en la primera pasada —AWS, CMD, SQL, ZIP—, corregidas). Tema técnico sin
norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`. El tema no está en
`herramientas/portadas.tsv`, como los demás de Canal Sur: ficha escrita a mano.

## Fuentes releídas y fecha

La investigación cubría el tema pero dejaba huecos (Move/Rename/Set-Content, alias, directiva por
defecto en 5.1) y extractos sin cita. Se descargaron y leyeron, todas el **05-10-2026**, en Microsoft
Learn es-es: las 24 páginas que ya había bajado la investigación (about_* de variables, operadores,
arrays, comillas, comodines, caracteres especiales, regex, tuberías, redirección, estructuras de
control, directivas; PS101 caps. 2 y 4; ciclo de vida; diferencias 5.1/7; ficheros), y además
`about_Aliases`, `about_Split`, `about_Join`, `about_Break`, `about_Continue`, `about_Scripts`,
`about_Profiles`, `about_Scopes`, `about_Providers`, `about_Environment_Variables`,
`about_Preference_Variables`, `about_Try_Catch_Finally`, `about_Methods`, `about_Pipeline_Chain_Operators`,
`about_Splatting`, `about_Booleans`, `about_Operator_Precedence`, `about_Execution_Policies?view=powershell-5.1`,
PS101 cap. 1, la guía de sustitución en cadenas, la de instalación en Windows, la de VS Code, y la ayuda
de los cmdlets `Get-Command`, `Get-Member`, `Get-Help`, `Update-Help`, `Where-Object`, `ForEach-Object`,
`Select-Object`, `Sort-Object`, `Measure-Object`, `Group-Object`, `Tee-Object`, `Format-Table`,
`Out-File`, `Export-Csv`, `Select-String`, `Set-ExecutionPolicy`, `Get-ChildItem`, `New-Item`,
`Copy-Item`, `Move-Item`, `Rename-Item`, `Remove-Item`, `Test-Path`, `Get-Content`, `Set-Content`,
`Add-Content`, `Set-Location`. (Format-List y la clase `System.String` dieron error 429: no se leyeron
y el tema no cita nada de ellas.)

Comprobación de literalidad por script: las **363** citas en negrita «…» del tema se buscaron en el
texto normalizado de esas páginas; aparecen todas (dos se corrigieron durante la comprobación porque
la fuente trae «-andoperadores ,» y «while ,», erratas que ahora se citan con [sic]). Las negritas que
servían de rótulo sin ser cita pasaron a cursiva.

## Decisiones frente al material

- Directiva de ejecución por defecto: la investigación la dejó sin confirmar para 5.1. Leída la
  página `?view=powershell-5.1`: Restricted en clientes, RemoteSigned en servidores. La página de
  PowerShell 7 se contradice (RemoteSigned «predeterminada para equipos Windows» y, a la vez,
  Restricted como efectiva sin directiva); el tema da la de 5.1 y declara la contradicción. **Si el
  verificador lo ve de otro modo, manda la fuente.**
- Versiones: sólo 7.6 LTS / 7.5 estable / 7.4 LTS anterior / 5.1, sin el número de revisión (cambia
  cada mes), como pedía la investigación. Las versiones de .NET se leyeron de la tabla corrigiendo el
  desplazamiento de columnas del volcado (7.6 → .NET 10.0, 7.5 → 9.0, 7.4 → 8.0).
- Se quitó lo que no pude confirmar: el motivo de que ciertos alias sólo existan en Windows; los
  nombres de métodos de `System.String` (`ToUpper()`, etc.); el `&` en segundo plano como novedad de
  PS 7 (la página no da versión); `Where()` «desde PS 4» (sólo `ForEach()` lo dice).
- El traductor de Microsoft dice «barra diagonal inversa» para escapar comillas en `about_Quoting_Rules`
  mientras su ejemplo usa el acento grave: el tema lo señala.
- `$ErrorActionPreference`: la página dice en un ejemplo que el valor por defecto es Continue y en otro
  Inquire (errata); el tema da Continue.
- Script de aplicación práctica: propio, no ejecutado (no hay `pwsh` en el entorno); declarado en
  «Trazabilidad» como oficio. **El verificador debería revisarlo línea a línea.**

## Copiado del común

Ninguno. El tema 7 no invoca norma del temario común de Canal Sur.

## Copiado de RTVE sin cambios

Ninguno. RTVE no tiene PowerShell en ningún tema (fila 29/7 de `informatica.tsv`, 0 %).

## Ficheros tocados

- `temas/canal-sur-especificos/29-operador-a-informatico/07-automatizacion-y-administracion-mediante-powershell.md` (nuevo).
- `informes/canal-sur-especificos/29-T07-redaccion.md` (este informe).
- Volcados de fuentes en el *scratchpad* de la sesión (fuera del repositorio).

## Diez preguntas tipo test de comprobación

Escritas antes de entregar, repartidas por las rúbricas del enunciado (teoría y aplicación práctica),
y contestadas sólo con el tema.

1. **(Entorno)** El ejecutable de PowerShell 7 en Windows, que convive con Windows PowerShell 5.1, es:
   a) `powershell.exe` · b) `pwsh.exe` · c) `ps7.exe` · d) `powershell_ise.exe`.
   **b.** Tema, ep. 1 «Windows PowerShell 5.1 y PowerShell 7». Contestada entera.
2. **(Ayuda)** Un equipo sin Internet necesita la ayuda actualizada. Lo correcto es:
   a) `Update-Help -Force` en ese equipo · b) `Get-Help -Online` · c) `Save-Help` en un equipo con
   Internet y después `Update-Help -SourcePath` en el otro · d) `Get-Command -Syntax`.
   **c.** Ep. 2 «Actualizar la ayuda». Entera.
3. **(Variables)** Tras `[string]$words = 2` y `$words += 10`, `$words` vale:
   a) 12 · b) `210` · c) error de conversión · d) 2.
   **b.** Ep. 3 «Tipos». Entera.
4. **(Operadores, aplicación práctica)** Un script contiene `if (36 > 42) { "true" } else { "false" }`.
   ¿Qué ocurre? a) Muestra `true` · b) Error de sintaxis · c) Muestra `false` y crea un fichero llamado
   42 con el contenido 36 · d) Compara como texto.
   **c.** Ep. 4 «De comparación», regla 4. Entera.
5. **(Arrays)** Con `$a = 0..9`, `$a[0..-2]` devuelve:
   a) del 0 al 8 · b) 0, 9 y 8 · c) un error · d) 0 y 8.
   **b.** Ep. 5 «Leer elementos». Entera.
6. **(Strings)** Con `$i = 5`, ¿qué orden muestra `The value of $i is 5.`?
   a) `"The value of $i is $i."` · b) `'The value of $i is $i.'` · c) ``"The value of `$i is $i."`` ·
   d) ``'The value of `$i is $i.'``.
   **c.** Ep. 6 «Comillas dentro de una cadena y escape». Entera.
7. **(Metacaracteres)** En una comparación `-like`, el patrón `[bc]ook` coincide con:
   a) *hook* · b) *book* y *cook* · c) *took* · d) cualquier palabra terminada en *ook*.
   **b.** Ep. 7 «Comodines». Entera.
8. **(Direccionamiento)** Los mensajes de `Write-Warning` van al flujo número:
   a) 2 · b) 3 · c) 4 · d) 6.
   **b.** Ep. 9 «Los flujos de salida». Entera.
9. **(Estructuras de control)** ¿Qué muestra `switch (3) { 1 {"It's one."} 3 {"It's three."} 3 {"Three again."} }`?
   a) Sólo `It's three.` · b) `It's three.` y `Three again.` · c) Error por condición repetida ·
   d) Nada, falta `default`.
   **b.** Ep. 10 «switch». Entera.
10. **(Tuberías y gestión de ficheros, aplicación práctica)** ¿Qué hace
    `Get-ChildItem -Path C:\Logs -Filter *.log | Where-Object { $_.Length -gt 1MB } | Remove-Item -WhatIf`?
    a) Borra todos los .log de C:\Logs y subcarpetas · b) Muestra qué .log de más de 1 MB de C:\Logs
    (sin subcarpetas) se borrarían, sin borrarlos · c) Borra los .log de más de 1 MB pidiendo
    confirmación · d) Da error porque `Remove-Item` no acepta tubería.
    **b.** Ep. 8 (tubería, `$_`), ep. 4 (sufijo MB), ep. 11 (`-Filter`, `-Recurse`, `-WhatIf`).
    Entera.

Resultado: 10 de 10 contestadas enteras con el tema; no hizo falta ampliarlo. La rúbrica de entorno
lleva además la directiva de ejecución (pregunta probable no incluida aquí: «directiva efectiva en un
cliente Windows sin ninguna definida» → Restricted, ep. 1).
