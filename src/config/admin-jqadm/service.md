
# decorators
## excludes

Excludes decorators added by the "common" option from the service JQAdm client

```
admin/jqadm/service/decorators/excludes = 
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
 admin/jqadm/service/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"client/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/decorators/global
* admin/jqadm/service/decorators/local

## global

Adds a list of globally available decorators only to the service JQAdm client

```
admin/jqadm/service/decorators/global = 
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
 admin/jqadm/service/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/decorators/excludes
* admin/jqadm/service/decorators/local

## local

Adds a list of local decorators only to the service JQAdm client

```
admin/jqadm/service/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Admin\JQAdm\Service\Decorator\*") around the JQAdm client.

```
 admin/jqadm/service/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Service\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/decorators/excludes
* admin/jqadm/service/decorators/global

# domains

List of domain items that should be fetched along with the service

```
admin/jqadm/service/domains = Array
(
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
* Since: 2017.10

If you need to display additional content, you can configure your own
list of domains (attribute, media, price, service, text, etc. are
domains) whose items are fetched from the storage.


# fields

List of service columns that should be displayed in the list view

```
admin/jqadm/service/fields = Array
(
    [0] => service.status
    [1] => service.type
    [2] => service.label
    [3] => service.provider
)
```

* Default: Array
(
    [0] => service.status
    [1] => service.type
    [2] => service.label
    [3] => service.provider
)

* Type: array - List of field names, i.e. search keys
* Since: 2017.07

Changes the list of service columns shown by default in the service list view.
The columns can be changed by the editor as required within the administraiton
interface.

The names of the colums are in fact the search keys defined by the managers,
e.g. "service.id" for the customer ID.


# item
## media/config/suggest

List of suggested configuration keys in service media panel

```
admin/jqadm/service/item/media/config/suggest = Array
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

List of suggested configuration keys in service price panel

```
admin/jqadm/service/item/price/config/suggest = Array
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

List of suggested configuration keys in service text panel

```
admin/jqadm/service/item/text/config/suggest = Array
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

Excludes decorators added by the "common" option from the service JQAdm client

```
admin/jqadm/service/media/decorators/excludes = 
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
 admin/jqadm/service/media/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/media/decorators/global
* admin/jqadm/service/media/decorators/local

## decorators/global

Adds a list of globally available decorators only to the service JQAdm client

```
admin/jqadm/service/media/decorators/global = Array
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
 admin/jqadm/service/media/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/media/decorators/excludes
* admin/jqadm/service/media/decorators/local

## decorators/local

Adds a list of local decorators only to the service JQAdm client

```
admin/jqadm/service/media/decorators/local = Array
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
("\Aimeos\Admin\JQAdm\Service\Decorator\*") around the JQAdm client.

```
 admin/jqadm/service/media/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Service\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/media/decorators/excludes
* admin/jqadm/service/media/decorators/global

## name

Name of the media subpart used by the JQAdm service implementation

```
admin/jqadm/service/media/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2017.07

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Service\Media\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## property/decorators/excludes

Excludes decorators added by the "common" option from the service JQAdm client

```
admin/jqadm/service/media/property/decorators/excludes = 
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
 admin/jqadm/service/media/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/media/property/decorators/global
* admin/jqadm/service/media/property/decorators/local

## property/decorators/global

Adds a list of globally available decorators only to the service JQAdm client

```
admin/jqadm/service/media/property/decorators/global = Array
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
 admin/jqadm/service/media/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/media/property/decorators/excludes
* admin/jqadm/service/media/property/decorators/local

## property/decorators/local

Adds a list of local decorators only to the service JQAdm client

```
admin/jqadm/service/media/property/decorators/local = Array
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
("\Aimeos\Admin\JQAdm\Service\Decorator\*") around the JQAdm client.

```
 admin/jqadm/service/media/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Service\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/media/property/decorators/excludes
* admin/jqadm/service/media/property/decorators/global

## property/name

Name of the property subpart used by the JQAdm service media implementation

```
admin/jqadm/service/media/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.04

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Service\Media\Property\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## property/subparts

List of JQAdm sub-clients rendered within the service media property section

```
admin/jqadm/service/media/property/subparts = Array
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

Relative path to the HTML body template of the media subpart for services.

```
admin/jqadm/service/media/property/template-item = service/item-media-property
```

* Default: service/item-media-property
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

List of JQAdm sub-clients rendered within the service media section

```
admin/jqadm/service/media/subparts = Array
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

Relative path to the HTML body template of the media subpart for services.

```
admin/jqadm/service/media/template-item = service/item-media
```

* Default: service/item-media
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
admin/jqadm/service/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2017.07

Each default admin client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Admin\JQAdm\Service\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Admin\JQAdm\Service\Myfavorite
```

then you have to set the this configuration option:

```
 admin/jqadm/service/name = Myfavorite
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

Excludes decorators added by the "common" option from the service JQAdm client

```
admin/jqadm/service/price/decorators/excludes = 
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
 admin/jqadm/service/price/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/price/decorators/global
* admin/jqadm/service/price/decorators/local

## decorators/global

Adds a list of globally available decorators only to the service JQAdm client

```
admin/jqadm/service/price/decorators/global = Array
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
 admin/jqadm/service/price/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/price/decorators/excludes
* admin/jqadm/service/price/decorators/local

## decorators/local

Adds a list of local decorators only to the service JQAdm client

```
admin/jqadm/service/price/decorators/local = Array
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
("\Aimeos\Admin\JQAdm\Service\Decorator\*") around the JQAdm client.

```
 admin/jqadm/service/price/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Service\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/price/decorators/excludes
* admin/jqadm/service/price/decorators/global

## name

Name of the price subpart used by the JQAdm service implementation

```
admin/jqadm/service/price/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2017.07

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Service\Price\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## property/decorators/excludes

Excludes decorators added by the "common" option from the service JQAdm client

```
admin/jqadm/service/price/property/decorators/excludes = 
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
 admin/jqadm/service/price/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/price/property/decorators/global
* admin/jqadm/service/price/property/decorators/local

## property/decorators/global

Adds a list of globally available decorators only to the service JQAdm client

```
admin/jqadm/service/price/property/decorators/global = Array
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
 admin/jqadm/service/price/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/price/property/decorators/excludes
* admin/jqadm/service/price/property/decorators/local

## property/decorators/local

Adds a list of local decorators only to the service JQAdm client

```
admin/jqadm/service/price/property/decorators/local = Array
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
("\Aimeos\Admin\JQAdm\Service\Decorator\*") around the JQAdm client.

```
 admin/jqadm/service/price/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Service\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/price/property/decorators/excludes
* admin/jqadm/service/price/property/decorators/global

## property/name

Name of the property subpart used by the JQAdm service price implementation

```
admin/jqadm/service/price/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2018.04

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Service\Price\Property\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## property/subparts

List of JQAdm sub-clients rendered within the service price property section

```
admin/jqadm/service/price/property/subparts = Array
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

Relative path to the HTML body template of the price subpart for services.

```
admin/jqadm/service/price/property/template-item = service/item-price-property
```

* Default: service/item-price-property
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

List of JQAdm sub-clients rendered within the service price section

```
admin/jqadm/service/price/subparts = Array
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

Relative path to the HTML body template of the price subpart for services.

```
admin/jqadm/service/price/template-item = service/item-price
```

* Default: service/item-price
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


# subparts

List of JQAdm sub-clients rendered within the service section

```
admin/jqadm/service/subparts = Array
(
    [media] => media
    [text] => text
    [price] => price
)
```

* Default: Array
(
)

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


# template-item

Relative path to the HTML body template for the service item.

```
admin/jqadm/service/template-item = service/item
```

* Default: service/item
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


# template-list

Relative path to the HTML body template for the service list.

```
admin/jqadm/service/template-list = service/list
```

* Default: service/list
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


# text
## decorators/excludes

Excludes decorators added by the "common" option from the service JQAdm client

```
admin/jqadm/service/text/decorators/excludes = 
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
 admin/jqadm/service/text/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Admin\JQAdm\Common\Decorator\*") added via
"admin/jqadm/common/decorators/default" to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/text/decorators/global
* admin/jqadm/service/text/decorators/local

## decorators/global

Adds a list of globally available decorators only to the service JQAdm client

```
admin/jqadm/service/text/decorators/global = Array
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
 admin/jqadm/service/text/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Admin\JQAdm\Common\Decorator\Decorator1" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/text/decorators/excludes
* admin/jqadm/service/text/decorators/local

## decorators/local

Adds a list of local decorators only to the service JQAdm client

```
admin/jqadm/service/text/decorators/local = Array
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
("\Aimeos\Admin\JQAdm\Service\Decorator\*") around the JQAdm client.

```
 admin/jqadm/service/text/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Admin\JQAdm\Service\Decorator\Decorator2" only to the JQAdm client.

See also:

* admin/jqadm/common/decorators/default
* admin/jqadm/service/text/decorators/excludes
* admin/jqadm/service/text/decorators/global

## name

Name of the text subpart used by the JQAdm service implementation

```
admin/jqadm/service/text/name = Standard
```

* Default: Standard
* Type: string - Last part of the JQAdm class name
* Since: 2017.10

Use "Myname" if your class is named "\Aimeos\Admin\Jqadm\Service\Text\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## subparts

List of JQAdm sub-clients rendered within the service text section

```
admin/jqadm/service/text/subparts = Array
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

Relative path to the HTML body template of the text subpart for services.

```
admin/jqadm/service/text/template-item = service/item-text
```

* Default: service/item-text
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
