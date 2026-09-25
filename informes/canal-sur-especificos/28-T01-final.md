# Puesto 28 · Operador/a de Sonido · Tema 1 · Fase 5 bis, revisión del remate

Fecha de trabajo y de lectura de todas las fuentes: 25-09-2026 (el encargo fija «hoy» en 24-09-2026).
Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/01-fundamentos-de-sonido.md`. Alcance:
sólo los pasajes listados en `28-T01-remate.md`.

## Cotejo

| Pasaje | Fuente releída | Resultado |
|---|---|---|
| Onda longitudinal (3 citas) | `openstax-17-2.txt` | Literales |
| 331/343 m/s, «generally greater», tabla (331, 1480, 1540, 5960) | `openstax-17-3.txt` | Literales; proporciones 4,47 y 18,0 bien |
| 344 m/s, presión y temperatura, ladrillo ×9 | `guia-dbhr-anejo1.txt` l. 167-177 | Literales |
| Contrafase por retardo (1 ms → 500, 1.500, 2.500 Hz) | Cálculo | Correcto |
| Salvedad DPA patilla 2 | Web DPA, «Polarity, phase and delay» (URL /technology/, descargada hoy) | Literal |
| Physclips: 3 citas, ADSR, clave al revés, «to me» | `physclips-timbre-envelope.txt` | Literales (fallos de maquetación de la web: «T imbre», «spectrum .») |
| Protocolo ruido 2.1.3-2.1.4 (4 citas) | `fuentes/protocolos-vigilancia/ruido.txt` l. 500-536 | Literales |
| OpenStax *Psychology 2e* (6 citas; autores, 2020) | `openstax-psych-5-4.txt` | Literales |
| Shinn-Cunningham (definición, sinónimo, 1–5 ms, decenas de ms; Boston; Springer 2013; DOI) | `shinn-cunningham-2013-precedence.txt` | Literales |
| Aislar/acondicionar, ley de masa, estanquidad, impactos | `guia-dbhr-anejo1.txt` l. 594-662, 1256-1298, 1630-1636, 690-696 | Literales, con dos salvedades omitidas (abajo) |

## Correcciones aplicadas (todas comprobadas en la fuente)

1. **Salvedad omitida (error 6)**, «Aislar no es acondicionar»: «Lo que da el aislamiento a una pared
   simple es, sobre todo, su masa» → la guía dice que depende **«sobre todo de su masa por unidad de
   superficie, su rigidez y el amortiguamiento…»**. Se cita entera.
2. **Salvedad omitida**, ley de masa: se añade que **«sólo se cumple en un cierto intervalo de
   frecuencias»**, entre la de resonancia y la crítica o de coincidencia (l. 1294-1296).
3. **Extensión sin fuente (error 9)**: «En ventanas y puertas manda la estanquidad» → la guía habla de
   la carpintería de fachada (ventanas); «puertas» quitado. Igual en la aplicación práctica
   («carpinterías estancas y bien selladas»).
4. **Generalización**: «aire < agua < sólidos» → «en general … sólidos rígidos», con el caucho
   vulcanizado de la misma tabla (**«Vulcanized rubber 54»** m/s), que es más lento que el aire.
5. Clave: «apenas tiene sostenimiento» → la fuente dice **effectively no sustain**: «en la práctica no
   tiene sostenimiento: sólo un ataque rápido y una caída lenta».
6. Antecedente: «esas células próximas a la ventana oval» → «las células ciliadas externas próximas a
   la ventana oval» (la cita del protocolo es de otro apartado, 2.1.4).
7. Redacción: «la de medio periodo» → «aquella cuyo medio periodo coincide con el retardo»; «La física
   de la Universidad…» → «La Escuela de Física…, en su web Physclips»; frase sin verbo en «Lo que este
   tema no da» (pistas biaurales y 50 ms) rehecha.
8. Trazabilidad: filas de OpenStax 17.3 y guía DB HR ampliadas con lo añadido.

Sin hallazgos en el resto. Antecedentes («la misma fuente», «el mismo protocolo», «la guía», «la
propia guía») comprobados en cada pasaje cambiado.

## Lentes

`refutar_prosa.py`: 0. `indice.py`: 43 epígrafes (aviso «sin portada», ya conocido, ajeno al tema).
`negritas.py` con la guía y OpenStax 17.3: las negritas nuevas, literales. Unas 9.900 palabras
según `indice.py`; la portada dice 9.300 (no se toca: el recuento del remate usó otro criterio).

## Ficheros tocados

El tema 1 y este informe.
