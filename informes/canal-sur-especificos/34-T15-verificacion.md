# 34 · T15 · Verificación (fase 3)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/15-periodismo-de-datos-informacion-publica.md`.
Se releyó cada dato nuevo en su fuente con los nueve errores delante. No se reverificó lo listado en
«Copiado del común» del informe de redacción (Ley 9/2007 arts. 79 y 86; LTPA arts. 43 y 45; DA 2.ª
LOPDGDD). Sí se revisó lo copiado de RTVE (Gestión 29, estadística descriptiva).

## Fuentes releídas (todas el 24-09-2026)

- LTAIBG, `fuentes/canal-sur/BOE-A-2013-12887.md`: arts. 1, 2, 5, 12-24, 33, 34, DA 1.ª, DF 8.ª y 9.ª.
- LTPA, `fuentes/canal-sur/BOE-A-2014-7534.md`: arts. 2, 3, 6, 7, 8, 19, 24, 25, 26, 30-34 (y se buscó «silencio»: no aparece).
- LRISP, `fuentes/canal-sur/BOE-A-2007-19814.md`: arts. 1, 2, 3, 4, 5, 8, 9, 11.
- Libro de estilo, `fuentes/canal-sur/documentos/libro-de-estilo-333233b.txt` (ligaduras normalizadas en copia del scratchpad): 3.3, 3.12, 3.12.1, 3.16, 3.16.1, 3.16.2, 4.3.2, 4.3.2.1, 7.1.3, 7.2.2, 9.2.10.

## Correcciones aplicadas (cada una comprobada en la fuente)

1. **Silencio en la LTPA (error 8/9)**: la tabla atribuía al art. 33.1 LTPA que «rige la legislación básica» para el silencio; el 33.1 regula la reclamación, y la LTPA no regula el silencio. Ahora: la LTPA no lo regula; el 20.4 LTAIBG es básico (DF 8.ª no lo exceptúa).
2. **Cabecera de la tabla (error 6)**: «Junta de Andalucía y sus entidades instrumentales» valía sólo para el plazo del art. 32; la reclamación del 33.1 alcanza a todos los sujetos. Columna renombrada «Ley andaluza (LTPA)» y el matiz pasado a la celda del plazo.
3. **Ámbito de la LTPA (error 6)**: «la mejora para la Junta y sus entidades» omitía entidades locales, universidades, etc. (art. 3.1 d-f). Reescrito.
4. **LRISP 3.1 (errores 1 y 6)**: la definición literal es la de la letra a), que ciñe los sujetos a las letras a) y b) del art. 2; las sociedades mercantiles públicas (2.c) tienen fórmula propia en la letra b). Añadido.
5. **LTAIBG DA 1.ª.3**: se aplica «al acceso a» la información destinada a la reutilización, no a la información sin más. Corregido.
6. **LRISP art. 8 (error 4)**: «podrá estar sometida, entre otras»; el tema lo presentaba como condiciones que «obligan» e «impone». Corregidos el título del epígrafe (e índice), la línea de «Qué se puede preguntar», el cierre del §7 y la viñeta del §8.
7. **LTPA 25.2**: «valorando siempre el acceso parcial» añadía «siempre». Ajustado al texto.
8. **LTPA 6.e**: es un principio de interpretación y aplicación, no una exigencia; reformulado.
9. **LE, ficha técnica**: está en 3.12.1, no en 3.12. **Sonido y claridad**: están bajo 3.16.2; numerados.
10. **LE 9.2.10 (error 6)**: está dentro de 9.2 «Malos tratos»; salvedad añadida.
11. **Normativa que el tema invoca (error 3)**: «12 a 24» incluía el art. 21, no citado → «12 a 20, 22 a 24»; añadidas DF 8.ª LTAIBG y art. 2 LRISP.

Copiado de RTVE (error 9, afirmaciones sin apoyo o imprecisas): quitados «el error de principiante más frecuente», «se confunden a diario» y «error frecuente en informes reales»; el CV ya no es «la única» medida comparable; simetría y orden media-mediana-moda, como regla general para distribuciones unimodales; polígono de frecuencias definido con precisión. Aritmética del ejemplo recomprobada (0,05; 0,065; 0,02167/0,1472; 0,0325/0,1803): correcta. Intro del §4 ampliada al primer apartado del §6.

## Sin hallazgos

Todas las demás negritas de LTAIBG, LTPA, LRISP y LE son literales y están en el precepto citado. Salvedades del tema (LTPA 33.1 frente a 43.1; LTPA 26 y 45, LO 15/1999; LTAIBG 33.1, ministerio; LRISP 11.1, AGE) confirmadas.

## Lentes

- `negritas.py` (LTAIBG, LTPA, LRISP, LE): 146 cotejadas; 4 «no están» (3.4 LRISP con elisión «[...]»; tres del LE partidas por un salto de página): verificadas a mano, literales. 4 «otro artículo»: falsos (el precepto citado es el correcto, 24, 32, 32 y 3).
- `refutar_exactitud.py`: 15 «no literales», todos falsos (citas del LE sin fuente BOE, la columna LTPA de la tabla, la elisión de 3.4).
- `refutar_modo.py`: 0. `refutar_prosa.py`: 0.
- `indice.py`: 9.265 palabras, 41 epígrafes; ficha actualizada.

Ficheros tocados: el tema y este informe (copias de trabajo en el scratchpad).
