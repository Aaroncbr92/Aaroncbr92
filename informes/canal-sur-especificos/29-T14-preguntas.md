# Puesto 29 · Tema 14 · Preguntas de refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). 15 preguntas tipo test de 4 opciones, de teoría y de
aplicación práctica, contestadas **sólo con el tema**
(`temas/canal-sur-especificos/29-operador-a-informatico/14-seguridad-informatica-criptografia-y-proteccion-en-redes.md`).
La clave se comprobó en la fuente indicada.

| # | Grado |
|---|---|
| 1-6, 8, 9, 12, 14, 15 | Entera (11) |
| 10 | A medias (1) |
| 7, 11, 13 | No (3) |

1. **Malware (teoría).** ¿Qué código malicioso se propaga por la red sin programa anfitrión ni
   intervención del usuario? a) Virus. b) Troyano. c) Gusano. d) *Adware*.
   — c). Epígrafe 1, cuadro (NIST SP 800-28). **Entera.**

2. **Adware (teoría).** Según Microsoft, el *adware* («software de publicidad»): a) es siempre malware;
   b) es una aplicación potencialmente no deseada, que no se considera malware; c) es una variante de
   troyano; d) es un tipo de *ransomware*.
   — b). Epígrafe 1, «Tres precisiones», 1 (**«Las PUA no se consideran malware.»**). **Entera.**

3. **Antivirus (teoría).** Microsoft Defender Antivirus sólo puede funcionar en modo pasivo:
   a) en Windows Server; b) si no hay otro antivirus; c) en los puntos de conexión incorporados a
   Microsoft Defender para punto de conexión; d) cuando la protección contra alteraciones está activa.
   — c). Epígrafe 1, «El antivirus». **Entera.**

4. **Ransomware (práctica).** Un equipo muestra ficheros cifrados y una nota de rescate. Lo primero,
   según INCIBE: a) pagar para recuperar los datos; b) restaurar las copias de inmediato; c) apagar el
   equipo para que no se extienda a la red interna; d) ejecutar No More Ransom.
   — c). Epígrafes 1 y 8. **Entera.**

5. **Perímetro (práctica).** El servidor web público consulta una base de datos interna: a) los dos
   en la DMZ; b) servidor en la DMZ y base de datos en la red interna; c) los dos en la red interna;
   d) servidor en la red interna y base de datos en la DMZ.
   — b). Epígrafes 2 y 8. **Entera.**

6. **Cortafuegos (teoría).** El que guarda cada conexión en una tabla de estado y bloquea los paquetes
   que se salen del estado esperado es: a) de filtrado de paquetes; b) de inspección con estado; c) de
   aplicación web; d) un encaminador con listas de control de acceso.
   — b). Epígrafe 2, SP 800-41. **Entera.**

7. **ENS (teoría).** El bloqueo del puesto por inactividad [mp.eq.2] se exige: a) en todas las
   categorías; b) sólo en nivel alto; c) desde el nivel medio de autenticidad (en el bajo no aplica);
   d) sólo en los servidores.
   — c). RD 311/2022, anexo II, mp.eq.2: «Nivel BAJO: no aplica. – Nivel MEDIO: mp.eq.2.». El tema cita
   mp.eq.2.1 sin nivel, justo después de lo que se exige «ya en categoría básica». **No.**

8. **Correo (teoría).** La especificación vigente de DMARC es: a) la RFC 7489; b) la RFC 7208; c) la
   RFC 6376; d) la RFC 9989.
   — d). Epígrafe 2 (**«obsoletes RFCs 7489 and 9091»**). **Entera.**

9. **Acceso remoto (práctica).** Un redactor trabaja desde un hotel contra la red de la empresa. La
   arquitectura de VPN que define la SP 800-77 para ese caso es: a) pasarela a pasarela; b) acceso remoto
   (equipo a pasarela); c) equipo a equipo; d) malla.
   — b). Epígrafes 2 y 8. **Entera.**

10. **Hash (teoría).** ¿Cuál es una función resumen? a) AES. b) SHA-256. c) RSA. d) Diffie-Hellman.
    — b). El tema da AES (simétrico), RSA (asimétrico) y Diffie-Hellman (intercambio de claves), y cita
    «FIPS 180 and FIPS 202» sin decir que son las familias SHA; se acierta sólo por descarte. **A medias.**

11. **Algoritmos (teoría).** Según la SP 800-77 Rev. 1 del NIST, ¿qué algoritmo no debe usarse ya en
    IPsec? a) AES-GCM. b) 3DES. c) HMAC-SHA-2. d) AES-CBC.
    — b). SP 800-77r1: **«3DES, MD5, SHA-1, and DH Groups 2 and 5 should not be used.»** El tema pone
    3DES como ejemplo de simétrico sin ese aviso. **No.**

12. **Vigencia (teoría).** El período de vigencia de un certificado cualificado no será superior a:
    a) dos años; b) cuatro años; c) cinco años; d) diez años.
    — c). Epígrafe 4, Ley 6/2020, art. 4.2. **Entera.**

13. **FNMT (práctica).** Un ciudadano quiere renovar un certificado FNMT que ya se renovó una vez. Según
    la sede: a) puede renovarlo en línea con el certificado vigente; b) tiene que acreditar su identidad
    otra vez: presencialmente en una oficina, por vídeo-identificación o leyendo su DNIe; c) sólo
    presencialmente en una oficina; d) no puede obtener otro certificado.
    — b). Sede FNMT, «Renovar»: «sin que acredites tú identidad presencialmente en una de nuestras
    Oficinas de Registro, mediante el servicio de Vídeo-Identificación o con la lectura de tu DNIe». El
    tema dice que no se renueva «sin acreditar la identidad presencialmente en una oficina» y lleva a la
    c). **No** (el tema induce el error; ver refutación, hallazgo 1).

14. **Sellado de tiempo (teoría).** Los sellos cualificados de tiempo electrónicos disfrutan de una
    presunción de: a) autenticidad del firmante; b) exactitud de la fecha y hora y de la integridad de
    los datos vinculados; c) confidencialidad; d) no repudio.
    — b). Epígrafe 5, eIDAS art. 41.2. **Entera.**

15. **Certificados (práctica).** Para llevar el certificado de la FNMT en software a otro ordenador con
    capacidad de firmar, se exporta: a) a `.cer` sin clave privada; b) a `.crt`; c) con clave privada a un
    `.pfx` o `.p12` protegido con contraseña; d) no se puede exportar.
    — c). Epígrafe 7 (FAQ 1551 y 1553). **Entera.**
