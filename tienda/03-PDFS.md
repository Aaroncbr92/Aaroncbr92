# 3 · Gestión de los PDF

Dos problemas distintos que se confunden a menudo:

- **La muestra** se enseña a cualquiera que pase por la web. Va a llegar a
  manos de gente que no ha pagado, y está bien que llegue: para eso es.
- **El volumen completo** sólo puede salir del servidor cuando hay un pedido
  pagado detrás.

Lo primero es un problema de *diseño de producto*. Lo segundo, de *control de
acceso*. Mezclarlos lleva al error clásico: intentar «proteger» la muestra con
trucos de navegador y dejar el completo colgando de una URL adivinable.

---

## 3.1 La regla que sostiene todo

> **Ningún PDF completo se guarda en una ruta accesible por HTTP.**

Los ficheros viven en `~/temarios_privados/`, hermana de `public_html`, no
dentro. No hay URL que llegue hasta ahí porque no hay camino: el servidor sólo
sirve lo que cuelga de la raíz del dominio.

Todo lo demás de este documento —tokens, límites, sellado— es *añadido*. Si
mañana fallara la firma de enlaces, el fichero seguiría sin ser alcanzable
desde fuera. Esa es la propiedad que hace que la elección de WordPress no
comprometa la seguridad de los archivos: **el CMS no custodia los ficheros**.

La comprobación de la fase 3 de `02-IMPLANTACION.md` es la que verifica esto, y
es la única del plan que, si falla, obliga a parar.

---

## 3.2 Generar las muestras

Con la herramienta del repositorio, que ya está escrita y probada sobre los
veinticinco volúmenes:

```bash
python3 herramientas/muestra.py            # los veinticinco
python3 herramientas/muestra.py --paginas 20   # más cuerpo, si quieres
```

Cada muestra sale con:

- **la portada limpia**, que es la cara del producto;
- **el índice completo**, a propósito: quien duda quiere comprobar que están
  sus temas, no leer gratis el primero;
- **doce páginas de cuerpo**, con marca de agua diagonal y un pie que dice de
  qué volumen salen y cuántas páginas tiene el completo;
- **una página de cierre** con el recuento y la dirección de la tienda, para
  que la muestra reenviada por ahí sin contexto siga diciendo de dónde sale.

Dónde acaba el índice **no se adivina**: se lee de los marcadores que `pdf.py`
deja escritos en el PDF, así que funciona igual en el de ocho temas y en el de
treinta y tres. Salen entre 17 y 24 páginas por volumen, 271–447 KB cada una.

> **La trampa que costó encontrarla.** Sellar una página con `merge_page` deja
> su flujo de contenido **sin comprimir**: la muestra de Sonido pesaba 1.665 KB
> en vez de 358, cinco veces más, sólo por eso. Hay que volver a comprimir cada
> página después de sellarla, y sólo se puede hacer cuando la página ya cuelga
> del escritor. Está resuelto en `muestra.py`, con el aviso escrito en su
> encabezado para que nadie lo «simplifique» más adelante.

---

## 3.3 Enseñar la muestra sin ofrecer la descarga

**PDF.js autoalojado**, en `wp-content/uploads/pdfjs/`. Nada de servicios de
terceros tipo visores incrustados: mandarles el PDF es publicarlo en su
infraestructura, y entonces el control lo tienen ellos.

El montaje, que ya trae hecho `toac-tienda.php`:

1. `/muestra/<slug>` pinta una página con el visor dentro de un `iframe`.
2. El visor recibe el PDF desde `/muestra-pdf/<slug>?t=…`, con un token firmado
   que **caduca a los quince minutos**.
3. Ese endpoint sirve el fichero con `Content-Disposition: inline` y
   `X-Robots-Tag: noindex`: se ve, no se ofrece guardar, y Google no lo indexa.
4. La barra del visor va recortada por CSS —descargar, imprimir, abrir en otra
   pestaña y propiedades del documento—. Se añade
   `codigo/servidor/pdfjs-recorte.css` al final de `pdfjs/web/viewer.css`.

**Y ahora la parte honesta.** Ese CSS no protege nada. El PDF ya está en el
navegador de quien lo mira; cualquiera con la consola abierta lo saca. Sirve
para que la interfaz sea coherente con lo que ofreces, no para impedir nada.

**Lo que sí protege es que ese fichero tiene diecinueve páginas.** Las otras
ciento ochenta y ocho no han salido del servidor y no hay manera de pedirlas.
Ese es el diseño: no se intenta que el usuario no pueda guardar lo que se le
enseña, se decide con cuidado qué se le enseña.

Un corolario incómodo pero importante: **no gastes esfuerzo en bloquear el
clic derecho ni en detectar capturas**. Molestan al comprador honesto, no
frenan a nadie, y dan una falsa sensación de seguridad que lleva a descuidar lo
que sí importa.

---

## 3.4 Servir el volumen completo

El circuito completo está en `01-ARQUITECTURA.md` §1.4. Aquí, lo que hay que
saber para mantenerlo.

### Los cinco filtros, en orden

| # | Filtro | Qué pasa si no |
|---|---|---|
| 1 | Sesión iniciada | Redirección a «Mi cuenta». |
| 2 | Token con HMAC válido y sin caducar (10 min) | Vuelve a su panel con un enlace nuevo. |
| 3 | El token se emitió **para esa cuenta** | 403. |
| 4 | Existe un pedido **pagado** con ese producto | 403. |
| 5 | No ha superado 8 descargas al día | 429. |

El filtro 4 es el que manda: los otros cuatro se pueden considerar defensa en
profundidad. Y se comprueba **en cada petición**, no al emitir el enlace: si
mañana reembolsas un pedido, la descarga deja de funcionar sin que borres nada.

### Por qué el token no lleva la ruta

Lleva el identificador del producto. Aunque alguien lo descodificase —va en
base64, no está cifrado— no aprendería dónde está el fichero. Lo que impide
falsificarlo es la firma HMAC-SHA256 con `TOAC_CLAVE_FIRMA`, que sólo está en
`wp-config.php`.

Y de ahí sale el botón de emergencia: **si algún día hay una filtración, cambia
esa constante**. Todos los enlaces emitidos dejan de valer en el acto, sin tocar
ni un pedido.

### Por qué `X-LiteSpeed-Send-File`

Servir 3,6 MB con `readfile()` significa que PHP mantiene un proceso ocupado
durante toda la descarga. En un alojamiento compartido, con el límite en
procesos de entrada, veinte descargas simultáneas tumban la web entera —incluida
la portada, incluido el pago—.

Con la cabecera de envío, PHP decide y **el servidor sirve**: el proceso de PHP
queda libre en milisegundos. Hostinger corre LiteSpeed, así que la cabecera es
`X-LiteSpeed-Send-File`; el plugin lo detecta solo con `TOAC_ENVIO = 'auto'`, y
si no lo consigue cae a `readfile()` por trozos, que funciona igual pero
consume más.

> **Comprobación.** Descarga un volumen y mira la respuesta en las herramientas
> de red: debe traer `Content-Length` correcto y **no** debe aparecer la
> cabecera `X-LiteSpeed-Send-File` en la respuesta (LiteSpeed la consume; si te
> llega al navegador, es que el servidor no la entendió y estás sirviendo por
> PHP).

---

## 3.5 El sellado nominativo

Es, de lejos, lo que más frena que un temario acabe en un grupo de descargas.
No por criptografía: **porque nadie sube a un grupo un PDF con su propio nombre
y su correo en el pie de las 259 páginas**.

Se sella una vez por comprador y se guarda en `~/temarios_privados/sellados/`;
las descargas siguientes reutilizan el sellado, y se rehace solo cuando
actualizas el volumen. Sin esa caché, sellar 578 páginas en cada clic sería
inviable en un compartido.

**Instalación** (por SSH, con Composer):

```bash
cd ~/public_html/wp-content
mkdir -p toac-lib && cd toac-lib
composer require setasign/fpdi setasign/fpdf
```

y en `wp-config.php`, antes de las constantes de TOAC:

```php
require_once '/home/uXXXXXXX/public_html/wp-content/toac-lib/vendor/autoload.php';
define( 'TOAC_SELLAR', true );
```

**La limitación, dicha antes de que te la encuentres.** FPDI en su versión
libre lee PDF hasta la especificación **1.4**. Los volúmenes los genera Chromium
vía `pdf.py`, que escribe **PDF 1.7**, así que FPDI a secas los va a rechazar.
Dos salidas:

1. **Rebajar la versión al generar.** Añade una pasada de `qpdf` en `pdf.py`:
   `qpdf --force-version=1.4 entrada.pdf salida.pdf`. Es lo más limpio, se hace
   una vez por volumen y no cuesta nada en cada descarga.
2. **Comprar el `FPDI PDF-Parser`** de Setasign (licencia de pago), que lee
   1.5 en adelante.

Si nada de esto está listo, `TOAC_SELLAR` a `false`: el plugin sirve el
original. La regla que se respeta en el código es que **una descarga pagada
nunca falla porque falle el sellado** — si la biblioteca no está o el sellado
lanza una excepción, se entrega el fichero sin sellar y se anota en el registro.

---

## 3.6 Actualizaciones de los temarios

Sale gratis por cómo está montado: el endpoint resuelve **el fichero actual**
del producto, no una copia congelada en el momento de la compra.

Cuando regeneres un volumen:

```bash
python3 herramientas/libro.py sonido && python3 herramientas/pdf.py libro-sonido.html
python3 herramientas/muestra.py libro-sonido.pdf
python3 herramientas/catalogo.py          # recalcula páginas, temas y fecha

scp -P 65002 libro-sonido.pdf            uXXXXXXX@…:~/temarios_privados/libros/
scp -P 65002 muestras/muestra-sonido.pdf uXXXXXXX@…:~/temarios_privados/muestras/
```

y actualiza `_toac_actualizado` en el producto (o reimporta el CSV). Los que ya
compraron descargan la versión nueva sin que toques nada más; los sellados
viejos se rehacen solos porque son más antiguos que el fichero.

**Y díselo.** Un correo a los compradores de ese volumen cuando cambia una
norma es el mejor argumento de venta que tiene un temario de oposiciones, y es
lo que justifica el precio frente a un PDF pirata de hace tres convocatorias.

---

## 3.7 Vigilancia

La tabla `wp_toac_descargas` está para mirarla, no para llenarse. Una consulta
al mes:

```sql
-- Cuentas con descargas desde muchas direcciones distintas: candidatas a
-- estar compartidas entre varias personas.
SELECT u.user_email,
       COUNT(DISTINCT d.ip) AS direcciones,
       COUNT(*)             AS descargas
FROM wp_toac_descargas d
JOIN wp_users u ON u.ID = d.user_id
WHERE d.fecha > DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY d.user_id
HAVING direcciones > 6
ORDER BY direcciones DESC;
```

Seis direcciones en un mes es normal —casa, móvil, trabajo, un tren—. Veinte no
lo es. Antes de acusar a nadie, mira las horas: una cuenta compartida se nota
porque descarga a la vez desde sitios distintos.
