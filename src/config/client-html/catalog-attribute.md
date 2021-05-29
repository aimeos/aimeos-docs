
# decorators
## excludes

Excludes decorators added by the "common" option from the catalog filter attribute html client

```
client/html/catalog/attribute/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"client/html/common/decorators/default" before they are wrapped
around the html client.

```
 client/html/catalog/attribute/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Client\Html\Common\Decorator\*") added via
"client/html/common/decorators/default" to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/attribute/decorators/global
* client/html/catalog/attribute/decorators/local

## global

Adds a list of globally available decorators only to the catalog filter attribute html client

```
client/html/catalog/attribute/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Client\Html\Common\Decorator\*") around the html client.

```
 client/html/catalog/attribute/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Client\Html\Common\Decorator\Decorator1" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/attribute/decorators/excludes
* client/html/catalog/attribute/decorators/local

## local

Adds a list of local decorators only to the catalog filter attribute html client

```
client/html/catalog/attribute/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Client\Html\Catalog\Decorator\*") around the html client.

```
 client/html/catalog/attribute/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Client\Html\Catalog\Decorator\Decorator2" only to the html client.

See also:

* client/html/common/decorators/default
* client/html/catalog/attribute/decorators/excludes
* client/html/catalog/attribute/decorators/global

# name

Class name of the used catalog attribute client implementation

```
client/html/catalog/attribute/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.04
* Since: 2018.04

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Catalog\Price\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Price\Myattribute
```

then you have to set the this configuration option:

```
 client/html/catalog/attribute/name = Myattribute
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyPrice"!


# preselect

Pre-select first item in selection list

```
client/html/catalog/attribute/preselect = 
```

* Default: 
* Type: boolean - True to select the first option by default, false to display the select hint
* Since: 2017.04

No option of the available selections for a product is pre-selected by
default. This setting removes the hint to select an option, so the first one
is selected by default.

The key for each value must be the type code of the attribute, e.g. "width",
"length", "color" or similar types. You can set the layout for all
attributes at once using e.g.

```
 client/html/catalog/attribute/preselect = array(
     'width' => false,
     'color' => true,
 )
```

Similarly, you can set the pre-selection for a specific attribute only,
leaving the rest untouched:

```
 client/html/catalog/attribute/preselect/color = true
```


## color

```
client/html/catalog/attribute/preselect/color = 
```

* Default: 


## interval

```
client/html/catalog/attribute/preselect/interval = 
```

* Default: 


## size

```
client/html/catalog/attribute/preselect/size = 
```

* Default: 


# subparts

List of HTML sub-clients rendered within the catalog attribute section

```
client/html/catalog/attribute/subparts = Array
(
    [0] => attribute
)
```

* Default: Array
* Type: array - List of sub-client names
* Since: 2018.04

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


# type

List of layout types for the optional attributes

```
client/html/catalog/attribute/type = 
```

* Default: 
* Type: array - List of attribute types as key and layout types as value, e.g. "select" or "radio"
* Since: 2015.10

Each product can contain optional attributes and this configuration setting
allows you to change how these attributs will be displayed, either as
drop-down menu (value: "select") or as list of radio buttons (value:
"radio").

The key for each value must be the type code of the attribute, e.g. "width",
"length", "color" or similar types. You can set the layout for all
attributes at once using e.g.

```
 client/html/catalog/attribute/type = array(
     'width' => 'select',
     'color' => 'radio',
 )
```

Similarly, you can set the layout type for a specific attribute only,
leaving the rest untouched:

```
 client/html/catalog/attribute/type/color = radio
```

Note: Up to 2015.10 this option was available as
client/html/catalog/detail/basket/attribute/type

See also:

* client/html/catalog/selection/type

## color

Layout types for the color attribute

```
client/html/catalog/attribute/type/color = select
```

* Default: select

See also:

* client/html/catalog/attribute/type

## interval

```
client/html/catalog/attribute/type/interval = select
```

* Default: select


## size

Layout types for the size attribute

```
client/html/catalog/attribute/type/size = select
```

* Default: select

See also:

* client/html/catalog/attribute/type