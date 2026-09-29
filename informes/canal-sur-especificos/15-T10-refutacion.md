# Grafista (15) · Tema 10 · Refutación (fase 4)

Tema: `temas/canal-sur-especificos/15-grafista/10-accesibilidad-contraste-legibilidad-tamano-lectura-facil-subtitulos-pictogramas-diseno-inclusivo.md`
(1.357 líneas, unas 16.750 palabras con ficha e índice). Fecha de trabajo del encargo: 24-09-2026;
fuentes releídas el 29-09-2026 (fecha del sistema). Refutador: no corrige; propone.

Ficheros tocados: este informe y `15-T10-preguntas.md`. Nada más (extractos de trabajo en el
scratchpad de la sesión, `t10/`).

Alcance: exactitud de todo lo que no está bajo «Copiado del común» ni «Copiado de RTVE sin cambios»
en `15-T10-redaccion.md` (lo adaptado sí); cobertura, del tema entero.

## 1. Lentes

- `negritas.py` contra RD 1112/2018 (arts. 2, 3, 5, 6), Ley 39/2015 (art. 2), RDLeg 1/2013 (art. 2),
  RD 707/2026 (volcado vigente a 02-01-2027), `wcag22.txt`, Libro de estilo (`.txt`), Carta, Contrato-
  programa, LGCA, Autismo España, Revista UNE 68, Plena Inclusión y las dos fuentes de ARASAAC: 261
  negritas, 161 «no están». Todas las no encontradas son de pasajes copiados (Burgos, CESyA, CNLSE,
  BT.1702, CAA, UNE 153101 por la Revista n.º 4), de la LAA (sin volcado; adaptado y ya verificado),
  de AccessibleEU/EN 301 549 (web) o citas del Libro de estilo que fallan sólo por las ligaduras «ﬁ»/«ﬂ»
  del `.txt` (6.5.2, 3.16 y 3.7.1: releídas a mano, literales). Una «mal atribuida» (el rótulo
  «Condiciones básicas de accesibilidad cognitiva», que también está en el RD 707/2026): falso positivo.
- `refutar_prosa.py`: un aviso, «AENOR» sin desarrollar (ya discutido en verificación; es marca).

## 2. Exactitud: comprobado sin hallazgo (29-09-2026)

RD 1112/2018 2.1.d), 3.3, 3.4.e), 5.1, 5.2, 6.1, 6.3, 6.4; Ley 39/2015 2.2 a) y b); RDLeg 1/2013 2.k),
l), m); RD 707/2026 artículo único, art. 1, 3 b) i) j) k) l), 4.2.a) 3.º y 4.º, 5.1.a), 5.2, 6.1 párr. 2.º,
6.3, 7.2 e) y g), DA 2.ª, DF 8.ª; WCAG 2.2: fecha, 1.1.1, 1.2.2, 1.2.4, 1.4.1, 1.4.3, 1.4.4, 1.4.5,
1.4.6, 1.4.10 (notas 1 y 2), 1.4.11, 1.4.12 (nota 1), 2.2.2, 2.3.1, 2.3.3, definiciones (*large scale*
y nota 1, *contrast ratio*, *relative luminance* con 0,04045, destello general, 25 % del campo de 10
grados), requisitos AA y AAA, párrafo 2.0/2.1; tabla de contrastes recalculada (21; 19,56; 4,54; 4,48;
4,00; 2,44; 1,61) y cuentas (4,57; 0,183; 0,30; 30/40/2,4/3,2); UIT-R BT.709-6 3.2 (señales con prima,
es decir, precorregidas: correcto lo que dice el tema); Libro de estilo 3.7.1, 3.16, 6.5.2 y siglas
(«cuando sea imprescindible», «Esta norma será obligatoria en las rotulaciones»); LGCA sin la expresión
«lectura fácil» (0 apariciones en el volcado); Autismo España (29-06-2026, «30 y 45%», UNE 170600:2025
y 170601:2026, CTN 170/GT 6); Revista UNE n.º 68 (abril de 2024, PNE 170600 y 170601); Plena Inclusión
(9186-1/2/3, 22727:2007, 17724:2003); ARASAAC (titularidad, licenseP2, licenseP3, CC BY-NC-SA, Sergio
Palao).

## 3. Hallazgos

**Graves: 0.**

**Menores: 5.**

1. **Error 5/9 · Siglas (línea 39-40).** ARASAAC se desarrolla como «Aragonese Portal of Augmentative and
   Alternative Communication». La única fuente leída que desarrolla la sigla (Aula Abierta de ARASAAC,
   créditos, `arasaac-condiciones.txt` l. 51) dice **«Aragonese Center of Augmentative and Alternative
   Communication (ARASAAC)»**. Propuesta: poner esa forma o quitar el desarrollo inglés y dejar «ARASAAC,
   el portal de pictogramas del Gobierno de Aragón».

2. **Error 6 · §8 «Diseño universal y ajustes razonables» (l. 988-990).** La cita del art. 4.2.a) 7.º
   termina en «…o el movimiento»» como si fuera el precepto entero, y el texto sigue: **«o informa sobre
   las condiciones ambientales para que las personas usuarias puedan usar sus propios recursos de
   apoyo.»** Propuesta: completar la cita (o marcar el corte con «…») y, si se quiere, decir que para
   el grafismo cuenta la primera alternativa. Ver pregunta 6 (a medias).

3. **Error 9 · §2, primera frase (l. 289).** «El contraste es el único requisito de legibilidad que las
   WCAG convierten en número» es demasiado absoluto: el 1.4.12 da valores (1,5; 2; 0,12; 0,16) y el
   1.4.8 (AAA, no citado) da 80 caracteres por línea e interlineado de espacio y medio. La diferencia real
   es que esos valores los debe poder imponer el usuario (1.4.12, nota 1; 1.4.8, nota 1), mientras que el
   contraste es un mínimo que cumple el propio contenido. Propuesta: «El contraste es el único requisito
   de legibilidad en el que las WCAG fijan un mínimo que el propio contenido tiene que cumplir».

4. **Error 9 (formal) · §4 «En antena» (l. 509).** Se nombra «la zona segura de grafismo de la EBU R 95»
   sin fila en «Trazabilidad» ni en «Normativa que el tema invoca»; el tema lo remite al tema 8 (y el
   tema 2 la cita con fuente, v1.1 de 2017). Propuesta: añadir «(tema 8)» a la fila de Trazabilidad de
   remisiones o una línea en Normativa «EBU R 95, sólo por remisión al tema 8».

5. **Error 6 · §7 «Qué son y dónde están en la ley» (l. 875-879).** «Lo que el reglamento pide a los
   pictogramas de señalización en los espacios públicos»: el 7.2 no «pide», da criterios que se tendrán
   en cuenta si las Administraciones **«podrán regular»** la accesibilidad cognitiva en su planificación
   urbanística, y la letra e) habla de **«pictogramas y señalizaciones»**. El paréntesis ya lo matiza en
   parte (la verificación arregló el mismo punto en §8). Propuesta: «Lo que el reglamento propone para
   los pictogramas y la señalización de los espacios públicos (artículo 7.2: criterios que las
   Administraciones tendrán en cuenta si regulan…)».

## 4. Cobertura del enunciado

Las siete rúbricas (contraste, legibilidad, tamaño, lectura fácil, subtítulos, pictogramas, diseño
inclusivo) tienen epígrafe propio, en el orden del enunciado, con aplicación práctica y cuentas.
Test: 12 enteras, 1 a medias, 2 no (`15-T10-preguntas.md`).

**Lagunas: 2** (se amplía el tema, poco texto):

1. **WCAG 1.4.8, Presentación visual (AAA)** — rúbricas legibilidad y tamaño. Mecanismo para que el
   usuario elija colores de texto y fondo; ancho no mayor de 80 caracteres (40 en CJK); texto no
   justificado; interlineado de al menos espacio y medio y espacio entre párrafos 1,5 veces mayor;
   ampliación al 200 % sin desplazamiento horizontal; nota 1 (no obliga a usar esos valores, sino a que
   haya mecanismo, que puede dar el navegador). Fuente: `wcag22.txt`, l. 493-506. Encaja en §3 «El
   espaciado» y resuelve el hallazgo 3. Pregunta 5.
2. **WCAG 2.3.2, Tres destellos (AAA)** — rúbrica diseño inclusivo (destellos). **«Web pages do not
   contain anything that flashes more than three times in any one second period.»** Es el hermano sin
   umbrales del 2.3.1 (A), y la pareja A/AAA es pregunta típica. Fuente: `wcag22.txt`, l. 712-716.
   Una frase en §8 «Movimiento y destellos». Pregunta 15. (De paso, el 1.4.9, Imágenes de texto sin
   excepción, AAA, es el hermano del 1.4.5; opcional.)

No se proponen como lagunas (huecos ya declarados en «Lo que este tema no da»): las pautas de
maquetación de la UNE 153101 y los criterios de la UNE 153010 en su texto (normas de pago), un umbral
de contraste o un cuerpo mínimo para antena, y lo propio de Canal Sur no publicado.

## 5. Extensión

16.000 palabras para siete rúbricas: el peso es lo copiado del común (unas 4.500). Las dos lagunas
suman unas 120 palabras. El recorte que propone el redactor (6.1 del CNLSE, tabla de cuotas) es
decisión del coordinador; esta refutación no lo exige.
