# Protocolos de Vigilancia Sanitaria Específica

**Qué son.** Los protocolos que la **Comisión de Salud Pública del Consejo Interterritorial del
Sistema Nacional de Salud** aprueba al amparo de la letra c) del apartado 3 del artículo 37 del Real
Decreto 39/1997, que manda que la vigilancia de la salud «estará sometida a protocolos específicos u
otros medios existentes con respecto a los factores de riesgo a los que esté expuesto el trabajador» y
encarga al Ministerio de Sanidad y a las comunidades autónomas establecer «la periodicidad y contenidos
específicos de cada caso».

**Por qué está aquí este almacén.** El **Anexo 2 de la convocatoria 1/2022 para la ocupación tipo de
Medicina de Empresa** nombra el protocolo de vigilancia sanitaria específica **once veces**, con esas
palabras, en once de sus treinta y tres puntos. **No es una fuente auxiliar: es la fuente que el propio
programa manda estudiar**, y sin ella la mitad clínica de ese temario no tendría documento detrás.

**Los otros volúmenes del proyecto los declararon como laguna.** Enfermería de Empresa dice tema tras
tema «no consultados» al llegar a ellos. **Con este almacén esa laguna se cierra**, y los temas de
Enfermería que la declararon siguen diciendo la verdad de lo que hicieron: se escribieron sin ellos.

## Lo que hay

| Fichero | Protocolo | Edición que lleva impresa |
|---|---|---|
| `adenocarcinoma` · `adenocarcinoma-guia` | Adenocarcinoma de fosas nasales y senos paranasales | 2019 |
| `agentes-biologicos` | Agentes biológicos | 2001 |
| `agentes-quimicos` | Personas con riesgo de exposición laboral a productos químicos | 2023 |
| `alveolitis` | Alveolitis alérgica extrínseca | 2000 |
| `amianto` | Amianto | 2013 |
| `anestesicos` | Agentes anestésicos inhalatorios | 2001 |
| `asma-laboral` | Asma laboral | 2000 |
| `cargas` | Manipulación manual de cargas | 1999 |
| `citostaticos` | Agentes citostáticos | 2003 |
| `cloruro-de-vinilo` | Cloruro de vinilo monómero | 1999 |
| `dermatosis` | Dermatosis laborales | 2003 |
| `movimientos-repetidos` | Movimientos repetidos de miembro superior | 2000 |
| `neuropatias` | Neuropatías por presión | 2000 |
| `oxido-de-etileno` | Óxido de etileno | 2003 |
| `pantallas` | Pantallas de visualización de datos | 1999 |
| `plaguicidas` | Plaguicidas | 1999 |
| `plomo` | Plomo | 1999 |
| `posturas-forzadas` | Posturas forzadas | 2000 |
| `radiaciones-ionizantes` | Radiaciones ionizantes | **Sin año impreso en su portada** |
| `radon` | Personas trabajadoras expuestas a radón | 2026 |
| `ruido` · `ruido-guia` | Ruido | 2022 el protocolo, 2019 la guía |
| `silicosis` | Silicosis | 2020 |
| `vibraciones` · `vibraciones-guia` | Vibraciones mecánicas | 2026 |

**Veintiséis documentos, 1.782 páginas.**

**Tres avisos que hay que dar con esta fuente.**

**Primero: la mayoría son antiguos y lo dicen ellos mismos en la portada.** Once de los veintiséis son
de 1999 a 2003. **Un protocolo de 1999 sobre pantallas de visualización describe un puesto que ya no
existe** —el tubo de rayos catódicos—, y **sus criterios de aptitud y su periodicidad siguen siendo los
que la Comisión de Salud Pública tiene aprobados.** El temario cita lo que dicen y **dice de qué año es
cada uno**, que es lo que permite al opositor saber qué está leyendo.

**Segundo: tres son posteriores a la fecha de corte del proyecto** —el de productos químicos, de 2023;
el de radón y el de vibraciones, de 2026—. **No son legislación y no hay redacción que congelar**, y es
el mismo criterio con que este proyecto usó material del Instituto posterior al corte. Los temas que
los usan lo declaran.

**Tercero: el protocolo de radiaciones ionizantes no lleva año impreso en su portada.** Es un dato de
la fuente, no un descuido de este volcado, y va declarado en el tema que lo usa.

## Cómo se vuelven a bajar

Los veintiséis salen de la misma página del Ministerio de Sanidad, en el área de salud laboral, dentro
de las guías y protocolos de vigilancia de la salud de las personas trabajadoras:

```sh
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
B=https://www.sanidad.gob.es/areas/saludLaboral/guiasVigiTrabajadores/protocolosVigilancia
curl -sSL -A "$UA" -e "$B/home.htm" -o ruido.pdf "$B/docs/ruidoProtocolo.pdf"
python3 -c "import pymupdf; d=pymupdf.open('ruido.pdf'); open('ruido.txt','w',encoding='utf-8').write('\n'.join(p.get_text() for p in d))"
```

**La página lista los nombres de fichero, que no siguen ningún patrón**: el de amianto es
`ProtoVigiAmianto1.pdf`, el de vibraciones `VibracionesPROTOCOLaCCESIBLE.pdf` y el de agentes químicos
`guiaQUIMICOS.pdf`. **Conviene sacarlos de la propia página y no adivinarlos**, y comprobar con `file`
que lo bajado es un PDF.
