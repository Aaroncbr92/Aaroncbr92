# Realizador/a (puesto 33) · Tema 16 · Fase 3, verificación

Tema: `temas/canal-sur-especificos/33-realizador-a/16-accesibilidad-responsabilidad-editorial.md`.
Fecha del encargo 24-09-2026; fuentes releídas el 29-09-2026 (fecha del sistema). Trabajo en el
scratchpad `v16/`.

## 1. Literalidad de lo copiado (sin re-verificar)

Reconstruido el tema con `t16/assemble.py` contra los ficheros actuales de 30/11, 34/17, 08/16 y
08/12: el resultado es idéntico al tema salvo el índice que insertó `indice.py`. Lo listado bajo
«Copiado del común» es literal, con sólo los 16 cambios de remisión de `adapt.log`. «Copiado de RTVE
sin cambios»: ninguno. Remisiones adaptadas: cada una tiene su antecedente en el epígrafe que nombra.

**Hallazgo en lo copiado (error 3, recuento):** el rango 08/16 l. 611-665 cortaba la tabla de la Guía
del CAA en la fila 9, bajo el rótulo «Las diez recomendaciones». Añadida la fila 10, literal de 08/16
l. 666.

## 2. Verificado en la fuente (29-09-2026)

- Ley 27/2007 (`boe.py`, BOE-A-2007-18476): arts. 1, 4.c/i, 14 (dos redacciones; también con `--fecha
  20100101`), 22, 23. Ley 26/2011 (BOE-A-2011-13241): art. 2 y título en el sumario XML del BOE.
- Ley 11/2011 (BOE-A-2011-20375): arts. 5 y 16; título en el sumario del BOE.
- Guía del CNLSE (txt y PDF con pypdf): 29 citas cotejadas normalizando guiones blandos; caps. 5, 6.1-6.4,
  créditos (FORTA y RTVE en el grupo de trabajo, p. 5), NIPO.
- UIT-R BT.1702-3: todas las citas; notas 1, 3, 5; anexos 2 y 5; página itu.int: «En vigor».
- LGCA (volcado del 24-09; la API del BOE devolvió 404 el 29-09): arts. 6.1, 95.1-2, 98.1, 99.1, 99.2.c,
  101.3, 102.2.b-c. Ley 12/2007 art. 57.2; LO 3/2007 art. 36; LO 1/2004 art. 14; LO 1/1996 art. 4.3.
- Libro de estilo (txt): 9.4.2, 9.4.2.1, 9.9, 9.7.3.

## 3. Correcciones aplicadas

1. **Error 9/8, art. 14 Ley 27/2007:** el tema decía que la Ley 26/2011 «añadió también el apartado 6».
   Falso: el 14.6 está en la redacción de 2007. El artículo 2 de la Ley 26/2011 cambió el 14.1 y el 14.3
   («lengua de signos española» → «lenguas de signos españolas»). Corregido (el informe de redacción
   atribuía la reforma al art. 1, que modifica la Ley 51/2003). Título de la Ley 26/2011 confirmado.
2. **Cita no literal, guía CNLSE 6.3.1:** la guía dice «tanto el **subtitulado** como el signado ocuparán
   espacios diferenciados» (txt y PDF, p. 63). La «corrección» del redactor a «subtitulo» era errónea: se
   deja como estaba en la investigación.
3. **Error 6, 22.1:** la cita empezaba en «los programas…» y omitía «las informaciones institucionales y».
4. **Error 4, 6.2:** «se compensa abriendo el iris» → la guía dice «se puede modificar la apertura del
   iris»; y la obturación «reduce» la aparición del verde, no lo elimina.
5. **Error 6, 6.3.3:** el fondo es primero «configurable» si la técnica lo permite; añadido.
6. **Error 9, audiodescripción «Una pista aparte»:** que se emita en pista propia que el espectador activa
   no tiene fuente leída; se deja lo que dice la guía de Burgos (dos pistas que se ecualizan) y se declara
   el hueco.
7. **Error 9, «lenguaje inclusivo»:** «Ninguna norma leída usa la expresión» era falso: la usa el
   preámbulo de la Ley 4/2023. Matizado al articulado.
8. **95.2 LGCA:** «un suceso» → «hechos delictivos» (§ 5 y tabla final).
9. **BT.1702, anexo 5:** «propensa a la epilepsia fotosensible» → «a la fotosensibilidad».
10. Cita no literal de la síntesis UNE 153010: «centrado» → «centrados» (los subtítulos).
11. «No recomendado» → «No recomendada» (99.2.c) en «Qué se puede preguntar».
12. 57.2 Ley 12/2007: añadido «de forma vejatoria», que la norma exige.
13. Aplicación práctica: la versión a la carta conserva accesibilidad (31.1.i LAA), **no** «la
    calificación»: quitado. Archivo de «víctimas» → archivo que ilustra sucesos (9.9.1). «Síntesis de la
    UNE 153020» → guía de Burgos que remite a esa UNE.
14. Menores: Contrato-programa punto 93, «producción propia **interna**». 6.1 rotulado como en la guía
    («Visión general»). Preferencia por la silueta: es del informe del CNLSE de 2015 que la guía resume.
15. Rótulos en femenino: quitado «es la regla de…» (sonaba a norma; es oficio).
16. «No consta» sobre la lengua de signos de Canal Sur: la guía del CNLSE (2017, 5.3) dice que Canal Sur
    la ofrecía por su segundo canal; añadido con fecha, y en «Lo que este tema no da».
17. Repetición quitada (cómo se subtitula en directo). Trazabilidad: cuatro filas nuevas; «In force» →
    «En vigor». Extensión: 26.700 palabras.

Comprobado, sin cambio: Ley 11/2011 (5.h/n/ñ, 16.1/3/4); arts. 14.1, 14.6, 23.1-2; CENELEC/Ofcom 1/6;
UPM 1/3 y 1/4; espacio sígnico; 1/125-1/250 s; cinco puntos de luz; BT.1702 (160 y 20 cd/m², 1/17
Michelson, 25 %, 360/334 ms, 200/1 000 cd/m²); arts. 98.1, 99.1, 99.2.c, 101.3; LO 3/2007 art. 36;
LO 1/2004 art. 14; remisiones a los temas 9, 11, 12, 13 y 17 del puesto.

## 4. Lentes

`negritas.py` (27/2007, 11/2011, CNLSE, BT.1702, LGCA, 12/2007, LO 3/2007, LO 1/2004, LO 1/1996): los
«no está» de lo nuevo son falsos positivos por guiones blandos del txt del CNLSE (cotejados a mano) o
del Libro de estilo (grep). `refutar_modo.py` (27/2007 y 11/2011): 0 hallazgos. `refutar_exactitud.py`:
sólo atribuciones espurias (números de apartado de la guía leídos como artículos). `refutar_prosa.py`:
dos repeticiones en pasajes copiados; «LOGROS» y «ROMPER», rótulos, falsos positivos. `indice.py`:
índice sin cambios, 26.748 palabras.

## 5. Avisos al coordinador

- La errata «CNSLE» sigue en 30/11 y 34/17 (ya avisada en redacción).
- 08/16 está bien; el corte de la fila 10 fue del ensamblado de este tema.
- El informe de redacción se equivocaba en dos puntos: «subtitulo» (punto 2) y «apartado 6» (punto 1).

## Ficheros tocados

El tema y este informe. Scratchpad: `v16/`.
