# Puesto 29 · Tema 14 · Remate (fase 5)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/14-seguridad-informatica-criptografia-y-proteccion-en-redes.md`.
Entrada: `29-T14-refutacion.md` (1 hallazgo grave, 3 menores, 2 lagunas) y `29-T14-preguntas.md` (11 / 1 / 3).

## Fuentes

- Releídas el 06-10-2026 en sus volcados: `s-fnmt-renovar.txt` (l. 145), `s-fnmt-obtener.txt` (menú,
  l. 23-39), `s-ms-criterios-malware.txt` (l. 56-78 y 114-118), `s-nist-sp800-77r1.txt` (l. 1080-1110,
  2289-2291, 4083-4084), `s-nist-glos-hash-function.txt`; RD 311/2022 (`BOE-A-2022-7191.md`, anexo II,
  mp.eq.2 l. 1794-1806 y mp.s.2 l. 2161-2173).
- Descargadas y leídas el 06-10-2026 (nuevas, en `fuentes/canal-sur/informatico/web/`):
  `s-nist-fips180-4.txt` (PDF del FIPS 180-4, pasado con `documento.py texto`) y `s-nist-fips202.txt`
  (resumen de la página del FIPS 202 en csrc.nist.gov). Hacían falta porque la SP 800-77 nombra SHA-1 y
  SHA-2 pero no SHA-256 ni SHA-3, y el glosario sólo da los números de las normas.

Todas las correcciones del informe se confirmaron en la fuente; ninguna resultó equivocada.

## Hallazgos de exactitud

| # | Pasaje cambiado | Antes | Después |
|---|---|---|---|
| 1 | Ep. 7, «Renovar, revocar…», renovación | «no se renueva sin acreditar la identidad presencialmente en una oficina» | Cita literal de la sede con las tres vías (oficina de registro, vídeo-identificación, lectura del DNIe) [sic por «tú identidad»] y que se pide de nuevo como primera obtención |
| 2 | Ep. 2, «Los servicios de Internet», mp.s.2 | d) presentada como amenaza «que enumera el [mp.s.2.1]», sin condición; frase repetida | Encabezado literal («deberán ser protegidos frente a las siguientes amenazas»), mp.s.2.1 entero con su condición de control de acceso, d) como uno de sus aspectos; mp.s.2.2 y 2.3 «no llevan condición» |
| 3 | Ep. 4, final de «Vigencia, revocación…» | «Son las tres vías que ofrece la FNMT: oficina, vídeo-identificación y DNIe» | De las cuatro modalidades (ep. 7), tres responden a vías de identificación; la cuarta es la «App Móvil» |
| 4 | Ep. 8, primer caso | Ventanas y redirección atribuidas al perfil del *adware*/PUA | Anuncios → *adware* (cita de la categoría PUA «Software de publicidad»); ventanas y redirección → software no deseado por «Falta de control», con las dos citas [sic] |

## Lagunas (se amplía el tema)

| # | Pasaje añadido | Contenido |
|---|---|---|
| L1 | Ep. 3, «Los algoritmos», párrafo nuevo al final | 3DES «deprecated» (nota 7 de la SP 800-77r1); cita «3DES, MD5, SHA-1, and DH Groups 2 and 5 should not be used…» con lo que la sustituye; HMAC-MD5 nunca aprobado; salvedad: el aviso es para IPsec |
| L1 | Ep. 3, cuadro de familias, fila simétrica | «3DES (ya no debe usarse; véase "Los algoritmos")» |
| L1 | Ep. 3, «Las funciones resumen», tras «FIPS 180 and FIPS 202» | Cuadro FIPS 180-4 (SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, SHA-512/256) y FIPS 202 (SHA3-224/256/384/512), citas literales; longitud de 160 a 512 bits; SHA-3 complementa a SHA-1 y SHA-2; MD5 fuera de ambas |
| L2 | Ep. 1, tras la cita de [mp.eq.2.1] | Aplicación por autenticidad: «Nivel BAJO: no aplica.», «Nivel MEDIO: mp.eq.2.», «Nivel ALTO: mp.eq.2 + R1.», y la cita de R1 (cierre de sesiones) |

## Otros pasajes tocados

- Portada: «Fuente» añade FIPS 180-4 y 202; «Redacción» da su fecha de lectura (06-10-2026);
  «Extensión» 15.700 → 16.200 palabras (`indice.py`: 16.238).
- Siglas: SHA, MD5, FIPS, DH, ECDH, HMAC, CBC y GCM (expansiones tomadas de la SP 800-77r1, l. 1083,
  1093-1094, 1119).
- «Qué se puede preguntar»: añade cuáles son las SHA y qué algoritmos ya no deben usarse.
- «Lo que este tema no da»: del FIPS 180-4 y 202 sólo se leyó qué funciones definen y la longitud;
  la SP 800-131A (lista general de algoritmos admitidos o retirados) no se leyó.
- Trazabilidad: frase de fechas; fila nueva FIPS 180-4 / FIPS 202; fila SP 800-77 añade los algoritmos
  que no deben usarse en IPsec.

Antecedentes revisados: «Ésta» (L2) remite a la medida [mp.eq.2.1] citada justo antes; «esas tres
vías» (H1) a la cita que las enumera; «(epígrafe 7)» (H3) y «("Los algoritmos")» apuntan a epígrafes
existentes.

## Lentes

- `indice.py` (sobre el tema): 45 epígrafes, sin epígrafes nuevos; índice idéntico al anterior. Una
  primera llamada sin argumento recorrió todos los temas del .tsv; es regenerable y no alteró temas
  fuera del puesto 29 (comprobado con `git status`).
- `negritas.py` (ENS, Ley 6/2020, Ley 39/2015 y todos los volcados web): 305 cotejadas; 5 no halladas,
  todas previas y ajenas al remate (RGPD/LOPDGDD copiados del común y una definición del eIDAS, cuyas
  fuentes no se pasaron). Todas las negritas nuevas, literales.
- `refutar_exactitud.py` y `refutar_modo.py` con el RD 311/2022: 0 hallazgos en pasajes del remate (las
  5 citas «no literales» de exactitud son del eIDAS y la FNMT, ajenas a la fuente dada).
- `refutar_prosa.py`: 0 hallazgos (un primer paso señaló SHA, ECDH y HMAC sin presentar; corregido en
  las siglas).

Preguntas 7, 10, 11 y 13 tienen ya respuesta entera en el tema.

## Ficheros tocados

El tema; este informe; dos volcados nuevos en `fuentes/canal-sur/informatico/web/`
(`s-nist-fips180-4.txt`, `s-nist-fips202.txt`).
