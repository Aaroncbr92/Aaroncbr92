# Puesto 30 · Tema 8 · Revisión de los pasajes del remate (fase 5 bis)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Revisados sólo los ocho pasajes que lista
`30-T08-remate.md`, cada dato contra su fuente guardada y cada remisión contra su antecedente.

## Fuentes releídas (25-09-2026)

| Fuente | Pasajes |
|---|---|
| `fuentes/canal-sur/montador/web/xmp-adobe.txt` (Adobe, developer.adobe.com/xmp/docs) | 1 |
| `.../web/xmp-dm.txt` y `.../web/xmp-dc.txt` (adobe/xmp-docs) | 1 |
| `fuentes/canal-sur/montador/ebu/tech3293.txt` (EBU Tech 3293 v. 1.10, § 2.1, pp. 7-8) | 1 (frase sobre EBUCore) |
| `.../web/lto-compatibility.txt` (lto.org) | 2, 6, 7, 8 |
| X Convenio RTVA, `fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt`, ll. 6810-6837 (BOJA 240, p. 190) | 3 |

## Resultado

- **Citas literales**: las 14 citas nuevas (4 de XMP, 2 de espacios de nombres, 7 propiedades `xmpDM`,
  1 de LTO) se cotejaron por programa: literales. La de ISO 16684-1 difiere sólo en el espacio que
  deja el enlace antes del punto en la fuente.
- **Ficha del puesto**: ocho tareas en la ficha, la sexta citada literal; el «Cinco de sus ocho»
  cuadra. El tema 13 tiene el epígrafe «La emisión automatizada»: la remisión es buena.
- **LTO**: 30 y 40 TB literales y sin calificar de nativos; el hueco lo dice bien.
- **Portada, «Qué se puede preguntar», «Documentos técnicos», «Lo que este tema no da», «Trazabilidad»,
  índice**: coherentes con el texto; el ancla del índice coincide con el rótulo.
- **Antecedentes**: «más abajo», «ella», «esas cifras», «Una sexta», «La de compatibilidad»: todos
  con su antecedente delante.

## Correcciones aplicadas (2, error 9)

1. «su documentación nombra a Premiere **entre los programas que fijan sus propiedades**»: la página
   `xmpDM` nombra a Premiere una sola vez (en `altTapeName`). Pasa a «nombra a Premiere como el
   programa desde el que se fija una de sus propiedades».
2. «los dos vocabularios parten del mismo conjunto de elementos»: ninguna fuente leída dice que el
   «Simple Dublin Core» de EBU Tech 3293 y el «Dublin Core Metadata Element Set» de Adobe sean el
   mismo conjunto (el tema declara no haber leído la lista de elementos del Dublin Core). Se
   sustituye por lo que dicen las fuentes: «EBUCore se define como extensión del Dublin Core, y el
   espacio `dc` de XMP toma de él sus nombres y su uso».

## Lentes tras corregir

`indice.py`: 11.034 palabras, 44 epígrafes. `refutar_prosa.py`: 1 hallazgo, el previo al remate
(referencia del convenio en «Documentos técnicos» y «Trazabilidad»). Negritas limpias.

## Ficheros tocados

El tema 08 y este informe.
