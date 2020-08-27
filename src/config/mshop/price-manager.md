
# decorators
## excludes

Excludes decorators added by the "common" option from the price manager

```
mshop/price/manager/decorators/excludes = Array
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
around the price manager.

```
 mshop/price/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the price manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/decorators/global
* mshop/price/manager/decorators/local

## global

Adds a list of globally available decorators only to the price manager

```
mshop/price/manager/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the price manager.

```
 mshop/price/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the price
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/decorators/excludes
* mshop/price/manager/decorators/local

## local

Adds a list of local decorators only to the price manager

```
mshop/price/manager/decorators/local = Array
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
("\Aimeos\MShop\Price\Manager\Decorator\*") around the price manager.

```
 mshop/price/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Price\Manager\Decorator\Decorator2" only to the price
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/decorators/excludes
* mshop/price/manager/decorators/global

# lists
## decorators/excludes

Excludes decorators added by the "common" option from the price list manager

```
mshop/price/manager/lists/decorators/excludes = Array
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
around the price list manager.

```
 mshop/price/manager/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the price list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/lists/decorators/global
* mshop/price/manager/lists/decorators/local

## decorators/global

Adds a list of globally available decorators only to the price list manager

```
mshop/price/manager/lists/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the price list
manager.

```
 mshop/price/manager/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the price
list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/lists/decorators/excludes
* mshop/price/manager/lists/decorators/local

## decorators/local

Adds a list of local decorators only to the price list manager

```
mshop/price/manager/lists/decorators/local = Array
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
("\Aimeos\MShop\Price\Manager\Lists\Manager\Decorator\*") around the
price list manager.

```
 mshop/price/manager/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Price\Manager\Lists\Decorator\Decorator2" only to the
price list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/lists/decorators/excludes
* mshop/price/manager/lists/decorators/global

## name

Class name of the used price list manager implementation

```
mshop/price/manager/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default price list manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Price\Manager\Lists\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Price\Manager\Lists\Mylist
```

then you have to set the this configuration option:

```
 mshop/price/manager/lists/name = Mylist
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
mshop/price/manager/lists/standard/aggregate/ansi = 
 SELECT "key", COUNT("id") AS "count"
 FROM (
 	SELECT :key AS "key", mprili."id" AS "id"
 	FROM "mshop_price_list" AS mprili
 	:joins
 	WHERE :cond
 	GROUP BY :key, mprili."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY "key"
```

* Default: mshop/price/manager/lists/standard/aggregate
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

* mshop/price/manager/lists/standard/insert/ansi
* mshop/price/manager/lists/standard/update/ansi
* mshop/price/manager/lists/standard/newid/ansi
* mshop/price/manager/lists/standard/delete/ansi
* mshop/price/manager/lists/standard/search/ansi
* mshop/price/manager/lists/standard/count/ansi

## standard/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/price/manager/lists/standard/aggregate/mysql = 
 SELECT "key", COUNT("id") AS "count"
 FROM (
 	SELECT :key AS "key", mprili."id" AS "id"
 	FROM "mshop_price_list" AS mprili
 	:joins
 	WHERE :cond
 	GROUP BY :key, mprili."id"
 	ORDER BY :order
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY "key"
```

* Default: 
 SELECT "key", COUNT("id") AS "count"
 FROM (
 	SELECT :key AS "key", mprili."id" AS "id"
 	FROM "mshop_price_list" AS mprili
 	:joins
 	WHERE :cond
 	GROUP BY :key, mprili."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY "key"


See also:

* mshop/price/manager/lists/standard/aggregate/ansi

## standard/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/price/manager/lists/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mprili."id"
 	FROM "mshop_price_list" AS mprili
 	:joins
 	WHERE :cond
 	ORDER BY mprili."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/price/manager/lists/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the price
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

* mshop/price/manager/lists/standard/insert/ansi
* mshop/price/manager/lists/standard/update/ansi
* mshop/price/manager/lists/standard/newid/ansi
* mshop/price/manager/lists/standard/delete/ansi
* mshop/price/manager/lists/standard/search/ansi
* mshop/price/manager/lists/standard/aggregate/ansi

## standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/price/manager/lists/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mprili."id"
 	FROM "mshop_price_list" AS mprili
 	:joins
 	WHERE :cond
 	ORDER BY mprili."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mprili."id"
 	FROM "mshop_price_list" AS mprili
 	:joins
 	WHERE :cond
 	ORDER BY mprili."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/price/manager/lists/standard/count/ansi

## standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/price/manager/lists/standard/delete/ansi = 
 DELETE FROM "mshop_price_list"
 WHERE :cond AND siteid = ?
```

* Default: mshop/price/manager/lists/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the price database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/lists/standard/insert/ansi
* mshop/price/manager/lists/standard/update/ansi
* mshop/price/manager/lists/standard/newid/ansi
* mshop/price/manager/lists/standard/search/ansi
* mshop/price/manager/lists/standard/count/ansi
* mshop/price/manager/lists/standard/aggregate/ansi

## standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/price/manager/lists/standard/delete/mysql = 
 DELETE FROM "mshop_price_list"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_price_list"
 WHERE :cond AND siteid = ?


See also:

* mshop/price/manager/lists/standard/delete/ansi

## standard/insert/ansi

Inserts a new price list record into the database table

```
mshop/price/manager/lists/standard/insert/ansi = 
 INSERT INTO "mshop_price_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/price/manager/lists/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the price list item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/lists/standard/update/ansi
* mshop/price/manager/lists/standard/newid/ansi
* mshop/price/manager/lists/standard/delete/ansi
* mshop/price/manager/lists/standard/search/ansi
* mshop/price/manager/lists/standard/count/ansi
* mshop/price/manager/lists/standard/aggregate/ansi

## standard/insert/mysql

Inserts a new price list record into the database table

```
mshop/price/manager/lists/standard/insert/mysql = 
 INSERT INTO "mshop_price_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_price_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/price/manager/lists/standard/insert/ansi

## standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/price/manager/lists/standard/newid/ansi = mshop/price/manager/lists/standard/newid
```

* Default: mshop/price/manager/lists/standard/newid
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
 SELECT currval('seq_mprili_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mprili_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/price/manager/lists/standard/insert/ansi
* mshop/price/manager/lists/standard/update/ansi
* mshop/price/manager/lists/standard/delete/ansi
* mshop/price/manager/lists/standard/search/ansi
* mshop/price/manager/lists/standard/count/ansi
* mshop/price/manager/lists/standard/aggregate/ansi

## standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/price/manager/lists/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/price/manager/lists/standard/newid

See also:

* mshop/price/manager/lists/standard/newid/ansi

## standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/price/manager/lists/standard/search/ansi = 
 SELECT :columns
 	mprili."id" AS "price.lists.id", mprili."parentid" AS "price.lists.parentid",
 	mprili."siteid" AS "price.lists.siteid", mprili."type" AS "price.lists.type",
 	mprili."domain" AS "price.lists.domain", mprili."refid" AS "price.lists.refid",
 	mprili."start" AS "price.lists.datestart", mprili."end" AS "price.lists.dateend",
 	mprili."config" AS "price.lists.config", mprili."pos" AS "price.lists.position",
 	mprili."status" AS "price.lists.status", mprili."mtime" AS "price.lists.mtime",
 	mprili."editor" AS "price.lists.editor", mprili."ctime" AS "price.lists.ctime"
 FROM "mshop_price_list" AS mprili
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/price/manager/lists/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the price
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

* mshop/price/manager/lists/standard/insert/ansi
* mshop/price/manager/lists/standard/update/ansi
* mshop/price/manager/lists/standard/newid/ansi
* mshop/price/manager/lists/standard/delete/ansi
* mshop/price/manager/lists/standard/count/ansi
* mshop/price/manager/lists/standard/aggregate/ansi

## standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/price/manager/lists/standard/search/mysql = 
 SELECT :columns
 	mprili."id" AS "price.lists.id", mprili."parentid" AS "price.lists.parentid",
 	mprili."siteid" AS "price.lists.siteid", mprili."type" AS "price.lists.type",
 	mprili."domain" AS "price.lists.domain", mprili."refid" AS "price.lists.refid",
 	mprili."start" AS "price.lists.datestart", mprili."end" AS "price.lists.dateend",
 	mprili."config" AS "price.lists.config", mprili."pos" AS "price.lists.position",
 	mprili."status" AS "price.lists.status", mprili."mtime" AS "price.lists.mtime",
 	mprili."editor" AS "price.lists.editor", mprili."ctime" AS "price.lists.ctime"
 FROM "mshop_price_list" AS mprili
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mprili."id" AS "price.lists.id", mprili."parentid" AS "price.lists.parentid",
 	mprili."siteid" AS "price.lists.siteid", mprili."type" AS "price.lists.type",
 	mprili."domain" AS "price.lists.domain", mprili."refid" AS "price.lists.refid",
 	mprili."start" AS "price.lists.datestart", mprili."end" AS "price.lists.dateend",
 	mprili."config" AS "price.lists.config", mprili."pos" AS "price.lists.position",
 	mprili."status" AS "price.lists.status", mprili."mtime" AS "price.lists.mtime",
 	mprili."editor" AS "price.lists.editor", mprili."ctime" AS "price.lists.ctime"
 FROM "mshop_price_list" AS mprili
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/price/manager/lists/standard/search/ansi

## standard/update/ansi

Updates an existing price list record in the database

```
mshop/price/manager/lists/standard/update/ansi = 
 UPDATE "mshop_price_list"
 SET :names
 	"parentid"=?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/price/manager/lists/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the price list item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/lists/standard/insert/ansi
* mshop/price/manager/lists/standard/newid/ansi
* mshop/price/manager/lists/standard/delete/ansi
* mshop/price/manager/lists/standard/search/ansi
* mshop/price/manager/lists/standard/count/ansi
* mshop/price/manager/lists/standard/aggregate/ansi

## standard/update/mysql

Updates an existing price list record in the database

```
mshop/price/manager/lists/standard/update/mysql = 
 UPDATE "mshop_price_list"
 SET :names
 	"parentid"=?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_price_list"
 SET :names
 	"parentid"=?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/price/manager/lists/standard/update/ansi

## submanagers

List of manager names that can be instantiated by the price list manager

```
mshop/price/manager/lists/submanagers = Array
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

Excludes decorators added by the "common" option from the price list type manager

```
mshop/price/manager/lists/type/decorators/excludes = Array
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
around the price list type manager.

```
 mshop/price/manager/lists/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the price list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/lists/type/decorators/global
* mshop/price/manager/lists/type/decorators/local

## type/decorators/global

Adds a list of globally available decorators only to the price list type manager

```
mshop/price/manager/lists/type/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the price list type
manager.

```
 mshop/price/manager/lists/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the price
list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/lists/type/decorators/excludes
* mshop/price/manager/lists/type/decorators/local

## type/decorators/local

Adds a list of local decorators only to the price list type manager

```
mshop/price/manager/lists/type/decorators/local = Array
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
("\Aimeos\MShop\Price\Manager\Lists\Type\Decorator\*") around the
price list type manager.

```
 mshop/price/manager/lists/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Price\Manager\Lists\Type\Decorator\Decorator2" only to
the price list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/lists/type/decorators/excludes
* mshop/price/manager/lists/type/decorators/global

## type/name

Class name of the used price list type manager implementation

```
mshop/price/manager/lists/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default price list type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Price\Manager\Lists\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Price\Manager\Lists\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/price/manager/lists/type/name = Mytype
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
mshop/price/manager/lists/type/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mprility."id"
 	FROM "mshop_price_list_type" AS mprility
 	:joins
 	WHERE :cond
 	ORDER BY mprility."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/price/manager/lists/type/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the price
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

* mshop/price/manager/lists/type/standard/insert/ansi
* mshop/price/manager/lists/type/standard/update/ansi
* mshop/price/manager/lists/type/standard/newid/ansi
* mshop/price/manager/lists/type/standard/delete/ansi
* mshop/price/manager/lists/type/standard/search/ansi

## type/standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/price/manager/lists/type/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mprility."id"
 	FROM "mshop_price_list_type" AS mprility
 	:joins
 	WHERE :cond
 	ORDER BY mprility."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mprility."id"
 	FROM "mshop_price_list_type" AS mprility
 	:joins
 	WHERE :cond
 	ORDER BY mprility."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/price/manager/lists/type/standard/count/ansi

## type/standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/price/manager/lists/type/standard/delete/ansi = 
 DELETE FROM "mshop_price_list_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/price/manager/lists/type/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the price database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/lists/type/standard/insert/ansi
* mshop/price/manager/lists/type/standard/update/ansi
* mshop/price/manager/lists/type/standard/newid/ansi
* mshop/price/manager/lists/type/standard/search/ansi
* mshop/price/manager/lists/type/standard/count/ansi

## type/standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/price/manager/lists/type/standard/delete/mysql = 
 DELETE FROM "mshop_price_list_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_price_list_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/price/manager/lists/type/standard/delete/ansi

## type/standard/insert/ansi

Inserts a new price list type record into the database table

```
mshop/price/manager/lists/type/standard/insert/ansi = 
 INSERT INTO "mshop_price_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/price/manager/lists/type/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the price list type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/lists/type/standard/update/ansi
* mshop/price/manager/lists/type/standard/newid/ansi
* mshop/price/manager/lists/type/standard/delete/ansi
* mshop/price/manager/lists/type/standard/search/ansi
* mshop/price/manager/lists/type/standard/count/ansi

## type/standard/insert/mysql

Inserts a new price list type record into the database table

```
mshop/price/manager/lists/type/standard/insert/mysql = 
 INSERT INTO "mshop_price_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_price_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/price/manager/lists/type/standard/insert/ansi

## type/standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/price/manager/lists/type/standard/newid/ansi = mshop/price/manager/lists/type/standard/newid
```

* Default: mshop/price/manager/lists/type/standard/newid
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
 SELECT currval('seq_mprility_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mprility_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/price/manager/lists/type/standard/insert/ansi
* mshop/price/manager/lists/type/standard/update/ansi
* mshop/price/manager/lists/type/standard/delete/ansi
* mshop/price/manager/lists/type/standard/search/ansi
* mshop/price/manager/lists/type/standard/count/ansi

## type/standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/price/manager/lists/type/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/price/manager/lists/type/standard/newid

See also:

* mshop/price/manager/lists/type/standard/newid/ansi

## type/standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/price/manager/lists/type/standard/search/ansi = 
 SELECT :columns
 	mprility."id" AS "price.lists.type.id", mprility."siteid" AS "price.lists.type.siteid",
 	mprility."code" AS "price.lists.type.code", mprility."domain" AS "price.lists.type.domain",
 	mprility."label" AS "price.lists.type.label", mprility."status" AS "price.lists.type.status",
 	mprility."mtime" AS "price.lists.type.mtime", mprility."editor" AS "price.lists.type.editor",
 	mprility."ctime" AS "price.lists.type.ctime", mprility."pos" AS "price.lists.type.position"
 FROM "mshop_price_list_type" AS mprility
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/price/manager/lists/type/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the price
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

* mshop/price/manager/lists/type/standard/insert/ansi
* mshop/price/manager/lists/type/standard/update/ansi
* mshop/price/manager/lists/type/standard/newid/ansi
* mshop/price/manager/lists/type/standard/delete/ansi
* mshop/price/manager/lists/type/standard/count/ansi

## type/standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/price/manager/lists/type/standard/search/mysql = 
 SELECT :columns
 	mprility."id" AS "price.lists.type.id", mprility."siteid" AS "price.lists.type.siteid",
 	mprility."code" AS "price.lists.type.code", mprility."domain" AS "price.lists.type.domain",
 	mprility."label" AS "price.lists.type.label", mprility."status" AS "price.lists.type.status",
 	mprility."mtime" AS "price.lists.type.mtime", mprility."editor" AS "price.lists.type.editor",
 	mprility."ctime" AS "price.lists.type.ctime", mprility."pos" AS "price.lists.type.position"
 FROM "mshop_price_list_type" AS mprility
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mprility."id" AS "price.lists.type.id", mprility."siteid" AS "price.lists.type.siteid",
 	mprility."code" AS "price.lists.type.code", mprility."domain" AS "price.lists.type.domain",
 	mprility."label" AS "price.lists.type.label", mprility."status" AS "price.lists.type.status",
 	mprility."mtime" AS "price.lists.type.mtime", mprility."editor" AS "price.lists.type.editor",
 	mprility."ctime" AS "price.lists.type.ctime", mprility."pos" AS "price.lists.type.position"
 FROM "mshop_price_list_type" AS mprility
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/price/manager/lists/type/standard/search/ansi

## type/standard/update/ansi

Updates an existing price list type record in the database

```
mshop/price/manager/lists/type/standard/update/ansi = 
 UPDATE "mshop_price_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/price/manager/lists/type/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the price list type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/lists/type/standard/insert/ansi
* mshop/price/manager/lists/type/standard/newid/ansi
* mshop/price/manager/lists/type/standard/delete/ansi
* mshop/price/manager/lists/type/standard/search/ansi
* mshop/price/manager/lists/type/standard/count/ansi

## type/standard/update/mysql

Updates an existing price list type record in the database

```
mshop/price/manager/lists/type/standard/update/mysql = 
 UPDATE "mshop_price_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_price_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/price/manager/lists/type/standard/update/ansi

## type/submanagers

List of manager names that can be instantiated by the price list type manager

```
mshop/price/manager/lists/type/submanagers = Array
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

Class name of the used price manager implementation

```
mshop/price/manager/name = Standard
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
 \Aimeos\MShop\Price\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Price\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/price/manager/name = Mymanager
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyManager"!


# property
## decorators/excludes

Excludes decorators added by the "common" option from the price property manager

```
mshop/price/manager/property/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the price property manager.

```
 mshop/price/manager/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the price property manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/property/decorators/global
* mshop/price/manager/property/decorators/local

## decorators/global

Adds a list of globally available decorators only to the price property manager

```
mshop/price/manager/property/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the price property
manager.

```
 mshop/price/manager/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the price
property manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/property/decorators/excludes
* mshop/price/manager/property/decorators/local

## decorators/local

Adds a list of local decorators only to the price property manager

```
mshop/price/manager/property/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Price\Manager\Property\Decorator\*") around the price
property manager.

```
 mshop/price/manager/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Price\Manager\Property\Decorator\Decorator2" only to the
price property manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/property/decorators/excludes
* mshop/price/manager/property/decorators/global

## name

Class name of the used price property manager implementation

```
mshop/price/manager/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.01

Each default price property manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Price\Manager\Property\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Price\Manager\Property\Myproperty
```

then you have to set the this configuration option:

```
 mshop/price/manager/property/name = Myproperty
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyProperty"!


## standard/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/price/manager/property/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mpripr."id"
 	FROM "mshop_price_property" AS mpripr
 	:joins
 	WHERE :cond
 	ORDER BY mpripr."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/price/manager/property/standard/count
* Type: string - SQL statement for counting items
* Since: 2018.01

Counts all records matched by the given criteria from the price
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

* mshop/price/manager/property/standard/insert/ansi
* mshop/price/manager/property/standard/update/ansi
* mshop/price/manager/property/standard/newid/ansi
* mshop/price/manager/property/standard/delete/ansi
* mshop/price/manager/property/standard/search/ansi

## standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/price/manager/property/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mpripr."id"
 	FROM "mshop_price_property" AS mpripr
 	:joins
 	WHERE :cond
 	ORDER BY mpripr."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mpripr."id"
 	FROM "mshop_price_property" AS mpripr
 	:joins
 	WHERE :cond
 	ORDER BY mpripr."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/price/manager/property/standard/count/ansi

## standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/price/manager/property/standard/delete/ansi = 
 DELETE FROM "mshop_price_property"
 WHERE :cond AND siteid = ?
```

* Default: mshop/price/manager/property/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2018.01

Removes the records specified by the given IDs from the price database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/property/standard/insert/ansi
* mshop/price/manager/property/standard/update/ansi
* mshop/price/manager/property/standard/newid/ansi
* mshop/price/manager/property/standard/search/ansi
* mshop/price/manager/property/standard/count/ansi

## standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/price/manager/property/standard/delete/mysql = 
 DELETE FROM "mshop_price_property"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_price_property"
 WHERE :cond AND siteid = ?


See also:

* mshop/price/manager/property/standard/delete/ansi

## standard/insert/ansi

Inserts a new price property record into the database table

```
mshop/price/manager/property/standard/insert/ansi = 
 INSERT INTO "mshop_price_property" ( :names
 	"parentid", "key", "type", "langid", "value",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/price/manager/property/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2018.01

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the price property item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/property/standard/update/ansi
* mshop/price/manager/property/standard/newid/ansi
* mshop/price/manager/property/standard/delete/ansi
* mshop/price/manager/property/standard/search/ansi
* mshop/price/manager/property/standard/count/ansi

## standard/insert/mysql

Inserts a new price property record into the database table

```
mshop/price/manager/property/standard/insert/mysql = 
 INSERT INTO "mshop_price_property" ( :names
 	"parentid", "key", "type", "langid", "value",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_price_property" ( :names
 	"parentid", "key", "type", "langid", "value",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/price/manager/property/standard/insert/ansi

## standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/price/manager/property/standard/newid/ansi = mshop/price/manager/property/standard/newid
```

* Default: mshop/price/manager/property/standard/newid
* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2018.01

As soon as a new record is inserted into the database table,
the database server generates a new and unique identifier for
that record. This ID can be used for retrieving, updating and
deleting that specific record from the table again.

For MySQL:
```
 SELECT LAST_INSERT_ID()
For PostgreSQL:
 SELECT currval('seq_mpripr_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mpripr_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/price/manager/property/standard/insert/ansi
* mshop/price/manager/property/standard/update/ansi
* mshop/price/manager/property/standard/delete/ansi
* mshop/price/manager/property/standard/search/ansi
* mshop/price/manager/property/standard/count/ansi

## standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/price/manager/property/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/price/manager/property/standard/newid

See also:

* mshop/price/manager/property/standard/newid/ansi

## standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/price/manager/property/standard/search/ansi = 
 SELECT :columns
 	mpripr."id" AS "price.property.id", mpripr."parentid" AS "price.property.parentid",
 	mpripr."siteid" AS "price.property.siteid", mpripr."type" AS "price.property.type",
 	mpripr."langid" AS "price.property.languageid", mpripr."value" AS "price.property.value",
 	mpripr."mtime" AS "price.property.mtime", mpripr."editor" AS "price.property.editor",
 	mpripr."ctime" AS "price.property.ctime"
 FROM "mshop_price_property" AS mpripr
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/price/manager/property/standard/search
* Type: string - SQL statement for searching items
* Since: 2018.01

Fetches the records matched by the given criteria from the price
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

* mshop/price/manager/property/standard/insert/ansi
* mshop/price/manager/property/standard/update/ansi
* mshop/price/manager/property/standard/newid/ansi
* mshop/price/manager/property/standard/delete/ansi
* mshop/price/manager/property/standard/count/ansi

## standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/price/manager/property/standard/search/mysql = 
 SELECT :columns
 	mpripr."id" AS "price.property.id", mpripr."parentid" AS "price.property.parentid",
 	mpripr."siteid" AS "price.property.siteid", mpripr."type" AS "price.property.type",
 	mpripr."langid" AS "price.property.languageid", mpripr."value" AS "price.property.value",
 	mpripr."mtime" AS "price.property.mtime", mpripr."editor" AS "price.property.editor",
 	mpripr."ctime" AS "price.property.ctime"
 FROM "mshop_price_property" AS mpripr
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mpripr."id" AS "price.property.id", mpripr."parentid" AS "price.property.parentid",
 	mpripr."siteid" AS "price.property.siteid", mpripr."type" AS "price.property.type",
 	mpripr."langid" AS "price.property.languageid", mpripr."value" AS "price.property.value",
 	mpripr."mtime" AS "price.property.mtime", mpripr."editor" AS "price.property.editor",
 	mpripr."ctime" AS "price.property.ctime"
 FROM "mshop_price_property" AS mpripr
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/price/manager/property/standard/search/ansi

## standard/update/ansi

Updates an existing price property record in the database

```
mshop/price/manager/property/standard/update/ansi = 
 UPDATE "mshop_price_property"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "langid" = ?,
 	"value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/price/manager/property/standard/update
* Type: string - SQL statement for updating records
* Since: 2018.01

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the price property item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/property/standard/insert/ansi
* mshop/price/manager/property/standard/newid/ansi
* mshop/price/manager/property/standard/delete/ansi
* mshop/price/manager/property/standard/search/ansi
* mshop/price/manager/property/standard/count/ansi

## standard/update/mysql

Updates an existing price property record in the database

```
mshop/price/manager/property/standard/update/mysql = 
 UPDATE "mshop_price_property"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "langid" = ?,
 	"value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_price_property"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "langid" = ?,
 	"value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/price/manager/property/standard/update/ansi

## submanagers

List of manager names that can be instantiated by the price property manager

```
mshop/price/manager/property/submanagers = Array
(
)
```

* Default: Array
* Type: array - List of sub-manager names
* Since: 2018.01

Managers provide a generic interface to the underlying storage.
Each manager has or can have sub-managers caring about particular
aspects. Each of these sub-managers can be instantiated by its
parent manager using the getSubManager() method.

The search keys from sub-managers can be normally used in the
manager as well. It allows you to search for items of the manager
using the search keys of the sub-managers to further limit the
retrieved list of items.


## type/decorators/excludes

Excludes decorators added by the "common" option from the price property type manager

```
mshop/price/manager/property/type/decorators/excludes = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the price property type manager.

```
 mshop/price/manager/property/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the price property type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/property/type/decorators/global
* mshop/price/manager/property/type/decorators/local

## type/decorators/global

Adds a list of globally available decorators only to the price property type manager

```
mshop/price/manager/property/type/decorators/global = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the price property
type manager.

```
 mshop/price/manager/property/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the price
property type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/property/type/decorators/excludes
* mshop/price/manager/property/type/decorators/local

## type/decorators/local

Adds a list of local decorators only to the price property type manager

```
mshop/price/manager/property/type/decorators/local = Array
(
)
```

* Default: Array
* Type: array - List of decorator names
* Since: 2018.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Price\Manager\Property\Type\Decorator\*") around the
price property type manager.

```
 mshop/price/manager/property/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Price\Manager\Property\Type\Decorator\Decorator2" only
to the price property type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/property/type/decorators/excludes
* mshop/price/manager/property/type/decorators/global

## type/name

Class name of the used price property type manager implementation

```
mshop/price/manager/property/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.01

Each default price property type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Price\Manager\Lists\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Price\Manager\Lists\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/price/manager/property/type/name = Mytype
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
mshop/price/manager/property/type/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mpriprty."id"
 	FROM "mshop_price_property_type" mpriprty
 	:joins
 	WHERE :cond
 	ORDER BY mpriprty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/price/manager/property/type/standard/count
* Type: string - SQL statement for counting items
* Since: 2018.01

Counts all records matched by the given criteria from the price
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

* mshop/price/manager/property/type/standard/insert/ansi
* mshop/price/manager/property/type/standard/update/ansi
* mshop/price/manager/property/type/standard/newid/ansi
* mshop/price/manager/property/type/standard/delete/ansi
* mshop/price/manager/property/type/standard/search/ansi

## type/standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/price/manager/property/type/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mpriprty."id"
 	FROM "mshop_price_property_type" mpriprty
 	:joins
 	WHERE :cond
 	ORDER BY mpriprty."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mpriprty."id"
 	FROM "mshop_price_property_type" mpriprty
 	:joins
 	WHERE :cond
 	ORDER BY mpriprty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/price/manager/property/type/standard/count/ansi

## type/standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/price/manager/property/type/standard/delete/ansi = 
 DELETE FROM "mshop_price_property_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/price/manager/property/type/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2018.01

Removes the records specified by the given IDs from the price database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/property/type/standard/insert/ansi
* mshop/price/manager/property/type/standard/update/ansi
* mshop/price/manager/property/type/standard/newid/ansi
* mshop/price/manager/property/type/standard/search/ansi
* mshop/price/manager/property/type/standard/count/ansi

## type/standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/price/manager/property/type/standard/delete/mysql = 
 DELETE FROM "mshop_price_property_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_price_property_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/price/manager/property/type/standard/delete/ansi

## type/standard/insert/ansi

Inserts a new price property type record into the database table

```
mshop/price/manager/property/type/standard/insert/ansi = 
 INSERT INTO "mshop_price_property_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/price/manager/property/type/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2018.01

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the price type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/property/type/standard/update/ansi
* mshop/price/manager/property/type/standard/newid/ansi
* mshop/price/manager/property/type/standard/delete/ansi
* mshop/price/manager/property/type/standard/search/ansi
* mshop/price/manager/property/type/standard/count/ansi

## type/standard/insert/mysql

Inserts a new price property type record into the database table

```
mshop/price/manager/property/type/standard/insert/mysql = 
 INSERT INTO "mshop_price_property_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_price_property_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/price/manager/property/type/standard/insert/ansi

## type/standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/price/manager/property/type/standard/newid/ansi = mshop/price/manager/property/type/standard/newid
```

* Default: mshop/price/manager/property/type/standard/newid
* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2018.01

As soon as a new record is inserted into the database table,
the database server generates a new and unique identifier for
that record. This ID can be used for retrieving, updating and
deleting that specific record from the table again.

For MySQL:
```
 SELECT LAST_INSERT_ID()
For PostgreSQL:
 SELECT currval('seq_mpriprty_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mpriprty_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/price/manager/property/type/standard/insert/ansi
* mshop/price/manager/property/type/standard/update/ansi
* mshop/price/manager/property/type/standard/delete/ansi
* mshop/price/manager/property/type/standard/search/ansi
* mshop/price/manager/property/type/standard/count/ansi

## type/standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/price/manager/property/type/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/price/manager/property/type/standard/newid

See also:

* mshop/price/manager/property/type/standard/newid/ansi

## type/standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/price/manager/property/type/standard/search/ansi = 
 SELECT :columns
 	mpriprty."id" AS "price.property.type.id", mpriprty."siteid" AS "price.property.type.siteid",
 	mpriprty."code" AS "price.property.type.code", mpriprty."domain" AS "price.property.type.domain",
 	mpriprty."label" AS "price.property.type.label", mpriprty."status" AS "price.property.type.status",
 	mpriprty."mtime" AS "price.property.type.mtime", mpriprty."editor" AS "price.property.type.editor",
 	mpriprty."ctime" AS "price.property.type.ctime", mpriprty."pos" AS "price.property.type.position"
 FROM "mshop_price_property_type" mpriprty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/price/manager/property/type/standard/search
* Type: string - SQL statement for searching items
* Since: 2018.01

Fetches the records matched by the given criteria from the price
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

* mshop/price/manager/property/type/standard/insert/ansi
* mshop/price/manager/property/type/standard/update/ansi
* mshop/price/manager/property/type/standard/newid/ansi
* mshop/price/manager/property/type/standard/delete/ansi
* mshop/price/manager/property/type/standard/count/ansi

## type/standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/price/manager/property/type/standard/search/mysql = 
 SELECT :columns
 	mpriprty."id" AS "price.property.type.id", mpriprty."siteid" AS "price.property.type.siteid",
 	mpriprty."code" AS "price.property.type.code", mpriprty."domain" AS "price.property.type.domain",
 	mpriprty."label" AS "price.property.type.label", mpriprty."status" AS "price.property.type.status",
 	mpriprty."mtime" AS "price.property.type.mtime", mpriprty."editor" AS "price.property.type.editor",
 	mpriprty."ctime" AS "price.property.type.ctime", mpriprty."pos" AS "price.property.type.position"
 FROM "mshop_price_property_type" mpriprty
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mpriprty."id" AS "price.property.type.id", mpriprty."siteid" AS "price.property.type.siteid",
 	mpriprty."code" AS "price.property.type.code", mpriprty."domain" AS "price.property.type.domain",
 	mpriprty."label" AS "price.property.type.label", mpriprty."status" AS "price.property.type.status",
 	mpriprty."mtime" AS "price.property.type.mtime", mpriprty."editor" AS "price.property.type.editor",
 	mpriprty."ctime" AS "price.property.type.ctime", mpriprty."pos" AS "price.property.type.position"
 FROM "mshop_price_property_type" mpriprty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/price/manager/property/type/standard/search/ansi

## type/standard/update/ansi

Updates an existing price property type record in the database

```
mshop/price/manager/property/type/standard/update/ansi = 
 UPDATE "mshop_price_property_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/price/manager/property/type/standard/update
* Type: string - SQL statement for updating records
* Since: 2018.01

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the price type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/property/type/standard/insert/ansi
* mshop/price/manager/property/type/standard/newid/ansi
* mshop/price/manager/property/type/standard/delete/ansi
* mshop/price/manager/property/type/standard/search/ansi
* mshop/price/manager/property/type/standard/count/ansi

## type/standard/update/mysql

Updates an existing price property type record in the database

```
mshop/price/manager/property/type/standard/update/mysql = 
 UPDATE "mshop_price_property_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_price_property_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/price/manager/property/type/standard/update/ansi

## type/submanagers

List of manager names that can be instantiated by the price property type manager

```
mshop/price/manager/property/type/submanagers = Array
(
)
```

* Default: Array
* Type: array - List of sub-manager names
* Since: 2018.01

Managers provide a generic interface to the underlying storage.
Each manager has or can have sub-managers caring about particular
aspects. Each of these sub-managers can be instantiated by its
parent manager using the getSubManager() method.

The search keys from sub-managers can be normally used in the
manager as well. It allows you to search for items of the manager
using the search keys of the sub-managers to further limit the
retrieved list of items.


# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/price/manager/sitemode = 3
```

* Default: 3
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole price domain if items from parent sites are inherited,
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
mshop/price/manager/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mpri."id"
 	FROM "mshop_price" AS mpri
 	:joins
 	WHERE :cond
 	GROUP BY mpri."id"
 	ORDER BY mpri."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/price/manager/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the price
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

* mshop/price/manager/standard/insert/ansi
* mshop/price/manager/standard/update/ansi
* mshop/price/manager/standard/newid/ansi
* mshop/price/manager/standard/delete/ansi
* mshop/price/manager/standard/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/price/manager/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mpri."id"
 	FROM "mshop_price" AS mpri
 	:joins
 	WHERE :cond
 	GROUP BY mpri."id"
 	ORDER BY mpri."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mpri."id"
 	FROM "mshop_price" AS mpri
 	:joins
 	WHERE :cond
 	GROUP BY mpri."id"
 	ORDER BY mpri."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/price/manager/standard/count/ansi

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/price/manager/standard/delete/ansi = 
 DELETE FROM "mshop_price"
 WHERE :cond AND siteid = ?
```

* Default: mshop/price/manager/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the price database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/standard/insert/ansi
* mshop/price/manager/standard/update/ansi
* mshop/price/manager/standard/newid/ansi
* mshop/price/manager/standard/search/ansi
* mshop/price/manager/standard/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/price/manager/standard/delete/mysql = 
 DELETE FROM "mshop_price"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_price"
 WHERE :cond AND siteid = ?


See also:

* mshop/price/manager/standard/delete/ansi

## insert/ansi

Inserts a new price record into the database table

```
mshop/price/manager/standard/insert/ansi = 
 INSERT INTO "mshop_price" ( :names
 	"type", "currencyid", "domain", "label",
 	"quantity", "value", "costs", "rebate", "taxrate",
 	"status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/price/manager/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the price item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/standard/update/ansi
* mshop/price/manager/standard/newid/ansi
* mshop/price/manager/standard/delete/ansi
* mshop/price/manager/standard/search/ansi
* mshop/price/manager/standard/count/ansi

## insert/mysql

Inserts a new price record into the database table

```
mshop/price/manager/standard/insert/mysql = 
 INSERT INTO "mshop_price" ( :names
 	"type", "currencyid", "domain", "label",
 	"quantity", "value", "costs", "rebate", "taxrate",
 	"status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_price" ( :names
 	"type", "currencyid", "domain", "label",
 	"quantity", "value", "costs", "rebate", "taxrate",
 	"status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/price/manager/standard/insert/ansi

## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/price/manager/standard/newid/ansi = mshop/price/manager/standard/newid
```

* Default: mshop/price/manager/standard/newid
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
 SELECT currval('seq_mpri_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mpri_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/price/manager/standard/insert/ansi
* mshop/price/manager/standard/update/ansi
* mshop/price/manager/standard/delete/ansi
* mshop/price/manager/standard/search/ansi
* mshop/price/manager/standard/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/price/manager/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/price/manager/standard/newid

See also:

* mshop/price/manager/standard/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/price/manager/standard/search/ansi = 
 SELECT :columns
 	mpri."id" AS "price.id", mpri."siteid" AS "price.siteid",
 	mpri."type" AS "price.type", mpri."currencyid" AS "price.currencyid",
 	mpri."domain" AS "price.domain", mpri."label" AS "price.label",
 	mpri."quantity" AS "price.quantity", mpri."value" AS "price.value",
 	mpri."costs" AS "price.costs", mpri."rebate" AS "price.rebate",
 	mpri."taxrate" AS "price.taxrates", mpri."status" AS "price.status",
 	mpri."mtime" AS "price.mtime", mpri."editor" AS "price.editor",
 	mpri."ctime" AS "price.ctime"
 FROM "mshop_price" AS mpri
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mpri."id", mpri."siteid", mpri."type", mpri."currencyid", mpri."domain", mpri."label",
 	mpri."quantity", mpri."value", mpri."costs", mpri."rebate", mpri."taxrate", mpri."status",
 	mpri."mtime", mpri."editor", mpri."ctime"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/price/manager/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the price
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

* mshop/price/manager/standard/insert/ansi
* mshop/price/manager/standard/update/ansi
* mshop/price/manager/standard/newid/ansi
* mshop/price/manager/standard/delete/ansi
* mshop/price/manager/standard/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/price/manager/standard/search/mysql = 
 SELECT :columns
 	mpri."id" AS "price.id", mpri."siteid" AS "price.siteid",
 	mpri."type" AS "price.type", mpri."currencyid" AS "price.currencyid",
 	mpri."domain" AS "price.domain", mpri."label" AS "price.label",
 	mpri."quantity" AS "price.quantity", mpri."value" AS "price.value",
 	mpri."costs" AS "price.costs", mpri."rebate" AS "price.rebate",
 	mpri."taxrate" AS "price.taxrates", mpri."status" AS "price.status",
 	mpri."mtime" AS "price.mtime", mpri."editor" AS "price.editor",
 	mpri."ctime" AS "price.ctime"
 FROM "mshop_price" AS mpri
 :joins
 WHERE :cond
 GROUP BY :group mpri."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mpri."id" AS "price.id", mpri."siteid" AS "price.siteid",
 	mpri."type" AS "price.type", mpri."currencyid" AS "price.currencyid",
 	mpri."domain" AS "price.domain", mpri."label" AS "price.label",
 	mpri."quantity" AS "price.quantity", mpri."value" AS "price.value",
 	mpri."costs" AS "price.costs", mpri."rebate" AS "price.rebate",
 	mpri."taxrate" AS "price.taxrates", mpri."status" AS "price.status",
 	mpri."mtime" AS "price.mtime", mpri."editor" AS "price.editor",
 	mpri."ctime" AS "price.ctime"
 FROM "mshop_price" AS mpri
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mpri."id", mpri."siteid", mpri."type", mpri."currencyid", mpri."domain", mpri."label",
 	mpri."quantity", mpri."value", mpri."costs", mpri."rebate", mpri."taxrate", mpri."status",
 	mpri."mtime", mpri."editor", mpri."ctime"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/price/manager/standard/search/ansi

## update/ansi

Updates an existing price record in the database

```
mshop/price/manager/standard/update/ansi = 
 UPDATE "mshop_price"
 SET :names
 	"type" = ?, "currencyid" = ?, "domain" = ?, "label" = ?,
 	"quantity" = ?, "value" = ?, "costs" = ?, "rebate" = ?,
 	"taxrate" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/price/manager/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the price item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/standard/insert/ansi
* mshop/price/manager/standard/newid/ansi
* mshop/price/manager/standard/delete/ansi
* mshop/price/manager/standard/search/ansi
* mshop/price/manager/standard/count/ansi

## update/mysql

Updates an existing price record in the database

```
mshop/price/manager/standard/update/mysql = 
 UPDATE "mshop_price"
 SET :names
 	"type" = ?, "currencyid" = ?, "domain" = ?, "label" = ?,
 	"quantity" = ?, "value" = ?, "costs" = ?, "rebate" = ?,
 	"taxrate" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_price"
 SET :names
 	"type" = ?, "currencyid" = ?, "domain" = ?, "label" = ?,
 	"quantity" = ?, "value" = ?, "costs" = ?, "rebate" = ?,
 	"taxrate" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/price/manager/standard/update/ansi

# submanagers

List of manager names that can be instantiated by the price manager

```
mshop/price/manager/submanagers = Array
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

Excludes decorators added by the "common" option from the price type manager

```
mshop/price/manager/type/decorators/excludes = Array
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
around the price type manager.

```
 mshop/price/manager/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the price type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/type/decorators/global
* mshop/price/manager/type/decorators/local

## decorators/global

Adds a list of globally available decorators only to the price type manager

```
mshop/price/manager/type/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the price type
manager.

```
 mshop/price/manager/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the price
type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/type/decorators/excludes
* mshop/price/manager/type/decorators/local

## decorators/local

Adds a list of local decorators only to the price type manager

```
mshop/price/manager/type/decorators/local = Array
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
("\Aimeos\MShop\Price\Manager\Type\Decorator\*") around the price type
manager.

```
 mshop/price/manager/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Price\Manager\Type\Decorator\Decorator2" only to the
price type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/price/manager/type/decorators/excludes
* mshop/price/manager/type/decorators/global

## name

Class name of the used price type manager implementation

```
mshop/price/manager/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default price type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Price\Manager\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Price\Manager\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/price/manager/type/name = Mytype
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
mshop/price/manager/type/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mprity."id"
 	FROM "mshop_price_type" AS mprity
 	:joins
 	WHERE :cond
 	ORDER BY mprity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/price/manager/type/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the price
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

* mshop/price/manager/type/standard/insert/ansi
* mshop/price/manager/type/standard/update/ansi
* mshop/price/manager/type/standard/newid/ansi
* mshop/price/manager/type/standard/delete/ansi
* mshop/price/manager/type/standard/search/ansi

## standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/price/manager/type/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mprity."id"
 	FROM "mshop_price_type" AS mprity
 	:joins
 	WHERE :cond
 	ORDER BY mprity."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mprity."id"
 	FROM "mshop_price_type" AS mprity
 	:joins
 	WHERE :cond
 	ORDER BY mprity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/price/manager/type/standard/count/ansi

## standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/price/manager/type/standard/delete/ansi = 
 DELETE FROM "mshop_price_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/price/manager/type/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the price database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/type/standard/insert/ansi
* mshop/price/manager/type/standard/update/ansi
* mshop/price/manager/type/standard/newid/ansi
* mshop/price/manager/type/standard/search/ansi
* mshop/price/manager/type/standard/count/ansi

## standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/price/manager/type/standard/delete/mysql = 
 DELETE FROM "mshop_price_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_price_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/price/manager/type/standard/delete/ansi

## standard/insert/ansi

Inserts a new price type record into the database table

```
mshop/price/manager/type/standard/insert/ansi = 
 INSERT INTO "mshop_price_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/price/manager/type/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the price type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/type/standard/update/ansi
* mshop/price/manager/type/standard/newid/ansi
* mshop/price/manager/type/standard/delete/ansi
* mshop/price/manager/type/standard/search/ansi
* mshop/price/manager/type/standard/count/ansi

## standard/insert/mysql

Inserts a new price type record into the database table

```
mshop/price/manager/type/standard/insert/mysql = 
 INSERT INTO "mshop_price_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_price_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/price/manager/type/standard/insert/ansi

## standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/price/manager/type/standard/newid/ansi = mshop/price/manager/type/standard/newid
```

* Default: mshop/price/manager/type/standard/newid
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
 SELECT currval('seq_mprity_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mprity_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/price/manager/type/standard/insert/ansi
* mshop/price/manager/type/standard/update/ansi
* mshop/price/manager/type/standard/delete/ansi
* mshop/price/manager/type/standard/search/ansi
* mshop/price/manager/type/standard/count/ansi

## standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/price/manager/type/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/price/manager/type/standard/newid

See also:

* mshop/price/manager/type/standard/newid/ansi

## standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/price/manager/type/standard/search/ansi = 
 SELECT :columns
 	mprity."id" AS "price.type.id", mprity."siteid" AS "price.type.siteid",
 	mprity."code" AS "price.type.code", mprity."domain" AS "price.type.domain",
 	mprity."label" AS "price.type.label", mprity."status" AS "price.type.status",
 	mprity."mtime" AS "price.type.mtime", mprity."editor" AS "price.type.editor",
 	mprity."ctime" AS "price.type.ctime", mprity."pos" AS "price.type.position"
 FROM "mshop_price_type" AS mprity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/price/manager/type/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the price
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

* mshop/price/manager/type/standard/insert/ansi
* mshop/price/manager/type/standard/update/ansi
* mshop/price/manager/type/standard/newid/ansi
* mshop/price/manager/type/standard/delete/ansi
* mshop/price/manager/type/standard/count/ansi

## standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/price/manager/type/standard/search/mysql = 
 SELECT :columns
 	mprity."id" AS "price.type.id", mprity."siteid" AS "price.type.siteid",
 	mprity."code" AS "price.type.code", mprity."domain" AS "price.type.domain",
 	mprity."label" AS "price.type.label", mprity."status" AS "price.type.status",
 	mprity."mtime" AS "price.type.mtime", mprity."editor" AS "price.type.editor",
 	mprity."ctime" AS "price.type.ctime", mprity."pos" AS "price.type.position"
 FROM "mshop_price_type" AS mprity
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mprity."id" AS "price.type.id", mprity."siteid" AS "price.type.siteid",
 	mprity."code" AS "price.type.code", mprity."domain" AS "price.type.domain",
 	mprity."label" AS "price.type.label", mprity."status" AS "price.type.status",
 	mprity."mtime" AS "price.type.mtime", mprity."editor" AS "price.type.editor",
 	mprity."ctime" AS "price.type.ctime", mprity."pos" AS "price.type.position"
 FROM "mshop_price_type" AS mprity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/price/manager/type/standard/search/ansi

## standard/update/ansi

Updates an existing price type record in the database

```
mshop/price/manager/type/standard/update/ansi = 
 UPDATE "mshop_price_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/price/manager/type/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the price type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/price/manager/type/standard/insert/ansi
* mshop/price/manager/type/standard/newid/ansi
* mshop/price/manager/type/standard/delete/ansi
* mshop/price/manager/type/standard/search/ansi
* mshop/price/manager/type/standard/count/ansi

## standard/update/mysql

Updates an existing price type record in the database

```
mshop/price/manager/type/standard/update/mysql = 
 UPDATE "mshop_price_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_price_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/price/manager/type/standard/update/ansi

## submanagers

List of manager names that can be instantiated by the price type manager

```
mshop/price/manager/type/submanagers = Array
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
