# Grafista (15) · Tema 3 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/15-grafista/03-grafismo-informativos-programas-deportes-promociones-continuidad-eventos.md`.
Fecha de trabajo del encargo: 24-09-2026. Fuentes leídas en esta verificación: 29-09-2026 (fecha de sistema).
Ficheros tocados: sólo el tema y este informe. Copia previa: scratchpad `15t03-antes-verif.md`.

## Lo copiado (sólo literalidad)

- **Copiado del común** (Realizador/a T12 y T3, Montador/a T6, Redactor/a T12): script de cotejo de cada
  negrita del tema contra los cuatro temas cerrados. Todas las negritas que el informe de redacción da
  por copiadas están literales en ellos (Vizrt, ATEM, IMS077_3, RD 1680/2011, LE 3.6.1, 3.16, 6.4, 6.5,
  7.4, 9.2.12.3, 9.9.1, reglas de rótulo, EBU R 95, LGCA 127, 128, 136, 137, 139, 144.4, LOREG 69.1 y
  69.7, Mateu). No re-verificados en fuente, como manda el encargo. Excepciones leídas en fuente porque
  no estaban literales en el común: LE 6.5.2 «un producto coherente…» (p. 93, confirmado) y el fragmento
  de LGCA 144.3 (confirmado).
- **Copiado de RTVE sin cambios**: literales frente a `diseno-grafico/08`, `09` y `realizacion/15`
  (tablas y frases), con una salvedad: la primera frase de «Informativos frente a programas» quita «que
  el enunciado pide» («La distinción que el enunciado pide es de criterio…»). Es una adaptación mínima,
  no cambia el sentido y va como oficio; se deja.

## Verificado en fuente (29-09-2026)

- ***Fonseca* 25 (2022), pp. 95-113** (PDF de revistas.usal.es, bajado por DOI y pasado a texto): las 21
  negritas son literales (resumen; Raunsbjerg y Sand; Andueza y Pérez, p. 127; Valero; Marín; Blanco;
  Roger, «Epsio»; Perin; gráfico 1, «elaboración propia»; entrevista a Brosel; técnicas). Afiliación
  Universidad de Málaga, confirmada.
- **LE** 7.1.2 y 7.1.3 (pp. 97-98), 8.4 y 8.4.1 (p. 119), 8.4.2 (p. 120, incluida «fiestas populares
  (Semana Santa, Rocío…)»): literales y páginas correctas.
- **Carta** 2024-2029 (BOJA 247, 28-XII-2023): arts. 13.6, 13.7, 19.1 y 19.2, literales.
  **Contrato-programa** (BOJA 245, 26-XII-2023): cláusula tercera, A, 3.1, punto 6, y punto 48, literales.
- **LGCA** (BOE, vigente hoy): arts. 127, 128, 136, 137, 139 y 144 con una sola redacción (9-7-2022);
  136.1/136.2 bien atribuidos; 137.2 tiene nueve letras (a-i).
- **LOREG** art. 69: redacción vigente desde el 2-2-2024 (BOE-A-2024-1993), confirmada; entrada «entre la
  convocatoria y la votación», confirmada.
- RD 1680/2011, BOE núm. 302, 16-XII-2011; RD 500/2024 sólo le añade el anexo III (profesorado): confirmado.
- Lo adaptado de RTVE (mosca, *pathfinder*, costuras, definición de continuidad): va declarado como oficio.

## Correcciones aplicadas

1. **Error 6 y 9 (LGCA 144)**: «Canal Sur puede emitir un resumen informativo con su señal (art. 144)»
   no está en la ley. Ahora: acontecimiento de interés general, breve resumen (144.1), sólo en
   noticiarios y programas informativos de actualidad (144.2). A 144.3 se añade la salvedad de los
   gastos técnicos.
2. **Error 9 (LE 7.1.2)**: «el tiempo de cada partido en los informativos se reparte» no está en el LE.
   Ahora dice que el Consejo de Administración de la RTVA fija las fórmulas de cobertura, con tiempo
   proporcional al apoyo en las elecciones homólogas anteriores.
3. **Error 9 (Fonseca)**: «quien organiza la competición produce la señal y su grafismo» no está en el
   artículo. Ahora: una productora oficial de la señal y un reglamento para la retransmisión televisiva
   que busca una imagen unificada (pp. 105 y 108 del artículo).
4. **Atribución (Blanco)**: el literal es del estudio, que glosa a Blanco, no una cita de Blanco. Se dice así.
5. **Siglas**: se quitan JEC y RA, que se presentaban sin usarse en el tema.
6. **Trazabilidad**: se añade 8.4.1 a la fila del LE; en la fila de *Fonseca* consta el cotejo de esta fase.

Se releyeron los pasajes cambiados: cada «apartado» y «ese artículo» tiene su antecedente.

## Lentes

- `negritas.py` (FJC, LE, Carta, Contrato-programa, LGCA, LOREG, EBU R 95, IMS077_3, RD 1680/2011):
  129 negritas; 22 «no está», todas explicadas. Las de Vizrt, Mateu y ATEM son del común, con fuente no
  pasada. LE 3.6.1 y «dos grupos humanos» también son del común. Las otras tres son de *Fonseca*, cortadas
  por guiones blandos del PDF y cotejadas a mano.
- `refutar_exactitud.py` (LGCA, LOREG): 2 «no literales». Son falsos positivos: Carta art. 13, que la
  herramienta busca en el art. 13 de la LGCA.
- `refutar_modo.py`: 0. `refutar_prosa.py`: 0. `indice.py`: 45 epígrafes, índice al día.

## Sin confirmar

Nada nuevo. Siguen declarados en el tema los huecos de la redacción: manuales de la casa, sistema de
grafismo de CSRTV, grafismo propio en retransmisiones, duraciones de promoción y señalización por edades.
