
# code
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/coupon/manager/code/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcouco."id"
 	FROM "mshop_coupon_code" mcouco
 	:joins
 	WHERE :cond
 	ORDER BY mcouco."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the coupon
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

* mshop/coupon/manager/code/insert/ansi
* mshop/coupon/manager/code/update/ansi
* mshop/coupon/manager/code/newid/ansi
* mshop/coupon/manager/code/delete/ansi
* mshop/coupon/manager/code/search/ansi
* mshop/coupon/manager/code/counter/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/coupon/manager/code/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcouco."id"
 	FROM "mshop_coupon_code" mcouco
 	:joins
 	WHERE :cond
 	ORDER BY mcouco."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
```

 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcouco."id"
 	FROM "mshop_coupon_code" mcouco
 	:joins
 	WHERE :cond
 	ORDER BY mcouco."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

See also:

* mshop/coupon/manager/code/count/ansi

## counter/ansi

Increases or decreases the counter of the coupon code record matched by the given code

```
mshop/coupon/manager/code/counter/ansi = 
 UPDATE "mshop_coupon_code"
 SET	"count" = "count" + ?, "mtime" = ?, "editor" = ?
 WHERE :cond AND "code" = ?
```

* Type: string - SQL statement for increasing/decreasing the coupon code count
* Since: 2014.03

A counter is associated to each coupon code and it's decreased
each time by one if a code used in an paid order was redeemed
successfully. Shop owners can also use the coupon code counter to
use the same code more often by setting it to an arbitrary value.
In this case, the code can be redeemed until the counter reaches
zero.

The coupon codes must be from one of the sites that are configured
via the context item. If the current site is part of a tree of
sites, the statement can increase or decrease codes from the
current site and all parent sites if the code is inherited by one
of the parent sites.

Each time the code is updated, the modify date/time is set to
the current timestamp and the editor field is updated.

See also:

* mshop/coupon/manager/code/insert/ansi
* mshop/coupon/manager/code/update/ansi
* mshop/coupon/manager/code/newid/ansi
* mshop/coupon/manager/code/delete/ansi
* mshop/coupon/manager/code/search/ansi
* mshop/coupon/manager/code/count/ansi

## counter/mysql

Increases or decreases the counter of the coupon code record matched by the given code

```
mshop/coupon/manager/code/counter/mysql = 
 UPDATE "mshop_coupon_code"
 SET	"count" = "count" + ?, "mtime" = ?, "editor" = ?
 WHERE :cond AND "code" = ?
```

* Default: 
```

 UPDATE "mshop_coupon_code"
 SET	"count" = "count" + ?, "mtime" = ?, "editor" = ?
 WHERE :cond AND "code" = ?
```

See also:

* mshop/coupon/manager/code/counter/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the coupon code manager

```
mshop/coupon/manager/code/decorators/excludes = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - Address of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the coupon code manager.

```
 mshop/coupon/manager/code/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the coupon code manager.

See also:

* mshop/common/manager/decorators/default
* mshop/coupon/manager/code/decorators/global
* mshop/coupon/manager/code/decorators/local

## decorators/global

Adds a list of globally available decorators only to the coupon code manager

```
mshop/coupon/manager/code/decorators/global = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - Address of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the coupon code manager.

```
 mshop/coupon/manager/code/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the coupon
code manager.

See also:

* mshop/common/manager/decorators/default
* mshop/coupon/manager/code/decorators/excludes
* mshop/coupon/manager/code/decorators/local

## decorators/local

Adds a list of local decorators only to the coupon code manager

```
mshop/coupon/manager/code/decorators/local = Array
(
)
```

* Default: 
```
Array
(
)
```
* Type: array - Address of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Coupon\Manager\Code\Decorator\*") around the coupon code
manager.

```
 mshop/coupon/manager/code/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Coupon\Manager\Code\Decorator\Decorator2" only to the
coupon code manager.

See also:

* mshop/common/manager/decorators/default
* mshop/coupon/manager/code/decorators/excludes
* mshop/coupon/manager/code/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/coupon/manager/code/delete/ansi = 
 DELETE FROM "mshop_coupon_code"
 WHERE :cond AND "siteid" LIKE ?
```

* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the coupon database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/coupon/manager/code/insert/ansi
* mshop/coupon/manager/code/update/ansi
* mshop/coupon/manager/code/newid/ansi
* mshop/coupon/manager/code/search/ansi
* mshop/coupon/manager/code/count/ansi
* mshop/coupon/manager/code/counter/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/coupon/manager/code/delete/mysql = 
 DELETE FROM "mshop_coupon_code"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: 
```

 DELETE FROM "mshop_coupon_code"
 WHERE :cond AND "siteid" LIKE ?
```

See also:

* mshop/coupon/manager/code/delete/ansi

## insert/ansi

Inserts a new coupon code record into the database table

```
mshop/coupon/manager/code/insert/ansi = 
 INSERT INTO "mshop_coupon_code" ( :names
 	"parentid", "code", "start", "end", "count", "ref",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the coupon item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/coupon/manager/code/update/ansi
* mshop/coupon/manager/code/newid/ansi
* mshop/coupon/manager/code/delete/ansi
* mshop/coupon/manager/code/search/ansi
* mshop/coupon/manager/code/count/ansi
* mshop/coupon/manager/code/counter/ansi

## insert/mysql

Inserts a new coupon code record into the database table

```
mshop/coupon/manager/code/insert/mysql = 
 INSERT INTO "mshop_coupon_code" ( :names
 	"parentid", "code", "start", "end", "count", "ref",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
```

 INSERT INTO "mshop_coupon_code" ( :names
 	"parentid", "code", "start", "end", "count", "ref",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

See also:

* mshop/coupon/manager/code/insert/ansi

## name

Class name of the used coupon code manager implementation

```
mshop/coupon/manager/code/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2014.03

Each default coupon code manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Coupon\Manager\Address\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Coupon\Manager\Address\Mycode
```

then you have to set the this configuration option:

```
 mshop/coupon/manager/code/name = Mycode
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyAddress"!


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/coupon/manager/code/newid/ansi = 
```

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
 SELECT currval('seq_mcouco_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mcouco_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/coupon/manager/code/insert/ansi
* mshop/coupon/manager/code/update/ansi
* mshop/coupon/manager/code/delete/ansi
* mshop/coupon/manager/code/search/ansi
* mshop/coupon/manager/code/count/ansi
* mshop/coupon/manager/code/counter/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/coupon/manager/code/newid/mysql = SELECT LAST_INSERT_ID()
```


See also:

* mshop/coupon/manager/code/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/coupon/manager/code/search/ansi = 
 SELECT :columns
 FROM "mshop_coupon_code" mcouco
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the coupon
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
replaces the ":order" placeholder. Columns of
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

* mshop/coupon/manager/code/insert/ansi
* mshop/coupon/manager/code/update/ansi
* mshop/coupon/manager/code/newid/ansi
* mshop/coupon/manager/code/delete/ansi
* mshop/coupon/manager/code/count/ansi
* mshop/coupon/manager/code/counter/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/coupon/manager/code/search/mysql = 
 SELECT :columns
 FROM "mshop_coupon_code" mcouco
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
```

 SELECT :columns
 FROM "mshop_coupon_code" mcouco
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

See also:

* mshop/coupon/manager/code/search/ansi

## submanagers

List of manager names that can be instantiated by the coupon code manager

```
mshop/coupon/manager/code/submanagers = Array
(
)
```

* Default: 
```
Array
(
)
```
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


## update/ansi

Updates an existing coupon code record in the database

```
mshop/coupon/manager/code/update/ansi = 
 UPDATE "mshop_coupon_code"
 SET :names
 	"parentid" = ?, "code" = ?, "start" = ?, "end" = ?,
 	"count" = ?, "ref" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the coupon item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/coupon/manager/code/insert/ansi
* mshop/coupon/manager/code/newid/ansi
* mshop/coupon/manager/code/delete/ansi
* mshop/coupon/manager/code/search/ansi
* mshop/coupon/manager/code/count/ansi
* mshop/coupon/manager/code/counter/ansi

## update/mysql

Updates an existing coupon code record in the database

```
mshop/coupon/manager/code/update/mysql = 
 UPDATE "mshop_coupon_code"
 SET :names
 	"parentid" = ?, "code" = ?, "start" = ?, "end" = ?,
 	"count" = ?, "ref" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: 
```

 UPDATE "mshop_coupon_code"
 SET :names
 	"parentid" = ?, "code" = ?, "start" = ?, "end" = ?,
 	"count" = ?, "ref" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

See also:

* mshop/coupon/manager/code/update/ansi

# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/coupon/manager/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcou."id"
 	FROM "mshop_coupon" mcou
 	:joins
 	WHERE :cond
 	GROUP BY mcou."id"
 	ORDER BY mcou."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the coupon
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

* mshop/coupon/manager/insert/ansi
* mshop/coupon/manager/update/ansi
* mshop/coupon/manager/newid/ansi
* mshop/coupon/manager/delete/ansi
* mshop/coupon/manager/search/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/coupon/manager/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcou."id"
 	FROM "mshop_coupon" mcou
 	:joins
 	WHERE :cond
 	GROUP BY mcou."id"
 	ORDER BY mcou."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
```

 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mcou."id"
 	FROM "mshop_coupon" mcou
 	:joins
 	WHERE :cond
 	GROUP BY mcou."id"
 	ORDER BY mcou."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

See also:

* mshop/coupon/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the coupon manager

```
mshop/coupon/manager/decorators/excludes = Array
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
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the coupon manager.

```
 mshop/coupon/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the coupon manager.

See also:

* mshop/common/manager/decorators/default
* mshop/coupon/manager/decorators/global
* mshop/coupon/manager/decorators/local

## global

Adds a list of globally available decorators only to the coupon manager

```
mshop/coupon/manager/decorators/global = Array
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
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the coupon code manager.

```
 mshop/coupon/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the coupon
code manager.

See also:

* mshop/common/manager/decorators/default
* mshop/coupon/manager/decorators/excludes
* mshop/coupon/manager/decorators/local

## local

Adds a list of local decorators only to the coupon manager

```
mshop/coupon/manager/decorators/local = Array
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
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Coupon\Manager\Decorator\*") around the coupon manager.

```
 mshop/coupon/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Coupon\Manager\Decorator\Decorator2" only to the coupon
code manager.

See also:

* mshop/common/manager/decorators/default
* mshop/coupon/manager/decorators/excludes
* mshop/coupon/manager/decorators/global

# delete
## ansi

Deletes the items matched by the given IDs from the database

```
mshop/coupon/manager/delete/ansi = 
 DELETE FROM "mshop_coupon"
 WHERE :cond AND "siteid" LIKE ?
```

* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the coupon database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/coupon/manager/insert/ansi
* mshop/coupon/manager/update/ansi
* mshop/coupon/manager/newid/ansi
* mshop/coupon/manager/search/ansi
* mshop/coupon/manager/count/ansi

## mysql

Deletes the items matched by the given IDs from the database

```
mshop/coupon/manager/delete/mysql = 
 DELETE FROM "mshop_coupon"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: 
```

 DELETE FROM "mshop_coupon"
 WHERE :cond AND "siteid" LIKE ?
```

See also:

* mshop/coupon/manager/delete/ansi

# insert
## ansi

Inserts a new coupon record into the database table

```
mshop/coupon/manager/insert/ansi = 
 INSERT INTO "mshop_coupon" ( :names
 	"label", "provider", "config", "start", "end",
 	"status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the coupon item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/coupon/manager/update/ansi
* mshop/coupon/manager/newid/ansi
* mshop/coupon/manager/delete/ansi
* mshop/coupon/manager/search/ansi
* mshop/coupon/manager/count/ansi

## mysql

Inserts a new coupon record into the database table

```
mshop/coupon/manager/insert/mysql = 
 INSERT INTO "mshop_coupon" ( :names
 	"label", "provider", "config", "start", "end",
 	"status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
```

 INSERT INTO "mshop_coupon" ( :names
 	"label", "provider", "config", "start", "end",
 	"status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

See also:

* mshop/coupon/manager/insert/ansi

# name

Class name of the used coupon manager implementation

```
mshop/coupon/manager/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2014.03

Each default manager can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Coupon\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Coupon\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/coupon/manager/name = Mymanager
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
mshop/coupon/manager/newid/ansi = 
```

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
 SELECT currval('seq_mcou_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mcou_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/coupon/manager/insert/ansi
* mshop/coupon/manager/update/ansi
* mshop/coupon/manager/delete/ansi
* mshop/coupon/manager/search/ansi
* mshop/coupon/manager/count/ansi

## mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/coupon/manager/newid/mysql = SELECT LAST_INSERT_ID()
```


See also:

* mshop/coupon/manager/newid/ansi

# resource

Name of the database connection resource to use

```
mshop/coupon/manager/resource = db-coupon
```

* Default: `db-coupon`
* Type: string - Database connection name
* Since: 2023.04
* Since: 2023.04

You can configure a different database connection for each data domain
and if no such connection name exists, the "db" connection will be used.
It's also possible to use the same database connection for different
data domains by configuring the same connection name using this setting.


# search
## ansi

Retrieves the records matched by the given criteria in the database

```
mshop/coupon/manager/search/ansi = 
 SELECT :columns
 FROM "mshop_coupon" mcou
 :joins
 WHERE :cond
 GROUP BY :group
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the coupon
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
replaces the ":order" placeholder. Columns of
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

* mshop/coupon/manager/insert/ansi
* mshop/coupon/manager/update/ansi
* mshop/coupon/manager/newid/ansi
* mshop/coupon/manager/delete/ansi
* mshop/coupon/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/coupon/manager/search/mysql = 
 SELECT :columns
 FROM "mshop_coupon" mcou
 :joins
 WHERE :cond
 GROUP BY mcou."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
```

 SELECT :columns
 FROM "mshop_coupon" mcou
 :joins
 WHERE :cond
 GROUP BY :group
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

See also:

* mshop/coupon/manager/search/ansi

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/coupon/manager/sitemode = 1
```

* Default: `1`
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole coupon domain if items from parent sites are inherited,
sites from child sites are aggregated or both.

Available constants for the site mode are:
* 0 = only items from the current site
* 1 = inherit items from parent sites
* 2 = aggregate items from child sites
* 3 = inherit and aggregate items at the same time

You also need to set the mode in the locale manager
(mshop/locale/manager/sitelevel) to one of the constants.
If you set it to the same value, it will work as described but you
can also use different modes. For example, if inheritance and
aggregation is configured the locale manager but only inheritance
in the domain manager because aggregating items makes no sense in
this domain, then items wil be only inherited. Thus, you have full
control over inheritance and aggregation in each domain.

See also:

* mshop/locale/manager/sitelevel

# submanagers

List of manager names that can be instantiated by the coupon manager

```
mshop/coupon/manager/submanagers = Array
(
    [0] => code
)
```

* Default: 
```
Array
(
    [0] => code
)
```
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

Updates an existing coupon record in the database

```
mshop/coupon/manager/update/ansi = 
 UPDATE "mshop_coupon"
 SET :names
 	"label" = ?, "provider" = ?, "config" = ?, "start" = ?,
 	"end" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the coupon item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/coupon/manager/insert/ansi
* mshop/coupon/manager/newid/ansi
* mshop/coupon/manager/delete/ansi
* mshop/coupon/manager/search/ansi
* mshop/coupon/manager/count/ansi

## mysql

Updates an existing coupon record in the database

```
mshop/coupon/manager/update/mysql = 
 UPDATE "mshop_coupon"
 SET :names
 	"label" = ?, "provider" = ?, "config" = ?, "start" = ?,
 	"end" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: 
```

 UPDATE "mshop_coupon"
 SET :names
 	"label" = ?, "provider" = ?, "config" = ?, "start" = ?,
 	"end" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

See also:

* mshop/coupon/manager/update/ansi