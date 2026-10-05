# Puesto 27 · Tema 19 · Verificación

Fase 3 · Verificar. Fecha de trabajo y de lectura de todas las fuentes: **05-10-2026** (el encargo fija
«hoy» en 24-09-2026; ninguna redacción usada entra en vigor entre ambas fechas).

Tema: `temas/canal-sur-especificos/27-oficial-tecnico-electricista/19-prevencion-de-riesgos-laborales-aplicada-al-puesto-de-trabajo.md`
(antes 20.974 palabras; ahora 21.305, 42 epígrafes según `indice.py`).

## Ficheros tocados

- Modificados: el tema 19 y este informe (creado). Nada más. (Los cambios que `git status` muestra en otros
  temas del 27 no son míos.)

## 1. Lo copiado: comprobación de literalidad (sin re-verificar)

Cotejo párrafo a párrafo (y fila a fila en tablas) del tema contra 32-15 y 32-14 de Productor/a, con un
guion de normalización de espacios y un `difflib` palabra a palabra sobre los párrafos que no casaban.

- Epígrafe 1 entero (l. 118-426), «Los riesgos generales» (párrafo inicial), epígrafe 3, epígrafe 4,
  «El Real Decreto 773/1997», la parte copiada de altura (anexo I.6, 4.1.1, 4.1.6, siete filas de
  escaleras) y la de cargas: **literales**.
- Únicas diferencias: exactamente los pasajes que el informe de redacción declara adaptados (tabla de
  disciplinas; «a todo el personal»; arranque de «Otros riesgos», ejemplo NTP 318 y cierre de guardias;
  entrada del epígrafe 3, letra d), salvedad del descanso, «programas», carga mental; 156.4.a), in
  itinere/misión, seguridad vial; frase de escaleras «4.2.2 a 4.2.5»; y en cargas, la supresión de la
  frase del flight case). No aparece ninguna diferencia no declarada.
- «Copiado de RTVE sin cambios»: vacío; nada que comprobar.

## 2. Lo verificado en su fuente

Leído con `boe.py precepto` (redacción vigente), DOUE en `fuentes/canal-sur/`, convenio en
`fuentes/canal-sur/documentos/x-convenio-rtva-boja-240-2014.txt` (l. 715-783, 4775-4793, 6665-6688) y
NTP 318 en `fuentes/salud-laboral/ntp-318.txt`.

| Bloque | Fuente | Resultado |
|---|---|---|
| Fichas 9311100 (pág. 185) y 9311200; art. 28.1, 29.4, 29.6, 30 del X Convenio | BOJA 240/2014 | Literal |
| Recursos preventivos | RD 39/1997 art. 22 bis (1 redacción, BOE-A-2006-9379, vig. 29-06-2006); Ley 31/1995 art. 32 bis.1, 2, 4 | Correcto |
| Riesgo eléctrico | RD 614/2001 arts. 1, 3, 4, 5; anexos I, II.A, III.A, IV.A, V.A.1 | Literal; dos salvedades omitidas (abajo) |
| Altura (nuevo) | RD 1215/1997 anexo II 4.2.5; anexo I.8 RD 614/2001 | Literal; una frase sin fuente (abajo) |
| Espacios confinados | 22 bis.1.b.4.º, .2, .3, .8.d; RD 614 anexo III.A.1 | Correcto; medidas declaradas como oficio |
| Cargas (párrafo nuevo) | RD 487/1997 anexo | «carga concentrada» no es factor del anexo (abajo) |
| Químicos | RD 374/2001 arts. 4, 5, 6, 9 (9 en redacción BOE-A-2015-7458) | Literal; salvedad y precisión (abajo) |
| Etiqueta | CLP arts. 2.3-2.6, 17.1, 20.3, anexo V; R. 2024/2865 no toca 2.3-2.6, 17, 20 ni anexo V (sólo añade puntos 39-41 al art. 2) | Correcto |
| Señalización | RD 485/1997 arts. 1, 2, 4, 5; anexos II, III.3, VII.2, 4, 8 | Literal; dos salvedades omitidas (abajo) |
| EPI (nuevo) | RD 773/1997 anexo III (bloque I, riesgos físicos); RD 614 anexos III.A.2-4, IV.A.2-3 | Literal |
| LGSS 156.4.a) | BOE-A-2015-11724 | «insolación, rayo» literal |
| Medidas en resumen, Normativa, No da, Trazabilidad | las anteriores | Correcto salvo filas corregidas |

Lentes: `negritas.py` (16 fuentes): todas las negritas de los pasajes verificados están en su fuente
(las «no encontradas» son rótulos, elisiones con […] correctas, y textos de guías y NTP de la parte
copiada); las 9 «mal atribuidas» son falsos positivos (CLP 17.1 d-h; títulos). `refutar_modo.py` con
RD 614, 374, 485, 1215: 0 hallazgos; con RD 39/1997, 7 falsos positivos (confunde los «Artículo 14…29»
de la Ley 31/1995 con los del RD). `refutar_prosa.py`: 0. `indice.py`: 42 epígrafes.

## 3. Correcciones aplicadas (cada una comprobada en la fuente)

1. **Error 3** · «De dónde sale este tema»: «siete materias» no cuadra con el paréntesis del enunciado
   (que separa EPIs, señalización y etiquetado). Ahora «sus materias» y «productos químicos y su etiquetado».
2. **Error 6** · RD 614/2001 art. 4.3: añadidas las condiciones de 4.3.a) (procedimiento del fabricante y
   verificación del material) y 4.3.b).
3. **Error 6** · Anexo II.A.1: añadido «salvo que existan razones esenciales para hacerlo de otra forma» y la
   salvedad de la señalización de la quinta etapa con las cuatro anteriores completadas.
4. **Error 9** · Plataformas elevadoras «según instrucciones del fabricante y por personal formado»: sin
   cita. Ahora con su fuente: RD 1215/1997 anexo II.1.3 y art. 5.
5. **Error 9** · Cargas: «carga concentrada» y «derramarse» no son factores del anexo del RD 487/1997;
   sustituidos por los literales «demasiado pesada» y «contenido corre el riesgo de desplazarse».
6. **Error 6** · RD 374/2001 art. 5: añadido que se aplica cuando la evaluación lo pone de manifiesto
   (5.1); «5.3» precisado como 5.3.b).
7. Art. 9.2.d RD 374/2001: «el trabajador tiene derecho» → «el empresario debe facilitar a los
   trabajadores o a sus representantes» (es lo que dice el precepto).
8. **Error 6** · RD 485/1997 anexo VII.2: los riesgos de caída/choque se señalizan con panel **o** color
   (VII.2.1.º-2.º); las franjas son para cuando es por color. VII.4.1.º: añadida la excepción de
   recipientes de corto uso. VII.4.3.º: el pictograma CLP se exige cuando el etiquetado se sustituye por
   señales y no hay equivalente; se citan VII.4.2.º y 4.3.º.
9. Tabla de señales: «Equipos de lucha contra incendios» no es tipo del art. 2; marcado «(anexo III)».
10. **Error 1 (antecedente)** · «la NTP cita» en el párrafo de la NTP 443 se refería a la NTP 318 → «la NTP 318».
11. Normativa: RD 614/2001 «Arts. 1 a 5» → «1, 3, 4 y 5» (el 2 no se cita); RD 1215/1997 añade art. 5 y
    anexo II.1.3. Trazabilidad: RD 1215/1997 con BOE-A-2004-19311 y vigencia; Ley 31/1995 art. 32 bis
    releído (1 redacción, vig. 14-12-2003). Ficha: extensión 21.305.

Pasajes cambiados releídos: cada «ese artículo», «el mismo anexo», «el 4.3», «su apartado 1» tiene su
antecedente delante.

## 4. Lo que no se ha podido confirmar (se mantiene declarado en el tema)

- Reformas del CLP anteriores a 2024/2865 y ATP del anexo V: no están en `fuentes/`; el tema ya lo dice.
- NTP sobre recintos confinados (INSST): no consultada; las medidas siguen dichas como práctica de oficio.
