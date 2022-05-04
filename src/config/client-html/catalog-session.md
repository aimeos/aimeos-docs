
# decorators
## excludes

Excludes decorators added by the "common" option from the catalog session html client

```
client/html/catalog/session/decorators/excludes = Array
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
 client/html/catalog/session/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/session/decorators/global
* client/html/catalog/session/decorators/local

## global

Adds a list of globally available decorators only to the catalog session html client

```
client/html/catalog/session/decorators/global = Array
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
 client/html/catalog/session/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/session/decorators/excludes
* client/html/catalog/session/decorators/local

## local

Adds a list of local decorators only to the catalog session html client

```
client/html/catalog/session/decorators/local = Array
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
 client/html/catalog/session/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/session/decorators/excludes
* client/html/catalog/session/decorators/global

# name

Class name of the used catalog session client implementation

```
client/html/catalog/session/name = Standard
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
 \Aimeos\Client\Html\Catalog\Session\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Session\Mysession
```

then you have to set the this configuration option:

```
 client/html/catalog/session/name = Mysession
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MySession"!


# pinned

All parameters defined for the catalog session pinned subpart

```
client/html/catalog/session/pinned = Array
(
)
```

* Default: Array
(
)

* Type: array - Associative list of name/value settings

This returns all settings related to the catalog session pinned subpart.
Please refer to the single settings for details.

See also:

* client/html/catalog/session#pinned

## count/enable

Displays the number of pinned products in the header of the pinned list

```
client/html/catalog/session/pinned/count/enable = 1
```

* Default: 1
* Type: integer - Zero to disable the counter, one to enable it
* Since: 2014.09

This configuration option enables or disables displaying the total number
of pinned products in the header of section. This increases the usability if
more than the shown products are available in the list but this depends on
the design of the site.

See also:

* client/html/catalog/session/seen/count/enable

## decorators/global

```
client/html/catalog/session/pinned/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/catalog/session/pinned/decorators/local = Array
(
)
```

* Default: Array
(
)



## domains

A list of domain names whose items should be available in the pinned view template for the product

```
client/html/catalog/session/pinned/domains = Array
(
    [0] => media
    [1] => price
    [2] => text
)
```

* Default: Array
(
    [0] => media
    [1] => price
    [2] => text
)

* Type: array - List of domain names
* Since: 2015.04

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

## maxitems

Maximum number of products displayed in the "pinned" section

```
client/html/catalog/session/pinned/maxitems = 50
```

* Default: 50
* Type: integer - Number of products
* Since: 2014.09

This option limits the number of products that are shown in the
"pinned" section after the users added the product to their list
of pinned products. It must be a positive integer value greater
than 0.

Note: The higher the value is the more data has to be transfered
to the client each time the user loads a page with the list of
pinned products.


## name

Name of the pinned part used by the catalog session client implementation

```
client/html/catalog/session/pinned/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.09

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Session\Pinned\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the catalog session pinned client.

```
client/html/catalog/session/pinned/template-body = catalog/session/pinned-body
```

* Default: catalog/session/pinned-body
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/catalog/session/pinned/template-header

## url/action

Name of the action that should create the output

```
client/html/catalog/session/pinned/url/action = session
```

* Default: session
* Type: string - Name of the action
* Since: 2014.09

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/catalog/session/pinned/url/target
* client/html/catalog/session/pinned/url/controller
* client/html/catalog/session/pinned/url/config

## url/config

Associative list of configuration options used for generating the URL

```
client/html/catalog/session/pinned/url/config = Array
(
)
```

* Default: Array
(
)

* Type: string - Associative list of configuration options
* Since: 2014.09

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

* client/html/catalog/session/pinned/url/target
* client/html/catalog/session/pinned/url/controller
* client/html/catalog/session/pinned/url/action
* client/html/url/config

## url/controller

Name of the controller whose action should be called

```
client/html/catalog/session/pinned/url/controller = Catalog
```

* Default: Catalog
* Type: string - Name of the controller
* Since: 2014.09

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/catalog/session/pinned/url/target
* client/html/catalog/session/pinned/url/action
* client/html/catalog/session/pinned/url/config

## url/filter

```
client/html/catalog/session/pinned/url/filter = Array
(
)
```

* Default: Array
(
)



## url/target

Destination of the URL where the controller specified in the URL is known

```
client/html/catalog/session/pinned/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2014.09

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/catalog/session/pinned/url/controller
* client/html/catalog/session/pinned/url/action
* client/html/catalog/session/pinned/url/config

# seen

All parameters defined for the catalog session seen subpart

```
client/html/catalog/session/seen = Array
(
)
```

* Default: Array
(
)

* Type: array - Associative list of name/value settings

This returns all settings related to the catalog session seen subpart.
Please refer to the single settings for details.

See also:

* client/html/catalog#session

## count/enable

Displays the number of last seen products in the header of the last seen list

```
client/html/catalog/session/seen/count/enable = 1
```

* Default: 1
* Type: integer - Zero to disable the counter, one to enable it
* Since: 2014.09

This configuration option enables or disables displaying the total number
of last seen products in the header of section. This increases the usability
if more than the shown products are available in the list but this depends on
the design of the site.

See also:

* client/html/catalog/session/pinned/count/enable

## decorators/global

```
client/html/catalog/session/seen/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/catalog/session/seen/decorators/local = Array
(
)
```

* Default: Array
(
)



## maxitems

Maximum number of products displayed in the "last seen" section

```
client/html/catalog/session/seen/maxitems = 6
```

* Default: 6
* Type: integer - Number of products
* Since: 2014.03

This option limits the number of products that are shown in the
"last seen" section after the user visited their detail pages. It
must be a positive integer value greater than 0.


## name

Name of the seen part used by the catalog session client implementation

```
client/html/catalog/session/seen/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Session\Seen\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the catalog session seen client.

```
client/html/catalog/session/seen/template-body = catalog/session/seen-body
```

* Default: catalog/session/seen-body
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/catalog/session/seen/template-header

# subparts

List of HTML sub-clients rendered within the catalog session section

```
client/html/catalog/session/subparts = Array
(
    [0] => pinned
    [1] => seen
)
```

* Default: Array
(
    [0] => pinned
    [1] => seen
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


# template-body

Relative path to the HTML body template of the catalog session client.

```
client/html/catalog/session/template-body = 
```

* Default: 
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/catalog/session/template-header

# template-header

Relative path to the HTML header template of the catalog session client.

```
client/html/catalog/session/template-header = 
```

* Default: 
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2014.03

The template file contains the HTML code and processing instructions
to generate the HTML code that is inserted into the HTML page header
of the rendered page in the frontend. The configuration string is the
path to the template file relative to the templates directory (usually
in client/html/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but suffixed by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, it
should be suffixed by the name of the new class.

See also:

* client/html/catalog/session/template-body