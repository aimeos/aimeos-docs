
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
can't be replaced using the modifyBody() and modifyHeader() methods.

See also:

* client/html/catalog/filter/cache
* client/html/catalog/lists/cache
* client/html/catalog/stage/cache

# decorators
## excludes

Excludes decorators added by the "common" option from the catalog detail html client

```
client/html/catalog/detail/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/catalog/detail/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/detail/decorators/global
* client/html/catalog/detail/decorators/local

## global

Adds a list of globally available decorators only to the catalog detail html client

```
client/html/catalog/detail/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/catalog/detail/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/detail/decorators/excludes
* client/html/catalog/detail/decorators/local

## local

Adds a list of local decorators only to the catalog detail html client

```
client/html/catalog/detail/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Catalog\Decorator\*") around the html client.

```
 client/html/catalog/detail/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/detail/decorators/excludes
* client/html/catalog/detail/decorators/global

# domains

A list of domain names whose items should be available in the product detail view template

```
client/html/catalog/detail/domains = Array
(
    [0] => attribute
    [1] => media
    [2] => media/property
    [3] => price
    [4] => product
    [5] => product/property
    [6] => text
    [supplier] => Array
        (
            [0] => text
            [1] => media
            [2] => supplier/address
        )

)
```

* Default: Array
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
client/html/catalog/detail/name = Standard
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
## image

Relative path to the detail image partial template file

```
client/html/catalog/detail/partials/image = catalog/detail/image-partial-standard
```

* Default: catalog/detail/image-partial-standard
* Type: string - Relative path to the template file
* Since: 2017.01

Partials are templates which are reused in other templates and generate
reoccuring blocks filled with data from the assigned values. The image
partial creates an HTML block for the catalog detail images.


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

# seen
## decorators/excludes

Excludes decorators added by the "common" option from the catalog detail seen html client

```
client/html/catalog/detail/seen/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/catalog/detail/seen/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/detail/seen/decorators/global
* client/html/catalog/detail/seen/decorators/local

## decorators/global

Adds a list of globally available decorators only to the catalog detail seen html client

```
client/html/catalog/detail/seen/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/catalog/detail/seen/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/detail/seen/decorators/excludes
* client/html/catalog/detail/seen/decorators/local

## decorators/local

Adds a list of local decorators only to the catalog detail seen html client

```
client/html/catalog/detail/seen/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Catalog\Decorator\*") around the html client.

```
 client/html/catalog/detail/seen/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/detail/seen/decorators/excludes
* client/html/catalog/detail/seen/decorators/global

## domains

A list of domain names whose items should be available in the last seen view template for the product

```
client/html/catalog/detail/seen/domains = Array
(
    [0] => media
    [1] => price
    [2] => text
)
```

* Default: Array
* Type: array - List of domain names
* Since: 2014.07

The templates rendering product details usually add the images,
prices and texts, etc. associated to the product
item. If you want to display additional or less content, you can
configure your own list of domains (attribute, media, price, product,
text, etc. are domains) whose items are fetched from the storage.
Please keep in mind that the more domains you add to the configuration,
the more time is required for fetching the content!

See also:

* client/html/catalog/domains
* client/html/catalog/lists/domains
* client/html/catalog/detail/domains

## name

Name of the seen part used by the catalog detail client implementation

```
client/html/catalog/detail/seen/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Detail\Seen\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## subparts

List of HTML sub-clients rendered within the catalog detail seen section

```
client/html/catalog/detail/seen/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2014.03

The output of the frontend is composed of the code generated by the HTML
clients. Each HTML client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain HTML clients themselves and therefore a
hierarchical tree of HTML clients is composed. Each HTML client creates
the output that is placed inside the container of its parent.

At first, always the HTML code generated by the parent is printed, then
the HTML code of its sub-clients. The order of the HTML sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 client/html/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 client/html/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural HTML, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## template-body

Relative path to the HTML body template of the catalog detail seen client.

```
client/html/catalog/detail/seen/template-body = catalog/detail/seen-partial-standard
```

* Default: catalog/detail/seen-partial-standard
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* client/html/catalog/detail/seen/template-header

# service
## decorators/excludes

Excludes decorators added by the "common" option from the catalog detail service html client

```
client/html/catalog/detail/service/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2016.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/catalog/detail/service/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/detail/service/decorators/global
* client/html/catalog/detail/service/decorators/local

## decorators/global

Adds a list of globally available decorators only to the catalog detail service html client

```
client/html/catalog/detail/service/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2016.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/catalog/detail/service/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/detail/service/decorators/excludes
* client/html/catalog/detail/service/decorators/local

## decorators/local

Adds a list of local decorators only to the catalog detail service html client

```
client/html/catalog/detail/service/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2016.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Catalog\Decorator\*") around the html client.

```
 client/html/catalog/detail/service/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/detail/service/decorators/excludes
* client/html/catalog/detail/service/service/decorators/global

## domains

A list of domain names whose items should be available for the services
in the services part of the catalog detail view templates

```
client/html/catalog/detail/service/domains = Array
(
    [0] => text
    [1] => price
)
```

* Default: Array
* Type: array - List of domain names
* Since: 2016.05

Usually, service prices and texts are available in the templates
rendering services related data. If you want to
display additional content like the attributes, you can configure
your own list of domains (attribute, media, price, text,
etc. are domains) whose items are fetched from the storage.

See also:

* client/html/catalog/detail/service/types

## name

Name of the shipping cost part used by the catalog detail client implementation

```
client/html/catalog/detail/service/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2017.01

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Detail\Service\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## subparts

List of HTML sub-clients rendered within the catalog detail service section

```
client/html/catalog/detail/service/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2016.05

The output of the frontend is composed of the code generated by the HTML
clients. Each HTML client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain HTML clients themselves and therefore a
hierarchical tree of HTML clients is composed. Each HTML client creates
the output that is placed inside the container of its parent.

At first, always the HTML code generated by the parent is printed, then
the HTML code of its sub-clients. The order of the HTML sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 client/html/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 client/html/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural HTML, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## template-body

Relative path to the HTML body template of the catalog detail service client.

```
client/html/catalog/detail/service/template-body = catalog/detail/service-body-standard
```

* Default: catalog/detail/service-body-standard
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2016.05

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* client/html/catalog/detail/service/template-header

## types

The service types available in the service template

```
client/html/catalog/detail/service/types = Array
(
    [0] => delivery
)
```

* Default: Array
* Type: array - List of type codes
* Since: 2016.05

By default, only delivery services will be available in the
template but you can extend the list to payment services too.

See also:

* client/html/catalog/detail/service/domains

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

# subparts

List of HTML sub-clients rendered within the catalog detail section

```
client/html/catalog/detail/subparts = Array
(
    [0] => seen
    [1] => service
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2014.03

The output of the frontend is composed of the code generated by the HTML
clients. Each HTML client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain HTML clients themselves and therefore a
hierarchical tree of HTML clients is composed. Each HTML client creates
the output that is placed inside the container of its parent.

At first, always the HTML code generated by the parent is printed, then
the HTML code of its sub-clients. The order of the HTML sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 client/html/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 client/html/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural HTML, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


# supplier
## name

Name of the supplier part used by the catalog detail client implementation

```
client/html/catalog/detail/supplier/name = 
```

* Default: 
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Detail\Supplier\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


# template-body

Relative path to the HTML body template of the catalog detail client.

```
client/html/catalog/detail/template-body = catalog/detail/body-standard
```

* Default: catalog/detail/body-standard
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* client/html/catalog/detail/template-header

# template-header

Relative path to the HTML header template of the catalog detail client.

```
client/html/catalog/detail/template-header = catalog/detail/header-standard
```

* Default: catalog/detail/header-standard
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the HTML code that is inserted into the HTML page header
of the rendered page in the frontend. The configuration string is the
path to the template file relative to the templates directory (usually
in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "standard" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "standard"
should be replaced by the name of the new class.

See also:

* client/html/catalog/detail/template-body

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