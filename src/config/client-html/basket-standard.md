
# check

Alters the behavior of the product checks before continuing with the checkout

```
client/html/basket/standard/check = 1
```

* Default: 1
* Type: integer - One of the allowed values (0, 1 or 2)
* Since: 2016.08

By default, the product related checks are performed every time the basket
is shown. They test if there are any products in the basket and execute all
basket plugins that have been registered for the "check.before" and "check.after"
events.

Using this configuration setting, you can either disable all checks completely
(0) or display a "Check" button instead of the "Checkout" button (2). In the
later case, customers have to click on the "Check" button first to perform
the checks and if everything is OK, the "Checkout" button will be displayed
that allows the customers to continue the checkout process. If one of the
checks fails, the customers have to fix the related basket item and must click
on the "Check" button again before they can continue.

Available values are:
```
 0 = no product related checks
 1 = checks are performed every time when the basket is displayed
 2 = checks are performed only when clicking on the "check" button
```


# coupon
## overwrite

Replace previous coupon codes each time the user enters a new one

```
client/html/basket/standard/coupon/overwrite = 1
```

* Default: 
* Type: boolean - True to overwrite a previous coupon, false to keep them
* Since: 2020.04

If you want to allow only one coupon code per order and replace a
previously entered one automatically, this configuration option
should be set to true.


# decorators
## excludes

Excludes decorators added by the "common" option from the basket standard html client

```
client/html/basket/standard/decorators/excludes = Array
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
 client/html/basket/standard/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/basket/standard/decorators/global
* client/html/basket/standard/decorators/local

## global

Adds a list of globally available decorators only to the basket standard html client

```
client/html/basket/standard/decorators/global = Array
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
 client/html/basket/standard/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/basket/standard/decorators/excludes
* client/html/basket/standard/decorators/local

## local

Adds a list of local decorators only to the basket standard html client

```
client/html/basket/standard/decorators/local = Array
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
 client/html/basket/standard/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Basket\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/basket/standard/decorators/excludes
* client/html/basket/standard/decorators/global

# name

Class name of the used basket standard client implementation

```
client/html/basket/standard/name = Standard
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
 \Aimeos\Client\Html\Basket\Standard\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Basket\Standard\Mybasket
```

then you have to set the this configuration option:

```
 client/html/basket/standard/name = Mybasket
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

List of HTML sub-clients rendered within the basket standard section

```
client/html/basket/standard/standard/subparts = Array
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

Relative path to the HTML body template of the basket standard client.

```
client/html/basket/standard/standard/template-body = basket/standard/body-standard
```

* Default: basket/standard/body-standard
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

* client/html/basket/standard/standard/template-header

## template-header

Relative path to the HTML header template of the basket standard client.

```
client/html/basket/standard/standard/template-header = basket/standard/header-standard
```

* Default: basket/standard/header-standard
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

* client/html/basket/standard/standard/template-body

# summary
## detail

Location of the detail partial template for the basket standard component

```
client/html/basket/standard/summary/detail = common/summary/detail-standard
```

* Default: common/summary/detail-standard
* Type: string - Relative path to the detail partial
* Since: 2017.01

To configure an alternative template for the detail partial, you
have to configure its path relative to the template directory
(usually client/html/templates/). It's then used to display the
product detail block in the basket standard component.


# url
## action

Name of the action that should create the output

```
client/html/basket/standard/url/action = index
```

* Default: index
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/basket/standard/url/target
* client/html/basket/standard/url/controller
* client/html/basket/standard/url/config
* client/html/basket/standard/url/site

## config

Associative list of configuration options used for generating the URL

```
client/html/basket/standard/url/config = Array
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

* client/html/basket/standard/url/target
* client/html/basket/standard/url/controller
* client/html/basket/standard/url/action
* client/html/basket/standard/url/site
* client/html/url/config

## controller

Name of the controller whose action should be called

```
client/html/basket/standard/url/controller = basket
```

* Default: basket
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/basket/standard/url/target
* client/html/basket/standard/url/action
* client/html/basket/standard/url/config
* client/html/basket/standard/url/site

## site

Locale site code where products will be added to the basket

```
client/html/basket/standard/url/site = 
```

* Default: 
* Type: string - Code of the locale site
* Since: 2018.04

In more complex setups with several shop sites, this setting allows to to
define the shop site that will manage the basket of the customer. For example
in market place setups where all vendors have there own shop sites, the basket
site should be the site code of the market place ("default" by default).

See also:

* client/html/basket/standard/url/target
* client/html/basket/standard/url/controller
* client/html/basket/standard/url/config

## target

Destination of the URL where the controller specified in the URL is known

```
client/html/basket/standard/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/basket/standard/url/controller
* client/html/basket/standard/url/action
* client/html/basket/standard/url/config
* client/html/basket/standard/url/site