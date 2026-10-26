
# cms/page

All parameters defined for the cms page component and its subparts

```
client/html/cms/page = 
```

* Type: array - Associative list of name/value settings

This returns all settings related to the page component.
Please refer to the single settings for pages.


# basket-add

Display the "add to basket" button for each product item

```
client/html/cms/page/basket-add = 
```

* Type: boolean - True to display the button, false to hide it
* Since: 2021.07

Enables the button for adding products to the basket for the products in CMS
pages. This works for all type of products, even for selection products
with product variants and product bundles. By default, also optional attributes
are displayed if they have been associated to a product.

To fetch the variant articles of selection products too, add this setting to
your configuration:

mshop/common/manager/maxdepth = 3

See also:

* client/html/catalog/home/basket-add
* client/html/catalog/lists/basket-add
* client/html/catalog/detail/basket-add
* client/html/catalog/product/basket-add
* client/html/basket/related/basket-add

# cache

Enables or disables caching only for the cms page component

```
client/html/cms/page/cache = 
```

* Type: boolean - True to enable caching, false to disable

Disable caching for components can be useful if you would have too much
entries to cache or if the component contains non-cacheable parts that
can't be replaced using the modify() method.

See also:

* client/html/cms/page/cache

# decorators
## excludes

Excludes decorators added by the "common" option from the cms page html client

```
client/html/cms/page/decorators/excludes = 
```

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/cms/page/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/cms/page/decorators/global
* client/html/cms/page/decorators/local

## global

Adds a list of globally available decorators only to the cms page html client

```
client/html/cms/page/decorators/global = 
```

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/cms/page/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/cms/page/decorators/excludes
* client/html/cms/page/decorators/local

## local

Adds a list of local decorators only to the cms page html client

```
client/html/cms/page/decorators/local = 
```

* Type: array - List of decorator names
* Since: 2021.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Cms\Decorator\*") around the html client.

```
 client/html/cms/page/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Cms\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/cms/page/decorators/excludes
* client/html/cms/page/decorators/global

# domains

A list of domain names whose items should be available in the cms page view template

```
client/html/cms/page/domains = 
```

* Type: array - List of domain names
* Since: 2021.04

The templates rendering the cms page section use the texts and
maybe images and attributes associated to the categories. You can
configure your own list of domains (attribute, media, price, product,
text, etc. are domains) whose items are fetched from the storage.
Please keep in mind that the more domains you add to the configuration,
the more time is required for fetching the content!


# metatags

Adds the title, meta and link tags to the HTML header

```
client/html/cms/page/metatags = 
```

* Type: boolean - True to display the meta tags, false to hide it
* Since: 2021.01

By default, each instance of the cms list component adds some HTML meta
tags to the page head section, like page title, meta keywords and description
as well as some link tags to support browser navigation. If several instances
are placed on one page, this leads to adding several title and meta tags used
by search engine. This setting enables you to suppress these tags in the page
header and maybe add your own to the page manually.


# name

Class name of the used cms page client implementation

```
client/html/cms/page/name = 
```

* Type: string - Last part of the class name
* Since: 2021.04

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Cms\Page\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Cms\Page\Mypage
```

then you have to set the this configuration option:

```
 client/html/cms/page/name = Mypage
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyPage"!


# subparts

List of HTML sub-clients rendered within the cms page section

```
client/html/cms/page/subparts = 
```

* Type: array - List of sub-client names
* Since: 2021.04

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

Relative path to the HTML body template of the cms page client.

```
client/html/cms/page/template-body = 
```

* Type: string - Relative path to the template creating code for the HTML page body
* Since: 2021.04

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

* client/html/cms/page/template-header

# template-cataloglist

Relative path to the HTML template of the page catalog list client.

```
client/html/cms/page/template-cataloglist = 
```

* Type: string - Relative path to the template creating code for the catalog list
* Since: 2021.07

The template file contains the HTML code and processing instructions
to generate the HTML code that is inserted into the HTML page
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

* client/html/cms/page/template-body
* client/html/cms/page/template-header

# template-header

Relative path to the HTML header template of the cms page client.

```
client/html/cms/page/template-header = 
```

* Type: string - Relative path to the template creating code for the HTML page head
* Since: 2021.04

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

* client/html/cms/page/template-body