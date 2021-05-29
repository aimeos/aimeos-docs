
# decorators
## excludes

Excludes decorators added by the "common" option from the catalog suggest html client

```
client/html/catalog/suggest/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.02

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/catalog/suggest/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/suggest/decorators/global
* client/html/catalog/suggest/decorators/local

## global

Adds a list of globally available decorators only to the catalog suggest html client

```
client/html/catalog/suggest/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.02

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/catalog/suggest/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/suggest/decorators/excludes
* client/html/catalog/suggest/decorators/local

## local

Adds a list of local decorators only to the catalog suggest html client

```
client/html/catalog/suggest/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2015.02

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Catalog\Decorator\*") around the html client.

```
 client/html/catalog/suggest/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/suggest/decorators/excludes
* client/html/catalog/suggest/decorators/global

# domains

List of domain items that should be fetched along with the products

```
client/html/catalog/suggest/domains = Array
(
    [0] => text
)
```

* Default: Array
* Type: array - List of domain names
* Since: 2016.08

The suggsted entries for the full text search in the catalog filter component
usually consist of the names of the matched products. By default, only the
product item including the localized name is available. You can add more domains
like e.g. "media" to get the images of the product as well.

**Note:** The more domains you will add, the slower the autocomplete requests
will be! Keep it to an absolute minium for user friendly response times.

See also:

* client/html/catalog/suggest/template-body
* client/html/catalog/suggest/restrict
* client/html/catalog/suggest/size

# name

Class name of the used catalog suggest client implementation

```
client/html/catalog/suggest/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2015.02

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Catalog\Suggest\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Suggest\Mysuggest
```

then you have to set the this configuration option:

```
 client/html/catalog/suggest/name = Mysuggest
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MySuggest"!


# restrict

Restricts suggestions to category and attribute facets

```
client/html/catalog/suggest/restrict = 1
```

* Default: 1
* Type: boolean - True to use category and facets, false for all results
* Since: 2019.07

Limits the shown suggestions to the current category and selected
attribute facets. If disabled, suggestions are limited by the
entered text only.

See also:

* client/html/catalog/suggest/domains
* client/html/catalog/suggest/size

# size

The number of products shown in the list of suggestions

```
client/html/catalog/suggest/size = 24
```

* Default: 24
* Type: integer - Number of products
* Since: 2018.10

Limits the number of products that are shown in the list of suggested
products.

See also:

* client/html/catalog/suggest/domains
* client/html/catalog/suggest/restrict

# subparts

List of HTML sub-clients rendered within the catalog suggest client

```
client/html/catalog/suggest/subparts = Array
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

Note: Up to 2015-02, this configuration option was available as
client/html/catalog/lists/simple/subparts


# template-body

Relative path to the HTML body template of the catalog suggest client.

```
client/html/catalog/suggest/template-body = catalog/suggest/body-standard
```

* Default: catalog/suggest/body-standard
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

Note: Up to 2015-02, this configuration option was available as
client/html/catalog/lists/simple/template-body

See also:

* client/html/catalog/suggest/template-header
* client/html/catalog/suggest/domains

# template-header

Relative path to the HTML header template of the catalog suggest client.

```
client/html/catalog/suggest/template-header = catalog/suggest/header-standard
```

* Default: catalog/suggest/header-standard
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2015.02

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

Note: Up to 2015-02, this configuration option was available as
client/html/catalog/lists/simple/template-header

See also:

* client/html/catalog/suggest/template-body
* client/html/catalog/suggest/domains

# url
## action

Name of the action that should create the output

```
client/html/catalog/suggest/url/action = suggest
```

* Default: suggest
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

Note: Up to 2015-02, the setting was available as
client/html/catalog/listsimple/url/action

See also:

* client/html/catalog/suggest/url/target
* client/html/catalog/suggest/url/controller
* client/html/catalog/suggest/url/config
* client/html/catalog/listsimple/url/action

## config

Associative list of configuration options used for generating the URL

```
client/html/catalog/suggest/url/config = Array
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

Note: Up to 2015-02, the setting was available as
client/html/catalog/listsimple/url/config

See also:

* client/html/catalog/suggest/url/target
* client/html/catalog/suggest/url/controller
* client/html/catalog/suggest/url/action
* client/html/url/config
* client/html/catalog/listsimple/url/config

## controller

Name of the controller whose action should be called

```
client/html/catalog/suggest/url/controller = catalog
```

* Default: catalog
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

Note: Up to 2015-02, the setting was available as
client/html/catalog/listsimple/url/controller

See also:

* client/html/catalog/suggest/url/target
* client/html/catalog/suggest/url/action
* client/html/catalog/suggest/url/config
* client/html/catalog/listsimple/url/controller

## target

Destination of the URL where the controller specified in the URL is known

```
client/html/catalog/suggest/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

Note: Up to 2015-02, the setting was available as
client/html/catalog/listsimple/url/target

See also:

* client/html/catalog/suggest/url/controller
* client/html/catalog/suggest/url/action
* client/html/catalog/suggest/url/config
* client/html/catalog/listsimple/url/target