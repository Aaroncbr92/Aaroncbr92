# Puesto 29 · Tema 6 · Revisión de los pasajes del remate (fase 5 bis)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/06-windows-11.md`. Revisados sólo los diez
pasajes que lista `29-T06-remate.md`, cada dato contra su fuente y cada remisión contra su antecedente.

## Fuentes leídas

| Fuente | Fecha de lectura |
|---|---|
| `w11-startupsettings.txt`, `w11-useraccts.txt`, `w11-localaccts.txt`, `w11-hello.txt` (volcados del remate) | releídos el 06-10-2026 |
| `ms-sfc.txt` (Microsoft Learn, «sfc») | volcado del 05-10-2026, releído el 06-10-2026 |
| `v-rdenable.txt` (Microsoft Learn, «Habilitar Escritorio remoto en el equipo») | volcado del 05-10-2026, releído el 06-10-2026 |
| Microsoft Learn (es-es), «Instalación de PowerShell en Windows» (en línea; no hay volcado) | 06-10-2026 |
| Temas 2, 7, 8 y 10 del puesto (para comprobar que las remisiones existen) | 06-10-2026 |

## Resultado por pasaje

1. Portada: correcta; «Extensión» pasa a 19.000 palabras (recuento tras esta revisión: 19.031).
2. Siglas (ELAM): conforme a la fuente.
3. «Qué se puede preguntar»: cubierto por los epígrafes nuevos.
4. WinGet (§ 2): confirmado en línea («La herramienta de línea de comandos winget está incluida en
   Windows 11…»); el tema 7 lo desarrolla. Faltaba la fuente en Trazabilidad: **añadida**.
5. Escritorio remoto (§ 4): ruta Inicio > Configuración > Sistema > Escritorio remoto confirmada en
   `v-rdenable.txt`; el tema 10 lo desarrolla. Faltaba en Trazabilidad: **añadida**.
6. Configuración de inicio y modo seguro (§ 5): todas las negritas literales; la ruta y las nueve
   opciones, conformes. **Corregido** (error 9, menor): «lista numerada» no consta así; la fuente da una
   lista y dice que se elige con las teclas numéricas o F1-F9. Ahora: «nueve opciones, que se eligen por
   su número según el orden en que Microsoft las enumera». Antecedentes («subepígrafe anterior»,
   «esa casilla», epígrafes 1 y 3) correctos.
7. `sfc /scannow` (§ 5): confirmado en `ms-sfc.txt` («repairs files with problems when possible»; grupo
   Administradores); el tema 2 lo desarrolla. Faltaba en Trazabilidad: **añadida**.
8. Cuentas (§ 6): negritas literales; rutas reconstruidas conformes. Dos correcciones:
   - **Salvedad omitida (error 6)**: «en concreto, si no hay ninguna otra cuenta habilitada…» daba una
     de las tres reglas del modo seguro como la regla. Añadidas las otras dos de la fuente (cuenta de
     dominio administradora con red; otro miembro habilitado del grupo de administradores locales).
   - Windows Hello: «una externa» precisado a «una externa de infrarrojos», como dice la fuente.
   - «No es la cuenta que se da a un usuario nuevo del puesto» (Invitado) es inferencia de oficio: se
     declara ahora en «Oficio sin fuente».
   - Remisiones: epígrafe 1 (Home y cuenta Microsoft, línea con cita literal), epígrafe 9
     (`compmgmt.msc`), epígrafe 5 (modo seguro) y tema 8 (`net user`): existen.
9. «Lo que este tema no da»: remisiones a temas 2, 7, 8 y 10 comprobadas.
10. Trazabilidad: tres filas nuevas (sfc, PowerShell/WinGet, Escritorio remoto), frase de fechas
    ampliada y una entrada más en «Oficio sin fuente».

## Lentes

`refutar_prosa.py`: 0 hallazgos. `indice.py`: 64 epígrafes, 19.031 palabras (su mensaje dice «sin
portada: es un esquema», aunque la portada está; no se ha tocado la herramienta).

## Otros ficheros tocados

Sólo el tema y este informe.
