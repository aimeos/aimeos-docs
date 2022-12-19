
# csv
## collapse

Collapse all lines in the subscription export on only one line

```
controller/jobs/subscription/export/csv/collapse = 1
```

* Default:
* Type: bool - True to collapse all lines of one subscription, false for separate lines
* Since: 2020.07

By default, the subscription export will contain several lines for each
subscription, e.g. for the product, the addresses, the delivery and payment
services as well as the invoice data. You can merge them into one line using
this configuration setting.


## container/content

Name of the content type inside the container to read the data from

```
controller/jobs/subscription/export/csv/container/content = CSV
```

* Default: CSV
* Type: array - Content type name
* Since: 2015.05

The content type must always be a CSV-like format and there are
currently two format types that are supported:

* CSV

See also:

* controller/jobs/subscription/export/csv/location
* controller/jobs/subscription/export/csv/container/type
* controller/jobs/subscription/export/csv/container/options

## container/options

List of file container options for the subscription export files

```
controller/jobs/subscription/export/csv/container/options = Array
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

* controller/jobs/subscription/export/csv/location
* controller/jobs/subscription/export/csv/container/content
* controller/jobs/subscription/export/csv/container/type

## container/type

Nave of the container type to read the data from

```
controller/jobs/subscription/export/csv/container/type = Directory
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

* controller/jobs/subscription/export/csv/location
* controller/jobs/subscription/export/csv/container/content
* controller/jobs/subscription/export/csv/container/options

## decorators/excludes

Excludes decorators added by the "common" option from the subscription export CSV job controller

```
controller/jobs/subscription/export/csv/decorators/excludes =
```

* Default:
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/subscription/export/csv/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/export/csv/decorators/global
* controller/jobs/subscription/export/csv/decorators/local

## decorators/global

Adds a list of globally available decorators only to the subscription export CSV job controller

```
controller/jobs/subscription/export/csv/decorators/global =
```

* Default:
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/subscription/export/csv/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/export/csv/decorators/excludes
* controller/jobs/subscription/export/csv/decorators/local

## decorators/local

Adds a list of local decorators only to the subscription export CSV job controller

```
controller/jobs/subscription/export/csv/decorators/local =
```

* Default:
* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Subscription\Export\Csv\Decorator\*") around the job
controller.

```
 controller/jobs/subscription/export/csv/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Subscription\Export\Csv\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/subscription/export/csv/decorators/excludes
* controller/jobs/subscription/export/csv/decorators/global

## location

Temporary file or directory where the content is stored which should be exported

```
controller/jobs/subscription/export/csv/location = /tmp
```

* Default: /tmp
* Type: string - Absolute file or directory path
* Since: 2018.04

The path can point to any supported container format as long as the
content is in CSV format, e.g.

* Directory container / CSV file
* Zip container / compressed CSV file

See also:

* controller/jobs/subscription/export/csv/container/type
* controller/jobs/subscription/export/csv/container/content
* controller/jobs/subscription/export/csv/container/options

## mapping

List of mappings between the position in the CSV file and item keys

```
controller/jobs/subscription/export/csv/mapping = Array
(
    [subscription] => Array
        (
            [0] => subscription.interval
            [1] => subscription.period
            [2] => subscription.ordbaseid
        )

    [address] => Array
        (
            [3] => order.address.firstname
            [4] => order.address.lastname
        )

    [product] => Array
        (
            [5] => order.product.prodcode
            [6] => order.product.price
        )

)
```

* Default: Array
(
    [subscription] => Array
        (
            [2] => subscription.interval
            [3] => subscription.datenext
            [4] => subscription.dateend
            [5] => subscription.period
            [6] => subscription.status
            [7] => subscription.ctime
            [8] => subscription.ordbaseid
        )

    [address] => Array
        (
            [2] => order.address.type
            [3] => order.address.salutation
            [4] => order.address.company
            [5] => order.address.vatid
            [6] => order.address.title
            [7] => order.address.firstname
            [8] => order.address.lastname
            [9] => order.address.address1
            [10] => order.address.address2
            [11] => order.address.address3
            [12] => order.address.postal
            [13] => order.address.city
            [14] => order.address.state
            [15] => order.address.countryid
            [16] => order.address.languageid
            [17] => order.address.telephone
            [18] => order.address.telefax
            [19] => order.address.email
            [20] => order.address.website
            [21] => order.address.longitude
            [22] => order.address.latitude
        )

    [product] => Array
        (
            [2] => order.product.type
            [3] => order.product.stocktype
            [4] => order.product.vendor
            [5] => order.product.prodcode
            [6] => order.product.productid
            [7] => order.product.quantity
            [8] => order.product.name
            [9] => order.product.mediaurl
            [10] => order.product.price
            [11] => order.product.costs
            [12] => order.product.rebate
            [13] => order.product.taxrate
            [14] => order.product.status
            [15] => order.product.position
            [16] => order.product.attribute.type
            [17] => order.product.attribute.code
            [18] => order.product.attribute.name
            [19] => order.product.attribute.value
        )

)

* Type: array - Associative list of processor names and lists of key/position pairs
* Since: 2018.04

This configuration setting overwrites the shared option
"controller/common/subscription/export/csv/mapping" if you need a
specific setting for the job controller. Otherwise, you should
use the shared option for consistency.

See also:

* controller/common/subscription/export/csv/max-size

## name

Class name of the used subscription suggestions scheduler controller implementation

```
controller/jobs/subscription/export/csv/name =
```

* Default:
* Type: string - Last part of the class name
* Since: 2018.04

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Subscription\Export\Csv\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Subscription\Export\Csv\Mycsv
```

then you have to set the this configuration option:

```
 controller/jobs/subscription/export/csv/name = Mycsv
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCsv"!
