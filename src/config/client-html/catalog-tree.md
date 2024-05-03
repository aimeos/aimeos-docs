
# decorators
## excludes

Excludes decorators added by the "common" option from the catalog tree html client

```
client/html/catalog/tree/decorators/excludes = 
```

* Type: array - List of decorator names

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/catalog/tree/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/tree/decorators/global
* client/html/catalog/tree/decorators/local

## global

Adds a list of globally available decorators only to the catalog tree html client

```
client/html/catalog/tree/decorators/global = 
```

* Type: array - List of decorator names

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/catalog/tree/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/tree/decorators/excludes
* client/html/catalog/tree/decorators/local

## local

Adds a list of local decorators only to the catalog tree html client

```
client/html/catalog/tree/decorators/local = 
```

* Type: array - List of decorator names

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Catalog\Decorator\*") around the html client.

```
 client/html/catalog/tree/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/tree/decorators/excludes
* client/html/catalog/tree/decorators/global

# name

Class name of the used catalog tree client implementation

```
client/html/catalog/tree/name = 
```

* Type: string - Last part of the class name
* Since: 2018.04

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Catalog\Tree\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Tree\Mytree
```

then you have to set the this configuration option:

```
 client/html/catalog/tree/name = Mytree
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyTree"!


# url
## action

Name of the action that should create the output

```
client/html/catalog/tree/url/action = list
```

* Default: `list`
* Type: string - Name of the action
* Since: 2019.01

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/catalog/tree/url/target
* client/html/catalog/tree/url/controller
* client/html/catalog/tree/url/config
* client/html/catalog/tree/url/filter

## config

Associative list of configuration options used for generating the URL

```
client/html/catalog/tree/url/config = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: string - Associative list of configuration options
* Since: 2019.01

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

* client/html/catalog/tree/url/target
* client/html/catalog/tree/url/controller
* client/html/catalog/tree/url/action
* client/html/catalog/tree/url/filter

## controller

Name of the controller whose action should be called

```
client/html/catalog/tree/url/controller = catalog
```

* Default: `catalog`
* Type: string - Name of the controller
* Since: 2019.01

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/catalog/tree/url/target
* client/html/catalog/tree/url/action
* client/html/catalog/tree/url/config
* client/html/catalog/tree/url/filter

## filter

Removes parameters for the detail page before generating the URL

```
client/html/catalog/tree/url/filter = Array
(
    [0] => path
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of parameter names to remove
* Since: 2022.10

This setting removes the listed parameters from the URLs. Keep care to
remove no required parameters!

See also:

* client/html/catalog/tree/url/target
* client/html/catalog/tree/url/controller
* client/html/catalog/tree/url/action
* client/html/catalog/tree/url/config

## target

Destination of the URL where the controller specified in the URL is known

```
client/html/catalog/tree/url/target = 
```

* Type: string - Destination of the URL
* Since: 2019.01

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/catalog/tree/url/controller
* client/html/catalog/tree/url/action
* client/html/catalog/tree/url/config
* client/html/catalog/tree/url/filter