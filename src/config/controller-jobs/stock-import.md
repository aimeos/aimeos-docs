
# csv
## backup

Name of the backup for sucessfully imported files

```
controller/jobs/stock/import/csv/backup = 
```

* Default: 
* Type: integer - Name of the backup file, optionally with date/time placeholders
* Since: 2019.04

After a CSV file was imported successfully, you can move it to another
location, so it won't be imported again and isn't overwritten by the
next file that is stored at the same location in the file system.

You should use an absolute path to be sure but can be relative path
if you absolutely know from where the job will be executed from. The
name of the new backup location can contain placeholders understood
by the PHP DateTime::format() method (with percent signs prefix) to
create dynamic paths, e.g. "backup/%Y-%m-%d" which would create
"backup/2000-01-01". For more information about the date() placeholders,
please have a look  into the PHP documentation of the
[format() method](https://www.php.net/manual/en/datetime.format.php).

**Note:** If no backup name is configured, the file will be removed!

See also:

* controller/jobs/stock/import/csv/location
* controller/jobs/stock/import/csv/max-size
* controller/jobs/stock/import/csv/skip-lines

## decorators/excludes

Excludes decorators added by the "common" option from the stock import CSV job controller

```
controller/jobs/stock/import/csv/decorators/excludes = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2019.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/stock/import/csv/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/stock/import/csv/decorators/global
* controller/jobs/stock/import/csv/decorators/local

## decorators/global

Adds a list of globally available decorators only to the stock import CSV job controller

```
controller/jobs/stock/import/csv/decorators/global = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2019.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/stock/import/csv/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/stock/import/csv/decorators/excludes
* controller/jobs/stock/import/csv/decorators/local

## decorators/local

Adds a list of local decorators only to the stock import CSV job controller

```
controller/jobs/stock/import/csv/decorators/local = 
```

* Default: 
* Type: array - List of decorator names
* Since: 2019.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Stock\Import\Csv\Decorator\*") around the job
controller.

```
 controller/jobs/stock/import/csv/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Stock\Import\Csv\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/stock/import/csv/decorators/excludes
* controller/jobs/stock/import/csv/decorators/global

## location

File or directory where the content is stored which should be imported

```
controller/jobs/stock/import/csv/location = stock
```

* Default: stock
* Type: string - Relative path to the CSV files
* Since: 2019.04

You need to configure the CSV file or directory with the CSV files that
should be imported. It should be an absolute path to be sure but can be
relative path if you absolutely know from where the job will be executed
from.

See also:

* controller/jobs/stock/import/csv/backup
* controller/jobs/stock/import/csv/max-size
* controller/jobs/stock/import/csv/skip-lines

## max-size

Maximum number of CSV rows to import at once

```
controller/jobs/stock/import/csv/max-size = 1000
```

* Default: 1000
* Type: integer - Number of rows
* Since: 2019.04

It's more efficient to read and import more than one row at a time
to speed up the import. Usually, the bigger the chunk that is imported
at once, the less time the importer will need. The downside is that
the amount of memory required by the import process will increase as
well. Therefore, it's a trade-off between memory consumption and
import speed.

See also:

* controller/jobs/stock/import/csv/backup
* controller/jobs/stock/import/csv/location
* controller/jobs/stock/import/csv/skip-lines

## name

Class name of the used stock suggestions scheduler controller implementation

```
controller/jobs/stock/import/csv/name = 
```

* Default: 
* Type: string - Last part of the class name
* Since: 2019.04

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Stock\Import\Csv\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Stock\Import\Csv\Mycsv
```

then you have to set the this configuration option:

```
 controller/jobs/stock/import/csv/name = Mycsv
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCsv"!


## skip-lines

Number of rows skipped in front of each CSV files

```
controller/jobs/stock/import/csv/skip-lines = 0
```

* Default: 0
* Type: integer - Number of rows
* Since: 2019.04

Some CSV files contain header information describing the content of
the column values. These data is for informational purpose only and
can't be imported into the database. Using this option, you can
define the number of lines that should be left out before the import
begins.

See also:

* controller/jobs/stock/import/csv/backup
* controller/jobs/stock/import/csv/location
* controller/jobs/stock/import/csv/max-size