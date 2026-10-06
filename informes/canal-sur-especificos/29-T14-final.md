# Puesto 29 · Tema 14 · Revisión del remate (fase 5 bis)

Fecha: 06-10-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/14-seguridad-informatica-criptografia-y-proteccion-en-redes.md`.
Alcance: sólo los pasajes listados en `29-T14-remate.md` (comprobados con `git diff HEAD`).

## Fuentes releídas (06-10-2026)

RD 311/2022 (`BOE-A-2022-7191.md`, mp.eq.2 y mp.s.2); `s-nist-sp800-77r1.txt` (l. 1078-1119, 2289-2291,
2540-2543, 4083); `s-nist-fips180-4.txt` (l. 51-58); `s-nist-fips202.txt`; `s-fnmt-renovar.txt` (l. 145);
`s-fnmt-obtener.txt` (menú); `s-ms-criterios-malware.txt` (Falta de control, PUA).

## Confirmado sin cambios

- H1 renovación FNMT: cita literal [sic] y condiciones; antecedente «esas tres vías» correcto.
- H2 mp.s.2: encabezado, mp.s.2.1 con su condición, d), 2.2 y 2.3 literales.
- L2 mp.eq.2: niveles y R1 literales.
- L1: cita «3DES, MD5, SHA-1, and DH Groups 2 and 5…», HMAC-MD5, fecha SP 800-77r1 (junio 2020),
  FIPS 180-4 (agosto 2015), lista SHA y 160-512 bits, «supplement…», siglas FIPS/HMAC/ECDH/CBC/GCM.

## Corregido (comprobado en la fuente)

| # | Pasaje | Error | Corrección |
|---|---|---|---|
| 1 | Ep. 3 «Los algoritmos», 3DES | 7 (dato superado): sólo la nota 7 «expected to be disallowed in the near future»; la misma SP 800-77r1, l. 2540, dice **«Triple DES has been deprecated since 2019 and will be disallowed after 2023.»** | Añadida esa cita; «Sobre MD5» → «Sobre HMAC-MD5» (la cita habla de HMAC-MD5) |
| 2 | Ep. 3, cuadro FIPS 202 | 6 (salvedad): la frase citada sigue con dos XOF (SHAKE128, SHAKE256) | Añadido que la frase sigue con ellas y que no son funciones resumen |
| 3 | Ep. 1, tras [mp.eq.2.1] | Redacción equívoca: «no se exige ya en lo básico» confunde con «Categoría BÁSICA» | «no se aplica por categoría, sino por el nivel de la dimensión de autenticidad», con el rótulo literal «Aplicación de la medida (por autenticidad).» |
| 4 | Ep. 4, final | 9: afirmaba que sólo tres modalidades «responden a vías de identificación» (lo de la App Móvil no consta) | «tres llevan en su nombre la vía de identificación», verificable en el menú |
| 5 | Ep. 8, primer caso | 9: el cambio de página de inicio atribuido a «Falta de control»; la lista de Microsoft no lo nombra | Falta de control → ventanas y redirección; se dice que el cambio de página de inicio no figura con ese nombre |
| 6 | Siglas | Coordinación rota («; y CBC y GCM dos modos…; el nombre…») | «; CBC y GCM, dos modos…» |

## Lentes

`refutar_prosa.py`: 0 hallazgos. `negritas.py` (ENS, SP 800-77r1, FIPS 180-4/202, Microsoft, FNMT):
todas las negritas del remate y las nuevas, literales (las «no está» son de fuentes no pasadas, ajenas).
Extensión: 16.777 por `wc -w`; la cifra de portada (16.200, de `indice.py`) se deja.

## Ficheros tocados

El tema y este informe.
