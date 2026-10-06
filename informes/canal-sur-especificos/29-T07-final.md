# Puesto 29 · Tema 7 · Revisión de los pasajes del remate (fase 5 bis)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/07-automatizacion-y-administracion-mediante-powershell.md`.
Alcance: sólo los siete pasajes listados en `29-T07-remate.md`.

## Fuentes releídas (learn.microsoft.com/es-es, descargadas el 06-10-2026)

Ayuda de `Copy-Item`, `Get-Item`, `Clear-Content`, `Import-Csv` (view=powershell-7.5); «Trabajar con
archivos y carpetas»; `about_Operators` 5.1 y 7.5; `System.String` (.NET 9.0).

## Resultado por pasaje

| # | Pasaje | Resultado |
|---|---|---|
| 1 | Ficha, Extensión 16.200 | Correcto (cifra de `indice.py` del remate; la corrección de abajo suma 3 palabras) |
| 2 | `&` al final, nota 5.1 | Correcto: cita literal en 7.5 («equivalente a Start-Job»); la lista de operadores especiales de 5.1 no lo trae (agrupación, subexpresión, matriz, llamada, conversión, coma, *dot sourcing*, formato, índice, canalización, intervalo, miembro, estático). Antecedente «su `about_Operators`»: correcto |
| 3 | Tabla de métodos de `System.String` y párrafo de advertencias | Las diez descripciones en negrita son literales (Substring con sus dos sobrecargas; StartsWith y IndexOf en su sobrecarga simple). «Todos los métodos de modificación…» y «Métodos que usan la comparación ordinal…» son literales. Ejemplos comprobados a mano: `Substring(0, 4)` da `PC01`, `IndexOf('\')` da 2. **Un hallazgo corregido** (abajo). Remisión a epígrafes 4 y 7: correcta (regla de la expresión regular en `-split`, ep. 4; `-replace`, ep. 7) |
| 4 | Filas `Get-Item` (`gi`), `Clear-Content` (`clc`), `Import-Csv` (`ipcsv`) | Correcto: descripciones literales; alias en «Notas», «Todas las plataformas» |
| 5 | Viñeta *Copy-Item* (contradicción) | Correcto: las tres citas de la ayuda (ejemplos 2 y 12, `-Force`) y las dos de la página de muestras son literales; «la ayuda del propio cmdlet» tiene antecedente |
| 6 | `Clear-Content` e `Import-Csv` en «Leer y escribir contenido» | Correcto: citas literales; `-Header` y la primera fila como encabezado en «Notas»; ejemplo 1 de Microsoft copiado tal cual |
| 7 | Trazabilidad | Correcto; fechas de lectura declaradas |

## Corrección aplicada

Ep. 6, segunda advertencia. El tema citaba que la referencia «separa las comparaciones **«ordinales
o ordinales insensibles a mayúsculas y minúsculas»**». En la fuente esa frase trata de otra cosa
(los caracteres nulos sólo se consideran en esas comparaciones): cita fuera de contexto (error 9).
Se sustituye por una frase de la misma página que sí sostiene la idea: **«una comparación ordinal
depende únicamente del valor binario de los caracteres comparados»**, así que distingue mayúsculas
de minúsculas. Comprobada en la fuente antes de aplicarla; antecedentes del párrafo releídos.

## Lentes

No se han vuelto a pasar `indice.py` ni `refutar_prosa.py` (cambio de una frase, sin epígrafes ni
siglas nuevas).

## Ficheros tocados

El tema 07 (una frase) y este informe. Descargas en el directorio temporal de la sesión.
