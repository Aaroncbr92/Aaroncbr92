# Despliegue en un comando

Monta en Hostinger todo lo que se puede montar sin ser tú.

```bash
# 1. Rellena seis datos
nano tienda/despliegue/config.sh

# 2. Mira lo que va a hacer, sin que haga nada
bash tienda/despliegue/desplegar.sh --simulacro

# 3. Hazlo
bash tienda/despliegue/desplegar.sh
```

Tarda unos minutos —lo que se van los 55 MB de PDF por la red— y se puede
repetir las veces que haga falta.

## Qué hace

| Paso | Qué monta |
|---|---|
| 1 | Regenera las 25 muestras y el catálogo desde los volúmenes de este repositorio. |
| 2 | Crea `~/temarios_privados/{libros,muestras,sellados}` **fuera de `public_html`**, con su `.htaccess` de red de seguridad. |
| 3 | Sube los 25 volúmenes y las 25 muestras (con `rsync` si lo tienes: la segunda vez sólo van los que cambien). |
| 4 | Coloca los tres mu-plugins, el tema hijo y el `.htaccess` de `uploads`. |
| 5 | Configura WordPress y WooCommerce por WP-CLI: constantes en `wp-config.php`, clave de firma generada en el servidor, moneda, cuenta obligatoria, sin envíos, tema hijo, PDF.js, LiteSpeed Cache, las cinco páginas legales y los 25 productos. |
| 6 | Comprueba desde fuera, con `curl`, que nada de lo que debe estar cerrado está abierto. |

## Qué NO hace, y no puede hacer ningún script

1. **Activar Stripe.** Pide tu NIF y tu IBAN: es verificación de identidad.
2. **Crear el proyecto de OAuth en Google.** Va contra tu cuenta de Google.
3. **Comprar el dominio y el certificado.** Se pagan con tu tarjeta.
4. **Redactar los textos legales.** Las cinco páginas quedan creadas con su
   esqueleto y marcadas como pendientes; los datos son tuyos.

Al terminar, el script los lista con las URL y los pasos exactos de cada uno.

## Lo que da por hecho

- **WordPress ya instalado** desde el hPanel (fase 2 de `../02-IMPLANTACION.md`)
  y el dominio con su certificado (fase 1). El script comprueba las dos cosas
  antes de tocar nada y para si faltan.
- **Acceso SSH con clave**, dado de alta en hPanel → Avanzado → Acceso SSH. No
  usa contraseñas: no se escribe ninguna en ningún fichero.
- **WP-CLI**, que Hostinger trae. Si no estuviera, el instalador se lo baja al
  `/tmp` del servidor y sigue.

## Lo que no rompe

- Hace **copia de `wp-config.php`** en `wp-config.php.antes-de-toac` antes de
  tocarlo, y **respeta toda constante que ya exista**.
- **No pisa un producto que ya esté**: refresca páginas, temas, preguntas y
  fecha —que es para lo que está `catalogo.py`— y deja en paz el precio y la
  descripción, que a esas alturas ya los habrás retocado a mano.
- **No borra nada.** Ni ficheros, ni páginas, ni pedidos.
- La **clave de firma** se genera en el servidor y no viaja ni se imprime. Si
  ya existía, se respeta: volver a desplegar no invalida los enlaces vivos.

## Volver a pasarlo cuando actualices un temario

```bash
python3 herramientas/libro.py sonido && python3 herramientas/pdf.py libro-sonido.html
bash tienda/despliegue/desplegar.sh
```

Sube el volumen nuevo, regenera su muestra y actualiza la fecha del producto.
Los que ya lo compraron descargan la versión nueva sin que toques nada más.

## Comprobar sin desplegar

```bash
bash tienda/despliegue/comprobar.sh
```

Veintinueve comprobaciones contra tu dominio, sin SSH. Las de los apartados
**«Los ficheros»** y **«La descarga»** son las que obligan a parar: si alguna
falla, hay un PDF alcanzable sin pagar.

Conviene pasarlo cada vez que toques un plugin, la caché o un `.htaccess`.
