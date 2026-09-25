# Puesto 08 · Tema 3 · Fase 3 · Verificación

Fecha: 24-09-2026. Tema:
`temas/canal-sur-especificos/08-camara-operador/03-captacion-eng-estudio-exteriores-um-directos.md`
(8.863 palabras tras la verificación, según `indice.py`).

## Método

- Cada negrita cotejada por script contra el texto completo de las cinco fuentes (normalizando
  espacios, ligaduras y comillas): todas aparecen literales; las dos que el script no encontró
  (LE 3.17.1.1 y 3.17.1.5) están partidas por mayúscula inicial y por salto de página, y son literales.
- Después, releído en la fuente el contexto de cada cita: epígrafe, página, salvedades y verbo.
- Saltado, como manda el encargo, lo listado bajo «Copiado del común» en `08-T03-redaccion.md`
  (tabla de vías y viñetas *Satélite* y *Mochila*; en «La preparación», los párrafos LE 8.3 y 8.1.6).
  Sí verificado lo copiado de RTVE (oficio): sin cifras ni normas inventadas; declarado como oficio.
- Lentes: tema técnico sin norma jurídica → `refutar_prosa.py` e `indice.py`. Prosa: 2 avisos no
  aplicables (ENG en el título, antes de las siglas; URSA, nombre de modelo explicado). Negritas rotas: 0.

## Fuentes releídas (24-09-2026)

| Fuente | Qué se comprobó |
|---|---|
| Libro de estilo CSTV (1.ª ed., marzo 2004), `libro-de-estilo-333233b.txt` | Intro p. 9; 3.17.1-3.17.1.5 pp. 59-62; 5-5.6 pp. 79-85; 8.3.2-8.3.4 pp. 117-118; 8.4-8.4.2 pp. 119-120. Epígrafes y páginas correctos |
| UIT-R SNG.770-2 (01/2012), `.txt` local | Considerando c), recomienda 8 y 9, anexo 1 § 1.1 y § 2.2.1: literales. Vigencia: `itu.int/rec/R-REC-SNG.770` consultada hoy, «In force»; la -1 «Superseded» |
| SMPTE 311-2009, `.txt` local | Aprobada 4-VI-2009; revisa 311M-2003; cl. 1, 5.1, 6.1, 6.2 literales |
| Blackmagic ATEM, manual es, `.txt` local | Líneas 772, 1011, 1019-1023, 1461-1463, 2674-2677, 7645: literales. El `.txt` sólo dice «© 2024»; título y «diciembre de 2024» se toman del registro `fuentes/fabricantes/README.md` |
| LiveU LU800, ficha `.txt` (descargada 03-09-2026) | Cinco citas literales |

## Correcciones aplicadas

| Nº | Error | Pasaje | Qué se hizo |
|---|---|---|---|
| 1 | 6 salvedad omitida | «El sonido en ENG», viñeta del sonido como noticia | LE 5.4 dice «hay que realizar, si es posible, una grabación específica… independiente de la imagen»: añadidos «si es posible» e «independiente de la imagen» |
| 2 | 4 / 9 | Cierre de «El tándem» | «el criterio técnico y visual recae en el cámara» exageraba LE 5.1 («es imprescindible para proponer soluciones… o aportar ideas»): ajustado |
| 3 | 9 | «El cable de cámara», glosa | SMPTE 311 no habla de alimentación ni dice que el cable «se tienda a la intemperie»: glosa reescrita a lo que dice el alcance (fibras monomodo y conductores para señal y control, entornos con humedad, intemperie y ozono) |
| 4 | 6 | Cita del alcance SMPTE 311 | Cortada antes de «however, it may be used for other applications»: añadida la salvedad |
| 5 | 3 recuento | «tres datos» de SNG.770-2 | Eran cuatro (1.1, 2.2.1, rec. 8, rec. 9): «cuatro datos», rec. 9 en viñeta propia |
| 6 | 9 | Tras rec. 9, «Una unidad de satélite no se enciende sin permiso» | Sustituido por lo que dice el texto: la autorización se presupone y la Recomendación sólo limita qué país la da. «Lo primero que se comprueba…» marcado como oficio |
| 7 | 4 | LE 8.4, monitor | «El narrador debe» por lo que dice el libro: «la mejor forma… es utilizar el monitor» |
| 8 | 1 cita cruzada | «El capítulo se dirige al narrador» | Es el epígrafe 8.4, no el capítulo 8 (Presencia en cámara): corregido |
| 9 | 9 | LE 8.4.2, paso de palio | Presentado como «regla de tono que vale para la imagen»: es regla para el narrador; la extensión a la imagen queda declarada como oficio |
| 10 | 9 | Robotizadas, orden de corte | Dato de oficio de RTVE sin fuente leída: acotado a «muchas consolas; depende del fabricante» |
| 11 | 9 | Portada, «única edición publicada» del LE | No confirmable: «primera edición (marzo de 2004), sin edición posterior localizada», como en «Lo que este tema no da» |

Cada pasaje cambiado se releyó: «la misma Recomendación», «el libro», «el narrador» y «ese tiempo»
tienen delante su antecedente.

## Comprobado sin cambios

Cifras LE (20-25 planos, 3-4 secuencias, 4-8 min, 10 y 5 s, 30 s y 1 min de barras); canales 1 y 2;
planos de entrevista (3.17.1.1); dos cámaras ENG (3.17.1.5, p. 61); 5.5 y 5.6; 8.3.2-8.3.4; siglas
(CSTV consta en LE 8.3.4); remisiones a los temas 1, 2, 4-8, 10, 11, 13-15 contra el enunciado.

## Avisos

- La fecha «diciembre de 2024» del manual ATEM no está en el `.txt`; se sostiene en el registro de
  fuentes. Si la refutación la quiere, que la coteje en el PDF original.
- `indice.py` marca el tema como «sin portada: es un esquema» aunque la portada existe; no es un
  problema del tema.

## Ficheros tocados

El tema y este informe.
