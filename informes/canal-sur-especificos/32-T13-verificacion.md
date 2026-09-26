# Productor/a (puesto 32) · Tema 13 · Fase 3, verificar

Tema: `temas/canal-sur-especificos/32-productor-a/13-igualdad-diversidad-y-accesibilidad-en-la-produccion.md`
(21.224 palabras según `indice.py`; 55 epígrafes). Fecha de verificación y de lectura de todas las
fuentes: 25-09-2026. Redacción que se estudia: la vigente el 24-09-2026.

Ficheros tocados: el tema y este informe. Nada más (el `12-*.md` modificado que aparece en
`git status` no es de esta fase).

## Copiado del común y de 34/17: sólo comprobación de literalidad

Script de cotejo línea a línea de los 20 rangos listados en `32-T13-redaccion.md` («Copiado del
común») contra el tema: 1.125 líneas de origen, 18 no literales, y las 18 son exactamente las
alteraciones declaradas (rótulos `###`→`####`, «epígrafe N»→«más arriba»/«epígrafe 9», «punto 7 del
temario»→«tema 7 del común», remisión a «Accesibilidad en la Ley 13/2022», frase final del punto 57
sustituida). Comprobado que cada «más arriba» tiene su antecedente en el tema. No re-verificado en
fuente. «Copiado de RTVE sin cambios»: ninguno (nada que comprobar).

## Verificado en fuente (todo lo redactado de nuevo)

Portada (redacciones: tsv de RD 393/2007, RD 171/2004, Ley 13/1999, LCSP; RD 1468/2008 =
BOE-A-2008-15919 confirmado en la API de análisis del BOE), siglas, ficha 5331000 (convenio, p. 194),
Carta 24.2, 25.1, 25.3, 8.1, 9.2, 17.1, 17.2; RD 524/2023 DD.2.d) y 3, DF 1.ª, arts. 12, 14.4, 15.4;
nota de derogación del RD 393/2007; arts. 2, 3, 4 y Norma 1.2, 1.4, 1.5, 2 (con su «(...)»), 3.1-3.7,
anexos I.1.d y 2.g, II y III; búsqueda BOE «Directriz Básica» 2023-07-01/2026-09-24 (sólo las cuatro
de 21-04-2026, BOE-A-2026-9158 a 9161); RD 171/2004 arts. 1-14, DA 1.ª y 3.ª; Ley 13/1999 arts. 1,
2, 5.7, 6.2, 6.5, 7.2, 12, 14-17; Ley 15/2022 arts. 3.1.l, 6.1.a, 21; LCSP 71.1.b y d, 122.3 bis,
126.3, 145.2.1.º, 201, 202 (y Ley 1/2025 en su texto), 319.1; Cámara de Cuentas 2018 (calificación
RTVA/CSRTV); ET 6; RD 1435/1985 art. 2; Ley 18/2007 art. 2.1. Todo lo demás cuadra.

## Hallazgos y correcciones (con el error del catálogo)

| # | Error | Pasaje | Corrección |
|---|---|---|---|
| 1 | 7 redacción derogada | Ep. 8 y Normativa: RD 1435/1985 «relación laboral especial de los artistas en espectáculos públicos» | El texto consolidado indica que se denomina, por el art. 2.1 del RDL 5/2022, «…de las personas artistas que desarrollan su actividad en las artes escénicas, audiovisuales y musicales…»; se da la denominación vigente y se advierte que el art. 2 sigue diciendo «espectáculos públicos». **Afecta probablemente al tema 11** |
| 2 | 6 salvedad omitida | Ep. 4, Ley 13/1999 art. 1.3 | Faltaba «en establecimientos públicos»: se cita el inciso entero |
| 3 | 6 salvedad omitida | Ep. 8, «Qué significa»: autorización del 6.4 ET | Se añade «si la grabación es “espectáculo público”», salvedad que el propio tema declara no confirmada |
| 4 | 9 / precisión | Ep. 8, «Qué significa»: información del art. 27 LPRL «a quien haya intervenido» | «a sus padres o tutores que hayan intervenido» (27.1) |
| 5 | 6 | Ep. 5, admisión (7.2 Ley 13/1999): «Los titulares» | «Los titulares de establecimientos públicos» |
| 6 | 5 siglas | «ONU» sin presentar (126.3 LCSP); BOE, BOJA, UE, DA/DT/DD/DF sin presentar | «Naciones Unidas»; añadidas a las siglas |
| 7 | 1 cita cruzada | Ep. 6: «*Contratación pública (artículo 12)*» y «Subvenciones y contratación (artículo 37)» sin ley delante | Rótulos de enlace «De la Ley 12/2007…» y «De la Ley 15/2022…» (texto nuevo, fuera de las copias) |
| 8 | forma | 14.4 RD 171/2004, negrita partida en mitad de línea | Reflujo |

Portada: extensión a 21.200; Trazabilidad: añadida la nota de denominación del RD 1435/1985.

## Lentes

- `negritas.py` (19 fuentes: LGCA, LAA, LO 3/2007, Ley 12/2007, Ley 15/2022, Ley 4/2023, Ley 18/2007,
  LPRL, RD 171/2004, RD 393/2007, RD 524/2023, Ley 13/1999, LCSP, ET, RD 1435/1985, CE, Carta,
  Contrato-programa, convenio): 605 negritas; en texto nuevo, los «no está» son rótulos y los «otro
  artículo» son falsos positivos (Norma 3.x leída como art. 3; 122.3 bis bajo su rótulo; art. 4.1.b).
- `refutar_exactitud.py`: mismos falsos positivos (apartados de la Norma tomados por artículos); todas
  las citas nuevas cotejadas a mano.
- `refutar_modo.py`: 17 avisos, todos por coincidencia de numeración entre normas (LCSP/LGCA/LPRL) o
  en pasajes copiados; ninguno en texto nuevo que cambie el sentido.
- `refutar_prosa.py`: 0 hallazgos. `indice.py`: 21.224 palabras, 55 epígrafes.

## Lo que sigue sin confirmar (ya declarado en el tema)

Directriz Básica de Autoprotección (no consta); Decreto 195/2007; si una grabación con público es
«espectáculo público»; el «(...)» de la Norma, apartado 2; autoridad laboral andaluza para menores;
documentos internos de la RTVA/CSRTV; aplicación de los arts. 122 y 126 LCSP a CSRTV (tema 10).
