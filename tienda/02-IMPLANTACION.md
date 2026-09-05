# 2 · Plan de implantación

Doce fases. Cada una termina en algo comprobable: si la comprobación no sale, no
se pasa a la siguiente. Sustituye `temarios.example` por tu dominio y
`uXXXXXXX` por tu usuario de Hostinger (lo ves en hPanel → SSH, o con `whoami`).

Tiempo realista de principio a fin: **tres a cinco días** de trabajo efectivo,
más lo que tarde el dominio en propagar.

> **Las fases 3, 5, 6, 8, 9 y 11 están automatizadas.** Con las fases 1 y 2
> hechas —dominio con certificado y WordPress instalado—, un solo comando monta
> el resto: ver [`despliegue/README.md`](despliegue/README.md). Este documento
> sigue siendo el que explica **qué** se está montando y por qué, y es el que
> hay que leer cuando algo no salga.

---

## Fase 1 · Dominio y certificado

1. hPanel → **Dominios** → registra o apunta el dominio al alojamiento.
2. hPanel → **Seguridad → SSL** → instala el certificado gratuito y activa
   **Forzar HTTPS**.
3. Deja el `www` redirigiendo al desnudo (o al revés), pero **uno solo**: dos
   orígenes con sesión abierta son dos problemas de cookies.

> **Comprobación.** `curl -I https://temarios.example` devuelve `200` y
> `curl -I http://temarios.example` devuelve `301` hacia `https`.

---

## Fase 2 · WordPress y PHP

1. hPanel → **Sitios web → Añadir web → WordPress**. Usuario administrador con
   nombre **que no sea `admin`** y contraseña larga generada, no inventada.
2. hPanel → **Avanzado → Configuración PHP**: versión **8.2 o 8.3**, y en
   *Opciones PHP*:

   | Directiva | Valor | Por qué |
   |---|---|---|
   | `memory_limit` | `256M` | Márgenes para el sellado de PDF. |
   | `upload_max_filesize` | `64M` | El volumen más gordo pesa 3,6 MB, pero el margen no cuesta nada. |
   | `post_max_size` | `64M` | Igual. |
   | `max_execution_time` | `120` | Una descarga larga no debe cortarse. |
   | `opcache.enable` | `On` | Rendimiento, gratis. |
   | `display_errors` | `Off` | Un aviso de PHP filtrando rutas del servidor es una fuga. |

3. Borra los plugins y temas que trae de fábrica y no vas a usar. **Un tema
   inactivo sin actualizar es una puerta abierta**, no un tema inactivo.

> **Comprobación.** WP → Herramientas → **Salud del sitio** en verde salvo, como
> mucho, avisos de rendimiento.

---

## Fase 3 · Las carpetas privadas

Por SSH (hPanel → Avanzado → Acceso SSH):

```bash
cd ~
mkdir -p temarios_privados/libros temarios_privados/muestras
chmod 750 temarios_privados temarios_privados/libros temarios_privados/muestras
```

Sube ahí los ficheros —desde tu máquina, con el repositorio delante:

```bash
# Los veinticinco volúmenes completos
scp -P 65002 libro-*.pdf uXXXXXXX@temarios.example:~/temarios_privados/libros/

# Las muestras, generadas antes con la herramienta del repositorio
python3 herramientas/muestra.py            # crea muestras/muestra-*.pdf
scp -P 65002 muestras/muestra-*.pdf uXXXXXXX@temarios.example:~/temarios_privados/muestras/
```

(El puerto SSH de Hostinger no es el 22; el tuyo aparece en el hPanel.)

Y por si algún día alguien mueve esa carpeta dentro del dominio, red de
seguridad —copia `codigo/servidor/temarios-privados.htaccess`:

```bash
scp -P 65002 tienda/codigo/servidor/temarios-privados.htaccess \
    uXXXXXXX@temarios.example:~/temarios_privados/.htaccess
```

> **Comprobación, y es la importante de toda la fase.**
> `curl -I https://temarios.example/temarios_privados/libros/libro-sonido.pdf`
> y cualquier otra ruta que se te ocurra deben devolver **404 o 403**. Si alguna
> devuelve `200`, para y no sigas.

---

## Fase 4 · Acceso con Google

Primero, en Google:

1. [Google Cloud Console](https://console.cloud.google.com) → **Nuevo proyecto**
   (`TOAC Temarios`).
2. **APIs y servicios → Pantalla de consentimiento de OAuth**: tipo *Externo*,
   nombre de la aplicación, correo de asistencia, logotipo, enlaces a tu aviso
   legal y a tu política de privacidad —Google los exige para publicar—, y
   ámbitos `email`, `profile`, `openid` y nada más.
3. **Credenciales → Crear → ID de cliente de OAuth → Aplicación web**:
   - Orígenes autorizados: `https://temarios.example`
   - URI de redirección: `https://temarios.example/?toac_google=callback`
4. Guarda el **ID de cliente** y el **secreto**.
5. **Publica** la aplicación. Mientras esté en *Prueba*, sólo entran las cuentas
   que hayas listado a mano.

Después, en tu sitio. Dos caminos:

**a) Con el código propio de esta entrega** (sin plugins de terceros):

```bash
scp -P 65002 tienda/codigo/mu-plugins/toac-google-sso.php \
    uXXXXXXX@temarios.example:~/public_html/wp-content/mu-plugins/
```

y añade a `wp-config.php` las constantes de `codigo/servidor/wp-config-extra.php`.
Es el fichero que responde al requisito 1; está comentado línea a línea.

**b) Con plugin**: *Nextend Social Login* → Google → pega ID y secreto. Cinco
minutos, y el mantenimiento es de otro. Elección legítima; el código propio te
libra de una dependencia más.

> **Comprobación.** En ventana de incógnito, `/mi-cuenta` muestra el botón,
> el ciclo completo te deja dentro, y en WP → Usuarios aparece el usuario nuevo
> con su correo. Repite el ciclo: la segunda vez debe **entrar en la misma
> cuenta**, no crear otra.

---

## Fase 5 · WooCommerce

1. Instala **WooCommerce** y pasa el asistente: España, EUR, y en *Tipo de
   negocio* marca **productos digitales**.
2. **WooCommerce → Ajustes → Productos → Descargas**: aunque las descargas las
   sirve el plugin propio, deja el método en **Forzar descargas** y marca
   **Se requiere inicio de sesión**. Es el cinturón por si algún día un producto
   se marca descargable por descuido.
3. **Ajustes → Cuentas y privacidad**:
   - Compra como invitado: **desactivada**. Sin cuenta no hay panel privado, y
     sin panel privado no hay requisito 5.
   - Permitir crear cuenta al finalizar la compra: **activada**.
   - Borrado automático de datos personales: según lo que digas en tu política.
4. **Ajustes → General**: desactiva envíos y cálculo de impuestos por dirección
   de envío. Aquí no se envía nada.
5. Páginas: deja que cree Carrito, Finalizar compra y Mi cuenta. Añade a mano
   **Tienda**, **Aviso legal**, **Privacidad**, **Cookies**, **Condiciones de
   venta** y **Contacto** (fase 11).

> **Comprobación.** Un producto de prueba a 0,50 € se compra de principio a fin
> con la pasarela en modo de pruebas y aparece en Pedidos como *Completado*.

---

## Fase 6 · El plugin propio y el catálogo

```bash
ssh -p 65002 uXXXXXXX@temarios.example 'mkdir -p ~/public_html/wp-content/mu-plugins'
scp -P 65002 tienda/codigo/mu-plugins/*.php \
    uXXXXXXX@temarios.example:~/public_html/wp-content/mu-plugins/
```

Van en `mu-plugins/` a propósito: **no se pueden desactivar desde el escritorio**
y no aparecen en la lista de plugins. Un administrador con prisa no puede apagar
por error el control de acceso a los ficheros.

Luego el catálogo:

1. WP → **Herramientas → Importar → WooCommerce productos (CSV)**.
2. Sube `tienda/catalogo/productos.csv`. El importador mapea solo las columnas
   `meta:_toac_*`.
3. Revisa **precios** (los del CSV son una propuesta, ver `05-LANZAMIENTO.md`),
   descripciones y las imágenes de portada.

Los veinticinco productos son **virtuales y no descargables**: la descarga la da
el endpoint propio, no WooCommerce.

> **Comprobación.** `/tienda` lista los 25 volúmenes, cada tarjeta enseña su
> fecha de actualización, y en la ficha de *Sonido* aparecen 207 páginas, 18
> temas y 134 preguntas.

---

## Fase 7 · Pasarela de pago

Detallada en [`04-PAGOS.md`](04-PAGOS.md). En corto:

1. Instala **WooCommerce Stripe Gateway**, conecta la cuenta, empieza en
   **modo de pruebas**.
2. Registra el webhook `https://temarios.example/?wc-api=wc_stripe` y pega el
   secreto de firma.
3. Prueba con la tarjeta `4242 4242 4242 4242`, y también con
   `4000 0000 0000 9995` (fondos insuficientes): el pedido debe quedar
   **Fallido** y **no** dar acceso a la descarga.
4. Si quieres PayPal, añade *WooCommerce PayPal Payments* y repite.
5. Pasa a **modo real** sólo tras la fase 10.

> **Comprobación.** Un pago rechazado no abre ninguna descarga. Es la prueba que
> más se olvida y la única que importa de verdad.

---

## Fase 8 · Muestras y visor

1. Genera las muestras y súbelas (fase 3) si no lo hiciste ya.
2. Descarga la última versión estable de **PDF.js** y súbela a
   `wp-content/uploads/pdfjs/`. Autoalojada: el visor no debe estar en el
   dominio de nadie más.
3. El plugin ya sirve `/muestra/<slug>` con el visor recortado —sin botón de
   descarga, sin impresión, sin «abrir en otra pestaña»— y el PDF por detrás con
   token de un solo uso.

> **Comprobación.** Abre `/muestra/sonido` sin sesión iniciada: debe verse la
> portada, el índice y doce páginas con su marca de agua, y **ninguna más**.
> Copia la URL del PDF que se ve en las herramientas de desarrollo, pégala en
> otra pestaña pasados cinco minutos: debe dar 403.

---

## Fase 9 · Caché y rendimiento

1. Instala **LiteSpeed Cache**. Ajustes recomendados: caché activada, TTL
   público de 604800, minificación de CSS/JS, imágenes en WebP.
2. **Y esto no es opcional** — LiteSpeed Cache → Caché → Excluir:

   ```
   /carrito
   /finalizar-compra
   /mi-cuenta
   /descarga
   /muestra
   ```

   Y en *No cachear cookies*: `wordpress_logged_in_`, `woocommerce_items_in_cart`,
   `wp_woocommerce_session_`.
3. Cloudflare gratuito delante: DNS proxy activado, **Always Use HTTPS**, y una
   regla de límite de peticiones sobre `/descarga*` — pongamos 30 peticiones por
   minuto y dirección IP.

> **Comprobación, la que descubre el desastre**: con dos navegadores y dos
> cuentas distintas, entra a `/mi-cuenta` a la vez en ambos. Si alguno ve los
> temarios del otro, hay una página de sesión cacheada. Arréglalo antes de
> seguir.

---

## Fase 10 · Copias de seguridad y vigilancia

1. hPanel → **Archivos → Copias de seguridad**: automáticas diarias activadas.
2. Copia propia fuera de Hostinger —una copia que vive en el mismo sitio que el
   original no es una copia. Cron semanal en hPanel:

   ```bash
   tar czf ~/copias/temarios-$(date +\%F).tar.gz ~/temarios_privados
   ```

   y sincronízalo a otro sitio (tu equipo, un disco, un almacenamiento externo).
3. **UptimeRobot** gratuito vigilando la portada y `/tienda`.
4. WP → Ajustes → General: correo de administración a una dirección que **leas**.

> **Comprobación.** Restaura la copia en el sitio de pruebas de Hostinger y
> comprueba que arranca. Una copia sin restaurar es una hipótesis.

---

## Fase 11 · Textos legales

Sin esto no se puede abrir en España. La lista y qué debe decir cada uno está en
[`05-LANZAMIENTO.md`](05-LANZAMIENTO.md) §5.1. En resumen: aviso legal con tus
datos identificativos, privacidad, cookies con banner de consentimiento previo,
condiciones de venta con la **renuncia expresa al desistimiento** —la casilla
obligatoria de la que depende que no te devuelvan un temario ya descargado— y
enlace a la plataforma europea de resolución de litigios.

---

## Fase 12 · Lanzamiento

En este orden, y no en otro:

1. Stripe a **modo real**; repite la compra de prueba con tu tarjeta de verdad y
   reembólsala.
2. Comprueba que el correo de confirmación llega y **no cae en no deseado**
   (prueba con Gmail, Outlook y una cuenta corporativa).
3. Quita el modo mantenimiento, `noindex` fuera: WP → Ajustes → Lectura.
4. Envía el `sitemap.xml` a Google Search Console.
5. Vigila los tres primeros pedidos reales de principio a fin, mirando los
   registros. Los fallos raros salen ahí y no en las pruebas.

> **Comprobación final.** Una persona ajena, desde su móvil, con su Google,
> compra un temario y lo tiene descargado sin escribirte. Si tiene que
> preguntarte algo, la tienda no está terminada.
