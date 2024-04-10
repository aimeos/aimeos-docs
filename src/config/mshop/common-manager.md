
# aggregate
## limit

Limits the number of records that are used when aggregating items

```
mshop/common/manager/aggregate/limit = 10000
```

* Default: `10000`
* Type: integer - Number of records
* Since: 2021.04

As counting huge amount of records (several 10 000 records) takes a long time,
the limit can cut down response times so the counts are available more quickly
in the front-end and the server load is reduced.

Using a low limit can lead to incorrect numbers if the amount of found items
is very high. Approximate item counts are normally not a problem but it can
lead to the situation that visitors see that no items are available despite
the fact that there would be at least one.


# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/common/manager/count/ansi = 
```

* Type: string - SQL statement for counting items
* Since: 2023.10

Counts all records matched by the given criteria from the
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

* mshop/common/manager/insert/ansi
* mshop/common/manager/update/ansi
* mshop/common/manager/newid/ansi
* mshop/common/manager/delete/ansi
* mshop/common/manager/search/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/common/manager/count/mysql = 
```


See also:

* mshop/common/manager/count/ansi

# decorators
## default

Configures the list of decorators applied to all shop managers

```
mshop/common/manager/decorators/default = Array
(
    [Depth] => Depth
    [Lazy] => Lazy
)
```

* Default: `Array
(
)
`
* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to configure a list of decorator names that should
be wrapped around the original instances of all created managers:

```
 mshop/common/manager/decorators/default = array( 'decorator1', 'decorator2' )
```

This would wrap the decorators named "decorator1" and "decorator2" around
all controller instances in that order. The decorator classes would be
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" and
"\Aimeos\MShop\Common\Manager\Decorator\Decorator2".


# delete
## ansi

```
mshop/common/manager/delete/ansi = 
 DELETE FROM ":table"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: `mshop/test/manager/delete`


## mysql

```
mshop/common/manager/delete/mysql = 
 DELETE FROM ":table"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: `
 DELETE FROM ":table"
 WHERE :cond AND "siteid" LIKE ?
`


# insert
## ansi

Inserts a new record into the database table

```
mshop/common/manager/insert/ansi = 
 INSERT INTO ":table" (
 	:names
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES (
 	:values
 	?, ?, ?, ?
 )
```

* Default: `mshop/test/manager/insert`
* Type: string - SQL statement for inserting records
* Since: 2023.10

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/common/manager/update/ansi
* mshop/common/manager/newid/ansi
* mshop/common/manager/delete/ansi
* mshop/common/manager/search/ansi
* mshop/common/manager/count/ansi

## mysql

Inserts a new record into the database table

```
mshop/common/manager/insert/mysql = 
 INSERT INTO ":table" (
 	:names
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES (
 	:values
 	?, ?, ?, ?
 )
```

* Default: `
 INSERT INTO ":table" (
 	:names
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES (
 	:values
 	?, ?, ?, ?
 )
`

See also:

* mshop/common/manager/insert/ansi

# maxdepth

Maximum level of recursion for retrieving referenced items

```
mshop/common/manager/maxdepth = 2
```

* Default: `2`
* Type: int - Number of levels
* Since: 2019.04

Searching for items also fetches the associated items referenced in the
list tables if the domain names are passed to the second parameter of e.g. the
search() method. To avoid infinite recursion because two items reference
each other, the maximum level must be limited.

The default setting (two levels) means that retrieving a product item with
sub-products will retrieve the directly associated products but not the
products referenced by the associated product for example.


# newid
## ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/common/manager/newid/ansi = 
```

* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2023.10

As soon as a new record is inserted into the database table,
the database server generates a new and unique identifier for
that record. This ID can be used for retrieving, updating and
deleting that specific record from the table again.

For MySQL:
```
 SELECT LAST_INSERT_ID()
For PostgreSQL:
 SELECT currval('seq_matt_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_matt_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/common/manager/insert/ansi
* mshop/common/manager/update/ansi
* mshop/common/manager/delete/ansi
* mshop/common/manager/search/ansi
* mshop/common/manager/count/ansi

## mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/common/manager/newid/mysql = SELECT LAST_INSERT_ID()
```


See also:

* mshop/common/manager/newid/ansi

# search
## ansi

Retrieves the records matched by the given criteria in the database

```
mshop/common/manager/search/ansi = 
 SELECT :columns
 FROM ":table"
 :joins
 WHERE :cond
 GROUP BY :group
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Type: string - SQL statement for searching items
* Since: 2023.10

Fetches the records matched by the given criteria from the
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

* mshop/common/manager/insert/ansi
* mshop/common/manager/update/ansi
* mshop/common/manager/newid/ansi
* mshop/common/manager/delete/ansi
* mshop/common/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/common/manager/search/mysql = 
 SELECT :columns
 FROM ":table"
 :joins
 WHERE :cond
 GROUP BY :group
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: `
 SELECT :columns
 FROM ":table"
 :joins
 WHERE :cond
 GROUP BY :group
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
`

See also:

* mshop/common/manager/search/ansi

# update
## ansi

Updates an existing record in the database

```
mshop/common/manager/update/ansi = 
```

* Type: string - SQL statement for updating records
* Since: 2023.10

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/common/manager/insert/ansi
* mshop/common/manager/newid/ansi
* mshop/common/manager/delete/ansi
* mshop/common/manager/search/ansi
* mshop/common/manager/count/ansi

## mysql

Updates an existing record in the database

```
mshop/common/manager/update/mysql = 
```


See also:

* mshop/common/manager/update/ansi