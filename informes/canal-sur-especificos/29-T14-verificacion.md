# Puesto 29 · Tema 14 · Verificación (fase 3)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Fuentes releídas el 06-10-2026 en los volcados de
`fuentes/canal-sur/informatico/web/` (`s-*.txt`, `incibe-guia-ransomware.txt`, `nomoreransom-es.txt`),
descargados el 05-10-2026 con URL y fecha en cabecera, y en los volcados del BOE (BOE-A-2020-14046,
BOE-A-2015-10565 con `boe.py precepto` art. 10, 3 redacciones, vigente desde 30-06-2022; BOE-A-2022-7191).
Descargado nuevo: `s-nist-glos-pharming.txt` (csrc.nist.gov/glossary/term/pharming, 06-10-2026).
Búsqueda en el BOE (`boe_buscar.py`) de una ley de transposición de NIS2, 06-10-2026: sin resultados.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/14-seguridad-informatica-criptografia-y-proteccion-en-redes.md`.

## Método

- **Copiado del común** (art. 33-34 RGPD y art. 87 LOPDGDD, de `canal-sur-comun/10`): no se re-verificó;
  cotejo por script normalizado: literal.
- **Copiado de RTVE sin cambios** (18 pasajes de `29-T14-redaccion.md`): no se re-verificó; cotejo por
  script contra `gestion-administrativa/08` y `/01` y `tecnica-informatica/04`, `/20` y `/21`: todos
  literales. Tres llevaban la marca ✔ de «respuesta oficial» de RTVE (cuadro de zonas de la DMZ, cuadro
  de familias criptográficas, cuadro SAN/SNI): se quitó la marca, que es propia de RTVE; nada más.
- Todo lo demás (lo adaptado de RTVE y lo nuevo) se verificó: cada una de las 289 negritas se localizó
  por script en su fuente y se leyó en contexto, comprobando la atribución (glosario y publicación de
  origen del NIST, artículo y apartado, medida y nivel del ENS); y se comprobó lo dicho en redonda. Con los
  nueve errores delante.
- Lentes (el tema cita normas): `negritas.py` 289 cotejadas, 1 «no está» (art. 3.19 eIDAS, marca ►C2◄
  del consolidado; ya declarado). `refutar_exactitud.py` con los tres volcados del BOE: 5 avisos falsos
  (citas del eIDAS y de la FNMT con número entre paréntesis), comprobados a mano. `refutar_modo.py`: 0.
  `refutar_prosa.py`: 0. `indice.py` sobre el tema: 45 epígrafes, el índice no cambia (15.511 palabras).

## Hallazgos y correcciones (todas aplicadas, cada una comprobada en su fuente)

| # | Error | Dónde | Qué pasaba | Corrección |
|---|---|---|---|---|
| 1 | 9 | § 1, otras categorías | El malware sin archivos «no deja un ejecutable en disco» y Defender «sólo» lo para por comportamiento: la página de Microsoft dice que no hay definición única (tipo III usa ficheros) y cita AMSI, supervisión del comportamiento, examen de memoria y del sector de arranque | «no se apoya, o no del todo, en ficheros» y «puede detener por su comportamiento aunque ya se esté ejecutando» |
| 2 | 1 | § 1, virus/gusanos/troyanos | «En castellano, de Microsoft:» encabezaba una lista cuyo primer punto es el NIST en inglés | «Lo que añaden la guía de malware del NIST y Microsoft (esta, en castellano)» |
| 3 | 9 / 3 | § 1, cuadro de engaños (adaptado de RTVE) | *Pharming* y bulo sin fuente; «Dos formas» con tres filas | *Pharming* con cita del NIST (SP 800-63-4, glosario; descargado); bulo quitado (sin fuente); *phishing* ajustado a la definición del NIST (correo o sitio web; no SMS) |
| 4 | 9 / 6 | § 2, cuadro de cortafuegos (adaptado) | «De aplicación (WAF)» mezclaba dos tipos que la SP 800-41 separa (2.1.3 y 2.1.9) | Dos filas: de aplicación (protocolo: adjunto ejecutable, orden FTP) y de aplicación web (HTTP, delante del servidor web) |
| 5 | 1 | § 2, servicios de Internet | La letra «d)» de mp.s.2 sin decir que es de mp.s.2.1 | Precisado |
| 6 | 4 | § 3, hash | «Las aprobadas deben cumplir»: el NIST dice *are designed to satisfy* | «están diseñadas para cumplir» |
| 7 | 9 | § 3, firma | «como dice la definición del NIST» que se firma con la privada: la definición sólo separa la clave que firma de la que verifica | Reescrito |
| 8 | 9 | § 4, PKI | RA «en la práctica, la que comprueba la identidad» y «las oficinas de acreditación de la FNMT hacen el papel de autoridad de registro»: ni la RFC 5280 ni la FNMT lo dicen | Quitado de la cita; la equivalencia queda como lectura de oficio, declarada |
| 9 | 9 | § 4, término legal | «La Ley 39/2015 todavía dice "prestadores de servicios de certificación"»: lo dice dentro del nombre de la lista | «remite a la "Lista de confianza de prestadores de servicios de certificación"» |
| 10 | 6 | § 4, identificación | Art. 7.2 Ley 6/2020 «abre» la identificación a distancia: remite a una orden ministerial | Precisado |
| 11 | 4 | § 4, identificación | Art. 7.6 «dispensa»: el texto dice «podrá no ser exigible» | Precisado con la cita |
| 12 | 4 | § 5, RFC 3161 | *SHOULD* traducido «debe» | «debería», con la aclaración |
| 13 | 3 | § 5, ENS mp.info.4 | «con estas cautelas» y se daban tres de cuatro (falta 4.2) | «entre sus cautelas» |
| 14 | 6 | § 6, Ley 39/2015 art. 10.2.c) | Faltaban los dos meses previos a la eficacia y la garantía de a) y b) en todos los procedimientos | Añadidos |
| 15 | 6 | § 6, ENS mp.info.3 | R1 (certificados cualificados) sin nivel | «desde el nivel medio» |
| 16 | 9 | § 6, FNMT | «el de representante de empresa»: la sede no usa ese nombre | Los de empresa con los rótulos de la sede |
| 17 | 9 | § 7, soportes | «Tarjeta o USB criptográficos (y el DNIe)», «la clave se genera dentro del chip»: la FAQ 1208 sólo dice que en tarjeta no se exporta | «Tarjeta criptográfica»; «se obtiene en la tarjeta y su clave privada no sale de ella» |
| 18 | 6 | § 7, renovación | «hay que volver a acreditar la identidad»: la sede dice presencialmente en una oficina | Precisado |
| 19 | — | Trazabilidad | Faltaban *pharming* y su fecha, y las nuevas notas de oficio | Añadidos |

## Confirmado sin cambios (muestra de lo comprobado en redonda o por atribución)

Glosario NIST: malware (SP 800-128), virus (SP 800-82r3 de RFC 4949), gusano y troyano (SP 800-28),
*spyware* (SP 800-128 de CNSSI 4009-2022), DMZ (CNSSI 4009-2022 y SP 800-41), VPN (RFC 4949), AES (FIPS
197); tareas de los troyanos; ENS op.exp.6 (básica; R1-R2 media; R3-R4 alta, y su contenido), mp.eq.2.1,
mp.com.1 (todas), mp.com.2 (bajo; R1 medio), mp.com.3.1, mp.s.1 (todas, con 1.3-1.5 y 1.6-1.7 bien
encuadrados), mp.info.4 (sólo alto), art. 2.1; servicios y procesos de Defender, `Get-MpComputerStatus`
y `AMRunningMode`; capas del filtrado de paquetes y de la inspección con estado; SP 800-46 (cuatro
formas) y SP 800-77 Rev. 1 (junio de 2020; AH no recomendado); RFC 9989 (mayo de 2026, obsoleta la 7489
de marzo de 2015); SPF en registro TXT del DNS; eIDAS 3.9-3.38 (numeración), 3.16 a)-n) (14, por el
Reglamento 2024/1183), 22.1-2, 25, 26, 28.4, 41, 42.1, anexos I, III y IV; Ley 6/2020 arts. 4, 5.1 (nueve
supuestos y su resumen), 5.2, 6.1.a), 7.1; Ley 39/2015 art. 10.2 y 10.5; FNMT: modalidades, cuatro pasos,
oficinas con cita previa (AEAT, Seguridad Social), navegadores, precauciones, instalable de tarjeta (32 y
64 bits, cerrar navegadores, administrador), utilidades (1.4.0.8), MultiCard, `certlm.msc` y
`certmgr.msc`, exportación (FAQ 1551, formato por defecto), formatos (FAQ 1553), renovación (60 días,
tres pasos), anulación (servicio telefónico 24x7 con código de solicitud), validez AC FNMT Usuarios.

## Lo que no se pudo confirmar

Quitado: la fila del bulo o *hoax* (sin definición en ninguna fuente leída). Declarado como oficio: la
equivalencia oficina de acreditación = autoridad de registro. Sigue sin fuente, y así lo declara la
Trazabilidad, el resto del oficio que listó la redacción.

## Pasajes cambiados

Los 19 de la tabla y las tres marcas ✔. Releídos: «según la definición del NIST de arriba» (la de
*phishing* está justo antes), «Dos formas» (ahora dos filas), «esta, en castellano», «entre las amenazas
… que enumera el [mp.s.2.1]», «el 7.6», «esa comunicación» tienen su antecedente delante.

## Ficheros tocados

- Modificado: el tema 14.
- Creados: este informe y `fuentes/canal-sur/informatico/web/s-nist-glos-pharming.txt`.
- `indice.py` sin argumentos se lanzó una vez por error: el puesto 29 no está en `portadas.tsv` y
  `git status` no muestra ficheros versionados modificados; ningún otro tema del puesto cambió de fecha.
- Temporales en el scratchpad.
