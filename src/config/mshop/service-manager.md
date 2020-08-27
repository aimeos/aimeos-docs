
# decorators
## excludes

Excludes decorators added by the "common" option from the service manager

```
mshop/service/manager/decorators/excludes = Array
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
"mshop/common/manager/decorators/default" before they are wrapped
around the service manager.

```
 mshop/service/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the service manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/decorators/global
* mshop/service/manager/decorators/local

## global

Adds a list of globally available decorators only to the service manager

```
mshop/service/manager/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the service manager.

```
 mshop/service/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the service
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/decorators/excludes
* mshop/service/manager/decorators/local

## local

Adds a list of local decorators only to the service manager

```
mshop/service/manager/decorators/local = Array
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
("\Aimeos\MShop\Service\Manager\Decorator\*") around the service manager.

```
 mshop/service/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Service\Manager\Decorator\Decorator2" only to the service
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/decorators/excludes
* mshop/service/manager/decorators/global

# lists
## decorators/excludes

Excludes decorators added by the "common" option from the service list manager

```
mshop/service/manager/lists/decorators/excludes = Array
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
"mshop/common/manager/decorators/default" before they are wrapped
around the service list manager.

```
 mshop/service/manager/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the service list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/lists/decorators/global
* mshop/service/manager/lists/decorators/local

## decorators/global

Adds a list of globally available decorators only to the service list manager

```
mshop/service/manager/lists/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the service list
manager.

```
 mshop/service/manager/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the service
list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/lists/decorators/excludes
* mshop/service/manager/lists/decorators/local

## decorators/local

Adds a list of local decorators only to the service list manager

```
mshop/service/manager/lists/decorators/local = Array
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
("\Aimeos\MShop\Service\Manager\Lists\Decorator\*") around the service
list manager.

```
 mshop/service/manager/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Service\Manager\Lists\Decorator\Decorator2" only to the
service list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/lists/decorators/excludes
* mshop/service/manager/lists/decorators/global

## name

Class name of the used service list manager implementation

```
mshop/service/manager/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default service list manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Service\Manager\Lists\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Service\Manager\Lists\Mylist
```

then you have to set the this configuration option:

```
 mshop/service/manager/lists/name = Mylist
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyList"!


## standard/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/service/manager/lists/standard/aggregate/ansi = 
 SELECT "key", COUNT("id") AS "count"
 FROM (
 	SELECT :key AS "key", mserli."id" AS "id"
 	FROM "mshop_service_list" AS mserli
 	:joins
 	WHERE :cond
 	GROUP BY :key, mserli."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY "key"
```

* Default: mshop/service/manager/lists/standard/aggregate
* Type: string - SQL statement for aggregating order items
* Since: 2014.07

Groups all records by the values in the key column and counts their
occurence. The matched records can be limited by the given criteria
from the order database. The records must be from one of the sites
that are configured via the context item. If the current site is part
of a tree of sites, the statement can count all records from the
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

This statement doesn't return any records. Instead, it returns pairs
of the different values found in the key column together with the
number of records that have been found for that key values.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/standard/insert/ansi
* mshop/service/manager/lists/standard/update/ansi
* mshop/service/manager/lists/standard/newid/ansi
* mshop/service/manager/lists/standard/delete/ansi
* mshop/service/manager/lists/standard/search/ansi
* mshop/service/manager/lists/standard/count/ansi

## standard/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/service/manager/lists/standard/aggregate/mysql = 
 SELECT "key", COUNT("id") AS "count"
 FROM (
 	SELECT :key AS "key", mserli."id" AS "id"
 	FROM "mshop_service_list" AS mserli
 	:joins
 	WHERE :cond
 	GROUP BY :key, mserli."id"
 	ORDER BY :order
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY "key"
```

* Default: 
 SELECT "key", COUNT("id") AS "count"
 FROM (
 	SELECT :key AS "key", mserli."id" AS "id"
 	FROM "mshop_service_list" AS mserli
 	:joins
 	WHERE :cond
 	GROUP BY :key, mserli."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY "key"


See also:

* mshop/service/manager/lists/standard/aggregate/ansi

## standard/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/lists/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mserli."id"
 	FROM "mshop_service_list" AS mserli
 	:joins
 	WHERE :cond
 	ORDER BY mserli."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/service/manager/lists/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the service
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

* mshop/service/manager/lists/standard/insert/ansi
* mshop/service/manager/lists/standard/update/ansi
* mshop/service/manager/lists/standard/newid/ansi
* mshop/service/manager/lists/standard/delete/ansi
* mshop/service/manager/lists/standard/search/ansi
* mshop/service/manager/lists/standard/aggregate/ansi

## standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/lists/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mserli."id"
 	FROM "mshop_service_list" AS mserli
 	:joins
 	WHERE :cond
 	ORDER BY mserli."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mserli."id"
 	FROM "mshop_service_list" AS mserli
 	:joins
 	WHERE :cond
 	ORDER BY mserli."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/service/manager/lists/standard/count/ansi

## standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/lists/standard/delete/ansi = 
 DELETE FROM "mshop_service_list"
 WHERE :cond AND siteid = ?
```

* Default: mshop/service/manager/lists/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the service database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/standard/insert/ansi
* mshop/service/manager/lists/standard/update/ansi
* mshop/service/manager/lists/standard/newid/ansi
* mshop/service/manager/lists/standard/search/ansi
* mshop/service/manager/lists/standard/count/ansi
* mshop/service/manager/lists/standard/aggregate/ansi

## standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/lists/standard/delete/mysql = 
 DELETE FROM "mshop_service_list"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_service_list"
 WHERE :cond AND siteid = ?


See also:

* mshop/service/manager/lists/standard/delete/ansi

## standard/insert/ansi

Inserts a new service list record into the database table

```
mshop/service/manager/lists/standard/insert/ansi = 
 INSERT INTO "mshop_service_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/service/manager/lists/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service list item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/standard/update/ansi
* mshop/service/manager/lists/standard/newid/ansi
* mshop/service/manager/lists/standard/delete/ansi
* mshop/service/manager/lists/standard/search/ansi
* mshop/service/manager/lists/standard/count/ansi
* mshop/service/manager/lists/standard/aggregate/ansi

## standard/insert/mysql

Inserts a new service list record into the database table

```
mshop/service/manager/lists/standard/insert/mysql = 
 INSERT INTO "mshop_service_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_service_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/service/manager/lists/standard/insert/ansi

## standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/service/manager/lists/standard/newid/ansi = mshop/service/manager/lists/standard/newid
```

* Default: mshop/service/manager/lists/standard/newid
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
 SELECT currval('seq_mserli_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mserli_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/service/manager/lists/standard/insert/ansi
* mshop/service/manager/lists/standard/update/ansi
* mshop/service/manager/lists/standard/delete/ansi
* mshop/service/manager/lists/standard/search/ansi
* mshop/service/manager/lists/standard/count/ansi
* mshop/service/manager/lists/standard/aggregate/ansi

## standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/service/manager/lists/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/service/manager/lists/standard/newid

See also:

* mshop/service/manager/lists/standard/newid/ansi

## standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/lists/standard/search/ansi = 
 SELECT :columns
 	mserli."id" AS "service.lists.id", mserli."parentid" AS "service.lists.parentid",
 	mserli."siteid" AS "service.lists.siteid", mserli."type" AS "service.lists.type",
 	mserli."domain" AS "service.lists.domain", mserli."refid" AS "service.lists.refid",
 	mserli."start" AS "service.lists.datestart", mserli."end" AS "service.lists.dateend",
 	mserli."config" AS "service.lists.config", mserli."pos" AS "service.lists.position",
 	mserli."status" AS "service.lists.status", mserli."mtime" AS "service.lists.mtime",
 	mserli."editor" AS "service.lists.editor", mserli."ctime" AS "service.lists.ctime"
 FROM "mshop_service_list" AS mserli
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/service/manager/lists/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the service
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

* mshop/service/manager/lists/standard/insert/ansi
* mshop/service/manager/lists/standard/update/ansi
* mshop/service/manager/lists/standard/newid/ansi
* mshop/service/manager/lists/standard/delete/ansi
* mshop/service/manager/lists/standard/count/ansi
* mshop/service/manager/lists/standard/aggregate/ansi

## standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/lists/standard/search/mysql = 
 SELECT :columns
 	mserli."id" AS "service.lists.id", mserli."parentid" AS "service.lists.parentid",
 	mserli."siteid" AS "service.lists.siteid", mserli."type" AS "service.lists.type",
 	mserli."domain" AS "service.lists.domain", mserli."refid" AS "service.lists.refid",
 	mserli."start" AS "service.lists.datestart", mserli."end" AS "service.lists.dateend",
 	mserli."config" AS "service.lists.config", mserli."pos" AS "service.lists.position",
 	mserli."status" AS "service.lists.status", mserli."mtime" AS "service.lists.mtime",
 	mserli."editor" AS "service.lists.editor", mserli."ctime" AS "service.lists.ctime"
 FROM "mshop_service_list" AS mserli
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mserli."id" AS "service.lists.id", mserli."parentid" AS "service.lists.parentid",
 	mserli."siteid" AS "service.lists.siteid", mserli."type" AS "service.lists.type",
 	mserli."domain" AS "service.lists.domain", mserli."refid" AS "service.lists.refid",
 	mserli."start" AS "service.lists.datestart", mserli."end" AS "service.lists.dateend",
 	mserli."config" AS "service.lists.config", mserli."pos" AS "service.lists.position",
 	mserli."status" AS "service.lists.status", mserli."mtime" AS "service.lists.mtime",
 	mserli."editor" AS "service.lists.editor", mserli."ctime" AS "service.lists.ctime"
 FROM "mshop_service_list" AS mserli
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/service/manager/lists/standard/search/ansi

## standard/update/ansi

Updates an existing service list record in the database

```
mshop/service/manager/lists/standard/update/ansi = 
 UPDATE "mshop_service_list"
 SET :names
 	"parentid"=?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/service/manager/lists/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service list item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/standard/insert/ansi
* mshop/service/manager/lists/standard/newid/ansi
* mshop/service/manager/lists/standard/delete/ansi
* mshop/service/manager/lists/standard/search/ansi
* mshop/service/manager/lists/standard/count/ansi
* mshop/service/manager/lists/standard/aggregate/ansi

## standard/update/mysql

Updates an existing service list record in the database

```
mshop/service/manager/lists/standard/update/mysql = 
 UPDATE "mshop_service_list"
 SET :names
 	"parentid"=?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_service_list"
 SET :names
 	"parentid"=?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/service/manager/lists/standard/update/ansi

## submanagers

List of manager names that can be instantiated by the service list manager

```
mshop/service/manager/lists/submanagers = Array
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


## type/decorators/excludes

Excludes decorators added by the "common" option from the service list type manager

```
mshop/service/manager/lists/type/decorators/excludes = Array
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
"mshop/common/manager/decorators/default" before they are wrapped
around the service list type manager.

```
 mshop/service/manager/lists/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the service list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/lists/type/decorators/global
* mshop/service/manager/lists/type/decorators/local

## type/decorators/global

Adds a list of globally available decorators only to the service list type manager

```
mshop/service/manager/lists/type/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the service list
type manager.

```
 mshop/service/manager/lists/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the service
list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/lists/type/decorators/excludes
* mshop/service/manager/lists/type/decorators/local

## type/decorators/local

Adds a list of local decorators only to the service list type manager

```
mshop/service/manager/lists/type/decorators/local = Array
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
("\Aimeos\MShop\Service\Manager\Lists\Type\Decorator\*") around the
service list type manager.

```
 mshop/service/manager/lists/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Service\Manager\Lists\Type\Decorator\Decorator2" only
to the service list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/lists/type/decorators/excludes
* mshop/service/manager/lists/type/decorators/global

## type/name

Class name of the used service list type manager implementation

```
mshop/service/manager/lists/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default service list type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Service\Manager\Lists\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Service\Manager\Lists\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/service/manager/lists/type/name = Mytype
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyType"!


## type/standard/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/lists/type/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mserlity."id"
 	FROM "mshop_service_list_type" as mserlity
 	:joins
 	WHERE :cond
 	ORDER BY mserlity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/service/manager/lists/type/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the service
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

* mshop/service/manager/lists/type/standard/insert/ansi
* mshop/service/manager/lists/type/standard/update/ansi
* mshop/service/manager/lists/type/standard/newid/ansi
* mshop/service/manager/lists/type/standard/delete/ansi
* mshop/service/manager/lists/type/standard/search/ansi

## type/standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/lists/type/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mserlity."id"
 	FROM "mshop_service_list_type" as mserlity
 	:joins
 	WHERE :cond
 	ORDER BY mserlity."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mserlity."id"
 	FROM "mshop_service_list_type" as mserlity
 	:joins
 	WHERE :cond
 	ORDER BY mserlity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/service/manager/lists/type/standard/count/ansi

## type/standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/lists/type/standard/delete/ansi = 
 DELETE FROM "mshop_service_list_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/service/manager/lists/type/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the service database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/type/standard/insert/ansi
* mshop/service/manager/lists/type/standard/update/ansi
* mshop/service/manager/lists/type/standard/newid/ansi
* mshop/service/manager/lists/type/standard/search/ansi
* mshop/service/manager/lists/type/standard/count/ansi

## type/standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/lists/type/standard/delete/mysql = 
 DELETE FROM "mshop_service_list_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_service_list_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/service/manager/lists/type/standard/delete/ansi

## type/standard/insert/ansi

Inserts a new service list type record into the database table

```
mshop/service/manager/lists/type/standard/insert/ansi = 
 INSERT INTO "mshop_service_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/service/manager/lists/type/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service list type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/type/standard/update/ansi
* mshop/service/manager/lists/type/standard/newid/ansi
* mshop/service/manager/lists/type/standard/delete/ansi
* mshop/service/manager/lists/type/standard/search/ansi
* mshop/service/manager/lists/type/standard/count/ansi

## type/standard/insert/mysql

Inserts a new service list type record into the database table

```
mshop/service/manager/lists/type/standard/insert/mysql = 
 INSERT INTO "mshop_service_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_service_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/service/manager/lists/type/standard/insert/ansi

## type/standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/service/manager/lists/type/standard/newid/ansi = mshop/service/manager/lists/type/standard/newid
```

* Default: mshop/service/manager/lists/type/standard/newid
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
 SELECT currval('seq_mserlity_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mserlity_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/service/manager/lists/type/standard/insert/ansi
* mshop/service/manager/lists/type/standard/update/ansi
* mshop/service/manager/lists/type/standard/delete/ansi
* mshop/service/manager/lists/type/standard/search/ansi
* mshop/service/manager/lists/type/standard/count/ansi

## type/standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/service/manager/lists/type/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/service/manager/lists/type/standard/newid

See also:

* mshop/service/manager/lists/type/standard/newid/ansi

## type/standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/lists/type/standard/search/ansi = 
 SELECT :columns
 	mserlity."id" AS "service.lists.type.id", mserlity."siteid" AS "service.lists.type.siteid",
 	mserlity."code" AS "service.lists.type.code", mserlity."domain" AS "service.lists.type.domain",
 	mserlity."label" AS "service.lists.type.label", mserlity."status" AS "service.lists.type.status",
 	mserlity."mtime" AS "service.lists.type.mtime", mserlity."editor" AS "service.lists.type.editor",
 	mserlity."ctime" AS "service.lists.type.ctime", mserlity."pos" AS "service.lists.type.position"
 FROM "mshop_service_list_type" AS mserlity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/service/manager/lists/type/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the service
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

* mshop/service/manager/lists/type/standard/insert/ansi
* mshop/service/manager/lists/type/standard/update/ansi
* mshop/service/manager/lists/type/standard/newid/ansi
* mshop/service/manager/lists/type/standard/delete/ansi
* mshop/service/manager/lists/type/standard/count/ansi

## type/standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/lists/type/standard/search/mysql = 
 SELECT :columns
 	mserlity."id" AS "service.lists.type.id", mserlity."siteid" AS "service.lists.type.siteid",
 	mserlity."code" AS "service.lists.type.code", mserlity."domain" AS "service.lists.type.domain",
 	mserlity."label" AS "service.lists.type.label", mserlity."status" AS "service.lists.type.status",
 	mserlity."mtime" AS "service.lists.type.mtime", mserlity."editor" AS "service.lists.type.editor",
 	mserlity."ctime" AS "service.lists.type.ctime", mserlity."pos" AS "service.lists.type.position"
 FROM "mshop_service_list_type" AS mserlity
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mserlity."id" AS "service.lists.type.id", mserlity."siteid" AS "service.lists.type.siteid",
 	mserlity."code" AS "service.lists.type.code", mserlity."domain" AS "service.lists.type.domain",
 	mserlity."label" AS "service.lists.type.label", mserlity."status" AS "service.lists.type.status",
 	mserlity."mtime" AS "service.lists.type.mtime", mserlity."editor" AS "service.lists.type.editor",
 	mserlity."ctime" AS "service.lists.type.ctime", mserlity."pos" AS "service.lists.type.position"
 FROM "mshop_service_list_type" AS mserlity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/service/manager/lists/type/standard/search/ansi

## type/standard/update/ansi

Updates an existing service list type record in the database

```
mshop/service/manager/lists/type/standard/update/ansi = 
 UPDATE "mshop_service_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/service/manager/lists/type/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service list type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/lists/type/standard/insert/ansi
* mshop/service/manager/lists/type/standard/newid/ansi
* mshop/service/manager/lists/type/standard/delete/ansi
* mshop/service/manager/lists/type/standard/search/ansi
* mshop/service/manager/lists/type/standard/count/ansi

## type/standard/update/mysql

Updates an existing service list type record in the database

```
mshop/service/manager/lists/type/standard/update/mysql = 
 UPDATE "mshop_service_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_service_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/service/manager/lists/type/standard/update/ansi

## type/submanagers

List of manager names that can be instantiated by the service list type manager

```
mshop/service/manager/lists/type/submanagers = Array
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


# name

Class name of the used service manager implementation

```
mshop/service/manager/name = Standard
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
 \Aimeos\MShop\Service\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Service\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/service/manager/name = Mymanager
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyManager"!


# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/service/manager/sitemode = 3
```

* Default: 3
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole service domain if items from parent sites are inherited,
sites from child sites are aggregated or both.

Available constants for the site mode are:
* 0 = only items from the current site
* 1 = inherit items from parent sites
* 2 = aggregate items from child sites
* 3 = inherit and aggregate items at the same time

You also need to set the mode in the locale manager
(mshop/locale/manager/standard/sitelevel) to one of the constants.
If you set it to the same value, it will work as described but you
can also use different modes. For example, if inheritance and
aggregation is configured the locale manager but only inheritance
in the domain manager because aggregating items makes no sense in
this domain, then items wil be only inherited. Thus, you have full
control over inheritance and aggregation in each domain.

See also:

* mshop/locale/manager/standard/sitelevel

# standard
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/standard/count/ansi = 
 SELECT count(*) as "count"
 FROM (
 	SELECT mser."id"
 	FROM "mshop_service" AS mser
 	:joins
 	WHERE :cond
 	GROUP BY mser."id"
 	ORDER BY mser."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/service/manager/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the service
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

* mshop/service/manager/standard/insert/ansi
* mshop/service/manager/standard/update/ansi
* mshop/service/manager/standard/newid/ansi
* mshop/service/manager/standard/delete/ansi
* mshop/service/manager/standard/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/standard/count/mysql = 
 SELECT count(*) as "count"
 FROM (
 	SELECT mser."id"
 	FROM "mshop_service" AS mser
 	:joins
 	WHERE :cond
 	GROUP BY mser."id"
 	ORDER BY mser."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT count(*) as "count"
 FROM (
 	SELECT mser."id"
 	FROM "mshop_service" AS mser
 	:joins
 	WHERE :cond
 	GROUP BY mser."id"
 	ORDER BY mser."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/service/manager/standard/count/ansi

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/standard/delete/ansi = 
 DELETE FROM "mshop_service"
 WHERE :cond AND siteid = ?
```

* Default: mshop/service/manager/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the service database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/standard/insert/ansi
* mshop/service/manager/standard/update/ansi
* mshop/service/manager/standard/newid/ansi
* mshop/service/manager/standard/search/ansi
* mshop/service/manager/standard/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/standard/delete/mysql = 
 DELETE FROM "mshop_service"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_service"
 WHERE :cond AND siteid = ?


See also:

* mshop/service/manager/standard/delete/ansi

## insert/ansi

Inserts a new service record into the database table

```
mshop/service/manager/standard/insert/ansi = 
 INSERT INTO "mshop_service" ( :names
 	"pos", "type", "code", "label", "provider", "start", "end",
 	"config", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/service/manager/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/standard/update/ansi
* mshop/service/manager/standard/newid/ansi
* mshop/service/manager/standard/delete/ansi
* mshop/service/manager/standard/search/ansi
* mshop/service/manager/standard/count/ansi

## insert/mysql

Inserts a new service record into the database table

```
mshop/service/manager/standard/insert/mysql = 
 INSERT INTO "mshop_service" ( :names
 	"pos", "type", "code", "label", "provider", "start", "end",
 	"config", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_service" ( :names
 	"pos", "type", "code", "label", "provider", "start", "end",
 	"config", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/service/manager/standard/insert/ansi

## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/service/manager/standard/newid/ansi = mshop/service/manager/standard/newid
```

* Default: mshop/service/manager/standard/newid
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
 SELECT currval('seq_mser_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mser_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/service/manager/standard/insert/ansi
* mshop/service/manager/standard/update/ansi
* mshop/service/manager/standard/delete/ansi
* mshop/service/manager/standard/search/ansi
* mshop/service/manager/standard/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/service/manager/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/service/manager/standard/newid

See also:

* mshop/service/manager/standard/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/standard/search/ansi = 
 SELECT :columns
 	mser."id" AS "service.id", mser."siteid" AS "service.siteid",
 	mser."pos" AS "service.position", mser."type" AS "service.type",
 	mser."code" AS "service.code", mser."label" AS "service.label",
 	mser."provider" AS "service.provider", mser."config" AS "service.config",
 	mser."start" AS "service.datestart", mser."end" AS "service.dateend",
 	mser."status" AS "service.status", mser."mtime" AS "service.mtime",
 	mser."editor" AS "service.editor",	mser."ctime" AS "service.ctime"
 FROM "mshop_service" AS mser
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mser."id", mser."siteid", mser."pos", mser."type", mser."code", mser."label",
 	mser."provider", mser."config", mser."start", mser."end", mser."status", mser."mtime",
 	mser."editor",	mser."ctime"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/service/manager/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the service
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

* mshop/service/manager/standard/insert/ansi
* mshop/service/manager/standard/update/ansi
* mshop/service/manager/standard/newid/ansi
* mshop/service/manager/standard/delete/ansi
* mshop/service/manager/standard/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/standard/search/mysql = 
 SELECT :columns
 	mser."id" AS "service.id", mser."siteid" AS "service.siteid",
 	mser."pos" AS "service.position", mser."type" AS "service.type",
 	mser."code" AS "service.code", mser."label" AS "service.label",
 	mser."provider" AS "service.provider", mser."config" AS "service.config",
 	mser."start" AS "service.datestart", mser."end" AS "service.dateend",
 	mser."status" AS "service.status", mser."mtime" AS "service.mtime",
 	mser."editor" AS "service.editor",	mser."ctime" AS "service.ctime"
 FROM "mshop_service" AS mser
 :joins
 WHERE :cond
 GROUP BY :group mser."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mser."id" AS "service.id", mser."siteid" AS "service.siteid",
 	mser."pos" AS "service.position", mser."type" AS "service.type",
 	mser."code" AS "service.code", mser."label" AS "service.label",
 	mser."provider" AS "service.provider", mser."config" AS "service.config",
 	mser."start" AS "service.datestart", mser."end" AS "service.dateend",
 	mser."status" AS "service.status", mser."mtime" AS "service.mtime",
 	mser."editor" AS "service.editor",	mser."ctime" AS "service.ctime"
 FROM "mshop_service" AS mser
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mser."id", mser."siteid", mser."pos", mser."type", mser."code", mser."label",
 	mser."provider", mser."config", mser."start", mser."end", mser."status", mser."mtime",
 	mser."editor",	mser."ctime"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/service/manager/standard/search/ansi

## update/ansi

Updates an existing service record in the database

```
mshop/service/manager/standard/update/ansi = 
 UPDATE "mshop_service"
 SET :names
 	"pos" = ?, "type" = ?, "code" = ?, "label" = ?, "provider" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/service/manager/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/standard/insert/ansi
* mshop/service/manager/standard/newid/ansi
* mshop/service/manager/standard/delete/ansi
* mshop/service/manager/standard/search/ansi
* mshop/service/manager/standard/count/ansi

## update/mysql

Updates an existing service record in the database

```
mshop/service/manager/standard/update/mysql = 
 UPDATE "mshop_service"
 SET :names
 	"pos" = ?, "type" = ?, "code" = ?, "label" = ?, "provider" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_service"
 SET :names
 	"pos" = ?, "type" = ?, "code" = ?, "label" = ?, "provider" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/service/manager/standard/update/ansi

# submanagers

List of manager names that can be instantiated by the service manager

```
mshop/service/manager/submanagers = Array
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


# type
## decorators/excludes

Excludes decorators added by the "common" option from the service type manager

```
mshop/service/manager/type/decorators/excludes = Array
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
"mshop/common/manager/decorators/default" before they are wrapped
around the service type manager.

```
 mshop/service/manager/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the service type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/type/decorators/global
* mshop/service/manager/type/decorators/local

## decorators/global

Adds a list of globally available decorators only to the service type manager

```
mshop/service/manager/type/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the service type
manager.

```
 mshop/service/manager/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the service
type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/type/decorators/excludes
* mshop/service/manager/type/decorators/local

## decorators/local

Adds a list of local decorators only to the service type manager

```
mshop/service/manager/type/decorators/local = Array
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
("\Aimeos\MShop\Service\Manager\Type\Decorator\*") around the service
type manager.

```
 mshop/service/manager/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Service\Manager\Type\Decorator\Decorator2" only to the
service type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/service/manager/type/decorators/excludes
* mshop/service/manager/type/decorators/global

## name

Class name of the used service type manager implementation

```
mshop/service/manager/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default service type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Service\Manager\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Service\Manager\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/service/manager/type/name = Mytype
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyType"!


## standard/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/type/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mserty."id"
 	FROM "mshop_service_type" AS mserty
 	:joins
 	WHERE :cond
 	ORDER BY mserty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/service/manager/type/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the service
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

* mshop/service/manager/type/standard/insert/ansi
* mshop/service/manager/type/standard/update/ansi
* mshop/service/manager/type/standard/newid/ansi
* mshop/service/manager/type/standard/delete/ansi
* mshop/service/manager/type/standard/search/ansi

## standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/service/manager/type/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mserty."id"
 	FROM "mshop_service_type" AS mserty
 	:joins
 	WHERE :cond
 	ORDER BY mserty."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mserty."id"
 	FROM "mshop_service_type" AS mserty
 	:joins
 	WHERE :cond
 	ORDER BY mserty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/service/manager/type/standard/count/ansi

## standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/type/standard/delete/ansi = 
 DELETE FROM "mshop_service_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/service/manager/type/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the service database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/type/standard/insert/ansi
* mshop/service/manager/type/standard/update/ansi
* mshop/service/manager/type/standard/newid/ansi
* mshop/service/manager/type/standard/search/ansi
* mshop/service/manager/type/standard/count/ansi

## standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/service/manager/type/standard/delete/mysql = 
 DELETE FROM "mshop_service_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_service_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/service/manager/type/standard/delete/ansi

## standard/insert/ansi

Inserts a new service type record into the database table

```
mshop/service/manager/type/standard/insert/ansi = 
 INSERT INTO "mshop_service_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/service/manager/type/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/type/standard/update/ansi
* mshop/service/manager/type/standard/newid/ansi
* mshop/service/manager/type/standard/delete/ansi
* mshop/service/manager/type/standard/search/ansi
* mshop/service/manager/type/standard/count/ansi

## standard/insert/mysql

Inserts a new service type record into the database table

```
mshop/service/manager/type/standard/insert/mysql = 
 INSERT INTO "mshop_service_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_service_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/service/manager/type/standard/insert/ansi

## standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/service/manager/type/standard/newid/ansi = mshop/service/manager/type/standard/newid
```

* Default: mshop/service/manager/type/standard/newid
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
 SELECT currval('seq_mserty_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mserty_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/service/manager/type/standard/insert/ansi
* mshop/service/manager/type/standard/update/ansi
* mshop/service/manager/type/standard/delete/ansi
* mshop/service/manager/type/standard/search/ansi
* mshop/service/manager/type/standard/count/ansi

## standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/service/manager/type/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/service/manager/type/standard/newid

See also:

* mshop/service/manager/type/standard/newid/ansi

## standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/type/standard/search/ansi = 
 SELECT :columns
 	mserty."id" AS "service.type.id", mserty."siteid" AS "service.type.siteid",
 	mserty."domain" AS "service.type.domain", mserty."code" AS "service.type.code",
 	mserty."label" AS "service.type.label", mserty."status" AS "service.type.status",
 	mserty."mtime" AS "service.type.mtime", mserty."editor" AS "service.type.editor",
 	mserty."ctime" AS "service.type.ctime", mserty."pos" AS "service.type.position"
 FROM "mshop_service_type" AS mserty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/service/manager/type/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the service
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

* mshop/service/manager/type/standard/insert/ansi
* mshop/service/manager/type/standard/update/ansi
* mshop/service/manager/type/standard/newid/ansi
* mshop/service/manager/type/standard/delete/ansi
* mshop/service/manager/type/standard/count/ansi

## standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/service/manager/type/standard/search/mysql = 
 SELECT :columns
 	mserty."id" AS "service.type.id", mserty."siteid" AS "service.type.siteid",
 	mserty."domain" AS "service.type.domain", mserty."code" AS "service.type.code",
 	mserty."label" AS "service.type.label", mserty."status" AS "service.type.status",
 	mserty."mtime" AS "service.type.mtime", mserty."editor" AS "service.type.editor",
 	mserty."ctime" AS "service.type.ctime", mserty."pos" AS "service.type.position"
 FROM "mshop_service_type" AS mserty
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mserty."id" AS "service.type.id", mserty."siteid" AS "service.type.siteid",
 	mserty."domain" AS "service.type.domain", mserty."code" AS "service.type.code",
 	mserty."label" AS "service.type.label", mserty."status" AS "service.type.status",
 	mserty."mtime" AS "service.type.mtime", mserty."editor" AS "service.type.editor",
 	mserty."ctime" AS "service.type.ctime", mserty."pos" AS "service.type.position"
 FROM "mshop_service_type" AS mserty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/service/manager/type/standard/search/ansi

## standard/update/ansi

Updates an existing service type record in the database

```
mshop/service/manager/type/standard/update/ansi = 
 UPDATE "mshop_service_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/service/manager/type/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the service type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/service/manager/type/standard/insert/ansi
* mshop/service/manager/type/standard/newid/ansi
* mshop/service/manager/type/standard/delete/ansi
* mshop/service/manager/type/standard/search/ansi
* mshop/service/manager/type/standard/count/ansi

## standard/update/mysql

Updates an existing service type record in the database

```
mshop/service/manager/type/standard/update/mysql = 
 UPDATE "mshop_service_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_service_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/service/manager/type/standard/update/ansi

## submanagers

List of manager names that can be instantiated by the service type manager

```
mshop/service/manager/type/submanagers = Array
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
