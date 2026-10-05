# Fase 5 bis · Oficial Técnico Electricista (27) · Tema 13 · Mantenimiento preventivo, correctivo y predictivo

Revisión sólo de los pasajes que cambió el remate (`27-T13-remate.md`), por diferencia con la copia
previa del tema. Fuentes releídas el 05-10-2026 (reloj del sistema; el encargo fija «hoy» en
24-09-2026; ninguna redacción usada es posterior). Ficheros tocados: el tema y este informe.

## Cotejo, pasaje por pasaje

| Pasaje | Fuente releída | Resultado |
|---|---|---|
| M1 · 1.2 y Trazabilidad: «edición anterior a la vigente» | Investigación D §1.1 (ficha AENOR: «Anula a UNE-EN 13306:2011»; pliego: «edición 2010») | Correcto; la reserva sin año es la forma prudente |
| M2 · 3.4 y 7.2: «apéndice 3, A3.2, punto 2» | RITE (BOE-A-2007-15820), apéndice 3: A3.2 «2. Mantenimiento de instalaciones térmicas», con la frase en negrita literal | Correcto |
| M3 · 1.1: primera tarea del J. Sec. Mantenimiento | X Convenio, BOJA 240/2014, p. 158, ficha 9310000 | Literal y primera de la lista. Correcto |
| L2 · 1.2: TPM | RD 401/2023, módulo 0968, RA 7 d) (también RA 8 c) y contenidos: «Mantenimiento productivo total (TPM)»), así que «lo incluyen como contenido» se sostiene; UC3M diapositiva 10; Cantabria cap. 5, 5.2.2 (tres ceros; «Los pilares (8 conceptos)»; «el orden no significa preferencia») | Todas las negritas, literales. Correcto |
| L1 · 3.4: MTBF, MTTF, MTTR, disponibilidad | Cantabria cap. 2: 2.3 (MTBF), 2.4 (MTTF), 2.5 (fórmula del MTTR), 2.14 (disponibilidad, entre 0 y 1, fórmula); UC3M diapositiva 25 («OTRAS MEDIDAS DE LA MANTENIBILIDAD · MTTR») | Negritas literales. Cálculo del SAI: 4.380/4.400 = 0,9955 ≈ 99,5 %. Correcto |
| L3 · 7.2: punto de pedido, stock de seguridad, stock mínimo | UOC PID_00253874, 1.3, 1.4, 1.6.2 | Literales; fórmula y definiciones de Cmed y Pmed exactas; ejemplo 2 + 4 × 1 = 6. Correcto |
| Siglas, «Qué se puede preguntar», ficha, «Lo que este tema no da», lista de oficio | — | Coherentes con lo añadido |

## Correcciones aplicadas (comprobadas en la fuente)

1. 3.4: «Los tres indicadores básicos se definen así…» → «El MTBF, el MTTR y la disponibilidad se
   definen así…». Ningún manual los llama «los tres indicadores básicos» (error 9).
2. Trazabilidad, Cantabria cap. 5: autores «C. Sierra Fernández y E. Andrea Calvo» (la portada del
   capítulo 5 nombra a los dos, igual que la del capítulo 2).
3. Trazabilidad, UC3M: «diapositiva 10» → «diapositivas 10 y 25». El MTTR como medida de la
   mantenibilidad está en la 25, no en la 10 (error 8).

## Antecedentes

«El real decreto no lo define» → RD 401/2023 inmediatamente antes; «Uno de sus ocho pilares» → el
TPM; «ellas» (3.4) → UNE-EN 15341 y 17007; «El mismo manual» (7.2) → el de la UOC; «epígrafe 7.1»
y «epígrafe 1.1» existen. Todo en orden.

## Lentes

`refutar_prosa.py`: 0 hallazgos. Sin cambios de rótulos: el índice no varía.

## Resultado

0 graves; 3 menores corregidos. Tema cerrado.
