
# decorators
## excludes

Excludes decorators added by the "common" option from the log manager

```
madmin/log/manager/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"madmin/common/manager/decorators/default" before they are wrapped
around the log manager.

```
 madmin/log/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"madmin/common/manager/decorators/default" for the log manager.

See also:

* madmin/common/manager/decorators/default
* madmin/log/manager/decorators/global
* madmin/log/manager/decorators/local

## global

Adds a list of globally available decorators only to the log manager

```
madmin/log/manager/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the log manager.

```
 madmin/log/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the log controller.

See also:

* madmin/common/manager/decorators/default
* madmin/log/manager/decorators/excludes
* madmin/log/manager/decorators/local

## local

Adds a list of local decorators only to the log manager

```
madmin/log/manager/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the log manager.

```
 madmin/log/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator2" only to the log
controller.

See also:

* madmin/common/manager/decorators/default
* madmin/log/manager/decorators/excludes
* madmin/log/manager/decorators/global

# name

Class name of the used log manager implementation

```
madmin/log/manager/name = Standard
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
 \Aimeos\MShop\Log\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Log\Manager\Mymanager
```

then you have to set the this configuration option:

```
 madmin/log/manager/name = Mymanager
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyManager"!


# standard
## count/ansi

Counts the number of records matched by the given criteria in the database

```
madmin/log/manager/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM(
 	SELECT malog."id"
 	FROM "madmin_log" AS malog
 	:joins
 	WHERE :cond
 	ORDER BY "id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: madmin/log/manager/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the log
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

* madmin/log/manager/standard/insert/ansi
* madmin/log/manager/standard/update/ansi
* madmin/log/manager/standard/newid/ansi
* madmin/log/manager/standard/delete/ansi
* madmin/log/manager/standard/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
madmin/log/manager/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM(
 	SELECT malog."id"
 	FROM "madmin_log" AS malog
 	:joins
 	WHERE :cond
 	ORDER BY "id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM(
 	SELECT malog."id"
 	FROM "madmin_log" AS malog
 	:joins
 	WHERE :cond
 	ORDER BY "id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* madmin/log/manager/standard/count/ansi

## delete/ansi

Deletes the items matched by the given IDs from the database

```
madmin/log/manager/standard/delete/ansi = 
 DELETE FROM "madmin_log"
 WHERE :cond AND "siteid" = ?
```

* Default: madmin/log/manager/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the log database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* madmin/log/manager/standard/insert/ansi
* madmin/log/manager/standard/update/ansi
* madmin/log/manager/standard/newid/ansi
* madmin/log/manager/standard/search/ansi
* madmin/log/manager/standard/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
madmin/log/manager/standard/delete/mysql = 
 DELETE FROM "madmin_log"
 WHERE :cond AND "siteid" = ?
```

* Default: 
 DELETE FROM "madmin_log"
 WHERE :cond AND "siteid" = ?


See also:

* madmin/log/manager/standard/delete/ansi

## insert/ansi

Inserts a new log record into the database table

```
madmin/log/manager/standard/insert/ansi = 
 INSERT INTO "madmin_log" ( :names
 	"facility", "timestamp", "priority", "message", "request", "siteid"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?
 )
```

* Default: madmin/log/manager/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the log item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* madmin/log/manager/standard/update/ansi
* madmin/log/manager/standard/newid/ansi
* madmin/log/manager/standard/delete/ansi
* madmin/log/manager/standard/search/ansi
* madmin/log/manager/standard/count/ansi

## insert/mysql

Inserts a new log record into the database table

```
madmin/log/manager/standard/insert/mysql = 
 INSERT INTO "madmin_log" ( :names
 	"facility", "timestamp", "priority", "message", "request", "siteid"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "madmin_log" ( :names
 	"facility", "timestamp", "priority", "message", "request", "siteid"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?
 )


See also:

* madmin/log/manager/standard/insert/ansi

## loglevel

Sets the severity level for messages to be written to the log

```
madmin/log/manager/standard/loglevel = 5
```

* Default: 5
* Type: int - Log level number
* Since: 2014.03

Manager, provider and other active components write messages about
problems, informational and debug output to the logs. The messages
that are actually written to the logs can be limited with the
"loglevel" configuration.

Available log levels are:
* Emergency (0): system is unusable
* Alert (1): action must be taken immediately
* Critical (2): critical conditions
* Error (3): error conditions
* Warning (4): warning conditions
* Notice (5): normal but significant condition
* Informational (6): informational messages
* Debug (7): debug messages

The "loglevel" configuration option defines the severity of messages
that will be written to the logs, e.g. a log level of "3" (error)
will allow all messages with an associated level of three and below
(error, critical, alert and emergency) to be written to the storage.
Messages with other log levels (warning, notice, informational and
debug) would be discarded and won't be written to the storage.

The higher the log level, the more messages will be written to the
storage. Keep in mind that a higher volume of messages will slow
down the system and the debug log level shouldn't be used in
production environments with a high number of visitors!


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
madmin/log/manager/standard/newid/ansi = madmin/log/manager/standard/newid
```

* Default: madmin/log/manager/standard/newid
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
 SELECT currval('seq_malog_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_malog_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* madmin/log/manager/standard/insert/ansi
* madmin/log/manager/standard/update/ansi
* madmin/log/manager/standard/delete/ansi
* madmin/log/manager/standard/search/ansi
* madmin/log/manager/standard/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
madmin/log/manager/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: madmin/log/manager/standard/newid

See also:

* madmin/log/manager/standard/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
madmin/log/manager/standard/search/ansi = 
 SELECT :columns
 	malog."id" AS "log.id", malog."siteid" AS "log.siteid",
 	malog."facility" AS "log.facility", malog."timestamp" AS "log.timestamp",
 	malog."priority" AS "log.priority", malog."message" AS "log.message",
 	malog."request" AS "log.request"
 FROM "madmin_log" AS malog
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: madmin/log/manager/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the log
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

* madmin/log/manager/standard/insert/ansi
* madmin/log/manager/standard/update/ansi
* madmin/log/manager/standard/newid/ansi
* madmin/log/manager/standard/delete/ansi
* madmin/log/manager/standard/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
madmin/log/manager/standard/search/mysql = 
 SELECT :columns
 	malog."id" AS "log.id", malog."siteid" AS "log.siteid",
 	malog."facility" AS "log.facility", malog."timestamp" AS "log.timestamp",
 	malog."priority" AS "log.priority", malog."message" AS "log.message",
 	malog."request" AS "log.request"
 FROM "madmin_log" AS malog
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	malog."id" AS "log.id", malog."siteid" AS "log.siteid",
 	malog."facility" AS "log.facility", malog."timestamp" AS "log.timestamp",
 	malog."priority" AS "log.priority", malog."message" AS "log.message",
 	malog."request" AS "log.request"
 FROM "madmin_log" AS malog
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* madmin/log/manager/standard/search/ansi

## update/ansi

Updates an existing log record in the database

```
madmin/log/manager/standard/update/ansi = 
 UPDATE "madmin_log"
 SET :names
 	"facility" = ?, "timestamp" = ?, "priority" = ?, "message" = ?, "request" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: madmin/log/manager/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the log item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* madmin/log/manager/standard/insert/ansi
* madmin/log/manager/standard/newid/ansi
* madmin/log/manager/standard/delete/ansi
* madmin/log/manager/standard/search/ansi
* madmin/log/manager/standard/count/ansi

## update/mysql

Updates an existing log record in the database

```
madmin/log/manager/standard/update/mysql = 
 UPDATE "madmin_log"
 SET :names
 	"facility" = ?, "timestamp" = ?, "priority" = ?, "message" = ?, "request" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "madmin_log"
 SET :names
 	"facility" = ?, "timestamp" = ?, "priority" = ?, "message" = ?, "request" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* madmin/log/manager/standard/update/ansi

# submanagers

List of manager names that can be instantiated by the log manager

```
madmin/log/manager/submanagers = Array
(
)
```

* Default: Array
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
