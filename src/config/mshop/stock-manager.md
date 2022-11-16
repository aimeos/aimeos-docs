
# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/stock/manager/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msto."id"
 	FROM "mshop_stock" msto
 	:joins
 	WHERE :cond
 	ORDER BY msto."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/stock/manager/count
* Type: string - SQL statement for counting items
* Since: 2017.01

Counts all records matched by the given criteria from the product
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

* mshop/stock/manager/insert/ansi
* mshop/stock/manager/update/ansi
* mshop/stock/manager/newid/ansi
* mshop/stock/manager/delete/ansi
* mshop/stock/manager/search/ansi
* mshop/stock/manager/stocklevel

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/stock/manager/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msto."id"
 	FROM "mshop_stock" msto
 	:joins
 	WHERE :cond
 	ORDER BY msto."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT msto."id"
 	FROM "mshop_stock" msto
 	:joins
 	WHERE :cond
 	ORDER BY msto."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/stock/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the product stock manager

```
mshop/stock/manager/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.01
* Since: 2017.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the product stock manager.

```
 mshop/stock/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the product stock manager.

See also:

* mshop/common/manager/decorators/default
* mshop/stock/manager/decorators/global
* mshop/stock/manager/decorators/local
* mshop/common/manager/decorators/default
* mshop/stock/manager/decorators/global
* mshop/stock/manager/decorators/local

## global

Adds a list of globally available decorators only to the product stock manager

```
mshop/stock/manager/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.01
* Since: 2017.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the product stock manager.

```
 mshop/stock/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the product controller.

See also:

* mshop/common/manager/decorators/default
* mshop/stock/manager/decorators/excludes
* mshop/stock/manager/decorators/local
* mshop/common/manager/decorators/default
* mshop/stock/manager/decorators/excludes
* mshop/stock/manager/decorators/local

## local

Adds a list of local decorators only to the product stock manager

```
mshop/stock/manager/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.01
* Since: 2017.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the product stock manager.

```
 mshop/stock/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator2" only to the product
controller.

See also:

* mshop/common/manager/decorators/default
* mshop/stock/manager/decorators/excludes
* mshop/stock/manager/decorators/global
* mshop/common/manager/decorators/default
* mshop/stock/manager/decorators/excludes
* mshop/stock/manager/decorators/global

# delete
## ansi

Deletes the items matched by the given IDs from the database

```
mshop/stock/manager/delete/ansi = 
 DELETE FROM "mshop_stock"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: mshop/stock/manager/delete
* Type: string - SQL statement for deleting items
* Since: 2017.01

Removes the records specified by the given IDs from the product database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/stock/manager/insert/ansi
* mshop/stock/manager/update/ansi
* mshop/stock/manager/newid/ansi
* mshop/stock/manager/search/ansi
* mshop/stock/manager/count/ansi
* mshop/stock/manager/stocklevel

## mysql

Deletes the items matched by the given IDs from the database

```
mshop/stock/manager/delete/mysql = 
 DELETE FROM "mshop_stock"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: 
 DELETE FROM "mshop_stock"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/stock/manager/delete/ansi

# insert
## ansi

Inserts a new product stock record into the database table

```
mshop/stock/manager/insert/ansi = 
 INSERT INTO "mshop_stock" ( :names
 	"prodid", "type", "stocklevel", "backdate",
 	"timeframe", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/stock/manager/insert
* Type: string - SQL statement for inserting records
* Since: 2017.01

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the product stock item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/stock/manager/update/ansi
* mshop/stock/manager/newid/ansi
* mshop/stock/manager/delete/ansi
* mshop/stock/manager/search/ansi
* mshop/stock/manager/count/ansi
* mshop/stock/manager/stocklevel

## mysql

Inserts a new product stock record into the database table

```
mshop/stock/manager/insert/mysql = 
 INSERT INTO "mshop_stock" ( :names
 	"prodid", "type", "stocklevel", "backdate",
 	"timeframe", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_stock" ( :names
 	"prodid", "type", "stocklevel", "backdate",
 	"timeframe", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/stock/manager/insert/ansi

# name

Class name of the used product stock manager implementation

```
mshop/stock/manager/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.01
* Since: 2017.01

Each default product stock manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Stock\Manager\Stock\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Stock\Manager\Stock\Mystock
```

then you have to set the this configuration option:

```
 mshop/stock/manager/name = Mystock
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyStock"!


# newid
## ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/stock/manager/newid/ansi = mshop/stock/manager/newid
```

* Default: mshop/stock/manager/newid
* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2017.01

As soon as a new record is inserted into the database table,
the database server generates a new and unique identifier for
that record. This ID can be used for retrieving, updating and
deleting that specific record from the table again.

For MySQL:
```
 SELECT LAST_INSERT_ID()
For PostgreSQL:
 SELECT currval('seq_msto_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_msto_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/stock/manager/insert/ansi
* mshop/stock/manager/update/ansi
* mshop/stock/manager/delete/ansi
* mshop/stock/manager/search/ansi
* mshop/stock/manager/count/ansi
* mshop/stock/manager/stocklevel

## mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/stock/manager/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/stock/manager/newid

See also:

* mshop/stock/manager/newid/ansi

# search
## ansi

Retrieves the records matched by the given criteria in the database

```
mshop/stock/manager/search/ansi = 
 SELECT :columns
 	msto."id" AS "stock.id", msto."prodid" AS "stock.productid",
 	msto."siteid" AS "stock.siteid", msto."type" AS "stock.type",
 	msto."stocklevel" AS "stock.stocklevel", msto."backdate" AS "stock.backdate",
 	msto."timeframe" AS "stock.timeframe", msto."mtime" AS "stock.mtime",
 	msto."ctime" AS "stock.ctime", msto."editor" AS "stock.editor"
 FROM "mshop_stock" msto
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/stock/manager/search
* Type: string - SQL statement for searching items
* Since: 2017.01

Fetches the records matched by the given criteria from the product
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

* mshop/stock/manager/insert/ansi
* mshop/stock/manager/update/ansi
* mshop/stock/manager/newid/ansi
* mshop/stock/manager/delete/ansi
* mshop/stock/manager/count/ansi
* mshop/stock/manager/stocklevel

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/stock/manager/search/mysql = 
 SELECT :columns
 	msto."id" AS "stock.id", msto."prodid" AS "stock.productid",
 	msto."siteid" AS "stock.siteid", msto."type" AS "stock.type",
 	msto."stocklevel" AS "stock.stocklevel", msto."backdate" AS "stock.backdate",
 	msto."timeframe" AS "stock.timeframe", msto."mtime" AS "stock.mtime",
 	msto."ctime" AS "stock.ctime", msto."editor" AS "stock.editor"
 FROM "mshop_stock" msto
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	msto."id" AS "stock.id", msto."prodid" AS "stock.productid",
 	msto."siteid" AS "stock.siteid", msto."type" AS "stock.type",
 	msto."stocklevel" AS "stock.stocklevel", msto."backdate" AS "stock.backdate",
 	msto."timeframe" AS "stock.timeframe", msto."mtime" AS "stock.mtime",
 	msto."ctime" AS "stock.ctime", msto."editor" AS "stock.editor"
 FROM "mshop_stock" msto
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/stock/manager/search/ansi

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/stock/manager/sitemode = 3
```

* Default: 3
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole stock domain if items from parent sites are inherited,
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

# stocklevel
## ansi

Increases or decreases the stock level for the given product and type code

```
mshop/stock/manager/stocklevel/ansi = 
 UPDATE "mshop_stock"
 SET "stocklevel" = "stocklevel" - ?, "mtime" = ?, "editor" = ?
 WHERE "prodid" = ? AND "type" = ? AND :cond
```

* Default: mshop/stock/manager/stocklevel
* Type: string - SQL statement for increasing/decreasing the stock level
* Since: 2017.01

The stock level is decreased for the ordered products each time
an order is placed by a customer successfully. Also, updates
from external sources like ERP systems can increase the stock
level of a product if no absolute values are set via save()
instead.

The stock level must be from one of the sites that are configured
via the context item. If the current site is part of a tree of
sites, the statement can increase or decrease stock levels from
the current site and all parent sites if the stock level is
inherited by one of the parent sites.

Each time the stock level is updated, the modify date/time is
set to the current timestamp and the editor field is updated.

See also:

* mshop/stock/manager/insert/ansi
* mshop/stock/manager/update/ansi
* mshop/stock/manager/newid/ansi
* mshop/stock/manager/delete/ansi
* mshop/stock/manager/search/ansi
* mshop/stock/manager/count/ansi

## mysql

Increases or decreases the stock level for the given product and type code

```
mshop/stock/manager/stocklevel/mysql = 
 UPDATE "mshop_stock"
 SET "stocklevel" = "stocklevel" - ?, "mtime" = ?, "editor" = ?
 WHERE "prodid" = ? AND "type" = ? AND :cond
```

* Default: 
 UPDATE "mshop_stock"
 SET "stocklevel" = "stocklevel" - ?, "mtime" = ?, "editor" = ?
 WHERE "prodid" = ? AND "type" = ? AND :cond


See also:

* mshop/stock/manager/stocklevel/ansi

# submanagers

List of manager names that can be instantiated by the product stock manager

```
mshop/stock/manager/submanagers = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-manager names
* Since: 2017.01

Managers provide a generic interface to the underlying storage.
Each manager has or can have sub-managers caring about particular
aspects. Each of these sub-managers can be instantiated by its
parent manager using the getSubManager() method.

The search keys from sub-managers can be normally used in the
manager as well. It allows you to search for items of the manager
using the search keys of the sub-managers to further limit the
retrieved list of items.


# type
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/stock/manager/type/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mstoty."id"
 	FROM "mshop_stock_type" mstoty
 	:joins
 	WHERE :cond
 	ORDER BY mstoty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/stock/manager/type/count
* Type: string - SQL statement for counting items
* Since: 2017.01

Counts all records matched by the given criteria from the product
database. The records must be from one of the sites that are
configured via the context item. If the current site is part of
a tree of sites, the statement can count all records from the
current site and the complete sub-tree of sites.

As the records can normally be limited by criteria from sub-managers,
their tables must be joined in the SQL context. This is done by
using the "internaldeps" stock from the definition of the ID
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

* mshop/stock/manager/type/insert/ansi
* mshop/stock/manager/type/update/ansi
* mshop/stock/manager/type/newid/ansi
* mshop/stock/manager/type/delete/ansi
* mshop/stock/manager/type/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/stock/manager/type/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mstoty."id"
 	FROM "mshop_stock_type" mstoty
 	:joins
 	WHERE :cond
 	ORDER BY mstoty."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mstoty."id"
 	FROM "mshop_stock_type" mstoty
 	:joins
 	WHERE :cond
 	ORDER BY mstoty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/stock/manager/type/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the stock type manager

```
mshop/stock/manager/type/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the stock type manager.

```
 mshop/stock/manager/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the stock type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/stock/manager/type/decorators/global
* mshop/stock/manager/type/decorators/local

## decorators/global

Adds a list of globally available decorators only to the stock type manager

```
mshop/stock/manager/type/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the stock type
manager.

```
 mshop/stock/manager/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the stock
type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/stock/manager/type/decorators/excludes
* mshop/stock/manager/type/decorators/local

## decorators/local

Adds a list of local decorators only to the stock type manager

```
mshop/stock/manager/type/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2017.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Stock\Manager\Type\Decorator\*") around the stock type
manager.

```
 mshop/stock/manager/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Stock\Manager\Type\Decorator\Decorator2" only to the
stock type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/stock/manager/type/decorators/excludes
* mshop/stock/manager/type/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/stock/manager/type/delete/ansi = 
 DELETE FROM "mshop_stock_type"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: mshop/stock/manager/type/delete
* Type: string - SQL statement for deleting items
* Since: 2017.01

Removes the records specified by the given IDs from the product database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/stock/manager/type/insert/ansi
* mshop/stock/manager/type/update/ansi
* mshop/stock/manager/type/newid/ansi
* mshop/stock/manager/type/search/ansi
* mshop/stock/manager/type/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/stock/manager/type/delete/mysql = 
 DELETE FROM "mshop_stock_type"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: 
 DELETE FROM "mshop_stock_type"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/stock/manager/type/delete/ansi

## insert/ansi

Inserts a new stock type record into the database table

```
mshop/stock/manager/type/insert/ansi = 
 INSERT INTO "mshop_stock_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/stock/manager/type/insert
* Type: string - SQL statement for inserting records
* Since: 2017.01

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the product type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/stock/manager/type/update/ansi
* mshop/stock/manager/type/newid/ansi
* mshop/stock/manager/type/delete/ansi
* mshop/stock/manager/type/search/ansi
* mshop/stock/manager/type/count/ansi

## insert/mysql

Inserts a new stock type record into the database table

```
mshop/stock/manager/type/insert/mysql = 
 INSERT INTO "mshop_stock_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_stock_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/stock/manager/type/insert/ansi

## name

Class name of the used stock type manager implementation

```
mshop/stock/manager/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2017.01

Each default stock type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Product\Manager\Stock\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Product\Manager\Stock\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/stock/manager/type/name = Mytype
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyType"!


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/stock/manager/type/newid/ansi = mshop/stock/manager/type/newid
```

* Default: mshop/stock/manager/type/newid
* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2017.01

As soon as a new record is inserted into the database table,
the database server generates a new and unique identifier for
that record. This ID can be used for retrieving, updating and
deleting that specific record from the table again.

For MySQL:
```
 SELECT LAST_INSERT_ID()
For PostgreSQL:
 SELECT currval('seq_mproprty_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mproprty_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/stock/manager/type/insert/ansi
* mshop/stock/manager/type/update/ansi
* mshop/stock/manager/type/delete/ansi
* mshop/stock/manager/type/search/ansi
* mshop/stock/manager/type/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/stock/manager/type/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/stock/manager/type/newid

See also:

* mshop/stock/manager/type/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/stock/manager/type/search/ansi = 
 SELECT :columns
 	mstoty."id" AS "stock.type.id", mstoty."siteid" AS "stock.type.siteid",
 	mstoty."code" AS "stock.type.code", mstoty."domain" AS "stock.type.domain",
 	mstoty."label" AS "stock.type.label", mstoty."status" AS "stock.type.status",
 	mstoty."mtime" AS "stock.type.mtime", mstoty."editor" AS "stock.type.editor",
 	mstoty."ctime" AS "stock.type.ctime", mstoty."pos" AS "stock.type.position"
 FROM "mshop_stock_type" mstoty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/stock/manager/type/search
* Type: string - SQL statement for searching items
* Since: 2017.01

Fetches the records matched by the given criteria from the product
database. The records must be from one of the sites that are
configured via the context item. If the current site is part of
a tree of sites, the SELECT statement can retrieve all records
from the current site and the complete sub-tree of sites.

As the records can normally be limited by criteria from sub-managers,
their tables must be joined in the SQL context. This is done by
using the "internaldeps" stock from the definition of the ID
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

* mshop/stock/manager/type/insert/ansi
* mshop/stock/manager/type/update/ansi
* mshop/stock/manager/type/newid/ansi
* mshop/stock/manager/type/delete/ansi
* mshop/stock/manager/type/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/stock/manager/type/search/mysql = 
 SELECT :columns
 	mstoty."id" AS "stock.type.id", mstoty."siteid" AS "stock.type.siteid",
 	mstoty."code" AS "stock.type.code", mstoty."domain" AS "stock.type.domain",
 	mstoty."label" AS "stock.type.label", mstoty."status" AS "stock.type.status",
 	mstoty."mtime" AS "stock.type.mtime", mstoty."editor" AS "stock.type.editor",
 	mstoty."ctime" AS "stock.type.ctime", mstoty."pos" AS "stock.type.position"
 FROM "mshop_stock_type" mstoty
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mstoty."id" AS "stock.type.id", mstoty."siteid" AS "stock.type.siteid",
 	mstoty."code" AS "stock.type.code", mstoty."domain" AS "stock.type.domain",
 	mstoty."label" AS "stock.type.label", mstoty."status" AS "stock.type.status",
 	mstoty."mtime" AS "stock.type.mtime", mstoty."editor" AS "stock.type.editor",
 	mstoty."ctime" AS "stock.type.ctime", mstoty."pos" AS "stock.type.position"
 FROM "mshop_stock_type" mstoty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/stock/manager/type/search/ansi

## submanagers

List of manager names that can be instantiated by the stock type manager

```
mshop/stock/manager/type/submanagers = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-manager names
* Since: 2017.01

Managers provide a generic interface to the underlying storage.
Each manager has or can have sub-managers caring about particular
aspects. Each of these sub-managers can be instantiated by its
parent manager using the getSubManager() method.

The search keys from sub-managers can be normally used in the
manager as well. It allows you to search for items of the manager
using the search keys of the sub-managers to further limit the
retrieved list of items.


## update/ansi

Updates an existing stock type record in the database

```
mshop/stock/manager/type/update/ansi = 
 UPDATE "mshop_stock_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: mshop/stock/manager/type/update
* Type: string - SQL statement for updating records
* Since: 2017.01

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the product type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/stock/manager/type/insert/ansi
* mshop/stock/manager/type/newid/ansi
* mshop/stock/manager/type/delete/ansi
* mshop/stock/manager/type/search/ansi
* mshop/stock/manager/type/count/ansi

## update/mysql

Updates an existing stock type record in the database

```
mshop/stock/manager/type/update/mysql = 
 UPDATE "mshop_stock_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_stock_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/stock/manager/type/update/ansi

# update
## ansi

Updates an existing product stock record in the database

```
mshop/stock/manager/update/ansi = 
 UPDATE "mshop_stock"
 SET :names
 	"prodid" = ?, "type" = ?, "stocklevel" = ?, "backdate" = ?,
 	"timeframe" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: mshop/stock/manager/update
* Type: string - SQL statement for updating records
* Since: 2017.01

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the product stock item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/stock/manager/insert/ansi
* mshop/stock/manager/newid/ansi
* mshop/stock/manager/delete/ansi
* mshop/stock/manager/search/ansi
* mshop/stock/manager/count/ansi
* mshop/stock/manager/stocklevel

## mysql

Updates an existing product stock record in the database

```
mshop/stock/manager/update/mysql = 
 UPDATE "mshop_stock"
 SET :names
 	"prodid" = ?, "type" = ?, "stocklevel" = ?, "backdate" = ?,
 	"timeframe" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_stock"
 SET :names
 	"prodid" = ?, "type" = ?, "stocklevel" = ?, "backdate" = ?,
 	"timeframe" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/stock/manager/update/ansi