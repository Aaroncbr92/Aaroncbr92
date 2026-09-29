# Grafista (15) · Tema 11 · Refutación (fase 4)

Tema: `temas/canal-sur-especificos/15-grafista/11-derechos-autor-bancos-imagenes-tipografias-licencias-imagen-atribucion.md`
(16.517 palabras, 51 epígrafes). Fecha del encargo: 24-09-2026; fuentes leídas el 29-09-2026 (fecha de
sistema). No se corrige: sólo se informa.

Ficheros tocados: este informe y `15-T11-preguntas.md`. El tema, no.

## Alcance

- Exactitud: todo lo que no figura como «Copiado del común» íntegro en `15-T11-redaccion.md`; de los
  pasajes «con ajustes», sólo lo ajustado o añadido. «Copiado de RTVE sin cambios»: ninguno.
- Cobertura: el tema entero contra el enunciado (punto 11 del Anexo V, puesto 2.15).

## Fuentes releídas (29-09-2026)

| Fuente | Qué | Resultado |
| --- | --- | --- |
| TRLPI, volcado local (BOE-A-1996-8930) y `redacciones.tsv` | arts. 5 a 11, 13 a 16, 41, 42, 43, 48, 48 bis, 49, 50, 51, 87, 96, 145, 146; última modificación (art. 177, 31-03-2022) | Literal y bien atribuido |
| Ley 20/2003, `boe.py --fecha 20260924` (BOE-A-2003-13615) | arts. 1, 5, 6, 7, 43 y DA 10.ª; una redacción | Literal |
| X Convenio, ficha 5345100 | Función, tareas, «y todo tipo» (sic), p. 129 | Literal; página correcta |
| Libro de estilo, 3.2.2 y 3.10 | Rótulo «reconstrucción», coleo y créditos | Literal |
| Adobe Stock license information | Niveles, 500.000, editorial, audio, IP indemnification, ETLA | Literal |
| SIL OFL 1.1 | Definición, permisos, cinco condiciones, documentos creados, nulidad | Literal |
| Google Fonts README | Directorios, redistribución, OFL/Apache/Ubuntu | Literal |
| ARASAAC (Aula Abierta y cadenas de arasaac.org) | BY-NC-SA, autor, propietario, exclusión comercial | Literal |
| Getty Content License Agreement (April 2026) | RF/RR/RM, exclusividad, «use», editorial, releases, uso sensible, comp, uso compartido, IA, créditos | Literal; dos salvedades omitidas (abajo) |

Lentes: `refutar_exactitud.py` y `refutar_modo.py` con el TRLPI, 0 hallazgos (32 «no literales» son de
otras normas o licencias, como ya dijo la verificación); `refutar_prosa.py`, 2 avisos de siglas (NC, SA),
falsos positivos: se presentan en la frase de siglas.

## Hallazgos de exactitud

Graves: ninguno.

Menores (2):

1. **Getty, IA: salvedad omitida (error 6).** Líneas 567-570 y cuadro del epígrafe 7 («Subir una foto de
   banco a una herramienta de IA…»). El contrato prohíbe cualquier uso «for any machine learning and/or
   artificial intelligence purposes, or for any technologies designed or intended for the identification
   of natural persons», no sólo el entrenamiento; y a continuación exceptúa: «**you may use artificial
   intelligence technology in connection with creative (non-editorial) content solely for: (i) internal
   use in connection with archiving, searching, indexing, or sorting creative content; and (ii) any
   permitted editing of licensed creative content.**» El tema no da ni el alcance amplio ni la excepción,
   que toca de lleno al archivo gráfico (tema 12) y a la edición con herramientas de IA. Pregunta 9: «no».
2. **Getty, uso compartido de RF: salvedad omitida (error 6).** Líneas 564-566 y fila «Imagen RF de
   Getty compartida en el equipo». El límite de diez es de usuarios; el mismo párrafo añade «**however you
   may make RF content available for viewing by any of your employees, clients and subcontractors**» y
   que el archivo en bruto no se entrega fuera de la entidad salvo a sus subcontratistas. Sin ello el
   lector concluye que sólo diez personas pueden ver la imagen. Pregunta 8: «a medias».

Comprobado y correcto (no son hallazgos): exclusividad RF/RM/RR tras la verificación; garantía de
releases (RF no editorial; RM/RR sólo con aviso); comp 30 días; créditos de foto y vídeo; Adobe
*Enhanced* sólo para vídeos, plantillas, 3D y Premium; tabla derecho moral/explotación (arts. 5, 14, 15,
16, 41, 42, 43); tabla de cesión exclusiva/no exclusiva (arts. 45, 48, 49, 50; la intransmisibilidad
con la salvedad del 49, párrafo tercero, está); 48 bis; arts. 1.2, 5, 6, 7, 43 y DA 10.ª de la Ley 20/2003;
viñetas nuevas de «La imagen en la pieza gráfica» (la afirmación de que el 7.5 remite al 8.2 y el 7.6 no
es descripción del texto).

## Cobertura del enunciado

Las seis materias del enunciado (derechos de autor, bancos de imágenes, tipografías, licencias,
derechos de imagen, atribución) tienen epígrafe propio, en su orden. 15 preguntas: 10 enteras,
2 a medias, 3 no (detalle en `15-T11-preguntas.md`). Dos de los fallos son los hallazgos 1 y 2; los
otros descansan en dos lagunas, ambas ya declaradas en «Lo que este tema no da»:

1. **Variantes Creative Commons (NC, ND, SA; y CC0).** El tema sólo da el texto de CC BY 4.0 y las
   siglas. Un test puede preguntar qué prohíbe ND o qué entiende NC por «no comercial»; esto último
   decidiría además la duda, declarada, de si una televisión pública usa ARASAAC «sin ánimo de lucro».
   Ampliar leyendo los textos legales 4.0 de BY-NC, BY-ND y BY-NC-SA (definición de «NonCommercial» y
   de material adaptado) y, si cabe, CC0. Preguntas 12 (y la duda de ARASAAC).
2. **Ley 17/2001, de Marcas.** Sin ella, el tema no responde qué significan ® y TM ni si puede usarse el
   logotipo de una empresa en una infografía informativa (uso descriptivo), caso diario del grafista.
   Ampliar con los preceptos de la Ley 17/2001 sobre el derecho conferido y sus límites (uso
   informativo/descriptivo) y, si consta en ella, el signo ®; si no consta, decirlo. Preguntas 13 y 15.

## Para el remate

- Hallazgos 1 y 2: añadir las dos salvedades en el texto y en las filas del cuadro del epígrafe 7
  (Sonnet basta; son literales de un fichero ya leído).
- Lagunas 1 y 2: ampliación (Opus) y, por tanto, fase 5 bis sobre lo ampliado.
