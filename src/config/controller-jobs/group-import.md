
# xml
## backup

Name of the backup for sucessfully imported files

```
controller/jobs/group/import/xml/backup = 
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

* controller/jobs/group/import/xml/domains
* controller/jobs/group/import/xml/location
* controller/jobs/group/import/xml/max-query

## decorators/excludes

Excludes decorators added by the "common" option from the group import CSV job controller

```
controller/jobs/group/import/xml/decorators/excludes = Array
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
 controller/jobs/group/import/xml/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\Controller\Jobs\Common\Decorator\*") added via
"controller/jobs/common/decorators/default" to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/group/import/xml/decorators/global
* controller/jobs/group/import/xml/decorators/local

## decorators/global

Adds a list of globally available decorators only to the group import CSV job controller

```
controller/jobs/group/import/xml/decorators/global = Array
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
 controller/jobs/group/import/xml/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\Controller\Jobs\Common\Decorator\Decorator1" only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/group/import/xml/decorators/excludes
* controller/jobs/group/import/xml/decorators/local

## decorators/local

Adds a list of local decorators only to the group import CSV job controller

```
controller/jobs/group/import/xml/decorators/local = Array
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
("\Aimeos\Controller\Jobs\Group\Import\Xml\Decorator\*") around the job
controller.

```
 controller/jobs/group/import/xml/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\Controller\Jobs\Group\Import\Xml\Decorator\Decorator2"
only to the job controller.

See also:

* controller/jobs/common/decorators/default
* controller/jobs/group/import/xml/decorators/excludes
* controller/jobs/group/import/xml/decorators/global

## location

Directory where the CSV files are stored which should be imported

```
controller/jobs/group/import/xml/location = /var/www/aimeos/ext/ai-controller-jobs/tests/Controller/Jobs/Xml/Import/_testfiles
```

* Default: `group`
* Type: string - Relative path to the XML files
* Since: 2019.04

It's the relative path inside the "fs-import" virtual file system
configuration. The default location of the "fs-import" file system is:

* Laravel: ./storage/import/
* TYPO3: /uploads/tx_aimeos/.secure/import/

See also:

* controller/jobs/group/import/xml/backup
* controller/jobs/group/import/xml/domains
* controller/jobs/group/import/xml/max-query

## max-query

Maximum number of XML nodes processed at once

```
controller/jobs/group/import/xml/max-query = 100
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

* controller/jobs/group/import/xml/domains
* controller/jobs/group/import/xml/location
* controller/jobs/group/import/xml/backup

## name

Class name of the used group suggestions scheduler controller implementation

```
controller/jobs/group/import/xml/name = Standard
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
 \Aimeos\Controller\Jobs\Group\Import\Xml\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\Controller\Jobs\Group\Import\Xml\Myxml
```

then you have to set the this configuration option:

```
 controller/jobs/group/import/xml/name = Myxml
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyXml"!
