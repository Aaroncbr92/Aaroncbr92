# Ayudante de Realización (05) · Tema 18 · Fase 5 · Remate

Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/18-prevencion-riesgos-laborales.md`.
Fecha de trabajo: 30-09-2026 (fecha del sistema; el encargo dice 24-09-2026). Entradas:
`05-T18-refutacion.md` y `05-T18-preguntas.md`. **Ha ampliado contenido** (dos lagunas): procede la
fase 5 bis sobre los pasajes 4 y 5.

## Fuentes releídas el 30-09-2026

- X Convenio, ficha 5353000 (`x-convenio-rtva-boja-240-2014.txt`, l. 4720-4743): confirma que la
  ficha sólo nombra «los estudios y salas de control» y «el control de realización».
- IMS077_3 (`incual-IMS077_3.txt`, l. 209-212): CR5.1 sigue tras «indicaciones recibidas» con
  «, comprobando los encuadres…».
- RD 487/1997 (BOE-A-1997-8670, `boe.py precepto` a1, a2, a3): 1 redacción, vigente desde 13-05-1997.
- RD 171/2004 (BOE-A-2004-1848, `boe.py precepto` a11): 1 redacción, vigente desde 30-04-2004.
- INSST, Guía Técnica de manipulación manual de cargas, septiembre de 2024, NIPO 118-24-023-2
  (`fuentes/prl-especifico/guia-tecnica-mmc-2024.txt`, l. 224-256 y 622-628).

## Correcciones de la refutación: las tres confirmadas y aplicadas

1. Error 9, ficha (epígrafe 2, «El puesto de ayudante de realización en el convenio»). Antes: «La
   ficha sitúa al ayudante en cuatro lugares de trabajo: el control de realización, el estudio o
   plató, la sala de montaje y, por los reportajes y microespacios, el exterior.» Ahora: «La ficha
   nombra **«los estudios y salas de control»** y **«el control de realización»**; de sus tareas se
   deducen cuatro lugares de trabajo (lectura de este tema): el control de realización, el estudio o
   plató, la sala de montaje (por el montaje y la postproducción) y, por los reportajes y
   microespacios, el exterior.»
2. Cita recortada (epígrafe 2, «Lo que la realización puede prevenir», último párrafo): CR5.1 termina
   ahora en «…según las indicaciones recibidas […]»**.
3. Prosa («Con personal de otras empresas»): las dos entradillas con dos puntos se funden en «La Ley
   31/1995 lo regula en su artículo 24, "Coordinación de actividades empresariales", que distingue
   situaciones que conviene no mezclar:».

## Lagunas: ampliaciones

4. P14 (a medias → entera). En «Con personal de otras empresas», tras el 24.6 y antes de «Aplicado
   al ayudante», párrafo nuevo con el art. 11 del RD 171/2004: rótulo literal «Relación no
   exhaustiva de medios de coordinación», la salvedad de otros medios (empresas, negociación
   colectiva, normativa sectorial) y las letras a) a g) en lista literal. El cierre «Qué medios de
   coordinación concretos usa la RTVA… no consta» se mantiene y conserva su antecedente.
5. P15 (no → entera). En «Orden, suelos y zonas peligrosas», al final, párrafo nuevo: RD 487/1997
   arts. 1.1, 2 y 3 (literales de 1.1, 2, 3.1 y del inciso final del 3.2; resto de 3.2 en redonda),
   la frase de la guía de que el RD **«no establece ningún valor concreto de referencia»**, la tabla 1
   de la Guía Técnica (< 3 kg / 3-25 kg / > 25 kg, literal), el peso máximo en condiciones ideales
   (25 kg hombres de 20 a 45 años, 20 kg mujeres) y la aplicación al puesto como lectura del tema.
6. Consecuencias: «Lo que este tema no da» reescribe el punto de cargas (se da lo anterior; no el
   anexo, arts. 4-6 ni el método de la guía; riesgo eléctrico sigue sin darse). «Normativa que el
   tema invoca»: fila nueva RD 487/1997 (arts. 1.1, 2 y 3); fila RD 171/2004 ahora «Art. 11 (medios
   de coordinación), como desarrollo del art. 24». «Trazabilidad»: filas nuevas RD 487/1997, RD
   171/2004 y Guía Técnica MMC 2024, con fecha de lectura. Portada: Extensión 20.945 palabras.

Relectura de los pasajes 1-5: cada «artículo 3.2», «la misma guía», «la tabla 1», «el artículo 24»
tiene delante su antecedente.

## Lentes

- `indice.py` sobre el tema: 20.945 palabras, 43 epígrafes (lo trata como fuera de `portadas.tsv`,
  por eso la extensión de la portada se ha puesto a mano con esa cifra). Aviso: una primera
  ejecución sin argumentos recorrió los temas de `portadas.tsv`; git no muestra cambios de
  contenido en ellos.
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` con RD 487/1997, RD 171/2004, guía MMC, IMS077_3 y convenio: todas las negritas
  nuevas se encuentran salvo «no establece ningún valor concreto de referencia», falso positivo por
  el guion blando del .txt («con­creto», l. 225-226), comprobado a mano. El resto de «NO ESTÁ» son
  pasajes de otras normas (LPRL, RD 773/1997) no pasadas a la lente.
- `refutar_exactitud.py` y `refutar_modo.py` con las mismas dos normas: ningún aviso en los pasajes
  nuevos; el único de modo («art. 15… facultados») es cruce con el art. 15 de la LPRL del texto
  copiado del común, no del RD 171/2004. No se toca.

## Ficheros tocados

El tema y este informe.
