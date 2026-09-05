# Guía paso a paso: de cero a vender

Un solo camino, en orden. No hace falta saber programar: hay que copiar y
pegar comandos y rellenar formularios.

**Cinco partes.** Las tres primeras se hacen del tirón en una mañana. La cuarta
son cuatro trámites que dependen de terceros y llevan su tiempo. La quinta es
abrir.

| Parte | Qué es | Tiempo |
|---|---|---|
| **A** | Preparar Hostinger | 1 h |
| **B** | Preparar tu ordenador | 30 min |
| **C** | El despliegue, en un comando | 20 min |
| **D** | Los cuatro trámites que sólo puedes hacer tú | 2–3 h, repartidas |
| **E** | Comprobar y abrir | 1 h |

**Ten a mano antes de empezar:** tu cuenta de Hostinger, una tarjeta, tu NIF y
tu domicilio fiscal (van en el aviso legal), una cuenta de Google y un correo
que leas de verdad.

> Los menús del hPanel cambian de nombre de vez en cuando. Si no encuentras uno
> tal como lo escribo aquí, usa el buscador del propio panel: los nombres que
> doy son los términos que hay que buscar.

---

# PARTE A · Hostinger

## A1 · El dominio

hPanel → **Dominios**.

- Si tu plan incluye dominio gratis, regístralo aquí.
- Si ya tienes uno en otro sitio, apunta sus DNS a Hostinger.

Elige un nombre corto y que se dicte por teléfono sin deletrear.

**Anota el dominio.** Lo vas a necesitar cinco veces más. Ejemplo a lo largo de
esta guía: `temarios-toac.es`.

> **Sabrás que va bien** cuando al escribir tu dominio en el navegador salga
> algo —aunque sea la página de bienvenida de Hostinger—. Puede tardar de unos
> minutos a unas horas. Sigue con A2 mientras tanto.

## A2 · El certificado (candado)

hPanel → **Seguridad → SSL** → instalar el certificado gratuito.

Y luego, en la misma pantalla o en **Rendimiento**, activa **Forzar HTTPS**.

> **Sabrás que va bien** cuando `https://tu-dominio` cargue con el candado y
> `http://tu-dominio` te lleve solo al `https`.

## A3 · Instalar WordPress

hPanel → **Sitios web** → tu web → **WordPress** → **Instalar**.

Tres cosas que importan al rellenar el formulario:

1. El usuario administrador **no se llama `admin`**. Pon otro nombre.
2. La contraseña, la que genere el panel. No una que te inventes.
3. El correo, uno que leas.

**Guarda usuario y contraseña en tu gestor de contraseñas.** No en un papel ni
en un `.txt` del escritorio.

## A4 · Ajustar PHP

hPanel → **Avanzado → Configuración PHP**.

Versión: **8.2 o 8.3**.

Y en la pestaña de opciones, deja estos valores:

| Opción | Valor |
|---|---|
| `memory_limit` | `256M` |
| `upload_max_filesize` | `64M` |
| `post_max_size` | `64M` |
| `max_execution_time` | `120` |
| `opcache.enable` | activado |
| `display_errors` | **desactivado** |

El último no es cosmético: un aviso de PHP en pantalla enseña rutas internas de
tu servidor a cualquiera que pase.

## A5 · Activar SSH y apuntar tres datos

hPanel → **Avanzado → Acceso SSH** → **Activar**.

Esa pantalla te da tres datos. **Apúntalos, los necesitas en B5:**

```
Host (o IP):  ...............
Usuario:      u........        ← empieza por «u» y siete u ocho cifras
Puerto:       .....           ← NO es el 22. Suele ser 65002
```

En la misma pantalla verás la **ruta** de tu web, algo como
`/home/u1234567/public_html`. Apúntala también.

---

# PARTE B · Tu ordenador

## B1 · Abrir una terminal

- **Mac**: Aplicaciones → Utilidades → **Terminal**.
- **Windows**: instala [Git for Windows](https://git-scm.com/download/win) y
  abre **Git Bash**. No sirve PowerShell ni el símbolo del sistema: los scripts
  son de `bash`.
- **Linux**: la que uses.

## B2 · Comprobar que tienes git y Python

Pega esto y pulsa Intro:

```bash
git --version && python3 --version
```

Tienen que salir dos versiones. Si alguna falla:

- **git**: en Mac, `xcode-select --install`. En Windows viene con Git Bash.
- **Python**: bájalo de [python.org](https://www.python.org/downloads/). En
  Windows, marca **«Add Python to PATH»** en el instalador.

## B3 · Traerte el repositorio

```bash
cd ~
git clone https://github.com/Aaroncbr92/Aaroncbr92.git temarios
cd temarios
git checkout claude/rtve-temarios-ecommerce-0nocvg
```

> **Sabrás que va bien** si `ls` enseña los `libro-*.pdf` y una carpeta
> `tienda`.

**A partir de aquí, todos los comandos se ejecutan desde esta carpeta.** Si
cierras la terminal y vuelves, empieza con `cd ~/temarios`.

## B4 · Instalar las tres librerías de Python

```bash
python3 -m pip install pypdf reportlab markdown-it-py
```

Son las que generan las muestras y el catálogo. Si da un error de permisos,
añade `--user` al final.

## B5 · Rellenar los seis datos

```bash
nano tienda/despliegue/config.sh
```

(Si `nano` te resulta incómodo, abre ese fichero con cualquier editor de texto.)

Sustituye con lo que apuntaste en A5:

```bash
SSH_HOST="temarios-toac.es"          # o la IP que te dio el panel
SSH_USER="u1234567"
SSH_PUERTO="65002"

DOMINIO="temarios-toac.es"           # sin https://
RUTA_WP="/home/u1234567/public_html"
CORREO_ADMIN="tu-correo@ejemplo.com"
```

En `nano` se guarda con **Ctrl+O**, Intro, y se sale con **Ctrl+X**.

## B6 · Dejar lista la conexión

```bash
bash tienda/despliegue/preparar-ssh.sh
```

El script:

1. Busca tu clave SSH. Si no tienes, la crea (te preguntará una contraseña para
   la clave: puedes dejarla vacía pulsando Intro dos veces).
2. Te enseña en pantalla tu **clave pública**, un bloque que empieza por
   `ssh-ed25519 AAAA...`.
3. Espera a que la pegues en **hPanel → Avanzado → Acceso SSH → Claves SSH →
   Añadir**.
4. Prueba la conexión.

> **La distinción que importa:** la clave **pública** está hecha para
> enseñarse; pegarla en el hPanel es exactamente su función. La **privada** —el
> fichero sin `.pub`— no sale de tu ordenador, no la pega uno en ningún sitio y
> no hay que dársela a nadie, yo incluido.

> **Sabrás que va bien** cuando el script termine con
> «Todo listo. El siguiente paso es…».

---

# PARTE C · El despliegue

## C1 · Ver qué va a hacer, sin que haga nada

```bash
bash tienda/despliegue/desplegar.sh --simulacro
```

Imprime cada orden que ejecutaría, sin tocar tu servidor. Léelo por encima:
verás las carpetas que va a crear, los 25 volúmenes que va a subir y los
ficheros que va a colocar.

## C2 · Hacerlo

```bash
bash tienda/despliegue/desplegar.sh
```

Tarda unos minutos: se van 55 MB de PDF por la red. Verás pasar nueve
apartados y, al final, las comprobaciones.

Esto deja montado: las carpetas privadas fuera de la web, los 25 volúmenes y
sus muestras, los tres plugins propios, el tema, WooCommerce configurado, la
clave de firma de los enlaces —generada en tu servidor—, el visor PDF.js, la
caché, las cinco páginas legales en blanco y **los 25 productos con su precio y
su fecha de actualización**.

> **Si algo falla**, el script te dice qué y para. No deja nada a medias que
> rompa la web: no borra, hace copia de `wp-config.php` antes de tocarlo y
> respeta lo que ya exista. Se puede volver a lanzar las veces que haga falta.

## C3 · Mirarlo con tus ojos

Abre en el navegador:

- `https://tu-dominio/tienda/` → los 25 temarios, cada uno con su fecha
- `https://tu-dominio/muestra/sonido/` → el visor con el índice y 12 páginas
- `https://tu-dominio/mi-cuenta/` → el acceso

Y prueba lo importante: pega
`https://tu-dominio/temarios_privados/libros/libro-sonido.pdf` en el navegador.
**Tiene que dar error.** Si te descarga el PDF, para y avísame.

---

# PARTE D · Los cuatro trámites que sólo puedes hacer tú

No es una limitación del programa: es que los cuatro exigen ser el titular.
Puedes hacerlos en cualquier orden, y la tienda ya funciona sin ellos —lo que
no puede es cobrar ni dejar entrar con Google—.

## D1 · Entrar con Google (30 min)

1. Ve a [console.cloud.google.com](https://console.cloud.google.com) → arriba,
   **Nuevo proyecto** → nómbralo `TOAC Temarios`.
2. Menú → **APIs y servicios → Pantalla de consentimiento de OAuth**.
   - Tipo: **Externo**
   - Nombre de la aplicación, tu correo de asistencia y tu logotipo
   - **Enlaces a tu aviso legal y a tu política de privacidad**: son
     `https://tu-dominio/aviso-legal/` y `https://tu-dominio/privacidad/`, que
     el despliegue ya creó
   - Permisos: `email`, `profile` y `openid`. Ninguno más.
3. **Credenciales → Crear credenciales → ID de cliente de OAuth → Aplicación
   web**:
   - Orígenes autorizados: `https://tu-dominio`
   - URI de redirección: `https://tu-dominio/?toac_google=callback`
4. Copia el **ID de cliente** y el **secreto**.
5. **Publica la aplicación** (botón «Publicar app»). Mientras esté en *Prueba*
   sólo entran las cuentas que listes a mano.
6. Vuelve a tu terminal y pégalos:

```bash
ssh -p 65002 u1234567@tu-dominio
cd /home/u1234567/public_html
wp config set TOAC_GOOGLE_ID 'PEGA-AQUI-EL-ID' --type=constant
wp config set TOAC_GOOGLE_SECRETO 'PEGA-AQUI-EL-SECRETO' --type=constant
exit
```

> **Compruébalo:** en una ventana de incógnito, entra en
> `https://tu-dominio/mi-cuenta/`, pulsa **Continuar con Google** y termina el
> ciclo. Luego **hazlo otra vez**: la segunda vez debe entrar en la misma
> cuenta, no crear otra.

## D2 · Cobrar con Stripe (1 h, más lo que tarde la verificación)

1. Crea la cuenta en [stripe.com](https://stripe.com) y **actívala**: te pedirá
   NIF, domicilio, actividad e IBAN. Es verificación de identidad; puede tardar
   de unas horas a un par de días.
2. En tu web: **Plugins → Añadir nuevo → «WooCommerce Stripe Gateway»**
   (el oficial, de Stripe) → Instalar y activar.
3. **WooCommerce → Ajustes → Pagos → Stripe → Conectar**. Déjalo en
   **modo de pruebas**.
4. Activa los métodos: tarjeta, **Bizum**, Apple Pay y Google Pay.
5. En el panel de Stripe → **Desarrolladores → Webhooks → Añadir**:
   - URL: `https://tu-dominio/?wc-api=wc_stripe`
   - Eventos: `payment_intent.succeeded`, `payment_intent.payment_failed`,
     `charge.refunded`, `charge.dispute.created`
   - Copia el secreto `whsec_…` y pégalo en los ajustes del plugin.

   **Este paso no es opcional.** Sin él, un pago que se confirme con retraso
   —una autenticación que el cliente termina en el móvil— no marca el pedido
   como pagado, y el cliente paga y no recibe nada.

6. **Prueba las cuatro**, en modo de pruebas:

   | Tarjeta | Qué tiene que pasar |
   |---|---|
   | `4242 4242 4242 4242` | Pedido completado y temario en «Mis temarios» |
   | `4000 0025 0000 3155` | Pide autenticación; al superarla, completado |
   | `4000 0000 0000 9995` | Pedido **fallido** y **ninguna descarga** |
   | Reembolso desde Stripe | El pedido pasa a reembolsado |

   La tercera es la que de verdad importa.

## D3 · Los textos legales (1–2 h)

El despliegue creó cinco páginas vacías, marcadas como pendientes:
`/aviso-legal/`, `/privacidad/`, `/cookies/`, `/condiciones-venta/` y
`/contacto/`.

Qué tiene que decir cada una está en
[`05-LANZAMIENTO.md` §5.1](05-LANZAMIENTO.md). Lo que no puede faltar:

- Tu **nombre o razón social, NIF, domicilio y correo** en el aviso legal.
- En privacidad, **nombrar a Stripe, a Google y a tu proveedor de correo** como
  cesionarios de datos, y mencionar el registro de descargas. Esto no viene en
  ninguna plantilla genérica: hay que escribirlo.
- En condiciones de venta, la **renuncia expresa al desistimiento** para
  contenido digital. El código ya pone la casilla obligatoria en el pago y
  guarda la prueba en el pedido; las condiciones tienen que decirlo también.
- Un **banner de cookies** con consentimiento previo (plugin de consentimiento;
  vale uno gratuito).

> Una revisión de un abogado cuesta bastante menos que una sanción, y mucho
> menos que reescribir las condiciones cuando ya hay doscientos clientes que
> aceptaron otras.

## D4 · El logotipo (15 min)

`marca/toac.svg` sigue pendiente desde antes de esto (ver `marca/README.md`).
Súbelo al repositorio y luego a la web, en **Apariencia → Personalizar**.

Si sólo tienes el render con fondo gris, hay que recortarlo: el fondo es un
color plano y sale limpio.

---

# PARTE E · Abrir

## E1 · Las comprobaciones automáticas

```bash
cd ~/temarios
bash tienda/despliegue/comprobar.sh
```

Veintinueve comprobaciones contra tu dominio. Las de los apartados **«Los
ficheros»** y **«La descarga»** son las que obligan a parar: si alguna falla,
hay un temario alcanzable sin pagar.

## E2 · Las que hay que hacer a mano

Estas cinco no las puede hacer un script:

- [ ] Dos navegadores, dos cuentas distintas, `/mi-cuenta/` abierto a la vez en
      ambos → **cada uno ve lo suyo**. Si uno ve los temarios del otro, hay una
      página de sesión cacheada y hay que arreglarlo antes de abrir.
- [ ] Compra real con tu tarjeta, de principio a fin, y reembólsala después.
- [ ] El correo de compra llega a Gmail, a Outlook y a una cuenta corporativa,
      **y no a la carpeta de no deseado**.
- [ ] Copia el enlace de descarga de «Mis temarios», espera once minutos y
      ábrelo → te devuelve a tu panel con un aviso, no el PDF.
- [ ] Ese mismo enlace, pegado en la sesión de otra cuenta → error.

La lista completa, con las diecisiete, está en
[`05-LANZAMIENTO.md` §5.3](05-LANZAMIENTO.md).

## E3 · Abrir

En este orden:

1. Stripe a **modo real**. Repite la compra con tu tarjeta de verdad y
   reembólsala.
2. WordPress → **Ajustes → Lectura** → quita el «disuadir a los motores de
   búsqueda».
3. hPanel → **Archivos → Copias de seguridad** → automáticas activadas.
4. Envía tu `sitemap.xml` a Google Search Console.
5. **Vigila los tres primeros pedidos reales de principio a fin.** Los fallos
   raros salen ahí y no en las pruebas.

> **La comprobación final**, y es la única que cuenta: que una persona ajena,
> desde su móvil, con su Google, compre un temario y lo tenga descargado sin
> escribirte. Si tiene que preguntarte algo, la tienda no está terminada.

---

# Después

## Cuando actualices un temario

```bash
cd ~/temarios
python3 herramientas/libro.py sonido && python3 herramientas/pdf.py libro-sonido.html
bash tienda/despliegue/desplegar.sh
```

Sube el volumen nuevo, regenera su muestra y actualiza la fecha del producto.
**Los que ya lo compraron descargan la versión nueva sin que toques nada más.**

Y avísales por correo. Un temario de oposiciones vale lo que vale su fecha, y
ahí es donde un PDF pirata de hace tres convocatorias no compite contigo.

## Media hora al mes

1. Actualizar WordPress, WooCommerce y los plugins (copia de seguridad antes).
2. Revisar la consulta de cuentas compartidas de
   [`03-PDFS.md` §3.7](03-PDFS.md).
3. Comprobar que la copia semanal fuera de Hostinger existe y pesa lo que debe.
4. Mirar si ha cambiado alguna norma de los temarios.

---

# Si algo se tuerce

| Lo que ves | Lo que suele ser |
|---|---|
| `preparar-ssh.sh` dice que no conecta | La clave tarda un par de minutos en valer. O el puerto no es el 22 (mira A5). O el acceso SSH está desactivado. |
| «No veo WordPress en …» | La `RUTA_WP` de `config.sh` no es esa. Míralo con `ssh -p PUERTO USUARIO@HOST 'ls ~'`. |
| «Faltan librerías de Python» | Ejecuta el `pip install` que el propio mensaje te da. |
| El catálogo no enseña la fecha | El tema hijo no está activo: Apariencia → Temas → **TOAC Temarios**. |
| El visor de la muestra sale en blanco | PDF.js no se bajó. El instalador te lo dijo; bájalo de github.com/mozilla/pdf.js/releases y descomprímelo en `wp-content/uploads/pdfjs/`. |
| Un usuario ve la sesión de otro | Caché en páginas privadas. Fase 9 de [`02-IMPLANTACION.md`](02-IMPLANTACION.md). |
| Descarga un PDF sin pagar | **Para.** Es lo único que obliga a cerrar la tienda hasta arreglarlo. |

Con cualquiera de estos, pégame el mensaje de error tal cual y lo miramos.
