
# decorators
## excludes

```
client/html/catalog/tree/decorators/excludes = Array
(
)
```

* Default: Array
(
)



## global

```
client/html/catalog/tree/decorators/global = Array
(
)
```

* Default: Array
(
)



## local

```
client/html/catalog/tree/decorators/local = Array
(
)
```

* Default: Array
(
)



# name

Class name of the used catalog tree client implementation

```
client/html/catalog/tree/name = Standard
```

* Default: Standard
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

* Default: list
* Type: string - Name of the action
* Since: 2019.01

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/catalog/tree/url/target
* client/html/catalog/tree/url/controller
* client/html/catalog/tree/url/config

## config

Associative list of configuration options used for generating the URL

```
client/html/catalog/tree/url/config = Array
(
)
```

* Default: Array
(
)

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
* client/html/url/config

## controller

Name of the controller whose action should be called

```
client/html/catalog/tree/url/controller = catalog
```

* Default: catalog
* Type: string - Name of the controller
* Since: 2019.01

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/catalog/tree/url/target
* client/html/catalog/tree/url/action
* client/html/catalog/tree/url/config

## filter

```
client/html/catalog/tree/url/filter = Array
(
)
```

* Default: Array
(
)



## target

Destination of the URL where the controller specified in the URL is known

```
client/html/catalog/tree/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2019.01

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/catalog/tree/url/controller
* client/html/catalog/tree/url/action
* client/html/catalog/tree/url/config