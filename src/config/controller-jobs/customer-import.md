
# csv
## backup

Name of the backup for sucessfully imported files

```
controller/jobs/customer/import/csv/backup = backup-%Y-%m-%d.csv
```

* Type: integer - Name of the backup file, optionally with date/time placeholders
* Since: 2025.10

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

* controller/jobs/customer/import/csv/cleanup
* controller/jobs/customer/import/csv/domains
* controller/jobs/customer/import/csv/location
* controller/jobs/customer/import/csv/mapping
* controller/jobs/customer/import/csv/max-size
* controller/jobs/customer/import/csv/skip-lines

## checks

```
controller/jobs/customer/import/csv/checks = Array
(
)
```

* Default: 
```
Array
(
)
```


## cleanup

Deletes all customers with categories which havn't been updated

```
controller/jobs/customer/import/csv/cleanup = 
```

* Default: ``
* Type: bool - TRUE to delete all untouched customers, FALSE to keep them
* Since: 2025.10

By default, the customer importer only adds new and updates existing
customers but doesn't delete any customers. If you want to remove all
customers which haven't been updated during the import, then set this
configuration option to "true". This will remove all customers which
are not assigned to any category but keep the ones without categories,
e.g. rebate customers.

See also:

* controller/jobs/customer/import/csv/backup
* controller/jobs/customer/import/csv/domains
* controller/jobs/customer/import/csv/location
* controller/jobs/customer/import/csv/mapping
* controller/jobs/customer/import/csv/max-size
* controller/jobs/customer/import/csv/skip-lines

## decorators/excludes

Excludes decorators added by the "common" option from the customer import CSV job controller

```
controller/jobs/customer/import/csv/decorators/excludes = Array
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
* Since: 2025.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/customer/import/csv/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/customer/import/csv/decorators/global
* controller/jobs/customer/import/csv/decorators/local

## decorators/global

Adds a list of globally available decorators only to the customer import CSV job controller

```
controller/jobs/customer/import/csv/decorators/global = Array
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
* Since: 2025.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/customer/import/csv/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/customer/import/csv/decorators/excludes
* controller/jobs/customer/import/csv/decorators/local

## decorators/local

Adds a list of local decorators only to the customer import CSV job controller

```
controller/jobs/customer/import/csv/decorators/local = Array
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
* Since: 2025.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Customer\Import\Csv\Decorator\*") around the job
controller.

```
 controller/jobs/customer/import/csv/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Customer\Import\Csv\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/customer/import/csv/decorators/excludes
* controller/jobs/customer/import/csv/decorators/global

## domains

List of item domain names that should be retrieved along with the customer items

```
controller/jobs/customer/import/csv/domains = Array
(
    [0] => customer/address
    [1] => customer/property
)
```

* Default: 
```
Array
(
    [0] => customer/address
    [1] => customer/property
)
```
* Type: array - Associative list of MShop item domain names
* Since: 2025.10

For efficient processing, the items associated to the customers can be
fetched to, minimizing the number of database queries required. To be
most effective, the list of item domain names should be used in the
mapping configuration too, so the retrieved items will be used during
the import.

See also:

* controller/jobs/customer/import/csv/backup
* controller/jobs/customer/import/csv/cleanup
* controller/jobs/customer/import/csv/location
* controller/jobs/customer/import/csv/mapping
* controller/jobs/customer/import/csv/max-size
* controller/jobs/customer/import/csv/skip-lines

## html

```
controller/jobs/customer/import/csv/html = 
```

* Default: ``


## location

Directory where the CSV files are stored which should be imported

```
controller/jobs/customer/import/csv/location = customer
```

* Default: `customer`
* Type: string - Relative path to the CSV files
* Since: 2015.08

It's the relative path inside the "fs-import" virtual file system
configuration. The default location of the "fs-import" file system is:

* Laravel: ./storage/import/
* TYPO3: /uploads/tx_aimeos/.secure/import/

See also:

* controller/jobs/customer/import/csv/backup
* controller/jobs/customer/import/csv/cleanup
* controller/jobs/customer/import/csv/domains
* controller/jobs/customer/import/csv/location
* controller/jobs/customer/import/csv/mapping
* controller/jobs/customer/import/csv/max-size
* controller/jobs/customer/import/csv/skip-lines

## mapping

List of mappings between the position in the CSV file and item keys

```
controller/jobs/customer/import/csv/mapping = Array
(
    [item] => Array
        (
            [0] => customer.code
            [1] => customer.label
            [2] => customer.salutation
            [3] => customer.company
            [4] => customer.vatid
            [5] => customer.title
            [6] => customer.firstname
            [7] => customer.lastname
            [8] => customer.address1
            [9] => customer.address2
            [10] => customer.address3
            [11] => customer.postal
            [12] => customer.city
            [13] => customer.state
            [14] => customer.languageid
            [15] => customer.countryid
            [16] => customer.telephone
            [17] => customer.telefax
            [18] => customer.mobile
            [19] => customer.email
            [20] => customer.website
            [21] => customer.longitude
            [22] => customer.latitude
            [23] => customer.birthday
            [24] => customer.status
        )

    [group] => Array
        (
            [25] => customer.groups
        )

    [address] => Array
        (
            [26] => customer.address.salutation
            [27] => customer.address.company
            [28] => customer.address.vatid
            [29] => customer.address.title
            [30] => customer.address.firstname
            [31] => customer.address.lastname
            [32] => customer.address.address1
            [33] => customer.address.address2
            [34] => customer.address.address3
            [35] => customer.address.postal
            [36] => customer.address.city
            [37] => customer.address.state
            [38] => customer.address.languageid
            [39] => customer.address.countryid
            [40] => customer.address.telephone
            [41] => customer.address.telefax
            [42] => customer.address.mobile
            [43] => customer.address.email
            [44] => customer.address.website
            [45] => customer.address.longitude
            [46] => customer.address.latitude
            [47] => customer.address.birthday
        )

    [property] => Array
        (
            [48] => customer.property.type
            [49] => customer.property.languageid
            [50] => customer.property.value
        )

)
```

* Default: 
```
Array
(
    [item] => Array
        (
            [0] => customer.code
            [1] => customer.label
            [2] => customer.salutation
            [3] => customer.company
            [4] => customer.vatid
            [5] => customer.title
            [6] => customer.firstname
            [7] => customer.lastname
            [8] => customer.address1
            [9] => customer.address2
            [10] => customer.address3
            [11] => customer.postal
            [12] => customer.city
            [13] => customer.state
            [14] => customer.languageid
            [15] => customer.countryid
            [16] => customer.telephone
            [17] => customer.telefax
            [18] => customer.mobile
            [19] => customer.email
            [20] => customer.website
            [21] => customer.longitude
            [22] => customer.latitude
            [23] => customer.birthday
            [24] => customer.status
        )

    [group] => Array
        (
            [25] => customer.groups
        )

    [address] => Array
        (
            [26] => customer.address.salutation
            [27] => customer.address.company
            [28] => customer.address.vatid
            [29] => customer.address.title
            [30] => customer.address.firstname
            [31] => customer.address.lastname
            [32] => customer.address.address1
            [33] => customer.address.address2
            [34] => customer.address.address3
            [35] => customer.address.postal
            [36] => customer.address.city
            [37] => customer.address.state
            [38] => customer.address.languageid
            [39] => customer.address.countryid
            [40] => customer.address.telephone
            [41] => customer.address.telefax
            [42] => customer.address.mobile
            [43] => customer.address.email
            [44] => customer.address.website
            [45] => customer.address.longitude
            [46] => customer.address.latitude
            [47] => customer.address.birthday
        )

    [property] => Array
        (
            [48] => customer.property.type
            [49] => customer.property.languageid
            [50] => customer.property.value
        )

)
```
* Type: array - Associative list of processor names and lists of key/position pairs
* Since: 2025.10

The importer have to know which data is at which position in the CSV
file. Therefore, you need to specify a mapping between each position
and the MShop domain item key (e.g. "customer.code") it represents.

You can use all domain item keys which are used in the fromArray()
methods of the item classes.

These mappings are grouped together by their processor names, which
are responsible for importing the data, e.g. all mappings in "item"
will be processed by the base customer importer while the mappings in
"text" will be imported by the text processor.

See also:

* controller/jobs/customer/import/csv/backup
* controller/jobs/customer/import/csv/cleanup
* controller/jobs/customer/import/csv/domains
* controller/jobs/customer/import/csv/location
* controller/jobs/customer/import/csv/max-size
* controller/jobs/customer/import/csv/skip-lines

## max-size

Maximum number of CSV rows to import at once

```
controller/jobs/customer/import/csv/max-size = 1000
```

* Default: `1000`
* Type: integer - Number of rows
* Since: 2025.10

It's more efficient to read and import more than one row at a time
to speed up the import. Usually, the bigger the chunk that is imported
at once, the less time the importer will need. The downside is that
the amount of memory required by the import process will increase as
well. Therefore, it's a trade-off between memory consumption and
import speed.

See also:

* controller/jobs/customer/import/csv/backup
* controller/jobs/customer/import/csv/cleanup
* controller/jobs/customer/import/csv/domains
* controller/jobs/customer/import/csv/location
* controller/jobs/customer/import/csv/mapping
* controller/jobs/customer/import/csv/skip-lines

## name

Class name of the used customer suggestions scheduler controller implementation

```
controller/jobs/customer/import/csv/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2025.10

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Customer\Import\Csv\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Customer\Import\Csv\Mycsv
```

then you have to set the this configuration option:

```
 controller/jobs/customer/import/csv/name = Mycsv
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCsv"!


## processor/address/name

Name of the address processor implementation

```
controller/jobs/customer/import/csv/processor/address/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2025.10

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Customer\Import\Csv\Processor\Address\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## processor/group/allowed

```
controller/jobs/customer/import/csv/processor/group/allowed = 
```



## processor/group/denied

```
controller/jobs/customer/import/csv/processor/group/denied = Array
(
    [0] => admin
    [1] => editor
)
```

* Default: 
```
Array
(
    [0] => admin
    [1] => editor
)
```


## processor/group/name

Name of the group processor implementation

```
controller/jobs/customer/import/csv/processor/group/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2025.10

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Customer\Import\Csv\Processor\Group\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## processor/property/name

Name of the property processor implementation

```
controller/jobs/customer/import/csv/processor/property/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the processor class name
* Since: 2025.10

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Customer\Import\Csv\Processor\Property\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".


## skip-lines

Number of rows skipped in front of each CSV files

```
controller/jobs/customer/import/csv/skip-lines = 1
```

* Default: `0`
* Type: integer - Number of rows
* Since: 2015.08

Some CSV files contain header information describing the content of
the column values. These data is for informational purpose only and
can't be imported into the database. Using this option, you can
define the number of lines that should be left out before the import
begins.

See also:

* controller/jobs/customer/import/csv/backup
* controller/jobs/customer/import/csv/cleanup
* controller/jobs/customer/import/csv/domains
* controller/jobs/customer/import/csv/location
* controller/jobs/customer/import/csv/mapping
* controller/jobs/customer/import/csv/max-size

# xml
## backup

Name of the backup for sucessfully imported files

```
controller/jobs/customer/import/xml/backup = 
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

* controller/jobs/customer/import/xml/domains
* controller/jobs/customer/import/xml/location
* controller/jobs/customer/import/xml/max-query

## decorators/excludes

Excludes decorators added by the "common" option from the customer import CSV job controller

```
controller/jobs/customer/import/xml/decorators/excludes = Array
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
* Since: 2019.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"controller/jobs/common/decorators/default" before they are wrapped
around the job controller.

```
 controller/jobs/customer/import/xml/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/customer/import/xml/decorators/global
* controller/jobs/customer/import/xml/decorators/local

## decorators/global

Adds a list of globally available decorators only to the customer import CSV job controller

```
controller/jobs/customer/import/xml/decorators/global = Array
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
* Since: 2019.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\Controller\Jobs\Common\Decorator\*") around the job controller.

```
 controller/jobs/customer/import/xml/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/customer/import/xml/decorators/excludes
* controller/jobs/customer/import/xml/decorators/local

## decorators/local

Adds a list of local decorators only to the customer import CSV job controller

```
controller/jobs/customer/import/xml/decorators/local = Array
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
* Since: 2019.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\Controller\Jobs\Customer\Import\Xml\Decorator\*") around the job
controller.

```
 controller/jobs/customer/import/xml/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Customer\Import\Xml\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/customer/import/xml/decorators/excludes
* controller/jobs/customer/import/xml/decorators/global

## domains

List of item domain names that should be retrieved along with the attribute items

```
controller/jobs/customer/import/xml/domains = Array
(
    [0] => customer/address
    [1] => group
    [2] => customer/property
    [3] => media
    [4] => product
    [5] => text
)
```

* Default: 
```
Array
(
    [0] => customer/address
    [1] => group
    [2] => customer/property
    [3] => media
    [4] => product
    [5] => text
)
```
* Type: array - Associative list of MShop item domain names
* Since: 2019.04

For efficient processing, the items associated to the customers can be
fetched to, minimizing the number of database queries required. To be
most effective, the list of item domain names should be used in the
mapping configuration too, so the retrieved items will be used during
the import.

See also:

* controller/jobs/customer/import/xml/backup
* controller/jobs/customer/import/xml/location
* controller/jobs/customer/import/xml/max-query

## location

Directory where the CSV files are stored which should be imported

```
controller/jobs/customer/import/xml/location = /var/www/aimeos/ext/ai-controller-jobs/tests/Controller/Jobs/Xml/Import/_testfiles
```

* Default: `customer`
* Type: string - Relative path to the XML files
* Since: 2019.04

It's the relative path inside the "fs-import" virtual file system
configuration. The default location of the "fs-import" file system is:

* Laravel: ./storage/import/
* TYPO3: /uploads/tx_aimeos/.secure/import/

See also:

* controller/jobs/customer/import/xml/backup
* controller/jobs/customer/import/xml/domains
* controller/jobs/customer/import/xml/max-query

## max-query

Maximum number of XML nodes processed at once

```
controller/jobs/customer/import/xml/max-query = 100
```

* Default: `100`
* Type: integer - Number of XML nodes
* Since: 2019.04

Processing and fetching several attribute items at once speeds up importing
the XML files. The more items can be processed at once, the faster the
import. More items also increases the memory usage of the importer and
thus, this parameter should be low enough to avoid reaching the memory
limit of the PHP process.

See also:

* controller/jobs/customer/import/xml/domains
* controller/jobs/customer/import/xml/location
* controller/jobs/customer/import/xml/backup

## name

Class name of the used customer suggestions scheduler controller implementation

```
controller/jobs/customer/import/xml/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2019.04

Each default job controller can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the controller factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\Controller\Jobs\Customer\Import\Xml\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Customer\Import\Xml\Myxml
```

then you have to set the this configuration option:

```
 controller/jobs/customer/import/xml/name = Myxml
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyXml"!


## processor/group/name

Name of the group processor implementation

```
controller/jobs/customer/import/xml/processor/group/name = 
```

* Type: string - Last part of the processor class name
* Since: 2019.04

Use "Myname" if your class is named "\Aimeos\Controller\Jobs\Common\Customer\Import\Xml\Processor\Group\Myname".
The name is case-sensitive and you should avoid camel case names like "MyName".
