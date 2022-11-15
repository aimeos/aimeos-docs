
# decorators
## excludes

```
client/html/catalog/suggest/decorators/excludes = Array
(
)
```

* Default: Array
(
)



## global

```
client/html/catalog/suggest/decorators/global = Array
(
)
```

* Default: Array
(
)



## local

```
client/html/catalog/suggest/decorators/local = Array
(
)
```

* Default: Array
(
)



# domains

List of domain items that should be fetched along with the products

```
client/html/catalog/suggest/domains = Array
(
    [0] => text
)
```

* Default: Array
(
    [0] => text
)

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

# template-body

Relative path to the HTML body template of the catalog suggest client.

```
client/html/catalog/suggest/template-body =
```

* Default:
* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2015.02

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

* client/html/catalog/suggest/template-header
* client/html/catalog/suggest/domains

# template-header

Relative path to the HTML header template of the catalog suggest client.

```
client/html/catalog/suggest/template-header =
```

* Default:
* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2015.02

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
client/html/catalog/suggest/url/controller = Catalog
```

* Default: Catalog
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

## filter

```
client/html/catalog/suggest/url/filter = Array
(
)
```

* Default: Array
(
)



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