# Puesto 30 · Tema 6 · Verificación (fase 3)

Fecha: 25-09-2026 (encargo fechado 24-09-2026).
Tema: `temas/canal-sur-especificos/30-operador-a-montador-a-de-video/06-montaje-de-programas-promociones-cultura-deportes-digital.md`
(tras la verificación, `indice.py`: 6.263 palabras, 25 epígrafes).

## Fuentes releídas y fecha

| Fuente | Qué se releyó | Fecha |
|---|---|---|
| LGCA, BOE-A-2022-11311: volcado local y `boe.py precepto` en vivo (a1-39, a1-40, a1-48 a a1-51, a1-56) | Arts. 127, 128, 136, 137, 138, 139, 144; 1 redacción cada uno, vigentes desde 9-7-2022 | 25-09-2026 |
| X Convenio RTVA, BOJA 240, 10-12-2014 (txt) | Fichas 5351000 (p. 196), 5353000 (p. 111), 5212204 (p. 127), 5212206 (p. 190), 5354000 (p. 101) | 25-09-2026 |
| Libro de estilo Canal Sur 2004 (txt) | 3.4, 3.10, 5.4, 7.3, 7.3.4, 7.5, 7.5.1, 8.4, 8.4.1, 8.4.2, 9.2/9.2.12.4, 9.10, 9.10.1; páginas; ISBN y edición | 25-09-2026 |
| Mateu Torres 2024 (txt; ficha editorial.umh.es para el ISBN) | 8.1, 8.2, 9.1, 10.1, 10.2; páginas por pie impreso | 25-09-2026 |
| EVS Multicam LSM, v10.01 (manualslib 850166, pp. 28-29 y portada) y v11.00.C (manualsdir 254262, p. 97) | Numeración, teclas, ángulos, banco 10, desarrollo de LSM | 25-09-2026 |
| Carta 2024-2029 y Contrato-programa 2024-2026 (txt) | «redes sociales», «plataforma», «montaje» | 25-09-2026 |

## Pasajes copiados: sólo literalidad

- Común (Redactor/a T07 § 1, música 3.2.2; T05 § 9, viñeta 8.4): `diff`/búsqueda normalizada → literales.
- RTVE sin cambios (E10 § 5 tabla y ritmo; E08 §§ 1, 2, 5, 6 y tablas): cada línea está en su origen
  una vez quitadas las negritas → literales. No se re-verifican.

## Correcciones (error del catálogo)

1. **6 salvedad omitida** · 9.2.12.4 («La música es un aditamento impropio…») se presentaba como regla
   general; está en el capítulo 9.2 «Malos tratos», sobre reportajes de sucesos. Se dice así y se ajusta la
   deducción (§ 1) y su eco en § 3 («En programas…»).
2. **6** · «No tiene sección de Cultura»: la cultura es un área de Sociedad (7.3, p. 101). Añadida la cita.
3. **6** · 3.10: la cita se cortaba en mitad de frase; se completa («aunque el realizador puede arbitrar
   numerosas variantes estéticas…») y se añade la frase del coleo.
4. **6** · Art. 136.2: añadida la salvedad «sin perjuicio de… otras técnicas publicitarias…». Art. 138.3:
   añadido «ininterrumpido» (antes «lo mismo»).
5. **1 cita cruzada** · § 5: se decía que autopromoción *y patrocinio* alcanzan al catálogo y plataformas
   «que el art. 127.1 nombra». Corregido: 127.1 para autopromoción; 128.1 para patrocinio (plataformas y
   vídeos generados por usuarios); 136.2-3, 137.1 y 139 se ciñen al televisivo lineal.
6. **9** · Paráfrasis del 127.1 («productos derivados de programas del mismo grupo») ajustada al texto.
7. **8 artículo mal (precisión)** · «El texto completo (8.4…)» → 8.4.1 (la frase está en «La palabra justa»).
8. **9** · EVS: el manual v10.01 no dice que la letra de 547B sea la cámara (sólo el número de máquina
   /04); quitada esa atribución al manual. Añadido lo que sí dice: la tecla F repetida llama los ángulos;
   y la reserva de las listas de la página 10 (v11.00). «Lo que este tema no da» actualizado.
9. **9** · Quitada del párrafo adaptado de E08 «Todas las cámaras de un clip comparten sus tiempos de
   entrada y salida»: no consta en lo leído del manual.
10. **9 / atribución** · Mateu: el «gancho» es del propio Mateu, no de Martínez Sáez; la duración del
    tráiler la toma de Chion (añadido en cuerpo y Trazabilidad). «La más simple» (estructura interactiva
    lineal) → «La primera tipología que recoge».
11. § 1: «sólo da pautas de montaje para los formatos informativos» → «están escritas para los formatos
    informativos» (sin afirmar un absoluto no comprobado).

Confirmado sin cambios: fichas del convenio (textos, códigos y páginas); todos los preceptos LGCA citados
y su letra/apartado (128.2, 128.3.a y c, 137.1.a-b, 137.2.a-c, i, 138.1-4, 139.1-2, 144.1-4); cálculo
89 s/90 s; páginas del Libro (47, 53, 82, 103-104, 106-107, 119-120, 130-131, 167-168) y de Mateu (85-88,
93, 99-101); ISBN de ambos libros; LSM = *Live Slow Motion* (subtítulo del manual); ausencia de pautas de
montaje en Carta y Contrato-programa.

## Lentes

- `negritas.py` (LGCA, convenio, Libro, Mateu): 91 cotejadas; 8 «no están» por ligaduras «ﬁ» o saltos de
  página del txt; las 8 comprobadas a ojo y con normalización propia: literales.
- `refutar_exactitud.py` (LGCA): 3 «no literales» son falsos positivos (lee «(3.4…» y «(8.4…» del Libro
  como artículos de la ley).
- `refutar_modo.py` (LGCA): 0 hallazgos. `refutar_prosa.py`: 1 («en definitiva», dentro de cita de Mateu).
  `indice.py`: 25 epígrafes, sin incidencias.
- Releídos los pasajes cambiados: «ellos», «aquellos reportajes» y «(§ 1)» tienen su antecedente.

## Ficheros tocados

- Modificado: el tema citado arriba.
- Creado: este informe.
