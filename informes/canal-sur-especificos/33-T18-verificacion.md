# Realizador/a (puesto 33) · Tema 18 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/33-realizador-a/18-seguridad-comunicacion-coordinacion-presion.md`
(11.588 palabras según `indice.py`, 39 epígrafes). Fecha de trabajo: 24-09-2026 (fecha del encargo;
fecha del sistema, 29-09-2026). Copia previa: `33t18-antes-verif.md` en el scratchpad.

## Copiado del común: sólo literalidad

Los ocho bloques que lista `33-T18-redaccion.md` («Copiado del común», del tema 32-14) se compararon
por script con el 32-14, normalizando los espacios (el tema los parte en otras líneas). Los ocho son
subcadena exacta: LE 5.6; viñeta «La instalación eléctrica (apartado 12)»; artículo 20 de la LPRL;
NBA 3.3; riesgo grave e inminente, del «Es el concepto…» al «…consultar.»; artículo 29 y responsable
preventivo, hasta «(apartado 3.3.3.c de la Norma).»; artículos 24.1 y 24.2; estrés (introducción,
NTP 318 y NTP 443). No se re-verificaron. «Copiado de RTVE sin cambios»: nada.

## Fuentes releídas (todo lo demás)

| Fuente | Fichero | Leída |
| --- | --- | --- |
| RD 1680/2011: arts. 4, 5 (d, e, g, k, l, m, n), 9 (p, q, r); 0905 RA 1.f, 3.a, 3.e, 3.f, 4.a, 4.c-4.f; 0909 RA 1.c, 1.e, 2.a-2.e, 4.b, 4.e-4.g, 5.c-5.e; «Referencias posteriores» | `fuentes/canal-sur/realizador/BOE-A-2011-19599.txt` | 24-09-2026 |
| RD 500/2024, art. 7 (anexo I: sólo suprime FOL, EIE y FCT, añade módulos nuevos y renombra «Proyecto») y art. 8 (anexo III) | `fuentes/canal-sur/realizador/BOE-A-2024-10685.txt` | 24-09-2026 |
| RD 1085/2020, disposición derogatoria única (la «SE DEROGA el anexo indicado» del RD 1680/2011 es el de convalidaciones, no el de módulos) | `boe.py precepto BOE-A-2020-17274 dd` | 24-09-2026 |
| IMS077_3: RP5 (CR5.2 a CR5.6); MF0217_3 CE1.5, CE1.9, CE2.3, CE2.5, otras capacidades | `fuentes/canal-sur/realizador/incual-IMS077_3.txt` | 24-09-2026 |
| Convenio: fichas 5351000 (p. 196; cinco tareas; no nombra seguridad) y 5353000 (p. 111); índice de artículos 25 a 31 | `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt` | 24-09-2026 |
| LE: portada (1.ª ed., marzo 2004), intro cap. 4, 4.4.4 (1, 3, 4, 6), 5.6, 6.1, 6.5, 6.5.1, 6.5.2, 8.1 (6, 7, 9) | `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt` | 24-09-2026 |
| RD 486/1997, anexo I (redacción BOE-A-2004-19311, desde 03-12-2004), 10.8.º; parte B no excluye 10 ni 12 | `fuentes/canal-sur/BOE-A-1997-8669.md` | 24-09-2026 |
| NBA: nota de derogación por RD 524/2023 y aplicación transitoria | `fuentes/canal-sur/BOE-A-2007-6237.md` | 24-09-2026 |
| LPRL 15.1.g (por la negrita atribuida) | `fuentes/canal-sur/BOE-A-1995-24292.md` | 24-09-2026 |
| NTP 685 (año 2003, autores) y NTP 438 (año 1995, autores) | scratchpad `rz/ntp685.txt`, `rz/ntp438c.txt` | 29-09-2026 |
| Clear-Com, «Interruptible Fold Back, AKA IFB» (16-03-2021) | `fuentes/canal-sur/sonido/fabricantes/clearcom-ifb-2021.txt` | 29-09-2026 |

Lentes: `negritas.py` con las 13 fuentes: 216 negritas; 9 «no están», todas rótulos (21.1…29.3,
24.1, 24.2, «El estrés (NTP 318, 1991)»); 1 «atribuida a otro artículo» (la cita del 21.2 que remite
al 14.1: correcta y copiada). `refutar_exactitud.py` (LPRL, RD 486/1997, NBA, RD 171/2004): 29 «no
literales», todas falsas alarmas, porque toma «(6.5)», «(8.1, punto 6)» o «artículo 5.k» del LE o del RD
1680/2011 como artículos de la LPRL; las negritas se cotejaron con su fuente real. `refutar_modo.py`: 0.
`refutar_prosa.py`: 0 (tras quitar «AKA» del título en la trazabilidad). `indice.py`: 39 epígrafes,
índice sin cambios.

## Correcciones aplicadas

1. Línea suelta duplicada en «El plató, un lugar de trabajo» («gradas del público y los cables no
   pueden estrecharlas ni cerrarlas.»), resto de una edición: quitada.
2. Error 3. «Advertencia»: «cuatro tipos de texto» → «cinco» (LPRL, RD 1680/2011, IMS077_3, textos
   de la casa y NTP).
3. Error 9. Artículo 4 del RD 1680/2011: «incluye realizar proyectos audiovisuales» no es lo que dice;
   ahora «consiste en organizar y supervisar la preparación, realización y montaje de proyectos
   audiovisuales filmados, grabados o en directo, así como en regir los procesos técnicos y artísticos
   de espectáculos en vivo y eventos», antes de la negrita.
4. Error 6. NTP 438, comunicación horizontal: se añade su salvedad literal («aunque en las
   organizaciones muy burocratizadas…»).
5. Error 4. NTP 438: «recomienda» el estilo democrático → «considera que se requiere» (la nota dice
   «se requiere»).
6. Error 5. Siglas: se presenta el BOE.
7. Error 9. IFB: el desarrollo de la sigla («Interruptible Fold Back») ahora se atribuye a Clear-Com y
   la fuente se añade a «Trazabilidad».
8. Trazabilidad y portada: IMS077_3 «CR5.1 a CR5.6» → «CR5.2 a CR5.6» (el CR5.1 no se cita);
   «actualización por Orden PCI/797/2019» → «publicación: Orden PCI/797/2019» (así lo da el INCUAL);
   convenio «artículos 25 a 31» → «25, 26, 27 y 31» (los que el texto cita); «según el PDF» → «según
   la propia nota».
9. Portada: se añade el RD 171/2004 (art. 14.1.b), que el tema cita. «Normativa que el tema invoca»:
   se añaden los artículos 14.1, 14.2, 15.1.g) y 18.1 de la LPRL, citados por remisión.

Pasajes cambiados releídos: ningún «ese artículo», «dicha» o «el apartado» queda sin antecedente.

## Confirmado sin cambios

Recuentos (seis competencias del art. 5, tres objetivos del art. 9, cinco tareas de la ficha, siete
requisitos de la NTP 685, cuatro grupos de barreras, tres niveles, seis variables de la NTP 438, tres
piezas del 0909, cuatro criterios del 0909 RA 2, dos criterios de la casa); atribución de cada RA,
CR, CE y apartado del LE; «qu» del 0909 RA 5.e (así en el BOE); remisiones a los temas 3, 4, 6, 11 y 19
y al tema 9 del común; lo declarado como oficio o lectura del tema va marcado como tal. Refutar puede
dar cero hallazgos si el tema está bien.

Ficheros tocados: el tema y este informe.
