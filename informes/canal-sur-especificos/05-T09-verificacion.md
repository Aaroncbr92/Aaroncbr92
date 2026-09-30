# Ayudante de Realización (05) · Tema 9 · Fase 3 · Verificación

Tema: `temas/canal-sur-especificos/05-ayudante-de-realizacion/09-mezcladores-efectos-transiciones-senalizacion.md`
Fecha: 30-09-2026 (el encargo fija «hoy» en el 24-09-2026; manda la del sistema). Todas las fuentes
se releyeron el 30-09-2026.

## Literalidad de lo copiado (sin re-verificar)

- **Copiado del común** (tema 33/09): cotejo por párrafos con script. Todos los epígrafes listados
  como «copiados enteros» son literales. En los «copiados en parte», las únicas diferencias con 33/09
  son las remisiones internas («epígrafe N», «arriba, en este epígrafe»), renumeradas para este tema;
  comprobadas una por una contra los epígrafes de este tema: todas correctas (4, 5, 6, 3, 2, 7, 1).
- **Copiado de RTVE sin cambios** (`temas/realizacion/11-…`, § 8): las tres piezas son literales,
  sin las negritas. Lo adaptado («Va en tres sitios a la vez»; ventanas con tres cámaras, «(oficio)»)
  coincide además, literal, con el tema cerrado 33/04, «El piloto»: sin datos que verificar.

## Verificado contra su fuente

| Pasaje | Fuente releída | Resultado |
|---|---|---|
| 1 · Lo que la cualificación pide al ayudante (CE1.5, CE1.6, RP1, CR1.2, CR1.3, CR2.1, contenidos 5 y 6) | `incual-IMS077_3.txt` | Literal; páginas 7, 18 y 20 correctas (cabeceras «Página: N de 25»); Orden PCI/797/2019 correcta |
| 3 · Lo que el ayudante comprueba de las transiciones | IMS077_3 (CE1.6, CR1.2) | Correcto; resto declarado oficio |
| 7 · Qué se entiende por señalización técnica; piloto; panel; vías; llamada; barras; lo que comprueba el ayudante | Manual ATEM es (pp. 1066-1067 «Sistemas de señalización»; puesta en marcha l. 1015-1032; buses l. 376-440; control de cámara l. 2960-2983; barras l. 5008; SDI Camera Control Protocol 5.0-5.2; Embedded Tally Control Protocol v1.0, 30/04/14) | Todas las negritas literales; cifras (8 relés, hasta 8 unidades, 5 V/14 mA, 30 V/1 A, DID/SDID x51/x52, VANC línea 15, 4 bits) correctas; «lo botones» y «ya la fuente» están así en el manual |
| 7 · Protocolo TSL UMD | `TSL_UMD-protocol.txt` (19/09/09) | Literal: V3.1/V4.0/V5.0, 38k4, 0-126 + 80 hex, 16 caracteres, colores 0-3, UDP 2048 bytes, TCP/IP, 65,535, sentido único |
| Nombre corto de cuatro caracteres | Manual ATEM l. 2773 | Correcto |
| NMOS IS-07 «Event & Tally» | Tema cerrado 33/15 (literal) | Se mantiene; «no da» ya declara que la especificación no se leyó |
| Remisiones a otros temas (1, 4, 6, 11, 12, 13, 14, 15) | Temas 05/04, 05/11, 05/15 | Contenido existe (GPI, piloto, titulador, sincronía, IP) |

## Correcciones aplicadas

1. **Error 1 (cita cruzada)**: tras las siglas quedaba el enunciado del puesto 2.33 (Realizador/a,
   «Mezclador de vídeo y recursos de realización…»), arrastrado del tema 33/09. Quitado; queda sólo
   el del puesto 2.5.
2. «Para el realizador, IS-07 es la que toca de cerca» (resto de 33/15) → «Para el ayudante».
3. **Error 9**: siglas, «RS-422 y RS-485, que así nombra el documento de TSL»: TSL escribe «RS 422/ RS 485».
   Cambiado a «que el documento de TSL escribe «RS 422/ RS 485»».

Nota de trazabilidad (sin cambio): el redactor presenta el párrafo de IS-07 como nuevo, pero es
literal de 33/15, como dice la propia «Trazabilidad».

## Lentes

- `indice.py`: 16.357 palabras, 64 epígrafes, índice coherente.
- `refutar_prosa.py`: 3 avisos (DVE, AMBER, GREEN), falsos positivos (título del enunciado; cita literal de TSL).
- `negritas.py` (ATEM, TSL, IMS077_3, RD 1680/2011, Libro de Estilo): 167 cotejadas, 8 no halladas,
  todas del texto copiado de 33/09 (Adobe, DaVinci Resolve, Mateu Torres, cuyas fuentes no están en
  local). `refutar_exactitud.py` y `refutar_modo.py` con el RD 1680/2011: 0 hallazgos.

## Ficheros tocados

- Modificado: el tema 09 (tres correcciones de arriba).
- Creado: este informe. Ningún otro.
