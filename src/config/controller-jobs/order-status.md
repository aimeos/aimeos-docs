
# csv
## decorators/excludes

Excludes decorators added by the "common" option from the order status CSV job controller

```
controller/jobs/order/status/csv/decorators/excludes = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2021.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/order/status/csv/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/status/csv/decorators/global
* controller/jobs/order/status/csv/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order status CSV job controller

```
controller/jobs/order/status/csv/decorators/global = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2021.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/order/status/csv/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/status/csv/decorators/excludes
* controller/jobs/order/status/csv/decorators/local

## decorators/local

Adds a list of local decorators only to the order status CSV job controller

```
controller/jobs/order/status/csv/decorators/local = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - List of decorator names
* Since: 2021.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Order\Status\Csv\Decorator\*") around the job
controller.

```
 controller/jobs/order/status/csv/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Order\Status\Csv\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/order/status/csv/decorators/excludes
* controller/jobs/order/status/csv/decorators/global

## directory

Path to the CSV files relative to the order status file system

```
controller/jobs/order/status/csv/directory = orderstatus
```

* Default: `orderstatus`
* Type: string - Relative sub-directory name, path or empty string
* Since: 2021.10

The CSV files for importing the order status values are expected to
be in a subdirectory of the used file system ("fs-orderstatus" or "fs")
named "orderstatus" by default. This can be changed to any other
sub-directory name (or a path with several sub-directories) or to an
empty string in case the files are located in the root directory of
the virtual file system.


## max-size

Maximum number of CSV rows to import at once

```
controller/jobs/order/status/csv/max-size = 1000
```

* Default: `1000`
* Type: int - Number of rows
* Since: 2021.10

It's more efficient to read and status more than one row at a time
to speed up the status. Usually, the bigger the chunk that is statused
at once, the less time the statuser will need. The downside is that
the amount of memory required by the status process will increase as
well. Therefore, it's a trade-off between memory consumption and
status speed.


## name

Class name of the used order suggestions scheduler controller implementation

```
controller/jobs/order/status/csv/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2021.10

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Order\Status\Csv\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Order\Status\Csv\Mycsv
```

then you have to set the this configuration option:

```
 controller/jobs/order/status/csv/name = Mycsv
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCsv"!


## separator

Character separating the values in the CSV file

```
controller/jobs/order/status/csv/separator = ;
```

* Default: `,`
* Type: string - Single byte separator character
* Since: 2021.10

By default, a comma (",") is used but it can be changed to e.g. a
semicolon (";") if neccesary.


## skip

Number of rows that should be skipped

```
controller/jobs/order/status/csv/skip = 1
```

* Default: `0`
* Type: int - Number of header rows to skip
* Since: 2021.10

If the CSV file contains a header that shouldn't be imported, set
this option to "1" or any number of rows that should be ignored.
