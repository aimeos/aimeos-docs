
# csv
## code/container/content

Name of the content type inside the container to read the data from

```
controller/jobs/coupon/import/csv/code/container/content = CSV
```

* Default: CSV
* Type: array - Content type name
* Since: 2017.10

The content type must always be a CSV-like format and there are
currently two format types that are supported:

* CSV

See also:

* controller/jobs/coupon/import/csv/code/container/type
* controller/jobs/coupon/import/csv/code/container/options

## code/container/options

List of file container options for the coupon import files

```
controller/jobs/coupon/import/csv/code/container/options = Array
(
)
```

* Default: Array
(
)

* Type: array - Associative list of option name/value pairs
* Since: 2017.10

Some container/content type allow you to hand over additional settings
for configuration. Please have a look at the article about
[container/content files](http://aimeos.org/docs/Developers/Utility/Create_and_read_files)
for more information.

See also:

* controller/jobs/coupon/import/csv/code/container/content
* controller/jobs/coupon/import/csv/code/container/type

## code/container/type

Name of the container type to read the data from

```
controller/jobs/coupon/import/csv/code/container/type = File
```

* Default: File
* Type: string - Container type name
* Since: 2017.10

The container type tells the importer how it should retrieve the data.
There are currently three container types that support the necessary
CSV content:

* File (plain)
* Zip

See also:

* controller/jobs/coupon/import/csv/code/container/content
* controller/jobs/coupon/import/csv/code/container/options

## code/decorators/excludes

Excludes decorators added by the "common" option from the coupon code import CSV job controller

```
controller/jobs/coupon/import/csv/code/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/coupon/import/csv/code/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/coupon/import/csv/code/decorators/global
* controller/jobs/coupon/import/csv/code/decorators/local

## code/decorators/global

Adds a list of globally available decorators only to the coupon code import CSV job controller

```
controller/jobs/coupon/import/csv/code/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/coupon/import/csv/code/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/coupon/import/csv/code/decorators/excludes
* controller/jobs/coupon/import/csv/code/decorators/local

## code/decorators/local

Adds a list of local decorators only to the coupon code import CSV job controller

```
controller/jobs/coupon/import/csv/code/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Coupon\Import\Csv\Code\Decorator\*") around the job
controller.

```
 controller/jobs/coupon/import/csv/code/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Coupon\Import\Csv\Code\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/coupon/import/csv/code/decorators/excludes
* controller/jobs/coupon/import/csv/code/decorators/global

## code/mapping

List of mappings between the position in the CSV file and item keys

```
controller/jobs/coupon/import/csv/code/mapping = Array
(
    [code] => Array
        (
            [0] => coupon.code.code
            [1] => coupon.code.count
            [2] => coupon.code.datestart
            [3] => coupon.code.dateend
        )

)
```

* Default: Array
(
    [code] => Array
        (
            [0] => coupon.code.code
            [1] => coupon.code.count
            [2] => coupon.code.datestart
            [3] => coupon.code.dateend
        )

)

* Type: array - Associative list of processor names and lists of key/position pairs
* Since: 2017.10

This configuration setting overwrites the shared option
"controller/common/coupon/import/csv/mapping" if you need a
specific setting for the job controller. Otherwise, you should
use the shared option for consistency.

See also:

* controller/jobs/coupon/import/csv/code/skip-lines
* controller/jobs/coupon/import/csv/code/max-size

## code/max-size

Maximum number of CSV rows to import at once

```
controller/jobs/coupon/import/csv/code/max-size = 1000
```

* Default: 1000
* Type: integer - Number of rows
* Since: 2017.10

It's more efficient to read and import more than one row at a time
to speed up the import. Usually, the bigger the chunk that is imported
at once, the less time the importer will need. The downside is that
the amount of memory required by the import process will increase as
well. Therefore, it's a trade-off between memory consumption and
import speed.

See also:

* controller/jobs/coupon/import/csv/code/skip-lines
* controller/jobs/coupon/import/csv/code/mapping

## code/name

Class name of the used coupon code import job controller implementation

```
controller/jobs/coupon/import/csv/code/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.10

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Coupon\Import\Csv\Code\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Coupon\Import\Csv\Code\Mycsv
```

then you have to set the this configuration option:

```
 controller/jobs/coupon/import/csv/code/name = Mycsv
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCsv"!


## code/skip-lines

Number of rows skipped in front of each CSV files

```
controller/jobs/coupon/import/csv/code/skip-lines = 0
```

* Default: 0
* Type: integer - Number of rows
* Since: 2015.08

Some CSV files contain header information describing the content of
the column values. These data is for informational purpose only and
can't be imported into the database. Using this option, you can
define the number of lines that should be left out before the import
begins.

See also:

* controller/jobs/coupon/import/csv/code/mapping
* controller/jobs/coupon/import/csv/code/max-size