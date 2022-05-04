
# csv
## container/content

Name of the content type inside the container to read the data from

```
controller/jobs/order/export/csv/container/content = CSV
```

* Default: CSV
* Type: array - Content type name
* Since: 2015.05

The content type must always be a CSV-like format and there are
currently two format types that are supported:

* CSV

See also:

* controller/jobs/order/export/csv/location
* controller/jobs/order/export/csv/container/type
* controller/jobs/order/export/csv/container/options

## container/options

List of file container options for the order export files

```
controller/jobs/order/export/csv/container/options = Array
(
)
```

* Default: Array
(
)

* Type: array - Associative list of option name/value pairs
* Since: 2015.05

Some container/content type allow you to hand over additional settings
for configuration. Please have a look at the article about
[container/content files](http://aimeos.org/docs/Developers/Utility/Create_and_read_files)
for more information.

See also:

* controller/jobs/order/export/csv/location
* controller/jobs/order/export/csv/container/content
* controller/jobs/order/export/csv/container/type

## container/type

Nave of the container type to read the data from

```
controller/jobs/order/export/csv/container/type = Directory
```

* Default: Directory
* Type: string - Container type name
* Since: 2015.05

The container type tells the exporter how it should retrieve the data.
There are currently three container types that support the necessary
CSV content:

* Directory
* Zip

See also:

* controller/jobs/order/export/csv/location
* controller/jobs/order/export/csv/container/content
* controller/jobs/order/export/csv/container/options

## decorators/excludes

Excludes decorators added by the "common" option from the order export CSV job controller

```
controller/jobs/order/export/csv/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2015.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/order/export/csv/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/export/csv/decorators/global
* controller/jobs/order/export/csv/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order export CSV job controller

```
controller/jobs/order/export/csv/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2015.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/export/csv/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/export/csv/decorators/excludes
* controller/jobs/order/export/csv/decorators/local

## decorators/local

Adds a list of local decorators only to the order export CSV job controller

```
controller/jobs/order/export/csv/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2015.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Export\Csv\Decorator\*") around the job
controller.

```
 controller/jobs/order/export/csv/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Export\Csv\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/export/csv/decorators/excludes
* controller/jobs/order/export/csv/decorators/global

## location

Temporary file or directory where the content is stored which should be exported

```
controller/jobs/order/export/csv/location = /tmp
```

* Default: /tmp
* Type: string - Absolute file or directory path
* Since: 2017.08

The path can point to any supported container format as long as the
content is in CSV format, e.g.

* Directory container / CSV file
* Zip container / compressed CSV file

See also:

* controller/jobs/order/export/csv/container/type
* controller/jobs/order/export/csv/container/content
* controller/jobs/order/export/csv/container/options

## mapping

List of mappings between the position in the CSV file and item keys

```
controller/jobs/order/export/csv/mapping = Array
(
    [invoice] => Array
        (
            [2] => order.type
            [3] => order.datepayment
            [4] => order.statuspayment
            [5] => order.datedelivery
            [6] => order.statusdelivery
            [7] => order.relatedid
            [8] => order.base.customerid
            [9] => order.base.sitecode
            [10] => order.base.languageid
            [11] => order.base.currencyid
            [12] => order.base.price
            [13] => order.base.costs
            [14] => order.base.rebate
            [15] => order.base.taxvalue
            [16] => order.base.taxflag
            [17] => order.base.status
            [18] => order.base.comment
        )

    [address] => Array
        (
            [2] => order.base.address.type
            [3] => order.base.address.salutation
            [4] => order.base.address.company
            [5] => order.base.address.vatid
            [6] => order.base.address.title
            [7] => order.base.address.firstname
            [8] => order.base.address.lastname
            [9] => order.base.address.address1
            [10] => order.base.address.address2
            [11] => order.base.address.address3
            [12] => order.base.address.postal
            [13] => order.base.address.city
            [14] => order.base.address.state
            [15] => order.base.address.countryid
            [16] => order.base.address.languageid
            [17] => order.base.address.telephone
            [18] => order.base.address.telefax
            [19] => order.base.address.email
            [20] => order.base.address.website
            [21] => order.base.address.longitude
            [22] => order.base.address.latitude
        )

    [service] => Array
        (
            [2] => order.base.service.type
            [3] => order.base.service.code
            [4] => order.base.service.name
            [5] => order.base.service.mediaurl
            [6] => order.base.service.price
            [7] => order.base.service.costs
            [8] => order.base.service.rebate
            [9] => order.base.service.taxrate
            [10] => order.base.service.attribute.type
            [11] => order.base.service.attribute.code
            [12] => order.base.service.attribute.name
            [13] => order.base.service.attribute.value
        )

    [coupon] => Array
        (
            [2] => order.base.coupon.code
        )

    [product] => Array
        (
            [2] => order.base.product.type
            [3] => order.base.product.stocktype
            [4] => order.base.product.vendor
            [5] => order.base.product.prodcode
            [6] => order.base.product.productid
            [7] => order.base.product.quantity
            [8] => order.base.product.name
            [9] => order.base.product.mediaurl
            [10] => order.base.product.price
            [11] => order.base.product.costs
            [12] => order.base.product.rebate
            [13] => order.base.product.taxrate
            [14] => order.base.product.status
            [15] => order.base.product.position
            [16] => order.base.product.attribute.type
            [17] => order.base.product.attribute.code
            [18] => order.base.product.attribute.name
            [19] => order.base.product.attribute.value
        )

)
```

* Default: Array
(
    [invoice] => Array
        (
            [2] => order.type
            [3] => order.datepayment
            [4] => order.statuspayment
            [5] => order.datedelivery
            [6] => order.statusdelivery
            [7] => order.relatedid
            [8] => order.base.customerid
            [9] => order.base.sitecode
            [10] => order.base.languageid
            [11] => order.base.currencyid
            [12] => order.base.price
            [13] => order.base.costs
            [14] => order.base.rebate
            [15] => order.base.taxvalue
            [16] => order.base.taxflag
            [17] => order.base.status
            [18] => order.base.comment
        )

    [address] => Array
        (
            [2] => order.base.address.type
            [3] => order.base.address.salutation
            [4] => order.base.address.company
            [5] => order.base.address.vatid
            [6] => order.base.address.title
            [7] => order.base.address.firstname
            [8] => order.base.address.lastname
            [9] => order.base.address.address1
            [10] => order.base.address.address2
            [11] => order.base.address.address3
            [12] => order.base.address.postal
            [13] => order.base.address.city
            [14] => order.base.address.state
            [15] => order.base.address.countryid
            [16] => order.base.address.languageid
            [17] => order.base.address.telephone
            [18] => order.base.address.telefax
            [19] => order.base.address.email
            [20] => order.base.address.website
            [21] => order.base.address.longitude
            [22] => order.base.address.latitude
        )

    [service] => Array
        (
            [2] => order.base.service.type
            [3] => order.base.service.code
            [4] => order.base.service.name
            [5] => order.base.service.mediaurl
            [6] => order.base.service.price
            [7] => order.base.service.costs
            [8] => order.base.service.rebate
            [9] => order.base.service.taxrate
            [10] => order.base.service.attribute.type
            [11] => order.base.service.attribute.code
            [12] => order.base.service.attribute.name
            [13] => order.base.service.attribute.value
        )

    [coupon] => Array
        (
            [2] => order.base.coupon.code
        )

    [product] => Array
        (
            [2] => order.base.product.type
            [3] => order.base.product.stocktype
            [4] => order.base.product.vendor
            [5] => order.base.product.prodcode
            [6] => order.base.product.productid
            [7] => order.base.product.quantity
            [8] => order.base.product.name
            [9] => order.base.product.mediaurl
            [10] => order.base.product.price
            [11] => order.base.product.costs
            [12] => order.base.product.rebate
            [13] => order.base.product.taxrate
            [14] => order.base.product.status
            [15] => order.base.product.position
            [16] => order.base.product.attribute.type
            [17] => order.base.product.attribute.code
            [18] => order.base.product.attribute.name
            [19] => order.base.product.attribute.value
        )

)

* Type: array - Associative list of processor names and lists of key/position pairs
* Since: 2017.08

This configuration setting overwrites the shared option
"controller/common/order/export/csv/mapping" if you need a
specific setting for the job controller. Otherwise, you should
use the shared option for consistency.

See also:

* controller/common/order/export/csv/max-size

## name

Class name of the used order suggestions scheduler controller implementation

```
controller/jobs/order/export/csv/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2015.01

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Export\Csv\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Export\Csv\Mycsv
```

then you have to set the this configuration option:

```
 controller/jobs/order/export/csv/name = Mycsv
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCsv"!
