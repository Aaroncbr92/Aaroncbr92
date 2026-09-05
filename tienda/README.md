# Tienda TOAC — venta de los temarios

Entrega de arquitectura, plan de implantación y código para vender en
automático los **veinticinco volúmenes** de `libro-*.pdf` desde el alojamiento
Unlimited de Hostinger.

## La decisión, en una línea

**WordPress + WooCommerce sobre el Hostinger que ya tienes**, con las descargas
y las muestras servidas por un plugin propio (`toac-tienda.php`) que guarda los
PDF **fuera de `public_html`** y nunca publica una URL de fichero.

El porqué —y cuándo esa decisión sería la equivocada— está en
[`01-ARQUITECTURA.md`](01-ARQUITECTURA.md).

## Los documentos

| Fichero | Qué resuelve |
|---|---|
| [`01-ARQUITECTURA.md`](01-ARQUITECTURA.md) | Stack elegido, las dos alternativas descartadas y con qué criterio, y el mapa de piezas. |
| [`02-IMPLANTACION.md`](02-IMPLANTACION.md) | Paso a paso desde el hPanel de Hostinger hasta el lanzamiento. Doce fases, con lo que hay que verificar en cada una. |
| [`03-PDFS.md`](03-PDFS.md) | Previsualización sin descarga, descarga protegida, marca de agua nominativa y qué protege de verdad cada capa. |
| [`04-PAGOS.md`](04-PAGOS.md) | Stripe (recomendado) y PayPal, webhooks, IVA/OSS y el desistimiento de contenido digital. |
| [`05-LANZAMIENTO.md`](05-LANZAMIENTO.md) | Textos legales obligatorios, precios propuestos, copias de seguridad, métricas y la lista de comprobación previa a abrir. |

## El código

| Fichero | Qué es |
|---|---|
| [`codigo/mu-plugins/toac-tienda.php`](codigo/mu-plugins/toac-tienda.php) | El plugin principal. Catálogo con fecha de actualización, muestra en línea, descarga firmada, registro de descargas y «Mis temarios». |
| [`codigo/mu-plugins/toac-google-sso.php`](codigo/mu-plugins/toac-google-sso.php) | Inicio de sesión con Google a medida (OAuth 2.0 + PKCE), por si no quieres depender de un plugin de terceros. |
| [`codigo/mu-plugins/toac-blindaje.php`](codigo/mu-plugins/toac-blindaje.php) | Cierre del área privada: sin caché, sin `wp-admin` para clientes, sin enumeración de usuarios, sin XML-RPC. |
| [`codigo/tema-hijo/`](codigo/tema-hijo/) | Tema hijo: ficha del temario, distintivo de «Actualizado el…» y hoja de estilo. |
| [`codigo/servidor/`](codigo/servidor/) | `.htaccess` de las carpetas de ficheros y el añadido a `wp-config.php`. |
| [`../herramientas/muestra.py`](../herramientas/muestra.py) | Genera los PDF de muestra (portada + índice + primeras páginas, con marca de agua) desde cada `libro-*.pdf`. |
| [`../herramientas/catalogo.py`](../herramientas/catalogo.py) | Genera el CSV de abajo leyendo cada dato de los propios volúmenes. Se vuelve a pasar cada vez que cambie uno. |
| [`catalogo/productos.csv`](catalogo/productos.csv) | Los veinticinco volúmenes listos para importar en WooCommerce, con páginas, temas, preguntas, plazas y precio propuesto. **Generado, no escrito a mano.** |

Las dos herramientas se pasan así, desde la raíz del repositorio:

```bash
python3 herramientas/muestra.py                       # muestras/muestra-*.pdf
python3 herramientas/catalogo.py --url tu-dominio.es  # tienda/catalogo/productos.csv
```

## Lo que hay que decidir antes de empezar

1. **Dominio.** Aún no hay ninguno en el repositorio. Los documentos usan
   `temarios.example` como marcador; hay que sustituirlo.
2. **Logotipo.** `marca/toac.svg` sigue pendiente (ver `marca/README.md`). La
   tienda lo necesita para la cabecera y para la marca de agua de las muestras.
3. **Pasarela.** La entrega asume **Stripe como principal y PayPal como
   secundaria**, porque WooCommerce las soporta a la vez y no obliga a elegir.
   Si sólo quieres una, quita la otra en la fase 7 de `02-IMPLANTACION.md`.
4. **Quién declara el IVA.** Vender contenido digital a consumidores de la UE
   obliga a la ventanilla única (OSS) desde el primer euro fuera de España.
   `04-PAGOS.md` explica la alternativa que te quita eso de encima, y lo que
   cuesta.
