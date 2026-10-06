# Puesto 29 · Tema 14 · Refutación (fase 4)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). No corrige: lista hallazgos para el remate.

Tema: `temas/canal-sur-especificos/29-operador-a-informatico/14-seguridad-informatica-criptografia-y-proteccion-en-redes.md`
(leído entero). Leídos además: `ENCARGO.md`, el enunciado del puesto 29, `29-T14-redaccion.md` y
`29-T14-verificacion.md`.

Fuentes releídas el 06-10-2026 (volcados del 05-10-2026 en `fuentes/canal-sur/informatico/web/` y del
BOE): Ley 6/2020 (BOE-A-2020-14046), arts. 4 a 7; Ley 39/2015, art. 10 con `boe.py precepto` (3
redacciones, vigente desde 30-06-2022); RD 311/2022 (BOE-A-2022-7191), art. 2.1 y anexo II (op.exp.6,
mp.eq.2, mp.com.1-2, mp.info.3-4, mp.s.1-2); eIDAS consolidado de 18-10-2024 (art. 3.16 a)-n), 28.4,
42.1); `s-ms-defender-antivirus`, `s-ms-criterios-malware`, `s-ms-prevenir-malware`,
`s-ms-ransomware-soporte`; `s-fnmt-obtener`, `-renovar`, `-anular`, `faq1146`, `faq1208`;
`s-nist-glos-hash-function`, `-pharming`; `s-nist-sp800-77r1`; `s-rfc3161`; `incibe-guia-ransomware`;
`nomoreransom-es`.

Saltado en exactitud (sí cuenta en cobertura): lo «Copiado del común» (arts. 33-34 RGPD y art. 87
LOPDGDD) y los 18 pasajes «Copiado de RTVE sin cambios» de `29-T14-redaccion.md`.

## Cobertura del enunciado

Las tres rúbricas y todos sus elementos tienen epígrafe propio: puesto de usuario, infección y
protección del SO, antivirus, malware, virus, gusanos, troyanos, *adware*, *spyware*, *ransomware*
(ep. 1); redes, correo, servicios de Internet, perímetro, acceso remoto, VPN, técnicas y mecanismos
(ep. 2); criptografía y algoritmos (3); certificados y autoridades (4); sellado de tiempo (5); firma
electrónica (6); instalación y administración de certificados y software de la FNMT (7). Sin rúbrica
del enunciado sin desarrollar.

## Hallazgos

| # | Gravedad | Error | Dónde | Qué pasa | Fuente |
|---|---|---|---|---|---|
| 1 | Grave | 6 / 9 | Ep. 7, «Renovar, revocar…», renovación | «no se renueva sin acreditar la identidad presencialmente en una oficina». La sede da tres vías: «presencialmente en una de nuestras Oficinas de Registro, mediante el servicio de Vídeo-Identificación o con la lectura de tu DNIe». Lo introdujo la verificación (su hallazgo 18) al precisar en exceso. Una pregunta con «sólo presencialmente» se fallaría (pregunta 13) | `s-fnmt-renovar.txt`, l. 145 |
| 2 | Menor | 6 | Ep. 2, «Los servicios de Internet», mp.s.2 | Presenta la letra d) como una de «las amenazas … que enumera el [mp.s.2.1]», sin la condición del apartado: «Cuando la información requiera control de acceso se garantizará la imposibilidad de acceder a la información obviando la autenticación, en particular, tomando medidas en los siguientes aspectos:». Además la frase repite «entre otras cosas, entre las amenazas», y queda mal construida | RD 311/2022, anexo II, mp.s.2.1 |
| 3 | Menor | 3 | Ep. 4, final de «Vigencia, revocación…» | «Son las tres vías que ofrece la FNMT: oficina, vídeo-identificación y DNIe», pero el ep. 7 (y la sede) da cuatro modalidades del certificado de ciudadano, con la «App Móvil». O se dice que son tres vías de identificación sin cerrar la lista, o se cuadra con el ep. 7 | `s-fnmt-obtener.txt` (menú) |
| 4 | Menor | 1 | Ep. 8, primer caso | Atribuye al perfil del «*adware* o de una aplicación potencialmente no deseada» las citas «Abra las ventanas del explorador sin autorización.» y «Redirigir el tráfico web…». En Microsoft son ejemplos de software que «presenta falta de control», dentro de los criterios del software no deseado, no de la categoría PUA ni del software de publicidad | `s-ms-criterios-malware.txt`, l. 75-78 y 114-118 |

## Lagunas (las preguntas no contestadas enteras)

| # | Pregunta | Qué falta | Fuente para ampliar |
|---|---|---|---|
| L1 | 10 y 11 | Las funciones resumen no tienen nombre (no aparecen SHA-1, SHA-2, SHA-3 ni MD5; «FIPS 180 and FIPS 202» no se explica). 3DES aparece como ejemplo de simétrico sin el aviso de que ya no debe usarse | `s-nist-sp800-77r1.txt`, l. 1108-1110 («Secure Hash Algorithm [SHA]: SHA-1 or the SHA-2 family … The SHA-3 family might be added in the future») y l. 2289 («3DES, MD5, SHA-1, and DH Groups 2 and 5 should not be used.»); l. 4083 (HMAC-MD5 nunca aprobado). Ya están en el repositorio |
| L2 | 7 | mp.eq.2.1 se cita sin nivel, justo tras lo que se exige «ya en categoría básica»: en nivel bajo «no aplica»; se exige desde el medio (de autenticidad), con R1 (cierre de sesiones) en el alto | RD 311/2022, anexo II, mp.eq.2 |

## Comprobado sin hallazgo (muestra)

Ley 6/2020, art. 4.2 (cinco años), 5.1 a)-i) y su resumen, 5.2, 6.1.a), 7.1, 7.2 (orden ministerial),
7.6 («podrá no ser exigible», cinco años); Ley 39/2015, art. 10.2 a)-c) (dos meses, garantía de a) y b)
en todos los procedimientos) y 10.5; ENS op.exp.6 (básica; R1+R2 media; R1-R4 alta), mp.com.1 (todas),
mp.com.2 (bajo; R1 medio), mp.info.3 (R1 desde el medio), mp.info.4 (sólo alto; 4.1, 4.3 y 4.4
literales), mp.s.1 (todas), art. 2.1; eIDAS 3.16 a)-n) (catorce), 28.4, 42.1.b); Defender (modo pasivo
y su condición); RFC 3161 *SHOULD*; *pharming* (SP 800-63-4); FNMT: oficinas con cita previa (AEAT,
Seguridad Social), anulación en línea, en oficina y 24x7, validez AC FNMT Usuarios hasta 31-12-2028,
FAQ 1208; INCIBE (apagar, no pagar) y No More Ransom.

## Preguntas

15 en `29-T14-preguntas.md`: 11 enteras, 1 a medias (10), 3 no (7, 11 y 13). La 13 falla por el
hallazgo 1, no por falta de contenido.

## Para el remate

Hallazgo 1, corregir con la sede. Hallazgos 2 a 4, pasajes. L1 y L2 amplían (Opus y fase 5 bis): L1
con un párrafo y quizá una fila en el cuadro de familias; L2 con una línea.

## Ficheros tocados

Creados: este informe y `29-T14-preguntas.md`. Ningún otro.
