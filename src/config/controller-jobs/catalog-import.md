
# csv
## backup

Name of the backup for sucessfully imported files

```
controller/jobs/catalog/import/csv/backup = backup-%Y-%m-%d.csv
```

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

**Note:** If no backup name is configured, the file will be removed!

See also:

* controller/jobs/catalog/import/csv/converter
* controller/jobs/catalog/import/csv/domains
* controller/jobs/catalog/import/csv/location
* controller/jobs/catalog/import/csv/mapping
* controller/jobs/catalog/import/csv/max-size
* controller/jobs/catalog/import/csv/skip-lines

## decorators/excludes

Excludes decorators added by the "common" option from the catalog import CSV job controller

```
controller/jobs/catalog/import/csv/decorators/excludes = 
```

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
controller/jobs/catalog/import/csv/decorators/global = 
```

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
controller/jobs/catalog/import/csv/decorators/local = 
```

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

For efficient processing, the items associated to the catalogs can be
fetched to, minimizing the number of database queries required. To be
most effective, the list of item domain names should be used in the
mapping configuration too, so the retrieved items will be used during
the import.

See also:

* controller/jobs/catalog/import/csv/backup
* controller/jobs/catalog/import/csv/converter
* controller/jobs/catalog/import/csv/location
* controller/jobs/catalog/import/csv/mapping
* controller/jobs/catalog/import/csv/max-size
* controller/jobs/catalog/import/csv/skip-lines

## location

Directory where the CSV files are stored which should be imported

```
controller/jobs/catalog/import/csv/location = catalog
```

* Default: catalog
* Type: string - Relative path to the CSV files
* Since: 2015.08

It's the relative path inside the "fs-import" virtual file system
configuration. The default location of the "fs-import" file system is:

* Laravel: ./storage/import/
* TYPO3: /uploads/tx_aimeos/.secure/import/

See also:

* controller/jobs/catalog/import/csv/backup
* controller/jobs/catalog/import/csv/converter
* controller/jobs/catalog/import/csv/domains
* controller/jobs/catalog/import/csv/location
* controller/jobs/catalog/import/csv/mapping
* controller/jobs/catalog/import/csv/max-size
* controller/jobs/catalog/import/csv/skip-lines

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

The importer have to know which data is at which position in the CSV
file. Therefore, you need to specify a mapping between each position
and the MShop domain item key (e.g. "catalog.code") it represents.

You can use all domain item keys which are used in the fromArray()
methods of the item classes.

These mappings are grouped together by their processor names, which
are responsible for importing the data, e.g. all mappings in "item"
will be processed by the base catalog importer while the mappings in
"text" will be imported by the text processor.

See also:

* controller/jobs/catalog/import/csv/backup
* controller/jobs/catalog/import/csv/converter
* controller/jobs/catalog/import/csv/domains
* controller/jobs/catalog/import/csv/location
* controller/jobs/catalog/import/csv/max-size
* controller/jobs/catalog/import/csv/skip-lines

## max-size

Maximum number of CSV rows to import at once

```
controller/jobs/catalog/import/csv/max-size = 1000
```

* Default: 1000
* Type: integer - Number of rows
* Since: 2018.04

It's more efficient to read and import more than one row at a time
to speed up the import. Usually, the bigger the chunk that is imported
at once, the less time the importer will need. The downside is that
the amount of memory required by the import process will increase as
well. Therefore, it's a trade-off between memory consumption and
import speed.

See also:

* controller/jobs/catalog/import/csv/backup
* controller/jobs/catalog/import/csv/converter
* controller/jobs/catalog/import/csv/domains
* controller/jobs/catalog/import/csv/location
* controller/jobs/catalog/import/csv/mapping
* controller/jobs/catalog/import/csv/skip-lines

## name

Class name of the used catalog CSV importer implementation

```
controller/jobs/catalog/import/csv/name = 
```

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

* controller/jobs/catalog/import/csv/backup
* controller/jobs/catalog/import/csv/converter
* controller/jobs/catalog/import/csv/domains
* controller/jobs/catalog/import/csv/location
* controller/jobs/catalog/import/csv/mapping
* controller/jobs/catalog/import/csv/max-size

# xml
## backup

Name of the backup for sucessfully imported files

```
controller/jobs/catalog/import/xml/backup = 
```

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

**Note:** If no backup name is configured, the file will be removed!

See also:

* controller/jobs/catalog/import/xml/domains
* controller/jobs/catalog/import/xml/location
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
    [0] => media
    [1] => text
)

* Type: array - Associative list of MShop item domain names
* Since: 2019.04

For efficient processing, the items associated to the products can be
fetched to, minimizing the number of database queries required. To be
most effective, the list of item domain names should be used in the
mapping configuration too, so the retrieved items will be used during
the import.

See also:

* controller/jobs/catalog/import/xml/backup
* controller/jobs/catalog/import/xml/location
* controller/jobs/catalog/import/xml/max-query

## location

Directory where the CSV files are stored which should be imported

```
controller/jobs/catalog/import/xml/location = /var/www/aimeos/ext/ai-controller-jobs/tests/Controller/Jobs/Xml/Import/_testfiles
```

* Default: catalog
* Type: string - Relative path to the XML files
* Since: 2019.04

It's the relative path inside the "fs-import" virtual file system
configuration. The default location of the "fs-import" file system is:

* Laravel: ./storage/import/
* TYPO3: /uploads/tx_aimeos/.secure/import/

See also:

* controller/jobs/catalog/import/xml/backup
* controller/jobs/catalog/import/xml/domains
* controller/jobs/catalog/import/xml/max-query

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
