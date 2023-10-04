
# address
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/address/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_address" mordad
 	:joins
 	WHERE :cond
 	GROUP BY mordad.id, :cols
 	ORDER BY mordad.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

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

## aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/address/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_address" mordad
 	:joins
 	WHERE :cond
 	GROUP BY mordad.id, :cols
 	ORDER BY mordad.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_address" mordad
 	:joins
 	WHERE :cond
 	GROUP BY mordad.id, :cols
 	ORDER BY mordad.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/address/aggregate/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/address/count/ansi = 
 SELECT COUNT( DISTINCT mordad."id" ) AS "count"
 FROM "mshop_order_address" mordad
 :joins
 WHERE :cond
```

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

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/address/count/mysql = 
 SELECT COUNT( DISTINCT mordad."id" ) AS "count"
 FROM "mshop_order_address" mordad
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordad."id" ) AS "count"
 FROM "mshop_order_address" mordad
 :joins
 WHERE :cond


See also:

* mshop/order/manager/address/count/ansi

## decorators/excludes

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

## decorators/global

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

## decorators/local

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
("\Aimeos\MShop\Order\Manager\Address\Decorator\*") around the
order base address manager.

```
 mshop/order/manager/address/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Address\Decorator\Decorator2" only
to the order base address manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/address/decorators/excludes
* mshop/order/manager/address/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/address/delete/ansi = 
 DELETE FROM "mshop_order_address"
 WHERE :cond AND "siteid" LIKE ?
```

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

## delete/mysql

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

## insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/address/insert/ansi = 
 INSERT INTO "mshop_order_address" ( :names
 	"parentid", "addrid", "type", "company", "vatid", "salutation",
 	"title", "firstname", "lastname", "address1", "address2",
 	"address3", "postal", "city", "state", "countryid", "langid",
 	"telephone", "mobile", "email", "telefax", "website", "longitude", "latitude",
 	"pos", "birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
 )
```

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

## insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/address/insert/mysql = 
 INSERT INTO "mshop_order_address" ( :names
 	"parentid", "addrid", "type", "company", "vatid", "salutation",
 	"title", "firstname", "lastname", "address1", "address2",
 	"address3", "postal", "city", "state", "countryid", "langid",
 	"telephone", "mobile", "email", "telefax", "website", "longitude", "latitude",
 	"pos", "birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
 )
```

* Default: 
 INSERT INTO "mshop_order_address" ( :names
 	"parentid", "addrid", "type", "company", "vatid", "salutation",
 	"title", "firstname", "lastname", "address1", "address2",
 	"address3", "postal", "city", "state", "countryid", "langid",
 	"telephone", "mobile", "email", "telefax", "website", "longitude", "latitude",
 	"pos", "birthday", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
 )


See also:

* mshop/order/manager/address/insert/ansi

## name

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
 \Aimeos\MShop\Order\Manager\Address\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Address\Myaddress
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


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/address/newid/ansi = 
```

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

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/address/newid/mysql = SELECT LAST_INSERT_ID()
```


See also:

* mshop/order/manager/address/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/address/search/ansi = 
 SELECT :columns
 	mordad."id" AS "order.address.id", mordad."parentid" AS "order.address.parentid",
 	mordad."siteid" AS "order.address.siteid", mordad."addrid" AS "order.address.addressid",
 	mordad."type" AS "order.address.type", mordad."company" AS "order.address.company",
 	mordad."vatid" AS "order.address.vatid", mordad."salutation" AS "order.address.salutation",
 	mordad."title" AS "order.address.title", mordad."firstname" AS "order.address.firstname",
 	mordad."lastname" AS "order.address.lastname", mordad."address1" AS "order.address.address1",
 	mordad."address2" AS "order.address.address2", mordad."address3" AS "order.address.address3",
 	mordad."postal" AS "order.address.postal", mordad."city" AS "order.address.city",
 	mordad."state" AS "order.address.state", mordad."countryid" AS "order.address.countryid",
 	mordad."langid" AS "order.address.languageid", mordad."telephone" AS "order.address.telephone",
 	mordad."email" AS "order.address.email", mordad."telefax" AS "order.address.telefax",
 	mordad."website" AS "order.address.website", mordad."longitude" AS "order.address.longitude",
 	mordad."latitude" AS "order.address.latitude", mordad."pos" AS "order.address.position",
 	mordad."mtime" AS "order.address.mtime", mordad."editor" AS "order.address.editor",
 	mordad."ctime" AS "order.address.ctime", mordad."birthday" AS "order.address.birthday",
 	mordad."mobile" AS "order.address.mobile"
 FROM "mshop_order_address" mordad
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

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

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/address/search/mysql = 
 SELECT :columns
 	mordad."id" AS "order.address.id", mordad."parentid" AS "order.address.parentid",
 	mordad."siteid" AS "order.address.siteid", mordad."addrid" AS "order.address.addressid",
 	mordad."type" AS "order.address.type", mordad."company" AS "order.address.company",
 	mordad."vatid" AS "order.address.vatid", mordad."salutation" AS "order.address.salutation",
 	mordad."title" AS "order.address.title", mordad."firstname" AS "order.address.firstname",
 	mordad."lastname" AS "order.address.lastname", mordad."address1" AS "order.address.address1",
 	mordad."address2" AS "order.address.address2", mordad."address3" AS "order.address.address3",
 	mordad."postal" AS "order.address.postal", mordad."city" AS "order.address.city",
 	mordad."state" AS "order.address.state", mordad."countryid" AS "order.address.countryid",
 	mordad."langid" AS "order.address.languageid", mordad."telephone" AS "order.address.telephone",
 	mordad."email" AS "order.address.email", mordad."telefax" AS "order.address.telefax",
 	mordad."website" AS "order.address.website", mordad."longitude" AS "order.address.longitude",
 	mordad."latitude" AS "order.address.latitude", mordad."pos" AS "order.address.position",
 	mordad."mtime" AS "order.address.mtime", mordad."editor" AS "order.address.editor",
 	mordad."ctime" AS "order.address.ctime", mordad."birthday" AS "order.address.birthday",
 	mordad."mobile" AS "order.address.mobile"
 FROM "mshop_order_address" mordad
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordad."id" AS "order.address.id", mordad."parentid" AS "order.address.parentid",
 	mordad."siteid" AS "order.address.siteid", mordad."addrid" AS "order.address.addressid",
 	mordad."type" AS "order.address.type", mordad."company" AS "order.address.company",
 	mordad."vatid" AS "order.address.vatid", mordad."salutation" AS "order.address.salutation",
 	mordad."title" AS "order.address.title", mordad."firstname" AS "order.address.firstname",
 	mordad."lastname" AS "order.address.lastname", mordad."address1" AS "order.address.address1",
 	mordad."address2" AS "order.address.address2", mordad."address3" AS "order.address.address3",
 	mordad."postal" AS "order.address.postal", mordad."city" AS "order.address.city",
 	mordad."state" AS "order.address.state", mordad."countryid" AS "order.address.countryid",
 	mordad."langid" AS "order.address.languageid", mordad."telephone" AS "order.address.telephone",
 	mordad."email" AS "order.address.email", mordad."telefax" AS "order.address.telefax",
 	mordad."website" AS "order.address.website", mordad."longitude" AS "order.address.longitude",
 	mordad."latitude" AS "order.address.latitude", mordad."pos" AS "order.address.position",
 	mordad."mtime" AS "order.address.mtime", mordad."editor" AS "order.address.editor",
 	mordad."ctime" AS "order.address.ctime", mordad."birthday" AS "order.address.birthday",
 	mordad."mobile" AS "order.address.mobile"
 FROM "mshop_order_address" mordad
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/address/search/ansi

## submanagers

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


## update/ansi

Updates an existing order record in the database

```
mshop/order/manager/address/update/ansi = 
 UPDATE "mshop_order_address"
 SET :names
 	"parentid" = ?, "addrid" = ?, "type" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?, "address2" = ?,
 	"address3" = ?, "postal" = ?, "city" = ?, "state" = ?, "countryid" = ?, "langid" = ?,
 	"telephone" = ?, "mobile" = ?, "email" = ?, "telefax" = ?, "website" = ?,
 	"longitude" = ?, "latitude" = ?, "pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

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

## update/mysql

Updates an existing order record in the database

```
mshop/order/manager/address/update/mysql = 
 UPDATE "mshop_order_address"
 SET :names
 	"parentid" = ?, "addrid" = ?, "type" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?, "address2" = ?,
 	"address3" = ?, "postal" = ?, "city" = ?, "state" = ?, "countryid" = ?, "langid" = ?,
 	"telephone" = ?, "mobile" = ?, "email" = ?, "telefax" = ?, "website" = ?,
 	"longitude" = ?, "latitude" = ?, "pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_order_address"
 SET :names
 	"parentid" = ?, "addrid" = ?, "type" = ?, "company" = ?, "vatid" = ?, "salutation" = ?,
 	"title" = ?, "firstname" = ?, "lastname" = ?, "address1" = ?, "address2" = ?,
 	"address3" = ?, "postal" = ?, "city" = ?, "state" = ?, "countryid" = ?, "langid" = ?,
 	"telephone" = ?, "mobile" = ?, "email" = ?, "telefax" = ?, "website" = ?,
 	"longitude" = ?, "latitude" = ?, "pos" = ?, "birthday" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/order/manager/address/update/ansi

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

* Type: string - SQL statement for aggregating the order items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/aggregate/ansi

## mysql

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/aggregateavg/mysql = 
```

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

* Type: string - SQL statement for aggregating the order items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/aggregate/ansi

## mysql

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/aggregatesum/mysql = 
```

* Type: string - SQL statement for aggregating the order items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/aggregatesum/ansi
* mshop/order/manager/aggregate/mysql

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
mshop/order/manager/basket/insert/ansi = 
```



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

# coupon
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/coupon/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_coupon" mordco
 	:joins
 	WHERE :cond
 	GROUP BY mordco.id, :cols
 	ORDER BY mordco.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

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

## aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/coupon/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_coupon" mordco
 	:joins
 	WHERE :cond
 	GROUP BY mordco.id, :cols
 	ORDER BY mordco.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_coupon" mordco
 	:joins
 	WHERE :cond
 	GROUP BY mordco.id, :cols
 	ORDER BY mordco.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/coupon/aggregate/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/coupon/count/ansi = 
 SELECT COUNT( DISTINCT mordco."id" ) AS "count"
 FROM "mshop_order_coupon" mordco
 :joins
 WHERE :cond
```

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

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/coupon/count/mysql = 
 SELECT COUNT( DISTINCT mordco."id" ) AS "count"
 FROM "mshop_order_coupon" mordco
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordco."id" ) AS "count"
 FROM "mshop_order_coupon" mordco
 :joins
 WHERE :cond


See also:

* mshop/order/manager/coupon/count/ansi

## decorators/excludes

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

## decorators/global

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

## decorators/local

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
("\Aimeos\MShop\Order\Manager\Coupon\Decorator\*") around the order
base coupon manager.

```
 mshop/order/manager/coupon/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Coupon\Decorator\Decorator2" only
to the order base coupon manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/coupon/decorators/excludes
* mshop/order/manager/coupon/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/coupon/delete/ansi = 
 DELETE FROM "mshop_order_coupon"
 WHERE :cond AND "siteid" LIKE ?
```

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

## delete/mysql

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

## insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/coupon/insert/ansi = 
 INSERT INTO "mshop_order_coupon" ( :names
 	"parentid", "ordprodid", "code", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )
```

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

## insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/coupon/insert/mysql = 
 INSERT INTO "mshop_order_coupon" ( :names
 	"parentid", "ordprodid", "code", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_order_coupon" ( :names
 	"parentid", "ordprodid", "code", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/coupon/insert/ansi

## name

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
 \Aimeos\MShop\Order\Manager\Coupon\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Coupon\Mycoupon
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


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/coupon/newid/ansi = 
```

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

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/coupon/newid/mysql = SELECT LAST_INSERT_ID()
```


See also:

* mshop/order/manager/coupon/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/coupon/search/ansi = 
 SELECT :columns
 	mordco."id" AS "order.coupon.id", mordco."parentid" AS "order.coupon.parentid",
 	mordco."siteid" AS "order.coupon.siteid", mordco."ordprodid" AS "order.coupon.ordprodid",
 	mordco."code" AS "order.coupon.code", mordco."mtime" AS "order.coupon.mtime",
 	mordco."editor" AS "order.coupon.editor", mordco."ctime" AS "order.coupon.ctime"
 FROM "mshop_order_coupon" mordco
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

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

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/coupon/search/mysql = 
 SELECT :columns
 	mordco."id" AS "order.coupon.id", mordco."parentid" AS "order.coupon.parentid",
 	mordco."siteid" AS "order.coupon.siteid", mordco."ordprodid" AS "order.coupon.ordprodid",
 	mordco."code" AS "order.coupon.code", mordco."mtime" AS "order.coupon.mtime",
 	mordco."editor" AS "order.coupon.editor", mordco."ctime" AS "order.coupon.ctime"
 FROM "mshop_order_coupon" mordco
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordco."id" AS "order.coupon.id", mordco."parentid" AS "order.coupon.parentid",
 	mordco."siteid" AS "order.coupon.siteid", mordco."ordprodid" AS "order.coupon.ordprodid",
 	mordco."code" AS "order.coupon.code", mordco."mtime" AS "order.coupon.mtime",
 	mordco."editor" AS "order.coupon.editor", mordco."ctime" AS "order.coupon.ctime"
 FROM "mshop_order_coupon" mordco
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/coupon/search/ansi

## submanagers

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


## update/ansi

Updates an existing order record in the database

```
mshop/order/manager/coupon/update/ansi = 
 UPDATE "mshop_order_coupon"
 SET :names
 	"parentid" = ?, "ordprodid" = ?, "code" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

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

## update/mysql

Updates an existing order record in the database

```
mshop/order/manager/coupon/update/mysql = 
 UPDATE "mshop_order_coupon"
 SET :names
 	"parentid" = ?, "ordprodid" = ?, "code" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_order_coupon"
 SET :names
 	"parentid" = ?, "ordprodid" = ?, "code" = ?, "mtime" = ?, "editor" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/order/manager/coupon/update/ansi

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
 	"invoiceno", "channel", "datepayment", "datedelivery",
 	"statusdelivery", "statuspayment", "relatedid",
 	"customerid", "sitecode", "langid", "currencyid",
 	"price", "costs", "rebate", "tax", "taxflag", "customerref",
 	"comment", "mtime", "editor", "siteid", "ctime",
 	"cdate", "cmonth", "cweek", "cwday", "chour"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

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
 	"invoiceno", "channel", "datepayment", "datedelivery",
 	"statusdelivery", "statuspayment", "relatedid",
 	"customerid", "sitecode", "langid", "currencyid",
 	"price", "costs", "rebate", "tax", "taxflag", "customerref",
 	"comment", "mtime", "editor", "siteid", "ctime",
 	"cdate", "cmonth", "cweek", "cwday", "chour"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_order" ( :names
 	"invoiceno", "channel", "datepayment", "datedelivery",
 	"statusdelivery", "statuspayment", "relatedid",
 	"customerid", "sitecode", "langid", "currencyid",
 	"price", "costs", "rebate", "tax", "taxflag", "customerref",
 	"comment", "mtime", "editor", "siteid", "ctime",
 	"cdate", "cmonth", "cweek", "cwday", "chour"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
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
mshop/order/manager/newid/ansi = 
```

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


See also:

* mshop/order/manager/newid/ansi

# product
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/product/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_product" mordpr
 	:joins
 	WHERE :cond
 	GROUP BY mordpr.id, :cols
 	ORDER BY mordpr.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

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

## aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/product/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_product" mordpr
 	:joins
 	WHERE :cond
 	GROUP BY mordpr.id, :cols
 	ORDER BY mordpr.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_product" mordpr
 	:joins
 	WHERE :cond
 	GROUP BY mordpr.id, :cols
 	ORDER BY mordpr.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/product/aggregate/ansi

## aggregateavg/ansi

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/product/aggregateavg/ansi = 
```

* Type: string - SQL statement for aggregating the order product items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/product/aggregate/ansi

## aggregateavg/mysql

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/product/aggregateavg/mysql = 
```

* Type: string - SQL statement for aggregating the order product items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/product/aggregateavg/ansi
* mshop/order/manager/product/aggregate/mysql

## aggregatesum/ansi

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/product/aggregatesum/ansi = 
```

* Type: string - SQL statement for aggregating the order product items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/product/aggregate/ansi

## aggregatesum/mysql

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/product/aggregatesum/mysql = 
```

* Type: string - SQL statement for aggregating the order product items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/product/aggregatesum/ansi
* mshop/order/manager/product/aggregate/mysql

## attribute/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/product/attribute/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_product_attr" mordprat
 	:joins
 	WHERE :cond
 	GROUP BY mordprat.id, :cols
 	ORDER BY mordprat.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

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

## attribute/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/product/attribute/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_product_attr" mordprat
 	:joins
 	WHERE :cond
 	GROUP BY mordprat.id, :cols
 	ORDER BY mordprat.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_product_attr" mordprat
 	:joins
 	WHERE :cond
 	GROUP BY mordprat.id, :cols
 	ORDER BY mordprat.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/product/attribute/aggregate/ansi

## attribute/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/product/attribute/count/ansi = 
 SELECT COUNT( DISTINCT mordprat."id" ) AS "count"
 FROM "mshop_order_product_attr" mordprat
 :joins
 WHERE :cond
```

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

## attribute/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/product/attribute/count/mysql = 
 SELECT COUNT( DISTINCT mordprat."id" ) AS "count"
 FROM "mshop_order_product_attr" mordprat
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordprat."id" ) AS "count"
 FROM "mshop_order_product_attr" mordprat
 :joins
 WHERE :cond


See also:

* mshop/order/manager/product/attribute/count/ansi

## attribute/decorators/excludes

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

## attribute/decorators/global

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

## attribute/decorators/local

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
("\Aimeos\MShop\Order\Manager\Product\Attribute\Decorator\*")
around the order base product attribute manager.

```
 mshop/order/manager/product/attribute/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Product\Attribute\Decorator\Decorator2"
only to the order base product attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/product/attribute/decorators/excludes
* mshop/order/manager/product/attribute/decorators/global

## attribute/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/product/attribute/delete/ansi = 
 DELETE FROM "mshop_order_product_attr"
 WHERE :cond AND "siteid" LIKE ?
```

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

## attribute/delete/mysql

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

## attribute/insert/ansi

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

## attribute/insert/mysql

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

## attribute/name

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
 \Aimeos\MShop\Order\Manager\Product\Attribute\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Product\Attribute\Myattribute
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


## attribute/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/product/attribute/newid/ansi = 
```

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

## attribute/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/product/attribute/newid/mysql = SELECT LAST_INSERT_ID()
```


See also:

* mshop/order/manager/product/attribute/newid/ansi

## attribute/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/product/attribute/search/ansi = 
 SELECT :columns
 	mordprat."id" AS "order.product.attribute.id", mordprat."siteid" AS "order.product.attribute.siteid",
 	mordprat."attrid" AS "order.product.attribute.attributeid", mordprat."parentid" AS "order.product.attribute.parentid",
 	mordprat."type" AS "order.product.attribute.type", mordprat."code" AS "order.product.attribute.code",
 	mordprat."value" AS "order.product.attribute.value", mordprat."quantity" AS "order.product.attribute.quantity",
 	mordprat."name" AS "order.product.attribute.name", mordprat."mtime" AS "order.product.attribute.mtime",
 	mordprat."editor" AS "order.product.attribute.editor", mordprat."ctime" AS "order.product.attribute.ctime",
 	mordprat."price" AS "order.product.attribute.price"
 FROM "mshop_order_product_attr" mordprat
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

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

## attribute/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/product/attribute/search/mysql = 
 SELECT :columns
 	mordprat."id" AS "order.product.attribute.id", mordprat."siteid" AS "order.product.attribute.siteid",
 	mordprat."attrid" AS "order.product.attribute.attributeid", mordprat."parentid" AS "order.product.attribute.parentid",
 	mordprat."type" AS "order.product.attribute.type", mordprat."code" AS "order.product.attribute.code",
 	mordprat."value" AS "order.product.attribute.value", mordprat."quantity" AS "order.product.attribute.quantity",
 	mordprat."name" AS "order.product.attribute.name", mordprat."mtime" AS "order.product.attribute.mtime",
 	mordprat."editor" AS "order.product.attribute.editor", mordprat."ctime" AS "order.product.attribute.ctime",
 	mordprat."price" AS "order.product.attribute.price"
 FROM "mshop_order_product_attr" mordprat
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordprat."id" AS "order.product.attribute.id", mordprat."siteid" AS "order.product.attribute.siteid",
 	mordprat."attrid" AS "order.product.attribute.attributeid", mordprat."parentid" AS "order.product.attribute.parentid",
 	mordprat."type" AS "order.product.attribute.type", mordprat."code" AS "order.product.attribute.code",
 	mordprat."value" AS "order.product.attribute.value", mordprat."quantity" AS "order.product.attribute.quantity",
 	mordprat."name" AS "order.product.attribute.name", mordprat."mtime" AS "order.product.attribute.mtime",
 	mordprat."editor" AS "order.product.attribute.editor", mordprat."ctime" AS "order.product.attribute.ctime",
 	mordprat."price" AS "order.product.attribute.price"
 FROM "mshop_order_product_attr" mordprat
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/product/attribute/search/ansi

## attribute/submanagers

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


## attribute/update/ansi

Updates an existing order record in the database

```
mshop/order/manager/product/attribute/update/ansi = 
```

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

## attribute/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/product/attribute/update/mysql = 
```


See also:

* mshop/order/manager/product/attribute/update/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/product/count/ansi = 
 SELECT COUNT( DISTINCT mordpr."id" ) AS "count"
 FROM "mshop_order_product" mordpr
 :joins
 WHERE :cond
```

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

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/product/count/mysql = 
 SELECT COUNT( DISTINCT mordpr."id" ) AS "count"
 FROM "mshop_order_product" mordpr
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordpr."id" ) AS "count"
 FROM "mshop_order_product" mordpr
 :joins
 WHERE :cond


See also:

* mshop/order/manager/product/count/ansi

## decorators/excludes

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

## decorators/global

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

## decorators/local

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
("\Aimeos\MShop\Order\Manager\Product\Decorator\*") around the
order base product manager.

```
 mshop/order/manager/product/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Product\Decorator\Decorator2" only
to the order base product manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/product/decorators/excludes
* mshop/order/manager/product/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/product/delete/ansi = 
 DELETE FROM "mshop_order_product"
 WHERE :cond AND "siteid" LIKE ?
```

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

## delete/mysql

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

## insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/product/insert/ansi = 
 INSERT INTO "mshop_order_product" ( :names
 	"parentid", "ordprodid", "ordaddrid", "type", "parentprodid", "prodid", "prodcode",
 	"vendor", "stocktype", "name", "description", "mediaurl", "timeframe",
 	"quantity", "currencyid", "price", "costs", "rebate", "tax", "taxrate", "taxflag",
 	"flags", "statuspayment", "statusdelivery", "pos", "mtime", "editor", "target",
 	"qtyopen", "notes", "scale", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

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

## insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/product/insert/mysql = 
 INSERT INTO "mshop_order_product" ( :names
 	"parentid", "ordprodid", "ordaddrid", "type", "parentprodid", "prodid", "prodcode",
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
 	"parentid", "ordprodid", "ordaddrid", "type", "parentprodid", "prodid", "prodcode",
 	"vendor", "stocktype", "name", "description", "mediaurl", "timeframe",
 	"quantity", "currencyid", "price", "costs", "rebate", "tax", "taxrate", "taxflag",
 	"flags", "statuspayment", "statusdelivery", "pos", "mtime", "editor", "target",
 	"qtyopen", "notes", "scale", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/product/insert/ansi

## name

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
 \Aimeos\MShop\Order\Manager\Product\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Product\Myproduct
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


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/product/newid/ansi = 
```

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

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/product/newid/mysql = SELECT LAST_INSERT_ID()
```


See also:

* mshop/order/manager/product/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/product/search/ansi = 
 SELECT :columns
 	mordpr."id" AS "order.product.id", mordpr."parentid" AS "order.product.parentid",
 	mordpr."siteid" AS "order.product.siteid", mordpr."ordprodid" AS "order.product.orderproductid",
 	mordpr."prodid" AS "order.product.productid", mordpr."prodcode" AS "order.product.prodcode",
 	mordpr."description" AS "order.product.description", mordpr."stocktype" AS "order.product.stocktype",
 	mordpr."type" AS "order.product.type", mordpr."name" AS "order.product.name",
 	mordpr."mediaurl" AS "order.product.mediaurl", mordpr."timeframe" AS "order.product.timeframe",
 	mordpr."quantity" AS "order.product.quantity", mordpr."currencyid" AS "order.product.currencyid",
 	mordpr."price" AS "order.product.price", mordpr."costs" AS "order.product.costs",
 	mordpr."rebate" AS "order.product.rebate", mordpr."tax" AS "order.product.taxvalue",
 	mordpr."taxrate" AS "order.product.taxrates", mordpr."taxflag" AS "order.product.taxflag",
 	mordpr."flags" AS "order.product.flags", mordpr."statusdelivery" AS "order.product.statusdelivery",
 	mordpr."pos" AS "order.product.position", mordpr."mtime" AS "order.product.mtime",
 	mordpr."editor" AS "order.product.editor", mordpr."ctime" AS "order.product.ctime",
 	mordpr."target" AS "order.product.target", mordpr."ordaddrid" AS "order.product.orderaddressid",
 	mordpr."vendor" AS "order.product.vendor", mordpr."scale" AS "order.product.scale",
 	mordpr."qtyopen" AS "order.product.qtyopen", mordpr."notes" AS "order.product.notes",
 	mordpr."statuspayment" AS "order.product.statuspayment", mordpr."parentprodid" AS "order.product.parentproductid"
 FROM "mshop_order_product" mordpr
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mordpr."id", mordpr."parentid", mordpr."siteid", mordpr."ordprodid", mordpr."prodid",
 	mordpr."prodcode", mordpr."description", mordpr."stocktype", mordpr."type",
 	mordpr."name", mordpr."mediaurl", mordpr."timeframe", mordpr."quantity",
 	mordpr."currencyid", mordpr."price", mordpr."costs", mordpr."rebate", mordpr."tax",
 	mordpr."taxrate", mordpr."taxflag", mordpr."flags", mordpr."statusdelivery", mordpr."pos",
 	mordpr."mtime", mordpr."editor", mordpr."ctime", mordpr."target", mordpr."ordaddrid",
 	mordpr."vendor", mordpr."qtyopen", mordpr."notes", mordpr."scale",
 	mordpr."statuspayment", mordpr."parentprodid"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

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

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/product/search/mysql = 
 SELECT :columns
 	mordpr."id" AS "order.product.id", mordpr."parentid" AS "order.product.parentid",
 	mordpr."siteid" AS "order.product.siteid", mordpr."ordprodid" AS "order.product.orderproductid",
 	mordpr."prodid" AS "order.product.productid", mordpr."prodcode" AS "order.product.prodcode",
 	mordpr."description" AS "order.product.description", mordpr."stocktype" AS "order.product.stocktype",
 	mordpr."type" AS "order.product.type", mordpr."name" AS "order.product.name",
 	mordpr."mediaurl" AS "order.product.mediaurl", mordpr."timeframe" AS "order.product.timeframe",
 	mordpr."quantity" AS "order.product.quantity", mordpr."currencyid" AS "order.product.currencyid",
 	mordpr."price" AS "order.product.price", mordpr."costs" AS "order.product.costs",
 	mordpr."rebate" AS "order.product.rebate", mordpr."tax" AS "order.product.taxvalue",
 	mordpr."taxrate" AS "order.product.taxrates", mordpr."taxflag" AS "order.product.taxflag",
 	mordpr."flags" AS "order.product.flags", mordpr."statusdelivery" AS "order.product.statusdelivery",
 	mordpr."pos" AS "order.product.position", mordpr."mtime" AS "order.product.mtime",
 	mordpr."editor" AS "order.product.editor", mordpr."ctime" AS "order.product.ctime",
 	mordpr."target" AS "order.product.target", mordpr."ordaddrid" AS "order.product.orderaddressid",
 	mordpr."vendor" AS "order.product.vendor", mordpr."scale" AS "order.product.scale",
 	mordpr."qtyopen" AS "order.product.qtyopen", mordpr."notes" AS "order.product.notes",
 	mordpr."statuspayment" AS "order.product.statuspayment", mordpr."parentprodid" AS "order.product.parentproductid"
 FROM "mshop_order_product" mordpr
 :joins
 WHERE :cond
 GROUP BY :group mordpr."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordpr."id" AS "order.product.id", mordpr."parentid" AS "order.product.parentid",
 	mordpr."siteid" AS "order.product.siteid", mordpr."ordprodid" AS "order.product.orderproductid",
 	mordpr."prodid" AS "order.product.productid", mordpr."prodcode" AS "order.product.prodcode",
 	mordpr."description" AS "order.product.description", mordpr."stocktype" AS "order.product.stocktype",
 	mordpr."type" AS "order.product.type", mordpr."name" AS "order.product.name",
 	mordpr."mediaurl" AS "order.product.mediaurl", mordpr."timeframe" AS "order.product.timeframe",
 	mordpr."quantity" AS "order.product.quantity", mordpr."currencyid" AS "order.product.currencyid",
 	mordpr."price" AS "order.product.price", mordpr."costs" AS "order.product.costs",
 	mordpr."rebate" AS "order.product.rebate", mordpr."tax" AS "order.product.taxvalue",
 	mordpr."taxrate" AS "order.product.taxrates", mordpr."taxflag" AS "order.product.taxflag",
 	mordpr."flags" AS "order.product.flags", mordpr."statusdelivery" AS "order.product.statusdelivery",
 	mordpr."pos" AS "order.product.position", mordpr."mtime" AS "order.product.mtime",
 	mordpr."editor" AS "order.product.editor", mordpr."ctime" AS "order.product.ctime",
 	mordpr."target" AS "order.product.target", mordpr."ordaddrid" AS "order.product.orderaddressid",
 	mordpr."vendor" AS "order.product.vendor", mordpr."scale" AS "order.product.scale",
 	mordpr."qtyopen" AS "order.product.qtyopen", mordpr."notes" AS "order.product.notes",
 	mordpr."statuspayment" AS "order.product.statuspayment", mordpr."parentprodid" AS "order.product.parentproductid"
 FROM "mshop_order_product" mordpr
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mordpr."id", mordpr."parentid", mordpr."siteid", mordpr."ordprodid", mordpr."prodid",
 	mordpr."prodcode", mordpr."description", mordpr."stocktype", mordpr."type",
 	mordpr."name", mordpr."mediaurl", mordpr."timeframe", mordpr."quantity",
 	mordpr."currencyid", mordpr."price", mordpr."costs", mordpr."rebate", mordpr."tax",
 	mordpr."taxrate", mordpr."taxflag", mordpr."flags", mordpr."statusdelivery", mordpr."pos",
 	mordpr."mtime", mordpr."editor", mordpr."ctime", mordpr."target", mordpr."ordaddrid",
 	mordpr."vendor", mordpr."qtyopen", mordpr."notes", mordpr."scale",
 	mordpr."statuspayment", mordpr."parentprodid"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/product/search/ansi

## submanagers

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


## update/ansi

Updates an existing order record in the database

```
mshop/order/manager/product/update/ansi = 
 UPDATE "mshop_order_product"
 SET :names
 	"parentid" = ?, "ordprodid" = ?, "ordaddrid" = ?, "type" = ?, "parentprodid" = ?,
 	"prodid" = ?, "prodcode" = ?, "vendor" = ?, "stocktype" = ?,
 	"name" = ?, "description" = ?, "mediaurl" = ?, "timeframe" = ?, "quantity" = ?,
 	"currencyid" = ?, "price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "flags" = ?, "statuspayment" = ?, "statusdelivery" = ?, "pos" = ?,
 	"mtime" = ?, "editor" = ?, "target" = ?, "qtyopen" = ?, "notes" = ?, "scale" = ?
 WHERE "siteid" LIKE ? AND "id" = ?
```

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

## update/mysql

Updates an existing order record in the database

```
mshop/order/manager/product/update/mysql = 
 UPDATE "mshop_order_product"
 SET :names
 	"parentid" = ?, "ordprodid" = ?, "ordaddrid" = ?, "type" = ?, "parentprodid" = ?,
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
 	"parentid" = ?, "ordprodid" = ?, "ordaddrid" = ?, "type" = ?, "parentprodid" = ?,
 	"prodid" = ?, "prodcode" = ?, "vendor" = ?, "stocktype" = ?,
 	"name" = ?, "description" = ?, "mediaurl" = ?, "timeframe" = ?, "quantity" = ?,
 	"currencyid" = ?, "price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxrate" = ?,
 	"taxflag" = ?, "flags" = ?, "statuspayment" = ?, "statusdelivery" = ?, "pos" = ?,
 	"mtime" = ?, "editor" = ?, "target" = ?, "qtyopen" = ?, "notes" = ?, "scale" = ?
 WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/order/manager/product/update/ansi

# resource

Name of the database connection resource to use

```
mshop/order/manager/resource = db-order
```

* Default: db-order
* Type: string - Database connection name
* Since: 2023.04
* Since: 2023.04
* Since: 2023.04
* Since: 2023.04
* Since: 2023.04
* Since: 2023.04
* Since: 2023.04
* Since: 2023.04
* Since: 2023.04
* Since: 2023.04

You can configure a different database connection for each data domain
and if no such connection name exists, the "db" connection will be used.
It's also possible to use the same database connection for different
data domains by configuring the same connection name using this setting.


# search
## ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/search/ansi = 
 SELECT :columns
 	mord."id" AS "order.id", mord."channel" AS "order.channel",
 	mord."siteid" AS "order.siteid", mord."invoiceno" AS "order.invoiceno",
 	mord."datepayment" AS "order.datepayment", mord."datedelivery" AS "order.datedelivery",
 	mord."statuspayment" AS "order.statuspayment", mord."statusdelivery" AS "order.statusdelivery",
 	mord."relatedid" AS "order.relatedid",
 	mord."sitecode" AS "order.sitecode", mord."customerid" AS "order.customerid",
 	mord."langid" AS "order.languageid", mord."currencyid" AS "order.currencyid",
 	mord."price" AS "order.price", mord."costs" AS "order.costs",
 	mord."rebate" AS "order.rebate", mord."tax" AS "order.taxvalue",
 	mord."taxflag" AS "order.taxflag", mord."customerref" AS "order.customerref",
 	mord."comment" AS "order.comment", mord."ctime" AS "order.ctime",
 	mord."mtime" AS "order.mtime", mord."editor" AS "order.editor"
 FROM "mshop_order" mord
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mord."id", mord."invoiceno", mord."siteid", mord."channel", mord."datepayment",
 	mord."datedelivery", mord."statuspayment", mord."statusdelivery", mord."relatedid",
 	mord."sitecode", mord."customerid", mord."langid", mord."currencyid", mord."price",
 	mord."costs", mord."rebate", mord."tax", mord."taxflag", mord."customerref", mord."comment",
 	mord."ctime", mord."mtime", mord."editor"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

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
 	mord."id" AS "order.id", mord."channel" AS "order.channel",
 	mord."siteid" AS "order.siteid", mord."invoiceno" AS "order.invoiceno",
 	mord."datepayment" AS "order.datepayment", mord."datedelivery" AS "order.datedelivery",
 	mord."statuspayment" AS "order.statuspayment", mord."statusdelivery" AS "order.statusdelivery",
 	mord."relatedid" AS "order.relatedid",
 	mord."sitecode" AS "order.sitecode", mord."customerid" AS "order.customerid",
 	mord."langid" AS "order.languageid", mord."currencyid" AS "order.currencyid",
 	mord."price" AS "order.price", mord."costs" AS "order.costs",
 	mord."rebate" AS "order.rebate", mord."tax" AS "order.taxvalue",
 	mord."taxflag" AS "order.taxflag", mord."customerref" AS "order.customerref",
 	mord."comment" AS "order.comment", mord."ctime" AS "order.ctime",
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
 	mord."id" AS "order.id", mord."channel" AS "order.channel",
 	mord."siteid" AS "order.siteid", mord."invoiceno" AS "order.invoiceno",
 	mord."datepayment" AS "order.datepayment", mord."datedelivery" AS "order.datedelivery",
 	mord."statuspayment" AS "order.statuspayment", mord."statusdelivery" AS "order.statusdelivery",
 	mord."relatedid" AS "order.relatedid",
 	mord."sitecode" AS "order.sitecode", mord."customerid" AS "order.customerid",
 	mord."langid" AS "order.languageid", mord."currencyid" AS "order.currencyid",
 	mord."price" AS "order.price", mord."costs" AS "order.costs",
 	mord."rebate" AS "order.rebate", mord."tax" AS "order.taxvalue",
 	mord."taxflag" AS "order.taxflag", mord."customerref" AS "order.customerref",
 	mord."comment" AS "order.comment", mord."ctime" AS "order.ctime",
 	mord."mtime" AS "order.mtime", mord."editor" AS "order.editor"
 FROM "mshop_order" mord
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mord."id", mord."invoiceno", mord."siteid", mord."channel", mord."datepayment",
 	mord."datedelivery", mord."statuspayment", mord."statusdelivery", mord."relatedid",
 	mord."sitecode", mord."customerid", mord."langid", mord."currencyid", mord."price",
 	mord."costs", mord."rebate", mord."tax", mord."taxflag", mord."customerref", mord."comment",
 	mord."ctime", mord."mtime", mord."editor"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/search/ansi

# service
## aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/service/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service" mordse
 	:joins
 	WHERE :cond
 	GROUP BY mordse.id, :cols
 	ORDER BY mordse.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

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

## aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/service/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service" mordse
 	:joins
 	WHERE :cond
 	GROUP BY mordse.id, :cols
 	ORDER BY mordse.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service" mordse
 	:joins
 	WHERE :cond
 	GROUP BY mordse.id, :cols
 	ORDER BY mordse.id DESC
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/service/aggregate/ansi

## aggregateavg/ansi

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/service/aggregateavg/ansi = 
```

* Type: string - SQL statement for aggregating the order service items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/service/aggregate/ansi

## aggregateavg/mysql

Computes the average of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/service/aggregateavg/mysql = 
```

* Type: string - SQL statement for aggregating the order service items and computing the average value
* Since: 2017.10

See also:

* mshop/order/manager/service/aggregateavg/ansi
* mshop/order/manager/service/aggregate/mysql

## aggregatesum/ansi

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/service/aggregatesum/ansi = 
```

* Type: string - SQL statement for aggregating the order service items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/service/aggregate/ansi

## aggregatesum/mysql

Computes the sum of all values grouped by the key column and matched by the given criteria

```
mshop/order/manager/service/aggregatesum/mysql = 
```

* Type: string - SQL statement for aggregating the order service items and computing the sum
* Since: 2017.10

See also:

* mshop/order/manager/service/aggregatesum/ansi
* mshop/order/manager/service/aggregate/mysql

## attribute/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/service/attribute/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service_attr" mordseat
 	:joins
 	WHERE :cond
 	GROUP BY mordseat.id, :cols
 	ORDER BY mordseat.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

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

## attribute/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/service/attribute/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service_attr" mordseat
 	:joins
 	WHERE :cond
 	GROUP BY mordseat.id, :cols
 	ORDER BY mordseat.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service_attr" mordseat
 	:joins
 	WHERE :cond
 	GROUP BY mordseat.id, :cols
 	ORDER BY mordseat.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/service/attribute/aggregate/ansi

## attribute/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/service/attribute/count/ansi = 
 SELECT COUNT( DISTINCT mordseat."id" ) AS "count"
 FROM "mshop_order_service_attr" mordseat
 :joins
 WHERE :cond
```

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

## attribute/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/service/attribute/count/mysql = 
 SELECT COUNT( DISTINCT mordseat."id" ) AS "count"
 FROM "mshop_order_service_attr" mordseat
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordseat."id" ) AS "count"
 FROM "mshop_order_service_attr" mordseat
 :joins
 WHERE :cond


See also:

* mshop/order/manager/service/attribute/count/ansi

## attribute/decorators/excludes

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

## attribute/decorators/global

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

## attribute/decorators/local

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
("\Aimeos\MShop\Order\Manager\Service\Attribute\Decorator\*")
around the order base service attribute manager.

```
 mshop/order/manager/service/attribute/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Service\Attribute\Decorator\Decorator2"
only to the order base service attribute manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/attribute/decorators/excludes
* mshop/order/manager/service/attribute/decorators/global

## attribute/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/service/attribute/delete/ansi = 
 DELETE FROM "mshop_order_service_attr"
 WHERE :cond AND "siteid" LIKE ?
```

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

## attribute/delete/mysql

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

## attribute/insert/ansi

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

## attribute/insert/mysql

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

## attribute/name

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
 \Aimeos\MShop\Order\Manager\Service\Attribute\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Service\Attribute\Myattribute
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


## attribute/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/service/attribute/newid/ansi = 
```

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

## attribute/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/service/attribute/newid/mysql = SELECT LAST_INSERT_ID()
```


See also:

* mshop/order/manager/service/attribute/newid/ansi

## attribute/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/attribute/search/ansi = 
 SELECT :columns
 	mordseat."id" AS "order.service.attribute.id", mordseat."siteid" AS "order.service.attribute.siteid",
 	mordseat."attrid" AS "order.service.attribute.attributeid", mordseat."parentid" AS "order.service.attribute.parentid",
 	mordseat."type" AS "order.service.attribute.type", mordseat."code" AS "order.service.attribute.code",
 	mordseat."value" AS "order.service.attribute.value", mordseat."quantity" AS "order.service.attribute.quantity",
 	mordseat."name" AS "order.service.attribute.name", mordseat."mtime" AS "order.service.attribute.mtime",
 	mordseat."ctime" AS "order.service.attribute.ctime", mordseat."editor" AS "order.service.attribute.editor",
 	mordseat."price" AS "order.service.attribute.price"
 FROM "mshop_order_service_attr" mordseat
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

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

## attribute/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/attribute/search/mysql = 
 SELECT :columns
 	mordseat."id" AS "order.service.attribute.id", mordseat."siteid" AS "order.service.attribute.siteid",
 	mordseat."attrid" AS "order.service.attribute.attributeid", mordseat."parentid" AS "order.service.attribute.parentid",
 	mordseat."type" AS "order.service.attribute.type", mordseat."code" AS "order.service.attribute.code",
 	mordseat."value" AS "order.service.attribute.value", mordseat."quantity" AS "order.service.attribute.quantity",
 	mordseat."name" AS "order.service.attribute.name", mordseat."mtime" AS "order.service.attribute.mtime",
 	mordseat."ctime" AS "order.service.attribute.ctime", mordseat."editor" AS "order.service.attribute.editor",
 	mordseat."price" AS "order.service.attribute.price"
 FROM "mshop_order_service_attr" mordseat
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordseat."id" AS "order.service.attribute.id", mordseat."siteid" AS "order.service.attribute.siteid",
 	mordseat."attrid" AS "order.service.attribute.attributeid", mordseat."parentid" AS "order.service.attribute.parentid",
 	mordseat."type" AS "order.service.attribute.type", mordseat."code" AS "order.service.attribute.code",
 	mordseat."value" AS "order.service.attribute.value", mordseat."quantity" AS "order.service.attribute.quantity",
 	mordseat."name" AS "order.service.attribute.name", mordseat."mtime" AS "order.service.attribute.mtime",
 	mordseat."ctime" AS "order.service.attribute.ctime", mordseat."editor" AS "order.service.attribute.editor",
 	mordseat."price" AS "order.service.attribute.price"
 FROM "mshop_order_service_attr" mordseat
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/service/attribute/search/ansi

## attribute/submanagers

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


## attribute/update/ansi

Updates an existing order record in the database

```
mshop/order/manager/service/attribute/update/ansi = 
```

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

## attribute/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/service/attribute/update/mysql = 
```


See also:

* mshop/order/manager/service/attribute/update/ansi

## count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/service/count/ansi = 
 SELECT COUNT( DISTINCT mordse."id" ) AS "count"
 FROM "mshop_order_service" mordse
 :joins
 WHERE :cond
```

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

## count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/service/count/mysql = 
 SELECT COUNT( DISTINCT mordse."id" ) AS "count"
 FROM "mshop_order_service" mordse
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordse."id" ) AS "count"
 FROM "mshop_order_service" mordse
 :joins
 WHERE :cond


See also:

* mshop/order/manager/service/count/ansi

## decorators/excludes

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

## decorators/global

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

## decorators/local

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
("\Aimeos\MShop\Order\Manager\Service\Decorator\*") around the
order base service manager.

```
 mshop/order/manager/service/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Service\Decorator\Decorator2" only
to the order base service manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/decorators/excludes
* mshop/order/manager/service/decorators/global

## delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/service/delete/ansi = 
 DELETE FROM "mshop_order_service"
 WHERE :cond AND "siteid" LIKE ?
```

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

## delete/mysql

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

## insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/service/insert/ansi = 
 INSERT INTO "mshop_order_service" ( :names
 	"parentid", "servid", "type", "code", "name", "mediaurl",
 	"currencyid", "price", "costs", "rebate", "tax", "taxrate",
 	"taxflag", "pos", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

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

## insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/service/insert/mysql = 
 INSERT INTO "mshop_order_service" ( :names
 	"parentid", "servid", "type", "code", "name", "mediaurl",
 	"currencyid", "price", "costs", "rebate", "tax", "taxrate",
 	"taxflag", "pos", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_order_service" ( :names
 	"parentid", "servid", "type", "code", "name", "mediaurl",
 	"currencyid", "price", "costs", "rebate", "tax", "taxrate",
 	"taxflag", "pos", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/service/insert/ansi

## name

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
 \Aimeos\MShop\Order\Manager\Service\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Service\Myservice
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


## newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/service/newid/ansi = 
```

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

## newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/service/newid/mysql = SELECT LAST_INSERT_ID()
```


See also:

* mshop/order/manager/service/newid/ansi

## search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/search/ansi = 
 SELECT :columns
 	mordse."id" AS "order.service.id", mordse."parentid" AS "order.service.parentid",
 	mordse."siteid" AS "order.service.siteid", mordse."servid" AS "order.service.serviceid",
 	mordse."type" AS "order.service.type", mordse."code" AS "order.service.code",
 	mordse."name" AS "order.service.name", mordse."mediaurl" AS "order.service.mediaurl",
 	mordse."currencyid" AS "order.service.currencyid", mordse."price" AS "order.service.price",
 	mordse."costs" AS "order.service.costs", mordse."rebate" AS "order.service.rebate",
 	mordse."tax" AS "order.service.taxvalue", mordse."taxrate" AS "order.service.taxrates",
 	mordse."taxflag" AS "order.service.taxflag", mordse."pos" AS "order.service.position",
 	mordse."mtime" AS "order.service.mtime", mordse."editor" AS "order.service.editor",
 	mordse."ctime" AS "order.service.ctime"
 FROM "mshop_order_service" mordse
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mordse."id", mordse."parentid", mordse."siteid", mordse."servid", mordse."type",
 	mordse."code", mordse."name", mordse."mediaurl", mordse."currencyid", mordse."price",
 	mordse."costs", mordse."rebate", mordse."tax", mordse."taxrate", mordse."taxflag",
 	mordse."pos", mordse."mtime", mordse."editor", mordse."ctime"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

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

## search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/search/mysql = 
 SELECT :columns
 	mordse."id" AS "order.service.id", mordse."parentid" AS "order.service.parentid",
 	mordse."siteid" AS "order.service.siteid", mordse."servid" AS "order.service.serviceid",
 	mordse."type" AS "order.service.type", mordse."code" AS "order.service.code",
 	mordse."name" AS "order.service.name", mordse."mediaurl" AS "order.service.mediaurl",
 	mordse."currencyid" AS "order.service.currencyid", mordse."price" AS "order.service.price",
 	mordse."costs" AS "order.service.costs", mordse."rebate" AS "order.service.rebate",
 	mordse."tax" AS "order.service.taxvalue", mordse."taxrate" AS "order.service.taxrates",
 	mordse."taxflag" AS "order.service.taxflag", mordse."pos" AS "order.service.position",
 	mordse."mtime" AS "order.service.mtime", mordse."editor" AS "order.service.editor",
 	mordse."ctime" AS "order.service.ctime"
 FROM "mshop_order_service" mordse
 :joins
 WHERE :cond
 GROUP BY :group mordse."id"
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordse."id" AS "order.service.id", mordse."parentid" AS "order.service.parentid",
 	mordse."siteid" AS "order.service.siteid", mordse."servid" AS "order.service.serviceid",
 	mordse."type" AS "order.service.type", mordse."code" AS "order.service.code",
 	mordse."name" AS "order.service.name", mordse."mediaurl" AS "order.service.mediaurl",
 	mordse."currencyid" AS "order.service.currencyid", mordse."price" AS "order.service.price",
 	mordse."costs" AS "order.service.costs", mordse."rebate" AS "order.service.rebate",
 	mordse."tax" AS "order.service.taxvalue", mordse."taxrate" AS "order.service.taxrates",
 	mordse."taxflag" AS "order.service.taxflag", mordse."pos" AS "order.service.position",
 	mordse."mtime" AS "order.service.mtime", mordse."editor" AS "order.service.editor",
 	mordse."ctime" AS "order.service.ctime"
 FROM "mshop_order_service" mordse
 :joins
 WHERE :cond
 GROUP BY :columns :group
 	mordse."id", mordse."parentid", mordse."siteid", mordse."servid", mordse."type",
 	mordse."code", mordse."name", mordse."mediaurl", mordse."currencyid", mordse."price",
 	mordse."costs", mordse."rebate", mordse."tax", mordse."taxrate", mordse."taxflag",
 	mordse."pos", mordse."mtime", mordse."editor", mordse."ctime"
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/service/search/ansi

## submanagers

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


## transaction/aggregate/ansi

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/service/transaction/aggregate/ansi = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service_tx" mordsetx
 	:joins
 	WHERE :cond
 	GROUP BY mordsetx.id, :cols
 	ORDER BY mordsetx.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys
```

* Type: string - SQL statement for aggregating order items
* Since: 2023.01

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

* mshop/order/manager/service/transaction/insert/ansi
* mshop/order/manager/service/transaction/update/ansi
* mshop/order/manager/service/transaction/newid/ansi
* mshop/order/manager/service/transaction/delete/ansi
* mshop/order/manager/service/transaction/search/ansi
* mshop/order/manager/service/transaction/count/ansi

## transaction/aggregate/mysql

Counts the number of records grouped by the values in the key column and matched by the given criteria

```
mshop/order/manager/service/transaction/aggregate/mysql = 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service_tx" mordsetx
 	:joins
 	WHERE :cond
 	GROUP BY mordsetx.id, :cols
 	ORDER BY mordsetx.id DESC
 	LIMIT :size OFFSET :start
 ) AS list
 GROUP BY :keys
```

* Default: 
 SELECT :keys, :type("val") AS "value"
 FROM (
 	SELECT :acols, :type(:val) AS "val"
 	FROM "mshop_order_service_tx" mordsetx
 	:joins
 	WHERE :cond
 	GROUP BY mordsetx.id, :cols
 	ORDER BY mordsetx.id DESC
 	OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
 ) AS list
 GROUP BY :keys


See also:

* mshop/order/manager/service/transaction/aggregate/ansi

## transaction/count/ansi

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/service/transaction/count/ansi = 
 SELECT COUNT( DISTINCT mordsetx."id" ) AS "count"
 FROM "mshop_order_service_tx" mordsetx
 :joins
 WHERE :cond
```

* Type: string - SQL statement for counting items
* Since: 2023.01

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

* mshop/order/manager/service/transaction/insert/ansi
* mshop/order/manager/service/transaction/update/ansi
* mshop/order/manager/service/transaction/newid/ansi
* mshop/order/manager/service/transaction/delete/ansi
* mshop/order/manager/service/transaction/search/ansi

## transaction/count/mysql

Counts the number of records matched by the given criteria in the database

```
mshop/order/manager/service/transaction/count/mysql = 
 SELECT COUNT( DISTINCT mordsetx."id" ) AS "count"
 FROM "mshop_order_service_tx" mordsetx
 :joins
 WHERE :cond
```

* Default: 
 SELECT COUNT( DISTINCT mordsetx."id" ) AS "count"
 FROM "mshop_order_service_tx" mordsetx
 :joins
 WHERE :cond


See also:

* mshop/order/manager/service/transaction/count/ansi

## transaction/decorators/excludes

Excludes decorators added by the "common" option from the order base service transaction manager

```
mshop/order/manager/service/transaction/decorators/excludes = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2023.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to remove a decorator added via
"mshop/common/manager/decorators/default" before they are wrapped
around the order base service transaction manager.

```
 mshop/order/manager/service/transaction/decorators/excludes = array( 'decorator1' )
```

This would remove the decorator named "decorator1" from the list of
common decorators ("\Aimeos\MShop\Common\Manager\Decorator\*") added via
"mshop/common/manager/decorators/default" for the order base service transaction manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/transaction/decorators/global
* mshop/order/manager/service/transaction/decorators/local

## transaction/decorators/global

Adds a list of globally available decorators only to the order base service transaction manager

```
mshop/order/manager/service/transaction/decorators/global = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2023.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap global decorators
("\Aimeos\MShop\Common\Manager\Decorator\*") around the order base
service transaction manager.

```
 mshop/order/manager/service/transaction/decorators/global = array( 'decorator1' )
```

This would add the decorator named "decorator1" defined by
"\Aimeos\MShop\Common\Manager\Decorator\Decorator1" only to the order
base service transaction manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/transaction/decorators/excludes
* mshop/order/manager/service/transaction/decorators/local

## transaction/decorators/local

Adds a list of local decorators only to the order base service transaction manager

```
mshop/order/manager/service/transaction/decorators/local = Array
(
)
```

* Default: Array
(
)

* Type: array - List of decorator names
* Since: 2023.01

Decorators extend the functionality of a class by adding new aspects
(e.g. log what is currently done), executing the methods of the underlying
class only in certain conditions (e.g. only for logged in users) or
modify what is returned to the caller.

This option allows you to wrap local decorators
("\Aimeos\MShop\Order\Manager\Service\Transaction\Decorator\*")
around the order base service transaction manager.

```
 mshop/order/manager/service/transaction/decorators/local = array( 'decorator2' )
```

This would add the decorator named "decorator2" defined by
"\Aimeos\MShop\Order\Manager\Service\Transaction\Decorator\Decorator2"
only to the order base service transaction manager.

See also:

* mshop/common/manager/decorators/default
* mshop/order/manager/service/transaction/decorators/excludes
* mshop/order/manager/service/transaction/decorators/global

## transaction/delete/ansi

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/service/transaction/delete/ansi = 
 DELETE FROM "mshop_order_service_tx"
 WHERE :cond AND "siteid" LIKE ?
```

* Type: string - SQL statement for deleting items
* Since: 2023.01

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

* mshop/order/manager/service/transaction/insert/ansi
* mshop/order/manager/service/transaction/update/ansi
* mshop/order/manager/service/transaction/newid/ansi
* mshop/order/manager/service/transaction/search/ansi
* mshop/order/manager/service/transaction/count/ansi

## transaction/delete/mysql

Deletes the items matched by the given IDs from the database

```
mshop/order/manager/service/transaction/delete/mysql = 
 DELETE FROM "mshop_order_service_tx"
 WHERE :cond AND "siteid" LIKE ?
```

* Default: 
 DELETE FROM "mshop_order_service_tx"
 WHERE :cond AND "siteid" LIKE ?


See also:

* mshop/order/manager/service/transaction/delete/ansi

## transaction/insert/ansi

Inserts a new order record into the database table

```
mshop/order/manager/service/transaction/insert/ansi = 
 INSERT INTO "mshop_order_service_tx" ( :names
 	"parentid", "type", "currencyid", "price", "costs", "rebate", "tax", "taxflag",
 	"status", "config", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Type: string - SQL statement for inserting records
* Since: 2023.01

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

* mshop/order/manager/service/transaction/update/ansi
* mshop/order/manager/service/transaction/newid/ansi
* mshop/order/manager/service/transaction/delete/ansi
* mshop/order/manager/service/transaction/search/ansi
* mshop/order/manager/service/transaction/count/ansi

## transaction/insert/mysql

Inserts a new order record into the database table

```
mshop/order/manager/service/transaction/insert/mysql = 
 INSERT INTO "mshop_order_service_tx" ( :names
 	"parentid", "type", "currencyid", "price", "costs", "rebate", "tax", "taxflag",
 	"status", "config", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )
```

* Default: 
 INSERT INTO "mshop_order_service_tx" ( :names
 	"parentid", "type", "currencyid", "price", "costs", "rebate", "tax", "taxflag",
 	"status", "config", "mtime", "editor", "siteid", "ctime"
 ) VALUES ( :values
 	?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
 )


See also:

* mshop/order/manager/service/transaction/insert/ansi

## transaction/name

Class name of the used order base service transaction manager implementation

```
mshop/order/manager/service/transaction/name = Standard
```

* Default: Standard
* Type: string - Last part of the class name
* Since: 2023.01

Each default order base service transaction manager can be replaced by an alternative imlementation.
To use this implementation, you have to set the last part of the class
name as configuration value so the manager factory knows which class it
has to instantiate.

For example, if the name of the default class is

```
 \Aimeos\MShop\Order\Manager\Service\Transaction\Standard
```

and you want to replace it with your own version named

```
 \Aimeos\MShop\Order\Manager\Service\Transaction\Mytransaction
```

then you have to set the this configuration option:

```
 mshop/order/manager/service/transaction/name = Mytransaction
```

The value is the last part of your own class name and it's case sensitive,
so take care that the configuration value is exactly named like the last
part of the class name.

The allowed characters of the class name are A-Z, a-z and 0-9. No other
characters are possible! You should always start the last part of the class
name with an upper case character and continue only with lower case characters
or numbers. Avoid chamel case names like "MyTransaction"!


## transaction/newid/ansi

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/service/transaction/newid/ansi = 
```

* Type: string - SQL statement for retrieving the last inserted record ID
* Since: 2023.01

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

* mshop/order/manager/service/transaction/insert/ansi
* mshop/order/manager/service/transaction/update/ansi
* mshop/order/manager/service/transaction/delete/ansi
* mshop/order/manager/service/transaction/search/ansi
* mshop/order/manager/service/transaction/count/ansi

## transaction/newid/mysql

Retrieves the ID generated by the database when inserting a new record

```
mshop/order/manager/service/transaction/newid/mysql = SELECT LAST_INSERT_ID()
```


See also:

* mshop/order/manager/service/transaction/newid/ansi

## transaction/search/ansi

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/transaction/search/ansi = 
 SELECT :columns
 	mordsetx."id" AS "order.service.transaction.id", mordsetx."siteid" AS "order.service.transaction.siteid",
 	mordsetx."parentid" AS "order.service.transaction.parentid", mordsetx."type" AS "order.service.transaction.type",
 	mordsetx."currencyid" AS "order.service.transaction.currencyid", mordsetx."price" AS "order.service.transaction.price",
 	mordsetx."costs" AS "order.service.transaction.costs", mordsetx."rebate" AS "order.service.transaction.rebate",
 	mordsetx."tax" AS "order.service.transaction.taxvalue", mordsetx."taxflag" AS "order.service.transaction.taxflag",
 	mordsetx."config" AS "order.service.transaction.config", mordsetx."status" AS "order.service.transaction.status",
 	mordsetx."mtime" AS "order.service.transaction.mtime", mordsetx."ctime" AS "order.service.transaction.ctime",
 	mordsetx."editor" AS "order.service.transaction.editor"
 FROM "mshop_order_service_tx" mordsetx
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY
```

* Type: string - SQL statement for searching items
* Since: 2023.01

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

* mshop/order/manager/service/transaction/insert/ansi
* mshop/order/manager/service/transaction/update/ansi
* mshop/order/manager/service/transaction/newid/ansi
* mshop/order/manager/service/transaction/delete/ansi
* mshop/order/manager/service/transaction/count/ansi

## transaction/search/mysql

Retrieves the records matched by the given criteria in the database

```
mshop/order/manager/service/transaction/search/mysql = 
 SELECT :columns
 	mordsetx."id" AS "order.service.transaction.id", mordsetx."siteid" AS "order.service.transaction.siteid",
 	mordsetx."parentid" AS "order.service.transaction.parentid", mordsetx."type" AS "order.service.transaction.type",
 	mordsetx."currencyid" AS "order.service.transaction.currencyid", mordsetx."price" AS "order.service.transaction.price",
 	mordsetx."costs" AS "order.service.transaction.costs", mordsetx."rebate" AS "order.service.transaction.rebate",
 	mordsetx."tax" AS "order.service.transaction.taxvalue", mordsetx."taxflag" AS "order.service.transaction.taxflag",
 	mordsetx."config" AS "order.service.transaction.config", mordsetx."status" AS "order.service.transaction.status",
 	mordsetx."mtime" AS "order.service.transaction.mtime", mordsetx."ctime" AS "order.service.transaction.ctime",
 	mordsetx."editor" AS "order.service.transaction.editor"
 FROM "mshop_order_service_tx" mordsetx
 :joins
 WHERE :cond
 ORDER BY :order
 LIMIT :size OFFSET :start
```

* Default: 
 SELECT :columns
 	mordsetx."id" AS "order.service.transaction.id", mordsetx."siteid" AS "order.service.transaction.siteid",
 	mordsetx."parentid" AS "order.service.transaction.parentid", mordsetx."type" AS "order.service.transaction.type",
 	mordsetx."currencyid" AS "order.service.transaction.currencyid", mordsetx."price" AS "order.service.transaction.price",
 	mordsetx."costs" AS "order.service.transaction.costs", mordsetx."rebate" AS "order.service.transaction.rebate",
 	mordsetx."tax" AS "order.service.transaction.taxvalue", mordsetx."taxflag" AS "order.service.transaction.taxflag",
 	mordsetx."config" AS "order.service.transaction.config", mordsetx."status" AS "order.service.transaction.status",
 	mordsetx."mtime" AS "order.service.transaction.mtime", mordsetx."ctime" AS "order.service.transaction.ctime",
 	mordsetx."editor" AS "order.service.transaction.editor"
 FROM "mshop_order_service_tx" mordsetx
 :joins
 WHERE :cond
 ORDER BY :order
 OFFSET :start ROWS FETCH NEXT :size ROWS ONLY


See also:

* mshop/order/manager/service/transaction/search/ansi

## transaction/submanagers

List of manager names that can be instantiated by the order base service transaction manager

```
mshop/order/manager/service/transaction/submanagers = Array
(
)
```

* Default: Array
(
)

* Type: array - List of sub-manager names
* Since: 2023.01

Managers provide a generic interface to the underlying storage.
Each manager has or can have sub-managers caring about particular
aspects. Each of these sub-managers can be instantiated by its
parent manager using the getSubManager() method.

The search keys from sub-managers can be normally used in the
manager as well. It allows you to search for items of the manager
using the search keys of the sub-managers to further limit the
retrieved list of items.


## transaction/update/ansi

Updates an existing order record in the database

```
mshop/order/manager/service/transaction/update/ansi = 
```

* Type: string - SQL statement for updating records
* Since: 2023.01

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

* mshop/order/manager/service/transaction/insert/ansi
* mshop/order/manager/service/transaction/newid/ansi
* mshop/order/manager/service/transaction/delete/ansi
* mshop/order/manager/service/transaction/search/ansi
* mshop/order/manager/service/transaction/count/ansi

## transaction/update/mysql

Updates an existing order record in the database

```
mshop/order/manager/service/transaction/update/mysql = 
```


See also:

* mshop/order/manager/service/transaction/update/ansi

## update/ansi

Updates an existing order record in the database

```
mshop/order/manager/service/update/ansi = 
```

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

## update/mysql

Updates an existing order record in the database

```
mshop/order/manager/service/update/mysql = 
```


See also:

* mshop/order/manager/service/update/ansi

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
mshop/order/manager/status/newid/ansi = 
```

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
    [0] => address
    [1] => coupon
    [2] => product
    [3] => service
    [4] => status
)
```

* Default: Array
(
    [0] => address
    [1] => coupon
    [2] => product
    [3] => service
    [4] => status
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
 	"invoiceno" = ?, "channel" = ?, "datepayment" = ?, "datedelivery" = ?,
 	"statusdelivery" = ?, "statuspayment" = ?, "relatedid" = ?,
 	"customerid" = ?, "sitecode" = ?, "langid" = ?, "currencyid" = ?,
 	"price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxflag" = ?,
 	"customerref" = ?, "comment" = ?, "mtime" = ?, "editor" = ?
 		WHERE "siteid" LIKE ? AND "id" = ?
```

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
 	"invoiceno" = ?, "channel" = ?, "datepayment" = ?, "datedelivery" = ?,
 	"statusdelivery" = ?, "statuspayment" = ?, "relatedid" = ?,
 	"customerid" = ?, "sitecode" = ?, "langid" = ?, "currencyid" = ?,
 	"price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxflag" = ?,
 	"customerref" = ?, "comment" = ?, "mtime" = ?, "editor" = ?
 		WHERE "siteid" LIKE ? AND "id" = ?
```

* Default: 
 UPDATE "mshop_order"
 SET :names
 	"invoiceno" = ?, "channel" = ?, "datepayment" = ?, "datedelivery" = ?,
 	"statusdelivery" = ?, "statuspayment" = ?, "relatedid" = ?,
 	"customerid" = ?, "sitecode" = ?, "langid" = ?, "currencyid" = ?,
 	"price" = ?, "costs" = ?, "rebate" = ?, "tax" = ?, "taxflag" = ?,
 	"customerref" = ?, "comment" = ?, "mtime" = ?, "editor" = ?
WHERE "siteid" LIKE ? AND "id" = ?


See also:

* mshop/order/manager/update/ansi