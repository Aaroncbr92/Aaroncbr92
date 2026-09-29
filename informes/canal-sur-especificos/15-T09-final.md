# Grafista (15) · Tema 9 · Revisión de lo rematado (fase 5 bis)

Tema: `temas/canal-sur-especificos/15-grafista/09-herramientas-diseno-composicion-edicion-plantillas-automatizacion.md`.
Entrada: la lista de pasajes cambiados de `15-T09-remate.md` (1 a 10). Fecha de trabajo del encargo:
24-09-2026; fuentes leídas de nuevo el 29-09-2026 (fecha del sistema), descargadas otra vez, no
tomadas de las copias del remate.
Ficheros tocados: el tema y este informe.

## Fuentes releídas (29-09-2026)

| Fuente | URL vigente | Fecha de la página |
|---|---|---|
| After Effects, «Work with Motion Graphics templates» | helpx.adobe.com/after-effects/desktop/motion-graphics/work-with-motion-graphics-templates/creating-motion-graphics-templates.html | 11-V-2026 |
| Photoshop, «Create data-driven graphics» | helpx.adobe.com/photoshop/using/creating-data-driven-graphics.html | 24-V-2023 |
| Photoshop, «Overview of Actions» | helpx.adobe.com/photoshop/desktop/automate-tasks/automation-settings-and-presets/actions-overview.html | 18-VIII-2026 |
| Photoshop, «Batch-process files» y «Create a droplet from an action» | helpx.adobe.com/photoshop/desktop/automate-tasks/process-a-batch-of-files/… | 23-II-2026 |
| *DaVinci Resolve 21 Reference Manual* (copia de la verificación) | — | julio de 2026 |

Títulos (H1) y fechas coinciden con los que da el tema. Las 8 negritas nuevas son literales; las
diferencias sólo eran espacios dobles del volcado HTML.

## Pasaje por pasaje

1. §1 «Las familias de programa» (M2): cambio de redacción, sin dato. Bien.
2. §1 «Licencias y versiones» (M1): el manual de Resolve habla de la **«free version»** (p. ej., render
   remoto: «does not work with the free version») y de la «non-studio version». Confirmado. Bien.
3. §5 «Unreal Engine 5.8»: coincide con la portada y la Trazabilidad. Bien.
4. §5 «Hacer la plantilla propia en un compositor»: cada paso contrastado con la página de After
   Effects (menú *Open in Essential Graphics*, *Primary*, propiedades en rojo, tipos admitidos,
   controles de fuente, renombrar/reordenar/agrupar/comentarios, enlace control-propiedad, destinos
   de exportación, *Set Poster Time*, vista previa, requisitos, avisos que no modifican, *File > Open
   Project*, datos CSV/TSV, tipos texto/número/color, filas mínimas y máximas). Correcciones:
   - Paso 1: la fuente dice anidar **«into the primary composition or the hierarchy»**; el tema sólo decía
     «dentro de la principal». Añadido «o de su jerarquía».
   - Cautelas (salvedad omitida, error 6): la lista de requisitos para no necesitar After Effects
     omitía que tampoco vale el material de *Dynamic Link* («Dynamic Link footage is not supported,
     such as Premiere sequences»). Añadido.
   - La glosa entre paréntesis de la cita mezclaba un dato de otra frase (el espacio de trabajo
     *Essential Graphics*); sacado a frase propia para que la glosa traduzca sólo la cita.
   - «el grupo de propiedades de datos de esa capa»: «esa capa» no tenía antecedente (se hablaba de un
     fichero). Ahora «de la capa que se ha creado con él».
5. §6 «Los *scripts*»: acción, *Batch* (origen: carpeta, subcarpetas, ficheros abiertos; destino:
   *None*, *Save and Close* que sobrescribe, *Folder*) y *droplet* (arrastrar fichero o carpeta):
   todo confirmado. Sin cambios.
6. §6 «Los datos rellenan la plantilla»: tres tipos de variable, capa de fondo, conjunto de datos,
   importación (primera línea con los nombres, un conjunto por línea, todas las variables en el
   fichero), vista previa, *Data Sets As Files* en PSD, *Apply* sobrescribe: confirmado. Corrección:
   «Se definen en *Image > Variables > Define*» tenía sujeto ambiguo (lo anterior hablaba de los
   conjuntos, que se crean en otro menú). Ahora: las variables, en *Define*; los conjuntos, en
   *Image > Variables > Data Sets*, y la importación, en *File > Import > Variable Data Sets*
   (menús leídos en la página).
7. Aplicación práctica, «Cuarenta versiones»: **recuento que no cuadra (error 3)**. «un fichero de
   texto de cuarenta líneas»: según la sintaxis de la fuente, la primera línea lleva los nombres de
   las variables y cada una de las siguientes, un conjunto; cuarenta versiones son cuarenta y una
   líneas. Corregido.
8. «Lo que este tema no da»: coherente con lo que ahora se da. Bien.
9. Portada: fuentes añadidas correctas; el tema tiene ahora 11.123 palabras («11.000
   aproximadamente» sigue valiendo).
10. Trazabilidad: títulos y fechas de las dos filas nuevas coinciden con las páginas. Bien.

Se releyeron los pasajes corregidos: cada «esa composición», «la misma página», «se generan» (las
versiones) tiene delante su antecedente.

## Lentes

- `indice.py`: 11.123 palabras, 43 epígrafes; los epígrafes no cambian, el índice sigue al día.
- `refutar_prosa.py`: los mismos 4 avisos de siglas ya aceptados (CAMIO, PRIME, XQ, LTS, nombres de
  producto). Sin repeticiones ni negritas rotas.

## Resultado

0 graves; 6 correcciones menores (1 recuento, 1 salvedad omitida, 1 precisión de la fuente, 2
antecedentes o sujetos ambiguos, 1 glosa). Ninguna corrección del remate estaba equivocada. Tema
cerrado.
