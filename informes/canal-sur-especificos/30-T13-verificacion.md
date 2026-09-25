# Puesto 30 · Tema 13 · Verificación (fase 3)

Fecha: 25-09-2026 (encargo fechado 24-09-2026). Tema:
`temas/canal-sur-especificos/30-operador-a-montador-a-de-video/13-automatizacion-plantillas-mam-newsroom-flujos.md`.

## Fuentes releídas y fecha

Todas releídas el 25-09-2026: X Convenio RTVA (txt, fichas 5212206 p. 190 y 5212204 p. 127; título y
anexo III); `mos.txt`, `moscur.txt`, `mosfaq.txt`; `avnews.txt`, `avpm.txt`; EBU Tech 3293 v1.10 (pp. 7-8);
Resolve 21, extractos `proxy.txt` (pp. 198, 215), `render.txt` (pp. 4185, 4193-4194, 4215), `vars.txt`
(pp. 345-346), `titles.txt` (p. 1215), `integr.txt` (p. 4418); Adobe `wb-ame.txt` y
`wb-ingest-proxy-workflow.txt`; Libro de estilo de Canal Sur (txt), 6.3 p. 91; glosario OAIS (CCSDS
650.0-M-3) para TCP/IP, XML y API; UIT BT.2100/BT.2408 para el nombre de la UIT; SMPTE ST 259 para el
nombre de la SMPTE.

## Copiados: sólo comprobación de literalidad (script de cotejo línea a línea)

- **Del común (Redactor/a T07, 351-366, 377-381, 385-398)**: literales. Sin re-verificar.
- **RTVE sin cambios**: literales salvo lo que declara el redactor (negrita y ✔ quitados; arranques
  parciales en `ing-tec-teleco/10` l. 130 y `ing-sup-teleco/14` l. 109). **Un fallo**: la regla 2 de
  degradación (`ing-sup-teleco/14`, 179-180) estaba cortada a media frase («…cuando la»); el rango
  declarado (175-180) dejaba fuera la l. 180. Restituida la línea literal.

## Hallazgos y correcciones (verificado lo nuevo y lo adaptado)

1. **Error 9.** § 4: «El más extendido [protocolo] tiene especificación publicada: MOS». Ninguna fuente
   dice que sea el más extendido (la FAQ lo llama «global industry solution»). → «Uno de ellos, con
   especificación publicada, es MOS». Es el pasaje adaptado de RTVE (punto 3).
2. **Error 6.** Resolve, segundo plano (p. 198): se omitía **«this operation is disabled by default»**.
   Añadido.
3. **Error 6.** MOS, reparto de papeles: las dos frases de la FAQ empiezan por «In General». Añadida la
   salvedad.
4. **Error 6/9.** *Render* remoto (p. 4215): la segunda condición no es «una biblioteca común», sino
   la misma biblioteca en red, otra Postgres conectada a una de las máquinas o un servidor dedicado; y
   la conclusión «sin almacenamiento compartido no hay *render* remoto» exageraba (el manual admite
   montar el volumen por red). Reescrito; añadido que con la versión gratuita no funciona.
5. **Error 8.** Carpetas vigiladas: todo está en la p. 215 (la 216 empieza en «To Remove…»). «pp. 215-216»
   → «p. 215», en el texto y en Trazabilidad.
6. **Error 8/9.** Aplicación práctica, paso 4: la «escaleta de planos» se atribuía a 6.1.2; es 6.3
   (p. 91). Citado 6.3 con su literal, releído en el Libro de estilo; añadido a Trazabilidad.
7. **Error 9.** «Avid vende por separado» Production Management: la página no habla de venta. → «presenta
   con página propia».
8. **Error 9.** Siglas: «UER en español» sin fuente leída. Quitado; queda «Unión Europea de
   Radiodifusión (EBU, *European Broadcasting Union*)», como en el tema 4 verificado.
9. **Forma.** «Qué sistema consta:» estaba antes del párrafo del Libro de estilo sobre los textos del
   redactor; movido delante del párrafo de Manfredi, que es el que lo responde. Quitada una línea en
   blanco doble tras la tabla de degradación.

Confirmado sin cambios: tareas de las fichas 5212206 y 5212204 (literales, páginas y anexo III); MOS
(definición, objetos, tres tipos de mensajes, objetivos, versiones y fechas, 1998, «more than 150»,
carácter no oficial); Avid (todas las citas); EBUCore (citas y páginas); Resolve (cola, *presets* .xml,
variables con % y «12_A_3», fecha/hora, rótulos, *plugins* y MAM); Adobe (cola, *preset* por defecto y
su salvedad, *proxies*). Recuentos (cinco funciones, tres mensajes, tres versiones, tres condiciones,
cuatro vías, tres redes) cuadran.

Queda como oficio declarado (sin fuente): la expansión de PAM («como lo nombra la industria»), igual que
en el tema 3.

## Lentes

Tema técnico sin norma legal. `negritas.py` contra las 16 fuentes: 89 negritas, 18 «no están»: rótulos
de viñeta, la cita MOS (artefacto «P rotocol» del volcado; cotejada a mano), la del Libro de estilo con
«[...]» y las de Manfredi (copiado del común). `refutar_prosa.py`: 1 hallazgo, falso positivo (MAM en el
título). `indice.py`: 8.423 palabras; Extensión 8.300 → 8.400.

## Ficheros tocados

El tema 13 y este informe.
