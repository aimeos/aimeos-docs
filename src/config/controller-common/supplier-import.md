
# csv
## converter

List of converter names for the values at the position in the CSV file

```
controller/common/supplier/import/csv/converter = Array
(
)
```

* Default: Array
* Type: array - Associative list of position/converter name (or list of names) pairs
* Since: 2020.07

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

* controller/common/supplier/import/csv/domains
* controller/common/supplier/import/csv/mapping
* controller/common/supplier/import/csv/max-size

## domains

List of item domain names that should be retrieved along with the supplier items

```
controller/common/supplier/import/csv/domains = Array
(
    [0] => media
    [1] => text
    [2] => supplier/address
)
```

* Default: Array
* Type: array - Associative list of MShop item domain names
* Since: 2020.07

For efficient processing, the items associated to the suppliers can be
fetched to, minimizing the number of database queries required. To be
most effective, the list of item domain names should be used in the
mapping configuration too, so the retrieved items will be used during
the import.

See also:

* controller/common/supplier/import/csv/mapping
* controller/common/supplier/import/csv/converter
* controller/common/supplier/import/csv/max-size

## mapping

List of mappings between the position in the CSV file and item keys

```
controller/common/supplier/import/csv/mapping = Array
(
    [item] => Array
        (
            [0] => supplier.code
            [1] => supplier.label
            [2] => supplier.status
        )

    [text] => Array
        (
            [3] => text.languageid
            [4] => text.type
            [5] => text.content
        )

    [media] => Array
        (
            [6] => media.type
            [7] => media.url
        )

    [address] => Array
        (
            [8] => supplier.address.languageid
            [9] => supplier.address.countryid
            [10] => supplier.address.city
        )

)
```

* Default: Array
* Type: array - Associative list of processor names and lists of key/position pairs
* Since: 2020.07

The importer have to know which data is at which position in the CSV
file. Therefore, you need to specify a mapping between each position
and the MShop domain item key (e.g. "supplier.code") it represents.

You can use all domain item keys which are used in the fromArray()
methods of the item classes.

These mappings are grouped together by their processor names, which
are responsible for importing the data, e.g. all mappings in "item"
will be processed by the base supplier importer while the mappings in
"text" will be imported by the text processor.

See also:

* controller/common/supplier/import/csv/domains
* controller/common/supplier/import/csv/converter
* controller/common/supplier/import/csv/max-size

## max-size

Maximum number of CSV rows to import at once

```
controller/common/supplier/import/csv/max-size = 1000
```

* Default: 1000
* Type: integer - Number of rows
* Since: 2020.07

It's more efficient to read and import more than one row at a time
to speed up the import. Usually, the bigger the chunk that is imported
at once, the less time the importer will need. The downside is that
the amount of memory required by the import process will increase as
well. Therefore, it's a trade-off between memory consumption and
import speed.

See also:

* controller/common/supplier/import/csv/domains
* controller/common/supplier/import/csv/mapping
* controller/common/supplier/import/csv/converter

## processor/address/name

```
controller/common/supplier/import/csv/processor/address/name = Standard
```

* Default: Standard


## processor/media/listtypes

```
controller/common/supplier/import/csv/processor/media/listtypes = 
```

* Default: 


## processor/media/name

```
controller/common/supplier/import/csv/processor/media/name = Standard
```

* Default: Standard


## processor/text/listtypes

```
controller/common/supplier/import/csv/processor/text/listtypes = 
```

* Default: 


## processor/text/name

```
controller/common/supplier/import/csv/processor/text/name = Standard
```

* Default: Standard


## separator

```
controller/common/supplier/import/csv/separator = 
```

* Default: 

