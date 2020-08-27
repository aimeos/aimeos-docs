
# attribute
## decorators/excludes

Excludes decorators added by the "common" option from the type JQAdm client

```
admin/jqadm/type/attribute/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/attribute/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/attribute/decorators/global
* admin/jqadm/type/attribute/decorators/local

## decorators/global

Adds a list of globally available decorators only to the type JQAdm client

```
admin/jqadm/type/attribute/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/attribute/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/attribute/decorators/excludes
* admin/jqadm/type/attribute/decorators/local

## decorators/local

Adds a list of local decorators only to the type JQAdm client

```
admin/jqadm/type/attribute/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Type\Attribute\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/attribute/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Type\Attribute\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/attribute/decorators/excludes
* admin/jqadm/type/attribute/decorators/global

## fields

List of attribute type columns that should be displayed in the list view

```
admin/jqadm/type/attribute/fields = Array
(
    [0] => attribute.type.domain
    [1] => attribute.type.status
    [2] => attribute.type.code
    [3] => attribute.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of attribute type columns shown by default in the attribute type
list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "attribute.type.id" for the attribute type ID.


## lists/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/attribute/lists/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/attribute/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/attribute/lists/decorators/global
* admin/jqadm/type/attribute/lists/decorators/local

## lists/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/attribute/lists/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/attribute/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/attribute/lists/decorators/excludes
* admin/jqadm/type/attribute/lists/decorators/local

## lists/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/attribute/lists/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Attribute\Liststype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/attribute/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Attribute\Liststype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/attribute/lists/decorators/excludes
* admin/jqadm/type/attribute/lists/decorators/global

## lists/fields

List of attribute list type columns that should be displayed in the list view

```
admin/jqadm/type/attribute/lists/fields = Array
(
    [0] => attribute.lists.type.domain
    [1] => attribute.lists.type.status
    [2] => attribute.lists.type.code
    [3] => attribute.lists.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of attribute list type columns shown by default in the attribute
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "attribute.lists.type.id" for the attribute type ID.


## lists/name

Class name of the used account favorite client implementation

```
admin/jqadm/type/attribute/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Attribute\Liststype\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Attribute\Liststype\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/attribute/lists/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## lists/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/attribute/lists/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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


## lists/template-item

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/attribute/lists/template-item = type/attribute/lists/item-standard
```

* Default: type/attribute/lists/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## lists/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/attribute/lists/template-list = type/attribute/lists/list-standard
```

* Default: type/attribute/lists/list-standard
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


## name

Class name of the used account favorite client implementation

```
admin/jqadm/type/attribute/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Type\Attribute\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Type\Attribute\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/attribute/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## property/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/attribute/property/decorators/excludes = Array
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

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/attribute/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/attribute/property/decorators/global
* admin/jqadm/type/attribute/property/decorators/local

## property/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/attribute/property/decorators/global = Array
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
 admin/jqadm/type/attribute/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/attribute/property/decorators/excludes
* admin/jqadm/type/attribute/property/decorators/local

## property/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/attribute/property/decorators/local = Array
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
("\Aimeos\Admin\JQAdm\Attribute\Propertytype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/attribute/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Attribute\Propertytype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/attribute/property/decorators/excludes
* admin/jqadm/type/attribute/property/decorators/global

## property/fields

List of attribute list type columns that should be displayed in the list view

```
admin/jqadm/type/attribute/property/fields = Array
(
    [0] => attribute.property.type.domain
    [1] => attribute.property.type.status
    [2] => attribute.property.type.code
    [3] => attribute.property.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of attribute list type columns shown by default in the attribute
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "attribute.property.type.id" for the attribute type ID.


## property/name

Class name of the used account favorite client implementation

```
admin/jqadm/type/attribute/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.01

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Attribute\Propertytype\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Attribute\Propertytype\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/attribute/property/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## property/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/attribute/property/standard/subparts = Array
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

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/attribute/property/template-item = type/attribute/property/item-standard
```

* Default: type/attribute/property/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2018.01

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


## property/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/attribute/property/template-list = type/attribute/property/list-standard
```

* Default: type/attribute/property/list-standard
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


## standard/subparts

List of JQAdm sub-clients rendered within the type section

```
admin/jqadm/type/attribute/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the type item.

```
admin/jqadm/type/attribute/template-item = type/attribute/item-standard
```

* Default: type/attribute/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## template-list

Relative path to the HTML body template for the type list.

```
admin/jqadm/type/attribute/template-list = type/attribute/list-standard
```

* Default: type/attribute/list-standard
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


# catalog
## lists/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/catalog/lists/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/catalog/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/catalog/lists/decorators/global
* admin/jqadm/type/catalog/lists/decorators/local

## lists/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/catalog/lists/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/catalog/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/catalog/lists/decorators/excludes
* admin/jqadm/type/catalog/lists/decorators/local

## lists/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/catalog/lists/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Catalog\Liststype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/catalog/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Catalog\Liststype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/catalog/lists/decorators/excludes
* admin/jqadm/type/catalog/lists/decorators/global

## lists/fields

List of catalog list type columns that should be displayed in the list view

```
admin/jqadm/type/catalog/lists/fields = Array
(
    [0] => catalog.lists.type.domain
    [1] => catalog.lists.type.status
    [2] => catalog.lists.type.code
    [3] => catalog.lists.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of catalog list type columns shown by default in the catalog
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "catalog.lists.type.id" for the catalog type ID.


## lists/name

Class name of the used account favorite client implementation

```
admin/jqadm/type/catalog/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Catalog\Liststype\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Catalog\Liststype\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/catalog/lists/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## lists/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/catalog/lists/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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


## lists/template-item

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/catalog/lists/template-item = type/catalog/lists/item-standard
```

* Default: type/catalog/lists/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## lists/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/catalog/lists/template-list = type/catalog/lists/list-standard
```

* Default: type/catalog/lists/list-standard
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


# customer
## lists/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/customer/lists/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/customer/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/customer/lists/decorators/global
* admin/jqadm/type/customer/lists/decorators/local

## lists/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/customer/lists/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/customer/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/customer/lists/decorators/excludes
* admin/jqadm/type/customer/lists/decorators/local

## lists/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/customer/lists/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Customer\Liststype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/customer/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Customer\Liststype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/customer/lists/decorators/excludes
* admin/jqadm/type/customer/lists/decorators/global

## lists/fields

List of customer list type columns that should be displayed in the list view

```
admin/jqadm/type/customer/lists/fields = Array
(
    [0] => customer.lists.type.domain
    [1] => customer.lists.type.status
    [2] => customer.lists.type.code
    [3] => customer.lists.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of customer list type columns shown by default in the customer
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "customer.lists.type.id" for the customer type ID.


## lists/name

Class name of the used account favorite client implementation

```
admin/jqadm/type/customer/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Customer\Liststype\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Customer\Liststype\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/customer/lists/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## lists/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/customer/lists/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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


## lists/template-item

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/customer/lists/template-item = type/customer/lists/item-standard
```

* Default: type/customer/lists/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## lists/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/customer/lists/template-list = type/customer/lists/list-standard
```

* Default: type/customer/lists/list-standard
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


## property/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/customer/property/decorators/excludes = Array
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

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/customer/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/customer/property/decorators/global
* admin/jqadm/type/customer/property/decorators/local

## property/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/customer/property/decorators/global = Array
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
 admin/jqadm/type/customer/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/customer/property/decorators/excludes
* admin/jqadm/type/customer/property/decorators/local

## property/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/customer/property/decorators/local = Array
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
("\Aimeos\Admin\JQAdm\Customer\Propertytype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/customer/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Customer\Propertytype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/customer/property/decorators/excludes
* admin/jqadm/type/customer/property/decorators/global

## property/fields

List of customer list type columns that should be displayed in the list view

```
admin/jqadm/type/customer/property/fields = Array
(
    [0] => customer.property.type.domain
    [1] => customer.property.type.status
    [2] => customer.property.type.code
    [3] => customer.property.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of customer list type columns shown by default in the customer
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "customer.property.type.id" for the customer type ID.


## property/name

Class name of the used account favorite client implementation

```
admin/jqadm/type/customer/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.01

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Customer\Propertytype\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Customer\Propertytype\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/customer/property/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## property/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/customer/property/standard/subparts = Array
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

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/customer/property/template-item = type/customer/property/item-standard
```

* Default: type/customer/property/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2018.01

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


## property/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/customer/property/template-list = type/customer/property/list-standard
```

* Default: type/customer/property/list-standard
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


# media
## decorators/excludes

Excludes decorators added by the "common" option from the type JQAdm client

```
admin/jqadm/type/media/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/media/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/media/decorators/global
* admin/jqadm/type/media/decorators/local

## decorators/global

Adds a list of globally available decorators only to the type JQAdm client

```
admin/jqadm/type/media/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/media/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/media/decorators/excludes
* admin/jqadm/type/media/decorators/local

## decorators/local

Adds a list of local decorators only to the type JQAdm client

```
admin/jqadm/type/media/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Type\Media\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/media/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Type\Media\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/media/decorators/excludes
* admin/jqadm/type/media/decorators/global

## fields

List of media type columns that should be displayed in the list view

```
admin/jqadm/type/media/fields = Array
(
    [0] => media.type.domain
    [1] => media.type.status
    [2] => media.type.code
    [3] => media.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of media type columns shown by default in the media type
list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "media.type.id" for the media type ID.


## lists/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/media/lists/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/media/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/media/lists/decorators/global
* admin/jqadm/type/media/lists/decorators/local

## lists/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/media/lists/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/media/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/media/lists/decorators/excludes
* admin/jqadm/type/media/lists/decorators/local

## lists/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/media/lists/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Media\Liststype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/media/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Media\Liststype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/media/lists/decorators/excludes
* admin/jqadm/type/media/lists/decorators/global

## lists/fields

List of media list type columns that should be displayed in the list view

```
admin/jqadm/type/media/lists/fields = Array
(
    [0] => media.lists.type.domain
    [1] => media.lists.type.status
    [2] => media.lists.type.code
    [3] => media.lists.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of media list type columns shown by default in the media
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "media.lists.type.id" for the media type ID.


## lists/name

Class name of the used account favorite client implementation

```
admin/jqadm/type/media/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Media\Liststype\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Media\Liststype\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/media/lists/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## lists/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/media/lists/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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


## lists/template-item

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/media/lists/template-item = type/media/lists/item-standard
```

* Default: type/media/lists/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## lists/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/media/lists/template-list = type/media/lists/list-standard
```

* Default: type/media/lists/list-standard
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


## name

Class name of the used account favorite client implementation

```
admin/jqadm/type/media/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Type\Media\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Type\Media\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/media/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## property/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/media/property/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/media/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/media/property/decorators/global
* admin/jqadm/type/media/property/decorators/local

## property/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/media/property/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/media/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/media/property/decorators/excludes
* admin/jqadm/type/media/property/decorators/local

## property/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/media/property/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Media\Propertytype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/media/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Media\Propertytype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/media/property/decorators/excludes
* admin/jqadm/type/media/property/decorators/global

## property/fields

List of media list type columns that should be displayed in the list view

```
admin/jqadm/type/media/property/fields = Array
(
    [0] => media.property.type.domain
    [1] => media.property.type.status
    [2] => media.property.type.code
    [3] => media.property.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of media list type columns shown by default in the media
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "media.property.type.id" for the media type ID.


## property/name

Class name of the used account favorite client implementation

```
admin/jqadm/type/media/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Media\Propertytype\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Media\Propertytype\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/media/property/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## property/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/media/property/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/media/property/template-item = type/media/property/item-standard
```

* Default: type/media/property/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## property/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/media/property/template-list = type/media/property/list-standard
```

* Default: type/media/property/list-standard
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


## standard/subparts

List of JQAdm sub-clients rendered within the type section

```
admin/jqadm/type/media/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the type item.

```
admin/jqadm/type/media/template-item = type/media/item-standard
```

* Default: type/media/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## template-list

Relative path to the HTML body template for the type list.

```
admin/jqadm/type/media/template-list = type/media/list-standard
```

* Default: type/media/list-standard
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


# plugin
## decorators/excludes

Excludes decorators added by the "common" option from the type JQAdm client

```
admin/jqadm/type/plugin/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/plugin/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/plugin/decorators/global
* admin/jqadm/type/plugin/decorators/local

## decorators/global

Adds a list of globally available decorators only to the type JQAdm client

```
admin/jqadm/type/plugin/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/plugin/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/plugin/decorators/excludes
* admin/jqadm/type/plugin/decorators/local

## decorators/local

Adds a list of local decorators only to the type JQAdm client

```
admin/jqadm/type/plugin/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Type\Plugin\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/plugin/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Type\Plugin\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/plugin/decorators/excludes
* admin/jqadm/type/plugin/decorators/global

## fields

List of plugin type columns that should be displayed in the list view

```
admin/jqadm/type/plugin/fields = Array
(
    [0] => plugin.type.domain
    [1] => plugin.type.status
    [2] => plugin.type.code
    [3] => plugin.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of plugin type columns shown by default in the plugin type
list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "plugin.type.id" for the plugin type ID.


## name

Class name of the used account favorite client implementation

```
admin/jqadm/type/plugin/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Type\Plugin\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Type\Plugin\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/plugin/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## standard/subparts

List of JQAdm sub-clients rendered within the type section

```
admin/jqadm/type/plugin/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the type item.

```
admin/jqadm/type/plugin/template-item = type/plugin/item-standard
```

* Default: type/plugin/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## template-list

Relative path to the HTML body template for the type list.

```
admin/jqadm/type/plugin/template-list = type/plugin/list-standard
```

* Default: type/plugin/list-standard
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


# price
## decorators/excludes

Excludes decorators added by the "common" option from the type JQAdm client

```
admin/jqadm/type/price/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/price/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/price/decorators/global
* admin/jqadm/type/price/decorators/local

## decorators/global

Adds a list of globally available decorators only to the type JQAdm client

```
admin/jqadm/type/price/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/price/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/price/decorators/excludes
* admin/jqadm/type/price/decorators/local

## decorators/local

Adds a list of local decorators only to the type JQAdm client

```
admin/jqadm/type/price/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Type\Price\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/price/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Type\Price\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/price/decorators/excludes
* admin/jqadm/type/price/decorators/global

## fields

List of price type columns that should be displayed in the list view

```
admin/jqadm/type/price/fields = Array
(
    [0] => price.type.domain
    [1] => price.type.status
    [2] => price.type.code
    [3] => price.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of price type columns shown by default in the price type
list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "price.type.id" for the price type ID.


## lists/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/price/lists/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/price/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/price/lists/decorators/global
* admin/jqadm/type/price/lists/decorators/local

## lists/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/price/lists/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/price/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/price/lists/decorators/excludes
* admin/jqadm/type/price/lists/decorators/local

## lists/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/price/lists/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Price\Liststype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/price/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Price\Liststype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/price/lists/decorators/excludes
* admin/jqadm/type/price/lists/decorators/global

## lists/fields

List of price list type columns that should be displayed in the list view

```
admin/jqadm/type/price/lists/fields = Array
(
    [0] => price.lists.type.domain
    [1] => price.lists.type.status
    [2] => price.lists.type.code
    [3] => price.lists.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of price list type columns shown by default in the price
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "price.lists.type.id" for the price type ID.


## lists/name

Class name of the used account favorite client implementation

```
admin/jqadm/type/price/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Price\Liststype\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Price\Liststype\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/price/lists/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## lists/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/price/lists/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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


## lists/template-item

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/price/lists/template-item = type/price/lists/item-standard
```

* Default: type/price/lists/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## lists/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/price/lists/template-list = type/price/lists/list-standard
```

* Default: type/price/lists/list-standard
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


## name

Class name of the used account favorite client implementation

```
admin/jqadm/type/price/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Type\Price\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Type\Price\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/price/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## property/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/price/property/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/price/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/price/property/decorators/global
* admin/jqadm/type/price/property/decorators/local

## property/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/price/property/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/price/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/price/property/decorators/excludes
* admin/jqadm/type/price/property/decorators/local

## property/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/price/property/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Price\Propertytype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/price/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Price\Propertytype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/price/property/decorators/excludes
* admin/jqadm/type/price/property/decorators/global

## property/fields

List of price list type columns that should be displayed in the list view

```
admin/jqadm/type/price/property/fields = Array
(
    [0] => price.property.type.domain
    [1] => price.property.type.status
    [2] => price.property.type.code
    [3] => price.property.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of price list type columns shown by default in the price
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "price.property.type.id" for the price type ID.


## property/name

Class name of the used account favorite client implementation

```
admin/jqadm/type/price/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Price\Propertytype\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Price\Propertytype\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/price/property/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## property/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/price/property/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/price/property/template-item = type/price/property/item-standard
```

* Default: type/price/property/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## property/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/price/property/template-list = type/price/property/list-standard
```

* Default: type/price/property/list-standard
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


## standard/subparts

List of JQAdm sub-clients rendered within the type section

```
admin/jqadm/type/price/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the type item.

```
admin/jqadm/type/price/template-item = type/price/item-standard
```

* Default: type/price/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## template-list

Relative path to the HTML body template for the type list.

```
admin/jqadm/type/price/template-list = type/price/list-standard
```

* Default: type/price/list-standard
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


# product
## decorators/excludes

Excludes decorators added by the "common" option from the type JQAdm client

```
admin/jqadm/type/product/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/product/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/product/decorators/global
* admin/jqadm/type/product/decorators/local

## decorators/global

Adds a list of globally available decorators only to the type JQAdm client

```
admin/jqadm/type/product/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/product/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/product/decorators/excludes
* admin/jqadm/type/product/decorators/local

## decorators/local

Adds a list of local decorators only to the type JQAdm client

```
admin/jqadm/type/product/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Type\Product\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/product/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Type\Product\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/product/decorators/excludes
* admin/jqadm/type/product/decorators/global

## fields

List of product type columns that should be displayed in the list view

```
admin/jqadm/type/product/fields = Array
(
    [0] => product.type.domain
    [1] => product.type.status
    [2] => product.type.code
    [3] => product.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of product type columns shown by default in the product type
list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "product.type.id" for the product type ID.


## lists/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/product/lists/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/product/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/product/lists/decorators/global
* admin/jqadm/type/product/lists/decorators/local

## lists/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/product/lists/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/product/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/product/lists/decorators/excludes
* admin/jqadm/type/product/lists/decorators/local

## lists/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/product/lists/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Product\Liststype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/product/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Product\Liststype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/product/lists/decorators/excludes
* admin/jqadm/type/product/lists/decorators/global

## lists/fields

List of product list type columns that should be displayed in the list view

```
admin/jqadm/type/product/lists/fields = Array
(
    [0] => product.lists.type.domain
    [1] => product.lists.type.status
    [2] => product.lists.type.code
    [3] => product.lists.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of product list type columns shown by default in the product
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "product.lists.type.id" for the product type ID.


## lists/name

Class name of the used account favorite client implementation

```
admin/jqadm/type/product/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Product\Liststype\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Product\Liststype\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/product/lists/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## lists/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/product/lists/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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


## lists/template-item

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/product/lists/template-item = type/product/lists/item-standard
```

* Default: type/product/lists/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## lists/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/product/lists/template-list = type/product/lists/list-standard
```

* Default: type/product/lists/list-standard
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


## name

Class name of the used account favorite client implementation

```
admin/jqadm/type/product/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Type\Product\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Type\Product\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/product/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## property/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/product/property/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/product/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/product/property/decorators/global
* admin/jqadm/type/product/property/decorators/local

## property/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/product/property/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/product/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/product/property/decorators/excludes
* admin/jqadm/type/product/property/decorators/local

## property/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/product/property/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Product\Liststype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/product/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Product\Liststype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/product/property/decorators/excludes
* admin/jqadm/type/product/property/decorators/global

## property/fields

List of product list type columns that should be displayed in the list view

```
admin/jqadm/type/product/property/fields = Array
(
    [0] => product.property.type.domain
    [1] => product.property.type.status
    [2] => product.property.type.code
    [3] => product.property.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of product list type columns shown by default in the product
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "product.property.type.id" for the product type ID.


## property/name

Class name of the used account favorite client implementation

```
admin/jqadm/type/product/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Product\Liststype\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Product\Liststype\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/product/property/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## property/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/product/property/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/product/property/template-item = type/product/property/item-standard
```

* Default: type/product/property/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## property/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/product/property/template-list = type/product/property/list-standard
```

* Default: type/product/property/list-standard
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


## standard/subparts

List of JQAdm sub-clients rendered within the type section

```
admin/jqadm/type/product/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the type item.

```
admin/jqadm/type/product/template-item = type/product/item-standard
```

* Default: type/product/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## template-list

Relative path to the HTML body template for the type list.

```
admin/jqadm/type/product/template-list = type/product/list-standard
```

* Default: type/product/list-standard
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


# service
## decorators/excludes

Excludes decorators added by the "common" option from the type JQAdm client

```
admin/jqadm/type/service/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/service/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/service/decorators/global
* admin/jqadm/type/service/decorators/local

## decorators/global

Adds a list of globally available decorators only to the type JQAdm client

```
admin/jqadm/type/service/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/service/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/service/decorators/excludes
* admin/jqadm/type/service/decorators/local

## decorators/local

Adds a list of local decorators only to the type JQAdm client

```
admin/jqadm/type/service/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Type\Service\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/service/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Type\Service\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/service/decorators/excludes
* admin/jqadm/type/service/decorators/global

## fields

List of service type columns that should be displayed in the list view

```
admin/jqadm/type/service/fields = Array
(
    [0] => service.type.domain
    [1] => service.type.status
    [2] => service.type.code
    [3] => service.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of service type columns shown by default in the service type
list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "service.type.id" for the service type ID.


## lists/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/service/lists/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/service/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/service/lists/decorators/global
* admin/jqadm/type/service/lists/decorators/local

## lists/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/service/lists/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/service/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/service/lists/decorators/excludes
* admin/jqadm/type/service/lists/decorators/local

## lists/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/service/lists/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Service\Liststype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/service/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Service\Liststype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/service/lists/decorators/excludes
* admin/jqadm/type/service/lists/decorators/global

## lists/fields

List of service list type columns that should be displayed in the list view

```
admin/jqadm/type/service/lists/fields = Array
(
    [0] => service.lists.type.domain
    [1] => service.lists.type.status
    [2] => service.lists.type.code
    [3] => service.lists.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of service list type columns shown by default in the service
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "service.lists.type.id" for the service type ID.


## lists/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/service/lists/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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


## lists/template-item

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/service/lists/template-item = type/service/lists/item-standard
```

* Default: type/service/lists/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## lists/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/service/lists/template-list = type/service/lists/list-standard
```

* Default: type/service/lists/list-standard
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


## name

Class name of the used account favorite client implementation

```
admin/jqadm/type/service/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Type\Service\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Type\Service\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/service/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## standard/subparts

List of JQAdm sub-clients rendered within the type section

```
admin/jqadm/type/service/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the type item.

```
admin/jqadm/type/service/template-item = type/service/item-standard
```

* Default: type/service/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## template-list

Relative path to the HTML body template for the type list.

```
admin/jqadm/type/service/template-list = type/service/list-standard
```

* Default: type/service/list-standard
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


# stock
## decorators/excludes

Excludes decorators added by the "common" option from the type JQAdm client

```
admin/jqadm/type/stock/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/stock/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/stock/decorators/global
* admin/jqadm/type/stock/decorators/local

## decorators/global

Adds a list of globally available decorators only to the type JQAdm client

```
admin/jqadm/type/stock/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/stock/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/stock/decorators/excludes
* admin/jqadm/type/stock/decorators/local

## decorators/local

Adds a list of local decorators only to the type JQAdm client

```
admin/jqadm/type/stock/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Type\Stock\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/stock/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Type\Stock\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/stock/decorators/excludes
* admin/jqadm/type/stock/decorators/global

## fields

List of stock type columns that should be displayed in the list view

```
admin/jqadm/type/stock/fields = Array
(
    [0] => stock.type.domain
    [1] => stock.type.status
    [2] => stock.type.code
    [3] => stock.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of stock type columns shown by default in the stock type
list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "stock.type.id" for the stock type ID.


## name

Class name of the used account favorite client implementation

```
admin/jqadm/type/stock/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Type\Stock\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Type\Stock\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/stock/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## standard/subparts

List of JQAdm sub-clients rendered within the type section

```
admin/jqadm/type/stock/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the type item.

```
admin/jqadm/type/stock/template-item = type/stock/item-standard
```

* Default: type/stock/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## template-list

Relative path to the HTML body template for the type list.

```
admin/jqadm/type/stock/template-list = type/stock/list-standard
```

* Default: type/stock/list-standard
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


# tag
## decorators/excludes

Excludes decorators added by the "common" option from the type JQAdm client

```
admin/jqadm/type/tag/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/tag/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/tag/decorators/global
* admin/jqadm/type/tag/decorators/local

## decorators/global

Adds a list of globally available decorators only to the type JQAdm client

```
admin/jqadm/type/tag/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/tag/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/tag/decorators/excludes
* admin/jqadm/type/tag/decorators/local

## decorators/local

Adds a list of local decorators only to the type JQAdm client

```
admin/jqadm/type/tag/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Type\Tag\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/tag/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Type\Tag\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/tag/decorators/excludes
* admin/jqadm/type/tag/decorators/global

## fields

List of tag type columns that should be displayed in the list view

```
admin/jqadm/type/tag/fields = Array
(
    [0] => tag.type.domain
    [1] => tag.type.status
    [2] => tag.type.code
    [3] => tag.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of tag type columns shown by default in the tag type
list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "tag.type.id" for the tag type ID.


## name

Class name of the used account favorite client implementation

```
admin/jqadm/type/tag/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Type\Tag\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Type\Tag\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/tag/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## standard/subparts

List of JQAdm sub-clients rendered within the type section

```
admin/jqadm/type/tag/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the type item.

```
admin/jqadm/type/tag/template-item = type/tag/item-standard
```

* Default: type/tag/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## template-list

Relative path to the HTML body template for the type list.

```
admin/jqadm/type/tag/template-list = type/tag/list-standard
```

* Default: type/tag/list-standard
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

Excludes decorators added by the "common" option from the type JQAdm client

```
admin/jqadm/type/text/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/text/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/text/decorators/global
* admin/jqadm/type/text/decorators/local

## decorators/global

Adds a list of globally available decorators only to the type JQAdm client

```
admin/jqadm/type/text/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/text/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/text/decorators/excludes
* admin/jqadm/type/text/decorators/local

## decorators/local

Adds a list of local decorators only to the type JQAdm client

```
admin/jqadm/type/text/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Type\Text\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/text/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Type\Text\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/text/decorators/excludes
* admin/jqadm/type/text/decorators/global

## fields

List of text type columns that should be displayed in the list view

```
admin/jqadm/type/text/fields = Array
(
    [0] => text.type.domain
    [1] => text.type.status
    [2] => text.type.code
    [3] => text.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of text type columns shown by default in the text type
list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "text.type.id" for the text type ID.


## lists/decorators/excludes

Excludes decorators added by the "common" option from the list type JQAdm client

```
admin/jqadm/type/text/lists/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/text/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/text/lists/decorators/global
* admin/jqadm/type/text/lists/decorators/local

## lists/decorators/global

Adds a list of globally available decorators only to the list type JQAdm client

```
admin/jqadm/type/text/lists/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/text/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/text/lists/decorators/excludes
* admin/jqadm/type/text/lists/decorators/local

## lists/decorators/local

Adds a list of local decorators only to the list type JQAdm client

```
admin/jqadm/type/text/lists/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Text\Liststype\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/text/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Text\Liststype\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/text/lists/decorators/excludes
* admin/jqadm/type/text/lists/decorators/global

## lists/fields

List of text list type columns that should be displayed in the list view

```
admin/jqadm/type/text/lists/fields = Array
(
    [0] => text.lists.type.domain
    [1] => text.lists.type.status
    [2] => text.lists.type.code
    [3] => text.lists.type.label
)
```

* Default: Array
* Type: array - List of field names, i.e. search keys
* Since: 2017.10

Changes the list of text list type columns shown by default in the text
list type list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "text.lists.type.id" for the text type ID.


## lists/standard/subparts

List of JQAdm sub-clients rendered within the list type section

```
admin/jqadm/type/text/lists/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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


## lists/template-item

Relative path to the HTML body template for the list type item.

```
admin/jqadm/type/text/lists/template-item = type/text/lists/item-standard
```

* Default: type/text/lists/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## lists/template-list

Relative path to the HTML body template for the list type list.

```
admin/jqadm/type/text/lists/template-list = type/text/lists/list-standard
```

* Default: type/text/lists/list-standard
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


## name

Class name of the used account favorite client implementation

```
admin/jqadm/type/text/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Type\Text\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Type\Text\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/text/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


## standard/subparts

List of JQAdm sub-clients rendered within the type section

```
admin/jqadm/type/text/standard/subparts = Array
(
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2017.10

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

Relative path to the HTML body template for the type item.

```
admin/jqadm/type/text/template-item = type/text/item-standard
```

* Default: type/text/item-standard
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.10

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


## template-list

Relative path to the HTML body template for the type list.

```
admin/jqadm/type/text/template-list = type/text/list-standard
```

* Default: type/text/list-standard
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
