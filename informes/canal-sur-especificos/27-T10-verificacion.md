# Verificación · Oficial Técnico Electricista (27) · Tema 10 · Reglamento de instalaciones térmicas en los edificios

Fase 3. Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/10-reglamento-de-instalaciones-termicas-en-los-edificios.md`
(16.401 palabras tras la verificación, 42 epígrafes). Fecha de lectura de todas las fuentes:
05-10-2026 (reloj del sistema; el encargo dice «hoy es 24-09-2026»; ninguna fuente tiene redacción
entre ambas fechas, así que no cambia nada).

Ficheros tocados: el tema y este informe. Ninguno más. (Los demás temas del puesto que `git status`
da por modificados no son obra de esta fase.)

## Alcance

- «Copiado del común» y «Copiado de RTVE sin cambios» del informe de redacción: **nada** en ambos.
  No había pasajes que comprobar con diff; se ha verificado el tema entero, incluido lo adaptado de
  RTVE.
- Fuentes releídas: RITE, `fuentes/canal-sur/BOE-A-2007-15820.md`, artículos 1 a 47 y
  disposiciones adicionales enteros; IT 1.1.4.1, IT 1.2.4.3.1, 1.2.4.3.5, 1.2.4.4, 1.2.4.5.1,
  1.2.4.5.2, 1.2.4.7, 1.2.4.8, IT 1.3.1 a 1.3.4.4.5 (salvo chimeneas), IT 2, IT 3 e IT 4 enteras,
  apéndice 1 (definición de EER). RDL 14/2022: `boe.py precepto BOE-A-2022-12925 a2-11` y `df-17`.
  Cadena de redacciones de los bloques `it1-2` e `it3-2` descargada con `boe.py` y comparada con diff
  (abajo).
- Lentes (el tema cita normas): `negritas.py` (295 negritas; 2 no encontradas = rótulos; 2
  «atribuidas a otro artículo», falsos positivos: «cuando este exista» está en el 28.1, bien citado, y
  «de acuerdo con un procedimiento reconocido» va en la columna del art. 17.1 de una tabla cuyo otro
  encabezado es el 16.3); `refutar_exactitud.py` (74 «no literales» que son todas citas a IT leídas
  como «art. 2/3/4»: la lente no trocea IT; se cotejaron a mano, todas literales); `refutar_modo.py`
  (0); `refutar_prosa.py` (0); `indice.py` (índice sin cambios).

## Reforma cruzada (aviso de `boe.py` en IT 1 e IT 3)

- **IT 3**: la redacción publicada el 02-08-2022 (BOE-A-2022-12925, sin fecha de vigencia) es
  idéntica a la de 01-07-2021 salvo dos notas «Véase el plan de choque… art. 29 del Real Decreto-ley
  14/2022». Confirma lo que dice el tema: el RDL no modificó el texto de la IT 3.8.
- **IT 1**: la redacción de BOE-A-2021-9176 (RD 390/2021, DF 2.ª, pub. 02-06-2021, vig. 03-06-2021)
  modifica la IT 1.2.4.1.2.1 (rendimientos de biomasa y prohibición de calderas y calentadores tipo B)
  antes de que el RD 178/2021 entrara en vigor. El volcado de `fuentes/canal-sur/` sirve la de
  01-07-2021 (texto anterior). **El tema no usa la IT 1.2.4.1.2.1**, así que no le afecta; se añade
  la mención en «Normativa». Aviso para quien use ese volcado en otros temas (9, 16): esa IT hay que
  leerla en la versión de BOE-A-2021-9176. No he tocado el volcado.

## Hallazgos y correcciones (todas comprobadas en la fuente antes de aplicarlas)

| # | Error | Pasaje | Corrección |
|---|---|---|---|
| 1 | 9 | 2.2: «Fuera de esos cinco casos, el control tiene que ser modulante (proporcional o por escalones)» | No lo dice la IT 1.2.4.3.1. Quitado |
| 2 | 9 | 2.2: «un dispositivo de seguridad que dispara se rearma a mano, después de ver por qué disparó» | Se deja la consecuencia (rearme manual fuera de los casos previstos) y se declara de oficio lo de buscar la causa |
| 3 | 6 | 2.2: autorregulación en edificios nuevos/existentes | Añadido «o, en casos justificados, en una zona» y «cuando sea viable técnica y económicamente» (IT 1.2.4.3.1.1) |
| 4 | 6 | 2.4: enfriamiento gratuito en sistemas mixtos | Las baterías en serie sólo con máquinas aire-agua; añadido el apartado 5 (incumplimiento justificable por la vía del art. 14.2) |
| 5 | 6 | 2.4: efecto Joule, letra c) | «sistemas de acumulación que carguen en horas valle» → con capacidad para captar en valle la demanda térmica total diaria prevista (IT 1.2.4.7.1.c) |
| 6 | 3/6 | 1.4: carné, dispensa del examen | Decía «la formación o la certificación»; el art. 42.2 dispensa las tres situaciones de b.1 (también la competencia por experiencia). Corregido; añadido «mayor de edad» (42.1.a) |
| 7 | 3 | 1.4: «Los requisitos del artículo 37 … empiezan por estos» (y cita c) y d)) | Empiezan por a) y b). Reescrito: son seis, a) a f), y se citan c) y d) tras nombrar a) y b) |
| 8 | 8 | 4.8: «exclusivamente durante el uso… » citado como IT 3.8.2.3 | Está en la IT 3.8.2.1; el «sin perjuicio… RD 486/1997» sí es 3.8.2.3. Citas separadas |
| 9 | 6 | 4.8: «Cierre automático de puertas (IT 3.8.4)» | La IT pide «un sistema de cierre de puertas adecuado, el cual podrá consistir en un sencillo brazo de cierre automático», cuando se requiera energía convencional. Añadido además el art. 29.tres del RDL 14/2022 (lo mismo «independientemente del origen renovable o no de la energía»), al que la DF 17.ª.2.c) sólo da fecha de cumplimiento (30-09-2022), no de fin |
| 10 | 9 | 6.1: tabla proyecto/memoria, fila «Planos o esquemas: Proyecto Sí» y «Cálculo… Implícito en la justificación» (de RTVE) | El art. 16.3 no enumera ni planos ni cálculo. Puesto «No lo enumera el artículo 16.3» |
| 11 | 9 | 5.1: «sólo una es obligatoria para el titular» | La inicial puede ser preceptiva (art. 24.1.c, 29.2, 30.1). Reescrito: sólo la periódica la impone con carácter general el RITE |
| 12 | 9 | 4.5: qué se mira en el tarado de seguridades y en bombas y ventiladores | La tabla 3.3 sólo nombra la operación; el detalle se declara de oficio (y en «Trazabilidad») |
| 13 | 9 | 4.6 y 4.7: cálculo del EER con la potencia absorbida; instrucciones de la IT 3.5 = «reglas de oro» | Marcados como lectura de oficio y añadidos a la trazabilidad; «potencia térmica» → «potencia frigorífica» |
| 14 | 6 | 4.7: silos de biomasa | Añadido «y no autorizado por el titular» (IT 3.5.3) |
| 15 | 9 | 4.2 y 6.1: «Confundirlas es el error más frecuente», «son las que un examen pediría», «lo más preguntable del reglamento» | Sin fuente. Quitados (no hay exámenes anteriores) |
| 16 | 5 | DN usado sin presentar (3.4) | Añadido a las siglas |
| 17 | 9 | Siglas: EER «potencia frigorífica dividida por la potencia eléctrica absorbida» | Sustituido por la definición literal del apéndice 1 |
| 18 | 1 | Portada: «artículos 1 a 4» (el 3 no se usa; falta el 8, que sí se cita) y RDL «sólo la DF 17.ª» (el tema cita también el art. 29) | Corregido: arts. 1, 2, 4, 6, 8…; RDL art. 29.uno y tres y DF 17.ª. Quitados de «Redacción que se estudia» los arts. 34, 38 y 40, que no se citan. Trazabilidad alineada (10 a 33, no 10 a 37) |
| 19 | — | Extensión | 16.100 → 16.400 palabras |

## Avisos del redactor, comprobados

1. Art. 28.1 (certificado sólo donde hay contrato obligatorio): correcto.
2. Art. 33.2 con «el aprovechamiento de energías residuales»: literal.
3. IT 3.4.1 remite a «IT 4.2.1.2 a)», que en la redacción vigente no tiene letras; el 80 % está en
   la IT 4.2.1.3.a): confirmado.
4. Cabecera de la tabla de medidas de generadores de calor («20kW», «70 kW», «P>1000kW»): así en el
   volcado; bien no reconstruirla.
5. Tabla 3.1, «Pn ≥70 kW» frente a «superior a 70 kW»: así en el BOE.
6. Art. 37.e) y RD 795/2010: el tema no lo nombra; correcto.
7. Art. 42.1.b.2: la fórmula es «deben justificar haber recibido y superado: b.2.1 … b.2.2
   Acreditar una experiencia…»; la lectura acumulativa del tema («el curso y la experiencia») es la
   del texto. Se deja.

## Comprobado sin cambios (muestra de lo que más riesgo tenía)

Art. 2.1-2.6 y tabla de reformas; art. 4, 6, 8, 10-14 (siete requisitos del art. 12: 7); art.
15-17 y 19-24 enteros, incluido el ejemplo del 24.11 (20→24 kW = 20 %; 20→26 kW = 30 %); art.
25-33 (tramos 5/70/5.000/1.000/400; cinco años del registro; validez de un año del certificado;
«podrá»/«deberá» del art. 32.2.b y 32.3.b; 3 y 6 meses); art. 35-37, 41-43. IT 1.1.4.1.2 (1,2 met,
0,5/1 clo, PPD < 10 %, 23-25/21-23 ºC, 45-60/40-50 %, 21/25 ºC, 35 %); IT 1.2.4.3.1.2 (cinco casos
de todo-nada), apartados 3, 4, 7, 8, 10 (5 m³/s); IT 1.2.4.3.5 (290 kW, UNE-EN 15232-1); IT
1.2.4.4 (ocho apartados, 70 kW y 20 kW de motor); 0,28 m³/s; 1,2 y dos tercios; IT 1.2.4.7.2-4;
IT 1.3.2-1.3.3 (cuatro pasos); IT 1.3.4.1.1.2, .3, .8; sala de máquinas (> 70 kW, dieciséis letras
a-p, 200 lux y 0,5, 1 l/(s·m²) a 100 Pa, cartel, letra p), riesgo alto (110 °C), gas (válvula
NC, reposición manual), 2,50 m y 0,5 m, 5 cm²/kW, 1,8·PN + 10·A, secuencia ventilador-caldera,
IP-33, Q = 10·A y 100 m³/h; IT 1.3.4.2 (3 kW, desconector, 1 mm y 0,25 mm, plenums, válvulas de
cierre); IT 1.3.4.4 (60 °C y 80 °C, vaina, nueve elementos de medida en > 70 kW); IT 2 (6 bar, dos
veces en ACS, 3 bar solar, líneas precargadas, UNE-EN 12599, nueve pruebas de eficiencia, niveles
del control); IT 3.1-3.3 (tabla 3.1 entera, notas, diez y veinte operaciones de la tabla 3.2,
cuarenta y tres de la 3.3 y sus periodicidades, leyenda, S* sólo en 31, 34 y 39); IT 3.4 (once
medidas de frío, 3 m/m, seis de calor, cinco años, 1.000 m²); IT 3.5-3.7; IT 3.8 (21/26 ºC, 30-70 %,
DIN A3, ± 0,5 ºC, uno cada 1.000 m², ± 1 ºC, 100 m², 1,7 m); RDL 14/2022 art. 29.uno (19/27 ºC) y
DF 17.ª.2.a) (hasta el 1-11-2023); IT 4 entera (70 kW, 80 %, EER 2, UNE-EN 15378-1, UNE EN
16798-17, quince años, cada 4 años, cada quince años, dos exenciones, bomba de calor por la IT
4.2.2).

## Para la refutación

- La aplicación al puesto declarada de oficio (CPD, sala de control, maniobras de cuadro, BMS que
  sólo arranca y para) está toda marcada en el texto y en «Trazabilidad».
- Huecos declarados, sin cambios: normativa andaluza de desarrollo; datos de las instalaciones de la
  RTVA.
