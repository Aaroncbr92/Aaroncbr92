# Grafista (15) · Tema 12 · Fase 5 bis (revisión de los pasajes del remate)

Tema: `temas/canal-sur-especificos/15-grafista/12-archivo-catalogacion-reutilizacion-elementos-graficos-plantillas-proyectos.md`.
Fecha del encargo: 24-09-2026; fuentes releídas el 29-09-2026 (fecha de sistema). Entrada: la lista de
pasajes de `15-T12-remate.md` (se revisaron los nueve, con detalle en 4 a 7). Ficheros tocados: el tema
y este informe (copia previa en el directorio temporal de la sesión).

## Fuentes releídas (29-09-2026)

| Fuente | Cómo | Pasajes |
|---|---|---|
| Vizrt, *Graphic Hub Administrator Guide* 3.9, «General Database Information» (con «Data Locking») | HTML descargado en el remate, texto extraído | 2, 5, 8 |
| Blackmagic Design, *DaVinci Resolve 21 Reference Manual*, pp. 95-96, 390, 392 | PDF, página a página (pymupdf) | 3, 6, 7 |
| X Convenio RTVA (BOJA 240/2014), texto local: arts. 1-3 y ficha 9420000 | grep | 1 |
| INCIBE, «Definiendo mi estrategia de copias de seguridad» | Reintento hoy: «Request Rejected». La cita no cambió en el remate (verificada en fase 3); sólo se comprobó el recuento del pasaje contra ella | 4, 7 |

Cotejo literal automático de todas las negritas de los pasajes 3, 5 y 6 contra su fuente: todas están.
La única «no» (*Power Bins*, «whatever clips… multi-user», pasaje no cambiado) es el guion de fin de
línea del PDF («multi- user»); literal.

## Correcciones aplicadas (comprobadas en la fuente)

1. **Siglas, SSFF** (error 8, menor): «donde en otros artículos dice» → «en otros pasajes (el segundo
   párrafo del mismo artículo 1, por ejemplo)»: el art. 1 usa las dos formas (líneas 171 y 174).
2. **Graphic Hub, tabla de bloqueos, *check out*** (error 9): «Lo pide el usuario» no está en la guía;
   dice **«Every file in the database can be checked out»** y que lo devuelve el usuario o lo cancela el
   administrador. Reescrita la columna con eso.
3. **Graphic Hub, *access rights*** (error 9): «Permanentes» no está en la guía (**«The database is able
   to maintain rights on files and folders»**). → «Sobre ficheros y carpetas, para user, group y world».
4. **Graphic Hub, suma para duplicados** (error 9): «Es la misma suma de verificación de "La copia
   comprobada"» → «una suma de verificación como la de…» (la guía no dice qué algoritmo usa).
5. **Power Bins, .drb sin medios** (error 6, salvedad): las frases «between projects and workstations…
   none of the actual media files are included» y «relink offline media» están en p. 390, pero en el
   apartado de los *bins* normales («Import and Export DaVinci Resolve Project Bins (.drb)»); a los *Power
   Bins* llegan por **«just like normal bins»**. El tema ahora lo dice así.
6. **Supuesto práctico, fila «Elementos comunes»** (error 6): «tienen que estar en un almacenamiento que
   vean todos los puestos» omitía la alternativa del manual (reenlazar); añadido «o pasarse aparte y
   reenlazarse», en línea con el cuerpo.

## Sin cambios (correctos)

- Pasaje 3 (*Archive*): «el manual no dice en esas páginas…»; antecedente «esas páginas» = pp. 95-96.
- Pasaje 4 (3-2-1): tres copias (el archivo más dos), dos dispositivos, una en otro edificio; cuadra con
  la cita. Pasaje 7, fila «Copias», coherente con él.
- Pasaje 5: todas las citas literales, incluido el aviso de Viz Artist 3.3.x (sección «Access Rights»).
  Antecedentes «En los dos primeros» (tabla de delante) y «esos apartados» (Locate Duplicate Files /
  Replace File References): correctos.
- Pasaje 6: «hidden by default… Show Power Bins» (p. 390), «Qué son», «Alcance» y «Para qué» (p. 392).
- Pasajes 8 y 9: coherentes con lo anterior; Adobe sigue declarado como no leído.

## Lentes

- `refutar_prosa.py`: 0 hallazgos. `indice.py`: 12.953 palabras, 37 epígrafes.

## Resultado

Seis correcciones menores (cuatro afirmaciones sin fuente o con salvedad omitida, una cita cruzada
imprecisa y un matiz del supuesto). Ningún dato nuevo sin fuente. Tema cerrado para el esquema.
