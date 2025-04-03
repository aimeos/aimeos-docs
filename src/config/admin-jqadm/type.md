
# decorators
## excludes

Excludes decorators added by the "common" option from the type JQAdm client

```
admin/jqadm/type/decorators/excludes = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2025.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/decorators/global
* admin/jqadm/type/decorators/local

## global

Adds a list of globally available decorators only to the type JQAdm client

```
admin/jqadm/type/decorators/global = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2025.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/decorators/excludes
* admin/jqadm/type/decorators/local

## local

Adds a list of local decorators only to the type JQAdm client

```
admin/jqadm/type/decorators/local = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2025.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Type\Decorator\*") around the JQAdm client.

```
 admin/jqadm/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Type\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/type/decorators/excludes
* admin/jqadm/type/decorators/global

# domains

List of domain names available for the items in the type JQAdm panel

```
admin/jqadm/type/domains = Array
(
    [attribute] => attribute
    [attribute/lists] => attribute/lists
    [attribute/property] => attribute/property
    [catalog/lists] => catalog/lists
    [customer/lists] => customer/lists
    [customer/property] => customer/property
    [media] => media
    [media/lists] => media/lists
    [media/property] => media/property
    [plugin] => plugin
    [price] => price
    [price/lists] => price/lists
    [price/property] => price/property
    [product] => product
    [product/lists] => product/lists
    [product/property] => product/property
    [rule] => rule
    [service] => service
    [service/lists] => service/lists
    [stock] => stock
    [tag] => tag
    [text] => text
    [text/lists] => text/lists
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of domain names
* Since: 2025.04

Type items are assigned to a domain which is used to group them and
to be able to filter the items in the JQAdm panel. The configured
domain names limits the domains in the panel to the available ones.


# fields

List of type columns that should be displayed in the list view

```
admin/jqadm/type/fields = Array
(
    [0] => type.domain
    [1] => type.status
    [2] => type.code
    [3] => type.label
)
```

* Default: 
```
Array
(
    [0] => type.domain
    [1] => type.status
    [2] => type.code
    [3] => type.label
)
```
* Type: array - List of field names, i.e. search keys
* Since: 2025.04

Changes the list of type columns shown by default in the type
list view. The columns can be changed by the editor as required within the
administraiton interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "type.id" for the type ID.


# name

Class name of the used type panel implementation

```
admin/jqadm/type/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2025.04

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Type\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/type/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


# subparts

List of JQAdm sub-clients rendered within the type section

```
admin/jqadm/type/subparts = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of sub-client names
* Since: 2025.04

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

Relative path to the HTML body template for the type item.

```
admin/jqadm/type/template-item = type/item
```

* Default: `type/item`
* Type: string - Relative path to the template creating the HTML code
* Since: 2025.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.


# template-list

Relative path to the HTML body template for the type list.

```
admin/jqadm/type/template-list = type/list
```

* Default: `type/list`
* Type: string - Relative path to the template creating the HTML code
* Since: 2025.04

The template file contains the HTML code and processing instructions
to generate the result shown in the body of the frontend. The
configuration string is the path to the template file relative
to the templates directory (usually in templates/admin/jqadm).

You can overwrite the template file configuration in extensions and
provide alternative templates. These alternative templates should be
named like the default one but with the string "default" replaced by
an unique name. You may use the name of your project for this. If
you've implemented an alternative client class as well, "default"
should be replaced by the name of the new class.
