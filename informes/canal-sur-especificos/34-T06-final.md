# 34 · T06 · Fase 5 bis (revisión de los pasajes del remate)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/06-grupos-comunicacion-forta.md`.
Alcance: sólo los 10 pasajes que lista `34-T06-remate.md` (se comparó con la copia anterior al remate).

## Fuentes descargadas de nuevo hoy (24-09-2026)

- forta.es: portada (menú y pie), «Quiénes somos» (HTML), «Organización», fichas del organismo valenciano
  (CACVSA) y gallego; notas de 11/12-07-2024 (Fuertes), 14-11-2024 (35 aniversario), 14-01-2025 (Mellado),
  18-09-2025 (Ojea) y 09-07-2026 (Aura), por la API pública de la web.
- sepi.es: «Sectores», listado filtrado «Mayoritaria», ficha `/es/sectores/agencia-efe`.
- grupojoly.com: portada y «Historia del grupo». prisa.com: «Media» y «Nosotros». cope.es: portada (pie).

## Comprobación, pasaje a pasaje

| # | Pasaje | Resultado |
|---|---|---|
| 1 | Siglas de entrada (SEPI) | Correcto |
| 2 | «Qué se puede preguntar» | Correcto. Cambiado «a quién pertenece la Cadena SER» por «qué relación tiene PRISA con la Cadena SER»: la fuente da un hecho de 1985 (PRISA accionista mayoritario de SER S.A.), no la propiedad actual |
| 3-4 | Mapa y §1 EFE | Las tres citas SEPI están literales en la ficha; EFE figura en el filtro «Mayoritaria», no en «Minoritaria», sector «Comunicación» |
| 5 | Tabla de privados (PRISA, COPE, Joly) | Citas literales. PRISA: en la cronología de «Nosotros» el año va detrás del hecho: 1985 es correcto. Los enlaces bajo «Marcas» están en la página. Joly: diez cabeceras y todas sus fechas coinciden con «Historia» |
| 6 | §2 Autodefinición y 85 % | Literales. La nota de Fuertes está publicada el 12-07-2024 con fecha de cabecera «11 de julio»: «nota de 11 de julio» vale |
| 7 | §2 Miembros | Denominaciones, CACVSA, CSAG, la cita del 35 aniversario, À Punt FM y el pie (con sus variantes) coinciden. El menú da diez siglas. Los doce van en bloques con logotipo y sin puntuación |
| 8 | §2 Órganos | Nombramiento de Ojea, cita de «hoy», predecesor Laucirica («en 1995 asumió…»), Mellado 2020 y julio de 2025: literales |
| 9 | «Lo que no da» | Coherente con lo añadido |
| 10 | Trazabilidad | Fila SEPI precisada: «“Sectores”, listado de empresas de participación mayoritaria y ficha “Agencia EFE”» |

Antecedentes: «esa web» (SEPI), «la misma web» (COPE), «la del 35 aniversario», «la misma nota»,
«La ficha valenciana», «El pie de la web de FORTA»: todos tienen su referente delante.

## Lentes

`indice.py`: 15 epígrafes, 3.201 palabras (portada actualizada). `refutar_prosa.py`: sólo las siglas de
la tabla de miembros, ya presentadas en ella; sin negritas rotas.

Hallazgos: 0 errores de dato; 2 precisiones aplicadas. Ficheros tocados: el tema 06 y este informe.
