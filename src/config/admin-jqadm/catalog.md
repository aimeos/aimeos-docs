
# decorators
## excludes

Excludes decorators added by the "common" option from the catalog JQAdm client

```
admin/jqadm/catalog/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2016.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/catalog/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/decorators/global
* admin/jqadm/catalog/decorators/local

## global

Adds a list of globally available decorators only to the catalog JQAdm client

```
admin/jqadm/catalog/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2016.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/catalog/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/decorators/excludes
* admin/jqadm/catalog/decorators/local

## local

Adds a list of local decorators only to the catalog JQAdm client

```
admin/jqadm/catalog/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2016.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Catalog\Decorator\*") around the JQAdm client.

```
 admin/jqadm/catalog/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Catalog\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/decorators/excludes
* admin/jqadm/catalog/decorators/global

# domains

List of domain items that should be fetched along with the catalog

```
admin/jqadm/catalog/domains = Array
(
    [media] => media
    [media/property] => media/property
    [text] => text
)
```

* Default: Array
* Type: array - List of domain names
* Since: 2016.01

If you need to display additional content, you can configure your own
list of domains (attribute, media, price, catalog, text, etc. are
domains) whose items are fetched from the storage.


# item
## config/suggest

List of suggested configuration keys in catalog item panel

```
admin/jqadm/catalog/item/config/suggest = Array
(
    [0] => css-class
)
```

* Default: Array
* Type: string - List of suggested config keys
* Since: 2017.10

Catalog items can store arbitrary key value pairs. This setting gives editors
a hint which config keys are available and are used in the templates.

See also:

* admin/jqadm/product/item/config/suggest

## media/config/suggest

List of suggested configuration keys in catalog media panel

```
admin/jqadm/catalog/item/media/config/suggest = Array
(
)
```

* Default: Array
* Type: string - List of suggested config keys
* Since: 2020.01

Item references can store arbitrary key value pairs. This setting gives
editors a hint which config keys are available and are used in the templates.


## text/config/suggest

List of suggested configuration keys in catalog text panel

```
admin/jqadm/catalog/item/text/config/suggest = Array
(
)
```

* Default: Array
* Type: string - List of suggested config keys
* Since: 2020.01

Item references can store arbitrary key value pairs. This setting gives
editors a hint which config keys are available and are used in the templates.


# media
## decorators/excludes

Excludes decorators added by the "common" option from the catalog JQAdm client

```
admin/jqadm/catalog/media/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/catalog/media/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/media/decorators/global
* admin/jqadm/catalog/media/decorators/local

## decorators/global

Adds a list of globally available decorators only to the catalog JQAdm client

```
admin/jqadm/catalog/media/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/catalog/media/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/media/decorators/excludes
* admin/jqadm/catalog/media/decorators/local

## decorators/local

Adds a list of local decorators only to the catalog JQAdm client

```
admin/jqadm/catalog/media/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Catalog\Decorator\*") around the JQAdm client.

```
 admin/jqadm/catalog/media/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Catalog\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/media/decorators/excludes
* admin/jqadm/catalog/media/decorators/global

## name

Name of the media subpart used by the JQAdm catalog implementation

```
admin/jqadm/catalog/media/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2017.07

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Catalog\Media\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## property/decorators/excludes

Excludes decorators added by the "common" option from the catalog JQAdm client

```
admin/jqadm/catalog/media/property/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/catalog/media/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/media/property/decorators/global
* admin/jqadm/catalog/media/property/decorators/local

## property/decorators/global

Adds a list of globally available decorators only to the catalog JQAdm client

```
admin/jqadm/catalog/media/property/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/catalog/media/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/media/property/decorators/excludes
* admin/jqadm/catalog/media/property/decorators/local

## property/decorators/local

Adds a list of local decorators only to the catalog JQAdm client

```
admin/jqadm/catalog/media/property/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Catalog\Decorator\*") around the JQAdm client.

```
 admin/jqadm/catalog/media/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Catalog\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/media/property/decorators/excludes
* admin/jqadm/catalog/media/property/decorators/global

## property/name

Name of the property subpart used by the JQAdm catalog media implementation

```
admin/jqadm/catalog/media/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.04

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Catalog\Media\Property\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## property/subparts

List of JQAdm sub-clients rendered within the catalog media property section

```
admin/jqadm/catalog/media/property/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2018.01

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## property/template-item

Relative path to the HTML body template of the media subpart for catalogs.

```
admin/jqadm/catalog/media/property/template-item = catalog/item-media-property-standard
```

* Default: catalog/item-media-property-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


## subparts

List of JQAdm sub-clients rendered within the catalog media section

```
admin/jqadm/catalog/media/subparts = Array
(
    [property] => property
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.07

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## template-item

Relative path to the HTML body template of the media subpart for catalogs.

```
admin/jqadm/catalog/media/template-item = catalog/item-media-standard
```

* Default: catalog/item-media-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.07

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


# name

Class name of the used account favorite client implementation

```
admin/jqadm/catalog/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2016.01

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Catalog\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Catalog\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/catalog/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


# product
## decorators/excludes

Excludes decorators added by the "common" option from the catalog JQAdm client

```
admin/jqadm/catalog/product/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/catalog/product/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/product/decorators/global
* admin/jqadm/catalog/product/decorators/local

## decorators/global

Adds a list of globally available decorators only to the catalog JQAdm client

```
admin/jqadm/catalog/product/decorators/global = Array
(
    [0] => Index
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/catalog/product/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/product/decorators/excludes
* admin/jqadm/catalog/product/decorators/local

## decorators/local

Adds a list of local decorators only to the catalog JQAdm client

```
admin/jqadm/catalog/product/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Catalog\Decorator\*") around the JQAdm client.

```
 admin/jqadm/catalog/product/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Catalog\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/product/decorators/excludes
* admin/jqadm/catalog/product/decorators/global

## fields

List of catalog list and product columns that should be displayed in the catalog product view

```
admin/jqadm/catalog/product/fields = Array
(
    [0] => catalog.lists.status
    [1] => catalog.lists.type
    [2] => catalog.lists.position
    [3] => catalog.lists.refid
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of catalog list and product columns shown by default in the
catalog product view. The columns can be changed by the editor as required
within the administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "catalog.lists.status" for the status value.


## name

Name of the product subpart used by the JQAdm catalog implementation

```
admin/jqadm/catalog/product/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2017.07

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Catalog\Product\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## subparts

List of JQAdm sub-clients rendered within the catalog product section

```
admin/jqadm/catalog/product/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.07

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The product of the JQAdm sub-clients
determines the product of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the product of the output by reproducting the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reproducting content by a fluid like
design.


## template-item

Relative path to the HTML body template of the product subpart for catalogs.

```
admin/jqadm/catalog/product/template-item = catalog/item-product-standard
```

* Default: catalog/item-product-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


# subparts

List of JQAdm sub-clients rendered within the catalog section

```
admin/jqadm/catalog/subparts = Array
(
    [media] => media
    [text] => text
    [price] => product
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2016.01

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


# template-item

Relative path to the HTML body template for the catalog item.

```
admin/jqadm/catalog/template-item = catalog/item-standard
```

* Default: catalog/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


# text
## decorators/excludes

Excludes decorators added by the "common" option from the catalog JQAdm client

```
admin/jqadm/catalog/text/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/catalog/text/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/text/decorators/global
* admin/jqadm/catalog/text/decorators/local

## decorators/global

Adds a list of globally available decorators only to the catalog JQAdm client

```
admin/jqadm/catalog/text/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/catalog/text/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/text/decorators/excludes
* admin/jqadm/catalog/text/decorators/local

## decorators/local

Adds a list of local decorators only to the catalog JQAdm client

```
admin/jqadm/catalog/text/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Catalog\Decorator\*") around the JQAdm client.

```
 admin/jqadm/catalog/text/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Catalog\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/catalog/text/decorators/excludes
* admin/jqadm/catalog/text/decorators/global

## name

Name of the text subpart used by the JQAdm catalog implementation

```
admin/jqadm/catalog/text/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2017.07

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Catalog\Text\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## subparts

List of JQAdm sub-clients rendered within the catalog text section

```
admin/jqadm/catalog/text/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.07

The output of the frontend is composed of the code generated by the JQAdm
clients. Each JQAdm client can consist of serveral (or none) sub-clients
that are responsible for rendering certain sub-parts of the output. The
sub-clients can contain JQAdm clients themselves and therefore a
hierarchical tree of JQAdm clients is composed. Each JQAdm client creates
the output that is placed inside the container of its parent.

At first, always the JQAdm code generated by the parent is printed, then
the JQAdm code of its sub-clients. The order of the JQAdm sub-clients
determines the order of the output of these sub-clients inside the parent
container. If the configured list of clients is

```
 array( "subclient1", "subclient2" )
```

you can easily change the order of the output by reordering the subparts:

```
 admin/jqadm/<clients>/subparts = array( "subclient1", "subclient2" )
```

You can also remove one or more parts if they shouldn't be rendered:

```
 admin/jqadm/<clients>/subparts = array( "subclient1" )
```

As the clients only generates structural JQAdm, the layout defined via CSS
should support adding, removing or reordering content by a fluid like
design.


## template-item

Relative path to the HTML body template of the text subpart for catalogs.

```
admin/jqadm/catalog/text/template-item = catalog/item-text-standard
```

* Default: catalog/item-text-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in admin/jqadm/templates).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.
