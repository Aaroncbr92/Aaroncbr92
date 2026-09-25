# Puesto 08 · Tema 11 · Fase 5 · Remate

Fecha: 24-09-2026. Tema:
`temas/canal-sur-especificos/08-camara-operador/11-seguridad-del-equipo-transporte-montaje-mantenimiento.md`.
Aplica `08-T11-refutacion.md` (5 hallazgos de exactitud, 2 lagunas) y `08-T11-preguntas.md`
(a medias la 10; no la 7 y la 14). Cada corrección, comprobada antes en la fuente. Ninguna rechazada.

**Amplía contenido nuevo: sí** (art. 66 del convenio; avisos de la p. 45 y salvedad de la p. 42 de
la Z200; resto del punto 3 del anexo II; archivos de escena y LUT que conserva el reinicio). Procede
la fase 5 bis sobre los pasajes de abajo.

## Fuentes releídas (todas el 24-09-2026)

- RD 1215/1997, BOE-A-1997-17824 (`boe.py precepto` a3 y anii; volcado `boe.py norma` para las
  lentes): art. 3.5, «segundo párrafo del apartado 1»; anexo II, 1, punto 3, sus dos párrafos.
- X Convenio RTVA (`x-convenio-rtva-boja-240-2014.txt`, l. 2062-2082; BOJA núm. 240, p. 83):
  art. 66.6, 66.7, 66.8 y 66.9.
- Sony PXW-Z200 Help Guide (`.txt`): p. 42 (l. 1579-1584, salvedad del adaptador); p. 45
  (l. 1666-1668); p. 166 (l. 9802), p. 167 (l. 9820), p. 169 (l. 9853): el All Reset no borra LUT 3D
  ni archivos de escena; p. 281 (l. 15857).

## Pasajes cambiados

1. **«La cámara es un equipo de trabajo»** (hallazgo 3): tras la cita del anexo II, 1.3, se añaden
   literales la segunda frase («Tampoco podrán utilizarse sin los elementos de protección…») y el
   segundo párrafo (uso en condiciones no consideradas por el fabricante previa evaluación de riesgos).
2. **«Las baterías, primer riesgo del equipo»**: la tercera viñeta remite a la salvedad del adaptador,
   explicada en el montaje.
3. **«La alimentación: qué cable la lleva»** (hallazgo 2; pregunta 7): salvedad literal de la p. 42
   (adaptador con la cámara en marcha con batería, interruptor encendido «without problem»); y
   (laguna 2) los dos avisos literales de la p. 45: la batería puesta no se carga con el adaptador y
   se desconecta tirando de la clavija en línea recta.
4. **«Cómo se guarda una óptica»** (hallazgo 5): las razones de la tabla se declaran también oficio,
   sin fuente de fabricante; columna «Por qué, según el oficio».
5. **«Qué mantenimiento es del operador»** (hallazgo 1; pregunta 10): art. 3.5 con el literal
   «en unas condiciones tales que satisfagan las disposiciones del segundo párrafo del apartado 1»
   del mismo artículo 3.
6. **«Las piezas que se gastan»** (hallazgo 4): quitado «porque borra los ajustes del operador»; se
   añade literal que no borra los archivos de escena (p. 169) y las LUT 3D importadas (pp. 166-167);
   guardar antes la configuración se declara costumbre de oficio.
7. **«El convenio y el cuidado del material»** (laguna 1; pregunta 14): nuevo párrafo con 66.6,
   66.7 y 66.8 literales y 66.9 resumido con su fragmento literal; la frase de gradación pasa a
   leve / grave / muy grave. «La vigencia del convenio… tema 7 del común» se conserva.
8. **Ficha**: Fuente «artículos 65, 66 y 67»; Extensión «10.900 palabras aproximadamente».
9. **Normativa que el tema invoca** y **Trazabilidad**: convenio con 66.6 a 66.9; Z200 con la
   salvedad (pp. 42-45) y pp. 166-167 y 169; lista de «Oficio sin norma» con las razones de la guarda
   de la óptica y el guardado de la configuración antes del reinicio.

Releídos todos: cada «el mismo punto», «la misma página», «del mismo artículo 3», «la 9.ª» y
«entre la leve y las muy graves» tiene su antecedente delante.

## Preguntas tras el remate

La 7, la 10 y la 14 pasan a **entera**. Resultado: 15 enteras.

## Lentes

- `indice.py`: 10.884 palabras, 44 epígrafes (sin epígrafes nuevos; índice sin cambios).
- `refutar_prosa.py`: 0 hallazgos.
- `negritas.py` (RD 1215/1997, LPRL, convenio, Libro de estilo, Z200, ILCE-1, IATA): 133 negritas,
  3 «no están», los mismos falsos positivos de la verificación (dos rótulos y la cita IATA con elisión).
- `refutar_exactitud.py` (RD 1215/1997 y LPRL): 1 «no literal», el falso positivo ya conocido (punto
  17 del anexo II anclado al «artículo 2.b»).
- `refutar_modo.py`: 0 hallazgos.

## Ficheros tocados

El tema 11 y este informe. Volcado auxiliar del RD 1215/1997 en el scratchpad (fuera del repositorio).
