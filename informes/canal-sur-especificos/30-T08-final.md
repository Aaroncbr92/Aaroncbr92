# Puesto 30 · Tema 8 · Fase 5 bis (revisión de los pasajes del remate)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Revisor distinto del rematador.
Alcance: sólo los 8 pasajes listados en `30-T08-remate.md` (diff del tema frente a b08a902).

## Fuentes releídas (25-09-2026)

`fuentes/canal-sur/montador/web/`: `rfc9043.txt` (resumen, § 1, § 4.2.16 «ec», § 4.9.3), `rfc9559.txt`
(cabecera y resumen), `loc-fdd000341.txt` (líneas 95, 115, 224), `loc-fdd000206.txt`, `jpeg-about.txt`;
`resolve21-extractos/tape.txt` (l. 149-151, p. 562). Nueva: `iasa-home.txt` (iasa-web.org, 25-09-2026).

## Comprobado sin cambios

- Las siete negritas nuevas: literales (RFC 9043 ×3, RFC 9559, LoC FFV1 ×2, LoC RDD 48).
- RFC 9043 «Informational», agosto de 2021; RFC 9559 «Standards Track», octubre de 2024.
- IASA-TC 06 de 2018 y clases 1-3 (analógico digitalizado, cintas digitales): ficha LoC fdd000341.
- ST 422 «available from SMPTE for purchase»: «de pago» correcto. Sigla JPEG: jpeg.org l. 57.
- Cálculo: 3.600 × 24 = 86.400; 3.600 × 25 = 90.000 → 00090000. Ejemplo literal de p. 562.
- Pasajes 4-8 (portada, qué se puede preguntar, tablas, huecos, trazabilidad): coherentes.

## Corregido (comprobado en la fuente)

1. **«cuadro a cuadro» (error 9)**: el RFC 9043 § 4.2.16 dice que el CRC de 32 bits va siempre en el
   registro de configuración y, con `ec = 1`, también en cada *slice*. Se sustituye por eso.
2. **Sigla IASA sin fuente (error 9)**: el desarrollo no constaba en ninguna fuente guardada; confirmado
   en iasa-web.org y añadido a «Documentos técnicos» y «Trazabilidad».
3. **Antecedentes**: «lo clasifica así» (el «lo» apuntaba a Matroska, la cita habla de FFV1 en
   Matroska) → «clasifica la combinación así, en su ficha del FFV1»; «su misma ficha» → «esa misma
   ficha»; «La ficha de la Biblioteca» (ambigua tras citar la del FFV1) → «Otra ficha…, la de esta
   combinación».

## Lentes

`indice.py`: 11.893 palabras, 45 epígrafes. `refutar_prosa.py`: 1 hallazgo, el mismo previo (referencia
del convenio en su sitio). Sin norma jurídica: no proceden las demás.

## Ficheros tocados

El tema 8; este informe; nuevo `fuentes/canal-sur/montador/web/iasa-home.txt`.
