# Igualdad en RTVE · las dos fuentes del tema 6

**Ninguna de las dos está en el BOE.** El programa las cita **por su URL en `rtve.es`**, así
que no hay identificador, ni texto consolidado, ni redacciones fechadas. Lo que hay es el
fichero que RTVE publica en su web.

| Fichero | Origen | Extensión |
|---|---|---|
| `II-Plan-Igualdad-2022-2026.pdf` | `https://www.rtve.es/contenidos/corporacion/II_Plan_de_Igualdad_entre_Mujeres_y_Hombres_en_la_Corporacion_RTVE_(2022_2026).pdf` | **118 páginas** |
| `Guia-Igualdad-2020.pdf` | `https://www.rtve.es/contenidos/corporacion/GUIA_DE_IGUALDAD_2020.pdf` | **26 páginas** |

Los `.txt` son la transcripción con `pdfminer.six`. **Se versionan también los PDF**, no solo
la transcripción: si RTVE sustituyera un fichero, **no quedaría rastro de la versión con la
que se ha estudiado**, y estos documentos no tienen histórico público como lo tiene el BOE.

## Fechas que fijan la versión

- **Guía de Igualdad: 2020.** La aprueba el **Observatorio de Igualdad** y la publica el
  **Instituto RTVE**.
- **II Plan de Igualdad: suscrito el 7 de marzo de 2022**, por una comisión negociadora
  **constituida el 22 de abril de 2021**.

Ambos son **anteriores a la fecha de corte de las bases (21/12/2022)**, de modo que son los
examinables.

## Cómo se verifican

Las lentes `refutar_exactitud.py` y `refutar_modo.py` **no sirven**: trocean el tema por
artículos y estos documentos no los tienen. Pasadas tal cual devuelven **«0 comprobadas,
0 hallazgos»**, que no es un aprobado sino una comprobación que no ha mirado nada.

Se usa **`herramientas/refutar_documento.py`**:

```
python3 herramientas/refutar_documento.py temas/general/06-igualdad.md fuentes/igualdad/*.txt
```

Contrasta **cada negrita del tema** y, sobre todo, **cada cifra en negrita** contra el texto
completo de las dos fuentes.

## Dos avisos sobre el contenido

1. **La Guía cita la Ley 7/2010** General de la Comunicación Audiovisual (artículos 4.2 y
   18.1), que a la fecha de corte **ya estaba derogada** por la **Ley 13/2022**, que es el
   tema 7. La Guía no se ha actualizado; para el examen vale lo que dice la Guía, pero esa
   remisión está caducada.
2. **El Plan describe el Consejo de Administración con diez miembros**, la redacción que dejó
   la Ley 5/2017. El Real Decreto-ley 5/2024 lo llevó a quince, pero eso es posterior al
   corte y, además, **el Plan dice lo que dice**.
