# Puesto 28 · Operador/a de Sonido · Tema 3 · Fase 5 bis, revisión de lo rematado

Fecha de trabajo: 25-09-2026 (el encargo fija «hoy» en 24-09-2026). Tema:
`temas/canal-sur-especificos/28-operador-a-de-sonido/03-microfonia.md`. Alcance: sólo los pasajes
que lista `28-T03-remate.md`.

## Fuentes releídas (todas el 25-09-2026)

- Royer Labs, «Ribbon Basics»: copia local `fuentes/canal-sur/sonido/fabricantes/royer-ribbon-basics.txt`.
- Neumann, página del U 87 Ai: copia local `neumann-u87ai.txt`.
- DPA, «The audio consequences of using wind, rain and virus protection…»: copia local `dpa-wind-rain-virus-protection.txt`.
- DPA *Mic University*, descargadas de nuevo con curl: «Know the basics about phantom power»;
  «A guide to pro wireless audio», partes 2, 3 y 6; «Troubleshooting wireless systems»; «Your first
  wireless system – comprehensive guide» (copias en el scratchpad de la sesión).

## Comprobado sin cambios

- Tabla de transductores, fila «De cinta» («es también dinámico»; activos): Royer, literal.
- Cinta en ocho: las seis citas de Royer, literales y con el sentido que les da el tema.
- Carga del micrófono: regla 5-10 veces, ejemplo 100 Ω → 500-1000 Ω, 3,4 kΩ y salvedad del
  dinámico, literales en la página de fantasma. «En otra de sus páginas» tiene antecedente.
- «Cómo modula»: ±40 / ±75 kHz, «must not be exceeded…» y «always equipped with a limiter…», parte 3, literales.
- Procedimiento rápido (apagar emisores, explorar, mismo grupo, canales distintos, de uno en uno) y
  la cita de repetición por canal: guía básica, literal.
- Espuma y directividad del cardioide, y el aire junto a las entradas: página de viento, literal.
- Trazabilidad, filas Royer y Neumann; «Lo que este tema no da»: conformes.

## Corregido

1. **Error 9 / 3 (recuento que no cuadra)**, «La recepción», antenas separadas: el remate decía que
   media longitud de onda «cumple las tres» cifras de DPA. Falso: a 600 MHz media onda son 25 cm, menos
   que los 30 cm de la guía básica. Se sustituye por la comparación a 600 MHz (12,5 / 25 / 30 cm) y a
   470 MHz (media onda ≈ 32 cm), y la regla «media longitud de onda y nunca menos de 30 cm». Cálculo
   añadido a la lista de cálculos de «Trazabilidad».
2. **Error 9**, U 87 Ai: «El patrón se elige con un conmutador del cuerpo, sin cambiar de cápsula»
   no está en la página de Neumann (sólo nombra conmutadores de filtro y atenuador). Quitado.
3. **Error 9 (generalización)**: «Con dos membranas se hace el micrófono de estudio de patrón
   seleccionable» y «El ejemplo clásico» no los dice ninguna fuente; queda «Un ejemplo de doble
   membrana con varios patrones es el Neumann U 87 Ai». El rótulo del párrafo pasa de «El condensador
   de varios patrones lleva doble membrana» a «El condensador de doble membrana y varios patrones».
4. **Error 9 (salvedad)**: Royer dice «Some multipattern condenser microphones…»; el tema lo
   generalizaba a «un condensador multipatrón». Ahora «los condensadores multipatrón que dan el ocho lo
   consiguen con electrónica activa».
5. «Lo que este tema no da»: «Cómo combina la electrónica las dos membranas» presuponía el mecanismo;
   pasa a «Cómo se combinan las dos membranas».

Antecedentes de los pasajes retocados releídos: «Royer añade», «las dos fuentes leídas», «las tres»
tienen su antecedente delante.

## Lentes

`refutar_prosa.py`: 0 hallazgos. Sin lentes de norma (el tema no cita norma jurídica). No cambia
ningún epígrafe: el índice no se toca.

## Otros ficheros tocados

Ninguno fuera del tema y este informe.
