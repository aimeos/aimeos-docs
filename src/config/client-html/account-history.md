
# decorators
## excludes

Excludes decorators added by the "common" option from the account history html client

```
client/html/account/history/decorators/excludes = Array
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
 client/html/account/history/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/account/history/decorators/global
* client/html/account/history/decorators/local

## global

Adds a list of globally available decorators only to the account history html client

```
client/html/account/history/decorators/global = Array
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
 client/html/account/history/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/account/history/decorators/excludes
* client/html/account/history/decorators/local

## local

Adds a list of local decorators only to the account history html client

```
client/html/account/history/decorators/local = Array
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
("\Aimeos\Client\Html\Account\Decorator\*") around the html client.

```
 client/html/account/history/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Account\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/account/history/decorators/excludes
* client/html/account/history/decorators/global

# lists
## decorators/excludes

Excludes decorators added by the "common" option from the account history list html client

```
client/html/account/history/lists/decorators/excludes = 
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
 client/html/account/history/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/account/history/lists/decorators/global
* client/html/account/history/lists/decorators/local

## decorators/global

Adds a list of globally available decorators only to the account history list html client

```
client/html/account/history/lists/decorators/global = Array
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
 client/html/account/history/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/account/history/lists/decorators/excludes
* client/html/account/history/lists/decorators/local

## decorators/local

Adds a list of local decorators only to the account history list html client

```
client/html/account/history/lists/decorators/local = Array
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
("\Aimeos\Client\Html\Account\Decorator\*") around the html client.

```
 client/html/account/history/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Account\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/account/history/lists/decorators/excludes
* client/html/account/history/lists/decorators/global

## name

Name of the list part used by the account history client implementation

```
client/html/account/history/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Account\History\Lists\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## standard/subparts

List of HTML sub-clients rendered within the account history list section

```
client/html/account/history/lists/standard/subparts = Array
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

Relative path to the HTML body template of the account history list client.

```
client/html/account/history/lists/standard/template-body = account/history/list-body-standard
```

* Default: account/history/list-body-standard
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

* client/html/account/history/lists/standard/template-header

# name

Class name of the used account history client implementation

```
client/html/account/history/name = Standard
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
 \Aimeos\Client\Html\Account\History\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Account\History\Myhistory
```

then you have to set the this configuration option:

```
 client/html/account/history/name = Myhistory
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyHistory"!


# order
## decorators/excludes

Excludes decorators added by the "common" option from the account history order html client

```
client/html/account/history/order/decorators/excludes = 
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
 client/html/account/history/order/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/account/history/order/decorators/global
* client/html/account/history/order/decorators/local

## decorators/global

Adds a list of globally available decorators only to the account history order html client

```
client/html/account/history/order/decorators/global = Array
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
 client/html/account/history/order/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/account/history/order/decorators/excludes
* client/html/account/history/order/decorators/local

## decorators/local

Adds a list of local decorators only to the account history order html client

```
client/html/account/history/order/decorators/local = Array
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
("\Aimeos\Client\Html\Account\Decorator\*") around the html client.

```
 client/html/account/history/order/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Account\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/account/history/order/decorators/excludes
* client/html/account/history/order/decorators/global

## name

Name of the order part used by the account history client implementation

```
client/html/account/history/order/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2015.02

Use "Myname" if your class is named "\Aimeos\Client\Html\Account\History\Order\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## standard/subparts

List of HTML sub-clients rendered within the account history order section

```
client/html/account/history/order/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2015.02

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

Relative path to the HTML body template of the account history order client.

```
client/html/account/history/order/standard/template-body = account/history/order-body-standard
```

* Default: account/history/order-body-standard
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2015.02

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

* client/html/account/history/order/standard/template-header

# standard
## subparts

List of HTML sub-clients rendered within the account history section

```
client/html/account/history/standard/subparts = Array
(
    [0] => lists
    [1] => order
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

Relative path to the HTML body template of the account history client.

```
client/html/account/history/standard/template-body = account/history/body-standard
```

* Default: account/history/body-standard
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

* client/html/account/history/standard/template-header

## template-header

Relative path to the HTML header template of the account history client.

```
client/html/account/history/standard/template-header = account/history/header-standard
```

* Default: account/history/header-standard
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

* client/html/account/history/standard/template-body

# summary
## address

Location of the address partial template for the account history component

```
client/html/account/history/summary/address = common/summary/address-standard
```

* Default: common/summary/address-standard
* Type: string - Relative path to the address partial
* Since: 2017.01

To configure an alternative template for the address partial, you
have to configure its path relative to the template directory
(usually client/html/templates/). It's then used to display the
payment or delivery address block in the account history component.

See also:

* client/html/account/history/summary/detail
* client/html/account/history/summary/service

## detail

Location of the detail partial template for the account history component

```
client/html/account/history/summary/detail = common/summary/detail-standard
```

* Default: common/summary/detail-standard
* Type: string - Relative path to the detail partial
* Since: 2017.01

To configure an alternative template for the detail partial, you
have to configure its path relative to the template directory
(usually client/html/templates/). It's then used to display the
product detail block in the account history component.

See also:

* client/html/account/history/summary/address
* client/html/account/history/summary/service

## service

Location of the service partial template for the account history component

```
client/html/account/history/summary/service = common/summary/service-standard
```

* Default: common/summary/service-standard
* Type: string - Relative path to the service partial
* Since: 2017.01

To configure an alternative template for the service partial, you
have to configure its path relative to the template directory
(usually client/html/templates/). It's then used to display the
payment or delivery service block in the account history component

See also:

* client/html/account/history/summary/address
* client/html/account/history/summary/detail

# url
## action

Name of the action that should create the output

```
client/html/account/history/url/action = history
```

* Default: history
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/account/history/url/target
* client/html/account/history/url/controller
* client/html/account/history/url/config

## config

Associative list of configuration options used for generating the URL

```
client/html/account/history/url/config = Array
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

* client/html/account/history/url/target
* client/html/account/history/url/controller
* client/html/account/history/url/action
* client/html/url/config

## controller

Name of the controller whose action should be called

```
client/html/account/history/url/controller = account
```

* Default: account
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/account/history/url/target
* client/html/account/history/url/action
* client/html/account/history/url/config

## target

Destination of the URL where the controller specified in the URL is known

```
client/html/account/history/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/account/history/url/controller
* client/html/account/history/url/action
* client/html/account/history/url/config