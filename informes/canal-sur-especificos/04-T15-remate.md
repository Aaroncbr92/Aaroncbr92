# 04 · Ayudante de Producción · Tema 15 · Remate (fase 5)

Tema: `temas/canal-sur-especificos/04-ayudante-de-produccion/15-herramientas-ofimaticas-y-aplicaciones-de-gestion.md`.
Fecha de corte: 24-09-2026. Lecturas de esta fase: 06-10-2026 (fecha del sistema).
Ficheros tocados: el tema y este informe. Resultado: **amplía** (tres lagunas cubiertas) → procede 5 bis.

## Fuentes releídas hoy (06-10-2026)

- Cámara de Cuentas, fiscalización RTVA-CSRTV 2018 (BOJA 36/2021, `.txt`): punto 99 (línea 1997-2004),
  apartado 9.2 (salvedad de la Disposición nº 6, líneas 10215-10221), apartado 9.2.1, Comité TIC,
  funciones a) a j) (líneas 10411-10441).
- RD 311/2022 (BOE-A-2022-7191), art. 2 con `boe.py`: redacción única, vig. 05-05-2022; 2.3 leído entero.
- Soporte de Microsoft, «Conceptos básicos del diseño de una base de datos» (descarga del 06-10-2026,
  `support.microsoft.com/es-es/access/database-design-basics`): «Crear una relación uno a uno» y resumen.

## Correcciones (las dos de exactitud, comprobadas: el informe acertaba)

1. **Apartado 9.2, no 9.2.1, para la salvedad de la Disposición nº 6.** Confirmado: el texto está al
   abrir el 9.2. Cambiado en la ficha (Fuente: «apartados 9.2 y 9.2.1»), en Trazabilidad (ídem) y en
   el cuerpo: «Salvedad: el propio informe explica, al abrir ese anexo (apartado 9.2), que esa
   organización la regulaba…».
2. **Contratos fuera del ERP.** Confirmado (punto 99: «aplicativos utilizados por parte de los
   servicios jurídicos», sin conexión con SAP). Tabla de oficio: la fila del ERP queda «Pedidos,
   facturas, contabilidad»; fila nueva «Contratos | Aplicaciones de los servicios jurídicos (sin nombre
   publicado) | El informe de la Cámara de Cuentas las sitúa fuera del ERP y sin conexión con él».
   «El ERP de la RTVA»: «El único que consta con nombre en un documento publicado es el ERP; el mismo
   informe menciona además, sin nombrarlos, los aplicativos de los servicios jurídicos, en los que se
   llevan los contratos (punto 99, abajo).»

## Ampliaciones (lagunas)

1. **Relación uno a uno** (pregunta 11). «Claves y relaciones»: fila nueva en la tabla, con
   «**Otro tipo de relación es la relación de uno a uno.**», «**Para cada registro de la tabla
   Producto, existe un único registro coincidente en la tabla complementaria.**» y las dos formas de
   representarla («**Si las dos tablas tienen el mismo tema…**», «**Si las dos tablas tienen diferentes
   temas…**»); párrafo nuevo tras la tabla: consejo de **si se puede combinar la información de las dos
   tablas en una sola** y el resumen **Las relaciones de uno a uno y de uno a varios requieren columnas
   comunes. Las relaciones de varios a varios requieren una tercera tabla.** Trazabilidad de esa página
   ampliada («relaciones (uno a varios, varios a varios y uno a uno)»).
2. **Las diez funciones del Comité TIC** (pregunta 13). «entre otras funciones» → «Le corresponden diez
   funciones»; añadidas literales b), f), h), i), j). Se mantiene la salvedad de la Disposición nº 6.
3. **ENS, art. 2.3** (pregunta 14). Párrafo nuevo en «La seguridad de la información…», antes de la
   salvedad: cita literal del primer párrafo del 2.3 (entidades del sector privado con relación
   contractual, incluida la política de seguridad del art. 12) y del párrafo de los pliegos (cortado
   con «[…]»). Trazabilidad: «artículos 1.2, 2.1 y 2.3 | Objeto y ámbito del ENS, también a los
   sistemas de los contratistas». La salvedad sobre en qué letra del art. 2.2 de la Ley 40/2015 encaja
   la RTVA sigue en pie y es coherente con el 2.3 (que habla de entidades «incluidas en el ámbito»).
4. «Qué se puede preguntar»: añadidos «qué tipos de relación hay entre tablas» y «a quién se aplica el
   Esquema Nacional de Seguridad, también a los contratistas».

Antecedentes releídos: «ese anexo (apartado 9.2)» sigue a «el anexo del informe (apartado 9.2.1)»;
«el mismo artículo 2, en ese apartado 3» sigue a «artículo 2.3 del Real Decreto 311/2022»; «(punto 99,
abajo)» remite al guion de Contratos del mismo epígrafe. Sin epígrafes nuevos.

## Lentes

- `indice.py`: 10.459 palabras, 41 epígrafes (antes ~10.200); índice regenerado.
- `negritas.py` (RD 311/2022, Ley 40/2015, Cámara de Cuentas, páginas de Microsoft): todas las
  negritas nuevas, `ok`. Los «NO ESTÁ» restantes son pasajes copiados del común (Operador/a T11, cuyas
  fuentes no se pasan) y uno preexistente: «el ERP del que dispone el grupo…» no casa sólo por la
  llamada de nota pegada en el `.txt` («ERP41»); el texto es literal. No se toca.
- `refutar_exactitud.py`: la cita de los pliegos salía atribuida al art. 12 (lo nombraba la cita
  anterior); se reescribe la entradilla («el mismo artículo 2, en ese apartado 3») y desaparece. Las
  2 «no literales» restantes son del Libro de estilo (otra fuente), preexistentes.
- `refutar_modo.py`: 0 hallazgos. `refutar_prosa.py`: 1, «BUSCAR» como sigla sin presentar: es nombre de
  función de Excel, falso positivo.
