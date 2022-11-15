
# basket-add

Display the "add to basket" button for each product item in the catalog home component

```
client/html/catalog/home/basket-add =
```

* Default:
* Type: boolean - True to display the button, false to hide it
* Since: 2020.10

Enables the button for adding products to the basket for the listed products.
This works for all type of products, even for selection products with product
variants and product bundles. By default, also optional attributes are
displayed if they have been associated to a product.

See also:

* client/html/catalog/lists/basket-add
* client/html/catalog/detail/basket-add
* client/html/basket/related/basket-add
* client/html/catalog/product/basket-add

# cache

Enables or disables caching only for the catalog home component

```
client/html/catalog/home/cache = 1
```

* Default: 1
* Type: boolean - True to enable caching, false to disable

Disable caching for components can be useful if you would have too much
entries to cache or if the component contains non-cacheable parts that
can't be replaced using the modify() method.

See also:

* client/html/catalog/detail/cache
* client/html/catalog/filter/cache
* client/html/catalog/stage/cache
* client/html/catalog/list/cache

# decorators
## excludes

```
client/html/catalog/home/decorators/excludes = Array
(
)
```

* Default: Array
(
)



## global

```
client/html/catalog/home/decorators/global = Array
(
)
```

* Default: Array
(
)



## local

```
client/html/catalog/home/decorators/local = Array
(
)
```

* Default: Array
(
)



# domains

A list of domain names whose items should be available in the catalog home view template

```
client/html/catalog/home/domains = Array
(
    [0] => catalog
    [1] => media
    [2] => media/property
    [3] => price
    [4] => supplier
    [5] => text
    [product] => Array
        (
            [0] => promotion
        )

)
```

* Default: Array
(
    [0] => catalog
    [1] => media
    [2] => media/property
    [3] => price
    [4] => supplier
    [5] => text
    [product] => Array
        (
            [0] => promotion
        )

)

* Type: array - List of domain names
* Since: 2020.10

The templates rendering home lists usually add the images, prices
and texts associated to each home item. If you want to display additional
content like the home attributes, you can configure your own list of
domains (attribute, media, price, home, text, etc. are domains)
whose items are fetched from the storage. Please keep in mind that
the more domains you add to the configuration, the more time is required
for fetching the content!

This configuration option overwrites the "client/html/catalog/domains"
option that allows to configure the domain names of the items fetched
for all catalog related data.

See also:

* client/html/catalog/domains
* client/html/catalog/detail/domains
* client/html/catalog/stage/domains
* client/html/catalog/lists/domains

# imageset-sizes

Size hints for loading the appropriate catalog home image sizes

```
client/html/catalog/home/imageset-sizes =
```

* Default:
* Type: string - HTML image "sizes" attribute
* Since: 2021.04

Modern browsers can load images of different sizes depending on their viewport
size. This is also known as serving "responsive images" because on small
smartphone screens, only small images are loaded while full width images are
loaded on large desktop screens.

A responsive image contains additional "srcset" and "sizes" attributes:

```
 <img src="img.jpg"
 	srcset="img-small.jpg 240w, img-large.jpg 720w"
 	sizes="(max-width: 320px) 240px, 720px"
 >
```

The images and their width in the "srcset" attribute are automatically added
based on the sizes of the generated preview images. The value of the "sizes"
attribute can't be determined by Aimeos because it depends on the used frontend
theme and the size of the images defined in the CSS file. This config setting
adds the required value for the "sizes" attribute.

It's value consists of one or more comma separated rules with
- an optional CSS media query for the view port size
- the (max) width the image will be displayed within this viewport size

Rules without a media query are independent of the view port size and must be
always at last because the rules are evaluated from left to right and the first
matching rule is used.

The above example tells the browser:
- Up to 320px view port width use img-small.jpg
- Above 320px view port width use img-large.jpg

For more information about the "sizes" attribute of the "img" HTML tag read:
{@link https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-sizes}

See also:

* client/html/common/imageset-sizes

# name

Class name of the used catalog home client implementation

```
client/html/catalog/home/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2019.06

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Catalog\Home\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Home\Myhome
```

then you have to set the this configuration option:

```
 client/html/catalog/home/name = Myhome
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyHome"!


# stock
## enable

Enables or disables displaying product stock levels in product list views

```
client/html/catalog/home/stock/enable = 1
```

* Default: 1
* Type: boolean - Value of "1" to display stock levels, "0" to disable displaying them
* Since: 2020.10

This configuration option allows shop owners to display product
stock levels for each product in list views or to disable
fetching product stock information.

The stock information is fetched via AJAX and inserted via Javascript.
This allows to cache product items by leaving out such highly
dynamic content like stock levels which changes with each order.

See also:

* client/html/catalog/detail/stock/enable
* client/html/catalog/stock/url/target
* client/html/catalog/stock/url/controller
* client/html/catalog/stock/url/action
* client/html/catalog/stock/url/config

# template-body

Relative path to the HTML body template of the catalog home client.

```
client/html/catalog/home/template-body = catalog/home/body
```

* Default: catalog/home/body
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2020.10

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/client/html).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/catalog/home/template-header

# template-header

Relative path to the HTML header template of the catalog home client.

```
client/html/catalog/home/template-header = catalog/home/header
```

* Default: catalog/home/header
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2020.10

The template file contains the HTML code and processing instructions
to generate the HTML code that is inserted into the HTML page header
of the rendered page in the frontend. The configuration string is the
path to the template file relative to the templates directory (usually
in templates/client/html).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/catalog/home/template-body

# url
## action

```
client/html/catalog/home/url/action = home
```

* Default: home


## config

```
client/html/catalog/home/url/config = Array
(
)
```

* Default: Array
(
)



## controller

```
client/html/catalog/home/url/controller = catalog
```

* Default: catalog


## target

```
client/html/catalog/home/url/target =
```

* Default:
