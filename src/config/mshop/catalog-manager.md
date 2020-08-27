
# decorators
## excludes

Excludes decorators added by the "common" option from the catalog manager

```
mshop/catalog/manager/decorators/excludes = Array
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
around the catalog manager.

```
 mshop/catalog/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the catalog manager.

See also:

* mshop/common/manager/decorators/default
* mshop/catalog/manager/decorators/global
* mshop/catalog/manager/decorators/local

## global

Adds a list of globally available decorators only to the catalog manager

```
mshop/catalog/manager/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the catalog manager.

```
 mshop/catalog/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the catalog
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/catalog/manager/decorators/excludes
* mshop/catalog/manager/decorators/local

## local

Adds a list of local decorators only to the catalog manager

```
mshop/catalog/manager/decorators/local = Array
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
("\Aimeos\MShop\Catalog\Manager\Decorator\*") around the catalog manager.

```
 mshop/catalog/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Catalog\Manager\Decorator\Decorator2" only to the catalog
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/catalog/manager/decorators/excludes
* mshop/catalog/manager/decorators/global

# lists
## decorators/excludes

Excludes decorators added by the "common" option from the catalog list manager

```
mshop/catalog/manager/lists/decorators/excludes = Array
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
around the catalog list manager.

```
 mshop/catalog/manager/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the catalog list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/catalog/manager/lists/decorators/global
* mshop/catalog/manager/lists/decorators/local

## decorators/global

Adds a list of globally available decorators only to the catalog list manager

```
mshop/catalog/manager/lists/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the catalog list manager.

```
 mshop/catalog/manager/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the catalog
list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/catalog/manager/lists/decorators/excludes
* mshop/catalog/manager/lists/decorators/local

## decorators/local

Adds a list of local decorators only to the catalog list manager

```
mshop/catalog/manager/lists/decorators/local = Array
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
("\Aimeos\MShop\Catalog\Manager\Lists\Decorator\*") around the catalog
list manager.

```
 mshop/catalog/manager/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Catalog\Manager\Lists\Decorator\Decorator2" only to the
catalog list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/catalog/manager/lists/decorators/excludes
* mshop/catalog/manager/lists/decorators/global

## name

Class name of the used catalog list manager implementation

```
mshop/catalog/manager/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default catalog list manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Catalog\Manager\Lists\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Catalog\Manager\Lists\Mylist
```

then you have to set the this configuration option:

```
 mshop/catalog/manager/lists/name = Mylist
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
mshop/catalog/manager/lists/standard/aggregate/ansi = 
 SELECT "key", COUNT("id") AS "count"
 FROM (
 	SELECT :key AS "key", mcatli."id" AS "id"
 	FROM "mshop_catalog_list" AS mcatli
 	:joins
 	WHERE :cond
 	GROUP BY :key, mcatli."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY "key"
```

* Default: mshop/catalog/manager/lists/standard/aggregate
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

* mshop/catalog/manager/lists/standard/insert/ansi
* mshop/catalog/manager/lists/standard/update/ansi
* mshop/catalog/manager/lists/standard/newid/ansi
* mshop/catalog/manager/lists/standard/delete/ansi
* mshop/catalog/manager/lists/standard/search/ansi
* mshop/catalog/manager/lists/standard/count/ansi

## standard/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/catalog/manager/lists/standard/aggregate/mysql = 
 SELECT "key", COUNT("id") AS "count"
 FROM (
 	SELECT :key AS "key", mcatli."id" AS "id"
 	FROM "mshop_catalog_list" AS mcatli
 	:joins
 	WHERE :cond
 	GROUP BY :key, mcatli."id"
 	ORDER BY :order
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY "key"
```

* Default: 
 SELECT "key", COUNT("id") AS "count"
 FROM (
 	SELECT :key AS "key", mcatli."id" AS "id"
 	FROM "mshop_catalog_list" AS mcatli
 	:joins
 	WHERE :cond
 	GROUP BY :key, mcatli."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY "key"


See also:

* mshop/catalog/manager/lists/standard/aggregate/ansi

## standard/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/catalog/manager/lists/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcatli."id"
 	FROM "mshop_catalog_list" AS mcatli
 	:joins
 	WHERE :cond
 	ORDER BY mcatli."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/catalog/manager/lists/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the catalog
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

* mshop/catalog/manager/lists/standard/insert/ansi
* mshop/catalog/manager/lists/standard/update/ansi
* mshop/catalog/manager/lists/standard/newid/ansi
* mshop/catalog/manager/lists/standard/delete/ansi
* mshop/catalog/manager/lists/standard/search/ansi
* mshop/catalog/manager/lists/standard/aggregate/ansi

## standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/catalog/manager/lists/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcatli."id"
 	FROM "mshop_catalog_list" AS mcatli
 	:joins
 	WHERE :cond
 	ORDER BY mcatli."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcatli."id"
 	FROM "mshop_catalog_list" AS mcatli
 	:joins
 	WHERE :cond
 	ORDER BY mcatli."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/catalog/manager/lists/standard/count/ansi

## standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/catalog/manager/lists/standard/delete/ansi = 
 DELETE FROM "mshop_catalog_list"
 WHERE :cond AND siteid = ?
```

* Default: mshop/catalog/manager/lists/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the catalog database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/lists/standard/insert/ansi
* mshop/catalog/manager/lists/standard/update/ansi
* mshop/catalog/manager/lists/standard/newid/ansi
* mshop/catalog/manager/lists/standard/search/ansi
* mshop/catalog/manager/lists/standard/count/ansi
* mshop/catalog/manager/lists/standard/aggregate/ansi

## standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/catalog/manager/lists/standard/delete/mysql = 
 DELETE FROM "mshop_catalog_list"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_catalog_list"
 WHERE :cond AND siteid = ?


See also:

* mshop/catalog/manager/lists/standard/delete/ansi

## standard/insert/ansi

Inserts a new catalog list record into the database table

```
mshop/catalog/manager/lists/standard/insert/ansi = 
 INSERT INTO "mshop_catalog_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/catalog/manager/lists/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the catalog list item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/lists/standard/update/ansi
* mshop/catalog/manager/lists/standard/newid/ansi
* mshop/catalog/manager/lists/standard/delete/ansi
* mshop/catalog/manager/lists/standard/search/ansi
* mshop/catalog/manager/lists/standard/count/ansi
* mshop/catalog/manager/lists/standard/aggregate/ansi

## standard/insert/mysql

Inserts a new catalog list record into the database table

```
mshop/catalog/manager/lists/standard/insert/mysql = 
 INSERT INTO "mshop_catalog_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_catalog_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/catalog/manager/lists/standard/insert/ansi

## standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/catalog/manager/lists/standard/newid/ansi = mshop/catalog/manager/lists/standard/newid
```

* Default: mshop/catalog/manager/lists/standard/newid
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
 SELECT currval('seq_mcatli_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mcatli_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/catalog/manager/lists/standard/insert/ansi
* mshop/catalog/manager/lists/standard/update/ansi
* mshop/catalog/manager/lists/standard/delete/ansi
* mshop/catalog/manager/lists/standard/search/ansi
* mshop/catalog/manager/lists/standard/count/ansi
* mshop/catalog/manager/lists/standard/aggregate/ansi

## standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/catalog/manager/lists/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/catalog/manager/lists/standard/newid

See also:

* mshop/catalog/manager/lists/standard/newid/ansi

## standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/catalog/manager/lists/standard/search/ansi = 
 SELECT :columns
 	mcatli."id" AS "catalog.lists.id", mcatli."parentid" AS "catalog.lists.parentid",
 	mcatli."siteid" AS "catalog.lists.siteid", mcatli."type" AS "catalog.lists.type",
 	mcatli."domain" AS "catalog.lists.domain", mcatli."refid" AS "catalog.lists.refid",
 	mcatli."start" AS "catalog.lists.datestart", mcatli."end" AS "catalog.lists.dateend",
 	mcatli."config" AS "catalog.lists.config", mcatli."pos" AS "catalog.lists.position",
 	mcatli."status" AS "catalog.lists.status", mcatli."mtime" AS "catalog.lists.mtime",
 	mcatli."editor" AS "catalog.lists.editor", mcatli."ctime" AS "catalog.lists.ctime"
 FROM "mshop_catalog_list" AS mcatli
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/catalog/manager/lists/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the catalog
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

* mshop/catalog/manager/lists/standard/insert/ansi
* mshop/catalog/manager/lists/standard/update/ansi
* mshop/catalog/manager/lists/standard/newid/ansi
* mshop/catalog/manager/lists/standard/delete/ansi
* mshop/catalog/manager/lists/standard/count/ansi
* mshop/catalog/manager/lists/standard/aggregate/ansi

## standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/catalog/manager/lists/standard/search/mysql = 
 SELECT :columns
 	mcatli."id" AS "catalog.lists.id", mcatli."parentid" AS "catalog.lists.parentid",
 	mcatli."siteid" AS "catalog.lists.siteid", mcatli."type" AS "catalog.lists.type",
 	mcatli."domain" AS "catalog.lists.domain", mcatli."refid" AS "catalog.lists.refid",
 	mcatli."start" AS "catalog.lists.datestart", mcatli."end" AS "catalog.lists.dateend",
 	mcatli."config" AS "catalog.lists.config", mcatli."pos" AS "catalog.lists.position",
 	mcatli."status" AS "catalog.lists.status", mcatli."mtime" AS "catalog.lists.mtime",
 	mcatli."editor" AS "catalog.lists.editor", mcatli."ctime" AS "catalog.lists.ctime"
 FROM "mshop_catalog_list" AS mcatli
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mcatli."id" AS "catalog.lists.id", mcatli."parentid" AS "catalog.lists.parentid",
 	mcatli."siteid" AS "catalog.lists.siteid", mcatli."type" AS "catalog.lists.type",
 	mcatli."domain" AS "catalog.lists.domain", mcatli."refid" AS "catalog.lists.refid",
 	mcatli."start" AS "catalog.lists.datestart", mcatli."end" AS "catalog.lists.dateend",
 	mcatli."config" AS "catalog.lists.config", mcatli."pos" AS "catalog.lists.position",
 	mcatli."status" AS "catalog.lists.status", mcatli."mtime" AS "catalog.lists.mtime",
 	mcatli."editor" AS "catalog.lists.editor", mcatli."ctime" AS "catalog.lists.ctime"
 FROM "mshop_catalog_list" AS mcatli
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/catalog/manager/lists/standard/search/ansi

## standard/update/ansi

Updates an existing catalog list record in the database

```
mshop/catalog/manager/lists/standard/update/ansi = 
 UPDATE "mshop_catalog_list"
 SET :names
 	 "parentid" = ?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	 "end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/catalog/manager/lists/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the catalog list item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/lists/standard/insert/ansi
* mshop/catalog/manager/lists/standard/newid/ansi
* mshop/catalog/manager/lists/standard/delete/ansi
* mshop/catalog/manager/lists/standard/search/ansi
* mshop/catalog/manager/lists/standard/count/ansi
* mshop/catalog/manager/lists/standard/aggregate/ansi

## standard/update/mysql

Updates an existing catalog list record in the database

```
mshop/catalog/manager/lists/standard/update/mysql = 
 UPDATE "mshop_catalog_list"
 SET :names
 	 "parentid" = ?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	 "end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_catalog_list"
 SET :names
 	 "parentid" = ?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	 "end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/catalog/manager/lists/standard/update/ansi

## submanagers

List of manager names that can be instantiated by the catalog list manager

```
mshop/catalog/manager/lists/submanagers = Array
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

Excludes decorators added by the "common" option from the catalog list type manager

```
mshop/catalog/manager/lists/type/decorators/excludes = Array
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
around the catalog list type manager.

```
 mshop/catalog/manager/lists/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the catalog list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/catalog/manager/lists/type/decorators/global
* mshop/catalog/manager/lists/type/decorators/local

## type/decorators/global

Adds a list of globally available decorators only to the catalog list type manager

```
mshop/catalog/manager/lists/type/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the catalog list type manager.

```
 mshop/catalog/manager/lists/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the catalog
list type manager..

See also:

* mshop/common/manager/decorators/default
* mshop/catalog/manager/lists/type/decorators/excludes
* mshop/catalog/manager/lists/type/decorators/local

## type/decorators/local

Adds a list of local decorators only to the catalog list type manager

```
mshop/catalog/manager/lists/type/decorators/local = Array
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
("\Aimeos\MShop\Catalog\Manager\Lists\Type\Decorator\*") around the catalog
list type manager.

```
 mshop/catalog/manager/lists/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Catalog\Manager\Lists\Type\Decorator\Decorator2" only to the
catalog list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/catalog/manager/lists/type/decorators/excludes
* mshop/catalog/manager/lists/type/decorators/global

## type/name

Class name of the used catalog list type manager implementation

```
mshop/catalog/manager/lists/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default catalog list type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Catalog\Manager\Lists\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Catalog\Manager\Lists\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/catalog/manager/lists/type/name = Mytype
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
mshop/catalog/manager/lists/type/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcatlity."id"
 	FROM "mshop_catalog_list_type" AS mcatlity
 	:joins
 	WHERE :cond
 	ORDER BY mcatlity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/catalog/manager/lists/type/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the catalog
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

* mshop/catalog/manager/lists/type/standard/insert/ansi
* mshop/catalog/manager/lists/type/standard/update/ansi
* mshop/catalog/manager/lists/type/standard/newid/ansi
* mshop/catalog/manager/lists/type/standard/delete/ansi
* mshop/catalog/manager/lists/type/standard/search/ansi

## type/standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/catalog/manager/lists/type/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcatlity."id"
 	FROM "mshop_catalog_list_type" AS mcatlity
 	:joins
 	WHERE :cond
 	ORDER BY mcatlity."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcatlity."id"
 	FROM "mshop_catalog_list_type" AS mcatlity
 	:joins
 	WHERE :cond
 	ORDER BY mcatlity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/catalog/manager/lists/type/standard/count/ansi

## type/standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/catalog/manager/lists/type/standard/delete/ansi = 
 DELETE FROM "mshop_catalog_list_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/catalog/manager/lists/type/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the catalog database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/lists/type/standard/insert/ansi
* mshop/catalog/manager/lists/type/standard/update/ansi
* mshop/catalog/manager/lists/type/standard/newid/ansi
* mshop/catalog/manager/lists/type/standard/search/ansi
* mshop/catalog/manager/lists/type/standard/count/ansi

## type/standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/catalog/manager/lists/type/standard/delete/mysql = 
 DELETE FROM "mshop_catalog_list_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_catalog_list_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/catalog/manager/lists/type/standard/delete/ansi

## type/standard/insert/ansi

Inserts a new catalog list type record into the database table

```
mshop/catalog/manager/lists/type/standard/insert/ansi = 
 INSERT INTO "mshop_catalog_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/catalog/manager/lists/type/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the catalog list type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/lists/type/standard/update/ansi
* mshop/catalog/manager/lists/type/standard/newid/ansi
* mshop/catalog/manager/lists/type/standard/delete/ansi
* mshop/catalog/manager/lists/type/standard/search/ansi
* mshop/catalog/manager/lists/type/standard/count/ansi

## type/standard/insert/mysql

Inserts a new catalog list type record into the database table

```
mshop/catalog/manager/lists/type/standard/insert/mysql = 
 INSERT INTO "mshop_catalog_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_catalog_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/catalog/manager/lists/type/standard/insert/ansi

## type/standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/catalog/manager/lists/type/standard/newid/ansi = mshop/catalog/manager/lists/type/standard/newid
```

* Default: mshop/catalog/manager/lists/type/standard/newid
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
 SELECT currval('seq_mcatlity_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mcatlity_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/catalog/manager/lists/type/standard/insert/ansi
* mshop/catalog/manager/lists/type/standard/update/ansi
* mshop/catalog/manager/lists/type/standard/delete/ansi
* mshop/catalog/manager/lists/type/standard/search/ansi
* mshop/catalog/manager/lists/type/standard/count/ansi

## type/standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/catalog/manager/lists/type/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/catalog/manager/lists/type/standard/newid

See also:

* mshop/catalog/manager/lists/type/standard/newid/ansi

## type/standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/catalog/manager/lists/type/standard/search/ansi = 
 SELECT :columns
 	mcatlity."id" AS "catalog.lists.type.id", mcatlity."siteid" AS "catalog.lists.type.siteid",
 	mcatlity."code" AS "catalog.lists.type.code", mcatlity."domain" AS "catalog.lists.type.domain",
 	mcatlity."label" AS "catalog.lists.type.label", mcatlity."mtime" AS "catalog.lists.type.mtime",
 	mcatlity."editor" AS "catalog.lists.type.editor", mcatlity."ctime" AS "catalog.lists.type.ctime",
 	mcatlity."status" AS "catalog.lists.type.status", mcatlity."pos" AS "catalog.lists.type.position"
 FROM "mshop_catalog_list_type" AS mcatlity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/catalog/manager/lists/type/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the catalog
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

* mshop/catalog/manager/lists/type/standard/insert/ansi
* mshop/catalog/manager/lists/type/standard/update/ansi
* mshop/catalog/manager/lists/type/standard/newid/ansi
* mshop/catalog/manager/lists/type/standard/delete/ansi
* mshop/catalog/manager/lists/type/standard/count/ansi

## type/standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/catalog/manager/lists/type/standard/search/mysql = 
 SELECT :columns
 	mcatlity."id" AS "catalog.lists.type.id", mcatlity."siteid" AS "catalog.lists.type.siteid",
 	mcatlity."code" AS "catalog.lists.type.code", mcatlity."domain" AS "catalog.lists.type.domain",
 	mcatlity."label" AS "catalog.lists.type.label", mcatlity."mtime" AS "catalog.lists.type.mtime",
 	mcatlity."editor" AS "catalog.lists.type.editor", mcatlity."ctime" AS "catalog.lists.type.ctime",
 	mcatlity."status" AS "catalog.lists.type.status", mcatlity."pos" AS "catalog.lists.type.position"
 FROM "mshop_catalog_list_type" AS mcatlity
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mcatlity."id" AS "catalog.lists.type.id", mcatlity."siteid" AS "catalog.lists.type.siteid",
 	mcatlity."code" AS "catalog.lists.type.code", mcatlity."domain" AS "catalog.lists.type.domain",
 	mcatlity."label" AS "catalog.lists.type.label", mcatlity."mtime" AS "catalog.lists.type.mtime",
 	mcatlity."editor" AS "catalog.lists.type.editor", mcatlity."ctime" AS "catalog.lists.type.ctime",
 	mcatlity."status" AS "catalog.lists.type.status", mcatlity."pos" AS "catalog.lists.type.position"
 FROM "mshop_catalog_list_type" AS mcatlity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/catalog/manager/lists/type/standard/search/ansi

## type/standard/update/ansi

Updates an existing catalog list type record in the database

```
mshop/catalog/manager/lists/type/standard/update/ansi = 
 UPDATE "mshop_catalog_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/catalog/manager/lists/type/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the catalog list type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/lists/type/standard/insert/ansi
* mshop/catalog/manager/lists/type/standard/newid/ansi
* mshop/catalog/manager/lists/type/standard/delete/ansi
* mshop/catalog/manager/lists/type/standard/search/ansi
* mshop/catalog/manager/lists/type/standard/count/ansi

## type/standard/update/mysql

Updates an existing catalog list type record in the database

```
mshop/catalog/manager/lists/type/standard/update/mysql = 
 UPDATE "mshop_catalog_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_catalog_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/catalog/manager/lists/type/standard/update/ansi

## type/submanagers

List of manager names that can be instantiated by the catalog list type manager

```
mshop/catalog/manager/lists/type/submanagers = Array
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

Class name of the used catalog manager implementation

```
mshop/catalog/manager/name = Standard
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
 \Aimeos\MShop\Catalog\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Catalog\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/catalog/manager/name = Mymanager
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
mshop/catalog/manager/sitemode = 3
```

* Default: 3
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole catalog domain if items from parent sites are inherited,
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
## cleanup/ansi

Deletes the categories for the given site from the database

```
mshop/catalog/manager/standard/cleanup/ansi = 
 DELETE FROM "mshop_catalog"
 WHERE :siteid AND "nleft" >= ? AND "nright" <= ?
```

* Default: mshop/catalog/manager/standard/cleanup
* Type: string - SQL statement for removing the records
* Since: 2014.03

Removes the records matched by the given site ID from the catalog
database.

The ":siteid" placeholder is replaced by the name and value of the
site ID column and the given ID or list of IDs.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/update/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/count/ansi

## cleanup/mysql

Deletes the categories for the given site from the database

```
mshop/catalog/manager/standard/cleanup/mysql = 
 DELETE FROM "mshop_catalog"
 WHERE :siteid AND "nleft" >= ? AND "nright" <= ?
```

* Default: 
 DELETE FROM "mshop_catalog"
 WHERE :siteid AND "nleft" >= ? AND "nright" <= ?


See also:

* mshop/catalog/manager/standard/cleanup/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/catalog/manager/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcat."id"
 	FROM "mshop_catalog" AS mcat
 	:joins
 	WHERE :cond
 	GROUP BY mcat."id"
 	ORDER BY mcat."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/catalog/manager/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the catalog
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

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/get/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/update/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/search-item/ansi
* mshop/catalog/manager/standard/move-left/ansi
* mshop/catalog/manager/standard/move-right/ansi
* mshop/catalog/manager/standard/update-parentid/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/catalog/manager/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcat."id"
 	FROM "mshop_catalog" AS mcat
 	:joins
 	WHERE :cond
 	GROUP BY mcat."id"
 	ORDER BY mcat."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcat."id"
 	FROM "mshop_catalog" AS mcat
 	:joins
 	WHERE :cond
 	GROUP BY mcat."id"
 	ORDER BY mcat."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/catalog/manager/standard/count/ansi

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/catalog/manager/standard/delete/ansi = 
 DELETE FROM "mshop_catalog"
 WHERE "siteid" = :siteid AND "nleft" >= ? AND "nright" <= ?
```

* Default: mshop/catalog/manager/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/standard/get/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/update/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/search-item/ansi
* mshop/catalog/manager/standard/count/ansi
* mshop/catalog/manager/standard/move-left/ansi
* mshop/catalog/manager/standard/move-right/ansi
* mshop/catalog/manager/standard/update-parentid/ansi
* mshop/catalog/manager/standard/insert-usage/ansi
* mshop/catalog/manager/standard/update-usage/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/catalog/manager/standard/delete/mysql = 
 DELETE FROM "mshop_catalog"
 WHERE "siteid" = :siteid AND "nleft" >= ? AND "nright" <= ?
```

* Default: 
 DELETE FROM "mshop_catalog"
 WHERE "siteid" = :siteid AND "nleft" >= ? AND "nright" <= ?


See also:

* mshop/catalog/manager/standard/delete/ansi

## get/ansi

Returns a node record and its complete subtree optionally limited by the level

```
mshop/catalog/manager/standard/get/ansi = 
 SELECT :columns
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft" AS "left", mcat."nright" AS "right",
 	mcat."mtime", mcat."editor", mcat."ctime", mcat."target"
 FROM "mshop_catalog" AS mcat, "mshop_catalog" AS parent
 WHERE mcat."siteid" = :siteid AND mcat."nleft" >= parent."nleft"
 	AND mcat."nleft" <= parent."nright"
 	AND parent."siteid" = :siteid AND parent."id" = ?
 	AND mcat."level" <= parent."level" + ? AND :cond
 GROUP BY :columns
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft", mcat."nright", mcat."target",
 	mcat."mtime", mcat."editor", mcat."ctime"
 ORDER BY mcat."nleft"
```

* Default: mshop/catalog/manager/standard/get
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the catalog
database. The records must be from one of the sites that are
configured via the context item. If the current site is part of
a tree of sites, the SELECT statement can retrieve all records
from the current site and the complete sub-tree of sites. This
statement retrieves all records that are part of the subtree for
the found node. The depth can be limited by the "level" number.

To limit the records matched, conditions can be added to the given
criteria object. It can contain comparisons like column names that
must match specific values which can be combined by AND, OR or NOT
operators. The resulting string of SQL conditions replaces the
":cond" placeholder before the statement is sent to the database
server.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/update/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/search-item/ansi
* mshop/catalog/manager/standard/count/ansi
* mshop/catalog/manager/standard/move-left/ansi
* mshop/catalog/manager/standard/move-right/ansi
* mshop/catalog/manager/standard/update-parentid/ansi
* mshop/catalog/manager/standard/insert-usage/ansi
* mshop/catalog/manager/standard/update-usage/ansi

## get/mysql

Returns a node record and its complete subtree optionally limited by the level

```
mshop/catalog/manager/standard/get/mysql = 
 SELECT :columns
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft" AS "left", mcat."nright" AS "right",
 	mcat."mtime", mcat."editor", mcat."ctime", mcat."target"
 FROM "mshop_catalog" AS mcat, "mshop_catalog" AS parent
 WHERE mcat."siteid" = :siteid AND mcat."nleft" >= parent."nleft"
 	AND mcat."nleft" <= parent."nright"
 	AND parent."siteid" = :siteid AND parent."id" = ?
 	AND mcat."level" <= parent."level" + ? AND :cond
 GROUP BY :columns
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft", mcat."nright", mcat."target",
 	mcat."mtime", mcat."editor", mcat."ctime"
 ORDER BY mcat."nleft"
```

* Default: 
 SELECT :columns
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft" AS "left", mcat."nright" AS "right",
 	mcat."mtime", mcat."editor", mcat."ctime", mcat."target"
 FROM "mshop_catalog" AS mcat, "mshop_catalog" AS parent
 WHERE mcat."siteid" = :siteid AND mcat."nleft" >= parent."nleft"
 	AND mcat."nleft" <= parent."nright"
 	AND parent."siteid" = :siteid AND parent."id" = ?
 	AND mcat."level" <= parent."level" + ? AND :cond
 GROUP BY :columns
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft", mcat."nright", mcat."target",
 	mcat."mtime", mcat."editor", mcat."ctime"
 ORDER BY mcat."nleft"


See also:

* mshop/catalog/manager/standard/get/ansi

## insert-usage/ansi

Updates the config, editor, ctime and mtime value of an inserted record

```
mshop/catalog/manager/standard/insert-usage/ansi = 
 UPDATE "mshop_catalog"
 SET :names "url" = ?, "config" = ?, "mtime" = ?, "editor" = ?, "target" = ?, "ctime" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/catalog/manager/standard/insert-usage
* Type: string - SQL statement for updating records
* Since: 2014.03

Each record contains some usage information like when it was
created, last modified and by whom. These information are part
of the catalog items and the generic tree manager doesn't care
about this information. Thus, they are updated after the tree
manager inserted the basic record information.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the catalog item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the method using this statement,
so the correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/get/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/search-item/ansi
* mshop/catalog/manager/standard/count/ansi
* mshop/catalog/manager/standard/move-left/ansi
* mshop/catalog/manager/standard/move-right/ansi
* mshop/catalog/manager/standard/update-parentid/ansi
* mshop/catalog/manager/standard/update-usage/ansi

## insert-usage/mysql

Updates the config, editor, ctime and mtime value of an inserted record

```
mshop/catalog/manager/standard/insert-usage/mysql = 
 UPDATE "mshop_catalog"
 SET :names "url" = ?, "config" = ?, "mtime" = ?, "editor" = ?, "target" = ?, "ctime" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_catalog"
 SET :names "url" = ?, "config" = ?, "mtime" = ?, "editor" = ?, "target" = ?, "ctime" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/catalog/manager/standard/insert-usage/ansi

## insert/ansi

Inserts a new catalog node into the database table

```
mshop/catalog/manager/standard/insert/ansi = 
 INSERT INTO "mshop_catalog" (
 	"siteid", "label", "code", "status", "parentid", "level",
 	"nleft", "nright", "config", "mtime", "ctime", "editor", "target"
 ) VALUES (
 	:siteid, ?, ?, ?, ?, ?, ?, ?, '', '1970-01-01 00:00:00', '1970-01-01 00:00:00', '', ''
 )
```

* Default: mshop/catalog/manager/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the catalog item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the insertNode() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/get/ansi
* mshop/catalog/manager/standard/update/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/search-item/ansi
* mshop/catalog/manager/standard/count/ansi
* mshop/catalog/manager/standard/move-left/ansi
* mshop/catalog/manager/standard/move-right/ansi
* mshop/catalog/manager/standard/update-parentid/ansi
* mshop/catalog/manager/standard/insert-usage/ansi
* mshop/catalog/manager/standard/update-usage/ansi

## insert/mysql

Inserts a new catalog node into the database table

```
mshop/catalog/manager/standard/insert/mysql = 
 INSERT INTO "mshop_catalog" (
 	"siteid", "label", "code", "status", "parentid", "level",
 	"nleft", "nright", "config", "mtime", "ctime", "editor", "target"
 ) VALUES (
 	:siteid, ?, ?, ?, ?, ?, ?, ?, '', '1970-01-01 00:00:00', '1970-01-01 00:00:00', '', ''
 )
```

* Default: 
 INSERT INTO "mshop_catalog" (
 	"siteid", "label", "code", "status", "parentid", "level",
 	"nleft", "nright", "config", "mtime", "ctime", "editor", "target"
 ) VALUES (
 	:siteid, ?, ?, ?, ?, ?, ?, ?, '', '1970-01-01 00:00:00', '1970-01-01 00:00:00', '', ''
 )


See also:

* mshop/catalog/manager/standard/insert/ansi

## lock/ansi

SQL statement for locking the catalog table

```
mshop/catalog/manager/standard/lock/ansi = mshop/catalog/manager/standard/lock
```

* Default: mshop/catalog/manager/standard/lock
* Type: string - Lock SQL statement
* Since: 2019.04

Updating the nested set of categories in the catalog table requires locking
the whole table to avoid data corruption. This statement will be followed by
insert or update statements and closed by an unlock statement.


## lock/mysql

SQL statement for locking the catalog table

```
mshop/catalog/manager/standard/lock/mysql = SELECT GET_LOCK('aimeos.catalog', -1)
```

* Default: mshop/catalog/manager/standard/lock

See also:

* mshop/catalog/manager/standard/lock/ansi

## move-left/ansi

Updates the left values of the nodes that are moved within the catalog tree

```
mshop/catalog/manager/standard/move-left/ansi = 
 UPDATE "mshop_catalog"
 SET "nleft" = "nleft" + ?, "level" = "level" + ?
 WHERE "siteid" = :siteid AND "nleft" >= ? AND "nleft" <= ?
```

* Default: mshop/catalog/manager/standard/move-left
* Type: string - SQL statement for updating records
* Since: 2014.03

When moving nodes or subtrees with the catalog tree, the left
value of each moved node inside the nested set must be updated
to match their new position within the catalog tree.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the catalog item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the moveNode() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/get/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/update/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/search-item/ansi
* mshop/catalog/manager/standard/count/ansi
* mshop/catalog/manager/standard/move-right/ansi
* mshop/catalog/manager/standard/update-parentid/ansi
* mshop/catalog/manager/standard/insert-usage/ansi
* mshop/catalog/manager/standard/update-usage/ansi

## move-left/mysql

Updates the left values of the nodes that are moved within the catalog tree

```
mshop/catalog/manager/standard/move-left/mysql = 
 UPDATE "mshop_catalog"
 SET "nleft" = "nleft" + ?, "level" = "level" + ?
 WHERE "siteid" = :siteid AND "nleft" >= ? AND "nleft" <= ?
```

* Default: 
 UPDATE "mshop_catalog"
 SET "nleft" = "nleft" + ?, "level" = "level" + ?
 WHERE "siteid" = :siteid AND "nleft" >= ? AND "nleft" <= ?


See also:

* mshop/catalog/manager/standard/move-left/ansi

## move-right/ansi

Updates the left values of the nodes that are moved within the catalog tree

```
mshop/catalog/manager/standard/move-right/ansi = 
 UPDATE "mshop_catalog"
 SET "nright" = "nright" + ?
 WHERE "siteid" = :siteid AND "nright" >= ? AND "nright" <= ?
```

* Default: mshop/catalog/manager/standard/move-right
* Type: string - SQL statement for updating records
* Since: 2014.03

When moving nodes or subtrees with the catalog tree, the right
value of each moved node inside the nested set must be updated
to match their new position within the catalog tree.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the catalog item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the moveNode() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/get/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/update/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/search-item/ansi
* mshop/catalog/manager/standard/count/ansi
* mshop/catalog/manager/standard/move-left/ansi
* mshop/catalog/manager/standard/update-parentid/ansi
* mshop/catalog/manager/standard/insert-usage/ansi
* mshop/catalog/manager/standard/update-usage/ansi

## move-right/mysql

Updates the left values of the nodes that are moved within the catalog tree

```
mshop/catalog/manager/standard/move-right/mysql = 
 UPDATE "mshop_catalog"
 SET "nright" = "nright" + ?
 WHERE "siteid" = :siteid AND "nright" >= ? AND "nright" <= ?
```

* Default: 
 UPDATE "mshop_catalog"
 SET "nright" = "nright" + ?
 WHERE "siteid" = :siteid AND "nright" >= ? AND "nright" <= ?


See also:

* mshop/catalog/manager/standard/move-right/ansi

## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/catalog/manager/standard/newid/ansi = mshop/catalog/manager/standard/newid
```

* Default: mshop/catalog/manager/standard/newid
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
 SELECT currval('seq_mcat_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mcat_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/get/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/update/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/search-item/ansi
* mshop/catalog/manager/standard/count/ansi
* mshop/catalog/manager/standard/move-left/ansi
* mshop/catalog/manager/standard/move-right/ansi
* mshop/catalog/manager/standard/update-parentid/ansi
* mshop/catalog/manager/standard/insert-usage/ansi
* mshop/catalog/manager/standard/update-usage/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/catalog/manager/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/catalog/manager/standard/newid

See also:

* mshop/catalog/manager/standard/newid/ansi

## search-item/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/catalog/manager/standard/search-item/ansi = 
 SELECT :columns
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft" AS "left", mcat."nright" AS "right",
 	mcat."mtime", mcat."editor", mcat."ctime", mcat."target"
 FROM "mshop_catalog" AS mcat
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft", mcat."nright", mcat."mtime", mcat."editor",
 	mcat."ctime", mcat."target"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/catalog/manager/standard/search-item
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the catalog
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

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/get/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/update/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/count/ansi
* mshop/catalog/manager/standard/move-left/ansi
* mshop/catalog/manager/standard/move-right/ansi
* mshop/catalog/manager/standard/update-parentid/ansi

## search-item/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/catalog/manager/standard/search-item/mysql = 
 SELECT :columns
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft" AS "left", mcat."nright" AS "right",
 	mcat."mtime", mcat."editor", mcat."ctime", mcat."target"
 FROM "mshop_catalog" AS mcat
 :joins
 WHERE :cond
 GROUP BY :group mcat."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft" AS "left", mcat."nright" AS "right",
 	mcat."mtime", mcat."editor", mcat."ctime", mcat."target"
 FROM "mshop_catalog" AS mcat
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft", mcat."nright", mcat."mtime", mcat."editor",
 	mcat."ctime", mcat."target"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/catalog/manager/standard/search-item/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/catalog/manager/standard/search/ansi = 
 SELECT :columns
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft" AS "left", mcat."nright" AS "right",
 	mcat."mtime", mcat."editor", mcat."ctime", mcat."target"
 FROM "mshop_catalog" AS mcat
 WHERE mcat."siteid" = :siteid AND mcat."nleft" >= ?
 	AND mcat."nright" <= ? AND :cond
 ORDER BY :order
```

* Default: mshop/catalog/manager/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the catalog
database. The records must be from one of the sites that are
configured via the context item. If the current site is part of
a tree of sites, the SELECT statement can retrieve all records
from the current site and the complete sub-tree of sites.

To limit the records matched, conditions can be added to the given
criteria object. It can contain comparisons like column names that
must match specific values which can be combined by AND, OR or NOT
operators. The resulting string of SQL conditions replaces the
":cond" placeholder before the statement is sent to the database
server.

If the records that are retrieved should be ordered by one or more
columns, the generated string of column / sort direction pairs
replaces the ":order" placeholder.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/get/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/update/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search-item/ansi
* mshop/catalog/manager/standard/count/ansi
* mshop/catalog/manager/standard/move-left/ansi
* mshop/catalog/manager/standard/move-right/ansi
* mshop/catalog/manager/standard/update-parentid/ansi
* mshop/catalog/manager/standard/insert-usage/ansi
* mshop/catalog/manager/standard/update-usage/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/catalog/manager/standard/search/mysql = 
 SELECT :columns
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft" AS "left", mcat."nright" AS "right",
 	mcat."mtime", mcat."editor", mcat."ctime", mcat."target"
 FROM "mshop_catalog" AS mcat
 WHERE mcat."siteid" = :siteid AND mcat."nleft" >= ?
 	AND mcat."nright" <= ? AND :cond
 ORDER BY :order
```

* Default: 
 SELECT :columns
 	mcat."id", mcat."code", mcat."url", mcat."label", mcat."config",
 	mcat."status", mcat."level", mcat."parentid", mcat."siteid",
 	mcat."nleft" AS "left", mcat."nright" AS "right",
 	mcat."mtime", mcat."editor", mcat."ctime", mcat."target"
 FROM "mshop_catalog" AS mcat
 WHERE mcat."siteid" = :siteid AND mcat."nleft" >= ?
 	AND mcat."nright" <= ? AND :cond
 ORDER BY :order


See also:

* mshop/catalog/manager/standard/search/ansi

## unlock/ansi

SQL statement for unlocking the catalog table

```
mshop/catalog/manager/standard/unlock/ansi = mshop/catalog/manager/standard/unlock
```

* Default: mshop/catalog/manager/standard/unlock
* Type: string - Lock SQL statement
* Since: 2019.04

Updating the nested set of categories in the catalog table requires locking
the whole table to avoid data corruption. This statement will be executed
after the table is locked and insert or update statements have been sent to
the database.


## unlock/mysql

SQL statement for unlocking the catalog table

```
mshop/catalog/manager/standard/unlock/mysql = SELECT RELEASE_LOCK('aimeos.catalog')
```

* Default: mshop/catalog/manager/standard/unlock

See also:

* mshop/catalog/manager/standard/unlock/ansi

## update-parentid/ansi

Updates the parent ID after moving a node record

```
mshop/catalog/manager/standard/update-parentid/ansi = 
 UPDATE "mshop_catalog"
 SET "parentid" = ?
 WHERE "siteid" = :siteid AND "id" = ?
```

* Default: mshop/catalog/manager/standard/update-parentid
* Type: string - SQL statement for updating records
* Since: 2014.03

When moving nodes with the catalog tree, the parent ID
references must be updated to match the new parent.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the catalog item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the moveNode() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/get/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/update/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/search-item/ansi
* mshop/catalog/manager/standard/count/ansi
* mshop/catalog/manager/standard/move-left/ansi
* mshop/catalog/manager/standard/move-right/ansi
* mshop/catalog/manager/standard/insert-usage/ansi
* mshop/catalog/manager/standard/update-usage/ansi

## update-parentid/mysql

Updates the parent ID after moving a node record

```
mshop/catalog/manager/standard/update-parentid/mysql = 
 UPDATE "mshop_catalog"
 SET "parentid" = ?
 WHERE "siteid" = :siteid AND "id" = ?
```

* Default: 
 UPDATE "mshop_catalog"
 SET "parentid" = ?
 WHERE "siteid" = :siteid AND "id" = ?


See also:

* mshop/catalog/manager/standard/update-parentid/ansi

## update-usage/ansi

Updates the config, editor and mtime value of an updated record

```
mshop/catalog/manager/standard/update-usage/ansi = 
 UPDATE "mshop_catalog"
 SET "url" = ?, "config" = ?, "mtime" = ?, "editor" = ?, "target" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/catalog/manager/standard/update-usage
* Type: string - SQL statement for updating records
* Since: 2014.03

Each record contains some usage information like when it was
created, last modified and by whom. These information are part
of the catalog items and the generic tree manager doesn't care
about this information. Thus, they are updated after the tree
manager saved the basic record information.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the catalog item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the method using this statement,
so the correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/get/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/search-item/ansi
* mshop/catalog/manager/standard/count/ansi
* mshop/catalog/manager/standard/move-left/ansi
* mshop/catalog/manager/standard/move-right/ansi
* mshop/catalog/manager/standard/update-parentid/ansi
* mshop/catalog/manager/standard/insert-usage/ansi

## update-usage/mysql

Updates the config, editor and mtime value of an updated record

```
mshop/catalog/manager/standard/update-usage/mysql = 
 UPDATE "mshop_catalog"
 SET "url" = ?, "config" = ?, "mtime" = ?, "editor" = ?, "target" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_catalog"
 SET "url" = ?, "config" = ?, "mtime" = ?, "editor" = ?, "target" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/catalog/manager/standard/update-usage/ansi

## update/ansi

Updates an existing catalog node in the database

```
mshop/catalog/manager/standard/update/ansi = 
 UPDATE "mshop_catalog"
 SET "label" = ?, "code" = ?, "status" = ?
 WHERE "siteid" = :siteid AND "id" = ?
```

* Default: mshop/catalog/manager/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the catalog item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveNode() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/catalog/manager/standard/delete/ansi
* mshop/catalog/manager/standard/get/ansi
* mshop/catalog/manager/standard/insert/ansi
* mshop/catalog/manager/standard/newid/ansi
* mshop/catalog/manager/standard/search/ansi
* mshop/catalog/manager/standard/search-item/ansi
* mshop/catalog/manager/standard/count/ansi
* mshop/catalog/manager/standard/move-left/ansi
* mshop/catalog/manager/standard/move-right/ansi
* mshop/catalog/manager/standard/update-parentid/ansi
* mshop/catalog/manager/standard/insert-usage/ansi
* mshop/catalog/manager/standard/update-usage/ansi

## update/mysql

Updates an existing catalog node in the database

```
mshop/catalog/manager/standard/update/mysql = 
 UPDATE "mshop_catalog"
 SET "label" = ?, "code" = ?, "status" = ?
 WHERE "siteid" = :siteid AND "id" = ?
```

* Default: 
 UPDATE "mshop_catalog"
 SET "label" = ?, "code" = ?, "status" = ?
 WHERE "siteid" = :siteid AND "id" = ?


See also:

* mshop/catalog/manager/standard/update/ansi

# submanagers

List of manager names that can be instantiated by the catalog manager

```
mshop/catalog/manager/submanagers = Array
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
