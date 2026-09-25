# Operador/a de Sonido (28) · Tema 12 · Verificación

Fase 3. Tema: `temas/canal-sur-especificos/28-operador-a-de-sonido/12-radiofrecuencia-aplicada-a-microfonia-inalambrica.md`.
Leído sólo `ENCARGO.md` del método y el enunciado del puesto.

Fecha de lectura de todas las fuentes: **25-09-2026** (el encargo fija el día de trabajo en el 24-09-2026).

## Fuentes releídas

- Orden TDF/732/2026 (BOE-A-2026-15661), volcado `fuentes/canal-sur/sonido/BOE-A-2026-15661.txt`: preámbulo,
  DA 1.ª y 2.ª, derogatoria, DF 2.ª; notas UN-17, UN-36, UN-48, UN-49, UN-81, UN-95, UN-105, UN-118, UN-119,
  UN-127, UN-151, UN-153; cuadro 790-862 MHz; `grep` de «micrófono», «PMSE», «audio» en todo el anexo
  (no hay otras notas de micrófonos; nada en 694-790 MHz ni en 2,4 GHz).
- Shure, `shure-antenna.txt` (entero, 1.058 líneas, por secciones) y `shure-selection.txt` (receptor,
  silenciador, diversidad, multitrayecto, bandas, selección de frecuencias, IM, LO/imagen, interferencias
  externas, ajuste del silenciador, comprobación previa, operación, averías, apéndice de IM).
- Tema 3 del puesto (para las remisiones DPA: 30 cm, media onda, 8 MHz, 823-832 MHz, cita del cable de AF).

## Pasajes copiados: sólo literalidad (no re-verificados)

Comprobado por programa (espacios y negritas normalizados): los cinco de «Copiado de RTVE sin cambios»
son idénticos a `sonido/13` e `informacion-grafica/06`; la tabla Banda/Grupo/Canal y sus dos párrafos
son idénticos al tema 6 de Cámara (08). Sin cambios en ellos.

## Lentes

- `negritas.py` con BOE + dos guías Shure: 165 negritas, 10 «no están», todas explicadas (rótulos; listas
  de canales en tabla del BOE, comprobadas a mano; fórmulas IM con «x» por «×»; cita de 250 kHz partida
  por salto de página, comprobada; cita DPA tomada del tema 3, comprobada allí).
- `refutar_exactitud.py` y `refutar_modo.py` con el BOE: 0 hallazgos (el CNAF no va por artículos; modo
  verbal revisado a mano: «deberán cesar», «podrán autorizarse», «autorizará», «podrá ser utilizada»).
- `refutar_prosa.py`: sólo el falso positivo «ETD». `indice.py`: sin cambios de epígrafes.

## Correcciones aplicadas (error del catálogo)

1. (9) «La banda II es la de la radio FM… 87,5 a 108 MHz» (adaptado de RTVE, «a verificar»): la cifra sí
   está en el CNAF, nota UN-17; el nombre «banda II» no está en ninguna fuente. Reescrito con UN-17 y
   cita literal; «banda II» quitado también en «Lo que este tema no da». UN-17 añadida a Normativa y
   Trazabilidad.
2. (9) «han trabajado siempre en los huecos del espectro de la televisión» (adaptado de RTVE): «siempre»
   sin fuente. Sustituido por la frase de Shure sobre canales de TV libres (dicha de EE. UU.); se
   mantiene «ese espectro» con antecedente.
3. (1) Cita del art. 85 de la Ley 11/2022: es texto del preámbulo de la orden; ahora se dice.
4. (6) UN-36: faltaba **«también con la consideración de uso común»**. Añadido.
5. (9) «Manda el texto de la nota» (UN-151): juicio sin fuente; y «los fabricantes» daban 823-832 MHz,
   DECT y 2,4 GHz, cuando la fuente (tema 3) es sólo DPA. Corregido.
6. (9) «invade la telefonía móvil» → la banda destinada a banda ancha inalámbrica y PPDR (UN-153).
7. (4) Bajar el silenciador «alarga el alcance» → Shure: «may increase the effective range».
8. (9) «La varilla corta que viene con el receptor»: Shure dice que pueden venir de cuarto o de media onda.
9. (9) Canal de 6 MHz «que es el de Estados Unidos» y «La que se usa es la log-periódica»: sin fuente
   explícita; reescrito (6 MHz como ejemplo de Shure, 8 MHz en Europa por el tema 3).
10. (6) «Do not use a 1/4-wave… remote» y «Always use 1/2-wave…» sin sus salvedades: Shure admite, como
    solución de apuro, cuarto de onda remota con amplificador o con plano de tierra. Añadido.
11. (9) «una antena sólo rinde en su banda»: Shure dice que pierde algo fuera y que VHF/UHF no se
    intercambian. Corregido con cita.
12. (9) «mínimo físico» frente a «recomendación de montaje» (Shure/DPA): calificación sin fuente.
    Reescrito; se añade la media longitud de onda de DPA (tema 3).
13. (6) Diversidad: faltaba «In most cases» antes del cuarto de onda. Añadido.
14. (6) Amplificadores de antena: faltaba que no todos los receptores dan tensión y que van junto a la
    antena. Añadido.
15. (3/9) Ejemplo de cable: «amplificador que recupere unos 2,5 dB o más» no casa con Shure («only the
    amount of gain necessary to compensate for loss in the cable»; ejemplos de ganancia neta de –1 a
    +4 dB). Reescrito.
16. (6) Distribución: el cuadro saltaba de 2 a 4-5 receptores; Shure pide activa desde más de dos, y
    no encadenar distribuidores activos más de dos niveles. Añadido.
17. (6) «Sólo cuentan los productos de orden impar»: Shure dice «In general». Corregido.
18. (3) Caso de IM: «El más cercano… 606,4 MHz»: 605,6 y 607,6 MHz están igual de cerca (0,4 MHz).
    Corregido; la conclusión (compatible) se mantiene. Recalculadas todas las cifras del caso y del
    ejemplo de tres emisores de Shure (208/192/182).
19. (9/6) «Lo que lo evita» (LO): Shure dice «will minimize»; faltaba su recomendación de apartarse
    250 kHz del oscilador local. Corregido y añadido.
20. Cobertura de la propia fuente: fila de equipos de potencia de alterna (reguladores, reactancias:
    «buzz or hum») en «De dónde vienen», y fila «Ruido con audio y RF normales / RFI muy fuerte» en la
    tabla de averías.
21. Portada: extensión 8.800 → 9.300 palabras (indice.py cuenta 9.250).

## Confirmado sin cambios

Todas las notas del CNAF (bandas, canales, potencias, canalizaciones, UN-48 frente a UN-119 y UN-151
frente al rótulo: discrepancias reales de la fuente, bien declaradas); DA 2.ª, derogatoria, DF 2.ª,
BOE núm. 173 de 17-VII-2026; todas las citas de Shure en su contexto (antenas, 10/30 dB, 15 m, altura,
45°, 40/10 cm, 5 m/1 m, cable 50/75 Ω, 3-5 dB, 3 dB por reparto, combinadores, 4 a 8 emisores,
coordinación, captura, 300 kHz-1,5 MHz, IM, 250 kHz, FI 10,7 MHz, imagen, silenciadores, multitrayecto,
tipos de diversidad, GSM, equipos digitales, reajuste automático, listas de comprobación y operación);
tabla de longitudes de onda y cuarto de onda en TDT (recalculados); autores y títulos de las guías;
el ejemplo de 200 MHz de Shure, que no cuadra con su fórmula (bien declarado).

## Ficheros tocados

- Editado el tema 12 (sólo los pasajes listados).
- Creado este informe.
- Scratchpad: copia previa del tema (`12-antes-verif.md`) y guiones de cotejo.
