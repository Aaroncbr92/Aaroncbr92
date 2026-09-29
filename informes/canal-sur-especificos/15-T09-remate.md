# Grafista (15) · Tema 9 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/15-grafista/09-herramientas-diseno-composicion-edicion-plantillas-automatizacion.md`.
Entradas: `15-T09-refutacion.md` (0 graves, 3 menores, 1 laguna) y `15-T09-preguntas.md`.
Fecha de trabajo del encargo: 24-09-2026; fuentes leídas el 29-09-2026 (fecha del sistema).
Ficheros tocados: el tema y este informe. Las descargas de trabajo están en el scratchpad, fuera del repositorio.

**Se amplió contenido nuevo** (L1, unas 990 palabras). Hace falta la fase 5 bis sobre los pasajes 4, 5, 6 y 7.

## Fuentes leídas para comprobar cada corrección (29-09-2026)

| Fuente | Qué se comprobó |
|---|---|
| *DaVinci Resolve 21 Reference Manual* (copia de la verificación) | M1: se buscaron «purchas», «paid», «license key» y «buy». Sólo aparecen compras de terceros (CineForm, OFX, easyDCP, nube); en ninguna parte dice que Studio sea de pago. La corrección procede |
| Adobe, After Effects, «Work with Motion Graphics templates» (helpx, 11-V-2026) | L1: panel *Essential Graphics*, composición principal, propiedades admitidas, controles de fuente, grupos y comentarios, exportación y destinos, miniatura, requisitos sin After Effects, reapertura del .mogrt y datos CSV/TSV. Cuatro citas, literales |
| Adobe, Photoshop, «Create data-driven graphics» (24-V-2023) | L1: los tres tipos de variable, la capa de fondo, qué es un conjunto de datos, la importación por texto, Define / Export Data Sets As Files y que *Apply* sobrescribe el original. Dos citas, literales |
| Adobe, Photoshop, «Overview of Actions» (18-VIII-2026), «Batch-process files» y «Create a droplet from an action» (23-II-2026) | L1: definición de acción, orden *Batch* con origen y destino, *droplet*. Dos citas, literales |

Todas las negritas nuevas se compararon a máquina con el texto descargado y coinciden (8 de 8). Las
URL antiguas `helpx.adobe.com/*/using/*` redirigen a las páginas nuevas `…/desktop/…`. Con un
*User-Agent* de navegador, Akamai devuelve 403; con el de curl, las páginas se descargan.

Ninguna corrección del informe estaba equivocada, así que se aplicaron las cuatro (M1, M2, M3 y L1).

## Pasajes cambiados

1. **§1 «Las familias de programa»** (M2): «la que más se pregunta» pasa a «la que más conviene tener clara».
2. **§1 «Licencias y versiones»** (M1): «una versión gratuita y otra, Studio, con funciones que la gratuita no tiene». En la consecuencia práctica, «versión de pago» pasa a «versión Studio».
3. **§5 «Plantillas en el sistema de grafismo de directo»** (M3): «UE 5.8» pasa a «Unreal Engine 5.8».
4. **§5 «Hacer la plantilla propia en un compositor»** (L1, pregunta 15): se quita el párrafo «no se ha podido leer». En su lugar va el panel *Essential Graphics* en cuatro pasos (abrir la composición principal, añadir propiedades, ordenar los controles, exportar), las cautelas (requisitos para no necesitar After Effects, aviso de fuentes, reapertura como proyecto) y las plantillas con datos CSV/TSV. Al final se mantiene la regla de oficio. Las siglas CSV y TSV se presentan donde aparecen por primera vez.
5. **§6 «Los *scripts*»** (L1): párrafo nuevo sobre las acciones, el procesamiento por lotes y el *droplet* de Photoshop, con la cautela de oficio de hacer copia antes de un lote que guarda sobre los originales.
6. **§6 «Los datos rellenan la plantilla»** (L1, pregunta 14): nueva viñeta sobre las variables y los conjuntos de datos de Photoshop.
7. **Aplicación práctica, «Cuarenta versiones de una misma pieza»**: una frase sobre las variables de Photoshop y la acción por lotes para los carteles fijos.
8. **«Lo que este tema no da»**: ahora sólo quedan sin leer las expresiones de After Effects, Illustrator y los *scripts* de Photoshop.
9. **Portada**: en «Fuente» se añaden las ayudas de After Effects y de Photoshop. La extensión pasa a 11.000 palabras, porque el tema tiene ahora 11.064.
10. **Trazabilidad**: dos filas nuevas, una para After Effects y otra para Photoshop, leídas el 29-09-2026. En el párrafo de oficio se añade la copia de seguridad antes de un lote.

Se releyeron los pasajes 4 a 7. Cada «esa capa», «la misma página» y «ese motor» tiene delante su antecedente.

## Lentes

El tema es técnico y no cita normas, así que sólo se pasaron `indice.py` y `refutar_prosa.py`.

- `indice.py`: el índice está al día, con 11.064 palabras en 43 epígrafes. El aviso «sin portada» es de la herramienta: el tema no está en `portadas.tsv`, pero la portada existe.
- `refutar_prosa.py`: 4 avisos de siglas, que son nombres de producto o parte de un título (CAMIO, PRIME, XQ, LTS). Se aceptan igual que en la refutación. No hay relleno, repeticiones ni negritas rotas.

## Preguntas afectadas

La pregunta 14 (antes a medias) y la 15 (antes sin respuesta) se contestan ahora enteras con el tema.
