# Puesto 29 · Tema 7 · Preguntas de refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/07-automatizacion-y-administracion-mediante-powershell.md`.

Quince preguntas tipo test de cuatro opciones, repartidas por las rúbricas del enunciado (entorno,
ayuda, variables, operadores, arrays, strings, metacaracteres, tuberías, direccionamiento,
estructuras de control, gestión de ficheros), de teoría y de aplicación práctica. Distintas de las
diez de la redacción. Contestadas **sólo con el tema**: entera / a medias / no.

1. **(Entorno, aplicación práctica)** En un equipo con `Get-ExecutionPolicy -List` que muestra
   MachinePolicy Undefined, UserPolicy Undefined, Process Undefined, CurrentUser RemoteSigned y
   LocalMachine AllSigned, la directiva efectiva es:
   a) AllSigned · b) RemoteSigned · c) Restricted · d) Undefined.
   **b.** Ep. 1 «La directiva de ejecución», ejemplo de Microsoft y orden de prioridad. **Entera.**

2. **(Entorno)** ¿Dónde guarda Windows PowerShell 5.1 la directiva fijada con `-Scope Process`?
   a) En `HKLM:\Software\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell` · b) En
   `powershell.config.json` · c) En la variable de entorno `$Env:PSExecutionPolicyPreference`, y se
   pierde al cerrar la sesión · d) En el perfil del usuario.
   **c.** Ep. 1, tabla de ámbitos. **Entera.**

3. **(Ayuda)** ¿Qué devuelve `help pr*cess`?
   a) Los comandos con *process* en el nombre · b) Nada: con el comodín dentro sólo busca nombres
   que coincidan y no hace búsqueda de texto completo · c) Un error de parámetro · d) 78 resultados.
   **b.** Ep. 2 «Buscar comandos con la ayuda». **Entera.**

4. **(Ayuda)** ¿Qué afirmación sobre `Get-Command` es correcta?
   a) Obtiene sus datos de los temas de ayuda · b) Sin parámetros incluye los ejecutables del PATH ·
   c) Con el nombre exacto de un comando importa el módulo que lo contiene · d) No admite comodines
   en `-Noun`.
   **c.** Ep. 2 «Get-Command». **Entera.**

5. **(Variables)** Se quiere que una variable creada dentro de un script siga existiendo en la
   sesión al terminar el script. ¿Qué se escribe?
   a) `$Private:Equipos = …` · b) `$Using:Equipos = …` · c) `$Global:Equipos = …` ·
   d) `$Script:Equipos = …`.
   **c.** Ep. 3 «Ámbito» (`$Global:Computers`; *dot sourcing* como alternativa). **Entera.**

6. **(Operadores)** ¿Qué devuelve `1,2,3 -eq 2`?
   a) `True` · b) `False` · c) `2` · d) Un error.
   **c.** Ep. 4 «De comparación», regla 2. **Entera.**

7. **(Operadores, versiones)** ¿Cuál de estos operadores funciona en Windows PowerShell 5.1?
   a) El ternario `? :` · b) `??` · c) `&&` · d) El operador de llamada `&` delante de una ruta
   entre comillas.
   **d.** Ep. 4: el tema lista ternario, `??` y `&&`/`||` como «de PowerShell 7, que no existen en
   Windows PowerShell 5.1»; el `&` de llamada está en ep. 1 y en la tabla de especiales. **Entera.**
   Variante que falla: si la opción correcta fuera «el `&` al final de una canalización (segundo
   plano)», el tema llevaría a error: lo pone en la tabla general de especiales, fuera de la lista
   de PowerShell 7, y la página `about_Operators` de 5.1 no lo tiene (hallazgo M1). **A medias.**

8. **(Arrays)** En un script, `$p = Get-Process Notepad` y luego `$p.Count`. ¿Qué garantiza que
   `Count` y el índice funcionen aunque haya cero o un proceso?
   a) `[ordered]` · b) Escribir `$p = @(Get-Process Notepad)` · c) `$p += …` · d) `-as [array]`.
   **b.** Ep. 5 «Crear una matriz» y ep. 11 (script práctico). **Entera.**

9. **(Arrays y tablas hash)** ¿Qué ocurre con `$h = [ordered]@{a=1}` frente a
   `[ordered]$h = @{a=1}`?
   a) Los dos crean un diccionario ordenado · b) El primero crea un diccionario ordenado; el segundo
   da error · c) El segundo crea una tabla ordenada y el primero no · d) Los dos dan error.
   **b.** Ep. 5 «Tablas hash». **Entera.**

10. **(Strings)** Con `$d = Get-Item C:\Windows`, ¿qué orden muestra la fecha de creación dentro del
    texto?
    a) `"Creada: $d.CreationTime"` · b) `'Creada: $($d.CreationTime)'` ·
    c) `"Creada: $($d.CreationTime)"` · d) `"Creada: ${d.CreationTime}"`.
    **c.** Ep. 6 «Comillas dobles y comillas simples». **Entera.**

11. **(Strings)** ¿Qué método de .NET devuelve la cadena en mayúsculas (`'abc'` → `'ABC'`)?
    a) `.ToUpper()` · b) `.Upper()` · c) `.Capitalize()` · d) `.UCase()`.
    **a.** El tema sólo remite a `Get-Member -MemberType Method` sobre una cadena y da `Replace()`;
    los métodos de `System.String` (`ToUpper()`, `ToLower()`, `Trim()`, `Substring()`, `Split()`,
    `Contains()`, `StartsWith()`) se quitaron por no haberse leído su página. **No** (laguna L1).

12. **(Metacaracteres)** En una expresión regular, ¿qué patrón equivale al comodín `*` de un nombre
    de fichero?
    a) `*` · b) `.*` · c) `?` · d) `\*`.
    **b.** Ep. 7, último párrafo de «Expresiones regulares». **Entera.**

13. **(Tuberías y direccionamiento, aplicación práctica)** Se quiere guardar en `servicios.txt` la
    lista de servicios y, a la vez, seguir filtrándola en la canalización. ¿Qué cmdlet?
    a) `Out-File` · b) `Tee-Object` · c) `Export-Csv` · d) `Set-Content`.
    **b.** Ep. 8 (tabla) y ep. 9 «Out-File y Tee-Object». **Entera.**

14. **(Estructuras de control)** En un `for`, al ejecutarse `continue`:
    a) Se sale del bucle · b) Se ejecuta la parte `Repeat` y después se evalúa la condición ·
    c) Se vuelve a ejecutar `Init` · d) Se salta a `finally`.
    **b.** Ep. 10 «break y continue». **Entera.**

15. **(Gestión de ficheros, aplicación práctica)** `Copy-Item -Path .\a.txt -Destination .\b.txt`,
    cuando `b.txt` ya existe y no es de sólo lectura:
    a) Falla siempre si no se añade `-Force` · b) Sobrescribe `b.txt` · c) Crea `b (1).txt` ·
    d) Pide confirmación.
    **b** según la ayuda del cmdlet `Copy-Item` (ejemplos 2 y 12: **«sobrescribiendo los archivos con
    el mismo nombre»**, **«los archivos con el mismo nombre se sobrescriben en la carpeta de
    destino»**, sin `-Force`); el tema, siguiendo sólo la página «Trabajar con archivos y carpetas»,
    lleva a la **a**. **A medias / mal** (hallazgo G1).

    Pregunta complementaria (no cuenta): «¿Qué cmdlet lee un CSV y devuelve objetos?» —
    `Import-Csv`. El tema da `Export-Csv` pero no su inverso, ni `Get-Item` ni `Clear-Content`.
    **No** (laguna L2).

## Recuento

| Resultado | Preguntas |
|---|---|
| Entera | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14 (13) |
| A medias | 15 (y la variante de la 7) |
| No | 11 (y la complementaria de la 15) |
