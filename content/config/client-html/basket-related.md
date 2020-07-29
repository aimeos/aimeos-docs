
# basket-add

```
client/html/basket/related/basket-add = 
```

* Default: 


# bought
## decorators/excludes

Excludes decorators added by the "common" option from the basket related bought html client

```
client/html/basket/related/bought/decorators/excludes = 
```

* Default: 
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
 client/html/basket/related/bought/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/basket/related/bought/decorators/global
* client/html/basket/related/bought/decorators/local

## decorators/global

Adds a list of globally available decorators only to the basket related bought html client

```
client/html/basket/related/bought/decorators/global = Array
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
 client/html/basket/related/bought/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/basket/related/bought/decorators/excludes
* client/html/basket/related/bought/decorators/local

## decorators/local

Adds a list of local decorators only to the basket related bought html client

```
client/html/basket/related/bought/decorators/local = Array
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
("\Aimeos\Client\Html\Basket\Decorator\*") around the html client.

```
 client/html/basket/related/bought/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Basket\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/basket/related/bought/decorators/excludes
* client/html/basket/related/bought/decorators/global

## name

Name of the bought together part used by the basket related client implementation

```
client/html/basket/related/bought/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.09

Use "Myname" if your class is named "\Aimeos\Client\Html\Basket\Related\Bought\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## standard/domains

The list of domain names whose items should be available in the template for the products

```
client/html/basket/related/bought/standard/domains = Array
(
    [0] => text
    [1] => price
    [2] => media
)
```

* Default: Array
* Type: array - List of domain names
* Since: 2014.09

The templates rendering product details usually add the images,
prices and texts, etc. associated to the product
item. If you want to display additional or less content, you can
configure your own list of domains (attribute, media, price, product,
text, etc. are domains) whose items are fetched from the storage.
Please keep in mind that the more domains you add to the configuration,
the more time is required for fetching the content!


## standard/limit

Number of items in the list of bought together products

```
client/html/basket/related/bought/standard/limit = 6
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


## standard/subparts

List of HTML sub-clients rendered within the basket related bought section

```
client/html/basket/related/bought/standard/subparts = Array
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


## standard/template-body

Relative path to the HTML body template of the basket related bought client.

```
client/html/basket/related/bought/standard/template-body = basket/related/bought-body-standard
```

* Default: basket/related/bought-body-standard
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

* client/html/basket/related/bought/standard/template-header

# decorators
## excludes

Excludes decorators added by the "common" option from the basket related html client

```
client/html/basket/related/decorators/excludes = Array
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
 client/html/basket/related/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/basket/related/decorators/global
* client/html/basket/related/decorators/local

## global

Adds a list of globally available decorators only to the basket related html client

```
client/html/basket/related/decorators/global = Array
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
 client/html/basket/related/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/basket/related/decorators/excludes
* client/html/basket/related/decorators/local

## local

Adds a list of local decorators only to the basket related html client

```
client/html/basket/related/decorators/local = Array
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
("\Aimeos\Client\Html\Basket\Decorator\*") around the html client.

```
 client/html/basket/related/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Basket\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/basket/related/decorators/excludes
* client/html/basket/related/decorators/global

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


# standard
## subparts

List of HTML sub-clients rendered within the basket related section

```
client/html/basket/related/standard/subparts = Array
(
    [0] => bought
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

Relative path to the HTML body template of the basket related client.

```
client/html/basket/related/standard/template-body = basket/related/body-standard
```

* Default: basket/related/body-standard
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

* client/html/basket/related/standard/template-header

## template-header

Relative path to the HTML header template of the basket related client.

```
client/html/basket/related/standard/template-header = basket/related/header-standard
```

* Default: basket/related/header-standard
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

* client/html/basket/related/standard/template-body