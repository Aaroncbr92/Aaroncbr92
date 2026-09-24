# T07 · Refutación (fase 4, modo ahorro) · X Convenio Colectivo de la RTVA

Tema: `temas/canal-sur-comun/07-x-convenio-colectivo.md` (verificado). Un solo agente, dos lentes en
una lectura. No se ha corregido el tema. Fecha de trabajo y de lectura de las fuentes: 24-09-2026.
Solo hallazgos; lo que está bien, en el cuadro.

## 1. Exactitud contra la fuente

Sin hallazgos. Lo cotejado además de lo que ya cotejó la verificación:

- `negritas.py` con las cuatro fuentes del encargo más los documentos que el tema cita (REGCON,
  Reglamento de la Mesa, fusión, Cámara de Cuentas, Ley 7/2024, bases y programa): 383 negritas;
  1 «no está» («Enunciado del programa», etiqueta de forma ya declarada); 4 «¿ART. N?», todas
  falsos positivos: la herramienta cruza la numeración del convenio con la del ET y la Ley 8/2025
  (art. 67.18 del convenio, «en el plazo de quince días», está en su art. 67.18, línea 2145 del
  texto; las dos del ET son del art. 38.3, que el tema nombra bien; la de la Ley 8/2025 es su
  art. 18.1, que el tema nombra bien).
- Paráfrasis releídas contra el BOJA: arts. 20.1, 32 (párrafo inicial), 37, 41, 42, 52, 55, 56, 60,
  62 y 66: conformes.
- ET vigente: arts. 37.4, 37.9, 35.2, 38.3 y 48.4 (párrafos 1 a 6), conformes con el contraste.
- Título del acuerdo de fusión en «Normativa»: la fórmula «fusión por absorción de «Canal Sur
  Televisión, S.A.» a «Canal Sur Radio, S.A.»» parece invertida, pero es literal del BOJA 219/2015; no
  es hallazgo.

## 2. Cobertura

Quince preguntas en `T07-preguntas.md`: **15 enteras, 0 a medias, 0 no**, seis de aplicación
práctica. Ambas rúbricas cubiertas (articulado por capítulos; art. 33 y DT 3.ª). Sin hallazgos.

## 3. Prosa

### H1 · DT 5.ª C, tramos T5 y T6 sin antecedente · menor

- **Dónde**: «Disposiciones transitorias», *Quinta*, apartado C: «…y medio punto menos para los
  temporales de los tramos T5 y T6».
- **Qué dice**: nombra los tramos por su rótulo sin haberlos presentado; el lector no sabe a qué
  retribución corresponden (el tema solo da el primero y el último tramo por su importe).
- **Qué debería decir**: «…de los tramos T5 y T6 (de 30.001 a 40.000 € y de 22.001 a 30.000 €)».
- **Fuente literal**: DT 5.ª C, cuadro de tramos (BOJA pp. 89-90): «T6 / 22.001 hasta 30.000»;
  «T5 / 30.001 hasta 40.000»; y «que se hallaran en los tramos T5 y T6, se le reduciría en medio
  punto».
- **Gravedad**: menor (antecedente ausente; no cambia ninguna respuesta del test).

Sin más hallazgos. `refutar_prosa.py`: 7 avisos, todos ya explicados en la verificación (siglas
presentadas en el párrafo de siglas o en su paréntesis; CEMAC sin fuente que lo desarrolle, dicho
en el tema). Las dos frases repetidas («lo que no se ha podido confirmar…», «no hay acuerdo
publicado ni inscrito…») están en epígrafes distintos y cada una cierra una reserva propia
(vigencia; transitorias): se dejan, no es relleno.

## Cuadro de lentes

| Lente | Tramos mirados | Resultado |
| --- | --- | --- |
| `negritas.py` (4 fuentes del encargo + 10 documentos citados) | 383 negritas | 1 no está (etiqueta), 4 ¿ART.? falsos positivos |
| Paráfrasis contra el BOJA (muestra) | 11 artículos | 0 |
| ET vigente, contraste | 5 preceptos | 0 |
| Preguntas | 15 | 15 enteras |
| `refutar_prosa.py` | tema entero | 7 avisos ya explicados; 1 hallazgo manual (H1) |

## Ficheros tocados

- `informes/canal-sur-comun/T07-preguntas.md` (nuevo).
- `informes/canal-sur-comun/T07-refutacion.md` (este informe).
- Ningún otro.
