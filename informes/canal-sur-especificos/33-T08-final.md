# Realizador/a (puesto 33) · Tema 8 · Revisión de lo rematado (fase 5 bis)

Fecha del encargo: 24-09-2026; revisión y lectura de fuentes: 29-09-2026. Tema:
`temas/canal-sur-especificos/33-realizador-a/08-camaras-opticas-soportes-encuadres.md`. Alcance: sólo
los cinco pasajes que lista `33-T08-remate.md`.

## Fuentes releídas (29-09-2026)

| Fuente | Dónde |
|---|---|
| EBU R 118 v2 (PDF de tech.ebu.ch) | § 1.2 (tabla de niveles), § 2.6 (Tier SP), § 2.9 (Tier 3, 33 %) |
| Blackmagic, *URSA Broadcast G2 Manual* | «Shooting at High Frame Rates» y cadencia de sensor (pp. 30-31) |
| Sony, *PXW-FS5 Operating Guide* 4-581-849-11(1) | Super Slow Motion: cadencias con 50i; «do not have sound» |
| *Libro de Estilo* RTVA 2004 | 8.4 (p. 119) y 8.4.1 (pp. 119-120) |
| RTVE `temas/realizacion/07-…` | Párrafo de los neutros (pasaje 1) |

## Comprobación por pasaje

1. **ND para abrir el diafragma**: párrafo restituido idéntico al de RTVE; va en redonda dentro del
   razonamiento declarado de oficio. Sin cambios.
2. **Estabilización en trípode**: la frase fusionada es oficio y así se marca; «la distorsión que
   advierte Sony» tiene delante la cita de la Z200 en el mismo epígrafe. Sin cambios.
3. **Alta velocidad y especiales**: todas las citas son literales (R 118 § 2.6 incluido «a
   programmes»; URSA; FS5 «100 fps, 200 fps, 400 fps, 800 fps»; LE 8.4). Cálculos correctos (25→100 =
   ×4 = dos pasos; 25→200 = ×8 = tres; 100/25 = un cuarto). Antecedentes: «el epígrafe anterior» = «La
   clasificación de la EBU…» (inmediatamente anterior); «citado en "La obturación…"» existe y contiene
   la cita de Blackmagic 25→50. Hallazgos corregidos:
   - H1 (error 6, salvedad omitida): «no computan en el cupo del material de menor calidad». La fuente
     dice «**does not usually count against any percentage of lower resolution material**». Ahora:
     «no suele computar en el porcentaje de material de menor resolución del programa (un cupo como el
     límite del nivel 3…)».
   - H2 (error 9): «A alta cadencia se nota más» no lo dice Blackmagic («Another thing to be mindful
     of…»); ahora «hay que vigilar». La prueba previa se atribuía a oficio y la pide Blackmagic en el
     pasaje ya citado en «La obturación…»: se atribuye a la fuente.
   - H3 (error 9, generalización): «La cámara lenta llega muda» apoyado sólo en la FS5. Ahora «En la
     FS5 la cámara lenta llega muda» y «Cuando es así, el sonido… lo pone el control».
   - H4 (error 9 y cita mal engarzada): «no el del espectáculo» no está en el LE; y «Si el narrador
     **«se vea obligado…»**» dejaba agramatical la cita, cuyo literal empieza «En caso de que se vea
     obligado». Reescrito con el literal «**el máximo acercamiento a la objetividad**» y la frase
     entera desde «En caso de que».
4. **Fila «Repetición»**: arrastraba H3 y H4 («porque llega muda»; «no al espectáculo»). Ahora:
   «sonido desde el control si la cámara la graba muda, como la FS5; la repetición sirve al juicio
   ecuánime del narrador (LE 8.4.1)».
5. **Accesorios**: siglas, pregunta, documentos citados y oficio, correctos. La fila de Trazabilidad de
   R 118 § 2.6 arrastraba H1: ahora «normalmente fuera del porcentaje de material de menor resolución».

## Lentes

- `refutar_prosa.py`: 0 hallazgos. `indice.py`: 18.591 palabras, 87 epígrafes (ficha: 18.500
  aproximadamente, se mantiene).

## Ficheros tocados

- El tema 08 (pasajes 3, 4 y 5) y este informe. Copia previa del tema en el directorio temporal de la
  sesión (`33T08-antes-5bis.md`).
