
# preselect

Pre-select first item in selection list

```
client/html/catalog/selection/preselect = 
```

* Default: 
* Type: boolean - True to select the first option by default, false to display the select hint
* Since: 2016.07

No option of the available selections for a product is pre-selected by
default. This setting removes the hint to select an option, so the first one
is selected by default.

The key for each value must be the type code of the attribute, e.g. "width",
"length", "color" or similar types. You can set the layout for all
attributes at once using e.g.

```
 client/html/catalog/selection/preselect = array(
     'width' => false,
     'color' => true,
 )
```

Similarly, you can set the pre-selection for a specific attribute only,
leaving the rest untouched:

```
 client/html/catalog/selection/preselect/color = true
```


## color

```
client/html/catalog/selection/preselect/color = 
```

* Default: 


## length

```
client/html/catalog/selection/preselect/length = 
```

* Default: 


## size

```
client/html/catalog/selection/preselect/size = 
```

* Default: 


## width

```
client/html/catalog/selection/preselect/width = 
```

* Default: 


# type

List of layout types for the variant attributes

```
client/html/catalog/selection/type = 
```

* Default: 
* Type: array - List of attribute types as key and layout types as value, e.g. "select" or "radio"
* Since: 2015.10

Selection products will contain variant attributes and this configuration
setting allows you to change how these attributs will be displayed, either
as drop-down menu (value: "select") or as list of radio buttons (value:
"radio").

The key for each value must be the type code of the attribute, e.g. "width",
"length", "color" or similar types. You can set the layout for all
attributes at once using e.g.

```
 client/html/catalog/selection/type = array(
     'width' => 'select',
     'color' => 'radio',
 )
```

Similarly, you can set the layout type for a specific attribute only,
leaving the rest untouched:

```
 client/html/catalog/selection/type/color = radio
```

Note: Up to 2016.10 this option was available as
client/html/catalog/detail/basket/selection/type

See also:

* client/html/catalog/attribute/type

## color

```
client/html/catalog/selection/type/color = select
```

* Default: select


## length

Layout types for the length selection

```
client/html/catalog/selection/type/length = select
```

* Default: select

See also:

* client/html/catalog/selection/type

## size

```
client/html/catalog/selection/type/size = select
```

* Default: select


## width

Layout types for the width selection

```
client/html/catalog/selection/type/width = select
```

* Default: select

See also:

* client/html/catalog/selection/type