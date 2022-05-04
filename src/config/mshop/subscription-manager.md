
# aggregate
## ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/subscription/manager/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_subscription" mord
 	:joins
 	WHERE :cond
 	GROUP BY mord.id, :cols, :val
 	ORDER BY mord.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/subscription/manager/aggregate
* Type: string - SQL statement for aggregating subscription items
* Since: 2018.04

Groups all records by the values in the key column and counts their
occurence. The matched records can be limited by the given criteria
from the subscription database. The records must be from one of the sites
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

* mshop/subscription/manager/insert/ansi
* mshop/subscription/manager/update/ansi
* mshop/subscription/manager/newid/ansi
* mshop/subscription/manager/delete/ansi
* mshop/subscription/manager/search/ansi
* mshop/subscription/manager/count/ansi

## mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/subscription/manager/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_subscription" mord
 	:joins
 	WHERE :cond
 	GROUP BY mord.id, :cols, :val
 	ORDER BY mord.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_subscription" mord
 	:joins
 	WHERE :cond
 	GROUP BY mord.id, :cols, :val
 	ORDER BY mord.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/subscription/manager/aggregate/ansi

# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/subscription/manager/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mord."id"
 	FROM "mshop_subscription" mord
 	:joins
 	WHERE :cond
 	GROUP BY mord."id"
 	ORDER BY mord."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/subscription/manager/count
* Type: string - SQL statement for counting items
* Since: 2018.04

Counts all records matched by the given criteria from the subscription
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

* mshop/subscription/manager/insert/ansi
* mshop/subscription/manager/update/ansi
* mshop/subscription/manager/newid/ansi
* mshop/subscription/manager/delete/ansi
* mshop/subscription/manager/search/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/subscription/manager/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mord."id"
 	FROM "mshop_subscription" mord
 	:joins
 	WHERE :cond
 	GROUP BY mord."id"
 	ORDER BY mord."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mord."id"
 	FROM "mshop_subscription" mord
 	:joins
 	WHERE :cond
 	GROUP BY mord."id"
 	ORDER BY mord."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/subscription/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the subscription manager

```
mshop/subscription/manager/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the subscription manager.

```
 mshop/subscription/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the subscription manager.

See also:

* mshop/common/manager/decorators/default
* mshop/subscription/manager/decorators/global
* mshop/subscription/manager/decorators/local

## global

Adds a list of globally available decorators only to the subscription manager

```
mshop/subscription/manager/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the subscription
manager.

```
 mshop/subscription/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the
subscription manager.

See also:

* mshop/common/manager/decorators/default
* mshop/subscription/manager/decorators/excludes
* mshop/subscription/manager/decorators/local

## local

Adds a list of local decorators only to the subscription manager

```
mshop/subscription/manager/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2018.04

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Subscription\Manager\Decorator\*") around the subscription
manager.

```
 mshop/subscription/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Subscription\Manager\Decorator\Decorator2" only to the
subscription manager.

See also:

* mshop/common/manager/decorators/default
* mshop/subscription/manager/decorators/excludes
* mshop/subscription/manager/decorators/global

# delete
## ansi

Deletes the items matched by the given IDs from the database

```
mshop/subscription/manager/delete/ansi = 
 DELETE FROM "mshop_subscription"
 WHERE :cond AND siteid = ?
```

* Default: mshop/subscription/manager/delete
* Type: string - SQL statement for deleting items
* Since: 2018.04

Removes the records specified by the given IDs from the subscription database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/subscription/manager/insert/ansi
* mshop/subscription/manager/update/ansi
* mshop/subscription/manager/newid/ansi
* mshop/subscription/manager/search/ansi
* mshop/subscription/manager/count/ansi

## mysql

Deletes the items matched by the given IDs from the database

```
mshop/subscription/manager/delete/mysql = 
 DELETE FROM "mshop_subscription"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_subscription"
 WHERE :cond AND siteid = ?


See also:

* mshop/subscription/manager/delete/ansi

# insert
## ansi

Inserts a new subscription record into the database table

```
mshop/subscription/manager/insert/ansi = 
 INSERT INTO "mshop_subscription" ( :names
 	"baseid", "ordprodid", "next", "end", "interval", "productid", "period",
 	"reason", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/subscription/manager/insert
* Type: string - SQL statement for inserting records
* Since: 2018.04

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the subscription item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The subscription of the columns must correspond to the
subscription in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/subscription/manager/update/ansi
* mshop/subscription/manager/newid/ansi
* mshop/subscription/manager/delete/ansi
* mshop/subscription/manager/search/ansi
* mshop/subscription/manager/count/ansi

## mysql

Inserts a new subscription record into the database table

```
mshop/subscription/manager/insert/mysql = 
 INSERT INTO "mshop_subscription" ( :names
 	"baseid", "ordprodid", "next", "end", "interval", "productid", "period",
 	"reason", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_subscription" ( :names
 	"baseid", "ordprodid", "next", "end", "interval", "productid", "period",
 	"reason", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/subscription/manager/insert/ansi

# name

Class name of the used subscription manager implementation

```
mshop/subscription/manager/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.04

Each default manager can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Subscription\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Subscription\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/subscription/manager/name = Mymanager
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
mshop/subscription/manager/newid/ansi = mshop/subscription/manager/newid
```

* Default: mshop/subscription/manager/newid
* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2018.04

As soon as a new record is inserted into the database table,
the database server generates a new and unique identifier for
that record. This ID can be used for retrieving, updating and
deleting that specific record from the table again.

For MySQL:
```
 SELECT LAST_INSERT_ID()
For PostgreSQL:
 SELECT currval('seq_msub_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_msub_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/subscription/manager/insert/ansi
* mshop/subscription/manager/update/ansi
* mshop/subscription/manager/delete/ansi
* mshop/subscription/manager/search/ansi
* mshop/subscription/manager/count/ansi

## mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/subscription/manager/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/subscription/manager/newid

See also:

* mshop/subscription/manager/newid/ansi

# search
## ansi

Retrieves the records matched by the given criteria in the database

```
mshop/subscription/manager/search/ansi = 
 SELECT :columns
 	mord."id" AS "subscription.id", mord."baseid" AS "subscription.ordbaseid",
 	mord."ordprodid" AS "subscription.ordprodid", mord."siteid" AS "subscription.siteid",
 	mord."next" AS "subscription.datenext", mord."end" AS "subscription.dateend",
 	mord."interval" AS "subscription.interval", mord."reason" AS "subscription.reason",
 	mord."productid" AS "subscription.productid", mord."period" AS "subscription.period",
 	mord."status" AS "subscription.status", mord."ctime" AS "subscription.ctime",
 	mord."mtime" AS "subscription.mtime", mord."editor" AS "subscription.editor"
 FROM "mshop_subscription" mord
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mord."id", mord."baseid", mord."ordprodid", mord."siteid", mord."next", mord."end",
 	mord."interval", mord."reason", mord."productid", mord."period", mord."status", mord."ctime",
 	mord."mtime", mord."editor"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/subscription/manager/search
* Type: string - SQL statement for searching items
* Since: 2018.04

Fetches the records matched by the given criteria from the subscription
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

If the records that are retrieved should be subscriptioned by one or more
columns, the generated string of column / sort direction pairs
replaces the ":subscription" placeholder. In case no subscriptioning is required,
the complete ORDER BY part including the "/*-subscriptionby*/.../*subscriptionby-*/"
markers is removed to speed up retrieving the records. Columns of
sub-managers can also be used for subscriptioning the result set but then
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

* mshop/subscription/manager/insert/ansi
* mshop/subscription/manager/update/ansi
* mshop/subscription/manager/newid/ansi
* mshop/subscription/manager/delete/ansi
* mshop/subscription/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/subscription/manager/search/mysql = 
 SELECT :columns
 	mord."id" AS "subscription.id", mord."baseid" AS "subscription.ordbaseid",
 	mord."ordprodid" AS "subscription.ordprodid", mord."siteid" AS "subscription.siteid",
 	mord."next" AS "subscription.datenext", mord."end" AS "subscription.dateend",
 	mord."interval" AS "subscription.interval", mord."reason" AS "subscription.reason",
 	mord."productid" AS "subscription.productid", mord."period" AS "subscription.period",
 	mord."status" AS "subscription.status", mord."ctime" AS "subscription.ctime",
 	mord."mtime" AS "subscription.mtime", mord."editor" AS "subscription.editor"
 FROM "mshop_subscription" mord
 :joins
 WHERE :cond
 GROUP BY :group mord."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mord."id" AS "subscription.id", mord."baseid" AS "subscription.ordbaseid",
 	mord."ordprodid" AS "subscription.ordprodid", mord."siteid" AS "subscription.siteid",
 	mord."next" AS "subscription.datenext", mord."end" AS "subscription.dateend",
 	mord."interval" AS "subscription.interval", mord."reason" AS "subscription.reason",
 	mord."productid" AS "subscription.productid", mord."period" AS "subscription.period",
 	mord."status" AS "subscription.status", mord."ctime" AS "subscription.ctime",
 	mord."mtime" AS "subscription.mtime", mord."editor" AS "subscription.editor"
 FROM "mshop_subscription" mord
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mord."id", mord."baseid", mord."ordprodid", mord."siteid", mord."next", mord."end",
 	mord."interval", mord."reason", mord."productid", mord."period", mord."status", mord."ctime",
 	mord."mtime", mord."editor"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/subscription/manager/search/ansi

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/subscription/manager/sitemode = 2
```

* Default: 2
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.04

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole subscription domain if items from parent sites are inherited,
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

List of manager names that can be instantiated by the subscription manager

```
mshop/subscription/manager/submanagers = Array
(
    [0] => base
)
```

* Default: Array
(
    [0] => base
)

* Type: array - List of sub-manager names
* Since: 2018.04

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

Updates an existing subscription record in the database

```
mshop/subscription/manager/update/ansi = 
 UPDATE "mshop_subscription"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "next" = ?, "end" = ?, "interval" = ?,
 	"productid" = ?, "period" = ?, "reason" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/subscription/manager/update
* Type: string - SQL statement for updating records
* Since: 2018.04

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the subscription item to the statement before they are
sent to the database server. The subscription of the columns must
correspond to the subscription in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/subscription/manager/insert/ansi
* mshop/subscription/manager/newid/ansi
* mshop/subscription/manager/delete/ansi
* mshop/subscription/manager/search/ansi
* mshop/subscription/manager/count/ansi

## mysql

Updates an existing subscription record in the database

```
mshop/subscription/manager/update/mysql = 
 UPDATE "mshop_subscription"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "next" = ?, "end" = ?, "interval" = ?,
 	"productid" = ?, "period" = ?, "reason" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_subscription"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "next" = ?, "end" = ?, "interval" = ?,
 	"productid" = ?, "period" = ?, "reason" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/subscription/manager/update/ansi