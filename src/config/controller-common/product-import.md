
# csv
## cache/attribute/name

```
controller/common/product/import/csv/cache/attribute/name = Standard
```

* Default: Standard


## cache/catalog/name

```
controller/common/product/import/csv/cache/catalog/name = Standard
```

* Default: Standard


## cache/product/name

```
controller/common/product/import/csv/cache/product/name = Standard
```

* Default: Standard


## converter

List of converter names for the values at the position in the CSV file

```
controller/common/product/import/csv/converter = Array
(
)
```

* Default: Array
* Type: array - Associative list of position/converter name (or list of names) pairs
* Since: 2015.05

Not all data in the CSV file is already in the required format. Maybe
the text encoding isn't UTF-8, the date is not in ISO format or something
similar. In order to convert the data before it's imported, you can
specify a list of converter objects that should be applied to the data
from the CSV file.

To each field in the CSV file, you can apply one or more converters,
e.g. to encode a Latin text to UTF8 for the second CSV field:

```
 array( 1 => 'Text/LatinUTF8' )
```

Similarly, you can also apply several converters at once to the same
field:

```
 array( 1 => array( 'Text/LatinUTF8', 'DateTime/EnglishISO' ) )
```

It would convert the data of the second CSV field first to UTF-8 and
afterwards try to translate it to an ISO date format.

The available converter objects are named "\Aimeos\MW\Convert\<type>_<conversion>"
where <type> is the data type and <conversion> the way of the conversion.
In the configuration, the type and conversion must be separated by a
slash (<type>/<conversion>).

**Note:** Keep in mind that the position of the CSV fields start at
zero (0). If you only need to convert a few fields, you don't have to
configure all fields. Only specify the positions in the array you
really need!

See also:

* controller/common/product/import/csv/domains
* controller/common/product/import/csv/mapping
* controller/common/product/import/csv/max-size

## domains

List of item domain names that should be retrieved along with the product items

```
controller/common/product/import/csv/domains = Array
(
    [attribute] => attribute
    [media] => media
    [price] => price
    [product] => product
    [product/property] => product/property
    [text] => text
)
```

* Default: Array
* Type: array - Associative list of MShop item domain names
* Since: 2015.05

For efficient processing, the items associated to the products can be
fetched to, minimizing the number of database queries required. To be
most effective, the list of item domain names should be used in the
mapping configuration too, so the retrieved items will be used during
the import.

See also:

* controller/common/product/import/csv/mapping
* controller/common/product/import/csv/converter
* controller/common/product/import/csv/max-size

## mapping

List of mappings between the position in the CSV file and item keys

```
controller/common/product/import/csv/mapping = Array
(
    [item] => Array
        (
            [0] => product.code
            [1] => product.label
            [2] => product.type
            [3] => product.status
        )

    [text] => Array
        (
            [4] => text.type
            [5] => text.content
            [6] => text.type
            [7] => text.content
        )

    [media] => Array
        (
            [8] => media.url
        )

    [price] => Array
        (
            [9] => price.currencyid
            [10] => price.quantity
            [11] => price.value
            [12] => price.taxrate
        )

    [attribute] => Array
        (
            [13] => attribute.code
            [14] => attribute.type
        )

    [product] => Array
        (
            [15] => product.code
            [16] => product.lists.type
        )

    [property] => Array
        (
            [17] => product.property.value
            [18] => product.property.type
        )

    [catalog] => Array
        (
            [19] => catalog.code
            [20] => catalog.lists.type
        )

)
```

* Default: Array
* Type: array - Associative list of processor names and lists of key/position pairs
* Since: 2015.05

The importer have to know which data is at which position in the CSV
file. Therefore, you need to specify a mapping between each position
and the MShop domain item key (e.g. "product.code") it represents.

You can use all domain item keys which are used in the fromArray()
methods of the item classes.

These mappings are grouped together by their processor names, which
are responsible for importing the data, e.g. all mappings in "item"
will be processed by the base product importer while the mappings in
"text" will be imported by the text processor.

See also:

* controller/common/product/import/csv/domains
* controller/common/product/import/csv/converter
* controller/common/product/import/csv/max-size

## max-size

Maximum number of CSV rows to import at once

```
controller/common/product/import/csv/max-size = 1000
```

* Default: 1000
* Type: integer - Number of rows
* Since: 2015.05

It's more efficient to read and import more than one row at a time
to speed up the import. Usually, the bigger the chunk that is imported
at once, the less time the importer will need. The downside is that
the amount of memory required by the import process will increase as
well. Therefore, it's a trade-off between memory consumption and
import speed.

See also:

* controller/common/product/import/csv/domains
* controller/common/product/import/csv/mapping
* controller/common/product/import/csv/converter

## processor/attribute/listtypes

```
controller/common/product/import/csv/processor/attribute/listtypes = 
```

* Default: 


## processor/attribute/name

```
controller/common/product/import/csv/processor/attribute/name = Standard
```

* Default: Standard


## processor/catalog/listtypes

```
controller/common/product/import/csv/processor/catalog/listtypes = 
```

* Default: 


## processor/catalog/name

```
controller/common/product/import/csv/processor/catalog/name = Standard
```

* Default: Standard


## processor/media/listtypes

```
controller/common/product/import/csv/processor/media/listtypes = 
```

* Default: 


## processor/media/name

```
controller/common/product/import/csv/processor/media/name = Standard
```

* Default: Standard


## processor/price/listtypes

```
controller/common/product/import/csv/processor/price/listtypes = 
```

* Default: 


## processor/price/name

```
controller/common/product/import/csv/processor/price/name = Standard
```

* Default: Standard


## processor/product/listtypes

```
controller/common/product/import/csv/processor/product/listtypes = Array
(
    [0] => default
    [1] => suggestion
)
```

* Default: Array


## processor/product/name

```
controller/common/product/import/csv/processor/product/name = Standard
```

* Default: Standard


## processor/property/name

```
controller/common/product/import/csv/processor/property/name = Standard
```

* Default: Standard


## processor/text/listtypes

```
controller/common/product/import/csv/processor/text/listtypes = 
```

* Default: 


## processor/text/name

```
controller/common/product/import/csv/processor/text/name = Standard
```

* Default: Standard


## separator

```
controller/common/product/import/csv/separator = 
```

* Default: 

