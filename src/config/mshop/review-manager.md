
# aggregate
## ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/review/manager/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_review" mrev
 	:joins
 	WHERE :cond
 	ORDER BY mrev.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Type: string - SQL statement for aggregating review items
* Since: 2020.10

Groups all records by the values in the key column and counts their
occurence. The matched records can be limited by the given criteria
from the review database. The records must be from one of the sites
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

* mshop/review/manager/insert/ansi
* mshop/review/manager/update/ansi
* mshop/review/manager/newid/ansi
* mshop/review/manager/delete/ansi
* mshop/review/manager/search/ansi
* mshop/review/manager/count/ansi

## mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/review/manager/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_review" mrev
 	:joins
 	WHERE :cond
 	ORDER BY :order
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
```

 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_review" mrev
 	:joins
 	WHERE :cond
 	ORDER BY mrev.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

See also:

* mshop/review/manager/aggregate/ansi

# aggregaterate
## ansi

```
mshop/review/manager/aggregaterate/ansi = 
 SELECT :keys, SUM("val") AS "sum", COUNT(*) AS "count"
 FROM (
 	SELECT :acols, mrev.rating AS "val"
 	FROM "mshop_review" mrev
 	:joins
 	WHERE :cond
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```



## mysql

```
mshop/review/manager/aggregaterate/mysql = 
 SELECT :keys, SUM("val") AS "sum", COUNT(*) AS "count"
 FROM (
 	SELECT :acols, mrev.rating AS "val"
 	FROM "mshop_review" mrev
 	:joins
 	WHERE :cond
 	ORDER BY :order
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
```

 SELECT :keys, SUM("val") AS "sum", COUNT(*) AS "count"
 FROM (
 	SELECT :acols, mrev.rating AS "val"
 	FROM "mshop_review" mrev
 	:joins
 	WHERE :cond
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```


# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/review/manager/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mrev."id"
 	FROM "mshop_review" mrev
 	:joins
 	WHERE :cond
 	GROUP BY mrev."id"
 	ORDER BY mrev."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Type: string - SQL statement for counting items
* Since: 2020.10

Counts all records matched by the given criteria from the review
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

* mshop/review/manager/insert/ansi
* mshop/review/manager/update/ansi
* mshop/review/manager/newid/ansi
* mshop/review/manager/delete/ansi
* mshop/review/manager/search/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/review/manager/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mrev."id"
 	FROM "mshop_review" mrev
 	:joins
 	WHERE :cond
 	GROUP BY mrev."id"
 	ORDER BY mrev."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
```

 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mrev."id"
 	FROM "mshop_review" mrev
 	:joins
 	WHERE :cond
 	GROUP BY mrev."id"
 	ORDER BY mrev."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

See also:

* mshop/review/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the review manager

```
mshop/review/manager/decorators/excludes = Array
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
* Since: 2020.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the review manager.

```
 mshop/review/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the review manager.

See also:

* mshop/common/manager/decorators/default
* mshop/review/manager/decorators/global
* mshop/review/manager/decorators/local

## global

Adds a list of globally available decorators only to the review manager

```
mshop/review/manager/decorators/global = Array
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
* Since: 2020.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the review
manager.

```
 mshop/review/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the
review manager.

See also:

* mshop/common/manager/decorators/default
* mshop/review/manager/decorators/excludes
* mshop/review/manager/decorators/local

## local

Adds a list of local decorators only to the review manager

```
mshop/review/manager/decorators/local = Array
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
* Since: 2020.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Review\Manager\Decorator\*") around the review
manager.

```
 mshop/review/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Review\Manager\Decorator\Decorator2" only to the
review manager.

See also:

* mshop/common/manager/decorators/default
* mshop/review/manager/decorators/excludes
* mshop/review/manager/decorators/global

# delete
## ansi

Deletes the items matched by the given IDs from the database

```
mshop/review/manager/delete/ansi = 
 DELETE FROM "mshop_review"
 WHERE :cond AND "siteid" LIKE ?
```

* Type: string - SQL statement for deleting items
* Since: 2020.10

Removes the records specified by the given IDs from the review database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/review/manager/insert/ansi
* mshop/review/manager/update/ansi
* mshop/review/manager/newid/ansi
* mshop/review/manager/search/ansi
* mshop/review/manager/count/ansi

## mysql

Deletes the items matched by the given IDs from the database

```
mshop/review/manager/delete/mysql = 
 DELETE FROM "mshop_review"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: 
```

 DELETE FROM "mshop_review"
 WHERE :cond AND "siteid" LIKE ?
```

See also:

* mshop/review/manager/delete/ansi

# insert
## ansi

Inserts a new review record into the database table

```
mshop/review/manager/insert/ansi = 
 INSERT INTO "mshop_review" ( :names
 	"domain", "refid", "customerid", "ordprodid", "name", "comment", "response",
 	"rating", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Type: string - SQL statement for inserting records
* Since: 2020.10

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the review item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The review of the columns must correspond to the
review in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/review/manager/update/ansi
* mshop/review/manager/newid/ansi
* mshop/review/manager/delete/ansi
* mshop/review/manager/search/ansi
* mshop/review/manager/count/ansi

## mysql

Inserts a new review record into the database table

```
mshop/review/manager/insert/mysql = 
 INSERT INTO "mshop_review" ( :names
 	"domain", "refid", "customerid", "ordprodid", "name", "comment", "response",
 	"rating", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
```

 INSERT INTO "mshop_review" ( :names
 	"domain", "refid", "customerid", "ordprodid", "name", "comment", "response",
 	"rating", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

See also:

* mshop/review/manager/insert/ansi

# name

Class name of the used review manager implementation

```
mshop/review/manager/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2020.10

Each default manager can be replace by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Review\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Review\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/review/manager/name = Mymanager
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
mshop/review/manager/newid/ansi = 
```

* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2020.10

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

* mshop/review/manager/insert/ansi
* mshop/review/manager/update/ansi
* mshop/review/manager/delete/ansi
* mshop/review/manager/search/ansi
* mshop/review/manager/count/ansi

## mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/review/manager/newid/mysql = SELECT LAST_INSERT_ID()
```


See also:

* mshop/review/manager/newid/ansi

# resource

Name of the database connection resource to use

```
mshop/review/manager/resource = db-review
```

* Default: `db-review`
* Type: string - Database connection name
* Since: 2023.04

You can configure a different database connection for each data domain
and if no such connection name exists, the "db" connection will be used.
It's also possible to use the same database connection for different
data domains by configuring the same connection name using this setting.


# search
## ansi

Retrieves the records matched by the given criteria in the database

```
mshop/review/manager/search/ansi = 
 SELECT :columns
 FROM "mshop_review" mrev
 :joins
 WHERE :cond
 GROUP BY :group
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Type: string - SQL statement for searching items
* Since: 2020.10

Fetches the records matched by the given criteria from the review
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

If the records that are retrieved should be reviewed by one or more
columns, the generated string of column / sort direction pairs
replaces the ":review" placeholder. In case no reviewing is required,
the complete ORDER BY part including the "/*-reviewby*/.../*reviewby-*/"
markers is removed to speed up retrieving the records. Columns of
sub-managers can also be used for reviewing the result set but then
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

* mshop/review/manager/insert/ansi
* mshop/review/manager/update/ansi
* mshop/review/manager/newid/ansi
* mshop/review/manager/delete/ansi
* mshop/review/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/review/manager/search/mysql = 
 SELECT :columns
 FROM "mshop_review" mrev
 :joins
 WHERE :cond
 GROUP BY :group
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
```

 SELECT :columns
 FROM "mshop_review" mrev
 :joins
 WHERE :cond
 GROUP BY :group
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

See also:

* mshop/review/manager/search/ansi

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/review/manager/sitemode = 2
```

* Default: `2`
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2020.10

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole review domain if items from parent sites are inherited,
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

List of manager names that can be instantiated by the review manager

```
mshop/review/manager/submanagers = Array
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
* Since: 2020.10

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

Updates an existing review record in the database

```
mshop/review/manager/update/ansi = 
```

* Type: string - SQL statement for updating records
* Since: 2020.10

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the review item to the statement before they are
sent to the database server. The review of the columns must
correspond to the review in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/review/manager/insert/ansi
* mshop/review/manager/newid/ansi
* mshop/review/manager/delete/ansi
* mshop/review/manager/search/ansi
* mshop/review/manager/count/ansi

## mysql

Updates an existing review record in the database

```
mshop/review/manager/update/mysql = 
```


See also:

* mshop/review/manager/update/ansi