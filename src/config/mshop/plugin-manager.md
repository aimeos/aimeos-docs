
# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/plugin/manager/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mplu."id"
 	FROM "mshop_plugin" mplu
 	:joins
 	WHERE :cond
 	ORDER BY mplu."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/plugin/manager/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the plugin
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

* mshop/plugin/manager/insert/ansi
* mshop/plugin/manager/update/ansi
* mshop/plugin/manager/newid/ansi
* mshop/plugin/manager/delete/ansi
* mshop/plugin/manager/search/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/plugin/manager/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mplu."id"
 	FROM "mshop_plugin" mplu
 	:joins
 	WHERE :cond
 	ORDER BY mplu."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mplu."id"
 	FROM "mshop_plugin" mplu
 	:joins
 	WHERE :cond
 	ORDER BY mplu."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/plugin/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the plugin manager

```
mshop/plugin/manager/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the plugin manager.

```
 mshop/plugin/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the plugin manager.

See also:

* mshop/common/manager/decorators/default
* mshop/plugin/manager/decorators/global
* mshop/plugin/manager/decorators/local

## global

Adds a list of globally available decorators only to the plugin manager

```
mshop/plugin/manager/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the plugin manager.

```
 mshop/plugin/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the plugin
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/plugin/manager/decorators/excludes
* mshop/plugin/manager/decorators/local

## local

Adds a list of local decorators only to the plugin manager

```
mshop/plugin/manager/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Plugin\Manager\Decorator\*") around the plugin manager.

```
 mshop/plugin/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Plugin\Manager\Decorator\Decorator2" only to the plugin
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/plugin/manager/decorators/excludes
* mshop/plugin/manager/decorators/global

# delete
## ansi

Deletes the items matched by the given IDs from the database

```
mshop/plugin/manager/delete/ansi = 
 DELETE FROM "mshop_plugin"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: mshop/plugin/manager/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the plugin database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/plugin/manager/insert/ansi
* mshop/plugin/manager/update/ansi
* mshop/plugin/manager/newid/ansi
* mshop/plugin/manager/search/ansi
* mshop/plugin/manager/count/ansi

## mysql

Deletes the items matched by the given IDs from the database

```
mshop/plugin/manager/delete/mysql = 
 DELETE FROM "mshop_plugin"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: 
 DELETE FROM "mshop_plugin"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/plugin/manager/delete/ansi

# insert
## ansi

Inserts a new plugin record into the database table

```
mshop/plugin/manager/insert/ansi = 
 INSERT INTO "mshop_plugin" ( :names
 	"type", "label", "provider", "config", "pos",
 	"status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/plugin/manager/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the plugin item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/plugin/manager/update/ansi
* mshop/plugin/manager/newid/ansi
* mshop/plugin/manager/delete/ansi
* mshop/plugin/manager/search/ansi
* mshop/plugin/manager/count/ansi

## mysql

Inserts a new plugin record into the database table

```
mshop/plugin/manager/insert/mysql = 
 INSERT INTO "mshop_plugin" ( :names
 	"type", "label", "provider", "config", "pos",
 	"status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_plugin" ( :names
 	"type", "label", "provider", "config", "pos",
 	"status", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/plugin/manager/insert/ansi

# name

Class name of the used plugin manager implementation

```
mshop/plugin/manager/name = Standard
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
 \Aimeos\MShop\Plugin\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Plugin\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/plugin/manager/name = Mymanager
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
mshop/plugin/manager/newid/ansi = mshop/plugin/manager/newid
```

* Default: mshop/plugin/manager/newid
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
 SELECT currval('seq_mplu_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mplu_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/plugin/manager/insert/ansi
* mshop/plugin/manager/update/ansi
* mshop/plugin/manager/delete/ansi
* mshop/plugin/manager/search/ansi
* mshop/plugin/manager/count/ansi

## mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/plugin/manager/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/plugin/manager/newid

See also:

* mshop/plugin/manager/newid/ansi

# search
## ansi

Retrieves the records matched by the given criteria in the database

```
mshop/plugin/manager/search/ansi = 
 SELECT :columns
 	mplu."id" AS "plugin.id", mplu."siteid" AS "plugin.siteid",
 	mplu."type" AS "plugin.type", mplu."label" AS "plugin.label",
 	mplu."provider" AS "plugin.provider", mplu."config" AS "plugin.config",
 	mplu."pos" AS "plugin.position", mplu."status" AS "plugin.status",
 	mplu."mtime" AS "plugin.mtime", mplu."editor" AS "plugin.editor",
 	mplu."ctime" AS "plugin.ctime"
 FROM "mshop_plugin" mplu
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/plugin/manager/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the plugin
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

* mshop/plugin/manager/insert/ansi
* mshop/plugin/manager/update/ansi
* mshop/plugin/manager/newid/ansi
* mshop/plugin/manager/delete/ansi
* mshop/plugin/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/plugin/manager/search/mysql = 
 SELECT :columns
 	mplu."id" AS "plugin.id", mplu."siteid" AS "plugin.siteid",
 	mplu."type" AS "plugin.type", mplu."label" AS "plugin.label",
 	mplu."provider" AS "plugin.provider", mplu."config" AS "plugin.config",
 	mplu."pos" AS "plugin.position", mplu."status" AS "plugin.status",
 	mplu."mtime" AS "plugin.mtime", mplu."editor" AS "plugin.editor",
 	mplu."ctime" AS "plugin.ctime"
 FROM "mshop_plugin" mplu
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mplu."id" AS "plugin.id", mplu."siteid" AS "plugin.siteid",
 	mplu."type" AS "plugin.type", mplu."label" AS "plugin.label",
 	mplu."provider" AS "plugin.provider", mplu."config" AS "plugin.config",
 	mplu."pos" AS "plugin.position", mplu."status" AS "plugin.status",
 	mplu."mtime" AS "plugin.mtime", mplu."editor" AS "plugin.editor",
 	mplu."ctime" AS "plugin.ctime"
 FROM "mshop_plugin" mplu
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/plugin/manager/search/ansi

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/plugin/manager/sitemode = 1
```

* Default: 1
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole plugin domain if items from parent sites are inherited,
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

List of manager names that can be instantiated by the plugin manager

```
mshop/plugin/manager/submanagers = Array
(
)
```

* Default: Array
(
)

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
mshop/plugin/manager/type/count/ansi = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mpluty."id"
 	FROM "mshop_plugin_type" mpluty
 	:joins
 	WHERE :cond
 	ORDER BY mpluty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list
```

* Default: mshop/plugin/manager/type/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the plugin
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

* mshop/plugin/manager/type/insert/ansi
* mshop/plugin/manager/type/update/ansi
* mshop/plugin/manager/type/newid/ansi
* mshop/plugin/manager/type/delete/ansi
* mshop/plugin/manager/type/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/plugin/manager/type/count/mysql = 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mpluty."id"
 	FROM "mshop_plugin_type" mpluty
 	:joins
 	WHERE :cond
 	ORDER BY mpluty."id"
 	LIMIT 10000 OFFSET 0
 ) AS list
```

* Default: 
 SELECT COUNT(*) AS "count"
 FROM (
 	SELECT mpluty."id"
 	FROM "mshop_plugin_type" mpluty
 	:joins
 	WHERE :cond
 	ORDER BY mpluty."id"
 	OFFSET 0 ROWS FETCH NEXT 10000 ROWS ONLY
 ) AS list


See also:

* mshop/plugin/manager/type/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the plugin type manager

```
mshop/plugin/manager/type/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the plugin type manager.

```
 mshop/plugin/manager/type/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the plugin type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/plugin/manager/type/decorators/global
* mshop/plugin/manager/type/decorators/local

## decorators/global

Adds a list of globally available decorators only to the plugin type manager

```
mshop/plugin/manager/type/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the plugin type
manager.

```
 mshop/plugin/manager/type/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the plugin
type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/plugin/manager/type/decorators/excludes
* mshop/plugin/manager/type/decorators/local

## decorators/local

Adds a list of local decorators only to the plugin type manager

```
mshop/plugin/manager/type/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2014.03

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Plugin\Manager\Type\Decorator\*") around the plugin
type manager.

```
 mshop/plugin/manager/type/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Plugin\Manager\Type\Decorator\Decorator2" only to the
plugin type manager.

See also:

* mshop/common/manager/decorators/default
* mshop/plugin/manager/type/decorators/excludes
* mshop/plugin/manager/type/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/plugin/manager/type/delete/ansi = 
 DELETE FROM "mshop_plugin_type"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: mshop/plugin/manager/type/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the plugin database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/plugin/manager/type/insert/ansi
* mshop/plugin/manager/type/update/ansi
* mshop/plugin/manager/type/newid/ansi
* mshop/plugin/manager/type/search/ansi
* mshop/plugin/manager/type/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/plugin/manager/type/delete/mysql = 
 DELETE FROM "mshop_plugin_type"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: 
 DELETE FROM "mshop_plugin_type"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/plugin/manager/type/delete/ansi

## insert/ansi

Inserts a new plugin type record into the database table

```
mshop/plugin/manager/type/insert/ansi = 
 INSERT INTO "mshop_plugin_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/plugin/manager/type/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the plugin type item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/plugin/manager/type/update/ansi
* mshop/plugin/manager/type/newid/ansi
* mshop/plugin/manager/type/delete/ansi
* mshop/plugin/manager/type/search/ansi
* mshop/plugin/manager/type/count/ansi

## insert/mysql

Inserts a new plugin type record into the database table

```
mshop/plugin/manager/type/insert/mysql = 
 INSERT INTO "mshop_plugin_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_plugin_type" ( :names
 	"code", "domain", "label", "pos", "status",
 	"mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/plugin/manager/type/insert/ansi

## name

Class name of the used plugin type manager implementation

```
mshop/plugin/manager/type/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default plugin type manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Plugin\Manager\Type\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Plugin\Manager\Type\Mytype
```

then you have to set the this configuration option:

```
 mshop/plugin/manager/type/name = Mytype
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
mshop/plugin/manager/type/newid/ansi = mshop/plugin/manager/type/newid
```

* Default: mshop/plugin/manager/type/newid
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
 SELECT currval('seq_mpluty_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mpluty_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/plugin/manager/type/insert/ansi
* mshop/plugin/manager/type/update/ansi
* mshop/plugin/manager/type/delete/ansi
* mshop/plugin/manager/type/search/ansi
* mshop/plugin/manager/type/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/plugin/manager/type/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/plugin/manager/type/newid

See also:

* mshop/plugin/manager/type/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/plugin/manager/type/search/ansi = 
 SELECT :columns
 	mpluty."id" AS "plugin.type.id", mpluty."siteid" AS "plugin.type.siteid",
 	mpluty."code" AS "plugin.type.code", mpluty."domain" AS "plugin.type.domain",
 	mpluty."label" AS "plugin.type.label", mpluty."status" AS "plugin.type.status",
 	mpluty."mtime" AS "plugin.type.mtime", mpluty."editor" AS "plugin.type.editor",
 	mpluty."ctime" AS "plugin.type.ctime", mpluty."pos" AS "plugin.type.position"
 FROM "mshop_plugin_type" mpluty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/plugin/manager/type/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the plugin
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

* mshop/plugin/manager/type/insert/ansi
* mshop/plugin/manager/type/update/ansi
* mshop/plugin/manager/type/newid/ansi
* mshop/plugin/manager/type/delete/ansi
* mshop/plugin/manager/type/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/plugin/manager/type/search/mysql = 
 SELECT :columns
 	mpluty."id" AS "plugin.type.id", mpluty."siteid" AS "plugin.type.siteid",
 	mpluty."code" AS "plugin.type.code", mpluty."domain" AS "plugin.type.domain",
 	mpluty."label" AS "plugin.type.label", mpluty."status" AS "plugin.type.status",
 	mpluty."mtime" AS "plugin.type.mtime", mpluty."editor" AS "plugin.type.editor",
 	mpluty."ctime" AS "plugin.type.ctime", mpluty."pos" AS "plugin.type.position"
 FROM "mshop_plugin_type" mpluty
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mpluty."id" AS "plugin.type.id", mpluty."siteid" AS "plugin.type.siteid",
 	mpluty."code" AS "plugin.type.code", mpluty."domain" AS "plugin.type.domain",
 	mpluty."label" AS "plugin.type.label", mpluty."status" AS "plugin.type.status",
 	mpluty."mtime" AS "plugin.type.mtime", mpluty."editor" AS "plugin.type.editor",
 	mpluty."ctime" AS "plugin.type.ctime", mpluty."pos" AS "plugin.type.position"
 FROM "mshop_plugin_type" mpluty
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/plugin/manager/type/search/ansi

## submanagers

List of manager names that can be instantiated by the plugin type manager

```
mshop/plugin/manager/type/submanagers = Array
(
)
```

* Default: Array
(
)

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

Updates an existing plugin type record in the database

```
mshop/plugin/manager/type/update/ansi = 
 UPDATE "mshop_plugin_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: mshop/plugin/manager/type/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the plugin type item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/plugin/manager/type/insert/ansi
* mshop/plugin/manager/type/newid/ansi
* mshop/plugin/manager/type/delete/ansi
* mshop/plugin/manager/type/search/ansi
* mshop/plugin/manager/type/count/ansi

## update/mysql

Updates an existing plugin type record in the database

```
mshop/plugin/manager/type/update/mysql = 
 UPDATE "mshop_plugin_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_plugin_type"
 SET :names
 	"code" = ?, "domain" = ?, "label" = ?, "pos" = ?,
 	"status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/plugin/manager/type/update/ansi

# update
## ansi

Updates an existing plugin record in the database

```
mshop/plugin/manager/update/ansi = 
 UPDATE "mshop_plugin"
 SET :names
 	"type" = ?, "label" = ?, "provider" = ?, "config" = ?,
 	"pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: mshop/plugin/manager/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the plugin item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/plugin/manager/insert/ansi
* mshop/plugin/manager/newid/ansi
* mshop/plugin/manager/delete/ansi
* mshop/plugin/manager/search/ansi
* mshop/plugin/manager/count/ansi

## mysql

Updates an existing plugin record in the database

```
mshop/plugin/manager/update/mysql = 
 UPDATE "mshop_plugin"
 SET :names
 	"type" = ?, "label" = ?, "provider" = ?, "config" = ?,
 	"pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_plugin"
 SET :names
 	"type" = ?, "label" = ?, "provider" = ?, "config" = ?,
 	"pos" = ?, "status" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/plugin/manager/update/ansi