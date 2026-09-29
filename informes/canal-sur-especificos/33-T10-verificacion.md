# Realizador/a (puesto 33) · Tema 10 · Fase 3, verificación

Fecha de trabajo: 24-09-2026 (fuentes releídas el 29-09-2026, fecha del sistema). Tema:
`temas/canal-sur-especificos/33-realizador-a/10-iluminacion-para-realizacion.md` (14.961 palabras y
58 epígrafes tras la verificación, según `indice.py`; la ficha pasa a «15.000 palabras aproximadamente»).

## Pasajes copiados: comprobación de que son literales

Script de párrafos y filas (sin negritas, sin `> `, con los saltos de línea unidos) contra
`08-camara-operador/05-iluminacion-basica.md`, `08-camara-operador/09-calidad-tecnica-de-imagen.md`,
`realizacion/08-la-iluminacion.md` y `realizacion-tv/16-la-iluminacion.md`, con un diff del párrafo
más parecido para los que no salen literales:

- **Copiado del común** (08/05 y 08/09, todos los epígrafes de la lista del redactor): literal. No se
  re-verifica. La negrita de LE 5.1 sólo difiere del volcado en la ligadura «ﬁ» de «diﬁcultades».
- **Adaptado del común**: cada diff es sólo la remisión declarada: «tema 1» → «tema 8» (seis sitios),
  «tema 2» → «tema 1», «tema 14» → «tema 19», «Luz artificial» → «El regulador y el color», «véase
  «Quién responde de ella»» → «epígrafe 4, «Quién ajusta las cámaras»». Remisiones comprobadas en los
  temas de destino (balance, ND y obturación en el 8; *raccord* y sus clases en el 1; PRL en el 19),
  salvo la del contraste, que se corrige (abajo, 1).
- **Copiado de RTVE sin cambios** (`realizacion/08` § 8; `realizacion-tv/16` § 4, § 5, § 6, § 7):
  literal; la fila de clave alta sólo pierde la marca ✔. No se re-verifica.
- **Adaptado de RTVE**: las tres definiciones (confusión tonal, matización, cinefoil) son la frase de
  RTVE sin «Ésa es la respuesta oficial…»; los párrafos «No es confusión tonal, en cambio…» y «El último
  factor da un recurso de plató…» dicen lo mismo que las opciones comentadas en RTVE § 4 y § 5 (el
  diafragma no matiza la sombra; fríos y cálidos, contraste de temperatura; complementarios, contraste
  máximo). Declarados como oficio. Correctos.

## Fuentes releídas y fechas

| Fuente | Qué se cotejó | Leída |
|---|---|---|
| RD 1680/2011 (BOE-A-2011-19599), volcado local | Título, fecha y «BOE» núm. 302, de 16-XII-2011; 0902 RA 2 c) y g), contenidos (continuidad; valor expresivo); 0903 RA 1 c), RA 4 c) y e), dos contenidos; 0904 RA 1 d), RA 4 e); 0905 RA 3 d), RA 4 b) y e), RA 5 b), cuatro contenidos; 0910 RA 1 a), b) y e), RA 2 d), contenidos. Cada criterio situado en su módulo y su RA por los números de línea | 29-09-2026 |
| RD 500/2024 (BOE-A-2024-10685), art. séptimo y nota de modificaciones del RD 1680/2011 | Modifica arts. 2, 10, 12, 15 y anexos I y III; en el anexo I sólo suprime FOL, EIE y FCT y añade módulos nuevos: no toca 0902-0905 ni 0910 | 29-09-2026 |
| X Convenio RTVA, BOJA 240/2014, anexo III | Fichas 5351000 (p. 196), 5341111 (p. 133), 5341112 (p. 132), 5341210 (p. 117), 5342100 (p. 209), 5342101 (p. 186), 5341310 (p. 116): cada cita, código y página; la salvedad «no constituye una lista cerrada»; que no hay ficha llamada «control de imagen» | 29-09-2026 |
| Libro de Estilo (2004), volcado local | 5.3 (p. 82, antorcha), 6.3.4 (p. 91, las dos citas), p. 119 (maquillaje, dentro de 8.3), 8.6 (p. 121) y 8.6.1 (p. 122, puntos 1 y 2); páginas por los marcadores del volcado | 29-09-2026 |

Lentes: `negritas.py` (RD, convenio, LE): 130 negritas, 58 no halladas, todas de pasajes copiados del
común (fabricantes, UIT-R, EBU, Adobe; LE 5.1 por la ligadura); 0 mal atribuidas.
`refutar_exactitud.py` y `refutar_modo.py` con el RD: 0 hallazgos (el tema cita el RD por módulo y RA,
no por artículo; ese cotejo se hizo a mano, arriba). `refutar_prosa.py`: 0. `indice.py`: 58 epígrafes.

## Correcciones aplicadas (con el error del catálogo)

1. **1 cita cruzada**. «El contraste que admite la cámara» (adaptado del común) mandaba al tema 8 el
   margen de exposición, el *knee*, los límites de la señal, la cebra y el falso color. El tema 8 del
   puesto 33 sólo presenta el *knee* y remite los límites de la señal (EBU R 103) al tema 14; la cebra y
   el falso color no están en ningún otro tema del puesto. Queda: límites de la señal, tema 14; *knee*,
   tema 8; la cebra y el falso color, sin remisión. Lo mismo en «Lo que este tema no da».
2. **3 recuento**. Normativa: módulo 0910 con «tres contenidos» → «dos contenidos» (el tema sólo cita
   «Calidad expresiva de la luz.» y «Equipos de iluminación para espectáculos…»). Los demás recuentos
   (dos, dos, cuatro contenidos; «tres módulos», «tres reglas», «tres límites», etc.) cuadran.
3. **9 / contradicción interna**. «Lo que este tema no da» ponía el cielo cubierto entre las fuentes
   «sin preajuste publicado», y la tabla de temperaturas da el preajuste «Cloud (6500K)» de la
   Blackmagic. Se reescribe como en el tema cerrado de origen: no se ha localizado norma que fije la
   temperatura medida de vela, bombilla, amanecer, cielo cubierto o sombra; el tema da preajustes y orden.
4. Ficha: extensión 14.900 → 15.000 palabras.

## Comprobado y correcto

- Todas las citas del RD, del convenio y del Libro de Estilo, al carácter (sólo el LE conserva sus
  ligaduras «ﬁ», «ﬂ»); «Concebir la atmósfera y estructura espacial del programa» corta una tarea más
  larga, sin punto de cierre: correcto.
- Las demás remisiones: DMX512, mesa de luces, control de iluminación e instrumentos de medida (tema 4);
  estilismo y vestuario (tema 5); órdenes y ensayos (tema 6); croma (tema 9) y decorados virtuales
  (tema 12); HDR (tema 14).
- Las razones de contraste por género que el tema atribuye al tema cerrado de Cámara Operador están en
  él (2:1; 2:1 a 4:1; 8:1 y más).
- Lo escrito de nuevo como oficio (funciones narrativas, luz según el programa, planificación, causas de
  ruptura, coordinación, supuestos) va declarado así y no da cifras ni normas sin fuente.

## Lo que no se pudo confirmar

Lo mismo que declaró el redactor (organización actual de iluminación y control de cámaras en CSRTV;
norma de continuidad lumínica; pautas HDR), ya en «Lo que este tema no da».

Ficheros tocados: el tema y este informe. Scripts de cotejo, sólo en el scratchpad.
