
# cache

Enables or disables caching only for the supplier detail component

```
client/html/supplier/detail/cache = 1
```

* Default: 1
* Type: boolean - True to enable caching, false to disable

Disable caching for components can be useful if you would have too much
entries to cache or if the component contains non-cacheable parts that
can't be replaced using the `modify()` methods.

See also:

* client/html/supplier/detail/cache
* client/html/supplier/filter/cache
* client/html/supplier/lists/cache

# decorators
## excludes

Excludes decorators added by the "common" option from the supplier detail html client

```
client/html/supplier/detail/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2020.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/supplier/detail/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/supplier/detail/decorators/global
* client/html/supplier/detail/decorators/local

## global

Adds a list of globally available decorators only to the supplier detail html client

```
client/html/supplier/detail/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2020.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/supplier/detail/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/supplier/detail/decorators/excludes
* client/html/supplier/detail/decorators/local

## local

Adds a list of local decorators only to the supplier detail html client

```
client/html/supplier/detail/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2020.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Supplier\Decorator\*") around the html client.

```
 client/html/supplier/detail/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Supplier\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/supplier/detail/decorators/excludes
* client/html/supplier/detail/decorators/global

# domains

A list of domain names whose items should be available in the supplier detail view template

```
client/html/supplier/detail/domains = Array
(
    [0] => supplier/address
    [1] => media
    [2] => text
)
```

* Default: Array
* Type: array - List of domain names
* Since: 2020.10

The templates rendering the supplier detail section use the texts and
maybe images and attributes associated to the categories. You can
configure your own list of domains (attribute, media, price, product,
text, etc. are domains) whose items are fetched from the storage.
Please keep in mind that the more domains you add to the configuration,
the more time is required for fetching the content!


# metatags

Adds the title, meta and link tags to the HTML header

```
client/html/supplier/detail/metatags = 1
```

* Default: 1
* Type: boolean - True to display the meta tags, false to hide it
* Since: 2021.01

By default, each instance of the supplier list component adds some HTML meta
tags to the page head section, like page title, meta keywords and description
as well as some link tags to support browser navigation. If several instances
are placed on one page, this leads to adding several title and meta tags used
by search engine. This setting enables you to suppress these tags in the page
header and maybe add your own to the page manually.

See also:

* client/html/supplier/lists/metatags

# name

Class name of the used supplier detail client implementation

```
client/html/supplier/detail/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2020.10

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Supplier\Detail\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Supplier\Detail\Mydetail
```

then you have to set the this configuration option:

```
 client/html/supplier/detail/name = Mydetail
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyDetail"!


# navigator
## name

Name of the navigator part used by the supplier detail client implementation

```
client/html/supplier/detail/navigator/name = 
```

* Default: 
* Type: string - Last part of the client class name
* Since: 2014.09

Use "Myname" if your class is named "\Aimeos\Client\Html\Supplier\Detail\Breadcrumb\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


# subparts

List of HTML sub-clients rendered within the supplier detail section

```
client/html/supplier/detail/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2020.10

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


# supid-default

The default supplier ID used if none is given as parameter

```
client/html/supplier/detail/supid-default = 1
```

* Default: 
* Type: string - Supplier ID
* Since: 2021.01

You can configure the default supplier ID if no ID is passed in the
URL using this configuration.

See also:

* client/html/catalog/lists/catid-default

# template-body

Relative path to the HTML body template of the supplier detail client.

```
client/html/supplier/detail/template-body = supplier/detail/body-standard
```

* Default: supplier/detail/body-standard
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2020.10

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

* client/html/supplier/detail/template-header

# template-header

Relative path to the HTML header template of the supplier detail client.

```
client/html/supplier/detail/template-header = supplier/detail/header-standard
```

* Default: supplier/detail/header-standard
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2020.10

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

* client/html/supplier/detail/template-body

# url
## action

```
client/html/supplier/detail/url/action = detail
```

* Default: detail


## config

```
client/html/supplier/detail/url/config = Array
(
)
```

* Default: Array


## controller

```
client/html/supplier/detail/url/controller = supplier
```

* Default: supplier


## filter

```
client/html/supplier/detail/url/filter = Array
(
)
```

* Default: Array


## target

```
client/html/supplier/detail/url/target = 
```

* Default: 
