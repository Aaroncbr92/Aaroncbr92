# 34 · T06 · Remate (fase 5)

Fecha: 24-09-2026. Tema: `temas/canal-sur-especificos/34-redactor-a/06-grupos-comunicacion-forta.md`
(2.512 → 3.193 palabras). Entradas: `34-T06-refutacion.md` y `34-T06-preguntas.md`.
**Ha habido ampliación con contenido nuevo** (L1-L4 y G1): procede la fase 5 bis sobre los pasajes listados abajo.

## Fuentes releídas para comprobar cada corrección (todas el 24-09-2026)

- forta.es: portada (menú de siglas), «Quiénes somos» (HTML), «Organización», ficha del organismo valenciano;
  notas 11-07-2024 (Fuertes), 14-11-2024 (35 aniversario), 14-01-2025 (Mellado), **18-09-2025 (Ojea, nueva)**,
  09-07-2026 (Aura), leídas por la API pública de la web.
- sepi.es: «Sectores», listado de participación mayoritaria y ficha «Agencia EFE».
- grupojoly.com: portada e «Historia»; prisa.com: «Media» y «Nosotros»; cope.es (pie).
- No accesibles: mediaset.es (403), cadenaser.com (403), gcope.es y prisamedia (502/sin respuesta), MFE sin texto de canales.

## Decisión sobre cada hallazgo

| # | Decisión | Qué dice la fuente |
|---|---|---|
| G1 | **Aplicado, corregido**. El informe acertaba en que las siglas sí constan, pero CRTVG no es la sigla vigente | Ficha valenciana: «Corporació Audiovisual de la Comunitat Valenciana S.A (CACVSA)»; nota 18-09-2025: «Corporación de Servicios Audiovisuales de Galicia (CSAG)». La nota del 35 aniversario usa CVMC y CRTVG (marcas de grupo): se cita literal como tal |
| M1 | **No aplicado: el informe se equivocó.** La página «Organización» está al día | Nota 18-09-2025: la Junta General «ha designado hoy a Fernando R. Ojea como nuevo secretario general… por unanimidad»; sucede a Laucirica («en 1995 asumió la Secretaría General»). Se añade esa fecha en lugar de la salvedad propuesta |
| M2 | Aplicado | «Sociedades mercantiles» → «Empresas privadas» |
| M3 | Aplicado | En el HTML de «Quiénes somos» los doce van en bloques sin puntuación: negrita sólo para la frase introductoria y para cada denominación en la tabla |
| M4 | Aplicado | Nota 14-01-2025: «ya fue presidente de FORTA a lo largo del primer semestre de 2020» |
| L1 | Ampliado | SEPI: EFE en participación mayoritaria, «100 % Participación SEPI»; autodefinición y delegaciones |
| L2 | Ampliado | Grupo Joly: «el primer grupo editorial andaluz», 1867, «diez periódicos» con sus fechas |
| L3 | Ampliado en parte | PRISA: autodefinición de PRISA Media, marcas enlazadas, SER y LOS40 vía SER S.A. (1985). COPE: «© Radio Popular S.A. - COPE» y «la Cadena COPE y TRECE». **Canales de Mediaset: siguen sin fuente legible; hueco mantenido** (pregunta 11 sigue en «no») |
| L4 | Ampliado | Nota 11-07-2024 (autodefinición, con […] en lugar de la URL) y nota 14-11-2024 (85 %) |

## Pasajes cambiados (para la fase 5 bis)

1. Siglas de entrada: se añade SEPI; se quita «las otras dos no constan en la web».
2. «Qué se puede preguntar»: EFE, siglas y marcas, autodefinición y cobertura, Grupo Joly, Cadena SER.
3. §1 «El mapa»: fila «Sector público estatal» (RTVE; Agencia EFE); «Empresas privadas»; COPE y Grupo Joly.
4. §1 epígrafe renombrado «El sector público estatal: RTVE y la Agencia EFE» + párrafo EFE.
5. §1 «Los grupos privados»: fila PRISA ampliada; filas nuevas COPE y Grupo Joly; párrafo posterior sin PRISA.
6. §2 «Qué es»: párrafo de autodefinición y 85 %.
7. §2 «Miembros»: introducción, tabla con negritas y siglas CACVSA/CSAG, dos párrafos nuevos (siglas y marcas),
   «El pie de la web de FORTA» (antes «la misma web», que perdió su antecedente).
8. §2 «Órganos»: nombramiento de Ojea (18-09-2025) y predecesor; Mellado en 2020.
9. «Lo que no da»: quitado el hueco de siglas; PRISA fuera; COPE reformulado.
10. «Trazabilidad»: tres filas nuevas y dos ampliadas. Portada: extensión 3.193.

Antecedentes releídos: «la misma nota» (14-01-2025), «La del 35 aniversario», «esa web» (SEPI), «La ficha
valenciana», «la misma web» (COPE): todos tienen su referente delante.

## Lentes

- `indice.py`: 15 epígrafes, 3.193 palabras; índice regenerado.
- `negritas.py` contra el texto de las páginas releídas hoy: todas las negritas nuevas están en su fuente
  (la de la nota de 11-07-2024 falla sólo por el […], comprobada a mano). Las 15 restantes que no casan son
  de fuentes no redescargadas (RTVE, UTECA, grupos, Carta del común), ya verificadas en fases 3-4.
- `refutar_prosa.py`: sin relleno ni repeticiones; siglas «sin presentar» = las de la tabla de miembros
  (presentadas en la tabla) y CMM/CRTVG dentro de la cita literal, declaradas como marcas no desarrolladas.
- Sin norma propia (la Carta es copiado del común): no se corren `refutar_exactitud.py` ni `refutar_modo.py`.

## Preguntas tras el remate

4, 6, 8, 10, 15 pasan a «entera»; 11 sigue en «no». Resultado previsto: 14 entera · 0 a medias · 1 no.

Ficheros tocados: el tema 06 y este informe. Descargas en la carpeta de trabajo de la sesión.
