
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

```
client/html/basket/standard/decorators/excludes = Array
(
)
```

* Default: Array
(
)



## global

```
client/html/basket/standard/decorators/global = Array
(
)
```

* Default: Array
(
)



## local

```
client/html/basket/standard/decorators/local = Array
(
)
```

* Default: Array
(
)



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


# summary
## detail

Location of the detail partial template for the basket standard component

```
client/html/basket/standard/summary/detail = common/summary/detail
```

* Default: common/summary/detail
* Type: string - Relative path to the detail partial
* Since: 2017.01

To configure an alternative template for the detail partial, you
have to configure its path relative to the template directory
(usually templates/client/html/). It's then used to display the
product detail block in the basket standard component.


# url
## action

Name of the action that should create the output

```
client/html/basket/standard/url/action = standard
```

* Default: standard
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/basket/standard/url/target
* client/html/basket/standard/url/controller
* client/html/basket/standard/url/config

## config

Associative list of configuration options used for generating the URL

```
client/html/basket/standard/url/config = Array
(
)
```

* Default: Array
(
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

* client/html/basket/standard/url/target
* client/html/basket/standard/url/controller
* client/html/basket/standard/url/action
* client/html/url/config

## controller

Name of the controller whose action should be called

```
client/html/basket/standard/url/controller = Basket
```

* Default: Basket
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/basket/standard/url/target
* client/html/basket/standard/url/action
* client/html/basket/standard/url/config

## filter

```
client/html/basket/standard/url/filter = Array
(
)
```

* Default: Array
(
)



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