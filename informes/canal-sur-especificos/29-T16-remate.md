# 29-T16 · Remate · Operador/a Informático · Prevención de riesgos laborales aplicada al puesto

Fecha: 06-10-2026 (fuentes releídas ese día). Tema:
`temas/canal-sur-especificos/29-operador-a-informatico/16-prevencion-de-riesgos-laborales-aplicada-al-puesto-de-trabajo.md`.
Entrada: `29-T16-refutacion.md` (0 graves, 2 menores, 1 laguna) y `29-T16-preguntas.md` (14 enteras, 1 no).
Ficheros tocados: el tema y este informe. **Remate con ampliación**: procede el 5 bis sobre los pasajes 3 y 4.

## Correcciones, comprobadas en la fuente

| N.º | Hallazgo | Fuente releída | Decisión |
| --- | --- | --- | --- |
| 1 | Error 8: «(anexo V.B.1)» por B.1.2 | BOE-A-2001-11881, anexo V, B.1.2 (l. 394): «La apertura de celdas, armarios y demás envolventes de material eléctrico estará restringida a trabajadores autorizados» | Aplicada: «(anexo V, B.1.2)» |
| 2 | Prosa ambigua sobre la reserva de apertura de envolventes | Mismo anexo: rótulo «Trabajos en proximidad» (l. 375) y B.1 «Acceso a recintos de servicio y envolventes de material eléctrico» | Aplicada: frase que la sitúa en su anexo y declara que el RD no dice si alcanza a abrir la caja de un equipo desconectado |

## Laguna 1 (pregunta 14): ampliación

Fuentes: INSST, tema 69 «TME de la extremidad superior», v. abril 2025 (`fuentes/prl-especifico/insst-tme-extremidad-superior.txt`, l. 20-84 y 446-451); INSST, DDC-TME-07 (l. 30-41, 52-56, 236-244) y DDC-TME-04 (l. 62-64), noviembre 2022 (`fuentes/ddc/`).

Añadido en «Ergonomía y trastornos musculoesqueléticos», tras «Qué son»: tabla de los cinco TME de extremidad superior que nombra el INSST (tendinitis del manguito, epicondilitis, epitrocleitis, túnel carpiano, ganglión) con localización y gesto; prevalencia del túnel carpiano por sexo; diagnósticos de los trabajos repetitivos; definición del STC (compresión del nervio mediano) y sus factores ocupacionales según la DDC-TME-07; y las dos salvedades de las DDC: no hay evidencia concluyente entre ordenador (teclado, ratón) y STC, ni el ordenador aparece como factor de riesgo de epicondilitis. Ojo: la clave de la pregunta 14 («se asocia al uso repetido de teclado y ratón») choca con esta salvedad; conviene reformular el enunciado (sin cambiar la respuesta b).

No se añaden la tenosinovitis de De Quervain ni la cervicalgia: el tema 69 no las nombra entre los TME más frecuentes.

## Pasajes cambiados

1. Epígrafe 2, «El riesgo eléctrico», párrafo «Lo que esto significa para el puesto»: cita a B.1.2 y frase nueva sobre el ámbito del anexo V.
2. «Qué se puede preguntar»: «qué son los TME, cuáles son los de la extremidad superior y qué movimientos los provocan».
3. Epígrafe 3, «Ergonomía y trastornos musculoesqueléticos»: bloque nuevo «Los TME de la extremidad superior» (tabla y tres párrafos).
4. «Trazabilidad»: fecha de lectura 06-10-2026 y fila nueva DDC-TME-04 y DDC-TME-07.

Antecedentes revisados: «Esta última reserva», «El mismo documento del INSST», «Del túnel carpiano», «Y de las lesiones» tienen delante su referente.

## Lentes

- `indice.py`: regenerado sin errores.
- `negritas.py` (RD 614/2001, tema 69, DDC-04, DDC-07): todas las negritas nuevas son literales (corregidas mayúsculas iniciales y comillas en la tabla).
- `refutar_prosa.py`: 0 hallazgos.
- `refutar_exactitud.py` (RD 614/2001): sin avisos sobre el anexo V; sus «no literales» son de pasajes ya verificados, no tocados.
