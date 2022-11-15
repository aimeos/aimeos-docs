
# basket-add

Display the "add to basket" button for each product item

```
client/html/basket/related/basket-add =
```

* Default:
* Type: boolean - True to display the button, false to hide it
* Since: 2020.10

Enables the button for adding products to the basket for the related products
in the basket. This works for all type of products, even for selection products
with product variants and product bundles. By default, also optional attributes
are displayed if they have been associated to a product.

See also:

* client/html/catalog/home/basket-add
* client/html/catalog/lists/basket-add
* client/html/catalog/detail/basket-add
* client/html/catalog/product/basket-add

# bought
## domains

The list of domain names whose items should be available in the template for the products

```
client/html/basket/related/bought/domains = Array
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
* Since: 2014.09

The templates rendering product details usually add the images,
prices and texts, etc. associated to the product
item. If you want to display additional or less content, you can
configure your own list of domains (attribute, media, price, product,
text, etc. are domains) whose items are fetched from the storage.
Please keep in mind that the more domains you add to the configuration,
the more time is required for fetching the content!


## limit

Number of items in the list of bought together products

```
client/html/basket/related/bought/limit = 6
```

* Default: 6
* Type: integer - Number of products
* Since: 2014.09

This option limits the number of suggested products in the
list of bought together products. The suggested items are
calculated using the products that are in the current basket
of the customer.

Note: You need to start the job controller for calculating
the bought together products regularly to get up to date
product suggestions.


# decorators
## excludes

```
client/html/basket/related/decorators/excludes = Array
(
)
```

* Default: Array
(
)



## global

```
client/html/basket/related/decorators/global = Array
(
)
```

* Default: Array
(
)



## local

```
client/html/basket/related/decorators/local = Array
(
)
```

* Default: Array
(
)



# name

Class name of the used basket related client implementation

```
client/html/basket/related/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Basket\Related\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Basket\Related\Mybasket
```

then you have to set the this configuration option:

```
 client/html/basket/related/name = Mybasket
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyBasket"!


# template-body

Relative path to the HTML body template of the basket related client.

```
client/html/basket/related/template-body =
```

* Default:
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

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

* client/html/basket/related/template-header

# template-header

Relative path to the HTML header template of the basket related client.

```
client/html/basket/related/template-header =
```

* Default:
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2014.03

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

* client/html/basket/related/template-body