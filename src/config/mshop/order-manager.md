
# aggregate
## ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order" mord
 	:joins
 	WHERE :cond
 	GROUP BY mord.id, :cols, :val
 	ORDER BY mord.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/aggregate
* Type: string - SQL statement for aggregating order items
* Since: 2014.09

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

* mshop/order/manager/insert/ansi
* mshop/order/manager/update/ansi
* mshop/order/manager/newid/ansi
* mshop/order/manager/delete/ansi
* mshop/order/manager/search/ansi
* mshop/order/manager/count/ansi

## mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order" mord
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
 	FROM "mshop_order" mord
 	:joins
 	WHERE :cond
 	GROUP BY mord.id, :cols, :val
 	ORDER BY mord.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/aggregate/ansi

# aggregateavg
## ansi

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/aggregateavg/ansi = 
```

* Default: 
* Type: string - SQL statement for aggregating the order items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/aggregate/ansi

## mysql

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/aggregateavg/mysql = 
```

* Default: 
* Type: string - SQL statement for aggregating the order items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/aggregateavg/ansi
* mshop/order/manager/aggregate/mysql

# aggregatesum
## ansi

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/aggregatesum/ansi = 
```

* Default: 
* Type: string - SQL statement for aggregating the order items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/aggregate/ansi

## mysql

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/aggregatesum/mysql = 
```

* Default: 
* Type: string - SQL statement for aggregating the order items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/aggregatesum/ansi
* mshop/order/manager/aggregate/mysql

# base
## address/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/address/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_address" mordbaad
 	:joins
 	WHERE :cond
 	GROUP BY mordbaad.id, :cols, :val
 	ORDER BY mordbaad.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/base/address/aggregate
* Type: string - SQL statement for aggregating order items
* Since: 2014.09

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

* mshop/order/manager/base/address/insert/ansi
* mshop/order/manager/base/address/update/ansi
* mshop/order/manager/base/address/newid/ansi
* mshop/order/manager/base/address/delete/ansi
* mshop/order/manager/base/address/search/ansi
* mshop/order/manager/base/address/count/ansi

## address/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/address/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_address" mordbaad
 	:joins
 	WHERE :cond
 	GROUP BY mordbaad.id, :cols, :val
 	ORDER BY mordbaad.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_address" mordbaad
 	:joins
 	WHERE :cond
 	GROUP BY mordbaad.id, :cols, :val
 	ORDER BY mordbaad.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/base/address/aggregate/ansi

## address/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/address/count/ansi = 
 SELECT COUNT( DISTINCT mordbaad."id" ) AS "count"
 FROM "mshop_order_base_address" mordbaad
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/base/address/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the order
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

* mshop/order/manager/base/address/insert/ansi
* mshop/order/manager/base/address/update/ansi
* mshop/order/manager/base/address/newid/ansi
* mshop/order/manager/base/address/delete/ansi
* mshop/order/manager/base/address/search/ansi

## address/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/address/count/mysql = 
 SELECT COUNT( DISTINCT mordbaad."id" ) AS "count"
 FROM "mshop_order_base_address" mordbaad
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordbaad."id" ) AS "count"
 FROM "mshop_order_base_address" mordbaad
 :joins
 WHERE :cond


See also:

* mshop/order/manager/base/address/count/ansi

## address/decorators/excludes

Excludes decorators added by the "common" option from the order base address manager

```
mshop/order/manager/base/address/decorators/excludes = Array
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
around the order base address manager.

```
 mshop/order/manager/base/address/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/address/decorators/global
* mshop/order/manager/base/address/decorators/local

## address/decorators/global

Adds a list of globally available decorators only to the order base address manager

```
mshop/order/manager/base/address/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order base
address manager.

```
 mshop/order/manager/base/address/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order base
address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/address/decorators/excludes
* mshop/order/manager/base/address/decorators/local

## address/decorators/local

Adds a list of local decorators only to the order base address manager

```
mshop/order/manager/base/address/decorators/local = Array
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
("\Aimeos\MShop\Order\Manager\Base\Address\Decorator\*") around the
order base address manager.

```
 mshop/order/manager/base/address/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Address\Decorator\Decorator2" only
to the order base address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/address/decorators/excludes
* mshop/order/manager/base/address/decorators/global

## address/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/address/delete/ansi = 
 DELETE FROM "mshop_order_base_address"
 WHERE :cond AND siteid = ?
```

* Default: mshop/order/manager/base/address/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the order database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/address/insert/ansi
* mshop/order/manager/base/address/update/ansi
* mshop/order/manager/base/address/newid/ansi
* mshop/order/manager/base/address/search/ansi
* mshop/order/manager/base/address/count/ansi

## address/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/address/delete/mysql = 
 DELETE FROM "mshop_order_base_address"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_order_base_address"
 WHERE :cond AND siteid = ?


See also:

* mshop/order/manager/base/address/delete/ansi

## address/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/base/address/insert/ansi = 
 INSERT INTO "mshop_order_base_address" ( :names
 	"baseid", "addrid", "type", "company", "vatid", "salutation",
 	"title", "firstname", "lastname", "address1", "address2",
 	"address3", "postal", "city", "state", "countryid", "langid",
 	"telephone", "email", "telefax", "website", "longitude", "latitude",
 	"pos", "birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
 )
```

* Default: mshop/order/manager/base/address/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/address/update/ansi
* mshop/order/manager/base/address/newid/ansi
* mshop/order/manager/base/address/delete/ansi
* mshop/order/manager/base/address/search/ansi
* mshop/order/manager/base/address/count/ansi

## address/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/base/address/insert/mysql = 
 INSERT INTO "mshop_order_base_address" ( :names
 	"baseid", "addrid", "type", "company", "vatid", "salutation",
 	"title", "firstname", "lastname", "address1", "address2",
 	"address3", "postal", "city", "state", "countryid", "langid",
 	"telephone", "email", "telefax", "website", "longitude", "latitude",
 	"pos", "birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
 )
```

* Default: 
 INSERT INTO "mshop_order_base_address" ( :names
 	"baseid", "addrid", "type", "company", "vatid", "salutation",
 	"title", "firstname", "lastname", "address1", "address2",
 	"address3", "postal", "city", "state", "countryid", "langid",
 	"telephone", "email", "telefax", "website", "longitude", "latitude",
 	"pos", "birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
 )


See also:

* mshop/order/manager/base/address/insert/ansi

## address/name

Class name of the used order base address manager implementation

```
mshop/order/manager/base/address/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default order base address manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Order\Manager\Base\Address\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Base\Address\Myaddress
```

then you have to set the this configuration option:

```
 mshop/order/manager/base/address/name = Myaddress
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyAddress"!


## address/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/address/newid/ansi = mshop/order/manager/base/address/newid
```

* Default: mshop/order/manager/base/address/newid
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
 SELECT currval('seq_mord_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mord_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/order/manager/base/address/insert/ansi
* mshop/order/manager/base/address/update/ansi
* mshop/order/manager/base/address/delete/ansi
* mshop/order/manager/base/address/search/ansi
* mshop/order/manager/base/address/count/ansi

## address/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/address/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/base/address/newid

See also:

* mshop/order/manager/base/address/newid/ansi

## address/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/address/search/ansi = 
 SELECT :columns
 	mordbaad."id" AS "order.base.address.id", mordbaad."baseid" AS "order.base.address.baseid",
 	mordbaad."siteid" AS "order.base.address.siteid", mordbaad."addrid" AS "order.base.address.addressid",
 	mordbaad."type" AS "order.base.address.type", mordbaad."company" AS "order.base.address.company",
 	mordbaad."vatid" AS "order.base.address.vatid", mordbaad."salutation" AS "order.base.address.salutation",
 	mordbaad."title" AS "order.base.address.title", mordbaad."firstname" AS "order.base.address.firstname",
 	mordbaad."lastname" AS "order.base.address.lastname", mordbaad."address1" AS "order.base.address.address1",
 	mordbaad."address2" AS "order.base.address.address2", mordbaad."address3" AS "order.base.address.address3",
 	mordbaad."postal" AS "order.base.address.postal", mordbaad."city" AS "order.base.address.city",
 	mordbaad."state" AS "order.base.address.state", mordbaad."countryid" AS "order.base.address.countryid",
 	mordbaad."langid" AS "order.base.address.languageid", mordbaad."telephone" AS "order.base.address.telephone",
 	mordbaad."email" AS "order.base.address.email", mordbaad."telefax" AS "order.base.address.telefax",
 	mordbaad."website" AS "order.base.address.website", mordbaad."longitude" AS "order.base.address.longitude",
 	mordbaad."latitude" AS "order.base.address.latitude", mordbaad."pos" AS "order.base.address.position",
 	mordbaad."mtime" AS "order.base.address.mtime", mordbaad."editor" AS "order.base.address.editor",
 	mordbaad."ctime" AS "order.base.address.ctime", mordbaad."birthday" AS "order.base.address.birthday"
 FROM "mshop_order_base_address" mordbaad
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/base/address/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the order
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

* mshop/order/manager/base/address/insert/ansi
* mshop/order/manager/base/address/update/ansi
* mshop/order/manager/base/address/newid/ansi
* mshop/order/manager/base/address/delete/ansi
* mshop/order/manager/base/address/count/ansi

## address/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/address/search/mysql = 
 SELECT :columns
 	mordbaad."id" AS "order.base.address.id", mordbaad."baseid" AS "order.base.address.baseid",
 	mordbaad."siteid" AS "order.base.address.siteid", mordbaad."addrid" AS "order.base.address.addressid",
 	mordbaad."type" AS "order.base.address.type", mordbaad."company" AS "order.base.address.company",
 	mordbaad."vatid" AS "order.base.address.vatid", mordbaad."salutation" AS "order.base.address.salutation",
 	mordbaad."title" AS "order.base.address.title", mordbaad."firstname" AS "order.base.address.firstname",
 	mordbaad."lastname" AS "order.base.address.lastname", mordbaad."address1" AS "order.base.address.address1",
 	mordbaad."address2" AS "order.base.address.address2", mordbaad."address3" AS "order.base.address.address3",
 	mordbaad."postal" AS "order.base.address.postal", mordbaad."city" AS "order.base.address.city",
 	mordbaad."state" AS "order.base.address.state", mordbaad."countryid" AS "order.base.address.countryid",
 	mordbaad."langid" AS "order.base.address.languageid", mordbaad."telephone" AS "order.base.address.telephone",
 	mordbaad."email" AS "order.base.address.email", mordbaad."telefax" AS "order.base.address.telefax",
 	mordbaad."website" AS "order.base.address.website", mordbaad."longitude" AS "order.base.address.longitude",
 	mordbaad."latitude" AS "order.base.address.latitude", mordbaad."pos" AS "order.base.address.position",
 	mordbaad."mtime" AS "order.base.address.mtime", mordbaad."editor" AS "order.base.address.editor",
 	mordbaad."ctime" AS "order.base.address.ctime", mordbaad."birthday" AS "order.base.address.birthday"
 FROM "mshop_order_base_address" mordbaad
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordbaad."id" AS "order.base.address.id", mordbaad."baseid" AS "order.base.address.baseid",
 	mordbaad."siteid" AS "order.base.address.siteid", mordbaad."addrid" AS "order.base.address.addressid",
 	mordbaad."type" AS "order.base.address.type", mordbaad."company" AS "order.base.address.company",
 	mordbaad."vatid" AS "order.base.address.vatid", mordbaad."salutation" AS "order.base.address.salutation",
 	mordbaad."title" AS "order.base.address.title", mordbaad."firstname" AS "order.base.address.firstname",
 	mordbaad."lastname" AS "order.base.address.lastname", mordbaad."address1" AS "order.base.address.address1",
 	mordbaad."address2" AS "order.base.address.address2", mordbaad."address3" AS "order.base.address.address3",
 	mordbaad."postal" AS "order.base.address.postal", mordbaad."city" AS "order.base.address.city",
 	mordbaad."state" AS "order.base.address.state", mordbaad."countryid" AS "order.base.address.countryid",
 	mordbaad."langid" AS "order.base.address.languageid", mordbaad."telephone" AS "order.base.address.telephone",
 	mordbaad."email" AS "order.base.address.email", mordbaad."telefax" AS "order.base.address.telefax",
 	mordbaad."website" AS "order.base.address.website", mordbaad."longitude" AS "order.base.address.longitude",
 	mordbaad."latitude" AS "order.base.address.latitude", mordbaad."pos" AS "order.base.address.position",
 	mordbaad."mtime" AS "order.base.address.mtime", mordbaad."editor" AS "order.base.address.editor",
 	mordbaad."ctime" AS "order.base.address.ctime", mordbaad."birthday" AS "order.base.address.birthday"
 FROM "mshop_order_base_address" mordbaad
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/base/address/search/ansi

## address/submanagers

List of manager names that can be instantiated by the order base address manager

```
mshop/order/manager/base/address/submanagers = Array
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


## address/update/ansi

Updates an existing order record in the database

```
mshop/order/manager/base/address/update/ansi = 
 UPDATE "mshop_order_base_address"
 SET :names
 	"baseid" = ?, "addrid" = ?, "type" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?, "address2" = ?,
 	"address3" = ?, "postal" = ?, "city" = ?, "state" = ?, "countryid" = ?, "langid" = ?,
 	"telephone" = ?, "email" = ?, "telefax" = ?, "website" = ?, "longitude" = ?, "latitude" = ?,
 	"pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/order/manager/base/address/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/address/insert/ansi
* mshop/order/manager/base/address/newid/ansi
* mshop/order/manager/base/address/delete/ansi
* mshop/order/manager/base/address/search/ansi
* mshop/order/manager/base/address/count/ansi

## address/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/base/address/update/mysql = 
 UPDATE "mshop_order_base_address"
 SET :names
 	"baseid" = ?, "addrid" = ?, "type" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?, "address2" = ?,
 	"address3" = ?, "postal" = ?, "city" = ?, "state" = ?, "countryid" = ?, "langid" = ?,
 	"telephone" = ?, "email" = ?, "telefax" = ?, "website" = ?, "longitude" = ?, "latitude" = ?,
 	"pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_order_base_address"
 SET :names
 	"baseid" = ?, "addrid" = ?, "type" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?, "address2" = ?,
 	"address3" = ?, "postal" = ?, "city" = ?, "state" = ?, "countryid" = ?, "langid" = ?,
 	"telephone" = ?, "email" = ?, "telefax" = ?, "website" = ?, "longitude" = ?, "latitude" = ?,
 	"pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/order/manager/base/address/update/ansi

## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base" mordba
 	:joins
 	WHERE :cond
 	GROUP BY mordba.id, :cols, :val
 	ORDER BY mordba.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/base/aggregate
* Type: string - SQL statement for aggregating order items
* Since: 2014.09

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

* mshop/order/manager/base/insert/ansi
* mshop/order/manager/base/update/ansi
* mshop/order/manager/base/newid/ansi
* mshop/order/manager/base/delete/ansi
* mshop/order/manager/base/search/ansi
* mshop/order/manager/base/count/ansi

## aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base" mordba
 	:joins
 	WHERE :cond
 	GROUP BY mordba.id, :cols, :val
 	ORDER BY mordba.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base" mordba
 	:joins
 	WHERE :cond
 	GROUP BY mordba.id, :cols, :val
 	ORDER BY mordba.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/base/aggregate/ansi

## aggregateavg/ansi

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/base/aggregateavg/ansi = 
```

* Default: 
* Type: string - SQL statement for aggregating the order base items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/base/aggregate/ansi

## aggregateavg/mysql

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/base/aggregateavg/mysql = 
```

* Default: 
* Type: string - SQL statement for aggregating the order base items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/base/aggregateavg/ansi
* mshop/order/manager/base/aggregate/mysql

## aggregatesum/ansi

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/base/aggregatesum/ansi = 
```

* Default: 
* Type: string - SQL statement for aggregating the order base items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/base/aggregate/ansi

## aggregatesum/mysql

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/base/aggregatesum/mysql = 
```

* Default: 
* Type: string - SQL statement for aggregating the order base items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/base/aggregatesum/ansi
* mshop/order/manager/base/aggregate/mysql

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/count/ansi = 
 SELECT COUNT( DISTINCT mordba."id" ) AS "count"
 FROM "mshop_order_base" mordba
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/base/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the order
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

* mshop/order/manager/base/insert/ansi
* mshop/order/manager/base/update/ansi
* mshop/order/manager/base/newid/ansi
* mshop/order/manager/base/delete/ansi
* mshop/order/manager/base/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/count/mysql = 
 SELECT COUNT( DISTINCT mordba."id" ) AS "count"
 FROM "mshop_order_base" mordba
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordba."id" ) AS "count"
 FROM "mshop_order_base" mordba
 :joins
 WHERE :cond


See also:

* mshop/order/manager/base/count/ansi

## coupon/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/coupon/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_coupon" mordbaco
 	:joins
 	WHERE :cond
 	GROUP BY mordbaco.id, :cols, :val
 	ORDER BY mordbaco.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/base/coupon/aggregate
* Type: string - SQL statement for aggregating order items
* Since: 2014.09

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

* mshop/order/manager/base/coupon/insert/ansi
* mshop/order/manager/base/coupon/update/ansi
* mshop/order/manager/base/coupon/newid/ansi
* mshop/order/manager/base/coupon/delete/ansi
* mshop/order/manager/base/coupon/search/ansi
* mshop/order/manager/base/coupon/count/ansi

## coupon/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/coupon/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_coupon" mordbaco
 	:joins
 	WHERE :cond
 	GROUP BY mordbaco.id, :cols, :val
 	ORDER BY mordbaco.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_coupon" mordbaco
 	:joins
 	WHERE :cond
 	GROUP BY mordbaco.id, :cols, :val
 	ORDER BY mordbaco.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/base/coupon/aggregate/ansi

## coupon/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/coupon/count/ansi = 
 SELECT COUNT( DISTINCT mordbaco."id" ) AS "count"
 FROM "mshop_order_base_coupon" mordbaco
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/base/coupon/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the order
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

* mshop/order/manager/base/coupon/insert/ansi
* mshop/order/manager/base/coupon/update/ansi
* mshop/order/manager/base/coupon/newid/ansi
* mshop/order/manager/base/coupon/delete/ansi
* mshop/order/manager/base/coupon/search/ansi

## coupon/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/coupon/count/mysql = 
 SELECT COUNT( DISTINCT mordbaco."id" ) AS "count"
 FROM "mshop_order_base_coupon" mordbaco
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordbaco."id" ) AS "count"
 FROM "mshop_order_base_coupon" mordbaco
 :joins
 WHERE :cond


See also:

* mshop/order/manager/base/coupon/count/ansi

## coupon/decorators/excludes

Excludes decorators added by the "common" option from the order base coupon manager

```
mshop/order/manager/base/coupon/decorators/excludes = Array
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
around the order base coupon manager.

```
 mshop/order/manager/base/coupon/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base coupon manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/coupon/decorators/global
* mshop/order/manager/base/coupon/decorators/local

## coupon/decorators/global

Adds a list of globally available decorators only to the order base coupon manager

```
mshop/order/manager/base/coupon/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order base coupon
manager.

```
 mshop/order/manager/base/coupon/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base coupon manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/coupon/decorators/excludes
* mshop/order/manager/base/coupon/decorators/local

## coupon/decorators/local

Adds a list of local decorators only to the order base coupon manager

```
mshop/order/manager/base/coupon/decorators/local = Array
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
("\Aimeos\MShop\Order\Manager\Base\Coupon\Decorator\*") around the order
base coupon manager.

```
 mshop/order/manager/base/coupon/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Coupon\Decorator\Decorator2" only
to the order base coupon manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/coupon/decorators/excludes
* mshop/order/manager/base/coupon/decorators/global

## coupon/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/coupon/delete/ansi = 
 DELETE FROM "mshop_order_base_coupon"
 WHERE :cond AND siteid = ?
```

* Default: mshop/order/manager/base/coupon/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the order database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/coupon/insert/ansi
* mshop/order/manager/base/coupon/update/ansi
* mshop/order/manager/base/coupon/newid/ansi
* mshop/order/manager/base/coupon/search/ansi
* mshop/order/manager/base/coupon/count/ansi

## coupon/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/coupon/delete/mysql = 
 DELETE FROM "mshop_order_base_coupon"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_order_base_coupon"
 WHERE :cond AND siteid = ?
 

See also:

* mshop/order/manager/base/coupon/delete/ansi

## coupon/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/base/coupon/insert/ansi = 
 INSERT INTO "mshop_order_base_coupon" ( :names
 	"baseid", "ordprodid", "code", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/base/coupon/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/coupon/update/ansi
* mshop/order/manager/base/coupon/newid/ansi
* mshop/order/manager/base/coupon/delete/ansi
* mshop/order/manager/base/coupon/search/ansi
* mshop/order/manager/base/coupon/count/ansi

## coupon/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/base/coupon/insert/mysql = 
 INSERT INTO "mshop_order_base_coupon" ( :names
 	"baseid", "ordprodid", "code", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_order_base_coupon" ( :names
 	"baseid", "ordprodid", "code", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/base/coupon/insert/ansi

## coupon/name

Class name of the used order base coupon manager implementation

```
mshop/order/manager/base/coupon/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default order base coupon manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Order\Manager\Base\Coupon\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Base\Coupon\Mycoupon
```

then you have to set the this configuration option:

```
 mshop/order/manager/base/coupon/name = Mycoupon
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyCoupon"!


## coupon/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/coupon/newid/ansi = mshop/order/manager/base/coupon/newid
```

* Default: mshop/order/manager/base/coupon/newid
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
 SELECT currval('seq_mord_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mord_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/order/manager/base/coupon/insert/ansi
* mshop/order/manager/base/coupon/update/ansi
* mshop/order/manager/base/coupon/delete/ansi
* mshop/order/manager/base/coupon/search/ansi
* mshop/order/manager/base/coupon/count/ansi

## coupon/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/coupon/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/base/coupon/newid

See also:

* mshop/order/manager/base/coupon/newid/ansi

## coupon/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/coupon/search/ansi = 
 SELECT :columns
 	mordbaco."id" AS "order.base.coupon.id", mordbaco."baseid" AS "order.base.coupon.baseid",
 	mordbaco."siteid" AS "order.base.coupon.siteid", mordbaco."ordprodid" AS "order.base.coupon.ordprodid",
 	mordbaco."code" AS "order.base.coupon.code", mordbaco."mtime" AS "order.base.coupon.mtime",
 	mordbaco."editor" AS "order.base.coupon.editor", mordbaco."ctime" AS "order.base.coupon.ctime"
 FROM "mshop_order_base_coupon" mordbaco
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/base/coupon/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the order
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

* mshop/order/manager/base/coupon/insert/ansi
* mshop/order/manager/base/coupon/update/ansi
* mshop/order/manager/base/coupon/newid/ansi
* mshop/order/manager/base/coupon/delete/ansi
* mshop/order/manager/base/coupon/count/ansi

## coupon/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/coupon/search/mysql = 
 SELECT :columns
 	mordbaco."id" AS "order.base.coupon.id", mordbaco."baseid" AS "order.base.coupon.baseid",
 	mordbaco."siteid" AS "order.base.coupon.siteid", mordbaco."ordprodid" AS "order.base.coupon.ordprodid",
 	mordbaco."code" AS "order.base.coupon.code", mordbaco."mtime" AS "order.base.coupon.mtime",
 	mordbaco."editor" AS "order.base.coupon.editor", mordbaco."ctime" AS "order.base.coupon.ctime"
 FROM "mshop_order_base_coupon" mordbaco
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordbaco."id" AS "order.base.coupon.id", mordbaco."baseid" AS "order.base.coupon.baseid",
 	mordbaco."siteid" AS "order.base.coupon.siteid", mordbaco."ordprodid" AS "order.base.coupon.ordprodid",
 	mordbaco."code" AS "order.base.coupon.code", mordbaco."mtime" AS "order.base.coupon.mtime",
 	mordbaco."editor" AS "order.base.coupon.editor", mordbaco."ctime" AS "order.base.coupon.ctime"
 FROM "mshop_order_base_coupon" mordbaco
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/base/coupon/search/ansi

## coupon/submanagers

List of manager names that can be instantiated by the order base coupon manager

```
mshop/order/manager/base/coupon/submanagers = Array
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


## coupon/update/ansi

Updates an existing order record in the database

```
mshop/order/manager/base/coupon/update/ansi = 
 UPDATE "mshop_order_base_coupon"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "code" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/order/manager/base/coupon/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/coupon/insert/ansi
* mshop/order/manager/base/coupon/newid/ansi
* mshop/order/manager/base/coupon/delete/ansi
* mshop/order/manager/base/coupon/search/ansi
* mshop/order/manager/base/coupon/count/ansi

## coupon/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/base/coupon/update/mysql = 
 UPDATE "mshop_order_base_coupon"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "code" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_order_base_coupon"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "code" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/order/manager/base/coupon/update/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the order base manager

```
mshop/order/manager/base/decorators/excludes = Array
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
around the order base manager.

```
 mshop/order/manager/base/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/decorators/global
* mshop/order/manager/base/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order base manager

```
mshop/order/manager/base/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order base
manager.

```
 mshop/order/manager/base/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/decorators/excludes
* mshop/order/manager/base/decorators/local

## decorators/local

Adds a list of local decorators only to the order base manager

```
mshop/order/manager/base/decorators/local = Array
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
("\Aimeos\MShop\Order\Manager\Base\Decorator\*") around the order base
manager.

```
 mshop/order/manager/base/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Decorator\Decorator2" only to the
order base manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/decorators/excludes
* mshop/order/manager/base/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/delete/ansi = 
 DELETE FROM "mshop_order_base"
 WHERE :cond AND siteid = ?
```

* Default: mshop/order/manager/base/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the order database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/insert/ansi
* mshop/order/manager/base/update/ansi
* mshop/order/manager/base/newid/ansi
* mshop/order/manager/base/search/ansi
* mshop/order/manager/base/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/delete/mysql = 
 DELETE FROM "mshop_order_base"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_order_base"
 WHERE :cond AND siteid = ?


See also:

* mshop/order/manager/base/delete/ansi

## insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/base/insert/ansi = 
 INSERT INTO "mshop_order_base" ( :names
 	"customerid", "sitecode", "langid", "currencyid",
 	"price", "costs", "rebate", "tax", "taxflag", "customerref",
 	"comment", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/base/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/update/ansi
* mshop/order/manager/base/newid/ansi
* mshop/order/manager/base/delete/ansi
* mshop/order/manager/base/search/ansi
* mshop/order/manager/base/count/ansi

## insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/base/insert/mysql = 
 INSERT INTO "mshop_order_base" ( :names
 	"customerid", "sitecode", "langid", "currencyid",
 	"price", "costs", "rebate", "tax", "taxflag", "customerref",
 	"comment", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_order_base" ( :names
 	"customerid", "sitecode", "langid", "currencyid",
 	"price", "costs", "rebate", "tax", "taxflag", "customerref",
 	"comment", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/base/insert/ansi

## name

Class name of the used order base manager implementation

```
mshop/order/manager/base/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default order base manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Order\Manager\Base\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Base\Mybase
```

then you have to set the this configuration option:

```
 mshop/order/manager/base/name = Mybase
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyBase"!


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/newid/ansi = mshop/order/manager/base/newid
```

* Default: mshop/order/manager/base/newid
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
 SELECT currval('seq_mord_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mord_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/order/manager/base/insert/ansi
* mshop/order/manager/base/update/ansi
* mshop/order/manager/base/delete/ansi
* mshop/order/manager/base/search/ansi
* mshop/order/manager/base/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/base/newid

See also:

* mshop/order/manager/base/newid/ansi

## product/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/product/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_product" mordbapr
 	:joins
 	WHERE :cond
 	GROUP BY mordbapr.id, :cols, :val
 	ORDER BY mordbapr.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/base/product/aggregate
* Type: string - SQL statement for aggregating order items
* Since: 2014.09

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

* mshop/order/manager/base/product/insert/ansi
* mshop/order/manager/base/product/update/ansi
* mshop/order/manager/base/product/newid/ansi
* mshop/order/manager/base/product/delete/ansi
* mshop/order/manager/base/product/search/ansi
* mshop/order/manager/base/product/count/ansi

## product/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/product/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_product" mordbapr
 	:joins
 	WHERE :cond
 	GROUP BY mordbapr.id, :cols, :val
 	ORDER BY mordbapr.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_product" mordbapr
 	:joins
 	WHERE :cond
 	GROUP BY mordbapr.id, :cols, :val
 	ORDER BY mordbapr.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/base/product/aggregate/ansi

## product/aggregateavg/ansi

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/base/product/aggregateavg/ansi = 
```

* Default: 
* Type: string - SQL statement for aggregating the order product items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/base/product/aggregate/ansi

## product/aggregateavg/mysql

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/base/product/aggregateavg/mysql = 
```

* Default: 
* Type: string - SQL statement for aggregating the order product items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/base/product/aggregateavg/ansi
* mshop/order/manager/base/product/aggregate/mysql

## product/aggregatesum/ansi

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/base/product/aggregatesum/ansi = 
```

* Default: 
* Type: string - SQL statement for aggregating the order product items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/base/product/aggregate/ansi

## product/aggregatesum/mysql

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/base/product/aggregatesum/mysql = 
```

* Default: 
* Type: string - SQL statement for aggregating the order product items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/base/product/aggregatesum/ansi
* mshop/order/manager/base/product/aggregate/mysql

## product/attribute/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/product/attribute/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_product_attr" mordbaprat
 	:joins
 	WHERE :cond
 	GROUP BY mordbaprat.id, :cols, :val
 	ORDER BY mordbaprat.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/base/product/attribute/aggregate
* Type: string - SQL statement for aggregating order items
* Since: 2014.09

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

* mshop/order/manager/base/product/attribute/insert/ansi
* mshop/order/manager/base/product/attribute/update/ansi
* mshop/order/manager/base/product/attribute/newid/ansi
* mshop/order/manager/base/product/attribute/delete/ansi
* mshop/order/manager/base/product/attribute/search/ansi
* mshop/order/manager/base/product/attribute/count/ansi

## product/attribute/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/product/attribute/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_product_attr" mordbaprat
 	:joins
 	WHERE :cond
 	GROUP BY mordbaprat.id, :cols, :val
 	ORDER BY mordbaprat.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_product_attr" mordbaprat
 	:joins
 	WHERE :cond
 	GROUP BY mordbaprat.id, :cols, :val
 	ORDER BY mordbaprat.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/base/product/attribute/aggregate/ansi

## product/attribute/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/product/attribute/count/ansi = 
 SELECT COUNT( DISTINCT mordbaprat."id" ) AS "count"
 FROM "mshop_order_base_product_attr" mordbaprat
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/base/product/attribute/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the order
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

* mshop/order/manager/base/product/attribute/insert/ansi
* mshop/order/manager/base/product/attribute/update/ansi
* mshop/order/manager/base/product/attribute/newid/ansi
* mshop/order/manager/base/product/attribute/delete/ansi
* mshop/order/manager/base/product/attribute/search/ansi

## product/attribute/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/product/attribute/count/mysql = 
 SELECT COUNT( DISTINCT mordbaprat."id" ) AS "count"
 FROM "mshop_order_base_product_attr" mordbaprat
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordbaprat."id" ) AS "count"
 FROM "mshop_order_base_product_attr" mordbaprat
 :joins
 WHERE :cond


See also:

* mshop/order/manager/base/product/attribute/count/ansi

## product/attribute/decorators/excludes

Excludes decorators added by the "common" option from the order base product attribute manager

```
mshop/order/manager/base/product/attribute/decorators/excludes = Array
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
around the order base product attribute manager.

```
 mshop/order/manager/base/product/attribute/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base product attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/product/attribute/decorators/global
* mshop/order/manager/base/product/attribute/decorators/local

## product/attribute/decorators/global

Adds a list of globally available decorators only to the order base product attribute manager

```
mshop/order/manager/base/product/attribute/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order base
product attribute manager.

```
 mshop/order/manager/base/product/attribute/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base product attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/product/attribute/decorators/excludes
* mshop/order/manager/base/product/attribute/decorators/local

## product/attribute/decorators/local

Adds a list of local decorators only to the order base product attribute manager

```
mshop/order/manager/base/product/attribute/decorators/local = Array
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
("\Aimeos\MShop\Order\Manager\Base\Product\Attribute\Decorator\*")
around the order base product attribute manager.

```
 mshop/order/manager/base/product/attribute/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Product\Attribute\Decorator\Decorator2"
only to the order base product attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/product/attribute/decorators/excludes
* mshop/order/manager/base/product/attribute/decorators/global

## product/attribute/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/product/attribute/delete/ansi = 
 DELETE FROM "mshop_order_base_product_attr"
 WHERE :cond AND siteid = ?
```

* Default: mshop/order/manager/base/product/attribute/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the order database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/product/attribute/insert/ansi
* mshop/order/manager/base/product/attribute/update/ansi
* mshop/order/manager/base/product/attribute/newid/ansi
* mshop/order/manager/base/product/attribute/search/ansi
* mshop/order/manager/base/product/attribute/count/ansi

## product/attribute/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/product/attribute/delete/mysql = 
 DELETE FROM "mshop_order_base_product_attr"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_order_base_product_attr"
 WHERE :cond AND siteid = ?


See also:

* mshop/order/manager/base/product/attribute/delete/ansi

## product/attribute/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/base/product/attribute/insert/ansi = 
 INSERT INTO "mshop_order_base_product_attr" ( :names
 	"attrid", "parentid", "type", "code", "value",
 	"quantity", "price", "name", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/base/product/attribute/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/product/attribute/update/ansi
* mshop/order/manager/base/product/attribute/newid/ansi
* mshop/order/manager/base/product/attribute/delete/ansi
* mshop/order/manager/base/product/attribute/search/ansi
* mshop/order/manager/base/product/attribute/count/ansi

## product/attribute/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/base/product/attribute/insert/mysql = 
 INSERT INTO "mshop_order_base_product_attr" ( :names
 	"attrid", "parentid", "type", "code", "value",
 	"quantity", "price", "name", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_order_base_product_attr" ( :names
 	"attrid", "parentid", "type", "code", "value",
 	"quantity", "price", "name", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/base/product/attribute/insert/ansi

## product/attribute/name

Class name of the used order base product attribute manager implementation

```
mshop/order/manager/base/product/attribute/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default order base product attribute manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Order\Manager\Base\Product\Attribute\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Base\Product\Attribute\Myattribute
```

then you have to set the this configuration option:

```
 mshop/order/manager/base/product/attribute/name = Myattribute
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyAttribute"!


## product/attribute/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/product/attribute/newid/ansi = mshop/order/manager/base/product/attribute/newid
```

* Default: mshop/order/manager/base/product/attribute/newid
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
 SELECT currval('seq_mord_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mord_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/order/manager/base/product/attribute/insert/ansi
* mshop/order/manager/base/product/attribute/update/ansi
* mshop/order/manager/base/product/attribute/delete/ansi
* mshop/order/manager/base/product/attribute/search/ansi
* mshop/order/manager/base/product/attribute/count/ansi

## product/attribute/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/product/attribute/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/base/product/attribute/newid

See also:

* mshop/order/manager/base/product/attribute/newid/ansi

## product/attribute/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/product/attribute/search/ansi = 
 SELECT :columns
 	mordbaprat."id" AS "order.base.product.attribute.id", mordbaprat."siteid" AS "order.base.product.attribute.siteid",
 	mordbaprat."attrid" AS "order.base.product.attribute.attributeid", mordbaprat."parentid" AS "order.base.product.attribute.parentid",
 	mordbaprat."type" AS "order.base.product.attribute.type", mordbaprat."code" AS "order.base.product.attribute.code",
 	mordbaprat."value" AS "order.base.product.attribute.value", mordbaprat."quantity" AS "order.base.product.attribute.quantity",
 	mordbaprat."name" AS "order.base.product.attribute.name", mordbaprat."mtime" AS "order.base.product.attribute.mtime",
 	mordbaprat."editor" AS "order.base.product.attribute.editor", mordbaprat."ctime" AS "order.base.product.attribute.ctime",
 	mordbaprat."price" AS "order.base.product.attribute.price"
 FROM "mshop_order_base_product_attr" mordbaprat
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/base/product/attribute/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the order
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

* mshop/order/manager/base/product/attribute/insert/ansi
* mshop/order/manager/base/product/attribute/update/ansi
* mshop/order/manager/base/product/attribute/newid/ansi
* mshop/order/manager/base/product/attribute/delete/ansi
* mshop/order/manager/base/product/attribute/count/ansi

## product/attribute/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/product/attribute/search/mysql = 
 SELECT :columns
 	mordbaprat."id" AS "order.base.product.attribute.id", mordbaprat."siteid" AS "order.base.product.attribute.siteid",
 	mordbaprat."attrid" AS "order.base.product.attribute.attributeid", mordbaprat."parentid" AS "order.base.product.attribute.parentid",
 	mordbaprat."type" AS "order.base.product.attribute.type", mordbaprat."code" AS "order.base.product.attribute.code",
 	mordbaprat."value" AS "order.base.product.attribute.value", mordbaprat."quantity" AS "order.base.product.attribute.quantity",
 	mordbaprat."name" AS "order.base.product.attribute.name", mordbaprat."mtime" AS "order.base.product.attribute.mtime",
 	mordbaprat."editor" AS "order.base.product.attribute.editor", mordbaprat."ctime" AS "order.base.product.attribute.ctime",
 	mordbaprat."price" AS "order.base.product.attribute.price"
 FROM "mshop_order_base_product_attr" mordbaprat
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordbaprat."id" AS "order.base.product.attribute.id", mordbaprat."siteid" AS "order.base.product.attribute.siteid",
 	mordbaprat."attrid" AS "order.base.product.attribute.attributeid", mordbaprat."parentid" AS "order.base.product.attribute.parentid",
 	mordbaprat."type" AS "order.base.product.attribute.type", mordbaprat."code" AS "order.base.product.attribute.code",
 	mordbaprat."value" AS "order.base.product.attribute.value", mordbaprat."quantity" AS "order.base.product.attribute.quantity",
 	mordbaprat."name" AS "order.base.product.attribute.name", mordbaprat."mtime" AS "order.base.product.attribute.mtime",
 	mordbaprat."editor" AS "order.base.product.attribute.editor", mordbaprat."ctime" AS "order.base.product.attribute.ctime",
 	mordbaprat."price" AS "order.base.product.attribute.price"
 FROM "mshop_order_base_product_attr" mordbaprat
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/base/product/attribute/search/ansi

## product/attribute/submanagers

List of manager names that can be instantiated by the order base product attribute manager

```
mshop/order/manager/base/product/attribute/submanagers = Array
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


## product/attribute/update/ansi

Updates an existing order record in the database

```
mshop/order/manager/base/product/attribute/update/ansi = 
```

* Default: 
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/product/attribute/insert/ansi
* mshop/order/manager/base/product/attribute/newid/ansi
* mshop/order/manager/base/product/attribute/delete/ansi
* mshop/order/manager/base/product/attribute/search/ansi
* mshop/order/manager/base/product/attribute/count/ansi

## product/attribute/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/base/product/attribute/update/mysql = 
```

* Default: 

See also:

* mshop/order/manager/base/product/attribute/update/ansi

## product/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/product/count/ansi = 
 SELECT COUNT( DISTINCT mordbapr."id" ) AS "count"
 FROM "mshop_order_base_product" mordbapr
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/base/product/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the order
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

* mshop/order/manager/base/product/insert/ansi
* mshop/order/manager/base/product/update/ansi
* mshop/order/manager/base/product/newid/ansi
* mshop/order/manager/base/product/delete/ansi
* mshop/order/manager/base/product/search/ansi

## product/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/product/count/mysql = 
 SELECT COUNT( DISTINCT mordbapr."id" ) AS "count"
 FROM "mshop_order_base_product" mordbapr
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordbapr."id" ) AS "count"
 FROM "mshop_order_base_product" mordbapr
 :joins
 WHERE :cond


See also:

* mshop/order/manager/base/product/count/ansi

## product/decorators/excludes

Excludes decorators added by the "common" option from the order base product manager

```
mshop/order/manager/base/product/decorators/excludes = Array
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
around the order base product manager.

```
 mshop/order/manager/base/product/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base product manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/product/decorators/global
* mshop/order/manager/base/product/decorators/local

## product/decorators/global

Adds a list of globally available decorators only to the order base product manager

```
mshop/order/manager/base/product/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order base
product manager.

```
 mshop/order/manager/base/product/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base product manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/product/decorators/excludes
* mshop/order/manager/base/product/decorators/local

## product/decorators/local

Adds a list of local decorators only to the order base product manager

```
mshop/order/manager/base/product/decorators/local = Array
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
("\Aimeos\MShop\Order\Manager\Base\Product\Decorator\*") around the
order base product manager.

```
 mshop/order/manager/base/product/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Product\Decorator\Decorator2" only
to the order base product manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/product/decorators/excludes
* mshop/order/manager/base/product/decorators/global

## product/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/product/delete/ansi = 
 DELETE FROM "mshop_order_base_product"
 WHERE :cond AND siteid = ?
```

* Default: mshop/order/manager/base/product/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the order database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/product/insert/ansi
* mshop/order/manager/base/product/update/ansi
* mshop/order/manager/base/product/newid/ansi
* mshop/order/manager/base/product/search/ansi
* mshop/order/manager/base/product/count/ansi

## product/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/product/delete/mysql = 
 DELETE FROM "mshop_order_base_product"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_order_base_product"
 WHERE :cond AND siteid = ?


See also:

* mshop/order/manager/base/product/delete/ansi

## product/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/base/product/insert/ansi = 
 INSERT INTO "mshop_order_base_product" ( :names
 	"baseid", "ordprodid", "ordaddrid", "type", "parentprodid", "prodid", "prodcode",
 	"vendor", "stocktype", "name", "description", "mediaurl", "timeframe",
 	"quantity", "currencyid", "price", "costs", "rebate", "tax", "taxrate", "taxflag",
 	"flags", "statuspayment", "statusdelivery", "pos", "mtime", "editor", "target", "qtyopen", "notes",
 	"siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/base/product/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/product/update/ansi
* mshop/order/manager/base/product/newid/ansi
* mshop/order/manager/base/product/delete/ansi
* mshop/order/manager/base/product/search/ansi
* mshop/order/manager/base/product/count/ansi

## product/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/base/product/insert/mysql = 
 INSERT INTO "mshop_order_base_product" ( :names
 	"baseid", "ordprodid", "ordaddrid", "type", "parentprodid", "prodid", "prodcode",
 	"vendor", "stocktype", "name", "description", "mediaurl", "timeframe",
 	"quantity", "currencyid", "price", "costs", "rebate", "tax", "taxrate", "taxflag",
 	"flags", "statuspayment", "statusdelivery", "pos", "mtime", "editor", "target", "qtyopen", "notes",
 	"siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_order_base_product" ( :names
 	"baseid", "ordprodid", "ordaddrid", "type", "parentprodid", "prodid", "prodcode",
 	"vendor", "stocktype", "name", "description", "mediaurl", "timeframe",
 	"quantity", "currencyid", "price", "costs", "rebate", "tax", "taxrate", "taxflag",
 	"flags", "statuspayment", "statusdelivery", "pos", "mtime", "editor", "target", "qtyopen", "notes",
 	"siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/base/product/insert/ansi

## product/name

Class name of the used order base product manager implementation

```
mshop/order/manager/base/product/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default order base product manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Order\Manager\Base\Product\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Base\Product\Myproduct
```

then you have to set the this configuration option:

```
 mshop/order/manager/base/product/name = Myproduct
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyProduct"!


## product/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/product/newid/ansi = mshop/order/manager/base/product/newid
```

* Default: mshop/order/manager/base/product/newid
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
 SELECT currval('seq_mord_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mord_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/order/manager/base/product/insert/ansi
* mshop/order/manager/base/product/update/ansi
* mshop/order/manager/base/product/delete/ansi
* mshop/order/manager/base/product/search/ansi
* mshop/order/manager/base/product/count/ansi

## product/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/product/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/base/product/newid

See also:

* mshop/order/manager/base/product/newid/ansi

## product/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/product/search/ansi = 
 SELECT :columns
 	mordbapr."id" AS "order.base.product.id", mordbapr."baseid" AS "order.base.product.baseid",
 	mordbapr."siteid" AS "order.base.product.siteid", mordbapr."ordprodid" AS "order.base.product.orderproductid",
 	mordbapr."prodid" AS "order.base.product.productid", mordbapr."prodcode" AS "order.base.product.prodcode",
 	mordbapr."description" AS "order.base.product.description", mordbapr."stocktype" AS "order.base.product.stocktype",
 	mordbapr."type" AS "order.base.product.type", mordbapr."name" AS "order.base.product.name",
 	mordbapr."mediaurl" AS "order.base.product.mediaurl", mordbapr."timeframe" AS "order.base.product.timeframe",
 	mordbapr."quantity" AS "order.base.product.quantity", mordbapr."currencyid" AS "order.base.product.currencyid",
 	mordbapr."price" AS "order.base.product.price", mordbapr."costs" AS "order.base.product.costs",
 	mordbapr."rebate" AS "order.base.product.rebate", mordbapr."tax" AS "order.base.product.taxvalue",
 	mordbapr."taxrate" AS "order.base.product.taxrates", mordbapr."taxflag" AS "order.base.product.taxflag",
 	mordbapr."flags" AS "order.base.product.flags", mordbapr."statusdelivery" AS "order.base.product.statusdelivery",
 	mordbapr."pos" AS "order.base.product.position", mordbapr."mtime" AS "order.base.product.mtime",
 	mordbapr."editor" AS "order.base.product.editor", mordbapr."ctime" AS "order.base.product.ctime",
 	mordbapr."target" AS "order.base.product.target", mordbapr."ordaddrid" AS "order.base.product.orderaddressid",
 	mordbapr."vendor" AS "order.base.product.vendor",
 	mordbapr."qtyopen" AS "order.base.product.qtyopen", mordbapr."notes" AS "order.base.product.notes",
 	mordbapr."statuspayment" AS "order.base.product.statuspayment", mordbapr."parentprodid" AS "order.base.product.parentproductid"
 FROM "mshop_order_base_product" mordbapr
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mordbapr."id", mordbapr."baseid", mordbapr."siteid", mordbapr."ordprodid", mordbapr."prodid",
 	mordbapr."prodcode", mordbapr."description", mordbapr."stocktype", mordbapr."type",
 	mordbapr."name", mordbapr."mediaurl", mordbapr."timeframe", mordbapr."quantity",
 	mordbapr."currencyid", mordbapr."price", mordbapr."costs", mordbapr."rebate", mordbapr."tax",
 	mordbapr."taxrate", mordbapr."taxflag", mordbapr."flags", mordbapr."statusdelivery", mordbapr."pos",
 	mordbapr."mtime", mordbapr."editor", mordbapr."ctime", mordbapr."target", mordbapr."ordaddrid",
 	mordbapr."vendor", mordbapr."qtyopen", mordbapr."notes",
 	mordbapr."statuspayment", mordbapr."parentprodid"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/base/product/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the order
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

* mshop/order/manager/base/product/insert/ansi
* mshop/order/manager/base/product/update/ansi
* mshop/order/manager/base/product/newid/ansi
* mshop/order/manager/base/product/delete/ansi
* mshop/order/manager/base/product/count/ansi

## product/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/product/search/mysql = 
 SELECT :columns
 	mordbapr."id" AS "order.base.product.id", mordbapr."baseid" AS "order.base.product.baseid",
 	mordbapr."siteid" AS "order.base.product.siteid", mordbapr."ordprodid" AS "order.base.product.orderproductid",
 	mordbapr."prodid" AS "order.base.product.productid", mordbapr."prodcode" AS "order.base.product.prodcode",
 	mordbapr."description" AS "order.base.product.description", mordbapr."stocktype" AS "order.base.product.stocktype",
 	mordbapr."type" AS "order.base.product.type", mordbapr."name" AS "order.base.product.name",
 	mordbapr."mediaurl" AS "order.base.product.mediaurl", mordbapr."timeframe" AS "order.base.product.timeframe",
 	mordbapr."quantity" AS "order.base.product.quantity", mordbapr."currencyid" AS "order.base.product.currencyid",
 	mordbapr."price" AS "order.base.product.price", mordbapr."costs" AS "order.base.product.costs",
 	mordbapr."rebate" AS "order.base.product.rebate", mordbapr."tax" AS "order.base.product.taxvalue",
 	mordbapr."taxrate" AS "order.base.product.taxrates", mordbapr."taxflag" AS "order.base.product.taxflag",
 	mordbapr."flags" AS "order.base.product.flags", mordbapr."statusdelivery" AS "order.base.product.statusdelivery",
 	mordbapr."pos" AS "order.base.product.position", mordbapr."mtime" AS "order.base.product.mtime",
 	mordbapr."editor" AS "order.base.product.editor", mordbapr."ctime" AS "order.base.product.ctime",
 	mordbapr."target" AS "order.base.product.target", mordbapr."ordaddrid" AS "order.base.product.orderaddressid",
 	mordbapr."vendor" AS "order.base.product.vendor",
 	mordbapr."qtyopen" AS "order.base.product.qtyopen", mordbapr."notes" AS "order.base.product.notes",
 	mordbapr."statuspayment" AS "order.base.product.statuspayment", mordbapr."parentprodid" AS "order.base.product.parentproductid"
 FROM "mshop_order_base_product" mordbapr
 :joins
 WHERE :cond
 GROUP BY :group mordbapr."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordbapr."id" AS "order.base.product.id", mordbapr."baseid" AS "order.base.product.baseid",
 	mordbapr."siteid" AS "order.base.product.siteid", mordbapr."ordprodid" AS "order.base.product.orderproductid",
 	mordbapr."prodid" AS "order.base.product.productid", mordbapr."prodcode" AS "order.base.product.prodcode",
 	mordbapr."description" AS "order.base.product.description", mordbapr."stocktype" AS "order.base.product.stocktype",
 	mordbapr."type" AS "order.base.product.type", mordbapr."name" AS "order.base.product.name",
 	mordbapr."mediaurl" AS "order.base.product.mediaurl", mordbapr."timeframe" AS "order.base.product.timeframe",
 	mordbapr."quantity" AS "order.base.product.quantity", mordbapr."currencyid" AS "order.base.product.currencyid",
 	mordbapr."price" AS "order.base.product.price", mordbapr."costs" AS "order.base.product.costs",
 	mordbapr."rebate" AS "order.base.product.rebate", mordbapr."tax" AS "order.base.product.taxvalue",
 	mordbapr."taxrate" AS "order.base.product.taxrates", mordbapr."taxflag" AS "order.base.product.taxflag",
 	mordbapr."flags" AS "order.base.product.flags", mordbapr."statusdelivery" AS "order.base.product.statusdelivery",
 	mordbapr."pos" AS "order.base.product.position", mordbapr."mtime" AS "order.base.product.mtime",
 	mordbapr."editor" AS "order.base.product.editor", mordbapr."ctime" AS "order.base.product.ctime",
 	mordbapr."target" AS "order.base.product.target", mordbapr."ordaddrid" AS "order.base.product.orderaddressid",
 	mordbapr."vendor" AS "order.base.product.vendor",
 	mordbapr."qtyopen" AS "order.base.product.qtyopen", mordbapr."notes" AS "order.base.product.notes",
 	mordbapr."statuspayment" AS "order.base.product.statuspayment", mordbapr."parentprodid" AS "order.base.product.parentproductid"
 FROM "mshop_order_base_product" mordbapr
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mordbapr."id", mordbapr."baseid", mordbapr."siteid", mordbapr."ordprodid", mordbapr."prodid",
 	mordbapr."prodcode", mordbapr."description", mordbapr."stocktype", mordbapr."type",
 	mordbapr."name", mordbapr."mediaurl", mordbapr."timeframe", mordbapr."quantity",
 	mordbapr."currencyid", mordbapr."price", mordbapr."costs", mordbapr."rebate", mordbapr."tax",
 	mordbapr."taxrate", mordbapr."taxflag", mordbapr."flags", mordbapr."statusdelivery", mordbapr."pos",
 	mordbapr."mtime", mordbapr."editor", mordbapr."ctime", mordbapr."target", mordbapr."ordaddrid",
 	mordbapr."vendor", mordbapr."qtyopen", mordbapr."notes",
 	mordbapr."statuspayment", mordbapr."parentprodid"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/base/product/search/ansi

## product/submanagers

List of manager names that can be instantiated by the order base product manager

```
mshop/order/manager/base/product/submanagers = Array
(
    [0] => attribute
)
```

* Default: Array
(
    [0] => attribute
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


## product/update/ansi

Updates an existing order record in the database

```
mshop/order/manager/base/product/update/ansi = 
 UPDATE "mshop_order_base_product"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "ordaddrid" = ?, "type" = ?, "parentprodid" = ?,
 	"prodid" = ?, "prodcode" = ?, "vendor" = ?, "stocktype" = ?,
 	"name" = ?, "description" = ?, "mediaurl" = ?, "timeframe" = ?, "quantity" = ?,
 	"currencyid" = ?, "price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "flags" = ?, "statuspayment" = ?, "statusdelivery" = ?, "pos" = ?,
 	"mtime" = ?, "editor" = ?, "target" = ?, "qtyopen" = ?, "notes" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/order/manager/base/product/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/product/insert/ansi
* mshop/order/manager/base/product/newid/ansi
* mshop/order/manager/base/product/delete/ansi
* mshop/order/manager/base/product/search/ansi
* mshop/order/manager/base/product/count/ansi

## product/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/base/product/update/mysql = 
 UPDATE "mshop_order_base_product"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "ordaddrid" = ?, "type" = ?, "parentprodid" = ?,
 	"prodid" = ?, "prodcode" = ?, "vendor" = ?, "stocktype" = ?,
 	"name" = ?, "description" = ?, "mediaurl" = ?, "timeframe" = ?, "quantity" = ?,
 	"currencyid" = ?, "price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "flags" = ?, "statuspayment" = ?, "statusdelivery" = ?, "pos" = ?,
 	"mtime" = ?, "editor" = ?, "target" = ?, "qtyopen" = ?, "notes" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_order_base_product"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "ordaddrid" = ?, "type" = ?, "parentprodid" = ?,
 	"prodid" = ?, "prodcode" = ?, "vendor" = ?, "stocktype" = ?,
 	"name" = ?, "description" = ?, "mediaurl" = ?, "timeframe" = ?, "quantity" = ?,
 	"currencyid" = ?, "price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "flags" = ?, "statuspayment" = ?, "statusdelivery" = ?, "pos" = ?,
 	"mtime" = ?, "editor" = ?, "target" = ?, "qtyopen" = ?, "notes" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/order/manager/base/product/update/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/search/ansi = 
 SELECT :columns
 	mordba."id" AS "order.base.id", mordba."siteid" AS "order.base.siteid",
 	mordba."sitecode" AS "order.base.sitecode", mordba."customerid" AS "order.base.customerid",
 	mordba."langid" AS "order.base.languageid", mordba."currencyid" AS "order.base.currencyid",
 	mordba."price" AS "order.base.price", mordba."costs" AS "order.base.costs",
 	mordba."rebate" AS "order.base.rebate", mordba."tax" AS "order.base.taxvalue",
 	mordba."taxflag" AS "order.base.taxflag", mordba."customerref" AS "order.base.customerref",
 	mordba."comment" AS "order.base.comment", mordba."mtime" AS "order.base.mtime",
 	mordba."ctime" AS "order.base.ctime", mordba."editor" AS "order.base.editor"
 FROM "mshop_order_base" mordba
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mordba."id", mordba."siteid", mordba."sitecode", mordba."customerid", mordba."langid",
 	mordba."currencyid", mordba."price", mordba."costs", mordba."rebate", mordba."tax",
 	mordba."taxflag", mordba."customerref", mordba."comment", mordba."mtime", mordba."ctime",
 	mordba."editor"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/base/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the order
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

* mshop/order/manager/base/insert/ansi
* mshop/order/manager/base/update/ansi
* mshop/order/manager/base/newid/ansi
* mshop/order/manager/base/delete/ansi
* mshop/order/manager/base/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/search/mysql = 
 SELECT :columns
 	mordba."id" AS "order.base.id", mordba."siteid" AS "order.base.siteid",
 	mordba."sitecode" AS "order.base.sitecode", mordba."customerid" AS "order.base.customerid",
 	mordba."langid" AS "order.base.languageid", mordba."currencyid" AS "order.base.currencyid",
 	mordba."price" AS "order.base.price", mordba."costs" AS "order.base.costs",
 	mordba."rebate" AS "order.base.rebate", mordba."tax" AS "order.base.taxvalue",
 	mordba."taxflag" AS "order.base.taxflag", mordba."customerref" AS "order.base.customerref",
 	mordba."comment" AS "order.base.comment", mordba."mtime" AS "order.base.mtime",
 	mordba."ctime" AS "order.base.ctime", mordba."editor" AS "order.base.editor"
 FROM "mshop_order_base" mordba
 :joins
 WHERE :cond
 GROUP BY :group mordba."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordba."id" AS "order.base.id", mordba."siteid" AS "order.base.siteid",
 	mordba."sitecode" AS "order.base.sitecode", mordba."customerid" AS "order.base.customerid",
 	mordba."langid" AS "order.base.languageid", mordba."currencyid" AS "order.base.currencyid",
 	mordba."price" AS "order.base.price", mordba."costs" AS "order.base.costs",
 	mordba."rebate" AS "order.base.rebate", mordba."tax" AS "order.base.taxvalue",
 	mordba."taxflag" AS "order.base.taxflag", mordba."customerref" AS "order.base.customerref",
 	mordba."comment" AS "order.base.comment", mordba."mtime" AS "order.base.mtime",
 	mordba."ctime" AS "order.base.ctime", mordba."editor" AS "order.base.editor"
 FROM "mshop_order_base" mordba
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mordba."id", mordba."siteid", mordba."sitecode", mordba."customerid", mordba."langid",
 	mordba."currencyid", mordba."price", mordba."costs", mordba."rebate", mordba."tax",
 	mordba."taxflag", mordba."customerref", mordba."comment", mordba."mtime", mordba."ctime",
 	mordba."editor"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/base/search/ansi

## service/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/service/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_service" mordbase
 	:joins
 	WHERE :cond
 	GROUP BY mordbase.id, :cols, :val
 	ORDER BY mordbase.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/base/service/aggregate
* Type: string - SQL statement for aggregating order items
* Since: 2014.09

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

* mshop/order/manager/base/service/insert/ansi
* mshop/order/manager/base/service/update/ansi
* mshop/order/manager/base/service/newid/ansi
* mshop/order/manager/base/service/delete/ansi
* mshop/order/manager/base/service/search/ansi
* mshop/order/manager/base/service/count/ansi

## service/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/service/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_service" mordbase
 	:joins
 	WHERE :cond
 	GROUP BY mordbase.id, :cols, :val
 	ORDER BY mordbase.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_service" mordbase
 	:joins
 	WHERE :cond
 	GROUP BY mordbase.id, :cols, :val
 	ORDER BY mordbase.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/base/service/aggregate/ansi

## service/aggregateavg/ansi

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/base/service/aggregateavg/ansi = 
```

* Default: 
* Type: string - SQL statement for aggregating the order service items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/base/service/aggregate/ansi

## service/aggregateavg/mysql

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/base/service/aggregateavg/mysql = 
```

* Default: 
* Type: string - SQL statement for aggregating the order service items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/base/service/aggregateavg/ansi
* mshop/order/manager/base/service/aggregate/mysql

## service/aggregatesum/ansi

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/base/service/aggregatesum/ansi = 
```

* Default: 
* Type: string - SQL statement for aggregating the order service items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/base/service/aggregate/ansi

## service/aggregatesum/mysql

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/base/service/aggregatesum/mysql = 
```

* Default: 
* Type: string - SQL statement for aggregating the order service items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/base/service/aggregatesum/ansi
* mshop/order/manager/base/service/aggregate/mysql

## service/attribute/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/service/attribute/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_service_attr" mordbaseat
 	:joins
 	WHERE :cond
 	GROUP BY mordbaseat.id, :cols, :val
 	ORDER BY mordbaseat.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/base/service/attribute/aggregate
* Type: string - SQL statement for aggregating order items
* Since: 2014.09

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

* mshop/order/manager/base/service/attribute/insert/ansi
* mshop/order/manager/base/service/attribute/update/ansi
* mshop/order/manager/base/service/attribute/newid/ansi
* mshop/order/manager/base/service/attribute/delete/ansi
* mshop/order/manager/base/service/attribute/search/ansi
* mshop/order/manager/base/service/attribute/count/ansi

## service/attribute/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/base/service/attribute/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_service_attr" mordbaseat
 	:joins
 	WHERE :cond
 	GROUP BY mordbaseat.id, :cols, :val
 	ORDER BY mordbaseat.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_base_service_attr" mordbaseat
 	:joins
 	WHERE :cond
 	GROUP BY mordbaseat.id, :cols, :val
 	ORDER BY mordbaseat.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/base/service/attribute/aggregate/ansi

## service/attribute/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/service/attribute/count/ansi = 
 SELECT COUNT( DISTINCT mordbaseat."id" ) AS "count"
 FROM "mshop_order_base_service_attr" mordbaseat
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/base/service/attribute/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the order
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

* mshop/order/manager/base/service/attribute/insert/ansi
* mshop/order/manager/base/service/attribute/update/ansi
* mshop/order/manager/base/service/attribute/newid/ansi
* mshop/order/manager/base/service/attribute/delete/ansi
* mshop/order/manager/base/service/attribute/search/ansi

## service/attribute/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/service/attribute/count/mysql = 
 SELECT COUNT( DISTINCT mordbaseat."id" ) AS "count"
 FROM "mshop_order_base_service_attr" mordbaseat
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordbaseat."id" ) AS "count"
 FROM "mshop_order_base_service_attr" mordbaseat
 :joins
 WHERE :cond


See also:

* mshop/order/manager/base/service/attribute/count/ansi

## service/attribute/decorators/excludes

Excludes decorators added by the "common" option from the order base service attribute manager

```
mshop/order/manager/base/service/attribute/decorators/excludes = Array
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
around the order base service attribute manager.

```
 mshop/order/manager/base/service/attribute/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base service attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/service/attribute/decorators/global
* mshop/order/manager/base/service/attribute/decorators/local

## service/attribute/decorators/global

Adds a list of globally available decorators only to the order base service attribute manager

```
mshop/order/manager/base/service/attribute/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order base
service attribute manager.

```
 mshop/order/manager/base/service/attribute/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base service attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/service/attribute/decorators/excludes
* mshop/order/manager/base/service/attribute/decorators/local

## service/attribute/decorators/local

Adds a list of local decorators only to the order base service attribute manager

```
mshop/order/manager/base/service/attribute/decorators/local = Array
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
("\Aimeos\MShop\Order\Manager\Base\Service\Attribute\Decorator\*")
around the order base service attribute manager.

```
 mshop/order/manager/base/service/attribute/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Service\Attribute\Decorator\Decorator2"
only to the order base service attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/service/attribute/decorators/excludes
* mshop/order/manager/base/service/attribute/decorators/global

## service/attribute/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/service/attribute/delete/ansi = 
 DELETE FROM "mshop_order_base_service_attr"
 WHERE :cond AND siteid = ?
```

* Default: mshop/order/manager/base/service/attribute/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the order database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/service/attribute/insert/ansi
* mshop/order/manager/base/service/attribute/update/ansi
* mshop/order/manager/base/service/attribute/newid/ansi
* mshop/order/manager/base/service/attribute/search/ansi
* mshop/order/manager/base/service/attribute/count/ansi

## service/attribute/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/service/attribute/delete/mysql = 
 DELETE FROM "mshop_order_base_service_attr"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_order_base_service_attr"
 WHERE :cond AND siteid = ?


See also:

* mshop/order/manager/base/service/attribute/delete/ansi

## service/attribute/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/base/service/attribute/insert/ansi = 
 INSERT INTO "mshop_order_base_service_attr" ( :names
 	"attrid", "parentid", "type", "code", "value",
 	"quantity", "price", "name", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/base/service/attribute/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/service/attribute/update/ansi
* mshop/order/manager/base/service/attribute/newid/ansi
* mshop/order/manager/base/service/attribute/delete/ansi
* mshop/order/manager/base/service/attribute/search/ansi
* mshop/order/manager/base/service/attribute/count/ansi

## service/attribute/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/base/service/attribute/insert/mysql = 
 INSERT INTO "mshop_order_base_service_attr" ( :names
 	"attrid", "parentid", "type", "code", "value",
 	"quantity", "price", "name", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_order_base_service_attr" ( :names
 	"attrid", "parentid", "type", "code", "value",
 	"quantity", "price", "name", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/base/service/attribute/insert/ansi

## service/attribute/name

Class name of the used order base service attribute manager implementation

```
mshop/order/manager/base/service/attribute/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default order base service attribute manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Order\Manager\Base\Service\Attribute\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Base\Service\Attribute\Myattribute
```

then you have to set the this configuration option:

```
 mshop/order/manager/base/service/attribute/name = Myattribute
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyAttribute"!


## service/attribute/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/service/attribute/newid/ansi = mshop/order/manager/base/service/attribute/newid
```

* Default: mshop/order/manager/base/service/attribute/newid
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
 SELECT currval('seq_mord_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mord_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/order/manager/base/service/attribute/insert/ansi
* mshop/order/manager/base/service/attribute/update/ansi
* mshop/order/manager/base/service/attribute/delete/ansi
* mshop/order/manager/base/service/attribute/search/ansi
* mshop/order/manager/base/service/attribute/count/ansi

## service/attribute/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/service/attribute/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/base/service/attribute/newid

See also:

* mshop/order/manager/base/service/attribute/newid/ansi

## service/attribute/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/service/attribute/search/ansi = 
 SELECT :columns
 	mordbaseat."id" AS "order.base.service.attribute.id", mordbaseat."siteid" AS "order.base.service.attribute.siteid",
 	mordbaseat."attrid" AS "order.base.service.attribute.attributeid", mordbaseat."parentid" AS "order.base.service.attribute.parentid",
 	mordbaseat."type" AS "order.base.service.attribute.type", mordbaseat."code" AS "order.base.service.attribute.code",
 	mordbaseat."value" AS "order.base.service.attribute.value", mordbaseat."quantity" AS "order.base.service.attribute.quantity",
 	mordbaseat."name" AS "order.base.service.attribute.name", mordbaseat."mtime" AS "order.base.service.attribute.mtime",
 	mordbaseat."ctime" AS "order.base.service.attribute.ctime", mordbaseat."editor" AS "order.base.service.attribute.editor",
 	mordbaseat."price" AS "order.base.service.attribute.price"
 FROM "mshop_order_base_service_attr" mordbaseat
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/base/service/attribute/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the order
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

* mshop/order/manager/base/service/attribute/insert/ansi
* mshop/order/manager/base/service/attribute/update/ansi
* mshop/order/manager/base/service/attribute/newid/ansi
* mshop/order/manager/base/service/attribute/delete/ansi
* mshop/order/manager/base/service/attribute/count/ansi

## service/attribute/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/service/attribute/search/mysql = 
 SELECT :columns
 	mordbaseat."id" AS "order.base.service.attribute.id", mordbaseat."siteid" AS "order.base.service.attribute.siteid",
 	mordbaseat."attrid" AS "order.base.service.attribute.attributeid", mordbaseat."parentid" AS "order.base.service.attribute.parentid",
 	mordbaseat."type" AS "order.base.service.attribute.type", mordbaseat."code" AS "order.base.service.attribute.code",
 	mordbaseat."value" AS "order.base.service.attribute.value", mordbaseat."quantity" AS "order.base.service.attribute.quantity",
 	mordbaseat."name" AS "order.base.service.attribute.name", mordbaseat."mtime" AS "order.base.service.attribute.mtime",
 	mordbaseat."ctime" AS "order.base.service.attribute.ctime", mordbaseat."editor" AS "order.base.service.attribute.editor",
 	mordbaseat."price" AS "order.base.service.attribute.price"
 FROM "mshop_order_base_service_attr" mordbaseat
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordbaseat."id" AS "order.base.service.attribute.id", mordbaseat."siteid" AS "order.base.service.attribute.siteid",
 	mordbaseat."attrid" AS "order.base.service.attribute.attributeid", mordbaseat."parentid" AS "order.base.service.attribute.parentid",
 	mordbaseat."type" AS "order.base.service.attribute.type", mordbaseat."code" AS "order.base.service.attribute.code",
 	mordbaseat."value" AS "order.base.service.attribute.value", mordbaseat."quantity" AS "order.base.service.attribute.quantity",
 	mordbaseat."name" AS "order.base.service.attribute.name", mordbaseat."mtime" AS "order.base.service.attribute.mtime",
 	mordbaseat."ctime" AS "order.base.service.attribute.ctime", mordbaseat."editor" AS "order.base.service.attribute.editor",
 	mordbaseat."price" AS "order.base.service.attribute.price"
 FROM "mshop_order_base_service_attr" mordbaseat
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/base/service/attribute/search/ansi

## service/attribute/submanagers

List of manager names that can be instantiated by the order base service attribute manager

```
mshop/order/manager/base/service/attribute/submanagers = Array
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


## service/attribute/update/ansi

Updates an existing order record in the database

```
mshop/order/manager/base/service/attribute/update/ansi = 
 UPDATE "mshop_order_base_service_attr"
 SET :names
 	"attrid" = ?, "parentid" = ?, "type" = ?, "code" = ?, "value" = ?,
 	"quantity" = ?, "price" = ?, "name" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/order/manager/base/service/attribute/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/service/attribute/insert/ansi
* mshop/order/manager/base/service/attribute/newid/ansi
* mshop/order/manager/base/service/attribute/delete/ansi
* mshop/order/manager/base/service/attribute/search/ansi
* mshop/order/manager/base/service/attribute/count/ansi

## service/attribute/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/base/service/attribute/update/mysql = 
 UPDATE "mshop_order_base_service_attr"
 SET :names
 	"attrid" = ?, "parentid" = ?, "type" = ?, "code" = ?, "value" = ?,
 	"quantity" = ?, "price" = ?, "name" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_order_base_service_attr"
 SET :names
 	"attrid" = ?, "parentid" = ?, "type" = ?, "code" = ?, "value" = ?,
 	"quantity" = ?, "price" = ?, "name" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/order/manager/base/service/attribute/update/ansi

## service/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/service/count/ansi = 
 SELECT COUNT( DISTINCT mordbase."id" ) AS "count"
 FROM "mshop_order_base_service" mordbase
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/base/service/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the order
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

* mshop/order/manager/base/service/insert/ansi
* mshop/order/manager/base/service/update/ansi
* mshop/order/manager/base/service/newid/ansi
* mshop/order/manager/base/service/delete/ansi
* mshop/order/manager/base/service/search/ansi

## service/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/base/service/count/mysql = 
 SELECT COUNT( DISTINCT mordbase."id" ) AS "count"
 FROM "mshop_order_base_service" mordbase
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordbase."id" ) AS "count"
 FROM "mshop_order_base_service" mordbase
 :joins
 WHERE :cond


See also:

* mshop/order/manager/base/service/count/ansi

## service/decorators/excludes

Excludes decorators added by the "common" option from the order base service manager

```
mshop/order/manager/base/service/decorators/excludes = Array
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
around the order base service manager.

```
 mshop/order/manager/base/service/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base service manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/service/decorators/global
* mshop/order/manager/base/service/decorators/local

## service/decorators/global

Adds a list of globally available decorators only to the order base service manager

```
mshop/order/manager/base/service/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order base
service manager.

```
 mshop/order/manager/base/service/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base service manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/service/decorators/excludes
* mshop/order/manager/base/service/decorators/local

## service/decorators/local

Adds a list of local decorators only to the order base service manager

```
mshop/order/manager/base/service/decorators/local = Array
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
("\Aimeos\MShop\Order\Manager\Base\Service\Decorator\*") around the
order base service manager.

```
 mshop/order/manager/base/service/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Service\Decorator\Decorator2" only
to the order base service manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/base/service/decorators/excludes
* mshop/order/manager/base/service/decorators/global

## service/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/service/delete/ansi = 
 DELETE FROM "mshop_order_base_service"
 WHERE :cond AND siteid = ?
```

* Default: mshop/order/manager/base/service/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the order database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/service/insert/ansi
* mshop/order/manager/base/service/update/ansi
* mshop/order/manager/base/service/newid/ansi
* mshop/order/manager/base/service/search/ansi
* mshop/order/manager/base/service/count/ansi

## service/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/base/service/delete/mysql = 
 DELETE FROM "mshop_order_base_service"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_order_base_service"
 WHERE :cond AND siteid = ?


See also:

* mshop/order/manager/base/service/delete/ansi

## service/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/base/service/insert/ansi = 
 INSERT INTO "mshop_order_base_service" ( :names
 	"baseid", "servid", "type", "code", "name", "mediaurl",
 	"currencyid", "price", "costs", "rebate", "tax", "taxrate",
 	"taxflag", "pos", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/base/service/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/service/update/ansi
* mshop/order/manager/base/service/newid/ansi
* mshop/order/manager/base/service/delete/ansi
* mshop/order/manager/base/service/search/ansi
* mshop/order/manager/base/service/count/ansi

## service/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/base/service/insert/mysql = 
 INSERT INTO "mshop_order_base_service" ( :names
 	"baseid", "servid", "type", "code", "name", "mediaurl",
 	"currencyid", "price", "costs", "rebate", "tax", "taxrate",
 	"taxflag", "pos", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_order_base_service" ( :names
 	"baseid", "servid", "type", "code", "name", "mediaurl",
 	"currencyid", "price", "costs", "rebate", "tax", "taxrate",
 	"taxflag", "pos", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/base/service/insert/ansi

## service/name

Class name of the used order base service manager implementation

```
mshop/order/manager/base/service/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default order base service manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Order\Manager\Base\Service\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Base\Service\Myservice
```

then you have to set the this configuration option:

```
 mshop/order/manager/base/service/name = Myservice
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyService"!


## service/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/service/newid/ansi = mshop/order/manager/base/service/newid
```

* Default: mshop/order/manager/base/service/newid
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
 SELECT currval('seq_mord_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mord_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/order/manager/base/service/insert/ansi
* mshop/order/manager/base/service/update/ansi
* mshop/order/manager/base/service/delete/ansi
* mshop/order/manager/base/service/search/ansi
* mshop/order/manager/base/service/count/ansi

## service/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/base/service/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/base/service/newid

See also:

* mshop/order/manager/base/service/newid/ansi

## service/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/service/search/ansi = 
 SELECT :columns
 	mordbase."id" AS "order.base.service.id", mordbase."baseid" AS "order.base.service.baseid",
 	mordbase."siteid" AS "order.base.service.siteid", mordbase."servid" AS "order.base.service.serviceid",
 	mordbase."type" AS "order.base.service.type", mordbase."code" AS "order.base.service.code",
 	mordbase."name" AS "order.base.service.name", mordbase."mediaurl" AS "order.base.service.mediaurl",
 	mordbase."currencyid" AS "order.base.service.currencyid", mordbase."price" AS "order.base.service.price",
 	mordbase."costs" AS "order.base.service.costs", mordbase."rebate" AS "order.base.service.rebate",
 	mordbase."tax" AS "order.base.service.taxvalue", mordbase."taxrate" AS "order.base.service.taxrates",
 	mordbase."taxflag" AS "order.base.service.taxflag", mordbase."pos" AS "order.base.service.position",
 	mordbase."mtime" AS "order.base.service.mtime", mordbase."editor" AS "order.base.service.editor",
 	mordbase."ctime" AS "order.base.service.ctime"
 FROM "mshop_order_base_service" mordbase
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mordbase."id", mordbase."baseid", mordbase."siteid", mordbase."servid", mordbase."type",
 	mordbase."code", mordbase."name", mordbase."mediaurl", mordbase."currencyid", mordbase."price",
 	mordbase."costs", mordbase."rebate", mordbase."tax", mordbase."taxrate", mordbase."taxflag",
 	mordbase."pos", mordbase."mtime", mordbase."editor", mordbase."ctime"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/base/service/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the order
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

* mshop/order/manager/base/service/insert/ansi
* mshop/order/manager/base/service/update/ansi
* mshop/order/manager/base/service/newid/ansi
* mshop/order/manager/base/service/delete/ansi
* mshop/order/manager/base/service/count/ansi

## service/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/base/service/search/mysql = 
 SELECT :columns
 	mordbase."id" AS "order.base.service.id", mordbase."baseid" AS "order.base.service.baseid",
 	mordbase."siteid" AS "order.base.service.siteid", mordbase."servid" AS "order.base.service.serviceid",
 	mordbase."type" AS "order.base.service.type", mordbase."code" AS "order.base.service.code",
 	mordbase."name" AS "order.base.service.name", mordbase."mediaurl" AS "order.base.service.mediaurl",
 	mordbase."currencyid" AS "order.base.service.currencyid", mordbase."price" AS "order.base.service.price",
 	mordbase."costs" AS "order.base.service.costs", mordbase."rebate" AS "order.base.service.rebate",
 	mordbase."tax" AS "order.base.service.taxvalue", mordbase."taxrate" AS "order.base.service.taxrates",
 	mordbase."taxflag" AS "order.base.service.taxflag", mordbase."pos" AS "order.base.service.position",
 	mordbase."mtime" AS "order.base.service.mtime", mordbase."editor" AS "order.base.service.editor",
 	mordbase."ctime" AS "order.base.service.ctime"
 FROM "mshop_order_base_service" mordbase
 :joins
 WHERE :cond
 GROUP BY :group mordbase."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordbase."id" AS "order.base.service.id", mordbase."baseid" AS "order.base.service.baseid",
 	mordbase."siteid" AS "order.base.service.siteid", mordbase."servid" AS "order.base.service.serviceid",
 	mordbase."type" AS "order.base.service.type", mordbase."code" AS "order.base.service.code",
 	mordbase."name" AS "order.base.service.name", mordbase."mediaurl" AS "order.base.service.mediaurl",
 	mordbase."currencyid" AS "order.base.service.currencyid", mordbase."price" AS "order.base.service.price",
 	mordbase."costs" AS "order.base.service.costs", mordbase."rebate" AS "order.base.service.rebate",
 	mordbase."tax" AS "order.base.service.taxvalue", mordbase."taxrate" AS "order.base.service.taxrates",
 	mordbase."taxflag" AS "order.base.service.taxflag", mordbase."pos" AS "order.base.service.position",
 	mordbase."mtime" AS "order.base.service.mtime", mordbase."editor" AS "order.base.service.editor",
 	mordbase."ctime" AS "order.base.service.ctime"
 FROM "mshop_order_base_service" mordbase
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mordbase."id", mordbase."baseid", mordbase."siteid", mordbase."servid", mordbase."type",
 	mordbase."code", mordbase."name", mordbase."mediaurl", mordbase."currencyid", mordbase."price",
 	mordbase."costs", mordbase."rebate", mordbase."tax", mordbase."taxrate", mordbase."taxflag",
 	mordbase."pos", mordbase."mtime", mordbase."editor", mordbase."ctime"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/base/service/search/ansi

## service/submanagers

List of manager names that can be instantiated by the order base service manager

```
mshop/order/manager/base/service/submanagers = Array
(
    [0] => attribute
)
```

* Default: Array
(
    [0] => attribute
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


## service/update/ansi

Updates an existing order record in the database

```
mshop/order/manager/base/service/update/ansi = 
 UPDATE "mshop_order_base_service"
 SET :names
 	"baseid" = ?, "servid" = ?, "type" = ?, "code" = ?,
 	"name" = ?, "mediaurl" = ?, "currencyid" = ?, "price" = ?,
 	"costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "pos" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/order/manager/base/service/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/service/insert/ansi
* mshop/order/manager/base/service/newid/ansi
* mshop/order/manager/base/service/delete/ansi
* mshop/order/manager/base/service/search/ansi
* mshop/order/manager/base/service/count/ansi

## service/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/base/service/update/mysql = 
 UPDATE "mshop_order_base_service"
 SET :names
 	"baseid" = ?, "servid" = ?, "type" = ?, "code" = ?,
 	"name" = ?, "mediaurl" = ?, "currencyid" = ?, "price" = ?,
 	"costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "pos" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_order_base_service"
 SET :names
 	"baseid" = ?, "servid" = ?, "type" = ?, "code" = ?,
 	"name" = ?, "mediaurl" = ?, "currencyid" = ?, "price" = ?,
 	"costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "pos" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/order/manager/base/service/update/ansi

## submanagers

List of manager names that can be instantiated by the order base manager

```
mshop/order/manager/base/submanagers = Array
(
    [0] => address
    [1] => coupon
    [2] => product
    [3] => service
)
```

* Default: Array
(
    [0] => address
    [1] => coupon
    [2] => product
    [3] => service
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

Updates an existing order record in the database

```
mshop/order/manager/base/update/ansi = 
 UPDATE "mshop_order_base"
 SET :names
 	"customerid" = ?, "sitecode" = ?, "langid" = ?, "currencyid" = ?,
 	"price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxflag" = ?,
 	"customerref" = ?, "comment" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/order/manager/base/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/base/insert/ansi
* mshop/order/manager/base/newid/ansi
* mshop/order/manager/base/delete/ansi
* mshop/order/manager/base/search/ansi
* mshop/order/manager/base/count/ansi

## update/mysql

Updates an existing order record in the database

```
mshop/order/manager/base/update/mysql = 
 UPDATE "mshop_order_base"
 SET :names
 	"customerid" = ?, "sitecode" = ?, "langid" = ?, "currencyid" = ?,
 	"price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxflag" = ?,
 	"customerref" = ?, "comment" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_order_base"
 SET :names
 	"customerid" = ?, "sitecode" = ?, "langid" = ?, "currencyid" = ?,
 	"price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxflag" = ?,
 	"customerref" = ?, "comment" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/order/manager/base/update/ansi

# count
## ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/count/ansi = 
 SELECT COUNT( DISTINCT mord."id" ) AS "count"
 FROM "mshop_order" mord
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the order
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

* mshop/order/manager/insert/ansi
* mshop/order/manager/update/ansi
* mshop/order/manager/newid/ansi
* mshop/order/manager/delete/ansi
* mshop/order/manager/search/ansi

## mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/count/mysql = 
 SELECT COUNT( DISTINCT mord."id" ) AS "count"
 FROM "mshop_order" mord
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mord."id" ) AS "count"
 FROM "mshop_order" mord
 :joins
 WHERE :cond


See also:

* mshop/order/manager/count/ansi

# decorators
## excludes

Excludes decorators added by the "common" option from the order manager

```
mshop/order/manager/decorators/excludes = Array
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
around the order manager.

```
 mshop/order/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/decorators/global
* mshop/order/manager/decorators/local

## global

Adds a list of globally available decorators only to the order manager

```
mshop/order/manager/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order manager.

```
 mshop/order/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/decorators/excludes
* mshop/order/manager/decorators/local

## local

Adds a list of local decorators only to the order manager

```
mshop/order/manager/decorators/local = Array
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
("\Aimeos\MShop\Order\Manager\Decorator\*") around the order manager.

```
 mshop/order/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Decorator\Decorator2" only to the order
manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/decorators/excludes
* mshop/order/manager/decorators/global

# delete
## ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/delete/ansi = 
 DELETE FROM "mshop_order"
 WHERE :cond AND siteid = ?
```

* Default: mshop/order/manager/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the order database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/insert/ansi
* mshop/order/manager/update/ansi
* mshop/order/manager/newid/ansi
* mshop/order/manager/search/ansi
* mshop/order/manager/count/ansi

## mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/delete/mysql = 
 DELETE FROM "mshop_order"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_order"
 WHERE :cond AND siteid = ?


See also:

* mshop/order/manager/delete/ansi

# insert
## ansi

Inserts a new order record into the database table

```
mshop/order/manager/insert/ansi = 
 INSERT INTO "mshop_order" ( :names
 	"baseid", "channel", "datepayment", "datedelivery",
 	"statusdelivery", "statuspayment", "relatedid", "mtime",
 	"editor", "siteid", "ctime", "cdate", "cmonth", "cweek", "cwday", "chour"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/update/ansi
* mshop/order/manager/newid/ansi
* mshop/order/manager/delete/ansi
* mshop/order/manager/search/ansi
* mshop/order/manager/count/ansi

## mysql

Inserts a new order record into the database table

```
mshop/order/manager/insert/mysql = 
 INSERT INTO "mshop_order" ( :names
 	"baseid", "channel", "datepayment", "datedelivery",
 	"statusdelivery", "statuspayment", "relatedid", "mtime",
 	"editor", "siteid", "ctime", "cdate", "cmonth", "cweek", "cwday", "chour"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_order" ( :names
 	"baseid", "channel", "datepayment", "datedelivery",
 	"statusdelivery", "statuspayment", "relatedid", "mtime",
 	"editor", "siteid", "ctime", "cdate", "cmonth", "cweek", "cwday", "chour"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/insert/ansi

# name

Class name of the used order manager implementation

```
mshop/order/manager/name = Standard
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
 \Aimeos\MShop\Order\Manager\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Mymanager
```

then you have to set the this configuration option:

```
 mshop/order/manager/name = Mymanager
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
mshop/order/manager/newid/ansi = mshop/order/manager/newid
```

* Default: mshop/order/manager/newid
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
 SELECT currval('seq_mord_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mord_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/order/manager/insert/ansi
* mshop/order/manager/update/ansi
* mshop/order/manager/delete/ansi
* mshop/order/manager/search/ansi
* mshop/order/manager/count/ansi

## mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/newid

See also:

* mshop/order/manager/newid/ansi

# search
## ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/search/ansi = 
 SELECT :columns
 	mord."id" AS "order.id", mord."baseid" AS "order.baseid",
 	mord."siteid" AS "order.siteid", mord."channel" AS "order.channel",
 	mord."datepayment" AS "order.datepayment", mord."datedelivery" AS "order.datedelivery",
 	mord."statuspayment" AS "order.statuspayment", mord."statusdelivery" AS "order.statusdelivery",
 	mord."relatedid" AS "order.relatedid", mord."ctime" AS "order.ctime",
 	mord."mtime" AS "order.mtime", mord."editor" AS "order.editor"
 FROM "mshop_order" mord
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mord."id", mord."baseid", mord."siteid", mord."channel", mord."datepayment", mord."datedelivery",
 	mord."statuspayment", mord."statusdelivery", mord."relatedid", mord."ctime", mord."mtime", mord."editor"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the order
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

* mshop/order/manager/insert/ansi
* mshop/order/manager/update/ansi
* mshop/order/manager/newid/ansi
* mshop/order/manager/delete/ansi
* mshop/order/manager/count/ansi

## mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/search/mysql = 
 SELECT :columns
 	mord."id" AS "order.id", mord."baseid" AS "order.baseid",
 	mord."siteid" AS "order.siteid", mord."channel" AS "order.channel",
 	mord."datepayment" AS "order.datepayment", mord."datedelivery" AS "order.datedelivery",
 	mord."statuspayment" AS "order.statuspayment", mord."statusdelivery" AS "order.statusdelivery",
 	mord."relatedid" AS "order.relatedid", mord."ctime" AS "order.ctime",
 	mord."mtime" AS "order.mtime", mord."editor" AS "order.editor"
 FROM "mshop_order" mord
 :joins
 WHERE :cond
 GROUP BY :group mord."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mord."id" AS "order.id", mord."baseid" AS "order.baseid",
 	mord."siteid" AS "order.siteid", mord."channel" AS "order.channel",
 	mord."datepayment" AS "order.datepayment", mord."datedelivery" AS "order.datedelivery",
 	mord."statuspayment" AS "order.statuspayment", mord."statusdelivery" AS "order.statusdelivery",
 	mord."relatedid" AS "order.relatedid", mord."ctime" AS "order.ctime",
 	mord."mtime" AS "order.mtime", mord."editor" AS "order.editor"
 FROM "mshop_order" mord
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mord."id", mord."baseid", mord."siteid", mord."channel", mord."datepayment", mord."datedelivery",
 	mord."statuspayment", mord."statusdelivery", mord."relatedid", mord."ctime", mord."mtime", mord."editor"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/search/ansi

# sitemode

Mode how items from levels below or above in the site tree are handled

```
mshop/order/manager/sitemode = 3
```

* Default: 3
* Type: int - Constant from Aimeos\MShop\Locale\Manager\Base class
* Since: 2018.01

By default, only items from the current site are fetched from the
storage. If the ai-sites extension is installed, you can create a
tree of sites. Then, this setting allows you to define for the
whole order domain if items from parent sites are inherited,
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

# status
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/status/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_status" mordst
 	:joins
 	WHERE :cond
 	GROUP BY mordst.id, :cols, :val
 	ORDER BY mordst.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/status/aggregate
* Type: string - SQL statement for aggregating order items
* Since: 2014.09

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

* mshop/order/manager/status/insert/ansi
* mshop/order/manager/status/update/ansi
* mshop/order/manager/status/newid/ansi
* mshop/order/manager/status/delete/ansi
* mshop/order/manager/status/search/ansi
* mshop/order/manager/status/count/ansi

## aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/status/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_status" mordst
 	:joins
 	WHERE :cond
 	GROUP BY mordst.id, :cols, :val
 	ORDER BY mordst.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :val AS "val"
 	FROM "mshop_order_status" mordst
 	:joins
 	WHERE :cond
 	GROUP BY mordst.id, :cols, :val
 	ORDER BY mordst.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/status/aggregate/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/status/count/ansi = 
 SELECT COUNT( DISTINCT mordst."id" ) AS "count"
 FROM "mshop_order_status" mordst
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/status/count
* Type: string - SQL statement for counting items
* Since: 2014.03

Counts all records matched by the given criteria from the order
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

* mshop/order/manager/status/insert/ansi
* mshop/order/manager/status/update/ansi
* mshop/order/manager/status/newid/ansi
* mshop/order/manager/status/delete/ansi
* mshop/order/manager/status/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/status/count/mysql = 
 SELECT COUNT( DISTINCT mordst."id" ) AS "count"
 FROM "mshop_order_status" mordst
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordst."id" ) AS "count"
 FROM "mshop_order_status" mordst
 :joins
 WHERE :cond


See also:

* mshop/order/manager/status/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the order status manager

```
mshop/order/manager/status/decorators/excludes = Array
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
around the order status manager.

```
 mshop/order/manager/status/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order status manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/status/decorators/global
* mshop/order/manager/status/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order status manager

```
mshop/order/manager/status/decorators/global = Array
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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order status
manager.

```
 mshop/order/manager/status/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
status manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/status/decorators/excludes
* mshop/order/manager/status/decorators/local

## decorators/local

Adds a list of local decorators only to the order status manager

```
mshop/order/manager/status/decorators/local = Array
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
("\Aimeos\MShop\Order\Manager\Status\Decorator\*") around the order
status manager.

```
 mshop/order/manager/status/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Status\Decorator\Decorator2" only to the
order status manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/status/decorators/excludes
* mshop/order/manager/status/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/status/delete/ansi = 
 DELETE FROM "mshop_order_status"
 WHERE :cond AND siteid = ?
```

* Default: mshop/order/manager/status/delete
* Type: string - SQL statement for deleting items
* Since: 2014.03

Removes the records specified by the given IDs from the order database.
The records must be from the site that is configured via the
context item.

The ":cond" placeholder is replaced by the name of the ID column and
the given ID or list of IDs while the site ID is bound to the question
mark.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/status/insert/ansi
* mshop/order/manager/status/update/ansi
* mshop/order/manager/status/newid/ansi
* mshop/order/manager/status/search/ansi
* mshop/order/manager/status/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/status/delete/mysql = 
 DELETE FROM "mshop_order_status"
 WHERE :cond AND siteid = ?
```

* Default: 
 DELETE FROM "mshop_order_status"
 WHERE :cond AND siteid = ?


See also:

* mshop/order/manager/status/delete/ansi

## insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/status/insert/ansi = 
 INSERT INTO "mshop_order_status" ( :names
 	"parentid", "type", "value", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/status/insert
* Type: string - SQL statement for inserting records
* Since: 2014.03

Items with no ID yet (i.e. the ID is NULL) will be created in
the database and the newly created ID retrieved afterwards
using the "newid" SQL statement.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The number of question marks must
be the same as the number of columns listed in the INSERT
statement. The order of the columns must correspond to the
order in the save() method, so the correct values are
bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/status/update/ansi
* mshop/order/manager/status/newid/ansi
* mshop/order/manager/status/delete/ansi
* mshop/order/manager/status/search/ansi
* mshop/order/manager/status/count/ansi

## insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/status/insert/mysql = 
 INSERT INTO "mshop_order_status" ( :names
 	"parentid", "type", "value", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_order_status" ( :names
 	"parentid", "type", "value", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/status/insert/ansi

## name

Class name of the used order status manager implementation

```
mshop/order/manager/status/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2014.03

Each default order status manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Order\Manager\Status\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Status\Mystatus
```

then you have to set the this configuration option:

```
 mshop/order/manager/status/name = Mystatus
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyStatus"!


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/status/newid/ansi = mshop/order/manager/status/newid
```

* Default: mshop/order/manager/status/newid
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
 SELECT currval('seq_mord_id')
For SQL Server:
 SELECT SCOPE_IDENTITY()
For Oracle:
 SELECT "seq_mord_id".CURRVAL FROM DUAL
```

There's no way to retrive the new ID by a SQL statements that
fits for most database servers as they implement their own
specific way.

See also:

* mshop/order/manager/status/insert/ansi
* mshop/order/manager/status/update/ansi
* mshop/order/manager/status/delete/ansi
* mshop/order/manager/status/search/ansi
* mshop/order/manager/status/count/ansi

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/status/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/status/newid

See also:

* mshop/order/manager/status/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/status/search/ansi = 
 SELECT :columns
 	mordst."id" AS "order.status.id", mordst."siteid" AS "order.status.siteid",
 	mordst."parentid" AS "order.status.parentid", mordst."type" AS "order.status.type",
 	mordst."value" AS "order.status.value", mordst."mtime" AS "order.status.mtime",
 	mordst."ctime" AS "order.status.ctime", mordst."editor" AS "order.status.editor"
 FROM "mshop_order_status" mordst
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/status/search
* Type: string - SQL statement for searching items
* Since: 2014.03

Fetches the records matched by the given criteria from the order
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

* mshop/order/manager/status/insert/ansi
* mshop/order/manager/status/update/ansi
* mshop/order/manager/status/newid/ansi
* mshop/order/manager/status/delete/ansi
* mshop/order/manager/status/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/status/search/mysql = 
 SELECT :columns
 	mordst."id" AS "order.status.id", mordst."siteid" AS "order.status.siteid",
 	mordst."parentid" AS "order.status.parentid", mordst."type" AS "order.status.type",
 	mordst."value" AS "order.status.value", mordst."mtime" AS "order.status.mtime",
 	mordst."ctime" AS "order.status.ctime", mordst."editor" AS "order.status.editor"
 FROM "mshop_order_status" mordst
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordst."id" AS "order.status.id", mordst."siteid" AS "order.status.siteid",
 	mordst."parentid" AS "order.status.parentid", mordst."type" AS "order.status.type",
 	mordst."value" AS "order.status.value", mordst."mtime" AS "order.status.mtime",
 	mordst."ctime" AS "order.status.ctime", mordst."editor" AS "order.status.editor"
 FROM "mshop_order_status" mordst
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/status/search/ansi

## submanagers

List of manager names that can be instantiated by the order status manager

```
mshop/order/manager/status/submanagers = Array
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

Updates an existing order record in the database

```
mshop/order/manager/status/update/ansi = 
 UPDATE "mshop_order_status"
 SET :names
 	"parentid" = ?, "type" = ?, "value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/order/manager/status/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/status/insert/ansi
* mshop/order/manager/status/newid/ansi
* mshop/order/manager/status/delete/ansi
* mshop/order/manager/status/search/ansi
* mshop/order/manager/status/count/ansi

## update/mysql

Updates an existing order record in the database

```
mshop/order/manager/status/update/mysql = 
 UPDATE "mshop_order_status"
 SET :names
 	"parentid" = ?, "type" = ?, "value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_order_status"
 SET :names
 	"parentid" = ?, "type" = ?, "value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/order/manager/status/update/ansi

# submanagers

List of manager names that can be instantiated by the order manager

```
mshop/order/manager/submanagers = Array
(
    [0] => base
    [1] => status
)
```

* Default: Array
(
    [0] => base
    [1] => status
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


# update
## ansi

Updates an existing order record in the database

```
mshop/order/manager/update/ansi = 
 UPDATE "mshop_order"
 SET :names
 	"baseid" = ?, "channel" = ?, "datepayment" = ?, "datedelivery" = ?, "statusdelivery" = ?,
 	"statuspayment" = ?, "relatedid" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: mshop/order/manager/update
* Type: string - SQL statement for updating records
* Since: 2014.03

Items which already have an ID (i.e. the ID is not NULL) will
be updated in the database.

The SQL statement must be a string suitable for being used as
prepared statement. It must include question marks for binding
the values from the order item to the statement before they are
sent to the database server. The order of the columns must
correspond to the order in the save() method, so the
correct values are bound to the columns.

The SQL statement should conform to the ANSI standard to be
compatible with most relational database systems. This also
includes using double quotes for table and column names.

See also:

* mshop/order/manager/insert/ansi
* mshop/order/manager/newid/ansi
* mshop/order/manager/delete/ansi
* mshop/order/manager/search/ansi
* mshop/order/manager/count/ansi

## mysql

Updates an existing order record in the database

```
mshop/order/manager/update/mysql = 
 UPDATE "mshop_order"
 SET :names
 	"baseid" = ?, "channel" = ?, "datepayment" = ?, "datedelivery" = ?, "statusdelivery" = ?,
 	"statuspayment" = ?, "relatedid" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_order"
 SET :names
 	"baseid" = ?, "channel" = ?, "datepayment" = ?, "datedelivery" = ?, "statusdelivery" = ?,
 	"statuspayment" = ?, "relatedid" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" = ? AND "id" = ?


See also:

* mshop/order/manager/update/ansi