# Puesto 29 · Tema 7 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/07-automatizacion-y-administracion-mediante-powershell.md`.
Entradas: `29-T07-refutacion.md` (G1, M1, L1, L2) y `29-T07-preguntas.md` (11 «no», 15 «a medias»).

## Fuentes releídas (todas descargadas de learn.microsoft.com/es-es el 06-10-2026)

| Página | Para |
|---|---|
| Ayuda de `Copy-Item` (view=powershell-7.5) | G1: ejemplos 2 y 12, parámetro `-Force` |
| «Trabajar con archivos y carpetas» (scripting/samples) | G1: «Si el archivo de destino ya existe, se produce un error…» |
| `about_Operators` view=powershell-5.1 y view=powershell-7.5 | M1 |
| `System.String` (dotnet/api, .NET 9.0) | L1 |
| Ayuda de `Import-Csv`, `Get-Item`, `Clear-Content` (7.5) | L2 |

## Comprobación y decisión

| # | ¿Confirmado en la fuente? | Aplicado |
|---|---|---|
| G1 | Sí. Las dos citas del cmdlet y la definición de `-Force` son literales; la página de muestras dice lo que el tema daba. Matiz: los ejemplos 2 y 12 muestran sobrescritura entre ficheros del mismo nombre dentro de la misma copia, no un destino ya existente antes de copiar; aun así es un fichero existente sobrescrito sin `-Force` | Se declara la contradicción con las tres citas y se dice qué comparten las dos fuentes (`-Force` para sólo lectura) |
| M1 | Sí. La 5.1 lista los especiales (agrupación, subexpresión, matriz, llamada, conversión, coma, *dot sourcing*, formato, índice, canalización, intervalo, miembro, estático); no hay operador en segundo plano. La 7.5 sí lo trae (línea «equivalente a Start-Job») | Nota en la fila de la tabla |
| L1 | Sí, laguna real (pregunta 11) | Ampliado: tabla nueva de métodos |
| L2 | Sí, laguna real (complementaria de la 15) | Ampliado: tres filas y un párrafo |

## Pasajes cambiados

1. **Ficha**, Extensión: «15.000» → «16.200 palabras aproximadamente».
2. **Ep. 4 «Especiales»**, fila «`&` al final»: se añade «No existe en Windows PowerShell 5.1: su
   `about_Operators` no lo recoge entre los especiales, sólo el `&` de llamada».
3. **Ep. 6 «Operaciones con cadenas»**: la fila «Otros métodos» remite a la tabla siguiente; tabla
   nueva con `ToUpper`, `ToLower`, `Trim` (y `TrimStart`/`TrimEnd`), `Substring`, `Split`,
   `Contains`, `StartsWith`/`EndsWith`, `IndexOf`, `Replace`, con la descripción literal de .NET y un
   ejemplo propio; párrafo con dos advertencias literales (los métodos devuelven cadena nueva;
   `Contains`, `Replace` y `Split` comparan en ordinal por defecto) y el contraste con `-split` y
   `-replace` (remite a epígrafes 4 y 7, comprobado que allí está la regla de la expresión regular).
4. **Ep. 11 «Los cmdlets de elementos»**: filas nuevas `Get-Item` (`gi`), `Clear-Content` (`clc`) e
   `Import-Csv` (`ipcsv`), alias de la sección Notas de cada ayuda («Todas las plataformas»).
5. **Ep. 11 «Crear, copiar, mover, renombrar»**, viñeta *Copy-Item*: reescrita (G1).
6. **Ep. 11 «Leer y escribir contenido»**: `Clear-Content` en el bloque de código; párrafo nuevo
   sobre `Import-Csv` (dos citas, `-Header`, ejemplo 1 de Microsoft) y `Clear-Content -Force`.
7. **Trazabilidad**: fecha del remate; cmdlets nuevos y la contradicción de `Copy-Item` en la fila de
   ficheros; filas nuevas para `about_Operators` 5.1 y `System.String`; los ejemplos de la tabla de
   métodos, declarados propios en «Oficio sin fuente detrás».

Relectura de antecedentes: «su `about_Operators`» (5.1, nombrada antes en la frase), «la misma
referencia» (la de .NET, en el párrafo anterior), «la tabla anterior» (la de operaciones), «la ayuda
del propio cmdlet» (Copy-Item): todos tienen delante su antecedente.

Corrección propia durante el remate: el ejemplo `IndexOf('\\')` habría buscado dos barras en
comillas simples (devuelve -1); queda `IndexOf('\')`. Los ejemplos de la tabla no se han ejecutado.

## Lentes

- `indice.py`: 16.207 palabras, 77 epígrafes (sin epígrafes nuevos; índice regenerado).
- `refutar_prosa.py`: primera pasada, 1 hallazgo (sigla «SEV» en un ejemplo, cambiado a
  `'PC01-sede'`); segunda pasada, 0.
- `negritas.py`, `refutar_exactitud.py`, `refutar_modo.py`: no proceden (tema técnico sin norma).

## Resultado sobre las preguntas

11 pasa a «entera» (tabla de métodos); 15 pasa a «entera» con la contradicción declarada (la
respuesta según la ayuda del cmdlet es la b); la variante de la 7 y la complementaria de la 15, a
«entera». Amplió contenido nuevo: **sí** (L1, L2) → procede la fase 5 bis sobre los pasajes 3, 4, 5 y 6.

## Ficheros tocados

El tema y este informe. Las descargas, en el directorio temporal de la sesión, sin guardar en el
repositorio. Las diferencias que `git diff` muestra en los temas 01, 05 y 06 no son de este remate.
