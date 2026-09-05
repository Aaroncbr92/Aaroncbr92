# 1 · Arquitectura

## 1.1 Lo que impone el alojamiento

Antes de elegir stack conviene decir en voz alta qué es un plan Unlimited de
Hostinger, porque descarta media baraja por sí solo:

- Es **alojamiento compartido con LiteSpeed**, no un VPS. No hay `root`, no hay
  `systemd`, no se dejan procesos vivos: un `node server.js` o un
  `php artisan queue:work` se mata en cuanto la sesión SSH se cierra.
- Hay **PHP 8.x y MySQL**, `.htaccess` (LiteSpeed lo interpreta), cron real
  desde el hPanel, SSH y Git en los planes que lo incluyen —conviene verificarlo
  en tu panel antes de la fase 2.
- Los recursos se miden en **procesos de entrada y en I/O**, no en «CPU
  ilimitada». Un pico de descargas concurrentes de PDF de 3 MB es lo primero que
  te va a topar, y eso condiciona cómo se sirven los ficheros (§3.4).
- «Unlimited» es de espacio, no de tráfico útil. Los veinticinco volúmenes pesan
  **45 MB en total**: el catálogo cabe de sobra. El problema nunca va a ser
  guardar, va a ser servir.

## 1.2 Las tres opciones sobre la mesa

### Opción A — WordPress + WooCommerce sobre el Hostinger actual ← **la recomendada**

WooCommerce ya trae resuelto, y probado por millones de tiendas, exactamente el
problema que tienes: pedido pagado → derecho de descarga → panel de cliente. Lo
que se programa a medida es sólo lo que WooCommerce no cubre bien: la muestra en
línea y el endurecimiento de la entrega del fichero.

**A favor**

- **Cero infraestructura.** Es el único de los tres que corre tal cual en un
  compartido, sin procesos residentes ni colas.
- **La lógica de dinero no la escribes tú.** Pasarela oficial de Stripe y de
  PayPal, con sus webhooks, sus reintentos y sus reembolsos ya implementados.
  Cada línea de código de pagos que no escribes es una vulnerabilidad que no
  introduces.
- **Mantenimiento realista para una persona.** Actualizaciones desde el hPanel,
  copias automáticas, y una comunidad que documenta cada error antes de que te
  ocurra.
- **La seguridad del fichero no depende del CMS.** Es la objeción habitual y es
  falsa cuando el PDF vive fuera de `public_html` y lo sirve un endpoint propio.
  Con el diseño de §1.4 el fichero es igual de inalcanzable que en un Laravel.

**En contra, y hay que asumirlo**

- Superficie de ataque mayor: cada plugin es código de terceros con acceso a la
  base de datos. Se compensa con disciplina: **pocos plugins, todos de autor
  conocido, todos actualizados** (la lista cerrada está en §1.5).
- Rendimiento mediocre si se deja por defecto. LiteSpeed Cache lo arregla, pero
  hay que excluir de caché las páginas de cuenta, carrito y pago, o acabas
  sirviendo la sesión de un usuario a otro. Está en la fase 9.

### Opción B — Desarrollo a medida (Laravel, o Node)

**Laravel** cabe técnicamente en un compartido —hay quien lo hace apuntando el
dominio a `public/`— pero el resultado es frágil: sin `supervisor` no tienes
colas, el `schedule:run` depende del cron del panel, `composer install` en
producción es lento, y el despliegue sin CI es a mano.

**Node queda directamente descartado**: el compartido de Hostinger no ejecuta
procesos persistentes. Node exigiría un VPS, es decir, otro plan y, sobre todo,
**ser tú el administrador de sistemas**: parches del kernel, `fail2ban`,
renovación de certificados, copias de seguridad.

Elegir A o B es elegir dónde gastas tus horas. En B escribes tú el flujo de
OAuth, el manejo de webhooks de Stripe con su idempotencia, la firma de enlaces,
el panel de administración y las facturas. Son entre dos y cuatro semanas de
trabajo, y luego son tuyas para siempre: cada fallo de seguridad en ese código
es tuyo.

**Cuándo B sería lo correcto**: si el producto dejara de ser «descargar un PDF»
y pasara a ser un lector en línea con progreso, tests autocorregidos y
estadísticas por tema. Ahí WooCommerce estorbaría. Hoy no es el caso, y montar
hoy la arquitectura de ese hipotético mañana es el error clásico.

### Opción C — Plataforma con vendedor de registro (Lemon Squeezy, Paddle, Gumroad)

Se sube el PDF, ellos cobran, ellos entregan y —esto es lo importante— **ellos
son el vendedor a efectos fiscales**: declaran el IVA de cada país de la UE por
ti. Te quitan de encima la ventanilla única (OSS), las facturas y la pasarela.

**El precio**: entre un 5 % y un 10 % de cada venta, la marca es suya, el
catálogo vive en su dominio y el día que suban comisiones o cierren, migras.

**Cuándo tiene sentido**: si el volumen previsto es bajo y prefieres no tener
obligaciones fiscales intracomunitarias. Es una decisión de negocio, no técnica,
y es legítima. Con veinticinco volúmenes propios y una marca (TOAC) que ya
existe en los libros, la recomendación es tienda propia.

## 1.3 Comparativa

| | A · WP + Woo | B · Laravel a medida | C · Vendedor de registro |
|---|---|---|---|
| Corre en tu Hostinger actual | **Sí** | Con dolor | No aplica |
| Tiempo hasta vender | **3–5 días** | 3–5 semanas | 1 día |
| Código de pagos que escribes | Ninguno | Todo | Ninguno |
| Seguridad del PDF | Igual (§1.4) | Igual | La suya |
| IVA de la UE | **Tuyo** | Tuyo | **Suyo** |
| Coste recurrente | Hosting + ~0 | Hosting/VPS + tu tiempo | 5–10 % de ventas |
| Dueño de la relación con el cliente | **Tú** | Tú | Ellos |

## 1.4 El diseño de la entrega de ficheros

Es el corazón de la propuesta, y es lo que hace que la objeción de seguridad
contra WordPress no aplique. **Ningún PDF completo vive bajo el dominio.**

```
/home/uXXXXXXX/
├── temarios_privados/          ← FUERA de public_html. Inalcanzable por HTTP.
│   ├── libros/                 ← libro-*.pdf, los 25 volúmenes completos
│   └── muestras/               ← muestra-*.pdf, portada + índice + 12 páginas
└── public_html/                ← el dominio apunta aquí
    ├── wp-admin/ wp-includes/ …
    └── wp-content/
```

El único camino hasta un fichero es este, y pasa entero por PHP:

```
Navegador
   │  GET /descarga/libro-sonido?t=<token firmado>
   ▼
WordPress ── toac-tienda.php
   │  1. ¿Sesión iniciada?                        → si no, 302 a /mi-cuenta
   │  2. ¿El token verifica el HMAC y no caducó?  → si no, 403
   │  3. ¿Ese usuario tiene un pedido pagado
   │     con ese producto?                        → si no, 403
   │  4. ¿Ha pasado el límite diario?             → si no, 429
   │  5. Anota la descarga (quién, qué, cuándo)
   │  6. Sella el PDF con nombre y correo (opc.)
   ▼
LiteSpeed ── X-LiteSpeed-Send-File: /home/…/libro-sonido.pdf
   │  El servidor sirve el fichero él mismo, sin cargarlo en memoria de PHP.
   ▼
Navegador
```

Los cuatro puntos que hacen que esto aguante:

1. **La ruta del fichero nunca sale al HTML.** No hay enlace directo que copiar
   ni URL que adivinar; el token no contiene la ruta, contiene el identificador
   del producto.
2. **El derecho se comprueba en cada petición**, contra el pedido pagado. No es
   un enlace «mágico» que caduca: es una autorización que se vuelve a evaluar.
3. **El token caduca en minutos** y va firmado con HMAC-SHA256 contra una clave
   que sólo está en `wp-config.php`. Compartir la URL por un grupo de Telegram no
   sirve de nada: al de un rato ya no abre, y al de otro usuario tampoco.
4. **Lo que se comparte queda marcado.** El sello con nombre y correo del
   comprador en el pie de cada página es, de lejos, lo que más frena la difusión.
   No es criptografía: es que nadie sube a un grupo un PDF con su propio correo
   en las 259 páginas.

Y la propiedad bonita de este diseño: como el endpoint resuelve **el fichero
actual** del producto, cuando regeneres un volumen con `libro.py` y lo subas,
todos los que ya compraron descargan la versión nueva sin que toques nada. La
actualización del temario es el argumento de venta y sale gratis.

## 1.5 Piezas, y por qué cada una

Lista cerrada. Cada plugin añadido fuera de esta lista es superficie nueva.

| Pieza | Elección | Por qué |
|---|---|---|
| CMS + tienda | WordPress + WooCommerce | §1.2 |
| Tema | Twenty Twenty-Five + tema hijo | Núcleo, sin sobrecarga. El hijo va en `codigo/tema-hijo/`. |
| Pagos | WooCommerce Stripe Gateway (oficial) | Mantenido por Stripe. PayPal Payments como segunda opción. |
| Acceso con Google | **`toac-google-sso.php`** propio, o Nextend Social Login | El propio no añade dependencias; el plugin ahorra mantenimiento. Ver §4 de `02-IMPLANTACION.md`. |
| Muestra en línea | PDF.js autoalojado + `muestra.py` | Sin servicio externo: el PDF no sale de tu servidor. |
| Descarga | `toac-tienda.php` propio | §1.4 |
| Caché | LiteSpeed Cache | Nativo del servidor de Hostinger; gratis y el que mejor se lleva con él. |
| Seguridad | Cloudflare gratuito + `toac-blindaje.php` | Cortafuegos y límite de peticiones delante; el resto en código propio. |
| Facturas | PDF Invoices & Packing Slips + EU/UK VAT | Obligatorio para facturar; ver `04-PAGOS.md`. |
| Correo transaccional | SMTP de Brevo o Mailgun, vía WP Mail SMTP | El `mail()` del compartido acaba en la carpeta de no deseado. Y si el correo de compra no llega, el cliente cree que le has robado. |

## 1.6 Modelo de datos

Casi todo cabe en lo que WooCommerce ya tiene. Sólo hay dos añadidos.

**Campos propios del producto** (metadatos, los pone `toac-tienda.php`):

| Clave | Ejemplo | Para qué |
|---|---|---|
| `_toac_slug` | `sonido` | Ata el producto a `libro-sonido.pdf` y a `muestra-sonido.pdf`. |
| `_toac_actualizado` | `2026-09-04` | La fecha que pide el requisito 2. Se muestra en catálogo y ficha. |
| `_toac_paginas` | `207` | Ficha del producto. |
| `_toac_temas` | `18` | Ficha. |
| `_toac_preguntas` | `134` | Ficha. |
| `_toac_puestos` | `68` | Plazas de esa ocupación en la convocatoria. Vende solo. |

**Tabla propia**, la única: `wp_toac_descargas` — `id`, `user_id`, `producto_id`,
`ip`, `agente`, `fecha`. Sirve para el límite diario, para detectar una cuenta
compartida entre veinte personas, y para poder responder «sí, se descargó» ante
una reclamación.

El derecho de descarga **no se guarda**: se deriva siempre de los pedidos
pagados. Un estado menos que pueda quedarse desincronizado con la realidad.
