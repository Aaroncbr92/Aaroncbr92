# Tema 14 del específico de Operador/a Informático · Seguridad informática, criptografía y protección en redes

**Siglas**: RTVA, CSRTV, FNMT, NIST, RFC, INCIBE, CCN, ENS, RGPD, LOPDGDD, eIDAS, PUA, EDR, DMZ, IDS, IPS, WAF, VPN, TSA, CRL, OCSP, SAN, SNI.

Esqueleto para repasar, no resumen: el tema desarrolla cada dato.

<!-- indice -->
<!-- /indice -->

## 1. Seguridad en el puesto de usuario
- C-I-D: ransomware ataca disponibilidad; spyware, confidencialidad.
- NIST SP 800-128, malware: daña C-I-D; incluye spyware y «some forms of adware». ENS: «código dañino».
- NIST/RFC 4949, virus: necesita anfitrión ejecutado. Microsoft: virus de macros.
- NIST SP 800-28, gusano: sin anfitrión ni usuario.
- NIST SP 800-28, troyano: código oculto en programa útil. Microsoft: no se propaga solo.
- NIST/CNSSI 4009, spyware: recoge información en secreto; registrador de teclas (Microsoft).
- Microsoft, adware: anuncios, encuestas; es PUA: «Las PUA no se consideran malware».
- Microsoft, ransomware: cifra, nota de rescate, se propaga por red. INCIBE: amenaza con publicar.
- Microsoft: puerta trasera, descargador (necesita Internet), dropper (no), exploit, software de seguridad no autorizado, ofuscador. NIST: rootkit, ataque combinado. Sin archivos: Defender por comportamiento.
- Microsoft, vías: sin actualizar; email, SMS, Teams; sitios maliciosos; pirateado; USB. INCIBE: spam, malas configuraciones, actualizaciones falsas, cracking.
- NIST, phishing: solicitud fraudulenta. Pharming (SP 800-63-4): redirigir corrompiendo DNS o equipo. Microsoft: 0 por O, 1 por l.
- Microsoft: malware corre con privilegios del usuario; cuenta no administradora; UAC no basta; 3-2-1 (3 copias, 2 ubicaciones, 1 sin conexión); wifi pública; unidades de confianza. Oficio: doble factor, cifrado, mínimo privilegio, formación.
- ENS (RD 311/2022, anexo II) op.exp.6, básica: .1 prevención y reacción; .2 software en puestos, servidores, perimetrales; .3 analizar ficheros externos; .4 bases actualizadas; .5 tiempo real. MEDIA +R1+R2; ALTA +R3 lista blanca +R4 EDR.
- ENS mp.eq.2.1: bloqueo por inactividad; autenticidad BAJO no, MEDIO mp.eq.2, ALTO +R1 (cancelar sesiones). ENS: sector público (Ley 40/2015 art. 2).
- NIST SP 800-83, antivirus: identifica malware, previene o contiene. Firmas: actualizar (op.exp.6.4), límite malware nuevo. Comportamiento: Defender predictivo desde 2015, anomalías activas por defecto. División = oficio.
- Defender: Windows 10, 11, Server. Activo; pasivo (no neutraliza; sólo con Defender para punto de conexión); deshabilitado. ¿Quién me protege? > Administrar proveedores; `Get-MpComputerStatus`, AMRunningMode Normal = activo.
- Procesos: MdCoreSvc/MpDefenderCoreService.exe; WinDefend/MsMpEng.exe; WdNisSvc/NisSrv.exe; MpCmdRun.exe. Examen de seguridad de Microsoft no reemplaza al antimalware.
- INCIBE: apagar el equipo; no pagar; plan de respuesta; No More Ransom (no todos tienen solución). Microsoft: limpiar antes. Tema 3.
- RGPD 33-34: autoridad ≤72 horas, salvo improbable riesgo; después, con motivos; encargado al responsable sin dilación. Interesado si alto riesgo; no si cifrado, medidas ulteriores o esfuerzo desproporcionado.
- LOPDGDD 87: acceso «a los solos efectos de controlar el cumplimiento de las obligaciones laborales o estatutarias y de garantizar la integridad de dichos dispositivos»; criterios con representantes; uso privado: precisar usos y garantías.

## 2. Seguridad y protección en redes de comunicaciones
- NIST, cortafuegos: pasarela que limita acceso entre redes. SP 800-41 Rev. 1 (2009): bloquear lo no permitido expresamente, entrada y salida = «deny by default».
- Tipos: paquetes (red/transporte; puertos; sin estado; router con ACL); con estado (tabla); aplicación (protocolo; proxy); WAF (HTTP). Capas: oficio.
- ENS mp.com.1: .1 protección perimetral, todo el tráfico la atraviesa; .2 flujos autorizados previamente.
- DMZ (NIST/CNSSI 4009-2022): segmento perimetral entre interna y externa; acceso restringido a información publicable. Zonas: externa, perimetral (web, correo, portal), interna (bases de datos, ficheros, puestos). Oficio: de la DMZ no se abre hacia dentro; dos cortafuegos o uno de tres patas.
- IDS (NIST): vigila eventos, avisa en tiempo real o casi. IPS: además intenta detener.
- Sandbox (NIST): entorno restringido sin acceso a recursos no autorizados. MV aísla un sistema (tema 10), sandbox un proceso.
- ENS mp.s.1 correo: .1 cuerpo y anexos; .2 encaminamiento; .3 spam; .4 código dañino; .5 applets; .6 limitar uso privado; .7 concienciación.
- RFC 7208 SPF: dominio autoriza servidores. RFC 6376 DKIM: firma, clave pública del dominio. RFC 9989 (mayo 2026) DMARC: política e informes; obsoleta RFC 7489 y 9091. Se publican en el DNS.
- Puertos (oficio): HTTP 80/HTTPS 443; DNS 53; SMTP 25, cliente 587; IMAP 143/993; POP3 110/995; FTP 21/SFTP 22; SSH 22/Telnet 23; FTP y Telnet en claro, desaconsejados.
- HTTPS: confidencialidad, integridad, autenticación del servidor; no garantiza que el sitio sea de fiar.
- Ataques web (oficio), WAF: inyección de SQL; guion entre sitios; falsificación de petición; denegación de servicio.
- ENS mp.s.2: .1 imposible obviar la autenticación, d) inyección de código; .2 escalado de privilegios; .3 cross site scripting.
- NIST SP 800-46 Rev. 2, cuatro formas: túnel (VPN; datos en cliente), portal (navegador; aplicación en servidor), escritorio remoto (controla un PC de la organización), acceso directo (servidor en DMZ; correo web). Dependen de la seguridad física del cliente. Túnel no protege datos del cliente ni pasarela-recursos internos. Tema 10.
- VPN (RFC 4949): red lógica restringida por cifrado o tunelado; confidencialidad e integridad cliente-pasarela.
- SP 800-77 Rev. 1 (2020), arquitecturas: pasarela a pasarela; acceso remoto (host-to-gateway); equipo a equipo; malla.
- IPsec: capa de red. ESP transporta cifrado e integridad; AH ya no recomendado. IKE negocia conexión, autentica, parámetros, claves de sesión; vigente IKEv2.
- VPN SSL: usa TLS, puerto 443. WireGuard: reciente, más simple y menos flexible que IPsec.
- ENS mp.com.2.1: VPN cifradas fuera del dominio (bajo); R1 (medio): algoritmos y parámetros autorizados por el CCN. mp.com.3.1: autenticar el otro extremo.
- Oficio: la VPN protege el transporte, no el destino.

## 3. Criptografía y algoritmos
- NIST, simétrica: misma clave secreta. Asimétrica: dos claves, una cifra o firma, otra descifra o verifica. Oficio: simétrica IDEA, AES, 3DES, ChaCha20; asimétrica RSA, ElGamal, curva elíptica.
- Cifrar: pública cifra, privada descifra. Firmar: privada firma, pública verifica. La privada no se entrega; la pública va en el certificado.
- Diffie-Hellman: intercambio de claves, no cifra. Asimétrica lenta, simétrica rápida.
- AES (NIST, FIPS 197): simétrico de bloque; BitLocker XTS-AES (tema 6).
- SP 800-77 Rev. 1: 3DES desaconsejado desde 2019, prohibido después de 2023. IKEv2: no usar 3DES, MD5, SHA-1, grupos DH 2 y 5; usar AES-CBC con HMAC-SHA-2 o AES-GCM con DH 14 o ECDH 19, 20, 21. HMAC-MD5 nunca aprobado. Aviso sólo IPsec.
- NIST, hash: salida de longitud fija; una vía; resistente a colisiones. FIPS 180-4 (2015): SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, SHA-512/256; 160 a 512 bits. FIPS 202: SHA3-224, -256, -384, -512 (SHAKE128 y SHAKE256 no son resumen); complementa a SHA-1 y SHA-2. MD5 en ninguna.
- NIST, firma digital: origen, integridad, no repudio; no cifra.

## 4. Certificados digitales y autoridades de certificación
- RFC 5280: vincula clave pública con titular, firmado por CA; vida limitada; X.509 v3.
- eIDAS art. 3.14 certificado de firma (persona física, nombre o seudónimo); 3.29 de sello (persona jurídica); 3.38 de sitio web. Cualificado: anexos I, III, IV.
- SAN (RFC 5280): extensión del certificado, más identidades. SNI: extensión del protocolo, el cliente dice el nombre.
- NIST, CA: expide y revoca. PKI: expedir, mantener, revocar. RFC 5280: entidad final, CA, RA (opcional, delegada), emisor de CRL, repositorio.
- eIDAS 3.19 prestador; 3.20 cualificado; Ley 39/2015 art. 10.2 aún dice «Lista de confianza de prestadores de servicios de certificación». Art. 22: listas de confianza.
- Servicios de confianza (art. 3.16, Reglamento 2024/1183): catorce, a) a n); i) crear sellos de tiempo; j) validarlos; m) archivo; n) libro mayor. Certificados = a).
- Ley 6/2020 art. 4: caducidad o revocación; cualificados ≤5 años.
- Art. 5.1, nueve supuestos: a) solicitud; b) secreto de datos de creación violado; c) resolución judicial o administrativa; d) fallecimiento o extinción; e) fin de representación; f) cese del prestador; g) falsedad o cambio de datos; h) criptografía insegura; i) otra causa lícita.
- eIDAS 28.4: revocado, no recupera estado. Ley 6/2020 5.2: suspensión en a), c), h) y duda de b), g), si la declaración de prácticas la prevé.
- RFC 5280, CRL: lista con fecha y hora, firmada, pública; se busca el número de serie. RFC 6960, OCSP: estado actual sin CRL.
- FNMT: revocar si copiado, PIN conocido, extravío.
- Ley 6/2020 art. 7: personación (DNI, pasaporte) o firma legitimada ante notario; 7.2 a distancia (vídeo-identificación) por orden ministerial; 7.6 «podrá no ser exigible» si <5 años. FNMT ciudadano: App Móvil, vídeo-identificación, presencial, DNIe.

## 5. Sellado de tiempo
- eIDAS 3.33: vincula datos con un instante, prueba de existencia. RFC 3161: TSA, existía antes de un momento; firma anterior a la revocación sigue verificable. messageImprint «SHOULD» contener el resumen.
- eIDAS 41: 1) efectos y admisibilidad aunque no sea cualificado; 2) cualificado: presunción de exactitud e integridad.
- Art. 42.1 cualificado: a) vínculo sin modificación sin detectar; b) fuente ligada al UTC; c) firma o sello avanzado del prestador cualificado o equivalente.
- Sello electrónico (3.25): origen e integridad; el de tiempo, fecha y hora.
- ENS mp.info.4 (sólo ALTO): .1 evidencia futura; .3 renovar regularmente; .4 sellos cualificados.

## 6. Firma electrónica
- eIDAS 3: firma (3.10); avanzada (3.11, art. 26); cualificada (3.12: avanzada + dispositivo cualificado + certificado cualificado). Firmante (3.9) persona física; la jurídica sella.
- Art. 26: a) vinculada al firmante de manera única; b) identifica; c) control exclusivo; d) modificación detectable.
- Art. 25: 1) efectos y prueba aunque no sea cualificada; 2) cualificada = manuscrita.
- Ley 39/2015 10.2 (desde 30-06-2022): a) firma cualificada y avanzada con certificados cualificados, Lista de confianza; b) sello cualificado y avanzado; c) otro sistema: registro previo, comunicación a la Secretaría General de Administración Digital, eficacia a los dos meses; a) y b) en todos los procedimientos. 10.5: identidad acreditada por la firma.
- ENS mp.info.3: cualquier firma legal; R1 (medio) avanzada con certificados cualificados. Tema 15.
- Ley 6/2020 6.1.a): nombre, apellidos y DNI, NIE o NIF, o pseudónimo inequívoco. FNMT: ciudadano; empresa; empleado público; seudónimo.

## 7. Instalación y administración de certificados electrónicos y software de la FNMT
- Soportes: software (exportable); tarjeta (no); nube.
- FNMT, cuatro pasos en orden: 1) configuración previa; 2) solicitud por Internet, Código de Solicitud por correo, contraseña no recuperable; 3) acreditación en Oficina de Acreditación de Identidad (AEAT, Seguridad Social, cita previa); 4) descarga ~1 hora después, copia de seguridad recomendada.
- Configurador FNMT-RCM: genera el par de claves en el equipo. Última versión de Firefox, Chrome, Edge, Opera, Safari.
- Precauciones: no formatear entre solicitud y descarga; mismo equipo y usuario; antivirus y proxies pueden impedirlo.
- Tarjeta (Windows): Instalable TC-FNMT, administrador, navegadores cerrados, 32/64 bits (v2.0.0, 27,5 MB): Java 8 Update 45 a 15, PKCS#11 (Mozilla), Smart Card Minidriver. Mac/Linux: MultiCard PKCS11 FNMT DNIe. Utilidades: Gestión de Certificados (v1.4.0.8; ver, importar, PIN); Eliminación de Certificado; Actualizador de Claves; Formatear tarjeta.
- Edge: menú o ALT+F > Configuración > «Certificados» > Administrar certificados > Personal. Firefox: Menú / Ajustes / Privacidad y Seguridad / Certificados / Ver certificados.
- Windows, tres almacenes: ordenador local, usuario actual, cuenta de servicio. `certlm.msc`, `certmgr.msc`, `mmc`: ver, exportar, importar, eliminar. Sin ser administrador, sólo el propio usuario.
- FNMT, exportar: con clave privada sólo para uso personal o copia; sin ella, para entregar; nunca entregar la privada. `.pfx` y `.p12` con clave privada; `.cer` pública (DER o PEM); `.crt` pública (PEM, Firefox).
- Edge (FAQ 1551): Personal > Exportar > «Exportar la clave privada» > contraseña (se pide al importar).
- Renovar: 60 días previos, sin revocar; tres pasos; ~1 hora. Si se obtuvo con certificado, DNIe, vídeo-identificación o ya renovado: acreditar otra vez.
- Revocar: con certificado, anulación online; sin él, Oficina de Acreditación; con código, teléfono 24x7. Verificar: servicio de verificación.
- Validez: AC FNMT Usuarios hasta 31-12-2028; sin plazo general.

## Normativa y huecos
- No da: HTTP/TLS, 802.1X (tema 13); BitLocker (6); Server (8); copias (3); escritorio remoto (10); ENS entero (15); NIS2 sin transponer; ISO 27000, CCN-STIC, FIPS 197, SP 800-131A, productos de RTVA/CSRTV: no leídos o no constan.
- Leído el 05-10-2026 (FIPS 180-4 y 202: 06-10-2026); eIDAS consolidado 18-10-2024.
