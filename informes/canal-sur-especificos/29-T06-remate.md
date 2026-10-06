# Puesto 29 · Tema 6 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/06-windows-11.md`.
Entrada: `29-T06-refutacion.md` (0 hallazgos, 3 lagunas) y `29-T06-preguntas.md` (10 enteras,
1 a medias, 4 no). **Se amplió el tema** con contenido nuevo: hace falta la fase 5 bis sobre los
pasajes listados abajo.

## Fuentes nuevas, leídas el 06-10-2026

Guardadas en `fuentes/canal-sur/informatico/web/`:

| Fichero | Fuente | Para qué |
|---|---|---|
| `w11-startupsettings.txt` | Soporte de Microsoft (es-es), «Configuración de inicio de Windows» (la antigua «Iniciar el equipo en modo seguro» redirige aquí) | Configuración de inicio, nueve opciones (lista numerada, F1-F9), modo seguro y variantes, ELAM, salir del modo seguro con `msconfig` |
| `w11-useraccts.txt` | Soporte de Microsoft (es-es), «Administrar cuentas de usuario en Windows» | Agregar/quitar usuario, cuenta local, cambiar tipo de cuenta, cuenta profesional o educativa, recomendación de cuenta Microsoft y de pocos administradores |
| `w11-localaccts.txt` | Microsoft Learn (es-es), «Cuentas locales» (ms.date 13-04-2026) | Definición de cuenta local, Usuarios y grupos locales, Administrador e Invitado integrados, modo seguro y cuenta de administrador, Ejecutar como administrador |
| `w11-hello.txt` | Soporte de Microsoft, «Configure Windows Hello» (la URL es-es redirige a en-us) | Opciones de inicio de sesión: cara, huella, PIN; requisitos |

Las 39 negritas añadidas se comprobaron por script contra estos cuatro ficheros (espacios
normalizados): todas aparecen literalmente. `lusrmgr.msc`, que proponía la refutación, no consta en
ninguna fuente leída: no se da (se da la carpeta Usuarios y grupos locales de Administración de
equipos, que sí consta).

## Correcciones de la refutación

Ninguna: la refutación no trajo hallazgos (graves 0, menores 0). La discrepancia «seis áreas» que
son siete ya estaba señalada en el tema; no se toca.

## Lagunas cubiertas (se amplía el tema, ninguna pregunta se recorta)

| Pregunta | Laguna | Dónde se cubre ahora |
|---|---|---|
| 9 (No) | L1 · Configuración de inicio y modo seguro | § 5, nuevo «La configuración de inicio y el modo seguro» |
| 12 (A medias) | L2 · Cuentas locales, tipos, creación, inicio de sesión | § 6, nuevo «Las cuentas de usuario del equipo y el inicio de sesión» |
| 5 (No) | L3 · WinGet | § 2, «Instalar, desinstalar y arrancar aplicaciones», párrafo final de remisión al tema 7; y «Lo que este tema no da» |
| 10 (No) | L3 · `sfc` | § 5, «Las opciones de recuperación…», párrafo final de remisión al tema 2; y «Lo que este tema no da» |
| 13 (No) | L3 · Escritorio remoto | § 4, «La página Red e Internet», párrafo final con la ruta y remisión al tema 10; y «Lo que este tema no da» |

Con lo añadido, las 15 preguntas se contestan con el tema (la 5, la 10 y la 13 por la ruta o la
orden que da el texto y la remisión al tema donde se desarrollan).

## Pasajes cambiados (para la fase 5 bis)

1. Portada: «Redacción que se estudia» (añade lectura del 06-10-2026) y «Extensión» (18.900 palabras).
2. Siglas: añadida ELAM.
3. «Qué se puede preguntar»: Configuración de inicio y modo seguro; tipos de cuenta, cuenta local,
   Administrador e Invitado, Windows Hello.
4. § 2 «Instalar, desinstalar y arrancar aplicaciones»: párrafo final (WinGet, tema 7).
5. § 4 «La página Red e Internet»: párrafo final (Escritorio remoto, tema 10).
6. § 5, nuevo epígrafe «La configuración de inicio y el modo seguro» (tras WinRE), con tabla de nueve
   opciones; el caso práctico y el aviso sobre la casilla Arranque seguro de `msconfig` frente al
   arranque seguro UEFI van como oficio.
7. § 5 «Las opciones de recuperación…»: párrafo final (`sfc /scannow`, tema 2).
8. § 6, nuevo epígrafe «Las cuentas de usuario del equipo y el inicio de sesión» (tras UAC), con tabla
   de tareas en Configuración > Cuentas.
9. «Lo que este tema no da»: `net user` (tema 8); WinGet (7), `sfc` (2), Escritorio remoto (10).
10. «Trazabilidad»: fecha de las cuatro fuentes nuevas, cuatro filas nuevas y dos entradas más en
    «Oficio sin fuente».

Releídos los pasajes: «la primera» (cuenta Microsoft), «esa casilla», «el subepígrafe anterior» (WinRE)
y las remisiones a epígrafes 1, 3, 5 y 9 tienen su antecedente.

## Lentes

Tema técnico sin norma: `indice.py` (índice regenerado, 64 epígrafes, 18.880 palabras) y
`refutar_prosa.py` (0 hallazgos).

## Otros ficheros tocados

Los cuatro volcados nuevos en `fuentes/canal-sur/informatico/web/` y este informe.
