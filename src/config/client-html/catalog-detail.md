
# basket-add

Display the "add to basket" button for each suggested/bought-together product item

```
client/html/catalog/detail/basket-add = 
```

* Default: 
* Type: boolean - True to display the button, false to hide it
* Since: 2021.04

Enables the button for adding products to the basket for the related products
in the basket. This works for all type of products, even for selection products
with product variants and product bundles. By default, also optional attributes
are displayed if they have been associated to a product.

To fetch the variant articles of selection products too, add this setting to
your configuration:

mshop/common/manager/maxdepth = 3

See also:

* client/html/catalog/home/basket-add
* client/html/catalog/lists/basket-add
* client/html/catalog/product/basket-add
* client/html/basket/related/basket-add

# cache

Enables or disables caching only for the catalog detail component

```
client/html/catalog/detail/cache = 1
```

* Default: 1
* Type: boolean - True to enable caching, false to disable

Disable caching for components can be useful if you would have too much
entries to cache or if the component contains non-cacheable parts that
can't be replaced using the modify() method.

See also:

* client/html/catalog/filter/cache
* client/html/catalog/lists/cache
* client/html/catalog/stage/cache

# domains

A list of domain names whose items should be available in the product detail view template

```
client/html/catalog/detail/domains = Array
(
    [0] => attribute
    [1] => attribute/property
    [2] => catalog
    [3] => media
    [4] => media/property
    [5] => price
    [6] => product
    [7] => product/property
    [8] => supplier
    [9] => supplier/address
    [10] => text
    [11] => stock
)
```

* Default: Array
(
    [0] => attribute
    [1] => attribute/property
    [2] => catalog
    [3] => media
    [4] => media/property
    [5] => price
    [6] => product
    [7] => product/property
    [8] => supplier
    [9] => supplier/address
    [10] => text
    [11] => stock
)

* Type: array - List of domain names
* Since: 2014.03

The templates rendering product details usually add the images,
prices, texts, attributes, products, etc. associated to the product
item. If you want to display additional or less content, you can
configure your own list of domains (attribute, media, price, product,
text, etc. are domains) whose items are fetched from the storage.
Please keep in mind that the more domains you add to the configuration,
the more time is required for fetching the content!

Since version 2014.05 this configuration option overwrites the
"client/html/catalog/domains" option that allows to configure the
domain names of the items fetched for all catalog related data.

See also:

* client/html/catalog/domains
* client/html/catalog/lists/domains

# metatags

Adds the title, meta and link tags to the HTML header

```
client/html/catalog/detail/metatags = 1
```

* Default: 1
* Type: boolean - True to display the meta tags, false to hide it
* Since: 2017.01

By default, each instance of the catalog list component adds some HTML meta
tags to the page head section, like page title, meta keywords and description
as well as some link tags to support browser navigation. If several instances
are placed on one page, this leads to adding several title and meta tags used
by search engine. This setting enables you to suppress these tags in the page
header and maybe add your own to the page manually.

See also:

* client/html/catalog/lists/metatags

# name

Class name of the used catalog detail client implementation

```
client/html/catalog/detail/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2014.03

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Catalog\Detail\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Detail\Mydetail
```

then you have to set the this configuration option:

```
 client/html/catalog/detail/name = Mydetail
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyDetail"!


# partials
## group

Relative path to the group product partial template file

```
client/html/catalog/detail/partials/group = 
```

* Default: 
* Type: string - Relative path to the template file
* Since: 2021.07

Partials are templates which are reused in other templates and generate
reoccuring blocks filled with data from the assigned values. The group
partial creates an HTML block for a list of sub-products assigned to a
group product a customer can select from.

See also:

* client/html/common/partials/attribute

## image

Relative path to the detail image partial template file

```
client/html/catalog/detail/partials/image = catalog/detail/image
```

* Default: catalog/detail/image
* Type: string - Relative path to the template file
* Since: 2017.01

Partials are templates which are reused in other templates and generate
reoccuring blocks filled with data from the assigned values. The image
partial creates an HTML block for the catalog detail images.


## seen

Relative path to the HTML template of the catalog detail seen partial.

```
client/html/catalog/detail/partials/seen = catalog/detail/seen
```

* Default: catalog/detail/seen
* Type: string - Relative path to the template creating the HTML fragment
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


# prodcode-default

The default product code used if none is given as parameter

```
client/html/catalog/detail/prodcode-default = 
```

* Default: 
* Type: string - Product code
* Since: 2019.10

To display a product detail view or a part of it for a specific
product, you can configure its code using this setting. This is
most useful in a CMS where the product code can be configured
separately for each content node.

See also:

* client/html/catalog/detail/prodid-default
* client/html/catalog/lists/catid-default

# prodid-default

The default product ID used if none is given as parameter

```
client/html/catalog/detail/prodid-default = 
```

* Default: 
* Type: string - Product ID
* Since: 2016.01

To display a product detail view or a part of it for a specific
product, you can configure its ID using this setting. This is
most useful in a CMS where the product ID can be configured
separately for each content node.

See also:

* client/html/catalog/detail/prodid-default
* client/html/catalog/lists/catid-default

# stock
## enable

Enables or disables displaying product stock levels in product detail view

```
client/html/catalog/detail/stock/enable = 1
```

* Default: 1
* Type: boolean - Value of "1" to display stock levels, "0" to disable displaying them
* Since: 2014.03

This configuration option allows shop owners to display product
stock levels for each product in the detail views or to disable
fetching product stock information.

The stock information is fetched via AJAX and inserted via Javascript.
This allows to cache product items by leaving out such highly
dynamic content like stock levels which changes with each order.

See also:

* client/html/catalog/lists/stock/enable
* client/html/catalog/stock/url/target
* client/html/catalog/stock/url/controller
* client/html/catalog/stock/url/action
* client/html/catalog/stock/url/config

# template-body

Relative path to the HTML body template of the catalog detail client.

```
client/html/catalog/detail/template-body = catalog/detail/body
```

* Default: catalog/detail/body
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

* client/html/catalog/detail/template-header
* client/html/catalog/detail/404

# template-header

Relative path to the HTML header template of the catalog detail client.

```
client/html/catalog/detail/template-header = catalog/detail/header
```

* Default: catalog/detail/header
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

* client/html/catalog/detail/template-body
* client/html/catalog/detail/404

# template-navigator

Relative path to the HTML template of the catalog detail navigator partial.

```
client/html/catalog/detail/template-navigator = catalog/detail/navigator
```

* Default: catalog/detail/navigator
* Type: string - Relative path to the template creating the HTML fragment
* Since: 2022.10

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


# url
## action

Name of the action that should create the output

```
client/html/catalog/detail/url/action = detail
```

* Default: detail
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/catalog/detail/url/target
* client/html/catalog/detail/url/controller
* client/html/catalog/detail/url/config
* client/html/catalog/detail/url/filter

## config

Associative list of configuration options used for generating the URL

```
client/html/catalog/detail/url/config = Array
(
    [absoluteUri] => 1
)
```

* Default: Array
(
    [absoluteUri] => 1
)

* Type: string - Associative list of configuration options
* Since: 2014.03

You can specify additional options as key/value pairs used when generating
the URLs, like

```
 client/html/<clientname>/url/config = array( 'absoluteUri' => true )
```

The available key/value pairs depend on the application that embeds the e-commerce
framework. This is because the infrastructure of the application is used for
generating the URLs. The full list of available config options is referenced
in the "see also" section of this page.

See also:

* client/html/catalog/detail/url/target
* client/html/catalog/detail/url/controller
* client/html/catalog/detail/url/action
* client/html/catalog/detail/url/filter
* client/html/url/config

## controller

Name of the controller whose action should be called

```
client/html/catalog/detail/url/controller = catalog
```

* Default: catalog
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/catalog/detail/url/target
* client/html/catalog/detail/url/action
* client/html/catalog/detail/url/config
* client/html/catalog/detail/url/filter

## filter

Removes parameters for the detail page before generating the URL

```
client/html/catalog/detail/url/filter = Array
(
    [0] => d_prodid
)
```

* Default: Array
(
)

* Type: array - List of parameter names to remove
* Since: 2019.04

For SEO, it's nice to have product URLs which contains the product names only.
Usually, product names are unique so exactly one product is found when resolving
the product by its name. If two or more products share the same name, it's not
possible to refer to the correct product and in this case, the product ID is
required as unique identifier.

This setting removes the listed parameters from the URLs of the detail pages.

See also:

* client/html/catalog/detail/url/target
* client/html/catalog/detail/url/controller
* client/html/catalog/detail/url/action
* client/html/catalog/detail/url/config

## target

Destination of the URL where the controller specified in the URL is known

```
client/html/catalog/detail/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/catalog/detail/url/controller
* client/html/catalog/detail/url/action
* client/html/catalog/detail/url/config
* client/html/catalog/detail/url/filter