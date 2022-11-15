
# decorators
## excludes

Excludes decorators added by the "common" option from the attribute JQAdm client

```
admin/jqadm/attribute/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/attribute/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/decorators/global
* admin/jqadm/attribute/decorators/local

## global

Adds a list of globally available decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/decorators/excludes
* admin/jqadm/attribute/decorators/local

## local

Adds a list of local decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Attribute\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Attribute\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/decorators/excludes
* admin/jqadm/attribute/decorators/global

# domains

List of domain items that should be fetched along with the attribute

```
admin/jqadm/attribute/domains = Array
(
    [attribute/property] => attribute/property
    [media] => media
    [media/property] => media/property
    [price] => price
    [price/property] => price/property
    [text] => text
)
```

* Default: Array
(
)

* Type: array - List of domain names
* Since: 2017.07

If you need to display additional content, you can configure your own
list of domains (attribute, media, price, attribute, text, etc. are
domains) whose items are fetched from the storage.


# fields

List of attribute columns that should be displayed in the list view

```
admin/jqadm/attribute/fields = Array
(
    [0] => attribute.status
    [1] => attribute.type
    [2] => attribute.code
    [3] => attribute.label
)
```

* Default: Array
(
    [0] => attribute.status
    [1] => attribute.type
    [2] => attribute.code
    [3] => attribute.label
)

* Type: array - List of field names, i.e. search keys
* Since: 2017.07

Changes the list of attribute columns shown by default in the attribute list view.
The columns can be changed by the editor as required within the administraiton
interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "attribute.id" for the attribute ID.


# item
## media/config/suggest

List of suggested configuration keys in attribute media panel

```
admin/jqadm/attribute/item/media/config/suggest = Array
(
)
```

* Default: Array
(
)

* Type: string - List of suggested config keys
* Since: 2020.01

Item references can store arbitrary key value pairs. This setting gives
editors a hint which config keys are available and are used in the templates.


## price/config/suggest

List of suggested configuration keys in attribute price panel

```
admin/jqadm/attribute/item/price/config/suggest = Array
(
)
```

* Default: Array
(
)

* Type: string - List of suggested config keys
* Since: 2020.01

Item references can store arbitrary key value pairs. This setting gives
editors a hint which config keys are available and are used in the templates.


## text/config/suggest

List of suggested configuration keys in attribute text panel

```
admin/jqadm/attribute/item/text/config/suggest = Array
(
)
```

* Default: Array
(
)

* Type: string - List of suggested config keys
* Since: 2020.01

Item references can store arbitrary key value pairs. This setting gives
editors a hint which config keys are available and are used in the templates.


# media
## decorators/excludes

Excludes decorators added by the "common" option from the attribute JQAdm client

```
admin/jqadm/attribute/media/decorators/excludes =
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
 admin/jqadm/attribute/media/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/media/decorators/global
* admin/jqadm/attribute/media/decorators/local

## decorators/global

Adds a list of globally available decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/media/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/media/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/media/decorators/excludes
* admin/jqadm/attribute/media/decorators/local

## decorators/local

Adds a list of local decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/media/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Attribute\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/media/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Attribute\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/media/decorators/excludes
* admin/jqadm/attribute/media/decorators/global

## name

Name of the media subpart used by the JQAdm attribute implementation

```
admin/jqadm/attribute/media/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2017.07

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Attribute\Media\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## property/decorators/excludes

Excludes decorators added by the "common" option from the attribute JQAdm client

```
admin/jqadm/attribute/media/property/decorators/excludes =
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
 admin/jqadm/attribute/media/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/media/property/decorators/global
* admin/jqadm/attribute/media/property/decorators/local

## property/decorators/global

Adds a list of globally available decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/media/property/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/media/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/media/property/decorators/excludes
* admin/jqadm/attribute/media/property/decorators/local

## property/decorators/local

Adds a list of local decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/media/property/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Attribute\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/media/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Attribute\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/media/property/decorators/excludes
* admin/jqadm/attribute/media/property/decorators/global

## property/name

Name of the property subpart used by the JQAdm attribute media implementation

```
admin/jqadm/attribute/media/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.04

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Attribute\Media\Property\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## property/subparts

List of JQAdm sub-clients rendered within the attribute media property section

```
admin/jqadm/attribute/media/property/subparts = Array
(
)
```

* Default: Array
(
)

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

Relative path to the HTML body template of the media subpart for attributes.

```
admin/jqadm/attribute/media/property/template-item = attribute/item-media-property
```

* Default: attribute/item-media-property
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

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


## subparts

List of JQAdm sub-clients rendered within the attribute media section

```
admin/jqadm/attribute/media/subparts = Array
(
    [property] => property
)
```

* Default: Array
(
)

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

Relative path to the HTML body template of the media subpart for attributes.

```
admin/jqadm/attribute/media/template-item = attribute/item-media
```

* Default: attribute/item-media
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.07

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


# name

Class name of the used account favorite client implementation

```
admin/jqadm/attribute/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.07

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Attribute\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Attribute\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/attribute/name = Myfavorite
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyFavorite"!


# price
## decorators/excludes

Excludes decorators added by the "common" option from the attribute JQAdm client

```
admin/jqadm/attribute/price/decorators/excludes =
```

* Default:
* Type: array - List of decorator names
* Since: 2016.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/attribute/price/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/price/decorators/global
* admin/jqadm/attribute/price/decorators/local

## decorators/global

Adds a list of globally available decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/price/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2016.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/price/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/price/decorators/excludes
* admin/jqadm/attribute/price/decorators/local

## decorators/local

Adds a list of local decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/price/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2016.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Attribute\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/price/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Attribute\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/price/decorators/excludes
* admin/jqadm/attribute/price/decorators/global

## name

Name of the price subpart used by the JQAdm attribute implementation

```
admin/jqadm/attribute/price/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2017.07

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Attribute\Price\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## property/decorators/excludes

Excludes decorators added by the "common" option from the attribute JQAdm client

```
admin/jqadm/attribute/price/property/decorators/excludes =
```

* Default:
* Type: array - List of decorator names
* Since: 2019.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"admin/jqadm/common/decorators/default" before they are wrapped
around the JQAdm client.

```
 admin/jqadm/attribute/price/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/price/property/decorators/global
* admin/jqadm/attribute/price/property/decorators/local

## property/decorators/global

Adds a list of globally available decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/price/property/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2019.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/price/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/price/property/decorators/excludes
* admin/jqadm/attribute/price/property/decorators/local

## property/decorators/local

Adds a list of local decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/price/property/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2019.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Attribute\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/price/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Attribute\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/price/property/decorators/excludes
* admin/jqadm/attribute/price/property/decorators/global

## property/name

Name of the property subpart used by the JQAdm attribute price implementation

```
admin/jqadm/attribute/price/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2019.07

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Attribute\Price\Property\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## property/subparts

List of JQAdm sub-clients rendered within the attribute price property section

```
admin/jqadm/attribute/price/property/subparts = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-client names
* Since: 2019.07

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

Relative path to the HTML body template of the price subpart for attributes.

```
admin/jqadm/attribute/price/property/template-item = attribute/item-price-property
```

* Default: attribute/item-price-property
* Type: string - Relative path to the template creating the HTML code
* Since: 2019.07

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


## subparts

List of JQAdm sub-clients rendered within the attribute price section

```
admin/jqadm/attribute/price/subparts = Array
(
    [property] => property
)
```

* Default: Array
(
)

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


## template-item

Relative path to the HTML body template of the price subpart for attributes.

```
admin/jqadm/attribute/price/template-item = attribute/item-price
```

* Default: attribute/item-price
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

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


# property
## decorators/excludes

Excludes decorators added by the "common" option from the attribute JQAdm client

```
admin/jqadm/attribute/property/decorators/excludes =
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
 admin/jqadm/attribute/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/property/decorators/global
* admin/jqadm/attribute/property/decorators/local

## decorators/global

Adds a list of globally available decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/property/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/property/decorators/excludes
* admin/jqadm/attribute/property/decorators/local

## decorators/local

Adds a list of local decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/property/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Attribute\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Attribute\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/property/decorators/excludes
* admin/jqadm/attribute/property/decorators/global

## name

Name of the property subpart used by the JQAdm attribute implementation

```
admin/jqadm/attribute/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2017.07

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Attribute\Property\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## subparts

List of JQAdm sub-clients rendered within the attribute property section

```
admin/jqadm/attribute/property/subparts = Array
(
)
```

* Default: Array
(
)

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


## template-item

Relative path to the HTML body template of the property subpart for attributes.

```
admin/jqadm/attribute/property/template-item = attribute/item-property
```

* Default: attribute/item-property
* Type: string - Relative path to the template creating the HTML code
* Since: 2018.01

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


# subparts

List of JQAdm sub-clients rendered within the attribute section

```
admin/jqadm/attribute/subparts = Array
(
    [media] => media
    [text] => text
    [price] => price
    [property] => property
)
```

* Default: Array
(
)

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


# template-item

Relative path to the HTML body template for the attribute item.

```
admin/jqadm/attribute/template-item = attribute/item
```

* Default: attribute/item
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.07

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

Relative path to the HTML body template for the attribute list.

```
admin/jqadm/attribute/template-list = attribute/list
```

* Default: attribute/list
* Type: string - Relative path to the template creating the HTML code
* Since: 2017.07

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


# text
## decorators/excludes

Excludes decorators added by the "common" option from the attribute JQAdm client

```
admin/jqadm/attribute/text/decorators/excludes =
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
 admin/jqadm/attribute/text/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/text/decorators/global
* admin/jqadm/attribute/text/decorators/local

## decorators/global

Adds a list of globally available decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/text/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Admin\JQAdm\Common\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/text/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/text/decorators/excludes
* admin/jqadm/attribute/text/decorators/local

## decorators/local

Adds a list of local decorators only to the attribute JQAdm client

```
admin/jqadm/attribute/text/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.07

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Attribute\Decorator\*") around the JQAdm client.

```
 admin/jqadm/attribute/text/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Attribute\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/attribute/text/decorators/excludes
* admin/jqadm/attribute/text/decorators/global

## name

Name of the text subpart used by the JQAdm attribute implementation

```
admin/jqadm/attribute/text/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2017.07

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Attribute\Text\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## subparts

List of JQAdm sub-clients rendered within the attribute text section

```
admin/jqadm/attribute/text/subparts = Array
(
)
```

* Default: Array
(
)

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

Relative path to the HTML body template of the text subpart for attributes.

```
admin/jqadm/attribute/text/template-item = attribute/item-text
```

* Default: attribute/item-text
* Type: string - Relative path to the template creating the HTML code
* Since: 2016.04

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
