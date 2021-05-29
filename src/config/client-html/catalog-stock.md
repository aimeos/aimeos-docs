
# decorators
## excludes

Excludes decorators added by the "common" option from the catalog stock html client

```
client/html/catalog/stock/decorators/excludes = Array
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
 client/html/catalog/stock/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/stock/decorators/global
* client/html/catalog/stock/decorators/local

## global

Adds a list of globally available decorators only to the catalog stock html client

```
client/html/catalog/stock/decorators/global = Array
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
 client/html/catalog/stock/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/stock/decorators/excludes
* client/html/catalog/stock/decorators/local

## local

Adds a list of local decorators only to the catalog stock html client

```
client/html/catalog/stock/decorators/local = Array
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
 client/html/catalog/stock/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/stock/decorators/excludes
* client/html/catalog/stock/decorators/global

# level
## low

The number of products in stock below it's considered a low stock level

```
client/html/catalog/stock/level/low = 5
```

* Default: 5
* Type: integer - Number of products in stock
* Since: 2014.03

There are four stock levels available:

* unlimited
* high
* low
* out

If no stock information is available, the number of products is considered
unlimited, which is useful for digital products. Zero or less products in
stock means out of stock while a quantity of products above the option value
represents a high stock value.

There can be the case that a stock level is sometimes negative even if only
products that are in stock can be bought. This is due to the time difference
the product is actually ordered and the stock level is decreased. If you've
configured the stock level update every minute, within this minute another
customer can buy the same product that is considered to be still in stock at
this time.

See also:

* client/html/catalog/stock/sort

# name

Class name of the used catalog stock client implementation

```
client/html/catalog/stock/name = Standard
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
 \Aimeos\Client\Html\Catalog\Stock\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Stock\Mystock
```

then you have to set the this configuration option:

```
 client/html/catalog/stock/name = Mystock
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyStock"!


# sort

Sortation key if stock levels for different types exist

```
client/html/catalog/stock/sort = stock.type
```

* Default: stock.type
* Type: array - List of key/value pairs for sorting
* Since: 2017.01

Products can be shipped from several warehouses with a different
stock level for each one. The stock levels for each warehouse will
be shown in the product detail page. To get a consistent sortation
of this list, the configured key will be used by the stock manager.

Possible keys for sorting are ("-stock.type" for descending order):

* stock.productid
* stock.stocklevel
* stock.type
* stock.dateback

See also:

* client/html/catalog/stock/level/low

# subparts

List of HTML sub-clients rendered within the catalog stock section

```
client/html/catalog/stock/subparts = Array
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


# template-body

Relative path to the HTML body template of the catalog stock client.

```
client/html/catalog/stock/template-body = catalog/stock/body-standard
```

* Default: catalog/stock/body-standard
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

* client/html/catalog/stock/template-header

# template-header

Relative path to the HTML header template of the catalog stock client.

```
client/html/catalog/stock/template-header = catalog/stock/header-standard
```

* Default: catalog/stock/header-standard
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

* client/html/catalog/stock/template-body

# url
## action

Name of the action that should create the output

```
client/html/catalog/stock/url/action = stock
```

* Default: stock
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/catalog/stock/url/target
* client/html/catalog/stock/url/controller
* client/html/catalog/stock/url/config
* client/html/catalog/stock/url/max-items

## config

Associative list of configuration options used for generating the URL

```
client/html/catalog/stock/url/config = Array
(
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

* client/html/catalog/stock/url/target
* client/html/catalog/stock/url/controller
* client/html/catalog/stock/url/action
* client/html/catalog/stock/url/max-items

## controller

Name of the controller whose action should be called

```
client/html/catalog/stock/url/controller = catalog
```

* Default: catalog
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/catalog/stock/url/target
* client/html/catalog/stock/url/action
* client/html/catalog/stock/url/config
* client/html/catalog/stock/url/max-items

## max-items

Maximum number of product stock levels per request

```
client/html/catalog/stock/url/max-items = 100
```

* Default: 100
* Type: integer - Maximum number of product codes per request
* Since: 2018.10

To avoid URLs that exceed the maximum amount of characters (usually 8190),
each request contains only up to the configured amount of product codes.
If more product codes are available, several requests will be sent to the
server.

See also:

* client/html/catalog/stock/url/target
* client/html/catalog/stock/url/controller
* client/html/catalog/stock/url/action
* client/html/catalog/stock/url/config

## target

Destination of the URL where the controller specified in the URL is known

```
client/html/catalog/stock/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/catalog/stock/url/controller
* client/html/catalog/stock/url/action
* client/html/catalog/stock/url/config
* client/html/catalog/stock/url/max-items