# Grafista (15) · Tema 2 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/15-grafista/02-identidad-visual-corporativa-manual-de-marca.md`.
Fecha de trabajo del encargo: 24-09-2026. Fuentes releídas el 29-09-2026 (fecha de sistema).
Ficheros tocados: el tema y este informe. Las páginas web se descargaron a la carpeta temporal de la
sesión (fuera del repositorio).

## Copiado del común: sólo comprobación de literalidad

Cotejado por texto normalizado contra `33-realizador-a/12-grafismo-rotulacion-ra-decorados-pantallas.md`:

- «Coherencia visual: lo que exige la casa», párrafos 1 y 2 (LE 6.5 y 7.4): **literales**. El párrafo 3
  es nuevo (oficio, sin dato que verificar), como decía el redactor.
- LE 3.16.2 («Los gráﬁcos tienen que primar…», p. 58): **literal**.
- Párrafo «Las medidas: "The action safe area is 3.5%…" … (figuras 1 a 6).»: **literal**.
- La frase de presentación de la EBU R 95 (título, v1.1, junio de 2017) se cotejó con
  `fuentes/canal-sur/realizador/ebu-r095.txt`: correcta. El párrafo de 1728 / 96 / 54 y el 3456 de
  «Cuentas» coinciden con la tabla de Realizador/a (figuras 4 y 5 de la R 95).

«Copiado de RTVE sin cambios»: ninguno (el redactor lo declaró así); nada que comprobar.

## Verificado en su fuente (29-09-2026)

| Fuente | Qué se comprobó | Resultado |
|---|---|---|
| Carta 2024-2029, BOJA 247, 28-XII-2023 (`.txt`) | 10.1, 10.2, 34.1 literales; rúbricas de los arts. 10 y 34; definición «(Canal Sur)» | Correcto |
| Contrato-programa, BOJA 245, 26-XII-2023; Acuerdo de 19-XII-2023 | Puntos 105 y 112 literales, dentro de la cláusula TERCERA (líneas 598-2494); puntos 45 y 46 (Canal Sur Más, Canal Sur Media) | Literales correctos; **una glosa corregida** (abajo) |
| Libro de Estilo, 1.ª ed., marzo de 2004 | 2.3.2.4 literal y destinatario; índice del capítulo 2; búsqueda de «logotipo», «logo», «anagrama» en todo el libro | Literal correcto; **ubicación corregida** (abajo) |
| Blog «Memoranda», entrada de 1995 | Título, 9-III-1995, dos literales, 13-III-1995, fuente *Diario 2* | Correcto |
| WCAG 2.2 (copia local del puesto, 12-XII-2024) | 1.4.1 (A), 1.4.3 (AA), 1.4.11 (AA), fórmula, 1 a 21, texto grande, exención del logotipo, *relative luminance* | Literales correctos; **salvedad añadida** (abajo) |
| UCF, guía «Frutiger» | Cuatro literales (aeropuerto, Roissy/1976, legibilidad, *humanistic sans serif*) | Correcto |
| MDN `<hex-color>` (en, modificada 20-04-2026) | Dos literales; componente alfa | Correcto |
| MDN «Diseño receptivo» (es, modificada 12-09-2026) | Tres literales; `<picture>`, `srcset`, `sizes` | Literales correctos; **término corregido** |
| Analysis Function, *colours* (23-11-2021, act. 12-02-2026) y *charts* (19-05-2022) | Seis literales y fechas | Correcto |
| Torres-Martín y otros, *Fonseca* 25, 2022, pp. 95-113, DOI 10.14201/fjc.29755 (PDF) | Tres literales de Andueza y Pérez (2016, p. 127); autores; número; páginas | Correcto (la cita está en la p. 99 del artículo) |

Lo adaptado de RTVE (temas 01, 05 y 12 de diseño gráfico) no tiene fuente escrita en RTVE («va
entero como oficio»); se revisó por coherencia interna y cálculo, y sigue declarado como oficio o teoría
clásica en el texto y en «Trazabilidad». Los cálculos (21:1, 1728/3456, 2⁸, 2¹⁶, 2²⁴, `#FF0000`,
1,618 y 618) cuadran.

## Correcciones aplicadas

1. **Error 9 (afirmación sin fuente)**: «Canal Sur no ha publicado un manual de identidad» (ficha y «De
   dónde sale») → «No se ha localizado publicado…». Una ausencia no se puede afirmar; sólo que no se halló.
2. **Error 9**: «Canal Sur Más», «plataforma de vídeo a petición» → «plataforma digital de *streaming*»,
   que es como la llama el Contrato-programa (punto 45).
3. **Contradicción interna**: «cuatro cosas, y ninguna es gráfica», cuando la cuarta (blog de 1995)
   describe colores y logotipo → «y sólo la última describe algo gráfico (la imagen de 1995)».
4. **Error 8/9 (ubicación)**: LE 2.3.2.4 no está en un «capítulo de conducta»: está en el capítulo 2,
   «Valores periodísticos», apartado 2.3, «El periodista ante la información». Y «el único del Libro de
   Estilo sobre el uso del logotipo» → «el único pasaje que nombra los logotipos» (el LE habla también
   de «anagramas» ajenos en los emplazamientos del directo, que no son la marca propia).
5. **Error 6 (salvedad omitida)**: 1.4.3 tiene tres excepciones; el tema daba texto grande y logotipo y
   omitía el texto incidental. Añadida, literal. Los textos que acompañan a la marca van al 4,5:1 «o al
   3:1 si son texto grande».
6. **Error 9, resuelto a favor**: la luminancia relativa de 0 a 1 (base del 21:1) **sí** está en WCAG
   (definición *relative luminance*); añadida literal, y la definición a «Trazabilidad».
7. Precisión: «un color de marca que no llega a 4,5:1 … puede ser fondo de un titular grande (3:1)» →
   sólo si llega a 3:1.
8. **Contradicción interna** (heredada de RTVE): la tabla de bits daba 16 bits = «alta precisión por
   canal» y el párrafo siguiente, «16 bits a secas = dieciséis en total». Celda corregida.
9. MDN llama a la técnica «diseño web responsivo (RWD)», no «adaptable»: corregido donde se cita.
10. Aplicación práctica: «en web y redes, 4,5:1» → «en web … y en redes por analogía», en línea con el
    aviso de que las WCAG son para contenido web.
11. «Trazabilidad» y ficha: fechas «fase de investigación» sustituidas por la lectura de hoy; añadidas la
    guía *charts* y el artículo de *Fonseca* a la ficha, y los puntos 45-46 del Contrato-programa.

No se quitó ningún dato: todo lo que el redactor dejó para el verificador se confirmó.

## Lentes

- `negritas.py` contra las trece fuentes (Carta, Contrato-programa, LE, WCAG, R 95, blog, UCF, dos MDN,
  dos Analysis Function, artículo de *Fonseca*): 49 negritas, **0 no encontradas**, 0 mal atribuidas.
- `refutar_modo.py` (Carta y Contrato-programa): 0 hallazgos. `refutar_exactitud.py`: no aplica a
  documentos BOJA sin articulado del BOE (0 comprobadas).
- `refutar_prosa.py`: 0 hallazgos. `indice.py`: índice regenerado, 40 epígrafes.
- Extensión tras la verificación: unas 8.650 palabras de cuerpo (9.150 con índice y tablas).

## Para la refutación

- Si los «anagramas» del LE (emplazamientos del directo) merece una línea en «coherencia» o en
  derechos de imagen: fuera de este tema; no se añadió.
- El párrafo 3 de «Coherencia visual» es oficio nuevo; no es del común.
