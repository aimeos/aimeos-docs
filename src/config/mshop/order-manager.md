
# aggregate
## ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/aggregate/ansi =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order" mord
 	:joins
 	WHERE :cond
 	GROUP BY mord.id, :cols
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
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order" mord
 	:joins
 	WHERE :cond
 	GROUP BY mord.id, :cols
 	ORDER BY mord.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default:
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order" mord
 	:joins
 	WHERE :cond
 	GROUP BY mord.id, :cols
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
mshop/order/manager/address/aggregate/ansi =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_address" mordbaad
 	:joins
 	WHERE :cond
 	GROUP BY mordbaad.id, :cols
 	ORDER BY mordbaad.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/address/aggregate
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

* mshop/order/manager/address/insert/ansi
* mshop/order/manager/address/update/ansi
* mshop/order/manager/address/newid/ansi
* mshop/order/manager/address/delete/ansi
* mshop/order/manager/address/search/ansi
* mshop/order/manager/address/count/ansi

## address/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/address/aggregate/mysql =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_address" mordbaad
 	:joins
 	WHERE :cond
 	GROUP BY mordbaad.id, :cols
 	ORDER BY mordbaad.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default:
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_address" mordbaad
 	:joins
 	WHERE :cond
 	GROUP BY mordbaad.id, :cols
 	ORDER BY mordbaad.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/address/aggregate/ansi

## address/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/address/count/ansi =
 SELECT COUNT( DISTINCT mordbaad."id" ) AS "count"
 FROM "mshop_order_address" mordbaad
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/address/count
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

* mshop/order/manager/address/insert/ansi
* mshop/order/manager/address/update/ansi
* mshop/order/manager/address/newid/ansi
* mshop/order/manager/address/delete/ansi
* mshop/order/manager/address/search/ansi

## address/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/address/count/mysql =
 SELECT COUNT( DISTINCT mordbaad."id" ) AS "count"
 FROM "mshop_order_address" mordbaad
 :joins
 WHERE :cond
```

* Default:
 SELECT COUNT( DISTINCT mordbaad."id" ) AS "count"
 FROM "mshop_order_address" mordbaad
 :joins
 WHERE :cond


See also:

* mshop/order/manager/address/count/ansi

## address/decorators/excludes

Excludes decorators added by the "common" option from the order base address manager

```
mshop/order/manager/address/decorators/excludes = Array
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
 mshop/order/manager/address/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/address/decorators/global
* mshop/order/manager/address/decorators/local

## address/decorators/global

Adds a list of globally available decorators only to the order base address manager

```
mshop/order/manager/address/decorators/global = Array
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
 mshop/order/manager/address/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order base
address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/address/decorators/excludes
* mshop/order/manager/address/decorators/local

## address/decorators/local

Adds a list of local decorators only to the order base address manager

```
mshop/order/manager/address/decorators/local = Array
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
 mshop/order/manager/address/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Address\Decorator\Decorator2" only
to the order base address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/address/decorators/excludes
* mshop/order/manager/address/decorators/global

## address/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/address/delete/ansi =
 DELETE FROM "mshop_order_address"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: mshop/order/manager/address/delete
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

* mshop/order/manager/address/insert/ansi
* mshop/order/manager/address/update/ansi
* mshop/order/manager/address/newid/ansi
* mshop/order/manager/address/search/ansi
* mshop/order/manager/address/count/ansi

## address/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/address/delete/mysql =
 DELETE FROM "mshop_order_address"
 WHERE :cond AND "siteid" LIKE ?
```

* Default:
 DELETE FROM "mshop_order_address"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/order/manager/address/delete/ansi

## address/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/address/insert/ansi =
 INSERT INTO "mshop_order_address" ( :names
 	"baseid", "addrid", "type", "company", "vatid", "salutation",
 	"title", "firstname", "lastname", "address1", "address2",
 	"address3", "postal", "city", "state", "countryid", "langid",
 	"telephone", "email", "telefax", "website", "longitude", "latitude",
 	"pos", "birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
 )
```

* Default: mshop/order/manager/address/insert
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

* mshop/order/manager/address/update/ansi
* mshop/order/manager/address/newid/ansi
* mshop/order/manager/address/delete/ansi
* mshop/order/manager/address/search/ansi
* mshop/order/manager/address/count/ansi

## address/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/address/insert/mysql =
 INSERT INTO "mshop_order_address" ( :names
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
 INSERT INTO "mshop_order_address" ( :names
 	"baseid", "addrid", "type", "company", "vatid", "salutation",
 	"title", "firstname", "lastname", "address1", "address2",
 	"address3", "postal", "city", "state", "countryid", "langid",
 	"telephone", "email", "telefax", "website", "longitude", "latitude",
 	"pos", "birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
 )


See also:

* mshop/order/manager/address/insert/ansi

## address/name

Class name of the used order base address manager implementation

```
mshop/order/manager/address/name = Standard
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
 mshop/order/manager/address/name = Myaddress
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
mshop/order/manager/address/newid/ansi = mshop/order/manager/address/newid
```

* Default: mshop/order/manager/address/newid
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

* mshop/order/manager/address/insert/ansi
* mshop/order/manager/address/update/ansi
* mshop/order/manager/address/delete/ansi
* mshop/order/manager/address/search/ansi
* mshop/order/manager/address/count/ansi

## address/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/address/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/address/newid

See also:

* mshop/order/manager/address/newid/ansi

## address/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/address/search/ansi =
 SELECT :columns
 	mordbaad."id" AS "order.address.id", mordbaad."baseid" AS "order.address.parentid",
 	mordbaad."siteid" AS "order.address.siteid", mordbaad."addrid" AS "order.address.addressid",
 	mordbaad."type" AS "order.address.type", mordbaad."company" AS "order.address.company",
 	mordbaad."vatid" AS "order.address.vatid", mordbaad."salutation" AS "order.address.salutation",
 	mordbaad."title" AS "order.address.title", mordbaad."firstname" AS "order.address.firstname",
 	mordbaad."lastname" AS "order.address.lastname", mordbaad."address1" AS "order.address.address1",
 	mordbaad."address2" AS "order.address.address2", mordbaad."address3" AS "order.address.address3",
 	mordbaad."postal" AS "order.address.postal", mordbaad."city" AS "order.address.city",
 	mordbaad."state" AS "order.address.state", mordbaad."countryid" AS "order.address.countryid",
 	mordbaad."langid" AS "order.address.languageid", mordbaad."telephone" AS "order.address.telephone",
 	mordbaad."email" AS "order.address.email", mordbaad."telefax" AS "order.address.telefax",
 	mordbaad."website" AS "order.address.website", mordbaad."longitude" AS "order.address.longitude",
 	mordbaad."latitude" AS "order.address.latitude", mordbaad."pos" AS "order.address.position",
 	mordbaad."mtime" AS "order.address.mtime", mordbaad."editor" AS "order.address.editor",
 	mordbaad."ctime" AS "order.address.ctime", mordbaad."birthday" AS "order.address.birthday"
 FROM "mshop_order_address" mordbaad
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/address/search
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

* mshop/order/manager/address/insert/ansi
* mshop/order/manager/address/update/ansi
* mshop/order/manager/address/newid/ansi
* mshop/order/manager/address/delete/ansi
* mshop/order/manager/address/count/ansi

## address/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/address/search/mysql =
 SELECT :columns
 	mordbaad."id" AS "order.address.id", mordbaad."baseid" AS "order.address.parentid",
 	mordbaad."siteid" AS "order.address.siteid", mordbaad."addrid" AS "order.address.addressid",
 	mordbaad."type" AS "order.address.type", mordbaad."company" AS "order.address.company",
 	mordbaad."vatid" AS "order.address.vatid", mordbaad."salutation" AS "order.address.salutation",
 	mordbaad."title" AS "order.address.title", mordbaad."firstname" AS "order.address.firstname",
 	mordbaad."lastname" AS "order.address.lastname", mordbaad."address1" AS "order.address.address1",
 	mordbaad."address2" AS "order.address.address2", mordbaad."address3" AS "order.address.address3",
 	mordbaad."postal" AS "order.address.postal", mordbaad."city" AS "order.address.city",
 	mordbaad."state" AS "order.address.state", mordbaad."countryid" AS "order.address.countryid",
 	mordbaad."langid" AS "order.address.languageid", mordbaad."telephone" AS "order.address.telephone",
 	mordbaad."email" AS "order.address.email", mordbaad."telefax" AS "order.address.telefax",
 	mordbaad."website" AS "order.address.website", mordbaad."longitude" AS "order.address.longitude",
 	mordbaad."latitude" AS "order.address.latitude", mordbaad."pos" AS "order.address.position",
 	mordbaad."mtime" AS "order.address.mtime", mordbaad."editor" AS "order.address.editor",
 	mordbaad."ctime" AS "order.address.ctime", mordbaad."birthday" AS "order.address.birthday"
 FROM "mshop_order_address" mordbaad
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default:
 SELECT :columns
 	mordbaad."id" AS "order.address.id", mordbaad."baseid" AS "order.address.parentid",
 	mordbaad."siteid" AS "order.address.siteid", mordbaad."addrid" AS "order.address.addressid",
 	mordbaad."type" AS "order.address.type", mordbaad."company" AS "order.address.company",
 	mordbaad."vatid" AS "order.address.vatid", mordbaad."salutation" AS "order.address.salutation",
 	mordbaad."title" AS "order.address.title", mordbaad."firstname" AS "order.address.firstname",
 	mordbaad."lastname" AS "order.address.lastname", mordbaad."address1" AS "order.address.address1",
 	mordbaad."address2" AS "order.address.address2", mordbaad."address3" AS "order.address.address3",
 	mordbaad."postal" AS "order.address.postal", mordbaad."city" AS "order.address.city",
 	mordbaad."state" AS "order.address.state", mordbaad."countryid" AS "order.address.countryid",
 	mordbaad."langid" AS "order.address.languageid", mordbaad."telephone" AS "order.address.telephone",
 	mordbaad."email" AS "order.address.email", mordbaad."telefax" AS "order.address.telefax",
 	mordbaad."website" AS "order.address.website", mordbaad."longitude" AS "order.address.longitude",
 	mordbaad."latitude" AS "order.address.latitude", mordbaad."pos" AS "order.address.position",
 	mordbaad."mtime" AS "order.address.mtime", mordbaad."editor" AS "order.address.editor",
 	mordbaad."ctime" AS "order.address.ctime", mordbaad."birthday" AS "order.address.birthday"
 FROM "mshop_order_address" mordbaad
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/address/search/ansi

## address/submanagers

List of manager names that can be instantiated by the order base address manager

```
mshop/order/manager/address/submanagers = Array
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
mshop/order/manager/address/update/ansi =
 UPDATE "mshop_order_address"
 SET :names
 	"baseid" = ?, "addrid" = ?, "type" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?, "address2" = ?,
 	"address3" = ?, "postal" = ?, "city" = ?, "state" = ?, "countryid" = ?, "langid" = ?,
 	"telephone" = ?, "email" = ?, "telefax" = ?, "website" = ?, "longitude" = ?, "latitude" = ?,
 	"pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: mshop/order/manager/address/update
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

* mshop/order/manager/address/insert/ansi
* mshop/order/manager/address/newid/ansi
* mshop/order/manager/address/delete/ansi
* mshop/order/manager/address/search/ansi
* mshop/order/manager/address/count/ansi

## address/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/address/update/mysql =
 UPDATE "mshop_order_address"
 SET :names
 	"baseid" = ?, "addrid" = ?, "type" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?, "address2" = ?,
 	"address3" = ?, "postal" = ?, "city" = ?, "state" = ?, "countryid" = ?, "langid" = ?,
 	"telephone" = ?, "email" = ?, "telefax" = ?, "website" = ?, "longitude" = ?, "latitude" = ?,
 	"pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default:
 UPDATE "mshop_order_address"
 SET :names
 	"baseid" = ?, "addrid" = ?, "type" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?, "address2" = ?,
 	"address3" = ?, "postal" = ?, "city" = ?, "state" = ?, "countryid" = ?, "langid" = ?,
 	"telephone" = ?, "email" = ?, "telefax" = ?, "website" = ?, "longitude" = ?, "latitude" = ?,
 	"pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/order/manager/address/update/ansi

## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/aggregate/ansi =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order" mordba
 	:joins
 	WHERE :cond
 	GROUP BY mordba.id, :cols
 	ORDER BY mordba.id DESC
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

## aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/aggregate/mysql =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order" mordba
 	:joins
 	WHERE :cond
 	GROUP BY mordba.id, :cols
 	ORDER BY mordba.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default:
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order" mordba
 	:joins
 	WHERE :cond
 	GROUP BY mordba.id, :cols
 	ORDER BY mordba.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/aggregate/ansi

## aggregateavg/ansi

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/aggregateavg/ansi =
```

* Default:
* Type: string - SQL statement for aggregating the order base items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/aggregate/ansi

## aggregateavg/mysql

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/aggregateavg/mysql =
```

* Default:
* Type: string - SQL statement for aggregating the order base items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/aggregateavg/ansi
* mshop/order/manager/aggregate/mysql

## aggregatesum/ansi

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/aggregatesum/ansi =
```

* Default:
* Type: string - SQL statement for aggregating the order base items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/aggregate/ansi

## aggregatesum/mysql

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/aggregatesum/mysql =
```

* Default:
* Type: string - SQL statement for aggregating the order base items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/aggregatesum/ansi
* mshop/order/manager/aggregate/mysql

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/count/ansi =
 SELECT COUNT( DISTINCT mordba."id" ) AS "count"
 FROM "mshop_order" mordba
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

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/count/mysql =
 SELECT COUNT( DISTINCT mordba."id" ) AS "count"
 FROM "mshop_order" mordba
 :joins
 WHERE :cond
```

* Default:
 SELECT COUNT( DISTINCT mordba."id" ) AS "count"
 FROM "mshop_order" mordba
 :joins
 WHERE :cond


See also:

* mshop/order/manager/count/ansi

## coupon/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/coupon/aggregate/ansi =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_coupon" mordbaco
 	:joins
 	WHERE :cond
 	GROUP BY mordbaco.id, :cols
 	ORDER BY mordbaco.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/coupon/aggregate
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

* mshop/order/manager/coupon/insert/ansi
* mshop/order/manager/coupon/update/ansi
* mshop/order/manager/coupon/newid/ansi
* mshop/order/manager/coupon/delete/ansi
* mshop/order/manager/coupon/search/ansi
* mshop/order/manager/coupon/count/ansi

## coupon/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/coupon/aggregate/mysql =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_coupon" mordbaco
 	:joins
 	WHERE :cond
 	GROUP BY mordbaco.id, :cols
 	ORDER BY mordbaco.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default:
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_coupon" mordbaco
 	:joins
 	WHERE :cond
 	GROUP BY mordbaco.id, :cols
 	ORDER BY mordbaco.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/coupon/aggregate/ansi

## coupon/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/coupon/count/ansi =
 SELECT COUNT( DISTINCT mordbaco."id" ) AS "count"
 FROM "mshop_order_coupon" mordbaco
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/coupon/count
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

* mshop/order/manager/coupon/insert/ansi
* mshop/order/manager/coupon/update/ansi
* mshop/order/manager/coupon/newid/ansi
* mshop/order/manager/coupon/delete/ansi
* mshop/order/manager/coupon/search/ansi

## coupon/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/coupon/count/mysql =
 SELECT COUNT( DISTINCT mordbaco."id" ) AS "count"
 FROM "mshop_order_coupon" mordbaco
 :joins
 WHERE :cond
```

* Default:
 SELECT COUNT( DISTINCT mordbaco."id" ) AS "count"
 FROM "mshop_order_coupon" mordbaco
 :joins
 WHERE :cond


See also:

* mshop/order/manager/coupon/count/ansi

## coupon/decorators/excludes

Excludes decorators added by the "common" option from the order base coupon manager

```
mshop/order/manager/coupon/decorators/excludes = Array
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
 mshop/order/manager/coupon/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base coupon manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/coupon/decorators/global
* mshop/order/manager/coupon/decorators/local

## coupon/decorators/global

Adds a list of globally available decorators only to the order base coupon manager

```
mshop/order/manager/coupon/decorators/global = Array
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
 mshop/order/manager/coupon/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base coupon manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/coupon/decorators/excludes
* mshop/order/manager/coupon/decorators/local

## coupon/decorators/local

Adds a list of local decorators only to the order base coupon manager

```
mshop/order/manager/coupon/decorators/local = Array
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
 mshop/order/manager/coupon/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Coupon\Decorator\Decorator2" only
to the order base coupon manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/coupon/decorators/excludes
* mshop/order/manager/coupon/decorators/global

## coupon/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/coupon/delete/ansi =
 DELETE FROM "mshop_order_coupon"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: mshop/order/manager/coupon/delete
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

* mshop/order/manager/coupon/insert/ansi
* mshop/order/manager/coupon/update/ansi
* mshop/order/manager/coupon/newid/ansi
* mshop/order/manager/coupon/search/ansi
* mshop/order/manager/coupon/count/ansi

## coupon/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/coupon/delete/mysql =
 DELETE FROM "mshop_order_coupon"
 WHERE :cond AND "siteid" LIKE ?
```

* Default:
 DELETE FROM "mshop_order_coupon"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/order/manager/coupon/delete/ansi

## coupon/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/coupon/insert/ansi =
 INSERT INTO "mshop_order_coupon" ( :names
 	"baseid", "ordprodid", "code", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/coupon/insert
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

* mshop/order/manager/coupon/update/ansi
* mshop/order/manager/coupon/newid/ansi
* mshop/order/manager/coupon/delete/ansi
* mshop/order/manager/coupon/search/ansi
* mshop/order/manager/coupon/count/ansi

## coupon/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/coupon/insert/mysql =
 INSERT INTO "mshop_order_coupon" ( :names
 	"baseid", "ordprodid", "code", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )
```

* Default:
 INSERT INTO "mshop_order_coupon" ( :names
 	"baseid", "ordprodid", "code", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/coupon/insert/ansi

## coupon/name

Class name of the used order base coupon manager implementation

```
mshop/order/manager/coupon/name = Standard
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
 mshop/order/manager/coupon/name = Mycoupon
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
mshop/order/manager/coupon/newid/ansi = mshop/order/manager/coupon/newid
```

* Default: mshop/order/manager/coupon/newid
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

* mshop/order/manager/coupon/insert/ansi
* mshop/order/manager/coupon/update/ansi
* mshop/order/manager/coupon/delete/ansi
* mshop/order/manager/coupon/search/ansi
* mshop/order/manager/coupon/count/ansi

## coupon/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/coupon/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/coupon/newid

See also:

* mshop/order/manager/coupon/newid/ansi

## coupon/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/coupon/search/ansi =
 SELECT :columns
 	mordbaco."id" AS "order.coupon.id", mordbaco."baseid" AS "order.coupon.parentid",
 	mordbaco."siteid" AS "order.coupon.siteid", mordbaco."ordprodid" AS "order.coupon.ordprodid",
 	mordbaco."code" AS "order.coupon.code", mordbaco."mtime" AS "order.coupon.mtime",
 	mordbaco."editor" AS "order.coupon.editor", mordbaco."ctime" AS "order.coupon.ctime"
 FROM "mshop_order_coupon" mordbaco
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/coupon/search
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

* mshop/order/manager/coupon/insert/ansi
* mshop/order/manager/coupon/update/ansi
* mshop/order/manager/coupon/newid/ansi
* mshop/order/manager/coupon/delete/ansi
* mshop/order/manager/coupon/count/ansi

## coupon/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/coupon/search/mysql =
 SELECT :columns
 	mordbaco."id" AS "order.coupon.id", mordbaco."baseid" AS "order.coupon.parentid",
 	mordbaco."siteid" AS "order.coupon.siteid", mordbaco."ordprodid" AS "order.coupon.ordprodid",
 	mordbaco."code" AS "order.coupon.code", mordbaco."mtime" AS "order.coupon.mtime",
 	mordbaco."editor" AS "order.coupon.editor", mordbaco."ctime" AS "order.coupon.ctime"
 FROM "mshop_order_coupon" mordbaco
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default:
 SELECT :columns
 	mordbaco."id" AS "order.coupon.id", mordbaco."baseid" AS "order.coupon.parentid",
 	mordbaco."siteid" AS "order.coupon.siteid", mordbaco."ordprodid" AS "order.coupon.ordprodid",
 	mordbaco."code" AS "order.coupon.code", mordbaco."mtime" AS "order.coupon.mtime",
 	mordbaco."editor" AS "order.coupon.editor", mordbaco."ctime" AS "order.coupon.ctime"
 FROM "mshop_order_coupon" mordbaco
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/coupon/search/ansi

## coupon/submanagers

List of manager names that can be instantiated by the order base coupon manager

```
mshop/order/manager/coupon/submanagers = Array
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
mshop/order/manager/coupon/update/ansi =
 UPDATE "mshop_order_coupon"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "code" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: mshop/order/manager/coupon/update
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

* mshop/order/manager/coupon/insert/ansi
* mshop/order/manager/coupon/newid/ansi
* mshop/order/manager/coupon/delete/ansi
* mshop/order/manager/coupon/search/ansi
* mshop/order/manager/coupon/count/ansi

## coupon/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/coupon/update/mysql =
 UPDATE "mshop_order_coupon"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "code" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default:
 UPDATE "mshop_order_coupon"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "code" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/order/manager/coupon/update/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the order base manager

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
around the order base manager.

```
 mshop/order/manager/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/decorators/global
* mshop/order/manager/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order base manager

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
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order base
manager.

```
 mshop/order/manager/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/decorators/excludes
* mshop/order/manager/decorators/local

## decorators/local

Adds a list of local decorators only to the order base manager

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
("\Aimeos\MShop\Order\Manager\Base\Decorator\*") around the order base
manager.

```
 mshop/order/manager/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Decorator\Decorator2" only to the
order base manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/decorators/excludes
* mshop/order/manager/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/delete/ansi =
 DELETE FROM "mshop_order"
 WHERE :cond AND "siteid" LIKE ?
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

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/delete/mysql =
 DELETE FROM "mshop_order"
 WHERE :cond AND "siteid" LIKE ?
```

* Default:
 DELETE FROM "mshop_order"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/order/manager/delete/ansi

## insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/insert/ansi =
 INSERT INTO "mshop_order" ( :names
 	"customerid", "sitecode", "langid", "currencyid",
 	"price", "costs", "rebate", "tax", "taxflag", "customerref",
 	"comment", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
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

## insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/insert/mysql =
 INSERT INTO "mshop_order" ( :names
 	"customerid", "sitecode", "langid", "currencyid",
 	"price", "costs", "rebate", "tax", "taxflag", "customerref",
 	"comment", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default:
 INSERT INTO "mshop_order" ( :names
 	"customerid", "sitecode", "langid", "currencyid",
 	"price", "costs", "rebate", "tax", "taxflag", "customerref",
 	"comment", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/insert/ansi

## name

Class name of the used order base manager implementation

```
mshop/order/manager/name = Standard
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
 mshop/order/manager/name = Mybase
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

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/newid

See also:

* mshop/order/manager/newid/ansi

## product/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/product/aggregate/ansi =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_product" mordbapr
 	:joins
 	WHERE :cond
 	GROUP BY mordbapr.id, :cols
 	ORDER BY mordbapr.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/product/aggregate
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

* mshop/order/manager/product/insert/ansi
* mshop/order/manager/product/update/ansi
* mshop/order/manager/product/newid/ansi
* mshop/order/manager/product/delete/ansi
* mshop/order/manager/product/search/ansi
* mshop/order/manager/product/count/ansi

## product/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/product/aggregate/mysql =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_product" mordbapr
 	:joins
 	WHERE :cond
 	GROUP BY mordbapr.id, :cols
 	ORDER BY mordbapr.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default:
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_product" mordbapr
 	:joins
 	WHERE :cond
 	GROUP BY mordbapr.id, :cols
 	ORDER BY mordbapr.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/product/aggregate/ansi

## product/aggregateavg/ansi

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/product/aggregateavg/ansi =
```

* Default:
* Type: string - SQL statement for aggregating the order product items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/product/aggregate/ansi

## product/aggregateavg/mysql

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/product/aggregateavg/mysql =
```

* Default:
* Type: string - SQL statement for aggregating the order product items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/product/aggregateavg/ansi
* mshop/order/manager/product/aggregate/mysql

## product/aggregatesum/ansi

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/product/aggregatesum/ansi =
```

* Default:
* Type: string - SQL statement for aggregating the order product items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/product/aggregate/ansi

## product/aggregatesum/mysql

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/product/aggregatesum/mysql =
```

* Default:
* Type: string - SQL statement for aggregating the order product items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/product/aggregatesum/ansi
* mshop/order/manager/product/aggregate/mysql

## product/attribute/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/product/attribute/aggregate/ansi =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_product_attr" mordbaprat
 	:joins
 	WHERE :cond
 	GROUP BY mordbaprat.id, :cols
 	ORDER BY mordbaprat.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/product/attribute/aggregate
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

* mshop/order/manager/product/attribute/insert/ansi
* mshop/order/manager/product/attribute/update/ansi
* mshop/order/manager/product/attribute/newid/ansi
* mshop/order/manager/product/attribute/delete/ansi
* mshop/order/manager/product/attribute/search/ansi
* mshop/order/manager/product/attribute/count/ansi

## product/attribute/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/product/attribute/aggregate/mysql =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_product_attr" mordbaprat
 	:joins
 	WHERE :cond
 	GROUP BY mordbaprat.id, :cols
 	ORDER BY mordbaprat.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default:
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_product_attr" mordbaprat
 	:joins
 	WHERE :cond
 	GROUP BY mordbaprat.id, :cols
 	ORDER BY mordbaprat.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/product/attribute/aggregate/ansi

## product/attribute/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/product/attribute/count/ansi =
 SELECT COUNT( DISTINCT mordbaprat."id" ) AS "count"
 FROM "mshop_order_product_attr" mordbaprat
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/product/attribute/count
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

* mshop/order/manager/product/attribute/insert/ansi
* mshop/order/manager/product/attribute/update/ansi
* mshop/order/manager/product/attribute/newid/ansi
* mshop/order/manager/product/attribute/delete/ansi
* mshop/order/manager/product/attribute/search/ansi

## product/attribute/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/product/attribute/count/mysql =
 SELECT COUNT( DISTINCT mordbaprat."id" ) AS "count"
 FROM "mshop_order_product_attr" mordbaprat
 :joins
 WHERE :cond
```

* Default:
 SELECT COUNT( DISTINCT mordbaprat."id" ) AS "count"
 FROM "mshop_order_product_attr" mordbaprat
 :joins
 WHERE :cond


See also:

* mshop/order/manager/product/attribute/count/ansi

## product/attribute/decorators/excludes

Excludes decorators added by the "common" option from the order base product attribute manager

```
mshop/order/manager/product/attribute/decorators/excludes = Array
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
 mshop/order/manager/product/attribute/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base product attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/product/attribute/decorators/global
* mshop/order/manager/product/attribute/decorators/local

## product/attribute/decorators/global

Adds a list of globally available decorators only to the order base product attribute manager

```
mshop/order/manager/product/attribute/decorators/global = Array
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
 mshop/order/manager/product/attribute/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base product attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/product/attribute/decorators/excludes
* mshop/order/manager/product/attribute/decorators/local

## product/attribute/decorators/local

Adds a list of local decorators only to the order base product attribute manager

```
mshop/order/manager/product/attribute/decorators/local = Array
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
 mshop/order/manager/product/attribute/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Product\Attribute\Decorator\Decorator2"
only to the order base product attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/product/attribute/decorators/excludes
* mshop/order/manager/product/attribute/decorators/global

## product/attribute/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/product/attribute/delete/ansi =
 DELETE FROM "mshop_order_product_attr"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: mshop/order/manager/product/attribute/delete
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

* mshop/order/manager/product/attribute/insert/ansi
* mshop/order/manager/product/attribute/update/ansi
* mshop/order/manager/product/attribute/newid/ansi
* mshop/order/manager/product/attribute/search/ansi
* mshop/order/manager/product/attribute/count/ansi

## product/attribute/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/product/attribute/delete/mysql =
 DELETE FROM "mshop_order_product_attr"
 WHERE :cond AND "siteid" LIKE ?
```

* Default:
 DELETE FROM "mshop_order_product_attr"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/order/manager/product/attribute/delete/ansi

## product/attribute/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/product/attribute/insert/ansi =
 INSERT INTO "mshop_order_product_attr" ( :names
 	"attrid", "parentid", "type", "code", "value",
 	"quantity", "price", "name", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/product/attribute/insert
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

* mshop/order/manager/product/attribute/update/ansi
* mshop/order/manager/product/attribute/newid/ansi
* mshop/order/manager/product/attribute/delete/ansi
* mshop/order/manager/product/attribute/search/ansi
* mshop/order/manager/product/attribute/count/ansi

## product/attribute/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/product/attribute/insert/mysql =
 INSERT INTO "mshop_order_product_attr" ( :names
 	"attrid", "parentid", "type", "code", "value",
 	"quantity", "price", "name", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default:
 INSERT INTO "mshop_order_product_attr" ( :names
 	"attrid", "parentid", "type", "code", "value",
 	"quantity", "price", "name", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/product/attribute/insert/ansi

## product/attribute/name

Class name of the used order base product attribute manager implementation

```
mshop/order/manager/product/attribute/name = Standard
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
 mshop/order/manager/product/attribute/name = Myattribute
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
mshop/order/manager/product/attribute/newid/ansi = mshop/order/manager/product/attribute/newid
```

* Default: mshop/order/manager/product/attribute/newid
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

* mshop/order/manager/product/attribute/insert/ansi
* mshop/order/manager/product/attribute/update/ansi
* mshop/order/manager/product/attribute/delete/ansi
* mshop/order/manager/product/attribute/search/ansi
* mshop/order/manager/product/attribute/count/ansi

## product/attribute/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/product/attribute/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/product/attribute/newid

See also:

* mshop/order/manager/product/attribute/newid/ansi

## product/attribute/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/product/attribute/search/ansi =
 SELECT :columns
 	mordbaprat."id" AS "order.product.attribute.id", mordbaprat."siteid" AS "order.product.attribute.siteid",
 	mordbaprat."attrid" AS "order.product.attribute.attributeid", mordbaprat."parentid" AS "order.product.attribute.parentid",
 	mordbaprat."type" AS "order.product.attribute.type", mordbaprat."code" AS "order.product.attribute.code",
 	mordbaprat."value" AS "order.product.attribute.value", mordbaprat."quantity" AS "order.product.attribute.quantity",
 	mordbaprat."name" AS "order.product.attribute.name", mordbaprat."mtime" AS "order.product.attribute.mtime",
 	mordbaprat."editor" AS "order.product.attribute.editor", mordbaprat."ctime" AS "order.product.attribute.ctime",
 	mordbaprat."price" AS "order.product.attribute.price"
 FROM "mshop_order_product_attr" mordbaprat
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/product/attribute/search
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

* mshop/order/manager/product/attribute/insert/ansi
* mshop/order/manager/product/attribute/update/ansi
* mshop/order/manager/product/attribute/newid/ansi
* mshop/order/manager/product/attribute/delete/ansi
* mshop/order/manager/product/attribute/count/ansi

## product/attribute/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/product/attribute/search/mysql =
 SELECT :columns
 	mordbaprat."id" AS "order.product.attribute.id", mordbaprat."siteid" AS "order.product.attribute.siteid",
 	mordbaprat."attrid" AS "order.product.attribute.attributeid", mordbaprat."parentid" AS "order.product.attribute.parentid",
 	mordbaprat."type" AS "order.product.attribute.type", mordbaprat."code" AS "order.product.attribute.code",
 	mordbaprat."value" AS "order.product.attribute.value", mordbaprat."quantity" AS "order.product.attribute.quantity",
 	mordbaprat."name" AS "order.product.attribute.name", mordbaprat."mtime" AS "order.product.attribute.mtime",
 	mordbaprat."editor" AS "order.product.attribute.editor", mordbaprat."ctime" AS "order.product.attribute.ctime",
 	mordbaprat."price" AS "order.product.attribute.price"
 FROM "mshop_order_product_attr" mordbaprat
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default:
 SELECT :columns
 	mordbaprat."id" AS "order.product.attribute.id", mordbaprat."siteid" AS "order.product.attribute.siteid",
 	mordbaprat."attrid" AS "order.product.attribute.attributeid", mordbaprat."parentid" AS "order.product.attribute.parentid",
 	mordbaprat."type" AS "order.product.attribute.type", mordbaprat."code" AS "order.product.attribute.code",
 	mordbaprat."value" AS "order.product.attribute.value", mordbaprat."quantity" AS "order.product.attribute.quantity",
 	mordbaprat."name" AS "order.product.attribute.name", mordbaprat."mtime" AS "order.product.attribute.mtime",
 	mordbaprat."editor" AS "order.product.attribute.editor", mordbaprat."ctime" AS "order.product.attribute.ctime",
 	mordbaprat."price" AS "order.product.attribute.price"
 FROM "mshop_order_product_attr" mordbaprat
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/product/attribute/search/ansi

## product/attribute/submanagers

List of manager names that can be instantiated by the order base product attribute manager

```
mshop/order/manager/product/attribute/submanagers = Array
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
mshop/order/manager/product/attribute/update/ansi =
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

* mshop/order/manager/product/attribute/insert/ansi
* mshop/order/manager/product/attribute/newid/ansi
* mshop/order/manager/product/attribute/delete/ansi
* mshop/order/manager/product/attribute/search/ansi
* mshop/order/manager/product/attribute/count/ansi

## product/attribute/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/product/attribute/update/mysql =
```

* Default:

See also:

* mshop/order/manager/product/attribute/update/ansi

## product/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/product/count/ansi =
 SELECT COUNT( DISTINCT mordbapr."id" ) AS "count"
 FROM "mshop_order_product" mordbapr
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/product/count
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

* mshop/order/manager/product/insert/ansi
* mshop/order/manager/product/update/ansi
* mshop/order/manager/product/newid/ansi
* mshop/order/manager/product/delete/ansi
* mshop/order/manager/product/search/ansi

## product/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/product/count/mysql =
 SELECT COUNT( DISTINCT mordbapr."id" ) AS "count"
 FROM "mshop_order_product" mordbapr
 :joins
 WHERE :cond
```

* Default:
 SELECT COUNT( DISTINCT mordbapr."id" ) AS "count"
 FROM "mshop_order_product" mordbapr
 :joins
 WHERE :cond


See also:

* mshop/order/manager/product/count/ansi

## product/decorators/excludes

Excludes decorators added by the "common" option from the order base product manager

```
mshop/order/manager/product/decorators/excludes = Array
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
 mshop/order/manager/product/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base product manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/product/decorators/global
* mshop/order/manager/product/decorators/local

## product/decorators/global

Adds a list of globally available decorators only to the order base product manager

```
mshop/order/manager/product/decorators/global = Array
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
 mshop/order/manager/product/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base product manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/product/decorators/excludes
* mshop/order/manager/product/decorators/local

## product/decorators/local

Adds a list of local decorators only to the order base product manager

```
mshop/order/manager/product/decorators/local = Array
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
 mshop/order/manager/product/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Product\Decorator\Decorator2" only
to the order base product manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/product/decorators/excludes
* mshop/order/manager/product/decorators/global

## product/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/product/delete/ansi =
 DELETE FROM "mshop_order_product"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: mshop/order/manager/product/delete
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

* mshop/order/manager/product/insert/ansi
* mshop/order/manager/product/update/ansi
* mshop/order/manager/product/newid/ansi
* mshop/order/manager/product/search/ansi
* mshop/order/manager/product/count/ansi

## product/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/product/delete/mysql =
 DELETE FROM "mshop_order_product"
 WHERE :cond AND "siteid" LIKE ?
```

* Default:
 DELETE FROM "mshop_order_product"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/order/manager/product/delete/ansi

## product/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/product/insert/ansi =
 INSERT INTO "mshop_order_product" ( :names
 	"baseid", "ordprodid", "ordaddrid", "type", "parentprodid", "prodid", "prodcode",
 	"vendor", "stocktype", "name", "description", "mediaurl", "timeframe",
 	"quantity", "currencyid", "price", "costs", "rebate", "tax", "taxrate", "taxflag",
 	"flags", "statuspayment", "statusdelivery", "pos", "mtime", "editor", "target",
 	"qtyopen", "notes", "scale", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/product/insert
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

* mshop/order/manager/product/update/ansi
* mshop/order/manager/product/newid/ansi
* mshop/order/manager/product/delete/ansi
* mshop/order/manager/product/search/ansi
* mshop/order/manager/product/count/ansi

## product/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/product/insert/mysql =
 INSERT INTO "mshop_order_product" ( :names
 	"baseid", "ordprodid", "ordaddrid", "type", "parentprodid", "prodid", "prodcode",
 	"vendor", "stocktype", "name", "description", "mediaurl", "timeframe",
 	"quantity", "currencyid", "price", "costs", "rebate", "tax", "taxrate", "taxflag",
 	"flags", "statuspayment", "statusdelivery", "pos", "mtime", "editor", "target",
 	"qtyopen", "notes", "scale", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default:
 INSERT INTO "mshop_order_product" ( :names
 	"baseid", "ordprodid", "ordaddrid", "type", "parentprodid", "prodid", "prodcode",
 	"vendor", "stocktype", "name", "description", "mediaurl", "timeframe",
 	"quantity", "currencyid", "price", "costs", "rebate", "tax", "taxrate", "taxflag",
 	"flags", "statuspayment", "statusdelivery", "pos", "mtime", "editor", "target",
 	"qtyopen", "notes", "scale", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/product/insert/ansi

## product/name

Class name of the used order base product manager implementation

```
mshop/order/manager/product/name = Standard
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
 mshop/order/manager/product/name = Myproduct
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
mshop/order/manager/product/newid/ansi = mshop/order/manager/product/newid
```

* Default: mshop/order/manager/product/newid
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

* mshop/order/manager/product/insert/ansi
* mshop/order/manager/product/update/ansi
* mshop/order/manager/product/delete/ansi
* mshop/order/manager/product/search/ansi
* mshop/order/manager/product/count/ansi

## product/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/product/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/product/newid

See also:

* mshop/order/manager/product/newid/ansi

## product/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/product/search/ansi =
 SELECT :columns
 	mordbapr."id" AS "order.product.id", mordbapr."baseid" AS "order.product.parentid",
 	mordbapr."siteid" AS "order.product.siteid", mordbapr."ordprodid" AS "order.product.orderproductid",
 	mordbapr."prodid" AS "order.product.productid", mordbapr."prodcode" AS "order.product.prodcode",
 	mordbapr."description" AS "order.product.description", mordbapr."stocktype" AS "order.product.stocktype",
 	mordbapr."type" AS "order.product.type", mordbapr."name" AS "order.product.name",
 	mordbapr."mediaurl" AS "order.product.mediaurl", mordbapr."timeframe" AS "order.product.timeframe",
 	mordbapr."quantity" AS "order.product.quantity", mordbapr."currencyid" AS "order.product.currencyid",
 	mordbapr."price" AS "order.product.price", mordbapr."costs" AS "order.product.costs",
 	mordbapr."rebate" AS "order.product.rebate", mordbapr."tax" AS "order.product.taxvalue",
 	mordbapr."taxrate" AS "order.product.taxrates", mordbapr."taxflag" AS "order.product.taxflag",
 	mordbapr."flags" AS "order.product.flags", mordbapr."statusdelivery" AS "order.product.statusdelivery",
 	mordbapr."pos" AS "order.product.position", mordbapr."mtime" AS "order.product.mtime",
 	mordbapr."editor" AS "order.product.editor", mordbapr."ctime" AS "order.product.ctime",
 	mordbapr."target" AS "order.product.target", mordbapr."ordaddrid" AS "order.product.orderaddressid",
 	mordbapr."vendor" AS "order.product.vendor", mordbapr."scale" AS "order.product.scale",
 	mordbapr."qtyopen" AS "order.product.qtyopen", mordbapr."notes" AS "order.product.notes",
 	mordbapr."statuspayment" AS "order.product.statuspayment", mordbapr."parentprodid" AS "order.product.parentproductid"
 FROM "mshop_order_product" mordbapr
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mordbapr."id", mordbapr."baseid", mordbapr."siteid", mordbapr."ordprodid", mordbapr."prodid",
 	mordbapr."prodcode", mordbapr."description", mordbapr."stocktype", mordbapr."type",
 	mordbapr."name", mordbapr."mediaurl", mordbapr."timeframe", mordbapr."quantity",
 	mordbapr."currencyid", mordbapr."price", mordbapr."costs", mordbapr."rebate", mordbapr."tax",
 	mordbapr."taxrate", mordbapr."taxflag", mordbapr."flags", mordbapr."statusdelivery", mordbapr."pos",
 	mordbapr."mtime", mordbapr."editor", mordbapr."ctime", mordbapr."target", mordbapr."ordaddrid",
 	mordbapr."vendor", mordbapr."qtyopen", mordbapr."notes", mordbapr."scale",
 	mordbapr."statuspayment", mordbapr."parentprodid"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/product/search
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

* mshop/order/manager/product/insert/ansi
* mshop/order/manager/product/update/ansi
* mshop/order/manager/product/newid/ansi
* mshop/order/manager/product/delete/ansi
* mshop/order/manager/product/count/ansi

## product/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/product/search/mysql =
 SELECT :columns
 	mordbapr."id" AS "order.product.id", mordbapr."baseid" AS "order.product.parentid",
 	mordbapr."siteid" AS "order.product.siteid", mordbapr."ordprodid" AS "order.product.orderproductid",
 	mordbapr."prodid" AS "order.product.productid", mordbapr."prodcode" AS "order.product.prodcode",
 	mordbapr."description" AS "order.product.description", mordbapr."stocktype" AS "order.product.stocktype",
 	mordbapr."type" AS "order.product.type", mordbapr."name" AS "order.product.name",
 	mordbapr."mediaurl" AS "order.product.mediaurl", mordbapr."timeframe" AS "order.product.timeframe",
 	mordbapr."quantity" AS "order.product.quantity", mordbapr."currencyid" AS "order.product.currencyid",
 	mordbapr."price" AS "order.product.price", mordbapr."costs" AS "order.product.costs",
 	mordbapr."rebate" AS "order.product.rebate", mordbapr."tax" AS "order.product.taxvalue",
 	mordbapr."taxrate" AS "order.product.taxrates", mordbapr."taxflag" AS "order.product.taxflag",
 	mordbapr."flags" AS "order.product.flags", mordbapr."statusdelivery" AS "order.product.statusdelivery",
 	mordbapr."pos" AS "order.product.position", mordbapr."mtime" AS "order.product.mtime",
 	mordbapr."editor" AS "order.product.editor", mordbapr."ctime" AS "order.product.ctime",
 	mordbapr."target" AS "order.product.target", mordbapr."ordaddrid" AS "order.product.orderaddressid",
 	mordbapr."vendor" AS "order.product.vendor", mordbapr."scale" AS "order.product.scale",
 	mordbapr."qtyopen" AS "order.product.qtyopen", mordbapr."notes" AS "order.product.notes",
 	mordbapr."statuspayment" AS "order.product.statuspayment", mordbapr."parentprodid" AS "order.product.parentproductid"
 FROM "mshop_order_product" mordbapr
 :joins
 WHERE :cond
 GROUP BY :group mordbapr."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default:
 SELECT :columns
 	mordbapr."id" AS "order.product.id", mordbapr."baseid" AS "order.product.parentid",
 	mordbapr."siteid" AS "order.product.siteid", mordbapr."ordprodid" AS "order.product.orderproductid",
 	mordbapr."prodid" AS "order.product.productid", mordbapr."prodcode" AS "order.product.prodcode",
 	mordbapr."description" AS "order.product.description", mordbapr."stocktype" AS "order.product.stocktype",
 	mordbapr."type" AS "order.product.type", mordbapr."name" AS "order.product.name",
 	mordbapr."mediaurl" AS "order.product.mediaurl", mordbapr."timeframe" AS "order.product.timeframe",
 	mordbapr."quantity" AS "order.product.quantity", mordbapr."currencyid" AS "order.product.currencyid",
 	mordbapr."price" AS "order.product.price", mordbapr."costs" AS "order.product.costs",
 	mordbapr."rebate" AS "order.product.rebate", mordbapr."tax" AS "order.product.taxvalue",
 	mordbapr."taxrate" AS "order.product.taxrates", mordbapr."taxflag" AS "order.product.taxflag",
 	mordbapr."flags" AS "order.product.flags", mordbapr."statusdelivery" AS "order.product.statusdelivery",
 	mordbapr."pos" AS "order.product.position", mordbapr."mtime" AS "order.product.mtime",
 	mordbapr."editor" AS "order.product.editor", mordbapr."ctime" AS "order.product.ctime",
 	mordbapr."target" AS "order.product.target", mordbapr."ordaddrid" AS "order.product.orderaddressid",
 	mordbapr."vendor" AS "order.product.vendor", mordbapr."scale" AS "order.product.scale",
 	mordbapr."qtyopen" AS "order.product.qtyopen", mordbapr."notes" AS "order.product.notes",
 	mordbapr."statuspayment" AS "order.product.statuspayment", mordbapr."parentprodid" AS "order.product.parentproductid"
 FROM "mshop_order_product" mordbapr
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mordbapr."id", mordbapr."baseid", mordbapr."siteid", mordbapr."ordprodid", mordbapr."prodid",
 	mordbapr."prodcode", mordbapr."description", mordbapr."stocktype", mordbapr."type",
 	mordbapr."name", mordbapr."mediaurl", mordbapr."timeframe", mordbapr."quantity",
 	mordbapr."currencyid", mordbapr."price", mordbapr."costs", mordbapr."rebate", mordbapr."tax",
 	mordbapr."taxrate", mordbapr."taxflag", mordbapr."flags", mordbapr."statusdelivery", mordbapr."pos",
 	mordbapr."mtime", mordbapr."editor", mordbapr."ctime", mordbapr."target", mordbapr."ordaddrid",
 	mordbapr."vendor", mordbapr."qtyopen", mordbapr."notes", mordbapr."scale",
 	mordbapr."statuspayment", mordbapr."parentprodid"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/product/search/ansi

## product/submanagers

List of manager names that can be instantiated by the order base product manager

```
mshop/order/manager/product/submanagers = Array
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
mshop/order/manager/product/update/ansi =
 UPDATE "mshop_order_product"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "ordaddrid" = ?, "type" = ?, "parentprodid" = ?,
 	"prodid" = ?, "prodcode" = ?, "vendor" = ?, "stocktype" = ?,
 	"name" = ?, "description" = ?, "mediaurl" = ?, "timeframe" = ?, "quantity" = ?,
 	"currencyid" = ?, "price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "flags" = ?, "statuspayment" = ?, "statusdelivery" = ?, "pos" = ?,
 	"mtime" = ?, "editor" = ?, "target" = ?, "qtyopen" = ?, "notes" = ?, "scale" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: mshop/order/manager/product/update
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

* mshop/order/manager/product/insert/ansi
* mshop/order/manager/product/newid/ansi
* mshop/order/manager/product/delete/ansi
* mshop/order/manager/product/search/ansi
* mshop/order/manager/product/count/ansi

## product/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/product/update/mysql =
 UPDATE "mshop_order_product"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "ordaddrid" = ?, "type" = ?, "parentprodid" = ?,
 	"prodid" = ?, "prodcode" = ?, "vendor" = ?, "stocktype" = ?,
 	"name" = ?, "description" = ?, "mediaurl" = ?, "timeframe" = ?, "quantity" = ?,
 	"currencyid" = ?, "price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "flags" = ?, "statuspayment" = ?, "statusdelivery" = ?, "pos" = ?,
 	"mtime" = ?, "editor" = ?, "target" = ?, "qtyopen" = ?, "notes" = ?, "scale" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default:
 UPDATE "mshop_order_product"
 SET :names
 	"baseid" = ?, "ordprodid" = ?, "ordaddrid" = ?, "type" = ?, "parentprodid" = ?,
 	"prodid" = ?, "prodcode" = ?, "vendor" = ?, "stocktype" = ?,
 	"name" = ?, "description" = ?, "mediaurl" = ?, "timeframe" = ?, "quantity" = ?,
 	"currencyid" = ?, "price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "flags" = ?, "statuspayment" = ?, "statusdelivery" = ?, "pos" = ?,
 	"mtime" = ?, "editor" = ?, "target" = ?, "qtyopen" = ?, "notes" = ?, "scale" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/order/manager/product/update/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/search/ansi =
 SELECT :columns
 	mordba."id" AS "order.id", mordba."siteid" AS "order.siteid",
 	mordba."sitecode" AS "order.sitecode", mordba."customerid" AS "order.customerid",
 	mordba."langid" AS "order.languageid", mordba."currencyid" AS "order.currencyid",
 	mordba."price" AS "order.price", mordba."costs" AS "order.costs",
 	mordba."rebate" AS "order.rebate", mordba."tax" AS "order.taxvalue",
 	mordba."taxflag" AS "order.taxflag", mordba."customerref" AS "order.customerref",
 	mordba."comment" AS "order.comment", mordba."mtime" AS "order.mtime",
 	mordba."ctime" AS "order.ctime", mordba."editor" AS "order.editor"
 FROM "mshop_order" mordba
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

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/search/mysql =
 SELECT :columns
 	mordba."id" AS "order.id", mordba."siteid" AS "order.siteid",
 	mordba."sitecode" AS "order.sitecode", mordba."customerid" AS "order.customerid",
 	mordba."langid" AS "order.languageid", mordba."currencyid" AS "order.currencyid",
 	mordba."price" AS "order.price", mordba."costs" AS "order.costs",
 	mordba."rebate" AS "order.rebate", mordba."tax" AS "order.taxvalue",
 	mordba."taxflag" AS "order.taxflag", mordba."customerref" AS "order.customerref",
 	mordba."comment" AS "order.comment", mordba."mtime" AS "order.mtime",
 	mordba."ctime" AS "order.ctime", mordba."editor" AS "order.editor"
 FROM "mshop_order" mordba
 :joins
 WHERE :cond
 GROUP BY :group mordba."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default:
 SELECT :columns
 	mordba."id" AS "order.id", mordba."siteid" AS "order.siteid",
 	mordba."sitecode" AS "order.sitecode", mordba."customerid" AS "order.customerid",
 	mordba."langid" AS "order.languageid", mordba."currencyid" AS "order.currencyid",
 	mordba."price" AS "order.price", mordba."costs" AS "order.costs",
 	mordba."rebate" AS "order.rebate", mordba."tax" AS "order.taxvalue",
 	mordba."taxflag" AS "order.taxflag", mordba."customerref" AS "order.customerref",
 	mordba."comment" AS "order.comment", mordba."mtime" AS "order.mtime",
 	mordba."ctime" AS "order.ctime", mordba."editor" AS "order.editor"
 FROM "mshop_order" mordba
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

* mshop/order/manager/search/ansi

## service/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/service/aggregate/ansi =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service" mordbase
 	:joins
 	WHERE :cond
 	GROUP BY mordbase.id, :cols
 	ORDER BY mordbase.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/service/aggregate
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

* mshop/order/manager/service/insert/ansi
* mshop/order/manager/service/update/ansi
* mshop/order/manager/service/newid/ansi
* mshop/order/manager/service/delete/ansi
* mshop/order/manager/service/search/ansi
* mshop/order/manager/service/count/ansi

## service/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/service/aggregate/mysql =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service" mordbase
 	:joins
 	WHERE :cond
 	GROUP BY mordbase.id, :cols
 	ORDER BY mordbase.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default:
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service" mordbase
 	:joins
 	WHERE :cond
 	GROUP BY mordbase.id, :cols
 	ORDER BY mordbase.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/service/aggregate/ansi

## service/aggregateavg/ansi

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/service/aggregateavg/ansi =
```

* Default:
* Type: string - SQL statement for aggregating the order service items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/service/aggregate/ansi

## service/aggregateavg/mysql

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/service/aggregateavg/mysql =
```

* Default:
* Type: string - SQL statement for aggregating the order service items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/service/aggregateavg/ansi
* mshop/order/manager/service/aggregate/mysql

## service/aggregatesum/ansi

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/service/aggregatesum/ansi =
```

* Default:
* Type: string - SQL statement for aggregating the order service items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/service/aggregate/ansi

## service/aggregatesum/mysql

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/service/aggregatesum/mysql =
```

* Default:
* Type: string - SQL statement for aggregating the order service items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/service/aggregatesum/ansi
* mshop/order/manager/service/aggregate/mysql

## service/attribute/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/service/attribute/aggregate/ansi =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service_attr" mordbaseat
 	:joins
 	WHERE :cond
 	GROUP BY mordbaseat.id, :cols
 	ORDER BY mordbaseat.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Default: mshop/order/manager/service/attribute/aggregate
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

* mshop/order/manager/service/attribute/insert/ansi
* mshop/order/manager/service/attribute/update/ansi
* mshop/order/manager/service/attribute/newid/ansi
* mshop/order/manager/service/attribute/delete/ansi
* mshop/order/manager/service/attribute/search/ansi
* mshop/order/manager/service/attribute/count/ansi

## service/attribute/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/service/attribute/aggregate/mysql =
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service_attr" mordbaseat
 	:joins
 	WHERE :cond
 	GROUP BY mordbaseat.id, :cols
 	ORDER BY mordbaseat.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default:
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service_attr" mordbaseat
 	:joins
 	WHERE :cond
 	GROUP BY mordbaseat.id, :cols
 	ORDER BY mordbaseat.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/service/attribute/aggregate/ansi

## service/attribute/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/service/attribute/count/ansi =
 SELECT COUNT( DISTINCT mordbaseat."id" ) AS "count"
 FROM "mshop_order_service_attr" mordbaseat
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/service/attribute/count
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

* mshop/order/manager/service/attribute/insert/ansi
* mshop/order/manager/service/attribute/update/ansi
* mshop/order/manager/service/attribute/newid/ansi
* mshop/order/manager/service/attribute/delete/ansi
* mshop/order/manager/service/attribute/search/ansi

## service/attribute/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/service/attribute/count/mysql =
 SELECT COUNT( DISTINCT mordbaseat."id" ) AS "count"
 FROM "mshop_order_service_attr" mordbaseat
 :joins
 WHERE :cond
```

* Default:
 SELECT COUNT( DISTINCT mordbaseat."id" ) AS "count"
 FROM "mshop_order_service_attr" mordbaseat
 :joins
 WHERE :cond


See also:

* mshop/order/manager/service/attribute/count/ansi

## service/attribute/decorators/excludes

Excludes decorators added by the "common" option from the order base service attribute manager

```
mshop/order/manager/service/attribute/decorators/excludes = Array
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
 mshop/order/manager/service/attribute/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base service attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/attribute/decorators/global
* mshop/order/manager/service/attribute/decorators/local

## service/attribute/decorators/global

Adds a list of globally available decorators only to the order base service attribute manager

```
mshop/order/manager/service/attribute/decorators/global = Array
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
 mshop/order/manager/service/attribute/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base service attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/attribute/decorators/excludes
* mshop/order/manager/service/attribute/decorators/local

## service/attribute/decorators/local

Adds a list of local decorators only to the order base service attribute manager

```
mshop/order/manager/service/attribute/decorators/local = Array
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
 mshop/order/manager/service/attribute/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Service\Attribute\Decorator\Decorator2"
only to the order base service attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/attribute/decorators/excludes
* mshop/order/manager/service/attribute/decorators/global

## service/attribute/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/service/attribute/delete/ansi =
 DELETE FROM "mshop_order_service_attr"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: mshop/order/manager/service/attribute/delete
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

* mshop/order/manager/service/attribute/insert/ansi
* mshop/order/manager/service/attribute/update/ansi
* mshop/order/manager/service/attribute/newid/ansi
* mshop/order/manager/service/attribute/search/ansi
* mshop/order/manager/service/attribute/count/ansi

## service/attribute/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/service/attribute/delete/mysql =
 DELETE FROM "mshop_order_service_attr"
 WHERE :cond AND "siteid" LIKE ?
```

* Default:
 DELETE FROM "mshop_order_service_attr"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/order/manager/service/attribute/delete/ansi

## service/attribute/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/service/attribute/insert/ansi =
 INSERT INTO "mshop_order_service_attr" ( :names
 	"attrid", "parentid", "type", "code", "value",
 	"quantity", "price", "name", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/service/attribute/insert
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

* mshop/order/manager/service/attribute/update/ansi
* mshop/order/manager/service/attribute/newid/ansi
* mshop/order/manager/service/attribute/delete/ansi
* mshop/order/manager/service/attribute/search/ansi
* mshop/order/manager/service/attribute/count/ansi

## service/attribute/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/service/attribute/insert/mysql =
 INSERT INTO "mshop_order_service_attr" ( :names
 	"attrid", "parentid", "type", "code", "value",
 	"quantity", "price", "name", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default:
 INSERT INTO "mshop_order_service_attr" ( :names
 	"attrid", "parentid", "type", "code", "value",
 	"quantity", "price", "name", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/service/attribute/insert/ansi

## service/attribute/name

Class name of the used order base service attribute manager implementation

```
mshop/order/manager/service/attribute/name = Standard
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
 mshop/order/manager/service/attribute/name = Myattribute
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
mshop/order/manager/service/attribute/newid/ansi = mshop/order/manager/service/attribute/newid
```

* Default: mshop/order/manager/service/attribute/newid
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

* mshop/order/manager/service/attribute/insert/ansi
* mshop/order/manager/service/attribute/update/ansi
* mshop/order/manager/service/attribute/delete/ansi
* mshop/order/manager/service/attribute/search/ansi
* mshop/order/manager/service/attribute/count/ansi

## service/attribute/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/service/attribute/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/service/attribute/newid

See also:

* mshop/order/manager/service/attribute/newid/ansi

## service/attribute/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/attribute/search/ansi =
 SELECT :columns
 	mordbaseat."id" AS "order.service.attribute.id", mordbaseat."siteid" AS "order.service.attribute.siteid",
 	mordbaseat."attrid" AS "order.service.attribute.attributeid", mordbaseat."parentid" AS "order.service.attribute.parentid",
 	mordbaseat."type" AS "order.service.attribute.type", mordbaseat."code" AS "order.service.attribute.code",
 	mordbaseat."value" AS "order.service.attribute.value", mordbaseat."quantity" AS "order.service.attribute.quantity",
 	mordbaseat."name" AS "order.service.attribute.name", mordbaseat."mtime" AS "order.service.attribute.mtime",
 	mordbaseat."ctime" AS "order.service.attribute.ctime", mordbaseat."editor" AS "order.service.attribute.editor",
 	mordbaseat."price" AS "order.service.attribute.price"
 FROM "mshop_order_service_attr" mordbaseat
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/service/attribute/search
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

* mshop/order/manager/service/attribute/insert/ansi
* mshop/order/manager/service/attribute/update/ansi
* mshop/order/manager/service/attribute/newid/ansi
* mshop/order/manager/service/attribute/delete/ansi
* mshop/order/manager/service/attribute/count/ansi

## service/attribute/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/attribute/search/mysql =
 SELECT :columns
 	mordbaseat."id" AS "order.service.attribute.id", mordbaseat."siteid" AS "order.service.attribute.siteid",
 	mordbaseat."attrid" AS "order.service.attribute.attributeid", mordbaseat."parentid" AS "order.service.attribute.parentid",
 	mordbaseat."type" AS "order.service.attribute.type", mordbaseat."code" AS "order.service.attribute.code",
 	mordbaseat."value" AS "order.service.attribute.value", mordbaseat."quantity" AS "order.service.attribute.quantity",
 	mordbaseat."name" AS "order.service.attribute.name", mordbaseat."mtime" AS "order.service.attribute.mtime",
 	mordbaseat."ctime" AS "order.service.attribute.ctime", mordbaseat."editor" AS "order.service.attribute.editor",
 	mordbaseat."price" AS "order.service.attribute.price"
 FROM "mshop_order_service_attr" mordbaseat
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default:
 SELECT :columns
 	mordbaseat."id" AS "order.service.attribute.id", mordbaseat."siteid" AS "order.service.attribute.siteid",
 	mordbaseat."attrid" AS "order.service.attribute.attributeid", mordbaseat."parentid" AS "order.service.attribute.parentid",
 	mordbaseat."type" AS "order.service.attribute.type", mordbaseat."code" AS "order.service.attribute.code",
 	mordbaseat."value" AS "order.service.attribute.value", mordbaseat."quantity" AS "order.service.attribute.quantity",
 	mordbaseat."name" AS "order.service.attribute.name", mordbaseat."mtime" AS "order.service.attribute.mtime",
 	mordbaseat."ctime" AS "order.service.attribute.ctime", mordbaseat."editor" AS "order.service.attribute.editor",
 	mordbaseat."price" AS "order.service.attribute.price"
 FROM "mshop_order_service_attr" mordbaseat
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/service/attribute/search/ansi

## service/attribute/submanagers

List of manager names that can be instantiated by the order base service attribute manager

```
mshop/order/manager/service/attribute/submanagers = Array
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
mshop/order/manager/service/attribute/update/ansi =
 UPDATE "mshop_order_service_attr"
 SET :names
 	"attrid" = ?, "parentid" = ?, "type" = ?, "code" = ?, "value" = ?,
 	"quantity" = ?, "price" = ?, "name" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: mshop/order/manager/service/attribute/update
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

* mshop/order/manager/service/attribute/insert/ansi
* mshop/order/manager/service/attribute/newid/ansi
* mshop/order/manager/service/attribute/delete/ansi
* mshop/order/manager/service/attribute/search/ansi
* mshop/order/manager/service/attribute/count/ansi

## service/attribute/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/service/attribute/update/mysql =
 UPDATE "mshop_order_service_attr"
 SET :names
 	"attrid" = ?, "parentid" = ?, "type" = ?, "code" = ?, "value" = ?,
 	"quantity" = ?, "price" = ?, "name" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default:
 UPDATE "mshop_order_service_attr"
 SET :names
 	"attrid" = ?, "parentid" = ?, "type" = ?, "code" = ?, "value" = ?,
 	"quantity" = ?, "price" = ?, "name" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/order/manager/service/attribute/update/ansi

## service/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/service/count/ansi =
 SELECT COUNT( DISTINCT mordbase."id" ) AS "count"
 FROM "mshop_order_service" mordbase
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/service/count
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

* mshop/order/manager/service/insert/ansi
* mshop/order/manager/service/update/ansi
* mshop/order/manager/service/newid/ansi
* mshop/order/manager/service/delete/ansi
* mshop/order/manager/service/search/ansi

## service/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/service/count/mysql =
 SELECT COUNT( DISTINCT mordbase."id" ) AS "count"
 FROM "mshop_order_service" mordbase
 :joins
 WHERE :cond
```

* Default:
 SELECT COUNT( DISTINCT mordbase."id" ) AS "count"
 FROM "mshop_order_service" mordbase
 :joins
 WHERE :cond


See also:

* mshop/order/manager/service/count/ansi

## service/decorators/excludes

Excludes decorators added by the "common" option from the order base service manager

```
mshop/order/manager/service/decorators/excludes = Array
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
 mshop/order/manager/service/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base service manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/decorators/global
* mshop/order/manager/service/decorators/local

## service/decorators/global

Adds a list of globally available decorators only to the order base service manager

```
mshop/order/manager/service/decorators/global = Array
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
 mshop/order/manager/service/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base service manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/decorators/excludes
* mshop/order/manager/service/decorators/local

## service/decorators/local

Adds a list of local decorators only to the order base service manager

```
mshop/order/manager/service/decorators/local = Array
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
 mshop/order/manager/service/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Base\Service\Decorator\Decorator2" only
to the order base service manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/decorators/excludes
* mshop/order/manager/service/decorators/global

## service/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/service/delete/ansi =
 DELETE FROM "mshop_order_service"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: mshop/order/manager/service/delete
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

* mshop/order/manager/service/insert/ansi
* mshop/order/manager/service/update/ansi
* mshop/order/manager/service/newid/ansi
* mshop/order/manager/service/search/ansi
* mshop/order/manager/service/count/ansi

## service/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/service/delete/mysql =
 DELETE FROM "mshop_order_service"
 WHERE :cond AND "siteid" LIKE ?
```

* Default:
 DELETE FROM "mshop_order_service"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/order/manager/service/delete/ansi

## service/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/service/insert/ansi =
 INSERT INTO "mshop_order_service" ( :names
 	"baseid", "servid", "type", "code", "name", "mediaurl",
 	"currencyid", "price", "costs", "rebate", "tax", "taxrate",
 	"taxflag", "pos", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: mshop/order/manager/service/insert
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

* mshop/order/manager/service/update/ansi
* mshop/order/manager/service/newid/ansi
* mshop/order/manager/service/delete/ansi
* mshop/order/manager/service/search/ansi
* mshop/order/manager/service/count/ansi

## service/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/service/insert/mysql =
 INSERT INTO "mshop_order_service" ( :names
 	"baseid", "servid", "type", "code", "name", "mediaurl",
 	"currencyid", "price", "costs", "rebate", "tax", "taxrate",
 	"taxflag", "pos", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default:
 INSERT INTO "mshop_order_service" ( :names
 	"baseid", "servid", "type", "code", "name", "mediaurl",
 	"currencyid", "price", "costs", "rebate", "tax", "taxrate",
 	"taxflag", "pos", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/service/insert/ansi

## service/name

Class name of the used order base service manager implementation

```
mshop/order/manager/service/name = Standard
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
 mshop/order/manager/service/name = Myservice
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
mshop/order/manager/service/newid/ansi = mshop/order/manager/service/newid
```

* Default: mshop/order/manager/service/newid
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

* mshop/order/manager/service/insert/ansi
* mshop/order/manager/service/update/ansi
* mshop/order/manager/service/delete/ansi
* mshop/order/manager/service/search/ansi
* mshop/order/manager/service/count/ansi

## service/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/service/newid/mysql = SELECT LAST_INSERT_ID()
```

* Default: mshop/order/manager/service/newid

See also:

* mshop/order/manager/service/newid/ansi

## service/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/search/ansi =
 SELECT :columns
 	mordbase."id" AS "order.service.id", mordbase."baseid" AS "order.service.parentid",
 	mordbase."siteid" AS "order.service.siteid", mordbase."servid" AS "order.service.serviceid",
 	mordbase."type" AS "order.service.type", mordbase."code" AS "order.service.code",
 	mordbase."name" AS "order.service.name", mordbase."mediaurl" AS "order.service.mediaurl",
 	mordbase."currencyid" AS "order.service.currencyid", mordbase."price" AS "order.service.price",
 	mordbase."costs" AS "order.service.costs", mordbase."rebate" AS "order.service.rebate",
 	mordbase."tax" AS "order.service.taxvalue", mordbase."taxrate" AS "order.service.taxrates",
 	mordbase."taxflag" AS "order.service.taxflag", mordbase."pos" AS "order.service.position",
 	mordbase."mtime" AS "order.service.mtime", mordbase."editor" AS "order.service.editor",
 	mordbase."ctime" AS "order.service.ctime"
 FROM "mshop_order_service" mordbase
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

* Default: mshop/order/manager/service/search
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

* mshop/order/manager/service/insert/ansi
* mshop/order/manager/service/update/ansi
* mshop/order/manager/service/newid/ansi
* mshop/order/manager/service/delete/ansi
* mshop/order/manager/service/count/ansi

## service/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/search/mysql =
 SELECT :columns
 	mordbase."id" AS "order.service.id", mordbase."baseid" AS "order.service.parentid",
 	mordbase."siteid" AS "order.service.siteid", mordbase."servid" AS "order.service.serviceid",
 	mordbase."type" AS "order.service.type", mordbase."code" AS "order.service.code",
 	mordbase."name" AS "order.service.name", mordbase."mediaurl" AS "order.service.mediaurl",
 	mordbase."currencyid" AS "order.service.currencyid", mordbase."price" AS "order.service.price",
 	mordbase."costs" AS "order.service.costs", mordbase."rebate" AS "order.service.rebate",
 	mordbase."tax" AS "order.service.taxvalue", mordbase."taxrate" AS "order.service.taxrates",
 	mordbase."taxflag" AS "order.service.taxflag", mordbase."pos" AS "order.service.position",
 	mordbase."mtime" AS "order.service.mtime", mordbase."editor" AS "order.service.editor",
 	mordbase."ctime" AS "order.service.ctime"
 FROM "mshop_order_service" mordbase
 :joins
 WHERE :cond
 GROUP BY :group mordbase."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default:
 SELECT :columns
 	mordbase."id" AS "order.service.id", mordbase."baseid" AS "order.service.parentid",
 	mordbase."siteid" AS "order.service.siteid", mordbase."servid" AS "order.service.serviceid",
 	mordbase."type" AS "order.service.type", mordbase."code" AS "order.service.code",
 	mordbase."name" AS "order.service.name", mordbase."mediaurl" AS "order.service.mediaurl",
 	mordbase."currencyid" AS "order.service.currencyid", mordbase."price" AS "order.service.price",
 	mordbase."costs" AS "order.service.costs", mordbase."rebate" AS "order.service.rebate",
 	mordbase."tax" AS "order.service.taxvalue", mordbase."taxrate" AS "order.service.taxrates",
 	mordbase."taxflag" AS "order.service.taxflag", mordbase."pos" AS "order.service.position",
 	mordbase."mtime" AS "order.service.mtime", mordbase."editor" AS "order.service.editor",
 	mordbase."ctime" AS "order.service.ctime"
 FROM "mshop_order_service" mordbase
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

* mshop/order/manager/service/search/ansi

## service/submanagers

List of manager names that can be instantiated by the order base service manager

```
mshop/order/manager/service/submanagers = Array
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
mshop/order/manager/service/update/ansi =
 UPDATE "mshop_order_service"
 SET :names
 	"baseid" = ?, "servid" = ?, "type" = ?, "code" = ?,
 	"name" = ?, "mediaurl" = ?, "currencyid" = ?, "price" = ?,
 	"costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "pos" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: mshop/order/manager/service/update
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

* mshop/order/manager/service/insert/ansi
* mshop/order/manager/service/newid/ansi
* mshop/order/manager/service/delete/ansi
* mshop/order/manager/service/search/ansi
* mshop/order/manager/service/count/ansi

## service/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/service/update/mysql =
 UPDATE "mshop_order_service"
 SET :names
 	"baseid" = ?, "servid" = ?, "type" = ?, "code" = ?,
 	"name" = ?, "mediaurl" = ?, "currencyid" = ?, "price" = ?,
 	"costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "pos" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default:
 UPDATE "mshop_order_service"
 SET :names
 	"baseid" = ?, "servid" = ?, "type" = ?, "code" = ?,
 	"name" = ?, "mediaurl" = ?, "currencyid" = ?, "price" = ?,
 	"costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "pos" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/order/manager/service/update/ansi

## submanagers

List of manager names that can be instantiated by the order base manager

```
mshop/order/manager/submanagers = Array
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
mshop/order/manager/update/ansi =
 UPDATE "mshop_order"
 SET :names
 	"customerid" = ?, "sitecode" = ?, "langid" = ?, "currencyid" = ?,
 	"price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxflag" = ?,
 	"customerref" = ?, "comment" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
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

## update/mysql

Updates an existing order record in the database

```
mshop/order/manager/update/mysql =
 UPDATE "mshop_order"
 SET :names
 	"customerid" = ?, "sitecode" = ?, "langid" = ?, "currencyid" = ?,
 	"price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxflag" = ?,
 	"customerref" = ?, "comment" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default:
 UPDATE "mshop_order"
 SET :names
 	"customerid" = ?, "sitecode" = ?, "langid" = ?, "currencyid" = ?,
 	"price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxflag" = ?,
 	"customerref" = ?, "comment" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/order/manager/update/ansi

# basket
## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/basket/count/ansi =
 SELECT COUNT( DISTINCT mordba."id" ) AS "count"
 FROM "mshop_order_basket" mordba
 :joins
 WHERE :cond
```

* Default: mshop/order/manager/basket/count
* Type: string - SQL statement for counting items
* Since: 2022.10

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

* mshop/order/manager/basket/insert/ansi
* mshop/order/manager/basket/update/ansi
* mshop/order/manager/basket/newid/ansi
* mshop/order/manager/basket/delete/ansi
* mshop/order/manager/basket/search/ansi

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/basket/count/mysql =
 SELECT COUNT( DISTINCT mordba."id" ) AS "count"
 FROM "mshop_order_basket" mordba
 :joins
 WHERE :cond
```

* Default:
 SELECT COUNT( DISTINCT mordba."id" ) AS "count"
 FROM "mshop_order_basket" mordba
 :joins
 WHERE :cond


See also:

* mshop/order/manager/basket/count/ansi

## decorators/excludes

Excludes decorators added by the "common" option from the order basket manager

```
mshop/order/manager/basket/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2022.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the order basket manager.

```
 mshop/order/manager/basket/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order basket manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/basket/decorators/global
* mshop/order/manager/basket/decorators/local

## decorators/global

Adds a list of globally available decorators only to the order basket manager

```
mshop/order/manager/basket/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2022.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order basket
manager.

```
 mshop/order/manager/basket/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
basket manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/basket/decorators/excludes
* mshop/order/manager/basket/decorators/local

## decorators/local

Adds a list of local decorators only to the order basket manager

```
mshop/order/manager/basket/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2022.10

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Order\Manager\Basket\Decorator\*") around the order
basket manager.

```
 mshop/order/manager/basket/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Basket\Decorator\Decorator2" only to the
order basket manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/basket/decorators/excludes
* mshop/order/manager/basket/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/basket/delete/ansi =
 DELETE FROM "mshop_order_basket"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: mshop/order/manager/basket/delete
* Type: string - SQL statement for deleting items
* Since: 2022.10

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

* mshop/order/manager/basket/insert/ansi
* mshop/order/manager/basket/update/ansi
* mshop/order/manager/basket/newid/ansi
* mshop/order/manager/basket/search/ansi
* mshop/order/manager/basket/count/ansi

## delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/basket/delete/mysql =
 DELETE FROM "mshop_order_basket"
 WHERE :cond AND "siteid" LIKE ?
```

* Default:
 DELETE FROM "mshop_order_basket"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/order/manager/basket/delete/ansi

## insert/ansi

```
mshop/order/manager/basket/insert/ansi = mshop/order/manager/basket/insert
```

* Default: mshop/order/manager/basket/insert


## insert/mysql

Inserts a new basket record into the database table or updates an existing one

```
mshop/order/manager/basket/insert/mysql =
 INSERT INTO "mshop_order_basket" (
 	"customerid", "content", "name", "mtime", "editor", "siteid", "ctime", "id"
 ) VALUES (
 	?, ?, ?, ?, ?, ?, ?, ?
 ) ON DUPLICATE KEY UPDATE
 	"customerid" = ?, "content" = ?, "name" = ?, "mtime" = ?, "editor" = ?
```

* Default: mshop/order/manager/basket/insert
* Type: string - SQL statement for inserting or updating records
* Since: 2022.10

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

* mshop/order/manager/basket/newid/ansi
* mshop/order/manager/basket/delete/ansi
* mshop/order/manager/basket/search/ansi
* mshop/order/manager/basket/count/ansi

## name

Class name of the used order basket manager implementation

```
mshop/order/manager/basket/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2022.10

Each default order basket manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Order\Manager\Basket\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Basket\Mybasket
```

then you have to set the this configuration option:

```
 mshop/order/manager/basket/name = Mybasket
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyBasket"!


## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/basket/search/ansi =
 SELECT :columns
 	mordba."id" AS "order.basket.id", mordba."siteid" AS "order.basket.siteid",
 	mordba."customerid" AS "order.basket.customerid", mordba."name" AS "order.basket.name",
 	mordba."content" AS "order.basket.content", mordba."mtime" AS "order.basket.mtime",
 	mordba."ctime" AS "order.basket.ctime", mordba."editor" AS "order.basket.editor"
 FROM "mshop_order_basket" mordba
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Default: mshop/order/manager/basket/search
* Type: string - SQL statement for searching items
* Since: 2022.10

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

* mshop/order/manager/basket/insert/ansi
* mshop/order/manager/basket/update/ansi
* mshop/order/manager/basket/newid/ansi
* mshop/order/manager/basket/delete/ansi
* mshop/order/manager/basket/count/ansi

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/basket/search/mysql =
 SELECT :columns
 	mordba."id" AS "order.basket.id", mordba."siteid" AS "order.basket.siteid",
 	mordba."customerid" AS "order.basket.customerid", mordba."name" AS "order.basket.name",
 	mordba."content" AS "order.basket.content", mordba."mtime" AS "order.basket.mtime",
 	mordba."ctime" AS "order.basket.ctime", mordba."editor" AS "order.basket.editor"
 FROM "mshop_order_basket" mordba
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default:
 SELECT :columns
 	mordba."id" AS "order.basket.id", mordba."siteid" AS "order.basket.siteid",
 	mordba."customerid" AS "order.basket.customerid", mordba."name" AS "order.basket.name",
 	mordba."content" AS "order.basket.content", mordba."mtime" AS "order.basket.mtime",
 	mordba."ctime" AS "order.basket.ctime", mordba."editor" AS "order.basket.editor"
 FROM "mshop_order_basket" mordba
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/basket/search/ansi

## submanagers

List of manager names that can be instantiated by the order basket manager

```
mshop/order/manager/basket/submanagers = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-manager names
* Since: 2022.10

Managers provide a generic interface to the underlying storage.
Each manager has or can have sub-managers caring about particular
aspects. Each of these sub-managers can be instantiated by its
parent manager using the getSubManager() method.

The search keys from sub-managers can be normally used in the
manager as well. It allows you to search for items of the manager
using the search keys of the sub-managers to further limit the
retrieved list of items.


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
 WHERE :cond AND "siteid" LIKE ?
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
 WHERE :cond AND "siteid" LIKE ?
```

* Default:
 DELETE FROM "mshop_order"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/order/manager/delete/ansi

# insert
## ansi

Inserts a new order record into the database table

```
mshop/order/manager/insert/ansi =
 INSERT INTO "mshop_order" ( :names
 	"baseid", "invoiceno", "channel", "datepayment", "datedelivery",
 	"statusdelivery", "statuspayment", "relatedid", "mtime",
 	"editor", "siteid", "ctime", "cdate", "cmonth", "cweek", "cwday", "chour"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
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
 	"baseid", "invoiceno", "channel", "datepayment", "datedelivery",
 	"statusdelivery", "statuspayment", "relatedid", "mtime",
 	"editor", "siteid", "ctime", "cdate", "cmonth", "cweek", "cwday", "chour"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default:
 INSERT INTO "mshop_order" ( :names
 	"baseid", "invoiceno", "channel", "datepayment", "datedelivery",
 	"statusdelivery", "statuspayment", "relatedid", "mtime",
 	"editor", "siteid", "ctime", "cdate", "cmonth", "cweek", "cwday", "chour"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
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
 	mord."id" AS "order.id", mord."baseid" AS "order.parentid", mord."channel" AS "order.channel",
 	mord."siteid" AS "order.siteid", mord."invoiceno" AS "order.invoiceno",
 	mord."datepayment" AS "order.datepayment", mord."datedelivery" AS "order.datedelivery",
 	mord."statuspayment" AS "order.statuspayment", mord."statusdelivery" AS "order.statusdelivery",
 	mord."relatedid" AS "order.relatedid", mord."ctime" AS "order.ctime",
 	mord."mtime" AS "order.mtime", mord."editor" AS "order.editor"
 FROM "mshop_order" mord
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mord."id", mord."baseid", mord."invoiceno", mord."siteid", mord."channel", mord."datepayment",
 	mord."datedelivery", mord."statuspayment", mord."statusdelivery", mord."relatedid", mord."ctime",
 	mord."mtime", mord."editor"
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
 	mord."id" AS "order.id", mord."baseid" AS "order.parentid", mord."channel" AS "order.channel",
 	mord."siteid" AS "order.siteid", mord."invoiceno" AS "order.invoiceno",
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
 	mord."id" AS "order.id", mord."baseid" AS "order.parentid", mord."channel" AS "order.channel",
 	mord."siteid" AS "order.siteid", mord."invoiceno" AS "order.invoiceno",
 	mord."datepayment" AS "order.datepayment", mord."datedelivery" AS "order.datedelivery",
 	mord."statuspayment" AS "order.statuspayment", mord."statusdelivery" AS "order.statusdelivery",
 	mord."relatedid" AS "order.relatedid", mord."ctime" AS "order.ctime",
 	mord."mtime" AS "order.mtime", mord."editor" AS "order.editor"
 FROM "mshop_order" mord
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mord."id", mord."baseid", mord."invoiceno", mord."siteid", mord."channel", mord."datepayment",
 	mord."datedelivery", mord."statuspayment", mord."statusdelivery", mord."relatedid", mord."ctime",
 	mord."mtime", mord."editor"
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
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_status" mordst
 	:joins
 	WHERE :cond
 	GROUP BY mordst.id, :cols
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
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_status" mordst
 	:joins
 	WHERE :cond
 	GROUP BY mordst.id, :cols
 	ORDER BY mordst.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default:
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_status" mordst
 	:joins
 	WHERE :cond
 	GROUP BY mordst.id, :cols
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
 WHERE :cond AND "siteid" LIKE ?
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
 WHERE :cond AND "siteid" LIKE ?
```

* Default:
 DELETE FROM "mshop_order_status"
 WHERE :cond AND "siteid" LIKE ?


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
 WHERE "siteid" LIKE ? AND "id" = ?
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
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default:
 UPDATE "mshop_order_status"
 SET :names
 	"parentid" = ?, "type" = ?, "value" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


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
 	"baseid" = ?, "invoiceno" = ?, "channel" = ?, "datepayment" = ?, "datedelivery" = ?,
 	"statusdelivery" = ?, "statuspayment" = ?, "relatedid" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
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
 	"baseid" = ?, "invoiceno" = ?, "channel" = ?, "datepayment" = ?, "datedelivery" = ?,
 	"statusdelivery" = ?, "statuspayment" = ?, "relatedid" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default:
 UPDATE "mshop_order"
 SET :names
 	"baseid" = ?, "invoiceno" = ?, "channel" = ?, "datepayment" = ?, "datedelivery" = ?,
 	"statusdelivery" = ?, "statuspayment" = ?, "relatedid" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/order/manager/update/ansi