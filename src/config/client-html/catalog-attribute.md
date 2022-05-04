
# decorators
## excludes

```
client/html/catalog/attribute/decorators/excludes = Array
(
)
```

* Default: Array
(
)



## global

```
client/html/catalog/attribute/decorators/global = Array
(
)
```

* Default: Array
(
)



## local

```
client/html/catalog/attribute/decorators/local = Array
(
)
```

* Default: Array
(
)



# name

Class name of the used catalog attribute client implementation

```
client/html/catalog/attribute/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.04

Each default HTML client can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the client factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Client\Html\Catalog\Attribute\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Client\Html\Catalog\Attribute\Myattribute
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
or numbers. Avoid chamel case names like "MyAttribute"!


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