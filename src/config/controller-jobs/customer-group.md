
# import
## xml/backup

Name of the backup for sucessfully imported files

```
controller/jobs/customer/group/import/xml/backup = 
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

* controller/jobs/customer/group/import/xml/domains
* controller/jobs/customer/group/import/xml/max-query

## xml/location

File or directory where the content is stored which should be imported

```
controller/jobs/customer/group/import/xml/location = /home/nose/Aimeos/src/core/aimeos-extensions/ai-controller-jobs/tests/Controller/Jobs/Xml/Import/_testfiles
```

* Default: 
* Type: string - Absolute file or directory path
* Since: 2019.04

You need to configure the XML file or directory with the XML files that
should be imported. It should be an absolute path to be sure but can be
relative path if you absolutely know from where the job will be executed
from.

See also:

* controller/jobs/customer/group/import/xml/container/type
* controller/jobs/customer/group/import/xml/container/content
* controller/jobs/customer/group/import/xml/container/options

## xml/max-query

Maximum number of XML nodes processed at once

```
controller/jobs/customer/group/import/xml/max-query = 1000
```

* Default: 1000
* Type: integer - Number of XML nodes
* Since: 2019.04

Processing and fetching several customer group items at once speeds up importing
the XML files. The more items can be processed at once, the faster the
import. More items also increases the memory usage of the importer and
thus, this parameter should be low enough to avoid reaching the memory
limit of the PHP process.

See also:

* controller/jobs/customer/group/import/xml/domains
* controller/jobs/customer/group/import/xml/backup