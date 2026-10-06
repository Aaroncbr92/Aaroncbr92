# Puesto 29 · Tema 6 · Preguntas de refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/06-windows-11.md`.
15 preguntas tipo test de 4 opciones, repartidas por las rúbricas del enunciado (teoría y aplicación
práctica, AP), distintas de las 10 de control de la redacción. Se contestan **sólo con el tema**.

1. **Versión.** La 25H2 de Windows 11 en ediciones Enterprise y Education deja de recibir
   actualizaciones el: a) 2027-10-12; b) 2028-10-10; c) 2029-10-09; d) 2026-10-13. → b. «Antes de
   empezar», tabla de versiones. **Entera.**
2. **Instalación.** Windows 11 Home exige para completar la configuración inicial: a) TPM 1.2;
   b) una cuenta local; c) conexión a Internet y cuenta Microsoft; d) unirse a un dominio. → c. § 1,
   «Requisitos». **Entera.**
3. **Instalación (AP).** Un equipo instalado en modo BIOS con disco MBR debe pasar a UEFI sin
   perder datos. Se usa: a) `diskpart clean` y `convert gpt`; b) MBR2GPT antes de cambiar el modo del
   firmware; c) Restablecer este PC; d) `defrag /o`. → b. § 1, «UEFI, arranque seguro y GPT».
   **Entera.**
4. **Despliegue (AP).** Para llevar los perfiles y datos de los usuarios de un equipo viejo a uno
   nuevo se usan: a) DISM y Windows SIM; b) ScanState y LoadState, de USMT; c) WDS y WSUS; d) VAMT.
   → b. § 1, «El despliegue en una organización». **Entera.**
5. **Aplicaciones (AP).** Para instalar una aplicación desde la línea de órdenes con el administrador
   de paquetes incluido en Windows 11 se usa: a) `msiexec /x`; b) `winget install`; c) `sc.exe
   create`; d) `gpupdate /boot`. → b. El tema sólo da `msiexec` y la desinstalación; no nombra
   winget ni Microsoft Store, ni remite al tema 7, que sí trata WinGet. **No.**
6. **Discos (AP).** En un disco básico MBR se crean particiones con Administración de discos. La
   cuarta: a) es principal; b) se configura como unidad lógica en una partición extendida; c) no se
   puede crear; d) exige convertir a dinámico. → b. § 3, «GPT y MBR». **Entera.**
7. **Controladores.** En el Administrador de dispositivos, «Código 28» significa: a) dispositivo
   deshabilitado; b) los controladores del dispositivo no están instalados; c) Windows detuvo el
   dispositivo por problemas; d) no se puede iniciar. → b. § 3, «Controladores». **Entera.**
8. **Red (AP).** `netstat -o` muestra una conexión sospechosa con PID 4321. Para saber qué programa
   es: a) `ping /a`; b) `tracert /d`; c) buscar el PID en el Administrador de tareas; d) `ipconfig
   /displaydns`. → c. § 4, «Las órdenes de red». **Entera.**
9. **Recuperación (AP).** Tras instalar un controlador, Windows no pasa del arranque y hay que
   iniciarlo con el mínimo de controladores. Ruta: a) WinRE > Solucionar problemas > Opciones
   avanzadas > Configuración de inicio > Reiniciar > modo seguro; b) Configuración > Windows Update >
   Pausar; c) `gpupdate /force`; d) Restablecer este PC quitando todo. → a. El tema da WinRE, sus
   herramientas y el menú Inicio avanzado, pero no la Configuración de inicio ni el modo seguro.
   **No.**
10. **Recuperación (AP).** Para comprobar y reparar los archivos protegidos del sistema en un
    Windows 11 que arranca se ejecuta: a) `sfc /scannow` como administrador; b) `cipher /w`;
    c) `defrag /o`; d) `gpresult /r`. → a. El tema no lo da ni remite al tema 2, que sí trata `sfc`.
    **No.**
11. **Seguridad.** En el cifrado de dispositivo de un equipo que sólo usa cuentas locales: a) la
    clave de recuperación se guarda en la cuenta Microsoft; b) el equipo queda desprotegido aunque
    los datos estén cifrados; c) no se cifra; d) se usa AES-256. → b. § 6, «BitLocker y el cifrado de
    dispositivo». **Entera.**
12. **Configuración básica (AP).** Hay que dar a un becario una cuenta local sin privilegios en su
    puesto. Lo correcto: a) cuenta de administrador para evitar avisos del UAC; b) cuenta estándar,
    creada en Configuración > Cuentas > Otros usuarios (o `lusrmgr.msc`, `net user`); c) cuenta
    Invitado; d) desactivar el UAC. → b. El tema da que Microsoft recomienda el usuario estándar y
    que Cuentas reúne «cuenta Microsoft, profesional, familia…», pero no cómo se crea una cuenta
    local ni los tipos de cuenta del cliente. **A medias.**
13. **Red (AP).** Para administrar un Windows 11 desde otro puesto por RDP hay que: a) activar
    Escritorio remoto en Configuración > Sistema (edición Pro o superior); b) poner la red como
    pública; c) activar el modo desarrollador; d) activar DoH. → a. El tema sólo nombra RDP por las
    sesiones activas en los reinicios; no da cómo se habilita ni remite al tema 10. **No.**
14. **Notificaciones.** Prioridad «Superior» en las notificaciones: a) se puede dar a todas las
    aplicaciones; b) sólo a una aplicación; c) sólo a las de sistema; d) anula No molestar. → b.
    § 7. **Entera.**
15. **GPO (AP).** La UO Redacción tiene bloqueada la herencia. Un GPO del dominio marcado como
    forzado (aplicado): a) no llega a Redacción; b) llega igualmente a Redacción; c) sólo llega a los
    equipos; d) sólo si se ejecuta `gpupdate /force`. → b. § 13, «Dónde se vinculan y en qué orden
    se aplican». **Entera.**

**Resultado: 10 enteras, 1 a medias, 4 no.**
