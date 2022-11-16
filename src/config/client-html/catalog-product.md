
# basket-add

Display the "add to basket" button for each product item

```
client/html/catalog/product/basket-add = 
```

* Default: 
* Type: boolean - True to display the button, false to hide it
* Since: 2019.10

Enables the button for adding products to the basket for the listed products.
This works for all type of products, even for selection products with product
variants and product bundles. By default, also optional attributes are
displayed if they have been associated to a product.

**Note:** To fetch the necessary product variants, you have to extend the
list of domains for "client/html/catalog/product/domains", e.g.

```
 client/html/catalog/product/domains = ['attribute', 'media', 'price', 'product', 'text']
```

See also:

* client/html/catalog/home/basket-add
* client/html/catalog/lists/basket-add
* client/html/catalog/detail/basket-add
* client/html/basket/related/basket-add

# cache

Enables or disables caching only for the catalog product component

```
client/html/catalog/product/cache = 1
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

# domains

A list of domain names whose items should be available in the catalog product view template

```
client/html/catalog/product/domains = Array
(
    [0] => catalog
    [1] => media
    [2] => media/property
    [3] => price
    [4] => supplier
    [5] => text
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
)

* Type: array - List of domain names
* Since: 2019.06

The templates rendering product lists usually add the images, prices
and texts associated to each product item. If you want to display additional
content like the product attributes, you can configure your own list of
domains (attribute, media, price, product, text, etc. are domains)
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

# name

Class name of the used catalog product client implementation

```
client/html/catalog/product/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2019.06

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Catalog\Product\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Product\Myproduct
```

then you have to set the this configuration option:

```
 client/html/catalog/product/name = Myproduct
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyProduct"!


# product-codes

List of codes of products to load for the current list.
Should be set dynamically through some integration plugin,
to allow a list of products with configurable products.

```
client/html/catalog/product/product-codes = Array
(
    [0] => CNE
    [1] => ABCD
    [2] => CNC
)
```

* Default: Array
(
)

* Type: string - List of codes of products to load for the current list
* Since: 2019.06


# stock
## enable

Enables or disables displaying product stock levels in product list views

```
client/html/catalog/product/stock/enable = 1
```

* Default: 1
* Type: boolean - Value of "1" to display stock levels, "0" to disable displaying them
* Since: 2019.06

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

Relative path to the HTML body template of the catalog product client.

```
client/html/catalog/product/template-body = catalog/product/body
```

* Default: catalog/product/body
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2019.06

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

* client/html/catalog/product/template-header

# template-header

Relative path to the HTML header template of the catalog product client.

```
client/html/catalog/product/template-header = catalog/product/header
```

* Default: catalog/product/header
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2019.06

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

* client/html/catalog/product/template-body