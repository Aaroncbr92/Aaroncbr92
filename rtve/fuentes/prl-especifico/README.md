# Fuentes del tema de PRL del específico que no son legislación

Dos de las cinco rúbricas de este tema **no tienen norma detrás**. Lo que hay es documentación
técnica oficial, y por eso se guarda aquí **el documento entero**, no una cita: para que
cualquier afirmación del tema se pueda comprobar y para que la lente `refutar_documento.py`
tenga contra qué contrastar.

La legislación va donde va siempre: volcada con `herramientas/boe.py` a
`fuentes/corte-20221221/`.

| Fichero | Qué es | Edición | Para qué |
| --- | --- | --- | --- |
| `guia-tecnica-pvd.pdf` / `.txt` | **Guía Técnica del INSST para la evaluación y prevención de los riesgos relativos a la utilización de equipos con pantallas de visualización** | **junio de 2021** (primera versión, junio de 1998) | Rúbrica 2: fatiga visual, carga mental, distancias, pausas |
| `insst-tme-extremidad-superior.pdf` / `.txt` | **INSST, *Trastornos musculoesqueléticos de la extremidad superior*** (material de los temas específicos del proceso selectivo de la Escala de Titulados Superiores del propio Instituto) | **abril de 2025** | Rúbrica 3 entera |
| `portal-tme.html` / `.txt` | Página del INSST sobre **trastornos musculoesqueléticos** | descargada el **30/08/2026** | Contexto y epidemiología |
| `ntp-536.pdf` / `.txt` | **NTP 536: Extintores de incendio portátiles: utilización** | **1999** | Rúbrica 4: agentes extintores y su adecuación a las clases de fuego |
| `ntp-1090.pdf` / `.txt` | **NTP 1090: Riesgos laborales viarios: marco conceptual (I)** | **2017** | Rúbrica 5: definiciones de in itinere, en misión y conductor profesional |
| `ntp-1091.pdf` / `.txt` | **NTP 1091: Riesgos laborales viarios: marco conceptual (II)** | **2017** | Rúbrica 5: Plan de Seguridad Vial y Plan de Movilidad |
| `cnsst-seguridad-vial.pdf` / `.txt` | Informe del **grupo de trabajo de Seguridad Vial Laboral de la Comisión Nacional de Seguridad y Salud en el Trabajo** | datos de **2014** | Rúbrica 5: dónde se centra la responsabilidad empresarial |
| `boe-anuario-in-itinere-en-mision.md` | Ficha con **la doctrina del Tribunal Supremo** sobre in itinere y en misión, tal como la enuncia el **Anuario de Derecho que publica el BOE** | leída el **30/08/2026** | Rúbrica 5: los cuatro elementos y los límites de la presunción |

## Tres avisos

**1. Las NTP no son obligatorias.** Ellas mismas lo dicen: «*Las NTP son guías de buenas
prácticas. Sus indicaciones no son obligatorias salvo que estén recogidas en una disposición
normativa vigente.*» Se usan como **fuente citable y estable**, que es lo que el `PLAN.md`
prevé para los temas sin norma detrás, no como derecho.

**2. Dos de estos documentos son posteriores a la fecha de corte** —el de TME es de abril de
2025 y la página del portal se descargó en 2026—. **No hay nada que congelar**: no son
legislación, y la definición que de ellos se toma —la de la **EU-OSHA de 2007**— es anterior al
corte y no ha cambiado. El tema lo dice en su trazabilidad.

**3. La ficha del Anuario de Derecho no sustituye a las sentencias.** Recoge **lo que se ha
podido leer**; **las sentencias del Tribunal Supremo no se han leído en su texto original**, y
por eso se citan como referencia y no como cita. Lo que no se pudo confirmar —la extensión del
in itinere a una segunda residencia— **está dicho como tal en el tema**.

## Cómo se vuelven a bajar

```
curl -sSL -o guia-tecnica-pvd.pdf "https://www.insst.es/documents/94886/203536/Gu%C3%ADa+t%C3%A9cnica+para+la+evaluaci%C3%B3n+y+prevenci%C3%B3n+de+los+riesgos+relativos+a+la+utilizaci%C3%B3n+de+equipos+con+pantallas+de+visualizaci%C3%B3n.pdf"
curl -sSL -o insst-tme-extremidad-superior.pdf "https://www.insst.es/documents/d/portal-insst/tema-69-tme-de-la-extremidad-superior"
curl -sSL -o ntp-536.pdf  "https://www.insst.es/documents/d/portal-insst/ntp_536-pdf"
curl -sSL -o ntp-1090.pdf "https://www.insst.es/documents/d/portal-insst/ntp-1090-pdf"
curl -sSL -o ntp-1091.pdf "https://www.insst.es/documents/d/portal-insst/ntp-1091-pdf"
curl -sSL -o cnsst-seguridad-vial.pdf "https://www.insst.es/documents/94886/150112/Documento+Seguridad+vial/63e8f7d1-a078-42c6-a1bb-af05954dc307"
```

**Ojo con el patrón de URL del INSST**: las rutas `documents/<id>/<id>/<nombre>.pdf` devuelven
**HTML con código 200** cuando no aciertan —no un 404—, así que un `curl` que «funciona» puede
haber traído una página de error. La ruta que sirve de verdad para las NTP y los temas es
**`documents/d/portal-insst/<slug>`**. Después de bajar, `file` sobre el resultado: si no dice
**PDF document**, no lo es.

Las transcripciones `.txt` se rehacen con:

```
python3 -c "from pdfminer.high_level import extract_text; open('X.txt','w').write(extract_text('X.pdf'))"
```

## Tercera tanda: los riesgos psicosociales, para el tema 16 de Producción

El punto 16 del Anexo 2 de **Producción** mete la prevención de riesgos laborales
en el mismo enunciado que la protección de datos y la contratación pública, y el
examen pregunta por el **nombre** del acoso psicológico en el trabajo. Ese nombre
lo fija el propio Instituto Nacional de Seguridad y Salud en el Trabajo.

| Fichero | Qué es | Dirección | Descargado |
|---|---|---|---|
| `ntp-476.pdf` y `.txt` | **NTP 476**, «El hostigamiento psicológico en el trabajo: *mobbing*», de 1998 | `insst.es/documents/d/portal-insst/ntp_476-pdf` | 03/09/2026 |
| `ntp-704.pdf` y `.txt` | **NTP 704**, «Síndrome de estar quemado por el trabajo o *burnout* (I): definición y proceso de generación» | `insst.es/documents/d/portal-insst/ntp_704-pdf` | 03/09/2026 |

**Las dos hacen falta juntas**, y ésa es la razón de traer la segunda: la pregunta
45 del examen de Producción opone *mobbing* a *burn out*, y **sin las dos fichas
sólo se puede afirmar la mitad**. La NTP 476 define el primero; la NTP 704 define
el segundo, y al definirlo demuestra que **no es lo que la pregunta pregunta**.

**Y una advertencia que la propia NTP 476 imprime en su cabecera**: «Actualizada
por la NTP 854». La 476 se cita aquí **por su definición**, que es la que el
vocabulario del examen usa; quien quiera el estado actual de la técnica debe ir a
la 854. Se ha intentado descargarla por la misma ruta y **devuelve «no
encontrado»**.
