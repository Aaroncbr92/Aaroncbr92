# Tema 10 del específico de Grafista · Accesibilidad: contraste, legibilidad, tamaño, lectura fácil, subtítulos, pictogramas y diseño inclusivo

**Siglas**: LGCA Ley 13/2022 · LAA Ley 10/2018 · RDLeg 1/2013 · LE Libro de estilo · WCAG · CNLSE · CESyA · LSE · TDT · DVB · EPG · ARASAAC

Esqueleto para repasar, no resumen: cada línea remite a su fuente; el detalle está en el tema.

<!-- indice -->
Marco · Contraste · Legibilidad · Tamaño · Lectura fácil · Subtítulos · Pictogramas · Diseño inclusivo
<!-- /indice -->

## Marco: herramientas y obligaciones
- LGCA arts. 101-109; 101.1.d calidad = normativa UNE sin norma concreta; 101.1.e signado = criterios CNLSE.
- LGCA 102.1 lineal abierto: 80 % subtítulos (desde inicio; máxima audiencia), LSE 5 h/sem, audiodescripción 5 h/sem.
- LGCA 102.2 servicio público (Canal Sur): 90 %, LSE 15 h, audiodescripción 15 h; sin «desde el inicio» (sí en 102.1.a, 103.1.a, 104.1.a).
- LGCA 103 condicional: 30 %, LSE gradual, audiodescripción 5 h. 104 a petición: 30 %, gradual ambos.
- Carta RTVA 13.9: informativos lineales subtitulados (HbbTV, web, directo, grabado, a petición). Contrato-programa 12: subtitulados en todo soporte, LSE, OTT Canal Sur Más paulatino.
- RD 1112/2018 (desde 20-9-2018): 2.1.d sector público institucional (Ley 39/2015 2.2 a y b); RTVA/CSRTV dentro = lectura propia. 5.1 perceptibles, operables, comprensibles, robustos; 5.2 accesibilidad integral en el diseño; 6.1 normas armonizadas DOUE; 6.3 EN 301 549 V1.1.2; 6.4 actos delegados.
- RD 1112/2018 3.3 excluye multimedia directo y pregrabado de radiodifusores públicos y filiales; 3.4.e contenidos de terceros.
- Armonizada hoy: EN 301 549 V3.2.1 (2021-03), Decisión (UE) 2021/1339 (11-8-2021; efecto 12-2-2022; retira V2.1.2); UNE-EN 301549:2022 (5-I-2022); WCAG 2.1 AA (AccessibleEU).
- EN 301 549 V4.1.1 (2026-09): WCAG 2.2, no citada en DOUE; a 24-09-2026 rige V3.2.1.
- WCAG 2.2 (12-XII-2024): cumplir 2.2 = cumplir 2.0 y 2.1; no las deroga. AA = todos A y AA; AAA no recomendado como política general.
- LE 6.5.2: imagen «al servicio de la eficacia, la accesibilidad y la claridad».

## Contraste
- WCAG 1.4.3 (AA): texto e imagen de texto 4,5:1; grande 3:1. 1.4.6 (AAA): 7:1; grande 4,5:1.
- WCAG 1.4.11 (AA): 3:1 frente a colores vecinos en componentes de interfaz y objetos gráficos necesarios.
- Excepciones: inactivo, decorativo, invisible, parte de imagen con otro contenido; logotipo o marca (eslogan aparte sí sujeto: lectura propia).
- Texto grande (WCAG): 18 pt o 14 pt negrita; cuenta tamaño entregado.
- WCAG contraste = (L1 + 0,05)/(L2 + 0,05), L1 más claro; rango 1 a 21.
- WCAG luminancia sRGB: L = 0,2126 R + 0,7152 G + 0,0722 B; canal/255; ≤ 0,04045 ÷ 12,92, si no ((c + 0,055)/1,055)^2,4. Coeficientes de UIT-R BT.709 (tema 8), otra operación.
- Cuentas propias: blanco/negro 21:1; amarillo/negro 19,6:1; blanco/#767676 4,54:1; #777777 4,48:1 (solo grande); blanco/rojo 4,0:1; azul/negro 2,4:1; blanco/#CCCCCC 1,6:1. Fondo máximo para blanco: 4,5:1 → 0,183; 3:1 → 0,30.
- WCAG 1.4.1 (A): color no único medio (informar, acción, respuesta, distinguir). Daltonismo: tema 4.
- Antena: sin umbral en norma; 4,5:1 = analogía. UNE 153010 (síntesis): amarillo sobre negro primero.
- Oficio: pastilla o faldón opaco.

## Legibilidad
- Oficio: palo seco, sin trazos finos, caja baja. Frutiger: señalética del aeropuerto Charles de Gaulle.
- WCAG 1.4.12 (AA): sin pérdida con interlineado 1,5, tras párrafo 2, letras 0,12, palabras 0,16 (× cuerpo); nota 1 no obliga a usarlos; cuerpo 20 px: 30, 40, 2,4, 3,2.
- WCAG 1.4.8 (AAA): colores elegibles; ≤ 80 caracteres (40 CJK); sin justificar; interlineado 1,5, párrafo 1,5× interlineado; 200 % sin scroll horizontal; basta mecanismo del navegador.
- WCAG 1.4.5 (AA): texto real, no imagen de texto, salvo personalizable o esencial; logotipos esenciales.
- LE 3.16: no «un simple flash»; 4-5 elementos por pantalla; mínimo 8 s; sin locución apresurada.
- Rótulos: analogía 15 caracteres/s (45 = 3 s).
- WCAG 2.2.2 (A): pausar lo que empieza solo, dura > 5 s y va con otro contenido, salvo esencial.

## Tamaño
- WCAG sin cuerpo mínimo. 1.4.4 (AA): 200 % sin ayudas ni pérdida; salvo subtítulos e imágenes de texto.
- WCAG 1.4.10 (AA): 320 px CSS = 1.280 px al 400 %; excepto mapas, diagramas, vídeo.
- Grande 18 pt/14 pt negrita baja 4,5:1 a 3:1; 16 pt sin negrita no es grande.
- Antena: sin cuerpo mínimo en norma; zona segura EBU R 95 (tema 8). Oficio: salida más pequeña, nombre más largo, sin encoger.

## Lectura fácil
- RDLeg 1/2013 2.k) (Ley 6/2022, desde 2-4-2022): accesibilidad cognitiva por lectura fácil, SAAC, pictogramas y otros medios. 29 bis: condiciones básicas; .2 desarrollo normativo; .3 exigibles en plazos reglamentarios.
- LAA 9.4 (Decreto-ley 3/2024): discapacidad intelectual, programas subtitulados según lectura fácil (TV autonómica pública o privada). LGCA no la usa ni fija cuota.
- UNE 153101:2018 EX «Lectura Fácil. Pautas y recomendaciones para la elaboración de documentos» (2018-05-03; CTN 153/GT 1); UNE 153102:2018 EX validadores (2018-12-26). Texto no leído.
- Rev. Normalización Española n.º 4 (6-2018): redacción, maquetación, validación; EX por primera norma; adaptación y creación; UNESCO ≈ 30 %.
- RD 707/2026 (2-9-2026; BOE 3-9): art. 1 objeto; DF 8.ª en vigor 2-1-2027, no vigente a 24-09-2026. 3.i lectura fácil (UNE 153101); 3.j lenguaje claro (UNE-ISO 24495-1); 3.k sencillo: frases cortas, palabras comunes, sin acrónimos, imágenes; 3.b apoyos visuales.
- RD 707/2026 5.2: suelo lenguaje sencillo; 5.1.a formato pictográfico y apoyos visuales. 6.1 pfo. 2: TV por LGCA y Ley 11/2023, no obliga a TV; 6.3 web/app: normativa sectorial.
- Sin norma de subtitulado en lectura fácil.
- LE siglas: desglosar la primera vez; OTAN, no NATO; «obligatoria en las rotulaciones».

## Subtítulos
- Burgos (2020) p. 3: texto sincronizado con audio; sirve en ruido o silencio. P. 4: abiertos incrustados sin control; cerrados activables (más accesibles). Abierto = imagen del grafista; cerrado lo pinta el receptor.
- UNE 153010:2012 (30-05-2012; anula 2003) y UNE 153020:2005 (26-01-2005, audiodescripción): en vigor; de pago, por síntesis de Burgos.
- Visual (pp. 4-5): centrados abajo; 2 líneas, excepcional 3; línea por personaje; 37 caracteres/línea; contextual entre paréntesis misma línea; sin partir sílabas; pausas en comas y puntos; sin abreviaturas.
- Mayúsculas solo título y texto original en mayúsculas; cursiva: voces de TV/radio/fuera de pantalla, títulos, canciones, otro idioma; números 0-10 letra, resto cifra; paréntesis mejor que corchetes.
- Colores (p. 5), orden: amarillo/negro; verde/negro; cian/negro; magenta/negro; blanco/negro; rojo/blanco; azul/blanco; azul/amarillo. Igual para personajes.
- Tiempo (p. 6): ~15 caracteres/s; 1 línea ≈ 3 s; 2 líneas ≤ 6 s; mínimo 1 s, máximo 6 s. Cuentas: 74 ≈ 5 s; 37 ≈ 2,5 s (guía: «unos tres segundos»).
- Sonoros (p. 6): voces en off en cursiva; efectos descritos. Personajes (pp. 6-7): color, etiquetas, guiones; guiones solo con riesgo de confusión.
- Nota declarada: Burgos se contradice (contextual en paréntesis vs «en mayúsculas y entre paréntesis»); sin resolver.
- CESyA folleto TDT (fichero 2010): teletexto = caja negra; DVB = más colores, tipografías, formatos; receptor compatible con ambos; qué emite Canal Sur: no consta.
- ETSI EN 300 743 V1.6.1 (2018-10): subtítulos, logos y gráficos en flujos DVB (CLUT; MPEG-2, ISO/IEC 13818-1).
- CNLSE 6.1 y 6.3.1: subtitulado y signado «no se interfieran», «espacios diferenciados».
- Oficio: zona inferior central libre; mosca, reloj y marcador fuera de las zonas del subtítulo y del intérprete.
- LE 3.7.1: total de 10-15 s, mejor subtítulos resumidos; sin interjecciones ni onomatopeyas; voz original al inicio y final de frase. El abierto no sustituye al cerrado.
- WCAG 1.2.2 (A) grabados; 1.2.4 (AA) directo. Vídeo web Canal Sur: normativa audiovisual (RD 1112/2018 3.3); WCAG referencia.
- Consejo Audiovisual de Andalucía (2025, rec. 3): recomienda texto alternativo, subtítulos, LSE, audiodescripción en redes; ninguna norma leída obliga. Redes: abierto (oficio).

## Pictogramas
- RDLeg 1/2013 2.k): medio de accesibilidad cognitiva.
- RD 707/2026 3.l): representación visual de un referente (objeto, espacio, acción, actividad, persona); comunicación: adaptados a cada persona; señalización: estandarizados, referentes consensuados, comprensibilidad y percepción evaluadas.
- Señalización: todos, con norma. Comunicación: cada usuario; «no existe una norma técnica» (Autismo España 29-VI-2026; 30-45 % de autistas).
- RD 707/2026 7.2 («podrán regular», «se tendrán en cuenta»): e) igualdad de género; g) símbolos reconocidos internacionalmente. DA 2.ª: Real Patronato, catálogo de señalización en 3 años; público y gratuito. 6.1: no obliga a TV.
- UNE 170600:2025 diseño de pictogramas de señalización accesibles (CTN 170/GT 6; título y ficha AENOR no localizados); UNE 170601:2026 comprensibilidad (base ISO 9186-1).
- UNE-ISO 9186-1:2022 comprensibilidad (partes 2 percepción, 3 asociación); ISO 22727:2007 símbolos públicos; ISO 17724:2003 vocabulario. Señalización física; en pantalla, analogía.
- ARASAAC: marca del Gobierno de Aragón; obra colectiva Z 901-2013, Diputación General de Aragón. CC BY-NC-SA: sin ánimo lucrativo, citar fuente, autor (Sergio Palao) y propietario, misma licencia; excluido uso comercial. TV pública con publicidad: sin resolver; autorización o jurídicos.
- Oficio: icono = pictograma de señalización; no solo color; 3:1 (1.4.11); acompaña al texto.

## Diseño inclusivo
- «Diseño inclusivo» no es expresión legal. RDLeg 1/2013 2.l): diseño universal, desde el origen, sin adaptación ni diseño especializado, sin excluir productos de apoyo (redacción 2013). 2.k): accesibilidad universal presupone diseño universal, sin perjuicio de ajustes razonables. 2.m): ajustes razonables, caso particular, sin carga desproporcionada o indebida.
- RD 707/2026 4.2.a) principios: uso equitativo, flexible, intuitivo y sencillo, información perceptible, tolerancia al error, reducción del esfuerzo, control de estímulos sensoriales, tamaño y espacio. 4.º: contraste, legibilidad, lo fundamental frente a lo secundario; 3.º: organizar por relevancia; 7.º: personalizar luz, sonido, movimiento. Criterio, no obligación de antena.
- Lista de oficio: contraste, color, tamaño, alternativas textuales (WCAG 1.1.1), subtitulado, audiodescripción, intérprete, destellos.
- Guía CNLSE (2017): buenas prácticas, no norma. Cap. 5: copresentación 5.1 («no se emplea en la actualidad en España»), imagen principal 5.2, insertada 5.3 (silueta 5.3.1, ventana 5.3.2).
- Silueta: oculta solo a la persona; croma; sin contraste con la piel baja legibilidad; preferida (informe CNLSE 2015).
- CNLSE 6.1: configurable; preservar en explotaciones futuras; subtitulado y signado compatibles, ninguno sustituye al otro.
- CNLSE 6.3.1 tamaño: sin mínimo universal; CENELEC y Ofcom 1/6; UPM: SD 1/3 de columnas, HD (720p, 1080i) 1/4; ver tronco, manos, cara y labios.
- CNLSE 6.3.1: izquierda si no hay personalización; sordociegos: mayor y fondo liso oscuro; prevalece el signado; desaparece sin contenido verbal; ningún grafismo, mosca, simbología o señalética invade («escrupulosamente»); ventanas a la misma altura. 6.4: identificar en pantalla, teletexto, miniguías, EPG (icono). 6.2: preservar contraste piel/ropa/fondo.
- Canal Sur (CNLSE 5.3, 2017): Canal Sur 2 con LSE desde oct. 2012; Telesigno 1994-2012. Hoy: no consta.
- UIT-R BT.1702-3 (11/2023; 2005-2018-2019-2023): recomendación, no obligatoria; no erradica riesgo; directo escapa al radiodifusor.
- BT.1702 dir. 1: peligro si imagen oscura < 160 cd/m² y diferencia ≥ 20 cd/m² (SDR y HDR); si ≥ 160, > 1/17 Michelson (solo HDR); rojo saturado peligroso.
- BT.1702: intermitencias aisladas, dobles o triples permitidas; no secuencias con > 25 % de pantalla y > 3 intermitencias (6 cambios) por s; flancos ≥ 360 ms (50 Hz), 334 ms (60 Hz). Nota declarada: «algunos... y» sin resolver. Cortes rápidos igual; > 5 s riesgo aun conforme.
- BT.1702 dir. 2: rayas claras y oscuras discernibles; peor si cambian de dirección, oscilan, parpadean o invierten. Notas: 1 requisitos de entrega; 3 blanco SDR 200, HLG 1.000 cd/m²; 5 analizadores; anexo 2 flashes; anexo 5 menores de 20 años, ≥ 2 m.
- WCAG 2.3.1 (A): ≤ 3 destellos/s o bajo umbral; general: ≥ 10 % de luminancia relativa, oscura < 0,80; 25 % de campo de 10°. 2.3.2 (AAA): ≤ 3/s sin excepción. 2.3.3 (AAA): animación por interacción desactivable. BT.1702 (25 % pantalla, cd/m²) ≠ WCAG (10°, relativa).
- Oficio: revisar cortinillas, cabeceras, rayas, LED de videowall; infantil con más cuidado.
- LAA 9.2 (Decreto-ley 3/2024): imagen «real, positiva, digna, inclusiva y no estereotipada y/o paternalista»; oficio: figuras diversas.

## Aplicación práctica
- Errores típicos (oficio): blanco/#CCCCCC; titular en imagen; rótulo en zona del subtítulo.

## Límites declarados
- Sin umbral de contraste ni de tamaño en emisión; EN 301 549 y UNE no leídas.
- No consta: RTVA/CSRTV en RD 1112/2018; otras partes del RD 707/2026; subtitulado, LSE y BT.1702 actuales de Canal Sur.
- Carta 13.9 (BOJA 247, 28-XII-2023); Contrato-programa 12, 92 (BOJA 245, 26-XII-2023).
