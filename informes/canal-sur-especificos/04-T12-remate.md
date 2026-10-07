# 04 · Ayudante de Producción · Tema 12 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/12-documentacion-internacional-para-desplazamientos.md`.
Rematado el 06-10-2026 (el «hoy» del encargo es el 24-09-2026) con `04-T12-refutacion.md` (0 graves,
4 menores, 3 lagunas) y `04-T12-preguntas.md` (11 enteras, 1 a medias, 3 no).

**Resultado: se amplió el tema** (lagunas L1-L3 cubiertas con fuente; M1-M4 aplicados). De 7.745 a
8.792 palabras de cuerpo; 30 epígrafes (uno nuevo). La extensión de la portada pasa de 7.500 a 8.800.

## Cada corrección, comprobada en la fuente antes de aplicarla (leídas el 06-10-2026)

| Hallazgo | Fuente releída | ¿El informe acertaba? | Aplicado |
|---|---|---|---|
| M1 · anexo A, art. 7 | BOE-A-1997-21711, volcado `fuentes/corte-20221221/`, línea 462 (dentro del anexo A, líneas 392-568) | Sí, literal | Sí |
| M2 · art. 39 del convenio | `x-convenio-rtva-boja-240-2014.txt`, línea 1272: «Durante la vigencia del presente Convenio Colectivo se procederá…» | Sí | Sí |
| M3 · desarrollo de ATA | Ni el Convenio ni la ficha de la Cámara desarrollan la sigla (grep sin resultados) | Sí | Sí: quitado el desarrollo |
| M4 · art. 24.4 y anexo C, art. 1 | Línea 288 (24.4) y anexo C, art. 1 a) («vehículo de carretera dotado de motor») | Sí | Sí: en portada y «Normativa» |
| L1 · UE, territorio único | Art. 18.1 (línea 224) y anexo III, notificación (línea 1646) | Sí, literales. La consecuencia práctica no se encontró en fuente aduanera (la Cámara no dice nada de la UE) | Base del Convenio añadida; el hueco se mantiene, declarado |
| L2 · vehículo y conductor | DGT, Sede Electrónica, «Solicitud del permiso internacional»; OFESAUTO, «Certificado Internacional de Seguro: Carta Verde» | — | Párrafos nuevos. Quién expide el CPD en España: no encontrado, declarado |
| L3 · vacunación | Ministerio de Sanidad, «Certificado Internacional de Vacunación o Profilaxis» y FAQ de los Centros de Vacunación Internacional | — | Epígrafe nuevo |

Nota sobre OFESAUTO: no es un organismo público sino la oficina nacional de las aseguradoras en el
sistema internacional del certificado; el tema lo dice así en la Trazabilidad. Las URL de Sanidad
«vacunacionInternacional.htm» y de dgt.es dieron 404; la de la DGSFP, certificado caducado (no se
desactivó la verificación).

## Pasajes cambiados

1. **Portada, «Fuente»**: añadidos los arts. 18 y 24.4 del Convenio, el art. 7 del anexo A, el art. 1
   del anexo de medios de transporte, las notificaciones de la Comunidad, la DGT, Sanidad y OFESAUTO.
   **«Extensión»**: 8.800.
2. **Siglas**: ATA, sin el desarrollo inglés/francés («nombre que le da la Cámara de Comercio de España,
   que no desarrolla la sigla»); nuevas DGT, CIS, OFESAUTO y OMS.
3. **«Qué se puede preguntar»**: límite de la validez sobre la reexportación, la UE como territorio
   único, permiso y seguro del vehículo, certificado de vacunación.
4. **«Dentro y fuera de la UE»**, tabla: fila «Material» con el art. 18; fila «Asistencia sanitaria» con
   el certificado de vacunación; fila nueva «Conducir el vehículo».
5. **«Cuánto dura»**: párrafo nuevo con el art. 7 del anexo A y su consecuencia (M1).
6. **«El material profesional…»**: la cita del CPD lleva ya su artículo (anexo C, art. 1 a); dos
   párrafos nuevos: permiso de conducción (DGT) y prueba de seguro (CIS o seguro de frontera,
   OFESAUTO), con la consecuencia de oficio para una UM que pasa a Marruecos (L2).
7. **«En qué territorios sirve»**: párrafo nuevo con el art. 18.1 y la notificación del anexo III; la
   consecuencia práctica, declarada como no leída (L1).
8. **«Seguro, Registro de viajeros…»**: la cita del art. 39 empieza en «Durante la vigencia del
   presente Convenio Colectivo» (M2).
9. **Epígrafe nuevo «El certificado internacional de vacunación»** (antes de «Dietas y viaje»): qué es,
   dónde se obtiene, fiebre amarilla, inglés o francés, validez de por vida, requisito de entrada,
   4-6 semanas de antelación (L3).
10. **«Paso a paso»**, fila «En cuanto se decide el viaje»: vacunas en la ficha del MAEC y cita en un
    Centro de Vacunación Internacional; permiso internacional y CIS si va un vehículo.
11. **Supuesto 1**, punto 3: la base del art. 18 y anexo III, con el hueco declarado.
12. **«Normativa que el tema invoca»**: fila del Convenio con arts. 18.1 y 24.4, art. 7 del anexo A,
    anexo C art. 1 a) y anexos II y III.
13. **«Lo que este tema no da»**: la línea del cuaderno entre Estados de la UE, reescrita; nuevas: quién
    expide el CPD en España y otros papeles del vehículo; qué países exigen vacunas hoy.
14. **«Trazabilidad»**: anexo A, arts. 1 a 7; arts. 18 y 24.4; nueva línea con DGT, Sanidad y OFESAUTO.

Releídos los pasajes cambiados: «Y los une el artículo 7 del anexo A», «esos centros», «esas fuentes»
y «la Comunidad lo notificó así» tienen su antecedente delante.

## Lentes

- `indice.py`: índice regenerado, 30 epígrafes; el tema no tiene fila en `portadas.tsv` (portada a mano).
- `negritas.py` (Convenio, convenio RTVA, Cámara, DGT, Sanidad, OFESAUTO): todas las negritas nuevas se
  encuentran literales. Las «NO ESTÁ» restantes son de fuentes no pasadas (RD 896/2003, reglamentos UE,
  PAG, TSE, MAEC, GOV.UK) y ya estaban. El aviso «¿art. 8? Por cadena de garantía» es falso positivo
  previo (la definición menciona el artículo 8; está en el art. 1).
- `refutar_exactitud.py` (Convenio): 14 «no literales», los mismos que antes del remate (citas de otras
  normas). Un 15.º que introdujo el paréntesis «(artículo 1, letra a)» junto a una negrita del
  apéndice I se resolvió reescribiendo la frase.
- `refutar_modo.py` (Convenio): 0 hallazgos.
- `refutar_prosa.py`: OMS sin presentar → añadida a las siglas. Queda CPD, falso positivo (la sigla se
  presenta como «sin desarrollar»). Una frase repetida («X Convenio Colectivo de la RTVA, BOJA núm.»), entre «Normativa» y «Trazabilidad», ya estaba y es nombre de fuente: no se toca.

## Preguntas tras el remate

4 (art. 7): ahora entera. 7 (vacunación): entera. 13 (Sevilla-Roma): a medias, con la base del
Convenio y el hueco práctico declarado. 14 (UM a Marruecos): entera en conducción y seguro; el
emisor del CPD queda declarado como hueco.

## Ficheros tocados

- El tema.
- `fuentes/institucionales/`: copias nuevas `DGT_permiso-internacional.txt`,
  `Sanidad_certificado-internacional-vacunacion.txt`, `Sanidad_vacunacion-internacional-faq.txt`,
  `OFESAUTO_carta-verde.txt`, y sus cuatro filas en `README.md`.
- Este informe.

Pasa a 5 bis (revisión de los pasajes cambiados) porque el remate amplió.
