
# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/attribute/manager/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT matt."id"
 	FROM "mshop_attribute" AS matt
 	:joins
 	WHERE :cond
 	GROUP BY matt."id"
 	ORDER BY matt."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/attribute/manager/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the attribute
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

* mshop/attribute/manager/insert/ansi
* mshop/attribute/manager/update/ansi
* mshop/attribute/manager/newid/ansi
* mshop/attribute/manager/delete/ansi
* mshop/attribute/manager/search/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/attribute/manager/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT matt."id"
 	FROM "mshop_attribute" AS matt
 	:joins
 	WHERE :cond
 	GROUP BY matt."id"
 	ORDER BY matt."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT matt."id"
 	FROM "mshop_attribute" AS matt
 	:joins
 	WHERE :cond
 	GROUP BY matt."id"
 	ORDER BY matt."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/attribute/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the attribute manager

```
mshop/attribute/manager/decorators/excludes = Array
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
around the attribute manager.

```
 mshop/attribute/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/decorators/global
* mshop/attribute/manager/decorators/local

## global

Adds a list of globally available decorators only to the attribute manager

```
mshop/attribute/manager/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the attribute manager.

```
 mshop/attribute/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the attribute controller.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/decorators/excludes
* mshop/attribute/manager/decorators/local

## local

Adds a list of local decorators only to the attribute manager

```
mshop/attribute/manager/decorators/local = Array
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
("\Aimeos\MShop\Attribute\Manager\Decorator\*") around the attribute manager.

```
 mshop/attribute/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Attribute\Manager\Decorator\Decorator2" only to the attribute
controller.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/decorators/excludes
* mshop/attribute/manager/decorators/global

# delete
## ansi

Deletes the items matched by the given IDs from the database

```
mshop/attribute/manager/delete/ansi = 
 DELETE FROM "mshop_attribute"
 WHERE :cond AND siteid = ?
```

* Default: mshop/attribute/manager/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the attribute database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/insert/ansi
* mshop/attribute/manager/update/ansi
* mshop/attribute/manager/newid/ansi
* mshop/attribute/manager/search/ansi
* mshop/attribute/manager/count/ansi

## mysql

Deletes the items matched by the given IDs from the database

```
mshop/attribute/manager/delete/mysql = 
 DELETE FROM "mshop_attribute"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_attribute"
 WHERE :cond AND siteid = ?


See also:

* mshop/attribute/manager/delete/ansi

# insert
## ansi

Inserts a new attribute record into the database table

```
mshop/attribute/manager/insert/ansi = 
 INSERT INTO "mshop_attribute" ( :names
 	"key", "type", "domain", "code", "status", "pos",
 	"label", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/attribute/manager/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the attribute item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/update/ansi
* mshop/attribute/manager/newid/ansi
* mshop/attribute/manager/delete/ansi
* mshop/attribute/manager/search/ansi
* mshop/attribute/manager/count/ansi

## mysql

Inserts a new attribute record into the database table

```
mshop/attribute/manager/insert/mysql = 
 INSERT INTO "mshop_attribute" ( :names
 	"key", "type", "domain", "code", "status", "pos",
 	"label", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_attribute" ( :names
 	"key", "type", "domain", "code", "status", "pos",
 	"label", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/attribute/manager/insert/ansi

# lists
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/attribute/manager/lists/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_attribute_list" AS mattli
 	:joins
 	WHERE :cond
 	GROUP BY :cols, mattli."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/attribute/manager/lists/aggregate
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

* mshop/attribute/manager/lists/insert/ansi
* mshop/attribute/manager/lists/update/ansi
* mshop/attribute/manager/lists/newid/ansi
* mshop/attribute/manager/lists/delete/ansi
* mshop/attribute/manager/lists/search/ansi
* mshop/attribute/manager/lists/count/ansi

## aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/attribute/manager/lists/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_attribute_list" AS mattli
 	:joins
 	WHERE :cond
 	GROUP BY :cols, mattli."id"
 	ORDER BY :order
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_attribute_list" AS mattli
 	:joins
 	WHERE :cond
 	GROUP BY :cols, mattli."id"
 	ORDER BY :order
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/attribute/manager/lists/aggregate/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/attribute/manager/lists/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattli."id"
 	FROM "mshop_attribute_list" AS mattli
 	:joins
 	WHERE :cond
 	ORDER BY mattli."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/attribute/manager/lists/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the attribute
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

* mshop/attribute/manager/lists/insert/ansi
* mshop/attribute/manager/lists/update/ansi
* mshop/attribute/manager/lists/newid/ansi
* mshop/attribute/manager/lists/delete/ansi
* mshop/attribute/manager/lists/search/ansi
* mshop/attribute/manager/lists/aggregate/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/attribute/manager/lists/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattli."id"
 	FROM "mshop_attribute_list" AS mattli
 	:joins
 	WHERE :cond
 	ORDER BY mattli."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattli."id"
 	FROM "mshop_attribute_list" AS mattli
 	:joins
 	WHERE :cond
 	ORDER BY mattli."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/attribute/manager/lists/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the attribute list manager

```
mshop/attribute/manager/lists/decorators/excludes = Array
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
around the attribute list manager.

```
 mshop/attribute/manager/lists/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the attribute list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/lists/decorators/global
* mshop/attribute/manager/lists/decorators/local

## decorators/global

Adds a list of globally available decorators only to the attribute list manager

```
mshop/attribute/manager/lists/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the attribute list
manager.

```
 mshop/attribute/manager/lists/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the attribute
list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/lists/decorators/excludes
* mshop/attribute/manager/lists/decorators/local

## decorators/local

Adds a list of local decorators only to the attribute list manager

```
mshop/attribute/manager/lists/decorators/local = Array
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
("\Aimeos\MShop\Attribute\Manager\Lists\Decorator\*") around the attribute
list manager.

```
 mshop/attribute/manager/lists/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Attribute\Manager\Lists\Decorator\Decorator2" only to the
attribute list manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/lists/decorators/excludes
* mshop/attribute/manager/lists/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/attribute/manager/lists/delete/ansi = 
 DELETE FROM "mshop_attribute_list"
 WHERE :cond AND siteid = ?
```

* Default: mshop/attribute/manager/lists/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the attribute database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/lists/insert/ansi
* mshop/attribute/manager/lists/update/ansi
* mshop/attribute/manager/lists/newid/ansi
* mshop/attribute/manager/lists/search/ansi
* mshop/attribute/manager/lists/count/ansi
* mshop/attribute/manager/lists/aggregate/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/attribute/manager/lists/delete/mysql = 
 DELETE FROM "mshop_attribute_list"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_attribute_list"
 WHERE :cond AND siteid = ?


See also:

* mshop/attribute/manager/lists/delete/ansi

## insert/ansi

Inserts a new attribute list record into the database table

```
mshop/attribute/manager/lists/insert/ansi = 
 INSERT INTO "mshop_attribute_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/attribute/manager/lists/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the attribute list item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/lists/update/ansi
* mshop/attribute/manager/lists/newid/ansi
* mshop/attribute/manager/lists/delete/ansi
* mshop/attribute/manager/lists/search/ansi
* mshop/attribute/manager/lists/count/ansi
* mshop/attribute/manager/lists/aggregate/ansi

## insert/mysql

Inserts a new attribute list record into the database table

```
mshop/attribute/manager/lists/insert/mysql = 
 INSERT INTO "mshop_attribute_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_attribute_list" ( :names
 	"parentid", "key", "type", "domain", "refid", "start", "end",
 	"config", "pos", "status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/attribute/manager/lists/insert/ansi

## name

Class name of the used attribute list manager implementation

```
mshop/attribute/manager/lists/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default attribute list manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Attribute\Manager\Lists\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Attribute\Manager\Lists\Mylist
```

then you have to set the this configuration option:

```
 mshop/attribute/manager/lists/name = Mylist
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyList"!


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/attribute/manager/lists/newid/ansi = mshop/attribute/manager/lists/newid
```

* Default: mshop/attribute/manager/lists/newid
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
 SELECT currval('seq_mattlity_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mattlity_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/attribute/manager/lists/insert/ansi
* mshop/attribute/manager/lists/update/ansi
* mshop/attribute/manager/lists/delete/ansi
* mshop/attribute/manager/lists/search/ansi
* mshop/attribute/manager/lists/count/ansi
* mshop/attribute/manager/lists/aggregate/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/attribute/manager/lists/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/attribute/manager/lists/newid

See also:

* mshop/attribute/manager/lists/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/attribute/manager/lists/search/ansi = 
 SELECT :columns
 	mattli."id" AS "attribute.lists.id", mattli."siteid" AS "attribute.lists.siteid",
 	mattli."parentid" AS "attribute.lists.parentid", mattli."type" AS "attribute.lists.type",
 	mattli."domain" AS "attribute.lists.domain", mattli."refid" AS "attribute.lists.refid",
 	mattli."start" AS "attribute.lists.datestart", mattli."end" AS "attribute.lists.dateend",
 	mattli."config" AS "attribute.lists.config", mattli."pos" AS "attribute.lists.position",
 	mattli."status" AS "attribute.lists.status", mattli."mtime" AS "attribute.lists.mtime",
 	mattli."ctime" AS "attribute.lists.ctime", mattli."editor" AS "attribute.lists.editor"
 FROM "mshop_attribute_list" AS mattli
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/attribute/manager/lists/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the attribute
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

* mshop/attribute/manager/lists/insert/ansi
* mshop/attribute/manager/lists/update/ansi
* mshop/attribute/manager/lists/newid/ansi
* mshop/attribute/manager/lists/delete/ansi
* mshop/attribute/manager/lists/count/ansi
* mshop/attribute/manager/lists/aggregate/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/attribute/manager/lists/search/mysql = 
 SELECT :columns
 	mattli."id" AS "attribute.lists.id", mattli."siteid" AS "attribute.lists.siteid",
 	mattli."parentid" AS "attribute.lists.parentid", mattli."type" AS "attribute.lists.type",
 	mattli."domain" AS "attribute.lists.domain", mattli."refid" AS "attribute.lists.refid",
 	mattli."start" AS "attribute.lists.datestart", mattli."end" AS "attribute.lists.dateend",
 	mattli."config" AS "attribute.lists.config", mattli."pos" AS "attribute.lists.position",
 	mattli."status" AS "attribute.lists.status", mattli."mtime" AS "attribute.lists.mtime",
 	mattli."ctime" AS "attribute.lists.ctime", mattli."editor" AS "attribute.lists.editor"
 FROM "mshop_attribute_list" AS mattli
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mattli."id" AS "attribute.lists.id", mattli."siteid" AS "attribute.lists.siteid",
 	mattli."parentid" AS "attribute.lists.parentid", mattli."type" AS "attribute.lists.type",
 	mattli."domain" AS "attribute.lists.domain", mattli."refid" AS "attribute.lists.refid",
 	mattli."start" AS "attribute.lists.datestart", mattli."end" AS "attribute.lists.dateend",
 	mattli."config" AS "attribute.lists.config", mattli."pos" AS "attribute.lists.position",
 	mattli."status" AS "attribute.lists.status", mattli."mtime" AS "attribute.lists.mtime",
 	mattli."ctime" AS "attribute.lists.ctime", mattli."editor" AS "attribute.lists.editor"
 FROM "mshop_attribute_list" AS mattli
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/attribute/manager/lists/search/ansi

## submanagers

List of manager names that can be instantiated by the attribute list manager

```
mshop/attribute/manager/lists/submanagers = Array
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


## type/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/attribute/manager/lists/type/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattlity."id"
 	FROM "mshop_attribute_list_type" AS mattlity
 	:joins
 	WHERE :cond
 	ORDER BY mattlity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/attribute/manager/lists/type/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the attribute
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

* mshop/attribute/manager/lists/type/insert/ansi
* mshop/attribute/manager/lists/type/update/ansi
* mshop/attribute/manager/lists/type/newid/ansi
* mshop/attribute/manager/lists/type/delete/ansi
* mshop/attribute/manager/lists/type/search/ansi

## type/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/attribute/manager/lists/type/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattlity."id"
 	FROM "mshop_attribute_list_type" AS mattlity
 	:joins
 	WHERE :cond
 	ORDER BY mattlity."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattlity."id"
 	FROM "mshop_attribute_list_type" AS mattlity
 	:joins
 	WHERE :cond
 	ORDER BY mattlity."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/attribute/manager/lists/type/count/ansi

## type/decorators/excludes

Excludes decorators added by the "common" option from the attribute list type manager

```
mshop/attribute/manager/lists/type/decorators/excludes = Array
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
around the attribute list type manager.

```
 mshop/attribute/manager/lists/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the attribute list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/lists/type/decorators/global
* mshop/attribute/manager/lists/type/decorators/local

## type/decorators/global

Adds a list of globally available decorators only to the attribute list type manager

```
mshop/attribute/manager/lists/type/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the attribute list
type manager.

```
 mshop/attribute/manager/lists/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the attribute
list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/lists/type/decorators/excludes
* mshop/attribute/manager/lists/type/decorators/local

## type/decorators/local

Adds a list of local decorators only to the attribute list type manager

```
mshop/attribute/manager/lists/type/decorators/local = Array
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
("\Aimeos\MShop\Attribute\Manager\Lists\Type\Decorator\*") around the
attribute list type manager.

```
 mshop/attribute/manager/lists/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Attribute\Manager\Lists\Type\Decorator\Decorator2" only
to the attribute list type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/lists/type/decorators/excludes
* mshop/attribute/manager/lists/type/decorators/global

## type/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/attribute/manager/lists/type/delete/ansi = 
 DELETE FROM "mshop_attribute_list_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/attribute/manager/lists/type/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the attribute database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/lists/type/insert/ansi
* mshop/attribute/manager/lists/type/update/ansi
* mshop/attribute/manager/lists/type/newid/ansi
* mshop/attribute/manager/lists/type/search/ansi
* mshop/attribute/manager/lists/type/count/ansi

## type/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/attribute/manager/lists/type/delete/mysql = 
 DELETE FROM "mshop_attribute_list_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_attribute_list_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/attribute/manager/lists/type/delete/ansi

## type/insert/ansi

Inserts a new attribute list type record into the database table

```
mshop/attribute/manager/lists/type/insert/ansi = 
 INSERT INTO "mshop_attribute_list_type"( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime","editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/attribute/manager/lists/type/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the attribute list type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/lists/type/update/ansi
* mshop/attribute/manager/lists/type/newid/ansi
* mshop/attribute/manager/lists/type/delete/ansi
* mshop/attribute/manager/lists/type/search/ansi
* mshop/attribute/manager/lists/type/count/ansi

## type/insert/mysql

Inserts a new attribute list type record into the database table

```
mshop/attribute/manager/lists/type/insert/mysql = 
 INSERT INTO "mshop_attribute_list_type"( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime","editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_attribute_list_type"( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime","editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/attribute/manager/lists/type/insert/ansi

## type/name

Class name of the used attribute list type manager implementation

```
mshop/attribute/manager/lists/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default attribute list type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Attribute\Manager\Lists\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Attribute\Manager\Lists\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/attribute/manager/lists/type/name = Mytype
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyType"!


## type/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/attribute/manager/lists/type/newid/ansi = mshop/attribute/manager/lists/type/newid
```

* Default: mshop/attribute/manager/lists/type/newid
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
 SELECT currval('seq_mattlity_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mattlity_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/attribute/manager/lists/type/insert/ansi
* mshop/attribute/manager/lists/type/update/ansi
* mshop/attribute/manager/lists/type/delete/ansi
* mshop/attribute/manager/lists/type/search/ansi
* mshop/attribute/manager/lists/type/count/ansi

## type/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/attribute/manager/lists/type/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/attribute/manager/lists/type/newid

See also:

* mshop/attribute/manager/lists/type/newid/ansi

## type/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/attribute/manager/lists/type/search/ansi = 
 SELECT :columns
 	mattlity."id" AS "attribute.lists.type.id", mattlity."siteid" AS "attribute.lists.type.siteid",
 	mattlity."code" AS "attribute.lists.type.code", mattlity."domain" AS "attribute.lists.type.domain",
 	mattlity."label" AS "attribute.lists.type.label", mattlity."status" AS "attribute.lists.type.status",
 	mattlity."mtime" AS "attribute.lists.type.mtime", mattlity."ctime" AS "attribute.lists.type.ctime",
 	mattlity."editor" AS "attribute.lists.type.editor", mattlity."pos" AS "attribute.lists.type.position"
 FROM "mshop_attribute_list_type" AS mattlity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/attribute/manager/lists/type/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the attribute
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

* mshop/attribute/manager/lists/type/insert/ansi
* mshop/attribute/manager/lists/type/update/ansi
* mshop/attribute/manager/lists/type/newid/ansi
* mshop/attribute/manager/lists/type/delete/ansi
* mshop/attribute/manager/lists/type/count/ansi

## type/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/attribute/manager/lists/type/search/mysql = 
 SELECT :columns
 	mattlity."id" AS "attribute.lists.type.id", mattlity."siteid" AS "attribute.lists.type.siteid",
 	mattlity."code" AS "attribute.lists.type.code", mattlity."domain" AS "attribute.lists.type.domain",
 	mattlity."label" AS "attribute.lists.type.label", mattlity."status" AS "attribute.lists.type.status",
 	mattlity."mtime" AS "attribute.lists.type.mtime", mattlity."ctime" AS "attribute.lists.type.ctime",
 	mattlity."editor" AS "attribute.lists.type.editor", mattlity."pos" AS "attribute.lists.type.position"
 FROM "mshop_attribute_list_type" AS mattlity
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mattlity."id" AS "attribute.lists.type.id", mattlity."siteid" AS "attribute.lists.type.siteid",
 	mattlity."code" AS "attribute.lists.type.code", mattlity."domain" AS "attribute.lists.type.domain",
 	mattlity."label" AS "attribute.lists.type.label", mattlity."status" AS "attribute.lists.type.status",
 	mattlity."mtime" AS "attribute.lists.type.mtime", mattlity."ctime" AS "attribute.lists.type.ctime",
 	mattlity."editor" AS "attribute.lists.type.editor", mattlity."pos" AS "attribute.lists.type.position"
 FROM "mshop_attribute_list_type" AS mattlity
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/attribute/manager/lists/type/search/ansi

## type/submanagers

List of manager names that can be instantiated by the attribute list type manager

```
mshop/attribute/manager/lists/type/submanagers = Array
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


## type/update/ansi

Updates an existing attribute list type record in the database

```
mshop/attribute/manager/lists/type/update/ansi = 
 UPDATE "mshop_attribute_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/attribute/manager/lists/type/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the attribute list type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/lists/type/insert/ansi
* mshop/attribute/manager/lists/type/newid/ansi
* mshop/attribute/manager/lists/type/delete/ansi
* mshop/attribute/manager/lists/type/search/ansi
* mshop/attribute/manager/lists/type/count/ansi

## type/update/mysql

Updates an existing attribute list type record in the database

```
mshop/attribute/manager/lists/type/update/mysql = 
 UPDATE "mshop_attribute_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_attribute_list_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/attribute/manager/lists/type/update/ansi

## update/ansi

Updates an existing attribute list record in the database

```
mshop/attribute/manager/lists/update/ansi = 
 UPDATE "mshop_attribute_list"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/attribute/manager/lists/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the attribute list item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/lists/insert/ansi
* mshop/attribute/manager/lists/newid/ansi
* mshop/attribute/manager/lists/delete/ansi
* mshop/attribute/manager/lists/search/ansi
* mshop/attribute/manager/lists/count/ansi
* mshop/attribute/manager/lists/aggregate/ansi

## update/mysql

Updates an existing attribute list record in the database

```
mshop/attribute/manager/lists/update/mysql = 
 UPDATE "mshop_attribute_list"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_attribute_list"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "domain" = ?, "refid" = ?, "start" = ?,
 	"end" = ?, "config" = ?, "pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/attribute/manager/lists/update/ansi

# name

Class name of the used attribute manager implementation

```
mshop/attribute/manager/name = Standard
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
 \Aimeos\MShop\Attribute\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Attribute\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/attribute/manager/name = Mymanager
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
mshop/attribute/manager/newid/ansi = mshop/attribute/manager/newid
```

* Default: mshop/attribute/manager/newid
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

* mshop/attribute/manager/insert/ansi
* mshop/attribute/manager/update/ansi
* mshop/attribute/manager/delete/ansi
* mshop/attribute/manager/search/ansi
* mshop/attribute/manager/count/ansi

## mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/attribute/manager/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/attribute/manager/newid

See also:

* mshop/attribute/manager/newid/ansi

# property
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/attribute/manager/property/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattpr."id"
 	FROM "mshop_attribute_property" AS mattpr
 	:joins
 	WHERE :cond
 	ORDER BY mattpr."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/attribute/manager/property/count
* Type: string - SQL statement for counting items
* Since: 2018.01

Counts all records matched by the given criteria from the attribute
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

* mshop/attribute/manager/property/insert/ansi
* mshop/attribute/manager/property/update/ansi
* mshop/attribute/manager/property/newid/ansi
* mshop/attribute/manager/property/delete/ansi
* mshop/attribute/manager/property/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/attribute/manager/property/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattpr."id"
 	FROM "mshop_attribute_property" AS mattpr
 	:joins
 	WHERE :cond
 	ORDER BY mattpr."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattpr."id"
 	FROM "mshop_attribute_property" AS mattpr
 	:joins
 	WHERE :cond
 	ORDER BY mattpr."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/attribute/manager/property/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the attribute property manager

```
mshop/attribute/manager/property/decorators/excludes = Array
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
around the attribute property manager.

```
 mshop/attribute/manager/property/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the attribute property manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/property/decorators/global
* mshop/attribute/manager/property/decorators/local

## decorators/global

Adds a list of globally available decorators only to the attribute property manager

```
mshop/attribute/manager/property/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the attribute property
manager.

```
 mshop/attribute/manager/property/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the attribute
property manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/property/decorators/excludes
* mshop/attribute/manager/property/decorators/local

## decorators/local

Adds a list of local decorators only to the attribute property manager

```
mshop/attribute/manager/property/decorators/local = Array
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
("\Aimeos\MShop\Attribute\Manager\Property\Decorator\*") around the attribute
property manager.

```
 mshop/attribute/manager/property/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Attribute\Manager\Property\Decorator\Decorator2" only to
the attribute property manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/property/decorators/excludes
* mshop/attribute/manager/property/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/attribute/manager/property/delete/ansi = 
 DELETE FROM "mshop_attribute_property"
 WHERE :cond AND siteid = ?
```

* Default: mshop/attribute/manager/property/delete
* Type: string - SQL statement for deleting items
* Since: 2018.01

Removes the records specified by the given IDs from the attribute database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/property/insert/ansi
* mshop/attribute/manager/property/update/ansi
* mshop/attribute/manager/property/newid/ansi
* mshop/attribute/manager/property/search/ansi
* mshop/attribute/manager/property/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/attribute/manager/property/delete/mysql = 
 DELETE FROM "mshop_attribute_property"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_attribute_property"
 WHERE :cond AND siteid = ?


See also:

* mshop/attribute/manager/property/delete/ansi

## insert/ansi

Inserts a new attribute property record into the database table

```
mshop/attribute/manager/property/insert/ansi = 
 INSERT INTO "mshop_attribute_property" ( :names
 	"parentid", "key", "type", "langid", "value",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/attribute/manager/property/insert
* Type: string - SQL statement for inserting records
* Since: 2018.01

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the attribute property item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/property/update/ansi
* mshop/attribute/manager/property/newid/ansi
* mshop/attribute/manager/property/delete/ansi
* mshop/attribute/manager/property/search/ansi
* mshop/attribute/manager/property/count/ansi

## insert/mysql

Inserts a new attribute property record into the database table

```
mshop/attribute/manager/property/insert/mysql = 
 INSERT INTO "mshop_attribute_property" ( :names
 	"parentid", "key", "type", "langid", "value",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_attribute_property" ( :names
 	"parentid", "key", "type", "langid", "value",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/attribute/manager/property/insert/ansi

## name

Class name of the used attribute property manager implementation

```
mshop/attribute/manager/property/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.01

Each default attribute property manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Attribute\Manager\Property\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Attribute\Manager\Property\Myproperty
```

then you have to set the this configuration option:

```
 mshop/attribute/manager/property/name = Myproperty
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyProperty"!


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/attribute/manager/property/newid/ansi = mshop/attribute/manager/property/newid
```

* Default: mshop/attribute/manager/property/newid
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
 SELECT currval('seq_mattpr_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mattpr_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/attribute/manager/property/insert/ansi
* mshop/attribute/manager/property/update/ansi
* mshop/attribute/manager/property/delete/ansi
* mshop/attribute/manager/property/search/ansi
* mshop/attribute/manager/property/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/attribute/manager/property/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/attribute/manager/property/newid

See also:

* mshop/attribute/manager/property/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/attribute/manager/property/search/ansi = 
 SELECT :columns
 	mattpr."id" AS "attribute.property.id", mattpr."parentid" AS "attribute.property.parentid",
 	mattpr."siteid" AS "attribute.property.siteid", mattpr."type" AS "attribute.property.type",
 	mattpr."langid" AS "attribute.property.languageid", mattpr."value" AS "attribute.property.value",
 	mattpr."mtime" AS "attribute.property.mtime", mattpr."editor" AS "attribute.property.editor",
 	mattpr."ctime" AS "attribute.property.ctime"
 FROM "mshop_attribute_property" AS mattpr
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/attribute/manager/property/search
* Type: string - SQL statement for searching items
* Since: 2018.01

Fetches the records matched by the given criteria from the attribute
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

* mshop/attribute/manager/property/insert/ansi
* mshop/attribute/manager/property/update/ansi
* mshop/attribute/manager/property/newid/ansi
* mshop/attribute/manager/property/delete/ansi
* mshop/attribute/manager/property/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/attribute/manager/property/search/mysql = 
 SELECT :columns
 	mattpr."id" AS "attribute.property.id", mattpr."parentid" AS "attribute.property.parentid",
 	mattpr."siteid" AS "attribute.property.siteid", mattpr."type" AS "attribute.property.type",
 	mattpr."langid" AS "attribute.property.languageid", mattpr."value" AS "attribute.property.value",
 	mattpr."mtime" AS "attribute.property.mtime", mattpr."editor" AS "attribute.property.editor",
 	mattpr."ctime" AS "attribute.property.ctime"
 FROM "mshop_attribute_property" AS mattpr
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mattpr."id" AS "attribute.property.id", mattpr."parentid" AS "attribute.property.parentid",
 	mattpr."siteid" AS "attribute.property.siteid", mattpr."type" AS "attribute.property.type",
 	mattpr."langid" AS "attribute.property.languageid", mattpr."value" AS "attribute.property.value",
 	mattpr."mtime" AS "attribute.property.mtime", mattpr."editor" AS "attribute.property.editor",
 	mattpr."ctime" AS "attribute.property.ctime"
 FROM "mshop_attribute_property" AS mattpr
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/attribute/manager/property/search/ansi

## submanagers

List of manager names that can be instantiated by the attribute property manager

```
mshop/attribute/manager/property/submanagers = Array
(
    [0] => type
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


## type/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/attribute/manager/property/type/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattprty."id"
 	FROM "mshop_attribute_property_type" mattprty
 	:joins
 	WHERE :cond
 	ORDER BY mattprty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/attribute/manager/property/type/count
* Type: string - SQL statement for counting items
* Since: 2018.01

Counts all records matched by the given criteria from the attribute
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

* mshop/attribute/manager/property/type/insert/ansi
* mshop/attribute/manager/property/type/update/ansi
* mshop/attribute/manager/property/type/newid/ansi
* mshop/attribute/manager/property/type/delete/ansi
* mshop/attribute/manager/property/type/search/ansi

## type/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/attribute/manager/property/type/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattprty."id"
 	FROM "mshop_attribute_property_type" mattprty
 	:joins
 	WHERE :cond
 	ORDER BY mattprty."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattprty."id"
 	FROM "mshop_attribute_property_type" mattprty
 	:joins
 	WHERE :cond
 	ORDER BY mattprty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/attribute/manager/property/type/count/ansi

## type/decorators/excludes

Excludes decorators added by the "common" option from the attribute property type manager

```
mshop/attribute/manager/property/type/decorators/excludes = Array
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
around the attribute property type manager.

```
 mshop/attribute/manager/property/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the attribute property type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/property/type/decorators/global
* mshop/attribute/manager/property/type/decorators/local

## type/decorators/global

Adds a list of globally available decorators only to the attribute property type manager

```
mshop/attribute/manager/property/type/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the attribute
property type manager.

```
 mshop/attribute/manager/property/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the attribute
property type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/property/type/decorators/excludes
* mshop/attribute/manager/property/type/decorators/local

## type/decorators/local

Adds a list of local decorators only to the attribute property type manager

```
mshop/attribute/manager/property/type/decorators/local = Array
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
("\Aimeos\MShop\Attribute\Manager\Property\Type\Decorator\*") around the
attribute property type manager.

```
 mshop/attribute/manager/property/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Attribute\Manager\Property\Type\Decorator\Decorator2" only to
the attribute property type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/property/type/decorators/excludes
* mshop/attribute/manager/property/type/decorators/global

## type/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/attribute/manager/property/type/delete/ansi = 
 DELETE FROM "mshop_attribute_property_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/attribute/manager/property/type/delete
* Type: string - SQL statement for deleting items
* Since: 2018.01

Removes the records specified by the given IDs from the attribute database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/property/type/insert/ansi
* mshop/attribute/manager/property/type/update/ansi
* mshop/attribute/manager/property/type/newid/ansi
* mshop/attribute/manager/property/type/search/ansi
* mshop/attribute/manager/property/type/count/ansi

## type/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/attribute/manager/property/type/delete/mysql = 
 DELETE FROM "mshop_attribute_property_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_attribute_property_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/attribute/manager/property/type/delete/ansi

## type/insert/ansi

Inserts a new attribute property type record into the database table

```
mshop/attribute/manager/property/type/insert/ansi = 
 INSERT INTO "mshop_attribute_property_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/attribute/manager/property/type/insert
* Type: string - SQL statement for inserting records
* Since: 2018.01

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the attribute type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/property/type/update/ansi
* mshop/attribute/manager/property/type/newid/ansi
* mshop/attribute/manager/property/type/delete/ansi
* mshop/attribute/manager/property/type/search/ansi
* mshop/attribute/manager/property/type/count/ansi

## type/insert/mysql

Inserts a new attribute property type record into the database table

```
mshop/attribute/manager/property/type/insert/mysql = 
 INSERT INTO "mshop_attribute_property_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_attribute_property_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/attribute/manager/property/type/insert/ansi

## type/name

Class name of the used attribute property type manager implementation

```
mshop/attribute/manager/property/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2018.01

Each default attribute property type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Attribute\Manager\Lists\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Attribute\Manager\Lists\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/attribute/manager/property/type/name = Mytype
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyType"!


## type/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/attribute/manager/property/type/newid/ansi = mshop/attribute/manager/property/type/newid
```

* Default: mshop/attribute/manager/property/type/newid
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
 SELECT currval('seq_mattprty_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mattprty_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/attribute/manager/property/type/insert/ansi
* mshop/attribute/manager/property/type/update/ansi
* mshop/attribute/manager/property/type/delete/ansi
* mshop/attribute/manager/property/type/search/ansi
* mshop/attribute/manager/property/type/count/ansi

## type/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/attribute/manager/property/type/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/attribute/manager/property/type/newid

See also:

* mshop/attribute/manager/property/type/newid/ansi

## type/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/attribute/manager/property/type/search/ansi = 
 SELECT :columns
 	mattprty."id" AS "attribute.property.type.id", mattprty."siteid" AS "attribute.property.type.siteid",
 	mattprty."code" AS "attribute.property.type.code", mattprty."domain" AS "attribute.property.type.domain",
 	mattprty."label" AS "attribute.property.type.label", mattprty."status" AS "attribute.property.type.status",
 	mattprty."mtime" AS "attribute.property.type.mtime", mattprty."editor" AS "attribute.property.type.editor",
 	mattprty."ctime" AS "attribute.property.type.ctime", mattprty."pos" AS "attribute.property.type.position"
 FROM "mshop_attribute_property_type" mattprty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/attribute/manager/property/type/search
* Type: string - SQL statement for searching items
* Since: 2018.01

Fetches the records matched by the given criteria from the attribute
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

* mshop/attribute/manager/property/type/insert/ansi
* mshop/attribute/manager/property/type/update/ansi
* mshop/attribute/manager/property/type/newid/ansi
* mshop/attribute/manager/property/type/delete/ansi
* mshop/attribute/manager/property/type/count/ansi

## type/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/attribute/manager/property/type/search/mysql = 
 SELECT :columns
 	mattprty."id" AS "attribute.property.type.id", mattprty."siteid" AS "attribute.property.type.siteid",
 	mattprty."code" AS "attribute.property.type.code", mattprty."domain" AS "attribute.property.type.domain",
 	mattprty."label" AS "attribute.property.type.label", mattprty."status" AS "attribute.property.type.status",
 	mattprty."mtime" AS "attribute.property.type.mtime", mattprty."editor" AS "attribute.property.type.editor",
 	mattprty."ctime" AS "attribute.property.type.ctime", mattprty."pos" AS "attribute.property.type.position"
 FROM "mshop_attribute_property_type" mattprty
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mattprty."id" AS "attribute.property.type.id", mattprty."siteid" AS "attribute.property.type.siteid",
 	mattprty."code" AS "attribute.property.type.code", mattprty."domain" AS "attribute.property.type.domain",
 	mattprty."label" AS "attribute.property.type.label", mattprty."status" AS "attribute.property.type.status",
 	mattprty."mtime" AS "attribute.property.type.mtime", mattprty."editor" AS "attribute.property.type.editor",
 	mattprty."ctime" AS "attribute.property.type.ctime", mattprty."pos" AS "attribute.property.type.position"
 FROM "mshop_attribute_property_type" mattprty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/attribute/manager/property/type/search/ansi

## type/submanagers

List of manager names that can be instantiated by the attribute property type manager

```
mshop/attribute/manager/property/type/submanagers = Array
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


## type/update/ansi

Updates an existing attribute property type record in the database

```
mshop/attribute/manager/property/type/update/ansi = 
 UPDATE "mshop_attribute_property_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/attribute/manager/property/type/update
* Type: string - SQL statement for updating records
* Since: 2018.01

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the attribute type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/property/type/insert/ansi
* mshop/attribute/manager/property/type/newid/ansi
* mshop/attribute/manager/property/type/delete/ansi
* mshop/attribute/manager/property/type/search/ansi
* mshop/attribute/manager/property/type/count/ansi

## type/update/mysql

Updates an existing attribute property type record in the database

```
mshop/attribute/manager/property/type/update/mysql = 
 UPDATE "mshop_attribute_property_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_attribute_property_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/attribute/manager/property/type/update/ansi

## update/ansi

Updates an existing attribute property record in the database

```
mshop/attribute/manager/property/update/ansi = 
 UPDATE "mshop_attribute_property"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "langid" = ?,
 	"value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/attribute/manager/property/update
* Type: string - SQL statement for updating records
* Since: 2018.01

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the attribute property item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/property/insert/ansi
* mshop/attribute/manager/property/newid/ansi
* mshop/attribute/manager/property/delete/ansi
* mshop/attribute/manager/property/search/ansi
* mshop/attribute/manager/property/count/ansi

## update/mysql

Updates an existing attribute property record in the database

```
mshop/attribute/manager/property/update/mysql = 
 UPDATE "mshop_attribute_property"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "langid" = ?,
 	"value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_attribute_property"
 SET :names
 	"parentid" = ?, "key" = ?, "type" = ?, "langid" = ?,
 	"value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/attribute/manager/property/update/ansi

# search
## ansi

Retrieves the records matched by the given criteria in the database

```
mshop/attribute/manager/search/ansi = 
 SELECT :columns
 	matt."id" AS "attribute.id", matt."siteid" AS "attribute.siteid",
 	matt."type" AS "attribute.type", matt."domain" AS "attribute.domain",
 	matt."code" AS "attribute.code", matt."status" AS "attribute.status",
 	matt."pos" AS "attribute.position", matt."label" AS "attribute.label",
 	matt."mtime" AS "attribute.mtime", matt."ctime" AS "attribute.ctime",
 	matt."editor" AS "attribute.editor"
 FROM "mshop_attribute" AS matt
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	matt."id", matt."siteid", matt."type", matt."domain", matt."code", matt."status",
 	matt."pos", matt."label", matt."mtime", matt."ctime", matt."editor"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/attribute/manager/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the attribute
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

* mshop/attribute/manager/insert/ansi
* mshop/attribute/manager/update/ansi
* mshop/attribute/manager/newid/ansi
* mshop/attribute/manager/delete/ansi
* mshop/attribute/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/attribute/manager/search/mysql = 
 SELECT :columns
 	matt."id" AS "attribute.id", matt."siteid" AS "attribute.siteid",
 	matt."type" AS "attribute.type", matt."domain" AS "attribute.domain",
 	matt."code" AS "attribute.code", matt."status" AS "attribute.status",
 	matt."pos" AS "attribute.position", matt."label" AS "attribute.label",
 	matt."mtime" AS "attribute.mtime", matt."ctime" AS "attribute.ctime",
 	matt."editor" AS "attribute.editor"
 FROM "mshop_attribute" AS matt
 :joins
 WHERE :cond
 GROUP BY :group matt."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	matt."id" AS "attribute.id", matt."siteid" AS "attribute.siteid",
 	matt."type" AS "attribute.type", matt."domain" AS "attribute.domain",
 	matt."code" AS "attribute.code", matt."status" AS "attribute.status",
 	matt."pos" AS "attribute.position", matt."label" AS "attribute.label",
 	matt."mtime" AS "attribute.mtime", matt."ctime" AS "attribute.ctime",
 	matt."editor" AS "attribute.editor"
 FROM "mshop_attribute" AS matt
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	matt."id", matt."siteid", matt."type", matt."domain", matt."code", matt."status",
 	matt."pos", matt."label", matt."mtime", matt."ctime", matt."editor"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/attribute/manager/search/ansi

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/attribute/manager/sitemode = 3
```

* Default: 3
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole attribute domain if items from parent sites are inherited,
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

List of manager names that can be instantiated by the attribute manager

```
mshop/attribute/manager/submanagers = Array
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
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/attribute/manager/type/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattty."id"
 	FROM "mshop_attribute_type" AS mattty
 	:joins
 	WHERE :cond
 	ORDER BY mattty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/attribute/manager/type/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the attribute
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

* mshop/attribute/manager/type/insert/ansi
* mshop/attribute/manager/type/update/ansi
* mshop/attribute/manager/type/newid/ansi
* mshop/attribute/manager/type/delete/ansi
* mshop/attribute/manager/type/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/attribute/manager/type/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattty."id"
 	FROM "mshop_attribute_type" AS mattty
 	:joins
 	WHERE :cond
 	ORDER BY mattty."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mattty."id"
 	FROM "mshop_attribute_type" AS mattty
 	:joins
 	WHERE :cond
 	ORDER BY mattty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/attribute/manager/type/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the attribute type manager

```
mshop/attribute/manager/type/decorators/excludes = Array
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
around the attribute type manager.

```
 mshop/attribute/manager/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the attribute type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/type/decorators/global
* mshop/attribute/manager/type/decorators/local

## decorators/global

Adds a list of globally available decorators only to the attribute type manager

```
mshop/attribute/manager/type/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the attribute type
manager.

```
 mshop/attribute/manager/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the attribute
type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/type/decorators/excludes
* mshop/attribute/manager/type/decorators/local

## decorators/local

Adds a list of local decorators only to the attribute type manager

```
mshop/attribute/manager/type/decorators/local = Array
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
("\Aimeos\MShop\Attribute\Manager\Type\Decorator\*") around the attribute
type manager.

```
 mshop/attribute/manager/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Attribute\Manager\Type\Decorator\Decorator2" only to the
attribute type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/attribute/manager/type/decorators/excludes
* mshop/attribute/manager/type/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/attribute/manager/type/delete/ansi = 
 DELETE FROM "mshop_attribute_type"
 WHERE :cond AND siteid = ?
```

* Default: mshop/attribute/manager/type/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the attribute database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/type/insert/ansi
* mshop/attribute/manager/type/update/ansi
* mshop/attribute/manager/type/newid/ansi
* mshop/attribute/manager/type/search/ansi
* mshop/attribute/manager/type/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/attribute/manager/type/delete/mysql = 
 DELETE FROM "mshop_attribute_type"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_attribute_type"
 WHERE :cond AND siteid = ?


See also:

* mshop/attribute/manager/type/delete/ansi

## insert/ansi

Inserts a new attribute type record into the database table

```
mshop/attribute/manager/type/insert/ansi = 
 INSERT INTO "mshop_attribute_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/attribute/manager/type/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the attribute type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/type/update/ansi
* mshop/attribute/manager/type/newid/ansi
* mshop/attribute/manager/type/delete/ansi
* mshop/attribute/manager/type/search/ansi
* mshop/attribute/manager/type/count/ansi

## insert/mysql

Inserts a new attribute type record into the database table

```
mshop/attribute/manager/type/insert/mysql = 
 INSERT INTO "mshop_attribute_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_attribute_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/attribute/manager/type/insert/ansi

## name

Class name of the used attribute type manager implementation

```
mshop/attribute/manager/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default attribute type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Attribute\Manager\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Attribute\Manager\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/attribute/manager/type/name = Mytype
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
mshop/attribute/manager/type/newid/ansi = mshop/attribute/manager/type/newid
```

* Default: mshop/attribute/manager/type/newid
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
 SELECT currval('seq_mattty_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mattty_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/attribute/manager/type/insert/ansi
* mshop/attribute/manager/type/update/ansi
* mshop/attribute/manager/type/delete/ansi
* mshop/attribute/manager/type/search/ansi
* mshop/attribute/manager/type/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/attribute/manager/type/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/attribute/manager/type/newid

See also:

* mshop/attribute/manager/type/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/attribute/manager/type/search/ansi = 
 SELECT :columns
 	mattty."id" AS "attribute.type.id", mattty."siteid" AS "attribute.type.siteid",
 	mattty."code" AS "attribute.type.code", mattty."domain" AS "attribute.type.domain",
 	mattty."label" AS "attribute.type.label", mattty."status" AS "attribute.type.status",
 	mattty."mtime" AS "attribute.type.mtime", mattty."ctime" AS "attribute.type.ctime",
 	mattty."editor" AS "attribute.type.editor", mattty."pos" AS "attribute.type.position"
 FROM "mshop_attribute_type" AS mattty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/attribute/manager/type/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the attribute
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

* mshop/attribute/manager/type/insert/ansi
* mshop/attribute/manager/type/update/ansi
* mshop/attribute/manager/type/newid/ansi
* mshop/attribute/manager/type/delete/ansi
* mshop/attribute/manager/type/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/attribute/manager/type/search/mysql = 
 SELECT :columns
 	mattty."id" AS "attribute.type.id", mattty."siteid" AS "attribute.type.siteid",
 	mattty."code" AS "attribute.type.code", mattty."domain" AS "attribute.type.domain",
 	mattty."label" AS "attribute.type.label", mattty."status" AS "attribute.type.status",
 	mattty."mtime" AS "attribute.type.mtime", mattty."ctime" AS "attribute.type.ctime",
 	mattty."editor" AS "attribute.type.editor", mattty."pos" AS "attribute.type.position"
 FROM "mshop_attribute_type" AS mattty
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mattty."id" AS "attribute.type.id", mattty."siteid" AS "attribute.type.siteid",
 	mattty."code" AS "attribute.type.code", mattty."domain" AS "attribute.type.domain",
 	mattty."label" AS "attribute.type.label", mattty."status" AS "attribute.type.status",
 	mattty."mtime" AS "attribute.type.mtime", mattty."ctime" AS "attribute.type.ctime",
 	mattty."editor" AS "attribute.type.editor", mattty."pos" AS "attribute.type.position"
 FROM "mshop_attribute_type" AS mattty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/attribute/manager/type/search/ansi

## submanagers

List of manager names that can be instantiated by the attribute type manager

```
mshop/attribute/manager/type/submanagers = Array
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


## update/ansi

Updates an existing attribute type record in the database

```
mshop/attribute/manager/type/update/ansi = 
 UPDATE "mshop_attribute_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/attribute/manager/type/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the attribute type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/type/insert/ansi
* mshop/attribute/manager/type/newid/ansi
* mshop/attribute/manager/type/delete/ansi
* mshop/attribute/manager/type/search/ansi
* mshop/attribute/manager/type/count/ansi

## update/mysql

Updates an existing attribute type record in the database

```
mshop/attribute/manager/type/update/mysql = 
 UPDATE "mshop_attribute_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_attribute_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/attribute/manager/type/update/ansi

# update
## ansi

Updates an existing attribute record in the database

```
mshop/attribute/manager/update/ansi = 
 UPDATE "mshop_attribute"
 SET :names
 	"key" = ?, "type" = ?, "domain" = ?, "code" = ?, "status" = ?,
 	"pos" = ?, "label" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/attribute/manager/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the attribute item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/attribute/manager/insert/ansi
* mshop/attribute/manager/newid/ansi
* mshop/attribute/manager/delete/ansi
* mshop/attribute/manager/search/ansi
* mshop/attribute/manager/count/ansi

## mysql

Updates an existing attribute record in the database

```
mshop/attribute/manager/update/mysql = 
 UPDATE "mshop_attribute"
 SET :names
 	"key" = ?, "type" = ?, "domain" = ?, "code" = ?, "status" = ?,
 	"pos" = ?, "label" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_attribute"
 SET :names
 	"key" = ?, "type" = ?, "domain" = ?, "code" = ?, "status" = ?,
 	"pos" = ?, "label" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/attribute/manager/update/ansi