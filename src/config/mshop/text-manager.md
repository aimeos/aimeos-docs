
# decorators
## excludes

Excludes decorators added by the "common" option from the text manager

```
mshop/text/manager/decorators/excludes = Array
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
around the text manager.

```
 mshop/text/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the text manager.

See also:

* mshop/common/manager/decorators/default
* mshop/text/manager/decorators/global
* mshop/text/manager/decorators/local

## global

Adds a list of globally available decorators only to the text manager

```
mshop/text/manager/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the text manager.

```
 mshop/text/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the text
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/text/manager/decorators/excludes
* mshop/text/manager/decorators/local

## local

Adds a list of local decorators only to the text manager

```
mshop/text/manager/decorators/local = Array
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
("\Aimeos\MShop\Text\Manager\Decorator\*") around the text manager.

```
 mshop/text/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Text\Manager\Decorator\Decorator2" only to the text
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/text/manager/decorators/excludes
* mshop/text/manager/decorators/global

# lists
## decorators/excludes

Excludes decorators added by the "common" option from the text list manager

```
mshop/text/manager/lists/decorators/excludes = Array
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
around the text list manager.

```
 mshop/text/manager/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the text list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/text/manager/lists/decorators/global
* mshop/text/manager/lists/decorators/local

## decorators/global

Adds a list of globally available decorators only to the text list manager

```
mshop/text/manager/lists/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the text list manager.

```
 mshop/text/manager/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the text
list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/text/manager/lists/decorators/excludes
* mshop/text/manager/lists/decorators/local

## decorators/local

Adds a list of local decorators only to the text list manager

```
mshop/text/manager/lists/decorators/local = Array
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
("\Aimeos\MShop\Text\Manager\Lists\Decorator\*") around the text list
manager.

```
 mshop/text/manager/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Text\Manager\Lists\Decorator\Decorator2" only to the text
list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/text/manager/lists/decorators/excludes
* mshop/text/manager/lists/decorators/global

## name

Class name of the used text list manager implementation

```
mshop/text/manager/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default text list manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Text\Manager\Lists\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Text\Manager\Lists\Mylist
```

then you have to set the this configuration option:

```
 mshop/text/manager/lists/name = Mylist
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
mshop/text/manager/lists/standard/aggregate/ansi = 
 SELECT "key", COUNT("id") AS "count"
 FROM (
 	SELECT :key AS "key", mtexli."id" AS "id"
 	FROM "mshop_text_list" AS mtexli
 	:joins
 	WHERE :cond
 	GROUP BY :key, mtexli."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY "key"
```

* Default: mshop/text/manager/lists/standard/aggregate
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

* mshop/text/manager/lists/standard/insert/ansi
* mshop/text/manager/lists/standard/update/ansi
* mshop/text/manager/lists/standard/newid/ansi
* mshop/text/manager/lists/standard/delete/ansi
* mshop/text/manager/lists/standard/search/ansi
* mshop/text/manager/lists/standard/count/ansi

## standard/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/text/manager/lists/standard/aggregate/mysql = 
 SELECT "key", COUNT("id") AS "count"
 FROM (
 	SELECT :key AS "key", mtexli."id" AS "id"
 	FROM "mshop_text_list" AS mtexli
 	:joins
 	WHERE :cond
 	GROUP BY :key, mtexli."id"
 	ORDER BY :order
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY "key"
```

* Default: 
 SELECT "key", COUNT("id") AS "count"
 FROM (
 	SELECT :key AS "key", mtexli."id" AS "id"
 	FROM "mshop_text_list" AS mtexli
 	:joins
 	WHERE :cond
 	GROUP BY :key, mtexli."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY "key"


See also:

* mshop/text/manager/lists/standard/aggregate/ansi

## standard/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/text/manager/lists/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mtexli."id"
 	FROM "mshop_text_list" AS mtexli
 	:joins
 	WHERE :cond
 	ORDER BY mtexli."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/text/manager/lists/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the text
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

* mshop/text/manager/lists/standard/insert/ansi
* mshop/text/manager/lists/standard/update/ansi
* mshop/text/manager/lists/standard/newid/ansi
* mshop/text/manager/lists/standard/delete/ansi
* mshop/text/manager/lists/standard/search/ansi
* mshop/text/manager/lists/standard/aggregate/ansi

## standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/text/manager/lists/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mtexli."id"
 	FROM "mshop_text_list" AS mtexli
 	:joins
 	WHERE :cond
 	ORDER BY mtexli."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mtexli."id"
 	FROM "mshop_text_list" AS mtexli
 	:joins
 	WHERE :cond
 	ORDER BY mtexli."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/text/manager/lists/standard/count/ansi

## standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/text/manager/lists/standard/delete/ansi = 
 DELETE FROM "mshop_text_list"
 WHERE :cond AND siteid = ?
```

* Default: mshop/text/manager/lists/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the text database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/text/manager/lists/standard/insert/ansi
* mshop/text/manager/lists/standard/update/ansi
* mshop/text/manager/lists/standard/newid/ansi
* mshop/text/manager/lists/standard/search/ansi
* mshop/text/manager/lists/standard/count/ansi
* mshop/text/manager/lists/standard/aggregate/ansi

## standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/text/manager/lists/standard/delete/mysql = 
 DELETE FROM "mshop_text_list"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_text_list"
 WHERE :cond AND siteid = ?


See also:

* mshop/text/manager/lists/standard/delete/ansi

## standard/insert/ansi

Inserts a new text list record into the database table

```
mshop/text/manager/lists/standard/insert/ansi = 
 INSERT INTO "mshop_text_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/text/manager/lists/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the text list item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/text/manager/lists/standard/update/ansi
* mshop/text/manager/lists/standard/newid/ansi
* mshop/text/manager/lists/standard/delete/ansi
* mshop/text/manager/lists/standard/search/ansi
* mshop/text/manager/lists/standard/count/ansi
* mshop/text/manager/lists/standard/aggregate/ansi

## standard/insert/mysql

Inserts a new text list record into the database table

```
mshop/text/manager/lists/standard/insert/mysql = 
 INSERT INTO "mshop_text_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_text_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/text/manager/lists/standard/insert/ansi

## standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/text/manager/lists/standard/newid/ansi = mshop/text/manager/lists/standard/newid
```

* Default: mshop/text/manager/lists/standard/newid
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
 SELECT currval('seq_mtexli_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mtexli_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/text/manager/lists/standard/insert/ansi
* mshop/text/manager/lists/standard/update/ansi
* mshop/text/manager/lists/standard/delete/ansi
* mshop/text/manager/lists/standard/search/ansi
* mshop/text/manager/lists/standard/count/ansi
* mshop/text/manager/lists/standard/aggregate/ansi

## standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/text/manager/lists/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/text/manager/lists/standard/newid

See also:

* mshop/text/manager/lists/standard/newid/ansi

## standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/text/manager/lists/standard/search/ansi = 
 SELECT :columns
 	mtexli."id" AS "text.lists.id", mtexli."parentid" AS "text.lists.parentid",
 	mtexli."siteid" AS "text.lists.siteid", mtexli."type" AS "text.lists.type",
 	mtexli."domain" AS "text.lists.domain", mtexli."refid" AS "text.lists.refid",
 	mtexli."start" AS "text.lists.datestart", mtexli."end" AS "text.lists.dateend",
 	mtexli."config" AS "text.lists.config", mtexli."pos" AS "text.lists.position",
 	mtexli."status" AS "text.lists.status", mtexli."mtime" AS "text.lists.mtime",
 	mtexli."editor" AS "text.lists.editor", mtexli."ctime" AS "text.lists.ctime"
 FROM "mshop_text_list" AS mtexli
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/text/manager/lists/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the text
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

* mshop/text/manager/lists/standard/insert/ansi
* mshop/text/manager/lists/standard/update/ansi
* mshop/text/manager/lists/standard/newid/ansi
* mshop/text/manager/lists/standard/delete/ansi
* mshop/text/manager/lists/standard/count/ansi
* mshop/text/manager/lists/standard/aggregate/ansi

## standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/text/manager/lists/standard/search/mysql = 
 SELECT :columns
 	mtexli."id" AS "text.lists.id", mtexli."parentid" AS "text.lists.parentid",
 	mtexli."siteid" AS "text.lists.siteid", mtexli."type" AS "text.lists.type",
 	mtexli."domain" AS "text.lists.domain", mtexli."refid" AS "text.lists.refid",
 	mtexli."start" AS "text.lists.datestart", mtexli."end" AS "text.lists.dateend",
 	mtexli."config" AS "text.lists.config", mtexli."pos" AS "text.lists.position",
 	mtexli."status" AS "text.lists.status", mtexli."mtime" AS "text.lists.mtime",
 	mtexli."editor" AS "text.lists.editor", mtexli."ctime" AS "text.lists.ctime"
 FROM "mshop_text_list" AS mtexli
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mtexli."id" AS "text.lists.id", mtexli."parentid" AS "text.lists.parentid",
 	mtexli."siteid" AS "text.lists.siteid", mtexli."type" AS "text.lists.type",
 	mtexli."domain" AS "text.lists.domain", mtexli."refid" AS "text.lists.refid",
 	mtexli."start" AS "text.lists.datestart", mtexli."end" AS "text.lists.dateend",
 	mtexli."config" AS "text.lists.config", mtexli."pos" AS "text.lists.position",
 	mtexli."status" AS "text.lists.status", mtexli."mtime" AS "text.lists.mtime",
 	mtexli."editor" AS "text.lists.editor", mtexli."ctime" AS "text.lists.ctime"
 FROM "mshop_text_list" AS mtexli
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/text/manager/lists/standard/search/ansi

## standard/update/ansi

Updates an existing text list record in the database

```
mshop/text/manager/lists/standard/update/ansi = 
 UPDATE "mshop_text_list"
 SET :names
 	"parentid"=?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/text/manager/lists/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the text list item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/text/manager/lists/standard/insert/ansi
* mshop/text/manager/lists/standard/newid/ansi
* mshop/text/manager/lists/standard/delete/ansi
* mshop/text/manager/lists/standard/search/ansi
* mshop/text/manager/lists/standard/count/ansi
* mshop/text/manager/lists/standard/aggregate/ansi

## standard/update/mysql

Updates an existing text list record in the database

```
mshop/text/manager/lists/standard/update/mysql = 
 UPDATE "mshop_text_list"
 SET :names
 	"parentid"=?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_text_list"
 SET :names
 	"parentid"=?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/text/manager/lists/standard/update/ansi

## submanagers

List of manager names that can be instantiated by the text list manager

```
mshop/text/manager/lists/submanagers = Array
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

Excludes decorators added by the "common" option from the text list type manager

```
mshop/text/manager/lists/type/decorators/excludes = Array
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
around the text list type manager.

```
 mshop/text/manager/lists/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the text list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/text/manager/lists/type/decorators/global
* mshop/text/manager/lists/type/decorators/local

## type/decorators/global

Adds a list of globally available decorators only to the text list type manager

```
mshop/text/manager/lists/type/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the text list type
manager.

```
 mshop/text/manager/lists/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the text
list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/text/manager/lists/type/decorators/excludes
* mshop/text/manager/lists/type/decorators/local

## type/decorators/local

Adds a list of local decorators only to the text list type manager

```
mshop/text/manager/lists/type/decorators/local = Array
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
("\Aimeos\MShop\Text\Manager\Lists\Type\Decorator\*") around the text
list type manager.

```
 mshop/text/manager/lists/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Text\Manager\Lists\Type\Decorator\Decorator2" only to
the text list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/text/manager/lists/type/decorators/excludes
* mshop/text/manager/lists/type/decorators/global

## type/name

Class name of the used text list type manager implementation

```
mshop/text/manager/lists/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default text list type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Text\Manager\Lists\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Text\Manager\Lists\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/text/manager/lists/type/name = Mytype
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
mshop/text/manager/lists/type/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mtexlity."id"
 	FROM "mshop_text_list_type" as mtexlity
 	:joins
 	WHERE :cond
 	ORDER BY mtexlity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/text/manager/lists/type/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the text
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

* mshop/text/manager/lists/type/standard/insert/ansi
* mshop/text/manager/lists/type/standard/update/ansi
* mshop/text/manager/lists/type/standard/newid/ansi
* mshop/text/manager/lists/type/standard/delete/ansi
* mshop/text/manager/lists/type/standard/search/ansi

## type/standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/text/manager/lists/type/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mtexlity."id"
 	FROM "mshop_text_list_type" as mtexlity
 	:joins
 	WHERE :cond
 	ORDER BY mtexlity."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mtexlity."id"
 	FROM "mshop_text_list_type" as mtexlity
 	:joins
 	WHERE :cond
 	ORDER BY mtexlity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/text/manager/lists/type/standard/count/ansi

## type/standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/text/manager/lists/type/standard/delete/ansi = 
 DELETE FROM "mshop_text_list_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/text/manager/lists/type/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the text database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/text/manager/lists/type/standard/insert/ansi
* mshop/text/manager/lists/type/standard/update/ansi
* mshop/text/manager/lists/type/standard/newid/ansi
* mshop/text/manager/lists/type/standard/search/ansi
* mshop/text/manager/lists/type/standard/count/ansi

## type/standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/text/manager/lists/type/standard/delete/mysql = 
 DELETE FROM "mshop_text_list_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_text_list_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/text/manager/lists/type/standard/delete/ansi

## type/standard/insert/ansi

Inserts a new text list type record into the database table

```
mshop/text/manager/lists/type/standard/insert/ansi = 
 INSERT INTO "mshop_text_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/text/manager/lists/type/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the text list type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/text/manager/lists/type/standard/update/ansi
* mshop/text/manager/lists/type/standard/newid/ansi
* mshop/text/manager/lists/type/standard/delete/ansi
* mshop/text/manager/lists/type/standard/search/ansi
* mshop/text/manager/lists/type/standard/count/ansi

## type/standard/insert/mysql

Inserts a new text list type record into the database table

```
mshop/text/manager/lists/type/standard/insert/mysql = 
 INSERT INTO "mshop_text_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_text_list_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/text/manager/lists/type/standard/insert/ansi

## type/standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/text/manager/lists/type/standard/newid/ansi = mshop/text/manager/lists/type/standard/newid
```

* Default: mshop/text/manager/lists/type/standard/newid
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
 SELECT currval('seq_mtexlity_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mtexlity_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/text/manager/lists/type/standard/insert/ansi
* mshop/text/manager/lists/type/standard/update/ansi
* mshop/text/manager/lists/type/standard/delete/ansi
* mshop/text/manager/lists/type/standard/search/ansi
* mshop/text/manager/lists/type/standard/count/ansi

## type/standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/text/manager/lists/type/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/text/manager/lists/type/standard/newid

See also:

* mshop/text/manager/lists/type/standard/newid/ansi

## type/standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/text/manager/lists/type/standard/search/ansi = 
 SELECT :columns
 	mtexlity."id" AS "text.lists.type.id", mtexlity."siteid" AS "text.lists.type.siteid",
 	mtexlity."code" AS "text.lists.type.code", mtexlity."domain" AS "text.lists.type.domain",
 	mtexlity."label" AS "text.lists.type.label", mtexlity."status" AS "text.lists.type.status",
 	mtexlity."mtime" AS "text.lists.type.mtime", mtexlity."editor" AS "text.lists.type.editor",
 	mtexlity."ctime" AS "text.lists.type.ctime", mtexlity."pos" AS "text.lists.type.position"
 FROM "mshop_text_list_type" AS mtexlity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/text/manager/lists/type/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the text
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

* mshop/text/manager/lists/type/standard/insert/ansi
* mshop/text/manager/lists/type/standard/update/ansi
* mshop/text/manager/lists/type/standard/newid/ansi
* mshop/text/manager/lists/type/standard/delete/ansi
* mshop/text/manager/lists/type/standard/count/ansi

## type/standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/text/manager/lists/type/standard/search/mysql = 
 SELECT :columns
 	mtexlity."id" AS "text.lists.type.id", mtexlity."siteid" AS "text.lists.type.siteid",
 	mtexlity."code" AS "text.lists.type.code", mtexlity."domain" AS "text.lists.type.domain",
 	mtexlity."label" AS "text.lists.type.label", mtexlity."status" AS "text.lists.type.status",
 	mtexlity."mtime" AS "text.lists.type.mtime", mtexlity."editor" AS "text.lists.type.editor",
 	mtexlity."ctime" AS "text.lists.type.ctime", mtexlity."pos" AS "text.lists.type.position"
 FROM "mshop_text_list_type" AS mtexlity
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mtexlity."id" AS "text.lists.type.id", mtexlity."siteid" AS "text.lists.type.siteid",
 	mtexlity."code" AS "text.lists.type.code", mtexlity."domain" AS "text.lists.type.domain",
 	mtexlity."label" AS "text.lists.type.label", mtexlity."status" AS "text.lists.type.status",
 	mtexlity."mtime" AS "text.lists.type.mtime", mtexlity."editor" AS "text.lists.type.editor",
 	mtexlity."ctime" AS "text.lists.type.ctime", mtexlity."pos" AS "text.lists.type.position"
 FROM "mshop_text_list_type" AS mtexlity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/text/manager/lists/type/standard/search/ansi

## type/standard/update/ansi

Updates an existing text list type record in the database

```
mshop/text/manager/lists/type/standard/update/ansi = 
 UPDATE "mshop_text_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/text/manager/lists/type/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the text list type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/text/manager/lists/type/standard/insert/ansi
* mshop/text/manager/lists/type/standard/newid/ansi
* mshop/text/manager/lists/type/standard/delete/ansi
* mshop/text/manager/lists/type/standard/search/ansi
* mshop/text/manager/lists/type/standard/count/ansi

## type/standard/update/mysql

Updates an existing text list type record in the database

```
mshop/text/manager/lists/type/standard/update/mysql = 
 UPDATE "mshop_text_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_text_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/text/manager/lists/type/standard/update/ansi

## type/submanagers

List of manager names that can be instantiated by the text list type manager

```
mshop/text/manager/lists/type/submanagers = Array
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

Class name of the used text manager implementation

```
mshop/text/manager/name = Standard
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
 \Aimeos\MShop\Text\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Text\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/text/manager/name = Mymanager
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
mshop/text/manager/sitemode = 3
```

* Default: 3
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole text domain if items from parent sites are inherited,
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
mshop/text/manager/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mtex."id"
 	FROM "mshop_text" AS mtex
 	:joins
 	WHERE :cond
 	GROUP BY mtex."id"
 	ORDER BY mtex."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/text/manager/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the text
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

* mshop/text/manager/standard/insert/ansi
* mshop/text/manager/standard/update/ansi
* mshop/text/manager/standard/newid/ansi
* mshop/text/manager/standard/delete/ansi
* mshop/text/manager/standard/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/text/manager/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mtex."id"
 	FROM "mshop_text" AS mtex
 	:joins
 	WHERE :cond
 	GROUP BY mtex."id"
 	ORDER BY mtex."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mtex."id"
 	FROM "mshop_text" AS mtex
 	:joins
 	WHERE :cond
 	GROUP BY mtex."id"
 	ORDER BY mtex."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/text/manager/standard/count/ansi

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/text/manager/standard/delete/ansi = 
 DELETE FROM "mshop_text"
 WHERE :cond AND siteid = ?
```

* Default: mshop/text/manager/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the text database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/text/manager/standard/insert/ansi
* mshop/text/manager/standard/update/ansi
* mshop/text/manager/standard/newid/ansi
* mshop/text/manager/standard/search/ansi
* mshop/text/manager/standard/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/text/manager/standard/delete/mysql = 
 DELETE FROM "mshop_text"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_text"
 WHERE :cond AND siteid = ?


See also:

* mshop/text/manager/standard/delete/ansi

## insert/ansi

Inserts a new text record into the database table

```
mshop/text/manager/standard/insert/ansi = 
 INSERT INTO "mshop_text" ( :names
 	"langid", "type", "domain", "label", "content",
 	"status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/text/manager/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the text item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/text/manager/standard/update/ansi
* mshop/text/manager/standard/newid/ansi
* mshop/text/manager/standard/delete/ansi
* mshop/text/manager/standard/search/ansi
* mshop/text/manager/standard/count/ansi

## insert/mysql

Inserts a new text record into the database table

```
mshop/text/manager/standard/insert/mysql = 
 INSERT INTO "mshop_text" ( :names
 	"langid", "type", "domain", "label", "content",
 	"status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_text" ( :names
 	"langid", "type", "domain", "label", "content",
 	"status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/text/manager/standard/insert/ansi

## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/text/manager/standard/newid/ansi = mshop/text/manager/standard/newid
```

* Default: mshop/text/manager/standard/newid
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
 SELECT currval('seq_mtex_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mtex_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/text/manager/standard/insert/ansi
* mshop/text/manager/standard/update/ansi
* mshop/text/manager/standard/delete/ansi
* mshop/text/manager/standard/search/ansi
* mshop/text/manager/standard/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/text/manager/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/text/manager/standard/newid

See also:

* mshop/text/manager/standard/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/text/manager/standard/search/ansi = 
 SELECT :columns
 	mtex."id" AS "text.id", mtex."siteid" AS "text.siteid",
 	mtex."langid" AS "text.languageid",	mtex."type" AS "text.type",
 	mtex."domain" AS "text.domain", mtex."label" AS "text.label",
 	mtex."content" AS "text.content", mtex."status" AS "text.status",
 	mtex."mtime" AS "text.mtime", mtex."editor" AS "text.editor",
 	mtex."ctime" AS "text.ctime"
 FROM "mshop_text" AS mtex
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mtex."id", mtex."siteid", mtex."langid",	mtex."type", mtex."domain", mtex."label",
 	mtex."content", mtex."status", mtex."mtime", mtex."editor", mtex."ctime"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/text/manager/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the text
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

* mshop/text/manager/standard/insert/ansi
* mshop/text/manager/standard/update/ansi
* mshop/text/manager/standard/newid/ansi
* mshop/text/manager/standard/delete/ansi
* mshop/text/manager/standard/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/text/manager/standard/search/mysql = 
 SELECT :columns
 	mtex."id" AS "text.id", mtex."siteid" AS "text.siteid",
 	mtex."langid" AS "text.languageid",	mtex."type" AS "text.type",
 	mtex."domain" AS "text.domain", mtex."label" AS "text.label",
 	mtex."content" AS "text.content", mtex."status" AS "text.status",
 	mtex."mtime" AS "text.mtime", mtex."editor" AS "text.editor",
 	mtex."ctime" AS "text.ctime"
 FROM "mshop_text" AS mtex
 :joins
 WHERE :cond
 GROUP BY :group mtex."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mtex."id" AS "text.id", mtex."siteid" AS "text.siteid",
 	mtex."langid" AS "text.languageid",	mtex."type" AS "text.type",
 	mtex."domain" AS "text.domain", mtex."label" AS "text.label",
 	mtex."content" AS "text.content", mtex."status" AS "text.status",
 	mtex."mtime" AS "text.mtime", mtex."editor" AS "text.editor",
 	mtex."ctime" AS "text.ctime"
 FROM "mshop_text" AS mtex
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mtex."id", mtex."siteid", mtex."langid",	mtex."type", mtex."domain", mtex."label",
 	mtex."content", mtex."status", mtex."mtime", mtex."editor", mtex."ctime"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/text/manager/standard/search/ansi

## update/ansi

Updates an existing text record in the database

```
mshop/text/manager/standard/update/ansi = 
 UPDATE "mshop_text"
 SET :names
 	"langid" = ?, "type" = ?, "domain" = ?, "label" = ?,
 	"content" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/text/manager/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the text item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/text/manager/standard/insert/ansi
* mshop/text/manager/standard/newid/ansi
* mshop/text/manager/standard/delete/ansi
* mshop/text/manager/standard/search/ansi
* mshop/text/manager/standard/count/ansi

## update/mysql

Updates an existing text record in the database

```
mshop/text/manager/standard/update/mysql = 
 UPDATE "mshop_text"
 SET :names
 	"langid" = ?, "type" = ?, "domain" = ?, "label" = ?,
 	"content" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_text"
 SET :names
 	"langid" = ?, "type" = ?, "domain" = ?, "label" = ?,
 	"content" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/text/manager/standard/update/ansi

# submanagers

List of manager names that can be instantiated by the text manager

```
mshop/text/manager/submanagers = Array
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

Excludes decorators added by the "common" option from the text type manager

```
mshop/text/manager/type/decorators/excludes = Array
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
around the text type manager.

```
 mshop/text/manager/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the text type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/text/manager/type/decorators/global
* mshop/text/manager/type/decorators/local

## decorators/global

Adds a list of globally available decorators only to the text type manager

```
mshop/text/manager/type/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the text type manager.

```
 mshop/text/manager/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the text
type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/text/manager/type/decorators/excludes
* mshop/text/manager/type/decorators/local

## decorators/local

Adds a list of local decorators only to the text type manager

```
mshop/text/manager/type/decorators/local = Array
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
("\Aimeos\MShop\Text\Manager\Type\Decorator\*") around the text type
manager.

```
 mshop/text/manager/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Text\Manager\Type\Decorator\Decorator2" only to the text
type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/text/manager/type/decorators/excludes
* mshop/text/manager/type/decorators/global

## name

Class name of the used text type manager implementation

```
mshop/text/manager/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default text type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Text\Manager\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Text\Manager\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/text/manager/type/name = Mytype
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
mshop/text/manager/type/standard/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mtexty."id"
 	FROM "mshop_text_type" mtexty
 	:joins
 	WHERE :cond
 	ORDER BY mtexty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/text/manager/type/standard/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the text
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

* mshop/text/manager/type/standard/insert/ansi
* mshop/text/manager/type/standard/update/ansi
* mshop/text/manager/type/standard/newid/ansi
* mshop/text/manager/type/standard/delete/ansi
* mshop/text/manager/type/standard/search/ansi

## standard/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/text/manager/type/standard/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mtexty."id"
 	FROM "mshop_text_type" mtexty
 	:joins
 	WHERE :cond
 	ORDER BY mtexty."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mtexty."id"
 	FROM "mshop_text_type" mtexty
 	:joins
 	WHERE :cond
 	ORDER BY mtexty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/text/manager/type/standard/count/ansi

## standard/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/text/manager/type/standard/delete/ansi = 
 DELETE FROM "mshop_text_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/text/manager/type/standard/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the text database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/text/manager/type/standard/insert/ansi
* mshop/text/manager/type/standard/update/ansi
* mshop/text/manager/type/standard/newid/ansi
* mshop/text/manager/type/standard/search/ansi
* mshop/text/manager/type/standard/count/ansi

## standard/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/text/manager/type/standard/delete/mysql = 
 DELETE FROM "mshop_text_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_text_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/text/manager/type/standard/delete/ansi

## standard/insert/ansi

Inserts a new text type record into the database table

```
mshop/text/manager/type/standard/insert/ansi = 
 INSERT INTO "mshop_text_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/text/manager/type/standard/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the text type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the saveItems() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/text/manager/type/standard/update/ansi
* mshop/text/manager/type/standard/newid/ansi
* mshop/text/manager/type/standard/delete/ansi
* mshop/text/manager/type/standard/search/ansi
* mshop/text/manager/type/standard/count/ansi

## standard/insert/mysql

Inserts a new text type record into the database table

```
mshop/text/manager/type/standard/insert/mysql = 
 INSERT INTO "mshop_text_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_text_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/text/manager/type/standard/insert/ansi

## standard/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/text/manager/type/standard/newid/ansi = mshop/text/manager/type/standard/newid
```

* Default: mshop/text/manager/type/standard/newid
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
 SELECT currval('seq_mtexty_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mtexty_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/text/manager/type/standard/insert/ansi
* mshop/text/manager/type/standard/update/ansi
* mshop/text/manager/type/standard/delete/ansi
* mshop/text/manager/type/standard/search/ansi
* mshop/text/manager/type/standard/count/ansi

## standard/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/text/manager/type/standard/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/text/manager/type/standard/newid

See also:

* mshop/text/manager/type/standard/newid/ansi

## standard/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/text/manager/type/standard/search/ansi = 
 SELECT :columns
 	mtexty."id" AS "text.type.id", mtexty."siteid" AS "text.type.siteid",
 	mtexty."code" AS "text.type.code", mtexty."domain" AS "text.type.domain",
 	mtexty."label" AS "text.type.label", mtexty."status" AS "text.type.status",
 	mtexty."mtime" AS "text.type.mtime", mtexty."editor" AS "text.type.editor",
 	mtexty."ctime" AS "text.type.ctime", mtexty."pos" AS "text.type.position"
 FROM "mshop_text_type" mtexty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/text/manager/type/standard/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the text
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

* mshop/text/manager/type/standard/insert/ansi
* mshop/text/manager/type/standard/update/ansi
* mshop/text/manager/type/standard/newid/ansi
* mshop/text/manager/type/standard/delete/ansi
* mshop/text/manager/type/standard/count/ansi

## standard/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/text/manager/type/standard/search/mysql = 
 SELECT :columns
 	mtexty."id" AS "text.type.id", mtexty."siteid" AS "text.type.siteid",
 	mtexty."code" AS "text.type.code", mtexty."domain" AS "text.type.domain",
 	mtexty."label" AS "text.type.label", mtexty."status" AS "text.type.status",
 	mtexty."mtime" AS "text.type.mtime", mtexty."editor" AS "text.type.editor",
 	mtexty."ctime" AS "text.type.ctime", mtexty."pos" AS "text.type.position"
 FROM "mshop_text_type" mtexty
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mtexty."id" AS "text.type.id", mtexty."siteid" AS "text.type.siteid",
 	mtexty."code" AS "text.type.code", mtexty."domain" AS "text.type.domain",
 	mtexty."label" AS "text.type.label", mtexty."status" AS "text.type.status",
 	mtexty."mtime" AS "text.type.mtime", mtexty."editor" AS "text.type.editor",
 	mtexty."ctime" AS "text.type.ctime", mtexty."pos" AS "text.type.position"
 FROM "mshop_text_type" mtexty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/text/manager/type/standard/search/ansi

## standard/update/ansi

Updates an existing text type record in the database

```
mshop/text/manager/type/standard/update/ansi = 
 UPDATE "mshop_text_type"
 SET :names
 	"code"=?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?,"mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/text/manager/type/standard/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the text type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the saveItems() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/text/manager/type/standard/insert/ansi
* mshop/text/manager/type/standard/newid/ansi
* mshop/text/manager/type/standard/delete/ansi
* mshop/text/manager/type/standard/search/ansi
* mshop/text/manager/type/standard/count/ansi

## standard/update/mysql

Updates an existing text type record in the database

```
mshop/text/manager/type/standard/update/mysql = 
 UPDATE "mshop_text_type"
 SET :names
 	"code"=?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?,"mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_text_type"
 SET :names
 	"code"=?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?,"mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/text/manager/type/standard/update/ansi

## submanagers

List of manager names that can be instantiated by the text type manager

```
mshop/text/manager/type/submanagers = Array
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
