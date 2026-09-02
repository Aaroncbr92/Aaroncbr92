# Información y Contenidos

Las fuentes del bloque específico de la ocupación. El Anexo 2 nombra **siete
documentos con su enlace** —puntos 4 a 10— y deja los tres primeros sin fuente,
porque son actualidad e instituciones. Aquí están **los siete**, y la novedad es
que están **los siete de verdad**: `convocatoria/FUENTES.md` daba dos por
imposibles.

## Los dos que se daban por imposibles, y por qué no lo eran

| Documento | Qué decía | Qué pasa de verdad |
|---|---|---|
| **Manual de estilo de RTVE** | «403, no se descarga» | **El 403 no era del servidor.** El programa da la dirección en `http://manualdeestilo.rtve.es/`, y la política de salida de este entorno **solo deja pasar https**. Con `https://` la misma dirección responde **200** y sirve el manual entero: ocho páginas, una por capítulo, unas **48.000 palabras** |
| **Informe mundial de la UNESCO 2021/2022** | «403, no se descarga» | **Sigue sin descargarse, y ahora se sabe por qué.** `unesdoc.unesco.org` está detrás de un desafío de JavaScript de Cloudflare —la página «Just a moment...»—, no de un bloqueo del proxy. Se probaron **cinco rutas** y ninguna abre. Lo que sí abre es **el sitio oficial del informe en `unesco.org`**, publicado por la propia UNESCO, con sus cuatro capítulos en español |

**La lección, que va a `ESTADO.md`:** un 403 no dice quién bloquea. Antes de
escribir «no se ha podido consultar» hay que mirar **el esquema de la dirección**
—`http` frente a `https`— y **quién firma la página de error**.

## Los siete documentos del Anexo 2

| Punto | Fichero | Qué es |
|---|---|---|
| 4 | `RTVE_codigo-autorregulacion-menores.pdf` y `.txt` | El código de 23 de julio de 2010, 20 páginas, del sitio de RTVE |
| 5 | `../corte-20221221/BOE-A-2018-8577.md` | El **RDL 4/2018** en su texto vigente al corte. **Ojo**: el Tribunal Constitucional declaró **inconstitucional y nulo** el apartado 3 del artículo único y la disposición final primera (STC 134/2021, `BOE-A-2021-13018`) |
| 6 | `RTVE_manual-de-estilo_*.txt`, ocho ficheros | El manual entero: inicio, CRTVE, TVE, RNE, Medios Interactivos, Cuestiones Sensibles, El Lenguaje y Anexos |
| 7 | `DOUE_directiva-2018-1808.pdf` y `.txt`, más `DOUE_directiva-2010-13-consolidada.txt` | La directiva modificativa **y** el texto de la Directiva 2010/13/UE **ya modificado por ella**. Hacen falta las dos: lo que el examen pregunta —límites de publicidad, prohibición del tabaco— está en los artículos de la 2010/13 tal como quedan tras la reforma |
| 8 | `PE_resolucion-25-11-2020.txt` | La resolución del Parlamento Europeo, DO C 425 de 20.10.2021 |
| 9 | `UNESCO_informe-2021-2022_*.txt`, cinco ficheros | El sitio oficial del informe en español. **No es el informe íntegro**, y cada fichero lo dice en su cabecera |
| 10 | `FIP_carta-etica.txt` y `.pdf` | La carta de la Federación Internacional de Periodistas, Túnez, 12 de junio de 2019: preámbulo y dieciséis artículos, que es el documento entero |

Se suma `UNESCO_dia-mundial-libertad-de-prensa.txt`, la página oficial del Día
Mundial de la Libertad de Prensa, que sostiene el **3 de mayo** y quién lo
proclamó.

## Las rutas que se han estrenado aquí

- **Cuando EUR-Lex devuelve 202 con cero bytes, el repositorio Cellar sirve el
  documento.** El enlace del programa a la Resolución del Parlamento Europeo
  —`eur-lex.europa.eu`, en PDF y en HTML— responde **202 Accepted y ningún byte**
  a toda consulta automática, tres intentos seguidos. La Oficina de Publicaciones
  de la Unión Europea sirve el mismo documento en
  `https://publications.europa.eu/resource/celex/<CELEX>` **si se le pide el
  idioma en la cabecera** (`Accept: application/xhtml+xml`,
  `Accept-Language: spa`); sin ella devuelve un 400 que, eso sí, **dice qué
  falta**. Por ahí salieron también la Directiva 2018/1808 y la 2010/13
  consolidada.
- **Una norma modificativa no se lee sola.** La Directiva 2018/1808 dice «el
  artículo 23 se sustituye por el texto siguiente». Estudiarla sin el texto
  consolidado obliga a reconstruir la norma de cabeza, que es lo que el
  apartado 1 del manual prohíbe. Por eso están las dos.

## Lo que este bloque no tiene

**El informe de la UNESCO en su texto íntegro.** De las cinco preguntas del
examen que salen de él, el sitio oficial contesta cuatro; **la del reparto por
regiones de los asesinatos de periodistas entre 2016 y 2020 no está en él**, y
va marcada en su tema como apoyada sólo en la plantilla oficial.
