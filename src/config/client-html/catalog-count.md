
# attribute
## aggregate

Enables or disables generating product counts for the attribute catalog filter

```
client/html/catalog/count/attribute/aggregate = 1
```

* Default: 1
* Type: boolean - Disabled if "0", enabled if "1"
* Since: 2014.03

This configuration option allows shop owners to enable or disable product counts
for the attribute section of the catalog filter HTML client.


## decorators/global

```
client/html/catalog/count/attribute/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/catalog/count/attribute/decorators/local = Array
(
)
```

* Default: Array
(
)



## name

Name of the attribute part used by the catalog count client implementation

```
client/html/catalog/count/attribute/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Count\Attribute\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the catalog count attribute client.

```
client/html/catalog/count/attribute/template-body =
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

* client/html/catalog/count/attribute/template-header

# decorators
## excludes

Excludes decorators added by the "common" option from the catalog count html client

```
client/html/catalog/count/decorators/excludes = Array
(
)
```

* Default: Array
(
)

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
 client/html/catalog/count/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/count/decorators/global
* client/html/catalog/count/decorators/local

## global

Adds a list of globally available decorators only to the catalog count html client

```
client/html/catalog/count/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/catalog/count/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/count/decorators/excludes
* client/html/catalog/count/decorators/local

## local

Adds a list of local decorators only to the catalog count html client

```
client/html/catalog/count/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.05

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Catalog\Decorator\*") around the html client.

```
 client/html/catalog/count/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/count/decorators/excludes
* client/html/catalog/count/decorators/global

# enable

Enables or disables displaying product counts in the catalog filter

```
client/html/catalog/count/enable = 1
```

* Default: 1
* Type: boolean - Value of "1" to display product counts, "0" to disable them
* Since: 2014.03

This configuration option allows shop owners to display product
counts in the catalog filter or to disable fetching product count
information.

The product count information is fetched via AJAX and inserted via
Javascript. This allows to cache parts of the catalog filter by
leaving out such highly dynamic content like product count which
changes with used filter parameter.

See also:

* client/html/catalog/count/url/target
* client/html/catalog/count/url/controller
* client/html/catalog/count/url/action
* client/html/catalog/count/url/config

# name

Class name of the used catalog count client implementation

```
client/html/catalog/count/name = Standard
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
 \Aimeos\Client\Html\Catalog\Count\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Count\Mycount
```

then you have to set the this configuration option:

```
 client/html/catalog/count/name = Mycount
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCount"!


# subparts

List of HTML sub-clients rendered within the catalog count section

```
client/html/catalog/count/subparts = Array
(
    [0] => tree
    [1] => supplier
    [2] => attribute
)
```

* Default: Array
(
    [0] => tree
    [1] => supplier
    [2] => attribute
)

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
## aggregate

Enables or disables generating product counts for the supplier catalog filter

```
client/html/catalog/count/supplier/aggregate = 1
```

* Default: 1
* Type: boolean - Disabled if "0", enabled if "1"
* Since: 2018.07

This configuration option allows shop owners to enable or disable product counts
for the supplier section of the catalog filter HTML client.


## decorators/global

```
client/html/catalog/count/supplier/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/catalog/count/supplier/decorators/local = Array
(
)
```

* Default: Array
(
)



## name

Name of the supplier part used by the catalog count client implementation

```
client/html/catalog/count/supplier/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2018.07

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Count\Attribute\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the catalog count supplier client.

```
client/html/catalog/count/supplier/template-body =
```

* Default:
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2018.07

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

* client/html/catalog/count/supplier/template-header

# template-body

Relative path to the HTML body template of the catalog count client.

```
client/html/catalog/count/template-body =
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

* client/html/catalog/count/template-header

# template-header

Relative path to the HTML header template of the catalog count client.

```
client/html/catalog/count/template-header =
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

* client/html/catalog/count/template-body

# tree
## aggregate

Enables or disables generating product counts for the category catalog filter

```
client/html/catalog/count/tree/aggregate = 1
```

* Default: 1
* Type: boolean - Disabled if "0", enabled if "1"
* Since: 2014.03

This configuration option allows shop owners to enable or disable product counts
for the tree section of the catalog filter HTML client.


## decorators/global

```
client/html/catalog/count/tree/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/catalog/count/tree/decorators/local = Array
(
)
```

* Default: Array
(
)



## name

Name of the tree part used by the catalog count client implementation

```
client/html/catalog/count/tree/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Count\Tree\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the catalog count tree client.

```
client/html/catalog/count/tree/template-body =
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

* client/html/catalog/count/tree/template-header

# url
## action

Name of the action that should create the output

```
client/html/catalog/count/url/action = count
```

* Default: count
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/catalog/count/url/target
* client/html/catalog/count/url/controller
* client/html/catalog/count/url/config

## config

Associative list of configuration options used for generating the URL

```
client/html/catalog/count/url/config = Array
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

* client/html/catalog/count/url/target
* client/html/catalog/count/url/controller
* client/html/catalog/count/url/action
* client/html/url/config

## controller

Name of the controller whose action should be called

```
client/html/catalog/count/url/controller = Catalog
```

* Default: Catalog
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/catalog/count/url/target
* client/html/catalog/count/url/action
* client/html/catalog/count/url/config

## filter

```
client/html/catalog/count/url/filter = Array
(
)
```

* Default: Array
(
)



## target

Destination of the URL where the controller specified in the URL is known

```
client/html/catalog/count/url/target =
```

* Default:
* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/catalog/count/url/controller
* client/html/catalog/count/url/action
* client/html/catalog/count/url/config