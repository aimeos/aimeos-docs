
# count
## ansi

Counts the number of records matched by the given criteria in the database

```
madmin/job/manager/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM(
 	SELECT majob."id"
 	FROM "madmin_job" majob
 	:joins
 	WHERE :cond
 	ORDER BY "id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: madmin/job/manager/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the job
database. The records must be from one of the sites that are
configured via the context item. If the current site is part of
a tree of sites, the statement can count all records from the
current site and the complete sub-tree of sites.

As the records can normally be limited by criteria from sub-managers,
their tables must be joined in the SQL context. This is done by
using the "internaldeps" property from the definition of the ID
column of the sub-managers. These internal dependencies specify
the JOIN between the tables and the used columns for joining. The
":joins" placeholder is then replaced by the JOIN strings from
the sub-managers.

To limit the records matched, conditions can be added to the given
criteria object. It can contain comparisons like column names that
must match specific values which can be combined by AND, OR or NOT
operators. The resulting string of SQL conditions replaces the
":cond" placeholder before the statement is sent to the database
server.

Both, the strings for ":joins" and for ":cond" are the same as for
the "search" SQL statement.

Contrary to the "search" statement, it doesn't return any records
but instead the number of records that have been found. As counting
thousands of records can be a long running task, the maximum number
of counted records is limited for performance reasons.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* madmin/job/manager/insert/ansi
* madmin/job/manager/update/ansi
* madmin/job/manager/newid/ansi
* madmin/job/manager/delete/ansi
* madmin/job/manager/search/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
madmin/job/manager/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM(
 	SELECT majob."id"
 	FROM "madmin_job" majob
 	:joins
 	WHERE :cond
 	ORDER BY "id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM(
 	SELECT majob."id"
 	FROM "madmin_job" majob
 	:joins
 	WHERE :cond
 	ORDER BY "id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* madmin/job/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the job manager

```
madmin/job/manager/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"madmin/common/manager/decorators/default" before they are wrapped
around the job manager.

```
 madmin/job/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"madmin/common/manager/decorators/default" for the job manager.

See also:

* madmin/common/manager/decorators/default
* madmin/job/manager/decorators/global
* madmin/job/manager/decorators/local

## global

Adds a list of globally available decorators only to the job manager

```
madmin/job/manager/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the job manager.

```
 madmin/job/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the job controller.

See also:

* madmin/common/manager/decorators/default
* madmin/job/manager/decorators/excludes
* madmin/job/manager/decorators/local

## local

Adds a list of local decorators only to the job manager

```
madmin/job/manager/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the job manager.

```
 madmin/job/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator2" only to the job
controller.

See also:

* madmin/common/manager/decorators/default
* madmin/job/manager/decorators/excludes
* madmin/job/manager/decorators/global

# delete
## ansi

Deletes the items matched by the given IDs from the database

```
madmin/job/manager/delete/ansi = 
 DELETE FROM "madmin_job"
 WHERE :cond
 AND "siteid" = ?
```

* Default: madmin/job/manager/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the job database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* madmin/job/manager/insert/ansi
* madmin/job/manager/update/ansi
* madmin/job/manager/newid/ansi
* madmin/job/manager/search/ansi
* madmin/job/manager/count/ansi

## mysql

Deletes the items matched by the given IDs from the database

```
madmin/job/manager/delete/mysql = 
 DELETE FROM "madmin_job"
 WHERE :cond
 AND "siteid" = ?
```

* Default: 
 DELETE FROM "madmin_job"
 WHERE :cond
 AND "siteid" = ?


See also:

* madmin/job/manager/delete/ansi

# insert
## ansi

Inserts a new job record into the database table

```
madmin/job/manager/insert/ansi = 
 INSERT INTO "madmin_job" ( :names
 	"label", "path", "status", "editor", "mtime", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )
```

* Default: madmin/job/manager/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the job item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* madmin/job/manager/update/ansi
* madmin/job/manager/newid/ansi
* madmin/job/manager/delete/ansi
* madmin/job/manager/search/ansi
* madmin/job/manager/count/ansi

## mysql

Inserts a new job record into the database table

```
madmin/job/manager/insert/mysql = 
 INSERT INTO "madmin_job" ( :names
 	"label", "path", "status", "editor", "mtime", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "madmin_job" ( :names
 	"label", "path", "status", "editor", "mtime", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )


See also:

* madmin/job/manager/insert/ansi

# name

Class name of the used job manager implementation

```
madmin/job/manager/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default manager can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Job\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Job\Manager\Mymanager
```

then you have to set the this configuration option:

```
 madmin/job/manager/name = Mymanager
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyManager"!


# newid
## ansi

Retrieves the ID generated by the database when inserting a new record

```
madmin/job/manager/newid/ansi = madmin/job/manager/newid
```

* Default: madmin/job/manager/newid
* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2014.03

As soon as a new record is inserted into the database table,
the database server generates a new and unique identifier for
that record. This ID can be used for retrieving, updating and
deleting that specific record from the table again.

For MySQL:
```
 SELECT LAST_INSERT_ID()
For PostgreSQL:
 SELECT currval('seq_majob_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_majob_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* madmin/job/manager/insert/ansi
* madmin/job/manager/update/ansi
* madmin/job/manager/delete/ansi
* madmin/job/manager/search/ansi
* madmin/job/manager/count/ansi

## mysql

Retrieves the ID generated by the database when inserting a new record

```
madmin/job/manager/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: madmin/job/manager/newid

See also:

* madmin/job/manager/newid/ansi

# search
## ansi

Retrieves the records matched by the given criteria in the database

```
madmin/job/manager/search/ansi = 
 SELECT :columns
 	majob."id" AS "job.id", majob."siteid" AS "job.siteid",
 	majob."label" AS "job.label", majob."path" AS "job.path",
 	majob."status" AS "job.status", majob."editor" AS "job.editor",
 	majob."mtime" AS "job.mtime", majob."ctime" AS "job.ctime"
 FROM "madmin_job" majob
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: madmin/job/manager/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the job
database. The records must be from one of the sites that are
configured via the context item. If the current site is part of
a tree of sites, the SELECT statement can retrieve all records
from the current site and the complete sub-tree of sites.

As the records can normally be limited by criteria from sub-managers,
their tables must be joined in the SQL context. This is done by
using the "internaldeps" property from the definition of the ID
column of the sub-managers. These internal dependencies specify
the JOIN between the tables and the used columns for joining. The
":joins" placeholder is then replaced by the JOIN strings from
the sub-managers.

To limit the records matched, conditions can be added to the given
criteria object. It can contain comparisons like column names that
must match specific values which can be combined by AND, OR or NOT
operators. The resulting string of SQL conditions replaces the
":cond" placeholder before the statement is sent to the database
server.

If the records that are retrieved should be ordered by one or more
columns, the generated string of column / sort direction pairs
replaces the ":order" placeholder. In case no ordering is required,
the complete ORDER BY part including the "/*-orderby*/.../*orderby-*/"
markers is removed to speed up retrieving the records. Columns of
sub-managers can also be used for ordering the result set but then
no index can be used.

The number of returned records can be limited and can start at any
number between the begining and the end of the result set. For that
the ":size" and ":start" placeholders are replaced by the
corresponding values from the criteria object. The default values
are 0 for the start and 100 for the size value.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* madmin/job/manager/insert/ansi
* madmin/job/manager/update/ansi
* madmin/job/manager/newid/ansi
* madmin/job/manager/delete/ansi
* madmin/job/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
madmin/job/manager/search/mysql = 
 SELECT :columns
 	majob."id" AS "job.id", majob."siteid" AS "job.siteid",
 	majob."label" AS "job.label", majob."path" AS "job.path",
 	majob."status" AS "job.status", majob."editor" AS "job.editor",
 	majob."mtime" AS "job.mtime", majob."ctime" AS "job.ctime"
 FROM "madmin_job" majob
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	majob."id" AS "job.id", majob."siteid" AS "job.siteid",
 	majob."label" AS "job.label", majob."path" AS "job.path",
 	majob."status" AS "job.status", majob."editor" AS "job.editor",
 	majob."mtime" AS "job.mtime", majob."ctime" AS "job.ctime"
 FROM "madmin_job" majob
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* madmin/job/manager/search/ansi

# submanagers

List of manager names that can be instantiated by the job manager

```
madmin/job/manager/submanagers = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-manager names
* Since: 2014.03

Managers provide a generic interface to the underlying storage.
Each manager has or can have sub-managers caring about particular
aspects. Each of these sub-managers can be instantiated by its
parent manager using the getSubManager() method.

The search keys from sub-managers can be normally used in the
manager as well. It allows you to search for items of the manager
using the search keys of the sub-managers to further limit the
retrieved list of items.


# update
## ansi

Updates an existing job record in the database

```
madmin/job/manager/update/ansi = 
 UPDATE "madmin_job"
 SET :names
 	"label" = ?, "path" = ?, "status" = ?, "editor" = ?, "mtime" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: madmin/job/manager/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the job item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* madmin/job/manager/insert/ansi
* madmin/job/manager/newid/ansi
* madmin/job/manager/delete/ansi
* madmin/job/manager/search/ansi
* madmin/job/manager/count/ansi

## mysql

Updates an existing job record in the database

```
madmin/job/manager/update/mysql = 
 UPDATE "madmin_job"
 SET :names
 	"label" = ?, "path" = ?, "status" = ?, "editor" = ?, "mtime" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "madmin_job"
 SET :names
 	"label" = ?, "path" = ?, "status" = ?, "editor" = ?, "mtime" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* madmin/job/manager/update/ansi