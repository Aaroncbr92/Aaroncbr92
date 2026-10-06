# Puesto 29 · Tema 6 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/06-windows-11.md` (1.455 líneas, ~17.700
palabras con `wc`). Preguntas: `29-T06-preguntas.md`. No se corrige nada: sólo se informa.

## Fuentes releídas y fecha

Todas el 06-10-2026, sobre los volcados de la redacción (`fuentes/canal-sur/informatico/web/w11-*.txt`,
leídos en línea el 05-10-2026): `w11-release`, `w11-pitr`, `w11-recovery`, `w11-pause`,
`w11-onerestart`, `w11-deploytools`, `w11-secapp`, `w11-bitlocker`, `w11-gpproc`, `w11-gpupdate`,
`w11-gpresult`, `w11-systools`, `w11-ways`, `w11-activehours`, `w11-notif`, `w11-wifi`, `w11-netess`,
`w11-taskbar`, `w11-uachow`. Literalidad de las negritas: no se repite el script (la verificación dio
586/586); se revisó la prosa en redonda y las tablas.

Saltado por exactitud: nada. «Copiado del común»: nada. «Copiado de RTVE sin cambios»: nada (los
dos temas de RTVE están en «actualizar: sí», y lo copiado de ellos va declarado como oficio).

## Lente 1 · Exactitud

Comprobados contra la fuente, sin hallazgo:

- Tabla de versiones: fechas de 26H2, 26H1, 25H2, 24H2 y 23H2 (disponibilidad y fin de
  actualización por ediciones) y compilaciones.
- Restauración puntual: activada en equipos no administrados, desactivada en los administrados por TI
  hasta 26H2, 200 GB, 24 h, 72 h, 2 %, Enterprise para frecuencia y retención; Restaurar sistema para
  ir «a un punto de restauración anterior a 3 días».
- Vuelta a la versión anterior en 10 días; pausa de 35 días; horas activas Automáticamente/Manual.
- VAMT (MAK sin KMS), Asistente de instalación (se puede usar antes de que Windows Update la ofrezca),
  reinicios de Windows Update «unas cuantas veces más».
- Seguridad de Windows: las siete secciones y su contenido.
- BitLocker: ediciones (Pro, Enterprise, Pro Education/SE, Education).
- GPO: síncrono/asíncrono, scripts, modos de combinación y reemplazo del bucle invertido, bloqueo de
  herencia frente a forzado, `Invoke-GPUpdate` local o remoto, `gpupdate /boot` y `/logoff`,
  `gpresult /h` en HTML.
- MSConfig: pestañas General, Arranque, Servicios, Inicio y Herramientas.
- Notificaciones: banners, pantalla de bloqueo, sonido, deslizar desde el lateral; Wi-Fi por QR con la
  cámara; límite de datos; lista de accesos directos con el botón secundario.

**Graves: 0. Menores: 0.** Los nueve errores: no hay normas (1, 2, 4, 7, 8 no proceden); siglas
presentadas (5); recuentos («seis componentes», «siete secciones», «cuatro posiciones», «cinco
disparadores», «seis áreas» que son siete, señalado) cuadran (3); salvedades repuestas en
verificación (6); lo que no tiene fuente, declarado como oficio en la Trazabilidad (9).

## Lente 2 · Cobertura del enunciado

Las quince rúbricas tienen epígrafe propio y en su orden. El test de 15 preguntas da 10 enteras, 1 a
medias y 4 no.

| # | Rúbrica | Laguna | Pregunta | Fuente disponible |
|---|---|---|---|---|
| L1 | Protección y recuperación del sistema | Configuración de inicio de WinRE y modo seguro (con funciones de red, símbolo del sistema): ni se da ni se remite | 9 | Buscar en support.microsoft.com («Iniciar el equipo en modo seguro en Windows»); no está entre los volcados |
| L2 | Configuración básica / seguridad | Cuentas locales del cliente: tipos (estándar, administrador), cómo se crean (Configuración > Cuentas > Otros usuarios, `lusrmgr.msc`, `net user`) y opciones de inicio de sesión (PIN, Windows Hello) | 12 | Buscar en soporte de Microsoft; `net user` ya está citado en el tema 8 |
| L3 | Interfaz y aplicaciones; protección y recuperación; conectividad de red | Faltan remisiones en «Lo que este tema no da»: instalar aplicaciones con WinGet (tema 7), reparar archivos del sistema con `sfc` (tema 2) y habilitar Escritorio remoto (tema 10). Basta una línea por cada una | 5, 10, 13 | Ya en los temas 2, 7 y 10 |

**Lagunas: 3** (L1 y L2 piden ampliar con fuente nueva; L3, sólo añadir remisiones).

## Otros ficheros tocados

Sólo `29-T06-preguntas.md` y este informe.
