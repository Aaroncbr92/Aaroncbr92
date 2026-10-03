# 31-T02 · Verificación · Diseño de programas de radio

Fase 3. Verificado el 3-X-2026 (fecha de referencia del encargo: 24-IX-2026).
Tema: `temas/canal-sur-especificos/31-presentador-productor-de-radio/02-diseno-de-programas-de-radio.md`
(8.863 palabras según `indice.py`; 50 epígrafes, sin cambios de rótulo).

## Copiado del común y de RTVE sin cambios: sólo literalidad

Comprobado por cotejo normalizado de párrafos (script en el momento) y `grep`, sin re-verificar:

- De 05-T02 (Ayudante de Realización): §6 «Qué es» (tres párrafos), «Cómo se organiza» (cita, tabla,
  párrafo de las dos reglas), primer párrafo de «El protocolo, también para el audio»; §4 «Es el
  pre-guion…», «La palabra tiene dos acepciones…», «Primera acepción…»; cita 6.1 del Libro de estilo
  (regla 1, l. 371-373 del origen); «La terna es de oficio; ninguna norma la fija.». Literales.
- De 34-T08 (Redactor/a): «un manual de periodismo televisivo» y las dos citas de §7. Literales.
- Del común 06 (Carta, art. 6): las tres viñetas de §8. Literales (bloque entero).
- De RTVE `realizacion/02` sin cambios: «Es la relación de secuencias…», «En informativos y en
  programas de directo…», entrada y lista de las tres premisas. Literales (sin negrita, como declara
  la redacción).

## Lentes

- `negritas.py` contra Contrato-programa, Carta, Manual de RTVE (anexos y RNE), López Vigil, AIMC
  (Normas y Marco General): 160 negritas; 14 no halladas, todas explicadas: rótulos (Enunciado, Qué
  se puede preguntar), las copiadas del común cuyas fuentes no se pasaron (Libro de estilo, MOS,
  Avid) y la de radio-fórmula, que lleva «[…]» y se cotejó a mano (glosario 7.5, l. 275). Ninguna
  atribuida a otro apartado.
- `refutar_prosa.py`: 1 hallazgo, falso positivo («EFECTO» es cita literal del libreto).
- `indice.py`: índice correcto.
- `refutar_exactitud.py` / `refutar_modo.py`: no aplican (el tema no cita preceptos del BOE; los
  «deberán/tendrán» del Contrato-programa se cotejaron a mano: «tendrán» del ap. 99, correcto).

## Verificado y conforme

- AIMC, *Normas de radio en EGM*: definición de programa (rótulo 2/03/2010), emisión radiofónica
  (Grupo Radio AIMC 01/04/2016), tipo de emisión (cinco clases). Fechas internas 2005-2019.
- AIMC, *Marco General 2026*: tabla de minutos (p. 30 impresa) cotejada sobre la imagen de la página:
  89,4 / 40,2 / 18,7 / 15,0 / 15,5 / 96,2 / 74,6 / 70,5; generalista 48,1, temática 40,8. Curva
  horaria (p. 29): sube desde las 6:00 y su meseta va de 8:00 a 11:00. PDF creado el 11-II-2026.
- Manual de RTVE: glosario 7.5 (pauta, escaleta, guion de continuidad, sección, microespacio,
  entradilla, radio convencional, temática, radio-fórmula); 3.1 (tono comunicativo); 3.5 (formato sin
  guion).
- Contrato-programa (BOJA 245, 26-12-2023; Acuerdo de 19-12-2023): ap. 5, 15, 98 (a-e, cifras y
  salvedad «orientativos») y 99.
- López Vigil: capítulos 5 (l. 3260), 6 (l. 3667; libreto l. 4476, guion horizontal l. 4757),
  9 (l. 10715) y 11 (l. 12723) confirmados; título completo, ISBN, Quito, introducción en Lima, abril
  2005. Modelos, estructuras, secciones, revista compacta, estilo, conductores, pasos, franjas,
  periodicidad y títulos, conformes.
- Cálculo de tiempos: rehecho; todas las horas, el desfase de 1:30 y los dos ajustes cuadran.

## Correcciones aplicadas (12)

1. Ficha, Fuente: Contrato-programa «apartados 5 y 98» → «5, 15, 98 y 99» (el tema usa los cuatro).
   Error 3.
2. «**Negrita = literal de la fuente.**» pasado a redonda: no es literal de ninguna fuente.
3. López Vigil «sigue a» Martí → «remite para esto a los capítulos 4 y 5 de Josep Ma. Martí»: la
   fuente sólo lo cita en nota. Error 9.
4. «estructura que atribuye a Cristina Romo, del ITESO» → «clasificación que, dice el autor,
   estructuró con la ayuda de Cristina Romo, catedrática en Guadalajara»: matiz de la nota y sigla
   ITESO sin presentar (no se desarrolla de memoria). Errores 9 y 5.
5. «López Vigil da dos respuestas» → «tres» y se añade la tercera, literal («el mejor formato es el
   que se rompe»). Error 3.
6. «(inferencia del propio manual, que lo plantea así)» → cita literal del manual («hay que evaluar
   la mayor o menor oportunidad de un formato en función de los objetivos…»). Error 9.
7. Música «hasta el 50 %»: quitado «para revistas musicadas», que la fuente no dice. Error 9.
8. Sección fija «el consultorio» → «los consejos de una doctora» (ejemplo de la fuente).
9. «con semanas de antelación»: la fuente no da plazo; → «con antelación» + cita literal («La revista
   de hoy no se piensa hoy, ni siquiera ayer.»). Error 9.
10. Tabla de los tres documentos, escaleta, «Qué no lleva: Los textos completos» → «—»: el glosario
    no lo dice. Error 9.
11. Equivalencia pre-guion de televisión = pauta de radio: marcada «(lectura de oficio)».
12. Trazabilidad: «(la radiorrevista)» → «(«Radiorevistas»)», rótulo del capítulo 9.

Antecedentes releídos en cada pasaje cambiado («La tercera» tras «La segunda»; «el manual lo dice
así» con López Vigil delante). Nada quitado por no confirmarse.

## No verificable aquí

- El cotejo con la web del Manual de RTVE que la ficha fecha el 03-10-2026: se verificó contra el
  volcado del proyecto, no contra la web.

## Fuentes y fecha de lectura

Todas leídas el 3-X-2026 en los volcados del proyecto (`fuentes/canal-sur/radio/`,
`fuentes/canal-sur/documentos/`, `fuentes/informacion/RTVE_manual-de-estilo_{anexos,rne}.txt`);
páginas 29-30 del *Marco General* renderizadas desde el PDF.

## Ficheros tocados

- Modificado el tema 02 (12 cambios arriba). Creado este informe. Ningún otro.
