# Grafista (15) · Tema 9 · Verificación (fase 3)

Tema: `temas/canal-sur-especificos/15-grafista/09-herramientas-diseno-composicion-edicion-plantillas-automatizacion.md`
(10.077 palabras, 43 epígrafes tras la verificación). Fecha de trabajo del encargo: 24-09-2026; fuentes
releídas el 29-09-2026 (fecha del sistema). Copia previa: scratchpad `15t09v/antes-verif.md`.

Ficheros tocados: sólo el tema y este informe.

## 1. Pasajes copiados: sólo comprobación de literalidad (no se re-verifican)

Cotejo mecánico (espacios normalizados; en RTVE, quitadas `**` y ✔) contra el tema de origen:

- **Copiado del común** (Montador/a 13, Realizador/a 12, Realizador/a 04), nueve pasajes: los nueve
  **literales**. Los de MOS, viñeta por viñeta; la frase que las presenta se acortó (declarado).
- **Copiado de RTVE sin cambios** (`diseno-grafico/10`): tablas (familias salvo cabecera, diferido/tiempo
  real, programas, capas, CMYK, vectorial, buscatrazos, máscara, interpolación, formatos) y frases
  **literales**. Cuatro no lo son del todo, por recortes de enlace que el redactor no declaró (sin
  cambio de contenido): «Qué es un canal[, para que la cifra signifique algo]»; «[Y] la razón es…» (TGA);
  «[La regla es la misma que la anterior vista al revés]: una luz es…»; «La palabra que decide es COPIA[,
  y la opción falsa dice «los mueve»]». Se dejan: la cifra 56 y las opciones del examen ya no están en el tema.

## 2. Lo verificado en su fuente

| Fuente (leída el 29-09-2026) | Resultado |
|---|---|
| X Convenio, BOJA 240 de 10-XII-2014, anexo III «Definición de funciones», p. 129, ficha 5345100 | Función básica y tareas, literales |
| *DaVinci Resolve 21 Reference Manual* (julio de 2026), PDF: cada página comprobada por el pie impreso | 25 citas literales; páginas 13, 215, 1226, 1634, 1640, 1728, 1775 correctas |
| Blender 5.2 LTS Manual (Glossary; Keyframes › Introduction), descargado de nuevo | *Render*, *Ray Tracing* («More accurate than Scanline, but much slower»), *Interpolation*, «a free form Bézier mode»: literales |
| Apple, *Apple ProRes* (abril de 2022), descargado de nuevo | Cita del 4444/4444 XQ, literal |
| Vizrt: *Introduction to Viz Artist* 5.3; *Viz Multiplay* 3.3 «Introduction»; *Viz Engine* 5.2 «Dual Channel Mode» | Llave de licencia, Pilot Data Server, playout, MOS, aplicación externa: literales |
| Chyron: *PRIME CG™ - 3D Real-Time Graphics* (URL canónica …/3d-real-time-graphics/); nota PRIME 5.3 (publicada el 12-02-2026) | Base Scenes, Logic-based, CAMIO, HTML Input, Playout Automation: literales |
| Epic, UE 5.8: *Motion Design Quickstart Guide*; *Setting Up Rundown Server for Motion Design* | Las cinco citas, literales |
| CasparCG, README (GitHub) | Definición, 2006, GPLv3, cliente: literales |
| Manfredi (2010), pp. 139-140 | «irán directamente a la emisión»; iNews de Avid en Canal Sur (para el párrafo adaptado «La otra vía…») |

Adaptado de RTVE (reescrito como afirmación): son **oficio**, sin fuente publicada, y así lo declara la
«Trazabilidad». Se comprobó que el sentido no cambia respecto de RTVE; nada que corregir.

## 3. Correcciones aplicadas (cada una comprobada antes en la fuente)

1. **Error 9 · Portada, siglas.** El *Libro de Estilo* de 2004 figuraba como fuente y como sigla, pero el
   tema no lo usa en ningún sitio. Quitado de «Fuente», de «Redacción que se estudia» y del párrafo de
   siglas. Añadido a «Fuente» *Introduction to Viz Artist* 5.3, que sí se cita.
2. **Error 6 · §1.** La cita de Resolve se cortaba en «color» («color correction» partido).
   Completada hasta «…within a single, easy to learn application.» (cap. 1, p. 13), con su traducción.
3. **Error 9 · §3 «Capas y nodos».** «La mezcla de dos imágenes se hace en un nodo *Merge*» no tenía cita
   (el redactor la apoyaba en p. 1728). Sustituida por el literal **«The Merge node is the primary tool
   available for compositing images together.»** (cap. 66, p. 1449; «capable of combining two inputs»).
4. **Error 9 · §3 «La máscara».** «En Fusion la máscara básica es de polígono»: la fuente dice **«The most
   used mask tool, the Polygon mask tool»** (p. 1775). Corregido a «la más usada».
5. **Error 6 · §3 «El alfa».** El borde claro se atribuía a incumplir cualquiera de las cuatro reglas; el
   manual lo liga sólo a mezclar una imagen no premultiplicada («if the image is not premultiplied…»).
   Corregido.
6. **Error 9 · §6 «Automatizar la salida».** La carpeta vigilada no es de Resolve: es del **Blackmagic
   Proxy Generator** (cap. 8, p. 215). Corregido.
7. **Error 5/1 · «Lo que este tema no da».** «El dato de Avid» sin antecedente: el texto sólo nombra
   iNews. Pasa a «El dato de iNews, de Avid, …».
8. **Trazabilidad, fila de Resolve.** Añadidas las páginas que sostienen afirmaciones nuevas: cap. 66
   (p. 1449), cap. 139 (p. 3339, Magic Mask v2 «Studio Version Only»), cap. 187 (p. 4215: **«Remote
   rendering does not work with the free version of DaVinci Resolve.»**, que sostiene el *render* remoto
   sólo en Studio y hasta ahora no tenía página). «Presentación inicial» pasa a cap. 1 (p. 13).

Releídos los pasajes cambiados: cada remisión («el manual», «la fuente», «ese panel») tiene su
antecedente delante.

## 4. Sin corregir, a la vista de la refutación

- Los módulos de integración por *scripts* sólo en Studio: sostenido por el pasaje copiado de Montador/a 13
  (cap. 201) y por «External Scripting Using: (Resolve Studio only)» (cap. 4, p. 109).
- «Resolve tiene una versión gratuita y una de pago, Studio»: el manual dice «free version»; que Studio
  sea de pago se deduce, no se lee literal.
- Los fragmentos Viz Pilot «supports scripting (Typescript)…» (§6) son parte de la cita copiada de
  Realizador/a 12 (comprobado con grep).

## 5. Lentes

Tema técnico que sólo cita el convenio (de un tema cerrado): `refutar_prosa.py`, `indice.py` y, por las
citas, `negritas.py` con todas las fuentes.

- `negritas.py`: 88 negritas cotejadas; 16 «no están», **todas en pasajes copiados del común** (Viz Pilot
  Edge, Media Encoder, MOS y rótulos de viñeta), cuyas fuentes no se volvieron a cargar. Ninguna mal atribuida.
- `refutar_prosa.py`: 3 avisos (PRIME, CAMIO, XQ), nombres de producto presentados como tales. Se aceptan.
- `indice.py`: 10.077 palabras, 43 epígrafes, índice al día.

Resultado: 8 correcciones y ningún dato quitado. Lo copiado es literal.
