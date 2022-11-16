
# attribute
## decorators/global

```
client/html/catalog/filter/attribute/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/catalog/filter/attribute/decorators/local = Array
(
)
```

* Default: Array
(
)



## domains

List of domain names whose items should be fetched with the filter attributes

```
client/html/catalog/filter/attribute/domains = Array
(
    [0] => text
    [1] => media
    [2] => media/property
)
```

* Default: Array
(
    [0] => text
    [1] => media
    [2] => media/property
)

* Type: array - List of domain item names
* Since: 2015.05

The templates rendering the attributes in the catalog filter usually
add the images and texts associated to each item. If you want to
display additional content, you can configure your own list of
domains (attribute, media, price, product, text, etc. are domains)
whose items are fetched from the storage. Please keep in mind that
the more domains you add to the configuration, the more time is
required for fetching the content!

See also:

* client/html/catalog/filter/attribute/types

## name

Name of the attribute part used by the catalog filter client implementation

```
client/html/catalog/filter/attribute/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Filter\Attribute\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the catalog filter attribute client.

```
client/html/catalog/filter/attribute/template-body = 
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

* client/html/catalog/filter/attribute/template-header

## types

List of attribute types that should be displayed in this order in the catalog filter

```
client/html/catalog/filter/attribute/types = Array
(
)
```

* Default: Array
(
)

* Type: array - List of attribute type codes
* Since: 2015.05

The attribute section in the catalog filter component can display
all attributes a visitor can use to reduce the listed products
to those that contains one or more attributes. By default, all
available attributes will be displayed and ordered by their
attribute type.

With this setting, you can limit the attribute types to only thoses
whose names are part of the setting value. Furthermore, a particular
order for the attribute types can be enforced that is different
from the standard order.

See also:

* client/html/catalog/filter/attribute/domains
* client/html/catalog/filter/attribute/types-oneof
* client/html/catalog/filter/attribute/types-option

## types-oneof

List of attribute types whose values should be used in a type specific "OR" condition

```
client/html/catalog/filter/attribute/types-oneof = Array
(
)
```

* Default: Array
(
)

* Type: array - List of attribute type codes
* Since: 2016.10

The attribute section in the catalog filter component can display all
attributes a visitor can use to filter the listed products to those that
contains one or more attributes.

This configuration setting lists the attribute types where at least one of
the attributes within the same attribute type must be referenced by the found
products.

See also:

* client/html/catalog/filter/attribute/types
* client/html/catalog/filter/attribute/types-option

## types-option

List of attribute types whose IDs should be used in a global "OR" condition

```
client/html/catalog/filter/attribute/types-option = Array
(
)
```

* Default: Array
(
)

* Type: array - List of attribute type codes
* Since: 2016.10

The attribute section in the catalog filter component can display all
attributes a visitor can use to filter the listed products to those that
contains one or more attributes.

This configuration setting lists the attribute types where at least one of
all attributes must be referenced by the found products. Only one attribute
of all listed attributes types (whatever matches) in enough. This setting is
different from "client/html/catalog/filter/attribute/types-oneof" because
it's not limited within the same attribute type

See also:

* client/html/catalog/filter/attribute/types
* client/html/catalog/filter/attribute/types-oneof

# button

Displays the "Search" button in the catalog filter if Javascript is disabled

```
client/html/catalog/filter/button = 1
```

* Default: 1
* Type: boolean - A value of "1" to enable the button, "0" to disable it
* Since: 2014.03

Usually the "Search" button is shown in the catalog filter if the browser
doesn't support Javascript or the user has disabled Javascript for the site.
If you are using parts of the catalog filter to e.g. render a menu, the
button shouldn't be displayed at all. This can be explicitely set via this
configuration option.


# cache

Enables or disables caching only for the catalog filter component

```
client/html/catalog/filter/cache = 1
```

* Default: 1
* Type: boolean - True to enable caching, false to disable

Disable caching for components can be useful if you would have too much
entries to cache or if the component contains non-cacheable parts that
can't be replaced using the modify() method.

See also:

* client/html/catalog/detail/cache
* client/html/catalog/lists/cache
* client/html/catalog/stage/cache

# decorators
## excludes

Excludes decorators added by the "common" option from the catalog filter html client

```
client/html/catalog/filter/decorators/excludes = Array
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
 client/html/catalog/filter/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/filter/decorators/global
* client/html/catalog/filter/decorators/local

## global

Adds a list of globally available decorators only to the catalog filter html client

```
client/html/catalog/filter/decorators/global = Array
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
 client/html/catalog/filter/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/filter/decorators/excludes
* client/html/catalog/filter/decorators/local

## local

Adds a list of local decorators only to the catalog filter html client

```
client/html/catalog/filter/decorators/local = Array
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
 client/html/catalog/filter/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/filter/decorators/excludes
* client/html/catalog/filter/decorators/global

# name

Class name of the used catalog filter client implementation

```
client/html/catalog/filter/name = Standard
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
 \Aimeos\Client\Html\Catalog\Filter\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Filter\Myfilter
```

then you have to set the this configuration option:

```
 client/html/catalog/filter/name = Myfilter
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFilter"!


# price
## decorators/global

```
client/html/catalog/filter/price/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/catalog/filter/price/decorators/local = Array
(
)
```

* Default: Array
(
)



## name

Name of the price part used by the catalog filter client implementation

```
client/html/catalog/filter/price/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2020.10

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Filter\Price\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the catalog filter price client.

```
client/html/catalog/filter/price/template-body = 
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

* client/html/catalog/filter/price/template-header

# remove-params

Removes the configured parameters before generating filter URLs for the list view

```
client/html/catalog/filter/remove-params = Array
(
    [0] => f_sort
)
```

* Default: Array
(
    [0] => f_sort
)

* Type: array - List of parameter names
* Since: 2020.04

Use this array instead if you want to keep the selected category and the
entered search string as well:

['f_catid', 'f_search', 'f_sort']

Downside: It will be impossible for customers to deselect the category!


# search
## decorators/global

```
client/html/catalog/filter/search/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/catalog/filter/search/decorators/local = Array
(
)
```

* Default: Array
(
)



## force-search

Always reuse the current input for full text searches

```
client/html/catalog/filter/search/force-search = 1
```

* Default: 1
* Type: boolean - True to reuse the search string, false to clear after each search
* Since: 2020.04

Normally, the full text search string is added to the input field after each
search. This is also the standard behavior of other shops.

If it's desired, setting this configuration option to "0" will drop the full
text search input so it's not used if the user selects a category or attribute
filter.


## name

Name of the search part used by the catalog filter client implementation

```
client/html/catalog/filter/search/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Filter\Search\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the catalog filter search client.

```
client/html/catalog/filter/search/template-body = 
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

* client/html/catalog/filter/search/template-header

# subparts

List of HTML sub-clients rendered within the catalog filter section

```
client/html/catalog/filter/subparts = Array
(
    [0] => search
    [1] => price
    [2] => supplier
    [3] => attribute
)
```

* Default: Array
(
    [0] => tree
    [1] => search
    [2] => price
    [3] => supplier
    [4] => attribute
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
## decorators/global

```
client/html/catalog/filter/supplier/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/catalog/filter/supplier/decorators/local = Array
(
)
```

* Default: Array
(
)



## domains

List of domain names whose items should be fetched with the filter suppliers

```
client/html/catalog/filter/supplier/domains = Array
(
    [0] => text
    [1] => media
    [2] => media/property
)
```

* Default: Array
(
    [0] => text
    [1] => media
    [2] => media/property
)

* Type: array - List of domain item names
* Since: 2018.07

The templates rendering the suppliers in the catalog filter usually
add the images and texts associated to each item. If you want to
display additional content, you can configure your own list of
domains (supplier, media, price, product, text, etc. are domains)
whose items are fetched from the storage. Please keep in mind that
the more domains you add to the configuration, the more time is
required for fetching the content!

See also:

* client/html/catalog/filter/supplier/types

## name

Name of the supplier part used by the catalog filter client implementation

```
client/html/catalog/filter/supplier/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2018.07

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Filter\Supplier\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## template-body

Relative path to the HTML body template of the catalog filter supplier client.

```
client/html/catalog/filter/supplier/template-body = 
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

* client/html/catalog/filter/supplier/template-header

# template-body

Relative path to the HTML body template of the catalog filter client.

```
client/html/catalog/filter/template-body = catalog/filter/body
```

* Default: catalog/filter/body
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

* client/html/catalog/filter/template-header

# template-header

Relative path to the HTML header template of the catalog filter client.

```
client/html/catalog/filter/template-header = catalog/filter/header
```

* Default: catalog/filter/header
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

* client/html/catalog/filter/template-body

# tree
## decorators/global

```
client/html/catalog/filter/tree/decorators/global = Array
(
)
```

* Default: Array
(
)



## decorators/local

```
client/html/catalog/filter/tree/decorators/local = Array
(
)
```

* Default: Array
(
)



## domains

List of domain names whose items should be fetched with the filter categories

```
client/html/catalog/filter/tree/domains = Array
(
    [0] => text
    [1] => media
    [2] => media/property
)
```

* Default: Array
(
    [0] => text
    [1] => media
    [2] => media/property
)

* Type: array - List of domain item names
* Since: 2014.03

The templates rendering the categories in the catalog filter usually
add the images and texts associated to each item. If you want to
display additional content, you can configure your own list of
domains (attribute, media, price, product, text, etc. are domains)
whose items are fetched from the storage. Please keep in mind that
the more domains you add to the configuration, the more time is
required for fetching the content!

See also:

* controller/frontend/catalog/levels-always
* controller/frontend/catalog/levels-only
* client/html/catalog/filter/tree/startid

## force-search

Use the current category in full text searches

```
client/html/catalog/filter/tree/force-search = 
```

* Default: 
* Type: boolean - True to enforce current category for search, false for full text search only
* Since: 2015.10

Normally, a full text search finds all products that match the entered string
regardless of the category the user is currently in. This is also the standard
behavior of other shops.

If it's desired, setting this configuration option to "1" will limit the full
text search to the current category only, so only products that match the text
and which are in the current category are found.


## name

Name of the tree part used by the catalog filter client implementation

```
client/html/catalog/filter/tree/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Filter\Tree\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## partial

Relative path to the category tree partial template file

```
client/html/catalog/filter/tree/partial = catalog/filter/tree-partial
```

* Default: catalog/filter/tree-partial
* Type: string - Relative path to the template file
* Since: 2022.04

Partials are templates which are reused in other templates and generate
reoccuring blocks filled with data from the assigned values. The tree
partial creates an HTML block of nested lists for category trees.


## startid

The ID of the category node that should be the root of the displayed category tree

```
client/html/catalog/filter/tree/startid = 
```

* Default: 
* Type: string - Category ID
* Since: 2014.03

If you want to display only a part of your category tree, you can
configure the ID of the category node from which rendering the
remaining sub-tree should start.

In most cases you can set this value via the administration interface
of the shop application. In that case you often can configure the
start ID individually for each catalog filter.

See also:

* controller/frontend/catalog/levels-always
* controller/frontend/catalog/levels-only
* client/html/catalog/filter/tree/domains

## template-body

Relative path to the HTML body template of the catalog filter tree client.

```
client/html/catalog/filter/tree/template-body = 
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

* client/html/catalog/filter/tree/template-header