# Puesto 08 · Tema 3 · Fase 5 · Remate

Fecha: 24-09-2026. Tema:
`temas/canal-sur-especificos/08-camara-operador/03-captacion-eng-estudio-exteriores-um-directos.md`.
Entrada: `08-T03-refutacion.md` (0 graves, 4 menores, 2 lagunas) y `08-T03-preguntas.md`.

## Fuentes releídas (24-09-2026)

- Libro de estilo de Canal Sur (`libro-de-estilo-333233b.txt`), 5.1 y 5.3.2.
- Manual ATEM en español (`Blackmagic_ATEM_manual-es.txt`), «Primeros pasos», paso 3.
- SMPTE 311-2009, cláusula 1 (ya citada en el tema: «signal and control»).

## Correcciones (todas confirmadas en la fuente; ninguna rechazada)

| Nº | Pasaje | Comprobación | Cambio |
|---|---|---|---|
| 1 | «Cuánto se graba y cómo», 3.ª viñeta | LE 5.3.2: los diez segundos son «como para que pueda ser empleados por sí mismos e independientemente del movimiento»; el *preroll* justifica sólo los cinco segundos; «sobre todo las panorámicas» | Reescrita: añade «sobre todo las panorámicas» y el motivo de los diez segundos en negrita literal; el *preroll* queda atribuido sólo a los cinco segundos |
| 2 | «La intercomunicación y el retorno», 1.er párrafo | La cita está en el paso 3 de «Primeros pasos», tras «El modelo ATEM Constellation 8K brinda la posibilidad…» | «al describir la puesta en marcha del modelo Constellation 8K, que tiene botones de intercomunicación en el panel frontal» |
| 3 | «El tándem…», viñeta «Por qué» | LE 5.1: el «ello» remite a «qué es lo que puede aflorar de una cobertura» | Antepuesto en redonda: «el periodista, que tiene que saber qué puede aflorar de una cobertura,» |
| 4 | «El cable de cámara», 1.er párrafo | SMPTE 311 cl. 1 sólo dice «signal and control» | Marcado «como costumbre de oficio (la norma de la fibra sólo habla de señal y control)» y añadido a la lista de oficio de «Trazabilidad» |

## Lagunas: se amplía el tema (contenido nuevo, de oficio)

No hay fuente leída para ninguna de las dos (grep sin resultado en `fuentes/`; la investigación B
dice del triax «no dar cifras»). Se añaden como oficio declarado, sin cifras.

1. Pregunta 9 · «Estudio» › «El operador en un plató multicámara»: fila nueva en la tabla,
   «Regidor (o jefe de plató)»: enlace a pie de plató entre la realización y el plató; transmite
   órdenes a presentadores e invitados, marca entradas y tiempos con señas, avisa al control; el
   operador se coordina con él en posiciones y desplazamientos y para que no entre en plano.
2. Pregunta 11 · «Unidades móviles» › «El cable de cámara»: párrafo nuevo al final, «Cuándo se usa
   cada familia es también oficio…»: fibra para distancias largas y capacidad, sin degradación con la
   longitud, más ligera, conector delicado, no suele repararse en campo; triax más pesado y de menor
   alcance, más robusto, reparable en campo; regla práctica. Sin cifras de alcance.

Otros cambios: ficha «Extensión» 8.800 → 9.200 palabras; «Trazabilidad», lista de oficio: «el papel
del regidor» y «lo que lleva el cable de cámara y la elección entre triax y fibra híbrida».

Releídos todos los pasajes cambiados: cada «ello», «ambos», «cada familia», «él» tiene su
antecedente delante.

## Lentes

- `indice.py`: 9.187 palabras, 44 epígrafes; índice regenerado (el tema no está en `portadas.tsv`,
  la ficha se mantiene a mano).
- `refutar_prosa.py`: 2 avisos, ambos previos y fuera de lo cambiado (ENG en el título, antes de las
  siglas; URSA es nombre de modelo, glosado).
- `negritas.py` contra las cinco fuentes: 91 negritas, 3 no encontradas (dos rótulos y la cita LE
  3.17.1.5 partida por salto de página, literal según la refutación). Las negritas nuevas de LE 5.3.2
  están.

## Resultado

Se amplió contenido nuevo (dos lagunas, oficio): procede la fase 5 bis sobre la fila del regidor y
el párrafo triax/fibra.

## Ficheros tocados

El tema y este informe.
