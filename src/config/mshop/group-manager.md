
# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/group/manager/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mgro."id"
 	FROM "mshop_group" mgro
 	:joins
 	WHERE :cond
 	ORDER BY mgro."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Type: string - SQL statement for counting items
* Since: 2015.08

Counts all records matched by the given criteria from the group
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

* mshop/group/manager/insert/ansi
* mshop/group/manager/update/ansi
* mshop/group/manager/newid/ansi
* mshop/group/manager/delete/ansi
* mshop/group/manager/search/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/group/manager/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mgro."id"
 	FROM "mshop_group" mgro
 	:joins
 	WHERE :cond
 	ORDER BY mgro."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
```

 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mgro."id"
 	FROM "mshop_group" mgro
 	:joins
 	WHERE :cond
 	ORDER BY mgro."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

See also:

* mshop/group/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the group manager

```
mshop/group/manager/decorators/excludes = Array
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
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the group manager.

```
 mshop/group/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the group manager.

See also:

* mshop/common/manager/decorators/default
* mshop/group/manager/decorators/global
* mshop/group/manager/decorators/local

## global

Adds a list of globally available decorators only to the group manager

```
mshop/group/manager/decorators/global = Array
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
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the group manager.

```
 mshop/group/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the group
group manager.

See also:

* mshop/common/manager/decorators/default
* mshop/group/manager/decorators/excludes
* mshop/group/manager/decorators/local

## local

Adds a list of local decorators only to the group manager

```
mshop/group/manager/decorators/local = Array
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
* Since: 2015.08

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Group\Manager\Decorator\*") around the group
group manager.

```
 mshop/group/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Group\Manager\Decorator\Decorator2" only to the
group manager.

See also:

* mshop/common/manager/decorators/default
* mshop/group/manager/decorators/excludes
* mshop/group/manager/decorators/global

# delete
## ansi

Deletes the items matched by the given IDs from the database

```
mshop/group/manager/delete/ansi = 
 DELETE FROM "mshop_group"
 WHERE :cond AND "siteid" LIKE ?
```

* Type: string - SQL statement for deleting items
* Since: 2015.08

Removes the records specified by the given IDs from the group
database. The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/group/manager/insert/ansi
* mshop/group/manager/update/ansi
* mshop/group/manager/newid/ansi
* mshop/group/manager/search/ansi
* mshop/group/manager/count/ansi

## mysql

Deletes the items matched by the given IDs from the database

```
mshop/group/manager/delete/mysql = 
 DELETE FROM "mshop_group"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: 
```

 DELETE FROM "mshop_group"
 WHERE :cond AND "siteid" LIKE ?
```

See also:

* mshop/group/manager/delete/ansi

# insert
## ansi

Inserts a new group record into the database table

```
mshop/group/manager/insert/ansi = 
 INSERT INTO "mshop_group" ( :names
 	"code", "label", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?
 )
```

* Type: string - SQL statement for inserting records
* Since: 2015.08

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the group item to the statement before
they are sent to the database server. The number of question
marks must be the same as the number of columns listed in the
INSERT statement. The order of the columns must correspond to
the order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/group/manager/update/ansi
* mshop/group/manager/newid/ansi
* mshop/group/manager/delete/ansi
* mshop/group/manager/search/ansi
* mshop/group/manager/count/ansi

## mysql

Inserts a new group record into the database table

```
mshop/group/manager/insert/mysql = 
 INSERT INTO "mshop_group" ( :names
 	"code", "label", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?
 )
```

* Default: 
```

 INSERT INTO "mshop_group" ( :names
 	"code", "label", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?
 )
```

See also:

* mshop/group/manager/insert/ansi

# name

Class name of the used group manager implementation

```
mshop/group/manager/name = Standard
```

* Default: `Standard`
* Type: string - Last part of the class name
* Since: 2015.08

Each default group manager can be replaced by an alternative
imlementation. To use this implementation, you have to set the last
part of the class name as configuration value so the manager factory
knows which class it has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Group\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Group\Manager\Mygroup
```

then you have to set the this configuration option:

```
 mshop/group/manager/name = Mygroup
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyGroup"!


# newid
## ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/group/manager/newid/ansi = 
```

* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2015.08

As soon as a new record is inserted into the database table,
the database server generates a new and unique identifier for
that record. This ID can be used for retrieving, updating and
deleting that specific record from the table again.

For MySQL:
```
 SELECT LAST_INSERT_ID()
For PostgreSQL:
 SELECT currval('seq_mcus_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mcus_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/group/manager/insert/ansi
* mshop/group/manager/update/ansi
* mshop/group/manager/delete/ansi
* mshop/group/manager/search/ansi
* mshop/group/manager/count/ansi

## mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/group/manager/newid/mysql = SELECT LAST_INSERT_ID()
```


See also:

* mshop/group/manager/newid/ansi

# resource

Name of the database connection resource to use

```
mshop/group/manager/resource = db-group
```

* Default: `db-group`
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
mshop/group/manager/search/ansi = 
 SELECT :columns
 FROM "mshop_group" mgro
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Type: string - SQL statement for searching items
* Since: 2015.08

Fetches the records matched by the given criteria from the group
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

* mshop/group/manager/insert/ansi
* mshop/group/manager/update/ansi
* mshop/group/manager/newid/ansi
* mshop/group/manager/delete/ansi
* mshop/group/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/group/manager/search/mysql = 
 SELECT :columns
 FROM "mshop_group" mgro
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
```

 SELECT :columns
 FROM "mshop_group" mgro
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

See also:

* mshop/group/manager/search/ansi

# submanagers

List of manager names that can be instantiated by the group manager

```
mshop/group/manager/submanagers = Array
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
* Since: 2015.08

Managers provide a generic interface to the underlying storage.
Each manager has or can have sub-managers caring about particular
aspects. Each of these sub-managers can be instantiated by its
parent manager using the getSubManager() method.

The search keys from sub-managers can be normally used in the
manager as well. It allows you to search for items of the manager
using the search keys of the sub-managers to further limit the
retrieved list of items.


# typo3
## count

Counts the number of records matched by the given criteria in the database

```
mshop/group/manager/typo3/count = 
```

* Type: string - SQL statement for counting items
* Since: 2015.08

Counts all records matched by the given criteria from the group
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

* mshop/group/manager/typo3/search

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/group/manager/typo3/delete/ansi = 
```

* Type: string - SQL statement for deleting items
* Since: 2015.08

Removes the records specified by the given IDs from the group
database. The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/group/manager/typo3/insert/ansi
* mshop/group/manager/typo3/update/ansi
* mshop/group/manager/typo3/newid/ansi
* mshop/group/manager/typo3/search/ansi
* mshop/group/manager/typo3/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/group/manager/typo3/delete/mysql = 
```


See also:

* mshop/group/manager/typo3/delete/ansi

## insert/ansi

Inserts a new group record into the database table

```
mshop/group/manager/typo3/insert/ansi = 
```

* Type: string - SQL statement for inserting records
* Since: 2015.08

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the group item to the statement before
they are sent to the database server. The number of question
marks must be the same as the number of columns listed in the
INSERT statement. The order of the columns must correspond to
the order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/group/manager/typo3/update/ansi
* mshop/group/manager/typo3/newid/ansi
* mshop/group/manager/typo3/delete/ansi
* mshop/group/manager/typo3/search/ansi
* mshop/group/manager/typo3/count/ansi

## insert/mysql

Inserts a new group record into the database table

```
mshop/group/manager/typo3/insert/mysql = 
```


See also:

* mshop/group/manager/typo3/insert/ansi

## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/group/manager/typo3/newid/ansi = 
```

* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2015.08

As soon as a new record is inserted into the database table,
the database server generates a new and unique identifier for
that record. This ID can be used for retrieving, updating and
deleting that specific record from the table again.

For MySQL:
```
 SELECT LAST_INSERT_ID()
For PostgreSQL:
 SELECT currval('seq_mcus_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mcus_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/group/manager/typo3/insert/ansi
* mshop/group/manager/typo3/update/ansi
* mshop/group/manager/typo3/delete/ansi
* mshop/group/manager/typo3/search/ansi
* mshop/group/manager/typo3/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/group/manager/typo3/newid/mysql = 
```


See also:

* mshop/group/manager/typo3/newid/ansi

## search

Retrieves the records matched by the given criteria in the database

```
mshop/group/manager/typo3/search = 
```

* Type: string - SQL statement for searching items
* Since: 2015.08

Fetches the records matched by the given criteria from the group
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

* mshop/group/manager/typo3/count

## update/ansi

Updates an existing group record in the database

```
mshop/group/manager/typo3/update/ansi = 
```

* Type: string - SQL statement for updating records
* Since: 2015.08

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the group item to the statement before
they are sent to the database server. The order of the columns
must correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/group/manager/typo3/insert/ansi
* mshop/group/manager/typo3/newid/ansi
* mshop/group/manager/typo3/delete/ansi
* mshop/group/manager/typo3/search/ansi
* mshop/group/manager/typo3/count/ansi

## update/mysql

Updates an existing group record in the database

```
mshop/group/manager/typo3/update/mysql = 
```


See also:

* mshop/group/manager/typo3/update/ansi

# update
## ansi

Updates an existing group record in the database

```
mshop/group/manager/update/ansi = 
 UPDATE "mshop_group"
 SET :names
 	"code" = ?, "label" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Type: string - SQL statement for updating records
* Since: 2015.08

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the group item to the statement before
they are sent to the database server. The order of the columns
must correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/group/manager/insert/ansi
* mshop/group/manager/newid/ansi
* mshop/group/manager/delete/ansi
* mshop/group/manager/search/ansi
* mshop/group/manager/count/ansi

## mysql

Updates an existing group record in the database

```
mshop/group/manager/update/mysql = 
 UPDATE "mshop_group"
 SET :names
 	"code" = ?, "label" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: 
```

 UPDATE "mshop_group"
 SET :names
 	"code" = ?, "label" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

See also:

* mshop/group/manager/update/ansi