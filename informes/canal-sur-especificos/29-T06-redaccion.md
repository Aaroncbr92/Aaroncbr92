# Puesto 29 · Tema 6 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real).
Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/06-windows-11.md`.
Material: `29-investigacion-B-sistemas.md` (§ Tema 6); RTVE
`temas/tecnica-informatica/16-sistemas-operativos-personales.md` y
`temas/gestion-administrativa/09-windows-10.md` (ambos «actualizar: sí», 15 %).

## Fuentes releídas y fecha

La investigación dejaba huecos (interfaz, personalización, Panel de control, red, controladores,
discos, procesamiento de GPO, gpedit en Home) y varias citas de support.microsoft.com sólo vía
resumen [WF]. Se descargaron todas las páginas directamente (support.microsoft.com sí respondió a
`curl` el 05-10-2026) y se guardaron como texto en
`fuentes/canal-sur/informatico/web/w11-*.txt`, con URL y fecha de lectura en cabecera. Todas leídas el
05-10-2026. Lista completa en la «Trazabilidad» del tema. Las citas [WF] de la investigación quedan
releídas en la página: notificaciones, protección del sistema, opciones de recuperación (la ruta
dudosa «Configuración > Solucionar problemas > Restablecer este equipo» no se usa; en WinRE es
«Solucionar problemas > Restablecer este equipo»), y `rstrui.exe` ahora con fuente («Restauración del
sistema»).

Huecos de la investigación cubiertos con fuente: orden LSDOU, refresco 90 + 30 min, 5 min en DC, 60
min de tope, forzado, bloqueo, bucle invertido («Procesamiento de directivas de grupo»); `gpupdate`,
`gpresult`; gpedit no disponible en Home («Herramientas de configuración del sistema»); interfaz
(barra de tareas, Inicio, Acoplar, Explorador, atajos), aplicaciones (desinstalar, inicio, `msiexec`),
Configuración y sus categorías, Panel de control, personalización (temas, colores), red (perfil
público/privado, TCP/IP, DoH, Wi-Fi, `ipconfig`, `ping`, `tracert`, `netstat`), controladores
(actualizar, reinstalar, revertir, códigos), discos (consola, GPT/MBR, básicos/dinámicos, `diskpart`
y la sintaxis de cada orden usada, `defrag`), instalación (formas, medios, instalación limpia,
activación), UAC (funcionamiento, ventanas, niveles), BitLocker y cifrado de dispositivo, `cipher`
(EFS), restauración puntual, KB5121772 (un reinicio al mes, 14-08-2026), horas activas.

Comprobación de literalidad por script (`scratchpad/check.py`, normaliza espacios y acentos graves):
las 581 citas en negrita del tema se hallan tal cual en las fuentes descargadas. Las rutas de menú
de las páginas de soporte salen desordenadas al pasar a texto; van en redonda, reconstruidas, nunca
en negrita.

## Qué se hizo

Versión base: 25H2 (vigente para equipos existentes el 24-09-2026), con 26H2 citada por su fecha
(29-09-2026) y sin novedades, como recomendó la investigación. Epígrafe previo de versión y quince
rúbricas en el orden del enunciado. «Panel de configuración» se interpreta como la pareja
Configuración/Panel de control (epígrafe 11), y se dice. `indice.py`: 16.931 palabras, 62 epígrafes.
`refutar_prosa.py`: 0 hallazgos (14 siglas sin presentar en la primera pasada, corregidas). Tema
técnico sin norma: no proceden `negritas.py`, `refutar_exactitud.py` ni `refutar_modo.py`. Ficha
escrita a mano (el tema no está en `herramientas/portadas.tsv`, como los demás de Canal Sur).

La extensión es alta (16.900 palabras con tablas y siglas): el enunciado tiene quince rúbricas y
cada una pide procedimiento y datos. El refutador puede proponer recortes de prosa; los datos están
todos citados.

Errores de las fuentes señalados en el tema: el menú Inicio «seis áreas» y enumera siete; las
preguntas frecuentes de Windows Update dicen «una vez al año» y «dos veces al año» para las
actualizaciones de funciones; la página UEFI/GPT llama a GPT «sistema de archivos»; erratas de
traducción con [sic] («Configurar Novedades automática», «sin signo», «no publicará», «Quita todos y
todos los formatos», etc.); WinRE: la misma página exige credenciales de administrador y dice que en
Windows 11 no hacen falta (se citan ambas).

Decisiones frente a RTVE (lo que no entra y por qué):

- Todo lo propio de RTVE: números de pregunta, respuestas oficiales, reparto de preguntas, «el
  examen entiende…», tablas de distractores (WPA3/TPM/EFS como opciones, `conexionList`, opciones a,
  b, d del UAC y de servicios), epígrafe de Ubuntu (es del tema 9).
- «La tecnología que se implementó en Windows 7…» (BitLocker): ninguna fuente leída da la versión de
  origen; se quita.
- La afirmación de RTVE 09 «En unidades de estado sólido no se desfragmenta: el sistema ejecuta en
  su lugar la orden TRIM» **la contradice Microsoft**: la referencia de `defrag` dice que en SSD la
  tarea programada hace análisis y recorte y la desfragmentación tradicional «se hace una vez al
  mes». No se copia; el tema da la versión de Microsoft. Manda la fuente.
- «La consola de servicios no tiene columna de dependencias» y «`get-service` … las dependencias no
  salen en su listado básico»: sin fuente; se sustituye por los parámetros `-RequiredServices` y
  `-DependentServices` de `Get-Service`, citados.
- Tabla de formatos `.msi`/`.exe`/`.msix` con ✔: se rehace con `msiexec` citado; `.exe` y `.msix`
  quedan en una frase.
- RTVE 09 (Windows 10): categorías de Configuración de Windows 10, cinta de opciones del Explorador,
  lista de accesorios (incluía WordPad) y herramientas del sistema: no valen para Windows 11 o no
  tienen fuente; se sustituyen por las páginas de soporte de Windows 11. La tabla de atajos se
  rehace con las descripciones literales de la página de métodos abreviados (la misma fuente que
  citaba RTVE, copia del 02-09-2026).
- Panel de control: la página de soporte con la lista de órdenes `.cpl` describe Windows 95/98/NT; no
  se usa y se declara.

## Copiado del común

Nada. Ningún tema cerrado de Canal Sur (común ni específicos) trata Windows.

## Copiado de RTVE sin cambios

Nada en sentido estricto: los dos temas de RTVE de este tema están marcados «actualizar: sí», así que
ningún pasaje entra en esta categoría y todo lo que viene de RTVE **sí se verifica**.

Para que el verificador lo localice, éstos son los pasajes copiados literal de RTVE (único cambio:
quitada la negrita, porque RTVE no citaba fuente; en dos casos se suprime la entradilla propia del
examen, indicada abajo). Van en redonda y se declaran como oficio en la Trazabilidad del tema:

| Pasaje en RTVE | Dónde va en el tema |
|---|---|
| RTVE 16 § 1: «Por qué la distinción importa al administrador: un `.msi` se puede instalar y desinstalar de forma uniforme en cientos de equipos; un `.exe` hay que estudiarlo caso por caso. Ésa es la razón de que el despliegue corporativo prefiera el primero.» | § 2, «Instalar, desinstalar y arrancar aplicaciones» |
| RTVE 16 § 2: «El atajo de memoria: `netstat` es *network statistics*, estadísticas de red. `tracert` es *trace route*, trazar la ruta.» | § 4, «Las órdenes de red» |
| RTVE 16 § 3: «Y la distinción que hay que llevar aprendida: cifrado de volumen frente a cifrado de fichero. El primero protege del robo del soporte; el segundo, del vecino de escritorio. Son complementarios y resuelven amenazas distintas.» | § 6, «BitLocker y el cifrado de dispositivo» |
| RTVE 16 § 3, frase final del párrafo del distractor: «Pero el chip no cifra el disco: guarda la llave.» → adaptada: «El chip no cifra el disco: guarda la llave y comprueba que el arranque no se ha tocado.» | § 6 (adaptada, no literal) |
| RTVE 16 § 4: «un administrador trabaja con una ficha de permisos reducida hasta que hace falta elevarla. Así, un programa lanzado por error no hereda privilegios administrativos sin que nadie lo vea. La ventana que aparece no es un trámite: es el punto donde el usuario decide elevar.» (entradilla cambiada: «Lo que el mecanismo resuelve de verdad:», sin «, y es lo que hay que entender») | § 6, «El control de cuentas de usuario» |
| RTVE 16 § 5: «Qué es una dependencia de servicio y por qué importa: un servicio puede necesitar que otro esté en marcha para arrancar. Cuando un servicio no arranca, lo primero que se mira es su pestaña de dependencias, porque el que falla suele ser el de abajo, no el que da el error.» | § 9, «Los servicios y sus dependencias» |
| RTVE 16 § 6: «La forma de una ruta de este tipo es siempre la misma:» + bloque `\\servidor\recurso\camino\dentro\del\recurso` | § 4, «Las rutas de red (UNC)» |
| RTVE 16 § 6: «el segundo elemento es el nombre del recurso compartido, no una unidad local. Los dos puntos de `C:` no caben ahí: es la letra de unidad vista desde el propio equipo, y la ruta de red se escribe desde fuera.» (sin la entradilla «Y de ahí se resuelve la pregunta:»; mayúscula inicial) | ídem |
| RTVE 16 § 6, tabla «Ruta / Por qué vale», tres filas, texto de las celdas literal | ídem |
| RTVE 16 § 6: «La diferencia es el carácter: el dólar es parte del nombre del recurso compartido y los dos puntos no lo son.» | ídem |
| RTVE 09 § 4.2: «Arrastrar dentro de la misma unidad mueve; entre unidades distintas, copia. Es el comportamiento por defecto y la causa de la mitad de los sustos.» (en minúscula tras dos puntos) | § 2, «El Explorador de archivos» |
| RTVE 09 § 1: «Lo borrado de una unidad de red o de una memoria extraíble no pasa por ella.» → adaptada: «…no pasa por la papelera.» | ídem (adaptada) |

## Otros ficheros tocados

- `fuentes/canal-sur/informatico/web/w11-*.txt`: volcados de texto de las páginas de Microsoft y SNIA
  leídas (nuevos; URL y fecha en cabecera). No se ha modificado ningún fichero existente.
- Ningún otro tema ni informe.

## Diez preguntas tipo test (comprobación de cobertura)

Repartidas por las rúbricas; las marcadas (AP) son de aplicación práctica. Todas se contestan
enteras con el tema.

1. Para instalar Windows 11, el módulo de plataforma segura debe ser, como mínimo, versión: a) 1.2;
   b) 2.0; c) 1.1; d) no es requisito. → **b**. § 1, tabla de requisitos («TPM: módulo de plataforma
   segura (TPM) versión 2.0»). (BitLocker sólo pide 1.2, § 6: buen distractor.) Entera.
2. En Windows 11, la barra de tareas: a) se puede mover a la parte superior desde su configuración;
   b) sólo se puede alinear al centro o a la izquierda y va siempre abajo; c) se puede anclar a
   cualquier lado; d) está alineada a la izquierda por defecto. → **b**. § 2, «La barra de tareas».
   Entera.
3. En un disco básico con estilo MBR se pueden crear: a) 128 particiones principales; b) hasta cuatro
   principales, o tres principales y una extendida; c) una principal y ocho lógicas; d) volúmenes
   reflejados. → **b**. § 3, «GPT y MBR». Entera.
4. (AP) Tras una actualización, la tarjeta de red deja de funcionar. Para volver a la versión anterior
   del controlador: a) Administrador de dispositivos > Propiedades > Controlador > Revertir al
   controlador anterior; b) Restablecer este PC; c) `gpupdate /force`; d) Desinstalar desde
   Programas y características. → **a**, con permisos de administrador. § 3, «Controladores».
   Entera.
5. (AP) `ping 192.168.1.10` responde, pero `ping servidor01` no. Lo más probable es: a) cable
   desconectado; b) un problema de resolución de nombres; c) cortafuegos del equipo local; d) TTL
   agotado. → **b**; `ipconfig /flushdns` vacía la caché del cliente DNS. § 4, «Las órdenes de red».
   Entera.
6. Según Microsoft, la partición de recuperación de un equipo UEFI debe ir: a) antes de la ESP; b)
   inmediatamente después de la partición de Windows; c) al final del disco tras las de datos; d) en
   un disco aparte. → **b**, para que Windows pueda ampliarla en futuras actualizaciones. § 10.
   Entera.
7. WinRE se inicia automáticamente cuando: a) falla un único arranque; b) hay dos intentos
   fallidos consecutivos de iniciar Windows; c) el disco supera el 90 % de ocupación; d) se instala
   una actualización de características. → **b**. § 5, «El entorno de recuperación». Entera.
8. Un usuario estándar intenta una tarea que requiere privilegios de administrador con UAC activo.
   Windows le muestra: a) la solicitud de consentimiento (basta con «Sí»); b) la solicitud de
   credenciales de un administrador; c) nada, se deniega en silencio; d) el Visor de eventos. →
   **b**. § 6, «El control de cuentas de usuario». Entera.
9. (AP) Un GPO vinculado al dominio fija el fondo de escritorio A y otro vinculado a la UO del
   usuario fija el B, sin forzado ni bloqueo. Se aplica: a) A, porque el dominio está más arriba; b)
   B, porque se procesa después y el contenedor más cercano gana; c) ninguno, por conflicto; d) el
   GPO local. → **b**. Y si no se fuerza, el cambio llega en segundo plano cada 90 minutos más hasta
   30 aleatorios. § 13. Entera.
10. Sobre puntos de restauración y reinicios: ¿cuál es correcta? a) La protección del sistema viene
    habilitada por defecto; b) Restaurar sistema revierte los archivos personales; c) las horas
    activas predeterminadas son de 8 a. m. a 5 p. m. y pueden durar hasta 18 horas; d) la
    restauración puntual guarda puntos durante 30 días. → **c**. § 14 (protección no habilitada por
    defecto; Restaurar sistema no toca archivos personales; puntual, 72 horas) y § 15. Entera.

Rúbricas que no tienen pregunta propia en estas diez y que el tema cubre: centro de notificaciones
(§ 7: Win + N, No molestar, prioridades), personalización (§ 8), configuración básica y avanzada (§ 9:
categorías, `msconfig`, `msinfo32`, `regedit`, `gpedit` no en Home), panel de configuración (§ 11) y
modo desarrollador (§ 12: Sistema > Avanzado en 25H2, requiere administrador). No ha hecho falta
ampliar el tema.
