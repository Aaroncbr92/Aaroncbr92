# Puesto 29 · Tema 14 · Redacción (fase 2)

Fecha: 05-10-2026 (encargo fechado 24-09-2026; las fuentes se leyeron el 05-10-2026, fecha real, como
en la investigación y en los temas 1 a 12). Escrito por epígrafes, guardando cada parte.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/14-seguridad-informatica-criptografia-y-proteccion-en-redes.md`
(15.700 palabras con siglas y cuadros; 8 epígrafes, 45 entradas de índice).
Material: `29-investigacion-C-datos-redes-seguridad.md` (§ Tema 14). Fila de
`informes/canal-sur-reuso/informatica.tsv`: RTVE `gestion-administrativa/08`, `tecnica-informatica/21`,
`/20`, `/04`, `gestion-administrativa/01`, 40 %, «actualizar: no». Común: `temas/canal-sur-comun/10-proteccion-de-datos.md`.

## Avance

- Ficha, siglas, enunciado, «qué se puede preguntar» y epígrafe 1 (puesto de usuario: propiedades, malware, virus/gusanos/troyanos, adware/spyware/ransomware, otras categorías, mecanismos de infección, protección en el SO, antivirus, ransomware y brecha, art. 87 LOPDGDD) guardados.
- Epígrafe 2 (cortafuegos, perímetro y DMZ, IDS/IPS, sandboxing, correo, servicios de Internet, acceso remoto, VPN, mapa de mecanismos) guardado.
- Epígrafes 3 (criptografía, algoritmos, hash, firma digital), 4 (certificados, CA/PKI/prestadores, vigencia y revocación), 5 (sellado de tiempo) y 6 (firma electrónica) guardados.
- Epígrafe 7 (certificados y software de la FNMT), 8 (aplicación práctica), normativa, «Lo que este tema no da» y trazabilidad guardados. Índice con `indice.py`.

## Fuentes leídas y fecha

Todas el 05-10-2026. Descargadas con URL y fecha en cabecera en `fuentes/canal-sur/informatico/web/`,
prefijo `s-` (57 ficheros nuevos):

- Microsoft Learn/Soporte (es-es): `s-ms-criterios-malware`, `s-ms-troyanos`, `s-ms-gusanos`,
  `s-ms-prevenir-malware`, `s-ms-macro`, `s-ms-sin-archivos`, `s-ms-defender-antivirus`, `s-ms-pua`,
  `s-ms-ransomware-soporte`, `s-ms-certificados-mmc`.
- NIST: `s-nist-sp800-83r1`, `s-nist-sp800-41r1`, `s-nist-sp800-46r2`, `s-nist-sp800-77r1` (texto de los
  PDF) y 23 términos del glosario CSRC (`s-nist-glos-*`).
- RFC: `s-rfc5280`, `s-rfc3161`, `s-rfc6960`, `s-rfc7208`, `s-rfc6376`, `s-rfc9989`; estado de cada una
  consultado en `rfc-editor.org/rfc/rfcNNNN.json`.
- eIDAS: `s-eidas-consolidado-20241018` (EUR-Lex). La página «ALL» de EUR-Lex lista tres consolidaciones
  (2014-09-17, 2024-05-20, 2024-10-18): la de 18-10-2024 es la última. Coincide con lo que dijo la
  investigación; se completó la letra n) del art. 3.16 («la actividad de registro de datos electrónicos
  en un libro mayor electrónico.»), que la investigación dejó abierta: la lista acaba en n).
- FNMT: `s-fnmt-obtener`, `-configuracion-previa`, `-solicitar`, `-descargar-certificado`,
  `-descarga-software`, `-renovar`, `-anular`, `-verificar`, FAQ `1063`, `1146`, `1208`, `1551`, `1553`.
- Ya en el repositorio: `incibe-guia-ransomware.txt`, `nomoreransom-es.txt`; BOE volcados por la
  investigación: BOE-A-2020-14046 (Ley 6/2020), BOE-A-2015-10565 (Ley 39/2015, art. 10 leído con
  `boe.py precepto`, 3 redacciones, vigente desde 30-06-2022), BOE-A-2022-7191 (RD 311/2022, anexo II
  con 1 redacción, vigente desde 05-05-2022).

No se pudieron leer: INCIBE (glosario, bloqueo «Request Rejected»), OSI (conexión rechazada), páginas
«security-101» de microsoft.com (403), página de Mozilla sobre certificados (vacía). Nada de lo que
dicen se usa.

## Comprobaciones

- Literalidad (script propio en el scratchpad, normaliza espacios, comillas y marcas ►C2/◄ de EUR-Lex):
  297 citas en negrita, 0 no halladas en las fuentes.
- `negritas.py` con todas las fuentes: tras pasar a cursiva los rótulos de párrafo (no son literales),
  sólo quedan como «no están» la cita del art. 3.19 eIDAS (el consolidado intercala la marca de
  corrección «►C2 … ◄»; el tema lo avisa) y nada más.
- `refutar_exactitud.py` con los volcados del BOE: 5 avisos falsos (citas del eIDAS y de la FNMT con
  «art.» o número entre paréntesis; el eIDAS no está en el BOE). Comprobadas a mano en sus fuentes.
- `refutar_prosa.py`: 9 siglas sin presentar en la primera pasada (AC, CS, DER, FAQ, ISO, PC, PIN, SMS,
  USB); presentadas. 0 hallazgos.
- Copias literales de RTVE y del común comparadas por script con su fichero de origen (sin las marcas
  de negrita y cursiva): todas idénticas.

## Copiado del común

De `temas/canal-sur-comun/10-proteccion-de-datos.md`, literal, sin tocar (verificación y refutación lo
saltan):

1. Epígrafe 1, «Si el puesto se infecta: el ransomware y la brecha»: el bloque entero *Violaciones de
   seguridad (artículos 33 y 34 del Reglamento).* (cuatro guiones), del apartado «Responsable y encargado
   del tratamiento» del común.
2. Epígrafe 1, «Cuando el operador entra en el equipo de otro»: el bloque *Artículo 87. Intimidad y uso de
   dispositivos digitales.* (apartados 1 a 3), del apartado «La garantía de los derechos digitales».

No se copiaron el art. 6.4 RGPD (cifrado y seudonimización) ni el art. 28 LOPDGDD que proponía la
investigación: el tema no los necesita para el enunciado.

## Copiado de RTVE sin cambios

Pasajes técnicos copiados palabra por palabra; sólo se han quitado las marcas de negrita y cursiva de
RTVE, porque en Canal Sur la negrita marca literalidad de fuente. Fuentes de RTVE marcadas
«actualizar: no».

De `gestion-administrativa/08-ofimatica.md`:
1. § 5.1: «Toda la seguridad de la información se ordena en tres propiedades…» con la lista de las tres
   (tema, epígrafe 1, «Las tres propiedades que se protegen»).
2. § 5.4: el párrafo «Contraseñas robustas y distintas por servicio; … contra el *phishing*.» (epígrafe 1,
   «Protección en el sistema operativo…»).

De `tecnica-informatica/21-la-seguridad-en-redes.md`:
3. § 1: cuadro Zona / Qué contiene / Quién llega (epígrafe 2, DMZ).
4. § 1: «La arquitectura clásica se monta con dos cortafuegos o con uno de tres patas… fabricantes
   distintos.»
5. § 4: «Qué hace un cortafuegos de aplicación web que los otros no pueden: … un guion incrustado en un
   formulario.»
6. § 4: cuadro Ataque / En qué consiste (cuatro filas) (epígrafe 2, «Los servicios de Internet»).
7. § 3: «Dónde se usa el aislamiento en la práctica: … antes de dejarlos pasar.»
8. § 3: «la máquina virtual aísla un sistema operativo entero; … a dos escalas.» (sin su arranque «Y el
   contraste con la virtualización del tema 17:», que se reescribió apuntando al tema 10).
9. § 5: la lista numerada 1-3 del orden de los cifrados (epígrafe 2, VPN).
10. § 5: «una red privada virtual protege el transporte, no el destino. Si el usuario visita un sitio
    malicioso a través del túnel, el túnel lo lleva igualmente.»
11. § 2: cuadro SAN / SNI y el párrafo «Para qué sirve cada una, con el caso que las explica: … un
    certificado por sitio.» (epígrafe 4).

De `tecnica-informatica/20-seguridad-de-la-informacion-iso-27000-e-itil.md`:
12. § 4: cuadro Familia / Cómo funciona / Ejemplos (epígrafe 3).
13. § 4: «El matiz sobre Diffie-Hellman, … con un algoritmo simétrico.»
14. § 4: «Y por qué en la práctica se usan las dos familias juntas: … para el resto de la sesión.» (sin la
    frase final que remite al tema 4 de RTVE).

De `tecnica-informatica/04-internet-origen-servicios-y-protocolos-seguros.md`:
15. § 4: cuadro Servicio / Protocolo / Puerto y el párrafo «El patrón que ordena toda la columna de la
    derecha: … por el puerto 22.» (epígrafe 2).
16. § 3: «HTTPS no es un protocolo distinto de HTTP: … conviene no confundirlas:», su cuadro de tres filas
    y «Lo que NO aporta, … millones lo tienen.» (epígrafe 2).
17. § 3: «Cómo funciona el certificado, en tres líneas: … todo va cifrado.» (epígrafe 4).

De `gestion-administrativa/01-gestion-administrativa.md`:
18. § 4.4: «Ni el formato ni el programa garantizan nada. … es un dibujo.» (epígrafe 6).

## Adaptado de RTVE (sí se verifica)

- `08-ofimatica` § 5.2: sólo las filas *Phishing*, *Pharming* y *Bulo* del cuadro de amenazas, con
  cabecera propia; troyano, *ransomware*, *spyware* y gusano se sustituyeron por definiciones con fuente.
  La explicación de *phishing* frente a *pharming* (que hablaba de «el examen») no se copió.
- `21` § 4: cuadro de tipos de cortafuegos, sin la marca ✔ de la respuesta oficial.
- `21` § 1: la regla «desde la zona perimetral no se puede iniciar una conexión hacia la red interna» y
  la ordenación de seguridad de la DMZ, reescritas sin la referencia a la pregunta 15.
- `21` § 5: el caso de la VPN en red abierta, reescrito sin la pregunta 77 ni sus opciones; conserva
  las frases «una red abierta no cifra nada» y el razonamiento.
- `01-gestion` § 4.4: el art. 10.2 de la Ley 39/2015 ya no se resume como en RTVE: se cita en su
  redacción vigente (letras a y b literales, c resumida, y 10.5).
- Quitado lo propio de RTVE: números de pregunta, «respuesta oficial», plantillas, remisiones a temas
  de RTVE (17, 20, 23, 4).

## Decisiones

- Organización por las tres rúbricas del enunciado, con la tercera partida en cinco epígrafes
  (criptografía; certificados y autoridades; sellado de tiempo; firma; FNMT) y uno final de aplicación
  práctica.
- Malware: definiciones del NIST (glosario y SP 800-83) para virus, gusano, troyano y *spyware*, y de
  Microsoft (castellano) para *adware*, *ransomware* y demás categorías. Se hace notar que Microsoft
  clasifica el *adware* como PUA y que «Las PUA no se consideran malware».
- Antivirus: Microsoft Defender (el del puesto Windows), con modos, servicios y `Get-MpComputerStatus`;
  ENS op.exp.6 como obligación del sector público.
- «Autoridad de certificación»: término técnico (NIST, RFC 5280); el legal es «prestador (cualificado) de
  servicios de confianza» (eIDAS 3.19-3.20). Se explica en el tema (salvedad 5 de la investigación).
- NIS2: sólo una línea en «Lo que este tema no da» (el enunciado no la nombra); no se citan las fuentes
  secundarias.
- Validez del certificado FNMT: sólo lo que dice la FAQ 1146 (AC FNMT Usuarios, hasta 31-12-2028). No se
  da el «cuatro años» (no confirmado).
- Formato `.pfx`/`.p12`: la investigación lo dejó sin fuente; confirmado en la FAQ 1553 de la FNMT.

## Salvedades detectadas en las fuentes (manda la fuente)

1. DMARC: la RFC 7489, que es la que citan los manuales, está obsoleta desde mayo de 2026 por la
   RFC 9989 (que **«obsoletes RFCs 7489 and 9091»**). El tema cita la 9989.
2. TLS 1.3: la RFC 8446 figura en `rfc-editor.org` como obsoleta por la RFC 9846. No afecta a este
   tema; avisar al redactor del tema 13.
3. eIDAS art. 3.19: el consolidado intercala la corrección de errores C2; la cita se da con el texto
   corregido y se avisa.
4. Ley 39/2015, art. 10.2, sigue diciendo «prestadores de servicios de certificación», terminología
   anterior al eIDAS; el tema lo señala.
5. Tema 6 (ya escrito) cita de Seguridad de Windows que Defender **«se deshabilita automáticamente
   cuando se instala un producto antivirus de terceros»**; la página de Defender dice que el modo pasivo
   sólo existe en equipos incorporados a Defender para punto de conexión. No es contradicción
   (deshabilitado frente a pasivo), pero el tema 14 da los tres modos para que se vea.
6. NIST SP 800-41 es de 2009 (Rev. 1, sin revisión posterior leída); se usa para conceptos estables
   (tipos de cortafuegos, «deny by default», DMZ).

## Ficheros tocados

- Creado: `temas/canal-sur-especificos/29-operador-a-informatico/14-seguridad-informatica-criptografia-y-proteccion-en-redes.md`.
- Creado: este informe.
- Añadidos: 57 ficheros `fuentes/canal-sur/informatico/web/s-*.txt`.
- `indice.py` sin argumentos se lanzó una vez por error sobre todos los temas de `portadas.tsv`: no
  cambió ningún fichero (comprobado con `git diff`).
- Temporales en el scratchpad (fuera del repositorio).

## Preguntas de control (10, tipo test) y comprobación con el tema

1. *Malware.* ¿Qué código malicioso se replica y se propaga por la red sin necesitar un programa
   anfitrión ni la intervención del usuario? a) Virus. b) Troyano. c) Gusano. d) *Adware*.
   — c). Epígrafe 1, cuadro de virus, gusanos y troyanos (definición NIST SP 800-28). **Entera.**
2. *Antivirus.* Microsoft Defender Antivirus en modo pasivo: a) no analiza ficheros; b) analiza y
   notifica, pero no neutraliza las amenazas; c) neutraliza sin notificar; d) es el antivirus principal.
   — b). Epígrafe 1, «El antivirus». **Entera.**
3. *Protección del SO / ENS.* En categoría básica, el ENS (op.exp.6) exige instalar software de
   protección frente a código dañino en: a) los servidores; b) los puestos de usuario; c) puestos de
   usuario, servidores y elementos perimetrales; d) sólo los elementos perimetrales.
   — c). Epígrafe 1, cita de op.exp.6.2. **Entera.**
4. *Seguridad perimetral, práctica.* Hay que publicar en Internet el servidor web de la cadena, que
   consulta una base de datos interna. Lo correcto: a) servidor y base de datos en la DMZ; b) servidor
   en la DMZ y base de datos en la red interna; c) ambos en la red interna con NAT; d) servidor en la red
   interna y base de datos en la DMZ. — b). Epígrafes 2 (cuadro de zonas) y 8 (caso). **Entera.**
5. *VPN.* Según el NIST (SP 800-77), la arquitectura de VPN que usa un teletrabajador para conectarse
   con la red de su organización es: a) pasarela a pasarela; b) acceso remoto o equipo a pasarela;
   c) equipo a equipo; d) malla. — b). Epígrafe 2, cuadro de arquitecturas. **Entera.**
6. *Correo.* ¿Qué mecanismo permite que un dominio autorice expresamente qué servidores pueden usar su
   nombre al enviar correo? a) DKIM. b) DMARC. c) SPF. d) S/MIME. — c). Epígrafe 2, cuadro de SPF, DKIM y
   DMARC. **Entera** (S/MIME no se trata; es distractor).
7. *Criptografía.* ¿Cuál es un algoritmo simétrico? a) RSA. b) ElGamal. c) AES. d) Diffie-Hellman.
   — c). Epígrafe 3, cuadro de familias y definición de AES. **Entera.**
8. *Autoridades de certificación.* En el Reglamento eIDAS, la entidad que expide certificados
   cualificados y a la que el organismo de supervisión ha concedido la cualificación se denomina:
   a) autoridad de certificación raíz; b) prestador cualificado de servicios de confianza; c) autoridad
   de registro; d) organismo de evaluación de la conformidad. — b). Epígrafe 4, art. 3.20. **Entera.**
9. *Sellado de tiempo.* Un sello cualificado de tiempo electrónico debe: a) basarse en una fuente de
   información temporal vinculada al Tiempo Universal Coordinado; b) expedirse por un notario; c) incluir
   el documento completo; d) renovarse cada cinco años. — a). Epígrafe 5, art. 42.1.b) (y la RFC 3161:
   se envía el resumen, no el documento). **Entera.**
10. *Firma electrónica y FNMT, práctica.* Un usuario obtuvo su certificado de la FNMT en software y
    quiere llevarlo a otro ordenador con capacidad de firmar. Debe: a) exportarlo sin clave privada en
    `.cer`; b) exportarlo con clave privada a un `.pfx` protegido con contraseña e importarlo en el otro
    equipo; c) volver a descargarlo con el código de solicitud en el equipo nuevo; d) copiar la carpeta
    del navegador. — b). Epígrafe 7 (FAQ 1063, 1551 y 1553; regla del mismo equipo y usuario) y caso del
    epígrafe 8. **Entera.**

Resultado: 10 de 10 contestadas enteras con el tema. Sin laguna; no hizo falta ampliar.
