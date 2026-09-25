# Puesto 08 · Tema 10 · Fase 4 · Refutación

Fecha: 24-09-2026. Tema:
`temas/canal-sur-especificos/08-camara-operador/10-cobertura-noticias-deportes-institucional-cultura-sucesos.md`
(7.644 palabras, 37 epígrafes). No se corrige: sólo se informa.

## Fuentes releídas (todas el 24-09-2026)

- Libro de estilo de Canal Sur (`fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt`): cotejada
  la atribución de epígrafe de cada cita contra las líneas de rótulo (2.5.4, 4.1.1, 4.2, 4.3.2.1,
  5.2-5.6, 7.1, 7.3, 7.4.2, 7.5-7.5.4, 8.3.2, 8.3.4, 8.4-8.4.2, 9.2.12.1-4, 9.5.2, 9.9-9.9.2,
  Introducción p. 9). Todas cuadran.
- LO 1/1982, art. 8 (`fuentes/canal-sur/BOE-A-1982-11196.md`): 8.2 a), c) y último párrafo literales;
  una sola redacción.
- CGPJ, Protocolo 2020 (`fuentes/informacion/CGPJ_protocolo-comunicacion-2020.txt`), 5.b, 5.d, 5.e:
  literales y bien atribuidos (STC 56/2004 y 57/2004, «perímetro lógico», libre acceso, tabla de pautas,
  funcionarios, mudo, *pool*).
- Ley 13/2022 (`fuentes/canal-sur/BOE-A-2022-11311.md`), art. 144 (una redacción, aplicable desde
  09-07-2022): para la laguna L1.

Saltado por «Copiado del común»: «Desaparecidos y suicidio» y el primer párrafo de «Qué es un
evento no controlado».

## Lentes

`refutar_documento.py` (LE + CGPJ + BOE): 111 negritas, 5 no casan, las mismas 5 ya cotejadas a mano
(2 rótulos de ficha; LE 4.2, 4.1.1 por salto de página; LE 5.4 con «[...]»); cifras huérfanas 0.
`refutar_prosa.py`: 0. `indice.py`: 7.644 palabras, 37 epígrafes.

## Exactitud

**Graves: 0.**

**Menores: 3.**

| Id | Línea | Error | Hallazgo | Propuesta |
|---|---|---|---|---|
| M1 | 565-567 | 6 salvedad omitida | La cita del detenido (LE 9.5.2) acaba en la «excepción matizada» y omite lo que la matiza: «Incluso en este supuesto debe imperar la discreción y sólo la atenuaremos si hay relación entre el presunto delito y la función que desarrolla, pero sólo en caso que el delito sea maniﬁesto, y si la identidad es necesaria para completar la información.» | Añadir esa frase a la cita |
| M2 | 217-218; 419-420; 422 | 9 inferencia sin marcar | Tres traducciones a imagen que el libro no dice, en redonda pero sin «(oficio)»: «planos generales, a ser posible altos… cabeza y cola» (4.3.2.1); «cubrir las cuatro miradas» (8.4.2); «más palabra, no otra imagen» (el libro sólo admite «un mayor apoyo de la palabra»). | Marcar como oficio o como lectura del tema; en toros, quitar «no otra imagen» |
| M3 | 586-595 | 6 salvedad omitida (cobertura) | La tabla del CGPJ (5.e) omite la pauta «Los jefes de prensa explicarán las limitaciones de grabación en el caso, por ejemplo, de testigos protegidos y/o víctimas», y corta la de posición antes de «que dará las pautas que considere oportunas». | Añadir la fila; completar la cita |

Comprobado sin hallazgo: título y fecha del libro (portada «Primera edición, Marzo de 2004»);
«C2 Andalucía» literal en 9.9.2; «El efecto Heisenberg» como título de 5.5, nombre tomado de las
memorias de Bradlee, e ilustración de Tom Wolfe; 7.5.1 «espectador directo o como oyente de radio»;
7.5.4 como lista de «Aspectos formales»; «deberán establecer un perímetro» (deber, no «podrá»);
pautas de 5.e presentadas como recomendaciones («se recomienda seguir estas pautas»); fechas de la
Comisión Permanente y el Pleno; siglas presentadas; remisiones a los temas 1, 3, 6, 8, 11, 12, 14, 15
y 16 cuadran con el enunciado.

## Cobertura del enunciado

Las seis materias (noticias, deportes, actos institucionales, cultura, sucesos, eventos no
controlados) tienen su `##` en el orden del enunciado, con fuente de la casa y aplicación al cámara.

**Lagunas: 1.**

- **L1 · Deportes: acceso de las cámaras y breve resumen informativo.** La Ley 13/2022, art. 144,
  obliga al titular de derechos exclusivos de un acontecimiento de interés general a permitir un
  breve resumen informativo (144.1), sólo en noticiarios y programas de actualidad (144.2), sin
  contraprestación si va en diferido y dura menos de noventa segundos, salvo gastos técnicos
  (144.3), con logotipo del organizador y del patrocinador principal (144.4), y **«Los prestadores
  del servicio de comunicación audiovisual televisivo podrán acceder, en la zona autorizada, a los
  espacios en los que se celebre tal acontecimiento.»** (144.5). Es el régimen que rige al cámara de
  ENG en un estadio, y el tema lo declara «no leído» cuando la fuente está en el repositorio y no lo
  desarrolla ningún tema común. Se amplía en «El deporte en ENG» (unas 120 palabras) y se quita
  el hueco correspondiente de «Lo que este tema no da»; la norma entra en «Normativa que el tema
  invoca» (Ley 13/2022, art. 144, redacción original, vigente el 24-09-2026). El catálogo de
  acontecimientos (art. 146) no hace falta.

## Preguntas

`08-T10-preguntas.md`: 15 preguntas (9 de teoría, 6 de aplicación práctica). 13 enteras, 1 a medias
(n.º 13, por M1), 1 no (n.º 6, por L1).

## Para el remate

Ampliación (L1) → Opus, y 5 bis sobre el pasaje ampliado. M1-M3, correcciones de pasaje.

## Otros ficheros tocados

Ninguno, salvo este informe y `08-T10-preguntas.md`.
