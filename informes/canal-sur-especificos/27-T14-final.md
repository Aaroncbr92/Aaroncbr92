# Fase 5 bis · Oficial Técnico Electricista (27) · Tema 14 · Medidas eléctricas e instrumentación

Revisión sólo de los pasajes que listó `27-T14-remate.md` (ficha, siglas, «Qué se puede preguntar»,
1.3, 3.5, 5.7, 6.2, «Trazabilidad»). Fuentes releídas el 05-10-2026 (reloj del sistema; «hoy» del
encargo, 24-09-2026; ninguna fuente técnica es posterior): INSST, guía de riesgo eléctrico 2020,
pp. 33-35; Megger, *Una puntada a tiempo*, pp. 10-15 y 63-64; Circutor CVM-NRG96 (M98245001-01-13A),
apdo. 1.11; Fluke Pub-ID 10562-es (5/2002), pp. 2-3.

## Comprobado sin cambios

- 1.3: las tres negritas del INSST son literales (quitado el guion blando); «obligatorio» en AT y
  «recomendable» en BT, bien atribuidos; la frase de la gama, puntas y pilas está en el apartado de AT;
  UNE-EN 61243-3, en el de BT. Antecedentes («la guía») correctos.
- 3.5: «pinza de alterna» casa con la tabla de 3.2 (transformador de corriente = sólo alterna).
- 5.7: tres métodos, 60 s, 5 a 10 minutos, fuga constante, dos ventajas, definiciones de DAR e IP,
  valores de la tabla I: todos coinciden con la fuente.
- 6.2: los dos cálculos de THD (literales del 1.11); CF = pico/rms = 1,4; CF = 2 en máquinas de
  oficina; HDF = 1,4/CF, 0,70, 20 A → 14 A; medida con TRMS que lea pico; neutro 80-130 %, orden 3,
  150 Hz: literales. «Regla general» y «sencilla fórmula», bien presentadas como no preceptivas.
- Trazabilidad: títulos, códigos y fechas (Megger 2006/2017; Fluke 2002; Circutor 01-13A) correctos.

## Corregido (comprobado en la fuente)

| Pasaje | Defecto | Corrección |
|---|---|---|
| 5.7, primer párrafo | «describe un modelo»: la fuente (p. 63) habla de la serie MIT400/2 | «dice de una serie de sus medidores (MIT400/2)» |
| 5.7, notas de la tabla | Nota ** aplicada a «los de la tabla»: en la fuente sólo marca «Above 1.6**» y «Above 4**» (excelente); se omitía su segunda frase (limpiar, tratar y secar el devanado) | Precisada la fila y añadida la frase (error 6) |
| 5.7, tercera nota | «cableado de un edificio»; *house wiring* es «cableado doméstico» (así lo traduce la propia guía, p. 11); no decía que ese tramo es «dudoso» en la tabla | Corregido y añadido |
| 5.7, doble lectura | «en un motor»: la fuente dice «motor síncrono» | Corregido |
| Siglas | HDF se usaba en 6.2 sin estar en la lista de siglas (error 5, leve: se presentaba en el texto) | Añadida |

## Lentes

`indice.py`: 14.483 palabras, 45 epígrafes. `refutar_prosa.py`: 0 hallazgos. Los pasajes cambiados no
citan norma: no se corren `refutar_exactitud.py` ni `refutar_modo.py`.

## Ficheros tocados

El tema y este informe.
