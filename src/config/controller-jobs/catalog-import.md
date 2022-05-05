
# csv
## backup

Name of the backup for sucessfully imported files

```
controller/jobs/catalog/import/csv/backup = tmp/notexist/import.zip
```

* Default:
* Type: integer - Name of the backup file, optionally with date/time placeholders
* Since: 2018.04

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

**Note:** If no backup name is configured, the file or directory
won't be moved away. Please make also sure that the parent directory
and the new directory are writable so the file or directory could be
moved.

See also:

* controller/jobs/catalog/import/csv/domains
* controller/jobs/catalog/import/csv/mapping
* controller/jobs/catalog/import/csv/skip-lines
* controller/jobs/catalog/import/csv/converter
* controller/jobs/catalog/import/csv/strict
* controller/common/catalog/import/csv/max-size

## container/content

Name of the content type inside the container to read the data from

```
controller/jobs/catalog/import/csv/container/content = CSV
```

* Default: CSV
* Type: array - Content type name
* Since: 2018.04

The content type must always be a CSV-like format and there are
currently two format types that are supported:

* CSV

See also:

* controller/jobs/catalog/import/csv/location
* controller/jobs/catalog/import/csv/container/type
* controller/jobs/catalog/import/csv/container/options

## container/options

List of file container options for the catalog import files

```
controller/jobs/catalog/import/csv/container/options = Array
(
)
```

* Default: Array
(
)

* Type: array - Associative list of option name/value pairs
* Since: 2018.04

Some container/content type allow you to hand over additional settings
for configuration. Please have a look at the article about
[container/content files](http://aimeos.org/docs/Developers/Utility/Create_and_read_files)
for more information.

See also:

* controller/jobs/catalog/import/csv/location
* controller/jobs/catalog/import/csv/container/content
* controller/jobs/catalog/import/csv/container/type

## container/type

Nave of the container type to read the data from

```
controller/jobs/catalog/import/csv/container/type = Zip
```

* Default: Directory
* Type: string - Container type name
* Since: 2018.04

The container type tells the importer how it should retrieve the data.
There are currently three container types that support the necessary
CSV content:

* Directory
* Zip

See also:

* controller/jobs/catalog/import/csv/location
* controller/jobs/catalog/import/csv/container/content
* controller/jobs/catalog/import/csv/container/options

## converter

List of converter names for the values at the position in the CSV file

```
controller/jobs/catalog/import/csv/converter = Array
(
)
```

* Default: Array
(
)

* Type: array - Associative list of position/converter name (or list of names) pairs
* Since: 2018.04

This configuration setting overwrites the shared option
"controller/common/catalog/import/csv/converter" if you need a
specific setting for the job controller. Otherwise, you should
use the shared option for consistency.

See also:

* controller/jobs/catalog/import/csv/domains
* controller/jobs/catalog/import/csv/mapping
* controller/jobs/catalog/import/csv/skip-lines
* controller/jobs/catalog/import/csv/strict
* controller/jobs/catalog/import/csv/backup
* controller/common/catalog/import/csv/max-size

## decorators/excludes

Excludes decorators added by the "common" option from the catalog import CSV job controller

```
controller/jobs/catalog/import/csv/decorators/excludes = Array
(
)
```

* Default: Array
(
)

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
 controller/jobs/catalog/import/csv/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/catalog/import/csv/decorators/global
* controller/jobs/catalog/import/csv/decorators/local

## decorators/global

Adds a list of globally available decorators only to the catalog import CSV job controller

```
controller/jobs/catalog/import/csv/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/catalog/import/csv/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/catalog/import/csv/decorators/excludes
* controller/jobs/catalog/import/csv/decorators/local

## decorators/local

Adds a list of local decorators only to the catalog import CSV job controller

```
controller/jobs/catalog/import/csv/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Catalog\Import\Csv\Decorator\*") around the job
controller.

```
 controller/jobs/catalog/import/csv/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Catalog\Import\Csv\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/catalog/import/csv/decorators/excludes
* controller/jobs/catalog/import/csv/decorators/global

## domains

List of item domain names that should be retrieved along with the catalog items

```
controller/jobs/catalog/import/csv/domains = Array
(
    [0] => media
    [1] => text
)
```

* Default: Array
(
    [0] => media
    [1] => text
)

* Type: array - Associative list of MShop item domain names
* Since: 2018.04

This configuration setting overwrites the shared option
"controller/common/catalog/import/csv/domains" if you need a
specific setting for the job controller. Otherwise, you should
use the shared option for consistency.

See also:

* controller/jobs/catalog/import/csv/mapping
* controller/jobs/catalog/import/csv/skip-lines
* controller/jobs/catalog/import/csv/converter
* controller/jobs/catalog/import/csv/strict
* controller/jobs/catalog/import/csv/backup
* controller/common/catalog/import/csv/max-size

## location

File or directory where the content is stored which should be imported

```
controller/jobs/catalog/import/csv/location = tmp/import.zip
```

* Default:
* Type: string - Absolute file or directory path
* Since: 2018.04

You need to configure the file or directory that acts as container
for the CSV files that should be imported. It should be an absolute
path to be sure but can be relative path if you absolutely know from
where the job will be executed from.

The path can point to any supported container format as long as the
content is in CSV format, e.g.

* Directory container / CSV file
* Zip container / compressed CSV file

See also:

* controller/jobs/catalog/import/csv/container/type
* controller/jobs/catalog/import/csv/container/content
* controller/jobs/catalog/import/csv/container/options

## mapping

List of mappings between the position in the CSV file and item keys

```
controller/jobs/catalog/import/csv/mapping = Array
(
    [item] => Array
        (
            [0] => catalog.code
            [1] => catalog.parent
            [2] => catalog.label
            [3] => catalog.status
        )

    [text] => Array
        (
            [4] => text.type
            [5] => text.content
        )

    [media] => Array
        (
            [6] => media.url
        )

)
```

* Default: Array
(
    [item] => Array
        (
            [0] => catalog.code
            [1] => catalog.parent
            [2] => catalog.label
            [3] => catalog.status
        )

    [text] => Array
        (
            [4] => text.type
            [5] => text.content
        )

    [media] => Array
        (
            [6] => media.url
        )

)

* Type: array - Associative list of processor names and lists of key/position pairs
* Since: 2018.04

This configuration setting overwrites the shared option
"controller/common/catalog/import/csv/mapping" if you need a
specific setting for the job controller. Otherwise, you should
use the shared option for consistency.

See also:

* controller/jobs/catalog/import/csv/domains
* controller/jobs/catalog/import/csv/skip-lines
* controller/jobs/catalog/import/csv/converter
* controller/jobs/catalog/import/csv/strict
* controller/jobs/catalog/import/csv/backup
* controller/common/catalog/import/csv/max-size

## name

Class name of the used catalog suggestions scheduler controller implementation

```
controller/jobs/catalog/import/csv/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.04

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Catalog\Import\Csv\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Catalog\Import\Csv\Mycsv
```

then you have to set the this configuration option:

```
 controller/jobs/catalog/import/csv/name = Mycsv
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
controller/jobs/catalog/import/csv/skip-lines = 1
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

* controller/jobs/catalog/import/csv/domains
* controller/jobs/catalog/import/csv/mapping
* controller/jobs/catalog/import/csv/converter
* controller/jobs/catalog/import/csv/strict
* controller/jobs/catalog/import/csv/backup
* controller/common/catalog/import/csv/max-size

## strict

Log all columns from the file that are not mapped and therefore not imported

```
controller/jobs/catalog/import/csv/strict = 1
```

* Default: 1
* Type: boolen - True if not imported columns should be logged, false if not
* Since: 2015.08

Depending on the mapping, there can be more columns in the CSV file
than those which will be imported. This can be by purpose if you want
to import only selected columns or if you've missed to configure one
or more columns. This configuration option will log all columns that
have not been imported if set to true. Otherwise, the left over fields
in the imported line will be silently ignored.

See also:

* controller/jobs/catalog/import/csv/domains
* controller/jobs/catalog/import/csv/mapping
* controller/jobs/catalog/import/csv/skip-lines
* controller/jobs/catalog/import/csv/converter
* controller/jobs/catalog/import/csv/backup
* controller/common/catalog/import/csv/max-size

# xml
## backup

Name of the backup for sucessfully imported files

```
controller/jobs/catalog/import/xml/backup =
```

* Default:
* Type: integer - Name of the backup file, optionally with date/time placeholders
* Since: 2019.04

After a XML file was imported successfully, you can move it to another
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

**Note:** If no backup name is configured, the file or directory
won't be moved away. Please make also sure that the parent directory
and the new directory are writable so the file or directory could be
moved.

See also:

* controller/jobs/catalog/import/xml/domains
* controller/jobs/catalog/import/xml/max-query

## decorators/excludes

Excludes decorators added by the "common" option from the catalog import CSV job controller

```
controller/jobs/catalog/import/xml/decorators/excludes = Array
(
)
```

* Default: Array
(
)

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
 controller/jobs/catalog/import/xml/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/catalog/import/xml/decorators/global
* controller/jobs/catalog/import/xml/decorators/local

## decorators/global

Adds a list of globally available decorators only to the catalog import CSV job controller

```
controller/jobs/catalog/import/xml/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2019.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/catalog/import/xml/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/catalog/import/xml/decorators/excludes
* controller/jobs/catalog/import/xml/decorators/local

## decorators/local

Adds a list of local decorators only to the catalog import CSV job controller

```
controller/jobs/catalog/import/xml/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2019.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Catalog\Import\Xml\Decorator\*") around the job
controller.

```
 controller/jobs/catalog/import/xml/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Catalog\Import\Xml\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/catalog/import/xml/decorators/excludes
* controller/jobs/catalog/import/xml/decorators/global

## domains

List of item domain names that should be retrieved along with the catalog items

```
controller/jobs/catalog/import/xml/domains = Array
(
    [media] => media
    [product] => product
    [text] => text
)
```

* Default: Array
(
)

* Type: array - Associative list of MShop item domain names
* Since: 2019.04

This configuration setting overwrites the shared option
"controller/common/catalog/import/xml/domains" if you need a
specific setting for the job controller. Otherwise, you should
use the shared option for consistency.

See also:

* controller/jobs/catalog/import/xml/backup
* controller/jobs/catalog/import/xml/max-query

## location

File or directory where the content is stored which should be imported

```
controller/jobs/catalog/import/xml/location =
```

* Default:
* Type: string - Absolute file or directory path
* Since: 2019.04

You need to configure the XML file or directory with the XML files that
should be imported. It should be an absolute path to be sure but can be
relative path if you absolutely know from where the job will be executed
from.

See also:

* controller/jobs/catalog/import/xml/container/type
* controller/jobs/catalog/import/xml/container/content
* controller/jobs/catalog/import/xml/container/options

## name

Class name of the used catalog suggestions scheduler controller implementation

```
controller/jobs/catalog/import/xml/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2019.04

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Catalog\Import\Xml\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Catalog\Import\Xml\Myxml
```

then you have to set the this configuration option:

```
 controller/jobs/catalog/import/xml/name = Myxml
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyXml"!
