
# basket-add

Display the "add to basket" button for each product item

```
client/html/catalog/lists/basket-add = 
```

* Default: 
* Type: boolean - True to display the button, false to hide it
* Since: 2016.01

Enables the button for adding products to the basket from the list view.
This works for all type of products, even for selection products with product
variants and product bundles. By default, also optional attributes are
displayed if they have been associated to a product.

**Note:** To fetch the necessary product variants, you have to extend the
list of domains for "client/html/catalog/lists/domains", e.g.

```
 client/html/catalog/lists/domains = array( 'attribute', 'media', 'price', 'product', 'text' )
```

See also:

* client/html/catalog/home/basket-add
* client/html/catalog/detail/basket-add
* client/html/catalog/product/basket-add
* client/html/basket/related/basket-add
* client/html/catalog/domains

# cache

Enables or disables caching only for the catalog lists component

```
client/html/catalog/lists/cache = 1
```

* Default: 1
* Type: boolean - True to enable caching, false to disable

Disable caching for components can be useful if you would have too much
entries to cache or if the component contains non-cacheable parts that
can't be replaced using the modifyBody() and modifyHeader() methods.

See also:

* client/html/catalog/detail/cache
* client/html/catalog/filter/cache
* client/html/catalog/stage/cache

# catid-default

The default category ID used if none is given as parameter

```
client/html/catalog/lists/catid-default = 
```

* Default: 
* Type: array|string - Category ID or IDs
* Since: 2014.03

If users view a product list page without a category ID in the
parameter list, the first found products are displayed with a
random order. You can circumvent this by configuring a default
category ID that should be used in this case (the ID of the root
category is best for this). In most cases you can set this value
via the administration interface of the shop application.

See also:

* client/html/catalog/lists/sort
* client/html/catalog/lists/size
* client/html/catalog/lists/domains
* client/html/catalog/lists/levels
* client/html/catalog/detail/prodid-default
* client/html/catalog/lists/supid-default

# decorators
## excludes

Excludes decorators added by the "common" option from the catalog list html client

```
client/html/catalog/lists/decorators/excludes = Array
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
 client/html/catalog/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/lists/decorators/global
* client/html/catalog/lists/decorators/local

## global

Adds a list of globally available decorators only to the catalog list html client

```
client/html/catalog/lists/decorators/global = Array
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
 client/html/catalog/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/lists/decorators/excludes
* client/html/catalog/lists/decorators/local

## local

Adds a list of local decorators only to the catalog list html client

```
client/html/catalog/lists/decorators/local = Array
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
("\Aimeos\Client\Html\Catalog\Decorator\*") around the html client.

```
 client/html/catalog/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/lists/decorators/excludes
* client/html/catalog/lists/decorators/global

# domains

A list of domain names whose items should be available in the product list view template

```
client/html/catalog/lists/domains = Array
(
    [0] => media
    [1] => media/property
    [2] => price
    [3] => text
)
```

* Default: Array
* Type: array - List of domain names
* Since: 2014.03

The templates rendering product lists usually add the images, prices
and texts associated to each product item. If you want to display additional
content like the product attributes, you can configure your own list of
domains (attribute, media, price, product, text, etc. are domains)
whose items are fetched from the storage. Please keep in mind that
the more domains you add to the configuration, the more time is required
for fetching the content!

This configuration option overwrites the "client/html/catalog/domains"
option that allows to configure the domain names of the items fetched
for all catalog related data.

See also:

* client/html/catalog/domains
* client/html/catalog/detail/domains
* client/html/catalog/stage/domains
* client/html/catalog/lists/catid-default
* client/html/catalog/lists/supid-default
* client/html/catalog/lists/size
* client/html/catalog/lists/levels
* client/html/catalog/lists/sort
* client/html/catalog/lists/pages

# head
## text-types

The list of text types that should be rendered in the catalog list head section

```
client/html/catalog/lists/head/text-types = Array
(
    [0] => long
)
```

* Default: Array
* Type: array - List of text type names
* Since: 2014.03

The head section of the catalog list view at least consists of the category
name. By default, all short and long descriptions of the category are rendered
as well.

You can add more text types or remove ones that should be displayed by
modifying these list of text types, e.g. if you've added a new text type
and texts of that type to some or all categories.


# infinite-scroll

Enables infinite scrolling in product catalog list

```
client/html/catalog/lists/infinite-scroll = 
```

* Default: 
* Type: boolean - True to use infinite scrolling, false to disable it
* Since: 2019.10

If set to true, products from the next page are loaded via XHR request
and added to the product list when the user reaches the list bottom.


# items
## decorators/excludes

Excludes decorators added by the "common" option from the catalog list items html client

```
client/html/catalog/lists/items/decorators/excludes = 
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
 client/html/catalog/lists/items/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/lists/items/decorators/global
* client/html/catalog/lists/items/decorators/local

## decorators/global

Adds a list of globally available decorators only to the catalog list items html client

```
client/html/catalog/lists/items/decorators/global = Array
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
 client/html/catalog/lists/items/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/lists/items/decorators/excludes
* client/html/catalog/lists/items/decorators/local

## decorators/local

Adds a list of local decorators only to the catalog list items html client

```
client/html/catalog/lists/items/decorators/local = Array
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
("\Aimeos\Client\Html\Catalog\Decorator\*") around the html client.

```
 client/html/catalog/lists/items/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/lists/items/decorators/excludes
* client/html/catalog/lists/items/decorators/global

## name

Name of the items part used by the catalog list client implementation

```
client/html/catalog/lists/items/name = Standard
```

* Default: Standard
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Lists\Items\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## subparts

List of HTML sub-clients rendered within the catalog list items section

```
client/html/catalog/lists/items/subparts = Array
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


## template-body

Relative path to the HTML body template of the catalog list items client.

```
client/html/catalog/lists/items/template-body = catalog/lists/items-body-standard
```

* Default: catalog/lists/items-body-standard
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

It's also possible to create a specific template for each type, e.g.
for the grid, list or whatever view you want to offer your users. In
that case, you can configure the template by adding "-<type>" to the
configuration key. To configure an alternative list view template for
example, use the key

client/html/catalog/lists/items/template-body-list = catalog/lists/items-body-list.php

The argument is the relative path to the new template file. The type of
the view is determined by the "l_type" parameter (allowed characters for
the types are a-z and 0-9), which is also stored in the session so users
will keep the view during their visit. The catalog list type subpart
contains the template for switching between list types.

See also:

* client/html/catalog/lists/items/template-header
* client/html/catalog/lists/type/template-body

## template-body-list

```
client/html/catalog/lists/items/template-body-list = catalog/lists/items-body-list
```

* Default: catalog/lists/items-body-standard


## template-header

Relative path to the HTML header template of the catalog list items client.

```
client/html/catalog/lists/items/template-header = catalog/lists/items-header-standard
```

* Default: catalog/lists/items-header-standard
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

It's also possible to create a specific template for each type, e.g.
for the grid, list or whatever view you want to offer your users. In
that case, you can configure the template by adding "-<type>" to the
configuration key. To configure an alternative list view template for
example, use the key

client/html/catalog/lists/items/template-header-list = catalog/lists/items-header-list.php

The argument is the relative path to the new template file. The type of
the view is determined by the "l_type" parameter (allowed characters for
the types are a-z and 0-9), which is also stored in the session so users
will keep the view during their visit. The catalog list type subpart
contains the template for switching between list types.

See also:

* client/html/catalog/lists/items/template-body
* client/html/catalog/lists/type/template-body

# levels

Include products of sub-categories in the product list of the current category

```
client/html/catalog/lists/levels = 1
```

* Default: 1
* Type: integer - Tree level constant
* Since: 2015.11

Sometimes it may be useful to show products of sub-categories in the
current category product list, e.g. if the current category contains
no products at all or if there are only a few products in all categories.

Possible constant values for this setting are:

* 1 : Only products from the current category
* 2 : Products from the current category and the direct child categories
* 3 : Products from the current category and the whole category sub-tree

Caution: Please keep in mind that displaying products of sub-categories
can slow down your shop, especially if it contains more than a few
products! You have no real control over the positions of the products
in the result list too because all products from different categories
with the same position value are placed randomly.

Usually, a better way is to associate products to all categories they
should be listed in. This can be done manually if there are only a few
ones or during the product import automatically.

See also:

* client/html/catalog/lists/catid-default
* client/html/catalog/lists/supid-default
* client/html/catalog/lists/domains
* client/html/catalog/lists/size
* client/html/catalog/lists/sort
* client/html/catalog/lists/pages

# metatags

Adds the title, meta and link tags to the HTML header

```
client/html/catalog/lists/metatags = 1
```

* Default: 1
* Type: boolean - True to display the meta tags, false to hide it
* Since: 2017.01

By default, each instance of the catalog list component adds some HTML meta
tags to the page head section, like page title, meta keywords and description
as well as some link tags to support browser navigation. If several instances
are placed on one page, this leads to adding several title and meta tags used
by search engine. This setting enables you to suppress these tags in the page
header and maybe add your own to the page manually.

See also:

* client/html/catalog/detail/metatags

# name

Class name of the used catalog list client implementation

```
client/html/catalog/lists/name = Standard
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
 \Aimeos\Client\Html\Catalog\Lists\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Lists\Mylist
```

then you have to set the this configuration option:

```
 client/html/catalog/lists/name = Mylist
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyList"!


# pages

Maximum number of product pages shown in pagination

```
client/html/catalog/lists/pages = 100
```

* Default: 100
* Type: integer - Number of pages
* Since: 2019.04

Limits the number of product pages that are shown in the navigation.
The user is able to move to the next page (or previous one if it's not
the first) to display the next (or previous) products.

The value must be a positive integer number. Negative values are not
allowed. The value can't be overwritten per request.

See also:

* client/html/catalog/lists/catid-default
* client/html/catalog/lists/supid-default
* client/html/catalog/lists/domains
* client/html/catalog/lists/levels
* client/html/catalog/lists/sort
* client/html/catalog/lists/size

# pagination
## enable

Enables or disables pagination in list views

```
client/html/catalog/lists/pagination/enable = 1
```

* Default: 1
* Type: boolean - True for enabling, false for disabling pagination
* Since: 2019.04

Pagination is automatically hidden if there are not enough products in the
category or search result. But sometimes you don't want to show the pagination
at all, e.g. if you implement infinite scrolling by loading more results
dynamically using AJAX.


# partials
## pagination

Relative path to the pagination partial template file for catalog lists

```
client/html/catalog/lists/partials/pagination = catalog/lists/pagination-standard
```

* Default: catalog/lists/pagination-standard
* Type: string - Relative path to the template file
* Since: 2017.01

Partials are templates which are reused in other templates and generate
reoccuring blocks filled with data from the assigned values. The pagination
partial creates an HTML block containing a page browser and sorting links
if necessary.


# promo
## decorators/excludes

Excludes decorators added by the "common" option from the catalog list promo html client

```
client/html/catalog/lists/promo/decorators/excludes = 
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
 client/html/catalog/lists/promo/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/lists/promo/decorators/global
* client/html/catalog/lists/promo/decorators/local

## decorators/global

Adds a list of globally available decorators only to the catalog list promo html client

```
client/html/catalog/lists/promo/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/catalog/lists/promo/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/lists/promo/decorators/excludes
* client/html/catalog/lists/promo/decorators/local

## decorators/local

Adds a list of local decorators only to the catalog list promo html client

```
client/html/catalog/lists/promo/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Catalog\Decorator\*") around the html client.

```
 client/html/catalog/lists/promo/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/lists/promo/decorators/excludes
* client/html/catalog/lists/promo/decorators/global

## name

Name of the promotion part used by the catalog list client implementation

```
client/html/catalog/lists/promo/name = 
```

* Default: 
* Type: string - Last part of the client class name
* Since: 2014.03

Use "Myname" if your class is named "\Aimeos\Client\Html\Catalog\Lists\Promo\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## size

The maximum number of products that should be shown in the promotion section

```
client/html/catalog/lists/promo/size = 6
```

* Default: 6
* Type: integer - Number of promotion products
* Since: 2014.03

Each product list can render a list of promoted products on
top if there are any products associated to that category whose
list type is "promotion". This option limits the maximum number
of products that are displayed. It takes only effect if more
promotional products are added to this category than the set
value.


## subparts

List of HTML sub-clients rendered within the catalog list promo section

```
client/html/catalog/lists/promo/subparts = Array
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


## template-body

Relative path to the HTML body template of the catalog list promotion client.

```
client/html/catalog/lists/promo/template-body = catalog/lists/promo-body-standard
```

* Default: catalog/lists/promo-body-standard
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

It's also possible to create a specific template for each type, e.g.
for the grid, list or whatever view you want to offer your users. In
that case, you can configure the template by adding "-<type>" to the
configuration key. To configure an alternative list view template for
example, use the key

client/html/catalog/lists/promo/template-body-list = catalog/lists/promo-body-list.php

The argument is the relative path to the new template file. The type of
the view is determined by the "l_type" parameter (allowed characters for
the types are a-z and 0-9), which is also stored in the session so users
will keep the view during their visit. The catalog list type subpart
contains the template for switching between list types.

See also:

* client/html/catalog/lists/promo/template-header
* client/html/catalog/lists/type/template-body

## template-header

Relative path to the HTML header template of the catalog list promotion client.

```
client/html/catalog/lists/promo/template-header = catalog/lists/promo-header-standard
```

* Default: catalog/lists/promo-header-standard
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

It's also possible to create a specific template for each type, e.g.
for the grid, list or whatever view you want to offer your users. In
that case, you can configure the template by adding "-<type>" to the
configuration key. To configure an alternative list view template for
example, use the key

client/html/catalog/lists/promo/template-header-list = catalog/lists/promo-header-list.php

The argument is the relative path to the new template file. The type of
the view is determined by the "l_type" parameter (allowed characters for
the types are a-z and 0-9), which is also stored in the session so users
will keep the view during their visit. The catalog list type subpart
contains the template for switching between list types.

See also:

* client/html/catalog/lists/promo/template-body
* client/html/catalog/lists/type/template-body

# size

The number of products shown in a list page

```
client/html/catalog/lists/size = 48
```

* Default: 48
* Type: integer - Number of products
* Since: 2014.03

Limits the number of products that are shown in the list pages to the
given value. If more products are available, the products are split
into bunches which will be shown on their own list page. The user is
able to move to the next page (or previous one if it's not the first)
to display the next (or previous) products.

The value must be an integer number from 1 to 100. Negative values as
well as values above 100 are not allowed. The value can be overwritten
per request if the "l_size" parameter is part of the URL.

See also:

* client/html/catalog/lists/catid-default
* client/html/catalog/lists/supid-default
* client/html/catalog/lists/domains
* client/html/catalog/lists/levels
* client/html/catalog/lists/sort
* client/html/catalog/lists/pages

# sort

Default sorting of product list if no other sorting is given by parameter

```
client/html/catalog/lists/sort = relevance
```

* Default: relevance
* Type: string - Sort code "relevance", "name", "-name", "price", "-price", "ctime" or "-ctime"
* Since: 2018.07

Configures the standard sorting of products in list views. This sorting is used
as long as it's not overwritten by an URL parameter. Except "relevance", all
other sort codes can be prefixed by a "-" (minus) sign to sort the products in
a descending order. By default, the sorting is ascending.

See also:

* client/html/catalog/lists/catid-default
* client/html/catalog/lists/supid-default
* client/html/catalog/lists/domains
* client/html/catalog/lists/levels
* client/html/catalog/lists/size

# stock
## enable

Enables or disables displaying product stock levels in product list views

```
client/html/catalog/lists/stock/enable = 1
```

* Default: 1
* Type: boolean - Value of "1" to display stock levels, "0" to disable displaying them
* Since: 2014.03

This configuration option allows shop owners to display product
stock levels for each product in list views or to disable
fetching product stock information.

The stock information is fetched via AJAX and inserted via Javascript.
This allows to cache product items by leaving out such highly
dynamic content like stock levels which changes with each order.

See also:

* client/html/catalog/detail/stock/enable
* client/html/catalog/stock/url/target
* client/html/catalog/stock/url/controller
* client/html/catalog/stock/url/action
* client/html/catalog/stock/url/config

# subparts

List of HTML sub-clients rendered within the catalog list section

```
client/html/catalog/lists/subparts = Array
(
    [0] => items
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


# supid-default

The default supplier ID used if none is given as parameter

```
client/html/catalog/lists/supid-default = 
```

* Default: 
* Type: array|string - Supplier ID or IDs
* Since: 2021.01

Products in the list page can be limited to one or more suppliers.
By default, the products are not limited to any supplier until one or
more supplier IDs are passed in the URL using the f_supid parameter.
You can also configure the default supplier IDs for limiting the
products if no IDs are passed in the URL using this configuration.

See also:

* client/html/catalog/lists/sort
* client/html/catalog/lists/size
* client/html/catalog/lists/domains
* client/html/catalog/lists/levels
* client/html/catalog/lists/catid-default
* client/html/catalog/detail/prodid-default

# template-body

Relative path to the HTML body template of the catalog list client.

```
client/html/catalog/lists/template-body = catalog/lists/body-standard
```

* Default: catalog/lists/body-standard
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

It's also possible to create a specific template for each type, e.g.
for the grid, list or whatever view you want to offer your users. In
that case, you can configure the template by adding "-<type>" to the
configuration key. To configure an alternative list view template for
example, use the key

client/html/catalog/lists/template-body-list = catalog/lists/body-list.php

The argument is the relative path to the new template file. The type of
the view is determined by the "l_type" parameter (allowed characters for
the types are a-z and 0-9), which is also stored in the session so users
will keep the view during their visit. The catalog list type subpart
contains the template for switching between list types.

See also:

* client/html/catalog/lists/template-header
* client/html/catalog/lists/type/template-body

# template-header

Relative path to the HTML header template of the catalog list client.

```
client/html/catalog/lists/template-header = catalog/lists/header-standard
```

* Default: catalog/lists/header-standard
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

It's also possible to create a specific template for each type, e.g.
for the grid, list or whatever view you want to offer your users. In
that case, you can configure the template by adding "-<type>" to the
configuration key. To configure an alternative list view template for
example, use the key

client/html/catalog/lists/template-header-list = catalog/lists/header-list.php

The argument is the relative path to the new template file. The type of
the view is determined by the "l_type" parameter (allowed characters for
the types are a-z and 0-9), which is also stored in the session so users
will keep the view during their visit. The catalog list type subpart
contains the template for switching between list types.

See also:

* client/html/catalog/lists/template-body
* client/html/catalog/lists/type/template-body

# url
## action

Name of the action that should create the output

```
client/html/catalog/lists/url/action = lists
```

* Default: lists
* Type: string - Name of the action
* Since: 2014.03

In Model-View-Controller (MVC) applications, actions are the methods of a
controller that create parts of the output displayed in the generated HTML page.
Action names are usually alpha-numeric.

See also:

* client/html/catalog/lists/url/target
* client/html/catalog/lists/url/controller
* client/html/catalog/lists/url/config

## config

Associative list of configuration options used for generating the URL

```
client/html/catalog/lists/url/config = Array
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

* client/html/catalog/lists/url/target
* client/html/catalog/lists/url/controller
* client/html/catalog/lists/url/action
* client/html/url/config

## controller

Name of the controller whose action should be called

```
client/html/catalog/lists/url/controller = Catalog
```

* Default: Catalog
* Type: string - Name of the controller
* Since: 2014.03

In Model-View-Controller (MVC) applications, the controller contains the methods
that create parts of the output displayed in the generated HTML page. Controller
names are usually alpha-numeric.

See also:

* client/html/catalog/lists/url/target
* client/html/catalog/lists/url/action
* client/html/catalog/lists/url/config

## filter

```
client/html/catalog/lists/url/filter = Array
(
)
```

* Default: Array


## target

Destination of the URL where the controller specified in the URL is known

```
client/html/catalog/lists/url/target = 
```

* Default: 
* Type: string - Destination of the URL
* Since: 2014.03

The destination can be a page ID like in a content management system or the
module of a software development framework. This "target" must contain or know
the controller that should be called by the generated URL.

See also:

* client/html/catalog/lists/url/controller
* client/html/catalog/lists/url/action
* client/html/catalog/lists/url/config